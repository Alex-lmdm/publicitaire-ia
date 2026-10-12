<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <!-- {{VIDEO_NOM}} de l'annonce « {{SUJET}} ». Point de départ VIDE : la composition s'écrit après
         le choix de l'angle et le PLAN.md validé (skill `annonce`). Durée cible {{DUREE}} s
         ({{DUREE_MIN}} à {{DUREE_MAX}} s). Format {{FORMAT}} 1080×1920, 30 images/s.
         Zones : `python3 {{MAISON}}tools/annonce.py zones {{FORMAT}}`. Tout texte important y tient. -->
    <script src="assets/vendor/gsap.min.js"></script>
    <script src="assets/vendor/CustomEase.min.js"></script>
    <!-- Style de la marque, copié du dossier Monteur IA à la création : polices et couleurs
         s'utilisent par var(--brand-*), jamais en dur (sauf les surfaces d'un produit montré). -->
    <link rel="stylesheet" href="brand/fonts.css">
    <link rel="stylesheet" href="brand/tokens.css">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: var(--brand-bg); }
      #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; background: var(--brand-bg); }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{DUREE}}" data-fps="30" data-width="1080" data-height="1920">
      <!-- Fond opaque, tout en bas de la pile : sans lui, une image vide passe en noir au rendu. -->
      <div id="fond" class="clip" data-start="0" data-duration="{{DUREE}}" data-track-index="0" style="position:absolute; inset:0; background:var(--brand-bg);"></div>

      <!-- Les sons (musique et bruitages) s'écrivent ici par tools/sons.py de Monteur IA. -->
      <!-- SONS -->
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      // La timeline couvre toute la durée, sinon les dernières images clignotent en noir.
      tl.to({}, { duration: {{DUREE}} }, 0);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
