# Style n°8 · Fenêtre posée · d'après Cursor (https://www.youtube.com/watch?v=An8IM-kPyms)

**Ce qu'on voit :** sur le clair de la marque presque nu, des phrases complètes et courtes, centrées, s'écrivent lettre à lettre et coupent net sur la démonstration : la fenêtre de l'application, avec ses vraies captures, posée sur un bureau à ses couleurs, filmée en gros plans rapides pendant que le curseur clique. Des barres comparatives prouvent ; un cube à son vrai logo ouvre et ferme la vidéo, la fin sur sa nuit.
**Souvent utile pour :** une preuve chiffrée posée calmement (avant / après, comparaison d'options), puis l'offre montrée dans son vrai outil, chapitre par chapitre ; lancement d'une nouvelle version, d'un logiciel, d'un espace de formation.
**D'après :** YouTube, Cursor, lancement de Cursor 2.0 · 64 s · 16:9 · musique électronique très discrète, pas de voix.

## 1. Le rythme

- **Le plus calme du catalogue** : chaque phrase se tient le temps de sa lecture, le graphique 4 s, l'écran filmé vit. Il se regarde comme une présentation de produit sûre d'elle.
- **Deux régimes qui alternent** : la phrase seule (immobile, la lumière du papier qui glisse derrière elle, une coupe nette avant et après), puis la démonstration (la caméra filme la fenêtre : gros plan, recul, clic, toutes les 0,5 à 1,5 s). Dès qu'un texte se lit (une demande tapée, le graphique), la caméra ne recadre plus : elle attend qu'il soit lu.
- **Les coupes tombent sur les temps de la musique**, jamais au milieu d'un geste.
- **Chez toi** : des phrases complètes, de 8 mots au plus (au-delà, coupe des mots : jamais une police plus petite), tapées puis tenues immobiles le temps de leur lecture (la scène calcule sa durée), pendant que la lumière du papier glisse lentement derrière elles (`sine.inOut`). Une phrase tenue sur ce clair presque nu est une image presque fixe : c'est le calme du style, sans figer l'image. Garde-les rares (une par chapitre) ; la fenêtre et le graphique portent le rythme.

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| Le cube logo | un cube à son vrai logo, aux faces de ses couleurs, qui roule et se pose, le nom qui sort de derrière lui | ouverture, le nom de l'offre | `t08-logo` (clair) |
| La phrase tapée et la coupe nette | une phrase complète de 8 mots au plus qui s'écrit à sa place, centrée, puis coupe sur un temps | promesse, titre de chapitre, annonce | `t08-phrase` |
| Les barres comparatives | deux graphiques en barres, la ligne de l'offre qui se remplit de sa couleur et compte sa valeur | preuve (chiffres vrais seulement) | `t08-barres` |
| La fenêtre filmée | sa vraie interface (ses captures) dans une fenêtre posée sur un bureau à ses couleurs, filmée en gros plans, le curseur qui clique et l'écran qui change, une demande qui se tape | démonstration | `t08-fenetre` |
| La fin sombre | coupe sur sa nuit, le cube aux faces claires, le nom, la phrase d'appel qui s'écrit | appel, fin | `t08-logo` (sombre) |

**Pour montrer son produit** : en chapitres, chacun annoncé par une phrase tapée qui nomme la
partie, puis la fenêtre remplie de ses vraies captures et du geste de cette partie.

### Des enchaînements qui marchent

Une vidéo de page de 45 à 90 s qui annonce, puis démontre :

1. **Ouverture** (2,7 s) : `t08-logo` en clair, le logo et le nom de l'offre, tenu le temps de sa lecture.
2. **Promesse** (4 à 5 s, sa lecture) : `t08-phrase`, ce que l'offre change, en une phrase complète.
3. **Preuve** (5 s) : `t08-barres`, seulement avec des chiffres vrais pour chaque ligne.
4. **Démonstration en 2 ou 3 chapitres** : à chaque fois `t08-phrase` (le nom de la partie), puis `t08-fenetre` (7 s) remplie de ses vraies captures et du geste de cette partie.
5. **Fin** (5,4 s) : `t08-logo` en sombre, le nom et la phrase d'appel, tenue 3 s.

## 3. Les fonds et les couleurs

Ses captures et les objets connus gardent leurs vraies couleurs ; tout le reste vient de sa marque
([interdits.md](../../references/interdits.md), « La palette ») :

| Rôle | Avec la marque du client |
|---|---|
| Fond des phrases et du graphique | son clair : `var(--brand-clair)` |
| Texte, barre forte | sa nuit : `var(--brand-sombre)` (sur une marque claire, c'est son texte) |
| Barres des autres options | `var(--brand-gris-4)` |
| Noms des lignes, graduations | `var(--brand-gris-2)` |
| Séparateurs des lignes | noir à 7 % |
| Fond de la fin | sa nuit ; le logo et le nom à son clair, la phrase d'appel en `var(--brand-gris-4)` |
| Fond de bureau | l'aplat de son accent (le défaut), un dégradé entre ses gris, sa nuit, ou une vraie photo à lui ; jamais un fond peint ni un paysage |
| Fenêtre | son clair (sa nuit pour une capture sombre), trois points gris dans la barre de titre |
| Accent | rare et toujours plein : le bureau en aplat, la barre forte s'il se lit sur le clair (sinon un carré plein devant le nom), la face du cube qui porte son logo |

- La ligne forte : l'accent s'il se lit comme une barre sur le clair (3:1 au moins, sa valeur dedans en `var(--brand-contrast)`), sinon sa nuit et un carré plein de l'accent, cerné de sa nuit, devant le nom (le cas d'un accent clair). Le kit choisit seul ; elle se remplit de gauche à droite, jamais par un fondu.
- La fin reste sombre et son nom clair, même sur une marque claire.
- Sur l'aplat de l'accent, la fenêtre prend un trait fin de sa nuit au lieu d'une ombre, et le flou de bougé reste à 2 px (plus fort, il mêlerait l'accent au sombre).
- Pas de dégradé sauf entre ses gris (le bureau « gris »), pas d'ombre sauf celle de la fenêtre sur un bureau gris ou sombre ; le seul passage sombre est la fin.

