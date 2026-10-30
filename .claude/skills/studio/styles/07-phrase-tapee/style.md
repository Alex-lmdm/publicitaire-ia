# Template n°7 · Phrase tapée · d'après Zaro (https://x.com/ZaroAI_/status/2070084796378747316)

**Ce qu'on voit :** des phrases courtes qui se tapent sur deux lignes derrière un gros curseur de
frappe à la couleur de la marque, en alternance avec des interfaces claires et nettes (une barre de
demande, une fenêtre, des cartes blanches) ; des icônes d'outils et des fichiers éparpillés qui se
changent en points, puis l'offre au centre d'orbites où tournent ses outils, et une galaxie
d'autres systèmes quand la caméra recule.
**Souvent utile pour :** lancer un logiciel ou une formation, montrer « tout ce qui tourne autour »
d'une offre (ses outils, ses modules, ses bonus).

**D'après :** X · Zaro · vidéo de lancement · 68 s · 16:9 (1920 × 1080, 30 images/s).
**Mesures de l'original (`studio_motion.py reference`) :** 1,56 événement par seconde, écart
médian 0,30 s entre deux événements, 16 coupes franches (presque toutes avec un changement de
fond), 4,4 s d'image figée au total. Musique à 104 battements par minute (un temps toutes les
0,58 s), un silence net à 4,5 s puis l'entrée franche à 5,0 s.
**Mesures de l'essai du kit** (4 scènes, marque LMDM, 28,5 s) : 1,08 événement par seconde, écart
médian 0,50 s, aucune image figée, `rythme` « ok ».

> On reprend la grammaire de la vidéo (phrases tapées, alternance des fonds, interfaces claires,
> objets éparpillés, orbite, galaxie, point final), jamais son contenu : ni ses textes, ni son logo,
> ni son produit, ni les logos d'applis qu'elle montre, ni sa musique. Tout passe aux couleurs et
> aux polices de la marque du client, et ce sont SES outils qui gravitent.

## 1. Le rythme

- **Une phrase, puis une preuve à l'écran, en alternance.** Chaque idée tient en deux lignes tapées
  (3 à 6 mots) sur un fond uni, puis une coupe franche montre la chose dans une interface claire.
  Une coupe toutes les 4 s en moyenne, presque toujours avec un changement de fond.
- **La frappe donne la cadence :** une ligne tapée en 0,7 à 0,9 s, la seconde aussitôt après, un ou
  deux clignements du curseur, coupe. Dans les interfaces, un geste toutes les 0,3 à 0,5 s (une carte qui
  tombe, un clic, une icône qui surgit).
- **Un silence avant le nom** (0,3 à 0,5 s de vide, musique coupée), puis l'entrée franche sur le mot
  géant.
- **Chez toi :** grille de 0,5 s ; garde les tenues de lecture vivantes (les mots qui s'allument
  bondissent un peu, les orbites tournent et les outils « se connectent » un par un, la poussière de
  pixels scintille) : l'essai a dû les ajouter pour ne laisser aucune image figée.

## 2. La structure

| Scène de l'original (temps approximatifs) | Rôle | Ce qui s'y passe | Dans le kit |
|---|---|---|---|
| 0 → 2,5 s | accroche | une phrase mot à mot sur fond presque noir, avec deux objets glissés dans la ligne (une vignette qui change, une pastille avec son curseur en pixels) | `t7-accroche` |
| 2,5 → 4,5 s | accroche | la suite de la phrase ; ses mots s'allument tour à tour à la couleur d'accent ; poussière de pixels | `t7-accroche` |
| 4,5 → 8,5 s | nom | un silence ; un mot géant tapé sur un nuage de la couleur d'accent ; coupe sur fond clair : le logo devient net, le nom sort | `t7-accroche` |
| 8,5 → 13 s | solution | deux lignes tapées sur le taupe ; coupe : la barre de demande où la phrase se tape, clic sur envoyer | `t7-phrase` |
| 13 → 20 s | démonstration | la fenêtre du produit se construit ; une relance tapée dans le chat | `t7-phrase` (la fenêtre) |
| 20 → 28 s | fonction | deux lignes tapées, des pastilles en pixels avec leurs curseurs ; une carte de liste entourée de contours en écho | non construit |
| 28 → 39 s | preuve | glisser-déposer dans un tableau, des graphiques ; « simple / puissant » en écran coupé sombre et clair, un schéma de flux | non construit |
| 39 → 44 s | problème rangé | une grande phrase retapée trois fois ; à chaque fin, des icônes d'applis, des notes et des fichiers surgissent ; tout se change en points ; la conclusion en écriture de points | `t7-eparpille` |
| 44 → 59 s | démonstration | les fichiers, les connexions, une grande question tapée, la réponse, la liste des sources qui défile, le téléphone | non construit |
| 59 → 65 s | promesse | la carte du produit DANS une phrase ; orbites en pointillés, outils qui tournent ; recul sur une galaxie de systèmes, conclusion tapée | `t7-orbite` |
| 65 → 68,5 s | appel | coupe sur fond clair : un point d'encre se contracte et devient le logo ; pastille d'appel en capitales | `t7-orbite` |

