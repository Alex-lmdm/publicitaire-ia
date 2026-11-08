# Style n°6 · Nuée d'encre · d'après Kimi (https://x.com/Kimi_Moonshot/status/2081757327146045450)

**Ce qu'on voit :** sur une page claire, un pinceau trace un cercle d'encre autour des mots de l'accroche et pose le point qui les finit ; le cercle et ses mots se défont en une nuée de points qui écrit les trois mots de l'offre, puis l'initiale de son nom ; une rafale de planches (ses vrais mots ou ses vraies images) remplit la page autour d'elle. Coupe sur la page vide : l'initiale qui change de forme, deux lignes « … Bientôt disponible. », le nom, le noir.
**Souvent utile pour :** un teaser (ouverture des inscriptions, nouvelle version, « bientôt disponible »), pour faire monter l'attente sans démonstration.
**D'après :** X · Kimi (Moonshot AI), teaser de K3 · 15 s · 16:9 (1920 × 1080, 30 images par seconde).
**La règle du style :** la nuée n'est jamais un décor. Chaque point naît d'une encre réellement posée (le cercle, des mots, un trait) et va écrire une vraie matière (ses mots, l'initiale de son nom) ; leur nombre vient du sujet (une place par case d'encre), jamais d'un effet. Une nuée qui n'écrit rien, une forme de points, un disque ou une sphère se retirent.

## 1. Le rythme

- Rapide et continu : un événement toutes les 0,5 s environ (le cercle, les mots, le point, la numérisation, chaque mot écrit puis posé, le trait qui souligne, les salves). Un passage de la nuée dure 0,5 à 0,55 s ; chaque point part avec un retard jusqu'à 0,22 s : le vol d'oiseaux.
- Les mots se lisent pendant que la matière vit autour : l'accroche reste dans son cercle plus de 2 s, les trois mots ensemble 0,8 s + 0,3 s par mot après le dernier posé (la scène le calcule) ; la nuée ne repart qu'ensuite.
- La musique (environ 116 battements par minute) marque un accent tous les 2 s, se retient pendant la rafale, puis frappe sur la coupe vers la page vide.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le cercle au pinceau | un cercle d'encre sèche autour de l'accroche ; le point du pinceau finit la phrase | accroche, temps fort | `coup-de-pinceau` |
| La numérisation | des colonnes de petits signes traversent l'encre et les mots ; des mots qui passent en gros pixels | passage d'une idée à l'autre | `coup-de-pinceau`, `nuee-de-particules` |
| La nuée qui écrit | l'encre défaite vole et écrit les mots suivants, un à un, chacun posé d'un coup en encre pleine ; le pinceau souligne le mot clé | tension, les parties ou étapes de l'offre | `nuee-de-particules` |
| L'initiale en points | les points des mots se rassemblent en l'initiale de son nom, qui respire | le mystère avant le nom | `nuee-de-particules`, `planches-en-rafale` |
| La rafale de planches | ses images ou ses mots en planches d'imprimerie, en salves sur le tempo autour de l'initiale | crescendo, l'univers de son offre | `planches-en-rafale` |
| Le sigle qui change de forme | coupe sur la page vide, l'initiale en grand change de forme tous les quarts de seconde, puis ses points de suspension | révélation du nom | `bientot` |
| Les deux lignes et le noir | le produit, puis « bientôt » ou la date réelle, le nom ou le logo, coupe au noir | offre, appel, fin | `bientot` |
| Le cadre d'imprimerie | légendes dans les coins, nombres qui défilent : une texture jamais lue | les scènes sur la page | `coup-de-pinceau`, `nuee-de-particules` |

Un style de teaser, sans démonstration : une interface s'y montre en capture, planche en noir et blanc de la rafale (`images`).

## 3. Les fonds et les couleurs

**Les objets connus gardent leurs vraies couleurs**, dans ce style comme dans tous les autres : tout
ce que son public reconnaît d'un coup d'œil, par exemple le dossier bleu du Mac et les fichiers du
kit (`K.ic("objet-…")`), le téléphone et ses notifications, les vrais logos de ses outils,
l'interface d'une plateforme, un objet de son métier. Ce sont les touches de couleur vraie du
film ; tout le reste prend les rôles ci-dessous ([image.md](../../references/image.md), « Les
objets connus »).

