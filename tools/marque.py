#!/usr/bin/env python3
"""MARQUE : les couleurs, les polices et le logo du client, d'où qu'ils viennent.

Au premier /studio, une seule question sur la source :
    page     le lien de sa page de vente : HTML et CSS lus, capture HyperFrames si elle marche ;
    images   des images ou des captures : palette mesurée sur leurs pixels ;
    video    une vidéo dont il aime le style : palette mesurée sur ses images, planche à regarder ;
    monteur  son dossier Monteur IA : couleurs, polices, mot-clé et musique repris, sans rien y écrire.

Le résultat s'écrit dans marque.json (racine du dossier), puis `ecrire_style` génère
brand/tokens.css, brand/fonts.css et brand/fonts/ : ce que chaque vidéo copie à sa création.

Les fonctions de décision sont pures (testées) ; les téléchargements et ffmpeg restent en bordure.
Python 3.9+, bibliothèque standard seulement.
"""
from __future__ import annotations

import colorsys
import datetime
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")
MAX_PAGE, MAX_CSS, MAX_FEUILLES = 4 * 1024 * 1024, 4 * 1024 * 1024, 10

# Style de départ (« Papier ») tant que la marque n'est pas réglée : noir et blanc, sans identité
# empruntée. Les polices livrées dans assets/fonts/ (licence SIL OFL).
DEFAUT = {"fond": "#f7f7f5", "texte": "#131313", "accent": "#131313", "surface": "#e8e8e4",
          "secondaire": None, "titres": "Anton", "corps": "Inter"}
POLICES_GENERIQUES = {"system-ui", "-apple-system", "blinkmacsystemfont", "ui-sans-serif", "sans-serif", "serif",
                      "ui-monospace", "monospace", "ui-serif", "arial", "helvetica", "helvetica neue",
                      "segoe ui", "roboto", "times new roman", "georgia", "courier new", "inherit", "initial"}
# Logos d'outils tiers souvent présents sur une page de vente : jamais pris pour le logo du client.
MARQUES_TIERCES = ("instagram", "facebook", "meta", "tiktok", "youtube", "linkedin", "twitter", "x-logo",
                   "whatsapp", "claude", "anthropic", "openai", "chatgpt", "gemini", "google", "apple", "stripe",
                   "paypal", "visa", "mastercard", "notion", "canva", "capcut", "figma", "slack", "discord",
                   "zoom", "shopify", "wordpress", "systeme", "trustpilot", "amex", "klarna")


class ErreurMarque(Exception):
    pass


# ---------------------------------------------------------------------------
# Couleurs
# ---------------------------------------------------------------------------
NOMMEES = {"white": "#ffffff", "black": "#000000", "transparent": None}


def hex_norme(valeur) -> str | None:
    """#abc, #aabbcc, #aabbccdd, rgb()/rgba(), white/black -> #aabbcc ; None si illisible ou transparent."""
    if valeur is None:
        return None
    v = str(valeur).strip().lower()
    if v in NOMMEES:
        return NOMMEES[v]
    m = re.fullmatch(r"#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            if len(h) == 4 and h[3] == "0":
                return None
            h = "".join(c * 2 for c in h[:3])
        elif len(h) == 8:
            if h[6:] == "00":
                return None
            h = h[:6]
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        alpha = m.group(4)
        if alpha is not None:
            a = float(alpha[:-1]) / 100 if alpha.endswith("%") else float(alpha)
            if a < 0.5:
                return None
        return "#" + "".join(f"{min(255, round(float(x))):02x}" for x in m.groups()[:3])
    return None


def rgb(h: str) -> tuple[int, int, int]:
    h = hex_norme(h) or "#000000"
    return int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)


def vers_hex(c) -> str:
    return "#" + "".join(f"{max(0, min(255, round(x))):02x}" for x in c)


def luminance(h: str) -> float:
    def canal(v: int) -> float:
        s = v / 255
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(h)
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def melange(a: str, b: str, t: float) -> str:
    ra, rb = rgb(a), rgb(b)
    return vers_hex(x + (y - x) * t for x, y in zip(ra, rb))


def lisible_sur(fond: str, candidats=("#ffffff", "#111111")) -> str:
    return max((c for c in candidats if c), key=lambda c: contraste(fond, c))


def saturation(h: str) -> float:
    r, g, b = (x / 255 for x in rgb(h))
    _h, l, s = colorsys.rgb_to_hls(r, g, b)
    return s if 0.08 < l < 0.95 else 0.0


def chromatique(h: str) -> bool:
    """Une vraie couleur (pas un gris, pas presque noir ni presque blanc) : candidate à l'accent."""
    r, g, b = rgb(h)
    return saturation(h) >= 0.35 and (max(r, g, b) - min(r, g, b)) >= 40


def distance(a: str, b: str) -> float:
    return sum((x - y) ** 2 for x, y in zip(rgb(a), rgb(b))) ** 0.5


def teinte(h: str) -> float:
    r, g, b = (x / 255 for x in rgb(h))
    return colorsys.rgb_to_hls(r, g, b)[0] * 360


def ecart_teinte(a: str, b: str) -> float:
    d = abs(teinte(a) - teinte(b)) % 360
    return min(d, 360 - d)


def regrouper(scores: dict[str, float], rayon: float = 48) -> list[tuple[str, float]]:
    """Fusionne les nuances proches (le jaune du bouton et celui de son survol) : chaque groupe est
    représenté par sa couleur la mieux notée et porte la somme des notes. Trié du meilleur au moins bon."""
    groupes: list[list] = []
    for couleur, note in sorted(scores.items(), key=lambda kv: -kv[1]):
        for g in groupes:
            if distance(g[0], couleur) <= rayon:
                g[1] += note
                break
        else:
            groupes.append([couleur, note])
    return sorted(((c, round(n, 3)) for c, n in groupes), key=lambda x: -x[1])


