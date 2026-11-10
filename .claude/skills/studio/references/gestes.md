# Le carnet de gestes : des idées à piocher, rangées par besoin

Quand un plan manque d'idée, ouvre la section de ce qu'il doit faire (accrocher, faire lire le mot
fort, prouver, montrer l'interface, annoncer une nouveauté, passer au plan suivant, finir) et
prends **un** geste, retravaillé avec ses objets à lui. Un geste par plan : un film qui les
enchaîne tous ressemble à un catalogue. Rien ici n'est obligé, et rien ne passe avant les
[interdits](interdits.md) (aucun chiffre hors de `OFFRE.json`, la marque par `var(--brand-*)`) ni
le [mouvement](metier.md) (« Les courbes et les durées »).

Durées en secondes, pour 30 images/s. Les fonctions `K.*` sont dans [kit.md](kit.md) ; les
passages déjà décrits (raccord d'objet, plongée, coupe, flash, volet…) dans [metier.md](metier.md),
« Les passages ».

## L'accroche : la première seconde

| Geste | Quand | Comment |
|---|---|---|
| **Le plan déjà en mouvement** | toute ouverture | la première image est prise au milieu d'un geste (une poussée de caméra à mi-course, une fenêtre qui finit d'arriver) : `fromTo` dont l'état de départ est déjà avancé, qui finit en 0,6 s `expo.out`. La première image montre le sujet (`first_frame_empty`) |
| **Le mot trop grand qui se pose** | une promesse en deux ou trois mots | `K.claque(tl, mot, 0, {de: 2.4, duree: 0.6})` : le mot déborde du cadre, net, et se range à sa taille |
| **Le détail qui recule** | sa page, son interface | la caméra part collée à un détail lisible (un bouton, un chiffre de sa page, ×3) et recule jusqu'à l'écran entier en 0,9 s : `K.zoom` et `K.courbeEchelle(3, 1, "power3.inOut")` |
| **La question tapée** | un outil qui répond, une IA | sa vraie question se tape dans un vrai champ (`K.taper`), le curseur envoie (`K.clic`), la réponse arrive : l'accroche est déjà la démonstration |
| **L'iris depuis un objet déjà là** | une révélation dès l'ouverture | un cercle (`clip-path: circle()`) s'ouvre depuis un objet visible, le point du logo, un bouton, un avatar, jusqu'au plein cadre en 0,5 s `power3.in` |
| **La basse retenue** | un Reel qui s'ouvre sur une musique | rien de lourd avant la révélation : le premier geste fort tombe sur l'entrée de la batterie (`calage` la repère) |

## Le mot fort : chaque ligne arrive à sa façon

Les entrées toutes prêtes du kit : `K.entreeMots`, `K.claque`, `K.taper`, `K.decoder`,
`K.rouleau`, `K.permuter`, `K.assembler`, `K.ouvrir`, `K.tranches`, et pour le mot qui agit,
`K.etire`, `K.barre`, `K.surligner`. Deux lignes qui se suivent n'entrent pas de la même façon.

| Geste | Quand | Comment |
|---|---|---|
| **Le surligneur qui marche** | une phrase dont un seul mot compte | chaque mot dans son `span` ; un bloc de l'accent s'ouvre derrière le premier (`K.surligner`), se referme par la droite (`scaleX: 0`, `transformOrigin: "100% 50%"`, 0,1 s) quand le suivant s'ouvre, et se gare sur le mot clé. 0,12 s par mot |
| **Les coins de sélection** | un mot ou un chiffre qu'on désigne | quatre coins en L (traits de 4 px de l'encre ou de l'accent), écartés de 40 px, se resserrent sur le mot en 0,35 s `power3.out`, comme un outil de design qui sélectionne ; ils peuvent sauter au mot suivant |
| **Le mot chaud qui refroidit** | la fin d'une phrase | le dernier mot arrive dans l'accent, puis passe à l'encre en 0,6 s `power2.out` (`color: K.jeton("--brand-text")`) : l'œil le lit en dernier |
| **La vague de couleur** | une ligne déjà posée qu'on relance | `K.lettres`, puis chaque lettre passe à l'accent et revient (0,25 s aller, 0,35 s retour), décalées de 0,025 s : une vague traverse la ligne |
| **Le trait à la main** | un chiffre, un mot à souligner | un soulignement ou un cercle tracé à main levée (un chemin SVG un peu irrégulier) qui se dessine en 0,4 s (`K.trace`, `power2.inOut`) |
| **Deux lignes, deux tailles** | une promesse avec sa précision | la ligne forte très grande, la seconde petite et nette dessous (`K.apparition`) : l'écart de taille fait la hiérarchie, pas un effet |

## La preuve : des chiffres qui se lisent

Chaque chiffre vient de `OFFRE.json`, avec sa source.

| Geste | Quand | Comment |
|---|---|---|
| **Le chiffre géant, l'étiquette minuscule** | une statistique, un résultat | le chiffre remplit la largeur, son étiquette en 30 à 40 px à côté ; il compte en 0,9 s `expo.out` (`K.compteur`) |
| **Le compte qui accélère puis saute** | un volume (inscrits, ventes, heures gagnées) | `K.compteur` jusqu'aux deux tiers sur `power4.in` (0,8 s), puis le total d'un coup (`K.claque` sur le chiffre final) |
| **Les cases qui se remplissent** | une proportion, une progression | une grille de petites cases (10 × 10 pour un pourcentage) qui se remplissent dans l'ordre de lecture, en rafale (0,01 s par case) ; la part se lit sans légende |
| **La courbe qui se trace** | une évolution | le chemin SVG se dessine en 1,2 s `power2.inOut` (`K.trace`), un point de l'accent le mène (`K.longer`), la valeur finale apparaît au bout |
| **Le compteur à rouleaux** | un chiffre rond, un prix | une bande de chiffres par position qui défile dans sa fenêtre : [kit.md](kit.md), « Les pièges » |

## L'interface qui agit

| Geste | Quand | Comment |
|---|---|---|
| **La boîte d'abord, le contenu ensuite** | toute fenêtre ou carte qui arrive | la boîte se pose (0,5 s `expo.out`), son contenu entre 0,1 à 0,15 s après, ligne par ligne (`K.apparition` avec `decalage: 0.05`) |
| **L'appui** | un bouton qu'on clique | le bouton s'enfonce (`scale: 0.96`, 0,08 s), tient 0,05 s, revient (0,2 s `power2.out`), avec `K.clic` sur le curseur |
| **Les étapes qui se cochent** | un outil qui travaille pour lui (une IA, une automatisation) | une liste d'étapes : chacune tourne (un petit cercle en rotation), puis devient une coche tracée (`K.trace`, `longueur: 30`) ; la suivante démarre quand la précédente est cochée |
| **Le squelette remplacé** | un chargement | des barres grises arrondies à la place du texte, puis le vrai contenu prend leur place, ligne par ligne (0,05 s d'écart) |
| **Le code en encre, la couleur après** | un outil de développeur | le code se tape d'une seule couleur (`K.taper`), la coloration arrive 0,2 s après la fin de la ligne |
| **Le petit carré qui se déplie** | une carte, une fenêtre qui naît | un carré de 40 px paraît d'abord, puis se déplie à la taille de la carte (`clip-path: inset(… round …)`, 0,45 s `power3.inOut`), le contenu ensuite |
| **La notification floue qui se précise** | une notification, un message reçu | elle arrive de 40 px au-dessus avec 12 px de flou qui se dissipe en 0,35 s (`K.notification`) |

## La nouveauté : une vidéo de mise à jour

| Geste | Quand | Comment |
|---|---|---|
| **Le changement sur place** | une option, un état, un réglage | l'interface ne bouge pas : seul ce qui change change (un interrupteur, une étiquette par `K.permuter`, une couleur), sous le curseur qui l'a fait |
| **Seul le dernier mot change** | « Disponible sur Mac » → « … et sur Windows » | la phrase tient, son dernier mot permute (`K.permuter`) ou défile (`K.rouleau`) |
| **Le nouveau pousse, les anciens reculent** | une liste, un fil, un historique | le nouvel élément entre en tête (0,45 s `expo.out`), les autres descendent d'un cran et rapetissent un peu (`scale: 0.96`), en même temps |
| **Le petit glissement, puis le grand saut** | un redimensionnement, une montée en gamme | l'objet grandit à peine (5 %, 0,15 s `power1.in`), puis saute à sa taille finale (0,5 s `expo.out`) |
| **Le produit fixe, le monde qui change** | plusieurs nouveautés à la suite | le produit reste au centre, à la même place ; derrière lui, le fond change à chaque nouveauté, par un volet net |
| **Le choisi grandit, les autres s'effacent** | une fonction parmi d'autres | une grille de fonctions ; celle qu'on présente grandit vers le centre pendant que les autres s'estompent et reculent (0,6 s `power3.inOut`) |

## Les passages qui manquent à « Les passages »

| Geste | Quand | Comment |
|---|---|---|
| **Le titre qui s'ouvre sur l'image** | du mot à la démonstration | le titre se remplit de l'image suivante (`background-clip: text` sur sa capture), puis grandit au-delà du cadre (`K.courbeEchelle`, 0,7 s) : on est dans l'image |
| **La fente derrière la ligne** | d'une phrase à sa preuve | une fente de la hauteur du texte s'ouvre derrière la ligne sur le plan suivant, puis s'élargit au plein cadre (`clip-path: inset()`, 0,5 s `power3.inOut`) |
| **Les portes** | une révélation | les deux moitiés de l'écran s'écartent comme des portes (0,45 s `power3.in`), la carte suivante monte au milieu |
| **Le passage dans le flou** | deux plans sans objet commun | tout le cadre passe au flou (0 à 24 px, 0,15 s), le plan change dans le flou, le nouveau revient net (0,25 s) |
| **L'image sautée dans un zoom** | une poussée rapide | dans une poussée de caméra, une seule image saute du plan au suivant, au même grossissement : le zoom porte la coupe |
| **Le fond qui s'éteint** | une sortie de scène | le fond s'assombrit ou se vide d'abord, le sujet part en dernier |

## La fin : la marque qui ramasse le film

| Geste | Quand | Comment |
|---|---|---|
| **Le logo serré qui recule** | une fin de film | le logo plein cadre, serré, recule jusqu'à sa place dans le bloc final (`K.courbeEchelle`, 0,8 s `power3.inOut`) pendant que le nom et l'appel entrent |
| **Le nom qui sort du logo** | un logo avec son nom | le nom glisse de derrière le symbole, masqué par lui (0,5 s `expo.out`) |
| **L'accent retenu** | un film d'encre et de gris | l'accent de la marque n'apparaît qu'au moment où le logo se pose : la couleur arrive avec lui |
| **Le logo en trois temps** | une fin sur la musique | le logo passe de fantôme (15 % de gris) à l'encre, puis à ses couleurs, un temps fort par étape |
| **Le logo trop grand qui se règle** | une fin courte | le logo arrive coupé par le cadre, ×2,2, et se pose à sa taille (0,6 s `expo.out`) |
