# La bibliothèque d'effets

Des effets éprouvés pour des annonces verticales. La plupart existent déjà comme recettes dans le
skill `hyperframes-animation` de Monteur IA (nom entre crochets : cherche-le dans
`blueprints-index.md`, `rules-index.md` ou `techniques.md` du skill). **Lis la recette avant de
coder** : elle donne la technique, pas le style. Le style vient de `style.md`.

Une story = un seul effet principal. Un Reel = trois ou quatre effets au plus, qui se répondent.

## Accroche et texte

1. **Accroche mot par mot sur les temps** [kinetic-type-beats]. Chaque mot arrive sur un temps,
   puis la phrase entière tient. Pour l'accroche du Reel.
2. **Texte qui monte d'une ligne-masque** [animate-text]. Chaque ligne sort d'un masque,
   décalée de 60 à 120 ms. Le plus sûr pour une promesse.
3. **Une ligne sert de masque à la suivante.** La phrase sortante découpe l'entrante. Pour
   enchaîner deux idées sans transition.
4. **La question tapée, l'offre y répond.** Le problème de l'audience se tape (en quelques
   étapes), puis la réponse arrive. Pas de recette toute faite : champ de saisie en HTML,
   frappe en étapes déterministes.

## L'offre et son contenu

5. **Ce que tu reçois en grille** [grid-card-assemble]. Les éléments de `recoit` et `bonus`
   s'assemblent en grille, le nom de l'offre au centre.
6. **Modules en éventail** [split-tilt-cards]. Les cartes des modules s'écartent en légère
   perspective. Pour une formation.
7. **Pastille qui grandit** [card-morph-anchor]. « Inscription » devient le programme, puis les
   modules : un seul objet qui se transforme.
8. **La page de vente dans un téléphone** [device-surface-showcase]. La vraie capture défile
   dans un cadre de téléphone qui recule. Pour la révélation.
9. **Clic guidé** [cursor-ui-demo]. Le curseur va sur « Rejoindre », la page réagit, le zoom
   suit. Pour une story d'ouverture ou un logiciel.
10. **Avant / après en volet** [comparison-split]. Le même cadre, sans puis avec l'offre.
11. **Liste qui se coche au rythme.** Les éléments de `recoit` se cochent un par un. Pour un
    teaser ou une relance.
12. **Parcours en pastille** : Inscrit ✓, Module 1, premier résultat. Toujours la même forme,
    son contenu change.

## Prix, preuve, échéance

13. **Prix barré, puis le trait souligne le vrai prix** [svg-path-draw]. Seulement si
    `prix.barre` existe dans la fiche.
14. **Compteur qui monte** [dataviz-countup]. Sur un vrai chiffre de `preuves`, arrondi vers le
    bas. S'arrête net, puis tient.
15. **Échéance en rouleau** [vertical-spring-ticker]. « J-3 », « Ce soir minuit » : les chiffres
    tournent puis se posent. Seulement avec `dates.fermeture`.
16. **Mur de témoignages balayé** : les vrais témoignages de la page, une ligne de lecture en
    retient un, mot pour mot.

## Clôture

17. **Bouton pressé qui envahit l'écran** [cta-morph-press]. Le bouton (couleur d'accent)
    s'enfonce puis remplit le cadre, qui devient l'écran final. La couleur dépasse les quatre
    coins, sinon on croit à un flash.
18. **Le fil rouge devient la signature** [logo-assemble-lockup]. L'élément d'accent du début
    (un point, un trait) revient former le nom ou le logo du créateur à la fin.
19. **Rafale de ce qui est livré** (1,5 s au plus) : les éléments de l'offre défilent vite et
    s'arrêtent sur le principal. Pour une story.
20. **Révélation par masque** : la couverture de l'offre apparaît par un iris ou un volet.

## Combiner

Un Reel solide tient souvent en : une accroche (1 ou 2), un fil (5, 8 ou 10), une révélation
(8 ou 17), une preuve ou un prix (13 ou 14), l'écran final. Chaque effet doit partir d'un élément
déjà à l'écran : rien n'apparaît sans cause.
