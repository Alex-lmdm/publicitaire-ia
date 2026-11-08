# Les scènes prêtes

Des scènes déjà construites avec le kit, contrôlées en 9:16 et en 16:9 : elles portent le niveau de
finition, et l'IA les remplit avec la vraie matière du client au lieu de tout réécrire à chaque
vidéo. Le langage, les recettes et le moment de s'en servir : skill `studio`,
`references/scenes.md`.

| Scène | Rôle | Durée | Ce qu'elle attend du client (`CONTENU`) |
|---|---|---|---|
| `situation.html` | ouvrir : la situation qu'on reconnaît, son coût, le ressenti (recette 1) | 7 à 10 s | la corvée en 2 à 6 lignes (ou une capture), 1 ou 2 temps de mots, un compteur chiffré avec son contexte, un ressenti |
| `nom-objet.html` | le pivot et le nom : l'objet de l'offre grandit, son nom claque lettre par lettre, son contenu en jaillit puis retombe (recette 6) | environ 4 s | l'objet (dossier, carnet, carte, app ou sa vraie image), son icône, le nom (1 à 3 mots), une ligne d'appui (3 à 6 mots), 2 à 4 vrais éléments de l'offre, la sortie (nœud ou volet) |
| `schema.html` | comment ça marche : les liens se tracent, le fil conducteur les parcourt, chaque nœud se coche, puis la caméra plonge dans l'offre (recette 12) | 4,5 à 5,5 s | le nœud de l'offre (nom, icône), 1 à 3 entrées, 2 à 4 sorties (nom, icône ou logo), une ligne d'appui ou un mot héros, le mot à surligner |
| `parcours.html` | le parcours en étapes : la caméra glisse de station en station derrière le fil conducteur, puis recule pour tout voir (recettes 11 et 22) | 7,5 s (3 étapes) à 9,5 s (4 étapes) | 3 à 5 étapes vraies : titre court, délai, matière (une liste qui se coche, un agenda qui se remplit, ou sa capture) |
| `demo.html` | comment ça marche : la démo dans son interface, le curseur agit, les étapes se cochent et leurs aperçus sortent de la fenêtre (recette 10) | 7 s | une ligne d'appui (3 à 6 mots), l'écran de son produit (titre, invite, demande tapée) ou sa capture avec la place de son champ, 3 ou 4 étapes vraies avec l'aperçu de chacune (2 textes ou une image), le statut obtenu, le bouton du résultat |
| `preuve.html` | prouver : l'éventail de ses vrais résultats, puis le grand chiffre (recettes 19 et 20) | 6,5 s | une ligne d'appui, 3 à 5 vraies captures et leur format, chacune avec son vrai chiffre et son contexte, le total arrondi vers le bas avec son repère et le mot à surligner |
| `prix.html` | l'offre et le prix : ce qu'on reçoit, puis le prix en deux temps et sa vraie échéance (recette 23) | 6 s | ce qu'on reçoit en 2 à 4 pastilles, le prix tel qu'affiché, ses modalités, l'échéance et sa date (ou null), l'ancien prix seulement si `prix.barre` est dans la fiche |
| `avant-apres.html` | comparer : l'écran coupé, l'ancienne façon et son chrono d'un côté, le résultat et son vrai délai de l'autre (recette 16) | 5,5 s | les étiquettes ; l'avant (titre, 3 à 6 lignes ou une capture, le chrono) ; l'après (résultat, 2 à 4 étapes ou une capture, le délai) |
| `messages.html` | prouver : ses vrais messages arrivent en rafale autour d'un compteur (recette 21) | 4,5 s (4 au moins) | 4 à 8 témoignages (prénom, texte, quand ; ou ses captures), un compteur avec son contexte |
| `fin.html` | finir : la mosaïque de la vidéo devient le bouton, le nom et l'appel (recettes 25 et 26) | 7 s (5,5 s en mode flèche) | 4 à 8 images de la vidéo, le nom, le texte du bouton, l'appel (3 à 6 mots), `mode` : bouton, ou flèche pour une pub (on n'y dessine pas de bouton) |

## S'en servir

1. Copie le fichier dans `compositions/` du projet (depuis un projet : `../../../templates/scenes/`).
2. Remplis son objet `CONTENU`, en tête du script : chaque texte, chiffre et image vient de
   `OFFRE.json` ou de `sources/` ; ce qui n'existe pas pour son offre se met à `null`, et le temps
   correspondant disparaît. **Rien d'exemple ne doit rester** : un chiffre d'exemple qui passe au
   rendu est un fait inventé.
3. Monte-la dans `index.html` comme toute scène (`kit.md`, « Le squelette d'une scène ») et donne à
   son hôte et à sa racine la durée qu'elle demande (le commentaire de `CONTENU` la donne) : si
   `data-duration` est trop court, `npm run check` relève des mots partis avant d'être lus
   (`line_unread`), et la console de l'aperçu écrit la durée à mettre.
4. `npm run check`, puis 3 à 6 images (`npx hyperframes snapshot --at …`) ; après le rendu,
   `rythme`, `cadre` et `palette`.
5. Pour la poser deux fois dans la même vidéo, remplace partout son identifiant (la valeur de
   `data-composition-id` : « situation », « temoignages » pour `messages.html`, « cloture » pour
   `fin.html`…) par un autre dans la copie.

**Entre deux scènes prêtes, le raccord est à toi.** Chacune finit proprement, mais posées bout à bout
elles se suivent en coupes franches nues : la fin de l'une doit devenir le début de la suivante (un
objet qui grandit, un flash depuis un clic, un volet : `references/mouvement.md`, « Les
transitions »). `rythme` le relève sur le film (« coupes franches nues », au plus un tiers des
raccords). Donne aussi à chaque scène **la durée qu'elle demande, arrondie au temps suivant de la
musique** (0,5 s de plus au plus, pour que la scène suivante parte sur un temps : `calage` le
vérifie) ; pas davantage : une scène trop longue tient sa dernière image, et `rythme` relève une
image figée.

Tu peux retoucher une scène copiée (une durée, une position, un geste en plus) : c'est ta copie. Ce
qui doit rester : sa matière en grand, ses mots dans le calque `k-mots` (immobiles pendant qu'on les
lit), sa première image qui montre déjà le sujet, ses tailles de texte.

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
- **Contrôlée** dans les deux formats avant d'entrer dans ce tableau : `check` sans erreur ni
  avertissement de métier sur un texte à lire, `rythme` et `cadre` « ok », images regardées.
