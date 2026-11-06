# Les recettes : des enchaînements éprouvés

Chaque recette est une scène (ou un raccord) déjà fabriquée avec le kit et validée à l'image,
avec ses temps. Adapte le contenu à l'offre, garde le mouvement et la densité. Le code de
référence de chacune vient d'une vraie vidéo de page (celle de Monteur IA, 68 s) ; les
fonctions sont décrites dans `kit.md`. Les recettes du skill `hyperframes-animation` (nom entre
crochets, livré dans ce dossier) donnent d'autres techniques : lis-les avant de coder un effet
nouveau.

Une story courte (un rappel, un teaser) = une ou deux recettes ; une story de lancement = une
recette par plan du film (huit ou neuf, de 2,5 à 6,5 s). Un Reel = trois ou quatre. Une vidéo de
page = huit à dix, reliées par des raccords d'objet. Chaque recette porte un plan du film : elle
montre ce qu'il dit, et pose ses quelques mots.

## Le langage du motion design (relevé le 07/11/2026)

Le créateur a donné pour référence sept vidéos de lancement faites par Higgsfield Katana (du motion
design écrit par une IA, comme ici). Ce qu'elles font, et que toute vidéo du studio fait aussi :

1. **Peu de mots, et ils jouent.** 20 à 30 mots en 30 à 40 s. Les mots clés en très grand, deux
   tons ; le mot fait ce qu'il dit (« STRETCH » s'étire, « TEMPLATE » se barre, « MOO » se répète
   jusqu'à « MOOOOOO »), puis il devient l'objet suivant (le O devient un œil, la caméra y plonge).
2. **On montre le comment.** La demande tapée dans l'outil, ses mots clés qui se surlignent, des
   lignes d'étape (« Je lis… », « J'anime… »), le rendu qui se charge, puis le film qui jaillit.
3. **Un fil rouge.** Un seul objet (un point, une comète, un anneau) traverse toute la vidéo : il
   relie les nœuds d'un schéma, raye ce qu'on rejette, ouvre la scène suivante.
4. **Des schémas qui se tracent** : des nœuds reliés par des traits qui se dessinent (« Claude →
   serveur → After Effects » tranché, « Katana → Prompt → Generate → Render »).
5. **La comparaison montrée** : l'ancienne méthode en pile d'étapes avec son compteur d'heures
   (2 h, 5 h, 9 h, 16 h), tranchée d'un coup ; la nouvelle en trois pastilles et « 15 s ».
6. **Des métaphores faites de la matière** : 4 812 messages qui passent dans un entonnoir et sortent
   « 1 », des tuiles qui se rangent dans un plateau, un mur de documents et une barre de recherche.
7. **Des étiquettes de fonction** : deux mots en blocs empilés (« Auto-Tracked / Task Completion »)
   posés à côté de l'interface qui le fait.
8. **Des interfaces manipulées** : un curseur qui tire des réglages, des cartes qui arrivent en 3D,
   une fenêtre qui se remplit.
9. **Le récapitulatif** : tous les plans du film en mosaïque (« This film is 9 equations »), puis le
   logo, la promesse, un bouton.
10. **Le son colle à chaque geste** : un coup sec par mot qui claque, un souffle par passage, le
    temps fort de la musique sur la révélation.

Ce que le studio ne reprend pas : leurs couleurs (la marque du client, seulement), leurs images
générées (photos, 3D réaliste : on montre sa vraie matière), leurs lueurs néon. Les recettes 23 à
33 traduisent ce langage avec le kit ; la story d'ouverture de Publicitaire IA (v3, 07/11/2026,
40 s, 9 plans, 36 mots à lire) les enchaîne : 23 → 24 → 25 → 26 → 27 + 28 → 29 → 30 → 31.

