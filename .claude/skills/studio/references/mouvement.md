# Le mouvement : lecture, rythme, caméra, raccords

Ce qu'on voit est dans [image.md](image.md) ; ici, comment ça bouge. Les réglages chiffrés
viennent de films de lancement mesurés image par image (dont ceux d'HyperFrames, licence
Apache-2.0) : ce sont des défauts par défaut, qu'une vidéo de référence du client ou un moment voulu
peuvent changer pour leur plan.

## La lecture : les mots suivent l'œil d'un inconnu

- Sans voix, un plan porte **un mot héros** (1 à 3 mots) et au besoin **une ligne d'appui** (3 à
  6 mots) : 8 au plus, et la vidéo entière **au plus un mot à lire par seconde**
  ([ecriture.md](ecriture.md)). Tout le reste se montre.
- **Tenue** : 0,8 s + 0,3 s par mot, jamais moins de 1,5 s (`studio_motion.py lecture`) ; une
  phrase d'accroche reste entière au moins 2 s, le dernier mot d'une phrase au moins 0,6 s avant la
  coupe, l'écran final 2,5 s ou plus. Une phrase qui accompagne une démonstration reste le temps du
  geste. `check` signale un texte parti trop tôt (`line_unread`).
- Une seule phrase à lire à la fois : la suivante entre après la sortie de la précédente, ou la
  remplace mot à mot sur la même ligne.
- **Un texte posé ne bouge plus** tant qu'on le lit : ni glissement, ni zoom lent, ni respiration.
  La vie vient de ce qu'il montre (l'interface qui agit, un compteur, un objet qui arrive) et du
  monde derrière. Si la caméra dérive pendant une tenue, les mots vivent hors de la caméra, dans
  leur propre calque au-dessus d'elle.
- Une fois lisible, un mot peut **jouer ce qu'il dit** : un geste d'une demi-seconde sur place (il
  claque, s'étire, se barre, se surligne, se change), puis il se tient.
- Avec une voix : un texte peut arriver un peu avant son mot, jamais partir avant que la voix ait
  fini la phrase.

## Le rythme : des vitesses qui contrastent

- Les coupes et la révélation s'appuient sur les repères mesurés du morceau (`son.md`) ; une pause
  musicale sert une attente ou un arrêt volontaire. Avec une voix, les gestes suivent ses mots.
- **Autour des mots, il se passe toujours quelque chose** : un objet qui arrive, un curseur qui
  clique, une coche, un compteur qui tourne, l'interface qui répond, un fond qui bascule avec sa
  cause. Le contrôle `rythme` mesure le MP4 rendu : au moins 0,7 événement par seconde, 1,2 s au
  plus d'écart médian, aucune image vraiment immobile plus de 1,5 s avant l'écran final. C'est un
  plancher, pas un but.
- **Contraste les vitesses** : une rafale (une liste en cascade, 40 à 80 ms d'écart ; des plans de
  0,13 à 0,8 s), puis une démonstration qui tient un même cadrage 5 à 8 s pendant que l'interface
  agit ; des plans de 1,8 à 3 s en moyenne, jamais tous de la même durée. Avant une révélation (le
  résultat, le prix), une pause de 0,3 à 0,75 s : c'est voulu, ce n'est pas un creux.
- Cale les événements sur une grille de tempo : à 120 battements par minute, un temps = 0,5 s.
  Calcule chaque temps depuis son numéro (n × 60 / BPM), sans additionner des valeurs arrondies.
  Coupe sur le temps, change la mise en page sur la mesure.
- **Un `rythme` trop bas se corrige par un événement de contenu**, jamais par la caméra : un vrai
  logo qui arrive, l'interface qui réagit, une carte de plus, une vraie capture qui glisse, un mot
  clé surligné d'un bloc plein. Si un plan n'a rien à montrer pendant sa tenue, c'est le script ou
  le repérage qui manque de matière. Ne comptent presque pas : un mot qui change seulement de
  couleur, une graisse qui bascule, une ligne tapée en petit, une carte gris clair sur blanc.
- Le milieu d'une vidéo (de la démo à la preuve) s'essouffle : aucun creux de plus de 2 s.

## La grammaire des mouvements

- **Une courbe par rôle, jamais la même partout** : une arrivée se pose sur une longue traîne
  (`expo.out`, `power4.out`) ; la caméra et un fond qui change de couleur accélèrent et freinent
  (`power2.inOut`, `expo.inOut`) ; une traversée ou une sortie accélère (`power3.in`). Le même
  `power2.out` de 0,5 s sur tout est ce qui fait « vidéo générée ». Vitesse constante seulement pour
  une tête de lecture, une barre de progression, une rotation.
- **Durées** : un mouvement rapide dure 0,3 à 0,6 s ; une entrée 0,4 à 0,7 s ; une sortie 40 à 50 %
  plus courte que son entrée, d'un seul geste (jamais glisser, s'arrêter, puis partir). Trop sèches,
  les entrées ressemblent à des bugs.
