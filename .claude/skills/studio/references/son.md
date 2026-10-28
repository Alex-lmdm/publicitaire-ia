# Le son

Plus de trois Reels sur quatre se regardent avec le son. Mais chaque vidéo doit aussi se
comprendre muette (stories, métro). Donc : **l'image porte le message, le son le renforce.**

## Ce qui est disponible chez le client

- **Bruitages, dans cet ordre** : le **Pack SFX** s'il est installé dans ce dossier
  (`python3 tools/studio_motion.py pack-sfx` le dit ; 156 sons pro dans `assets/sfx/pack/`, la fiche
  de chacun dans `assets/sfx/catalog.json` : rôle, usage, gain calibré, instant d'impact, prises ;
  la table « quel son pour quoi » dans `assets/sfx/sons-par-situation.md`) ; sinon les bruitages de
  la bibliothèque HeyGen s'il est relié (`heygen bruitages "<description en anglais>"` depuis le
  projet, puis `heygen prendre <n> --bruitage` : le son va dans `assets/sons/`, son instant d'impact
  est affiché) ; ses propres MP3. Les 22 sons de démarrage du dossier
  (`assets/sfx/starter/`, index « à utiliser quand… » dans `sounds.md`, licence CC0) en dernier
  recours : dans une vidéo de motion design, ils sonnent bon marché (retour du créateur,
  12/10/2026) ; peu nombreux et bien placés, ils restent mieux que le silence.
- **Musique** : toute vidéo en a une, c'est elle qui la porte (sans voix, les bruitages seuls
  sonnent maigres). Dans cet ordre : le morceau qu'il a donné (un fichier glissé ici, ou `musique`
  de `marque.json`, rangé dans `marque/`) ; sinon ses **musiques de lancement** (17 morceaux offerts
  avec la formation, dans `assets/musiques/` ; `python3 tools/studio_motion.py musiques` dit
  lesquelles sont installées), choisies comme dit plus bas. Dans l'app HyperFrames aussi : la
  commande `musiques`, jamais `find_music`.
- Musiques pas installées : dis-le une fois, en une phrase : « Tes 17 musiques de lancement ne sont
  pas encore installées : télécharge les cinq ambiances dans ta formation (module Musique), puis
  dis-moi « installe mes musiques ». » En attendant, sa musique ou la vidéo sans musique, en le
  disant.
- La bibliothèque de musiques de HeyGen ne se propose plus : avec un compte gratuit, ses conditions
  interdisent l'usage commercial et publicitaire, et aucune licence claire n'est publiée pour les
  comptes payants. S'il la demande lui-même, préviens-le une fois de ce point, puis
  [heygen.md](heygen.md).
- Ne télécharge jamais une musique d'un site au hasard : les droits ne sont pas garantis. Ne lance
  jamais une génération de musique payante.

## Le Pack SFX (produit vendu à part)

Le client l'installe d'une phrase ; ne suis **jamais** l'INSTALL.md de l'archive (il vise Monteur IA) :

- « Installe le Pack SFX depuis le fichier pack-sfx.zip de mon dossier Téléchargements » :
  `python3 tools/studio_motion.py pack-sfx installer ~/Downloads/pack-sfx.zip` (Windows :
  `%USERPROFILE%\Downloads\pack-sfx.zip`). Seuls les sons et leurs fiches sont copiés.
- « Reprends le Pack SFX de mon dossier Monteur IA » : `python3 tools/studio_motion.py pack-sfx
  reprendre "<dossier Monteur IA>"` (le chemin est dans `marque.json` → `monteur_ia` s'il a déjà
  repris sa marque ; sinon demande-le). Son dossier Monteur IA n'est jamais modifié.