23. **La négation montrée** (3,5 s, nuit). Au lieu d'écrire « je ne l'ai ni filmée ni montée » :
    un viseur de caméra qui tourne (quatre coins, « REC » et son point, le temps qui défile), « ni
    filmée. » claque, une barre de l'accent raye le viseur (`K.barre`), qui s'éteint au gris ;
    « ni montée. » claque, une timeline de montage s'ouvre piste par piste (`K.volet`), sa tête de
    lecture avance, une barre la raye et ses morceaux tombent. Sortie : la coupe (32).
24. **La demande qui devient le film** (9 s, clair, dans l'outil). Le logo de l'outil claque, son
    nom surligné, puis il se range dans la barre de sa fenêtre ; le curseur y glisse le dossier du
    produit (une pastille pleine), le lien de sa page se colle (une pastille, jamais une adresse),
    la demande se tape, envoyer : elle monte en bulle. Les étapes de la page se cochent toutes les
    0,5 s (un anneau qui tourne, puis la coche) et l'aperçu de chacune sort de la fenêtre par la
    droite, sans cacher son étape (la vraie page, les vraies phrases, sa palette, la musique, les
    images relues). Tout se range dans le fichier, qui se charge ; « Prête » ; le curseur clique sa
    vignette et son jaune part du clic (`K.flash`).
25. **Le nom sur l'objet** (3 s, aplat). Le dossier géant grandit depuis le point cliqué, plein
    d'emblée ; son nom claque lettre par lettre (`K.lettres` + `K.claque`, 0,035 s d'écart) ; ses
    fichiers (ceux que la page promet) en dépassent un instant puis retombent. Sortie : l'aplat
    s'efface par un volet, le dossier se resserre en nœud et prend l'accent d'un coup (jamais un
    fondu de l'encre au jaune : il passerait par l'olive).
