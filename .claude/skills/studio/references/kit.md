# Le kit : des briques qui retirent de la friction

Chaque projet reçoit `kit/` (chargé par `index.html`) : les fonds, le curseur, la caméra et son
zoom, les objets flottants, le chapitre, les fenêtres, le téléphone, les objets connus, les mots qui
jouent, et des fonctions GSAP déterministes. **Sers-t'en pour ce qu'il fait déjà bien** (un clic,
une frappe, un compteur, un zoom calculé, un logo qui flotte) ; tout le reste s'écrit sur mesure, en
GSAP et en CSS, pour ce plan-là. Une boîte à outils à consulter, pas un mode d'emploi à suivre. Les
scènes d'exemple sont dans [scenes.md](scenes.md) ; le contrat que toute scène respecte, dans
[composition.md](composition.md).

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
(`K.cadre`) sur l'hôte d'abord, comme la durée (`K.duree`) : une scène écrite en 9:16 et montée
par un hôte en 16:9 se met en page en 16:9. `K.chapitre`, la zone par défaut de `K.champ` et le
mot fantôme s'y adaptent seuls. Les coordonnées que tu donnes toi-même (`K.trajet`, `zone`, `evite`, `K.flash`) sont en
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
      <div id="s3-curseur-calque" style="position:absolute; inset:0; z-index:70;"></div>
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
| `k-fond k-fond-sombre` · `k-fond-clair` · `k-fond-accent` | fonds : la nuit de la marque (`var(--brand-sombre)`) avec grille fine, blanc à peine gris (`#f3f3f3`) avec grille, couleur d'accent pleine |
| `k-vignette` · `k-vignette-claire` | assombrit les bords (à placer sous le sujet si un plein écran de couleur doit rester pur) |
| `k-mots` | le calque des mots, devant tout ce que la scène montre : la caméra peut dériver dessous, ses mots ne bougent pas |
| `k-ligne` (dans `k-mots`) | une ligne de mots posée de bord à bord (`left: 0; right: 0`, sans retour à la ligne) : on lui donne `top` et `text-align` |
| `k-scene3d` > `k-camera` | l'espace en perspective et la caméra qu'on anime (`scale`, `rotationX/Y/Z`, `x`, `y`) |
| `k-plan` | un objet placé dans l'espace 3D |
| `k-titre`, `k-mot`, `k-leger`, `k-accent` | titres à deux graisses ; chaque `k-mot` entre séparément ; sur l'accent, `k-sur-accent` (le texte prend `var(--brand-contrast)`) |
| `k-chapitre` > `k-fantome` + `k-etiquette` + `k-interrupteur` (`k-plein`, `k-bille`) | le motif des chapitres ; variantes `k-sur-sombre`, `k-sur-clair`, `k-sur-accent` ; le fantôme fait 15,625 % de la largeur (300 px en 16:9, 169 px en 9:16) |
| `k-fenetre` + `k-feux` | fenêtre d'application (coins, ombre, trois points) |
| `k-tel` > `k-tel-ecran` (+ `k-tel-ilot`) | téléphone ; sa capture est une image posée directement dans l'écran (`k-tel-ecran > img`, plein écran) ; une interface reconstruite dans l'écran garde ses images à leur taille |
| `k-tuile` (`k-tuile-sombre`, `-accent`, `-blanche`) | tuile d'icône des champs flottants |
| `k-carte`, `k-carte-sombre`, `k-pastille` | cartes et pastilles |
| `k-disque` | le disque de couleur des flashs (`K.flash`) |

## Les fonctions