Rien que la marque ([image.md](../../references/image.md), « La palette ») :

| Rôle | Chez le client |
|---|---|
| La page | un aplat `var(--brand-clair)`, une ombre neutre à peine visible vers les bords (noir à 4,5 %) ; ni grain ni texture |
| L'encre (pinceau, points, mots, planches) | `var(--brand-sombre)`, lue par le script sur la scène |
| Le mot sur un aplat d'encre ou une pilule | `var(--brand-clair)` |
| L'accent | **un seul détail**, plein : le troisième point du sigle (au choix aussi le point du pinceau, `POINT.accent`) ; jamais un fond, jamais en transparence |
| Ses images | en noir et blanc, dans un cadre fin |
| Le noir final | `var(--brand-sombre)` |

Monochrome : ne remplis pas une forme de couleur, pas de fond sombre au milieu. La page reste claire sur une marque sombre : jamais `var(--brand-bg)` ni `var(--brand-text)` pour la page et l'encre.

## 4. La typographie

- **L'accroche** (scène 1) : police de titres, 600, un mot par ligne, la plus longue à 62 % du diamètre du cercle (environ 110 px en 16:9, 130 px en 9:16), sans point final.
- **Les trois mots** (scène 2) : police de titres, 700, empilés, le plus long à 78 % de la largeur (80 % en 9:16).
- **L'initiale en points** (scènes 2 et 3) : police de titres, 700, à 80 % du petit côté.
- **Les planches** (scène 3) : police de titres, 600 dans un cadre, 700 sur un aplat ou une pilule, 800 seule sur un filet, de 28 px à une soixantaine ; un mot trop long pour sa pilule ou son cadre se pose sur un filet. Leurs « N° 07 » (9 px) et « fig. 2 » (11 px, italique) sont de la texture.
- **Le cadre d'imprimerie** : police de texte, 11 px (9 px la petite ligne), un mot en gras et en capitales espacées (0,08 em), un filet ; des nombres de 11 px qui changent tous les quarts de seconde. Texture (`data-layout-ignore`) : jamais un chiffre de vente, une date ou une promesse.
- **Le sigle** : l'initiale à la taille de l'initiale en points (60 % de la largeur au plus), en quatre états (fine 400, très grasse 900, en contour, fine), puis ses trois points ; le groupe tient dans 74 % de la largeur.
- **Les deux lignes** : police de titres, 600, interligne 1,15, centrées, finies par un point, la plus longue à 74 % de la largeur ; deux ou trois mots par ligne, sinon on coupe.
- **Le nom** : police de titres, 700, capitales, espacement 0,02 em, à 74 % de la largeur ; ou le logo, 60 % de la largeur et 40 % de la hauteur au plus.
- **Sans police de marque imposée :** **Source Serif 4** (600) pour les lignes et le sigle, comme la serif de l'original. `python3 tools/studio_motion.py police "Source Serif 4"` (depuis la racine), son fichier de `marque/polices/` copié dans `assets/fonts/` du projet, un `@font-face` (600, `font-display: block`) et `--t06-titres: "Source Serif 4", var(--brand-font-display);` dans la scène, à la fois dans les scènes 2 et 3 (même initiale). Le nom garde la police de la marque.

## 5. Les mouvements signature

