# Notes de maintenance · Style n°7 · Phrase tapée

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/07-phrase-tapee/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les essais mesurés, ce qui ne se refait pas) est rangé ici.

## Les mesures, sorties de la fiche

- **L'original (`studio_motion.py reference`) :** X · Zaro · vidéo de lancement · 68 s · 16:9
  (1920 × 1080, 30 images/s). 1,56 événement par seconde, écart médian 0,30 s entre deux
  événements, 16 coupes franches (presque toutes avec un changement de fond), 4,4 s d'image figée
  au total. Musique à 104 battements par minute (un temps toutes les 0,58 s), un silence net à 4,5 s
  puis l'entrée franche à 5,0 s ; 4,5 s d'introduction, un passage plus calme pendant la recherche
  dans les fichiers.
- **Essai du kit refait le 06/11/2026** (les 4 scènes bout à bout, 48,9 s, marque LMDM, avec ses
  vraies images et les logos de ses outils, chaque texte tenu le temps de sa lecture, aucun
  recadrage pendant une lecture) : `rythme` « ok », 0,88 événement par seconde en 16:9 et 0,71 en
  9:16 (écart médian 0,70 s), aucune image figée ; `palette` « ok » (ses images tombent sans
  fondu). L'essai d'avant (28,6 s, 1,48 événement par seconde) tenait ses phrases 0,3 à 0,9 s :
  trop vite pour les lire.
- **La règle « jamais une teinte tirée de l'accent »** est née de l'essai du 03/11/2026 et de la
  story refusée du 06/11/2026.
- **La vidéo du haut de la page de Publicitaire IA (03/11/2026)**, exemple de la fiche : la phrase
  et ses objets, le mot géant, le désordre réduit en points, l'orbite et le point d'encre venaient
  du kit ; le dossier déposé sur Claude et la conversation dans Claude avaient été construits pour
  son cas, dans ce style.

## L'original, scène par scène

