# Notes de maintenance · Style n°4 · Mots éparpillés

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/04-mots-eparpilles/style.md`) dit la règle au présent ; ce qui l'a
fait naître (l'original scène par scène, les essais mesurés, les refus datés, l'ancien exemple) est
rangé ici.

## Ce qui est sorti de la fiche

### Les mesures

- **Mesures de l'original** (`studio_motion.py reference`) : 1,19 événement par seconde, écart
  médian 0,60 s, 23 coupes franches (presque toutes dans les transitions en pixels), image figée la
  plus longue 5,1 s (la fin noire).
- **Mesures de l'essai du kit** (les 4 scènes bout à bout, 59,5 s, marque LMDM, la vraie matière de
  la story d'ouverture de Publicitaire IA, 06/11/2026) : `rythme` 1,06 événement par seconde en
  16:9 (écart médian 0,70 s), 1,09 en 9:16 (0,80 s), aucune image figée ; `palette` « ok » dans les
  deux formats ; marque claire (Dupliq.me, accent orange) vérifiée par captures. Ces mesures valent
  pour l'ancien exemple (59,5 s) ; le nouvel exemple (54,1 s) n'a pas été rendu ni mesuré par
  `rythme` et `palette`.

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (ses images ne se refont pas ; ses durées non
plus) :

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Papier 1 | accroche, le problème | 1,9 s | Un mot à la fois sur la grille, un objet du quotidien en 3D qui surgit avec chaque mot ; dans le kit, une phrase complète tenue le temps de la lire, ses cases portant sa vraie matière (`mots-objets.html`) |
| Écran 1 | le problème vécu | 1,3 s | Transition en pixels ; l'écran tramé de couleurs, un téléphone de bureau qui vibre, la pastille de verre de ce qui arrive (« NOUVELLE DEMANDE ») ; dans le kit, sa nuit tramée, la pastille claire et sa vraie capture qui vibre |
| Papier 2 | le problème, encore | 1,3 s | Une deuxième phrase courte, d'autres objets (dans le kit, d'autres matières) |
| Écran 2 | le problème qui coûte | 1,1 s | Le téléphone sous un autre angle, une autre pastille (« APPEL MANQUÉ ») |
| Papier 3 | la chute du problème | 1,4 s | La phrase qui fait mal, entourée de tous les objets (dans le kit, de toutes les matières vues) ; puis les carrés d'un dégradé chaud envahissent l'écran (dans le kit, sa couleur pleine) |
| Le pivot | bascule | 4 s | La phrase pivot sur le dégradé (« Ça, c'était avant. »), le dégradé devient un orbe lumineux dans ses anneaux, l'orbe change de couleur et s'ouvre ; dans le kit, sa couleur qui se resserre en disque autour de la phrase, puis porte son logo et son nom (`orbe-pivot.html`) |
| La conversation | solution, démonstration | 6 s | Les bulles de verre sur le dégradé de l'après ; l'offre répond, le résultat arrive et se coche ; dans le kit, des bulles pleines sur sa couleur, un vrai échange (`messages-verre.html`) |
| La fin | offre et appel | 6,5 s | Le cadre au trait, la phrase d'appel ; le cadre devient les trois cartes de l'offre, qui deviennent un trait, puis le nom et le bouton (`fin-cadre.html`) |

### Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas.** Ses objets photoréalistes (des rendus 3D :
  bouteille, casque, cône, clavier, tasse), ses téléphones de bureau, les couleurs tramées de ses
  écrans et son orbe fluide ne se redessinent jamais, ni en 3D, ni en dessin simplifié, ni en formes
  simples à sa place (essai du 06/11/2026 : des carrés et des ronds noirs et jaunes sans sujet autour
  de « Et ton offre attend. »). À leur place, sa vraie matière (ses captures, sa vraie vidéo, ses
  vrais chiffres, les logos de ses outils), sinon ses mots.
- **Le tempo haché** (un papier toutes les 1,2 à 1,9 s) → des phrases complètes, tenues le temps de
  les lire ; la vie vient des cases qui arrivent pendant la tenue.
- **La vraie trame** (des points de tailles variables selon la lumière) → des tirets blancs très
  pâles sur sa nuit : la texture de l'écran, sans image dessous.
- **L'orbe fluide** (une matière lumineuse qui coule) → un disque plein de sa couleur dans ses
  anneaux, sans lueur ni cœur blanc, qui porte sa phrase puis son logo.
- **Les dégradés vifs** (l'alerte, l'après, les cartes) et le trait lumineux → sa couleur pleine, en
  aplat, et un trait plein et fin.
- **Les bulles de verre** → des bulles pleines sans ombre : sur un aplat, le verre ne se voit pas,
  et un verre clair sur sa couleur la pâlirait.
- **La voix off et la conversation jouée** → texte et musique par défaut.
- **Les petits textes et les 5 s de noir** de l'original → agrandis et raccourcis pour la lecture.
- **Les trois familles de couleurs** (bleu, rouge, vert) → ses couleurs seules : sa couleur pleine,
  sa nuit, son clair et des gris.

Leçons gardées dans la fiche, au présent : la phrase sous « D'après » (les images de l'original), la
section 1 (des phrases complètes, tenues), la table de la section 3 (tirets, disque, aplat, bulles
pleines et leur raison), la section 8 (texte et musique par défaut), la section 9.

### Les essais et refus datés

- **Story refusée du 06/11/2026** (« beaucoup trop rapide ») : elle suivait le tempo de l'original
  (un papier toutes les 1,2 à 1,9 s, des bulles toutes les 1,2 s). D'où « Des phrases complètes,
  tenues » (section 1).
- **Le piège de la palette, essai du 06/11/2026** : sur le jaune, une bulle de sa nuit qui entre en
  fondu, un logo flou, une ombre noire passaient par l'olive et le brun (`palette` relevait 13 % d'une
  image). D'où « Sur sa couleur, rien ne se fond, ne se floute ni ne porte d'ombre sombre » (section 3).
- **Essai Dupliq.me du 06/11/2026** : le logo de Claude se confondait avec un accent orange. D'où la
  ligne sur le logo d'outil qui se confond avec sa couleur (section 3).
- **Pub d'essai du 03/11/2026** : la carte du résultat est passée à 38 et 28 px pour être lue sur un
  téléphone ; la fin de pub en 9:16 a pris « Découvre-le » et une flèche à la place du bouton.
- **Les tailles de l'original** : des bulles de 22 px, une phrase d'appel de 24 px ; le kit agrandit
  tout pour la lecture sur un téléphone.
- **Les 9:16 bout à bout** (essai du 06/11/2026 sur LMDM) : 59,5 s, `rythme` « ok », 1,09 événement
  par seconde, écart médian 0,80 s, aucune image figée, `palette` « ok », raccords image pour image.

### L'ancien exemple des scènes

L'exemple était l'essai du kit : la story d'ouverture de Publicitaire IA (ses phrases, les
illustrations de sa page, sa vraie pub, l'échange réel de la vidéo de sa page, ses chiffres, ses
logos d'outils), avec ses captures `assets/images/options-filmer.png`, `options-devis.png`,
`options-samedi.png`, `pub-image.jpg`, `page-defile.jpg`, `scene-1.jpg` à `scene-5.jpg`.

- `mots-objets` : « Pour avoir une vidéo, tu as trois options. », les écrans « TE FILMER », « UN
  DEVIS DÈS 1 500 € », « UN WEEK-END DE MONTAGE », « Pour une vidéo qui fait amateur. », un chiffre
  « dès 1 500 € », les logos Instagram, Facebook, YouTube, CapCut, TikTok.
- `orbe-pivot` : « Il y a une quatrième option. », son logo et « Publicitaire IA ».
- `messages-verre` : « Fais-moi une vidéo de vente. » avec le lien de sa page, « Trois idées pour ta
  vidéo : » (« L'IA qui parle », « Deux métiers en un », « Trois étapes »), « La 2. », « Je fabrique
  tout en motion design. », la carte « 5 scènes prêtes », les logos Claude et ChatGPT.
- `fin-cadre` : « Ta première vidéo qui vend, prête dans l'heure. », les cartes « 16 méthodes », « La
  formation pas à pas », « 4 bonus offerts », « Publicitaire IA » et « Je veux mon Publicitaire IA ».

L'enchaînement « Les options écartées » de la fiche en venait (« TE FILMER », « UN DEVIS DÈS
1 500 € », « UN WEEK-END DE MONTAGE ») ; la fiche le garde en générique.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit, et que l'IA copie
surtout le code des scènes. Ce qui a changé :

**La fiche** (36 538 → 25 756 octets) :
- Sorti vers cette note : les mesures, « L'original, pour mémoire », « Ce qui ne se fera pas à
  l'identique », les dates, l'ancien exemple. Retiré parce que l'index le dit (`README.md`,
  « Appliquer un style ») : la citation « On reprend la grammaire… », l'ouverture de la section 2,
  « Sur n'importe quelle marque, claire ou sombre » (sauf ce qui est propre au style : la nuit d'une
  marque claire, le logo qui se confond avec la couleur, rien de fondu ni d'ombré sur la couleur).
- Lien `references/style.md` → `../../references/image.md` (« La vraie matière ») ; lien vers
  `structures.md` (publicité) ; `voix.md` gardé.
- Section 4 : « 12 mots au plus » → 8 au plus (dans les scènes) ; tailles à lire relevées à 28 px au
  moins (étiquette et lien des bulles 28 px, cartes de choix 30 px, ligne des cartes de l'offre 28 px,
  titre du résultat 34 px) ; phrase pivot 88 px (76 px en 9:16), pour mieux remplir le disque.
- Section 5 : le pivot ne fait plus battre sa couleur (un voile blanc de 14 %, une teinte tirée de
  l'accent) : chaque mot tombe d'une pulsation d'échelle. Le disque se resserre pendant que le logo y
  entre (il n'est plus vide 0,35 s) et passe à 240 px (270 en 9:16) pour que le sujet tienne 40 % du
  cadre. Les mots de bulle s'allument d'un gris de la marque au texte plein (au lieu de 22 %
  d'opacité). Les cartes de l'offre ne battent plus sous le texte qu'on lit : leurs icônes battent.
  Le fond du cadre de fin monte vers `--brand-gris-1` (au lieu d'un voile blanc de 20 %). Les
  transitions en pixels sont dites transitions, jamais une poussière posée sur un plan.
- Section 3 : cases en `--brand-gris-4` (au lieu du noir à 5,5 %), pastilles empilées en
  `--brand-gris-2` et `--brand-gris-1` (au lieu de blancs en transparence), cadre au trait
  `--brand-gris-2`.
- Exemples génériques (un logiciel fictif de prise de rendez-vous ; la section « Sur une autre
  offre » couvre la formation et le coaching) ; durées et « Ce qu'on remplace » mis à jour (l'objet
  `EXEMPLE`).

**Les scènes** (chacune a son objet `EXEMPLE` marqué « À REMPLACER », l'exemple fictif d'un logiciel
de prise de rendez-vous, « Ton offre » pour nom) :
- `mots-objets` et `-vertical` (20,4 → 18,4 s) : textes, matières des cases et pastilles dans
  `EXEMPLE`, la mise en page dans `PLANS` (par numéro) ; « UN DEVIS DÈS 1 500 € » et le chiffre « dès
  1 500 € » remplacés (« 40 messages ») ; cases en `--brand-gris-4`, pastilles empilées en gris
  pleins, plus d'ombre sur un logo posé sur la couleur ; `OUVERTURE` : la première image porte le
  premier mot et sa case (`first_frame_empty` corrigé) ; un mot sans place suit le précédent.
- `orbe-pivot` et `-vertical` (7,5 → 7,2 s) : plus de voile blanc à chaque mot (pulsation d'échelle
  du mot) ; disque de logo plus grand, jamais vide ; phrase plus grande.
- `messages-verre` et `-vertical` (16,4 → 14,6 s) : l'échange réel de l'auteur remplacé ; bulles de
  8 mots au plus ; mots à venir en gris lisible ; étiquette, lien, choix et numéros à 28 px au moins.
- `fin-cadre` et `-vertical` (15,2 → 13,9 s) : fond du cadre en `--brand-gris-1`, trait gris en
  jeton ; ligne des cartes à 28 px ; seules les icônes battent ; textes de l'auteur remplacés.

Vérifié sur le banc « Banc styles 04 » (marque sombre, accent jaune) : `check` sans erreur pour
chaque scène, images regardées. Restent signalés : `first_frame_empty` pour `orbe-pivot` et
`messages-verre` (des scènes de milieu, qui commencent sur le raccord de couleur), et
`composition_file_too_large` (lint) pour `mots-objets` (plus de 300 lignes, en-tête compris).
