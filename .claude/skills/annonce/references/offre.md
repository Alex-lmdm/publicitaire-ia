# La fiche de l'offre : ce que les vidéos ont le droit de dire

Une annonce qui invente perd la confiance de l'audience du client, et peut tomber sous la
publicité trompeuse. Donc une règle simple : **ce qui n'est pas dans `OFFRE.json` avec sa source
n'apparaît dans aucune vidéo.** Le ton, le rythme, les transitions et les blagues sont libres.
Les faits ne le sont pas.

## 1. Capturer la page

Depuis le dossier Monteur IA :

```bash
npx hyperframes capture "<lien de la page>" -o "annonces/<annonce>/sources/capture"
```

Ne propose pas de clé Gemini : la capture marche sans, et le client n'a rien à configurer.
Contrôle que `sources/capture/extracted/visible-text.txt` existe et n'est pas vide, et que
`screenshots/` contient des images. Sinon (page protégée, page vide, erreur) : dis-le en une
phrase et demande deux ou trois captures d'écran de sa page, ou le texte de l'offre. Une capture
ratée n'est jamais une source.

Sans page de vente : le client décrit l'offre. Chaque fait qu'il donne a la source `client`.
Ses captures vont dans `sources/` et se citent par leur nom de fichier.

## 2. Remplir OFFRE.json

Source unique : `visible-text.txt` (ce que la page affiche vraiment), plus ce que le client a dit.
Chaque fait porte `source` : `page`, `client`, ou le nom d'un fichier de `sources/`.

| Champ | Ce qu'on y met | Piège |
|---|---|---|
| `produit` | Le nom exact de l'offre | Pas un nom raccourci inventé |
| `type` | `lancement`, `nouveaute`, `relance` ou `dernier-jour` | |
| `promesse.texte` | La promesse centrale, **9 mots au plus**, reprise du titre de la page | Raccourcir sans changer le sens ; pas de superlatif ajouté |
| `recoit` | Ce qu'on reçoit concrètement (modules, séances, fichiers, accès) | Un intitulé de module se recopie, il ne se reformule pas en mieux |
| `prix` | `montant` en nombre, `barre` seulement si la page affiche un vrai prix précédent | Un « valeur 997 € » n'est pas un prix barré |
| `bonus` | Chaque bonus tel que la page le nomme | |
| `dates` | `ouverture` et `fermeture` en `AAAA-MM-JJ` ou `AAAA-MM-JJTHH:MM` | Sans fermeture réelle : pas de story « dernier jour », pas de compte à rebours |
| `preuves` | `type` : `chiffre`, `temoignage`, `resultat` ou `media` | Un témoignage se cite **mot pour mot** (`mot_pour_mot: true`) avec son prénom tel qu'affiché |
| `cta` | `mot_cle` (un mot en MAJUSCULES) et la phrase d'appel à l'action | La phrase reprend le geste réel (commenter, cliquer le lien) |
| `interdits` | Ce que le client ne veut pas voir (un concurrent, un ancien prix, un sujet) | |

Arrondis toujours **vers le bas** : « 3 354 000 vues » devient « 3,3 millions », jamais
« 3,4 millions ». Un chiffre sans date ni contexte (« +200 % ») ne s'utilise pas seul.

Données personnelles : un tableau de ventes, une boîte mail, un CRM montrés dans une capture
gardent leur forme mais leurs noms, emails et montants de clients passent en exemples fictifs
cohérents. Note-le dans `sources/NOTES.md`.

## 3. Vérifier

```bash
python3 tools/annonce.py offre "annonces/<annonce>"
```

Corrige jusqu'à « ok ». L'outil refuse aussi une story « dernier jour » sans date de fermeture.

## 4. Le montrer au client

Cinq à sept lignes, dans ses mots à lui, pas un JSON :

> Voici ce que j'ai compris de ta page :
> - **Monteur IA** : tes Reels montés par ton IA.
> - On reçoit : le système complet, la formation pas à pas, Reel Cloneur offert.
> - **97 €**, paiement unique. Ouverture jeudi 18 h, fermeture dimanche minuit.
> - Preuve : 3,3 millions de vues sur tes 20 derniers Reels.
> - Mot-clé : MONTEUR.
>
> C'est tout ce que tes vidéos auront le droit d'affirmer. Corrige-moi si quelque chose est faux ou manque.

Une correction du client met à jour la fiche (source `client`), puis on revérifie.

## Pendant la fabrication

Dans `PLAN.md`, chaque texte affiché pointe vers sa clé (`prix.montant`, `bonus[0]`,
`preuves[1]`). Un texte sans clé est du ton (« C'est ouvert »), jamais un fait. À la revue,
relis chaque texte de la planche face à la fiche.
