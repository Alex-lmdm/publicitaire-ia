# Style n°6 · Nuée d'encre · d'après Kimi (https://x.com/Kimi_Moonshot/status/2081757327146045450)

**Ce qu'on voit :** sur une page claire, un aplat de la couleur claire de la marque, un coup de pinceau à l'encre de la marque se défait en une nuée de points qui cherche sa forme (trois traits, trois colonnes filaires, trois disques en gros pixels, trois points pleins, puis l'initiale de l'offre en points), puis une rafale de planches remplit la page : ses vraies images ou ses vrais mots, composés comme des planches d'imprimerie. Coupe sur la page vide : l'initiale qui change de forme, deux lignes « … Bientôt disponible. », le nom, le noir.
**Souvent utile pour :** un teaser (ouverture des inscriptions, nouvelle version, « bientôt disponible »), quand on veut faire monter l'attente sans rien montrer du produit.
**D'après :** X · Kimi (Moonshot AI), teaser de K3 · 15 s · 16:9 (1920 × 1080, 30 images par seconde).
**Mesures de l'original (`studio_motion.py reference`) :** 1,88 événement par seconde, écart médian 0,40 s, aucune image figée ; une coupe détectée (le noir final), plus la coupe franche de la page pleine vers la page vide, que l'outil ne compte pas (deux images claires).
**Mesures de l'essai du kit refait le 06/11/2026** (les 4 scènes bout à bout, 18,1 s, marque LMDM, sans choc de caméra, les lignes de fin tenues le temps de leur lecture) : en 16:9, 1,23 événement par seconde, écart médian 0,60 s ; en 9:16, 1,30 événement par seconde, écart médian 0,50 s ; aucune image figée, `rythme` et `palette` « ok » dans les deux formats.

> On reprend la grammaire de la vidéo, jamais son contenu : ni ses idéogrammes, ni ses gravures,
> ni sa photo de lune, ni son papier, ni son logo, ni son texte, ni sa musique. Le pinceau trace un
> geste universel (un cercle, un point) ; les planches montrent ses vraies images ou ses vrais mots,
> jamais un dessin inventé pour l'occasion.

## 1. Le rythme

- Rapide et continu : une forme toutes les 0,7 s environ, sans jamais s'arrêter. La nuée passe d'une forme à l'autre en 0,45 à 0,55 s ; chaque point part avec un petit retard (jusqu'à 0,22 s), ce qui donne l'effet de vol d'oiseaux.
- La musique (environ 116 battements par minute) marque un accent tous les quatre temps (2 s) ; elle se retient pendant la rafale de planches, puis frappe sur la coupe vers la page vide : c'est le moment de la révélation.
- Le contrôle `rythme` du studio compte les gros changements de lumière : des points fins sur une page claire bougent peu. Le kit le fait passer en grossissant et en densifiant la nuée (3 400 points de 3 à 8 px), en changeant de forme toutes les 0,75 s, en serrant la nuée d'un coup en trois points pleins et en faisant surgir les planches par salves : des événements de la matière, jamais de la caméra. Garde ces réglages. La caméra, elle, ne fait qu'avancer lentement pendant le geste : les cinq premières secondes se lisent sur une image stable (ni choc au point posé, ni sursaut à la numérisation, retirés du kit le 06/11/2026) ; n'ajoute jamais de coup de caméra pour le contrôle.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le coup de pinceau | un cercle à l'encre sèche en un geste, le point posé, la caméra qui avance lentement | accroche, temps fort | `coup-de-pinceau` |
| La numérisation | des colonnes de petits signes traversent l'encre, qui commence à se défaire | passage d'une idée à l'autre | `coup-de-pinceau` |
| La nuée qui cherche sa forme | des milliers de points qui prennent des formes l'une après l'autre, toujours par trois (traits, colonnes, disques, points pleins), puis l'initiale de l'offre | tension, les trois parties ou étapes de l'offre | `nuee-de-particules` |
| La rafale de planches | ses images ou ses mots, composés en planches d'imprimerie, qui remplissent la page en salves sur le tempo | crescendo, l'univers de son sujet, ce qu'on reçoit | `planches-en-rafale` |
| Le sigle qui change de forme | coupe sur la page vide, l'initiale qui change de forme tous les quarts de seconde | révélation du nom | `bientot` |
| Les deux lignes et le noir | le produit, puis « bientôt » ou la date réelle, le logotype, coupe au noir | offre, appel, fin | `bientot` |
| Le cadre d'imprimerie | des légendes dans les coins, des nombres qui défilent : une planche d'étude | toutes les scènes sur la page | `coup-de-pinceau`, `nuee-de-particules` |

