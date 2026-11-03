"""Tests de tools/voix.py : le texte juste calé sur les temps des mots, et les respirations.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))

import voix  # noqa: E402


def mot(t, s, e):
    return {"text": t, "start": s, "end": e}


class Caler(unittest.TestCase):
    def test_mots_remplaces_sautes_et_ponctuation(self):
        """Ce que Parakeet a fait sur la voix Nika (03/11/2026) : « It's » pour « C'est », « Cloud »
        pour « Claude », « que ce soit » sauté."""
        texte = "C'est possible. Tu le branches à Claude ? Avant de créer quoi que ce soit, il réfléchit."
        reco = [mot("It's", 0.0, 0.3), mot("possible.", 0.3, 0.9), mot("Tu", 1.2, 1.3), mot("le", 1.3, 1.4),
                mot("branches", 1.4, 1.8), mot("à", 1.8, 1.9), mot("Cloud?", 1.9, 2.3), mot("Avant", 2.8, 3.1),
                mot("de", 3.1, 3.2), mot("créer", 3.2, 3.5), mot("quoi,", 3.5, 3.8), mot("il", 4.6, 4.7),
                mot("réfléchit.", 4.7, 5.3)]
        m = voix.caler(texte, reco)
        self.assertEqual([x["text"] for x in m], ["C'est", "possible.", "Tu", "le", "branches", "à", "Claude ?", "Avant",
                                                  "de", "créer", "quoi", "que", "ce", "soit,", "il", "réfléchit."])
        par = {x["text"]: x for x in m}
        self.assertEqual(par["C'est"]["start"], 0.0)                    # le temps du mot d'en face
        self.assertEqual(par["Claude ?"]["start"], 1.9)
        self.assertGreaterEqual(par["que"]["start"], par["quoi"]["start"])   # les mots sautés, entre leurs voisins
        self.assertLessEqual(par["soit,"]["end"], par["il"]["start"])
        debuts = [x["start"] for x in m]
        self.assertEqual(debuts, sorted(debuts))
        self.assertTrue(all(x["end"] > x["start"] for x in m))

    def test_debut_dans_un_silence_recale(self):
        m = voix.caler("Un deux.", [mot("Un", 0.0, 0.4), mot("deux.", 0.5, 1.0)], silences=[(0.4, 0.8)])
        self.assertEqual(m[1]["start"], 0.8)

    def test_projet(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "work").mkdir()
            (p / "assets" / "audio").mkdir(parents=True)
            (p / "work" / "voix.txt").write_text("Bonjour Alex.")
            (p / "assets" / "audio" / "transcript.json").write_text(json.dumps([mot("Bonjour", 0.1, 0.5), mot("Alice.", 0.5, 0.9)]))
            r = voix.caler_projet(p)
            self.assertEqual((r["mots"], r["concordants"]), (2, 1))
            ecrit = json.loads((p / "assets" / "audio" / "transcript.json").read_text())
            self.assertEqual(ecrit[1]["text"], "Alex.")
            self.assertTrue((p / "assets" / "audio" / "transcript-brut.json").is_file())
            voix.caler_projet(p)                                          # rejouable : repart toujours de la brute
            self.assertEqual(json.loads((p / "assets" / "audio" / "transcript-brut.json").read_text())[1]["text"], "Alice.")


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg absent")
class Respiration(unittest.TestCase):
    def test_ouvre_la_pause_et_decale_les_mots(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            audio = p / "assets" / "audio"
            audio.mkdir(parents=True)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "sine=f=300:d=2", "-f", "lavfi",
                            "-i", "anullsrc=r=48000:cl=mono:d=0.5", "-f", "lavfi", "-i", "sine=f=300:d=2", "-filter_complex",
                            "[0:a]aformat=sample_rates=48000:channel_layouts=mono[a];[2:a]aformat=sample_rates=48000:channel_layouts=mono[c];"
                            "[a][1:a][c]concat=n=3:v=0:a=1[o]", "-map", "[o]", str(audio / "voix.wav")], check=True)
            (audio / "transcript.json").write_text(json.dumps([mot("Un", 0.0, 2.0), mot("deux.", 2.5, 4.5)]))
            r = voix.respiration(p, 2.2, 1.5)
            self.assertAlmostEqual(r["ajout"], 1.0, delta=0.05)
            self.assertAlmostEqual(r["duree"], 5.5, delta=0.05)
            mots = json.loads((audio / "transcript.json").read_text())
            self.assertEqual(mots[0]["start"], 0.0)
            self.assertAlmostEqual(mots[1]["start"], 3.5, delta=0.05)
            self.assertTrue((audio / "voix-avant-respiration.wav").is_file())


if __name__ == "__main__":
    unittest.main()
