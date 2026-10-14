#!/usr/bin/env python3
"""PACK SFX : la bibliothèque de bruitages pro (produit vendu à part), rangée dans ce dossier.

Deux chemins, au choix du client :
    installer <pack-sfx.zip>          l'archive qu'il a achetée (son INSTALL.md vise Monteur IA :
                                      on ne le suit pas, on prend seulement les sons et leurs fiches) ;
    reprendre <dossier Monteur IA>    le pack déjà installé chez lui, lu sans rien y modifier.

Ce qui est copié, et rien d'autre :
    assets/sfx/pack/**                les sons, rangés par famille ;
    assets/sfx/catalog.json           la fiche de chaque son (rôle, usage, gain calibré, instant
                                      d'impact, prises) ;
    assets/sfx/sons-par-situation.md  la table « ce qui se passe à l'écran → le son ».
Ni ses outils ni son skill, écrits pour le montage des Reels de Monteur IA. Le pack n'est jamais
versionné (.gitignore) : il se réinstalle depuis l'archive du client.

Python 3.9+, bibliothèque standard seulement.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import unicodedata
import zipfile
from pathlib import Path

SONS = "assets/sfx/pack/"
FICHES = {
    "assets/sfx/catalog.json": "assets/sfx/catalog.json",
    ".claude/skills/pack-sfx/references/sons-par-situation.md": "assets/sfx/sons-par-situation.md",
}
EXTENSIONS_SON = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}
MANIFESTE = "assets/sfx/.pack-sfx-manifest.json"
CATALOGUE = "assets/sfx/catalog.json"


class ErreurPack(Exception):
    pass


def chemin_sur(nom: str) -> str | None:
    """Un chemin d'archive sans danger (relatif, sans « .. »), normalisé ; None sinon."""
    nom = nom.replace("\\", "/")
    if nom.startswith("/") or (len(nom) > 1 and nom[1] == ":"):
        return None
    propre = posixpath.normpath(nom)
    if propre.startswith("../") or propre == ".." or "/../" in f"/{propre}/":
        return None
    return propre


def selection(noms: list[str]) -> dict[str, str]:
    """Pour les fichiers d'une source (archive ou dossier) : {nom dans la source: chemin dans ce
    dossier}. Repère la racine du pack par son catalogue (« pack-sfx/assets/sfx/catalog.json »),
    garde les sons de assets/sfx/pack/ et les deux fiches, ignore tout le reste. Lève ErreurPack si
    ce n'est pas un Pack SFX."""
    surs = {n: chemin_sur(n) for n in noms if not n.endswith("/")}
    catalogues = sorted((p for p in surs.values() if p and (p == CATALOGUE or p.endswith("/" + CATALOGUE))), key=len)
    if not catalogues:
        raise ErreurPack("ce n'est pas un Pack SFX : aucun assets/sfx/catalog.json dedans")
    prefixe = catalogues[0][: -len(CATALOGUE)]
    choix = {}
    for brut, p in surs.items():
        if not p or not p.startswith(prefixe):
            continue
        rel = p[len(prefixe):]
        if rel in FICHES:
            choix[brut] = FICHES[rel]
        elif rel.startswith(SONS) and Path(rel).suffix.lower() in EXTENSIONS_SON and "/." not in "/" + rel:
            choix[brut] = rel
    if not any(v.startswith(SONS) for v in choix.values()):
        raise ErreurPack("ce Pack SFX ne contient aucun son (assets/sfx/pack/ vide)")
    return choix


def _empreinte(donnees: bytes) -> str:
    return hashlib.sha256(donnees).hexdigest()


