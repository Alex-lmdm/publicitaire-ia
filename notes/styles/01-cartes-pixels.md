# Notes de maintenance · Style n°1 · Cartes pixels

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/01-cartes-pixels/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les mesures, les essais, ce qui a changé) est rangé ici.

## Ce qui sortait de la fiche

### Les mesures de l'original et de l'essai

- **Original** (`studio_motion.py reference`) : 1920 × 1080, 24 images/s ; 1,82 événement par
  seconde, écart médian 0,30 s, 10 coupes franches détectées en 66 s (vers 6,6, 10,8, 20,8, 26,1,
  31,2, 32,0, 36,7 et 40,0 s), 4,0 s d'image tenue (le logo final). Par tranche de 6 s : de 1,0 à
  2,7 événements par seconde. Tempo de la musique : environ 92 battements par minute ; sonie
  mesurée -12,6 LUFS (trop fort pour nous : on vise -16 LUFS au mastering), courts silences nets
  vers 33 s et juste avant le logo final.
- **Essai du kit** (marque LMDM, 21,6 s, 06/11/2026, avec une vraie capture dans l'aperçu) :
  1,44 événement par seconde en 16:9 (écart médian 0,50 s), 1,39 en 9:16 (0,50 s), aucune image
  figée, `rythme` et `palette` « ok » dans les deux formats.

### La citation d'ouverture

> On reprend la grammaire de la vidéo (grille, cartes, pixels, glyphes, cadres de repérage,
> chevron), jamais son contenu : ni ses textes, ni son logo, ni ses images (veste, fauteuils, pages
> web), ni son produit, ni sa musique, ni ses couleurs. L'orange de Firecrawl devient la couleur de
> la marque du client, posée pleine ; ses images ne se redessinent pas : l'aperçu de la fiche montre
> la vraie capture du client, ou rien.

L'index (`styles/README.md`) le dit désormais pour tous les styles.

### L'original, scène par scène

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

L'ouverture de l'original : 3 s sans un mot, une structure de pixels qui se monte en perspective,
puis la carte de discussion. Sa fin : le chevron, le blanc, le logo et le nom en pixels, tenus 4 s,
sans appel écrit (le bouton du kit reprend le bouton orange de l'original, vers 30 s). Son produit
(un service pour développeurs) : cartes d'interface simplifiées, logos des outils reliés (OpenAI,
Anthropic, Gemini), logos des clients autour de l'icône.

### Les couleurs mesurées de l'original

| Rôle | Couleur mesurée |
|---|---|
| Fond de toute la vidéo | gris très clair `#f9f9f9` (avec la marque LMDM : `#f8f8f8`) |
| Grille | traits de 2 px `#e7e7e7` tous les 180 px, un point `#e3e3e3` au centre de chaque case |
| Trame de glyphes du bas | glyphes `#d9d9d9` (. : + = X) |
| Cartes, panneaux, tuiles, fin | blanc, ombre douce (8 %) |
| Accent : pixels, point qui voyage, cadres, chiffre, chevron, bouton | orange `#eb4606` ; le chargeur de l'ancien kit alternait l'accent et deux gris en dur (`#cfcfcf`, `#e3e3e3`) |
| Cartes sombres, mosaïque | encre `#1d1d1d`, gris `#262626` et `#373737` |
| Gris clairs de la mosaïque | `#c9c9c9`, `#adadad` |
| Texte posé sur l'accent | blanc |

### Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas** : la veste, les fauteuils, les pages web et le mur
  de pages ne se redessinent jamais. L'aperçu de la fiche montre sa vraie capture (fournie pour la
  vidéo), sinon il disparaît ; le faux lecteur vidéo, sa barre de lecture et l'étoile décorative
  des premiers kits sont retirés.
