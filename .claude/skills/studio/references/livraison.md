# La livraison

Le client doit pouvoir publier sans réfléchir : les fichiers bien nommés, le texte de chaque
publication prêt, et, pour une campagne, le moment de chaque publication.

## Le dossier `livraison/`

| Fichier | Quand | Contenu |
|---|---|---|
| `<vidéo>.mp4` | toujours | La vidéo masterisée, couverture en première image : `reel.mp4`, `page.mp4`, `story-ouverture.mp4`, `page-1x1.mp4`… |
| `<vidéo>-sans-musique.mp4` | Reel, TikTok | Les mêmes bruitages sans musique, pour un son de la plateforme |
| `<vidéo>.jpg` | page, section | L'affiche, montrée avant la lecture : elle affiche déjà la promesse |
| `legende-reel.txt`, `legende-tiktok.txt` | Reel, TikTok | La légende, prête à coller |
| `textes-pub.txt`, `textes-fil.txt` | pub, fil | Texte principal, titre, description, bouton conseillé ; une version par accroche |
| `post-linkedin.txt`, `post-x.txt` | LinkedIn, X | Le texte du post |
| `integration.md` | page, section | Comment poser la vidéo sur sa page (ci-dessous) |
| `couverture.jpg` | Reel, TikTok | La couverture, lisible à 200 px de large |

Puis `python3 tools/studio_motion.py livrer "<dossier>"` : « ok » ou la liste de ce qui manque.

## La couverture et l'affiche

Une image composée exprès (pas une capture au hasard) : la promesse ou le nom de l'offre en grand,
dans la zone texte, lisible à 200 px de large. Elle ne montre rien que la vidéo ne dit pas. Pose-la
en première image :

```bash
python3 tools/studio_motion.py couverture exports/reel-master.mp4 livraison/couverture.jpg livraison/reel.mp4
```

Pour une page, l'affiche (`page.jpg`) est la première image de la vidéo, de moins de 100 Ko :
`python3 tools/studio_motion.py affiche livraison/page.mp4 livraison/page.jpg`.

## Les textes de publication

Dans la voix du client (relis sa page de vente et ses légendes s'il y en a). Le mot-clé ou le
lien est exactement celui de la vidéo.

**Légende de Reel ou TikTok**

```
<La promesse en une ligne, sans emoji au début>

<Deux ou trois lignes : le problème, ce que l'offre change, tirés de la fiche>

<La date si elle est réelle : « Ouvert jusqu'à dimanche minuit. »>

💬 Commente <MOT> et je t'envoie le lien en DM.
```

Pas de liste de hashtags (deux ou trois au plus, s'il en met d'habitude). Sans automatisation de
DM (`dm` vide dans `studio.config.json` : demande-le une fois s'il ne l'a pas dit), propose
« Le lien est dans ma bio ».

**Pub** : pour chaque accroche, un texte principal (3 à 5 lignes : problème, résultat, preuve),
un titre de 5 mots, une description courte, et le bouton conseillé (« En savoir plus »,
« S'inscrire »). Sans prix.

**LinkedIn** : un post de 6 à 10 lignes courtes, ton professionnel, le problème métier, un résultat
chiffré de la fiche, le lien à la fin. **X** : 1 à 3 lignes, le fait nouveau ou le résultat, le lien.

## Poser la vidéo sur une page de vente (`integration.md`)

Le client utilise souvent systeme.io, Webflow, WordPress ou une page faite par son IA. Explique
simplement :

- **Vidéo du haut de page** : héberge-la (sur l'hébergeur de son outil de page, ou YouTube en non
  répertorié, ou Vimeo), active la lecture automatique en muet si l'outil le permet, ajoute
  l'affiche. Le bouton d'achat va juste sous la vidéo.
- **Boucle de section** : pas de lecteur YouTube (il affiche des contrôles et des suggestions).
  Si sa page accepte du code : `<video autoplay muted loop playsinline poster="section.jpg"
  src="section.mp4"></video>`. Une boucle de plus de 5 s doit pouvoir se mettre en pause.

## Le calendrier (campagne de lancement)

Dans `PLAN.md`, section « ## Quand publier », avec les vraies dates de la fiche :

```
## Quand publier

- Mercredi 15, 18 h : story teaser (story-teaser.mp4).
- Jeudi 16, 18 h : Reel (reel.mp4 + legende-reel.txt), puis la story d'ouverture
  (story-ouverture.mp4) avec le sticker lien sur la zone libre en bas.
- Dimanche 19, le matin : story dernier jour (story-dernier-jour.mp4), sticker lien au même endroit.
```

## Le message au client

Court. Ce qu'il a, où le mettre, comment demander une retouche :

> C'est prêt, tout est dans `livraison/` :
> - la vidéo de ta page de vente (avec son affiche) et la façon de la poser sur ta page ;
> - le Reel, sa version sans musique, sa couverture et sa légende.
>
> Une retouche ? Dis-la simplement, par exemple « laisse le prix affiché plus longtemps ».

Ne publie rien toi-même, n'envoie rien : la publication reste à lui.
