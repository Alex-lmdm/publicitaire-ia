#!/usr/bin/env node
/**
 * sync.mjs : régénère ce qui se déduit du dépôt, sur la machine du client.
 *
 *   1. GSAP, installé par npm, copié dans assets/vendor/ (jamais redistribué dans le dépôt) ;
 *   2. le style de la marque (brand/) et l'accueil de l'app HyperFrames, par l'outil Python
 *      (`studio_motion.py style`, seul propriétaire de la marque) ;
 *   3. CLAUDE.md et AGENTS.md, à la racine et dans l'accueil, depuis templates/AGENT.md.tpl ;
 *   4. la copie des skills pour Codex (.claude/skills/ -> .agents/skills/).
 *
 * Lancé par `npm install` / `npm ci` (postinstall) et par `npm run sync`. Ne touche jamais aux
 * vidéos du client ni à sa marque. Node pur, zéro dépendance, cross-platform.
 *
 * Chaque étape est tentée même si une autre échoue. Le postinstall (`… || exit 0`) ne fait jamais
 * échouer `npm ci` : un échec se lit donc dans la sortie, en dernière ligne, « sync incomplet :
 * relance `npm run sync` », et `npm run sync` lancé seul sort alors en erreur (code 1).
 */

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const rel = (p) => path.relative(ROOT, p) || ".";
const log = (msg) => console.log(msg);
const warn = (msg) => console.warn(`⚠️  ${msg}`);
const RELANCE = "relance `npm run sync`";

// Codex lit AGENTS.md jusqu'à 32 Kio par défaut et tronque la suite sans prévenir.
const LIMITE_CODEX = 32 * 1024;

export function lireProduit(racine = ROOT) {
  const p = JSON.parse(fs.readFileSync(path.join(racine, "produit.json"), "utf8"));
  const version = fs.existsSync(path.join(racine, "VERSION"))
    ? fs.readFileSync(path.join(racine, "VERSION"), "utf8").trim() : "";
  return { nom: String(p.nom), code: String(p.code), editeur: String(p.editeur ?? ""), version };
}

/** Écrit seulement si le contenu change : l'app HyperFrames signale toute écriture dans un projet
 *  ouvert (l'accueil en est un). */
export function ecrireSiDifferent(file, contenu) {
  if (fs.existsSync(file) && fs.readFileSync(file, "utf8") === contenu) return false;
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, contenu);
  return true;
}

// ---------------------------------------------------------------------------
// 1. GSAP
// ---------------------------------------------------------------------------
const GSAP = ["gsap.min.js", "CustomEase.min.js"];

export function copierGsap(racine = ROOT) {
  const source = path.join(racine, "node_modules", "gsap", "dist");
  if (!fs.existsSync(source)) {
    warn("GSAP absent de node_modules : lance `npm ci` (les vidéos ne s'animeraient pas).");
    return false;
  }
  const dest = path.join(racine, "assets", "vendor");
  fs.mkdirSync(dest, { recursive: true });
  for (const nom of GSAP) {
    const de = path.join(source, nom);
    const vers = path.join(dest, nom);
    if (!fs.existsSync(vers) || !fs.readFileSync(de).equals(fs.readFileSync(vers))) fs.copyFileSync(de, vers);
  }
  log(`  copié   ${rel(dest)}/ (GSAP, depuis node_modules)`);
  return true;
}

// ---------------------------------------------------------------------------
// 2. Style de la marque et accueil : l'outil Python s'en charge
// ---------------------------------------------------------------------------
function python() {
  const candidats = process.platform === "win32" ? [["python"], ["py", "-3"], ["python3"]] : [["python3"], ["python"]];
  for (const [cmd, ...args] of candidats) {
    const r = spawnSync(cmd, [...args, "--version"], { encoding: "utf8", windowsHide: true });
    if (r.status === 0 && /Python 3\.(9|1\d)/.test(`${r.stdout}${r.stderr}`)) return [cmd, ...args];
  }
  return null;
}

