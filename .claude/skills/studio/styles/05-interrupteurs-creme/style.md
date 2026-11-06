# Style n°5 · Interrupteurs crème · d'après ClaudeDevs (https://x.com/ClaudeDevs/status/2091953609185657251)

**Ce qu'on voit :** sur un papier clair (le blanc et les gris de la marque), un panneau de réglages vu de très près : une main clique, les interrupteurs s'allument en cascade. Puis des phrases calmes au centre, un trait à main levée qui entoure, souligne et relie, une grille de pastilles qui se cochent en vague, et la fenêtre de l'offre qui travaille avant la carte d'annonce.
**Souvent utile pour :** annoncer une nouveauté (un module, un bonus, une fonction, une mise à jour), ou montrer qu'un seul réglage sert tout le monde.
**D'après :** X · ClaudeDevs, « Authorize once » · 34 s · 16:9 (1920 × 1080, 24 images par seconde).
**Mesures de l'original (`studio_motion.py reference`) :** 0,62 événement par seconde, écart médian 0,50 s entre deux, 8,5 s d'image figée en tout, aucune coupe franche.
**Mesures du kit monté (les 4 scènes bout à bout, 28,5 s, marque LMDM, essai du 06/11/2026) :** `rythme` répond « ok » : 1,16 événement par seconde en 16:9 et 1,08 en 9:16, écart médian 0,80 s, aucune image figée ; `palette` répond « ok ».

> On reprend la grammaire de la vidéo, jamais son contenu : ni ses textes, ni l'interface et les
> logos de Claude, ni les logos de ses partenaires, ni ses couleurs, ni sa musique. L'interface du
> kit est neutre et ne prend que les couleurs du client : ses neutres et son accent plein.

## 1. Le rythme

