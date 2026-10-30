"""Tests de tools/musiques.py : les musiques de lancement installées depuis leurs archives, puis
choisies selon le but, le support et la durée de la vidéo.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))
import musiques  # noqa: E402

# Les vraies archives, chez l'éditeur seulement (elles ne sont jamais dans le dépôt).
LIVRAISON = Path.home() / "code" / "pack-musique" / "livraison" / "1.0.0"


def morceau(ambiance: str, n: int, entree: float, duree: float = 120.0, tempo: float = 120.0, recale: bool = True) -> dict:
    return {"fichier": f"{ambiance}/{ambiance}-{n:02d}-test.mp3", "ambiance": musiques.AMBIANCES[ambiance],
            "style": f"style {n}", "usage_conseille": "test", "tempo_bpm": tempo, "recale_a_120": recale,
            "premier_temps_s": 0.0, "entree_franche_s": entree, "duree_s": duree}


def archive(chemin: Path, ambiance: str, liste: list[dict], racine: str = "musiques-lancement/", extra: dict | None = None) -> Path:
    """Une archive comme celles de la formation : <racine><ambiance>/*.mp3, sa fiche, la licence."""
    with zipfile.ZipFile(chemin, "w") as z:
        z.writestr(f"{racine}{ambiance}/catalog.json", json.dumps({"version": "1.0.0", "ambiance": musiques.AMBIANCES[ambiance],
                                                                  "morceaux": liste}))
        for m in liste:
            z.writestr(racine + m["fichier"], b"ID3" + m["fichier"].encode() * 50)
        z.writestr(f"{racine}LICENCE.md", "# Licence")
        for nom, donnees in (extra or {}).items():
            z.writestr(nom, donnees)
    return chemin


BANQUE = {
    "lancement-energique": [morceau("lancement-energique", 1, 17.5, 149, 125), morceau("lancement-energique", 2, 3.0, 118, 131)],
    "montee-cinematique": [morceau("montee-cinematique", 1, 8.5, 129)],
    "tech-minimale": [morceau("tech-minimale", 1, 16.5, 148, 131), morceau("tech-minimale", 2, 32.0, 60)],
    "court-percutant": [morceau("court-percutant", 1, 7.2, 124, 131)],
    "premium-calme": [morceau("premium-calme", 1, 14.7, 120, 111), morceau("premium-calme", 2, 16.0, 133, 98, recale=False)],
}


class Installation(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.racine = self.tmp / "produit"
        self.racine.mkdir()
        self.dl = self.tmp / "Downloads"
        self.dl.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def zips(self, *ambiances: str) -> list[Path]:
        return [archive(self.dl / f"musiques-{a}.zip", a, BANQUE[a]) for a in ambiances]

    def test_une_puis_les_autres_s_ajoutent(self):
        res = musiques.installer(self.racine, self.zips("tech-minimale"))
        self.assertEqual(res["ambiances"], {"tech-minimale": 2})
        self.assertIn("Montée cinématique", res["absentes"])
        res = musiques.installer(self.racine, self.zips(*BANQUE))
        self.assertEqual(res["total"], 8)
        self.assertEqual(res["absentes"], [])
        self.assertTrue((self.racine / "assets/musiques/LICENCE.md").is_file())
        self.assertTrue((self.racine / "assets/musiques/tech-minimale/catalog.json").is_file())

    def test_refaire_ne_change_rien(self):
        musiques.installer(self.racine, self.zips(*BANQUE))
        res = musiques.installer(self.racine, self.zips(*BANQUE))
        self.assertEqual(res["ecrits"], 0)
        self.assertEqual(res["retires"], 0)

    def test_nouvelle_version_retire_les_morceaux_disparus(self):
        musiques.installer(self.racine, self.zips("lancement-energique"))
        archive(self.dl / "musiques-lancement-energique.zip", "lancement-energique", BANQUE["lancement-energique"][:1])
        res = musiques.installer(self.racine, [self.dl / "musiques-lancement-energique.zip"])
        self.assertEqual(res["retires"], 1)
        self.assertEqual(res["ambiances"], {"lancement-energique": 1})

    def test_dossier_decompresse_par_safari(self):
        # Safari décompresse tout seul : « musiques-lancement 2/tech-minimale/… », sans l'archive.
        dossier = self.dl / "musiques-lancement 2"
        with zipfile.ZipFile(self.zips("tech-minimale")[0]) as z:
            z.extractall(self.tmp / "x")
        (self.tmp / "x" / "musiques-lancement").rename(dossier)
        (self.dl / "musiques-tech-minimale.zip").unlink()
        sources = musiques.sources_par_defaut(self.dl)
        self.assertEqual(sources, [dossier])
        self.assertEqual(musiques.installer(self.racine, sources)["ambiances"], {"tech-minimale": 2})

    def test_sources_par_defaut_ignore_le_reste_et_garde_les_doublons_du_navigateur(self):
        self.zips("premium-calme")
        (self.dl / "musiques-premium-calme.zip").rename(self.dl / "musiques-premium-calme (1).zip")
        (self.dl / "musiques-mariage").mkdir()
        (self.dl / "musiques-mariage" / "valse.mp3").write_bytes(b"x")
        (self.dl / "photos.zip").write_bytes(b"x")
        noms = [p.name for p in musiques.sources_par_defaut(self.dl)]
        self.assertCountEqual(noms, ["musiques-premium-calme (1).zip", "musiques-mariage"])
        res = musiques.installer(self.racine, musiques.sources_par_defaut(self.dl))
        self.assertEqual(res["ambiances"], {"premium-calme": 2})
        self.assertEqual(len(res["erreurs"]), 1)   # le dossier personnel, ignoré et signalé

    def test_rien_a_installer(self):
        with self.assertRaisesRegex(musiques.ErreurMusiques, "aucune archive"):
            musiques.installer(self.racine, [])

    def test_acces_refuse_a_telechargements(self):
        """macOS protège Téléchargements : l'app de l'assistant doit y avoir été autorisée. Un message à
        suivre, jamais une PermissionError brute."""
        zip_, = self.zips("tech-minimale")
        refus = PermissionError(1, "Operation not permitted")
        with mock.patch.object(Path, "iterdir", side_effect=refus):
            with self.assertRaisesRegex(musiques.ErreurMusiques, "glisse le fichier ici"):
                musiques.sources_par_defaut(self.dl)
        with mock.patch("zipfile.ZipFile", side_effect=refus):
            with self.assertRaisesRegex(musiques.ErreurMusiques, "glisse le fichier ici"):
                musiques.installer(self.racine, [zip_])
        self.assertEqual(musiques.acces_refuse(self.dl, "darwin"),
                         f"macOS refuse l'accès à {self.dl}. Autorise l'accès dans Réglages Système > Confidentialité "
                         "et sécurité > Fichiers et dossiers, ou glisse le fichier ici.")
        self.assertIn("glisse le fichier ici", musiques.acces_refuse(self.dl, "win32"))

    def test_archive_abimee_ou_etrangere(self):
        (self.dl / "musiques-x.zip").write_bytes(b"pas un zip")
        with self.assertRaisesRegex(musiques.ErreurMusiques, "ZIP lisible"):
            musiques.installer(self.racine, [self.dl / "musiques-x.zip"])
        sans_morceau = archive(self.dl / "musiques-y.zip", "tech-minimale", BANQUE["tech-minimale"])
        with zipfile.ZipFile(sans_morceau) as z:
            contenu = {n: z.read(n) for n in z.namelist() if not n.endswith("02-test.mp3")}
        with zipfile.ZipFile(sans_morceau, "w") as z:
            for n, d in contenu.items():
                z.writestr(n, d)
        with self.assertRaisesRegex(musiques.ErreurMusiques, "absent"):
            musiques.installer(self.racine, [sans_morceau])

    def test_chemins_dangereux_refuses(self):
        piege = [dict(morceau("tech-minimale", 1, 10), fichier="../../evil.mp3")]
        with self.assertRaisesRegex(musiques.ErreurMusiques, "invalide"):
            musiques.installer(self.racine, [archive(self.dl / "musiques-p.zip", "tech-minimale", piege)])
        autre = [dict(morceau("tech-minimale", 1, 10), fichier="premium-calme/x.mp3")]
        with self.assertRaisesRegex(musiques.ErreurMusiques, "invalide"):
            musiques.installer(self.racine, [archive(self.dl / "musiques-q.zip", "tech-minimale", autre)])
        # Un fichier hors fiche (script, chemin remontant) n'est jamais copié.
        musiques.installer(self.racine, [archive(self.dl / "musiques-r.zip", "court-percutant", BANQUE["court-percutant"],
                                                 extra={"musiques-lancement/../../x.sh": b"rm", "musiques-lancement/run.py": b"x"})])
        copies = sorted(p.relative_to(self.racine).as_posix() for p in self.racine.rglob("*") if p.is_file())
        self.assertEqual(copies, ["assets/musiques/LICENCE.md", "assets/musiques/court-percutant/catalog.json",
                                  "assets/musiques/court-percutant/court-percutant-01-test.mp3"])
        self.assertFalse((self.tmp / "x.sh").exists())

    @unittest.skipUnless(LIVRAISON.is_dir(), "archives de l'éditeur absentes")
    def test_vraies_archives(self):
        res = musiques.installer(self.racine, sorted(LIVRAISON.glob("musiques-*.zip")))
        self.assertEqual(res["total"], 17)
        self.assertEqual(res["absentes"], [])
        self.assertEqual(res["ambiances"], {"lancement-energique": 7, "montee-cinematique": 3, "tech-minimale": 4,
                                            "court-percutant": 1, "premium-calme": 2})

    @unittest.skipUnless((LIVRAISON / "complet" / "musiques-lancement.zip").is_file(), "fichier unique absent")
    def test_vrai_fichier_unique(self):
        """Le fichier unique de la formation (depuis le 30/10/2026) : les 17 d'un coup, renommé « (1) » par
        le navigateur compris."""
        copie = self.dl / "musiques-lancement (1).zip"
        copie.write_bytes((LIVRAISON / "complet" / "musiques-lancement.zip").read_bytes())
        self.assertEqual(musiques.sources_par_defaut(self.dl), [copie])
        res = musiques.installer(self.racine, [copie])
        self.assertEqual((res["total"], res["absentes"]), (17, []))


class Choix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        tmp = Path(cls._tmp.name)
        cls.racine = tmp / "produit"
        cls.racine.mkdir()
        musiques.installer(cls.racine, [archive(tmp / f"musiques-{a}.zip", a, BANQUE[a]) for a in BANQUE])

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def ids(self, **k) -> list[str]:
        return [m["id"] for m in musiques.choisir(self.racine, **k)]

    def test_le_but_donne_l_ambiance(self):
        self.assertTrue(self.ids(objectif="nouveaute", support="reel", duree=25)[0].startswith("montee-cinematique"))
        self.assertTrue(self.ids(objectif="fonctionnalite", support="page", duree=40)[0].startswith("tech-minimale"))
        self.assertTrue(self.ids(objectif="preuve", support="reel", duree=30)[0].startswith("premium-calme"))
        self.assertTrue(self.ids(objectif="lancement", support="page", duree=60)[0].startswith("lancement-energique"))

    def test_format_court_pour_vendre_passe_au_percutant(self):
        self.assertEqual(self.ids(objectif="vente", support="reel", duree=30)[0], "court-percutant-01-test")
        self.assertEqual(self.ids(objectif="vente", support="page", duree=30)[0], "lancement-energique-01-test")

    def test_trop_court_ecarte(self):
        # tech-minimale-02 : 60 s, batterie à 32 s → 28 s après l'entrée, pas assez pour 40 s de vidéo.
        self.assertNotIn("tech-minimale-02-test", self.ids(objectif="fonctionnalite", support="page", duree=40, a=8))
        self.assertIn("tech-minimale-02-test", self.ids(objectif="fonctionnalite", support="page", duree=20, a=8))

    def test_intro_courte_passe_derriere(self):
        # lancement-02 : batterie à 3 s, la vidéo l'attend à 8 s : il démarrerait 5 s en retard.
        choix = musiques.choisir(self.racine, objectif="lancement", support="page", duree=40, a=8)
        self.assertEqual(choix[0]["id"], "lancement-energique-01-test")
        tardif = next(m for m in choix if m["id"] == "lancement-energique-02-test")
        self.assertTrue(any("après le début" in r for r in tardif["raisons"]))

    def test_ambiance_imposee_et_autres(self):
        self.assertEqual(self.ids(ambiance="premium-calme", duree=30), ["premium-calme-01-test", "premium-calme-02-test"])
        premiers = set(self.ids(objectif="vente", support="reel", duree=30))
        autres = set(self.ids(objectif="vente", support="reel", duree=30, exclure=premiers))
        self.assertTrue(autres)
        self.assertFalse(premiers & autres)

    def test_recale_a_120_prefere(self):
        self.assertEqual(self.ids(ambiance="premium-calme", duree=30)[0], "premium-calme-01-test")

    def test_varie_selon_les_videos_deja_faites(self):
        projet = self.racine / "videos" / "Lancement · 2026-10-15" / "Lancement · Page de vente"
        (projet / "assets" / "audio").mkdir(parents=True)
        (projet / "assets" / "audio" / "SOURCE.md").write_text(
            "- `x.mp3` : « style 1 », musiques de lancement, lancement-energique-01-test (ambiance Lancement énergique)")
        try:
            autre = self.racine / "videos" / "Autre · 2026-10-16" / "Autre · Page de vente"
            self.assertEqual(musiques.deja_utilises(self.racine), {"lancement-energique-01-test": 1})
            self.assertEqual(musiques.deja_utilises(self.racine, sauf=projet), {})
            choix = musiques.choisir(self.racine, objectif="lancement", support="page", duree=40, projet=autre)
            premier = next(m for m in choix if m["id"] == "lancement-energique-01-test")
            self.assertIn("déjà dans 1 de tes vidéos", premier["raisons"])
        finally:
            shutil.rmtree(self.racine / "videos")

    def test_jamais_plus_de_deux_d_une_ambiance_sur_trois(self):
        choix = musiques.choisir(self.racine, objectif="lancement", support="page", duree=30)
        self.assertLessEqual(sum(m["cle"] == "lancement-energique" for m in choix), 2)

    def test_ambiance_dite_par_le_client(self):
        self.assertEqual(musiques.ambiance_demandee("Tech minimale"), "tech-minimale")
        self.assertEqual(musiques.ambiance_demandee("une musique plus premium"), "premium-calme")
        self.assertEqual(musiques.ambiance_demandee("Montée cinématique"), "montee-cinematique")
        self.assertEqual(musiques.ambiance_demandee("court-percutant"), "court-percutant")
        self.assertIsNone(musiques.ambiance_demandee("jazz"))

    def test_page_d_ecoute_demarre_avant_la_batterie(self):
        m = next(x for x in musiques.morceaux(self.racine) if x["id"] == "tech-minimale-01-test")
        self.assertTrue(musiques.page(m)["url"].endswith("#t=8.5"))


class Commande(unittest.TestCase):
    """La commande de bout en bout, dans une copie du dossier (les musiques n'y sont jamais versionnées)."""

    def test_installer_choisir_prendre(self):
        with tempfile.TemporaryDirectory() as t:
            tmp = Path(t)
            copie = tmp / "Publicitaire IA"
            copie.mkdir()
            for nom in ("produit.json", "VERSION", "tools", "templates", "assets", "hyperframes.json"):
                src = RACINE / nom
                if src.is_dir():
                    shutil.copytree(src, copie / nom, ignore=shutil.ignore_patterns("musiques", "__pycache__"))
                elif src.is_file():
                    shutil.copy2(src, copie / nom)
            dl = tmp / "home" / "Downloads"
            dl.mkdir(parents=True)
            for a in BANQUE:
                archive(dl / f"musiques-{a}.zip", a, BANQUE[a])
            env = {**os.environ, "HOME": str(tmp / "home"), "USERPROFILE": str(tmp / "home")}
            outil = [sys.executable, str(copie / "tools" / "studio_motion.py")]
            r = subprocess.run(outil + ["musiques", "installer"], cwd=copie, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("8 musiques de lancement", r.stdout)
            r = subprocess.run(outil + ["nouvelle", "Test", "--objectif", "vente", "--videos", "reel,section"],
                               cwd=copie, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            reel = next((copie / "videos").glob("*/* · Reel"))
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue(r.stdout.startswith("1. court-percutant-01-test"), r.stdout)
            self.assertTrue((reel / "work" / "ecoute-musiques.html").is_file())
            r = subprocess.run(outil + ["musiques", "prendre", "2"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            source = (reel / "assets" / "audio" / "SOURCE.md").read_text(encoding="utf-8")
            self.assertIn("musiques de lancement, lancement-energique-01-test", source)
            self.assertTrue((reel / "assets" / "audio" / "lancement-energique-01-test.mp3").is_file())
            section = next((copie / "videos").glob("*/* · Section de page"))
            r = subprocess.run(outil + ["musiques", "choisir"], cwd=section, env=env, capture_output=True, text=True)
            self.assertIn("muette", r.stdout)


if __name__ == "__main__":
    unittest.main()
