# Publicitaire IA : des vidéos en motion design qui vendent ton offre, partout où tu publies

Un dossier à télécharger, à ouvrir dans **Claude Code** ou **Codex**, et qui fabrique tes vidéos en
motion design sur ton ordinateur, avec ton abonnement Claude ou ChatGPT
habituel. Pas d'abonnement en plus.

Tu vends une formation, un coaching, un logiciel, un template ? Tu écris « Fais-moi une nouvelle
vidéo » (raccourci : `/studio`, dans Codex `$studio`). Ton assistant
te pose quelques questions à choix (une seule fois sur ta marque et ce que tu vends, puis à chaque
vidéo : le but et où tu vas la mettre), et fabrique la vidéo.

**Du texte à l'écran et de la musique, par défaut.** Tu n'as rien à enregistrer : la musique vient
de tes 17 musiques de lancement (offertes avec la formation, utilisables dans tes pubs). À chaque
vidéo, ton assistant prend celles qui vont avec son but, tu écoutes et tu choisis, et il cale
l'entrée de la batterie au moment où ton offre apparaît. Une voix off s'ajoute quand tu veux, même
sur une vidéo déjà faite : ta voix enregistrée au téléphone, ou une voix de synthèse HeyGen
(quelques centimes).

**Ta marque en une question.** La première fois (« Personnalise Publicitaire IA à ma marque »), il
te demande d'où la prendre : le lien de
ta page de vente (il en tire tes couleurs, tes polices et ton logo), des images, une vidéo dont tu
aimes le style, ou ton dossier Monteur IA si tu en as un (il reprend ses réglages sans y toucher).
Il te montre le résultat ; tu dis « ok » ou ce qui cloche.

**Pour tous les buts**

- vendre ton offre (la vidéo du haut de ta page de vente, un Reel de vente, une pub) ;
- annoncer une nouveauté (un module, une fonction, un bonus) ;
- montrer une fonctionnalité précise (une boucle muette pour une section de ta page) ;
- ton lancement (teaser, ouverture, relance, dernier jour) ;
- faire s'inscrire (guide gratuit, liste d'attente, live) ;
- expliquer comment ça marche ;
- mettre en valeur un témoignage ou un résultat.

**Sur tous les supports**, chacun avec son format, ses zones de sécurité et sa bonne durée :
Reel, story, TikTok et Shorts, pub plein écran ou dans le fil, page de vente (en haut ou dans une
section), LinkedIn, X, YouTube. La même vidéo se décline d'un support à l'autre, remise en page,
pas recadrée.

**Ce qui fait la différence**

1. **Une structure qui vend**, choisie selon le but : le problème avant le produit, une promesse
   claire, une démonstration, une preuve, un appel à l'action adapté au support.
2. **Un motion design de niveau studio** : il se passe quelque chose toutes les demi-secondes,
   très peu de texte, ton produit et les outils que tu utilises à l'écran, des fonds qui
   alternent.
3. **Rien d'inventé** : ton assistant lit ta page de vente et te montre ce qu'il a compris ; c'est
   tout ce que tes vidéos auront le droit d'affirmer.
4. **Chaque vidéo regardée avant toi** : rythme mesuré, planche de contrôle avec les zones de
   chaque plateforme, revue critique, son réglé au niveau des Reels, vérification de l'export.
5. **Prête à publier** : la vidéo, le texte de publication de chaque plateforme, la couverture ou
   l'affiche, la façon de la poser sur ta page, le calendrier d'un lancement.

**8 templates de vidéos de lancement** : des looks repris de vraies vidéos de logiciels (Firecrawl,
Polymarket, Cursor…), refaits pour ta marque. « Fais-moi une vidéo dans le template 3 » : ton
assistant part de ses scènes, avec ton offre et tes couleurs. Une vidéo qui n'est pas dans la liste ?
Donne son lien (YouTube, TikTok, Instagram, X), il en reprend le rythme et la mise en scène.

