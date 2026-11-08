/* Les matières de la 3D poussée (kit.md, « La 3D » ; scenes.md, « La 3D, quand elle sert ») : du
   bois veiné, du papier ligné, de l'alu brossé, du plastique, de la céramique, du verre, un mur peint,
   du carton, dessinés par le code. Chaque texture sort d'un hasard à graine (K.rng) : la même à chaque
   rendu, dans chaque fenêtre de rendu, sans fichier à fournir.

   On ne l'importe pas soi-même : plan3d la charge et la donne à `construire` (`matiere.bois()`…).
   Les matières éclairées gardent les couleurs de la vraie vie (le bois est brun, le papier crème) :
   elles servent les plans de plateau (data-plateau, scenes.md), jamais les couleurs de la marque, qui
   se posent en aplat. Les métaux, le verre et les plastiques restent neutres par défaut. */
import * as THREE from "three";

const K = window.K;
const cache = new Map();

/** Une matière construite une fois par réglage : vingt touches partagent la même. */
function memo(cle, fabriquer) {
  if (!cache.has(cle)) cache.set(cle, fabriquer());
  return cache.get(cle);
}

/** Un bruit doux, périodique (px × py cellules : la texture se répète sans couture), à graine. */
export function bruit(graine, px = 8, py = 8) {
  const r = K.rng(graine), v = new Float32Array(px * py);
  for (let i = 0; i < v.length; i++) v[i] = r();
  const lisse = (t) => t * t * (3 - 2 * t);
  return (x, y) => {
    const xi = Math.floor(x), yi = Math.floor(y), u = lisse(x - xi), w = lisse(y - yi);
    const x0 = ((xi % px) + px) % px, y0 = ((yi % py) + py) % py, x1 = (x0 + 1) % px, y1 = (y0 + 1) % py;
    const a = v[y0 * px + x0], b = v[y0 * px + x1], c = v[y1 * px + x0], d = v[y1 * px + x1];
    return a + (b - a) * u + (c - a) * w + (a - b - c + d) * u * w;
  };
}

/** Plusieurs octaves d'un bruit périodique, de 0 à 1 environ. */
function fbm(graine, px, py, octaves = 4) {
  const couches = Array.from({ length: octaves }, (_, i) => bruit(graine + i * 101, px << i, py << i));
  return (x, y) => {
    let s = 0, a = 0.5, n = 0;
    for (let i = 0; i < octaves; i++) { s += a * couches[i](x * (1 << i), y * (1 << i)); n += a; a *= 0.5; }
    return s / n;
  };
}

function toile(l, h) {
  const c = document.createElement("canvas");
  c.width = l; c.height = h;
  return c;
}

/** Une texture three.js depuis un canvas : `couleur` (sRGB) pour une image, sinon une carte de
    données (rugosité, relief), qui se répète. */
function versTexture(c, { couleur = true, repetition = [1, 1] } = {}) {
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.repeat.set(...repetition);
  t.anisotropy = 8;
  if (couleur) t.colorSpace = THREE.SRGBColorSpace;
  return t;
}

/** Remplit un canvas pixel par pixel : f(x, y) rend [r, g, b] (0-255). */
function peindre(l, h, f) {
  const c = toile(l, h), ctx = c.getContext("2d"), img = ctx.createImageData(l, h), d = img.data;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < l; x++) {
      const [r, g, b] = f(x, y), i = (y * l + x) * 4;
      d[i] = r; d[i + 1] = g; d[i + 2] = b; d[i + 3] = 255;
    }
  }
  ctx.putImageData(img, 0, 0);
  return c;
}

const hexa = (h) => { const c = new THREE.Color(h); return [c.r * 255, c.g * 255, c.b * 255]; };
const mel = (a, b, p) => [a[0] + (b[0] - a[0]) * p, a[1] + (b[1] - a[1]) * p, a[2] + (b[2] - a[2]) * p];

// ---------------------------------------------------------------------------
// Le bois : des veines qui suivent la longueur (axe des u), des pores fins, des planches.
// ---------------------------------------------------------------------------
const BOIS = {
  chene: ["#c8a276", "#86603b"], noyer: ["#7a5034", "#3f2616"], clair: ["#e6cfa6", "#bf9a68"],
  fonce: ["#5a3d2b", "#2c1d14"], cedre: ["#e8bf8f", "#c48d5c"],
};

/** Du bois (une table, un bureau, une étagère). `essence` : chene, noyer, clair, fonce, cedre ;
    `planches` : le nombre de lames sur la hauteur de la texture ; `repetition` : combien de fois la
    texture se répète sur la surface (une texture couvre 8 unités, 80 cm, de bois). Le fil est fin et
    serré, comme une vraie lame de chêne : des cernes sombres et minces, des pores étirés. */
