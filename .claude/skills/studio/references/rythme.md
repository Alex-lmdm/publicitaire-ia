# Rythme, mouvement et caméra

Ce fichier fait foi pour les vidéos du studio. La référence de niveau est une vidéo de
lancement produit en motion design : il s'y passe quelque chose **toutes les demi-secondes**, le
texte tient en quelques mots, la caméra ne s'arrête jamais vraiment, et un objet devient le
suivant au lieu de laisser place à un écran vide. Une vidéo qui enchaîne des écrans de texte
posés, même propres, ressemble à des slides : c'est l'échec à éviter.

Le contrôle `python3 ../../../tools/studio_motion.py rythme exports/<vidéo>.mp4` (depuis le projet) mesure le MP4 rendu : **au moins
1 événement par seconde**, **0,8 s au plus entre deux événements en général**, et **aucune image
figée plus de 1 s** avant l'écran final. Il ne dit pas si c'est beau ; il dit si ça vit.

## La densité : un événement toutes les demi-secondes

Un événement, c'est ce que l'œil remarque : un mot qui entre, un objet qui arrive, un curseur qui
clique, une coche, un compteur qui tourne, un fond qui bascule, la caméra qui change d'intention.
Pas forcément un nouveau plan : souvent un petit geste dans le même plan.

- Cale le plan sur une **grille de tempo** : 120 battements par minute, un temps = 0,5 s. Les
  événements tombent sur les temps (ou les demi-temps pour une rafale). La musique s'y posera.
- Pendant qu'un texte se lit, il reste immobile, **mais le monde autour vit** : la caméra dérive
  lentement, les objets flottants bougent, le curseur approche, un compteur tourne.
- Une tenue sans rien autour ne dépasse jamais 1 s. Seul l'écran final se tient (2,5 s ou plus),
  et même lui garde un peu de vie (objets qui dérivent).
- Rafales : une liste d'éléments arrive en cascade de 0,05 à 0,13 s d'écart, jamais un par un à
  une seconde d'intervalle.
- **Le milieu de la vidéo s'essouffle** (de la démo à la preuve) : vise 1,3 événement par seconde
  et aucun creux de plus de 2 s (`rythme` liste les plus longs). Comble-les par de petits
  événements réels, chacun avec son bruitage : un flash quand le vrai résultat apparaît, une
  pastille qui confirme (« Description prête »), une carte de plus qui arrive, un trait qui
  s'allonge sous un chiffre tenu. Léger : le spectateur ne doit pas le remarquer, seulement ne
  pas s'ennuyer.

## Lire sans s'ennuyer

- Un écran porte **1 à 4 mots**, 6 au plus et rarement (`studio_motion.py lecture "<texte>"`
  calcule la tenue et prévient au-delà). Ce qui ne tient pas en 4 mots se **montre** : une
  interface, un objet, un compteur, un avant / après.
- Tenue minimale : 0,25 s par mot + 0,5 s, jamais moins de 0,8 s. Un mot isolé se lit en un
  temps ; une ligne de 4 mots en un peu plus d'une seconde.
- Deux graisses : la partie d'appui en léger et grise, le mot qui compte en gras (« Ton nouveau
  **monteur** »). Un mot clé peut être surligné à la couleur de la marque.
- On ne déplace pas un texte pendant qu'on le lit. Il entre, se pose, reste, sort.

## La grammaire du mouvement

