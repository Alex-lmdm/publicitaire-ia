# Style n°2 · Titres géants · d'après Cyera (https://x.com/motionimo/status/2103703350017433670)

**Ce qu'on voit :** une charte graphique qui prend vie, aux seules couleurs de la marque, autour de sa vraie matière. Des titres si grands qu'ils débordent du cadre sur sa couleur d'accent, un spécimen tapé sur une grille, une carte à coins ronds qui s'ouvre sur sa vraie capture et change de palette sur les temps, une mosaïque de cartes qui portent ses captures, ses chiffres, ses modules et le bouton de sa page, un disque qui porte son logo et pose le nom de l'offre avec sa phrase, une grille d'une case par élément réel de l'offre, et le slogan géant dont le point devient le bouton. Les cadres à poignées et les repères attrapent, mesurent et révèlent ; aucune étiquette technique.
**Souvent utile pour :** une vidéo de lancement ou d'accueil (la nouvelle offre, la nouvelle marque, l'ouverture d'un programme), en haut d'une page de vente ou en ouverture d'un webinaire.

**D'après :** le film de marque de Cyera réalisé par Motionimo · 16:9 · 30 s · musique seule, sans voix.
**Mesures de l'original** (`studio_motion.py reference`) : 1,71 événement par seconde, écart médian 0,40 s, 22 coupes franches, image figée la plus longue 1,2 s (le logo final).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 32,5 s, marque LMDM, vraie matière de la story d'ouverture, 06/11/2026) : `rythme` 1,35 événement par seconde en 16:9 et 1,18 en 9:16, écart médian 0,60 s, aucune image figée ; `palette` « ok » dans les deux formats. Chaque phrase tenue au moins le temps de sa lecture : la vidéo est plus lente que l'original, exprès.

> On reprend la grammaire (mises en page, typographie, mouvements, transitions, façon de montrer
> le produit), jamais le contenu : ni ses textes, ni son logo, ni ses images (paysages, sphère,
> planète, objets), ni ses couleurs, ni sa musique, ni son tempo de lecture. Ce qu'on voit vient du
> client et se peint aux seules couleurs de sa marque.

## 1. Le rythme

- **L'original coupe toutes les 1,4 s** sur les temps forts de la musique : une identité, pas une offre, presque sans texte à lire. Chez le client, **la phrase décide de la tenue** : chaque page reste au moins le temps de lire la sienne (`studio_motion.py lecture`, 0,3 s par mot + 0,8 s, jamais moins de 1,5 s ; la carte de fin 3 s), puis la coupe tombe sur le temps fort suivant. Les scènes du kit placent seules leurs coupes d'après leurs textes et disent dans la console s'il manque du temps à leur data-duration.
- **Pendant qu'on lit, la vie vient de la phrase et de sa matière**, un événement toutes les 0,5 à 0,8 s : une graisse qui bascule sur les temps, une lettre tapée, la bande qui change de palette, le mot clé surligné d'un bloc d'accent, le cadre à poignées qui attrape le nom, un chiffre qui monte, une case qui se coche. Une tenue sans rien autour ne dépasse jamais 0,8 s (`rythme` la compte comme une image figée).
- **Rafales** : les icônes se dessinent à 0,03 s d'écart, les repères à 0,04 à 0,05 s, les cartes de la mosaïque arrivent à 0,06 s d'écart.
- **La caméra pendant la lecture** : une dérive lente seulement (×1,00 à ×1,045 sur toute la tenue, `sine.inOut`). Les gestes de caméra du style (l'approche d'un coin, le recul en mosaïque, la montée et la descente du disque, l'approche d'une case) tombent entre deux phrases, jamais sous un texte qu'on lit ; aucun recadrage sec dans les cinq premières secondes (le titre géant ne bouge que lentement).
- **Une seule respiration** : juste avant le nom final, l'énergie retombe une demi-seconde, puis le dernier temps fort tombe sur le nom.
- **Chez le client** : 1,2 événement par seconde au moins, une coupe franche entre deux phrases, jamais une phrase coupée avant sa lecture.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le titre qui déborde | une phrase en trois lignes énormes sur l'accent plein écran, lisible dès la première image, deux mots qui changent de graisse sur les temps | accroche, promesse, temps fort | `titre-geant` (plan A) |
| Le spécimen tapé | une phrase tapée sur une grille, en deux voix ; un cadre de sélection attrape la ligne légère, qui passe en gras | problème, promesse précisée, prix | `titre-geant` (plan B) |
| Les repères de maquette | traits, pointillés, points et cadres à poignées qui attrapent, mesurent et révèlent une vraie matière : le motif qui revient d'une scène à l'autre, sans aucune étiquette technique | toutes les scènes, celles construites pour son cas comprises | toutes les scènes |
| La carte et la mosaïque | un point d'accent file au centre d'une carte et s'ouvre sur sa vraie capture ; la bande du nom, trois palettes sur les temps ; puis la caméra recule sur six cartes de sa vraie matière (captures, bouton, modules, chiffre) | solution, démonstration de son produit | `carte-mosaique` |
| Le disque qui pose le nom | un cercle dessiné au trait se remplit de son logo (ou d'une capture, d'un vrai chiffre) cerclé d'accent, monte, redescend le long d'un trait de marque et se pose au point de fuite ; les rayons partent, le nom s'écrit, sa phrase se pose, un surlignage à poignées attrape le nom | révélation, le nom de l'offre et ce qu'elle fait | `disque-revelation` |
| La grille d'icônes | une case par élément réel de l'offre (ses outils par leur vrai logo) ; la caméra s'approche de l'élément phare, il se remplit d'accent et son vrai nom se surligne | ce qu'on reçoit | `grille-final` (plan A) |
| Le slogan géant et le bouton | une phrase de sa page en deux lignes géantes sur la nuit, son point final est un disque d'accent qui file sous le nom et devient le bouton que le curseur clique | promesse finale, appel | `grille-final` (plans B et C) |

