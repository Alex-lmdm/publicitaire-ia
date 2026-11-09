# La seconde passe : refaire la mise en scène, pas la retoucher

Le client la demande après la livraison (la phrase de sa formation : « Tu es un directeur artistique
en motion design… Repasse sur toute ma vidéo, plan par plan, et rends-la beaucoup plus
impressionnante… », ou ses mots : « rends-la plus impressionnante », « repasse dessus »). Il veut une
vidéo **beaucoup plus impressionnante**, pas la même un peu mieux. Une passe qui garde ce que la
revue avait validé ne lui donne presque rien : à l'essai, la moitié des images étaient restées
identiques et les vrais gains n'arrivaient qu'à la fin. Cette passe refait la mise en scène de
chaque plan, au niveau d'[ambition.md](ambition.md).

## Ce qui reste, ce qui change

- **Reste** : le script (ce que chaque plan raconte, et ses mots), sa marque et ses couleurs, les faits
  de la fiche, la musique et ses repères (les scènes partent sur les mêmes temps), les
  [interdits](interdits.md), et « Interdits de cette vidéo » dans `PLAN.md` : des défauts à ne pas
  refaire, pas des images à garder. Ils ont été écrits avec les objets de l'ancienne mise en scène,
  qui vont disparaître : ils se redisent d'abord en règles (la marche, étape 3).
- **Change** : l'image de chaque plan. Garder le script, c'est garder ce qu'il dit, pas sa mise en
  page. Un plan ne garde son image que si le client l'a demandé.

## Les objectifs, visibles à l'œil nu sur la planche

1. **Aucun plan n'a la même image qu'avant** : un autre cadre, une autre disposition, une autre
   entrée des mots. Sur deux planches aux mêmes instants, aucune case n'est identique.
2. **Des passages où un objet devient le suivant** : la plupart des passages, trois au moins ; au
   plus une coupe franche, sur un temps fort.
3. **De la vraie profondeur sur la moitié des plans au moins** : des objets à plusieurs distances,
   qui arrivent du fond, pivotent, s'empilent ; une interface vue en perspective plutôt qu'à plat ; la
   caméra qui plonge dedans et en ressort.
4. **Les fonds** changent avec le film, chaque fois avec une cause à l'écran (un objet qui grandit, un
   iris, un volet), et l'un d'eux au moins porte un temps fort (la nuit ou l'aplat de sa marque).
5. **La fin**, refaite en grand : ce qu'on a vu revient et devient l'appel, la marque (son logo, son
   nom) en grand sur la dernière image, qui bouge encore ; elle se tient 2,5 s au moins. Une petite
   carte figée sur un grand fond n'est pas une fin, même tenue le temps qu'il faut.
6. **La typographie** : le mot fort de chaque plan a son entrée travaillée, différente d'un plan à
   l'autre, et au moins un mot joue ce qu'il dit ; les lignes d'appui apparaissent nettes.
7. **Le sujet ne rapetisse pas** : ce que le spectateur doit lire (les mots, un bouton, l'interface
   qui porte l'information) reste lisible sur un téléphone à chaque instant où il compte. Un plan
   large est permis s'il dure moins d'une seconde, ou s'il se resserre ensuite sur son sujet (un
   recul qui révèle, une vue d'ensemble juste avant de plonger sur un détail). Restent interdits :
   deux objets qui se partagent l'écran en petit pendant tout un plan (l'un devant, l'autre en
   profondeur), et un sujet collé à un bord avec le vide de l'autre côté. `cadre` regarde une médiane
   et ne le voit pas : compare les planches case à case.

## La marche

1. Mets de côté la vidéo livrée : copie `../livraison/<vidéo>.mp4` dans `work/avant-seconde-passe.mp4`.
2. Sa planche serrée : `python3 ../../../tools/studio_motion.py planche work/avant-seconde-passe.mp4
   --pas 0.5`.
3. Dans `PLAN.md`, section « Seconde passe », d'abord **les interdits de cette vidéo redits en
   règles** valables pour n'importe quelle image : « le pont devant le téléphone cachait le titre »
   devient « rien ne passe devant un titre pendant qu'on le lit » ; « les téléphones descendaient
   sur les boutons » devient « rien d'important sous la zone sûre du bas » ; « creux de 1,5 s après
   l'accroche » devient « aucun creux de plus d'une seconde ». Puis, plan par plan : son image
   d'avant en une ligne, et sa nouvelle mise en scène (le cadre, la profondeur, le fond, l'objet qui
   l'amène et celui qui l'emmène, l'entrée des mots). Relis la liste face aux sept objectifs
   **avant** d'écrire le code.
4. Réécris les scènes, souvent en entier : une scène qu'on retouche garde son image. `npm run check`,
   puis le rendu.
5. Compare les deux planches serrées (`planche exports/<vidéo>.mp4 --pas 0.5` et celle de l'étape 2)
   aux mêmes instants : chaque objectif doit se voir, et chaque règle de l'étape 3 tenir ; un plan
   resté presque identique, ou dont le sujet reste petit plus d'une seconde sans se resserrer, se
   refait.
6. Les collisions pendant les animations ([revue.md](revue.md), porte 2), puis la revue (contrôles,
   relecteur neuf, son, export) et la livraison mise à jour.

Au client, en trois lignes : ce qui a changé (les passages, la profondeur, la fin…), où est la
nouvelle version, et qu'il peut encore tout changer avec ses mots.
