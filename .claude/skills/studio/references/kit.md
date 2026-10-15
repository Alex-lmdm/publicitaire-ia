# Le kit : les briques de chaque scène

Chaque projet reçoit `kit/` (chargé par `index.html`) : les fonds vivants, le curseur, les objets
flottants, le chapitre, les fenêtres, le téléphone, les textes à deux graisses, et des fonctions
GSAP déterministes. **Pars de lui** : il porte le niveau de finition, et c'est lui qu'on améliore
d'une vidéo à l'autre. Les recettes complètes (enchaînements éprouvés) sont dans `recettes.md`.

Fichiers : `kit.css` (classes `k-*`), `kit.js` (objet `K`), `icones.js` (82 icônes Lucide),
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

## Les classes

| Classe | Rôle |
|---|---|
| `k-scene` | conteneur plein cadre de la scène |
| `k-fond k-fond-sombre` · `k-fond-clair` · `k-fond-jaune` | fonds : gris anthracite fixe (`#1b1b1d`, il ne suit pas `--brand-bg`) avec grille fine, blanc cassé avec grille, couleur d'accent pleine |
| `k-vignette` · `k-vignette-claire` | assombrit les bords (à placer sous le sujet si un plein écran de couleur doit rester pur) |
| `k-scene3d` > `k-camera` | l'espace en perspective et la caméra qu'on anime (`scale`, `rotationX/Y/Z`, `x`, `y`) |
| `k-plan` | un objet placé dans l'espace 3D |
| `k-titre`, `k-mot`, `k-leger`, `k-accent` | titres à deux graisses ; chaque `k-mot` entre séparément |
| `k-chapitre` > `k-fantome` + `k-etiquette` + `k-interrupteur` (`k-plein`, `k-bille`) | le motif des chapitres ; variantes `k-sur-sombre`, `k-sur-clair`, `k-sur-jaune` ; le fantôme fait 15,625 % de la largeur (300 px en 16:9, 169 px en 9:16) |
| `k-fenetre` + `k-feux` | fenêtre d'application (coins, ombre, trois points) |
| `k-tel` > `k-tel-ecran` (+ `k-tel-ilot`) | téléphone ; une image ou des calques dans l'écran |
| `k-tuile` (`k-tuile-sombre`, `-jaune`, `-blanche`) | tuile d'icône des champs flottants |
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

## Les pièges (tous rencontrés)

- **État de départ** : `K.cacher` ou `gsap.set` à la construction, jamais `tl.set(…, 0)` (la
  première image montrerait l'élément). Même chose pour la position de départ d'un curseur ou
  d'un disque (le kit le fait).
- `K.arrivee` lit l'opacité donnée par `K.champ` : ne cache pas le champ avant de l'appeler.
- `flouPres: 0` et `flouLoin: 0` valent bien zéro (logos nets) ; sans eux, le flou par défaut
  s'applique.
- Le kit d'un projet est une copie : si le kit du dossier change pendant la fabrication,
  recopie `kit.js` et `kit.css` dans le projet, sinon une fonction manque et la scène reste figée
  (toutes ses images identiques).
- Un panneau plein écran qui doit couvrir la scène 3D lui donne un `z-index` plus haut que
  `k-scene3d`, ou donne `z-index` à `k-scene3d` pour qu'elle reste devant.
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
  le reçoit dans le HTML. Cet attribut est réservé à la typographie décorative : jamais sur un
  texte qu'on doit lire.
