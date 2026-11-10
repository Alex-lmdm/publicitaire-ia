# Notes de maintenance · le catalogue de styles (index)

Fichiers de maintenance : l'IA ne les lit pas pendant une vidéo. Les fiches
(`.claude/skills/studio/styles/NN-nom/style.md`) et l'index (`README.md`) disent la règle au présent ;
ce qui l'a fait naître (l'original scène par scène, les essais mesurés, les refus datés, les anciens
noms) est rangé ici, un fichier par style.

## Ce qui sortait de l'index (README.md) lors du ménage du 07/11/2026

- **Les anciens noms** : les styles 5 et 8 s'appelaient « Interrupteurs crème » et « Fenêtre
  peinte » jusqu'à la 0.9.0 (des noms de couleur et d'image, devenus faux quand les styles ont pris
  les couleurs de la marque). L'index garde la règle : un client qui emploie l'ancien nom veut le
  même style.
- **« template »** : ses premières vidéos appelaient les styles ainsi.
- **Les aperçus** (`assets/styles/<dossier>.mp4|.jpg`) sont tournés à la marque LMDM ; l'index dit
  « sur une marque d'essai ».
- **L'image redessinée** : story refusée du 06/11/2026, des couchers de soleil et une planète
  redessinés, bruns et orangés (« c'est vraiment moche »). Essais du 06/11/2026 : des disques et des
  carrés sans sujet. D'où la règle : une image de l'original devient la vraie matière du client,
  jamais une forme seule.
- **La teinte tirée de l'accent** : pub d'essai du 03/11/2026 et story refusée du 06/11/2026 (un
  accent jaune en transparence sur du sombre fait du brun, de l'olive ou de l'orangé).
- **L'exemple de structure** : vidéo du haut de la page de Publicitaire IA, style 7, 03/11/2026 :
  la structure venait du texte de la voix off ; trois gestes du kit repris (la phrase et ses objets,
  le désordre réduit en points, l'orbite et le point d'encre) ; deux scènes construites pour son cas
  (le dossier déposé sur Claude, la conversation dans Claude). L'index en garde une version
  générique.
- **Les liens** : l'index renvoyait à `references/style.md` (« Aucune image inventée », « La
  palette ») et `references/rythme.md` (« La caméra ») ; ils renvoient désormais à
  `references/image.md` et `references/mouvement.md`.

## Le ménage du 07/11/2026

Un audit a montré que les fiches et leurs exemples contredisaient les règles du produit, et que
l'IA copie surtout le code des exemples. Ce qui est commun aux 8 fiches (l'ouverture de la
section 2, la citation « On reprend la grammaire… », « Sur n'importe quelle marque », la ligne de
contraste, les rappels de palette et de lecture) se dit une fois dans l'index, « Appliquer un
style », point 6 « La loi de toutes les scènes ». Chaque scène regroupe ses textes d'exemple dans
un objet `EXEMPLE` marqué « À REMPLACER » ; `tests/test_styles.py` (classes `Menage` et
`Exemples`) le vérifie.

## Les aperçus du 10/11/2026

Les aperçus des styles 1 à 8 (`assets/styles/<dossier>.mp4|.jpg`) ont été refaits depuis les scènes
actuelles des styles, et non plus découpés dans les vidéos d'essai du 06/11 (d'anciennes copies des
scènes, qui affichaient encore 97 € et 2 974 €). La méthode, pour les refaire :

- un projet par style dans `videos/Aperçus des styles · 2026-11-10/` (hors git), créé par `nouvelle`,
  marque LMDM, la fiche de la story d'ouverture (`OFFRE.json` : 67 €, 2 976 €, ses 35 musiques…) et
  les vraies captures de la page ;
- deux à quatre scènes du style copiées telles quelles, seul l'objet `EXEMPLE` rempli (et, au style 4,
  les places des mots de `PLANS`, calées sur les phrases) ; rendu entier en HyperFrames 0.9.26, flou
  de bougé compris ;
- 5 s découpées en un ou deux passages (coupe franche), 1280 × 720, 30 i/s, h264 muet, CRF 20 à 26
  pour rester sous 900 Ko ; l'affiche prise sur l'image qui montre le mieux le style.

Gestes montrés : 1 le mur de bruit, la mosaïque, les pixels qui deviennent la fiche annotée ;
2 le titre qui déborde, la carte et la mosaïque ; 3 la barre filée et sa pastille, la plongée,
le carrousel chiffré ; 4 les mots éparpillés et leurs cases, la transition en pixels, le pivot en
disque ; 5 la cascade d'interrupteurs, le trait qui entoure ; 6 le cercle au pinceau, la
numérisation, l'initiale et la rafale de planches ; 7 le mot géant sur l'aplat, la demande envoyée
et sa fenêtre ; 8 la phrase tapée, la fenêtre filmée sur sa couleur.

Laissé de côté, et pourquoi : le cube logo du style 8 (le flou de bougé en mode `capture` l'aplatit :
face grise sans logo ; signalé à Alex), ses barres comparatives (aucune comparaison chiffrée dans la
fiche), le verre piloté du style 3 (sans paiement en plusieurs fois ni bonus, son deuxième cadrage
vise un élément caché et montre la moitié haute vide ; signalé à Alex).
Autre défaut vu en montant le style 1, signalé à Alex : le garde-fou des exemples (`K.emplacements`)
prend le label mono du style (« [ 02 · LA SOLUTION ] ») pour un emplacement oublié ; `check` sort
donc en erreur sur toute vidéo qui garde ce label dans `t01-carte-annotee` ou `t01-chiffre`.
