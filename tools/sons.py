#!/usr/bin/env python3
"""SONS DANS LA VIDÉO : pose les bruitages et la musique d'un projet dans son index.html (bloc SONS).

Repris de Monteur IA (même éditeur) et appelé par `studio_motion.py sons` : c'est ce qui permet au
bouton Export de l'app HyperFrames (ou à `npm run render`) de sortir la vidéo complète, et à
l'app d'afficher chaque son comme un clip de la timeline. « Reel » désigne ici le projet d'une vidéo.

    import sons
    sons.poser(reel, evenements, musique=..., voix_off=..., ecart=(18, 8), entree=None, ecraser=False)

Un évènement est un dict : {"src": Path, "start": s, "vol": dB, "trim": (t0, t1) | None,
"fondu_entree": s, "fondu_sortie": s, "af": filtre ffmpeg | None}. Ce que HyperFrames ne sait pas
faire lui-même (variante « af » : accélérer, inverser…, musique trop courte à boucler) est
préparé en fichier par ffmpeg dans assets/sons/, puis posé tel quel. Un son déjà rangé dans
assets/ du Reel (trouvé dans l'app par find_sound_effect ou find_music) y reste : pas de copie.

Réglages repris de l'ancien mixage ffmpeg, mesurés à 0,3 dB près sur un vrai Reel :
volume en dB -> data-volume ; fondus en enveloppe data-automation ; voix, sons et musique sur le
bus « mixage ». Depuis HyperFrames 0.9, l'enveloppe MULTIPLIE data-volume (elle le remplaçait en
0.8) : data-volume porte le niveau le plus haut du son, l'enveloppe sa forme, de 0 à 1
(`niveau_et_forme`). Écrire le niveau dans les deux le comptait deux fois : la musique du
premier Reel rendu en 0.9 (08/11/2026) sortait 24 dB sous le niveau voulu.

Sans voix, la musique porte la vidéo : son niveau ne se choisit plus au jugé, il se mesure
(`MUSIQUE_SANS_VOIX_LUFS`), et les bruitages se règlent par rapport à elle (`emergence`).

Niveau final : sur ce bus, un gain amène le mixage entier (voix comprise, mesuré par ffmpeg au
moment de la pose) à -16 LUFS, le niveau des Reels qu'on croise sur Instagram ; puis un plafond à
-1,5 dB garde les crêtes sous -1 dBTP une fois la vidéo encodée. Les volumes de la voix, des sons
et de la musique, calibrés sur une voix vers -24 LUFS (sortie d'Adobe Podcast), ne changent pas
entre eux : tout monte ensemble. Sans ce gain, un Reel sortait vers -24 LUFS, deux fois moins fort
à l'oreille que ses voisins du fil.

Protection : le bloc porte une empreinte. Retouché à la main ou dans l'app, il n'est plus réécrit
sans `ecraser=True`.
"""
from __future__ import annotations

import hashlib
import html
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

LIMITE_DB = -1.5        # plafond des crêtes : marge pour l'encodage AAC (crête vraie <= -1 dBTP)
CIBLE_LUFS = -16.0      # niveau final d'un Reel
GAIN_MAX_DB = 12.0      # bornes du gain d'HyperFrames (-60 à +12 dB) ; au-delà, un mixage presque muet
FONDU_MUSIQUE = (0.4, 1.2)
# Sans voix, la musique seule se pose à ce niveau avant le mastering (la vidéo de démonstration :
# un morceau de Mixkit à -17 dB, vers -30 LUFS), quel que soit le morceau : un morceau drill
# mastérisé fort (-12 LUFS) et une musique douce (-20 LUFS) sonnent alors pareil sous les mêmes
# bruitages. `mastering` remonte ensuite le tout à -16 LUFS.
MUSIQUE_SANS_VOIX_LUFS = -30.0
MUSIQUE_TROP_BASSE = 3.0     # dB sous la référence : la musique ne porte plus la vidéo
BLOC_RE = re.compile(r"( *)<!-- SONS:DEBUT[^>]*empreinte (\w+) -->\n(.*?)\n *<!-- SONS:FIN -->", re.S)
PLACE = "<!-- SONS -->"   # emplacement posé par le gabarit de chaque vidéo