C'est un style de teaser, sans geste de démonstration : une interface s'y montre en capture,
comme une planche en noir et blanc sur la page (`IMAGES` de la rafale), avec le cadre d'imprimerie.

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (c'est un teaser : il n'a pas de bloc « problème ») :

| Rôle | Temps (original) | Ce qui s'y passe |
|---|---|---|
| Accroche | 0 à 3 s | Un pinceau trace des caractères à l'encre sèche, en gros, sur la page. Le tracé se « numérise » (colonnes de petits signes) et commence à se défaire. |
| Tension | 3 à 9 s | Le tracé devient une nuée de points qui prend des formes l'une après l'autre, toujours par trois : traits, filets, colonnes en treillis, piliers de signes, arches en pixels, trois boules, trois sphères hérissées, une seule sphère, une lune. |
| Crescendo | 9 à 12 s | Autour de la lune, une rafale de gravures (instruments, machines, plantes, architecture) remplit toute la page. La musique se retient. |
| Révélation | 12 à 13 s | Coupe franche sur la page vide : le nom de la version change de forme tous les quarts de seconde. |
| Offre et appel | 13 à 15 s | Deux lignes posées au centre (le produit, puis « bientôt »), le logotype, coupe au noir. |

Le kit suit le même ordre en quatre scènes de 4,5 s, 5 s, 2,8 s et 5,6 s (section « Les compositions du kit »). Il en garde les gestes, jamais les images : les sphères et la lune deviennent trois points pleins et l'initiale de l'offre, les gravures ses vraies images ou ses mots.

## 3. Les fonds et les couleurs

Les couleurs sont celles de la marque, rien d'autre ([../../references/style.md](../../references/style.md),
« La palette ») : sa couleur la plus claire pour la page, sa plus sombre pour l'encre, un seul
détail à l'accent, posé plein.

| Rôle | Original | Chez le client |
|---|---|---|
| La page (fond de tout) | papier gris chaud, grain fin et fibres | un aplat de sa couleur claire, `var(--brand-clair)` (LMDM : blanc), avec un dégradé neutre à peine visible vers les bords (noir à 4,5 %) ; ni grain, ni fibres, ni texture |
| L'encre (pinceau, points, planches, textes) | noir | `var(--brand-sombre)`, sa couleur la plus sombre (sur une marque claire, la couleur de son texte), lue par le script sur la scène |
| La couleur | aucune | **un seul détail** à l'accent, plein : le troisième point du sigle final (et, au choix, le point posé par le pinceau, `accent: true`, dessiné sans transparence). Jamais de fond de couleur, jamais l'accent en transparence |
| Les gravures | planches au trait | ses vraies images (passées en noir et blanc) ou ses vrais mots, à l'encre ; un aplat d'encre porte son mot à la couleur de la page |
| Le noir final | noir | la même encre, `var(--brand-sombre)` |

Le look est monochrome : c'est sa force. Ne remplis pas une forme de couleur, ne mets pas de fond sombre au milieu.

**Sur n'importe quelle marque, claire ou sombre** : la page prend la plus claire de ses couleurs et l'encre la plus sombre (`--brand-clair`, `--brand-sombre`) ; jamais `var(--brand-bg)` ni `var(--brand-text)` (sur une marque sombre, son fond est foncé : la page deviendrait noire), jamais une couleur écrite dans le script. L'encre reste ainsi toujours foncée sur une page claire, et les deux lignes et le nom gardent un contraste d'au moins 4,5:1.

## 4. La typographie

