# Style n°3 · Verre sombre · d'après Polymarket (https://x.com/Polymarket/status/2095530373274816595)

**Ce qu'on voit :** une vidéo de nuit, dans la couleur la plus sombre de la marque, à peine
éclairée par une lumière blanche en coin ; des phrases nettes posées en grand, leur fin à l'accent,
et surtout une interface en verre sombre inclinée en 3D que la caméra montre partie par partie
pendant qu'un curseur la pilote (un curseur qu'on glisse, un interrupteur, un total qui change, un
bouton cliqué qui se défait en points). L'accent se pose toujours plein : un trait, un
remplissage, un bouton.
**Souvent utile pour :** présenter une offre et son prix, une page de paiement, un logiciel qu'on
pilote ; lancer une nouvelle formule.

## 1. Le rythme

- **Peu de coupes, beaucoup de gestes.** Le rythme vient de la caméra entre deux phrases (recul,
  plongée, passage d'une partie de l'interface à la suivante), des mises au point et des gestes
  dans l'interface : pendant la démonstration, un geste toutes les 0,3 à 0,5 s (le prix tourne,
  une puce s'allume, le curseur glisse, un champ tombe), la caméra posée.
- **Une ouverture lente, puis tout s'accélère** : l'accroche presque silencieuse, l'entrée franche
  de la musique sur le nom de l'offre, la démonstration dense, puis une rafale de cartes.
- **Une fin qui respire** : la musique se coupe, une ligne seule, l'adresse avec un seul impact,
  le logo tenu 3 s. C'est la seule tenue longue.
- **Le tempo** : grille de 0,5 s (120 par minute) ; les scènes du kit déduisent leur durée de la
  lecture de leurs phrases. Sur cette nuit presque nue, une tenue vit de ce que la phrase montre :
  ses vraies captures en verre qui arrivent de la profondeur, le nom qui se remplit de l'accent
  dans sa pastille, la trame qui s'allume. Sans capture, `rythme` voit une image figée : c'est la
  matière qui manque, jamais un recadrage à ajouter.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| La mise au point et le recul | deux mots géants, flous, deviennent nets ; la caméra recule, la phrase se complète, sa fin à l'accent, et se pose à la moitié de la largeur ; elle se tient immobile pendant que ses vraies captures arrivent autour d'elle | accroche, promesse | `t3-onglets` (début) |
| La barre filée et la pastille fixe | une barre d'onglets défile sous une pastille cerclée de l'accent qui reste au centre et se pose sur l'offre | le choix (le problème), la solution qui ressort | `t3-onglets` |
| La plongée et la trame de points | la pastille se remplit de l'accent, on la traverse (un éclair de la couleur pleine) ; l'appel se forme en points, en grand, puis devient net | passage, le nom de l'offre | `t3-onglets` (fin), `t3-cartes` |
| Le verre piloté | une interface en verre sombre, inclinée en 3D, montrée en trois cadrages (un par partie) pendant qu'un curseur la règle ; pour un prix, sa vraie page de paiement, simplifiée | démonstration de son interface, l'offre et son prix | `t3-commande` |
| Le carrousel en gros plan | un mot seul dans sa pastille, puis une rafale de cartes inclinées, une toutes les 0,5 s, leur chiffre dans la tuile de l'accent ; la dernière se pose et se lit | ce qu'on reçoit, preuves chiffrées | `t3-cartes` |
| La fin en silence | le verbe seul dans le silence, la ligne complète, l'adresse et son trait d'accent, le logo et le nom | appel, fin | `t3-fin` |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation. Pour un Reel : `t3-onglets`
(raccourci à la plongée) → `t3-commande` → `t3-fin`.

**Une vidéo de page (16:9, 60 à 120 s) :** les quatre scènes bout à bout font 36 s. La durée vient
de la démonstration, jamais de tenues plus longues : entre `t3-onglets` et `t3-cartes`, refais le
cycle **interface, option, preuve** pour 2 ou 3 fonctionnalités réelles (15 à 20 s par cycle) :
son écran réel dans le même verre et la même caméra, piloté par le curseur (copie de
`t3-commande`, ou une capture dans le verre) ; le réglage qui change le résultat ; la preuve, une
carte de `t3-cartes` posée et lue avec le vrai chiffre. Au-delà d'une minute, ajoute le plein
écran de l'accent sur le prix (section 3). Chaque copie change son préfixe partout (`t3c` →
`t3c2`). Sans fonctionnalité réelle pour un troisième cycle, la vidéo reste plus courte.

