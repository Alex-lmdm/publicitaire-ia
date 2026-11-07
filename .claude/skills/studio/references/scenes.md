# Les scènes : le langage, les scènes prêtes, les recettes

Chaque plan du film devient une scène. Trois sources, dans cet ordre :

1. **Une scène prête** (`templates/scenes/` du dossier Publicitaire IA, ci-dessous) : déjà
   construite avec le kit, en 9:16 et en 16:9, contrôlée. Copie-la dans `compositions/` du projet,
   remplace son objet `CONTENU` par les vrais textes, chiffres et images du client (clés de
   `OFFRE.json`, fichiers de `sources/`), et garde son mouvement.
2. **Un geste d'un style** du catalogue, si la vidéo a un style (`styles/<NN>/compositions/`).
3. **Une recette** décrite plus bas, construite avec le kit (`kit.md`).

Une story courte = une ou deux scènes ; une story de lancement = une scène par plan (huit ou neuf,
de 2,5 à 6,5 s) ; un Reel = trois à cinq ; une vidéo de page = huit à dix, reliées par des raccords
d'objet. Chaque scène porte un plan du film : elle montre ce qu'il dit et pose ses quelques mots.

## Le langage du motion design

Ce que font les vidéos de lancement de niveau studio, et que toute vidéo du studio fait aussi :

1. **Peu de mots, et ils jouent.** 20 à 30 mots en 30 à 40 s, en très grand, deux tons ; le mot
   fait ce qu'il dit (« ÉTIRE » s'étire, « FINI » se barre) puis devient l'objet suivant.
2. **On montre le comment** : la demande tapée, les étapes qui se cochent, le résultat qui sort ;
   le module qui s'ouvre, la séance qui se réserve, le document qui se remplit.
3. **Un fil conducteur** : un seul objet (un point de sa couleur, un anneau) traverse la vidéo,
   relie les nœuds d'un schéma, raye ce qu'on rejette, ouvre la scène suivante.
4. **Des schémas qui se tracent** : des nœuds vrais reliés par des traits qui se dessinent.
5. **La comparaison montrée** : l'ancienne façon en pile d'étapes avec son compteur d'heures ou
   d'euros, tranchée d'un coup ; la nouvelle en trois pastilles et son vrai délai.
6. **Des métaphores faites de sa matière** : ses messages qui passent dans un entonnoir et en
   sortent un seul, ses modules qui se rangent dans un plateau, un mur de documents et une barre de
   recherche.
7. **Des étiquettes de fonction** : deux mots en blocs empilés posés à côté de ce qui le fait.
8. **Des interfaces manipulées** : un curseur qui tire un réglage, des cartes qui arrivent en 3D,
   une fenêtre qui se remplit.
9. **Le récapitulatif** : les plans du film en mosaïque, puis le nom, la promesse, l'appel.
10. **Le son colle à chaque geste** : un coup sec par mot qui claque, un souffle par passage, le
    temps fort de la musique sur la révélation ([son.md](son.md)).

On n'en reprend jamais les couleurs (sa marque seulement), les images générées ni les lueurs.

## Les scènes prêtes

`templates/scenes/README.md` (depuis un projet : `../../../templates/scenes/README.md`) les liste
avec leur rôle, leur durée et ce qu'elles attendent du client, et dit comment s'en servir. Chacune
lit `K.cadre` et se met en page seule en 9:16 comme en 16:9. Remplis `CONTENU` (rien d'exemple ne
doit rester : un chiffre ou un nom d'exemple qui passe au rendu est un fait inventé), donne-lui la
durée qu'elle demande (pas plus : elle tiendrait sa dernière image), puis `npm run check` et 3
images. Le raccord entre deux scènes prêtes est à toi : la fin de l'une devient le début de la
suivante ([mouvement.md](mouvement.md), « Les transitions »).

## Les recettes, par rôle

Les durées sont des repères. Chaque recette part d'un objet déjà à l'écran : rien n'apparaît sans
cause.

### Ouvrir : la situation qu'on reconnaît

1. **La corvée** (6 à 9 s, nuit). L'outil ou la situation pénible d'avant en grand et en perspective
   (une timeline de montage, un tableur, une boîte mail débordante, un agenda saturé), ses vrais
   logos autour. Un mot par temps, en très gros, et à chaque mot la situation se charge un peu plus.
   Puis tout passe au flou et un compteur dit son prix (heures, euros), avec son contexte dessous.
   Enfin le ressenti (« Épuisant. ») tombe lourdement. Sortie : la caméra recule, un disque clair
   envahit l'écran.
2. **La question tapée** : le problème s'écrit dans un champ de saisie, l'offre y répond.
3. **La négation montrée** (3,5 s, nuit). Au lieu d'écrire « sans X ni Y » : l'objet de X (une
   caméra qui tourne, un devis, un tableur), barré par l'accent (`K.barre`), qui s'éteint au gris ;
   puis l'objet de Y, barré, ses morceaux tombent. Sortie : la coupe (`K.tranche`).
4. **La preuve d'abord** : le résultat montré avant d'être expliqué (la vraie capture, le vrai
   chiffre avec son repère), puis « comment ? ».

### Le pivot et le nom

5. **Le choix** (5 à 6 s, clair). Une ligne en deux temps (« Ton nouveau **coach** » → « tient
   dans ta **poche.** »), les options montent de la profondeur, le curseur les survole, clique
   celle qu'on montre : les autres tombent, la couleur d'accent part du clic ; le nom de l'offre se
   forme lettre par lettre, en très gros, avec une petite ligne qui dit ce qu'elle fait.
6. **Le nom sur l'objet** (3 s, aplat). L'objet de l'offre (un dossier, un carnet, une carte de
   membre, l'icône de l'app) grandit depuis le point cliqué ; son nom claque lettre par lettre
   (`K.lettres` + `K.claque`) ; ce qu'il contient en dépasse un instant puis retombe. Sortie : un
   volet, ou l'objet devient le nœud d'un schéma.