26. **Le schéma qui se trace** (3 s, nuit). Le nœud du produit, une ligne d'appui (« Tu l'installes
    dans »), les nœuds des outils claquent ; deux liens se tracent et le fil rouge les parcourt
    (`K.lien`, `K.trace`, `K.longer`), chaque outil reçoit (un petit coup d'échelle) et se coche.
27. **Le titre qui se change sur place** (5 s, nuit) : « Ton lien. » ; la pastille du lien et ses
    quatre offres en rafale ; le fil descend dans le dossier ; quatre liens en partent vers quatre
    formats, chacun avec la première image d'une vraie vidéo et son étiquette ; le titre devient
    « Tes vidéos. » à la même place. Les formats flottent chacun à son temps pendant qu'on lit.
28. **La vignette qui devient la vidéo** (0,8 s) : le format choisi grandit jusqu'au plein écran
    (`scale` = largeur de l'écran / largeur de la vignette, centre amené au centre), le reste
    s'efface en flou ; à l'arrivée, la vraie vidéo joue à la racine d'`index.html`, et sa première
    image est exactement la vignette (`ffmpeg -ss 0 -frames:v 1`).
29. **La bande-démo à volets** (6,5 s). Ses vraies vidéos, l'une après l'autre, chacune dans son
    format (plein écran en 9:16, son 16:9 sur toute la largeur), avec leur étiquette sous la bande
    du sticker (« Pub » « faite avec Publicitaire IA ») ; un volet de l'accent en biais couvre
    chaque coupe (8 de rythme.md), le dernier s'arrête et devient l'aplat du prix. Jamais un
    exemple qui est lui-même un écran de texte, ni l'accroche « problème » d'une pub.
30. **Le prix en deux temps** (5 s, aplat). « 67 € » claque en très grand (jamais un compteur dont
    une valeur de passage se lirait comme un prix), « Paiement unique » s'ouvre dessous ; puis ils
    montent et se resserrent, la page du calendrier de la vraie échéance claque, et l'échéance se
    lit, la date surlignée d'un bloc d'encre.
31. **La mosaïque du film qui devient la marque** (5 s, nuit) : huit vraies images de cette vidéo
    arrivent de la profondeur, la caméra recule, elles se resserrent au centre et deviennent
    l'avatar et le nom ; l'appel claque juste au-dessus de la bande du sticker, son point final est
    le point de la marque qui bat la mesure.
32. **La coupe** (transition, 0,6 s) : `K.tranche(tl, calque, t)`, appelée en dernier : un trait de
    l'accent traverse l'écran en biais, le calque se fend et ses deux moitiés tombent, le fond
    d'après apparaît. Sur un temps fort (juste avant l'entrée de la musique).
33. **La pile contre les pastilles** (comparaison, 5 s) : l'ancienne méthode en étapes empilées une
    à une avec un compteur qui grimpe (en heures, d'après la page), le fil rouge la tranche et elle
    tombe ; à sa place, les étapes de l'offre en trois pastilles reliées et leur vrai délai. Vrais
    chiffres seulement (les alternatives et `recoit` de la fiche).

## Ouvrir : le problème qu'on vit

1. **La corvée** (8 à 9 s, fond sombre). L'outil pénible d'avant en grand et en perspective
   (une timeline de montage, un tableur, une boîte mail débordante), **ses vrais logos** qui
   flottent autour, nets. Un mot par temps, en très gros (« Couper. » « Sous-titrer. » « Les
   bruitages. » « Recadrer. »), et à chaque mot l'outil se charge un peu plus. Puis tout passe au
   flou et un **compteur** dit le prix de la corvée (« 0:00:00 » → « 3:00:00 » qui vire à la
   couleur d'accent), avec l'outil et le contexte dessous (« sur CapCut, pour un seul Reel. »).
   Enfin le ressenti : « Épuisant. » tombe lourdement, s'écrase, et les logos chutent avec lui.
   Sortie : la caméra recule et un disque clair envahit l'écran.
2. **La question tapée** : le problème s'écrit dans un champ de saisie, l'offre y répond.

## Le pivot et le nom

3. **Le choix de l'outil** (5 à 6 s, fond clair). Une ligne en deux temps (« Ton nouveau
   **monteur** » → « c'est ton **IA.** » surligné), les tuiles des outils montent de la
   profondeur (ChatGPT, Codex, Claude), le curseur les survole une à une (chaque tuile se
   soulève), clique celle qu'on montre : les autres tombent, **la couleur d'accent part du clic**
   et envahit l'écran ; le nom de l'offre se forme lettre par lettre, en très gros, avec une
   petite ligne dessous (« avec Claude ou ChatGPT » et leurs logos).
4. **Le nom qui se construit** [logo-assemble-lockup] : les objets du début se rassemblent en
   nom ou en logo.

## Montrer le produit en action

5. **La couleur devient l'interface** (raccord, 1 s). Le plein écran de couleur est la fenêtre
   de l'application, vue de très près ; la caméra recule et pivote, la couleur s'efface par un
   volet net, l'interface apparaît dessous.
5 bis. **Le produit entre dans l'outil** (1,7 s), juste après l'arrivée de l'interface et avant
   de s'en servir : une fenêtre Finder (thème clair, barre latérale, dossiers bleus du Mac) glisse
   sur le côté, le curseur sélectionne le dossier du produit (« Monteur IA », surligné en bleu),
   le fait glisser jusqu'au champ de l'outil, et l'étiquette du dossier y apparaît ; le Finder
   repart. Le spectateur comprend l'enchaînement : son IA, le produit qu'on y met, puis ce qu'on
   lui demande. Même idée pour une extension qu'on ajoute, un compte qu'on connecte.
6. **La démo dans l'outil** (8 à 10 s). Dans l'interface reconstruite (ex. Claude : barre
   latérale, « Quoi de prévu, Alex ? », champ de saisie, dossier du projet en étiquette à la
   couleur de la marque) : le curseur **glisse un fichier** depuis l'extérieur jusqu'au champ, la
   caméra **zoome sur le champ**, on **tape** la demande en moins d'une seconde, clic sur envoyer ;
   la caméra recule, la bulle de la demande monte, la réponse arrive et **chaque étape se coche**
   toutes les 0,6 s pendant que **son aperçu sort de la fenêtre** et flotte en 3D sur le côté
   (une carte par étape). Le fichier final apparaît, le curseur clique dessus : flash de couleur.
7. **Le chapitre et la plongée** (1,4 s + la démo). Sur fond de couleur d'accent : mot géant
   pâle qui glisse, étiquette nette, interrupteur ; le curseur l'active, on plonge à travers vers
   la démonstration de la fonction. Le motif revient pour chaque fonction.
8. **La transformation mesurée** (3 à 4 s). La matière brute en grand (une bande de 3:50), les
   défauts se marquent un à un en rouge avec leur étiquette (« raté », « blanc »), disparaissent,
   le reste se resserre, le compteur descend (« 3:50 » → « 0:42 »). La bande courte devient
   l'objet suivant (un téléphone qui monte).
9. **Les réglages qui volent dans le résultat** (4 s). Le résultat à gauche (un téléphone), un
   titre court à droite (« Ton **style** », « appris une seule fois. »). Des pastilles arrivent
   une à une à droite (« Ta couleur », « Ta police », « Tes sous-titres », « Ta musique ») puis
   volent dans le téléphone, et chacune s'y applique à l'arrivée.
10. **La retouche en une phrase** (2,5 s). Une bulle où l'on tape (« Le titre plus gros. »), le
    titre grossit dans le résultat, la réponse arrive avec une coche (« C'est fait. »).
11. **Clic guidé** [cursor-ui-demo] et **interface dans un téléphone** [device-surface-showcase]
    pour d'autres produits.

## Comparer

12. **L'écran coupé** (5 s). Un volet clair pousse la moitié droite. À gauche, sombre : « À la
    **main** », l'outil d'avant qui se remplit, le curseur qui s'agite, un chrono qui file
    jusqu'à 3:00:00 et vire au rouge. À droite, clair : « Avec **ton IA** », le résultat, une
    bulle de demande, une pastille « Prêt · 0:42 », « Quelques **clics.** ». Sortie : le panneau
    clair glisse sur toute la largeur, le résultat revient au centre.
12 bis. **Le balai dans le téléphone** (6,5 s, vertical). Un téléphone au centre montre la
    prise brute (une image de la vraie vidéo), une mini ligne de temps en bas ; une tête de
    lecture blanche la balaie et chaque raté s'allume à son passage (étiquettes rouges « raté »,
    « blanc », en quinconce pour ne pas se toucher). Sur le temps fort de la musique, un balai
    jaune traverse l'écran de droite à gauche et révèle le Reel monté, qui **joue vraiment**
    (une `<video>` posée à la racine de `index.html`, aux coordonnées exactes de l'écran du
    téléphone, avec pour vignette l'image exacte de son premier instant joué). L'étiquette passe
    de « Avant · brut 3:50 » à « Après · monté 0:42 », puis ce que l'IA a fait arrive en puces
    qui **chevauchent le bord du téléphone** (jamais collées au bord de l'image, hors zone sûre).
    Sortie : le téléphone rétrécit et devient la carte centrale de l'éventail (14).
13. **La comparaison des options** [comparison-split] : monteur, agence, faire seul, l'offre ;
    vrais chiffres seulement.

## Prouver

14. **L'éventail des vrais résultats** (2,5 s). Le résultat central rétrécit, ses voisins (les
    vrais Reels, les vraies pages) arrivent des deux côtés en éventail ; sous **chacun**, une
    pastille de vues compte jusqu'à son vrai chiffre (demande au client ceux qui manquent : une
    carte sans chiffre fait trou). Les vrais logos de la plateforme flottent autour.
15. **Le grand chiffre** (2 s). Les résultats s'écartent et passent au flou ; le total compte au
    centre en énorme (« +3,3 M », « de vues »), arrondi vers le bas, fidèle à la fiche.
16. **Les vrais messages** (3 s). **Toutes** les captures de témoignages de la page (7 dans la
    démo, pas 4) arrivent de la profondeur une à une autour d'un compteur (« +190 », « créateurs
    l'utilisent déjà »), chacune avec un petit bruitage, puis dérivent. Garde-les dans le cadre
    même quand la caméra est zoomée (une carte coupée au bord fait négligé).

## L'offre et le prix

17. **Le travelling des stations** (4,5 s) [spatial-pan-stations]. Ce qu'on reçoit, posé sur
    une longue toile, la caméra glisse de station en station : chaque station a son titre court,
    sa pastille de délai (« prêt en 1 minute ») et sa matière animée (le dossier qui se remplit,
    les 21 skills qui tombent en vrac puis se rangent, les miniatures de la formation qui
    arrivent). Puis la caméra recule pour tout voir et passe au flou.
18. **Les bonus en pluie** (2 s). « Et les **bonus** », les pastilles des bonus tombent en
    place, chacune avec son icône, et dérivent.
19. **Le prix en plein écran** (3,5 s, fond couleur d'accent). Le prix en énorme, puis la ligne
    d'appui (« **Paiement unique,** accès à vie. ») ; un trait sous le prix qui s'allonge pendant
    la tenue. Deux entrées possibles : le prix qui compte jusqu'à sa valeur, ou **l'ancrage qui
    dégringole** (« 1 997 € » tient 0,4 s, puis descend jusqu'à « 97 € », qui claque avec un
    boom). L'ancrage seulement avec un chiffre que le client fournit (`prix.barre` dans la fiche) ; s'il ne correspond à aucun prix réellement pratiqué, préviens-le
    une fois du risque (en Europe, une réduction annoncée doit se référer au prix le plus bas des
    30 derniers jours) et laisse-le décider. Sortie : un disque sombre part du centre.
20. **L'échéance en rouleau** [vertical-spring-ticker], seulement avec une vraie date.

## Finir

21. **La mosaïque qui devient le bouton** (6 à 7 s). Tout ce qu'on a vu revient en mosaïque 3D
    (vignettes d'interface, résultats, prix, le nom), la caméra recule et se redresse, puis tout
    se resserre au centre et devient un bouton détouré ; le curseur arrive et clique, le bouton
    se remplit de la couleur d'accent, le nom de l'offre au-dessus, une petite ligne dessous.
    Tenu 2,5 s avec des objets qui dérivent.
22. **Le bouton pressé qui envahit l'écran** [cta-morph-press] pour un Reel (« Commente MOT »).

## Combiner

La vidéo de page de démonstration enchaîne : 1 (la corvée) → 3 (le choix, le nom) → 5 + 5 bis + 6
(le dossier Monteur IA glissé dans Claude, puis la démo) → 7 + 8 (chapitre Dérushage) → 9 + 10 (le style, la retouche) → 12 (l'écran
coupé) → 14 + 15 + 16 (la preuve) → 17 + 18 (l'offre) → 19 (le prix) → 21 (le final). Chaque
recette part d'un objet déjà à l'écran : rien n'apparaît sans cause.

La pub verticale de démonstration (30 s, `pub`) en reprend le cœur, remis en page pour le
téléphone : 1 (« 3 heures sur CapCut pour un Reel ? », lisible dès la première image) → 3 (le
choix, le nom) → 5 bis + 5 + 6 (« Monte cette vidéo. » dans Claude) → 12 bis (avant/après) → 14
+ 15 (la preuve) → 19 sans ancrage (le nom, le prix, « Découvre-le » et une flèche vers le bouton
de la pub). Six scènes de 2,5 à 8,5 s ; la démo est la plus longue, c'est l'angle.
