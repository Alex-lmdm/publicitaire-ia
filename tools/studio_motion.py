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
    python3 tools/studio_motion.py ajouter <dossier> --videos linkedin,story   # « la même pour LinkedIn »
    python3 tools/studio_motion.py offre <dossier de la vidéo>
    python3 tools/studio_motion.py lecture "<texte affiché>" [--final]
    python3 tools/studio_motion.py zones <support> [--format 16x9]
    python3 tools/studio_motion.py reference <dossier> <lien ou fichier> [--nom taapit]   # la vidéo dont il aime le style
    python3 tools/studio_motion.py logos <projet> claude openai codex [icone:rocket]      # logos des outils montrés
    python3 tools/studio_motion.py planche <video.mp4> [--support reel] [--temps 0.5,2,4.2]
    python3 tools/studio_motion.py rythme <video.mp4>                # au moins 1 événement/s, rien de figé
    python3 tools/studio_motion.py musique <morceau.wav> [--sortie calee.wav --a 8 --duree 67]   # tempo, entrée, calage
    python3 tools/studio_motion.py emergence <projet>                # chaque bruitage dépasse la musique
    python3 tools/studio_motion.py son <video.mp4> [--cible -16]
    python3 tools/studio_motion.py mastering <entree.mp4> <sortie.mp4> [--cible -16]
    python3 tools/studio_motion.py sans-musique <projet>
    python3 tools/studio_motion.py couverture <video.mp4> <image.jpg> <sortie.mp4>
    python3 tools/studio_motion.py affiche <video.mp4> <affiche.jpg> [--temps 0]
    python3 tools/studio_motion.py preparer-video <entree.mp4> <sortie.mp4> [--avec-son]
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

VERSION = "0.4.1"
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
              "sticker": True, "texte": "stories.txt"},
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


def avec_sticker(v: dict) -> bool:
    """Une story renvoie vers un lien (sticker posé par le client), sauf le teaser d'un lancement."""
    return bool(SUPPORTS[v["support"]].get("sticker")) and v.get("role") != "teaser"


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
# Un écran porte 1 à 4 mots (6 au plus) : la vidéo montre, le texte titre. Lu vite, donc tenu
# moins longtemps qu'une phrase ; ce qui l'entoure continue de vivre pendant la lecture.
PAR_MOT, ASSISE, PLANCHER, FINAL = 0.25, 0.5, 0.8, 2.5
MOTS_CONSEILLES, MOTS_MAX = 4, 6


def mots(texte: str) -> int:
    return len([m for m in re.split(r"\s+", texte.strip()) if re.search(r"\w", m)])


def lecture(texte: str, final: bool = False) -> float:
    """Durée minimale (s) pendant laquelle un texte doit rester immobile et lisible.

    0,25 s par mot + 0,5 s d'assise, jamais moins de 0,8 s ; l'écran final (appel à l'action)
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
    "echeances": [],
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


def _date(valeur) -> datetime.datetime | None:
    try:
        return datetime.datetime.fromisoformat(str(valeur))
    except ValueError:
        return None


FICHIER_SOURCE = re.compile(r"^[^\s/]+\.[a-z0-9]{2,5}$", re.I)


def sources_absentes(fiche: dict, dossier: Path) -> list[str]:
    """Les sources qui nomment un fichier (« capture-prix.png ») absent de sources/ ou du dossier."""
    trouvees: list[str] = []

    def visiter(x) -> None:
        if isinstance(x, dict):
            src = str(x.get("source") or "").strip()
            if FICHIER_SOURCE.match(src) and not any((d / src).is_file() for d in (dossier / "sources", dossier)):
                trouvees.append(src)
            for v in x.values():
                visiter(v)
        elif isinstance(x, list):
            for v in x:
                visiter(v)
    visiter(fiche)
    return sorted(set(trouvees))


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
    for i, e in enumerate(fiche.get("echeances") or []):
        if not _texte(e):
            pb.append(f"echeances[{i}] : dis ce qui se termine (ex. « Bonus Reel Cloneur offert »).")
        elif _date(e.get("date")) is None:
            pb.append(f"echeances[{i}] : date « {e.get('date')} » illisible (AAAA-MM-JJ[THH:MM]).")
        elif not _source(e):
            pb.append(f"echeances[{i}] « {e['texte'][:40]} » : sans source.")
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


def polices_manquantes(dossier: Path) -> list[str]:
    """Les polices de la marque (titres, texte) qui n'ont aucun @font-face dans brand/fonts.css.

    Au rendu, HyperFrames ne télécharge pas une police absente : il prend la suivante de la liste
    (souvent Impact ou une police système), alors que `check` et les captures, eux, la trouvent
    sur Google Fonts. Le défaut ne se voit donc que sur le MP4 rendu, d'où ce contrôle en amont."""
    tokens, fonts = dossier / "brand" / "tokens.css", dossier / "brand" / "fonts.css"
    if not tokens.is_file():
        return []
    css = tokens.read_text(encoding="utf-8")
    declarees = set(re.findall(r'font-family:\s*"?([^";]+?)"?\s*;', fonts.read_text(encoding="utf-8"))) if fonts.is_file() else set()
    manquantes = []
    for role in ("display", "body"):
        m = re.search(rf"--brand-font-{role}:\s*([^;]+);", css)
        if not m:
            continue
        famille = m.group(1).split(",")[0].strip().strip('"')
        if famille and famille not in declarees and famille not in manquantes:
            manquantes.append(famille)
    return manquantes


CONSEIL_POLICE = ("dépose ses fichiers .woff2 dans assets/fonts/ du dossier Monteur IA, déclare-la dans la table "
                  "`fonts` de templates/style-presets.json, puis `npm run sync` ; ou choisis une police livrée "
                  "avec /setup visuel")


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
        ("Node", shutil.which("node") is not None or any(Path.home().glob(".nvm/versions/node/*/bin/node"))),
    ):
        print(f"{'✅' if present else '❌'} {nom}")
        ok = ok and present
    for famille in polices_manquantes(m):
        print(f"⚠️ police « {famille} » sans fichier : au rendu, elle serait remplacée par une autre. Pour la garder, {CONSEIL_POLICE}.")
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


POLICES_INTERFACES = ((400, "normal", "Inter-400.woff2"), (400, "italic", "Inter-400-italic.woff2"),
                      (600, "normal", "Inter-600.woff2"), (700, "normal", "Inter-700.woff2"),
                      (900, "normal", "Inter-900.woff2"))


