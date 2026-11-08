# L'image : ce qu'on voit à chaque instant

Une vidéo du studio a le niveau d'une vidéo de lancement faite par un studio de motion design :
**ce qu'on voit raconte, quelques mots très grands le ponctuent.** Le test : on coupe le son, on
regarde sans se presser, et on a compris ce que fait l'offre, pour qui, et quoi faire, sans avoir lu
plus d'un mot par seconde. Le mouvement, les raccords et la caméra sont dans
[mouvement.md](mouvement.md).

## Trois identités

1. **Sa marque** porte la vidéo : couleurs, polices et logo, déjà dans `brand/` du projet
   (`var(--brand-…)`, `brand/logo.*`). Jamais une couleur ni une police de marque en dur.
2. **Les surfaces de son offre** gardent leur identité : sa page, son espace de formation, son
   logiciel, dans leurs vraies couleurs et polices (relevées dans la capture).
3. **Les outils** qu'il utilise ou dont sa page parle (Instagram, Notion, Canva, Stripe, Zoom,
   ChatGPT…) gardent leurs logos et leur allure : des repères que son public connaît
   (`studio_motion.py logos`).

## La vraie matière

Ce qui se montre vient du client ou de ses outils, **et se fabrique en motion design** : des mots,
des interfaces, des chiffres, des objets et des schémas animés en code. Ses photos et ses vidéos ne
sont pas le film : elles n'y entrent que pour montrer son produit ou son résultat, mises en scène
(« Ses photos et ses vidéos », juste après). Pour chaque plan, descends cette échelle et prends le
premier barreau qui existe :

1. **Son produit ou son résultat en action.** Son interface reconstruite d'après capture, animée :
   on tape, on clique, elle répond. Simplifier pour qu'elle se lise (agrandir le bouton utile,
   réduire une liste à cinq lignes), oui ; inventer une fonction ou un écran, non. Une
   simplification se note dans `sources/NOTES.md`. Ou le résultat lui-même (le Reel que son outil a
   produit, la page créée, un avant / après, un vrai message reçu), joué dans un objet qui agit :
   le téléphone du kit, la fenêtre, la bulle, la notification.
2. **Un vrai chiffre** de `OFFRE.json` mis en scène : un compteur, une barre, un prix, avec son
   contexte.
3. **Le schéma de son vrai mécanisme** : des nœuds vrais (sa page, son produit, les étapes, ce qu'on
   obtient) reliés par des traits qui se tracent, le fil conducteur qui les parcourt.
4. **Les objets connus et les vrais logos** des outils que l'offre nomme (plus bas).
5. **Ses mots seuls**, en très grand, qui jouent ce qu'ils disent.

## Ses photos et ses vidéos : seulement pour montrer le résultat

Sa page en est souvent pleine. **Le but n'est pas de les reprendre** : une vidéo faite de ses
photos recadrées, zoomées ou posées en fond est un diaporama, pas du motion design. Retour du
créateur sur le Reel Gordon Ramsay (08/11/2026), où chaque plan reprenait une photo de la page dans
la même carte : « juste une succession d'images », « les motion design sont assez basiques et
bateau ».

- **Une photo ou une vidéo de sa page n'entre que si elle montre ce qu'il vend en marche ou ce
  qu'on obtient** : son logiciel, son espace de formation, le Reel produit, l'avant / après, une
  vraie capture de ventes ou de message. Une photo d'ambiance, un portrait, une photo de banque
  d'images, un décor, une mise en scène de produit : jamais, même si sa page n'a que ça.
- **Elle est mise en scène, avec astuce** : dans un objet qui agit (le Reel qui joue dans le
  téléphone, sur l'interface de la plateforme, un double tap, le cœur ; la capture qui sort de la
  fenêtre ; l'avant / après qu'un curseur partage), et du motion design se passe sur elle ou autour
  (un compteur qui monte, une coche, une notification qui arrive, un mot qui claque). Exemple : le
  Reel Dupliq.me de la page de vente de Publicitaire IA, où la vidéo obtenue joue dans un iPhone,
  parce qu'elle est tout le résultat.
