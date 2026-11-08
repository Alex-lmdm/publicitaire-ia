"""Tests du catalogue de styles (`.claude/skills/studio/styles/`) : chaque kit a sa fiche, ses
scènes, ses gestes signature et son aperçu ; l'index les liste tous sous le même nom ; rien n'y
reprend la ponctuation interdite. Le style 0, « Sur mesure » (le style maison), a sa fiche et son
aperçu ; ses gestes sont les scènes prêtes et les fonctions du kit. Puis `tools/styles.py`, qui les
lit pour la page des styles."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
STYLES = RACINE / ".claude" / "skills" / "studio" / "styles"
TITRE = re.compile(r"^# Style n°(\d+) · (.+?) · d'après (.+?) \((https?://\S+)\)$")
TITRE_MAISON = re.compile(r"^# Style n°0 · (.+?) · le style maison$")
SCENES_PRETES = RACINE / "templates" / "scenes"
KIT = RACINE / "templates" / "kit"
sys.path.insert(0, str(RACINE / "tools"))

import musiques  # noqa: E402
import styles  # noqa: E402


def kits() -> list[Path]:
    """Les huit styles repris d'une vraie vidéo (01 à 08), chacun avec ses compositions."""
    return sorted(d for d in STYLES.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name) and d.name[:2] != "00")


def maison() -> Path:
    return next(d for d in STYLES.iterdir() if d.is_dir() and d.name.startswith("00-"))