def _polices_interfaces(projet: Path) -> Path:
    """Inter (licence SIL OFL), la police des interfaces reconstruites (Claude, Codex, un logiciel).
    Sa feuille s'écrit à côté de ses fichiers, dans assets/fonts/ : le rendu refuse un chemin qui
    remonte (« ../ »), et une feuille rangée dans kit/ en aurait besoin. Seuls les fichiers présents
    sont déclarés ; sans eux, la feuille reste vide et le texte prend la police de secours."""
    fonts = projet / "assets" / "fonts"
    fonts.mkdir(parents=True, exist_ok=True)
    lignes = [f'@font-face {{ font-family: "Inter"; font-style: {style}; font-weight: {poids}; '
              f'font-display: block; src: url("{nom}") format("woff2"); }}'
              for poids, style, nom in POLICES_INTERFACES if (fonts / nom).is_file()]
    feuille = fonts / "interfaces.css"
    feuille.write_text("/* Inter (licence SIL OFL), pour les interfaces reconstruites. Écrit par studio_motion.py. */\n"
                       + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return feuille


def _kit(m: Path) -> Path | None:
    """Le kit de briques (fonds, curseur, objets flottants, chapitres, interfaces) : celui de
    l'extension, sinon celui installé dans le dossier Monteur IA."""
    for dossier in (OUTILS.parent / "templates" / "kit", m / "templates" / "studio-motion" / "kit"):
        if (dossier / "kit.js").is_file():
            return dossier
    return None


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
    for v in videos:
        creer_projet(m, dossier, sujet, objectif, v, date)
    return dossier


def creer_projet(m: Path, dossier: Path, sujet: str, objectif: str, v: dict, date: str) -> Path:
    """Un projet de l'app HyperFrames pour une vidéo du dossier : style copié, gabarit, instructions."""
    gabarit_md, gabarit_html = _gabarits(m)
    maintenant = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    s = SUPPORTS[v["support"]]
    largeur, hauteur = FORMATS[v["format"]]
    cle, duree = cle_video(v), duree_cible(v)
    projet = dossier / propre(f"{sujet} · {nom_video(v)}", 60)
    projet.mkdir(parents=True)
    for sous in ("assets/images", "assets/audio", "exports", "work"):
        (projet / sous).mkdir(parents=True, exist_ok=True)
    _copier_style(m, projet)
    _polices_interfaces(projet)
    kit = _kit(m)
    if kit:
        shutil.copytree(kit, projet / "kit", dirs_exist_ok=True, ignore=shutil.ignore_patterns(".DS_Store"))
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
                          "role": v.get("role"), "format": v["format"], "sujet": sujet, "date": date,
                          "sticker": avec_sticker(v)}}
    (projet / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    paquet = {"name": f"studio-motion-{cle}", "private": True, "type": "module",
              "scripts": {"dev": "hyperframes preview", "check": "hyperframes check",
                          "render": f"hyperframes render -o exports/{cle}.mp4"}}
    (projet / "package.json").write_text(json.dumps(paquet, indent=2) + "\n", encoding="utf-8")
    return projet


def ajouter(m: Path, dossier: Path, videos: list[dict]) -> list[Path]:
    """Ajoute des vidéos (un autre support, un autre format) à un dossier existant : même fiche, même
    plan, même sujet. Une vidéo déjà présente n'est jamais recréée."""
    existants = projets(dossier)
    if not existants:
        sys.exit(f"ERREUR : {dossier} n'a aucun projet de vidéo : crée-le avec `nouvelle`.")
    deja = {meta["video"] for _p, meta in existants}
    doublons = [cle_video(v) for v in videos if cle_video(v) in deja]
    if doublons:
        sys.exit(f"ERREUR : déjà dans ce dossier : {', '.join(doublons)}. Donne un autre format (@4x5) ou un rôle.")
    frere, meta0 = existants[0]
    sujet, objectif, date = meta0.get("sujet", dossier.name), meta0.get("objectif", "vente"), meta0.get("date", "")
    plan = dossier / "PLAN.md"
    ajouts = []
    for v in videos:
        projet = creer_projet(m, dossier, sujet, objectif, v, date)
        # La matière déjà préparée pour la première vidéo (polices locales, images, vidéos
        # préparées) sert aussi à la déclinaison : on la reprend au lieu de la refaire.
        for sous in ("assets/fonts", "assets/images", "assets/video"):
            if (frere / sous).is_dir():
                shutil.copytree(frere / sous, projet / sous, dirs_exist_ok=True)
        _polices_interfaces(projet)
        ajouts.append(projet)
        sup = SUPPORTS[v["support"]]
        lo, hi = sup["ideal"]
        section = (f"### {nom_video(v)} ({v['format']}, {lo} à {hi} s visées, {sup['son']})\n\n"
                   "Déclinaison : même structure et même message, remis en page pour ce format, "
                   "raccourci si le support le demande (une story garde un geste par bloc).\n\n"
                   "| Temps | Bloc | À l'écran (texte exact) | Voix | Clé de OFFRE.json | Mouvement | Son |\n"
                   "|---|---|---|---|---|---|---|\n")
        if plan.is_file():
            plan.write_text(inserer_section(plan.read_text(encoding="utf-8"), section), encoding="utf-8")
    return ajouts


def inserer_section(plan: str, section: str) -> str:
    """Ajoute une section de vidéo à la fin de « ## Vidéos » (avant le titre de niveau 2 suivant),
    ou à la fin du plan s'il n'a pas cette partie."""
    m = re.search(r"^## Vidéos\s*$", plan, re.M)
    if not m:
        return plan.rstrip("\n") + "\n\n" + section
    suite = re.search(r"^## ", plan[m.end():], re.M)
    if not suite:
        return plan.rstrip("\n") + "\n\n" + section
    coupe = m.end() + suite.start()
    return plan[:coupe].rstrip("\n") + "\n\n" + section + "\n" + plan[coupe:]


def projets(dossier: Path) -> list[tuple[Path, dict]]:
    sortie = []
    for p in sorted(dossier.iterdir()):
        if (p / "meta.json").is_file():
            try:
                sortie.append((p, json.loads((p / "meta.json").read_text(encoding="utf-8"))["monteurIa"]))
            except (ValueError, KeyError):
                continue
    return sortie


def cmd_ajouter(a) -> None:
    m = maison()
    dossier = _dossier_fiche(Path(a.dossier))
    try:
        videos = [lire_video(x) for x in a.videos.split(",") if x.strip()]
    except ValueError as e:
        sys.exit(f"ERREUR : {e}")
    for projet in ajouter(m, dossier, videos):
        print(f"• ajouté : {projet.name} (polices, images et vidéos du premier projet reprises)")
    print("• même fiche (OFFRE.json) ; complète sa section dans PLAN.md, puis remets la vidéo en page pour ce format")
    for famille in polices_manquantes(m):
        print(f"⚠️ police « {famille} » sans fichier dans brand/fonts.css : vérifie que le projet a ses @font-face locaux, sinon {CONSEIL_POLICE}.")


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
    for famille in polices_manquantes(m):
        print(f"⚠️ police « {famille} » sans fichier : le MP4 la remplacerait. Pour la garder, {CONSEIL_POLICE}. "
              "Sinon, utilise une police déclarée dans brand/fonts.css.")
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
    pb += [f"source « {f} » introuvable dans sources/ : la fiche cite un fichier qui n'existe pas." for f in sources_absentes(fiche, dossier)]
    if pb:
        print("\n".join(f"❌ {p}" for p in pb))
        sys.exit(1)
    print("ok : chaque fait de la fiche a sa source")


def cmd_lecture(a) -> None:
    n = mots(a.texte)
    print(f"{lecture(a.texte, final=a.final):.1f} s minimum à l'écran ({n} mots)")
    if n > MOTS_MAX:
        print(f"⚠️ {n} mots : trop pour un écran ({MOTS_CONSEILLES} conseillés, {MOTS_MAX} au plus). Coupe, ou montre-le au lieu de l'écrire.")
    elif n > MOTS_CONSEILLES:
        print(f"• {n} mots : acceptable une fois, {MOTS_CONSEILLES} au plus d'habitude.")


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
    sticker = SUPPORTS[support].get("sticker") and not a.sans_sticker and (
        a.sticker or meta.get("sticker") or meta.get("role") in ROLES_STICKER)
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


# ---------------------------------------------------------------------------
# Le rythme, mesuré sur le MP4 rendu. Étalonné le 12/10/2026 : une vidéo produit de référence
# (motion design d'un lancement) fait 1,5 événement par seconde, un écart médian de 0,4 s entre
# deux et 3 % d'image figée (son écran final) ; une vidéo en « slides » refusée par son client
# faisait 0,33 événement par seconde, 1,75 s d'écart médian et 67 % d'image figée.
# ---------------------------------------------------------------------------
RYTHME_FPS, RYTHME_TAILLE = 10, (96, 54)
SEUIL_FIGE, FIGE_MAX = 0.3, 1.0        # écart moyen des pixels (0-255) sous lequel rien ne bouge ; plage tolérée (s)
SEUIL_EVENEMENT = 2.0                   # un pic d'écart au-dessus = un événement (entrée, clic, coupe, compteur)
EVENEMENTS_MIN, ECART_MEDIAN_MAX = 1.0, 0.8
CREUX_SIGNALE, FIN_LIBRE = 2.0, 3.5    # creux entre deux événements montrés ; l'écran final peut se tenir


def ecarts_images(ffmpeg: str, video: Path) -> list[float]:
    """Écart moyen entre deux images successives (10 par seconde, en petit, en gris)."""
    w, h = RYTHME_TAILLE
    r = subprocess.run([ffmpeg, "-v", "error", "-i", str(video), "-vf",
                        f"fps={RYTHME_FPS},scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[-400:])
    n, b = w * h, r.stdout
    images = [b[i:i + n] for i in range(0, len(b) - n + 1, n)]
    return [sum(abs(x - y) for x, y in zip(images[i], images[i - 1])) / n for i in range(1, len(images))]


def verdict_rythme(ecarts: list[float], fps: int = RYTHME_FPS, fin_libre: float = FIN_LIBRE) -> dict:
    """Plages figées, événements par seconde, écart médian entre deux événements, plus longs creux.
    L'écran final (les `fin_libre` dernières secondes) peut se tenir."""
    duree = len(ecarts) / fps
    limite = max(0, len(ecarts) - int(fin_libre * fps))
    figees, debut = [], None
    for i, v in enumerate(ecarts[:limite] + [SEUIL_FIGE]):
        if v < SEUIL_FIGE:
            debut = i if debut is None else debut
        elif debut is not None:
            if (i - debut) / fps >= FIGE_MAX:
                figees.append((round(debut / fps, 1), round((i - debut) / fps, 1)))
            debut = None
    pics = [i for i in range(1, len(ecarts) - 1)
            if ecarts[i] >= SEUIL_EVENEMENT and ecarts[i] >= ecarts[i - 1] and ecarts[i] >= ecarts[i + 1]]
    utiles = [i for i in pics if i < limite]
    intervalles = [(utiles[k] - utiles[k - 1]) / fps for k in range(1, len(utiles))]
    par_s = len(utiles) / (limite / fps) if limite else 0.0
    mediane = sorted(intervalles)[len(intervalles) // 2] if intervalles else round(limite / fps, 1)
    creux = sorted(((round(utiles[k - 1] / fps, 1), round((utiles[k] - utiles[k - 1]) / fps, 1))
                    for k in range(1, len(utiles)) if (utiles[k] - utiles[k - 1]) / fps > CREUX_SIGNALE),
                   key=lambda c: -c[1])
    problemes = []
    if figees:
        problemes.append("image figée : " + ", ".join(f"à {d:.1f} s pendant {l:.1f} s" for d, l in figees[:6]))
    if par_s < EVENEMENTS_MIN:
        problemes.append(f"{par_s:.2f} événement par seconde : il en faut {EVENEMENTS_MIN:.0f} au moins (une entrée, un clic, "
                         "un compteur, une coche, un recadrage toutes les demi-secondes)")
    if mediane > ECART_MEDIAN_MAX:
        problemes.append(f"{mediane:.2f} s entre deux événements en général : {ECART_MEDIAN_MAX} s au plus")
    return {"duree": round(duree, 1), "evenements_par_s": round(par_s, 2), "ecart_median": round(mediane, 2),
            "figees": figees, "creux": creux[:5], "problemes": problemes}


def cmd_rythme(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    meta = meta_de(Path(a.video)) or {}
    fin = FIN_LIBRE if not (SUPPORTS.get(meta.get("support") or "", {}).get("boucle")) else 0.0
    try:
        v = verdict_rythme(ecarts_images(ffmpeg, Path(a.video)), fin_libre=fin)
    except RuntimeError as e:
        sys.exit(f"ERREUR : lecture de la vidéo impossible : {e}")
    print(f"• {v['duree']:.0f} s · {v['evenements_par_s']:.2f} événement par seconde (≥ {EVENEMENTS_MIN:.0f}) · "
          f"écart médian {v['ecart_median']:.2f} s (≤ {ECART_MEDIAN_MAX}) · image figée : "
          f"{sum(l for _d, l in v['figees']):.1f} s")
    if v["creux"]:
        print("  plus longs creux à regarder : " + ", ".join(f"{d:.1f} s (+{l:.1f} s)" for d, l in v["creux"]))
    if v["problemes"]:
        for pb in v["problemes"]:
            print(f"✗ {pb}")
        sys.exit(1)
    print("ok : le rythme tient (ce contrôle ne dit pas si c'est beau : regarde la planche).")


# ---------------------------------------------------------------------------
# Une vidéo de référence (celle dont le client aime le style) : on en tire la grammaire
# (fonds, mots par écran, motifs, transitions, caméra), jamais le contenu.
# ---------------------------------------------------------------------------
def ytdlp(m: Path | None) -> str | None:
    """Le téléchargeur de Reel Cloneur s'il est installé (tenu à jour), sinon celui du système."""
    if m is not None:
        for sous in ("bin/yt-dlp", "Scripts/yt-dlp.exe"):
            chemin = m / ".reel-cloneur-venv" / sous
            if chemin.exists():
                return str(chemin)
    return shutil.which("yt-dlp")


def coupes_video(ffmpeg: str, video: Path, seuil: float = 0.2) -> list[float]:
    r = subprocess.run([ffmpeg, "-hide_banner", "-i", str(video), "-filter:v", f"select='gt(scene,{seuil})',showinfo",
                        "-f", "null", "-"], capture_output=True, text=True)
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]


ANALYSE_GRILLE = """
## Ce que la vidéo fait (à remplir en regardant les planches)

Chaque case de planche dure 0,5 s, de gauche à droite puis de haut en bas (24 cases = 12 s).

- **Fonds** : quelles couleurs, combien de bascules (sombre, clair, couleur pleine, écran coupé) ?
- **Mots par écran** : combien en général, et le plus long ?
- **Ce qui vit pendant qu'on lit** : caméra, objets flottants, curseur ?
- **Le motif qui revient** (un geste, un cadre, un objet qui relie les parties) :
- **Les transitions** : un objet devient le suivant, un flash depuis un clic, un volet, une coupe ?
- **Les interfaces montrées** : lesquelles, reconstruites comment, animées comment ?
- **La fin** :

## Ce qu'on reprend pour la vidéo du client

La grammaire seulement (rythme, densité, procédés), avec sa marque et son offre. Jamais le
contenu, les textes, les images ni la musique de la référence.
"""


def cmd_reference(a) -> None:
    m = maison_de(Path(a.dossier)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    dossier = Path(a.dossier).resolve()
    if not (dossier / "OFFRE.json").is_file():
        sys.exit("ERREUR : donne le dossier de la vidéo (celui qui contient OFFRE.json).")
    nom = propre(a.nom or "reference", 30)
    sortie = dossier / "sources" / "reference" / nom
    sortie.mkdir(parents=True, exist_ok=True)
    if re.match(r"https?://", a.source):
        dl = ytdlp(m)
        if not dl:
            sys.exit("ERREUR : pas de téléchargeur. Installe celui de Reel Cloneur (python3 tools/cloner_reel.py installer) "
                     "ou télécharge la vidéo toi-même et donne son chemin.")
        r = lancer([dl, "--no-playlist", "-q", "--no-warnings", "-o", str(sortie / "video.%(ext)s"), a.source])
        videos = sorted(sortie.glob("video.*"))
        if r.returncode != 0 or not videos:
            sys.exit(f"ERREUR : téléchargement impossible : {(r.stderr or '')[-300:]} Télécharge-la toi-même et donne son chemin.")
        video = videos[0]
    else:
        source = Path(a.source).expanduser()
        if not source.is_file():
            sys.exit(f"ERREUR : fichier introuvable : {source}")
        video = sortie / ("video" + source.suffix.lower())
        shutil.copy2(source, video)
    for ancien in sortie.glob("planche-*.jpg"):
        ancien.unlink()
    r = lancer([ffmpeg, "-v", "error", "-y", "-i", str(video), "-vf", "fps=2,scale=320:-2,tile=6x4:padding=4:color=gray",
                "-start_number", "1", str(sortie / "planche-%02d.jpg")])
    if r.returncode != 0:
        sys.exit(f"ERREUR : planches impossibles : {r.stderr[-300:]}")
    coupes = coupes_video(ffmpeg, video)
    v = verdict_rythme(ecarts_images(ffmpeg, video), fin_libre=0.0)
    planches = sorted(p.name for p in sortie.glob("planche-*.jpg"))
    texte = (f"# Vidéo de référence : {nom}\n\nSource : {a.source}\n\n## Mesures\n\n"
             f"- Durée : {v['duree']:.0f} s\n- Événements : {v['evenements_par_s']:.2f} par seconde, écart médian "
             f"{v['ecart_median']:.2f} s\n- Image figée : {sum(l for _d, l in v['figees']):.1f} s\n"
             f"- Coupes franches : {len(coupes)} ({', '.join(f'{t:.1f}' for t in coupes[:30])})\n"
             f"- Planches : {', '.join(planches)}\n" + ANALYSE_GRILLE)
    (sortie / "ANALYSE.md").write_text(texte, encoding="utf-8")
    print(f"• référence analysée : {sortie}")
    print(f"  {v['evenements_par_s']:.2f} événement/s, écart médian {v['ecart_median']:.2f} s, {len(coupes)} coupes franches, "
          f"{len(planches)} planches. Regarde les planches et remplis ANALYSE.md.")


# ---------------------------------------------------------------------------
# Logos et icônes, posés dans le projet (le rendu est hors ligne). Les logos des outils que
# l'offre utilise viennent de theSVG, les icônes de Lucide ; chacun est nettoyé avant d'entrer.
# ---------------------------------------------------------------------------
SOURCES_SVG = {
    "logo": "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/{nom}/{variante}.svg",
    "icone": "https://cdn.jsdelivr.net/npm/lucide-static@0.460.0/icons/{nom}.svg",
}
INTERDITS_SVG = re.compile(r"<script|<foreignObject|\son\w+\s*=|javascript:|(?:xlink:)?href\s*=\s*[\"']\s*(?:https?:|data:|//)", re.I)
MONOCHROMES = {"#fff", "#ffffff", "#000", "#000000", "#111", "#111111", "white", "black"}


def nettoyer_svg(svg: str, recolorable: bool = True) -> str:
    """SVG prêt à poser en ligne : rien d'actif, taille fluide, couleur unique passée en currentColor."""
    if INTERDITS_SVG.search(svg):
        raise ValueError("SVG refusé : il contient un script, un lien externe ou un gestionnaire d'évènement")
    svg = re.sub(r"<\?xml.*?\?>|<!--.*?-->|<title>.*?</title>|<desc>.*?</desc>", "", svg, flags=re.S)
    debut = re.search(r"<svg\b[^>]*>", svg)
    if not debut:
        raise ValueError("pas de balise <svg>")
    tete = re.sub(r'\s(?:width|height|class)="[^"]*"', "", debut.group(0))
    tete = tete.replace("<svg", '<svg width="100%" height="100%"', 1)
    svg = svg[:debut.start()] + tete + svg[debut.end():]
    couleurs = {c.lower() for c in re.findall(r'fill="([^"]+)"', svg)} - {"none", "currentcolor"}
    if recolorable and couleurs and couleurs <= MONOCHROMES:
        svg = re.sub(r'fill="([^"]+)"', lambda mm: 'fill="currentColor"' if mm.group(1).lower() in MONOCHROMES else mm.group(0), svg)
    return re.sub(r"\s*\n\s*", " ", svg).strip()


def telecharger_svg(genre: str, nom: str) -> str:
    import urllib.request
    variantes = ("default", "color", "mono") if genre == "logo" else ("",)
    for variante in variantes:
        url = SOURCES_SVG[genre].format(nom=nom, variante=variante)
        try:
            with urllib.request.urlopen(url, timeout=15) as rep:
                if rep.status == 200:
                    return rep.read().decode("utf-8", "replace")
        except Exception:
            continue
    raise ValueError(f"{genre} « {nom} » introuvable")


def ecrire_ajouts(projet: Path, ajouts: dict[str, str]) -> Path:
    fichier = projet / "kit" / "ajouts.js"
    fichier.parent.mkdir(parents=True, exist_ok=True)
    existants = {}
    if fichier.is_file():
        m = re.search(r"Object\.assign\(window\.K_ICONES \|\| \{\}, (\{.*\})\);", fichier.read_text(encoding="utf-8"), re.S)
        if m:
            existants = json.loads(m.group(1))
    existants.update(ajouts)
    fichier.write_text("/* Logos (theSVG) et icônes (Lucide, ISC) ajoutés à ce projet, nettoyés. Généré par studio_motion.py. */\n"
                       "window.K_ICONES = Object.assign(window.K_ICONES || {}, " + json.dumps(existants, ensure_ascii=False, indent=0) + ");\n",
                       encoding="utf-8")
    return fichier


def cmd_logos(a) -> None:
    projet = Path(a.projet).resolve()
    if not (projet / "index.html").is_file():
        sys.exit("ERREUR : donne le dossier d'un projet de vidéo (celui qui contient index.html).")
    ajouts, echecs = {}, []
    for brut in a.noms:
        genre, _, nom = brut.partition(":") if ":" in brut else (a.genre, "", brut)
        try:
            cle = ("logo-" if genre == "logo" else "") + nom
            ajouts[cle] = nettoyer_svg(telecharger_svg(genre, nom))
        except ValueError as e:
            echecs.append(str(e))
    if ajouts:
        f = ecrire_ajouts(projet, ajouts)
        print(f"• {len(ajouts)} ajouté(s) dans {f.relative_to(projet)} : {', '.join(ajouts)} (K.ic(\"logo-claude\"), K.ic(\"rocket\"))")
    for e in echecs:
        print(f"⚠️ {e}")
    if not ajouts:
        sys.exit(1)


# ---------------------------------------------------------------------------
# La musique calée sur la vidéo : tempo, temps forts (la grosse caisse) et entrée franche du
# morceau, puis une version ramenée au tempo de la grille (120 battements par minute = un temps
# toutes les 0,5 s) et décalée pour que l'entrée tombe à l'instant choisi de la vidéo.
# ---------------------------------------------------------------------------
MUSIQUE_SR, MUSIQUE_PAS = 11025, 110        # échantillonnage d'analyse, pas de ~10 ms


def enveloppe(ffmpeg: str, audio: Path, graves: bool = False) -> list[float]:
    """Énergie toutes les ~10 ms (mono) ; `graves` ne garde que la grosse caisse et la basse."""
    filtre = ["-af", "lowpass=f=150"] if graves else []
    r = subprocess.run([ffmpeg, "-v", "error", "-i", str(audio), *filtre, "-ac", "1", "-ar", str(MUSIQUE_SR),
                        "-f", "s16le", "-"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[-300:])
    import array
    a = array.array("h")
    a.frombytes(r.stdout[: len(r.stdout) // 2 * 2])
    if sys.byteorder == "big":
        a.byteswap()
    n = MUSIQUE_PAS
    return [math.sqrt(sum(v * v for v in a[i:i + n]) / n) for i in range(0, len(a) - n, n)]


def tempo_de(env: list[float], fps: float, bas: float = 90.0, haut: float = 150.0) -> float:
    """Tempo (battements par minute) par autocorrélation des attaques."""
    lg = [math.log(1e-3 + e) for e in env]
    att = [max(0.0, lg[i] - lg[i - 1]) for i in range(1, len(lg))]
    milieu = len(att) // 2
    seg = att[max(0, milieu - int(20 * fps)): milieu + int(20 * fps)] or att
    meilleur = (0.0, 120.0)
    bpm = bas
    while bpm <= haut:
        decal = 60 * fps / bpm
        d0, fr = int(decal), decal - int(decal)
        score = sum(seg[i] * ((1 - fr) * seg[i + d0] + fr * seg[i + d0 + 1]) for i in range(len(seg) - d0 - 1))
        if score > meilleur[0]:
            meilleur = (score, bpm)
        bpm = round(bpm + 0.1, 1)
    return meilleur[1]


def phase_de(env_graves: list[float], fps: float, bpm: float) -> float:
    """Instant du premier temps fort (s) : la grille qui ramasse le plus d'attaques de grosse caisse
    (la montée de l'énergie des graves, pas son pic, qui arrive un huitième de seconde après)."""
    lg = [math.log(1e-3 + e) for e in env_graves]
    att = [0.0] + [max(0.0, lg[i] - lg[i - 1]) for i in range(1, len(lg))]
    pas = 60 * fps / bpm
    nb = int(len(att) / pas) - 1
    meilleur = (-1.0, 0)
    for k in range(int(pas)):
        score = sum(att[int(k + j * pas)] for j in range(nb))
        if score > meilleur[0]:
            meilleur = (score, k)
    return meilleur[1] / fps


def entree_de(env: list[float], fps: float, saut_db: float = 6.0, jusqu_a: float = 40.0) -> float | None:
    """Première entrée franche (s) : la seconde dont l'énergie dépasse de `saut_db` les 3 s d'avant."""
    def db(i0: int, i1: int) -> float:
        tranche = env[max(0, i0):max(i0 + 1, i1)]
        return 20 * math.log10(1e-3 + sum(tranche) / len(tranche))
    pas = int(fps / 4)
    for i in range(int(3 * fps), min(len(env) - int(fps), int(jusqu_a * fps)), pas):
        if db(i, i + int(fps)) - db(i - int(3 * fps), i) >= saut_db:
            # au quart de seconde près, la montée la plus raide de cette seconde
            fin = max(range(i, i + int(fps) + pas, pas), key=lambda j: db(j, j + pas) - db(j - pas, j))
            return round(fin / fps, 2)
    return None


def calage(entree: float, phase: float, bpm: float, cible_bpm: float, a_t: float) -> dict:
    """Facteur de tempo et décalage pour que l'entrée (posée sur le temps fort le plus proche)
    tombe à `a_t` s dans la vidéo. decalage > 0 : on coupe le début du morceau ; < 0 : il démarre
    plus tard dans la vidéo."""
    facteur = cible_bpm / bpm if cible_bpm and 0.9 <= cible_bpm / bpm <= 1.1 else 1.0
    temps = 60 / bpm
    sur_temps = phase + round((entree - phase) / temps) * temps     # l'entrée recalée sur un temps fort
    entree_etiree = sur_temps / facteur
    return {"facteur": round(facteur, 6), "entree": round(entree_etiree, 3), "decalage": round(entree_etiree - a_t, 3)}


def cmd_musique(a) -> None:
    m = maison_de(Path(a.entree)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    source = Path(a.entree)
    fps = MUSIQUE_SR / MUSIQUE_PAS
    env, graves = enveloppe(ffmpeg, source), enveloppe(ffmpeg, source, graves=True)
    bpm = tempo_de(env, fps)
    phase = phase_de(graves, fps, bpm)
    entree = entree_de(env, fps)
    print(f"• tempo {bpm:.1f} battements par minute (un temps toutes les {60 / bpm:.3f} s), premier temps fort à {phase:.2f} s, "
          + (f"entrée franche à {entree:.2f} s" if entree is not None else "pas d'entrée franche dans les 40 premières secondes"))
    if not a.sortie:
        return
    if a.a is None or entree is None:
        sys.exit("ERREUR : donne --a <instant de la vidéo où l'entrée doit tomber> (le morceau doit avoir une entrée franche).")
    c = calage(entree, phase, bpm, a.bpm, a.a)
    filtres = []
    if c["facteur"] != 1.0:
        filtres.append(f"atempo={c['facteur']:.6f}")
    if c["decalage"] >= 0:
        filtres.append(f"atrim=start={c['decalage']:.3f},asetpts=PTS-STARTPTS")
    else:
        retard = int(round(-c["decalage"] * 1000))
        filtres.append(f"adelay={retard}|{retard}")
    if a.duree:
        filtres.append(f"atrim=duration={a.duree + 0.6:.2f}")
    r = lancer([ffmpeg, "-v", "error", "-y", "-i", str(source), "-af", ",".join(filtres), "-c:a", "pcm_s16le", str(a.sortie)])
    if r.returncode != 0:
        sys.exit(f"ERREUR : préparation impossible : {r.stderr[-300:]}")
    vitesse = f"tempo ramené à {a.bpm:g} ({(c['facteur'] - 1) * 100:+.1f} %), " if c["facteur"] != 1.0 else ""
    print(f"• {a.sortie} : {vitesse}l'entrée tombe à {a.a:g} s de la vidéo, sur un temps fort. "
          "Pose-le comme musique (sons.poser, musique_db autour de -10 sans voix).")


# ---------------------------------------------------------------------------
# L'émergence des bruitages : chacun doit dépasser la musique de 4 dB au moins (méthode du Pack
# SFX : énergie max sur 50 ms pendant le son, moins le fond musical), le fond étant pris autour
# du son (une intro calme laisse passer des sons plus doux). Lu dans le bloc SONS d'index.html.
# ---------------------------------------------------------------------------
EMERGENCE_MIN, EMERGENCE_MAX, FENETRE_50MS = 4.0, 16.0, 2400   # 50 ms à 48 kHz


def sons_poses(index: Path) -> tuple[dict | None, list[dict]]:
    """(musique, bruitages) écrits par tools/sons.py dans index.html : src, début, durée, départ dans
    le fichier, volume linéaire (le niveau porté par l'enveloppe quand il y en a une)."""
    import html as _html
    page = index.read_text(encoding="utf-8")
    musique, bruitages = None, []
    for balise in re.findall(r"<audio\b[^>]*>", page):
        attr = dict(re.findall(r'([\w-]+)="([^"]*)"', balise))
        if not attr.get("src") or attr.get("data-audio-group") != "mixage":
            continue
        vol = float(attr.get("data-volume", "1") or 1)
        if "data-automation" in attr:
            try:
                pistes = json.loads(_html.unescape(attr["data-automation"]))["lanes"]
                vol = max(pt["v"] for l in pistes if l.get("target") == "volume" for pt in l["points"])
            except (ValueError, KeyError):
                pass
        son = {"src": index.parent / attr["src"], "debut": float(attr.get("data-start", 0)),
               "duree": float(attr.get("data-duration", 0)), "depart": float(attr.get("data-media-start", 0)), "vol": vol}
        if attr.get("id") == "musique":
            musique = son
        elif not attr.get("id", "").startswith("voix"):
            bruitages.append(son)
    return musique, bruitages


def energies_50ms(echantillons) -> list[float]:
    w = FENETRE_50MS
    return [20 * math.log10(max(1e-9, math.sqrt(sum(v * v for v in echantillons[k * w:(k + 1) * w]) / w)) / 32768)
            for k in range(len(echantillons) // w)]


def verdict_emergence(e_mix: list[float], e_musique: list[float], sons: list[dict]) -> list[tuple[float, str, float]]:
    """(début, nom, émergence en dB) pour chaque bruitage. Fond = médiane de la musique sur ±1,5 s,
    jamais plus de 8 dB sous sa médiane générale."""
    tri = sorted(e_musique)
    general = tri[len(tri) // 2] if tri else -120.0
    pas = 48000 / FENETRE_50MS
    sortie = []
    for s in sons:
        k0 = int(s["debut"] * pas)
        k1 = max(k0 + 1, int((s["debut"] + min(s["duree"], 2.0)) * pas) + 1)
        autour = sorted(e_musique[max(0, k0 - 30):k0 + 30]) or [general]
        fond = max(autour[len(autour) // 2], general - 8)
        pic = max(e_mix[k0:k1]) if e_mix[k0:k1] else -120.0
        sortie.append((s["debut"], Path(s["src"]).stem, round(pic - fond, 1)))
    return sortie


def cmd_emergence(a) -> None:
    import array
    projet = Path(a.projet).resolve()
    index = projet / "index.html"
    m = maison_de(projet) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not index.is_file() or not ffmpeg:
        sys.exit("ERREUR : donne le dossier d'un projet de vidéo, avec ffmpeg installé.")
    musique, sons = sons_poses(index)
    if not sons:
        sys.exit("ERREUR : aucun bruitage posé dans index.html (bloc SONS).")
    if musique is None:
        print("• pas de musique : rien à masquer, l'émergence ne se mesure pas.")
        return
    m_ = re.search(r'data-composition-id="main"[^>]*data-duration="([\d.]+)"', index.read_text(encoding="utf-8"))
    duree = float(m_.group(1)) if m_ else max(s["debut"] + s["duree"] for s in sons)

    def piste(liste: list[dict]) -> "array.array":
        entrees, filtres = [], []
        for i, s in enumerate(liste):
            entrees += ["-i", str(s["src"])]
            filtres.append(f"[{i}:a]atrim=start={s['depart']:.3f}:duration={max(s['duree'], 0.05):.3f},asetpts=PTS-STARTPTS,"
                           f"volume={s['vol']:.4f},adelay={int(s['debut'] * 1000)}:all=1,aresample=48000[s{i}]")
        filtres.append("".join(f"[s{i}]" for i in range(len(liste))) +
                       f"amix=inputs={len(liste)}:normalize=0:dropout_transition=0,apad=whole_dur={duree:.3f},atrim=0:{duree:.3f}[a]")
        r = subprocess.run([ffmpeg, "-v", "error", *entrees, "-filter_complex", ";".join(filtres), "-map", "[a]",
                            "-ac", "1", "-ar", "48000", "-f", "s16le", "-"], capture_output=True)
        if r.returncode != 0:
            sys.exit(f"ERREUR : mixage de contrôle impossible : {r.stderr.decode('utf-8', 'replace')[-300:]}")
        x = array.array("h")
        x.frombytes(r.stdout[: len(r.stdout) // 2 * 2])
        return x

    mus, sfx = piste([musique]), piste(sons)
    n = min(len(mus), len(sfx))
    somme = [max(-32768, min(32767, mus[i] + sfx[i])) for i in range(n)]
    res = verdict_emergence(energies_50ms(somme), energies_50ms(mus[:n]), sons)
    faibles = [r for r in res if r[2] < EMERGENCE_MIN]
    forts = [r for r in res if r[2] > EMERGENCE_MAX]
    print(f"• {len(res)} bruitages : {len(res) - len(faibles) - len(forts)} s'entendent (4 à 16 dB au-dessus de la musique), "
          f"{len(faibles)} trop faibles, {len(forts)} trop forts")
    for d, nom, em in faibles:
        print(f"  faible : {d:6.2f} s {nom} ({em:+.1f} dB)")
    for d, nom, em in forts:
        print(f"  fort, à écouter : {d:6.2f} s {nom} ({em:+.1f} dB)")
    if len(faibles) > max(1, len(res) // 20):
        print("✗ trop de bruitages couverts par la musique : remonte-les (par famille) ou baisse la musique.")
        sys.exit(1)
    print("ok : les bruitages ressortent de la musique.")


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


def verdict_sonore(mesure: dict, cible: float = CIBLE_LUFS) -> list[str]:
    """Écarts à la cible de livraison : -16 LUFS (±1) par défaut, crête vraie sous -1 dBTP."""
    pb = []
    try:
        i, tp = float(mesure["input_i"]), float(mesure["input_tp"])
    except (KeyError, ValueError):
        return ["mesure illisible"]
    if math.isinf(i) or i < -60:
        return ["vidéo muette (aucun son mesurable)"]
    if abs(i - cible) > 1.0:
        pb.append(f"sonie {i:.1f} LUFS, cible {cible:.0f} ±1 : lance `studio_motion.py mastering`")
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
    pb = verdict_sonore(mesure, a.cible)
    print(f"sonie {float(mesure['input_i']):.1f} LUFS, crête {float(mesure['input_tp']):.1f} dBTP")
    print("\n".join(f"❌ {p}" for p in pb) if pb else "ok")


def chaine_mastering(gain_db: float, plafond: float = 0.7) -> str:
    """Gain puis limiteur suréchantillonné : le niveau monte, les crêtes restent sous -2 dBFS, donc
    sous -1 dBTP une fois encodées en AAC. Un loudnorm seul refuse de monter un clip court aux sons
    piqués (il protège ses crêtes) et s'arrête 2 à 3 LU sous la cible."""
    # Attaque de 0,5 ms et plafond à -2,5 dBFS : les clics du Pack SFX ont des attaques si rapides
    # qu'un limiteur à 3 ms les laissait passer à -0,9 dBTP (mesuré le 12/10/2026).
    # Second étage après le retour à 48 kHz : le filtre de rééchantillonnage recrée des crêtes
    # que l'AAC pousse ensuite jusqu'à -0,1 dBTP sur une vidéo pleine de clics.
    return (f"aresample=192000,volume={gain_db:.2f}dB,"
            "alimiter=limit=0.75:attack=0.5:release=60:level=false,aresample=48000,"
            f"alimiter=limit={plafond:.4f}:attack=0.1:release=40:level=false")


def cmd_mastering(a) -> None:
    m = maison_de(Path(a.entree)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    mesure = mesure_sonore(ffmpeg, Path(a.entree))
    if mesure is None or math.isinf(float(mesure["input_i"])):
        sys.exit("ERREUR : pas de son à masteriser (vidéo muette).")
    gain = a.cible - float(mesure["input_i"])
    apres, plafond = None, 0.7
    for _ in range(6):  # chaque passe corrige l'écart de la précédente ; deux suffisent d'habitude
        r = lancer([ffmpeg, "-v", "error", "-y", "-i", a.entree, "-c:v", "copy", "-af", chaine_mastering(gain, plafond),
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.sortie])
        if r.returncode != 0:
            sys.exit(f"ERREUR : mastering impossible : {r.stderr[-400:]}")
        apres = mesure_sonore(ffmpeg, Path(a.sortie))
        if apres is None:
            break
        ecart, crete = a.cible - float(apres["input_i"]), float(apres["input_tp"])
        if crete > PLAFOND_TP - 0.2:
            # L'AAC fait déborder les attaques très vives (clics) : on abaisse le plafond d'autant.
            plafond *= 10 ** ((PLAFOND_TP - 0.4 - crete) / 20)
            gain += max(0.0, ecart)
            continue
        if abs(ecart) <= 0.5:
            break
        gain += ecart
    if apres:
        print(f"• {a.sortie} : {float(apres['input_i']):.1f} LUFS, crête {float(apres['input_tp']):.1f} dBTP")
        pb = verdict_sonore(apres, a.cible)
        if pb:
            print("\n".join(f"❌ {p}" for p in pb))
            sys.exit(1)
    else:
        print(f"• {a.sortie}")


def cmd_preparer_video(a) -> None:
    """Prépare une vraie vidéo (un Reel du client, une capture d'écran filmée) pour une composition :
    une image clé par seconde (sinon HyperFrames saute ou fige des images au rendu), H.264, sans son
    par défaut (la vidéo de vente a sa propre bande son)."""
    m = maison_de(Path(a.entree)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    son = ["-c:a", "aac", "-b:a", "160k"] if a.avec_son else ["-an"]
    r = lancer([ffmpeg, "-v", "error", "-y", "-i", a.entree, "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                "-pix_fmt", "yuv420p", "-g", str(FPS), "-keyint_min", str(FPS), "-r", str(FPS), *son,
                "-movflags", "+faststart", a.sortie])
    if r.returncode != 0:
        sys.exit(f"ERREUR : préparation impossible : {r.stderr[-400:]}")
    print(f"• {a.sortie} : prête pour la composition (une image clé par seconde{', son gardé' if a.avec_son else ', sans son'})")


def cmd_affiche(a) -> None:
    """L'affiche d'une vidéo de page : une image de la vidéo (la première par défaut, qui doit déjà
    porter la promesse), en JPEG de moins de 100 Ko, montrée avant la lecture ou si elle est bloquée."""
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffmpeg = binaire(m, "ffmpeg")
    if not ffmpeg:
        sys.exit("ERREUR : ffmpeg introuvable.")
    for qualite in range(2, 32, 2):
        r = lancer([ffmpeg, "-v", "error", "-y", "-ss", f"{a.temps:.3f}", "-i", a.video, "-frames:v", "1",
                    "-q:v", str(qualite), a.sortie])
        if r.returncode != 0 or not Path(a.sortie).is_file():
            sys.exit(f"ERREUR : affiche impossible : {r.stderr[-400:]}")
        if Path(a.sortie).stat().st_size <= 100 * 1024:
            break
    print(f"• {a.sortie} : {Path(a.sortie).stat().st_size // 1024} Ko (image à {a.temps:.1f} s)")


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
        print("• pas de musique dans cette vidéo : elle est déjà la version sans musique, rien à faire.")
        return
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


def meta_par_nom(video: Path) -> dict | None:
    """Une vidéo de livraison/ n'a pas de meta.json : on la retrouve par son nom (reel.mp4,
    story-ouverture.mp4, page-1x1.mp4, reel-sans-musique.mp4) parmi les projets du dossier."""
    p = Path(video).resolve()
    dossier = next((d for d in (p.parent, *p.parents) if (d / "OFFRE.json").is_file()), None)
    if dossier is None:
        return None
    nom = re.sub(r"-(sans-musique|master)$", "", p.stem)
    return next((meta for _projet, meta in projets(dossier) if meta.get("video") == nom), None)


def cmd_export(a) -> None:
    m = maison_de(Path(a.video)) or maison_de(OUTILS)
    ffprobe = binaire(m, "ffprobe")
    if not ffprobe:
        sys.exit("ERREUR : ffprobe introuvable.")
    meta = meta_de(Path(a.video)) or meta_par_nom(Path(a.video)) or {}
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
    aj = s.add_parser("ajouter", help="Ajoute une vidéo (un autre support ou format) à un dossier existant.")
    aj.add_argument("dossier")
    aj.add_argument("--videos", required=True, help="support[:rôle][@format], séparés par des virgules.")
    aj.set_defaults(f=cmd_ajouter)
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
    rf = s.add_parser("reference", help="Analyse une vidéo dont le client aime le style (planches, coupes, rythme).")
    rf.add_argument("dossier", help="Le dossier de la vidéo (celui de OFFRE.json).")
    rf.add_argument("source", help="Lien (Instagram, YouTube, TikTok…) ou fichier vidéo.")
    rf.add_argument("--nom", help="Nom court de la référence (défaut : reference).")
    rf.set_defaults(f=cmd_reference)
    lo = s.add_parser("logos", help="Ajoute au projet les logos des outils montrés (theSVG) ou des icônes (Lucide).")
    lo.add_argument("projet")
    lo.add_argument("noms", nargs="+", help="claude openai notion… ; icone:rocket pour une icône Lucide.")
    lo.add_argument("--genre", default="logo", choices=("logo", "icone"))
    lo.set_defaults(f=cmd_logos)
    ry = s.add_parser("rythme", help="Mesure le rythme du MP4 : événements par seconde, images figées.")
    ry.add_argument("video")
    ry.set_defaults(f=cmd_rythme)
    pl = s.add_parser("planche", help="Planche de contrôle avec les zones dessinées.")
    pl.add_argument("video")
    pl.add_argument("--support", choices=sorted(SUPPORTS), help="Défaut : celui du projet.")
    pl.add_argument("--sticker", action="store_true", help="Dessine la zone du sticker lien (story).")
    pl.add_argument("--sans-sticker", action="store_true", help="Story sans lien : ne dessine pas la zone du sticker.")
    pl.add_argument("--temps", help="Instants en secondes, séparés par des virgules (repères + 0,3 s).")
    pl.add_argument("--sortie")
    pl.set_defaults(f=cmd_planche)
    mu = s.add_parser("musique", help="Tempo, temps forts et entrée d'un morceau ; version calée sur la vidéo.")
    mu.add_argument("entree")
    mu.add_argument("--sortie", help="Fichier WAV calé à écrire (sinon : analyse seule).")
    mu.add_argument("--a", type=float, help="Instant de la vidéo (s) où l'entrée franche doit tomber.")
    mu.add_argument("--bpm", type=float, default=120.0, help="Tempo de la grille de la vidéo (défaut 120 ; 0 = garder le sien).")
    mu.add_argument("--duree", type=float, help="Durée de la vidéo (s), pour couper le morceau.")
    mu.set_defaults(f=cmd_musique)
    em = s.add_parser("emergence", help="Vérifie que chaque bruitage posé dépasse la musique de 4 dB au moins.")
    em.add_argument("projet")
    em.set_defaults(f=cmd_emergence)
    so = s.add_parser("son", help="Mesure la sonie et la crête.")
    so.add_argument("video")
    so.add_argument("--cible", type=float, default=CIBLE_LUFS, help="Sonie visée en LUFS (défaut -16 ; -20 pour des bruitages seuls).")
    so.set_defaults(f=cmd_son)
    ma = s.add_parser("mastering", help="Met le son à -16 LUFS (ou --cible), crêtes sous -1 dBTP.")
    ma.add_argument("entree")
    ma.add_argument("sortie")
    ma.add_argument("--cible", type=float, default=CIBLE_LUFS, help="Sonie visée en LUFS (défaut -16 ; -20 pour des bruitages seuls).")
    ma.set_defaults(f=cmd_mastering)
    pv = s.add_parser("preparer-video", help="Prépare une vraie vidéo pour une composition (images clés, sans son).")
    pv.add_argument("entree")
    pv.add_argument("sortie")
    pv.add_argument("--avec-son", action="store_true")
    pv.set_defaults(f=cmd_preparer_video)
    af = s.add_parser("affiche", help="L'affiche d'une vidéo de page, en JPEG de moins de 100 Ko.")
    af.add_argument("video")
    af.add_argument("sortie")
    af.add_argument("--temps", type=float, default=0.0)
    af.set_defaults(f=cmd_affiche)
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