- **Jamais** en fond plein cadre, jamais une carte photo sous un titre posé, jamais une photo qui
  dérive lentement pendant qu'on lit. **Une photo fixe ne porte jamais deux plans de suite**, et
  au plus un plan sur quatre.
- **Le test du diaporama**, sur chaque plan : cache ses photos et ses vidéos. S'il ne reste qu'un
  titre et un cadre, le plan est une diapositive : refais-le en motion design.
- **Une offre hors du digital** (un cours en présentiel, un produit physique, un restaurant) n'a
  souvent que des photos. La vidéo se construit quand même : sa fiche (le programme qui se coche,
  le prix qui claque), les objets de son métier reconstruits (la fiche recette, le ticket, la carte
  de réservation), ses mots qui jouent. Publicitaire IA est fait pour les offres en ligne : la porte
  de vérité le dit au client ([offre.md](offre.md)).

Ce qu'on peut montrer selon ce qu'il vend :

| Il vend | Ce qu'on montre de vrai |
|---|---|
| Une formation | l'espace de formation, le sommaire qui se déroule, un module qui s'ouvre, les vraies miniatures, le résultat promis |
| Un coaching, un service | le déroulé de l'accompagnement en étapes, l'agenda des séances, les messages reçus, ce que le client a entre les mains à la fin |
| Un logiciel, une app | la fonction en action dans son interface reconstruite, le résultat qu'elle produit |
| Un template, un guide | le document qui se remplit, les pages qui défilent, le résultat obtenu |
| Une communauté | les espaces, le rythme (lives, défis), ce qu'on y trouve, sans inventer de membres |
| Des résultats | les vraies captures (ventes, vues, avant / après) avec leurs vrais chiffres |

## Les objets connus : la touche de couleur vraie

