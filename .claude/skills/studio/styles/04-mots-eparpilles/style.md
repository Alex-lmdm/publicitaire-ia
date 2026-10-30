# Template n°4 · Mots éparpillés · d'après ElevenLabs (https://x.com/ElevenLabs/status/2100262886916358361)

**Ce qu'on voit :** un avant / après en deux mondes. L'avant est un papier quadrillé où la phrase du problème arrive un mot à la fois, éparpillée sur la grille, entourée d'objets du quotidien posés sur des cases grises, coupé par des écrans tramés où un téléphone sonne, chaque bascule se faisant en carrés de pixels ; puis une phrase pivot sur un dégradé vif qui se resserre en orbe lumineux, s'allume, change de couleur et s'ouvre sur l'après : un dégradé vif où une conversation arrive en bulles de verre, avant une fin noire où un cadre au trait devient les cartes de l'offre, puis le nom.
**Souvent utile pour :** un avant / après (la corvée d'avant, la vie avec l'offre), une offre qui répond, accompagne ou automatise (un assistant, un coaching, un logiciel), une vidéo de page ou une pub.

**D'après :** « Reception » d'ElevenLabs · 16:9 · 33 s · voix off, conversation jouée et musique douce.
**Mesures de l'original** (`studio_motion.py reference`) : 1,19 événement par seconde, écart médian 0,60 s, 23 coupes franches (presque toutes dans les transitions en pixels), image figée la plus longue 5,1 s (la fin noire).
**Mesures de l'essai du kit** (les 4 scènes bout à bout, 23,9 s, marque LMDM) : `rythme` 1,33 événement par seconde, écart médian 0,70 s, aucune image figée.

> On reprend la grammaire (rythme, mises en page, typographie, mouvements, transitions, façon de
> montrer le produit), jamais le contenu : ni ses textes, ni ses objets, ni ses téléphones, ni son
> logo, ni sa voix, ni sa musique. Tout passe aux couleurs et aux polices de la marque du client.

## 1. Le rythme

