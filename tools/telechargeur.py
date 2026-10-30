#!/usr/bin/env python3
"""TÉLÉCHARGEUR : yt-dlp, pour lire une vidéo de référence depuis son lien (YouTube, TikTok,
Instagram, X), sans que le client ait à l'enregistrer lui-même.

Il vit dans `.telechargeur-venv/`, à la racine du dossier : un environnement Python à part, jamais
celui de l'ordinateur. yt-dlp demande Python 3.10 ou plus récent ; macOS fournit 3.9, on cherche donc
celui de Homebrew ou de python.org. Gratuit, une minute, toujours avec l'accord du client
(`studio_motion.py telechargeur installer`). Même mécanique que le Reel Cloneur de Monteur IA.

Instagram et TikTok changent souvent : yt-dlp se met à jour tout seul, au plus toutes les 12 h,
sans bloquer si l'ordinateur est hors ligne.
Python 3.9+, bibliothèque standard seulement.
"""
from __future__ import annotations

import datetime
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
VENV = RACINE / ".telechargeur-venv"
WIN = sys.platform.startswith("win")
PAQUET = "yt-dlp[default,curl-cffi]"
VERSION_MIN = "2026.07.01"     # en dessous, Instagram ne se télécharge plus sans connexion
MAJ_STAMP = VENV / ".derniere-maj"
MAJ_INTERVALLE = 12 * 3600


class ErreurTelechargeur(Exception):
    pass


def lancer(cmd: list[str], timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)


def venv_bin(nom: str, venv: Path = VENV) -> Path:
    return venv / ("Scripts" if WIN else "bin") / (nom + (".exe" if WIN else ""))


def version_python(exe: str) -> tuple[int, int] | None:
    try:
        r = lancer([exe, "-c", "import sys; print('%d.%d' % sys.version_info[:2])"], timeout=20)
        if r.returncode == 0:
            majeur, mineur = r.stdout.strip().split(".")
            return int(majeur), int(mineur)
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return None


def python_recent() -> str | None:
    """Un Python 3.10+ pour l'environnement : celui qui tourne, sinon Homebrew, python.org ou `py` (Windows)."""
    noms = ["python3.13", "python3.12", "python3.11", "python3.14", "python3.10", "python3", "python"]
    candidats = [sys.executable] + [p for p in (shutil.which(n) for n in noms) if p]
    for prefixe in ("/opt/homebrew/bin", "/usr/local/bin", "/Library/Frameworks/Python.framework/Versions/Current/bin"):
        candidats += [str(Path(prefixe) / n) for n in noms if (Path(prefixe) / n).exists()]
    if WIN and shutil.which("py"):
        for v in ("3.13", "3.12", "3.11", "3.10"):
            r = lancer(["py", f"-{v}", "-c", "import sys; print(sys.executable)"], timeout=20)
            if r.returncode == 0 and r.stdout.strip():
                candidats.append(r.stdout.strip())
    vus: set[str] = set()
    for c in candidats:
        if c in vus:
            continue
        vus.add(c)
        v = version_python(c)
        if v and v >= (3, 10):
            return c
    return None


def version_ytdlp(exe: str) -> str:
    try:
        r = lancer([exe, "--version"], timeout=60)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def assez_recent(version: str) -> bool:
    def cle(v: str) -> tuple[int, ...]:
        return tuple(int(x) for x in re.findall(r"\d+", v)[:3])
    return bool(version) and cle(version) >= cle(VERSION_MIN)


def executable(venv: Path = VENV) -> str | None:
    """yt-dlp de l'environnement du dossier, sinon celui de l'ordinateur s'il est assez récent."""
    p = venv_bin("yt-dlp", venv)
    if p.exists():
        return str(p)
    systeme = shutil.which("yt-dlp")
    if systeme and assez_recent(version_ytdlp(systeme)):
        return systeme
    return None


def mettre_a_jour(forcer: bool = False) -> None:
    py = venv_bin("python")
    if not py.exists():
        return
    if not forcer and MAJ_STAMP.exists() and time.time() - MAJ_STAMP.stat().st_mtime < MAJ_INTERVALLE:
        return
    try:
        # Hors ligne, pip réessaie longtemps par défaut : on coupe court (10 s, un seul nouvel essai).
        r = lancer([str(py), "-m", "pip", "install", "--upgrade", "--quiet", "--disable-pip-version-check",
                    "--timeout", "10", "--retries", "1", PAQUET], timeout=120)
        if r.returncode == 0:
            MAJ_STAMP.write_text(datetime.datetime.now().isoformat())
    except (OSError, subprocess.SubprocessError):
        pass


def installer() -> str:
    """Crée `.telechargeur-venv/` et y installe yt-dlp. Rend la version installée."""
    py = venv_bin("python")
    if py.exists() and not (version_python(str(py)) or (0, 0)) >= (3, 10):
        shutil.rmtree(VENV, ignore_errors=True)
    if not py.exists():
        base = python_recent()
        if not base:
            conseil = ("brew install python@3.12 (sans Homebrew : son installeur Homebrew.pkg, étape 1 d'INSTALL.md, "
                       "jamais son script install.sh)" if sys.platform == "darwin"
                       else "winget install -e --id Python.Python.3.12" if WIN else "sudo apt install python3.12-venv")
            raise ErreurTelechargeur("il faut un Python 3.10 ou plus récent pour le téléchargeur (celui de "
                                     f"l'ordinateur est plus ancien) : {conseil}, puis relance l'installation.")
        r = lancer([base, "-m", "venv", str(VENV)], timeout=300)
        if r.returncode != 0:
            raise ErreurTelechargeur("impossible de créer .telechargeur-venv/ : " + (r.stderr or r.stdout)[-500:])
    r = lancer([str(py), "-m", "pip", "install", "--upgrade", "--quiet", "--disable-pip-version-check", PAQUET], timeout=600)
    if r.returncode != 0:
        raise ErreurTelechargeur("l'installation de yt-dlp a échoué (connexion internet ?) : " + (r.stderr or r.stdout)[-500:])
    MAJ_STAMP.write_text(datetime.datetime.now().isoformat())
    v = version_ytdlp(str(venv_bin("yt-dlp")))
    if not assez_recent(v):
        raise ErreurTelechargeur(f"yt-dlp {v or '?'} est trop ancien (il faut {VERSION_MIN} ou plus).")
    return v