export function bois({ essence = "chene", planches = 5, repetition = [1, 1], vernis = 0.25, graine = 7 } = {}) {
  return memo(`bois:${essence}:${planches}:${repetition}:${vernis}:${graine}`, () => {
    const [clair, fonce] = (BOIS[essence] || BOIS.chene).map(hexa);
    const T = 1024, cernes = 9;                                   // cernes par lame
    const ondule = fbm(graine, 2, 4 * planches, 3), lent = fbm(graine + 1, 3, 3, 3);
    const pore = bruit(graine + 3, 512, 128), teinte = bruit(graine + 9, 1, planches * 2);
    const relief = new Float32Array(T * T);
    const image = peindre(T, T, (x, y) => {
      const u = x / T, v = y / T, lame = Math.floor(v * planches), dans = v * planches - lame;
      const phase = dans * cernes + (ondule(u * 2, v * 4 * planches) - 0.5) * 7 + lame * 3.7;
      const f = phase - Math.floor(phase);
      const cerne = Math.max(0, 1 - Math.abs(f - 0.86) / 0.07);   // le bois d'été : un trait mince et sombre
      const doux = 0.5 + 0.5 * Math.sin(phase * Math.PI * 2);      // le bois de printemps, plus clair
      const p = pore(u * 512, v * 128), point = p > 0.78 ? (p - 0.78) * 2.5 : 0;
      const joint = Math.min(1, Math.min(dans, 1 - dans) * T / planches / 1.2);   // la rainure entre deux lames
      const k = 0.3 + (lent(u * 3, v * 3) - 0.5) * 0.35 + cerne * 0.42 + doux * 0.08 + point * 0.25
        + (teinte(0.5, lame * 2 + 0.5) - 0.5) * 0.3;
      relief[y * T + x] = (1 - cerne * 0.6 - point * 0.6) * joint;
      return mel(clair, fonce, Math.min(1, Math.max(0, k))).map((c) => c * (0.6 + 0.4 * joint));
    });
    const bosses = peindre(T, T, (x, y) => { const k = relief[y * T + x] * 255; return [k, k, k]; });
    return new THREE.MeshPhysicalMaterial({
      map: versTexture(image, { repetition }), bumpMap: versTexture(bosses, { couleur: false, repetition }),
      bumpScale: 0.8, roughness: 0.5, clearcoat: vernis, clearcoatRoughness: 0.3,
    });
  });
}

// ---------------------------------------------------------------------------
// Le papier : une page (crème, ses fibres), lignée, à petits carreaux, ou Seyès (le cahier d'écolier).
// ---------------------------------------------------------------------------
/** Une page de l × h unités (1 unité = 10 cm). `lignes` : "lignes" (lignes bleues et marge rouge),
    "carreaux" (5 mm), "seyes" (le cahier français), "blanc". Rend une matière dont la texture couvre
    exactement la page (une ShapeGeometry plaquée, ou le dessus d'une boîte). */
export function papier({ l = 1.48, h = 2.1, lignes = "lignes", teinte = "#f6f3ea", marge = true, graine = 21 } = {}) {
  return memo(`papier:${l}:${h}:${lignes}:${teinte}:${marge}:${graine}`, () => {
    const mm = 4, L = Math.min(2048, Math.round(l * 100 * mm)), H = Math.min(2048, Math.round(h * 100 * mm));
    const k = L / (l * 100);                                    // pixels par millimètre (réel)
    const fibre = bruit(graine, 64, 64), fond = hexa(teinte);
    const c = peindre(L, H, (x, y) => {
      const f = (fibre(x / L * 64, y / H * 64 * (H / L)) - 0.5) * 7;
      return fond.map((v) => v + f);
    });
    const ctx = c.getContext("2d");
    const trait = (couleur, largeur, x1, y1, x2, y2) => {
      ctx.strokeStyle = couleur; ctx.lineWidth = largeur;
      ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    };
    const haut = 22 * k;                                         // l'en-tête d'une page, sans ligne
    if (lignes === "lignes") {
      for (let y = haut; y < H - 6 * k; y += 8 * k) trait("rgba(92,140,204,0.55)", Math.max(1, 0.25 * k), 0, y, L, y);
    } else if (lignes === "carreaux") {
      for (let y = 0; y < H; y += 5 * k) trait("rgba(110,150,200,0.38)", Math.max(1, 0.2 * k), 0, y, L, y);
      for (let x = 0; x < L; x += 5 * k) trait("rgba(110,150,200,0.38)", Math.max(1, 0.2 * k), x, 0, x, H);
    } else if (lignes === "seyes") {
      for (let y = haut, i = 0; y < H - 4 * k; y += 2 * k, i++) {
        trait(i % 4 === 0 ? "rgba(120,96,170,0.62)" : "rgba(150,135,200,0.32)", Math.max(1, (i % 4 === 0 ? 0.28 : 0.18) * k), 0, y, L, y);
      }
      for (let x = 30 * k; x < L; x += 8 * k) trait("rgba(150,135,200,0.32)", Math.max(1, 0.18 * k), x, haut, x, H);
    }
    if (marge && lignes !== "blanc") trait("rgba(214,76,82,0.7)", Math.max(1, 0.3 * k), 25 * k, 0, 25 * k, H);
    const t = versTexture(c);
    t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
    return new THREE.MeshStandardMaterial({ map: t, roughness: 0.92 });
  });
}

