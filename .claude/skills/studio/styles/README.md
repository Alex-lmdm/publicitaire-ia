# Les templates du catalogue

Huit templates de vidéos de lancement, chacun repris d'une vraie vidéo de logiciel qui a fait ses
preuves, refait par nous (une fiche, des scènes signature déjà construites) et contrôlé sur une vraie
marque, en 16:9 et en 9:16. Le client les voit en vidéo dans sa formation (module « Templates ») et
les demande par leur numéro, leur nom ou la marque d'origine : « fais-moi une vidéo dans le
template 3 », « le template Verre sombre », « comme celle de Polymarket ».

**Un template est un look, pas un sujet.** Il se choisit à ce qu'on voit (fonds, typographie,
mouvements, façon de montrer le produit) et se fait sur n'importe quelle offre : une formation, un
coaching, un logiciel, un template. Ce qui suivait le sujet de l'original (une commande de trading,
des connecteurs d'entreprise) s'adapte à son offre : section « Sur une autre offre » de chaque fiche.

> On reprend la grammaire de ces vidéos, jamais leur contenu : ni leurs textes, ni leurs logos, ni
> leurs images, ni leur produit, ni leur musique. Tout passe aux couleurs et aux polices de sa marque.

| N° | Template | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
|---|---|---|---|---|---|
| 1 | Cartes pixels | grille claire, cartes d'interface du flou au net, blocs de pixels qui couvrent et découvrent, grand chiffre | Firecrawl | passer du problème au résultat | `01-cartes-pixels` |
| 2 | Titres géants | titres qui débordent du cadre sur la couleur de la marque, spécimen sur grille, mosaïque de cartes, sphère et faisceau, grille d'icônes | Cyera (studio Motionimo) | une vidéo de lancement | `02-titres-geants` |
| 3 | Verre sombre | interface en verre sombre inclinée en 3D, curseur qui règle l'offre, fond de nuit éclairé par la marque | Polymarket | l'offre et son prix | `03-verre-sombre` |
| 4 | Mots éparpillés | l'avant : mots un à un parmi des objets sur papier quadrillé, transitions en pixels ; l'après : orbe, dégradé vif, messages en verre | ElevenLabs | un avant / après | `04-mots-eparpilles` |
| 5 | Interrupteurs crème | papier crème, interrupteurs en cascade, trait à main levée qui entoure, coches en vague | ClaudeDevs | annoncer une nouveauté | `05-interrupteurs-creme` |
| 6 | Nuée d'encre | papier à fibres, cercle au pinceau qui se défait en nuée de points, gravures, « bientôt » | Kimi | un teaser avant l'ouverture | `06-nuee-d-encre` |
| 7 | Phrase tapée | phrases tapées derrière un gros curseur, outils éparpillés puis en orbite autour de l'offre | Zaro | lancer un logiciel ou une formation | `07-phrase-tapee` |
| 8 | Fenêtre peinte | phrases courtes sur blanc chaud, barres comparatives, l'outil dans une fenêtre sur fond peint | Cursor | prouver avec des chiffres | `08-fenetre-peinte` |

## Appliquer un template

1. **Le bon template.** Il donne un numéro, un nom ou une marque : prends ce kit, quel que soit le
   sujet de l'original. **Ne déconseille jamais un template parce que son offre ne ressemble pas à
   l'original** : c'est un look. Il hésite (« lequel tu me conseilles ? ») : demande-lui ce qu'il
   aime voir (fond clair ou sombre, interface en 3D, typo géante, papier, couleurs vives), puis
   propose 2 ou 3 templates de la colonne « Ce qu'on voit », numéro et nom, chacun avec la raison en
   une ligne ; son but n'est qu'un indice en plus (colonne « Souvent utile pour »).
2. **Le brief et l'offre comme d'habitude** (étapes 1 et 2 du skill) : le template fixe le look, pas
   le but ni les supports. `OFFRE.json` reste la seule source des faits : les chiffres, les prix et
   les noms d'exemple des scènes du kit se remplacent tous, ou la scène se retire. Jamais de faux
   chiffre parce que la scène en montrait un.
3. **La structure** : celle de son objectif ([structures.md](../references/structures.md)), posée
   dans la suite de scènes du template (section « La structure » de la fiche). Les trois idées
   restent dans ce look.
4. **La fabrication** : lis la fiche en entier, puis copie les scènes du kit (`compositions/`) dans
   le projet de chaque vidéo (`compositions/` du projet). Remplace leurs textes par ceux du plan,
   garde leurs mouvements signature et leur rythme : les recadrages et les gestes que la fiche
   donne pour passer `rythme` ne se retirent pas. Les couleurs viennent de `var(--brand-*)`, jamais en
   dur ; un logo absent de sa marque se remplace par son nom, jamais par un autre logo.
5. **Les autres formats** : section « En vertical et en carré » de la fiche. Une mise en page,
   jamais un recadrage.
6. **La revue**, comme toute vidéo ([revue.md](../references/revue.md)).
7. **Il le garde** (« garde ce template pour mes prochaines vidéos ») : ajoute `template N` à ses
   `preferences` (`studio.config.json`) ; ses vidéos suivantes partent de ce kit, avec ses
   corrections par-dessus.
