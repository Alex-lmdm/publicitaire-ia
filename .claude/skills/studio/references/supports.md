# Les supports : où la vidéo sera vue

Le format de sortie suit le support. **Une même vidéo sur plusieurs supports = plusieurs mises
en page**, jamais un recadrage : on replace les éléments dans le nouveau cadre et on garde le
rythme. Fabrique d'abord la version du support principal, puis décline.

`python3 tools/studio_motion.py supports` donne les durées et formats ;
`python3 tools/studio_motion.py zones <support> [--format …]` la zone de texte sûre en pixels.

| Support | Format | Durée visée (bornes) | Son | Appel à l'action |
|---|---|---|---|---|
| `reel` Reel Instagram, Facebook | 9:16 | 20–45 s (7–90) | avec son, compréhensible sans | « Commente MOT », lien en bio |
| `tiktok` TikTok, YouTube Shorts | 9:16 | 20–35 s (7–180) | avec son | lien en bio, mot-clé en commentaire |
| `story` Story | 9:16 | 8–30 s (4–60) | souvent muette | sticker lien posé par le client, « réponds MOT » |
| `pub` Pub plein écran | 9:16 | 15–30 s (6–60) | avec son, compréhensible sans | bouton de la pub |
| `fil` Post ou pub dans le fil | 4:5 | 15–30 s (6–60) | souvent muet | bouton sous la vidéo, légende |
| `page` Haut de page de vente | 16:9 (`@1x1` ou `@4x5` pour le téléphone) | 60–120 s (20–300) | lecture auto **muette** | le bouton sous la vidéo |
| `section` Boucle dans une section | 16:9 | 10–25 s (6–45) | muette, en boucle | aucun dans la vidéo |
| `linkedin` LinkedIn | 4:5 | 30–90 s (10–600) | muette par défaut | dans le texte du post |
| `x` X | 16:9 (ou `@1x1`) | 20–60 s (6–140) | muette par défaut | dans le texte du post, URL au carton final |
| `youtube` YouTube, présentation | 16:9 | 60–180 s (20–900) | avec son | dans la vidéo et la description |

Les bornes sont dures : l'export refuse une vidéo hors bornes et prévient au-delà de la durée
visée. Une story s'arrête bien avant 30 s si tout est dit ; un Reel reste sous 45 s ; une vidéo de
page reste sous 2 minutes sauf si l'offre le demande vraiment.

## Les zones de sécurité

Tout texte important (promesse, prix, date, mot-clé, bouton dessiné) tient **dans** la zone.
Le décor peut déborder. La zone de chaque support et de chaque format, en pixels, c'est
`studio_motion.py zones`.

| Support | Haut | Bas | Gauche | Droite | Ce qui recouvre |
|---|---|---|---|---|---|
| `reel` | 15,6 % | 25 % | 9,3 % | 13,9 % | « Reels », caméra ; pseudo, légende, son ; colonne J'aime, commentaire, partage |
| `tiktok` | 13,2 % | 36,8 % | 11,3 % | 22,4 % | Onglets ; légende et son (très haut) ; colonne d'actions large |
| `story` | 14 % | 15 % | 7,4 % | 7,4 % | Progression et profil ; « Envoyer un message » |
| `pub` | 14 % | 35 % | 6 % | 6 % | En plus : le bouton et le texte de la pub en bas (zone officielle de Meta) |
| `fil`, `section` | 5 % | 5 % | 5 % | 5 % | Rien, marge de confort |
| `page`, `linkedin`, `x` | 5 à 6 % | 10 % | 5 % | 5 % | La barre du lecteur en bas |
| `youtube` | 8 % | 12 % | 5 % | 5 % | Titre au survol, barre du lecteur |

Un client qui publie la même vidéo en Reel ET sur TikTok : compose dans la zone `tiktok` (la plus
stricte), et centre le texte un peu à gauche.

**Sticker lien d'une story** (ouverture, relance, dernier jour, ou toute story qui renvoie vers
un lien) : réserve la bande `x 190 → 890, y 1180 → 1420`, fond calme, rien d'important dedans, et
une phrase courte juste au-dessus (« Le lien est ici ↓ »). Dis au client où le poser.

## Ce qui change selon le support

- **Page de vente (`page`)** : la vidéo démarre souvent en muet et en boucle, et l'économie
  d'énergie de l'iPhone peut bloquer la lecture automatique. Donc la **première image affiche
  déjà la promesse** (c'est aussi l'affiche), et chaque idée se lit à l'écran. Si la vidéo a une
  voix, des sous-titres incrustés en plus.
- **Section (`section`)** : une seule fonction, aucune piste son (`-an` à l'export), la dernière
  image raccorde avec la première. Fichier léger : vise moins de 0,5 Mo par seconde.
- **Pub (`pub`, `fil`)** : la proposition est lisible avant 3 s ; le prix n'apparaît pas (il fait
  baisser les clics) ; jamais de faux bouton dessiné dans le bas. Livre 3 accroches différentes
  sur le même corps quand le client veut tester.
- **LinkedIn, X** : lecture muette par défaut, ton plus sobre ; le problème métier et un résultat
  chiffré pèsent plus qu'une ambiance. Le texte du post porte l'appel à l'action.
- **Reel, TikTok** : la vente arrive à la fin seulement. Le mot-clé de l'écran final est celui
  de la légende.
- **Story** : un message par story ; une série se pense écran par écran (5 à 15 s chacun),
  chacun compréhensible seul.

## Sous-titres et texte (quand il y a une voix)

17 caractères par seconde au plus, 42 caractères par ligne au plus, 2 lignes au plus, chaque
groupe affiché au moins 0,7 s. Dans la zone de texte, jamais sur le bas d'un format vertical.
