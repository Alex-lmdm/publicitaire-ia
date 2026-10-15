#!/usr/bin/env python3
"""HEYGEN : la bibliothèque de musiques et les voix de synthèse de HeyGen, avec le compte du client.

Ce que ça coûte :
    la recherche de musiques et l'écoute des voix sont gratuites (aucun débit, vérifié le
    14/10/2026 : le solde ne bouge pas) ;
    une voix de synthèse est payante, prélevée sur son solde HeyGen (environ 0,04 $ la minute,
    tarif Starfish de l'API ; HeyGen n'offre plus de crédit d'API depuis février 2026, il faut
    recharger quelques dollars). `parler` annonce le coût et refuse sans `confirme=True`.

La clé : la variable HEYGEN_API_KEY, sinon ~/.heygen/credentials, le fichier du CLI heygen (le même
que lit le skill media-use de HyperFrames : une seule connexion pour tout). Le client la copie dans
son compte HeyGen (Settings > API), une seule fois.

Par l'API directement, pas par le CLI heygen : il n'existe pas sous Windows.
Python 3.9+, bibliothèque standard seulement.
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.heygen.com"
FICHIER_CLE = Path.home() / ".heygen" / "credentials"
PAGE_CLE = "https://app.heygen.com/settings?nav=API"
PRIX_VOIX_MINUTE = 0.04          # dollars, tarif Starfish de l'API HeyGen (octobre 2026)
MOTS_PAR_SECONDE = 2.5           # débit d'une voix off française
FORME_CLE = re.compile(r"[A-Za-z0-9_\-=+/.]{20,200}")


class ErreurHeygen(Exception):
    pass


# ---------------------------------------------------------------------------
# La clé
# ---------------------------------------------------------------------------
def _lire_fichier_cle() -> str | None:
    try:
        texte = FICHIER_CLE.read_text(encoding="utf-8").strip()
    except OSError:
        return None
    return texte if FORME_CLE.fullmatch(texte) else None


def cle() -> str | None:
    env = (os.environ.get("HEYGEN_API_KEY") or "").strip()
    return env or _lire_fichier_cle()


def source_cle() -> str | None:
    """D'où vient la clé, pour le dire au client (jamais la clé elle-même)."""
    if (os.environ.get("HEYGEN_API_KEY") or "").strip():
        return "la variable HEYGEN_API_KEY"
    if _lire_fichier_cle():
        return "~/.heygen/credentials"
    if FICHIER_CLE.is_file():
        return "oauth"          # connecté par `heygen auth login --oauth` : pas de clé lisible ici
    return None


