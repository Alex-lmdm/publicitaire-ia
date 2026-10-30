# Template n°1 · Cartes pixels · d'après Firecrawl (https://x.com/firecrawl/status/2057495269785358384)

**Ce qu'on voit :** sur une grille claire à points, des cartes d'interface passent du désordre au net : un mur de cartes floues autour d'une discussion sombre, des blocs de pixels qui couvrent puis découvrent l'écran, des pixels de couleur qui deviennent une fiche blanche annotée de petits cadres. La preuve tombe en grand chiffre au milieu de glyphes (# + X =), les logos des outils se relient au logo de la marque, et un chevron en escalier blanchit l'écran pour le logo final.
**Souvent utile pour :** montrer le passage du problème (trop d'infos, trop d'outils, trop de conseils) au résultat propre ; une méthode, un logiciel ou une formation qui « met de l'ordre ».
**D'après :** post X de Firecrawl, « From web noise to working UI » · 66 s · 16:9 (1920 × 1080, 24 images/s) · musique électronique, sans voix, presque sans texte.
**Mesures (`studio_motion.py reference`) :** 1,82 événement par seconde, écart médian 0,30 s, 10 coupes franches détectées en 66 s (vers 6,6, 10,8, 20,8, 26,1, 31,2, 32,0, 36,7 et 40,0 s), 4,0 s d'image tenue (le logo final). Par tranche de 6 s : de 1,0 à 2,7 événements par seconde. Tempo de la musique : environ 92 battements par minute.
**Essai du kit (marque LMDM, 21,6 s) :** 1,56 événement par seconde en 16:9 (écart médian 0,30 s), 1,44 en 9:16 (0,40 s), aucune image figée, `rythme` « ok » dans les deux formats.

> On reprend la grammaire de la vidéo (grille, cartes, pixels, glyphes, cadres de repérage, chevron), jamais son contenu : ni ses textes, ni son logo, ni ses images (veste, fauteuils, pages web), ni son produit, ni sa musique. L'orange de Firecrawl devient la couleur de la marque du client.

## 1. Le rythme

- **Toutes les 0,3 s, un geste** : un pixel qui s'allume, une ligne qui se décode, un cadre qui se pose, la caméra qui recadre. Rien ne reste immobile plus d'une seconde, sauf le logo final (4 s).
- **Peu de coupes franches** (10 en 66 s) : presque tout passe d'une scène à l'autre par un objet (le panneau devient une case, les pixels deviennent une carte) ou par les blocs de pixels.
- **La caméra ne s'arrête jamais** : poussée lente pendant qu'on lit (4 à 6 % sur 2 à 3 s, `sine.inOut`), puis recadrage net à chaque nouvelle intention (0,3 à 0,85 s, `expo.out` ou `expo.inOut`) vers la partie qui compte.
- **Les rafales** : les pixels et les cartes arrivent en cascade (0,02 à 0,1 s d'écart), jamais un par un à intervalle lent.
- **Pas de texte à lire dans l'original.** Le kit en ajoute un minimum (un label mono et une étiquette de 2 à 4 mots par scène), parce qu'une vidéo de page démarre muette.
- **Chez toi :** grille de 0,5 s du studio (120 battements par minute) ou celle de la musique ; les scènes du kit tiennent 1,4 à 1,6 événement par seconde. Le milieu (la carte annotée, les logos) est le plus calme : n'y ajoute pas de tenue.

## 2. La structure

L'original, scène par scène :

| Temps | Rôle | Ce qui s'y passe |
|---|---|---|
| 0 à 3 s | Accroche | Une structure de pixels gris, un orange, un noir, se monte en perspective et tourne ; aucun mot. |
| 3 à 6,6 s | Problème | La carte de discussion sombre (question, « réflexion », réponse) ; la caméra pousse, un mur de réponses grises et floues se lève autour : le bruit. |
| 6,6 à 10,8 s | Problème | Des fiches sombres s'empilent et défilent vers le haut, trop nombreuses ; un fond de glyphes ASCII derrière. |
| 10,8 à 16 s | Solution | Un fil gris avec un point orange trace un chemin entre des étiquettes de prix ; des pixels orange s'assemblent ; une fiche produit blanche arrive et se fait annoter (cadres et étiquettes : catégorie, prix, mot-clé). |
| 16 à 20,8 s | Solution | Un carré se remplit de glyphes et devient un cube orange ; la mosaïque de pixels sombres coupe. |
| 20,8 à 33,6 s | Démonstration | Un globe en fil de fer avec ses étiquettes ; il se déroule en grille ; une page web passe en fil de fer puis en code brut ; un bouton orange s'écrit et se clique ; une carte de connexion se remplit. |
| 33,6 à 54,8 s | Démonstration en trois chapitres | Le mur de pages pivote ; une page sort, se trame en glyphes et devient des données propres ; trois chapitres en labels mono entre crochets (chercher, extraire, agir), chacun ouvert par une grille de pixels. |
| 54,8 à 58,2 s | Preuve | Le grand chiffre orange au milieu des glyphes, son étiquette mono ; puis l'icône au centre et les logos des clients autour, sur des tuiles blanches. |
| 58,2 à 61,2 s | Intégrations | L'icône reliée aux logos des IA par un maillon ; le chevron en escalier part du bord droit. |
| 61,2 à 66 s | Fin | Sur blanc, le logo et le nom se forment en pixels et se tiennent 4 s ; pas d'appel à l'action écrit. |

Chez toi (vidéo de page de 60 à 90 s), dans cet ordre, avec les compositions du kit :

1. **Problème** (5,5 s) : `t01-bruit`, la question du prospect, le mur de bruit, « Trop de bruit. ».
2. Raccord : `t01-raccord-pixels` par-dessus la coupe.
3. **Solution** (6,5 s) : `t01-carte-annotee`, les pixels deviennent la fiche de l'offre, annotée.
4. **Démonstration** (20 à 40 s) : deux ou trois chapitres, chacun ouvert par son label mono « [ 03 · … ] » et une carte d'interface réelle (recettes du studio, au look de ce template : grille claire, cartes blanches ou sombres, décodage, cadres). Une mosaïque de pixels entre deux chapitres, pas plus d'une fois sur deux.
5. **Preuve** (2,8 s) : `t01-chiffre`, seulement avec un vrai chiffre.
6. **Outils, offre et appel** (6,8 s) : `t01-logos-fin`, les logos reliés, le chevron, le nom, le bouton.

## 3. Les fonds et les couleurs

| Rôle dans l'original | Couleur mesurée | Avec la marque du client |
|---|---|---|
| Fond de toute la vidéo | gris très clair `#f9f9f9` | reste `#f8f8f8` : c'est le look, quelle que soit la marque |
| Grille | traits de 2 px `#e7e7e7` tous les 180 px, un point `#e3e3e3` au centre de chaque case | reste ; quelques cases `#f0f0f0` s'allument par à-coups |
| Trame de glyphes du bas | glyphes `#d9d9d9` (. : + = X) | reste, très pâle, au bas de l'écran |
| Cartes, panneaux, tuiles, fin | blanc, ombre douce (8 %) | reste |
| Accent : pixels, point qui voyage, cadres, chiffre, chevron, bouton | orange `#eb4606` | `var(--brand-accent)` ; teintes du chargeur à 42 % et 18 % sur le fond |
| Cartes sombres, mosaïque | encre `#1d1d1d`, gris `#262626` et `#373737` | la couleur sombre de la marque : son fond s'il est sombre (LMDM : `#202022`), sinon son texte, sinon `#1d1d1f` ; la mosaïque mêle cette encre à 100, 94 et 88 % |
| Gris clairs de la mosaïque | `#c9c9c9`, `#adadad` | l'encre à 22 et 36 % sur blanc |
| Texte posé sur l'accent | blanc | `var(--brand-contrast)` |

- **Accent clair** (jaune, vert pâle, luminance au-dessus de 0,28) : un jaune ne se lit pas sur le gris clair. Le kit le détecte seul et passe en classe `t01-accent-clair` : les cadres de repérage et le chiffre passent à l'encre (le chiffre souligné d'un trait de couleur), les teintes du chargeur deviennent des gris, l'accent reste en aplat (pixels, étiquettes, surlignage, chevron, bouton). Jamais d'accent clair transparent. Le chiffre, qui est un texte, passe à l'encre plus tôt : dès que l'accent ne s'y lit plus à 4,5:1 sur le gris clair (luminance au-dessus de 0,17).
- **Sur n'importe quelle marque, claire ou sombre** : le gris clair, la grille, le blanc des cartes et de la fin restent ceux de l'original, fixes ; seuls l'accent et l'encre des cartes sombres viennent de la marque, et l'encre se choisit seule (son fond s'il est sombre, sinon son texte, sinon `#1d1d1f` : jamais une couleur claire). Le texte posé sur l'accent est en `var(--brand-contrast)` ; tout texte garde un contraste d'au moins 4,5:1.
- Aucun dégradé, aucun néon ; les seules ombres sont douces et larges.
- Les bascules de fond de l'original : clair presque partout, deux passages sombres (la mosaïque, l'écran de code) et le blanc pur de la fin. Le kit garde ce dosage : ce template ne fait pas alterner sombre, clair et couleur pleine comme le style par défaut du studio, c'est voulu.