## 4. La typographie

- **Phrases** : la police de titres de la marque en 400, très serrée (-0,03 em) ; sans police de marque, Inter ou Geist.
- **Graphique** : la police de texte de la marque ; le nom fort en 700 et à sa nuit ; un mot par axe (la mesure), l'unité dans la valeur (« 52/60 », « 190/h ») ; au plus 8 mots à lire sur tout le graphique.
- **Fenêtre** : ses captures à leur vraie taille ; le gros plan les rend lisibles (1,8 au plus sur une image, sinon floue). La barre de titre (15 px) est de la texture.
- **Les mots héros** (le nom à côté du cube, le nom seul dans une fenêtre sans capture) : la scène règle leur taille à environ 60 % de la largeur (80 % en 9:16).

| Texte | 1920 × 1080 | 1080 × 1920 | Casse, alignement |
|---|---|---|---|
| Phrase tapée (8 mots au plus) | 104 px sur deux lignes équilibrées, réduite seule (72 px au plus bas) si elle déborde | 112 px, sur 2 ou 3 lignes équilibrées (80 px au plus bas) | phrase, point final, centrée |
| Noms des lignes du graphique | 36 px | 36 px | phrase, à gauche |
| Graduations | 26 px, de la texture | 26 px | chiffres |
| Titres d'axes | 32 px, un mot | 32 px | phrase, à gauche sous l'axe |
| Valeur de la ligne forte | 32 px en 600, dans la barre | 32 px | à droite dans la barre |
| Nom à côté du cube | environ 60 % de la largeur avec le cube (220 px au plus), en 400 | 80 %, sous le cube (200 px au plus) | tel quel |
| Phrase d'appel de la fin | 48 px | 52 px | phrase, centrée |
| Nom dans la fenêtre sans capture | 60 % de la fenêtre (220 px au plus), en 600 | idem, fenêtre réduite | tel quel, centré |

## 5. Les mouvements signature

