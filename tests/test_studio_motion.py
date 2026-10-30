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
        # Story idéalement sous 30 s, Reel sous 45 s, page de vente sous 2 min.
        self.assertLessEqual(sm.SUPPORTS["story"]["ideal"][1], 30)
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
        self.assertEqual(sm.lecture("Nouveau"), 0.8)

    def test_par_mot(self):
        self.assertEqual(sm.lecture("Ton nouveau monteur"), 1.3)
        self.assertEqual(sm.lecture("Tes Reels montés par ton IA"), 2.0)

    def test_ecran_court(self):
        # Un écran porte 1 à 4 mots ; au-delà de 6, l'outil prévient.
        self.assertEqual((sm.MOTS_CONSEILLES, sm.MOTS_MAX), (4, 6))

    def test_ecran_final(self):
        self.assertEqual(sm.lecture("Commente MONTEUR", final=True), 2.5)

    def test_ponctuation_seule(self):
        self.assertEqual(sm.lecture(" — ! "), 0.0)


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
            self.assertEqual((fiche["produit"], fiche["objectif"]), ("Ma formation", "vente"))
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
            self.assertIn("### LinkedIn (4x5", texte)
            self.assertLess(texte.index("### LinkedIn"), texte.index("## Livraison"))
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
            for f in ("reel.mp4", "page.mp4", "story-teaser.mp4", "page.jpg", "legende-reel.txt",
                      "couverture.jpg", "integration.md", "stories.txt"):
                (dossier / "livraison" / f).write_bytes(b"x")
            (dossier / "PLAN.md").write_text("## Quand publier\n", encoding="utf-8")
            self.assertEqual(sm.manques_livraison(dossier), [])

    def test_vente_sans_calendrier(self):
        with tempfile.TemporaryDirectory() as d:
            maison = racine_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "fonctionnalite", [sm.lire_video("section")], "2026-10-12")
            (dossier / "livraison" / "section.mp4").write_bytes(b"x")
            (dossier / "livraison" / "section.jpg").write_bytes(b"x")
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


if __name__ == "__main__":
    unittest.main()
