# Rythme, mouvement et caméra

La faute numéro un des vidéos faites par IA : **ça va trop vite**. Le texte passe avant d'être
lu, la caméra court, tout bouge en même temps. Ces règles sont des planchers mesurables.

## Lire avant de bouger

- Un texte reste **immobile** au moins `0,35 s par mot + 0,3 s`, jamais moins de 1,2 s.
  `python3 tools/studio_motion.py lecture "<texte>"` fait le calcul. L'écran final tient 2,5 s ou plus.
- On ne déplace pas un texte pendant qu'on le lit. Il entre, il se pose, il reste, il sort.
- « Entrée rapide, puis tenue » : jamais « entrée rapide, puis disparu ».
- Sur une musique rapide (plus de 110 temps par minute), le texte ne suit pas chaque temps :
  un temps sur deux, ou tout apparaît puis tient.
- Si le plan ne tient pas dans la durée : **coupe du texte**, ne raccourcis pas les tenues.

## La grammaire du mouvement

- Entrées de **0,24 à 0,38 s**, en décélération (`power3.out` ou proche), avec un déplacement de
  10 à 28 px. Jamais un simple fondu d'opacité seul.
- Sorties **plus rapides** que les entrées (50 à 75 % de leur durée).
- Aucun mouvement à vitesse constante (sauf une barre de progression). Pas de rebond ni
  d'élastique sur les titres ; un très léger dépassement à l'arrivée est permis sur un élément
  d'interface.
- Une seule chose bouge à la fois. Le reste se stabilise pendant qu'on lit ou qu'on regarde.
- Rien ne bouge au moment d'une coupe : au moins 0,15 s de calme avant.
- **Interdits** : flottements, respirations et oscillations en boucle pour « remplir » ;
  tremblements de caméra ; effets qui se répètent sans cible.

## Caméra et transitions

- La caméra est **lente** : environ la moitié de la vitesse qu'on choisirait par réflexe
  (un recadrage prend 0,6 à 1,2 s, un mouvement long 1,5 à 3 s). Un seul mouvement de caméra
  par plan, motivé : on s'approche du geste, on recule sur le résultat.
- 2 à 3 transitions par vidéo, pas plus. Un sens de mouvement dominant pour toute la vidéo.
- Raccord en pleine vitesse : l'objet sortant et l'objet entrant partagent la direction et la
  vitesse apparente autour de la coupe.
- Jamais de fondu enchaîné entre deux mises en page chargées (on voit une double exposition
  boueuse) : décale la sortie et l'entrée, ou repasse par le fond.
- Un objet qui reste d'un plan à l'autre (le bouton, la carte de l'offre, le point d'accent) relie
  mieux qu'un effet de transition.

## Gestes et interfaces

Quand on montre un produit en action (une page, un logiciel, un espace de formation) :
**état avant → intention (le curseur approche) → action → réaction de l'interface → état
obtenu → pause utile**. Le clic précède la réaction ; la pointe du curseur est son point actif ;
on tape en quelques étapes courtes, jamais un paragraphe entier. Le produit change à l'écran,
pas seulement son cadre.

## Le temps fort

- 0,3 à 0,6 s d'immobilité juste avant la révélation de l'offre : le silence prépare le moment.
- La révélation tombe sur le temps fort de la musique (voir `son.md`).
- La vidéo se termine sur une image propre et tenue, sans élément à moitié sorti.

## Avant d'animer

Pose les 3 ou 4 images clés de la vidéo (accroche, révélation, preuve, écran final) et
regarde-les à taille de téléphone. Une mise en page ratée se voit là. L'animation vient après.
