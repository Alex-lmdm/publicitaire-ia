# Connecter son compte Epidemic Sound

Option demandée par le client, jamais une condition pour fabriquer sa vidéo. Le MCP relie son
compte à son assistant : recherche, écoute et téléchargement de musiques et de bruitages. Le
client garde le choix et sa propre licence. Aucun achat ni abonnement ne se fait à sa place.

Avant de configurer, relis la [documentation officielle Epidemic](https://developers.epidemicsound.com/docs/mcp/).
Pour Codex, relis aussi la [documentation officielle MCP](https://developers.openai.com/codex/mcp/).
Les commandes ci-dessous servent à préparer la connexion ; ne les présente pas comme déjà exécutées.

## Sa clé, saisie sur son ordinateur

Dans Epidemic : **Account → API keys → MCP Server API key**. Ce n'est pas la clé de l'API
partenaire. Le client la crée lui-même. Ne lui demande jamais de la coller dans la conversation,
ne la lis pas et ne l'affiche pas. Prépare la configuration, puis guide-le vers une saisie locale
masquée dans son terminal ou un gestionnaire de secrets. Aucun secret dans Publicitaire IA,
ses projets, `marque.json` ou un dépôt Git.

La variable `EPIDEMIC_SOUND_MCP_API_KEY` doit être disponible dans le processus qui lance
l'assistant. Vérifie seulement sa présence et sa longueur, jamais sa valeur. Ne copie pas la clé
en clair dans une commande qui restera dans l'historique.

Pièges rencontrés le 07/11/2026 (Claude Code, app de bureau sur Mac) :
- Une saisie masquée (`read -s`) lancée depuis la conversation ne reçoit rien : ouvre-la dans un
  vrai onglet de terminal (un petit script qui lit la clé et l'ajoute à `~/.zshrc`).
- L'app ouverte depuis le Dock ne lit pas `~/.zshrc` : le serveur répond 401 alors que la clé est
  bonne. Pour trancher, teste la clé depuis le terminal (une requête `initialize` au serveur avec
  l'en-tête `Authorization`) : 200 veut dire que la clé est bonne et que l'app ne la voit pas. Le
  remède : la recopier, sans l'afficher, dans `env` de `~/.claude/settings.json` (sauvegarde
  d'abord), puis le client quitte l'app (Cmd+Q) et la rouvre.

## Claude Code

Ajoute le serveur à la configuration personnelle, sans remplacer les autres serveurs :

```sh
claude mcp add -s user --transport http epidemic-sound https://www.epidemicsound.com/a/mcp-service/mcp --header 'Authorization: Bearer ${EPIDEMIC_SOUND_MCP_API_KEY}'
claude mcp list
```

Garde la référence littérale à la variable. Adapte la commande au shell du client, puis rouvre
la conversation si nécessaire. Vérifie la connexion par une recherche de musique.

## Codex

Dans sa configuration personnelle `~/.codex/config.toml` (ou son emplacement personnel
effectif), ajoute seulement cette entrée, sans écraser une entrée existante ni les autres :

```toml
[mcp_servers.epidemic_sound]
url = "https://www.epidemicsound.com/a/mcp-service/mcp"
bearer_token_env_var = "EPIDEMIC_SOUND_MCP_API_KEY"
```

La valeur est un **nom de variable**, jamais la clé. Vérifie avec `codex mcp list`, puis une
recherche depuis une nouvelle conversation. Ne suppose pas que l'OAuth d'un autre assistant
fonctionne dans Codex : Epidemic réserve ses redirections à certains clients.

## Vérifier puis utiliser

Commence par une recherche et un extrait : aucun téléchargement ni génération pour ce test.
La documentation indique que le compte gratuit peut chercher et écouter ; télécharger demande
un abonnement admissible actif. Une connexion réussie ne démontre pas que sa licence couvre
la publicité ou les vidéos de ses clients. En cas d'échec, montre une explication sans secret ;
le client peut toujours télécharger lui-même le morceau sur le site et fournir le fichier.

Ensuite : `son.md`, « Son compte Epidemic Sound » et « Construire l'image sur la bande-son ».