- **Les légendes d'imprimerie** (coins de la page) : la police de texte de la marque, 11 px (9 px pour la petite ligne), un mot clé en gras et en capitales espacées (0,08 em), un filet fin ; en bas, six nombres de 11 px qui changent tous les quarts de seconde. Mêmes tailles en 1080 × 1920.
- **L'initiale en points** (scènes 2 et 3) : la police de titres de la marque, graisse 700, à 80 % de la hauteur du cadre (de la largeur en 9:16), écrite par 3 400 points.
- **Les planches de mots** (scène 3) : la police de titres, 600 dans un cadre fin, 700 sur un aplat d'encre ou dans une pilule (le mot à la couleur de la page), 800 seul sur un filet ; de 17 px à une soixantaine selon sa case ; un petit numéro (« N° 07 », 9 px) et des légendes (« fig. 2 », 11 px, en italique).
- **Le sigle** : l'initiale du nom de l'offre, 150 px, police de titres de la marque, en quatre états (fine 400, très grasse 900 avec trois barres, en contour, fine avec trois points).
- **Les deux lignes finales** : police de titres de la marque, graisse 600, 76 px, interligne 1,2, centrées, casse de la phrase, chacune finie par un point. Réduites seules à 80 % de la largeur (74 % en 9:16, la zone de texte d'un Reel).
- **Le nom** : police de titres de la marque, graisse 700, 104 px, en capitales, espacement 0,02 em (ou le logo, 120 px de haut).
- **Police libre la plus proche quand la marque n'impose rien :** l'original pose ses deux lignes dans une serif de titrage demi-grasse : **Source Serif 4** (graisse 600) pour les lignes et le sigle. `python3 tools/studio_motion.py police "Source Serif 4"` (depuis la racine), copie son fichier de `marque/polices/` dans `assets/fonts/` du projet, puis dans le style de la scène : `@font-face { font-family: "Source Serif 4"; font-weight: 600; font-display: block; src: url("assets/fonts/<son fichier>.woff2") format("woff2"); }` et `--t06-titres: "Source Serif 4", var(--brand-font-display);`. Le nom reste dans la police de la marque. Une initiale en points dessinée dans cette serif se règle dans les scènes 2 et 3 à la fois (même `--t06-titres`).

## 5. Les mouvements signature

Tous sont dans `compositions/`.

1. **Le coup de pinceau** (scène 1). Un seul geste en deux élans (0,45 s puis 0,6 s) : une tête ronde où le pinceau se pose, 150 poils qui portent l'encre et sèchent le long du geste (la page passe dans la queue), puis un point posé en 0,22 s ; la caméra avance lentement pendant tout le geste (×1,02 → ×1,05, sine.inOut), sans choc.
2. **La numérisation** (scène 1). Des colonnes de petits signes, couleur de la page, traversent l'encre (redistribuées douze fois par seconde) ; la page reste stable (le sursaut de côté de l'original n'est pas repris : c'est le début de la vidéo).
3. **La nuée qui cherche sa forme** (scènes 1 et 2). L'encre devient 3 400 points qui tournent dans le sens du geste (deux poussées), s'aplatissent en bande, puis prennent les formes une à une : trois traits, trois colonnes en treillis qui tournent (12 anneaux de 10 nœuds, fils fins), trois disques en gros pixels (les points se calent sur une grille de 15 px), trois points serrés qui deviennent d'un coup trois disques pleins (0,26 s : les points de suspension), puis l'initiale de l'offre écrite en points, qui respire (+6 % en 0,4 s) et frémit. Passage : 0,45 à 0,55 s, power3.inOut, avec un léger bombé.
4. **La rafale de planches** (scène 3). Une trentaine de planches, une par case d'une grille de 8 × 5 (5 × 9 en 9:16) tenue dans une marge, l'initiale gardant sa place, surgissent en cinq salves sur le tempo (0,42 s d'écart), du centre vers les bords : chacune se pose en 0,16 s (back.out), son cadre se dessine en 0,32 s, son mot s'écrit de gauche à droite en 0,3 s. Une planche, c'est une de ses images (en noir et blanc, dans un cadre fin) ou un de ses mots : dans un cadre, sur un aplat d'encre, dans une pilule, seul sur un filet ; quelques disques pleins ponctuent. Aucune ne déborde de sa case ni du cadre. La caméra recule de 14 % pendant 2,2 s.
5. **Le sigle qui change de forme** (scène 4). Coupes franches tous les 0,24 s : l'initiale fine, puis très grasse avec trois barres, puis en contour, puis fine avec trois points qui arrivent un à un (le dernier à l'accent).
6. **Le cadre d'imprimerie** (scènes 1 et 2). Petites légendes dans les coins et nombres qui défilent en bas : la page a l'air d'une planche d'étude. Le cadre s'efface quand l'initiale se forme.