Pour une vidéo de page (60 à 90 s) : `t7-accroche` → `t7-phrase` → (une démonstration de ton
produit dans la même fenêtre claire) → `t7-eparpille` → (une preuve) → `t7-orbite`. Pour un Reel :
`t7-phrase` → `t7-orbite`.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Avec la marque du client |
|---|---|---|
| Noir chaud | l'ouverture, la galaxie | `--t7-nuit` : le fond de la marque assombri (86 % fond, 14 % noir) |
| Taupe chaud | les phrases tapées sur deux lignes, l'orbite | `--t7-taupe` : le fond de la marque mêlé de 20 % de son gris. LMDM : graphite |
| Blanc cassé chaud | les interfaces, les objets éparpillés, le logo | `--t7-clair` : blanc cassé teinté de 5 % du fond de la marque |
| Lavande | le curseur de frappe, les mots qui s'allument, le nuage du mot géant, la pastille d'appel | `var(--brand-accent)`, texte posé dessus en `var(--brand-contrast)` |
| Gris clair | la 2e ligne d'une phrase | `--t7-gris` : le texte de la marque à 55 % sur le taupe |
| Encre | texte sur fond clair, bouton d'envoi, point final | `--t7-encre` : le fond de la marque assombri |
| Blanc pur | cartes, barre de demande, fenêtres | blanc, ombres douces |

**Quatre fonds qui alternent par coupe franche** (noir, nuage de couleur, clair, taupe) : c'est la
respiration du look, comme le veut le studio. Sur fond clair, l'accent ne sert qu'en **aplat** (le
nuage, la pastille, une vignette) : jamais en texte ni en trait fin, illisible avec un accent clair
(jaune) ; le curseur de frappe y passe à l'encre.

## 4. La typographie

- **Police :** une grotesque neutre à l'espacement très serré, moyenne (500) pour les phrases,
  demi-grasse (600) pour le nom. La marque n'impose rien : **Inter Tight** (libre ; ou Inter à
  −4,5 %). Dans le kit : `var(--brand-font-display)` pour les phrases (`--t7-police`),
  `var(--brand-font-body)` pour les interfaces. L'écriture en points : la même police passée au
  crible d'une trame de points (pas de police en plus ; **Doto**, libre, si on veut la vraie).
- **Casse et alignement :** casse de la phrase, un point final à chaque phrase ; deux lignes
  empilées serrées, la première pleine, la seconde grise ; centré. Espacement −4,5 %. La pastille
  d'appel en capitales espacées de 14 % (une police à chasse fixe si la marque en a une :
  `--t7-police-pastille`).
- **Le curseur de frappe** est une barre épaisse (7 % de la taille du texte, 82 % de sa hauteur).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Phrase d'ouverture avec ses objets | 104 px | 92 px, sur deux lignes |
| Suite qui s'allume | 116 px | 100 px |
| Mot géant sur le nuage | 270 px | 200 px |
| Deux lignes tapées | 124 px | 96 px |
| Demande dans la barre | 40 px | 40 px × 0,74 |
| Grande phrase retapée | 136 px | 112 px, à la ligne |
| Écriture en points | 150 px | 96 px |
| Phrase autour de la carte | 96 px | 96 px, au-dessus et au-dessous |
| Conclusion sur la galaxie | 104 px | 76 px |
| Nom (sans logo) | 150 px au plus, ajusté à sa longueur | ~105 px pour 15 lettres |
| Pastille d'appel | 30 px | 30 px |

