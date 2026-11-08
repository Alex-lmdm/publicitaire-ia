"""Tests de tools/studio_motion.py : la partie qui ne dépend ni de ffmpeg ni de l'app.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import contextlib
import copy
import io
import json
import math
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))
import studio_motion as sm  # noqa: E402


def fiche_valide(objectif: str = "vente") -> dict:
    return {
        "produit": "Monteur IA",
        "lien": "https://www.lemondedumarketing.fr/monteur-ia",
        "objectif": objectif,
        "public": {"texte": "Créateurs qui postent des Reels", "source": "page"},
        "probleme": {"texte": "Trois heures de montage par Reel", "source": "page"},
        "promesse": {"texte": "Tes Reels montés par ton IA", "source": "page"},
        "mecanisme": {"texte": "21 skills de montage branchés à Claude", "source": "page"},
        "nouveaute": {"texte": "", "source": ""},
        "recoit": [{"texte": "Le système complet", "source": "page"}],
        "prix": {"montant": 97, "devise": "EUR", "barre": None, "source": "page"},
        "bonus": [{"texte": "Reel Cloneur offert", "source": "page"}],
        "garantie": {"texte": "", "source": ""},
        "dates": {"ouverture": "2026-10-16T18:00", "fermeture": "2026-10-19T23:59", "source": "client"},
        "preuves": [{"type": "chiffre", "texte": "3,3 millions de vues", "source": "page"}],
        "objections": [{"texte": "Pas besoin de savoir monter", "source": "page"}],
        "cta": {"mot_cle": "MONTEUR", "phrase": "Commente MONTEUR", "lien": "", "source": "client"},
        "interdits": [],
    }


class Videos(unittest.TestCase):
    def test_support_seul(self):
        self.assertEqual(sm.lire_video("reel"), {"support": "reel", "role": None, "format": "9x16"})

    def test_role_et_format(self):
        v = sm.lire_video("story:dernier-jour")
        self.assertEqual((v["role"], v["format"]), ("dernier-jour", "9x16"))
        self.assertEqual(sm.cle_video(v), "story-dernier-jour")
        p = sm.lire_video("page@1x1")
        self.assertEqual(sm.cle_video(p), "page-1x1")
        self.assertEqual(sm.nom_video(p), "Page de vente 1x1")

    def test_inconnus(self):
        for spec in ("snapchat", "story:demain", "reel@3x4", "Reel"):
            with self.assertRaises(ValueError):
                sm.lire_video(spec)

    def test_defauts_valides(self):
        for o in sm.OBJECTIFS.values():
            for spec in o["defaut"]:
                sm.lire_video(spec)

    def test_durees_coherentes(self):
        for cle, s in sm.SUPPORTS.items():
            lo, hi = s["ideal"]
            self.assertTrue(s["min"] <= lo <= hi <= s["max"], cle)
            self.assertIn(s["format"], sm.FORMATS)

    def test_bornes_demandees(self):
        # Une story tient dans un segment (60 s), Reel sous 45 s, page de vente sous 2 min.
        self.assertLessEqual(sm.SUPPORTS["story"]["ideal"][1], 60)
        self.assertLessEqual(sm.SUPPORTS["reel"]["ideal"][1], 45)
        self.assertLessEqual(sm.SUPPORTS["page"]["ideal"][1], 120)


class Installation(unittest.TestCase):
    def test_node_22_12_au_moins(self):
        """puppeteer-core (le navigateur de HyperFrames) exige Node 22.12 : un 22.11 passait `verifier`."""
        self.assertEqual(sm.version_node("v22.12.0\n"), (22, 12))
        self.assertGreaterEqual(sm.version_node("v26.13.0"), sm.NODE_MIN)
        self.assertLess(sm.version_node("v22.11.0"), sm.NODE_MIN)
        self.assertLess(sm.version_node("v20.19.5"), sm.NODE_MIN)
        self.assertIsNone(sm.version_node(""))
        with mock.patch("shutil.which", return_value="/usr/local/bin/node"), \
             mock.patch.object(sm, "lancer", return_value=mock.Mock(stdout="v22.11.0\n")):
            self.assertEqual(sm.node_installe(), (False, "v22.11.0"))
        with mock.patch("shutil.which", return_value=None):
            self.assertEqual(sm.node_installe(), (False, ""))

    def test_app_hyperframes_sur_mac_et_sous_windows(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            applications, maison, local = d / "Applications", d / "maison", d / "AppData" / "Local"
            for p in (applications, maison):
                p.mkdir()
            self.assertIsNone(sm.app_hyperframes("darwin", maison, {}, applications))
            (maison / "Applications" / "HyperFrames.app").mkdir(parents=True)
            self.assertEqual(sm.app_hyperframes("darwin", maison, {}, applications), maison / "Applications" / "HyperFrames.app")
            (applications / "HyperFrames.app").mkdir()
            self.assertEqual(sm.app_hyperframes("darwin", maison, {}, applications), applications / "HyperFrames.app")
            exe = local / "Programs" / "HyperFrames" / "HyperFrames.exe"
            self.assertIsNone(sm.app_hyperframes("win32", maison, {"LOCALAPPDATA": str(local)}, applications))
            exe.parent.mkdir(parents=True)
            exe.write_bytes(b"MZ")
            self.assertEqual(sm.app_hyperframes("win32", maison, {"LOCALAPPDATA": str(local)}, applications), exe)
            self.assertIsNone(sm.app_hyperframes("win32", maison, {}, applications))
            self.assertIsNone(sm.app_hyperframes("linux", maison, {}, applications))

    def test_ligne_de_l_app(self):
        with tempfile.TemporaryDirectory() as d:
            maison = Path(d)
            app = maison / "HyperFrames.exe"
            self.assertIsNone(sm.ligne_app(None, "win32", maison, {}))
            self.assertIn("`npm.cmd run app -- brancher`", sm.ligne_app(app, "win32", maison, {}))
            self.assertIn("`npm run app -- brancher`", sm.ligne_app(app, "darwin", maison, {}))
            config = maison / "config-claude"
            config.mkdir()
            (config / "settings.json").write_text('{"env": {"CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD": "1"}}',
                                                  encoding="utf-8")
            self.assertEqual(sm.ligne_app(app, "win32", maison, {"CLAUDE_CONFIG_DIR": str(config)}),
                             "ℹ️ app HyperFrames : installée et branchée")
            (config / "settings.json").write_text('["pas un objet"]', encoding="utf-8")
            self.assertIn("pas encore branchée", sm.ligne_app(app, "darwin", maison, {"CLAUDE_CONFIG_DIR": str(config)}))


class Lecture(unittest.TestCase):
    def test_plancher(self):
        self.assertEqual(sm.lecture("Nouveau"), 1.5)

    def test_par_mot(self):
        self.assertEqual(sm.lecture("Ton offre est bonne."), 2.0)
        self.assertEqual(sm.lecture("Tu donnes le lien de ta page de vente."), 3.5)

    def test_ecran_plan(self):
        # Sans voix, l'image raconte : un mot héros et une ligne d'appui, 8 mots au plus sur une image
        # (la story v2 en phrases entières, refusée le 07/11/2026 : « on dirait des sous-titres »).
        self.assertEqual((sm.MOTS_CONSEILLES, sm.MOTS_MAX), (4, 8))

    def test_budget_de_mots(self):
        # La story v2 refusée : 115 mots en 47,5 s ; la v3 : 36 mots en 40 s.
        v2 = sm.budget_mots(["mot " * 115], 47.5)
        self.assertTrue(v2["trop"])
        v3 = sm.budget_mots(["Cette story : ni filmée. ni montée.", "C'est Claude.", "mot " * 28], 40)
        self.assertFalse(v3["trop"])
        self.assertEqual(sm.budget_mots([], 10)["mots"], 0)
        self.assertEqual(sm.budget_mots(["un deux trois"], 3)["par_seconde"], 1.0)

    def test_lecture_de_plusieurs_plans(self):
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            sm.main(["lecture", "Ton lien.", "Tes vidéos.", "Touche le lien.", "--final", "--duree", "8"])
        texte = sortie.getvalue()
        self.assertIn("plan 1 · 1.5 s", texte)
        self.assertIn("plan 3 · 3.0 s", texte)
        self.assertIn("7 mots à lire en 8 s", texte)
        self.assertNotIn("trop de texte", texte)
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            sm.main(["lecture", "Ton lien.", "Tes vidéos.", "Touche le lien.", "--duree", "6"])
        self.assertIn("trop de texte", sortie.getvalue())

    def test_ecran_final(self):
        self.assertEqual(sm.lecture("Commente MONTEUR", final=True), 3.0)

    def test_durees_d_une_campagne(self):
        # Une story de lancement présente l'offre : l'ouverture vise 45 s, jamais 10 (essai du 06/11/2026).
        duree = lambda spec: sm.duree_cible(sm.lire_video(spec))
        self.assertEqual(duree("story:ouverture"), 45)
        self.assertEqual(duree("story:teaser"), 15)
        self.assertGreaterEqual(duree("story:dernier-jour"), 25)

    def test_ponctuation_seule(self):
        self.assertEqual(sm.lecture(" — ! "), 0.0)


class Palette(unittest.TestCase):
    """La story refusée du 06/11/2026 : des bruns tirés du jaune passaient tous les contrôles."""
    MARQUE = ["#202022", "#ffffff", "#ffee00", "#3b3b3d", "#9b9b9c"]

    def image(self, *couleurs):
        # Une image de 100 pixels, chaque couleur (hex, nombre de pixels) à la suite.
        octets = bytearray()
        for hexa, n in couleurs:
            octets += bytes(int(hexa[i:i + 2], 16) for i in (1, 3, 5)) * n
        return bytes(octets)

    def test_jaune_noir_blanc_et_gris_passent(self):
        img = self.image(("#ffee00", 40), ("#202022", 30), ("#ffffff", 20), ("#808080", 10))
        self.assertEqual(sm.verdict_palette([img] * 4, self.MARQUE)["plages"], [])

    def test_un_brun_tire_du_jaune_est_signale(self):
        brun = self.image(("#6c440c", 60), ("#202022", 40))
        v = sm.verdict_palette([self.image(("#ffee00", 100))] * 2 + [brun] * 3, self.MARQUE, fps=2)
        self.assertEqual(len(v["plages"]), 1)
        self.assertEqual((v["plages"][0]["debut"], v["plages"][0]["fin"]), (1.0, 2.5))
        self.assertIn("brun", " ".join(v["plages"][0]["couleurs"]))

    def test_un_lissage_de_bord_ne_suffit_pas(self):
        # Quelques pixels de bord (jaune à demi sur noir) restent sous le seuil.
        img = self.image(("#ffee00", 49), ("#202022", 49), ("#807710", 2))
        self.assertEqual(sm.verdict_palette([img], self.MARQUE)["plages"], [])

    def test_couleurs_lues_dans_les_jetons(self):
        css = "--brand-bg: #202022;\n--brand-accent: #ffee00;\n--brand-text: #FFFFFF;\n--brand-sombre: #202022;"
        self.assertEqual(sm.couleurs_marque(css), ["#202022", "#ffffff", "#ffee00"])

    def test_les_objets_connus_gardent_leurs_couleurs(self):
        """08/11/2026 : « jaune, noir, blanc, on ne voit que ça ». Le dossier bleu du Mac, un PDF, les
        boutons d'une fenêtre passent ; le brun tiré du jaune reste signalé."""
        img = self.image(("#ffee00", 30), ("#202022", 30), ("#5db6f7", 20), ("#2f8fe6", 8), ("#d42d28", 6),
                         ("#28c840", 6))
        self.assertEqual(sm.verdict_palette([img] * 3, self.MARQUE)["plages"], [])
        self.assertEqual(len(sm.verdict_palette([img] * 3, self.MARQUE, connues=())["plages"]), 1)
        brun = self.image(("#6c440c", 60), ("#202022", 40))
        self.assertEqual(len(sm.verdict_palette([brun] * 3, self.MARQUE)["plages"]), 1)

    def test_le_kit_et_la_palette_connaissent_les_memes_couleurs(self):
        """Chaque teinte d'un objet connu du kit (objets.js, lignes « couleur d'outil » de kit.css) est
        dans COULEURS_CONNUES : sinon `palette` refuserait le kit lui-même."""
        kit = RACINE / "templates" / "kit"
        textes = [(kit / "objets.js").read_text(encoding="utf-8")]
        textes += [l for l in (kit / "kit.css").read_text(encoding="utf-8").splitlines() if "couleur d'outil" in l]
        teintes = set()
        for h in re.findall(r"#([0-9a-fA-F]{6})\b", "\n".join(textes)):
            L, a, b = sm.oklab(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))
            if math.hypot(a, b) >= sm.NEUTRE_MAX:
                teintes.add("#" + h.lower())
        self.assertTrue(teintes)
        self.assertLessEqual(teintes, set(sm.COULEURS_CONNUES))

    def test_les_logos_du_projet(self):
        with tempfile.TemporaryDirectory() as t:
            projet = Path(t)
            self.assertEqual(sm.couleurs_des_logos(projet), [])
            (projet / "kit").mkdir()
            (projet / "kit" / "ajouts.js").write_text('window.K_ICONES = Object.assign(window.K_ICONES || {}, '
                                                       '{"logo-stripe": "<svg fill=\\"#635BFF\\"><path fill=\\"#fff\\"/></svg>"});',
                                                       encoding="utf-8")
            self.assertEqual(sm.couleurs_des_logos(projet), ["#635bff", "#ffffff"])


