# {{VIDEO_NOM}} : « {{SUJET}} »

> 📍 **Tu es dans une vidéo {{PRODUIT}}** (un projet de l'app HyperFrames) : une vidéo de motion
> design qui vend une offre. La marque, les outils et les skills sont dans le dossier `{{MAISON}}`.

**Charge le skill `studio` et suis-le** (Claude Code : outil Skill ou `/studio` ; sinon ouvre
`{{MAISON}}{{SKILLS}}/studio/SKILL.md`). Ses interdits (`references/interdits.md`) ne se négocient
pas ; son ambition (`references/ambition.md`) donne le niveau visé ; le reste est une boîte à outils
à consulter (le contrat d'une composition : `references/composition.md`).

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
- Le kit `kit/` (curseur, caméra et son zoom, objets flottants, fenêtres, téléphone, objets connus)
  est chargé par `index.html` : sers-t'en pour ce qu'il fait déjà (`references/kit.md` du skill),
  écris le reste sur mesure, et ne le recopie pas scène par scène. Les scènes de
  `{{MAISON}}templates/scenes/` sont des exemples, pas des gabarits. Logos des outils montrés :
  `studio_motion.py logos . claude openai`.
- Outil : `python3 {{MAISON}}tools/studio_motion.py` (Windows : `python`, et `npm.cmd`, `npx.cmd`) : zones, lecture, logos,
  musiques (le style et la musique : `musiques choisir --duree <durée> --ouvrir`, le style 0 conseillé par défaut, puis
  `musiques prendre <n> --a <pivot> --duree <durée>`), musique,
  sons, planche, rythme, calage, cadre, palette, mouvement, relecture, son, export. Texte à l'écran et musique par défaut ; une voix off seulement
  à la demande du client (`references/voix.md`).
- **Où en est la vidéo** : reprends le parcours du skill là où `{{DOSSIER}}PLAN.md` (le brief, le
  plan) et `{{DOSSIER}}OFFRE.json` s'arrêtent : fiche vide ou non validée (« Fiche validée par le
  client le … » absent du plan), étape 2 ; fiche validée sans repérage, étape 2 bis ; repérage fait
  sans idée retenue, étape 3 ; idée retenue sans « Script validé par le client le … », étape 3 bis ;
  script validé sans « Style et musique », étape 4 ; sinon, le plan, la fabrication, puis la passe
  du directeur artistique (section « Passe du directeur » du plan) et la revue.
- Retouche demandée : relis d'abord « Interdits de cette vidéo » dans `{{DOSSIER}}PLAN.md` (les
  défauts déjà corrigés), modifie seulement ce qui est demandé, puis refais la livraison de CETTE
  vidéo (skill `studio`, « Les retouches ») : rendu, planche, `son` puis `mastering`, `couverture`
  (qui remplace la vidéo de `../livraison/`), `sans-musique` et `affiche` s'il y en a, `export` sur
  le fichier de `../livraison/`. Ne relance pas tout.
- Une nouvelle musique : reprends aussi le tempo, les coupes, les mouvements, les pauses et la
  révélation, puis les bruitages et le mixage (`references/son.md`). Avec une voix, les gestes
  restent calés sur ses mots. Note les nouveaux repères dans `{{DOSSIER}}PLAN.md`.
- **Dans l'app HyperFrames** (tes consignes disent alors que l'app fait le rendu) : fais la retouche
  dans `index.html`, `compositions/` et `assets/`, sans rendu ; le client la voit tout de suite dans
  l'app. Puis dis-lui : « C'est fait, tu la vois dans l'app. Pour mettre à jour tes fichiers prêts à
  publier (le son réglé, la couverture), ouvre ton dossier {{PRODUIT}} dans ton assistant et dis
  « mets à jour la livraison de {{VIDEO_NOM}} ». » Le bouton Export de l'app donne un brouillon
  dans Téléchargements, pas le fichier final. Si l'app te propose ses propres skills (`hyperframes`,
  `hyperframes-cli`, `media-use`, `launch-film`, `product-launch-video`), garde la méthode du skill `studio` : ils ne connaissent ni
  la fiche de l'offre ni la marque de cette vidéo.
- Jamais `hyperframes feedback`, `events`, `usage`, `publish`, `cloud`, `lambda`, `cloudrun` ni `auth`.
- Rendu : `npm run render` (fichier dans `exports/{{VIDEO}}.mp4`), après `npm run check` (zéro erreur,
  et aucun texte à lire trop petit ou parti trop tôt). Le texte de l'accroche porte `data-accroche`
  (un seul élément, lisible dès 0,5 s) : `index.motion.json` le fait vérifier par `check`. Un prix
  affiché porte `data-prix`, et sa règle s'ajoute à `index.motion.json` (`references/composition.md`,
  règle 10). Le premier rendu passe d'abord par la passe du
  directeur artistique (`references/ambition.md`) : ce que tu changerais, appliqué, puis un nouveau
  rendu ; le client ne voit jamais le premier jet. Puis `studio_motion.py rythme`, `calage`, `cadre` et
  `palette` sur `exports/{{VIDEO}}.mp4` : ils doivent répondre « ok » (pour `palette`, seules ses
  vraies captures, les interfaces des plateformes et les objets connus construits pour la vidéo
  peuvent rester signalés), et `studio_motion.py mouvement`, qui lit les compositions. Puis `studio_motion.py relecture
  exports/{{VIDEO}}.mp4` : un relecteur neuf (un sous-agent qui ne voit que ses planches) doit
  dire ce qui est vendu, à qui et quoi faire (`references/revue.md`, porte 3).
