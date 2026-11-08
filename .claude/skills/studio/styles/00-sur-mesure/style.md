# Style n°0 · Sur mesure · le style maison

**Ce qu'on voit :** sa vraie matière en grand et en profondeur ; chaque passage, un objet qui devient
le suivant ; peu de mots, énormes, qui jouent ce qu'ils disent ; ses interfaces qui chargent,
répondent, se réorganisent ; une caméra qui plonge dans les objets et en ressort ailleurs ; des
fonds qui changent avec une cause.
**Souvent utile pour :** tout, et d'abord sa première vidéo. C'est le style conseillé par défaut.
**D'après :** aucune vidéo en particulier : le niveau des films de lancement faits par les grands
studios de motion design, décrit dans [ambition.md](../../references/ambition.md).

**Pourquoi « sur mesure ».** Les styles 1 à 8 reprennent la grammaire d'une vidéo qui existe.
Celui-ci n'impose aucun geste : chaque vidéo y prend une forme à elle, écrite pour son offre et son
script. Son seul cahier des charges est l'ambition (des passages causés, de la profondeur, des mots
qui jouent, des interfaces qui vivent, une caméra qui a une raison de bouger, le flou de bougé) et
le seuil « on la regarde deux fois ». Deux vidéos dans ce style ne doivent pas se ressembler.

## 1. Le rythme

