# Le style : vivant, dense, à sa marque

Une vidéo du studio doit avoir le niveau d'une vidéo de lancement produit faite par un
studio de motion design : **ce qu'on voit raconte, et quelques mots très grands le ponctuent** :
ses vraies interfaces qui agissent, le schéma de son mécanisme qui se trace, ses vraies vidéos, ses
vrais chiffres, des fonds qui changent, rien qui fasse vide. Le test : on coupe le son, on regarde
sans se presser, et on a compris ce que fait l'offre, pour qui, et quoi faire, sans avoir lu plus
d'un mot par seconde.

## Trois niveaux d'identité

1. **La marque du client** porte la vidéo : couleurs, polices et logo de `marque.json`, déjà
   dans `brand/` du projet (`var(--brand-bg)`, `var(--brand-accent)`, `var(--brand-secondary)`,
   `var(--brand-font-display)`…, et `brand/logo.*` s'il en a un). Jamais une couleur ou une police
   de marque écrite en dur.
2. **Les surfaces de son offre** gardent leur propre identité : sa page, son espace de formation,
   son logiciel, dans leurs vraies couleurs et polices (relevées dans la capture).
3. **Les outils tiers** qu'il utilise ou dont sa page parle (Claude, ChatGPT, Notion, Canva,
   CapCut, Instagram…) gardent leurs logos, leurs couleurs et leur allure. Ce sont des repères
   que l'audience connaît : montre-les (`studio_motion.py logos` pose leurs logos).

Si sa marque n'est pas encore réglée (`marque.json` absent : style de départ noir et blanc),
règle-la d'abord avec `marque.md` : une question sur la source, puis son accord. Aucune question
de code couleur ou de nom de police : il valide un aperçu.

## La palette : ses couleurs, rien d'autre

Tout ce que la vidéo dessine (fonds, textes, formes, traits, dégradés, lueurs) prend ses couleurs
dans `brand/tokens.css`, et seulement là :

- ses couleurs : `--brand-bg`, `--brand-surface`, `--brand-text`, `--brand-muted`,
  `--brand-accent`, `--brand-secondary`, `--brand-contrast` (le texte posé sur l'accent) ;
- la nuit et le jour de ses styles : `--brand-sombre` (sa couleur la plus sombre, pour tous les
  fonds de nuit) et `--brand-clair` (la plus claire) ;
- des gris entre les deux (`--brand-gris-1` à `--brand-gris-4`), du noir, du blanc, et ces
  neutres en transparence (une grille en blanc à 5 %, une ombre noire).

Les dégradés se font entre neutres (du noir au gris, du sombre au gris), jamais vers l'accent ni
depuis lui. L'accent se pose **plein** : jamais en transparence sur un fond sombre (ni en fondu ni en flou
à son entrée : le temps de l'effet, il vire à l'olive, essai du style 2 du 06/11/2026), jamais mélangé
au noir ou au gris, jamais dérivé (`oklch(from …)`, `color-mix` avec l'accent, une « nuit »
teintée) : un jaune assombri devient brun, olive ou orangé, et la vidéo n'est plus à sa marque
(story refusée du 06/11/2026, des couchers de soleil bruns tirés de son jaune). Pour un trait
discret, un gris ou du blanc en transparence ; pour un trait de marque, l'accent plein et fin.

Seules ses **vraies captures** (sa page, son produit, ses vidéos, ses résultats) et les **logos de
ses outils** gardent leurs propres couleurs. `studio_motion.py palette exports/<vidéo>.mp4` relève
tout le reste à la revue.

## Aucune image inventée : sa vraie matière, dans cet ordre

Ce qui se montre vient du client ou de ses outils. Jamais un paysage, un ciel, une planète, une
sphère, une gravure, un tableau peint, une photo d'ambiance ou un objet décoratif dessiné pour
l'occasion : ils font « vidéo d'IA » et sortent de sa palette.

Pour chaque phrase du script, ce qu'on voit pendant qu'on la lit se cherche en descendant cette
échelle ; prends le premier barreau qui existe pour cette phrase :

1. **Une vraie capture** : sa page, son produit, son espace de formation, un résultat, un message
   reçu, une vraie vidéo (`sources/`, `assets/`).
2. **Son interface reconstruite** d'après capture, animée : on tape, on clique, elle répond.
3. **Un vrai chiffre** de `OFFRE.json` mis en scène : un compteur qui monte, une barre qui se
   remplit, un prix qui se pose, avec son contexte.