Tu retouches chaque vidéo en une phrase. Sur Mac et Windows, l'app HyperFrames (gratuite, en option)
te permet aussi de la regarder et de la retoucher à la souris.

## Installation

Dans Claude Code ou Codex : « Télécharge Publicitaire IA depuis
https://github.com/Alex-lmdm/publicitaire-ia et suis les instructions d'installation de son
INSTALL.md ». Détail : [INSTALL.md](INSTALL.md). Il faut Node 22 ou plus, Python 3.9 ou plus et
ffmpeg (l'IA les installe avec ton accord) ; l'app HyperFrames est en option.

**Les 17 musiques de lancement** (offertes avec la formation) s'installent d'une phrase, une fois
les cinq ambiances téléchargées : « Installe mes 17 musiques de lancement depuis mon dossier
Téléchargements ».

**Le Pack SFX** (156 bruitages pro, vendu à part) s'ajoute d'une phrase : « Installe le Pack SFX
depuis le fichier pack-sfx.zip de mon dossier Téléchargements », ou « Reprends le Pack SFX de mon
dossier Monteur IA ».

## Contenu

- `.claude/skills/studio/` : la méthode (bienvenue et marque, fiche de l'offre, repérage,
  structures par but, idées, écriture, supports, voix, rythme, style, kit, recettes, son, revue,
  livraison). `.claude/skills/hyperframes-*` : le contrat de composition, les effets et les
  commandes de HyperFrames (copies de la version 0.8.136, licence Apache 2.0).
- `tools/studio_motion.py` : marque, création des vidéos par support et par format, vérification
  de la fiche, analyse d'une vidéo de référence, logos des outils, temps de lecture, zones,
  planche, rythme, calage de la musique, pose et émergence des sons, mastering, couverture,
  export, livraison. `tools/heygen.py` : la bibliothèque de musiques et les voix de HeyGen, avec
  le compte du client. `tools/marque.py` : lecture de la marque (page, images, vidéo, Monteur IA).
  `tools/pack_sfx.py` : installation du Pack SFX et recherche dans son catalogue.
  `tools/musiques.py` : installation des musiques de lancement et choix selon le but de la vidéo.
  `tools/sons.py` : écriture des sons dans la vidéo. Python 3.9+, sans dépendance.
- `scripts/` : `sync.mjs` (prépare le dossier après `npm ci`), `app-hyperframes.mjs` (ouvre une
  vidéo dans l'app HyperFrames).
- `templates/` : le point de départ de chaque vidéo, le kit de briques de motion design, la
  vignette d'accueil et le modèle des instructions de l'assistant.
- `assets/` : deux polices libres (Inter, Anton) et 22 sons de démarrage (CC0).
- `tests/` : `python3 -m unittest discover -s tests` (Windows : `python`) et `npm test`.

Ce qui t'appartient reste chez toi et n'est jamais remplacé par une mise à jour : `marque.json` et
`marque/` (ta marque), `studio.config.json` (ton profil), `videos/` (tes vidéos), et le Pack SFX
si tu l'as installé (`assets/sfx/pack/` et ses fiches), tes musiques de lancement (`assets/musiques/`).
Rien de tout ça n'est dans le dépôt. Ta clé
HeyGen, si tu en relies une, reste hors du dossier, dans `~/.heygen/credentials`.

## Pour l'éditeur

- Nom, code et dépôt dans `produit.json` : les instructions de l'assistant, la vignette d'accueil
  et les messages des outils les lisent là ; README, INSTALL et le skill les écrivent en toutes
  lettres, et un test vérifie qu'ils disent la même chose (et qu'aucun ancien nom ne traîne). Le
  skill s'appelle `studio` (commande `/studio`), l'outil `tools/studio_motion.py`.
- Version : [VERSION](VERSION) (et `package.json`). Crédits et licences : [CREDITS.md](CREDITS.md).
