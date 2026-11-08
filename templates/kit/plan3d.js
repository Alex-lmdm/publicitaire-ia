/* La 3D du kit : un plan en vraie 3D (three.js), quand il sert (scenes.md, « La 3D, quand elle
   sert » ; le mode d'emploi : kit.md, « La 3D »). Ce module fait la plomberie ; la scène ne décrit
   que ses objets et leur pose :

     import { plan3d } from "./kit/plan3d.js";
     plan3d(document.getElementById("s5-vue"), async ({ THREE, scene, camera, distance, courbe, … }) => {
       … crée les objets …
       return (t) => { … pose les objets et la caméra d'après t seul (secondes depuis le début du plan) … };
     });

   - Le plan dure ce que dure l'hôte de sa sous-composition (data-start, data-duration).
   - Chaque image se dessine d'après son instant seul (`hf-seek` de HyperFrames, comme son exemple
     path-traced-3d) : jamais d'horloge, de minuterie, de requestAnimationFrame ni de Math.random
     (le hasard voulu : `hasard()`, toujours le même), sinon l'aperçu et le rendu diffèrent.
   - Fond transparent : le fond du kit (la nuit, le clair, l'aplat) se voit derrière les objets.
   - Les couleurs : les matières éclairées restent neutres (gris, blanc, noir, alu, verre) ; une
     couleur (celle de la marque, celle d'un objet connu) se pose en aplat, sans lumière (`aplat`) :
     éclairée, elle s'assombrit en teintes hors de sa palette (un jaune vire à l'olive).
   - Le kit (kit.js) est chargé avant : `K.cadre`, `K.jeton`, `K.rng`, `K.ic` servent ici.
   three.js : licence MIT, copié de node_modules par `npm run sync` dans assets/vendor/. */
import * as THREE from "../assets/vendor/three.module.min.js";

const K = window.K;

