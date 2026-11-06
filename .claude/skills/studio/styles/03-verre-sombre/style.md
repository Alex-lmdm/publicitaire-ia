# Style n°3 · Verre sombre · d'après Polymarket (https://x.com/Polymarket/status/2095530373274816595)

**Ce qu'on voit :** une vidéo de nuit, dans la couleur la plus sombre de la marque, à peine
éclairée par une lueur blanche ; de petites phrases nettes, un mot à l'accent, et surtout une
interface en verre sombre inclinée en 3D que la caméra descend pendant qu'un curseur la pilote (un
curseur qu'on glisse, un interrupteur, un total qui change, un bouton qu'on clique et qui se défait
en points). L'accent se pose toujours plein : un trait, un remplissage, un bouton, un éclair.
**Souvent utile pour :** présenter une offre et son prix, une page de paiement, un logiciel qu'on
pilote ; lancer une nouvelle formule.

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

> On reprend la grammaire de la vidéo (rythme, mise en page, verre, caméra, trame de points,
> transitions), jamais son contenu : ni ses textes, ni son logo, ni ses marchés, ni ses chiffres, ni
> sa musique, ni sa nuit bleue. Tout passe aux seules couleurs et à la police de la marque du client.

## 1. Le rythme

- **Peu de coupes, beaucoup de gestes.** Deux coupes franches en 37 s : le rythme vient de la
  caméra (recul, glissé, plongée), des mises au point et des gestes dans l'interface. Un geste
  toutes les 0,3 à 0,5 s pendant la démonstration (le prix tourne, une pastille s'allume, le curseur
  glisse, l'interrupteur bascule, un champ tombe).
- **Une ouverture lente, puis tout s'accélère** : 7 s d'accroche presque silencieuse (la phrase,
  les onglets), entrée franche de la musique sur le nom, puis la démonstration dense, puis un
  carrousel très rapide (une carte toutes les 0,5 s).
- **Une fin qui respire** : la musique se coupe, une ligne seule, l'adresse avec un seul impact, le
  logo tenu 3 à 4 s. C'est la seule tenue longue autorisée.
- **Chez toi :** grille de 0,5 s (120 par minute). Chaque phrase se tient le temps de sa lecture
  (`studio_motion.py lecture` : 0,3 s par mot + 0,8 s, 2 s au moins pour l'accroche) et les scènes
  en déduisent leur durée. Pendant une lecture, la caméra ne fait qu'une dérive lente (3 à 5 %,
  sine.inOut) : sur cette nuit presque nue, la vie vient de ce que la phrase montre, ses vraies
  captures en verre qui arrivent de la profondeur une à une (autour de l'accroche, sous l'appel),
  le nom qui se remplit de l'accent dans sa pastille. Sans capture, une tenue de nuit est une image
  figée pour `rythme` : c'est le repérage qui manque de matière, jamais un recadrage à ajouter
  (essai du 06/11/2026 : le recadrage sec ajouté sous l'accroche est retiré).

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| La mise au point et le recul | deux mots géants, flous, deviennent nets ; la caméra recule, la phrase finit petite avec sa fin à l'accent, puis se tient pendant que ses vraies captures arrivent autour d'elle | accroche, promesse | `t3-onglets` (début) |
| La barre filée et la pastille fixe | une barre d'onglets défile sous une pastille cerclée de l'accent qui reste au centre et se pose sur l'offre | le choix (le problème), la solution qui ressort | `t3-onglets` |
| La plongée et la trame de points | la pastille se remplit de l'accent, on la traverse (un éclair de la couleur pleine) ; un texte se forme en points puis devient net | passage, le nom de l'offre | `t3-onglets` (fin), `t3-cartes` |
| Le verre piloté | une interface en verre sombre, inclinée en 3D, que la caméra descend par paliers pendant qu'un curseur la règle ; pour un prix, c'est sa vraie page de paiement, simplifiée | démonstration de son interface, l'offre et son prix | `t3-commande` |
| Le carrousel en gros plan | un mot seul, puis une carte inclinée toutes les 0,5 s | ce qu'on reçoit, preuves chiffrées | `t3-cartes` |
| La fin en silence | le verbe seul dans le silence, la ligne complète, l'adresse qui brille, le logo et le nom | appel, fin | `t3-fin` |

**Pour montrer une fonctionnalité** de son offre : le cycle interface, option, preuve, dans le
même verre incliné (section « Des enchaînements qui marchent »).

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

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

Pour un Reel : `t3-onglets` (raccourci à la plongée) → `t3-commande` → `t3-fin`.

**Une vidéo de page (16:9, 60 à 120 s) :** les quatre scènes du kit bout à bout ne font que
33 s, et une vidéo de page montée avec elles seules sort à 33 s, loin de la cible. La durée
vient de la démonstration, jamais de tenues plus longues : entre `t3-onglets` et `t3-cartes`,
refais le cycle **interface, option, preuve** pour 2 ou 3 fonctionnalités réelles de l'offre (15 à
20 s par cycle) :
1. **L'interface** : un écran réel de la fonctionnalité dans le même verre incliné, la même caméra
   qui descend par paliers et le curseur qui le pilote (copie de `t3-commande` avec ses vrais
   champs, ou une capture dans le verre) ;
2. **L'option** : le réglage qui change le résultat (un curseur glissé, un interrupteur, une
   formule choisie), le total ou le résultat qui se met à jour ;
