# Les scènes : des exemples, pas des gabarits

Chaque plan du script devient une scène (une sous-composition de `compositions/`, montée dans
`index.html` : [kit.md](kit.md), « Le squelette d'une scène »). Tu l'écris sur mesure pour ce plan.
Les scènes déjà construites sont là pour t'inspirer, jamais pour te dicter le film.

Une story courte compte une ou deux scènes ; une story de lancement une par plan (huit ou neuf) ; un
Reel trois à six ; une vidéo de page huit à dix. Le nombre suit le script, et un plan peut tenir en
une scène comme en deux.

## Les scènes prêtes, en exemples

`templates/scenes/` (depuis un projet : `../../../templates/scenes/`) en garde dix, construites avec
le kit : `situation`, `nom-objet`, `schema`, `parcours`, `demo`, `preuve`, `prix`, `avant-apres`,
`messages`, `fin`. Écrites en 9:16, chacune prend le format du projet qui la monte (`K.cadre` lit
son hôte) et se remet en page en 16:9. Leur liste, leur rôle et ce qui en a été contrôlé :
`templates/scenes/README.md`. Sers-t'en comme d'un carnet :

- **lis-en une** pour voir comment se règle un problème (une mise en page qui marche dans les deux
  formats, une tenue de lecture calculée, une rafale, une caméra qui glisse de station en station) ;
- **reprends-en un geste** (le calcul, la courbe, l'enchaînement) dans ta propre scène ;
- **ou copie-la** dans `compositions/` et transforme-la autant que ton plan le demande. Une copie
  se remplit en entier : son objet `CONTENU` reçoit la vraie matière du client, et **rien d'exemple
  ne reste** (un chiffre d'exemple qui passe au rendu est un fait inventé). Ses faits y sont des
  emplacements (« [PRÉNOM] », « [SON PRIX] », « [CHIFFRE] », « [DÉLAI] ») : tant qu'il en reste un,
  la scène l'écrit en erreur dans la console (`K.emplacements`) et `check` le compte. L'accroche
  porte `data-accroche` (`situation`), le prix `data-prix` (`prix`) : un seul élément de la vidéo
  chacun ([composition.md](composition.md), règle 10).

Une scène prête posée telle quelle, puis une autre, puis une autre, donne exactement la vidéo plate
qu'on ne livre pas ([ambition.md](ambition.md)) : le passage entre deux scènes est toujours à toi.

## Des idées de plans, par rôle

Des points de départ ; change-les d'une offre à l'autre (le même film pour deux offres est un
défaut).

- **Ouvrir** : la corvée d'avant en grand, qui se charge à chaque mot, puis son coût chiffré ; la
  question tapée dans un champ ; la négation montrée (l'objet de l'ancienne façon barré, éteint,
  ses morceaux qui tombent) ; la preuve d'abord ; l'image qui intrigue ([ecriture.md](ecriture.md)).
- **Le pivot et le nom** : l'objet de son offre qui grandit depuis un clic et porte son nom ; un
  titre qui se change sur place ; les options qui montent de la profondeur, le curseur choisit la
  sienne, les autres tombent.
- **Comment ça marche** : la démo dans son interface reconstruite (le curseur agit, chaque étape se
  coche, son aperçu sort de la fenêtre) ; **le produit qui entre dans l'outil** que son public a
  déjà (le modèle posé dans Notion, le dossier glissé dans son IA : sans ce geste, on ne comprend
  pas ce qu'on achète en plus) ; le parcours en étapes sur une longue toile ; le schéma qui se trace,
  parcouru par le fil conducteur ; la matière brute qui se transforme, défaut par défaut.
- **Comparer** : l'écran coupé (l'ancienne façon et son chrono d'un côté, le résultat de l'autre) ;
  la pile d'étapes tranchée, remplacée par trois pastilles ; le balai qui révèle l'après.
- **Prouver** : ses vraies captures en éventail, chacune avec son vrai chiffre ; le grand chiffre
  au centre sur le flou ; ses vrais messages qui arrivent de la profondeur.
- **L'offre et le prix** : ce qu'on reçoit en travelling ; le prix qui claque, puis sa vraie
  échéance ; la vitrine des exemples (plus bas).
- **Finir** : ce qu'on a vu revient en mosaïque et se resserre en un bouton ; le produit se pose
  avec son nom et l'appel.

## Les vraies vidéos dans le film

Une `<video>` ne vit jamais dans une scène : elle vit à la racine d'`index.html`, son cadre en
`z-index: 2` ([kit.md](kit.md), pièges). Trois cas reviennent :

- **La vitrine des exemples** (des vidéos ou des pages faites pour d'autres offres) : elles restent
  dans leur vignette, jamais en plein écran. La rangée monte, le curseur clique la première, elle
  vient au centre (près de la moitié de la largeur), les autres pivotent sur les côtés
  (`rotationY` de 40 à 52°, voile et flou qui grandissent avec la distance), l'extrait joue 2 s
  avec sa barre de lecture, une bulle dit en 2 ou 3 mots ce que c'est. Pas de bouton lecture dans
  une story (il invite à toucher l'écran). Les vignettes et leurs `<video>` à la racine
  d'`index.html` (une seule timeline les place), deux affiches par vignette (première et dernière
  image de l'extrait) ; le curseur et les bulles dans une scène transparente devant (`z-index: 3`).
  Extraits de 2 s préparés par `preparer-video`.
- **La vignette qui devient la vidéo** de son offre : une vignette grandit jusqu'au plein écran
  (`scale` = largeur de l'écran / largeur de la vignette, centre amené au centre : `K.zoom`) ; à
  l'arrivée, la vraie vidéo joue, et sa première image est exactement la vignette (`ffmpeg -ss 0
  -frames:v 1`).
- **Le résultat qui joue dans le téléphone** : la `<video>` aux coordonnées exactes de l'écran du
  téléphone de la scène.
