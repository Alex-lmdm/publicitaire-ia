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

    def test_chaque_fonction_a_son_mode_d_emploi(self):
        # Une fonction du kit que kit.md ne nomme pas, l'agent ne s'en sert jamais (relevé Katana du
        # 07/11/2026 : le mot qui joue, le schéma, le fil rouge, la coupe).
        js = (KIT / "kit.js").read_text(encoding="utf-8")
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        fonctions = sorted(set(re.findall(r"\bK\.(\w+) = function", js)))
        self.assertIn("tranche", fonctions)
        manquantes = [f for f in fonctions if f"K.{f}" not in md and f not in ("entre",)]
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



class TroisD(unittest.TestCase):
    """La 3D du kit (three.js, 08/11/2026) : un outil, pas des plans imposés. Il importe three.js copié par
    `npm run sync`, ne lit aucune horloge, et son mode d'emploi le nomme."""

    def test_le_module_et_son_contrat(self):
        js = (KIT / "plan3d.js").read_text(encoding="utf-8")
        self.assertIn('from "../assets/vendor/three.module.min.js"', js)
        self.assertIn("export function plan3d(", js)
        self.assertIn('addEventListener("hf-seek"', js)           # chaque image d'après son instant
        self.assertIn("buildReady", js)
        self.assertIn("preserveDrawingBuffer: true", js)
        code = re.sub(r"/\*.*?\*/|//[^\n]*", "", js, flags=re.S)   # hors commentaires
        for horloge in ("requestAnimationFrame(", "Date.now(", "performance.now(", "setTimeout(", "setInterval(",
                        "Math.random"):
            self.assertNotIn(horloge, code, horloge)
        self.assertIn("K.rng(", code)                               # le hasard du kit, pas le sien
        self.assertIn("Math.min(fin,", code)                        # hors du plan : il ne redessine plus

    def test_l_exemple_de_kit_md_suit_les_regles(self):
        """L'IA copie l'exemple : une matière éclairée y reste neutre (l'accent éclairé vire à l'olive),
        il se cadre par `distance` (9:16 comme 16:9) et cache ses mots dès la construction."""
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        exemple = re.search(r"```html\n(.*?)```", md.split("## La 3D : `kit/plan3d.js`", 1)[1], re.S).group(1)
        self.assertIn("distance(", exemple)
        self.assertIn("K.cacher(", exemple)
        self.assertNotIn("tl.set(\"#s5-titre\", { autoAlpha: 0 }, 0)", exemple)
        for eclairee in re.findall(r"Mesh(?:Standard|Physical)Material\(\{[^}]*\}", exemple):
            self.assertNotIn("--brand-accent", eclairee)

    def test_sync_le_copie_et_le_mode_d_emploi_le_nomme(self):
        sync = (RACINE / "scripts" / "sync.mjs").read_text(encoding="utf-8")
        self.assertIn('"build/three.module.min.js"', sync)
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        for nom in ("plan3d(", "poser(t)", "jeton(", "texture(", "arrondi(", "plaquer(", "sol(", "distance(",
                    "courbe(", "aplat(", "hasard()", "snapshot --at 2,0,2"):
            self.assertIn(nom, md, nom)
        scenes = (RACINE / ".claude" / "skills" / "studio" / "references" / "scenes.md").read_text(encoding="utf-8")
        self.assertIn("## La 3D, quand elle sert", scenes)