Un exemple et pas un plan à suivre (ses couleurs, ses images et ses textes restent les siens : on
n'en garde que les gestes) :

| Scène de l'original (temps approximatifs) | Rôle | Ce qui s'y passe | Dans le kit |
|---|---|---|---|
| 0 → 2,5 s | accroche | une phrase mot à mot sur fond presque noir, avec deux objets glissés dans la ligne (une vignette qui change, une pastille avec son curseur en pixels) | `t7-accroche` |
| 2,5 → 4,5 s | accroche | la suite de la phrase ; ses mots s'allument tour à tour à la couleur d'accent ; poussière de pixels | `t7-accroche` |
| 4,5 → 8,5 s | nom | un silence ; un mot géant tapé sur un nuage de la couleur d'accent ; coupe sur fond clair : le logo devient net, le nom sort | `t7-accroche` |
| 8,5 → 13 s | solution | deux lignes tapées sur un taupe ; coupe : la barre de demande où la phrase se tape, clic sur envoyer | `t7-phrase` |
| 13 → 20 s | démonstration | la fenêtre du produit se construit ; une relance tapée dans le chat | `t7-phrase` (la fenêtre) |
| 20 → 28 s | fonction | deux lignes tapées, des pastilles en pixels avec leurs curseurs ; une carte de liste entourée de contours en écho | non construit |
| 28 → 39 s | preuve | glisser-déposer dans un tableau, des graphiques ; « simple / puissant » en écran coupé sombre et clair, un schéma de flux | non construit |
| 39 → 44 s | problème rangé | une grande phrase retapée trois fois ; à chaque fin, des icônes d'applis, des notes et des fichiers surgissent ; tout se change en points ; la conclusion en écriture de points | `t7-eparpille` (rangé autrement, voir plus bas) |
| 44 → 59 s | démonstration | les fichiers, les connexions, une grande question tapée, la réponse, la liste des sources qui défile, le téléphone | non construit |
| 59 → 65 s | promesse | la carte du produit DANS une phrase ; orbites en pointillés, outils qui tournent ; recul sur une galaxie de systèmes, conclusion tapée | `t7-orbite` |
| 65 → 68,5 s | appel | coupe sur fond clair : un point d'encre se contracte et devient le logo ; pastille d'appel en capitales | `t7-orbite` |

## Les couleurs mesurées de l'original

| Dans l'original | Son rôle | Avec la marque du client |
|---|---|---|
| Noir chaud | l'ouverture, le recul de l'orbite | la nuit |
| Taupe chaud | les phrases tapées sur deux lignes, l'orbite | l'ardoise (`--brand-gris-1`) |
| Nuage de lavande | le mot géant | l'aplat plein de l'accent |
| Blanc cassé chaud | les interfaces, les objets éparpillés, le logo | son clair |
| Blanc cassé | le texte sur le noir et le taupe | son clair |
| Lavande | le curseur de frappe, les mots qui s'allument, la pastille, les liserés | l'accent plein (`--brand-accent-lisible` pour un mot sur la nuit) |
| Gris clair | la 2e ligne d'une phrase, les mots d'appui | `--brand-gris-4` sur l'ardoise, `--brand-gris-3` sur la nuit |
| Encre | texte sur fond clair, bouton d'envoi, point final | `--brand-sombre` |
| Blanc pur | cartes, barre de demande, fenêtres | son clair |

## Ce qui ne se fera pas à l'identique

- **Les images de l'original** (ses vignettes, ses notes, ses fichiers, ses captures du logiciel,
  ses icônes d'applis) ne se refont pas : la vignette, les objets éparpillés, la fenêtre et la carte
  prennent sa vraie matière (ses captures, ses miniatures, ses photos, les logos de ses outils), ou
  des mots. Jamais un faux document, un faux dossier, une fausse note, un squelette de carte, une
  icône de remplacement ni une galaxie décorative.
- **Ses couleurs** (le noir, le taupe et le blanc cassé chauds, la lavande) → celles de sa marque
  seulement : sa nuit, son ardoise, son clair, son accent plein.
- **Le nuage de lavande du mot géant** → l'aplat plein de son accent ; jamais un nuage de l'accent
  mêlé de blanc. Les grappes de pixels qui battaient dessus sont retirées depuis le 07/11/2026.
- **L'éclat de l'orbite** (un halo de couleur derrière la carte) → les orbites et la carte qui
  passent d'un coup à l'accent plein, le temps d'un battement.
- **Les logos d'applis de l'original** → ceux des outils du client (`studio_motion.py logos`) ; une
  marque absente des registres se demande au client, jamais redessinée.
- **Les icônes en pixel-art et les pastilles en points avec leurs curseurs** (la scène des
  « agents ») → seulement la pastille de l'ouverture et son curseur en pixels.
- **La police matricielle** (l'écriture en points de la conclusion) → la conclusion tapée dans la
  police de la marque (depuis le 07/11/2026 ; avant, la police de la marque vue à travers une trame
  de points).
- **La lavande sur fond clair** (curseur, liserés) → l'accent seulement en aplat sur le clair.
- **La police à chasse fixe de la pastille** → la police de la marque en capitales espacées.
- **La galaxie** (des dizaines de systèmes en vraie profondeur) → ses autres systèmes, de vrais
  noms, dans un même plan et un flou d'ensemble ; sans eux, le recul se fait sur l'orbite seule.
- **Les scènes d'interface en action** (relance dans le chat, tableau glissé, graphiques, écran
  coupé, schéma de flux, fichiers, liste des sources qui défile, téléphone) : non construites dans
  le kit ; elles se refont avec les mêmes briques et sa vraie matière.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit (mots, tailles,
caméra, palette, formes sans sujet) et que l'IA copie surtout le code des scènes.

**La fiche** (28 815 → 20 109 octets, −30 %) :
- Sorti vers cette note : les mesures de l'original et des essais, l'original scène par scène, la
  colonne « Dans l'original » des couleurs, « Ce qui ne se fera pas à l'identique », les dates, la
  citation « On reprend la grammaire… » et l'ouverture de la section 2 (dites une fois par
  l'index), l'exemple tiré de la vidéo de la page de Publicitaire IA.
- « 8 mots conseillés » → « 8 mots au plus » ; tenue de 2 s au moins pour l'accroche gardée.
- « La caméra fait une dérive ou une poussée lente (3 à 12 %) pendant la lecture » → une phrase
  posée ne bouge plus ; seuls le monde ou les anneaux dérivent (2 à 5 %).
- Lien `../../references/style.md` → `../../references/image.md` ; « Premium et calme » et
  « Tech minimale » cités par leur vrai nom.
- « Le désordre réduit en points » devient « Le désordre rangé » (voir `t7-eparpille`) ; la
  « poussière de pixels » (ouverture, fin) et les « grappes de pixels » du mot géant disparaissent
  des sections 1, 2, 5 et 9 ; le point d'encre n'existe plus qu'avec un logo (une transition, plus
  un objet sans sujet).
