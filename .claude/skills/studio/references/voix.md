# La voix

**Par défaut : du texte à l'écran et de la musique.** C'est la promesse de Publicitaire IA : le
client n'a rien à faire, la vidéo se comprend muette (beaucoup de supports se regardent sans le
son), et la musique la porte. Ne propose pas de voix s'il n'en demande pas.

Une **voix off** s'ajoute à sa demande, à une nouvelle vidéo ou à une vidéo déjà faite
(« ajoute une voix off », « je veux une voix »). Quel que soit le mode, **tout ce qui compte se lit
encore à l'écran**. Deux façons, à lui proposer en un seul message :

> Pour la voix off, deux possibilités :
> 1) **ta voix** : je t'écris le texte, tu l'enregistres au dictaphone de ton téléphone (gratuit,
>    le plus convaincant) ;
> 2) **une voix de synthèse HeyGen** : tu choisis une voix, je la génère (quelques centimes par
>    vidéo, prélevés sur ton compte HeyGen, coût annoncé avant).
> Dans les deux cas, je t'écris d'abord le texte et tu le valides.

S'il refuse les deux, une voix de synthèse gratuite existe sur son ordinateur (plus bas, D), moins
naturelle : propose-la en dernier.

## 1. Le texte d'abord, toujours validé

- Une nouvelle vidéo : écris le texte d'après `PLAN.md`, scène par scène.
- Une vidéo déjà faite : pars de ses scènes et de leurs durées (`PLAN.md` et `npx hyperframes
  timeline` dans son projet). La voix suit l'ordre des scènes ; une scène trop courte pour sa phrase
  s'allongera (étape 3), elle ne se bourre pas de mots.
- Phrases de 12 mots au plus, une idée par phrase, des mots qu'il dirait vraiment, environ 2,5 mots
  par seconde. L'écran ne recopie pas la voix mot pour mot : il garde le mot clé, le chiffre, le nom
  de l'offre. Mêmes règles que `ecriture.md`, et rien qui ne soit dans `OFFRE.json`.
- Range-le dans `work/voix.txt` (dans le projet de la vidéo), montre-le-lui en entier avec sa durée
  estimée, et **attends son accord**. Rien ne s'enregistre ni ne se génère avant.

## 2. La voix

### B. Sa voix, enregistrée sur son téléphone

1. Donne-lui le texte validé avec la consigne : au dictaphone de son téléphone, dans un endroit
   calme, téléphone à 20 cm, phrase par phrase ; s'il se trompe, il reprend la phrase, on garde la
   dernière version. Pas besoin d'une prise parfaite d'une traite.
2. Le fichier passe sur son ordinateur (AirDrop sur Mac, ou envoyé à lui-même par email ou
   WhatsApp) : il le laisse dans Téléchargements et te le dit, ou il le glisse dans la
   conversation. Cherche le fichier audio le plus récent de Téléchargements (m4a, mp3, wav, aac)
   et range-le dans `assets/audio/voix-brute.*`.
3. Transcris-la (`npx hyperframes transcribe assets/audio/voix-brute.m4a`) : le texte daté montre
   les reprises. Garde la dernière prise de chaque phrase, coupe les blancs de plus de 0,4 s avec
   ffmpeg (`atrim` + `concat`), mets-la au niveau d'une voix de Reel (`loudnorm=I=-24:TP=-3`), puis
   exporte `assets/audio/voix.wav`. Fais écouter le résultat avant de caler la vidéo dessus.
4. Le temps de chaque mot : `npx hyperframes transcribe assets/audio/voix.wav`.

### C. Une voix de synthèse HeyGen (payante, quelques centimes)

1. HeyGen doit être relié ([heygen.md](heygen.md)). Les voix s'écoutent gratuitement :
   `heygen voix --genre femme --ouvrir` (ou `homme`) depuis le projet. Les aperçus sont souvent en
   anglais : la voix parlera la langue du texte. Il répond par un numéro ; note l'id dans
   `studio.config.json` (`voix_heygen`) pour ses prochaines vidéos.
