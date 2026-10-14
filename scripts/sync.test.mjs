import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { resoudreBlocs, remplir, genererInstructions, copierSkills, lireProduit } from "./sync.mjs";

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function dossierDeTest(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "studio-sync-"));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  for (const f of ["produit.json", "VERSION"]) fs.copyFileSync(path.join(RACINE, f), path.join(dir, f));
  fs.mkdirSync(path.join(dir, "templates"));
  fs.copyFileSync(path.join(RACINE, "templates", "AGENT.md.tpl"), path.join(dir, "templates", "AGENT.md.tpl"));
  return dir;
}

test("les blocs conditionnels gardent seulement ceux demandés", () => {
  const texte = "a{{#X}}x{{#Y}}y{{/Y}}{{/X}}{{#Z}}z{{/Z}}b";
  assert.equal(resoudreBlocs(texte, ["X"]), "axb");
  assert.equal(resoudreBlocs(texte, ["X", "Y"]), "axyb");
  assert.equal(remplir("{{A}} {{B}}", { A: "1" }), "1 {{B}}");
});

test("CLAUDE.md et AGENTS.md portent le nom du produit, chacun son agent, à la racine et dans l'accueil", (t) => {
  const dir = dossierDeTest(t);
  const accueil = path.join(dir, "Accueil test");
  fs.mkdirSync(accueil);
  fs.writeFileSync(path.join(accueil, "meta.json"), JSON.stringify({ studioMotion: { lieu: "accueil" } }));
  genererInstructions(dir);
  const { nom } = lireProduit(dir);
  const claude = fs.readFileSync(path.join(dir, "CLAUDE.md"), "utf8");
  const agents = fs.readFileSync(path.join(dir, "AGENTS.md"), "utf8");
  assert.ok(claude.startsWith(`# ${nom} :`));
  assert.doesNotMatch(claude, /\{\{/);
  assert.match(claude, /outil \*\*Skill\*\*/);
  assert.doesNotMatch(agents, /outil \*\*Skill\*\*/);
  assert.match(agents, /\.agents\/skills\/<nom>\/SKILL\.md/);
  assert.match(claude, /Tu es à la racine/);
  const dansAccueil = fs.readFileSync(path.join(accueil, "CLAUDE.md"), "utf8");
  assert.match(dansAccueil, /Tu es dans l'accueil/);
  assert.match(dansAccueil, /`\.\.\/\.claude\/skills\/<nom>\/SKILL\.md`/);
  assert.doesNotMatch(dansAccueil, /Tu es à la racine/);
});

test("la copie des skills pour Codex suit exactement .claude/skills", (t) => {
  const dir = dossierDeTest(t);
  const skill = path.join(dir, ".claude", "skills", "studio");
  fs.mkdirSync(skill, { recursive: true });
  fs.writeFileSync(path.join(skill, "SKILL.md"), "---\nname: studio\n---\n# Studio\n");
  fs.mkdirSync(path.join(dir, ".agents", "skills", "ancien"), { recursive: true });
  copierSkills(dir);
  const copie = fs.readFileSync(path.join(dir, ".agents", "skills", "studio", "SKILL.md"), "utf8");
  assert.match(copie, /^---\nname: studio\n---\n<!-- Copie générée/);
  assert.equal(fs.existsSync(path.join(dir, ".agents", "skills", "ancien")), false);
});
