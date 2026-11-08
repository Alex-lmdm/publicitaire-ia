# Le kit : les briques de chaque scène

Chaque projet reçoit `kit/` (chargé par `index.html`) : les fonds vivants, le curseur, les objets
flottants, le chapitre, les fenêtres, le téléphone, les textes à deux graisses, et des fonctions
GSAP déterministes. **Pars de lui** : il porte le niveau de finition, et c'est lui qu'on améliore
d'une vidéo à l'autre. Les scènes prêtes et les recettes sont dans [scenes.md](scenes.md) ; le
contrat que toute scène respecte, dans [composition.md](composition.md).

Fichiers : `kit.css` (classes `k-*`), `kit.js` (objet `K`), `icones.js` (82 icônes Lucide),
`objets.js` (les objets connus dans leurs vraies couleurs : le dossier du Mac, les fichiers),
`ajouts.js` (les logos et icônes ajoutés par `studio_motion.py logos`). Inter, la police des
interfaces reconstruites, se déclare dans `assets/fonts/interfaces.css`, écrit à la création du
projet à côté de ses fichiers : une feuille ne pointe jamais vers `../` (le rendu la refuse).

## Le squelette d'une scène

Une scène = une sous-composition dans `compositions/`, montée dans `index.html` sur la piste 1,
bout à bout. Tous les identifiants sont préfixés par l'identifiant de la scène.

La taille de la scène est celle de `index.html` (son `data-width` et son `data-height`), sur
la racine de la scène comme sur son hôte dans `index.html` : **1080 × 1920** pour un Reel ou une
story (le défaut, ci-dessous), **1920 × 1080** en 16:9 (page de vente, YouTube). Le kit la lit
là (`K.cadre`) : `K.chapitre`, la zone par défaut de `K.champ` et le mot fantôme s'y adaptent
seuls. Les coordonnées que tu donnes toi-même (`K.trajet`, `zone`, `evite`, `K.flash`) sont en
pixels de cette composition : en 9:16, x va jusqu'à 1080 et y jusqu'à 1920.

```html
<template>
  <style>/* #s3 .s3-… : styles propres à la scène */</style>
  <!-- 9:16 (Reel, story). En 16:9 : data-width="1920" data-height="1080". -->
  <div data-composition-id="s3" data-width="1080" data-height="1920" data-duration="9.5" style="position:absolute; inset:0;">
    <div id="s3" class="k-scene">
      <div class="k-fond k-fond-sombre"></div>
      <div class="k-champ" id="s3-champ"></div>              <!-- objets flottants, derrière -->
      <div class="k-scene3d"><div class="k-camera" id="s3-cam">
        <!-- le sujet, en perspective : .k-plan, .k-fenetre, .k-tel… -->
      </div></div>
      <div class="k-vignette"></div>
      <div id="s3-curseur-hote" style="position:absolute; inset:0; z-index:70;"></div>
    </div>
  </div>
  <script>
    (function () {
      window.__timelines = window.__timelines || {};
      var D = 9.5, tl = gsap.timeline({ paused: true });
      // … K.champ, K.curseur, K.trajet, K.clic, K.taper, K.compteur, tl.to(…) …
      window.__timelines["s3"] = tl;
    })();
  </script>
</template>
```

Son hôte dans `index.html`, sur la piste 1, à la suite de la scène d'avant :

```html
<div id="s3-hote" data-composition-id="s3" data-composition-src="compositions/s3.html" data-start="12" data-duration="9.5" data-track-index="1" data-width="1080" data-height="1920"></div>
```