| Fonction | Ce qu'elle fait |
|---|---|
| `K.ic(nom)` | le SVG d'une icône (`"rocket"`) ou d'un logo ajouté (`"logo-claude"`) |
| `K.cacher(cible)` | cache dès la construction, première image comprise |
| `K.emplacements(id, CONTENU)` | le garde-fou des exemples, appelé par chaque scène prête : un emplacement resté dans son objet (« [PRÉNOM] », « [SON PRIX] », « [CHIFFRE] ») s'écrit en erreur dans la console, que `check` compte ; rend la liste |
| `K.el(parent, tag, classe, html, style)` | crée un élément |
| `K.rng(graine)` | aléatoire à graine (jamais `Math.random`) |
| `K.entre(a, b, p)` | la valeur entre `a` et `b` à la part `p` (0 à 1) : une place, une taille réparties |
| `K.cadre(el)` | `{largeur, hauteur}` de la composition qui contient `el`, lus sur `data-width` / `data-height` : ceux de l'hôte dans `index.html` d'abord, sinon de la composition la plus haute qui en porte |
| `K.duree(el)` | la durée donnée à la scène qui contient `el` (sa racine, ou son hôte une fois montée : HyperFrames retire `data-duration` de la racine intérieure au montage) |
| `K.entreeMots(tl, cible, t, {decalage, y, flou, echelle, duree, ease})` | **le mot fort du plan seulement** : il entre mot par mot en montant d'un flou qui se dissipe (46 px, 14 px de flou par défaut) |
| `K.apparition(tl, cible, t, {decalage, duree, ease})` | **les lignes d'appui, les étiquettes, un contexte** : ils paraissent nets sur place, d'un fondu de 0,18 s, sans montée, sans flou ni échelle ([metier.md](metier.md), « Le mot fort, puis des lignes nettes ») ; `decalage` pour une liste lue élément par élément |
| `K.sortieMots(tl, cible, t, {decalage, y, flou, duree, ease})` | sortie rapide (une sortie peut bouger : elle part) |
| `K.curseur(calque, id, clair)` | crée le curseur dans son calque (`clair` = blanc, sur fond sombre) |
| `K.trajet(tl, curseur, [[t, x, y, durée, courbe], …])` | déplace le curseur ; le premier point le place, dès la construction au premier trajet (même s'il est donné plus tard que 0) ; d'un coup à son instant pour un trajet suivant |
| `K.clic(tl, curseur, t)` | le curseur s'enfonce, une onde part de la pointe |
| `K.zoom(el, [x, y], echelle, {vers})` | la caméra qui amène le point [x, y] de la scène au centre du cadre (ou à `vers`), à cette échelle : rend `{scale, x, y}`, à passer tel quel à la caméra (`tl.to(cam, Object.assign({duration: 0.7, ease: K.courbeEchelle(1, z.scale, "power2.inOut")}, z), t)`) |
| `K.courbeEchelle(de, a, courbe)` | la courbe d'un zoom ou d'une plongée de l'échelle `de` à `a`, qui anime son logarithme : l'échelle paraît grandir régulièrement au lieu de ralentir |
| `K.vu(el, zoom, [x, y])` | où l'on voit à l'écran le point [x, y] de la scène quand la caméra est posée sur `zoom` : pour mener le curseur (hors de la caméra) sur ce qu'elle montre (`var p = K.vu(cam, z, [x, y])`, puis `K.trajet(tl, cur, [[0, x0, y0], [t, p[0], p[1], 0.4]])`). Exact pour ce qui est à plat dans la caméra ; une rotation de quelques degrés décale un peu |
| `K.taper(tl, el, texte, debut, fin, D)` | frappe au clavier par petits groupes de lettres (le caret est en CSS) |
| `K.compteur(tl, el, de, a, debut, duree, D, format, courbe)` | chiffre qui tourne (format libre : « 3,3 M », « 2:59:41 », « 97 € ») ; une cible qui n'est pas un nombre (l'emplacement « [CHIFFRE] » d'un exemple) s'affiche telle quelle |
| `K.texteSelon(tl, el, D, fn)` | texte qui dépend du temps (un mot qui change à un instant précis) |
| `K.champ(parent, {graine, nombre, objets, zone, evite, tailleMin, tailleMax, flouLoin, flouPres, opaciteLoin})` | répartit des objets en profondeur, flous devant et au loin ; sans `zone`, sur tout le cadre de la composition (un objet au bord peut y être coupé : donne une `zone` en retrait pour tout garder entier) |
| `K.logoNu(svg, couleur)` | fabrique d'objets pour `K.champ` : **le logo seul, sans fond** (`K.logoNu(K.ic("logo-instagram"))`) ; `couleur` pour un logo monochrome (`"#ffffff"` sur fond sombre). C'est la fabrique des objets flottants |
| `K.tuileMarque(fond, encre, svg, bord)` | un logo sur une tuile à ses couleurs : seulement pour une **icône d'application** montrée comme telle (l'écran d'accueil d'un téléphone, un dock), jamais pour les objets flottants |
| `K.tuile(classe, svg)` | fabrique d'objets génériques (à éviter pour les champs flottants) |
| `K.derive(tl, objets, debut, duree, amplitude)` | dérive lente, plus ample au premier plan |
| `K.arrivee(tl, objets, t, {etalement, duree, ease, ordre, graine})` | les objets surgissent de la profondeur en rafale, le premier en tête, les autres à des écarts inégaux (`etalement` : 0,6 s ; `duree` : 0,6 s ; `ordre: "prof"` : du proche au lointain) ; l'échelle se pose presque sans rebond (`back.out(1)`), l'opacité monte à part, sans rebond, jusqu'à celle que `K.champ` a donnée |
| `K.flash(tl, disque, x, y, t, duree)` | un disque de couleur part de (x, y) et couvre l'écran (`power3.inOut`) |
| `K.chapitre(tl, racine, curseur, t, {depart, cible})` | chapitre complet (mot fantôme, étiquette, curseur, interrupteur) ; rend l'instant de la plongée. Le clic vise l'interrupteur d'après la taille de la composition, en 9:16 comme en 16:9 ; `cible: [x, y]` seulement si le CSS de la scène a déplacé l'interrupteur |
| `K.jeton(nom)` | la valeur d'un jeton de la marque (`K.jeton("--brand-gris-2")`), pour un tween de couleur (GSAP n'interpole pas une variable CSS) |

