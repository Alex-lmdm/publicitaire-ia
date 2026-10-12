#!/usr/bin/env python3
"""STUDIO MOTION : l'outil de l'extension Studio Motion IA de Monteur IA.

Des vidéos en motion design qui vendent l'offre du client, pour un objectif (vendre l'offre,
annoncer une nouveauté, montrer une fonctionnalité, lancer, faire s'inscrire, expliquer,
prouver) et sur les supports qu'il choisit (Reel, story, pub, page de vente, LinkedIn, X,
YouTube). Le support décide du format de sortie, des zones de sécurité et des durées.

Le skill `studio` décide quoi dire et quoi montrer ; cet outil fait le travail mécanique et
vérifiable, pour que rien ne dépende de la mémoire de l'agent.

Usage (depuis le dossier Monteur IA, ou depuis un projet de vidéo) :
    python3 tools/studio_motion.py verifier
    python3 tools/studio_motion.py supports                      # supports, formats, durées
    python3 tools/studio_motion.py nouvelle "<sujet>" --objectif vente --videos reel,page [--ouvrir]
    python3 tools/studio_motion.py offre <dossier de la vidéo>
    python3 tools/studio_motion.py lecture "<texte affiché>" [--final]
    python3 tools/studio_motion.py zones <support> [--format 16x9]
    python3 tools/studio_motion.py planche <video.mp4> [--support reel] [--temps 0.5,2,4.2]
    python3 tools/studio_motion.py son <video.mp4>
    python3 tools/studio_motion.py mastering <entree.mp4> <sortie.mp4>
    python3 tools/studio_motion.py sans-musique <projet>
    python3 tools/studio_motion.py couverture <video.mp4> <image.jpg> <sortie.mp4>
    python3 tools/studio_motion.py export <video.mp4> [--support reel]
    python3 tools/studio_motion.py livrer <dossier de la vidéo>

Une syntaxe pour les vidéos : `support[:rôle][@format]`, par exemple `story:teaser`,
`page@1x1`, `pub@4x5`. Python 3.9+ et la bibliothèque standard seulement. FFmpeg et ffprobe
sont ceux de Monteur IA.
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

VERSION = "0.2.0"
OUTILS = Path(__file__).resolve().parent
FPS = 30

# ---------------------------------------------------------------------------
# Formats de sortie
# ---------------------------------------------------------------------------
FORMATS: dict[str, tuple[int, int]] = {
    "9x16": (1080, 1920),   # Reel, story, TikTok, Shorts, pub plein écran
    "4x5": (1080, 1350),    # fil Instagram et Facebook, pub dans le fil, LinkedIn (recommandé)
    "1x1": (1080, 1080),    # LinkedIn, X, carrousel, page de vente sur téléphone
    "16x9": (1920, 1080),   # page de vente, YouTube, X, présentation
}

# ---------------------------------------------------------------------------
# Supports : où la vidéo sera vue. Durées en secondes : `min` et `max` sont des bornes dures
# (l'export les refuse), `ideal` la plage visée. Zones : fractions de la hauteur (haut, bas) et
# de la largeur (gauche, droite) que l'interface de la plateforme recouvre, plus une marge.
# Valeurs v0.2, la plus stricte des sources retenue, à recaler sur un vrai téléphone.
# ---------------------------------------------------------------------------
SUPPORTS: dict[str, dict] = {
    "reel": {"nom": "Reel", "titre": "Reel Instagram ou Facebook", "format": "9x16",
             "min": 7, "ideal": (20, 45), "max": 90, "zones": (0.156, 0.25, 0.093, 0.139),
             "son": "avec son, compréhensible sans", "cta": "« Commente MOT » ou lien en bio",
             "texte": "legende-reel.txt"},
    "tiktok": {"nom": "TikTok", "titre": "TikTok ou YouTube Shorts", "format": "9x16",
               "min": 7, "ideal": (20, 35), "max": 180, "zones": (0.132, 0.368, 0.113, 0.224),
               "son": "avec son, compréhensible sans", "cta": "lien en bio ou mot-clé en commentaire",
               "texte": "legende-tiktok.txt"},
    "story": {"nom": "Story", "titre": "Story Instagram ou Facebook", "format": "9x16",
              "min": 4, "ideal": (8, 30), "max": 60, "zones": (0.14, 0.15, 0.074, 0.074),
              "son": "souvent muette : tout se lit", "cta": "sticker lien (posé par le client) ou « réponds MOT »",
              "sticker": True},
    "pub": {"nom": "Pub", "titre": "Publicité plein écran (Reels, Stories, TikTok)", "format": "9x16",
            "min": 6, "ideal": (15, 30), "max": 60, "zones": (0.14, 0.35, 0.06, 0.06),
            "son": "avec son, compréhensible sans", "cta": "bouton de la pub, jamais dessiné dans les 35 % du bas",
            "texte": "textes-pub.txt"},
    "fil": {"nom": "Fil", "titre": "Post ou pub dans le fil Instagram et Facebook", "format": "4x5",
            "min": 6, "ideal": (15, 30), "max": 60, "zones": (0.05, 0.05, 0.05, 0.05),
            "son": "souvent muet : tout se lit", "cta": "bouton sous la vidéo, ou dans la légende",
            "texte": "textes-fil.txt"},
    "page": {"nom": "Page de vente", "titre": "Vidéo de vente en haut d'une page de vente ou de capture",
             "format": "16x9", "min": 20, "ideal": (60, 120), "max": 300, "zones": (0.06, 0.1, 0.05, 0.05),
             "son": "lecture auto muette, puis avec son : texte à l'écran obligatoire",
             "cta": "le bouton de la page, juste sous la vidéo", "affiche": True},
    "section": {"nom": "Section de page", "titre": "Boucle muette dans une section de page de vente",
                "format": "16x9", "min": 6, "ideal": (10, 25), "max": 45, "zones": (0.05, 0.05, 0.05, 0.05),
                "son": "muette, en boucle", "cta": "aucun dans la vidéo (la page le porte)", "affiche": True,
                "boucle": True},
    "linkedin": {"nom": "LinkedIn", "titre": "Post vidéo LinkedIn", "format": "4x5",
                 "min": 10, "ideal": (30, 90), "max": 600, "zones": (0.05, 0.1, 0.05, 0.05),
                 "son": "muette par défaut : tout se lit", "cta": "dans le texte du post",
                 "texte": "post-linkedin.txt"},
    "x": {"nom": "X", "titre": "Post vidéo X", "format": "16x9",
          "min": 6, "ideal": (20, 60), "max": 140, "zones": (0.05, 0.1, 0.05, 0.05),
          "son": "muette par défaut : tout se lit", "cta": "dans le texte du post", "texte": "post-x.txt"},
    "youtube": {"nom": "YouTube", "titre": "Vidéo YouTube ou présentation", "format": "16x9",
                "min": 20, "ideal": (60, 180), "max": 900, "zones": (0.08, 0.12, 0.05, 0.05),
                "son": "avec son", "cta": "dans la vidéo et la description"},
}

# ---------------------------------------------------------------------------
# Objectifs : ce que la vidéo doit obtenir. La structure détaillée vit dans le skill
# (references/structures.md) ; ici, les vidéos proposées par défaut.
# ---------------------------------------------------------------------------
OBJECTIFS: dict[str, dict] = {
    "vente": {"nom": "Vendre l'offre", "defaut": ["reel"],
              "quoi": "Présenter l'offre entière et donner envie d'acheter"},
    "nouveaute": {"nom": "Annoncer une nouveauté", "defaut": ["reel", "story"],
                  "quoi": "Un nouveau module, une fonction, un bonus : donner envie d'y avoir accès"},
    "fonctionnalite": {"nom": "Montrer une fonctionnalité", "defaut": ["section"],
                       "quoi": "Une seule fonction, ou une partie de l'offre, et le problème qu'elle règle"},
    "lancement": {"nom": "Lancement", "defaut": ["reel", "story:teaser", "story:ouverture", "story:dernier-jour"],
                  "quoi": "La suite de publications d'une ouverture : teaser, ouverture, relance, dernier jour"},
    "inscription": {"nom": "Faire s'inscrire", "defaut": ["reel", "story"],
                    "quoi": "Un guide gratuit, une liste d'attente, un live ou un webinaire"},
    "explication": {"nom": "Expliquer comment ça marche", "defaut": ["page"],
                    "quoi": "Le fonctionnement en trois étapes, pour lever le doute « est-ce que c'est pour moi »"},
    "preuve": {"nom": "Montrer une preuve", "defaut": ["reel"],
               "quoi": "Un témoignage, un résultat ou un avant / après, mis en valeur"},
}
ROLES = {"teaser": "teaser", "ouverture": "ouverture", "relance": "relance",
         "dernier-jour": "dernier jour", "rappel": "rappel"}
ROLES_STICKER = {"ouverture", "relance", "dernier-jour", "rappel"}
ROLES_FERMETURE = {"dernier-jour"}
# Bande réservée au sticker lien d'une story (fractions de 1080 × 1920) : rien d'important dedans.
STICKER = (190 / 1080, 1180 / 1920, 700 / 1080, 240 / 1920)


def lire_video(spec: str) -> dict:
    """`support[:rôle][@format]` -> {"support", "role", "format"}. Lève ValueError si inconnu."""
    m = re.fullmatch(r"\s*([a-z]+)(?::([a-z-]+))?(?:@(\d+x\d+))?\s*", spec)
    if not m:
        raise ValueError(f"« {spec} » : la forme attendue est support[:rôle][@format].")
    support, role, fmt = m.groups()
    if support not in SUPPORTS:
        raise ValueError(f"support « {support} » inconnu ({', '.join(SUPPORTS)}).")
    if role and role not in ROLES:
        raise ValueError(f"rôle « {role} » inconnu ({', '.join(ROLES)}).")
    fmt = fmt or SUPPORTS[support]["format"]
    if fmt not in FORMATS:
        raise ValueError(f"format « {fmt} » inconnu ({', '.join(FORMATS)}).")
    return {"support": support, "role": role, "format": fmt}


def cle_video(v: dict) -> str:
    """Nom de fichier d'une vidéo : reel, story-teaser, page-1x1…"""
    cle = v["support"] + (f"-{v['role']}" if v.get("role") else "")
    if v["format"] != SUPPORTS[v["support"]]["format"]:
        cle += f"-{v['format']}"
    return cle


