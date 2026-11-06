# Style n°2 · Titres géants · d'après Cyera (https://x.com/motionimo/status/2103703350017433670)

**Ce qu'on voit :** une charte graphique qui prend vie, aux seules couleurs de la marque. Des titres si grands qu'ils débordent du cadre sur sa couleur d'accent, un spécimen typographique posé sur une grille avec ses étiquettes de maquette, une carte à coins ronds qui naît d'un point d'accent et change de palette sur les temps, une mosaïque de cartes qui portent sa vraie matière, un disque d'accent qui monte, redescend le long d'un trait et pose le nom de l'offre, une grille d'icônes au trait fin, et le slogan géant dont le point devient le bouton.
**Souvent utile pour :** une vidéo de lancement ou d'accueil (la nouvelle offre, la nouvelle marque, l'ouverture d'un programme), en haut d'une page de vente ou en ouverture d'un webinaire.

**D'après :** le film de marque de Cyera réalisé par Motionimo · 16:9 · 30 s · musique seule, sans voix.
**Mesures de l'original** (`studio_motion.py reference`) : 1,71 événement par seconde, écart médian 0,40 s, 22 coupes franches, image figée la plus longue 1,2 s (le logo final).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 22 s, marque LMDM, 06/11/2026) : `rythme` 1,58 événement par seconde en 16:9 comme en 9:16, écart médian 0,50 s, aucune image figée ; `palette` « ok » dans les deux formats.

> On reprend la grammaire (rythme, mises en page, typographie, mouvements, transitions, façon de
> montrer le produit), jamais le contenu : ni ses textes, ni son logo, ni ses images (paysages,
> sphère, planète, objets), ni ses couleurs, ni sa musique. Ce qu'on voit vient du client et se
> peint aux seules couleurs de sa marque.

## 1. Le rythme

- **Une coupe franche toutes les 1,4 s en moyenne**, toujours sur un temps fort de la musique : la vidéo enchaîne des « pages » de charte (le titre, le spécimen, la carte, la mosaïque, le disque, la grille, le slogan, le nom), chacune tenue 1 à 2,5 s.
- **Dans chaque page, un événement toutes les 0,25 à 0,4 s** : une graisse qui bascule, une lettre tapée, un repère qui se trace, une couche de la carte qui monte, une icône qui se dessine.
- **Rafales** : les icônes se dessinent à 0,03 s d'écart, les repères à 0,04 à 0,05 s, les cartes de la mosaïque arrivent à 0,06 s d'écart.
- **La caméra ne s'arrête jamais** : poussée lente (×1,00 à ×1,07 sur 2 s) pendant qu'on lit, recul rapide (0,6 à 0,9 s, `expo.inOut`) entre deux intentions.
- **Une seule respiration** : juste avant le nom final, l'énergie retombe une demi-seconde, puis le dernier temps fort tombe sur le nom.
- **Chez le client** : vise 1,5 événement par seconde au moins, une coupe franche toutes les 1 à 2 s, jamais une page tenue plus de 2,5 s, sauf l'écran final.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le titre qui déborde | trois lignes énormes sur l'accent plein écran, un mot qui change de graisse sur les temps | accroche, promesse, temps fort | `titre-geant` (plan A) |
| Le spécimen tapé | la phrase tapée sur une grille, en deux voix, avec ses étiquettes de maquette ; un cadre de sélection attrape un mot | problème, promesse précisée, titre de chapitre | `titre-geant` (plan B) |
| Les repères de maquette | traits, pointillés, points, cotes et étiquettes vraies qui se tracent : le motif qui revient d'une scène à l'autre | toutes les scènes, celles construites pour son cas comprises | toutes les scènes |
| La carte et la mosaïque | un point d'accent devient le fond d'une carte qui se construit par couches et change trois fois de palette, puis la caméra recule sur six cartes de sa vraie matière | solution, démonstration de son produit | `carte-mosaique` |
| Le disque qui pose le nom | un cercle dessiné au trait prend l'accent, monte, redescend le long d'un trait de marque et se pose au point de fuite ; les rayons partent, le nom s'écrit | révélation, le nom de l'offre | `disque-revelation` |
| La grille d'icônes | une icône au trait par élément réel de l'offre, l'élément phare sélectionné | ce qu'on reçoit | `grille-final` (plan A) |
| Le slogan géant et le bouton | deux lignes géantes sur la nuit, leur point final est un disque d'accent qui file sous le nom et devient le bouton que le curseur clique | promesse finale, appel | `grille-final` (plans B et C) |

