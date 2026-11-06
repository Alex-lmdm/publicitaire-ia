# Rythme, mouvement et caméra

Ce fichier fait foi pour les vidéos du studio. La référence de niveau est une vidéo de
lancement produit en motion design : il s'y passe quelque chose **toutes les demi-secondes**
autour du texte, la caméra ne s'arrête jamais vraiment, et un objet devient le suivant au lieu de
laisser place à un écran vide. Mais **les mots, eux, suivent la lecture** : un groupe de mots
reste tant qu'un inconnu n'a pas fini de le lire. Et il y en a peu : l'image raconte. Trois
échecs à éviter : des écrans de texte posés sur un fond mort (on dirait des slides), des mots qui
filent avant d'être lus (la story d'ouverture refusée du 06/11/2026 : 19 s, des écrans de 1 à 4
mots changés toutes les 1 à 2 s, « beaucoup trop rapide »), et des sous-titres (la story v2
refusée du 07/11/2026 : une phrase entière par écran, 115 mots en 47 s).

Le contrôle `python3 ../../../tools/studio_motion.py rythme exports/<vidéo>.mp4` (depuis le projet) mesure le MP4 rendu : **au moins
0,7 événement par seconde**, **1,2 s au plus entre deux événements en général**, et **aucune
image vraiment immobile plus de 1,5 s** avant l'écran final (une dérive lente, une vidéo qui tourne
vivent). Il ne dit pas si c'est beau ; il dit si ça vit. Recalé le 06/11/2026 pour des phrases
tenues le temps de leur lecture : vise plus (1 à 1,3 événement par seconde autour du texte), ce
n'est qu'un plancher.

## La densité : un événement toutes les demi-secondes

Un événement, c'est ce que l'œil remarque : un objet qui arrive, un curseur qui clique, une
coche, un compteur qui tourne, un fond qui bascule, le mot clé de la phrase qui s'allume, la
caméra qui change d'intention entre deux phrases. Pas forcément un nouveau plan : souvent un petit
geste dans le même plan. **Jamais une nouvelle phrase** : les phrases changent au rythme de leur
lecture, pas du tempo. **Jamais un recadrage ajouté** pour qu'il se passe quelque chose : ce qui
vit pendant la lecture, c'est ce que la phrase montre.

- Cale le plan sur une **grille de tempo** : 120 battements par minute, un temps = 0,5 s. Les
  événements tombent sur les temps (ou les demi-temps pour une rafale). La musique s'y posera.
- Pendant qu'un texte se lit, il reste immobile, **mais le monde autour vit** : la caméra dérive
  lentement, les objets flottants bougent, le curseur approche, un compteur tourne.
- Une tenue sans rien autour ne dépasse jamais 1 s. Seul l'écran final se tient (3 s ou plus),
  et même lui garde un peu de vie (objets qui dérivent).
- Rafales : une liste d'éléments arrive en cascade de 0,05 à 0,13 s d'écart, jamais un par un à
  une seconde d'intervalle.
- **Le milieu de la vidéo s'essouffle** (de la démo à la preuve) : vise 1,3 événement par seconde
  et aucun creux de plus de 2 s (`rythme` liste les plus longs). Comble-les par de petits
  événements réels, chacun avec son bruitage : un flash quand le vrai résultat apparaît, une
  pastille qui confirme (« Description prête »), une carte de plus qui arrive, un trait qui
  s'allonge sous un chiffre tenu. Léger : le spectateur ne doit pas le remarquer, seulement ne
  pas s'ennuyer.

Piège (essai du 03/11/2026) : un mot qui change seulement de couleur, une ligne qui se tape en
petit dans une barre, une carte gris clair sur blanc ne comptent pas pour `rythme` (l'image change
trop peu) ; le premier rendu tombait à 0,83 événement par seconde. Une graisse qui bascule
sur un grand titre non plus (essai du style 2 du 06/11/2026) : un surlignage plein, oui. Un logo
au trait fin ou des mots qui s'allument comptent à peine ; une capture qui se pose, un logo plein,
une page qui défile par paliers comptent (essai du style 4).

**Un `rythme` trop bas se corrige par un événement de contenu, jamais par la caméra** : un vrai
logo qui arrive, un compteur qui tourne, l'interface qui réagit (une coche, une bulle, une carte
de plus), une vraie capture qui glisse, le mot clé surligné d'un bloc plein, un fond qui bascule
avec sa cause. Un recadrage sec ajouté sur chaque mot passe le contrôle et fabrique une vidéo
agitée qu'on ne lit plus : c'est la mécanique de la story refusée du 06/11/2026 (« beaucoup trop
rapide »). Si une phrase n'a rien à montrer pendant sa tenue, c'est le script ou le repérage qui
manque de matière ([style.md](style.md), « Aucune image inventée »), pas la caméra.

## Lire d'abord : les mots suivent la lecture

- Sans voix, un plan porte **un mot héros** (1 à 3 mots) et au besoin **une ligne d'appui** (3 à
  6 mots), 8 au plus, et la vidéo entière au plus un mot à lire par seconde
  ([ecriture.md](ecriture.md)). Tout le reste se **montre** : une interface qui agit, un schéma qui
  se trace, un objet, un compteur, un avant / après, la vraie vidéo.