## 5. Les mouvements signature

1. **La phrase tapée sur deux lignes** (`t7-phrase`, et le mot géant de `t7-accroche`, la
   conclusion de `t7-orbite`) : frappe par petits groupes de lettres (`K.taper`), une ligne en
   0,75 s, la seconde 0,3 s après ; le curseur de frappe passe à la ligne suivante ; un
   clignement de 0,2 s, coupe.
2. **Les objets dans la ligne** (`t7-accroche`) : les mots montent un à un (0,3 s d'écart, 0,45 s,
   expo.out, flou 8 px → 0) ; la vignette et la pastille surgissent dans la phrase (back.out(2.2)) ;
   la vignette change toutes les 0,45 s avec un petit rebond ; puis les mots de la suite s'allument
   tour à tour à la couleur d'accent (0,32 s d'écart) en sautant de 14 px.
3. **La demande envoyée** (`t7-phrase`) : la demande se tape en 0,85 s, les logos empilés surgissent
   (0,08 s d'écart), le curseur clique sur envoyer (enfoncement 0,08 s, back.out(3)), la barre
   s'envole (0,45 s, power3.in), la fenêtre arrive floue et un peu trop claire (0,7 s, expo.out), sa
   barre latérale (0,04 s d'écart) puis ses cartes tombent (0,12 s d'écart, back.out(1.6)).
4. **Le désordre réduit en points** (`t7-eparpille`) : la phrase se tape, s'efface lettre à lettre
   et se retape (trois fins en 2,4 s) ; à chaque fin, un groupe d'objets surgit en profondeur (0,07 s
   d'écart, back.out(1.7)), quelques-uns flous ; puis chaque objet passe en points (trame de 10 px)
   et file vers le centre en rétrécissant (0,7 s, power3.in) ; la conclusion apparaît en écriture
   de points dans un cadre de points.
5. **L'orbite et la galaxie** (`t7-orbite`) : trois cercles en pointillés s'ouvrent autour de la
   carte (0,7 s, expo.out, 0,14 s d'écart), les objets surgissent dessus (0,035 s d'écart) ; chaque
   anneau tourne à sa vitesse (100°, −64°, 38° sur la scène, sine.inOut) et les objets restent
   droits ; les outils « se connectent » un par un (liseré d'accent, 0,3 s d'écart) ; la caméra
   recule de ×1,08 à ×0,36 en 1,6 s (expo.inOut) sur huit autres systèmes, le fond fonce, tout passe
   au flou (5 px) pendant que la conclusion se tape.
6. **Le point d'encre** (`t7-orbite`) : coupe sur fond clair, un point qui se contracte et se
   déforme (0,55 s), devient le logo (ou s'efface s'il n'y en a pas) ; le nom sort de derrière lui
   (0,6 s, expo.out) ; la pastille se dévoile de gauche à droite (0,45 s) ; la poussière de pixels
   apparaît dans les coins.

## 6. Les transitions

- **Dans l'original :** la coupe franche sur un temps de la musique, presque toujours avec un
  changement de fond (noir → nuage → clair → taupe → clair…). À l'intérieur d'une scène : la barre
  qui recule pour laisser venir la fenêtre, les objets qui se défont en points, le recul sur la
  galaxie avec flou, le point qui devient le logo. Aucun fondu enchaîné.
- **Dans le kit :** les coupes sont dans les scènes (nuit → nuage → clair dans `t7-accroche`, taupe →
  clair dans `t7-phrase`, nuit → clair dans `t7-orbite`) et entre elles, toujours sur un temps et
  avec un changement de fond : `t7-accroche` finit sur le clair du nom, `t7-phrase` commence sur le
  taupe ; `t7-phrase` finit sur la fenêtre claire, `t7-eparpille` reste clair mais change de
  cadrage ; `t7-eparpille` finit sur l'écriture en points, `t7-orbite` commence sur le taupe.

## 7. Le produit à l'écran

- **Dans l'original :** la vraie interface du logiciel, en clair, reconstruite à grande échelle
  (barre latérale, tableaux, cartes), des cartes extraites (une liste, les sources), et la barre de
  demande qui le pilote. Le produit est la carte au centre de l'orbite.
- **Chez toi :** la barre de demande montre ce qu'on demande vraiment à son produit (ou la question
  que se pose son client) ; la fenêtre montre **sa vraie interface** (`R.capture` : une capture dans
  `assets/images/`, sinon le squelette du kit) ; la carte de l'orbite porte son offre (une capture,
  son nom, une ligne vraie, son contenu réel) ; les logos sont ceux des outils que l'offre utilise
  vraiment, posés par `studio_motion.py logos` (montrés ici comme des icônes d'applis, sur une tuile
  blanche ou translucide) ; les autres systèmes de la galaxie sont ses autres modules, bonus ou
  offres.

