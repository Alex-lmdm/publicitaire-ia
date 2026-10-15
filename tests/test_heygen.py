"""Tests de tools/heygen.py et de la commande `heygen` : sans réseau (l'API est simulée).

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))
import heygen  # noqa: E402
import sons  # noqa: E402
import studio_motion as sm  # noqa: E402

CLE = "sk_V2_hgu_test_0123456789abcdefABCDEF"


def piste(i: int, duree: float) -> dict:
    return {"id": f"{i:02d}abcdef0123456789", "name": f"Astral Generated Music: {i}", "duration": duree,
            "description": f"upbeat launch track {i}", "audio_url": f"https://exemple.test/m{i}.wav?X-Amz=1", "type": "music"}


class Cle(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.patch = mock.patch.object(heygen, "FICHIER_CLE", self.tmp / ".heygen" / "credentials")
        self.patch.start()
        self.env = mock.patch.dict(os.environ, {}, clear=False)
        self.env.start()
        os.environ.pop("HEYGEN_API_KEY", None)

    def tearDown(self):
        self.patch.stop()
        self.env.stop()
        shutil.rmtree(self.tmp)

    def test_ordre_des_sources(self):
        self.assertIsNone(heygen.cle())
        self.assertIsNone(heygen.source_cle())
        heygen.FICHIER_CLE.parent.mkdir()
        heygen.FICHIER_CLE.write_text(CLE + "\n")
        self.assertEqual(heygen.cle(), CLE)
        self.assertEqual(heygen.source_cle(), "~/.heygen/credentials")
        os.environ["HEYGEN_API_KEY"] = "sk_env_0123456789abcdefghij"
        self.assertEqual(heygen.cle(), "sk_env_0123456789abcdefghij")

    def test_connexion_oauth_reconnue(self):
        heygen.FICHIER_CLE.parent.mkdir()
        heygen.FICHIER_CLE.write_text('{"oauth": {"access_token": "x"}}')
        self.assertIsNone(heygen.cle())
        self.assertEqual(heygen.source_cle(), "oauth")

    def test_enregistrer_verifie_puis_ne_remplace_pas_sans_accord(self):
        with mock.patch.object(heygen, "verifier_cle") as verif:
            f = heygen.enregistrer_cle("  " + CLE + "\n")
            verif.assert_called_once_with(CLE)
        self.assertEqual(f.read_text().strip(), CLE)
        if os.name != "nt":
            self.assertEqual(f.stat().st_mode & 0o777, 0o600)
        with mock.patch.object(heygen, "verifier_cle"):
            with self.assertRaises(heygen.ErreurHeygen):
                heygen.enregistrer_cle("sk_autre_0123456789abcdefghij")
            heygen.enregistrer_cle("sk_autre_0123456789abcdefghij", remplacer=True)
        self.assertEqual(f.read_text().strip(), "sk_autre_0123456789abcdefghij")

    def test_clé_mal_copiée(self):
        with self.assertRaises(heygen.ErreurHeygen):
            heygen.enregistrer_cle("ma clé avec des espaces")

    def test_sans_cle_message_clair(self):
        with self.assertRaises(heygen.ErreurHeygen) as e:
            heygen.appel("GET", "/v3/audio/sounds")
        self.assertIn("heygen connecter", str(e.exception))


class Musiques(unittest.TestCase):
    def test_filtre_par_duree_et_pagine(self):
        pages = [{"data": [piste(1, 20), piste(2, 90)], "has_more": True, "next_token": "t2"},
                 {"data": [piste(3, 15), piste(4, 70)], "has_more": False}]
        with mock.patch.object(heygen, "appel", side_effect=pages) as appel:
            res = heygen.chercher_musiques("launch", nombre=5, duree_min=60)
        self.assertEqual([p["duration"] for p in res], [90, 70])
        self.assertEqual(appel.call_args_list[1].args[2]["token"], "t2")

    def test_page_ecoute_echappe(self):
        with tempfile.TemporaryDirectory() as d:
            page = heygen.page_ecoute("Titre", "Consigne", [{"numero": 1, "nom": "<b>x</b>", "detail": "a&b",
                                                             "url": 'https://e.test/a.wav?x=1&y="2"'}], Path(d) / "p.html")
            texte = page.read_text()
        self.assertIn("&lt;b&gt;x&lt;/b&gt;", texte)
        self.assertIn('src="https://e.test/a.wav?x=1&amp;y=&quot;2&quot;"', texte)

    def test_extension_d_un_lien_signe(self):
        self.assertEqual(heygen.extension("https://s3.test/v/abc.wav?X-Amz-Signature=1", ".mp3"), ".wav")
        self.assertEqual(heygen.extension("https://s3.test/v/abc?X=1", ".mp3"), ".mp3")


class Voix(unittest.TestCase):
    def test_cout_annonce_sans_aucun_appel(self):
        with mock.patch.object(heygen, "appel") as appel:
            with self.assertRaises(heygen.ErreurHeygen) as e:
                heygen.parler("Ton offre mérite une vraie vidéo, faite en dix minutes.", "v1")
            appel.assert_not_called()
        self.assertIn("--confirme", str(e.exception))
        secondes, dollars = heygen.cout_voix(" ".join(["mot"] * 150))      # 150 mots ≈ 1 min
        self.assertAlmostEqual(secondes, 60, delta=1)
        self.assertAlmostEqual(dollars, 0.04, delta=0.005)

    def test_commande_parler_refuse_sans_accord(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "index.html").write_text("<html></html>")
            with mock.patch.object(heygen, "appel") as appel, self.assertRaises(SystemExit) as e:
                sm.main(["heygen", "parler", "Bonjour à toi", "--voix", "v1", "--dans", d])
            appel.assert_not_called()
        self.assertIn("payante", str(e.exception.code))

    def test_commande_prendre_range_et_source(self):
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d)
            (projet / "index.html").write_text("<html></html>")
            (projet / "work").mkdir()
            (projet / "work" / "musiques-heygen.json").write_text(json.dumps({"requete": "x", "pistes": [piste(7, 80)]}))

            def faux(url, dest):
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(b"RIFF")
                return dest
            with mock.patch.object(heygen, "telecharger", side_effect=faux), redirect_stdout(io.StringIO()):
                sm.main(["heygen", "prendre", "1", "--dans", d])
                sm.main(["heygen", "prendre", "1", "--dans", d])           # deux fois : une seule ligne de source
            self.assertTrue((projet / "assets" / "audio" / "heygen-07abcdef.wav").is_file())
            source = (projet / "assets" / "audio" / "SOURCE.md").read_text()
            self.assertEqual(source.count("heygen-07abcdef.wav"), 1)
            with self.assertRaises(SystemExit):
                sm.main(["heygen", "prendre", "2", "--dans", d])


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg absent")
class VoixDansLeMixage(unittest.TestCase):
    def test_voix_posee_mesuree_et_musique_dessous(self):
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d)
            audio = projet / "assets" / "audio"
            audio.mkdir(parents=True)
            for nom, src in (("voix.wav", "sine=f=300:d=4"), ("musique.wav", "sine=f=110:d=10")):
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", src, "-af", "volume=0.2",
                                "-ar", "48000", str(audio / nom)], check=True)
            (projet / "index.html").write_text('<div data-composition-id="main" data-duration="6">\n  <!-- SONS -->\n</div>\n')
            (projet / "sons.json").write_text(json.dumps({"voix": "assets/audio/voix.wav", "voix_debut": 0.5,
                                                          "musique": "assets/audio/musique.wav", "evenements": []}))
            sortie = io.StringIO()
            with redirect_stdout(sortie):
                sm.main(["sons", str(projet), str(projet / "sons.json")])
            page = (projet / "index.html").read_text()
            self.assertIn('id="voix" src="assets/audio/voix.wav" data-start="0.500" data-duration="4.000"', page)
            self.assertIn(f'data-volume="{sons.lin(-26.5)}"', page)              # la musique sous la voix
            self.assertIn("la voix et la musique posés", sortie.getvalue())
            self.assertIn("gain", sortie.getvalue())                             # voix audible : niveau final réglé


if __name__ == "__main__":
    unittest.main()
