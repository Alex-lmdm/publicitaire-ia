"""Le kit de motion design suit la taille réelle de la composition (9:16 comme 16:9).

Les tests de comportement chargent templates/kit/kit.js dans Node avec un faux DOM et un faux
GSAP qui notent les appels : aucune dépendance, ils sont sautés si Node manque.
"""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
KIT = RACINE / "templates" / "kit"

# Faux DOM minimal (classes, attributs, closest, querySelector à combinateur descendant) et faux
# GSAP : de quoi exécuter K.cadre, K.champ, K.curseur et K.chapitre hors navigateur.
HARNAIS = r"""
const vm = require("vm"), fs = require("fs");
const cas = JSON.parse(process.argv[process.argv.length - 1]);
class El {
  constructor(tag) { this.tagName = tag; this.attrs = {}; this.style = {}; this.dataset = {};
    this.children = []; this.parentElement = null; this.className = ""; this._html = ""; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; }
  hasAttribute(k) { return k in this.attrs; }
  appendChild(c) { c.parentElement = this; this.children.push(c); return c; }
  set innerHTML(v) { this._html = v; } get innerHTML() { return this._html; }
  matches(sel) {
    const re = /\.([\w-]+)|\[([\w-]+)\]/g; let m, ok = true, vu = false;
    while ((m = re.exec(sel))) { vu = true;
      ok = ok && (m[1] ? (" " + this.className + " ").includes(" " + m[1] + " ") : this.hasAttribute(m[2])); }
    return vu && ok;
  }
  closest(sel) { let n = this; while (n) { if (n.matches(sel)) return n; n = n.parentElement; } return null; }
  descendants() { const out = []; const f = (n) => n.children.forEach((c) => { out.push(c); f(c); }); f(this); return out; }
  querySelectorAll(sel) {
    const parts = sel.trim().split(/\s+/), dernier = parts.pop();
    return this.descendants().filter((e) => {
      if (!e.matches(dernier)) return false;
      let n = e.parentElement, i = parts.length - 1;
      while (i >= 0 && n && n !== this) { if (n.matches(parts[i])) i--; n = n.parentElement; }
      return i < 0;
    });
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
}
const el = (parent, classe, attrs) => { const e = new El("div"); e.className = classe || "";
  Object.assign(e.attrs, attrs || {}); if (parent) parent.appendChild(e); return e; };
const corps = new El("body"), appels = [], erreurs = [];
const tl = {};
["to", "fromTo", "set"].forEach((m) => { tl[m] = (cible, a, b, c) => { appels.push({ m, cible, a, b, c }); return tl; }; });
const gsap = { set: (cible, vars) => appels.push({ m: "gsap.set", cible, a: vars }), parseEase: () => (p) => p };
const document = { createElement: (tag) => new El(tag), querySelector: (sel) => corps.querySelector(sel) };
const window = { console: { error: (m) => erreurs.push(String(m)) } };
const ctx = vm.createContext({ window, document, gsap, console: window.console });
vm.runInContext(fs.readFileSync(cas.kit, "utf8"), ctx);
const K = window.K;

// Une composition principale et une scène (sous-composition) de la taille demandée. Avec `hote`, la
// scène est montée comme HyperFrames la monte : l'hôte d'index.html (data-composition-file, à la
// taille du projet) porte la racine intérieure de la scène, restée à la taille où elle a été écrite.
const attrsTaille = cas.sansTaille ? {} : { "data-width": String(cas.largeur), "data-height": String(cas.hauteur) };
const main = el(corps, "", Object.assign({ "data-composition-id": "main" }, cas.tailleMain || cas.hote ? attrsTaille : {}));
const parentScene = cas.hote ? el(main, "", Object.assign({ "data-composition-id": "s1", "data-composition-file": "compositions/s1.html" }, attrsTaille)) : main;
const scene = el(parentScene, "", Object.assign({ "data-composition-id": "s1" },
  cas.hote ? { "data-width": String(cas.hote[0]), "data-height": String(cas.hote[1]) } : cas.tailleMain ? {} : attrsTaille));
const res = {};
res.cadre = K.cadre ? K.cadre(scene) : null;
res.racine = { taille: [scene.getAttribute("data-width"), scene.getAttribute("data-height")], style: [scene.style.width, scene.style.height] };

const champ = el(scene, "k-champ");
const fab = (t) => { const e = new El("div"); e.style.width = t + "px"; e.dataset.taille = t; return e; };
const opts = { graine: 3, nombre: 60, objets: [fab] };
if (cas.zone) opts.zone = cas.zone;
res.objets = K.champ(champ, opts).map((e) => {
  const t = parseFloat(e.dataset.taille);
  return { x: parseFloat(e.style.left) + t / 2, y: parseFloat(e.style.top) + t / 2 };
});

const chap = el(scene, "k-chapitre");
const fantome = el(chap, "k-fantome k-sur-jaune");
const etiquette = el(chap, "k-etiquette"); el(etiquette, "k-mot"); el(etiquette, "k-mot");
const inter = el(chap, "k-interrupteur"); el(inter, "k-plein"); el(inter, "k-bille");
const hote = el(scene, "");
const curseur = K.curseur(hote, "c1", false);
appels.length = 0;
res.fin = K.chapitre(tl, chap, curseur, 1, cas.options || {});
res.fantomeIgnore = fantome.hasAttribute("data-layout-ignore");
const surCurseur = appels.filter((a) => a.cible === curseur);
res.depart = surCurseur.filter((a) => a.m === "gsap.set").map((a) => [a.a.x, a.a.y])[0];
res.clic = surCurseur.filter((a) => a.m === "to").map((a) => [a.a.x, a.a.y])[0];
res.fantome = appels.filter((a) => a.cible === fantome && a.m === "fromTo").map((a) => [a.a.x, a.b.x])[0];

// L'ordinateur portable du kit (08/11/2026), fermé puis ouvert par défaut.
const ordis = [K.ordinateur(scene, { largeur: 1000, capture: "assets/images/page.png", ouvert: 0 }), K.ordinateur(scene, { teinte: "gris" })];
res.ordi = ordis.map((o) => ({
  touches: o.racine.descendants().filter((e) => e.className === "k-ordi-touche").length,
  image: o.image ? o.image.src : null, style: o.racine.attrs.style, classe: o.racine.className,
  couvercle: appels.filter((a) => a.cible === o.couvercle && a.m === "gsap.set").map((a) => a.a.rotationX)[0],
  parties: [o.couvercle, o.ecran, o.base].map((e) => e.className),
  voulu: [o.base, o.image].map((e) => !!e && e.hasAttribute("data-layout-allow-overflow")),
}));
// La caméra qui s'approche d'un point (08/11/2026) : le point visé arrive au centre, et K.vu dit où le
// curseur doit aller pour le désigner une fois la caméra posée.
const z = K.zoom(scene, [300, 400], 1.3);
res.zoom = { z, vu: K.vu(scene, z, [300, 400]), coin: K.vu(scene, z, [0, 0]),
  ailleurs: K.vu(scene, K.zoom(scene, [300, 400], 2, { vers: [100, 120] }), [300, 400]),
  neutre: K.vu(scene, null, [10, 20]) };
// La courbe d'une plongée de ×1 à ×4 (09/11/2026) : avec la courbe de base linéaire du faux GSAP,
// l'échelle doit doubler à mi-chemin (×2), pas valoir ×2,5.
const ce = K.courbeEchelle(1, 4, "none");
res.courbe = { bornes: [ce(0), ce(1)], milieu: 1 + 3 * ce(0.5), plat: K.courbeEchelle(2, 2)(0.3) };

// L'apparition nette (09/11/2026) : un fondu court, sans montée, sans flou ni échelle.
appels.length = 0;
const ligne = el(scene, "k-mot");
K.apparition(tl, ligne, 1.2);
res.apparition = appels.filter((a) => a.cible === ligne).map((a) => ({ m: a.m, de: a.a, vers: a.b, t: a.c }));
// L'arrivée des objets : l'échelle peut rebondir, jamais l'opacité.
appels.length = 0;
const objet = new El("div"); objet.dataset.prof = "0.5"; objet.style.opacity = "0.7";
K.arrivee(tl, [objet], 0.4);
res.arrivee = appels.filter((a) => a.cible === objet).map((a) => ({ de: a.a, vers: a.b }));
// Le curseur se pose à son premier point dès la construction, même donné après 0.
appels.length = 0;
const cur = K.curseur(el(scene, ""), "c2", true);
K.trajet(tl, cur, [[1.5, 300, 400], [2, 500, 600, 0.4]]);
res.trajet = appels.filter((a) => a.cible === cur).map((a) => ({ m: a.m, x: a.a.x, y: a.a.y, t: a.b }));
// Le garde-fou des exemples, et le compteur qui affiche un emplacement sans compter.
res.emplacements = K.emplacements("s1", { nom: "[PRÉNOM]", liste: [{ prix: "[SON PRIX]" }, 12], vrai: "Inès" });
res.erreurs = erreurs.slice();
res.sansEmplacement = K.emplacements("s1", { nom: "Inès", cases: [2, 3] });
const chiffre = new El("div");
appels.length = 0;
K.compteur(tl, chiffre, 0, "[CHIFFRE]", 0.2, 1, 5);
res.compteur = { texte: chiffre.textContent, tweens: appels.length };
process.stdout.write(JSON.stringify(res));
"""