def _ecrire(racine: Path, copies: dict[str, bytes], source: str) -> dict:
    """Écrit les fichiers choisis (un fichier identique n'est pas réécrit), retire ceux d'une version
    précédente du pack qui n'existent plus, puis vérifie que chaque son du catalogue est là."""
    ancien = {}
    try:
        ancien = json.loads((racine / MANIFESTE).read_text(encoding="utf-8")).get("fichiers") or {}
    except (OSError, ValueError):
        pass
    ecrits = identiques = 0
    for rel, donnees in copies.items():
        cible = racine / rel
        if cible.is_file() and cible.stat().st_size == len(donnees) and cible.read_bytes() == donnees:
            identiques += 1
            continue
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_bytes(donnees)
        ecrits += 1
    retires = 0
    for rel in ancien:
        if rel not in copies and rel.startswith(SONS) and (racine / rel).is_file():
            (racine / rel).unlink()
            retires += 1
    manifeste = {"source": source, "fichiers": {rel: _empreinte(d) for rel, d in sorted(copies.items())}}
    (racine / MANIFESTE).write_text(json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    e = etat(racine)
    if e["manquants"]:
        raise ErreurPack(f"pack incomplet : {len(e['manquants'])} son(s) du catalogue absents "
                         f"(ex. {', '.join(e['manquants'][:3])}) ; l'archive est peut-être abîmée, retélécharge-la")
    return {**e, "ecrits": ecrits, "identiques": identiques, "retires": retires}


def installer_depuis_zip(racine: Path, archive: Path) -> dict:
    archive = Path(archive).expanduser()
    if not archive.is_file():
        raise ErreurPack(f"archive introuvable : {archive}")
    try:
        with zipfile.ZipFile(archive) as z:
            choix = selection(z.namelist())
            copies = {rel: z.read(nom) for nom, rel in choix.items()}
    except zipfile.BadZipFile as e:
        raise ErreurPack(f"{archive.name} n'est pas une archive ZIP lisible ({e})") from e
    return _ecrire(racine, copies, f"archive {archive.name}")


def reprendre_depuis_monteur(racine: Path, dossier: Path) -> dict:
    """Copie le pack installé dans un dossier Monteur IA. Lit seulement : rien n'y est écrit."""
    dossier = Path(dossier).expanduser().resolve()
    if not (dossier / "templates" / "AGENT.md.tpl").is_file():
        raise ErreurPack(f"{dossier} n'est pas un dossier Monteur IA (templates/AGENT.md.tpl manque)")
    if not (dossier / CATALOGUE).is_file() or not (dossier / SONS).is_dir():
        raise ErreurPack("pas de Pack SFX dans ce dossier Monteur IA (assets/sfx/pack/ ou assets/sfx/catalog.json manque)")
    noms = [p.relative_to(dossier).as_posix() for p in (dossier / "assets" / "sfx").rglob("*") if p.is_file()]
    noms += [p.relative_to(dossier).as_posix() for p in (dossier / ".claude" / "skills" / "pack-sfx").rglob("*") if p.is_file()]
    choix = selection(noms)
    copies = {rel: (dossier / nom).read_bytes() for nom, rel in choix.items()}
    return _ecrire(racine, copies, f"dossier Monteur IA {dossier}")


def catalogue(racine: Path) -> dict:
    try:
        return json.loads((racine / CATALOGUE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def etat(racine: Path) -> dict:
    """Combien de sons pro du catalogue sont présents (le pack est optionnel)."""
    c = catalogue(racine)
    attendus = [s for s in c.get("sounds") or [] if s.get("source") == "pack"]
    manquants = [s["file"] for s in attendus if not (racine / "assets" / "sfx" / s["file"]).is_file()]
    return {"installe": bool(attendus) and not manquants, "presents": len(attendus) - len(manquants),
            "attendus": len(attendus), "version": c.get("version"), "manquants": manquants}


def _plat(texte: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", str(texte).lower()) if unicodedata.category(c) != "Mn")


def chercher(racine: Path, mots: list[str], limite: int = 15) -> list[dict]:
    """Les sons du catalogue (pack et sons de démarrage) dont la fiche contient tous les mots."""
    voulus = [_plat(w) for m in mots for w in m.split()]  # « whoosh simple » vaut deux mots
    trouves = []
    for s in catalogue(racine).get("sounds") or []:
        texte = _plat(" ".join(str(s.get(k) or "") for k in ("id", "name", "category", "role", "usage", "tags")))
        if all(m in texte for m in voulus) and (racine / "assets" / "sfx" / s["file"]).is_file():
            trouves.append(s)
    return trouves[:limite]


def ligne(s: dict) -> str:
    """Une ligne lisible par l'agent : le chemin vu d'un projet de vidéo et les réglages du son."""
    prises = f", {len(s['segments'])} prises (trim)" if s.get("segments") else ""
    return (f"{s['id']} : ../../../assets/sfx/{s['file']} · {s.get('role')} · gain {s.get('gain_db')} dB · "
            f"impact {s.get('hit')} s ({s.get('align')}) · {s.get('duration')} s{prises} · {s.get('usage', '')}")

