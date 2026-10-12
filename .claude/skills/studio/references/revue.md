# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. Une vidéo
n'est finie que quand **tu as regardé sa planche** et corrigé ce qui ne va pas. Applique les
portes dans l'ordre, pour chaque vidéo, et ne passe à la suivante que si la précédente est
franchie.

## Porte 1 : la composition

`npm run check` dans le dossier de la vidéo (contrôles HyperFrames). Corrige toute erreur. Puis
`npm run render`.

**Seul le MP4 rendu fait foi.** `check` et `snapshot` téléchargent une police qui manque, le rendu
non : une police sans fichier passe en Impact ou en police système seulement dans le MP4. Regarde
donc la planche du fichier rendu, jamais seulement les captures de `check`.

## Porte 2 : la planche

```bash
python3 <dossier Monteur IA>/tools/studio_motion.py planche exports/reel.mp4 \
  --temps 0.3,1.8,4.3,8.3,12.3,17.8
python3 <…>/tools/studio_motion.py planche exports/story-ouverture.mp4
```

Prends les repères de ton plan, chacun plus 0,3 s (le moment où l'élément est posé) ; la
dernière image est toujours ajoutée. L'outil lit le support et le format dans le projet et dessine
la bonne zone (et la bande du sticker pour une story avec lien). Ouvre la planche et regarde-la
vraiment :

- Tout texte important est **dans le cadre vert** ; rien dans le rouge (sticker).
- Chaque texte se lit à la taille de la vignette (360 px de large, la taille d'un aperçu).
- L'accroche est lisible sur la première vignette.
- La dernière image est propre : rien à moitié sorti, l'appel à l'action entier.
- Chaque texte de la planche correspond à une clé de `OFFRE.json`, ou c'est du ton.
- Vidéo de page : la première image affiche la promesse (c'est elle qu'on voit si la lecture
  automatique est bloquée).
- Boucle de section : la dernière image raccorde avec la première, sans saut.

## Porte 3 : la revue critique

Change de rôle : tu es un directeur artistique exigeant qui n'a pas fait la vidéo. Note de 1 à
10, avec une phrase de justification, sur ces huit critères :

1. **Accroche** : on comprend ce qu'on gagne à rester avant 3 s, sans le son.
2. **Structure** : chaque bloc de la structure choisie remplit son rôle, dans l'ordre ; le
   problème vient avant le produit.
3. **Lisibilité** : chaque texte reste le temps de le lire, rien ne court.
4. **Une idée par plan** : un sujet dominant, de l'air autour.
5. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources.
6. **Le mouvement sert** : il montre l'offre ou porte un mot ; aucun effet décoratif, caméra lente.
7. **Marque** : ses couleurs, ses polices, une seule couleur d'accent.
8. **Appel à l'action** : celui du support, clair, tenu, impossible à rater.

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout. Liste toujours les trois plus gros défauts, même si tout est à 8.

Dernier test, le plus simple : à partir des seules vignettes, résume le message en une phrase.
Si cette phrase n'est pas la promesse de la fiche, la vidéo ne dit pas ce qu'elle doit dire.

## Porte 4 : le son

`python3 …/studio_motion.py son exports/reel.mp4`, puis `mastering` si la mesure n'est pas « ok ».
Réécoute le début et la révélation : le temps fort tombe-t-il sur l'offre ?

## Porte 5 : l'export

```bash
python3 …/studio_motion.py export livraison/reel.mp4   # le support se déduit du nom du fichier
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