Les déclinaisons de l'original (le nom de la marque sur trois images) deviennent les trois parties
réelles de l'offre, sur trois cartes, avec leurs vrais noms ou leurs vraies captures.

### L'original, pour mémoire

L'original est un film de marque : il présente une identité, pas une offre. Ses pages, dans l'ordre, avec le rôle que chacune peut tenir ; ses images (paysages, sphère, objets) ne se refont jamais, seuls leurs mouvements passent dans le kit :

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Le titre géant | accroche | 1,5 à 2 s | La couleur d'accent plein écran, la promesse en trois lignes énormes qui débordent ; les mots changent de graisse sur les temps (`titre-geant.html`, plan A) |
| Le spécimen | problème ou promesse précisée | 2 s | Coupe sur le fond sombre : la phrase tapée lettre par lettre sur une grille, deux voix (gras, puis léger en retrait), étiquettes de maquette ; un cadre de sélection attrape un mot (`titre-geant.html`, plan B) |
| La carte | solution : le produit apparaît | 3 s | Un coin arrondi et sa cote, la carte se remplit (dans l'original, d'un paysage peint), des repères se posent, le nom de l'offre s'écrit en léger ; chez le client, le point d'accent devient le fond de la carte, ou sa vraie capture (`carte-mosaique.html`) |
| La mosaïque | démonstration | 2 s | La caméra recule : six cartes arrivent autour, chacune avec un morceau du vrai produit (`carte-mosaique.html`, fin) |
| La révélation | révélation | 5 s | Dans l'original, une sphère de verre dessinée au trait prend sa couleur, flotte dans un canyon et dépose le produit dans un faisceau de lumière ; chez le client, un disque d'accent plein fait le même trajet et pose le nom de l'offre au point de fuite (`disque-revelation.html`) |
| La grille d'icônes | offre : ce qu'on reçoit | 2,4 s | Une icône par élément de l'offre, dessinée au trait fin ; un cadre attrape l'élément phare et son étiquette s'écrit (`grille-final.html`, plan A) |
| Les déclinaisons (facultatif) | preuve ou contenu | 1,5 à 2 s | Dans l'original, le nom décliné sur trois images qui changent toutes les 0,6 s ; chez le client, les parties de l'offre (modules, bonus, communauté) sur trois cartes, avec leurs vrais noms |
| Le slogan | promesse finale | 2 s | Deux lignes blanches géantes (dans l'original, dans un espace peint) ; chez le client, sur la nuit quadrillée, leur point final en disque d'accent (`grille-final.html`, plan B) |
| Le nom et le bouton | appel | 3,6 s | Le nom et ses repères ; le point du slogan se pose et devient le bouton, le curseur le clique (`grille-final.html`, plan C) |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

Une vidéo de page de 60 s double les pages du milieu (deux cartes, une mosaïque de captures, la révélation, les déclinaisons) ; un Reel de 25 s garde titre, carte, révélation, final.

## 3. Les fonds et les couleurs

Ses couleurs, rien d'autre ([../../references/style.md](../../references/style.md), « La palette ») :
la nuit, le clair et les gris de sa marque, et son accent posé plein.

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Aubergine presque noir | le fond des pages sombres, la grille, l'espace | `var(--brand-sombre)`, la couleur la plus sombre de sa marque (sur une marque claire, son texte), sur toutes les pages de nuit ; la grille en blanc à 5 % |
| Lilas vif | le titre géant en plein écran, le texte du spécimen | `var(--brand-accent)` pour le plein écran (le titre est écrit en `var(--brand-contrast)` dessus) ; le spécimen, posé sur la nuit, en `var(--brand-accent-lisible)` (l'accent, ou son clair s'il ne se lit pas sur la nuit) |
| Violets, roses et pêche du crépuscule | les paysages, la sphère, l'espace | rien : ces images ne se refont pas. À leur place, ses vraies captures, ou les quatre fonds de carte de sa palette (accent, clair, gris, sombre) |
| Vert lime | le point qui bouge, les poignées, le surlignage, le logo final | l'accent lui-même, plein : jamais une deuxième couleur inventée |
| Blanc cassé | la page du dessin au trait | `var(--brand-clair)`, le trait en `var(--brand-sombre)` |
| Blanc | le slogan, les titres, les étiquettes | `var(--brand-clair)` ; les notes en `var(--brand-gris-3)` |

**Les traits.** Un trait discret (la grille, les rayons, les repères sur la nuit) est du blanc en
transparence, donc un gris ; un trait de marque (le cadre de sélection, ses poignées, le trait qui
tombe du disque, la cote du bouton) est l'accent plein et fin (`--brand-accent-lisible` sur la
nuit). Aucun dégradé ne touche l'accent, aucune teinte n'en est tirée, aucun accent ne reste en
transparence : même une carte d'accent arrive en glissant, sans fondu (sur la nuit, un jaune à
moitié transparent devient olive).