## 8. Le son

- **Dans l'original :** une électro-pop entraînante vers 104 par minute, 4,5 s d'introduction, un
  silence net puis l'entrée franche sur le mot géant (5,0 s) ; une pulsation forte et régulière
  (chaque temps marqué) ; un passage plus calme pendant la recherche dans les fichiers ; fondu sur
  le logo.
- **Chez toi :** ambiance « Lancement énergique » ; entrée franche calée sur le mot géant
  (`musiques prendre … --a <instant du nuage>`), et un silence de la musique calé sur le noir que le
  kit laisse juste avant (4,7 → 4,85 s de `t7-accroche`). Bruitages, un par geste : frappe de clavier par groupe (pas une
  par lettre) sur chaque phrase tapée, petits pops pour les objets de la ligne et les objets
  éparpillés, clic sur envoyer, souffle quand la fenêtre arrive, grain numérique quand tout passe en
  points, souffle long sur le recul de la galaxie, un impact doux sur le logo.

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** fond presque noir, poussière de pixels, la phrase mot à mot avec
  ses deux objets dans la ligne, puis la suite dont les mots s'allument. Lisible dès 0,5 s.
- **La fin :** le point d'encre sur fond clair qui devient le logo, le nom, la pastille d'appel en
  capitales sur l'accent, tenue 1,7 s avec la poussière qui scintille dans les coins. En page de
  vente, la pastille reprend le texte du bouton situé sous la vidéo.

## Ce qui ne se fera pas à l'identique

- **Les logos d'applis de l'original** → ceux des outils du client (`studio_motion.py logos`) ; une
  marque absente des registres se demande au client, jamais redessinée.
- **Les icônes en pixel-art et les pastilles en points avec leurs curseurs** (la scène des
  « agents ») → seulement la pastille de l'ouverture et son curseur en pixels.
- **La police matricielle** → la police de la marque vue à travers une trame de points (même effet de
  loin, lettres pleines de près).
- **Les tons chauds** (brun, taupe, grège) → dérivés du fond de la marque : graphite et blanc cassé
  froid pour LMDM.
- **La lavande sur fond clair** (curseur, liserés) → l'accent seulement en aplat sur le clair.
- **La police à chasse fixe de la pastille** → la police de la marque en capitales espacées.
- **La galaxie** (des dizaines de systèmes en vraie profondeur) → huit systèmes dans un même plan et
  un flou d'ensemble.
- **Les scènes d'interface en action** (relance dans le chat, tableau glissé, graphiques, écran coupé,
  schéma de flux, fichiers, liste des sources qui défile, téléphone) : non construites dans le kit ;
  elles se refont avec les mêmes briques (fond clair, cartes blanches, barre de demande, phrase
  tapée, coupe franche).

## Sur une autre offre

C'est un look : il se monte sur n'importe quelle offre. Ce qui suivait le logiciel s'adapte.