3. **La preuve** : une carte de `t3-cartes` en gros plan avec le vrai chiffre, ou une ligne mot à
   mot sur la trame de points.

Trois cycles donnent 70 à 85 s avec l'ouverture et la fin ; ajoute le plein écran de l'accent sur
le prix (section 3) au-delà d'une minute. Chaque copie de scène change son préfixe partout (`t3c`
→ `t3c2`, `t3c3`). S'il manque une fonctionnalité réelle pour un troisième cycle, la vidéo reste
plus courte : on n'invente rien pour tenir la durée.

## 3. Les fonds et les couleurs

Les couleurs sont celles de la marque, rien d'autre ([../../references/style.md](../../references/style.md),
« La palette ») : sa couleur la plus sombre pour la nuit, sa plus claire pour le texte, ses gris,
du noir et du blanc en transparence, et l'accent posé plein.

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

Ce look reste de nuit du début à la fin : pas d'alternance sombre et clair. Les « bascules » de
fond se font par la lumière : la lueur blanche qui glisse, la trame qui s'allume, l'éclair de
l'accent quand on traverse le bouton, l'éclat blanc du clic. Une vidéo de plus d'une minute ajoute
un plein écran de la couleur d'accent sur le prix (recette 19) pour garder trois bascules par
minute.

**Sur n'importe quelle marque, claire ou sombre.** La nuit, le texte et les gris viennent des jetons
de la palette (`--brand-sombre`, `--brand-clair`, `--brand-gris-1` à `--brand-gris-4`), jamais de
`var(--brand-bg)`, `var(--brand-text)` ni `var(--brand-muted)` (sur une marque claire, son fond est
clair et la nuit deviendrait un gris moyen). L'accent ne se dérive jamais : ni mélangé à une autre
couleur, ni éclairci ou assombri par le calcul, ni halo, ni lueur, ni dégradé, ni accent en
transparence comme état de repos (un jaune à demi transparent sur la nuit devient olive ou brun ;
story refusée du 06/11/2026). Un voile
ou une vignette ne passe jamais au-dessus de l'accent : la vignette est posée sous le sujet, et la
profondeur de champ ne garde pas de voile sombre. Tout texte garde un contraste d'au moins 4,5:1 :
un accent trop sombre pour se lire sur la nuit cède sa place à `--brand-accent-lisible`.

**Le flou et l'accent.** Un bouton ou une pastille à l'accent qui passe dans un flou mêle son jaune
et son texte foncé à la nuit : `palette` relève ces images. D'où les réglages du kit, à garder : des
bandes de profondeur de champ courtes et douces (6 px), des cartes qui glissent sans flou, un bon qui
recule sans s'effacer (la coupe le fait disparaître), une lame claire qui se retire par un balayage
et non par un fondu, une liste qui s'estompe écrite en clair (seule sa ligne pleine, au milieu,
prend l'accent). Mesure-le sur le rendu de chaque vidéo.

