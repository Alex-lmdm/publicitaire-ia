# Le style : vivant, dense, à sa marque

Une vidéo du studio doit avoir le niveau d'une vidéo de lancement produit faite par un
studio de motion design : **beaucoup de choses montrées, très peu de texte**, des interfaces que
les gens reconnaissent, des fonds qui changent, rien qui fasse vide. Le test : on coupe le son,
on ne lit presque rien, et on a compris ce que fait l'offre.

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

## Des fonds qui alternent, jamais un aplat vide

Ses Reels ont peut-être un fond uni : une vidéo de motion design, non. Le fond est un acteur.

- **Quatre fonds qui alternent**, à partir de sa marque : sombre (sa couleur de fond, avec une
  grille fine, `k-fond-sombre`), clair (blanc cassé avec grille, `k-fond-clair`), **sa couleur
  d'accent en plein écran** pour les temps forts (le nom de l'offre, les chapitres, le prix,
  `k-fond-jaune` ou son équivalent), et l'écran coupé sombre / clair pour un avant / après.
  Au moins trois bascules par minute, chacune avec une cause (un clic, un volet, un objet).
- **Des objets qui flottent seulement quand ils ont un sens, et seulement de vrais logos**
  (`K.champ` avec `K.tuileMarque`) : le logo de l'outil dont on parle, dans ses vraies couleurs
  (CapCut autour de la corvée du montage « sur CapCut », Instagram autour des Reels et de leurs
  vues, Claude et ChatGPT sur l'écran final « avec Claude ou ChatGPT »). Ils sont **nets** pour
  la plupart, pour qu'on reconnaisse l'outil au premier coup d'œil (au plus un, tout près, flou),
  assez grands (80 à 240 px en 1920), et laissent libre la zone du sujet. **Disperse-les avec une
  vraie profondeur** : quelques petits au loin (60 à 90 px, légèrement flous), des moyens nets
  (100 à 150 px), un ou deux très grands et flous au premier plan, à moitié hors champ dans un
  coin. Jamais collés aux mots ni au sujet : place-les à la main (x, y, taille, flou) quand le
  champ automatique les tasse près du texte, et vérifie sur les images clés à toutes les échelles
  de la caméra (retour du créateur, 12/10/2026). **Jamais d'icônes génériques** (ciseaux, note de musique, éclair, étoile) :
  elles font « inventé ». Une scène sans logo pertinent n'a pas d'objets flottants : elle vit par
  sa caméra, son interface et ses textes (retour du créateur, 12/10/2026).
- Une vignette discrète sur les bords donne de la profondeur au sombre (`k-vignette`).

## Des interfaces, pas des slides

Ce qui se montre, du plus fort au plus faible :

| Il a | Tu fais |
|---|---|
| Un logiciel, une app, un outil d'IA qu'on pilote | L'interface reconstruite en HTML d'après capture, animée : on glisse un fichier, on tape, on clique, elle répond |
| Un produit qui vit dans un outil connu (Claude, ChatGPT, Notion…) | L'interface de cet outil, reconnaissable (sa barre latérale, son champ de saisie, ses couleurs), et le produit qui y travaille |
| Une formation | L'espace de formation, les vidéos du programme (vraies miniatures), les modules qui tombent en place |
| Des résultats réels (ses Reels, ses ventes, ses avant / après) | Les vraies images, en éventail, en mosaïque, dans un téléphone, avec leurs vrais chiffres qui montent |
| Des témoignages en capture | Les vraies captures, en cartes qui arrivent de la profondeur |
| Rien que deux phrases | Une vidéo typographique à sa marque, mais vivante (objets, fonds qui alternent). Dis-lui ce qu'une capture apporterait |

Fidèle, pas littéral : simplifier une interface pour qu'elle se lise (agrandir le bouton utile,
réduire une liste à cinq lignes, retirer la navigation) oui ; inventer une fonction ou un écran
que le produit n'a pas, non. Une simplification se note dans `sources/NOTES.md`. Les noms, les
chiffres et les textes visibles dans une interface sont vrais (de la fiche ou de la capture).

## La typographie

- 1 à 4 mots par écran ; le reste se montre (`rythme.md`).
- Deux graisses de sa police : léger et grisé pour l'appui, gras pour le mot qui compte.
- Le mot clé à la couleur de la marque, ou surligné d'un bloc de cette couleur.
- Les très grands chiffres (un compteur, un prix) occupent l'écran, sur un fond flou.
- Un mot géant et pâle en fond, l'étiquette nette devant : le motif des chapitres.

## Ce qui trahit une vidéo faite par IA (à ne jamais faire)

| Interdit | À la place |
|---|---|
| Une suite d'écrans de texte posés sur le même fond uni | Des interfaces et des objets en mouvement, des fonds qui alternent |
| Des phrases complètes à l'écran, des listes à puces | 1 à 4 mots, le reste montré |
| Grand titre centré sur un dégradé, trois cartes qui flottent sans rapport avec l'offre | Les objets du sujet, les vraies interfaces |
| Halos néon, reflets d'objectif, sol quadrillé lumineux, ondes de choc, particules génériques | Des objets du sujet floutés par la profondeur ; la grille fine du kit |
| Texte en dégradé, contours lumineux, machine à écrire sur une phrase entière | Texte plein ; la frappe seulement dans un champ de saisie |
| Emoji comme icônes | Les icônes du kit (Lucide) dans une interface, les logos des outils |
| Des icônes génériques qui flottent dans toutes les scènes | De vrais logos, dans leurs couleurs, seulement là où ils renvoient à ce qu'on dit |
| Fausse interface vague dans un faux navigateur | L'interface réelle, reconstruite d'après capture |
| Fondus enchaînés entre deux écrans | Un objet qui devient le suivant, un flash, un volet |
| Le même enchaînement d'une vidéo à l'autre | Change l'angle, les interfaces, les motifs et au moins trois réglages (fonds, cadrages, transitions, tempo) d'un client à l'autre |

Test final : si cette vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom,
elle est trop générique. Recommence par ce que son offre a de visible.