2. Le coût : `heygen parler work/voix.txt --voix <id>` (sans `--confirme`) l'affiche sans rien
   générer. Annonce-le (« environ 0,02 $ sur ton solde HeyGen »), **attends son accord**.
3. `heygen parler work/voix.txt --voix <id> --confirme` : `assets/audio/voix.wav` (déjà au niveau
   d'une voix de Reel) et `work/voix-mots.json` (le temps de chaque mot). Fais-lui écouter avant de
   caler la vidéo. Une phrase qui sonne mal se corrige dans le texte (ponctuation, mot plus simple)
   et se régénère, coût annoncé de nouveau.
4. Solde vide : voir [heygen.md](heygen.md) (recharger quelques dollars, ou sa voix au téléphone).

### D. Une voix de synthèse locale (gratuite, en dernier recours)

Elle demande deux paquets Python (pour Python 3.10 à 3.13) et un modèle d'environ 300 Mo,
téléchargés une fois. Annonce-le, puis installe-les **à part**, dans le dossier (jamais dans le
Python de son ordinateur), depuis la racine. Le Python du Mac (3.9) ne convient pas : avec son
accord, `brew install python@3.12` d'abord.

```bash
python3.12 -m venv .venv-voix                              # Windows : py -3.12 -m venv .venv-voix
.venv-voix/bin/pip install kokoro-onnx soundfile           # Windows : .venv-voix\Scripts\pip install kokoro-onnx soundfile
```

Puis, depuis le projet, avec ce Python-là (variable `HYPERFRAMES_PYTHON`) :

```bash
HYPERFRAMES_PYTHON=../../../.venv-voix/bin/python npx hyperframes tts "<texte>" --voice ff_siwis --lang fr-fr -o assets/audio/voix.wav
```

Sous Windows (PowerShell) : `$env:HYPERFRAMES_PYTHON="..\..\..\.venv-voix\Scripts\python.exe"`, puis
la même commande `npx hyperframes tts`. Si l'installation échoue, n'insiste pas : propose sa voix au
téléphone.

`ff_siwis` est la voix française ; `--speed 1.05` si elle traîne. Fais écouter 10 secondes avant
de produire toute la vidéo : sa qualité ne plaît pas à tout le monde. Puis `transcribe` comme en B.

Une autre voix payante (ElevenLabs…) seulement s'il l'a déjà et l'accepte, coût annoncé avant.
Ne clone jamais une voix sans son accord explicite.

## 3. Caler la vidéo sur la voix

- Les animations se calent sur les mots : un élément arrive **avec** le mot qui le nomme, pas
  après. Chaque scène commence avec la phrase qui la porte ; allonge ou raccourcis la scène
  (`data-duration` dans `index.html`, en gardant la grille de 0,5 s autant que possible) plutôt que
  de presser la voix.
- Pose la voix avec les sons, dans `work/sons.json` : `"voix": "assets/audio/voix.wav"`,
  `"voix_debut": 0.3` (son départ dans la vidéo). La musique passe d'elle-même sous la voix
  (`musique_db` -26,5 par défaut) et le mélange entier est amené au niveau des Reels. Avec une voix,
  moins de bruitages : seulement les gestes forts (clic, coche, impact sur le nom et le prix).
  Une vidéo déjà sonorisée : refais la liste complète et relance `sons` avec `--ecraser`.
- Des sous-titres incrustés en plus si le support se regarde muet (story, pub dans le fil).
- Puis rendu, revue et export comme toute vidéo ([revue.md](revue.md)).

## 4. Une vidéo déjà livrée

La version avec voix s'ajoute à côté de l'autre : `livraison/<vidéo>-voix.mp4`, l'originale reste
(pour une pub, il teste les deux). Dis-lui laquelle est laquelle dans ton message de livraison.
