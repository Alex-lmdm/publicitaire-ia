# Les repères du métier

Une boîte à outils, pas un mode d'emploi : des chiffres mesurés sur des films de lancement (dont
ceux d'HyperFrames, licence Apache-2.0) et sur nos vidéos, à consulter quand tu hésites. Ce sont
des défauts par défaut : un moment voulu, un style ou une vidéo de référence peuvent les changer
pour leur plan, jamais les interdits ([interdits.md](interdits.md)).

## Le cadre

- **Le sujet remplit le cadre** : au moins 40 % de la largeur ou de la hauteur. Un petit élément au
  milieu d'un grand fond n'est pas un plan : approche la caméra, agrandis, ou donne-lui un monde
  (des cartes autour, sa page derrière, ses résultats en éventail). `cadre` relève ces instants sur
  le MP4.
- **Une interface se montre de près** : ses mots utiles à 28 px au moins (`check` :
  `text_below_floor`) ; ses micro-textes non lus sont de la texture (`data-layout-ignore`).
- **Une fenêtre d'interface occupe au moins les deux tiers de l'écran et déborde d'un bord** (elle
  sort du cadre à droite, en bas), jamais posée au milieu du vide, hors plan large bref. Cinq façons
  de rater une interface reconstruite : trop chargée (tout le logiciel au lieu du geste du plan), un
  squelette gris (des barres à la place des mots : interdit), une capture rétrécie collée en petit,
  plate (face caméra, figée), sans la couleur de sa marque.
- Pas tout au centre : décentré, sorti d'un bord, coupé par le cadre quand c'est voulu ; des
  échelles qui contrastent (un mot géant à côté d'une étiquette, un objet proche et d'autres loin).
- **En vertical, on recompose** : le sujet s'empile en hauteur et grandit (interface en carte
  verticale, téléphone au centre, mots empilés plus gros) ; jamais une mise en page 16:9 rétrécie.
  Les autres formats d'une même vidéo sont des mises en page, jamais des recadrages.

## La typographie

| Rôle | Mots | Taille en 9:16 (en 16:9, à proportion de la hauteur de 1080) |
|---|---|---|
| le **mot héros** | 1 à 3 | il remplit 60 à 90 % de la largeur de sa colonne (130 à 400 px) |
| la **ligne d'appui** | 3 à 6 | 56 à 72 px |
| les **étiquettes** posées sur ce qu'on montre | 1 à 4 | 30 à 40 px, jamais sous 28 px |

Deux tons : le plein et l'accent (« Ton **lien.** »), ou le gris d'appui et le plein. Un contour net
(`k-contour`) pour doubler un mot plein, jamais une lueur ; un texte plein, jamais en dégradé ; la
frappe au clavier seulement dans un champ de saisie. Des étiquettes de fonction en blocs empilés
(`k-blocs`) à côté de l'interface qui le fait.

**La lecture, en détail** : une phrase d'accroche reste entière 2 s au moins ; le dernier mot d'une
phrase 0,6 s au moins avant la coupe ; l'écran final 2,5 s ou plus ; une seule phrase à lire à la
fois (la suivante entre quand la précédente sort, ou la remplace sur la même ligne). `check`
signale un texte parti trop tôt (`line_unread`).

## Les courbes et les durées

- **Une courbe par geste, et peu de gestes** : un film garde deux ou trois façons de bouger, les
  mêmes d'un bout à l'autre. Une arrivée se pose sur une longue traîne (`expo.out`, `power4.out`) ;
  une traversée ou une sortie accélère (`power3.in`) ; la caméra et un fond qui change accélèrent
  et freinent (`power2.inOut`, `power3.inOut`). Vitesse constante seulement pour une tête de
  lecture, une barre de progression, une rotation.
