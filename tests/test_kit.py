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
const corps = new El("body"), appels = [];
const tl = {};
["to", "fromTo", "set"].forEach((m) => { tl[m] = (cible, a, b, c) => { appels.push({ m, cible, a, b, c }); return tl; }; });
const gsap = { set: (cible, vars) => appels.push({ m: "gsap.set", cible, a: vars }), parseEase: () => (p) => p };
const document = { createElement: (tag) => new El(tag), querySelector: (sel) => corps.querySelector(sel) };
const window = {};
const ctx = vm.createContext({ window, document, gsap });
vm.runInContext(fs.readFileSync(cas.kit, "utf8"), ctx);
const K = window.K;

// Une composition principale et une scène (sous-composition) de la taille demandée.
const attrsTaille = cas.sansTaille ? {} : { "data-width": String(cas.largeur), "data-height": String(cas.hauteur) };
const main = el(corps, "", Object.assign({ "data-composition-id": "main" }, cas.tailleMain ? attrsTaille : {}));
const scene = el(main, "", Object.assign({ "data-composition-id": "s1" }, cas.tailleMain ? {} : attrsTaille));
const res = {};
res.cadre = K.cadre ? K.cadre(scene) : null;

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

    def test_16_9_inchange(self):
        # Les valeurs d'avant le passage au 9:16, à l'identique : aucun projet 16:9 ne bouge.
        r = self.lancer(1920, 1080)
        self.assertEqual(r["clic"], [978, 662])
        self.assertEqual(r["depart"], [1500, 1000])
        self.assertEqual(r["fantome"], [260, -60])
        self.assertAlmostEqual(r["fin"], 2.35)

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

    def test_mode_d_emploi(self):
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        self.assertIn('data-width="1080" data-height="1920"', md)
        self.assertIn("data-layout-ignore", md)
        self.assertNotIn("kit de l'extension", md)


if __name__ == "__main__":
    unittest.main()