- La structure isométrique de l'ouverture, le globe en fil de fer, le cube, le mur de pages qui
  pivote, la page qui passe en fil de fer puis en code : trop liés à un produit qui lit le web, pas
  construits dans le kit. Leur grammaire (tramage, raccord d'objet, caméra qui entre dans une case)
  reste disponible.
- Le logo final qui se forme dans une trame de glyphes, de gauche à droite : remplacé par une
  grille de 6 × 6 pixels (clairs et à l'accent) qui tombent, le nom se décodant à côté.
- Les logos de clients autour de l'icône : remplacés par les logos des outils liés à l'offre (un
  logo de client se montre seulement avec son accord).
- Presque aucun texte dans l'original : le kit ajoute un label mono et une étiquette de 2 à 4 mots
  par scène. Aucun appel à l'action dans l'original : le kit finit sur un bouton écrit et cliqué.
- Un accent clair (le jaune de LMDM) ne peut pas faire les traits fins de l'orange : le kit passe
  les cadres et le chiffre à l'encre. Les teintes pâles de l'orange (le chargeur, l'éclair des
  cadres) deviennent des gris, pour toutes les marques. La fiche garde la leçon, section 3.
- La police mono de l'original : remplacée par la mono de la marque ou du système.

## Le ménage du 07/11/2026

Taille de la fiche : 25 744 octets avant, 17 968 après (`wc -c`, -30 %).

**La fiche**
- Sortis vers cette note : les mesures, l'essai du kit, la citation d'ouverture, l'original scène
  par scène, la colonne « Couleur mesurée », « Ce qui ne se fera pas à l'identique », la sonie de
  l'original. La leçon de l'accent clair reste en section 3, au présent.
- Retiré ce que l'index dit déjà : l'ouverture de la section 2, « Sur n'importe quelle marque »,
  « aucun dégradé, aucun néon ».
- La caméra : « toutes les 0,3 s, un geste… la caméra qui recadre », « la caméra ne s'arrête
  jamais… recadrage net à chaque nouvelle intention » et « un cadre toutes les 0,32 s, et la caméra
  fait un pas vers chacun » contredisaient la loi (jamais de pas de caméra sous un texte). Désormais :
  le contenu vit toutes les 0,3 s, la caméra dérive lentement pendant la lecture et ne fait qu'un
  recadrage net quand l'intention change.
- Les gris en dur (`#cfcfcf`, `#e3e3e3`, `#8a8a8a`) deviennent des jetons ; l'appui gris des titres
  passe à `--brand-gris-2` (`#8a8a8a` ne passait pas 4,5:1 sur le clair).
- La table de typographie : label 20 → 28 px, étiquette d'un cadre 13 → 28 px, texte d'interface
  20-22 → 28-30 px, étiquette du chiffre 26 → 32 px ; le grand chiffre et le nom final deviennent
  des mots héros (environ 60 % de la largeur, 80 % en 9:16) au lieu de 250 et 124 px fixes.
- Les durées : `t01-chiffre` 2,8 → 3,4 s, `t01-logos-fin` 6,8 → 9 s (le montage d'exemple suit).
- « Ce qu'on remplace » renvoie à l'objet `EXEMPLE` de chaque scène.

**Les scènes** (toutes : un objet `EXEMPLE` unique en tête du script, plus aucune couleur en dur
hors du blanc et du noir en transparence pour la grille et les ombres, cartes en `--brand-clair`)
- `t01-bruit` : carte de discussion agrandie (900 × 540, 960 × 600 en 9:16), question, réponse et
  champ à 30 px (34 px en 9:16), label à 28 px ; la réponse en 3 lignes courtes (8 mots) ; la bulle,
  la réponse et le champ en `--brand-gris-1` et `2` au lieu de blancs en transparence ; « Réponse »,
  l'invite, la frappe dans le champ et le mur en texture ; la poussée de caméra de 15 % sous la
  lecture devient une dérive de 5 % ; l'étiquette arrive à 2,1 s (lue 2 s avant le raccord).
- `t01-carte-annotee` : les pas de caméra de 0,3 s toutes les 0,32 s et le recadrage final sous la
  lecture sont retirés : un seul recadrage pendant que les pixels deviennent la carte, puis une
  dérive de 4,5 % ; fiche agrandie (titre 64, prix 56, promesse 30, genre, pastilles et étiquettes
  des cadres 28 px) ; promesse en 2 lignes ; amas de pixels agrandi (84 px, pas de 124 px) ; un prix
  vide retire sa ligne et son cadre ; prix d'exemple « 300 € », marqué comme exemple.
- `t01-chiffre` : chiffre en mot héros (60 % de la largeur), étiquette 32 px, label 28 px ; tenue
  de 1,6 s une fois compté (D = 3,4 s).
- `t01-logos-fin` : la caméra ne fait plus que le recul d'entrée puis une dérive (plus de trois
  recadrages sous le titre) ; le titre arrive à 1,25 s et se lit 2,5 s avant le chevron ; nom final
  en mot héros ; sans logo, son nom à la place (plus d'initiale) ; sans le logo de l'outil relié, pas
  de rond vide ; ce qui est sous le chevron s'éteint une fois couvert ; écran final tenu 3 s
  (D = 9 s) ; logo par défaut `brand/logo.png` (le banc n'a pas de `logo.svg`).
- `t01-raccord-pixels` : `EXEMPLE = {}` ; le ton « nuit sous un blanc à 5 % » devient
  `--brand-gris-2`.