/** La tranche d'un bloc de pages : de fines lignes serrées (à poser sur les côtés d'une boîte). */
export function tranche({ teinte = "#efebe0", graine = 5 } = {}) {
  return memo(`tranche:${teinte}:${graine}`, () => {
    const b = bruit(graine, 1, 128), fond = hexa(teinte);
    const c = peindre(64, 512, (_x, y) => { const f = (b(0.5, y / 4) - 0.5) * 40; return fond.map((v) => v + f); });
    return new THREE.MeshStandardMaterial({ map: versTexture(c), roughness: 0.95 });
  });
}

// ---------------------------------------------------------------------------
// Les métaux, les plastiques, le verre, la céramique
// ---------------------------------------------------------------------------
const ALU = { argent: "#d3d5d9", gris: "#7c7e83", noir: "#3a3b3e", clair: "#e6e7e9" };

/** De l'aluminium (un ordinateur, une tablette, une virole de crayon). `brosse` : des stries fines
    dans le sens de la longueur ; `teinte` : argent, gris, noir, clair (des neutres). */
export function alu({ teinte = "argent", brosse = true, rugosite = 0.34, graine = 31 } = {}) {
  return memo(`alu:${teinte}:${brosse}:${rugosite}:${graine}`, () => {
    const options = { color: ALU[teinte] || teinte, metalness: 1, roughness: rugosite };
    if (brosse) {
      const strie = bruit(graine, 4, 512), fine = bruit(graine + 1, 32, 512);
      const c = peindre(256, 1024, (x, y) => {
        const k = 150 + (strie(x / 64, y / 2) - 0.5) * 60 + (fine(x / 8, y / 2) - 0.5) * 40;
        return [k, k, k];
      });
      options.roughnessMap = versTexture(c, { couleur: false });   // des stries le long des u (la largeur)
      options.anisotropy = 0.5;
    }
    return new THREE.MeshPhysicalMaterial(options);
  });
}

/** Un métal poli (une spirale, un anneau) : du chrome neutre. */
export function chrome({ rugosite = 0.14 } = {}) {
  return memo(`chrome:${rugosite}`, () => new THREE.MeshStandardMaterial({ color: "#dcdde0", metalness: 1, roughness: rugosite }));
}

/** Du plastique : `mat` (une touche, une coque) ou brillant. La couleur est celle de l'objet réel. */
export function plastique({ couleur = "#1c1c1e", mat = true, graine = 41 } = {}) {
  return memo(`plastique:${couleur}:${mat}:${graine}`, () => {
    const b = bruit(graine, 128, 128);
    const c = peindre(256, 256, (x, y) => { const k = 128 + (b(x / 2, y / 2) - 0.5) * 90; return [k, k, k]; });
    return new THREE.MeshPhysicalMaterial({
      color: couleur, roughness: mat ? 0.62 : 0.28, clearcoat: mat ? 0 : 0.6, clearcoatRoughness: 0.2,
      bumpMap: versTexture(c, { couleur: false, repetition: [6, 6] }), bumpScale: 0.25,
    });
  });
}

/** Du verre poli, sombre (l'écran éteint, le dos d'un téléphone) ; `depoli` pour un dos mat. */
export function verre({ couleur = "#0c0c0e", depoli = false } = {}) {
  return memo(`verre:${couleur}:${depoli}`, () => new THREE.MeshPhysicalMaterial({
    color: couleur, roughness: depoli ? 0.38 : 0.05, metalness: 0, clearcoat: 1, clearcoatRoughness: depoli ? 0.3 : 0.03,
  }));
}

/** Un reflet de vitre à poser juste devant un écran allumé : il n'ajoute qu'un peu de lumière (l'image
    de l'écran reste exacte dessous). `force` reste faible : un reflet franc voile sa capture (essai du
    08/11/2026, l'écran ouvert à 110° renvoyait le plafond de la pièce). plan3d lui donne la pièce. */
export function reflet({ force = 0.12 } = {}) {
  return memo(`reflet:${force}`, () => new THREE.MeshStandardMaterial({
    color: "#000000", roughness: 0.12, metalness: 0, transparent: true, depthWrite: false,
    blending: THREE.AdditiveBlending, userData: { reflet: force },
  }));
}