def choisir_couleurs(indices: dict) -> dict:
    """Décide fond, texte, accent et secondaire à partir des indices d'une page.

    indices : {"sections": [(type, fond)], "couleurs": [hex par fréquence], "titres": [hex],
               "boutons": [hex], "theme": [hex], "masque": hex | None, "variables": {nom: hex},
               "frequences_css": {hex: n}}
    Rend {"fond", "texte", "accent", "secondaire", "raisons": [...]}."""
    raisons = []
    sections = [(t, hex_norme(c)) for t, c in indices.get("sections") or [] if hex_norme(c)]
    couleurs = [c for c in (hex_norme(x) for x in indices.get("couleurs") or []) if c]
    theme = [c for c in (hex_norme(x) for x in indices.get("theme") or []) if c]
    fond = None
    hero = next((c for t, c in sections if t == "hero"), None)
    if hero:
        fond, raison = hero, "fond de la première section de la page"
    elif sections:
        fond, raison = sections[0][1], "fond de la première section"
    elif theme:
        fond, raison = min(theme, key=luminance), "couleur de thème de la page"
    else:
        neutres = [c for c in couleurs if not chromatique(c)]
        frequences = indices.get("frequences_css") or {}
        neutres += sorted((c for c in frequences if not chromatique(c)), key=lambda c: -frequences[c])
        fond, raison = (neutres[0], "couleur neutre la plus présente") if neutres else (DEFAUT["fond"], "style de départ")
    raisons.append(f"fond {fond} : {raison}")

    titres = [c for c in (hex_norme(x) for x in indices.get("titres") or []) if c]
    texte = next((c for c in titres if contraste(c, fond) >= 4.5 and not chromatique(c)), None)
    if texte:
        raisons.append(f"texte {texte} : couleur des titres sur ce fond")
    else:
        texte = lisible_sur(fond)
        raisons.append(f"texte {texte} : le plus lisible sur le fond")

    scores: dict[str, float] = {}

    def noter(c, points):
        c = hex_norme(c)
        if c and chromatique(c):
            scores[c] = scores.get(c, 0.0) + points

    noter(indices.get("masque"), 5)                     # couleur de l'icône d'onglet (mask-icon)
    for nom, c in (indices.get("variables") or {}).items():
        n = nom.lower()
        if re.search(r"(primary|brand|accent|main|marque)", n):
            if not re.search(r"\d", n):
                noter(c, 4)
            elif re.search(r"-(400|500|600)$", n):
                noter(c, 2)
    for t, c in sections:
        noter(c, 3)
    for c in indices.get("boutons") or []:
        noter(c, 3)
    for c in titres:
        noter(c, 1)
    for rang, c in enumerate(couleurs):
        noter(c, 1.0 - rang / max(1, len(couleurs)))
    frequences = indices.get("frequences_css") or {}
    if frequences:
        plus = max(frequences.values())
        for c, n in frequences.items():
            noter(c, 0.8 * n / plus)
    classes = regrouper(scores)
    if classes:
        accent = classes[0][0]
        raisons.append(f"accent {accent} : la couleur vive la plus utilisée par la marque")
    else:
        accent = texte
        raisons.append(f"accent {accent} : aucune couleur vive sur la page, marque en noir et blanc")
    secondaire = next((c for c, n in classes[1:] if n >= 2 and ecart_teinte(c, accent) >= 40), None)
    if secondaire:
        raisons.append(f"secondaire {secondaire} : deuxième couleur vive de la page")
    return {"fond": fond, "texte": texte, "accent": accent, "secondaire": secondaire, "raisons": raisons}


