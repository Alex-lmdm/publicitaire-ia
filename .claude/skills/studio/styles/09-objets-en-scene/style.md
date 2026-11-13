# Style n°9 · Objets en scène · d'après Ditch (https://www.instagram.com/p/DfEWcKnSGCa/)

Une pub qui avance à toute vitesse sans jamais faire enfantin : un gros mot par phrase, qui fait ce qu'il dit ;
des objets connus de son public, dessinés en code et **sans visage**, qui agissent (un terminal qui imprime
un ticket, une balance qui bascule, un réveil qui sonne) ; ses interfaces reconstruites qui vivent ; un
coup de zoom sur chaque temps fort ; et **un seul passage où un objet a un visage** : celui qui incarne le
problème. L'accroche est la plus dense de la vidéo : il s'y passe quelque chose toutes les 0,2 à 0,3 s.

Le dosage fait le style. Des visages partout, des couleurs vives dans chaque plan : c'est un dessin animé
pour enfants. Un visage, au bon endroit, sur un fond tenu et une palette serrée : c'est une pub
professionnelle avec une touche drôle.

## 1. Le rythme

- **L'accroche** (3 à 6 s) : un événement toutes les 0,2 à 0,3 s. Une carte arrive en zoomant, ses lignes
  s'ajoutent, un chiffre grimpe, puis le mot fort explose au centre, des pastilles se mettent en orbite,
  une étiquette claque.
- **Le reste** : une phrase par plan, une action toutes les 1 à 2 s. Chaque geste, chaque coupe et chaque
  son part sur un mot dit (avec une voix, `assets/mots.js`), sinon sur un temps de la musique.
- Les gros mots tiennent le temps de leur lecture (`studio_motion.py lecture`) et ne bougent plus pendant
  qu'on les lit : la vie vient des objets autour d'eux et des coups de zoom.
- 20 à 45 s. Rien ne s'arrête plus de 0,6 s sans un mot à lire (`rythme`).

## 2. Les gestes signature et leur place

| Geste | Ce qu'on voit | Il sert à | Dans le kit |
|---|---|---|---|
| L'accroche qui monte | sur l'aplat de son accent, la carte de son interface arrive en zoomant ; ses lignes s'ajoutent et se cochent pendant qu'un chiffre grimpe ; la carte tombe, la phrase vient au centre en très gros, son dernier mot surligné ; des pastilles en orbite ; une étiquette claque de travers | l'accroche, la promesse montrée dès la première seconde | `t9-accroche` |
| Le gros mot qui joue | à chaque phrase, un à trois mots en très gros qui font ce qu'ils disent : ils claquent, se font surligner, rayer, étirer, rapetissent (« presque rien ») ou grandissent, s'assemblent, se tapent | chaque phrase | `t9-accroche`, `t9-probleme`, `t9-ticket` |
| Le coup de zoom | sur un mot fort, tout le cadre grossit de 3 à 5 % en 0,06 s puis revient en 0,3 s, d'un côté puis de l'autre | les temps forts, deux à cinq par scène | `t9-accroche` |
| Le problème a un visage | l'objet qui incarne le problème (une étiquette de prix, un réveil, un pixel qui travaille) a des yeux, des sourcils, une bouche : il sue, grimace, montre les dents ; en face, la solution est un objet sans visage, à l'accent | le problème, une seule fois dans la vidéo | `t9-probleme` |
| L'objet sans visage qui agit | un objet connu, dessiné en code, fait la phrase : un terminal avale une pièce et imprime, une balance bascule, des dés retombent sur six, un réveil fait six tours | la démonstration, la preuve, le coût | `t9-ticket` |
| Le rappel | un objet revient en réponse : le ticket sans fin du problème, puis le ticket minuscule de la solution, au même endroit | la solution, la chute | `t9-ticket` |
| Le passage par l'objet | la caméra plonge dans un objet ou un nom ; la scène suivante s'ouvre au plus près de l'objet qui le prolonge (le clap qui vrille devient le réveil qui finit la vrille, le nom de l'étiquette devient l'onglet d'une image) | quelques raccords, pas tous | `t9-probleme` |

### Des enchaînements qui marchent

- **Pub ou Reel avec voix** : l'accroche qui monte, le problème a un visage (5 à 8 s), puis des objets sans
  visage et ses interfaces, le rappel, l'appel sur l'aplat de l'accent.
- **Une nouveauté** : l'accroche qui monte sur la carte de la nouveauté, l'objet sans visage qui agit pour
  chaque chose qu'elle fait, l'appel.
