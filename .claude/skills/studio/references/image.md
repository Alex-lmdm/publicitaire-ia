# L'image : ce qu'on voit à chaque instant

Une vidéo du studio a le niveau d'une vidéo de lancement faite par un studio de motion design :
**ce qu'on voit raconte, quelques mots très grands le ponctuent.** Le test : on coupe le son, on
regarde sans se presser, et on a compris ce que fait l'offre, pour qui, et quoi faire, sans avoir lu
plus d'un mot par seconde. Le mouvement, les raccords et la caméra sont dans
[mouvement.md](mouvement.md).

## Trois identités

1. **Sa marque** porte la vidéo : couleurs, polices et logo, déjà dans `brand/` du projet
   (`var(--brand-…)`, `brand/logo.*`). Jamais une couleur ni une police de marque en dur.
2. **Les surfaces de son offre** gardent leur identité : sa page, son espace de formation, son
   logiciel, dans leurs vraies couleurs et polices (relevées dans la capture).
3. **Les outils** qu'il utilise ou dont sa page parle (Instagram, Notion, Canva, Stripe, Zoom,
   ChatGPT…) gardent leurs logos et leur allure : des repères que son public connaît
   (`studio_motion.py logos`).

## La vraie matière

Ce qui se montre vient du client ou de ses outils. Pour chaque plan, descends cette échelle et
prends le premier barreau qui existe :

1. **Une vraie capture** : sa page, son produit, son espace de formation, un résultat, un message
   reçu, une vraie vidéo (`sources/`, `assets/`).
2. **Son interface reconstruite** d'après capture, animée : on tape, on clique, elle répond.
   Simplifier pour qu'elle se lise (agrandir le bouton utile, réduire une liste à cinq lignes), oui ;
   inventer une fonction ou un écran, non. Une simplification se note dans `sources/NOTES.md`.
3. **Un vrai chiffre** de `OFFRE.json` mis en scène : un compteur, une barre, un prix, avec son
   contexte.
4. **Le schéma de son vrai mécanisme** : des nœuds vrais (sa page, son produit, les étapes, ce qu'on
   obtient) reliés par des traits qui se tracent, le fil conducteur qui les parcourt.
5. **Les vrais logos nus** des outils que l'offre nomme.
6. **Ses mots seuls**, en très grand, qui jouent ce qu'ils disent.

Ce qu'on peut montrer selon ce qu'il vend :

| Il vend | Ce qu'on montre de vrai |
|---|---|
| Une formation | l'espace de formation, le sommaire qui se déroule, un module qui s'ouvre, les vraies miniatures, le résultat promis |
| Un coaching, un service | le déroulé de l'accompagnement en étapes, l'agenda des séances, les messages reçus, ce que le client a entre les mains à la fin |
| Un logiciel, une app | la fonction en action dans son interface reconstruite, le résultat qu'elle produit |
| Un template, un guide | le document qui se remplit, les pages qui défilent, le résultat obtenu |
| Une communauté | les espaces, le rythme (lives, défis), ce qu'on y trouve, sans inventer de membres |
| Des résultats | les vraies captures (ventes, vues, avant / après) avec leurs vrais chiffres |

Une forme simple à ses couleurs (disque, aplat, case, cadre, trait) sert de **cadre** (elle porte
une capture, un chiffre, un logo, un mot), de **transition** (elle couvre, s'ouvre, devient l'objet
suivant) ou de **fil conducteur** (le point de sa couleur qui relie, raye, devient le point final) ;
jamais de sujet d'un plan. Il manque une matière importante : c'est la question unique du repérage
([reperage.md](reperage.md)), pas une forme de plus.

## Le cadre

- **Le sujet remplit le cadre** : ce qu'on regarde occupe au moins 40 % de la largeur ou de la
  hauteur. Un petit élément au milieu d'un grand fond vide n'est jamais un plan : approche la caméra,
  recadre, ou donne-lui un monde (des cartes autour, sa page derrière, ses résultats en éventail).
- **Une interface se montre de près** : assez pour que ses mots utiles fassent au moins 28 px sur
  un petit côté de 1080 (`check` le mesure : `text_below_floor`). Ses micro-textes non lus sont de
  la texture.
