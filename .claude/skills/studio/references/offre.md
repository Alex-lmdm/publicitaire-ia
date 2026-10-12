# La fiche de l'offre : ce que les vidéos ont le droit de dire

Une vidéo qui invente perd la confiance de l'audience du client, et peut tomber sous la publicité
trompeuse. Une règle simple : **ce qui n'est pas dans `OFFRE.json` avec sa source n'apparaît dans
aucune vidéo.** Le ton, le rythme, les images et les transitions sont libres. Les faits ne le
sont pas.

## 1. Capturer la page

Depuis le dossier Monteur IA :

```bash
npx hyperframes capture "<lien de la page>" -o "studio-motion/<dossier>/sources/capture"
```

Ne propose pas de clé Gemini : la capture marche sans, et le client n'a rien à configurer.
Contrôle que `sources/capture/extracted/visible-text.txt` existe et n'est pas vide, et que
`screenshots/` contient des images. Sinon (page protégée, page vide, erreur) : dis-le en une
phrase et demande deux ou trois captures d'écran de sa page, ou le texte de l'offre. Une capture
ratée n'est jamais une source. La capture garde aussi les couleurs, polices et images de la page :
la vidéo s'en sert.

Sans page de vente : le client décrit l'offre. Chaque fait qu'il donne a la source `client`.
Ses captures vont dans `sources/` et se citent par leur nom de fichier.

## 2. Remplir OFFRE.json

Source unique : `visible-text.txt` (ce que la page affiche vraiment), plus ce que le client a dit.
Chaque élément porte `source` : `page`, `client`, ou le nom d'un fichier de `sources/`. Remplis
ce que l'objectif demande ; les autres champs restent vides.

| Champ | Ce qu'on y met | Piège |
|---|---|---|
| `produit` | Le nom exact de l'offre (ou de la fonctionnalité, du guide) | Pas de nom raccourci inventé |
| `objectif` | `vente`, `nouveaute`, `fonctionnalite`, `lancement`, `inscription`, `explication`, `preuve` | |
| `public` | Pour qui, tel que la page le dit | |
| `probleme` | Le problème de l'audience, dans ses mots (obligatoire pour vendre, expliquer, faire s'inscrire) | Pas de douleur exagérée que la page ne dit pas |
| `promesse` | La promesse centrale, **9 mots au plus**, reprise du titre de la page | Raccourcir sans changer le sens ; pas de superlatif ajouté |
| `mecanisme` | Comment ça marche, ce qui rend la promesse possible | |
| `nouveaute` | Ce qui est nouveau (obligatoire pour l'objectif nouveauté) | |
| `recoit` | Ce qu'on reçoit concrètement (modules, séances, fichiers, accès) | Un intitulé se recopie, il ne se reformule pas en mieux |
| `prix` | `montant` en nombre ; `barre` seulement si la page affiche un vrai prix précédent | Un « valeur 997 € » n'est pas un prix barré |
| `bonus` | Chaque bonus tel que la page le nomme | |
| `garantie` | La garantie, mot pour mot | Aucune garantie inventée |
| `dates` | `ouverture` et `fermeture` de l'offre, en `AAAA-MM-JJ` ou `AAAA-MM-JJTHH:MM` | Sans fermeture réelle : pas de « dernier jour », pas de compte à rebours |
| `echeances` | Les autres vraies échéances : `{texte, date, source}` (un bonus retiré, un prix qui change) | Seules urgences permises, avec `dates.fermeture` |
| `preuves` | `type` : `chiffre`, `temoignage`, `resultat` ou `media` | Un témoignage se cite **mot pour mot** (`mot_pour_mot: true`), avec le prénom s'il est affiché ; jamais de prénom inventé |
| `objections` | Les doutes que la page lève (« pas besoin de savoir monter ») | |
| `cta` | `mot_cle` (un mot en MAJUSCULES), `phrase`, ou `lien` | La phrase reprend le geste réel |
| `interdits` | Ce que le client ne veut pas voir (un concurrent, un ancien prix, un sujet) | |

Pour les chiffres attachés à des médias (les vues de chaque Reel affiché sur la page), regarde
aussi `sources/capture/extracted/video-manifest.json` et `asset-descriptions.md` : ils relient
chaque vidéo de la page à son texte.

**Dates et vidéo qui dure** : une vidéo de page ou un Reel reste en ligne des mois. N'y mets pas
une date qui sera dépassée dans une semaine (« bonus jusqu'au 17 ») : elle va dans la légende, la
story ou la pub, qui vivent moins longtemps.

Arrondis toujours **vers le bas** : « 3 354 000 vues » devient « 3,3 millions », jamais
« 3,4 millions ». Un chiffre sans contexte (« +200 % ») ne s'utilise pas seul.

Données personnelles : un tableau de ventes, une boîte mail, un CRM montrés dans une capture
gardent leur forme, mais leurs noms, emails et montants de clients deviennent des exemples
fictifs cohérents. Note-le dans `sources/NOTES.md`.

## 3. Vérifier

```bash
python3 tools/studio_motion.py offre "studio-motion/<dossier>"
```

Corrige jusqu'à « ok ». L'outil exige aussi ce que l'objectif demande (le problème pour vendre, la
nouveauté pour une nouveauté, une preuve pour une preuve) et refuse un « dernier jour » sans date
de fermeture.

## 4. Le montrer au client

Cinq à sept lignes, dans ses mots à lui, pas un JSON :

> Voici ce que j'ai compris de ta page :
> - **Monteur IA**, pour les créateurs qui postent des Reels : tes Reels montés par ton IA.
> - Le problème : des heures de montage sur CapCut.
> - On reçoit : le système complet, les 21 skills, l'app gratuite. Bonus : Reel Cloneur offert.
> - **97 €**, paiement unique.
> - Preuve : plus de 3,3 millions de vues sur tes 20 derniers Reels.
>
> C'est tout ce que ta vidéo aura le droit d'affirmer. Corrige-moi si quelque chose est faux ou
> manque.

Une correction du client met à jour la fiche (source `client`), puis on revérifie.

## Pendant la fabrication

Dans `PLAN.md`, chaque texte affiché pointe vers sa clé (`prix.montant`, `bonus[0]`,
`preuves[1]`). Un texte sans clé est du ton (« C'est ouvert »), jamais un fait. À la revue,
relis chaque texte de la planche face à la fiche.