def appel(methode: str, chemin: str, params: dict | None = None, corps: dict | None = None,
          cle_api: str | None = None, delai: float = 30) -> dict:
    cle_api = cle_api or cle()
    if not cle_api:
        raise ErreurHeygen("pas de compte HeyGen relié : `heygen connecter <clé>` (la clé se copie sur "
                           f"{PAGE_CLE})")
    url = API + chemin + ("?" + urllib.parse.urlencode(params) if params else "")
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None
    entetes = {"X-Api-Key": cle_api, "Accept": "application/json", "User-Agent": "publicitaire-ia"}
    if donnees is not None:
        entetes["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=donnees, method=methode, headers=entetes)
    try:
        with urllib.request.urlopen(req, timeout=delai) as rep:
            return json.loads(rep.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        if e.code in (401, 403):
            raise ErreurHeygen("HeyGen refuse la clé (elle a peut-être été régénérée) : recopie-la sur "
                               f"{PAGE_CLE}, puis `heygen connecter <clé>`") from None
        if e.code == 402 or "insufficient" in detail.lower() or "balance" in detail.lower():
            raise ErreurHeygen("solde HeyGen insuffisant pour cette génération : il se recharge sur "
                               "https://app.heygen.com (Settings > API, quelques dollars suffisent)") from None
        raise ErreurHeygen(f"HeyGen a répondu {e.code} : {detail}") from None
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise ErreurHeygen(f"HeyGen injoignable ({e}) : vérifie la connexion internet, puis réessaie") from None


def solde(cle_api: str | None = None) -> float | None:
    donnees = appel("GET", "/v3/users/me", cle_api=cle_api).get("data") or {}
    montant = (donnees.get("wallet") or {}).get("remaining_balance")
    return float(montant) if isinstance(montant, (int, float)) else None


def verifier_cle(cle_api: str) -> None:
    """Un appel gratuit (une recherche d'un morceau) : la clé est-elle acceptée ?"""
    appel("GET", "/v3/audio/sounds", {"query": "upbeat", "type": "music", "limit": 1}, cle_api=cle_api)


def enregistrer_cle(cle_api: str, remplacer: bool = False) -> Path:
    cle_api = cle_api.strip()
    if not FORME_CLE.fullmatch(cle_api):
        raise ErreurHeygen("ce n'est pas une clé HeyGen (une suite de lettres et de chiffres, sans espace) : "
                           f"recopie-la sur {PAGE_CLE}")
    verifier_cle(cle_api)
    if FICHIER_CLE.is_file() and FICHIER_CLE.read_text(encoding="utf-8").strip() != cle_api and not remplacer:
        raise ErreurHeygen("une autre connexion HeyGen existe déjà sur cet ordinateur (~/.heygen/credentials). "
                           "Demande au client s'il veut la remplacer, puis relance avec --remplacer")
    FICHIER_CLE.parent.mkdir(parents=True, exist_ok=True)
    FICHIER_CLE.write_text(cle_api + "\n", encoding="utf-8")
    if os.name != "nt":
        os.chmod(FICHIER_CLE, 0o600)
    return FICHIER_CLE


# ---------------------------------------------------------------------------
# Musiques (gratuit)
# ---------------------------------------------------------------------------
def chercher_musiques(requete: str, nombre: int = 8, duree_min: float | None = None,
                      score_min: float = 0.6, genre: str = "music") -> list[dict]:
    """Les morceaux (ou, genre="sound_effects", les bruitages) les plus proches de la description
    (en anglais), au moins aussi longs que `duree_min`. Gratuit."""
    trouves, jeton = [], None
    for _ in range(4):
        params = {"query": requete, "type": genre, "limit": 50, "min_score": score_min}
        if jeton:
            params["token"] = jeton
        rep = appel("GET", "/v3/audio/sounds", params)
        for piste in rep.get("data") or []:
            if duree_min and (piste.get("duration") or 0) < duree_min:
                continue
            trouves.append(piste)
            if len(trouves) >= nombre:
                return trouves
        jeton = rep.get("next_token")
        if not rep.get("has_more") or not jeton:
            break
    return trouves


# ---------------------------------------------------------------------------
# Voix (écoute gratuite, génération payante)
# ---------------------------------------------------------------------------
def voix_disponibles(langue: str = "fr", genre: str | None = None, nombre: int = 12) -> list[dict]:
    params = {"engine": "starfish", "type": "public", "language": langue, "limit": min(100, max(nombre, 1))}
    if genre:
        params["gender"] = genre
    return (appel("GET", "/v3/voices", params).get("data") or [])[:nombre]


def mots(texte: str) -> int:
    return len(re.findall(r"\w+(?:['’]\w+)?", texte))


def cout_voix(texte: str, vitesse: float = 1.0) -> tuple[float, float]:
    """(secondes estimées, dollars estimés) d'une voix de synthèse."""
    secondes = max(1.0, mots(texte) / MOTS_PAR_SECONDE / max(vitesse, 0.5))
    return round(secondes, 1), max(0.01, round(secondes / 60 * PRIX_VOIX_MINUTE, 2))


def parler(texte: str, voix: str, vitesse: float = 1.0, langue: str = "fr", confirme: bool = False) -> dict:
    """Génère la voix (payant). Renvoie {audio_url, duration, word_timestamps}."""
    if not confirme:
        secondes, dollars = cout_voix(texte, vitesse)
        raise ErreurHeygen(f"génération payante : environ {secondes:g} s de voix, environ {dollars:.2f} $ prélevés "
                           "sur le solde HeyGen du client. Annonce-lui ce coût, attends son accord, puis relance "
                           "avec --confirme")
    if len(texte) > 5000:
        raise ErreurHeygen("texte trop long pour une seule génération (5 000 caractères au plus) : découpe-le")
    corps = {"text": texte, "voice_id": voix, "speed": vitesse, "language": langue}
    return appel("POST", "/v3/voices/speech", corps=corps, delai=180).get("data") or {}


# ---------------------------------------------------------------------------
# Fichiers
# ---------------------------------------------------------------------------
def extension(url: str, defaut: str) -> str:
    """L'extension du fichier d'un lien signé (.wav, .mp3), sans ses paramètres."""
    suffixe = Path(urllib.parse.urlparse(url).path).suffix.lower()
    return suffixe if re.fullmatch(r"\.[a-z0-9]{2,4}", suffixe) else defaut


def telecharger(url: str, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    temp = dest.with_name(dest.name + ".part")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "publicitaire-ia"}),
                                    timeout=120) as rep, open(temp, "wb") as f:
            while True:
                bloc = rep.read(1 << 16)
                if not bloc:
                    break
                f.write(bloc)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        temp.unlink(missing_ok=True)
        raise ErreurHeygen(f"téléchargement impossible ({e}) : le lien a peut-être expiré (7 jours), "
                           "relance la recherche") from None
    temp.replace(dest)
    return dest


