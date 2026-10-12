# Les vidéos d'une annonce

Tout est en **1080 × 1920, 30 images/s**. Chaque vidéo se comprend **sans le son** (beaucoup de
stories se regardent muettes) et a une seule mission. Les durées sont dans `tools/annonce.py`
(`VIDEOS`) : l'outil d'export refuse une vidéo hors bornes.

## Les zones de sécurité

`python3 tools/annonce.py zones reel` (ou `story`) donne les pixels exacts. Résumé v0.1 :

| | Haut | Bas | Gauche | Droite | Ce qui recouvre |
|---|---|---|---|---|---|
| Reel | 300 | 480 | 100 | 150 | En haut « Reels » et la caméra ; en bas le pseudo, la légende, le son ; à droite J'aime, commentaire, partage |
| Story | 270 | 290 | 80 | 80 | En haut la progression et le profil ; en bas « Envoyer un message » |

Tout texte qui compte (promesse, prix, date, mot-clé) tient **dans** la zone. Un décor, une
image de fond ou un mouvement peuvent déborder. Ces valeurs viennent des sources les plus
strictes ; si le client constate un recouvrement sur son téléphone, élargis la marge concernée
pour lui dans `annonce.config.json` (`zones`) et dis-le-lui.

**Le sticker lien** (stories ouverture, dernier jour, relance) : Instagram ne permet pas de le
poser dans la vidéo, le client l'ajoute en publiant. Réserve-lui la bande
`x 190 → 890, y 1180 → 1420` : **rien d'important dedans**, un fond calme, et une flèche ou une
phrase courte juste au-dessus (« Le lien est ici ↓ »). Dis au client où le poser.

## Le Reel d'annonce (15 à 30 s, 20 s visées)

Une seule promesse, une seule offre, un seul appel à l'action.

| Temps (pour 20 s) | Rôle | Règle |
|---|---|---|
| 0 → 2 s | **Accroche** | Mouvement dès la première image, promesse lisible avant 2 s, sans le son. 7 mots au plus |
| 2 → 8 s | **Le fil de l'angle** | Ce qu'on voit (résultat, avant/après, ce qu'on reçoit). Une idée par plan |
| ~8 s (40 %) | **Révélation de l'offre** | Nom, puis ce qu'on reçoit. Le temps fort de la musique tombe ici. 0,3 à 0,6 s de calme juste avant |
| 8 → 15 s | **Preuve et contenu** | Bonus, preuve de la fiche, prix si l'angle le montre |
| 15 → 20 s | **Écran final** | « Commente MOT » : le mot en grand, seule couleur d'accent, **immobile au moins 2,5 s**. Il rime avec l'accroche |

Texte : 5 mots au plus à l'écran à la fois, accroche sur 2 lignes au plus. Le mot ou le chiffre
vedette fait 120 px ou plus ; aucun texte sous 40 px. Le sujet principal se place entre 20 et
35 % de la hauteur (là où l'œil arrive), jamais collé au bas.

## Le Reel nouveauté (10 à 20 s, 14 s visées)

Accroche « Nouveau : … » (ou mieux, le bénéfice de la nouveauté), la nouveauté en action ou en
gros plan, où elle s'insère, l'appel à l'action. Pas de prix si la nouveauté est incluse.

## Les stories (5 à 12 s)

**Un seul mouvement principal par story** (environ 1,5 s), puis une tenue lisible. Jamais une
image figée plus de 2 s sans le moindre mouvement (une seule petite réaction suffit). Elles
reprennent le style du Reel et ses éléments, en plus simple.

| Story | Quand | Ce qu'elle fait | Sticker |
|---|---|---|---|
| **Teaser** (5 à 10 s) | La veille | Un bout de l'offre, flouté ou masqué, et « Demain, 18 h » si la date est réelle. Rien du prix | Non |
| **Ouverture** (6 à 12 s) | Jour J, juste après le Reel | « C'est ouvert » + l'offre en une ligne + le prix | **Oui** |
| **Relance** (5 à 10 s) | Au milieu | Un élément de l'offre (un bonus, une preuve) + rappel | **Oui** |
| **Dernier jour** (6 à 12 s) | Dernier jour, le matin | La vraie échéance (« Ferme ce soir minuit ») + ce que l'offre contient | **Oui**, et seulement si `dates.fermeture` existe |

Une story ne porte jamais de compte à rebours inventé : l'heure affichée est celle de la fiche.

## Les autres formats

Le client peut demander une version carrée (1080 × 1080) ou paysage (1920 × 1080) pour sa page de
vente, YouTube ou LinkedIn. C'est une **recomposition**, pas un recadrage : on replace les
éléments dans le nouveau cadre, on garde le rythme. Fais-la après la version verticale validée.