- La table de typographie suit les scènes (pastille 42 px, pilules 30 px au moins, carte 42/36 px,
  étiquettes 32 px, pastille d'appel 34 px, mot géant et nom de fin calculés à 60 à 90 % de la
  largeur) ; la table des compositions dit les champs d'`EXEMPLE` et les nouvelles durées.

**Les scènes** (toutes : `R` fondu dans `EXEMPLE`, un objet unique marqué « À REMPLACER », valeurs
neutres d'une formation, d'un coaching et d'un logiciel ; aucun texte tiré des offres de l'auteur) :
- `t7-accroche` : poussière de pixels sur la nuit et grappes de pixels sur l'aplat et le clair
  retirées ; la vignette ne porte plus que de vraies images (des mots qui défilaient toutes les
  0,45 s ne se lisaient pas, à 20 px) et se retire sans elles ; la pastille porte un seul mot à
  42 px (au lieu de trois mots changeants à 22 px) ; le premier mot est là dès la première image
  (une ouverture jamais vide) ; aucune phrase ne grossit pendant sa lecture ; mot géant et nom
  calculés à 60 à 90 % de la largeur ; la suite passe à la ligne en 9:16 (elle débordait). 11,2 s.
- `t7-phrase` : textes génériques (un logiciel qui résume une page) ; le recul de caméra finit avec
  la frappe de la demande (il continuait 0,7 s sous la lecture), dérive de 2 % ensuite ; la fenêtre
  ne s'incline plus que de 4° et 2 % ; feux décoratifs de la fenêtre retirés ; sous-titre 22 → 32 px,
  adresse 24 → 30 px ; fond des cartes en `--brand-gris-4` au lieu d'un voile noir. 12,2 s (8,9 sans
  fenêtre).
- `t7-eparpille` : les `●` et `▬` (formes sans sujet), `logo-capcut` et les mots tirés des vidéos de
  l'auteur retirés ; « tout se change en points et file au centre » (une poussière décorative)
  remplacé par un vrai rangement : chaque objet file vers sa place dans trois rangs nets (captures,
  outils, mots), se redresse et devient net ; la conclusion en écriture de points dans son cadre de
  points qui scintillaient devient une phrase tapée à la place de la phrase ; un mot en pilule n'est
  plus jamais flou ni coupé par le bord (sa dérive est comptée), et fait 30 px au moins ; 5 mots en
  pilule au plus, pour rester sous 8 mots à l'écran. 10,1 s.
- `t7-orbite` : couleur en dur `#202022` (le fond tweené vers la nuit) → un calque de
  `--brand-sombre` qui apparaît ; les points décoratifs des anneaux retirés : les orbites portent
  ses logos et ses captures (et au besoin deux étiquettes), une orbite vide ne se dessine pas ; tuiles
  et étiquettes en voile blanc → `--brand-clair` ; liseré blanc translucide autour des cartes
  retiré ; textes de la carte 27/18/16 px → 42/36 px (la ligne du bas retirée : trop de mots) et
  étiquettes 17 → 32 px ; la poussée pendant la lecture passe de 12 % sur tout le monde à 5 % sur
  les seuls anneaux ; les mots de la carte s'effacent au recul (ils passaient à 11 px sous la
  conclusion) ; les noms des autres systèmes, vus seulement de loin et flous, sont marqués
  `data-layout-ignore` ; poussière de pixels de la fin retirée ; le point d'encre n'existe qu'avec
  un logo ; nom de fin calculé à 60 à 90 % de la largeur. 15,2 s.

**Vérifié** sur le banc « Banc styles 07 · 2026-11-07 » (16:9 et 9:16, les quatre scènes bout à bout,
plus des variantes sans images, sans logo, avec une capture et avec étiquettes) : `check` sans
erreur ni avertissement de lecture ou de taille ; planches regardées à chaque moment clé.
