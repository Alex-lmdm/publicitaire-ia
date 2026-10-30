#!/usr/bin/env python3
"""LES MUSIQUES DE LANCEMENT : 17 musiques offertes avec la formation, rangées dans ce dossier.

Le client les télécharge dans sa formation en un fichier, musiques-lancement.zip (avant le
30/10/2026 : cinq archives, une par ambiance, musiques-<ambiance>.zip). Chacun contient :
    musiques-lancement/<ambiance>/*.mp3           les morceaux (MP3 320 kbit/s) ;
    musiques-lancement/<ambiance>/catalog.json    la fiche de chacun : style, usage conseillé,
                                                  tempo, recalage à 120, premier temps, entrée
                                                  franche (la batterie qui arrive), durée ;
    musiques-lancement/LICENCE.md                 ce qu'il a le droit d'en faire.

    installer [<zip ou dossier>…]   sans argument : les musiques-*.zip du dossier Téléchargements,
                                    et les dossiers musiques-lancement* qu'un navigateur (Safari)
                                    a décompressés tout seul. Le fichier unique ou les archives
                                    par ambiance : chacune s'ajoute aux autres, refaire ne
                                    change rien.
    choisir                         les meilleures pour une vidéo, selon son but, son support, sa
                                    durée et l'instant où la batterie doit entrer.

Rangement : assets/musiques/<ambiance>/ (morceaux et fiche) et assets/musiques/LICENCE.md. Jamais
versionné (.gitignore) : la licence interdit de partager les fichiers seuls, et le dépôt est public.

Python 3.9+, bibliothèque standard seulement.
"""
from __future__ import annotations

import json
import os
import posixpath
import re
import zipfile
from pathlib import Path

DOSSIER = "assets/musiques"
EXTENSIONS = {".mp3", ".wav"}

# Les cinq ambiances de la banque, dans l'ordre de la formation.
AMBIANCES = {
    "lancement-energique": "Lancement énergique",
    "montee-cinematique": "Montée cinématique",
    "tech-minimale": "Tech minimale",
    "court-percutant": "Court et percutant",
    "premium-calme": "Premium et calme",
}

# Le but de la vidéo → les ambiances, de la plus juste à la moins juste. Pour un format court
# (Reel, pub, story), « Court et percutant » passe devant quand le but est de vendre ou de faire
# s'inscrire : un beat qui démarre tout de suite.
PAR_OBJECTIF = {
    "vente": ["lancement-energique", "montee-cinematique", "court-percutant"],
    "lancement": ["lancement-energique", "montee-cinematique", "court-percutant"],
    "nouveaute": ["montee-cinematique", "lancement-energique", "court-percutant"],
    "fonctionnalite": ["tech-minimale", "court-percutant", "premium-calme"],
    "explication": ["tech-minimale", "premium-calme", "lancement-energique"],
    "inscription": ["lancement-energique", "court-percutant", "tech-minimale"],
    "preuve": ["premium-calme", "tech-minimale", "montee-cinematique"],
}
COURTS = {"reel", "tiktok", "pub", "fil", "story"}
MUETS = {"section"}   # la boucle d'une section de page : muette, sans musique

# Les mots du client pour imposer une ambiance (« prends une musique tech minimale »).
SYNONYMES = {
    "energique": "lancement-energique", "lancement": "lancement-energique",
    "cinematique": "montee-cinematique", "montee": "montee-cinematique", "revelation": "montee-cinematique",
    "tech": "tech-minimale", "minimale": "tech-minimale", "minimal": "tech-minimale",
    "court": "court-percutant", "percutant": "court-percutant",
    "premium": "premium-calme", "calme": "premium-calme", "luxe": "premium-calme",
}

ECOUTE_AVANT = 8.0   # chaque extrait de la page d'écoute démarre 8 s avant l'entrée de la batterie


class ErreurMusiques(Exception):
    pass


def _sur(nom: str) -> str | None:
    """Un chemin d'archive sans danger (relatif, sans « .. »), normalisé ; None sinon."""
    nom = nom.replace("\\", "/")
    if nom.startswith("/") or (len(nom) > 1 and nom[1] == ":"):
        return None
    propre = posixpath.normpath(nom)
    if propre in (".", "..") or propre.startswith("../") or "/../" in f"/{propre}/":
        return None
    return propre