- **Un avant / après** : le problème a un visage (l'avant), le passage par l'objet, le rappel (l'après).

## 3. Les fonds et les couleurs

- **Un seul fond** pour toute la vidéo : son clair (`var(--brand-clair)`). L'aplat de son accent
  (`var(--brand-accent)`) seulement à l'ouverture, à l'appel et en éclat d'un temps fort ; le texte posé
  dessus prend `var(--brand-contrast)`.
- **Un seul accent** : sa couleur, pour la solution (son objet, son mot surligné, son étiquette).
- **Une seule couleur de mauvaise nouvelle** : son jeton négatif (`var(--brand-negative)`) pour ce qui
  coûte, ce qui gêne, une rature, un total qui fait mal. Rien d'autre en rouge.
- Son sombre (`var(--brand-sombre)`) pour les gros mots et les objets neutres ; ses gris
  (`var(--brand-gris-1)` à `4`) pour les lignes d'interface.
- Les objets se peignent par rôle : `"accent"`, `"sombre"`, `"clair"`, `"alerte"` (`objets-en-scene.css`
  les peint avec ces jetons, en aplats : aucune teinte tirée de l'accent). Jamais une couleur de plus
  par scène, jamais un objet arc-en-ciel. Seules les vraies interfaces tierces et les vrais logos gardent
  leurs couleurs.

## 4. La typographie

- Deux polices pour toute la vidéo : sa police de titres (`var(--brand-font-display)`) pour les gros mots,
  en capitales, serrés ; sa police de texte pour les interfaces.
- Les gros mots font 140 à 270 px en 16:9 (120 à 200 px en 9:16), centrés dans la bande libre au-dessus du
  sujet, jamais sur lui. Un mot surligné par phrase au plus (un bloc de l'accent, ou du clair sur
  l'accent).
- Les gros mots portent le script : pas de sous-titres de chaque mot en plus. Les chiffres en très gros,
  comme des objets.

## 5. Les mouvements signature

- **Trois règles pour chaque objet** : il prend son élan avant de partir (il s'écrase avant de sauter,
  recule avant de foncer : `back.out`, `P.ecrase`) ; les départs sont décalés de 0,05 à 0,1 s, jamais tout
  en même temps ; le flou de bougé suit le mouvement (`data-motion-blur` en mode capture sur `#root`).
  Jamais une ligne droite à vitesse constante (`mouvement`).
- Les mots : `K.claque`, `K.surligner`, `K.barre`, `K.etire`, `K.assembler`, `K.taper`, `K.permuter`
  (`references/kit.md`). Les objets : `P.tombe`, `P.ecrase`, `P.saute`, `P.secoue`, `P.pop` ; les coups de
  zoom : `P.coups(tl, racine, [[t, force, origine], …])`.
- La caméra bouge dans chaque plan : elle s'approche doucement, recule pour révéler, file d'un objet au
  suivant (`P.vue`, `P.cam`).
- **Le piège du flou de bougé** : un élément qui bouge se peint par-dessus ce qui est fixe. Un mot
  surligné ou un mot posé sur un objet en mouvement prend `data-motion-blur="off"` ; sous un éclat de
  couleur, la caméra ne bouge qu'une fois l'éclat refermé.

## 6. Les transitions

- **Par l'objet, à quelques raccords** : la caméra plonge sur un objet qui vrille, la scène suivante
  s'ouvre au plus près de l'objet suivant qui finit la vrille ; elle plonge dans un nom, la suivante
  s'ouvre sur le même nom, un éclat de sa couleur se referme en cercle sur lui ; une pièce sort d'une
  scène et tombe dans la suivante.
- Ailleurs, un filé dans le sens de la caméra, ou une coupe franche sur un temps fort de la musique. Au
  plus un tiers de coupes franches (`rythme`).

## 7. Le produit à l'écran

Ses interfaces reconstruites d'après capture, et vivantes : une carte dont les lignes s'ajoutent, un
éditeur qui tape, un aperçu qui réagit à chaque ligne, un compteur qui grimpe. Ses vrais logos et ceux de
ses outils, toujours sans visage. Jamais un écran que sa page ne montre pas.

## 8. Le son

Un bruitage sur chaque mot qui claque, chaque chiffre, chaque mouvement (une centaine pour 45 s) :
un clic sec sur un mot, un souffle sur un zoom, un choc sur un objet qui tombe, un tic sur un chiffre ; la
voix toujours au-dessus (`emergence`). Jamais deux fois le même bruitage de suite (`sons` signale ceux
qui lassent). La musique : « Court et percutant » ou « Lancement énergique » (`references/son.md`).
Le style marche avec une voix off (les gestes calés sur ses mots) comme avec le texte et la musique seuls.

## 9. L'ouverture et la fin

- **L'ouverture** montre la promesse ou la douleur dès la première image, par une interface qui monte
  (une carte, un chiffre), jamais par son logo. La phrase de l'accroche porte `data-accroche` et se lit
  dès 0,5 s.
- **La fin** : un rebondissement (ce qui change tout dans ce qu'on vient de voir), puis la clé sur l'aplat
  de l'accent : « Commente MOT », le lien en bio ou le bouton de la pub.

## Sur une autre offre

Le visage va toujours au problème que son client connaît : l'heure perdue (un réveil épuisé), l'argent qui
part (une étiquette qui mord, un ticket sans fin), la tâche qui revient (une pile qui grandit). Les objets
sans visage sont ceux de son public : un agenda, une tasse, un ticket, une balance, un terminal, un dé, une
pièce. Pour une formation, l'interface est son espace de cours ou son programme ; pour un coaching, ses
messages et son agenda ; pour un logiciel, son produit. Un chiffre affiché vient de la fiche
(`OFFRE.json`) ; sinon le compteur montre un avancement (de 0 à 100 %) ou se retire.

## En vertical et en carré

Les scènes du kit se remettent en page seules (`K.cadre`) : en 9:16, la phrase géante passe sur deux
lignes, la carte prend la largeur, la balance se resserre. Les gros mots restent dans la bande libre du
haut, hors de la zone de l'interface de la plateforme (`zones`). Une mise en page, jamais un recadrage.

## Les compositions du kit

**D'abord, la bibliothèque des objets** : copie `kit/objets-en-scene.js` et `kit/objets-en-scene.css` de
ce dossier dans `assets/` du projet, puis charge-les dans `index.html`, juste après le kit :
`<link rel="stylesheet" href="assets/objets-en-scene.css">` et
`<script src="assets/objets-en-scene.js"></script>`. Elle donne les objets (`P.clap`, `P.reveil`,
`P.etiquette`, `P.balance`, `P.de`, `P.piece`, `P.tele`, `P.loupe`, `P.tasse`, `P.pellicule`, `P.ticket`,
`P.triangle`, `P.rond`, `P.bloc`), leurs gestes, `P.coups`, la caméra (`P.vue`, `P.cam`) et le visage
(`P.visage`). Un objet sans visage : `P.sansVisage(objet)`. Chaque objet prend une couleur par rôle :
`couleur: "accent" | "sombre" | "clair" | "alerte"`.

Chaque scène est une sous-composition 16:9 prête à copier dans `compositions/` puis à monter dans
`index.html` (sa durée en `data-duration`, bout à bout sur la piste 1). Ses textes et ses noms d'exemple
sont dans l'objet `EXEMPLE` en tête du script (chaque champ y est décrit) ; les couleurs ne viennent que
de `var(--brand-*)`.

| Fichier | Durée (objet `EXEMPLE`) | Ce qu'elle montre | Ce qu'on remplace dans `EXEMPLE` |
|---|---|---|---|
| `compositions/t9-accroche.html` | 5,4 s | la carte qui zoome, ses lignes cochées, le chiffre qui grimpe, la phrase géante, l'orbite, l'étiquette | `phrase` (2 à 4 mots, le dernier surligné), `nom` (le fichier de la carte), `titre`, `lignes` (2 à 4), `compteur` (`de`, `a`, `suffixe` : un vrai chiffre de la fiche, ou un avancement), `etiquette` (`""` la retire) |
| `compositions/t9-probleme.html` | 4,8 s | la balance, la petite étiquette de la solution, la grosse du problème qui s'écrase et montre les dents, la phrase mot à mot | `phrase` (3 à 5 mots), `surligne` (le rang du mot surligné, `-1` : aucun), `solution` et `probleme` (un mot court chacun), `plonger` (la caméra plonge dans le nom du problème à la fin) |
| `compositions/t9-ticket.html` | 4,2 s | le terminal sans visage, la pièce, l'écran qui tape, le ticket minuscule ou sans fin, la phrase | `phrase` (2 à 4 mots), `ecran` (un signe ou un mot court), `symbole` (sa devise), `long` (`true` : le ticket sans fin, ce qui coûte ; `false` : le ticket minuscule, presque rien) |

Chaque scène calcule sa durée (`D` dans le script) : reporte-la dans `data-duration`, ici et sur l'hôte.
Pour le rappel, monte `t9-ticket` deux fois : `long: true` sur le problème, `long: false` sur la solution
(change le préfixe `t9t` partout dans la seconde copie). Identifiants préfixés `t9a`, `t9p`, `t9t`.
