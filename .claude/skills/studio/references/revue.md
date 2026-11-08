# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. Une vidéo
n'est finie que quand **tu as regardé sa planche** et corrigé ce qui ne va pas. Applique les
portes dans l'ordre, pour chaque vidéo, et ne passe à la suivante que si la précédente est
franchie.

## Porte 1 : la composition

`npm run check` dans le dossier de la vidéo. Zéro erreur ; un texte net volontairement posé sur
une couche floue se marque (`kit.md`, pièges). Ses avertissements de métier (`craft`) se corrigent
tous sur un texte qu'on doit lire : `text_below_floor` (texte sous 28 px : agrandis, ou approche la
caméra d'une interface), `line_unread` (parti avant d'être lu : allonge la tenue), `first_frame_empty`
(la première image est l'affiche : elle montre déjà le sujet). Puis `npm run render`, puis, depuis
le projet :

```bash
python3 ../../../tools/studio_motion.py rythme exports/page.mp4
python3 ../../../tools/studio_motion.py cadre exports/page.mp4
```

`rythme` doit répondre « ok » : au moins 0,7 événement par seconde, 1,2 s au plus d'écart médian,
aucune image vraiment immobile plus de 1,5 s avant l'écran final, et des plans de durées variées.
Il liste les plus longs creux : souvent un raccord qui traîne ou une scène qui démarre vide. Un
creux se comble par ce que le plan montre, jamais par un recadrage ajouté
([mouvement.md](mouvement.md)). `cadre` doit répondre « ok » : il relève les instants où l'image
est presque vide (un petit sujet au milieu d'un grand fond) ; chacun se corrige en approchant la
caméra, en agrandissant le sujet ou en lui donnant un monde ([image.md](image.md), « Le cadre »).

**Seul le MP4 rendu fait foi.** `check` et `snapshot` téléchargent une police qui manque, le rendu
non : une police sans fichier passe en Impact ou en police système seulement dans le MP4. Regarde
donc la planche du fichier rendu, jamais seulement les captures de `check`.

## Porte 2 : la planche

```bash
python3 ../../../tools/studio_motion.py planche exports/reel.mp4 \
  --temps 0.3,1.8,4.3,8.3,12.3,17.8
python3 ../../../tools/studio_motion.py planche exports/story-ouverture.mp4
```

Prends les repères de ton plan, chacun plus 0,3 s (le moment où l'élément est posé) ; la
dernière image est toujours ajoutée. Pour juger le rythme, fais aussi une planche serrée, une
image toutes les 0,5 s (`ffmpeg -i exports/page.mp4 -vf "fps=2,scale=320:-2,tile=6x4" planche-%02d.jpg`),
et regarde-la comme on regarde la vidéo de référence : chaque case doit différer de la
précédente. L'outil lit le support et le format dans le projet et dessine
la bonne zone (et la bande du sticker pour une story avec lien). Ouvre la planche et regarde-la
vraiment :

- Tout texte important est **dans le cadre vert** ; rien dans le rouge (sticker).
- Chaque texte se lit à la taille de la vignette (360 px de large, la taille d'un aperçu).
- L'accroche est lisible sur la première vignette.
- La dernière image est propre : rien à moitié sorti, l'appel à l'action entier.
- Chaque texte de la planche correspond à une clé de `OFFRE.json`, ou c'est du ton.
- Vidéo de page : la première image est déjà forte et dit le sujet (c'est elle qu'on voit si la
  lecture automatique est bloquée).
- **Le test des sous-titres** : chaque plan se comprend par ce qu'il montre ET ses quelques mots ;
  aucune image ne porte plus de 8 mots à lire (hors interface, étiquettes et logos) ; sur toute la
  vidéo, un mot à lire par seconde au plus (`studio_motion.py lecture "<mots du plan 1>" … --duree
  <s>`) ; et la mise en page des sous-titres (une phrase en haut, une petite interface dessous)
  ne revient pas d'un plan à l'autre.
- **Les défauts interdits** ([image.md](image.md)) : passe la liste ligne à ligne sur la planche.
  Chaque défaut présent (de la liste ou non) s'écrit dans « Interdits de cette vidéo » et se
  corrige.
- Le test du spectateur froid ([ecriture.md](ecriture.md)) : à partir des seules vignettes, dans
  l'ordre, on sait ce que c'est, pour qui, le problème réglé, comment ça marche, pourquoi le
  croire, combien et quoi faire. Une réponse manque : la vidéo n'est pas finie. Ce test se refait
  à la porte 3 par un relecteur neuf, qui ne connaît pas le script.
- Les couleurs : celles de la marque, du noir, du blanc et des gris neutres ; ni brun, ni olive,
  ni orangé tirés de l'accent ; aucune image inventée (paysage, illustration) ; les objets connus
  dans leurs vraies couleurs ([image.md](image.md), « Les objets connus »).
  `studio_motion.py palette exports/<vidéo>.mp4` connaît les couleurs du kit et des logos du
  projet, et liste les autres instants hors palette : chacun est une vraie capture, l'interface
  d'une plateforme ou un objet connu construit pour la vidéo, ou se corrige.
- Le fond change quand le film change de temps, avec une cause visible (avec un style du catalogue,
  les fonds de sa fiche) ; aucun écran ne fait vide.
- Aucune image clé dont le seul sujet est une forme ou un aplat (un disque, un carré, une case
  vide) pendant plus d'une seconde, hors carte de fin et transition : la forme porte une vraie
  matière, ou elle s'en va ([image.md](image.md), « La vraie matière »).
- Le cadre : sur chaque image clé, le sujet occupe au moins 40 % de la largeur ou de la hauteur ; rien
  n'est tout petit au milieu d'un grand fond ; en vertical, la mise en page est recomposée, pas
  rétrécie.
- Sur une planche serrée des cinq premières secondes et des tenues de phrase, un texte posé ne
  bouge plus et la caméra ne recadre pas pendant qu'on lit ([mouvement.md](mouvement.md), « La
  caméra »).
- Les raccords : la dernière case d'une scène et la première de la suivante se ressemblent.
- Boucle de section : la dernière image raccorde avec la première, sans saut.

## Porte 3 : le relecteur neuf, puis la revue critique

Tu connais le script : tu ne peux pas être le spectateur froid de ta propre vidéo (son auteur ne
voit pas ce qu'un inconnu ne comprend pas). La compréhension se juge donc par **une IA qui n'a pas
fait la vidéo**.

**1. La relecture à froid.**

```bash
python3 ../../../tools/studio_motion.py relecture exports/story-ouverture.mp4
```

L'outil tire du MP4 rendu des planches (une image toutes les 0,5 s, sans zones ni repères) dans un
dossier au nom neutre, et écrit la consigne du relecteur (`CONSIGNE.md`). Lance un **sous-agent**
(Claude Code : l'outil Agent ; Codex : un sous-agent, qu'il lance quand on le lui demande) avec
pour seule consigne le contenu de `CONSIGNE.md` et ces seules planches : ni le script, ni
`PLAN.md`, ni `OFFRE.json`, ni rien de la conversation. Il répond en trois phrases (ce qui est
vendu, à qui, ce qu'on doit faire maintenant), puis ce qu'il a dû deviner, ce qu'il n'a pas pu
lire, le moment où il serait parti, et si la vidéo montre ou fait lire (le passage le plus
« diapositive »). Ce passage-là se refait : il montre ce qu'il écrit. Compare ses trois phrases à la promesse, au public et à
l'appel à l'action de `OFFRE.json` (l'outil les affiche) : **tout écart est un P0**, à corriger
avant le reste. Sans sous-agent possible (un assistant qui n'en lance pas), fais la relecture
toi-même, à partir des seules planches, avant de relire le script, et dis-le dans ta revue.

**2. Le relevé.** `relecture exports/<vidéo>.mp4 --releve` ajoute à la consigne le script validé
(section « Script » de `PLAN.md`) et ce que la vidéo doit faire dire. Le relecteur (le même, ou un
neuf) rend une ligne par défaut : « t = 4,5 s · où · problème · changement exact · P0, P1 ou P2 ».

- **P0** casse la lecture ou la compréhension : une phrase partie avant d'être lue, un texte
  illisible, l'offre jamais dite, un chiffre sans son contexte, une couleur hors de la marque,
  une forme seule à la place d'un sujet, un recadrage sec pendant une lecture.
- **P1** affaiblit le film : un creux, un raccord qui saute, une preuve peu lisible, une image qui
  ne montre pas ce que dit la phrase.
- **P2** polit : un alignement, une taille, un détail.

Les P0 et les P1 se corrigent, puis on refait le rendu et les portes 1 à 3 (relecture à froid
comprise, avec un relecteur neuf : celui d'avant connaît désormais la vidéo). Les P2 se corrigent
s'il reste du temps.

**3. Les interdits de cette vidéo.** Chaque P0 et chaque P1 corrigé s'écrit en une ligne dans la
section « Interdits de cette vidéo » de `PLAN.md` (« l'accroche reste 3,5 s, sans recadrage », « le
67 € ne passe jamais dans la bande du sticker »). Relis-la avant chaque retouche : une correction
ne doit pas en défaire une autre. Un plan créé avant la 0.9.0 n'a pas cette section : ajoute-la à
la fin.

**4. La revue critique.** Change de rôle : tu es un directeur artistique exigeant. Note de 1 à 10,
avec une phrase de justification, sur ces dix critères :

1. **Compréhension** : la note vient du relecteur neuf. S'il n'a pas su dire ce qui est vendu, à
   qui et quoi faire, c'est 3 au plus, quel que soit le reste.
2. **Accroche** : on comprend de quoi on parle, pour qui, et ce qu'on gagne à rester avant 3 s.
3. **Structure** : chaque bloc de la structure choisie remplit son rôle, dans l'ordre ; le
   problème vient avant le produit ; le comment est montré.
4. **Rythme** : il se passe quelque chose toutes les demi-secondes autour des mots ; chaque groupe
   de mots reste le temps de le lire à voix haute, sans se presser. Trop rapide pour être lu, c'est
   4 au plus.
5. **Montré, pas lu** : chaque plan montre ce qu'il dit (des interfaces qui réagissent, un schéma
   qui se trace, de vraies vidéos), et ses mots, peu nombreux et très grands, jouent ce qu'ils
   disent ; des fonds qui alternent, rien de vide. Si on dirait des slides ou des sous-titres
   (plus d'un mot à lire par seconde), c'est 3 au plus.
6. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources ; chaque
   chiffre avec son contexte.
7. **Le mouvement sert** : il montre l'offre ou relie deux idées (un objet qui devient le
   suivant) ; la caméra vit sans courir ; aucun effet générique (néon, particules sans sujet). Un
   plan en 3D qui décore sans rien montrer de plus que le plat, c'est 5 au plus.
8. **Marque et couleurs vraies** : ses couleurs pour le film (plus noir, blanc, gris), ses polices,
   une seule couleur d'accent ; aucune image inventée ; et les objets connus dans leurs vraies
   couleurs, autant que [image.md](image.md) le demande (« Les objets connus »). Une teinte dérivée
   (un brun, un orangé tirés de son accent), c'est 4 au plus. Une vidéo toute en trois couleurs, ou
   un dossier, un fichier, un téléphone génériques à la couleur de la marque alors que l'objet connu
   existe, c'est 6 au plus.
9. **Appel à l'action** : celui du support, clair, tenu, impossible à rater.
10. **Le niveau** ([image.md](image.md), « Le cadre ») : chaque plan a son moment signature, de la
    profondeur (perspective, flou de distance, ombres), un sujet qui remplit le cadre, une caméra
    qui voyage entre les plans, des courbes et des entrées variées ([mouvement.md](mouvement.md)).
    Des petits éléments centrés sur un grand fond vide, ou des plans à plat posés les uns après les
    autres, c'est 5 au plus : propre ne suffit pas, le seuil est « on la regarde deux fois ».

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout. Liste toujours les trois plus gros défauts, même si tout est à 8. Si le client a donné
une vidéo de référence, mets côte à côte une planche de chaque (même cadence) : le niveau se juge
contre elle, pas contre la version précédente.

Avec un style du catalogue, le garde-fou ([styles/README.md](../styles/README.md)) : la planche
montre au moins trois de ses gestes signature (deux sous 15 s) dans sa grammaire (typographie,
mise en page, mouvements, transitions), aux couleurs de la marque (et à celles des objets connus)
et avec la seule vraie matière du client. Un style ne justifie jamais une image inventée ni une couleur hors palette.

Le test du résumé, c'est la relecture à froid : si les trois phrases du relecteur neuf ne disent
pas la promesse de la fiche, la vidéo ne dit pas ce qu'elle doit dire, aussi bonnes que soient ses
notes.

## Porte 4 : le son

```bash
python3 ../../../tools/studio_motion.py calage exports/reel.mp4
python3 ../../../tools/studio_motion.py son exports/reel.mp4
```

`calage` doit répondre « ok » : le montage suit la bande-son ([son.md](son.md), « Construire
l'image sur la bande-son »). Sans voix, chaque scène part sur un temps de la musique (une scène « à
0,12 s du temps » : fais finir celle d'avant sur ce temps) ; avec une voix, chaque scène part avec
la phrase qui la porte, aucune ne change au milieu d'un mot, et la batterie n'entre jamais sous un
mot (une respiration : `voix respiration`) ; dans les deux cas, un geste fort se voit sur l'entrée
franche de la batterie (le nom qui claque, un flash, une coupe). Chaque refus est
un P1 : il se corrige avant la livraison. `son` mesure le niveau, puis `mastering` si la mesure
n'est pas « ok ».
Réécoute le début et la révélation : le temps fort tombe-t-il sur l'offre ? La pose des sons
(`sons`) ne doit laisser aucun « bruitage qui lasse » (le même son deux fois de suite, trois fois
en 6 s, ou un son du pack qui cache un cliquet) : [son.md](son.md), « Les bruitages ».

## Porte 5 : l'export

```bash
python3 ../../../tools/studio_motion.py export ../livraison/reel.mp4   # le support se déduit du nom du fichier
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