- Tenue minimale : **0,3 s par mot + 0,8 s, jamais moins de 1,5 s** (`studio_motion.py lecture
  "<phrase>"`), l'écran final 3 s. Une phrase de 8 mots reste environ 3,2 s : c'est la vitesse
  d'un inconnu qui lit sur son téléphone, pas celle de l'auteur qui connaît déjà le texte. Une
  phrase qui accompagne une démonstration reste plus longtemps, le temps que le geste se fasse.
- Une seule phrase à lire à la fois : la suivante n'entre qu'après la sortie de la précédente (ou
  la remplace mot à mot sur la même ligne).
- Deux graisses : la partie d'appui en léger et grise, le mot qui compte en gras (« Ton nouveau
  **monteur** »). Un mot clé peut être surligné à la couleur de la marque.
- Un mot ne glisse pas pendant qu'on le lit. Une fois lisible, il peut **jouer ce qu'il dit** :
  il claque, s'étire, se barre, se surligne, se change sur place (« Ton lien. » devient « Tes
  vidéos. »), ses lettres tombent en rafale. C'est un geste du mot, d'une demi-seconde, pas un
  déplacement : il reste à sa place et lisible.
- Le dernier mot d'une phrase reste au moins 0,6 s avant la coupe, et une phrase d'accroche reste
  entière à l'écran au moins 2 s : retour du client du 03/11/2026 (« il réfléchit » coupé à peine
  tapé, « qui vendent ton offre » arrivé trop tard). Avec une voix, un texte peut arriver un peu
  avant son mot ; jamais partir avant que la voix ait fini la phrase.

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
- **Pendant qu'une phrase se lit** (de la fin de son entrée à sa sortie), la caméra ne fait
  qu'une **dérive lente** : 2 à 6 % d'échelle ou quelques dizaines de pixels sur toute la tenue,
  `sine.inOut`. Jamais de recadrage sec, de coup de zoom ni de saut de cadre sous un texte qu'on lit.
- **Les cinq premières secondes se lisent sur une image stable** : aucun recadrage sec. L'accroche
  peut entrer par la caméra (un recul qui la révèle, une mise au point, ses mots un à un) : c'est son
  apparition ; une fois lisible, elle ne bouge plus que lentement.
- Un **recadrage**, c'est la caméra qui change de cadre sur ce qui est déjà là. Le passage à ce qui
  suit (un raccord d'objet, un volet, un filé vers la scène suivante) n'en est pas un : il arrive
  quand la phrase a été lue.
- Entre deux intentions (une phrase sort, la suivante arrive), elle **recadre vite** (0,6 à 0,9 s,
  `expo.inOut`) : elle s'approche du geste (le champ où l'on tape, le bouton qu'on clique), elle
  recule sur le résultat. Un clic peut donner un petit coup de caméra, jamais pendant la lecture
  d'une phrase posée.
- Pour zoomer sur un point P avec une échelle s, déplace la caméra de (centre − P) × s.
- Profondeur de champ : les objets très proches et très lointains sont flous, le sujet est net.
  Pendant un grand chiffre, ce qui est derrière passe au flou et s'assombrit.

## Les transitions : un objet devient le suivant

Peu de coupes franches. Les procédés qui marchent, du plus fort au plus simple (les recettes de
« Le langage du motion design », [recettes.md](recettes.md), en donnent le détail) :

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
5. **La coupe** (`K.tranche`) : un trait de son accent fend l'écran en biais, les deux moitiés
   tombent et découvrent le plan suivant. Une fois ou deux par vidéo, sur un temps fort.
6. **La vignette qui devient la vidéo** : une petite image (un format dans un schéma, un fichier
   prêt) grandit jusqu'au plein écran ; à l'arrivée, la vraie vidéo joue, avec pour première image
   exactement cette vignette.
7. **Le fil rouge qui mène au suivant** : le point de sa couleur parcourt un lien qui se trace et
   allume l'objet d'arrivée (`K.lien`, `K.trace`, `K.longer`).
8. **Les volets en biais** entre deux vraies vidéos plein écran : un panneau de son accent, incliné,
   traverse l'écran et le couvre à l'instant de la coupe (une vidéo ne se fend pas : elle vit à la
   racine d'`index.html`).
9. **La coupe franche** sur un temps fort de la musique, rarement.

Jamais de fondu enchaîné entre deux mises en page chargées (double exposition boueuse). Une
couleur qui disparaît s'efface par un volet net (`scaleY` vers 0), pas par une transparence.

## Le motif qui revient

Une vidéo longue a besoin d'un geste qui revient et structure : le spectateur reconnaît qu'on
passe à la partie suivante. Deux motifs du kit : **le fil rouge** (le point de sa couleur, le même
d'un bout à l'autre : il raye, il parcourt les liens, il devient le point final de l'appel), et
**le chapitre** (`K.chapitre`). Un mot géant et
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