- **Entrées** de 0,4 à 0,7 s en forte décélération (`expo.out`), avec déplacement (20 à 50 px)
  et léger flou qui se dissipe ; mot par mot pour un titre (0,06 à 0,1 s d'écart). Jamais un
  fondu d'opacité seul.
- **Sorties** plus rapides que les entrées (0,25 à 0,35 s, `power2.in`), vers le haut ou en
  flou.
- Objets d'interface : un léger dépassement à l'arrivée (`back.out(2)`) est bienvenu ; pas de
  rebond élastique sur les titres.
- Aucun mouvement à vitesse constante (sauf une tête de lecture, une barre de progression).
- Interdits : oscillations en boucle sur un élément qu'on lit, tremblement de caméra, effet qui
  se répète sans cible.

## La caméra : continue, en profondeur

- Chaque scène vit dans un espace en perspective (`k-scene3d` > `k-camera` du kit). La caméra a
  presque toujours un léger angle (rotation de 4 à 15°) et dérive pendant les tenues.
- Entre deux intentions, elle **recadre vite** (0,6 à 0,9 s, `expo.inOut`) : elle s'approche du
  geste (le champ où l'on tape, le bouton qu'on clique), elle recule sur le résultat.
- Pour zoomer sur un point P avec une échelle s, déplace la caméra de (centre − P) × s.
- Profondeur de champ : les objets très proches et très lointains sont flous, le sujet est net.
  Pendant un grand chiffre, ce qui est derrière passe au flou et s'assombrit.

## Les transitions : un objet devient le suivant

Peu de coupes franches. Les procédés qui marchent, du plus fort au plus simple :

1. **Le raccord d'objet** : l'objet de fin d'une scène est l'objet de début de la suivante (le
   fond jaune du nom devient la fenêtre de l'application ; la bande montée devient un téléphone ;
   tout se resserre en un bouton). La scène suivante commence avec cet objet exactement à la même
   place et à la même taille.
2. **Le flash depuis un clic** : le curseur clique, un disque de couleur part du point cliqué et
   envahit l'écran (`K.flash`). Le fond change d'un coup, avec une cause visible.
3. **La plongée** : on traverse l'élément cliqué (l'interrupteur d'un chapitre) en zoomant à
   travers, avec flou ; la démo est derrière.
4. **Le volet** : un panneau d'une autre couleur glisse et pousse la moitié de l'écran (écran
   coupé avant / après), ou remplace le fond.
5. **La coupe franche** sur un temps fort de la musique, rarement.

Jamais de fondu enchaîné entre deux mises en page chargées (double exposition boueuse). Une
couleur qui disparaît s'efface par un volet net (`scaleY` vers 0), pas par une transparence.

## Le motif qui revient

Une vidéo longue a besoin d'un geste qui revient et structure : le spectateur reconnaît qu'on
passe à la partie suivante. Le motif du kit : **le chapitre** (`K.chapitre`). Un mot géant et
pâle glisse en fond, l'étiquette nette dit la fonction (« Dérushage »), le curseur active un
interrupteur, on plonge dans la démonstration. Sur fond de couleur de marque, il devient la
signature de la vidéo. Deux à cinq chapitres par vidéo de page, un ou deux dans un Reel.

## Gestes et interfaces

Quand on montre un produit en action : **état avant → le curseur approche → clic → l'interface
réagit → état obtenu**, sans pause morte entre les étapes. Le clic précède la réaction ; la
pointe du curseur est son point actif ; on tape par petits groupes de lettres (`K.taper`), en
moins d'une seconde pour une phrase courte. Ce que le produit produit sort de la fenêtre en
aperçus flottants (une carte par étape cochée) : la profondeur et la densité viennent de là.

## La fin

Tout ce qu'on a vu revient en mosaïque (vignettes des interfaces, des résultats, du prix), la
caméra recule et pivote, puis tout se resserre au centre en **un bouton** que le curseur clique :
il se remplit de la couleur de la marque. Le nom et le bouton se tiennent ensuite au moins 2,5 s,
avec quelques objets qui dérivent autour. En page de vente, ce bouton désigne celui qui est sous
la vidéo.

## Avant d'animer

Pose les images clés de chaque scène (début, milieu, fin) et regarde-les à la taille d'une
vignette (`npx hyperframes snapshot --at …`). Une mise en page ratée se voit là. Puis anime en
vérifiant les raccords : la dernière image d'une scène et la première de la suivante doivent se
ressembler à s'y méprendre.