def interrupteur(largeur, hauteur):
    """Rectangle de l'interrupteur d'après kit.css (centré, `margin: <haut>px 0 0 -<moitié>px`)."""
    css = (KIT / "kit.css").read_text(encoding="utf-8")
    bloc = re.search(r"\.k-interrupteur \{([^}]*)\}", css).group(1)
    l = float(re.search(r"width:\s*([\d.]+)px", bloc).group(1))
    h = float(re.search(r"height:\s*([\d.]+)px", bloc).group(1))
    haut = float(re.search(r"margin:\s*([\d.]+)px", bloc).group(1))
    x0, y0 = largeur / 2 - l / 2, hauteur / 2 + haut
    return x0, y0, x0 + l, y0 + h


def pointe(clic):
    """La pointe de la flèche du curseur : (6.5, 3.5) dans un viewBox de 32, dessinée en 46 px."""
    return clic[0] + 6.5 * 46 / 32, clic[1] + 3.5 * 46 / 32


@unittest.skipUnless(shutil.which("node"), "Node absent")
class KitSelonLeFormat(unittest.TestCase):
    def lancer(self, largeur, hauteur, **cas):
        cas.update(kit=str(KIT / "kit.js"), largeur=largeur, hauteur=hauteur)
        sortie = subprocess.run(["node", "-e", HARNAIS, json.dumps(cas)], capture_output=True, text=True, timeout=60)
        self.assertEqual(sortie.returncode, 0, sortie.stderr)
        return json.loads(sortie.stdout)

    def test_cadre_lu_sur_l_hote_d_abord(self):
        """Une scène prête est écrite en 9:16 (sa racine à 1080 × 1920) : montée par un hôte en 16:9,
        elle prend le format de l'hôte (revue du 09/11/2026 : une colonne de 1080 px dans un 16:9)."""
        r = self.lancer(1920, 1080, hote=[1080, 1920])
        self.assertEqual(r["cadre"], {"largeur": 1920, "hauteur": 1080})
        # HyperFrames pose la racine intérieure à la taille écrite (1080 px) : elle prend celle de l'hôte.
        self.assertEqual(r["racine"], {"taille": ["1920", "1080"], "style": ["1920px", "1080px"]})
        self.assertEqual(self.lancer(1080, 1920, hote=[1920, 1080])["cadre"], {"largeur": 1080, "hauteur": 1920})
        # Même taille que l'hôte : rien ne change.
        self.assertEqual(self.lancer(1080, 1920, hote=[1080, 1920])["racine"]["style"], [None, None])

    def test_cadre_lu_sur_la_composition(self):
        self.assertEqual(self.lancer(1080, 1920)["cadre"], {"largeur": 1080, "hauteur": 1920})
        # Une scène sans taille prend celle de la composition qui l'englobe.
        self.assertEqual(self.lancer(1080, 1920, tailleMain=True)["cadre"], {"largeur": 1080, "hauteur": 1920})
        # Aucune taille nulle part : l'ancien défaut du kit.
        self.assertEqual(self.lancer(0, 0, sansTaille=True)["cadre"], {"largeur": 1920, "hauteur": 1080})

    def test_le_curseur_clique_sur_l_interrupteur(self):
        for largeur, hauteur in ((1080, 1920), (1920, 1080), (1080, 1350), (1080, 1080)):
            with self.subTest(format=(largeur, hauteur)):
                r = self.lancer(largeur, hauteur)
                x, y = pointe(r["clic"])
                x0, y0, x1, y1 = interrupteur(largeur, hauteur)
                self.assertTrue(x0 <= x <= x1 and y0 <= y <= y1, (r["clic"], (x0, y0, x1, y1)))
                dx, dy = r["depart"]
                self.assertTrue(0 <= dx <= largeur and 0 <= dy <= hauteur, r["depart"])

    def test_l_ordinateur_du_kit(self):
        """Un ordinateur en perspective CSS, comme le téléphone : la 3D de three.js a été retirée le
        08/11/2026 (trop coûteuse pour ce qu'elle apporte), l'ordinateur qui s'ouvre sur sa page reste."""
        ferme, ouvert = self.lancer(1920, 1080)["ordi"]
        self.assertGreater(ferme["touches"], 75)                       # un clavier touche par touche
        self.assertEqual(ferme["image"], "assets/images/page.png")      # sa vraie capture sur l'écran
        self.assertIsNone(ouvert["image"])                              # sans capture : l'écran reste noir
        self.assertIn("width:1000px; height:660px;", ferme["style"])
        self.assertEqual((ferme["couvercle"], ouvert["couvercle"]), (-86, 12))
        self.assertEqual(ouvert["classe"], "k-ordi k-ordi-gris")
        self.assertEqual(ferme["parties"], ["k-ordi-couvercle", "k-ordi-ecran", "k-ordi-base"])
        self.assertEqual(ferme["voulu"], [True, True])               # la base couchée, la page qui défile : pas un défaut
        css = (KIT / "kit.css").read_text(encoding="utf-8")
        for regle in (".k-ordi-base", ".k-ordi-couvercle", ".k-ordi-touche", ".k-ordi-pave", ".k-ordi-ecran img"):
            self.assertIn(regle + " {", css, regle)

    def test_le_zoom_amene_le_point_au_centre(self):
        """Une aide technique, pas un geste imposé : la caméra (origine au centre) qui amène un point de
        la scène au centre, et la place de ce point à l'écran pour y mener le curseur (V2 du Reel
        concept du 08/11/2026, où le calcul était écrit à la main)."""
        for largeur, hauteur in ((1080, 1920), (1920, 1080)):
            with self.subTest(format=(largeur, hauteur)):
                r = self.lancer(largeur, hauteur)["zoom"]
                self.assertEqual(sorted(r["z"]), ["scale", "x", "y"])     # rien d'autre : passé tel quel à GSAP
                self.assertEqual(r["z"]["scale"], 1.3)
                for v, attendu in zip(r["vu"], (largeur / 2, hauteur / 2)):
                    self.assertAlmostEqual(v, attendu)
                cx, cy = largeur / 2, hauteur / 2
                for v, attendu in zip(r["coin"], (cx + (0 - cx) * 1.3 + r["z"]["x"], cy + (0 - cy) * 1.3 + r["z"]["y"])):
                    self.assertAlmostEqual(v, attendu)
                for v, attendu in zip(r["ailleurs"], (100, 120)):
                    self.assertAlmostEqual(v, attendu)
                self.assertEqual(r["neutre"], [10, 20])

    def test_la_courbe_du_zoom_anime_le_logarithme_de_l_echelle(self):
        r = self.lancer(1080, 1920)["courbe"]
        self.assertEqual(r["bornes"], [0, 1])
        self.assertAlmostEqual(r["milieu"], 2.0)          # ×1 → ×4 : ×2 à mi-chemin, comme l'œil le perçoit
        self.assertAlmostEqual(r["plat"], 0.3)            # sans changement d'échelle : la courbe de base

    def test_16_9_inchange(self):
        # Les valeurs d'avant le passage au 9:16, à l'identique : aucun projet 16:9 ne bouge.
        r = self.lancer(1920, 1080)
        self.assertEqual(r["clic"], [978, 662])
        self.assertEqual(r["depart"], [1500, 1000])
        self.assertEqual(r["fantome"], [260, -60])
        self.assertAlmostEqual(r["fin"], 2.35)

    def test_l_apparition_est_nette(self):
        (a,) = self.lancer(1080, 1920)["apparition"]
        self.assertEqual(a["m"], "fromTo")
        self.assertEqual(a["de"], {"opacity": 0})
        self.assertEqual(a["vers"]["opacity"], 1)
        self.assertLessEqual(a["vers"]["duration"], 0.2)
        for prop in ("y", "x", "filter", "scale"):
            self.assertNotIn(prop, a["vers"])
        self.assertEqual(a["t"], 1.2)

    def test_l_opacite_ne_rebondit_jamais(self):
        tweens = self.lancer(1080, 1920)["arrivee"]
        for tw in tweens:
            if "opacity" in tw["vers"]:
                self.assertNotIn("back", tw["vers"].get("ease", ""), tw)
                self.assertNotIn("scale", tw["vers"])
                self.assertEqual(tw["vers"]["opacity"], 0.7)      # l'opacité que K.champ avait donnée
        self.assertTrue(any("scale" in tw["vers"] for tw in tweens))

    def test_le_curseur_se_pose_a_son_premier_point(self):
        trajet = self.lancer(1080, 1920)["trajet"]
        self.assertEqual(trajet[0], {"m": "gsap.set", "x": 300, "y": 400})   # dès la construction
        self.assertIn({"m": "set", "x": 300, "y": 400, "t": 1.5}, trajet)  # et à son instant
        self.assertIn({"m": "to", "x": 500, "y": 600, "t": 2}, trajet)

    def test_le_garde_fou_des_exemples(self):
        r = self.lancer(1080, 1920)
        self.assertEqual(r["emplacements"], ["[PRÉNOM]", "[SON PRIX]"])
        self.assertEqual(len(r["erreurs"]), 1)
        self.assertIn("[PRÉNOM], [SON PRIX]", r["erreurs"][0])
        self.assertEqual(r["sansEmplacement"], [])
        self.assertEqual(r["compteur"], {"texte": "[CHIFFRE]", "tweens": 0})

    def test_options_depart_et_cible(self):
        r = self.lancer(1080, 1920, options={"depart": [100, 200], "cible": [300, 400]})
        self.assertEqual(r["depart"], [100, 200])
        self.assertEqual(r["clic"], [300, 400])

    def test_fantome_hors_audit(self):
        self.assertTrue(self.lancer(1080, 1920)["fantomeIgnore"])

    def test_champ_dans_le_cadre(self):
        for largeur, hauteur in ((1080, 1920), (1920, 1080)):
            with self.subTest(format=(largeur, hauteur)):
                objets = self.lancer(largeur, hauteur)["objets"]
                self.assertTrue(all(0 <= o["x"] <= largeur and 0 <= o["y"] <= hauteur for o in objets))
                # Répartis sur tout le cadre, pas tassés dans un coin.
                self.assertGreater(max(o["x"] for o in objets), largeur * 0.8)
                self.assertGreater(max(o["y"] for o in objets), hauteur * 0.8)

    def test_zone_donnee_respectee(self):
        zone = {"x0": 100, "y0": 300, "x1": 500, "y1": 900}
        objets = self.lancer(1080, 1920, zone=zone)["objets"]
        self.assertTrue(all(100 <= o["x"] <= 500 and 300 <= o["y"] <= 900 for o in objets))


