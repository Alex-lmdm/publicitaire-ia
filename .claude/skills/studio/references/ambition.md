# L'ambition : le niveau qu'on livre

Une vidéo du studio a le niveau d'un film de lancement fait par un grand studio de motion design
pour une marque. Le seuil n'est pas « propre » : c'est **« on la regarde deux fois »**. Cette page
donne le niveau, pas la façon d'y arriver. Le code est à toi, écrit sur mesure pour cette offre et
ce script ; les interdits ([interdits.md](interdits.md)) sont le cadre, et à l'intérieur tout est
permis.

## La vidéo qu'on ne livre pas : propre, mais plate

Une vidéo peut passer tous les contrôles et rester plate : des coupes et des fondus entre les
scènes, des interfaces posées à plat face à la caméra, deux effets de texte répétés d'un bout à
l'autre, des scènes qui entrent toutes de la même façon. C'est ce que donne une méthode suivie à la
lettre. Le même film, refait avec la même fiche, le même script et la même musique, mais en
visant le niveau ci-dessous puis en passant le premier rendu au crible (« La passe du directeur
artistique », plus bas), devient une vidéo qu'on a envie de revoir.

Le script validé fixe **ce qu'on voit et ce qu'on lit**. La façon de le montrer (les passages, la
caméra, la profondeur, la typographie, le rythme des gestes) est à toi : le client a validé un
film, pas une mise en page.

## Les principes

**1. Chaque passage est un objet qui devient le suivant.** Entre deux plans, quelque chose à l'écran
cause le passage et se transforme : le bouton cliqué envahit l'écran puis devient la barre
d'adresse ; une carte se retourne sur la suite ; une fenêtre pivote et devient un téléphone ; la
caméra plonge dans un écran et en ressort ailleurs ; des cartes se resserrent en une seule ; tout
ce qu'on a vu se rassemble en un bouton. Varie-les : une vidéo a plusieurs sortes de passages, et
jamais la même deux fois de suite. Une coupe franche reste permise, sur un temps fort, en plein
mouvement ; un fondu enchaîné entre deux mises en page, jamais.

**2. De la vraie profondeur.** L'écran est un espace, pas une page : des fenêtres qui arrivent du
fond, un anneau ou un mur d'objets en perspective, un premier plan flou qui passe, le sujet net, un
fond qui vit ; des ombres qui posent les objets ; un flou qui grandit avec la distance. Une
interface qui se redresse en arrivant vaut mieux qu'une interface posée à plat. La perspective du
navigateur (la caméra du kit) suffit, sans moteur 3D.

**3. Des mots qui jouent ce qu'ils disent.** Peu de mots, très grands, et chacun entre à sa façon :
révélé par un masque, des lettres en désordre qui se remettent en ligne, une machine à sous qui
s'arrête sur le bon mot, un compteur à rouleaux, des lettres qui viennent des objets, un mot qui
change de couleur sous le bord d'un objet qui passe, un mot qui claque, s'étire, se barre, se
surligne, tombe. Une entrée différente presque à chaque plan. Puis le mot se tient, immobile, le
temps d'être lu.

