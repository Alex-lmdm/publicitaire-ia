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


def fausse_fiche_mixkit(dossier: Path, n: int = 2) -> Path:
    """Une fiche Mixkit dont les adresses sont des fichiers locaux (file://) : rien ne part sur le réseau."""
    dossier.mkdir(parents=True, exist_ok=True)
    noms = ["un", "deux", "trois"][:n]
    liste = []
    for i, nom in enumerate(noms):
        source = dossier / f"source-{nom}.mp3"
        source.write_bytes(b"ID3" + nom.encode() * 100)
        liste.append({"id": f"mixkit-{nom}", "titre": nom.title(), "fichier": f"mixkit/mixkit-{nom}.mp3",
                      "url": source.resolve().as_uri(), "ambiance": ["tech-minimale", "court-percutant", "premium-calme"][i],
                      "style": f"style {nom}", "usage_conseille": "test", "tempo_bpm": 120.0, "recale_a_120": True,
                      "premier_temps_s": 0.0, "entree_franche_s": None if i == 0 else 4.0, "duree_s": 120.0})
    fiche = dossier / "musiques-mixkit.json"
    fiche.write_text(json.dumps({"morceaux": liste}), encoding="utf-8")
    return fiche


class Mixkit(unittest.TestCase):
    """Les 18 de Mixkit : jamais livrées, téléchargées chez le client depuis Mixkit."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.racine = self.tmp / "produit"
        self.racine.mkdir()
        patcher = mock.patch.dict(os.environ, {"PIA_MIXKIT_FICHE": str(fausse_fiche_mixkit(self.tmp / "mk"))})
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        self._tmp.cleanup()

    def test_la_vraie_fiche(self):
        with mock.patch.dict(os.environ, {"PIA_MIXKIT_FICHE": ""}):
            liste = musiques.mixkit()
        self.assertEqual(len(liste), 18)
        self.assertEqual(len({m["id"] for m in liste}), 18)
        for m in liste:
            self.assertIn(m["ambiance"], musiques.AMBIANCES, m["id"])
            self.assertTrue(m["url"].startswith("https://assets.mixkit.co/music/"), m["id"])
            self.assertEqual(m["fichier"], f"mixkit/{m['id']}.mp3")
            self.assertGreater(m["duree_s"], 60, m["id"])

    def test_telecharge_ce_qui_manque_puis_rien(self):
        res = musiques.installer_mixkit(self.racine)
        self.assertEqual((res["ecrits"], res["identiques"], res["erreurs"]), (2, 0, []))
        res = musiques.installer_mixkit(self.racine)
        self.assertEqual((res["ecrits"], res["identiques"]), (0, 2))
        e = musiques.etat(self.racine)
        self.assertEqual((e["total"], e["lancement"], e["mixkit"], e["mixkit_attendus"]), (2, 0, 2, 2))
        self.assertTrue(e["installe"])

    def test_une_absente_n_arrete_pas_les_autres(self):
        (self.tmp / "mk" / "source-un.mp3").unlink()
        res = musiques.installer_mixkit(self.racine)
        self.assertEqual(res["ecrits"], 1)
        self.assertEqual(len(res["erreurs"]), 1)
        self.assertFalse((self.racine / "assets/musiques/mixkit/mixkit-un.mp3.part").exists())

    def test_choisies_comme_les_autres_avec_leur_licence(self):
        musiques.installer_mixkit(self.racine)
        liste = {m["id"]: m for m in musiques.morceaux(self.racine)}
        self.assertIn("Mixkit", liste["mixkit-un"]["licence"])
        self.assertEqual(liste["mixkit-un"]["nom_ambiance"], "Tech minimale")
        # Sans entrée franche, le premier temps est calé au début : jamais « démarre après le début ».
        choix = musiques.choisir(self.racine, objectif="fonctionnalite", support="page", duree=30, a=8)
        un = next(m for m in choix if m["id"] == "mixkit-un")
        self.assertEqual(un["raisons"], ["Tech minimale"])
        self.assertIn("batterie dès le début", musiques.ligne(un))
        self.assertNotIn("#t=", musiques.page(un)["url"])
        # Trop court pour toute la vidéo : écarté.
        self.assertNotIn("mixkit-un", {m["id"] for m in musiques.choisir(self.racine, objectif="fonctionnalite", duree=125)})


class LienDeLaFormation(unittest.TestCase):
    """Les 17 par le lien personnel de la phrase de la formation."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.racine = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_refuse_une_autre_adresse(self):
        for lien in ("http://app.lemondedumarketing.fr/x", "https://exemple.com/musiques.zip", "file:///etc/passwd"):
            with self.assertRaisesRegex(musiques.ErreurMusiques, "pas celui de ta formation"):
                musiques.telecharger_pack(self.racine, lien, ouvrir=mock.Mock(side_effect=AssertionError("jamais appelé")))

    def test_lien_expire(self):
        import urllib.error
        refus = urllib.error.HTTPError("https://app.lemondedumarketing.fr/x", 404, "Not Found", {}, None)
        with self.assertRaisesRegex(musiques.ErreurMusiques, "expiré"):
            musiques.telecharger_pack(self.racine, "https://app.lemondedumarketing.fr/api/formations/musiques-lancement/download?cle=x",
                                      ouvrir=mock.Mock(side_effect=refus))
        self.assertEqual(list((self.racine / ".cache" / "musiques").glob("*")), [])

    def test_telecharge_puis_s_installe(self):
        import io
        zip_ = archive(self.racine / "source.zip", "premium-calme", BANQUE["premium-calme"])
        reponse = mock.MagicMock()
        reponse.__enter__.return_value = io.BytesIO(zip_.read_bytes())
        ouvrir = mock.Mock(return_value=reponse)
        cible = musiques.telecharger_pack(self.racine, "https://app.lemondedumarketing.fr/api/formations/musiques-lancement/download?cle=abc", ouvrir)
        self.assertEqual(ouvrir.call_args[0][0].full_url, "https://app.lemondedumarketing.fr/api/formations/musiques-lancement/download?cle=abc")
        res = musiques.installer(self.racine, [cible])
        self.assertEqual(res["ambiances"], {"premium-calme": 2})


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

    def test_seulement_un_dossier_a_lui_dans_telechargements(self):
        """Essai du 06/11/2026 : « musiques-pub-a-ecouter » (ses MP3 à lui) arrêtait la mise à jour, les 17
        déjà installées. Trouvé dans Téléchargements, il s'ignore ; donné par le client, il est refusé."""
        (self.dl / "musiques-pub-a-ecouter").mkdir()
        (self.dl / "musiques-pub-a-ecouter" / "musique-1-stomp.mp3").write_bytes(b"x")
        musiques.installer(self.racine, self.zips("tech-minimale"))
        (self.dl / "musiques-tech-minimale.zip").unlink()
        sources = musiques.sources_par_defaut(self.dl)
        res = musiques.installer(self.racine, sources, trouvees=True)
        self.assertEqual((res["ambiances"], res["ecrits"], len(res["erreurs"])), ({"tech-minimale": 2}, 0, 1))
        with self.assertRaisesRegex(musiques.ErreurMusiques, "pas des musiques de lancement"):
            musiques.installer(self.racine, sources)
        (self.dl / "musiques-x.zip").write_bytes(b"pas un zip")   # une archive abîmée se signale toujours
        with self.assertRaisesRegex(musiques.ErreurMusiques, "ZIP lisible"):
            musiques.installer(self.racine, musiques.sources_par_defaut(self.dl), trouvees=True)

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

    def test_page_avec_voix_off_prend_les_ambiances_feutrees(self):
        """Essai du 03/11/2026 : une vidéo de page avec voix off passe sous un argument qu'on écoute."""
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d) / "Vente · Page de vente"
            (projet / "work").mkdir(parents=True)
            (projet / "work" / "voix.txt").write_text("Tu veux des vidéos qui vendent ton offre ?")
            premier = self.ids(objectif="vente", support="page", duree=20, a=8, projet=projet)[0]
            self.assertTrue(premier.startswith(("tech-minimale", "premium-calme")), premier)
            sans_voix = self.ids(objectif="vente", support="page", duree=20, a=8, projet=Path(d) / "vide")[0]
            self.assertTrue(sans_voix.startswith("lancement-energique"), sans_voix)

    def test_le_style_donne_son_ambiance(self):
        """Revue du 03/11/2026 : la page des styles proposait « Dubstep puissant » avec le style 5, calme."""
        premier = self.ids(objectif="vente", support="reel", duree=25, preferees=["premium-calme", "tech-minimale"])[0]
        self.assertTrue(premier.startswith("premium-calme"), premier)
        with tempfile.TemporaryDirectory() as d:   # une voix off sur une page passe toujours devant le style
            projet = Path(d) / "Vente · Page de vente"
            (projet / "work").mkdir(parents=True)
            (projet / "work" / "voix.txt").write_text("Une voix.")
            premier = self.ids(objectif="vente", support="page", duree=20, a=8, projet=projet, preferees=["lancement-energique"])[0]
            self.assertTrue(premier.startswith(("tech-minimale", "premium-calme")), premier)

    def test_entree_franche_sur_le_pivot_passe_devant(self):
        """Essai du 03/11/2026 : à note égale, le tri par nom faisait passer Mixkit (batterie dès le
        début) devant les morceaux maison dont la batterie peut entrer sur le pivot."""
        choix = musiques.choisir(self.racine, ambiance="tech-minimale", duree=20, a=8)
        calables = [m for m in choix if m.get("entree_franche_s") is not None and float(m["entree_franche_s"]) >= 8]
        self.assertTrue(calables)
        self.assertEqual(choix[0]["id"], calables[0]["id"])

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
            index_styles = Path(".claude") / "skills" / "studio" / "styles" / "README.md"
            (copie / index_styles).parent.mkdir(parents=True)
            shutil.copy2(RACINE / index_styles, copie / index_styles)
            dl = tmp / "home" / "Downloads"
            dl.mkdir(parents=True)
            for a in BANQUE:
                archive(dl / f"musiques-{a}.zip", a, BANQUE[a])
            fiche_mixkit = fausse_fiche_mixkit(tmp / "mixkit", n=1)
            env = {**os.environ, "HOME": str(tmp / "home"), "USERPROFILE": str(tmp / "home"), "PIA_MIXKIT_FICHE": str(fiche_mixkit)}
            outil = [sys.executable, str(copie / "tools" / "studio_motion.py")]
            r = subprocess.run(outil + ["musiques", "installer"], cwd=copie, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("9 musiques de lancement", r.stdout)
            self.assertIn("8 de la formation", r.stdout)
            self.assertIn("1/1 de Mixkit", r.stdout)
            self.assertTrue((copie / "assets" / "musiques" / "mixkit" / "mixkit-un.mp3").is_file())
            for a in BANQUE:   # la mise à jour : les archives rangées, un dossier « musiques-… » à lui reste
                (dl / f"musiques-{a}.zip").unlink()
            (dl / "musiques-pub-a-ecouter").mkdir()
            (dl / "musiques-pub-a-ecouter" / "musique-1-stomp.mp3").write_bytes(b"x")
            r = subprocess.run(outil + ["musiques", "installer"], cwd=copie, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("(ignoré : musiques-pub-a-ecouter", r.stdout)
            self.assertIn("8 de la formation", r.stdout)
            r = subprocess.run(outil + ["nouvelle", "Test", "--objectif", "vente", "--videos", "reel,section"],
                               cwd=copie, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            reel = next((copie / "videos").glob("*/* · Reel"))
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue(r.stdout.startswith("1. court-percutant-01-test"), r.stdout)
            self.assertIn("ton conseil : 0 « Sur mesure »", r.stdout)                     # le style maison, par défaut
            page = reel / "work" / "ecoute-musiques.html"
            self.assertEqual(page.read_text(encoding="utf-8").count("<video "), 10)          # le style se choisit ici
            self.assertEqual(page.read_text(encoding="utf-8").count("Mon conseil"), 1)
            self.assertEqual(page.read_text(encoding="utf-8").count("<audio "), 3)
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30", "--style", "3"], cwd=reel, env=env,
                               capture_output=True, text=True)
            self.assertIn("ton conseil : 3 « Verre sombre »", r.stdout)
            self.assertEqual(page.read_text(encoding="utf-8").count("Mon conseil"), 1)
            r = subprocess.run(outil + ["musiques", "choisir", "--style", "10"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("pas de style 10 : de 0 à 9", r.stderr)
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30", "--sans-styles"], cwd=reel, env=env,
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertNotIn("<video ", page.read_text(encoding="utf-8"))
            r = subprocess.run(outil + ["musiques", "prendre", "2"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            r = subprocess.run(outil + ["musiques", "prendre", "2", "--a", "7.5"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            liste = json.loads((reel / "work" / "musiques.json").read_text(encoding="utf-8"))
            self.assertEqual((liste["a"], liste["pris"]), (7.5, "lancement-energique-01-test"))   # relu par `sons`
            source = (reel / "assets" / "audio" / "SOURCE.md").read_text(encoding="utf-8")
            self.assertIn("musiques de lancement, lancement-energique-01-test", source)
            self.assertTrue((reel / "assets" / "audio" / "lancement-energique-01-test.mp3").is_file())
            section = next((copie / "videos").glob("*/* · Section de page"))
            r = subprocess.run(outil + ["musiques", "choisir"], cwd=section, env=env, capture_output=True, text=True)
            self.assertIn("muette", r.stdout)
            styles_seuls = (section / "work" / "ecoute-musiques.html").read_text(encoding="utf-8")
            self.assertEqual((styles_seuls.count("<video "), styles_seuls.count("<audio ")), (10, 0))
            (copie / "studio.config.json").write_text(json.dumps({"preferences": ["style 4"]}), encoding="utf-8")
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertIn("son style gardé : 4", r.stdout)
            self.assertNotIn("<video ", page.read_text(encoding="utf-8"))
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30", "--style", "2"], cwd=reel, env=env,
                               capture_output=True, text=True)   # il en veut un autre : `--style` rouvre la page
            self.assertIn("ton conseil : 2 « Titres géants »", r.stdout)
            self.assertEqual(page.read_text(encoding="utf-8").count("<video "), 10)
            (copie / "studio.config.json").write_text(json.dumps({"preferences": ["style 0"]}), encoding="utf-8")
            r = subprocess.run(outil + ["musiques", "choisir", "--duree", "30"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertIn("son style gardé : 0", r.stdout)                                  # 0 n'est pas « aucun »
            self.assertNotIn("<video ", page.read_text(encoding="utf-8"))

    def test_sans_musiques_la_page_montre_les_styles(self):
        """Revue du 03/11/2026 : sans musiques installées, `musiques choisir` s'arrêtait sur une erreur et le
        client ne voyait jamais les styles."""
        with tempfile.TemporaryDirectory() as t:
            copie = Path(t) / "Publicitaire IA"
            copie.mkdir()
            for nom in ("produit.json", "VERSION", "tools", "templates", "assets", "hyperframes.json"):
                src = RACINE / nom
                if src.is_dir():
                    shutil.copytree(src, copie / nom, ignore=shutil.ignore_patterns("musiques", "__pycache__"))
                elif src.is_file():
                    shutil.copy2(src, copie / nom)
            index_styles = Path(".claude") / "skills" / "studio" / "styles" / "README.md"
            (copie / index_styles).parent.mkdir(parents=True)
            shutil.copy2(RACINE / index_styles, copie / index_styles)
            env = {**os.environ, "HOME": str(Path(t) / "home"), "USERPROFILE": str(Path(t) / "home")}
            outil = [sys.executable, str(copie / "tools" / "studio_motion.py")]
            r = subprocess.run(outil + ["nouvelle", "Test", "--objectif", "vente", "--videos", "reel"], cwd=copie, env=env,
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            reel = next((copie / "videos").glob("*/* · Reel"))
            r = subprocess.run(outil + ["musiques", "choisir", "--style", "7"], cwd=reel, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("pas installées", r.stdout)
            self.assertIn("Sa réponse : le numéro du style.", r.stdout)
            page = (reel / "work" / "ecoute-musiques.html").read_text(encoding="utf-8")
            self.assertEqual((page.count("<video "), page.count("<audio ")), (10, 0))


if __name__ == "__main__":
    unittest.main()
