#!/usr/bin/env python3
"""LES STYLES DU CATALOGUE : les 8 looks de `.claude/skills/studio/styles/`, lus dans leur index, et
leurs aperçus (`assets/styles/<dossier>.mp4|.jpg`).

Appelé par `studio_motion.py musiques choisir` : le style se choisit avec la musique, sur la même
page (SKILL.md, étape 4). Un style gardé par le client (« garde ce style pour mes prochaines
vidéos ») est `style N` dans les préférences de `studio.config.json` ; ses premières vidéos
disaient `template N`, qui vaut pareil.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

INDEX = Path(".claude") / "skills" / "studio" / "styles" / "README.md"
APERCUS = Path("assets") / "styles"
# | N° | Style | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
LIGNE = re.compile(r"^\| (\d+) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| `([^`]+)` \|$")
GARDE = re.compile(r"(?:style|template)\s*(?:n°\s*)?(\d+)", re.I)
# La musique de chaque style (section 8 « Le son » de sa fiche, qui les nomme) : ces ambiances passent
# devant celles du but de la vidéo, jamais devant une voix off sur une page (musiques.choisir).
AMBIANCES = {1: ["tech-minimale"], 2: ["lancement-energique", "montee-cinematique"],
             3: ["tech-minimale", "montee-cinematique"], 4: ["premium-calme", "montee-cinematique"],
             5: ["premium-calme", "tech-minimale"], 6: ["montee-cinematique"], 7: ["lancement-energique"],
             8: ["tech-minimale", "premium-calme"]}


def catalogue(racine: Path) -> list[dict]:
    """Les styles de l'index, dans l'ordre : [{n, nom, voit, dapres, utile, dossier, video, image}]
    (video et image : les fichiers de l'aperçu, qui peuvent manquer)."""
    index = racine / INDEX
    if not index.is_file():
        return []
    styles = []
    for ligne in index.read_text(encoding="utf-8").splitlines():
        m = LIGNE.match(ligne.strip())
        if m:
            dossier = m.group(6)
            styles.append({"n": int(m.group(1)), "nom": m.group(2).strip(), "voit": m.group(3).strip(),
                           "dapres": m.group(4).strip(), "utile": m.group(5).strip(), "dossier": dossier,
                           "video": racine / APERCUS / f"{dossier}.mp4", "image": racine / APERCUS / f"{dossier}.jpg"})
    return styles


def garde(racine: Path) -> int | None:
    """Le numéro du style gardé dans ses préférences (`studio.config.json`), sinon None."""
    try:
        conf = json.loads((racine / "studio.config.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    for p in conf.get("preferences") or []:
        m = GARDE.fullmatch(str(p).strip())
        if m:
            return int(m.group(1))
    return None


def ambiances(n: int | None) -> list[str]:
    """Les ambiances de musique du style n, de la plus juste à la moins juste ([] sans style)."""
    return list(AMBIANCES.get(n or 0, []))


def vitrine(racine: Path, conseil: int | None = None) -> list[dict]:
    """Les styles tels que la page les montre : [{numero, nom, detail, video, image, conseil}], les
    fichiers en adresses file:// (la page s'ouvre depuis le disque). `conseil` : le numéro conseillé."""
    sortie = []
    for s in catalogue(racine):
        sortie.append({"numero": s["n"], "nom": s["nom"], "detail": s["voit"],
                       "video": s["video"].resolve().as_uri() if s["video"].is_file() else "",
                       "image": s["image"].resolve().as_uri() if s["image"].is_file() else "",
                       "conseil": s["n"] == conseil})
    return sortie
