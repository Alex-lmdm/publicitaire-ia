# Les styles du catalogue

Huit styles de motion design, chacun repris d'une vraie vidéo de lancement de logiciel qui a fait
ses preuves, refait par nous (une fiche, des scènes signature déjà construites) et contrôlé en 16:9
et en 9:16, sur une marque claire comme sur une marque sombre : chaque scène a sa mise en page
verticale (un fichier `-vertical.html`, ou une scène qui se remet en page seule). Le client les voit
en vidéo sur la page des styles et des musiques, à chaque vidéo (étape 4 du skill), et dans sa
formation (module « Styles »). Il les demande par leur numéro, leur nom ou la marque d'origine :
« dans le style 3 », « le style Verre sombre », « comme celle de Polymarket » ; « template » veut
dire la même chose (ses premières vidéos les appelaient ainsi).

**Un style est un look, pas un plan.** Il donne ce qu'on voit (fonds, typographie, mouvements,
transitions, façon de montrer le produit) et ses gestes signature. La structure, elle, vient
toujours de la vidéo du client : son but, l'idée qu'il a choisie, son script, ce qu'il veut montrer.
Un style se fait donc sur n'importe quelle offre (une formation, un coaching, un logiciel, un
template) et pour n'importe quel but (vendre, une pub, une nouveauté, un lancement). Ce qui suivait
le sujet de l'original (une commande de trading, des connecteurs d'entreprise) s'adapte à son
offre : section « Sur une autre offre » de chaque fiche.

> On reprend la grammaire de ces vidéos, jamais leur contenu : ni leurs textes, ni leurs logos, ni
> leurs images, ni leur produit, ni leur musique. Tout passe aux couleurs et aux polices de sa marque.

| N° | Style | Ce qu'on voit | D'après | Souvent utile pour | Dossier |
|---|---|---|---|---|---|
| 1 | Cartes pixels | grille claire, cartes d'interface du flou au net, blocs de pixels qui couvrent et découvrent, grand chiffre | Firecrawl | passer du problème au résultat | `01-cartes-pixels` |
| 2 | Titres géants | titres qui débordent du cadre sur la couleur de la marque, spécimen sur grille, mosaïque de cartes, sphère et faisceau, grille d'icônes | Cyera (studio Motionimo) | une vidéo de lancement | `02-titres-geants` |
| 3 | Verre sombre | interface en verre sombre inclinée en 3D, curseur qui règle l'offre, fond de nuit éclairé par la marque | Polymarket | l'offre et son prix | `03-verre-sombre` |
| 4 | Mots éparpillés | l'avant : mots un à un parmi des objets sur papier quadrillé, transitions en pixels ; l'après : orbe, dégradé vif, messages en verre | ElevenLabs | un avant / après | `04-mots-eparpilles` |
| 5 | Interrupteurs crème | papier crème, interrupteurs en cascade, trait à main levée qui entoure, coches en vague | ClaudeDevs | annoncer une nouveauté | `05-interrupteurs-creme` |
| 6 | Nuée d'encre | papier à fibres, cercle au pinceau qui se défait en nuée de points, gravures, « bientôt » | Kimi | un teaser avant l'ouverture | `06-nuee-d-encre` |
| 7 | Phrase tapée | phrases tapées derrière un gros curseur, outils éparpillés puis en orbite autour de l'offre | Zaro | lancer un logiciel ou une formation | `07-phrase-tapee` |
| 8 | Fenêtre peinte | phrases courtes sur blanc chaud, barres comparatives, l'outil dans une fenêtre sur fond peint | Cursor | prouver avec des chiffres | `08-fenetre-peinte` |

Chaque style a son aperçu dans `assets/styles/` (`<dossier>.mp4` et `<dossier>.jpg` : quelques
secondes de ses gestes, à la marque LMDM), que la page des styles et des musiques montre.

## Appliquer un style