- Calme et régulier : un geste à la fois, posé sur une grille de 0,5 s (la musique tourne autour de 118 battements par minute). Les textes entrent par un flou qui se dissipe, sans saut ; la caméra fait de grands mouvements rares et nets (le recul, le glissement, la plongée).
- L'original ne fait que 0,62 événement par seconde : trop calme pour le contrôle `rythme` du studio (1 au moins, 0,8 s d'écart médian au plus). Le kit garde le calme mais **recadre doucement à chaque phrase** (0,5 à 0,8 s, expo.inOut, 4 à 13 % d'échelle, avec un léger glissement de côté : un zoom pile au centre ne se mesure pas) et donne un petit coup de caméra à chaque clic. C'est ce qui le fait passer : ne retire pas ces recadrages.
- Une couleur de marque claire (jaune, pastel) change peu la luminosité : le contrôle compte alors surtout les textes, le trait, la main et la caméra. Avec un accent foncé, la cascade et les coches comptent aussi.
- Tenue d'un texte : 1 à 1,5 s, jamais plus sans un recadrage ou un geste autour.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| La cascade d'interrupteurs | un clic sur l'interrupteur maître, les autres rangs s'allument en cascade | accroche, ce qu'on reçoit (modules, fonctions) | `interrupteurs-cascade`, et le menu de `fenetre-annonce` |
| Le trait à main levée | un seul trait qui entoure les mots clés, souligne le mot fort et voyage d'une phrase à l'autre | promesse, mot fort, tout temps fort | `interrupteurs-cascade`, `trait-qui-relie` |
| Les filets qui relient | deux filets relient la phrase à ce qui l'entoure ; la phrase devient le nom de l'offre | solution, le nom de l'offre | `trait-qui-relie` |
| La vague de coches | des anneaux qui se remplissent et se cochent en vague | preuve, résultat, « pour tous » | `grille-de-coches` |
| La carte qui devient fenêtre | une carte s'ouvre en plein écran sur la vraie interface, où une demande se tape et des étapes s'écrivent | démonstration | `grille-de-coches` (fin), `fenetre-annonce` |
| La pastille d'annonce et la signature | une petite pastille au-dessus d'un titre en deux lignes, puis le logo qui tourne et se pose | annonce, offre, fin | `fenetre-annonce` (fin) |
| Les phrases qui respirent | chaque phrase entre mot par mot par un flou qui se dissipe, la caméra s'en approche | toutes les phrases | toutes les scènes |

Ce style n'a pas de geste « problème » : pour une vidéo qui vend, le problème se construit sur
le même papier clair (recette 1 du studio, la corvée), avec le trait à main levée qui entoure ce
qui coûte.

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (c'est une annonce : il n'a pas de bloc « problème ») :

| Rôle | Temps | Ce qui s'y passe |
|---|---|---|
| Accroche | 0 à 2,8 s | Gros plan sur un panneau de réglages. Une main clique l'interrupteur maître, les autres s'allument en cascade. |
| Solution | 2,8 à 6 s | La caméra recule et glisse : le panneau reste en témoin au bord gauche. Une phrase de deux lignes au centre ; un trait à main levée entoure ses mots clés. Des disques de membres arrivent en vague à droite. |
| Solution | 6 à 7,6 s | Un mot fort, seul, souligné par le même trait. |
| Solution | 7,7 à 11 s | Une phrase reliée par deux filets au panneau et aux membres ; elle devient le logo de l'outil qui fait le lien. |
| Preuve | 10,5 à 15,8 s | Les membres deviennent des anneaux, la caméra glisse, les anneaux se remplissent et se cochent en vague. Zoom : une phrase au centre de la grille. |
| Preuve | 15,8 à 17 s | Les pastilles deviennent des cartes (l'espace de chaque membre, à son prénom). Plongée dans l'une d'elles. |
| Démonstration | 17 à 28,4 s | La fenêtre : le menu « + » où les interrupteurs s'allument encore, une demande tapée puis envoyée, des étapes qui s'écrivent avec l'icône de chaque outil. |
| Offre | 28,4 à 31,4 s | Carte d'annonce : une petite pastille (« bêta ») au-dessus d'un titre de deux lignes. |
| Appel | 31,4 à 34 s | La signature : le logo tourne et se pose, le nom s'écrit. Ni bouton ni phrase d'appel. |

Le kit regroupe ces temps en quatre scènes (section « Les compositions du kit ») : 1 + 2, puis 3 + 4, puis la preuve, puis la démonstration, l'offre et la signature.

## 3. Les fonds et les couleurs

Ses couleurs, rien d'autre ([../../references/style.md](../../references/style.md), « La palette ») :
les neutres de sa marque (son clair, ses gris, sa couleur sombre) et son accent posé plein. Les
variables `--t05-*` en tête du style de chaque scène ne font que nommer ces jetons.

| Rôle | Original | Chez le client |
|---|---|---|
| Papier, le fond de tout | crème #EFEFE5 | un gris très clair tiré de ses neutres : `--t05-papier` (son clair mêlé à `--brand-gris-4`). Jamais une teinte crème inventée, jamais le fond sombre de la marque |
| Panneau, disques, cartes, fenêtre | blanc cassé #F9FAF5 | son clair, `--t05-carte` (`var(--brand-clair)`) |
| Onglet, rails éteints, bulle, bouton inactif | #DDDDD1 | un gris clair de ses neutres, `--t05-pli` (la bulle, `--t05-bulle`, un cran plus clair) |
| Textes | encre presque noire | sa couleur sombre, `--t05-encre` (`var(--brand-sombre)`) ; le texte gris d'un champ, `--t05-gris-texte` (`var(--brand-gris-2)`) |
| Interrupteurs allumés | bleu d'interface #3588D6 | l'accent plein (`--t05-allume`) ; la bille reste blanche, avec une ombre noire transparente |
| Trait à main levée, pastilles cochées | terracotta #D26E57, la couleur de la marque d'origine | l'accent de la marque. S'il est trop clair sur le papier (contraste sous 2 avec son clair : un jaune, un pastel), le trait et les anneaux passent **tout seuls** à l'encre ; la pastille reste à l'accent, avec une coche de la couleur lisible dessus (`--brand-contrast`) |
| Icônes des membres | lavande #8276B8 | son gris, `--t05-gris` (`var(--brand-gris-3)`) |
| Icônes des rangs et des étapes | les vrais logos des outils | une icône du kit sur une tuile à l'accent, ou les vrais logos si l'offre branche des outils |
| Ombres | ombres chaudes, teintées | du noir en transparence, neutre |

**Sur n'importe quelle marque, claire ou sombre** : le papier, les cartes, l'encre et les gris
viennent de sa palette (`--brand-clair`, `--brand-gris-2` à `--brand-gris-4`, `--brand-sombre`) ;
sur une marque sombre comme sur une claire, le look reste clair (jamais `var(--brand-bg)` quand
c'est sa nuit). La marque donne aussi l'accent, toujours plein (interrupteurs, trait, pastilles,
tuiles, bouton d'envoi actif), et ce qui est écrit dessus passe en `var(--brand-contrast)`. Un
bouton inactif est gris, jamais l'accent en transparence ; un anneau de lisibilité se pose autour
de l'accent, jamais par-dessus. Tout texte garde un contraste d'au moins 4,5:1 (sa couleur sombre
sur le papier : 13:1 chez LMDM).

Un seul fond pendant presque toute la vidéo ; la bascule, c'est le passage du papier gris clair à la fenêtre de son clair (scène 3 vers scène 4). N'ajoute ni fond sombre ni plein écran de couleur au milieu : le look s'effondre. Seule exception possible : la signature finale sur la couleur de la marque.

## 4. La typographie

- **Titres.** Dans l'original, une serif de livre en graisse régulière. Chez le client : **la police de titres de sa marque** (`--t05-titres`, qui vaut `var(--brand-font-display)`), en graisse régulière (400), jamais en gras sauf le nom de l'offre et la signature.
- **Sa marque n'impose rien, ou il veut le look complet :** Source Serif 4 (libre, Google Fonts), graisse 400 à 500, la plus proche. `python3 tools/studio_motion.py police "Source Serif 4"` (depuis la racine), copie son fichier de `marque/polices/` dans `assets/fonts/` du projet, puis dans le style de chaque scène : `@font-face { font-family: "Source Serif 4"; font-weight: 400; font-display: block; src: url("assets/fonts/<son fichier>.woff2") format("woff2"); }` et `--t05-titres: "Source Serif 4", var(--brand-font-display);`. Essayé sur le projet d'essai : le rendu la prend.
- **Interfaces** (panneau, menu, champ, étapes) : la police de texte de la marque (`--t05-texte`), régulière.
- Casse de la phrase partout, sauf la pastille en capitales espacées. Tout est centré, sauf le panneau, le menu et les étapes (alignés à gauche, comme une vraie interface). Approche serrée (-0,02 em) sur les titres.
- 6 mots au plus par écran. Une phrase trop large se réduit seule (les scènes la mesurent).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Phrase de deux lignes | 72 px, interligne 1,16 | 84 px |
| Mot fort, seul | 112 px | scène en 16:9 seulement |
| Nom de l'offre entre les filets | 92 px, graisse 600 | scène en 16:9 seulement |
| Salut de la fenêtre | 64 px | 55 px (fenêtre à 86 %) ; un salut long se réduit seul (840 px de la fenêtre au plus, son point compris) |
| Titre de la carte d'annonce | 72 px | 72 px, réduit si trop large |
| Pastille (« Nouveau ») | 30 px, capitales, espacement 0,14 em, contour 2 px | 30 px |
| Signature | 112 px, graisse 600 | réduite à la largeur |
| Panneau : interrupteur maître, rangs | 29 et 26 px, vus à ×1,68 au début | vus à ×1,45 |
| Étapes, bulle | 40 et 34 px | 40 et 34 px |

## 5. Les mouvements signature

Tous sont dans `compositions/`.

1. **La cascade d'interrupteurs** (scène 1, et le menu de la scène 4). La main clique l'interrupteur maître (bille en 0,28 s, power3.inOut), puis chaque rang s'allume 0,105 s après le précédent (0,24 s chacun, gonflement ×1,07 aller-retour). La caméra donne un petit coup au clic (de ×1,05 à ×1,1 en 0,14 s, retour en 0,36 s), puis descend avec la cascade.
2. **Le trait à main levée qui voyage** (scènes 1 et 2). Un seul trait de 7 px, bouts ronds, bord légèrement irrégulier (filtre de turbulence fixe). Il arrive par la gauche, entoure les mots clés en 0,8 s (power2.inOut) en effaçant son entrée, tient, puis file hors de l'image par une queue qui contourne la phrase (0,7 s, power2.in). Il revient par le haut souligner le mot fort, rembobine, redescend le long du panneau et devient le filet de gauche. Technique : on montre un morceau [a, b] de la longueur du chemin (pointillé SVG), calculé comme une fonction du temps.
3. **Les filets qui relient** (scène 2). Panneau, phrase, membres, à mi-hauteur. Quand la phrase devient le nom, les filets s'allongent ou raccourcissent (0,5 s) pour garder 46 px d'écart.
4. **La vague de coches** (scène 3). Chaque anneau se remplit comme un camembert (0,42 s, power1.inOut), la coche se trace (0,22 s), de gauche à droite (0,13 s par colonne, 0,045 s par rang).
5. **Le disque qui devient carte, la carte qui devient fenêtre** (scènes 3 et 4). Les pastilles se réduisent à un point, les disques s'écartent de 25 % et deviennent des carrés arrondis avec l'espace du membre ; la carte visée s'ouvre en plein écran par une découpe qui s'élargit (0,85 s, expo.inOut) pendant que son contenu grandit.
6. **Les phrases qui respirent.** Chaque phrase entre mot par mot par un flou qui se dissipe (0,7 s, expo.out, 0,07 s entre deux mots, 12 px de montée) ; la caméra s'en approche de 4 à 13 % avec un léger glissement, puis revient au plan large quand elle sort (flou, 0,35 s).

## 6. Les transitions

- Aucune coupe franche. Tout passe par la caméra et les objets : le gros plan qui recule (le panneau devient un témoin au bord), le glissement de côté vers la grille, le zoom dans la grille, la carte qui s'ouvre en fenêtre, le contenu qui s'efface vers le haut avant la carte d'annonce.
- Un texte en remplace un autre sur place par un fondu flou (le nom prend la place de la phrase), jamais par un volet.
- Le trait relie les phrases entre elles : il quitte l'une et rejoint l'autre.
- Raccords du kit : chaque scène commence sur la dernière image de la précédente (panneau et membres identiques entre 1 et 2, grille d'anneaux entre 2 et 3, fenêtre plein écran entre 3 et 4).

## 7. Le produit à l'écran

- L'original montre le produit par ses réglages (un panneau de connecteurs), ses utilisateurs (des disques), l'espace de chacun (des cartes) et le produit qui travaille (la fenêtre, avec les logos des outils dans les étapes).
- Chez le client : le panneau, ce sont les parties de son offre (modules, bonus, fonctions) ; les disques, ses membres (élèves, clients) ; les cartes, l'espace de chacun ; la fenêtre, son produit en action. Jamais l'interface de Claude.
- **La fenêtre par défaut de `fenetre-annonce`** (un champ de demande, une demande tapée, des étapes qui s'écrivent) ne vaut que si son offre a vraiment ce champ : un outil d'IA, un assistant qu'on pilote en écrivant (Publicitaire IA, qui vit dans Claude ou ChatGPT, en a un). Sinon, ce serait une interface inventée : la fenêtre montre son espace de formation ou son logiciel en vraie capture (ou reconstruit d'après capture), ou la scène commence à la carte d'annonce.
- Interfaces neutres et propres : coins arrondis (24 px), filets fins, ombres douces, interrupteurs à bille. Jamais de faux navigateur.

## 8. Le son

- Original : une musique douce et régulière (environ 118 battements par minute, sans montée ni chute), des clics d'interface légers sur la cascade (quatre clics à 0,125 s), la musique se pose sur la signature.
- Chez le client : une musique de lancement calme (`musiques choisir --ambiance "Premium et calme"`, ou « Tech minimale »), calée à 120. Bruitages petits et secs : un clic doux par interrupteur, un « pop » léger par disque, un frottement de crayon sur la boucle, un tintement discret sur la signature. Jamais de souffle (whoosh) ni d'impact : ils cassent le calme.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 5`) : « Premium et calme » puis « Tech minimale », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture :** la première image est déjà le gros plan du panneau (rien de vide), la main entre tout de suite, le clic tombe vers 1 s.
- **Fin :** la carte d'annonce (pastille + titre, 1,5 s), puis la signature : la pastille de la marque (ou son logo) tourne et se pose, le nom s'écrit de gauche à droite et tient 1,2 s (2,5 s au moins pour une vidéo de page). L'original n'a pas de bouton ; pour une vidéo de vente, la signature peut céder la place à la fin du studio (recette 21, le bouton), sur le même papier clair.

## Ce qui ne se fera pas à l'identique

- La serif de l'original (dessin propriétaire) : la police de la marque, ou Source Serif 4.
- Le papier crème et le blanc cassé : les neutres de la marque (un papier gris très clair tiré de son clair et de son gris le plus clair, des cartes de son clair) ; aucune teinte crème inventée. Le nom du style reste pour l'instant « Interrupteurs crème ».
- Le bleu, le terracotta et la lavande : l'accent de la marque partout, plein ; le trait passe à l'encre si l'accent est trop clair sur le papier.
- Les logos des outils dans les rangs : des icônes du kit sur une tuile à l'accent (ou les vrais logos des outils de l'offre).
- La main : un pointeur redessiné.
- Le logo du partenaire entre les filets : le nom de l'offre (ou le logo de l'outil qui fait le lien chez le client).
- La caméra : plus de recadrages que l'original, pour passer le contrôle `rythme`.
- La grille de cartes : régulière (l'original décale une rangée sur deux), textes des cartes plus petits.
- Les étapes : révélées de gauche à droite, sans le scintillement continu de l'original.
- Le gros plan du début est posé dès la première image (l'original le fait apparaître en fondu).

## Sur une autre offre

- **Formation :** rangs = modules et bonus ; membres = élèves ; fenêtre = l'espace de formation où le module annoncé s'ouvre (d'après capture), ou l'assistant si la formation en a un. Mot fort : « Une fois. », « Inclus. ».
- **Coaching :** rangs = séances, groupe, ressources ; membres = les coachés ; cartes = leur espace ; fenêtre = l'agenda ou l'espace membre. Mot fort : « Pour tous. ».
- **Logiciel :** rangs = les fonctions ou les intégrations, avec leurs vrais logos (`studio_motion.py logos`) ; membres = l'équipe ou les clients ; fenêtre = le logiciel d'après capture ; le nom entre les filets = l'outil branché.
- **Toujours :** la cascade, le trait qui entoure et relie, la vague de coches, la carte qui devient fenêtre, la pastille d'annonce, le papier clair.

## En vertical et en carré

- **Scènes 1 et 3 :** elles se remettent en page seules en 9:16 (change `data-width` et `data-height` de leur racine en 1080 et 1920) : panneau en haut, phrase au milieu (84 px), membres sur deux rangées en bas ; la grille passe à 5 colonnes et sa rangée du milieu se vide pour la phrase. Essayées en 1080 × 1920.
- **Scène 4 :** la fenêtre et la carte se centrent seules (contenu à 86 %). C'est la scène la plus calme du kit : seule, `rythme` la trouve sous 1 événement par seconde (en 16:9 comme en 9:16). Bout à bout en 9:16, les quatre scènes passent sur LMDM (essai du 06/11/2026 : 1,08 événement par seconde, écart médian 0,80 s), mais tout juste : un accent jaune se voit peu sur le papier clair. Avec un accent clair, garde-lui un geste à l'encre de plus (une étape de plus, la main qui revient cliquer) ou raccourcis-la. En 9:16, la caméra du menu garde le « + » presque à sa place et un salut long se réduit seul : le salut reste entier dans les gros plans.
- **Scène 2 (testée, `trait-qui-relie-vertical.html`) :** sa propre mise en page 9:16, à monter à la place de `trait-qui-relie.html`. Le panneau reste en haut et les membres sur deux rangées en bas, exactement là où la scène 1 en 9:16 les laisse ; le mot fort (128 px), la phrase (84 px) et le nom (104 px) se posent au centre, entre les deux ; le trait descend par la droite du panneau pour souligner, puis passe sous lui et devient deux filets verticaux (du panneau à la phrase, de la phrase aux membres). À la fin, la caméra glisse vers le bas et la grille d'anneaux (5 colonnes, la cinquième arrive avec la vague) tombe pile sur la première image de la scène 3 en 9:16. Essayée bout à bout avec les quatre scènes en 1080 × 1920, sur une marque claire et sur LMDM.
- **Carré et 4:5 :** même logique que le vertical ; le panneau se coupe plus tôt (seule la colonne des interrupteurs reste), la phrase descend à 64 px.

## Les compositions du kit

Montées bout à bout dans cet ordre, elles raccordent image pour image (28,5 s) ; chacune vit aussi seule. Essai du 06/11/2026 sur la marque LMDM, avec les vrais faits de Publicitaire IA, en 16:9 et en 9:16 : `check` sans erreur ni avertissement, `palette` « ok », `rythme` « ok ». La police se règle par `--t05-titres` et `--t05-texte` ; les couleurs `--t05-*` en tête du style de chaque scène ne font que nommer les jetons de sa marque : ne les remplace jamais par une couleur écrite en dur.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/interrupteurs-cascade.html` | 6,5 s | le panneau en gros plan, le clic, la cascade, le recul, la phrase entourée, les membres | l'onglet, l'interrupteur maître, les RANGS, la phrase et ses mots entourés |
| `compositions/trait-qui-relie.html` | 6,5 s | le mot fort souligné, la phrase reliée par deux filets, le nom de l'offre, les membres qui deviennent des anneaux, le glissement vers la grille | MOT, PHRASE, NOM (ou un logo), les RANGS identiques à la scène 1 |
| `compositions/trait-qui-relie-vertical.html` | 6,5 s | la même scène remise en page en 9:16 : panneau en haut, textes au centre, filets verticaux, membres en bas, glissement vers le bas jusqu'à la grille | comme la version 16:9 |
| `compositions/grille-de-coches.html` | 6,5 s | la vague de coches, le zoom et la phrase, les cartes des membres, la plongée | TEXTE, SALUTS, ACCUEIL |
| `compositions/fenetre-annonce.html` | 9 s | la fenêtre, le menu « + » en cascade, la demande, les étapes, la pastille et le titre, la signature | SALUT, ACCUEIL, MENU, DEMANDE et ETAPES (seulement si son offre a vraiment un champ de demande, section 7), PASTILLE, TITRE, NOM, LOGO |
