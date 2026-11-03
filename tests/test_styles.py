"""Tests du catalogue de styles (`.claude/skills/studio/styles/`) : chaque kit a sa fiche, ses
scènes, ses gestes signature et son aperçu ; l'index les liste tous sous le même nom ; rien n'y
reprend la ponctuation interdite. Puis `tools/styles.py`, qui les lit pour la page des styles."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
STYLES = RACINE / ".claude" / "skills" / "studio" / "styles"
TITRE = re.compile(r"^# Style n°(\d+) · (.+?) · d'après (.+?) \((https?://\S+)\)$")
sys.path.insert(0, str(RACINE / "tools"))

import musiques  # noqa: E402
import styles  # noqa: E402


def kits() -> list[Path]:
    return sorted(d for d in STYLES.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name))


def gestes(fiche: str) -> list[list[str]]:
    """Les lignes de la table des gestes (section 2), découpées en cellules."""
    section = fiche.split("## 2. Les gestes signature et leur place", 1)[1].split("\n## 3.", 1)[0]
    table = section.split("| Geste | Ce qu'on voit | Il sert à | Dans le kit |", 1)[1].split("\n\n", 1)[0]
    return [[c.strip() for c in l.strip().strip("|").split("|")] for l in table.strip().splitlines()[1:]]


class Catalogue(unittest.TestCase):
    def test_huit_kits_numerotes_dans_l_ordre(self):
        self.assertEqual([int(d.name[:2]) for d in kits()], list(range(1, 9)))

    def test_chaque_kit_a_sa_fiche_et_ses_scenes(self):
        for d in kits():
            fiche = (d / "style.md").read_text(encoding="utf-8")
            m = TITRE.match(fiche.splitlines()[0])
            self.assertIsNotNone(m, f"{d.name} : titre de fiche")
            self.assertEqual(int(m.group(1)), int(d.name[:2]), d.name)
            for section in ("## 1. Le rythme", "## 2. Les gestes signature et leur place", "### L'original, pour mémoire",
                            "## 3. Les fonds et les couleurs", "## Sur une autre offre", "## Les compositions du kit"):
                self.assertIn(section, fiche, f"{d.name} : {section}")
            self.assertNotIn("## 2. La structure", fiche, f"{d.name} : l'ancienne structure imposée")
            self.assertNotIn("—", fiche, f"{d.name} : tiret long")
            scenes = sorted((d / "compositions").glob("*.html"))
            self.assertGreaterEqual(len(scenes), 2, d.name)
            for s in scenes:
                self.assertIn("data-composition-id", s.read_text(encoding="utf-8"), f"{d.name}/{s.name}")

    def test_les_gestes_viennent_du_kit(self):
        """Le garde-fou demande trois gestes par vidéo : chaque fiche en offre au moins cinq, et chaque
        scène citée dans « Dans le kit » existe."""
        for d in kits():
            lignes = gestes((d / "style.md").read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(lignes), 5, d.name)
            for cellules in lignes:
                self.assertEqual(len(cellules), 4, f"{d.name} : {cellules[0]}")
                for scene in re.findall(r"`([^`]+)`", cellules[3]):
                    self.assertTrue((d / "compositions" / f"{scene.removesuffix('.html')}.html").is_file(),
                                    f"{d.name} : {scene} n'est pas dans le kit")

    def test_chaque_fiche_nomme_l_ambiance_de_sa_musique(self):
        """Les musiques proposées avec un style suivent sa fiche (section 8) : les deux disent la même chose."""
        for d in kits():
            son = (d / "style.md").read_text(encoding="utf-8").split("## 8. Le son", 1)[1].split("\n## 9.", 1)[0]
            cles = styles.ambiances(int(d.name[:2]))
            self.assertTrue(cles, d.name)
            for cle in cles:
                self.assertIn(f"« {musiques.AMBIANCES[cle]} »", son, d.name)

    def test_les_scenes_portent_le_nom_du_style(self):
        """L'IA copie et lit ces scènes : leur en-tête dit « style » et le nom actuel, jamais un ancien nom."""
        for d in kits():
            for s in (d / "compositions").glob("*.html"):
                texte = s.read_text(encoding="utf-8")
                for ancien in ("TEMPLATE N°", "Template n°", "DÉGRADÉS VIFS", "PAPIER PINCEAU", "FENÊTRES BARRES", "· Orbite ·"):
                    self.assertNotIn(ancien, texte, f"{d.name}/{s.name}")

    def test_chaque_style_a_son_apercu(self):
        for d in kits():
            for ext in ("mp4", "jpg"):
                f = RACINE / "assets" / "styles" / f"{d.name}.{ext}"
                self.assertTrue(f.is_file(), f"{d.name} : aperçu {ext}")
                self.assertLess(f.stat().st_size, 1_000_000, f"{d.name} : aperçu {ext} trop lourd")

    def test_l_index_liste_chaque_kit_sous_son_nom(self):
        index = (STYLES / "README.md").read_text(encoding="utf-8")
        for d in kits():
            nom = TITRE.match((d / "style.md").read_text(encoding="utf-8").splitlines()[0]).group(2)
            ligne = next((l for l in index.splitlines() if l.startswith(f"| {int(d.name[:2])} |")), "")
            self.assertIn(nom, ligne, f"{d.name} : absent de l'index ou sous un autre nom")
            self.assertIn(d.name, index, f"{d.name} : dossier absent de l'index")
        self.assertNotIn("—", index)


class Outil(unittest.TestCase):
    def test_catalogue_lu_dans_l_index(self):
        cat = styles.catalogue(RACINE)
        self.assertEqual([s["n"] for s in cat], list(range(1, 9)))
        for s, d in zip(cat, kits()):
            self.assertEqual(s["dossier"], d.name)
            self.assertTrue(s["video"].is_file(), s["dossier"])
        vitrine = styles.vitrine(RACINE, conseil=7)
        self.assertEqual([s["numero"] for s in vitrine if s["conseil"]], [7])
        self.assertTrue(all(s["video"].startswith("file:") for s in vitrine))

    def test_style_garde_dans_les_preferences(self):
        with tempfile.TemporaryDirectory() as t:
            r = Path(t)
            self.assertIsNone(styles.garde(r))                            # pas encore de profil
            for prefs, attendu in ((["choisis toujours la musique"], None), (["style 4"], 4),
                                   (["template 3"], 3), (["Style n°2"], 2)):
                (r / "studio.config.json").write_text(json.dumps({"preferences": prefs}), encoding="utf-8")
                self.assertEqual(styles.garde(r), attendu, prefs)
            self.assertEqual(styles.catalogue(r), [])                     # sans index : aucun style


if __name__ == "__main__":
    unittest.main()