Les déclinaisons de l'original (le nom de la marque sur trois images) deviennent les trois parties
réelles de l'offre, sur trois cartes, avec leurs vraies captures ou leurs vrais noms.

### L'original, pour mémoire

L'original est un film de marque : il présente une identité, pas une offre. Ses pages, dans l'ordre, avec le rôle que chacune peut tenir ; ses images (paysages, sphère, objets) ne se refont jamais et ne deviennent pas des formes : seuls leurs mouvements passent dans le kit, autour de la vraie matière du client.

| Bloc | Rôle | Durée chez le client | Ce qui s'y passe |
|---|---|---|---|
| Le titre géant | accroche | la lecture de sa phrase (2,6 s pour 6 mots) | La couleur d'accent plein écran, la promesse en trois lignes énormes qui débordent ; deux mots changent de graisse sur les temps (`titre-geant.html`, plan A) |
| Le spécimen | problème, promesse précisée ou prix | 0,9 s de frappe + sa lecture | Coupe sur le fond sombre : la phrase tapée sur une grille, deux voix (gras, puis léger en retrait) ; un cadre de sélection attrape la ligne légère (`titre-geant.html`, plan B) |
| La carte | solution : le produit apparaît | 3,6 à 4 s | Un coin arrondi et son trait de marque ; dans l'original, la carte se remplit d'un paysage peint ; chez le client, le point d'accent s'ouvre sur sa vraie capture, la bande du nom s'écrit en léger, la bande change de palette pendant la lecture (`carte-mosaique.html`) |
| La mosaïque | démonstration | 2,5 s | La caméra recule : six cartes arrivent autour, chacune avec un morceau du vrai produit (`carte-mosaique.html`, fin) |
| La révélation | révélation | 3,5 s de trajet + la lecture du nom et de sa phrase | Dans l'original, une sphère de verre dessinée au trait prend sa couleur, flotte dans un canyon et dépose le produit dans un faisceau de lumière ; chez le client, un disque qui porte son logo fait le même trajet sur la nuit et pose le nom de l'offre et sa phrase au point de fuite (`disque-revelation.html`) |
| La grille d'icônes | offre : ce qu'on reçoit | 2,65 s + la lecture du nom de l'élément phare | Une case par élément réel de l'offre, dessinée au trait fin ; la caméra s'approche de l'élément phare, un cadre l'attrape, il se remplit d'accent, son nom s'écrit et se surligne (`grille-final.html`, plan A) |
| Les déclinaisons (facultatif) | preuve ou contenu | la lecture de chaque nom | Dans l'original, le nom décliné sur trois images ; chez le client, les parties de l'offre (modules, bonus, communauté) sur trois cartes, avec leurs vraies captures ou leurs vrais noms |
| Le slogan | promesse finale | 1,2 s d'entrée + sa lecture | Deux lignes blanches géantes (dans l'original, dans un espace peint) ; chez le client, sur la nuit quadrillée, leur point final en disque d'accent, deux mots qui changent de graisse (`grille-final.html`, plan B) |
| Le nom et le bouton | appel | 4,2 s au moins | Le nom et ses repères ; le point du slogan se pose et devient le bouton, le curseur le clique ; tenue de 3 s au moins (`grille-final.html`, plan C) |

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

