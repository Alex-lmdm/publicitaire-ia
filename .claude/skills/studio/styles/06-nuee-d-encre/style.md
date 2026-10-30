# Template n°6 · Nuée d'encre · d'après Kimi (https://x.com/Kimi_Moonshot/status/2081757327146045450)

**Ce qu'on voit :** sur une page de papier gris chaud, un coup de pinceau à l'encre se défait en une nuée de points qui cherche sa forme (trois traits, trois colonnes filaires, trois disques en gros pixels, trois sphères hérissées, une lune au crayon), puis une rafale de planches de gravure remplit la page. Coupe sur la page vide : l'initiale qui change de forme, deux lignes « … Bientôt disponible. », le nom, le noir.
**Souvent utile pour :** un teaser (ouverture des inscriptions, nouvelle version, « bientôt disponible »), quand on veut faire monter l'attente sans rien montrer du produit.
**D'après :** X · Kimi (Moonshot AI), teaser de K3 · 15 s · 16:9 (1920 × 1080, 30 images par seconde).
**Mesures de l'original (`studio_motion.py reference`) :** 1,88 événement par seconde, écart médian 0,40 s, aucune image figée ; une coupe détectée (le noir final), plus la coupe franche des gravures vers la page vide, que l'outil ne compte pas (deux images claires).
**Mesures du kit monté (les 4 scènes bout à bout, 16,1 s, marque de test) :** `rythme` répond « ok » : 1,52 événement par seconde, écart médian 0,60 s, aucune image figée.

> On reprend la grammaire de la vidéo, jamais son contenu : ni ses idéogrammes, ni ses gravures,
> ni sa photo de lune, ni son logo, ni son texte, ni sa musique. Le pinceau trace un geste
> universel (un cercle, un point), les planches sont dessinées par le script.

## 1. Le rythme

- Rapide et continu : une forme toutes les 0,7 s environ, sans jamais s'arrêter. La nuée passe d'une forme à l'autre en 0,45 à 0,55 s ; chaque point part avec un petit retard (jusqu'à 0,22 s), ce qui donne l'effet de vol d'oiseaux.
- La musique (environ 116 battements par minute) marque un accent tous les quatre temps (2 s) ; elle se retient pendant la rafale de gravures, puis frappe sur la coupe vers la page vide : c'est le moment de la révélation.
- Le contrôle `rythme` du studio compte les gros changements de lumière : des points fins sur du papier clair bougent peu. Le kit le fait passer en grossissant et en densifiant la nuée (3 400 points de 3 à 8 px), en changeant de forme toutes les 0,75 s, en donnant de petits coups de caméra (le point posé, la numérisation) et en faisant surgir les gravures par salves. Garde ces réglages.

## 2. La structure

| Rôle | Temps (original) | Ce qui s'y passe |
|---|---|---|
| Accroche | 0 à 3 s | Un pinceau trace des caractères à l'encre sèche, en gros, sur la page. Le tracé se « numérise » (colonnes de petits signes) et commence à se défaire. |
| Tension | 3 à 9 s | Le tracé devient une nuée de points qui prend des formes l'une après l'autre, toujours par trois : traits, filets, colonnes en treillis, piliers de signes, arches en pixels, trois boules, trois sphères hérissées, une seule sphère, une lune. |
| Crescendo | 9 à 12 s | Autour de la lune, une rafale de gravures (instruments, machines, plantes, architecture) remplit toute la page. La musique se retient. |
| Révélation | 12 à 13 s | Coupe franche sur la page vide : le nom de la version change de forme tous les quarts de seconde. |
| Offre et appel | 13 à 15 s | Deux lignes posées au centre (le produit, puis « bientôt »), le logotype, coupe au noir. |

Le kit suit le même ordre en quatre scènes de 4,5 s, 5 s, 2,8 s et 3,8 s (section « Les compositions du kit »). Pas de bloc « problème » : c'est un teaser.

## 3. Les fonds et les couleurs

| Rôle | Original | Chez le client |
|---|---|---|
| La page (fond de tout) | papier gris chaud #E3E4DE, grain fin et fibres | gardé, c'est le look : `--t06-papier` (les fibres et le grain sont dessinés par le script) |
| L'encre (pinceau, points, gravures, textes) | noir | la couleur sombre de la marque si elle en a une (son fond, s'il est foncé), sinon un noir d'encre : réglé tout seul |
| La couleur | aucune | **un seul détail** à l'accent de la marque : le troisième point du sigle final (et, au choix, un geste du pinceau marqué `accent: true`). Jamais de fond de couleur |
| Le noir final | noir | la même encre (le fond foncé de la marque) |

Le look est monochrome : c'est sa force. Ne remplis pas une forme de couleur, ne mets pas de fond sombre au milieu.