### Les objets connus, dans leurs vraies couleurs

Ce que tout le monde reconnaît garde son vrai visage ([metier.md](metier.md), « Les objets connus ») :
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
| `K.ordinateur(parent, {largeur, capture, ouvert, teinte})` | **seulement s'il le demande** (plus bas) : un ordinateur portable en perspective, son couvercle sur sa charnière, son écran qui porte sa vraie capture, son clavier, son pavé tactile, en alu (`teinte: "gris"` : l'alu sombre) ; rend `{racine, couvercle, ecran, image, base}` |

**L'ordinateur qui s'ouvre sur sa page, seulement à sa demande** (« un effet 3D », « mon ordinateur
qui s'ouvre », « ma page sur un portable ») : c'est une maquette correcte, pas un moment signature.
Sans demande de sa part, sa page se montre comme d'habitude en motion design : à plat, en grand, dans
la fenêtre du kit, en perspective, et elle agit. Posé dans la caméra d'un `k-scene3d`, reculé et
incliné pour qu'on voie son clavier, il s'ouvre, puis sa page défile. Le même code se cadre en 16:9
et en 9:16 :

```js
var cam = document.getElementById("s4-cam"), c = K.cadre(cam), v = c.hauteur > c.largeur, L = v ? 900 : 1150;
var ordi = K.ordinateur(cam, { largeur: L, capture: "assets/images/page.png", ouvert: 0 });   // fermé au départ
gsap.set(ordi.racine, { left: (c.largeur - L) / 2, top: v ? 560 : 120, z: -L * 0.9, rotationX: -18, rotationY: -14 });
tl.to(ordi.couvercle, { rotationX: 12, duration: 1.2, ease: "expo.out" }, 0.3)        // il s'ouvre
  .to(ordi.image, { y: -900, duration: 2.6, ease: "sine.inOut" }, 1.6);             // puis sa page défile
```

`couvercle` : `rotationX` de -86 (fermé) à 12 (ouvert, un peu en arrière). `image` : une capture
longue de sa page défile par `y`. Recule-le (`z`, environ 0,9 fois sa largeur) : trop près de la
caméra, sa base déborde du cadre. Pour plonger dans l'écran, la caméra s'approche (`scale`) jusqu'à
ce que l'écran remplisse l'image (`K.zoom`), puis son interface reconstruite prend le relais.

Partout où une scène prend une icône (`icone` d'un `CONTENU`, `K.ic`), un `objet-…` se met à la
place d'une icône d'un seul trait quand l'idée a un objet connu. Ces couleurs ne débordent jamais sur un fond, un texte ou un
trait ; `palette` les connaît.

### Le mot qui joue, le schéma, le fil conducteur, la coupe

Des façons de faire jouer un mot, de tracer un schéma, de trancher l'écran ([ambition.md](ambition.md),
principe 3). `cible` accepte un sélecteur, un élément ou une liste.

| Fonction | Ce qu'elle fait |
|---|---|
| `K.lettres(el)` | découpe le texte en lettres (`span.k-lettre`), rend la liste : pour une rafale de lettres |
| `K.claque(tl, cible, t, {de, y, rotation, decalage, duree, ease})` | le mot arrive d'un coup, plein (aucun fondu : rien ne vire à l'olive sur l'accent), à l'échelle `de` (1,45 : il se pose en rétrécissant ; 0,4 : il grandit), et se pose ; `decalage` pour une rafale |
| `K.etire(tl, cible, t, {axe, facteur, tenue, retour, duree, decalage, origine})` | le mot (ou ses lettres) s'étire puis revient : `axe: "x"` en largeur (`"y"` par défaut), `facteur` 1,7, `tenue` 0,6 s avant le retour, `retour: false` pour qu'il reste étiré, `duree` de l'aller (0,35 s), `decalage` entre deux lettres, `origine` (le bas du mot, ou son bord gauche en `x`) |
| `K.barre(tl, el, t, {angle, eteindre})` | une barre pleine de l'accent raye l'élément ; `eteindre` : la couleur qu'il prend ensuite (`K.jeton("--brand-gris-2")`) |
| `K.surligner(tl, el, t, {couleur, encre})` | un bloc plein s'ouvre derrière le mot, de gauche à droite ; `couleur` du bloc (l'accent par défaut ; l'encre sur l'aplat), `encre` du mot |
| `K.volet(tl, cible, t, {decalage, origine})` | des blocs (étiquettes, pastilles pleines, pistes) s'ouvrent depuis leur bord, en rafale |
| `K.lien(parent, [x1, y1], [x2, y2], {svg, courbe, classe, taille})` | un lien courbe d'un schéma (SVG `k-liens`, aux pixels de la composition), rend le chemin ; `svg` pour en ajouter au même dessin ; `courbe` : son bombé (0,25 ; 0 : droit) ; `classe: "k-lien-discret"` pour un trait gris ; `taille: {largeur, hauteur}` pour un dessin plus grand que le cadre (une toile qui défile) |
| `K.trace(tl, chemin, t, duree, {ease, longueur})` | le trait se dessine de son début à sa fin (`power2.inOut` par défaut) ; `longueur` quand le chemin ne se mesure pas encore (une coche dans une icône : 30) ; rend sa longueur |
| `K.longer(tl, el, chemin, t, duree, D, {de, a})` | le fil conducteur (`k-fil`) suit le trait ; même durée et même courbe que `K.trace` : il en dessine la pointe. `el` ne prend aucun autre mouvement x / y |
| `K.tranche(tl, calque, t, {de, a, duree, ecart})` | la coupe : un trait de l'accent fend l'écran en biais (de `de` à gauche à `a` à droite, en part de la hauteur : 0,64 et 0,36), le calque (plein cadre) se fend et ses moitiés tombent en `duree` (0,55 s), écartées de `ecart` (les trois quarts de la hauteur). **Appelée en dernier**, la timeline complète : elle fige une copie du calque à l'instant t (jamais de `<video>` dedans) |

