# Écrire ce qui s'affiche (et ce qui se dit)

Le motion design qui décore vend mal : dans l'étude Motion de 578 750 publicités Meta
(septembre 2025 à janvier 2026), l'animation seule gagne dans 4,6 % des cas, quand le texte clair
(11,6 %), l'annonce d'une nouveauté (11,4 %) ou d'une promo et le prix d'ancrage gagnent plus de
deux fois plus souvent. **Le mouvement sert le message et la démonstration, jamais l'inverse.**

**Sans voix (le cas par défaut), le texte est le script.** C'est lui qui raconte ; l'image prouve
ce qu'il dit (l'interface en action, le résultat, la vraie capture). Une vidéo qui enchaîne des
mots isolés et des chiffres (« C'est ouvert. » « Ma pub la plus rentable. » « 2 976 € de
ventes. » « Prix de lancement. ») ne dit rien à quelqu'un qui ne connaît pas l'offre : c'est la
story d'ouverture refusée par le créateur le 06/11/2026 (« on n'a rien compris, on ne sait pas
ce qui s'est passé »). Court ne veut pas dire elliptique : chaque écran porte une phrase entière,
qu'on comprend seule.

Le client est le créateur ; tu écris dans **sa** voix (relis sa page de vente, ses légendes s'il
y en a dans le dossier). Le tutoiement suit le sien. Les phrases de sa page sont déjà validées par
lui : reprends-les quand elles disent ce qu'il faut (« Ton offre est bonne. Encore faut-il qu'on
la voie. »), plutôt que d'en inventer de moins bonnes.

## Le script : écrire pour un inconnu (étape 3 bis du skill)

Le script s'écrit **avant** les scènes, le style et la musique, et le client le valide.

1. **Écris-le d'abord comme tu le dirais.** Imagine que tu présentes l'offre à voix haute, en
   45 secondes, à quelqu'un de son public qui n'a jamais entendu parler du créateur ni du produit.
   Écris ce texte d'un trait, dans sa voix, en suivant les blocs de la structure
   ([structures.md](structures.md)).
2. **Découpe en phrases** : une idée par phrase, une phrase par écran, 3 à 10 mots (12 au plus,
   sur deux lignes). Une phrase trop longue se coupe en deux écrans qui se suivent et se lisent
   d'un seul mouvement (« Tu donnes le lien de ta page. » puis « Il en fait des vidéos qui
   vendent. »).
3. **Chaque bloc a sa phrase.** En particulier : pour qui ; le problème et ce qu'il coûte ; ce que
   c'est (le nom de l'offre ET ce qu'elle fait, dans la même phrase ou la suivante) ; comment ça
   marche (deux ou trois phrases d'étapes, montrées) ; la preuve avec son contexte ; l'offre ;
   l'appel. Un nom seul (« Publicitaire IA. ») n'explique rien : « Publicitaire IA installe un
   publicitaire dans ton Claude ou ton ChatGPT. »
4. **Chaque chiffre porte son contexte**, sur le même écran ou celui d'avant : quoi, pour quel
   produit, sur quelle période, et ce qu'il veut dire. « 2 976 € » seul ne dit rien ; « Ma pub pour
   Monteur IA, faite avec lui : 2 976 € de ventes pour 239 € de pub. » se comprend.
5. **Aucun mot que son public n'emploie pas**, ou alors expliqué : « 12 € de ventes pour 1 € de
   pub » plutôt que « ROAS 12,47 » ; « une vidéo animée » plutôt que « du motion design » s'il ne
   le dit pas lui-même. Les mots d'une interface montrée (une colonne « ROAS » dans la capture
   Meta) peuvent rester : la phrase au-dessus dit ce qu'ils veulent dire.
6. **Pour chaque phrase, ce qu'on voit pendant qu'on la lit.** La phrase dit, l'image prouve : la
   demande tapée dans la vraie interface, la fiche qui se remplit, la pub qui tourne, la ligne de
   la capture Meta entourée. Une phrase sans rien à montrer reste courte.
7. **La tenue** : `studio_motion.py lecture "<phrase>"` pour chacune ; la somme donne la durée.
   Trop long pour le support : retire la phrase la moins utile, ou montre-la au lieu de l'écrire ;
   n'accélère jamais.

### Le test du spectateur froid

Lis seulement les phrases, dans l'ordre, comme quelqu'un qui ne sait rien de l'offre. Il doit
pouvoir répondre, sans les images et sans le son :

1. C'est quoi ? (le nom et ce que ça fait)
2. Pour qui ?
3. Quel problème ça règle, et ce que ce problème lui coûte aujourd'hui ?
4. Comment ça marche, en une phrase ?
5. Pourquoi le croire ? (la preuve, avec son contexte)
6. Combien, et jusqu'à quand ? (quand la vidéo vend)
7. Qu'est-ce que je fais maintenant ?

