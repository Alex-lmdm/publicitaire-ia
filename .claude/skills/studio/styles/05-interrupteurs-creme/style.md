# Template n°5 · Interrupteurs crème · d'après ClaudeDevs (https://x.com/ClaudeDevs/status/2091953609185657251)

**Ce qu'on voit :** sur un papier crème, un panneau de réglages vu de très près : une main clique, les interrupteurs s'allument en cascade. Puis des phrases calmes au centre, un trait à main levée qui entoure, souligne et relie, une grille de pastilles qui se cochent en vague, et la fenêtre de l'offre qui travaille avant la carte d'annonce.
**Souvent utile pour :** annoncer une nouveauté (un module, un bonus, une fonction, une mise à jour), ou montrer qu'un seul réglage sert tout le monde.
**D'après :** X · ClaudeDevs, « Authorize once » · 34 s · 16:9 (1920 × 1080, 24 images par seconde).
**Mesures de l'original (`studio_motion.py reference`) :** 0,62 événement par seconde, écart médian 0,50 s entre deux, 8,5 s d'image figée en tout, aucune coupe franche.
**Mesures du kit monté (les 4 scènes bout à bout, 28,5 s, marque de test) :** `rythme` répond « ok » : 1,16 événement par seconde, écart médian 0,80 s, aucune image figée.

> On reprend la grammaire de la vidéo, jamais son contenu : ni ses textes, ni l'interface et les
> logos de Claude, ni les logos de ses partenaires, ni sa musique. L'interface du kit est neutre et
> prend les couleurs du client.

## 1. Le rythme