| Classe | Rôle |
|---|---|
| `k-heros` | le mot héros : 1 à 3 mots, très gras, serrés, qui remplissent la largeur |
| `k-contour` | le mot en contour net (un trait plein, `--k-contour`), pour doubler un mot plein ; jamais une lueur |
| `k-blocs` > `span.k-bloc-accent` · `k-bloc-clair` · `k-bloc-sombre` | les étiquettes de fonction : deux ou trois mots en blocs empilés |
| `k-noeud` (`k-noeud-sombre`, `k-noeud-accent`) | un nœud de schéma (logo + nom) |
| `k-fil` | le fil conducteur : le point de l'accent |

## Les pièges (tous rencontrés)

- **Le flou de bougé** est réglé sur `#root` d'`index.html` (`data-motion-blur="on"
  data-motion-blur-tier="capture" data-motion-blur-shutter="180"`) : posé seulement sur la racine
  d'une scène, il ne s'applique pas (aucune ligne `[motion-blur]` dans le journal du rendu). Le
  journal dit comment il a été calculé (`[motion-blur] on … tier=…`) : `tier=capture` est normal.
  Un `filter fallback` se corrige : `reasonCode=tier-auto`, c'est que `data-motion-blur-tier="capture"`
  manque (depuis HyperFrames 0.9.20, le mode automatique n'adoucit plus que les rotations et les
  zooms) ; sinon un `backface-visibility: hidden` dans une scène en 3D : pour retourner une carte,
  échange ses deux faces à 90° plutôt que de cacher la face arrière ; un volume fermé et opaque
  (le cube du style 8, l'ordinateur du kit) se trie seul en profondeur, ses faces écartées de 1 ou
  2 px ; sinon `data-motion-blur="off"` sur ce sous-arbre. Le kit n'en pose aucun. N'anime jamais `#root`
  lui-même (transformation, opacité) : le flou s'éteint. Un projet créé avant ce réglage ne l'a pas :
  ajoute les trois attributs sur `#root`, puis `npm run check`. **Le flou n'existe que dans un rendu entier** : les images de
  `snapshot` et un extrait `render --start/--end` (« distributed-render » dans le journal) en sont
  privés. La traîne et l'allure d'un geste rapide se jugent sur la planche du MP4 entier.
