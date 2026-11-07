# Style n°7 · Phrase tapée · d'après Zaro (https://x.com/ZaroAI_/status/2070084796378747316)

**Ce qu'on voit :** des phrases courtes qui se tapent derrière un gros curseur de frappe à la
couleur de la marque, en alternance avec des interfaces claires et nettes (une barre de demande,
une fenêtre où arrive sa vraie matière) ; ses captures, les logos de ses outils et quelques mots
éparpillés autour d'une phrase retapée, qui se rangent d'un coup en rangs nets ; puis l'offre au
centre d'orbites où tournent ses outils, et ses autres modules quand la caméra recule.
**Souvent utile pour :** lancer un logiciel ou une formation, montrer « tout ce qui tourne autour »
d'une offre (ses outils, ses modules, ses bonus).
**D'après :** X · Zaro · vidéo de lancement · 68 s · 16:9.

## 1. Le rythme

- **Une phrase, puis une preuve à l'écran, en alternance.** Chaque idée tient en une phrase tapée
  (une ou deux lignes, 8 mots au plus) sur un fond uni, puis une coupe franche montre la chose dans
  une interface claire. Une coupe toutes les 4 s en moyenne, presque toujours avec un changement de
  fond.
- **La frappe donne la cadence :** une ligne tapée en 0,7 à 0,9 s, la seconde aussitôt après, puis
  la phrase se tient le temps de sa lecture avant la coupe (2 s au moins pour l'accroche ;
  [mouvement.md](../../references/mouvement.md), « La lecture »). Les
  scènes calculent ces tenues et leur durée (`D` dans le script, à reporter en `data-duration`).
  Dans les interfaces, un geste toutes les 0,3 à 0,5 s (une carte qui tombe, un clic, un logo qui
  surgit).
- **Un silence avant le nom** (0,3 à 0,5 s de nuit vide, musique coupée), puis l'entrée franche sur
  le mot géant.
- **Chez toi :** grille de 0,5 s. Une phrase posée ne bouge plus : la vie vient de ce qu'elle
  montre (ses mots qui s'allument, la vignette qui change d'image, sa page jointe qui défile, la
  matière qui surgit autour de la phrase retapée, les orbites qui battent) ; s'il en manque, de la
  vraie matière qui bouge, jamais un recadrage.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| La phrase et ses objets | une phrase mot à mot avec une vignette (ses vraies images qui défilent) et une pastille glissées dans la ligne ; la suite s'allume mot à mot à l'accent | accroche, promesse | `t7-accroche` |
| Le mot géant sur l'aplat | un silence, un mot géant tapé sur l'aplat plein de l'accent, puis le logo net et le nom sur fond clair | le nom de l'offre, temps fort | `t7-accroche` (fin) |
| La phrase sur deux lignes | deux lignes tapées sur l'ardoise derrière le gros curseur de couleur, leurs mots qui s'allument, coupe franche | toute phrase clé, titre de chapitre | `t7-phrase` (début) |
| La demande envoyée | une demande tapée dans une barre, sa vraie page jointe au-dessus, les logos de ses outils empilés, le clic sur envoyer, la fenêtre du résultat qui se remplit de ses vraies images | solution, démonstration de son interface | `t7-phrase` |
| Le désordre rangé | une phrase retapée trois fois, sa matière (captures, logos, quelques mots) qui surgit autour ; tout file vers le centre et se range d'un coup en rangs nets, la conclusion tapée à la place de la phrase | le problème rangé, ce qu'on remplace | `t7-eparpille` |
| L'orbite et le recul | la carte de l'offre dans la phrase, puis au centre de trois orbites où tournent ses outils et ses captures, qui se connectent ; le recul sur ses autres modules, la conclusion tapée | promesse, outils et intégrations, ce qu'on reçoit | `t7-orbite` |
| Le point d'encre | sur fond clair, un point qui se contracte et devient le logo, le nom qui sort, la pastille d'appel | appel, fin | `t7-orbite` (fin) |

**Pour montrer son produit** : la demande envoyée ouvre une fenêtre claire où arrive sa vraie
matière ; une conversation s'y montre, ses réponses tapées. Une scène d'interface que le kit n'a
pas (un fichier glissé, un tableau, la liste des sources) se construit avec les mêmes briques :
fond clair, cartes blanches, barre de demande, phrase tapée, coupe franche.

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation. Pour une vidéo de page (60 à
90 s) : `t7-accroche` → `t7-phrase` → (une démonstration de son produit dans la même fenêtre
claire) → `t7-eparpille` → (une preuve) → `t7-orbite`. Pour un Reel : `t7-phrase` → `t7-orbite`.

