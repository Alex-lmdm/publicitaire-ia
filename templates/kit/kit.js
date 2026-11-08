/* Kit de motion design : les briques d'un motion design produit, communes aux scènes (chargé dans
   index.html après GSAP). Tout est déterministe : aucune horloge, aléatoire à graine, chaque état
   se calcule à partir du temps de la scène. Chaque fonction ajoute ses mouvements à la timeline
   donnée. Mode d'emploi : skill `studio`, references/kit.md.

   Règle d'or des états de départ : un élément caché au début se cache par gsap.set (ou K.cacher)
   à la construction, jamais par tl.set(…, 0) : un set à 0 ne s'applique pas sur la toute
   première image, qui montrerait l'élément une fraction de seconde. */
(function () {
  var K = (window.K = window.K || {});
  var NS = "http://www.w3.org/2000/svg";

  // Chaque appel rend ses propres identifiants (dégradés, masques d'un logo) : le même logo posé deux
  // fois ne partage plus ses `id`, sinon la seconde copie disparaît (essai du 06/11/2026, style 7).
  var copiesIc = 0;
  K.ic = function (nom) {
    var svg = (window.K_ICONES || {})[nom] || "";
    if (svg.indexOf('id="') < 0) return svg;
    var n = ++copiesIc, ids = [];
    svg.replace(/\sid="([^"]+)"/g, function (m, id) { ids.push(id); return m; });
    ids.forEach(function (id) {
      var neuf = id + "-k" + n;
      svg = svg.split('id="' + id + '"').join('id="' + neuf + '"')
        .split("url(#" + id + ")").join("url(#" + neuf + ")")
        .split('href="#' + id + '"').join('href="#' + neuf + '"');
    });
    return svg;
  };
  // Cache dès la construction (première image comprise) ; un tween ou un set les montre ensuite.
  K.cacher = function (cible, vars) { gsap.set(cible, Object.assign({ opacity: 0 }, vars || {})); };

  // Aléatoire à graine : la même graine donne toujours la même suite.
  K.rng = function (graine) {
    var s = (graine >>> 0) || 1;
    return function () { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; };
  };
  K.entre = function (a, b, p) { return a + (b - a) * p; };

  // Taille de la composition qui contient `el` : data-width / data-height de la racine
  // [data-composition-id] la plus proche qui les porte (1080 × 1920 pour un Reel ou une story,
  // 1920 × 1080 en 16:9). Lue dans le HTML, jamais mesurée à l'écran : le même résultat à chaque
  // image, dans l'aperçu comme au rendu. Sans racine trouvée : la composition principale, sinon
  // 1920 × 1080 (l'ancien défaut du kit).
  K.cadre = function (el) {
    var lire = function (n) {
      var l = parseFloat(n.getAttribute("data-width")), h = parseFloat(n.getAttribute("data-height"));
      return l > 0 && h > 0 ? { largeur: l, hauteur: h } : null;
    };
    var n = el && el.closest ? el.closest("[data-composition-id]") : null, c;
    while (n) {
      if ((c = lire(n))) return c;
      n = n.parentElement ? n.parentElement.closest("[data-composition-id]") : null;
    }
    var racine = document.querySelector("[data-composition-id][data-width][data-height]");
    return (racine && lire(racine)) || { largeur: 1920, hauteur: 1080 };
  };

  // La durée donnée à une scène : celle de sa racine, ou, une fois montée, celle de son hôte dans
  // index.html (HyperFrames retire data-duration de la racine intérieure au montage). 0 si aucune.
  K.duree = function (el) {
    for (var n = el; n && n.getAttribute; n = n.parentElement) {
      var d = parseFloat(n.getAttribute("data-duration"));
      if (d > 0) return d;
    }
    return 0;
  };

  // La valeur d'un jeton de la marque (`--brand-gris-2`), pour un tween de couleur : GSAP
  // n'interpole pas une variable CSS.
  K.jeton = function (nom) {
    return window.getComputedStyle ? getComputedStyle(document.documentElement).getPropertyValue(nom).trim() : "";
  };

  K.el = function (parent, tag, classe, html, style) {
    var e = document.createElement(tag || "div");
    if (classe) e.className = classe;
    if (html != null) e.innerHTML = html;
    if (style) e.setAttribute("style", style);
    if (parent) parent.appendChild(e);
    return e;
  };

  // --- Textes qui dépendent du temps (frappe, compteurs) --------------------------------
  // Un seul tween de 0 à la fin de la scène ; onUpdate rend l'état du temps courant.
  K.texteSelon = function (tl, el, dureeScene, fn) {
    var o = { t: 0 };
    var rendre = function () { var v = fn(o.t); if (el.textContent !== v) el.textContent = v; };
    tl.to(o, { t: dureeScene, duration: dureeScene, ease: "none", onUpdate: rendre }, 0);
    el.textContent = fn(0);
  };
  // Frappe au clavier : par petits groupes de lettres, irréguliers mais fixes.
  K.taper = function (tl, el, texte, debut, fin, dureeScene) {
    var r = K.rng(texte.length * 7919 + 13), paliers = [0], n = 0;
    while (n < texte.length) { n = Math.min(texte.length, n + 1 + Math.floor(r() * 3)); paliers.push(n); }
    K.texteSelon(tl, el, dureeScene, function (t) {
      if (t < debut) return "";
      if (t >= fin) return texte;
      var i = Math.floor(((t - debut) / (fin - debut)) * (paliers.length - 1));
      return texte.slice(0, paliers[i]);
    });
  };
  // Compteur : de → à, avec une courbe GSAP et un format libre.
  K.compteur = function (tl, el, de, a, debut, duree, dureeScene, format, courbe) {
    var ease = gsap.parseEase(courbe || "expo.out");
    format = format || function (v) { return String(Math.round(v)); };
    K.texteSelon(tl, el, dureeScene, function (t) {
      var p = t <= debut ? 0 : t >= debut + duree ? 1 : ease((t - debut) / duree);
      return format(de + (a - de) * p);
    });
  };

  // --- Mots qui entrent et sortent ------------------------------------------------------
  K.entreeMots = function (tl, cible, t, o) {
    o = o || {};
    tl.fromTo(cible,
      { y: o.y != null ? o.y : 46, opacity: 0, filter: "blur(" + (o.flou != null ? o.flou : 14) + "px)", scale: o.echelle || 0.94 },
      { y: 0, opacity: 1, filter: "blur(0px)", scale: 1, duration: o.duree || 0.55, ease: o.ease || "expo.out", stagger: o.decalage != null ? o.decalage : 0.07 }, t);
  };
  K.sortieMots = function (tl, cible, t, o) {
    o = o || {};
    tl.to(cible, { y: o.y != null ? o.y : -34, opacity: 0, filter: "blur(" + (o.flou != null ? o.flou : 12) + "px)", duration: o.duree || 0.28, ease: o.ease || "power2.in", stagger: o.decalage != null ? o.decalage : 0.03 }, t);
  };

  // --- Le curseur -------------------------------------------------------------------------
  K.curseur = function (parent, id, clair) {
    var e = K.el(parent, "div", "k-curseur");
    e.id = id;
    var remplissage = clair ? "#ffffff" : "#111111", trait = clair ? "#111111" : "#ffffff";
    e.innerHTML =
      '<div class="k-onde"></div>' +
      '<svg viewBox="0 0 32 32"><path d="M6.5 3.5 L6.5 25.5 L12.2 20.3 L15.9 28.6 L19.6 27 L16 18.9 L23.8 18.9 Z" fill="' + remplissage +
      '" stroke="' + trait + '" stroke-width="1.9" stroke-linejoin="round"/></svg>';
    return e;
  };
  // Trajet : [[t, x, y, durée, courbe], …] ; le premier point place le curseur.
  K.trajet = function (tl, el, points) {
    points.forEach(function (p, i) {
      if (i === 0) { if (p[0] === 0) gsap.set(el, { x: p[1], y: p[2] }); else tl.set(el, { x: p[1], y: p[2] }, p[0]); }
      else tl.to(el, { x: p[1], y: p[2], duration: p[3] || 0.55, ease: p[4] || "power3.inOut" }, p[0]);
    });
  };
  K.clic = function (tl, el, t) {
    var svg = el.querySelector("svg"), onde = el.querySelector(".k-onde");
    tl.to(svg, { scale: 0.8, duration: 0.07, ease: "power2.out" }, t)
      .to(svg, { scale: 1, duration: 0.22, ease: "back.out(3)" }, t + 0.07)
      .fromTo(onde, { scale: 0.25, opacity: 0.95 }, { scale: 1.5, opacity: 0, duration: 0.5, ease: "power2.out" }, t);
  };

  // --- Les objets flottants ---------------------------------------------------------------
  // Un champ d'objets répartis en profondeur : les plus proches et les plus lointains sont
  // flous (profondeur de champ), ceux du milieu sont nets. Retourne les éléments créés.
  // Sans `zone`, les objets se répartissent sur tout le cadre de la composition (K.cadre).
  K.champ = function (parent, o) {
    var r = K.rng(o.graine || 1), els = [];
    var cadre = o.zone ? null : K.cadre(parent);
    var z = o.zone || { x0: 0, y0: 0, x1: cadre.largeur, y1: cadre.hauteur };
    var evite = o.evite; // { x0, y0, x1, y1 } : zone centrale à laisser libre
    var n = o.nombre || 14, fabriques = o.objets;
    for (var i = 0; i < n; i++) {
      var prof = (i + r() * 0.9) / n; // 0 = tout près, 1 = au loin, réparti
      var x, y, essais = 0;
      do {
        x = K.entre(z.x0, z.x1, r()); y = K.entre(z.y0, z.y1, r()); essais++;
      } while (evite && essais < 30 && x > evite.x0 && x < evite.x1 && y > evite.y0 && y < evite.y1);
      var taille = K.entre(o.tailleMax || 150, o.tailleMin || 54, prof);
      // Un flou demandé à 0 vaut 0 (pas le défaut) : des logos qu'on doit reconnaître restent nets.
      var flou = prof > 0.62 ? (prof - 0.62) * (o.flouLoin != null ? o.flouLoin : 16) : prof < 0.14 ? (0.14 - prof) * (o.flouPres != null ? o.flouPres : 70) : 0;
      var e = fabriques[i % fabriques.length](taille, i, r);
      e.style.left = (x - taille / 2) + "px";
      e.style.top = (y - taille / 2) + "px";
      e.style.filter = "blur(" + flou.toFixed(1) + "px)";
      e.style.opacity = String(K.entre(1, o.opaciteLoin != null ? o.opaciteLoin : 0.55, prof));
      e.style.zIndex = String(100 - Math.round(prof * 100));
      e.dataset.prof = prof.toFixed(3);
      e.dataset.rot = ((r() - 0.5) * 2 * (o.rotation != null ? o.rotation : 14)).toFixed(1);
      e.dataset.ph = r().toFixed(3);
      parent.appendChild(e);
      els.push(e);
    }
    return els;
  };
  K.tuile = function (classe, contenu) {
    return function (taille) {
      var e = document.createElement("div");
      e.className = "k-tuile " + (typeof classe === "function" ? classe() : classe);
      e.style.width = e.style.height = taille + "px";
      e.innerHTML = contenu;
      return e;
    };
  };
  // Tuile d'un vrai logo, dans les vraies couleurs de la marque (fond, encre du logo). Les objets
  // flottants sont des logos d'outils ou des objets du sujet, jamais des icônes génériques.
  K.tuileMarque = function (fond, encre, svg, bord) {
    return function (taille) {
      var e = document.createElement("div");
      e.className = "k-tuile k-tuile-marque";
      e.style.width = e.style.height = taille + "px";
      e.style.background = fond;
      e.style.color = encre;
      if (bord) e.style.boxShadow = "inset 0 0 0 2px " + bord + ", 0 18px 40px rgba(0,0,0,.35)";
      e.innerHTML = svg;
      return e;
    };
  };
  // Un vrai logo NU, pour K.champ : le logo seul, sans tuile ni fond, dans ses couleurs (un logo
  // monochrome prend `couleur`, sinon celle du texte). Une ombre douce le détache du fond.
  K.logoNu = function (svg, couleur) {
    return function (taille) {
      var e = document.createElement("div");
      e.className = "k-logo-nu";
      e.style.width = e.style.height = taille + "px";
      if (couleur) e.style.color = couleur;
      e.innerHTML = svg;
      return e;
    };
  };
  // --- Les objets connus, dans leurs vraies couleurs (image.md, « Les objets connus ») ----------
  // La barre d'état d'un iPhone dans l'écran du téléphone (`k-tel-ecran`) : l'heure, le réseau, le
  // Wi-Fi, la batterie. `clair` : blanche, sur un écran sombre (le défaut) ; false : noire.
  K.statut = function (ecran, o) {
    o = o || {};
    var encre = o.clair === false ? "#000000" : "#ffffff";
    var barre = K.el(ecran, "div", "k-statut", null, "color:" + encre + ";");
    K.el(barre, "span", "k-statut-heure").textContent = o.heure || "9:41";
    K.el(barre, "span", "k-statut-icones",
      '<svg viewBox="0 0 18 12" width="34" height="22"><rect x="0" y="8" width="3" height="4" rx="1" fill="currentColor"/>' +
      '<rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="currentColor"/><rect x="10" y="3" width="3" height="9" rx="1" fill="currentColor"/>' +
      '<rect x="15" y="0" width="3" height="12" rx="1" fill="currentColor"/></svg>' +
      '<svg viewBox="0 0 16 12" width="30" height="22"><path d="M8 11.5l2.4-3a3.5 3.5 0 0 0-4.8 0z" fill="currentColor"/>' +
      '<path d="M3.2 6.3a7 7 0 0 1 9.6 0M.6 3.4a10.8 10.8 0 0 1 14.8 0" stroke="currentColor" stroke-width="1.7" fill="none" stroke-linecap="round"/></svg>' +
      '<svg viewBox="0 0 27 13" width="50" height="24"><rect x="0.8" y="0.8" width="22.4" height="11.4" rx="3.6" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.4" fill="none"/>' +
      '<rect x="2.6" y="2.6" width="18.8" height="7.8" rx="2.2" fill="currentColor"/><path d="M24.8 4.6v3.8a2 2 0 0 0 0-3.8z" fill="currentColor" fill-opacity="0.45"/></svg>');
    return barre;
  };
  // Une notification d'iPhone : l'icône de l'app (un vrai logo : K.ic("logo-stripe")), son nom, l'instant,
  // un titre et un texte. o = {icone, app, quand, titre, texte, sombre, largeur} ; rend l'élément, à placer
  // (left, top) et à animer. Ses mots se lisent : titre 34 px, texte 32 px, en-tête 28 px.
  K.notification = function (parent, o) {
    o = o || {};
    var n = K.el(parent, "div", "k-notif" + (o.sombre ? " k-notif-sombre" : ""), null,
      "width:" + (o.largeur || 860) + "px;");
    K.el(n, "div", "k-notif-icone", o.icone || "");
    var corps = K.el(n, "div", "k-notif-corps");
    var tete = K.el(corps, "div", "k-notif-tete");
    K.el(tete, "span").textContent = o.app || "";
    K.el(tete, "span").textContent = o.quand || "maintenant";
    if (o.titre) K.el(corps, "div", "k-notif-titre").textContent = o.titre;
    if (o.texte) K.el(corps, "div", "k-notif-texte").textContent = o.texte;
    return n;
  };
  // Une bulle de messagerie : "bleue" (le message envoyé d'un iPhone), "grise" (le message reçu),
  // "whatsapp" (le vert clair d'un message WhatsApp envoyé). Rend l'élément, à placer et à animer.
  K.bulle = function (parent, texte, genre) {
    var b = K.el(parent, "div", "k-bulle k-bulle-" + (genre || "grise"));
    b.textContent = texte;
    return b;
  };
  // Un ordinateur portable en perspective, comme le téléphone (k-tel) : un couvercle qui pivote sur sa
  // charnière, son écran qui porte sa vraie capture, une base en alu avec son clavier touche par touche
  // et son pavé tactile. À poser dans la caméra (k-camera) d'un k-scene3d, que l'on incline pour voir la
  // base. o = { largeur (px, 1100), capture (chemin d'image), ouvert (0 fermé à 1 ouvert, 1), teinte
  // ("argent" ou "gris") }. Rend { racine, couvercle, ecran, image, base } : on anime `couvercle`
  // (rotationX : -86 fermé, 12 ouvert), `racine` (x, y, rotationY…) et `image` (y : la page défile).
  K.ordinateur = function (parent, o) {
    o = o || {};
    var L = o.largeur || 1100, H = Math.round(L * 0.66), P = Math.round(L * 0.68);
    var r = K.el(parent, "div", "k-ordi" + (o.teinte === "gris" ? " k-ordi-gris" : ""), null,
      "width:" + L + "px; height:" + H + "px;");
    var base = K.el(r, "div", "k-ordi-base", null, "height:" + P + "px;");
    base.setAttribute("data-layout-allow-overflow", "");   // couchée en 3D sous le couvercle : voulu, pas un débordement
    K.el(base, "div", "k-ordi-ombre");
    K.el(base, "div", "k-ordi-charniere");
    var clavier = K.el(base, "div", "k-ordi-clavier");
    // Les rangs d'un clavier de portable, en largeur de touche (1 = une lettre) ; les flèches en demi-touches.
    var rangs = [[0.55, [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5]],
      [1, [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [1, [1.8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.7]],
      [1, [2.3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2.2]], [1, [1, 1, 1, 1.25, 5, 1.25, 1, "fleches"]]];
    var pas = 100 / 14.5, haut = 100 / 5.55, y = 0, jeu = Math.max(1, Math.round(L * 0.0028));
    var touche = function (x, yy, l, h) {
      K.el(clavier, "i", "k-ordi-touche", null, "left:" + x + "%; top:" + yy + "%; width:" + (l * pas) + "%; height:" + h + "%; border-width:" + jeu + "px;");
    };
    rangs.forEach(function (rang) {
      var h = rang[0] * haut, x = 0;
      rang[1].forEach(function (l) {
        if (l === "fleches") {
          touche(x, y + h / 2, 1, h / 2); touche(x + pas, y, 1, h / 2); touche(x + pas, y + h / 2, 1, h / 2); touche(x + 2 * pas, y + h / 2, 1, h / 2);
          x += 3 * pas;
        } else { touche(x, y, l, h); x += l * pas; }
      });
      y += h;
    });
    K.el(base, "div", "k-ordi-pave");
    K.el(base, "div", "k-ordi-tranche");
    var couvercle = K.el(r, "div", "k-ordi-couvercle");
    K.el(couvercle, "div", "k-ordi-dos");
    var cadre = K.el(couvercle, "div", "k-ordi-cadre");
    var ecran = K.el(cadre, "div", "k-ordi-ecran"), image = null;
    if (o.capture) {                                      // une capture longue défile sous le cadre de l'écran : voulu
      image = K.el(ecran, "img"); image.src = o.capture; image.alt = ""; image.setAttribute("data-layout-allow-overflow", "");
    }
    K.el(cadre, "i", "k-ordi-camera");
    gsap.set(couvercle, { rotationX: -86 + 98 * (o.ouvert == null ? 1 : o.ouvert) });
    return { racine: r, couvercle: couvercle, ecran: ecran, image: image, base: base };
  };
  // Dérive lente et continue (parallaxe : le proche bouge plus que le lointain). Finie.
  K.derive = function (tl, els, debut, duree, amplitude) {
    amplitude = amplitude || 60;
    els.forEach(function (e) {
      var prof = parseFloat(e.dataset.prof), ph = parseFloat(e.dataset.ph), rot = parseFloat(e.dataset.rot);
      var a = amplitude * (1.25 - prof);
      tl.fromTo(e, { x: -a * Math.cos(ph * 6.28), y: -a * 0.6 * Math.sin(ph * 6.28), rotation: rot },
        { x: a * Math.cos(ph * 6.28), y: a * 0.6 * Math.sin(ph * 6.28), rotation: rot * 0.4, duration: duree, ease: "sine.inOut" }, debut);
    });
  };
  // Arrivée des objets depuis la profondeur, en rafale.
  K.arrivee = function (tl, els, t, o) {
    o = o || {};
    els.forEach(function (e, i) {
      var prof = parseFloat(e.dataset.prof);
      tl.fromTo(e, { scale: 0, opacity: 0 }, { scale: 1, opacity: parseFloat(e.style.opacity), duration: o.duree || 0.6, ease: o.ease || "back.out(1.6)" },
        t + (o.ordre === "prof" ? prof : i / els.length) * (o.etalement || 0.6));
    });
  };

  // --- Flash de couleur depuis un point (clic) -------------------------------------------
  K.flash = function (tl, el, x, y, t, duree) {
    gsap.set(el, { x: x, y: y, scale: 0 });
    tl.to(el, { scale: 24, duration: duree || 0.6, ease: "expo.inOut" }, t);
  };

  // --- Chapitre : mot fantôme, étiquette, interrupteur cliqué -----------------------------
  // racine contient .k-fantome, .k-etiquette (des .k-mot), .k-interrupteur (.k-plein, .k-bille).
  // Les positions se calculent sur la taille de la composition (K.cadre) : le même appel marche
  // en 9:16 et en 16:9. o.depart = [x, y] du curseur au début ; o.cible = [x, y] où il clique,
  // seulement si l'interrupteur a été déplacé par le CSS de la scène.
  K.chapitre = function (tl, racine, curseur, t, o) {
    o = o || {};
    var fantome = racine.querySelector(".k-fantome"), mots = racine.querySelectorAll(".k-etiquette .k-mot"),
      inter = racine.querySelector(".k-interrupteur"), plein = inter.querySelector(".k-plein"), bille = inter.querySelector(".k-bille");
    var cadre = K.cadre(racine), L = cadre.largeur, H = cadre.hauteur, echelle = L / 1920;
    // Le fantôme est un décor presque invisible voulu : hors des audits de lisibilité de `check`.
    if (fantome) fantome.setAttribute("data-layout-ignore", "");
    gsap.set(plein, { scaleX: 0 });
    tl.fromTo(fantome, { x: 260 * echelle, opacity: 0 }, { x: -60 * echelle, opacity: 1, duration: 2.4, ease: "power2.out" }, t);
    K.entreeMots(tl, mots, t + 0.1, { decalage: 0.06 });
    tl.fromTo(inter, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2)" }, t + 0.3);
    // L'interrupteur est centré en largeur, 96 px sous le milieu (kit.css) : la pointe du curseur
    // tombe sur sa moitié droite, là où la bille arrive.
    var cx = o.cible ? o.cible[0] : L / 2 + 18, cy = o.cible ? o.cible[1] : H / 2 + 122;
    var dx = o.depart ? o.depart[0] : (L * 1500) / 1920, dy = o.depart ? o.depart[1] : (H * 1000) / 1080;
    K.trajet(tl, curseur, [[0, dx, dy], [t + 0.35, cx, cy, 0.55, "power3.out"]]);
    K.clic(tl, curseur, t + 0.95);
    tl.to(bille, { x: 40, duration: 0.3, ease: "power3.inOut" }, t + 0.98);
    tl.to(plein, { scaleX: 1, duration: 0.3, ease: "power3.inOut" }, t + 0.98);
    return t + 1.35; // moment où la plongée vers la démo peut partir
  };

  // --- Le mot qui joue : il fait ce qu'il dit --------------------------------------------
  // Relevé sur les vidéos de Higgsfield Katana (06/11/2026) : peu de mots, très grands, et chacun
  // agit (il claque, s'étire, se barre, se surligne). Un geste part d'un mot déjà lisible et le
  // laisse lisible ; aucun mot ne tremble ni ne glisse sans raison.
  var liste = function (cible) {
    if (!cible) return [];
    if (typeof cible === "string") return Array.prototype.slice.call(document.querySelectorAll(cible));
    if (cible.length != null && !cible.nodeType) return Array.prototype.slice.call(cible);
    return [cible];
  };

  // Découpe le texte d'un élément en lettres (span.k-lettre), espaces gardés ; rend les lettres.
  K.lettres = function (el) {
    var texte = el.textContent, lettres = [];
    el.textContent = "";
    for (var i = 0; i < texte.length; i++) {
      if (texte[i] === " ") { el.appendChild(document.createTextNode(" ")); continue; }
      var s = K.el(el, "span", "k-lettre");
      s.textContent = texte[i];
      lettres.push(s);
    }
    return lettres;
  };

  // Le claquement : le mot arrive d'un coup, plein (aucun fondu : rien ne vire à l'olive sur
  // l'accent), plus grand, et se pose. `decalage` pour une rafale de mots ou de lettres.
  K.claque = function (tl, cible, t, o) {
    o = o || {};
    liste(cible).forEach(function (e, i) {
      var ti = t + i * (o.decalage || 0);
      if (ti > 0) { K.cacher(e); tl.set(e, { opacity: 1 }, ti); }
      tl.fromTo(e, { scale: o.de || 1.45, y: o.y || 0, rotation: o.rotation || 0 },
        { scale: 1, y: 0, rotation: 0, duration: o.duree || 0.42, ease: o.ease || "expo.out" }, ti);
    });
  };

  // L'étirement : le mot (ou ses lettres) s'étire puis revient. axe "y" (défaut) ou "x".
  K.etire = function (tl, cible, t, o) {
    o = o || {};
    var axe = o.axe === "x" ? "scaleX" : "scaleY";
    liste(cible).forEach(function (e, i) {
      var ti = t + i * (o.decalage || 0), aller = {}, retour = {};
      gsap.set(e, { transformOrigin: o.origine || (axe === "scaleY" ? "50% 100%" : "0% 50%") });
      aller[axe] = o.facteur || 1.7;
      retour[axe] = 1;
      tl.to(e, Object.assign({ duration: o.duree || 0.35, ease: "power3.out" }, aller), ti);
      if (o.retour !== false) tl.to(e, Object.assign({ duration: 0.5, ease: "expo.out" }, retour), ti + (o.tenue || 0.6));
    });
  };

  // La barre : un trait plein de l'accent raye le mot (« ni filmée »), qui peut ensuite s'éteindre
  // (`eteindre` : la couleur qu'il prend, un gris de la marque).
  K.barre = function (tl, el, t, o) {
    o = o || {};
    // Un élément déjà placé (absolu) le reste : seul un élément statique devient le repère de la barre.
    if (window.getComputedStyle && getComputedStyle(el).position === "static") el.style.position = "relative";
    var b = K.el(el, "span", "k-barre");
    gsap.set(b, { scaleX: 0, rotation: o.angle != null ? o.angle : -3 });
    tl.to(b, { scaleX: 1, duration: o.duree || 0.26, ease: "power3.inOut" }, t);
    if (o.eteindre) tl.to(el, { color: o.eteindre, duration: 0.2, ease: "power1.out" }, t + 0.16);
    return b;
  };

  // Le surlignage : un bloc plein de l'accent (ou de `couleur`) s'ouvre derrière le mot, de gauche
  // à droite ; `encre` change la couleur du mot au passage.
  K.surligner = function (tl, el, t, o) {
    o = o || {};
    el.classList.add("k-surligne");
    // le bloc derrière, le texte devant (dans son propre span) : aucun z-index négatif
    var s = K.el(null, "span", "k-surlignage"), texte = K.el(null, "span", "k-surligne-texte");
    if (o.couleur) s.style.background = o.couleur;
    while (el.firstChild) texte.appendChild(el.firstChild);
    el.appendChild(s);
    el.appendChild(texte);
    gsap.set(s, { scaleX: 0 });
    tl.to(s, { scaleX: 1, duration: o.duree || 0.3, ease: "power3.inOut" }, t);
    if (o.encre) tl.to(el, { color: o.encre, duration: 0.1, ease: "none" }, t + 0.12);
    return s;
  };

  // Le volet : des blocs (étiquettes de fonction, pastilles pleines) s'ouvrent depuis leur bord,
  // en rafale ; jamais un bloc de l'accent qui entre en fondu.
  K.volet = function (tl, cible, t, o) {
    o = o || {};
    liste(cible).forEach(function (e, i) {
      gsap.set(e, { scaleX: 0, transformOrigin: o.origine || "0% 50%" });
      tl.to(e, { scaleX: 1, duration: o.duree || 0.32, ease: o.ease || "power3.out" }, t + i * (o.decalage != null ? o.decalage : 0.09));
    });
  };

  // --- Le schéma qui se trace et le fil rouge ---------------------------------------------
  // Un lien courbe entre deux points [x, y] de la composition (SVG `k-liens` posé sur `parent`,
  // aux pixels de la composition) ; `o.svg` pour en ajouter au même dessin. Rend le chemin.
  K.lien = function (parent, a, b, o) {
    o = o || {};
    var svg = o.svg;
    if (!svg) {
      var c = o.taille || K.cadre(parent);
      svg = document.createElementNS(NS, "svg");
      svg.setAttribute("class", "k-liens");
      svg.setAttribute("viewBox", "0 0 " + c.largeur + " " + c.hauteur);
      svg.setAttribute("width", String(c.largeur));
      svg.setAttribute("height", String(c.hauteur));
      parent.appendChild(svg);
    }
    var courbe = o.courbe != null ? o.courbe : 0.25;
    var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1];
    var p = document.createElementNS(NS, "path");
    p.setAttribute("d", "M" + a[0] + " " + a[1] + " Q" + (mx - dy * courbe) + " " + (my + dx * courbe) + " " + b[0] + " " + b[1]);
    p.setAttribute("class", "k-lien" + (o.classe ? " " + o.classe : ""));
    svg.appendChild(p);
    return p;
  };
  // Trace un trait SVG (un lien, un arc, un soulignement) de son début à sa fin.
  K.trace = function (tl, chemin, t, duree, o) {
    o = o || {};
    var L = chemin.getTotalLength ? chemin.getTotalLength() : o.longueur || 1000;
    gsap.set(chemin, { strokeDasharray: L + " " + L, strokeDashoffset: L });
    tl.to(chemin, { strokeDashoffset: 0, duration: duree || 0.5, ease: o.ease || "power2.inOut" }, t);
    return L;
  };
  // Le fil rouge suit un trait : `el` (un `k-fil`, une pastille) va de `o.de` à `o.a` (0 à 1) de sa
  // longueur. Avec la même durée et la même courbe que K.trace, il en dessine la pointe. Calculé à
  // chaque image d'après le temps de la scène (`D`) : `el` ne prend aucun autre mouvement x / y.
  K.longer = function (tl, el, chemin, t, duree, D, o) {
    o = o || {};
    var L = chemin.getTotalLength(), de = o.de || 0, a = o.a != null ? o.a : 1;
    var ease = gsap.parseEase(o.ease || "power2.inOut"), etat = { t: 0 };
    var placer = function () {
      var q = etat.t <= t ? 0 : etat.t >= t + duree ? 1 : ease((etat.t - t) / duree);
      var pt = chemin.getPointAtLength((de + (a - de) * q) * L);
      gsap.set(el, { x: pt.x, y: pt.y });
    };
    tl.to(etat, { t: D, duration: D, ease: "none", onUpdate: placer }, 0);
    placer();
  };

  // --- La coupe : un trait de l'accent fend l'écran, les deux moitiés tombent -------------
  // `calque` : un calque plein cadre (position absolue, inset 0) de la scène ; ce qui est derrière
  // lui apparaît. Le trait monte de gauche (o.de, en part de la hauteur) à droite (o.a). Appelle-la
  // EN DERNIER, la timeline complète : elle fige une copie du calque telle qu'il est à l'instant t
  // (jamais de <video> dedans). Rend la copie.
  K.tranche = function (tl, calque, t, o) {
    o = o || {};
    var c = K.cadre(calque), L = c.largeur, H = c.hauteur;
    var ya = (o.de != null ? o.de : 0.64) * H, yb = (o.a != null ? o.a : 0.36) * H;
    tl.seek(t, false);
    var copie = calque.cloneNode(true);
    tl.seek(0, false);
    copie.removeAttribute("id");
    Array.prototype.forEach.call(copie.querySelectorAll("[id]"), function (n) { n.removeAttribute("id"); });
    calque.parentNode.insertBefore(copie, calque.nextSibling);
    var px = function (x, y) { return x + "px " + y + "px"; };
    gsap.set(calque, { clipPath: "polygon(" + [px(0, 0), px(L, 0), px(L, H), px(0, H)].join(", ") + ")" });
    gsap.set(copie, { opacity: 0, clipPath: "polygon(" + [px(0, ya), px(L, yb), px(L, H), px(0, H)].join(", ") + ")" });
    tl.set(calque, { clipPath: "polygon(" + [px(0, 0), px(L, 0), px(L, yb), px(0, ya)].join(", ") + ")" }, t);
    tl.set(copie, { opacity: 1 }, t);
    var long = Math.sqrt(L * L + (yb - ya) * (yb - ya)) * 1.12, angle = (Math.atan2(yb - ya, L) * 180) / Math.PI;
    var trait = K.el(calque.parentNode, "div", "k-tranche-trait");
    trait.setAttribute("data-layout-allow-overflow", "");
    gsap.set(trait, { width: long, x: -long * 0.05, y: ya, rotation: angle, transformOrigin: "0% 50%", scaleX: 0 });
    tl.to(trait, { scaleX: 1, duration: 0.16, ease: "power2.in" }, t - 0.16);
    tl.to(trait, { scaleY: 0, duration: 0.24, ease: "power2.in" }, t + 0.16);
    var d = o.duree || 0.55, ecart = o.ecart || H * 0.75;
    tl.to(calque, { y: -ecart, x: -50, rotation: -4, duration: d, ease: "power3.in" }, t + 0.04);
    tl.to(copie, { y: ecart, x: 50, rotation: 4, duration: d, ease: "power3.in" }, t + 0.04);
    return copie;
  };
})();
