# Le style : sa marque, son offre, rien de générique

## Trois niveaux d'identité

1. **La marque du client** porte l'annonce : couleurs, polices et mot-clé de `brand.config.json`,
   déjà dans `brand/tokens.css` du projet (`var(--brand-bg)`, `var(--brand-accent)`,
   `var(--brand-font-display)`…). Jamais une couleur ou une police de marque écrite en dur.
2. **Les surfaces de son offre** gardent leur propre identité : sa page de vente, son espace de
   formation, son logiciel restent dans leurs vraies couleurs et polices (relevées dans la
   capture). On ne repeint pas une interface aux couleurs de la marque.
3. **Les outils tiers** qu'il montre (Claude, Notion, Canva…) gardent leurs logos et leurs couleurs.

Si sa marque n'est pas encore réglée (style « neutral » de départ), utilise les couleurs de sa
page de vente pour le décor, et dis-lui qu'un `/setup visuel` de Monteur IA les fixera pour la
suite. Ne lui pose aucune question de couleur ou de police pour démarrer.

## Ce qui fait « cher » (leçons des vidéos produit d'Apple)

- **Un plan = une idée**, avec de l'air autour. Le vide fait le côté haut de gamme.
- **Fond calme** (la couleur de fond de sa marque, ou noir / blanc cassé), la couleur vit sur
  l'offre, le produit, le chiffre. Jamais une couleur vive sur une couleur vive.
- **Deux polices au plus**, celles de sa marque, les mêmes règles du début à la fin.
- **Une seule couleur d'accent**, réservée à ce qui compte : le mot-clé, le prix, le bouton.
  Trois couleurs au plus dans tout le film.
- Des coupes qu'on remarque à peine. L'effet ne doit pas se voir avant le message.

## Fidèle, pas littéral

Simplifier une interface pour qu'elle se lise sur téléphone : oui (agrandir le bouton utile,
isoler une carte, réduire une liste à trois éléments, couper la navigation). Inventer une fonction,
un écran que la page ne montre pas, un faux tableau de bord : non. Pour une capture : la garder
nette (capture assez grande, ou reconstruction en HTML de la zone qui bouge), jamais un petit
bitmap agrandi jusqu'au flou. Une simplification se note dans `sources/NOTES.md`.

Matière disponible, de la meilleure à la plus faible :

| Il a | Tu fais |
|---|---|
| Une page de vente en ligne | Capture, puis tu réutilises ses vrais textes, images, couleurs et polices |
| Des captures de son produit | Plaques fidèles pour le fixe, reconstruction HTML pour ce qui bouge |
| Le document, le template, l'ebook | Le vrai support, avec des données d'exemple cohérentes |
| Rien que deux phrases | Une annonce typographique sobre, à ses couleurs, sans fausse interface. Dis-lui ce qu'une capture apporterait |

## Ce qui trahit une vidéo faite par IA (à ne jamais faire)

| Interdit | À la place |
|---|---|
| Grand titre centré sur un dégradé, trois cartes qui flottent | Le produit, l'offre, un geste réel |
| Tout qui apparaît en fondu, l'un après l'autre | Des entrées avec déplacement, une seule à la fois, et des tenues |
| Particules, halos néon, reflets d'objectif, sol quadrillé, ondes de choc | Rien : le vide est un choix |
| Texte en dégradé, contours lumineux, effet machine à écrire sur une phrase entière | Texte plein, couleur de la marque |
| Emoji comme icônes | Les icônes de son produit, ou aucune |
| Cartes et éléments qui respirent ou oscillent en boucle | Immobile quand on lit |
| Fausse interface vague dans un faux navigateur | Sa vraie page, ou une typographie franche |
| Étiquettes et cadres décoratifs dans les coins | Rien dans les coins (c'est là qu'Instagram met son interface) |
| Le même enchaînement d'une annonce à l'autre | Change l'angle, la structure et au moins quatre réglages (fond, cadrage, transitions, tempo, typographie) d'un client à l'autre et d'un lancement à l'autre |

Test final : si cette vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom,
elle est trop générique. Recommence par l'offre.