Sa marque peint le film : les fonds, les mots, les formes, les accents. **Ce qui est réel et connu
garde son vrai visage et ses vraies couleurs**, et c'est ce qui donne de la fraîcheur : une vidéo
toute dans les trois couleurs de la marque (par exemple jaune, noir, blanc, et rien d'autre) fait fade.

**Le réflexe, à chaque plan** : qu'est-ce que son public reconnaîtrait ici d'un coup d'œil ? Une
interface qu'il utilise, une icône qu'il voit tous les jours, un objet de son métier ou de sa vie.
Si la réponse existe, montre-la telle qu'il la connaît, dans ses vraies couleurs, plutôt qu'une
forme ou une icône à la couleur de la marque. Chaque offre a les siens, et la plupart ne sont dans
aucune liste : pars de son sujet, de son métier, de son public et de ce que sa page montre.

**Des exemples, jamais une liste fermée.** Ce que le kit a déjà, prêt à poser :

| Le plan parle de… | On montre |
|---|---|
| un dossier, un fichier, un document | le dossier bleu du Mac, le fichier PDF, Word, Excel, PowerPoint, la vidéo, l'image, le son, l'archive : `K.ic("objet-dossier")`, `objet-pdf`, `objet-doc`, `objet-tableur`, `objet-presentation`, `objet-video`, `objet-image`, `objet-audio`, `objet-zip`, `objet-fichier` (le kit, `objets.js`) |
| un outil, une app, un moyen de paiement | son vrai logo en couleurs (`studio_motion.py logos`, 7 432 marques), nu ou en icône d'app |
| une plateforme (Instagram, YouTube, TikTok, Stripe, Gmail, Notion, Zoom…) | son interface, reconstruite d'après une vraie capture, dans ses couleurs et sa police : le post, le lecteur, la page de paiement, la boîte de réception |
| son téléphone, une notification, un message | le téléphone du kit (`k-tel`) avec sa barre d'état (`K.statut` : 9:41, réseau, batterie) ; la notification d'iPhone (`K.notification`, l'icône d'app = le vrai logo) ; les bulles bleues, grises ou WhatsApp (`K.bulle`) |
| une fenêtre d'ordinateur | la fenêtre du kit (`k-fenetre`) et ses trois boutons rouge, jaune, vert (`k-feux`) |

Et ce que le kit n'a pas, à construire pour son offre, par exemple :

| Son offre touche à… | Ce que son public reconnaîtrait |
|---|---|
| le sport, la santé | la montre et ses anneaux d'activité, l'appli de course et son tracé, la prise de rendez-vous en ligne |
| l'immobilier | l'annonce avec ses photos et son prix au m², le plan d'un appartement, la carte et ses épingles |
| la cuisine, la restauration | la fiche recette, le ticket de commande, l'appli de livraison et son suivi |
| le commerce en ligne | le tableau de bord des ventes, le panier, l'étiquette du colis et son suivi |
| l'argent, la gestion | la carte bancaire, l'appli de la banque, la facture, le relevé |
| la musique, le podcast, la vidéo | le lecteur et sa barre de progression, la forme d'onde, la timeline de montage |
| le voyage | la carte d'embarquement, la réservation, l'itinéraire sur la carte |

**Le fabriquer.** Un vrai logo : `logos`. Une plateforme : reconstruite d'après une vraie capture
(le repérage la prend). Un objet de son métier : dessiné en HTML ou en SVG d'après son allure
courante, comme ceux du kit, dans ses couleurs habituelles, assez grand pour se reconnaître.
`palette` connaît les couleurs du kit et des logos posés ; celles d'un objet construit pour cette
vidéo y restent signalées : la revue vérifie que ce sont bien les siennes, pas une teinte de
l'accent.

- **Une icône d'un seul trait (Lucide) seulement pour une idée sans objet connu** : une coche, une
  flèche, un euro. Jamais un dossier, un fichier, une enveloppe ou un téléphone génériques teintés
  de l'accent quand l'objet a un vrai visage.
- **Des touches, pas un décor** : ces couleurs restent sur leur objet. Jamais un fond, un texte, un
  trait ni un dégradé tiré d'elles ; le film reste à sa marque.
- **Toujours vrai** : un logo ou l'interface d'une marque seulement pour un outil que l'offre
  utilise ou dont sa page parle, une plateforme seulement là où son offre vit vraiment (sa pub sur
  Instagram, son paiement par Stripe) ; un objet courant (un dossier, une carte d'embarquement, un
  ticket) se montre quand le plan parle de lui. Aucun faux contenu : ce qu'un objet affiche de
  lisible (un prix, une date, un nom, une vente) vient de la fiche ; sinon c'est une texture
  illisible, jamais un chiffre inventé.
- **Le seuil** : toute vidéo de plus de 15 s montre au moins trois objets connus dans leurs vraies
  couleurs (logos compris), une vidéo plus courte au moins un. Le repérage les liste
  ([reperage.md](reperage.md)).

Une forme simple à ses couleurs (disque, aplat, case, cadre, trait) sert de **cadre** (elle porte
une capture, un chiffre, un logo, un mot), de **transition** (elle couvre, s'ouvre, devient l'objet
suivant) ou de **fil conducteur** (le point de sa couleur qui relie, raye, devient le point final) ;
jamais de sujet d'un plan. Il manque une matière importante : c'est la question unique du repérage
([reperage.md](reperage.md)), pas une forme de plus.

## Le cadre

- **Le sujet remplit le cadre** : ce qu'on regarde occupe au moins 40 % de la largeur ou de la
  hauteur. Un petit élément au milieu d'un grand fond vide n'est jamais un plan : approche la caméra,
  recadre, ou donne-lui un monde (des cartes autour, sa page derrière, ses résultats en éventail).
- **Une interface se montre de près** : assez pour que ses mots utiles fassent au moins 28 px sur
  un petit côté de 1080 (`check` le mesure : `text_below_floor`). Ses micro-textes non lus sont de
  la texture.
- **De la profondeur** : trois plans (un premier plan qui passe, flou ; le sujet, net ; un fond qui
  vit), une perspective légère, une ombre qui situe l'objet, un flou qui grandit avec la distance.
- **Des échelles qui contrastent** : un mot géant à côté d'une étiquette ; un objet tout proche et
  d'autres au loin.
- **Pas tout au centre** : le sujet peut être décentré, sortir d'un bord, être coupé par le cadre
  quand c'est voulu. Tout centré, tout petit, tout au même plan : c'est une maquette, pas un film.
- **En vertical, on recompose** : en 9:16, le sujet s'empile en hauteur et grandit (interface en
  carte verticale, téléphone au centre, mots empilés et plus gros) ; on ne rétrécit jamais une mise
  en page 16:9 au milieu d'un écran haut. Tout texte important tient dans la zone sûre du support
  (`studio_motion.py zones`).