function genererStyle() {
  const py = python();
  if (!py) {
    // Sans Python, ni style, ni accueil, ni consignes de l'accueil (écrites ensuite par ce script).
    warn(`Python 3.9+ introuvable : style et accueil pas créés. Installe Python (INSTALL.md, étape 1), puis ${RELANCE}.`);
    return false;
  }
  const [cmd, ...args] = py;
  const r = spawnSync(cmd, [...args, path.join(ROOT, "tools", "studio_motion.py"), "style"], { cwd: ROOT, encoding: "utf8", windowsHide: true });
  // Sous Windows, Python écrit ses fins de ligne en \r\n.
  const lignes = (texte) => String(texte ?? "").trim().split(/\r?\n/).filter(Boolean);
  if (r.status !== 0) {
    warn(`style non généré : ${lignes(r.stderr).pop() || lignes(r.stdout).pop() || r.error?.message || `code ${r.status}`}`);
    return false;
  }
  for (const ligne of lignes(r.stdout)) log(`  ${ligne.replace(/^•\s*/, "")}`);
  return true;
}

// ---------------------------------------------------------------------------
// 3. CLAUDE.md / AGENTS.md
// ---------------------------------------------------------------------------
/** Garde le contenu des blocs {{#NOM}}…{{/NOM}} nommés dans `garder`, retire les autres. */
export function resoudreBlocs(texte, garder) {
  const gardes = new Set(garder);
  for (let avant = null; avant !== texte;) {
    avant = texte;
    texte = texte.replace(/\{\{#([A-Z0-9_]+)\}\}([\s\S]*?)\{\{\/\1\}\}/g, (_t, nom, dedans) => (gardes.has(nom) ? dedans : ""));
  }
  return texte;
}

export function remplir(texte, valeurs) {
  return texte.replace(/\{\{([A-Z0-9_]+)\}\}/g, (tout, cle) => (cle in valeurs ? String(valeurs[cle]) : tout));
}

function lireMeta(dir) {
  try {
    return JSON.parse(fs.readFileSync(path.join(dir, "meta.json"), "utf8"));
  } catch {
    return null;
  }
}

/** Les accueils de l'app HyperFrames (créés par `studio_motion.py style`). */
export function accueils(racine = ROOT) {
  return fs.readdirSync(racine, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => path.join(racine, e.name))
    .filter((d) => lireMeta(d)?.studioMotion?.lieu === "accueil");
}

export function genererInstructions(racine = ROOT) {
  const produit = lireProduit(racine);
  const modele = fs.readFileSync(path.join(racine, "templates", "AGENT.md.tpl"), "utf8");
  const lieux = [
    { dir: racine, maison: "", bloc: "LIEU_RACINE" },
    ...accueils(racine).map((dir) => ({ dir, maison: "../", bloc: "LIEU_ACCUEIL" })),
  ];
  let plusLong = 0;
  for (const lieu of lieux) {
    const valeurs = { PRODUIT: produit.nom, CODE: produit.code, VERSION: produit.version, MAISON: lieu.maison };
    for (const [fichier, agent] of [["CLAUDE.md", "CLAUDE_CODE"], ["AGENTS.md", "CODEX"]]) {
      const contenu = remplir(resoudreBlocs(modele, [agent, lieu.bloc]), valeurs);
      plusLong = Math.max(plusLong, Buffer.byteLength(contenu));
      ecrireSiDifferent(path.join(lieu.dir, fichier), contenu);
    }
    log(`  généré  ${rel(path.join(lieu.dir, "CLAUDE.md"))} + AGENTS.md`);
  }
  // Garde-fou pour qui édite le modèle : les consignes font quelques Kio, Codex en lit 32 par défaut.
  if (plusLong > LIMITE_CODEX) warn(`consignes de ${plusLong} octets : Codex n'en lit que ${LIMITE_CODEX} par défaut, raccourcis templates/AGENT.md.tpl.`);
  return true;
}

// ---------------------------------------------------------------------------
// 4. Skills pour Codex
// ---------------------------------------------------------------------------
const TAMPON = "<!-- Copie générée : éditer .claude/skills/";

/** Ajoute le tampon « Copie générée » APRÈS l'en-tête YAML : Codex ne reconnaît un skill que si
 *  SKILL.md commence par `---`. L'en-tête est reconnu en LF comme en CRLF (Git pour Windows extrait
 *  en CRLF sans .gitattributes), avec ou sans BOM ; le tampon reprend la fin de ligne du fichier. */
export function tamponner(texte, nom) {
  const tampon = `${TAMPON}${nom}/ puis npm run sync -->`;
  const entete = texte.match(/^(\uFEFF?---\r?\n[\s\S]*?\r?\n---[ \t]*(?:\r?\n|$))/);
  if (!entete) return `${tampon}\n${texte}`;
  const eol = /\r\n/.test(entete[1]) ? "\r\n" : "\n";
  const tete = /\n$/.test(entete[1]) ? entete[1] : entete[1] + eol;
  return tete + tampon + eol + texte.slice(entete[1].length);
}

export function copierSkills(racine = ROOT) {
  const source = path.join(racine, ".claude", "skills");
  const dest = path.join(racine, ".agents", "skills");
  fs.mkdirSync(dest, { recursive: true });
  const noms = fs.readdirSync(source, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name);
  for (const nom of noms) {
    // Copie à l'identique : un fichier retiré de la source ne doit pas survivre dans la copie.
    // Sous Windows, un fichier encore ouvert (Codex, antivirus) bloque un instant : on réessaie.
    fs.rmSync(path.join(dest, nom), { recursive: true, force: true, maxRetries: 3 });
    fs.cpSync(path.join(source, nom), path.join(dest, nom), { recursive: true });
    const skill = path.join(dest, nom, "SKILL.md");
    if (fs.existsSync(skill)) fs.writeFileSync(skill, tamponner(fs.readFileSync(skill, "utf8"), nom));
  }
  // Un skill retiré de .claude/skills/ disparaît aussi de la copie.
  for (const e of fs.readdirSync(dest, { withFileTypes: true })) {
    if (e.isDirectory() && !noms.includes(e.name)) fs.rmSync(path.join(dest, e.name), { recursive: true, force: true, maxRetries: 3 });
  }
  log(`  copié   ${noms.length} skills vers ${rel(dest)}/ (Codex)`);
  return true;
}

/** Lance les étapes une à une : une étape qui échoue (false ou exception) n'empêche pas les
 *  suivantes. Rend la liste des étapes en échec. */
export function lancerEtapes(etapes) {
  const echecs = [];
  for (const [nom, etape] of etapes) {
    try {
      if (etape() === false) echecs.push(nom);
    } catch (error) {
      warn(`${nom} : ${error.message}`);
      echecs.push(nom);
    }
  }
  return echecs;
}

export const messageIncomplet = (echecs) => `❌ sync incomplet : ${RELANCE} (en échec : ${echecs.join(", ")}).`;

function main() {
  const produit = lireProduit();
  log(`🔄 ${produit.nom} ${produit.version} : préparation du dossier\n`);
  const echecs = lancerEtapes([
    ["GSAP", () => copierGsap()],
    ["style et accueil", () => genererStyle()],
    ["consignes CLAUDE.md et AGENTS.md", () => genererInstructions()],
    ["skills pour Codex", () => copierSkills()],
  ]);
  if (echecs.length) {
    console.error(`\n${messageIncomplet(echecs)}`);
    return 1;
  }
  log("\nok");
  return 0;
}

if (process.argv[1] && fs.realpathSync(path.resolve(process.argv[1])) === fileURLToPath(import.meta.url)) {
  try {
    process.exitCode = main();
  } catch (error) {
    // Dossier incomplet (produit.json absent…) : le message le dit, `npm ci` n'échoue pas pour autant.
    console.error(`❌ sync incomplet : ${error.message}. Vérifie que le dossier est complet, puis ${RELANCE}.`);
    process.exitCode = 1;
  }
}
