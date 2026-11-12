# La voix

**Par défaut : du texte à l'écran et de la musique.** C'est la promesse de Publicitaire IA : le
client n'a rien à faire, la vidéo se comprend muette (beaucoup de supports se regardent sans le
son), et la musique la porte. Ne propose pas de voix s'il n'en demande pas.

Une **voix off** s'ajoute à sa demande, à une nouvelle vidéo ou à une vidéo déjà faite
(« ajoute une voix off », « je veux une voix »). Quel que soit le mode, **tout ce qui compte se lit
encore à l'écran**. Deux façons, à lui proposer en un seul message :

> Pour la voix off, deux possibilités :
> 1) **une voix IA, gratuite**, sur Google AI Studio : je t'écris le texte et le ton, tu les colles
>    sur le site, tu choisis une voix et tu télécharges le fichier (2 minutes, avec ton compte Google) ;
> 2) **ta voix** : je t'écris le texte, tu l'enregistres au dictaphone de ton téléphone (gratuit,
>    le plus convaincant).
> Dans les deux cas, je t'écris d'abord le texte et tu le valides.

S'il a un compte HeyGen et le préfère, une voix HeyGen se génère d'ici (plus bas, C, payante ; ses
conditions s'appliquent, [heygen.md](heygen.md), « Les droits »).
S'il refuse tout, une voix de synthèse gratuite existe sur son ordinateur (D), moins naturelle :
propose-la en dernier.

## 1. Le texte d'abord, toujours validé

- Une nouvelle vidéo : le texte de la voix, c'est le script validé (étape 3 bis du skill), plan par
  plan. Pour une vidéo de page
  qu'il veut avec voix off dès le départ, le texte peut venir **avant** le plan : il se valide, la
  voix se génère, puis le plan se cale sur ses mots (plus naturel pour une
  courte VSL, la voix porte la structure).
- Une vidéo déjà faite : pars de ses scènes et de leurs durées (`PLAN.md` et `npx hyperframes
  timeline` dans son projet). La voix suit l'ordre des scènes ; une scène trop courte pour sa phrase
  s'allongera (étape 3), elle ne se bourre pas de mots.
- Phrases de 12 mots au plus, une idée par phrase, des mots qu'il dirait vraiment. Durée : environ
  2,5 mots par seconde pour sa voix, mais **3 mots par seconde pour une voix Google AI Studio**
  (131 mots en 41 s avec « rythme soutenu », au lieu des 52 s estimées) ;
  pour une vidéo de page, le ton dit « rythme posé ». L'écran ne recopie pas la voix mot pour mot : il garde le mot clé, le chiffre, le nom
  de l'offre. Mêmes règles que `ecriture.md`, et rien qui ne soit dans `OFFRE.json`.
- Range-le dans `work/voix.txt` (dans le projet de la vidéo), montre-le-lui en entier avec sa durée
  estimée, et **attends son accord**. Rien ne s'enregistre ni ne se génère avant.

## 2. La voix

### A. Une voix IA gratuite, sur Google AI Studio

Le site gratuit de Google (Gemini TTS, usage commercial et pub permis) ; il le fait lui-même, avec
son compte Google, et la formation (module « Voix off ») le lui montre écran par écran.

1. Donne-lui, d'un bloc et prêts à copier : le **texte validé** (tu peux y poser des balises de
   pause, `<short pause>`, là où une respiration aide), la **consigne de ton** en une ligne
   (« Voix off de pub, chaleureuse et assurée, rythme posé », adaptée au but de la vidéo), et **la voix
   conseillée** dans la catégorie « Commercial Voiceover » (Nika, Koda ou Tavi), avec le lien
   https://aistudio.google.com/generate-speech.
2. Le geste, en une phrase : « Create new dialog, colle le texte, clique Speaker 1 et choisis la
   voix, clique Style et colle le ton, Run, écoute, puis Download en bas à droite. » Le filtre de
   langue « French » ne montre rien sans compte payant : inutile, les voix parlent la langue du
   texte.
