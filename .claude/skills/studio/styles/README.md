# Les styles du catalogue

**Le style 0, « Sur mesure », est le style maison** : il ne copie aucune vidéo et n'impose aucun
geste ; chaque vidéo y prend sa forme, au niveau d'[ambition.md](../references/ambition.md). C'est
le conseil par défaut (point 1 ci-dessous).

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
réelle) et se peint aux couleurs de sa marque (point 6, et [interdits.md](../references/interdits.md)). La structure, elle, vient toujours de la
vidéo du client : son but, l'idée qu'il a choisie, son script validé, ce qu'il veut montrer. On ne
refait pas l'original séquence par séquence : on adapte tout. Un style se fait donc sur n'importe
quelle offre (une formation, un coaching, un logiciel, un template) et pour n'importe quel but
(vendre, une pub, une nouveauté, un lancement) ; ce qui suivait le sujet de l'original s'adapte à
son offre (section « Sur une autre offre » de chaque fiche).

> On reprend la grammaire de ces vidéos, jamais leur contenu : ni leurs textes, ni leurs logos, ni
> leurs images, ni leur produit, ni leur musique, ni leurs couleurs. Une image de l'original
> (paysage, photo, illustration, objet) devient la vraie matière du client qui sert le script
> ([interdits.md](../references/interdits.md), « Rien d'inventé ») : une capture, son interface
> reconstruite, un vrai chiffre mis en scène, les vrais logos de ses outils, puis seulement ses
> mots. On ne la redessine jamais, et on ne la remplace pas par une forme seule (un disque, un
> carré, une nuée sans sujet).

| N° | Style | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
|---|---|---|---|---|---|
| 0 | Sur mesure | sa vraie matière en grand et en profondeur, chaque passage un objet qui devient le suivant, des mots qui jouent ce qu'ils disent, des interfaces qui vivent, une caméra qui plonge : une forme neuve pour chaque offre | le style maison, au niveau des grands studios de motion design | tout, et d'abord sa première vidéo | `00-sur-mesure` |
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
   n'accélère aucune tenue pour suivre le tempo de l'original.
3. **Les gestes du style** (section 2 de sa fiche) : chaque scène du plan prend le geste qui sert
   son rôle (une accroche, un problème, une démonstration, une preuve, un appel). Une scène sans
   geste qui convienne (son interface, ce que l'original n'avait pas) se construit dans la
   grammaire du style : sa typographie, ses mises en page, ses mouvements, ses transitions (sections
   3 à 7 de la fiche). Note dans `PLAN.md`, pour chaque scène, le geste repris ou « construite dans
   le style ».
4. **Le garde-fou** (styles 1 à 8) : chaque vidéo garde au moins trois gestes signature de son
   style (deux sous 15 s), sinon on ne le reconnaît plus. Un geste signature est un mouvement, une
   mise en page ou un motif ; jamais une image. Le style 0 n'en a pas : sa seule exigence est le
   niveau d'[ambition.md](../references/ambition.md).
5. **Les scènes des styles 1 à 8** sont des démonstrations de leurs gestes, pas des scènes à remplir :
   on en reprend le mouvement (le code d'une entrée, d'un cadre de sélection, d'un recul de caméra),
   jamais le décor. Tu peux en copier une dans `compositions/` du projet : ses textes, chiffres, prix
   et noms d'exemple sont tous dans l'objet `EXEMPLE`, en tête de son script, et chaque valeur se
   remplace par une donnée d'`OFFRE.json` ou sa ligne se retire, avec ce qu'elle montrait. Une icône,
   un logo ou une capture qui manque retire son élément : jamais une icône de remplacement, jamais
   un autre logo. En style 0, les scènes prêtes (`templates/scenes/`) sont des exemples du même
   ordre ([scenes.md](../references/scenes.md)).
6. **Les interdits valent dans tous les styles** ([interdits.md](../references/interdits.md)) : un
   style ne justifie ni une image inventée, ni une couleur hors de sa palette (les fonds de nuit d'un
   style prennent `var(--brand-sombre)`, ses fonds clairs `var(--brand-clair)`, ses aplats
   `var(--brand-accent)`, ses gris `var(--brand-gris-1)` à `4`, le texte sur la nuit
   `var(--brand-clair)` et sur l'accent `var(--brand-contrast)`), ni un texte sous 28 px, ni une
   tenue plus courte que la lecture, ni un bouton dessiné dans une pub. L'ambition aussi
   ([ambition.md](../references/ambition.md)) : sa grammaire décide des gestes, le niveau reste
   celui d'un grand studio.
7. **Les autres formats** : section « En vertical et en carré » de la fiche. Une mise en page,
   jamais un recadrage. En 9:16, prends la version `-vertical.html` d'une scène quand le kit en a
   une (kits 2, 4 et 5) ; sinon monte-la telle quelle par un hôte en 1080 × 1920 : le kit
   (`K.cadre`) recale sa racine sur l'hôte et elle se remet en page seule. Ces versions sont calées pour un Reel : en pub, vérifie sur la planche la zone sûre de la
   pub et remonte ce qui en sort.
8. **La passe du directeur et la revue**, comme toute vidéo ([ambition.md](../references/ambition.md),
   [revue.md](../references/revue.md)), garde-fou compris.
9. **Il le garde** (« garde ce style pour mes prochaines vidéos ») : ajoute `style N` à ses
   `preferences` (`studio.config.json` ; un ancien `template N` vaut `style N`). La page ne le
   redemande plus : rappelle-le en une ligne, il peut toujours en demander un autre.

Chaque fiche ne dit ensuite que ce qui est propre à son style : son rythme, ses gestes, ses fonds
(quel jeton pour quel rôle), sa typographie, ses mouvements, ses transitions, son produit à
l'écran, son son, son ouverture et sa fin, ses adaptations à une autre offre et à d'autres formats,
et ses scènes.
