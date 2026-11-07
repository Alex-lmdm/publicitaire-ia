# Notes de maintenance · Style n°3 · Verre sombre

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/03-verre-sombre/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les mesures, les essais datés) est rangé ici.

## Ce qui sortait de la fiche lors du ménage du 07/11/2026

### L'original et les mesures

**D'après :** X · Polymarket · « Perps » · 37 s · 16:9 (1920 × 1080, 24 images/s).
**Mesures de l'original (`studio_motion.py reference`) :** 1,92 événement par seconde, écart
médian 0,30 s entre deux événements, 2 coupes franches seulement (à 28,2 s), 7,0 s d'image figée au
total (surtout la fin : l'adresse et le logo tenus en silence). Musique à 93 battements par minute
(un temps toutes les 0,65 s), entrée franche à 7,0 s.
**Mesures de l'essai du kit refait le 06/11/2026** (les 4 scènes bout à bout, 33 s, marque LMDM,
chaque phrase tenue le temps de sa lecture, ses vraies captures autour de l'accroche et sous
l'appel, aucun recadrage pendant une lecture) : en 16:9, 1,09 événement par seconde, écart médian
0,70 s ; en 9:16, 1,02 événement par seconde, écart médian 0,80 s ; aucune image figée, `rythme`
et `palette` « ok » dans les deux formats.

La citation qui ouvrait la fiche (désormais dite une fois dans l'index, `README.md`) :

> On reprend la grammaire de la vidéo (rythme, mise en page, verre, caméra, trame de points,
> transitions), jamais son contenu : ni ses textes, ni son logo, ni ses marchés, ni ses chiffres, ni
> sa musique, ni sa nuit bleue. Tout passe aux seules couleurs et à la police de la marque du client.

Section 1, sur l'original : « Deux coupes franches en 37 s : le rythme vient de la caméra (recul,
glissé, plongée) » ; « 7 s d'accroche presque silencieuse » ; « un carrousel très rapide (une
carte toutes les 0,5 s) ». Essai du 06/11/2026 : le recadrage sec ajouté sous l'accroche pour
nourrir `rythme` a été retiré (la fiche garde la leçon : la matière, jamais un recadrage).

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre :

| Scène de l'original | Rôle | Durée | Ce qui s'y passe | Dans le kit |
|---|---|---|---|---|
| La promesse | accroche | 3,3 s | deux mots géants, flous, deviennent nets ; la caméra recule d'un coup, la phrase finit petite, sa fin en couleur | `t3-onglets` |
| Les onglets | problème (le choix) | 3,6 s | une barre d'onglets entre, défile très vite sous une pastille fixe, qui se pose sur le produit ; on plonge dans ce bouton posé sur une trame de points | `t3-onglets` |
| Le nom | solution | 2,5 s | « Découvre … » se forme en points puis devient net, entrée franche de la musique | `t3-onglets` |
| L'interface entière | solution | 3,5 s | toute l'interface inclinée, la caméra glisse et se pose sur une carte | à refaire avec le verre du kit |
| Le bon de commande | démonstration et prix | 6,5 s | le bon pivote et entre ; montant, pastilles, curseur glissé, interrupteur, champs, total, bouton cliqué qui se défait en points | `t3-commande` |
| Le bénéfice | preuve | 1,6 s | une ligne mot à mot, une carte en points pivote entre deux mots | non construit |
| L'interface éclatée | preuve | 4 s | trois couches d'interface en 3D (graphique devant, listes derrière), le curseur clique | non construit |
| Le carrousel | offre | 2,6 s | un mot seul, puis une carte en gros plan toutes les 0,5 s | `t3-cartes` |
| L'appel | appel | 2,5 s | coupe franche dans le silence : le verbe seul, puis la ligne complète | `t3-fin` |
| L'adresse et le logo | appel | 6,5 s | l'adresse qui brille (un impact), puis le logo et le nom, tenus | `t3-fin` |

### Les couleurs de l'original (section 3)