class Erreur(Exception):
    pass


def outil(nom: str) -> str:
    """ffmpeg / ffprobe : celui du PATH, sinon Homebrew (Mac), sinon le lien winget (Windows) ; les
    mêmes endroits que `studio_motion.py verifier`, pour que « ✅ ffmpeg » veuille dire « ça marche »."""
    trouve = shutil.which(nom)
    if trouve:
        return trouve
    for dossier in ("/opt/homebrew/bin", "/usr/local/bin"):
        if (Path(dossier) / nom).exists():
            return str(Path(dossier) / nom)
    winget = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Links" / f"{nom}.exe"
    return str(winget) if winget.exists() else nom


def empreinte(contenu: str) -> str:
    return hashlib.sha1(contenu.encode("utf-8")).hexdigest()[:10]


def duree(path: Path) -> float:
    out = subprocess.run([outil("ffprobe"), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          str(path)], capture_output=True, encoding="utf-8", errors="replace").stdout.strip()
    try:
        return float(out)
    except ValueError:
        raise Erreur(f"durée illisible : {path}")


def lin(db: float) -> float:
    return round(10 ** (db / 20), 4)


def _attr_json(obj) -> str:
    return html.escape(json.dumps(obj, separators=(",", ":")), quote=True)


def _enveloppe(points) -> str:
    return _attr_json({"version": 1, "lanes": [{"target": "volume", "points": points}]})


def niveau_et_forme(points) -> tuple[float, list[dict]]:
    """(data-volume, points de l'enveloppe) pour des points de volume linéaires : HyperFrames 0.9
    multiplie data-volume par l'enveloppe (« A volume lane multiplies data-volume », vérifié par un
    rendu le 08/11/2026 : 0,5 sous une enveloppe à 0,5 sort à -12 dB). Le plus haut niveau va dans
    data-volume (c'est lui que l'app montre et règle), l'enveloppe garde la forme, de 0 à 1."""
    haut = max((float(p["v"]) for p in points), default=0.0)
    if haut <= 0:
        return 0.0, [{"t": p["t"], "v": 0} for p in points]
    return round(haut, 4), [{"t": p["t"], "v": round(float(p["v"]) / haut, 4)} for p in points]


def _audio_avec_enveloppe(points) -> str:
    """Les attributs data-volume et data-automation d'un son à enveloppe."""
    haut, forme = niveau_et_forme(points)
    return f'data-volume="{haut}" data-automation="{_enveloppe(forme)}"'


def sonie(src: Path, total: float) -> float | None:
    """La sonie intégrée (LUFS) d'un fichier sur ses `total` premières secondes, à plein volume."""
    return mesurer([{"src": src, "start": 0.0, "duree": total, "media_start": 0.0, "volume": 1.0}], total)


def _nom(src: Path, sfx_dir: Path | None, prefixe: str = "") -> str:
    try:
        base = "-".join(src.relative_to(sfx_dir).parts) if sfx_dir else src.name
    except ValueError:
        base = src.name
    return f"{prefixe}{base}"


def _dans_le_reel(reel: Path, src: Path) -> str | None:
    """Le chemin d'un son déjà rangé dans assets/ du Reel (relatif au Reel), sinon None."""
    try:
        rel = src.resolve().relative_to((reel / "assets").resolve())
    except ValueError:
        return None
    return f"assets/{rel.as_posix()}"


def _src(chemin: str) -> str:
    return html.escape(chemin, quote=True)


def _copie(src: Path, dest: Path) -> None:
    if not dest.exists() or dest.stat().st_size != src.stat().st_size:
        shutil.copy2(src, dest)