# Les briques et les matières de la 3D, construites dans Node : three.js vient de node_modules (comme
# l'import map le fait dans le navigateur), un faux canvas note chaque texture peinte (son empreinte),
# et Math.random lève une erreur s'il est appelé depuis nos fichiers.
HARNAIS_3D = r"""
import { pathToFileURL } from "node:url";
const [briquesJs] = process.argv.slice(-1);
let empreinte = 2166136261;
const noter = (d) => { for (let i = 0; i < d.length; i += 7) empreinte = Math.imul(empreinte ^ d[i], 16777619) >>> 0; };
const ctx = new Proxy({}, { get: (o, k) => k in o ? o[k]
  : k === "createImageData" ? (l, h) => ({ data: new Uint8ClampedArray(l * h * 4) })
  : k === "putImageData" ? (img) => noter(img.data) : () => {}, set: (o, k, v) => { o[k] = v; return true; } });
globalThis.document = { createElement: () => ({ width: 0, height: 0, getContext: () => ctx }), fonts: { load: async () => [] } };
globalThis.window = { K: {
  rng: (g) => { let s = (g >>> 0) || 1; return () => { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; },
  jeton: () => "" } };
const hasard = Math.random;   // three.js en tire ses identifiants internes (sans effet sur l'image) ; nos fichiers jamais
Math.random = () => { if (/briques3d|matieres3d/.test(new Error().stack.split("\n")[2] || "")) throw new Error("Math.random appelé"); return hasard(); };
const THREE = await import("three");
const { fabriquerBriques } = await import(pathToFileURL(briquesJs).href);
const arrondi = (l, h, r) => { const s = new THREE.Shape(), x = -l / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + l - r, y); s.quadraticCurveTo(x + l, y, x + l, y + r); s.lineTo(x + l, y + h - r);
  s.quadraticCurveTo(x + l, y + h, x + l - r, y + h); s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y); return s; };
const outils = { arrondi, plaquer: (g) => g, aplat: (c, e = {}) => new THREE.MeshBasicMaterial({ color: c, toneMapped: false, ...e }),
  texture: async () => { const t = new THREE.Texture(); t.image = { width: 1440, height: 3240 }; return t; } };
const b = fabriquerBriques(outils);
const ordi = await b.ordinateur({ ecran: "page.png", ouvert: 0 });
const ferme = ordi.couvercle.rotation.x; ordi.ouvrir(1);
const tel = await b.telephone({ ecran: "app.png" }), tab = await b.tablette({}), carnet = await b.carnet({ titre: "Offre" });
const crayon = b.crayon(), plateau = b.plateau({}), classe = [b.pupitre(), b.chaise(), b.tableau()];
const tasse = b.tasse({ cafe: true }), corps = tasse.children[0].geometry;
const p = corps.attributes.position, n = corps.attributes.normal;   // la paroi extérieure : ses normales regardent dehors
let dehors = 0, total = 0;
for (let i = 0; i < p.count; i++) {
  const r = Math.hypot(p.getX(i), p.getZ(i));
  if (Math.abs(r - 0.41) < 1e-3 && p.getY(i) > 0.03 && p.getY(i) < 0.97) { total++; if (n.getX(i) * p.getX(i) + n.getZ(i) * p.getZ(i) > 0) dehors++; }
}
const meshes = (o) => { let k = 0; o.traverse((x) => { if (x.isMesh) k++; }); return k; };
console.log(JSON.stringify({ empreinte, ferme, ouvert: ordi.couvercle.rotation.x, touches: meshes(ordi), tel: meshes(tel),
  tab: meshes(tab), carnet: meshes(carnet), crayon: meshes(crayon), plateau: meshes(plateau), classe: classe.map(meshes), dehors, total,
  dims: [ordi.dimensions.l, tel.dimensions.h, carnet.dimensions.e], defiler: typeof tel.defiler, cote: tasse.side }));
"""


