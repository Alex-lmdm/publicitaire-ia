# Style n°0 · Sur mesure · le style maison

**Ce qu'on voit :** sa vraie matière en grand et en perspective, que la caméra parcourt ; peu de
mots, énormes, qui jouent ce qu'ils disent (ils claquent, se barrent, se surlignent, se changent
sur place) ; le point de sa couleur qui relie tout, d'un schéma qui se trace jusqu'au point final
de l'appel ; l'objet de son offre qui grandit et porte son nom ; trois fonds qui se relaient avec
une cause (sa nuit à grille fine, son clair, l'aplat de son accent).
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

- **Des vitesses qui contrastent** ([mouvement.md](../../references/mouvement.md), « Le rythme ») :
  une rafale (une liste en cascade, des plans de 0,13 à 0,8 s), puis une démonstration qui tient le
  même cadrage 5 à 8 s pendant que l'interface agit ; des plans de 1,8 à 3 s en moyenne, jamais tous
  de la même durée.
- **Peu de mots, et ils jouent** : 20 à 30 mots en 30 à 40 s. Chaque groupe de mots tient sa
  lecture sans bouger (`studio_motion.py lecture`) ; la vie, pendant ce temps, vient de ce qu'il
  montre (l'interface qui répond, une coche, un compteur, une capture qui glisse).
- **Une pause avant la révélation** (0,3 à 0,75 s : le nom, le résultat, le prix), puis l'entrée
  franche.
- **Chez toi :** grille de 0,5 s ; chaque scène commence sur un temps (sa durée arrondie au temps
  suivant), les coupes et la révélation sur les repères du morceau ([son.md](../../references/son.md),
  « Construire l'image sur la bande-son ») ; avec une voix, les gestes suivent ses mots.

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
15 s). Et des objets connus dans leurs vraies couleurs : trois au moins au-delà de 15 s, un dans un
Reel ([image.md](../../references/image.md), « Les objets connus »). Le reste du film se construit avec les recettes de [scenes.md](../../references/scenes.md)
(28 recettes par rôle), dans la même grammaire.

**Pour montrer son produit** : son interface reconstruite, de près, dans l'espace 3D du kit (une
fenêtre, un téléphone) ; la caméra s'approche du geste (le champ où l'on tape, le bouton qu'on
clique) puis recule sur le résultat ([image.md](../../references/image.md), « La vraie matière »).

### Des enchaînements qui marchent

Des points de départ, jamais une obligation ; change l'enchaînement d'une offre à l'autre. Une vidéo
de page pour un logiciel : `situation` → `nom-objet` → `demo` → `avant-apres` → `preuve` → `prix` →
`fin`. Une formation : `preuve` → `nom-objet` → `parcours` → `messages` → `prix` → `fin`. Un
coaching : `situation` → (le titre qui se change sur place) → `parcours` → `preuve` → `prix` →
`fin`. Un Reel : trois à cinq scènes, par exemple `situation` → `nom-objet` → `schema` → `fin`.

## 3. Les fonds et les couleurs

**Les objets connus gardent leurs vraies couleurs**, dans ce style comme dans tous les autres : le
dossier bleu du Mac et les fichiers du kit (`K.ic("objet-…")`), le téléphone et sa barre d'état, la
notification et les bulles d'iPhone, les vrais logos de ses outils, l'interface d'une plateforme
reconstruite d'après capture. Ce sont les touches de couleur vraie du film ; tout le reste prend
les rôles ci-dessous ([image.md](../../references/image.md), « Les objets connus »).

