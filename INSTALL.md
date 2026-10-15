# Installer Publicitaire IA

Publicitaire IA fabrique des vidéos en motion design qui vendent ton offre. Il s'installe **tout
seul**, sans autre logiciel de la formation, et sans abonnement en plus. Tout tourne sur ton
ordinateur, avec ton abonnement Claude ou ChatGPT habituel.

Ouvre **Claude Code** ou **Codex** et écris :

```text
Télécharge Publicitaire IA depuis https://github.com/Alex-lmdm/publicitaire-ia et suis les instructions d'installation de son INSTALL.md
```

L'IA télécharge le dossier, vérifie ton ordinateur, te dit ce qu'il manque, puis installe tout.
**Quand elle te propose de commencer, réponds « go ».** Elle exécute les commandes : tu n'as rien
à recopier dans un terminal. Si une manipulation est nécessaire de ton côté, elle te guide.

L'app **HyperFrames** (Mac) est en option : elle sert à voir et retoucher chaque vidéo à la
souris. L'installation la branche si elle est là.

---

## Pour l'IA : l'installation, étape par étape

Parle-lui en français, simplement, une phrase par étape, sans jargon ; dis toujours qui agit
maintenant. Garde les noms des fichiers et des commandes tels quels. Ne passe jamais à l'étape
suivante si l'étape en cours a échoué ; en cas d'échec, diagnostique en trois lignes (message
d'erreur → cause probable → UNE action corrective), puis retente.

**0. Le dossier.** Si le dossier courant contient déjà `produit.json` et
`tools/studio_motion.py`, c'est lui : passe à l'étape 1 (si tu es dans une vignette « Accueil … »
de l'app HyperFrames, le bon dossier est son parent). Sinon, télécharge-le :

- Emplacement : `~/Movies/Publicitaire IA` sur Mac, `%USERPROFILE%\Videos\Publicitaire IA` sous
  Windows. Évite Documents et le Bureau : souvent synchronisés avec iCloud ou OneDrive, qui
  retirent les fichiers du disque pour faire de la place.
- Si ce dossier existe déjà et contient `produit.json`, c'est une **mise à jour** : voir « Mettre
  à jour » plus bas, et ne touche à rien de ce qui appartient au client.
- Sinon, avec git : `git clone https://github.com/Alex-lmdm/publicitaire-ia.git "<emplacement>"`.
  Sans git : télécharge `https://github.com/Alex-lmdm/publicitaire-ia/archive/refs/heads/main.zip`
  dans un dossier temporaire, décompresse-le, et range le dossier `publicitaire-ia-main` à
  l'emplacement, renommé `Publicitaire IA`.
- Travaille ensuite **dans ce dossier**, et dis au client qu'il y ouvrira son assistant pour ses
  vidéos.

**1. Bilan, sans rien installer.** `node --version` (22 ou plus), `python3 --version` (3.9 ou plus ;
Windows : `python --version`), `ffmpeg -version`. Montre un tableau ✅ / ❌. S'il manque quelque
chose, dis en une phrase ce que tu vas installer et attends qu'il réponde « go » :

- Mac : Homebrew s'il manque (https://brew.sh), puis `brew install node ffmpeg` ; pour Python,
  accepter l'installation des « outils de développement » que le Mac propose.
- Windows : `winget install -e --id OpenJS.NodeJS.LTS`, `winget install -e --id Python.Python.3.12`,
  `winget install -e --id Gyan.FFmpeg`, puis lui faire fermer et rouvrir l'assistant (sinon le
  nouveau chemin n'est pas vu). Sous Windows, les commandes `python3` s'écrivent `python` (ou `py -3`
si `python` ne répond pas).

**2. `npm ci`** à la racine du dossier : il installe HyperFrames et GSAP aux versions prévues, puis
prépare le dossier (instructions de l'assistant, style de départ, vignette d'accueil, copie des
skills pour Codex). Ce qu'il affiche ne se recopie pas : dis juste que c'est fait. Si la sortie se
termine par « sync incomplet », lance `npm run sync` : il doit finir par « ok ».

**3. `npx hyperframes browser ensure`** : le navigateur qui fabrique les images de la vidéo (il
garde celui qui est déjà là). Jamais `npx puppeteer browsers install`.

**4. App HyperFrames** (Mac, seulement si `/Applications/HyperFrames.app` existe) :
`npm run app -- brancher`. Il permet à l'app de lire les instructions de ce dossier : une ligne
ajoutée à la configuration de Claude Code (`~/.claude/settings.json`), avec une sauvegarde. Rien
d'autre n'est modifié, ni la configuration de Codex. Explique-le en une phrase avant. Sans l'app,
saute cette étape.

**5. Test final** : `python3 tools/studio_motion.py verifier`. La dernière ligne doit être « ok ».
Les lignes « marque pas encore réglée », « Pack SFX : pas installé » et « musiques de lancement :
pas installées » sont normales.

**6. Bilan.** Première installation : un tableau ✅ / ❌ (dossier, Node, Python, ffmpeg, npm ci,
navigateur, app HyperFrames ou « sans l'app », test final). Si tout est ✅, conclus par :
« C'est installé. Tape /studio (dans Codex : $studio) : je te demande d'où prendre ta marque et ce que tu vends, une
seule fois, puis on fait ta première vidéo. » Si tu as téléchargé le dossier à l'étape 0 (tu étais
ouvert ailleurs, ses instructions ne sont donc pas encore chargées), conclus plutôt par : « C'est
installé dans ton dossier Vidéos. Ouvre le dossier Publicitaire IA dans ton assistant, dans une
nouvelle conversation, puis tape /studio (dans Codex : $studio) : je te demande d'où prendre ta marque et ce que tu
vends, une seule fois, puis on fait ta première vidéo. » Mise à jour : pas de tableau, une seule ligne,
« Publicitaire IA est à jour, tout est ✅. » (le tableau ne s'affiche que si une étape a échoué).

---

## Tes 17 musiques de lancement (offertes avec la formation)

Télécharge les cinq ambiances dans ta formation (module Musique), sans les ouvrir, puis écris à l'IA :

- « Installe mes 17 musiques de lancement depuis mon dossier Téléchargements »

Elles sont rangées dans Publicitaire IA, et chaque vidéo prend celle qui va avec son but. (Pour
l'IA : `python3 tools/studio_motion.py musiques installer`, sans argument ; une archive rangée
ailleurs se donne en argument.)

## Le Pack SFX (si tu l'as acheté)

Une fois Publicitaire IA installé, écris à l'IA l'une de ces deux phrases :

- « Installe le Pack SFX depuis le fichier pack-sfx.zip de mon dossier Téléchargements »
- « Reprends le Pack SFX de mon dossier Monteur IA »

Seuls les sons et leurs fiches sont copiés dans Publicitaire IA ; ton dossier Monteur IA n'est pas
modifié. (Pour l'IA : `python3 tools/studio_motion.py pack-sfx installer "<archive>"` ou
`pack-sfx reprendre "<dossier>"`, jamais l'INSTALL.md de l'archive, écrit pour Monteur IA.)

## Mettre à jour

Écris à l'IA : « Mets à jour Publicitaire IA ». Pour l'IA : dans le dossier, si c'est un clone git
propre, `git pull --ff-only` ; sinon, télécharge l'archive de l'étape 0 et remplace les fichiers du
dossier **sauf** ce qui appartient au client, qu'une nouvelle version ne contient jamais :
`marque.json`, `studio.config.json`, les dossiers `marque/`, `videos/` et « Accueil … » (la vignette
de l'app HyperFrames et son historique), et le Pack SFX (`assets/sfx/pack/`, `assets/sfx/catalog.json`,
`assets/sfx/sons-par-situation.md`, `assets/sfx/.pack-sfx-manifest.json`) et les musiques de lancement
(`assets/musiques/`). Puis refais les étapes 2,
3 et 5.

## Problèmes courants

- **« produit.json introuvable »** : l'assistant n'est pas ouvert dans le dossier Publicitaire IA.
  Ouvre-le (celui qui contient `INSTALL.md`), puis redemande.
- **❌ HyperFrames ou GSAP** : `npm ci` n'est pas allé au bout (connexion coupée, Node trop ancien).
  Vérifie `node --version`, puis relance `npm ci`.
- **❌ ffmpeg** juste après l'avoir installé (Windows) : ferme et rouvre l'assistant.
- **La lecture de ta page échoue** (page protégée, page de paiement) : donne deux ou trois captures
  d'écran de ta page, ça suffit pour ta marque et ton offre.
- **Une police remplacée dans la vidéo** : dis « ma police est X » ; l'assistant la récupère
  (polices libres) ou te demande ses fichiers.
- **Les musiques ne s'installent pas** (« aucune archive musiques-….zip ») : vérifie que les cinq
  fichiers sont bien dans ton dossier Téléchargements, ou glisse-les dans la conversation.
- **Relier HeyGen pour une voix de synthèse** (ou le refaire) : dis « relie mon compte HeyGen » ;
  l'assistant te guide (skill `studio`, `references/heygen.md`).