## 3. Les fonds et les couleurs

Les couleurs viennent de sa marque, et seulement d'elle ([image.md](../../references/image.md),
« La palette ») ; ses captures et les logos de ses outils gardent leurs vraies couleurs.

| Rôle dans ce style | Avec la marque du client |
|---|---|
| L'ouverture, le recul de l'orbite | la nuit : `var(--brand-sombre)` |
| Les phrases tapées sur deux lignes, l'orbite | l'ardoise : `var(--brand-gris-1)`, son gris le plus sombre |
| Le mot géant | l'aplat plein `var(--brand-accent)`, le mot en `var(--brand-contrast)` |
| Les interfaces, les objets éparpillés, le logo, la carte et les tuiles de l'orbite | son clair : `var(--brand-clair)`, filets et ombres en noir transparent |
| Le texte sur la nuit et sur l'ardoise | `var(--brand-clair)` |
| Le curseur de frappe, la pastille, les liserés, les orbites qui battent | `var(--brand-accent)` plein, texte posé dessus en `var(--brand-contrast)` |
| Les mots qui s'allument sur la nuit ou l'ardoise | `var(--brand-accent-lisible)` |
| La 2e ligne d'une phrase, les mots d'appui | `var(--brand-gris-4)` sur l'ardoise, `var(--brand-gris-3)` sur la nuit |
| Le texte sur fond clair, le bouton d'envoi, le point d'encre | l'encre : `var(--brand-sombre)` |
| Le trait des orbites | un pointillé fin de blanc transparent |

- **Jamais `var(--brand-bg)` ni `var(--brand-text)` dans ce look** : sur une marque claire, la nuit
  deviendrait claire et le texte noir sur gris.
