#!/usr/bin/env node
/**
 * app-hyperframes.mjs : branche ce dossier sur l'app HyperFrames Studio.
 *
 *   node scripts/app-hyperframes.mjs etat               où en est le branchement (ne modifie rien)
 *   node scripts/app-hyperframes.mjs brancher           l'app lit désormais les instructions du projet
 *   node scripts/app-hyperframes.mjs ouvrir <dossier>   ouvre un projet (accueil ou vidéo) dans l'app
 *
 * Le chemin du script se donne depuis là où l'on est : depuis un projet de vidéo
 * (`videos/<vidéo>/<format>/`, qui a son propre package.json, donc pas de `npm run app`),
 * `node ../../../scripts/app-hyperframes.mjs ouvrir .` ; depuis l'accueil,
 * `node ../scripts/app-hyperframes.mjs ouvrir .`. Un chemin relatif se lit depuis le dossier où la
 * commande est tapée, y compris par `npm run app` (qui, lui, s'exécute toujours à la racine).
 *
 * Pourquoi « brancher » : l'app lance Claude Code sans charger le CLAUDE.md du projet ouvert
 * (`--setting-sources user`). La variable CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1, posée
 * dans la clé `env` de la config Claude Code de l'utilisateur, lui fait lire le CLAUDE.md du
 * dossier ouvert (l'app passe toujours ce dossier en `--add-dir`). Effet ailleurs : un dossier
 * ajouté à une session Claude Code fait lire son CLAUDE.md, rien d'autre. Rien d'autre n'est
 * modifié dans la config, et une sauvegarde est faite avant toute écriture.
 *
 * Codex n'a rien à brancher : il lit lui-même AGENTS.md et `.agents/skills/` du dossier ouvert.
 * Les consignes générées font quelques Kio, loin de sa limite de 32 Kio (sync.mjs prévient si le
 * modèle la dépassait un jour) : « brancher » ne touche jamais à la config de Codex.
 *
 * Node pur, zéro dépendance, cross-platform.
 */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const SCRIPT = fileURLToPath(import.meta.url);
const RACINE = path.resolve(path.dirname(SCRIPT), "..");

/** Le nom du produit et son code (nom du dépôt), lus dans produit.json. */
export function produit(racine = RACINE) {
  try {
    const p = JSON.parse(fs.readFileSync(path.join(racine, "produit.json"), "utf8"));
    return { nom: String(p.nom || "ce dossier"), code: String(p.code || "publicitaire-ia") };
  } catch {
    return { nom: "ce dossier", code: "publicitaire-ia" };
  }
}
const { nom: PRODUIT, code: CODE } = produit();

export const VARIABLE = "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD";
export const APP_ID = "dev.hyperframes.desktop";
export const DOWNLOAD_URL = "https://hyperframes.dev/studio";
// Un dossier est un projet pour l'app s'il a un index.html et l'un de ces fichiers.
const PROJECT_MARKERS = ["hyperframes.json", "meta.json", "project.json"];

/** Le dossier de config de Claude Code, résolu comme Claude Code et l'app le résolvent. */
export function claudeHome(env = process.env, home = os.homedir()) {
  return env.CLAUDE_CONFIG_DIR || path.join(home, ".claude");
}

export const settingsPath = (env, home) => path.join(claudeHome(env, home), "settings.json");

const isObject = (value) => value !== null && typeof value === "object" && !Array.isArray(value);