Le repère de départ du gabarit (`#attente`, et ses deux lignes dans le script d'`index.html`) se
retire à la première scène montée ; `data-duration` de `#root` et de `#fond` prend la durée totale
de la vidéo (au départ, la durée visée de son support : une fin plus courte tiendrait la dernière image).

## Les classes

| Classe | Rôle |
|---|---|
| `k-scene` | conteneur plein cadre de la scène |
| `k-fond k-fond-sombre` · `k-fond-clair` · `k-fond-accent` | fonds : gris anthracite neutre (`#1b1b1d`) avec grille fine, blanc à peine gris (`#f3f3f3`) avec grille, couleur d'accent pleine ; pour une nuit à sa marque, `var(--brand-sombre)` |
| `k-vignette` · `k-vignette-claire` | assombrit les bords (à placer sous le sujet si un plein écran de couleur doit rester pur) |
| `k-mots` | le calque des mots, devant tout ce que la scène montre (un canvas 3D compris) |
| `k-scene3d` > `k-camera` | l'espace en perspective et la caméra qu'on anime (`scale`, `rotationX/Y/Z`, `x`, `y`) |
| `k-plan` | un objet placé dans l'espace 3D |
| `k-titre`, `k-mot`, `k-leger`, `k-accent` | titres à deux graisses ; chaque `k-mot` entre séparément |
| `k-chapitre` > `k-fantome` + `k-etiquette` + `k-interrupteur` (`k-plein`, `k-bille`) | le motif des chapitres ; variantes `k-sur-sombre`, `k-sur-clair`, `k-sur-accent` ; le fantôme fait 15,625 % de la largeur (300 px en 16:9, 169 px en 9:16) |
| `k-fenetre` + `k-feux` | fenêtre d'application (coins, ombre, trois points) |
| `k-tel` > `k-tel-ecran` (+ `k-tel-ilot`) | téléphone ; une image ou des calques dans l'écran |
| `k-tuile` (`k-tuile-sombre`, `-accent`, `-blanche`) | tuile d'icône des champs flottants |
| `k-carte`, `k-carte-sombre`, `k-pastille` | cartes et pastilles |
| `k-disque` | le disque de couleur des flashs (`K.flash`) |

## Les fonctions

| Fonction | Ce qu'elle fait |
|---|---|
| `K.ic(nom)` | le SVG d'une icône (`"rocket"`) ou d'un logo ajouté (`"logo-claude"`) |
| `K.cacher(cible)` | cache dès la construction, première image comprise |
| `K.el(parent, tag, classe, html, style)` | crée un élément |
| `K.rng(graine)` | aléatoire à graine (jamais `Math.random`) |
| `K.cadre(el)` | `{largeur, hauteur}` de la composition qui contient `el` (lus sur `data-width` / `data-height`) |
| `K.duree(el)` | la durée donnée à la scène qui contient `el` (sa racine, ou son hôte une fois montée : HyperFrames retire `data-duration` de la racine intérieure au montage) |
| `K.entreeMots(tl, cible, t, {decalage, y, flou})` / `K.sortieMots(tl, cible, t)` | entrée mot par mot (montée, flou qui se dissipe), sortie rapide |
| `K.curseur(hote, id, clair)` | crée le curseur (`clair` = blanc, sur fond sombre) |
| `K.trajet(tl, curseur, [[t, x, y, durée, courbe], …])` | déplace le curseur ; le premier point le place |
| `K.clic(tl, curseur, t)` | le curseur s'enfonce, une onde part de la pointe |
| `K.taper(tl, el, texte, debut, fin, D)` | frappe au clavier par petits groupes de lettres (le caret est en CSS) |
| `K.compteur(tl, el, de, a, debut, duree, D, format, courbe)` | chiffre qui tourne (format libre : « 3,3 M », « 2:59:41 », « 97 € ») |
| `K.texteSelon(tl, el, D, fn)` | texte qui dépend du temps (un mot qui change à un instant précis) |
| `K.champ(parent, {graine, nombre, objets, zone, evite, tailleMin, tailleMax, flouLoin, flouPres, opaciteLoin})` | répartit des objets en profondeur, flous devant et au loin ; sans `zone`, sur tout le cadre de la composition (un objet au bord peut y être coupé : donne une `zone` en retrait pour tout garder entier) |
| `K.logoNu(svg, couleur)` | fabrique d'objets pour `K.champ` : **le logo seul, sans fond** (`K.logoNu(K.ic("logo-instagram"))`) ; `couleur` pour un logo monochrome (`"#ffffff"` sur fond sombre). C'est la fabrique des objets flottants |
| `K.tuileMarque(fond, encre, svg, bord)` | un logo sur une tuile à ses couleurs : seulement pour une **icône d'application** montrée comme telle (l'écran d'accueil d'un téléphone, un dock), jamais pour les objets flottants |
| `K.tuile(classe, svg)` | fabrique d'objets génériques (à éviter pour les champs flottants) |
| `K.derive(tl, objets, debut, duree, amplitude)` | dérive lente, plus ample au premier plan |
| `K.arrivee(tl, objets, t, {etalement})` | les objets surgissent de la profondeur en rafale |
| `K.flash(tl, disque, x, y, t, duree)` | un disque de couleur part de (x, y) et couvre l'écran |
| `K.chapitre(tl, racine, curseur, t, {depart, cible})` | chapitre complet (mot fantôme, étiquette, curseur, interrupteur) ; rend l'instant de la plongée. Le clic vise l'interrupteur d'après la taille de la composition, en 9:16 comme en 16:9 ; `cible: [x, y]` seulement si le CSS de la scène a déplacé l'interrupteur |
| `K.jeton(nom)` | la valeur d'un jeton de la marque (`K.jeton("--brand-gris-2")`), pour un tween de couleur (GSAP n'interpole pas une variable CSS) |

### Les objets connus, dans leurs vraies couleurs

Ce que tout le monde reconnaît garde son vrai visage ([image.md](image.md), « Les objets connus ») :
ils sont chargés par `kit/objets.js` (s'il manque dans le projet : recopie `objets.js`, `kit.js`
et `kit.css` du dossier `templates/kit/` et ajoute `<script src="kit/objets.js"></script>` après
`icones.js` dans son `index.html`).

