"""Tests du catalogue de templates (`.claude/skills/studio/styles/`) : chaque kit a sa fiche et ses
scènes, l'index les liste tous sous le même nom, et rien n'y reprend la ponctuation interdite."""
import re
import unittest
from pathlib import Path

STYLES = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "studio" / "styles"
TITRE = re.compile(r"^# Template n°(\d+) · (.+?) · d'après (.+?) \((https?://\S+)\)$")


def kits() -> list[Path]:
    return sorted(d for d in STYLES.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name))


class Catalogue(unittest.TestCase):
    def test_huit_kits_numerotes_dans_l_ordre(self):
        self.assertEqual([int(d.name[:2]) for d in kits()], list(range(1, 9)))

    def test_chaque_kit_a_sa_fiche_et_ses_scenes(self):
        for d in kits():
            fiche = (d / "style.md").read_text(encoding="utf-8")
            m = TITRE.match(fiche.splitlines()[0])
            self.assertIsNotNone(m, f"{d.name} : titre de fiche")
            self.assertEqual(int(m.group(1)), int(d.name[:2]), d.name)
            for section in ("## 1. Le rythme", "## 2. La structure", "## 3. Les fonds et les couleurs",
                            "## Sur une autre offre", "## Les compositions du kit"):
                self.assertIn(section, fiche, f"{d.name} : {section}")
            self.assertNotIn("—", fiche, f"{d.name} : tiret long")
            scenes = sorted((d / "compositions").glob("*.html"))
            self.assertGreaterEqual(len(scenes), 2, d.name)
            for s in scenes:
                self.assertIn("data-composition-id", s.read_text(encoding="utf-8"), f"{d.name}/{s.name}")

    def test_l_index_liste_chaque_kit_sous_son_nom(self):
        index = (STYLES / "README.md").read_text(encoding="utf-8")
        for d in kits():
            nom = TITRE.match((d / "style.md").read_text(encoding="utf-8").splitlines()[0]).group(2)
            ligne = next((l for l in index.splitlines() if l.startswith(f"| {int(d.name[:2])} |")), "")
            self.assertIn(nom, ligne, f"{d.name} : absent de l'index ou sous un autre nom")
            self.assertIn(d.name, index, f"{d.name} : dossier absent de l'index")
        self.assertNotIn("—", index)


if __name__ == "__main__":
    unittest.main()
