/* La 3D du kit : un plan en vraie 3D (three.js), quand il sert (scenes.md, « La 3D, quand elle
   sert » ; le mode d'emploi : kit.md, « La 3D »). Ce module fait la plomberie ; la scène ne décrit
   que ses objets et leur pose :

     import { plan3d } from "./kit/plan3d.js";
     plan3d(document.getElementById("s5-vue"), async ({ THREE, scene, camera, briques, matiere, net, … }) => {
       … crée les objets (briques.ordinateur({ ecran: "assets/images/page.png" }), …) …
       return (t) => { … pose les objets et la caméra d'après t seul (secondes depuis le début du plan) … };
     }, { focale: 50, lumiere: "fenetre", ouverture: 2.8, contact: true, finition: true });

   - Le plan dure ce que dure l'hôte de sa sous-composition (data-start, data-duration).
   - Chaque image se dessine d'après son instant seul (`hf-seek` de HyperFrames, comme son exemple
     path-traced-3d) : jamais d'horloge, de minuterie, de requestAnimationFrame ni de Math.random
     (le hasard voulu : `hasard()`, toujours le même), sinon l'aperçu et le rendu diffèrent. Les
     textures dessinées (matieres3d.js) et le bruit de l'ombre de contact sortent d'une graine fixe.
   - Deux niveaux (scenes.md) : des objets détaillés sur le fond du kit (fond transparent, lumière de
     studio, couleurs de la marque en aplat), ou un plateau photographique (une table, un mur, une
     lumière de fenêtre, l'objectif et sa profondeur de champ, la finition film), qui a son propre
     fond opaque et se marque `data-plateau` sur son hôte dans index.html.
   - Les couleurs : une couleur à garder exacte (la marque, la capture du client sur un écran, un
     objet connu) se pose en aplat (`aplat`) : ni la lumière, ni le rendu photographique ne la
     changent. Les matières éclairées gardent les couleurs de la vraie vie.
   - L'unité : 10 cm (un ordinateur portable fait 3 unités de large). La focale et la profondeur de
     champ en dépendent.
   - Le kit (kit.js) est chargé avant : `K.cadre`, `K.jeton`, `K.rng`, `K.ic` servent ici.
   three.js : licence MIT, copié de node_modules par `npm run sync` dans assets/vendor/ (ses modules
   d'exemples dans assets/vendor/three-addons/, que l'import map d'index.html appelle `three/addons/`). */
import * as THREE from "../assets/vendor/three.module.min.js";

const K = window.K;
const UNITE_MM = 100;                 // 1 unité de la scène = 10 cm

// Les modules d'exemples de three.js (l'import map d'index.html), chargés à la demande : un projet
// créé avant elle garde ses plans simples, et le message dit quoi faire s'il en veut davantage.
const ADDONS = {
  piece: "three/addons/environments/RoomEnvironment.js",
  composeur: "three/addons/postprocessing/EffectComposer.js",
  rendu: "three/addons/postprocessing/RenderPass.js",
  sortie: "three/addons/postprocessing/OutputPass.js",
  shader: "three/addons/postprocessing/ShaderPass.js",
  bokeh: "three/addons/postprocessing/BokehPass.js",
  gtao: "three/addons/postprocessing/GTAOPass.js",
  simplex: "three/addons/math/SimplexNoise.js",
};
const MANQUE = "plan3d : les modules de three.js ne se chargent pas. Il manque l'import map dans index.html "
  + "(recopie la ligne <script type=\"importmap\"> de templates/projet/index.html.tpl, avant les autres scripts), "
  + "ou assets/vendor/three-addons/ (recopie assets/vendor/ depuis la racine du dossier, après `npm run sync`)";

async function charger(noms) {
  const sortie = {};
  await Promise.all(noms.map(async (n) => { sortie[n] = await import(ADDONS[n]); }));
  return sortie;
}