def _ffmpeg(args) -> None:
    r = subprocess.run([outil("ffmpeg"), "-y", "-v", "error", *args], capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise Erreur(f"ffmpeg a échoué : {r.stderr[-600:]}")


def lire_lufs(sortie_ffmpeg: str) -> float | None:
    """La loudness intégrée du résumé d'ebur128 (dernière valeur « I: … LUFS »), sinon None."""
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", sortie_ffmpeg)
    return float(m[-1]) if m else None


def gain_final(niveau: float | None) -> float:
    """Le gain (dB) qui amène un mixage de ce niveau à CIBLE_LUFS ; 0 s'il est illisible ou muet."""
    if niveau is None or niveau < -60:
        return 0.0
    return round(max(-GAIN_MAX_DB, min(GAIN_MAX_DB, CIBLE_LUFS - niveau)), 1)


def _canaux(src: Path) -> int:
    out = subprocess.run([outil("ffprobe"), "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels",
                          "-of", "csv=p=0", str(src)], capture_output=True, encoding="utf-8", errors="replace").stdout
    try:
        return int(out.strip().split(",")[0])
    except ValueError:
        return 2


def mesurer(pistes, total: float) -> float | None:
    """Loudness intégrée (LUFS) des pistes sommées comme sur le bus, avant gain ; None si ffmpeg échoue.
    Une piste : {"src": Path, "start": s, "duree": s | None, "media_start": s, "volume": linéaire,
    "fondu_entree": s, "fondu_sortie": s}. Les enveloppes sont approchées par des fondus linéaires :
    seule compte la loudness de l'ensemble, pas celle d'un instant. Une source mono est jouée à plein
    niveau sur les deux canaux, comme le fait le rendu HyperFrames (vérifié avec 0.8.136 ; ffmpeg,
    lui, la répartirait à -3 dB)."""
    if not pistes:
        return None
    entrees, filtres = [], []
    for i, p in enumerate(pistes):
        entrees += ["-i", str(p["src"])]
        stereo = "pan=stereo|c0=c0|c1=c0" if _canaux(p["src"]) == 1 else "aformat=channel_layouts=stereo"
        f = f"[{i}:a]atrim=start={p['media_start']:.3f}"
        if p.get("duree"):
            f += f":duration={p['duree']:.3f}"
        f += f",asetpts=PTS-STARTPTS,aformat=sample_rates=48000,{stereo},volume={p['volume']}"
        if p.get("fondu_entree"):
            f += f",afade=t=in:st=0:d={p['fondu_entree']:.3f}"
        if p.get("fondu_sortie") and p.get("duree"):
            f += f",afade=t=out:st={max(p['duree'] - p['fondu_sortie'], 0):.3f}:d={p['fondu_sortie']:.3f}"
        filtres.append(f + f",adelay={int(round(p['start'] * 1000))}:all=1[p{i}]")
    filtres.append("".join(f"[p{i}]" for i in range(len(pistes)))
                   + f"amix=inputs={len(pistes)}:normalize=0:dropout_transition=0,atrim=0:{total:.3f},ebur128[m]")
    r = subprocess.run([outil("ffmpeg"), "-nostats", "-hide_banner", *entrees, "-filter_complex", ";".join(filtres),
                        "-map", "[m]", "-f", "null", "-"], capture_output=True, encoding="utf-8", errors="replace")
    return lire_lufs(r.stderr) if r.returncode == 0 else None


# ---------------------------------------------------------------------------
# La musique sous une voix off (recherche du 03/11/2026, references/son.md « La musique sous la
# voix ») : pendant la parole, la musique se tient à un écart mesuré sous la voix (18 LU sur une
# page de vente, 15 dans un Reel), quel que soit le morceau ; elle remonte seulement dans les vraies
# respirations (1,5 s et plus), avant le premier mot et après le dernier, et finit en fondu doux.
# Le ducking est une enveloppe calculée d'avance sur les pauses de la voix, jamais un compresseur
# (celui de ffmpeg baisse selon le niveau de chaque mot et mange la première syllabe).
# ---------------------------------------------------------------------------
PAUSE_MIN = 1.45        # une pause plus courte ne fait pas remonter la musique (pompage)
SEUIL_SILENCE = -45.0   # dB : sous ce niveau, la voix se tait (silencedetect)
CREUX_DB = 10.0         # le creux juste avant l'entrée franche de la musique, dans une respiration
FONDU_FIN_VOIX = 2.0    # s : le fondu final d'une vidéo avec voix (courbe douce, jamais linéaire)
LIMITE_VOIX_DB = -2.0   # plafond des crêtes avec une voix : marge pour les plateformes qui réencodent


def silences(src: Path, seuil: float = SEUIL_SILENCE, duree_min: float = 0.25) -> list[tuple[float, float]]:
    """Les silences d'un fichier (début, fin), en secondes du fichier."""
    r = subprocess.run([outil("ffmpeg"), "-nostats", "-hide_banner", "-i", str(src), "-af",
                        f"silencedetect=n={seuil}dB:d={duree_min}", "-f", "null", "-"],
                       capture_output=True, encoding="utf-8", errors="replace")
    debuts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    fins = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(debuts, fins + [duree(src)] * (len(debuts) - len(fins))))