Les couleurs du film viennent de sa marque ([image.md](../../references/image.md), « La
palette ») ; ses captures, les logos de ses outils et les objets connus gardent leurs vraies
couleurs (le paragraphe d'avant).

| Rôle dans ce style | Avec la marque du client |
|---|---|
| La situation, le schéma, la démo, la preuve | la nuit à grille fine : `k-fond-sombre`, ou `var(--brand-sombre)` |
| Les étapes, l'écran coupé (côté résultat), les interfaces | le clair à grille : `k-fond-clair`, ou `var(--brand-clair)` |
| Le nom sur l'objet, le prix, un chapitre, un temps fort | l'aplat plein `var(--brand-accent)`, le texte posé dessus en `var(--brand-contrast)` |
| Le fil conducteur, la barre qui raye, le bloc qui surligne, le trait de la coupe | `var(--brand-accent)` plein |
| Le mot d'accent sur la nuit | `var(--brand-accent-lisible)` |
| Les mots d'appui, ce qui s'éteint | `var(--brand-gris-2)` à `var(--brand-gris-4)` |
| Les étiquettes de fonction | `k-blocs` : un bloc de l'accent, un bloc clair, un bloc sombre |

- **Le fond est un acteur** : il change quand le film change de temps (le nom, un chapitre, le
  prix, un avant / après), avec une cause à l'écran (un clic, un volet, un objet qui grandit, un
  disque parti du clic).
- **Trois fonds dans toute vidéo de plus de 15 s** ; un Reel peut en garder deux. Le fond qui
  domine suit sa marque : une marque claire prend plus de clair, une marque sombre plus de nuit.
- Sur l'aplat, rien n'entre en fondu, en flou ni avec une ombre sombre ([kit.md](../../references/kit.md),
  « Les pièges »).

## 4. La typographie

- **Police :** `var(--brand-font-display)` en très gras (800) pour le mot héros et les titres, à
  l'espacement serré (−3 à −4,5 %) ; `var(--brand-font-body)` pour les étiquettes ; Inter pour ses
  interfaces reconstruites (`assets/fonts/interfaces.css`).
- **Deux tons** : le plein et l'accent (« Ton **lien.** »), ou le gris d'appui et le plein
  (`k-titre`, `k-leger`, `k-accent`).
- **Trois tailles, jamais plus** ([image.md](../../references/image.md), « La typographie ») :

| Rôle | Mots | 1080 × 1920 | 1920 × 1080 |
|---|---|---|---|
| Le mot héros (`k-heros`) | 1 à 3 | 60 à 90 % de la largeur (130 à 400 px) | 60 à 90 % de la largeur, la moitié de la hauteur au plus |
| La ligne d'appui | 3 à 6 | 56 à 72 px | 56 à 72 px |
| Les étiquettes posées sur ce qu'on montre | 1 à 4 | 30 à 40 px | 30 à 40 px |

- Un contour net (`k-contour`) peut doubler un mot plein ; jamais une lueur ni un dégradé. La frappe
  au clavier seulement dans un champ de saisie.

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
  à l'écran ([mouvement.md](../../references/mouvement.md), « Les transitions ») : le raccord d'objet,
  l'objet qui devient le monde, la traversée d'un bouton, le disque parti du clic (`K.flash`), le
  report, le volet, le fil conducteur qui allume l'objet d'arrivée.
- **La coupe** (`K.tranche`) une ou deux fois par vidéo, sur un temps fort de la musique.
- Au plus un tiers de coupes franches entre les plans, jamais de fondu enchaîné ; un sens dominant
  dans toute la vidéo.

## 7. Le produit à l'écran

- Sa vraie matière, en descendant l'échelle de [image.md](../../references/image.md) (« La vraie
  matière ») : une vraie capture, son interface reconstruite et animée, un vrai chiffre mis en
  scène, le schéma de son vrai mécanisme, les vrais logos de ses outils, puis seulement ses mots.
- **Ce qui est connu se montre tel qu'on le connaît** : un dossier est le dossier bleu du Mac
  (`objet-dossier`, ou `nom-objet` avec `objet: "dossier"`, qui le prend par défaut), un document est
  un vrai PDF ou un vrai fichier Word (`objet-pdf`, `objet-doc`…), un outil est son vrai logo, un
  message arrive en notification d'iPhone (`K.notification`) ou en bulle (`K.bulle`), le téléphone a
  sa barre d'état (`K.statut`). Les icônes d'un seul trait, seulement pour une idée sans objet connu.
- L'objet de son offre se choisit au début de la fabrication et revient : il grandit au pivot
  (`nom-objet`), devient le nœud du schéma, se pose dans l'outil que son public a déjà (scenes.md,
  recette 9), finit dans la mosaïque.
- Une matière qui manque retire son élément : jamais une carte vide, une icône de remplacement ni
  une forme seule à la place d'un sujet.

## 8. Le son