/** De la céramique émaillée (une tasse) : blanche par défaut. */
export function ceramique({ couleur = "#f3f1ec" } = {}) {
  return memo(`ceramique:${couleur}`, () => new THREE.MeshPhysicalMaterial({
    color: couleur, roughness: 0.22, clearcoat: 1, clearcoatRoughness: 0.06,
  }));
}

/** Un vernis coloré (un crayon peint), en couleur réelle de l'objet. */
export function laque({ couleur = "#f2b31b" } = {}) {
  return memo(`laque:${couleur}`, () => new THREE.MeshPhysicalMaterial({ color: couleur, roughness: 0.3, clearcoat: 1, clearcoatRoughness: 0.1 }));
}

/** Une matière simple et mate (une gomme, du caoutchouc, du graphite, du café) : une couleur, une rugosité. */
export function mat({ couleur = "#151515", rugosite = 0.9, metal = 0 } = {}) {
  return memo(`mat:${couleur}:${rugosite}:${metal}`, () => new THREE.MeshStandardMaterial({ color: couleur, roughness: rugosite, metalness: metal }));
}

// ---------------------------------------------------------------------------
// Le plateau : un mur peint, du carton
// ---------------------------------------------------------------------------
/** Un mur peint (le fond d'un plateau) : une couleur réelle, presque unie, un léger grain de plâtre. */
export function mur({ couleur = "#e2ded7", repetition = [3, 2], graine = 51 } = {}) {
  return memo(`mur:${couleur}:${repetition}:${graine}`, () => {
    const lent = fbm(graine, 4, 4, 3), grain = bruit(graine + 7, 256, 256), fond = hexa(couleur);
    const c = peindre(512, 512, (x, y) => {
      const f = (lent(x / 128, y / 128) - 0.5) * 10 + (grain(x / 2, y / 2) - 0.5) * 6;
      return fond.map((v) => v + f);
    });
    return new THREE.MeshStandardMaterial({ map: versTexture(c, { repetition }), roughness: 0.96 });
  });
}

/** Du carton ou du kraft (la couverture d'un carnet, une boîte d'envoi). */
export function carton({ couleur = "#b48c5e", graine = 61 } = {}) {
  return memo(`carton:${couleur}:${graine}`, () => {
    const fibre = bruit(graine, 128, 32), tache = fbm(graine + 5, 4, 4, 3), fond = hexa(couleur);
    const c = peindre(512, 512, (x, y) => {
      const f = (fibre(x / 4, y / 16) - 0.5) * 22 + (tache(x / 128, y / 128) - 0.5) * 18;
      return fond.map((v) => v + f);
    });
    return new THREE.MeshStandardMaterial({ map: versTexture(c), roughness: 0.88 });
  });
}

/** Un texte imprimé (le nom de son offre sur la couverture de son carnet), dans la police de sa marque,
    en texture : `texte` vient d'OFFRE.json (jamais un faux nom). Les mots à lire restent en HTML. */
export async function impression(texte, { l = 1024, h = 512, police = "var(--brand-font-display)", graisse = 800,
  taille = 0.28, encre = "#111111", fond = null, alignement = "center" } = {}) {
  const famille = police.startsWith("var(") ? (K.jeton(police.slice(4, -1)) || "sans-serif") : police;
  const fonte = `${graisse} ${Math.round(h * taille)}px ${famille}`;
  try { await document.fonts.load(fonte, texte); } catch (_e) { /* la police de secours */ }
  const c = toile(l, h), ctx = c.getContext("2d");
  if (fond) { ctx.fillStyle = fond; ctx.fillRect(0, 0, l, h); }
  ctx.fillStyle = encre; ctx.font = fonte; ctx.textAlign = alignement; ctx.textBaseline = "middle";
  ctx.fillText(texte, alignement === "left" ? h * 0.15 : l / 2, h / 2, l * 0.9);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}

/** Le motif d'un store (des lames de lumière) ou d'une fenêtre à carreaux, pour la lumière « fenetre ». */
export function motifLumiere(motif = "store", { lames = 9, ouverture = 0.55 } = {}) {
  const c = toile(512, 512), ctx = c.getContext("2d");
  ctx.fillStyle = "#000"; ctx.fillRect(0, 0, 512, 512);
  ctx.fillStyle = "#fff"; ctx.filter = "blur(2px)";
  if (motif === "fenetre") {
    const m = 512 * 0.06;
    for (const [x, y] of [[0, 0], [1, 0], [0, 1], [1, 1]]) ctx.fillRect(m + x * 256, m + y * 256, 256 - 2 * m, 256 - 2 * m);
  } else if (motif === "store") {
    const pas = 512 / lames;
    for (let i = 0; i < lames; i++) ctx.fillRect(0, i * pas + pas * (1 - ouverture) / 2, 512, pas * ouverture);
  } else {
    ctx.fillRect(0, 0, 512, 512);
  }
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
