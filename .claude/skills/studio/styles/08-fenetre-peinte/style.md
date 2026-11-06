# Style n°8 · Fenêtre peinte · d'après Cursor (https://www.youtube.com/watch?v=An8IM-kPyms)

**Ce qu'on voit :** sur le clair de la marque presque nu, des phrases courtes centrées s'écrivent lettre à lettre et coupent net sur la démonstration : la fenêtre de l'application, avec sa vraie interface (ses captures), posée sur un bureau aux couleurs de la marque (l'aplat de son accent, un dégradé de ses gris ou sa nuit), filmée en gros plans rapides (flou de bougé) pendant que le curseur clique et que l'écran change. Une preuve en barres comparatives (la ligne de l'offre se remplit de sa nuit) et un cube à son vrai logo qui roule ouvrent et ferment la vidéo, la fin sur sa nuit.
**Souvent utile pour :** une preuve chiffrée posée calmement (avant / après, comparaison d'options), puis l'offre montrée dans son vrai outil, chapitre par chapitre ; lancement d'une nouvelle version, d'un logiciel, d'un espace de formation.
**D'après :** YouTube, Cursor, lancement de Cursor 2.0 · 64 s · 16:9 (1920 × 1080, 60 images/s) · musique électronique très discrète, pas de voix.
**Mesures (`studio_motion.py reference`) :** 0,75 événement par seconde, écart médian 0,90 s, 3 coupes franches détectées (45,2, 46,5 et 62,3 s), 27,4 s d'images tenues (phrases et graphique tenus 2 s, écrans peu bougés). Tempo de la musique : environ 113 battements par minute, entrée franche à 3,2 s ; sonie -29 LUFS (très bas).
**Essai du kit refait le 06/11/2026 (marque LMDM, 19,8 s, avec les vraies captures de sa page) :** 1,23 événement par seconde en 16:9 comme en 9:16, écart médian 0,70 s, aucune image figée ; `rythme` et `palette` « ok » dans les deux formats.

> On reprend la grammaire (phrase tapée, coupe nette, fenêtre filmée en gros plans, barres grises et ligne forte, cube logo, fin sombre), jamais le contenu : ni ses phrases, ni son logo, ni ses captures, ni le tableau peint de son fond d'écran, ni ses couleurs, ni sa musique.

## 1. Le rythme

- **Le plus calme du catalogue** : l'original tient chaque phrase 2 s, le graphique 3 s, et laisse vivre l'écran filmé. Il se regarde comme une présentation de produit sûre d'elle.
- **Deux régimes qui alternent** : la phrase seule (immobile, une coupe nette avant et après), puis la démonstration (la caméra bouge toutes les 0,5 à 1,5 s : gros plan, recul, clic, frappe).
- **Les coupes tombent sur les temps de la musique** (environ 113 battements par minute), jamais au milieu d'un geste.
- **Chez toi** : le studio exige au moins un événement par seconde et aucune image tenue 1 s ou plus. Le kit garde le calme mais le resserre : phrases de 3 ou 4 mots tenues 0,7 à 0,9 s après la frappe, caméra qui avance de 6 % pendant la phrase, gros plans ajoutés sur le graphique, un geste toutes les 0,5 à 1 s dans la fenêtre. N'allonge jamais une phrase au-delà de ce que dit son en-tête : `rythme` la verrait figée.

## 2. Les gestes signature et leur place

La structure vient de la vidéo du client, jamais de l'original ([../README.md](../README.md),
« Appliquer un style ») : chaque scène de son plan prend le geste qui sert son rôle, les autres se
construisent dans la grammaire des sections 3 à 7. Au moins trois gestes par vidéo (deux sous
15 s) ; le détail de chaque mouvement est en section 5.

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le cube logo | un cube à son vrai logo, aux faces de ses couleurs, qui roule et se pose, le nom qui sort de derrière lui | ouverture, le nom de l'offre | `t08-logo` (clair) |
| La phrase tapée et la coupe nette | une phrase courte qui s'écrit à sa place, centrée, puis coupe sur un temps | promesse, titre de chapitre, annonce | `t08-phrase` |
| Les barres comparatives | deux graphiques en barres, la ligne de l'offre qui se remplit de sa couleur et compte sa valeur | preuve (chiffres vrais seulement) | `t08-barres` |
| La fenêtre filmée | sa vraie interface (ses captures) dans une fenêtre posée sur un bureau à ses couleurs, filmée en gros plans, le curseur qui clique et l'écran qui change, une demande qui se tape | démonstration | `t08-fenetre` |
| La fin sombre | coupe sur sa nuit, le cube aux faces claires, le nom, la phrase d'appel qui s'écrit | appel, fin | `t08-logo` (sombre) |