3. Il dit que le fichier est dans ses Téléchargements (ou il le glisse ici) : cherche le fichier
   audio le plus récent (wav, mp3, m4a), range-le dans `assets/audio/voix-brute.*`, puis prépare
   `assets/audio/voix.wav` et le temps de chaque mot (E, plus bas). Fais écouter avant de caler la
   vidéo.
4. Une phrase qui sonne mal : corrige-la dans le texte, il ne régénère que ce bloc sur le site.
5. Pour qu'il choisisse à l'oreille, propose **deux ou trois voix** générées avec le même texte et le
   même ton (Nika, Koda, Tavi), rangées dans `assets/audio/prises/`, et vérifie chacune par la
   transcription (E) avant de la lui faire écouter : lors d'un essai, Koda collait
   « Publicitaire IA » en « Publicitéria » et disait les questions comme des affirmations.
   Si tu pilotes toi-même le navigateur intégré, il te faut sa connexion Google : il se connecte,
   jamais toi. Le bouton Download y range le fichier dans ses Téléchargements sous le nom
   « Generated Audio <date>.wav ».
   **11/11/2026, Gemini 3.8 Flash TTS** : le panneau Speaker 1 a un filtre « Gender » (Feminine,
   Masculine) ; pour une voix féminine en français, **Cleo** (« Warm and engaging ») a tout dit juste,
   question montante comprise, en 31 s pour 100 mots. Kira allait trop vite (27 s) et disait
   « Commande » pour « Commente » ; Nika disait « Publicitaire AI » à l'anglaise. Dans le texte,
   écris « Publicitaire I.A. » (avec les points) et un mot-clé en minuscules entre guillemets
   (« pub ») : en capitales, la voix risque de l'épeler. Les balises de pause ne sont pas
   nécessaires : la ponctuation suffit, et `voix respiration` ouvre les vraies pauses ensuite.
   **12/11/2026, mêmes voix pilotées dans son Chrome (extension)** : 128 mots, rythme soutenu,
   en 40 s pour **Mako** (la seule voix du style « Energetic ») et Ludo, 45 s pour Koda et Cleo ;
   toutes ont dit « Commente » et « l'I.A. » juste. Piège : une phrase absente de la transcription
   d'une prise entière n'est pas une phrase sautée par la voix. Whisper en perdait une sur deux
   prises de 45 s ; retranscrit seul (`-ss 14 -t 22`), le passage y était. Retranscris le passage
   avant de régénérer. Dans le panneau des voix, un filtre (Style…) reste actif quand on cherche
   un nom : repasse-le sur « All styles », sinon la voix cherchée n'apparaît pas.
   Un nom anglais se dit mal : Autonoe disait « Silence » pour « Seedance ». Réécris-le dans le
   texte de la voix seulement (l'écran garde la vraie orthographe) et génère plusieurs écritures
   d'un coup. **Seule l'oreille du client tranche** : « Sidance » a été transcrit « Sidance » par
   Whisper, mais dit « saïdense » à l'oreille. Whisper écarte seulement les ratés francs
   (« Sîdènse » → « Syndesia », « Ci-dense » → « Science »). **Retenu à l'oreille : « Si-danse »**
   (deux mots français liés par un tiret), écrit ainsi dans le texte de la voix. Une consigne de
   prononciation dans le champ Style aplatit l'intonation : préfère réécrire le mot.

### B. Sa voix, enregistrée sur son téléphone

1. Donne-lui le texte validé avec la consigne : au dictaphone de son téléphone, dans un endroit
   calme, téléphone à 20 cm, phrase par phrase ; s'il se trompe, il reprend la phrase, on garde la
   dernière version. Pas besoin d'une prise parfaite d'une traite.
2. Le fichier passe sur son ordinateur (AirDrop sur Mac, ou envoyé à lui-même par email ou
   WhatsApp) : il le laisse dans Téléchargements et te le dit, ou il le glisse dans la
   conversation. Cherche le fichier audio le plus récent de Téléchargements (m4a, mp3, wav, aac)
   et range-le dans `assets/audio/voix-brute.*`.
3. Transcris-la telle quelle, comme en E (`npx hyperframes transcribe assets/audio/voix-brute.m4a
   --engine parakeet --language fr`) : le texte daté montre les reprises. Garde la dernière prise de
   chaque phrase et raccourcis à 0,4 s les blancs plus longs entre les phrases, avec ffmpeg (`atrim`
   + `concat`), dans `assets/audio/voix-montee.wav`.
4. Prépare `assets/audio/voix.wav` depuis `voix-montee.wav` et le temps de chaque mot (E). Fais
   écouter le résultat avant de caler la vidéo dessus.

### C. Une voix de synthèse HeyGen (payante, quelques centimes)

1. HeyGen doit être relié ([heygen.md](heygen.md)). Les voix s'écoutent gratuitement :
   `heygen voix --genre femme --ouvrir` (ou `homme`) depuis le projet. Les aperçus sont souvent en
   anglais : la voix parlera la langue du texte. Il répond par un numéro ; note l'id dans
   `studio.config.json` (`voix_heygen`) pour ses prochaines vidéos.
2. Le coût : `heygen parler work/voix.txt --voix <id>` (sans `--confirme`) l'affiche sans rien
   générer. Annonce-le (le montant affiché), **attends son accord**.
3. `heygen parler work/voix.txt --voix <id> --confirme` : `assets/audio/voix.wav` (déjà au niveau
   d'une voix de Reel) et `work/voix-mots.json` (le temps de chaque mot). Fais-lui écouter avant de
   caler la vidéo. Une phrase qui sonne mal se corrige dans le texte (ponctuation, mot plus simple)
   et se régénère, coût annoncé de nouveau.
4. Solde vide : voir [heygen.md](heygen.md) (recharger quelques dollars, ou sa voix au téléphone).

### D. Une voix de synthèse locale (gratuite, en dernier recours)

Elle demande deux paquets Python (pour Python 3.10 à 3.13) et un modèle d'environ 300 Mo,
téléchargés une fois. Annonce-le, puis installe-les **à part**, dans le dossier (jamais dans le
Python de son ordinateur), depuis la racine. Le Python du Mac (3.9) ne convient pas : avec son
accord, `brew install python@3.12` d'abord (sans Homebrew : son installeur `Homebrew.pkg`, comme à
l'étape 1 d'INSTALL.md, jamais son script `install.sh`).

```bash
python3.12 -m venv .venv-voix                              # Windows : py -3.12 -m venv .venv-voix
.venv-voix/bin/pip install kokoro-onnx soundfile           # Windows : .venv-voix\Scripts\pip install kokoro-onnx soundfile
```

Puis, depuis le projet, avec ce Python-là (variable `HYPERFRAMES_PYTHON`) :

```bash
HYPERFRAMES_PYTHON=../../../.venv-voix/bin/python npx hyperframes tts "<texte>" --voice ff_siwis --lang fr-fr -o assets/audio/voix-brute.wav
```

Sous Windows (PowerShell) : `$env:HYPERFRAMES_PYTHON="..\..\..\.venv-voix\Scripts\python.exe"`, puis
la même commande avec `npx.cmd hyperframes tts`. Si l'installation échoue, n'insiste pas : propose sa
voix au téléphone.

`ff_siwis` est la voix française ; `--speed 1.05` si elle traîne. Fais écouter 10 secondes avant
de produire toute la vidéo : sa qualité ne plaît pas à tout le monde. Puis `assets/audio/voix.wav`
et le temps de chaque mot, comme en E.

Une autre voix payante (ElevenLabs…) seulement s'il l'a déjà et l'accepte, coût annoncé avant.
Ne clone jamais une voix sans son accord explicite.

### E. Le fichier de la voix et le temps de chaque mot (A, B et D)

Depuis le projet de la vidéo. Sous Windows, dans PowerShell, `npx.cmd` au lieu de `npx`.

1. **La voix au niveau d'une voix de Reel**, les blancs de plus de 0,4 s du début et de la fin
   ramenés à 0,4 s, en 48 kHz (sans `-ar 48000`, `loudnorm` sort du 192 kHz). L'entrée est
   `voix-brute.*` (A, D) ou `voix-montee.wav` (B) :

   ```bash
   ffmpeg -v error -y -i assets/audio/voix-brute.wav -af "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.4,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.4,areverse,loudnorm=I=-24:TP=-3:LRA=11" -ar 48000 -c:a pcm_s16le assets/audio/voix.wav
   ```

2. **Le temps de chaque mot**, par Parakeet, le modèle de reconnaissance vocale de HyperFrames
   (français compris), sur son ordinateur. La langue de la voix se donne toujours : `fr`, ou `en`,
   `es`… si la voix n'est pas en français.

   ```bash
   npx hyperframes transcribe assets/audio/voix.wav --engine parakeet --language fr
   ```

   Il écrit `assets/audio/transcript.json`, à côté de la voix : chaque mot, son début et sa fin en
   secondes (quelques secondes de calcul). Puis, **toujours**, remets le texte juste sur ces temps :

   ```bash
   python3 ../../../tools/studio_motion.py voix caler
   ```

   Il garde les mots de `work/voix.txt` et prend à la transcription le temps de chaque mot ; la
   transcription brute reste dans `assets/audio/transcript-brut.json`. Piège vu sur une
   voix Google AI Studio en français (Nika) : Parakeet écrivait des mots en anglais (« It's » pour
   « C'est », « And that video? ») et sautait des passages entiers (120 mots reconnus sur 131) ;
   sans `voix caler`, des animations se calaient sur des mots absents.

   À la première voix off, il répond « Parakeet is not installed » : le modèle se télécharge une
   fois sur l'ordinateur. Annonce-le d'abord (« Pour caler la vidéo sur ta voix, je télécharge une
   fois le modèle qui reconnaît les mots : 675 Mo, environ une minute. »), puis :

   ```bash
   npx hyperframes models install parakeet
   ```

   et relance la transcription. **Jamais `transcribe` sans `--engine parakeet --language …`** : le
   modèle par défaut est anglais et invente un texte sur une voix française, et sur Mac il installe
   un autre outil (whisper-cpp) sans demander. Parakeet refuse de s'installer (Windows sur
   processeur ARM) : cale la vidéo sur les pauses de la voix (`ffmpeg -i assets/audio/voix.wav -af
   silencedetect=n=-40dB:d=0.3 -f null -`, une phrase entre deux pauses) et sur `work/voix.txt`.

3. **Les respirations.** Une voix de synthèse ne laisse presque aucune pause (aucune d'une seconde
   lors d'un essai). Ouvre-en une de 1,5 s juste avant la phrase du pivot, **en Reel aussi**, et
   une d'environ 1 s quand le résultat s'affiche : la musique entre dans ce trou au lieu de couvrir
   le nom de l'offre (son.md, « Sous une voix off »). Piège du 11/11/2026 : une respiration de 1 s
   au pivot d'un Reel ne fait pas remonter la musique (`sons` ne la remonte qu'à partir de 1,45 s :
   « remontée dans 0 respiration(s) »), et sa cassure passe sous la voix ; à 1,5 s, elle éclate.

   ```bash
   python3 ../../../tools/studio_motion.py voix respiration <instant de la pause, en s du fichier> [--secondes 1.5]
   ```

   Le silence s'allonge au milieu de la pause la plus proche, les mots suivants reculent d'autant
   dans `transcript.json` ; l'ancienne voix reste dans `voix-avant-respiration.wav`. Fais-le avant
   d'écrire le plan, sinon décale ensuite les scènes d'après.
   Une respiration de moins de 1,5 s ne fait pas remonter la musique (`sons` : « remontée dans 0
   respiration ») : l'entrée franche s'y perd sous la voix. Pour qu'elle claque, 1,5 s même en Reel
   ou en story.
   Sauf pour une voix rapide de Reel (12/11/2026, Reel motion) : 1,5 s après « six heures » sonnait comme un
   blanc (« on attend quasiment deux secondes »). Là, 0,7 s au plus : cale l'attaque de la batterie juste
   après le dernier mot, note-la dans `"musique_entree"`, et décale la musique d'autant que la voix (tout ce
   qui suit garde son calage).

   Piège (11/11/2026, story « prompt secret ») : pour changer la longueur d'une respiration, repars
   de `voix-avant-respiration.wav` et **retranscris** (`transcribe`, puis `voix caler`) avant la
   nouvelle `respiration` : `transcript-brut.json` garde les temps déjà décalés, et `voix caler`
   les décalait une seconde fois (les mots d'après tombaient 0,6 s trop tard). Après une
   respiration, Parakeet peut aussi brouiller la fin (des mots placés dans le silence) : vérifie
   les dernières phrases sur `ffmpeg -af silencedetect=n=-40dB:d=0.25` (une phrase entre deux
   silences) et corrige leurs temps dans `transcript.json` s'il le faut.

## 3. Caler la vidéo sur la voix

- Les animations se calent sur les mots (`assets/audio/transcript.json`, ou `work/voix-mots.json`
  pour une voix HeyGen) : un élément arrive **avec** le mot qui le nomme, pas après. Chaque scène
  commence avec la phrase qui la porte ; allonge ou raccourcis la scène (`data-duration` dans
  `index.html`, en gardant la grille de 0,5 s autant que possible) plutôt que de presser la voix.
  Piège (12/11/2026, Reel motion) : une voix de synthèse enchaîne ses phrases sans silence de 0,25 s, donc
  presque aucun mot n'« ouvre une phrase » pour `calage`, et cinq scènes posées sur leur phrase ont été
  refusées. Fais alors partir chaque scène sur un temps de la grille que `calage` mesure (à 0,04 s près),
  entre deux mots (à plus de 0,06 s de leur cœur) : calcule les candidats avec ses propres fonctions
  (`pistes_audio`, `mots_de_la_voix`, `grille_musique`, `temps_de_la_grille`, `_mot_coupe` de
  `tools/studio_motion.py`), puis déplace le texte d'une scène dans la fin de la précédente s'il le faut.
- Pose la voix avec les sons, dans `work/sons.json` : `"voix": "assets/audio/voix.wav"`,
  `"voix_debut": 0.3` (son départ dans la vidéo). La musique passe d'elle-même sous la voix, à un
  écart mesuré sur le morceau, baissée pendant la parole et remontée dans les respirations (son.md,
  « Sous une voix off ») ; le mélange entier est amené au niveau des Reels. Avec une voix,
  moins de bruitages : les gestes forts (clic, coche, impact sur le nom et le prix), et une frappe
  de clavier sur chaque phrase tapée importante, une prise différente à chaque fois : un peu de
  bruitages, sans en abuser. Plus discrets aussi : aucun ne passe
  au-dessus de la voix qui l'entoure (`emergence` le vérifie, son.md, « L'équilibre entre la
  musique, les bruitages et la voix »).
  Une vidéo déjà sonorisée : refais la liste complète et relance `sons` (`--ecraser` seulement si
  le bloc a été retouché à la main ou dans l'app, son.md, « Poser les sons »).
- Des sous-titres incrustés en plus si le support se regarde muet (story, pub dans le fil) : ils
  suivent la voix ([supports.md](supports.md), « Sous-titres et texte »), hors de la règle d'un mot
  à lire par seconde.
- Puis rendu, revue et export comme toute vidéo ([revue.md](revue.md)).

## 4. Une vidéo déjà livrée

La version avec voix s'ajoute à côté de l'autre : `livraison/<vidéo>-voix.mp4`, l'originale reste
(pour une pub, il teste les deux). Dis-lui laquelle est laquelle dans ton message de livraison.
