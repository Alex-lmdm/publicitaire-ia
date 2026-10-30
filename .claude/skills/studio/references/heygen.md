# HeyGen : les voix de synthèse (et sa bibliothèque de musiques, sur demande)

HeyGen (heygen.com, l'éditeur de HyperFrames) sert ici aux **voix de synthèse**, quand le client
en demande une ([voix.md](voix.md)). La musique des vidéos vient de ses **musiques de lancement**,
offertes avec la formation ([son.md](son.md)). La bibliothèque de musiques de HeyGen (plus de
10 000 morceaux) ne se propose plus : avec un compte gratuit, ses conditions interdisent l'usage
commercial et publicitaire, et aucune licence claire n'est publiée pour les comptes payants. S'il
la demande lui-même, dis-le-lui une fois avant de chercher.

| Ce qu'on fait avec HeyGen | Prix |
|---|---|
| Chercher, écouter et prendre une musique | gratuit (le solde ne bouge pas) |
| Écouter les voix de synthèse | gratuit |
| Générer une voix off de synthèse | payant, prélevé sur son solde HeyGen : environ 0,12 $ la minute ; le compte gratuit n'a pas de solde, il se recharge de quelques dollars |

Tout passe par `python3 tools/studio_motion.py heygen …` (`connecter` et l'état depuis la racine ;
`musiques`, `bruitages`, `prendre`, `voix` et `parler` depuis le projet d'une vidéo, avec
`../../../tools/studio_motion.py`), sur Mac comme sous Windows, dans Claude Code, Codex et l'app
HyperFrames : la même méthode partout.

## Relier son compte (une fois, trois minutes)

`heygen` (sans rien d'autre) dit s'il est déjà relié. Ne le propose que lorsqu'il demande une voix
de synthèse (ou, lui-même, la bibliothèque de musiques de HeyGen). Le guide, à lui envoyer tel
quel :

> Pour ta voix de synthèse, il faut relier un compte HeyGen. Trois minutes, une seule fois :
>
> 1. Crée ton compte gratuit sur https://app.heygen.com/signup (avec Google, c'est le plus
>    rapide). Si HeyGen te propose un abonnement, passe : le compte gratuit suffit.
> 2. Ouvre https://app.heygen.com/settings?nav=API et copie ta clé (« API token »). HeyGen ne la
>    remontre pas : si tu l'as perdue, il en crée une nouvelle.
> 3. Colle-la ici.
>
> Elle reste sur ton ordinateur. Rien n'est jamais payé sans ton accord.

Quand il colle la clé :

```bash
python3 tools/studio_motion.py heygen connecter <la clé>
```

« ✅ HeyGen relié » : dis-lui simplement que c'est fait. **Ne répète jamais la clé** dans tes
messages et ne l'écris dans aucun fichier du dossier : l'outil la range dans
`~/.heygen/credentials` (le fichier du logiciel heygen, réservé à sa session).

## Les messages de l'outil

- **« une autre connexion HeyGen existe déjà »** : il a déjà un compte relié (un autre outil, un
  autre compte). Demande-lui s'il veut le remplacer par celui-ci, puis `--remplacer`.
- **« HeyGen refuse la clé »** : elle a été mal copiée ou régénérée. Fais-lui recopier la clé.
- **« relié par le CLI heygen (connexion du navigateur) »** : il s'est connecté autrement ;
  fais-lui copier une clé (étape 2) et `heygen connecter <clé> --remplacer`.
- **« solde HeyGen insuffisant »** (voix seulement) : une voix de synthèse coûte quelques
  centimes, prélevés sur un solde à recharger soi-même. Propose-lui de recharger 5 $ (une quarantaine
  de minutes de voix) sur https://app.heygen.com/settings?nav=API, la page de sa clé, rubrique des
  crédits d'API ; ou d'enregistrer sa voix au téléphone, gratuitement (`voix.md`).
- **« HeyGen injoignable »** : pas de connexion internet ; réessaie plus tard, sans bloquer le
  reste de la vidéo.

## Les droits

Ce qui vient de HeyGen se prend avec le compte du client, pour ses vidéos, aux conditions de
HeyGen (compte gratuit : pas d'usage commercial ni publicitaire). Note toujours la source (l'outil
le fait dans `assets/audio/SOURCE.md`). Ne l'envoie à personne et ne le range jamais ailleurs que
dans le projet de la vidéo.
