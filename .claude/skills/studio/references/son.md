# Le son

Plus de trois Reels sur quatre se regardent avec le son. Mais chaque vidéo doit aussi se
comprendre muette (stories, métro). Donc : **l'image porte le message, le son le renforce.**

## Ce qui est disponible chez le client

- **Bruitages, dans cet ordre** : le **Pack SFX** s'il est installé dans ce dossier
  (`python3 tools/studio_motion.py pack-sfx` le dit ; 156 sons pro dans `assets/sfx/pack/`, la fiche
  de chacun dans `assets/sfx/catalog.json` : rôle, usage, gain calibré, instant d'impact, prises ;
  la table « quel son pour quoi » dans `assets/sfx/sons-par-situation.md`) ; sinon ses propres MP3.
  Les 22 sons de démarrage du dossier
  (`assets/sfx/starter/`, index « à utiliser quand… » dans `sounds.md`, licence CC0) **seulement
  sans le pack** : peu nombreux et bien placés, ils restent mieux que le silence. **Avec le pack, il
  les remplace** : écoutés chacun face à ses remplaçants, 20 sur 22 sonnent bon marché à côté. Seuls
  `starter-pop` et `starter-click-double` restent, en variantes ; `pack-sfx chercher` ne propose plus
  les autres et `sons` les signale.
- **Musique** : toute vidéo en a une, c'est elle qui la porte (sans voix, les bruitages seuls
  sonnent maigres). Dans cet ordre : le morceau qu'il a donné (un fichier glissé ici, ou `musique`
  de `marque.json`, rangé dans `marque/`) ; sinon ses **musiques de lancement** (35 morceaux offerts
  avec la formation, dans `assets/musiques/` ; `python3 tools/studio_motion.py musiques` dit
  lesquelles sont installées), choisies comme dit plus bas. Dans l'app HyperFrames aussi : la
  commande `musiques`, jamais `find_music`. S'il demande son catalogue Epidemic Sound connecté,
  utilise-le à la place de la banque incluse (section suivante).
- Moins de 35 installées : lance d'abord `musiques installer` depuis la racine (il reprend celles
  de Mixkit). Il manque encore les 17 de la formation ? Dis-le une fois, en une phrase : « Il manque
  une partie de tes musiques : colle-moi la phrase « Installe mes musiques de lancement » du module
  Musique de ta formation. » En attendant, choisis parmi celles qui sont là.
- La bibliothèque de HeyGen (musiques et bruitages) ne se propose plus : avec un compte gratuit, ses
  conditions interdisent l'usage commercial et publicitaire, et aucune licence claire n'est publiée
  pour les comptes payants. S'il la demande lui-même, préviens-le une fois de ce point, puis
  [heygen.md](heygen.md) (`heygen bruitages`, `heygen prendre <n> --bruitage`).
- Ne télécharge jamais une musique d'un site au hasard : les droits ne sont pas garantis. Ne lance
  jamais une génération de musique payante.

## Son compte Epidemic Sound, en option

La banque incluse reste le choix par défaut ; un fichier du client passe toujours en premier. S'il demande Epidemic Sound (ou a gardé cette préférence),
cherche avec **son propre compte connecté** par MCP, sans demander sa clé dans la conversation.
Connexion : [epidemic.md](epidemic.md). Aucun abonnement n'est nécessaire pour utiliser les 35.

- Recherche trois directions adaptées à l'offre, au style visuel et à la présence d'une voix.
  Fais écouter les extraits, puis télécharge le morceau retenu avec les outils du MCP. Ne prétends
  pas l'avoir écouté si tu ne l'as pas fait. Ne lance aucune génération ni adaptation payante.