## 6. Les transitions

- Aucune coupe du pinceau à l'initiale : tout est une seule matière qui se transforme (l'encre devient points, les points deviennent formes, les formes une lettre).
- Une coupe franche, une seule, sur le temps fort : la page pleine de planches devient la page vide. Puis des coupes franches courtes dans la révélation (sigle, lignes, nom) et la coupe au noir.
- Raccords du kit : la scène 2 part de la bande de la scène 1 (mêmes points, même graine), la scène 3 de l'initiale de la scène 2 (même tirage de points, elle continue de frémir).

## 7. Le produit à l'écran

- L'original ne montre rien du produit : c'est un teaser. Le chiffre de la version (le trois) structure tout : trois traits, trois colonnes, trois sphères, trois points.
- Chez le client : on ne montre pas son offre non plus. Le trois peut devenir un vrai nombre de l'offre (trois modules, trois étapes) ; jamais un chiffre affiché qui n'est pas dans OFFRE.json. Les planches laissent deviner son univers avec sa vraie matière : ses images (`IMAGES` : ses croquis, ses captures de page ou de produit, fournis au moment de faire sa vidéo), sinon ses vrais mots (`MOTS` : ses formats, ses modules, ses outils, tirés de OFFRE.json ou de sa page). Jamais un dessin, une gravure, une texture ou une sphère dessinés pour l'occasion ; sans images ni mots, la rafale se retire.

## 8. Le son

- Original : une musique électronique sourde et régulière (environ 116 battements par minute), un accent tous les quatre temps (toutes les 2 s), le son qui se retient pendant la rafale, puis une frappe nette sur la coupe vers la page vide et un dernier accent sur le logotype.
- Chez le client : une musique qui monte puis frappe, et **jamais plus d'une seconde de silence au début de la vidéo**. La coupe vers la page vide tombe vers 12 à 13,5 s, alors que les morceaux de l'ambiance « Montée cinématique » n'ont que 3,5 à 8,5 s d'intro : caler leur batterie sur la coupe ferait démarrer la musique 4 à 9 s après l'image, et le teaser resterait muet au début. Deux façons justes, depuis le projet de la vidéo :
  1. **Un morceau dont l'intro couvre la coupe.** `python3 ../../../tools/studio_motion.py musiques choisir --a <instant de la coupe> --duree <durée de la vidéo>` (sans imposer d'ambiance) classe d'abord les morceaux dont la batterie entre à la coupe ou après ; il écrit « démarre … s après le début (intro courte) » pour les autres : écarte ceux où ce retard dépasse une seconde. Puis `musiques prendre <n> --a <instant de la coupe> --duree <durée>` : la batterie frappe sur la révélation.
  2. **Un morceau à l'intro courte** (il préfère une « Montée cinématique ») : la musique part à 0 et la batterie entre où elle entre, `musiques prendre <n> --a <instant de sa batterie> --duree <durée>` (l'instant que `musiques choisir` écrit après « batterie à »). La coupe vers la page vide garde alors son coup sourd (bruitage ci-dessous) pour frapper.
  Après le rendu, écoute le début ou mesure-le (`ffmpeg -i <mp4> -af silencedetect=n=-45dB:d=1 -f null -` ne doit signaler aucun silence qui commence à 0).
