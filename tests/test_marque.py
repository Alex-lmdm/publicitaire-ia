"""Tests de tools/marque.py : l'extraction de la marque, sans réseau ni ffmpeg.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))
import marque as mq  # noqa: E402
import studio_motion as sm  # noqa: E402

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 600
WOFF2 = b"wOF2" + b"\x00" * 2000


def racine_vide(base: Path) -> Path:
    """Un dossier du produit avec ses polices livrées (registre compris)."""
    racine = base / "studio"
    (racine / "assets").mkdir(parents=True)
    shutil.copytree(RACINE / "assets" / "fonts", racine / "assets" / "fonts")
    return racine


def empreinte(dossier: Path) -> str:
    h = hashlib.sha1()
    for f in sorted(p for p in dossier.rglob("*") if p.is_file()):
        h.update(str(f.relative_to(dossier)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


# Une page de vente comme celle de LeMondeDuMarketing : Next.js, Tailwind, Poppins en trois sous-ensembles.
PAGE = """<!DOCTYPE html><html lang="fr"><head>
<title>Monteur IA : tes Reels montés par ton IA | LeMondeDuMarketing</title>
<meta property="og:site_name" content="LeMondeDuMarketing"/>
<link rel="stylesheet" href="/_next/static/css/a.css"/>
<link rel="apple-touch-icon" sizes="180x180" href="/static/favicons/apple-touch-icon.png"/>
<link rel="icon" type="image/png" sizes="32x32" href="/static/favicons/favicon-32x32.png"/>
<link rel="mask-icon" href="/static/favicons/safari-pinned-tab.svg" color="#FFEE00"/>
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#fff"/>
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#202022"/>
</head><body>
<img src="/images/logos/instagram.svg" alt="Instagram logo" class="logo"/>
<img src="/images/logos/claude.svg" alt="Claude" class="h-6"/>
</body></html>"""

CSS = """:root{--color-primary-300:#fff247;--color-primary-400:#fe0;--color-primary-500:#e6d700;--color-gray-900:#202022}
@font-face{font-family:Brandsans;font-style:normal;font-weight:400;src:url(/_next/static/media/a-s.woff2) format("woff2");unicode-range:u+0900-097f,u+1cd0-1cf4}
@font-face{font-family:Brandsans;font-style:normal;font-weight:400;src:url(/_next/static/media/b-s.p.woff2) format("woff2");unicode-range:u+00??,u+0131,u+0152-0153}
@font-face{font-family:Brandsans;font-style:normal;font-weight:800;src:url(/_next/static/media/c-s.p.woff2) format("woff2");unicode-range:u+00??,u+0131}
body{font-family:Brandsans,ui-sans-serif,system-ui;background-color:#202022;color:#fff}
.btn{background-color:#fe0;color:#202022}.h1{color:#fff}.lien{color:#155dfc}"""

GOOGLE = """/* cyrillic */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/poppins/v24/cyr.woff2) format('woff2');
  unicode-range: U+0301, U+0400-045F, U+0490-0491;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/poppins/v24/lat400.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 800;
  src: url(https://fonts.gstatic.com/s/poppins/v24/lat800.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F;
}
"""


class Couleurs(unittest.TestCase):
    def test_lecture_des_couleurs(self):
        self.assertEqual(mq.hex_norme("#FE0"), "#ffee00")
        self.assertEqual(mq.hex_norme("#202022ff"), "#202022")
        self.assertEqual(mq.hex_norme("rgb(255, 238, 0)"), "#ffee00")
        self.assertEqual(mq.hex_norme("white"), "#ffffff")
        self.assertIsNone(mq.hex_norme("rgba(0, 0, 0, 0)"))
        self.assertIsNone(mq.hex_norme("transparent"))
        self.assertIsNone(mq.hex_norme("var(--x)"))

    def test_gris_jamais_accent(self):
        for gris in ("#202022", "#e4e4e4", "#8a8a8a", "#ffffff", "#000000"):
            self.assertFalse(mq.chromatique(gris), gris)
        for vive in ("#ffee00", "#155dfc", "#ff2e7e"):
            self.assertTrue(mq.chromatique(vive), vive)

    def test_page_lmdm(self):
        """Les indices de la capture réelle de la page Monteur IA (12/10/2026)."""
        indices = {
            "sections": [("hero", "#202022"), ("content", "#FFFFFF"), ("content", "#202022"), ("content", "#FFEE00")],
            "couleurs": ["#FFFFFF", "#202022", "#E4E4E4", "#E6D700", "#000000", "#FFEE00", "#8A8A8A", "#155DFC"],
            "titres": ["#FFFFFF", "#202022", "#FFFFFF"],
            "boutons": ["#000000"], "theme": ["#ffffff", "#202022"], "masque": "#FFEE00",
            "variables": {"--color-primary-400": "#ffee00", "--color-primary-500": "#e6d700"},
        }
        c = mq.choisir_couleurs(indices)
        self.assertEqual((c["fond"], c["texte"], c["accent"]), ("#202022", "#ffffff", "#ffee00"))
        self.assertIsNone(c["secondaire"])  # le bleu d'un détail de maquette n'est pas une couleur de marque

    def test_page_sans_couleur_vive(self):
        c = mq.choisir_couleurs({"sections": [("hero", "#ffffff")], "couleurs": ["#ffffff", "#111111", "#888888"]})
        self.assertEqual(c["fond"], "#ffffff")
        self.assertEqual(c["accent"], c["texte"])

    def test_deuxieme_couleur_de_marque(self):
        c = mq.choisir_couleurs({"sections": [("hero", "#0d1220"), ("content", "#58a6ff"), ("content", "#ff2e7e")],
                                 "boutons": ["#58a6ff"], "couleurs": ["#0d1220", "#58a6ff", "#ff2e7e"]})
        self.assertEqual((c["accent"], c["secondaire"]), ("#58a6ff", "#ff2e7e"))

    def test_nuances_regroupees(self):
        groupes = mq.regrouper({"#ffee00": 5, "#e6d700": 4, "#155dfc": 1})
        self.assertEqual(groupes[0], ("#ffee00", 9))

    def test_palette_d_image(self):
        sombre, blanc, jaune = bytes((32, 32, 34)), bytes((255, 255, 255)), bytes((255, 238, 0))
        pixels = sombre * 700 + blanc * 200 + jaune * 100
        c = mq.couleurs_depuis_palette(mq.palette_pixels(pixels))
        self.assertEqual(mq.distance(c["fond"], "#202022") < 20, True)
        self.assertEqual(c["texte"], "#ffffff")
        self.assertLess(mq.distance(c["accent"], "#ffee00"), 20)

    def test_style_lisible(self):
        s = mq.resoudre({"couleurs": {"fond": "#202022", "texte": "#131313", "accent": "#ffee00"}, "polices": {}})
        self.assertEqual(s["texte"], "#ffffff")
        self.assertEqual(s["sur_accent"], "#202022")
        depart = mq.resoudre(None)
        self.assertEqual((depart["fond"], depart["titres"], depart["corps"]), ("#f7f7f5", "Anton", "Inter"))


class PageHtmlEtCss(unittest.TestCase):
    def test_html(self):
        infos = mq.lire_html(PAGE, "https://www.exemple.fr/offre")
        self.assertEqual(infos["feuilles"], ["https://www.exemple.fr/_next/static/css/a.css"])
        self.assertEqual(infos["masque"], "#ffee00")
        self.assertEqual(infos["theme"], ["#ffffff", "#202022"])
        urls = [l["url"] for l in infos["logos"]]
        self.assertEqual(urls[0], "https://www.exemple.fr/static/favicons/apple-touch-icon.png")
        self.assertFalse(any("instagram" in u or "claude" in u for u in urls))
        self.assertEqual(mq.nom_du_site(infos, "https://www.exemple.fr/offre"), "LeMondeDuMarketing")

    def test_logo_du_site_avant_l_icone(self):
        html = '<link rel="apple-touch-icon" href="/i.png"><header><img src="/img/acme-logo.svg" alt="Acme"></header>'
        infos = mq.lire_html(html, "https://acme.fr/")
        self.assertEqual(infos["logos"][0]["url"], "https://acme.fr/img/acme-logo.svg")

    def test_faces_latines(self):
        faces = mq.faces_css(CSS, "https://www.exemple.fr/_next/static/css/a.css")
        self.assertEqual(len(faces), 3)
        latines = [(f["poids"], f["url"].rsplit("/", 1)[1]) for f in faces if f["latin"]]
        self.assertEqual(latines, [(400, "b-s.p.woff2"), (800, "c-s.p.woff2")])
        self.assertEqual(mq.familles_utilisees(CSS), ["Brandsans"])
        self.assertEqual(mq.variables_couleur(CSS)["--color-primary-400"], "#ffee00")
        self.assertEqual(mq.frequences_couleurs(CSS)["#202022"], 2)

    def test_plages_unicode(self):
        self.assertTrue(mq.couvre_latin("U+0000-00FF, U+0131"))
        self.assertTrue(mq.couvre_latin("u+00??,u+0131"))
        self.assertFalse(mq.couvre_latin("u+0900-097f,u+1cd0-1cf4"))
        self.assertFalse(mq.couvre_latin("u+0100-02ba"))
        self.assertTrue(mq.couvre_latin(None))

    def test_google_fonts_latin_seulement(self):
        faces = mq.faces_google(GOOGLE)
        self.assertEqual([(f["poids"], f["url"].rsplit("/", 1)[1]) for f in faces],
                         [(400, "lat400.woff2"), (800, "lat800.woff2")])

    def test_polices_d_apres_la_capture(self):
        capture = {"polices": {"titres": "Poppins", "corps": "Inter"}, "familles": ["Poppins"]}
        self.assertEqual(mq.choisir_polices(capture, [], []), {"titres": "Poppins", "corps": "Inter"})
        self.assertEqual(mq.choisir_polices({"polices": {"titres": "system-ui"}}, ["Brandsans"], []),
                         {"titres": "Brandsans", "corps": "Brandsans"})
        self.assertEqual(mq.choisir_polices(None, [], []), {"titres": "Anton", "corps": "Inter"})

    def test_page_de_bout_en_bout_sans_reseau(self):
        """Lien de la page -> marque.json, logo, police de la page installée, style généré."""
        reponses = {
            "https://www.exemple.fr/offre": (PAGE.encode(), "text/html"),
            "https://www.exemple.fr/_next/static/css/a.css": (CSS.encode(), "text/css"),
            "https://www.exemple.fr/static/favicons/apple-touch-icon.png": (PNG, "image/png"),
            "https://www.exemple.fr/_next/static/media/b-s.p.woff2": (WOFF2, "font/woff2"),
            "https://www.exemple.fr/_next/static/media/c-s.p.woff2": (WOFF2 + b"8", "font/woff2"),
        }

        def faux_telecharger(url, limite=0, accepte="*/*"):
            if url not in reponses:
                raise mq.ErreurMarque(f"{url} : 404")
            return reponses[url]

        def pas_google(famille, *a, **k):
            raise mq.ErreurMarque(f"« {famille} » n'est pas sur Google Fonts")

        with tempfile.TemporaryDirectory() as d, mock.patch.object(mq, "telecharger", faux_telecharger), \
                mock.patch.object(mq, "css_google", pas_google):
            racine = racine_vide(Path(d))
            marque, journal = mq.depuis_page(racine, "https://www.exemple.fr/offre", None)
            self.assertEqual(journal, [])
            self.assertEqual(marque["source"]["type"], "page")
            self.assertEqual(marque["nom"], "LeMondeDuMarketing")
            self.assertEqual((marque["couleurs"]["fond"], marque["couleurs"]["accent"]), ("#202022", "#ffee00"))
            self.assertEqual(marque["polices"], {"titres": "Brandsans", "corps": "Brandsans"})
            self.assertEqual(marque["logo"], "marque/logo.png")
            self.assertTrue((racine / "marque" / "logo.png").is_file())
            registre = mq.lire_registre(racine / "marque" / "polices")
            self.assertEqual([f["poids"] for f in registre["Brandsans"]["faces"]], [400, 800])
            self.assertIn("licence", registre["Brandsans"]["licence"])
            self.assertFalse(marque["valide"])
            mq.ecrire(racine, marque)
            s = mq.ecrire_style(racine)
            self.assertEqual(s["manquantes"], [])
            self.assertEqual(sm.polices_manquantes(racine), [])
            tokens = (racine / "brand" / "tokens.css").read_text(encoding="utf-8")
            self.assertIn("--brand-accent: #ffee00;", tokens)
            self.assertIn('--brand-font-display: "Brandsans"', tokens)
            self.assertIn('url("fonts/Brandsans-800.woff2")', (racine / "brand" / "fonts.css").read_text(encoding="utf-8"))
            self.assertTrue((racine / "brand" / "logo.png").is_file())

    def test_police_libre_preferee_a_celle_de_la_page(self):
        def faux_telecharger(url, limite=0, accepte="*/*"):
            if url == "https://fonts.googleapis.com/css2":
                return GOOGLE.encode(), "text/css"
            return WOFF2, "font/woff2"

        with tempfile.TemporaryDirectory() as d, mock.patch.object(mq, "telecharger", faux_telecharger), \
                mock.patch.object(mq, "css_google", lambda famille, *a, **k: GOOGLE):
            racine = racine_vide(Path(d))
            origine = mq.acquerir_police(racine, "Poppins", [])
            self.assertIn("Google Fonts", origine)
            self.assertEqual(sorted((racine / "marque" / "polices").glob("*.woff2"))[0].name, "Poppins-400.woff2")
            self.assertEqual(mq.acquerir_police(racine, "Inter"), "déjà disponible")


# Trois vraies pages de vente, enregistrées le 30/10/2026 et réduites à ce que lit la lecture de la
# marque (tests/pages/<site>/ : en-tête, feuille de style, capture HyperFrames, logo) : aucun réseau.
PAGES = RACINE / "tests" / "pages"
CAS = {
    "dupliq": ("https://dupliq.me", "Dupliq.me", "#ff5b00", "https://dupliq.me/favicon.svg"),
    "lmdm": ("https://www.lemondedumarketing.fr/monteur-ia", "LeMondeDuMarketing", "#ffee00",
             "https://www.lemondedumarketing.fr/static/favicons/apple-touch-icon.png"),
    "systeme": ("https://systeme.io/fr", "Systeme.io", "#00a0ff",
                "https://systeme.io/161/60a777c6b6c23_60a777c6b6c22_favicon.png"),
}


class PagesEnregistrees(unittest.TestCase):
    """Sur dupliq.me, la lecture prenait le titre de la page pour le nom (« Ton shooting photo avec
    l'IA ») et le jaune de deux onglets (#ffd447) pour la couleur, au lieu de l'orange des boutons, des
    liens et du logo (#ff5b00)."""

    def lire(self, site: str, avec_capture: bool = True) -> dict:
        url, _nom, _accent, logo = CAS[site]
        dossier = PAGES / site
        reponses = {url: ((dossier / "page.html").read_bytes(), "text/html"),
                    mq.urllib.parse.urljoin(url, "/feuille.css"): ((dossier / "feuille.css").read_bytes(), "text/css"),
                    logo: ((dossier / "logo.svg").read_bytes(), "image/svg+xml")}

        def faux_telecharger(adresse, limite=0, accepte="*/*"):
            if adresse not in reponses:
                raise mq.ErreurMarque(f"{adresse} : 404")
            return reponses[adresse]

        def fausse_capture(_hyperframes, _url, dest):
            shutil.copytree(dossier / "capture", dest)
            return dest

        def pas_google(famille, *a, **k):
            raise mq.ErreurMarque(f"« {famille} » : pas de réseau dans les tests")

        with tempfile.TemporaryDirectory() as d, mock.patch.object(mq, "telecharger", faux_telecharger), \
                mock.patch.object(mq, "capturer", fausse_capture), mock.patch.object(mq, "css_google", pas_google):
            marque, _journal = mq.depuis_page(racine_vide(Path(d)), url, ["hyperframes"] if avec_capture else None)
        return marque

    def test_nom_et_couleur_de_trois_pages(self):
        for site, (_url, nom, accent, _logo) in CAS.items():
            for avec_capture in (True, False):
                marque = self.lire(site, avec_capture)
                self.assertEqual((marque["nom"], marque["couleurs"]["accent"]), (nom, accent),
                                 f"{site}, capture : {avec_capture}")

    def test_le_logo_retenu_et_sa_couleur(self):
        marque = self.lire("dupliq")
        self.assertEqual(marque["logo"], "marque/logo.svg")
        self.assertTrue(any(n.endswith("couleur #ff6333") for n in marque["notes"]), marque["notes"])
        self.assertEqual(mq.couleur_logo(PAGES / "systeme" / "logo.svg"), "#01a2ff")
        self.assertIsNone(mq.couleur_logo(PAGES / "lmdm" / "page.html"))      # ni SVG ni image : rien

    def test_le_nom_ne_vient_jamais_du_titre(self):
        def nom(entete: str, url: str = "https://dupliq.me") -> str:
            return mq.nom_du_site(mq.lire_html(f"<head>{entete}</head>", url), url)
        titre = "<title>Dupliq.me | Ton shooting photo avec l'IA</title>"
        self.assertEqual(nom(titre), "Dupliq.me")
        self.assertEqual(nom(titre + '<meta property="og:site_name" content="Dupliq">'), "Dupliq")
        self.assertEqual(nom(titre + '<meta name="application-name" content="Dupliq App">'), "Dupliq App")
        self.assertEqual(nom(titre + '<img src="/a.svg" alt="Dupliq logo" class="h-8">'), "Dupliq")
        self.assertEqual(nom(titre + '<img src="/images/logos/claude.svg" alt="Claude">'), "Dupliq.me")
        self.assertEqual(nom('<meta property="og:site_name" content="Ton shooting photo avec l\'IA, en 3 clics">'),
                         "Dupliq.me")
        self.assertEqual(mq.nom_de_domaine("https://www.lemondedumarketing.fr/monteur-ia"), "Lemondedumarketing")
        self.assertEqual(mq.nom_de_domaine("https://lmdm.systeme.io/offre"), "Lmdm")
        self.assertEqual(mq.nom_de_domaine("https://boutique.exemple.co.uk/"), "Exemple")

    def test_les_boutons_d_action_avant_le_decor(self):
        css = ".hero{background:#ffd447}.carte{background-color:#ffd447}.btn-primary{background-color:#ff5b00}" \
              "a{color:#ff5b00}a:hover{color:#e55200}button{background-color:transparent}"
        actions, liens = mq.couleurs_actions_css(css)
        self.assertEqual((actions, liens), ({"#ff5b00": 1}, {"#ff5b00": 1, "#e55200": 1}))
        c = mq.choisir_couleurs({"sections": [("hero", "#f4f2f0"), ("content", "#ffd447"), ("content", "#ffd447")],
                                 "boutons": ["#ffd447", "#ffd447"], "actions_css": actions, "liens_css": liens,
                                 "variables": {"--accent-primary": "#ff5b00", "--accent-secondary": "#ffd447",
                                               "--accent-secondary-hover": "#f5c730"}})
        self.assertEqual(c["accent"], "#ff5b00")


class MonteurIA(unittest.TestCase):
    def dossier_monteur(self, base: Path) -> Path:
        m = base / "Monteur IA"
        (m / "templates").mkdir(parents=True)
        (m / "templates" / "AGENT.md.tpl").write_text("# Monteur IA\n", encoding="utf-8")
        (m / "brand.config.json").write_text(json.dumps({
            "brand": {"name": "Ma Marque", "handle": "@mamarque"},
            "visual": {"bg": "#202022", "accent": "#ffee00", "fontDisplay": "Titrage", "fontBody": "Inter"},
            "cta": {"defaultKeyword": "GUIDE"}, "audio": {"musicFile": "fond.mp3"}}), encoding="utf-8")
        (m / "brand" / "fonts").mkdir(parents=True)
        (m / "brand" / "tokens.css").write_text(
            ":root {\n  --brand-bg: #202022;\n  --brand-text: #131313;\n  --brand-accent: #ffee00;\n"
            "  --brand-surface: #2b2b2d;\n  --brand-font-display: Titrage, Impact, sans-serif;\n"
            "  --brand-font-body: Inter, Arial, sans-serif;\n}\n", encoding="utf-8")
        (m / "brand" / "fonts.css").write_text(
            '@font-face {\n  font-family: "Titrage";\n  font-style: normal;\n  font-weight: 700;\n'
            '  src: url("fonts/Titrage-700.woff2") format("woff2");\n}\n', encoding="utf-8")
        (m / "brand" / "fonts" / "Titrage-700.woff2").write_bytes(WOFF2)
        (m / "assets" / "logos").mkdir(parents=True)
        (m / "assets" / "logos" / "bytedance.svg").write_text("<svg/>", encoding="utf-8")
        (m / "assets" / "logos" / "claude.svg").write_text("<svg/>", encoding="utf-8")
        (m / "assets" / "logos" / "ma-marque.png").write_bytes(PNG)
        (m / "assets" / "music").mkdir(parents=True)
        (m / "assets" / "music" / "fond.mp3").write_bytes(b"ID3" + b"\x00" * 100)
        (m / "assets" / "sfx" / "pack").mkdir(parents=True)
        return m

    def test_reprise_sans_rien_modifier(self):
        with tempfile.TemporaryDirectory() as d:
            racine = racine_vide(Path(d))
            monteur = self.dossier_monteur(Path(d))
            avant = empreinte(monteur)
            marque = mq.depuis_monteur(racine, monteur)
            self.assertEqual(empreinte(monteur), avant)
            self.assertEqual(marque["source"]["type"], "monteur")
            # Son logo (« ma-marque.png ») est repris ; ByteDance et Claude, logos d'outils rangés au même endroit, jamais.
            self.assertEqual((marque["nom"], marque["mot_cle"]), ("Ma Marque", "GUIDE"))
            self.assertEqual(marque["couleurs"]["fond"], "#202022")
            self.assertEqual(marque["couleurs"]["texte"], "#ffffff")  # #131313 illisible sur ce fond
            self.assertEqual(marque["polices"], {"titres": "Titrage", "corps": "Inter"})
            self.assertTrue((racine / "marque" / "polices" / "Titrage-700.woff2").is_file())
            self.assertEqual(marque["logo"], "marque/logo.png")
            self.assertEqual(marque["musique"], "marque/musique.mp3")
            self.assertEqual(marque["monteur_ia"], str(monteur.resolve()))
            self.assertTrue(any("Pack SFX" in n for n in marque["notes"]))
            mq.ecrire(racine, marque)
            self.assertEqual(mq.ecrire_style(racine)["manquantes"], [])

    def test_logos_des_outils_jamais_pris_pour_le_sien(self):
        with tempfile.TemporaryDirectory() as d:
            racine = racine_vide(Path(d))
            monteur = self.dossier_monteur(Path(d))
            (monteur / "assets" / "logos" / "ma-marque.png").unlink()
            marque = mq.depuis_monteur(racine, monteur)
            self.assertIsNone(marque["logo"])
            self.assertTrue(any("aucun logo" in n for n in marque["notes"]))
            self.assertFalse(any((racine / "marque").glob("logo.*")))

    def test_pas_un_dossier_monteur(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(mq.ErreurMarque):
                mq.depuis_monteur(racine_vide(Path(d)), Path(d))


class Retouches(unittest.TestCase):
    def options(self, **kw):
        base = {c: None for c in ("fond", "texte", "accent", "secondaire", "surface", "titres", "corps", "nom",
                                  "mot_cle", "logo")}
        base.update(kw)
        return argparse.Namespace(**base)

    def test_regler_une_couleur_et_le_mot_cle(self):
        with tempfile.TemporaryDirectory() as d:
            racine = racine_vide(Path(d))
            depart = mq.nouvelle("page", "x", {"fond": "#202022", "accent": "#ffee00"}, {"titres": "Inter", "corps": "Inter"})
            depart["valide"] = True
            m = sm.regler(racine, depart, self.options(accent="#FF2E7E", mot_cle="guide", titres="Anton"))
            self.assertEqual(m["couleurs"]["accent"], "#ff2e7e")
            self.assertEqual((m["mot_cle"], m["polices"]["titres"]), ("GUIDE", "Anton"))
            self.assertFalse(m["valide"])
            with self.assertRaises(mq.ErreurMarque):
                sm.regler(racine, depart, self.options(fond="bleu"))


class NomDuProduit(unittest.TestCase):
    GENERES = {"node_modules", ".git", ".agents", "brand", "marque", "videos", "assets/vendor", "__pycache__"}
    TEXTES = (".md", ".py", ".mjs", ".js", ".json", ".tpl", ".html", ".css", ".txt")

    def fichiers(self):
        for f in RACINE.rglob("*"):
            rel = f.relative_to(RACINE).as_posix()
            if not f.is_file() or f.suffix.lower() not in self.TEXTES or rel in ("CLAUDE.md", "AGENTS.md"):
                continue
            if any(rel == g or rel.startswith(g + "/") for g in self.GENERES) or rel.startswith("Accueil "):
                continue
            yield rel, f.read_text(encoding="utf-8", errors="ignore")

    def test_aucun_ancien_nom(self):
        """Le nom provisoire et la version espagnole ont été abandonnés le 13/10/2026."""
        abandonnes = ("Studio " + "Motion IA", "INSTALL" + ".es", "studio" + "-motion/")  # écrits en morceaux : ce test se lit aussi
        fautifs = [rel for rel, texte in self.fichiers() if any(x in texte for x in abandonnes)]
        self.assertEqual(fautifs, [])
        self.assertFalse((RACINE / ("INSTALL" + ".es.md")).exists())

    def test_le_meme_nom_partout(self):
        produit = json.loads((RACINE / "produit.json").read_text(encoding="utf-8"))
        paquet = json.loads((RACINE / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(paquet["name"], produit["code"])
        self.assertTrue(produit["depot"].endswith("/" + produit["code"]))
        for doc in ("README.md", "INSTALL.md", ".claude/skills/studio/SKILL.md"):
            self.assertIn(produit["nom"], (RACINE / doc).read_text(encoding="utf-8"), doc)
        # La phrase d'installation de la formation, mot pour mot.
        phrase = (f"Télécharge {produit['nom']} depuis {produit['depot']} et suis les instructions "
                  "d'installation de son INSTALL.md")
        self.assertIn(phrase, (RACINE / "INSTALL.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
