# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. La revue
vient après la passe du directeur ([ambition.md](ambition.md)) : elle vérifie que la version
travaillée tient les interdits et qu'un inconnu la comprend. Applique les portes dans l'ordre, pour
chaque vidéo, et ne passe à la suivante que si la précédente est franchie.

## Porte 1 : la composition et le rendu

`npm run check` dans le projet de la vidéo (le dossier qui contient `index.html`). Zéro erreur ; un texte net volontairement posé sur
une couche floue se marque (`kit.md`, pièges). Ses avertissements de métier (`craft`) se corrigent
tous sur un texte qu'on doit lire : `text_below_floor` (texte sous 28 px : agrandis, ou approche la
caméra d'une interface), `line_unread` (parti avant d'être lu : allonge la tenue), `first_frame_empty`
(la première image est l'affiche : elle montre déjà le sujet). Puis `npm run render`, puis, depuis
le projet :

```bash
python3 ../../../tools/studio_motion.py rythme exports/page.mp4
python3 ../../../tools/studio_motion.py cadre exports/page.mp4
python3 ../../../tools/studio_motion.py palette exports/page.mp4
```

`rythme` doit répondre « ok » (au moins 0,7 événement par seconde, 1,2 s au plus d'écart médian,
aucune image vraiment immobile plus de 1,5 s avant l'écran final, des plans de durées variées ;
de 0,6 à 1,5 s, un avis : rien à faire si des mots s'y lisent, sinon un événement de contenu) ; un
creux se comble par ce que le plan montre, jamais par un recadrage ajouté
([metier.md](metier.md), « Le rythme »). `cadre` doit répondre « ok » : chaque instant presque vide
se corrige en approchant la caméra, en agrandissant le sujet ou en lui donnant un monde
([metier.md](metier.md), « Le cadre »). `palette` connaît les couleurs du kit et des logos du
projet, et liste les autres instants : chacun est une vraie capture, l'interface d'une plateforme
ou un objet connu construit pour la vidéo, ou se corrige ([interdits.md](interdits.md), « La
palette »).

**Seul le MP4 rendu fait foi.** `check` et `snapshot` téléchargent une police qui manque, le rendu
non : une police sans fichier passe en police système seulement dans le MP4. Le journal du rendu
dit aussi si le flou de bougé s'est appliqué (`[motion-blur] on`, et pourquoi en mode allégé :
[kit.md](kit.md), pièges). Les images de `snapshot` et un extrait `--start/--end` n'ont jamais ce
flou : ils servent à juger une place ou une collision, la traîne se juge sur la planche du MP4 entier.

## Porte 2 : la planche

```bash
python3 ../../../tools/studio_motion.py planche exports/reel.mp4 --temps 0.3,1.8,4.3,8.3,12.3,17.8
python3 ../../../tools/studio_motion.py planche exports/reel.mp4 --pas 0.5
```

La première prend les repères de ton plan, chacun plus 0,3 s (le moment où l'élément est posé), et
dessine la zone sûre du support (et la bande du sticker d'une story avec lien) ; la seconde, une
image toutes les demi-secondes, sert à juger le rythme et les passages : chaque case doit différer
de la précédente. Ouvre-les et regarde-les vraiment :

- **les interdits, ligne à ligne** ([interdits.md](interdits.md)) : chaque texte correspond à une clé
  de `OFFRE.json` ou c'est du ton ; aucune image inventée ; le test du diaporama sur chaque image
  clé ; la palette ; au plus 8 mots à lire par image et un mot par seconde sur la vidéo
  (`studio_motion.py lecture "<mots du plan 1>" … --duree <s> --final`) ; tout texte important dans le cadre
  vert, rien dans le rouge, lisible à la taille de la vignette ; l'accroche lisible sur la première
  vignette ; un texte posé qui ne bouge plus, et pas de recadrage sous une lecture ;
- la première image déjà forte (vidéo de page : c'est elle qu'on voit si la lecture automatique est
  bloquée), la dernière propre (l'appel à l'action entier) ; une boucle de section qui raccorde sa
  dernière image à la première ;
- **les collisions pendant les animations**, que le `check` ordinaire et le relecteur ne voient
  pas : `npx hyperframes check --at-transitions --json` (une minute pour 35 s) regarde au début et à
  la fin de chaque mouvement et liste les instants où un texte est recouvert ou déborde. Regarde
  chacun (`npx hyperframes snapshot --at <t>`) : un objet qui passe sur un mot déjà lu, un volet,
  c'est voulu ; un texte qu'on lit et qui touche un autre texte, passe sous un objet ou sort du
  cadre, même pendant deux images, se corrige. Puis chaque passage de près (`snapshot --range
  <début>,<fin> --frames 8`) ;
- aucune image clé dont le seul sujet est une forme ou un aplat plus d'une seconde, hors fin et
  passage ; aucun sujet perdu en petit dans un grand vide ; en vertical, une mise en page recomposée ;
- le test du spectateur froid ([ecriture.md](ecriture.md)) : à partir des seules vignettes, dans
  l'ordre, on sait ce que c'est, pour qui, le problème réglé, comment ça marche, pourquoi le croire,
  combien et quoi faire. Ce test se refait à la porte 3 par un relecteur neuf.

Chaque défaut trouvé s'écrit dans « Interdits de cette vidéo » et se corrige.

## Porte 3 : le relecteur neuf, puis la revue critique

Tu connais le script : tu ne peux pas être le spectateur froid de ta propre vidéo. La compréhension
se juge donc par **une IA qui n'a pas fait la vidéo**.

**1. La relecture à froid.**

```bash
python3 ../../../tools/studio_motion.py relecture exports/story-ouverture.mp4
```

L'outil tire du MP4 rendu des planches (une image toutes les 0,5 s, toutes les secondes au-delà de
75 s, sans zones ni repères) dans un
dossier au nom neutre, et écrit la consigne du relecteur (`CONSIGNE.md`). Lance un **sous-agent**
(Claude Code : l'outil Agent ; Codex : un sous-agent, qu'il lance quand on le lui demande) avec
pour seule consigne le contenu de `CONSIGNE.md` et ces seules planches : ni le script, ni
`PLAN.md`, ni `OFFRE.json`, ni rien de la conversation. Il répond en trois phrases (ce qui est
vendu, à qui, ce qu'on doit faire maintenant), puis ce qu'il a dû deviner, ce qu'il n'a pas pu
lire, le moment où il serait parti, et si la vidéo montre ou fait lire (le passage le plus
« diapositive »). Ce passage-là se refait : il montre ce qu'il écrit. Compare ses trois phrases à la
promesse, au public et à l'appel à l'action de `OFFRE.json` (l'outil les affiche) : **tout écart est
un P0**, à corriger avant le reste. Sans sous-agent possible, fais la relecture toi-même, à partir
des seules planches, avant de relire le script, et dis-le dans ta revue.

**2. Le relevé.** `relecture exports/<vidéo>.mp4 --releve` ajoute à la consigne le script validé
(section « Script » de `PLAN.md`), ce que la vidéo doit faire dire et les mesures du rendu
(`rythme`, `cadre`, `calage`, `emergence`), données comme des faits. Le relecteur (le même, ou un
neuf) rend une ligne par défaut, située sur la grille de 6 × 6 cases de ses planches : « t = 4,5 s ·
planche 1, image 10, cases B2 à D3 · problème · changement exact · P0, P1 ou P2 ».

- **P0** casse la lecture, la compréhension ou un interdit : une phrase partie avant d'être lue, un
  texte illisible, l'offre jamais dite, un chiffre sans son contexte, une couleur hors de la marque,
  une forme seule à la place d'un sujet, un recadrage sec pendant une lecture.
- **P1** affaiblit le film : un creux, un passage qui saute, une preuve peu lisible, une image qui
  ne montre pas ce que dit la phrase.
- **P2** polit : un alignement, une taille, un détail.

Les P0 et les P1 se corrigent, puis on refait le rendu et les portes 1 à 3 (relecture à froid
comprise, avec un relecteur neuf : celui d'avant connaît désormais la vidéo). Les P2 se corrigent
s'il reste du temps. **La revue s'arrête** quand un relecteur neuf dit ce que dit la fiche (ce qui
est vendu, à qui, quoi faire), ne relève plus de P0, et que les contrôles qui bloquent répondent
« ok » : `check` (zéro erreur), `export` et `livrer`. Un refus de `rythme`, `cadre`, `palette`,
`calage` ou `emergence` est un P1 : il se corrige, ou s'écrit dans `PLAN.md` avec sa raison (un
faux tempo, une vraie capture hors palette). Chaque relecteur trouvera toujours un P1 neuf : deux
tours de correction suffisent, la revue critique comprise. Le reste, le client le demandera en
retouche.

**3. Les interdits de cette vidéo.** Chaque P0 et chaque P1 corrigé s'écrit en une ligne dans la
section « Interdits de cette vidéo » de `PLAN.md`, comme une règle qui vaudrait pour n'importe
quelle image, pas avec les objets d'aujourd'hui : une seconde passe les remplacera (« l'accroche
reste 3,5 s, sans recadrage », « aucun prix dans la bande du sticker »). Relis-la avant chaque retouche : une correction
ne doit pas en défaire une autre. Un plan créé avant la 0.9.0 n'a pas cette section : ajoute-la à
la fin.

**4. La revue critique**, une fois le son passé (porte 4 : le critère 10 en dépend). Note de 1 à
10, avec une phrase de justification :

1. **Compréhension** : ta note, d'après les trois phrases du relecteur neuf (lui ne note pas) ; s'il
   n'a pas su dire ce qui est vendu, à qui et quoi faire, 3 au plus.
2. **Accroche** : avant 3 s, on sait de quoi on parle, pour qui, et ce qu'on gagne à rester.
3. **Structure** : chaque bloc remplit son rôle, dans l'ordre ; le problème avant le produit ; le
   comment montré.
4. **Lecture** : chaque groupe de mots reste le temps de le lire à voix haute ; trop rapide, 4 au
   plus.
5. **Montré, pas lu** : chaque plan montre ce qu'il dit ; des slides, des sous-titres, 3 au plus ;
   une suite de photos de sa page, 4 au plus.
6. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources.
7. **Marque et couleurs vraies** : sa palette, ses polices, et les objets connus dans leurs vraies
   couleurs ; une teinte dérivée de l'accent, 4 au plus ; une vidéo toute en trois couleurs, 6 au
   plus.
8. **Appel à l'action** : celui du support, clair, tenu, impossible à rater.
9. **Le niveau** : la grille de la passe du directeur ([ambition.md](ambition.md)) ; une vidéo
   propre mais plate (coupes et fondus, interfaces à plat, deux effets de texte), 5 au plus.
10. **Le son** : la musique porte, les bruitages vont avec elle, aucun ne lasse (porte 4).

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout, dans les deux tours de correction : un critère encore à 7 après eux se dit au client, en
une phrase, dans le message de livraison. Liste toujours les trois plus gros défauts, même si tout
est à 8. Si le client a donné
une vidéo de référence, mets côte à côte une planche de chaque (même cadence) : le niveau se juge
contre elle. Avec un style 1 à 8, la planche montre au moins trois de ses gestes signature (deux
sous 15 s) ([styles/README.md](../styles/README.md), point 4).

## Porte 4 : le son

```bash
python3 ../../../tools/studio_motion.py calage exports/reel.mp4
python3 ../../../tools/studio_motion.py emergence .
python3 ../../../tools/studio_motion.py son exports/reel.mp4
```

`emergence` doit répondre « ok » : sans voix, la musique s'entend bien et les bruitages dépassent
son fond de 4 à 10 dB ; avec une voix, aucun bruitage ne passe au-dessus d'elle ([son.md](son.md),
« L'équilibre entre la musique, les bruitages et la voix »). Un refus est un P1.

`calage` doit répondre « ok » : le montage suit la bande-son ([son.md](son.md), « Construire
l'image sur la bande-son »). Sans voix, chaque scène part sur un temps de la musique (une scène « à
0,12 s du temps » : fais finir celle d'avant sur ce temps) ; avec une voix, chaque scène part avec
la phrase qui la porte, aucune ne change au milieu d'un mot, et la batterie n'entre jamais sous un
mot (une respiration : `voix respiration`) ; dans les deux cas, un geste fort se voit sur l'entrée
franche de la batterie (le nom qui claque, un flash, une coupe). Chaque refus est un P1, sauf le
faux tempo d'une basse syncopée ([son.md](son.md), « Le caler ») : mesure la phase avant de bouger
une scène. `son` mesure le niveau, puis `mastering`, toujours : le fichier livré est la version
masterisée ([son.md](son.md), « Le niveau final »). Réécoute le
début et la révélation : le temps fort tombe-t-il sur l'offre ? La pose des sons (`sons`) ne doit
laisser aucun « bruitage qui lasse » ([son.md](son.md), « Les bruitages »).

## Porte 5 : l'export

D'abord la couverture, qui écrit la vidéo livrée dans `../livraison/` ([livraison.md](livraison.md),
« La couverture et l'affiche »), puis l'export vérifie ce fichier-là :

```bash
python3 ../../../tools/studio_motion.py couverture exports/reel-master.mp4 3.5
python3 ../../../tools/studio_motion.py export ../livraison/reel.mp4   # le support se déduit du nom du fichier
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
