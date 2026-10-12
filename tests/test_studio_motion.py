"""Tests de tools/studio_motion.py : la partie qui ne dépend ni de ffmpeg ni de l'app.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

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


class Lecture(unittest.TestCase):
    def test_plancher(self):
        self.assertEqual(sm.lecture("Nouveau"), 1.2)

    def test_par_mot(self):
        self.assertEqual(sm.lecture("Tes Reels montés par ton IA"), 2.4)

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

    def test_chaine_mastering(self):
        self.assertIn("volume=12.50dB", sm.chaine_mastering(12.5))


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


def maison_de_test(racine: Path) -> Path:
    maison = racine / "Monteur IA"
    (maison / "templates").mkdir(parents=True)
    (maison / "templates" / "AGENT.md.tpl").write_text("# test\n", encoding="utf-8")
    (maison / "brand").mkdir()
    (maison / "brand" / "tokens.css").write_text(":root{}", encoding="utf-8")
    (maison / "hyperframes.json").write_text("{}", encoding="utf-8")
    return maison


class Creation(unittest.TestCase):
    def test_serie_multi_formats(self):
        with tempfile.TemporaryDirectory() as d:
            maison = maison_de_test(Path(d))
            videos = [sm.lire_video(s) for s in ("reel", "page", "page@1x1", "story:ouverture")]
            dossier = sm.creer(maison, "Ma formation", "vente", videos, "2026-10-12")
            self.assertEqual(dossier.parent.name, "studio-motion")
            self.assertEqual(dossier.name, "Ma formation · 2026-10-12")
            liste = {meta["video"]: (p, meta) for p, meta in sm.projets(dossier)}
            self.assertEqual(sorted(liste), ["page", "page-1x1", "reel", "story-ouverture"])
            page, meta = liste["page"]
            self.assertEqual((meta["lieu"], meta["format"], meta["objectif"]), ("studio-motion", "16x9", "vente"))
            html = (page / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-width="1920" data-height="1080"', html)
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

    def test_doublon_refuse(self):
        with tempfile.TemporaryDirectory() as d:
            maison = maison_de_test(Path(d))
            with self.assertRaises(SystemExit):
                sm.creer(maison, "X", "vente", [sm.lire_video("reel"), sm.lire_video("reel")], "2026-10-12")

    def test_meta_retrouvee_depuis_un_export(self):
        with tempfile.TemporaryDirectory() as d:
            maison = maison_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "fonctionnalite", [sm.lire_video("section")], "2026-10-12")
            projet = sm.projets(dossier)[0][0]
            video = projet / "exports" / "section.mp4"
            video.write_bytes(b"x")
            self.assertEqual(sm.meta_de(video)["support"], "section")
            self.assertIsNone(sm.meta_de(maison))

    def test_livraison(self):
        with tempfile.TemporaryDirectory() as d:
            maison = maison_de_test(Path(d))
            videos = [sm.lire_video(s) for s in ("reel", "page", "story:teaser")]
            dossier = sm.creer(maison, "Offre", "lancement", videos, "2026-10-12")
            manques = sm.manques_livraison(dossier)
            for attendu in ("reel.mp4", "page.mp4", "story-teaser.mp4", "page.jpg (l'affiche, montrée avant la lecture)",
                            "legende-reel.txt (le texte de publication)"):
                self.assertIn(attendu, manques)
            self.assertTrue(any("Quand publier" in m for m in manques))
            self.assertIn("couverture.jpg (la couverture du Reel)", manques)
            self.assertIn("integration.md (comment poser la vidéo sur la page)", manques)
            for f in ("reel.mp4", "page.mp4", "story-teaser.mp4", "page.jpg", "legende-reel.txt",
                      "couverture.jpg", "integration.md"):
                (dossier / "livraison" / f).write_bytes(b"x")
            (dossier / "PLAN.md").write_text("## Quand publier\n", encoding="utf-8")
            self.assertEqual(sm.manques_livraison(dossier), [])

    def test_vente_sans_calendrier(self):
        with tempfile.TemporaryDirectory() as d:
            maison = maison_de_test(Path(d))
            dossier = sm.creer(maison, "Offre", "fonctionnalite", [sm.lire_video("section")], "2026-10-12")
            (dossier / "livraison" / "section.mp4").write_bytes(b"x")
            (dossier / "livraison" / "section.jpg").write_bytes(b"x")
            self.assertEqual(sm.manques_livraison(dossier), ["integration.md (comment poser la vidéo sur la page)"])
            (dossier / "livraison" / "integration.md").write_text("x", encoding="utf-8")
            self.assertEqual(sm.manques_livraison(dossier), [])


if __name__ == "__main__":
    unittest.main()