**4. Des interfaces qui vivent.** Son produit ne se montre pas en capture posée : il charge, répond,
se réorganise. Un curseur qui agit (l'état d'avant, l'approche, le clic, la réaction), une frappe,
une coche qui se dessine, un chargement, des colonnes qui changent de place, une liste qui se
remplit, un aperçu qui sort de la fenêtre et flotte à côté. Simplifier pour qu'elle se lise, oui
(noté dans `sources/NOTES.md`) ; inventer une fonction, jamais.

**5. Une caméra qui a une raison de bouger.** Elle s'approche du geste (le champ où l'on tape, le
bouton qu'on clique), plonge dans un objet pour passer au plan suivant, recule sur le résultat,
suit ce qui relie deux idées. Elle ne bouge jamais pour remplir. **Les mots sortent dès qu'ils sont
lus, pour la libérer** : pendant la lecture elle tient (au plus, le monde dérive à peine derrière
des mots restés dans leur calque) ; dès que les mots partent, elle voyage.

**6. Le flou de bougé.** Un mouvement rapide laisse une traîne dans son sens, comme filmé : il donne
du poids aux passages et de la vitesse aux arrivées. Il est réglé dans chaque projet
(`data-motion-blur` sur `#root` d'`index.html`) : écris des mouvements francs, le rendu le calcule.

**7. Des vitesses qui contrastent, sur la musique.** Une rafale, puis une démonstration qui tient
son cadre pendant que l'interface agit ; une courte pause avant la révélation ; le geste le plus
fort sur le temps fort du morceau. Une courbe par rôle, jamais la même partout.

**8. Sa vraie matière, en grand, avec des touches de couleur vraie.** Le sujet remplit le cadre :
son produit en action, ses vrais chiffres mis en scène, le schéma de son vrai mécanisme, puis
seulement ses mots. À chaque plan, demande-toi ce que son public reconnaîtrait d'un coup d'œil (une
interface qu'il utilise, un objet de son métier, la notification de son téléphone) et montre-le
avec ses vraies couleurs : une vidéo toute dans les trois couleurs de la marque fait fade. Au-delà
de 15 s, au moins trois objets connus, logos compris.

## Ce qui fait « vidéo générée »

Chacun de ces réflexes est un signe que rien n'a été décidé : tout qui entre par un fondu qui
monte, tout centré, tout en même temps ; le même `power2.out` de 0,5 s partout ; des boucles qui
flottent, pulsent ou respirent à la place d'un mouvement ; une poussée lente en fin de scène ; un
tremblement de caméra ; des halos, néons, orbes, reflets d'objectif, particules ou nuées
décoratives, dégradés violets ; trois cartes en ligne, un titre sur une capture assombrie, des
étiquettes dans les coins, des compteurs « 01 / 02 » ; la même mise en page à chaque plan (le titre en
haut, l'objet au centre, plan après plan) ; des icônes génériques à la place des vrais
logos ; le logo rangé dans un coin toute la vidéo ; le même enchaînement d'une vidéo à l'autre.

Le test final : si la vidéo pouvait annoncer n'importe quelle autre offre en changeant le nom, elle
est trop générique. Recommence par ce que son offre a de visible.

## Avec quoi tu construis

Le kit ([kit.md](kit.md)) retire de la friction (le curseur et ses clics, la frappe, les compteurs,
la caméra et son zoom, les objets connus, les mots qui claquent) ; tout le reste s'écrit sur
mesure, en GSAP et en CSS. Les scènes prêtes de `templates/scenes/` et celles des styles sont des
**exemples** ([scenes.md](scenes.md)) : prends-y un geste, un calcul, une idée, ou copie-en une et
transforme-la ; aucune n'est un passage obligé. Les repères chiffrés du métier (courbes, durées,
passages, cadre, typographie) sont dans [metier.md](metier.md), à consulter quand tu hésites.

Avec un style 1 à 8, sa grammaire décide des gestes (un style à plat reste à plat) ; cette page
garde le niveau : des passages causés, des interfaces qui vivent, des mots qui jouent, la finition.

## La passe du directeur artistique

Le premier rendu n'est jamais la livraison. Avant la revue, regarde-le comme un directeur de motion
design qui a vingt ans de films de lancement pour des marques derrière lui, et à qui l'on montre un
premier jet.

1. **Regarde le MP4 rendu**, jamais le code : depuis le projet, `python3
   ../../../tools/studio_motion.py planche exports/<vidéo>.mp4 --pas 0.5` (une image toutes les
   demi-secondes, sur plusieurs planches), dans l'ordre ; puis chaque passage de près (`npx
   hyperframes snapshot --range <début>,<fin> --frames 8`, sans flou de bougé : la traîne se juge
   sur la planche).
2. **Écris ce que tu changerais**, dans `PLAN.md`, section « Passe du directeur », plan par plan,
   sur ces points :
   - **les passages** : lesquels sont des coupes ou des fondus qui pourraient être un objet qui
     devient le suivant ?
   - **la profondeur et la 3D** : quelles interfaces sont posées à plat ? Qu'est-ce qui pourrait
     venir du fond, pivoter, s'empiler en perspective ?
   - **la typographie animée** : combien d'entrées de mots différentes ? Lesquelles se répètent ?
     Quel mot pourrait jouer ce qu'il dit ?
   - **les interfaces vivantes** : où l'interface est-elle figée alors qu'elle pourrait charger,
     répondre, se réorganiser ?
   - **la caméra** : bouge-t-elle pour une raison ? Les mots sortent-ils dès qu'ils sont lus pour la
     laisser partir ?
   - **les fonds** : changent-ils avec le film, avec une cause ? Un temps fort a-t-il le sien ?
   - **la fin** : ramasse-t-elle le film, la marque en grand sur la dernière image, qui bouge encore ?
   - **la finition** : la traîne du flou, les courbes, les ombres, les alignements, la première et
     la dernière image, le geste sur le temps fort.
   Un premier jet qui ne t'inspire que deux changements n'a pas été regardé assez durement.
3. **Applique-la**, dans les interdits et dans le script validé (ce qu'on voit et ce qu'on lit ne
   changent pas ; la façon de le montrer, si), puis `npm run check` et un nouveau rendu.
4. **Une passe suffit** avant la revue ([revue.md](revue.md)) : ne cherche pas la perfection du
   premier coup. Le client peut demander à la livraison une seconde passe, plus radicale : elle
   refait la mise en scène de chaque plan ([seconde-passe.md](seconde-passe.md)).

Le client ne voit jamais le premier jet : il reçoit la version travaillée.