- **Un moment signature par plan** : un geste qu'on n'attend pas et qu'on a envie de revoir (la
  vignette cliquée qui vient au centre pendant que les autres pivotent, le dossier qui devient le
  nœud d'un schéma, la liste barrée qui tombe en morceaux). Nomme-le dans le plan avant d'animer.

## La palette : ses couleurs, et les vraies couleurs des objets connus

Tout ce que la vidéo dessine, hors objets connus (plus haut), prend ses couleurs dans
`brand/tokens.css`, et seulement là :
`--brand-bg`, `--brand-surface`, `--brand-text`, `--brand-muted`, `--brand-accent`,
`--brand-secondary`, `--brand-contrast` (le texte sur l'accent), `--brand-sombre` (les fonds de
nuit), `--brand-clair`, `--brand-accent-lisible` (l'accent d'un texte sur la nuit), les gris
`--brand-gris-1` à `--brand-gris-4`, et du blanc ou du noir en transparence pour une grille fine ou
une ombre.

L'accent se pose **plein**, jamais en transparence sur un fond sombre (ni en fondu ni en flou à son
entrée : le temps de l'effet, il vire à l'olive ou au brun), jamais mélangé au noir, au blanc ou au
gris, jamais dérivé (`oklch(from …)`, `color-mix`, une « nuit » teintée). Une couleur qui passe de
l'encre à l'accent change d'un coup, sous un volet ou un mouvement. Les dégradés vont d'un neutre à
un neutre. Un texte garde un contraste d'au moins 4,5:1 avec son fond.

Seuls ses **vraies captures**, les **logos de ses outils**, les **interfaces des plateformes** et
les **objets connus** (ceux du kit et ceux construits pour la vidéo) gardent leurs propres couleurs
(« Les objets connus », plus haut). `studio_motion.py palette` connaît celles du kit et des logos
posés dans le projet, et relève tout le reste sur le MP4 : chaque instant relevé est l'un d'eux, ou
une teinte à corriger.

## Les fonds et les objets

- **Le fond est un acteur, pas un quota.** Il change quand le film change de temps (le nom de
  l'offre, un chapitre, le prix, un avant / après), avec une cause visible (un clic, un volet, un
  objet qui grandit). Les fonds du kit : la nuit à sa marque avec une grille fine, le clair avec
  grille, l'accent plein pour les temps forts, l'écran coupé pour un avant / après.
- **Des logos qui flottent seulement quand ils ont un sens** : les vrais logos nus (`K.logoNu`, sans
  tuile) de l'outil dont la scène parle, pour remplir une zone vide ; 6 à 8, la plupart nets, en
  vraie profondeur (petits au loin, moyens nets, un ou deux grands et flous au premier plan),
  jamais collés aux mots, hors de la bande du sticker. Une scène sans logo pertinent n'en a pas :
  elle vit par sa matière. Jamais d'icônes génériques (étoile, éclair, ciseaux).
- Le contexte se montre par l'interface plutôt qu'en titre : pour « un client m'a écrit », le
  téléphone, la notification, le message.

## La typographie

- **Trois tailles, jamais plus**, en 9:16 (en 16:9, à proportion de la hauteur de 1080) :

  | Rôle | Mots | Taille |
  |---|---|---|
  | le **mot héros** | 1 à 3 | il remplit 60 à 90 % de la largeur de sa colonne (130 à 400 px en 9:16) |
  | la **ligne d'appui** | 3 à 6 | 56 à 72 px |
  | les **étiquettes** posées sur ce qu'on montre | 1 à 4 | 30 à 40 px, jamais sous 28 px |

  Trop de mots se règle en coupant des mots, jamais en réduisant la police. Au plus 8 mots à lire
  sur une image, hors interface.
- **Le mot joue ce qu'il dit**, une fois lisible : il claque, s'étire, se barre, se surligne d'un
  bloc plein, se change sur place, ses lettres tombent en rafale (`kit.md`). Deux tons : le plein et
  l'accent (« Ton **lien.** »), ou le gris d'appui et le plein.