export function plan3d(canvas, construire, options = {}) {
  if (!canvas) throw new Error("plan3d : le canvas manque (un id faux ?)");
  if (!K) throw new Error("plan3d : le kit (kit/kit.js) n'est pas chargé dans index.html");
  const hote = canvas.closest("[data-start]");
  const debut = Number(hote?.dataset.start || 0), fin = Number(hote?.dataset.duration) || Infinity;
  const { largeur: L, hauteur: H } = K.cadre(canvas);
  canvas.width = L; canvas.height = H;

  const lum = typeof options.lumiere === "string" ? { type: options.lumiere } : { type: "studio", ...(options.lumiere || {}) };
  const finition = options.finition === true ? {} : options.finition || null;
  // La chaîne d'effets (objectif, ombre de contact, finition) : l'image a alors son propre fond, opaque.
  const effets = Boolean(options.ouverture || options.contact || finition);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: !effets, alpha: !effets, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(L, H, false);
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  // Le rendu des matières éclairées : neutre en studio (des blancs et des gris qui restent neutres),
  // photographique à la fenêtre. Les aplats n'y passent jamais.
  renderer.toneMapping = lum.type === "fenetre" ? THREE.AgXToneMapping : THREE.NeutralToneMapping;
  renderer.toneMappingExposure = options.exposition ?? (lum.type === "fenetre" ? 1.15 : 1);
  renderer.shadowMap.enabled = options.ombre !== false || lum.type === "fenetre";
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  // `focale` : en millimètres, comme un objectif (35 large, 50 naturel, 85 serré) ; sinon `angle`,
  // l'angle de vue vertical en degrés (26 par défaut).
  const camera = new THREE.PerspectiveCamera(options.angle ?? 26, L / H, 0.1, 300);
  if (options.focale) camera.setFocalLength(options.focale);
  camera.position.set(0, 0.3, 7);

  let mise = null;                                    // ce que `net` a demandé pendant poser(t)
  const outils = {
    THREE, scene, camera, renderer, largeur: L, hauteur: H,
    /** un hasard toujours le même (graine fixe) : placer des objets « au hasard » sans que deux rendus diffèrent */
    hasard: K.rng(1),
    /** une courbe de GSAP, à appliquer à une progression de 0 à 1 : courbe("expo.out")(p) */
    courbe: (nom) => window.gsap.parseEase(nom),
    /** une couleur de sa marque (THREE.Color) : jeton("--brand-accent") */
    jeton: (nom) => new THREE.Color(K.jeton(nom) || "#808080"),
    /** une matière en aplat, sans lumière : la couleur reste exactement elle (la marque, un objet connu, une capture) */
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
    /** la caméra autour d'un point (THREE.Vector3 ou [x, y, z]) : à `d` unités, `hauteur` degrés au-dessus
        de l'horizon (0 : à hauteur du point, 90 : à la verticale), `cote` degrés vers la droite (0 : de face,
        depuis +z) ; elle le regarde */
    orbite: (cible, d, hauteur = 20, cote = 0) => {
      const p = Array.isArray(cible) ? new THREE.Vector3(...cible) : cible;
      const h = THREE.MathUtils.degToRad(hauteur), c = THREE.MathUtils.degToRad(cote);
      camera.position.set(p.x + d * Math.cos(h) * Math.sin(c), p.y + d * Math.sin(h), p.z + d * Math.cos(h) * Math.cos(c));
      camera.lookAt(p);
    },
    /** la mise au point de l'objectif (avec `ouverture`), à appeler dans poser(t) : sur un objet
        (son centre), un point (THREE.Vector3) ou une distance ; sans elle, sur l'origine */
    net: (cible) => { mise = cible; },
  };

  const pixel = new Uint8Array(4);
  const attendreGpu = () => {           // un pixel relu : l'image est vraiment finie (même sans carte graphique)
    const gl = renderer.getContext();
    gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixel);
  };
  let poser = null, montre = null, dessiner = null;
  const pret = (async () => {
    // 1. Les modules : la pièce (des reflets de vraie pièce), les matières, les briques, les effets.
    const voulus = ["piece", ...(effets ? ["composeur", "rendu", "sortie", "shader"] : []),
      ...(options.ouverture ? ["bokeh"] : []), ...(options.contact ? ["gtao", "simplex"] : [])];
    let mod = null, kit = null, raison = null;
    try {
      mod = await charger(voulus);
      const [matiere, briques] = await Promise.all([import("./matieres3d.js"), import("./briques3d.js")]);
      kit = { matiere, briques };
    } catch (e) {
      raison = `${MANQUE} (${e.message})`;
      if (effets) throw new Error(raison);
    }
    const absent = () => { throw new Error(raison); };
    Object.defineProperty(outils, "matiere", { get: () => kit ? kit.matiere : absent(), enumerable: true });
    let briques = null;
    Object.defineProperty(outils, "briques", {
      get: () => (kit ? (briques ||= kit.briques.fabriquerBriques(outils)) : absent()), enumerable: true,
    });

    // 2. La lumière : le studio (produit) ou la fenêtre (un soleil chaud, l'ombre d'un store).
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = mod ? pmrem.fromScene(new mod.piece.RoomEnvironment(), 0.04).texture : studio(pmrem);
    outils.lumieres = lum.type === "fenetre" ? fenetre(scene, lum, kit) : plateauStudio(scene, lum, options.ombre !== false);
    outils.lumiere = outils.lumieres.principale;
    scene.environmentIntensity = lum.reflets ?? (lum.type === "fenetre" ? 0.55 : 0.9);

    // 3. La scène du plan.
    poser = await construire(outils);
    if (typeof poser !== "function") throw new Error("plan3d : construire doit rendre poser(t)");
    poser(0);
    if (lum.type !== "fenetre" && options.ajusterOmbre !== false) ajusterOmbre(scene, outils.lumiere);
    // Les métaux ne montrent que ce qu'ils reflètent : ils voient la pièce en entier, même quand sa
    // lumière d'ambiance est baissée pour laisser le soleil dessiner les ombres.
    // Une vitre d'écran (matiere.reflet) n'en garde qu'un peu : sa capture reste lisible.
    scene.traverse((o) => {
      for (const m of [].concat(o.material || [])) {
        if (!scene.environment || m.envMap) continue;
        if (m.userData?.reflet !== undefined) { m.envMap = scene.environment; m.envMapIntensity = m.userData.reflet; }
        else if (m.metalness >= 0.5) { m.envMap = scene.environment; m.envMapIntensity = lum.metaux ?? 1; }
      }
    });

    // 4. Les effets : ils dessinent dans un tampon où chaque matière garde son propre rendu (un aplat
    //    reste exact), puis l'objectif, l'ombre de contact et la finition, enfin l'écran.
    let composeur = null, objectif = null, grain = null;
    if (effets) {
      const fond = options.fond ?? "--brand-sombre";
      scene.background = typeof fond === "string" && fond.startsWith("--") ? outils.jeton(fond) : new THREE.Color(fond);
      ({ composeur, objectif, grain } = chaine(renderer, scene, camera, L, H, mod, options, finition));
    }
    const focus = new THREE.Vector3(), devant = new THREE.Vector3();
    dessiner = (t) => {
      mise = null;
      poser(t);
      if (objectif) {
        camera.updateMatrixWorld();
        camera.getWorldDirection(devant);
        let S;
        if (typeof mise === "number") S = mise;
        else {
          if (mise?.isObject3D) new THREE.Box3().setFromObject(mise).getCenter(focus);
          else if (mise?.isVector3) focus.copy(mise);
          else if (Array.isArray(mise)) focus.set(...mise);
          else focus.set(0, 0, 0);
          S = focus.sub(camera.position).dot(devant);
        }
        S = Math.max(S, camera.near * 4);
        const f = camera.getFocalLength(), N = options.ouverture;
        const coc = (f * f) / (N * Math.max(S * UNITE_MM - f, 1));          // en mm, pour |D − S| / D = 1
        objectif.uniforms.focus.value = S;
        objectif.uniforms.aperture.value = coc / camera.getFilmHeight() * 0.5 * H;   // le rayon en pixels
      }
      if (grain) grain.uniforms.graine.value = Math.round(t * 30) % 997;   // le grain change à chaque image, toujours le même
      if (composeur) composeur.render(0);
      else renderer.render(scene, camera);
    };
    await renderer.compileAsync(scene, camera);
    dessiner(0);
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
      dessiner(t);
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

// ---------------------------------------------------------------------------
// Les deux lumières prêtes
// ---------------------------------------------------------------------------
/** Le studio produit : une lumière principale douce qui porte l'ombre, un remplissage neutre. */
function plateauStudio(scene, lum, ombre) {
  const cle = new THREE.DirectionalLight(0xffffff, lum.force ?? 2.2);
  cle.position.set(...(lum.position ?? [-3, 6, 4]));
  cle.castShadow = ombre;
  cle.shadow.mapSize.set(2048, 2048); cle.shadow.radius = 8; cle.shadow.bias = -0.0004; cle.shadow.normalBias = 0.01;
  Object.assign(cle.shadow.camera, { left: -5, right: 5, top: 5, bottom: -5 });
  const ciel = new THREE.HemisphereLight(0xffffff, 0x444444, 0.6);
  scene.add(cle, cle.target, ciel);
  return { principale: cle, ciel };
}

/** La fenêtre : un soleil chaud qui entre de côté par une fenêtre, le motif de son store (ou de ses
    carreaux) sur la table et le mur, le bleu doux du ciel dans les ombres. */
function fenetre(scene, lum, kit) {
  const cote = lum.cote === "droite" ? 1 : -1;
  const soleil = new THREE.SpotLight(new THREE.Color(lum.couleur ?? "#ffdfb8"), lum.force ?? 9, 0, lum.angle ?? 0.5, lum.penombre ?? 0.35, 0);
  soleil.position.set(...(lum.position ?? [cote * 13, 12, 6]));
  soleil.target.position.set(...(lum.cible ?? [0, 0, -1.5]));
  soleil.castShadow = true;
  soleil.shadow.mapSize.set(2048, 2048); soleil.shadow.bias = -0.00012; soleil.shadow.normalBias = 0.015;
  soleil.shadow.camera.near = 4; soleil.shadow.camera.far = 80;
  if (kit && (lum.motif ?? "store") !== "aucun") {
    soleil.map = kit.matiere.motifLumiere(lum.motif ?? "store", { lames: lum.lames ?? 26, ouverture: lum.ouverture ?? 0.55 });
    soleil.map.center.set(0.5, 0.5);
    soleil.map.rotation = lum.inclinaison ?? 0.12;
  }
  const ciel = new THREE.HemisphereLight(new THREE.Color(lum.ciel ?? "#cfdcf5"), new THREE.Color(lum.sol ?? "#6d5a48"), lum.ambiance ?? 0.3);
  const rebond = new THREE.DirectionalLight(new THREE.Color("#e6ecf8"), lum.rebond ?? 0.25);
  rebond.position.set(-cote * 8, 6, 9);
  scene.add(soleil, soleil.target, ciel, rebond);
  return { principale: soleil, soleil, ciel, rebond };
}

/** Le cadre de l'ombre de la lumière principale du studio, ajusté aux objets qui la portent : une
    ombre nette sur les petits objets, entière sur les grands. Garde la direction de la lumière. */
function ajusterOmbre(scene, cle) {
  const boite = new THREE.Box3();
  scene.updateMatrixWorld(true);
  scene.traverse((o) => { if (o.isMesh && o.castShadow) boite.expandByObject(o, true); });
  if (boite.isEmpty()) return;
  const s = boite.getBoundingSphere(new THREE.Sphere()), R = Math.max(0.5, s.radius * 1.6);
  const dir = cle.position.clone().sub(cle.target.position).normalize();
  cle.target.position.copy(s.center);
  cle.position.copy(s.center).addScaledVector(dir, R * 3);
  Object.assign(cle.shadow.camera, { left: -R, right: R, top: R, bottom: -R, near: 0.05, far: R * 6 });
  cle.shadow.camera.updateProjectionMatrix();
}

// Un studio pour les reflets, si les modules de three manquent : une boîte sombre et trois panneaux lumineux.
function studio(pmrem) {
  const s = new THREE.Scene();
  s.add(new THREE.Mesh(new THREE.BoxGeometry(20, 20, 20), new THREE.MeshBasicMaterial({ color: 0x202020, side: THREE.BackSide })));
  const panneau = (x, y, z, l, h, i) => {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(l, h), new THREE.MeshBasicMaterial({ color: new THREE.Color(i, i, i) }));
    m.position.set(x, y, z); m.lookAt(0, 0, 0); s.add(m);
  };
  panneau(-6, 4, 5, 6, 3, 3); panneau(7, 2, 3, 3, 8, 2); panneau(0, 8, -4, 10, 2, 1.5);
  return pmrem.fromScene(s, 0.04).texture;
}

// ---------------------------------------------------------------------------
// La chaîne d'effets : l'objectif (profondeur de champ), l'ombre de contact, la finition film
// ---------------------------------------------------------------------------
const SOMMET = `varying vec2 vUv;
void main() { vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;

// Un vrai flou d'objectif : chaque point devient un disque dont la taille suit son écart au plan net,
// comme sur un capteur (rayon ∝ |D − S| / D). Un objet net ne bave pas sur le fond flou ; un fond
// flou ne passe pas devant un objet net. 72 échantillons en spirale, tournée par pixel (fixe).
const FLOU = `#include <common>
#include <packing>
varying vec2 vUv;
uniform sampler2D tColor;
uniform sampler2D tDepth;
uniform float focus;
uniform float aperture;
uniform float maxblur;
uniform float nearClip;
uniform float farClip;
uniform vec2 resolution;
float distanceVue(vec2 p) {
  return -perspectiveDepthToViewZ(unpackRGBAToDepth(texture2D(tDepth, p)), nearClip, farClip);
}
float rayon(float z) { return min(aperture * abs(z - focus) / max(z, 1e-3), maxblur); }
float hachage(vec2 p) { return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
const int N = 72;
void main() {
  vec4 base = texture2D(tColor, vUv);
  float z0 = distanceVue(vUv);
  float r0 = rayon(z0);
  if (r0 < 0.6) { gl_FragColor = vec4(base.rgb, 1.0); return; }
  vec3 somme = base.rgb;
  float total = 1.0;
  float tour = hachage(floor(gl_FragCoord.xy)) * 6.2831853;
  vec2 px = 1.0 / resolution;
  for (int i = 1; i < N; i++) {
    float fi = float(i);
    float r = sqrt(fi / float(N)) * r0;
    float a = fi * 2.39996323 + tour;
    vec2 p = vUv + vec2(cos(a), sin(a)) * r * px;
    float z = distanceVue(p);
    float ri = rayon(z);
    if (z > z0) ri = min(ri, r0 * 2.0);
    float m = smoothstep(r - 1.0, r + 1.0, ri);
    somme += mix(somme / total, texture2D(tColor, p).rgb, m);
    total += 1.0;
  }
  gl_FragColor = vec4(somme / total, 1.0);
}`;

// La finition film : un grain fin, sans couleur, qui change à chaque image (d'après son numéro), et
// un léger vignettage. Appliqué après la sortie, sur l'image finale.
const FILM = `varying vec2 vUv;
uniform sampler2D tDiffuse;
uniform float graine;
uniform float grain;
uniform float vignette;
uniform vec2 resolution;
float hachage(vec2 p) { vec3 q = fract(vec3(p.xyx) * 0.1031); q += dot(q, q.yzx + 33.33); return fract((q.x + q.y) * q.z); }
void main() {
  vec4 c = texture2D(tDiffuse, vUv);
  vec2 q = floor(vUv * resolution) + graine * vec2(37.0, 17.0);
  float n = hachage(q) + hachage(q + vec2(113.0, 71.0)) - 1.0;
  float l = dot(c.rgb, vec3(0.2126, 0.7152, 0.0722));
  c.rgb += n * grain * (1.0 - 0.6 * abs(2.0 * l - 1.0));
  vec2 d = (vUv - 0.5) * vec2(resolution.x / max(resolution.x, resolution.y), resolution.y / max(resolution.x, resolution.y));
  c.rgb *= 1.0 - vignette * smoothstep(0.3, 0.8, length(d) * 1.25);
  gl_FragColor = vec4(c.rgb, 1.0);
}`;

function chaine(renderer, scene, camera, L, H, mod, options, finition) {
  const { EffectComposer } = mod.composeur, { RenderPass } = mod.rendu, { OutputPass } = mod.sortie, { ShaderPass } = mod.shader;
  // Le tampon : en demi-flottants, lissé (4 échantillons), et marqué comme une sortie : chaque matière
  // y applique son propre rendu (les aplats aucun), au lieu d'un rendu photographique posé sur tout.
  const tampon = new THREE.WebGLRenderTarget(L, H, { type: THREE.HalfFloatType, samples: 4 });
  const composeur = new EffectComposer(renderer, tampon);
  for (const rt of [composeur.renderTarget1, composeur.renderTarget2]) {
    rt.isXRRenderTarget = true;
    rt.texture.colorSpace = THREE.LinearSRGBColorSpace;      // des valeurs linéaires : la sortie convertit
  }
  composeur.setPixelRatio(1);
  composeur.setSize(L, H);
  composeur.addPass(new RenderPass(scene, camera));
  // Les passes qui relisent la scène (profondeur, normales) la dessinent sans son fond : un fond de
  // couleur effacerait leur tampon avec lui (une profondeur fausse partout où rien n'est posé).
  const sansFond = (f) => { const fond = scene.background; scene.background = null; try { f(); } finally { scene.background = fond; } };

  if (options.contact) {
    const { GTAOPass } = mod.gtao, { SimplexNoise } = mod.simplex;
    // L'ombre de contact (là où deux objets se touchent). Son bruit de lissage vient d'une graine fixe :
    // celui de three.js est tiré au hasard à chaque chargement (des images qui scintilleraient).
    class OmbreContact extends GTAOPass {
      generateNoise(taille = 64) {
        const simplex = new SimplexNoise({ random: K.rng(97) }), d = new Uint8Array(taille * taille * 4);
        for (let i = 0; i < taille; i++) {
          for (let j = 0; j < taille; j++) {
            const k = (i * taille + j) * 4;
            d[k] = (simplex.noise(i, j) * 0.5 + 0.5) * 255;
            d[k + 1] = (simplex.noise(i + taille, j) * 0.5 + 0.5) * 255;
            d[k + 2] = (simplex.noise(i, j + taille) * 0.5 + 0.5) * 255;
            d[k + 3] = (simplex.noise(i + taille, j + taille) * 0.5 + 0.5) * 255;
          }
        }
        const t = new THREE.DataTexture(d, taille, taille, THREE.RGBAFormat, THREE.UnsignedByteType);
        t.wrapS = t.wrapT = THREE.RepeatWrapping;
        t.needsUpdate = true;
        return t;
      }
      render(...a) { sansFond(() => super.render(...a)); }
    }
    const c = typeof options.contact === "object" ? options.contact : {};
    const ao = new OmbreContact(scene, camera, L, H);
    ao.updateGtaoMaterial({ radius: c.rayon ?? 0.3, distanceExponent: 1, thickness: 1, scale: 1, samples: 16, distanceFallOff: 1 });
    ao.updatePdMaterial({ lumaPhi: 10, depthPhi: 2, normalPhi: 3, radius: 6, rings: 2, samples: 16 });
    ao.blendIntensity = c.force ?? 0.9;
    composeur.addPass(ao);
  }

  let objectif = null;
  if (options.ouverture) {
    const { BokehPass } = mod.bokeh;
    class Objectif extends BokehPass {
      constructor() {
        super(scene, camera, { focus: 6, aperture: 0, maxblur: 1 });
        this.uniforms.resolution = { value: new THREE.Vector2(L, H) };
        this.uniforms.maxblur.value = options.flouMax ?? 0.035 * Math.min(L, H);
        this.materialBokeh = new THREE.ShaderMaterial({ uniforms: this.uniforms, vertexShader: SOMMET, fragmentShader: FLOU });
        this.fsQuad.material = this.materialBokeh;
      }
      setSize(w, h) { super.setSize(w, h); this.uniforms.resolution?.value.set(w, h); }
      render(...a) { sansFond(() => super.render(...a)); }   // la profondeur, sans le fond de la scène
    }
    objectif = new Objectif();
    composeur.addPass(objectif);
  }

  // La sortie : la conversion vers l'écran seulement, sans second rendu photographique (déjà fait par matière).
  class Sortie extends OutputPass {
    render(r, ...reste) {
      const avant = r.toneMapping;
      r.toneMapping = THREE.NoToneMapping;
      super.render(r, ...reste);
      r.toneMapping = avant;
    }
  }
  composeur.addPass(new Sortie());

  let grain = null;
  if (finition) {
    grain = new ShaderPass({
      uniforms: { tDiffuse: { value: null }, graine: { value: 0 }, grain: { value: finition.grain ?? 0.02 },
        vignette: { value: finition.vignette ?? 0.22 }, resolution: { value: new THREE.Vector2(L, H) } },
      vertexShader: SOMMET, fragmentShader: FILM,
    });
    composeur.addPass(grain);
  }
  composeur.setSize(L, H);
  return { composeur, objectif, grain };
}