def selection(noms: list[str], lire) -> dict[str, str]:
    """Pour les fichiers d'une source (archive ou dossier) : {nom dans la source: chemin dans ce
    dossier}. Repère chaque ambiance par sa fiche (« <racine>/<ambiance>/catalog.json »), garde les
    morceaux qu'elle décrit, sa fiche et la licence, ignore tout le reste. `lire(nom)` rend le
    contenu d'un fichier de la source. Lève ErreurMusiques si ce ne sont pas des musiques de
    lancement, ou s'il manque un morceau décrit."""
    surs = {n: _sur(n) for n in noms if not n.endswith("/")}
    par_chemin = {p: n for n, p in surs.items() if p}
    choix: dict[str, str] = {}
    for brut, p in surs.items():
        if not p or not p.endswith("/catalog.json"):
            continue
        dossier_ambiance = posixpath.dirname(p)
        ambiance = posixpath.basename(dossier_ambiance)
        if ambiance not in AMBIANCES:
            continue
        racine = posixpath.dirname(dossier_ambiance)
        try:
            fiche = json.loads(lire(brut))
        except ValueError as e:
            raise ErreurMusiques(f"la fiche de l'ambiance {AMBIANCES[ambiance]} est illisible ({e})") from e
        morceaux = fiche.get("morceaux") or []
        if not morceaux:
            raise ErreurMusiques(f"la fiche de l'ambiance {AMBIANCES[ambiance]} ne décrit aucun morceau")
        choix[brut] = f"{DOSSIER}/{ambiance}/catalog.json"
        for m in morceaux:
            fichier = _sur(str(m.get("fichier") or ""))
            if (not fichier or posixpath.dirname(fichier) != ambiance
                    or Path(fichier).suffix.lower() not in EXTENSIONS):
                raise ErreurMusiques(f"fiche {AMBIANCES[ambiance]} : chemin de morceau invalide ({m.get('fichier')!r})")
            source = par_chemin.get(posixpath.join(racine, fichier) if racine else fichier)
            if source is None:
                raise ErreurMusiques(f"{fichier} est décrit dans la fiche mais absent : l'archive est peut-être "
                                     "abîmée, retélécharge-la dans ta formation")
            choix[source] = f"{DOSSIER}/{fichier}"
        licence = posixpath.join(racine, "LICENCE.md") if racine else "LICENCE.md"
        if licence in par_chemin:
            choix[par_chemin[licence]] = f"{DOSSIER}/LICENCE.md"
    if not choix:
        raise ErreurMusiques("ce ne sont pas des musiques de lancement : aucune fiche <ambiance>/catalog.json dedans")
    return choix


def _lire_source(source: Path) -> dict[str, bytes]:
    """{chemin dans ce dossier: contenu} pour une archive ZIP ou un dossier décompressé."""
    if source.is_dir():
        fichiers = {p.relative_to(source).as_posix(): p for p in source.rglob("*") if p.is_file()}
        # Le dossier donné peut être « musiques-lancement » lui-même, ou celui qui le contient.
        choix = selection(list(fichiers), lambda n: fichiers[n].read_bytes())
        return {dest: fichiers[nom].read_bytes() for nom, dest in choix.items()}
    try:
        with zipfile.ZipFile(source) as z:
            choix = selection(z.namelist(), z.read)
            return {dest: z.read(nom) for nom, dest in choix.items()}
    except zipfile.BadZipFile as e:
        raise ErreurMusiques(f"{source.name} n'est pas une archive ZIP lisible ({e}) : retélécharge-la") from e


def telechargements() -> Path:
    """Le dossier Téléchargements du client (Mac, Windows, Linux)."""
    if os.name == "nt" and os.environ.get("USERPROFILE"):
        return Path(os.environ["USERPROFILE"]) / "Downloads"
    return Path.home() / "Downloads"


def sources_par_defaut(dossier: Path | None = None) -> list[Path]:
    """Les archives musiques-*.zip du dossier Téléchargements (« musiques-tech-minimale (1).zip »
    compris), et les dossiers musiques-… qu'un navigateur ou Windows a décompressés (Safari en fait
    « musiques-lancement », « musiques-lancement 2 »…). Ce qui n'est pas une ambiance est ignoré."""
    d = dossier or telechargements()
    if not d.is_dir():
        return []
    trouves = [p for p in d.iterdir() if p.name.lower().startswith("musiques-")
               and ((p.is_file() and p.suffix.lower() == ".zip") or p.is_dir())]
    return sorted(trouves, key=lambda p: p.stat().st_mtime)   # le plus récent en dernier : il l'emporte