**Sur n'importe quelle marque, claire ou sombre.** La nuit est toujours `--brand-sombre` : sur une
marque claire, c'est la couleur de son texte, et le look reste nocturne, à ses couleurs. Le texte
posé sur la nuit est `--brand-clair` ; tout texte garde un contraste d'au moins 4,5:1 (un accent
sombre qui colore un texte sur la nuit passe par `--brand-accent-lisible`).

Les fonds alternent par coupe franche : accent plein, nuit quadrillée, carte d'accent, ses
palettes (clair, sombre), mosaïque, clair du dessin au trait, nuit. Au moins quatre bascules en
20 s.

## 4. La typographie

- **Police** : celle des titres de la marque (`var(--brand-font-display)`), en deux graisses : **600** pour la voix pleine, **400** pour la voix légère. L'original oppose une linéale (Haffer) et une serif fine (Season Mix), deux polices payantes. Si la marque n'impose rien : **Inter Tight** (titres, 500 et 600), et pour la voix légère **Instrument Serif** (Regular), ou à défaut Inter Tight 300 ; `studio_motion.py police "<Famille>"` les installe.
- **Casse** : celle de la phrase, minuscules, un point final sur les phrases courtes (« en grand. ») ; le point final du slogan est le disque d'accent.
- **Alignement** : à gauche, toujours ; le titre géant colle au bord gauche (30 px), la voix légère du spécimen est en retrait. Le nom de l'offre se centre (dans la bande de la carte, au-dessus du disque, au final).
- **Approche** : serrée, -0,035 à -0,045 em sur les grands titres.
- **Interlignage** : 0,95 à 1 ; les lignes se frôlent. Si un jambage (p, g, q) tombe sur un accent ou un point de la ligne du dessous, on écarte la ligne ou on change la coupe.
- **Étiquettes de maquette** : 21 à 26 px, police du texte, en clair (à 82 % sur la nuit) ou dans l'encre de la carte ; elles disent une chose vraie (la police, la taille, le rayon, la couleur et son code), jamais du faux texte.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Titre géant (3 lignes, puis 6 en vertical) | 380 px, bases à 375 px d'écart | 300 px, un mot par ligne, bases à 318 px |
| Spécimen | 300 px, bases à 300 et 290 px | 220 px, bases à 230 et 216 px |
| Nom de l'offre dans la carte (voix légère) | 156 px (réduit s'il déborde de la bande) | 110 px, sur deux lignes s'il le faut |
| Mot d'une carte de la mosaïque | 170 px | 150 px |
| Nom posé par le disque | 120 px | 104 px |
| Slogan final (blanc) | 236 px, 2 lignes | 166 px, 3 lignes |
| Nom de la marque au final | 132 px | 96 px |
| Texte du bouton | 46 px dans une pilule de 120 px, élargie à son libellé | 44 px dans une pilule de 112 px, aux deux tiers de la largeur au moins |
| Étiquettes, cotes | 21 à 24 px | 24 à 28 px |

