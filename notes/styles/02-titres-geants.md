# Notes de maintenance · Style n°2 · Titres géants

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/02-titres-geants/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les essais mesurés, les refus datés, les exemples tirés des
vidéos de l'auteur) est rangé ici, tel qu'il était dans la fiche jusqu'au ménage du 07/11/2026.

## Ce qui est sorti de la fiche

### Les mesures

**Mesures de l'original** (`studio_motion.py reference`) : 1,71 événement par seconde, écart médian 0,40 s, 22 coupes franches, image figée la plus longue 1,2 s (le logo final).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 32,5 s, marque LMDM, vraie matière de la story d'ouverture, 06/11/2026) : `rythme` 1,35 événement par seconde en 16:9 et 1,18 en 9:16, écart médian 0,60 s, aucune image figée ; `palette` « ok » dans les deux formats. Chaque phrase tenue au moins le temps de sa lecture : la vidéo est plus lente que l'original, exprès.

### La citation d'ouverture (désormais dite une fois dans l'index, « Appliquer un style »)

> On reprend la grammaire (mises en page, typographie, mouvements, transitions, façon de montrer
> le produit), jamais le contenu : ni ses textes, ni son logo, ni ses images (paysages, sphère,
> planète, objets), ni ses couleurs, ni sa musique, ni son tempo de lecture. Ce qu'on voit vient du
> client et se peint aux seules couleurs de sa marque.

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

### Les couleurs de l'original (tableau de la section 3)

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Aubergine presque noir | le fond des pages sombres, la grille, l'espace | `var(--brand-sombre)`, la couleur la plus sombre de sa marque (sur une marque claire, son texte), sur toutes les pages de nuit ; la grille en blanc à 5 % |
| Lilas vif | le titre géant en plein écran, le texte du spécimen | `var(--brand-accent)` pour le plein écran (le titre est écrit en `var(--brand-contrast)` dessus) ; le spécimen, posé sur la nuit, en `var(--brand-accent-lisible)` (l'accent, ou son clair s'il ne se lit pas sur la nuit) |
| Violets, roses et pêche du crépuscule | les paysages, la sphère, l'espace | rien : ces images ne se refont pas. À leur place, sa vraie matière : ses captures (sa page, son produit, ses résultats), son logo dans le disque, ses vrais chiffres. Les fonds de carte de sa palette (accent, clair, gris, sombre) ne sont que des cadres |
| Vert lime | le point qui bouge, les poignées, le surlignage, le logo final | l'accent lui-même, plein : jamais une deuxième couleur inventée |
| Blanc cassé | la page du dessin au trait | `var(--brand-clair)`, le trait en `var(--brand-sombre)` |
| Blanc | le slogan, les titres | `var(--brand-clair)` |

Le paragraphe des traits, avec son essai daté (la leçon reste dans la fiche, sans date) :

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

### Le rythme d'avant (section 1)

- **L'original coupe toutes les 1,4 s** sur les temps forts de la musique : une identité, pas une offre, presque sans texte à lire. Chez le client, **la phrase décide de la tenue** : chaque page reste au moins le temps de lire la sienne (`studio_motion.py lecture`, 0,3 s par mot + 0,8 s, jamais moins de 1,5 s ; la carte de fin 3 s), puis la coupe tombe sur le temps fort suivant. Les scènes du kit placent seules leurs coupes d'après leurs textes et disent dans la console s'il manque du temps à leur data-duration.
- **Pendant qu'on lit, la vie vient de la phrase et de sa matière**, un événement toutes les 0,5 à 0,8 s : une graisse qui bascule sur les temps, une lettre tapée, la bande qui change de palette, le mot clé surligné d'un bloc d'accent, le cadre à poignées qui attrape le nom, un chiffre qui monte, une case qui se coche. Une tenue sans rien autour ne dépasse jamais 0,8 s (`rythme` la compte comme une image figée).
- **Rafales** : les icônes se dessinent à 0,03 s d'écart, les repères à 0,04 à 0,05 s, les cartes de la mosaïque arrivent à 0,06 s d'écart.
- **La caméra pendant la lecture** : une dérive lente seulement (×1,00 à ×1,045 sur toute la tenue, `sine.inOut`). Les gestes de caméra du style (l'approche d'un coin, le recul en mosaïque, la montée et la descente du disque, l'approche d'une case) tombent entre deux phrases, jamais sous un texte qu'on lit ; aucun recadrage sec dans les cinq premières secondes (le titre géant ne bouge que lentement).
- **Une seule respiration** : juste avant le nom final, l'énergie retombe une demi-seconde, puis le dernier temps fort tombe sur le nom.
- **Chez le client** : 1,2 événement par seconde au moins, une coupe franche entre deux phrases, jamais une phrase coupée avant sa lecture.

### Le son et l'ouverture de l'original (sections 8 et 9)

