# La revue : rien ne part sans être regardé

Les contrôles automatiques disent si le fichier est valide, pas si la vidéo est bonne. Une vidéo
n'est finie que quand **tu as regardé sa planche** et corrigé ce qui ne va pas. Applique les
portes dans l'ordre, pour chaque vidéo, et ne passe à la suivante que si la précédente est
franchie.

## Porte 1 : la composition

`npm run check` dans le dossier de la vidéo (contrôles HyperFrames). Corrige toute erreur ; un
texte net volontairement posé sur une couche floue se marque (`kit.md`, pièges). Puis
`npm run render`, puis :

```bash
python3 ../../../tools/studio_motion.py rythme exports/page.mp4
```

Il doit répondre « ok » : au moins 0,7 événement par seconde, 1,2 s au plus d'écart médian entre
deux, aucune image vraiment immobile plus de 1,5 s avant l'écran final. Il liste aussi les plus longs creux :
regarde-les, c'est souvent un raccord qui traîne ou une scène qui démarre vide. Un creux se comble
par ce que la phrase montre (un logo qui arrive, l'interface qui réagit, un compteur), jamais par
un recadrage ajouté ([rythme.md](rythme.md)).

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
- Chaque écran porte une phrase entière, qui se comprend seule ; aucun n'en porte plus de 12
  mots (hors interfaces), ni deux phrases à lire en même temps.
- Le test du spectateur froid ([ecriture.md](ecriture.md)) : à partir des seules vignettes, dans
  l'ordre, on sait ce que c'est, pour qui, le problème réglé, comment ça marche, pourquoi le
  croire, combien et quoi faire. Une réponse manque : la vidéo n'est pas finie. Ce test se refait
  à la porte 3 par un relecteur neuf, qui ne connaît pas le script.
- Les couleurs : uniquement celles de la marque, du noir, du blanc et des gris neutres ; ni brun,
  ni olive, ni orangé tirés de l'accent ; aucune image inventée (paysage, illustration). Seules les
  vraies captures du client et les logos de ses outils gardent leurs couleurs. `studio_motion.py
  palette exports/<vidéo>.mp4` liste les instants hors palette : chacun est une vraie capture, ou
  se corrige.
- Les fonds alternent (sombre, clair, couleur pleine ; avec un style du catalogue, ceux de sa fiche),
  aucun écran ne fait vide.
- Aucune image clé dont le seul sujet est une forme ou un aplat (un disque, un carré, une case
  vide) pendant plus d'une seconde, hors carte de fin et transition : la forme porte une vraie
  matière, ou elle s'en va ([style.md](style.md), « Aucune image inventée »).
- Sur une planche serrée des cinq premières secondes et des tenues de phrase, la caméra ne fait
  qu'une dérive lente : aucun recadrage sec pendant qu'on lit ([rythme.md](rythme.md), « La caméra »).
- Les raccords : la dernière case d'une scène et la première de la suivante se ressemblent.
- Boucle de section : la dernière image raccorde avec la première, sans saut.

## Porte 3 : le relecteur neuf, puis la revue critique

Tu connais le script : tu ne peux pas être le spectateur froid de ta propre vidéo (story refusée
du 06/11/2026 : « on n'a rien compris », ce que la revue de son auteur n'avait pas vu). La
compréhension se juge donc par **une IA qui n'a pas fait la vidéo**.

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
lire, et le moment où il serait parti. Compare ses trois phrases à la promesse, au public et à
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
avec une phrase de justification, sur ces neuf critères :

1. **Compréhension** : la note vient du relecteur neuf. S'il n'a pas su dire ce qui est vendu, à
   qui et quoi faire, c'est 3 au plus, quel que soit le reste.
2. **Accroche** : on comprend de quoi on parle, pour qui, et ce qu'on gagne à rester avant 3 s.
3. **Structure** : chaque bloc de la structure choisie remplit son rôle, dans l'ordre ; le
   problème vient avant le produit ; le comment est montré.
4. **Rythme** : il se passe quelque chose toutes les demi-secondes autour du texte ; chaque phrase
   reste le temps de la lire à voix haute, sans se presser. Trop rapide pour être lu, c'est 4 au plus.
5. **Montré et dit** : une phrase courte par écran, et pendant qu'on la lit, ce qu'elle dit se voit
   (des interfaces, des résultats, des preuves) ; des fonds qui alternent, rien de vide. Si on
   dirait des slides, c'est 3 au plus.
6. **Fidélité** : prix, dates, preuves et interfaces conformes à la fiche et aux sources ; chaque
   chiffre avec son contexte.
7. **Le mouvement sert** : il montre l'offre ou relie deux idées (un objet qui devient le
   suivant) ; la caméra vit sans courir ; aucun effet générique (néon, particules sans sujet).
8. **Marque** : ses couleurs et seulement elles (plus noir, blanc, gris), ses polices, une seule
   couleur d'accent ; aucune image inventée. Une teinte dérivée (un brun, un orangé tirés de son
   jaune), c'est 4 au plus.
9. **Appel à l'action** : celui du support, clair, tenu, impossible à rater.

Tout critère à 7 ou moins se corrige, puis on refait le rendu et la planche, jusqu'à 8 ou plus
partout. Liste toujours les trois plus gros défauts, même si tout est à 8. Si le client a donné
une vidéo de référence, mets côte à côte une planche de chaque (même cadence) : le niveau se juge
contre elle, pas contre la version précédente.

Avec un style du catalogue, le garde-fou ([styles/README.md](../styles/README.md)) : la planche
montre au moins trois de ses gestes signature (deux sous 15 s) dans sa grammaire (typographie,
mise en page, mouvements, transitions), aux couleurs de la marque et avec la seule vraie matière du
client. Un style ne justifie jamais une image inventée ni une couleur hors palette.

Le test du résumé, c'est la relecture à froid : si les trois phrases du relecteur neuf ne disent
pas la promesse de la fiche, la vidéo ne dit pas ce qu'elle doit dire, aussi bonnes que soient ses
notes.

## Porte 4 : le son

`python3 ../../../tools/studio_motion.py son exports/reel.mp4`, puis `mastering` si la mesure n'est pas « ok ».
Réécoute le début et la révélation : le temps fort tombe-t-il sur l'offre ?

## Porte 5 : l'export

```bash
python3 ../../../tools/studio_motion.py export ../livraison/reel.mp4   # le support se déduit du nom du fichier
```

« ok : prêt pour Instagram » ou on corrige (taille, codec, images par seconde, démarrage rapide,
durée hors bornes).

## Ce que tu dis au client de la revue

Rien du détail technique. S'il reste une limite réelle (une capture floue qu'on n'a pas pu
remplacer, une zone d'interface reconstituée), dis-la en une phrase dans le message de livraison.
