#!/usr/bin/env python3
"""LA VOIX OFF : le texte juste calé sur le temps de chaque mot, et les respirations.

Appelé par `studio_motion.py voix caler` et `voix respiration` (references/voix.md, section E).

- caler : la reconnaissance vocale (Parakeet) donne de bons temps mais pas toujours les bons mots.
  Sur une voix Google AI Studio en français (essai du 03/11/2026, voix Nika), elle écrivait
  « It's » pour « C'est », « Cloud » pour « Claude », et sautait des mots entiers (120 mots
  reconnus sur 131). On garde le texte validé (`work/voix.txt`) et on prend à la transcription
  les temps des mots qui concordent ; un mot remplacé reprend le temps de celui d'en face, un mot
  sauté se place entre ses voisins, au prorata de sa longueur ; un début de mot qui tombe dans
  un silence de la voix est recalé à la fin de ce silence.
- respiration : une voix de synthèse ne laisse presque aucune pause (3,2 mots par seconde sur
  l'essai). Pour que la musique entre dans un trou au moment clé, on ouvre un silence dans le
  fichier de la voix, au milieu de la pause la plus proche, et on décale la suite des mots.
"""
from __future__ import annotations

import difflib
import json
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path

import sons


class Erreur(Exception):
    pass


def norme(mot: str) -> str:
    """Le mot sans accents, sans ponctuation, en minuscules : « Créée. » → « creee »."""
    sans = unicodedata.normalize("NFD", mot.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", sans)


def mots_du_texte(texte: str) -> list[str]:
    """Les mots du texte validé, ponctuation collée au mot d'avant (« offre ? » → un mot)."""
    texte = texte.replace("« ", "«").replace(" »", "»")
    mots = []
    for t in texte.split():
        if norme(t) or not mots:
            mots.append(t)
        else:
            mots[-1] += " " + t          # « ? », « ! », « : » seuls : collés au mot d'avant
    return [m.replace("«", "« ").replace("»", " »") for m in mots]


def caler(texte: str, transcription: list[dict], silences: list[tuple[float, float]] | None = None) -> list[dict]:
    """Le texte juste, mot par mot, avec les temps de la transcription. Rend [{id, text, start, end}]."""
    mots = mots_du_texte(texte)
    if not mots:
        raise Erreur("le texte de la voix est vide (work/voix.txt).")
    reco = [w for w in transcription if norme(str(w.get("text", "")))]
    if not reco:
        raise Erreur("la transcription est vide : relance `npx hyperframes transcribe … --engine parakeet --language fr`.")
    a, b = [norme(m) for m in mots], [norme(str(w["text"])) for w in reco]
    temps: list[tuple[float, float] | None] = [None] * len(mots)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                w = reco[j1 + k]
                temps[i1 + k] = (float(w["start"]), float(w["end"]))
        elif op == "replace" and j2 > j1:
            # n mots du texte pour m mots reconnus : la plage reconnue se partage au prorata
            debut, fin = float(reco[j1]["start"]), float(reco[j2 - 1]["end"])
            _repartir(temps, mots, i1, i2, debut, fin)
    # les mots sautés : entre leurs voisins, au prorata de leur longueur
    i = 0
    while i < len(mots):
        if temps[i] is not None:
            i += 1
            continue
        j = i
        while j < len(mots) and temps[j] is None:
            j += 1
        debut = temps[i - 1][1] if i > 0 else max(0.0, (temps[j][0] if j < len(mots) else 0.0) - 0.3 * (j - i))
        fin = temps[j][0] if j < len(mots) else debut + 0.3 * (j - i)
        _repartir(temps, mots, i, j, debut, max(fin, debut + 0.08 * (j - i)))
        i = j
    sortie = []
    for k, (m, (s, e)) in enumerate(zip(mots, temps)):
        for a0, b0 in silences or []:
            if a0 + 0.05 < s < b0 - 0.02:
                s = b0                                   # un début de mot dans un silence : à sa fin
        sortie.append({"id": f"w{k}", "text": m, "start": round(s, 2), "end": round(max(e, s + 0.08), 2)})
    for x, y in zip(sortie, sortie[1:]):                 # jamais deux mots qui se chevauchent
        if y["start"] < x["start"]:
            y["start"] = x["start"]
        if x["end"] > y["start"]:
            x["end"] = y["start"]
        if x["end"] <= x["start"]:
            x["end"] = round(x["start"] + 0.05, 2)
            y["start"] = max(y["start"], x["end"])
    return sortie


def _repartir(temps, mots, i1, i2, debut: float, fin: float) -> None:
    poids = [max(len(norme(m)), 1) for m in mots[i1:i2]]
    total, t = sum(poids), debut
    for k, p in enumerate(poids):
        d = (fin - debut) * p / total
        temps[i1 + k] = (t, t + d)
        t += d


def caler_projet(projet: Path) -> dict:
    """Écrit assets/audio/transcript.json avec le texte de work/voix.txt (la transcription brute est
    gardée dans transcript-brut.json). Rend {"mots", "concordants", "places"}."""
    audio = projet / "assets" / "audio"
    t_f, txt = audio / "transcript.json", projet / "work" / "voix.txt"
    brut = audio / "transcript-brut.json"
    if not txt.is_file():
        raise Erreur("work/voix.txt introuvable : le texte validé de la voix.")
    if not (t_f.is_file() or brut.is_file()):
        raise Erreur("assets/audio/transcript.json introuvable : transcris d'abord la voix (voix.md, section E).")
    if not brut.is_file():
        shutil.copy2(t_f, brut)
    reco = json.loads(brut.read_text(encoding="utf-8"))
    voix = audio / "voix.wav"
    calees = caler(txt.read_text(encoding="utf-8"), reco, sons.silences(voix) if voix.is_file() else None)
    t_f.write_text(json.dumps(calees, ensure_ascii=False, indent=2), encoding="utf-8")
    a = [norme(m["text"]) for m in calees]
    b = [norme(str(w.get("text", ""))) for w in reco if norme(str(w.get("text", "")))]
    concordants = sum(m.size for m in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    return {"mots": len(calees), "reconnus": len(b), "concordants": concordants}


def respiration(projet: Path, instant: float, secondes: float = 1.5) -> dict:
    """Ouvre une respiration de `secondes` dans assets/audio/voix.wav, à la pause la plus proche de
    `instant` (secondes du fichier de la voix) : le silence est allongé en son milieu et les mots
    suivants de transcript.json reculent d'autant. L'ancienne voix reste dans voix-avant-respiration.wav."""
    audio = projet / "assets" / "audio"
    voix = audio / "voix.wav"
    if not voix.is_file():
        raise Erreur("assets/audio/voix.wav introuvable.")
    pauses = sons.silences(voix, duree_min=0.2)
    if not pauses:
        raise Erreur("aucune pause dans la voix : choisis un autre instant.")
    a, b = min(pauses, key=lambda p: abs((p[0] + p[1]) / 2 - instant))
    if abs((a + b) / 2 - instant) > 1.5:
        raise Erreur(f"aucune pause à moins de 1,5 s de {instant:.2f} s : la plus proche est {a:.2f} → {b:.2f} s.")
    ajout = round(secondes - (b - a), 3)
    if ajout <= 0:
        return {"pause": (a, b), "ajout": 0.0}
    milieu = round((a + b) / 2, 3)
    avant = audio / "voix-avant-respiration.wav"
    if not avant.exists():
        shutil.copy2(voix, avant)
    tmp = audio / "_voix-respiration.wav"
    r = subprocess.run([sons.outil("ffmpeg"), "-v", "error", "-y", "-i", str(voix), "-filter_complex",
                        f"[0:a]atrim=0:{milieu},asetpts=PTS-STARTPTS[a];aevalsrc=0:d={ajout}:s=48000[s];"
                        f"[0:a]atrim={milieu},asetpts=PTS-STARTPTS[b];[a][s][b]concat=n=3:v=0:a=1[o]",
                        "-map", "[o]", "-ar", "48000", "-c:a", "pcm_s16le", str(tmp)], capture_output=True, text=True)
    if r.returncode != 0:
        raise Erreur(f"ffmpeg : {r.stderr.strip()[-300:]}")
    tmp.replace(voix)
    for nom in ("transcript.json", "transcript-brut.json"):
        f = audio / nom
        if f.is_file():
            mots = json.loads(f.read_text(encoding="utf-8"))
            for w in mots:
                if float(w["start"]) >= milieu:
                    w["start"] = round(float(w["start"]) + ajout, 2)
                    w["end"] = round(float(w["end"]) + ajout, 2)
            f.write_text(json.dumps(mots, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"pause": (round(a, 2), round(b, 2)), "ajout": ajout, "duree": round(sons.duree(voix), 2)}
