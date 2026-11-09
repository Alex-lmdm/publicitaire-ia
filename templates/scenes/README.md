# Les scènes prêtes : des exemples

Dix scènes déjà construites avec le kit. Écrites en 9:16, elles prennent le format du projet qui
les monte (`K.cadre` lit leur hôte et recale leur racine) : en 16:9, elles se remettent en page
seules. Ce qui en a été contrôlé est en bas de ce fichier. Ce sont des
**exemples dont on s'inspire**, pas des gabarits à remplir : on y lit comment se règle un problème
(une mise en page qui marche dans les deux formats, une tenue de lecture calculée, une rafale, une
caméra qui glisse), on en reprend un geste, ou on en copie une pour la transformer. Une vidéo faite
de scènes prêtes posées bout à bout est plate ; le niveau visé et la façon de s'en servir : skill
`studio`, `references/ambition.md` et `references/scenes.md`.

| Scène | Rôle | Durée | Ce qu'elle attend du client (`CONTENU`) |
|---|---|---|---|
| `situation.html` | ouvrir : la situation qu'on reconnaît, son coût, le ressenti | 7 à 10 s | la corvée en 2 à 6 lignes (ou une capture), 1 ou 2 temps de mots, un compteur chiffré avec son contexte, un ressenti |
| `nom-objet.html` | le pivot et le nom : l'objet de l'offre grandit, son nom claque lettre par lettre, son contenu en jaillit puis retombe | environ 4 s | l'objet (dossier, bleu comme celui du Mac par défaut ; carnet, carte, app ou sa vraie image), son icône, le nom (1 à 3 mots), une ligne d'appui (3 à 6 mots), 2 à 4 vrais éléments de l'offre, la sortie (nœud ou volet) |
| `schema.html` | comment ça marche : les liens se tracent, le fil conducteur les parcourt, chaque nœud se coche, puis la caméra plonge dans l'offre | 4,5 à 5,5 s | le nœud de l'offre (nom, icône), 1 à 3 entrées, 2 à 4 sorties (nom, icône ou logo), une ligne d'appui ou un mot héros, le mot à surligner |
| `parcours.html` | le parcours en étapes : la caméra glisse de station en station derrière le fil conducteur, puis recule pour tout voir | 7,5 s (3 étapes) à 9,5 s (4 étapes) | 3 à 5 étapes vraies : titre court, délai, matière (une liste qui se coche, un agenda qui se remplit, ou sa capture) |
| `demo.html` | comment ça marche : la démo dans son interface, le curseur agit, les étapes se cochent et leurs aperçus sortent de la fenêtre | 7 s | une ligne d'appui (3 à 6 mots), l'écran de son produit (titre, invite, demande tapée) ou sa capture avec la place de son champ, 3 ou 4 étapes vraies avec l'aperçu de chacune (2 textes ou une image, et l'objet connu qu'elle produit : `icone`), le statut obtenu, le bouton du résultat |
| `preuve.html` | prouver : l'éventail de ses vrais résultats, puis le grand chiffre | 6,5 s | une ligne d'appui, 3 à 5 vraies captures et leur format, chacune avec son vrai chiffre et son contexte, le total arrondi vers le bas avec son repère et le mot à surligner |
| `prix.html` | l'offre et le prix : ce qu'on reçoit, puis le prix en deux temps et sa vraie échéance | 6 s | ce qu'on reçoit en 2 à 4 pastilles, le prix tel qu'affiché, ses modalités, l'échéance et sa date (ou null), l'ancien prix seulement si `prix.barre` est dans la fiche |
| `avant-apres.html` | comparer : l'écran coupé, l'ancienne façon et son chrono d'un côté, le résultat et son vrai délai de l'autre | 5,5 s | les étiquettes ; l'avant (titre, 3 à 6 lignes ou une capture, le chrono) ; l'après (résultat, 2 à 4 étapes ou une capture, le délai) |
| `messages.html` | prouver : ses vrais messages arrivent en rafale autour d'un compteur | 4,5 s (4 au moins) | 4 à 8 témoignages (prénom, texte, quand ; ou ses captures), un compteur avec son contexte |
| `fin.html` | finir : la mosaïque de la vidéo devient le bouton, le nom et l'appel | 7 s (5,5 s en mode flèche) | 4 à 8 images de la vidéo, le nom, le texte du bouton, l'appel (3 à 6 mots), `mode` : bouton, ou flèche pour une pub (on n'y dessine pas de bouton) |

## S'en servir

- **Pour t'inspirer** : ouvre-la, lis son script (le calcul de sa mise en page sur `K.cadre`, sa
  tenue de lecture, ses courbes), et écris ta propre scène pour ton plan.
