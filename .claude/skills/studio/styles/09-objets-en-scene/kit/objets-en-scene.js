/* Style n°9 · Objets en scène · la bibliothèque des objets (P) : objets connus dessinés en code, sans visage par
   défaut, et le visage (P.visage) pour le seul objet qui incarne le problème. Copie ce fichier et objets-en-scene.css dans
   assets/ du projet et charge-les dans index.html après le kit (style.md, « Les compositions du kit »).
   Les couleurs : des rôles, peints avec les jetons de la marque (objets-en-scene.css) : "accent" (son accent), "sombre",
   "clair", "alerte" (la mauvaise nouvelle : son jeton négatif) ; les anciens noms du banc restent compris
   ("citron" = accent, "nuit" = sombre, "papier" = clair, "rouge" = alerte).
   Les objets rebondissent plus que « presque aucun rebond » (metier.md : le dépassement de back.out(s) vaut
   4s³ / 27(s+1)²) : c'est leur élan, la signature du style. */
/* BANC PERSONNAGES (12/11/2026) : les personnages-objets, dessinés en code, et leurs gestes.
   Un personnage : P.perso(parent, {x, y, w, h}) pose sa place au sol (x, y = le milieu de sa base) ;
   chaque fabrique (P.clap, P.reveil, P.etiquette…) le remplit et lui donne un visage (P.visage).
   Tout est une fonction du temps de la timeline : les gestes s'ajoutent à `tl` à un instant donné,
   en général le début d'un mot de la voix (assets/mots.js). Jamais de hasard : K.rng. */