def nom_video(v: dict) -> str:
    nom = SUPPORTS[v["support"]]["nom"] + (f" {ROLES[v['role']]}" if v.get("role") else "")
    if v["format"] != SUPPORTS[v["support"]]["format"]:
        nom += f" {v['format']}"
    return nom


def duree_cible(v: dict) -> int:
    lo, hi = SUPPORTS[v["support"]]["ideal"]
    if v.get("role") in ROLES:
        return min(hi, max(lo, 10))  # les stories d'une campagne restent courtes
    return round((lo + hi) / 2)


# ---------------------------------------------------------------------------
# Zones de sécurité
# ---------------------------------------------------------------------------
def zone_texte(support: str, fmt: str | None = None) -> dict:
    """Le rectangle où tout texte important doit tenir, en pixels, pour ce support et ce format."""
    largeur, hauteur = FORMATS[fmt or SUPPORTS[support]["format"]]
    haut, bas, gauche, droite = SUPPORTS[support]["zones"]
    x, y = round(largeur * gauche), round(hauteur * haut)
    return {"x": x, "y": y, "largeur": largeur - x - round(largeur * droite),
            "hauteur": hauteur - y - round(hauteur * bas)}


def zone_sticker(fmt: str = "9x16") -> dict:
    largeur, hauteur = FORMATS[fmt]
    x, y, w, h = STICKER
    return {"x": round(largeur * x), "y": round(hauteur * y), "largeur": round(largeur * w), "hauteur": round(hauteur * h)}


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
    "objectif": "vente",
    "public": {"texte": "", "source": ""},
    "probleme": {"texte": "", "source": ""},
    "promesse": {"texte": "", "source": ""},
    "mecanisme": {"texte": "", "source": ""},
    "nouveaute": {"texte": "", "source": ""},
    "recoit": [],
    "prix": {"montant": None, "devise": "EUR", "barre": None, "source": ""},
    "bonus": [],
    "garantie": {"texte": "", "source": ""},
    "dates": {"ouverture": None, "fermeture": None, "source": ""},
    "preuves": [],
    "objections": [],
    "cta": {"mot_cle": "", "phrase": "", "lien": "", "source": ""},
    "interdits": [],
}
PROMESSE_MAX_MOTS = 9
PREUVES = {"chiffre", "temoignage", "resultat", "media"}
CHAMPS_TEXTE = ("public", "probleme", "promesse", "mecanisme", "nouveaute", "garantie")


