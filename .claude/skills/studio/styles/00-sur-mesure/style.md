# Style n°0 · Sur mesure · le style maison

**Ce qu'on voit :** sa vraie matière en grand et en perspective, que la caméra parcourt ; peu de
mots, énormes, qui jouent ce qu'ils disent (ils claquent, se barrent, se surlignent, se changent
sur place) ; le point de sa couleur qui relie tout, d'un schéma qui se trace jusqu'au point final
de l'appel ; l'objet de son offre qui grandit et porte son nom ; des fonds qui changent avec une
cause (sa nuit à grille fine, son clair, l'aplat de son accent).
**Souvent utile pour :** tout, et d'abord sa première vidéo. C'est le style conseillé par défaut.
**D'après :** le langage des vidéos de lancement faites par des studios de motion design (relevé
notamment sur celles de Higgsfield), refait par nous : c'est lui que portent le kit et les scènes
prêtes.

**Pourquoi « sur mesure ».** Les styles 1 à 8 reprennent la grammaire d'une vidéo qui existe. Celui-ci
n'en copie aucune : chaque vidéo y prend sa forme à elle. L'objet de son offre (son dossier, son
carnet, sa carte de membre, l'icône de son app), l'enchaînement des scènes que son offre appelle
([scenes.md](../../references/scenes.md), « Combiner » : jamais le même film pour deux offres), le
fond qui domine et les gestes viennent de sa vidéo. Ce qui ne change pas d'une vidéo à l'autre, c'est
le niveau et quelques gestes qui font qu'on le reconnaît (section 2).

## 1. Le rythme

Celui de [mouvement.md](../../references/mouvement.md) (« Le rythme »), calé sur la bande-son
([son.md](../../references/son.md), « Construire l'image sur la bande-son »). Ce style y tient
surtout à deux choses : **des vitesses qui contrastent** (une rafale, puis une démonstration qui
tient son cadrage pendant que l'interface agit) et **une pause avant la révélation** (0,3 à
0,75 s), puis l'entrée franche.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le mot qui joue | un mot héros (1 à 3 mots) qui claque plein en se posant, s'étire, se barre, se surligne d'un bloc ou se change sur place, puis devient l'objet suivant | accroche, temps fort, toute idée clé | `K.claque`, `K.etire`, `K.surligner`, `k-heros` |
| La négation montrée | l'objet de l'ancienne façon (une caméra qui tourne, un tableur, un devis) barré par l'accent, éteint au gris, ses morceaux qui tombent ; puis un trait de l'accent fend l'écran en biais | le problème, ce qu'on remplace | `situation`, `K.barre`, `K.tranche` |
| Le nom sur l'objet | l'objet de son offre grandit depuis le clic sur l'aplat de sa couleur, son nom claque lettre par lettre, ce qu'il contient en jaillit puis retombe | le pivot, le nom | `nom-objet` |
| Le fil conducteur | le point de sa couleur parcourt les liens d'un schéma qui se trace, allume chaque nœud qui se coche, raye ce qu'on rejette, devient le point final de l'appel | le mécanisme, le motif qui revient | `schema`, `k-fil`, `K.longer` |
| La démo qui sort de la fenêtre | dans son interface reconstruite, le curseur agit, chaque étape se coche et son aperçu sort de la fenêtre pour flotter en 3D | comment ça marche | `demo` |
| Le travelling des étapes | ses étapes vraies posées sur une longue toile, la caméra glisse de station en station derrière le fil conducteur, puis recule pour tout voir | le parcours, ce qu'on reçoit | `parcours` |
| L'éventail et le grand chiffre | ses vraies captures en éventail, chacune avec son chiffre qui compte, puis le total énorme au centre sur le flou | la preuve | `preuve`, `messages` |
| L'écran coupé | un volet clair pousse la moitié de l'écran : l'ancienne façon et son chrono d'un côté, le résultat et son vrai délai de l'autre | comparer, un avant / après | `avant-apres` |
| Le prix qui claque | le prix en très grand sur l'aplat, ses modalités qui s'ouvrent dessous, puis la vraie échéance surlignée d'un bloc | l'offre et le prix | `prix` |
| La mosaïque qui devient le bouton | les images de la vidéo reviennent en mosaïque 3D, se resserrent en un bouton que le curseur clique, le nom au-dessus | la fin, l'appel | `fin` |

**Le garde-fou de ce style** : le mot qui joue est dans toute vidéo, le fil conducteur dans toute
vidéo de plus de 15 s, puis au moins un autre geste de la table (trois gestes en tout, deux sous
15 s). Le reste du film se construit avec les recettes de [scenes.md](../../references/scenes.md),
dans la même grammaire.

### Des enchaînements qui marchent

Des points de départ, jamais une obligation ; change l'enchaînement d'une offre à l'autre. Une vidéo
de page pour un logiciel : `situation` → `nom-objet` → `demo` → `avant-apres` → `preuve` → `prix` →
`fin`. Une formation : `preuve` → `nom-objet` → `parcours` → `messages` → `prix` → `fin`. Un
coaching : `situation` → (le titre qui se change sur place) → `parcours` → `preuve` → `prix` →
`fin`. Un Reel : trois à cinq scènes, par exemple `situation` → `nom-objet` → `schema` → `fin`.

## 3. Les fonds et les couleurs

Les couleurs de sa marque, plus les vraies couleurs des objets connus
([styles/README.md](../README.md), « La loi de toutes les scènes »), dans ces rôles :

| Rôle dans ce style | Avec la marque du client |
|---|---|
| La situation, le schéma, la démo, la preuve | la nuit à grille fine : `k-fond-sombre`, ou `var(--brand-sombre)` |
| Les étapes, l'écran coupé (côté résultat), les interfaces | le clair à grille : `k-fond-clair`, ou `var(--brand-clair)` |
| Le nom sur l'objet, le prix, un chapitre, un temps fort | l'aplat plein `var(--brand-accent)`, le texte posé dessus en `var(--brand-contrast)` |
| Le fil conducteur, la barre qui raye, le bloc qui surligne, le trait de la coupe | `var(--brand-accent)` plein |
| Le mot d'accent sur la nuit | `var(--brand-accent-lisible)` |
| Les mots d'appui, ce qui s'éteint | `var(--brand-gris-2)` à `var(--brand-gris-4)` |
| Les étiquettes de fonction | `k-blocs` : un bloc de l'accent, un bloc clair, un bloc sombre |

- Le fond change quand le film change de temps, avec une cause à l'écran
  ([image.md](../../references/image.md), « Les fonds et les objets ») ; celui qui domine suit sa
  marque : une marque claire prend plus de clair, une marque sombre plus de nuit.
- Sur l'aplat, rien n'entre en fondu, en flou ni avec une ombre sombre ([kit.md](../../references/kit.md),
  « Les pièges »).

## 4. La typographie

Celle de [image.md](../../references/image.md) (« La typographie » : trois tailles, le mot héros sur
60 à 90 % de la largeur), avec `var(--brand-font-display)` très grasse (800) et serrée (−3 à −4,5 %)
pour le mot héros et les titres, en deux tons (`k-titre`, `k-leger`, `k-accent`) ;
`var(--brand-font-body)` pour les étiquettes ; Inter pour ses interfaces reconstruites.

## 5. Les mouvements signature

La grammaire entière est dans [mouvement.md](../../references/mouvement.md) ; ce style en fait sa
signature :

1. **Le mot qui claque** (`K.claque`) : il arrive plein, d'un coup, à l'échelle 1,45, et se pose en
   rétrécissant ; jamais un fondu (sur l'aplat, il virerait à l'olive). Variantes dans une même
   vidéo : lettre par lettre pour un nom (`K.lettres`), mot par mot sortant d'un flou de 6 px, le mot
   qui défile comme une machine à sous avant de se poser.
2. **Le fil conducteur** (`K.lien`, `K.trace`, `K.longer`) : le trait se dessine et le point de sa
   couleur en est la pointe ; chaque nœud atteint reçoit un petit coup d'échelle et se coche.
3. **La caméra qui voyage entre les plans** (`k-scene3d` > `k-camera`) : elle s'approche du geste,
   plonge dans l'objet, recule sur le résultat (0,6 à 0,9 s, `expo.inOut`) ; pendant une lecture,
   seulement une dérive lente du monde derrière les mots.
4. **La profondeur** : trois plans (un premier plan flou qui passe, le sujet net, un fond qui vit),
   les vrais logos de ses outils en champ (`K.champ`, `K.logoNu`) quand la scène parle d'eux.
5. **Les arrivées en rafale** (`K.arrivee`) : ses captures, ses messages, ses étapes surgissent de
   la profondeur, 40 à 80 ms d'écart, une courbe longue (`expo.out`) et un léger dépassement sur un
   objet d'interface (`back.out(1.4)` à `back.out(2)`).

## 6. Les transitions

- **Un objet devient le suivant** : trois à cinq sortes par vidéo, chacune causée par quelque chose
  à l'écran ([mouvement.md](../../references/mouvement.md), « Les transitions »).
- **La coupe** (`K.tranche`) une ou deux fois par vidéo, sur un temps fort de la musique.

## 7. Le produit à l'écran

- Sa vraie matière, en descendant l'échelle de [image.md](../../references/image.md) (« La vraie
  matière »), et ce que son public reconnaît dans ses vraies couleurs (« Les objets connus ») : le
  dossier de `nom-objet` est le dossier bleu du Mac par défaut.
- Son produit : son interface reconstruite, de près, dans l'espace 3D du kit (une fenêtre, un
  téléphone) ; la caméra s'approche du geste (le champ où l'on tape, le bouton qu'on clique) puis
  recule sur le résultat.
