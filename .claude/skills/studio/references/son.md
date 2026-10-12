# Le son

Plus de trois Reels sur quatre se regardent avec le son. Mais chaque vidéo doit aussi se
comprendre muette (stories, métro). Donc : **l'image porte le message, le son le renforce.**

## Ce qui est disponible chez le client

- **Bruitages** : `assets/sfx/starter/` du dossier Monteur IA (22 sons libres de droits, liste dans
  `sounds.md`), plus `assets/sfx/pack/` s'il a le Pack SFX (156 sons rangés par catégorie). Ses
  propres MP3 à la racine de `assets/sfx/`.
- **Musique** : son morceau de fond (`audio.musicFile` de `brand.config.json`, rangé dans
  `assets/music/`). S'il n'en a pas, livre d'abord une version sans musique et propose-lui d'en
  déposer une, ou d'ajouter un son Instagram à la publication (voir la version sans musique).
- Ne télécharge jamais une musique d'un site : les droits ne sont pas garantis.

## Poser les sons

Utilise le module de Monteur IA, qui écrit les sons dans `index.html` comme des pistes de la
timeline (ils apparaissent dans l'app, le bouton Export sort la vidéo complète) :

```bash
python3 -c "import sys; from pathlib import Path; sys.path.insert(0, '<dossier Monteur IA>/tools'); \
import sons; print(sons.poser(Path('.'), [<évènements>], musique=Path('<musique>'), musique_db=-14))"
```

Lance-le depuis le dossier de la vidéo : il écrit à l'emplacement `<!-- SONS -->` de
`index.html` et lit la durée de la vidéo. Un évènement : `{"src": Path(...), "start": s, "vol": dB}`
(lis l'en-tête de `tools/sons.py` pour les options : `trim`, fondus). Pour changer les sons
ensuite, relance avec la liste complète et `ecraser=True`. Sans voix, `musique_db` autour de **-14**
(la musique est le lit de la vidéo, pas un fond sous une voix). Le module écrit la musique
avec `id="musique"` : c'est ce que retrouve la version sans musique.

## La musique

- Le **temps fort** (drop, entrée de la batterie) tombe sur la révélation de l'offre, vers 40 %
  de la durée. Repère-le à l'oreille et par l'énergie (le moment où le volume monte nettement),
  pas sur une grille automatique : elle se trompe souvent de deux temps. Démarre la musique au
  bon endroit du morceau pour que ce temps fort arrive au bon moment de la vidéo.
- Recale les coupes sur les temps à un demi-temps près au plus, seulement si le tempo est net.
- L'écran final tombe sur le dernier temps fort, puis la musique s'éteint en fondu (0,8 à 1,5 s).
- Stories : musique facultative ; si oui, la même que le Reel, plus discrète.

## Les bruitages

- **Un son par évènement réel** à l'écran (un clic, une carte qui se pose, un prix qui tombe),
  jamais pour remplir. Pas plus de deux fois le même son dans une vidéo.
- Calé sur l'image de l'évènement : l'attaque du son (son début audible) au moment exact du
  contact, ou 2 à 3 images avant pour un impact. Un décalage de 0,2 s se voit.
- Dans une cascade (cinq éléments qui tombent), seuls le premier et le dernier sonnent.
- Pas de carillon sur un clic (c'est la signature des vidéos de modèle). Au plus une montée
  (riser) et un impact par vidéo, pour la révélation.
- Évite les sons très aigus en série : ils fatiguent à l'écoute au téléphone.

## Le niveau final

Sans voix, Monteur IA ne règle pas le niveau final : c'est à toi. Après le rendu :

```bash
python3 tools/studio_motion.py son exports/reel.mp4         # mesure
python3 tools/studio_motion.py mastering exports/reel.mp4 exports/reel-master.mp4
```

Cible : **-16 LUFS ±1, crêtes sous -1 dBTP**, le même niveau que ses Reels habituels. Le fichier
livré est la version masterisée.

## La version sans musique du Reel

Beaucoup de créateurs ajoutent un son tendance dans Instagram. Livre toujours
`reel-sans-musique.mp4` : mêmes bruitages, pas de musique.
`python3 <dossier Monteur IA>/tools/studio_motion.py sans-musique .` prépare `index-sans-musique.html`
et affiche la commande de rendu (`npx hyperframes render -c index-sans-musique.html -o …`).
Refais-le après toute retouche du Reel, puis masterise ce fichier comme l'autre.