- Bruitages : un frottement de pinceau sur le geste, un grésillement bref sur la numérisation, un souffle léger pendant la nuée, un coup net sur les trois points pleins, de petits clics de papier sur les salves de planches, un coup sourd sur la coupe, rien sur le noir final.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 6`) : « Montée cinématique », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture :** la page et son cadre sont là dès la première image, le pinceau part à 0,1 s : on voit tout de suite une main qui trace.
- **Fin :** le sigle (1,2 s), les deux lignes (la deuxième 0,5 s après la première), tenues ensemble le temps de leur lecture (`studio_motion.py lecture` : 2 s pour quatre mots, la scène la calcule), le nom 1,5 s au moins, puis 0,3 s de noir. La deuxième ligne dit quand ou où (« Bientôt disponible. », ou une vraie date de la fiche) ; un appel plus direct (« Inscris-toi sur la liste ») se met à sa place si la page le permet.

## Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas.** La lune photographique et les sphères deviennent trois points pleins puis l'initiale de l'offre en points ; les gravures anciennes, ses vraies images (ses croquis, ses captures, en noir et blanc) ou ses vrais mots composés en planches. Jamais une gravure, une sphère, une lune ou une texture dessinées par le script.
- **Le papier** (gris chaud, grain, fibres) : un aplat de sa couleur claire.
- Les idéogrammes au pinceau : un cercle et un point (un geste universel, réglable par ses points).
- Les piliers de signes et les arches tramées : trois disques en gros pixels.
- Le logotype « K2, K3, KIII » : l'initiale de l'offre avec trois barres puis trois points.
- Les légendes de l'original : des légendes génériques en français (à remplacer).
- Le noir et blanc pur : la page et l'encre sont la plus claire et la plus sombre de ses couleurs, un seul point prend son accent.
- La durée : 17,9 s au lieu de 15 s (les lignes de fin tenues le temps de leur lecture).

## Sur une autre offre

- **Formation :** le trois devient ses trois modules ou ses trois étapes ; les planches, ses croquis ou ses captures (`IMAGES`), sinon les titres de ses modules (`MOTS`) ; les lignes : « Ta formation. » puis « Ouverture le 12 janvier. » (date réelle seulement).
- **Coaching :** le cercle au pinceau parle tout seul (calme, clarté) ; les planches, les mots de sa méthode (ses étapes, ses thèmes) ; les lignes : le nom du programme, puis « Bientôt les inscriptions. ».
- **Logiciel :** les planches peuvent être ses écrans ou ses schémas passés en noir et blanc (`IMAGES`) ; le sigle, l'initiale du logiciel ; les lignes : le nom, puis « Bientôt en accès anticipé. ».
- **Toujours :** la page claire, le pinceau, la nuée qui change de forme par trois, la rafale qui remplit la page, la coupe sur la page vide, le noir final.

## En vertical et en carré

- **9:16 (essayé en 1080 × 1920, marque LMDM, 06/11/2026) :** les quatre scènes se remettent en page seules (change `data-width` et `data-height` de leur racine). Le cercle reste entier, les formes par trois s'empilent en hauteur (traits, pixels, points pleins), les colonnes restent côte à côte en plus haut, l'initiale reste au centre, la grille des planches passe à 5 colonnes sur 9 rangs (ses mots des bords peuvent passer sous l'interface d'un Reel : c'est une texture, rien d'important), la fin reste centrée.
- **Carré et 4:5 :** même mise en page que le 16:9 (formes en ligne), qui se resserre ; vérifie que la troisième forme ne touche pas le bord et que les légendes du bas restent hors de la bande du sticker.

## Les compositions du kit

Montées bout à bout dans cet ordre, elles raccordent image pour image (17,9 s avec les textes d'exemple) ; chacune vit aussi seule (la scène 2 et la scène 3 commencent alors sur la bande et sur l'initiale). Les couleurs ne viennent que des jetons de la palette (`var(--brand-clair)`, `var(--brand-sombre)`, l'accent plein), lus par le script sur la scène.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/coup-de-pinceau.html` | 4,5 s | la page et son cadre, le cercle au pinceau, le point, la numérisation, la nuée qui tourne et se pose en bande | LEGENDES, GESTES (le tracé ; `accent: true` pose le point à l'accent, plein) |
| `compositions/nuee-de-particules.html` | 5 s | la bande qui devient trois traits, trois colonnes en treillis, trois disques en pixels, trois points pleins, puis son initiale en points | LEGENDES (les mêmes), INITIALE, l'ordre et les temps des FORMES |
| `compositions/planches-en-rafale.html` | 2,8 s | l'initiale au centre, cinq salves de planches (ses images ou ses mots) qui remplissent la page | IMAGES (ses vraies images, dans `assets/images/`), MOTS (ses vrais mots), INITIALE (la même), LEGENDES_FIG |
| `compositions/bientot.html` | 5,6 s (deux lignes de 4 mots ; la scène calcule sa durée d'après ses lignes et son nom) | la page vide, le sigle qui change de forme, les deux lignes, le nom, le noir | NOM, LIGNES, LOGO |
