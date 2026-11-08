# Style n°5 · Interrupteurs en cascade · d'après ClaudeDevs (https://x.com/ClaudeDevs/status/2091953609185657251)

**Ce qu'on voit :** sur un papier clair (le blanc et les gris de la marque), son panneau de réglages vu de près : une main clique, les interrupteurs s'allument en cascade. Puis des phrases calmes au centre, un trait à main levée qui entoure, souligne et relie, une grille de pastilles qui cochent en vague les éléments de l'offre, et la fenêtre de l'offre qui travaille avant la carte d'annonce.
**Souvent utile pour :** annoncer une nouveauté (un module, un bonus, une fonction, une mise à jour), ou montrer qu'un seul réglage sert tout le monde.

L'interface du kit est neutre et ne prend que les couleurs du client : ses neutres et son accent plein. Jamais l'interface ni les logos de l'original.

## 1. Le rythme

- Calme et régulier : un geste à la fois, sur une grille de 0,5 s (musique autour de 118 battements par minute). Les textes entrent par un flou qui se dissipe.
- La caméra fait de grands mouvements rares et nets (recul, approche, glissement, plongée) **entre deux textes** ; pendant une lecture, une dérive de 3 à 5 % (sine.inOut), et aucun coup au clic : la main et les interrupteurs font le geste.
- Chaque scène calcule ses tenues d'après ses textes (`studio_motion.py lecture`) et en déduit sa durée (D dans le script, à reporter en `data-duration`).
- **Le rythme vient du contenu.** Les gestes fins de l'original (un trait de 7 px, des billes) échappent au contrôle `rythme` : le kit les rend francs, d'un coup, et leur donne de la matière. Les membres surgissent ensemble ; mots clés et mot fort se surlignent d'un bloc plein ; les vrais logos des outils que la phrase nomme arrivent pendant sa lecture (`LOGOS`, scène 2) ; les membres deviennent des anneaux ; les coches tombent en trois salves et écrivent l'élément coché ; la grille respire deux fois ; chaque étape cochée sort sa vraie capture ; la pastille d'annonce se remplit d'encre. Une graisse qui bascule, un trait fin, une bille ne comptent pas.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| La cascade d'interrupteurs | le panneau de l'offre vu de près, un clic sur l'interrupteur maître, les autres rangs s'allument en cascade | accroche, ce qu'on reçoit (modules, fonctions) | `interrupteurs-cascade`, et le menu de `fenetre-annonce` |
| Le trait à main levée | un seul trait qui entoure les mots clés de la phrase, souligne le mot fort et voyage d'une phrase à l'autre | promesse, mot fort, tout temps fort | `interrupteurs-cascade`, `trait-qui-relie` |
| Les filets qui relient | deux filets relient la phrase au panneau et aux membres ; la phrase devient le nom de l'offre | solution, le nom de l'offre | `trait-qui-relie` |
| La vague de coches | des anneaux qui se remplissent et se cochent en vague ; autour de la phrase, chaque coche coche un vrai élément de l'offre, son nom écrit dans le disque | preuve, ce qui est inclus, « pour tous » | `grille-de-coches` |
| La carte qui devient fenêtre | une carte s'ouvre en plein écran sur la vraie interface, où une demande se tape et des étapes s'écrivent | démonstration | `grille-de-coches` (fin), `fenetre-annonce` |
| La pastille d'annonce et la signature | une petite pastille au-dessus d'un titre en deux lignes, puis le logo qui tourne et se pose, le nom en grand | annonce, offre, fin | `fenetre-annonce` (fin) |
| Les phrases qui respirent | chaque phrase entre mot par mot par un flou qui se dissipe, se tient le temps de sa lecture pendant une lente dérive de la caméra | toutes les phrases | toutes les scènes |

Ce style n'a pas de geste « problème » : pour une vidéo qui vend, le problème se construit sur le même papier clair (recette 1 de [scenes.md](../../references/scenes.md), la corvée), avec le trait à main levée qui entoure ce qui coûte.

## 3. Les fonds et les couleurs

**Les objets connus gardent leurs vraies couleurs**, dans ce style comme dans tous les autres : le
dossier bleu du Mac et les fichiers du kit (`K.ic("objet-…")`), le téléphone et sa barre d'état, la
notification et les bulles d'iPhone, les vrais logos de ses outils, l'interface d'une plateforme
reconstruite d'après capture. Ce sont les touches de couleur vraie du film ; tout le reste prend
les rôles ci-dessous ([image.md](../../references/image.md), « Les objets connus »).

Les variables `--t05-*` en tête de chaque scène nomment les jetons de la marque ([image.md](../../references/image.md), « La palette ») : jamais une couleur en dur à leur place.