- **Les mots s'allument d'un coup** à l'accent plein, jamais par un mélange de l'accent et du
  blanc ; les orbites battent en passant d'un coup à l'accent plein ; le recul passe à la nuit (sa
  couleur posée par-dessus l'ardoise) et s'assombrit sous un voile de cette nuit, jamais par un
  filtre sur les couleurs de la marque.
- **Quatre fonds qui alternent par coupe franche** (la nuit, l'aplat de l'accent, le clair,
  l'ardoise) : c'est la respiration du look. Sur fond clair, l'accent ne sert qu'en **aplat** (la
  pastille) : jamais en texte ni en trait fin, illisible avec un accent clair (un jaune) ; le
  curseur de frappe y passe à l'encre.

## 4. La typographie

- **Police :** une grotesque neutre à l'espacement très serré, moyenne (500) pour les phrases,
  demi-grasse (600) pour le nom, grasse (700) pour le mot géant. Dans le kit :
  `var(--brand-font-display)` pour les phrases (`--t7-police`), `var(--brand-font-body)` pour les
  interfaces. La marque n'impose rien : **Inter Tight** (libre) s'en approche.
- **Casse et alignement :** casse de la phrase, un point final à chaque phrase ; deux lignes
  empilées serrées, la première pleine, la seconde grise ; centré ; espacement −4,5 %. La pastille
  d'appel en capitales espacées de 14 % (une police à chasse fixe si la marque en a une :
  `--t7-police-pastille`).
- **Le curseur de frappe** est une barre épaisse (7 % de la taille du texte, 82 % de sa hauteur).
- **Le mot géant et le nom de la fin** (avec son logo, qui prend la hauteur du nom) occupent 60 à
  90 % de la largeur : les scènes calculent leur taille d'après leur longueur.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Phrase d'ouverture avec ses objets | 104 px, pastille 42 px | 92 px, sur deux lignes |
| Suite qui s'allume | 116 px | 100 px, à la ligne |
| Mot géant sur l'aplat | 540 px pour 5 lettres (la moitié de la hauteur au plus) | 314 px pour 5 lettres |
| Deux lignes tapées | 124 px | 96 px |
| Demande dans la barre | 40 px | 50 px, sur deux lignes |
| Adresse de la page jointe ; titre et sous-titre de la fenêtre | 30 px ; 52 et 32 px | 30 px ; 60 et 36 px |
| Grande phrase retapée, conclusion du rangement | 136 px | 112 px, à la ligne |
| Mots en pilule (éparpillés, puis rangés à la taille du plus petit) | 34 à 44 px | 30 à 38 px |
| Phrase autour de la carte | 96 px | 96 px, au-dessus et au-dessous |
| Nom et ligne de la carte (affichés à l'échelle de l'orbite) | 42 et 36 px (36 et 31 px affichés) | 42 et 36 px (34 et 29 px affichés) |
| Étiquettes en orbite | 32 px | 32 px |
| Conclusion sur le recul | 104 px | 84 px |
| Pastille d'appel | 34 px | 34 px |

## 5. Les mouvements signature

1. **La phrase tapée** (`t7-phrase`, le mot géant de `t7-accroche`, les conclusions de
   `t7-eparpille` et `t7-orbite`) : frappe par petits groupes de lettres (`K.taper`), une ligne en
   0,75 s, la seconde 0,3 s après ; le curseur passe à la ligne suivante et clignote ; la phrase se
   tient le temps de sa lecture sans bouger, ses mots s'allument tour à tour à l'accent en
   bondissant de 14 px, puis coupe.
2. **Les objets dans la ligne** (`t7-accroche`) : le premier morceau est là dès la première image,
   les autres montent un à un (0,3 s d'écart, 0,45 s, expo.out, flou 8 px → 0) ; la vignette et la
   pastille surgissent dans la phrase (back.out(2.2)) ; la vignette change d'image d'un coup toutes
   les 0,45 s avec un petit rebond, le petit curseur clique deux fois la pastille ; puis les mots
   de la suite s'allument tour à tour, d'un coup, à l'accent (0,32 s d'écart) en sautant de 14 px.
3. **La demande envoyée** (`t7-phrase`) : la caméra recule sur la barre pendant que la demande se
   tape (×1,18 → 1 en 1 s ; ×1,04 en 9:16), puis ne fait qu'une dérive de 2 % ; sa page jointe se
   dévoile au-dessus et défile, les logos surgissent un à un, le curseur clique sur envoyer
   (back.out(3)), la barre s'envole (0,45 s, power3.in), la fenêtre arrive floue (0,7 s, expo.out),
   puis ses images tombent (0,12 s d'écart, back.out(1.6)) ou sa capture se dévoile (0,8 s).
4. **Le désordre rangé** (`t7-eparpille`) : la phrase se tape, se tient, s'efface lettre à lettre
   et se retape (trois fins, chacune lue) ; à chaque fin, un groupe d'objets surgit en deux salves
   (back.out(1.7), 0,7 s d'écart) et dérive autour d'elle, à une place qui ne couvre ni la phrase
   ni un mot ; captures et logos parfois flous, jamais un mot. Puis la phrase s'efface et tout se
   range d'un coup : chaque objet file vers sa place dans trois rangs nets (captures au-dessus,
   outils puis mots au-dessous ; 0,75 s, power3.inOut), se redresse, devient net et se tasse en se
   posant, pendant que la conclusion se tape à la place de la phrase.
5. **L'orbite et le recul** (`t7-orbite`) : la carte se pose dans la phrase, sa capture se dévoile
   de haut en bas ; les mots s'écartent, trois cercles en pointillés s'ouvrent autour d'elle (0,7 s,
   expo.out) et sa matière surgit dessus : ses outils sur les deux premiers, ses captures (et deux
   étiquettes au plus) sur le dernier, là où l'image a de la place ; une orbite sans objet ne se
   dessine pas. Chaque anneau tourne à sa vitesse (100°, −64°, 30°, sine.inOut), les objets restent
   droits ; les outils « se connectent » un par un (liseré plein de l'accent) et quatre fois les
   orbites et la carte passent d'un coup à l'accent plein (0,16 s). Pendant que la ligne de la carte
   se lit, la carte ne bouge pas : seuls les anneaux poussent lentement (×1,05). Puis ses mots
   s'effacent, la caméra recule à ×0,36 en 1,6 s (expo.inOut) sur ses autres systèmes, le fond passe
   à la nuit, tout passe au flou (6 px) sous un voile de la nuit (55 %), et la conclusion se tape.
6. **Le point d'encre** (`t7-orbite`) : coupe sur fond clair, un point d'encre se contracte et se
   déforme (0,55 s) puis devient le logo (sans logo, pas de point : le nom monte du flou) ; le nom
   sort de derrière lui (0,6 s, expo.out) ; la pastille se dévoile de gauche à droite (0,45 s) ;
   l'écran final se tient 3 s.

## 6. Les transitions

- **La coupe franche sur un temps de la musique**, presque toujours avec un changement de fond
  (nuit → aplat → clair → ardoise → clair…). À l'intérieur d'une scène : la barre qui s'envole pour
  laisser venir la fenêtre, la matière qui se range, le recul avec flou, le point qui devient le
  logo. Aucun fondu enchaîné.
- **Dans le kit :** les coupes sont dans les scènes (nuit → aplat → clair, ardoise → clair,
  ardoise → nuit → clair) et entre elles : `t7-accroche` finit sur le clair, `t7-phrase` commence
  sur l'ardoise et finit sur le clair, `t7-eparpille` reste clair mais change de cadrage,
  `t7-orbite` commence sur l'ardoise.

## 7. Le produit à l'écran

- La barre de demande montre ce qu'on demande vraiment à son produit (ou la question que se pose
  son client) ; la fenêtre montre **sa vraie matière** : ses images du résultat (`cartes`, de vraies
  miniatures, de vraies pages) ou la capture de son produit (`capture`), dans `assets/images/`. Sans
  elles, la fenêtre ne s'ouvre pas : jamais de cartes vides ni de squelette.
- La carte de l'orbite porte son offre (sa capture, sinon son logo, puis son nom et une ligne
  vraie) ; les logos sont ceux des outils que l'offre utilise vraiment, posés par
  `studio_motion.py logos` et montrés comme des icônes d'applis, sur une tuile claire (la grammaire
  de l'original) ; ses autres systèmes sont ses vrais modules, bonus ou offres, ou il n'y en a pas.