def installer(racine: Path, sources: list[Path]) -> dict:
    """Range les ambiances trouvées dans les sources (archives ou dossiers). Un fichier identique
    n'est pas réécrit ; un morceau qui n'est plus dans la fiche de son ambiance est retiré."""
    if not sources:
        raise ErreurMusiques(f"aucune archive musiques-….zip dans {telechargements()} : télécharge le "
                             "fichier des 17 musiques dans ta formation (module Musique), puis redemande")
    copies: dict[str, bytes] = {}
    erreurs = []
    for source in sources:
        source = Path(source).expanduser()
        if not source.exists():
            erreurs.append(f"{source} introuvable")
            continue
        try:
            copies.update(_lire_source(source))
        except ErreurMusiques as e:
            erreurs.append(f"{source.name} : {e}")
    if not copies:
        raise ErreurMusiques(" ; ".join(erreurs) or "rien à installer")
    ecrits = identiques = retires = 0
    for rel, donnees in sorted(copies.items()):
        cible = racine / rel
        if cible.is_file() and cible.stat().st_size == len(donnees) and cible.read_bytes() == donnees:
            identiques += 1
            continue
        cible.parent.mkdir(parents=True, exist_ok=True)
        provisoire = cible.with_name(cible.name + ".part")
        provisoire.write_bytes(donnees)
        provisoire.replace(cible)
        ecrits += 1
    for ambiance in {Path(rel).parts[2] for rel in copies if rel.endswith("/catalog.json")}:
        gardes = {posixpath.basename(m["fichier"]) for m in fiche(racine, ambiance).get("morceaux") or []}
        for f in (racine / DOSSIER / ambiance).iterdir():
            if f.is_file() and f.suffix.lower() in EXTENSIONS and f.name not in gardes:
                f.unlink()
                retires += 1
    e = etat(racine)
    if e["manquants"]:
        raise ErreurMusiques(f"installation incomplète : {len(e['manquants'])} morceau(x) absent(s) "
                             f"(ex. {', '.join(e['manquants'][:3])}) ; retélécharge l'archive de cette ambiance")
    return {**e, "ecrits": ecrits, "identiques": identiques, "retires": retires, "erreurs": erreurs}


