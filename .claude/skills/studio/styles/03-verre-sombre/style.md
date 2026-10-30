# Template n°3 · Verre sombre · d'après Polymarket (https://x.com/Polymarket/status/2095530373274816595)

**Ce qu'on voit :** une vidéo de nuit, presque noire, éclairée par une lueur à la couleur de la
marque ; de petites phrases nettes, un mot en couleur, et surtout une interface en verre sombre
inclinée en 3D que la caméra descend pendant qu'un curseur la pilote (un curseur qu'on glisse, un
interrupteur, un total qui change, un bouton qu'on clique et qui se défait en points).
**Souvent utile pour :** présenter une offre et son prix, une page de paiement, un logiciel qu'on
pilote ; lancer une nouvelle formule.

**D'après :** X · Polymarket · « Perps » · 37 s · 16:9 (1920 × 1080, 24 images/s).
**Mesures de l'original (`studio_motion.py reference`) :** 1,92 événement par seconde, écart
médian 0,30 s entre deux événements, 2 coupes franches seulement (à 28,2 s), 7,0 s d'image figée au
total (surtout la fin : l'adresse et le logo tenus en silence). Musique à 93 battements par minute
(un temps toutes les 0,65 s), entrée franche à 7,0 s.
**Mesures de l'essai du kit** (4 scènes, marque LMDM, 23,7 s) : 1,34 événement par seconde, écart
médian 0,50 s, aucune image figée, `rythme` « ok ».

> On reprend la grammaire de la vidéo (rythme, mise en page, verre, caméra, trame de points,
> transitions), jamais son contenu : ni ses textes, ni son logo, ni ses marchés, ni ses chiffres, ni
> sa musique. Tout passe aux couleurs et à la police de la marque du client.

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
- **Chez toi :** grille de 0,5 s (120 par minute) ; le milieu ne garde jamais plus de 1 s sans geste
  (l'essai a ajouté un recadrage sec et une fin de phrase mot à mot pendant la tenue de l'accroche,
  là où l'original reste 2 s sur une phrase qui recule).

## 2. La structure

| Scène de l'original | Rôle | Durée | Ce qui s'y passe | Dans le kit |
|---|---|---|---|---|
| La promesse | accroche | 3,3 s | deux mots géants, flous, à la couleur d'accent, deviennent nets et blancs ; la caméra recule d'un coup, la phrase finit petite, sa fin en couleur | `t3-onglets` |
| Les onglets | problème (le choix) | 3,6 s | une barre d'onglets entre, défile très vite sous une pastille lumineuse fixe, qui se pose sur le produit ; on plonge dans ce bouton posé sur une trame de points | `t3-onglets` |
| Le nom | solution | 2,5 s | « Découvre … » se forme en points puis devient net, entrée franche de la musique | `t3-onglets` |
| L'interface entière | solution | 3,5 s | toute l'interface inclinée, la caméra glisse et se pose sur une carte | à refaire avec le verre du kit |
| Le bon de commande | démonstration et prix | 6,5 s | le bon pivote et entre ; montant, pastilles, curseur glissé, interrupteur, champs, total, bouton cliqué qui se défait en points | `t3-commande` |
| Le bénéfice | preuve | 1,6 s | une ligne mot à mot, une carte en points pivote entre deux mots | non construit |
| L'interface éclatée | preuve | 4 s | trois couches d'interface en 3D (graphique devant, listes derrière), le curseur clique | non construit |
| Le carrousel | offre | 2,6 s | un mot seul, puis une carte en gros plan toutes les 0,5 s | `t3-cartes` |
| L'appel | appel | 2,5 s | coupe franche dans le silence : le verbe seul, puis la ligne complète | `t3-fin` |
| L'adresse et le logo | appel | 6,5 s | l'adresse qui brille (un impact), puis le logo et le nom, tenus | `t3-fin` |

Pour une vidéo de page (60 à 90 s), enchaîne : `t3-onglets` → `t3-commande` → `t3-cartes` →
`t3-fin`, et place entre les deux premières une ou deux démonstrations de ton produit dans le même
verre (même caméra, même flou haut et bas). Pour un Reel : `t3-onglets` (raccourci à la plongée)
→ `t3-commande` → `t3-fin`.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Avec la marque du client |
|---|---|---|
| Bleu nuit presque noir | le fond de toute la vidéo | `--t3-nuit` : le fond de la marque assombri (38 % fond, 62 % noir) et teinté de 7 % d'accent. LMDM : noir chaud |
| Lueur bleue diffuse en haut à gauche, plus faible en bas à droite | la lumière de la scène, qui bouge doucement | l'accent éclairci (60 % accent, 40 % blanc) à 16 % ; LMDM : un halo doré très doux |
| Bleu vif | le mot de la fin de phrase, la pastille choisie, le bouton principal, le curseur rempli | `var(--brand-accent)` ; le texte posé dessus en `var(--brand-contrast)` |
| Verre sombre (liseré clair en haut, reflets blancs à 10-25 %) | les interfaces et les cartes | `--t3-verre` : le fond de la marque mêlé de noir ; les reflets restent blancs |
| Blanc, gris bleuté | textes, onglets inactifs, libellés | `var(--brand-text)` ; `var(--brand-muted)` légèrement teinté d'accent |
| Trame de points blancs | derrière le bouton, les cartes, et le texte qui se forme | identique (points blancs à 15-25 %) |
| Vert et rouge (hausse, baisse) | le sens propre au trading | non repris : dans un bon de commande, l'accent suffit |

Ce look reste de nuit du début à la fin : pas d'alternance sombre et clair. Les « bascules » de
fond se font par la lumière (la lueur qui glisse, la trame qui s'allume, l'éclat du clic, le gros
plan sur le bouton). Une vidéo de plus d'une minute ajoute un plein écran de la couleur d'accent sur
le prix (recette 19) pour garder trois bascules par minute. Avec une marque à l'accent clair (jaune,
vert pâle), le rendu devient noir et or plutôt que bleu nuit : c'est voulu.

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
| Les onglets à l'écran | 75 à 120 px (46 px × zoom 1,6 à 2,6) | 40 à 65 px |
| « Découvre Ton offre », l'appel | 58 à 64 px | 58 à 64 px |
| Le bon : libellés / prix / bouton | 30 / 112 / 38 px, × 1,2 à 1,45 par la caméra | mêmes tailles, × 1 à 1,2 |
| Les cartes : nom / chiffre / bouton | 62 / 58 / 44 px, × 1,4 à 1,6 | × 0,85 |
| Le nom de la marque à la fin | 76 px | 76 px |

## 5. Les mouvements signature

1. **La mise au point et le recul** (`t3-onglets`, 0 → 3,2 s) : les deux mots géants, flous de
   16 px et à la couleur d'accent, deviennent nets et blancs en 0,45 s (power2.out) ; la caméra
   recule de ×4,6 à ×1 en 0,75 s (expo.inOut) et la ligne se recentre ; la fin de phrase entre mot
   à mot (0,3 s d'écart, flou 12 px → 0) ; lent recul jusqu'à ×0,64 puis un recadrage sec (×0,78 en
   0,4 s, expo.out).
2. **La barre filée et la pastille fixe** (`t3-onglets`, 3,3 → 5,6 s) : le premier onglet seul, les
   suivants à 0,17 s d'écart ; toute la barre défile en 1 s (power3.inOut) avec un flou de vitesse
   horizontal (0 → 18 px → 0) et un zoom ×1,6 → ×2 ; la pastille lumineuse reste au centre, les
   onglets passent dessous, et elle se pose sur l'offre.
3. **La plongée dans le bouton** (`t3-onglets`, 5,6 → 7 s) : zoom ×2 → ×2,6 en 0,85 s (expo.out),
   la trame de points et le halo s'allument derrière, un reflet glisse sur l'arête haute (0,7 s),
   puis on traverse le bouton (×7, flou 18 px, 0,45 s, power3.in).
4. **Le bon piloté** (`t3-commande`, 7,2 s) : il entre de profil (pivot de 87° à 0° en 0,8 s,
   power4.inOut) depuis une lame claire et floue ; caméra inclinée (22° en X, −10° → −5° en Y, −3°
   en Z) qui descend le bon par paliers de 0,7 s (power3.inOut) ; flou de profondeur en bandes en
   haut et en bas de l'image (9 px) ; le curseur glisse en 0,95 s (power2.inOut), clique (0,07 s
   d'enfoncement), l'interrupteur bascule (0,28 s), les champs tombent (back.out(1.8), 0,09 s
   d'écart), les compteurs tournent (expo.out, 0,7 à 0,9 s).
5. **La trame de points** (`t3-onglets` à 7 s, `t3-commande` à 6,3 s, `t3-cartes`) : le texte se
   forme d'abord en points (étiré de 25 %, avec un écho flou deux fois plus grand qui se résorbe en
   0,7 s), le texte plein prend le relais 0,3 s après ; à l'inverse, le bouton cliqué se vide et ne
   laisse que ses points, qui montent de 30 px et s'effacent (0,6 s, power2.in).
6. **Le carrousel en gros plan** (`t3-cartes`) : une carte toutes les 0,5 s, chacune avec son angle
   (16 à 24° en X, ±20 à 26° en Y), entrée glissée de 360 px en 0,3 s (expo.out, flou 8 px → 0),
   coupe nette à la suivante ; arête haute éclairée ; les lignes montent une à une (0,07 s d'écart).

## 6. Les transitions

- **Dans l'original :** presque pas de coupe. On passe d'une idée à l'autre par la mise au point
  (flou → net), par la plongée à travers un objet (le bouton), par une lame claire (l'interface vue
  de profil qui pivote), par la dissolution en points, par un fondu flou entre deux lignes courtes.
  Une seule coupe franche, posée sur le silence avant l'appel.
- **Dans le kit :** `t3-onglets` finit sur la ligne qui se dissout dans le flou ; `t3-commande`
  commence par la lame claire qui pivote. `t3-commande` finit par le bouton qui se défait en points
  et le bon qui recule ; `t3-cartes` commence sur un mot seul. `t3-cartes` → `t3-fin` : la coupe
  franche, sur un silence de la musique.

## 7. Le produit à l'écran

- **Dans l'original :** le produit est l'interface elle-même, montrée de quatre façons : en entier
  et inclinée, une carte, le bon de commande en gros plan piloté par le curseur, les couches
  éclatées. Toujours la vraie interface, simplifiée, en thème sombre, avec de gros chiffres.
- **Chez toi :** le bon de commande est **sa vraie page de paiement**, simplifiée : ses formules, son
  prix, le paiement en plusieurs fois s'il existe, son option ou son bonus s'il en a un, le total,
  son bouton. Les cartes montrent ce qu'on reçoit vraiment (modules, bonus, fonctions) avec leurs
  vrais chiffres. Un logiciel : sa vraie interface va dans le même verre, avec la même caméra.
  Jamais de champ, de réduction ni de prix barré inventés ; une ligne qui n'existe pas chez lui se
  retire.
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

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** deux mots géants et flous à la couleur de la marque, qui deviennent
  nets et blancs, puis la caméra recule d'un coup : la promesse complète, petite, sa fin en couleur.
  Lisible dès la première image (les mots sont énormes), même floue.
- **La fin :** coupe franche dans le silence sur le verbe d'appel seul, en couleur ; la ligne se
  complète ; elle se change dans un flou en l'adresse de sa page, qui brille ; puis son logo et son
  nom, tenus 1,5 s ou plus. En page de vente, l'adresse peut devenir le texte du bouton situé sous
  la vidéo.

## Ce qui ne se fera pas à l'identique

- **La profondeur de champ optique** (flou réel selon la distance) → deux bandes floues fixes en haut
  et en bas de l'image : l'effet est le même tant que le bon est incliné, mais le flou ne suit pas
  un objet qui sortirait de la bande nette.
- **Le flou de mouvement** de chaque déplacement → un flou horizontal sur la barre d'onglets
  seulement ; les autres mouvements restent nets.
- **La lueur optique** (halo réel de la lumière sur le texte) → une ombre douce et blanche sous le
  texte.
- **Le bleu nuit** → la nuit de la marque : noir et or avec un accent jaune, bleu nuit seulement si
  l'accent est bleu.
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

- **9:16 (essayé sur `t3-onglets` et `t3-commande`) :** passe la racine de la scène à
  1080 × 1920 ; tout se recadre seul (K.cadre) : les onglets à ×0,55, le bon moins rapproché
  (×1,02) et suivi plus haut dans l'image (le point visé à 37 % de la hauteur) pour qu'il remplisse
  le haut ; il occupe presque toute la largeur, c'est le format où il est le plus lisible.
- **9:16, `t3-cartes` et `t3-fin` :** les cartes passent à ×0,85 et moins inclinées en Y ; la fin
  est centrée et ne bouge pas. Vérifie à l'image qu'un nom long tient (sinon baisse sa taille).
- **4:5 et 1:1 :** même règle (racine à 1080 × 1350 ou 1080 × 1080) ; garde le bon en entier en
  largeur, et vérifie le cadrage du carrousel (cartes coupées à droite et en bas, jamais en haut).

## Les compositions du kit

Chaque scène est une sous-composition 16:9 prête à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Tout ce qui change d'une
offre à l'autre est dans l'objet `R` en tête du script ; les couleurs ne viennent que de
`var(--brand-*)`.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (objet `R`) |
|---|---|---|---|
| `compositions/t3-onglets.html` | 8,2 s | la promesse floue → nette et le recul ; la barre d'onglets filée sous la pastille fixe ; la plongée dans le bouton sur la trame ; « Découvre Ton offre » qui se forme en points | la promesse (2 morceaux), les onglets (les sujets de son univers ; l'offre doit en faire partie), le nom de l'offre, le verbe d'appel, l'icône du premier onglet |
| `compositions/t3-commande.html` | 7,2 s | le bon de commande en verre incliné : entrée de profil, prix qui tourne, pastilles de ce qui est inclus, curseur du nombre de paiements, interrupteur du bonus, total, bouton cliqué qui se défait en points | formules, menu, libellés de paiement, nom, accès, prix réel, ce qui est inclus (icône du kit + mot), nombre de paiements possible (1 = retire le curseur), bonus (0 = retire la ligne), texte du bouton, mention |
| `compositions/t3-cartes.html` | 3,6 s | un mot seul, puis cinq cartes en gros plan incliné, une toutes les 0,5 s | le mot ; pour chaque carte : l'icône du kit ou le logo d'un outil, le nom, le sous-titre, le vrai chiffre et son unité, trois lignes réelles, la durée ("" pour la retirer). La durée de la scène suit le nombre de cartes (0,5 s chacune + 1,1 s) |
| `compositions/t3-fin.html` | 4,8 s | le verbe d'appel seul, la ligne complète, l'adresse qui brille, le logo et le nom | le verbe, la suite de la ligne, l'adresse réelle (courte, sans https://), le logo (`brand/logo.svg`, "" sans logo), le nom |

Les scènes `t3-onglets` et `t3-commande` attendent les polices avant de mesurer (onglets, lignes,
positions du curseur) : garde la construction dans `construire()`. Identifiants préfixés `t3o`,
`t3c`, `t3k`, `t3f` : si tu montes deux fois la même scène, change le préfixe partout dans la
copie.