- La vignette de l'ouverture et les objets éparpillés sont sa vraie matière : sans elle, la
  vignette se retire et la phrase éparpillée a moins d'objets ; jamais un faux document, un
  caractère ni une forme posés comme objets.

## 8. Le son

- **L'original :** une électro-pop vers 104 par minute, chaque temps marqué, un silence net puis
  l'entrée franche sur le mot géant, un fondu sur le logo.
- **Chez toi :** ambiance « Lancement énergique », proposée à la page des styles et des musiques
  (`musiques choisir --style 7`), jamais imposée (une ambiance qu'il demande passe devant). Entrée
  franche calée sur le mot géant (`musiques prendre … --a <instant de l'aplat>`), et un silence de
  la musique calé sur la nuit que le kit laisse juste avant (0,4 s avant le mot géant de
  `t7-accroche` : 6,2 → 6,6 s avec l'objet `EXEMPLE`).
- **Avec une voix off sur une page** : ambiance « Tech minimale » ou « Premium et calme », la
  musique sous la voix ([son.md](../../references/son.md), « Sous une voix off ») ; la batterie
  entre dans une respiration de la voix avant le nom, jamais sous lui.
- **Bruitages, un par geste :** frappe de clavier par groupe (pas une par lettre) sur chaque phrase
  tapée, petits pops pour les objets de la ligne et les objets éparpillés, clic sur envoyer, souffle
  quand la fenêtre arrive, un glissement quand tout se range, souffle long sur le recul, un impact
  doux sur le logo.

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** la nuit de sa marque, le premier mot déjà là sur la toute
  première image, la phrase qui se pose avec ses deux objets dans la ligne, puis la suite dont les
  mots s'allument. Lisible dès 0,5 s.
- **La fin :** le point d'encre sur fond clair qui devient le logo, le nom, la pastille d'appel en
  capitales sur l'accent, tenue 3 s (l'écran final). En page de vente, la pastille reprend le texte
  du bouton situé sous la vidéo.

## Sur une autre offre

C'est un look : il se monte sur n'importe quelle offre. Ce qui suivait le logiciel s'adapte.

- **Formation :** la phrase d'ouverture dit ce que contient l'offre, la vignette montre ses vraies
  miniatures ; la barre porte la question de l'élève, la fenêtre l'espace de formation ; les objets
  éparpillés sont le désordre de son sujet ; l'orbite met la formation au centre, ses outils et ses
  modules autour.
- **Coaching :** la phrase dit l'accompagnement ; la barre, la question du client ; la fenêtre, le
  plan ou l'agenda réel ; l'orbite, ses séances, ses outils et ses ressources autour du coaching.
- **Logiciel :** le plus proche de l'original : la barre pilote le produit, la fenêtre est sa vraie
  interface, les objets éparpillés sont les outils qu'il relie, l'orbite montre ses intégrations.
- **Toujours :** les phrases tapées derrière le curseur de couleur, l'alternance des quatre fonds
  par coupe franche, les interfaces claires, le désordre rangé, l'orbite et le recul, le point
  d'encre qui devient le logo.

## En vertical et en carré

- **9:16 :** passe la racine de chaque scène à 1080 × 1920, elle se remet en page seule (tailles en
  section 4). Les phrases passent à la ligne à la même taille ; le mot géant et le nom suivent la
  largeur ; la barre de demande prend 1 000 px, la caméra n'y recule que de ×1,04 ; la fenêtre du
  résultat passe en portrait (1 000 × 1 460 px) ; les objets éparpillés se répartissent au-dessus et
  au-dessous de la phrase, leurs rangs passent à la ligne ; l'orbite prend toute la largeur (×0,95),
  la phrase au-dessus et au-dessous de la carte, ses captures tournent en haut et en bas.
- **4:5** (racine à 1080 × 1350) prend la même mise en page verticale. **En 1:1**, les scènes
  gardent leur mise en page 16:9 : vérifie la planche, une phrase trop large passe à la ligne.

## Les compositions du kit

Chaque scène est une sous-composition 16:9 prête à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Ses textes, ses images et
ses noms d'exemple sont dans l'objet `EXEMPLE` en tête du script (chaque champ y est décrit) ; les
couleurs ne viennent que de `var(--brand-*)`. Les logos nommés (`logo-notion`…) se posent d'abord
dans le projet par `studio_motion.py logos <projet> <noms>` : un nom absent est retiré de la scène.
Les images (`assets/images/…`) sont ses vraies captures, miniatures ou photos.

| Fichier | Durée (objet `EXEMPLE`) | Ce qu'elle montre | Ce qu'on remplace dans `EXEMPLE` |
|---|---|---|---|
| `compositions/t7-accroche.html` | 11,2 s | la phrase et ses objets, la suite qui s'allume, le silence, le mot géant, le logo et le nom | `phrase` (ses morceaux ; `[carte]` et `[pastille]` y placent les objets), `gris` (les morceaux gris), `vignettes` (ses vraies images ; `[]` retire la vignette), `pastille` (un mot ; `""` la retire), `suite`, `geant`, `logo` (`brand/logo.svg` ou `.png` ; `""` sans logo), `nom` |
| `compositions/t7-phrase.html` | 12,2 s avec une fenêtre (8,9 s sans) | les deux lignes tapées, la demande envoyée, la fenêtre du résultat | `ligne1` et `ligne2`, `demande`, `logos` (3 au plus), `lien` (`img` : sa page en une ou deux captures, `adresse`), `titre` et `sousTitre` de la fenêtre, `cartes` et leur `format` (ses images du résultat) ou `capture` (la capture de son produit) |
| `compositions/t7-eparpille.html` | 10,1 s (trois fins de 3 mots, une conclusion de 3) | le désordre rangé | `debut`, `fins` (trois), `groupes` (ses logos, ses captures `{ img, format }`, des mots en pilule : 5 au plus sur la scène, ils restent avec la phrase), `fin` (la conclusion) |
| `compositions/t7-orbite.html` | 15,2 s | la carte dans la phrase, l'orbite et le recul, la conclusion tapée, le point d'encre, le nom, la pastille d'appel | `avant` et `apres` (la phrase), `carte` (`nom`, `texte`, `capture`), `logos`, `images` (ses captures en orbite), `etiquettes` (deux mots au plus, ou `[]`), `autres` (ses autres systèmes, de vrais noms, ou `[]`), `conclusion`, `logo`, `nom`, `appel` |

Chaque scène calcule sa durée (`D` dans le script) : reporte-la dans `data-duration`, ici et sur
l'hôte (+0,3 s par mot de plus). Les mots de la carte comptent dans les 8 mots de leur image. Une
phrase du script plus longue que ce qu'une mise en page prend passe sur deux lignes à la même
taille, ou dans une scène construite dans le style.

Identifiants préfixés `t7a`, `t7p`, `t7e`, `t7o` : si tu montes deux fois la même scène, change le
préfixe partout dans la copie.
