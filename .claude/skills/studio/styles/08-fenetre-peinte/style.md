# Template n°8 · Fenêtre peinte · d'après Cursor (https://www.youtube.com/watch?v=An8IM-kPyms)

**Ce qu'on voit :** sur un blanc chaud presque nu, des phrases courtes centrées s'écrivent lettre à lettre et coupent net sur la démonstration : la fenêtre de l'application, posée sur un fond de bureau peint, filmée en gros plans rapides (flou de bougé) pendant que le curseur clique et tape. Une preuve en barres comparatives (la ligne de l'offre passe au noir) et un logo en cube qui roule ouvrent et ferment la vidéo, la fin sur fond sombre.
**Souvent utile pour :** une preuve chiffrée posée calmement (avant / après, comparaison d'options), puis l'offre montrée dans son vrai outil, chapitre par chapitre ; lancement d'une nouvelle version, d'un logiciel, d'un espace de formation.
**D'après :** YouTube, Cursor, lancement de Cursor 2.0 · 64 s · 16:9 (1920 × 1080, 60 images/s) · musique électronique très discrète, pas de voix.
**Mesures (`studio_motion.py reference`) :** 0,75 événement par seconde, écart médian 0,90 s, 3 coupes franches détectées (45,2, 46,5 et 62,3 s), 27,4 s d'images tenues (phrases et graphique tenus 2 s, écrans peu bougés). Tempo de la musique : environ 113 battements par minute, entrée franche à 3,2 s ; sonie -29 LUFS (très bas).
**Essai du kit (marque LMDM, 19,8 s) :** 1,11 événement par seconde en 16:9 comme en 9:16, écart médian 0,80 s, aucune image figée, `rythme` « ok ».

> On reprend la grammaire (phrase tapée, coupe nette, fenêtre filmée en gros plans, barres grises et ligne forte, cube logo, fin sombre), jamais le contenu : ni ses phrases, ni son logo, ni ses captures, ni le tableau peint de son fond d'écran, ni sa musique.

## 1. Le rythme

- **Le plus calme du catalogue** : l'original tient chaque phrase 2 s, le graphique 3 s, et laisse vivre l'écran filmé. Il se regarde comme une présentation de produit sûre d'elle.
- **Deux régimes qui alternent** : la phrase seule (immobile, une coupe nette avant et après), puis la démonstration (la caméra bouge toutes les 0,5 à 1,5 s : gros plan, recul, clic, frappe).
- **Les coupes tombent sur les temps de la musique** (environ 113 battements par minute), jamais au milieu d'un geste.
- **Chez toi** : le studio exige au moins un événement par seconde et aucune image tenue 1 s ou plus. Le kit garde le calme mais le resserre : phrases de 3 ou 4 mots tenues 0,7 à 0,9 s après la frappe, caméra qui avance de 6 % pendant la phrase, gros plans ajoutés sur le graphique, un geste toutes les 0,5 à 1 s dans la fenêtre. N'allonge jamais une phrase au-delà de ce que dit son en-tête : `rythme` la verrait figée.

## 2. La structure

L'original, scène par scène :

| Temps | Rôle | Ce qui s'y passe |
|---|---|---|
| 0 à 2 s | Ouverture | Le cube logo roule au centre, se pose, « 2.0 » apparaît à côté. |
| 2 à 3,8 s | Annonce | « Introducing Composer, our first agent model. » s'écrit, deux lignes centrées. |
| 4,4 à 8,4 s | Preuve | Deux graphiques en barres côte à côte (score, vitesse), cinq lignes ; celle du produit passe au noir, son nom en gras. |
| 8,4 à 11,5 s | Annonce | Une seconde phrase tapée (la nouvelle version). |
| 11,5 à 19 s | Démonstration | La fenêtre sur fond peint, vue entière ; gros plan sur les onglets, clic ; la barre latérale ; une tâche se tape dans le champ. |
| 19 à 20,3 s | Chapitre 1 | Une phrase tapée qui nomme la fonction. |
| 20,3 à 34,5 s | Démonstration | Un menu déroulant, puis trois colonnes qui travaillent en même temps. |
| 34,5 à 37 s | Chapitre 2 | Une phrase tapée. |
| 37 à 44 s | Démonstration | La revue des changements, gros plans sur les lignes modifiées. |
| 44 à 46 s | Chapitre 3 | Une phrase tapée. |
| 46 à 62 s | Démonstration | Le navigateur intégré, sélection d'un élément, la console. |
| 62,3 à 64,4 s | Fin | Coupe sur fond presque noir, cube blanc qui roule, nom en capitales qui sort de derrière lui. |

Chez toi (vidéo de page de 45 à 90 s), avec les compositions du kit :

1. **Ouverture** (2 s) : `t08-logo` en clair, le logo et le nom de l'offre.
2. **Promesse** (1,4 à 1,6 s) : `t08-phrase`, ce que l'offre change, en 3 ou 4 mots.
3. **Preuve** (4 s) : `t08-barres`, seulement avec des chiffres vrais pour chaque ligne.
4. **Démonstration en 2 ou 3 chapitres** : à chaque fois `t08-phrase` (le nom de la partie), puis `t08-fenetre` (7 s) remplie avec la vraie interface et le geste de cette partie.
5. **Fin** (3,8 s) : `t08-logo` en sombre, le nom et la phrase d'appel.

## 3. Les fonds et les couleurs

| Rôle dans l'original | Couleur mesurée | Avec la marque du client |
|---|---|---|
| Fond des phrases et du graphique | blanc chaud `#f7f7f4` | reste : c'est le look |
| Texte, barre forte | encre chaude `#1d1c19` à `#27251f` | l'encre de la marque : son fond s'il est sombre (LMDM : `#202022`), sinon son texte |
| Barres des autres options | gris chaud `#cdcdca` | reste |
| Séparateurs des lignes | `#eeeeeb` | reste (`#e8e8e4`) |
| Fond de la fin | presque noir `#13110b` | l'encre de la marque |
| Logo et nom de la fin | `#ececec` | blanc cassé `#f1f0ec` |
| Fond de bureau | un tableau impressionniste (bleus, verts, ocres) | un fond peint à touches de pinceau, généré (palette neutre de paysage, 2,5 % de touches à l'accent), ou une image à lui |
| Accent | aucun | rare : la barre forte si l'accent est assez foncé pour se lire sur le blanc chaud, sinon un petit carré à l'accent devant le nom ; le bouton d'envoi de la fenêtre ; quelques touches du fond peint |

- Le kit détecte seul si l'accent se lit sur le blanc chaud (luminance de 0,28 au plus). Avec le jaune de LMDM, la ligne forte passe à l'encre et un carré jaune cerné marque l'offre.
- Pas de dégradé, pas d'ombre sauf celle de la fenêtre (large et douce), pas de couleur pleine en fond : le seul passage sombre est la fin.
- L'interface montrée garde ses propres couleurs (celles de l'offre), comme la fenêtre de l'original garde les siennes.

## 4. La typographie

- **Phrases** : l'original prend une grotesque neutre, en 400, très serrée. Le kit prend la police de titres de la marque en 400. Police libre la plus proche si la marque n'impose rien : Inter (livrée avec le kit, pour les interfaces) ou Geist.
- **Graphique** : la police de texte de la marque ; noms des lignes en gris (`#6f6e69`), le nom fort en 700 et à l'encre ; titres d'axes sur deux lignes (la mesure, puis l'unité entre parenthèses).
- **Interface de la fenêtre** : Inter, aux tailles d'une vraie application (12 à 26 px en vue entière) ; c'est le gros plan qui la rend lisible.

| Texte | 1920 × 1080 | 1080 × 1920 | Casse, alignement |
|---|---|---|---|
| Phrase tapée (3 ou 4 mots) | 104 px (80 px dans l'original), espacement -0,03 em | 92 px, sur 2 ou 3 lignes | phrase, point final, centrée |
| Noms des lignes du graphique | 30 px | 30 px | phrase, à gauche |
| Graduations | 25 px | 25 px | chiffres |
| Titres d'axes | 31 px, deux lignes | 31 px | phrase, à gauche sous l'axe |
| Valeur de la ligne forte | 26 px en 600, dans la barre | 26 px | à droite dans la barre |
| Nom à côté du cube | 120 px en 400 | 104 px, sous le cube | tel quel |
| Phrase d'appel de la fin | 38 px | 38 px | phrase, centrée |

## 5. Les mouvements signature

1. **La phrase tapée** (`t08-phrase`) : la phrase est posée entière, lettres invisibles ; elles apparaissent à leur place définitive (le texte centré ne bouge pas), par petits paquets irréguliers, environ 45 lettres par seconde dans l'original, 25 dans le kit ; puis la tenue, et la coupe nette. La caméra avance de 6 % pendant toute la scène.
2. **Les barres comparatives** (`t08-barres`) : les axes se tracent depuis la gauche (0,45 s, `expo.out`), les graduations et les titres apparaissent ; les lignes arrivent de haut en bas (0,07 s d'écart), chaque barre grandit depuis la gauche (0,6 s, `expo.out`), toutes grises ; puis la ligne de l'offre prend sa couleur (0,25 s), son nom passe en gras et sa valeur compte au bout de sa barre (0,6 s). Ajout du kit : gros plan sur cette ligne dans le premier graphique (0,7 s, `expo.inOut`), glissé jusqu'au second, recul.
3. **La fenêtre filmée** (`t08-fenetre`) : vue entière sur le fond peint, puis gros plans de 0,5 s (`expo.inOut`) avec un flou de bougé qui monte à 7 px au milieu du mouvement ; le curseur macOS (noir cerné de blanc) clique (enfoncement de 0,07 s, onde), l'interface change d'un coup, sans animation ; une demande se tape dans le champ par petits groupes de lettres ; la réponse monte (0,45 s, `expo.out`) ; recul sur la vue entière.
4. **Le cube logo** (`t08-logo`) : un cube aux faces de l'encre (claires en fin de vidéo), le logo sur la face avant ; il roule depuis trois rotations qui se calment (1 s, `expo.out`), glisse à gauche (0,7 s, `expo.inOut`) pendant que le nom sort de derrière lui (0,7 s), puis continue de flotter d'un quart de tour.
5. **La fin sombre** : coupe nette sur l'encre, le même cube en clair, le nom en blanc cassé, la phrase d'appel qui s'écrit dessous et se tient.

## 6. Les transitions

- **La coupe nette** entre une phrase et une démonstration, sur un temps de la musique : c'est la ponctuation de ce template (et la bascule du blanc chaud au fond peint fait l'événement).
- **Dans une démonstration, c'est la caméra qui enchaîne** : gros plan, recul, glissé, toujours avec le flou de bougé, jamais de fondu.
- **La coupe sur le sombre** pour la fin, une seule fois.
- Pas de mosaïque, pas de flash, pas de volet, pas de fondu enchaîné.

## 7. Le produit à l'écran

- L'original montre **son vrai logiciel**, en enregistrement d'écran, dans une fenêtre macOS posée sur un fond de bureau peint ; la caméra va chercher chaque détail (onglets, menu, champ, lignes modifiées) au lieu de les écrire.
- **Chez toi** : la vraie interface de l'offre, reconstruite fidèlement en HTML d'après capture (le kit fournit un espace de formation par défaut : barre latérale de modules, leçon en vidéo, liste à cocher, champ de question) ou sa capture en image dans la fenêtre ; les gros plans montrent ce qui fait vendre. Une fonction que l'offre n'a pas ne s'invente pas : remplace le contenu par défaut, ne le garde jamais tel quel.
- Une vraie vidéo d'écran du client peut remplacer l'interface : elle se prépare avec `studio_motion.py preparer-video` et vit à la racine d'`index.html` (règle du studio), ce qui oblige à porter les gros plans sur son cadre ; pas construit dans le kit.

## 8. Le son

- **Musique de l'original** : électronique minimale et feutrée, environ 113 battements par minute, faite de pulsations graves douces et de petits clics, sans mélodie appuyée ; elle entre franchement à 3,2 s, après le logo, et se mixe très bas (-29 LUFS mesurés ; on vise -16 LUFS au mastering).
- **Chez toi** : l'ambiance « Tech minimale » des musiques de lancement (`musiques choisir --ambiance "Tech minimale"`), ou « Premium et calme » pour une offre haut de gamme ; l'entrée de batterie sur la première phrase.
- **Bruitages**, rares et doux : un clic de souris discret à chaque clic, une frappe de clavier très basse pendant que la phrase ou la demande s'écrit, une pulsation sourde sur chaque coupe vers une phrase. Pas de whoosh sur les gros plans, pas d'impact : le calme fait la marque de ce template.

## 9. L'ouverture et la fin

- **Ouverture** : le cube roule et se pose, le nom sort de derrière lui, sur le blanc chaud, en 2 s ; puis la coupe sur la première phrase. Le sujet se lit dès 1 s.
- **Fin** : coupe sur l'encre de la marque, le cube clair, le nom en blanc, et (ajout du kit, l'original n'en a pas) une phrase d'appel calme qui s'écrit dessous (« Le lien est juste en dessous. »), tenue 1,5 s ; c'est l'écran final, il peut se tenir.

## Ce qui ne se fera pas à l'identique

- **Le calme** : l'original tient ses phrases 2 s et laisse 27 s d'images presque fixes ; le studio refuse toute image tenue 1 s ou plus. Le kit raccourcit les phrases (3 ou 4 mots au lieu de 6 à 8), tape plus lentement (25 lettres par seconde au lieu de 45), écrit plus grand (104 px au lieu de 80), fait avancer la caméra pendant les phrases et ajoute des gros plans au graphique.
- **L'enregistrement d'écran** : remplacé par une interface reconstruite en HTML (ou la capture du client) que la caméra filme ; les gestes (clic, frappe, réponse) sont joués, pas enregistrés.
- **Le tableau du fond d'écran** (une œuvre réelle) : remplacé par un fond peint à touches de pinceau, généré à graine, ou par une image fournie par le client.
- **Le cube de l'original** est le logo de Cursor : le kit pose le logo plat de la marque sur la face avant d'un cube. Sans logo, l'initiale du nom.
- **« 2.0 » à côté du logo** : remplacé par le nom de l'offre.
- **Les phrases longues en deux lignes** de l'original : le kit vise 3 ou 4 mots (règle du studio) ; deux lignes seulement pour 5 ou 6 mots, rarement.
- **Pas d'appel à l'action dans l'original** : le kit en ajoute un, écrit en phrase calme.
- **La valeur au bout des barres** : absente de l'original, ajoutée pour que la preuve se lise sans les graduations.

## Sur une autre offre

C'est un look : il se pose sur toute offre qui a une interface à montrer. Ce qui suivait le produit de l'original s'adapte :

- **Formation** : la fenêtre est l'espace de formation (le contenu par défaut du kit : modules, leçon en vidéo, liste à cocher, question) ; les chapitres sont les parties de la méthode ; les barres comparent un résultat mesuré chez les élèves, si la page le donne.
- **Coaching** : la fenêtre est l'outil réel de l'accompagnement (agenda des séances, espace client, messagerie, document de suivi) ; les chapitres sont les étapes de l'accompagnement ; les barres, seulement avec des mesures vraies (sinon, pas de scène de barres).
- **Logiciel** : la fenêtre est sa capture ou sa reconstruction, les gros plans vont sur ses fonctions ; les barres comparent un temps, un coût ou un score face aux autres options, avec des chiffres sourcés.
- **Toujours** : le blanc chaud, les phrases tapées et la coupe nette, la fenêtre sur fond peint filmée en gros plans, l'accent rare, le cube et la fin sombre.

## En vertical et en carré

- **9:16 (1080 × 1920)** : mets `data-width="1080" data-height="1920"` sur la racine de chaque composition et sur son hôte ; tout se règle seul (classe `t08-vertical`) : phrase en 92 px sur 2 ou 3 lignes, les deux graphiques empilés (chacun avec ses noms), la fenêtre réduite au milieu du fond peint (ses gros plans remplissent l'écran au même cadrage), le nom sous le cube. Testé sur toutes les compositions, `rythme` « ok » (captures dans les preuves).
- **4:5 et carré** : pas de mise en page propre, non testé. La fenêtre se réduit seule pour tenir dans tout format. En 4:5 (1080 × 1350), la mise en page verticale s'applique mais elle est dessinée pour 1920 de haut : réduis la phrase à 80 px et le graphique à 4 lignes. En carré, c'est la mise en page horizontale qui s'applique, dessinée pour 1920 de large : le graphique déborde, place ses deux blocs l'un sous l'autre (`blocs` dans le script). À vérifier image par image.

## Les compositions du kit

Dossier `compositions/`, 16:9 par défaut, chacune avec son en-tête (ce qu'elle montre, sa durée, ce qu'on remplace). Elles se servent du kit du projet (`K`) et des variables de la marque (`--brand-*`) ; les identifiants commencent par `t08-`.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `t08-logo.html` | 2 s (clair) ou 3,8 s (sombre) | Ouverture ou fin : le cube au logo qui roule, le nom qui sort de derrière ; en fin, la phrase d'appel tapée | `FOND`, `LOGO`, `NOM`, `APPEL`, l'id (`t08-ouverture`, `t08-fin`) et la durée |
| `t08-phrase.html` | 1,4 s (3 mots) | La phrase tapée centrée, le titre de chaque partie | `LIGNES`, la durée (1,4 s pour 3 mots, +0,25 s par mot), un id par phrase |
| `t08-barres.html` | 4 s | La preuve : deux graphiques en barres, la ligne de l'offre qui prend sa couleur et sa valeur, le gros plan qui la lit | `LIGNES` (chiffres vrais seulement), `AXES` (titres, échelle, graduations, format) |
| `t08-fenetre.html` | 7 s | La démonstration : la fenêtre sur fond peint, cinq gros plans, quatre clics, la demande tapée, la réponse | `APP` (tout le contenu de l'interface), `PLANS`, `PALETTE` et `GRAINE` ou `FOND_IMAGE` |

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
