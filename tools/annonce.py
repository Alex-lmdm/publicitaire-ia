#!/usr/bin/env python3
"""ANNONCE : l'outil de l'extension d'annonces de lancement de Monteur IA.

Le skill `annonce` décide quoi montrer ; cet outil fait le travail mécanique et vérifiable,
pour que rien ne dépende de la mémoire de l'agent : dossiers des vidéos, fiche de l'offre,
zones de sécurité Instagram, temps de lecture, planche de contrôle, son, couverture, export.

Usage (depuis le dossier Monteur IA, ou depuis n'importe quel projet d'annonce) :
    python3 tools/annonce.py verifier
    python3 tools/annonce.py nouvelle "<sujet>" --videos reel,teaser,ouvert,dernier-jour [--ouvrir]
    python3 tools/annonce.py offre <dossier de l'annonce>
    python3 tools/annonce.py lecture "<texte affiché à l'écran>"
    python3 tools/annonce.py zones reel|story
    python3 tools/annonce.py planche <video.mp4> [--format reel|story] [--temps 0.5,2,4.2]
    python3 tools/annonce.py son <video.mp4>
    python3 tools/annonce.py mastering <entree.mp4> <sortie.mp4>
    python3 tools/annonce.py sans-musique <projet>            # prépare la version sans musique
    python3 tools/annonce.py couverture <video.mp4> <image.jpg> <sortie.mp4>
    python3 tools/annonce.py export <video.mp4> --format reel|story
    python3 tools/annonce.py livrer <dossier de l'annonce>

Python 3.9+ et la bibliothèque standard seulement. FFmpeg et ffprobe sont ceux de Monteur IA.
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Windows : une sortie redirigée est en cp1252, et un « ✅ » y ferait planter l'outil.
for _flux in (sys.stdout, sys.stderr):
    try:
        _flux.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

VERSION = "0.1.0"
OUTILS = Path(__file__).resolve().parent
LARGEUR, HAUTEUR, FPS = 1080, 1920, 30

# ---------------------------------------------------------------------------
# Les vidéos d'une annonce
# ---------------------------------------------------------------------------
# Chaque type porte son format, sa durée cible et sa place dans le lancement. Les durées sont
# des bornes de fabrication : une vidéo plus courte que son minimum ne laisse pas lire son texte.
VIDEOS: dict[str, dict] = {
    "reel": {"format": "reel", "nom": "Reel", "min": 15, "cible": 20, "max": 30,
             "quand": "le jour J, en premier"},
    "nouveaute": {"format": "reel", "nom": "Reel nouveauté", "min": 10, "cible": 14, "max": 20,
                  "quand": "le jour de la sortie"},
    "teaser": {"format": "story", "nom": "Story teaser", "min": 5, "cible": 7, "max": 10,
               "quand": "la veille"},
    "ouvert": {"format": "story", "nom": "Story ouverture", "min": 6, "cible": 8, "max": 12,
               "quand": "le jour J, juste après le Reel", "sticker": True},
    "dernier-jour": {"format": "story", "nom": "Story dernier jour", "min": 6, "cible": 8, "max": 12,
                     "quand": "le dernier jour, le matin", "sticker": True, "exige_fermeture": True},
    "relance": {"format": "story", "nom": "Story relance", "min": 5, "cible": 7, "max": 10,
                "quand": "au milieu du lancement", "sticker": True},
    "story": {"format": "story", "nom": "Story", "min": 5, "cible": 7, "max": 12,
              "quand": "le jour de la sortie", "sticker": True},
}

# ---------------------------------------------------------------------------
# Zones de sécurité (1080 × 1920). Ce que l'interface d'Instagram recouvre, plus une marge.
# Texte important et prix : toujours DANS la zone « texte ». Valeurs v0.1, à recaler sur un
# vrai téléphone (le skill le rappelle) ; la règle la plus stricte des sources a été retenue.
# ---------------------------------------------------------------------------
ZONES: dict[str, dict] = {
    # Reel : en haut le titre « Reels » et la caméra, en bas le pseudo, la légende et le son,
    # à droite la colonne J'aime / commentaire / partage.
    "reel": {"haut": 300, "bas": 480, "gauche": 100, "droite": 150},
    # Story : en haut la barre de progression et le profil, en bas « Envoyer un message ».
    "story": {"haut": 270, "bas": 290, "gauche": 80, "droite": 80},
}
# Story avec lien : bande réservée au sticker lien, que le client posera dans Instagram.
STICKER = {"x": 190, "y": 1180, "largeur": 700, "hauteur": 240}


def zone_texte(fmt: str) -> dict:
    """Le rectangle où tout texte important doit tenir, en pixels (x, y, largeur, hauteur)."""
    z = ZONES[fmt]
    return {"x": z["gauche"], "y": z["haut"],
            "largeur": LARGEUR - z["gauche"] - z["droite"], "hauteur": HAUTEUR - z["haut"] - z["bas"]}


def chevauche(a: dict, b: dict) -> bool:
    return not (a["x"] + a["largeur"] <= b["x"] or b["x"] + b["largeur"] <= a["x"]
                or a["y"] + a["hauteur"] <= b["y"] or b["y"] + b["hauteur"] <= a["y"])


def dans(a: dict, b: dict) -> bool:
    """Vrai si le rectangle a tient entièrement dans b."""
    return (a["x"] >= b["x"] and a["y"] >= b["y"] and a["x"] + a["largeur"] <= b["x"] + b["largeur"]
            and a["y"] + a["hauteur"] <= b["y"] + b["hauteur"])


# ---------------------------------------------------------------------------
# Temps de lecture : la règle la plus stricte des sources étudiées
# ---------------------------------------------------------------------------
PAR_MOT, ASSISE, PLANCHER, FINAL = 0.35, 0.3, 1.2, 2.5


def mots(texte: str) -> int:
    return len([m for m in re.split(r"\s+", texte.strip()) if re.search(r"\w", m)])


def lecture(texte: str, final: bool = False) -> float:
    """Durée minimale (s) pendant laquelle un texte doit rester immobile et lisible.

    0,35 s par mot + 0,3 s d'assise, jamais moins de 1,2 s ; l'écran final (appel à l'action)
    reste au moins 2,5 s. Arrondi au dixième supérieur."""
    n = mots(texte)
    if n == 0:
        return 0.0
    duree = max(PLANCHER, n * PAR_MOT + ASSISE)
    if final:
        duree = max(duree, FINAL)
    return math.ceil(duree * 10 - 1e-9) / 10


# ---------------------------------------------------------------------------
# La fiche de l'offre : tout ce que les vidéos auront le droit d'affirmer
# ---------------------------------------------------------------------------
FICHE_VIDE = {
    "produit": "",
    "lien": "",
    "type": "lancement",
    "promesse": {"texte": "", "source": ""},
    "recoit": [],
    "prix": {"montant": None, "devise": "EUR", "barre": None, "source": ""},
    "bonus": [],
    "dates": {"ouverture": None, "fermeture": None, "source": ""},
    "preuves": [],
    "cta": {"mot_cle": "", "phrase": "", "source": ""},
    "interdits": [],
}
TYPES = {"lancement", "nouveaute", "relance", "dernier-jour"}
PROMESSE_MAX_MOTS = 9
PREUVES = {"chiffre", "temoignage", "resultat", "media"}


def _source(element: dict) -> str:
    return str(element.get("source") or "").strip()


def verifier_fiche(fiche: dict, videos: list[str] | None = None) -> list[str]:
    """Les problèmes de la fiche OFFRE.json, en français. Liste vide = la fiche est utilisable.

    Règle de fond : chaque fait affiché porte sa source (une adresse, « page », « client » s'il l'a
    dit lui-même, ou le nom d'un fichier de sources/). Ce qui n'a pas de source n'existe pas."""
    pb: list[str] = []
    if not str(fiche.get("produit") or "").strip():
        pb.append("produit : le nom de ce qui est annoncé manque.")
    if fiche.get("type") not in TYPES:
        pb.append(f"type : « {fiche.get('type')} » inconnu (attendu : {', '.join(sorted(TYPES))}).")
    promesse = fiche.get("promesse") or {}
    if not str(promesse.get("texte") or "").strip():
        pb.append("promesse : la phrase centrale manque (reprise du titre de la page).")
    else:
        if mots(promesse["texte"]) > PROMESSE_MAX_MOTS:
            pb.append(f"promesse : {mots(promesse['texte'])} mots, {PROMESSE_MAX_MOTS} au plus à l'écran.")
        if not _source(promesse):
            pb.append("promesse : sans source.")
    for i, item in enumerate(fiche.get("recoit") or []):
        if not isinstance(item, dict) or not str(item.get("texte") or "").strip():
            pb.append(f"recoit[{i}] : texte manquant.")
        elif not _source(item):
            pb.append(f"recoit[{i}] « {item['texte'][:40]} » : sans source.")
    prix = fiche.get("prix") or {}
    if prix.get("montant") is not None:
        if not isinstance(prix["montant"], (int, float)) or prix["montant"] < 0:
            pb.append("prix.montant : un nombre positif est attendu.")
        if not _source(prix):
            pb.append("prix : sans source.")
        if prix.get("barre") is not None and (not isinstance(prix["barre"], (int, float)) or prix["barre"] <= prix["montant"]):
            pb.append("prix.barre : un prix barré doit être un vrai prix plus élevé, affiché sur la page.")
    for i, b in enumerate(fiche.get("bonus") or []):
        if not isinstance(b, dict) or not str(b.get("texte") or "").strip():
            pb.append(f"bonus[{i}] : texte manquant.")
        elif not _source(b):
            pb.append(f"bonus[{i}] « {b['texte'][:40]} » : sans source.")
    dates = fiche.get("dates") or {}
    for cle in ("ouverture", "fermeture"):
        valeur = dates.get(cle)
        if valeur:
            try:
                datetime.datetime.fromisoformat(str(valeur))
            except ValueError:
                pb.append(f"dates.{cle} : « {valeur} » n'est pas une date AAAA-MM-JJ[THH:MM].")
    if (dates.get("ouverture") or dates.get("fermeture")) and not _source(dates):
        pb.append("dates : sans source.")
    if dates.get("ouverture") and dates.get("fermeture"):
        try:
            if datetime.datetime.fromisoformat(str(dates["fermeture"])) <= datetime.datetime.fromisoformat(str(dates["ouverture"])):
                pb.append("dates : la fermeture doit suivre l'ouverture.")
        except ValueError:
            pass
    for i, p in enumerate(fiche.get("preuves") or []):
        if not isinstance(p, dict) or not str(p.get("texte") or "").strip():
            pb.append(f"preuves[{i}] : texte manquant.")
            continue
        if p.get("type") not in PREUVES:
            pb.append(f"preuves[{i}] : type « {p.get('type')} » inconnu ({', '.join(sorted(PREUVES))}).")
        if not _source(p):
            pb.append(f"preuves[{i}] « {p['texte'][:40]} » : sans source, donc inutilisable.")
        if p.get("type") == "temoignage" and not p.get("mot_pour_mot"):
            pb.append(f"preuves[{i}] : un témoignage se cite mot pour mot (`mot_pour_mot: true`).")
    cta = fiche.get("cta") or {}
    if not str(cta.get("mot_cle") or "").strip() and not str(cta.get("phrase") or "").strip():
        pb.append("cta : ni mot-clé ni phrase d'appel à l'action.")
    if cta.get("mot_cle") and not re.fullmatch(r"[A-ZÀ-ÖØ-Þ0-9]{2,20}", str(cta["mot_cle"])):
        pb.append("cta.mot_cle : un seul mot en MAJUSCULES, sans espace (ex. FORMATION).")
    for video in videos or []:
        if VIDEOS.get(video, {}).get("exige_fermeture") and not dates.get("fermeture"):
            pb.append(f"{video} : pas de date de fermeture sur la page, donc pas de story « dernier jour ».")
    return pb


# ---------------------------------------------------------------------------
# Les lieux : le dossier Monteur IA et les annonces
# ---------------------------------------------------------------------------
INTERDITS_NOM = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def propre(texte: str, longueur: int = 40) -> str:
    texte = re.sub(r"\s+", " ", INTERDITS_NOM.sub("-", str(texte))).strip(" .-")
    return texte[:longueur].rstrip(" .-")


def maison_de(depart: Path) -> Path | None:
    """Le dossier Monteur IA qui contient `depart` : celui qui porte templates/AGENT.md.tpl."""
    p = Path(depart).resolve()
    for d in (p, *p.parents):
        if (d / "templates" / "AGENT.md.tpl").is_file():
            return d
    return None


def maison() -> Path:
    m = maison_de(OUTILS) or maison_de(Path.cwd())
    if m is None:
        sys.exit("ERREUR : je ne trouve pas le dossier Monteur IA (il contient templates/AGENT.md.tpl). "
                 "Ouvre ton assistant dans ton dossier Monteur IA et relance.")
    return m


def config(m: Path) -> dict:
    for nom in ("brand.config.json", "brand.config.example.json"):
        f = m / nom
        if f.is_file():
            try:
                return json.loads(f.read_text(encoding="utf-8"))
            except ValueError:
                return {}
    return {}


def binaire(m: Path | None, nom: str) -> str | None:
    """ffmpeg / ffprobe : celui des réglages de Monteur IA, sinon celui du PATH, sinon Homebrew."""
    if m is not None:
        chemin = ((config(m).get("env") or {}).get("ffmpegPath") or "").strip()
        if chemin:
            candidat = Path(chemin).with_name(nom) if nom != "ffmpeg" else Path(chemin)
            if candidat.exists():
                return str(candidat)
    trouve = shutil.which(nom)
    if trouve:
        return trouve
    for dossier in ("/opt/homebrew/bin", "/usr/local/bin"):
        if (Path(dossier) / nom).exists():
            return str(Path(dossier) / nom)
    return None


def lancer(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace", **kw)


# ---------------------------------------------------------------------------
# Commandes
# ---------------------------------------------------------------------------
def cmd_verifier(_a) -> None:
    m = maison()
    lignes = []
    ok = True
    for nom, present in (
        ("dossier Monteur IA", True),
        ("skill annonce", (m / ".claude" / "skills" / "annonce" / "SKILL.md").is_file()),
        ("aiguillage dans les instructions", "BEGIN EXTENSION: annonce" in (m / "templates" / "AGENT.md.tpl").read_text(encoding="utf-8")),
        ("style de la marque (brand/)", (m / "brand" / "tokens.css").is_file()),
        ("HyperFrames", (m / "node_modules" / ".bin" / "hyperframes").exists() or shutil.which("hyperframes") is not None),
        ("ffmpeg", binaire(m, "ffmpeg") is not None),
        ("ffprobe", binaire(m, "ffprobe") is not None),
        ("Node", shutil.which("node") is not None),
    ):
        lignes.append(f"{'✅' if present else '❌'} {nom}")
        ok = ok and present
    print("\n".join(lignes))
    print("ok" if ok else "à corriger")
    if not ok:
        sys.exit(1)


def _copier_style(m: Path, projet: Path) -> None:
    """Le rendu ne voit que le dossier du projet : on y copie le style, les polices et GSAP."""
    for sous in ("brand", "assets/vendor", "assets/fonts"):
        src = m / sous
        if src.is_dir():
            shutil.copytree(src, projet / sous, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("atoms.html", "BRAND.md", "*.ttf", ".DS_Store"))


def _instructions(gabarit: str, **valeurs: str) -> str:
    for cle, val in valeurs.items():
        gabarit = gabarit.replace("{{" + cle + "}}", val)
    return gabarit


def creer_annonce(m: Path, sujet: str, videos: list[str], date: str) -> Path:
    """annonces/<sujet> · <date>/ : la fiche, le plan, les sources, la livraison, et un projet de
    l'app HyperFrames par vidéo. Une annonce existante n'est jamais écrasée."""
    inconnues = [v for v in videos if v not in VIDEOS]
    if inconnues:
        sys.exit(f"ERREUR : vidéo inconnue : {', '.join(inconnues)} (possibles : {', '.join(VIDEOS)}).")
    base = m / "annonces" / " · ".join(p for p in (propre(sujet), date) if p)
    dossier, n = base, 2
    while dossier.exists():
        dossier, n = base.with_name(f"{base.name} ({n})"), n + 1
    for sous in ("sources", "livraison"):
        (dossier / sous).mkdir(parents=True, exist_ok=True)
    fiche = dict(FICHE_VIDE, produit=sujet)
    (dossier / "OFFRE.json").write_text(json.dumps(fiche, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dossier / "PLAN.md").write_text(
        f"# Annonce : {sujet}\n\nCréée le {date}. Vidéos : {', '.join(VIDEOS[v]['nom'] for v in videos)}.\n\n"
        "## Angle retenu\n\n(à remplir après le choix du client)\n\n## Vidéos\n\n"
        + "".join(f"### {VIDEOS[v]['nom']} ({VIDEOS[v]['cible']} s, {VIDEOS[v]['quand']})\n\n"
                  "| Temps | À l'écran (texte exact) | Clé de OFFRE.json | Mouvement | Son |\n|---|---|---|---|---|\n\n"
                  for v in videos),
        encoding="utf-8")
    gabarit_md = (OUTILS.parent / "templates" / "projet" / "CLAUDE.md.tpl")
    gabarit_html = (OUTILS.parent / "templates" / "projet" / "index.html.tpl")
    if not gabarit_md.is_file():  # outil copié dans le dossier Monteur IA : gabarits rangés à côté
        gabarit_md = m / "templates" / "annonce" / "CLAUDE.md.tpl"
        gabarit_html = m / "templates" / "annonce" / "index.html.tpl"
    maintenant = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    for v in videos:
        spec = VIDEOS[v]
        projet = dossier / propre(f"{sujet} · {spec['nom']}", 60)
        projet.mkdir(parents=True)
        for sous in ("assets/images", "assets/audio", "exports", "work"):
            (projet / sous).mkdir(parents=True, exist_ok=True)
        _copier_style(m, projet)
        if (m / "hyperframes.json").is_file():
            shutil.copy2(m / "hyperframes.json", projet / "hyperframes.json")
        valeurs = {"SUJET": sujet, "VIDEO": v, "VIDEO_NOM": spec["nom"], "FORMAT": spec["format"],
                   "DUREE": str(spec["cible"]), "DUREE_MIN": str(spec["min"]), "DUREE_MAX": str(spec["max"]),
                   "MAISON": "../../../", "ANNONCE": "../"}
        if gabarit_html.is_file():
            (projet / "index.html").write_text(_instructions(gabarit_html.read_text(encoding="utf-8"), **valeurs), encoding="utf-8")
        if gabarit_md.is_file():
            texte = _instructions(gabarit_md.read_text(encoding="utf-8"), **valeurs)
            (projet / "CLAUDE.md").write_text(texte, encoding="utf-8")
            (projet / "AGENTS.md").write_text(texte, encoding="utf-8")
        meta = {"id": projet.name, "name": projet.name, "createdAt": maintenant,
                "monteurIa": {"lieu": "annonce", "video": v, "format": spec["format"], "sujet": sujet, "date": date}}
        (projet / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paquet = {"name": f"annonce-{v}", "private": True, "type": "module",
                  "scripts": {"dev": "hyperframes preview", "check": "hyperframes check",
                              "render": f"hyperframes render -o exports/{v}.mp4"}}
        (projet / "package.json").write_text(json.dumps(paquet, indent=2) + "\n", encoding="utf-8")
    return dossier


def cmd_nouvelle(a) -> None:
    m = maison()
    if not propre(a.sujet):
        sys.exit("ERREUR : donne un sujet à l'annonce, en quelques mots.")
    videos = [v.strip() for v in a.videos.split(",") if v.strip()]
    dossier = creer_annonce(m, a.sujet, videos, a.date)
    print(f"• annonce créée : {dossier.relative_to(m)}")
    for projet in sorted(p for p in dossier.iterdir() if (p / "meta.json").is_file()):
        print(f"  - {projet.name}")
    print("• à remplir d'abord : OFFRE.json (puis `annonce.py offre`), puis PLAN.md")
    if a.ouvrir:
        ouvreur = m / "scripts" / "app-hyperframes.mjs"
        for projet in sorted(p for p in dossier.iterdir() if (p / "meta.json").is_file()):
            if ouvreur.is_file():
                lancer(["node", str(ouvreur), "ouvrir", str(projet)], cwd=m)
        print("• projets ouverts dans l'app HyperFrames")


def _dossier_annonce(chemin: Path) -> Path:
    p = Path(chemin).resolve()
    for d in (p, *p.parents):
        if (d / "OFFRE.json").is_file():
            return d
    sys.exit(f"ERREUR : aucun OFFRE.json dans {p} ni au-dessus. Donne le dossier de l'annonce.")


def cmd_offre(a) -> None:
    dossier = _dossier_annonce(Path(a.dossier))
    fiche = json.loads((dossier / "OFFRE.json").read_text(encoding="utf-8"))
    videos = [json.loads((p / "meta.json").read_text(encoding="utf-8"))["monteurIa"]["video"]
              for p in dossier.iterdir() if (p / "meta.json").is_file()]
    pb = verifier_fiche(fiche, videos)
    if pb:
        print("\n".join(f"❌ {p}" for p in pb))
        sys.exit(1)
    print("ok : chaque fait de la fiche a sa source")


def cmd_lecture(a) -> None:
    print(f"{lecture(a.texte, final=a.final):.1f} s minimum à l'écran ({mots(a.texte)} mots)")


def cmd_zones(a) -> None:
    z = zone_texte(a.format)
    print(json.dumps({"format": a.format, "taille": [LARGEUR, HAUTEUR], "marges": ZONES[a.format],
                      "zone_texte": z, "sticker_lien": STICKER if a.format == "story" else None},
                     ensure_ascii=False, indent=2))


def _duree(ffprobe: str, video: Path) -> float:
    r = lancer([ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(video)])
    try:
        return float(r.stdout.strip())
    except ValueError:
        sys.exit(f"ERREUR : impossible de lire la durée de {video}.")


def instants_planche(duree: float, temps: list[float] | None, pas: float = 1.0) -> list[float]:
    """Les instants de la planche : ceux demandés (repères + 0,3 s), sinon un par seconde, plus
    toujours la dernière image. Bornés à la durée de la vidéo, sans doublon, triés."""
    base = temps if temps else [round(i * pas + 0.3, 2) for i in range(int(duree // pas) + 1)]
    # Deux images avant la fin, arrondi vers le bas : un instant au-delà de la dernière image
    # (7,97 s pour une vidéo de 8 s à 30 images/s) ne rend rien.
    fin = max(0.0, math.floor((duree - 2 / FPS) * 100) / 100)
    vus = sorted({round(min(max(0.0, t), fin), 2) for t in base} | {fin})
    return vus


def cmd_planche(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg, ffprobe = binaire(m, "ffmpeg"), binaire(m, "ffprobe")
    if not ffmpeg or not ffprobe:
        sys.exit("ERREUR : ffmpeg introuvable.")
    video = Path(a.video).resolve()
    temps = [float(t) for t in a.temps.split(",")] if a.temps else None
    instants = instants_planche(_duree(ffprobe, video), temps)
    sortie = Path(a.sortie) if a.sortie else video.with_name(video.stem + "-planche.jpg")
    travail = sortie.with_suffix("")
    travail.mkdir(parents=True, exist_ok=True)
    z = zone_texte(a.format)
    boites = [f"drawbox=x={z['x']}:y={z['y']}:w={z['largeur']}:h={z['hauteur']}:color=0x00ff88@0.9:t=4"]
    if a.format == "story" and a.sticker:
        boites.append(f"drawbox=x={STICKER['x']}:y={STICKER['y']}:w={STICKER['largeur']}:h={STICKER['hauteur']}:color=0xff3366@0.9:t=6")
    vignettes = []
    for i, t in enumerate(instants):
        img = travail / f"{i:03d}.jpg"
        filtres = ",".join(boites + [f"drawtext=text='{t:.2f} s':x=24:y=24:fontsize=54:fontcolor=white:box=1:boxcolor=black@0.6",
                                     "scale=360:-2"])
        r = lancer([ffmpeg, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-vf", filtres, str(img)])
        if r.returncode != 0:  # drawtext absent de certaines compilations : sans l'heure, tant pis
            filtres = ",".join(boites + ["scale=360:-2"])
            r = lancer([ffmpeg, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-vf", filtres, str(img)])
        if (r.returncode != 0 or not img.is_file()) and t >= instants[-1]:
            # Dernière image : on la prend depuis la fin du fichier.
            r = lancer([ffmpeg, "-v", "error", "-y", "-sseof", "-0.1", "-i", str(video), "-update", "1",
                        "-vf", ",".join(boites + ["scale=360:-2"]), str(img)])
        if r.returncode == 0 and img.is_file():
            vignettes.append(img)
        else:
            print(f"⚠️ image à {t:.2f} s non extraite")
    if not vignettes:
        sys.exit("ERREUR : aucune image extraite.")
    colonnes = min(6, len(vignettes))
    lignes = math.ceil(len(vignettes) / colonnes)
    r = lancer([ffmpeg, "-v", "error", "-y", "-framerate", "1", "-i", str(travail / "%03d.jpg"),
                "-vf", f"tile={colonnes}x{lignes}:padding=8:margin=8:color=0x202022", "-frames:v", "1", str(sortie)])
    if r.returncode != 0:
        sys.exit(f"ERREUR : planche impossible : {r.stderr[-400:]}")
    shutil.rmtree(travail, ignore_errors=True)
    print(f"• planche : {sortie} ({len(vignettes)} images : {', '.join(f'{t:.2f}' for t in instants)} s)")
    print("  vert = zone texte (rien d'important dehors)" + (", rouge = sticker lien (rien dedans)" if a.format == "story" and a.sticker else ""))


# Même niveau que les Reels de Monteur IA (tools/sons.py) : -16 LUFS, celui du fil Instagram ;
# plafond -1,5 dB pour garder les crêtes sous -1 dBTP une fois la vidéo encodée.
CIBLE_LUFS, CIBLE_TP, PLAFOND_TP = -16.0, -1.5, -1.0


def mesure_sonore(ffmpeg: str, video: Path) -> dict | None:
    r = lancer([ffmpeg, "-hide_banner", "-nostats", "-i", str(video), "-af",
                f"loudnorm=I={CIBLE_LUFS}:TP={CIBLE_TP}:LRA=11:print_format=json", "-f", "null", "-"])
    bloc = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S)
    if not bloc:
        return None
    return json.loads(bloc.group(0))


def verdict_sonore(mesure: dict) -> list[str]:
    """Écarts à la cible de livraison : -16 LUFS (±1) et crête vraie sous -1 dBTP."""
    pb = []
    try:
        i, tp = float(mesure["input_i"]), float(mesure["input_tp"])
    except (KeyError, ValueError):
        return ["mesure illisible"]
    if math.isinf(i) or i < -60:
        return ["vidéo muette (aucun son mesurable)"]
    if abs(i - CIBLE_LUFS) > 1.0:
        pb.append(f"sonie {i:.1f} LUFS, cible {CIBLE_LUFS:.0f} ±1 : lance `annonce.py mastering`")
    if tp > PLAFOND_TP:
        pb.append(f"crête {tp:.1f} dBTP au-dessus de {PLAFOND_TP:.0f} : risque de saturation sur téléphone")
    return pb


def cmd_son(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    mesure = mesure_sonore(ffmpeg, Path(a.video))
    if mesure is None:
        print("ℹ️ pas de piste son : version muette (normal pour une story sans musique)")
        return
    pb = verdict_sonore(mesure)
    print(f"sonie {float(mesure['input_i']):.1f} LUFS, crête {float(mesure['input_tp']):.1f} dBTP")
    print("\n".join(f"❌ {p}" for p in pb) if pb else "ok")


def chaine_mastering(gain_db: float) -> str:
    """Gain puis limiteur suréchantillonné : le niveau monte, les crêtes restent sous -2 dBFS, donc
    sous -1 dBTP une fois encodées en AAC. Un loudnorm seul refuse de monter un clip court aux sons
    piqués (il protège ses crêtes) et s'arrête 2 à 3 LU sous la cible."""
    return (f"aresample=192000,volume={gain_db:.2f}dB,"
            "alimiter=limit=0.79:attack=3:release=60:level=false,aresample=48000")


def cmd_mastering(a) -> None:
    m = maison_de(Path(a.entree)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    mesure = mesure_sonore(ffmpeg, Path(a.entree))
    if mesure is None or math.isinf(float(mesure["input_i"])):
        sys.exit("ERREUR : pas de son à masteriser (vidéo muette).")
    gain = CIBLE_LUFS - float(mesure["input_i"])
    apres = None
    for _ in range(4):  # chaque passe corrige l'écart de la précédente ; deux suffisent d'habitude
        r = lancer([ffmpeg, "-v", "error", "-y", "-i", a.entree, "-c:v", "copy", "-af", chaine_mastering(gain),
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.sortie])
        if r.returncode != 0:
            sys.exit(f"ERREUR : mastering impossible : {r.stderr[-400:]}")
        apres = mesure_sonore(ffmpeg, Path(a.sortie))
        if apres is None:
            break
        ecart = CIBLE_LUFS - float(apres["input_i"])
        if abs(ecart) <= 0.5:
            break
        gain += ecart
    if apres:
        print(f"• {a.sortie} : {float(apres['input_i']):.1f} LUFS, crête {float(apres['input_tp']):.1f} dBTP")
        pb = verdict_sonore(apres)
        if pb:
            print("\n".join(f"❌ {p}" for p in pb))
            sys.exit(1)
    else:
        print(f"• {a.sortie}")


def sans_musique_html(html: str) -> tuple[str, int]:
    """Retire du master la musique de fond (`id="musique"`, posé par tools/sons.py de Monteur IA, ou
    `data-role="musique"` posé à la main), pour la version que le client habillera d'un son
    Instagram. Les bruitages restent."""
    motif = re.compile(r'\s*<audio\b[^>]*(?:\bid="musique"|data-role="musique")[^>]*>(?:\s*</audio>)?', re.I)
    return motif.subn("", html)


def cmd_sans_musique(a) -> None:
    projet = Path(a.projet).resolve()
    index = projet / "index.html"
    if not index.is_file():
        sys.exit(f"ERREUR : {projet} n'a pas d'index.html.")
    html, n = sans_musique_html(index.read_text(encoding="utf-8"))
    if n == 0:
        sys.exit("ERREUR : aucune piste de musique (id=\"musique\") dans index.html : rien à retirer.")
    # À côté d'index.html : ses chemins (assets/, brand/) restent valides au rendu.
    cible = projet / "index-sans-musique.html"
    cible.write_text(html, encoding="utf-8")
    video = (json.loads((projet / "meta.json").read_text(encoding="utf-8")).get("monteurIa") or {}).get("video", "reel") \
        if (projet / "meta.json").is_file() else "reel"
    print(f"• {cible.name} prêt ({n} piste(s) de musique retirée(s)). Rendu :")
    print(f"  npx hyperframes render -c {cible.name} -o exports/{video}-sans-musique.mp4")


def cmd_couverture(a) -> None:
    """La couverture devient la toute première image : les aperçus (X, WhatsApp, Instagram avant
    lecture) montrent alors la bonne image. Une seule image remplacée, son conservé."""
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    r = lancer([ffmpeg, "-v", "error", "-y", "-i", a.video, "-i", a.image, "-filter_complex",
                f"[1:v]scale={LARGEUR}:{HAUTEUR}:force_original_aspect_ratio=increase,crop={LARGEUR}:{HAUTEUR}[c];"
                "[0:v][c]overlay=0:0:enable='eq(n,0)'[v]",
                "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16",
                "-preset", "slow", "-c:a", "copy", "-movflags", "+faststart", a.sortie])
    if r.returncode != 0:
        sys.exit(f"ERREUR : couverture impossible : {r.stderr[-400:]}")
    print(f"• {a.sortie} : la couverture est la première image")


def debut_rapide(chemin: Path) -> bool | None:
    """Vrai si l'index (moov) précède les données (mdat) : la vidéo démarre avant d'être chargée."""
    try:
        with open(chemin, "rb") as f:
            entete = f.read(4 * 1024 * 1024)
    except OSError:
        return None
    moov, mdat = entete.find(b"moov"), entete.find(b"mdat")
    if moov == -1 and mdat == -1:
        return None
    return moov != -1 and (mdat == -1 or moov < mdat)


def verdict_export(info: dict, fmt: str, video: str | None = None) -> list[str]:
    """Les écarts d'un fichier exporté aux attentes d'Instagram (ffprobe -show_streams -show_format)."""
    pb = []
    flux = info.get("streams") or []
    v = next((s for s in flux if s.get("codec_type") == "video"), None)
    if not v:
        return ["aucune piste vidéo"]
    if (v.get("width"), v.get("height")) != (LARGEUR, HAUTEUR):
        pb.append(f"taille {v.get('width')}×{v.get('height')}, attendu {LARGEUR}×{HAUTEUR}")
    if v.get("codec_name") != "h264":
        pb.append(f"codec {v.get('codec_name')}, attendu h264")
    if v.get("pix_fmt") != "yuv420p":
        pb.append(f"pixels {v.get('pix_fmt')}, attendu yuv420p (sinon couleurs fausses sur iPhone)")
    try:
        num, den = (int(x) for x in str(v.get("r_frame_rate", "0/1")).split("/"))
        if den and abs(num / den - FPS) > 0.5:
            pb.append(f"{num / den:.2f} images/s, attendu {FPS}")
    except ValueError:
        pass
    a = next((s for s in flux if s.get("codec_type") == "audio"), None)
    if a and a.get("codec_name") != "aac":
        pb.append(f"son {a.get('codec_name')}, attendu aac")
    try:
        duree = float((info.get("format") or {}).get("duration"))
    except (TypeError, ValueError):
        duree = None
    if video and duree is not None:
        spec = VIDEOS.get(video)
        if spec and not (spec["min"] - 0.5 <= duree <= spec["max"] + 0.5):
            pb.append(f"durée {duree:.1f} s hors de {spec['min']}–{spec['max']} s pour « {spec['nom']} »")
    elif duree is not None and fmt == "story" and duree > 60:
        pb.append(f"durée {duree:.1f} s : une story se coupe au-delà de 60 s")
    return pb


def cmd_export(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffprobe = binaire(m, "ffprobe")
    if not ffprobe:
        sys.exit("ERREUR : ffprobe introuvable.")
    r = lancer([ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", a.video])
    try:
        info = json.loads(r.stdout)
    except ValueError:
        sys.exit(f"ERREUR : {a.video} illisible.")
    pb = verdict_export(info, a.format, a.video_type)
    if debut_rapide(Path(a.video)) is False:
        pb.append("démarrage lent (index en fin de fichier) : réexporte avec -movflags +faststart")
    print("\n".join(f"❌ {p}" for p in pb) if pb else "ok : prêt pour Instagram")
    if pb:
        sys.exit(1)


LIVRABLES = {"legende.txt": "la légende du Reel", "couverture.jpg": "la couverture"}


def manques_livraison(dossier: Path) -> list[str]:
    """Ce qui manque dans livraison/ : un MP4 par vidéo de l'annonce, la légende et la couverture
    si un Reel est prévu, et le calendrier de publication dans PLAN.md."""
    livraison = dossier / "livraison"
    projets = [p for p in dossier.iterdir() if (p / "meta.json").is_file()]
    videos = [json.loads((p / "meta.json").read_text(encoding="utf-8"))["monteurIa"]["video"] for p in projets]
    manques = [f"{v}.mp4" for v in videos if not (livraison / f"{v}.mp4").is_file()]
    if any(VIDEOS.get(v, {}).get("format") == "reel" for v in videos):
        manques += [f"{f} ({quoi})" for f, quoi in LIVRABLES.items() if not (livraison / f).is_file()]
    plan = (dossier / "PLAN.md").read_text(encoding="utf-8") if (dossier / "PLAN.md").is_file() else ""
    if "## Quand publier" not in plan:
        manques.append("PLAN.md : la section « ## Quand publier »")
    return manques


def cmd_livrer(a) -> None:
    dossier = _dossier_annonce(Path(a.dossier))
    manques = manques_livraison(dossier)
    if manques:
        print("\n".join(f"❌ manque : {x}" for x in manques))
        sys.exit(1)
    print(f"ok : tout est dans {dossier / 'livraison'}")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Annonces de lancement en Reel et en stories (extension Monteur IA).")
    p.add_argument("--version", action="version", version=VERSION)
    s = p.add_subparsers(dest="commande", required=True)
    s.add_parser("verifier", help="Vérifie l'installation.").set_defaults(f=cmd_verifier)
    n = s.add_parser("nouvelle", help="Crée une annonce et un projet par vidéo.")
    n.add_argument("sujet")
    n.add_argument("--videos", default="reel,teaser,ouvert,dernier-jour")
    n.add_argument("--date", default=datetime.date.today().isoformat())
    n.add_argument("--ouvrir", action="store_true")
    n.set_defaults(f=cmd_nouvelle)
    o = s.add_parser("offre", help="Vérifie OFFRE.json : chaque fait a sa source.")
    o.add_argument("dossier")
    o.set_defaults(f=cmd_offre)
    lec = s.add_parser("lecture", help="Temps minimum à l'écran d'un texte.")
    lec.add_argument("texte")
    lec.add_argument("--final", action="store_true", help="Écran final (appel à l'action).")
    lec.set_defaults(f=cmd_lecture)
    z = s.add_parser("zones", help="Zones de sécurité en pixels.")
    z.add_argument("format", choices=sorted(ZONES))
    z.set_defaults(f=cmd_zones)
    pl = s.add_parser("planche", help="Planche de contrôle avec les zones dessinées.")
    pl.add_argument("video")
    pl.add_argument("--format", choices=sorted(ZONES), default="reel")
    pl.add_argument("--sticker", action="store_true", help="Dessine la zone du sticker lien (story).")
    pl.add_argument("--temps", help="Instants en secondes, séparés par des virgules (repères + 0,3 s).")
    pl.add_argument("--sortie")
    pl.set_defaults(f=cmd_planche)
    so = s.add_parser("son", help="Mesure la sonie et la crête.")
    so.add_argument("video")
    so.set_defaults(f=cmd_son)
    ma = s.add_parser("mastering", help="Met le son à -16 LUFS, crête -1,5 dBTP (deux passes).")
    ma.add_argument("entree")
    ma.add_argument("sortie")
    ma.set_defaults(f=cmd_mastering)
    sm = s.add_parser("sans-musique", help="Prépare la version sans musique d'un projet.")
    sm.add_argument("projet")
    sm.set_defaults(f=cmd_sans_musique)
    co = s.add_parser("couverture", help="Pose la couverture en première image.")
    co.add_argument("video")
    co.add_argument("image")
    co.add_argument("sortie")
    co.set_defaults(f=cmd_couverture)
    ex = s.add_parser("export", help="Vérifie un MP4 pour Instagram.")
    ex.add_argument("video")
    ex.add_argument("--format", choices=sorted(ZONES), default="reel")
    ex.add_argument("--type", dest="video_type", choices=sorted(VIDEOS), help="Type de vidéo (bornes de durée).")
    ex.set_defaults(f=cmd_export)
    li = s.add_parser("livrer", help="Vérifie que la livraison est complète.")
    li.add_argument("dossier")
    li.set_defaults(f=cmd_livrer)
    args = p.parse_args(argv)
    args.f(args)


if __name__ == "__main__":
    main()