- **Pour la transformer** : copie le fichier dans `compositions/` du projet (depuis un projet :
  `../../../templates/scenes/`) ; c'est ta copie, change-la autant que ton plan le demande (sa mise
  en scène, sa caméra, ses passages, ses gestes). Son objet `CONTENU`, en tête du script, se remplit
  en entier : chaque texte, chiffre et image vient de `OFFRE.json` ou de `sources/` ; ce qui
  n'existe pas pour son offre se met à `null`, et le temps correspondant disparaît. **Rien
  d'exemple ne doit rester** : un chiffre d'exemple qui passe au rendu est un fait inventé. Ses faits
  y sont des emplacements (« [PRÉNOM] », « [SON PRIX] », « [CHIFFRE] », « [DÉLAI] ») : tant qu'il
  en reste un, la scène l'écrit en erreur dans la console (`K.emplacements`), et `check` le compte.
  `situation` porte `data-accroche`, `prix` porte `data-prix` : un seul élément de la vidéo chacun
  (`composition.md`, règle 10) ; retire-les d'une seconde copie. Une
  icône (`icone`) : d'abord ce qu'on reconnaît, dans ses vraies couleurs (le vrai logo de l'outil,
  `logos`, ou un objet connu du kit : `objet-pdf`, `objet-dossier`…) ; une icône d'un seul trait
  seulement pour une idée (une coche, un euro).
- Montée dans `index.html` comme toute scène (`kit.md`, « Le squelette d'une scène »), elle prend
  la durée qu'elle demande (le commentaire de `CONTENU` la donne), jusqu'au temps suivant de la
  musique, pas davantage : trop courte, `npm run check` relève des mots partis avant d'être lus
  (`line_unread`) ; trop longue, elle tient sa dernière image. Puis `npm run check` et 3 à 6 images.
- Pour la poser deux fois dans la même vidéo, remplace partout son identifiant (la valeur de
  `data-composition-id`) par un autre dans la copie.
- **Le passage entre deux scènes est toujours à toi** : posées bout à bout, elles se suivent en
  coupes nues. La fin de l'une devient le début de la suivante (`references/metier.md`, « Les
  passages ») ; `rythme` relève les coupes franches nues sur le film.

Ce qui reste vrai dans une copie : sa matière en grand, ses mots dans le calque `k-mots` (immobiles
pendant qu'on les lit), sa première image qui montre déjà le sujet, ses tailles de texte.

## Les règles d'une scène prête (pour en écrire une nouvelle)

- **Un seul fichier**, une sous-composition (`<template>`), identifiant unique (la racine, la clé
  de la timeline et le préfixe de chaque identifiant intérieur), tout le contenu dans un objet
  `CONTENU` en tête du script, avec un commentaire par champ.
- **Les deux formats** : la mise en page se calcule depuis `K.cadre` (`V = hauteur > largeur`) ; en
  9:16 on empile et on agrandit, en 16:9 on met côte à côte ; une `zone` (haut, bas en part de la
  hauteur) règle la place des textes selon le support.
- **Les tailles** : le mot héros remplit 60 à 90 % de sa colonne (taille estimée sur le nombre de
  lettres, jamais mesurée à l'écran) ; aucun texte à lire sous 28 px ; une matière qui passe au flou
  ou qui sert de texture porte `data-layout-ignore`.
- **Le cadre** : le sujet occupe au moins 40 % de la largeur ou de la hauteur ; une carte prend la
  hauteur de sa matière, jamais une grande surface vide.
- **La lecture** : 0,8 s + 0,3 s par mot (1,5 s au moins) ; les mots claquent en bloc, se tiennent
  immobiles, sortent en 0,25 à 0,3 s ; la scène calcule la durée qu'il lui faut et la compare à
  `K.duree` (celle de son hôte une fois montée).
- **La première image** montre déjà le sujet et ses premiers mots (c'est l'affiche).
- **Des événements de contenu** pendant les tenues (une ligne qui s'ajoute, un compteur, une
  coche) : `rythme` doit répondre « ok » sur la scène seule.
- **La palette** : seulement les jetons `var(--brand-*)` et les neutres du kit ; rien de
  transparent sur l'accent.
- **Contrôlée** dans les deux formats avant d'entrer dans ce tableau, son `CONTENU` d'exemple en
  place : `lint` sans erreur ; `check` sans autre erreur que celle du garde-fou des exemples, sans
  avertissement de métier sur un texte à lire, et ses intentions tenues (`index.motion.json` :
  l'accroche dès 0,5 s, rien de figé plus de 1,5 s, le prix dans le cadre) ; images regardées
  (`snapshot`). `rythme` et `cadre` se lancent sur le MP4 de la vidéo qui la monte.

## Ce qui a été contrôlé (09/11/2026, HyperFrames 0.9.26)

Les dix scènes montées bout à bout dans un projet 16:9 puis dans un projet 9:16 (le gabarit du
dossier, `CONTENU` d'exemple en place, les intentions de `nouvelle` et la règle du prix) :

- `lint` : aucune erreur (un avertissement : `demo.html` dépasse 300 lignes) ;
- `check` : une erreur par scène, celle du garde-fou des exemples (voulue : leurs emplacements
  sont là) ; aucune erreur de mise en page ni de mouvement ; l'accroche, le mouvement continu et le
  prix dans le cadre tenus ; quelques avertissements de contraste dans `prix` vers 5,4 s (la date
  passe à l'accent pendant que son bloc s'ouvre ; le bas du prix d'exemple sur le bloc des
  modalités) ;
- images regardées dans les deux formats.

Pas contrôlé ici : `rythme`, `cadre` et le flou de bougé, qui demandent un rendu entier.
