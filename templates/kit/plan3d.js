/* La 3D du kit : un plan en vraie 3D (three.js), quand il sert (scenes.md, « La 3D, quand elle
   sert »). Ce module fait la plomberie, la scène ne décrit que ses objets et leur pose :

     import { plan3d } from "./kit/plan3d.js";
     plan3d(document.getElementById("s5-vue"), async ({ THREE, scene, camera, jeton, texture, arrondi }) => {
       … crée les objets (une capture en texture : await texture("assets/images/page.png")) …
       return (t) => { … pose les objets et la caméra d'après t seul (secondes depuis le début du plan) … };
     });

   - Le plan dure ce que dure son porteur : le canvas posé à la racine d'index.html (ses data-start et
     data-duration), ou l'hôte de la sous-composition qui le contient.
   - Chaque image se dessine d'après son instant seul (`hf-seek` de HyperFrames, comme son exemple
     path-traced-3d) : jamais d'horloge, de minuterie, de requestAnimationFrame ni de Math.random libre
     (le hasard de la construction est fixé), sinon deux rendus ne donnent pas les mêmes images.
   - Fond transparent : le fond du kit (la nuit, le clair, l'aplat) se voit derrière les objets.
   - Les couleurs : `jeton("--brand-accent")` rend une couleur de la marque ; les objets connus gardent
     les leurs (image.md, « Les objets connus »). Une ombre au sol, jamais sur l'aplat (elle y vire à
     l'olive) : `ombre: false` dans les options, ou un fond de nuit ou de clair.
   three.js : licence MIT, copié de node_modules par `npm run sync` dans assets/vendor/. */
import * as THREE from "../assets/vendor/three.module.min.js";

export { THREE };

let plans = 0;

export function plan3d(canvas, construire, options = {}) {
  if (!canvas) throw new Error("plan3d : le canvas manque (un id faux ?)");
  const porteur = canvas.closest("[data-start]");
  const debut = Number(porteur?.dataset.start || 0);
  const racine = canvas.closest("[data-width]");
  const L = Number(racine?.dataset.width) || canvas.width, H = Number(racine?.dataset.height) || canvas.height;
  canvas.width = L; canvas.height = H;

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(L, H, false);
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NeutralToneMapping;     // garde les couleurs de la marque fidèles
  renderer.shadowMap.enabled = options.ombre !== false;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.environment = studio(renderer);                // des reflets de studio doux, sans décor
  scene.environmentIntensity = options.reflets ?? 0.9;
  const camera = new THREE.PerspectiveCamera(options.focale ?? 26, L / H, 0.1, 100);
  camera.position.set(0, 0.3, 7);

  // Une lumière principale, douce, qui porte l'ombre ; un remplissage neutre.
  const cle = new THREE.DirectionalLight(0xffffff, 2.2);
  cle.position.set(-3, 6, 4);
  cle.castShadow = options.ombre !== false;
  cle.shadow.mapSize.set(2048, 2048); cle.shadow.radius = 8; cle.shadow.bias = -0.0004;
  Object.assign(cle.shadow.camera, { left: -5, right: 5, top: 5, bottom: -5 });
  scene.add(cle, new THREE.HemisphereLight(0xffffff, 0x444444, 0.6));

  const css = getComputedStyle(document.documentElement);
  const outils = {
    THREE, scene, camera, renderer, lumiere: cle, largeur: L, hauteur: H,
    /** une couleur de la marque : jeton("--brand-accent") */
    jeton: (nom) => new THREE.Color(css.getPropertyValue(nom).trim() || "#808080"),
    /** une image du projet en texture (une capture, un logo en PNG), prête à poser */
    texture: async (src) => {
      const t = await new THREE.TextureLoader().loadAsync(src);
      t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
      return t;
    },
    /** un rectangle aux coins ronds (l × h, rayon r), centré : la forme d'un téléphone, d'une carte,
        d'un écran, d'une pastille, à extruder (THREE.ExtrudeGeometry) ou à poser à plat (ShapeGeometry) */
    arrondi,
    /** un sol qui ne garde que l'ombre (neutre), à la hauteur y */
    sol: (y = -1, opacite = 0.22) => {
      const s = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.ShadowMaterial({ opacity: opacite }));
      s.rotation.x = -Math.PI / 2; s.position.y = y; s.receiveShadow = true; scene.add(s);
      return s;
    },
    /** ramène les coordonnées de texture d'une ShapeGeometry de l × h à 0..1 (une capture qui remplit la forme) */
    plaquer: (geometrie, l, h) => {
      const uv = geometrie.attributes.uv;
      for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / l + 0.5, uv.getY(i) / h + 0.5);
      return geometrie;
    },
  };

  const pixel = new Uint8Array(4);
  const attendreGpu = () => {           // un pixel relu : l'image est vraiment finie (même sans carte graphique)
    const gl = renderer.getContext();
    gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixel);
  };
  let poser = null, montre = null;
  const pret = (async () => {
    poser = await auHasardFixe(1, () => construire(outils));
    if (typeof poser !== "function") throw new Error("plan3d : construire doit rendre poser(t)");
    poser(0);
    await renderer.compileAsync(scene, camera);
    renderer.render(scene, camera);
    attendreGpu();
  })();
  window.__hf = window.__hf || {};
  window.__hf.buildReady = window.__hf.buildReady || {};
  window.__hf.buildReady["plan3d-" + (canvas.id || ++plans)] = pret;

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
    const t = Math.max(0, ev.detail.time - debut);
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

// Le hasard de la construction (les identifiants de three.js, un placement « au hasard ») est fixé :
// chaque rendu, chaque relecture, donne les mêmes images.
async function auHasardFixe(graine, construire) {
  const natif = Math.random;
  let etat = graine >>> 0;
  Math.random = () => {
    etat = (etat + 0x6d2b79f5) >>> 0;
    let t = etat;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  try {
    return await construire();
  } finally {
    Math.random = natif;
  }
}