def _source(element: dict) -> str:
    return str(element.get("source") or "").strip()


def _texte(element) -> str:
    return str((element or {}).get("texte") or "").strip() if isinstance(element, dict) else ""


def verifier_fiche(fiche: dict, videos: list[dict] | None = None) -> list[str]:
    """Les problèmes de la fiche OFFRE.json, en français. Liste vide = la fiche est utilisable.

    Règle de fond : chaque fait affiché porte sa source (une adresse, « page », « client » s'il l'a
    dit lui-même, ou le nom d'un fichier de sources/). Ce qui n'a pas de source n'existe pas."""
    pb: list[str] = []
    objectif = fiche.get("objectif")
    if not str(fiche.get("produit") or "").strip():
        pb.append("produit : le nom de ce qui est présenté manque.")
    if objectif not in OBJECTIFS:
        pb.append(f"objectif : « {objectif} » inconnu ({', '.join(OBJECTIFS)}).")
    for champ in CHAMPS_TEXTE:
        element = fiche.get(champ) or {}
        if _texte(element) and not _source(element):
            pb.append(f"{champ} : sans source.")
    promesse = _texte(fiche.get("promesse"))
    if not promesse:
        pb.append("promesse : la phrase centrale manque (reprise du titre de la page).")
    elif mots(promesse) > PROMESSE_MAX_MOTS:
        pb.append(f"promesse : {mots(promesse)} mots, {PROMESSE_MAX_MOTS} au plus à l'écran.")
    if objectif == "nouveaute" and not _texte(fiche.get("nouveaute")):
        pb.append("nouveaute : dis ce qui est nouveau (objectif « nouveauté »).")
    if objectif in ("vente", "explication", "inscription") and not _texte(fiche.get("probleme")):
        pb.append("probleme : une vidéo de vente part du problème de l'audience ; il manque.")
    for cle in ("recoit", "bonus", "objections"):
        for i, item in enumerate(fiche.get(cle) or []):
            if not _texte(item):
                pb.append(f"{cle}[{i}] : texte manquant.")
            elif not _source(item):
                pb.append(f"{cle}[{i}] « {item['texte'][:40]} » : sans source.")
    prix = fiche.get("prix") or {}
    if prix.get("montant") is not None:
        if not isinstance(prix["montant"], (int, float)) or prix["montant"] < 0:
            pb.append("prix.montant : un nombre positif est attendu.")
        elif prix.get("barre") is not None and (not isinstance(prix["barre"], (int, float)) or prix["barre"] <= prix["montant"]):
            pb.append("prix.barre : un prix barré doit être un vrai prix plus élevé, affiché sur la page.")
        if not _source(prix):
            pb.append("prix : sans source.")
    dates = fiche.get("dates") or {}
    lues = {}
    for cle in ("ouverture", "fermeture"):
        valeur = dates.get(cle)
        if valeur:
            try:
                lues[cle] = datetime.datetime.fromisoformat(str(valeur))
            except ValueError:
                pb.append(f"dates.{cle} : « {valeur} » n'est pas une date AAAA-MM-JJ[THH:MM].")
    if lues and not _source(dates):
        pb.append("dates : sans source.")
    if "ouverture" in lues and "fermeture" in lues and lues["fermeture"] <= lues["ouverture"]:
        pb.append("dates : la fermeture doit suivre l'ouverture.")
    for i, p in enumerate(fiche.get("preuves") or []):
        if not _texte(p):
            pb.append(f"preuves[{i}] : texte manquant.")
            continue
        if p.get("type") not in PREUVES:
            pb.append(f"preuves[{i}] : type « {p.get('type')} » inconnu ({', '.join(sorted(PREUVES))}).")
        if not _source(p):
            pb.append(f"preuves[{i}] « {p['texte'][:40]} » : sans source, donc inutilisable.")
        if p.get("type") == "temoignage" and not p.get("mot_pour_mot"):
            pb.append(f"preuves[{i}] : un témoignage se cite mot pour mot (`mot_pour_mot: true`).")
    if objectif == "preuve" and not (fiche.get("preuves") or []):
        pb.append("preuves : l'objectif « preuve » demande au moins une preuve sourcée.")
    cta = fiche.get("cta") or {}
    if not any(str(cta.get(k) or "").strip() for k in ("mot_cle", "phrase", "lien")):
        pb.append("cta : ni mot-clé, ni phrase, ni lien d'appel à l'action.")
    if cta.get("mot_cle") and not re.fullmatch(r"[A-ZÀ-ÖØ-Þ0-9]{2,20}", str(cta["mot_cle"])):
        pb.append("cta.mot_cle : un seul mot en MAJUSCULES, sans espace (ex. FORMATION).")
    for v in videos or []:
        if v.get("role") in ROLES_FERMETURE and not dates.get("fermeture"):
            pb.append(f"{cle_video(v)} : pas de date de fermeture sur la page, donc pas de « dernier jour ».")
    return pb


