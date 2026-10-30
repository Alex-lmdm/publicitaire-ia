"""Tests de tools/pack_sfx.py : le Pack SFX installé depuis son archive ou repris de Monteur IA.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import hashlib
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
import pack_sfx  # noqa: E402

CATALOGUE = {"pack": "pack-sfx", "version": "1.1.0", "sounds": [
    {"id": "ui-check-pop", "file": "pack/ui/ui-check-pop.mp3", "source": "pack", "role": "succes",
     "usage": "pop de validation : coche verte", "tags": "coche", "gain_db": -22.0, "hit": 0.0, "align": "start", "duration": 0.6},
    {"id": "money-cash-register", "file": "pack/money/money-cash-register.mp3", "source": "pack", "role": "argent",
     "usage": "caisse enregistreuse : vente, « ka-ching »", "tags": "", "gain_db": -20.5, "hit": 0.32, "align": "start", "duration": 1.1},
    {"id": "starter-click-ui", "file": "starter/click-ui.mp3", "source": "starter", "role": "apparition",
     "usage": "clic d'interface", "tags": "", "gain_db": -17.0, "hit": 0.0, "align": "start", "duration": 0.1},
]}

# L'archive telle qu'elle est vendue : un dossier pack-sfx/ avec ses sons, ses fiches, et ce qui vise
# Monteur IA (INSTALL.md, outils, skill), qu'on ne doit pas copier.
ARCHIVE = {
    "pack-sfx/INSTALL.md": b"# Installer le Pack SFX dans Monteur IA",
    "pack-sfx/install.py": b"print('Monteur IA')",
    "pack-sfx/tools/sfx_mix.py": b"#",
    "pack-sfx/.claude/skills/pack-sfx/SKILL.md": b"---\nname: pack-sfx\n---",
    "pack-sfx/.claude/skills/pack-sfx/references/sons-par-situation.md": "# À l'écran → le son".encode(),
    "pack-sfx/assets/sfx/catalog.json": json.dumps(CATALOGUE).encode(),
    "pack-sfx/assets/sfx/pack/ui/ui-check-pop.mp3": b"ID3" + b"\x01" * 400,
    "pack-sfx/assets/sfx/pack/money/money-cash-register.mp3": b"ID3" + b"\x02" * 400,
    "pack-sfx/assets/sfx/pack/ui/.DS_Store": b"x",
}


def ecrire_archive(chemin: Path, contenu: dict) -> Path:
    with zipfile.ZipFile(chemin, "w") as z:
        for nom, donnees in contenu.items():
            z.writestr(nom, donnees)
    return chemin


def empreinte(dossier: Path) -> str:
    h = hashlib.sha1()
    for f in sorted(p for p in dossier.rglob("*") if p.is_file()):
        h.update(str(f.relative_to(dossier)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


class Selection(unittest.TestCase):
    def test_sons_et_fiches_seulement(self):
        choix = pack_sfx.selection(list(ARCHIVE))
        self.assertEqual(sorted(choix.values()), [
            "assets/sfx/catalog.json", "assets/sfx/pack/money/money-cash-register.mp3",
            "assets/sfx/pack/ui/ui-check-pop.mp3", "assets/sfx/sons-par-situation.md"])

    def test_chemins_pieges_refuses(self):
        noms = list(ARCHIVE) + ["pack-sfx/assets/sfx/pack/../../../../evil.mp3", "/etc/passwd.mp3",
                                "pack-sfx/assets/sfx/pack/ui/../../../tools/x.mp3"]
        valeurs = pack_sfx.selection(noms).values()
        self.assertTrue(all(v.startswith("assets/sfx/") and ".." not in v for v in valeurs))
        self.assertIsNone(pack_sfx.chemin_sur("../x"))
        self.assertIsNone(pack_sfx.chemin_sur("C:/x"))

    def test_pas_un_pack(self):
        with self.assertRaises(pack_sfx.ErreurPack):
            pack_sfx.selection(["monteur-ia/README.md", "x/assets/sfx/pack/a.mp3"])


class Installation(unittest.TestCase):
    def test_depuis_l_archive_puis_relance(self):
        with tempfile.TemporaryDirectory() as d:
            racine = Path(d) / "publicitaire"
            racine.mkdir()
            archive = ecrire_archive(Path(d) / "pack-sfx.zip", ARCHIVE)
            res = pack_sfx.installer_depuis_zip(racine, archive)
            self.assertEqual((res["presents"], res["attendus"], res["ecrits"]), (2, 2, 4))
            self.assertTrue((racine / "assets/sfx/sons-par-situation.md").is_file())
            for absent in ("INSTALL.md", "install.py", "tools/sfx_mix.py", ".claude", "assets/sfx/pack/ui/.DS_Store"):
                self.assertFalse((racine / absent).exists(), absent)
            again = pack_sfx.installer_depuis_zip(racine, archive)
            self.assertEqual((again["ecrits"], again["identiques"]), (0, 4))
            self.assertEqual([s["id"] for s in pack_sfx.chercher(racine, ["coche"])], ["ui-check-pop"])
            self.assertEqual([s["id"] for s in pack_sfx.chercher(racine, ["pop validation"])], ["ui-check-pop"])
            self.assertIn("../../../assets/sfx/pack/money/money-cash-register.mp3",
                          pack_sfx.ligne(pack_sfx.chercher(racine, ["caisse"])[0]))

    def test_ligne_montre_les_prises(self):
        son = {"id": "paper-marker-stroke", "file": "pack/paper/paper-marker-stroke.mp3", "duration": 11.6,
               "segments": [[0.0, 0.37], [0.61, 0.94], [1.13, 2.34], [2.5, 2.9], [3.1, 3.5]]}
        ligne = pack_sfx.ligne(son)
        self.assertIn("5 prises, une seule à poser par son trim : [0.0, 0.37], [0.61, 0.94]", ligne)
        self.assertIn("…", ligne)
        self.assertNotIn("prises", pack_sfx.ligne(dict(son, segments=None)))

    def test_archive_incomplete(self):
        incomplete = {k: v for k, v in ARCHIVE.items() if "money" not in k}
        with tempfile.TemporaryDirectory() as d:
            racine = Path(d) / "publicitaire"
            racine.mkdir()
            with self.assertRaises(pack_sfx.ErreurPack):
                pack_sfx.installer_depuis_zip(racine, ecrire_archive(Path(d) / "p.zip", incomplete))

    def test_reprise_depuis_monteur_ia_sans_le_modifier(self):
        with tempfile.TemporaryDirectory() as d:
            monteur = Path(d) / "Monteur IA"
            (monteur / "templates").mkdir(parents=True)
            (monteur / "templates" / "AGENT.md.tpl").write_text("# Monteur IA\n", encoding="utf-8")
            for nom, donnees in ARCHIVE.items():
                rel = nom[len("pack-sfx/"):]
                if rel.startswith(("assets/", ".claude/")):
                    (monteur / rel).parent.mkdir(parents=True, exist_ok=True)
                    (monteur / rel).write_bytes(donnees)
            (monteur / "assets/sfx/starter").mkdir(parents=True)
            (monteur / "assets/sfx/starter/click-ui.mp3").write_bytes(b"starter")
            avant = empreinte(monteur)
            racine = Path(d) / "publicitaire"
            racine.mkdir()
            res = pack_sfx.reprendre_depuis_monteur(racine, monteur)
            self.assertEqual(empreinte(monteur), avant)
            self.assertEqual(res["presents"], 2)
            self.assertFalse((racine / "assets/sfx/starter/click-ui.mp3").exists())  # ses sons de démarrage restent chez lui
            with self.assertRaises(pack_sfx.ErreurPack):
                pack_sfx.reprendre_depuis_monteur(racine, Path(d))


class Telechargements(unittest.TestCase):
    """Sans chemin : le Pack SFX pris dans Téléchargements, l'archive ou le dossier que Safari a
    décompressé tout seul (il ouvre les ZIP téléchargés et jette l'archive)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.racine = self.tmp / "publicitaire"
        self.racine.mkdir()
        self.dl = self.tmp / "Downloads"
        self.dl.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def decompresse(self, nom: str = "pack-sfx") -> Path:
        with zipfile.ZipFile(ecrire_archive(self.tmp / "a.zip", ARCHIVE)) as z:
            z.extractall(self.tmp / "x")
        (self.tmp / "x" / "pack-sfx").rename(self.dl / nom)
        return self.dl / nom

    def test_dossier_decompresse_par_safari(self):
        dossier = self.decompresse("pack-sfx 2")
        self.assertEqual(pack_sfx.sources_par_defaut(self.dl), [dossier])
        res = pack_sfx.installer_par_defaut(self.racine, self.dl)
        self.assertEqual((res["presents"], res["attendus"], res["ignores"]), (2, 2, []))
        for absent in ("INSTALL.md", "install.py", "tools", ".claude", "assets/sfx/pack/ui/.DS_Store"):
            self.assertFalse((self.racine / absent).exists(), absent)
        self.assertEqual(pack_sfx.installer(self.racine, dossier)["identiques"], 4)   # le dossier en argument

    def test_le_plus_recent_l_emporte(self):
        ancien = ecrire_archive(self.dl / "pack-sfx.zip", {
            **ARCHIVE, "pack-sfx/assets/sfx/catalog.json": json.dumps({**CATALOGUE, "version": "1.0.0"}).encode()})
        os.utime(ancien, (1_000_000_000, 1_000_000_000))
        recent = ecrire_archive(self.dl / "pack-sfx (1).zip", ARCHIVE)
        (self.dl / "photos.zip").write_bytes(b"x")
        self.assertEqual(pack_sfx.sources_par_defaut(self.dl), [ancien, recent])
        self.assertEqual(pack_sfx.installer_par_defaut(self.racine, self.dl)["version"], "1.1.0")

    def test_un_telechargement_interrompu_laisse_place_au_suivant(self):
        bon = ecrire_archive(self.dl / "pack-sfx.zip", ARCHIVE)
        os.utime(bon, (1_000_000_000, 1_000_000_000))
        (self.dl / "pack-sfx (1).zip").write_bytes(b"PK\x03\x04 interrompu")
        res = pack_sfx.installer_par_defaut(self.racine, self.dl)
        self.assertEqual(res["presents"], 2)
        self.assertEqual(len(res["ignores"]), 1)
        self.assertTrue(res["ignores"][0].startswith("pack-sfx (1).zip : "))

    def test_rien_dans_telechargements(self):
        (self.dl / "photos.zip").write_bytes(b"x")
        with self.assertRaisesRegex(pack_sfx.ErreurPack, "aucun Pack SFX"):
            pack_sfx.installer_par_defaut(self.racine, self.dl)

    def test_acces_refuse(self):
        archive = ecrire_archive(self.dl / "pack-sfx.zip", ARCHIVE)
        refus = PermissionError(1, "Operation not permitted")
        with mock.patch.object(Path, "iterdir", side_effect=refus):
            with self.assertRaisesRegex(pack_sfx.ErreurPack, "glisse le fichier ici"):
                pack_sfx.installer_par_defaut(self.racine, self.dl)
        with mock.patch("zipfile.ZipFile", side_effect=refus):
            with self.assertRaisesRegex(pack_sfx.ErreurPack, "glisse le fichier ici"):
                pack_sfx.installer(self.racine, archive)
        self.assertIn("Autorise l'accès dans Réglages Système > Confidentialité et sécurité > Fichiers et dossiers, "
                      "ou glisse le fichier ici", musiques.acces_refuse(self.dl, "darwin"))

    def test_commande_sans_chemin(self):
        """`pack-sfx installer` seul, dans une copie du dossier, avec le dossier que Safari a laissé."""
        copie = self.tmp / "Publicitaire IA"
        copie.mkdir()
        shutil.copy2(RACINE / "produit.json", copie / "produit.json")
        shutil.copy2(RACINE / "VERSION", copie / "VERSION")
        shutil.copytree(RACINE / "tools", copie / "tools", ignore=shutil.ignore_patterns("__pycache__"))
        self.decompresse()
        env = {**os.environ, "HOME": str(self.tmp), "USERPROFILE": str(self.tmp)}
        r = subprocess.run([sys.executable, str(copie / "tools" / "studio_motion.py"), "pack-sfx", "installer"],
                           cwd=copie, env=env, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("2/2 sons pro", r.stdout)
        self.assertIn("dossier pack-sfx", r.stdout)
        self.assertTrue((copie / "assets" / "sfx" / "pack" / "ui" / "ui-check-pop.mp3").is_file())

    @unittest.skipIf(os.name == "nt" or os.geteuid() == 0, "droits POSIX d'un utilisateur ordinaire")
    def test_commande_dossier_illisible(self):
        """Téléchargements illisible : un message à suivre, jamais une trace Python."""
        copie = self.tmp / "Publicitaire IA"
        copie.mkdir()
        shutil.copy2(RACINE / "produit.json", copie / "produit.json")
        shutil.copytree(RACINE / "tools", copie / "tools", ignore=shutil.ignore_patterns("__pycache__"))
        self.dl.chmod(0)
        try:
            env = {**os.environ, "HOME": str(self.tmp), "USERPROFILE": str(self.tmp)}
            for commande in (["pack-sfx", "installer"], ["musiques", "installer"]):
                r = subprocess.run([sys.executable, str(copie / "tools" / "studio_motion.py"), *commande],
                                   cwd=copie, env=env, capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(r.returncode, 1, commande)
                self.assertIn("glisse le fichier ici", r.stderr, commande)
                self.assertNotIn("Traceback", r.stderr, commande)
        finally:
            self.dl.chmod(0o755)


class JamaisDansLeDepot(unittest.TestCase):
    def test_ignore_par_git(self):
        chemins = ["assets/sfx/pack/ui/ui-check-pop.mp3", "assets/sfx/catalog.json",
                   "assets/sfx/sons-par-situation.md", "assets/sfx/.pack-sfx-manifest.json"]
        r = subprocess.run(["git", "check-ignore", "--no-index", *chemins], cwd=RACINE, capture_output=True, text=True)
        if r.returncode == 128:
            self.skipTest("pas un dépôt git")
        self.assertEqual(sorted(r.stdout.split()), sorted(chemins))
        suivis = subprocess.run(["git", "ls-files", "assets/sfx/pack", "assets/sfx/catalog.json"], cwd=RACINE,
                                capture_output=True, text=True).stdout.split()
        self.assertEqual(suivis, [])


if __name__ == "__main__":
    unittest.main()
