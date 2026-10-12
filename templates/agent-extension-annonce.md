

<!-- BEGIN EXTENSION: annonce (ajouté par l'installation de l'extension d'annonces ; ne pas dupliquer) -->

## 📣 Extension installée : annonces de lancement

Le client lance quelque chose ou sort une nouveauté, et veut ses annonces : il tape `/annonce`,
dit « annonce mon lancement », « fais le Reel de lancement », « les stories de mon lancement »,
« annonce ma nouveauté », « anuncia mi lanzamiento », ou colle le lien de sa page de vente en
demandant des vidéos. Charge le skill **`annonce`** et suis-le (outil
`{{MAISON}}tools/annonce.py`). Ce n'est pas un Reel face caméra : pas de dérush, pas de pipeline
Reel. Chaque annonce vit dans `{{MAISON}}annonces/<sujet> · <date>/`, avec sa fiche d'offre
(`OFFRE.json`, seule source des faits affichés) et **un projet de l'app HyperFrames par vidéo**.
Depuis l'accueil de l'app, crée l'annonce avec `python3 ../tools/annonce.py nouvelle "<sujet>"
--videos … --ouvrir`, puis continue dans le projet du Reel. Rien n'est inventé (prix, dates,
témoignages, rareté) ; rien n'est publié par toi.

<!-- END EXTENSION: annonce -->
