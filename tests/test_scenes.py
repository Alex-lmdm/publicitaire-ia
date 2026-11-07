"""Tests des scènes prêtes (`templates/scenes/`) : chacune suit le contrat de son README (un objet
CONTENU à remplir, les deux formats lus sur K.cadre, le calque des mots, la durée lue sur l'hôte une
fois montée), ne peint qu'avec la marque, ne cite aucune vraie marque, et figure au catalogue."""
import re
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SCENES = RACINE / "templates" / "scenes"
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RGBA = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)")
MARQUES = ("LeMondeDuMarketing", "LMDM", "Publicitaire IA", "Monteur IA", "CapCut", "Dupliq")
OUTIL = "couleur d'outil"   # une vraie interface tierce garde ses couleurs, et le dit


def scenes() -> list[Path]:
    return sorted(SCENES.glob("*.html"))


class Contrat(unittest.TestCase):
    def test_il_y_a_des_scenes(self):
        self.assertGreaterEqual(len(scenes()), 6)

    def test_chaque_scene_suit_le_contrat(self):
        for s in scenes():
            texte = s.read_text(encoding="utf-8")
            with self.subTest(s.name):
                self.assertIn("<template>", texte)
                self.assertEqual(len(re.findall(r"\bvar CONTENU = \{", texte)), 1, "un seul objet CONTENU")
                self.assertIn("K.cadre(", texte)
                self.assertIn("window.__timelines[", texte)
                # Une fois montée, HyperFrames retire data-duration de la racine intérieure : la durée
                # se lit sur l'hôte (K.duree), jamais sur le seul parent.
                self.assertNotIn('parentElement.getAttribute("data-duration")', texte)

    def test_chaque_scene_est_au_catalogue(self):
        catalogue = (SCENES / "README.md").read_text(encoding="utf-8")
        for s in scenes():
            with self.subTest(s.name):
                self.assertIn(f"| `{s.name}` |", catalogue)

    def test_aucune_vraie_marque(self):
        for s in scenes():
            texte = s.read_text(encoding="utf-8")
            with self.subTest(s.name):
                for m in MARQUES:
                    self.assertNotIn(m, texte)


class Palette(unittest.TestCase):
    def lignes(self):
        for s in scenes():
            for n, ligne in enumerate(s.read_text(encoding="utf-8").splitlines(), 1):
                yield f"{s.name}:{n}", ligne

    def test_aucune_couleur_tiree_de_l_accent(self):
        for lieu, ligne in self.lignes():
            with self.subTest(lieu):
                self.assertNotIn("oklch(from", ligne)
                self.assertNotRegex(ligne, r"color-mix\([^;]*--brand-accent")

    def test_aucune_couleur_en_dur_hors_du_blanc_et_du_noir(self):
        for lieu, ligne in self.lignes():
            if OUTIL in ligne:
                continue
            # Le repli d'un jeton lu par K.jeton (jamais rendu : brand/tokens.css est toujours chargé).
            ligne = re.sub(r'K\.jeton\([^)]*\)\s*\|\|\s*"#[0-9a-fA-F]{3,6}"', "", ligne)
            with self.subTest(lieu):
                for h in HEX.findall(ligne):
                    self.assertIn(h.lower(), ("fff", "ffffff", "000", "000000"), f"#{h}")
                for r, g, b in RGBA.findall(ligne):
                    self.assertIn((int(r), int(g), int(b)), ((0, 0, 0), (255, 255, 255)), f"rgba({r}, {g}, {b})")


if __name__ == "__main__":
    unittest.main()