## 4. La typographie

- **Interfaces** (carte de discussion, fiche, boutons) : une grotesque neutre. Le kit prend Inter (livrée dans chaque projet) ; l'original est proche d'Inter ou de Geist.
- **Labels, étiquettes, données** : une mono. La police mono de la marque si elle en a une ; sinon la mono du système (SF Mono, Menlo, Consolas). Police libre la plus proche à poser si la marque n'impose rien : JetBrains Mono ou Geist Mono.
- **Titres** (l'original n'en a pas, le kit les ajoute) : la police de titres de la marque, deux graisses dans une étiquette blanche, l'appui en 400 gris (`#8a8a8a`), le mot fort en 700 surligné à l'accent. Sans police de marque : Inter ou Geist.
- **Chiffre** : police de titres en 700, très serrée (-0,045 em), à l'accent (à l'encre si l'accent est clair).

| Texte | 1920 × 1080 | 1080 × 1920 | Casse, alignement |
|---|---|---|---|
| Label mono « [ 01 · LE PROBLÈME ] » | 20 px, espacement 0,16 em | 24 px | capitales, entre crochets, à gauche, en haut |
| Étiquette-titre (2 à 4 mots) | 66 px | 72 à 76 px | phrase, à gauche, sous le label |
| Texte d'interface | 20 à 22 px | 25 px | phrase |
| Titre et prix de la fiche | 58 et 52 px | 66 et 60 px | phrase, à gauche |
| Étiquette d'un cadre | 13 px mono, gras | 13 px | capitales, sur l'accent |
| Grand chiffre | 250 px | 210 px | centré |
| Étiquette du chiffre | 26 px mono | 26 px | minuscules, centrée dans sa pastille |
| Nom final | 124 px | 112 px | centré, à côté du logo (dessous en vertical) |
| Bouton | 42 px | 42 px | phrase, centré |

