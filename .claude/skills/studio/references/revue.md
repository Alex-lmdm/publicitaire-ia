# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. Une vidéo
n'est finie que quand **tu as regardé sa planche** et corrigé ce qui ne va pas. Applique les
portes dans l'ordre, pour chaque vidéo, et ne passe à la suivante que si la précédente est
franchie.

## Porte 1 : la composition

`npm run check` dans le dossier de la vidéo (contrôles HyperFrames). Corrige toute erreur ; un
texte net volontairement posé sur une couche floue se marque (`kit.md`, pièges). Puis
`npm run render`, puis :

```bash
python3 ../../../tools/studio_motion.py rythme exports/page.mp4
```

Il doit répondre « ok » : au moins 1 événement par seconde, 0,8 s au plus d'écart médian entre
deux, aucune image figée plus de 1 s avant l'écran final. Il liste aussi les plus longs creux :
regarde-les, c'est souvent un raccord qui traîne ou une scène qui démarre vide.

**Seul le MP4 rendu fait foi.** `check` et `snapshot` téléchargent une police qui manque, le rendu
non : une police sans fichier passe en Impact ou en police système seulement dans le MP4. Regarde
donc la planche du fichier rendu, jamais seulement les captures de `check`.

## Porte 2 : la planche

```bash
python3 ../../../tools/studio_motion.py planche exports/reel.mp4 \
  --temps 0.3,1.8,4.3,8.3,12.3,17.8
python3 ../../../tools/studio_motion.py planche exports/story-ouverture.mp4
```

Prends les repères de ton plan, chacun plus 0,3 s (le moment où l'élément est posé) ; la
dernière image est toujours ajoutée. Pour juger le rythme, fais aussi une planche serrée, une
image toutes les 0,5 s (`ffmpeg -i exports/page.mp4 -vf "fps=2,scale=320:-2,tile=6x4" planche-%02d.jpg`),
et regarde-la comme on regarde la vidéo de référence : chaque case doit différer de la
précédente. L'outil lit le support et le format dans le projet et dessine
la bonne zone (et la bande du sticker pour une story avec lien). Ouvre la planche et regarde-la
vraiment :

- Tout texte important est **dans le cadre vert** ; rien dans le rouge (sticker).
- Chaque texte se lit à la taille de la vignette (360 px de large, la taille d'un aperçu).
- L'accroche est lisible sur la première vignette.
- La dernière image est propre : rien à moitié sorti, l'appel à l'action entier.
- Chaque texte de la planche correspond à une clé de `OFFRE.json`, ou c'est du ton.
- Vidéo de page : la première image est déjà forte et dit le sujet (c'est elle qu'on voit si la
  lecture automatique est bloquée).
- Aucun écran ne porte plus de 6 mots (hors interfaces) ; la plupart en portent 1 à 4.
- Les fonds alternent (sombre, clair, couleur pleine), aucun écran ne fait vide.
- Les raccords : la dernière case d'une scène et la première de la suivante se ressemblent.
- Boucle de section : la dernière image raccorde avec la première, sans saut.

## Porte 3 : la revue critique

Change de rôle : tu es un directeur artistique exigeant qui n'a pas fait la vidéo. Note de 1 à
10, avec une phrase de justification, sur ces huit critères :

1. **Accroche** : on comprend ce qu'on gagne à rester avant 3 s, sans le son.
2. **Structure** : chaque bloc de la structure choisie remplit son rôle, dans l'ordre ; le
   problème vient avant le produit.
3. **Rythme** : il se passe quelque chose toutes les demi-secondes ; on ne s'ennuie jamais, et
   chaque texte reste pourtant le temps de le lire.
4. **Montré, pas écrit** : des interfaces, des objets, des résultats ; 1 à 4 mots par écran ;
   des fonds qui alternent, rien de vide. Si on dirait des slides, c'est 3 au plus.
5. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources.
6. **Le mouvement sert** : il montre l'offre ou relie deux idées (un objet qui devient le
   suivant) ; la caméra vit sans courir ; aucun effet générique (néon, particules sans sujet).
7. **Marque** : ses couleurs, ses polices, une seule couleur d'accent.
8. **Appel à l'action** : celui du support, clair, tenu, impossible à rater.

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout. Liste toujours les trois plus gros défauts, même si tout est à 8. Si le client a donné
une vidéo de référence, mets côte à côte une planche de chaque (même cadence) : le niveau se juge
contre elle, pas contre la version précédente.

Dernier test, le plus simple : à partir des seules vignettes, résume le message en une phrase.
Si cette phrase n'est pas la promesse de la fiche, la vidéo ne dit pas ce qu'elle doit dire.

## Porte 4 : le son

`python3 ../../../tools/studio_motion.py son exports/reel.mp4`, puis `mastering` si la mesure n'est pas « ok ».
Réécoute le début et la révélation : le temps fort tombe-t-il sur l'offre ?

## Porte 5 : l'export

```bash
python3 ../../../tools/studio_motion.py export ../livraison/reel.mp4   # le support se déduit du nom du fichier
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
