# Les styles du catalogue

**Le style 0, « Sur mesure », est le style maison** : celui que portent le kit et les scènes prêtes,
qui ne copie aucune vidéo et prend une forme à lui pour chaque offre. C'est le conseil par défaut
(point 1 ci-dessous).

Puis huit styles de motion design, chacun repris d'une vraie vidéo de lancement de logiciel qui a fait
ses preuves, refait par nous (une fiche, des scènes signature déjà construites) et contrôlé en 16:9
et en 9:16, sur une marque claire comme sur une marque sombre : chaque scène a sa mise en page
verticale (un fichier `-vertical.html`, ou une scène qui se remet en page seule). Le client les voit
en vidéo sur la page des styles et des musiques, à chaque vidéo (étape 4 du skill), et dans sa
formation (module « Styles »). Il les demande par leur numéro, leur nom ou la marque d'origine :
« dans le style 3 », « le style Verre sombre », « comme celle de Polymarket » ; « template » veut
dire la même chose ; « le style maison » ou « sur mesure » veulent le style 0. « Interrupteurs
crème » et « Fenêtre peinte » sont d'anciens noms des styles 5 et 8 : un client qui les emploie veut
le même style.

**Un style est une inspiration, pas un plan ni un décor.** Il donne une façon de présenter les
choses : sa typographie, ses mises en page, ses mouvements, ses transitions, ses motifs (un cadre
de sélection, des repères de maquette, une phrase tapée, une fenêtre inclinée) et ses gestes
signature. Il ne donne ni ses images ni ses couleurs : ce qu'on voit vient du client (sa matière
réelle) et se peint aux couleurs de sa marque (point 6). La structure, elle, vient toujours de la
vidéo du client : son but, l'idée qu'il a choisie, son script validé, ce qu'il veut montrer. On ne
refait pas l'original séquence par séquence : on adapte tout. Un style se fait donc sur n'importe
quelle offre (une formation, un coaching, un logiciel, un template) et pour n'importe quel but
(vendre, une pub, une nouveauté, un lancement) ; ce qui suivait le sujet de l'original s'adapte à
son offre (section « Sur une autre offre » de chaque fiche).

> On reprend la grammaire de ces vidéos, jamais leur contenu : ni leurs textes, ni leurs logos, ni
> leurs images, ni leur produit, ni leur musique, ni leurs couleurs. Une image de l'original
> (paysage, photo, illustration, objet) devient la vraie matière du client qui sert le script
> ([image.md](../references/image.md), « La vraie matière ») : une capture, son interface
> reconstruite, un vrai chiffre mis en scène, les vrais logos de ses outils, puis seulement ses
> mots. On ne la redessine jamais, et on ne la remplace pas par une forme seule (un disque, un
> carré, une nuée sans sujet).

| N° | Style | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
|---|---|---|---|---|---|
| 0 | Sur mesure | sa vraie matière en grand et en perspective que la caméra parcourt, des mots énormes qui claquent, se barrent, se surlignent, le point de sa couleur qui relie tout, l'objet de son offre qui porte son nom | le style maison, d'après les studios de motion design | tout, et d'abord sa première vidéo | `00-sur-mesure` |
| 1 | Cartes pixels | grille claire, cartes d'interface du flou au net, blocs de pixels qui couvrent et découvrent, grand chiffre | Firecrawl | passer du problème au résultat | `01-cartes-pixels` |
| 2 | Titres géants | titres géants qui débordent du cadre à leur entrée, sur la couleur de la marque, spécimen tapé sur grille, carte qui s'ouvre sur sa vraie capture et mosaïque de sa matière, disque qui porte son logo et pose le nom, grille d'une case par élément de l'offre | Cyera (studio Motionimo) | une vidéo de lancement | `02-titres-geants` |
| 3 | Verre sombre | interface en verre sombre inclinée en 3D, curseur qui règle l'offre, ses vraies captures en verre autour des phrases, sur la nuit de la marque et son accent en aplats | Polymarket | l'offre et son prix | `03-verre-sombre` |
| 4 | Mots éparpillés | l'avant : une phrase mot à mot sur papier quadrillé, ses cases portant sa vraie matière (captures, chiffres, logos), des transitions en pixels ; l'après : sa couleur qui se resserre en disque autour de la phrase pivot puis porte son logo, une vraie conversation en bulles | ElevenLabs | un avant / après | `04-mots-eparpilles` |
| 5 | Interrupteurs en cascade | papier clair à sa marque, interrupteurs qui s'allument en cascade, trait à main levée qui entoure, coches en vague, phrases calmes | ClaudeDevs | annoncer une nouveauté | `05-interrupteurs-creme` |
| 6 | Nuée d'encre | page claire, cercle au pinceau autour de ses mots qui se défait en points, ses mots écrits en points puis son initiale, planches de ses vrais mots ou images, « bientôt » | Kimi | un teaser avant l'ouverture | `06-nuee-d-encre` |
| 7 | Phrase tapée | phrases tapées derrière un gros curseur, sa vraie matière et ses outils éparpillés puis en orbite autour de l'offre | Zaro | lancer un logiciel ou une formation | `07-phrase-tapee` |
| 8 | Fenêtre posée | phrases complètes tapées sur un fond clair, barres comparatives, l'outil dans une fenêtre posée sur sa couleur | Cursor | prouver avec des chiffres | `08-fenetre-peinte` |

