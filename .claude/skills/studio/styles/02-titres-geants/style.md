# Template n°2 · Titres géants · d'après Cyera (https://x.com/motionimo/status/2103703350017433670)

**Ce qu'on voit :** une charte graphique qui prend vie. Des titres si grands qu'ils débordent du cadre sur la couleur de la marque, un spécimen typographique posé sur une grille avec ses étiquettes de maquette, des cartes à coins ronds remplies de paysages illustrés au crépuscule, une sphère de verre qui livre le produit dans un faisceau de lumière, une grille d'icônes au trait fin, et le slogan géant qui finit dans l'espace.
**Souvent utile pour :** une vidéo de lancement ou d'accueil (la nouvelle offre, la nouvelle marque, l'ouverture d'un programme), en haut d'une page de vente ou en ouverture d'un webinaire.

**D'après :** le film de marque de Cyera réalisé par Motionimo · 16:9 · 30 s · musique seule, sans voix.
**Mesures de l'original** (`studio_motion.py reference`) : 1,71 événement par seconde, écart médian 0,40 s, 22 coupes franches, image figée la plus longue 1,2 s (le logo final).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 22 s, marque LMDM) : `rythme` 1,74 événement par seconde, écart médian 0,40 s, aucune image figée.

> On reprend la grammaire (rythme, mises en page, typographie, mouvements, transitions, façon de
> montrer le produit), jamais le contenu : ni ses textes, ni son logo, ni ses illustrations, ni sa
> musique. Tout passe aux couleurs et aux polices de la marque du client.

## 1. Le rythme

- **Une coupe franche toutes les 1,4 s en moyenne**, toujours sur un temps fort de la musique : la vidéo enchaîne des « pages » de charte (le titre, le spécimen, la carte, la mosaïque, la sphère, la grille, le slogan, le logo), chacune tenue 1 à 2,5 s.
- **Dans chaque page, un événement toutes les 0,25 à 0,4 s** : une graisse qui bascule, une lettre tapée, un repère qui se trace, une couche de paysage qui monte, une icône qui se dessine.
- **Rafales** : les icônes se dessinent à 0,03 s d'écart, les repères à 0,04 à 0,05 s, les cartes de la mosaïque arrivent à 0,06 s d'écart.
- **La caméra ne s'arrête jamais** : poussée lente (×1,00 à ×1,07 sur 2 s) pendant qu'on lit, recul rapide (0,6 à 0,9 s, `expo.inOut`) entre deux intentions.
- **Une seule respiration** : juste avant le logo final, l'énergie retombe une demi-seconde, puis le dernier temps fort tombe sur le nom.
- **Chez le client** : vise 1,5 événement par seconde au moins, une coupe franche toutes les 1 à 2 s, jamais une page tenue plus de 2,5 s, sauf l'écran final.

## 2. La structure

L'original est un film de marque : il présente une identité, pas une offre. Pour une vidéo qui vend, on garde ses pages et leur ordre, et on leur donne un rôle :

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Le titre géant | accroche | 1,5 à 2 s | La couleur d'accent plein écran, la promesse en trois lignes énormes qui débordent ; les mots changent de graisse sur les temps (`titre-geant.html`, plan A) |
| Le spécimen | problème ou promesse précisée | 2 s | Coupe sur le fond sombre : la phrase tapée lettre par lettre sur une grille, deux voix (gras, puis léger en retrait), étiquettes de maquette ; un cadre de sélection attrape un mot (`titre-geant.html`, plan B) |
| La carte paysage | solution : le produit apparaît | 3 s | Un coin arrondi et sa cote, la carte se remplit d'un paysage, des repères se posent, le nom de l'offre s'écrit en léger (`carte-paysage.html`) |
| La mosaïque | démonstration | 2 s | La caméra recule : six cartes arrivent autour, chacune avec un morceau du vrai produit (`carte-paysage.html`, fin) |
| La sphère et le faisceau | révélation | 5 s | Une sphère dessinée au trait prend sa couleur, flotte dans un canyon, monte et dépose le produit (un cube) dans un faisceau de lumière (`sphere-faisceau.html`) |
| La grille d'icônes | offre : ce qu'on reçoit | 2,4 s | Une icône par élément de l'offre, dessinée au trait fin ; un cadre attrape l'élément phare et son étiquette s'écrit (`grille-final.html`, plan A) |
| Les déclinaisons (facultatif) | preuve ou contenu | 1,5 à 2 s | Dans l'original, le nom décliné sur trois paysages qui changent toutes les 0,6 s ; chez le client, les parties de l'offre (modules, bonus, communauté) sur trois cartes, avec leurs vrais noms |
| Le slogan dans l'espace | promesse finale | 2 s | Deux lignes blanches géantes, la sphère passe derrière les lettres, des cubes dérivent (`grille-final.html`, plan B) |
| Le nom et le bouton | appel | 3,6 s | Le nom et ses repères, la sphère se pose et devient le bouton, le curseur le clique (`grille-final.html`, plan C) |

