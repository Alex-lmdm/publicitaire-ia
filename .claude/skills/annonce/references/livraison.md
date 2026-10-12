# La livraison

Le client doit pouvoir publier sans réfléchir : les fichiers bien nommés, la légende prête, le
moment de chaque publication.

## Le dossier `livraison/`

| Fichier | Contenu |
|---|---|
| `reel.mp4` | Le Reel d'annonce, masterisé, couverture en première image |
| `reel-sans-musique.mp4` | Le même sans musique, pour un son Instagram |
| `teaser.mp4`, `ouvert.mp4`, `relance.mp4`, `dernier-jour.mp4` | Les stories prévues |
| `nouveaute.mp4`, `story.mp4` | Pour une nouveauté |
| `couverture.jpg` | La couverture du Reel (1080 × 1920) |
| `legende.txt` | La légende du Reel, prête à coller |

Puis `python3 tools/annonce.py livrer "<dossier de l'annonce>"` : « ok » ou la liste de ce qui
manque.

## La couverture

Une image composée exprès (pas une capture au hasard) : la promesse ou le nom de l'offre en
grand, dans la zone texte, lisible à 200 px de large (c'est la taille dans la grille du profil).
Elle ne montre rien que le Reel ne dit pas. Pose-la en première image :

```bash
python3 tools/annonce.py couverture exports/reel-master.mp4 livraison/couverture.jpg livraison/reel.mp4
```

Les aperçus (WhatsApp, X, la grille avant lecture) montrent alors la bonne image.

## La légende

Dans la voix du client (relis 2 ou 3 de ses légendes s'il en a dans le dossier, sinon sa page de
vente). Structure :

```
<La promesse en une ligne, sans emoji au début>

<Deux ou trois lignes : ce qu'on reçoit, ce qui change, tiré de la fiche>

<La date si c'est un lancement : « Ouvert jusqu'à dimanche minuit. »>

💬 Commente <MOT> et je t'envoie le lien en DM.
```

Pas de liste de hashtags (deux ou trois au plus, s'il en met d'habitude). La phrase d'appel à
l'action reprend exactement le mot-clé de la vidéo. S'il n'utilise pas d'automatisation de DM
(`cta.dmTool` vide dans `brand.config.json`), propose « Le lien est dans ma bio » à la place et
demande-lui ce qu'il préfère.

## Le calendrier (« ## Quand publier » dans PLAN.md)

Écris les vraies dates, tirées de la fiche :

```
## Quand publier

- Mercredi 15, 18 h : story teaser (teaser.mp4).
- Jeudi 16, 18 h : Reel d'annonce (reel.mp4 + legende.txt), puis tout de suite la story
  d'ouverture (ouvert.mp4) avec le sticker lien sur la zone libre en bas.
- Dimanche 19, le matin : story dernier jour (dernier-jour.mp4), sticker lien au même endroit.
```

## Le message au client

Court. Ce qu'il a, quand le poster, comment demander une retouche :

> C'est prêt, tout est dans `livraison/` :
> - le Reel d'annonce (et sa version sans musique si tu veux un son Instagram), sa couverture et sa légende ;
> - les stories teaser, ouverture et dernier jour.
>
> Le calendrier est dans PLAN.md : teaser mercredi 18 h, Reel et story d'ouverture jeudi 18 h,
> dernier jour dimanche matin. Sur les stories avec lien, pose le sticker sur la zone libre en bas.
>
> Une retouche ? Dis-la simplement, par exemple « laisse le prix affiché plus longtemps ».

Ne publie rien toi-même, n'envoie rien : la publication reste à lui.