- **Deux tempos.** L'avant est haché : un mot toutes les 0,3 à 0,4 s, un objet avec chaque mot, une transition en pixels toutes les 1,2 à 1,9 s (papier, écran, papier, écran, papier). L'après respire : une bulle toutes les 1,2 s, ses mots qui s'allument à 0,07 s d'écart, le fond qui tourne.
- **Le pivot est la seule pause voulue** : la phrase pivot se lit sur la couleur (1 s), puis tout se resserre en orbe ; l'orbe tient 1,5 s en vivant (il tourne, s'allume, bat).
- **L'original est calme** (1,19 événement par seconde, des textes minuscules, 5 s de noir à la fin) : le kit le resserre pour passer le contrôle `rythme` du studio (cinq transitions en pixels en 7,4 s, des points qui annoncent chaque réponse, le fond qui respire à chaque bulle, une carte de résultat, une lueur qui monte à chaque mot de l'appel).
- **Le contrôle** : sur ce template, un mot seul ou une petite bulle ne compte pas comme un événement (trop petit à l'image) ; ce sont les objets qui surgissent, les carrés de pixels, les changements de fond et les recadrages qui font le rythme. Ne retire pas l'objet qui accompagne chaque mot.

## 2. La structure

| Bloc | Rôle | Durée | Ce qui s'y passe |
|---|---|---|---|
| Papier 1 | accroche, le problème | 1,9 s | Un mot à la fois sur la grille, un objet du quotidien qui surgit avec chaque mot (`mots-objets.html`) |
| Écran 1 | le problème vécu | 1,3 s | Transition en pixels ; l'écran tramé, le téléphone qui vibre, la pastille de verre de ce qui arrive (« NOUVELLE DEMANDE ») |
| Papier 2 | le problème, encore | 1,3 s | Une deuxième phrase courte, d'autres objets |
| Écran 2 | le problème qui coûte | 1,1 s | Le téléphone sous un autre angle, une autre pastille (« APPEL MANQUÉ ») |
| Papier 3 | la chute du problème | 1,4 s | La phrase qui fait mal, entourée de tous les objets ; puis les carrés du dégradé chaud envahissent l'écran |
| Le pivot | bascule | 4 s | La phrase pivot sur le dégradé chaud (« Ça, c'était avant. »), le dégradé devient un orbe dans ses anneaux, l'orbe change de couleur et s'ouvre (`orbe-pivot.html`) |
| La conversation | solution, démonstration | 6 s | Les bulles de verre sur le dégradé de l'après ; l'offre répond, le résultat arrive et se coche (`messages-verre.html`) |
| La fin | offre et appel | 6,5 s | Le cadre au trait, la phrase d'appel ; le cadre devient les trois cartes de l'offre, qui deviennent un trait, puis le nom et le bouton (`fin-cadre.html`) |

L'original répète le motif papier / écran trois fois sur 13 s (trois besoins, trois téléphones) ; une vidéo de page de 45 à 60 s peut faire de même (une ligne de `PAPIERS` et d'`ECRANS` par besoin), puis allonger la conversation (deux échanges) avant la fin.

## 3. Les fonds et les couleurs

| Dans l'original | Son rôle | Chez le client |
|---|---|---|
| Papier blanc cassé, grille grise de 100 px, cases gris clair | le monde d'avant, calme et neutre | identique : neutre, ce n'est pas la marque (le papier `#efeee9`, l'encre `#151515`, les cases `#e3e2de`) |
| Trame bleu-vert en tirets | l'écran où le problème arrive | l'accent en tirets sur un presque noir **fixe** (`#0c0d10` teinté d'accent), avec une tache décalée vers le chaud |
| Dégradé rouge-orange vif | l'alerte, la bascule | l'accent tourné vers le rouge de `--t04-ecart` degrés (50 par défaut), en trois teintes |
| Noir et anneaux fins | le vide autour de l'orbe, la fin | un noir **fixe** (`#050505`) et des anneaux blancs à 22 %, sur toutes les marques |
| Dégradé vert, bleu, jaune, flou | l'après | l'accent entouré de ses voisines (une plus froide, une plus chaude, une presque blanche), toujours claires |
| Bulles de verre clair, texte blanc | la conversation | du verre et une encre qui suivent `var(--brand-contrast)` : texte foncé sur verre clair pour un accent clair, l'inverse pour un accent sombre |
| Cartes en dégradé vert-jaune, logo blanc | l'offre, la signature | les trois teintes de l'après ; la phrase d'appel et le nom en blanc (`--t04-texte`), le bouton en `var(--brand-accent)` |

**Sur n'importe quelle marque, claire ou sombre.** Le papier de l'avant, l'écran tramé, le noir de
l'orbe, le passage au noir et la fin restent ceux de l'original : des valeurs fixes (papier
blanc cassé, presque noir, noir), jamais `var(--brand-bg)` ni `var(--brand-text)` (sur une marque
claire, l'orbe et la fin devenaient blancs, le texte du cadre noir sur blanc : le look partait).
Le texte posé sur le noir est blanc ; la marque ne donne que les accents (la trame, les dégradés
dérivés, le bouton). Tout texte garde un contraste d'au moins 4,5:1 : sur le dégradé chaud, la
phrase pivot blanche porte une ombre douce ; les bulles et les cartes suivent `var(--brand-contrast)`.

C'est le seul template qui sort d'une seule teinte : les dégradés tournent autour de l'accent (de 50 degrés de chaque côté). Une marque qui veut rester stricte règle `--t04-ecart` à 12 dans les quatre scènes. Avec un accent jaune : trame jaune-orangé sur presque noir, alerte rouge-orange, après citron, vert tendre et orangé.

## 4. La typographie

- **Police** : celle de la marque, en graisse **400** pour les mots de l'avant, la phrase pivot et la phrase d'appel ; **600** pour le bouton. L'original utilise une linéale grotesque fine et ronde ; si la marque n'impose rien : **Inter** (400, déjà livrée pour les interfaces), ou **Inter Tight** pour les grands mots.
- **Les bulles, les pastilles et les cartes** : Inter (`assets/fonts/interfaces.css`), comme une vraie interface.
- **Casse** : celle de la phrase, en minuscules ; les pastilles en capitales, approche +4 %.
- **Placement** : les mots de l'avant ne sont jamais alignés : chacun à sa place sur la grille de 100 px, en zigzag, lus de gauche à droite ; la phrase pivot et la phrase d'appel au centre ; les bulles à gauche (l'offre) et à droite (le client).

| Élément | 1920 × 1080 | 1080 × 1920 |
|---|---|---|
| Mots de l'avant | 104 px | 96 px, deux ou trois rangées dans la bande du milieu |
| Glyphe du sujet (icône pleine) | 78 px | 72 px |
| Pastille de verre | 24 px, capitales | 26 px |
| Phrase pivot | 76 px, blanc | 64 px |
| Texte des bulles | 38 px (Inter 500) | 44 px (testé) |
| Étiquette d'une bulle | 22 px | 26 px |
| Phrase d'appel dans le cadre | 70 px | 58 px, sur deux lignes |
| Nom final | 104 px | 88 px |
| Bouton | 40 px dans une pilule de 96 px | 44 px dans une pilule de 104 px |

L'original écrit beaucoup plus petit (des bulles de 22 px, une phrase d'appel de 24 px) : le kit agrandit pour la lecture sur un téléphone et pour le contrôle du rythme.

## 5. Les mouvements signature

1. **Les mots éparpillés et leurs objets** (`mots-objets.html`) : chaque mot se tape en 0,1 à 0,2 s à sa place sur la grille, 0,35 à 0,4 s après le précédent ; avec lui, un objet surgit sur sa case grise (×0,55 à ×1 en 0,3 s, `back.out(1.8)`), puis flotte (8 px, 3 degrés, `sine.inOut`) ; le papier pousse doucement (×1,00 à ×1,03 en 2,2 s).
2. **La transition en pixels** (`mots-objets.html`, cinq fois) : 144 carrés de 120 px ; chaque carré bascule à son seuil (55 % de hasard à graine, 45 % de balayage de gauche à droite), en 0,4 s, à vitesse constante. Le plan suivant apparaît à travers les carrés (`clip-path`), sans fondu.
3. **L'écran tramé et le téléphone** (`mots-objets.html`) : des taches de couleur floues (80 px de flou) vues à travers un masque de tirets (4 × 9 px tous les 7 × 12 px), posées sur des taches plus sombres ; elles dérivent (160 et 90 px en 2 s). Le téléphone (CSS 3D, incliné de 24 degrés) monte de 80 px en 1,4 s (`power2.out`), vibre six fois (0,06 s, 3 degrés) quand la pastille de verre glisse à côté de lui (0,4 s, `expo.out`).
4. **Le pivot en orbe** (`orbe-pivot.html`) : à chaque mot de la phrase pivot, la couleur bat (un voile blanc de 16 % qui s'éteint en 0,35 s) ; le dégradé se resserre en disque (rayon 1 250 → 300 px en 0,6 s, `power3.inOut`, puis → 175 px en 0,8 s, `expo.out`), trois anneaux apparaissent (0,6 s, 0,08 s d'écart), le cœur blanc et le halo s'allument (0,5 s), l'orbe bat une fois (×1,04), passe aux couleurs de l'après (0,5 s), puis s'ouvre sur tout l'écran (0,85 s, `power3.in`) pendant que les anneaux s'éloignent.
5. **Les messages de verre** (`messages-verre.html`) : trois points qui sautent annoncent chaque réponse (0,38 s avant), la bulle se pose (26 px, flou de 8 px, 0,45 s, `expo.out`), ses mots s'allument un à un (0,07 s d'écart, depuis 22 % d'opacité), l'orbe de l'avatar bat, le dégradé respire (×1,07 → ×1 en 0,6 s), le fil remonte (0,5 s) ; la carte de résultat arrive, sa barre se remplit (0,7 s) et se coche (`back.out(2.5)`).
6. **Le cadre qui devient l'offre** (`fin-cadre.html`) : le cadre se trace (contour de 2,5 px, 0,7 s, `power2.inOut`), chaque mot de l'appel monte du flou (0,3 s) et allume un peu plus le cadre, les mots s'effacent dans le désordre (0,07 s d'écart), le cadre se resserre en carte (0,55 s, `expo.inOut`), deux cartes en sortent (±420 px, 0,55 s), les trois se rejoignent (0,4 s), s'aplatissent en un trait lumineux (0,45 s, `expo.in`), le nom sort du flou (0,6 s), le bouton saute (`back.out(2)`), le curseur le clique.

## 6. Les transitions

- **Les carrés de pixels** entre le papier et les écrans, et pour entrer dans le dégradé chaud : la transition signature, toujours sur un temps de la musique.
- **Le disque** : une couleur plein écran se resserre en orbe, l'orbe s'ouvre en couleur plein écran (l'avant devient l'après par le même objet).
- **Le passage au noir** après la conversation (0,6 s), comme l'original, pour isoler l'appel.
- **Le morphing de la fin** : le cadre devient une carte, la carte trois cartes, les cartes un trait, le trait le soulignement du nom.
- Jamais de fondu enchaîné entre deux plans chargés : les carrés de pixels font ce travail.

## 7. Le produit à l'écran

- **Le problème** se montre par les objets du quotidien (ses outils, ses papiers, son téléphone) et par l'appareil où le problème arrive, avec une pastille de verre qui dit ce qu'on rate.
- **L'offre** se montre par sa présence (l'orbe, qui devient l'avatar des bulles) et par **une vraie conversation** : son assistant qui répond, ses vrais échanges avec des clients, une vraie question de sa FAQ et sa vraie réponse ; puis **la carte du résultat** (ce que le produit rend vraiment : une page, un plan, un rendez-vous, une vidéo).
- **Le contenu de l'offre** se montre en trois cartes (ses trois parties réelles), comme les trois offres de l'original.
- Jamais une conversation inventée présentée comme vraie : sans échange réel, la scène montre une question de sa FAQ et la réponse de sa page.

## 8. Le son

- **Original** : une voix off chaleureuse dit la phrase du problème, et chaque mot apparaît au moment où il est dit ; pendant les messages, la conversation est jouée à deux voix (la voix de synthèse de l'offre et celle du client) ; une musique douce derrière, tempo estimé autour de 104 battements par minute, sans montée forte.
- **Chez le client** : texte et musique par défaut (une musique de lancement calme puis lumineuse, 95 à 110 battements par minute) ; les mots et les transitions en pixels se calent sur ses temps. Une voix off seulement à sa demande ([voix.md](../../references/voix.md)) : chaque mot de l'avant apparaît alors quand il est dit, et la conversation peut se jouer à deux voix.
- **Bruitages** : un petit tic par objet qui surgit, un grésillement bref sur chaque transition en pixels, la vibration d'un téléphone sur les écrans, une nappe qui monte pendant le pivot et un impact doux quand l'orbe s'ouvre, une bulle douce par message, un clic sur le bouton.

## 9. L'ouverture et la fin

- **Original** : il s'ouvre sur le papier vide, le premier mot tapé lettre à lettre au centre ; il finit sur le logo au-dessus d'un trait lumineux, puis le noir (5 s en tout).
- **Chez le client** : pour une vidéo de page, la première image doit déjà dire le sujet : avance les instants du premier mot et du premier objet à 0 (ils sont là dès la première image). La fin garde le nom et le trait, et ajoute le bouton que le curseur clique ; le nom et le bouton tiennent 2 s au moins, sans le long noir de l'original.

## Ce qui ne se fera pas à l'identique

- **Les objets photoréalistes** (des rendus 3D : bouteille, casque, cône, clavier, tasse) → des objets dessinés en SVG, simples et ombrés (calendrier, tasse, réveil, post-it, enveloppe, carnet), ou mieux ses photos détourées et les logos des outils de la corvée.
- **Les téléphones de bureau photoréalistes** → un smartphone en CSS 3D (le téléphone du kit), incliné.
- **La vraie trame** (des points de tailles variables selon la lumière) → des taches de couleur vues à travers des tirets réguliers, sur deux couches : la texture est là, pas la finesse du tramage.
- **L'orbe fluide** (une matière lumineuse qui coule) → des dégradés flous qui tournent dans un disque, un cœur blanc et un halo : plus simple.
- **La voix off et la conversation jouée** → texte et musique par défaut.
- **Les petits textes et les 5 s de noir** de l'original → agrandis et raccourcis pour la lecture et le contrôle du rythme.
- **Les trois familles de couleurs** (bleu, rouge, vert) → une famille qui tourne autour de l'accent.

## Sur une autre offre

Le template est un look : il se monte sur n'importe quelle offre. Ce qui suivait l'original (un standard téléphonique tenu par une IA) s'adapte :

- **Toujours** : le papier quadrillé, les mots éparpillés et leurs objets, les écrans tramés et les pastilles, les carrés de pixels, la phrase pivot, l'orbe, l'après en dégradé vif, une conversation en verre, le cadre qui devient l'offre.
- **Une formation** : les objets du quotidien de l'élève (carnet, post-it, vidéos à regarder plus tard, le réveil) ; la pastille dit ce qu'il rate (« ENCORE REPORTÉ », « PAS COMMENCÉ ») ; la conversation est une vraie question d'élève et la vraie réponse du formateur ou de l'assistant de la formation ; la carte du résultat est le module terminé ou le vrai livrable ; les trois cartes, ses trois parties.
- **Un coaching** : l'agenda, le téléphone, les messages en retard ; la pastille « NOUVEAU MESSAGE » ; la conversation, un vrai échange avec un client (avec son accord) ou un vrai témoignage en messages ; la carte, la séance réservée ; les trois cartes, ses formats d'accompagnement.
- **Un logiciel** : les logos des outils qu'il remplace sur les cases grises ; la pastille, l'alerte qu'il évite ; la conversation, son vrai assistant ou ses vraies notifications ; la carte, son vrai résultat ; les trois cartes, trois fonctions ou trois formules.

## En vertical et en carré

- **9:16 : chaque scène a sa version verticale** (`mots-objets-vertical.html`, `orbe-pivot-vertical.html`, `messages-verre-vertical.html`, `fin-cadre-vertical.html`), remise en page et jamais recadrée. Les quatre bout à bout en 1080 × 1920 font 23,9 s (essai sur une marque claire et sur LMDM : `rythme` « ok », 1,28 événement par seconde, écart médian 0,70 s, aucune image figée, raccords image pour image).
- **Le papier en 9:16** (`mots-objets-vertical.html`) : les mots à 96 px, en deux ou trois rangées dans la bande du milieu (de 780 à 1 100 px dans le kit, 600 à 1 300 au plus), 8 lettres au plus par mot ; les objets dans les bandes du haut et du bas (cases de 200 à 300 px sur la grille de 100 px : x = 40, 140…, y = 60, 160…), quelques petites cases sur les bords : l'écran est rempli de haut en bas. Les carrés de pixels restent à 120 px (9 colonnes, 16 rangées). Sur les écrans, le téléphone plus grand (500 × 1 000 px, centré, même inclinaison) et la pastille centrée au-dessus de lui.
- **L'orbe en 9:16** (`orbe-pivot-vertical.html`) : centré, un peu plus grand (disque de 320 px de rayon, orbe de 200 px), anneaux plus larges (460, 740 et 1 080 px) qui occupent la hauteur ; la phrase pivot passe à 64 px ; l'après a les mêmes taches que `messages-verre-vertical.html`.
- **La conversation en 9:16** (`messages-verre-vertical.html`) : elle remplit l'écran comme sur un téléphone : colonne de 968 px, bulles de 44 px, le fil part du milieu et remonte de 560 px en tout, le recadrage est plus doux (×1,03).
- **La fin en 9:16** (`fin-cadre-vertical.html`) : le cadre fait 960 × 700 px, la phrase d'appel à 58 px passe seule sur deux lignes, centrée ; les trois cartes (720 × 240 px) sortent au-dessus et au-dessous de la première, s'empilent en colonne, puis la colonne s'aplatit en un trait de 860 px ; le nom à 88 px au-dessus, le bouton (pilule de 104 px, texte de 44 px) dessous, vers le milieu de l'écran.
- **4:5 et 1:1** : comme le 16:9 resserré ; 9 colonnes de carrés, les objets seulement sur les côtés, deux cartes au lieu de trois en 1:1 si le texte ne tient pas.
- Les mots clés restent hors des 10 % du haut et des 20 % du bas en vertical (les commandes de l'application).

## Les compositions du kit

| Fichier | Durée | Ce qu'elle montre | Ce qu'on remplace |
|---|---|---|---|
| `compositions/mots-objets.html` | 7,4 s | L'avant : trois papiers (mots éparpillés et objets), deux écrans tramés avec le téléphone et sa pastille, reliés par cinq transitions en pixels, puis l'entrée du dégradé chaud | L'id `t04-mots`, `PAPIERS` (les mots, leur place, leurs objets et leurs instants), `ECRANS` (pastille, notification, place et angle du téléphone), le `GLYPHE` du sujet |
| `compositions/orbe-pivot.html` | 4,0 s | La bascule : la phrase pivot sur le dégradé chaud qui bat, le disque, les anneaux, l'orbe qui s'allume, change de couleur et s'ouvre sur l'après | L'id `t04-orbe`, `PIVOT` (2 à 4 mots et leurs instants), `MOMENTS` si la musique l'exige |
| `compositions/messages-verre.html` | 6,0 s | L'après : la conversation en bulles de verre sur le dégradé vif, les points qui annoncent les réponses, la carte du résultat qui se coche, puis le noir | L'id `t04-msg`, `MESSAGES` (un vrai échange), `ETIQUETTE`, `CADENCE`, `RESULTAT` (ou `null`) |
| `compositions/messages-verre-vertical.html` | 6,0 s | La même conversation en 9:16 | Comme la version 16:9 |
| `compositions/fin-cadre.html` | 6,5 s | L'offre et l'appel : le cadre et sa phrase, les trois cartes, le trait, le nom, le bouton cliqué | L'id `t04-fin`, `APPEL`, `CARTES` (les trois parties réelles de l'offre), le nom (ou son logo en `<img>`), le libellé du bouton |
| `compositions/mots-objets-vertical.html` | 7,4 s | L'avant en 9:16 : les mots dans la bande du milieu, les objets en haut et en bas, le grand téléphone et sa pastille au-dessus, les carrés de pixels en 9 × 16 | Comme la version 16:9 ; les places des mots et des objets suivent la grille verticale (en-tête du fichier) |
| `compositions/orbe-pivot-vertical.html` | 4,0 s | La bascule en 9:16 : l'orbe centré, plus grand, ses anneaux sur toute la hauteur | Comme la version 16:9 |
| `compositions/fin-cadre-vertical.html` | 6,5 s | L'offre et l'appel en 9:16 : le cadre de 960 × 700 px, la phrase sur deux lignes, les trois cartes empilées, le trait, le nom, le bouton cliqué | Comme la version 16:9 ; trois cartes |

Bout à bout dans cet ordre, elles font une vidéo de 23,9 s qui se tient seule, en 16:9 comme en 9:16 avec les versions `-vertical` (essais : `rythme` « ok », `check` sans erreur). Les raccords sont faits dans les deux formats : la fin de `mots-objets` est la première image de `orbe-pivot` (le dégradé chaud plein cadre), la fin de `orbe-pivot` celle de `messages-verre` (le dégradé de l'après, mêmes taches), et `messages-verre` finit dans le noir où commence `fin-cadre`. Un format = une seule famille de fichiers : en 9:16, monte les quatre `-vertical`, jamais une scène 16:9.
