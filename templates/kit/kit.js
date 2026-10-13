/* Kit Studio Motion : les briques d'un motion design produit, communes aux scènes (chargé dans
   index.html après GSAP). Tout est déterministe : aucune horloge, aléatoire à graine, chaque état
   se calcule à partir du temps de la scène. Chaque fonction ajoute ses mouvements à la timeline
   donnée. Mode d'emploi : skill `studio`, references/kit.md.

   Règle d'or des états de départ : un élément caché au début se cache par gsap.set (ou K.cacher)
   à la construction, jamais par tl.set(…, 0) : un set à 0 ne s'applique pas sur la toute
   première image, qui montrerait l'élément une fraction de seconde. */
(function () {
  var K = (window.K = window.K || {});
  var NS = "http://www.w3.org/2000/svg";

  K.ic = function (nom) { return (window.K_ICONES || {})[nom] || ""; };
  // Cache dès la construction (première image comprise) ; un tween ou un set les montre ensuite.
  K.cacher = function (cible, vars) { gsap.set(cible, Object.assign({ opacity: 0 }, vars || {})); };

  // Aléatoire à graine : la même graine donne toujours la même suite.
  K.rng = function (graine) {
    var s = (graine >>> 0) || 1;
    return function () { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; };
  };
  K.entre = function (a, b, p) { return a + (b - a) * p; };

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
  K.champ = function (parent, o) {
    var r = K.rng(o.graine || 1), els = [];
    var z = o.zone || { x0: 0, y0: 0, x1: 1920, y1: 1080 };
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
  K.chapitre = function (tl, racine, curseur, t, o) {
    o = o || {};
    var fantome = racine.querySelector(".k-fantome"), mots = racine.querySelectorAll(".k-etiquette .k-mot"),
      inter = racine.querySelector(".k-interrupteur"), plein = inter.querySelector(".k-plein"), bille = inter.querySelector(".k-bille");
    gsap.set(plein, { scaleX: 0 });
    tl.fromTo(fantome, { x: 260, opacity: 0 }, { x: -60, opacity: 1, duration: 2.4, ease: "power2.out" }, t);
    K.entreeMots(tl, mots, t + 0.1, { decalage: 0.06 });
    tl.fromTo(inter, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2)" }, t + 0.3);
    var cx = 960 + 18, cy = 540 + 122;
    K.trajet(tl, curseur, [[0, o.depart ? o.depart[0] : 1500, o.depart ? o.depart[1] : 1000], [t + 0.35, cx, cy, 0.55, "power3.out"]]);
    K.clic(tl, curseur, t + 0.95);
    tl.to(bille, { x: 40, duration: 0.3, ease: "power3.inOut" }, t + 0.98);
    tl.to(plein, { scaleX: 1, duration: 0.3, ease: "power3.inOut" }, t + 0.98);
    return t + 1.35; // moment où la plongée vers la démo peut partir
  };
})();