- **De la profondeur** : trois plans (un premier plan qui passe, flou ; le sujet, net ; un fond qui
  vit), une perspective légère, une ombre qui situe l'objet, un flou qui grandit avec la distance.
- **Des échelles qui contrastent** : un mot géant à côté d'une étiquette ; un objet tout proche et
  d'autres au loin.
- **Pas tout au centre** : le sujet peut être décentré, sortir d'un bord, être coupé par le cadre
  quand c'est voulu. Tout centré, tout petit, tout au même plan : c'est une maquette, pas un film.
- **En vertical, on recompose** : en 9:16, le sujet s'empile en hauteur et grandit (interface en
  carte verticale, téléphone au centre, mots empilés et plus gros) ; on ne rétrécit jamais une mise
  en page 16:9 au milieu d'un écran haut. Tout texte important tient dans la zone sûre du support
  (`studio_motion.py zones`).
- **Un moment signature par plan** : un geste qu'on n'attend pas et qu'on a envie de revoir (la
  vignette cliquée qui vient au centre pendant que les autres pivotent, le dossier qui devient le
  nœud d'un schéma, la liste barrée qui tombe en morceaux). Nomme-le dans le plan avant d'animer.

## La palette : ses couleurs, rien d'autre

Tout ce que la vidéo dessine prend ses couleurs dans `brand/tokens.css`, et seulement là :
`--brand-bg`, `--brand-surface`, `--brand-text`, `--brand-muted`, `--brand-accent`,
`--brand-secondary`, `--brand-contrast` (le texte sur l'accent), `--brand-sombre` (les fonds de
nuit), `--brand-clair`, `--brand-accent-lisible` (l'accent d'un texte sur la nuit), les gris
`--brand-gris-1` à `--brand-gris-4`, et du blanc ou du noir en transparence pour une grille fine ou
une ombre.

L'accent se pose **plein**, jamais en transparence sur un fond sombre (ni en fondu ni en flou à son
entrée : le temps de l'effet, il vire à l'olive ou au brun), jamais mélangé au noir, au blanc ou au
gris, jamais dérivé (`oklch(from …)`, `color-mix`, une « nuit » teintée). Une couleur qui passe de
l'encre à l'accent change d'un coup, sous un volet ou un mouvement. Les dégradés vont d'un neutre à
un neutre. Un texte garde un contraste d'au moins 4,5:1 avec son fond.

Seules ses **vraies captures** et les **logos de ses outils** gardent leurs propres couleurs.
`studio_motion.py palette` relève tout le reste sur le MP4.

## Les fonds et les objets

- **Le fond est un acteur, pas un quota.** Il change quand le film change de temps (le nom de
  l'offre, un chapitre, le prix, un avant / après), avec une cause visible (un clic, un volet, un
  objet qui grandit). Les fonds du kit : la nuit à sa marque avec une grille fine, le clair avec
  grille, l'accent plein pour les temps forts, l'écran coupé pour un avant / après.
- **Des logos qui flottent seulement quand ils ont un sens** : les vrais logos nus (`K.logoNu`, sans
  tuile) de l'outil dont la scène parle, pour remplir une zone vide ; 6 à 8, la plupart nets, en
  vraie profondeur (petits au loin, moyens nets, un ou deux grands et flous au premier plan),
  jamais collés aux mots, hors de la bande du sticker. Une scène sans logo pertinent n'en a pas :
  elle vit par sa matière. Jamais d'icônes génériques (étoile, éclair, ciseaux).
- Le contexte se montre par l'interface plutôt qu'en titre : pour « un client m'a écrit », le
  téléphone, la notification, le message.

## La typographie

- **Trois tailles, jamais plus**, en 9:16 (en 16:9, à proportion de la hauteur de 1080) :

  | Rôle | Mots | Taille |
  |---|---|---|
  | le **mot héros** | 1 à 3 | il remplit 60 à 90 % de la largeur (130 à 400 px en 9:16) |
  | la **ligne d'appui** | 3 à 6 | 56 à 72 px |
  | les **étiquettes** posées sur ce qu'on montre | 1 à 4 | 30 à 40 px, jamais sous 28 px |

  Trop de mots se règle en coupant des mots, jamais en réduisant la police. Au plus 8 mots à lire
  sur une image, hors interface.
