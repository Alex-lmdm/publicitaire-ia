# Style n°2 · Titres géants · d'après Cyera (https://x.com/motionimo/status/2103703350017433670)

**Ce qu'on voit :** une charte graphique qui prend vie, aux couleurs de la marque, autour de sa vraie matière. Des titres géants sur sa couleur d'accent, qui débordent du cadre à leur entrée et à leur sortie, un spécimen tapé sur une grille, une carte à coins ronds qui s'ouvre sur sa vraie capture et change de palette sur les temps, une mosaïque de cartes qui portent ses captures, ses chiffres, ses modules et le bouton de sa page, un disque qui porte son logo et pose le nom de l'offre avec sa phrase, une grille d'une case par élément réel de l'offre, et le slogan géant dont le point devient le bouton. Les cadres à poignées et les repères attrapent, mesurent et révèlent ; aucune étiquette technique.
**Souvent utile pour :** une vidéo de lancement ou d'accueil (la nouvelle offre, la nouvelle marque, l'ouverture d'un programme), en haut d'une page de vente ou en ouverture d'un webinaire.

**D'après :** le film de marque de Cyera réalisé par Motionimo · 16:9 · 30 s · musique seule, sans voix.

## 1. Le rythme

- **L'original coupe toutes les 1,4 s**, presque sans texte : chez le client, la phrase décide de la tenue, puis la coupe tombe sur le temps fort suivant (la carte de fin : 3 s au moins).
- **Pendant qu'on lit, la vie vient de la phrase et de sa matière**, un événement toutes les 0,5 à 0,8 s : une graisse qui bascule sur les temps, une lettre tapée, la bande qui change de palette, le mot clé sélectionné d'un bloc d'accent, le cadre à poignées qui attrape le nom, un chiffre qui monte, une case qui se coche. Une tenue sans rien autour ne dépasse jamais 0,8 s.
- **Rafales** : les icônes se dessinent à 0,03 s d'écart, les repères à 0,04 à 0,05 s, les cartes de la mosaïque arrivent à 0,06 s d'écart.
- **Les gestes de caméra du style** (l'approche d'un coin, le recul en mosaïque, la montée et la descente du disque, l'approche d'une case) tombent entre deux phrases ; sous un texte qu'on lit, la caméra se tient et le texte ne bouge pas : la vie vient de lui (une graisse qui bascule, un mot qui se sélectionne, une bande qui change de palette).
- **Une seule respiration** : juste avant le nom final, l'énergie retombe une demi-seconde, puis le dernier temps fort tombe sur le nom.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le titre qui déborde | une phrase en trois lignes énormes sur l'accent plein écran : elle arrive si grande qu'elle déborde du cadre, se resserre en 0,6 s jusqu'à tenir entière du haut au bas du cadre, et repart dans le débordement à la sortie ; pendant sa lecture, deux mots changent de graisse sur les temps | accroche, promesse, temps fort | `titre-geant` (plan A) |
| Le spécimen tapé | une phrase tapée sur une grille, en deux voix ; un cadre de sélection attrape la ligne légère, qui passe en gras | problème, promesse précisée, prix | `titre-geant` (plan B) |
| Les repères de maquette | traits, pointillés, points et cadres à poignées qui attrapent, mesurent et révèlent une vraie matière : le motif qui revient d'une scène à l'autre, sans aucune étiquette technique | toutes les scènes, celles construites pour son cas comprises | toutes les scènes |
| La carte et la mosaïque | un point d'accent file au centre d'une carte et s'ouvre sur sa vraie capture ; la bande du nom, trois palettes sur les temps ; puis la caméra recule sur six cartes qui portent chacune sa vraie matière (captures, bouton, modules, chiffre) | solution, démonstration de son produit | `carte-mosaique` |
| Le disque qui pose le nom | un cercle dessiné au trait se remplit de son logo (ou d'une capture, d'un vrai chiffre) cerclé d'accent, monte, redescend le long d'un trait de marque et se pose au point de fuite ; les rayons partent, le nom s'écrit en grand, sa phrase se pose, un bloc d'accent sélectionne le nom lettre par lettre | révélation, le nom de l'offre et ce qu'elle fait | `disque-revelation` |
| La grille d'icônes | une case par élément réel de l'offre (ses outils par leur vrai logo) ; la caméra s'approche de l'élément phare, il se remplit d'accent et son vrai nom se surligne | ce qu'on reçoit | `grille-final` (plan A) |
| Le slogan géant et le bouton | une phrase de sa page en deux lignes géantes sur la nuit, son point final est un disque d'accent qui file sous le nom et devient le bouton que le curseur clique | promesse finale, appel | `grille-final` (plans B et C) |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation. Une vidéo de page de 60 s double les pages du milieu (deux cartes, une mosaïque de captures, la révélation, les parties de l'offre) ; un Reel de 30 s garde titre, carte, révélation, final.