def blocs_de_parole(voix: Path, debut: float, total: float) -> tuple[list, list]:
    """(blocs, trous) en temps de la vidéo : un bloc est une suite de mots dont les pauses font moins
    de PAUSE_MIN ; un trou est une respiration d'au moins PAUSE_MIN entre deux blocs."""
    longueur = duree(voix)
    parle, t = [], 0.0
    for a, b in silences(voix):
        if a > t + 0.05:
            parle.append((t, a))
        t = max(t, b)
    if t < longueur - 0.05:
        parle.append((t, longueur))
    if not parle:
        return [], []
    blocs = [list(parle[0])]
    for a, b in parle[1:]:
        if a - blocs[-1][1] < PAUSE_MIN:
            blocs[-1][1] = b
        else:
            blocs.append([a, b])
    blocs = [(round(min(a + debut, total), 3), round(min(b + debut, total), 3)) for a, b in blocs]
    trous = [(blocs[i][1], blocs[i + 1][0]) for i in range(len(blocs) - 1)]
    return blocs, trous


def court_terme(src: Path) -> list[tuple[float, float]]:
    """La sonie court terme (fenêtre de 3 s) toutes les 100 ms : [(t, LUFS)]."""
    r = subprocess.run([outil("ffmpeg"), "-nostats", "-hide_banner", "-i", str(src), "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, encoding="utf-8", errors="replace")
    return [(float(t), float(s)) for t, s in re.findall(r"t:\s*([\d.]+).*?S:\s*(-?[\d.]+)", r.stderr)]


def reference_musique(musique: Path, blocs) -> float | None:
    """La sonie de référence du morceau sous la voix : le 90e centile de sa sonie court terme sur
    les instants où la voix parle (sa section la plus forte sous la voix tient ainsi l'écart)."""
    valeurs = sorted(s for t, s in court_terme(musique) if s > -70 and any(a + 1.5 <= t <= b for a, b in blocs))
    if not valeurs:
        valeurs = sorted(s for _t, s in court_terme(musique) if s > -70)
    return valeurs[int(0.9 * (len(valeurs) - 1))] if valeurs else None


def enveloppe_sous_voix(blocs, trous, total: float, v_sous: float, v_sans: float,
                        entree: float | None = None) -> list[dict]:
    """Les points de volume de la musique (linéaires), en secondes de la vidéo : basse sous la voix,
    au niveau « sans voix » avant le premier mot (s'il arrive après 1,5 s), dans les respirations et
    après le dernier mot. Une entrée franche de la musique qui tombe dans une respiration est
    précédée d'un creux (le temps fort sonne plus fort par contraste)."""
    pts = [(0.0, 0.0)]
    if not blocs:
        return [{"t": 0, "v": 0}, {"t": round(min(FONDU_MUSIQUE[0], total), 3), "v": v_sous}, {"t": round(total, 3), "v": v_sous}]
    premier = blocs[0][0]
    if premier >= 1.5:
        pts += [(FONDU_MUSIQUE[0], v_sans), (premier - 0.3, v_sans), (premier, v_sous)]
    else:
        pts += [(min(FONDU_MUSIQUE[0], max(premier, 0.05)), v_sous)]
    creux = v_sous * 10 ** (-CREUX_DB / 20)
    for a, b in trous:
        if entree is not None and a + 0.1 < entree < b - 0.4:
            pts += [(a, v_sous), (a + 0.05, creux), (entree, creux), (entree + 0.05, v_sans), (b - 0.3, v_sans), (b, v_sous)]
        elif b - a >= 2.5:
            pts += [(a + 0.4, v_sous), (a + 1.2, v_sans), (b - 0.3, v_sans), (b, v_sous)]
        else:
            pts += [(a + 0.1, v_sous), (a + 0.35, v_sans), (b - 0.3, v_sans), (b, v_sous)]
    fin_voix = blocs[-1][1]
    remontee = fin_voix + 1.2                  # maintien 0,4 s après le dernier mot, remontée en 0,8 s
    if remontee <= total - 0.8:                # place pour remonter, puis un fondu d'au moins 0,8 s
        debut_fondu = max(total - FONDU_FIN_VOIX, remontee)
        pts += [(fin_voix + 0.4, v_sous), (remontee, v_sans), (debut_fondu, v_sans)]
        haut = v_sans
    else:
        debut_fondu = max(total - FONDU_FIN_VOIX, fin_voix + 0.4)
        pts += [(debut_fondu, v_sous)]
        haut = v_sous
    d = max(total - debut_fondu, 0.05)
    for k in (1, 2, 3, 4):                     # fondu final en quart de sinus (approché en 4 pas)
        x = k / 4
        pts.append((debut_fondu + d * x, haut * math.sin((1 - x) * math.pi / 2) ** 2))
    propres, t_prec = [], -1.0
    for t, v in pts:
        t = round(min(max(t, 0.0), total), 3)
        if t <= t_prec:
            t = round(t_prec + 0.001, 3)
        if t > total:
            continue
        propres.append({"t": t, "v": round(v, 4)})
        t_prec = t
    return propres


def pistes_du_master(reel: Path, page: str) -> list[dict]:
    """Les pistes du master qui passent par le bus « mixage » hors du bloc SONS : la voix."""
    pistes = []
    for balise in re.findall(r"<audio\b[^>]*>", BLOC_RE.sub("", page)):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', balise))
        src = reel / html.unescape(a["src"]) if a.get("src") else None
        if a.get("data-audio-group") != "mixage" or not src or not src.is_file():
            continue
        try:
            pistes.append({"src": src, "start": float(a.get("data-start") or 0),
                           "duree": float(a["data-duration"]) if a.get("data-duration") else None,
                           "media_start": float(a.get("data-media-start") or 0),
                           "volume": float(a.get("data-volume") or 1)})
        except ValueError:
            continue
    return pistes


def _preparer_variante(e, dossier: Path, sfx_dir: Path | None) -> tuple[str, float]:
    """Une variante « af » : le segment rogné, transformé par ffmpeg, en WAV. -> (nom, durée)."""
    t0, t1 = e.get("trim") or (0.0, None)
    signature = hashlib.sha1(f"{e['src']}|{t0}|{t1}|{e['af']}".encode()).hexdigest()[:8]
    nom = f"{Path(_nom(e['src'], sfx_dir)).stem}-variante-{signature}.wav"
    dest = dossier / nom
    if not dest.exists():
        coupe = ["-ss", f"{t0:.3f}"] + (["-to", f"{t1:.3f}"] if t1 else [])
        _ffmpeg([*coupe, "-i", str(e["src"]), "-af", str(e["af"]), "-ar", "48000", "-ac", "2", str(dest)])
    return nom, duree(dest)


def _preparer_musique(musique: Path, dossier: Path, total: float, reel: Path) -> str:
    """La musique (chemin pour src), bouclée en WAV si elle est plus courte que la vidéo ; sinon
    copiée telle quelle, ou laissée en place si elle est déjà dans assets/ du Reel."""
    if duree(musique) >= total:
        sur_place = _dans_le_reel(reel, musique)
        if sur_place:
            return sur_place
        nom = f"musique-{musique.name}"
        _copie(musique, dossier / nom)
        return f"assets/sons/{nom}"
    nom = f"musique-{musique.stem}-boucle-{int(total * 1000)}.wav"
    if not (dossier / nom).exists():
        _ffmpeg(["-stream_loop", "-1", "-i", str(musique), "-t", f"{total:.3f}", "-ar", "48000", str(dossier / nom)])
    return f"assets/sons/{nom}"


def lignes(reel: Path, evenements, musique: Path | None, musique_db: float | None, total: float,
           sfx_dir: Path | None = None, voix=(), rapport: dict | None = None,
           voix_off: dict | None = None, ecart: tuple[float, float] = (18.0, 8.0),
           entree: float | None = None) -> list[str]:
    """Les éléments du bloc SONS (copie ou prépare chaque son dans assets/sons/ du Reel).
    voix : les pistes du master hors bloc (pistes_du_master), mesurées avec les sons pour régler
    le niveau final ; sans voix audible, pas de gain. voix_off : {"src": Path, "start": s, "vol": dB},
    la voix off posée dans le bloc (Publicitaire IA), mesurée elle aussi comme une voix. rapport :
    rempli avec le niveau mesuré et le gain posé.
    Avec une voix off, la musique suit `enveloppe_sous_voix` : `ecart` = (écart sous la voix pendant
    la parole, écart quand elle se tait), en LU ; son niveau se mesure sur le morceau, sauf
    `musique_db` donné (réglage manuel, il prime). `entree` : l'instant de l'entrée franche."""
    dossier = reel / "assets" / "sons"
    dossier.mkdir(parents=True, exist_ok=True)
    out, voix = [], list(voix)
    if voix_off:
        src = Path(voix_off["src"])
        if not src.exists():
            raise Erreur(f"voix introuvable : {src}")
        chemin = _dans_le_reel(reel, src)
        if not chemin:
            _copie(src, dossier / src.name)
            chemin = f"assets/sons/{src.name}"
        start = round(max(float(voix_off.get("start") or 0), 0.0), 3)
        garde = round(min(duree(src), max(total - start, 0.0)), 3)
        v = lin(float(voix_off.get("vol") or 0))
        out.append(f'<audio id="voix" src="{_src(chemin)}" data-start="{start:.3f}" data-duration="{garde:.3f}" '
                   f'data-media-start="0" data-volume="{v}" data-track-index="18" data-audio-group="mixage"></audio>')
        voix.append({"src": reel / chemin, "start": start, "duree": garde, "media_start": 0.0, "volume": v})
    pistes = list(voix)
    if musique:
        chemin = _preparer_musique(musique, dossier, total, reel)
        fe, fs = min(FONDU_MUSIQUE[0], total / 4), min(FONDU_MUSIQUE[1], total / 3)
        if voix_off:
            # sous une voix off : niveau mesuré sur le morceau, enveloppe calée sur les pauses
            blocs, trous = blocs_de_parole(Path(voix_off["src"]), float(voix_off.get("start") or 0), total)
            jouee = mesurer([voix[-1]], total) if voix else None     # la voix off, posée en dernier
            ref = reference_musique(reel / chemin, blocs)
            if musique_db is None:
                musique_db = (jouee - ecart[0] - ref) if (jouee is not None and ref is not None) else -26.5
            v = lin(musique_db)
            v_sans = lin(musique_db + ecart[0] - ecart[1])
            pts = enveloppe_sous_voix(blocs, trous, total, v, v_sans, entree)
            fs = FONDU_FIN_VOIX
            if rapport is not None:
                rapport["musique"] = {"gain": round(musique_db, 1), "ecart": ecart[0], "respirations": len(trous),
                                      "voix": jouee, "reference": ref}
        else:
            # sans voix : la musique porte la vidéo, posée à la référence quel que soit le morceau
            morceau = sonie(reel / chemin, total)
            manuel = musique_db is not None
            if not manuel:
                musique_db = (max(-40.0, min(GAIN_MAX_DB, MUSIQUE_SANS_VOIX_LUFS - morceau))
                              if morceau is not None and morceau > -70 else -17.0)
            v = lin(musique_db)
            pts = [{"t": 0, "v": 0}, {"t": round(fe, 3), "v": v},
                   {"t": round(total - fs, 3), "v": v}, {"t": round(total, 3), "v": 0}]
            if rapport is not None:
                rapport["musique_seule"] = {"gain": round(musique_db, 1), "manuel": manuel,
                                            "niveau": round(morceau + musique_db, 1) if morceau is not None else None,
                                            "reference": MUSIQUE_SANS_VOIX_LUFS}
        out.append(f'<audio id="musique" src="{_src(chemin)}" '
                   f'data-start="0" data-duration="{round(total, 3)}" data-media-start="0" '
                   f'data-track-index="19" data-audio-group="mixage" {_audio_avec_enveloppe(pts)}></audio>')
        pistes.append({"src": reel / chemin, "start": 0.0, "duree": total, "media_start": 0.0, "volume": v,
                       "fondu_entree": fe, "fondu_sortie": fs})
    fins = []   # une piste par son qui se chevauche : deux clips sur la même piste, l'un disparaît
    for n, e in enumerate(sorted(evenements, key=lambda x: x["start"]), start=1):
        src = Path(e["src"])
        if not src.exists():
            raise Erreur(f"son introuvable : {src}")
        if e.get("af"):
            nom, garde = _preparer_variante(e, dossier, sfx_dir)
            chemin, debut = f"assets/sons/{nom}", 0.0
        else:
            chemin = _dans_le_reel(reel, src)
            if not chemin:
                nom = _nom(src, sfx_dir)
                _copie(src, dossier / nom)
                chemin = f"assets/sons/{nom}"
            complet = duree(src)
            t0, t1 = e.get("trim") or (0.0, complet)
            debut, garde = t0, min(t1, complet) - t0
        garde = round(garde, 3)
        start = round(max(float(e["start"]), 0.0), 3)
        piste = next((i for i, fin in enumerate(fins) if fin <= start), None)
        if piste is None:
            piste = len(fins)
            fins.append(start + garde)
        else:
            fins[piste] = start + garde
        v = lin(float(e["vol"]))
        ligne = (f'<audio id="sfx-{n:02d}" src="{_src(chemin)}" data-start="{start:.3f}" '
                 f'data-duration="{garde:.3f}" data-media-start="{debut:.3f}" '
                 f'data-track-index="{20 + piste}" data-audio-group="mixage"')
        fe, fs = float(e.get("fondu_entree") or 0), float(e.get("fondu_sortie") or 0)
        if fe or fs:
            pts = [{"t": 0, "v": 0 if fe else v}]
            if fe:
                pts.append({"t": round(min(fe, garde), 3), "v": v})
            if fs:
                pts.append({"t": round(max(garde - fs, 0), 3), "v": v})
                pts.append({"t": garde, "v": 0})
            ligne += f" {_audio_avec_enveloppe(pts)}"
        else:
            ligne += f' data-volume="{v}"'
        out.append(ligne + "></audio>")
        pistes.append({"src": reel / chemin, "start": start, "duree": garde, "media_start": debut, "volume": v,
                       "fondu_entree": fe, "fondu_sortie": fs})
    # Gain seulement si une voix s'entend : sans elle (Reel muet, vidéo d'exemple), le niveau reste
    # celui d'aujourd'hui plutôt que de pousser la musique seule de 12 dB.
    voix_audible = bool(voix) and (mesurer(list(voix), total) or -99.0) > -50
    niveau = mesurer(pistes, total) if voix_audible else None
    gain = gain_final(niveau)
    if rapport is not None:
        rapport.update(niveau=niveau, gain=gain, cible=CIBLE_LUFS)
    limite = LIMITE_VOIX_DB if voix_off else LIMITE_DB
    if rapport is not None:
        rapport["limite"] = limite
    chaine = {"version": 1, "nodes": [
        {"type": "gain", "id": "n0", "label": "Niveau final", "params": {"gain": gain}},
        {"type": "limiter", "id": "n1", "label": "Plafond", "params": {"limit": limite}}]}
    return [f'<hf-audio-group id="mixage" data-label="Mixage" data-fx-chain="{_attr_json(chaine)}"></hf-audio-group>',
            *out]


def poser(reel: Path, evenements, musique: Path | None = None, musique_db: float | None = None,
          total: float | None = None, sfx_dir: Path | None = None, ecraser: bool = False,
          voix_off: dict | None = None, ecart: tuple[float, float] = (18.0, 8.0),
          entree: float | None = None) -> dict:
    """Écrit le bloc SONS dans reel/index.html. Lève Erreur si le bloc a été retouché (sauf ecraser).
    Rend {"niveau": LUFS mesuré avant gain | None, "gain": dB, "cible": LUFS}."""
    index = reel / "index.html"
    if not index.exists():
        raise Erreur("index.html manquant : ce dossier n'est pas un projet de vidéo.")
    page = index.read_text(encoding="utf-8")
    existant = BLOC_RE.search(page)
    if existant:
        indent = existant.group(1)
        if empreinte(existant.group(3)) != existant.group(2) and not ecraser:
            raise Erreur("les sons ont ete retouches a la main ou dans l'app depuis leur pose : modifie-les "
                         "directement dans index.html, ou relance avec --ecraser pour repartir de la liste.")
    elif PLACE in page:
        indent = re.search(rf"( *){re.escape(PLACE)}", page).group(1)
    else:
        raise Erreur("emplacement des sons introuvable dans index.html : remets la ligne <!-- SONS --> "
                     "juste avant la fin de la composition principale.")
    if total is None:
        m = re.search(r'data-composition-id="main"[^>]*data-duration="([\d.]+)"', page)
        if not m:
            raise Erreur("durée du montage introuvable dans index.html.")
        total = float(m.group(1))
    rapport = {}
    contenu = "\n".join(indent + l for l in lignes(reel, evenements, musique, musique_db, total, sfx_dir,
                                                    voix=pistes_du_master(reel, page), rapport=rapport,
                                                    voix_off=voix_off, ecart=ecart, entree=entree))
    bloc = (f"{indent}<!-- SONS:DEBUT genere par tools/sons.py, empreinte {empreinte(contenu)} -->\n"
            f"{contenu}\n{indent}<!-- SONS:FIN -->")
    page = (page[:existant.start()] + bloc + page[existant.end():]) if existant \
        else page.replace(f"{indent}{PLACE}", bloc, 1)
    index.write_text(page, encoding="utf-8")
    return rapport


def resume_musique_seule(m: dict) -> str:
    """La ligne de la musique sans voix : son niveau, et l'alerte si un réglage manuel l'enterre."""
    if m.get("niveau") is None:
        return f"\n  Musique : {m['gain']:+.1f} dB (sonie du morceau illisible)."
    ligne = (f"\n  Musique : {m['gain']:+.1f} dB, à {m['niveau']:.1f} LUFS avant le mastering "
             f"(référence sans voix {m['reference']:.0f} LUFS{', réglage manuel' if m['manuel'] else ''}) : "
             "les bruitages se règlent sur elle (`emergence`).")
    if m["niveau"] < m["reference"] - MUSIQUE_TROP_BASSE:
        ligne += (f"\n⚠️  Musique {m['reference'] - m['niveau']:.1f} dB sous la référence : elle ne porte plus la vidéo. "
                  "Retire « musique_db » et baisse plutôt les bruitages trop forts.")
    return ligne


def resume_niveau(rapport: dict) -> str:
    """Une ligne pour le récapitulatif de la pose."""
    m = rapport.get("musique")
    musique = (f"\n  Musique sous la voix : {m['gain']:+.1f} dB, {m['ecart']:.0f} LU sous la voix pendant qu'elle parle, "
               f"remontée dans {m['respirations']} respiration(s), avant le premier mot et après le dernier.") if m else ""
    if rapport.get("musique_seule"):
        musique += resume_musique_seule(rapport["musique_seule"])
    if rapport.get("niveau") is None:
        return "Niveau final : non mesuré (pas de voix audible, ou mesure impossible), aucun gain posé." + musique
    return (f"Niveau final : mixage mesuré à {rapport['niveau']:.1f} LUFS, gain {rapport['gain']:+.1f} dB "
            f"(visé {rapport['cible']:.0f} LUFS, crêtes plafonnées à {rapport.get('limite', LIMITE_DB)} dB)." + musique)


if __name__ == "__main__":
    sys.exit("Module partagé : utilise `python3 tools/studio_motion.py sons <projet> <sons.json>`.")