## 5. Les mouvements signature

1. **Le titre qui déborde** (`titre-geant.html`) : trois lignes de 380 px qui touchent le haut et le bas du cadre ; le bloc pousse de ×1,00 à ×1,07 en 1,9 s (`power1.inOut`), la ligne du bas glisse de 210 px vers la gauche (`power2.inOut`) et révèle la fin de son mot coupé ; toutes les 0,4 s, un mot bascule de graisse d'un coup (600 ↔ 400), sans transition.
2. **Le spécimen tapé** (`titre-geant.html`) : chaque ligne se tape par groupes de lettres en 0,3 s (`K.taper`), la grille se trace (traits de 1 px en blanc transparent, `scaleX` puis `scaleY` de 0 à 1 en 0,5 s, `expo.out`, 0,03 s d'écart), les étiquettes montent de 10 px (0,4 s, `expo.out`, 0,12 s d'écart) ; le cadre de sélection à quatre poignées se pose en 0,22 s (`power3.out`, depuis ×1,04), la ligne passe en gras et en clair 0,2 s après, revient 0,3 s plus tard, et l'interlignage se resserre (0,35 s, `expo.inOut`) pendant que l'étiquette passe de « 100 % » à « 96 % ».
3. **Les repères de maquette** (dans les quatre scènes) : traits pleins de 2 px et traits pointillés qui se tracent en 0,42 s (`expo.out`, 0,05 s d'écart) et se rétractent de même, points clairs de 16 px qui sautent (0,3 s, `back.out(2.5)`, 0,04 s d'écart), une cote près d'un coin (« Rayon 64 px »), des étiquettes vraies (la police et sa taille, la couleur et son code). C'est le motif qui revient d'une page à l'autre.
4. **La carte qui se construit par couches** (`carte-mosaique.html`) : le point d'accent du coin file au centre et devient le fond de la carte (un cercle qui s'ouvre jusqu'aux bords, 0,5 s, `power3.inOut`) ; la bande du nom s'ouvre depuis le centre (0,5 s, `expo.out`) ; trois étiquettes montent de 30, 70 et 120 px (0,45 à 0,55 s, `expo.out`, 0,14 s d'écart) ; les repères se tracent, le nom entre mot par mot en voix légère, sa marque dessous. Puis la même carte change trois fois de palette sur les temps (clair, sombre, accent, 0,16 s chacune), et son étiquette de couleur suit.
5. **Le recul en mosaïque** (`carte-mosaique.html`) : la caméra part à ×2,6 sur un coin, recule à ×1 en 0,62 s (`expo.inOut`), pousse doucement, puis recule à ×0,44 en 0,85 s pendant que six cartes arrivent de la droite, de hors champ, et glissent sous la grande (0,85 s, `expo.out`, 0,06 s d'écart, sans fondu) ; dans la mosaïque, la vie continue (une liste se coche toutes les 0,18 s, le curseur clique le bouton qui se remplit, les mots se posent avec un rebond).
6. **Le disque qui pose le nom** (`disque-revelation.html`) : sur le clair, un cercle se dessine au trait avec son carré de construction et sa cote (`stroke-dashoffset`, 0,5 s, `power2.inOut`, 0,06 s d'écart), prend l'accent d'un coup en gonflant (×0,86 à ×1, `back.out(1.6)`) ; coupe sur la nuit : un cadre de sélection l'attrape (0,22 s, `power3.out`) avec l'étiquette de sa couleur, il monte en 1,3 s (`power2.inOut`) en rapetissant à ×0,62 pendant que la caméra lève les yeux ; le trait de marque tombe en 0,3 s (`power3.in`), deux traits de construction s'ouvrent en cône (0,5 s, `expo.out`) ; il redescend le long du trait en 1,7 s (`power1.inOut`), la caméra revient, l'horizon se trace (0,6 s, `expo.out`) ; posé au point de fuite, les rayons de perspective partent de lui (0,55 s, `expo.out`, 0,018 s d'écart) et le nom s'écrit lettre par lettre au-dessus.
7. **Le point qui devient le bouton** (`grille-final.html`) : le point final du slogan est un disque d'accent qui tombe en place (0,45 s, `back.out(2.4)`) ; à la coupe, il file sous le nom (0,55 s, `expo.inOut`) et y plonge (0,16 s) ; le bouton naît de lui, un rond qui s'étire en pilule (0,45 s, `expo.out`) ; au clic, l'accent le remplit depuis le centre (0,4 s, `power3.out`).

## 6. Les transitions

- **La coupe franche sur un temps fort** est la transition principale : d'une page de charte à la suivante, d'un fond à l'autre, sans fondu.
- **Le raccord d'objet** : le point d'accent du coin devient le fond de la carte ; les rayons du point de pose deviennent l'étoile qui ouvre la grille d'icônes ; le point du slogan file sous le nom et devient le bouton.
- **Le recul de caméra** : une carte devient une mosaïque de cartes.
- **Le changement de palette** : la même mise en page, trois palettes de sa marque en trois temps.
- Jamais de fondu enchaîné entre deux pages chargées ; une page disparaît par coupe, un repère en se rétractant (0,2 à 0,3 s).

## 7. Le produit à l'écran

- **Dans des cartes à coins ronds** (64 px pour 1 480 px de large) : le produit n'apparaît jamais seul sur un fond uni. Chaque carte porte un morceau du vrai produit : une vraie capture (`image` : sa page, son espace de formation, son logiciel, un résultat), la liste de ses vrais modules qui se coche, le vrai libellé du bouton de sa page cliqué par le curseur, un mot ou une phrase de sa page en grand.
- **En mosaïque** : la caméra recule et montre tout le produit d'un coup, cartes coupées aux bords du cadre (les cartes coupées restent des aplats de sa palette).
- **Le disque** : le point d'accent qui porte la révélation ; un logo rond de sa marque peut s'y poser (`LOGO`), sinon il reste l'accent plein et pose le nom.
- Dans l'original, la plateforme apparaît aussi sur un ordinateur portable devant un coucher de soleil : chez le client, sa page ou son espace de formation en vraie capture dans une carte, ou dans une fenêtre du kit (`k-fenetre`) posée sur la nuit ou sur un aplat de sa palette.
- Une carte sans matière réelle reste un aplat ou un mot : jamais une interface inventée, un faux lecteur vidéo, une icône de décor ni une image redessinée.

## 8. Le son

- **Original** : musique seule, sans voix ni bruitage marqué. Une nappe électronique aérienne, tempo estimé autour de 110 battements par minute ; une montée douce les 4 premières secondes (pendant la construction), l'énergie pleine dès la coupe sur le titre géant, une retombée d'une demi-seconde juste avant le logo final. Les coupes tombent sur les attaques de la musique (montées fortes mesurées à 4,3 s, 6,3 s, 7,9 s, 8,7 s, 10,1 s, 13,1 s, 14,5 s, 21,1 s, 21,9 s et 28,5 s).
- **Chez le client** : une musique de lancement inspirante, 100 à 120 battements par minute, avec une entrée franche et un dernier temps fort à garder pour le bouton (`studio_motion.py musiques choisir`). Les coupes et les bascules de graisse se calent sur ses temps.
- **Bruitages, légers** : un petit clic sur chaque cadre de sélection et sur le clic du curseur, un souffle bref sur les reculs de caméra et sur la chute du trait, un impact grave sur la pose du disque et sur le bouton qui se remplit. Rien sur les lettres tapées (trop de petits sons).
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 2`) : « Lancement énergique » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur la construction du logo (des points gris qui s'assemblent sur un blanc cassé, des traits de construction, le nom qui s'écrit, un surlignage vert à poignées), puis le logo blanc sur le sombre. Il finit sur le slogan géant, puis le logo sur le sombre, tenu 1,7 s.
- **Chez le client** : la vidéo s'ouvre directement sur le titre géant (la promesse se lit dès la première image, même sans le son) ; la construction du logo ne se garde que pour une vidéo d'accueil d'une marque qui a un vrai logo. Elle finit sur le slogan géant et son point, puis le nom de la marque, ses repères et le bouton cliqué, tenus 2,5 s au moins (le plan pousse doucement). En page de vente, le bouton reprend le libellé du bouton sous la vidéo ; en pub, ni bouton ni curseur : « Découvre-le » et une flèche vers le bas.

## Ce qui ne se fera pas à l'identique

- **Les deux polices** (Haffer et Season Mix, payantes) → la police de la marque en deux graisses ; la voix serif devient la graisse légère.
- **La construction du logo à partir de points** (faite pour leur logo) → pas de scène dans le kit ; le nom de la marque s'écrit lettre par lettre avec ses repères.
- **Les images de l'original ne se refont pas** : ni les paysages peints au crépuscule, ni la sphère de verre et son canyon, ni la planète et l'espace, ni le portable photoréaliste, ni les objets dérivés (casquette, carnet, sweat), ni les astéroïdes. Rien ne se redessine : à leur place, la vraie matière du client (ses captures, son interface, ses vidéos, ses résultats) ou les aplats et la typographie de sa palette ; la révélation passe par un disque d'accent plein, le slogan se pose sur la nuit.
- **Le violet avec son vert lime complémentaire** → la palette de sa marque et rien d'autre : l'accent plein sur ses neutres (sa nuit, son clair, ses gris) ; la vidéo est plus graphique que l'original.
- **Le faisceau de lumière** → un trait de marque fin et deux traits de construction : aucun halo, aucune lueur.

## Sur une autre offre

Le style est une façon de présenter : il se monte sur n'importe quelle offre. Ce qui suivait l'original (une plateforme de sécurité) s'adapte :

- **Toujours** : le titre géant qui déborde, le spécimen sur sa grille, les repères de maquette, la carte et sa mosaïque, le disque qui pose le nom, la grille d'icônes au trait, le slogan et son point qui devient le bouton, les coupes sur les temps.
- **Une formation** : la mosaïque montre l'espace de formation en capture et la liste des vrais modules qui se coche ; le disque pose le nom de la formation ; une icône par module ou bonus ; le bouton « Je commence » ou le libellé de la page.
- **Un coaching** : les cartes montrent un créneau de son agenda, l'écran d'un appel, de vrais messages de clients (captures) ; le disque pose le nom de l'accompagnement ; une icône par étape de l'accompagnement ; le bouton « Je réserve mon appel ».
- **Un logiciel** : les cartes portent ses vraies interfaces (captures ou écrans reconstruits) et le curseur y clique ; le disque pose le nom de l'app, ou porte son icône ronde (`LOGO`) ; une icône par fonction ; le bouton « Essayer ».
- **Les déclinaisons** de l'original (le nom sur trois images) deviennent les trois parties de l'offre, avec leurs vrais noms ou leurs vraies captures.

## En vertical et en carré

- **9:16 : chaque scène a sa version verticale, testée** sur la marque sombre de LMDM (les quatre bout à bout, 22 s : `rythme` et `palette` « ok »). Prends le fichier `-vertical.html` à la place du 16:9 : on ne recadre jamais une scène 16:9, on la remet en page.
  - `titre-geant-vertical.html` : le titre géant passe à un mot par ligne, six lignes de 300 px qui remplissent la hauteur, la dernière déborde à droite ; le spécimen passe à 220 px, posé un peu au-dessus du milieu (les commandes de l'application occupent le bas).
  - `carte-mosaique-vertical.html` : les cartes passent en portrait (960 × 1 360 px) et la grande remplit l'image ; le coin du départ et sa cote restent au-dessus de la bande du bas ; le nom passe sur deux lignes s'il est long ; au recul, la mosaïque met deux cartes par rangée sur trois rangées (la grande au centre de la rangée du milieu, entre deux cartes coupées par les bords, des aplats). Le bouton, la liste et les mots vont sur les cartes entières.
  - `disque-revelation-vertical.html` : le disque monte jusqu'à 35 % de la hauteur, le trait descend d'environ 1 400 px jusqu'à l'horizon, posé à 60 % de la hauteur ; le nom s'écrit au-dessus, en 104 px.
  - `grille-final-vertical.html` : la grille d'icônes en 4 colonnes ; le slogan sur trois lignes de 166 px (10 caractères au plus par ligne), son étiquette au-dessus ; le nom à 96 px et le bouton aux deux tiers de la largeur au moins (720 px), au-dessus de la bande du bas, sa cote dessous.
- **4:5 et 1:1** : le titre géant en quatre lignes de 260 px (4:5) ou trois lignes de 240 px (1:1) ; la mosaïque en 2 × 2 ; le reste suit le 16:9 resserré au centre.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical ; seul le titre géant déborde exprès, et sa ligne clé reste au milieu.

## Les compositions du kit

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/titre-geant.html` | 4,0 s | L'accroche : le titre géant qui déborde sur l'accent (1,9 s), coupe, le spécimen tapé sur sa grille avec ses étiquettes et son cadre de sélection (2,1 s) | L'id `t02-titre`, les trois lignes du titre (un `<span>` par mot), les trois lignes du spécimen (`data-texte`), les instants des bascules (`BASCULES`) |
| `compositions/titre-geant-vertical.html` | 4,0 s | La même scène remise en page en 9:16 : six lignes d'un mot, spécimen à 220 px | Comme la version 16:9 ; un mot par ligne, 6 caractères au plus sur les lignes du milieu |
| `compositions/carte-mosaique.html` | 5,0 s | Le produit : le coin et sa cote, le point d'accent qui devient le fond de la carte, la bande, les étiquettes, les repères, le nom en léger, trois palettes sur les temps, puis la mosaïque de six cartes de sa matière | L'id `t02-carte`, `NOM` et `MARQUE`, les cartes (`CARTES` : leur fond, leur contenu, ses vraies captures en `image`, ses vrais modules, le vrai libellé du bouton, ses mots) |
| `compositions/carte-mosaique-vertical.html` | 5,0 s | La même scène remise en page en 9:16 : cartes en portrait, la grande plein cadre, puis la mosaïque de deux cartes par rangée sur trois rangées | Comme la version 16:9 ; la matière sur les cartes entières (c1, c2, c5, c6), jamais sur les cartes coupées (c3, c4) |
| `compositions/disque-revelation.html` | 5,0 s | La révélation : le cercle dessiné au trait qui prend l'accent, la coupe sur la nuit, le cadre qui l'attrape, la montée, le trait qui tombe, la descente, la pose au point de fuite, les rayons, le nom | L'id `t02-revele`, `NOM`, `LOGO` (facultatif), les instants (`MOMENTS`) sur les temps de la musique |
| `compositions/disque-revelation-vertical.html` | 5,0 s | La même scène remise en page en 9:16 : le disque à 35 % de la hauteur, un trait plus long, la pose à 60 % | Comme la version 16:9 |
| `compositions/grille-final.html` | 8,0 s | L'offre et l'appel : la grille d'icônes qui se dessine et son élément phare sélectionné, le slogan géant et son point d'accent, le nom et ses repères, le point qui devient le bouton cliqué | L'id `t02-final`, les icônes (`ICONES` : une par élément réel de l'offre), `CHOISIE` et `ETIQUETTE`, le slogan (4 mots au plus), le nom (ou son logo en `<img>`), le libellé du bouton |
| `compositions/grille-final-vertical.html` | 8,0 s | La même scène remise en page en 9:16 : grille de 4 colonnes, slogan sur trois lignes, bouton aux deux tiers de la largeur au moins | Comme la version 16:9 ; le slogan sur trois lignes (`#t02-final-l1` à `l3`, 10 caractères au plus par ligne) |

Bout à bout dans cet ordre, elles font une vidéo de 22 s qui se tient seule. Essai du 06/11/2026 sur la marque sombre de LMDM, avec les vrais faits de Publicitaire IA, en 16:9 et en 9:16 : `check` sans erreur ni avertissement, `palette` « ok », `rythme` « ok » (1,58 événement par seconde dans les deux formats, écart médian 0,50 s, aucune image figée). Les palettes des cartes, les repères et le disque suivent n'importe quelle marque : rien ne se règle à la main.
