

<!-- BEGIN EXTENSION: studio-motion (ajouté par l'installation de Studio Motion IA ; ne pas dupliquer) -->

## 🎬 Extension installée : Studio Motion IA (vidéos en motion design qui vendent)

Le client veut une vidéo qui présente ou vend son offre (pas un Reel face caméra) : il tape
`/studio`, ou demande « une vidéo pour ma page de vente », « une pub », « présente ma nouvelle
fonctionnalité », « annonce mon lancement », « un Reel en motion design pour mon offre », « una
vídeo de venta », ou colle le lien de sa page de vente en demandant une vidéo. Charge le skill
**`studio`** et suis-le (outil `{{MAISON}}tools/studio_motion.py`). Il pose d'abord ses questions
à choix (objectif, où la vidéo sera vue, voix), puis tout se fait par la fiche de l'offre
(`OFFRE.json`, seule source des faits affichés). Chaque vidéo vit dans
`{{MAISON}}studio-motion/<sujet> · <date>/`, **un projet de l'app HyperFrames par format**.
Depuis l'accueil de l'app, crée-la avec `python3 ../tools/studio_motion.py nouvelle "<sujet>"
--objectif … --videos … --ouvrir`, puis continue dans le premier projet. Rien n'est inventé
(prix, dates, témoignages, rareté) ; rien n'est publié par toi.

<!-- END EXTENSION: studio-motion -->