## 4. La typographie

- **Les légendes d'imprimerie** (coins de la page) : la police de texte de la marque, 11 px (9 px pour la petite ligne), un mot clé en gras et en capitales espacées (0,08 em), un filet fin ; en bas, six nombres de 11 px qui changent tous les quarts de seconde. Mêmes tailles en 1080 × 1920.
- **Le sigle** : l'initiale du nom de l'offre, 150 px, police de titres de la marque, en quatre états (fine 400, très grasse 900 avec trois barres, en contour, fine avec trois points).
- **Les deux lignes finales** : police de titres de la marque, graisse 600, 76 px, interligne 1,2, centrées, casse de la phrase, chacune finie par un point. Réduites seules à 80 % de la largeur (en 9:16 surtout).
- **Le nom** : police de titres de la marque, graisse 700, 104 px, en capitales, espacement 0,02 em (ou le logo, 120 px de haut).
- **Police libre la plus proche quand la marque n'impose rien :** l'original pose ses deux lignes dans une serif de titrage demi-grasse : **Source Serif 4** (graisse 600) pour les lignes et le sigle. `python3 tools/studio_motion.py police "Source Serif 4"` (depuis la racine), copie son fichier de `marque/polices/` dans `assets/fonts/` du projet, puis dans le style de la scène : `@font-face { font-family: "Source Serif 4"; font-weight: 600; font-display: block; src: url("assets/fonts/<son fichier>.woff2") format("woff2"); }` et `--t06-titres: "Source Serif 4", var(--brand-font-display);`. Le nom reste dans la police de la marque.

## 5. Les mouvements signature

Tous sont dans `compositions/`.

1. **Le coup de pinceau** (scène 1). Un seul geste en deux élans (0,45 s puis 0,6 s) : une tête ronde où le pinceau se pose, 150 poils qui portent l'encre et sèchent le long du geste (le papier passe dans la queue), puis un point posé en 0,22 s avec un petit choc de caméra (+3,5 % en 0,09 s, retour en 0,45 s).
2. **La numérisation** (scène 1). Des colonnes de petits signes, couleur du papier, traversent l'encre (redistribuées douze fois par seconde) ; la page fait un sursaut de côté (14 px, puis -9 px, en 0,11 s).
3. **La nuée qui cherche sa forme** (scènes 1 et 2). L'encre devient 3 400 points qui tournent dans le sens du geste (deux poussées), s'aplatissent en bande, puis prennent les formes une à une : trois traits, trois colonnes en treillis qui tournent (12 anneaux de 10 nœuds, fils fins), trois disques en gros pixels (les points se calent sur une grille de 15 px), trois sphères hérissées (rayons fins depuis le centre), une seule sphère ombrée comme une lune au crayon (lumière en haut à droite), qui tourne et respire. Passage : 0,45 à 0,55 s, power3.inOut, avec un léger bombé.
4. **La rafale de gravures** (scène 3). Une cinquantaine de planches au trait (globe filaire, spirale, rose des vents, relief en treillis, escalier en hélice, engrenage, orbites, polyèdre, tore, pendule, éventail, sphère hachurée, parabole, cube, onde, pylône) surgissent en cinq salves sur le tempo (0,42 s d'écart), du centre vers les bords : chacune se pose en 0,16 s (back.out) et ses traits se dessinent en 0,32 s ; la caméra recule de 14 % pendant 2,2 s.
5. **Le sigle qui change de forme** (scène 4). Coupes franches tous les 0,24 s : l'initiale fine, puis très grasse avec trois barres, puis en contour, puis fine avec trois points qui arrivent un à un (le dernier à l'accent).
6. **Le cadre d'imprimerie** (scènes 1 et 2). Petites légendes dans les coins et nombres qui défilent en bas : la page a l'air d'une planche d'étude. Le cadre s'efface quand la sphère se forme.

## 6. Les transitions

