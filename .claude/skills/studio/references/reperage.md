# Le repérage : ce que la vidéo va montrer

Une vidéo de motion design produit se construit avec des images, pas avec des phrases. Avant de
choisir l'angle, fais l'inventaire de **ce qui peut se montrer** et réunis la matière. C'est
cette étape qui sépare une vidéo de niveau studio d'une suite de slides. « Ce qui peut se
montrer » ne veut pas dire « les photos de sa page » : la plupart se reconstruisent et s'animent,
et ses photos n'entrent que pour montrer le résultat ([interdits.md](interdits.md), « Pas de
diaporama de sa page »).

Elle vient juste après la porte de vérité (`offre.md`), avant la structure. Elle prend quelques
minutes et ne pose au plus qu'une question au client, dans le message de la fiche et des trois idées.

## 1. Le design de sa page

La capture de l'étape 2 donne son univers. Relève dans `PLAN.md` (partie « Repérage ») :

- sa palette réelle (fond, accent, surfaces claires), ses polices, ses formes (cartes arrondies,
  pastilles, coins), ses images signatures (ses Reels en éventail, une photo, un objet) ;
- ses sections qui sont déjà des visuels (un terminal, une maquette de téléphone, un tableau de
  bord) : elles se reconstruisent et s'animent.

## 2. L'inventaire des surfaces

Liste, avec sa source, tout ce que la vidéo peut montrer de vrai :

| Surface | Exemples | Comment |
|---|---|---|
| **Son produit** | son logiciel, son espace de formation, son template, son app | Reconstruit en HTML d'après capture, animé (on clique, on tape, ça répond) |
| **Les outils dont l'offre parle** | Instagram, Notion, Canva, Stripe, Zoom, Excel, ChatGPT, Claude | Leur logo (`studio_motion.py logos <projet> claude openai …`) et leur interface reconnaissable |
| **Le résultat** | ses Reels, un avant / après, un tableau de ventes, une page créée | Les vraies images et vidéos du dossier `sources/`, jouées dans un objet qui agit (le téléphone, la fenêtre, l'interface de la plateforme) |
| **Les preuves** | captures de témoignages, chiffres de la page | Les vraies captures, les chiffres de la fiche |
| **Le problème** | la façon pénible d'avant (un tableur, dix onglets, un agenda saturé, une boîte mail qui déborde) | Reconstruit en simple, reconnaissable, sans marque inventée |
| **Les objets connus** | tout ce que son public reconnaît d'un coup d'œil : un dossier, des fichiers, le téléphone et ses notifications, des messages, et surtout les objets de son métier (l'annonce immobilière, la montre de sport, le ticket de commande, la carte d'embarquement…) | Dans leurs vraies couleurs : ceux du kit (`K.ic("objet-dossier")`, `objet-pdf`…, `K.statut`, `K.notification`, `K.bulle`, `k-feux` : [kit.md](kit.md)), les autres construits d'après leur allure courante ou une capture ([metier.md](metier.md), « Les objets connus ») |

**Trie ses photos et ses vidéos.** Pour chacune, note dans `PLAN.md` « résultat » (elle montre son
produit en marche ou ce qu'on obtient : on la mettra en scène) ou « décor » (ambiance, portrait,
mise en scène, banque d'images : elle reste hors du film). Une page qui n'a que du décor n'est pas
une matière manquante : la vidéo se construit en motion design ([interdits.md](interdits.md), « Pas de
diaporama de sa page »).

Range cette matière dans l'ordre d'[ambition.md](ambition.md) (principe 8) :
les vraies captures, les interfaces à reconstruire, les vrais chiffres de la fiche à mettre en
scène, les logos des outils, et ce qui ne pourra être dit que par ses mots. Au moment du script,
chaque phrase prendra le plus haut barreau qui existe pour elle ; une phrase qui ne trouverait que
sa typographie signale la matière à demander (section 3), jamais une forme à dessiner.

Note aussi, plan par plan, **les objets connus** qu'il montrera dans leurs vraies couleurs (pour
chaque plan : qu'est-ce que son public reconnaîtrait ici ? La réponse est souvent propre à son
métier, et absente de toute liste), autant qu'[ambition.md](ambition.md) le demande (principe 8 : trois au
moins au-delà de 15 s). Une vidéo dont la liste reste vide finira toute dans les trois couleurs de la marque.

