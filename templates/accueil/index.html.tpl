<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <script src="assets/vendor/gsap.min.js"></script>
    <!-- Vignette d'accueil dans l'app HyperFrames : elle montre la marque telle que les vidéos la
         porteront. Aucune vidéo ici : chacune a son projet dans videos/. FICHIER GÉNÉRÉ par
         `studio_motion.py style` (brand/ est une copie du style). -->
    <link rel="stylesheet" href="brand/fonts.css">
    <link rel="stylesheet" href="brand/tokens.css">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: var(--brand-bg); }
      .bloc { position: absolute; left: 110px; right: 110px; color: var(--brand-text); font-family: var(--brand-font-body); }
      #produit { top: 150px; font-size: 34px; font-weight: 600; letter-spacing: 0.04em; color: var(--brand-muted); text-transform: uppercase; }
      #logo { position: absolute; top: 260px; left: 110px; width: 200px; height: 200px; object-fit: contain; border-radius: 36px; }
      #marque { top: 520px; font-family: var(--brand-font-display); font-weight: 800; font-size: {{TAILLE_MARQUE}}px; line-height: 1.05; letter-spacing: -0.02em; overflow-wrap: anywhere; }
      #etat { top: 690px; font-size: 40px; line-height: 1.3; color: var(--brand-muted); }
      #nuancier { top: 860px; display: flex; gap: 34px; }
      .pastille { display: flex; flex-direction: column; align-items: center; gap: 18px; font-size: 26px; color: var(--brand-muted); }
      .pastille i { display: block; width: 170px; height: 170px; border-radius: 50%; border: 4px solid var(--brand-surface-contrast); }
      #polices { top: 1180px; display: flex; gap: 70px; align-items: flex-end; }
      .police b { display: block; font-size: 150px; line-height: 1; color: var(--brand-text); }
      .police span { display: block; margin-top: 12px; font-size: 28px; color: var(--brand-muted); }
      #consigne { top: 1640px; font-size: 44px; line-height: 1.3; }
      #consigne strong { background: var(--brand-accent); color: var(--brand-contrast); padding: 2px 14px; border-radius: 10px; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="accueil" data-start="0" data-duration="6" data-fps="30" data-width="1080" data-height="1920">
      <p id="produit" class="bloc clip" data-start="0" data-duration="6" data-track-index="0">{{PRODUIT}}</p>
      {{LOGO}}
      <h1 id="marque" class="bloc clip" data-start="0" data-duration="6" data-track-index="1">{{MARQUE}}</h1>
      <p id="etat" class="bloc clip" data-start="0" data-duration="6" data-track-index="2">{{ETAT}}</p>
      <div id="nuancier" class="bloc clip" data-start="0" data-duration="6" data-track-index="3">
        <div class="pastille"><i style="background:{{FOND}}"></i>fond {{FOND}}</div>
        <div class="pastille"><i style="background:{{ACCENT}}"></i>marque {{ACCENT}}</div>
        <div class="pastille"><i style="background:{{TEXTE}}"></i>texte {{TEXTE}}</div>
        {{PASTILLE_SECONDAIRE}}
      </div>
      <div id="polices" class="bloc clip" data-start="0" data-duration="6" data-track-index="4">
        <div class="police"><b style="font-family:var(--brand-font-display); font-weight:800;">Aa</b><span>titres · {{TITRES}}</span></div>
        <div class="police"><b style="font-family:var(--brand-font-body); font-weight:400;">Aa</b><span>texte · {{CORPS}}</span></div>
      </div>
      <p id="consigne" class="bloc clip" data-start="0" data-duration="6" data-track-index="6">Tes vidéos se fabriquent dans Claude Code ou Codex : <strong>« fais-moi une vidéo »</strong>. Ici, tu les regardes et tu les retouches.</p>
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      tl.from("#marque", { y: 30, opacity: 0, duration: 0.6, ease: "power3.out" }, 0.1);
      tl.from(".pastille", { scale: 0.6, opacity: 0, duration: 0.45, stagger: 0.08, ease: "back.out(1.6)" }, 0.3);
      tl.from(".police", { y: 24, opacity: 0, duration: 0.5, stagger: 0.1, ease: "power3.out" }, 0.6);
      window.__timelines["accueil"] = tl;
    </script>
  </body>
</html>