/** État du branchement, sans rien écrire. */
export function readBranchement(file) {
  if (!fs.existsSync(file)) return { file, exists: false, branche: false };
  let settings;
  try {
    settings = JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (error) {
    return { file, exists: true, branche: false, invalid: `JSON illisible (${error.message})` };
  }
  if (!isObject(settings)) return { file, exists: true, branche: false, invalid: "ce n'est pas un objet JSON" };
  if (settings.env !== undefined && !isObject(settings.env))
    return { file, exists: true, branche: false, invalid: "sa clé « env » n'est pas un objet" };
  return { file, exists: true, branche: settings.env?.[VARIABLE] === "1" };
}

const stamp = (date) => date.toISOString().replace(/[:.]/g, "-");

/** Pose la variable. Idempotent ; sauvegarde le fichier avant de l'écrire ; refuse un fichier
 *  qu'il ne sait pas lire plutôt que de l'écraser. */
export function brancher(file, now = new Date()) {
  const state = readBranchement(file);
  if (state.invalid)
    throw new Error(`${file} : ${state.invalid}. Rien n'a été modifié : corrige ce fichier, puis relance.`);
  if (state.branche) return { ...state, changed: false, backup: null };

  let settings = {};
  let backup = null;
  if (state.exists) {
    settings = JSON.parse(fs.readFileSync(file, "utf8"));
    backup = `${file}.avant-${CODE}-${stamp(now)}`;
    fs.copyFileSync(file, backup);
  } else {
    fs.mkdirSync(path.dirname(file), { recursive: true });
  }
  settings.env = { ...(settings.env ?? {}), [VARIABLE]: "1" };
  // Écriture atomique : Claude Code peut relire ce fichier à tout moment.
  const tmp = `${file}.tmp-${process.pid}`;
  fs.writeFileSync(tmp, `${JSON.stringify(settings, null, 2)}\n`);
  fs.renameSync(tmp, file);
  return { file, exists: true, branche: true, changed: true, backup };
}

// ---------------------------------------------------------------------------
// D'où la commande est tapée, et comment la retaper de là
// ---------------------------------------------------------------------------
/** Le dossier où la commande a été tapée. `npm run app` s'exécute toujours à la racine (npm remonte
 *  jusqu'au package.json, l'accueil n'en a pas) et garde le dossier d'appel dans INIT_CWD. */
export function dossierAppel(env = process.env, cwd = process.cwd()) {
  return env.npm_lifecycle_event === "app" && env.INIT_CWD ? env.INIT_CWD : cwd;
}

const entreGuillemets = (texte) => (/[\s"'`$&|;<>()]/.test(texte) ? `"${texte}"` : texte);

/** La commande à taper depuis `depuis` : chemin relatif du script dans le dossier, absolu ailleurs. */
export function commande(sous, depuis = dossierAppel()) {
  const versAppel = path.relative(RACINE, depuis);
  const dedans = !versAppel.startsWith("..") && !path.isAbsolute(versAppel);
  const script = dedans ? path.relative(depuis, SCRIPT) : SCRIPT;
  return `node ${entreGuillemets(script)} ${sous}`;
}

/** Chemin de l'app installée, ou null. Sur Linux, l'emplacement varie : on n'en cherche pas. */
export function findApp({ platform = process.platform, home = os.homedir(), exists = fs.existsSync } = {}) {
  if (platform !== "darwin") return null;
  return ["/Applications/HyperFrames.app", path.join(home, "Applications", "HyperFrames.app")].find(exists) ?? null;
}

/** Vrai si l'app reconnaît ce dossier comme un projet. */
export function isProject(dir) {
  if (!fs.existsSync(path.join(dir, "index.html"))) return false;
  return PROJECT_MARKERS.some((name) => fs.existsSync(path.join(dir, name)));
}

/** La CLI HyperFrames de ce dossier (0.8 et plus : elle sait ouvrir un projet dans l'app). */
export function localCli({ platform = process.platform, exists = fs.existsSync } = {}) {
  const bin = path.join(RACINE, "node_modules", ".bin", platform === "win32" ? "hyperframes.cmd" : "hyperframes");
  return exists(bin) ? bin : null;
}

/** Les projets de l'app rangés directement dans `dir` (les formats d'une vidéo, l'accueil). */
function sousProjets(dir) {
  try {
    return fs.readdirSync(dir, { withFileTypes: true })
      .filter((e) => e.isDirectory() && isProject(path.join(dir, e.name))).map((e) => e.name).sort();
  } catch {
    return [];
  }
}

/** Pourquoi `target` ne s'ouvre pas, et quoi taper à la place. */
export function pasUnProjet(target, depuis = dossierAppel()) {
  if (!fs.existsSync(target)) return `${target} introuvable. Vérifie le chemin (il se lit depuis ${depuis}).`;
  const projets = sousProjets(target);
  const exemple = () => commande(`ouvrir ${entreGuillemets(path.relative(depuis, path.join(target, projets[0])) || ".")}`, depuis);
  if (fs.existsSync(path.join(target, "produit.json")))
    return `${target} est le dossier ${PRODUIT} lui-même, pas un projet de l'app. Ouvre l'accueil` +
      (projets.length ? ` (${exemple()})` : "") + ", ou un projet de vidéo : videos/<vidéo>/<format>/.";
  if (projets.length)
    return `${target} est le dossier d'une vidéo : ouvre l'un de ses projets (${projets.join(", ")}), par exemple ${exemple()}.`;
  return `${target} n'est pas un projet HyperFrames : il lui faut un index.html et un meta.json. ` +
    "Depuis le dossier d'un projet de vidéo : node ../../../scripts/app-hyperframes.mjs ouvrir .";
}

/** Ouvre un projet dans l'app (Mac, Linux). Ailleurs, explique le geste à faire à la main.
 *  Un chemin relatif se lit depuis le dossier où la commande a été tapée. */
export function ouvrir(dir, {
  platform = process.platform, app = findApp({ platform }), cli = localCli({ platform }), run = execFileSync,
  depuis = dossierAppel(),
} = {}) {
  const target = path.resolve(depuis, dir);
  if (!isProject(target)) throw new Error(pasUnProjet(target, depuis));
  if (platform === "darwin" && app) {
    run("open", ["-b", APP_ID, target]);
    return { opened: true, target };
  }
  if (platform === "linux" && cli) {
    run(cli, ["open", target]);
    return { opened: true, target };
  }
  const how =
    platform === "win32"
      ? "L'app HyperFrames n'existe pas encore sous Windows : continue dans Claude Code ou Codex."
      : `Dans l'app HyperFrames, menu Fichier > Ouvrir un dossier, puis choisis ${target}.` +
        (platform === "darwin" ? ` (App introuvable : télécharge-la sur ${DOWNLOAD_URL}.)` : "");
  return { opened: false, target, how };
}

function describe(env = process.env) {
  const state = readBranchement(settingsPath(env));
  const app = findApp();
  const lines = [];
  if (state.invalid) lines.push(`Config Claude Code : ${state.invalid} (${state.file}).`);
  else if (state.branche) lines.push(`Config Claude Code : l'app lit les instructions de ${PRODUIT}.`);
  else lines.push(`Config Claude Code : à brancher (${commande("brancher")}).`);
  lines.push("Codex : rien à brancher, il lit lui-même AGENTS.md et .agents/skills/ du dossier ouvert.");
  if (process.platform === "win32") lines.push("App HyperFrames : pas encore disponible sous Windows.");
  else if (process.platform !== "darwin") lines.push("App HyperFrames : à ouvrir depuis le menu de ton système (Linux).");
  else lines.push(app ? `App HyperFrames : installée (${app}).` : `App HyperFrames : pas installée (${DOWNLOAD_URL}).`);
  return { state, app, text: lines.join("\n") };
}

function main(argv) {
  const [command, arg] = argv;
  if (command === "etat") {
    const { state, app, text } = describe();
    console.log(argv.includes("--json") ? JSON.stringify({ ...state, app }, null, 2) : text);
    return 0;
  }
  if (command === "brancher") {
    // Seule la config de Claude Code change : Codex lit déjà AGENTS.md et les skills du dossier.
    try {
      const result = brancher(settingsPath());
      if (!result.changed) console.log(`Déjà branché : l'app lit les instructions de ${PRODUIT}.`);
      else {
        console.log(`Branché : l'app HyperFrames lira les instructions de ${PRODUIT}.`);
        if (result.backup) console.log(`Sauvegarde de l'ancienne config : ${result.backup}`);
        console.log("Effet à la prochaine conversation ouverte dans l'app.");
      }
      return 0;
    } catch (error) {
      console.error(`❌ Claude Code : ${error.message}`);
      return 1;
    }
  }
  if (command === "ouvrir") {
    // Sans dossier : celui où la commande est tapée (le projet de vidéo où l'on se trouve).
    const result = ouvrir(arg ?? ".");
    console.log(result.opened ? `Ouvert dans l'app : ${result.target}` : result.how);
    return 0;
  }
  console.error(`Usage : ${commande("etat [--json] | brancher | ouvrir <dossier>")}\n` +
    "Depuis un projet de vidéo : node ../../../scripts/app-hyperframes.mjs ouvrir .");
  return 2;
}

// Lancé directement (pas importé par un test) : Node donne au module son chemin réel, liens résolus
// (dossier temporaire du Mac sous /var, dossier rangé derrière un lien) ; argv[1] garde le chemin tapé.
if (process.argv[1] && fs.realpathSync(path.resolve(process.argv[1])) === fileURLToPath(import.meta.url)) {
  try {
    process.exitCode = main(process.argv.slice(2));
  } catch (error) {
    console.error(`❌ ${error.message}`);
    process.exitCode = 1;
  }
}