class Zones(unittest.TestCase):
    def test_reel_en_pixels(self):
        z = sm.zone_texte("reel")
        self.assertEqual((z["x"], z["y"]), (100, 300))
        self.assertEqual(z["x"] + z["largeur"], 1080 - 150)
        self.assertEqual(z["y"] + z["hauteur"], 1920 - 480)

    def test_paysage(self):
        z = sm.zone_texte("page")
        self.assertEqual((z["x"], z["y"]), (96, 65))
        self.assertTrue(sm.dans(z, {"x": 0, "y": 0, "largeur": 1920, "hauteur": 1080}))

    def test_format_force(self):
        z = sm.zone_texte("linkedin", "4x5")
        self.assertEqual(z["y"] + z["hauteur"], 1350 - 135)

    def test_sticker_dans_la_zone_story(self):
        self.assertTrue(sm.dans(sm.zone_sticker(), sm.zone_texte("story")))

    def test_pub_plus_stricte_que_reel(self):
        self.assertLess(sm.zone_texte("pub")["hauteur"], sm.zone_texte("reel")["hauteur"])

    def test_tiktok_zone_meta(self):
        # Zone utile publiée pour TikTok : x 122-838, y 254-1213 (à 2 px près).
        z = sm.zone_texte("tiktok")
        self.assertAlmostEqual(z["x"], 122, delta=2)
        self.assertAlmostEqual(z["x"] + z["largeur"], 838, delta=2)
        self.assertAlmostEqual(z["y"] + z["hauteur"], 1213, delta=2)

    def test_pub_zone_meta(self):
        # Zone utile publiée par Meta pour les Reels et Stories sponsorisés : y 269-1248.
        z = sm.zone_texte("pub")
        self.assertAlmostEqual(z["y"], 269, delta=2)
        self.assertAlmostEqual(z["y"] + z["hauteur"], 1248, delta=2)

    def test_chevauchement(self):
        a = {"x": 0, "y": 0, "largeur": 10, "hauteur": 10}
        self.assertTrue(sm.chevauche(a, {"x": 5, "y": 5, "largeur": 10, "hauteur": 10}))
        self.assertFalse(sm.chevauche(a, {"x": 10, "y": 0, "largeur": 5, "hauteur": 5}))


class Fiche(unittest.TestCase):
    def test_fiche_valide(self):
        self.assertEqual(sm.verifier_fiche(fiche_valide(), [sm.lire_video("story:dernier-jour")]), [])

    def test_fait_sans_source(self):
        f = fiche_valide()
        f["bonus"][0]["source"] = ""
        self.assertTrue(any("bonus[0]" in p for p in sm.verifier_fiche(f)))

    def test_texte_sans_source(self):
        f = fiche_valide()
        f["mecanisme"]["source"] = ""
        self.assertIn("mecanisme : sans source.", sm.verifier_fiche(f))

    def test_vente_sans_probleme(self):
        f = fiche_valide()
        f["probleme"] = {"texte": "", "source": ""}
        self.assertTrue(any(p.startswith("probleme") for p in sm.verifier_fiche(f)))

    def test_nouveaute_exige_la_nouveaute(self):
        f = fiche_valide("nouveaute")
        self.assertTrue(any(p.startswith("nouveaute") for p in sm.verifier_fiche(f)))
        f["nouveaute"] = {"texte": "Module Reel Cloneur", "source": "page"}
        self.assertEqual(sm.verifier_fiche(f), [])

    def test_preuve_exige_une_preuve(self):
        f = fiche_valide("preuve")
        f["preuves"] = []
        self.assertTrue(any(p.startswith("preuves") for p in sm.verifier_fiche(f)))

    def test_temoignage_mot_pour_mot(self):
        f = fiche_valide()
        f["preuves"].append({"type": "temoignage", "texte": "Génial", "source": "page"})
        self.assertTrue(any("mot pour mot" in p for p in sm.verifier_fiche(f)))

    def test_dernier_jour_sans_fermeture(self):
        f = fiche_valide()
        f["dates"]["fermeture"] = None
        pb = sm.verifier_fiche(f, [sm.lire_video("story:dernier-jour")])
        self.assertTrue(any("dernier jour" in p for p in pb))

    def test_prix_barre_doit_etre_plus_haut(self):
        f = fiche_valide()
        f["prix"]["barre"] = 67
        self.assertTrue(any("prix.barre" in p for p in sm.verifier_fiche(f)))

    def test_promesse_trop_longue(self):
        f = fiche_valide()
        f["promesse"]["texte"] = "Une promesse beaucoup trop longue pour tenir sur un écran de téléphone"
        self.assertTrue(any(p.startswith("promesse") and "mots" in p for p in sm.verifier_fiche(f)))

    def test_cta_par_lien_suffit(self):
        f = fiche_valide()
        f["cta"] = {"mot_cle": "", "phrase": "", "lien": "https://exemple.fr", "source": "page"}
        self.assertEqual(sm.verifier_fiche(f), [])

    def test_mot_cle(self):
        f = fiche_valide()
        f["cta"]["mot_cle"] = "mon mot"
        self.assertTrue(any("mot_cle" in p for p in sm.verifier_fiche(f)))

    def test_dates_dans_l_ordre(self):
        f = fiche_valide()
        f["dates"]["fermeture"] = "2026-10-01"
        self.assertTrue(any("fermeture doit suivre" in p for p in sm.verifier_fiche(f)))

    def test_fiche_vide_signale_l_essentiel(self):
        pb = sm.verifier_fiche(copy.deepcopy(sm.FICHE_VIDE))
        for debut in ("produit", "promesse", "probleme", "cta"):
            self.assertTrue(any(p.startswith(debut) for p in pb), debut)


class Echeances(unittest.TestCase):
    def test_echeance_valide(self):
        f = fiche_valide()
        f["echeances"] = [{"texte": "Bonus Reel Cloneur offert", "date": "2026-10-17T23:59", "source": "page"}]
        self.assertEqual(sm.verifier_fiche(f), [])

    def test_echeance_sans_date_ni_source(self):
        f = fiche_valide()
        f["echeances"] = [{"texte": "Bonus", "date": "samedi", "source": "page"}, {"texte": "Prix", "date": "2026-10-20", "source": ""}]
        pb = sm.verifier_fiche(f)
        self.assertTrue(any("echeances[0]" in p and "date" in p for p in pb))
        self.assertTrue(any("echeances[1]" in p and "source" in p for p in pb))

    def test_source_fichier_absente(self):
        with tempfile.TemporaryDirectory() as d:
            dossier = Path(d)
            (dossier / "sources").mkdir()
            (dossier / "sources" / "prix.png").write_bytes(b"x")
            f = fiche_valide()
            f["prix"]["source"] = "prix.png"
            f["bonus"][0]["source"] = "bonus.png"
            self.assertEqual(sm.sources_absentes(f, dossier), ["bonus.png"])


class Polices(unittest.TestCase):
    def test_police_sans_fichier(self):
        with tempfile.TemporaryDirectory() as d:
            m = Path(d)
            (m / "brand").mkdir()
            (m / "brand" / "tokens.css").write_text(':root{ --brand-font-display: Poppins, Impact, sans-serif; --brand-font-body: Inter, Arial; }', encoding="utf-8")
            (m / "brand" / "fonts.css").write_text('@font-face { font-family: "Inter"; src: url(x.woff2); }', encoding="utf-8")
            self.assertEqual(sm.polices_manquantes(m), ["Poppins"])
            (m / "brand" / "fonts.css").write_text('@font-face { font-family: "Inter"; } @font-face { font-family: "Poppins"; }', encoding="utf-8")
            self.assertEqual(sm.polices_manquantes(m), [])


class Sticker(unittest.TestCase):
    def test_story_avec_lien_par_defaut(self):
        self.assertTrue(sm.avec_sticker(sm.lire_video("story")))
        self.assertTrue(sm.avec_sticker(sm.lire_video("story:ouverture")))
        self.assertFalse(sm.avec_sticker(sm.lire_video("story:teaser")))
        self.assertFalse(sm.avec_sticker(sm.lire_video("reel")))

    def test_inserer_section(self):
        plan = "# T\n\n## Vidéos\n\n### Reel\n\n## Livraison\n\nx\n"
        sortie = sm.inserer_section(plan, "### Story\n")
        self.assertLess(sortie.index("### Story"), sortie.index("## Livraison"))
        self.assertGreater(sortie.index("### Story"), sortie.index("### Reel"))
        self.assertTrue(sm.inserer_section("# T\n", "### Story\n").endswith("### Story\n"))


class Rythme(unittest.TestCase):
    """Le verdict se calcule sur les écarts entre images (10 par seconde)."""

    def test_video_vivante(self):
        # Un pic toutes les 0,5 s, un léger mouvement entre deux : ok.
        ecarts = [3.0 if i % 5 == 0 else 0.8 for i in range(1, 300)]
        v = sm.verdict_rythme(ecarts)
        self.assertEqual(v["problemes"], [])
        self.assertGreaterEqual(v["evenements_par_s"], 1.9)
        self.assertLessEqual(v["ecart_median"], 0.5)

    def test_slides_refusees(self):
        # Un changement toutes les 4 s, rien entre deux : figé, trop peu d'événements.
        ecarts = [5.0 if i % 40 == 0 else 0.0 for i in range(1, 400)]
        v = sm.verdict_rythme(ecarts)
        self.assertTrue(v["figees"])
        self.assertEqual(len(v["problemes"]), 3)

    def test_phrase_tenue_sa_lecture(self):
        # Recalage du 06/11/2026 : un geste toutes les 1,2 s, une dérive lente entre deux (une phrase
        # tenue le temps de la lire, la matière qui vit autour) : ok, rien de figé.
        ecarts = [3.0 if i % 12 == 0 else 0.15 for i in range(1, 400)]
        v = sm.verdict_rythme(ecarts)
        self.assertEqual(v["problemes"], [])
        self.assertEqual(v["figees"], [])
        # La même tenue sans aucune dérive (un texte posé sur un aplat) : figée.
        ecarts = [3.0 if i % 20 == 0 else 0.0 for i in range(1, 400)]
        self.assertTrue(sm.verdict_rythme(ecarts)["figees"])

    def test_ecran_final_libre(self):
        vivant = [3.0 if i % 5 == 0 else 0.8 for i in range(1, 200)]
        v = sm.verdict_rythme(vivant + [0.0] * 30)   # 3 s tenues à la fin
        self.assertEqual(v["figees"], [])
        self.assertEqual(v["problemes"], [])
        v = sm.verdict_rythme(vivant[:100] + [0.0] * 30 + vivant[100:])   # 3 s figées au milieu
        self.assertEqual(v["figees"], [(10.0, 3.0)])

    def test_boucle_sans_ecran_final(self):
        ecarts = [3.0 if i % 5 == 0 else 0.8 for i in range(1, 100)] + [0.0] * 20
        self.assertTrue(sm.verdict_rythme(ecarts, fin_libre=0.0)["figees"])