**Pour montrer son produit** : en chapitres, chacun annoncé par une phrase tapée qui nomme la
partie, puis la fenêtre remplie de ses vraies captures et du geste de cette partie (le clic qui
change d'écran, la demande tapée, le gros plan sur ce qui fait vendre).

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre :

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

### Des enchaînements qui marchent

Des points de départ quand le plan s'y prête, jamais une obligation.

Une vidéo de page de 45 à 90 s qui annonce, comme l'original, puis démontre :

1. **Ouverture** (2 s) : `t08-logo` en clair, le logo et le nom de l'offre.
2. **Promesse** (1,4 à 1,6 s) : `t08-phrase`, ce que l'offre change, en 3 ou 4 mots.
3. **Preuve** (4 s) : `t08-barres`, seulement avec des chiffres vrais pour chaque ligne.
4. **Démonstration en 2 ou 3 chapitres** : à chaque fois `t08-phrase` (le nom de la partie), puis `t08-fenetre` (7 s) remplie de ses vraies captures et du geste de cette partie.
5. **Fin** (3,8 s) : `t08-logo` en sombre, le nom et la phrase d'appel.

## 3. Les fonds et les couleurs

Les couleurs viennent de sa marque, et seulement d'elle ([style.md](../../references/style.md),
« La palette ») : son clair, sa nuit, ses gris, son accent en aplat plein, du noir et du blanc en
transparence pour les ombres et les filets. Ses captures gardent leurs vraies couleurs.

