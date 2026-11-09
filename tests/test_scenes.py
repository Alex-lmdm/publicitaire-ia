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


class Exemples(unittest.TestCase):
    """Revue du 09/11/2026 : l'IA recopie les exemples avant de lire les règles. Les faits d'une scène
    prête (prénom, témoignage, chiffre, prix, date, délai) sont des emplacements évidents, et la scène
    dit dans la console qu'il en reste ; ses anciens faux exemples réalistes ne reviennent pas."""
    ANCIENS = ("Camille", "Léa M.", "690 €", "30 novembre", "1 850 €", "2340", "7530", "6 semaines",
               "18 vidéos", "300 €", "1000 élèves", "1 000 élèves")
    EMPLACEMENT = re.compile(r'"[^"\n]*\[[A-ZÀ-Ý0-9][^\]"\n]*\][^"\n]*"')

    def contenu(self, texte):
        debut = texte.index("var CONTENU = {")
        return texte[debut:texte.index("\n      };", debut)]

    def test_aucun_ancien_faux_exemple(self):
        for s in scenes():
            texte = s.read_text(encoding="utf-8")
            with self.subTest(s.name):
                for ancien in self.ANCIENS:
                    self.assertNotIn(ancien, texte)

    def test_chaque_scene_porte_des_emplacements_et_son_garde_fou(self):
        for s in scenes():
            texte = s.read_text(encoding="utf-8")
            with self.subTest(s.name):
                self.assertRegex(self.contenu(texte), self.EMPLACEMENT, "au moins un fait en emplacement")
                self.assertIn("K.emplacements(ID, CONTENU);", texte)
                # appelé avant toute mise en page : il parle même si la scène plante ensuite
                self.assertLess(texte.index("K.emplacements(ID, CONTENU);"), texte.index("K.cadre("))


class Intentions(unittest.TestCase):
    """Ce que `check` vérifie (`index.motion.json`) : l'accroche porte data-accroche sur un seul élément,
    le prix data-prix ; chaque scène qui les porte le rappelle dans son en-tête."""

    def test_l_accroche_de_l_ouverture(self):
        texte = (SCENES / "situation.html").read_text(encoding="utf-8")
        self.assertEqual(texte.count('setAttribute("data-accroche"'), 1)
        self.assertIn("if (k === 0) bloc.setAttribute(\"data-accroche\"", texte)
        self.assertIn("data-accroche", texte.split("<template>")[0])   # l'en-tête le dit

    def test_le_prix(self):
        texte = (SCENES / "prix.html").read_text(encoding="utf-8")
        self.assertEqual(texte.count('setAttribute("data-prix"'), 1)
        tete = texte.split("<template>")[0]
        self.assertIn("data-prix", tete)
        self.assertIn('{"kind": "staysInFrame", "selector": "[data-prix]"}', tete)

    def test_aucune_autre_scene_ne_les_porte(self):
        for s in scenes():
            if s.name in ("situation.html", "prix.html"):
                continue
            with self.subTest(s.name):
                script = s.read_text(encoding="utf-8").split("<template>", 1)[1]
                self.assertNotIn("data-accroche", script)
                self.assertNotIn("data-prix", script)


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