@unittest.skipUnless(shutil.which("node") and (RACINE / "node_modules" / "three").is_dir(), "Node ou three.js absent")
class Briques3D(unittest.TestCase):
    """Les briques de la 3D poussée (08/11/2026) : construites pièce par pièce, sans hasard du navigateur,
    les mêmes textures à chaque chargement (le rendu ouvre plusieurs navigateurs en parallèle)."""

    @classmethod
    def setUpClass(cls):
        def lancer():
            r = subprocess.run(["node", "--input-type=module", "-e", HARNAIS_3D, str(KIT / "briques3d.js")],
                               cwd=RACINE, capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                raise AssertionError(r.stderr[-1500:])
            return json.loads(r.stdout.strip().splitlines()[-1])
        cls.a, cls.b = lancer(), lancer()

    def test_les_briques_se_construisent_piece_par_piece(self):
        self.assertGreater(self.a["touches"], 80)          # l'ordinateur : chaque touche est une pièce
        self.assertGreater(self.a["tel"], 10)
        self.assertGreater(self.a["carnet"], 40)           # la spirale, anneau par anneau
        self.assertGreaterEqual(self.a["crayon"], 7)
        self.assertEqual(len(self.a["classe"]), 3)         # le pupitre, la chaise, le tableau : un décor de classe
        self.assertTrue(all(n >= 6 for n in self.a["classe"]), self.a["classe"])
        self.assertEqual(self.a["defiler"], "function")
        self.assertAlmostEqual(self.a["dims"][0], 3.04)    # 1 unité = 10 cm : un 13 pouces fait 30,4 cm

    def test_l_ordinateur_s_ouvre(self):
        self.assertAlmostEqual(self.a["ferme"], 3.14159 / 2, places=3)                  # fermé : à plat
        self.assertAlmostEqual(self.a["ouvert"], 3.14159 / 2 - 110 * 3.14159 / 180, places=3)

    def test_les_textures_sont_les_memes_a_chaque_chargement(self):
        self.assertEqual(self.a["empreinte"], self.b["empreinte"])

    def test_la_tasse_regarde_dehors(self):
        """Un profil tourné à l'envers : la lumière le cache, l'objectif non (un halo flou autour)."""
        self.assertGreater(self.a["total"], 0)
        self.assertEqual(self.a["dehors"], self.a["total"])


class TroisDPoussee(unittest.TestCase):
    """Le niveau b : l'import map, les modules de three copiés par sync, les effets déterministes, les
    aplats exacts sous le rendu photographique, et le mode d'emploi qui nomme tout."""

    def test_l_import_map_vient_avant_tout_script(self):
        gabarit = (RACINE / "templates" / "projet" / "index.html.tpl").read_text(encoding="utf-8")
        m = re.search(r'<script type="importmap">(.*?)</script>', gabarit, re.S)
        self.assertIsNotNone(m)
        self.assertEqual(json.loads(m.group(1))["imports"], {"three": "./assets/vendor/three.module.min.js",
                                                             "three/addons/": "./assets/vendor/three-addons/"})
        self.assertLess(m.start(), gabarit.index("<script src="))

    def test_chaque_module_appele_est_copie_par_sync(self):
        sync = (RACINE / "scripts" / "sync.mjs").read_text(encoding="utf-8")
        liste = re.search(r"export const MODULES_THREE = \[(.*?)\];", sync, re.S).group(1)
        for f in ("plan3d.js", "briques3d.js", "matieres3d.js"):
            for module in re.findall(r'"three/addons/([^"]+)"', (KIT / f).read_text(encoding="utf-8")):
                self.assertIn(f'"{module}"', liste, f"{f} : {module}")

    def test_rien_ne_depend_de_l_horloge_ni_du_hasard(self):
        for f in ("plan3d.js", "briques3d.js", "matieres3d.js"):
            code = re.sub(r"/\*.*?\*/|//[^\n]*", "", (KIT / f).read_text(encoding="utf-8"), flags=re.S)
            for horloge in ("requestAnimationFrame(", "Date.now(", "performance.now(", "setTimeout(", "setInterval(",
                            "Math.random"):
                self.assertNotIn(horloge, code, f"{f} : {horloge}")
        js = (KIT / "plan3d.js").read_text(encoding="utf-8")
        self.assertIn("generateNoise(", js)              # le bruit de l'ombre de contact, à graine fixe
        self.assertIn("new SimplexNoise({ random: K.rng(", js)
        self.assertIn("Math.round(t * 30)", js)          # le grain suit le numéro de l'image

    def test_les_aplats_restent_exacts_sous_le_rendu_photographique(self):
        """Le tampon des effets applique le rendu de chaque matière (les aplats aucun) ; la sortie ne
        fait que convertir. Sans cela, la capture du client sur un écran prendrait la teinte du film."""
        js = (KIT / "plan3d.js").read_text(encoding="utf-8")
        self.assertIn("rt.isXRRenderTarget = true", js)
        self.assertIn("rt.texture.colorSpace = THREE.LinearSRGBColorSpace", js)
        self.assertIn("r.toneMapping = THREE.NoToneMapping", js)
        self.assertIn("toneMapped: false", js)
        # la vitre d'un écran ne garde qu'un peu de la pièce : un reflet franc voilait sa capture (essai du 08/11/2026)
        self.assertIn("m.userData?.reflet !== undefined", js)
        force = re.search(r"export function reflet\(\{ force = ([\d.]+) \}", (KIT / "matieres3d.js").read_text(encoding="utf-8"))
        self.assertLessEqual(float(force.group(1)), 0.2)

    def test_le_mode_d_emploi_nomme_les_outils_et_les_briques(self):
        md = (RACINE / ".claude" / "skills" / "studio" / "references" / "kit.md").read_text(encoding="utf-8")
        for nom in ("focale:", 'lumiere: "fenetre"', "ouverture:", "contact: true", "finition: true", "net(",
                    "briques.ordinateur(", "briques.telephone(", "briques.tablette(", "briques.carnet(",
                    "briques.crayon(", "briques.tasse(", "briques.plateau(", "briques.pupitre(", "briques.chaise(",
                    "briques.tableau(", "orbite(", "bois(", "papier(", "alu(",
                    "impression(", "data-plateau", "data-layout-allow-overflow", "importmap"):
            self.assertIn(nom, md, nom)
        plateau = re.findall(r"```html\n(.*?)```", md.split("### Niveau b : un plateau", 1)[1], re.S)
        self.assertIn('lumiere: "fenetre"', plateau[0])
        self.assertIn("data-layout-allow-overflow", plateau[0])
        self.assertIn("jeton(", plateau[0])               # la couverture à sa marque, jamais en dur
        self.assertNotRegex(plateau[0], r"couverture: \"#")
        self.assertIn("data-plateau", plateau[1])         # l'hôte du plateau

    def test_les_deux_niveaux_sont_ecrits(self):
        ref = RACINE / ".claude" / "skills" / "studio"
        scenes = (ref / "references" / "scenes.md").read_text(encoding="utf-8")
        section = scenes.split("## La 3D, quand elle sert", 1)[1].split("## Combiner", 1)[0]
        for mot in ("3D : a", "3D : b", "plateau", "Détaillé", "data-plateau", "Le héros reste sa vraie matière"):
            self.assertIn(mot, section, mot)
        self.assertNotIn("**Simple**", section)
        self.assertIn("Le plateau de la 3D poussée", (ref / "references" / "image.md").read_text(encoding="utf-8"))
        self.assertIn("data-plateau", (ref / "styles" / "README.md").read_text(encoding="utf-8"))
        self.assertIn("plan de plateau", (ref / "references" / "revue.md").read_text(encoding="utf-8"))
        skill = (ref / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Des plans en 3D dans ta vidéo ?", skill)
        self.assertIn("abonnement Claude ou ChatGPT", skill)


if __name__ == "__main__":
    unittest.main()