(function () {
  var P = window.P = {};
  var ROLES = { accent: "citron", sombre: "nuit", clair: "papier", alerte: "rouge" };
  P.role = function (c) { return ROLES[c] || c; };
  var NS = "http://www.w3.org/2000/svg";
  var n = 0;
  P.uid = function (p) { n += 1; return (p || "p") + "-" + n; };

  function div(parent, classe, style, html) {
    var e = document.createElement("div");
    if (classe) e.className = classe;
    if (style) e.setAttribute("style", style);
    if (html) e.innerHTML = html;
    parent.appendChild(e);
    return e;
  }
  P.div = div;

  // ---------------------------------------------------------------- le personnage
  // o : x, y (la base), w, h (la taille du corps), ombre (true), ombreW (largeur de l'ombre).
  P.perso = function (parent, o) {
    var r = div(parent, "p-perso" + (o.classe ? " " + o.classe : ""), "left:" + o.x + "px; top:" + o.y + "px;");
    if (o.id) r.id = o.id;
    var ombre = null;
    if (o.ombre !== false) {
      var ow = o.ombreW || o.w * 0.9;
      ombre = div(r, "p-ombre", "left:" + (-ow / 2) + "px; top:" + (-ow * 0.09) + "px; width:" + ow + "px; height:" + (ow * 0.18) + "px;");
    }
    var saut = div(r, "p-saut");
    var corps = div(saut, "p-corps", "left:" + (-o.w / 2) + "px; top:" + (-o.h) + "px; width:" + o.w + "px; height:" + o.h + "px;");
    return { racine: r, saut: saut, corps: corps, ombre: ombre, w: o.w, h: o.h };
  };

  // Une pièce de corps : une forme en matière (`mat` : "rouge", "papier"…), placée dans le corps.
  P.mat = function (parent, mat, x, y, w, h, rayon, extra) {
    mat = P.role(mat);
    return div(parent, "p-mat p-mat-" + mat, "left:" + x + "px; top:" + y + "px; width:" + w + "px; height:" + h + "px; border-radius:" + rayon + ";" + (extra || ""));
  };

  // ---------------------------------------------------------------- le visage
  var BOUCHES = {
    sourire: '<path class="p-trait" d="M-20,-6 Q0,14 20,-6"/>',
    grand: '<path class="p-plein" d="M-25,-11 L25,-11 Q23,22 0,25 Q-23,22 -25,-11Z"/><path class="p-langue" d="M-13,15 Q0,4 13,15 Q8,23 0,24 Q-8,23 -13,15Z"/>',
    ouvert: '<path class="p-plein" d="M-16,-7 L16,-7 Q14,12 0,13 Q-14,12 -16,-7Z"/>',
    o: '<ellipse class="p-plein" cx="0" cy="2" rx="9" ry="12"/>',
    oo: '<ellipse class="p-plein" cx="0" cy="6" rx="15" ry="20"/>',
    plat: '<path class="p-trait" d="M-14,0 L14,0"/>',
    triste: '<path class="p-trait" d="M-18,9 Q0,-8 18,9"/>',
    dents: '<rect class="p-dent" x="-25" y="-11" width="50" height="24" rx="11"/><path class="p-trait" style="stroke-width:4" d="M-25,1 L25,1 M-9,-11 L-9,13 M8,-11 L8,13"/>',
    malin: '<path class="p-trait" d="M-18,3 Q4,12 22,-10"/>',
    vague: '<path class="p-trait" d="M-21,3 Q-11,-6 0,3 Q11,12 21,3"/>',
    petit: '<path class="p-trait" d="M-9,-2 Q0,6 9,-2"/>'
  };
  P.BOUCHES = Object.keys(BOUCHES);

  // o : x, y (centre du visage dans le corps), taille (px pour 1em), peau (classe de matière pour les
  // paupières : "rouge"…), clair (traits papier, sur un écran sombre), joues (true), bouche ("sourire").
  P.visage = function (parent, o) {
    var v = div(parent, "p-visage" + (o.clair ? " p-visage-clair" : ""), "left:" + o.x + "px; top:" + o.y + "px; font-size:" + o.taille + "px;");
    var V = { el: v, bouches: {} };
    if (o.joues !== false && !o.clair) {
      V.joues = [div(v, "p-joue p-joue-g"), div(v, "p-joue p-joue-d")];
    }
    V.yeux = ["g", "d"].map(function (c) {
      var w = div(v, "p-oeil p-oeil-" + c);
      var oeil = { w: w, o: div(w, "p-o"), f: div(w, "p-f"), z: div(w, "p-z"), c: div(w, "p-cerne") };
      if (o.peau) oeil.p = div(oeil.o, "p-paupiere p-mat p-mat-sans-reflet p-mat-" + o.peau);
      return oeil;
    });
    V.sourcils = [div(v, "p-sourcil p-sourcil-g"), div(v, "p-sourcil p-sourcil-d")];
    if (o.sansSourcils) V.sourcils.forEach(function (s) { s.style.display = "none"; });
    var b = div(v, "p-bouche");
    if (o.boucheY != null) b.style.top = o.boucheY + "em";
    V.bouche_el = b;
    Object.keys(BOUCHES).forEach(function (k) {
      var s = document.createElementNS(NS, "svg");
      s.setAttribute("viewBox", "-50 -30 100 60");
      s.innerHTML = BOUCHES[k];
      b.appendChild(s);
      V.bouches[k] = s;
    });
    V.goutte_el = div(v, "p-goutte");
    var depart = o.bouche || "sourire";
    V.bouches[depart].classList.add("p-active");
    V.courante = depart;
    if (o.yeux) poserYeux(V, o.yeux);

    // La bouche change d'un coup (comme une bouche de dessin animé), à l'instant t.
    V.bouche = function (tl, t, nom) {
      Object.keys(V.bouches).forEach(function (k) { tl.set(V.bouches[k], { opacity: k === nom ? 1 : 0 }, t); });
      return V;
    };
    // Les yeux : "ouverts", "joie" (∩ ∩), "fermes" (∪ ∪), "clin" (le droit plissé), "grands".
    V.yeuxA = function (tl, t, nom) {
      var etats = { ouverts: ["o", "o"], joie: ["f", "f"], fermes: ["z", "z"], clin: ["o", "f"], grands: ["o", "o"] }[nom];
      V.yeux.forEach(function (y, i) {
        ["o", "f", "z"].forEach(function (k) { tl.set(y[k], { opacity: etats[i] === k ? 1 : 0 }, t); });
      });
      tl.to(V.yeux.map(function (y) { return y.w; }), { scale: nom === "grands" ? 1.45 : 1, duration: 0.18, ease: "back.out(2.4)" }, t);
      return V;
    };
    // Un clignement de 0,14 s.
    V.cligne = function (tl, t) {
      var os = V.yeux.map(function (y) { return y.o; });
      tl.to(os, { scaleY: 0.08, duration: 0.06, ease: "power2.in" }, t)
        .to(os, { scaleY: 1, duration: 0.09, ease: "power2.out" }, t + 0.06);
      return V;
    };
    V.clignements = function (tl, liste) { liste.forEach(function (t) { V.cligne(tl, t); }); return V; };
    // Le regard : les yeux glissent de (dx, dy) em.
    V.regard = function (tl, t, dx, dy, d) {
      tl.to(V.yeux.map(function (y) { return y.o; }), { x: (dx || 0) + "em", y: (dy || 0) + "em", duration: d == null ? 0.16 : d, ease: "power2.out" }, t);
      return V;
    };
    // Les sourcils : angle (degrés, > 0 = le bout intérieur monte : inquiet), dy (em, < 0 = plus haut).
    V.sourcilsA = function (tl, t, angle, dy, d) {
      tl.to(V.sourcils[0], { rotation: -angle, y: (dy || 0) + "em", duration: d == null ? 0.16 : d, ease: "power2.out" }, t)
        .to(V.sourcils[1], { rotation: angle, y: (dy || 0) + "em", duration: d == null ? 0.16 : d, ease: "power2.out" }, t);
      return V;
    };
    // Les paupières tombent (p de 0 à 1 : la part de l'œil couverte).
    V.paupieres = function (tl, t, p, d) {
      var ps = V.yeux.map(function (y) { return y.p; }).filter(Boolean);
      if (ps.length) tl.to(ps, { height: (p * 104) + "%", duration: d == null ? 0.2 : d, ease: "power2.inOut" }, t);
      return V;
    };
    V.cernes = function (tl, t, on) { tl.to(V.yeux.map(function (y) { return y.c; }), { opacity: on ? 1 : 0, duration: 0.25 }, t); return V; };
    // Une goutte de sueur glisse le long de la tempe.
    V.goutte = function (tl, t, d) {
      d = d || 0.9;
      tl.fromTo(V.goutte_el, { opacity: 0, y: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.14, ease: "back.out(2)", immediateRender: false }, t)
        .to(V.goutte_el, { y: "0.9em", duration: d, ease: "power1.in" }, t + 0.14)
        .to(V.goutte_el, { opacity: 0, duration: 0.15 }, t + 0.14 + d - 0.12);
      return V;
    };
    return V;
  };
  function poserYeux(V, nom) {
    var etats = { ouverts: ["o", "o"], joie: ["f", "f"], fermes: ["z", "z"], clin: ["o", "f"] }[nom] || ["o", "o"];
    V.yeux.forEach(function (y, i) { ["o", "f", "z"].forEach(function (k) { y[k].style.opacity = etats[i] === k ? 1 : 0; }); });
  }

  // ---------------------------------------------------------------- les gestes du corps
  // Il surgit : de rien à sa taille, avec un rebond (le rebond est pour les personnages, jamais pour un texte).
  P.pop = function (tl, p, t, o) {
    o = o || {};
    gsap.set(p.saut, { scale: 0 });
    if (p.ombre) gsap.set(p.ombre, { scale: 0 });
    tl.to(p.saut, { scale: 1, duration: o.duree || 0.55, ease: o.ease || "back.out(2.2)" }, t);
    if (p.ombre) tl.to(p.ombre, { scale: 1, duration: 0.35, ease: "power2.out" }, t);
    if (o.etire !== false) {
      tl.fromTo(p.corps, { scaleY: 1.18, scaleX: 0.86 }, { scaleY: 1, scaleX: 1, duration: 0.6, ease: "elastic.out(1.1, 0.42)", immediateRender: false }, t + 0.05);
    }
    return t + (o.duree || 0.55);
  };
  // Il tombe du ciel et s'écrase au sol : de dy (px au-dessus) à 0.
  P.tombe = function (tl, p, t, o) {
    o = o || {};
    var dy = o.dy || 900, d = o.duree || 0.42;
    gsap.set(p.saut, { y: -dy });
    if (p.ombre) gsap.set(p.ombre, { scale: 0.2, opacity: 0 });
    tl.to(p.saut, { y: 0, duration: d, ease: "power2.in" }, t);
    if (p.ombre) tl.to(p.ombre, { scale: 1, opacity: 1, duration: d, ease: "power2.in" }, t);
    P.ecrase(tl, p, t + d, o.force || 1);
    return t + d;
  };
  // L'écrasement à l'atterrissage, puis il se remet en place en tremblant un peu.
  P.ecrase = function (tl, p, t, force) {
    force = force == null ? 1 : force;
    tl.to(p.corps, { scaleY: 1 - 0.22 * force, scaleX: 1 + 0.18 * force, duration: 0.07, ease: "power2.out" }, t)
      .to(p.corps, { scaleY: 1, scaleX: 1, duration: 0.55, ease: "elastic.out(1.2, 0.35)" }, t + 0.07);
    return t + 0.62;
  };
  // Un saut sur place (ou vers dx) : il se ramasse, s'étire en montant, s'écrase en retombant.
  P.saute = function (tl, p, t, o) {
    o = o || {};
    var h = o.hauteur || 140, d = o.duree || 0.5, dx = o.dx || 0;
    tl.to(p.corps, { scaleY: 0.84, scaleX: 1.12, duration: 0.08, ease: "power2.out" }, t)
      .to(p.corps, { scaleY: 1.1, scaleX: 0.92, duration: 0.12, ease: "power2.out" }, t + 0.08)
      .to(p.saut, { y: -h, duration: d / 2, ease: "power2.out" }, t + 0.08)
      .to(p.corps, { scaleY: 1, scaleX: 1, duration: d / 2, ease: "sine.inOut" }, t + 0.2)
      .to(p.saut, { y: 0, duration: d / 2, ease: "power2.in" }, t + 0.08 + d / 2);
    if (dx) tl.to(p.racine, { x: "+=" + dx, duration: d, ease: "sine.inOut" }, t + 0.08);
    if (p.ombre) tl.to(p.ombre, { scale: 0.6, opacity: 0.5, duration: d / 2, ease: "power2.out", yoyo: true, repeat: 1 }, t + 0.08);
    P.ecrase(tl, p, t + 0.08 + d, 0.7);
    return t + 0.08 + d;
  };
  // Non de la tête : n allers-retours de ± amp degrés.
  P.secoue = function (tl, p, t, o) {
    o = o || {};
    var amp = o.amp || 9, nb = o.nombre || 3, d = o.duree || 0.11;
    for (var i = 0; i < nb; i++) tl.to(p.corps, { rotation: i % 2 ? -amp : amp, duration: d, ease: "sine.inOut" }, t + i * d);
    tl.to(p.corps, { rotation: 0, duration: d * 1.4, ease: "sine.out" }, t + nb * d);
    return t + nb * d + d * 1.4;
  };
  // Il penche (degrés), depuis sa base.
  P.penche = function (tl, p, t, angle, d) { tl.to(p.corps, { rotation: angle, duration: d || 0.3, ease: "back.out(2)" }, t); return t + (d || 0.3); };
  // Il respire : un très léger gonflement, du début à la fin (des allers-retours comptés : jamais repeat -1).
  P.respire = function (tl, p, debut, fin, o) {
    o = o || {};
    var per = o.periode || 1.4, amp = o.amp || 0.022, nb = Math.max(1, Math.floor((fin - debut) / (per / 2)));
    tl.to(p.corps, { scaleY: 1 + amp, scaleX: 1 - amp * 0.6, duration: per / 2, ease: "sine.inOut", yoyo: true, repeat: nb - 1 }, debut);
  };
  // Il se ratatine et disparaît.
  P.part = function (tl, p, t, o) {
    o = o || {};
    tl.to(p.saut, { scale: 0, duration: o.duree || 0.3, ease: "back.in(2)" }, t);
    if (p.ombre) tl.to(p.ombre, { scale: 0, duration: 0.25 }, t);
    return t + (o.duree || 0.3);
  };

  // ---------------------------------------------------------------- les personnages
  // Le clap de cinéma (la vidéo). o.couleur ("rouge"). Rend aussi `bras` : rotation -26 (ouvert) à 0 (claqué).
  P.clap = function (parent, o) {
    var w = 420, h = 390;
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id });
    P.mat(p.corps, P.role(o.couleur || "rouge"), 0, 120, w, 270, "38px");
    div(p.corps, "p-part p-rayures", "left:0; top:74px; width:" + w + "px; height:54px; border-radius:12px; overflow:hidden;");
    p.bras = div(p.corps, "p-part p-rayures-inv", "left:0; top:18px; width:" + w + "px; height:54px; border-radius:12px; overflow:hidden; transform-origin: 4% 100%;");
    P.mat(p.corps, "papier", -6, 54, 36, 36, "50%");
    gsap.set(p.bras, { rotation: o.ouvert == null ? -26 : o.ouvert });
    p.visage = P.visage(p.corps, { x: w / 2, y: 250, taille: 64, peau: P.role(o.couleur || "rouge"), bouche: o.bouche, yeux: o.yeux });
    return p;
  };
  // Il claque : le bras s'ouvre puis tombe d'un coup.
  P.claque = function (tl, p, t) {
    tl.to(p.bras, { rotation: -34, duration: 0.12, ease: "power2.out" }, t - 0.14)
      .to(p.bras, { rotation: 0, duration: 0.07, ease: "power3.in" }, t - 0.02)
      .to(p.bras, { rotation: -26, duration: 0.5, ease: "elastic.out(1, 0.4)" }, t + 0.18);
    P.ecrase(tl, p, t + 0.05, 0.45);
  };

  // Le curseur de la souris (l'humain). Pointe en haut à gauche.
  P.curseur = function (parent, o) {
    var w = 230, h = 300;
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id, ombreW: 180 });
    var id = P.uid("curseur");
    p.corps.insertAdjacentHTML("beforeend",
      '<svg class="p-part" viewBox="0 0 230 300" style="left:0; top:0; width:230px; height:300px; overflow:visible;">' +
      '<defs><radialGradient id="' + id + '" cx="30%" cy="25%" r="85%"><stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="var(--o-papier)"/><stop offset="1" stop-color="var(--o-papier-ombre)"/></radialGradient></defs>' +
      '<path d="M18,10 L18,262 Q18,276 30,266 L86,214 L124,290 Q130,300 142,295 L170,282 Q180,276 176,266 L138,190 L210,184 Q224,182 214,172 L34,8 Q18,-4 18,10Z" fill="url(#' + id + ')" stroke="var(--o-nuit)" stroke-width="12" stroke-linejoin="round"/></svg>');
    p.visage = P.visage(p.corps, { x: 78, y: 132, taille: 36, peau: "papier", bouche: o.bouche, yeux: o.yeux });
    return p;
  };

  // Le réveil : corps rond, deux cloches, un cadran papier avec son visage, deux aiguilles.
  P.reveil = function (parent, o) {
    var w = 380, h = 420, c = P.role(o.couleur || "orange");
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id });
    P.mat(p.corps, "nuit", 70, 378, 46, 42, "40% 40% 50% 50%");
    P.mat(p.corps, "nuit", 264, 378, 46, 42, "40% 40% 50% 50%");
    p.cloches = [P.mat(p.corps, c, 6, 24, 118, 104, "60% 60% 30% 30%", "transform: rotate(-24deg);"), P.mat(p.corps, c, 256, 24, 118, 104, "60% 60% 30% 30%", "transform: rotate(24deg);")];
    P.mat(p.corps, "nuit", 172, 30, 36, 46, "12px");
    P.mat(p.corps, c, 20, 60, 340, 340, "50%");
    p.cadran = P.mat(p.corps, "papier", 52, 92, 276, 276, "50%", "box-shadow: inset 0 6px 14px rgba(0,0,0,0.12);");
    for (var i = 0; i < 12; i++) {
      var a = i * 30 * Math.PI / 180;
      div(p.corps, "p-part", "left:" + (190 + Math.sin(a) * 118 - 4) + "px; top:" + (230 - Math.cos(a) * 118 - 9) + "px; width:8px; height:18px; border-radius:4px; background:var(--brand-gris-4); transform: rotate(" + (i * 30) + "deg);");
    }
    p.heures = div(p.corps, "p-aiguille", "left:184px; top:162px; width:12px; height:68px;");
    p.minutes = div(p.corps, "p-aiguille", "left:185px; top:126px; width:10px; height:104px; background: var(--o-rouge);");
    P.mat(p.corps, "nuit", 178, 218, 24, 24, "50%");
    p.visage = P.visage(p.corps, { x: 190, y: 214, taille: 42, peau: "papier", bouche: o.bouche, yeux: o.yeux, boucheY: 1.05 });
    return p;
  };

  // L'étiquette de prix : forme SVG, couture en pointillés, trou et ficelle, un bandeau qui porte un mot.
  P.etiquette = function (parent, o) {
    var w = o.w || 300, h = o.h || 400, c = P.role(o.couleur || "rouge"), id = P.uid("tag");
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id, ombre: o.ombre });
    var r = Math.min(w, h) * 0.08, cut = w * 0.22, top = 0;
    var d = "M" + cut + "," + top + " L" + (w - cut) + "," + top + " L" + w + "," + (cut * 0.9) + " L" + w + "," + (h - r) + " Q" + w + "," + h + " " + (w - r) + "," + h +
      " L" + r + "," + h + " Q0," + h + " 0," + (h - r) + " L0," + (cut * 0.9) + "Z";
    p.corps.insertAdjacentHTML("beforeend",
      '<svg class="p-part" viewBox="0 0 ' + w + " " + h + '" style="left:0; top:0; width:' + w + "px; height:" + h + 'px; overflow:visible;">' +
      '<defs><radialGradient id="' + id + '" cx="30%" cy="22%" r="95%"><stop offset="0" stop-color="var(--o-' + c + '-clair)"/><stop offset="0.5" stop-color="var(--o-' + c + ')"/><stop offset="1" stop-color="var(--o-' + c + '-ombre)"/></radialGradient></defs>' +
      '<path d="' + d + '" fill="url(#' + id + ')" stroke="var(--o-' + c + '-ombre)" stroke-width="3" stroke-linejoin="round"/>' +
      '<path d="' + d + '" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="' + Math.max(3, w * 0.012) + '" stroke-dasharray="' + (w * 0.03) + " " + (w * 0.025) + '" transform="translate(' + (w * 0.05) + "," + (w * 0.05) + ") scale(" + (1 - 0.1 * 1) + "," + (1 - 0.1 * w / h) + ')"/>' +
      '<circle cx="' + (w / 2) + '" cy="' + (w * 0.17) + '" r="' + (w * 0.065) + '" fill="var(--o-papier)" stroke="var(--o-' + c + '-ombre)" stroke-width="' + (w * 0.02) + '"/></svg>');
    if (o.ficelle) div(p.corps, "p-part", "left:" + (w / 2 - 2) + "px; top:" + (-o.ficelle + w * 0.17) + "px; width:4px; height:" + o.ficelle + "px; background: var(--brand-gris-3);");
    if (o.mot != null) {
      p.bandeau = P.mat(p.corps, c, w * 0.08, h * 0.28, w * 0.84, h * 0.2, (w * 0.04) + "px", "background: var(--o-" + c + "-ombre);");
      p.mot = div(p.bandeau, "p-texte", "left:0; right:0; top:50%; margin-top:" + (-h * 0.075) + "px; font-size:" + (h * 0.15) + "px; color: " + (c === "citron" ? "var(--brand-contrast)" : "var(--o-papier)") + ";", o.mot);
    }
    p.visage = P.visage(p.corps, { x: w / 2, y: h * 0.66, taille: w * 0.18, peau: c, bouche: o.bouche, yeux: o.yeux });
    return p;
  };

  // Un bloc (le pixel, le carré) : un cube aux angles doux.
  P.bloc = function (parent, o) {
    var s = o.taille || 160;
    var p = P.perso(parent, { x: o.x, y: o.y, w: s, h: s, id: o.id, ombre: o.ombre });
    P.mat(p.corps, P.role(o.couleur || "bleu"), 0, 0, s, s, (s * 0.17) + "px");
    p.visage = P.visage(p.corps, { x: s / 2, y: s * 0.46, taille: s * 0.19, peau: P.role(o.couleur || "bleu"), bouche: o.bouche, yeux: o.yeux });
    return p;
  };
  // Le rond.
  P.rond = function (parent, o) {
    var s = o.taille || 200;
    var p = P.perso(parent, { x: o.x, y: o.y, w: s, h: s, id: o.id, ombre: o.ombre });
    p.peau = P.mat(p.corps, P.role(o.couleur || "rose"), 0, 0, s, s, "50%");
    p.visage = P.visage(p.corps, { x: s / 2, y: s * 0.46, taille: s * 0.16, peau: P.role(o.couleur || "rose"), bouche: o.bouche, yeux: o.yeux });
    return p;
  };
  // Le triangle (pointe en haut, angles arrondis).
  P.triangle = function (parent, o) {
    var s = o.taille || 220, c = P.role(o.couleur || "citron"), id = P.uid("tri");
    var p = P.perso(parent, { x: o.x, y: o.y, w: s, h: s * 0.9, id: o.id, ombre: o.ombre });
    var H = s * 0.9;
    p.corps.insertAdjacentHTML("beforeend",
      '<svg class="p-part" viewBox="0 0 ' + s + " " + H + '" style="left:0; top:0; width:' + s + "px; height:" + H + 'px; overflow:visible;">' +
      '<defs><radialGradient id="' + id + '" cx="35%" cy="35%" r="85%"><stop offset="0" stop-color="var(--o-' + c + '-clair)"/><stop offset="0.5" stop-color="var(--o-' + c + ')"/><stop offset="1" stop-color="var(--o-' + c + '-ombre)"/></radialGradient></defs>' +
      '<path d="M' + (s / 2) + "," + (s * 0.06) + " L" + (s * 0.96) + "," + (H - s * 0.04) + " L" + (s * 0.04) + "," + (H - s * 0.04) + 'Z" fill="url(#' + id + ')" stroke="url(#' + id + ')" stroke-width="' + (s * 0.12) + '" stroke-linejoin="round"/></svg>');
    p.visage = P.visage(p.corps, { x: s / 2, y: H * 0.62, taille: s * 0.13, peau: null, bouche: o.bouche, yeux: o.yeux, joues: false });
    return p;
  };

  // La télé : un écran sombre où vit un visage clair, deux antennes. `bandeau` : le sous-titre en bas de l'écran.
  P.tele = function (parent, o) {
    var w = 380, h = 330, c = P.role(o.couleur || "violet");
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id });
    div(p.corps, "p-part", "left:118px; top:-6px; width:8px; height:96px; border-radius:4px; background: var(--o-nuit); transform: rotate(-30deg); transform-origin: 50% 100%;");
    div(p.corps, "p-part", "left:254px; top:-6px; width:8px; height:96px; border-radius:4px; background: var(--o-nuit); transform: rotate(30deg); transform-origin: 50% 100%;");
    P.mat(p.corps, c, 66, -20, 30, 30, "50%");
    P.mat(p.corps, c, 284, -20, 30, 30, "50%");
    P.mat(p.corps, "nuit", 70, 300, 50, 34, "30% 30% 50% 50%");
    P.mat(p.corps, "nuit", 260, 300, 50, 34, "30% 30% 50% 50%");
    P.mat(p.corps, c, 0, 70, w, 240, "44px");
    p.ecran = P.mat(p.corps, "nuit", 30, 96, 320, 188, "30px", "box-shadow: inset 0 0 0 4px rgba(0,0,0,0.25);");
    p.visage = P.visage(p.corps, { x: 190, y: 150, taille: 44, clair: true, bouche: o.bouche || "sourire", yeux: o.yeux });
    p.sous = div(p.ecran, "p-part", "left:30px; right:30px; bottom:16px; height:52px; border-radius:10px; background: var(--o-citron); overflow:hidden;");
    p.sousMot = div(p.sous, "p-texte", "left:0; right:0; top:4px; font-size:44px; color: var(--o-nuit);", o.bandeau || "");
    return p;
  };

  // La loupe : un anneau, un verre, un manche ; dans le verre, un œil énorme (grossi par la loupe).
  P.loupe = function (parent, o) {
    var w = 360, h = 400;
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id, ombreW: 260 });
    p.manche = P.mat(p.corps, "orange", 214, 212, 70, 200, "35px", "transform: rotate(-40deg); transform-origin: 50% 0%;");
    P.mat(p.corps, "nuit", 10, 0, 300, 300, "50%");
    p.verre = div(p.corps, "p-part", "left:34px; top:24px; width:252px; height:252px; border-radius:50%; overflow:hidden; background: radial-gradient(110% 110% at 32% 28%, #ffffff 0%, var(--o-papier) 45%, var(--o-papier-ombre) 100%);");
    p.oeil = div(p.verre, "p-part", "left:126px; top:132px; width:0; height:0;");
    p.globe = div(p.oeil, "p-part", "left:-62px; top:-74px; width:124px; height:164px; border-radius:50%; background: var(--o-encre);");
    div(p.globe, "p-part", "right:14px; top:20px; width:40px; height:40px; border-radius:50%; background:#ffffff;");
    p.sourcil = div(p.oeil, "p-part", "left:-70px; top:-112px; width:140px; height:26px; border-radius:13px; background: var(--o-encre);");
    div(p.corps, "p-part", "left:34px; top:24px; width:252px; height:252px; border-radius:50%; background: radial-gradient(closest-side at 30% 26%, rgba(255,255,255,0.7), rgba(255,255,255,0) 60%);");
    return p;
  };

  // La tirelire : un cochon rose, sa fente, son groin.
  P.tirelire = function (parent, o) {
    var w = 460, h = 360;
    var p = P.perso(parent, { x: o.x, y: o.y, w: w, h: h, id: o.id });
    ["70px", "330px"].forEach(function (x) { P.mat(p.corps, "rose", parseFloat(x), 286, 60, 74, "18px"); });
    ["130px", "270px"].forEach(function (x) { P.mat(p.corps, "rose", parseFloat(x), 290, 60, 70, "18px", ""); });
    p.oreilles = [P.mat(p.corps, "rose", 92, 20, 90, 96, "20% 80% 20% 70%", "transform: rotate(-28deg);"), P.mat(p.corps, "rose", 278, 20, 90, 96, "80% 20% 70% 20%", "transform: rotate(28deg);")];
    p.peau = P.mat(p.corps, "rose", 0, 50, w, 270, "50%");
    p.fente = div(p.corps, "p-part", "left:178px; top:66px; width:104px; height:18px; border-radius:9px; background: var(--o-rose-ombre);");
    p.visage = P.visage(p.corps, { x: 230, y: 158, taille: 44, peau: "rose", bouche: o.bouche, yeux: o.yeux, boucheY: 2.15 });
    p.groin = P.mat(p.corps, "rose", 178, 186, 104, 76, "50%", "background: radial-gradient(120% 120% at 35% 30%, var(--o-rose-clair), var(--o-rose) 70%); box-shadow: 0 6px 12px rgba(0,0,0,0.25);");
    div(p.groin, "p-part", "left:26px; top:24px; width:16px; height:28px; border-radius:50%; background: var(--o-rose-ombre);");
    div(p.groin, "p-part", "left:62px; top:24px; width:16px; height:28px; border-radius:50%; background: var(--o-rose-ombre);");
    return p;
  };

  // Le dé : blanc, six points ; les deux points du haut servent d'yeux, des sourcils peuvent paraître.
  P.de = function (parent, o) {
    var s = o.taille || 260;
    var p = P.perso(parent, { x: o.x, y: o.y, w: s, h: s, id: o.id });
    P.mat(p.corps, "papier", 0, 0, s, s, (s * 0.2) + "px", "box-shadow: inset -10px -14px 0 rgba(0,0,0,0.06);");
    p.points = [];
    [[0.3, 0.25], [0.7, 0.25], [0.3, 0.5], [0.7, 0.5], [0.3, 0.75], [0.7, 0.75]].forEach(function (q) {
      p.points.push(div(p.corps, "p-part", "left:" + (q[0] * s - s * 0.075) + "px; top:" + (q[1] * s - s * 0.075) + "px; width:" + (s * 0.15) + "px; height:" + (s * 0.15) + "px; border-radius:50%; background: var(--o-encre);"));
    });
    p.points.push(div(p.corps, "p-part", "left:" + (0.5 * s - s * 0.075) + "px; top:" + (0.5 * s - s * 0.075) + "px; width:" + (s * 0.15) + "px; height:" + (s * 0.15) + "px; border-radius:50%; background: var(--o-encre); opacity:0;"));
    // La face montrée (1 à 6) : les points visibles, d'un coup.
    var FACES = { 1: [6], 2: [0, 5], 3: [0, 6, 5], 4: [0, 1, 4, 5], 5: [0, 1, 4, 5, 6], 6: [0, 1, 2, 3, 4, 5] };
    p.face = function (tl, t, n) { p.points.forEach(function (pt, k) { tl.set(pt, { opacity: FACES[n].indexOf(k) >= 0 ? 1 : 0 }, t); }); };
    p.sourcils = [div(p.corps, "p-part", "left:" + (0.3 * s - s * 0.11) + "px; top:" + (0.06 * s) + "px; width:" + (s * 0.22) + "px; height:" + (s * 0.05) + "px; border-radius:6px; background: var(--o-encre); opacity:0;"),
      div(p.corps, "p-part", "left:" + (0.7 * s - s * 0.11) + "px; top:" + (0.06 * s) + "px; width:" + (s * 0.22) + "px; height:" + (s * 0.05) + "px; border-radius:6px; background: var(--o-encre); opacity:0;")];
    return p;
  };

  // Une pièce d'or (une matière d'objet connu : l'argent).
  P.piece = function (parent, x, y, s, o) {
    o = o || {};
    var e = P.mat(parent, "or", x - s / 2, y - s / 2, s, s, "50%", "box-shadow: inset 0 0 0 " + (s * 0.07) + "px var(--o-or-ombre);" + (o.style || ""));
    div(e, "p-texte", "left:0; right:0; top:50%; margin-top:" + (-s * 0.29) + "px; font-size:" + (s * 0.56) + "px; color: var(--o-or-ombre);", "€");
    return e;
  };
  // Des lunettes de soleil (la décontraction), centrées sur (cx, cy) du parent, largeur w.
  P.lunettes = function (parent, cx, cy, w) {
    var h = w * 0.3, e = div(parent, "p-part", "left:" + (cx - w / 2) + "px; top:" + (cy - h / 2) + "px; width:" + w + "px; height:" + h + "px;");
    [0, 1].forEach(function (k) {
      var v = P.mat(e, "nuit", k ? w * 0.54 : 0, 0, w * 0.46, h, "22% 22% 46% 46%", "box-shadow: inset 0 0 0 " + (w * 0.018) + "px var(--o-encre);");
      div(v, "p-part", "left:18%; top:16%; width:18%; height:60%; border-radius:30%; background: rgba(255,255,255,0.32); transform: skewX(-18deg);");
    });
    div(e, "p-part", "left:" + (w * 0.42) + "px; top:" + (h * 0.18) + "px; width:" + (w * 0.16) + "px; height:" + (h * 0.14) + "px; border-radius:6px; background: var(--o-encre);");
    return e;
  };

  // ================================================================ B2 : accessoires et objets sans visage
  // Damiano ne donne un visage qu'aux « coupables » ; le reste de son film, ce sont des objets qui agissent et
  // des accessoires posés sur les personnages. Tout se dessine ici, en code, aux couleurs de la vidéo.

  // Un casque de chantier (l'ouvrier), posé sur (cx, cy) = le milieu de son bord, largeur w.
  P.casque = function (parent, cx, cy, w, couleur) {
    var c = couleur || "citron", h = w * 0.62;
    var e = div(parent, "p-part", "left:" + (cx - w / 2) + "px; top:" + (cy - h) + "px; width:" + w + "px; height:" + h + "px;");
    P.mat(e, c, w * 0.12, 0, w * 0.76, h * 0.92, "50% 50% 12% 12% / 70% 70% 12% 12%");
    P.mat(e, c, w * 0.43, -h * 0.06, w * 0.14, h * 0.86, "8px", "background: var(--o-" + c + "-ombre); opacity: 0.55;");
    P.mat(e, c, 0, h * 0.8, w, h * 0.2, (h * 0.1) + "px", "background: linear-gradient(180deg, var(--o-" + c + ") 0%, var(--o-" + c + "-ombre) 100%);");
    return e;
  };

  // Une toile d'araignée dans un coin : des rayons et des fils en arc, à tisser (P.tisser).
  // (x, y) = le coin, s = la taille, sens = "hg" (le coin en haut à gauche), "hd", "bg", "bd".
  P.toile = function (parent, x, y, s, sens) {
    sens = sens || "hg";
    var sx = sens.charAt(1) === "d" ? -1 : 1, sy = sens.charAt(0) === "b" ? -1 : 1;
    var e = document.createElementNS(NS, "svg");
    e.setAttribute("viewBox", "0 0 " + s + " " + s);
    e.setAttribute("class", "p-toile");
    e.setAttribute("style", "position:absolute; left:" + (sx > 0 ? x : x - s) + "px; top:" + (sy > 0 ? y : y - s) + "px; width:" + s + "px; height:" + s + "px; overflow:visible;" + (sx < 0 || sy < 0 ? "transform: scale(" + sx + "," + sy + ");" : ""));
    var fils = [], angles = [0, 18, 36, 54, 72, 90];
    angles.forEach(function (a) {
      var r = a * Math.PI / 180;
      var l = document.createElementNS(NS, "path");
      l.setAttribute("d", "M0,0 L" + (Math.cos(r) * s).toFixed(1) + "," + (Math.sin(r) * s).toFixed(1));
      e.appendChild(l); fils.push(l);
    });
    [0.25, 0.45, 0.65, 0.85].forEach(function (k) {
      var d = "";
      angles.forEach(function (a, i) {
        var r = a * Math.PI / 180, R = k * s * (i % 2 ? 0.96 : 1);
        var px = (Math.cos(r) * R).toFixed(1), py = (Math.sin(r) * R).toFixed(1);
        if (i === 0) d += "M" + px + "," + py;
        else {
          var rm = (a - 9) * Math.PI / 180, Rm = R * 0.82;
          d += " Q" + (Math.cos(rm) * Rm).toFixed(1) + "," + (Math.sin(rm) * Rm).toFixed(1) + " " + px + "," + py;
        }
      });
      var l = document.createElementNS(NS, "path");
      l.setAttribute("d", d);
      e.appendChild(l); fils.push(l);
    });
    parent.appendChild(e);
    fils.forEach(function (f) { var L = f.getTotalLength ? f.getTotalLength() : s * 2; f.style.strokeDasharray = L; f.style.strokeDashoffset = L; f._L = L; });
    return { el: e, fils: fils };
  };
  // Elle se tisse de t à t + d : les rayons d'abord, puis les arcs.
  P.tisser = function (tl, toile, t, d) {
    var n = toile.fils.length;
    toile.fils.forEach(function (f, i) { tl.to(f, { strokeDashoffset: 0, duration: d / n * 2.2, ease: "power1.inOut" }, t + i * d / n * 0.8); });
  };

  // Une tasse de café (sans visage), base au milieu en (x, y), largeur s. Rend {el, vapeur: [3 fils]}.
  P.tasse = function (parent, x, y, s, couleur) {
    var c = couleur || "papier", h = s * 0.82;
    var e = div(parent, "p-part", "left:" + (x - s / 2) + "px; top:" + (y - h) + "px; width:" + s + "px; height:" + h + "px;");
    div(e, "p-part", "left:" + (s * 0.66) + "px; top:" + (h * 0.22) + "px; width:" + (s * 0.42) + "px; height:" + (h * 0.42) + "px; border-radius:50%; border:" + (s * 0.09) + "px solid var(--o-" + c + "-ombre); box-sizing:border-box;");
    P.mat(e, c, 0, 0, s * 0.84, h, "8% 8% 38% 38% / 6% 6% 30% 30%");
    div(e, "p-part", "left:" + (s * 0.05) + "px; top:" + (h * 0.03) + "px; width:" + (s * 0.74) + "px; height:" + (h * 0.12) + "px; border-radius:50%; background: radial-gradient(closest-side, var(--brand-sombre), var(--brand-sombre));");
    var v = [];
    for (var i = 0; i < 3; i++) {
      var sv = document.createElementNS(NS, "svg");
      sv.setAttribute("viewBox", "0 0 20 80");
      sv.setAttribute("style", "position:absolute; left:" + (s * (0.14 + i * 0.22)) + "px; top:" + (-h * 0.9) + "px; width:" + (s * 0.16) + "px; height:" + (h * 0.8) + "px; overflow:visible; opacity:0;");
      sv.innerHTML = '<path d="M10,78 Q2,62 10,48 Q18,34 10,20 Q4,10 10,2" fill="none" stroke="rgba(0,0,0,0.28)" stroke-width="4" stroke-linecap="round"/>';
      e.appendChild(sv); v.push(sv);
    }
    return { el: e, vapeur: v, h: h };
  };
  // La vapeur monte en boucle de debut à fin (des répétitions comptées).
  P.vapeur = function (tl, tasse, debut, fin) {
    var per = 1.1, nb = Math.max(1, Math.floor((fin - debut) / per));
    tasse.vapeur.forEach(function (v, i) {
      tl.fromTo(v, { opacity: 0, y: 10, scaleY: 0.7 }, { keyframes: [{ opacity: 1, y: -6, scaleY: 1, duration: per * 0.5, ease: "sine.out" }, { opacity: 0, y: -26, duration: per * 0.5, ease: "sine.in" }], repeat: nb - 1, immediateRender: false }, debut + i * per / 3);
    });
  };

  // Les « z » du sommeil : trois lettres qui montent en grossissant, de debut à fin.
  P.zzz = function (tl, parent, x, y, debut, fin, taille) {
    taille = taille || 70;
    var per = 1.2, nb = Math.max(1, Math.floor((fin - debut) / per));
    for (var i = 0; i < 3; i++) {
      var z = div(parent, "p-texte", "left:" + x + "px; top:" + y + "px; font-size:" + taille + "px; color: var(--o-nuit); opacity:0;", "z");
      tl.fromTo(z, { opacity: 0, x: 0, y: 0, scale: 0.5, rotation: -10 }, { keyframes: [{ opacity: 1, x: taille * 0.4, y: -taille * 0.7, scale: 0.8, rotation: 6, duration: per * 0.5, ease: "sine.out" }, { opacity: 0, x: taille * 0.9, y: -taille * 1.6, scale: 1.15, rotation: -8, duration: per * 0.5, ease: "sine.in" }], repeat: nb - 1, immediateRender: false }, debut + i * per / 3);
    }
  };

  // Un ticket de caisse : une bande de papier, des lignes grises (aucun chiffre : rien d'inventé), un bord dentelé.
  // (x, y) = le haut au milieu, w = la largeur, h = sa longueur totale. Rend {el (le cadre qui masque), bande}.
  P.ticket = function (parent, x, y, w, h, lignes) {
    var cadre = div(parent, "p-part", "left:" + (x - w / 2) + "px; top:" + y + "px; width:" + w + "px; height:0px; overflow:hidden;");
    var bande = div(cadre, "p-part p-ticket", "left:0; bottom:0; width:" + w + "px; height:" + h + "px;");
    var k = P.ticketLignes(bande, w, h, lignes);
    return { el: cadre, bande: bande, h: h, total: k };
  };
  P.ticketLignes = function (bande, w, h, lignes) {
    var rng = (window.K && K.rng) ? K.rng(7) : Math.random, yy = 40, total = null;
    var n = lignes || Math.floor((h - 160) / 46);
    for (var i = 0; i < n; i++) {
      var lw = (0.35 + rng() * 0.3) * w;
      div(bande, "p-part", "left:" + (w * 0.09) + "px; top:" + yy + "px; width:" + lw + "px; height:14px; border-radius:7px; background: var(--brand-gris-4);");
      div(bande, "p-part", "right:" + (w * 0.09) + "px; top:" + yy + "px; width:" + (w * 0.16) + "px; height:14px; border-radius:7px; background: var(--brand-gris-4);");
      yy += 46;
    }
    total = div(bande, "p-part", "left:" + (w * 0.09) + "px; right:" + (w * 0.09) + "px; top:" + (yy + 10) + "px; height:" + (w * 0.2) + "px; border-top: 6px dashed var(--brand-gris-3); padding-top: 14px; font-family: var(--brand-font-display); font-size:" + (w * 0.17) + "px; line-height:1; color: var(--o-rouge); text-align: right; letter-spacing: 0.04em;", "€€€€€");
    return total;
  };

  // Une pellicule (la vidéo) : bande sombre, perforations, n images. Rend {el, images: [divs]}.
  P.pellicule = function (parent, x, y, n, wImg, o) {
    o = o || {};
    var hImg = wImg * 0.5625, pad = wImg * 0.08, H = hImg + pad * 4.2, W = n * (wImg + pad) + pad;
    var e = div(parent, "p-part p-pellicule", "left:" + x + "px; top:" + y + "px; width:" + W + "px; height:" + H + "px;");
    var trous = function (top) {
      for (var i = 0; i < Math.floor(W / (pad * 1.6)); i++) div(e, "p-part", "left:" + (pad * 0.5 + i * pad * 1.6) + "px; top:" + top + "px; width:" + (pad * 0.8) + "px; height:" + (pad * 0.9) + "px; border-radius:" + (pad * 0.2) + "px; background: var(--o-papier-fond2); opacity:0.85;");
    };
    trous(pad * 0.45); trous(H - pad * 1.35);
    var images = [];
    for (var j = 0; j < n; j++) images.push(div(e, "p-part p-pellicule-img", "left:" + (pad + j * (wImg + pad)) + "px; top:" + (pad * 2.1) + "px; width:" + wImg + "px; height:" + hImg + "px;" + (o.imgStyle || "")));
    return { el: e, images: images, W: W, H: H, wImg: wImg, hImg: hImg };
  };

  // Une balance (sans visage) : socle, colonne, fléau, deux plateaux qui restent à plat.
  // (x, y) = le milieu du socle au sol ; l = la demi-longueur du fléau. p.incliner(tl, t, angle, d, ease).
  P.balance = function (parent, x, y, o) {
    o = o || {};
    var l = o.l || 430, haut = o.haut || 560, pend = o.pend || 230, wP = o.wPlateau || 400;
    var e = div(parent, "p-part", "left:" + x + "px; top:" + y + "px; width:0; height:0;");
    div(e, "p-ombre", "left:-260px; top:-26px; width:520px; height:70px;");
    P.mat(e, "nuit", -170, -60, 340, 60, "30px 30px 14px 14px");
    P.mat(e, "nuit", -24, -haut, 48, haut - 40, "20px");
    var pivot = div(e, "p-part", "left:0; top:" + (-haut) + "px; width:0; height:0;");
    var fleau = div(pivot, "p-part", "left:" + (-l - 20) + "px; top:-18px; width:" + (2 * l + 40) + "px; height:36px;");
    P.mat(fleau, "nuit", 0, 0, 2 * l + 40, 36, "18px");
    P.mat(pivot, "or", -34, -34, 68, 68, "50%");
    var plateaux = [-1, 1].map(function (cote) {
      var pl = div(e, "p-part", "left:0; top:0; width:0; height:0;");
      var fils = div(pl, "p-part", "left:" + (-wP * 0.36) + "px; top:0; width:" + (wP * 0.72) + "px; height:" + pend + "px; border-left: 5px solid var(--brand-gris-2); border-right: 5px solid var(--brand-gris-2); clip-path: polygon(50% 0, 100% 100%, 0 100%); background: linear-gradient(90deg, transparent calc(50% - 2px), var(--brand-gris-2) calc(50% - 2px), var(--brand-gris-2) calc(50% + 2px), transparent calc(50% + 2px));");
      var ligne = document.createElementNS(NS, "svg");
      ligne.setAttribute("viewBox", "0 0 100 100"); ligne.setAttribute("preserveAspectRatio", "none");
      ligne.setAttribute("style", "position:absolute; left:" + (-wP * 0.4) + "px; top:0; width:" + (wP * 0.8) + "px; height:" + pend + "px; overflow:visible;");
      ligne.innerHTML = '<path d="M50,0 L0,100 M50,0 L100,100" stroke="var(--brand-gris-2)" stroke-width="1.2" vector-effect="non-scaling-stroke" style="stroke-width:5px"/>';
      fils.remove(); pl.appendChild(ligne);
      var plat = P.mat(pl, "or", -wP / 2, pend - 10, wP, 44, "10px 10px 50% 50% / 10px 10px 100% 100%");
      var dessus = div(pl, "p-part", "left:0; top:" + (pend - 10) + "px; width:0; height:0;");
      return { el: pl, cote: cote, dessus: dessus };
    });
    var etat = { a: 0 };
    function placer() {
      var r = etat.a * Math.PI / 180;
      gsap.set(fleau, { rotation: etat.a, transformOrigin: "50% 50%" });
      plateaux.forEach(function (pq) {
        gsap.set(pq.el, { x: pq.cote * l * Math.cos(r), y: -haut + pq.cote * l * Math.sin(r) });
      });
    }
    placer();
    var b = { el: e, plateaux: plateaux, etat: etat, haut: haut, pend: pend, l: l };
    b.incliner = function (tl, t, angle, d, ease) {
      tl.to(etat, { a: angle, duration: d || 0.5, ease: ease || "elastic.out(1, 0.45)", onUpdate: placer }, t);
    };
    b.placer = placer;
    return b;
  };

  // Une gerbe d'étincelles (des étoiles à quatre branches), autour de (x, y), à l'instant t.
  P.etincelles = function (tl, parent, x, y, t, o) {
    o = o || {};
    var n = o.nombre || 6, R = o.rayon || 150, c = P.role(o.couleur || "citron"), s = o.taille || 44;
    for (var i = 0; i < n; i++) {
      var a = (i / n) * Math.PI * 2 + (o.angle || 0.3);
      var e = div(parent, "p-part", "left:" + (x - s / 2) + "px; top:" + (y - s / 2) + "px; width:" + s + "px; height:" + s + "px;");
      e.innerHTML = '<svg viewBox="-10 -10 20 20" style="width:100%; height:100%; overflow:visible;"><path d="M0,-10 Q1.4,-1.4 10,0 Q1.4,1.4 0,10 Q-1.4,1.4 -10,0 Q-1.4,-1.4 0,-10Z" fill="var(--o-' + c + ')" stroke="var(--o-nuit)" stroke-width="1.2"/></svg>';
      gsap.set(e, { scale: 0, opacity: 0 });
      var k = (i % 2 ? 0.75 : 1);
      tl.fromTo(e, { scale: 0, opacity: 1, x: 0, y: 0, rotation: 0 }, { scale: k, x: Math.cos(a) * R * k, y: Math.sin(a) * R * k, rotation: 90, duration: 0.35, ease: "power3.out", immediateRender: false }, t)
        .to(e, { scale: 0, opacity: 0, duration: 0.25, ease: "power2.in" }, t + 0.35);
    }
  };

  // Une pile de pièces (sans visage), base au milieu en (x, y), n pièces de largeur s.
  P.pile = function (parent, x, y, n, s) {
    var e = div(parent, "p-part", "left:" + (x - s / 2) + "px; top:" + (y - n * s * 0.16 - s * 0.3) + "px; width:" + s + "px; height:" + (n * s * 0.16 + s * 0.3) + "px;");
    for (var i = 0; i < n; i++) {
      P.mat(e, "or", (i % 2 ? 4 : -3), (n - 1 - i) * s * 0.16, s, s * 0.3, "50%", "box-shadow: inset 0 -" + (s * 0.06) + "px 0 var(--o-or-ombre), 0 2px 0 var(--o-or-ombre);");
    }
    return e;
  };

  // La caméra du banc B2 : amène le point (wx, wy) du monde au point (fx, fy) du cadre, à l'échelle s.
  // Le monde a son origine en haut à gauche (transform-origin 0 0). Rend {x, y, scale}, pour gsap.
  P.vue = function (s, wx, wy, fx, fy) { return { scale: s, x: (fx == null ? 960 : fx) - wx * s, y: (fy == null ? 540 : fy) - wy * s }; };
  // Un mouvement de caméra de t à t + d vers une vue (P.vue).
  P.cam = function (tl, monde, t, d, vue, ease) { tl.to(monde, Object.assign({ duration: d, ease: ease || "power2.inOut" }, vue), t); };
  // B3 (13/11/2026) : les coups de zoom (« boum boum ») sur les mots forts, la signature du style : toute la scène
  // grossit d'un coup (0,06 s) puis revient (0,3 s), d'un côté puis de l'autre. liste : [[t, force, origine], …].
  // Deux coups à 0,36 s d'écart au moins (le premier doit être revenu à 1 avant que l'origine change).
  P.coups = function (tl, el, liste) {
    liste.forEach(function (c) {
      tl.to(el, { scale: 1 + (c[1] || 0.03), duration: 0.06, ease: "power2.out", transformOrigin: c[2] || "50% 50%" }, c[0])
        .to(el, { scale: 1, duration: 0.3, ease: "power2.out" }, c[0] + 0.06);
    });
  };
  // B4 (13/11/2026, Alexandre : « trop de petits objets avec une bouche et des yeux, ça fait enfantin ») : un objet sans
  // visage. Le visage reste construit (ses gestes ne cassent rien) mais ne se voit plus ; la loupe perd son œil.
  P.sansVisage = function (p) {
    if (p && p.visage && p.visage.el) p.visage.el.style.display = "none";
    if (p && p.globe) p.globe.style.display = "none";
    if (p && p.sourcil) p.sourcil.style.display = "none";
    return p;
  };
})();