- **L'original :** des morceaux de lancement à la batterie marquée, un silence net avant la
  révélation, un bruitage par geste.
- **Chez toi :** ce style n'impose aucune ambiance : la musique suit le but et le support de la vidéo
  ([son.md](../../references/son.md), « Choisir le morceau »). Entrée franche sur le pivot (le nom
  sur l'objet, le résultat), une pause du morceau sur la pause qui précède la révélation, l'écran
  final sur le dernier temps fort.
- **Avec une voix off** : les gestes suivent ses mots (un élément arrive avec le mot qui le nomme),
  la batterie entre dans une respiration de la voix, jamais sous le nom.
- **Bruitages, un par geste, jamais le même deux fois de suite** : un coup sec sur le mot qui claque,
  un souffle court quand le fil conducteur part, un petit clic par coche, un impact sur la coupe,
  un glissement sur le travelling, un pop par objet d'une rafale.

## 9. L'ouverture et la fin

- **Les 3 premières secondes :** la situation qu'on reconnaît, déjà là sur la toute première image
  (l'objet de l'ancienne façon, sa vraie capture, ou la preuve d'abord), et un mot héros qui la
  ponctue ; lisible dès 0,5 s, sur une image stable.
- **La fin :** la mosaïque qui devient le bouton (`fin`), ou le produit qui se pose avec son nom et
  l'appel, le fil conducteur en point final ; le nom et l'appel tenus 2,5 s au moins. En pub,
  « Découvre-le » et une flèche vers le bas, sans dessiner de bouton (`fin`, mode flèche).

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
- **Toujours :** le mot qui joue, le fil conducteur, la caméra qui voyage, un objet qui devient le
  suivant, trois fonds qui se relaient avec une cause, et les objets connus dans leurs vraies
  couleurs.

## Quand il décrit un autre style

Il répond « aucun de ces styles » sans rien dire de plus : c'est ce style, tel quel. Il décrit ce
qu'il veut (« plus calme », « tout sur fond clair », « de la 3D partout », « une typo énorme »,
« façon vieux papier ») : pars de ce style et applique ses mots, notés en une ligne dans `PLAN.md`
(« Style 0, ce qu'il a décrit : … ») :

| Il dit | Ce qui change |
|---|---|
| plus calme, plus premium | moins de rafales, des plans plus longs, des entrées douces (mot par mot sortant du flou), moins de bruitages |
| plus énergique, ça doit bouger | plus de rafales et de raccords d'objet, des plans plus courts entre les phrases, la coupe deux fois |
| fond clair, lumineux | le clair domine, la nuit seulement pour un temps fort |
| sombre, nuit | la nuit domine, l'aplat pour les temps forts |
| de la 3D, de la profondeur | la caméra voyage davantage, plus de plans en perspective et de champs de logos |
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
depuis un projet : `../../../templates/scenes/`), construites avec le kit, contrôlées en 9:16 et en
16:9 ; leur mode d'emploi est dans `templates/scenes/README.md`. Copie la scène dans `compositions/`
du projet et remplis son objet `CONTENU` avec sa vraie matière (rien d'exemple ne doit rester).

| Scène | Le geste | Durée |
|---|---|---|
| `situation` | la négation montrée, la corvée et son coût | 7 à 10 s |
| `nom-objet` | le nom sur l'objet | environ 4 s |
| `schema` | le fil conducteur, le schéma qui se trace | 4,5 à 5,5 s |
| `demo` | la démo qui sort de la fenêtre | 7 s |
| `parcours` | le travelling des étapes | 7,5 à 9,5 s |
| `preuve` | l'éventail et le grand chiffre | 6,5 s |
| `messages` | ses vrais messages en rafale autour d'un compteur | 4,5 s |
| `avant-apres` | l'écran coupé | 5,5 s |
| `prix` | le prix qui claque | 6 s |
| `fin` | la mosaïque qui devient le bouton | 7 s (5,5 s en mode flèche) |

Une scène que la table n'a pas se construit avec une recette de [scenes.md](../../references/scenes.md)
et les fonctions du kit ([kit.md](../../references/kit.md)). Le raccord entre deux scènes prêtes est
à toi : la fin de l'une devient le début de la suivante.