4. **Le schéma de son vrai mécanisme** : des nœuds (sa page, son produit, l'IA, les formats livrés)
   reliés par des liens qui se tracent, le fil rouge qui les parcourt (`K.lien`, `K.trace`,
   `K.longer`). Il explique « comment ça marche » sans une phrase ; chaque nœud est vrai.
5. **Les vrais logos nus** des outils que l'offre nomme, 6 à 8 (`studio_motion.py logos`).
6. **Sa typographie seule** : ses vrais mots, en grand, qui jouent ce qu'ils disent.

Une forme simple à ses couleurs (un disque, un aplat, une case, un cadre, un trait) sert de
**cadre** (elle porte une capture, un chiffre, un logo, un mot), de **transition** (elle couvre,
s'ouvre, devient l'objet suivant) ou de **fil rouge** (le point de sa couleur qui raye, parcourt un
lien, devient le point final) : **jamais de sujet d'un plan**. Une image clé dont le seul sujet
est une forme ou un aplat pendant plus d'une seconde est un défaut, sauf la carte de fin et une
transition (essais des styles 2 et 4 du 06/11/2026 : des disques, des carrés et des ronds seuls à
la place des objets de l'original, une vidéo qui ne montre plus rien). Un style dont l'original
montrait des images (paysages, photos, objets) les remplace par le plus haut barreau disponible.
S'il manque une matière importante, c'est la question unique du repérage
([reperage.md](reperage.md)), pas une forme de plus.

## Des fonds qui alternent, jamais un aplat vide

Ses Reels ont peut-être un fond uni : une vidéo de motion design, non. Le fond est un acteur.

- **Quatre fonds qui alternent**, à partir de sa marque : sombre (sa couleur de fond, avec une
  grille fine, `k-fond-sombre`), clair (un blanc à peine gris, avec grille, `k-fond-clair`), **sa couleur
  d'accent en plein écran** pour les temps forts (le nom de l'offre, les chapitres, le prix,
  `k-fond-jaune` ou son équivalent), et l'écran coupé sombre / clair pour un avant / après.
  Au moins trois bascules par minute, chacune avec une cause (un clic, un volet, un objet).
- **Des objets qui flottent seulement quand ils ont un sens, et seulement de vrais logos, nus**
  (`K.champ` avec `K.logoNu`) : le logo seul, **sans tuile ni fond**, dans ses vraies couleurs,
  de l'outil dont on parle (CapCut autour de la corvée du montage « sur CapCut », Instagram autour
  des Reels et de leurs vues, Claude et ChatGPT sur l'écran final « avec Claude ou ChatGPT »). Leur
  rôle : **combler les zones vides** d'un écran, sur certaines scènes ; ailleurs, le vide est bien.
  Quand ils sont là, **6 à 8**, pas 3 (huit Instagram autour d'un DM, par exemple) : la plupart
  **nets**, pour qu'on reconnaisse l'outil au premier coup d'œil, quelques-uns flous. **Disperse-les
  avec une vraie profondeur** : quelques petits au loin (60 à 90 px, tailles données pour une largeur de 1920 ; en vertical, à proportion de 1080, légèrement flous), des
  moyens nets (100 à 150 px), un ou deux très grands et flous au premier plan, à moitié hors champ
  dans un coin. Jamais collés aux mots ni au sujet, hors de la bande du sticker : place-les à la
  main (x, y, taille, flou) quand le champ automatique les tasse près du texte, et vérifie sur les
  images clés à toutes les échelles de la caméra. Pas de logos là où l'écran montre déjà les
  marques (un téléphone avec Instagram, les icônes des applis de partage) : ça charge ; et les
  écrans de révélation restent nus (retours du créateur, 12/10/2026). **Jamais d'icônes
  génériques** (ciseaux, note de musique, éclair, étoile) : elles font « inventé ». Une scène sans
  logo pertinent n'a pas d'objets flottants : elle vit par sa caméra, son interface et ses textes.
- Le contexte se montre par l'interface plutôt qu'en titre : pour « un client m'a écrit », un
  téléphone, la notification Instagram, l'appli qui s'ouvre sur le message. Ne redis pas à l'écran
  un détail sans enjeu ; des logos PayPal et Stripe suffisent à évoquer l'argent.
- Une vignette discrète sur les bords donne de la profondeur au sombre (`k-vignette`).

## Des interfaces, pas des slides

Ce qui se montre, du plus fort au plus faible :

| Il a | Tu fais |
|---|---|
| Un logiciel, une app, un outil d'IA qu'on pilote | L'interface reconstruite en HTML d'après sa capture, animée : on glisse un fichier, on tape, on clique, elle répond (reconstruire sa vraie interface n'est pas inventer une image : c'est sa matière, simplifiée pour se lire) |
| Un produit qui vit dans un outil connu (Claude, ChatGPT, Notion…) | L'interface de cet outil, reconnaissable (sa barre latérale, son champ de saisie, ses couleurs), et le produit qui y travaille |
| Une formation | L'espace de formation, les vidéos du programme (vraies miniatures), les modules qui tombent en place |
| Des résultats réels (ses Reels, ses ventes, ses avant / après) | Les vraies images, en éventail, en mosaïque, dans un téléphone, avec leurs vrais chiffres qui montent |
| Des témoignages en capture | Les vraies captures, en cartes qui arrivent de la profondeur |
| Rien que deux phrases | Une vidéo typographique à sa marque, mais vivante (ses vrais chiffres mis en scène, les logos de ses outils, des fonds qui alternent). Dis-lui ce qu'une capture apporterait |

Fidèle, pas littéral : simplifier une interface pour qu'elle se lise (agrandir le bouton utile,
réduire une liste à cinq lignes, retirer la navigation) oui ; inventer une fonction ou un écran
que le produit n'a pas, non. Une simplification se note dans `sources/NOTES.md`. Les noms, les
chiffres et les textes visibles dans une interface sont vrais (de la fiche ou de la capture).

## La typographie

- Sans voix, peu de mots, en trois tailles : le **mot héros** (1 à 3 mots qui remplissent la
  largeur, `k-heros`), la **ligne d'appui** (3 à 6 mots), les **étiquettes** posées sur ce qu'on
  montre. Le reste se montre (`ecriture.md`, `rythme.md`).
- Le mot **joue ce qu'il dit** : il claque (`K.claque`), s'étire (`K.etire`), se barre
  (`K.barre`), se surligne d'un bloc plein (`K.surligner`), se change sur place, ses lettres
  tombent en rafale (`K.lettres`).
- Deux tons : le plein et l'accent (« Ton **lien.** »), ou le gris d'appui et le plein (« ni »
  gris, « filmée. » blanc). Un contour net (`k-contour`, un trait plein) pour doubler un mot plein,
  jamais une lueur.
- Les étiquettes de fonction : deux ou trois mots en blocs pleins empilés (`k-blocs`), posés à côté
  de l'interface qui le fait (« Retouches / en une phrase »).
- Les très grands chiffres (un compteur, un prix) occupent l'écran.
- Un mot géant et pâle en fond, l'étiquette nette devant : le motif des chapitres.

## Ce qui trahit une vidéo faite par IA (à ne jamais faire)

| Interdit | À la place |
|---|---|
| Une suite d'écrans de texte posés sur le même fond uni | Des interfaces et des objets en mouvement, des fonds qui alternent |
| Des sous-titres : une phrase entière par écran, en haut, au-dessus d'une petite interface, plan après plan | Le plan montre en grand ; un mot héros qui joue, une ligne d'appui au plus ; un mot à lire par seconde au plus |
| Des paragraphes, des listes à puces, des mots isolés qu'on ne comprend pas | Ce que l'idée dit, montré (l'interface qui agit, le schéma qui se trace), et ses mots qui claquent |
| Des images inventées (paysages, couchers de soleil, planètes, sphères, illustrations) | La vraie matière du client, en descendant l'échelle : capture, interface, chiffre, logos, ses mots |
| Des formes seules (disques, carrés, ronds, aplats) à la place des objets d'un style | Une forme qui porte une matière réelle, ou qui sert de transition |
| Des teintes tirées de l'accent (brun, olive, orangé), l'accent en transparence sur du sombre | L'accent plein sur des neutres : noir, blanc, gris |
| Grand titre centré sur un dégradé, trois cartes qui flottent sans rapport avec l'offre | Les objets du sujet, les vraies interfaces |
| Halos néon, reflets d'objectif, sol quadrillé lumineux, ondes de choc, particules génériques | Des objets du sujet floutés par la profondeur ; la grille fine du kit |
| Texte en dégradé, contours lumineux, machine à écrire sur une phrase entière | Texte plein ; la frappe seulement dans un champ de saisie |
| Emoji comme icônes | Les icônes du kit (Lucide) dans une interface, les logos des outils |
| Des icônes génériques qui flottent dans toutes les scènes, des logos posés sur des tuiles | De vrais logos nus, dans leurs couleurs, 6 à 8 là où l'écran a des zones vides et un sujet relié à ces marques |
| Fausse interface vague dans un faux navigateur | L'interface réelle, reconstruite d'après capture |
| Fondus enchaînés entre deux écrans | Un objet qui devient le suivant, un flash, un volet |
| Une caméra qui recadre sèchement pendant qu'on lit, pour faire du rythme | Une dérive lente pendant la lecture, un recadrage net entre deux phrases ([rythme.md](rythme.md)) |
| Le même enchaînement d'une vidéo à l'autre | Change l'angle, les interfaces, les motifs et au moins trois réglages (fonds, cadrages, transitions, tempo) d'un client à l'autre |

**Avec un style du catalogue, sa grammaire prime sur ce tableau pour la typographie et le
mouvement** : la phrase tapée du style 7 ou les longues phrases sur fond clair du style 8 sont ses
gestes, pas des fautes (revue du 03/11/2026). Jamais pour les couleurs, les images ni la lecture :
un style ne justifie aucune teinte hors palette, aucune image inventée, aucune forme seule à la
place d'un sujet, aucune phrase tenue moins longtemps que sa lecture (revues du 06/11/2026), ni
plus d'un mot à lire par seconde (07/11/2026) : la phrase tapée du style 7 et les longues phrases
du style 8 se gardent pour un ou deux plans, pas pour toute la vidéo.

Test final : si cette vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom,
elle est trop générique. Recommence par ce que son offre a de visible.
