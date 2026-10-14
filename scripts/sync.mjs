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
 */

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const rel = (p) => path.relative(ROOT, p) || ".";
const log = (msg) => console.log(msg);
const warn = (msg) => console.warn(`⚠️  ${msg}`);

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
    const r = spawnSync(cmd, [...args, "--version"], { encoding: "utf8" });
    if (r.status === 0 && /Python 3\.(9|1\d)/.test(`${r.stdout}${r.stderr}`)) return [cmd, ...args];
  }
  return null;
}

function genererStyle() {
  const py = python();
  if (!py) {
    warn("Python 3.9+ introuvable : le style et l'accueil seront créés au premier `studio_motion.py verifier`.");
    return;
  }
  const [cmd, ...args] = py;
  const r = spawnSync(cmd, [...args, path.join(ROOT, "tools", "studio_motion.py"), "style"], { cwd: ROOT, encoding: "utf8" });
  if (r.status !== 0) warn(`style non généré : ${(r.stderr || r.stdout).trim().split("\n").pop()}`);
  else for (const ligne of r.stdout.trim().split("\n").filter(Boolean)) log(`  ${ligne.replace(/^•\s*/, "")}`);
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
  if (plusLong > LIMITE_CODEX) warn(`consignes de ${plusLong} octets : Codex n'en lit que ${LIMITE_CODEX} par défaut (npm run app -- brancher).`);
}

// ---------------------------------------------------------------------------
// 4. Skills pour Codex
// ---------------------------------------------------------------------------
const TAMPON = "<!-- Copie générée : éditer .claude/skills/";

export function copierSkills(racine = ROOT) {
  const source = path.join(racine, ".claude", "skills");
  const dest = path.join(racine, ".agents", "skills");
  fs.mkdirSync(dest, { recursive: true });
  const noms = fs.readdirSync(source, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name);
  for (const nom of noms) {
    // Copie à l'identique : un fichier retiré de la source ne doit pas survivre dans la copie.
    fs.rmSync(path.join(dest, nom), { recursive: true, force: true });
    fs.cpSync(path.join(source, nom), path.join(dest, nom), { recursive: true });
    const skill = path.join(dest, nom, "SKILL.md");
    if (fs.existsSync(skill)) {
      const texte = fs.readFileSync(skill, "utf8");
      const tampon = `${TAMPON}${nom}/ puis npm run sync -->`;
      const entete = texte.match(/^(---\n[\s\S]*?\n---\n)/);
      fs.writeFileSync(skill, entete ? entete[1] + tampon + "\n" + texte.slice(entete[1].length) : tampon + "\n" + texte);
    }
  }
  // Un skill retiré de .claude/skills/ disparaît aussi de la copie.
  for (const e of fs.readdirSync(dest, { withFileTypes: true })) {
    if (e.isDirectory() && !noms.includes(e.name)) fs.rmSync(path.join(dest, e.name), { recursive: true, force: true });
  }
  log(`  copié   ${noms.length} skills vers ${rel(dest)}/ (Codex)`);
}

function main() {
  const produit = lireProduit();
  log(`🔄 ${produit.nom} ${produit.version} : préparation du dossier\n`);
  copierGsap();
  genererStyle();
  genererInstructions();
  copierSkills();
  log("\nok");
}

if (process.argv[1] && fs.realpathSync(path.resolve(process.argv[1])) === fileURLToPath(import.meta.url)) {
  try {
    main();
  } catch (error) {
    console.error(`❌ ${error.message}`);
    process.exitCode = 1;
  }
}