7. **Le titre qui se change sur place** (5 s) : « Ta page. » ; la matière arrive en rafale ;
   le titre devient « Tes clients. » à la même place.

### Montrer comment ça marche

8. **La couleur devient l'interface** (raccord, 1 s). Le plein écran de couleur est la fenêtre de
   l'application vue de très près ; la caméra recule et pivote, l'interface apparaît.
9. **Le produit entre dans l'outil** (1,7 s), quand l'offre vit dans un outil que le public a déjà
   (un modèle Notion, une extension, un dossier pour son IA, un groupe privé) : le curseur prend
   l'objet de l'offre et le pose dans l'outil, qui l'accepte. Sans ce geste, le spectateur ne
   comprend pas ce qu'il achète en plus de ce qu'il a.
10. **La démo dans l'interface** (6 à 10 s). Dans son interface reconstruite : le curseur agit (un
    fichier glissé, une demande tapée en moins d'une seconde, un bouton), la caméra s'approche du
    geste puis recule ; la réponse arrive et chaque étape se coche toutes les 0,5 à 0,6 s pendant
    que son aperçu sort de la fenêtre et flotte en 3D sur le côté. Le résultat apparaît, le curseur
    clique : flash de sa couleur.
11. **Le parcours en étapes** (5 à 8 s), pour un coaching, une formation, un service : les étapes
    vraies (de la page) posées sur une longue toile, la caméra glisse de station en station ; chaque
    station a son titre court, sa pastille de délai et sa matière (le sommaire, l'agenda, le
    document livré).