- Les étiquettes de fonction : deux ou trois mots en blocs pleins empilés (`k-blocs`), posés à côté
  de l'interface qui le fait.
- Un contour net (`k-contour`) pour doubler un mot plein, jamais une lueur. Texte plein, jamais en
  dégradé. La frappe au clavier seulement dans un champ de saisie.

## Les défauts interdits

C'est là que tombe une vidéo générée quand rien d'autre n'est décidé. Chacun est interdit, sauf si
la vraie matière du client ou sa vidéo de référence le contient, et alors seulement comme elle.

| Interdit | À la place |
|---|---|
| Un fond sombre vide avec de petits éléments au milieu | Le sujet en grand, au moins 40 % du cadre, dans un monde |
| Des écrans de texte posés sur le même fond, plan après plan (des slides) | Sa matière qui agit, un objet qui devient le suivant |
| Des sous-titres : une phrase par écran, en haut, au-dessus d'une petite interface | Le plan montre en grand ; un mot héros, une ligne d'appui au plus |
| Des mots isolés ou des chiffres sans contexte | Ce que l'idée dit, montré, et ses mots qui claquent |
| Des images inventées : paysages, couchers de soleil, planètes, sphères, illustrations, photos d'ambiance | Sa vraie matière, en descendant l'échelle |
| Ses photos de page à la suite, recadrées, zoomées ou en fond (un diaporama) | Du motion design construit ; ses photos seulement pour montrer le résultat, mises en scène (« Ses photos et ses vidéos ») |
| Des formes seules (disques, carrés, aplats) comme sujet ; des particules, nuées ou poussières décoratives | Une forme qui porte une matière réelle, ou qui sert de transition |
| Halos, néons, reflets d'objectif, orbes lumineux, sol quadrillé lumineux, ondes de choc | Des objets du sujet floutés par la profondeur ; la grille fine du kit |
| Dégradés violets ou bleus, dégradés tirés de l'accent | L'accent plein sur des neutres |
| Tout centré ; tout qui entre en même temps ; chaque élément qui monte en fondu | Des entrées variées et décalées ([mouvement.md](mouvement.md)) |
| Un texte qui bouge pendant qu'on le lit ; un titre qui continue de glisser une fois posé | Le titre posé reste immobile ; la vie vient du sujet et du monde autour |
| Trois cartes en ligne, une grille de chiffres, un titre sur une capture assombrie | Une carte à la fois, au premier plan, qui agit |
| Des étiquettes dans les coins, des cadres et des crochets décoratifs, des compteurs « 01 / 02 » | Des étiquettes posées sur ce qu'on montre |
| Le logo rangé dans un coin pendant toute la vidéo | Le logo arrive à son moment (le nom, la fin) |
| Des icônes génériques, des emoji, des logos posés sur des tuiles | Les vrais logos nus de ses outils, là où ils ont un sens |
| Un dossier, un fichier, une enveloppe ou un téléphone génériques aux couleurs de la marque ; une vidéo toute en trois couleurs | L'objet connu dans ses vraies couleurs : le dossier bleu du Mac, le vrai PDF, la vraie notification, le vrai logo |
| Une fausse interface vague dans un faux navigateur | Son interface réelle, reconstruite d'après capture |
| Le même enchaînement d'une vidéo à l'autre | Change l'angle, la matière, les gestes, les fonds et les transitions d'une vidéo à l'autre |

Après le premier rendu, nomme chaque défaut présent (de cette liste ou non), écris-le dans
« Interdits de cette vidéo » (`PLAN.md`) et corrige-le. La liste de la vidéo grandit à chaque rendu.

Test final : si cette vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom, elle
est trop générique. Recommence par ce que son offre a de visible.

## Avec un style du catalogue

La grammaire du style (sa typographie, ses mises en page, ses mouvements, ses transitions) prime
sur cette page pour ce qui est des gestes. Jamais pour la palette, la vraie matière, le cadre, la
taille du texte ou la lecture : un style ne justifie aucune teinte hors palette, aucune image
inventée, aucune forme seule à la place d'un sujet, aucun texte plus petit que 28 px, aucune
phrase tenue moins longtemps que sa lecture, ni plus d'un mot à lire par seconde.