1. **La phrase tapée** (`t08-phrase`) : la phrase est posée entière, lettres invisibles ; elles apparaissent à leur place définitive (rien ne glisse), par petits paquets irréguliers, 25 signes par seconde ; puis la tenue, le temps de sa lecture, et la coupe nette. Dérive lente de 5,5 % sur toute la scène.
2. **Les barres comparatives** (`t08-barres`) : les axes se tracent depuis la gauche (0,45 s, `expo.out`) ; les lignes arrivent de haut en bas (0,07 s d'écart), chaque barre grandit depuis la gauche (0,6 s), toutes grises ; puis la ligne de l'offre se remplit de sa couleur (0,35 s), son nom passe en gras et sa valeur compte au bout de sa barre. La caméra se pose, puis se tient pendant les 4 s de lecture (la lumière du papier glisse derrière) : jamais de gros plan ni d'aller-retour sous le graphique.
3. **La fenêtre filmée** (`t08-fenetre`) : vue entière, puis gros plans de 0,5 s (`power3.inOut`), dont le flou de bougé vient du rendu (aucun flou ajouté à la main) ; le curseur macOS clique et la capture suivante remplace l'écran d'un coup ; une demande se tape dans le vrai champ de sa capture, montrée assez près pour faire 28 px, et aucun gros plan ne part tant qu'elle se lit (la scène les retire) ; recul. Sans capture : aucun gros plan, son nom seul dans la fenêtre, une dérive lente, 3 s.
4. **Le cube logo** (`t08-logo`) : un cube aux faces de ses couleurs (sa nuit et ses gris, claires en fin de vidéo ; la face avant à son accent pour un logo en icône carrée), son vrai logo devant ; il roule depuis trois rotations qui se calment (1 s, `expo.out`), glisse à sa place (0,7 s) pendant que le nom sort de derrière lui, puis flotte d'un quart de tour ; le nom, lui, ne bouge plus, et la lumière du papier glisse derrière. Sans logo, pas de cube : le nom monte seul de son masque.
5. **La fin sombre** : coupe nette sur sa nuit, le cube aux faces claires, le nom à son clair, la phrase d'appel qui s'écrit dessous et se tient 3 s.

## 6. Les transitions

- **La coupe nette** entre une phrase et une démonstration, sur un temps de la musique : c'est la ponctuation de ce style (et la bascule du clair au bureau de couleur fait l'événement).
- **Dans une démonstration sans texte à lire, c'est la caméra qui enchaîne** : gros plan, recul, glissé, toujours avec le flou de bougé, jamais de fondu.
- **La coupe sur le sombre** pour la fin, une seule fois.
- Pas de mosaïque, pas de flash, pas de volet, pas de fondu enchaîné.

## 7. Le produit à l'écran

- Le produit se montre **dans sa vraie fenêtre** ; la caméra va chercher chaque détail (onglets, menu, champ) au lieu de l'écrire.
- **Chez toi** : ses vraies captures (sa page, son espace de formation, son logiciel), une par écran, chaque clic montrant la suivante ; ou son interface reconstruite fidèlement d'après capture. Le kit n'en invente aucune : sans capture, la scène se retire (montre plutôt sa page), ou, pour un titre de partie, la fenêtre se montre sur son seul nom, 3 s. Les gestes (clic, frappe) sont joués sur ses captures ; une fonction que l'offre n'a pas ne s'invente pas.
- Une vraie vidéo d'écran du client peut remplacer les captures (`studio_motion.py preparer-video`, à la racine d'`index.html`, les gros plans portés sur son cadre) ; pas construit dans le kit.

## 8. Le son