| Dans l'original | Son rôle | Avec la marque du client |
|---|---|---|
| Bleu nuit presque noir | le fond de toute la vidéo | `var(--brand-sombre)` : la couleur la plus sombre de la marque (LMDM : son anthracite ; une marque claire : la couleur de son texte) |
| Lueur bleue diffuse en haut à gauche, plus faible en bas à droite | la lumière de la scène, qui bouge doucement | du blanc très faible (7,5 % en haut à gauche, 4 % en bas à droite), qui glisse ; jamais teinté de l'accent |
| Bleu vif | le mot de la fin de phrase, la pastille choisie, le bouton principal, le curseur rempli | `var(--brand-accent)` plein : le cercle de la pastille (un trait de 2 px), son remplissage, le bouton, la piste remplie, l'interrupteur, la tuile des cartes ; le texte posé dessus en `var(--brand-contrast)` ; un mot ou un chiffre à l'accent sur la nuit en `var(--brand-accent-lisible)` |
| Halo bleu autour de la pastille et du bouton, lueur sur le texte qui se forme | la lumière de l'interface | aucun halo : la pastille est cerclée d'un trait plein puis se remplit par un volet, le bouton est plein ; la lueur du texte est blanche |
| Verre sombre (liseré clair en haut, reflets blancs à 10-25 %) | les interfaces et les cartes | un noir en transparence (`rgba(0, 0, 0, .42)`) posé sur la nuit, avec les mêmes liserés et reflets blancs |
| Blanc, gris bleuté | textes, onglets inactifs, libellés | `var(--brand-clair)` et `var(--brand-gris-3)` (`var(--brand-gris-4)` pour un libellé d'appui plus clair) |
| Trame de points blancs | derrière le bouton, les cartes, et le texte qui se forme | identique (points blancs à 15-25 %) |
| Vert et rouge (hausse, baisse) | le sens propre au trading | non repris : dans un bon de commande, l'accent suffit |

La note datée de la section 3 : un jaune à demi transparent sur la nuit devient olive ou brun
(story refusée du 06/11/2026).

### « Le flou et l'accent », tel qu'il était

**Le flou et l'accent.** Un bouton ou une pastille à l'accent qui passe dans un flou mêle son jaune
et son texte foncé à la nuit : `palette` relève ces images. D'où les réglages du kit, à garder : des
bandes de profondeur de champ courtes et douces (6 px), des cartes qui glissent sans flou, un bon qui
recule sans s'effacer (la coupe le fait disparaître), une lame claire qui se retire par un balayage
et non par un fondu, une liste qui s'estompe écrite en clair (seule sa ligne pleine, au milieu,
prend l'accent). Mesure-le sur le rendu de chaque vidéo.

### Ce qui ne se fera pas à l'identique

- **Les images de l'original** : il n'en a pas (que son interface et sa typographie). Un plan de sa
  vidéo qui en demanderait une prend sa vraie matière (une capture de sa page, de son produit), ou
  rien ; on ne la redessine jamais.
- **La profondeur de champ optique** (flou réel selon la distance) → deux bandes floues fixes en haut
  et en bas de l'image, courtes et douces (6 px) : l'effet est le même tant que le bon est incliné,
  mais le flou ne suit pas un objet qui sortirait de la bande nette.
- **Le flou de mouvement** de chaque déplacement → un flou horizontal sur la barre d'onglets
  seulement ; les autres mouvements restent nets (une carte floue mêlerait son accent à la nuit).
- **La lueur optique** (halo réel de la lumière sur le texte, halo bleu autour des boutons) → une
  ombre douce et blanche sous le texte ; autour de la pastille et du bouton, rien : l'accent plein
  suffit.
- **Le bleu nuit et sa lumière bleue** → la nuit de la marque (`--brand-sombre`) et une lueur
  blanche très faible ; jamais une nuit ou une lueur tirée de l'accent.
- **Sa police maison** → la police de la marque (Poppins pour LMDM, plus ronde et plus large ; Inter
  si la marque n'impose rien).
- **Les chiffres qui défilent au-dessus des boutons** (prix du marché) → les lignes réelles de chaque
  carte qui montent une à une.
- **L'interface entière inclinée, la ligne au carré de points qui pivote, l'interface éclatée en
  couches** : non construites dans le kit ; elles se refont avec le même verre (`.t3c-bon`), la même
  caméra et la même trame.

### La typographie d'avant (« petit, sauf deux fois »)

- **Petit, sauf deux fois.** C'est le contraire du « très gros » habituel du studio : les phrases
  restent petites et posées, seuls les deux premiers mots (au tout début) et le prix sont énormes.

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Les deux mots géants de l'ouverture | ~80 % de la largeur (calculé) | ~80 % de la largeur |
| La phrase d'accroche (après le recul) | 60 px, finit vers 40 px | 60 px |
| Les onglets à l'écran | 75 à 120 px (46 px × zoom 1,6 à 2,6) | 50 à 100 px (la barre au plus ×0,85, la pastille de l'offre tient dans la largeur) |
| « Découvre Ton offre », l'appel | 58 à 64 px | 58 à 64 px |
| Le bon : libellés / prix / bouton | 30 / 112 / 38 px, × 1,2 à 1,45 par la caméra | mêmes tailles, × 1 à 1,2 |
| Les cartes : nom / chiffre / bouton | 62 / 58 / 44 px, × 1,4 à 1,6 | 62 / 170 / 44 px (carte en portrait), × 0,85 à 0,96 |
| Le nom de la marque à la fin | 76 px | 76 px |

### Le bon piloté d'avant (paliers et bandes floues)

4. **Le bon piloté** (`t3-commande`, 7,2 s) : il entre de profil (pivot de 87° à 0° en 0,8 s,
   power4.inOut) depuis une lame blanche et floue, qui se retire d'un balayage (0,45 s) ; caméra
   inclinée (22° en X, −10° → −5° en Y, −3° en Z) qui descend le bon par paliers de 0,7 s
   (power3.inOut) ; flou de profondeur en bandes en haut et en bas de l'image (6 px) ; le curseur
   glisse en 0,95 s (power2.inOut), clique (0,07 s d'enfoncement), l'interrupteur bascule et se
   remplit par un volet (0,28 s), les champs tombent (back.out(1.8), 0,09 s d'écart), les
   compteurs tournent (expo.out, 0,7 à 0,9 s).

### Le vertical, essai daté

- **9:16 (les quatre scènes essayées bout à bout, marque LMDM, 06/11/2026) :** passe la racine de la
  scène à 1080 × 1920 ; tout se recadre seul (K.cadre) : la barre d'onglets aussi grande que
  possible (au plus ×0,85, tant que la pastille de l'offre tient dans la largeur au plus près : un
  nom long la rend plus petite), la pastille qui couvre l'écran plus loin (elle grandit jusqu'à la
  hauteur), le bon moins rapproché (×1,02) et
  suivi plus haut dans l'image (le point visé à 37 % de la hauteur) pour qu'il remplisse le haut,
  puis le bouton posé à 60 % de la hauteur pour le clic ; ses bandes floues sont plus fines (24 %
  en haut, 16 % en bas). Il occupe presque toute la largeur, c'est le format où il est le plus
  lisible.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit (index, « Appliquer
un style », point 6) et que l'IA copie surtout le code des scènes. Fiche : 30 057 octets avant,
20 653 après.

**La fiche (`style.md`)**
- Sortis vers cette note : les mesures de l'original et de l'essai, l'original scène par scène,
  « Ce qui ne se fera pas à l'identique » (ses leçons restent en sections 3, 5 et 7, au présent),
  la colonne « Dans l'original » des couleurs, les dates, la marque d'essai.
- Retirés car l'index les dit : la citation « On reprend la grammaire… », l'ouverture de la
  section 2, « Sur n'importe quelle marque, claire ou sombre ».
- Lien `../../references/style.md` → `../../references/image.md` (« La palette »).
- La typographie « petit, sauf deux fois » devient « grand et posé » : une phrase seule à la
  moitié de la largeur au moins, un mot héros à 60 % (85 % en 9:16) ; le tableau suit les tailles
  que les scènes calculent. Raison : la loi du cadre (sujet à 40 % au moins, jamais un petit
  élément au milieu du vide) ; la promesse finissait à 38 px au milieu d'un cadre vide.
- Le verre piloté : trois cadrages, un par partie, au lieu de paliers de 0,7 s qui se suivaient
  (4 pas de caméra en 4 s, dont deux collés à 4,35 s et 5,15 s, sous les textes du bon) ; plus de
  bande floue de profondeur de champ (le bon passait son accent dans le flou à chaque cadrage).
- Le carrousel : la rafale devient de la texture, la dernière carte se lit ; chaque carte ne porte
  plus que son chiffre (dans la tuile de l'accent) et son nom.
- « Le flou et l'accent » au présent, complété des réglages des scènes refaites ; plus de halo ni
  de lueur sur le texte (`image.md` : « jamais une lueur », halos interdits).
- « Les compositions du kit » : l'objet `EXEMPLE` et ses champs, les nouvelles durées
  (`t3-commande` 9 s, `t3-cartes` calculée, 6,2 s).

**Les scènes**
- Toutes : l'objet `R` fondu dans `var EXEMPLE = { … }; // À REMPLACER…`, en-têtes « À remplacer :
  l'objet EXEMPLE » ; plus de halo (`t3o-halo`, `t3o-bande`, `t3f-halo`, `t3f-eclat`,
  `t3c-eclat`) ni de lueur sur le texte ou le logo ; textes à lire immobiles pendant leur
  lecture (la trame et la lumière dérivent derrière) ; l'accent n'entre ni ne sort plus en fondu
  ou en flou.
- `t3-onglets` : la promesse finit à 52 % de la largeur (84 % sur deux lignes en 9:16) au lieu de
  ×0,64 (22 %) ; sa fin entre par des volets au lieu d'un flou ; l'appel final calculé à 62 % de
  la largeur (85 % en 9:16) ; la pastille de sélection apparaît sans fondu, vide (plus de voile
  blanc) ; le nom sous la pastille pleine s'éteint pendant qu'elle le couvre (contraste 1:1 relevé
  par `check`) ; les onglets qui filent sont de la texture ; plus d'étoile de secours pour l'icône
  du premier onglet ; une capture qui manque retire sa carte.
- `t3-commande` : trois cadrages (2,4 s et 6 s) au lieu de quatre paliers ; 9 s au lieu de 7,2 s ;
  plus de bandes floues ; le sélecteur de paiement cerclé de l'accent (la pastille pleine qui
  glissait sous un libellé foncé faisait échouer le contraste à mi-course) ; les gris en dur de
  secours (`#111111`, `#999999`) remplacés par `K.jeton` ; les surfaces blanches en transparence
  (puces, piste, valeur, interrupteur) en `--brand-gris-1`, la lame et les billes en
  `--brand-clair` ; prix d'exemple rond (300 €, bonus 30 €) ; libellés à 30-32 px ; menu, accès et
  mention en texture (`data-layout-ignore`) ; le sélecteur, les icônes des puces et les champs du
  bonus n'entrent plus en fondu ; les points du bouton se retirent par un volet. L'audit citait un
  `#202022` en dur : il n'était pas dans la scène du catalogue (seulement dans le `tokens.css` du
  banc) ; les seules couleurs en dur étaient ces deux gris de secours.