# ---------------------------------------------------------------------------
# Palette mesurée sur des pixels (images, images d'une vidéo)
# ---------------------------------------------------------------------------
def palette_pixels(pixels: bytes, taille_case: int = 16) -> list[tuple[str, float]]:
    """Couleurs dominantes d'une suite de pixels RGB (3 octets chacun) : (hex moyen, part de l'image)."""
    cases: dict[tuple, list] = {}
    n = len(pixels) // 3
    for i in range(n):
        r, g, b = pixels[3 * i], pixels[3 * i + 1], pixels[3 * i + 2]
        cle = (r // taille_case, g // taille_case, b // taille_case)
        c = cases.setdefault(cle, [0, 0, 0, 0])
        c[0] += r
        c[1] += g
        c[2] += b
        c[3] += 1
    brut = {vers_hex((c[0] / c[3], c[1] / c[3], c[2] / c[3])): c[3] / max(1, n) for c in cases.values()}
    return regrouper(brut, rayon=40)


def couleurs_depuis_palette(palette: list[tuple[str, float]]) -> dict:
    """fond = la couleur qui couvre le plus ; accent = la couleur vive la plus présente (1 % au moins)."""
    raisons = []
    if not palette:
        raise ErreurMarque("aucun pixel lisible")
    fond = palette[0][0]
    raisons.append(f"fond {fond} : couvre {palette[0][1] * 100:.0f} % des images")
    texte = lisible_sur(fond)
    raisons.append(f"texte {texte} : le plus lisible sur le fond")
    vives = [(c, p) for c, p in palette if chromatique(c) and p >= 0.01 and distance(c, fond) > 60]
    if vives:
        accent = vives[0][0]
        raisons.append(f"accent {accent} : la couleur vive la plus présente ({vives[0][1] * 100:.0f} %)")
    else:
        accent = texte
        raisons.append(f"accent {accent} : pas de couleur vive, marque en noir et blanc")
    secondaire = next((c for c, p in vives[1:] if p >= 0.01 and ecart_teinte(c, accent) >= 40), None)
    if secondaire:
        raisons.append(f"secondaire {secondaire} : deuxième couleur vive")
    return {"fond": fond, "texte": texte, "accent": accent, "secondaire": secondaire, "raisons": raisons}


def pixels_image(ffmpeg: str, fichier: Path, cote: int = 64) -> bytes:
    """L'image réduite (cote × cote au plus), en RGB brut, par ffmpeg."""
    r = subprocess.run([ffmpeg, "-v", "error", "-i", str(fichier), "-frames:v", "1", "-vf",
                        f"scale={cote}:{cote}:force_original_aspect_ratio=decrease,format=rgb24",
                        "-f", "rawvideo", "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise ErreurMarque(f"image illisible : {fichier.name}")
    return r.stdout


def pixels_video(ffmpeg: str, fichier: Path, images: int = 12, cote: int = 64) -> bytes:
    """Des images réparties sur toute la vidéo, réduites, en RGB brut."""
    duree = duree_media(ffmpeg, fichier) or 30.0
    pas = max(0.5, duree / images)
    r = subprocess.run([ffmpeg, "-v", "error", "-i", str(fichier), "-vf",
                        f"fps=1/{pas:.3f},scale={cote}:{cote}:force_original_aspect_ratio=decrease,format=rgb24",
                        "-frames:v", str(images), "-f", "rawvideo", "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise ErreurMarque(f"vidéo illisible : {fichier.name}")
    return r.stdout


def duree_media(ffmpeg: str, fichier: Path) -> float | None:
    r = subprocess.run([ffmpeg, "-hide_banner", "-i", str(fichier)], capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else None


# ---------------------------------------------------------------------------
# La page de vente : HTML et CSS
# ---------------------------------------------------------------------------
def telecharger(url: str, limite: int = MAX_PAGE, accepte: str = "*/*") -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accepte, "Accept-Language": "fr,en;q=0.5"})
    try:
        with urllib.request.urlopen(req, timeout=20) as rep:
            return rep.read(limite + 1)[:limite], rep.headers.get("Content-Type", "")
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise ErreurMarque(f"{url} : {e}") from e


def attributs(balise: str) -> dict[str, str]:
    return {k.lower(): v for k, _q, v in re.findall(r"([\w:-]+)\s*=\s*([\"'])(.*?)\2", balise, re.S)}


def lire_html(html: str, base: str) -> dict:
    """Ce que le HTML dit de la marque : feuilles de style, styles en ligne, couleur de thème, couleur
    de l'icône d'onglet, logos candidats (du plus sûr au moins sûr), titre et nom du site."""
    feuilles, logos, theme = [], [], []
    masque = None
    for balise in re.findall(r"<link\b[^>]*>", html, re.I):
        a = attributs(balise)
        rels = a.get("rel", "").lower().split()
        href = a.get("href")
        if not href:
            continue
        url = urllib.parse.urljoin(base, href)
        if "stylesheet" in rels:
            feuilles.append(url)
        elif "apple-touch-icon" in rels or "apple-touch-icon-precomposed" in rels:
            logos.append({"url": url, "type": "icone", "taille": _taille(a.get("sizes")) or 180, "rang": 2})
        elif "icon" in rels or "shortcut" in rels:
            logos.append({"url": url, "type": "icone", "taille": _taille(a.get("sizes")) or (64 if url.endswith(".svg") else 32), "rang": 3})
        elif "mask-icon" in rels:
            masque = hex_norme(a.get("color")) or masque
            logos.append({"url": url, "type": "masque", "taille": 64, "rang": 4})
    for balise in re.findall(r"<meta\b[^>]*>", html, re.I):
        a = attributs(balise)
        nom = (a.get("name") or a.get("property") or "").lower()
        if nom in ("theme-color", "msapplication-tilecolor") and hex_norme(a.get("content")):
            theme.append(hex_norme(a.get("content")))
    site = None
    for balise in re.findall(r"<meta\b[^>]*>", html, re.I):
        a = attributs(balise)
        if (a.get("property") or "").lower() == "og:site_name" and a.get("content"):
            site = a["content"].strip()
    for balise in re.findall(r"<img\b[^>]*>", html, re.I):
        a = attributs(balise)
        src = a.get("src") or ""
        trace = " ".join((src, a.get("alt", ""), a.get("class", ""), a.get("id", ""))).lower()
        if "logo" in trace and src and not any(t in trace for t in MARQUES_TIERCES) and not src.startswith("data:"):
            logos.append({"url": urllib.parse.urljoin(base, src), "type": "image", "taille": 0, "rang": 1})
    styles = "\n".join(re.findall(r"<style\b[^>]*>(.*?)</style>", html, re.I | re.S))
    titre = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    logos.sort(key=lambda l: (l["rang"], -l["taille"]))
    return {"feuilles": feuilles[:MAX_FEUILLES], "styles": styles, "theme": theme, "masque": masque,
            "logos": logos, "titre": re.sub(r"\s+", " ", titre.group(1)).strip() if titre else "", "site": site}


def _taille(sizes: str | None) -> int:
    m = re.search(r"(\d+)x\d+", sizes or "")
    return int(m.group(1)) if m else 0


def faces_css(css: str, base: str = "") -> list[dict]:
    """Les @font-face d'une feuille : famille, poids (le bas d'une plage), style, url du woff2 (sinon
    woff, sinon ttf), et si la face couvre le latin de base (les accents du français)."""
    faces = []
    for bloc in re.findall(r"@font-face\s*\{([^}]*)\}", css, re.I):
        famille = re.search(r"font-family\s*:\s*([^;]+)", bloc, re.I)
        if not famille:
            continue
        nom = famille.group(1).strip().strip("'\"")
        poids = re.search(r"font-weight\s*:\s*([^;]+)", bloc, re.I)
        poids_v = poids.group(1).strip() if poids else "400"
        poids_v = {"normal": "400", "bold": "700"}.get(poids_v.lower(), poids_v)
        m = re.match(r"(\d+)(?:\s+(\d+))?", poids_v)
        style = re.search(r"font-style\s*:\s*([^;]+)", bloc, re.I)
        sources = re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)\s*(?:format\(\s*['\"]?([\w-]+)['\"]?\s*\))?", bloc, re.I)
        formats = {u: format_police(u, f) for u, f in sources}
        choix = next((u for voulu in ("woff2", "woff", "truetype", "opentype") for u in formats if formats[u] == voulu), None)
        if not choix:
            continue
        plage = re.search(r"unicode-range\s*:\s*([^;]+)", bloc, re.I)
        faces.append({"famille": nom, "poids": int(m.group(1)) if m else 400,
                      "poids_max": int(m.group(2)) if m and m.group(2) else None,
                      "style": "italic" if style and "italic" in style.group(1).lower() else "normal",
                      "url": urllib.parse.urljoin(base, choix) if base else choix,
                      "latin": couvre_latin(plage.group(1) if plage else None)})
    return faces


def format_police(url: str, declare: str | None) -> str:
    """woff2, woff, truetype ou opentype : le format déclaré, sinon celui de l'extension."""
    f = (declare or Path(urllib.parse.urlparse(url).path).suffix.lstrip(".")).lower()
    return {"ttf": "truetype", "otf": "opentype"}.get(f, f)


def couvre_latin(plage: str | None) -> bool:
    """Vrai si la plage unicode couvre « A » et « é » (sans plage : tout est couvert)."""
    if not plage:
        return True
    for morceau in plage.split(","):
        m = morceau.strip().lower().lstrip("u+")
        if "?" in m:
            bas, haut = int(m.replace("?", "0"), 16), int(m.replace("?", "f"), 16)
        elif "-" in m:
            a, b = m.split("-", 1)
            bas, haut = int(a, 16), int(b.lstrip("u+"), 16)
        else:
            try:
                bas = haut = int(m, 16)
            except ValueError:
                continue
        if bas <= 0x41 and haut >= 0xE9:
            return True
    return False


def variables_couleur(css: str) -> dict[str, str]:
    """Les propriétés personnalisées qui portent une couleur (--color-primary-400: #fe0)."""
    sortie = {}
    for nom, valeur in re.findall(r"(--[\w-]+)\s*:\s*([^;}]+)", css):
        c = hex_norme(valeur.strip())
        if c:
            sortie.setdefault(nom, c)
    return sortie


def frequences_couleurs(css: str) -> dict[str, int]:
    """Les couleurs écrites dans les déclarations color / background (sans les variables)."""
    compte: dict[str, int] = {}
    for valeur in re.findall(r"(?<![-\w])(?:color|background(?:-color)?)\s*:\s*([^;}]+)", css, re.I):
        for brut in re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)", valeur):
            c = hex_norme(brut)
            if c:
                compte[c] = compte.get(c, 0) + 1
    return compte


def familles_utilisees(css: str) -> list[str]:
    """Les familles nommées dans les déclarations font-family, de la plus fréquente à la moins."""
    compte: dict[str, int] = {}
    for valeur in re.findall(r"font-family\s*:\s*([^;}]+)", css, re.I):
        premiere = valeur.split(",")[0].strip().strip("'\"")
        if premiere and not premiere.startswith("var(") and premiere.lower() not in POLICES_GENERIQUES:
            compte[premiere] = compte.get(premiere, 0) + 1
    return sorted(compte, key=lambda f: -compte[f])


def indices_capture(capture: Path) -> dict:
    """Ce que la capture HyperFrames a mesuré sur la page rendue : sections, couleurs par fréquence,
    couleurs des titres et des boutons, polices des titres et du texte."""
    extrait = capture / "extracted"
    tokens = _json(extrait / "tokens.json")
    styles = _json(extrait / "design-styles.json")
    typo = styles.get("typography") or []
    titres_famille = next((t.get("fontFamily") for t in typo if t.get("role") in ("display", "heading")), None)
    corps_famille = next((t.get("fontFamily") for t in typo if t.get("role") == "body"), None)
    return {
        "sections": [(s.get("type"), s.get("backgroundColor")) for s in tokens.get("sections") or []],
        "couleurs": tokens.get("colors") or [],
        "titres": [h.get("color") for h in tokens.get("headings") or [] if h.get("level") in (1, 2)],
        "boutons": [b.get("background") for b in (styles.get("buttons") or []) + (tokens.get("ctas") or [])
                    if isinstance(b, dict)],
        "polices": {"titres": titres_famille, "corps": corps_famille},
        "familles": [f.get("family") for f in tokens.get("fonts") or [] if f.get("family")],
        "titre": tokens.get("title") or "",
    }


def _json(fichier: Path) -> dict:
    try:
        return json.loads(fichier.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def choisir_polices(capture: dict | None, familles_css: list[str], faces: list[dict]) -> dict:
    """titres et corps : ce que la page rendue utilise (capture), sinon les familles des CSS, sinon
    celles qui ont des @font-face. Une police système (Arial, system-ui) devient Inter."""
    declarees = []
    for f in faces:
        if f["famille"] not in declarees:
            declarees.append(f["famille"])

    def propre(famille):
        if not famille:
            return None
        f = famille.split(",")[0].strip().strip("'\"")
        return None if f.lower() in POLICES_GENERIQUES or f.startswith("var(") else f

    capture = capture or {}
    titres = propre((capture.get("polices") or {}).get("titres"))
    corps = propre((capture.get("polices") or {}).get("corps"))
    repli = next((propre(f) for f in (capture.get("familles") or []) + familles_css + declarees if propre(f)), None)
    titres, corps = titres or repli, corps or repli or titres
    titres = titres or corps
    return {"titres": titres or DEFAUT["titres"], "corps": corps or DEFAUT["corps"]}


# ---------------------------------------------------------------------------
# Les polices : registre, Google Fonts, fichiers de la page
# ---------------------------------------------------------------------------
REGISTRE = "polices.json"
POIDS_GOOGLE = (100, 200, 300, 400, 500, 600, 700, 800, 900)


def nom_fichier_police(famille: str, poids: int, style: str, ext: str = "woff2") -> str:
    base = re.sub(r"[^A-Za-z0-9]+", "", famille) or "Police"
    return f"{base}-{poids}{'-italic' if style == 'italic' else ''}.{ext}"


def lire_registre(dossier: Path) -> dict:
    return _json(dossier / REGISTRE)


def ecrire_registre(dossier: Path, registre: dict) -> None:
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / REGISTRE).write_text(json.dumps(registre, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def faces_disponibles(racine: Path, famille: str) -> tuple[Path, dict] | None:
    """(dossier, entrée) de la famille : les polices du client d'abord, puis celles livrées."""
    for dossier in (racine / "marque" / "polices", racine / "assets" / "fonts"):
        reg = lire_registre(dossier)
        cle = next((k for k in reg if k.lower() == famille.lower()), None)
        if cle and reg[cle].get("faces"):
            return dossier, {**reg[cle], "famille": cle}
    return None


def css_google(famille: str, poids=POIDS_GOOGLE, italique: bool = False) -> str:
    axes = ";".join(f"{'1' if italique else '0'},{p}" for p in poids)
    url = ("https://fonts.googleapis.com/css2?family=" + urllib.parse.quote(famille).replace("%20", "+")
           + f":ital,wght@{axes}&display=swap")
    contenu, _type = telecharger(url, accepte="text/css")
    texte = contenu.decode("utf-8", "replace")
    if "@font-face" not in texte:
        raise ErreurMarque(f"« {famille} » n'est pas sur Google Fonts")
    return texte


def faces_google(css: str) -> list[dict]:
    """Les faces latines d'une feuille Google Fonts (une par poids et par style)."""
    retenues = {}
    for f in faces_css(css):
        if f["latin"]:
            retenues.setdefault((f["poids"], f["style"]), f)
    return [retenues[k] for k in sorted(retenues)]


def installer_faces(racine: Path, famille: str, faces: list[dict], licence: str) -> list[str]:
    """Télécharge les faces dans marque/polices/ et les déclare dans son registre."""
    dossier = racine / "marque" / "polices"
    dossier.mkdir(parents=True, exist_ok=True)
    registre = lire_registre(dossier)
    entree = {"licence": licence, "faces": []}
    vues = {}
    partages = {f["url"] for f in faces if sum(g["url"] == f["url"] for g in faces) > 1}
    for f in faces:
        ext = Path(urllib.parse.urlparse(f["url"]).path).suffix.lstrip(".").lower() or "woff2"
        # Une police variable : un seul fichier sert toutes les graisses.
        nom = (f"{re.sub(r'[^A-Za-z0-9]+', '', famille)}-variable{'-italic' if f['style'] == 'italic' else ''}.{ext}"
               if f["url"] in partages else nom_fichier_police(famille, f["poids"], f["style"], ext))
        if f["url"] not in vues:
            contenu, _t = telecharger(f["url"], limite=2 * 1024 * 1024)
            if len(contenu) < 1000:
                continue
            (dossier / nom).write_bytes(contenu)
            vues[f["url"]] = nom
        entree["faces"].append({"fichier": vues[f["url"]], "poids": f["poids"], "style": f["style"],
                                "format": {"ttf": "truetype", "otf": "opentype"}.get(ext, ext)})
    if not entree["faces"]:
        raise ErreurMarque(f"aucun fichier de « {famille} » n'a pu être téléchargé")
    registre[famille] = entree
    ecrire_registre(dossier, registre)
    return [f["fichier"] for f in entree["faces"]]


def acquerir_police(racine: Path, famille: str, faces_page: list[dict] | None = None) -> str:
    """Rend la police utilisable au rendu, et dit d'où elle vient. Ordre : déjà là (livrée ou déjà
    installée), Google Fonts (police libre, toutes graisses), sinon les fichiers de sa page."""
    if faces_disponibles(racine, famille):
        return "déjà disponible"
    try:
        faces = faces_google(css_google(famille))
        if faces:
            installer_faces(racine, famille, faces, "Google Fonts (police libre)")
            return f"police libre, téléchargée depuis Google Fonts ({len(faces)} graisses)"
    except ErreurMarque:
        pass
    propres = {}
    for f in faces_page or []:
        if f["famille"].lower() == famille.lower() and f["latin"]:
            propres.setdefault((f["poids"], f["style"]), f)
    if propres:
        installer_faces(racine, famille, [propres[k] for k in sorted(propres)],
                        "reprise de sa page : vérifier que sa licence couvre la vidéo")
        return "reprise des fichiers de ta page (si tu as acheté cette police, vérifie que ta licence couvre la vidéo)"
    raise ErreurMarque(f"« {famille} » introuvable (ni sur Google Fonts, ni dans les fichiers de la page)")


# ---------------------------------------------------------------------------
# Le logo
# ---------------------------------------------------------------------------
SIGNATURES = ((b"\x89PNG", ".png"), (b"\xff\xd8\xff", ".jpg"), (b"RIFF", ".webp"), (b"GIF8", ".gif"))


def type_image(contenu: bytes) -> str | None:
    for sig, ext in SIGNATURES:
        if contenu.startswith(sig):
            return ext
    debut = contenu[:600].lstrip().lower()
    if debut.startswith(b"<svg") or (debut.startswith(b"<?xml") and b"<svg" in contenu[:2000].lower()):
        if re.search(rb"<script|\son\w+\s*=|javascript:", contenu, re.I):
            return None
        return ".svg"
    if contenu[:4] == b"\x00\x00\x01\x00":
        return ".ico"
    return None


def recuperer_logo(racine: Path, candidats: list[dict]) -> tuple[str, str] | None:
    """Le premier logo candidat qui est vraiment une image : (chemin relatif à la racine, origine)."""
    dossier = racine / "marque"
    dossier.mkdir(parents=True, exist_ok=True)
    for c in candidats:
        try:
            contenu, _t = telecharger(c["url"], limite=3 * 1024 * 1024)
        except ErreurMarque:
            continue
        ext = type_image(contenu)
        if not ext or ext == ".ico" or len(contenu) < 200:
            continue
        for ancien in dossier.glob("logo.*"):
            ancien.unlink()
        (dossier / f"logo{ext}").write_bytes(contenu)
        origine = {"image": "image « logo » de la page", "icone": "icône du site", "masque": "icône d'onglet"}[c["type"]]
        return f"marque/logo{ext}", origine
    return None


# ---------------------------------------------------------------------------
# marque.json
# ---------------------------------------------------------------------------
FICHIER = "marque.json"


def lire(racine: Path) -> dict | None:
    m = _json(racine / FICHIER)
    return m or None


def ecrire(racine: Path, marque: dict) -> Path:
    f = racine / FICHIER
    f.write_text(json.dumps(marque, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return f


def nouvelle(source_type: str, valeur: str, couleurs: dict, polices: dict, **reste) -> dict:
    return {"version": 1, "nom": reste.get("nom"),
            "source": {"type": source_type, "valeur": valeur, "date": datetime.date.today().isoformat()},
            "couleurs": {k: couleurs.get(k) for k in ("fond", "texte", "accent", "surface", "secondaire")},
            "polices": {"titres": polices.get("titres"), "corps": polices.get("corps")},
            "logo": reste.get("logo"), "mot_cle": reste.get("mot_cle"), "musique": reste.get("musique"),
            "monteur_ia": reste.get("monteur_ia"), "notes": reste.get("notes") or [], "valide": False}


def resoudre(marque: dict | None) -> dict:
    """Les valeurs finales du style : celles de marque.json, complétées par des dérivées lisibles."""
    m = marque or {}
    c = m.get("couleurs") or {}
    p = m.get("polices") or {}
    fond = hex_norme(c.get("fond")) or DEFAUT["fond"]
    texte = hex_norme(c.get("texte")) or lisible_sur(fond)
    if contraste(texte, fond) < 3:
        texte = lisible_sur(fond)
    accent = hex_norme(c.get("accent")) or (DEFAUT["accent"] if not marque else texte)
    surface = hex_norme(c.get("surface")) or melange(fond, lisible_sur(fond), 0.08)
    return {
        "fond": fond, "texte": texte, "accent": accent, "surface": surface,
        "secondaire": hex_norme(c.get("secondaire")) or accent,
        "attenue": melange(texte, fond, 0.42),
        # Sur l'accent : une couleur de la marque si elle s'y lit bien, sinon la plus lisible.
        "sur_accent": next((x for x in (fond, texte) if contraste(x, accent) >= 4.5),
                           lisible_sur(accent, (fond, texte, "#ffffff", "#111111"))),
        "contour": "#0b0b0b" if luminance(texte) > 0.5 else "#ffffff",
        "surface_contraste": melange(surface, lisible_sur(fond), 0.82),
        "titres": p.get("titres") or DEFAUT["titres"], "corps": p.get("corps") or DEFAUT["corps"],
        "nom": m.get("nom") or "", "logo": m.get("logo"), "personnalisee": bool(marque),
    }


# ---------------------------------------------------------------------------
# brand/ : ce que chaque vidéo copie
# ---------------------------------------------------------------------------
TOKENS = """/* Style de la marque : FICHIER GÉNÉRÉ depuis marque.json par `studio_motion.py style`.
   Ne pas l'éditer : change marque.json (ou `studio_motion.py marque regler …`), puis régénère.
   Marque : {source} */

:root {{
  --brand-bg: {fond};              /* fond principal */
  --brand-surface: {surface};         /* cartes, blocs surélevés */
  --brand-text: {texte};            /* texte principal, lisible sur le fond */
  --brand-muted: {attenue};           /* texte d'appui, grisé */
  --brand-accent: {accent};          /* la couleur de la marque */
  --brand-secondary: {secondaire};       /* deuxième couleur (l'accent s'il n'y en a pas) */
  --brand-contrast: {sur_accent};        /* texte posé SUR l'accent */
  --brand-stroke: {contour};          /* contour de lisibilité */
  --brand-surface-contrast: {surface_contraste}; /* surface qui tranche (rare) */
  --brand-negative: #ff5050;        /* croix, erreur (hors marque) */

  --brand-font-display: "{titres}", "Arial Narrow", Impact, sans-serif;
  --brand-font-body: "{corps}", "Avenir Next", Arial, system-ui, sans-serif;
  --brand-font-mono: ui-monospace, "Courier New", monospace;

  --brand-ease-inout: cubic-bezier(0.65, 0, 0.35, 1);
  --brand-ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
}}
"""


def faces_pour(racine: Path, famille: str) -> list[tuple[Path, dict]]:
    trouve = faces_disponibles(racine, famille)
    if not trouve:
        return []
    dossier, entree = trouve
    return [(dossier / f["fichier"], f) for f in entree["faces"] if (dossier / f["fichier"]).is_file()]


def ecrire_style(racine: Path) -> dict:
    """Régénère brand/ (tokens.css, fonts.css, fonts/, logo) depuis marque.json. Rend le style résolu
    et la liste des polices sans fichier (au rendu, elles seraient remplacées)."""
    marque = lire(racine)
    s = resoudre(marque)
    brand = racine / "brand"
    fonts = brand / "fonts"
    if fonts.exists():
        shutil.rmtree(fonts)
    fonts.mkdir(parents=True)
    blocs, manquantes = [], []
    for famille in dict.fromkeys((s["titres"], s["corps"])):
        faces = faces_pour(racine, famille)
        if not faces:
            manquantes.append(famille)
            continue
        for chemin, f in faces:
            shutil.copy2(chemin, fonts / chemin.name)
            blocs.append(f'@font-face {{ font-family: "{famille}"; font-style: {f.get("style", "normal")}; '
                         f'font-weight: {f.get("poids", 400)}; font-display: block; '
                         f'src: url("fonts/{chemin.name}") format("{f.get("format", "woff2")}"); }}')
    (brand / "fonts.css").write_text(
        "/* Polices de la marque : FICHIER GÉNÉRÉ par `studio_motion.py style`. Hébergées en local\n"
        "   (brand/fonts/, à côté de cette feuille) : le rendu ne télécharge rien. */\n" + "\n".join(blocs) + "\n",
        encoding="utf-8")
    source = (marque or {}).get("source") or {}
    libelle = f"{source.get('type')} ({source.get('valeur')})" if marque else "style de départ, marque pas encore réglée"
    (brand / "tokens.css").write_text(TOKENS.format(source=libelle, **s), encoding="utf-8")
    for ancien in brand.glob("logo.*"):
        ancien.unlink()
    if s["logo"] and (racine / s["logo"]).is_file():
        shutil.copy2(racine / s["logo"], brand / ("logo" + Path(s["logo"]).suffix.lower()))
    s["manquantes"] = manquantes
    return s


def resume(marque: dict | None, s: dict) -> list[str]:
    """Ce qu'on montre au client pour validation, en lignes simples."""
    lignes = []
    if marque and marque.get("nom"):
        lignes.append(f"Marque : {marque['nom']}")
    lignes.append(f"Fond {s['fond']} · texte {s['texte']} · couleur de la marque {s['accent']}"
                  + (f" · deuxième couleur {s['secondaire']}" if s["secondaire"] != s["accent"] else ""))
    lignes.append(f"Titres en {s['titres']}, texte en {s['corps']}")
    lignes.append(f"Logo : {s['logo']}" if s["logo"] else "Logo : aucun (ses vidéos s'en passent, ou il en donne un)")
    if marque and marque.get("mot_cle"):
        lignes.append(f"Mot-clé : {marque['mot_cle']}")
    return lignes


# ---------------------------------------------------------------------------
# Monteur IA : lu, jamais écrit
# ---------------------------------------------------------------------------
def est_monteur(dossier: Path) -> bool:
    return (dossier / "templates" / "AGENT.md.tpl").is_file() and (
        (dossier / "brand.config.json").is_file() or (dossier / "brand.config.example.json").is_file())


def lire_tokens_monteur(css: str) -> dict:
    def val(nom):
        m = re.search(rf"--brand-{nom}:\s*([^;]+);", css)
        return m.group(1).strip() if m else None

    def famille(nom):
        v = val(nom)
        return v.split(",")[0].strip().strip("'\"") if v else None
    return {"fond": hex_norme(val("bg")), "texte": hex_norme(val("text")), "accent": hex_norme(val("accent")),
            "surface": hex_norme(val("surface")), "titres": famille("font-display"), "corps": famille("font-body")}


def depuis_monteur(racine: Path, dossier: Path) -> dict:
    """Reprend la marque d'un dossier Monteur IA : couleurs et polices telles que ses Reels les
    utilisent (son brand/ généré, sinon ses réglages et son style de départ), nom, mot-clé, musique,
    logo. Copie ce qu'il faut dans marque/ ; n'écrit jamais dans `dossier`."""
    dossier = Path(dossier).expanduser().resolve()
    if not est_monteur(dossier):
        raise ErreurMarque(f"{dossier} n'est pas un dossier Monteur IA (il manque templates/AGENT.md.tpl "
                           "ou brand.config.json)")
    config = _json(dossier / "brand.config.json") or _json(dossier / "brand.config.example.json")
    visuel = {k: v for k, v in (config.get("visual") or {}).items() if v not in (None, "")}
    notes = []
    tokens = dossier / "brand" / "tokens.css"
    if tokens.is_file():
        lu = lire_tokens_monteur(tokens.read_text(encoding="utf-8"))
        notes.append("couleurs et polices lues dans son style généré (brand/tokens.css)")
    else:
        presets = _json(dossier / "templates" / "style-presets.json").get("presets") or []
        voulu = visuel.get("stylePreset")
        preset = next((p for p in presets if p.get("id") == voulu), None) or (presets[0] if presets else {})
        v = {**(preset.get("visual") or {}), **visuel}
        lu = {"fond": hex_norme(v.get("bg")), "texte": hex_norme(v.get("text")), "accent": hex_norme(v.get("accent")),
              "surface": hex_norme(v.get("surface")), "titres": v.get("fontDisplay"), "corps": v.get("fontBody")}
        notes.append("couleurs et polices lues dans ses réglages (brand.config.json et son style de départ)")
    if not (dossier / "brand.config.json").is_file():
        notes.append("son Monteur IA n'est pas encore personnalisé : c'est son style de départ")
    if lu.get("fond") and lu.get("texte") and contraste(lu["texte"], lu["fond"]) < 3:
        lisible = lisible_sur(lu["fond"])
        notes.append(f"texte {lu['texte']} illisible sur son fond {lu['fond']} : {lisible} à la place")
        lu["texte"] = lisible
    polices = _importer_polices_monteur(racine, dossier, [lu.get("titres"), lu.get("corps")], notes)
    # Une police déclarée chez lui mais sans fichier : la version libre (Google Fonts) si elle existe.
    polices = assurer_polices(racine, polices, [], notes)
    marque_cfg = config.get("brand") or {}
    cta = config.get("cta") or {}
    musique = _copier_musique(racine, dossier, (config.get("audio") or {}).get("musicFile"), notes)
    logo = _copier_logo_monteur(racine, dossier)
    pack = dossier / "assets" / "sfx" / "pack"
    if pack.is_dir():
        notes.append(f"Pack SFX présent dans son dossier Monteur IA ({pack}) : `pack-sfx reprendre` le copie ici, avec son accord")
    return nouvelle("monteur", str(dossier), lu, polices, nom=marque_cfg.get("name"), mot_cle=cta.get("defaultKeyword"),
                    musique=musique, logo=logo, monteur_ia=str(dossier), notes=notes)


def _importer_polices_monteur(racine: Path, dossier: Path, familles: list, notes: list) -> dict:
    """Copie dans marque/polices/ les fichiers des polices de ses Reels (déclarées dans son
    brand/fonts.css, ou dans sa table de polices)."""
    faces = []
    css = dossier / "brand" / "fonts.css"
    if css.is_file():
        for f in faces_css(css.read_text(encoding="utf-8")):
            nom = Path(urllib.parse.urlparse(f["url"]).path).name
            for base in (dossier / "brand" / "fonts", dossier / "assets" / "fonts"):
                if (base / nom).is_file():
                    faces.append({**f, "chemin": base / nom})
                    break
    table = (_json(dossier / "templates" / "style-presets.json").get("fonts") or {})
    for famille, entree in table.items():
        if isinstance(entree, dict):
            for f in entree.get("faces") or []:
                chemin = dossier / "assets" / "fonts" / str(f.get("file"))
                if chemin.is_file():
                    faces.append({"famille": famille, "poids": int(f.get("weight", 400)), "style": f.get("style", "normal"),
                                  "url": str(f.get("file")), "latin": True, "chemin": chemin})
    retenues = {}
    for famille in dict.fromkeys(f for f in familles if f):
        if faces_disponibles(racine, famille):
            retenues[famille] = famille
            continue
        siennes = {}
        for f in faces:
            if f["famille"].lower() == famille.lower():
                siennes.setdefault((f["poids"], f["style"]), f)
        if not siennes:
            notes.append(f"police « {famille} » sans fichier dans son dossier Monteur IA")
            continue
        destination = racine / "marque" / "polices"
        destination.mkdir(parents=True, exist_ok=True)
        registre = lire_registre(destination)
        entree = {"licence": "reprise de son dossier Monteur IA", "faces": []}
        for (poids, style), f in sorted(siennes.items()):
            ext = f["chemin"].suffix.lstrip(".").lower()
            nom = nom_fichier_police(famille, poids, style, ext)
            shutil.copy2(f["chemin"], destination / nom)
            entree["faces"].append({"fichier": nom, "poids": poids, "style": style,
                                    "format": {"ttf": "truetype", "otf": "opentype"}.get(ext, ext)})
        registre[famille] = entree
        ecrire_registre(destination, registre)
        retenues[famille] = famille
    return {"titres": familles[0], "corps": familles[1] or familles[0]}


def _copier_musique(racine: Path, dossier: Path, fichier, notes: list) -> str | None:
    if not fichier:
        return None
    for chemin in (dossier / str(fichier), dossier / "assets" / "music" / str(fichier)):
        if chemin.is_file():
            dest = racine / "marque" / ("musique" + chemin.suffix.lower())
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(chemin, dest)
            notes.append(f"sa musique de fond reprise ({chemin.name})")
            return f"marque/{dest.name}"
    return None


def _copier_logo_monteur(racine: Path, dossier: Path) -> str | None:
    """Son logo : la première image de assets/logos/, sinon une image « logo » de assets/images/."""
    images = (".png", ".svg", ".jpg", ".jpeg", ".webp")
    candidats = []
    for base, il_faut_logo in ((dossier / "assets" / "logos", False), (dossier / "assets" / "images", True)):
        if base.is_dir():
            candidats += [f for f in sorted(base.iterdir())
                          if f.is_file() and f.suffix.lower() in images and (not il_faut_logo or "logo" in f.name.lower())]
    if not candidats:
        return None
    dest = racine / "marque" / ("logo" + candidats[0].suffix.lower())
    dest.parent.mkdir(parents=True, exist_ok=True)
    for ancien in dest.parent.glob("logo.*"):
        ancien.unlink()
    shutil.copy2(candidats[0], dest)
    return f"marque/{dest.name}"


# ---------------------------------------------------------------------------
# Les quatre sources, de bout en bout
# ---------------------------------------------------------------------------
def nom_du_site(infos: dict, url: str) -> str:
    """og:site_name, sinon la partie du titre après « | » ou « - », sinon le domaine."""
    if infos.get("site"):
        return infos["site"]
    morceaux = [m.strip() for m in re.split(r"\s[|\-–—·]\s", infos.get("titre") or "") if m.strip()]
    if len(morceaux) > 1 and len(morceaux[-1]) <= 40:
        return morceaux[-1]
    hote = urllib.parse.urlparse(url).hostname or ""
    return re.sub(r"^www\.", "", hote)


def lire_feuilles(infos: dict, journal: list) -> tuple[str, list[dict]]:
    """Le texte de toutes les feuilles (et un niveau de @import) et leurs @font-face, chacune
    résolue par rapport à sa propre adresse."""
    textes, faces = [infos.get("styles") or ""], faces_css(infos.get("styles") or "", infos.get("base", ""))
    a_lire = list(infos.get("feuilles") or [])
    vues = set()
    while a_lire and len(vues) < MAX_FEUILLES:
        url = a_lire.pop(0)
        if url in vues:
            continue
        vues.add(url)
        try:
            css = telecharger(url, MAX_CSS, accepte="text/css")[0].decode("utf-8", "replace")
        except ErreurMarque as e:
            journal.append(f"feuille illisible : {e}")
            continue
        textes.append(css)
        faces += faces_css(css, url)
        for imp in re.findall(r"@import\s+(?:url\()?\s*['\"]?([^'\")\s;]+)", css)[:5]:
            a_lire.append(urllib.parse.urljoin(url, imp))
    return "\n".join(textes), faces


def capturer(hyperframes: list[str], url: str, dest: Path) -> Path | None:
    """La capture HyperFrames (navigateur sans fenêtre) : couleurs et polices réellement rendues,
    images de la page. 1 à 2 minutes ; None si elle échoue."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run([*hyperframes, "capture", url, "-o", str(dest), "--skip-assets", "--skip-vision",
                            "--max-screenshots", "4", "--timeout", "60000", "--json"],
                           capture_output=True, text=True, timeout=300)
    except (subprocess.TimeoutExpired, OSError):
        return None
    return dest if r.returncode == 0 and (dest / "extracted" / "tokens.json").is_file() else None


def depuis_page(racine: Path, url: str, hyperframes: list[str] | None = None) -> tuple[dict, list[str]]:
    """La marque d'après sa page de vente. Rend (marque, journal)."""
    journal: list[str] = []
    if not re.match(r"https?://", url):
        url = "https://" + url
    html = telecharger(url, accepte="text/html")[0].decode("utf-8", "replace")
    capture = capturer(hyperframes, url, racine / "marque" / "capture") if hyperframes else None
    if capture is None and hyperframes:
        journal.append("capture de la page impossible : marque tirée du HTML et des feuilles de style seulement")
    if capture is not None and (capture / "extracted" / "page.html").is_file():
        # La page rendue par le navigateur : elle contient ce qu'un site en JavaScript n'écrit pas dans son HTML.
        html = html + "\n" + (capture / "extracted" / "page.html").read_text(encoding="utf-8", errors="replace")
    infos = lire_html(html, url)
    infos["base"] = url
    css, faces = lire_feuilles(infos, journal)
    ic = indices_capture(capture) if capture else {}
    indices = {"sections": ic.get("sections") or [], "couleurs": ic.get("couleurs") or [],
               "titres": ic.get("titres") or [], "boutons": ic.get("boutons") or [],
               "theme": infos["theme"], "masque": infos["masque"], "variables": variables_couleur(css),
               "frequences_css": frequences_couleurs(css)}
    couleurs = choisir_couleurs(indices)
    polices = choisir_polices(ic, familles_utilisees(css), faces)
    notes = list(couleurs["raisons"])
    polices = assurer_polices(racine, polices, faces, notes)
    logo = recuperer_logo(racine, infos["logos"])
    if logo:
        notes.append(f"logo : {logo[1]}")
    else:
        notes.append("logo : aucun trouvé sur la page")
    marque = nouvelle("page", url, couleurs, polices, nom=nom_du_site(infos, url), logo=logo[0] if logo else None,
                      notes=notes)
    return marque, journal


def assurer_polices(racine: Path, polices: dict, faces: list[dict], notes: list) -> dict:
    """Chaque police choisie devient utilisable au rendu ; sinon, celle de départ prend sa place."""
    retenues = dict(polices)
    for role, defaut in (("titres", DEFAUT["titres"]), ("corps", DEFAUT["corps"])):
        famille = polices.get(role)
        try:
            origine = acquerir_police(racine, famille, faces)
            notes.append(f"{'titres' if role == 'titres' else 'texte'} en {famille} : {origine}")
        except ErreurMarque as e:
            retenues[role] = defaut
            notes.append(f"{e} : {defaut} à la place pour les {'titres' if role == 'titres' else 'textes'}")
    return retenues


def depuis_images(racine: Path, fichiers: list[Path], ffmpeg: str) -> dict:
    """La marque d'après des images ou des captures : palette mesurée. Les polices ne se lisent pas
    sur une image : celles déjà réglées restent (l'agent en propose une avec `police`)."""
    pixels = b""
    for f in fichiers:
        pixels += pixels_image(ffmpeg, Path(f))
    couleurs = couleurs_depuis_palette(palette_pixels(pixels))
    actuelle = lire(racine) or {}
    polices = actuelle.get("polices") or {"titres": DEFAUT["titres"], "corps": DEFAUT["corps"]}
    notes = couleurs["raisons"] + ["polices : à choisir en regardant les images (`studio_motion.py police`)"]
    return nouvelle("images", ", ".join(Path(f).name for f in fichiers), couleurs, polices,
                    nom=actuelle.get("nom"), logo=actuelle.get("logo"), notes=notes)


def depuis_video(racine: Path, fichier: Path, ffmpeg: str) -> dict:
    """La marque d'après une vidéo dont il aime le style : palette de ses images, et une planche
    (marque/video/planche.jpg) que l'agent regarde pour les polices et le style."""
    couleurs = couleurs_depuis_palette(palette_pixels(pixels_video(ffmpeg, Path(fichier))))
    dossier = racine / "marque" / "video"
    dossier.mkdir(parents=True, exist_ok=True)
    duree = duree_media(ffmpeg, Path(fichier)) or 30.0
    subprocess.run([ffmpeg, "-v", "error", "-y", "-i", str(fichier), "-vf",
                    f"fps=12/{max(duree, 1):.2f},scale=320:-2,tile=4x3:padding=6:color=gray", "-frames:v", "1",
                    str(dossier / "planche.jpg")], capture_output=True)
    actuelle = lire(racine) or {}
    polices = actuelle.get("polices") or {"titres": DEFAUT["titres"], "corps": DEFAUT["corps"]}
    notes = couleurs["raisons"] + ["polices : à choisir en regardant marque/video/planche.jpg (`studio_motion.py police`)"]
    return nouvelle("video", str(fichier), couleurs, polices, nom=actuelle.get("nom"), logo=actuelle.get("logo"),
                    notes=notes)