- **Ce qui se rend mal** (le flou de bougé et l'encodage, mesurés le 09/11/2026) :
  - `backdrop-filter` (le verre dépoli) et `mix-blend-mode` sur un objet qui bouge, ou sur un de ses
    parents, disparaissent dans le mode de flou qui rend les rotations : le verre seulement sur un
    panneau immobile, sinon `data-motion-blur="off"` sur ce sous-arbre.
  - Un masque ou un `clip-path` sur un objet qui bouge prend des bords durs : masque un parent
    immobile et anime l'enfant dedans (comme `.clip`).
  - Une opacité ou un `filter` sur un élément en `preserve-3d` l'aplatit et montre ses deux faces :
    fais disparaître son enveloppe (un parent sans 3D), jamais l'élément en perspective. Un flou de
    profondeur se pose sur ce qui est à plat : la matière d'une carte (`preuve`), la bulle dans sa
    pose (`messages`), une station sans `k-plan` (`parcours`), l'espace `k-scene3d` qui porte toute
    la caméra (`situation`).
  - Un flou de bougé fait à la main (un `filter: blur` pendant un mouvement) s'ajoute à celui du
    rendu : jamais. Un flou voulu (la profondeur, une matière qui passe au second plan) se pose
    hors d'un mouvement, ou dure plus que lui.
  - Une transformation CSS (`transform`) sur un élément que GSAP déplace : GSAP la lit et la
    réécrit. Place-le par `inset`, une marge ou `xPercent` (le kit place ainsi le mot fantôme).
  - `will-change: transform` n'aide pas au rendu, et sur un objet que la caméra ou un zoom agrandit,
    Chrome le dessine à sa taille de départ : il reste flou une fois grand. Ne le pose jamais : ni
    le kit ni les exemples n'en posent (un test l'interdit dans `templates/` et dans les styles).
  - Un grand dégradé linéaire sombre en plein cadre fait des bandes à l'encodage (des marches de
    130 px) : un aplat, un dégradé radial, ou un aplat avec une lueur locale.
  - Une capture d'écran filmée de son produit posée dans la vidéo : `npm run render --
    --video-frame-format png` (l'extraction en JPEG abîme les aplats et le texte fin).
- **Un identifiant intérieur égal à celui de l'hôte** d'une scène dans `index.html` (`a04-hote`) :
  `getElementById` trouve l'hôte, plein écran, et l'objet s'y pose en haut à gauche, sans les styles
  de la scène (un dossier en Times dans le coin). Les éléments d'une scène
  ne finissent jamais par `-hote` : le calque du curseur ou de la main s'appelle `-calque`
  (`s3-curseur-calque`).
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
- Un panneau plein écran qui doit couvrir la scène 3D lui donne un `z-index` plus haut que
  `k-scene3d`, ou donne `z-index` à `k-scene3d` pour qu'elle reste devant.
- **L'écran du téléphone** : seule une image posée directement dans `k-tel-ecran` (son enfant
  direct) prend tout l'écran ; un site ou une app reconstruits dans l'écran gardent leurs images
  (une couverture, des cartes) à leur taille. Un projet créé avant le 09/11/2026 a l'ancienne
  règle (toute image de l'écran en plein écran) : recopie `kit.css`.
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
- **Les intentions et `check`** (`composition.md`, règle 10) : `data-accroche` et `data-prix` vont
  chacun sur un seul élément de toute la vidéo (une scène d'ouverture copiée deux fois en porte
  deux : `motion_selector_ambiguous`) ; une règle sans élément donne `motion_selector_missing`.
  `check` juge l'accroche à son opacité et à sa taille, pas à un masque : une phrase qui se tape
  ou s'imprime derrière un masque doit se lire à 0,5 s sur l'image elle-même.
- **Le point final de l'appel et `check`** (08/11/2026) : `K.longer` suit son trait sur toute la
  durée de la scène ; dans la scène de fin, `check` croit alors que la dernière ligne (le nom, le
  bouton) n'est lue que 0,75 s. Pour ce dernier trajet, fais suivre le trait seulement pendant le
  trajet (un tween de 0 à 1 avec `onUpdate` qui place le point, posé au départ par un premier appel).
- **Des lettres en désordre** (un mot qui « joue » le chaos avant de se remettre en ligne) se
  chevauchent pour `check` (`content_overlap`) : écart vertical de ±15 px et rotation de ±7° au
  plus, puis `data-layout-allow-overlap` sur la ligne, après avoir vérifié à l'image qu'elle se lit.
