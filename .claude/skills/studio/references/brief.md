# Les questions à choix : le profil, puis le brief

Le client n'est pas technique et ne sait pas toujours ce qu'il veut. Des choix numérotés lui
évitent la page blanche : il répond « 1, b, A » en trois secondes, ou décrit autre chose. Pose
toujours toutes les questions d'une étape **dans un seul message**, avec une valeur par défaut
recommandée, et saute celles dont tu connais déjà la réponse.

## Au premier usage : la marque et le profil (une seule fois)

Si `marque.json` ou `studio.config.json` n'existe pas à la racine du dossier, commence par là, en
un seul message (saute la question dont tu connais déjà la réponse) :

> Bienvenue dans Publicitaire IA 🎬 Trois questions, une seule fois, pour que tes vidéos portent ta marque et partent
> toujours de ton offre :
>
> **1. Ta marque (couleurs, polices, logo) : je la prends où ?**
> a) sur ta page de vente : colle son lien (le plus simple) ·
> b) sur des images ou des captures de ta marque : glisse-les ici ·
> c) sur une vidéo dont tu aimes le style : son lien, ou le fichier ·
> d) j'ai Monteur IA : je reprends ses réglages
>
> **2. Qu'est-ce que tu vends surtout ?** (plusieurs choix possibles)
> a) une formation · b) un coaching ou un accompagnement · c) un logiciel ou une app ·
> d) un template, un guide, un ebook · e) une communauté · f) autre chose (dis-moi)
>
> **3. Pour tes vidéos, tu préfères :**
> A) du texte à l'écran et de la musique (le plus simple) ·
> B) ta voix, enregistrée sur ton téléphone ·
> C) une voix de synthèse, gratuite, générée sur ton ordinateur
>
> Réponds par exemple « a monsite.fr/formation, a, A ».

La réponse 1 se traite avec [marque.md](marque.md) : l'outil lit la source, puis tu lui montres
sa marque et tu attends son accord. Enregistre le reste dans `studio.config.json` :
`{"vend": [...], "page": "...", "voix": "texte|ma-voix|voix-ia", "dm": null,
"reference_style": null, "supports_habituels": [], "preferences": []}` (`page` vient de la
réponse 1 a, sinon du premier brief). Les préférences dites plus tard (« toujours sans musique »,
« mes vidéos en noir ») s'y ajoutent et se relisent à chaque vidéo.

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

- objectif **d** (lancement) : les dates d'ouverture et de fermeture, et les vidéos voulues ;
- objectif **e** (inscription) : la date du live s'il y en a un ;
- objectif **c** (fonctionnalité) : laquelle, et ce qu'elle évite au client ;
- support **D** (pub) : « je te prépare 3 accroches différentes sur le même corps, pour tester ? »
  (oui par défaut) ;
- la voix, si le profil ne la donne pas ou si le support la change (une boucle de page est muette).

Recommande toujours une combinaison, avec sa raison en une phrase. Si le client répond « je
sais pas » ou « choisis », prends ta recommandation et avance.

## Traduire les réponses en commande

| Réponse | `--objectif` | `--videos` |
|---|---|---|
| a (vendre) + A + E | `vente` | `reel,page` |
| b (nouveauté) + A + B | `nouveaute` | `reel,story` |
| c (fonctionnalité) + F | `fonctionnalite` | `section` |
| d (lancement) | `lancement` | `reel,story:teaser,story:ouverture,story:dernier-jour` (+ `story:relance` si demandé) |
| e (inscription) + A + B | `inscription` | `reel,story` |
| f (explication) + E | `explication` | `page` |
| g (preuve) + A | `preuve` | `reel` |
| support D (pub) | | `pub` (plein écran) et souvent `fil` (4:5) |
| support G (LinkedIn) | | `linkedin` (4:5) |

Un format différent du format habituel du support se demande avec `@` : `page@1x1` (page de
vente sur téléphone), `x@1x1`. `python3 tools/studio_motion.py supports` liste tout (depuis la
racine du dossier).
