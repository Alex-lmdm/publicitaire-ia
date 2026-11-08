# Style n°1 · Cartes pixels · d'après Firecrawl (https://x.com/firecrawl/status/2057495269785358384)

**Ce qu'on voit :** sur une grille claire à points, des cartes d'interface passent du désordre au net : un mur de cartes floues autour d'une discussion sombre, des blocs de pixels qui couvrent puis découvrent l'écran, des pixels de couleur qui deviennent une fiche annotée de cadres, un grand chiffre dans des glyphes, les logos des outils reliés au sien, un chevron en escalier qui blanchit l'écran pour le logo final.
**Souvent utile pour :** montrer le passage du problème (trop d'infos, trop d'outils, trop de conseils) au résultat propre ; une méthode, un logiciel ou une formation qui « met de l'ordre ».
**D'après :** post X de Firecrawl, « From web noise to working UI » · 66 s · 16:9 · musique électronique, sans voix, presque sans texte.

## 1. Le rythme

- **Le contenu vit toutes les 0,3 s** : un pixel qui s'allume, une ligne qui se décode, un cadre qui se pose. Rien ne reste immobile plus d'une seconde, sauf l'écran final.
- **Les rafales** : les pixels, les cartes et les cadres arrivent en cascade (0,02 à 0,32 s d'écart), jamais un par un à intervalle lent.
- **La caméra, elle, est calme** : une dérive lente pendant qu'on lit (4 à 5 % sur la tenue, `sine.inOut`), et un seul recadrage net quand l'intention change, entre deux phrases (0,45 à 0,7 s, `expo.out` ou `expo.inOut`) : la question qui part, les pixels qui deviennent la fiche. Jamais un pas de caméra vers chaque cadre.
- **Peu de coupes franches** : presque tout passe d'une scène à l'autre par un objet (le panneau devient une case, les pixels deviennent une carte) ou par la mosaïque de pixels.
- **Peu de texte** : un label mono et une étiquette de 2 à 4 mots par scène ; le reste est l'interface montrée.
- **Chez toi :** la grille de 0,5 s du studio ou celle de la musique (environ 1,4 événement par seconde dans le kit). Au milieu (la carte annotée, les logos), les cadres qui se posent font la vie : jamais une tenue vide ni un recadrage ajouté.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le mur de bruit | la carte de discussion sombre, la question qui se tape, un mur de réponses grises et floues qui se lève autour | accroche, problème | `t01-bruit` |
| La mosaïque de pixels | des blocs de pixels qui couvrent l'écran par à-coups, puis tombent rangée par rangée | raccord entre deux scènes, ouverture d'un chapitre | `t01-raccord-pixels` |
| Les pixels qui deviennent l'interface | un amas de pixels à l'accent glisse et devient la fiche de l'offre (avec sa vraie capture dans l'aperçu), que des cadres de repérage annotent en cascade | solution, démonstration de son produit | `t01-carte-annotee` |
| Le décodage | chaque texte arrive en glyphes qui se fixent de gauche à droite | tous les textes : labels, titres, nom | toutes les scènes |
| Le grand chiffre dans les glyphes | un vrai chiffre qui compte au milieu d'un nuage de glyphes | preuve (seulement avec un vrai chiffre) | `t01-chiffre` |
| Les logos reliés et le chevron | les logos de ses outils reliés à l'offre, le chevron en escalier, le nom en pixels, le bouton tapé et cliqué | outils, offre, appel | `t01-logos-fin` |

**Pour montrer son produit** : en chapitres, chacun ouvert par son label mono « [ 03 · … ] » et
une carte d'interface réelle ; une mosaïque de pixels entre deux chapitres, une fois sur deux au plus.

### Des enchaînements qui marchent

Une vidéo de page de 60 à 90 s qui raconte un problème puis sa solution :

