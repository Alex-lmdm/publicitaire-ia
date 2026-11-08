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
  refaire, pas des images à garder.
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
5. **La fin**, refaite en grand : ce qu'on a vu revient et devient l'appel, et elle se tient 2,5 s
   au moins.
6. **La typographie** : une entrée différente à chaque plan, et au moins un mot qui joue ce qu'il dit.

## La marche

1. Mets de côté la vidéo livrée : copie `../livraison/<vidéo>.mp4` dans `work/avant-seconde-passe.mp4`.
2. Sa planche serrée : `python3 ../../../tools/studio_motion.py planche work/avant-seconde-passe.mp4
   --pas 0.5`.
3. Dans `PLAN.md`, section « Seconde passe », plan par plan : son image d'avant en une ligne, puis sa
   nouvelle mise en scène (le cadre, la profondeur, le fond, l'objet qui l'amène et celui qui
   l'emmène, l'entrée des mots). Relis la liste face aux six objectifs **avant** d'écrire le code.
4. Réécris les scènes, souvent en entier : une scène qu'on retouche garde son image. `npm run check`,
   puis le rendu.
5. Compare les deux planches serrées (`planche exports/<vidéo>.mp4 --pas 0.5` et celle de l'étape 2)
   aux mêmes instants : chaque objectif doit se voir ; un plan resté presque identique se refait.
6. Les collisions pendant les animations ([revue.md](revue.md), porte 2), puis la revue (contrôles,
   relecteur neuf, son, export) et la livraison mise à jour.

Au client, en trois lignes : ce qui a changé (les passages, la profondeur, la fin…), où est la
nouvelle version, et qu'il peut encore tout changer avec ses mots.