class Calage(unittest.TestCase):
    """`calage` : le montage suit la musique et la voix (audit du 08/11/2026 : la méthode calait la
    musique, rien ne vérifiait que l'image suivait)."""
    GRILLE = [round(0.5 * k, 3) for k in range(0, 41)]          # 120 battements par minute, 20 s

    def test_scenes_sur_les_temps(self):
        v = sm.verdict_calage([0, 3.5, 9.0, 13.5], self.GRILLE, [], 3.5, 2.0)
        self.assertEqual((v["problemes"], v["calees"], v["comptees"]), ([], 3, 3))

    def test_une_scene_hors_du_temps(self):
        v = sm.verdict_calage([0, 3.9, 8.0], self.GRILLE, [], None, None)
        self.assertEqual(len(v["problemes"]), 1)
        self.assertIn("3.90 s tombe à 0.10 s du temps (4.00 s)", v["problemes"][0])
        self.assertIn("arrondis la durée", v["problemes"][0])

    def test_une_image_pres_du_temps_suffit(self):
        self.assertEqual(sm.verdict_calage([4.033], self.GRILLE, [], None, None)["problemes"], [])

    def test_rien_ne_se_voit_sur_l_entree(self):
        v = sm.verdict_calage([0, 4.0], self.GRILLE, [], 3.5, 0.4)
        self.assertTrue(any("la batterie entre à 3.50 s" in p for p in v["problemes"]))

    def test_avec_une_voix_la_scene_part_avec_sa_phrase(self):
        mots = [(1.0, 1.4, "Ton"), (1.45, 1.9, "offre"), (4.2, 4.6, "Elle"), (4.65, 5.1, "vend")]
        v = sm.verdict_calage([0, 4.1], self.GRILLE, mots, None, None)     # 4,1 : hors temps, mais avec « Elle »
        self.assertEqual((v["problemes"], v["calees"]), ([], 1))
        v = sm.verdict_calage([0, 1.6], self.GRILLE, mots, None, None)     # au milieu de « offre »
        self.assertIn("coupe le mot « offre »", v["problemes"][0])
        v = sm.verdict_calage([0, 2.7], self.GRILLE, mots, None, None)     # ni temps ni phrase
        self.assertIn("ni sur un temps", v["problemes"][0])

    def test_la_batterie_n_entre_pas_sous_un_mot(self):
        mots = [(3.3, 3.8, "Publicitaire")]
        v = sm.verdict_calage([0], self.GRILLE, mots, 3.5, 2.0)
        self.assertTrue(any("sous le mot « Publicitaire »" in p for p in v["problemes"]))

    def test_les_scenes_avant_la_musique_ne_comptent_pas(self):
        grille = [round(2.0 + 0.5 * k, 3) for k in range(0, 20)]   # la musique part à 2 s
        v = sm.verdict_calage([0, 1.3, 2.5], grille, [], None, None)
        self.assertEqual((v["problemes"], v["comptees"]), ([], 1))

    def test_la_grille_de_la_musique(self):
        temps = sm.temps_de_la_grille({"bpm": 120.0, "phase": 0.01}, 0.0, 0.0, 2.0)
        self.assertEqual(temps, [0.01, 0.51, 1.01, 1.51])
        temps = sm.temps_de_la_grille({"bpm": 120.0, "phase": 0.2}, 1.0, 0.0, 2.5)    # posée à 1 s
        self.assertEqual(temps, [1.2, 1.7, 2.2])

    def test_le_geste_autour_de_l_entree(self):
        ecarts = [0.5] * 300
        ecarts[104] = 40.0                                                  # l'image 105, à 3,5 s
        self.assertGreaterEqual(sm.geste_autour(ecarts, 30.0, 3.5), 1)
        self.assertLess(sm.geste_autour(ecarts, 30.0, 6.0), 1)

    def test_les_pistes_et_les_mots(self):
        with tempfile.TemporaryDirectory() as t:
            projet = Path(t)
            (projet / "index.html").write_text(
                '<audio data-hf-id="hf-1" id="musique" src="assets/audio/musique.wav" data-start="0.5" '
                'data-duration="20" data-media-start="0"></audio>'
                '<audio id="voix" src="assets/audio/voix.wav" data-start="0.300" data-duration="18" '
                'data-media-start="0"></audio><audio id="sfx-01" src="a.mp3" data-start="1"></audio>', encoding="utf-8")
            pistes = sm.pistes_audio(projet)
            self.assertEqual(sorted(pistes), ["musique", "voix"])               # pas l'identifiant de l'app
            self.assertEqual((pistes["musique"]["debut"], pistes["musique"]["duree"]), (0.5, 20.0))
            (projet / "assets" / "audio").mkdir(parents=True)
            (projet / "assets" / "audio" / "transcript.json").write_text(json.dumps(
                [{"text": "Ton", "start": 0.1, "end": 0.4}, {"text": "offre", "start": 0.45, "end": 0.9}]), encoding="utf-8")
            self.assertEqual(sm.mots_de_la_voix(projet, 0.3), [(0.4, 0.7, "Ton"), (0.75, 1.2, "offre")])
            self.assertIsNone(sm.entree_voulue(projet))
            (projet / "work").mkdir()
            (projet / "work" / "musiques.json").write_text(json.dumps({"a": 6.0}), encoding="utf-8")
            self.assertIsNone(sm.entree_voulue(projet))                         # proposé, pas encore pris
            (projet / "work" / "musiques.json").write_text(json.dumps({"a": 6.0, "pris": "x"}), encoding="utf-8")
            self.assertEqual(sm.entree_voulue(projet), 6.0)
            (projet / "work" / "sons.json").write_text(json.dumps({"musique_entree": 5.5}), encoding="utf-8")
            self.assertEqual(sm.entree_voulue(projet), 5.5)

    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg absent")
    def test_sur_un_vrai_rendu(self):
        """Une musique à 120 dont la batterie entre à 4 s, une vidéo qui flashe à 4 s, trois scènes :
        « ok » ; une scène poussée de 0,2 s hors du temps, ou un flash ailleurs : refusé."""
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d)
            (projet / "assets" / "audio").mkdir(parents=True)
            (projet / "exports").mkdir()
            (projet / "meta.json").write_text(json.dumps({"support": "page"}), encoding="utf-8")
            kick = "sin(2*PI*55*t)*exp(-30*mod(t,0.5))*if(lt(t,4),0.08,0.9)"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"aevalsrc='{kick}':d=12:s=44100",
                            "-f", "lavfi", "-i", "sine=f=330:d=12", "-filter_complex",
                            "[1]volume='if(lt(t,4),0.01,0.2)':eval=frame[b];[0][b]amix=inputs=2:normalize=0",
                            "-ar", "44100", str(projet / "assets" / "audio" / "musique.wav")], check=True)

            def rendre(flash: float) -> Path:
                video = projet / "exports" / "page.mp4"
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=gray:s=320x180:r=30:d=12",
                                "-vf", f"drawbox=x=0:y=0:w=320:h=180:color=white:t=fill:enable='between(t,{flash},{flash + 0.2})'",
                                "-pix_fmt", "yuv420p", str(video)], check=True)
                return video

            def monter(debuts: list[float]) -> None:
                hotes = "".join(f'<div data-composition-src="compositions/s{i}.html" data-start="{t}" data-duration="4" '
                                f'data-track-index="1"></div>' for i, t in enumerate(debuts))
                (projet / "index.html").write_text(hotes + '<audio id="musique" src="assets/audio/musique.wav" '
                                                   'data-start="0" data-duration="12" data-media-start="0"></audio>',
                                                   encoding="utf-8")

            def calage(video: Path) -> tuple[int, str]:
                sortie = io.StringIO()
                with contextlib.redirect_stdout(sortie):
                    try:
                        sm.main(["calage", str(video)])
                        return 0, sortie.getvalue()
                    except SystemExit as e:
                        return int(e.code or 0), sortie.getvalue()

            video = rendre(4.0)
            monter([0, 4.0, 8.0])
            code, texte = calage(video)
            self.assertEqual(code, 0, texte)
            self.assertIn("tempo 120", texte)
            self.assertIn("2/2 scènes calées", texte)
            monter([0, 4.2, 8.0])
            code, texte = calage(video)
            self.assertEqual(code, 1, texte)
            self.assertIn("4.20 s tombe à 0.20 s du temps", texte)
            monter([0, 4.0, 8.0])
            code, texte = calage(rendre(6.3))
            self.assertEqual(code, 1, texte)
            self.assertIn("l'image ne fait rien de fort autour", texte)


class Scenes(unittest.TestCase):
    """Le montage lu dans index.html : des durées variées, peu de coupes franches nues."""

    def index(self, dossier: Path, hotes: list[tuple[float, float, int]]) -> Path:
        lignes = [f'<div id="s{k}-hote" data-composition-id="s{k}" data-composition-src="compositions/s{k}.html" '
                  f'data-start="{d}" data-duration="{l}" data-track-index="{piste}"></div>'
                  for k, (d, l, piste) in enumerate(hotes)]
        (dossier / "index.html").write_text("<body>\n" + "\n".join(lignes) + "\n</body>", encoding="utf-8")
        return dossier

    def test_scenes_de_la_piste_principale(self):
        with tempfile.TemporaryDirectory() as t:
            projet = self.index(Path(t), [(0, 3.5, 1), (3.5, 6, 1), (9.5, 4, 1), (3.5, 6, 5)])
            self.assertEqual(sm.scenes_du_projet(projet), [(0.0, 3.5), (3.5, 6.0), (9.5, 4.0)])

    def test_durees_toutes_egales(self):
        calmes = [0.5] * 200
        egales = [(i * 4.0, 4.0) for i in range(5)]
        self.assertTrue(any("durent presque toutes" in p for p in sm.verdict_scenes(calmes, egales)))
        variees = [(0, 2.5), (2.5, 7.0), (9.5, 3.0), (12.5, 5.5), (18, 2.0)]
        self.assertEqual(sm.verdict_scenes(calmes, variees), [])

    def test_coupes_franches_nues(self):
        scenes = [(0, 3.0), (3.0, 4.5), (7.5, 2.5), (10.0, 6.0)]
        nues = [0.5] * 200
        for d, _l in scenes[1:]:
            nues[round(d * 10) - 1] = 90.0            # un saut d'image, rien ne bouge autour
        self.assertTrue(any("coupes franches nues" in p for p in sm.verdict_scenes(nues, scenes)))
        portees = [0.5] * 200
        for d, _l in scenes[1:]:
            i = round(d * 10) - 1
            portees[i - 1], portees[i], portees[i + 1] = 45.0, 90.0, 60.0   # un flash, un volet : ça bouge autour
        self.assertEqual(sm.verdict_scenes(portees, scenes), [])


class Cadre(unittest.TestCase):
    """Le sujet remplit-il l'image ? Mesuré case par case sur le MP4 rendu."""

    def image(self, w: int, h: int, fond=(27, 27, 29), rectangles=()) -> bytes:
        px = bytearray(bytes(fond) * (w * h))
        for (x0, y0, x1, y1, couleur) in rectangles:
            for y in range(y0, y1):
                for x in range(x0, x1):
                    i = (y * w + x) * 3
                    px[i:i + 3] = bytes(couleur)
        return bytes(px)

    def test_taille_de_lecture(self):
        self.assertEqual(sm.taille_cadre(1080, 1920), (128, 224))
        self.assertEqual(sm.taille_cadre(1920, 1080), (224, 128))

    def test_fond_vide_puis_sujet_qui_remplit(self):
        w, h = 128, 224
        self.assertEqual(sm.occupation(self.image(w, h), w, h), 0.0)
        # Une petite pastille au centre : presque vide.
        petit = self.image(w, h, rectangles=[(56, 104, 72, 120, (255, 238, 0))])
        self.assertLess(sm.occupation(petit, w, h), sm.OCCUPATION_MIN)
        # Une fenêtre qui prend les trois quarts de la largeur et la moitié de la hauteur : rempli.
        grand = self.image(w, h, rectangles=[(16, 56, 112, 168, (245, 245, 245))])
        self.assertGreater(sm.occupation(grand, w, h), 0.3)

    def test_une_grille_fine_et_une_vignette_ne_comptent_pas(self):
        w, h = 128, 224
        grille = [(x, 0, x + 1, h, (40, 40, 42)) for x in range(0, w, 8)]
        vignette = [(0, 0, w, 12, (14, 14, 15)), (0, h - 12, w, h, (14, 14, 15))]
        self.assertEqual(sm.occupation(self.image(w, h, rectangles=grille + vignette), w, h), 0.0)

    def test_un_mot_heros_se_tient_seul(self):
        w, h = 128, 224
        # Un mot très grand qui traverse l'écran (80 % de la largeur, 9 % de la hauteur) : rempli.
        heros = self.image(w, h, rectangles=[(12, 100, 115, 120, (255, 255, 255))])
        self.assertGreaterEqual(sm.occupation(heros, w, h), sm.OCCUPATION_MIN)
        # Une ligne de petit texte aussi large (3 % de la hauteur) : presque vide.
        ligne = self.image(w, h, rectangles=[(12, 108, 115, 115, (255, 255, 255))])
        self.assertLess(sm.occupation(ligne, w, h), sm.OCCUPATION_MIN)

    def test_plages_presque_vides(self):
        occ = [0.4] * 8 + [0.05] * 6 + [0.4] * 8 + [0.05] * 2 + [0.4] * 4   # 1,5 s vide, puis 0,5 s
        v = sm.verdict_cadre(occ, fps=4)
        self.assertEqual([(p["debut"], p["fin"]) for p in v["plages"]], [(2.0, 3.5)])
        self.assertAlmostEqual(v["mediane"], 0.4)


