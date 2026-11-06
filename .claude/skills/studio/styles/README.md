# Les styles du catalogue

Huit styles de motion design, chacun repris d'une vraie vidéo de lancement de logiciel qui a fait
ses preuves, refait par nous (une fiche, des scènes signature déjà construites) et contrôlé en 16:9
et en 9:16, sur une marque claire comme sur une marque sombre : chaque scène a sa mise en page
verticale (un fichier `-vertical.html`, ou une scène qui se remet en page seule). Le client les voit
en vidéo sur la page des styles et des musiques, à chaque vidéo (étape 4 du skill), et dans sa
formation (module « Styles »). Il les demande par leur numéro, leur nom ou la marque d'origine :
« dans le style 3 », « le style Verre sombre », « comme celle de Polymarket » ; « template » veut
dire la même chose (ses premières vidéos les appelaient ainsi).

**Un style est une inspiration, pas un plan ni un décor.** Il donne une façon de présenter les
choses : sa typographie, ses mises en page, ses mouvements, ses transitions, ses motifs (un cadre
de sélection, des repères de maquette, une phrase tapée, une fenêtre inclinée) et ses gestes
signature. Il ne donne ni ses images ni ses couleurs : ce qu'on voit vient du client (sa matière
réelle) et se peint aux seules couleurs de sa marque. La structure, elle, vient toujours de la
vidéo du client : son but, l'idée qu'il a choisie, son script validé, ce qu'il veut montrer. On ne
refait pas l'original séquence par séquence : on adapte tout.
Un style se fait donc sur n'importe quelle offre (une formation, un coaching, un logiciel, un
template) et pour n'importe quel but (vendre, une pub, une nouveauté, un lancement). Ce qui suivait
le sujet de l'original (une commande de trading, des connecteurs d'entreprise) s'adapte à son
offre : section « Sur une autre offre » de chaque fiche.