## 3. Les fonds et les couleurs

La palette ([interdits.md](../../references/interdits.md), « La palette ») prend ces
rôles :

| Rôle dans le style | Avec la marque du client |
|---|---|
| la nuit, fond de toute la vidéo | `var(--brand-sombre)` |
| la lumière de la scène | du blanc très faible en coin (7,5 % en haut à gauche, 4 % en bas à droite), qui glisse ; jamais un halo derrière un texte |
| le verre (interfaces, cartes, cadres des captures) | une ombre : du noir en transparence (`rgba(0, 0, 0, .42)`), un liseré clair en haut, des reflets blancs fins |
| les surfaces dans le verre (puces, pistes, interrupteur éteint, valeur, premier onglet) | `var(--brand-gris-1)` ; la lame claire et les billes en `var(--brand-clair)` |
| le texte | `var(--brand-clair)` ; inactif `var(--brand-gris-3)`, d'appui `var(--brand-gris-4)` |
| l'accent plein | le cercle de la pastille (2 px), son remplissage, la piste remplie, l'interrupteur, le bouton et ses points, la tuile des cartes, le trait sous l'adresse ; dessus, `var(--brand-contrast)` |
| un mot ou un chiffre à l'accent sur la nuit | `var(--brand-accent-lisible)` |
| la trame de points | des points blancs à 15-25 % |

Le look reste de nuit du début à la fin. Les bascules se font par la lumière qui glisse, la trame
qui s'allume, l'éclair de l'accent quand on traverse le bouton ; une vidéo de plus d'une minute
ajoute un plein écran de l'accent sur le prix. Un code de couleur propre à un sujet
(le vert et le rouge d'une hausse) n'est pas repris.

**Le flou et l'accent.** Un bouton, une pastille ou un mot à l'accent flou ou à demi transparent
sur la nuit vire à l'olive ou au brun (`palette` relève ces images). D'où les réglages du kit :
- l'accent entre et sort par une coupe, un glissé ou un volet ; un texte à l'accent passe au clair
  d'un coup avant de se dissoudre dans le flou, et prend l'accent d'un coup (jamais un fondu de
  couleur) ;
- le flou de vitesse ne touche que la barre d'onglets ; les cartes glissent sans flou ; le bon
  recule sans s'effacer ;
- pas de bande floue de profondeur de champ sur le bon, plein d'accent : sa profondeur vient de
  l'inclinaison, de la perspective et de sa grande ombre ;
- un sélecteur qui glisse est cerclé de l'accent, pas rempli (ses libellés restent lisibles à
  chaque image) ; un mot recouvert par sa pastille pleine s'éteint le temps qu'elle le couvre ;
- ni halo ni lueur sur le texte, le logo ou le bouton ; la vignette reste sous le sujet.

## 4. La typographie

- **Police :** une seule, sans empattement, demi-grasse (600), moyenne (500) pour l'adresse :
  `var(--brand-font-body)` (variable `--t3-police`), Inter si la marque n'impose rien.
- **Casse et alignement :** casse de la phrase, jamais de capitales ; lignes centrées ; interfaces
  alignées à gauche, chiffres à droite. Texte plein, sans lueur.
- **Grand et posé.** Une phrase seule se pose à la moitié de la largeur au moins (en 9:16, ses deux
  morceaux empilés), un mot héros à 60 % (85 % en 9:16) : les scènes le calculent. Le contraste
  d'échelle vient de l'ouverture (les premiers mots énormes) et du prix.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Les mots géants de l'ouverture | ~80 % de la largeur | ~80 % de la largeur |