- **Presque aucun rebond** : un objet d'interface qui arrive (une fenêtre, une carte, un bouton, une
  pastille) dépasse sa place de 1 à 4 %, `back.out(0.6)` à `back.out(1)` ; un texte, jamais (il se
  pose net) ; la caméra, presque pas. Au-delà, tout paraît en caoutchouc et plus rien n'a l'air
  précis : `back.out(2)` dépasse de 13 %, `back.out(3)` de 25 % (le dépassement de `back.out(s)`
  vaut 4s³ / 27(s+1)²). Jamais de rebond sur l'opacité ni la couleur.
- **Deux horloges** : l'interface de son produit bouge à sa vraie vitesse, 100 à 300 ms (un menu, un
  onglet, une coche, un bouton qui réagit ; Linear anime en 100 et 160 ms, Vercel en 100 et 150) ;
  le film bouge à la sienne, 0,4 à 0,9 s (les mots, les objets, la caméra, les passages). Une
  interface qui s'ouvre en 0,6 s paraît fausse ; un titre qui entre en 0,15 s paraît un bug.
- **La durée suit la distance** : 0,3 s pour un petit pas, 0,6 à 0,9 s pour une traversée de
  l'écran. Une sortie est 40 à 50 % plus courte que son entrée, d'un seul geste.
- **Un meneur et des suiveurs** : dans un groupe, un élément part le premier, les autres réagissent
  après lui avec des écarts inégaux (40, 70, 55 ms… tirés par `K.rng`), jamais en file régulière ;
  le suivant part quand le précédent en est à 30 à 50 %. Décalages : une lettre par image ; les mots
  d'un titre qui se construit d'un bloc, 33 à 40 ms ; 60 à 120 ms seulement pour des mots qu'on lit
  un à un ; les éléments d'une liste, 40 à 80 ms.
- **La boîte se pose, puis le texte entre** : un texte ne change jamais en même temps que la boîte qui
  le porte. L'ancien sort, la boîte change de taille ou de place, le nouveau entre une fois la boîte
  posée (le premier signe d'une animation générée, sinon).
- **Le mot fort, puis des lignes nettes** : le mot fort du plan a son entrée travaillée (masque,
  lettres, machine à sous, claque…), différente d'un plan à l'autre ; les lignes d'appui et les
  étiquettes apparaissent nettes (un fondu de 0,15 à 0,2 s, sans montée ni flou).
- **Un seul foyer dans une interface** : le curseur et ce qu'il touche bougent, le reste se tient.
- **Le flou de bougé** : réglé sur `#root` d'`index.html` (`data-motion-blur="on"`,
  `data-motion-blur-shutter="180"`) ; le journal du rendu dit s'il s'est appliqué (les pièges :
  [kit.md](kit.md)).

## Le rythme

- Les coupes et la révélation s'appuient sur les repères mesurés du morceau ([son.md](son.md),
  « Construire l'image sur la bande-son ») ; avec une voix, les gestes suivent ses mots. À 120
  battements par minute, un temps = 0,5 s : calcule chaque temps depuis son numéro (n × 60 / BPM).
