"""Tests de tools/annonce.py : la partie qui ne dépend ni de ffmpeg ni de l'app.

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
import annonce  # noqa: E402


def fiche_valide() -> dict:
    return {
        "produit": "Monteur IA",
        "lien": "https://www.lemondedumarketing.fr/monteur-ia",
        "type": "lancement",
        "promesse": {"texte": "Tes Reels montés par ton IA", "source": "page"},
        "recoit": [{"texte": "Le système complet", "source": "page"}],
        "prix": {"montant": 97, "devise": "EUR", "barre": None, "source": "page"},
        "bonus": [{"texte": "Reel Cloneur offert", "source": "page"}],
        "dates": {"ouverture": "2026-10-16T18:00", "fermeture": "2026-10-19T23:59", "source": "client"},
        "preuves": [{"type": "chiffre", "texte": "3,3 millions de vues", "source": "page"}],
        "cta": {"mot_cle": "MONTEUR", "phrase": "Commente MONTEUR", "source": "client"},
        "interdits": [],
    }


class Lecture(unittest.TestCase):
    def test_plancher(self):
        self.assertEqual(annonce.lecture("Nouveau"), 1.2)

    def test_par_mot(self):
        # 6 mots : 6 × 0,35 + 0,3 = 2,4 s
        self.assertEqual(annonce.lecture("Tes Reels montés par ton IA"), 2.4)

    def test_ecran_final(self):
        self.assertEqual(annonce.lecture("Commente MONTEUR", final=True), 2.5)

    def test_ponctuation_seule(self):
        self.assertEqual(annonce.lecture(" — ! "), 0.0)


class Zones(unittest.TestCase):
    def test_zone_texte_reel(self):
        z = annonce.zone_texte("reel")
        self.assertEqual((z["x"], z["y"]), (100, 300))
        self.assertEqual(z["x"] + z["largeur"], 1080 - 150)
        self.assertEqual(z["y"] + z["hauteur"], 1920 - 480)

    def test_sticker_dans_la_zone_story(self):
        self.assertTrue(annonce.dans(annonce.STICKER, annonce.zone_texte("story")))

    def test_chevauchement(self):
        a = {"x": 0, "y": 0, "largeur": 10, "hauteur": 10}
        self.assertTrue(annonce.chevauche(a, {"x": 5, "y": 5, "largeur": 10, "hauteur": 10}))
        self.assertFalse(annonce.chevauche(a, {"x": 10, "y": 0, "largeur": 5, "hauteur": 5}))


class Fiche(unittest.TestCase):
    def test_fiche_valide(self):
        self.assertEqual(annonce.verifier_fiche(fiche_valide(), ["reel", "dernier-jour"]), [])

    def test_fait_sans_source(self):
        f = fiche_valide()
        f["bonus"][0]["source"] = ""
        self.assertTrue(any("bonus[0]" in p for p in annonce.verifier_fiche(f)))

    def test_temoignage_mot_pour_mot(self):
        f = fiche_valide()
        f["preuves"].append({"type": "temoignage", "texte": "Génial", "source": "page"})
        self.assertTrue(any("mot pour mot" in p for p in annonce.verifier_fiche(f)))

    def test_dernier_jour_sans_fermeture(self):
        f = fiche_valide()
        f["dates"]["fermeture"] = None
        self.assertTrue(any("dernier jour" in p for p in annonce.verifier_fiche(f, ["dernier-jour"])))

    def test_prix_barre_doit_etre_plus_haut(self):
        f = fiche_valide()
        f["prix"]["barre"] = 67
        self.assertTrue(any("prix.barre" in p for p in annonce.verifier_fiche(f)))

    def test_promesse_trop_longue(self):
        f = fiche_valide()
        f["promesse"]["texte"] = "Une promesse beaucoup trop longue pour tenir sur un écran de téléphone"
        self.assertTrue(any("promesse" in p and "mots" in p for p in annonce.verifier_fiche(f)))

    def test_mot_cle(self):
        f = fiche_valide()
        f["cta"]["mot_cle"] = "mon mot"
        self.assertTrue(any("mot_cle" in p for p in annonce.verifier_fiche(f)))

    def test_dates_dans_l_ordre(self):
        f = fiche_valide()
        f["dates"]["fermeture"] = "2026-10-01"
        self.assertTrue(any("fermeture doit suivre" in p for p in annonce.verifier_fiche(f)))

    def test_fiche_vide_signale_l_essentiel(self):
        pb = annonce.verifier_fiche(copy.deepcopy(annonce.FICHE_VIDE))
        self.assertTrue(any(p.startswith("produit") for p in pb))
        self.assertTrue(any(p.startswith("promesse") for p in pb))
        self.assertTrue(any(p.startswith("cta") for p in pb))


class Planche(unittest.TestCase):
    def test_un_par_seconde_et_derniere_image(self):
        t = annonce.instants_planche(3.0, None)
        self.assertEqual(t[0], 0.3)
        self.assertEqual(t[-1], 2.93)

    def test_reperes_bornes(self):
        self.assertEqual(annonce.instants_planche(2.0, [-1, 0.5, 9]), [0.0, 0.5, 1.93])


class Son(unittest.TestCase):
    def test_dans_la_cible(self):
        self.assertEqual(annonce.verdict_sonore({"input_i": "-16.3", "input_tp": "-1.8"}), [])

    def test_trop_faible_et_sature(self):
        pb = annonce.verdict_sonore({"input_i": "-20", "input_tp": "-0.2"})
        self.assertEqual(len(pb), 2)

    def test_muet(self):
        self.assertIn("muette", annonce.verdict_sonore({"input_i": "-inf", "input_tp": "-inf"})[0])


class Export(unittest.TestCase):
    def info(self, **video):
        v = {"codec_type": "video", "codec_name": "h264", "width": 1080, "height": 1920, "pix_fmt": "yuv420p", "r_frame_rate": "30/1"}
        v.update(video)
        return {"streams": [v, {"codec_type": "audio", "codec_name": "aac"}], "format": {"duration": "20.0"}}

    def test_conforme(self):
        self.assertEqual(annonce.verdict_export(self.info(), "reel", "reel"), [])

    def test_ecarts(self):
        pb = annonce.verdict_export(self.info(width=1920, height=1080, pix_fmt="yuv444p"), "reel")
        self.assertEqual(len(pb), 2)

    def test_duree_hors_bornes(self):
        info = self.info()
        info["format"]["duration"] = "40"
        self.assertTrue(any("durée" in p for p in annonce.verdict_export(info, "story", "teaser")))

    def test_debut_rapide(self):
        with tempfile.TemporaryDirectory() as d:
            rapide, lent = Path(d) / "a.mp4", Path(d) / "b.mp4"
            rapide.write_bytes(b"....ftyp....moov....mdat....")
            lent.write_bytes(b"....ftyp....mdat....moov....")
            self.assertTrue(annonce.debut_rapide(rapide))
            self.assertFalse(annonce.debut_rapide(lent))


class SansMusique(unittest.TestCase):
    def test_retire_seulement_la_musique(self):
        html = ('<audio id="musique" data-role="musique" src="assets/audio/m.mp3" data-start="0"></audio>\n'
                '<audio id="clic" src="assets/audio/clic.mp3" data-start="1"></audio>')
        sortie, n = annonce.sans_musique_html(html)
        self.assertEqual(n, 1)
        self.assertNotIn("musique", sortie)
        self.assertIn("clic.mp3", sortie)

    def test_musique_posee_par_monteur_ia(self):
        html = ('<audio id="musique" src="assets/sons/musique-m.mp3" data-start="0" data-track-index="19"></audio>\n'
                '<audio id="sfx-01" src="assets/sons/pop.mp3" data-start="1.2"></audio>')
        sortie, n = annonce.sans_musique_html(html)
        self.assertEqual(n, 1)
        self.assertIn("sfx-01", sortie)
        self.assertNotIn('id="musique"', sortie)


class Creation(unittest.TestCase):
    def test_annonce_complete_sans_ecraser(self):
        with tempfile.TemporaryDirectory() as d:
            maison = Path(d) / "Monteur IA"
            (maison / "templates").mkdir(parents=True)
            (maison / "templates" / "AGENT.md.tpl").write_text("# test\n", encoding="utf-8")
            (maison / "brand").mkdir()
            (maison / "brand" / "tokens.css").write_text(":root{}", encoding="utf-8")
            (maison / "hyperframes.json").write_text("{}", encoding="utf-8")
            dossier = annonce.creer_annonce(maison, "Ma formation", ["reel", "ouvert"], "2026-10-12")
            self.assertEqual(dossier.name, "Ma formation · 2026-10-12")
            projets = sorted(p for p in dossier.iterdir() if (p / "meta.json").is_file())
            self.assertEqual([p.name for p in projets], ["Ma formation · Reel", "Ma formation · Story ouverture"])
            meta = json.loads((projets[0] / "meta.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["monteurIa"]["lieu"], "annonce")
            self.assertTrue((projets[0] / "index.html").is_file())
            self.assertIn("1080", (projets[0] / "index.html").read_text(encoding="utf-8"))
            self.assertTrue((projets[0] / "CLAUDE.md").is_file())
            self.assertTrue((projets[0] / "brand" / "tokens.css").is_file())
            self.assertIn("render", json.loads((projets[0] / "package.json").read_text(encoding="utf-8"))["scripts"])
            fiche = json.loads((dossier / "OFFRE.json").read_text(encoding="utf-8"))
            self.assertEqual(fiche["produit"], "Ma formation")
            deuxieme = annonce.creer_annonce(maison, "Ma formation", ["reel"], "2026-10-12")
            self.assertEqual(deuxieme.name, "Ma formation · 2026-10-12 (2)")

    def test_livraison_incomplete(self):
        with tempfile.TemporaryDirectory() as d:
            maison = Path(d) / "M"
            (maison / "templates").mkdir(parents=True)
            (maison / "templates" / "AGENT.md.tpl").write_text("", encoding="utf-8")
            dossier = annonce.creer_annonce(maison, "Offre", ["reel", "teaser"], "2026-10-12")
            manques = annonce.manques_livraison(dossier)
            self.assertIn("reel.mp4", manques)
            self.assertIn("teaser.mp4", manques)
            self.assertTrue(any("Quand publier" in m for m in manques))
            for f in ("reel.mp4", "teaser.mp4", "legende.txt", "couverture.jpg"):
                (dossier / "livraison" / f).write_bytes(b"x")
            (dossier / "PLAN.md").write_text("## Quand publier\n", encoding="utf-8")
            self.assertEqual(annonce.manques_livraison(dossier), [])

    def test_video_inconnue(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(SystemExit):
                annonce.creer_annonce(Path(d), "X", ["tiktok"], "2026-10-12")


if __name__ == "__main__":
    unittest.main()
