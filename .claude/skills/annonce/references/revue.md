# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. Une vidéo
n'est finie que quand **tu as regardé sa planche** et corrigé ce qui ne va pas. Applique les
portes dans l'ordre, pour chaque vidéo, et ne passe à la suivante que si la précédente est
franchie.

## Porte 1 : la composition

`npm run check` dans le dossier de la vidéo (contrôles HyperFrames). Corrige toute erreur. Puis
`npm run render`.

## Porte 2 : la planche

```bash
python3 <dossier Monteur IA>/tools/annonce.py planche exports/reel.mp4 --format reel \
  --temps 0.3,1.8,4.3,8.3,12.3,17.8
python3 <…>/tools/annonce.py planche exports/ouvert.mp4 --format story --sticker
```

Prends les repères de ton plan, chacun plus 0,3 s (le moment où l'élément est posé) ; la
dernière image est toujours ajoutée. Ouvre la planche et regarde-la vraiment :

- Tout texte important est **dans le cadre vert** ; rien dans le rouge (sticker).
- Chaque texte se lit à la taille de la vignette (360 px de large, la taille d'un aperçu).
- L'accroche est lisible sur la première vignette.
- La dernière image est propre : rien à moitié sorti, l'appel à l'action entier.
- Chaque texte de la planche correspond à une clé de `OFFRE.json`, ou c'est du ton.

## Porte 3 : la revue critique

Change de rôle : tu es un directeur artistique exigeant qui n'a pas fait la vidéo. Note de 1 à
10, avec une phrase de justification, sur ces sept critères :

1. **Accroche** : on comprend le sujet avant 2 s, sans le son.
2. **Lisibilité** : chaque texte reste le temps de le lire, rien ne court.
3. **Une idée par plan** : un sujet dominant, de l'air autour.
4. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources.
5. **Mouvement** : entrées décélérées, caméra lente et motivée, pas d'effet gratuit.
6. **Marque** : ses couleurs, ses polices, une seule couleur d'accent.
7. **Appel à l'action** : le mot-clé en grand, tenu, impossible à rater.

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout. Liste toujours les trois plus gros défauts, même si tout est à 8.

Dernier test, le plus simple : à partir des seules vignettes, résume le message en une phrase.
Si cette phrase n'est pas la promesse de la fiche, la vidéo ne dit pas ce qu'elle doit dire.

## Porte 4 : le son

`python3 …/annonce.py son exports/reel.mp4`, puis `mastering` si la mesure n'est pas « ok ».
Réécoute le début et la révélation : le temps fort tombe-t-il sur l'offre ?

## Porte 5 : l'export

```bash
python3 …/annonce.py export livraison/reel.mp4 --format reel --type reel
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