- **Musique de l'original** : électronique minimale et feutrée, environ 113 battements par minute, faite de pulsations graves douces et de petits clics, sans mélodie appuyée ; elle entre franchement après le logo.
- **Chez toi** : l'ambiance « Tech minimale » des musiques de lancement (`musiques choisir --ambiance "Tech minimale"`), ou « Premium et calme » pour une offre haut de gamme ; l'entrée de batterie sur la première phrase.
- **Bruitages**, rares et doux : un clic discret à chaque clic, une frappe très basse pendant que la phrase ou la demande s'écrit, une pulsation sourde sur chaque coupe vers une phrase. Pas de whoosh sur les gros plans, pas d'impact.
- **Ambiance proposée** à la page des styles et des musiques (`musiques choisir --style 8`) : « Tech minimale » puis « Premium et calme », jamais imposée (une ambiance qu'il demande passe devant).

## 9. L'ouverture et la fin

- **Ouverture** : le cube roule et se pose, le nom sort de derrière lui, sur son clair, en 1,2 s, puis se tient sa lecture ; puis la coupe sur la première phrase. Le sujet se lit dès 1 s.
- **Fin** : coupe sur sa nuit, le cube aux faces claires, le nom à son clair, et une phrase d'appel calme qui s'écrit dessous (« Le lien est juste en dessous. »), tenue 3 s ; c'est l'écran final, il peut se tenir.

## Sur une autre offre

C'est un look : il se pose sur toute offre qui a une interface à montrer. Ce qui suivait le produit de l'original s'adapte :

- **Formation** : la fenêtre montre ses vraies captures de l'espace de formation (ses modules, une leçon, un exercice) ; les chapitres sont les parties de la méthode ; les barres comparent un résultat mesuré chez les élèves, si la page le donne.
- **Coaching** : la fenêtre montre l'outil réel de l'accompagnement (agenda des séances, espace client, messagerie, document de suivi), en captures ; les chapitres sont les étapes de l'accompagnement ; les barres, seulement avec des mesures vraies (sinon, pas de scène de barres).
- **Logiciel** : la fenêtre est sa capture ou sa reconstruction d'après capture, les gros plans vont sur ses fonctions ; les barres comparent un temps, un coût ou un score face aux autres options, avec des chiffres sourcés.
- **Sans interface à montrer** : sa page de vente en captures (le titre, la promesse, le bouton).
- **Toujours** : son clair presque nu, les phrases tapées et la coupe nette, la fenêtre filmée en gros plans sur un bureau à ses couleurs, l'accent rare et plein, le cube à son logo et la fin sur sa nuit.

## En vertical et en carré

- **9:16 (1080 × 1920)** : mets `data-width="1080" data-height="1920"` sur la racine de chaque composition et sur son hôte ; tout se règle seul (classe `t08-vertical`) : phrase en 112 px sur 2 ou 3 lignes, graphiques empilés, fenêtre réduite au milieu du bureau et gros plans plus serrés (×1,4), nom sous le cube. Le bureau à l'aplat de l'accent tient bien les bandes autour de la fenêtre ; en gris, elles font vide.
- **4:5 et carré** : pas de mise en page propre, non testé. En 4:5, la mise en page verticale s'applique (dessinée pour 1920 de haut) : réduis la phrase à 90 px. En carré, c'est l'horizontale : le graphique déborde, empile ses deux blocs (`blocs` dans le script). À vérifier image par image.

## Les compositions du kit

Dossier `compositions/`, 16:9 par défaut, chacune avec son en-tête (ce qu'elle montre, sa durée, ce qu'on remplace). Elles se servent du kit du projet (`K`) et des variables de la marque (`--brand-*`) ; les identifiants commencent par `t08-`. Chaque texte, chiffre et nom d'exemple est dans l'objet `EXEMPLE` en tête du script : sa valeur vient d'`OFFRE.json`, ou sa ligne se retire.

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace (`EXEMPLE`) |
|---|---|---|---|
| `t08-logo.html` | 2,7 s (clair) ou 5,4 s (sombre), calculée par la scène | Ouverture ou fin : le cube à son logo qui roule, le nom qui sort de derrière ; en fin, la phrase d'appel tapée, tenue 3 s | `logo` (son fichier dans `brand/`, ou "" : le nom seul), `nom`, `appel` ; hors d'EXEMPLE : `FOND`, `FACE`, `LOGO_TAILLE`, l'id (`t08-ouverture`, `t08-fin`) et la durée |
| `t08-phrase.html` | 0,06 s + 0,04 s par signe + sa lecture (4,6 s pour 7 mots et 41 signes, 5,1 s pour 8 mots) | La phrase complète tapée, centrée sur deux lignes, tenue le temps de sa lecture : le titre de chaque partie | `lignes` (une phrase de 8 mots au plus) ; la durée (calculée par la scène), un id par phrase |
| `t08-barres.html` | 5 s | La preuve : deux graphiques en barres, la ligne de l'offre qui se remplit de sa couleur et compte sa valeur, tenus 4 s | `lignes` (3 à 5 options, chiffres vrais seulement), `axes` (un mot, l'unité, l'échelle, les graduations) |
| `t08-fenetre.html` | 7 s (3 s sans capture) | La démonstration : ses vraies captures dans la fenêtre, sept gros plans, les clics qui changent d'écran, la demande tapée | `titre`, `captures`, `demande` ; hors d'EXEMPLE, à caler sur ses captures : `CLICS`, `DEMANDE` (le champ), `PLANS`, `FOND` (ou `FOND_IMAGE`), `FENETRE` |

Le montage dans `index.html` (16:9), tout sur la piste 1, bout à bout, coupes nettes :

```html
<div id="s1-hote" data-composition-id="t08-ouverture" data-composition-src="compositions/t08-ouverture.html" data-start="0" data-duration="2.7" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s2-hote" data-composition-id="t08-phrase-1" data-composition-src="compositions/t08-phrase-1.html" data-start="2.7" data-duration="4.6" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s3-hote" data-composition-id="t08-fenetre" data-composition-src="compositions/t08-fenetre.html" data-start="7.3" data-duration="7" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s4-hote" data-composition-id="t08-phrase-2" data-composition-src="compositions/t08-phrase-2.html" data-start="14.3" data-duration="5.1" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s5-hote" data-composition-id="t08-barres" data-composition-src="compositions/t08-barres.html" data-start="19.4" data-duration="5" data-track-index="1" data-width="1920" data-height="1080"></div>
<div id="s6-hote" data-composition-id="t08-fin" data-composition-src="compositions/t08-fin.html" data-start="24.4" data-duration="5.4" data-track-index="1" data-width="1920" data-height="1080"></div>
```

Chaque copie d'une composition (deux phrases, l'ouverture et la fin) change son id partout dans le fichier (racine, script, préfixe CSS) : deux scènes au même id se marcheraient dessus.