- **Chevauchement** : l'élément suivant part quand le précédent en est à 30 à 50 %. Tout à la suite
  fait robot, tout ensemble fait bon marché. Décalages : une lettre par image, les mots de 60 à
  120 ms, les éléments d'une liste de 40 à 80 ms.
- **Ressorts** : un léger dépassement sur un objet d'interface qui arrive (`back.out(1.4)` à
  `back.out(2)`), jamais sur l'opacité ni la couleur, jamais sur un titre ni sur un bouton.
- **Varie les entrées des titres** dans une même vidéo, jamais un fondu qui monte pour chacun :
  - mot par mot, un flou de 6 px qui se dissipe et l'opacité qui monte en 0,13 s, 0,067 s d'écart,
    sans déplacement ;
  - mot par mot, du gris clair à l'encre, sans déplacement ;
  - la ligne entière qui sort du flou (8 px vers 0 en 0,13 à 0,2 s) ;
  - lettre par lettre pour un nom (`K.lettres`), 0,03 à 0,1 s d'écart ;
  - le mot qui claque, plein, en se posant de plus grand (`K.claque`) ;
  - un mot de la phrase qui défile comme une machine à sous avant de se poser (0,1 s par tour).
  Sortie : flou et fondu de 0,13 à 0,25 s, ou le mouvement de la scène.
- **Flou de bougé** : un mouvement rapide porte un flou dans son sens (6 à 12 px sur un texte, 15 à
  20 px plein cadre), au plus fort au milieu du geste. Pour une vidéo qui bouge vite,
  `data-motion-blur="on"` (et `data-motion-blur-shutter="180"`) sur `#root` d'`index.html` le
  calcule au rendu, puis `npm run check`. Posé seulement sur la racine d'une scène, il ne s'applique
  pas (constaté le 08/11/2026 : aucune ligne `[motion-blur]` dans le journal du rendu). Le journal
  doit dire `tier=capture` : un `backface-visibility: hidden` dans une scène en 3D le fait passer en
  `filter` (flou allégé, rotations et zooms seulement adoucis) ; pour retourner une carte, échange
  ses deux faces à 90° plutôt que de cacher la face arrière.
- **Ce qui fait « généré »** : des boucles qui respirent, flottent ou pulsent à la place d'un
  mouvement ; un titre qui continue de glisser ou de grossir une fois posé ; une poussée lente en
  fin de scène ; une onde à chaque clic ; chaque scène qui entre de la même façon ; des oscillations
  sur ce qu'on lit ; un tremblement de caméra.

## La caméra : elle voyage entre les plans

- Chaque scène vit dans un espace en perspective (`k-scene3d` > `k-camera` du kit). Entre deux
  plans, la caméra **voyage** : elle s'approche du geste (le champ où l'on tape, le bouton qu'on
  clique), plonge dans l'objet, recule sur le résultat, glisse vers l'objet suivant (0,6 à 0,9 s,
  `expo.inOut` ou `power2.inOut`).
- **Pendant qu'un texte se lit**, pas de recadrage, de coup de zoom ni de saut de cadre ; au plus
  une dérive lente du monde derrière les mots (2 à 6 % sur toute la tenue, `sine.inOut`), les mots
  restant immobiles dans leur calque.
- **Les cinq premières secondes se lisent sur une image stable** : l'accroche peut entrer par la
  caméra (un recul qui la révèle), puis elle ne bouge plus.
