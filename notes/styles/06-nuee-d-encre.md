# Notes de maintenance · Style n°6 · Nuée d'encre

Fichier de maintenance : l'IA ne le lit pas pendant une vidéo. La fiche
(`.claude/skills/studio/styles/06-nuee-d-encre/style.md`) dit la règle au présent ; ce qui l'a fait
naître (l'original scène par scène, les essais mesurés, les adaptations datées) est rangé ici.

## Ce qui sortait de la fiche lors du ménage du 07/11/2026

### Les mesures

- **Mesures de l'original** (`studio_motion.py reference`) : 1,88 événement par seconde, écart médian
  0,40 s, aucune image figée ; une coupe détectée (le noir final), plus la coupe franche de la page
  pleine vers la page vide, que l'outil ne compte pas (deux images claires).
- **Essai du kit refait le 06/11/2026** (les 4 scènes bout à bout, 18,1 s, marque LMDM, sans choc
  de caméra, les lignes de fin tenues le temps de leur lecture) : en 16:9, 1,23 événement par
  seconde, écart médian 0,60 s ; en 9:16, 1,30 événement par seconde, écart médian 0,50 s ; aucune
  image figée, `rythme` et `palette` « ok » dans les deux formats.
- **9:16 essayé en 1080 × 1920, marque LMDM, 06/11/2026.**

### La citation propre au style

> On reprend la grammaire de la vidéo, jamais son contenu : ni ses idéogrammes, ni ses gravures,
> ni sa photo de lune, ni son papier, ni son logo, ni son texte, ni sa musique. Le pinceau trace un
> geste universel (un cercle, un point) ; les planches montrent ses vraies images ou ses vrais mots,
> jamais un dessin inventé pour l'occasion.

L'index (`README.md`, « Appliquer un style ») dit la règle générale ; la fiche garde « La règle du
style » (la nuée écrit toujours une vraie matière).

### L'original, pour mémoire

Scène par scène, un exemple et pas un plan à suivre (c'est un teaser : il n'a pas de bloc « problème ») :

| Rôle | Temps (original) | Ce qui s'y passe |
|---|---|---|
| Accroche | 0 à 3 s | Un pinceau trace des caractères à l'encre sèche, en gros, sur la page. Le tracé se « numérise » (colonnes de petits signes) et commence à se défaire. |
| Tension | 3 à 9 s | Le tracé devient une nuée de points qui prend des formes l'une après l'autre, toujours par trois : traits, filets, colonnes en treillis, piliers de signes, arches en pixels, trois boules, trois sphères hérissées, une seule sphère, une lune. |
| Crescendo | 9 à 12 s | Autour de la lune, une rafale de gravures (instruments, machines, plantes, architecture) remplit toute la page. La musique se retient. |
| Révélation | 12 à 13 s | Coupe franche sur la page vide : le nom de la version change de forme tous les quarts de seconde. |
| Offre et appel | 13 à 15 s | Deux lignes posées au centre (le produit, puis « bientôt »), le logotype, coupe au noir. |

### Les couleurs de l'original (ancienne colonne « Original » de la section 3)

| Rôle | Original |
|---|---|
| La page | papier gris chaud, grain fin et fibres |
| L'encre | noir |
| La couleur | aucune |
| Les gravures | planches au trait |
| Le noir final | noir |

La fiche disait aussi « `var(--brand-clair)` (LMDM : blanc) ».

### Ce qui ne se fera pas à l'identique (texte de la fiche jusqu'au 07/11/2026)

- **Les images de l'original ne se refont pas.** La lune photographique et les sphères deviennent
  trois points pleins puis l'initiale de l'offre en points ; les gravures anciennes, ses vraies
  images (ses croquis, ses captures, en noir et blanc) ou ses vrais mots composés en planches.
- **Le papier** (gris chaud, grain, fibres) : un aplat de sa couleur claire.
- Les idéogrammes au pinceau : un cercle et un point (un geste universel, réglable par ses points).
- Les piliers de signes et les arches tramées : trois disques en gros pixels.
- Le logotype « K2, K3, KIII » : l'initiale de l'offre avec trois barres puis trois points.
- Les légendes de l'original : des légendes génériques en français (à remplacer).
- Le noir et blanc pur : la page et l'encre sont la plus claire et la plus sombre de ses couleurs,
  un seul point prend son accent.
- La durée : 17,9 s au lieu de 15 s (les lignes de fin tenues le temps de leur lecture).

Depuis le 07/11/2026 : les trois points pleins, les trois disques en pixels, les trois traits et
les trois colonnes en treillis ont disparu (des formes sans sujet) ; les idéogrammes deviennent le
cercle autour des mots de l'accroche ; les formes par trois deviennent les trois mots de l'offre ;
la lune devient l'initiale en points ; le logotype, l'initiale avec ses trois points de suspension
(sans barres) ; la durée du kit, 20,3 s.

### L'ancienne règle de rythme (retirée)

La fiche disait : le contrôle `rythme` compte les gros changements de lumière, des points fins sur
une page claire bougent peu ; « le kit le fait passer en grossissant et en densifiant la nuée
(3 400 points de 3 à 8 px), en changeant de forme toutes les 0,75 s, en serrant la nuée d'un coup
en trois points pleins ». Elle notait aussi que le choc de caméra au point posé et le sursaut à la
numérisation avaient été retirés du kit le 06/11/2026. Retirée : un `rythme` bas se corrige par un
événement de contenu (`references/mouvement.md`, « Le rythme »), jamais par une nuée décorative.

## Le ménage du 07/11/2026

Un audit a montré que la fiche et ses scènes contredisaient la loi du produit : une nuée de 3 400
points sans sujet (le nombre était réglé pour faire passer `rythme`), des formes par trois (traits,
colonnes en treillis, disques en pixels, trois disques pleins) sujets de leur plan, des disques
pleins dans la rafale, des textes à 17 px, un sigle de 150 px et un nom de 104 px perdus au milieu
de la page, un recul de caméra de 14 % sous l'initiale.

**La fiche** (21 165 → 14 578 caractères) : « Ce qu'on voit » et une « règle du style » (la nuée
écrit toujours une vraie matière, son nombre de points vient du sujet) ; section 1 sans la règle de
rythme par la nuée ; section 2 sans l'ouverture commune ni l'original (ici), une ligne « L'initiale
en points » ajoutée ; section 3 sans la colonne de l'original, lien vers `image.md` ; tailles de la
section 4 alignées sur les scènes (planches 28 px au moins, sigle, lignes et nom à 74 % de la
largeur) ; sections 5 à 9 refaites sur les nouvelles scènes ; « Ce qui ne se fera pas à
l'identique » et les mesures ici ; compositions du kit : durées et champs d'`EXEMPLE`.