- **Original** : musique seule, sans voix ni bruitage marqué. Une nappe électronique aérienne, tempo estimé autour de 110 battements par minute ; une montée douce les 4 premières secondes (pendant la construction), l'énergie pleine dès la coupe sur le titre géant, une retombée d'une demi-seconde juste avant le logo final. Les coupes tombent sur les attaques de la musique (montées fortes mesurées à 4,3 s, 6,3 s, 7,9 s, 8,7 s, 10,1 s, 13,1 s, 14,5 s, 21,1 s, 21,9 s et 28,5 s).

- **Original** : il s'ouvre sur la construction du logo (des points gris qui s'assemblent sur un blanc cassé, des traits de construction, le nom qui s'écrit, un surlignage vert à poignées), puis le logo blanc sur le sombre. Il finit sur le slogan géant, puis le logo sur le sombre, tenu 1,7 s.

### Les leçons datées

- **Étiquettes** : une étiquette écrite porte une info réelle de la fiche (le prix, la date, le nom de l'offre, un chiffre de preuve) ou n'existe pas. Les étiquettes de maquette de l'original (la police et sa taille, le rayon, la couleur et son code) ne disent rien à son public et passent pour des restes oubliés (relecteur neuf de la story refusée du 06/11/2026) : elles sont réservées à une vidéo qui parle de design (une marque, un template).

- **Le disque** : il porte son logo (`LOGO`, l'icône de sa marque), sinon une vraie capture découpée dans le disque (`IMAGE`), sinon un vrai chiffre (`CHIFFRE`), dès qu'il prend sa couleur ; jamais un aplat seul qui monte et redescend (essai du 06/11/2026 : un disque jaune seul sous le nom).

Le paragraphe « Sur n'importe quelle marque, claire ou sombre » de la section 3 (essai du
06/11/2026 aux couleurs de Dupliq.me, accent orange sur sa nuit : tout se lit) est désormais dit une
fois dans l'index.

### Ce qui ne se fera pas à l'identique

- **Les deux polices** (Haffer et Season Mix, payantes) → la police de la marque en deux graisses ; la voix serif devient la graisse légère.
- **La construction du logo à partir de points** (faite pour leur logo) → pas de scène dans le kit ; son logo se pose dans le disque, le nom s'écrit lettre par lettre et le surlignage à poignées l'attrape.
- **Le tempo de lecture de l'original** (une page toutes les 1,4 s, presque sans texte) → chaque phrase du client tenue le temps de sa lecture.
- **Les images de l'original ne se refont pas et ne deviennent pas des formes** : ni les paysages peints au crépuscule, ni la sphère de verre et son canyon, ni la planète et l'espace, ni le portable photoréaliste, ni les objets dérivés (casquette, carnet, sweat), ni les astéroïdes et les cubes. À leur place, la vraie matière du client, en descendant l'échelle : ses captures (sa page, son produit, ses vidéos, ses résultats), son interface reconstruite, ses vrais chiffres, les vrais logos de ses outils, puis ses mots ; la révélation passe par un disque qui porte son logo, le slogan se pose sur la nuit.
- **Les étiquettes de maquette** (police, taille, rayon, code couleur) → aucune par défaut : seulement une info réelle de la fiche, ou rien.
- **Le violet avec son vert lime complémentaire** → la palette de sa marque et rien d'autre : l'accent plein sur ses neutres (sa nuit, son clair, ses gris) ; la vidéo est plus graphique que l'original.
- **Le faisceau de lumière** → un trait de marque fin et deux traits de construction : aucun halo, aucune lueur.

### Les essais du kit (sections « En vertical et en carré » et « Les compositions du kit »)

- **9:16 : chaque scène a sa version verticale, testée** sur la marque sombre de LMDM (les quatre bout à bout, 32,5 s : `rythme` et `palette` « ok ») et contrôlée aux couleurs de Dupliq.me. Prends le fichier `-vertical.html` à la place du 16:9 : on ne recadre jamais une scène 16:9, on la remet en page.

Bout à bout dans cet ordre, elles font une vidéo de 30 à 35 s qui se tient seule. Essai du 06/11/2026 sur la marque sombre de LMDM, avec la vraie matière de la story d'ouverture (sa page en capture, sa pub, sa capture Meta, ses vraies vidéos, son logo, les faits de sa fiche), en 16:9 et en 9:16, 32,5 s : `check` sans erreur, `palette` « ok », `rythme` « ok » (1,35 et 1,18 événement par seconde, écart médian 0,60 s, aucune image figée) ; puis aux couleurs de Dupliq.me (marque claire, accent orange) par captures : tout se lit. Les palettes des cartes, les repères et le disque suivent n'importe quelle marque : rien ne se règle à la main.

Le tableau des compositions d'avant (les textes à remplacer étaient écrits en dur) :

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

### Les exemples tirés des offres de l'auteur, retirés des scènes

- `disque-revelation.html` et sa version verticale : « Publicitaire IA » + « installe un
  publicitaire dans Claude ou ChatGPT. » comme exemple de nom et de phrase.
- `grille-final.html` : « 35 musiques de lancement » comme exemple d'étiquette, « 67 € jusqu'au 12
  novembre » comme exemple de note sous le bouton.
- La fiche : « 67 € », « 34 achats » comme vrais chiffres d'un disque sans logo.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit, et que l'IA copie
surtout le code des scènes. Ce qui a changé, et pourquoi :

**La fiche** (34 339 octets avant, 23 974 après) :
- Sorti vers cette note : les mesures, la citation, l'original scène par scène, les couleurs de
  l'original, ce qui ne se fera pas à l'identique, les essais datés, les exemples de l'auteur.
  Retiré parce que l'index le dit (« Appliquer un style ») : l'ouverture de la section 2, « Sur
  n'importe quelle marque », les rappels de lecture et de contraste.
- Les liens vers `references/style.md` deviennent `references/image.md` (« La palette », « La vraie
  matière »).
- Le titre géant ne déborde plus pendant qu'on le lit : la fiche disait « trois lignes de 380 px qui
  touchent le haut et le bas du cadre », la dernière coupée à droite et révélée par une glissade.
  Le débordement devient l'entrée et la sortie ; pendant la lecture, chaque mot est entier, la plus
  longue ligne à 90 % de la largeur au plus (3 lignes de 340 px).
- Les mots héros (le nom posé par le disque, le slogan, le nom de fin) prennent 60 à 90 % de la
  largeur : 120, 236 et 132 px fixes devenaient 30 à 50 % ; les scènes règlent leur taille seules.
- La mosaïque ne porte plus d'aplat sans sujet (la fiche en permettait « une ou deux ») ; ses
  textes à lire montent à 64-66 px dans la carte (28 px à l'écran à ×0,44) ; la pastille de la
  marque se retire au recul.
- Le disque reste grand tant qu'il est le sujet (42 % de la hauteur au plan A, ×1,15 pendant la
  montée, au lieu de 33 % puis ×0,62) ; posé, le sujet est le nom.
- Le surlignage devient une sélection lettre par lettre (un texte posé sur l'accent ne passe plus à
  moitié couvert : `check` signalait un contraste de 1,2:1 pendant le balayage).
- Durées : titre 5,6 → 6,4 s (entrée et sortie du débordement), carte 6,6 → 6,9 s (la mosaïque se
  lit), disque 7,7 → 7,8 s, grille 11,6 → 11,8 s (11,7 → 11,9 s en vertical).

**Les scènes** (chacune avec un objet `EXEMPLE` marqué « À REMPLACER », en-tête « À remplacer :
l'objet EXEMPLE ») :
- `titre-geant` (et vertical) : textes générés depuis `EXEMPLE` (exemple : un logiciel, « Ton site
  en ligne ce soir. ») ; entrée à ×1,5 et sortie en débordement, taille réglée à la mesure des
  lignes, marges pour la poussée ; la glissade de la dernière ligne et la dérive verticale sous le
  texte sont retirées ; le spécimen se réduit seul s'il sort du cadre (« à lancer » : sans jambage
  sur la ligne légère).
- `carte-mosaique` (et vertical) : `NOM`, `MARQUE` et la matière des cartes dans `EXEMPLE`
  (exemple : une formation), leurs places et fonds dans `PLACES` ; plus d'aplat (une capture sur
  les cartes coupées) ; textes de carte à 64-66 px ; mesure du texte corrigée (la boîte d'un
  chiffre ou d'un contexte fait toute la carte : la scène les réduisait toujours, le contexte
  tombait à 26 px à l'écran) ; un contexte, un libellé ou une ligne trop longs le disent dans la
  console au lieu de rapetisser.
- `disque-revelation` (et vertical) : `EXEMPLE` neutre (un coaching : « Ton coaching » + « t'aide
  à décider plus vite. ») ; disque ×1,25 au plan A, ×1,15 en haut, ×0,42 posé ; le nom mesuré
  lettre à lettre (sa boîte fait toute la largeur : la scène le réduisait toujours à 94 px) et réglé
  à 68 % (80 % en vertical) ; nom et phrase écartés pour le cadre de sélection ; sélection lettre par
  lettre du mot clé et du nom.
- `grille-final` (et vertical) : textes générés depuis `EXEMPLE` (exemple : un logiciel et ses
  fonctions) ; slogan à 70 % (85 %) de la largeur, nom de fin à 64 % (80 %), posé au-dessus de son
  repère (jambages compris) ; grille de fond marquée `data-layout-allow-overflow` ; logo facultatif
  devant le nom.

**Vérifié** sur les bancs « Banc styles 02 · Page de vente » (16:9) et « Reel » (9:16), marque
sombre à accent jaune, captures d'une vraie page en matière : les quatre scènes bout à bout (32,9 s
en 16:9, 33 s en 9:16), `check` sans erreur, sans `text_below_floor`, `line_unread` ni contraste
(restent `composition_file_too_large` et `film_silent`, sans musique sur le banc) ; images
regardées à chaque moment clé.
