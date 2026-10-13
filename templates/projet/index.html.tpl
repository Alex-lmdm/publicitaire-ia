<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width={{LARGEUR}}, height={{HAUTEUR}}">
    <!-- {{VIDEO_NOM}} : « {{SUJET}} » ({{OBJECTIF}}). Point de départ VIDE : la composition s'écrit
         après le choix de la structure et de l'angle, et le PLAN.md (skill `studio`).
         {{SUPPORT_TITRE}}, format {{FORMAT}} ({{LARGEUR}}×{{HAUTEUR}}), 30 images/s, {{IDEAL}} s visées.
         Zones : `python3 {{MAISON}}tools/studio_motion.py zones {{SUPPORT}} --format {{FORMAT}}`.
         Rythme visé : un événement toutes les demi-secondes, 1 à 4 mots par écran, des fonds qui
         alternent ; `studio_motion.py rythme exports/{{VIDEO}}.mp4` le vérifie après le rendu. -->
    <script src="assets/vendor/gsap.min.js"></script>
    <script src="assets/vendor/CustomEase.min.js"></script>
    <!-- Style de la marque, copié du dossier Monteur IA à la création : polices et couleurs
         s'utilisent par var(--brand-*), jamais en dur (sauf les surfaces d'un produit montré). -->
    <link rel="stylesheet" href="brand/fonts.css">
    <link rel="stylesheet" href="brand/tokens.css">
    <!-- Le kit (fonds vivants, curseur, objets flottants, chapitres, fenêtres, téléphone) : mode
         d'emploi dans references/kit.md du skill `studio`. Une scène = une sous-composition. -->
    <link rel="stylesheet" href="kit/kit.css">
    <!-- Inter, pour les interfaces reconstruites : feuille écrite à côté de ses fichiers. -->
    <link rel="stylesheet" href="assets/fonts/interfaces.css">
    <script src="kit/icones.js"></script>
    <script src="kit/ajouts.js"></script>
    <script src="kit/kit.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: {{LARGEUR}}px; height: {{HAUTEUR}}px; overflow: hidden; background: var(--brand-bg); }
      #root { position: relative; width: {{LARGEUR}}px; height: {{HAUTEUR}}px; overflow: hidden; background: var(--brand-bg); }
      [data-composition-id="main"] > div[data-composition-src] { position: absolute; inset: 0; z-index: 1; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{DUREE}}" data-fps="30" data-width="{{LARGEUR}}" data-height="{{HAUTEUR}}">
      <!-- Fond opaque, tout en bas de la pile : sans lui, une image vide passe en noir au rendu. -->
      <div id="fond" class="clip" data-start="0" data-duration="{{DUREE}}" data-track-index="0" style="position:absolute; inset:0; background:var(--brand-bg);"></div>

      <!-- Repère de départ, à remplacer par les scènes (une sous-composition par scène). -->
      <div id="attente" class="clip" data-start="0" data-duration="{{DUREE}}" data-track-index="1" style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center;">
        <p id="attente-texte" style="font:600 48px/1.2 var(--brand-font-body); color:var(--brand-muted); text-align:center;">{{VIDEO_NOM}} · à composer</p>
        <div id="attente-barre" style="position:absolute; left:10%; right:10%; bottom:50%; margin-bottom:-60px; height:6px; border-radius:3px; background:var(--brand-accent); transform-origin:left center;"></div>
      </div>

      <!-- Les sons (voix, musique et bruitages) s'écrivent ici par tools/sons.py de Monteur IA. -->
      <!-- SONS -->
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      // La durée vient de data-duration ; pas de tween vide pour l'allonger (règle HyperFrames).
      // La barre avance sur toute la durée : `check` vérifie que l'image change jusqu'à la fin.
      tl.from("#attente-texte", { y: 20, opacity: 0, duration: 0.4, ease: "power3.out" }, 0.2);
      tl.fromTo("#attente-barre", { scaleX: 0 }, { scaleX: 1, duration: {{DUREE}}, ease: "none" }, 0);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