1. **Problème** (5,5 s) : `t01-bruit`, la question du prospect, le mur de bruit, l'étiquette du problème.
2. Raccord : `t01-raccord-pixels` par-dessus la coupe.
3. **Solution** (6,5 s) : `t01-carte-annotee`, les pixels deviennent la fiche de l'offre, annotée.
4. **Démonstration** (20 à 40 s) : deux ou trois chapitres, chacun ouvert par son label mono et une carte d'interface réelle, construite dans ce style.
5. **Preuve** (3,4 s) : `t01-chiffre`, seulement avec un vrai chiffre.
6. **Outils, offre et appel** (9 s) : `t01-logos-fin`, les logos reliés, le chevron, le nom, le bouton.

## 3. Les fonds et les couleurs

**Les objets connus gardent leurs vraies couleurs**, dans ce style comme dans tous les autres : le
dossier bleu du Mac et les fichiers du kit (`K.ic("objet-…")`), le téléphone et sa barre d'état, la
notification et les bulles d'iPhone, les vrais logos de ses outils, l'interface d'une plateforme
reconstruite d'après capture. Ce sont les touches de couleur vraie du film ; tout le reste prend
les rôles ci-dessous ([image.md](../../references/image.md), « Les objets connus »).

| Rôle | Avec la marque du client |
|---|---|
| Fond de toute la vidéo | son clair (`var(--brand-clair)`), à peine grisé par un noir à 3 % |
| Grille | des noirs en transparence (traits à 7 %, points à 8,5 %) ; quelques cases (noir à 3 %) s'allument par à-coups |
| Trame de glyphes du bas | `var(--brand-gris-4)`, au bas de l'écran (de la texture) |
| Cartes, panneaux, tuiles, fin | `var(--brand-clair)`, un filet noir à 8 %, une ombre neutre douce |
| Accent : pixels, point qui voyage, cadres, chiffre, chevron, bouton, étiquettes | `var(--brand-accent)`, plein ; le texte dessus en `var(--brand-contrast)` |
| Chargeur en pixels | sa couleur et `var(--brand-gris-3)`, `var(--brand-gris-4)` |
| Carte de discussion sombre | sa nuit (`var(--brand-sombre)`) ; la bulle `var(--brand-gris-2)`, la réponse et le champ `var(--brand-gris-1)`, le texte `var(--brand-clair)` |
| Mosaïque de pixels | sa nuit et ses deux premiers gris, avec un sur six de ses gris clairs (`var(--brand-gris-3)`, `var(--brand-gris-4)`) |
| Textes d'appui sur le clair (label, appui des titres, genre, promesse) | `var(--brand-gris-2)` (4,5:1 sur le clair ; jamais `var(--brand-gris-3)`) |
| Aperçu de la fiche | sa vraie capture, dans ses propres couleurs ; sans capture, pas d'aperçu |

- **Accent clair** (jaune, vert pâle, luminance au-dessus de 0,28) : il ne se lit pas en trait fin sur le clair. Le kit le détecte seul (classe `t01-accent-clair`) : les cadres de repérage passent à l'encre, l'accent reste en aplat (pixels, étiquettes, surlignage, chevron, bouton). Le chiffre, qui est un texte, passe à l'encre plus tôt, dès que l'accent ne s'y lit plus à 4,5:1 (luminance au-dessus de 0,17), souligné d'un trait plein de sa couleur.
- Ce qui serait une teinte pâle de l'accent (le chargeur, l'éclair d'un cadre) est un gris, pour toutes les marques.
- Clair presque partout, deux passages sombres (la discussion, la mosaïque) et le clair pur de la fin : ce style n'alterne pas sombre, clair et couleur pleine comme le style par défaut du studio, c'est voulu.

## 4. La typographie

- **Interfaces** (discussion, fiche, boutons) : Inter, livrée dans chaque projet. **Labels, étiquettes, données** : la mono de la marque, sinon celle du système (SF Mono, Menlo, Consolas).
- **Titres** : la police de titres de la marque, deux graisses dans une étiquette claire, l'appui en 400 (`var(--brand-gris-2)`), le mot fort en 700 surligné à l'accent.
- **Chiffre et nom final** : police de titres en 700, très serrée (-0,045 em) ; ce sont les mots héros : la scène règle leur taille pour qu'ils occupent environ 60 % de la largeur (80 % en 9:16).
- **De la texture** (`data-layout-ignore`) : le mur de bruit, les glyphes, « Réponse », l'invite et la frappe du champ (la question se lit dans sa bulle).

