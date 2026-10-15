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
  musiques (la musique : `musiques choisir --duree <durée> --ouvrir`, puis `musiques prendre <n> --a <pivot>
  --duree <durée>`), musique,
  sons, planche, rythme, son, export. Texte à l'écran et musique par défaut ; une voix off seulement
  à la demande du client (`references/voix.md`).
- **Où en est la vidéo** : reprends le parcours du skill là où `{{DOSSIER}}PLAN.md` (le brief, le
  plan) et `{{DOSSIER}}OFFRE.json` s'arrêtent : fiche vide, étape 2 ; fiche validée sans plan, étape 3.
- Retouche demandée : modifie seulement ce qui est demandé, refais le rendu de CETTE vidéo,
  puis repasse la planche et l'export. Ne relance pas tout.
- **Dans l'app HyperFrames** (tes consignes disent alors que l'app fait le rendu) : fais la retouche
  dans `index.html`, `compositions/` et `assets/`, sans rendu ; le client la voit tout de suite dans
  l'app. Puis dis-lui : « C'est fait, tu la vois dans l'app. Pour mettre à jour tes fichiers prêts à
  publier (le son réglé, la couverture), ouvre ton dossier {{PRODUIT}} dans ton assistant et dis
  « mets à jour la livraison de {{VIDEO_NOM}} ». » Le bouton Export de l'app donne un brouillon
  dans Téléchargements, pas le fichier final. Si l'app te propose ses propres skills (`hyperframes`,
  `launch-film`, `product-launch-video`), garde la méthode du skill `studio` : ils ne connaissent ni
  la fiche de l'offre ni la marque de cette vidéo.
- Jamais `hyperframes feedback`, `publish`, `cloud`, `lambda` ni `cloudrun`.
- Rendu : `npm run render` (fichier dans `exports/{{VIDEO}}.mp4`), après `npm run check`. Puis
  `studio_motion.py rythme exports/{{VIDEO}}.mp4` : il doit répondre « ok ».