## 3. Les fonds et les couleurs

Ses couleurs ([interdits.md](../../references/interdits.md), « La palette ») : la nuit, le clair et les gris de sa marque, et son accent posé plein ; les objets connus gardent les leurs.

| Rôle dans le style | Chez le client |
|---|---|
| Les pages de nuit (spécimen, révélation, grille, slogan, fin) | `var(--brand-sombre)` ; la grille fine en blanc à 5 % |
| Le titre géant plein écran | `var(--brand-accent)`, le titre en `var(--brand-contrast)` |
| Le spécimen, posé sur la nuit | `var(--brand-accent-lisible)` ; la ligne attrapée passe en `var(--brand-clair)` |
| Le point, les poignées, la sélection, le bouton | l'accent lui-même, plein (`--brand-accent-lisible` pour un trait fin sur la nuit) : jamais une deuxième couleur inventée |
| La page du dessin au trait | `var(--brand-clair)`, le trait en `var(--brand-sombre)` |
| Le slogan, les noms, les titres sur la nuit | `var(--brand-clair)` |
| Les fonds de carte de la mosaïque | accent, clair, `--brand-gris-1`, sombre : des cadres autour de sa matière, jamais une carte vide |

**Les traits.** Un trait discret (la grille, les rayons, les repères sur la nuit) est du blanc en
transparence, donc un gris ; un trait de marque (le cadre de sélection, ses poignées, le trait qui
tombe du disque, le repère du bouton) est l'accent plein et fin. Aucun accent ne reste en
transparence : une carte d'accent arrive en glissant, un disque d'accent grandit, un texte d'accent
se tape ; jamais de fondu ni de flou sur l'accent (sur la nuit, un jaune flou ou à moitié
transparent devient olive). Un texte posé sur un bloc d'accent passe à `--brand-contrast` lettre par
lettre, à mesure que le bloc le sélectionne : aucune lettre n'est jamais à moitié couverte.

Les fonds alternent par coupe franche : accent plein, nuit quadrillée, sa capture dans la carte, ses
palettes, mosaïque, clair du dessin au trait, nuit. Au moins quatre bascules en 30 s.

## 4. La typographie