- Calme et régulier : un geste à la fois, posé sur une grille de 0,5 s (la musique tourne autour de 118 battements par minute). Les textes entrent par un flou qui se dissipe, sans saut ; la caméra fait de grands mouvements rares et nets (le recul, le glissement, la plongée).
- L'original ne fait que 0,62 événement par seconde : trop calme pour le contrôle `rythme` du studio (1 au moins, 0,8 s d'écart médian au plus). Le kit garde le calme mais **recadre doucement à chaque phrase** (0,5 à 0,8 s, expo.inOut, 4 à 13 % d'échelle, avec un léger glissement de côté : un zoom pile au centre ne se mesure pas) et donne un petit coup de caméra à chaque clic. C'est ce qui le fait passer : ne retire pas ces recadrages.
- Une couleur de marque claire (jaune, pastel) change peu la luminosité : le contrôle compte alors surtout les textes, le trait, la main et la caméra. Avec un accent foncé, la cascade et les coches comptent aussi.
- Tenue d'un texte : 1 à 1,5 s, jamais plus sans un recadrage ou un geste autour.

## 2. La structure

L'original, scène par scène (c'est une annonce : il n'a pas de bloc « problème ») :

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

Le kit regroupe ces temps en quatre scènes (section « Les compositions du kit ») : 1 + 2, puis 3 + 4, puis la preuve, puis la démonstration, l'offre et la signature. Pour une vidéo de vente, place avant la scène 1 une recette « problème » du studio (la corvée, recette 1) sur le même papier crème.

## 3. Les fonds et les couleurs

| Rôle | Original | Chez le client |
|---|---|---|
| Papier, le fond de tout | crème #EFEFE5 | gardé, c'est le look : `--t05-papier`. Un crème plus chaud ou plus froid se règle là ; jamais le fond sombre de la marque. |
| Panneau, disques, cartes, fenêtre | blanc cassé #F9FAF5 | `--t05-carte` |
| Onglet, rails éteints | #DDDDD1 | `--t05-pli` |
| Textes | encre presque noire | `--t05-encre` |
| Interrupteurs allumés | bleu d'interface #3588D6 | l'accent de la marque (`--t05-allume`) ; la bille reste blanche avec une ombre |
| Trait à main levée, pastilles cochées | terracotta #D26E57, la couleur de la marque d'origine | l'accent de la marque. S'il est trop clair sur le crème (contraste sous 2 : un jaune, un pastel), le trait et les anneaux passent **tout seuls** à l'encre ; la pastille reste à l'accent, avec une coche de la couleur lisible dessus (`--brand-contrast`) |
| Icônes des membres | lavande #8276B8 | gris neutre `--t05-gris` |
| Icônes des rangs et des étapes | les vrais logos des outils | une icône du kit sur une tuile à l'accent, ou les vrais logos si l'offre branche des outils |

Un seul fond pendant presque toute la vidéo ; la bascule, c'est le passage du papier crème à la fenêtre blanc cassé (scène 3 vers scène 4). N'ajoute ni fond sombre ni plein écran de couleur au milieu : le look s'effondre. Seule exception possible : la signature finale sur la couleur de la marque.

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
| Salut de la fenêtre | 64 px | 55 px (fenêtre à 86 %) |
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
- Chez le client : le panneau, ce sont les parties de son offre (modules, bonus, fonctions) ; les disques, ses membres (élèves, clients) ; les cartes, l'espace de chacun ; la fenêtre, son produit en action : un champ de demande si l'offre est un outil d'IA, sinon son espace de formation ou son logiciel reconstruit d'après capture. Jamais l'interface de Claude.
- Interfaces neutres et propres : coins arrondis (24 px), filets fins, ombres douces, interrupteurs à bille. Jamais de faux navigateur.

## 8. Le son

- Original : une musique douce et régulière (environ 118 battements par minute, sans montée ni chute), des clics d'interface légers sur la cascade (quatre clics à 0,125 s), la musique se pose sur la signature.
- Chez le client : une musique de lancement calme (`musiques choisir --ambiance "Premium et calme"`, ou « Tech minimale »), calée à 120. Bruitages petits et secs : un clic doux par interrupteur, un « pop » léger par disque, un frottement de crayon sur la boucle, un tintement discret sur la signature. Jamais de souffle (whoosh) ni d'impact : ils cassent le calme.

## 9. L'ouverture et la fin

- **Ouverture :** la première image est déjà le gros plan du panneau (rien de vide), la main entre tout de suite, le clic tombe vers 1 s.
- **Fin :** la carte d'annonce (pastille + titre, 1,5 s), puis la signature : la pastille de la marque (ou son logo) tourne et se pose, le nom s'écrit de gauche à droite et tient 1,2 s (2,5 s au moins pour une vidéo de page). L'original n'a pas de bouton ; pour une vidéo de vente, la signature peut céder la place à la fin du studio (recette 21, le bouton), sur le même crème.

## Ce qui ne se fera pas à l'identique

- La serif de l'original (dessin propriétaire) : la police de la marque, ou Source Serif 4.
- Le bleu, le terracotta et la lavande : l'accent de la marque partout ; le trait passe à l'encre si l'accent est trop clair sur le crème.
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
- **Toujours :** la cascade, le trait qui entoure et relie, la vague de coches, la carte qui devient fenêtre, la pastille d'annonce, le papier crème.

## En vertical et en carré

- **Scènes 1 et 3 :** elles se remettent en page seules en 9:16 (change `data-width` et `data-height` de leur racine en 1080 et 1920) : panneau en haut, phrase au milieu (84 px), membres sur deux rangées en bas ; la grille passe à 5 colonnes et sa rangée du milieu se vide pour la phrase. Essayées en 1080 × 1920.
- **Scène 4 :** la fenêtre et la carte se centrent seules (contenu à 86 %).
- **Scène 2 :** en 16:9 seulement. En vertical : panneau en haut, phrase au centre, membres en bas, filets verticaux ; ou saute-la et passe de la scène 1 à la scène 3 par un recul.
- **Carré et 4:5 :** même logique que le vertical ; le panneau se coupe plus tôt (seule la colonne des interrupteurs reste), la phrase descend à 64 px.

## Les compositions du kit

Montées bout à bout dans cet ordre, elles raccordent image pour image (28,5 s) ; chacune vit aussi seule. Les couleurs et la police se règlent par les variables `--t05-*` en tête du style de chaque scène.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/interrupteurs-cascade.html` | 6,5 s | le panneau en gros plan, le clic, la cascade, le recul, la phrase entourée, les membres | l'onglet, l'interrupteur maître, les RANGS, la phrase et ses mots entourés |
| `compositions/trait-qui-relie.html` | 6,5 s | le mot fort souligné, la phrase reliée par deux filets, le nom de l'offre, les membres qui deviennent des anneaux, le glissement vers la grille | MOT, PHRASE, NOM (ou un logo), les RANGS identiques à la scène 1 |
| `compositions/grille-de-coches.html` | 6,5 s | la vague de coches, le zoom et la phrase, les cartes des membres, la plongée | TEXTE, SALUTS, ACCUEIL |
| `compositions/fenetre-annonce.html` | 9 s | la fenêtre, le menu « + » en cascade, la demande, les étapes, la pastille et le titre, la signature | SALUT, ACCUEIL, MENU, DEMANDE, ETAPES, PASTILLE, TITRE, NOM, LOGO |