def page_ecoute(titre: str, consigne: str, pistes: list[dict], dest: Path) -> Path:
    """Une page à ouvrir dans le navigateur : un lecteur par piste, numérotée, pour que le client
    écoute et réponde par un numéro. pistes = [{"numero", "nom", "detail", "url"}]."""
    lignes = []
    for p in pistes:
        lignes.append(
            f'<li><span class="n">{int(p["numero"])}</span><div><b>{html.escape(str(p["nom"]))}</b>'
            f'<small>{html.escape(str(p.get("detail", "")))}</small>'
            f'<audio controls preload="none" src="{html.escape(str(p["url"]), quote=True)}"></audio></div></li>')
    contenu = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<style>
:root {{ color-scheme: dark; }}
body {{ margin: 0; background: #111214; color: #f2f2f2; font: 16px/1.45 -apple-system, "Segoe UI", Inter, sans-serif; }}
main {{ max-width: 760px; margin: 0 auto; padding: 32px 16px 64px; }}
h1 {{ font-size: 26px; margin: 0 0 6px; }} p {{ color: #b8b8bd; margin: 0 0 24px; }}
ol {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }}
li {{ display: flex; gap: 16px; align-items: center; background: #1b1c20; border-radius: 14px; padding: 14px 16px; }}
.n {{ flex: none; width: 44px; height: 44px; border-radius: 50%; background: #FFEE00; color: #111;
      display: grid; place-items: center; font-weight: 800; font-size: 19px; }}
li div {{ flex: 1; min-width: 0; display: grid; gap: 6px; }}
small {{ color: #9a9aa0; }} audio {{ width: 100%; }}
</style></head><body><main><h1>{html.escape(titre)}</h1><p>{html.escape(consigne)}</p>
<ol>{"".join(lignes)}</ol></main></body></html>
"""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(contenu, encoding="utf-8")
    return dest


def ouvrir(fichier: Path) -> bool:
    """Ouvre la page dans le navigateur du client. Faux si ce n'est pas possible ici."""
    try:
        if sys.platform == "darwin":
            return subprocess.run(["open", str(fichier)], capture_output=True).returncode == 0
        if os.name == "nt":
            os.startfile(str(fichier))  # type: ignore[attr-defined]
            return True
        return subprocess.run(["xdg-open", str(fichier)], capture_output=True).returncode == 0
    except (OSError, AttributeError):
        return False
