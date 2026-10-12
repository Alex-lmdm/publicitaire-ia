# Studio Motion IA : des vidéos en motion design qui vendent ton offre, partout où tu publies

Extension du système **Monteur IA** (nom provisoire).

Tu vends une formation, un coaching, un logiciel, un template ? Tu tapes `/studio`. Ton monteur
te pose quelques questions à choix (une seule fois sur ce que tu vends, puis à chaque vidéo : le
but et où tu vas la mettre), et fabrique la vidéo.

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
section), LinkedIn, X, YouTube. Le format n'est qu'un réglage de sortie : la même vidéo se décline
d'un support à l'autre, remise en page, pas recadrée.

**Ce qui fait la différence**

1. **Une structure qui vend**, choisie selon le but : le problème avant le produit, une promesse
   claire, une démonstration, une preuve, un appel à l'action adapté au support.
2. **Un motion design qui montre** ton offre (ta page, ton logiciel, ton espace de formation, ton
   résultat) au lieu de la décorer.
3. **Rien d'inventé** : ton monteur lit ta page de vente et te montre ce qu'il a compris ; c'est
   tout ce que tes vidéos auront le droit d'affirmer.
4. **Chaque vidéo regardée avant toi** : planche de contrôle avec les zones de chaque plateforme,
   revue critique notée, son réglé au niveau de tes Reels, vérification de l'export.
5. **Prête à publier** : la vidéo, le texte de publication de chaque plateforme, la couverture ou
   l'affiche, la façon de la poser sur ta page, le calendrier d'un lancement.

Texte à l'écran et musique, ta voix enregistrée sur ton téléphone, ou une voix de synthèse
gratuite : tu choisis. Tes vidéos portent ta marque (couleurs, polices, mot-clé déjà réglés dans
ton Monteur IA). Chaque vidéo est un projet de l'app HyperFrames : tu la retouches en une phrase.

## Installation

Voir [INSTALL.md](INSTALL.md). Il faut Monteur IA installé ; tout tourne sur ton ordinateur, avec
ton abonnement Claude ou Codex habituel.

## Contenu

- `.claude/skills/studio/` : la méthode (questions à choix, fiche de l'offre, structures par but,
  idées, écriture, supports, voix, rythme, style, effets, son, revue, livraison).
- `tools/studio_motion.py` : création des vidéos par support et par format, vérification de la
  fiche, temps de lecture, zones, planche, son, couverture, export, livraison. Python 3.9+, sans
  dépendance.
- `templates/` : le point de départ de chaque vidéo et l'aiguillage ajouté à Monteur IA.
- `tests/` : `python3 -m unittest discover -s tests`.

Version : voir [VERSION](VERSION). Crédits : [CREDITS.md](CREDITS.md).