| Rôle | Chez le client |
|---|---|
| Papier, le fond de tout | `--t05-papier` : son clair mêlé à `--brand-gris-4`, jamais une teinte crème inventée |
| Panneau, disques, cartes, fenêtre, champ, menu, billes | son clair, `--t05-carte` (`var(--brand-clair)`) |
| Onglet, rails éteints, bulle, bouton inactif | un gris clair de ses neutres, `--t05-pli` (la bulle, `--t05-bulle`, un cran plus clair) |
| Textes | sa couleur sombre, `--t05-encre` (`var(--brand-sombre)`) ; le texte gris d'un champ, `--t05-gris-texte` (`var(--brand-gris-2)`) |
| Interrupteurs allumés, tuiles d'icône, bouton d'envoi actif | l'accent plein (`--t05-allume`) ; ce qui est écrit dessus, `--brand-contrast` |
| Trait à main levée, anneaux, blocs pleins | l'accent ; trop clair sur le papier (contraste sous 2 : un jaune, un pastel), ils passent **tout seuls** à l'encre, texte en clair dessus ; la pastille cochée reste à l'accent, coche `--brand-contrast` |
| Icônes des membres | son gris, `--t05-gris-texte` |
| Icônes des rangs et des étapes | une icône du kit sur une tuile à l'accent, ou les vrais logos des outils branchés |
| La main | son clair, cernée de sa couleur sombre |

Sur une marque sombre comme sur une claire, le look reste clair : jamais `var(--brand-bg)` quand c'est sa nuit. Un anneau de lisibilité se pose autour de l'accent, jamais par-dessus.

Un seul fond presque toute la vidéo ; la bascule est le passage du papier à la fenêtre de son clair (scène 3 vers 4). Ni fond sombre ni plein écran de couleur au milieu : le look s'effondre (seule exception possible, la signature sur la couleur de la marque).

## 4. La typographie