**Les scènes** (chacune : un objet `EXEMPLE` en tête, « À remplacer : l'objet EXEMPLE » dans
l'en-tête, aucune couleur en dur hors `#000` des canevas cachés) :

- `coup-de-pinceau.html` (4,5 → 5,4 s) : le cercle porte l'accroche (`EXEMPLE.accroche`, un mot par
  ligne) qui s'imprime pendant qu'il se ferme ; le point du pinceau devient le point final de la
  phrase ; la numérisation traverse le cercle et les mots ; la nuée naît de l'encre réellement
  posée (une place par case de 9 px du cercle, 4 à 9 px des mots) au lieu de 3 400 points tirés au
  hasard ; légendes dans `EXEMPLE.legendes`, cadre en `data-layout-ignore`, sans « LANCEMENT EN
  COURS » ; aucune mesure de la page pendant le rendu (lint).
- `nuee-de-particules.html` (5 → 5,5 s, calculée) : traits, colonnes, disques en pixels et trois
  disques pleins retirés ; la bande écrit les trois mots de l'offre (`EXEMPLE.trois`) un à un, chacun
  posé d'un coup en encre pleine (texte de la page, lisible par `check`), le reste de la bande
  descend à la ligne suivante ; le pinceau souligne le mot clé pendant la lecture (un événement de
  la phrase : sans lui, `rythme` voyait 1,5 s d'image figée) ; les mots passent en gros pixels puis
  s'envolent en l'initiale (`EXEMPLE.nom`), les points en trop s'éteignant ; temps calculés d'après
  le nombre de mots.
- `planches-en-rafale.html` (2,8 s) : disques pleins retirés ; planche à 28 px au moins (un mot trop
  long pour sa pilule ou son cadre passe seul sur un filet) ; la rafale est une texture
  (`data-layout-ignore`), l'initiale la seule chose à lire, au-dessus du calque des planches ; recul
  de caméra 14 % → dérive de 6 % (sine.inOut) ; textes dans `EXEMPLE` ; même tirage d'initiale que
  la scène 2.
- `bientot.html` (5,6 → 6,6 s, calculée) : le sigle est une seule lettre qui change d'état (plus de
  `line_unread` par état), à la taille de l'initiale en points, centrée jusqu'à ses points ; ses
  trois barres retirées (des formes sans sujet) ; lignes et nom à 74 % de la largeur (76 px et
  104 px auparavant) ; logo à 60 % de la largeur et 40 % de la hauteur au plus ; caméra en dérive
  de 3 % sous les lignes puis sous le nom ; le nom tenu 2,5 s (écran final).

**Vérifié** (banc `videos/Banc styles 06 · 2026-11-07/`, marque sombre du banc, Poppins) : les
quatre scènes bout à bout en 16:9 et en 9:16 (20,3 s), `hyperframes check` sans erreur ni
avertissement de lecture, de taille, de contraste ou de mise en page (reste `film_silent`, le banc
n'a pas de son) ; rendu 16:9 : `rythme` 1,38 événement par seconde, écart médian 0,50 s, aucune
image figée ; `palette` « ok ».

**Reste hors de ce ménage** : l'aperçu `assets/styles/06-nuee-d-encre.mp4|.jpg` (5 s) montre
l'ancienne scène 1 : un cercle vide, le point à l'accent posé seul au centre, puis une nuée qui ne
porte rien, avec des légendes « LMDM. PUBLICITAIRE IA » ; il est à retourner avec ces scènes.
