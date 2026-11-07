# Notes de maintenance · Style n°5 · Interrupteurs en cascade

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/05-interrupteurs-creme/style.md`) dit la règle au présent ; ce qui l'a
fait naître (l'original scène par scène, les mesures, les essais datés, l'ancien nom) est rangé ici.

## L'original et son nom

- **Ancien nom** : « Interrupteurs crème » (jusqu'à la 0.9.0 ; il désigne toujours ce style, l'index
  le dit). Un nom de couleur, devenu faux quand le style a pris les couleurs de la marque.
- **D'après** : X · ClaudeDevs, « Authorize once » · 34 s · 16:9 (1920 × 1080, 24 images par
  seconde).
- **Mesures de l'original (`studio_motion.py reference`)** : 0,62 événement par seconde, écart
  médian 0,50 s entre deux, 8,5 s d'image figée en tout, aucune coupe franche.
- **Mesures du kit refait le 06/11/2026** (les 4 scènes bout à bout, 42,1 s, marque LMDM, chaque
  texte tenu le temps de sa lecture, aucun recadrage pendant une lecture, la vie venue des
  événements de contenu) : `rythme` « ok » : 0,81 événement par seconde en 16:9 (écart médian
  1,0 s) et 0,78 en 9:16 (1,1 s), aucune image figée ; `palette` « ok ». Le kit d'avant ne passait
  que par des recadrages toutes les 0,6 à 0,8 s sous les phrases, retirés (story refusée du
  06/11/2026).
- **Essai du 06/11/2026** : sans recadrage, les gestes fins de l'original (des traits de 7 px, des
  billes, des coches sur un papier clair) ne donnaient que 0,4 événement par seconde au contrôle
  `rythme`, même avec un accent foncé. D'où les événements francs du kit (section 1 de la fiche).
- **Essai du kit du 06/11/2026** sur la marque LMDM, avec les vrais faits de l'offre de l'auteur,
  en 16:9 et en 9:16 : `check` sans erreur ni avertissement, `palette` « ok », `rythme` « ok »
  (0,81 et 0,78 événement par seconde). La version verticale de la scène 2 a été essayée bout à
  bout avec les quatre scènes en 1080 × 1920, sur une marque claire et sur LMDM.
- **La police** : Source Serif 4 essayée sur le projet d'essai : le rendu la prend.
- **La fenêtre par défaut** (champ de demande, demande tapée, étapes) : la fiche citait l'offre de
  l'auteur, qui vit dans un assistant, comme exemple d'une offre qui a vraiment ce champ.

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (c'est une annonce : il n'a pas de bloc
« problème ») :

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

Le kit regroupe ces temps en quatre scènes : 1 + 2, puis 3 + 4, puis la preuve, puis la
démonstration, l'offre et la signature.

### Les couleurs mesurées de l'original

| Rôle | Original |
|---|---|
| Papier, le fond de tout | crème #EFEFE5 |
| Panneau, disques, cartes, fenêtre | blanc cassé #F9FAF5 |
| Onglet, rails éteints, bulle, bouton inactif | #DDDDD1 |
| Textes | encre presque noire |
| Interrupteurs allumés | bleu d'interface #3588D6 |
| Trait à main levée, pastilles cochées | terracotta #D26E57, la couleur de la marque d'origine |
| Icônes des membres | lavande #8276B8 |
| Icônes des rangs et des étapes | les vrais logos des outils |
| Ombres | ombres chaudes, teintées |

Contraste mesuré sur la marque d'essai : sa couleur sombre sur le papier, 13:1.

## Ce qui ne se fera pas à l'identique

- La serif de l'original (dessin propriétaire) : la police de la marque, ou Source Serif 4.
- Le papier crème et le blanc cassé : les neutres de la marque (un papier gris très clair tiré de
  son clair et de son gris le plus clair, des cartes de son clair) ; aucune teinte crème inventée.
- Le bleu, le terracotta et la lavande : l'accent de la marque partout, plein ; le trait passe à
  l'encre si l'accent est trop clair sur le papier.
- Les logos des outils dans les rangs : des icônes du kit sur une tuile à l'accent (ou les vrais
  logos des outils de l'offre).
- La main : un pointeur redessiné.
- Le logo du partenaire entre les filets : le nom de l'offre (ou le logo de l'outil qui fait le
  lien chez le client).
- La caméra : aussi calme que l'original pendant les lectures (une dérive lente), ce qui laisse le
  kit sous le seuil de `rythme` sans les événements de contenu.
- La grille de cartes : régulière (l'original décale une rangée sur deux), textes des cartes plus
  petits (de la texture).
- Les étapes : révélées de gauche à droite, sans le scintillement continu de l'original.
- Le gros plan du début est posé dès la première image (l'original le fait apparaître en fondu).
- (Depuis le 07/11/2026) Les coches de la grille cochent de vrais éléments de l'offre, écrits dans
  leur disque ; l'original ne cochait que des membres anonymes.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit, et que l'IA copie
surtout le code des scènes. Taille de la fiche : 24 657 octets avant, 16 937 après (31 % de moins).
Vérifié sur le banc « Banc styles 05 » (marque sombre, accent jaune), les quatre scènes bout à bout
en 16:9 et en 9:16 (43,5 s) : `check` sans erreur ni avertissement (hors `film_silent`, le banc n'a
pas de son).

Dans la fiche :
- Sortis vers cette note : l'ancien nom, la ligne « D'après », les mesures de l'original et du kit,
  les essais datés, « L'original, pour mémoire », la colonne des couleurs mesurées, « Ce qui ne se
  fera pas à l'identique », l'exemple tiré de l'offre de l'auteur (section 7), la marque d'essai.
- Retirés parce que l'index les dit (« Appliquer un style ») : la citation « On reprend la
  grammaire… », l'ouverture de la section 2, « Sur n'importe quelle marque » (sauf ce qui est propre
  au style : le look reste clair sur une marque sombre), la ligne de contraste.
- Corrigé : « 8 mots conseillés » devient « 8 au plus » ; « une phrase plus longue ne se raccourcit
  jamais : elle passe sur deux lignes plus petites » contredisait « jamais en réduisant la police » :
  elle passe désormais dans une scène construite dans le style (la réduction automatique des scènes
  ne rattrape qu'une police de marque plus large) ; le « petit coup de caméra au clic » disparaît
  (un pas de caméra sous un texte) ; le mot fort, le nom entre les filets et la signature sont des
  mots héros (60 % de la largeur ou plus) ; la table de typographie suit les scènes ; les liens
  visent `references/image.md`, `mouvement.md` et `scenes.md` (les recettes) au lieu de
  `references/style.md` et des recettes du skill.

Dans les scènes (toutes) : un objet `EXEMPLE` en tête du script, marqué « À REMPLACER », regroupe
les textes d'exemple (le HTML n'en porte plus) ; l'en-tête dit « À remplacer : l'objet EXEMPLE » ;
plus de couleur en dur (la main, les billes, les champs et le menu prennent `--brand-clair`,
`--brand-sombre` ou `--t05-carte`) ; plus de `z-index` négatif sous les blocs pleins.
- `interrupteurs-cascade` : le gros plan montre tout le panneau (chaque réglage lu à 42 px, le
  panneau à plus de la moitié du cadre ; avant, le dernier rang n'était à l'image que 0,27 s) ; la
  caméra ne fait qu'une dérive jusqu'au recul (elle suivait la cascade par un glissement) ; rangs
  à 28 px (26 avant : sous le plancher une fois le panneau au bord) ; phrase à 80 px en 16:9 (72) ;
  la boucle du trait ne coupe plus le mot voisin.
- `trait-qui-relie` et `-vertical` : le mot fort devient un mot héros (62 % de la largeur, caméra
  approchée en 16:9), le nom entre les filets aussi grand que les filets le permettent (64 % en
  9:16) ; rangs à 28 px ; le nom du maître dans `EXEMPLE`.
- `grille-de-coches` : la caméra s'approche avant la vague, et chaque coche autour de la phrase
  coche un vrai élément de l'offre (`EXEMPLE.COCHES`, son nom dans le disque, 31 px à l'image) ;
  avant, une grille de pastilles anonymes était seule sujet du plan. Les miniatures des cartes
  sont de la texture (`data-layout-ignore`) ; champ à 34 px (raccord avec la scène 4).
- `fenetre-annonce` : menu à 33 px et champ à 34 px (24 et 26 px en 9:16 avant) ; plus de coups de
  caméra au clic ni d'allers-retours sous le salut : une dérive, un recadrage vers le champ, une
  dérive, un recadrage vers les étapes ; le zoom du champ ne le coupe plus en 9:16 ; le menu et la
  demande tapée restent le temps de leur lecture (la scène passe de 16,7 à 18,5 s) ; titre de la
  carte à 80 px ; la signature est le mot héros de la fin (62 % de la largeur) ; la pastille se
  remplit d'un coup (le fondu passait par un contraste de 1,4:1).