| Texte | 1920 × 1080 | 1080 × 1920 | Casse, alignement |
|---|---|---|---|
| Label mono « [ 01 · LE PROBLÈME ] » | 28 px, espacement 0,14 em | 30 px | capitales, entre crochets, à gauche, en haut |
| Étiquette-titre (2 à 4 mots) | 66 px | 72 à 76 px | phrase, à gauche, sous le label |
| Texte de la discussion (question, réponse) | 30 px | 34 px | phrase |
| Fiche : titre, prix, promesse | 64, 56 et 30 px | 68, 62 et 34 px | phrase, à gauche |
| Fiche : genre, pastilles | 28 px mono | 30 px | phrase |
| Étiquette d'un cadre | 28 px mono, gras | 28 px | capitales, sur l'accent |
| Grand chiffre | environ 60 % de la largeur, 400 px au plus | 80 %, 300 px au plus | centré |
| Étiquette du chiffre | 32 px mono | 32 px | minuscules, centrée dans sa pastille |
| Nom final | environ 60 % de la largeur, 240 px au plus | 80 %, 220 px au plus | centré, à côté du logo (dessous en vertical) |
| Bouton | 42 px | 42 px | phrase, centré |

## 5. Les mouvements signature

1. **La mosaïque de pixels** (`t01-raccord-pixels`, 1,45 s) : des blocs de 240 px, coupés en 2 × 2 pixels de tons différents (un sur six clair), surgissent par à-coups, sans fondu, des bords vers le centre en 0,6 s ; un pixel sur cinq clignote en gris clair 0,07 s. L'écran couvert grossit de 4 %, puis les blocs tombent rangée par rangée du haut vers le bas en 0,3 s.
2. **Les pixels qui deviennent l'interface** (`t01-carte-annotee`) : un amas en croix de 12 pixels à l'accent (84 px, pas de 124 px : près de la moitié de la hauteur) s'allume en vague, ses teintes tournent toutes les 0,12 s ; puis chaque pixel glisse et s'étire jusqu'à un bloc de la fiche (0,65 s, `expo.inOut`) pendant que la carte grandit et que la caméra fait son seul recadrage vers elle ; avec sa vraie capture, l'aplat de l'aperçu se dissout en pixels (0,5 s) et découvre la capture, qui recule doucement (×1,06 → ×1 en 2,4 s).
3. **Le décodage** (toutes les scènes) : chaque texte arrive en glyphes (# % @ X = + : * / < >) renouvelés toutes les 0,045 s, qui se fixent de gauche à droite en 0,4 à 0,6 s.
4. **Les cadres de repérage** (`t01-carte-annotee`) : un cadre de 2 px se pose sur une partie de la fiche (de 112 % à 100 %, 0,3 s, `expo.out`), un éclair gris s'y éteint, son étiquette monte de 8 px (`back.out`) ; un cadre toutes les 0,32 s, la caméra en dérive lente (4,5 %) : la cascade est la vie du plan.
5. **Le chiffre dans les glyphes** (`t01-chiffre`) : les hachures s'ouvrent, le chiffre compte jusqu'à sa valeur en 1,25 s (`expo.out`) dans un nuage de glyphes qui s'éteint par le centre ; six points s'allument du centre vers les bords ; le chiffre compté se tient 1,6 s.
6. **Le chevron en escalier** (`t01-logos-fin`) : quatre couches en marches de 54 px partent du bord droit l'une après l'autre (0,16 s d'écart, 1,05 s chacune, `power2.in`) : une grille de cellules, l'accent, un gris, le clair qui couvre tout.

## 6. Les transitions

- **La mosaïque de pixels sombres** : le raccord signature, deux ou trois fois par vidéo de page, jamais deux fois de suite, sur la piste 2 par-dessus la coupe.
- **Le raccord d'objet** : le panneau du chiffre se resserre en case blanche qui reçoit le logo ; les pixels deviennent la fiche.
- **La dissolution en pixels** : un aplat (l'aperçu, le logo final, la case du centre) se découvre par carrés qui tombent dans le désordre.
- **Le chevron en escalier** : une seule fois, pour passer à la fin.
- **La coupe franche** : rare, sur un temps fort de la musique.
- Jamais de fondu enchaîné entre deux écrans chargés.

## 7. Le produit à l'écran

- Le produit devient des **cartes d'interface simplifiées** (une discussion, une fiche qu'on annote, des données, une connexion) : chacune fait une seule chose, lisible en une seconde, assez près pour que ses mots utiles fassent 28 px au moins.
- **Chez toi** : l'offre devient une fiche claire (nom, genre, prix exact, promesse, 3 pastilles) avec **sa vraie capture** dans l'aperçu (miniature de leçon, sa page, l'écran du logiciel, photo de séance) ; sans capture, la fiche se resserre sur son texte. Les cadres repèrent ce qui fait vendre ; la discussion porte la vraie question du prospect ; les tuiles, les vrais logos des outils de l'offre (`studio_motion.py logos`), jamais ceux de ses clients sans leur accord. Une interface qu'il n'a pas ne s'invente pas.

## 8. Le son

- **Musique de l'original** : électronique sèche et percussive, environ 92 battements par minute, faite de clics, de bips et de grésillements numériques plus que de mélodie, avec de courts silences nets (juste avant le logo final).
- **Chez toi** : l'ambiance « Tech minimale » des musiques de lancement (`musiques choisir --ambiance "Tech minimale"`), l'entrée de batterie calée sur l'arrivée de la fiche (le pivot).
- **Bruitages**, légers et numériques, jamais d'impact grave : des clics secs pour la mosaïque, un bip court par cadre (pas un par pixel), la frappe pour la question et le bouton, un « ding » léger pour le maillon, un souffle doux pour le chevron, un clic et un petit « pop » pour le bouton final.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 1`) : « Tech minimale », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture** : `t01-bruit`, la carte là dès la première image et la question qui se tape.
- **Fin** : le chevron, le clair, le logo en pixels et le nom qui se décode, puis le bouton tapé et cliqué ; l'écran final se tient 3 s. Sans logo, le nom seul.

## Sur une autre offre

C'est un look : il se pose sur toute offre. Ce qui suivait le produit de l'original s'adapte :

- **Formation** : la discussion porte la question des élèves (« Par où je commence ? ») ; la fiche est la formation (genre « Formation · En ligne », pastilles Vidéos, Modèles, Bonus), l'aperçu la capture d'une vraie miniature de leçon ; le chiffre compte les élèves ; les tuiles sont les outils enseignés.
- **Coaching** : la discussion porte ce que les clients disent au premier appel ; la fiche est l'accompagnement (format, durée, séances), l'aperçu une photo de séance ou l'agenda réel ; le chiffre compte les clients accompagnés ; les tuiles, seulement les outils vraiment utilisés (visio, suivi).
- **Logiciel** : le bruit, ce sont les dix outils ou onglets qu'il remplace ; la fiche est son écran principal (capture réelle dans l'aperçu), les cadres repèrent ses fonctions ; le chiffre compte les utilisateurs ; les tuiles sont ses intégrations réelles.
- **Toujours** : la grille claire, les pixels, le décodage, la mosaïque, les cadres, le chevron, l'accent seul en couleur, toujours plein ; dans l'aperçu, sa vraie capture ou rien.

## En vertical et en carré

- **9:16 (1080 × 1920)** : mets `data-width="1080" data-height="1920"` sur la racine de chaque composition et sur son hôte ; la mise en page se règle seule (classe `t01-vertical`) : mur de bruit en 3 colonnes, discussion de 920 px, fiche en colonne (sa capture en haut, 848 × 500), labels et étiquettes en haut dans la zone sûre (x 100, y 300 et plus), tuiles réparties en hauteur, logo au-dessus du nom à la fin.
- **4:5 et carré** : pas de mise en page propre, non testé. En 4:5, la mise en page verticale s'applique seule (dessinée pour 1920 de haut) ; en carré, force-la (`vertical = true`). Puis réduis la caméra de chaque scène (`scale` 0,7 en 4:5, 0,56 en carré) et remonte labels et étiquettes vers y = 120. À vérifier image par image.

## Les compositions du kit

Dossier `compositions/`, 16:9 par défaut, chacune avec son en-tête (ce qu'elle montre, sa durée, ce qu'on remplace). Elles se servent du kit du projet (`K`) et des variables de la marque (`--brand-*`) ; les identifiants commencent par `t01-`. Chaque texte, chiffre et nom d'exemple est dans l'objet `EXEMPLE` en tête du script : sa valeur vient d'`OFFRE.json`, ou sa ligne se retire.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (`EXEMPLE`) |
|---|---|---|---|
| `t01-bruit.html` | 5,5 s | Problème : la discussion sombre, la question tapée, la réponse, le mur de bruit, l'étiquette | `etiquette`, `titre` (2 à 4 mots), `question` (celle du prospect), `reponse` (2 ou 3 lignes courtes), `bruit` (10 à 14 phrases du domaine, le décor), `qui` et `invite` (l'interface) |
| `t01-raccord-pixels.html` | 1,45 s | Raccord : la mosaïque de pixels sombres | aucun texte ; l'id (un par raccord) et `GRAINE` |
| `t01-carte-annotee.html` | 6,5 s | Solution : le chargeur, les pixels qui deviennent la fiche, le décodage, l'aperçu sur sa vraie capture, les cadres en cascade | `etiquette`, `titre`, `genre`, `prix` (exact, ou "" : la ligne se retire), `lignes` (la promesse), `pastilles`, `capture` (ou "" : pas d'aperçu), `reperes` (étiquettes et cibles) |
| `t01-chiffre.html` | 3,4 s | Preuve : le chiffre qui compte dans les glyphes, son étiquette ; sortie en case blanche | `etiquette`, `nombre` (le vrai chiffre, sinon pas de scène), `libelle` |
| `t01-logos-fin.html` | 9 s | Outils et fin : les tuiles d'outils, le maillon, le chevron, le logo et le nom, le bouton tapé et cliqué, l'écran final tenu 3 s | `logos` (les vrais outils), `outil` (celui qu'on relie), `logo` (ou "" : son nom à la place), `nom`, `titre`, `bouton` |

Le montage dans `index.html` (16:9) : les scènes bout à bout sur la piste 1, le raccord sur la piste 2, au-dessus, démarrant 0,8 s avant la coupe :

```html
<div id="s1-hote" data-composition-id="t01-bruit" data-composition-src="compositions/t01-bruit.html" data-start="0" data-duration="5.5" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="r1-hote" data-composition-id="t01-raccord-pixels" data-composition-src="compositions/t01-raccord-pixels.html" data-start="4.7" data-duration="1.45" data-track-index="2" data-width="1920" data-height="1080" style="z-index:3;"></div>
<div id="s2-hote" data-composition-id="t01-carte-annotee" data-composition-src="compositions/t01-carte-annotee.html" data-start="5.5" data-duration="6.5" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s3-hote" data-composition-id="t01-chiffre" data-composition-src="compositions/t01-chiffre.html" data-start="12" data-duration="3.4" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s4-hote" data-composition-id="t01-logos-fin" data-composition-src="compositions/t01-logos-fin.html" data-start="15.4" data-duration="9" data-track-index="1" data-width="1920" data-height="1080"></div>
```

Avant de monter `t01-logos-fin` : `python3 ../../../tools/studio_motion.py logos . claude chatgpt …` depuis le projet, avec les outils de l'offre. Un second raccord dans la même vidéo prend un autre id (`t01-raccord-2`) et une autre graine.