1. **Le cercle au pinceau** (scène 1). Un geste en deux élans (0,45 s puis 0,6 s) : une tête ronde, 150 poils qui sèchent le long du geste (la page passe dans la queue). Pendant qu'il ferme le cercle, les mots s'impriment de gauche à droite (0,3 s par ligne) ; puis le pinceau pose le point final (0,22 s). La caméra avance lentement (×1,02 → ×1,05, sine.inOut), sans choc.
2. **La numérisation** (scènes 1 et 2). Des colonnes de signes couleur de la page traversent l'encre et les mots (redistribuées douze fois par seconde), puis l'encre se défait ; dans la scène 2, les mots passent un instant en pixels de 15 px avant de s'envoler.
3. **La nuée qui écrit** (scènes 1 et 2). Un point par case d'encre (9 px pour le cercle, 4 à 9 px pour les mots). Ils tournent dans le sens du geste (deux poussées) et se posent en bande ; chaque mot prend sa part de la bande, s'écrit en points (0,5 s, power3.inOut, léger bombé) et se pose d'un coup en encre (0,1 s) ; le reste de la bande descend à la ligne du mot suivant. Pendant la lecture, le pinceau souligne le mot clé (0,35 s) ; son trait se défait avec les mots.
4. **L'initiale en points** (scènes 2 et 3). Les points se rassemblent en 0,55 s, ceux en trop s'éteignent en vol ; elle respire (+6 % en 0,4 s), frémit, puis ne bouge plus pendant la rafale.
5. **La rafale de planches** (scène 3). Une trentaine de planches, une par case d'une grille de 8 × 5 (5 × 9 en 9:16) qui laisse sa place à l'initiale, en cinq salves (0,42 s d'écart) du centre vers les bords : chacune se pose en 0,16 s (back.out), son cadre se dessine en 0,32 s, son mot s'écrit en 0,3 s. Une texture (`data-layout-ignore`) : l'initiale reste la seule chose à lire. Aucune ne déborde de sa case. Leur calque dérive de 6 % (sine.inOut) sous l'initiale immobile.
6. **Le sigle** (scène 4). Coupes franches tous les 0,24 s sur la même lettre, puis trois points un à un (le dernier à l'accent) ; en 9:16 la lettre se resserre quand ils arrivent.
7. **Le cadre d'imprimerie** (scènes 1 et 2). La page a l'air d'une planche d'étude ; le cadre s'efface quand l'initiale se forme.

## 6. Les transitions

- Du pinceau à l'initiale, aucune coupe : une seule matière qui se transforme (l'encre et les mots deviennent points, les points des mots, les mots une lettre).
- Une seule coupe franche sur le temps fort : la page pleine de planches devient la page vide ; puis des coupes courtes dans la révélation et la coupe au noir.
- Raccords du kit : la scène 2 part de la bande de la scène 1 (même forme, même graine), la scène 3 de l'initiale de la scène 2 (même tirage), la scène 4 pose son sigle à la taille de cette initiale.

## 7. Le produit à l'écran

Pas de démonstration, mais tout ce qu'on voit vient de son offre : les mots du script (l'accroche, ses parties), l'initiale de son nom, ses formats, ses modules et ses outils (`mots`), ses croquis ou ses captures (`images`). Le trois de l'original (sa version) devient un vrai nombre de l'offre (trois modules, trois étapes) ; deux ou quatre parties font deux ou quatre mots ; jamais un chiffre qui n'est pas dans OFFRE.json. Sans images ni mots, la rafale se retire. Jamais une gravure, une sphère, une lune ou une texture dessinées pour l'occasion.

## 8. Le son

- Original : une musique électronique sourde (environ 116 battements par minute), un accent tous les quatre temps, le son retenu pendant la rafale, une frappe nette sur la coupe et un dernier accent sur le logotype.
- Chez le client : une musique qui monte puis frappe, et **jamais plus d'une seconde de silence au début**. La coupe vers la page vide tombe vers 13 à 14 s, alors que les morceaux « Montée cinématique » n'ont que 3,5 à 8,5 s d'intro : caler leur batterie sur la coupe laisserait le début muet. Deux façons justes, depuis le projet :
  1. **Un morceau dont l'intro couvre la coupe** : `python3 ../../../tools/studio_motion.py musiques choisir --a <instant de la coupe> --duree <durée>` (sans ambiance imposée) ; écarte un morceau dont il écrit « démarre … s après le début » avec plus d'une seconde, puis `musiques prendre <n> --a <instant de la coupe> --duree <durée>`.
  2. **Un morceau à l'intro courte** (il veut une « Montée cinématique ») : `musiques prendre <n> --a <instant de sa batterie> --duree <durée>` (l'instant écrit après « batterie à ») ; la coupe garde son coup sourd pour frapper.
  Après le rendu, `ffmpeg -i <mp4> -af silencedetect=n=-45dB:d=1 -f null -` ne signale aucun silence qui commence à 0.