export function plan3d(canvas, construire, options = {}) {
  if (!canvas) throw new Error("plan3d : le canvas manque (un id faux ?)");
  if (!K) throw new Error("plan3d : le kit (kit/kit.js) n'est pas chargé dans index.html");
  const hote = canvas.closest("[data-start]");
  const debut = Number(hote?.dataset.start || 0), fin = Number(hote?.dataset.duration) || Infinity;
  const { largeur: L, hauteur: H } = K.cadre(canvas);
  canvas.width = L; canvas.height = H;

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(L, H, false);
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NeutralToneMapping;     // des blancs et des gris qui restent neutres
  renderer.shadowMap.enabled = options.ombre !== false;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.environment = studio(renderer);                // des reflets de studio doux, sans décor
  scene.environmentIntensity = 0.9;
  // `angle` : l'angle de vue vertical en degrés (plus petit = plus serré, comme un téléobjectif).
  const camera = new THREE.PerspectiveCamera(options.angle ?? 26, L / H, 0.1, 100);
  camera.position.set(0, 0.3, 7);

  // Une lumière principale, douce, qui porte l'ombre ; un remplissage neutre.
  const cle = new THREE.DirectionalLight(0xffffff, 2.2);
  cle.position.set(-3, 6, 4);
  cle.castShadow = options.ombre !== false;
  cle.shadow.mapSize.set(2048, 2048); cle.shadow.radius = 8; cle.shadow.bias = -0.0004;
  Object.assign(cle.shadow.camera, { left: -5, right: 5, top: 5, bottom: -5 });
  scene.add(cle, new THREE.HemisphereLight(0xffffff, 0x444444, 0.6));

  const outils = {
    THREE, scene, camera, renderer, lumiere: cle, largeur: L, hauteur: H,
    /** un hasard toujours le même (graine fixe) : placer des objets « au hasard » sans que deux rendus diffèrent */
    hasard: K.rng(1),
    /** une courbe de GSAP, à appliquer à une progression de 0 à 1 : courbe("expo.out")(p) */
    courbe: (nom) => window.gsap.parseEase(nom),
    /** une couleur de sa marque (THREE.Color) : jeton("--brand-accent") */
    jeton: (nom) => new THREE.Color(K.jeton(nom) || "#808080"),
    /** une matière en aplat, sans lumière : la couleur reste exactement elle (la marque, un objet connu) */
    aplat: (couleur, extra = {}) => new THREE.MeshBasicMaterial({ color: couleur, toneMapped: false, ...extra }),
    /** une image en texture : un fichier du projet ("assets/images/page.png") ou un SVG du kit
        (K.ic("logo-stripe"), K.ic("objet-pdf")) ; `couleur` remplace currentColor d'un SVG d'un seul trait */
    texture: async (src, { taille = 1024, couleur = "#000000" } = {}) => {
      let t;
      if (String(src).trim().startsWith("<svg")) {
        const vb = /viewBox="([^"]+)"/.exec(src);
        const [, , w, h] = vb ? vb[1].trim().split(/[\s,]+/).map(Number) : [0, 0, 1, 1];
        const haut = Math.round(taille * (h / w || 1));
        const svg = String(src).replace(/currentColor/g, couleur)
          .replace(/<svg\b/, `<svg width="${taille}" height="${haut}"`);
        const img = new Image();
        img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
        await img.decode();
        const c = document.createElement("canvas");
        c.width = taille; c.height = haut;
        c.getContext("2d").drawImage(img, 0, 0, taille, haut);
        t = new THREE.CanvasTexture(c);
      } else {
        t = await new THREE.TextureLoader().loadAsync(src);
      }
      t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
      return t;
    },
    /** un rectangle aux coins ronds (l × h, rayon r), centré : la forme d'un téléphone, d'une carte,
        d'un écran, d'une pastille, à extruder (THREE.ExtrudeGeometry) ou à poser à plat (ShapeGeometry) */
    arrondi,
    /** ramène les coordonnées de texture d'une ShapeGeometry de l × h à 0..1 (une image qui remplit la forme) */
    plaquer: (geometrie, l, h) => {
      const uv = geometrie.attributes.uv;
      for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / l + 0.5, uv.getY(i) / h + 0.5);
      return geometrie;
    },
    /** un sol invisible qui ne garde que l'ombre (neutre), à la hauteur y : jamais sur l'aplat */
    sol: (y = -1, opacite = 0.22) => {
      const s = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.ShadowMaterial({ opacity: opacite }));
      s.rotation.x = -Math.PI / 2; s.position.y = y; s.receiveShadow = true; scene.add(s);
      return s;
    },
    /** la distance de la caméra pour qu'un objet de l × h (face à elle) occupe `part` du cadre, en
        largeur ou en hauteur selon ce qui bloque : le même plan se cadre en 16:9 comme en 9:16 */
    distance: (l, h, part = 0.6) => {
      const v = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));
      return Math.max(h / (part * 2 * v), l / (part * 2 * v * camera.aspect));
    },
  };

  const pixel = new Uint8Array(4);
  const attendreGpu = () => {           // un pixel relu : l'image est vraiment finie (même sans carte graphique)
    const gl = renderer.getContext();
    gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixel);
  };
  let poser = null, montre = null;
  const pret = (async () => {
    poser = await construire(outils);
    if (typeof poser !== "function") throw new Error("plan3d : construire doit rendre poser(t)");
    poser(0);
    await renderer.compileAsync(scene, camera);
    renderer.render(scene, camera);
    attendreGpu();
  })();
  window.__hf = window.__hf || {};
  window.__hf.buildReady = window.__hf.buildReady || {};
  window.__hf.buildReady["plan3d-" + (canvas.id || debut)] = pret;

  // HyperFrames attend que chaque sous-composition déclare sa timeline (45 s, puis il passe) : une scène
  // en 3D sans mots animés n'en a pas, on lui en donne une vide. Celle de la scène, si elle en a une,
  // la remplace.
  const compo = canvas.closest("[data-composition-id]")?.dataset.compositionId;
  window.__timelines = window.__timelines || {};
  if (compo && compo !== "main" && !window.__timelines[compo] && window.gsap) {
    window.__timelines[compo] = window.gsap.timeline({ paused: true });
  }

  let file = pret;
  window.addEventListener("hf-seek", (ev) => {
    const t = Math.min(fin, Math.max(0, ev.detail.time - debut));   // hors du plan : sa première ou sa dernière image
    file = file.catch(() => {}).then(() => pret).then(() => {
      if (t === montre) return;
      poser(t);
      renderer.render(scene, camera);
      attendreGpu();
      montre = t;
    });
    ev.detail.waitUntil(file);
  });
  return pret;
}

function arrondi(l, h, r) {
  const s = new THREE.Shape(), x = -l / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + l - r, y); s.quadraticCurveTo(x + l, y, x + l, y + r);
  s.lineTo(x + l, y + h - r); s.quadraticCurveTo(x + l, y + h, x + l - r, y + h);
  s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  return s;
}

// Un studio pour les reflets : une boîte sombre et trois panneaux lumineux, passée au PMREM.
function studio(renderer) {
  const s = new THREE.Scene();
  s.add(new THREE.Mesh(new THREE.BoxGeometry(20, 20, 20), new THREE.MeshBasicMaterial({ color: 0x202020, side: THREE.BackSide })));
  const panneau = (x, y, z, l, h, i) => {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(l, h), new THREE.MeshBasicMaterial({ color: new THREE.Color(i, i, i) }));
    m.position.set(x, y, z); m.lookAt(0, 0, 0); s.add(m);
  };
  panneau(-6, 4, 5, 6, 3, 3); panneau(7, 2, 3, 3, 8, 2); panneau(0, 8, -4, 10, 2, 1.5);
  return new THREE.PMREMGenerator(renderer).fromScene(s, 0.04).texture;
}
