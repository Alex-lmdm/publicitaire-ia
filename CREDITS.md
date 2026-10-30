# Crédits et licences

Publicitaire IA, par LeMondeDuMarketing. Le dossier s'appuie sur des outils, des polices, des sons et des idées
open source : merci à leurs auteurs. Chaque élément livré a été vérifié à la source avant d'être
redistribué (13 octobre 2026).

## Installés par npm, jamais copiés dans ce dépôt

- **HyperFrames** 0.8.136 (Apache-2.0), HeyGen : compositions HTML rendues en vidéo, capture de
  site, contrôles, rendu. https://github.com/heygen-com/hyperframes
- **GSAP** 3.14.2 (licence « Standard No Charge » de GreenSock) : animation. Installé depuis npm,
  copié sur l'ordinateur du client par `npm run sync` (assets/vendor/, non versionné).
  https://gsap.com/standard-license

HyperFrames envoie par défaut des statistiques d'usage anonymes et vérifie ses mises à jour en
ligne (dossier `~/.hyperframes/`). Pour les couper : `npx hyperframes telemetry disable`.

## Outils de l'ordinateur, non livrés

- **FFmpeg** (LGPL/GPL) : planches, mesure du rythme et du son, couverture, export.
- **Node.js** et **Python** : le moteur et les outils.

## Livrés dans ce dossier

| Quoi | Où | Licence | Source |
|---|---|---|---|
| Skills `hyperframes-core`, `hyperframes-animation`, `hyperframes-cli` | `.claude/skills/hyperframes-*` (texte de licence dans chacun) | Apache-2.0, © HeyGen ; copies non modifiées de la version 0.8.136 (commit 4c4b857) | https://github.com/heygen-com/hyperframes |
| Police **Inter** (400, 400 italique, 600, 700, 900) | `assets/fonts/` + `OFL-Inter.txt` | SIL OFL 1.1, © The Inter Project Authors | https://github.com/rsms/inter |
| Police **Anton** (400) | `assets/fonts/` + `OFL-Anton.txt` | SIL OFL 1.1, © The Anton Project Authors | https://github.com/googlefonts/AntonFont |
| 14 sons Freesound | `assets/sfx/starter/` | CC0 1.0 (domaine public), vérifiée sur chaque page | numéros dans `assets/sfx/starter/sounds.md` |
| 8 sons Kenney « Interface Sounds » | `assets/sfx/starter/` | CC0 | https://kenney.nl/assets/interface-sounds |
| Icônes **Lucide** | `templates/kit/icones.js` + `LICENSE-lucide.txt` | ISC, © Lucide Icons and Contributors | https://lucide.dev |
| Module de pose des sons | `tools/sons.py` | repris de Monteur IA (LeMondeDuMarketing) | |

Aucun son du **Pack SFX** (produit vendu à part) n'est livré ici. Le client l'installe sur son
ordinateur depuis son archive `pack-sfx.zip`, ou le reprend de son dossier Monteur IA
(`studio_motion.py pack-sfx`) ; ces fichiers sont exclus du dépôt (`.gitignore`).

## Récupérés à la demande, jamais livrés

- **Polices de la marque du client** : de préférence la version libre de **Google Fonts** (SIL
  OFL ou Apache), téléchargée sur son ordinateur ; à défaut, les fichiers de sa propre page (son
  usage relève de sa licence, l'outil le lui signale) ou de son dossier Monteur IA.
- **theSVG** (MIT), puis **simple-icons** (CC0) en secours : les logos des outils que l'offre du
  client utilise (`studio_motion.py logos`), posés dans son seul projet. Chaque logo reste la marque
  de son propriétaire et ne sert qu'à désigner l'outil réellement utilisé. https://thesvg.org,
  https://simpleicons.org
- **Musiques de lancement** : 17 musiques générées par LeMondeDuMarketing avec Suno (abonnement
  Pro), livrées aux acheteurs avec la formation, jamais dans ce dépôt ; leur licence est dans
  `assets/musiques/LICENCE.md` une fois installées (usage dans toutes les vidéos, publicités
  comprises ; pas de redistribution des fichiers seuls).
- **Musiques de Mixkit** : 18 liens vers mixkit.co (licence Mixkit Stock Music Free : pub permise,
  sans crédit), dans `references/son.md` du skill `studio`. Aucun fichier n'est fourni ici : le
  client télécharge lui-même celle qu'il veut. https://mixkit.co/license/
- **Bibliothèque de musiques, bruitages et voix de HeyGen** : cherchés et pris avec le compte du
  client (`studio_motion.py heygen`), par l'API de HeyGen, pour ses seules vidéos, aux conditions de
  HeyGen ; la source de chaque morceau est notée dans `assets/audio/SOURCE.md` du projet.
  https://www.heygen.com

## Projets dont on s'est inspiré

Aucun code n'en est copié tel quel ; les règles ci-dessous ont été traduites, comparées entre
elles (la plus stricte a été retenue) et adaptées au format vertical d'Instagram.

- **brag**, © 2026 Shunit Haviv Hakimi, licence MIT : le parcours à portes de contrôle, l'ancrage
  des affirmations dans le projet, les données sensibles remplacées par des exemples, le temps de
  lecture minimum, le mixage, la couverture posée en première image.
  https://github.com/latent-spaces/brag
- **product-launch-motion**, AbubakrChan, licence MIT : la liste blanche des faits, l'arrondi vers
  le bas, la grammaire des entrées, la planche par repères, le mastering mesuré.
  https://github.com/AbubakrChan/product-launch-motion
- **motion-graphics-skills**, charlie947, licence MIT : zones de sécurité verticales, tailles de
  texte, interdits, contrôle de l'export. https://github.com/charlie947/motion-graphics-skills
- **claude-motion-design**, howseen-ai, licence MIT : le temps fort trouvé par l'énergie, la revue
  notée par un juge distinct, le test du résumé à partir des seules images.
  https://github.com/howseen-ai/claude-motion-design
- **claude-motion**, whaleyxbt, licence MIT : la planche de contrôle obligatoire, une montée et un
  impact par vidéo. https://github.com/whaleyxbt/claude-motion
- **animate**, cth9191, licence MIT : silence avant le temps fort, défauts interdits.
  https://github.com/cth9191/animate
- **motion-design-skill**, LottieFiles, licence MIT : durées selon la distance et l'émotion.
  https://github.com/LottieFiles/motion-design-skill
- Galeries **prompt-motion.com** et **motionpromptgallery.com** : les familles d'effets qui
  marchent (aucun prompt n'est repris).
- Leo (@leomeethewoo), « Make your product videos look expensive (Apple Framework) » : la couleur
  sur le produit (sa règle du vide a été abandonnée en 0.4 : elle donnait des slides).
- **Taap.it V2**, vidéo de lancement de Kylian Khalifa : la référence de niveau, mesurée image par
  image (un événement toutes les demi-secondes, peu de texte, chapitres à interrupteur, fonds qui
  alternent, mosaïque finale qui devient le bouton). Aucun contenu n'en est repris.
- Repères publics des plateformes (zones de sécurité Meta, TikTok, YouTube ; durées LinkedIn et X)
  et étude Motion « Creative Benchmarks 2026 » sur 578 750 publicités Meta (le motion design
  décoratif gagne moins que la démonstration, le texte lisible et l'offre claire).