Ensuite, pour chaque geste, cherche d'abord dans `assets/sfx/sons-par-situation.md`, puis
`python3 tools/studio_motion.py pack-sfx chercher <mots>` (« coche », « argent », « whoosh »…) : il
donne le chemin à mettre dans `sons.json` (vu du projet), le gain calibré, l'instant d'impact et
les prises. Un identifiant `:N` de la table désigne la N-ième prise : son `trim` est dans les
`segments` du catalogue. **Un son à plusieurs prises se pose toujours avec le `trim` d'une seule** :
sans lui, toutes ses prises jouent à la suite sous les scènes suivantes (16 traits de feutre sur 11 s
entendus « en fond partout »), et `sons` refuse de le poser. Les identifiants `starter-*` sont les
sons de démarrage du dossier, calibrés de la même façon. Le pack n'est jamais copié dans le dépôt ni dans une livraison : seuls
les sons posés vont dans le projet de la vidéo (`assets/sons/`, fait par `sons`).

## Les musiques de lancement (offertes avec la formation)

17 musiques faites pour les vidéos qui vendent, en cinq ambiances, chacune avec une vraie entrée
de batterie. Le client les installe une fois, d'une phrase : « Installe mes 17 musiques de
lancement depuis mon dossier Téléchargements » (ou toute demande d'installer ses musiques) :

```bash
python3 tools/studio_motion.py musiques installer
```

Depuis la racine. Sans argument, il prend les `musiques-*.zip` du dossier Téléchargements et les
dossiers que Safari a décompressés tout seul ; une archive rangée ailleurs se donne en argument.
Refaire ne change rien, et une ambiance téléchargée plus tard s'ajoute aux autres. Réponds en une
ligne : combien sont installées, et les ambiances qui manquent s'il en manque (il les télécharge
dans sa formation, module Musique). Elles ne sont jamais versionnées ni livrées : seul le morceau
choisi va dans le projet de la vidéo.

## Poser les sons

La commande `sons` écrit les sons dans `index.html` comme des pistes de la timeline (ils
apparaissent dans l'app, le bouton Export sort la vidéo complète). Écris la liste dans
`work/sons.json` (chemins relatifs au projet), puis, depuis le dossier de la vidéo :

```bash
python3 ../../../tools/studio_motion.py sons . work/sons.json
```

```json
{"musique": "assets/audio/musique.wav", "musique_db": -17,
 "evenements": [{"src": "../../../assets/sfx/starter/click-ui.mp3", "start": 1.2, "vol": -6},
                {"src": "assets/audio/whoosh.wav", "start": 3.0, "vol": -9, "trim": [0, 0.6], "fondu_sortie": 0.1}]}
```

Elle écrit à l'emplacement `<!-- SONS -->` de `index.html` et lit la durée de la vidéo. Options
d'un évènement : `trim`, `fondu_entree`, `fondu_sortie`, `af` (un filtre ffmpeg, lis l'en-tête de
`tools/sons.py`). Pour changer les sons ensuite, refais la liste complète et relance `sons` ; `--ecraser` seulement si le bloc a été retouché à la main ou dans l'app. Sans voix, la musique porte la vidéo et les
bruitages la ponctuent : l'équilibre se règle par `emergence` (plus bas), pas à l'oreille. Garde
le mélange assez bas pour que le limiteur de la composition ne travaille pas (dans la vidéo de
démonstration, `musique_db=-17` et les bruitages en proportion), `mastering` remonte le tout. Le module écrit la musique
avec `id="musique"` : c'est ce que retrouve la version sans musique.

## La musique

### Choisir le morceau

Une proposition par vidéo, depuis son projet (le but et le support sont lus dans le projet) :

```bash
python3 ../../../tools/studio_motion.py musiques choisir --duree <durée de la vidéo> --a <pivot> --ouvrir
```

