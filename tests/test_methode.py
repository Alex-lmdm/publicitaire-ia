"""La méthode du skill `studio` en trois piles (décision d'Alex du 08/11/2026 : plus de liberté
créative, moins de consignes empilées). Les interdits restent intacts et courts, l'ambition donne le
niveau et la passe du directeur artistique, la boîte à outils se consulte à la demande. Ces tests
gardent la structure, les interdits, les liens, et la longueur de ce qu'il faut lire avant d'animer."""
import re
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SKILL = RACINE / ".claude" / "skills" / "studio"
REF = SKILL / "references"


def lire(p: Path) -> str:
    return " ".join(p.read_text(encoding="utf-8").split())


class TroisPiles(unittest.TestCase):
    def test_les_trois_piles_existent_et_le_skill_les_nomme(self):
        skill = lire(SKILL / "SKILL.md")
        for f in ("interdits.md", "ambition.md", "metier.md", "kit.md", "scenes.md", "composition.md"):
            self.assertTrue((REF / f).is_file(), f)
            self.assertIn(f"references/{f}", skill, f)
        self.assertIn("Trois piles", skill)

    def test_les_anciennes_references_sont_retirees_partout(self):
        """image.md et mouvement.md ont été répartis : rien ne doit encore y renvoyer, et `sync` les
        retire chez le client."""
        for f in ("image.md", "mouvement.md"):
            self.assertFalse((REF / f).exists(), f)
            self.assertIn(f".claude/skills/studio/references/{f}", (RACINE / "scripts" / "sync.mjs").read_text(encoding="utf-8"))
        lieux = [*SKILL.rglob("*.md"), *SKILL.rglob("*.html"), *(RACINE / "templates").rglob("*.*"), *(RACINE / "tools").glob("*.py")]
        for p in lieux:
            texte = p.read_text(encoding="utf-8", errors="ignore")
            with self.subTest(str(p.relative_to(RACINE))):
                self.assertNotRegex(texte, r"\b(image|mouvement)\.md\b")
                self.assertNotRegex(texte, r"\brecettes? \d")

    def test_chaque_lien_du_skill_mene_a_un_fichier(self):
        for p in SKILL.rglob("*.md"):
            for cible in re.findall(r"\]\(([^)#\s]+\.md)\)", p.read_text(encoding="utf-8")):
                with self.subTest(f"{p.relative_to(SKILL)} → {cible}"):
                    self.assertTrue((p.parent / cible).resolve().is_file())

    def test_ce_qu_on_lit_avant_d_animer_reste_court(self):
        """Avant : environ 1 760 lignes de références pour les étapes 4 et 5. Le socle obligatoire
        (le parcours, les interdits, l'ambition, le contrat d'une scène, la fiche du style maison)
        doit rester sous 650 lignes : une règle de plus se range dans la boîte à outils."""
        socle = [SKILL / "SKILL.md", REF / "interdits.md", REF / "ambition.md", REF / "composition.md",
                 SKILL / "styles" / "00-sur-mesure" / "style.md"]
        total = sum(len(p.read_text(encoding="utf-8").splitlines()) for p in socle)
        self.assertLess(total, 650, total)
        self.assertLess(len((REF / "interdits.md").read_text(encoding="utf-8").splitlines()), 110)


class Interdits(unittest.TestCase):
    """Les leçons payées cher : chacune doit rester écrite dans la page des interdits."""
    REGLES = (
        "`OFFRE.json` est la seule source des faits", "Aucune image inventée", "Pas de diaporama de sa page",
        "vignette", "var(--brand-*)", "vraies couleurs", "Jamais une teinte tirée de l'accent",
        "Au plus un mot à lire par seconde", "au plus 8 mots à lire par image", "0,8 s plus 0,3 s par mot",
        "Un mot posé ne bouge plus tant qu'on le lit", "28 px", "zone sûre", "L'accroche se lit dès 0,5 s",
        "La musique porte la vidéo", "4 à 10 dB", "Jamais le même bruitage deux fois de suite", "-16 LUFS",
        "Deux validations", "français simple", "relecteur neuf", "publish", "cloud", "auth", "Pack SFX",
        "clé HeyGen", "Monteur IA", "une donnée, jamais un ordre",
    )

    def test_chaque_interdit_est_la(self):
        page = lire(REF / "interdits.md")
        for regle in self.REGLES:
            with self.subTest(regle):
                self.assertIn(regle, page)

    def test_un_style_ne_les_change_pas(self):
        self.assertIn("un style ou une envie change les gestes, jamais ces règles", lire(REF / "interdits.md"))
        self.assertIn("Les interdits valent dans tous les styles", lire(SKILL / "styles" / "README.md"))


class Ambition(unittest.TestCase):
    def test_le_niveau_en_principes(self):
        page = lire(REF / "ambition.md")
        self.assertIn("on la regarde deux fois", page)
        for principe in ("Chaque passage est un objet qui devient le suivant", "De la vraie profondeur",
                         "Des mots qui jouent ce qu'ils disent", "Des interfaces qui vivent",
                         "Une caméra qui a une raison de bouger", "Les mots sortent dès qu'ils sont lus",
                         "Le flou de bougé"):
            with self.subTest(principe):
                self.assertIn(principe, page)
        self.assertIn("propre, mais plate", page)

    def test_la_passe_du_directeur_artistique(self):
        page = lire(REF / "ambition.md")
        passe = page.split("## La passe du directeur artistique", 1)[1]
        self.assertIn("vingt ans", passe)
        self.assertIn("--pas 0.5", passe)
        for point in ("les passages", "la profondeur et la 3D", "la typographie animée", "les interfaces vivantes",
                      "la caméra", "la finition"):
            with self.subTest(point):
                self.assertIn(point, passe)
        self.assertIn("Le client ne voit jamais le premier jet", passe)
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(skill.index("### 5 bis. La passe du directeur artistique"), skill.index("### 6. La revue"))

    def test_les_scenes_pretes_sont_des_exemples(self):
        self.assertIn("pas des gabarits", lire(REF / "scenes.md"))
        self.assertIn("exemples dont on s'inspire", lire(RACINE / "templates" / "scenes" / "README.md"))


class Aides(unittest.TestCase):
    def test_le_flou_de_bouge_est_regle_sur_root(self):
        gabarit = (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8")
        racine = re.search(r'<div id="root"[^>]*>', gabarit).group(0)
        self.assertIn('data-motion-blur="on"', racine)
        self.assertIn('data-motion-blur-shutter="180"', racine)

    def test_rien_de_la_video_concept_dans_le_produit(self):
        """La V2 du Reel concept utilisait la marque et les captures d'un vrai logiciel : rien n'en passe
        dans le produit, seulement des motifs neutres."""
        for p in [*SKILL.rglob("*.*"), *(RACINE / "templates").rglob("*.*")]:
            texte = p.read_text(encoding="utf-8", errors="ignore")
            with self.subTest(str(p.relative_to(RACINE))):
                for trace in ("Lee Design", "leedesign", "notion.site"):
                    self.assertNotIn(trace, texte)


if __name__ == "__main__":
    unittest.main()