1. **Le bon style.** Il le choisit sur la page des styles et des musiques, ou il l'a donné
   d'emblée : prends ce kit, quel que soit le sujet de l'original. **Ne déconseille jamais un style
   parce que son offre ne ressemble pas à l'original** : c'est un look. Ton conseil, en une phrase,
   part de ce que la vidéo va montrer (son interface, un avant / après, des chiffres, une annonce,
   un teaser) et de sa marque (claire ou sombre) ; la colonne « Souvent utile pour » n'est qu'un
   indice. Il hésite (« lequel tu me conseilles ? ») : demande-lui ce qu'il aime voir (fond clair ou
   sombre, interface en 3D, typo géante, papier, couleurs vives), puis propose 2 ou 3 styles,
   numéro et nom, chacun avec sa raison en une ligne.
2. **La structure vient de sa vidéo**, jamais de l'original : celle de son but
   ([structures.md](../references/structures.md)), l'idée qu'il a choisie, son script. Le style ne
   change ni la structure ni les trois idées. `OFFRE.json` reste la seule source des faits : les
   chiffres, les prix et les noms d'exemple des scènes du kit se remplacent tous, ou la scène se
   retire. Jamais de faux chiffre parce que la scène en montrait un.
3. **Les gestes du style** (section 2 de sa fiche) : chaque scène du plan prend le geste qui sert
   son rôle (une accroche, un problème, une démonstration, une preuve, un appel). Une scène sans
   geste qui convienne (son interface, son produit, ce que l'original n'avait pas) se construit
   dans la grammaire du style : ses fonds, sa typographie, ses mouvements, ses transitions, sa façon
   de montrer le produit (sections 3 à 7 de la fiche). Plus son cas ressemble à l'original (un
   lancement de logiciel), plus de scènes du kit se reprennent telles quelles ; plus il s'en
   éloigne, plus on en construit. Note dans `PLAN.md`, pour chaque scène, le geste repris ou
   « construite dans le style ».
   Exemple (vidéo du haut de la page de Publicitaire IA, style 7, 03/11/2026) : la structure vient
   du texte de la voix off ; trois gestes du kit repris (la phrase et ses objets, le désordre réduit
   en points, l'orbite et le point d'encre) ; deux scènes construites pour son cas, dans le style
   (le dossier déposé sur Claude, la conversation dans Claude).
4. **Le garde-fou** : chaque vidéo garde au moins trois gestes signature de son style (deux sous
   15 s), sinon on ne le reconnaît plus, et c'est là que la qualité tombe.
5. **La fabrication** : lis la fiche en entier, puis copie dans le projet de chaque vidéo
   (`compositions/` du projet) les scènes du kit que le plan reprend, en entier ou en partie (on
   garde le geste, on coupe le reste). Remplace leurs textes par ceux du plan, garde leurs
   mouvements signature et leur rythme : les recadrages et les gestes que la fiche donne pour passer
   `rythme` ne se retirent pas. Un logo absent de sa marque se remplace par son nom, jamais par un
   autre logo.
   **Les couleurs, sur n'importe quelle marque.** Les fonds qui signent le look (la nuit, le noir,
   le taupe, le papier, le crème) restent ceux du kit, fixes, que sa marque soit claire ou sombre :
   ne les remplace jamais par `var(--brand-bg)`, et le texte posé sur un fond sombre reste clair
   (jamais `var(--brand-text)` d'une marque claire). Sa marque donne les accents
   (`var(--brand-accent)`, le texte posé dessus en `var(--brand-contrast)`) et ses polices. Tout
   texte garde un contraste d'au moins 4,5:1 avec son fond (section 3 de chaque fiche). Une scène
   construite dans le style prend les mêmes fonds, les mêmes polices et les mêmes accents. Avec un
   accent jaune, tout mélange de l'accent avec du noir ou du gris vire à l'olive, presque brun, et
   un dégradé vers le blanc passe par le jaune pâle : garde l'accent pur sur des fonds neutres
   (pub d'essai du 03/11/2026, fiche 4, section 3).
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
