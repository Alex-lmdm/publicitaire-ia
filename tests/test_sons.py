"""Tests de tools/sons.py : la musique sous une voix off (recherche du 03/11/2026, son.md).

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))

import sons  # noqa: E402


def voix_synthetique(dest: Path, morceaux) -> None:
    """Une « voix » faite de sons (secondes) et de silences (négatif), en mono 48 kHz."""
    parts, filtres = [], []
    for i, d in enumerate(morceaux):
        src = f"sine=f=300:d={d}" if d > 0 else f"anullsrc=r=48000:cl=mono:d={-d}"
        parts += ["-f", "lavfi", "-i", src]
        filtres.append(f"[{i}:a]aformat=sample_rates=48000:channel_layouts=mono,volume=0.3[a{i}]")
    filtres.append("".join(f"[a{i}]" for i in range(len(morceaux))) + f"concat=n={len(morceaux)}:v=0:a=1[o]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *parts, "-filter_complex", ";".join(filtres), "-map", "[o]", str(dest)], check=True)


class Enveloppe(unittest.TestCase):
    def test_respiration_creux_debut_et_fin(self):
        blocs, trous = [(2.0, 8.0), (10.0, 20.0)], [(8.0, 10.0)]
        pts = sons.enveloppe_sous_voix(blocs, trous, 24.0, 0.05, 0.16, entree=8.4)
        t = [p["t"] for p in pts]
        self.assertEqual(t, sorted(t))                                   # le temps avance toujours
        self.assertEqual(pts[0]["v"], 0)
        self.assertEqual(pts[-1], {"t": 24.0, "v": 0.0})                 # fondu jusqu'au silence
        au = lambda x: next(p["v"] for p in pts if p["t"] >= x)
        self.assertEqual(au(1.0), 0.16)                                  # premier mot après 1,5 s : la musique est en avant
        self.assertEqual(au(2.0), 0.05)                                  # sous la voix dès le premier mot
        self.assertLess(au(8.2), 0.02)                                   # le creux avant l'entrée franche
        self.assertEqual(au(8.9), 0.16)                                  # la respiration, en avant
        self.assertEqual(au(10.0), 0.05)                                 # redescendue au mot suivant
        self.assertEqual(au(21.3), 0.16)                                 # après le dernier mot

    def test_sans_respiration_la_musique_reste_basse(self):
        pts = sons.enveloppe_sous_voix([(0.4, 19.0)], [], 20.0, 0.05, 0.16)
        self.assertTrue(all(p["v"] <= 0.05 for p in pts if 0.4 <= p["t"] <= 19.0))


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg absent")
class Pauses(unittest.TestCase):
    def test_une_pause_courte_ne_coupe_pas_le_bloc(self):
        with tempfile.TemporaryDirectory() as d:
            v = Path(d) / "voix.wav"
            voix_synthetique(v, [1.0, -0.6, 1.0, -2.0, 1.0])
            blocs, trous = sons.blocs_de_parole(v, 0.5, 10.0)
            self.assertEqual(len(blocs), 2)                              # 0,6 s : même bloc ; 2 s : une respiration
            self.assertEqual(len(trous), 1)
            self.assertAlmostEqual(blocs[0][0], 0.5, delta=0.05)
            self.assertAlmostEqual(trous[0][1] - trous[0][0], 2.0, delta=0.1)

    def test_musique_posee_a_l_ecart_sous_la_voix(self):
        with tempfile.TemporaryDirectory() as d:
            projet = Path(d)
            audio = projet / "assets" / "audio"
            audio.mkdir(parents=True)
            voix_synthetique(audio / "voix.wav", [3.0, -2.0, 3.0])
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anoisesrc=d=12:c=pink:a=0.3", "-ar", "48000",
                            "-ac", "2", str(audio / "musique.wav")], check=True)
            (projet / "index.html").write_text('<div data-composition-id="main" data-duration="11">\n  <!-- SONS -->\n</div>\n')
            rapport = sons.poser(projet, [], musique=audio / "musique.wav", voix_off={"src": audio / "voix.wav", "start": 0.5},
                                 ecart=(18.0, 8.0))
            m = rapport["musique"]
            self.assertEqual(m["respirations"], 1)
            self.assertAlmostEqual(m["voix"] - (m["reference"] + m["gain"]), 18.0, delta=0.2)   # l'écart visé
            self.assertEqual(rapport["limite"], sons.LIMITE_VOIX_DB)
            self.assertIn("Musique sous la voix", sons.resume_niveau(rapport))


if __name__ == "__main__":
    unittest.main()