class KitTexte(unittest.TestCase):
    def test_plus_de_taille_16_9_en_dur(self):
        js = (KIT / "kit.js").read_text(encoding="utf-8")
        self.assertNotIn("960 + 18", js)
        self.assertNotIn("x1: 1920, y1: 1080", js)
        self.assertIn("K.cadre = function", js)
        self.assertNotIn("Math.random", js)
        self.assertNotIn("Date.now", js)
        self.assertNotIn("performance.now", js)

    def test_fantome_proportionnel_a_la_largeur(self):
        css = (KIT / "kit.css").read_text(encoding="utf-8")
        chapitre = re.search(r"\.k-chapitre \{([^}]*)\}", css).group(1)
        self.assertIn("container-type: inline-size", chapitre)
        fantome = re.search(r"\.k-fantome \{([^}]*)\}", css).group(1)
        cqw = float(re.search(r"font-size:\s*([\d.]+)cqw", fantome).group(1))
        self.assertAlmostEqual(cqw * 1920 / 100, 300)   # 300 px en 16:9, comme avant
        self.assertLess(cqw * 1080 / 100, 200)          # et non plus 300 px en 9:16

    def test_couleurs_de_la_marque(self):
        """Revue du 09/11/2026 : le texte posé sur l'accent prend l'encre que la marque a choisie pour
        lui, et la nuit du kit est celle de la marque (les gris du kit restent pour les interfaces)."""
        css = re.sub(r"/\*.*?\*/", "", (KIT / "kit.css").read_text(encoding="utf-8"), flags=re.S)
        regles = dict((m.group(1).strip(), m.group(2)) for m in re.finditer(r"([^{}]+)\{([^}]*)\}", css))
        for sel, val in regles.items():
            if "k-sur-accent" in sel or "k-tuile-accent" in sel or "k-fond-accent .k-logo-nu" in sel:
                with self.subTest(sel):
                    self.assertNotIn("--k-encre", val)
                    self.assertIn("--brand-contrast", val)
        self.assertIn("var(--brand-sombre", regles[".k-fond-sombre"])
        self.assertNotIn("--k-gris:", css)   # inutilisé

    def test_rien_que_gsap_deplace_n_a_de_transformation_css(self):
        css = (KIT / "kit.css").read_text(encoding="utf-8")
        fantome = re.sub(r"/\*.*?\*/", "", re.search(r"\.k-fantome \{([^}]*)\}", css).group(1), flags=re.S)
        self.assertNotRegex(fantome, r"transform\s*:")

    def test_seule_la_capture_du_telephone_le_remplit(self):
        css = (KIT / "kit.css").read_text(encoding="utf-8")
        self.assertIn(".k-tel-ecran > img {", css)
        self.assertNotIn(".k-tel-ecran img {", css)

    def test_mode_d_emploi(self):
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        self.assertIn('data-width="1080" data-height="1920"', md)
        self.assertIn('id="s3-curseur-calque"', md)          # jamais un identifiant intérieur en -hote
        for option in ("K.apparition(", "K.emplacements(", "K.entre(a, b, p)", "{ease, longueur}", "{de, a, duree, ecart}",
                       "{svg, courbe, classe, taille}", "{etalement, duree, ease, ordre, graine}", "`k-ligne`"):
            self.assertIn(option, md, option)
        self.assertIn("data-layout-ignore", md)
        self.assertNotIn("kit de l'extension", md)

    def test_chaque_fonction_a_son_mode_d_emploi(self):
        # Une fonction du kit que kit.md ne nomme pas, l'agent ne s'en sert jamais (relevé Katana du
        # 07/11/2026 : le mot qui joue, le schéma, le fil rouge, la coupe).
        js = (KIT / "kit.js").read_text(encoding="utf-8")
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        fonctions = sorted(set(re.findall(r"\bK\.(\w+) = function", js)))
        self.assertIn("tranche", fonctions)
        manquantes = [f for f in fonctions if f"K.{f}" not in md]
        self.assertEqual(manquantes, [])