def nom_du_style(d: Path) -> str:
    premiere = (d / "style.md").read_text(encoding="utf-8").splitlines()[0]
    m = (TITRE_MAISON if d.name.startswith("00-") else TITRE).match(premiere)
    return m.group(1 if d.name.startswith("00-") else 2)


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
            with self.subTest(d.name):
                fiche = (d / "style.md").read_text(encoding="utf-8")
                m = TITRE.match(fiche.splitlines()[0])
                self.assertIsNotNone(m, f"{d.name} : titre de fiche")
                self.assertEqual(int(m.group(1)), int(d.name[:2]), d.name)
                for section in ("## 1. Le rythme", "## 2. Les gestes signature et leur place",
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
            with self.subTest(d.name):
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
            with self.subTest(d.name):
                son = (d / "style.md").read_text(encoding="utf-8").split("## 8. Le son", 1)[1].split("\n## 9.", 1)[0]
                cles = styles.ambiances(int(d.name[:2]))
                self.assertTrue(cles, d.name)
                for cle in cles:
                    self.assertIn(f"« {musiques.AMBIANCES[cle]} »", son, d.name)

    def test_les_scenes_portent_le_nom_du_style(self):
        """L'IA copie et lit ces scènes : leur en-tête dit « style » et le nom actuel, jamais un ancien nom."""
        for d in kits():
            with self.subTest(d.name):
                for s in (d / "compositions").glob("*.html"):
                    texte = s.read_text(encoding="utf-8")
                    for ancien in ("TEMPLATE N°", "Template n°", "DÉGRADÉS VIFS", "PAPIER PINCEAU", "FENÊTRES BARRES", "· Orbite ·"):
                        self.assertNotIn(ancien, texte, f"{d.name}/{s.name}")

    def test_chaque_style_a_son_apercu(self):
        for d in [maison(), *kits()]:
            with self.subTest(d.name):
                for ext in ("mp4", "jpg"):
                    f = RACINE / "assets" / "styles" / f"{d.name}.{ext}"
                    self.assertTrue(f.is_file(), f"{d.name} : aperçu {ext}")
                    self.assertLess(f.stat().st_size, 1_000_000, f"{d.name} : aperçu {ext} trop lourd")

    def test_l_index_liste_chaque_kit_sous_son_nom(self):
        index = (STYLES / "README.md").read_text(encoding="utf-8")
        for d in [maison(), *kits()]:
            with self.subTest(d.name):
                nom = nom_du_style(d)
                ligne = next((l for l in index.splitlines() if l.startswith(f"| {int(d.name[:2])} |")), "")
                self.assertIn(nom, ligne, f"{d.name} : absent de l'index ou sous un autre nom")
                self.assertIn(d.name, index, f"{d.name} : dossier absent de l'index")
        self.assertNotIn("—", index)


class Maison(unittest.TestCase):
    """Le style 0 (« Sur mesure ») : le conseil par défaut. Pas de compositions à lui : ses gestes sont
    les scènes prêtes (`templates/scenes/`) et les fonctions et classes du kit, que la fiche nomme."""

    def fiche(self) -> str:
        return (maison() / "style.md").read_text(encoding="utf-8")

    def test_sa_fiche(self):
        self.assertEqual(maison().name, "00-sur-mesure")
        self.assertIsNotNone(TITRE_MAISON.match(self.fiche().splitlines()[0]))
        for section in ("## 1. Le rythme", "## 2. Les gestes signature et leur place", "## 3. Les fonds et les couleurs",
                        "## 8. Le son", "## Sur une autre offre", "## Quand il décrit un autre style",
                        "## Les compositions du kit"):
            self.assertIn(section, self.fiche(), section)
        self.assertNotIn("—", self.fiche())
        self.assertFalse((maison() / "compositions").exists(), "ses gestes sont les scènes prêtes, pas une copie")

    def test_ses_gestes_existent(self):
        """Chaque nom de la colonne « Dans le kit » est une scène prête, une fonction `K.` du kit ou une
        classe `k-` du kit ; ses dix scènes prêtes sont toutes à sa table des compositions."""
        kit_js = (KIT / "kit.js").read_text(encoding="utf-8")
        kit_css = (KIT / "kit.css").read_text(encoding="utf-8")
        lignes = gestes(self.fiche())
        self.assertGreaterEqual(len(lignes), 5)
        for cellules in lignes:
            self.assertEqual(len(cellules), 4, cellules[0])
            for nom in re.findall(r"`([^`]+)`", cellules[3]):
                with self.subTest(nom):
                    if nom.startswith("K."):
                        self.assertRegex(kit_js, rf"\bK\.{re.escape(nom[2:])}\s*=|\b{re.escape(nom[2:])}\s*[:(]", nom)
                    elif nom.startswith("k-"):
                        self.assertIn(f".{nom}", kit_css, nom)
                    else:
                        self.assertTrue((SCENES_PRETES / f"{nom}.html").is_file(), f"{nom} n'est pas une scène prête")
        compositions = self.fiche().split("## Les compositions du kit", 1)[1]
        for s in sorted(SCENES_PRETES.glob("*.html")):
            self.assertIn(f"`{s.stem}`", compositions, f"{s.stem} absente de sa table")

    def test_sa_musique_suit_le_but(self):
        self.assertEqual(styles.ambiances(0), [])
        self.assertIn("n'impose aucune ambiance", self.fiche().split("## 8. Le son", 1)[1])


class Menage(unittest.TestCase):
    """L'IA lit les fiches et l'index pendant une vidéo : ils disent la règle au présent. L'historique
    (l'original scène par scène, les essais, les refus datés, les anciens noms) vit dans
    `notes/styles/`, que l'IA ne lit pas ; les références renvoient aux fichiers du skill d'aujourd'hui."""
    DATE = re.compile(r"\b\d{1,2}/\d{1,2}/20\d\d\b")
    HISTOIRE = ("L'original, pour mémoire", "Ce qui ne se fera pas à l'identique", "Mesures de l'essai",
                "Essai du kit", "refusée le", "jusqu'à la 0.")
    REFERENCES_PARTIES = ("references/style.md", "references/rythme.md")

    def docs(self):
        yield "README.md", (STYLES / "README.md").read_text(encoding="utf-8")
        for d in [maison(), *kits()]:
            yield f"{d.name}/style.md", (d / "style.md").read_text(encoding="utf-8")

    def test_ni_date_ni_historique(self):
        for nom, texte in self.docs():
            with self.subTest(nom):
                self.assertIsNone(self.DATE.search(texte), f"{nom} : date {self.DATE.search(texte)}")
                for mot in self.HISTOIRE:
                    self.assertFalse(mot in texte, f"{nom} : {mot}")

    def test_les_liens_visent_les_references_d_aujourd_hui(self):
        for nom, texte in self.docs():
            with self.subTest(nom):
                for ancien in self.REFERENCES_PARTIES:
                    self.assertFalse(ancien in texte, f"{nom} : {ancien}")

    def test_l_historique_est_range_dans_les_notes(self):
        for d in [maison(), *kits()]:
            with self.subTest(d.name):
                self.assertTrue((RACINE / "notes" / "styles" / f"{d.name}.md").is_file(), f"{d.name} : note d'historique")


class Exemples(unittest.TestCase):
    """L'IA copie surtout le code des scènes : rien n'y doit pouvoir passer pour un fait. Leurs textes,
    chiffres, prix et noms d'exemple vivent dans un seul objet `EXEMPLE`, en tête du script, marqué
    « À REMPLACER » ; aucun ne vient d'une vraie marque ; aucun caractère posé comme un objet."""
    EXEMPLE = re.compile(r"\b(?:var|const|let)\s+EXEMPLE\s*=\s*\{")
    MARQUES = ("LMDM", "LeMondeDuMarketing", "Le Monde du Marketing", "Publicitaire IA", "Monteur IA",
               "lemondedumarketing", "CapCut", "1 500 €")
    OBJETS = ("●", "▬", "★", "☆")

    def scenes(self):
        for d in kits():
            for s in sorted((d / "compositions").glob("*.html")):
                yield f"{d.name}/{s.name}", s.read_text(encoding="utf-8")

    def test_un_seul_objet_exemple_a_remplacer(self):
        for nom, texte in self.scenes():
            with self.subTest(nom):
                self.assertEqual(len(self.EXEMPLE.findall(texte)), 1, f"{nom} : un objet EXEMPLE")
                self.assertTrue("À REMPLACER" in texte, f"{nom} : EXEMPLE sans « À REMPLACER »")

    def test_aucune_vraie_marque_dans_les_exemples(self):
        docs = list(self.scenes()) + list(Menage().docs())
        for nom, texte in docs:
            with self.subTest(nom):
                for marque in self.MARQUES:
                    self.assertFalse(marque in texte, f"{nom} : {marque}")

    def test_aucun_caractere_pose_comme_un_objet(self):
        for nom, texte in self.scenes():
            with self.subTest(nom):
                for c in self.OBJETS:
                    self.assertFalse(c in texte, f"{nom} : {c}")


class Palette(unittest.TestCase):
    """Les scènes des styles ne peignent qu'avec la marque : ses jetons, et du noir ou du blanc. Né de
    la story refusée du 06/11/2026 (paysages bruns tirés du jaune, « nuit » teintée)."""
    HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
    RGBA = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)")
    OUTIL = "couleur d'outil"   # une vraie interface tierce garde ses couleurs, et le dit

    def lignes(self):
        for d in kits():
            for scene in sorted((d / "compositions").glob("*.html")):
                for n, ligne in enumerate(scene.read_text(encoding="utf-8").splitlines(), 1):
                    yield f"{d.name}/{scene.name}:{n}", ligne

    def test_aucune_couleur_tiree_de_l_accent(self):
        for lieu, ligne in self.lignes():
            with self.subTest(lieu):
                self.assertNotIn("oklch(from", ligne, lieu)
                self.assertNotRegex(ligne, r"color-mix\([^;]*--brand-accent", lieu)

    def test_aucune_couleur_en_dur_hors_du_blanc_et_du_noir(self):
        """Les gris aussi viennent de la marque (`--brand-gris-1` à `4`) : en dur, seuls le blanc et le
        noir restent (en transparence pour une grille fine ou une ombre), sauf la couleur d'une vraie
        interface tierce, qui le dit."""
        for lieu, ligne in self.lignes():
            with self.subTest(lieu):
                if self.OUTIL in ligne:
                    continue
                for h in self.HEX.findall(ligne):
                    self.assertIn(h.lower(), ("fff", "ffffff", "000", "000000"), f"{lieu} : #{h}")
                for r, g, b in self.RGBA.findall(ligne):
                    self.assertIn((int(r), int(g), int(b)), ((0, 0, 0), (255, 255, 255)), f"{lieu} : rgba({r}, {g}, {b})")


class Outil(unittest.TestCase):
    def test_catalogue_lu_dans_l_index(self):
        cat = styles.catalogue(RACINE)
        self.assertEqual([s["n"] for s in cat], list(range(0, 9)))     # le style maison en premier
        self.assertEqual(cat[0]["nom"], "Sur mesure")
        for s, d in zip(cat, [maison(), *kits()]):
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
                                   (["template 3"], 3), (["Style n°2"], 2), (["style 0"], 0)):
                (r / "studio.config.json").write_text(json.dumps({"preferences": prefs}), encoding="utf-8")
                self.assertEqual(styles.garde(r), attendu, prefs)
            self.assertEqual(styles.catalogue(r), [])                     # sans index : aucun style


if __name__ == "__main__":
    unittest.main()