- Un recadrage, c'est la caméra qui change de cadre sur ce qui est déjà là ; un passage à la scène
  suivante (raccord d'objet, volet, filé) n'en est pas un.
- Pour zoomer sur un point P avec une échelle s, déplace la caméra de (centre − P) × s.
- Profondeur de champ : très proche et très loin sont flous, le sujet est net. Pendant un grand
  chiffre, ce qui est derrière passe au flou et s'assombrit.

## Les transitions : un objet devient le suivant

Trois à cinq sortes par vidéo, chacune causée par quelque chose à l'écran ; au plus un tiers de
coupes franches entre les plans ; jamais de fondu enchaîné entre deux mises en page chargées.

| Transition | Comment |
|---|---|
| **Le raccord d'objet** | l'objet de fin d'une scène est l'objet de début de la suivante, à la même place et à la même taille |
| **L'objet devient le monde** | une carte ou une pastille grandit au-delà du cadre en 0,65 s (`power2.inOut`), ses coins s'arrondissent moins, ce qui l'entoure se floute ; le nouveau contenu apparaît pendant qu'elle grandit |
| **La traversée d'un bouton** | la caméra va au bouton (0,6 s, avec flou), puis il passe de 8 % à 250 % du cadre en 0,35 s (`power3.in`) ; sa couleur devient l'image suivante |
| **Le flash ou l'iris depuis le clic** | le curseur clique, un disque de sa couleur part du point cliqué et couvre l'écran (`K.flash`, ou `clip-path: circle()` en 0,15 s) |
| **Le report** | le résultat rétrécit (1 → 0,6, flou au milieu du geste) et se pose dans l'écran suivant, qui se construit autour |
| **Le volet** | un panneau d'une autre couleur pousse la moitié de l'écran (avant / après) ou remplace le fond ; une couleur qui disparaît s'efface par un volet net, jamais par transparence |
| **La coupe** | un trait de l'accent fend l'écran en biais, les deux moitiés tombent (`K.tranche`) ; une ou deux fois par vidéo, sur un temps fort |
| **La vignette qui devient la vidéo** | une petite image grandit jusqu'au plein écran et la vraie vidéo joue, avec pour première image exactement cette vignette |
| **Le fil conducteur** | le point de sa couleur parcourt un trait qui se trace et allume l'objet d'arrivée (`K.lien`, `K.trace`, `K.longer`) |
| **La coupe franche** | sur un temps fort de la musique, au moment le plus rapide d'un mouvement, avec le même sens et la même vitesse des deux côtés ; l'image sortante peut s'assombrir de 40 % sur 3 images |

Une coupe se fait en plein mouvement, jamais sur deux images arrêtées. Garde **un sens dominant**
dans la vidéo (par exemple de droite à gauche) ; les autres sens disent quelque chose (monter =
révéler, reculer = arriver au résultat).

## Le motif qui revient

Une vidéo de plus de 30 s a un geste qui revient et structure : **le fil conducteur** (le même point
de sa couleur d'un bout à l'autre : il raye, il parcourt les liens, il devient le point final de
l'appel) ou **le chapitre** (`K.chapitre` : un mot géant et pâle qui glisse en fond, l'étiquette
nette dit la fonction, le curseur active un interrupteur, on plonge dans la démonstration). Deux à
cinq chapitres dans une vidéo de page, un ou deux dans un Reel.

## Gestes et interfaces

Un produit en action : **état avant → le curseur approche → clic → l'interface réagit → état
obtenu**, sans pause morte. Le clic précède la réaction ; la pointe du curseur est son point actif ;
on tape par petits groupes de lettres (`K.taper`), en moins d'une seconde pour une phrase courte.
Ce que le produit produit sort de la fenêtre en aperçus qui flottent : la profondeur et la densité
viennent de là. Un clic dans un nouvel écran est un raccord : le nouvel écran arrive un peu grand et
se pose.

## La fin

Elle ramasse le film et donne le geste : tout ce qu'on a vu revient en mosaïque puis se resserre en
un bouton que le curseur clique ; ou le produit se pose avec son nom et l'appel ; ou le fil
conducteur devient le point final de la phrase d'appel. Le nom et l'appel se tiennent au moins
2,5 s. En page de vente, la fin désigne le bouton sous la vidéo ; en pub, « Découvre-le » et une
flèche vers le bas, sans dessiner de bouton.

## Ce que le client dit, ce qu'on change

| Il dit | Change |
|---|---|
| « trop rapide » | ralentis les zooms et les déplacements à 0,7 fois leur vitesse, et allonge les tenues qui tombent sous la lecture ; rien d'autre |
| « accélère » | accélère le contenu et raccourcis le plan d'autant ; les plans suivants avancent |
| « les titres bougent » | pose-les, puis tiens-les immobiles jusqu'à leur sortie |
| « on dirait des slides » | entre dans le plan suivant par un objet à l'écran ; coupe un mouvement en plein vol ; montre la matière en grand |
| « on dirait des sous-titres » | retire des mots : un mot héros par plan, le reste se montre |