- **Des vitesses qui contrastent** : une rafale (40 à 80 ms d'écart, des plans de 0,13 à 0,8 s),
  puis une démonstration qui tient un même cadre 5 à 8 s pendant que l'interface agit ; des plans
  de 1,8 à 3 s en moyenne, jamais tous de la même durée ; avant une révélation, une pause de 0,3 à
  0,75 s ; aucun creux de plus de 2 s au milieu de la vidéo.
- `rythme` mesure le MP4 : au moins 0,7 événement par seconde, 1,2 s au plus d'écart médian, aucune
  image immobile plus de 1,5 s avant l'écran final. C'est un plancher. **Un rythme trop bas se
  corrige par un événement de contenu** (un logo qui arrive, l'interface qui réagit, une carte de
  plus), jamais par la caméra. Ne comptent presque pas : un mot qui change seulement de couleur, une
  ligne tapée en petit, une carte gris clair sur blanc.

## Les passages

Un objet devient le suivant ; chaque passage a une cause à l'écran. Des façons de faire, à varier :

| Passage | Comment |
|---|---|
| **Le raccord d'objet** | l'objet de fin d'une scène est celui du début de la suivante, à la même place et à la même taille |
| **L'objet devient le monde** | une carte grandit au-delà du cadre (0,65 s, `power2.inOut`), ses coins s'arrondissent moins, ce qui l'entoure se floute ; le nouveau contenu apparaît pendant qu'elle grandit |
| **Le bouton qui envahit l'écran** | un calque plein de sa couleur, découpé par `clip-path: inset(… round …)` à la taille exacte du bouton, s'ouvre au plein écran en 0,2 s (`power2.in`) puis se referme sur l'objet suivant (une barre d'adresse) ; les mots posés dessus et dessous changent de couleur sous son bord |
| **La carte qui se retourne** | `rotationY` de 0 à 180 ; à 90°, la face avant se cache et la face arrière se montre (`tl.set` d'opacité), sans `backface-visibility` |
| **La fenêtre qui pivote** | la fenêtre tourne (`rotationY` vers 85°) et sort, l'objet suivant (le téléphone) entre en pivotant de l'autre côté avec le même contenu remis en page |
| **La plongée** | la caméra fonce dans un écran (`scale` 3 et plus, `ease: K.courbeEchelle(1, 3, "power3.in")`, avec flou) ; on ressort de l'autre côté dans la scène suivante |
| **Le flash ou l'iris depuis le clic** | un disque de sa couleur part du point cliqué et couvre l'écran (`K.flash`, ou `clip-path: circle()`) |
| **Le report** | le résultat rétrécit et se pose dans l'écran suivant, qui se construit autour |
| **Le volet** | un panneau d'une autre couleur pousse la moitié de l'écran ou remplace le fond, net, jamais par transparence |
| **La coupe** | un trait de l'accent fend l'écran en biais, les deux moitiés tombent (`K.tranche`), sur un temps fort |
| **La vignette qui devient la vidéo** | une petite image grandit jusqu'au plein écran et la vraie vidéo joue, avec pour première image exactement cette vignette |
| **Le fil conducteur** | un point de sa couleur parcourt un trait qui se trace et allume l'objet d'arrivée (`K.lien`, `K.trace`, `K.longer`) |
| **La coupe franche** | sur un temps fort, au moment le plus rapide d'un mouvement, avec le même sens et la même vitesse des deux côtés |

Au plus un tiers de coupes franches entre les plans (`rythme` compte les coupes nues). Garde un sens
dominant dans la vidéo ; les autres sens disent quelque chose (monter = révéler, reculer = arriver
au résultat). Une couleur qui disparaît s'efface par un volet net.

## La caméra

- Chaque scène vit dans un espace en perspective (`k-scene3d` > `k-camera`). `K.zoom` calcule
  l'échelle et le déplacement qui amènent un point de la scène au centre (ou ailleurs), et `K.vu`
  dit où ce point se trouve à l'écran une fois la caméra posée, pour y mener le curseur
  ([kit.md](kit.md)).
- Un voyage entre deux cadres : 0,5 à 0,9 s, `power2.inOut` ou `power3.inOut` (leur vitesse culmine
  à 2 ou 3 fois la moyenne ; celle d'`expo.inOut`, à 7 fois : un à-coup). Une approche du geste :
  ×1,2 à ×1,4, assez pour que les mots de l'interface se lisent, sans couper ce que le geste vise.
- **Pas de yo-yo** : avancer puis reculer jusqu'au même cadre sans que rien n'ait changé, ou revenir
  à son point de départ, défait ce qu'on vient de montrer. La caméra va quelque part ; un recul
  montre autre chose (le résultat, l'ensemble qui a changé), sinon il ne se fait pas.
- **Une échelle qui paraît régulière** : un zoom ou une plongée animés en ligne droite semblent
  ralentir en grandissant (de ×1 à ×2 frappe plus que de ×3 à ×4). `K.courbeEchelle(de, a,
  "power2.inOut")` anime le logarithme de l'échelle ([kit.md](kit.md)).
- Les cinq premières secondes se lisent sur une image stable : l'accroche peut entrer par la caméra
  (un recul qui la révèle), puis elle se tient.
- Profondeur de champ : très proche et très loin sont flous, le sujet net ; pendant un grand
  chiffre, ce qui est derrière passe au flou et s'assombrit.

## Les fonds et les logos

- Le fond change quand le film change de temps (le nom de l'offre, un chapitre, le prix, un avant /
  après), avec une cause visible (un clic, un volet, un objet qui grandit). Ceux du kit : la nuit à
  grille fine, le clair à grille, l'aplat de l'accent, l'écran coupé.
- Des logos qui flottent seulement quand la scène parle de leur outil : les vrais logos nus
  (`K.logoNu`), 6 à 8, en vraie profondeur (petits au loin, moyens nets, un ou deux grands et flous
  devant), jamais collés aux mots ni dans la bande du sticker. Sans logo pertinent, pas de champ.

## Les objets connus

Ce que son public reconnaît d'un coup d'œil garde son vrai visage. Le kit en a déjà :

| Le plan parle de… | Dans le kit |
|---|---|
| un dossier, un fichier, un document | `K.ic("objet-dossier")` (le dossier bleu du Mac), `objet-pdf`, `objet-doc`, `objet-tableur`, `objet-presentation`, `objet-video`, `objet-image`, `objet-audio`, `objet-zip`, `objet-fichier` |
| un outil, une app, un moyen de paiement | son vrai logo (`studio_motion.py logos`, 7 432 marques), nu ou en icône d'app |
| son téléphone, une notification, un message | `k-tel`, `K.statut`, `K.notification`, `K.bulle` |
| une fenêtre d'ordinateur | `k-fenetre` et ses `k-feux` |

Les autres se construisent en HTML ou en SVG d'après leur allure courante ou une capture : une
plateforme (le post Instagram, la page de paiement Stripe, la boîte de réception) d'après une vraie
capture ; un objet de son métier (la montre et ses anneaux, l'annonce immobilière et son prix au m²,
le ticket de commande, la carte d'embarquement, la facture, la timeline de montage) d'après son
allure. Une icône d'un seul trait (Lucide) seulement pour une idée sans objet connu (une coche, une
flèche, un euro). `palette` connaît les couleurs du kit et des logos posés ; celles d'un objet
construit restent signalées, et la revue vérifie que ce sont les siennes.

## La fin

Elle ramasse le film et donne le geste : ce qu'on a vu revient et se resserre en un bouton que le
curseur clique ; ou le produit se pose avec son nom et l'appel. Le nom et l'appel se tiennent
2,5 s au moins, et la dernière image porte la marque en grand (son logo, son nom) et bouge encore :
jamais une petite carte figée sur un grand fond. En page de vente, la fin désigne le bouton sous la vidéo ; en pub, « Découvre-le »
et une flèche vers le bas, sans dessiner de bouton.

## Ce que le client dit, ce qu'on change

| Il dit | Change |
|---|---|
| « trop rapide » | ralentis les déplacements et la caméra à 0,7 fois leur vitesse, et allonge les tenues qui tombent sous la lecture ; rien d'autre |
| « accélère » | accélère le contenu et raccourcis le plan d'autant ; les plans suivants avancent |
| « les titres bougent » | pose-les, puis tiens-les immobiles jusqu'à leur sortie |
| « on dirait des slides » | entre dans le plan suivant par un objet à l'écran, coupe un mouvement en plein vol, montre la matière en grand |
| « on dirait des sous-titres » | retire des mots : un mot héros par plan, le reste se montre |