## 4. La typographie

- **Police :** une seule, sans empattement neutre, demi-grasse partout (600), moyenne (500) pour
  l'adresse. La marque n'impose rien : **Inter** (libre, déjà livrée avec le kit pour les
  interfaces). Dans le kit : `var(--brand-font-body)` (variable `--t3-police` de chaque scène).
- **Casse et alignement :** casse de la phrase, jamais de capitales ; lignes centrées ; interfaces
  alignées à gauche, chiffres à droite. Une lueur blanche très douce sur le texte (ombre de 26 px à
  22 %).
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

## 5. Les mouvements signature

1. **La mise au point et le recul** (`t3-onglets`, 0 → 2,25 s, puis la tenue) : les deux mots
   géants, flous de 16 px, deviennent nets en 0,45 s (power2.out), en `--brand-clair` ; la caméra
   recule de ×4,6 à ×1 en 0,75 s (expo.inOut) et la ligne se recentre ; la fin de phrase entre mot
   à mot (0,3 s d'écart au plus, flou 12 px → 0) pendant un dernier recul jusqu'à ×0,64 (×0,86 au
   plus en 9:16, pour qu'elle se lise sur un téléphone) : c'est l'apparition de l'accroche. Puis
   elle se tient le temps de sa lecture : dérive de 3 % (sine.inOut), la trame et la lueur
   s'allument derrière elle, ses vraies captures (`R.captures`, 2 ou 3) arrivent de la profondeur
   dans le verre du look, une toutes les 0,6 s, à gauche, à droite et en haut (au-dessus et
   au-dessous en 9:16), jamais sur la phrase, et repartent avec elle. Aucun recadrage sec.
2. **La barre filée et la pastille fixe** (`t3-onglets`, une fois l'accroche lue) : le premier onglet seul, les
   suivants à 0,17 s d'écart ; toute la barre défile en 1 s (power3.inOut) avec un flou de vitesse
   horizontal (0 → 18 px → 0) et un zoom ×1,6 → ×2 ; la pastille, cerclée d'un trait plein de
   l'accent, reste au centre, les onglets passent dessous, et elle se pose sur l'offre.
3. **La plongée dans le bouton** (`t3-onglets`, 5,6 → 7 s) : zoom ×2 → ×2,6 en 0,85 s (expo.out),
   la trame de points et une lueur blanche s'allument derrière, un reflet glisse sur l'arête haute
   (0,7 s) ; la pastille se remplit de l'accent par un volet de gauche à droite (0,26 s,
   power3.inOut), le nom passe en `--brand-contrast` ; puis on la traverse : elle grandit jusqu'à
   couvrir tout l'écran (0,38 s, power3.in), un éclair de la couleur pleine de deux ou trois
   images, et coupe sur la nuit. « Découvre Ton offre » se forme en points et se tient le temps
   de sa lecture ; au milieu de la tenue, le nom se remplit de l'accent dans sa pastille cerclée
   (un volet, le mot clé surligné d'un bloc plein), qui se vide par un volet avant la sortie.
4. **Le bon piloté** (`t3-commande`, 7,2 s) : il entre de profil (pivot de 87° à 0° en 0,8 s,
   power4.inOut) depuis une lame blanche et floue, qui se retire d'un balayage (0,45 s) ; caméra
   inclinée (22° en X, −10° → −5° en Y, −3° en Z) qui descend le bon par paliers de 0,7 s
   (power3.inOut) ; flou de profondeur en bandes en haut et en bas de l'image (6 px) ; le curseur
   glisse en 0,95 s (power2.inOut), clique (0,07 s d'enfoncement), l'interrupteur bascule et se
   remplit par un volet (0,28 s), les champs tombent (back.out(1.8), 0,09 s d'écart), les
   compteurs tournent (expo.out, 0,7 à 0,9 s).
5. **La trame de points** (`t3-onglets` à 7 s, `t3-commande` à 6,3 s, `t3-cartes`) : le texte se
   forme d'abord en points blancs (étiré de 25 %, avec un écho flou deux fois plus grand qui se
   résorbe en 0,7 s), le texte plein prend le relais 0,3 s après ; à l'inverse, le bouton cliqué
   s'ouvre d'un trou qui part du clic (0,36 s) et ne laisse que ses points, pleins et à l'accent,
   qui montent de 30 px et s'effacent (0,5 s) pendant que le bon recule.
6. **Le carrousel en gros plan** (`t3-cartes`) : le mot seul se tient 2 s dans la pastille qui se
   remplit (sa lecture), puis une carte toutes les 0,5 s, chacune avec son angle
   (16 à 24° en X, ±20 à 26° en Y), entrée glissée de 360 px en 0,3 s (expo.out, sans flou), coupe
   nette à la suivante ; arête haute éclairée ; les lignes montent une à une (0,07 s d'écart) ; la
   dernière file hors champ jusqu'à la coupe. Le carrousel est une rafale : une carte se voit d'un
   coup d'œil (son nom, son chiffre), elle ne se lit pas ; ce qu'il faut lire se dit dans le mot
   ou la phrase qui l'annonce, tenus le temps de leur lecture.

## 6. Les transitions

- **Dans l'original :** presque pas de coupe. On passe d'une idée à l'autre par la mise au point
  (flou → net), par la plongée à travers un objet (le bouton), par une lame claire (l'interface vue
  de profil qui pivote), par la dissolution en points, par un fondu flou entre deux lignes courtes.
  Une seule coupe franche, posée sur le silence avant l'appel.
- **Dans le kit :** la plongée traverse le bouton plein : l'accent couvre l'écran, coupe sur la
  nuit où le nom se forme en points. `t3-onglets` finit sur la ligne qui se dissout dans le flou ;
  `t3-commande` commence par la lame claire qui pivote. `t3-commande` finit par le bouton qui se
  défait en points et le bon qui recule ; `t3-cartes` commence sur un mot seul. `t3-cartes` →
  `t3-fin` : la coupe franche, sur un silence de la musique. Les fondus flous ne touchent que du
  blanc et du gris (un texte, la lueur, la trame), jamais une grande surface de l'accent.

## 7. Le produit à l'écran

- **Dans l'original :** le produit est l'interface elle-même, montrée de quatre façons : en entier
  et inclinée, une carte, le bon de commande en gros plan piloté par le curseur, les couches
  éclatées. Toujours la vraie interface, simplifiée, en thème sombre, avec de gros chiffres.
- **Chez toi :** le bon de commande suit **sa vraie page de paiement** (sa capture en est la source),
  simplifiée : ses formules, son prix, ses façons de payer, le paiement en plusieurs fois s'il
  existe, son option ou son bonus s'il en a un, le total, son bouton. Les cartes montrent ce qu'on
  reçoit vraiment (modules, bonus, fonctions) avec leurs vrais chiffres. Un logiciel : sa vraie
  interface va dans le même verre, avec la même caméra. Jamais de champ, de réduction ni de prix
  barré inventés ; une ligne qui n'existe pas chez lui se retire. Aucune illustration : ce style ne
  montre que son interface et sa typographie.
- **Le curseur :** la flèche du kit (pleine et sombre, contour blanc), posée dans le plan du bon :
  elle s'incline avec lui.

## 8. Le son

- **Dans l'original :** une nappe électronique sombre et feutrée, vers 93 par minute. Les 7
  premières secondes restent basses (des impacts sourds sur les reculs de caméra), l'entrée franche
  tombe sur le nom (7,0 s), une pulsation régulière porte la démonstration, puis la musique se coupe
  net (28,5 s) : la ligne d'appel passe dans le silence, une montée courte amène **un seul impact**
  sur l'adresse (30,5 s), et le logo finit en silence.
- **Chez toi :** ambiance « Tech minimale » (ou « Montée cinématique » pour une révélation),
  entrée calée sur le nom (`musiques prendre … --a <instant du nom>`). Bruitages, un par geste :
  souffle doux sur le recul, souffle filé sur le défilement des onglets, petit clic sur la pastille,
  scintillement numérique sur le texte en points, clics d'interface (curseur, interrupteur,
  bouton), cliquetis de compteur sur le prix, éparpillement sur la dissolution, un souffle par
  carte. Coupe la musique 1 à 2 s avant l'adresse (`son` et `mastering` ensuite) et garde l'impact
  pour l'adresse seulement.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 3`) : « Tech minimale » puis « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** deux mots géants et flous, qui deviennent nets, puis la caméra
  recule d'un coup : la promesse complète, petite, sa fin à l'accent. Lisible dès la première image
  (les mots sont énormes), même floue.
- **La fin :** coupe franche dans le silence sur le verbe d'appel seul, en couleur ; la ligne se
  complète et se tient le temps de sa lecture pendant que sa vraie page monte de la profondeur
  dans le verre incliné, sous elle, et se redresse ; elle se change dans un flou en l'adresse de sa
  page, qui brille et se tient le temps de sa lecture (une seconde capture de la page glisse dans
  le verre) ; puis son logo et son nom, tenus 3 s (l'écran final). En page de vente, l'adresse
  peut devenir le texte du bouton situé sous la vidéo.

## Ce qui ne se fera pas à l'identique

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

## Sur une autre offre

C'est un look : il se monte sur n'importe quelle offre. Ce qui suivait le trading s'adapte.

- **Formation :** onglets = les sujets de son univers (ceux de sa page) ; bon = formule, prix,
  paiement en plusieurs fois, bonus ; cartes = les modules et les bonus avec leur nombre de vidéos ;
  le curseur glissé = le nombre de paiements.
- **Coaching :** onglets = les problèmes qu'il traite ; bon = la formule (nombre de séances), le prix,
  l'option (un appel de plus) ; cartes = les étapes de l'accompagnement ; le curseur glissé = le
  nombre de séances, si sa page le propose.
- **Logiciel :** onglets = les fonctions ou les métiers ; le bon devient sa vraie interface (le verre
  garde la même caméra), le curseur glissé = un réglage réel (crédits, utilisateurs, formule) ;
  cartes = les fonctions ou les intégrations, avec le logo de l'outil (`studio_motion.py logos`)
  dans la tuile.
- **Toujours :** la nuit de la marque, la petite phrase avec la fin en couleur, la pastille fixe sous
  les onglets, la plongée, la trame de points, le verre incliné piloté par le curseur, la fin en
  silence.

## En vertical et en carré

- **9:16 (les quatre scènes essayées bout à bout, marque LMDM, 06/11/2026) :** passe la racine de la
  scène à 1080 × 1920 ; tout se recadre seul (K.cadre) : la barre d'onglets aussi grande que
  possible (au plus ×0,85, tant que la pastille de l'offre tient dans la largeur au plus près : un
  nom long la rend plus petite), la pastille qui couvre l'écran plus loin (elle grandit jusqu'à la
  hauteur), le bon moins rapproché (×1,02) et
  suivi plus haut dans l'image (le point visé à 37 % de la hauteur) pour qu'il remplisse le haut,
  puis le bouton posé à 60 % de la hauteur pour le clic ; ses bandes floues sont plus fines (24 %
  en haut, 16 % en bas). Il occupe presque toute la largeur, c'est le format où il est le plus
  lisible.
- **9:16, `t3-cartes` et `t3-fin` :** les cartes passent en portrait (940 × 1 000 : le chiffre en
  grand sous le nom, la liste plus grande, le bouton en bas), à ×0,85 à 0,96 et moins inclinées en
  Y : la carte entière tient dans la zone de texte d'un Reel (y de 300 à 1 440). La fin est
  centrée ; avec sa capture, les textes montent au tiers haut et sa page se pose dessous, dans
  le verre incliné ; une ligne trop longue (une adresse) se réduit seule à 88 % de la largeur.
- **9:16, l'accroche :** la phrase finit à ×0,86 au plus (au lieu de ×0,64) pour se lire sur un
  téléphone ; ses captures se posent au-dessus et au-dessous d'elle, une image large prend
  jusqu'à 60 % de la largeur.
- **4:5 et 1:1 :** même règle (racine à 1080 × 1350 ou 1080 × 1080) ; garde le bon en entier en
  largeur, et vérifie le cadrage du carrousel (cartes coupées à droite et en bas, jamais en haut).

## Les compositions du kit

Chaque scène est une sous-composition 16:9 prête à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Tout ce qui change d'une
offre à l'autre est dans l'objet `R` en tête du script ; les couleurs ne viennent que des jetons de
la palette (`var(--brand-sombre)`, `var(--brand-clair)`, `var(--brand-gris-*)`, l'accent plein),
avec du blanc et du noir en transparence.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (objet `R`) |
|---|---|---|---|
| `compositions/t3-onglets.html` | 7,2 s + la lecture de la promesse + celle de « Découvre Ton offre » (11,2 s pour 5 et 3 mots, 11,5 s pour 6 et 3 ; la scène la calcule) | la promesse floue → nette et le recul, tenue le temps de sa lecture pendant que ses vraies captures arrivent autour d'elle ; la barre d'onglets filée sous la pastille fixe cerclée de l'accent ; la pastille qui se remplit et la plongée (l'éclair de l'accent) ; « Découvre Ton offre » qui se forme en points et se tient, son nom qui se remplit de l'accent | la promesse (2 morceaux, 8 mots au plus : une ligne), les onglets (les sujets de son univers ; l'offre doit en faire partie), le nom de l'offre, le verbe d'appel, l'icône du premier onglet, ses vraies captures (2 ou 3 : ses vidéos, sa page, un résultat) |
| `compositions/t3-commande.html` | 7,2 s | le bon de commande en verre incliné, d'après sa vraie page de paiement : entrée de profil, prix qui tourne, pastilles de ce qui est inclus, curseur du nombre de paiements, interrupteur du bonus, total, bouton cliqué qui se défait en points | formules, menu, libellés de paiement, nom, accès, prix réel, ce qui est inclus (icône du kit + mot), nombre de paiements possible (1 = retire le curseur), bonus (0 = retire la ligne), texte du bouton, mention |
| `compositions/t3-cartes.html` | 5,1 s | un mot seul tenu 2 s dans sa pastille qui se remplit, puis cinq cartes en gros plan incliné, une toutes les 0,5 s | le mot ; pour chaque carte : l'icône du kit ou le logo d'un outil, le nom, le sous-titre, le vrai chiffre et son unité, trois lignes réelles, la durée ("" pour la retirer). La durée de la scène suit le nombre de cartes (2 s pour le mot, 0,5 s par carte, + 0,6 s) |
| `compositions/t3-fin.html` | 9,2 s (ligne de 4 mots, logo ; la scène la calcule) | le verbe d'appel seul, la ligne complète tenue le temps de sa lecture sur la lueur et la trame, sa vraie page dans le verre incliné sous elle, l'adresse qui brille et se tient, le logo et le nom tenus 3 s | le verbe, la suite de la ligne, l'adresse réelle (courte, sans https://), sa capture (la page où mène l'adresse, ou deux captures de cette page ; "" : la tenue ne vit que de la lumière et `rythme` la verra figée), le logo (`brand/logo.svg`, "" sans logo), le nom |

`t3-onglets` et `t3-fin` tiennent chaque phrase le temps de sa lecture et calculent leur durée
(`D` dans le script) : reporte-la dans `data-duration`, ici et sur l'hôte dans `index.html`. Une
phrase du script plus longue que ce qu'une mise en page prend ne se raccourcit jamais : elle passe
dans une scène construite dans le style (deux lignes, même verre, même dérive).

Les scènes `t3-onglets` et `t3-commande` attendent les polices avant de mesurer (onglets, lignes,
positions du curseur) : garde la construction dans `construire()`. Identifiants préfixés `t3o`,
`t3c`, `t3k`, `t3f` : si tu montes deux fois la même scène, change le préfixe partout dans la
copie.