def fiche(racine: Path, ambiance: str) -> dict:
    try:
        return json.loads((racine / DOSSIER / ambiance / "catalog.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def morceaux(racine: Path) -> list[dict]:
    """Tous les morceaux installés, avec leur ambiance (clé) et leur chemin dans ce dossier."""
    liste = []
    for ambiance in AMBIANCES:
        for m in fiche(racine, ambiance).get("morceaux") or []:
            chemin = racine / DOSSIER / m["fichier"]
            if chemin.is_file():
                liste.append({**m, "cle": ambiance, "nom_ambiance": AMBIANCES[ambiance], "chemin": chemin,
                              "id": Path(m["fichier"]).stem})
    return liste


def etat(racine: Path) -> dict:
    """Ce qui est installé, par ambiance, et ce qui manque."""
    par_ambiance, manquants = {}, []
    for ambiance in AMBIANCES:
        decrits = fiche(racine, ambiance).get("morceaux") or []
        absents = [m["fichier"] for m in decrits if not (racine / DOSSIER / m["fichier"]).is_file()]
        manquants += absents
        if decrits:
            par_ambiance[ambiance] = len(decrits) - len(absents)
    return {"installe": bool(par_ambiance), "total": sum(par_ambiance.values()), "ambiances": par_ambiance,
            "absentes": [AMBIANCES[a] for a in AMBIANCES if a not in par_ambiance], "manquants": manquants,
            "version": next((fiche(racine, a).get("version") for a in par_ambiance), None)}


def ambiance_demandee(texte: str | None) -> str | None:
    """« tech minimale », « Tech-minimale », « premium » → la clé de l'ambiance ; None si inconnue."""
    if not texte:
        return None
    plat = re.sub(r"[^a-z]+", " ", texte.lower().translate(str.maketrans("éèêàâîôûç", "eeeaaiouc"))).strip()
    if plat.replace(" ", "-") in AMBIANCES:
        return plat.replace(" ", "-")
    for mot in plat.split():
        if mot in SYNONYMES:
            return SYNONYMES[mot]
    return None


def deja_utilises(racine: Path, sauf: Path | None = None) -> dict[str, int]:
    """Combien de vidéos du client utilisent déjà chaque morceau (lu dans les SOURCE.md de ses
    projets, sauf celui de la vidéo en cours) : pour ne pas lui reproposer toujours la même musique."""
    compte: dict[str, int] = {}
    for source in (racine / "videos").glob("*/*/assets/audio/SOURCE.md"):
        if sauf and source.parents[2].resolve() == Path(sauf).resolve():
            continue
        try:
            texte = source.read_text(encoding="utf-8")
        except OSError:
            continue
        for ident in set(re.findall(r"musiques de lancement, ([a-z0-9-]+)", texte)):
            compte[ident] = compte.get(ident, 0) + 1
    return compte


def choisir(racine: Path, objectif: str = "vente", support: str = "reel", duree: float = 30.0,
            a: float | None = None, ambiance: str | None = None, exclure: set[str] | None = None,
            nombre: int = 3, projet: Path | None = None) -> list[dict]:
    """Les `nombre` meilleurs morceaux pour une vidéo, du plus juste au moins juste, avec la raison.

    - l'ambiance vient du but (et du support pour un format court), sauf si le client en impose une ;
    - le morceau doit durer assez : de son entrée franche à sa fin, la suite de la vidéo après
      l'instant `a` où la batterie doit entrer (sinon la fin serait muette) ;
    - son intro doit couvrir le début de la vidéo (entrée franche à `a` ou après), sinon la musique
      démarrerait en retard ;
    - un morceau proche de 120 battements par minute se cale sur la grille des scènes ;
    - un morceau déjà utilisé dans ses vidéos passe derrière, pour varier."""
    exclure = exclure or set()
    if a is None:
        a = min(10.0, max(3.0, round(duree * 0.2 * 2) / 2))   # le pivot, vers 20 % de la vidéo
    if ambiance:
        ordre = [ambiance] + [x for x in PAR_OBJECTIF.get(objectif, PAR_OBJECTIF["vente"]) if x != ambiance]
    else:
        ordre = list(PAR_OBJECTIF.get(objectif, PAR_OBJECTIF["vente"]))
        if support in COURTS and objectif in ("vente", "inscription"):
            ordre.remove("court-percutant")
            ordre.insert(0, "court-percutant")
    utilises = deja_utilises(racine, sauf=projet)
    notes = []
    for m in morceaux(racine):
        if m["id"] in exclure:
            continue
        rang = ordre.index(m["cle"]) if m["cle"] in ordre else len(ordre)
        if ambiance and m["cle"] != ambiance:
            continue
        # Recalé à 120, le morceau s'étire ou se resserre (au plus 10 %) : ses temps aussi.
        tempo = float(m.get("tempo_bpm") or 120)
        facteur = 120 / tempo if m.get("recale_a_120") and 0.9 <= 120 / tempo <= 1.1 else 1.0
        entree = float(m.get("entree_franche_s") or 0) / facteur
        longueur = float(m.get("duree_s") or 0) / facteur
        if longueur - entree < (duree - a) + 1.5:
            continue   # trop court : la fin de la vidéo serait muette
        note = 100.0 - 30 * rang
        retard = max(0.0, a - entree)
        note -= 6 * retard                                      # silence au début de la vidéo
        note += 8 if m.get("recale_a_120") else -8
        note -= 12 * utilises.get(m["id"], 0)
        raisons = [m["nom_ambiance"]]
        if retard > 0.5:
            raisons.append(f"démarre {retard:.1f} s après le début (intro courte)")
        if utilises.get(m["id"]):
            raisons.append(f"déjà dans {utilises[m['id']]} de tes vidéos")
        notes.append((note, m, raisons))
    notes.sort(key=lambda x: (-x[0], x[1]["id"]))
    # Au plus deux morceaux d'une même ambiance sur trois propositions, pour donner un vrai choix.
    retenus, par_ambiance = [], {}
    for note, m, raisons in notes:
        if not ambiance and par_ambiance.get(m["cle"], 0) >= max(2, nombre - 1):
            continue
        par_ambiance[m["cle"]] = par_ambiance.get(m["cle"], 0) + 1
        retenus.append({**m, "note": round(note, 1), "raisons": raisons, "a": a})
        if len(retenus) == nombre:
            break
    return retenus


def ligne(m: dict) -> str:
    """Une ligne lisible par l'agent : le morceau, son style, son entrée et sa durée."""
    tempo = f"{m.get('tempo_bpm'):.0f} bpm" + (", recalé à 120" if m.get("recale_a_120") else ", garde son tempo")
    return (f"{m['id']} · {' · '.join(m['raisons'])} · {m.get('style', '')} · batterie à "
            f"{float(m.get('entree_franche_s') or 0):.1f} s · {float(m.get('duree_s') or 0):.0f} s · {tempo}")


def page(m: dict) -> dict:
    """L'entrée de la page d'écoute : l'extrait démarre juste avant l'entrée de la batterie."""
    debut = max(0.0, float(m.get("entree_franche_s") or 0) - ECOUTE_AVANT)
    return {"nom": f"{m['nom_ambiance']} · {m.get('style', '')}",
            "detail": f"la batterie entre à {float(m.get('entree_franche_s') or 0):.0f} s ; "
                      f"l'extrait démarre {ECOUTE_AVANT:.0f} s avant",
            "url": m["chemin"].resolve().as_uri() + (f"#t={debut:.1f}" if debut else "")}