# ---------------------------------------------------------------------------
# Les lieux : le dossier Monteur IA et les vidéos
# ---------------------------------------------------------------------------
INTERDITS_NOM = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
DOSSIER = "studio-motion"


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


def meta_de(chemin: Path) -> dict | None:
    """Le bloc monteurIa du projet qui contient `chemin` (une vidéo exportée, un dossier)."""
    p = Path(chemin).resolve()
    depart = p if p.is_dir() else p.parent
    for d in (depart, *depart.parents):
        f = d / "meta.json"
        if f.is_file():
            try:
                return json.loads(f.read_text(encoding="utf-8")).get("monteurIa") or {}
            except ValueError:
                return None
        if (d / "templates" / "AGENT.md.tpl").is_file():
            return None
    return None


# ---------------------------------------------------------------------------
# Commandes
# ---------------------------------------------------------------------------
def cmd_verifier(_a) -> None:
    m = maison()
    ok = True
    for nom, present in (
        ("dossier Monteur IA", True),
        ("skill studio", (m / ".claude" / "skills" / "studio" / "SKILL.md").is_file()),
        ("aiguillage dans les instructions", "BEGIN EXTENSION: studio-motion" in (m / "templates" / "AGENT.md.tpl").read_text(encoding="utf-8")),
        ("gabarits des vidéos", (m / "templates" / "studio-motion" / "index.html.tpl").is_file()
         or (OUTILS.parent / "templates" / "projet" / "index.html.tpl").is_file()),
        ("style de la marque (brand/)", (m / "brand" / "tokens.css").is_file()),
        ("HyperFrames", (m / "node_modules" / ".bin" / "hyperframes").exists() or shutil.which("hyperframes") is not None),
        ("ffmpeg", binaire(m, "ffmpeg") is not None),
        ("ffprobe", binaire(m, "ffprobe") is not None),
        ("Node", shutil.which("node") is not None),
    ):
        print(f"{'✅' if present else '❌'} {nom}")
        ok = ok and present
    print("ok" if ok else "à corriger")
    if not ok:
        sys.exit(1)


def cmd_supports(_a) -> None:
    print("Supports (format par défaut, durée idéale, bornes) :")
    for cle, s in SUPPORTS.items():
        lo, hi = s["ideal"]
        print(f"- {cle:9} {s['format']:5} {lo}–{hi} s (de {s['min']} à {s['max']} s) · {s['titre']} · {s['son']}")
    print("\nObjectifs :")
    for cle, o in OBJECTIFS.items():
        print(f"- {cle:15} {o['nom']} : {o['quoi']} (par défaut : {', '.join(o['defaut'])})")
    print(f"\nFormats : {', '.join(f'{k} ({w}×{h})' for k, (w, h) in FORMATS.items())}")
    print(f"Rôles d'une campagne : {', '.join(ROLES)}")


def _copier_style(m: Path, projet: Path) -> None:
    """Le rendu ne voit que le dossier du projet : on y copie le style, les polices et GSAP."""
    for sous in ("brand", "assets/vendor", "assets/fonts"):
        src = m / sous
        if src.is_dir():
            shutil.copytree(src, projet / sous, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("atoms.html", "BRAND.md", "*.ttf", ".DS_Store"))


def _remplir(gabarit: str, **valeurs: str) -> str:
    for cle, val in valeurs.items():
        gabarit = gabarit.replace("{{" + cle + "}}", val)
    return gabarit