Puis choisis **les logos qui flotteront**, scène par scène : seulement ceux des outils dont la
scène parle (l'outil du problème, la plateforme des résultats, les IA de l'offre), récupérés par
`studio_motion.py logos`. Pas d'icônes génériques. Vérifie aussi que les chiffres de la page sont
à jour : demande au client s'il en a de plus récents (une page dit souvent « plus de 150 », alors
qu'il en compte 190) et les chiffres de chaque résultat montré.

Quand le produit vit dans un outil (un modèle Notion, une extension, un dossier pour son IA, un
groupe privé), prévois de **montrer comment il s'y branche** avant de s'en servir
([scenes.md](scenes.md), « Comment ça marche ») : sans ce geste, le spectateur ne comprend pas ce qu'il achète
par rapport à l'outil qu'il a déjà.

Exemple (une formation d'illustration freelance) : l'espace de formation et ses six modules
[captures], le modèle de devis qui se remplit [capture du module 4], l'agenda des séances de
groupe, les portfolios d'élèves avant / après [sources/eleves], leurs messages de premiers clients
[captures de la page], les logos de Behance et d'Instagram (là où les élèves publient).

## 3. Ce qui manque : une seule question

Si une surface importante n'a pas de matière (une capture floue, aucune image de son produit en
action), ou si des phrases du script n'auraient que du texte à montrer, demande-la **à choix**, dans le message de la fiche et des trois idées (SKILL.md, étape 3), avec ta recommandation ; vise d'abord la matière de ces plans-là (faute de
matière, une vidéo finit en disques et en carrés seuls à l'écran) :

> Pour que ta vidéo montre vraiment ton produit, il me manque des images de [ton logiciel / ton
> espace de formation] en action. Tu peux m'envoyer :
> **a)** 2 ou 3 captures d'écran (ou le lien d'une page où on le voit) ;
> **b)** une courte vidéo où tu l'utilises, même filmée au téléphone ;
> **c)** rien : je fais avec ce que j'ai.
> Je te conseille a. Réponds par lettres (« a b »).

Sans réponse, ou « c », avance avec la matière disponible et dis dans la livraison ce qu'une
capture aurait apporté. Le style de la vidéo ne se demande pas ici : il se choisit à l'étape 3 bis,
le style maison (0), un des 9 styles, ou d'après une vidéo qu'il aime (section 4).

## 4. La vidéo de référence (si le client en donne une)

```bash
python3 tools/studio_motion.py reference "<dossier>" "<lien ou fichier>" --nom <nom-court>
```

L'outil télécharge la vidéo, en tire une planche toutes les 0,5 s, compte les coupes franches et
mesure le rythme, puis prépare `sources/reference/<nom>/ANALYSE.md`. Pas encore de téléchargeur ?
L'outil le dit : propose-le au client (« Pour lire ce lien, j'installe un téléchargeur de vidéos,
gratuit, une minute. Je le fais ? »), puis `python3 tools/studio_motion.py telechargeur installer` et
relance. S'il refuse, ou si ça échoue, demande-lui d'enregistrer son écran pendant que la vidéo passe
et de glisser le fichier dans la conversation. Regarde les planches et
remplis l'analyse : fonds et bascules, mots par écran, ce qui vit pendant la lecture, le motif qui
revient, les transitions, la caméra, les interfaces, la fin. Recopie dans `PLAN.md` les procédés
retenus et les mesures à atteindre (événements par seconde, part d'image figée).

On reprend **la grammaire**, jamais le contenu : ni ses textes, ni ses images, ni sa musique, ni
son produit. Sans référence, le niveau par défaut est celui d'[ambition.md](ambition.md).

## Ce que tu écris dans PLAN.md

```markdown
## Repérage

- Univers de la page : fond crème, accent corail, Fraunces et Inter, cartes arrondies, dessins
  d'élèves en grille.
- Surfaces : espace de formation (6 modules) [capture formation-1.jpg] · modèle de devis
  reconstruit · 8 portfolios d'élèves [sources/eleves] · 5 témoignages [capture/assets] · agenda
  des séances.
- Photos et vidéos : portfolios d'élèves avant / après = résultat (dans la fenêtre de Behance) ;
  portrait de la formatrice, photos d'atelier = décor (hors du film).
- Logos flottants : Behance et Instagram (les portfolios) ; aucune icône générique.
- Référence : aucune (ou : son nom, ses événements par seconde, ses procédés retenus).
- Manque : rien (ou : demandé au client, avec la date).
```