- **Police** : celle des titres de la marque (`var(--brand-font-display)`), en deux graisses : **600** pour la voix pleine, **400** pour la voix légère. L'original oppose une linéale et une serif fine, deux polices payantes. Si la marque n'impose rien : **Inter Tight** (titres, 500 et 600), et pour la voix légère **Instrument Serif** (Regular), ou à défaut Inter Tight 300 ; `studio_motion.py police "<Famille>"` les installe.
- **Une phrase entière par page**, jamais des mots isolés : le titre géant, le spécimen, le nom et sa phrase, le nom de l'élément phare, le slogan sont chacun une phrase de sa page ou de sa fiche.
- **Géant, mais entier pendant qu'on le lit** : le titre déborde du cadre à son entrée et à sa sortie ; entre les deux, chaque mot est entier et la plus longue ligne tient dans 90 % de la largeur. Le nom posé par le disque, le slogan et le nom de fin sont des mots héros : les scènes règlent seules leur taille à leur mesure (60 à 90 % de la largeur). Trop de caractères se règlent en coupant des mots.
- **Casse** : celle de la phrase, minuscules, un point final sur les phrases courtes (« ce soir. ») ; le point final du slogan est le disque d'accent.
- **Alignement** : à gauche, toujours ; le titre géant colle au bord gauche (30 px), la voix légère du spécimen est en retrait. Le nom de l'offre se centre (dans la bande de la carte, au-dessus du disque, au final).
- **Approche** : serrée, -0,035 à -0,045 em sur les grands titres. **Interlignage** : 0,95 à 1 ; les lignes se frôlent. Si un jambage (p, g, q) tombe sur un accent ou un point de la ligne du dessous, on change la coupe.
- **Étiquettes** : une étiquette écrite porte une info réelle de la fiche (le prix, la date, le nom de l'offre, un chiffre de preuve) ou n'existe pas. Les étiquettes de maquette de l'original (la police et sa taille, le rayon, la couleur et son code) ne disent rien à son public et passent pour des restes oubliés : elles sont réservées à une vidéo qui parle de design (une marque, un template).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Titre géant | 3 lignes de 340 px (8 caractères au plus par ligne), bases à 0,987 × la taille d'écart | 6 lignes d'un mot, 300 px (5 caractères au plus) |
| Spécimen | 300 px, bases à 312, 612 et 902 px | 180 px, bases à 660, 846 et 1 022 px, entre x 100 et 930 |
| Étiquette (une info réelle) | 30 px | 30 px |
| Nom de l'offre dans la carte (voix légère) | 156 px (réduit s'il déborde de la bande) | 110 px, sur deux lignes s'il le faut |
| Une carte de la mosaïque (vue à ×0,44 ; ×0,46 en vertical) | chiffre 230 px ; contexte, liste et bouton 66 px (29 px à l'écran) | chiffre 200 px ; 64 px (29 px à l'écran) |
| Nom posé par le disque, sa phrase | 68 % de la largeur (260 px au plus), 58 px | 80 % de la largeur (200 px au plus), 54 px |
| Nom de l'élément phare de la grille | 44 px (68 px à l'écran, caméra approchée) | 40 px (62 px à l'écran) |
| Slogan final | 2 lignes, la plus longue à 70 % de la largeur (300 px au plus) | 3 lignes, 85 % (200 px au plus) |
| Nom de la marque au final | 64 % de la largeur (280 px au plus) | 80 % de la largeur (200 px au plus) |
| Texte du bouton | 46 px dans une pilule de 120 px, élargie à son libellé | 44 px dans une pilule de 112 px, aux deux tiers de la largeur au moins |

## 5. Les mouvements signature

1. **Le titre qui déborde** (`titre-geant.html`) : le bloc entre à ×1,5 et se resserre en 0,6 s (`power3.out`) jusqu'à tenir entier ; pendant la lecture, il ne bouge plus : toutes les 0,5 s, un mot de la ligne du milieu bascule de graisse d'un coup (600 ↔ 400) ; à la sortie, il repart à ×1,5 en 0,3 s (`power2.in`), la coupe tombe.
2. **Le spécimen tapé** (`titre-geant.html`) : les lignes se tapent par groupes de lettres (`K.taper`, la dernière posée 0,9 s après la coupe) ; la grille se trace (traits de 1 px en blanc transparent, 0,5 s, `expo.out`, 0,03 s d'écart) ; le cadre de sélection se pose sur la ligne légère (0,22 s, `power3.out`), elle passe en gras et en clair puis revient ; la caméra se tient, le spécimen se lit immobile.
3. **Les repères de maquette** (dans les quatre scènes) : traits pleins et pointillés qui se tracent en 0,42 s (`expo.out`) et se rétractent de même, points clairs qui sautent (0,3 s, `back.out(1)`), cadres à quatre poignées qui attrapent un disque, une ligne, un nom ou une case ; aucun n'écrit de cote.
4. **La carte par couches** (`carte-mosaique.html`) : la caméra recule du coin (×2,6 à ×1 en 0,6 s, `power3.inOut` sur `K.courbeEchelle`), le point d'accent file au centre et s'ouvre en cercle sur sa vraie capture (0,48 s : il n'est le sujet que 0,8 s) ; la bande du nom s'ouvre (0,5 s, `expo.out`, au tiers bas sur une capture), les repères la mesurent, le nom entre mot par mot, sa marque paraît nette dessous ; pendant la lecture, la bande change trois fois de palette (0,3 s d'écart).
5. **Le recul en mosaïque** (`carte-mosaique.html`) : le nom lu, la pastille de la marque se retire et la caméra recule à ×0,44 (0,85 s, `power3.inOut` sur `K.courbeEchelle`) pendant que six cartes glissent de hors champ sous la grande (0,06 s d'écart, sans fondu) ; la vie continue (un chiffre qui monte, une liste qui se coche, le curseur qui clique le bouton) et la caméra dérive.
6. **Le disque qui pose le nom** (`disque-revelation.html`) : sur le clair, le cercle se dessine au trait avec son carré de construction (0,45 s) et se remplit de sa vraie matière en gonflant jusqu'à ×1,25 (42 % de la hauteur, `back.out(1)`) ; coupe sur la nuit : un cadre l'attrape, il monte (1,1 s, ×1,15) pendant que la caméra lève les yeux ; le trait de marque tombe (0,3 s, `power3.in`), deux traits de construction s'ouvrent en cône (un trait fin : aucun faisceau, aucun halo) ; il redescend le long du trait (1,2 s, ×0,42), la caméra revient, l'horizon se trace ; posé au point de fuite, les rayons partent de lui, le nom s'écrit lettre par lettre, sa phrase se pose. Pendant la lecture : le mot clé puis le nom sont sélectionnés lettre par lettre d'un bloc d'accent (0,3 s, comme dans un éditeur), un mot du nom change de graisse, la sélection se retire vers la droite 0,9 s avant la coupe.
7. **La case phare et le point qui devient le bouton** (`grille-final.html`) : la caméra s'approche de la case phare (×1,5 en 0,9 s) avant tout texte ; un cadre l'attrape, son nom se tape, un disque d'accent la remplit (0,4 s, `back.out(1)`), les autres passent au flou. Le point du slogan tombe en place (0,45 s, `back.out(1)`) ; à la coupe, il file sous le nom (0,55 s, `power3.inOut`), le bouton naît de lui en s'étirant en pilule (0,45 s), le curseur le clique, l'accent le remplit.

## 6. Les transitions

- **La coupe franche sur un temps fort** est la transition principale : d'une page de charte à la suivante, une fois sa phrase lue, d'un fond à l'autre, sans fondu.
- **Le débordement** : le titre géant entre et sort en débordant du cadre, la coupe tombe sur sa sortie.
- **Le raccord d'objet** : le point d'accent du coin s'ouvre sur la capture de la carte ; les rayons du point de pose deviennent l'étoile qui ouvre la grille d'icônes ; le point du slogan file sous le nom et devient le bouton.
- **Le recul de caméra** : une carte devient une mosaïque de cartes, entre deux phrases.
- **Le changement de palette** : la même mise en page, trois palettes de sa marque en trois temps.
- Jamais de fondu enchaîné entre deux pages chargées ; une page disparaît par coupe, un repère en se rétractant (0,2 à 0,3 s).

## 7. Le produit à l'écran

- **Dans des cartes à coins ronds** (64 px pour 1 480 px), jamais seul sur un fond uni. La grande carte porte toujours une vraie capture (`cadrage` choisit la partie montrée) ; les autres descendent l'échelle de la vraie matière ([ambition.md](../../references/ambition.md), principe 8) : une capture, son interface reconstruite (ses vrais modules qui se cochent, le vrai libellé de son bouton cliqué), un vrai chiffre et son contexte, puis un mot de sa page.
- **En mosaïque**, chaque carte, même coupée par un bord, porte une capture ou un morceau de son interface. On y lit seulement le nom, un chiffre et son contexte (hors bouton et liste) ; ce qu'on y lit fait au moins 64 px dans la carte (28 px à l'écran).
- **Le disque** porte son logo, sinon une capture découpée, sinon un vrai chiffre, dès qu'il prend sa couleur ; jamais un aplat seul. Posé, il n'est plus que le point de fuite : le sujet est le nom et sa phrase.
- **La grille** : une case par élément réel de l'offre (ses outils par leur vrai logo), autant de cases qu'il y en a.
- **Son produit dans un appareil** : sa vraie capture dans une carte, ou dans une fenêtre du kit (`k-fenetre`) posée sur la nuit ou sur un aplat de sa palette.
- Sans aucune capture (c'est la question unique du repérage), la grande carte garde ses mots dans la bande ; jamais une interface inventée, un faux lecteur, une icône de décor, une forme 3D ni une image redessinée.

## 8. Le son

- **Original** : musique seule, sans voix ni bruitage marqué ; une nappe électronique aérienne autour de 110 battements par minute, une montée douce pendant la construction, l'énergie pleine dès le titre géant, une retombée d'une demi-seconde juste avant le logo final ; les coupes tombent sur les attaques de la musique.
- **Chez le client** : une musique de lancement inspirante, 100 à 120 battements par minute, avec une entrée franche et un dernier temps fort à garder pour le bouton (`studio_motion.py musiques choisir`). Les coupes et les bascules de graisse se calent sur ses temps, sans jamais raccourcir une tenue de lecture.
- **Bruitages, légers** : un petit clic sur chaque cadre de sélection et sur le clic du curseur, un souffle bref sur les reculs de caméra, sur le débordement du titre et sur la chute du trait, un impact grave sur la pose du disque et sur le bouton qui se remplit. Rien sur les lettres tapées (trop de petits sons).
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 2`) : « Lancement énergique » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur la construction du logo (des points qui s'assemblent, des traits de construction, le nom qui s'écrit, un surlignage à poignées) et finit sur le slogan géant, puis le logo sur le sombre.
- **Chez le client** : la vidéo s'ouvre directement sur le titre géant (il déborde dès la première image et se lit entier à 0,6 s, même sans le son) ; la sélection à poignées passe sur le nom posé par le disque. Elle finit sur le slogan géant et son point, puis le nom de la marque, ses repères et le bouton cliqué, tenus 3 s au moins, immobiles. En page de vente, le bouton reprend le libellé du bouton sous la vidéo ; en pub, ni bouton ni curseur : « Découvre-le » et une flèche vers le bas.

## Sur une autre offre

Ce qui suivait l'original (une plateforme de sécurité) s'adapte, et chaque geste porte sa vraie matière :

- **Toujours** : le titre géant qui déborde à son entrée et à sa sortie, le spécimen sur sa grille, les repères et les cadres à poignées, la carte qui s'ouvre sur sa capture et sa mosaïque, le disque qui porte son logo et pose le nom avec sa phrase, la grille d'une case par élément réel, le slogan et son point qui devient le bouton, une coupe franche après chaque phrase lue.
- **Une formation** : la carte s'ouvre sur son espace de formation en capture ; la mosaïque montre une leçon, la liste des vrais modules qui se coche, le nombre réel de modules ou d'heures qui monte, un message d'élève en capture ; le disque porte son logo et pose « Nom + ce que la formation apprend » ; une case par module ou bonus ; le bouton « Je commence » ou le libellé de la page.
- **Un coaching** : la carte s'ouvre sur sa page ; les cartes montrent un créneau de son agenda, l'écran d'un appel, de vrais messages de clients (captures) ; le disque porte son logo ou sa photo de profil et pose le nom de l'accompagnement et sa promesse ; une case par étape de l'accompagnement ; le bouton « Je réserve mon appel ».
- **Un logiciel** : la carte s'ouvre sur son interface ; les cartes portent ses vraies interfaces (captures ou écrans reconstruits) et le curseur y clique ; le disque porte l'icône de l'app ; une case par fonction, les outils qu'il relie par leur vrai logo ; le bouton « Essayer ».
- **Sans logo** : le disque porte une capture découpée (sa page, son produit) ou un vrai chiffre de sa fiche (son prix, un nombre d'élèves).
- **Les déclinaisons** de l'original (le nom sur trois images) deviennent les trois parties de l'offre (modules, bonus, communauté), sur trois cartes, avec leurs vraies captures ou leurs vrais noms.

## En vertical et en carré

- **9:16 : chaque scène a sa version `-vertical.html`**, à prendre à la place du 16:9 (on remet en page, on ne recadre jamais).
  - `titre-geant-vertical.html` : un mot par ligne, six lignes de 300 px qui remplissent la hauteur (5 caractères au plus) ; le spécimen à 180 px dans la zone de texte d'un Reel (x 100 à 930 : 8 caractères au plus par ligne grasse), un peu au-dessus du milieu.
  - `carte-mosaique-vertical.html` : cartes en portrait (960 × 1 360 px), la grande remplit l'image (une vraie image en hauteur, sa pub ou sa story, la remplit mieux qu'une capture large) ; au recul (×0,46), deux cartes par rangée sur trois rangées : le bouton et la liste en haut, des images en bas (sous les commandes de l'application), des captures sur les cartes coupées par les bords.
  - `disque-revelation-vertical.html` : le disque monte jusqu'à 35 % de la hauteur, le trait descend d'environ 1 500 px jusqu'à l'horizon, posé aux deux tiers ; le nom (80 % de la largeur) et sa phrase au-dessus, hors des 10 % du haut.
  - `grille-final-vertical.html` : la grille en 4 colonnes ; le slogan sur trois lignes (10 caractères au plus) ; le nom à 80 % de la largeur, le bouton aux deux tiers de la largeur au moins.
- **4:5 et 1:1** : le titre géant en quatre lignes de 260 px (4:5) ou trois lignes de 240 px (1:1) ; la mosaïque en 2 × 2 ; le reste suit le 16:9 resserré au centre.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical ; seul le titre géant touche les bords, et il ne déborde qu'à son entrée et à sa sortie.

## Les compositions du kit

Chaque scène lit sa durée dans son data-duration (et celui de son hôte), place ses coupes d'après la lecture de ses textes et écrit dans la console la durée qu'il lui faut. Ses textes, chiffres, noms et chemins d'exemple sont dans l'objet `EXEMPLE`, en tête de son script ; ses paramètres de mouvement (instants, échelles, places) restent en dehors.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/titre-geant.html` | 6,4 s | Le titre géant qui entre et sort en débordant, lu entier sur l'accent ; coupe, le spécimen tapé sur sa grille | `EXEMPLE` : `titre` (trois lignes), `specimen` (deux lignes grasses, une légère), `etiquettes` (0 à 2 infos réelles) ; `COUPE`, `BASCULES` ; data-duration = COUPE + 0,9 s + lecture du spécimen |
| `compositions/titre-geant-vertical.html` | 6,4 s | La même en 9:16 : six lignes d'un mot, spécimen à 180 px | Comme en 16:9 ; `titre` : un mot par ligne |
| `compositions/carte-mosaique.html` | 6,9 s | Le point qui s'ouvre sur sa capture, la bande du nom et ses trois palettes, puis la mosaïque de six cartes de sa matière | `EXEMPLE` : `nom`, `marque`, `cartes` (la grande et sa capture, puis captures, bouton, modules, chiffre et contexte) ; data-duration = l'instant du recul + 2,8 s |
| `compositions/carte-mosaique-vertical.html` | 6,9 s | La même en 9:16 : cartes en portrait, mosaïque de deux cartes par rangée | Comme en 16:9 |
| `compositions/disque-revelation.html` | 7,8 s | Le cercle qui se remplit de son logo, la montée, le trait, la pose au point de fuite, le nom en grand et sa phrase sélectionnés | `EXEMPLE` : `nom`, `phrase`, `mot_cle`, la matière du disque (`logo`, sinon `image` et `cadrage`, sinon `chiffre`), `etiquette` ; `MOMENTS` ; data-duration = la phrase posée + sa lecture |
| `compositions/disque-revelation-vertical.html` | 7,8 s | La même en 9:16 : le disque à 35 % de la hauteur, la pose aux deux tiers | Comme en 16:9 |
| `compositions/grille-final.html` | 11,8 s | La grille d'une case par élément réel, la case phare et son nom, le slogan géant et son point, le nom et le bouton cliqué | `EXEMPLE` : `icones`, `choisie`, `etiquette`, `slogan` (deux lignes, 4 mots au plus), `nom` (et `logo`), `bouton`, `note` |
| `compositions/grille-final-vertical.html` | 11,9 s | La même en 9:16 : 4 colonnes, slogan sur trois lignes | Comme en 16:9 ; `slogan` sur trois lignes |

Bout à bout dans cet ordre, elles font une vidéo de 33 s qui se tient seule ; les palettes, les repères, le disque et la taille des mots héros suivent n'importe quelle marque et n'importe quel texte.
