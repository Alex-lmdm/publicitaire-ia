"""Tests de tools/telechargeur.py : où le téléchargeur est cherché, sans rien installer."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import telechargeur  # noqa: E402


class TestTelechargeur(unittest.TestCase):
    def test_version_assez_recente(self):
        self.assertTrue(telechargeur.assez_recent("2026.08.19"))
        self.assertTrue(telechargeur.assez_recent(telechargeur.VERSION_MIN))
        self.assertFalse(telechargeur.assez_recent("2025.12.31"))
        self.assertFalse(telechargeur.assez_recent(""))

    def test_celui_du_dossier_passe_avant_celui_de_l_ordinateur(self):
        with tempfile.TemporaryDirectory() as d:
            venv = Path(d) / ".telechargeur-venv"
            exe = telechargeur.venv_bin("yt-dlp", venv)
            exe.parent.mkdir(parents=True)
            exe.write_text("")
            with mock.patch("shutil.which", return_value="/usr/bin/yt-dlp"):
                self.assertEqual(telechargeur.executable(venv), str(exe))

    def test_un_yt_dlp_trop_ancien_de_l_ordinateur_est_ignore(self):
        with tempfile.TemporaryDirectory() as d:
            venv = Path(d) / ".telechargeur-venv"
            with mock.patch("shutil.which", return_value="/usr/bin/yt-dlp"), \
                 mock.patch.object(telechargeur, "version_ytdlp", return_value="2024.01.01"):
                self.assertIsNone(telechargeur.executable(venv))
            with mock.patch("shutil.which", return_value="/usr/bin/yt-dlp"), \
                 mock.patch.object(telechargeur, "version_ytdlp", return_value="2026.08.19"):
                self.assertEqual(telechargeur.executable(venv), "/usr/bin/yt-dlp")

    def test_aucun_telechargeur(self):
        with tempfile.TemporaryDirectory() as d:
            with mock.patch("shutil.which", return_value=None):
                self.assertIsNone(telechargeur.executable(Path(d) / ".telechargeur-venv"))


if __name__ == "__main__":
    unittest.main()