| Rôle dans l'original | Couleur mesurée | Avec la marque du client |
|---|---|---|
| Fond des phrases et du graphique | blanc chaud `#f7f7f4` | son clair : `var(--brand-clair)` |
| Texte, barre forte | encre chaude `#1d1c19` à `#27251f` | sa nuit : `var(--brand-sombre)` (sur une marque claire, c'est son texte) |
| Barres des autres options | gris chaud `#cdcdca` | `var(--brand-gris-4)` |
| Noms des lignes, graduations | gris chauds | `var(--brand-gris-2)`, `var(--brand-gris-1)` |
| Séparateurs des lignes | `#eeeeeb` | noir à 7 % |
| Fond de la fin | presque noir `#13110b` | sa nuit |
| Logo et nom de la fin | `#ececec` | son clair ; la phrase d'appel en `var(--brand-gris-4)` |
| Fond de bureau | un tableau impressionniste (bleus, verts, ocres) | l'aplat de son accent (le défaut), un dégradé entre ses gris, sa nuit, ou une vraie photo à lui ; jamais un fond peint ni un paysage |
| Accent | aucun | rare et toujours plein : le bureau en aplat, la barre forte s'il se lit sur le clair (sinon un carré plein devant le nom), la face du cube qui porte son logo |

- Le kit choisit seul la couleur de la ligne forte : l'accent s'il se lit comme une barre sur le clair (contraste de 3:1 au moins, sa valeur écrite dedans en `var(--brand-contrast)`), sinon sa nuit (le jaune de LMDM, l'orange de Dupliq.me), avec un carré plein de l'accent, cerné de sa nuit, devant le nom. Seul ce choix entre deux couleurs de sa marque se calcule : aucune couleur n'en est tirée.
- **Sur n'importe quelle marque, claire ou sombre**, les jetons s'en chargent : la nuit est sa couleur la plus sombre (son fond s'il est sombre, sinon son texte), le clair la plus claire, ses gris entre les deux ; la fin reste donc sombre et son nom clair même sur une marque claire. Tout texte garde un contraste d'au moins 4,5:1.
- **Jamais une teinte tirée de l'accent** (story refusée du 06/11/2026) : ni `color-mix` avec l'accent, ni l'accent en transparence, ni une ombre posée sur l'aplat de l'accent (elle le salirait en brun ou en olive) : sur ce bureau, la fenêtre prend un trait fin de sa nuit à la place de son ombre. La ligne forte se remplit de gauche à droite, jamais par un fondu de couleurs.
- Pas de dégradé sauf entre ses gris (le bureau « gris »), pas d'ombre sauf celle de la fenêtre (large et douce, sur un bureau gris ou sombre), pas de couleur pleine en fond hors du bureau : le seul passage sombre est la fin.
- Ses captures gardent leurs propres couleurs (celles de son offre), comme la fenêtre de l'original garde les siennes ; les trois points de la barre de titre sont gris.

## 4. La typographie

- **Phrases** : l'original prend une grotesque neutre, en 400, très serrée. Le kit prend la police de titres de la marque en 400. Police libre la plus proche si la marque n'impose rien : Inter (livrée avec le kit, pour les interfaces) ou Geist.
- **Graphique** : la police de texte de la marque ; noms des lignes en gris (`var(--brand-gris-2)`), le nom fort en 700 et à sa nuit ; titres d'axes sur deux lignes (la mesure, puis l'unité entre parenthèses).
- **Fenêtre** : ses captures à leur vraie taille, la barre de titre en Inter 15 px ; c'est le gros plan qui rend la capture lisible (1,8 au plus sur une capture en image, sinon elle devient floue).

| Texte | 1920 × 1080 | 1080 × 1920 | Casse, alignement |
|---|---|---|---|
| Phrase tapée (3 ou 4 mots) | 104 px (80 px dans l'original), espacement -0,03 em | 112 px, sur 2 ou 3 lignes équilibrées | phrase, point final, centrée |
| Noms des lignes du graphique | 30 px | 30 px | phrase, à gauche |
| Graduations | 25 px | 25 px | chiffres |
| Titres d'axes | 31 px, deux lignes | 31 px | phrase, à gauche sous l'axe |
| Valeur de la ligne forte | 26 px en 600, dans la barre | 26 px | à droite dans la barre |
| Nom à côté du cube | 120 px en 400 | 104 px, sous le cube | tel quel |
| Phrase d'appel de la fin | 38 px | 38 px | phrase, centrée |
| Titre de la fenêtre sans capture | 104 px en 600 | 104 px | tel quel, centré |

## 5. Les mouvements signature

1. **La phrase tapée** (`t08-phrase`) : la phrase est posée entière, lettres invisibles ; elles apparaissent à leur place définitive (le texte centré ne bouge pas), par petits paquets irréguliers, environ 45 lettres par seconde dans l'original, 25 dans le kit ; puis la tenue, et la coupe nette. La caméra avance de 6 % pendant toute la scène.
2. **Les barres comparatives** (`t08-barres`) : les axes se tracent depuis la gauche (0,45 s, `expo.out`), les graduations et les titres apparaissent ; les lignes arrivent de haut en bas (0,07 s d'écart), chaque barre grandit depuis la gauche (0,6 s, `expo.out`), toutes grises ; puis la ligne de l'offre se remplit de sa couleur de gauche à droite (0,35 s), son nom passe en gras et sa valeur compte au bout de sa barre (0,6 s). Ajout du kit : gros plan sur cette ligne dans le premier graphique (0,7 s, `expo.inOut`), glissé jusqu'au second, recul.
3. **La fenêtre filmée** (`t08-fenetre`) : vue entière sur le bureau, puis gros plans de 0,5 s (`expo.inOut`) avec un flou de bougé qui monte à 7 px au milieu du mouvement ; le curseur macOS (noir cerné de blanc) clique (enfoncement de 0,07 s, onde) et la capture suivante remplace l'écran d'un coup, sans animation ; une demande se tape dans le vrai champ de sa capture par petits groupes de lettres, puis part au clic suivant ; recul sur la vue entière. Sans capture, la caméra va et vient sur le seul titre.
4. **Le cube logo** (`t08-logo`) : un cube aux faces de ses couleurs (sa nuit et ses gris, claires en fin de vidéo ; la face avant à son accent quand son logo est une icône carrée), son vrai logo sur la face avant ; il roule depuis trois rotations qui se calment (1 s, `expo.out`), glisse à gauche (0,7 s, `expo.inOut`) pendant que le nom sort de derrière lui (0,7 s), puis continue de flotter d'un quart de tour. Sans logo, pas de cube : le nom monte seul de derrière son masque.
5. **La fin sombre** : coupe nette sur sa nuit, le même cube aux faces claires, le nom à son clair, la phrase d'appel qui s'écrit dessous et se tient.

## 6. Les transitions

- **La coupe nette** entre une phrase et une démonstration, sur un temps de la musique : c'est la ponctuation de ce style (et la bascule du clair au bureau de couleur fait l'événement).
- **Dans une démonstration, c'est la caméra qui enchaîne** : gros plan, recul, glissé, toujours avec le flou de bougé, jamais de fondu.
- **La coupe sur le sombre** pour la fin, une seule fois.
- Pas de mosaïque, pas de flash, pas de volet, pas de fondu enchaîné.

## 7. Le produit à l'écran

- L'original montre **son vrai logiciel**, en enregistrement d'écran, dans une fenêtre macOS posée sur un fond de bureau peint ; la caméra va chercher chaque détail (onglets, menu, champ, lignes modifiées) au lieu de les écrire.
- **Chez toi** : ses vraies captures dans la fenêtre (`CAPTURES`, dans `assets/images/` : sa page, son espace de formation, son logiciel), une par écran, chaque clic montrant la suivante ; ou son interface reconstruite fidèlement en HTML d'après capture, à la place des captures. Le kit n'en invente aucune : sans capture, la fenêtre reste vide, à ses couleurs, avec son seul titre (garde alors la scène courte). Les gros plans montrent ce qui fait vendre ; une fonction que l'offre n'a pas ne s'invente pas.
- Une vraie vidéo d'écran du client peut remplacer les captures : elle se prépare avec `studio_motion.py preparer-video` et vit à la racine d'`index.html` (règle du studio), ce qui oblige à porter les gros plans sur son cadre ; pas construit dans le kit.

## 8. Le son

- **Musique de l'original** : électronique minimale et feutrée, environ 113 battements par minute, faite de pulsations graves douces et de petits clics, sans mélodie appuyée ; elle entre franchement à 3,2 s, après le logo, et se mixe très bas (-29 LUFS mesurés ; on vise -16 LUFS au mastering).
- **Chez toi** : l'ambiance « Tech minimale » des musiques de lancement (`musiques choisir --ambiance "Tech minimale"`), ou « Premium et calme » pour une offre haut de gamme ; l'entrée de batterie sur la première phrase.
- **Bruitages**, rares et doux : un clic de souris discret à chaque clic, une frappe de clavier très basse pendant que la phrase ou la demande s'écrit, une pulsation sourde sur chaque coupe vers une phrase. Pas de whoosh sur les gros plans, pas d'impact : le calme fait la marque de ce style.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 8`) : « Tech minimale » puis « Premium et calme », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture** : le cube roule et se pose, le nom sort de derrière lui, sur son clair, en 2 s ; puis la coupe sur la première phrase. Le sujet se lit dès 1 s.
- **Fin** : coupe sur sa nuit, le cube aux faces claires, le nom à son clair, et (ajout du kit, l'original n'en a pas) une phrase d'appel calme qui s'écrit dessous (« Le lien est juste en dessous. »), tenue 1,5 s ; c'est l'écran final, il peut se tenir.

## Ce qui ne se fera pas à l'identique

- **Les images de l'original ne se refont pas** : ni le tableau de son fond d'écran (une œuvre réelle), ni ses captures du logiciel. Le bureau prend un fond de sa marque (l'aplat de son accent, un dégradé de ses gris, sa nuit) ou sa vraie photo (`FOND_IMAGE`), et la fenêtre ses vraies captures ; jamais un fond peint généré, un paysage ni une interface inventée.
- **Ses couleurs** (le blanc chaud, l'encre et les gris chauds) → son clair, sa nuit et ses gris (section 3) ; les feux de la fenêtre macOS → trois points gris.
- **Le calme** : l'original tient ses phrases 2 s et laisse 27 s d'images presque fixes ; le studio refuse toute image tenue 1 s ou plus. Le kit raccourcit les phrases (3 ou 4 mots au lieu de 6 à 8), tape plus lentement (25 lettres par seconde au lieu de 45), écrit plus grand (104 px au lieu de 80), fait avancer la caméra pendant les phrases et ajoute des gros plans au graphique.
- **L'enregistrement d'écran** : remplacé par ses captures (ou son interface reconstruite d'après capture) que la caméra filme ; les gestes (clic, changement d'écran, frappe) sont joués, pas enregistrés.
- **Le cube de l'original** est le logo de Cursor : le kit pose le vrai logo de la marque sur la face avant d'un cube aux couleurs de sa marque. Sans logo, pas de cube : son nom seul, jamais une initiale qui ferait un faux logo.
- **« 2.0 » à côté du logo** : remplacé par le nom de l'offre.
- **Les phrases longues en deux lignes** de l'original : le kit vise 3 ou 4 mots (règle du studio) ; deux lignes seulement pour 5 ou 6 mots, rarement.
- **Pas d'appel à l'action dans l'original** : le kit en ajoute un, écrit en phrase calme.
- **La valeur au bout des barres** : absente de l'original, ajoutée pour que la preuve se lise sans les graduations.

## Sur une autre offre

C'est un look : il se pose sur toute offre qui a une interface à montrer. Ce qui suivait le produit de l'original s'adapte :

- **Formation** : la fenêtre montre ses vraies captures de l'espace de formation (ses modules, une leçon, un exercice) ; les chapitres sont les parties de la méthode ; les barres comparent un résultat mesuré chez les élèves, si la page le donne.
- **Coaching** : la fenêtre montre l'outil réel de l'accompagnement (agenda des séances, espace client, messagerie, document de suivi), en captures ; les chapitres sont les étapes de l'accompagnement ; les barres, seulement avec des mesures vraies (sinon, pas de scène de barres).
- **Logiciel** : la fenêtre est sa capture ou sa reconstruction d'après capture, les gros plans vont sur ses fonctions ; les barres comparent un temps, un coût ou un score face aux autres options, avec des chiffres sourcés.
- **Sans interface à montrer** : sa page de vente en captures (le titre, la promesse, le bouton), comme dans l'essai du kit.
- **Toujours** : son clair presque nu, les phrases tapées et la coupe nette, la fenêtre filmée en gros plans sur un bureau à ses couleurs, l'accent rare et plein, le cube à son logo et la fin sur sa nuit.

## En vertical et en carré

- **9:16 (1080 × 1920)** : mets `data-width="1080" data-height="1920"` sur la racine de chaque composition et sur son hôte ; tout se règle seul (classe `t08-vertical`) : phrase en 112 px sur 2 ou 3 lignes équilibrées, les deux graphiques empilés (chacun avec ses noms), la fenêtre réduite au milieu du bureau et ses gros plans qui serrent davantage (×1,4) pour remplir l'écran, le nom sous le cube. Essayé sur toutes les compositions le 06/11/2026, `rythme` et `palette` « ok ». Le bureau à l'aplat de l'accent tient bien les bandes au-dessus et au-dessous de la fenêtre ; en gris, elles font vide.
- **4:5 et carré** : pas de mise en page propre, non testé. La fenêtre se réduit seule pour tenir dans tout format. En 4:5 (1080 × 1350), la mise en page verticale s'applique mais elle est dessinée pour 1920 de haut : réduis la phrase à 90 px et le graphique à 4 lignes. En carré, c'est la mise en page horizontale qui s'applique, dessinée pour 1920 de large : le graphique déborde, place ses deux blocs l'un sous l'autre (`blocs` dans le script). À vérifier image par image.

## Les compositions du kit

Dossier `compositions/`, 16:9 par défaut, chacune avec son en-tête (ce qu'elle montre, sa durée, ce qu'on remplace). Elles se servent du kit du projet (`K`) et des variables de la marque (`--brand-*`) ; les identifiants commencent par `t08-`.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `t08-logo.html` | 2 s (clair) ou 3,8 s (sombre) | Ouverture ou fin : le cube à son vrai logo qui roule, le nom qui sort de derrière ; en fin, la phrase d'appel tapée | `FOND`, `LOGO`, `FACE`, `LOGO_TAILLE`, `NOM`, `APPEL`, l'id (`t08-ouverture`, `t08-fin`) et la durée |
| `t08-phrase.html` | 1,4 s (3 mots) | La phrase tapée centrée, le titre de chaque partie | `LIGNES`, la durée (1,4 s pour 3 mots, +0,25 s par mot), un id par phrase |
| `t08-barres.html` | 4 s | La preuve : deux graphiques en barres, la ligne de l'offre qui se remplit de sa couleur et compte sa valeur, le gros plan qui la lit | `LIGNES` (chiffres vrais seulement), `AXES` (titres, échelle, graduations, format) |
| `t08-fenetre.html` | 7 s (3 s sans capture) | La démonstration : la fenêtre et ses vraies captures sur un bureau à ses couleurs, sept gros plans, les clics qui changent d'écran, la demande tapée dans son champ | `TITRE`, `CAPTURES`, `CLICS`, `DEMANDE`, `PLANS`, `FOND` (ou `FOND_IMAGE`), `FENETRE` |

Le montage dans `index.html` (16:9), tout sur la piste 1, bout à bout, coupes nettes :

```html
<div id="s1-hote" data-composition-id="t08-ouverture" data-composition-src="compositions/t08-ouverture.html" data-start="0" data-duration="2" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s2-hote" data-composition-id="t08-phrase-1" data-composition-src="compositions/t08-phrase-1.html" data-start="2" data-duration="1.4" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s3-hote" data-composition-id="t08-fenetre" data-composition-src="compositions/t08-fenetre.html" data-start="3.4" data-duration="7" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s4-hote" data-composition-id="t08-phrase-2" data-composition-src="compositions/t08-phrase-2.html" data-start="10.4" data-duration="1.6" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s5-hote" data-composition-id="t08-barres" data-composition-src="compositions/t08-barres.html" data-start="12" data-duration="4" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s6-hote" data-composition-id="t08-fin" data-composition-src="compositions/t08-fin.html" data-start="16" data-duration="3.8" data-track-index="1" data-width="1920" data-height="1080"></div>
```

Chaque copie d'une composition (deux phrases, l'ouverture et la fin) change son id partout dans le fichier (racine, script, préfixe CSS) : deux scènes au même id se marcheraient dessus.