Chaque style a son aperçu dans `assets/styles/` (`<dossier>.mp4` et `<dossier>.jpg` : quelques
secondes de ses gestes, sur une marque d'essai), que la page des styles et des musiques montre.

## Appliquer un style

1. **Le bon style.** Il le choisit sur la page des styles et des musiques, ou il l'a donné
   d'emblée : prends sa grammaire, quel que soit le sujet de l'original. **Ne déconseille jamais un
   style parce que son offre ne ressemble pas à l'original** : c'est une façon de présenter. **Ton
   conseil** (marqué sur la page, et pris s'il répond « choisis ») : le style 0 pour sa première
   vidéo (aucune livraison dans les autres dossiers de `videos/`), et par défaut ensuite ; un des
   huit quand sa vidéo appelle nettement sa grammaire (des chiffres à comparer : 8 ; un teaser : 6 ;
   son offre et son prix sur une marque sombre : 3 ; la colonne « Souvent utile pour » donne
   l'indice) ou qu'il a aimé ce look. Dis-le en une phrase, avec ce que la vidéo va montrer. Il
   hésite (« lequel tu me conseilles ? ») : demande-lui ce qu'il aime voir (fond clair ou sombre,
   interface en 3D, typo géante, phrase tapée, fenêtres), puis propose 2 ou 3 styles, numéro et
   nom, chacun avec sa raison en une ligne. Il décrit ce qu'il veut, ou répond « aucun » : sa fiche
   du style 0, « Quand il décrit un autre style ».
2. **La structure vient de sa vidéo**, jamais de l'original : celle de son but
   ([structures.md](../references/structures.md)), l'idée qu'il a choisie, son script validé. Le
   style ne change ni la structure, ni les idées, ni le script : il ne raccourcit aucune phrase et
   n'accélère aucune tenue pour suivre le tempo de l'original. `OFFRE.json` reste la seule source
   des faits. Jamais de faux chiffre parce que la scène en montrait un.
3. **Les gestes du style** (section 2 de sa fiche) : chaque scène du plan prend le geste qui sert
   son rôle (une accroche, un problème, une démonstration, une preuve, un appel). Une scène sans
   geste qui convienne (son interface, son produit, ce que l'original n'avait pas) se construit
   dans la grammaire du style : sa typographie, ses mises en page, ses mouvements, ses
   transitions, sa façon de montrer le produit (sections 3 à 7 de la fiche). Note dans `PLAN.md`,
   pour chaque scène, le geste repris ou « construite dans le style ». Exemple (une vidéo de page
   pour un logiciel, en style 7) : la structure vient du texte de la voix off ; trois gestes du kit
   repris (la phrase et ses objets, le désordre rangé, l'orbite autour de l'offre) ; deux scènes
   construites pour son cas, dans le style (le fichier déposé dans l'outil, la réponse qui arrive).
4. **Le garde-fou** : chaque vidéo garde au moins trois gestes signature de son style (deux sous
   15 s), sinon on ne le reconnaît plus ; le style 0 dit lesquels (sa fiche, section 2). Un geste signature est un mouvement, une mise en page ou
   un motif ; jamais une image (un paysage, une sphère, une gravure ne sont pas des gestes).
5. **Les scènes du kit** (styles 1 à 8) sont des démonstrations de ces gestes, pas des scènes à remplir : on en
   reprend le mouvement (le code d'une entrée, d'un cadre de sélection, d'un recul de caméra),
   jamais le décor. Lis la fiche en entier, puis écris les scènes du plan à partir du script : une
   phrase, ce qu'elle montre (sa vraie matière), et le geste du style qui la présente. Tu peux
   copier dans `compositions/` du projet une scène du kit pour en garder le mouvement. Ses textes,
   chiffres, prix et noms d'exemple sont tous dans l'objet `EXEMPLE`, en tête de son script : chaque
   valeur se remplace par une donnée d'`OFFRE.json` ou sa ligne se retire, avec ce qu'elle montrait.
   Une icône, un logo ou une capture qui manque retire son élément : jamais une icône de
   remplacement (une étoile), jamais un autre logo (son nom, à la place d'un logo absent). En
   style 0, au contraire, les scènes prêtes (`templates/scenes/`) se remplissent : leur objet
   `CONTENU` ([scenes.md](../references/scenes.md)).
6. **La loi de toutes les scènes**, quel que soit le style (le détail : [image.md](../references/image.md)
   et [mouvement.md](../references/mouvement.md)) :
   - **Les mots** : au plus 8 mots à lire par image (hors mots d'une interface montrée), au plus un
     mot à lire par seconde sur la vidéo. Chaque groupe de mots reste à l'écran au moins 0,8 s plus
     0,3 s par mot, et jamais moins de 1,5 s (`studio_motion.py lecture`), quel que soit le tempo de
     l'original ([mouvement.md](../references/mouvement.md), « La lecture »).
   - **La taille** : tout texte à lire fait au moins 28 px rapporté à un petit côté de 1080 px
     (2,6 %) ; le mot héros (1 à 3 mots) occupe 60 à 90 % de la largeur. Trop de mots se règle en
     coupant des mots, jamais en réduisant la police. Une interface reconstruite se montre assez
     près (caméra, échelle) pour que ses mots utiles atteignent ce plancher ; ses micro-textes non
     lus sont de la texture, marqués `data-layout-ignore` ([image.md](../references/image.md), « La
     typographie »).
   - **Le cadre** : le sujet d'un plan occupe au moins 40 % de la largeur ou de la hauteur du cadre ;
     jamais un petit élément au milieu d'un grand fond vide. En 9:16 comme en 16:9 : une scène
     verticale se recompose en hauteur, elle ne rétrécit pas la version 16:9
     ([image.md](../references/image.md), « Le cadre »).
   - **La caméra** : pendant qu'un texte se lit (de la fin de son entrée à sa sortie), seulement une
     dérive lente (2 à 6 % d'échelle ou quelques dizaines de pixels sur toute la tenue,
     `sine.inOut`) ; un recadrage net seulement entre deux phrases ; jamais de pas de caméra répétés
     ni d'allers-retours sous un texte. La vie, pendant la lecture, vient de ce que la phrase montre :
     un `rythme` trop bas se corrige par un événement de contenu, jamais par un recadrage ajouté
     ([mouvement.md](../references/mouvement.md), « La caméra » et « Le rythme »).
   - **Les couleurs : celles de sa marque, plus les vraies couleurs des objets connus**
     ([image.md](../references/image.md), « La palette »). Tout vient de `brand/tokens.css` : `--brand-bg`, `--brand-surface`, `--brand-text`,
     `--brand-muted`, `--brand-accent`, `--brand-secondary`, `--brand-contrast`, `--brand-sombre`,
     `--brand-clair`, `--brand-accent-lisible`, `--brand-gris-1` à `--brand-gris-4`. Les fonds de nuit
     d'un style prennent `var(--brand-sombre)` (sa couleur la plus sombre : son fond s'il est sombre,
     son texte s'il est clair), ses fonds clairs `var(--brand-clair)`, ses fonds pleins
     `var(--brand-accent)`, ses gris `var(--brand-gris-1)` à `var(--brand-gris-4)`. Le texte posé
     sur la nuit est `var(--brand-clair)`, sur l'accent `var(--brand-contrast)`. Du blanc ou du noir
     en transparence seulement pour une grille fine ou une ombre neutre. Aucune couleur en dur hors
     ces neutres, sauf celles des **objets connus**, dans tous les styles : tout ce que son public
     reconnaît d'un coup d'œil, par exemple le dossier bleu du Mac et les fichiers du kit
     (`objets.js`), la notification et les bulles d'iPhone, les vrais logos de ses outils, l'interface
     d'une plateforme reconstruite d'après capture, un objet de son métier. Ils gardent leurs vraies
     couleurs, ce sont les touches qui évitent une vidéo toute en trois couleurs
     ([image.md](../references/image.md), « Les objets connus ») ; leurs couleurs ne débordent jamais
     sur un fond, un texte ou un trait. Aucune teinte tirée de l'accent (`oklch(from…)`, `color-mix` avec l'accent, l'accent
     mêlé de blanc ou de noir, un dégradé vers lui, l'accent en transparence sur du sombre) : avec un
     jaune, cela fait du brun, de l'olive ou de l'orangé. Tout texte garde un contraste d'au moins
     4,5:1 avec son fond. Aucun halo, néon ni dégradé coloré ; les ombres sont neutres. Seule
     exception : un plan de plateau de la 3D poussée, quand le client l'a choisie (son hôte marqué
     `data-plateau`, [scenes.md](../references/scenes.md), « La 3D, quand elle sert »). Ses matières
     et sa lumière gardent les couleurs de la vraie vie (le bois, le mur, le soleil chaud) ; ses mots,
     ses accents et ses fonds à plat restent à sa marque, et les autres plans dans sa palette.
   - **Les images** : celles de l'original (paysages, photos, illustrations, sphères, gravures,
     fonds peints) deviennent sa vraie matière, en descendant l'échelle : une capture de sa page, de
     son produit ou d'un résultat, son interface reconstruite, un vrai chiffre mis en scène, les vrais
     logos de ses outils, puis seulement ses mots. Une forme du kit (disque, aplat, case, cadre,
     points) porte cette matière, sert de transition ou de fil conducteur, jamais de sujet : pas de
     particules ni de nuée décoratives, pas de caractères `●` ou `▬` posés comme objets
     ([image.md](../references/image.md), « Les défauts interdits »). Le plateau de la 3D poussée
     n'en est pas une image inventée : il entoure sa vraie matière ([image.md](../references/image.md),
     « Le plateau de la 3D poussée »).
   - **Une pub ne dessine pas de bouton** ([structures.md](../references/structures.md), publicité) :
     la fin du style garde son geste et finit sur « Découvre-le » et une flèche vers le bas.
7. **Les autres formats** : section « En vertical et en carré » de la fiche. Une mise en page,
   jamais un recadrage. En 9:16, prends la version `-vertical.html` d'une scène quand le kit en a
   une (kits 2, 4 et 5) ; sinon passe la racine de la scène à 1080 × 1920, elle se remet en page
   seule. Ces versions sont calées pour un Reel : en pub, vérifie sur la planche la zone sûre de la
   pub (tout texte entre y 269 et 1 248) et remonte ce qui en sort.
8. **La revue**, comme toute vidéo ([revue.md](../references/revue.md)), garde-fou compris.
9. **Il le garde** (« garde ce style pour mes prochaines vidéos ») : ajoute `style N` à ses
   `preferences` (`studio.config.json` ; un ancien `template N` vaut `style N`). La page ne le
   redemande plus : rappelle-le en une ligne, il peut toujours en demander un autre.

Chaque fiche ne dit ensuite que ce qui est propre à son style : son rythme, ses gestes, ses fonds
(quel jeton pour quel rôle), sa typographie, ses mouvements, ses transitions, son produit à
l'écran, son son, son ouverture et sa fin, ses adaptations à une autre offre et à d'autres formats,
et ses scènes.