class ObjetsConnus(unittest.TestCase):
    """Les objets connus, dans leurs vraies couleurs (08/11/2026 : « jaune, noir, blanc, on ne voit que
    ça ») : chargés par chaque projet, sans identifiant qui se dédouble, tous au mode d'emploi."""
    OBJETS = ("dossier", "fichier", "pdf", "doc", "tableur", "presentation", "video", "image", "audio", "zip")

    def test_chaque_objet_existe_et_se_copie_sans_conflit(self):
        js = (KIT / "objets.js").read_text(encoding="utf-8")
        for nom in self.OBJETS:
            self.assertIn(f'"objet-{nom}"', js, nom)
        self.assertNotIn(' id="', js)                   # deux copies d'un même objet ne se gênent pas
        self.assertNotIn("<script", js.split("*/", 1)[1])

    def test_chaque_projet_les_charge_avant_le_kit(self):
        gabarit = (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8")
        ordre = [gabarit.index(f'src="kit/{f}"') for f in ("icones.js", "objets.js", "ajouts.js", "kit.js")]
        self.assertEqual(ordre, sorted(ordre))

    def test_le_mode_d_emploi_les_nomme(self):
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        for nom in ("objet-dossier", "objet-pdf", "K.statut", "K.notification", "K.bulle", "k-objet"):
            self.assertIn(nom, md, nom)


class SansThreeJs(unittest.TestCase):
    """08/11/2026 : la 3D en three.js est retirée (Alex : trop de complexité et d'abonnement pour une vidéo
    qui doit vendre). Le kit garde ses objets en perspective CSS ; sync retire les fichiers chez le client."""

    def test_ni_three_ni_plan3d(self):
        self.assertNotIn("three", json.loads((RACINE / "package.json").read_text(encoding="utf-8"))["devDependencies"])
        for f in ("plan3d.js", "briques3d.js", "matieres3d.js"):
            self.assertFalse((KIT / f).exists(), f)
        self.assertNotIn("importmap", (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8"))
        sync = (RACINE / "scripts" / "sync.mjs").read_text(encoding="utf-8")
        for f in ('"templates/kit/plan3d.js"', '"assets/vendor/three.module.min.js"', '"assets/vendor/three-addons"'):
            self.assertIn(f, sync, f)


if __name__ == "__main__":
    unittest.main()