12. **Le schéma qui se trace** (3 à 5 s, nuit). Le nœud de l'offre, une ligne d'appui, les nœuds
    de ce qui entre et de ce qui sort ; les liens se tracent et le fil conducteur les parcourt
    (`K.lien`, `K.trace`, `K.longer`) ; chaque nœud reçoit (un petit coup d'échelle) et se coche.
13. **Le chapitre et la plongée** (1,4 s + la démo). Sur l'accent : mot géant pâle qui glisse,
    étiquette nette, interrupteur ; le curseur l'active, on plonge vers la démonstration.
14. **La transformation mesurée** (3 à 4 s). La matière brute en grand, les défauts se marquent un
    à un avec leur étiquette, disparaissent, le reste se resserre, le compteur descend. Le résultat
    devient l'objet suivant.
15. **Les réglages qui volent dans le résultat** (4 s). Le résultat à gauche, un titre court à
    droite ; des pastilles arrivent une à une puis volent dans le résultat, chacune s'y applique.

### Comparer

16. **L'écran coupé** (5 s). Un volet clair pousse la moitié droite. À gauche, sombre : l'ancienne
    façon qui se remplit, un chrono qui file. À droite, clair : le résultat, le vrai délai. Sortie :
    le panneau clair couvre tout, le résultat revient au centre.
17. **La pile contre les pastilles** (5 s). L'ancienne méthode en étapes empilées avec un compteur
    qui grimpe (d'après la page), le fil conducteur la tranche, elle tombe ; à sa place, les étapes
    de l'offre en trois pastilles reliées. Vrais chiffres seulement (`alternatives`, `recoit`).
18. **Le balai dans le téléphone** (6,5 s, vertical). Le téléphone montre l'avant ; une tête de
    lecture le balaie et chaque défaut s'allume ; sur le temps fort, un balai de sa couleur traverse
    l'écran et révèle l'après, qui joue vraiment (une `<video>` à la racine d'`index.html`, aux
    coordonnées exactes de l'écran du téléphone).

### Prouver

19. **L'éventail des vrais résultats** (2,5 s). Les vraies captures arrivent en éventail ; sous
    chacune, une pastille compte jusqu'à son vrai chiffre (demande ceux qui manquent : une carte
    sans chiffre fait trou).
20. **Le grand chiffre** (2 s). Les résultats s'écartent et passent au flou ; le total compte au
    centre en énorme, arrondi vers le bas, avec son repère.
21. **Les vrais messages** (3 s). Toutes les captures de témoignages de la page arrivent de la
    profondeur autour d'un compteur, chacune avec un petit bruitage, et restent dans le cadre.

### L'offre et le prix

22. **Le travelling de ce qu'on reçoit** (4,5 s). Ce qu'on reçoit posé sur une longue toile ; la
    caméra glisse de station en station (titre court, pastille de délai, matière animée), puis
    recule pour tout voir.
23. **Le prix en deux temps** (5 s, aplat). Le prix claque en très grand (jamais un compteur dont
    une valeur de passage se lirait comme un prix), « Paiement unique » s'ouvre dessous ; puis la
    vraie échéance se lit, sa date surlignée d'un bloc. Un prix barré seulement avec `prix.barre`
    dans la fiche ; s'il ne correspond à aucun prix pratiqué, préviens le client une fois (en Europe,
    une réduction annoncée se réfère au prix le plus bas des 30 derniers jours).
24. **La vitrine des exemples** (environ 2 s par exemple). Des vidéos ou des pages d'exemple
    restent **dans leur vignette**, jamais en plein écran (on les prendrait pour la pub d'une autre
    offre) : la rangée monte, le curseur clique la première, elle vient au centre en grand (près de
    la moitié de la largeur), les autres pivotent sur les côtés en carrousel (`rotationY` de 40 à
    52°, voile et flou qui grandissent avec la distance) ; l'extrait joue 2 s avec sa barre de
    lecture, une bulle claire dit en 2 ou 3 mots ce que c'est ; un clic toutes les 2 s. Aucun bouton
    lecture dans une story (il invite à toucher l'écran, ce qui fait passer à la suivante).
    Fabrication : les vignettes et leurs `<video>` vivent à la racine d'`index.html` (une seule
    timeline les place par `x`, `y`, `scale`, `rotationY`, `transformPerspective`), avec deux
    affiches par vignette (première et dernière image de l'extrait) ; le curseur et les bulles dans
    une scène transparente devant (`z-index: 3`). Extraits de 2 s préparés par `preparer-video`.

### Finir

25. **La mosaïque qui devient le bouton** (5 à 7 s). Les vraies images de cette vidéo reviennent en
    mosaïque 3D, la caméra recule, elles se resserrent au centre en un bouton ; le curseur le clique,
    il se remplit de l'accent, le nom au-dessus, une petite ligne dessous ; tenu 2,5 s.
26. **Le nom et l'appel** (4 s) : le produit se pose avec son nom, l'appel claque juste au-dessus de
    la bande du sticker (story), son point final est le point de sa couleur.

### Raccords

27. **La vignette qui devient la vidéo** (0,8 s) : une vignette grandit jusqu'au plein écran
    (`scale` = largeur de l'écran / largeur de la vignette, centre amené au centre), le reste
    s'efface en flou ; à l'arrivée, la vraie vidéo joue à la racine d'`index.html`, et sa première
    image est exactement la vignette (`ffmpeg -ss 0 -frames:v 1`). Seulement pour une vidéo de son
    offre à lui.
28. **La coupe** (0,6 s) : `K.tranche(tl, calque, t)`, appelée en dernier ; sur un temps fort.

## Combiner

Une vidéo de page qui vend un logiciel peut enchaîner : 1 (la corvée) → 5 (le choix, le nom) → 8 +
9 + 10 (la démo) → 13 + 14 (un chapitre par fonction) → 16 (l'écran coupé) → 19 + 20 + 21 (la
preuve) → 22 (l'offre) → 23 (le prix) → 25 (la fin). Une formation : 4 (la preuve d'abord) → 6 (le
nom sur l'objet) → 11 (le parcours) → 21 (les messages) → 22 → 23 → 26. Un coaching : 1 (la
situation) → 7 (le titre qui change) → 11 (les étapes) → 19 (les résultats) → 23 → 26. Change
l'enchaînement d'une vidéo à l'autre : le même film pour deux offres est un défaut.
