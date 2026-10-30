# La marque du client : une question, puis sa validation

Ses vidéos portent sa marque : ses couleurs, ses polices, son logo. Elle se règle **une seule
fois**, au premier `/studio`, et vit dans `marque.json` à la racine du dossier. Tout le reste
(`brand/tokens.css`, `brand/fonts.css`, la copie dans chaque vidéo, la vignette d'accueil de l'app)
en est généré. Il ne choisit jamais un code couleur ni un nom de police : il valide ce que tu lui
montres.

## 1. La question (dans le message de bienvenue, voir `brief.md`)

> **Ta marque (couleurs, polices, logo) : je la prends où ?**
> a) sur ta page de vente : colle son lien (le plus simple) ·
> b) sur des images ou des captures de ta marque : glisse-les ici ·
> c) sur une vidéo dont tu aimes le style : son lien, ou le fichier ·
> d) j'ai Monteur IA : je reprends ses réglages (dis-moi où est son dossier)

Recommande **a** s'il a une page. Depuis la racine du dossier :

| Réponse | Commande | Ce qu'elle fait |
|---|---|---|
| a | `python3 tools/studio_motion.py marque page "<lien>"` | Lit la page et ses feuilles de style, puis la capture (1 à 2 minutes) : nom (celui que le site se donne, le texte de son logo, sinon son domaine, jamais le titre de la page), fond, couleur de la marque (celle de ses boutons d'action, de ses liens et de son logo, avant les couleurs de décor), polices des titres et du texte, logo (icône du site si la page n'a pas de logo) |
| b | `python3 tools/studio_motion.py marque images "<image>" "<image>"…` | Mesure la palette des images (fond, couleur de la marque) |
| c | `python3 tools/studio_motion.py marque video "<lien ou fichier>"` | Mesure la palette de la vidéo et écrit sa planche (`marque/video/planche.jpg`) |
| d | `python3 tools/studio_motion.py marque monteur "<dossier Monteur IA>"` | Reprend couleurs, polices, nom, mot-clé, musique et logo de ses Reels, sans rien écrire dans son dossier |

Dis-lui ce qui se passe en une phrase (« Je lis ta page, une à deux minutes. Tu n'as rien à
faire. »). Un échec (page protégée, lien mort) se dit simplement, avec l'autre chemin : « Ta page
ne se laisse pas lire. Glisse-moi deux captures d'écran, ça suffit. »

**b et c : les polices.** Une palette se mesure, une police se reconnaît à l'œil. Regarde les
images (ou la planche) et nomme la police la plus proche parmi les polices libres que tu connais
(Montserrat, Poppins, Inter, Bebas Neue, Archivo Black, Playfair Display, DM Sans…), puis :

```bash
python3 tools/studio_motion.py marque regler --titres "Montserrat" --corps "Inter"
```

L'outil la télécharge depuis Google Fonts (polices libres). Dans le doute, garde celles de départ
et dis-le.

**c : le style.** La vidéo sert deux fois : ici pour la marque, puis à chaque vidéo pour le
rythme et les procédés (`studio_motion.py reference`, étape 2 bis du skill). Note son lien dans
`studio.config.json` (`reference_style`).

**d : où est son dossier ?** S'il ne sait pas, cherche dans son dossier personnel (trois niveaux
au plus) un dossier qui contient `templates/AGENT.md.tpl` et `brand.config.json`, et
propose-le. Tu ne modifies **jamais** rien dans ce dossier : tu le lis. S'il y a installé le
Pack SFX (l'outil le signale), propose de le reprendre aussi : `pack-sfx reprendre` le copie dans
ce dossier (`son.md`, section « Le Pack SFX »).

## 2. La montrer et la faire valider

L'outil écrit `marque.json`, régénère le style, et affiche :

- le résumé (nom, fond, couleur de la marque, texte, polices, logo) ;
- comment il l'a lue (une ligne par décision : « fond #202022 : fond de la première section ») ;
- l'aperçu `marque/apercu.png` (la vignette d'accueil : pastilles de couleur, « Aa » dans chaque
  police, logo). Regarde-le toi-même avant de le montrer. Dans l'app HyperFrames, la vignette
  d'accueil le montre aussi.

Puis un message court, sans code couleur sauf s'il en parle :

> Voici ta marque telle que je la lis sur ta page : fond **anthracite**, couleur de marque
> **jaune vif**, titres et texte en **Poppins**, et ton logo. (aperçu : marque/apercu.png)
> C'est bien toi ? Réponds « ok », ou dis-moi ce qui cloche (« le jaune est plus doux »,
> « mon logo est sur fond blanc »…).

Ses retours se traduisent en `marque regler` (`--fond`, `--accent`, `--texte`, `--secondaire`,
`--titres`, `--corps`, `--nom`, `--mot-cle`, `--logo <fichier>`), puis tu remontres l'aperçu.
Quand il dit « ok » : `python3 tools/studio_motion.py marque valider`. Une marque non validée
n'empêche pas de travailler, mais ne fabrique pas sa première vidéo sans sa réponse.

## Plus tard

- « Change ma couleur », « prends ma nouvelle police », « voici mon logo » : `marque regler`, puis
  `marque` pour remontrer. Les vidéos déjà créées gardent leur style ; une nouvelle vidéo part
  avec la marque à jour.
- Une autre source (« reprends tout depuis ma nouvelle page ») : la commande de la source, la
  précédente est gardée dans `marque/precedente.json`.
- `python3 tools/studio_motion.py marque` seul montre la marque actuelle.

## Ce qu'on ne fait jamais

- Reprendre la police d'une page sans le dire : l'outil préfère la version libre (Google Fonts) ;
  s'il a dû prendre les fichiers de sa page, il le note, et tu dis au client qu'une police achetée
  peut demander une licence vidéo.
- Prendre le logo d'un outil tiers (Instagram, Claude, Stripe…) pour le sien : l'outil les écarte ;
  si le seul logo trouvé est son icône de site, dis-le et demande s'il en a un plus grand.
- Écrire dans son dossier Monteur IA, ou y lancer une commande qui le modifie.