Celui de sa musique ([son.md](../../references/son.md), « Construire l'image sur la bande-son ») :
des vitesses qui contrastent (une rafale, puis une démonstration qui tient son cadre pendant que
l'interface agit), une courte pause avant la révélation, le geste le plus fort sur l'entrée franche
du morceau. Les repères chiffrés : [metier.md](../../references/metier.md), « Le rythme ».

## 2. Des gestes dont s'inspirer

Aucun n'est obligatoire, aucun n'est à reprendre tel quel : ce sont des idées déjà construites, dans
le kit ou dans les scènes prêtes, à prendre, transformer ou laisser.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le mot qui joue | un mot héros qui claque en se posant, s'étire, se barre, se surligne d'un bloc, ses lettres qui tombent ou se remettent en ligne | accroche, temps fort, toute idée clé | `K.claque`, `K.etire`, `K.barre`, `K.surligner`, `K.lettres`, `k-heros` |
| Le bouton qui envahit l'écran | le bouton cliqué s'ouvre au plein écran par un masque puis se referme sur l'objet suivant, les mots changent de couleur sous son bord | le pivot, un passage | sur mesure ([metier.md](../../references/metier.md), « Les passages »), `K.clic` |
| La négation montrée | l'objet de l'ancienne façon barré par l'accent, éteint au gris, puis un trait de l'accent fend l'écran en biais | le problème, ce qu'on remplace | `situation`, `K.barre`, `K.tranche` |
| L'objet qui porte son nom | l'objet de son offre grandit depuis le clic, son nom claque lettre par lettre, ce qu'il contient en jaillit | le pivot, le nom | `nom-objet` |
| Le schéma et son fil | un point de sa couleur parcourt les liens d'un schéma qui se trace et allume chaque nœud | le mécanisme | `schema`, `K.lien`, `K.trace`, `K.longer`, `k-fil` |
| La démo qui vit | dans son interface reconstruite, le curseur agit, chaque étape se coche, l'aperçu sort de la fenêtre et flotte en 3D | comment ça marche | `demo`, `K.curseur`, `K.taper` |
| La caméra qui s'approche du geste | la caméra se pose sur le champ où l'on tape, le curseur y va, puis elle recule sur le résultat | comment ça marche | `K.zoom`, `K.vu` |
| Le travelling des étapes | ses étapes vraies sur une longue toile, la caméra glisse de station en station | le parcours, ce qu'on reçoit | `parcours` |
| L'éventail et le grand chiffre | ses vraies captures en éventail, chacune avec son chiffre, puis le total énorme sur le flou | la preuve | `preuve`, `messages`, `K.compteur` |
| L'écran coupé | un volet pousse la moitié de l'écran : l'ancienne façon et son chrono d'un côté, le résultat de l'autre | comparer | `avant-apres` |
| Le prix qui claque | le prix en très grand sur l'aplat, puis la vraie échéance surlignée | l'offre et le prix | `prix` |
| Tout revient en bouton | les images de la vidéo reviennent en mosaïque 3D et se resserrent en un bouton que le curseur clique | la fin, l'appel | `fin` |

## 3. Les fonds et les couleurs

Les couleurs de sa marque, plus les vraies couleurs des objets connus
([interdits.md](../../references/interdits.md), « La palette »), dans ces rôles :

| Rôle | Avec la marque du client |
|---|---|
| La nuit (une situation, un schéma, une preuve) | `k-fond-sombre`, ou `var(--brand-sombre)` |
| Le clair (des étapes, des interfaces, le côté résultat) | `k-fond-clair`, ou `var(--brand-clair)` |
| Un temps fort (le nom, le prix, un chapitre) | l'aplat plein `var(--brand-accent)`, le texte posé dessus en `var(--brand-contrast)` |
| Ce qui relie, raye, surligne, tranche | `var(--brand-accent)` plein |
| Le mot d'accent sur la nuit | `var(--brand-accent-lisible)` |
| Les mots d'appui, ce qui s'éteint | `var(--brand-gris-2)` à `var(--brand-gris-4)` |

Le fond qui domine suit sa marque : une marque claire prend plus de clair, une marque sombre plus de
nuit. Sur l'aplat, rien n'entre en fondu, en flou ni avec une ombre sombre
([kit.md](../../references/kit.md), « Les pièges »).

## 4. Le son

Ce style n'impose aucune ambiance : la musique suit le but et le support de la vidéo
([son.md](../../references/son.md), « Choisir le morceau »). Un bruitage par geste visible, jamais
le même deux fois de suite ; l'entrée franche du morceau sur le pivot ; avec une voix off, la
batterie entre dans une respiration.

## Sur une autre offre

C'est le style fait pour toutes les offres : chaque vidéo y trouve sa forme.

- **Formation :** l'objet est son espace de formation ou son sommaire ; ses modules s'ouvrent ; la
  preuve d'abord quand elle a de vrais résultats d'élèves.
- **Coaching :** l'objet est son accompagnement (l'agenda, le plan) ; les étapes réelles ; ses vrais
  messages.
- **Logiciel :** son interface reconstruite porte la vidéo, et elle vit ; ce qui entre et ce qui sort.
- **Template, guide, communauté :** le document qui se remplit, les pages qui défilent ; les espaces
  et le rythme de la communauté, sans inventer de membres.

## Quand il décrit un autre style

Il décrit ce qu'il veut (« plus calme », « tout sur fond clair », « de la 3D partout », « une typo
énorme », « façon vieux papier ») : pars de ce style et applique ses mots, notés en une ligne dans
`PLAN.md` (« Style 0, ce qu'il a décrit : … »). Il répond « aucun » sans rien dire de plus : une
seule question à choix sur ce qu'il veut de différent (les lignes de la table, ou le lien d'une
vidéo qu'il aime), avec ta recommandation, puis la même chose.

| Il dit | Ce qui change |
|---|---|
| plus calme, plus premium | moins de rafales, des plans plus longs, des entrées douces (des mots qui sortent du flou), moins de bruitages |
| plus énergique, ça doit bouger, en mettre plein la vue | plus de passages d'objet et de plongées de caméra, des plans plus courts entre les phrases, la coupe deux fois |
| fond clair, lumineux | le clair domine, la nuit seulement pour un temps fort |
| sombre, nuit | la nuit domine, l'aplat pour les temps forts |
| de la 3D, de la profondeur | des fenêtres venues du fond, des murs et des anneaux d'objets en perspective, son téléphone qui pivote ; son ordinateur qui s'ouvre sur sa page s'il le demande (`K.ordinateur`) |
| une typo énorme | le mot héros à 90 % de la largeur, une ligne d'appui de moins |

Ses mots changent les gestes, jamais les interdits. Une description qui suppose une image inventée
(un paysage, des particules) ou une couleur hors de sa marque se dit en une phrase, avec ce qu'on
fera à la place. Il colle le lien d'une vidéo : c'est `studio_motion.py reference`, pas cette
section.

## En vertical et en carré

- **9:16 :** chaque scène se compose pour 1080 × 1920 : le sujet s'empile en hauteur et grandit,
  l'interface passe en carte verticale ou dans le téléphone, les mots empilés plus gros
  ([metier.md](../../references/metier.md), « Le cadre »). Tout texte dans la zone sûre du support
  (`studio_motion.py zones`).
- **4:5** prend la mise en page verticale ; **1:1** la mise en page 16:9 : vérifie la planche, un
  mot héros trop large passe à la ligne.

## Les compositions du kit

Ce style n'a pas de compositions à lui. Les scènes prêtes de la racine du dossier
(`templates/scenes/`, depuis un projet : `../../../templates/scenes/`), nommées dans la colonne
« Dans le kit » de la section 2, sont des exemples : lis-les, reprends-en un geste, ou copie-en une
et transforme-la ([scenes.md](../../references/scenes.md)). Les fonctions du kit :
[kit.md](../../references/kit.md).
