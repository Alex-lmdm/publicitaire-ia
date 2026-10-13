# Le repérage : ce que la vidéo va montrer

Une vidéo de motion design produit se construit avec des images, pas avec des phrases. Avant de
choisir l'angle, fais l'inventaire de **ce qui peut se montrer** et réunis la matière. C'est
cette étape qui sépare une vidéo de niveau studio d'une suite de slides.

Elle vient juste après la porte de vérité (`offre.md`), avant la structure. Elle prend quelques
minutes et ne pose au plus qu'une question au client.

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
| **Les outils dont l'offre parle** | Claude, ChatGPT, Codex, Notion, Canva, CapCut, Instagram, Stripe | Leur logo (`studio_motion.py logos <projet> claude openai …`) et leur interface reconnaissable |
| **Le résultat** | ses Reels, un avant / après, un tableau de ventes, une page créée | Les vraies images et vidéos du dossier `sources/` |
| **Les preuves** | captures de témoignages, chiffres de la page | Les vraies captures, les chiffres de la fiche |
| **Le problème** | l'outil pénible d'avant (une timeline chargée, un tableur, dix onglets) | Reconstruit en simple, reconnaissable, sans marque inventée |

Puis choisis **les logos qui flotteront**, scène par scène : seulement ceux des outils dont la
scène parle (l'outil du problème, la plateforme des résultats, les IA de l'offre), récupérés par
`studio_motion.py logos`. Pas d'icônes génériques. Vérifie aussi que les chiffres de la page sont
à jour : demande au client s'il en a de plus récents (la page de la démo disait « plus de 150
créateurs », le créateur en comptait 190) et les vues de chaque résultat montré.

Quand le produit vit dans un outil (un dossier pour Claude, une extension, un modèle Notion),
prévois de **montrer comment il s'y branche** avant de s'en servir (recette 5 bis) : sans ce
geste, le spectateur ne comprend pas ce qu'il achète par rapport à l'outil qu'il a déjà.

Exemple (Monteur IA, système qui monte les Reels avec Claude ou ChatGPT) : la page parle de
Claude et de ChatGPT, donc les tuiles des trois IA (ChatGPT, Codex, Claude), le curseur qui
choisit Claude, l'interface de bureau de Claude (son onglet Code, « Quoi de prévu, Alex ? »), la
vidéo brute glissée dans le champ, la demande tapée, les étapes qui se cochent avec leurs aperçus,
la timeline de montage d'avant pour le problème, ses vrais Reels et leurs vues, ses vrais
messages de clients, les vraies miniatures de la formation.

## 3. Ce qui manque : une seule question

Si une surface importante n'a pas de matière (une capture floue, aucune image de son produit en
action), demande-la **en un seul message à choix**, avec ta recommandation :

> Pour que ta vidéo montre vraiment ton produit, il me manque des images de [ton logiciel / ton
> espace de formation] en action. Tu peux m'envoyer :
> **a)** 2 ou 3 captures d'écran (ou le lien d'une page où on le voit) ;
> **b)** une courte vidéo où tu l'utilises, même filmée au téléphone ;
> **c)** une vidéo dont tu aimes le style (un lien suffit), pour que je vise ce niveau ;
> **d)** rien : je fais avec ce que j'ai.
> Je te conseille a et c. Réponds par lettres (« a c »).

Sans réponse, ou « d », avance avec la matière disponible et dis dans la livraison ce qu'une
capture aurait apporté.

## 4. La vidéo de référence (si le client en donne une)

```bash
python3 tools/studio_motion.py reference "<dossier>" "<lien ou fichier>" --nom <nom-court>
```

L'outil télécharge la vidéo, en tire une planche toutes les 0,5 s, compte les coupes franches et
mesure le rythme, puis prépare `sources/reference/<nom>/ANALYSE.md`. Regarde les planches et
remplis l'analyse : fonds et bascules, mots par écran, ce qui vit pendant la lecture, le motif qui
revient, les transitions, la caméra, les interfaces, la fin. Recopie dans `PLAN.md` les procédés
retenus et les mesures à atteindre (événements par seconde, part d'image figée).

On reprend **la grammaire**, jamais le contenu : ni ses textes, ni ses images, ni sa musique, ni
son produit. Sans référence, la grammaire par défaut est celle de `rythme.md` et `style.md`
(étalonnée sur une vidéo de lancement produit : 1,5 événement par seconde).

## Ce que tu écris dans PLAN.md

```markdown
## Repérage

- Univers de la page : fond #202022, accent jaune #ffee00, Poppins, cartes blanches arrondies,
  Reels en éventail.
- Surfaces : Claude (bureau, onglet Code) [capture formation-1.jpg] · timeline de montage
  reconstruite · ses 7 Reels [sources/reels] · 4 témoignages [capture/assets] · miniatures de la
  formation.
- Objets flottants : ciseaux, sous-titres, note, onde, horloge, logo CapCut, logos des IA.
- Référence : taapit (1,5 événement/s, 17 coupes en 77 s) : chapitres avec interrupteur, fond
  couleur plein écran pour le nom, mosaïque finale qui devient le bouton.
- Manque : rien (ou : demandé au client le 12/10).
```