class Musique(unittest.TestCase):
    FPS = 100.0

    def pulsations(self, bpm, duree=40.0, debut=0.0):
        env, pas = [], 60 * self.FPS / bpm
        for i in range(int(duree * self.FPS)):
            k = (i - debut * self.FPS) / pas
            env.append(1000.0 if i >= debut * self.FPS and k - int(k) < 0.08 else 10.0)
        return env

    def test_tempo(self):
        self.assertAlmostEqual(sm.tempo_de(self.pulsations(122.7), self.FPS), 122.7, delta=0.3)
        self.assertAlmostEqual(sm.tempo_de(self.pulsations(100.0), self.FPS), 100.0, delta=0.3)

    def test_phase_sur_l_attaque(self):
        env = self.pulsations(120.0, debut=0.2)
        self.assertAlmostEqual(sm.phase_de(env, self.FPS, 120.0) % 0.5, 0.2, delta=0.02)

    def test_entree_franche(self):
        env = [10.0] * 800 + [1000.0] * 800      # silence relatif puis entrée à 8 s
        self.assertAlmostEqual(sm.entree_de(env, self.FPS), 8.0, delta=0.26)
        self.assertIsNone(sm.entree_de([10.0] * 2000, self.FPS))

    def test_calage(self):
        # Le morceau de la démo : 122,7 bpm, temps fort à 0,39 s, entrée à 7,73 s -> 8,0 s dans la vidéo.
        c = sm.calage(7.73, 0.39, 122.7, 120.0, 8.0)
        self.assertAlmostEqual(c["facteur"], 0.977995, places=4)
        self.assertAlmostEqual(c["entree"] - c["decalage"], 8.0, places=2)
        self.assertEqual(sm.calage(7.73, 0.39, 122.7, 0, 8.0)["facteur"], 1.0)      # tempo gardé
        self.assertEqual(sm.calage(5.0, 0.0, 150.0, 120.0, 8.0)["facteur"], 1.0)    # écart trop grand
        self.assertLess(sm.calage(2.0, 0.0, 120.0, 120.0, 8.0)["decalage"], 0)      # démarre plus tard


    def test_premier_temps_fort(self):
        self.assertAlmostEqual(sm.premier_temps_fort(self.pulsations(124.0, debut=0.3), self.FPS), 0.3, delta=0.011)
        self.assertEqual(sm.premier_temps_fort(self.pulsations(100.0), self.FPS), 0.0)
        self.assertEqual(sm.premier_temps_fort([0.0] * 500, self.FPS), 0.0)          # muet : rien à couper
        self.assertEqual(sm.premier_temps_fort([], self.FPS), 0.0)

    def test_calage_sans_entree(self):
        c = sm.calage_sans_entree(0.25, 124.0, 120.0)
        self.assertAlmostEqual(c["facteur"], 120 / 124, places=5)
        self.assertAlmostEqual(c["decalage"], 0.25 * 124 / 120, places=3)          # le premier temps à 0 s
        self.assertEqual(sm.calage_sans_entree(0.1, 100.0, 120.0), {"facteur": 1.0, "entree": 0.1, "decalage": 0.1})

    def test_message_sans_entree(self):
        recale = sm.message_sans_entree("m.wav", sm.calage_sans_entree(0.0, 124.0, 120.0), 124.0, 120.0)
        self.assertIn("pas d'entrée franche", recale)
        self.assertIn("premier temps fort du morceau est calé au début de la vidéo, tempo ramené à 120 (-3.2 %)", recale)
        self.assertTrue(recale.endswith("chaque temps tombe sur la grille de 0.5 s."))
        garde = sm.message_sans_entree("m.wav", sm.calage_sans_entree(0.0, 100.2, 120.0), 100.2, 120.0)
        self.assertIn("son tempo est gardé (100.2 battements par minute, trop loin de 120 pour le recaler)", garde)
        self.assertIn("toutes les 0.599 s, pas sur la grille de la vidéo", garde)
        self.assertIn("ses temps tombent toutes les 0.500 s.", sm.message_sans_entree("m.wav", {"facteur": 1.0}, 120.0, 0))

    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg absent")
    def test_morceau_sans_entree_franche(self):
        """« Mets ma musique » avec un morceau dont la batterie part tout de suite : avant, `musique` répondait
        « donne --a » alors que --a était donné. Le premier temps fort tombe au début de la vidéo."""
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            morceau, sortie = Path(d) / "m.wav", Path(d) / "c.wav"
            kick = "if(gte(t,0.25)*lt(mod(t-0.25,60/124),0.08),sin(2*PI*55*t)*exp(-30*mod(t-0.25,60/124)),0)"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"aevalsrc='{kick}':d=30:s=44100",
                            "-f", "lavfi", "-i", "sine=f=330:d=30", "-filter_complex",
                            "[1]volume=0.05[b];[0][b]amix=inputs=2:normalize=0", "-ar", "44100", str(morceau)], check=True)
            ffmpeg = shutil.which("ffmpeg")
            fps = sm.MUSIQUE_SR / sm.MUSIQUE_PAS
            self.assertIsNone(sm.entree_de(sm.enveloppe(ffmpeg, morceau), fps))
            sortie_texte = io.StringIO()
            with contextlib.redirect_stdout(sortie_texte):
                sm.main(["musique", str(morceau), "--sortie", str(sortie), "--a", "8", "--duree", "15"])
            self.assertIn("pas d'entrée franche (la batterie part dès le début)", sortie_texte.getvalue())
            graves = sm.enveloppe(ffmpeg, sortie, graves=True)
            premiere = next(i for i, v in enumerate(graves) if v > max(graves) * 0.3) / fps
            self.assertLess(premiere, 0.03)                                  # le premier temps à 0 s
            self.assertAlmostEqual(len(graves) / fps, 15.6, delta=0.1)       # coupé à la durée de la vidéo

    def test_filtres_calage(self):
        plus_tard = sm.filtres_calage({"facteur": 0.98, "decalage": -1.5}, 20)
        self.assertEqual(plus_tard, "atempo=0.980000,adelay=1500|1500,asetpts=N/SR/TB,atrim=duration=20.60")
        coupe = sm.filtres_calage({"facteur": 1.0, "decalage": 2.25})
        self.assertEqual(coupe, "atrim=start=2.250,asetpts=PTS-STARTPTS")

    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg absent")
    def test_calage_reel_demarre_plus_tard(self):
        """Avec ffmpeg 8.1, adelay suivi d'atrim perdait le silence ajouté : l'entrée tombait 2 s trop tôt."""
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            morceau, sortie = Path(d) / "m.wav", Path(d) / "c.wav"
            kick = "if(gte(t,6)*lt(mod(t-6,60/124),0.08),sin(2*PI*55*t)*exp(-30*mod(t-6,60/124)),0)"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "sine=f=220:d=30", "-f", "lavfi",
                            "-i", f"aevalsrc='{kick}':d=30:s=44100", "-filter_complex",
                            "[0]volume='if(lt(t,6),0.03,0.15)':eval=frame[a];[a][1]amix=inputs=2:normalize=0",
                            "-ar", "44100", str(morceau)], check=True)
            sm.main(["musique", str(morceau), "--sortie", str(sortie), "--a", "8", "--duree", "15"])
            ffmpeg = shutil.which("ffmpeg")
            fps = sm.MUSIQUE_SR / sm.MUSIQUE_PAS
            graves = sm.enveloppe(ffmpeg, sortie, graves=True)
            premiere = next(i for i, v in enumerate(graves) if v > max(graves) * 0.3) / fps
            self.assertAlmostEqual(premiere, 8.0, delta=0.15)          # la batterie arrive à 8 s
            self.assertGreater(sm.silence_initial(sm.enveloppe(ffmpeg, sortie), fps), 1.0)


class Emergence(unittest.TestCase):
    def test_bruitage_au_dessus_du_fond(self):
        musique = [-25.0] * 400                        # 20 s de musique à -25 dB (50 ms par case)
        mix = list(musique)
        mix[100] = -18.0                               # un clic à 5 s : +7 dB
        mix[200] = -23.5                               # un clic à 10 s : +1,5 dB, couvert
        res = sm.verdict_emergence(mix, musique, [{"src": "a/clic.mp3", "debut": 5.0, "duree": 0.1},
                                                  {"src": "a/doux.mp3", "debut": 10.0, "duree": 0.1}])
        self.assertEqual([(r[1], r[2]) for r in res], [("clic", 7.0), ("doux", 1.5)])

    def test_fond_local_d_une_intro_calme(self):
        musique = [-33.0] * 100 + [-25.0] * 300        # intro 8 dB plus calme
        mix = list(musique)
        mix[40] = -27.0                                 # pendant l'intro : +6 dB sur le fond local
        res = sm.verdict_emergence(mix, musique, [{"src": "clic.mp3", "debut": 2.0, "duree": 0.1}])
        self.assertEqual(res[0][2], 6.0)

    def test_lecture_du_bloc_sons(self):
        with tempfile.TemporaryDirectory() as d:
            index = Path(d) / "index.html"
            index.write_text(
                '<audio id="musique" src="assets/audio/m.wav" data-start="0" data-duration="67.0" data-media-start="0" '
                'data-volume="0.1413" data-audio-group="mixage" data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:'
                '[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0},{&quot;t&quot;:0.4,&quot;v&quot;:0.1413}]}]}"></audio>\n'
                '<audio id="sfx-01" src="assets/sons/clic.mp3" data-start="1.000" data-duration="0.186" data-media-start="0.000" '
                'data-volume="1.7783" data-audio-group="mixage"></audio>', encoding="utf-8")
            musique, sons = sm.sons_poses(index)
            self.assertAlmostEqual(musique["vol"], 0.1413)
            self.assertEqual(len(sons), 1)
            self.assertEqual((sons[0]["debut"], sons[0]["vol"]), (1.0, 1.7783))


class Svg(unittest.TestCase):
    def test_logo_monochrome_recolorable(self):
        brut = ('<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" width="256" height="260" viewBox="0 0 256 260">'
                '<title>OpenAI</title><path fill="#fff" d="M1 1h10v10z"/></svg>')
        propre = sm.nettoyer_svg(brut)
        self.assertTrue(propre.startswith('<svg width="100%" height="100%"'))
        self.assertIn('fill="currentColor"', propre)
        self.assertNotIn("<title>", propre)
        self.assertNotIn('width="256"', propre)

    def test_identifiants_et_styles_isoles(self):
        insta = ('<svg viewBox="0 0 1 1"><defs><radialGradient id="a"/></defs>'
                 '<use href="#a"/><path fill="url(#a)" d="M0 0h1z"/></svg>')
        propre = sm.nettoyer_svg(insta, prefixe="logo-instagram")
        self.assertIn('id="logo-instagram-a"', propre)
        self.assertIn('href="#logo-instagram-a"', propre)
        self.assertIn('fill="url(#logo-instagram-a)"', propre)
        self.assertNotIn('id="a"', propre)
        tiktok = '<svg viewBox="0 0 1 1"><style>.cls-2{fill:#fe2c55}.cls-3, path{fill:#25f4ee}</style><path class="cls-2"/></svg>'
        propre = sm.nettoyer_svg(tiktok, prefixe="logo-tiktok")
        self.assertIn('<svg class="logo-tiktok"', propre)
        self.assertIn(".logo-tiktok .cls-2 {", propre)
        self.assertIn(".logo-tiktok .cls-3, .logo-tiktok path {", propre)

    def test_logo_deux_tons_garde_ses_tons(self):
        notion = '<svg viewBox="0 0 10 10"><path fill="#FFF" d="M0 0h9v9z"/><path d="M2 2h5v5z"/></svg>'
        self.assertNotIn("currentColor", sm.nettoyer_svg(notion))

    def test_logo_noir_par_defaut_ou_presque_noir(self):
        self.assertIn('<svg fill="currentColor"', sm.nettoyer_svg('<svg viewBox="0 0 1 1"><path d="M0 0h1z"/></svg>'))
        github = '<svg viewBox="0 0 1 1"><path fill="#181717" d="M0 0h1z"/><path fill="none" d="M0 0"/></svg>'
        self.assertIn('fill="currentColor"', sm.nettoyer_svg(github))

    def test_logo_en_couleur_garde_sa_couleur(self):
        propre = sm.nettoyer_svg('<svg viewBox="0 0 24 24"><path fill="#D97757" d="M0 0h1z"/></svg>')
        self.assertIn('fill="#D97757"', propre)

    def test_svg_actif_refuse(self):
        for piege in ('<svg><script>alert(1)</script></svg>', '<svg onload="x()"></svg>',
                      '<svg><image href="https://exemple.com/a.png"/></svg>', '<svg><foreignObject/></svg>'):
            with self.assertRaises(ValueError):
                sm.nettoyer_svg(piege)

    def test_ajouts_fusionnes(self):
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d)
            sm.ecrire_ajouts(projet, {"logo-claude": "<svg/>"})
            f = sm.ecrire_ajouts(projet, {"rocket": "<svg></svg>"})
            texte = f.read_text(encoding="utf-8")
            self.assertIn('"logo-claude"', texte)
            self.assertIn('"rocket"', texte)