- Bruitages : un frottement de pinceau sur le cercle et sur le trait, un grésillement sur la numérisation, un souffle pendant la nuée, un coup net sur chaque mot posé, des clics de papier sur les salves, un coup sourd sur la coupe, rien sur le noir.
- **Ambiance proposée** (`musiques choisir --style 6`) : « Montée cinématique », jamais imposée.

## 9. L'ouverture et la fin

- **Ouverture :** la page et son cadre dès la première image, le pinceau à 0,1 s, les mots à 0,7 s : une main qui trace, et ce qu'elle entoure.
- **Fin :** le sigle (1,3 s), les deux lignes (la deuxième 0,5 s après), tenues le temps de leur lecture (la scène le calcule), le nom 2,5 s, 0,3 s de noir. La deuxième ligne dit quand ou où (« Bientôt disponible. », une vraie date de la fiche, ou un appel comme « Inscris-toi sur la liste »).

## Sur une autre offre

- **Formation :** son accroche dans le cercle ; ses trois modules ou étapes ; les planches, ses croquis ou captures, sinon les titres de ses modules ; « Ta formation. » puis « Ouverture le 12 janvier. » (date réelle seulement).
- **Coaching :** le cercle parle tout seul (calme, clarté) autour de sa promesse ; les étapes de sa méthode ; les planches, ses thèmes ; le nom du programme, puis « Bientôt les inscriptions. ».
- **Logiciel :** ses trois fonctions ; ses écrans ou schémas en noir et blanc dans les planches ; l'initiale du logiciel ; le nom, puis « Bientôt en accès anticipé. ».
- **Toujours :** la page claire, le cercle qui porte des mots, la nuée qui écrit, la rafale qui remplit la page, la coupe sur la page vide, le noir.

## En vertical et en carré

- **9:16 :** les quatre scènes se remettent en page seules (`data-width` et `data-height` de leur racine). Le cercle et son accroche à 80 % de la largeur, les trois mots empilés à 80 %, l'initiale au centre, les planches en 5 colonnes sur 9 rangs (celles des bords passent sous l'interface d'un Reel : une texture), le sigle qui se resserre, la fin centrée à 74 %.
- **Carré et 4:5 :** la mise en page du 16:9, resserrée ; le cercle ne touche pas le bord, les légendes du bas restent hors de la bande du sticker.

## Les compositions du kit

Bout à bout dans cet ordre, elles raccordent (20,3 s avec les textes d'exemple) ; chacune vit aussi seule. Leurs textes sont dans l'objet `EXEMPLE`, en tête du script.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (`EXEMPLE`) |
|---|---|---|---|
| `compositions/coup-de-pinceau.html` | 5,4 s | la page et son cadre, le cercle autour de l'accroche, le point, la numérisation, la nuée posée en bande | `accroche` (1 à 3 mots du script, un par ligne, sans point final), `legendes` (les repères des coins) |
| `compositions/nuee-de-particules.html` | 5,5 s pour trois mots (calculée) | la bande qui écrit les mots un à un, le mot clé souligné, la numérisation, l'initiale en points | `trois` (les parties de l'offre, un mot chacune), `nom` (son initiale), `legendes` |
| `compositions/planches-en-rafale.html` | 2,8 s | l'initiale au centre, cinq salves de planches | `images` (ses vraies images, dans `assets/images/`), `mots` (10 à 20 vrais mots), `legendes` (les « fig. »), `nom` |
| `compositions/bientot.html` | 6,6 s pour deux lignes de 4 mots (calculée) | la page vide, le sigle, les deux lignes, le nom ou le logo, le noir | `nom`, `lignes` (deux lignes de 2 ou 3 mots), `logo` (vide : le nom) |