L'outil prend l'ambiance qui va avec le but et le support, écarte les morceaux trop courts (de
l'entrée de la batterie à la fin, ils doivent couvrir la vidéo après le pivot), préfère ceux dont
l'intro couvre le début de la vidéo et ceux qui se recalent à 120, fait passer derrière ceux déjà
pris dans ses autres vidéos, et propose les trois meilleurs, le plus juste en premier :

| But ou support | Ambiance |
|---|---|
| Lancement, vente sur une page | Lancement énergique |
| Révélation, nouveauté | Montée cinématique |
| Fonctionnalité, explication, démo sous une voix | Tech minimale |
| Vente ou inscription en Reel, pub, story | Court et percutant, puis Lancement énergique |
| Témoignage, preuve, offre haut de gamme | Premium et calme |

Le pivot (`--a`, l'instant où la solution apparaît) n'est pas encore fixé ? Laisse-le : l'outil le
suppose vers 20 % de la vidéo, et l'entrée de batterie de chaque morceau, affichée, t'aide à le
placer. Une boucle de section de page est muette : pas de musique.

La page d'écoute s'ouvre dans son navigateur (chaque extrait démarre quelques secondes avant
l'entrée de la batterie). Dis-lui : « Je t'ai ouvert une page avec 3 musiques pour cette vidéo ;
je te conseille la 1. Écoute et réponds par le numéro (ou « choisis » : je prends la 1). » S'il a
dit une fois « choisis toujours pour moi » (préférence de `studio.config.json`), prends la première
sans demander et dis laquelle.

Ses demandes, à tout moment :

- « Prends une musique Tech minimale » (ou une autre ambiance : Lancement énergique, Montée
  cinématique, Court et percutant, Premium et calme ; « plus calme », « plus énergique ») :
  `musiques choisir --ambiance "<ambiance>"`.
- « Fais-moi écouter d'autres musiques », « aucune » : `musiques choisir --autres` (trois qu'il n'a
  pas encore entendues pour cette vidéo).
- « Mets ma musique » (un fichier glissé) : elle passe avant ; range-la dans `assets/audio/`, puis
  `musique <fichier>` l'analyse.

Puis, depuis le projet :

```bash
python3 ../../../tools/studio_motion.py musiques prendre <numéro> --a <pivot> --duree <durée>
```

Le morceau est copié dans `assets/audio/`, sa source notée dans `assets/audio/SOURCE.md`, et il est
calé dans `assets/audio/musique.wav` comme dit ci-dessous (sans `--a`, il est seulement copié). Le
pivot bouge en écrivant le plan ? Refais seulement le calage, avec `musique`.

### Le caler

- **L'entrée franche** du morceau (la batterie qui arrive) tombe sur le pivot : le moment où la
  solution apparaît après le problème (dans la vidéo de démonstration, la première image de
  « Ton nouveau monteur », à 8 s). Avant elle, l'intro calme du morceau porte la tension.
- Cale le morceau avec l'outil, qui mesure son tempo, ses temps forts (l'attaque de la grosse
  caisse) et son entrée, le ramène au tempo de la grille (120 battements par minute, un temps
  toutes les 0,5 s ; au plus 10 % d'écart, inaudible sous 3 %) et le décale pour que l'entrée
  tombe à l'instant voulu, sur un temps fort :

  ```bash
  python3 ../../../tools/studio_motion.py musique assets/audio/morceau.mp3                      # analyse seule
  python3 ../../../tools/studio_motion.py musique assets/audio/morceau.mp3 --sortie assets/audio/musique.wav --a 8 --duree 67
  ```

  Les événements de la vidéo, posés sur la grille de 0,5 s, tombent alors sur les temps.
- L'écran final tombe sur le dernier temps fort, puis la musique s'éteint en fondu (0,8 à 1,5 s).
- Stories : musique facultative ; si oui, la même que le Reel, plus discrète.

## Les bruitages

- **Un son par évènement réel** à l'écran (un clic, une carte qui se pose, un prix qui tombe),
  jamais pour remplir. Un même geste garde le même son (un clic sonne comme un clic) ; varie le
  volume, et ne répète pas un son marquant (impact, riser, cha-ching).
- Calé sur l'image de l'évènement : l'attaque du son (son début audible) au moment exact du
  contact, ou 2 à 3 images avant pour un impact. Un décalage de 0,2 s se voit.
- Dans une cascade (cinq éléments qui tombent), seuls le premier et le dernier sonnent.
- Pas de carillon sur un clic (c'est la signature des vidéos de modèle). Un impact par temps
  fort (le nom de l'offre, le chiffre clé, le prix), jamais deux de suite ; une montée (riser)
  au plus, avant le final ou la révélation.
- Avec une musique forte, un bruitage **par geste visible** : clic du curseur, frappe, coche,
  compteur, passage, impact sur le nom et le prix, et aussi les petits événements du milieu
  (aperçus qui sortent, cartes qui arrivent, pastilles qui confirment). Une minute en porte 110 à
  140, beaucoup très discrets ; en dessous de 90, le milieu sonne vide (retour du créateur). Ils se posent
  par `work/sons.json` ; écris leurs temps par scène (début de la scène + instant de sa timeline),
  par exemple avec un petit script `work/sons.py` qui produit `sons.json`, pour décaler une scène
  sans tout recalculer.
- Avec le Pack SFX : pars du `gain_db` du catalogue et cale le son sur son `hit` quand son `align`
  vaut `hit` (début = instant de l'événement − `hit`). Le pack est calibré pour une musique
  discrète sous une voix : sous une musique qui porte la vidéo, remonte chaque **famille** de ce
  qu'il lui faut (dans la vidéo de démonstration, musique à -17 dB : clics +26 dB, passages et
  impacts +14 à +15, coches +17, puis tout le mélange -7 dB), les clics les plus doux un peu plus.
- **Lisse la pointe des clics** : ceux du pack montent de 19 à 24 dB au-dessus de leur corps. Un
  limiteur sur le son seul (`"af": "alimiter=limit=…:attack=0.1:release=8:level=false"`, plafond
  12 dB au-dessus de son énergie) les garde présents sans que le limiteur final fasse « pomper »
  la musique à chaque clic. `mastering` abaisse ensuite son propre plafond tout seul si l'AAC
  fait déborder une crête au-dessus de -1 dBTP.
- Le mélange posé ne doit jamais faire travailler le limiteur de la composition (crête du rendu
  sous -3 dBTP) : baisse tout le mélange d'un bloc, `mastering` remonte ensuite.
- Contrôle : `python3 ../../../tools/studio_motion.py emergence .` dans le projet. Chaque bruitage doit
  dépasser la musique qui l'entoure de 4 dB au moins (méthode du Pack SFX, sur 50 ms) ; il répond
  « ok » quand 95 % y sont (au plus un son couvert sur vingt, et un seul tant qu'il y en a moins de quarante).
- Évite les sons très aigus en série : ils fatiguent à l'écoute au téléphone.

## Le niveau final

Sans voix, la pose des sons ne règle pas le niveau final : c'est à toi. Après le rendu :

```bash
python3 ../../../tools/studio_motion.py son exports/reel.mp4         # mesure
python3 ../../../tools/studio_motion.py mastering exports/reel.mp4 exports/reel-master.mp4
```

Cible : **-16 LUFS ±1, crêtes sous -1 dBTP**, le même niveau que ses Reels habituels. Le fichier
livré est la version masterisée. Sur des clics très secs, l'encodage fait varier les crêtes d'un
essai à l'autre : `mastering` fait jusqu'à huit essais et garde le meilleur. S'il répond encore ❌,
lis la mesure : une crête trop haute se corrige en baissant les bruitages les plus secs, pas en
relançant.

**Bruitages seuls, sans musique ni voix** : -16 LUFS les fait sonner maigres et trop forts, chaque
clic monté de 12 dB. Vise **-20 LUFS** : `mastering … --cible -20` puis `son … --cible -20`. Mieux :
propose au client d'ajouter une musique, c'est elle qui porte une vidéo sans voix.

Avec musique, la cible reste **-16 LUFS** : la vidéo de démonstration (musique à -17 dB, 87
bruitages du pack) sort à -28,3 LUFS du rendu et passe à -16,1 après `mastering`, crêtes à
-1,2 dBTP. Pour la version web, recompresse l'image et **recopie le son** (`-c:a copy`) : le
réencoder fait remonter les crêtes au-dessus de -1 dBTP.

## La version sans musique du Reel

Beaucoup de créateurs ajoutent un son tendance dans Instagram. Quand le Reel a une musique, livre
`reel-sans-musique.mp4` : mêmes bruitages, pas de musique.
`python3 ../../../tools/studio_motion.py sans-musique .` la rend dans `exports/<vidéo>-sans-musique.mp4`
(le fichier temporaire qu'elle utilise disparaît ensuite).
Refais-le après toute retouche du Reel, puis masterise ce fichier comme l'autre.
