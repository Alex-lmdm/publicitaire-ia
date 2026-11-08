# Notes de maintenance · style 0 « Sur mesure » (le style maison)

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/00-sur-mesure/style.md`) dit la règle au présent.

## D'où il vient

- **La story d'ouverture de Publicitaire IA** (06 et 07/11/2026) : la v1 en style 2 et la v2 en
  style 7 ont été refusées par Alex (« trop de texte, on a l'impression de voir des sous-titres »,
  paysages bruns tirés du jaune). Pas seulement à cause du style, mais la version validée (v3 puis
  v4) a été faite **hors catalogue**, sur le langage relevé sur les vidéos de Higgsfield Katana
  (`notes/methode.md`, ligne du 07/11/2026). Ce langage est devenu `references/scenes.md` (« Le
  langage du motion design », recettes), les fonctions `K.claque`, `K.barre`, `K.tranche`,
  `K.lien`, `K.trace`, `K.longer` du kit et les 10 scènes prêtes de `templates/scenes/`.
- **L'audit du 08/11/2026** : à l'étape du style, « choisis » prenait toujours un des 8 styles, et
  « aucun de ces styles » ou « décris-le » n'avaient aucune consigne (l'IA improvisait). Le chemin
  qui avait donné la meilleure vidéo n'était donc pas proposé au client.
- **Décision d'Alex du 08/11/2026 (option B)** : un choix 0, le style maison, conseillé par défaut
  pour la première vidéo, avec son aperçu sur la page des styles ; les 8 styles restent pour qui veut
  une allure précise ; « décris-le » part du style 0.

## Choix de fabrication

- **Le nom « Sur mesure »** : il dit au client qu'il n'entre pas dans le moule d'une vidéo qui
  existe. « Signature » a été écarté : le skill emploie déjà « gestes signature » et « moment
  signature », l'IA aurait lu « les gestes signature du style Signature ».
- **Pas de dossier `compositions/`** : ses gestes sont les scènes prêtes, déjà contrôlées en 9:16 et
  16:9 ; les dupliquer aurait fait deux copies à tenir. `tests/test_styles.py` vérifie que chaque
  scène citée par la fiche existe dans `templates/scenes/` ou dans le kit.
- **Pas d'ambiance de musique propre** : la musique suit le but et le support (`styles.AMBIANCES`
  n'a pas d'entrée 0).
- **Le numéro 0** : il se lit « sans style du catalogue », et reste le premier sur la page. Dans le
  code, 0 est faux en Python : `styles.garde` et `musiques choisir` comparent à `None`.
- **L'aperçu** (`assets/styles/00-sur-mesure.mp4|.jpg`, 5 s, muet, 1280 × 720) : trois scènes prêtes
  rendues à la marque LMDM avec leur contenu d'exemple (le nom sur l'objet, le schéma et son fil
  conducteur, la mosaïque qui devient le bouton).
