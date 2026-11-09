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


class SecondePasse(unittest.TestCase):
    """Décision d'Alex du 08/11/2026 : ne pas viser parfait du premier coup, mais apprendre au client à
    demander une seconde passe. La phrase est figée dans sa formation (dépôt lmdm-blog, chapitre
    « Ta première vidéo qui vend ») : le skill la reconnaît mot pour mot."""
    PHRASE = ("Tu es un directeur artistique en motion design avec vingt ans de films de lancement pour des "
              "marques. Repasse sur toute ma vidéo, plan par plan, et rends-la beaucoup plus impressionnante")

    def test_le_skill_reconnait_la_phrase_de_la_formation(self):
        skill = lire(SKILL / "SKILL.md")
        self.assertIn(self.PHRASE, skill)
        self.assertIn("**La seconde passe**", skill)
        self.assertIn("Repasse sur toute ma vidéo", lire(RACINE / "templates" / "AGENT.md.tpl"))

    def test_la_livraison_la_propose_et_la_revue_s_arrete(self):
        self.assertIn("seconde passe", lire(REF / "livraison.md"))
        self.assertIn("La revue s'arrête", lire(REF / "revue.md"))
        self.assertIn("Une passe suffit", lire(REF / "ambition.md"))

    def test_la_seconde_passe_refait_la_mise_en_scene(self):
        """Essai du 08/11/2026 sur le Reel Calendly : une seconde passe prudente gardait la moitié des
        images ; Alex : « renforce-la ». Elle change chaque plan, les fonds et la fin compris."""
        page = lire(REF / "seconde-passe.md")
        for objectif in ("Aucun plan n'a la même image qu'avant", "Des passages où un objet devient le suivant",
                         "De la vraie profondeur", "Les fonds", "La fin", "work/avant-seconde-passe.mp4",
                         "Garder le script, c'est garder ce qu'il dit, pas sa mise en page"):
            with self.subTest(objectif):
                self.assertIn(objectif, page)
        self.assertIn("references/seconde-passe.md", lire(SKILL / "SKILL.md"))
        passe = lire(REF / "ambition.md").split("## La passe du directeur artistique", 1)[1]
        self.assertIn("les fonds", passe)
        self.assertIn("la fin", passe)
        self.assertIn("les collisions pendant les animations", lire(REF / "revue.md"))

    def test_la_seconde_passe_garde_les_lecons_de_la_v3(self):
        """V3 du Reel Calendly (09/11/2026) : les interdits de la vidéo, écrits avec les anciens objets,
        n'alertaient plus après la remise en scène ; la fin « en grand » est sortie petite et figée, et
        des sujets ont rapetissé sans que `cadre` le voie."""
        page = lire(REF / "seconde-passe.md")
        for lecon in ("les interdits de cette vidéo redits en règles", "Le sujet ne rapetisse pas",
                      "la marque (son logo, son nom) en grand sur la dernière image, qui bouge encore",
                      "sept objectifs"):
            with self.subTest(lecon):
                self.assertIn(lecon, page)
        self.assertIn("comme une règle qui vaudrait pour n'importe quelle image", lire(REF / "revue.md"))

    def test_le_cadre_laisse_de_la_liberte(self):
        """Alex (09/11/2026, après le Reel Notion refait) : des interfaces toujours en plein cadre, un texte
        qui change de place à chaque plan, des mots posés sur l'interface et un écran noir venaient de
        règles trop directives. La méthode ne garde que ce qui est à éviter, et laisse le reste au goût
        du modèle."""
        passe = lire(REF / "seconde-passe.md")
        self.assertIn("un sujet perdu en petit, ou collé à un bord avec le vide de l'autre côté", passe)
        self.assertIn("lisible sur un téléphone à chaque instant où il compte", passe)
        metier = lire(REF / "metier.md")
        self.assertIn("Un repère de goût, pas une règle", metier)
        self.assertIn("Le plein cadre est un moment, pas une habitude", metier)
        self.assertNotIn("deux tiers de l'écran", metier)
        interdits = lire(REF / "interdits.md")
        self.assertIn("Les mots ne recouvrent jamais ce que le plan montre", interdits)
        self.assertIn("Le fond reste dans sa marque", interdits)
        self.assertNotIn("le titre en haut, l'objet au centre", lire(REF / "ambition.md"))

    def test_les_mots_d_une_interface_ne_sont_pas_des_faits(self):
        self.assertIn("jamais des barres grises à leur place", lire(REF / "interdits.md"))


class Aides(unittest.TestCase):
    def test_le_flou_de_bouge_est_regle_sur_root(self):
        gabarit = (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8")
        racine = re.search(r'<div id="root"[^>]*>', gabarit).group(0)
        self.assertIn('data-motion-blur="on"', racine)
        self.assertIn('data-motion-blur-shutter="180"', racine)
        # Depuis HyperFrames 0.9.20, le mode automatique n'adoucit plus les rotations : capture demandé.
        self.assertIn('data-motion-blur-tier="capture"', racine)

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


class Mouvement(unittest.TestCase):
    """Les exemples presque sans rebond (09/11/2026) : 117 `back.out` dans les scènes, le kit et les
    styles, dont 47 au-delà du plafond de la méthode. Claude copie les exemples plus que les règles."""
    DOSSIERS = (RACINE / "templates" / "scenes", RACINE / "templates" / "kit", RACINE / "templates" / "accueil",
                SKILL / "styles", REF)

    def fichiers(self):
        return [p for d in self.DOSSIERS for p in d.rglob("*") if p.suffix in (".html", ".js", ".tpl", ".md")]

    def test_aucun_rebond_au_dela_de_4_pour_cent(self):
        trop = [f"{p.relative_to(RACINE)} : back.out({m.group(1)})" for p in self.fichiers()
                for m in re.finditer(r"back\.out\((\d+(?:\.\d+)?)\)", p.read_text(encoding="utf-8"))
                if float(m.group(1)) > 1 and "4s³" not in p.read_text(encoding="utf-8")]
        self.assertEqual(trop, [])

    def test_la_camera_ne_voyage_plus_en_expo_inout(self):
        motif = re.compile(r"tl\.(?:to|fromTo)\((?:cam|camA|monde|bureau|scene3d)\b[^;]*expo\.inOut")
        trop = [str(p.relative_to(RACINE)) for p in self.fichiers() if motif.search(p.read_text(encoding="utf-8"))]
        self.assertEqual(trop, [])

    def test_les_regles_du_mouvement(self):
        metier = (REF / "metier.md").read_text(encoding="utf-8")
        for phrase in ("Presque aucun rebond", "Deux horloges", "La boîte se pose, puis le texte entre",
                       "Pas de yo-yo", "K.courbeEchelle"):
            self.assertIn(phrase, metier)
        self.assertIn("lignes d'appui apparaissent nettes", (REF / "seconde-passe.md").read_text(encoding="utf-8"))