> On reprend la grammaire de ces vidéos, jamais leur contenu : ni leurs textes, ni leurs logos, ni
> leurs images, ni leur produit, ni leur musique, ni leurs couleurs. Une image de l'original
> (paysage, photo, illustration, objet) devient la vraie matière du client qui sert le script, prise
> en descendant l'échelle de [style.md](../references/style.md) (« Aucune image inventée ») : une
> capture, son interface reconstruite, un vrai chiffre mis en scène, les vrais logos de ses outils,
> puis seulement ses mots. On ne la redessine jamais (story refusée du 06/11/2026 : des couchers de
> soleil et une planète redessinés, bruns et orangés, « c'est vraiment moche ») et on ne la remplace
> pas par une forme seule (essais du 06/11/2026 : des disques et des carrés sans sujet).

| N° | Style | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
|---|---|---|---|---|---|
| 1 | Cartes pixels | grille claire, cartes d'interface du flou au net, blocs de pixels qui couvrent et découvrent, grand chiffre | Firecrawl | passer du problème au résultat | `01-cartes-pixels` |
| 2 | Titres géants | titres qui débordent du cadre sur la couleur de la marque, spécimen tapé sur grille, carte qui s'ouvre sur sa vraie capture et mosaïque de sa matière, disque qui porte son logo et pose le nom, grille d'une case par élément de l'offre | Cyera (studio Motionimo) | une vidéo de lancement | `02-titres-geants` |
| 3 | Verre sombre | interface en verre sombre inclinée en 3D, curseur qui règle l'offre, ses vraies captures en verre autour des phrases, sur la nuit de la marque et son accent en aplats | Polymarket | l'offre et son prix | `03-verre-sombre` |
| 4 | Mots éparpillés | l'avant : une phrase mot à mot sur papier quadrillé, ses cases portant sa vraie matière (captures, chiffres, logos), des transitions en pixels ; l'après : sa couleur qui se resserre en disque autour de la phrase pivot puis porte son logo, une vraie conversation en bulles | ElevenLabs | un avant / après | `04-mots-eparpilles` |
| 5 | Interrupteurs en cascade | papier clair à sa marque, interrupteurs qui s'allument en cascade, trait à main levée qui entoure, coches en vague, phrases calmes | ClaudeDevs | annoncer une nouveauté | `05-interrupteurs-creme` |
| 6 | Nuée d'encre | page claire, cercle au pinceau qui se défait en nuée de points, planches de ses vrais mots ou images, « bientôt » | Kimi | un teaser avant l'ouverture | `06-nuee-d-encre` |
| 7 | Phrase tapée | phrases tapées derrière un gros curseur, sa vraie matière et ses outils éparpillés puis en orbite autour de l'offre | Zaro | lancer un logiciel ou une formation | `07-phrase-tapee` |
| 8 | Fenêtre posée | phrases complètes tapées sur un fond clair, barres comparatives, l'outil dans une fenêtre posée sur sa couleur | Cursor | prouver avec des chiffres | `08-fenetre-peinte` |

Les styles 5 et 8 s'appelaient « Interrupteurs crème » et « Fenêtre peinte » jusqu'à la 0.9.0 (des
noms de couleur et d'image, devenus faux quand les styles ont pris les couleurs de la marque) : un
client qui emploie l'ancien nom veut le même style.

Chaque style a son aperçu dans `assets/styles/` (`<dossier>.mp4` et `<dossier>.jpg` : quelques
secondes de ses gestes, à la marque LMDM), que la page des styles et des musiques montre.

## Appliquer un style

1. **Le bon style.** Il le choisit sur la page des styles et des musiques, ou il l'a donné
   d'emblée : prends sa grammaire, quel que soit le sujet de l'original. **Ne déconseille jamais un
   style parce que son offre ne ressemble pas à l'original** : c'est une façon de présenter. Ton conseil, en une phrase,
   part de ce que la vidéo va montrer (son interface, un avant / après, des chiffres, une annonce,
   un teaser) et de sa marque (claire ou sombre) ; la colonne « Souvent utile pour » n'est qu'un
   indice. Il hésite (« lequel tu me conseilles ? ») : demande-lui ce qu'il aime voir (fond clair ou
   sombre, interface en 3D, typo géante, phrase tapée, fenêtres), puis propose 2 ou 3 styles,
   numéro et nom, chacun avec sa raison en une ligne.
2. **La structure vient de sa vidéo**, jamais de l'original : celle de son but
   ([structures.md](../references/structures.md)), l'idée qu'il a choisie, son script validé. Le
   style ne change ni la structure, ni les idées, ni le script : il ne raccourcit aucune phrase et
   n'accélère aucune tenue pour suivre le tempo de l'original. `OFFRE.json` reste la seule source des faits : les
   chiffres, les prix et les noms d'exemple des scènes du kit se remplacent tous, ou la scène se
   retire. Jamais de faux chiffre parce que la scène en montrait un.
3. **Les gestes du style** (section 2 de sa fiche) : chaque scène du plan prend le geste qui sert
   son rôle (une accroche, un problème, une démonstration, une preuve, un appel). Une scène sans
   geste qui convienne (son interface, son produit, ce que l'original n'avait pas) se construit
   dans la grammaire du style : sa typographie, ses mises en page, ses mouvements, ses
   transitions, sa façon de montrer le produit (sections 3 à 7 de la fiche). Les scènes du kit sont
   des démonstrations de ces gestes, pas des scènes à remplir : on en reprend le mouvement (le code
   d'une entrée, d'un cadre de sélection, d'un recul de caméra), jamais le décor. Note dans
   `PLAN.md`, pour chaque scène, le geste repris ou « construite dans le style ».
   Exemple (vidéo du haut de la page de Publicitaire IA, style 7, 03/11/2026) : la structure vient
   du texte de la voix off ; trois gestes du kit repris (la phrase et ses objets, le désordre réduit
   en points, l'orbite et le point d'encre) ; deux scènes construites pour son cas, dans le style
   (le dossier déposé sur Claude, la conversation dans Claude).
4. **Le garde-fou** : chaque vidéo garde au moins trois gestes signature de son style (deux sous
   15 s), sinon on ne le reconnaît plus. Un geste signature est un mouvement, une mise en page ou
   un motif ; jamais une image (un paysage, une sphère, une gravure ne sont pas des gestes).
5. **La fabrication** : lis la fiche en entier, puis écris les scènes du plan à partir du script :
   une phrase, ce qu'elle montre (la vraie matière du client), et le geste du style qui la
   présente. Tu peux copier dans `compositions/` du projet une scène du kit pour en garder le
   mouvement, puis tu en retires tout ce qui n'est pas au client (ses textes, ses chiffres, ses
   images d'exemple). Les phrases gardent la tenue de leur lecture (`lecture`), quel que soit le
   tempo de l'original ; pendant qu'on les lit, la vie vient de ce qu'elles montrent, et la caméra
   ne fait qu'une dérive lente ([rythme.md](../references/rythme.md), « La caméra »). Un `rythme`
   trop bas se corrige par un événement de contenu, jamais par un recadrage ajouté. Un logo absent
   de sa marque se remplace par son nom, jamais par un autre logo.
   **Les couleurs : celles de sa marque, rien d'autre** ([style.md](../references/style.md), « La
   palette »). Les fonds de nuit du style prennent `var(--brand-sombre)`, ses fonds clairs
   `var(--brand-clair)` (ou un gris très clair), ses fonds pleins `var(--brand-accent)` ; les gris
   viennent de `var(--brand-gris-1)` à `var(--brand-gris-4)`. Le texte posé sur la nuit est
   `var(--brand-clair)`, sur l'accent `var(--brand-contrast)`. Aucune couleur dérivée de l'accent
   (`oklch(from var(--brand-accent) …)`, `color-mix` avec l'accent, un dégradé vers lui) et aucun
   accent en transparence sur du sombre : avec un jaune, cela fait du brun, de l'olive ou de
   l'orangé (pub d'essai du 03/11/2026, story refusée du 06/11/2026). Tout texte garde un contraste
   d'au moins 4,5:1 avec son fond.
   **Les images de l'original** (paysages, photos, illustrations, sphères, gravures, fonds peints)
   deviennent sa vraie matière, en descendant l'échelle : une capture de sa page, de son produit ou
   d'un résultat, son interface reconstruite, un vrai chiffre mis en scène, les vrais logos de ses
   outils, puis seulement ses mots. Une forme du kit (disque, aplat, case, cadre) porte cette
   matière ou sert de transition, jamais de sujet. On ne les redessine jamais.
   **Une pub ne dessine pas de bouton** ([structures.md](../references/structures.md), publicité) :
   la fin du style garde son geste et finit sur « Découvre-le » et une flèche vers le bas.
6. **Les autres formats** : section « En vertical et en carré » de la fiche. Une mise en page,
   jamais un recadrage. En 9:16, prends la version `-vertical.html` d'une scène quand le kit en a
   une (kits 2, 4 et 5) ; sinon passe la racine de la scène à 1080 × 1920, elle se remet en page
   seule. Ces versions sont calées pour un Reel : en pub, vérifie sur la planche la zone sûre de la
   pub (tout texte entre y 269 et 1 248) et remonte ce qui en sort.
7. **La revue**, comme toute vidéo ([revue.md](../references/revue.md)), garde-fou compris.
8. **Il le garde** (« garde ce style pour mes prochaines vidéos ») : ajoute `style N` à ses
   `preferences` (`studio.config.json` ; un ancien `template N` vaut `style N`). La page ne le
   redemande plus : rappelle-le en une ligne, il peut toujours en demander un autre.