| Objet | Ce que c'est |
|---|---|
| `K.ic("objet-dossier")` | le dossier bleu du Mac |
| `K.ic("objet-fichier")`, `objet-pdf`, `objet-doc`, `objet-tableur`, `objet-presentation`, `objet-video`, `objet-image`, `objet-audio`, `objet-zip` | un document, et les fichiers PDF, Word, Excel, PowerPoint, vidéo, image, son, archive, avec leur couleur et leur étiquette |
| `K.statut(ecran, {heure, clair})` | la barre d'état d'un iPhone (9:41, réseau, Wi-Fi, batterie) en haut de `k-tel-ecran` ; `clair: false` : noire, sur un écran clair |
| `K.notification(parent, {icone, app, quand, titre, texte, sombre, largeur})` | une notification d'iPhone ; `icone` : le vrai logo (`K.ic("logo-stripe")`) ; ses mots se lisent (titre 34 px, texte 32 px) ; rend l'élément, à placer et animer |
| `K.bulle(parent, texte, genre)` | une bulle de messagerie : `"bleue"` (envoyé d'un iPhone), `"grise"` (reçu), `"whatsapp"` |
| `k-objet` | le porteur d'un objet en grand (`K.el(cam, "div", "k-objet", K.ic("objet-pdf"), "width:…; height:…")`), avec son ombre |
| `k-feux` | les trois boutons rouge, jaune, vert d'une fenêtre du Mac (`k-fenetre`) |

Partout où une scène prend une icône (`icone` d'un `CONTENU`, `K.ic`), un `objet-…` se met à la
place d'une icône d'un seul trait quand l'idée a un objet connu. Ces couleurs ne débordent jamais sur un fond, un texte ou un
trait ; `palette` les connaît.

### Le mot qui joue, le schéma, le fil conducteur, la coupe

Le langage du motion design de [scenes.md](scenes.md). `cible` accepte un sélecteur, un élément ou
une liste.

| Fonction | Ce qu'elle fait |
|---|---|
| `K.lettres(el)` | découpe le texte en lettres (`span.k-lettre`), rend la liste : pour une rafale de lettres |
| `K.claque(tl, cible, t, {de, y, rotation, decalage, duree, ease})` | le mot arrive d'un coup, plein (aucun fondu : rien ne vire à l'olive sur l'accent), à l'échelle `de` (1,45 : il se pose en rétrécissant ; 0,4 : il grandit), et se pose ; `decalage` pour une rafale |
| `K.etire(tl, cible, t, {axe, facteur, tenue, retour})` | le mot (ou ses lettres) s'étire puis revient ; `axe: "x"` en largeur |
| `K.barre(tl, el, t, {angle, eteindre})` | une barre pleine de l'accent raye l'élément ; `eteindre` : la couleur qu'il prend ensuite (`K.jeton("--brand-gris-2")`) |
| `K.surligner(tl, el, t, {couleur, encre})` | un bloc plein s'ouvre derrière le mot, de gauche à droite ; `couleur` du bloc (l'accent par défaut ; l'encre sur l'aplat), `encre` du mot |
| `K.volet(tl, cible, t, {decalage, origine})` | des blocs (étiquettes, pastilles pleines, pistes) s'ouvrent depuis leur bord, en rafale |
| `K.lien(parent, [x1, y1], [x2, y2], {svg, courbe, classe})` | un lien courbe d'un schéma (SVG `k-liens`, aux pixels de la composition), rend le chemin ; `svg` pour en ajouter au même dessin ; `classe: "k-lien-discret"` pour un trait gris |
| `K.trace(tl, chemin, t, duree)` | le trait se dessine de son début à sa fin |
| `K.longer(tl, el, chemin, t, duree, D, {de, a})` | le fil conducteur (`k-fil`) suit le trait ; même durée et même courbe que `K.trace` : il en dessine la pointe. `el` ne prend aucun autre mouvement x / y |
| `K.tranche(tl, calque, t, {de, a, duree})` | la coupe : un trait de l'accent fend l'écran en biais, le calque (plein cadre) se fend et ses moitiés tombent. **Appelée en dernier**, la timeline complète : elle fige une copie du calque à l'instant t (jamais de `<video>` dedans) |

| Classe | Rôle |
|---|---|
| `k-heros` | le mot héros : 1 à 3 mots, très gras, serrés, qui remplissent la largeur |
| `k-contour` | le mot en contour net (un trait plein, `--k-contour`), pour doubler un mot plein ; jamais une lueur |
| `k-blocs` > `span.k-bloc-accent` · `k-bloc-clair` · `k-bloc-sombre` | les étiquettes de fonction : deux ou trois mots en blocs empilés |
| `k-noeud` (`k-noeud-sombre`, `k-noeud-accent`) | un nœud de schéma (logo + nom) |
| `k-fil` | le fil conducteur : le point de l'accent |

## La 3D : `kit/plan3d.js`

Un plan en vraie 3D (three.js, copié dans `assets/vendor/` par `npm run sync`), au niveau choisi
par le client et à l'usage décrit dans [scenes.md](scenes.md) (« La 3D, quand elle sert »). C'est
une sous-composition comme une autre : un canvas, un script **module** qui appelle `plan3d`, et ses
mots en HTML par-dessus, dans le calque `k-mots`, animés par la timeline de la scène comme partout.
`plan3d` fait la plomberie (le rendu, la lumière, la synchronisation sur le temps de la vidéo) et
donne à la scène ses outils, ses **briques** (des objets du quotidien déjà construits pièce par
pièce) et ses **matières** ; la scène pose ses objets et rend `poser(t)`. L'unité est **10 cm** :
un ordinateur portable fait 3 unités de large, une tasse un peu moins d'une. Le repère : y vers le
haut, la caméra regarde de face depuis +z vers -z ; une brique se pose sur y = 0 (la table, le sol),
le mur d'un plateau est à z = -`recul`.

### Niveau a : un objet détaillé sur le fond de sa marque

Ce squelette se cadre seul en 9:16 comme en 16:9 (`distance`) :

```html
<template>
  <style>
    #s5-titre { position: absolute; left: 8%; top: 6%; font: 800 120px/0.95 var(--brand-font-display); letter-spacing: -0.04em; color: var(--brand-clair); }
  </style>
  <!-- 9:16 (Reel, story). En 16:9 : data-width="1920" data-height="1080". -->
  <div data-composition-id="s5" data-width="1080" data-height="1920" data-duration="4" style="position:absolute; inset:0;">
    <div id="s5" class="k-scene">
      <div class="k-fond k-fond-sombre"></div>
      <canvas id="s5-vue" style="position:absolute; inset:0; width:100%; height:100%;"></canvas>
      <div class="k-mots"><div id="s5-titre">Ta page.</div></div>
    </div>
  </div>
  <script type="module">
    import { plan3d } from "./kit/plan3d.js";
    plan3d(document.getElementById("s5-vue"), async ({ scene, camera, briques, distance, courbe, sol }) => {
      sol(-0.8);                                          // l'ombre au sol, neutre (jamais sur l'aplat)
      const tel = await briques.telephone({ ecran: "assets/images/app.png" });   // sa vraie capture, en aplat
      scene.add(tel);
      const d0 = distance(tel.dimensions.l, tel.dimensions.h, 0.62), arrivee = courbe("expo.out"), derive = courbe("sine.inOut");
      return (t) => {                                     // t : secondes depuis le début du plan
        const a = arrivee(Math.min(1, t / 0.8)), b = derive(Math.min(1, t / 4));
        tel.rotation.y = -1 + 0.8 * a;                    // il arrive en pivotant, puis se tient
        tel.position.y = -0.3 * (1 - a);
        tel.defiler(0.3 * b);                             // sa capture défile doucement sur l'écran
        camera.position.set(0.1, 0.1, d0 * (1.02 - 0.03 * b));   // puis une dérive lente, 3 %
        camera.lookAt(0, 0, 0);
      };
    }, { focale: 50 });
  </script>
  <script>
    (function () {                                        // ses mots : la timeline de la scène, comme partout
      window.__timelines = window.__timelines || {};
      var tl = gsap.timeline({ paused: true });
      K.cacher("#s5-titre");                              // caché dès la construction, il claque à 0,6 s
      tl.set("#s5-titre", { opacity: 1 }, 0.6)
        .from("#s5-titre", { scale: 1.45, duration: 0.45, ease: "expo.out", transformOrigin: "0% 50%" }, 0.6);
      window.__timelines["s5"] = tl;
    })();
  </script>
</template>
```

### Niveau b : un plateau

Une photo de produit qui bouge : la table, le mur, sa vraie matière au centre, des objets du
quotidien autour, le soleil d'une fenêtre, l'objectif et la finition film. Le même plan se cadre en
16:9 (un plan large, à hauteur de table) et en 9:16 (une plongée sur le bureau, la tasse au premier
plan). Son hôte dans `index.html` porte **`data-plateau`**, son canvas **`data-layout-allow-overflow`**
(un plateau remplit l'image : il touche les bords exprès).

```html
<template>
  <style>
    #s3-titre { position: absolute; left: 6%; top: 7%; font: 800 140px/0.95 var(--brand-font-display); letter-spacing: -0.04em; color: var(--brand-sombre); }
    #s3-titre span { background: var(--brand-accent); color: var(--brand-contrast); padding: 0 0.12em; }
  </style>
  <!-- 16:9. En 9:16 (Reel, story) : data-width="1080" data-height="1920" ici et sur l'hôte ; le code choisit sa caméra (vertical). -->
  <div data-composition-id="s3" data-width="1920" data-height="1080" data-duration="4.5" style="position:absolute; inset:0;">
    <div id="s3" class="k-scene">
      <canvas id="s3-vue" data-layout-allow-overflow style="position:absolute; inset:0; width:100%; height:100%;"></canvas>
      <div class="k-mots"><div id="s3-titre">Ta <span>page.</span></div></div>
    </div>
  </div>
  <script type="module">
    import { plan3d } from "./kit/plan3d.js";
    const NOM = "…";              // le nom de son offre, recopié de OFFRE.json (offre.nom) comme tous ses mots, imprimé sur son carnet
    plan3d(document.getElementById("s3-vue"), async ({ scene, briques, jeton, courbe, orbite, net, largeur, hauteur }) => {
      const vertical = hauteur > largeur;
      scene.add(briques.plateau({ bois: "chene", mur: "#e4ded4", recul: 7 }));     // la table (dessus à y = 0), le mur
      const ordi = await briques.ordinateur({ ecran: "assets/images/page.png", ouvert: 0.3 });   // sa vraie page
      ordi.position.set(-0.5, 0, 0.3); ordi.rotation.y = 0.1;
      const carnet = await briques.carnet({ couverture: jeton("--brand-sombre"), titre: NOM, encre: jeton("--brand-accent") });
      carnet.position.set(2.75, 0, 0.75); carnet.rotation.y = -0.32;
      const crayon = briques.crayon();
      crayon.position.set(2.65, carnet.dimensions.e, 0.9); crayon.rotation.y = 0.95;
      const tasse = briques.tasse({ cafe: true });
      tasse.position.set(...(vertical ? [-0.9, 0, 4.1] : [-3.9, 0, -2.6])); tasse.rotation.y = 2.2;
      scene.add(ordi, carnet, crayon, tasse);
      const arrivee = courbe("expo.out"), derive = courbe("sine.inOut");
      // la caméra : le point regardé, sa distance (unités), sa hauteur et son côté (degrés). 16:9 : à hauteur
      // de table, le mur derrière ; 9:16 : une plongée sur le bureau, la tasse au premier plan.
      const cible = vertical ? [0.45, 0.2, 0.2] : [-0.5, 0.85, 0], d0 = vertical ? 13.5 : 12.8;
      const haut = vertical ? 57 : 21, cote = vertical ? 6 : 9;
      return (t) => {
        const a = arrivee(Math.min(1, Math.max(0, (t - 0.2) / 1.3))), b = derive(Math.min(1, t / 4.5));
        ordi.ouvrir(0.3 + 0.7 * a);                                    // il s'ouvre...
        ordi.defiler(0.32 * derive(Math.min(1, Math.max(0, (t - 1.6) / 2.9))));   // ...puis sa page défile
        orbite(cible, d0 * (1.04 - 0.05 * b), haut, cote);             // une avancée lente
        net(ordi.ecran);                                               // la mise au point sur sa page
      };
    }, { focale: 50, lumiere: "fenetre", ouverture: 2.8, contact: true, finition: true });
  </script>
  <!-- … ses mots : la timeline de la scène, comme au niveau a … -->
</template>
```

```html
<div id="s3-hote" data-composition-id="s3" data-composition-src="compositions/s3.html" data-start="8" data-duration="4.5" data-track-index="1" data-width="1920" data-height="1080" data-plateau></div>
```

### Les réglages du plan

| Option de `plan3d(canvas, construire, {…})` | Ce qu'elle fait |
|---|---|
| `focale: 35`, `50`, `85` | l'objectif, en millimètres : 35 large (un décor), 50 naturel, 85 serré (un objet, un détail) ; sinon `angle`, l'angle de vue vertical (26° par défaut) |
| `lumiere: "studio"` (par défaut) | la lumière produit : une principale douce qui porte l'ombre (ajustée seule aux objets), un remplissage neutre, les reflets d'une pièce |
| `lumiere: "fenetre"`, ou `{ type: "fenetre", cote: "droite", motif: "store" \| "fenetre" \| "aucun", force, couleur, inclinaison, position, cible }` | un soleil chaud qui entre de côté et dessine l'ombre d'un store (ou des carreaux d'une fenêtre) sur la table et le mur, le bleu du ciel dans les ombres, un rendu photographique. Le soleil est à 13 unités à gauche (`cote: "droite"` : à droite), 12 au-dessus, 6 devant, et vise [0, 0, -1,5] ; pour un grand décor (une salle de classe), éloigne-le (`position: [-60, 45, 10]`) et vise le centre du décor |
| `ouverture: 1.4` à `8` | la profondeur de champ d'un vrai objectif : 2 très flou, 2.8 un fond doux, 5.6 presque tout net ; la mise au point se fait par `net()` |
| `contact: true` | l'ombre de contact, là où deux objets se touchent |
| `finition: true`, ou `{ grain, vignette }` | la finition film : un grain fin qui change à chaque image (toujours le même à un instant donné) et un léger vignettage |
| `fond: "--brand-sombre"` | avec `ouverture`, `contact` ou `finition`, l'image est opaque : la couleur de ce qui n'est couvert par rien (un plateau couvre tout) |
| `exposition`, `ombre: false` | plus clair (1.3) ou plus sombre (0.9) ; sans ombre |

| Outil donné à `construire` | Ce qu'il donne |
|---|---|
| `THREE`, `scene`, `camera`, `renderer`, `largeur`, `hauteur` | three.js et la scène prête : la caméra, un fond transparent au niveau a (le fond du kit se voit derrière), la taille de la composition |
| `lumiere`, `lumieres` | la lumière principale (le soleil à la fenêtre), et toutes (`soleil`, `ciel`, `rebond`), à déplacer si le plan le demande |
| `briques`, `matiere` | les objets et les matières, plus bas |
| `orbite(cible, d, hauteur, cote)` | la caméra autour d'un point (`[x, y, z]`) : à `d` unités, `hauteur` degrés au-dessus de l'horizon (0 à hauteur du point, 90 à la verticale), `cote` degrés vers la droite (0 de face) ; elle le regarde. À appeler dans `poser(t)` |
| `net(cible)` | la mise au point, à appeler dans `poser(t)` : sur un objet (`ordi.ecran`), un point (`[x, y, z]`) ou une distance ; sans elle, sur l'origine |
| `distance(l, h, part)` | la distance de la caméra pour qu'un objet de l × h, face à elle, occupe `part` du cadre (0,6 par défaut) : le même plan se cadre en 9:16 comme en 16:9 |
| `courbe("expo.out")` | une courbe de GSAP, à appliquer à une progression de 0 à 1 : les mêmes arrivées et dérives qu'ailleurs ([mouvement.md](mouvement.md)) |
| `jeton("--brand-gris-1")` | une couleur de sa marque (`THREE.Color`) |
| `aplat(couleur, {map})` | une matière sans lumière : la couleur reste exactement elle (l'accent, un objet connu, une capture), même sous le soleil et l'objectif |
| `texture(src, {taille, couleur})` | une image du projet (`"assets/images/page.png"`) ou un SVG du kit (`K.ic("logo-stripe")`, `K.ic("objet-pdf")`) prête à poser ; `couleur` pour un SVG d'un seul trait |
| `arrondi(l, h, r)`, `plaquer(geometrie, l, h)` | un rectangle aux coins ronds, centré, à extruder (`ExtrudeGeometry`) ou à poser à plat (`ShapeGeometry`) ; une image qui remplit une forme posée à plat |
| `sol(y, opacite)` | un sol invisible qui ne garde que l'ombre, neutre (niveau a) |
| `hasard()` | un hasard toujours le même, pour placer des objets « au hasard » |

### Les briques : des objets du quotidien, pièce par pièce

Chaque brique est un groupe three.js, à la taille réelle, posé sur sa base (y = 0 : sur la table)
sauf le téléphone et la tablette, centrés et debout, écran vers la caméra. Un écran prend sa **vraie
capture** (`ecran` : son chemin, ou une texture déjà chargée), en aplat, cadrée comme une page (le
haut d'abord) ; sans capture il reste éteint. Une vitre légère passe devant (`reflet: false` pour
l'ôter). Aucune marque n'est dessinée (ni logo sur une coque, ni lettre sur les touches).

| Brique | Ses pièces | Ce qu'on en fait |
|---|---|---|
| `briques.ordinateur({ ecran, teinte: "argent" \| "gris" \| "noir", ouvert, cadrage })` | coque d'alu brossé, clavier touche par touche, pavé tactile, pieds, ports, charnière, écran et sa caméra | `ouvrir(p)` (0 fermé, 1 ouvert à 110°), `defiler(p)` (sa page défile : 0 le haut, 1 le bas), `ecran`, `couvercle`, `dimensions` |
| `briques.telephone({ ecran, teinte: "graphite" \| "argent" \| "noir" \| "blanc" })` | cadre de métal, vitre, écran, île, dos de verre dépoli, bloc photo et ses objectifs, flash, boutons | `defiler(p)`, `ecran`, `epaisseur` ; couché sur la table : `rotation.x = -Math.PI / 2`, `position.y = epaisseur / 2` |
| `briques.tablette({ ecran, teinte })` | coque d'alu, vitre, écran, caméras | comme le téléphone |
| `briques.carnet({ couverture, titre, encre, pages: "lignes" \| "carreaux" \| "seyes" \| "blanc", ouvert })` | couvertures, bloc de pages et sa tranche, page lignée (ou Seyès, le cahier d'écolier), spirale de métal et ses trous | `ouvrir(p)` (la couverture se rabat), `dimensions` ; `titre` : le nom de son offre (`OFFRE.json`), imprimé dans la police de sa marque |
| `briques.crayon({ couleur, gomme })` | corps hexagonal laqué, bois taillé, mine, virole et ses rainures, gomme | couché sur un pan, la pointe vers +x |
| `briques.tasse({ couleur, cafe })` | corps tourné en céramique émaillée, anse, café | l'anse vers +x |
| `briques.pupitre({ bois, metal })`, `briques.chaise({ bois, metal })` | le pupitre d'écolier (plateau de bois, casier, pieds en tube) et sa chaise (assise, dossier) | posés sur y = 0 ; l'élève est côté +z, le dossier de la chaise aussi : mets la chaise 3 unités devant le pupitre |
| `briques.tableau({ l, h, ardoise, cadre })` | le tableau noir (2,4 × 1 m par défaut) : ardoise verte, cadre de bois, rebord, deux craies, la brosse ; rien n'y est écrit | centré, face à +z : sur le mur, `position.set(0, 14, -recul + 0.3)` |
| `briques.plateau({ bois, mur, recul, largeur, profondeur, hauteurMur, sansMur })` | une table de bois (dessus à y = 0) et un mur peint à `recul` derrière ; par défaut 40 × 22 unités de table, un mur de 24 de haut à 7 derrière ; agrandi (`largeur: 90, profondeur: 70, recul: 30, hauteurMur: 40`), la table devient le parquet d'une pièce | `table`, `mur` |
| `briques.boite`, `dalle`, `coque`, `plaque`, `cylindre`, `ecran` | les formes de base aux arêtes arrondies : `boite(l, h, p, r, matiere)` (centrée), `dalle(l, p, e, rCoins, rBords, matiere, echelleUV)` (une planche couchée, posée sur y = 0), `coque(l, h, e, r, b, matiere, echelleUV)` (une coque debout, centrée, face à +z), `plaque(l, h, r, matiere)` (une face plate, centrée, face à +z, sa texture la remplit), `cylindre(rHaut, rBas, h, matiere)` (centré, debout selon y), `ecran(source, l, h, r)` ; `echelleUV: 8` pour du bois (une texture couvre 80 cm) | construire, pièce par pièce, un objet que le kit n'a pas : une boîte d'envoi, une étagère, une montre |

| Matière (`matiere.…`) | Ce qu'elle donne |
|---|---|
| `bois({ essence: "chene" \| "noyer" \| "clair" \| "fonce" \| "cedre", planches, repetition })` | un bois veiné, ses cernes, ses pores, ses lames |
| `papier({ l, h, lignes: "lignes" \| "carreaux" \| "seyes" \| "blanc", marge })`, `tranche()` | une page crème, fibreuse, lignée ; la tranche d'un bloc de pages |
| `alu({ teinte, brosse })`, `chrome()` | l'aluminium brossé ou poli, le métal d'une spirale |
| `plastique({ couleur, mat })`, `verre({ couleur, depoli })`, `ceramique({ couleur })`, `laque({ couleur })`, `mat({ couleur, rugosite })` | une touche, une coque, l'écran éteint, une tasse, un crayon peint, une gomme |
| `mur({ couleur })`, `carton({ couleur })` | un mur peint, du kraft |
| `impression(texte, { police, encre, fond })` | un texte imprimé dans la police de sa marque (le nom de son offre sur une couverture) ; jamais un texte à lire, qui reste en HTML |

Toutes sortent d'un hasard à graine : la même texture à chaque rendu, sans fichier à fournir.

### Les règles du plan

- **Les couleurs** : une matière éclairée (le bois, le papier, l'alu) garde les couleurs de la vraie
  vie ; sa marque se pose en `aplat` (et ses mots en HTML). Au niveau a, une matière éclairée reste
  neutre (les gris de sa marque, du blanc, du noir, l'alu, le verre) : éclairée, une couleur
  s'assombrit sur ses côtés en teintes hors de sa palette (un jaune vire à l'olive), et `palette` le
  refuse. Au niveau b, l'hôte du plateau porte `data-plateau` : `palette` laisse ses couleurs à la
  revue, et refuse la vidéo si les plateaux en couvrent plus de la moitié.
- **Ses mots sur un plateau** : un mur clair et une table au soleil font un fond changeant ; ses mots
  prennent son encre sombre (`--brand-sombre`) sur un décor clair, son encre claire sur un décor sombre
  (un tableau noir, un mur foncé), ou, partout, un bloc plein (son accent, ou sa couleur sombre sous son
  texte clair).
- **Cadrer un plateau** : `orbite`. En 16:9, à hauteur de table, 15 à 25° ; en 9:16, une plongée de
  45 à 60° sur un bureau (la table remplit le cadre haut), ou 15 à 25° pour garder le mur et le décor
  (une salle de classe) ; 10 à 14 unités pour un bureau à 50 mm, davantage pour une pièce (35 mm).
  Vérifie à l'image : le héros (sa capture) occupe au moins 40 % de la largeur dans le plan qui le montre.
- **Sortir d'un plateau** vers un plan à plat : un bloc de ses mots (son accent) qui grandit jusqu'à
  couvrir l'écran et devient le fond du plan suivant, ou un disque qui part de l'écran de l'ordinateur
  (`K.flash`). Ce raccord joué par-dessus le plateau compte dans sa durée (celle de son hôte), donc
  dans la moitié de la vidéo que les plateaux ne dépassent pas.
- **La capture qui va avec l'objet** : sa page de bureau sur l'ordinateur ou la tablette, une capture
  de téléphone sur le téléphone (une page de bureau y serait illisible).
- **En 9:16**, un objet couché (un ordinateur ouvert) reste petit dans un cadre haut : plonge sur la
  table (la caméra au-dessus), préfère un objet debout (un téléphone, une carte), ou rapproche-le
  (`distance(l, h, 0.85)`).
- **`poser(t)` ne lit que t** : jamais d'horloge, de minuterie, de `requestAnimationFrame`, de boucle
  ni de `Math.random` (`hasard`). La preuve : `npx hyperframes snapshot --at 2,0,2` donne deux images
  identiques à 2 s.
- **Ce que `check` ne voit pas** : rien de ce qui est dessiné dans le canvas (taille, contraste, temps
  de lecture). Les mots à lire restent donc en HTML ; regarde les images du plan. Un objet qui sort du
  cadre exprès (`canvas_content_at_edge`) : `data-layout-allow-overflow` sur le canvas, après avoir
  vérifié l'image ; un plateau le porte toujours.
- **Pas de texte en relief** : ses mots à lire restent en HTML (lisibles, contrôlés par `check`, dans
  sa police). Un nom posé sur un objet s'imprime (`impression`, le `titre` du carnet).
- **Le rendu** passe par la carte graphique : un plateau de 4,5 s se rend en une dizaine de secondes.
  Sans elle, en logiciel, environ quinze fois plus lentement, avec les mêmes images : un plateau par
  vidéo de Reel, des textures de 2048 px au plus.
- **Un projet créé avant le 8 novembre 2026** n'a pas l'import map de three (la ligne
  `<script type="importmap">` du gabarit `templates/projet/index.html.tpl`, avant les autres scripts
  de son `index.html`) ni `assets/vendor/three-addons/` : ses plans simples marchent, un plateau
  s'arrête avec ce message. Recopie la ligne, et `assets/vendor/` depuis la racine du dossier (après
  `npm run sync`). Un projet dont `kit/plan3d.js` manque : recopie `kit/` depuis `templates/kit/`.

## Les pièges (tous rencontrés)

- **Un identifiant intérieur égal à celui de l'hôte** d'une scène dans `index.html` (`a04-hote`) :
  `getElementById` trouve l'hôte, plein écran, et l'objet s'y pose en haut à gauche, sans les styles
  de la scène (un dossier en Times dans le coin). Les éléments d'une scène
  ne finissent jamais par `-hote`.
- **Une couleur qui passe de l'encre à l'accent** (un dossier sombre qui prend l'accent) ne se fond
  pas : à mi-chemin, elle est olive. Elle change d'un coup (`tl.set`), quand un volet ou un
  mouvement la couvre.
- **Les grands titres et `check`** : la boîte d'un texte vaut 1,4 fois sa taille, même
  avec un interligne serré ; deux textes empilés qui se touchent à l'œil se « chevauchent » pour
  `check`. Laisse environ 0,2 fois la taille de police entre la boîte de l'un et celle de l'autre.

- **Sur un aplat de sa couleur, rien n'entre en fondu, en flou ni avec une ombre sombre** : un élément
  sombre à demi transparent sur un jaune fait de l'olive, et `palette` le relève. Fais-le paraître
  à pleine opacité et grandir, ou entrer par un volet.
- **Un projet créé avant la version 0.9.0** n'a pas les jetons de palette (`--brand-sombre`,
  `--brand-clair`, `--brand-gris-1` à `4`, `--brand-accent-lisible`) que les scènes des styles
  utilisent : sans eux, un fond de nuit devient transparent. Recopie `brand/tokens.css` du dossier
  Publicitaire IA (après `studio_motion.py style`) dans le `brand/` du projet avant d'y poser une
  scène d'un style.

- **État de départ** : `K.cacher` ou `gsap.set` à la construction, jamais `tl.set(…, 0)` (la
  première image montrerait l'élément). Même chose pour la position de départ d'un curseur ou
  d'un disque (le kit le fait).
- `K.arrivee` lit l'opacité donnée par `K.champ` : ne cache pas le champ avant de l'appeler.
- **Décaler une scène déjà écrite** (elle démarre 0,5 s plus tard dans la vidéo) : jamais
  `tl.shiftChildren(-0.5)`. GSAP recale les animations qui passeraient avant 0 et tout arrive
  0,5 s trop tard (une fenêtre invisible pendant 1 s, des cartes en retard sur la voix). Garde le départ de la scène et ajoute en tête ce qui doit tenir (la fin de la scène
  d'avant, figée), ou réécris les temps.
- `flouPres: 0` et `flouLoin: 0` valent bien zéro (logos nets) ; sans eux, le flou par défaut
  s'applique.
- Le kit d'un projet est une copie : si le kit du dossier change pendant la fabrication,
  recopie `kit.js` et `kit.css` dans le projet, sinon une fonction manque et la scène reste figée
  (toutes ses images identiques).
- **Une forme tournée** (`LatheGeometry`, une tasse, un vase) se décrit par son profil, de
  l'extérieur du dessous vers l'intérieur : à l'envers, ses faces regardent vers dedans, la lumière
  le cache (`DoubleSide`), mais l'objectif la prend pour du vide et fait un halo flou autour
  (essai du 08/11/2026). Pas de `DoubleSide` pour cacher une forme retournée : retourne son profil.
- Un panneau plein écran qui doit couvrir la scène 3D lui donne un `z-index` plus haut que
  `k-scene3d`, ou donne `z-index` à `k-scene3d` pour qu'elle reste devant.
- Une vraie vidéo à la racine d'`index.html` (le Reel qui joue dans le téléphone, un résultat
  posé sur l'interface) : son cadre prend `z-index: 2` et passe devant toutes les scènes, qui
  restent à 1 chacune dans leur propre empilement (règle du gabarit). Les `z-index` d'une scène
  ne comptent que chez elle : son voile à 55 ne couvre jamais la vidéo. Un texte qui doit passer
  DEVANT la vidéo vit dans une scène dont l'hôte porte `style="z-index:3"` (et un fond transparent
  si la vidéo doit rester visible). Un projet créé avant la version 0.6.3 garde l'ancienne règle,
  qui ne s'appliquait plus une fois la scène montée : recopie celle du gabarit
  (`templates/projet/index.html.tpl`) dans son `index.html`.
- Un disque ou un panneau qu'on agrandit d'un facteur 20 prend une couleur unie, jamais la grille
  (elle grossirait avec lui).
- Raccord avec un plein écran de couleur (le nom de l'offre qui devient une fenêtre) : la fenêtre
  commence à une échelle qui couvre tout l'écran, et le texte qu'elle porte au départ a la taille
  et la place du texte de la scène précédente une fois cette échelle appliquée.
- Un panneau qu'on fait glisser sur toute la largeur se déplace (`x`), il ne s'étire pas
  (`scaleX`) : la grille resterait déformée au raccord.
- Logos : seulement ceux des outils réellement liés à l'offre, posés par `studio_motion.py logos`
  (nettoyés, en ligne ; un nom courant suffit, « chatgpt » trouve le logo d'OpenAI, et
  `logos chercher <nom>` donne l'identifiant d'une marque). Un logo blanc ou noir passe en
  `currentColor` : sa couleur suit le CSS (`K.logoNu(svg, "#ffffff")` sur un fond sombre). Une
  marque absente des registres (récente, de niche) : demande son logo au client, une fois, puis
  `logos <projet> fichier:<chemin>` ; jamais un logo redessiné ni une icône à sa place.
- `npx hyperframes check` signale le texte net posé sur une couche volontairement floue :
  marque la couche floue (ou le texte) avec `data-layout-allow-overlap`, après avoir vérifié à
  l'image que tout se lit.
- Le mot fantôme est presque invisible exprès : `check` le compterait comme un texte illisible
  (erreur de contraste). `K.chapitre` lui pose `data-layout-ignore` ; un fantôme animé à la main
  le reçoit dans le HTML. Cet attribut est réservé à ce qui n'est pas à lire : la typographie
  décorative, et une matière qui sert de texture (une interface qui passe au flou derrière un
  chiffre). Jamais sur un texte qu'on doit lire.
