# {{VIDEO_NOM}} : « {{SUJET}} »

> 📍 **Tu es dans une vidéo {{PRODUIT}}** (un projet de l'app HyperFrames) : une vidéo de motion
> design qui vend une offre. La marque, les outils et les skills sont dans le dossier `{{MAISON}}`.

**Charge le skill `studio` et suis-le** (Claude Code : outil Skill ou `/studio` ; sinon ouvre
`{{MAISON}}{{SKILLS}}/studio/SKILL.md`). Ses références décident de la structure, de l'écriture, du
format, du rythme, du son et de la revue de cette vidéo. Contrat d'une composition :
`{{MAISON}}{{SKILLS}}/hyperframes-core/SKILL.md` ; effets : `{{MAISON}}{{SKILLS}}/hyperframes-animation/SKILL.md`.

- Objectif : **{{OBJECTIF}}**. Support : **{{SUPPORT_TITRE}}**. Format **{{FORMAT}}**
  ({{LARGEUR}}×{{HAUTEUR}}), 30 images/s, **{{IDEAL}} s** visées (bornes {{DUREE_MIN}} à {{DUREE_MAX}} s).
  Son : {{SON}}. Appel à l'action : {{CTA}}.
- Le dossier parent (`{{DOSSIER}}`) porte la fiche, le plan, les sources et la livraison.
  **`{{DOSSIER}}OFFRE.json` est la seule source des faits** : un prix, une date, un chiffre ou un
  témoignage absent de la fiche n'apparaît pas dans la vidéo.
- Ta part du plan : la section « {{VIDEO_NOM}} » de `{{DOSSIER}}PLAN.md`. Ne la change pas sans le
  dire au client.
- La marque est copiée dans `brand/` (couleurs `var(--brand-*)`, polices, `brand/logo.*` s'il en a
  un) : jamais une couleur ou une police de marque en dur. Elle vient de `{{MAISON}}marque.json`.
- Le rendu ne voit que ce dossier : une capture, un logo, un son ou une voix va d'abord dans `assets/`.
- Le kit `kit/` (fonds vivants, curseur, objets flottants, chapitres, fenêtres, téléphone) est
  chargé par `index.html` : pars de lui (mode d'emploi : `references/kit.md` du skill), ne le
  réécris pas scène par scène. Logos des outils montrés : `studio_motion.py logos . claude openai`.
- Outil : `python3 {{MAISON}}tools/studio_motion.py` (Windows : `python`) : zones, lecture, logos,
  sons, planche, rythme, son, export.
- Retouche demandée : modifie seulement ce qui est demandé, refais le rendu de CETTE vidéo,
  puis repasse la planche et l'export. Ne relance pas tout.
- Rendu : `npm run render` (fichier dans `exports/{{VIDEO}}.mp4`), après `npm run check`. Puis
  `studio_motion.py rythme exports/{{VIDEO}}.mp4` : il doit répondre « ok ».
