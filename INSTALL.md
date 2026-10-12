# Installation de l'extension d'annonces

**Pour l'IA :** guide l'utilisateur dans sa langue (espagnol s'il te parle espagnol), y compris
les bilans. Garde les noms des fichiers et des commandes tels quels. Le client n'est pas
technique : une phrase simple par étape, pas de jargon.

C'est une **extension** de Monteur IA : elle s'installe **dans ton dossier Monteur IA** existant
et reprend ses réglages (couleurs, polices, mot-clé, sons). Pas de compte à créer, pas de clé,
pas d'abonnement : tout tourne sur ton ordinateur.

> ⚠️ **Prérequis : Monteur IA installé et fonctionnel.** Si ce n'est pas encore fait, installe
> d'abord Monteur IA (son INSTALL.md), puis reviens ici.

---

## 🚀 Le prompt d'installation

> **Le plus simple :** ouvre ton agent (Claude Code ou Codex, ou l'app HyperFrames) **dans ton
> dossier Monteur IA** et colle la phrase d'installation de ta formation. Il fait tout, en une à
> deux minutes.

Sinon, télécharge le ZIP de ce dépôt, dézippe-le où tu veux, ouvre ton agent **dans ton dossier
Monteur IA**, et colle exactement le bloc ci-dessous comme premier message (remplace le chemin de
la première ligne par l'endroit où tu as dézippé) :

```text
Tu es mon assistant d'installation pour l'extension d'annonces de mon Monteur IA.
Le dossier de l'extension dézippé est ici : ~/Downloads/lancement-ia-main
(Si tu viens de la phrase « Télécharge l'extension… », ignore cette ligne : le dossier est celui
que tu télécharges à l'étape 0.)
Installe l'extension étape par étape, sans jamais rien casser. Suis ces règles :

0. TÉLÉCHARGEMENT (seulement si tu n'as pas déjà le dossier de l'extension) : dans un dossier
   temporaire, hors du dossier Monteur IA, télécharge l'archive de l'adresse donnée dans ma
   phrase (bouton « Code » puis « Download ZIP » si tu ne peux pas la télécharger toi-même) et
   décompresse-la.

1. VÉRIFIE que le dossier courant est bien un dossier Monteur IA : `templates/AGENT.md.tpl`,
   `tools/` et `.claude/skills/` existent, et `brand.config.json` ou `brand.config.example.json`
   est présent. Si tu es dans « Accueil Monteur IA » (l'accueil de l'app HyperFrames), le dossier
   Monteur IA est le dossier parent : travaille depuis lui. Sinon, ARRÊTE-TOI et dis-moi d'ouvrir
   mon agent dans mon dossier Monteur IA.

2. COPIE dans le dossier Monteur IA, depuis le dossier de l'extension (étapes sans risque à
   refaire : un fichier identique ne se recopie pas, une version différente est remplacée) :
   a) le dossier `.claude/skills/annonce/` → dans `.claude/skills/` (s'il y est déjà, remplace
      le dossier entier par la nouvelle version) ;
   b) `tools/annonce.py` → dans `tools/` ;
   c) les fichiers de `templates/projet/` → dans `templates/annonce/` (crée-le) ;
   d) crée le dossier `annonces/` s'il n'existe pas, et ajoute la ligne `annonces/` au
      `.gitignore` du dossier Monteur IA si elle n'y est pas (rien d'autre ne change) ;
   e) AIGUILLAGE : si `templates/AGENT.md.tpl` ne contient PAS le marqueur
      « BEGIN EXTENSION: annonce », ajoute le contenu INTÉGRAL du fichier
      `templates/agent-extension-annonce.md` de l'extension À LA FIN de
      `templates/AGENT.md.tpl` (sans le modifier, lignes vides du début comprises). S'il contient
      déjà le marqueur, remplace tout le bloc, de la ligne `<!-- BEGIN EXTENSION: annonce …-->` à
      la ligne `<!-- END EXTENSION: annonce -->` incluses, par le contenu du fichier ; ne touche
      à rien d'autre.

3. Lance `npm run sync` à la racine du dossier Monteur IA (il régénère CLAUDE.md / AGENTS.md avec
   l'aiguillage et copie le skill pour Codex dans `.agents/skills/`). Si la commande échoue,
   copie simplement `.claude/skills/annonce/` dans `.agents/skills/` à la main. Ce que cette
   commande affiche concerne Monteur IA, pas l'extension : ne le recopie pas, dis juste que c'est
   fait.

4. SMOKE TEST : `python3 tools/annonce.py verifier` (Windows : `python …`). La dernière ligne doit
   être « ok ». Vérifie aussi que `CLAUDE.md` contient « annonces de lancement ».

RÈGLE POUR TOUTES LES ÉTAPES : ne passe jamais à l'étape suivante si l'étape en cours a échoué.
En cas d'échec : diagnostique en trois lignes (message d'erreur → cause probable → UNE action
corrective), puis retente.

5. PREMIÈRE INSTALLATION : affiche un TABLEAU récapitulatif ✅ / ❌ (dossier Monteur IA, skill,
   outil, gabarits, dossier annonces/ et .gitignore, aiguillage, sync, smoke test). Si tout est
   ✅, conclus par : « C'est installé. Le jour où tu lances quelque chose, tape /annonce avec le
   lien de ta page de vente, ta date et ton mot-clé. Tu peux aussi essayer tout de suite sur une
   offre que tu vends déjà. »
   MISE À JOUR (l'extension était déjà là) : pas de tableau. Une seule ligne : « L'extension
   d'annonces est à jour, tout est ✅. » Le tableau ne s'affiche que si une étape a échoué.
```

C'est tout. Laisse l'IA travailler et réponds-lui si elle te pose une question.

---

## Installation manuelle (si tu préfères)

1. Télécharge et dézippe ce dépôt.
2. Copie `.claude/skills/annonce/` dans le dossier `.claude/skills/` de ton Monteur IA.
3. Copie `tools/annonce.py` dans `tools/`, et le contenu de `templates/projet/` dans un nouveau
   dossier `templates/annonce/`.
4. Crée un dossier `annonces/` à la racine.
5. Ajoute le contenu de `templates/agent-extension-annonce.md` à la fin de `templates/AGENT.md.tpl`
   (une seule fois), puis lance `npm run sync`.
6. Lance `python3 tools/annonce.py verifier`.

## Problèmes courants

- **« je ne trouve pas le dossier Monteur IA »** : l'agent n'est pas ouvert dans ton dossier
  Monteur IA. Ouvre-le au bon endroit et recolle la phrase.
- **❌ HyperFrames** : l'installation de Monteur IA n'est pas allée au bout. Relance son prompt
  d'installation.
- **La capture de ta page échoue** (page protégée, page de paiement) : donne deux ou trois
  captures d'écran de ta page, ça suffit.