Une vidéo de page de 60 s double les pages du milieu (deux cartes paysage, deux sphères ou une sphère et une mosaïque de captures, les déclinaisons) ; un Reel de 25 s garde titre, carte, sphère, final.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Aubergine presque noir | le fond des pages sombres, la grille | `var(--brand-bg)` |
| Lilas vif | le titre géant en plein écran, le texte du spécimen | `var(--brand-accent)` (le titre est écrit en `var(--brand-contrast)` dessus) |
| Violets profonds, roses et pêche du crépuscule | les paysages, la sphère, l'espace | des teintes **dérivées de l'accent** en oklch relatif : plus sombres et décalées de teinte pour les ombres (`--t02-d`, -40 degrés par défaut ; +40 pour un accent vert, sinon le ciel tire sur le kaki), plus claires et moins saturées pour les lumières |
| Vert lime | le point qui bouge, les poignées, le surlignage, le logo final | l'accent lui-même : jamais une deuxième couleur inventée |
| Blanc cassé | la page du dessin au trait | blanc cassé teinté de 7 % d'accent |
| Blanc | le slogan, les titres posés sur un paysage | `var(--brand-text)` |

Les fonds alternent par coupe franche : accent plein, sombre quadrillé, sombre avec cartes, blanc cassé, paysage, espace, sombre. Au moins quatre bascules en 20 s. Avec un accent jaune, les paysages deviennent un coucher de soleil doré (ciel brun-orangé, horizon crème, îles brunes) ; avec un accent violet, on retrouve l'original.

## 4. La typographie

- **Police** : celle des titres de la marque (`var(--brand-font-display)`), en deux graisses : **600** pour la voix pleine, **400** pour la voix légère. L'original oppose une linéale (Haffer) et une serif fine (Season Mix), deux polices payantes. Si la marque n'impose rien : **Inter Tight** (titres, 500 et 600), et pour la voix légère **Instrument Serif** (Regular), ou à défaut Inter Tight 300 ; `studio_motion.py police "<Famille>"` les installe.
- **Casse** : celle de la phrase, minuscules, un point final sur les phrases courtes (« en grand. »).
- **Alignement** : à gauche, toujours ; le titre géant colle au bord gauche (30 px), la voix légère du spécimen est en retrait.
- **Approche** : serrée, -0,035 à -0,045 em sur les grands titres.
- **Interlignage** : 0,95 à 1 ; les lignes se frôlent. Si un jambage (p, g, q) tombe sur un accent ou un point de la ligne du dessous, on écarte la ligne ou on change la coupe.
- **Étiquettes de maquette** : 21 à 24 px, police du texte, blanc à 82 % ou gris de la marque ; elles disent une chose vraie (la police, la taille, le rayon), jamais du faux texte.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Titre géant (3 lignes, puis 6 en vertical) | 380 px, bases à 375 px d'écart | 300 px, un mot par ligne, bases à 318 px |
| Spécimen | 300 px, bases à 300 et 290 px | 220 px, bases à 230 et 216 px |
| Nom de l'offre dans la carte (voix légère) | 156 px | 110 px |
| Slogan final (2 lignes, blanc) | 236 px | 160 à 170 px, 3 lignes |
| Nom de la marque au final | 132 px | 96 px |
| Texte du bouton | 46 px dans une pilule de 120 px | 44 px dans une pilule de 112 px |
| Étiquettes, cotes | 21 à 24 px | 24 à 26 px |

## 5. Les mouvements signature