## 5. Les mouvements signature

1. **La mosaïque de pixels** (`t01-raccord-pixels`, 1,45 s) : des blocs de 240 px, coupés en 2 × 2 pixels de tons différents (un sur six clair), surgissent par à-coups, sans fondu, des bords gauche et droit vers le centre en 0,6 s ; un pixel sur cinq clignote en gris clair 0,07 s avant de foncer. L'écran couvert grossit de 4 % pendant 0,4 s, puis les blocs tombent rangée par rangée du haut vers le bas en 0,3 s.
2. **Les pixels qui deviennent l'interface** (`t01-carte-annotee`) : un amas en croix de 12 pixels à l'accent (72 px, pas de 104 px) s'allume en vague (0,05 s d'écart), ses teintes tournent toutes les 0,12 s ; puis chaque pixel glisse et s'étire jusqu'à un bloc de la fiche (0,65 s, `expo.inOut`, 0,03 s d'écart) pendant que la carte blanche grandit derrière (0,7 s) ; l'aperçu se dissout en pixels (ordre aléatoire, 0,5 s).
3. **Le décodage** (toutes les scènes) : chaque texte arrive en glyphes (# % @ X = + : * / < >) renouvelés toutes les 0,045 s, qui se fixent de gauche à droite en 0,4 à 0,6 s. Labels, titres, contenu des cartes, nom final.
4. **Les cadres de repérage** (`t01-carte-annotee`) : un cadre de 2 px se pose sur une partie de la fiche (de 112 % à 100 %, 0,3 s, `expo.out`), un éclair de remplissage s'y éteint en 0,45 s, une petite étiquette en capitales monte de 8 px (`back.out`) ; un cadre toutes les 0,32 s, et la caméra fait un pas vers chacun.
5. **Le chiffre dans les glyphes** (`t01-chiffre`) : les hachures s'ouvrent en 0,5 s, le chiffre compte de 0 à sa valeur en 1,25 s (`expo.out`) au milieu d'un nuage de glyphes d'abord dense sur lui, puis seulement sur ses bords, éteint en 1,6 s ; six points s'allument du centre vers les bords (0,1 s d'écart).
6. **Le chevron en escalier** (`t01-logos-fin`) : quatre couches en marches de 54 px (pas de 62 px en 16:9, 50 px en 9:16) partent du bord droit l'une après l'autre (0,16 s d'écart, 1,05 s chacune, `power2.in`) : une grille de cellules, l'accent, un gris, le blanc qui couvre tout.

## 6. Les transitions

- **La mosaïque de pixels sombres** : le raccord signature, deux ou trois fois par vidéo de page, jamais deux fois de suite. Elle se pose sur la piste 2, par-dessus la coupe (voir « Les compositions du kit »).
- **Le raccord d'objet** : le panneau du chiffre se resserre en case blanche, la case reçoit le logo ; les pixels deviennent la fiche ; dans l'original, le globe se déroule en grille et la caméra entre dans une case.
- **La dissolution en pixels** : un aplat (l'aperçu de la fiche, le logo final, la case du centre) se découvre par carrés qui tombent dans le désordre.
- **Le chevron en escalier** : une seule fois, pour passer à la fin.
- **La coupe franche** : rare, sur un temps fort de la musique.
- Jamais de fondu enchaîné entre deux écrans chargés.

## 7. Le produit à l'écran

- L'original ne montre jamais de capture brute : son produit (un service pour développeurs) devient des **cartes d'interface simplifiées et propres** : une discussion avec l'agent, une fiche produit qu'on annote, des fiches de données, un mur de pages, une connexion. Chaque carte fait une seule chose, lisible en une seconde.
- Les **logos des outils** reliés (OpenAI, Anthropic, Gemini) et ceux des clients autour de l'icône disent l'écosystème.
- **Chez toi** : l'offre devient une fiche blanche (nom, genre, prix exact, promesse en 3 lignes, 3 pastilles de contenu) avec un **vrai visuel** dans l'aperçu (miniature de leçon, écran du logiciel, photo de séance) ; les cadres repèrent ce qui fait vendre ; la discussion sombre porte la vraie question du prospect ; les tuiles portent les vrais logos des outils de l'offre (`studio_motion.py logos`). Une interface qu'il n'a pas ne s'invente pas.

## 8. Le son

- **Musique de l'original** : électronique sèche et percussive, environ 92 battements par minute (mesuré), faite de clics, de bips et de grésillements numériques plus que de mélodie, avec de courts silences nets (vers 33 s, et juste avant le logo final). Sonie mesurée -12,6 LUFS : trop fort pour nous, on vise -16 LUFS (`mastering`).
- **Chez toi** : l'ambiance « Tech minimale » des musiques de lancement (`musiques choisir --ambiance "Tech minimale"`), l'entrée de batterie calée sur l'arrivée de la fiche (le pivot).
- **Bruitages**, tous légers et numériques, jamais d'impact grave : une rafale de clics secs pour la mosaïque, un bip court par cadre de repérage (pas un par pixel), quelques bips pour le chargeur, la frappe au clavier pour la question et le bouton, un « ding » léger quand le maillon s'allume, un souffle doux pour le chevron, un clic de souris et un petit « pop » pour le bouton final.

## 9. L'ouverture et la fin

- **Ouverture de l'original** : 3 s sans un mot, une structure de pixels qui se monte en perspective, puis la carte de discussion. **Chez toi** : `t01-bruit` ouvre directement sur la carte et la question qui se tape (le sujet se comprend à la première seconde) ; en vidéo de page, si cette scène ouvre la vidéo, fais arriver l'étiquette dès 0,3 s.
- **Fin de l'original** : le chevron en escalier, le blanc, le logo et le nom qui se forment en pixels, tenus 4 s, sans appel écrit. **Chez toi** : la même fin, plus le bouton qui s'écrit lettre à lettre et le clic du curseur (repris du bouton orange de l'original, à 30 s), tenus 1 s ; allonge la tenue à 2,5 s si c'est la dernière scène.

## Ce qui ne se fera pas à l'identique

- La structure isométrique de l'ouverture, le globe en fil de fer, le cube, le mur de pages qui pivote, la page qui passe en fil de fer puis en code : trop liés à un produit qui lit le web, pas construits dans le kit. Leur grammaire (tramage, raccord d'objet, caméra qui entre dans une case) reste disponible.
- Le logo final qui se forme dans une trame de glyphes, de gauche à droite : remplacé par une grille de 6 × 6 pixels (blancs et à l'accent) qui tombent, le nom se décodant à côté.
- Les logos de clients autour de l'icône : remplacés par les logos des outils liés à l'offre (un logo de client se montre seulement avec son accord).
- Presque aucun texte dans l'original : le kit ajoute un label mono et une étiquette de 2 à 4 mots par scène.
- Aucun appel à l'action dans l'original : le kit finit sur un bouton écrit et cliqué.
- Un accent clair (le jaune de LMDM) ne peut pas faire les traits fins de l'orange : le kit passe les cadres et le chiffre à l'encre.
- La police mono de l'original : remplacée par la mono de la marque ou du système.

## Sur une autre offre

C'est un look : il se pose sur toute offre. Ce qui suivait le produit de l'original s'adapte :

- **Formation** : la discussion porte la question des élèves (« Par où je commence ? ») ; la fiche est la formation (genre « Formation · En ligne · Accès à vie », pastilles Vidéos, Modèles, Bonus), l'aperçu une vraie miniature de leçon ; le chiffre compte les élèves ; les tuiles sont les outils enseignés.
- **Coaching** : la discussion porte ce que les clients disent au premier appel ; la fiche est l'accompagnement (format, durée, séances), l'aperçu une photo de séance ou l'agenda réel ; le chiffre compte les clients accompagnés ; les tuiles, seulement les outils vraiment utilisés (visio, suivi).
- **Logiciel** : le bruit, ce sont les dix outils ou onglets qu'il remplace ; la fiche est son écran principal (capture réelle dans l'aperçu), les cadres repèrent ses fonctions ; le chiffre compte les utilisateurs ; les tuiles sont ses intégrations réelles.
- **Toujours** : la grille claire, les pixels, le décodage, la mosaïque, les cadres, le chevron, l'accent seul en couleur.

## En vertical et en carré

- **9:16 (1080 × 1920)** : mets `data-width="1080" data-height="1920"` sur la racine de chaque composition et sur son hôte ; la mise en page se règle seule (classe `t01-vertical`) : mur de bruit en 3 colonnes, fiche en colonne (aperçu 828 × 480 en haut, texte dessous), labels et étiquettes en haut dans la zone sûre (x 100, y 300 et plus), tuiles réparties en hauteur, logo au-dessus du nom à la fin, mosaïque et chevron recalculés. Testé sur toutes les compositions (captures dans les preuves).
- **4:5 et carré** : pas de mise en page propre. En 4:5 (1080 × 1350), la mise en page verticale s'applique seule mais elle est dessinée pour 1920 de haut ; en carré, force-la (`vertical = true` dans le script). Puis réduis la caméra de chaque scène (`scale` 0,7 en 4:5, 0,56 en carré) et remonte labels et étiquettes vers y = 120. À vérifier image par image : rien n'a été testé dans ces deux formats.

## Les compositions du kit

Dossier `compositions/`, 16:9 par défaut, chacune avec son en-tête (ce qu'elle montre, sa durée, ce qu'on remplace). Elles se servent du kit du projet (`K`) et des variables de la marque (`--brand-*`) ; les identifiants commencent par `t01-`.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `t01-bruit.html` | 5,5 s | Problème : la carte de discussion sombre, la question tapée, la réponse, le mur de bruit flou, l'étiquette « Trop de bruit. » | la question, la réponse (3 lignes), 10 à 14 phrases de bruit du domaine, le label et l'étiquette |
| `t01-raccord-pixels.html` | 1,45 s | Raccord : la mosaïque de pixels sombres, couverture puis départ par rangées | l'id (un par raccord) et la graine |
| `t01-carte-annotee.html` | 6,5 s | Solution : le chargeur en pixels, les pixels qui deviennent la fiche, le décodage, l'aperçu dissous, les cinq cadres de repérage, le recadrage final | la fiche (nom, genre, prix exact, promesse, pastilles), le visuel de l'aperçu, les étiquettes des cadres, le label |
| `t01-chiffre.html` | 2,8 s | Preuve : le panneau à hachures, le chiffre qui compte dans les glyphes, son étiquette, les points ; sortie en case blanche | le vrai chiffre (obligatoire, sinon pas de scène), ce qu'il compte, le label |
| `t01-logos-fin.html` | 6,8 s | Outils et fin : le logo dans la case, les tuiles d'outils, le maillon qui relie, le chevron en escalier, le logo et le nom en pixels, le bouton tapé et cliqué | les logos des outils, l'outil relié, le logo et le nom, l'étiquette, le bouton |

Le montage dans `index.html` (16:9) : les scènes bout à bout sur la piste 1, le raccord sur la piste 2, au-dessus, démarrant 0,8 s avant la coupe :

```html
<div id="s1-hote" data-composition-id="t01-bruit" data-composition-src="compositions/t01-bruit.html" data-start="0" data-duration="5.5" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="r1-hote" data-composition-id="t01-raccord-pixels" data-composition-src="compositions/t01-raccord-pixels.html" data-start="4.7" data-duration="1.45" data-track-index="2" data-width="1920" data-height="1080" style="z-index:3;"></div>
<div id="s2-hote" data-composition-id="t01-carte-annotee" data-composition-src="compositions/t01-carte-annotee.html" data-start="5.5" data-duration="6.5" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s3-hote" data-composition-id="t01-chiffre" data-composition-src="compositions/t01-chiffre.html" data-start="12" data-duration="2.8" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s4-hote" data-composition-id="t01-logos-fin" data-composition-src="compositions/t01-logos-fin.html" data-start="14.8" data-duration="6.8" data-track-index="1" data-width="1920" data-height="1080"></div>
```

Avant de monter `t01-logos-fin` : `python3 ../../../tools/studio_motion.py logos . claude chatgpt …` depuis le projet, avec les outils de l'offre. Un second raccord dans la même vidéo prend un autre id (`t01-raccord-2`) et une autre graine.