Une vidéo de page de 60 s double les pages du milieu (deux cartes, une mosaïque de captures, la révélation, les déclinaisons) ; un Reel de 30 s garde titre, carte, révélation, final.

## 3. Les fonds et les couleurs

Ses couleurs, rien d'autre ([../../references/style.md](../../references/style.md), « La palette ») :
la nuit, le clair et les gris de sa marque, et son accent posé plein.

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Aubergine presque noir | le fond des pages sombres, la grille, l'espace | `var(--brand-sombre)`, la couleur la plus sombre de sa marque (sur une marque claire, son texte), sur toutes les pages de nuit ; la grille en blanc à 5 % |
| Lilas vif | le titre géant en plein écran, le texte du spécimen | `var(--brand-accent)` pour le plein écran (le titre est écrit en `var(--brand-contrast)` dessus) ; le spécimen, posé sur la nuit, en `var(--brand-accent-lisible)` (l'accent, ou son clair s'il ne se lit pas sur la nuit) |
| Violets, roses et pêche du crépuscule | les paysages, la sphère, l'espace | rien : ces images ne se refont pas. À leur place, sa vraie matière : ses captures (sa page, son produit, ses résultats), son logo dans le disque, ses vrais chiffres. Les fonds de carte de sa palette (accent, clair, gris, sombre) ne sont que des cadres |
| Vert lime | le point qui bouge, les poignées, le surlignage, le logo final | l'accent lui-même, plein : jamais une deuxième couleur inventée |
| Blanc cassé | la page du dessin au trait | `var(--brand-clair)`, le trait en `var(--brand-sombre)` |
| Blanc | le slogan, les titres | `var(--brand-clair)` |

**Les traits.** Un trait discret (la grille, les rayons, les repères sur la nuit) est du blanc en
transparence, donc un gris ; un trait de marque (le cadre de sélection, ses poignées, le trait qui
tombe du disque, le repère du bouton) est l'accent plein et fin (`--brand-accent-lisible` sur la
nuit). Aucun dégradé ne touche l'accent, aucune teinte n'en est tirée, aucun accent ne reste en
transparence : une carte d'accent arrive en glissant, un disque d'accent grandit, un texte d'accent
se tape ; jamais de fondu ni de flou sur l'accent (sur la nuit, un jaune flou ou à moitié
transparent devient olive : essai du 06/11/2026, la ligne légère du spécimen entrée en flou).

**Sur n'importe quelle marque, claire ou sombre.** La nuit est toujours `--brand-sombre` : sur une
marque claire, c'est la couleur de son texte, et le look reste nocturne, à ses couleurs (essai du
06/11/2026 aux couleurs de Dupliq.me, accent orange sur sa nuit : tout se lit). Le texte posé sur la
nuit est `--brand-clair` ; tout texte garde un contraste d'au moins 4,5:1 (un accent sombre qui
colore un texte sur la nuit passe par `--brand-accent-lisible`).

Les fonds alternent par coupe franche : accent plein, nuit quadrillée, sa capture dans la carte, ses
palettes, mosaïque, clair du dessin au trait, nuit. Au moins quatre bascules en 30 s.

## 4. La typographie

