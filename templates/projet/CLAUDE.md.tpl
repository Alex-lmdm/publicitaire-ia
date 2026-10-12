# {{VIDEO_NOM}} : annonce « {{SUJET}} »

> 📍 **Tu es dans une vidéo d'annonce** (un projet de l'app HyperFrames, extension d'annonces de
> Monteur IA). Ce n'est pas un Reel face caméra : pas de dérush, pas de sous-titres de voix, pas
> de cadrage du visage. Le pipeline Reel de Monteur IA ne s'applique pas ici.

**Charge le skill `annonce` et suis-le** (Claude Code : outil Skill ou `/annonce` ; sinon ouvre
`{{MAISON}}.claude/skills/annonce/SKILL.md`). Ses références décident du format, du rythme, du
son et de la revue de cette vidéo.

- Format : **{{FORMAT}}**, 1080×1920, 30 images/s, durée cible **{{DUREE}} s** ({{DUREE_MIN}} à {{DUREE_MAX}} s).
- L'annonce entière (fiche de l'offre, plan, sources, livraison) est dans le dossier parent
  (`{{ANNONCE}}`). **`{{ANNONCE}}OFFRE.json` est la seule source des faits** : un prix, une date,
  un chiffre ou un témoignage absent de la fiche n'apparaît pas dans la vidéo.
- Ta part du plan : la section « {{VIDEO_NOM}} » de `{{ANNONCE}}PLAN.md`. Ne la change pas sans
  le dire au client.
- Le rendu ne voit que ce dossier : une capture, un logo ou un son va d'abord dans `assets/`.
- Outil : `python3 {{MAISON}}tools/annonce.py` (zones, lecture, planche, son, export).
- Retouche demandée : modifie seulement ce qui est demandé, refais le rendu de CETTE vidéo,
  puis repasse la planche et l'export. Ne relance pas l'annonce entière.
- Rendu : `npm run render` (fichier dans `exports/{{VIDEO}}.mp4`), après `npm run check`.
