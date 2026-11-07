# Notes de maintenance · Style n°8 · Fenêtre posée

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/08-fenetre-peinte/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les mesures, les essais, ce qui a changé) est rangé ici.

## Ce qui sortait de la fiche

### L'ancien nom

« Fenêtre peinte » (jusqu'à la 0.9.0 ; il désigne toujours ce style). Le dossier garde ce nom
(`08-fenetre-peinte`) ; l'index (`styles/README.md`) dit qu'un client qui l'emploie veut le même style.

### Les mesures de l'original et des essais

- **Original** (`studio_motion.py reference`) : 1920 × 1080, 60 images/s ; 0,75 événement par
  seconde, écart médian 0,90 s, 3 coupes franches détectées (45,2, 46,5 et 62,3 s), 27,4 s
  d'images tenues (phrases et graphique tenus 2 s, écrans peu bougés). Tempo de la musique :
  environ 113 battements par minute, entrée franche à 3,2 s (après le logo) ; sonie -29 LUFS (très
  bas ; on vise -16 LUFS au mastering). L'original tape environ 45 lettres par seconde et écrit ses
  phrases en 80 px.
- **Essai du kit refait le 06/11/2026** (marque LMDM, 30,8 s, avec les vraies captures de sa page
  et des phrases complètes de 9 et 11 mots tenues le temps de leur lecture) : `rythme` « ok » (0,77
  événement par seconde en 16:9 comme en 9:16, écart médian 0,80 s, aucune image vraiment
  immobile) et `palette` « ok » dans les deux formats. L'essai d'avant (19,8 s) tenait des phrases
  de 3 ou 4 mots 0,7 à 0,9 s : trop court pour les lire. Toutes les compositions essayées en 9:16
  le 06/11/2026, `rythme` et `palette` « ok ».
- La phrase d'exemple de `t08-phrase` était « Tu donnes le lien de ta page de vente. » (9 mots,
  tirée du parcours de Publicitaire IA) ; la ligne « Sans interface à montrer : sa page de vente en
  captures » renvoyait à cet essai.

### La citation d'ouverture

> On reprend la grammaire (phrase tapée, coupe nette, fenêtre filmée en gros plans, barres grises
> et ligne forte, cube logo, fin sombre), jamais le contenu : ni ses phrases, ni son logo, ni ses
> captures, ni le tableau peint de son fond d'écran, ni ses couleurs, ni sa musique.

L'index le dit désormais pour tous les styles.

### L'original, scène par scène

| Temps | Rôle | Ce qui s'y passe |
|---|---|---|
| 0 à 2 s | Ouverture | Le cube logo roule au centre, se pose, « 2.0 » apparaît à côté. |
| 2 à 3,8 s | Annonce | « Introducing Composer, our first agent model. » s'écrit, deux lignes centrées. |
| 4,4 à 8,4 s | Preuve | Deux graphiques en barres côte à côte (score, vitesse), cinq lignes ; celle du produit passe au noir, son nom en gras. |
| 8,4 à 11,5 s | Annonce | Une seconde phrase tapée (la nouvelle version). |
| 11,5 à 19 s | Démonstration | La fenêtre sur un fond de bureau peint, vue entière ; gros plan sur les onglets, clic ; la barre latérale ; une tâche se tape dans le champ. |
| 19 à 20,3 s | Chapitre 1 | Une phrase tapée qui nomme la fonction. |
| 20,3 à 34,5 s | Démonstration | Un menu déroulant, puis trois colonnes qui travaillent en même temps. |
| 34,5 à 37 s | Chapitre 2 | Une phrase tapée. |
| 37 à 44 s | Démonstration | La revue des changements, gros plans sur les lignes modifiées. |
| 44 à 46 s | Chapitre 3 | Une phrase tapée. |
| 46 à 62 s | Démonstration | Le navigateur intégré, sélection d'un élément, la console. |
| 62,3 à 64,4 s | Fin | Coupe sur fond presque noir, cube blanc qui roule, nom en capitales qui sort de derrière lui. |

L'original montre son vrai logiciel en enregistrement d'écran, dans une fenêtre macOS posée sur
un fond de bureau peint (un tableau réel).

### Les couleurs mesurées de l'original

| Rôle | Couleur mesurée |
|---|---|
| Fond des phrases et du graphique | blanc chaud `#f7f7f4` |
| Texte, barre forte | encre chaude `#1d1c19` à `#27251f` |
| Barres des autres options | gris chaud `#cdcdca` |
| Noms des lignes, graduations | gris chauds |
| Séparateurs des lignes | `#eeeeeb` |
| Fond de la fin | presque noir `#13110b` |
| Logo et nom de la fin | `#ececec` |
| Fond de bureau | un tableau impressionniste (bleus, verts, ocres) |
| Accent | aucun |

La ligne forte passe à la nuit avec un carré de l'accent quand l'accent ne se lit pas en barre :
c'était le cas du jaune de LMDM et de l'orange de Dupliq.me. La règle « jamais une teinte tirée de
l'accent » est née de la story refusée du 06/11/2026 (l'accent en transparence et une ombre sur
l'aplat de l'accent salissaient le jaune en brun ou en olive).

### Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas** : ni le tableau de son fond d'écran (une œuvre
  réelle), ni ses captures du logiciel. Le bureau prend un fond de sa marque ou sa vraie photo
  (`FOND_IMAGE`), et la fenêtre ses vraies captures ; jamais un fond peint généré, un paysage ni
  une interface inventée.
- **Ses couleurs** (le blanc chaud, l'encre et les gris chauds) → son clair, sa nuit et ses gris ;
  les feux de la fenêtre macOS → trois points gris.
- **Le calme** : l'original tient ses phrases 2 s et laisse 27 s d'images presque fixes. Le kit
  tient ses phrases le temps de leur lecture (0,3 s par mot + 0,8 s), tape plus lentement (25
  lettres par seconde au lieu de 45), écrit plus grand (104 px au lieu de 80) et fait dériver la
  caméra pendant les phrases ; une tenue calme ne se corrige jamais en raccourcissant la phrase ni
  en recadrant.
- **L'enregistrement d'écran** : remplacé par ses captures (ou son interface reconstruite d'après
  capture) que la caméra filme ; les gestes (clic, changement d'écran, frappe) sont joués.
- **Le cube de l'original** est le logo de Cursor : le kit pose le vrai logo de la marque sur la
  face avant d'un cube à ses couleurs. Sans logo, pas de cube : son nom seul, jamais une initiale.
- **« 2.0 » à côté du logo** : remplacé par le nom de l'offre.
- **Les phrases longues en deux lignes** : gardées en deux lignes équilibrées (trois en 9:16).
- **Pas d'appel à l'action dans l'original** : le kit en ajoute un, écrit en phrase calme.
- **La valeur au bout des barres** : absente de l'original, ajoutée pour que la preuve se lise sans
  les graduations.

## Le ménage du 07/11/2026

Taille de la fiche : 24 606 octets avant, 17 206 après (`wc -c`, -30 %).

**La fiche**
- Sortis vers cette note : l'ancien nom, les mesures, l'essai du kit, la citation d'ouverture,
  l'original scène par scène, la colonne « Couleur mesurée », la story refusée, « Ce qui ne se fera
  pas à l'identique », les exemples de l'auteur (LMDM, Dupliq.me, « comme dans l'essai du kit »). Le
  lien vers `references/style.md` devient `../../references/image.md`.
- Retiré ce que l'index dit déjà : l'ouverture de la section 2, « Sur n'importe quelle marque ».
- Les mots : « 8 mots conseillés, 12 au plus » et « 8 à 12 mots » deviennent « 8 mots au plus »
  partout (des phrases complètes, mais de 8 mots au plus : au-delà, on coupe des mots, jamais la
  police) ; le graphique tient en 8 mots (un mot par axe, l'unité dans la valeur).
- La caméra : plus de gros plans ni d'allers-retours sous le graphique (dérive vers la ligne forte) ;
  pendant une demande tapée, aucun gros plan ; sans capture, plus de va-et-vient : une dérive lente.
- Les tailles suivent les scènes : noms des lignes 30 → 36 px, valeur 26 → 32 px, titres d'axes
  31 → 32 px (un mot), graduations en texture, phrase d'appel 38 → 48 px ; le nom à côté du cube et
  le nom d'une fenêtre sans capture deviennent des mots héros (environ 60 % de la largeur).
- Les durées : `t08-phrase` 5,1 → 4,6 s pour la phrase d'exemple (7 mots), `t08-barres` 4 → 5 s ;
  le montage d'exemple suit.
- « Ce qu'on remplace » renvoie à l'objet `EXEMPLE` de chaque scène.

**Les scènes** (toutes : un objet `EXEMPLE` unique en tête du script)
- `t08-phrase` : phrase d'exemple neutre de 7 mots (« Ta méthode, enfin rangée au même endroit. »),
  « 8 mots au plus » dans l'en-tête ; dérive ramenée de 6,1 à 5,5 %.
- `t08-barres` : libellés courts (« Manuel », « Agence », « Ton offre », « Coach »), 4 lignes, un mot
  par axe et l'unité dans la valeur ; noms 36 px, valeur 32 px, titres 32 px, graduations en
  `data-layout-ignore` ; les trois recadrages (gros plan, glissé, recul) sous la lecture remplacés
  par une dérive de 5 % vers la ligne forte ; tenue de 4 s (D = 5 s).
- `t08-fenetre` : le repli « sans capture » (allers-retours de caméra de 0,5 s avec flou sous le
  titre) est retiré : aucun gros plan, son nom seul en grand, dérive lente de 4 % ; les gros plans
  qui tomberaient pendant la lecture d'une demande sont retirés ; la barre de titre (15 px) en
  texture ; les trois points en `--brand-gris-4` / `--brand-gris-2` au lieu de noir ou blanc en
  transparence.
- `t08-logo` : le nom en mot héros (le cube suit sa taille), la phrase d'appel à 48 px (52 en 9:16),
  la mise en page calculée d'après le bloc ; logo par défaut `brand/logo.png` (le banc n'a pas de
  `logo.svg`).