- **Titres** : la police de titres de sa marque (`--t05-titres`), en graisse 400, jamais en gras sauf le nom de l'offre et la signature. L'original prend une serif de livre.
- **Sa marque n'impose rien, ou il veut le look complet :** Source Serif 4 (libre), 400 à 500. `python3 tools/studio_motion.py police "Source Serif 4"` (depuis la racine), son fichier de `marque/polices/` dans `assets/fonts/` du projet, puis dans chaque scène un `@font-face` (`font-display: block`) et `--t05-titres: "Source Serif 4", var(--brand-font-display);`.
- **Interfaces** (panneau, menu, champ, étapes, noms cochés) : la police de texte (`--t05-texte`), régulière, alignées à gauche comme une vraie interface ; le reste est centré. Casse de la phrase, sauf la pastille en capitales espacées ; -0,02 em sur les titres.
- Une phrase par écran, 8 mots au plus : les mises en page du kit en prennent 8 (scène 1), deux lignes de 3 (scène 2), 7 (scène 3). Une phrase du script qui n'y tient pas passe dans une scène construite dans le style ; la réduction automatique des scènes ne rattrape qu'une police de marque plus large (jusqu'à 70 %).
- **Les mots héros** (le mot fort, le nom entre les filets, la signature) remplissent la largeur : les scènes calculent leur taille.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Phrase de deux lignes | 80 px (scène 1), 72 px entre les filets (scène 2), interligne 1,16 | 84 px |
| Phrase dans la grille (scène 3) | 56 px dans un trou de 520 px, vue à ×1,7 (95 px à l'image) | 64 px dans un trou de 600 px, vue à ×1,55 |
| Mot fort, seul | 62 % de la largeur à l'image (caméra à ×1,15), 112 à 280 px | 64 % de la largeur, 130 à 300 px |
| Nom de l'offre entre les filets | graisse 600, 700 px de large pour laisser les filets (92 à 160 px) | 64 % de la largeur, 104 à 220 px |
| Panneau : interrupteur maître, rangs | 30 et 28 px, vus à ×1,5 au début (42 px à l'image) | vus à ×1,45 |
| Noms cochés (scène 3) | 18 px, graisse 500, vus à ×1,7 (31 px à l'image) | 19,5 px vus à ×1,55 |
| Salut de la fenêtre ; menu « + » et champ | 64 px ; 33 et 34 px | fenêtre à 86 % (28 px ou plus à l'image) ; un salut long se réduit seul |
| Étapes, bulle ; titre de la carte | 40 et 34 px ; 80 px | les mêmes |
| Pastille (« Nouveau ») | 30 px, capitales, espacement 0,14 em, contour 2 px | 30 px |
| Signature | le nom (graisse 600) et sa pastille : 62 % de la largeur (112 à 260 px) | 62 % de la largeur |

## 5. Les mouvements signature

Tous sont dans `compositions/` ([mouvement.md](../../references/mouvement.md), « La caméra »).

1. **La cascade** (scène 1, menu de la scène 4). Le panneau entier à l'image, vu de près ; la main clique le maître (bille en 0,28 s, power3.inOut), chaque rang s'allume 0,105 s après le précédent (0,24 s, gonflement ×1,07 aller-retour) ; la caméra dérive de 4 % jusqu'au recul.
2. **Le trait qui voyage** (scènes 1 et 2). Un trait de 7 px, bouts ronds, bord irrégulier (turbulence fixe). Il arrive par la gauche, entoure les mots clés en 0,8 s (power2.inOut) sans toucher le mot voisin, tient, file par une queue qui contourne la phrase (0,7 s, power2.in) ; il revient par le haut souligner le mot fort, rembobine, redescend le long du panneau et devient le filet de gauche. Technique : un morceau [a, b] de la longueur du chemin (pointillé SVG), fonction du temps.
3. **Les filets** (scène 2) : panneau, phrase, membres à mi-hauteur ; quand la phrase devient le nom, ils s'ajustent (0,5 s) pour garder 46 px d'écart.
4. **La vague de coches** (scène 3). La caméra s'approche d'abord (×1,7) ; chaque anneau se remplit en camembert (0,42 s, power1.inOut), la coche se trace (0,22 s), en trois salves ; autour de la phrase, la pastille monte et le nom de l'élément s'écrit dessous.
5. **La carte qui devient fenêtre** (scènes 3 et 4). Les pastilles se réduisent à un point, les disques s'écartent de 25 % et deviennent des cartes (l'espace du membre en miniature, de la texture) ; la carte visée s'ouvre en plein écran par une découpe qui s'élargit (0,85 s, expo.inOut).
6. **Les phrases qui respirent** : entrée mot par mot par un flou (0,7 s, expo.out, 0,07 s entre deux mots, 12 px de montée), tenue pendant la dérive, sortie en flou (0,35 s) pendant que la caméra revient au plan large.

## 6. Les transitions

- Aucune coupe franche : le gros plan qui recule (le panneau devient un témoin au bord), le glissement vers la grille, la carte qui s'ouvre en fenêtre, le contenu qui s'efface vers le haut avant la carte d'annonce.
- Un texte en remplace un autre sur place par un fondu flou, jamais par un volet ; le trait quitte une phrase et rejoint l'autre.
- Chaque scène du kit commence sur la dernière image de la précédente (panneau et membres entre 1 et 2, grille d'anneaux entre 2 et 3, fenêtre plein écran entre 3 et 4).

## 7. Le produit à l'écran

- Le panneau, ce sont les parties de son offre (modules, bonus, fonctions) ; les disques, ses membres (élèves, clients) ; les coches, ce qui est inclus ; les cartes, l'espace de chacun ; la fenêtre, son produit en action.
- **La fenêtre par défaut de `fenetre-annonce`** (un champ, une demande tapée, des étapes) ne vaut que si son offre a vraiment ce champ (un outil d'IA, un assistant qu'on pilote en écrivant). Sinon la fenêtre montre son espace ou son logiciel en vraie capture (ou reconstruit d'après capture), ou la scène commence à la carte d'annonce.
- Interfaces neutres : coins arrondis (24 px), filets fins, ombres douces, interrupteurs à bille, vues assez près pour que le nom de chaque réglage se lise ; les cartes en miniature sont de la texture. Jamais de faux navigateur.

## 8. Le son

- Original : une musique douce et régulière (environ 118 battements par minute, sans montée ni chute), des clics d'interface légers sur la cascade (quatre clics à 0,125 s), la musique se pose sur la signature.
- Chez le client : une musique de lancement calme (`musiques choisir --ambiance "Premium et calme"`, ou « Tech minimale »), calée à 120. Bruitages petits et secs : un clic doux par interrupteur, un « pop » léger par disque, un frottement de crayon sur la boucle, un tintement discret sur la signature. Jamais de souffle (whoosh) ni d'impact : ils cassent le calme.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 5`) : « Premium et calme » puis « Tech minimale », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture :** la première image est déjà le gros plan du panneau (rien de vide), la main entre tout de suite, le clic tombe vers 1 s.
- **Fin :** la carte d'annonce (pastille + titre, tenue le temps de lire le titre), puis la signature : la pastille de la marque (ou son logo) tourne et se pose, le nom s'écrit de gauche à droite, en grand, et tient 3 s (l'écran final). Pour une vidéo de vente, la signature peut céder la place à une fin du studio ([scenes.md](../../references/scenes.md), recettes 25 et 26), sur le même papier clair.

## Sur une autre offre

- **Formation :** rangs = modules et bonus ; membres = élèves ; coches = ce que chaque élève reçoit ; fenêtre = l'espace de formation où le module annoncé s'ouvre (d'après capture), ou l'assistant si la formation en a un. Mot fort : « Une fois. », « Inclus. ».
- **Coaching :** rangs = séances, groupe, ressources ; membres = les coachés ; coches = les séances et ressources incluses ; cartes = leur espace ; fenêtre = l'agenda ou l'espace membre. Mot fort : « Pour tous. ».
- **Logiciel :** rangs = les fonctions ou les intégrations, avec leurs vrais logos (`studio_motion.py logos`) ; membres = l'équipe ou les clients ; coches = les fonctions activées ; fenêtre = le logiciel d'après capture ; le nom entre les filets = l'outil branché.
- **Toujours :** la cascade, le trait qui entoure et relie, la vague de coches, la carte qui devient fenêtre, la pastille d'annonce, le papier clair.

## En vertical et en carré

- **Scènes 1, 3 et 4 :** elles se remettent en page seules en 9:16 (racine en 1080 × 1920). Scène 1 : panneau en haut, phrase au milieu, membres sur deux rangées en bas. Scène 3 : grille de 5 colonnes, rangée du milieu vide pour la phrase, noms cochés au-dessus et au-dessous. Scène 4 : fenêtre et carte centrées (contenu à 86 %), approche du champ à ×1,12 pour le garder entier.
- **Scène 2 :** monte `trait-qui-relie-vertical.html` à la place de `trait-qui-relie.html`. Panneau en haut et membres en bas, là où la scène 1 en 9:16 les laisse ; mot fort, phrase et nom au centre ; le trait descend par la droite du panneau, souligne, puis devient deux filets verticaux ; à la fin, la caméra glisse vers le bas et la grille (la cinquième colonne arrive avec la vague) tombe pile sur la première image de la scène 3 en 9:16.
- **Carré et 4:5 :** même logique que le vertical ; le panneau se coupe plus tôt (seule la colonne des interrupteurs reste), la phrase descend à 64 px.

## Les compositions du kit

Montées bout à bout dans cet ordre (ids `t05-cascade`, `t05-trait`, `t05-coches`, `t05-annonce`), elles raccordent image pour image (43,5 s avec les textes d'exemple) ; chacune vit aussi seule. Chaque scène calcule sa durée (D dans le script) : reporte-la dans `data-duration`, sur la racine et sur l'hôte. Ses textes d'exemple sont dans l'objet `EXEMPLE` (chaque champ y dit ce qu'il montre).

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (l'objet `EXEMPLE`) |
|---|---|---|---|
| `compositions/interrupteurs-cascade.html` | 4,8 s + la lecture de la phrase (7,4 s pour 6 mots) | le panneau vu de près, le clic, la cascade, le recul, la phrase entourée, les membres | `ONGLET`, `MAITRE`, `RANGS` (5 à 7 vrais éléments de l'offre), `PHRASE` (8 mots au plus), `ENTOURE` |
| `compositions/trait-qui-relie.html` | 3,3 s + la lecture du mot, de la phrase et du nom (9,9 s pour 2, 5 et 2 mots) | le mot fort en grand et souligné, la phrase reliée par deux filets, les logos de ses outils, le nom de l'offre, les anneaux, le glissement vers la grille | `MOT`, `PHRASE` (deux lignes de 3 mots), `NOM`, `LOGOS` ([] : aucun), `MAITRE` et `RANGS` de la scène 1 |
| `compositions/trait-qui-relie-vertical.html` | comme la version 16:9 | la même scène en 9:16 : filets verticaux, glissement vers le bas | comme la version 16:9 |
| `compositions/grille-de-coches.html` | 4,9 s + la lecture de la phrase (7,7 s pour 5 mots) | l'approche, la vague qui coche les éléments de l'offre, la phrase, les cartes des membres, la plongée | `TEXTE` (7 mots au plus), `COCHES` (6 vrais éléments de l'offre), `SALUTS`, `ACCUEIL` |
| `compositions/fenetre-annonce.html` | 18,5 s avec les textes d'exemple | la fenêtre, le menu en cascade, la demande tapée, les étapes qui se cochent, la carte d'annonce, la signature tenue 3 s | `SALUT` et `ACCUEIL` (ceux de la scène 3), `MENU`, `DEMANDE` et `ETAPES` (section 7), `PASTILLE`, `TITRE` (8 mots au plus), `FORT`, `NOM`, `LOGO` |
