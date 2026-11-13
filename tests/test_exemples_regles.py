"""Les exemples suivent les règles qu'ils illustrent (revue du 09/11/2026 : l'IA recopie les exemples
avant de lire les règles). Le kit, les scènes prêtes et les compositions des styles : ni `will-change`,
ni `expo.inOut` (l'à-coup), ni rebond sur l'opacité, ni `backface-visibility`, ni identifiant
intérieur en `-hote` ; l'accroche et le prix portent les attributs que `check` vérifie."""
import re
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TEMPLATES = RACINE / "templates"
STYLES = RACINE / ".claude" / "skills" / "studio" / "styles"


def exemples() -> list[Path]:
    """Ce que l'IA recopie : le kit, les scènes prêtes, les compositions des styles."""
    return ([TEMPLATES / "kit" / "kit.css", TEMPLATES / "kit" / "kit.js"] + sorted((TEMPLATES / "scenes").glob("*.html"))
            + sorted(STYLES.glob("*/compositions/*.html")))


def nom(f: Path) -> str:
    return str(f.relative_to(RACINE))


def objets_qui_contiennent(texte: str, motif: str):
    """Chaque objet `{ … }` (au plus près) qui contient `motif` : les réglages d'un tween."""
    for m in re.finditer(re.escape(motif), texte):
        i, prof = m.start(), 0
        while i > 0:
            i -= 1
            if texte[i] == "}":
                prof += 1
            elif texte[i] == "{":
                if prof == 0:
                    break
                prof -= 1
        j, prof = m.end(), 0
        while j < len(texte):
            if texte[j] == "{":
                prof += 1
            elif texte[j] == "}":
                if prof == 0:
                    break
                prof -= 1
            j += 1
        yield texte.count("\n", 0, m.start()) + 1, texte[i:j + 1]


class Rendu(unittest.TestCase):
    def test_jamais_de_will_change(self):
        """Il n'aide pas au rendu, et un objet que la caméra agrandit reste flou (kit.md, « Les pièges »)."""
        fichiers = [f for f in TEMPLATES.rglob("*") if f.is_file() and f.suffix in (".html", ".css", ".js", ".tpl")]
        fichiers += [f for f in STYLES.rglob("*") if f.is_file() and f.suffix in (".html", ".css", ".js")]
        self.assertTrue(fichiers)
        for f in fichiers:
            texte = f.read_text(encoding="utf-8")
            with self.subTest(nom(f)):
                self.assertNotRegex(texte, r"will-change\s*:")
                self.assertNotIn("willChange", texte)

    def test_jamais_de_backface_visibility(self):
        """Il éteint le flou de bougé du rendu : un volume fermé se trie seul, une carte échange ses faces."""
        for f in exemples():
            with self.subTest(nom(f)):
                self.assertNotRegex(f.read_text(encoding="utf-8"), r"backface-visibility\s*:|backfaceVisibility")

    def test_aucun_identifiant_interieur_en_hote(self):
        """`getElementById` trouverait l'hôte d'index.html (kit.md, « Les pièges ») : un calque, `-calque`."""
        for f in exemples():
            texte = f.read_text(encoding="utf-8")
            with self.subTest(nom(f)):
                self.assertNotRegex(texte, r'id="[\w-]*-hote"')
                self.assertNotRegex(texte, r'\$\("[\w-]*hote"\)')


class Courbes(unittest.TestCase):
    def test_jamais_d_expo_in_out(self):
        """Sa vitesse culmine à 7 fois la moyenne : un à-coup (metier.md, « La caméra »)."""
        fiches = sorted(STYLES.glob("*/style.md"))
        for f in exemples() + fiches:
            with self.subTest(nom(f)):
                self.assertNotIn("expo.inOut", f.read_text(encoding="utf-8"))

    def test_jamais_de_rebond_sur_l_opacite(self):
        """Une opacité qui dépasse sa cible se voit dès que la cible est sous 1 (metier.md, « Les courbes »)."""
        for f in exemples():
            texte = f.read_text(encoding="utf-8")
            for ligne, objet in objets_qui_contiennent(texte, "back.out"):
                if ";" in objet:      # le corps d'une fonction (un appel à franchit("back.out")…), pas un tween
                    continue
                with self.subTest(f"{nom(f)}:{ligne}"):
                    self.assertNotRegex(objet, r"\bopacity\s*:")

    def test_les_mots_du_style_7_ne_sautent_plus(self):
        for f in sorted((STYLES / "07-phrase-tapee" / "compositions").glob("*.html")):
            with self.subTest(f.name):
                self.assertNotRegex(f.read_text(encoding="utf-8"), r"\{ y: -14, [^}]*yoyo: true")
        fiche = (STYLES / "07-phrase-tapee" / "style.md").read_text(encoding="utf-8")
        self.assertNotRegex(fiche, r"(?<![\d,])14 px")