| La promesse, après le recul | une ligne à 52 % de la largeur (85 px pour 5 mots) | deux lignes à 84 % (jusqu'à 150 px) |
| Les onglets | 75 à 120 px (46 px × zoom 1,6 à 2,6) | 50 à 100 px (barre au plus ×0,85) |
| L'appel « verbe + nom » | 62 % de la largeur (~105 px) | 85 % (~80 px) |
| Le bon : libellés / prix / bouton | 30 à 32 / 112 / 40 px, × 1,22 à 1,46 | mêmes tailles, × 1,02 à 1,22 |
| Le bon : menu, accès, mention | 24 à 26 px, texture (`data-layout-ignore`) | idem |
| Le mot des cartes | 60 % de la largeur | 85 % |
| Les cartes : chiffre / nom | 110 / 88 px ; la carte lue à ~62 % de la largeur | 150 / 104 px (en portrait) |
| La ligne d'appel, l'adresse | 50 à 88 % de la largeur | 80 % |
| Le logo et le nom | 60 % de la largeur | 80 % |

## 5. Les mouvements signature

1. **La mise au point et le recul** (`t3-onglets`, 0 → 2,25 s) : les mots géants, flous de 16 px,
   deviennent nets en 0,45 s (power2.out) ; la caméra recule à une échelle intermédiaire en 0,75 s
   (power3.inOut), la ligne se recentre ; la fin de phrase entre mot à mot, chacun par un volet qui
   monte (0,3 s d'écart au plus), pendant un dernier recul jusqu'à sa taille de lecture. Puis la
   phrase se tient immobile : derrière elle, la trame s'allume et s'élargit (5 %), la lumière
   glisse, ses captures (2 ou 3) arrivent de la profondeur dans le verre, une toutes les 0,6 s,
   autour d'elle (au-dessus et au-dessous en 9:16), jamais dessus. Aucun recadrage.
2. **La barre filée et la pastille fixe** (une fois l'accroche lue) : le premier onglet seul, les
   suivants à 0,17 s d'écart ; la barre défile en 1 s (power3.inOut), flou de vitesse horizontal
   (0 → 18 px → 0), zoom ×1,6 → ×2 ; la pastille cerclée de l'accent apparaît d'un coup au centre,
   s'ouvre en largeur, les onglets passent dessous, elle se pose sur l'offre. La barre qui file est
   de la texture : on lit le premier onglet et celui de l'offre.
3. **La plongée dans le bouton** (1,4 s après la barre) : zoom ×2 → ×2,6 en 0,85 s (expo.out), un
   reflet glisse sur l'arête haute ; la pastille se remplit de l'accent par un volet (0,26 s), le
   nom passe en `--brand-contrast` ; on la traverse : elle couvre l'écran (0,38 s, power3.in), un
   éclair de deux ou trois images, coupe sur la nuit. L'appel se forme en points, en grand, devient
   net d'un coup et se tient ; au milieu de la tenue, le nom se remplit de l'accent dans sa
   pastille (un volet) et claque, puis elle se vide avant la sortie.
4. **Le verre piloté** (`t3-commande`, 9 s) : il entre de profil (87° → 0° en 0,8 s, power4.inOut)
   depuis une lame claire qui se retire d'un balayage (0,45 s) ; caméra inclinée (22° en X, −10° →
   −5° en Y sur toute la scène, −3° en Z) qui montre le bon en **trois cadrages**, un par partie
   (le prix ; le réglage ; le total et le bouton) : un recadrage net de 0,7 s (power3.inOut) entre
   deux, qui rapproche aussi la caméra (×1,12 puis ×1,2), puis la seule dérive lente pendant que
   la partie se lit et agit. Ses gestes : le prix tourne (0,9 s, expo.out), les puces s'allument ;
   le curseur glisse (0,95 s, power2.inOut) et clique (0,07 s), la pastille du paiement glisse,
   l'interrupteur bascule et se remplit par un volet (0,28 s), les champs tombent (back.out(1)) ;
   le total tourne (0,7 s), le curseur clique le bouton.
5. **La trame de points** : le texte se forme d'abord en points blancs (étiré de 25 %, un écho flou
   deux fois plus grand qui se résorbe en 0,7 s), le texte plein prend le relais d'un coup 0,3 s
   après ; à l'inverse, le bouton cliqué s'ouvre d'un trou qui part du clic (0,36 s) et ne laisse
   que ses points à l'accent, qui montent de 30 px et se retirent par un volet pendant que le bon
   recule.
6. **Le carrousel en gros plan** (`t3-cartes`) : le mot seul, dans sa pastille qui s'ouvre du
   centre, se tient et se remplit de l'accent ; puis une carte toutes les 0,5 s, chacune son angle
   (16 à 24° en X, ±20 à 26° en Y), glissée de 360 px en 0,3 s (expo.out, sans flou), coupe nette à
   la suivante. La rafale est de la texture ; la dernière carte se pose en entier au centre, se
   tient immobile le temps de sa lecture (un reflet glisse sur son arête), puis file hors champ.

## 6. Les transitions

Presque pas de coupe : on passe d'une idée à l'autre par la mise au point, par la plongée à
travers un objet (le bouton), par une lame claire (l'interface vue de profil qui pivote), par la
dissolution en points, par un fondu flou entre deux lignes courtes ; une seule coupe franche, sur
le silence avant l'appel. Dans le kit : `t3-onglets` finit sur l'appel qui se dissout dans le flou ;
`t3-commande` commence par la lame qui pivote et finit par le bouton en points et le bon qui
recule ; `t3-cartes` commence sur un mot seul ; `t3-cartes` → `t3-fin` : la coupe franche, sur un
silence de la musique. Les fondus flous ne touchent que du clair et du gris.

## 7. Le produit à l'écran

- **Le produit est l'interface elle-même** : en entier et inclinée, une carte, le bon de commande
  piloté par le curseur, des couches éclatées ; toujours la vraie interface, simplifiée, en thème
  sombre, avec de gros chiffres, assez près pour que ses mots utiles (le prix, une option, le
  bouton) fassent 28 px au moins à l'écran.
- **Le bon de commande** suit **sa vraie page de paiement** (sa capture en est la source) : ses
  formules, son prix, ses façons de payer, son option ou son bonus s'il en a un, le total, son
  bouton. Les cartes montrent ce qu'on reçoit vraiment, avec les vrais chiffres. Un logiciel : sa
  vraie interface dans le même verre, avec la même caméra. Jamais de champ, de réduction ni de prix
  barré inventés ; une ligne qui n'existe pas chez lui se retire. Aucune illustration.
- **L'interface entière inclinée, la ligne au carré de points qui pivote, l'interface éclatée en
  couches** se refont avec le même verre (`.t3c-bon`), la même caméra et la même trame.
- **Le curseur :** la flèche du kit, posée dans le plan du bon : elle s'incline avec lui.

## 8. Le son

- **La grammaire :** une nappe électronique sombre et feutrée, vers 93 par minute ; l'accroche
  reste basse (des impacts sourds sur les reculs), l'entrée franche tombe sur le nom de l'offre,
  une pulsation porte la démonstration, puis la musique se coupe net : la ligne d'appel passe dans
  le silence, une montée courte amène **un seul impact** sur l'adresse, le logo finit en silence.
- **Chez toi :** ambiance « Tech minimale » (ou « Montée cinématique » pour une révélation),
  entrée calée sur le nom (`musiques prendre … --a <instant du nom>`). Bruitages, un par geste :
  souffle doux sur le recul, souffle filé sur les onglets, petit clic sur la pastille,
  scintillement sur le texte en points, clics d'interface, cliquetis de compteur sur le prix,
  éparpillement sur la dissolution, un souffle par carte. Coupe la musique 1 à 2 s avant
  l'adresse (`son` et `mastering` ensuite) et garde l'impact pour l'adresse seulement.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 3`) :
  « Tech minimale » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe
  devant).

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** deux mots géants et flous, qui deviennent nets, puis la caméra
  recule : la promesse complète, posée en grand, sa fin à l'accent. Lisible dès la première image.
- **La fin :** coupe franche dans le silence sur le verbe d'appel seul, à l'accent ; la ligne se
  complète et se tient pendant que sa vraie page monte dans le verre incliné, sous elle ; elle se
  change dans un flou en l'adresse de sa page, en grand : à l'impact, sa fin prend l'accent et un
  trait plein se tire dessous ; puis son logo et son nom, tenus 3 s. En page de vente, l'adresse
  peut devenir le texte du bouton situé sous la vidéo.

## Sur une autre offre

C'est un look : il se monte sur n'importe quelle offre. Ce qui suivait le trading s'adapte.

- **Formation :** onglets = les sujets de sa page ; bon = formule, prix, paiement en plusieurs
  fois, bonus ; cartes = les modules et les bonus avec leur nombre de vidéos ; le curseur glissé =
  le nombre de paiements.
- **Coaching :** onglets = les problèmes qu'il traite ; bon = la formule (nombre de séances), le
  prix, l'option (un appel de plus) ; cartes = les étapes de l'accompagnement.
- **Logiciel :** onglets = les fonctions ou les métiers ; le bon devient sa vraie interface, le
  curseur glissé = un réglage réel (crédits, utilisateurs, formule) ; cartes = les fonctions ou
  les intégrations, avec le vrai logo nu de l'outil (`studio_motion.py logos`).
- **Toujours :** la nuit de la marque, la phrase posée avec sa fin à l'accent, la pastille fixe
  sous les onglets, la plongée, la trame de points, le verre incliné piloté, la fin en silence.

## En vertical et en carré

- **9:16 :** passe la racine de la scène à 1080 × 1920 ; tout se recompose seul (`K.cadre`) : la
  promesse s'empile sur deux lignes et grandit ; la barre d'onglets au plus ×0,85, tant que la
  pastille de l'offre tient dans la largeur (un nom long la rend plus petite) ; le bon remplit la
  largeur (×1,02), son premier cadrage le montre presque entier, le dernier pose son bas près du
  bas de l'image ; les cartes passent en portrait (940 × 700, la tuile en haut, le nom dessous) et
  tiennent dans la zone de texte d'un Reel (y de 300 à 1 440) ; la fin est centrée, à 80 % de la
  largeur, et avec sa capture les textes montent au tiers haut.
- **4:5 et 1:1 :** même règle (racine à 1080 × 1350 ou 1080 × 1080) ; garde le bon en entier en
  largeur et la carte lue en entier (les cartes de la rafale peuvent sortir à droite et en bas,
  jamais en haut).

## Les compositions du kit

Chaque scène est une sous-composition 16:9 à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Ce qui change d'une offre
à l'autre est dans l'objet `EXEMPLE`, en tête du script ; les paramètres de mouvement (durées,
poses, cadrages) restent hors de lui.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (objet `EXEMPLE`) |
|---|---|---|---|
| `compositions/t3-onglets.html` | 7,2 s + la lecture de la promesse et de l'appel (11,2 s pour 5 et 3 mots ; la scène la calcule) | la promesse floue puis nette, le recul et la tenue avec ses captures ; la barre filée sous la pastille ; la plongée ; l'appel en points puis net, son nom qui se remplit | `promesse` (2 morceaux, 8 mots au plus), `onglets` (les sujets de sa page, 6 à 9, l'offre comprise ; une barre verticale seule pose un séparateur), `offre`, `appel` (le verbe), `iconePremier` ("" : aucune), `captures` (2 ou 3 vraies captures) |
| `compositions/t3-commande.html` | 9 s | le bon en verre incliné, en trois cadrages : le prix et ce qui est inclus ; le nombre de paiements et le bonus ; le total et le bouton qui se défait en points | `formules`, `menu`, `paiements`, `nom`, `acces`, `prix` (son vrai prix TTC), `inclus` (icône du kit, ce qui est inclus), `foisMax` (1 retire le curseur, le sélecteur de paiement et « Aujourd'hui » ; sans bonus non plus, le deuxième cadrage montre ce qui est inclus), `foisLab`, `bonus` (son prix ; 0 retire la ligne), `bonusNom`, `bonusLab`, `aujourdhui`, `total`, `bouton`, `mention` ; `menu`, `acces`, `mention` sont de la texture ("" les retire) |
| `compositions/t3-cartes.html` | la lecture du mot + 0,5 s par carte de la rafale + la lecture de la dernière (6,2 s pour 5 cartes ; la scène la calcule) | le mot dans sa pastille, la rafale de cartes inclinées, la dernière posée et lue | `mot` ; `cartes` (3 à 6, la dernière se lit) : `nom`, `chiffre` et `unite` (son vrai nombre ; "" retire la tuile), `logo` (le logo nu d'un outil ; "" : aucun) |
| `compositions/t3-fin.html` | 9,2 s (ligne de 4 mots, logo ; la scène la calcule) | le verbe seul, la ligne tenue sur la trame, sa vraie page dans le verre, l'adresse et son trait, le logo et le nom tenus 3 s | `verbe`, `suite`, `adresse` (réelle, courte, sans https://, en deux parties : la 2e prend l'accent), `capture` (la page où mène l'adresse, ou deux captures ; "" : `rythme` verra la tenue figée), `logo` (son fichier dans `brand/` ; "" : le nom seul), `nom` |

Les scènes qui calculent leur durée (`D` dans le script) : reporte-la dans `data-duration`, ici et
sur l'hôte dans `index.html`. Une phrase du script plus longue que ce qu'une mise en page prend ne
se raccourcit jamais : elle passe dans une scène construite dans le style (deux lignes, même verre,
même tenue). Toutes attendent les polices avant de mesurer : garde la construction dans
`construire()`. Identifiants préfixés `t3o`, `t3c`, `t3k`, `t3f` : si tu montes deux fois la même
scène, change le préfixe partout dans la copie.