class Kit(unittest.TestCase):
    def test_kit_livre(self):
        kit = RACINE / "templates" / "kit"
        for f in ("kit.css", "kit.js", "icones.js", "ajouts.js"):
            self.assertTrue((kit / f).is_file(), f)
        js = (kit / "kit.js").read_text(encoding="utf-8")
        for fonction in ("K.champ", "K.curseur", "K.trajet", "K.clic", "K.taper", "K.compteur", "K.flash", "K.chapitre", "K.cacher", "K.tuileMarque", "K.logoNu"):
            self.assertIn(fonction + " = function", js)
        self.assertNotIn("Math.random", js)
        self.assertNotIn("o.flouPres || 70", js)   # un flou demandé à 0 doit valoir 0
        gabarit = (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8")
        for f in ("kit/kit.css", "kit/icones.js", "kit/ajouts.js", "kit/kit.js", "assets/fonts/interfaces.css"):
            self.assertIn(f, gabarit)
        # Chaque scène isolée, avant ET après montage (HyperFrames remplace data-composition-src par
        # data-composition-file) : sinon ses z-index passent devant une vraie vidéo de la racine.
        regle = next(l for l in gabarit.splitlines() if 'div:is([data-composition-src]' in l)
        self.assertIn("[data-composition-file]", regle)
        self.assertIn("isolation: isolate", regle)
        for css in kit.glob("*.css"):   # le rendu refuse une feuille qui remonte d'un dossier
            self.assertNotIn("../", css.read_text(encoding="utf-8"), css.name)


class AuClient(unittest.TestCase):
    def test_jamais_versionne(self):
        """Ce qui appartient au client (INSTALL.md, « Mettre à jour ») n'entre jamais dans le dépôt : une mise
        à jour par git ne peut donc pas l'écraser."""
        import subprocess
        chemins = [".claude/settings.local.json", ".venv-voix/bin/python", ".telechargeur-venv/bin/yt-dlp",
                   "marque.json", "studio.config.json", "videos/Offre · 2026-10-30/OFFRE.json", "assets/musiques/LICENCE.md"]
        r = subprocess.run(["git", "-c", "core.quotepath=off", "check-ignore", "--no-index", *chemins], cwd=RACINE,
                           capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 128:
            self.skipTest("pas un dépôt git")
        self.assertEqual(sorted(r.stdout.splitlines()), sorted(chemins))


class Planche(unittest.TestCase):
    def test_un_par_seconde_et_derniere_image(self):
        t = sm.instants_planche(3.0, None)
        self.assertEqual(t[0], 0.3)
        self.assertEqual(t[-1], 2.93)

    def test_longue_video_espacee(self):
        t = sm.instants_planche(90.0, None)
        self.assertLessEqual(len(t), 32)

    def test_reperes_bornes(self):
        self.assertEqual(sm.instants_planche(2.0, [-1, 0.5, 9]), [0.0, 0.5, 1.93])


class Son(unittest.TestCase):
    def test_dans_la_cible(self):
        self.assertEqual(sm.verdict_sonore({"input_i": "-16.3", "input_tp": "-1.8"}), [])

    def test_trop_faible_et_sature(self):
        self.assertEqual(len(sm.verdict_sonore({"input_i": "-20", "input_tp": "-0.2"})), 2)

    def test_muet(self):
        self.assertIn("muette", sm.verdict_sonore({"input_i": "-inf", "input_tp": "-inf"})[0])

    def test_cible_reglable(self):
        self.assertEqual(sm.verdict_sonore({"input_i": "-20.2", "input_tp": "-3"}, -20), [])
        self.assertEqual(len(sm.verdict_sonore({"input_i": "-20.2", "input_tp": "-3"})), 1)

    def test_chaine_mastering(self):
        self.assertIn("volume=12.50dB", sm.chaine_mastering(12.5))

    def test_plafond_descend_apres_un_debord(self):
        # L'AAC a sorti +0,82 dBTP avec un plafond à -3,39 dBFS : le plafond suivant descend de 2,22 dB
        plafond = sm.plafond_suivant(10 ** (-3.39 / 20), 0.82)
        self.assertAlmostEqual(20 * math.log10(plafond), -3.39 - 2.22, places=2)

    def test_plafond_remonte_avec_de_la_marge(self):
        # Le cas du 28/10/2026 : plafond trop bas après des débords passagers, mixage écrasé à -7,1 dBTP
        # (5,7 dB de marge : il remonte de la moitié, pour ne pas osciller)
        self.assertAlmostEqual(20 * math.log10(sm.plafond_suivant(0.2, -7.1)), 20 * math.log10(0.2) + 2.85, places=2)

    def test_plafond_borne(self):
        self.assertEqual(sm.plafond_suivant(0.7, 30.0), 0.1)
        self.assertEqual(sm.plafond_suivant(0.7, -40.0), 0.8)

    def test_meilleur_essai(self):
        # Le cas du 28/10/2026 : un essai juste, puis un essai qui déborde, puis un mixage écrasé
        bon = {"input_i": "-16.4", "input_tp": "-2.3"}
        deborde = {"input_i": "-16.1", "input_tp": "0.8"}
        ecrase = {"input_i": "-20.5", "input_tp": "-7.1"}
        self.assertEqual(min([deborde, ecrase, bon], key=sm.rang_mastering), bon)
        self.assertLess(sm.rang_mastering(ecrase), sm.rang_mastering(deborde))


class PrisesOubliees(unittest.TestCase):
    SFX = Path(tempfile.gettempdir()) / "studio" / "assets" / "sfx"
    CATALOGUE = [{"id": "paper-marker-stroke", "file": "pack/paper/paper-marker-stroke.mp3", "duration": 11.625,
                  "segments": [[0.0, 0.37], [0.61, 0.94], [1.13, 2.34], [2.5, 2.9]]},
                 {"id": "click-mouse-click", "file": "pack/clicks/click-mouse-click.mp3", "duration": 0.15, "segments": None}]

    def test_son_a_prises_sans_trim(self):
        fautifs = sm.prises_oubliees([{"src": self.SFX / "pack/paper/paper-marker-stroke.mp3", "start": 1.3}],
                                     self.CATALOGUE, self.SFX)
        self.assertEqual(len(fautifs), 1)
        for attendu in ("paper-marker-stroke", "1.30 s", "4 prises", "[0.0, 0.37]", "catalog.json"):
            self.assertIn(attendu, fautifs[0])

    def test_prise_choisie_son_simple_ou_hors_pack(self):
        evenements = [{"src": self.SFX / "pack/paper/paper-marker-stroke.mp3", "start": 1.3, "trim": (0.0, 0.37)},
                      {"src": self.SFX / "pack/clicks/click-mouse-click.mp3", "start": 2.0},
                      {"src": Path(tempfile.gettempdir()) / "projet" / "assets" / "sons" / "mon-son.mp3", "start": 3.0}]
        self.assertEqual(sm.prises_oubliees(evenements, self.CATALOGUE, self.SFX), [])

    def test_sans_pack_installe(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(sm.catalogue_sfx(Path(d)), [])


class SonsQuiLassent(unittest.TestCase):
    """Retour du client du 07/11/2026 : le même bruitage revenait sans cesse, et c'était un cliquet."""
    SFX = Path(tempfile.gettempdir()) / "studio" / "assets" / "sfx"
    CATALOGUE = [{"id": i, "file": f"pack/{i}.mp3"} for i in
                 ("click-short-snap", "click-single-snap", "click-hard", "ui-pop-up", "starter-pop", "click-click-sequence")]

    def ev(self, ident, t, trim=None):
        e = {"src": self.SFX / f"pack/{ident}.mp3", "start": t}
        if trim:
            e["trim"] = trim
        return e

    def test_la_story_v3_est_signalee(self):
        # 15,85 et 15,97 (deux fois de suite), puis 18,55 et 21,20 : 4 fois en 6 s, et un cliquet à chaque fois
        evenements = [self.ev("click-short-snap", t) for t in (15.85, 15.97, 18.55, 21.2)]
        avis = sm.sons_qui_lassent(evenements, self.CATALOGUE, self.SFX)
        self.assertTrue(any("deux fois de suite (15.85 et 15.97 s)" in a for a in avis))
        self.assertTrue(any("4 fois en 6 s" in a for a in avis))
        self.assertEqual(sum("cliquet de molette" in a for a in avis), 4)

    def test_une_serie_qui_alterne_passe(self):
        evenements = [self.ev("ui-pop-up", 20.57), self.ev("starter-pop", 20.67), self.ev("ui-pop-up", 22.0),
                      self.ev("click-single-snap", 23.0), self.ev("ui-pop-up", 30.0)]
        self.assertEqual(sm.sons_qui_lassent(evenements, self.CATALOGUE, self.SFX), [])

    def test_trois_fois_en_six_secondes(self):
        evenements = [self.ev("ui-pop-up", 1.0), self.ev("starter-pop", 2.0), self.ev("ui-pop-up", 4.0),
                      self.ev("starter-pop", 5.0), self.ev("ui-pop-up", 6.5)]
        avis = sm.sons_qui_lassent(evenements, self.CATALOGUE, self.SFX)
        self.assertEqual(avis, ["ui-pop-up 3 fois en 6 s (1.00, 4.00, 6.50 s) : varie-le"])

    def test_piege_rogne_ou_sans_fin_sure(self):
        sur = [self.ev("click-short-snap", 1.0, trim=[0.0, 0.25]), self.ev("click-hard", 5.0, trim=[0.0, 0.2])]
        self.assertEqual(sm.sons_qui_lassent(sur, self.CATALOGUE, self.SFX), [])
        avis = sm.sons_qui_lassent([self.ev("click-hard", 1.0, trim=[0.0, 0.4]), self.ev("click-click-sequence", 9.0)],
                                   self.CATALOGUE, self.SFX)
        self.assertIn('rogne-le avec "trim": [0, 0.2]', avis[0])
        self.assertIn("prends un autre son", avis[1])


class Export(unittest.TestCase):
    def info(self, largeur=1080, hauteur=1920, duree="20.0", audio=True, **video):
        v = {"codec_type": "video", "codec_name": "h264", "width": largeur, "height": hauteur,
             "pix_fmt": "yuv420p", "r_frame_rate": "30/1"}
        v.update(video)
        flux = [v] + ([{"codec_type": "audio", "codec_name": "aac"}] if audio else [])
        return {"streams": flux, "format": {"duration": duree}}

    def test_conforme(self):
        self.assertEqual(sm.verdict_export(self.info(), "reel"), ([], []))

    def test_page_paysage(self):
        pb, avis = sm.verdict_export(self.info(1920, 1080, "90"), "page")
        self.assertEqual((pb, avis), ([], []))

    def test_mauvais_format(self):
        pb, _ = sm.verdict_export(self.info(), "page")
        self.assertTrue(any("taille" in p for p in pb))

    def test_format_force(self):
        self.assertEqual(sm.verdict_export(self.info(1080, 1080, "60"), "page", "1x1")[0], [])

    def test_ecarts(self):
        pb, _ = sm.verdict_export(self.info(1920, 1080, pix_fmt="yuv444p"), "reel")
        self.assertEqual(len(pb), 2)

    def test_duree(self):
        pb, _ = sm.verdict_export(self.info(duree="75"), "story")
        self.assertTrue(any("durée" in p for p in pb))
        pb, avis = sm.verdict_export(self.info(duree="40"), "story")
        self.assertEqual((pb, [a for a in avis if "visées" in a]), ([], []))  # une story a le temps d'un vrai script
        pb, avis = sm.verdict_export(self.info(duree="60"), "reel")
        self.assertEqual(pb, [])
        self.assertTrue(any("visées" in a for a in avis))

    def test_boucle_sans_son(self):
        _, avis = sm.verdict_export(self.info(1920, 1080, "20"), "section")
        self.assertTrue(any("piste son" in a for a in avis))
        self.assertEqual(sm.verdict_export(self.info(1920, 1080, "20", audio=False), "section"), ([], []))

    def test_page_trop_lourde(self):
        _, avis = sm.verdict_export(self.info(1920, 1080, "90"), "page", poids=40 * 1024 * 1024)
        self.assertTrue(any("Mo" in a for a in avis))

    def test_format_de(self):
        self.assertEqual(sm.format_de(self.info(1080, 1350)), "4x5")
        self.assertIsNone(sm.format_de(self.info(720, 1280)))

    def test_debut_rapide(self):
        with tempfile.TemporaryDirectory() as d:
            rapide, lent = Path(d) / "a.mp4", Path(d) / "b.mp4"
            rapide.write_bytes(b"....ftyp....moov....mdat....")
            lent.write_bytes(b"....ftyp....mdat....moov....")
            self.assertTrue(sm.debut_rapide(rapide))
            self.assertFalse(sm.debut_rapide(lent))


class SansMusique(unittest.TestCase):
    def test_retire_seulement_la_musique(self):
        html = ('<audio id="musique" src="assets/sons/musique-m.mp3" data-start="0" data-track-index="19"></audio>\n'
                '<audio id="sfx-01" src="assets/sons/pop.mp3" data-start="1.2"></audio>\n'
                '<audio id="voix" src="assets/audio/voix.wav" data-start="0"></audio>')
        sortie, n = sm.sans_musique_html(html)
        self.assertEqual(n, 1)
        self.assertIn("sfx-01", sortie)
        self.assertIn('id="voix"', sortie)
        self.assertNotIn('id="musique"', sortie)

    def test_marque_a_la_main(self):
        sortie, n = sm.sans_musique_html('<audio data-role="musique" src="m.mp3"></audio>')
        self.assertEqual((n, sortie), (1, ""))


class Voix(unittest.TestCase):
    def test_transcription_toujours_par_parakeet_avec_la_langue(self):
        """`hyperframes transcribe` seul prend un modèle anglais : sur une voix française il invente un texte
        anglais, sous Windows il n'a pas de moteur, sur Mac il installe whisper-cpp sans demander."""
        docs = [p for p in (RACINE / ".claude" / "skills" / "studio").rglob("*.md") if "styles" not in p.parts]
        docs += [RACINE / "templates" / "AGENT.md.tpl", RACINE / "INSTALL.md"]
        commandes = []
        for doc in docs:
            texte = " ".join(doc.read_text(encoding="utf-8").split())
            for i in [m.start() for m in re.finditer(r"hyperframes transcribe ", texte)]:
                commandes.append((doc.name, texte[i:texte.index("`", i)].strip()))
        self.assertGreaterEqual(len(commandes), 2)
        for doc, commande in commandes:
            self.assertIn("--engine parakeet --language ", commande, f"{doc} : {commande}")
        voix = (RACINE / ".claude" / "skills" / "studio" / "references" / "voix.md").read_text(encoding="utf-8")
        self.assertIn("npx hyperframes models install parakeet", voix)
        self.assertIn("675 Mo", voix)
        self.assertIn("areverse", voix)
        self.assertIn("loudnorm=I=-24:TP=-3", voix)
        self.assertIn("-ar 48000", voix)


class LancerHyperframes(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node") and (RACINE / "node_modules" / "hyperframes" / "bin" / "hyperframes.mjs").is_file(),
                         "npm ci pas lancé")
    def test_par_node_jamais_par_cmd(self):
        """Revue du 03/11/2026 : sous Windows, `hyperframes.cmd` passe par cmd.exe, qui coupe une adresse
        au premier « & » (un lien copié d'Instagram) : la capture de sa page échouait."""
        cli = sm.hyperframes_cli()
        self.assertEqual(Path(cli[-1]).name, "hyperframes.mjs")
        self.assertEqual(Path(cli[0]).stem.lower(), "node")


class Consignes(unittest.TestCase):
    SKILL = RACINE / ".claude" / "skills" / "studio"

    def test_le_skill_ne_cite_que_des_styles_du_catalogue(self):
        catalogue = (self.SKILL / "styles" / "README.md").read_text(encoding="utf-8")
        noms = set(re.findall(r"^\| \d+ \| ([^|]+?) \|", catalogue, re.M))
        self.assertEqual(len(noms), 9)                  # le style maison (0) et les 8 styles
        self.assertIn("Sur mesure", noms)
        skill = " ".join((self.SKILL / "SKILL.md").read_text(encoding="utf-8").split())
        cites = re.findall(r"« dans le style ([^»]+?) »", skill)
        self.assertTrue(cites)
        self.assertLessEqual(set(cites), noms)

    def test_la_voix_proposee_en_premier_est_celle_de_google(self):
        skill = " ".join((self.SKILL / "SKILL.md").read_text(encoding="utf-8").split())
        self.assertNotIn("voix de synthèse HeyGen", skill)
        self.assertIn("voix IA gratuite de Google AI Studio", skill)

    def test_l_etude_motion_a_la_taille_de_la_page_de_vente(self):
        for doc in (self.SKILL / "references" / "ecriture.md", RACINE / "CREDITS.md"):
            texte = doc.read_text(encoding="utf-8")
            self.assertIn("578 750 publicités", texte, doc.name)
            self.assertNotIn("550 000", texte, doc.name)


def jpeg(largeur: int, hauteur: int) -> bytes:
    """Les premiers octets d'un vrai JPEG (JFIF puis SOF0) : assez pour sa signature et sa taille."""
    app0 = b"\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
    sof0 = (b"\xff\xc0\x00\x11\x08" + hauteur.to_bytes(2, "big") + largeur.to_bytes(2, "big")
            + b"\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01")
    return b"\xff\xd8" + app0 + sof0 + b"\xff\xd9"


def png(largeur: int, hauteur: int) -> bytes:
    return (b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + largeur.to_bytes(4, "big") + hauteur.to_bytes(4, "big")
            + b"\x08\x02\x00\x00\x00" + b"\x00" * 4)


# Ce que deux essais ont livré comme couverture.jpg : de la vidéo H.264 (journaux du 30/10/2026).
H264 = b"\x00\x00\x00\x01\x67\x64\x00\x32\xac\xd9\x40\x44\x02\x27\xe5\x84" + b"\x00" * 64


def racine_de_test(base: Path) -> Path:
    """Un dossier du produit, réduit à ce que la création d'une vidéo lit : produit.json, les
    gabarits et le kit du dépôt, un style de marque."""
    racine = base / "studio"
    (racine / "templates").mkdir(parents=True)
    for sous in ("projet", "kit", "accueil"):
        shutil.copytree(RACINE / "templates" / sous, racine / "templates" / sous)
    shutil.copy2(RACINE / "produit.json", racine / "produit.json")
    (racine / "brand").mkdir()
    (racine / "brand" / "tokens.css").write_text(":root{}", encoding="utf-8")
    (racine / "hyperframes.json").write_text("{}", encoding="utf-8")
    return racine


class NomsDeDossiers(unittest.TestCase):
    def test_sans_dollar_ni_accent_grave(self):
        """Les noms se tapent entre guillemets dans les commandes : `$` et l'accent grave y sont actifs."""
        self.assertEqual(sm.propre("Gagne 1000$ par mois"), "Gagne 1000 par mois")
        self.assertEqual(sm.propre("L`atelier d'$HOME"), "L'atelier d'HOME")
        self.assertEqual(sm.propre("Promo : 50 % / été"), "Promo - 50 % - été")

    def test_coupe_sur_une_limite_de_mot(self):
        self.assertEqual(sm.propre("Nouvelle fonctionnalité de sous-titres automatiques", 30), "Nouvelle fonctionnalité de")
        self.assertEqual(sm.propre("Promo #1 -50% & L'Été d'Émilie, la formation crochet", 30),
                         "Promo #1 -50% & L'Été d'Émilie")
        self.assertEqual(sm.propre("Anticonstitutionnellement", 10), "Anticonsti")      # un seul mot : coupé net
        self.assertEqual(sm.propre("Offre", 30), "Offre")

    def test_chemin_windows_sous_200_caracteres(self):
        """Le sujet était répété en entier dans le dossier et dans le projet : avec un nom d'utilisateur
        Windows ordinaire, le chemin d'un son posé atteignait 226 caractères (240 pour une story)."""
        self.assertEqual(sm.NOMS_MAX, 73)
        specs = ["reel", "story:dernier-jour", "story:ouverture", "page", "page@1x1", "section", "linkedin", "pub@4x5",
                 "tiktok", "youtube"]
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            sujet = "Promo #1 -50% & L'Été d'Émilie, la formation crochet complète en 30 jours"
            premier = sm.creer(maison, sujet, "lancement", [sm.lire_video(s) for s in specs], "2026-10-30")
            deuxieme = sm.creer(maison, sujet, "lancement", [sm.lire_video(s) for s in specs], "2026-10-30")
            self.assertEqual(deuxieme.name, "Promo #1 -50% & L'Été d'Émilie · 2026-10-30 (2)")
            noms = {meta["video"]: p.name for p, meta in sm.projets(premier)}
            self.assertEqual(noms["reel"], "Promo #1 -50% & L'Été · Reel")
            self.assertEqual(noms["story-dernier-jour"], "Promo #1 · Story dernier jour")
            self.assertEqual({meta["video"]: p.name for p, meta in sm.projets(deuxieme)}["reel"], "Promo #1 -50% · Reel")
            sm.ajouter(maison, deuxieme, [sm.lire_video("x")])
            for dossier in (premier, deuxieme):
                for projet, meta in sm.projets(dossier):
                    self.assertTrue(projet.name.endswith(sm.nom_video(meta)), projet.name)
                    fichiers = [p.relative_to(projet).as_posix() for p in projet.rglob("*") if p.is_file()]
                    self.assertLessEqual(max(map(len, fichiers)), len(sm.FICHIER_LE_PLUS_PROFOND))
                    chemin = f"{sm.EXEMPLE_WINDOWS}{dossier.name}\\{projet.name}\\{sm.FICHIER_LE_PLUS_PROFOND}"
                    self.assertLess(len(chemin), 200, chemin)


class Creation(unittest.TestCase):
    def test_serie_multi_formats(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            videos = [sm.lire_video(s) for s in ("reel", "page", "page@1x1", "story:ouverture")]
            dossier = sm.creer(maison, "Ma formation", "vente", videos, "2026-10-12")
            self.assertEqual(dossier.parent.name, "videos")
            self.assertEqual(dossier.name, "Ma formation · 2026-10-12")
            liste = {meta["video"]: (p, meta) for p, meta in sm.projets(dossier)}
            self.assertEqual(sorted(liste), ["page", "page-1x1", "reel", "story-ouverture"])
            page, meta = liste["page"]
            self.assertEqual((meta["lieu"], meta["format"], meta["objectif"]), ("video", "16x9", "vente"))
            html = (page / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-width="1920" data-height="1080"', html)
            self.assertTrue((page / "kit" / "kit.js").is_file())
            self.assertTrue((page / "kit" / "icones.js").is_file())
            self.assertNotIn("{{", html)
            carre = (liste["page-1x1"][0] / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-width="1080" data-height="1080"', carre)
            self.assertNotIn("{{", (page / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertTrue((page / "brand" / "tokens.css").is_file())
            self.assertEqual(json.loads((page / "package.json").read_text(encoding="utf-8"))["scripts"]["render"],
                             "hyperframes render -o exports/page.mp4")
            fiche = json.loads((dossier / "OFFRE.json").read_text(encoding="utf-8"))
            # le nom de l'offre se lit sur sa page (étape 2), pas dans le sujet de la vidéo (essai du 03/11/2026)
            self.assertEqual((fiche["produit"], fiche["objectif"]), ("", "vente"))
            self.assertIn("produit : le nom de ce qui est présenté manque.", sm.verifier_fiche(fiche))
            deuxieme = sm.creer(maison, "Ma formation", "vente", [sm.lire_video("reel")], "2026-10-12")
            self.assertEqual(deuxieme.name, "Ma formation · 2026-10-12 (2)")

    def test_ajouter_une_declinaison(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("reel")], "2026-10-12")
            reel = sm.projets(dossier)[0][0]
            (reel / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
            (reel / "assets" / "fonts" / "poppins.css").write_text("@font-face{}", encoding="utf-8")
            plan = dossier / "PLAN.md"
            plan.write_text(plan.read_text(encoding="utf-8") + "\n## Livraison\n\n(à venir)\n", encoding="utf-8")
            ajouts = sm.ajouter(maison, dossier, [sm.lire_video("linkedin"), sm.lire_video("story")])
            self.assertEqual([p.name for p in ajouts], ["Offre · LinkedIn", "Offre · Story"])
            metas = {meta["video"]: meta for _p, meta in sm.projets(dossier)}
            self.assertEqual(sorted(metas), ["linkedin", "reel", "story"])
            self.assertEqual((metas["linkedin"]["format"], metas["linkedin"]["objectif"]), ("4x5", "vente"))
            texte = (dossier / "PLAN.md").read_text(encoding="utf-8")
            self.assertIn("## Style et musique", texte)   # une conversation reprise sait si l'étape 4 est faite
            self.assertLess(texte.index("## Script"), texte.index("## Style et musique"))   # le script se valide avant
            self.assertIn("### LinkedIn (4x5", texte)
            self.assertLess(texte.index("### LinkedIn"), texte.index("## Livraison"))
            # les défauts de la revue, relus avant chaque retouche, restent après les vidéos (0.9.0)
            self.assertLess(texte.index("### LinkedIn"), texte.index("## Interdits de cette vidéo"))
            self.assertTrue((ajouts[0] / "assets" / "fonts" / "poppins.css").is_file())
            self.assertTrue(metas["story"]["sticker"])
            self.assertFalse(metas["linkedin"]["sticker"])
            with self.assertRaises(SystemExit):
                sm.ajouter(maison, dossier, [sm.lire_video("reel")])

    def test_police_des_interfaces_dans_le_projet(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            (maison / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
            (maison / "assets" / "fonts" / "Inter-400.woff2").write_bytes(b"x")
            dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("pub")], "2026-10-13")
            projet = sm.projets(dossier)[0][0]
            css = (projet / "assets" / "fonts" / "interfaces.css").read_text(encoding="utf-8")
            self.assertIn('url("Inter-400.woff2")', css)
            self.assertNotIn("Inter-700", css)
            self.assertNotIn("../", css)
            self.assertIn("assets/fonts/interfaces.css", (projet / "index.html").read_text(encoding="utf-8"))

    def test_doublon_refuse(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            with self.assertRaises(SystemExit):
                sm.creer(maison, "X", "vente", [sm.lire_video("reel"), sm.lire_video("reel")], "2026-10-12")

    def test_meta_par_nom_en_livraison(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("reel"), sm.lire_video("page")], "2026-10-12")
            for nom, support in (("reel.mp4", "reel"), ("page.mp4", "page"), ("reel-sans-musique.mp4", "reel")):
                video = dossier / "livraison" / nom
                video.write_bytes(b"x")
                self.assertIsNone(sm.meta_de(video))
                self.assertEqual(sm.meta_par_nom(video)["support"], support)
            inconnue = dossier / "livraison" / "autre.mp4"
            inconnue.write_bytes(b"x")
            self.assertIsNone(sm.meta_par_nom(inconnue))

    def test_gabarit_sans_tween_vide(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("reel")], "2026-10-12")
            html = (sm.projets(dossier)[0][0] / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("tl.to({}", html)
            self.assertIn("Reel · à composer", html)

    def test_meta_retrouvee_depuis_un_export(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "fonctionnalite", [sm.lire_video("section")], "2026-10-12")
            projet = sm.projets(dossier)[0][0]
            video = projet / "exports" / "section.mp4"
            video.write_bytes(b"x")
            self.assertEqual(sm.meta_de(video)["support"], "section")
            self.assertIsNone(sm.meta_de(maison))

    def test_livraison(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            videos = [sm.lire_video(s) for s in ("reel", "page", "story:teaser")]
            dossier = sm.creer(maison, "Offre", "lancement", videos, "2026-10-12")
            manques = sm.manques_livraison(dossier)
            for attendu in ("reel.mp4", "page.mp4", "story-teaser.mp4", "page.jpg (l'affiche, montrée avant la lecture)",
                            "legende-reel.txt (le texte de publication)", "stories.txt (le texte de publication)"):
                self.assertIn(attendu, manques)
            self.assertTrue(any("Quand publier" in m for m in manques))
            self.assertIn("couverture.jpg (la couverture du Reel)", manques)
            self.assertIn("integration.md (comment poser la vidéo sur la page)", manques)
            for f in ("reel.mp4", "page.mp4", "story-teaser.mp4", "legende-reel.txt", "integration.md", "stories.txt"):
                (dossier / "livraison" / f).write_bytes(b"x")
            (dossier / "livraison" / "page.jpg").write_bytes(jpeg(1920, 1080))
            (dossier / "livraison" / "couverture.jpg").write_bytes(jpeg(1080, 1920))
            (dossier / "PLAN.md").write_text("## Quand publier\n", encoding="utf-8")
            self.assertEqual(sm.manques_livraison(dossier), [])
            # « livrer » répondait « ok » sur une couverture.jpg qui était de la vidéo H.264.
            (dossier / "livraison" / "couverture.jpg").write_bytes(H264)
            self.assertEqual(sm.manques_livraison(dossier), [
                "couverture.jpg : pas une image JPEG ou PNG (c'est de la vidéo H.264) ; refais-la avec `couverture`"])
            (dossier / "livraison" / "couverture.jpg").write_bytes(jpeg(1080, 1080))
            self.assertIn("pas au format de la vidéo (1080×1920)", sm.manques_livraison(dossier)[0])
            (dossier / "livraison" / "couverture.jpg").write_bytes(png(540, 960))
            (dossier / "livraison" / "page.jpg").write_bytes(b"x")
            self.assertEqual(sm.manques_livraison(dossier), [
                "page.jpg : pas une image JPEG ou PNG (ce n'est pas une image) ; refais-la avec `affiche`"])

    def test_vente_sans_calendrier(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "fonctionnalite", [sm.lire_video("section")], "2026-10-12")
            (dossier / "livraison" / "section.mp4").write_bytes(b"x")
            (dossier / "livraison" / "section.jpg").write_bytes(jpeg(1920, 1080))
            self.assertEqual(sm.manques_livraison(dossier), ["integration.md (comment poser la vidéo sur la page)"])
            (dossier / "livraison" / "integration.md").write_text("x", encoding="utf-8")
            self.assertEqual(sm.manques_livraison(dossier), [])


class Logos(unittest.TestCase):
    REGISTRE = [{"slug": "openai", "title": "OpenAI", "aliases": []},
                {"slug": "lemon-squeezy", "title": "Lemon Squeezy", "aliases": ["LemonSqueezy"]},
                {"slug": "notion-badge", "title": "Notion", "aliases": []},
                {"slug": "notion", "title": "Notion", "aliases": []},
                {"slug": "metabase", "title": "Metabase", "aliases": []}]

    def test_noms_courants_retrouves(self):
        self.assertEqual(sm.correspondances("ChatGPT", self.REGISTRE)[0]["slug"], "openai")       # alias maison
        self.assertEqual(sm.correspondances("lemon squeezy", self.REGISTRE)[0]["slug"], "lemon-squeezy")
        self.assertEqual(sm.correspondances("Notion", self.REGISTRE)[0]["slug"], "notion")         # le badge après
        self.assertEqual(sm.correspondances("kajabi", self.REGISTRE), [])

    def test_cle_du_kit(self):
        self.assertEqual(sm.cle_logo("Lemon Squeezy"), "lemon-squeezy")
        self.assertEqual(sm.cle_logo("Système.io"), "systeme-io")

    def test_logo_du_client(self):
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d) / "p"
            projet.mkdir()
            png = Path(d) / "mon logo.png"
            png.write_bytes(b"\x89PNG")
            self.assertEqual(sm.logo_fichier(projet, png), '<img src="assets/logos/mon logo.png" alt="">')
            self.assertTrue((projet / "assets" / "logos" / "mon logo.png").is_file())
            svg = Path(d) / "l.svg"
            svg.write_text('<svg viewBox="0 0 10 10"><script>x</script></svg>')
            with self.assertRaises(ValueError):
                sm.logo_fichier(projet, svg)


class ImagesReelles(unittest.TestCase):
    def test_signature_et_taille(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "couverture.jpg"
            for contenu, attendu in ((jpeg(1080, 1920), ("jpeg", 1080, 1920)), (png(1920, 1080), ("png", 1920, 1080)),
                                     (H264, None), (b"x", None), (b"\xff\xd8\xff\xda" + b"\x00" * 20, None)):
                f.write_bytes(contenu)
                self.assertEqual(sm.image_reelle(f), attendu)
            f.write_bytes(H264)
            self.assertEqual(sm.nature_fichier(f), "c'est de la vidéo H.264")
            f.write_bytes(jpeg(1080, 1920))
            self.assertIsNone(sm.probleme_image(f, (1080, 1920)))
            self.assertIn("pas au format", sm.probleme_image(f, (1920, 1080)))
            f.write_bytes(jpeg(360, 640))
            self.assertIn("trop petite", sm.probleme_image(f, (1080, 1920)))


class ArgumentsDeCouverture(unittest.TestCase):
    """Les arguments se reconnaissent à leur nature, dans n'importe quel ordre (4 essais sur 9 s'étaient
    trompés d'ordre le 30/10/2026)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.d = Path(self._tmp.name)
        self.projet = self.d / "Offre · Reel"
        (self.projet / "exports").mkdir(parents=True)
        (self.projet / "work").mkdir()
        (self.d / "livraison").mkdir()
        self.video = self.projet / "exports" / "reel-master.mp4"
        self.video.write_bytes(b"\x00\x00\x00\x18ftypmp42")
        self.image = self.projet / "work" / "couv.png"
        self.image.write_bytes(png(800, 800))

    def tearDown(self):
        self._tmp.cleanup()

    def lire(self, *args) -> dict:
        return sm.lire_couverture([str(a) for a in args])

    def test_tous_les_ordres(self):
        jpg, mp4 = self.d / "livraison" / "couverture.jpg", self.d / "livraison" / "reel.mp4"
        attendu = {"video": self.video, "instant": None, "image": self.image, "sortie": mp4, "sortie_image": jpg}
        for args in ((self.video, self.image, jpg, mp4), (mp4, jpg, self.image, self.video), (jpg, self.video, mp4, self.image)):
            self.assertEqual(self.lire(*args), attendu, args)
        # Le cas des journaux : la vidéo, l'image, puis couverture.jpg pris pour la vidéo de sortie.
        self.assertEqual(self.lire(self.video, self.image, jpg)["sortie_image"], jpg)
        self.assertIsNone(self.lire(self.video, self.image, jpg)["sortie"])

    def test_instant_et_sorties_existantes(self):
        jpg = self.d / "livraison" / "couverture.jpg"
        jpg.write_bytes(H264)                                  # une ancienne couverture ratée : réécrite
        c = self.lire("3,5", self.video, jpg)
        self.assertEqual((c["instant"], c["image"], c["sortie_image"]), (3.5, None, jpg))
        self.assertEqual(self.lire(self.video, "12s")["instant"], 12.0)
        mp4 = self.d / "livraison" / "reel.mp4"
        mp4.write_bytes(b"x")                                  # une livraison déjà faite : la sortie
        self.assertEqual((self.lire(mp4, self.video, "2")["video"], self.lire(mp4, self.video, "2")["sortie"]), (self.video, mp4))

    def test_messages_exacts(self):
        fausse = self.projet / "work" / "fausse.jpg"
        fausse.write_bytes(H264)
        for args, message in (((self.image, "3"), "il manque la vidéo rendue"),
                              ((self.video, fausse), "« " + str(fausse) + " » n'est pas une image JPEG ou PNG (c'est de la vidéo H.264)"),
                              ((self.video, "2", "3"), "deux instants (2, 3)"),
                              ((self.video, "notes.txt"), "« notes.txt » n'est ni une vidéo"),
                              ((self.video,), "il manque la couverture"),
                              ((self.video, self.image, "a.jpg", "b.jpg"), "plusieurs images de sortie")):
            with self.assertRaises(ValueError) as e:
                self.lire(*args)
            self.assertIn(message, str(e.exception), args)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg absent")
class Couverture(unittest.TestCase):
    def setUp(self):
        import subprocess
        self._tmp = tempfile.TemporaryDirectory()
        maison = racine_de_test(Path(self._tmp.name))
        self.dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("reel")], "2026-10-30")
        self.projet = sm.projets(self.dossier)[0][0]
        self.video = self.projet / "exports" / "reel-master.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0x202022:s=1080x1920:r=30:d=2",
                        "-f", "lavfi", "-i", "sine=f=440:d=2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
                        "-shortest", str(self.video)], check=True)
        self.image = self.projet / "work" / "couv.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0xff5b00:s=800x800:d=1",
                        "-frames:v", "1", str(self.image)], check=True)
        self.livraison = self.dossier / "livraison"

    def tearDown(self):
        self._tmp.cleanup()

    def couverture(self, *args: str) -> str:
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            sm.main(["couverture", *[str(a) for a in args]])
        return sortie.getvalue()

    def premiere_image(self, video: Path) -> tuple[int, int, int]:
        import subprocess
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-frames:v", "1", "-vf", "scale=1:1",
                            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
        return tuple(r.stdout[:3])

    def test_l_ordre_des_essais_qui_livrait_de_la_video_dans_le_jpg(self):
        self.couverture(self.video, self.image, self.livraison / "couverture.jpg")
        self.assertEqual(sm.image_reelle(self.livraison / "couverture.jpg"), ("jpeg", 1080, 1920))
        rouge, vert, bleu = self.premiere_image(self.livraison / "reel.mp4")
        self.assertGreater(rouge, 200)                           # la couverture orange en première image
        self.assertLess(bleu, 60)

    def test_quatre_arguments_dans_le_desordre_puis_un_instant(self):
        self.couverture(self.livraison / "reel.mp4", self.image, self.livraison / "couverture.jpg", self.video)
        self.assertEqual(sm.image_reelle(self.livraison / "couverture.jpg"), ("jpeg", 1080, 1920))
        texte = self.couverture(self.video, "1.5")
        self.assertIn("couverture 1080×1920 (image de la vidéo à 1.5 s)", texte)
        self.assertLess(max(self.premiere_image(self.livraison / "reel.mp4")), 60)   # le fond sombre de la vidéo
        (self.livraison / "legende-reel.txt").write_text("x", encoding="utf-8")
        self.assertEqual(sm.manques_livraison(self.dossier), [])

    def test_version_sans_musique(self):
        sans = self.projet / "exports" / "reel-sans-musique-master.mp4"
        shutil.copy2(self.video, sans)
        self.couverture(sans, self.image)
        self.assertTrue((self.livraison / "reel-sans-musique.mp4").is_file())
        self.assertFalse((self.livraison / "reel.mp4").exists())

    def test_instant_hors_de_la_video(self):
        with self.assertRaises(SystemExit) as e:
            self.couverture(self.video, "40")
        self.assertIn("l'instant 40 s dépasse la vidéo (2.0 s)", str(e.exception))
        self.assertFalse((self.livraison / "couverture.jpg").exists())


# Un faux yt-dlp qui se comporte comme le vrai sur ce point : il ne retélécharge jamais un fichier déjà là.
FAUX_YTDLP = """#!{python}
import json, os, shutil, sys
args = sys.argv[1:]
sortie = args[args.index("-o") + 1].replace("%(ext)s", "mp4")
if os.path.exists(sortie):
    print("[download] " + sortie + " has already been downloaded")
    sys.exit(0)
source = json.loads({liens!r}).get(args[-1])
if not source:
    sys.stderr.write("ERROR: [generic] Unable to download webpage: HTTP Error 404")
    sys.exit(1)
shutil.copy(source, sortie)
"""


@unittest.skipUnless(shutil.which("ffmpeg") and os.name != "nt", "ffmpeg et un faux téléchargeur exécutable")
class Reference(unittest.TestCase):
    def setUp(self):
        import subprocess
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        liens = {}
        for nom, duree in (("premiere", 2), ("deuxieme", 4)):
            fichier = self.tmp / f"{nom}.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"testsrc2=s=320x240:r=10:d={duree}",
                            "-pix_fmt", "yuv420p", str(fichier)], check=True)
            for lien in (f"https://exemple.test/{nom}", f"https://www.exemple.test/{nom}"):
                liens[lien] = str(fichier)
        self.dl = self.tmp / "yt-dlp"
        self.dl.write_text(FAUX_YTDLP.format(python=sys.executable, liens=json.dumps(liens)), encoding="utf-8")
        self.dl.chmod(0o755)
        self.dossier = self.tmp / "Offre · 2026-10-30"
        self.dossier.mkdir()
        (self.dossier / "OFFRE.json").write_text("{}", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def reference(self, *args: str) -> None:
        with mock.patch.object(sm, "ytdlp", return_value=str(self.dl)), contextlib.redirect_stdout(io.StringIO()):
            sm.main(["reference", str(self.dossier), *args])

    def analyse(self, nom: str = "reference") -> str:
        return (self.dossier / "sources" / "reference" / nom / "ANALYSE.md").read_text(encoding="utf-8")

    def test_un_deuxieme_lien_analyse_la_deuxieme_video(self):
        self.reference("https://exemple.test/premiere")
        self.assertIn("- Durée : 2 s", self.analyse())
        self.reference("https://exemple.test/deuxieme")
        self.assertIn("Source : https://exemple.test/deuxieme", self.analyse())
        self.assertIn("- Durée : 4 s", self.analyse())
        self.assertEqual([p.name for p in (self.dossier / "sources" / "reference" / "reference").glob("video.*")],
                         ["video.mp4"])

    def test_lien_sans_https(self):
        self.reference("www.exemple.test/premiere", "--nom", "sans-https")
        self.assertIn("Source : https://www.exemple.test/premiere", self.analyse("sans-https"))

    def test_un_echec_ne_laisse_rien(self):
        self.reference("https://exemple.test/premiere")
        avant = sorted(p.name for p in (self.dossier / "sources" / "reference" / "reference").iterdir())
        for args in (("https://exemple.test/absente", "--nom", "echec"), ("https://exemple.test/absente",),
                     ("www.exemple.test/absente", "--nom", "echec"), ("pas-une-video.mp4", "--nom", "echec")):
            with self.assertRaises(SystemExit):
                self.reference(*args)
        self.assertEqual(sorted(p.name for p in (self.dossier / "sources" / "reference").iterdir()), ["reference"])
        self.assertEqual(sorted(p.name for p in (self.dossier / "sources" / "reference" / "reference").iterdir()), avant)
        self.assertIn("- Durée : 2 s", self.analyse())

    def test_fichier_de_l_ordinateur(self):
        self.reference(str(self.tmp / "deuxieme.mp4"), "--nom", "fichier")
        self.assertIn("- Durée : 4 s", self.analyse("fichier"))
        self.assertTrue((self.tmp / "deuxieme.mp4").is_file())       # le fichier du client reste où il est


class Liens(unittest.TestCase):
    def test_lien_complete_comme_capture(self):
        self.assertEqual(sm.lien_video("www.youtube.com/shorts/abc123"), "https://www.youtube.com/shorts/abc123")
        self.assertEqual(sm.lien_video("instagram.com/reel/C9xYz/"), "https://instagram.com/reel/C9xYz/")
        self.assertEqual(sm.lien_video("vm.tiktok.com/ZMabc/"), "https://vm.tiktok.com/ZMabc/")
        self.assertEqual(sm.lien_video(" https://x.com/a/status/1 "), "https://x.com/a/status/1")
        self.assertEqual(sm.lien_video("HTTP://exemple.fr/v"), "HTTP://exemple.fr/v")

    def test_fichier_jamais_pris_pour_un_lien(self):
        self.assertIsNone(sm.lien_video("clip.mov"))
        self.assertIsNone(sm.lien_video("Vidéos/clip.mp4"))
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "www.exemple.fr" / "v"
            f.parent.mkdir()
            f.write_bytes(b"x")
            self.assertIsNone(sm.lien_video(str(f)))



class Relecture(unittest.TestCase):
    """La relecture à froid : le relecteur ne voit que les planches du rendu, jamais le script ni le
    nom du dossier (story refusée du 06/11/2026, que son auteur avait mal relue)."""

    def test_une_image_par_demi_seconde(self):
        self.assertEqual(sm.instants_relecture(3.0, 0.5), [0.25, 0.75, 1.25, 1.75, 2.25, 2.75])
        self.assertEqual(len(sm.instants_relecture(50.0, 0.5)), 100)
        self.assertEqual(sm.instants_relecture(0.2, 0.5), [0.25])

    def test_section_du_plan(self):
        plan = "# Titre\n\n## Script\n\n1. Ta dernière vidéo ?\n2. Trois options.\n\n## Style et musique\n\nx\n"
        self.assertEqual(sm.section_plan(plan, "Script"), "1. Ta dernière vidéo ?\n2. Trois options.")
        self.assertEqual(sm.section_plan(plan, "Vidéos"), "")

    def test_ce_que_la_video_doit_dire(self):
        fiche = copy.deepcopy(sm.FICHE_VIDE)
        fiche.update(produit="Publicitaire IA")
        fiche["promesse"]["texte"] = "Installe un publicitaire dans Claude"
        fiche["prix"]["montant"] = 67
        fiche["cta"]["phrase"] = "Touche le lien"
        lignes = sm.faits_releve(fiche)
        for attendu in ("Produit : Publicitaire IA", "Promesse : Installe un publicitaire dans Claude",
                        "Prix : 67 EUR", "Appel à l'action : Touche le lien"):
            self.assertIn(attendu, lignes)
        self.assertNotIn("Pour qui", lignes)                  # un champ vide ne s'écrit pas

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg absent")
    def test_planches_neutres_puis_releve(self):
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre secrète", "lancement", [sm.lire_video("story:ouverture")], "2026-11-06")
            projet = sm.projets(dossier)[0][0]
            video = projet / "exports" / "story.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=s=1080x1920:r=30:d=7",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", str(video)], check=True)
            plan = dossier / "PLAN.md"
            plan.write_text(plan.read_text(encoding="utf-8").replace(
                "## Script\n", "## Script\n\n1. Une phrase du script, secrète.\n", 1), encoding="utf-8")
            fiche = json.loads((dossier / "OFFRE.json").read_text(encoding="utf-8"))
            fiche["produit"] = "Offre secrète"
            fiche["promesse"]["texte"] = "La promesse secrète"
            (dossier / "OFFRE.json").write_text(json.dumps(fiche, ensure_ascii=False), encoding="utf-8")

            with contextlib.redirect_stdout(io.StringIO()):
                sm.main(["relecture", str(video)])
            sortie = sm.dossier_relecture(video.resolve())
            self.addCleanup(shutil.rmtree, sortie, True)
            planches = sorted(sortie.glob("planche-*.jpg"))
            self.assertEqual(len(planches), 2)                 # 14 images, 12 par planche
            consigne = (sortie / "CONSIGNE.md").read_text(encoding="utf-8")
            for secret in ("secrète", "Offre", "PLAN", str(projet)):
                self.assertNotIn(secret, consigne.replace("ni un plan", ""))
            self.assertIn("de 6 à 7 s", consigne)

            with contextlib.redirect_stdout(io.StringIO()):
                sm.main(["relecture", str(video), "--releve"])
            releve = (sortie / "RELEVE.md").read_text(encoding="utf-8")
            self.assertIn("1. Une phrase du script, secrète.", releve)
            self.assertIn("Promesse : La promesse secrète", releve)

            with contextlib.redirect_stdout(io.StringIO()):
                sm.main(["relecture", str(video)])     # une nouvelle relecture à froid ne garde pas le relevé
            self.assertFalse((sortie / "RELEVE.md").exists())

    def test_le_modele_vide_n_est_pas_un_script(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "vente", [sm.lire_video("reel")], "2026-11-06")
            texte = (dossier / "PLAN.md").read_text(encoding="utf-8")
            self.assertEqual(sm.section_plan(texte, "Script")[:1], "(")   # le modèle vide, entre parenthèses


if __name__ == "__main__":
    unittest.main()