class Intentions(unittest.TestCase):
    """`index.motion.json` vérifie `[data-accroche]` (lisible dès 0,5 s) et, pour un prix, `[data-prix]`
    (il ne sort pas du cadre) : les scènes d'ouverture des styles et celles qui montrent un prix les
    portent, sur un seul élément chacune."""
    OUVERTURES = {"01-cartes-pixels": ["t01-bruit"], "02-titres-geants": ["titre-geant", "titre-geant-vertical"],
                  "03-verre-sombre": ["t3-onglets"], "04-mots-eparpilles": ["mots-objets", "mots-objets-vertical"],
                  "05-interrupteurs-creme": ["interrupteurs-cascade"], "06-nuee-d-encre": ["coup-de-pinceau"],
                  "07-phrase-tapee": ["t7-accroche"], "08-fenetre-peinte": ["t08-logo"],
                  "09-objets-en-scene": ["t9-accroche"]}
    PRIX = {"01-cartes-pixels": "t01-carte-annotee", "03-verre-sombre": "t3-commande"}

    def test_chaque_style_marque_son_accroche(self):
        for style, scenes in self.OUVERTURES.items():
            for s in scenes:
                texte = (STYLES / style / "compositions" / f"{s}.html").read_text(encoding="utf-8")
                with self.subTest(f"{style}/{s}"):
                    corps = texte.split("<template>", 1)[1]
                    marques = len(re.findall(r'\bdata-accroche\b(?!=)', re.sub(r"<!--.*?-->|//[^\n]*", "", corps, flags=re.S)))
                    self.assertEqual(marques, 1, "un seul élément porte data-accroche")

    def test_aucune_autre_composition_ne_marque_l_accroche(self):
        ouvertures = {f"{st}/{s}.html" for st, ss in self.OUVERTURES.items() for s in ss}
        for f in sorted(STYLES.glob("*/compositions/*.html")):
            cle = f"{f.parent.parent.name}/{f.name}"
            if cle in ouvertures:
                continue
            with self.subTest(cle):
                self.assertNotIn("data-accroche", f.read_text(encoding="utf-8"))

    def test_le_prix_est_marque(self):
        for style, s in self.PRIX.items():
            texte = (STYLES / style / "compositions" / f"{s}.html").read_text(encoding="utf-8")
            with self.subTest(s):
                self.assertIn("data-prix", texte.split("<template>", 1)[1])
                self.assertIn('{"kind": "staysInFrame", "selector": "[data-prix]"}', texte)

    def test_les_faux_prix_et_chiffres_des_styles(self):
        """« 300 € » et « 1000 élèves » se recopiaient tels quels : ce sont des emplacements, et la
        scène le dit dans la console tant qu'ils restent."""
        for f in sorted(STYLES.glob("*/compositions/*.html")):
            texte = f.read_text(encoding="utf-8")
            with self.subTest(f.name):
                self.assertNotIn('"300 €"', texte)
                self.assertNotRegex(texte, r"\bprix: 300\b|\bnombre: 1000\b|\bbonus: 30,")
        for s in ("01-cartes-pixels/compositions/t01-carte-annotee", "01-cartes-pixels/compositions/t01-chiffre",
                  "03-verre-sombre/compositions/t3-commande"):
            texte = (STYLES / f"{s}.html").read_text(encoding="utf-8")
            with self.subTest(s):
                self.assertIn("K.emplacements(", texte)
                self.assertRegex(texte, r'"\[[A-ZÀ-Ý ]+\]"')


if __name__ == "__main__":
    unittest.main()