- S'il préfère le site, laisse-le choisir et donner le fichier. Playlist conseillée dans la formation :
  [Sons déformés / Glitchy Sounds](https://www.epidemicsound.com/fr/music/themes/technology/glitchy-sounds/).
- Range le fichier dans `assets/audio/` du projet ; note titre, artiste, identifiant, source et
  licence déclarée dans `SOURCE.md`. Analyse-le comme tout morceau fourni. Un téléchargement ne
  prouve pas à lui seul que son plan couvre une publicité ou une nouvelle publication.
- Les bruitages de son compte sont aussi disponibles à sa demande. Garde leurs sources et la
  même règle de licence ; les fichiers seuls ne se livrent jamais.
- MCP absent : propose le fichier téléchargé sur le site ou accompagne la connexion. N'achète
  rien. Les vidéos publiées pendant la période couverte restent autorisées ; une nouvelle vidéo
  après expiration demande un abonnement actif ou une licence adaptée.

## Le Pack SFX (produit vendu à part)

Le client l'installe d'une phrase ; ne suis **jamais** l'INSTALL.md de l'archive (il vise Monteur IA) :

- « Installe le Pack SFX depuis le fichier pack-sfx.zip de mon dossier Téléchargements » :
  `python3 tools/studio_motion.py pack-sfx installer`, sans argument. Il prend le plus récent des
  `pack-sfx*.zip` de Téléchargements, ou le dossier `pack-sfx` que Safari a décompressé tout seul ;
  une archive ou un dossier rangé ailleurs se donne en argument (`pack-sfx installer
  "<archive ou dossier>"`). Seuls les sons et leurs fiches sont copiés. « macOS refuse l'accès » :
  dis-lui d'autoriser l'app de son assistant dans Réglages Système > Confidentialité et sécurité >
  Fichiers et dossiers, ou de glisser le fichier ici.
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
sons de démarrage du dossier : avec le pack, seuls `starter-pop` et `starter-click-double` se posent
encore. Un son « secours » (`chercher` l'écrit : `ui-check-pop`, `ui-clean-click`, `misc-punch`,
`slice-ring-low`, `misc-error-buzz`, `ui-unlock`, `ui-ping`, jugés moins bons à la même écoute) ne
vient qu'après tous les autres. Le pack n'est jamais copié dans le dépôt ni dans une livraison : seuls
les sons posés vont dans le projet de la vidéo (`assets/sons/`, fait par `sons`).

## Les musiques de lancement (offertes avec la formation)

35 musiques faites pour les vidéos qui vendent, en cinq ambiances. Elles s'installent avec le dossier
(INSTALL.md, étape 5) : 17 viennent de la formation, par le lien personnel de sa phrase ; 18 sont des
musiques de Mixkit (fiche `tools/musiques-mixkit.json`), que l'outil télécharge depuis Mixkit sur son
ordinateur, la licence de Mixkit interdisant qu'on lui en livre les fichiers. Pour le client, c'est
une seule banque : ne lui parle pas de leur origine, sauf s'il le demande. Il colle « Installe mes
musiques de lancement : <lien> » (ou toute demande d'installer ses musiques) :

```bash
python3 tools/studio_motion.py musiques installer --lien "<lien>"
```

Depuis la racine. Sans `--lien`, il reprend le lien noté à l'installation, sinon il prend les
`musiques-*.zip` de Téléchargements (et les dossiers que Safari a décompressés) ; une archive rangée
ailleurs se donne en argument. Les 18 de Mixkit viennent à chaque fois, celles qui manquent seulement.
Refaire ne change rien. Réponds en une ligne : combien sont installées ; lien expiré : il recolle la
phrase du module Musique. Elles ne sont jamais versionnées ni livrées : seul le morceau choisi va dans
le projet de la vidéo, avec sa licence dans `assets/audio/SOURCE.md`.

## Poser les sons

La commande `sons` écrit les sons dans `index.html` comme des pistes de la timeline (ils
apparaissent dans l'app, le bouton Export sort la vidéo complète). Écris la liste dans
`work/sons.json` (chemins relatifs au projet), puis, depuis le projet de la vidéo :

```bash
python3 ../../../tools/studio_motion.py sons . work/sons.json
```

```json
{"musique": "assets/audio/musique.wav",
 "evenements": [{"src": "../../../assets/sfx/starter/click-ui.mp3", "start": 1.2, "vol": -6},
                {"src": "assets/audio/whoosh.wav", "start": 3.0, "vol": -9, "trim": [0, 0.6], "fondu_sortie": 0.1}]}
```

Elle écrit à l'emplacement `<!-- SONS -->` de `index.html` et lit la durée de la vidéo. Options
d'un évènement : `trim`, `fondu_entree`, `fondu_sortie`, `af` (un filtre ffmpeg, lis l'en-tête de
`tools/sons.py`). Pour changer les sons ensuite, refais la liste complète et relance `sons` ; `--ecraser` seulement si le bloc a été retouché à la main ou dans l'app. Le module écrit la musique
avec `id="musique"` : c'est ce que retrouve la version sans musique. Le niveau de la musique se
règle tout seul (section suivante) ; les bruitages se règlent sur elle, par `emergence`, pas à
l'oreille. `mastering` remonte ensuite le tout à -16 LUFS.

## L'équilibre entre la musique, les bruitages et la voix

Le défaut le plus fréquent : des bruitages très forts sur une musique qu'on n'entend presque plus.
La règle :

- **Sans voix, la musique porte la vidéo** : on l'entend bien, du début à la fin. `sons` la pose
  toute seule à sa référence (-30 LUFS avant le mastering, quel que soit le morceau : un morceau
  mastérisé fort est baissé, un morceau doux remonté) et l'écrit : « Musique : … dB, à -30 LUFS ».
  Les bruitages vont **avec** elle, presque au même niveau : chacun dépasse le fond musical de 4 à
  10 dB (vise 5 à 8), jamais plus. `emergence` le vérifie et dit, son par son, de combien monter ou
  baisser. Le réglage par défaut, validé à l'oreille entre +4, +7 et +10 dB : +7 dB en médiane.
- **Ne baisse jamais la musique pour faire ressortir un bruitage** : monte le bruitage, ou
  baisse ceux qui sont trop forts. `"musique_db"` reste un réglage manuel ; `sons` prévient s'il
  enterre la musique de plus de 3 dB sous sa référence (une musique baissée à -24 dB pour faire
  ressortir les bruitages, avec le défaut d'enveloppe ci-dessous, sort 30 dB sous eux).
- **Avec une voix off, la voix passe devant tout** : la musique se tient 15 à 18 LU sous elle
  (« Sous une voix off », plus bas), les bruitages sont moins nombreux (voix.md) et **jamais plus
  forts qu'elle** : `emergence` refuse un bruitage dont la crête dépasse le niveau de la voix qui
  l'entoure.
- Une enveloppe de volume (`data-automation`) **multiplie** `data-volume` depuis HyperFrames 0.9
  (elle le remplaçait avant) : `sons` écrit le niveau dans `data-volume` et la forme (0 à 1) dans
  l'enveloppe. Si tu écris toi-même une enveloppe (le son d'une vraie vidéo, par exemple), fais
  pareil ; le niveau écrit dans les deux est compté deux fois (constaté le 08/11/2026 : 0,5 sous une
  enveloppe à 0,5 sort à -12 dB).
  **Une vidéo posée avant cette correction** (son bloc porte le même niveau dans `data-volume` et
  dans l'enveloppe de la musique) sonne au carré de son réglage : « -10,5 dB » y sort à -21. La
  reposer avec le même `"musique_db"` monte donc la musique d'autant, d'un coup (11/11/2026, story
  d'ouverture : +10,5 dB, alors que le client avait réglé ce niveau à l'oreille). Avant de reposer,
  lis la ligne `<audio id="musique">` : si l'enveloppe ne monte pas à 1, écris dans `"musique_db"`
  le double du réglage (le niveau entendu), puis règle les bruitages dessus. Même piège pour les
  sons à fondu, qui sonnaient plus bas que leur réglage.

## La musique

### Construire l'image sur la bande-son

Avant `PLAN.md` et toute animation, le morceau est choisi, analysé et calé. Avec une voix off,
prépare d'abord ses mots et ses respirations (`voix.md`), puis le morceau. Dans `PLAN.md`, note
les repères **du fichier qui sera posé** : tempo après calage, temps forts, entrée de batterie,
pauses ou ruptures, changements d'énergie, dernier accent et fin. Les outils mesurent le tempo
et l'entrée ; relève les autres repères sur l'onde ou avec `ffmpeg silencedetect`, sans inventer
une écoute. Vérifie les instants dans le fichier final, pas seulement dans la fiche du catalogue.
**Les scènes partent sur les temps** : sans voix, chaque scène commence sur un temps noté dans
`PLAN.md` (la fin de la scène d'avant y tombe, au plus un temps après la durée qu'elle demande) ;
avec une voix, elle commence avec la phrase qui la porte, sur un temps quand c'est possible. Après
le rendu, `calage exports/<vidéo>.mp4` le vérifie sur la vidéo finie ([revue.md](revue.md),
porte 4).

Sans voix, le mouvement suit les phrases musicales : révélation sur une entrée forte, rafale
sur une accélération, attente ou arrêt volontaire dans une pause, écran final sur la résolution.
Avec une voix, les gestes suivent les mots ; les accents musicaux se placent dans ses pauses.
La grille à 120 est un moyen de calage : si le tempo reste différent, construis sur celui-ci.

### Changer de morceau

Toute demande de remplacement comprend le **recalage du motion design** : nouveau fichier dans
`assets/audio/`, source actualisée, analyse, nouveaux repères dans `PLAN.md`, puis coupes,
transitions, moments forts, pauses et fin adaptés. Garde les faits, le message et la marque ;
avec une voix, conserve le calage des gestes sur ses mots. Repose ensuite les bruitages, recalcule
le mixage, puis refais rendu, revue, mastering et livraison (version sans musique comprise).
Ne te contente pas de remplacer `musique.wav` sous des animations restées au même rythme.

Le client peut coller, avec son nouveau fichier :

> Remplace la musique de cette vidéo par ce fichier et recale tout le motion design dessus : tempo,
> temps forts, pauses, révélation et fin. Garde le message, la marque et la voix off si j'en ai une.
> Refais les bruitages, le mixage et la livraison.

### Choisir le morceau

Une proposition par vidéo, depuis son projet (le but et le support sont lus dans le projet), sur
la même page que les styles (le style se choisit avec la musique, dans le message du script : SKILL.md, étape 3 bis) :

```bash
python3 ../../../tools/studio_motion.py musiques choisir --duree <durée de la vidéo> --a <pivot> --ouvrir
```

Sans `--style`, la page marque ton conseil sur le style 0 (« Sur mesure », le style maison, dont la
musique suit le but et le support) ; `--style <N>` le marque sur un des 8, et les trois musiques
suivent alors son ambiance (section 8 de sa fiche) ; un style déjà connu (demandé d'emblée, ou gardé dans ses préférences) :
`--sans-styles` (avec `--style <N>` pour garder son ambiance), la page ne montre que les musiques.
Sans musiques de lancement installées, ou si aucune ne couvre la vidéo, elle ne montre que les styles.

L'outil prend l'ambiance qui va avec le but et le support, écarte les morceaux trop courts (de
l'entrée de la batterie à la fin, ils doivent couvrir la vidéo après le pivot), préfère ceux dont
l'intro couvre le début de la vidéo, ceux dont l'entrée franche peut tomber sur le pivot et ceux qui
se recalent à 120, fait passer derrière ceux déjà pris dans ses autres vidéos, et propose les trois
meilleurs, le plus juste en premier :

| But ou support | Ambiance |
|---|---|
| Lancement, vente sur une page | Lancement énergique |
| Vente sur une page **avec voix off** | Tech minimale, Premium et calme (feutrées : la musique passe sous un argument qu'on écoute) |
| Révélation, nouveauté | Montée cinématique |
| Fonctionnalité, explication, démo sous une voix | Tech minimale |
| Vente ou inscription en Reel, pub, story | Court et percutant, puis Lancement énergique |
| Témoignage, preuve, offre haut de gamme | Premium et calme |

Le pivot (`--a`, l'instant où la solution apparaît) n'est pas encore fixé ? Laisse-le : l'outil le
suppose vers 20 % de la vidéo, et l'entrée de batterie de chaque morceau, affichée, t'aide à le
placer. Une boucle de section de page est muette : pas de musique, la page ne montre que les styles.

La page s'ouvre dans son navigateur : le style 0 et les 9 styles en vidéo, puis les 3 musiques
(chaque extrait démarre quelques secondes avant l'entrée de la batterie). Dis-lui, à la suite du script : « Je t'ai ouvert
une page avec les styles et 3 musiques pour cette vidéo ; je te conseille le style 0, « Sur mesure »,
notre style maison, construit pour ta vidéo, et la musique 1. Réponds par exemple « ok, 0, 1 » : ok
pour le script, puis le style, puis la musique (ou « ok, choisis » : je prends mes conseils). Aucun ne te plaît ? Décris ce que tu veux. » Sans styles sur la page : « …
3 musiques ; je te conseille la 1. Réponds par le numéro. » S'il a dit une fois « choisis toujours
pour moi » (préférence de `studio.config.json`), prends la première musique sans demander et dis
laquelle.

Ses demandes, à tout moment :

- « Prends une musique Tech minimale » (ou une autre ambiance : Lancement énergique, Montée
  cinématique, Court et percutant, Premium et calme ; « plus calme », « plus énergique ») :
  `musiques choisir --ambiance "<ambiance>"`.
- « Fais-moi écouter d'autres musiques », « aucune » : `musiques choisir --autres` (trois qu'il n'a
  pas encore entendues pour cette vidéo ; `--sans-styles` si son style est déjà choisi).
- « Mets ma musique », « Mets cette musique dans ma vidéo » (un fichier glissé, ou le morceau le
  plus récent de ses Téléchargements) : elle passe avant les musiques de lancement. Dite pendant une
  vidéo, elle vaut **pour cette vidéo** : range-la dans `assets/audio/` de son projet, note sa
  source dans `assets/audio/SOURCE.md`, puis `musique <fichier>` l'analyse et la cale (« Le caler »,
  plus bas). Elle ne devient sa musique de marque, pour toutes ses vidéos (`marque regler --musique
  "<fichier>"`), que s'il le demande (« garde-la pour toutes mes vidéos »).
- Aucune ne lui plaît : `musiques choisir --autres` jusqu'à ce qu'il n'y en ait plus ; puis sa propre
  musique (« Mets ma musique »).

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
- **Sans entrée franche** (la batterie part dès la première seconde, fréquent, Mixkit compris),
  l'analyse dit « pas d'entrée franche » et la même commande cale le **premier temps fort du
  morceau au début de la vidéo** : `--a` ne sert alors à rien, le message le dit. Recalé à 120, chaque
  temps tombe sur la grille de 0,5 s ; un tempo trop loin de 120 est gardé, et le message donne
  l'écart entre deux temps : cale les événements forts dessus. Le pivot se marque alors à l'image
  (un impact, un changement de fond), pas par la musique.
- **Le tempo qui fait foi est celui du morceau entier**, que `musique` note dans le fichier calé.
  Sur une basse syncopée (une 808, une drill), `calage` peut lire un autre tempo sur la vidéo : un
  rapport simple (3/4, 2/3, 1/2), qu'il corrige seul (« tempo lu … »), ou un léger écart (120,76
  au lieu de 120) qui le fait voir des scènes « à 0,05 à 0,20 s du temps », de plus en plus près au
  fil de la vidéo. Dans les deux cas, ce n'est pas le montage : laisse les scènes sur la grille de
  0,5 s calée par `musique`, ne les recale jamais sur ce faux tempo, et écris-le dans `PLAN.md` (un
  P1 expliqué, revue.md). Un fichier calé par une version plus ancienne ne porte pas son tempo :
  refais-le avec `musique`. Le geste fort sur l'entrée franche, lui, est un vrai défaut quand
  `calage` le relève (un clic seul ne suffit pas : un flash, des mots qui changent d'un coup).
- **Une grosse caisse en 3-3-2** (trap, reggaeton : une attaque toutes les trois doubles croches) fait lire les
  4/3 du vrai tempo, même sur le morceau entier (10/11/2026 : « Attitude », 103,8 lu 139,8, et l'entrée franche
  lue à 4,49 s au lieu de 4,60 s). `musique` note alors ce faux tempo, que `calage` reprend. Avant d'écrire le
  plan, vérifie sur l'onde : les grosses caisses qui reviennent à écart fixe donnent la mesure (ici 2,31 s, soit
  4 temps à 103,8), et le nombre de mesures entre deux entrées tombe rond. Un tempo noté faux se réécrit dans le
  fichier calé (`ffmpeg -i musique.wav -c copy -metadata comment="publicitaire-ia tempo=103.76" corrige.wav`).
  Trois temps du vrai tempo valent quatre du faux : des scènes posées sur ces multiples tombent juste.
- **Un morceau trap d'Epidemic Sound** (13/11/2026, « Sand Box », 85 BPM) : `musique` lisait 103,7 BPM et une
  entrée franche à 6,73 s, toutes deux fausses. Le fichier d'Epidemic porte son vrai tempo dans ses étiquettes
  (`ffprobe -show_entries format_tags` : `TBPM=85`) ; l'onde le confirme (la mesure de 2,82 s revient). La vraie
  entrée (la basse qui revient après deux mesures sans elle, à 21,512 s) se trouve à l'onde, graves seuls
  (`lowpass=f=150`, énergie par tranches de 50 ms). Cale alors à la main avec les fonctions de l'outil
  (`calage(entree, entree, bpm, 0, a)` puis `filtres_calage`), et note `tempo=85.00` dans le fichier calé. Même
  ainsi, `calage` lit la grille de ce morceau avec un demi-temps de décalage et refuse une coupe posée sur le vrai
  temps : garde-la, et écris-le dans `PLAN.md` (un P1 expliqué).
- **Un morceau monté** (deux passages raccordés par une pause, pour finir sur sa vraie fin) : après la coupe,
  les temps ne prolongent plus ceux du début, et `calage` garde la grille du début. Cale les scènes d'après sur
  les attaques mesurées dans le fichier posé (la première grosse caisse du refrain, l'accord final) et écris-le
  dans `PLAN.md` (un P1 expliqué).
- **Avec une voix, `calage` peut lire un faux tempo sur le mélange** (11/11/2026, story « prompt secret » :
  143,5 lu au lieu de 120, sans rapport simple) et refuser une scène qui part pile sur l'entrée franche qu'il
  mesure lui-même. Si la scène part à l'instant de `"musique_entree"` (posé par `musique` sur un temps fort),
  ne la déplace pas : écris-le dans `PLAN.md` (un P1 expliqué).
- L'écran final tombe sur le dernier temps fort, puis la musique s'éteint en fondu (0,8 à 1,5 s).
- Stories : la même musique que le Reel, comme toute vidéo (elle se regarde souvent muette : tout
  s'y lit sans le son).

### Sous une voix off

D'après une recherche (normes de diffusion, tests d'écoute, studios d'explainer, plateformes) et
un essai sur une vraie vidéo de vente. Oui, une musique sous toute voix off, mais une musique
qui travaille **en dessous** :

- **L'écart, réglé tout seul par `sons`.** Pendant que la voix parle, la musique se tient à **18 LU**
  sous la voix sur une page de vente, YouTube ou LinkedIn, à **15 LU** dans un Reel, une pub, une
  story ; quand la voix se tait, elle remonte à 8 LU (page) ou 6 LU (Reel) sous elle. L'outil mesure
  le morceau (sa section la plus forte sous la voix) : plus de gain fixe, l'écart tient quel que soit
  le morceau. Une version accessible (public âgé ou malentendant) : `"musique_ecart": 20` dans
  `sons.json`. `"musique_db"` reste un réglage manuel, qui prime.
- **Le ducking : une courbe calculée sur les pauses de la voix**, jamais un compresseur. Une pause de
  moins de 1,5 s ne fait pas remonter la musique (elle pomperait) ; une respiration d'au moins 1,5 s,
  le temps avant le premier mot (s'il arrive après 1,5 s) et la fin après le dernier mot la font
  remonter. L'entrée franche du morceau (`musiques prendre --a`, ou `"musique_entree"` dans
  `sons.json`) qui tombe dans une respiration est précédée d'un creux de 0,3 s : le temps fort sonne
  plus fort par contraste. La pose l'écrit : « Musique sous la voix : … dB, 18 LU sous la voix… ».
- **Une respiration au pivot.** Une voix de synthèse n'en laisse aucune : ouvre-la dans la voix
  (`voix respiration`, voix.md) **avant** de caler la musique, pour que la batterie entre dans le
  silence et pas sous le nom de l'offre (sur l'essai, elle tombait pile sous « grâce à Publicitaire
  IA »).
- **Le morceau.** Instrumental, sans voix chantée ni mélodie en avant sous les explications (pas de
  sifflement, de piano ou de synthé solo), une pulsation stable, une humeur positive pour vendre. Un
  seul morceau par vidéo. Évite les clichés : ukulélé et sifflement, crescendo orchestral, montée
  électro prévisible, morceau de bande-annonce.
- **La fin** : la musique remonte après le dernier mot et s'éteint en 2 s, en courbe douce.
- **Le niveau final** : -16 LUFS comme toujours ; avec une voix, les crêtes sont plafonnées à
  -2 dBTP (les plateformes réencodent le fichier). `mastering` et `son` le font seuls quand `sons` a
  posé la voix ; une voix posée à la main se signale avec `--voix`.
- **Un aperçu fait à la main** (un mélange ffmpeg pour faire écouter des musiques sous la voix) passe
  la voix mono en stéréo par `pan=stereo|c0=c0|c1=c0`, jamais `aformat` : `aformat` la joue 3 dB plus
  bas que le rendu et fausse l'écart (des aperçus à 10 LU, trop forts).

## Les bruitages

- **Un son par évènement réel** à l'écran (un clic, une carte qui se pose, un prix qui tombe),
  jamais pour remplir. Un même geste garde la même **famille** (un clic sonne comme un clic), mais
  pas le même fichier : **jamais le même son deux fois de suite** à moins de 3 s, ni trois fois en
  6 s. Une série (les coches, les formats qui arrivent, les clics d'une démo) alterne deux ou trois
  sons voisins de la famille (`click-mouse-click`, `click-mac-single`, `click-mouse-deep`,
  `click-mouse-light` ; `ui-pop-up`, `starter-pop`, `ui-bubble-pop`, `click-single-snap` ; pour un
  élément qui se pose, `click-single-snap`, `camera-lens-cap` et ses 5 prises, `paper-paper-slide`).
  Jamais un son de démarrage écarté pour varier une série : c'est par là qu'ils entraient. Ne répète
  pas un son marquant (impact, riser, cha-ching) : le même bruitage plusieurs fois d'affilée
  lasse vite. Un son qui revient plus loin change
  un peu de hauteur à chaque retour, tout seul (`sons` le prépare : 4 % plus aigu, 3 % plus grave…) ;
  `"hauteur": 1` dans l'évènement le garde tel quel, `"hauteur": 1.1` en choisit une. La règle des
  3 s et des 6 s ne change pas.
- **Après une cassure forte, sous une voix** (11/11/2026, Reel écran Publicitaire IA) : quand la
  musique devient dense (batterie pleine), un bruitage ne peut plus être à la fois 4 dB au-dessus
  d'elle et sous la voix ; `emergence` dit « faible », puis, une fois monté, « plus fort que la
  voix ». La voix passe d'abord : garde seulement les gestes forts (impact sur le nom, clic d'envoi,
  notification), juste sous la voix, retire les petits bruitages que la batterie couvre de toute
  façon, et écris le refus d'`emergence` restant dans `PLAN.md` (un P1 expliqué). Ne baisse pas la
  musique pour eux.
- **Les sons qui trompent** : certains noms du pack cachent une rafale. `click-short-snap` n'est pas
  un claquement sec mais un snap suivi d'un **cliquet de molette** (12 petits tics, entendus « tic
  tic tic » par le client : posé 11 fois, il a gâché la story v3) ; `click-hard` fait trois clics ;
  `click-click-sequence`, `click-click-whoosh`, `click-fast-burst` et `ui-counter-tick` sont des
  rafales. Pour un mot qui claque : `click-hard` rogné à `[0, 0.2]`, `click-single-snap` ;
  `misc-punch` en secours seulement. Le pack a peu d'accents secs : un par temps fort, la variation
  de hauteur fait le reste. `sons` prévient de ces pièges, de chaque répétition (« bruitages qui
  lassent ») et des sons de démarrage que le pack remplace : corrige-les avant le rendu.
- Calé sur l'image de l'évènement : l'attaque du son (son début audible) au moment exact du
  contact, ou 2 à 3 images avant pour un impact. Un décalage de 0,2 s se voit.
- Dans une cascade (cinq éléments qui tombent), seuls le premier et le dernier sonnent.
- Pas de carillon sur un clic (c'est la signature des vidéos de modèle). Un impact par temps
  fort (le nom de l'offre, le chiffre clé, le prix), jamais deux de suite ; une montée (riser)
  au plus, avant le final ou la révélation.
- Avec une musique forte, un bruitage **par geste visible** : clic du curseur, frappe, coche,
  compteur, passage, impact sur le nom et le prix, et aussi les petits événements du milieu
  (aperçus qui sortent, cartes qui arrivent, pastilles qui confirment). Une minute en porte 110 à
  140, beaucoup très discrets ; en dessous de 90, le milieu sonne vide. Ils se posent
  par `work/sons.json` ; écris leurs temps par scène (début de la scène + instant de sa timeline),
  par exemple avec un petit script `work/sons.py` qui produit `sons.json`, pour décaler une scène
  sans tout recalculer.
- Avec le Pack SFX : pars du `gain_db` du catalogue et cale le son sur son `hit` quand son `align`
  vaut `hit` (début = instant de l'événement − `hit`). Le pack est calibré pour une musique
  discrète sous une voix : sous une musique qui porte la vidéo (à sa référence de -30 LUFS),
  remonte chaque **famille** de ce qu'il lui faut (dans la vidéo de démonstration : clics +26 dB,
  passages et impacts +14 à +15, coches +17, puis tout le mélange -7 dB), les clics les plus doux
  un peu plus, puis ajuste chaque son d'après `emergence`.
- **Lisse la pointe des clics** : ceux du pack montent de 19 à 24 dB au-dessus de leur corps. Un
  limiteur sur le son seul (`"af": "alimiter=limit=…:attack=0.1:release=8:level=false"`, plafond
  12 dB au-dessus de son énergie) les garde présents sans que le limiteur final fasse « pomper »
  la musique à chaque clic. `mastering` abaisse ensuite son propre plafond tout seul si l'AAC
  fait déborder une crête au-dessus de -1 dBTP.
- Le mélange posé ne doit jamais faire travailler le limiteur de la composition (crête du rendu
  sous -3 dBTP) : baisse tout le mélange d'un bloc, `mastering` remonte ensuite.
- Contrôle : `python3 ../../../tools/studio_motion.py emergence .` dans le projet. La crête de chaque
  bruitage (sur 50 ms, méthode du Pack SFX) doit dépasser le fond musical qui l'entoure de 4 à
  10 dB : en dessous il est couvert, au-dessus il écrase la musique. Il répond « ok » quand 95 %
  sont dans la fourchette de chaque côté (au plus un son sur vingt, et un seul tant qu'il y en a
  moins de quarante), et donne pour chaque son dehors le réglage qui le ramène entre 5 et 8. Avec
  une voix, aucun bruitage ne dépasse la voix qui l'entoure. Depuis le 08/11/2026, la crête se
  mesure sur les bruitages seuls : sur le mélange, les coups de grosse caisse d'un morceau rythmé
  passaient pour le bruitage.
- **Un bruitage posé dans un silence du morceau** (la montée et l'impact juste avant une entrée franche) :
  `emergence` le compare à un fond presque muet et demande de le baisser à chaque mesure, sans fin (10/11/2026 :
  un impact descendu à -30 dB en cinq passes). Règle-le à la main sur un son du même rôle posé en plein refrain.
  Et `alimiter` refuse un plafond sous 0,0625 : écris-le avec quatre décimales.
- **Sous une voix, sur une basse 808** (13/11/2026, story « vente », 33 bruitages) : `emergence` trouvait des
  sons longs (whoosh épais, page tournée, machine à écrire, impact grave) à la fois « trop faibles » sous la
  musique et « plus forts que la voix » dès qu'on les remontait : la basse les masque, la voix non. Ne règle pas en
  boucle sur ses conseils (trois passes l'ont fait osciller, un clavier monté à +1,7 dB) : repars des niveaux
  d'origine, une seule passe, la voix d'abord ; retire ces sons longs ou remplace-les par un son plus aigu du même
  rôle. Ceux qu'il dit « plus forts que la voix » dans un silence de la voix (une respiration, après le dernier
  mot) relèvent du piège ci-dessus : garde-les.
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

Avec musique, la cible reste **-16 LUFS** : la vidéo de démonstration (musique vers -30 LUFS, 87
bruitages du pack) sort à -28,3 LUFS du rendu et passe à -16,1 après `mastering`, crêtes à
-1,2 dBTP. Pour la version web, recompresse l'image et **recopie le son** (`-c:a copy`) : le
réencoder fait remonter les crêtes au-dessus de -1 dBTP.

## La version sans musique du Reel

Beaucoup de créateurs ajoutent un son tendance dans Instagram. Quand le Reel a une musique, livre
`reel-sans-musique.mp4` : mêmes bruitages, pas de musique.
`python3 ../../../tools/studio_motion.py sans-musique .` la rend dans `exports/<vidéo>-sans-musique.mp4`
(le fichier temporaire qu'elle utilise disparaît ensuite).
Refais-le après toute retouche du Reel, puis masterise-le à **-20 LUFS** (des bruitages seuls :
`mastering … --cible -20`, « Le niveau final »), avant `couverture`.