- **Le mot joue ce qu'il dit**, une fois lisible : il claque, s'étire, se barre, se surligne d'un
  bloc plein, se change sur place, ses lettres tombent en rafale (`kit.md`). Deux tons : le plein et
  l'accent (« Ton **lien.** »), ou le gris d'appui et le plein.
- Les étiquettes de fonction : deux ou trois mots en blocs pleins empilés (`k-blocs`), posés à côté
  de l'interface qui le fait.
- Un contour net (`k-contour`) pour doubler un mot plein, jamais une lueur. Texte plein, jamais en
  dégradé. La frappe au clavier seulement dans un champ de saisie.

## Les défauts interdits

C'est là que tombe une vidéo générée quand rien d'autre n'est décidé. Chacun est interdit, sauf si
la vraie matière du client ou sa vidéo de référence le contient, et alors seulement comme elle.

| Interdit | À la place |
|---|---|
| Un fond sombre vide avec de petits éléments au milieu | Le sujet en grand, au moins 40 % du cadre, dans un monde |
| Des écrans de texte posés sur le même fond, plan après plan (des slides) | Sa matière qui agit, un objet qui devient le suivant |
| Des sous-titres : une phrase par écran, en haut, au-dessus d'une petite interface | Le plan montre en grand ; un mot héros, une ligne d'appui au plus |
| Des mots isolés ou des chiffres sans contexte | Ce que l'idée dit, montré, et ses mots qui claquent |
| Des images inventées : paysages, couchers de soleil, planètes, sphères, illustrations, photos d'ambiance | Sa vraie matière, en descendant l'échelle |
| Des formes seules (disques, carrés, aplats) comme sujet ; des particules, nuées ou poussières décoratives | Une forme qui porte une matière réelle, ou qui sert de transition |
| Halos, néons, reflets d'objectif, orbes lumineux, sol quadrillé lumineux, ondes de choc | Des objets du sujet floutés par la profondeur ; la grille fine du kit |
| Dégradés violets ou bleus, dégradés tirés de l'accent | L'accent plein sur des neutres |
| Tout centré ; tout qui entre en même temps ; chaque élément qui monte en fondu | Des entrées variées et décalées ([mouvement.md](mouvement.md)) |
| Un texte qui bouge pendant qu'on le lit ; un titre qui continue de glisser une fois posé | Le titre posé reste immobile ; la vie vient du sujet et du monde autour |
| Trois cartes en ligne, une grille de chiffres, un titre sur une capture assombrie | Une carte à la fois, au premier plan, qui agit |
| Des étiquettes dans les coins, des cadres et des crochets décoratifs, des compteurs « 01 / 02 » | Des étiquettes posées sur ce qu'on montre |
| Le logo rangé dans un coin pendant toute la vidéo | Le logo arrive à son moment (le nom, la fin) |
| Des icônes génériques, des emoji, des logos posés sur des tuiles | Les vrais logos nus de ses outils, là où ils ont un sens |
| Une fausse interface vague dans un faux navigateur | Son interface réelle, reconstruite d'après capture |
| Le même enchaînement d'une vidéo à l'autre | Change l'angle, la matière, les gestes, les fonds et les transitions d'une vidéo à l'autre |

Après le premier rendu, nomme chaque défaut présent (de cette liste ou non), écris-le dans
« Interdits de cette vidéo » (`PLAN.md`) et corrige-le. La liste de la vidéo grandit à chaque rendu.

Test final : si cette vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom, elle
est trop générique. Recommence par ce que son offre a de visible.

## Avec un style du catalogue

La grammaire du style (sa typographie, ses mises en page, ses mouvements, ses transitions) prime
sur cette page pour ce qui est des gestes. Jamais pour la palette, la vraie matière, le cadre, la
taille du texte ou la lecture : un style ne justifie aucune teinte hors palette, aucune image
inventée, aucune forme seule à la place d'un sujet, aucun texte plus petit que 28 px, aucune
phrase tenue moins longtemps que sa lecture, ni plus d'un mot à lire par seconde.