- **Formation :** la phrase d'ouverture dit ce que contient l'offre (« Des vidéos [vignette] et des
  [pastille] modèles ») ; la barre porte la question que se pose l'élève ; la fenêtre montre l'espace
  de formation (vraie capture) ; les objets éparpillés sont le désordre de son sujet (notes, idées,
  fichiers, outils) ; l'orbite met la formation au centre, ses outils et ses modules autour.
- **Coaching :** la phrase dit l'accompagnement ; la barre, la question du client ; la fenêtre, le
  plan ou l'agenda réel ; l'orbite met le coaching au centre, ses séances, ses outils et ses
  ressources autour.
- **Logiciel :** le plus proche de l'original : la barre pilote le produit, la fenêtre est sa vraie
  interface, les objets éparpillés sont les outils qu'il relie, l'orbite montre ses intégrations.
- **Toujours :** les phrases tapées en deux lignes derrière le curseur de couleur, l'alternance des
  quatre fonds par coupe franche, les interfaces claires, le désordre réduit en points, l'orbite et
  la galaxie, le point d'encre qui devient le logo.

## En vertical et en carré

- **9:16 (essayé sur `t7-accroche` et `t7-orbite`) :** passe la racine de la scène à 1080 × 1920.
  La phrase d'ouverture passe seule sur deux lignes ; l'orbite est à ×0,74, les mots se placent
  au-dessus et au-dessous de la carte, les autres systèmes surtout en haut et en bas ; le nom
  s'ajuste à sa longueur.
- **9:16, `t7-phrase` et `t7-eparpille` (prévu dans le code, pas encore essayé) :** les deux lignes
  à 96 px, la barre à ×0,74 et la fenêtre à ×0,7 ; les objets éparpillés se répartissent au-dessus
  et au-dessous de la phrase, qui passe à la ligne. Regarde les images clés avant de livrer.
- **4:5 et 1:1 :** même règle (racine à 1080 × 1350 ou 1080 × 1080) ; garde les trois anneaux dans le
  cadre et au moins un tiers de l'image libre autour de la phrase éparpillée.

## Les compositions du kit

Chaque scène est une sous-composition 16:9 prête à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Tout ce qui change d'une
offre à l'autre est dans l'objet `R` en tête du script ; les couleurs ne viennent que de
`var(--brand-*)`. Les logos nommés (`logo-claude`…) doivent d'abord être posés dans le projet par
`studio_motion.py logos <projet> <noms>` : un nom absent prend une icône neutre, à remplacer.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (objet `R`) |
|---|---|---|---|
| `compositions/t7-accroche.html` | 7,2 s | la phrase mot à mot avec une vignette et une pastille dans la ligne, la suite qui s'allume, le silence, le mot géant tapé sur le nuage de couleur, le logo et le nom sur fond clair | les morceaux de la phrase (`[carte]` et `[pastille]` placent les objets), les mots gris, les icônes de la vignette, les mots de la pastille, la suite, le mot géant, le logo (`brand/logo.svg`, "" sans logo), le nom |
| `compositions/t7-phrase.html` | 6,6 s | deux lignes tapées sur le taupe ; la barre de demande tapée, les logos empilés, le clic sur envoyer ; la fenêtre du résultat qui se remplit | les deux lignes, la demande, les 3 logos, le titre et le sous-titre de la fenêtre, les icônes des vignettes, la capture de son produit |
| `compositions/t7-eparpille.html` | 5,2 s | une grande phrase retapée trois fois, les notes, fichiers et icônes d'outils qui surgissent, tout qui se change en points, la conclusion en écriture de points | le début et les trois fins, les notes, les puces, les fichiers, 6 à 8 logos d'outils, la conclusion |
| `compositions/t7-orbite.html` | 9,6 s | la carte de l'offre dans la phrase, les trois orbites et les outils qui tournent, le recul sur la galaxie, la conclusion tapée, le point d'encre, le logo, le nom, la pastille d'appel | les deux morceaux de la phrase, la carte (nom, ligne, bas, capture), les logos, les deux étiquettes, les autres systèmes, la conclusion, le logo, le nom, l'appel (avec sa vraie adresse) |

Identifiants préfixés `t7a`, `t7p`, `t7e`, `t7o` : si tu montes deux fois la même scène, change le
préfixe partout dans la copie.
