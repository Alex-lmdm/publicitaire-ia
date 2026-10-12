# Annonces de lancement : le Reel et les stories de ton lancement, faits par ton Monteur IA

Extension du système **Monteur IA**. Nom provisoire : **Lancement IA**.

Tu lances une formation, un nouveau module, une offre ? Tu tapes `/annonce` et tu donnes le lien
de ta page de vente. Ton monteur :

1. **Lit ta page** et te montre ce qu'il a compris : la promesse, ce qu'on reçoit, le prix, les
   bonus, les dates, les preuves. Tu corriges. C'est tout ce que tes vidéos auront le droit
   d'affirmer : rien n'est inventé.
2. **Te propose trois idées d'annonce**, vraiment différentes, et te dit laquelle il conseille.
   Tu réponds 1, 2 ou 3.
3. **Fabrique tes vidéos en vertical** : le Reel d'annonce (20 secondes, musique et bruitages
   calés, « commente MOT » à la fin) et les stories du lancement (teaser la veille, ouverture le
   jour J, dernier jour), avec une place libre pour ton sticker lien.
4. **Les regarde avant toi** : chaque vidéo passe une planche de contrôle (zones de sécurité
   d'Instagram, temps de lecture, dernière image), une revue critique notée, le réglage du son et
   la vérification de l'export.
5. **Te livre** les MP4, la légende prête à coller, la couverture, une version sans musique pour
   un son Instagram, et le calendrier de publication.

Une nouveauté plus petite (un module, une fonction, un bonus) : « annonce ma nouveauté », et tu
reçois un Reel et une story.

Tes annonces portent **ta marque** (couleurs, polices, mot-clé déjà réglés dans ton Monteur IA).
Chaque vidéo est un projet de l'app HyperFrames : tu la retouches comme un Reel, en une phrase
(« laisse le prix affiché plus longtemps »).

## Installation

Voir [INSTALL.md](INSTALL.md). Il faut Monteur IA installé ; tout tourne sur ton ordinateur, avec
ton abonnement Claude ou Codex habituel.

## Contenu

- `.claude/skills/annonce/` : la méthode (fiche de l'offre, angles, formats, rythme, style,
  effets, son, revue, livraison).
- `tools/annonce.py` : création des annonces, vérification de la fiche, zones, temps de
  lecture, planche, son, couverture, export, livraison. Python 3.9+, sans dépendance.
- `templates/` : le point de départ de chaque vidéo et l'aiguillage ajouté à Monteur IA.
- `tests/` : `python3 -m unittest discover -s tests`.

Version : voir [VERSION](VERSION). Crédits : [CREDITS.md](CREDITS.md).