Une réponse manque : une phrase manque. On l'ajoute avant de montrer le script au client. Une
vidéo d'inscription ou de nouveauté remplace 6 par « ce que j'obtiens en m'inscrivant » ou « ce
qui est nouveau ».

### Montrer le script au client

Tel qu'il sera lu, sans jargon de fabrication :

> Voici le script de ta story, environ 45 s. Chaque ligne est un écran, dans l'ordre, avec ce
> qu'on voit pendant qu'on la lit :
> 1. « La dernière vidéo qui a fait vendre ton offre, c'était quand ? » · la phrase en très grand
>    sur ton jaune (3,4 s)
> 2. « Pour en avoir une, tu as trois options. » · trois cartes qui arrivent (2,6 s)
> 3. …
>
> Dis-moi ce que tu changes (un mot, une phrase, l'ordre), ou « ok ».

## L'accroche (les 2 à 3 premières secondes)

Elle dit de quoi on parle, pour qui, et ce que le spectateur gagne à rester. Choisis selon ce que
l'audience sait déjà, sans jamais supposer qu'elle connaît le produit :

| L'audience… | Accroche | Exemple (à adapter, jamais à copier) |
|---|---|---|
| connaît le créateur, attend l'offre | L'annonce, puis aussitôt ce que c'est et pour qui | « C'est ouvert. » → « Publicitaire IA fait tes vidéos de vente avec ton IA. » |
| connaît le produit, hésite | Une objection levée, une preuve, une comparaison | « 3,3 millions de vues. Même méthode. » |
| connaît la solution, pas ce produit | Ce qui le rend différent | « Tes Reels montés par ton IA, pas par toi. » |
| connaît le problème | Le problème nommé, puis la solution annoncée | « Trois heures de montage par Reel ? » |
| ne sait pas encore qu'il a un problème | Une situation qu'il reconnaît, une question | « Pourquoi la plupart des créateurs arrêtent au bout d'un mois » |

Formules qui marchent, à remplir avec la fiche :
- « Passe de [ce que tu vis] à [résultat], grâce à [mécanisme]. » : la corvée chiffrée, puis le
  mécanisme qui la supprime, chaque étape avec sa phrase et son image
- « Je pensais que [résultat] demandait [ancienne méthode]… jusqu'à [mécanisme]. »
- « Nouveau : [fait]. [Ce que ça change pour toi]. »
- « Voici comment tu [résultat] en trois étapes. »
- « Pour [résultat], tu as trois options. [Les trois, avec leur coût.] Il y en a une quatrième. »

Préfère l'instructif à la curiosité vide : « Commence en 15 minutes » vend mieux que « Découvre le
secret ». Une question entre dans la tête ; une affirmation se juge vraie ou fausse.

Devant une audience froide (le cas par défaut) :
- ouvre sur ce qu'elle vit, pas sur une annonce ni sur le nom du produit, et sans l'interpeller
  par une étiquette (« Coachs, écoutez ») ;
- une question qui suppose déjà le problème (« La dernière vidéo qui a fait vendre ton offre,
  c'était quand ? »), jamais une question à laquelle on répond « non » ;
- aucun mot qui invite seulement à explorer (« découvre », « révélé », « le secret ») : il attire
  des curieux, pas des acheteurs ;
- l'agacement vise une cible extérieure (le devis, le week-end perdu, la méthode usée), jamais le
  spectateur.
Devant une audience chaude (après un prélancement), la preuve ou la nouvelle peut ouvrir, puis on
redit le problème en une phrase.

## Le corps

- **Pourquoi, quoi, comment** : le problème et le désir d'abord, le résultat ensuite, puis le
  comment montré en deux ou trois étapes (assez pour qu'on y croie, jamais un tutoriel). Le
  comment n'est jamais sauté : sans lui, la promesse ressemble à toutes les autres.
- **Le vrai problème**, concret, dans les mots de l'audience. « Tu postes, et personne ne voit
  ton offre » plutôt que « manque de visibilité ». Ses options d'aujourd'hui, avec leur vrai coût,
  font comprendre la valeur sans prix barré.
- **Une fonctionnalité = le problème qu'elle supprime + ce qu'on obtient.** Jamais une liste de
  fonctions. « Fonction + bénéfice + mécanisme = résultat ».
- **« Voici ce qui se passe quand tu rejoins »** plutôt que « voici ce que tu reçois ». Un module
  ne s'appelle pas « Module 3 : les hooks », il devient « Tes 3 premières secondes écrites pour
  toi ».
- **Spécifique** : un chiffre, un délai, un nom vaut mieux qu'un adjectif. Découpe une grande
  promesse en morceaux crédibles (« 20 ventes par jour » plutôt que « 1 M€ »).
- **La preuve** dans cet ordre : possible dans le monde, possible pour d'autres (qui lui
  ressemblent), possible pour toi. Le repère avant le chiffre (« Une pub Meta, 239 € de
  budget. »), puis le résultat (« 2 976 € de ventes. »), puis son contexte (quelle offre, à quel
  prix, sur quelle période) et sa traduction simple (« Environ 12 € de ventes pour 1 € de pub. »,
  des ventes, pas du bénéfice). Montre la capture datée, la dépense à côté des ventes. C'est son
  résultat à lui, jamais une promesse de revenu au spectateur (les régies suspendent les comptes
  qui en font). Jamais deux chiffres d'affilée sans repère.
- **Le prix**, quand on le montre : d'abord ce qu'on reçoit et quand on y accède, puis le prix,
  recadré (ce que coûte un motion designer, une agence, le temps perdu), jamais seul, puis la vraie
  échéance avec sa vraie raison (« Prix de lancement : 67 € jusqu'à jeudi 23 h 59. Ensuite, 97 €. »).
  Ni compte à rebours, ni places limitées, ni prolongation : une date tenue.
- **Dire ce qu'on ne dit pas, c'est laisser croire le contraire** : si c'est facile, rapide, ou
  pas technique, la vidéo le dit (« Tu n'animes rien, tu ne montes rien. »), et pour qui c'est.

## Les pièges qui font décrocher

- Vendre avant d'avoir posé le problème : le spectateur n'avance pas tant qu'il n'en a pas.
- Le jargon : un ou deux mots nouveaux au plus dans toute la vidéo, le nom du produit compris
  (« ROAS », « CPM », « créa », « motion design » se traduisent).
- Plusieurs idées dans un écran, deux chiffres d'affilée sans repère.
- Un nom de produit sans ce qu'il fait, une preuve sans contexte, un prix sans ce qu'on reçoit.
- Un appel sec, sans dire ce qui attend derrière le lien.

## Les mots à l'écran

- **Sans voix : une phrase courte et complète par écran**, 3 à 10 mots, 12 au plus, sur une ou
  deux lignes (`studio_motion.py lecture "<phrase>"` donne sa tenue et prévient au-delà). Le mot
  qui compte en gras ou surligné à la couleur de la marque. Jamais un paragraphe, jamais deux
  phrases à lire en même temps (une petite ligne d'appui sous le titre, oui).
- **Avec une voix off** : le texte souligne la voix, 1 à 5 mots (les mots clés de la phrase dite),
  plus des sous-titres si la vidéo démarre muette (page de vente, story).
- Une liste se montre en objets (pastilles, cartes, coches), 5 au plus, chacun de 2 à 5 mots, avec
  une phrase qui dit ce qu'est la liste (« Avec chaque vidéo, tu reçois : »).
- Les mots d'une interface reconstruite (une demande tapée, une étape cochée, un nom de fichier)
  ne comptent pas comme texte de la vidéo : ils font partie de ce qu'on montre, et sont vrais.
- Des mots qu'on comprend en une seconde, ceux que l'audience emploie ; aucun jargon, aucun mot
  rare ou inventé (« Bruiter. » sonnait faux : « Les bruitages. »).
- **La douleur se ressent, elle ne se constate pas.** Un chiffre seul (« 3:00:00 ») ne dit pas
  que c'est pénible : nomme l'outil et le contexte (« 3 heures sur CapCut, pour un seul Reel. »),
  puis le ressenti (« Épuisant. »), avec une image qui s'effondre.
- Verbes d'action et « tu vas… » plutôt que « imagine… » ou « regarde… ».
- Pour une vidéo de plus de 45 s : le motif des chapitres (`K.chapitre`) porte le nom de chaque
  fonction (« Dérushage », « Ton style »), pas un intitulé de partie (« Le problème »).
- Aucun tiret long, aucun emoji comme icône, pas de points d'exclamation en série.

## L'appel à l'action

Un seul, dit et écrit, adapté au support (`supports.md`). Le verbe dit ce qu'on obtient :
« Accède », « Commence », « Reçois le guide », pas « Ajouter au panier ». Une raison le
précède ou le suit (« Parce que ta première vidéo peut être prête dans l'heure. »). En story, la
phrase d'appel se pose juste au-dessus de la bande du sticker.

## L'urgence

Seulement si elle est réelle et dans la fiche : une date de fermeture, un prix qui change, un
bonus retiré à une date. Une vraie date attire (« lance-toi avant dimanche ») ; un compte à rebours
inventé fait fuir une audience qui en a déjà vu cent. Sans désir, la rareté ne sert à rien :
construis d'abord l'envie, l'échéance vient à la fin, avec ce qui se passe après (« Jeudi
23 h 59, il passe à 97 €. »).

## Avant de garder un texte

Lis chaque écran à voix haute, à ton rythme normal : s'il part avant que tu aies fini, il est trop
court. Demande-toi : « Si quelqu'un ne voit que cet écran, comprend-il quelque chose d'utile ? »
et « Ce texte pourrait-il annoncer n'importe quelle autre offre ? » Si oui à la seconde question,
il est trop générique : reviens à la fiche. Puis repasse le test du spectateur froid sur le tout.