- **Police** : celle des titres de la marque (`var(--brand-font-display)`), en deux graisses : **600** pour la voix pleine, **400** pour la voix légère. L'original oppose une linéale (Haffer) et une serif fine (Season Mix), deux polices payantes. Si la marque n'impose rien : **Inter Tight** (titres, 500 et 600), et pour la voix légère **Instrument Serif** (Regular), ou à défaut Inter Tight 300 ; `studio_motion.py police "<Famille>"` les installe.
- **Une phrase entière par page**, jamais des mots isolés : le titre géant, le spécimen, le nom et sa phrase, le nom de l'élément phare, le slogan sont chacun une phrase de sa page ou de sa fiche.
- **Casse** : celle de la phrase, minuscules, un point final sur les phrases courtes (« en grand. ») ; le point final du slogan est le disque d'accent.
- **Alignement** : à gauche, toujours ; le titre géant colle au bord gauche (30 px), la voix légère du spécimen est en retrait. Le nom de l'offre se centre (dans la bande de la carte, au-dessus du disque, au final).
- **Approche** : serrée, -0,035 à -0,045 em sur les grands titres.
- **Interlignage** : 0,95 à 1 ; les lignes se frôlent. Si un jambage (p, g, q) tombe sur un accent ou un point de la ligne du dessous, on écarte la ligne ou on change la coupe.
- **Étiquettes** : une étiquette écrite porte une info réelle de la fiche (le prix, la date, le nom de l'offre, un chiffre de preuve) ou n'existe pas. Les étiquettes de maquette de l'original (la police et sa taille, le rayon, la couleur et son code) ne disent rien à son public et passent pour des restes oubliés (relecteur neuf de la story refusée du 06/11/2026) : elles sont réservées à une vidéo qui parle de design (une marque, un template).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Titre géant (3 lignes, puis 6 en vertical) | 380 px, bases à 375 px d'écart | 300 px, un mot par ligne, bases à 318 px |
| Spécimen | 300 px, bases à 300 et 290 px | 180 px, bases à 186 et 176 px, dans la zone de texte d'un Reel |
| Nom de l'offre dans la carte (voix légère) | 156 px (réduit s'il déborde de la bande) | 110 px, sur deux lignes s'il le faut |
| Chiffre d'une carte de la mosaïque, son contexte | 230 px, 62 px | 200 px, 54 px |
| Nom posé par le disque, sa phrase | 120 px, 58 px (voix légère) | 104 px, 54 px |
| Nom de l'élément phare de la grille | 44 px (66 px à l'écran, caméra approchée) | 40 px (60 px à l'écran) |
| Slogan final (blanc) | 236 px, 2 lignes | 166 px, 3 lignes |
| Nom de la marque au final | 132 px | 96 px |
| Texte du bouton | 46 px dans une pilule de 120 px, élargie à son libellé | 44 px dans une pilule de 112 px, aux deux tiers de la largeur au moins |

## 5. Les mouvements signature

1. **Le titre qui déborde** (`titre-geant.html`) : trois lignes de 380 px qui touchent le haut et le bas du cadre, lisibles dès la première image et tenues le temps de leur lecture ; le bloc pousse de ×1,00 à ×1,045 sur toute la tenue (`sine.inOut`), la ligne du bas glisse lentement vers la gauche (1,8 s au plus, `sine.inOut`, juste assez pour montrer la fin de son mot coupé, mesuré à la police) ; toutes les 0,5 s, un mot de la ligne du milieu bascule de graisse d'un coup (600 ↔ 400), sans transition.
2. **Le spécimen tapé** (`titre-geant.html`) : les trois lignes se tapent par groupes de lettres (la dernière posée 0,9 s après la coupe, `K.taper`) ; la grille se trace (traits de 1 px en blanc transparent, `scaleX` puis `scaleY` de 0 à 1 en 0,5 s, `expo.out`, 0,03 s d'écart) ; le cadre de sélection à quatre poignées se pose sur la ligne légère (0,22 s, `power3.out`, depuis ×1,04), elle passe en gras et en clair, revient 0,7 s plus tard ; le texte ne bouge pas, la caméra dérive (×1,03).
3. **Les repères de maquette** (dans les quatre scènes) : traits pleins de 2 px et traits pointillés qui se tracent en 0,42 s (`expo.out`, 0,05 s d'écart) et se rétractent de même, points clairs de 16 px qui sautent (0,3 s, `back.out(2.5)`, 0,04 s d'écart), cadres à quatre poignées qui attrapent un disque, une ligne, un nom ou une case. Ils mesurent et désignent une vraie matière ; aucun n'écrit de cote.
4. **La carte qui se construit par couches** (`carte-mosaique.html`) : la caméra recule du coin (×2,6 à ×1 en 0,6 s, `expo.inOut`) pendant que le point d'accent file au centre ; il s'ouvre en cercle jusqu'aux bords (0,48 s, `power3.inOut`) sur sa vraie capture : le point n'est le sujet que 0,8 s ; la bande du nom s'ouvre depuis le centre (0,5 s, `expo.out`, au tiers bas sur une capture), les repères la mesurent, le nom entre mot par mot en voix légère, sa marque dessous dans une pastille. Pendant que le nom se lit, la bande change trois fois de palette sur les temps (0,3 s d'écart).
5. **Le recul en mosaïque** (`carte-mosaique.html`) : une fois le nom lu, la caméra recule à ×0,44 en 0,85 s (`expo.inOut`) pendant que six cartes arrivent de la droite, de hors champ, et glissent sous la grande (0,85 s, `expo.out`, 0,06 s d'écart, sans fondu) ; dans la mosaïque, la vie continue (un vrai chiffre qui monte, une liste qui se coche toutes les 0,18 s, le curseur qui clique le bouton qui se remplit) et la caméra dérive.
6. **Le disque qui pose le nom** (`disque-revelation.html`) : sur le clair, un cercle se dessine au trait avec son carré de construction (`stroke-dashoffset`, 0,45 s, `power2.inOut`, 0,05 s d'écart) et se remplit d'un coup de sa vraie matière, cerclée d'accent, en gonflant (×0,86 à ×1, `back.out(1.6)`, à 0,55 s) ; coupe sur la nuit : un cadre de sélection l'attrape (0,22 s, `power3.out`), il monte en 1,1 s (`power2.inOut`) en rapetissant à ×0,62 pendant que la caméra lève les yeux ; le trait de marque tombe en 0,3 s (`power3.in`), deux traits de construction s'ouvrent en cône (0,5 s, `expo.out`) ; il redescend le long du trait en 1,2 s (`power1.inOut`), la caméra revient, l'horizon se trace (0,6 s, `expo.out`) ; posé au point de fuite, les rayons de perspective partent de lui (0,55 s, `expo.out`, 0,018 s d'écart), le nom s'écrit lettre par lettre, sa phrase se pose dessous mot par mot. Pendant la lecture : le mot clé de la phrase se surligne d'un bloc d'accent, un cadre à poignées attrape le nom, un bloc d'accent le remplit (le surlignage de l'original), un mot du nom change de graisse sur les temps, le surlignage se retire 0,9 s avant la coupe.
7. **La case phare et le point qui devient le bouton** (`grille-final.html`) : la grille dessinée, la caméra s'approche de la case phare (×1,5 en 0,9 s, `expo.inOut`) avant tout texte ; un cadre l'attrape, son vrai nom se tape, la case se remplit d'un disque d'accent (0,4 s, `back.out(2)`), les autres passent au flou, le nom se surligne. Le point final du slogan est un disque d'accent qui tombe en place (0,45 s, `back.out(2.4)`, sans fondu) ; pendant la lecture du slogan, deux mots changent de graisse ; à la coupe, le point file sous le nom (0,55 s, `expo.inOut`) et y plonge (0,16 s) ; le bouton naît de lui, un rond qui s'étire en pilule (0,45 s, `expo.out`) ; au clic, l'accent le remplit depuis le centre (0,4 s, `power3.out`).

## 6. Les transitions

- **La coupe franche sur un temps fort** est la transition principale : d'une page de charte à la suivante, une fois sa phrase lue, d'un fond à l'autre, sans fondu.
- **Le raccord d'objet** : le point d'accent du coin s'ouvre sur la capture de la carte ; les rayons du point de pose deviennent l'étoile qui ouvre la grille d'icônes ; le point du slogan file sous le nom et devient le bouton.
- **Le recul de caméra** : une carte devient une mosaïque de cartes, entre deux phrases.
- **Le changement de palette** : la même mise en page, trois palettes de sa marque en trois temps.
- Jamais de fondu enchaîné entre deux pages chargées ; une page disparaît par coupe, un repère en se rétractant (0,2 à 0,3 s).

## 7. Le produit à l'écran

- **Dans des cartes à coins ronds** (64 px pour 1 480 px de large) : le produit n'apparaît jamais seul sur un fond uni. La grande carte porte toujours une vraie capture (`image` : sa page, son espace de formation, son logiciel, un résultat ; `cadrage` choisit la partie montrée) ; les autres descendent l'échelle de [../../references/style.md](../../references/style.md) (« Aucune image inventée ») : une capture, son interface reconstruite (la liste de ses vrais modules qui se coche, le vrai libellé du bouton de sa page cliqué par le curseur), un vrai chiffre de la fiche qui monte avec son contexte, puis un mot de sa page.
- **En mosaïque** : la caméra recule et montre tout le produit d'un coup. Un aplat de sa palette n'est qu'un cadre : une ou deux cartes coupées par les bords au plus, jamais la grande.
- **Le disque** : il porte son logo (`LOGO`, l'icône de sa marque), sinon une vraie capture découpée dans le disque (`IMAGE`), sinon un vrai chiffre (`CHIFFRE`), dès qu'il prend sa couleur ; jamais un aplat seul qui monte et redescend (essai du 06/11/2026 : un disque jaune seul sous le nom).
- **La grille** : une case par élément réel de l'offre (ses modules, ses bonus, ses outils par leur vrai logo), autant de cases qu'il y en a ; le nom de l'élément phare le dit.
- Dans l'original, la plateforme apparaît aussi sur un ordinateur portable devant un coucher de soleil : chez le client, sa page ou son espace de formation en vraie capture dans une carte, ou dans une fenêtre du kit (`k-fenetre`) posée sur la nuit ou sur un aplat de sa palette.
- Sans aucune capture (c'est la question unique du repérage), la grande carte garde ses mots dans la bande ; jamais une interface inventée, un faux lecteur vidéo, une icône de décor, une forme 3D ni une image redessinée.

## 8. Le son

- **Original** : musique seule, sans voix ni bruitage marqué. Une nappe électronique aérienne, tempo estimé autour de 110 battements par minute ; une montée douce les 4 premières secondes (pendant la construction), l'énergie pleine dès la coupe sur le titre géant, une retombée d'une demi-seconde juste avant le logo final. Les coupes tombent sur les attaques de la musique (montées fortes mesurées à 4,3 s, 6,3 s, 7,9 s, 8,7 s, 10,1 s, 13,1 s, 14,5 s, 21,1 s, 21,9 s et 28,5 s).
- **Chez le client** : une musique de lancement inspirante, 100 à 120 battements par minute, avec une entrée franche et un dernier temps fort à garder pour le bouton (`studio_motion.py musiques choisir`). Les coupes et les bascules de graisse se calent sur ses temps, sans jamais raccourcir une tenue de lecture.
- **Bruitages, légers** : un petit clic sur chaque cadre de sélection et sur le clic du curseur, un souffle bref sur les reculs de caméra et sur la chute du trait, un impact grave sur la pose du disque et sur le bouton qui se remplit. Rien sur les lettres tapées (trop de petits sons).
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 2`) : « Lancement énergique » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur la construction du logo (des points gris qui s'assemblent sur un blanc cassé, des traits de construction, le nom qui s'écrit, un surlignage vert à poignées), puis le logo blanc sur le sombre. Il finit sur le slogan géant, puis le logo sur le sombre, tenu 1,7 s.
- **Chez le client** : la vidéo s'ouvre directement sur le titre géant (la promesse se lit dès la première image, même sans le son, sur une image qui ne bouge que lentement) ; le surlignage à poignées passe sur le nom posé par le disque. Elle finit sur le slogan géant et son point, puis le nom de la marque, ses repères et le bouton cliqué, tenus 3 s au moins (le plan pousse doucement). En page de vente, le bouton reprend le libellé du bouton sous la vidéo ; en pub, ni bouton ni curseur : « Découvre-le » et une flèche vers le bas.

## Ce qui ne se fera pas à l'identique

- **Les deux polices** (Haffer et Season Mix, payantes) → la police de la marque en deux graisses ; la voix serif devient la graisse légère.
- **La construction du logo à partir de points** (faite pour leur logo) → pas de scène dans le kit ; son logo se pose dans le disque, le nom s'écrit lettre par lettre et le surlignage à poignées l'attrape.
- **Le tempo de lecture de l'original** (une page toutes les 1,4 s, presque sans texte) → chaque phrase du client tenue le temps de sa lecture.
- **Les images de l'original ne se refont pas et ne deviennent pas des formes** : ni les paysages peints au crépuscule, ni la sphère de verre et son canyon, ni la planète et l'espace, ni le portable photoréaliste, ni les objets dérivés (casquette, carnet, sweat), ni les astéroïdes et les cubes. À leur place, la vraie matière du client, en descendant l'échelle : ses captures (sa page, son produit, ses vidéos, ses résultats), son interface reconstruite, ses vrais chiffres, les vrais logos de ses outils, puis ses mots ; la révélation passe par un disque qui porte son logo, le slogan se pose sur la nuit.
- **Les étiquettes de maquette** (police, taille, rayon, code couleur) → aucune par défaut : seulement une info réelle de la fiche, ou rien.
- **Le violet avec son vert lime complémentaire** → la palette de sa marque et rien d'autre : l'accent plein sur ses neutres (sa nuit, son clair, ses gris) ; la vidéo est plus graphique que l'original.
- **Le faisceau de lumière** → un trait de marque fin et deux traits de construction : aucun halo, aucune lueur.

## Sur une autre offre

Le style est une façon de présenter : il se monte sur n'importe quelle offre. Ce qui suivait l'original (une plateforme de sécurité) s'adapte, et chaque geste porte sa vraie matière :

- **Toujours** : le titre géant qui déborde, le spécimen sur sa grille, les repères et les cadres à poignées, la carte qui s'ouvre sur sa capture et sa mosaïque, le disque qui porte son logo et pose le nom avec sa phrase, la grille d'une case par élément réel, le slogan et son point qui devient le bouton, une coupe franche après chaque phrase lue.
- **Une formation** : la carte s'ouvre sur son espace de formation en capture ; la mosaïque montre une leçon, la liste des vrais modules qui se coche, le nombre réel de modules ou d'heures qui monte, un message d'élève en capture ; le disque porte son logo et pose « Nom + ce que la formation apprend » ; une case par module ou bonus ; le bouton « Je commence » ou le libellé de la page.
- **Un coaching** : la carte s'ouvre sur sa page ; les cartes montrent un créneau de son agenda, l'écran d'un appel, de vrais messages de clients (captures) ; le disque porte son logo ou sa photo de profil et pose le nom de l'accompagnement et sa promesse ; une case par étape de l'accompagnement ; le bouton « Je réserve mon appel ».
- **Un logiciel** : la carte s'ouvre sur son interface ; les cartes portent ses vraies interfaces (captures ou écrans reconstruits) et le curseur y clique ; le disque porte l'icône de l'app ; une case par fonction, les outils qu'il relie par leur vrai logo ; le bouton « Essayer ».
- **Sans logo** : le disque porte une capture découpée (sa page, son produit) ou un vrai chiffre (« 67 € », « 34 achats »).
- **Les déclinaisons** de l'original (le nom sur trois images) deviennent les trois parties de l'offre, avec leurs vraies captures ou leurs vrais noms.

## En vertical et en carré

- **9:16 : chaque scène a sa version verticale, testée** sur la marque sombre de LMDM (les quatre bout à bout, 32,5 s : `rythme` et `palette` « ok ») et contrôlée aux couleurs de Dupliq.me. Prends le fichier `-vertical.html` à la place du 16:9 : on ne recadre jamais une scène 16:9, on la remet en page.
  - `titre-geant-vertical.html` : le titre géant passe à un mot par ligne, six lignes de 300 px qui remplissent la hauteur, la dernière déborde à droite ; le spécimen passe à 180 px et tient dans la zone de texte d'un Reel (x 100 à 930 : 8 caractères au plus par ligne grasse), posé un peu au-dessus du milieu (les commandes de l'application occupent le bas).
  - `carte-mosaique-vertical.html` : les cartes passent en portrait (960 × 1 360 px) et la grande remplit l'image : une vraie image en hauteur (sa pub, sa story, son Reel) la remplit mieux qu'une capture d'écran large ; le nom passe sur deux lignes s'il est long ; au recul, la mosaïque met deux cartes par rangée sur trois rangées (la grande au centre de la rangée du milieu, entre deux cartes coupées par les bords : des aplats, de simples cadres). Le bouton et la liste vont sur la rangée du haut, des images sur celle du bas (sous les commandes de l'application).
  - `disque-revelation-vertical.html` : le disque monte jusqu'à 35 % de la hauteur, le trait descend d'environ 1 500 px jusqu'à l'horizon, posé aux deux tiers de la hauteur ; le nom (104 px) et sa phrase (54 px, trois lignes au plus) au-dessus, hors des 10 % du haut.
  - `grille-final-vertical.html` : la grille d'icônes en 4 colonnes ; le slogan sur trois lignes de 166 px (10 caractères au plus par ligne) ; le nom à 96 px et le bouton aux deux tiers de la largeur au moins (720 px), au-dessus de la bande du bas, son repère dessous.
- **4:5 et 1:1** : le titre géant en quatre lignes de 260 px (4:5) ou trois lignes de 240 px (1:1) ; la mosaïque en 2 × 2 ; le reste suit le 16:9 resserré au centre.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical ; seul le titre géant déborde exprès, et sa ligne clé reste au milieu.

## Les compositions du kit

Chaque scène lit sa durée dans son data-duration (et celui de son hôte), place ses coupes d'après la lecture de ses textes et écrit dans la console la durée qu'il lui faut si elle manque de temps.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/titre-geant.html` | 5,6 s | L'accroche : le titre géant qui déborde sur l'accent, tenu le temps de sa lecture, coupe, le spécimen tapé sur sa grille et son cadre de sélection | L'id `t02-titre`, les trois lignes du titre (un `<span>` par mot, une phrase entière), les trois lignes du spécimen (`data-texte`), `ETIQUETTES` (facultatives : une info réelle), `COUPE` et les bascules (`BASCULES`) ; data-duration = COUPE + 0,9 s + lecture du spécimen |
| `compositions/titre-geant-vertical.html` | 5,6 s | La même scène remise en page en 9:16 : six lignes d'un mot, spécimen à 180 px | Comme la version 16:9 ; un mot par ligne, 6 caractères au plus sur les lignes du milieu |
| `compositions/carte-mosaique.html` | 6,6 s | Le produit : le coin et son trait de marque, le point d'accent qui s'ouvre sur sa vraie capture, la bande, les repères, le nom en léger, trois palettes pendant sa lecture, puis la mosaïque de six cartes de sa matière | L'id `t02-carte`, `NOM` et `MARQUE`, les cartes (`CARTES` : la grande avec sa capture en `image` et son `cadrage`, puis ses captures, le vrai libellé du bouton, ses vrais modules, un vrai chiffre et son contexte) ; data-duration = l'instant du recul + 2,5 s |
| `compositions/carte-mosaique-vertical.html` | 6,6 s | La même scène remise en page en 9:16 : cartes en portrait, la grande plein cadre, puis la mosaïque de deux cartes par rangée sur trois rangées | Comme la version 16:9 ; la matière sur les cartes entières (c1, c2, c5, c6), les cartes coupées (c3, c4) en aplats |
| `compositions/disque-revelation.html` | 7,7 s | La révélation : le cercle dessiné au trait qui se remplit de son logo, la coupe sur la nuit, le cadre qui l'attrape, la montée, le trait qui tombe, la descente, la pose au point de fuite, les rayons, le nom et sa phrase, le surlignage à poignées | L'id `t02-revele`, `NOM`, `PHRASE` et `MOT_CLE`, la matière du disque (`LOGO`, sinon `IMAGE` et `CADRAGE`, sinon `CHIFFRE`), `ETIQUETTE` (facultative : une info réelle), les instants (`MOMENTS`) ; data-duration = la phrase posée + sa lecture |
| `compositions/disque-revelation-vertical.html` | 7,7 s | La même scène remise en page en 9:16 : le disque à 35 % de la hauteur, un trait plus long, la pose aux deux tiers, le nom et sa phrase au-dessus | Comme la version 16:9 |
| `compositions/grille-final.html` | 11,6 s | L'offre et l'appel : la grille d'une case par élément réel qui se dessine, l'approche de la case phare qui se remplit d'accent et son nom surligné, le slogan géant et son point d'accent, le nom et ses repères, le point qui devient le bouton cliqué | L'id `t02-final`, les cases (`ICONES` : une par élément réel, ses outils par leur logo), `CHOISIE` et `ETIQUETTE` (son vrai nom), le slogan (4 mots au plus, une phrase de sa page), le nom (ou son logo en `<img>`), le libellé du bouton, `NOTE` (facultative : une info réelle sous le bouton) |
| `compositions/grille-final-vertical.html` | 11,7 s | La même scène remise en page en 9:16 : grille de 4 colonnes, slogan sur trois lignes, bouton aux deux tiers de la largeur au moins | Comme la version 16:9 ; le slogan sur trois lignes (`#t02-final-l1` à `l3`, 10 caractères au plus par ligne) |

Bout à bout dans cet ordre, elles font une vidéo de 30 à 35 s qui se tient seule. Essai du 06/11/2026 sur la marque sombre de LMDM, avec la vraie matière de la story d'ouverture (sa page en capture, sa pub, sa capture Meta, ses vraies vidéos, son logo, les faits de sa fiche), en 16:9 et en 9:16, 32,5 s : `check` sans erreur, `palette` « ok », `rythme` « ok » (1,35 et 1,18 événement par seconde, écart médian 0,60 s, aucune image figée) ; puis aux couleurs de Dupliq.me (marque claire, accent orange) par captures : tout se lit. Les palettes des cartes, les repères et le disque suivent n'importe quelle marque : rien ne se règle à la main.