1. **Le titre qui déborde** (`titre-geant.html`) : trois lignes de 380 px qui touchent le haut et le bas du cadre ; le bloc pousse de ×1,00 à ×1,07 en 1,9 s (`power1.inOut`), la ligne du bas glisse de 210 px vers la gauche (`power2.inOut`) et révèle la fin de son mot coupé ; toutes les 0,4 s, un mot bascule de graisse d'un coup (600 ↔ 400), sans transition.
2. **Le spécimen tapé** (`titre-geant.html`) : chaque ligne se tape par groupes de lettres en 0,3 s (`K.taper`), la grille se trace (traits de 1 px, `scaleX` puis `scaleY` de 0 à 1 en 0,5 s, `expo.out`, 0,03 s d'écart), les étiquettes montent de 10 px (0,4 s, `expo.out`, 0,12 s d'écart) ; le cadre de sélection à quatre poignées se pose en 0,22 s (`power3.out`, depuis ×1,04), la ligne passe en gras et en blanc 0,2 s après, revient 0,3 s plus tard, et l'interlignage se resserre (0,35 s, `expo.inOut`) pendant que l'étiquette passe de « 100 % » à « 96 % ».
3. **Les repères de maquette** (dans les quatre scènes) : traits pleins de 2 px et traits pointillés qui se tracent en 0,42 s (`expo.out`, 0,05 s d'écart), points blancs de 16 px qui sautent (0,3 s, `back.out(2.5)`, 0,04 s d'écart), une bande assombrie qui marque la zone sélectionnée, une cote près d'un coin (« Rayon 64 px »). C'est le motif qui revient d'une page à l'autre.
4. **Le paysage qui se construit par couches** (`carte-paysage.html`) : le ciel en 0,25 s, la lueur de l'horizon qui s'ouvre (×0,2 à ×1, 0,5 s, `expo.out`), la mer qui descend de l'horizon (0,42 s), les reflets qui s'allongent depuis le centre (0,035 s d'écart), les îles lointaines qui montent de 30 px, les proches de 70 px, le rivage de 120 px (0,45 à 0,55 s, `expo.out`, 0,12 à 0,15 s d'écart). Puis la même carte change trois fois de palette sur les temps (jour, nuit, crépuscule, 0,16 s chacune).
5. **Le recul en mosaïque** (`carte-paysage.html`) : la caméra part à ×2,6 sur un coin, recule à ×1 en 0,62 s (`expo.inOut`), pousse doucement, puis recule à ×0,44 en 0,85 s pendant que six cartes arrivent de la droite (1 400 px, 0,85 s, `expo.out`, 0,06 s d'écart) ; dans la mosaïque, la vie continue (une liste se coche toutes les 0,18 s, un curseur clique un bouton, un lecteur avance).
6. **La sphère de verre** (`sphere-faisceau.html`, `grille-final.html`) : dessin au trait (`stroke-dashoffset`, 0,5 s, `power2.inOut`, 0,04 s d'écart), couleur en 0,24 s avec un gonflement (×0,86 à ×1, `back.out(1.6)`) ; elle tourne par ses hublots qui glissent derrière la silhouette (64 px sur toute la scène, vitesse constante), monte en 1,3 s (`power2.inOut`) en rapetissant à ×0,62 ; le trait de lumière tombe en 0,3 s (`power3.in`), le cône s'ouvre en 0,5 s (`expo.out`), le cube descend en 1,7 s (`power1.inOut`) en tournant de 230 degrés, et les rayons de perspective partent du point de pose (0,55 s, `expo.out`, 0,018 s d'écart).

## 6. Les transitions

- **La coupe franche sur un temps fort** est la transition principale : d'une page de charte à la suivante, d'un fond à l'autre, sans fondu.
- **Le raccord d'objet** : le point d'accent du coin devient le soleil du paysage ; les rayons de perspective du point de pose deviennent l'étoile qui ouvre la grille d'icônes ; la sphère du slogan vole sous le nom et devient le bouton.
- **Le recul de caméra** : une carte devient une mosaïque de cartes.
- **Le changement de palette** : la même mise en page, trois palettes en trois temps.
- Jamais de fondu enchaîné entre deux pages chargées ; une page disparaît par coupe, un repère par une opacité rapide (0,2 à 0,3 s).

## 7. Le produit à l'écran

- **Dans des cartes à coins ronds** (64 px pour 1 480 px de large) posées sur des paysages : le produit n'apparaît jamais seul sur un fond uni. Chaque carte porte un morceau du vrai produit, simplifié pour se lire petit : une liste de modules qui se coche, le bouton de la page cliqué par le curseur, un lecteur vidéo qui avance, une tuile avec l'icône de l'offre, ou une vraie capture (`<img>`).
- **En mosaïque** : la caméra recule et montre tout le produit d'un coup, cartes coupées aux bords du cadre.
- **Le cube** : le produit comme objet, livré par la sphère. Une face peut porter l'icône ou le logo de l'offre.
- Dans l'original, la plateforme apparaît aussi sur un ordinateur portable devant un coucher de soleil : chez le client, sa page ou son espace de formation dans une carte, ou dans une fenêtre du kit (`k-fenetre`) posée sur un paysage.
- Une carte sans matière réelle reste un paysage seul : jamais une interface inventée.

## 8. Le son

- **Original** : musique seule, sans voix ni bruitage marqué. Une nappe électronique aérienne, tempo estimé autour de 110 battements par minute ; une montée douce les 4 premières secondes (pendant la construction), l'énergie pleine dès la coupe sur le titre géant, une retombée d'une demi-seconde juste avant le logo final. Les coupes tombent sur les attaques de la musique (montées fortes mesurées à 4,3 s, 6,3 s, 7,9 s, 8,7 s, 10,1 s, 13,1 s, 14,5 s, 21,1 s, 21,9 s et 28,5 s).
- **Chez le client** : une musique de lancement inspirante, 100 à 120 battements par minute, avec une entrée franche et un dernier temps fort à garder pour le bouton (`studio_motion.py musiques choisir`). Les coupes et les bascules de graisse se calent sur ses temps.
- **Bruitages, légers** : un petit clic sur chaque cadre de sélection et sur le clic du curseur, un souffle bref sur les reculs de caméra et sur l'ouverture du faisceau, un impact grave sur le bouton qui se remplit. Rien sur les lettres tapées (trop de petits sons).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur la construction du logo (des points gris qui s'assemblent sur un blanc cassé, des traits de construction, le nom qui s'écrit, un surlignage vert à poignées), puis le logo blanc sur le sombre. Il finit sur le slogan géant dans l'espace, puis le logo sur le sombre, tenu 1,7 s.
- **Chez le client** : la vidéo s'ouvre directement sur le titre géant (la promesse se lit dès la première image, même sans le son) ; la construction du logo ne se garde que pour une vidéo d'accueil d'une marque qui a un vrai logo. Elle finit sur le slogan dans l'espace, puis le nom de la marque, ses repères et le bouton cliqué, tenus 2,5 s au moins avec des cubes qui dérivent. En page de vente, le bouton reprend le libellé du bouton sous la vidéo.

## Ce qui ne se fera pas à l'identique

- **Les deux polices** (Haffer et Season Mix, payantes) → la police de la marque en deux graisses ; la voix serif devient la graisse légère.
- **La construction du logo à partir de points** (faite pour leur logo) → pas de scène dans le kit ; le nom de la marque s'écrit lettre par lettre avec ses repères.
- **Les paysages peints, texturés, avec leurs détails au trait** → des paysages vectoriels en aplats et dégradés (ciel, lueur, mer, îles, falaises en gradins), plus simples.
- **Le violet avec son vert lime complémentaire** → une seule famille de teintes, dérivée de l'accent : la vidéo est plus monochrome que l'original.
- **La sphère** : un dessin vectoriel simplifié ; sa rotation est simulée par les hublots qui glissent, pas par un vrai modèle 3D.
- **Le portable photoréaliste et les objets dérivés** (casquette, carnet, sweat) → absents ; le cube du produit et les cartes les remplacent.
- **Les astéroïdes texturés** de la fin → des cubes du produit qui dérivent.
- **Le slogan devant la sphère** : dans l'espace, la sphère passe à contre-jour (assombrie à 58 %) derrière les lettres, pour que le slogan blanc reste lisible même quand l'accent est clair (jaune, pastel).

## Sur une autre offre

Le template est un look : il se monte sur n'importe quelle offre. Ce qui suivait l'original (une plateforme de sécurité) s'adapte :

- **Toujours** : le titre géant qui déborde, le spécimen sur sa grille, les repères de maquette, les cartes paysage, la sphère qui livre le cube, la grille d'icônes au trait, le slogan dans l'espace, les coupes sur les temps.
- **Une formation** : la mosaïque montre l'espace de formation et la liste des vrais modules qui se coche ; le cube est la formation ; une icône par module ou bonus ; le bouton « Je commence » ou le libellé de la page.
- **Un coaching** : les cartes montrent un créneau dans un agenda, l'écran d'un appel vidéo, de vrais messages de clients (captures) ; le cube est la séance ; une icône par étape de l'accompagnement ; le bouton « Je réserve mon appel ».
- **Un logiciel** : les cartes portent ses vraies interfaces (captures ou écrans reconstruits) et le curseur y clique ; une face du cube porte l'icône de l'app ; une icône par fonction ; le bouton « Essayer ».
- **Les déclinaisons** de l'original (le nom sur trois paysages) deviennent les trois parties de l'offre, avec leurs vrais noms.

## En vertical et en carré

- **9:16 (testé, `titre-geant-vertical.html`)** : le titre géant passe à un mot par ligne, six lignes de 300 px qui remplissent la hauteur, la dernière déborde à droite ; le spécimen passe à 220 px, posé un peu au-dessus du milieu (les commandes de l'application occupent le bas). On ne recadre jamais une scène 16:9 : on la remet en page.
- **Les autres scènes en 9:16** : la mosaïque en deux colonnes de cartes 16:9 (900 px de large) sur trois rangées ; le canyon plus haut, la sphère à 35 % de la hauteur, le faisceau plus long ; la grille d'icônes en 4 colonnes et 6 rangées ; le slogan sur trois lignes de 160 à 170 px ; le bouton aux deux tiers de la largeur, au-dessus de la bande du bas.
- **4:5 et 1:1** : le titre géant en quatre lignes de 260 px (4:5) ou trois lignes de 240 px (1:1) ; la mosaïque en 2 × 2 ; le reste suit le 16:9 resserré au centre.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical ; seul le titre géant déborde exprès, et sa ligne clé reste au milieu.

## Les compositions du kit

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/titre-geant.html` | 4,0 s | L'accroche : le titre géant qui déborde sur l'accent (1,9 s), coupe, le spécimen tapé sur sa grille avec ses étiquettes et son cadre de sélection (2,1 s) | L'id `t02-titre`, les trois lignes du titre (un `<span>` par mot), les trois lignes du spécimen (`data-texte`), les instants des bascules (`BASCULES`) |
| `compositions/titre-geant-vertical.html` | 4,0 s | La même scène remise en page en 9:16 : six lignes d'un mot, spécimen à 220 px | Comme la version 16:9 ; un mot par ligne, 6 caractères au plus sur les lignes du milieu |
| `compositions/carte-paysage.html` | 5,0 s | Le produit : le coin et sa cote, la carte qui se remplit d'un paysage, les repères, le nom en léger, trois palettes sur les temps, puis la mosaïque de six cartes avec des morceaux du produit | L'id `t02-carte`, le nom de l'offre et la ligne dessous, le contenu des cartes (`CARTES` : ses vraies captures, ses vrais modules, le vrai libellé du bouton), leur palette et leur relief |
| `compositions/sphere-faisceau.html` | 5,0 s | La révélation : la sphère dessinée au trait qui prend sa couleur, le canyon, la montée, le faisceau, le cube qui se pose, les rayons de perspective | L'id `t02-sphere`, les faces du cube (l'icône ou le logo de l'offre), les instants (`MOMENTS`) sur les temps de la musique ; aucun texte |
| `compositions/grille-final.html` | 8,0 s | L'offre et l'appel : la grille d'icônes qui se dessine et son élément phare sélectionné, le slogan géant dans l'espace avec la sphère, le nom et ses repères, la sphère qui devient le bouton cliqué | L'id `t02-final`, les icônes (`ICONES` : une par élément réel de l'offre), `CHOISIE` et `ETIQUETTE`, le slogan (4 mots au plus), le nom (ou son logo en `<img>`), le libellé du bouton |

Bout à bout dans cet ordre, elles font une vidéo de 22 s qui se tient seule (essai : `rythme` « ok », `check` sans erreur). Le changement de palette, les repères et les teintes dérivées marchent avec n'importe quel accent ; `--t02-d` se règle une fois par marque (+40 pour un accent vert).
