# Écrire ce qui s'affiche (et ce qui se dit)

Le motion design qui décore vend mal : dans l'étude Motion de 578 750 publicités Meta
(septembre 2025 à janvier 2026), l'animation seule gagne dans 4,6 % des cas, quand le texte clair
(11,6 %), l'annonce d'une nouveauté (11,4 %) ou d'une promo et le prix d'ancrage gagnent plus de
deux fois plus souvent. **Le mouvement sert le message et la démonstration, jamais l'inverse.**

**Sans voix (le cas par défaut), l'image raconte et les mots ponctuent.** Ce qu'on voit se passer
(le dossier glissé dans l'IA, la demande tapée, les étapes qui se cochent, les vidéos qui sortent)
porte le sens ; à l'écran, seulement les mots qui claquent, très grands, qui jouent ce qu'ils disent.
Deux échecs opposés, tous deux refusés par le créateur :
- **le trop peu** : des mots isolés et des chiffres sans rien montrer (« C'est ouvert. » « Ma pub la
  plus rentable. » « 2 976 € de ventes. ») ne disent rien à un inconnu (story d'ouverture refusée
  le 06/11/2026 : « on n'a rien compris ») ;
- **le trop de texte** : une phrase entière par écran, posée en haut au-dessus d'une petite
  interface, treize fois de suite (115 mots en 47 s) : « trop de texte, on a l'impression de voir
  des sous-titres, c'est phrase par phrase » (story v2 refusée le 07/11/2026). La référence qu'il a
  donnée (les vidéos de Higgsfield Katana) dit 20 à 30 mots en 30 à 40 s : tout le reste se montre.
Court ne veut pas dire elliptique : chaque plan se comprend seul, par ce qu'il montre ET ses mots.

Le client est le créateur ; tu écris dans **sa** voix (relis sa page de vente, ses légendes s'il
y en a dans le dossier). Le tutoiement suit le sien. Les phrases de sa page sont déjà validées par
lui : reprends-les quand elles disent ce qu'il faut (« Ton offre est bonne. Encore faut-il qu'on
la voie. »), plutôt que d'en inventer de moins bonnes.

## Le film : ce qu'on voit, puis les mots (étape 3 bis du skill)

Le film (on dit « le script » au client) s'écrit **avant** les scènes, le style et la musique, et le
client le valide. C'est une suite de **plans** : pour chacun, ce qui se passe à l'écran, puis les
quelques mots qu'on y lit.

1. **Écris-le d'abord comme tu le dirais.** Imagine que tu présentes l'offre à voix haute, en
   45 secondes, à quelqu'un de son public qui n'a jamais entendu parler du créateur ni du produit.
   Écris ce texte d'un trait, dans sa voix, en suivant les blocs de la structure
   ([structures.md](structures.md)). Ce texte est pour toi : il ne s'affiche pas tel quel.
2. **Pour chaque idée, demande-toi ce qu'on peut MONTRER au lieu de l'écrire.** Une idée = un plan
   de 2,5 à 6 s, avec une action que l'œil suit et qui prouve (l'échelle de la matière de
   [style.md](style.md)). Exemples tirés de la story d'ouverture v3 (07/11/2026) :

   | L'idée (ce qu'on dirait) | Ce qu'on montre à la place | Les mots qui restent |
   |---|---|---|
   | « Cette story, je ne l'ai ni filmée ni montée. » | un viseur de caméra REC qui tourne, barré d'un trait jaune ; une timeline de montage qui arrive, barrée, ses morceaux tombent | « Cette story : » « ni filmée. » « ni montée. » |
   | « Claude a écrit le script, puis l'a animée. » | la fenêtre de Claude : le dossier glissé dans la barre, la demande tapée, cinq étapes qui se cochent et leurs aperçus qui sortent de la fenêtre, le fichier qui se charge | « C'est Claude. » (le reste est l'interface) |
   | « Tu lui donnes le lien de ta page, il en fait tes pubs, tes Reels, tes stories. » | le schéma qui se trace : la pastille « ta page de vente » entre dans le dossier, quatre liens en sortent vers quatre formats, chacun avec l'image d'une vraie vidéo | « Ton lien. » qui devient « Tes vidéos. » |
   | « Pour une formation, un coaching, un logiciel ou un service. » | quatre pastilles sous le lien de la page | (les pastilles, matière) |
   | « Je m'en sers pour mes propres vidéos de vente. » | ses vraies vidéos en plein écran, l'une après l'autre | « Pub faite avec Publicitaire IA » (étiquette) |

3. **Ne garde à l'écran que les mots qui claquent.** Par plan, 0 à 8 mots à lire, hors interface :
   un **mot héros** (1 à 3 mots, très grand, qui joue ce qu'il dit) et, au besoin, une **ligne
   d'appui** (3 à 6 mots, petite, au-dessus ou dessous). Les mots d'une interface montrée (la
   demande tapée, une étape cochée, un nom de fichier, une étiquette de format) font partie de la
   matière : ils sont vrais et brefs, ils ne racontent pas à la place de l'image.
4. **Le budget de mots** : sans voix, **au plus un mot à lire par seconde de vidéo** en tout (hors
   interface), et la moitié des plans portent 0 à 3 mots. `studio_motion.py lecture "<mots du plan
   1>" "<mots du plan 2>" … --duree <s>` donne la tenue de chacun et le compte. Au-delà : montre au
   lieu d'écrire, ou retire le plan le moins utile ; n'accélère jamais.
5. **Chaque bloc a son plan.** En particulier : pour qui ; le problème et ce qu'il coûte ; ce que
   c'est (le nom de l'offre ET ce qu'elle fait : un nom seul n'explique rien, le plan doit montrer
   ce qu'il fait) ; comment ça marche (deux ou trois gestes montrés) ; la preuve avec son
   contexte ; l'offre ; l'appel.
6. **Chaque chiffre porte son contexte**, montré ou écrit, sur le même plan ou celui d'avant :
   quoi, pour quel produit, sur quelle période. La ligne Meta à côté du chiffre, la pub qui tourne
   au-dessus : le contexte peut être l'image.
7. **Aucun mot que son public n'emploie pas**, ou alors expliqué : « 12 € de ventes pour 1 € de
   pub » plutôt que « ROAS 12,47 ». Les mots d'une interface montrée peuvent rester.
8. **La tenue** : chaque groupe de mots reste le temps de sa lecture (`lecture`) ; le plan, lui,
   dure le temps de son geste. La somme donne la durée, qui tient dans celle du support.

### Le test du spectateur froid

Passe en revue les plans dans l'ordre (ce qu'on voit, puis les mots), comme quelqu'un qui ne sait
rien de l'offre et regarde sans le son. Il doit pouvoir répondre :

1. C'est quoi ? (le nom et ce que ça fait)
2. Pour qui ?
3. Quel problème ça règle, et ce que ce problème lui coûte aujourd'hui ?
4. Comment ça marche, en une phrase ?
5. Pourquoi le croire ? (la preuve, avec son contexte)
6. Combien, et jusqu'à quand ? (quand la vidéo vend)
7. Qu'est-ce que je fais maintenant ?

Une réponse manque : un plan manque (ou ce qu'il montre ne suffit pas). On l'ajoute avant de
montrer le script au client. Une vidéo d'inscription ou de nouveauté remplace 6 par « ce que
j'obtiens en m'inscrivant » ou « ce qui est nouveau ». Le relecteur neuf ([revue.md](revue.md))
refait ce test sur le rendu : c'est lui qui tranche.

### Montrer le script au client

Plan par plan, ce qu'on voit d'abord, les mots ensuite, sans jargon de fabrication :

> Voici le script de ta story, environ 40 s, en 9 plans. Pour chacun, ce qu'on voit, puis les mots
> à l'écran :
> 1. Un viseur de caméra qui tourne (REC), barré d'un trait jaune ; une timeline de montage, barrée,
>    qui tombe en morceaux · « Cette story : ni filmée. ni montée. » (3,5 s)
> 2. Le logo de Claude, puis sa fenêtre : ton dossier glissé dedans, le lien de ta page, la demande
>    tapée · « C'est Claude. » (4,5 s)
> 3. …
>
> En tout : 36 mots à lire, 0,9 par seconde. Dis-moi ce que tu changes (un mot, un plan, l'ordre),
> ou « ok ».

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
- **une situation factuelle et précise** qu'il reconnaît d'un coup : un objet concret (une pub, un
  Reel, sa page de vente), l'outil qu'il utilise, et un temps ou un prix tiré de la page (« 3 heures
  sur CapCut pour monter tes Reels Instagram ? », la pub la plus rentable de Monteur IA ; « Un
  week-end sur Canva pour une seule pub vidéo ? »). Jamais une question vague dont il faut deviner
  l'objet : « La dernière vidéo qui a fait vendre ton offre, c'était quand ? » a été refusée par le
  client (06/11/2026 : « une vidéo qui a fait vendre, tu parles de quoi ? D'une pub ? ») ;
- une question qui suppose déjà le problème, jamais une question à laquelle on répond « non » ;
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

- **Trois tailles, jamais plus** : le **mot héros** (1 à 3 mots, 130 à 400 px en 9:16, il remplit
  la largeur), la **ligne d'appui** (3 à 6 mots, 56 à 72 px), les **étiquettes** posées sur ce
  qu'on montre (« Pub », « faite avec Publicitaire IA », 30 à 40 px). Au plus 8 mots à lire sur une
  image, hors interface (`studio_motion.py lecture` prévient au-delà).
- **Le mot joue ce qu'il dit**, une fois lisible : il claque, s'étire, se barre, se surligne, se
  change sur place (« Ton lien. » devient « Tes vidéos. »), ses lettres tombent en rafale
  (`K.claque`, `K.etire`, `K.barre`, `K.surligner`, [kit.md](kit.md)). Deux tons : le plein et
  l'accent (« Ton **lien.** »), ou le gris d'appui (« ni » gris, « filmée. » blanc).
- **Jamais la mise en page des sous-titres** : une phrase en haut, une petite interface dessous,
  plan après plan. C'est la story v2 refusée (07/11/2026). Le sujet du plan est ce qu'on montre, en
  grand ; les mots s'y posent.
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
