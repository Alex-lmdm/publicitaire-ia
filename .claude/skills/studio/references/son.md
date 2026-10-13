# Le son

Plus de trois Reels sur quatre se regardent avec le son. Mais chaque vidéo doit aussi se
comprendre muette (stories, métro). Donc : **l'image porte le message, le son le renforce.**

## Ce qui est disponible chez le client

- **Bruitages, dans cet ordre** : le **Pack SFX** s'il est installé (`assets/sfx/pack/`, 156 sons
  pro, et `assets/sfx/catalog.json` qui donne pour chacun son rôle, son gain calibré et son instant
  d'impact ; table « quel son pour quoi » dans le skill `pack-sfx`) ; sinon la bibliothèque de
  sons de HeyGen (`find_sound_effect` dans l'app, ou l'API avec son compte, `type=sound_effects`) ;
  ses propres MP3. Les 22 sons de démarrage (`assets/sfx/starter/`) en dernier recours seulement :
  dans une vidéo de motion design, ils sonnent bon marché (retour du créateur, 12/10/2026).
- **Musique** : son morceau de fond (`audio.musicFile` de `brand.config.json`, rangé dans
  `assets/music/`), ou la **bibliothèque de musiques de HeyGen** : dans l'app HyperFrames par
  `find_music` ; hors de l'app, par l'API avec son compte HeyGen (`npx hyperframes auth status`
  dit s'il est connecté). La recherche est gratuite : vérifie-le une fois (son solde ne bouge
  pas) et ne lance jamais une génération payante sans son accord. Décris le morceau en anglais,
  par l'énergie et le tempo (« upbeat modern product-launch track, 120 BPM, no vocals »), et
  prends un morceau **plus long que la vidéo**. Note sa source dans `assets/audio/SOURCE.md`.
- Une vidéo de motion design sans voix a besoin d'une musique : sans elle, les bruitages sonnent
  maigres. S'il n'y en a pas, livre la version sans musique et dis-le.
- Ne télécharge jamais une musique d'un site au hasard : les droits ne sont pas garantis.

## Poser les sons

Utilise le module de Monteur IA, qui écrit les sons dans `index.html` comme des pistes de la
timeline (ils apparaissent dans l'app, le bouton Export sort la vidéo complète) :

```bash
python3 -c "import sys; from pathlib import Path; sys.path.insert(0, '<dossier Monteur IA>/tools'); \
import sons; print(sons.poser(Path('.'), [<évènements>], musique=<Path('…') ou None>, musique_db=-14))"
```

Lance-le depuis le dossier de la vidéo : il écrit à l'emplacement `<!-- SONS -->` de
`index.html` et lit la durée de la vidéo. Un évènement : `{"src": Path(...), "start": s, "vol": dB}`
(lis l'en-tête de `tools/sons.py` pour les options : `trim`, fondus). Pour changer les sons
ensuite, relance avec la liste complète et `ecraser=True`. Sans voix, la musique porte la vidéo et les
bruitages la ponctuent : l'équilibre se règle par `emergence` (plus bas), pas à l'oreille. Garde
le mélange assez bas pour que le limiteur de la composition ne travaille pas (dans la vidéo de
démonstration, `musique_db=-17` et les bruitages en proportion), `mastering` remonte le tout. Le module écrit la musique
avec `id="musique"` : c'est ce que retrouve la version sans musique.

## La musique

- **L'entrée franche** du morceau (la batterie qui arrive) tombe sur le pivot : le moment où la
  solution apparaît après le problème (dans la vidéo de démonstration, la première image de
  « Ton nouveau monteur », à 8 s). Avant elle, l'intro calme du morceau porte la tension.
- Cale le morceau avec l'outil, qui mesure son tempo, ses temps forts (l'attaque de la grosse
  caisse) et son entrée, le ramène au tempo de la grille (120 battements par minute, un temps
  toutes les 0,5 s ; au plus 10 % d'écart, inaudible sous 3 %) et le décale pour que l'entrée
  tombe à l'instant voulu, sur un temps fort :

  ```bash
  python3 tools/studio_motion.py musique assets/audio/morceau.wav                      # analyse seule
  python3 tools/studio_motion.py musique assets/audio/morceau.wav --sortie assets/audio/musique.wav --a 8 --duree 67
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
  depuis une liste écrite dans `work/sons_page.py`, temps par scène (début de la scène + instant
  de la timeline), pour décaler une scène sans tout recalculer.
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
- Contrôle : `python3 tools/studio_motion.py emergence .` dans le projet. Chaque bruitage doit
  dépasser la musique qui l'entoure de 4 dB au moins (méthode du Pack SFX, sur 50 ms) ; il répond
  « ok » quand 95 % y sont.
- Évite les sons très aigus en série : ils fatiguent à l'écoute au téléphone.

## Le niveau final

Sans voix, Monteur IA ne règle pas le niveau final : c'est à toi. Après le rendu :

```bash
python3 tools/studio_motion.py son exports/reel.mp4         # mesure
python3 tools/studio_motion.py mastering exports/reel.mp4 exports/reel-master.mp4
```

Cible : **-16 LUFS ±1, crêtes sous -1 dBTP**, le même niveau que ses Reels habituels. Le fichier
livré est la version masterisée.

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
`python3 <dossier Monteur IA>/tools/studio_motion.py sans-musique .` prépare `index-sans-musique.html`
et affiche la commande de rendu (`npx hyperframes render -c index-sans-musique.html -o …`).
Refais-le après toute retouche du Reel, puis masterise ce fichier comme l'autre.