def _gabarits(m: Path) -> tuple[Path, Path]:
    pres = OUTILS.parent / "templates" / "projet"
    if (pres / "index.html.tpl").is_file():
        return pres / "CLAUDE.md.tpl", pres / "index.html.tpl"
    return m / "templates" / "studio-motion" / "CLAUDE.md.tpl", m / "templates" / "studio-motion" / "index.html.tpl"


def creer(m: Path, sujet: str, objectif: str, videos: list[dict], date: str) -> Path:
    """studio-motion/<sujet> · <date>/ : la fiche, le plan, les sources, la livraison, et un projet de
    l'app HyperFrames par vidéo. Rien n'est jamais écrasé."""
    if objectif not in OBJECTIFS:
        sys.exit(f"ERREUR : objectif inconnu : {objectif} ({', '.join(OBJECTIFS)}).")
    if not videos:
        sys.exit("ERREUR : aucune vidéo demandée.")
    cles = [cle_video(v) for v in videos]
    if len(set(cles)) != len(cles):
        sys.exit(f"ERREUR : deux vidéos portent le même nom ({', '.join(cles)}) : donne-leur un rôle ou un format.")
    base = m / DOSSIER / " · ".join(p for p in (propre(sujet), date) if p)
    dossier, n = base, 2
    while dossier.exists():
        dossier, n = base.with_name(f"{base.name} ({n})"), n + 1
    for sous in ("sources", "livraison"):
        (dossier / sous).mkdir(parents=True, exist_ok=True)
    fiche = json.loads(json.dumps(FICHE_VIDE))
    fiche.update(produit=sujet, objectif=objectif)
    (dossier / "OFFRE.json").write_text(json.dumps(fiche, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    plan = [f"# {OBJECTIFS[objectif]['nom']} : {sujet}\n\nCréé le {date}. Objectif : {OBJECTIFS[objectif]['quoi']}.\n",
            "## Brief\n\n(objectif précis, public, supports, voix, ce que la vidéo doit faire faire)\n",
            "## Structure et angle retenus\n\n(à remplir après le choix du client)\n", "## Vidéos\n"]
    for v in videos:
        s = SUPPORTS[v["support"]]
        lo, hi = s["ideal"]
        plan.append(f"### {nom_video(v)} ({v['format']}, {lo} à {hi} s visées, {s['son']})\n\n"
                    "| Temps | Bloc | À l'écran (texte exact) | Voix | Clé de OFFRE.json | Mouvement | Son |\n"
                    "|---|---|---|---|---|---|---|\n")
    (dossier / "PLAN.md").write_text("\n".join(plan), encoding="utf-8")
    gabarit_md, gabarit_html = _gabarits(m)
    maintenant = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    for v in videos:
        s = SUPPORTS[v["support"]]
        largeur, hauteur = FORMATS[v["format"]]
        cle, duree = cle_video(v), duree_cible(v)
        projet = dossier / propre(f"{sujet} · {nom_video(v)}", 60)
        projet.mkdir(parents=True)
        for sous in ("assets/images", "assets/audio", "exports", "work"):
            (projet / sous).mkdir(parents=True, exist_ok=True)
        _copier_style(m, projet)
        if (m / "hyperframes.json").is_file():
            shutil.copy2(m / "hyperframes.json", projet / "hyperframes.json")
        lo, hi = s["ideal"]
        valeurs = {"SUJET": sujet, "VIDEO": cle, "VIDEO_NOM": nom_video(v), "SUPPORT": v["support"],
                   "SUPPORT_TITRE": s["titre"], "FORMAT": v["format"], "LARGEUR": str(largeur),
                   "HAUTEUR": str(hauteur), "DUREE": str(duree), "IDEAL": f"{lo} à {hi}",
                   "DUREE_MIN": str(s["min"]), "DUREE_MAX": str(s["max"]), "SON": s["son"], "CTA": s["cta"],
                   "OBJECTIF": OBJECTIFS[objectif]["nom"], "MAISON": "../../../", "DOSSIER": "../"}
        if gabarit_html.is_file():
            (projet / "index.html").write_text(_remplir(gabarit_html.read_text(encoding="utf-8"), **valeurs), encoding="utf-8")
        if gabarit_md.is_file():
            texte = _remplir(gabarit_md.read_text(encoding="utf-8"), **valeurs)
            (projet / "CLAUDE.md").write_text(texte, encoding="utf-8")
            (projet / "AGENTS.md").write_text(texte, encoding="utf-8")
        meta = {"id": projet.name, "name": projet.name, "createdAt": maintenant,
                "monteurIa": {"lieu": "studio-motion", "objectif": objectif, "video": cle, "support": v["support"],
                              "role": v.get("role"), "format": v["format"], "sujet": sujet, "date": date}}
        (projet / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        paquet = {"name": f"studio-motion-{cle}", "private": True, "type": "module",
                  "scripts": {"dev": "hyperframes preview", "check": "hyperframes check",
                              "render": f"hyperframes render -o exports/{cle}.mp4"}}
        (projet / "package.json").write_text(json.dumps(paquet, indent=2) + "\n", encoding="utf-8")
    return dossier


def projets(dossier: Path) -> list[tuple[Path, dict]]:
    sortie = []
    for p in sorted(dossier.iterdir()):
        if (p / "meta.json").is_file():
            try:
                sortie.append((p, json.loads((p / "meta.json").read_text(encoding="utf-8"))["monteurIa"]))
            except (ValueError, KeyError):
                continue
    return sortie


def cmd_nouvelle(a) -> None:
    m = maison()
    if not propre(a.sujet):
        sys.exit("ERREUR : donne un sujet, en quelques mots.")
    specs = a.videos.split(",") if a.videos else OBJECTIFS[a.objectif]["defaut"]
    try:
        videos = [lire_video(s) for s in specs if s.strip()]
    except ValueError as e:
        sys.exit(f"ERREUR : {e}")
    dossier = creer(m, a.sujet, a.objectif, videos, a.date)
    print(f"• créé : {dossier.relative_to(m)} ({OBJECTIFS[a.objectif]['nom']})")
    for projet, meta in projets(dossier):
        print(f"  - {projet.name} ({meta['format']})")
    print("• à remplir d'abord : OFFRE.json (puis `studio_motion.py offre`), puis PLAN.md")
    if a.ouvrir:
        ouvreur = m / "scripts" / "app-hyperframes.mjs"
        for projet, _meta in projets(dossier):
            if ouvreur.is_file():
                lancer(["node", str(ouvreur), "ouvrir", str(projet)], cwd=m)
        print("• projets ouverts dans l'app HyperFrames")


def _dossier_fiche(chemin: Path) -> Path:
    p = Path(chemin).resolve()
    for d in (p, *p.parents):
        if (d / "OFFRE.json").is_file():
            return d
    sys.exit(f"ERREUR : aucun OFFRE.json dans {p} ni au-dessus. Donne le dossier de la vidéo.")


def cmd_offre(a) -> None:
    dossier = _dossier_fiche(Path(a.dossier))
    fiche = json.loads((dossier / "OFFRE.json").read_text(encoding="utf-8"))
    pb = verifier_fiche(fiche, [meta for _p, meta in projets(dossier)])
    if pb:
        print("\n".join(f"❌ {p}" for p in pb))
        sys.exit(1)
    print("ok : chaque fait de la fiche a sa source")


def cmd_lecture(a) -> None:
    print(f"{lecture(a.texte, final=a.final):.1f} s minimum à l'écran ({mots(a.texte)} mots)")


def cmd_zones(a) -> None:
    fmt = a.format or SUPPORTS[a.support]["format"]
    sortie = {"support": a.support, "format": fmt, "taille": FORMATS[fmt], "zone_texte": zone_texte(a.support, fmt)}
    if SUPPORTS[a.support].get("sticker"):
        sortie["sticker_lien"] = zone_sticker(fmt)
    print(json.dumps(sortie, ensure_ascii=False, indent=2))


def _sonder(ffprobe: str, video: Path) -> dict:
    r = lancer([ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)])
    try:
        return json.loads(r.stdout)
    except ValueError:
        sys.exit(f"ERREUR : {video} illisible.")


def format_de(info: dict) -> str | None:
    v = next((s for s in info.get("streams") or [] if s.get("codec_type") == "video"), None)
    if not v:
        return None
    taille = (v.get("width"), v.get("height"))
    return next((k for k, t in FORMATS.items() if t == taille), None)


def instants_planche(duree: float, temps: list[float] | None, pas: float = 1.0) -> list[float]:
    """Les instants de la planche : ceux demandés (repères + 0,3 s), sinon un par seconde (un toutes
    les 3 s au-delà de 40 s), plus toujours la dernière image. Bornés, sans doublon, triés."""
    if not temps and duree > 40:
        pas = 3.0
    base = temps if temps else [round(i * pas + 0.3, 2) for i in range(int(duree // pas) + 1)]
    # Deux images avant la fin, arrondi vers le bas : un instant au-delà de la dernière image
    # (7,97 s pour une vidéo de 8 s à 30 images/s) ne rend rien.
    fin = max(0.0, math.floor((duree - 2 / FPS) * 100) / 100)
    return sorted({round(min(max(0.0, t), fin), 2) for t in base} | {fin})


def cmd_planche(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg, ffprobe = binaire(m, "ffmpeg"), binaire(m, "ffprobe")
    if not ffmpeg or not ffprobe:
        sys.exit("ERREUR : ffmpeg introuvable.")
    video = Path(a.video).resolve()
    info = _sonder(ffprobe, video)
    meta = meta_de(video) or {}
    support = a.support or meta.get("support") or "reel"
    fmt = format_de(info) or SUPPORTS[support]["format"]
    try:
        duree = float((info.get("format") or {}).get("duration"))
    except (TypeError, ValueError):
        sys.exit(f"ERREUR : durée de {video} illisible.")
    temps = [float(t) for t in a.temps.split(",")] if a.temps else None
    instants = instants_planche(duree, temps)
    sortie = Path(a.sortie) if a.sortie else video.with_name(video.stem + "-planche.jpg")
    travail = sortie.with_suffix("")
    travail.mkdir(parents=True, exist_ok=True)
    z = zone_texte(support, fmt)
    trait = max(3, FORMATS[fmt][0] // 270)
    boites = [f"drawbox=x={z['x']}:y={z['y']}:w={z['largeur']}:h={z['hauteur']}:color=0x00ff88@0.9:t={trait}"]
    sticker = SUPPORTS[support].get("sticker") and (a.sticker or meta.get("role") in ROLES_STICKER)
    if sticker:
        s = zone_sticker(fmt)
        boites.append(f"drawbox=x={s['x']}:y={s['y']}:w={s['largeur']}:h={s['hauteur']}:color=0xff3366@0.9:t={trait + 2}")
    largeur_vignette = 360 if FORMATS[fmt][0] <= FORMATS[fmt][1] else 480
    vignettes = []
    for i, t in enumerate(instants):
        img = travail / f"{i:03d}.jpg"
        chaine = boites + [f"scale={largeur_vignette}:-2"]
        r = lancer([ffmpeg, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-vf", ",".join(chaine), str(img)])
        if (r.returncode != 0 or not img.is_file()) and t >= instants[-1]:
            # Dernière image : on la prend depuis la fin du fichier.
            r = lancer([ffmpeg, "-v", "error", "-y", "-sseof", "-0.1", "-i", str(video), "-update", "1",
                        "-vf", ",".join(chaine), str(img)])
        if r.returncode == 0 and img.is_file():
            vignettes.append(img)
        else:
            print(f"⚠️ image à {t:.2f} s non extraite")
    if not vignettes:
        sys.exit("ERREUR : aucune image extraite.")
    colonnes = min(6 if largeur_vignette == 360 else 4, len(vignettes))
    lignes = math.ceil(len(vignettes) / colonnes)
    r = lancer([ffmpeg, "-v", "error", "-y", "-framerate", "1", "-i", str(travail / "%03d.jpg"),
                "-vf", f"tile={colonnes}x{lignes}:padding=8:margin=8:color=0x202022", "-frames:v", "1", str(sortie)])
    if r.returncode != 0:
        sys.exit(f"ERREUR : planche impossible : {r.stderr[-400:]}")
    shutil.rmtree(travail, ignore_errors=True)
    print(f"• planche : {sortie} ({len(vignettes)} images : {', '.join(f'{t:.2f}' for t in instants)} s)")
    print("  vert = zone texte (rien d'important dehors)" + (", rouge = sticker lien (rien dedans)" if sticker else ""))


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
        pb.append(f"sonie {i:.1f} LUFS, cible {CIBLE_LUFS:.0f} ±1 : lance `studio_motion.py mastering`")
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
        print("ℹ️ pas de piste son : version muette (normal pour une boucle de page ou une story sans musique)")
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
    Instagram. Les bruitages et la voix restent."""
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
    cle = (meta_de(projet) or {}).get("video", "video")
    print(f"• {cible.name} prêt ({n} piste(s) de musique retirée(s)). Rendu :")
    print(f"  npx hyperframes render -c {cible.name} -o exports/{cle}-sans-musique.mp4")


def cmd_couverture(a) -> None:
    """La couverture devient la toute première image : les aperçus (X, WhatsApp, Instagram avant
    lecture) montrent alors la bonne image. Une seule image remplacée, son conservé."""
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg, ffprobe = binaire(m, "ffmpeg"), binaire(m, "ffprobe")
    if not ffmpeg or not ffprobe:
        sys.exit("ERREUR : ffmpeg introuvable.")
    fmt = format_de(_sonder(ffprobe, Path(a.video))) or "9x16"
    largeur, hauteur = FORMATS[fmt]
    r = lancer([ffmpeg, "-v", "error", "-y", "-i", a.video, "-i", a.image, "-filter_complex",
                f"[1:v]scale={largeur}:{hauteur}:force_original_aspect_ratio=increase,crop={largeur}:{hauteur}[c];"
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


def verdict_export(info: dict, support: str, fmt: str | None = None, poids: int | None = None) -> tuple[list[str], list[str]]:
    """Les écarts d'un fichier exporté (ffprobe -show_streams -show_format) : (bloquants, avis)."""
    pb, avis = [], []
    s = SUPPORTS[support]
    attendu = fmt or s["format"]
    flux = info.get("streams") or []
    v = next((x for x in flux if x.get("codec_type") == "video"), None)
    if not v:
        return ["aucune piste vidéo"], avis
    if (v.get("width"), v.get("height")) != FORMATS[attendu]:
        pb.append(f"taille {v.get('width')}×{v.get('height')}, attendu {FORMATS[attendu][0]}×{FORMATS[attendu][1]} ({attendu})")
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
    a = next((x for x in flux if x.get("codec_type") == "audio"), None)
    if a and a.get("codec_name") != "aac":
        pb.append(f"son {a.get('codec_name')}, attendu aac")
    if a and s.get("boucle"):
        avis.append("boucle de page avec une piste son : retire-la (-an), elle pèse et ne sera jamais entendue")
    try:
        duree = float((info.get("format") or {}).get("duration"))
    except (TypeError, ValueError):
        duree = None
    if duree is not None:
        hi = s["ideal"][1]
        if duree < s["min"] - 0.5 or duree > s["max"] + 0.5:
            pb.append(f"durée {duree:.1f} s hors de {s['min']}–{s['max']} s pour {s['titre']}")
        elif duree > hi + 0.5:
            avis.append(f"durée {duree:.1f} s au-delà des {hi} s visées pour ce support : coupe si tu peux")
    if poids and s.get("affiche") and poids > 25 * 1024 * 1024:
        avis.append(f"{poids / 1024 / 1024:.0f} Mo : lourd pour une page web, vise moins de 15 Mo")
    return pb, avis


def cmd_export(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffprobe = binaire(m, "ffprobe")
    if not ffprobe:
        sys.exit("ERREUR : ffprobe introuvable.")
    meta = meta_de(Path(a.video)) or {}
    support = a.support or meta.get("support")
    if support not in SUPPORTS:
        sys.exit("ERREUR : précise le support (--support reel, story, pub, page…).")
    fmt = a.format or (meta.get("format") if meta.get("support") == support else None)
    pb, avis = verdict_export(_sonder(ffprobe, Path(a.video)), support, fmt, Path(a.video).stat().st_size)
    if debut_rapide(Path(a.video)) is False:
        pb.append("démarrage lent (index en fin de fichier) : réexporte avec -movflags +faststart")
    for x in avis:
        print(f"⚠️ {x}")
    print("\n".join(f"❌ {p}" for p in pb) if pb else f"ok : prêt pour {SUPPORTS[support]['titre']}")
    if pb:
        sys.exit(1)


def manques_livraison(dossier: Path) -> list[str]:
    """Ce qui manque dans livraison/ : un MP4 par vidéo, le texte de publication de chaque support
    qui en a un, l'affiche des vidéos de page, et le calendrier d'une campagne de lancement."""
    livraison = dossier / "livraison"
    manques = []
    textes = set()
    campagne = page = reel = False
    for _projet, meta in projets(dossier):
        cle, s = meta["video"], SUPPORTS.get(meta.get("support"), {})
        if not (livraison / f"{cle}.mp4").is_file():
            manques.append(f"{cle}.mp4")
        if s.get("affiche") and not (livraison / f"{cle}.jpg").is_file():
            manques.append(f"{cle}.jpg (l'affiche, montrée avant la lecture)")
        if s.get("texte"):
            textes.add(s["texte"])
        campagne = campagne or meta.get("objectif") == "lancement" or bool(meta.get("role"))
        page = page or bool(s.get("affiche"))
        reel = reel or meta.get("support") in ("reel", "tiktok")
    manques += [f"{t} (le texte de publication)" for t in sorted(textes) if not (livraison / t).is_file()]
    if reel and not (livraison / "couverture.jpg").is_file():
        manques.append("couverture.jpg (la couverture du Reel)")
    if page and not (livraison / "integration.md").is_file():
        manques.append("integration.md (comment poser la vidéo sur la page)")
    plan = (dossier / "PLAN.md").read_text(encoding="utf-8") if (dossier / "PLAN.md").is_file() else ""
    if campagne and "## Quand publier" not in plan:
        manques.append("PLAN.md : la section « ## Quand publier »")
    return manques


def cmd_livrer(a) -> None:
    dossier = _dossier_fiche(Path(a.dossier))
    manques = manques_livraison(dossier)
    if manques:
        print("\n".join(f"❌ manque : {x}" for x in manques))
        sys.exit(1)
    print(f"ok : tout est dans {dossier / 'livraison'}")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Studio Motion IA : vidéos en motion design qui vendent (extension Monteur IA).")
    p.add_argument("--version", action="version", version=VERSION)
    s = p.add_subparsers(dest="commande", required=True)
    s.add_parser("verifier", help="Vérifie l'installation.").set_defaults(f=cmd_verifier)
    s.add_parser("supports", help="Supports, objectifs et formats possibles.").set_defaults(f=cmd_supports)
    n = s.add_parser("nouvelle", help="Crée une vidéo (ou une série) et un projet par format.")
    n.add_argument("sujet")
    n.add_argument("--objectif", default="vente", choices=sorted(OBJECTIFS))
    n.add_argument("--videos", help="support[:rôle][@format], séparés par des virgules (défaut : selon l'objectif).")
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
    z = s.add_parser("zones", help="Zone de texte sûre en pixels.")
    z.add_argument("support", choices=sorted(SUPPORTS))
    z.add_argument("--format", choices=sorted(FORMATS))
    z.set_defaults(f=cmd_zones)
    pl = s.add_parser("planche", help="Planche de contrôle avec les zones dessinées.")
    pl.add_argument("video")
    pl.add_argument("--support", choices=sorted(SUPPORTS), help="Défaut : celui du projet.")
    pl.add_argument("--sticker", action="store_true", help="Dessine la zone du sticker lien (story).")
    pl.add_argument("--temps", help="Instants en secondes, séparés par des virgules (repères + 0,3 s).")
    pl.add_argument("--sortie")
    pl.set_defaults(f=cmd_planche)
    so = s.add_parser("son", help="Mesure la sonie et la crête.")
    so.add_argument("video")
    so.set_defaults(f=cmd_son)
    ma = s.add_parser("mastering", help="Met le son à -16 LUFS, crêtes sous -1 dBTP.")
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
    ex = s.add_parser("export", help="Vérifie un MP4 pour son support.")
    ex.add_argument("video")
    ex.add_argument("--support", choices=sorted(SUPPORTS), help="Défaut : celui du projet.")
    ex.add_argument("--format", choices=sorted(FORMATS))
    ex.set_defaults(f=cmd_export)
    li = s.add_parser("livrer", help="Vérifie que la livraison est complète.")
    li.add_argument("dossier")
    li.set_defaults(f=cmd_livrer)
    args = p.parse_args(argv)
    args.f(args)


if __name__ == "__main__":
    main()
