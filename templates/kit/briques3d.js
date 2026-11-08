/* Les briques de la 3D (kit.md, « La 3D ») : des objets du quotidien construits à partir de leurs
   vraies pièces, aux arêtes arrondies, à la taille réelle (1 unité = 10 cm) : l'ordinateur portable
   (coque, clavier touche par touche, pavé tactile, charnière, écran), le téléphone, la tablette, le
   carnet à spirale, le crayon, la tasse, et le plateau (une table de bois, un mur peint).

   On ne l'importe pas soi-même : plan3d la charge et la donne à `construire` (`briques.ordinateur()`…).
   Chaque écran accepte la vraie capture du client (son chemin, ou une texture déjà chargée), qui se
   pose en aplat : ses couleurs restent exactement les siennes. Aucune marque n'est dessinée (ni logo
   sur la coque, ni lettre sur les touches) : la seule marque visible est celle du client, sur son écran
   ou imprimée sur son carnet (`titre`, depuis OFFRE.json).

   Chaque brique est un THREE.Group posé sur sa base (y = 0 : elle se pose sur la table), sauf le
   téléphone et la tablette, centrés et debout face à la caméra (écran vers +z). */
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import * as M from "./matieres3d.js";

/** Les briques, liées aux outils du plan (sa façon de charger une image, ses aplats). */
export function fabriquerBriques(outils) {
  const { aplat } = outils;

  // ---------------------------------------------------------------------------
  // Les formes de base, à réutiliser pour construire un objet que le kit n'a pas
  // ---------------------------------------------------------------------------
  /** Un rectangle aux coins ronds (l × h, rayon r), centré. */
  const arrondi = outils.arrondi;

  /** Une boîte aux arêtes arrondies (l × h × p, rayon r), centrée. */
  function boite(l, h, p, r, matiere, segments = 3) {
    const m = new THREE.Mesh(new RoundedBoxGeometry(l, h, p, segments, r), matiere);
    m.castShadow = m.receiveShadow = true;
    return m;
  }

  /** Une dalle couchée (l × p, épaisseur e), coins ronds en plan (rCoins) et bords arrondis (rBords),
      posée sur y = 0. `echelleUV` : une texture couvre tant d'unités (8 pour du bois : 80 cm). */
  function dalle(l, p, e, rCoins, rBords, matiere, echelleUV = 1) {
    const b = Math.min(rBords, e / 2 - 1e-4);
    const g = new THREE.ExtrudeGeometry(arrondi(l - 2 * b, p - 2 * b, Math.max(1e-3, rCoins - b)), {
      depth: Math.max(1e-4, e - 2 * b), bevelEnabled: true, bevelThickness: b, bevelSize: b, bevelSegments: 4, curveSegments: 16,
    });
    g.rotateX(-Math.PI / 2);
    g.translate(0, b, 0);
    if (echelleUV !== 1) {
      const uv = g.attributes.uv;
      for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / echelleUV, uv.getY(i) / echelleUV);
    }
    g.computeVertexNormals();
    const m = new THREE.Mesh(g, matiere);
    m.castShadow = m.receiveShadow = true;
    return m;
  }

  /** Une plaque plate aux coins ronds, face à +z, sa texture la remplit (une capture, une page). */
  function plaque(l, h, r, matiere) {
    const m = new THREE.Mesh(outils.plaquer(new THREE.ShapeGeometry(arrondi(l, h, r), 24), l, h), matiere);
    m.receiveShadow = true;
    return m;
  }

  /** Une coque debout (l × h, épaisseur e), coins ronds (r) et bords arrondis (b), centrée, face à +z.
      `echelleUV` comme pour la dalle (8 pour du bois). */
  function coque(l, h, e, r, b, matiere, echelleUV = 1) {
    const g = new THREE.ExtrudeGeometry(arrondi(l - 2 * b, h - 2 * b, Math.max(1e-3, r - b)), {
      depth: Math.max(1e-4, e - 2 * b), bevelEnabled: true, bevelThickness: b, bevelSize: b, bevelSegments: 4, curveSegments: 20,
    });
    g.translate(0, 0, -(e - 2 * b) / 2);
    if (echelleUV !== 1) {
      const uv = g.attributes.uv;
      for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / echelleUV, uv.getY(i) / echelleUV);
    }
    g.computeVertexNormals();
    const m = new THREE.Mesh(g, matiere);
    m.castShadow = m.receiveShadow = true;
    return m;
  }

  function cylindre(rHaut, rBas, h, matiere, segments = 32) {
    const m = new THREE.Mesh(new THREE.CylinderGeometry(rHaut, rBas, h, segments), matiere);
    m.castShadow = m.receiveShadow = true;
    return m;
  }

  /** L'écran : sa capture en aplat, cadrée comme `object-fit: cover` (le haut de la page d'abord), et
      un reflet de vitre par-dessus. Rend { groupe, ecran, defiler(p) } : defiler(0) montre le haut
      de la capture, defiler(1) son bas (une page qui défile sur l'écran). */
  async function ecran(source, l, h, r, { cadrage = "haut", reflet = true, eteint = "#050506" } = {}) {
    const groupe = new THREE.Group();
    let defiler = () => {};
    let matiere;
    if (source) {
      const t = source.isTexture ? source : await outils.texture(source);
      const img = t.image, ia = (img.width || 1) / (img.height || 1), ea = l / h;
      t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
      if (ia >= ea) {
        t.repeat.set(ea / ia, 1); t.offset.set((1 - ea / ia) / 2, 0);
      } else {
        const part = ia / ea;
        t.repeat.set(1, part);
        defiler = (p) => { t.offset.y = (1 - part) * (1 - Math.min(1, Math.max(0, p))); };
        defiler(cadrage === "centre" ? 0.5 : cadrage === "bas" ? 1 : 0);
      }
      matiere = aplat(0xffffff, { map: t });
    } else {
      matiere = aplat(eteint);
    }
    const e = plaque(l, h, r, matiere);
    groupe.add(e);
    if (reflet) {
      const v = plaque(l, h, r, M.reflet());
      v.position.z = 0.0008;
      groupe.add(v);
    }
    return { groupe, ecran: e, defiler };
  }

  // ---------------------------------------------------------------------------
  // L'ordinateur portable (13 pouces : 30,4 × 21,5 cm), fermé à ouvrir(0), ouvert à 110° à ouvrir(1)
  // ---------------------------------------------------------------------------
  async function ordinateur({ ecran: capture = null, teinte = "argent", ouvert = 1, cadrage = "haut", reflet = true } = {}) {
    const L = 3.04, P = 2.15, eB = 0.115, eC = 0.05, Hc = 2.11;
    const coqueM = M.alu({ teinte }), sombre = M.plastique({ couleur: "#141416" }), touche = M.plastique({ couleur: "#1b1b1d" });
    const objet = new THREE.Group();

    // La base : la coque, le creux du clavier, les touches, le pavé tactile, les pieds, les ports.
    objet.add(dalle(L, P, eB, 0.13, 0.025, coqueM));
    const zClavier = -P / 2 + 0.15, profClavier = 1.13;
    const fondClavier = plaque(2.66, profClavier, 0.05, sombre);
    fondClavier.rotation.x = -Math.PI / 2;
    fondClavier.position.set(0, eB + 0.0006, zClavier + profClavier / 2);
    objet.add(fondClavier);
    const rangs = [
      [0.55, [1.5, ...Array(12).fill(1), 1]],
      [1, [1, ...Array(10).fill(1), 1, 1, 1.5]],
      [1, [1.5, ...Array(12).fill(1), 1]],
      [1, [1.8, ...Array(11).fill(1), 1.7]],
      [1, [2.3, ...Array(10).fill(1), 2.2]],
      [1, [1, 1, 1, 1.25, 5, 1.25, 1, "fleches"]],
    ];
    const pas = 2.54 / 14.5, jeu = 0.022, geos = new Map();
    const poserTouche = (x, z, lu, pu) => {
      const l = lu * pas - jeu, p = pu * pas - jeu, cle = `${l.toFixed(3)}:${p.toFixed(3)}`;
      if (!geos.has(cle)) geos.set(cle, new RoundedBoxGeometry(l, 0.014, p, 2, 0.012));
      const k = new THREE.Mesh(geos.get(cle), touche);
      k.position.set(x + l / 2 + jeu / 2, eB + 0.0006 + 0.007, z);
      k.receiveShadow = true;
      objet.add(k);
    };
    let z = zClavier + 0.05;
    for (const [hauteur, touches] of rangs) {
      const pz = hauteur * pas, zc = z + pz / 2;
      let x = -2.54 / 2;
      for (const lu of touches) {
        if (lu === "fleches") {                                  // ← ↑↓ → : des demi-touches
          poserTouche(x, zc + pz / 4, 1, 0.5); poserTouche(x + pas, zc - pz / 4, 1, 0.5);
          poserTouche(x + pas, zc + pz / 4, 1, 0.5); poserTouche(x + 2 * pas, zc + pz / 4, 1, 0.5);
          x += 3 * pas;
        } else {
          poserTouche(x, zc, lu, hauteur);
          x += lu * pas;
        }
      }
      z += pz;
    }
    const pave = plaque(1.32, 0.78, 0.05, M.alu({ teinte, brosse: false, rugosite: 0.22 }));
    pave.rotation.x = -Math.PI / 2;
    pave.position.set(0, eB + 0.0009, zClavier + profClavier + 0.1 + 0.39);
    const bordPave = plaque(1.335, 0.795, 0.055, sombre);
    bordPave.rotation.x = -Math.PI / 2;
    bordPave.position.set(0, eB + 0.0004, pave.position.z);
    objet.add(bordPave, pave);
    for (const [x, zz] of [[-1.3, -0.85], [1.3, -0.85], [-1.3, 0.85], [1.3, 0.85]]) {
      const pied = cylindre(0.04, 0.04, 0.01, M.mat({ couleur: "#1a1a1a" }), 20);
      pied.position.set(x, -0.003, zz);
      objet.add(pied);
    }
    for (const [i, lp] of [[0, 0.085], [1, 0.085]]) {
      const port = plaque(lp, 0.028, 0.012, sombre);
      port.rotation.y = -Math.PI / 2;
      port.position.set(-L / 2 - 0.0008, eB * 0.5, -0.6 + i * 0.13);
      objet.add(port);
    }
    const charniere = cylindre(0.028, 0.028, L - 0.6, M.alu({ teinte: "noir", brosse: false, rugosite: 0.4 }), 24);
    charniere.rotation.z = Math.PI / 2;
    charniere.position.set(0, eB + 0.005, -P / 2 + 0.035);
    objet.add(charniere);

    // Le couvercle : il pivote sur la charnière ; debout, son écran regarde +z.
    const couvercle = new THREE.Group();
    couvercle.position.set(0, eB, -P / 2 + 0.035);
    const coqueC = coque(L, Hc, eC, 0.13, 0.018, coqueM);
    coqueC.position.set(0, Hc / 2, -eC / 2 - 0.004);
    const vitre = plaque(L - 0.02, Hc - 0.02, 0.12, M.verre());
    vitre.position.set(0, Hc / 2, -0.0035);
    const Ls = L - 0.17, Hs = Ls / 1.6;
    const e = await ecran(capture, Ls, Hs, 0.025, { cadrage, reflet });
    e.groupe.position.set(0, 0.2 + Hs / 2, -0.0025);
    const camera = cylindre(0.011, 0.011, 0.002, M.verre({ couleur: "#16181c" }), 20);
    camera.rotation.x = Math.PI / 2;
    camera.position.set(0, Hc - 0.05, -0.003);
    couvercle.add(coqueC, vitre, e.groupe, camera);
    objet.add(couvercle);

    objet.ouvrir = (p) => { couvercle.rotation.x = Math.PI / 2 - THREE.MathUtils.degToRad(110) * Math.min(1, Math.max(0, p)); };
    objet.ouvrir(ouvert);
    Object.assign(objet, { couvercle, ecran: e.ecran, defiler: e.defiler, dimensions: { l: L, p: P, h: Hc } });
    return objet;
  }

  // ---------------------------------------------------------------------------
  // Le téléphone (7,2 × 14,8 cm) et la tablette (17,9 × 24,7 cm), debout, écran vers +z
  // ---------------------------------------------------------------------------
  async function telephone({ ecran: capture = null, teinte = "graphite", cadrage = "haut", reflet = true } = {}) {
    const l = 0.716, h = 1.476, e = 0.078, r = 0.11;
    const couleurs = { graphite: ["#55575c", "#2c2d30"], argent: ["#d8d9dc", "#e9e8e4"], noir: ["#2a2a2c", "#1b1b1d"], blanc: ["#e4e4e2", "#f1f0ec"] };
    const [cadre, dos] = couleurs[teinte] || couleurs.graphite;
    const objet = new THREE.Group();
    objet.add(coque(l, h, e, r, 0.014, M.alu({ teinte: cadre, brosse: false, rugosite: 0.2 })));
    const vitre = plaque(l - 0.012, h - 0.012, r - 0.006, M.verre());
    vitre.position.z = e / 2 + 0.0004;
    const s = await ecran(capture, l - 0.05, h - 0.05, r - 0.025, { cadrage, reflet });
    s.groupe.position.z = e / 2 + 0.0009;
    const ile = plaque(0.19, 0.056, 0.028, aplat("#000000"));
    ile.position.set(0, h / 2 - 0.025 - 0.06, e / 2 + 0.0022);
    objet.add(vitre, s.groupe, ile);
    const arriere = plaque(l - 0.012, h - 0.012, r - 0.006, M.verre({ couleur: dos, depoli: true }));
    arriere.rotation.y = Math.PI;
    arriere.position.z = -e / 2 - 0.0004;
    objet.add(arriere);
    const bloc = coque(0.31, 0.31, 0.014, 0.075, 0.005, M.verre({ couleur: dos }));
    bloc.position.set(-l / 2 + 0.2, h / 2 - 0.2, -e / 2 - 0.007);
    objet.add(bloc);
    for (const [x, y] of [[-0.06, 0.06], [0.06, -0.06]]) {
      const bague = cylindre(0.058, 0.058, 0.016, M.alu({ teinte: cadre, brosse: false, rugosite: 0.15 }), 32);
      bague.rotation.x = Math.PI / 2;
      bague.position.set(bloc.position.x + x, bloc.position.y + y, -e / 2 - 0.016);
      const lentille = cylindre(0.043, 0.043, 0.004, M.verre({ couleur: "#0a0b10" }), 32);
      lentille.rotation.x = Math.PI / 2;
      lentille.position.set(bague.position.x, bague.position.y, -e / 2 - 0.0245);
      objet.add(bague, lentille);
    }
    const flash = cylindre(0.016, 0.016, 0.003, M.mat({ couleur: "#e8e2cf", rugosite: 0.4 }), 20);
    flash.rotation.x = Math.PI / 2;
    flash.position.set(bloc.position.x + 0.07, bloc.position.y + 0.07, -e / 2 - 0.015);
    objet.add(flash);
    const bouton = (x, y, hb) => {
      const b = boite(0.014, hb, 0.026, 0.006, M.alu({ teinte: cadre, brosse: false, rugosite: 0.25 }));
      b.position.set(x, y, 0);
      objet.add(b);
    };
    bouton(l / 2 + 0.004, 0.27, 0.17);
    bouton(-l / 2 - 0.004, 0.42, 0.06); bouton(-l / 2 - 0.004, 0.27, 0.12); bouton(-l / 2 - 0.004, 0.11, 0.12);
    Object.assign(objet, { ecran: s.ecran, defiler: s.defiler, dimensions: { l, h, e }, epaisseur: e });
    return objet;
  }

  async function tablette({ ecran: capture = null, teinte = "argent", cadrage = "haut", reflet = true } = {}) {
    const l = 1.79, h = 2.47, e = 0.062, r = 0.18;
    const objet = new THREE.Group();
    objet.add(coque(l, h, e, r, 0.012, M.alu({ teinte, rugosite: 0.32 })));
    const vitre = plaque(l - 0.01, h - 0.01, r - 0.005, M.verre());
    vitre.position.z = e / 2 + 0.0004;
    const s = await ecran(capture, l - 0.17, h - 0.17, 0.1, { cadrage, reflet });
    s.groupe.position.z = e / 2 + 0.0009;
    const cam = cylindre(0.012, 0.012, 0.002, M.verre({ couleur: "#16181c" }), 20);
    cam.rotation.x = Math.PI / 2;
    cam.position.set(0, h / 2 - 0.045, e / 2 + 0.0015);
    objet.add(vitre, s.groupe, cam);
    const bague = cylindre(0.05, 0.05, 0.01, M.alu({ teinte, brosse: false, rugosite: 0.15 }), 32);
    bague.rotation.x = Math.PI / 2;
    bague.position.set(-l / 2 + 0.16, h / 2 - 0.16, -e / 2 - 0.004);
    const lentille = cylindre(0.036, 0.036, 0.003, M.verre({ couleur: "#0a0b10" }), 32);
    lentille.rotation.x = Math.PI / 2;
    lentille.position.set(bague.position.x, bague.position.y, -e / 2 - 0.0095);
    objet.add(bague, lentille);
    Object.assign(objet, { ecran: s.ecran, defiler: s.defiler, dimensions: { l, h, e }, epaisseur: e });
    return objet;
  }

  // ---------------------------------------------------------------------------
  // Le carnet à spirale (A5 : 14,8 × 21 cm), couché, la spirale à gauche ; ouvrir(1) rabat sa couverture
  // ---------------------------------------------------------------------------
  async function carnet({ couverture = "#1f2b3a", titre = "", encre = "#f4f1ea", pages = "lignes", ouvert = 0, matiere = null } = {}) {
    const l = 1.48, p = 2.1, eC = 0.016, eP = 0.07, E = eC * 2 + eP;
    const css = (c) => (typeof c === "string" ? c : "#" + new THREE.Color(c).getHexString());   // un jeton (THREE.Color) ou "#…"
    couverture = css(couverture); encre = css(encre);
    const objet = new THREE.Group();
    const dos = boite(l, eC, p, 0.007, M.carton({ couleur: "#3a3a3c" }));
    dos.position.y = eC / 2;
    const page = M.papier({ l: l - 0.06, h: p - 0.05, lignes: pages });
    const cote = M.tranche();
    const bloc = boite(l - 0.06, eP, p - 0.05, 0.004, [cote, cote, page, cote, cote, cote], 2);
    bloc.position.set(0.02, eC + eP / 2, 0);
    objet.add(dos, bloc);

    // La couverture : sa couleur (ou une matière), son titre imprimé (le nom de son offre, de la fiche).
    let faceCouv;
    if (matiere) {
      faceCouv = matiere;
    } else {
      const t = await M.impression(titre, { l: 740, h: 1050, fond: couverture, encre, taille: 0.075 });
      faceCouv = new THREE.MeshStandardMaterial({ map: t, roughness: 0.72 });
    }
    const bordCouv = new THREE.MeshStandardMaterial({ color: matiere ? 0x888888 : couverture, roughness: 0.75 });
    const pivot = new THREE.Group();
    const x0 = -l / 2 + 0.012, y0 = E / 2;
    pivot.position.set(x0, y0, 0);
    const couv = boite(l, eC, p, 0.007, matiere ? matiere : [bordCouv, bordCouv, faceCouv, bordCouv, bordCouv, bordCouv]);
    couv.position.set(l / 2 - 0.012, E - eC / 2 - y0, 0);
    pivot.add(couv);
    objet.add(pivot);

    // La spirale : des anneaux de métal qui passent dans les trous de la couverture et des pages.
    const nb = Math.floor((p - 0.12) / 0.085), anneau = new THREE.TorusGeometry(0.058, 0.0065, 10, 28);
    const trou = new THREE.Mesh(new THREE.CircleGeometry(0.014, 16), M.mat({ couleur: "#101010" }));
    for (let i = 0; i < nb; i++) {
      const zz = -((nb - 1) * 0.085) / 2 + i * 0.085;
      const a = new THREE.Mesh(anneau, M.chrome());
      a.position.set(x0, y0, zz);
      a.castShadow = true;
      objet.add(a);
      const t1 = trou.clone(); t1.rotation.x = -Math.PI / 2; t1.position.set(0.04, E - y0 + 0.0006, zz); pivot.add(t1);
      const t2 = trou.clone(); t2.rotation.x = -Math.PI / 2; t2.position.set(-l / 2 + 0.06, eC + eP + 0.0006, zz); objet.add(t2);
    }

    objet.ouvrir = (q) => { pivot.rotation.z = Math.PI * 0.985 * Math.min(1, Math.max(0, q)); };
    objet.ouvrir(ouvert);
    Object.assign(objet, { couverture: couv, page: bloc, dimensions: { l, p, e: E } });
    return objet;
  }

  // ---------------------------------------------------------------------------
  // Le crayon (17,5 cm), couché sur un pan, la pointe vers +x
  // ---------------------------------------------------------------------------
  function crayon({ couleur = "#f2b31b", gomme = "#ee9d97", virole = "clair" } = {}) {
    const R = 0.0416, objet = new THREE.Group();
    const hex = new THREE.Shape();
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      i ? hex.lineTo(R * Math.cos(a), R * Math.sin(a)) : hex.moveTo(R * Math.cos(a), R * Math.sin(a));
    }
    const lc = 1.42;
    const g = new THREE.ExtrudeGeometry(hex, { depth: lc - 0.008, bevelEnabled: true, bevelThickness: 0.004, bevelSize: 0.003, bevelSegments: 2 });
    g.translate(0, 0, -(lc - 0.008) / 2);
    g.rotateY(Math.PI / 2);
    g.computeVertexNormals();
    const corps = new THREE.Mesh(g, M.laque({ couleur }));
    corps.castShadow = corps.receiveShadow = true;
    corps.position.x = -0.01;
    const bois = cylindre(0.012, 0.0365, 0.16, M.bois({ essence: "cedre", planches: 1 }), 32);
    bois.rotation.z = -Math.PI / 2;
    bois.position.x = 0.7 + 0.08;
    const mine = cylindre(0.0012, 0.012, 0.036, M.mat({ couleur: "#2b2c30", rugosite: 0.32, metal: 0.45 }), 24);
    mine.rotation.z = -Math.PI / 2;
    mine.position.x = 0.86 + 0.018;
    const anneauV = cylindre(0.0372, 0.0372, 0.12, M.alu({ teinte: virole, brosse: false, rugosite: 0.28 }), 32);
    anneauV.rotation.z = -Math.PI / 2;
    anneauV.position.x = -0.72 - 0.05;
    for (const dx of [-0.035, 0, 0.035]) {
      const rainure = new THREE.Mesh(new THREE.TorusGeometry(0.0372, 0.0016, 6, 32), M.alu({ teinte: "gris", brosse: false, rugosite: 0.3 }));
      rainure.rotation.y = Math.PI / 2;
      rainure.position.x = anneauV.position.x + dx;
      objet.add(rainure);
    }
    const bout = new THREE.Mesh(new THREE.CapsuleGeometry(0.034, 0.05, 6, 24), M.mat({ couleur: gomme, rugosite: 0.85 }));
    bout.rotation.z = -Math.PI / 2;
    bout.position.x = -0.84;
    bout.castShadow = true;
    objet.add(corps, bois, mine, anneauV, bout);
    objet.position.y = R * Math.sin(Math.PI / 3);              // posé sur un pan : y = 0 sous lui
    const tout = new THREE.Group();
    tout.add(objet);
    tout.dimensions = { l: 1.75, h: 2 * R };
    return tout;
  }

  // ---------------------------------------------------------------------------
  // La tasse (8,2 cm de diamètre, 9,5 cm de haut), l'anse vers +x
  // ---------------------------------------------------------------------------
  function tasse({ couleur = "#f3f1ec", cafe = false } = {}) {
    const profil = [[0, 0.07], [0.34, 0.07], [0.37, 0.085], [0.38, 0.12], [0.38, 0.93], [0.384, 0.944], [0.395, 0.95],
      [0.406, 0.944], [0.41, 0.93], [0.41, 0.06], [0.404, 0.022], [0.388, 0.004], [0.36, 0], [0.33, 0], [0.32, 0.01], [0, 0.01]]
      .reverse()                                               // du dessous vers le dedans : les faces regardent dehors
      .map(([x, y]) => new THREE.Vector2(x, y));
    const corpsM = M.ceramique({ couleur });
    const corps = new THREE.Mesh(new THREE.LatheGeometry(profil, 72), corpsM);
    corps.castShadow = corps.receiveShadow = true;
    const chemin = new THREE.CatmullRomCurve3([[0.37, 0.8], [0.56, 0.82], [0.66, 0.66], [0.64, 0.42], [0.52, 0.27], [0.37, 0.25]]
      .map(([x, y]) => new THREE.Vector3(x, y, 0)));
    const anse = new THREE.Mesh(new THREE.TubeGeometry(chemin, 48, 0.036, 14, false), corpsM);
    anse.castShadow = anse.receiveShadow = true;
    const objet = new THREE.Group();
    objet.add(corps, anse);
    if (cafe) {
      const surface = new THREE.Mesh(new THREE.CircleGeometry(0.379, 48), new THREE.MeshPhysicalMaterial({ color: "#26150b", roughness: 0.06, clearcoat: 1 }));
      surface.rotation.x = -Math.PI / 2;
      surface.position.y = 0.79;
      objet.add(surface);
    }
    objet.dimensions = { l: 0.82, h: 0.95 };
    return objet;
  }

  // ---------------------------------------------------------------------------
  // La salle de classe : le pupitre d'écolier, sa chaise, le tableau (un décor complet, s'il sert l'offre)
  // ---------------------------------------------------------------------------
  /** Le pupitre d'écolier (60 × 45 cm, 64 cm de haut), posé sur y = 0, l'élève côté +z : son plateau de
      bois, son casier de métal, ses pieds en tube. */
  function pupitre({ bois = "clair", metal = "#3b3e44" } = {}) {
    const objet = new THREE.Group(), tube = M.mat({ couleur: metal, rugosite: 0.45, metal: 0.6 });
    const dessus = dalle(6, 4.5, 0.22, 0.25, 0.05, M.bois({ essence: bois, planches: 6 }), 8);
    dessus.position.y = 6.4 - 0.22;
    const casier = dalle(5.4, 3.6, 0.06, 0.1, 0.02, tube);
    casier.position.set(0, 5.3, -0.3);
    const fond = boite(5.4, 0.9, 0.06, 0.02, tube);
    fond.position.set(0, 5.75, -2.1);
    objet.add(dessus, casier, fond);
    for (const [x, z] of [[-2.7, -1.9], [2.7, -1.9], [-2.7, 1.9], [2.7, 1.9]]) {
      const pied = cylindre(0.13, 0.13, 6.2, tube, 16);
      pied.position.set(x, 3.1, z);
      objet.add(pied);
    }
    objet.dimensions = { l: 6, p: 4.5, h: 6.4 };
    return objet;
  }

  /** La chaise d'écolier (assise à 38 cm), posée sur y = 0, le dossier côté +z (face au pupitre en -z). */
  function chaise({ bois = "clair", metal = "#3b3e44" } = {}) {
    const objet = new THREE.Group(), tube = M.mat({ couleur: metal, rugosite: 0.45, metal: 0.6 });
    const assise = dalle(3.6, 3.6, 0.14, 0.3, 0.04, M.bois({ essence: bois, planches: 6 }), 8);
    assise.position.y = 3.8 - 0.14;
    const dossier = coque(3.6, 1.6, 0.14, 0.25, 0.04, M.bois({ essence: bois, planches: 6 }), 8);
    dossier.position.set(0, 6.0, 1.7);
    objet.add(assise, dossier);
    for (const [x, z] of [[-1.6, -1.6], [1.6, -1.6], [-1.6, 1.6], [1.6, 1.6]]) {
      const pied = cylindre(0.11, 0.11, z > 0 ? 6.8 : 3.7, tube, 16);
      pied.position.set(x, z > 0 ? 3.4 : 1.85, z);
      objet.add(pied);
    }
    objet.dimensions = { l: 3.6, p: 3.6, h: 6.8 };
    return objet;
  }

  /** Le tableau noir (2,4 × 1 m), centré, face à +z, à poser sur le mur : son ardoise verte, son cadre
      de bois, son rebord, deux craies et la brosse. Rien n'y est écrit (aucun faux texte). */
  function tableau({ l = 24, h = 10, ardoise = "#2c4a38", cadre = "chene" } = {}) {
    const objet = new THREE.Group(), bord = M.bois({ essence: cadre, planches: 1 });
    const surface = plaque(l, h, 0.05, M.mur({ couleur: ardoise, repetition: [l / 8, h / 8] }));
    objet.add(surface);
    for (const [x, y, lb, hb] of [[0, h / 2 + 0.2, l + 0.8, 0.4], [0, -h / 2 - 0.2, l + 0.8, 0.4], [-l / 2 - 0.2, 0, 0.4, h], [l / 2 + 0.2, 0, 0.4, h]]) {
      const b = boite(lb, hb, 0.35, 0.06, bord);
      b.position.set(x, y, 0.1);
      objet.add(b);
    }
    const rebord = boite(l, 0.12, 0.9, 0.04, bord);
    rebord.position.set(0, -h / 2 - 0.45, 0.45);
    objet.add(rebord);
    for (const [x, rz] of [[-3, 0.1], [-2.2, -0.25]]) {
      const craie = cylindre(0.055, 0.055, 0.8, M.mat({ couleur: "#f1efe8", rugosite: 0.95 }), 12);
      craie.rotation.z = Math.PI / 2 + rz;
      craie.position.set(x, -h / 2 - 0.33, 0.6);
      objet.add(craie);
    }
    const brosse = boite(1.2, 0.35, 0.5, 0.05, M.bois({ essence: "fonce", planches: 1 }));
    brosse.position.set(4, -h / 2 - 0.2, 0.5);
    objet.add(brosse);
    objet.dimensions = { l, h };
    return objet;
  }

  // ---------------------------------------------------------------------------
  // Le plateau : une table de bois (dessus à y = 0) et un mur peint derrière
  // ---------------------------------------------------------------------------
  function plateau({ bois = "chene", planches = 5, mur = "#e2ded7", recul = 7, largeur = 40, profondeur = 22, hauteurMur = 24, sansMur = false } = {}) {
    const groupe = new THREE.Group();
    const table = dalle(largeur, profondeur, 0.35, 0.25, 0.04, M.bois({ essence: bois, planches }), 8);
    table.position.set(0, -0.35, profondeur / 2 - recul);
    table.castShadow = false;
    groupe.add(table);
    let fond = null;
    if (!sansMur) {
      fond = new THREE.Mesh(new THREE.PlaneGeometry(largeur * 1.6, hauteurMur), M.mur({ couleur: mur, repetition: [largeur * 1.6 / 12, hauteurMur / 12] }));
      fond.position.set(0, hauteurMur / 2 - 0.35, -recul);
      fond.receiveShadow = true;
      groupe.add(fond);
    }
    Object.assign(groupe, { table, mur: fond });
    return groupe;
  }

  return { ordinateur, telephone, tablette, carnet, crayon, tasse, pupitre, chaise, tableau, plateau,
    boite, dalle, plaque, coque, cylindre, ecran };
}