- `t3-cartes` : chaque carte réduite à son chiffre (dans la tuile) et à son nom, au lieu d'une
  dizaine de mots (sous-titre, trois lignes, bouton, durée) tenus 0,5 s ; la rafale en texture,
  la dernière carte posée en entier et tenue le temps de sa lecture ; plus d'étoile de secours ni
  d'icône générique dans la tuile (un chiffre absent retire la tuile) ; plus de « 12 vidéos » ni de
  « 24/7 » en dur ; le mot à 60 % de la largeur (85 % en 9:16), sa pastille s'ouvre par un volet ;
  durée calculée (6,2 s).
- `t3-fin` : la ligne et l'adresse à 50 % de la largeur au moins (80 % en 9:16), le logo et le nom
  à 60 % (80 %) ; le verbe passe au clair d'un coup (son fondu de couleur passait par un jaune
  pâle) ; l'impact sur l'adresse devient un trait plein de l'accent tiré dessous, sa fin prenant
  l'accent d'un coup ; le logo s'ouvre par un volet rond au lieu d'un flou ; logo d'exemple
  `brand/logo.png` (le banc n'a pas de `logo.svg` : erreur 404 au `check`).

**Vérifié** sur le banc « Banc styles 03 » (Page de vente 1920 × 1080 et Reel 1080 × 1920) : les
quatre scènes montées bout à bout, `check` sans erreur ni avertissement en 16:9 comme en 9:16 (hors
« film sans son ») ; planches regardées à chaque lecture, recadrage et fin.
