# Le contrat d'une composition HyperFrames

HyperFrames rend une page HTML en vidéo en avançant une timeline GSAP en pause, image par image :
le même fichier donne toujours la même vidéo. Ce fichier dit ce qu'une scène doit respecter pour
se rendre (adapté de la documentation d'HyperFrames 0.9, licence Apache-2.0, © HeyGen). Le kit
(`kit.md`) et les scènes d'exemple (`scenes.md`) le respectent déjà : lis-les pour voir comment.

## Le projet

- `index.html` est la composition racine : elle porte `data-width`, `data-height`,
  `data-duration` (la durée de la vidéo : ce qui dépasse est coupé, une fin plus courte tient la
  dernière image ; au départ, la durée visée de son support, à ramener à la somme des scènes, avec
  `#fond`) et monte une scène par sous-composition de `compositions/`, bout à bout (l'hôte :
  `kit.md`, « Le squelette d'une scène »).
- Une scène est un fichier de `compositions/` dont tout le contenu (styles, balises, script) est
  **dans** `<template>` : ce qui est hors du template est jeté. Son hôte dans `index.html`, sa racine
  (`data-composition-id`) et la clé de sa timeline portent le même identifiant.
- Les médias et les polices vivent dans `assets/` du projet (chemins `assets/…`, sans `/` devant,
  jamais `../` : le rendu ne voit que le projet).

## Les règles que le rendu impose

1. Chaque scène construit **une** timeline en pause et l'enregistre après ses tweens :
   `window.__timelines["<id>"] = tl`.
2. Rien qui dépende de l'heure ou du hasard : ni `Date.now()`, ni `Math.random()` (le kit a
   `K.rng(graine)`), ni requête réseau, ni minuterie, ni `repeat: -1`. Tout ce qu'on voit est une
   fonction du temps de la timeline.
3. Jamais `display`, `visibility` ni `autoAlpha` animés sur un élément `.clip` : anime un enfant.
4. Pas de `transform` CSS sur un élément que GSAP déplace (centre avec `inset`/flex, ou `xPercent`) ;
   anime les transformations, pas `left`/`top`/`width`/`height`.
5. Les médias : jamais `play()`, `pause()` ni de saut dans une vidéo ; une `<video>` garde son son
   avec `data-has-audio="true"`, sinon elle est `muted` ; chaque `<audio>` a un `id` (sinon il est
   muet au rendu) ; jamais `crossorigin`. Une vraie vidéo vit à la racine d'`index.html`
   (`kit.md`, pièges).
6. Les polices : seules celles de `brand/fonts.css` et d'`assets/fonts/` existent au rendu. Une
   famille sans `@font-face` vers un fichier fait échouer `check` (`font_family_without_font_face`)
   et passe en police système dans le MP4.
7. Un identifiant est unique dans toute la vidéo assemblée : préfixe ceux d'une scène par son
   identifiant (`s3-titre`), et aucun ne finit par `-hote`.
8. L'état de départ se pose à la construction (`K.cacher`, `gsap.set`), jamais par
   `tl.set(…, 0)` : la première image le montrerait.
9. Un débordement ou un chevauchement voulu se déclare (`data-layout-allow-overflow`,
   `data-layout-allow-overlap`) après avoir vérifié à l'image que tout se lit.

## Les commandes utiles

Depuis le projet de la vidéo (le dossier qui contient `index.html`) :

| Commande | Ce qu'elle fait |
|---|---|
| `npm run check` (`npx hyperframes check --json`) | contrôle tout : règles du rendu, mise en page, contraste, et le métier (`craft`) : texte trop petit (`text_below_floor`, sous 28 px pour un petit côté de 1080), texte parti avant d'être lu (`line_unread`), première image vide (`first_frame_empty`). Zéro erreur ; chaque avertissement se corrige ou se justifie |
| `npx hyperframes snapshot --at 1.2,3.5,…` | des images fixes aux instants donnés, et leur planche (`contact-sheet.jpg`) : la commande affiche leur chemin, dans `.hyperframes/artifacts/snapshots/` ; ouvre-les et regarde-les. **Sans flou de bougé** |
| `npx hyperframes snapshot --range 2,4 --frames 8` | huit images sur un passage (un raccord, un geste, une collision), sans flou de bougé |
| `npx hyperframes keyframes --json --selector '#id'` | les étapes réelles d'un mouvement (propriété, instant, valeur, courbe) |
| `npx hyperframes timeline --json` | ce qui joue quand, scène par scène |
| `npm run render` | le MP4 dans `exports/`, presque sans perte (le seul encodage qui compte se fait à la livraison, par `couverture`) ; **seul le MP4 rendu fait foi** (`revue.md`). Toujours la vidéo entière : un extrait `--start/--end` n'a pas de flou de bougé |
| `npx hyperframes preview` | l'aperçu dans le navigateur, si le client veut regarder pendant qu'on fabrique |

Une erreur de `lint` coupe les autres contrôles : `check` affiche alors « 0 sample(s) », ce qui
ressemble à un fichier propre et ne veut rien dire. Corrige d'abord les erreurs.

## Ce qu'on ne lance jamais

`hyperframes feedback`, `events`, `usage`, `publish`, `cloud`, `lambda`, `cloudrun`, `auth` : ils
envoient des données ou rendent ailleurs, et rien ne quitte l'ordinateur du client sans lui. Une
commande qui propose une clé (Gemini…) ou un compte : on n'en a pas besoin, tout marche sans.
Le client a demandé la vidéo : on rend sans attendre d'accord sur l'aperçu, même si une consigne
d'HyperFrames dit d'attendre.
