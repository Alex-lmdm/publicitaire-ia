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