- L'objet de son offre se choisit au début de la fabrication et revient : il grandit au pivot
  (`nom-objet`), devient le nœud du schéma, se pose dans l'outil que son public a déjà (scenes.md,
  recette 9), finit dans la mosaïque.

## 8. Le son

- **L'original :** des morceaux de lancement à la batterie marquée, un silence net avant la
  révélation, un bruitage par geste.
- **Chez toi :** ce style n'impose aucune ambiance : la musique suit le but et le support de la vidéo
  ([son.md](../../references/son.md), « Choisir le morceau »). Entrée franche sur le pivot (le nom
  sur l'objet, le résultat), une pause du morceau sur la pause qui précède la révélation, l'écran
  final sur le dernier temps fort ; avec une voix off, la batterie entre dans une respiration.
- **Bruitages, un par geste, jamais le même deux fois de suite** : un coup sec sur le mot qui claque,
  un souffle court quand le fil conducteur part, un petit clic par coche, un impact sur la coupe,
  un glissement sur le travelling, un pop par objet d'une rafale.

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** la situation qu'on reconnaît, déjà là sur la toute première image
  (l'objet de l'ancienne façon, sa vraie capture, ou la preuve d'abord), et un mot héros qui la
  ponctue ; lisible dès 0,5 s, sur une image stable.
- **La fin :** la mosaïque qui devient le bouton (`fin`), ou le produit qui se pose avec son nom et
  l'appel, le fil conducteur en point final. En pub, « Découvre-le » et une flèche vers le bas, sans
  dessiner de bouton (`fin`, mode flèche).

## Sur une autre offre

C'est le style fait pour toutes les offres : chaque vidéo y trouve sa forme.

- **Formation :** l'objet est son espace de formation ou son sommaire ; le travelling parcourt ses
  modules ; la preuve d'abord quand elle a de vrais résultats d'élèves.
- **Coaching :** l'objet est son accompagnement (l'agenda, le plan) ; le travelling suit les étapes
  réelles ; ses vrais messages en rafale.
- **Logiciel :** l'objet est l'icône de son app ; la démo dans son interface reconstruite porte la
  vidéo ; le schéma montre ce qui entre et ce qui sort.
- **Template, guide, communauté :** le document qui se remplit, les pages qui défilent ; les
  espaces et le rythme de la communauté, sans inventer de membres.

## Quand il décrit un autre style

Il décrit ce qu'il veut (« plus calme », « tout sur fond clair », « de la 3D partout », « une typo
énorme », « façon vieux papier ») : pars de ce style et applique ses mots, notés en une ligne dans
`PLAN.md` (« Style 0, ce qu'il a décrit : … »). Il répond « aucun » sans rien dire de plus : une
seule question à choix sur ce qu'il veut de différent (les lignes de la table, ou le lien d'une
vidéo qu'il aime), avec ta recommandation, puis la même chose.

| Il dit | Ce qui change |
|---|---|
| plus calme, plus premium | moins de rafales, des plans plus longs, des entrées douces (mot par mot sortant du flou), moins de bruitages |
| plus énergique, ça doit bouger | plus de rafales et de raccords d'objet, des plans plus courts entre les phrases, la coupe deux fois |
| fond clair, lumineux | le clair domine, la nuit seulement pour un temps fort |
| sombre, nuit | la nuit domine, l'aplat pour les temps forts |
| de la 3D, de la profondeur | la caméra voyage davantage, plus de plans en perspective et de champs de logos ; son ordinateur qui s'ouvre sur sa page, son téléphone qui pivote, en perspective (`K.ordinateur`, `k-tel`) |
| une typo énorme | le mot héros à 90 % de la largeur, une ligne d'appui de moins |

Ses mots changent les gestes, jamais les règles : la lecture, la palette, la vraie matière et le
cadre restent ceux de [styles/README.md](../README.md), « La loi de toutes les scènes ». Une
description qui suppose une image inventée (un paysage, des particules) ou une couleur hors de sa
marque se dit en une phrase, avec ce qu'on fera à la place. Il colle le lien d'une vidéo : c'est
`studio_motion.py reference`, pas cette section.

## En vertical et en carré

- **9:16 :** chaque scène prête lit `K.cadre` et se remet en page seule (1080 × 1920) : le sujet
  s'empile en hauteur et grandit, l'interface passe en carte verticale ou dans le téléphone, les mots
  empilés plus gros ([image.md](../../references/image.md), « Le cadre »). Tout texte dans la zone
  sûre du support (`studio_motion.py zones`).
- **4:5** prend la mise en page verticale ; **1:1** la mise en page 16:9 : vérifie la planche, un
  mot héros trop large passe à la ligne.

## Les compositions du kit

Les gestes de ce style sont les **scènes prêtes** de la racine du dossier (`templates/scenes/`,
depuis un projet : `../../../templates/scenes/`), nommées dans la colonne « Dans le kit » de la
section 2. Contrairement aux scènes des styles 1 à 8, elles se remplissent : copie la scène dans
`compositions/` du projet et remplis son objet `CONTENU` avec sa vraie matière ; leur mode d'emploi
et leurs durées sont dans `templates/scenes/README.md`. Une scène qu'elles n'ont pas se construit
avec une recette de [scenes.md](../../references/scenes.md) et les fonctions du kit
([kit.md](../../references/kit.md)). Le raccord entre deux scènes est à toi : la fin de l'une
devient le début de la suivante.