- Aucune coupe du pinceau à la lune : tout est une seule matière qui se transforme (l'encre devient points, les points deviennent formes).
- Une coupe franche, une seule, sur le temps fort : la page pleine de gravures devient la page vide. Puis des coupes franches courtes dans la révélation (sigle, lignes, nom) et la coupe au noir.
- Raccords du kit : la scène 2 part de la bande de la scène 1 (mêmes points, même graine), la scène 3 de la sphère de la scène 2 (elle continue de tourner).

## 7. Le produit à l'écran

- L'original ne montre rien du produit : c'est un teaser. Le chiffre de la version (le trois) structure tout : trois traits, trois colonnes, trois sphères, trois points.
- Chez le client : on ne montre pas son offre non plus. Le trois peut devenir un vrai nombre de l'offre (trois modules, trois étapes) ; jamais un chiffre affiché qui n'est pas dans OFFRE.json. Ses propres dessins, croquis ou captures en noir et blanc peuvent prendre la place des planches de gravure (IMAGES, scène 3) : c'est la façon de laisser deviner son univers.

## 8. Le son

- Original : une musique électronique sourde et régulière (environ 116 battements par minute), un accent tous les quatre temps (toutes les 2 s), le son qui se retient pendant les gravures, puis une frappe nette sur la coupe vers la page vide et un dernier accent sur le logotype.
- Chez le client : une musique qui monte puis frappe (`musiques choisir --ambiance "Montée cinématique"`), calée pour que son entrée franche tombe sur la coupe vers la page vide (`musiques prendre <n> --a <instant de la coupe>`). Bruitages : un frottement de pinceau sur le geste, un grésillement bref sur la numérisation, un souffle léger pendant la nuée, de petits clics de papier sur les salves de gravures, un coup sourd sur la coupe, rien sur le noir final.

## 9. L'ouverture et la fin

- **Ouverture :** la page et son cadre sont là dès la première image, le pinceau part à 0,1 s : on voit tout de suite une main qui trace.
- **Fin :** le sigle (1,2 s), les deux lignes (1,3 s, la deuxième 0,5 s après la première), le nom (0,8 s), puis 0,3 s de noir. La deuxième ligne dit quand ou où (« Bientôt disponible. », ou une vraie date de la fiche) ; un appel plus direct (« Inscris-toi sur la liste ») se met à sa place si la page le permet.

## Ce qui ne se fera pas à l'identique

- Les idéogrammes au pinceau : un cercle et un point (un geste universel, réglable par ses points).
- La lune photographique : une sphère en pointillé ombrée.
- Les gravures anciennes : des planches au trait dessinées par le script (ou les illustrations libres du client) ; moins riches que de vraies gravures, sans photo.
- Les piliers de signes et les arches tramées : trois disques en gros pixels.
- Le logotype « K2, K3, KIII » : l'initiale de l'offre avec trois barres puis trois points.
- Les légendes de l'original : des légendes génériques en français (à remplacer).
- Le noir et blanc pur : l'encre prend la couleur sombre de la marque, un seul point prend son accent.
- La durée : 16,1 s au lieu de 15 s.

## Sur une autre offre

- **Formation :** le trois devient ses trois modules ou ses trois étapes ; les planches, des croquis de ses thèmes (fournis par le client) ; les lignes : « Ta formation. » puis « Ouverture le 12 janvier. » (date réelle seulement).
- **Coaching :** le cercle au pinceau parle tout seul (calme, clarté) ; les planches peuvent rester générées ; les lignes : le nom du programme, puis « Bientôt les inscriptions. ».
- **Logiciel :** les planches peuvent être ses schémas ou ses écrans passés en noir et blanc (IMAGES) ; le sigle, l'initiale du logiciel ; les lignes : le nom, puis « Bientôt en accès anticipé. ».
- **Toujours :** le papier, le pinceau, la nuée qui change de forme par trois, la rafale qui remplit la page, la coupe sur la page vide, le noir final.

## En vertical et en carré

- **9:16 (essayé en 1080 × 1920) :** les quatre scènes se remettent en page seules (change `data-width` et `data-height` de leur racine). Le cercle reste entier, les formes par trois s'empilent en hauteur (traits, pixels, sphères), les colonnes restent côte à côte en plus haut, la grille des gravures passe à 6 colonnes sur 11 rangs, la fin reste centrée.
- **Carré et 4:5 :** même mise en page que le 16:9 (formes en ligne), qui se resserre ; vérifie que la troisième forme ne touche pas le bord et que les légendes du bas restent hors de la bande du sticker.

## Les compositions du kit

Montées bout à bout dans cet ordre, elles raccordent image pour image (16,1 s) ; chacune vit aussi seule (la scène 2 et la scène 3 commencent alors sur la bande et sur la sphère).

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/coup-de-pinceau.html` | 4,5 s | la page et son cadre, le cercle au pinceau, le point, la numérisation, la nuée qui tourne et se pose en bande | LEGENDES, GESTES (le tracé), la couleur du papier |
| `compositions/nuee-de-particules.html` | 5 s | la bande qui devient trois traits, trois colonnes en treillis, trois disques en pixels, trois sphères hérissées, puis une lune | LEGENDES (les mêmes), l'ordre et les temps des FORMES |
| `compositions/gravures-en-rafale.html` | 2,8 s | la lune au centre, cinq salves de planches de gravure qui remplissent la page | IMAGES (ses illustrations), LEGENDES_FIG |
| `compositions/bientot.html` | 3,8 s | la page vide, le sigle qui change de forme, les deux lignes, le nom, le noir | NOM, LIGNES, LOGO |
