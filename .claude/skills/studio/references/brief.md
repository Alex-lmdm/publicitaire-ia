# Les questions à choix : la marque, puis le brief

Le client n'est pas technique et ne sait pas toujours ce qu'il veut. Des choix numérotés lui
évitent la page blanche : il répond « 1, b, A » en trois secondes, ou décrit autre chose. Pose
toujours toutes les questions d'une étape **dans un seul message**, avec une valeur par défaut
recommandée, et saute celles dont tu connais déjà la réponse.

## Au premier usage : sa marque (une seule question, une seule fois)

Si `marque.json` ou `studio.config.json` n'existe pas à la racine du dossier, commence par là :

> Bienvenue dans Publicitaire IA 🎬 Une seule question, une seule fois, pour que tes vidéos portent ta
> marque :
>
> **Ta marque (couleurs, polices, logo) : je la prends où ?**
> a) sur ta page de vente : colle son lien (le plus simple) ·
> b) sur des images ou des captures de ta marque : glisse-les ici ·
> c) sur une vidéo dont tu aimes le style : son lien, ou le fichier ·
> d) j'ai Monteur IA : je reprends ses réglages
>
> Réponds par exemple « a monsite.fr/formation ».

Ne demande pas ce qu'il vend : sa page le dit, et le brief de chaque vidéo demande ce qu'on présente.

La réponse se traite avec [marque.md](marque.md) : l'outil lit la source, puis tu lui montres sa
marque et tu attends son accord. Écris ensuite `studio.config.json` : `{"page": "...", "voix":
"texte", "dm": null, "reference_style": null, "supports_habituels": [], "preferences": []}` (`page`
vient de la réponse a, sinon du premier brief ; `voix` reste `texte` tant qu'il ne demande pas de
voix off, puis `voix-ia` (Google AI Studio, avec `voix_ia` pour le nom de sa voix), `ma-voix` ou
`voix-heygen` (avec `voix_heygen` pour l'id de sa voix)). Les préférences dites plus tard (« toujours
sans musique », « choisis toujours la musique pour moi », « mes vidéos en noir ») s'y ajoutent et se
relisent à chaque vidéo.

**Ses musiques.** `python3 tools/studio_motion.py musiques` dit si les 35 musiques de lancement sont
installées (le cas normal : l'installation les a mises). S'il en manque, ne pose pas de question :
termine ton message de bienvenue par une ligne, « Tes musiques de lancement ne sont pas toutes
installées : colle quand tu veux la phrase « Installe mes musiques de lancement » du module Musique
de ta formation. » Sa phrase collée : `python3 tools/studio_motion.py musiques installer --lien "<le
lien de sa phrase>"` ([son.md](son.md), « Les musiques de lancement »). Sa propre musique pour toutes
ses vidéos (un fichier qu'il glisse) : `python3 tools/studio_motion.py marque regler --musique
"<fichier>"`.

## À chaque vidéo : le brief

Reprends ce que le client a déjà dit. Pour le reste, un seul message :

> On fait quoi aujourd'hui ?
>
> **1. Le but de la vidéo**
> a) vendre mon offre (donner envie d'acheter) ·
> b) annoncer une nouveauté (un module, une fonction, un bonus) ·
> c) montrer une fonctionnalité précise ·
> d) mon lancement (teaser, ouverture, relance, dernier jour) ·
> e) faire s'inscrire (guide gratuit, liste d'attente, live) ·
> f) expliquer comment ça marche ·
> g) mettre en valeur un témoignage ou un résultat
>
> **2. Où tu vas la mettre** (plusieurs choix possibles, chacun aura son format)
> A) Reel · B) story · C) TikTok ou Shorts · D) publicité · E) page de vente (en haut) ·
> F) section de ma page (boucle muette) · G) LinkedIn · H) X · I) YouTube
>
> **3. Ce qu'on présente** : le lien de la page (ou ta page habituelle), ou deux phrases et
> quelques captures.
>
> Ma recommandation pour toi : **a + A + E**, le Reel et la vidéo de ta page de vente racontent
> la même chose en deux longueurs. Réponds par exemple « a, A E, monsite.fr/offre ».

Ajoute une question seulement si elle change la vidéo :

- objectif **d** (lancement) : les dates d'ouverture et de fermeture, les vidéos voulues, et s'il a
  déjà fait des jours de prélancement qui ont posé le problème et ses preuves (sans réponse : non,
  l'audience est froide et chaque vidéo présente l'offre de zéro, [structures.md](structures.md)) ;
- objectif **e** (inscription) : la date du live s'il y en a un ;
- objectif **c** (fonctionnalité) : laquelle, et ce qu'elle évite au client ;
- support **D** (pub) : « je te prépare 3 accroches différentes sur le même corps, pour tester ? »
  (oui par défaut) ;
- aucune question sur la voix : texte et musique par défaut ; une voix off se fait à sa demande
  ([voix.md](voix.md)).

Recommande toujours une combinaison, avec sa raison en une phrase. Si le client répond « je
sais pas » ou « choisis », prends ta recommandation et avance.

## Traduire les réponses en commande

| Réponse | `--objectif` | `--videos` |
|---|---|---|
| a (vendre) + A + E | `vente` | `reel,page` |
| b (nouveauté) + A + B | `nouveaute` | `reel,story` |
| c (fonctionnalité) + F | `fonctionnalite` | `section` |
| d (lancement) | `lancement` | `reel,story:teaser,story:ouverture`, `story:dernier-jour` seulement si sa page donne la date de fermeture (sinon `offre` la refuse), `story:relance` s'il la demande |
| e (inscription) + A + B | `inscription` | `reel,story` |
| f (explication) + E | `explication` | `page` |
| g (preuve) + A | `preuve` | `reel` |
| support D (pub) | | `pub` (plein écran) et souvent `fil` (4:5) |
| support G (LinkedIn) | | `linkedin` (4:5) |

Un format différent du format habituel du support se demande avec `@` : `page@1x1` (page de
vente sur téléphone), `x@1x1`. `python3 tools/studio_motion.py supports` liste tout (depuis la
racine du dossier).
