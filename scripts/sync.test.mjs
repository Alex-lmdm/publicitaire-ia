import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import {
  resoudreBlocs, remplir, genererInstructions, copierSkills, lireProduit, tamponner, lancerEtapes, messageIncomplet,
} from "./sync.mjs";

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

test("les phrases de l'app HyperFrames ont leur consigne, à la racine comme dans l'accueil", (t) => {
  const dir = dossierDeTest(t);
  const accueil = path.join(dir, "Accueil test");
  fs.mkdirSync(accueil);
  fs.writeFileSync(path.join(accueil, "meta.json"), JSON.stringify({ studioMotion: { lieu: "accueil" } }));
  genererInstructions(dir);
  const { nom } = lireProduit(dir);
  for (const [lieu, maison] of [[dir, ""], [accueil, "../"]]) {
    for (const fichier of ["CLAUDE.md", "AGENTS.md"]) {
      const texte = fs.readFileSync(path.join(lieu, fichier), "utf8").replace(/\s+/g, " ");
      assert.ok(texte.includes(`« J'ai installé l'app HyperFrames : branche-la sur ${nom} »`), `${fichier} : brancher`);
      assert.ok(texte.includes(`node ${maison}scripts/app-hyperframes.mjs brancher`), `${fichier} : la commande`);
      assert.ok(texte.includes("« Ouvre ma dernière vidéo dans l'app HyperFrames »"), `${fichier} : ouvrir`);
      assert.ok(texte.includes(`node ${maison}scripts/app-hyperframes.mjs ouvrir`), `${fichier} : ouvrir`);
      assert.ok(texte.includes("« Mets à jour la livraison de ma vidéo »"), `${fichier} : livraison`);
    }
  }
  // La livraison se refait dans l'assistant, jamais depuis l'app.
  assert.match(fs.readFileSync(path.join(dir, "CLAUDE.md"), "utf8").replace(/\s+/g, " "), /skill `studio`, « Les retouches »/);
  assert.match(fs.readFileSync(path.join(accueil, "CLAUDE.md"), "utf8").replace(/\s+/g, " "), /elle ne se fait pas dans l'app/);
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

// Git pour Windows extrait en CRLF quand rien ne l'en empêche : l'en-tête doit être reconnu quand même,
// sinon le tampon passe avant `---` et Codex ne voit plus le skill.
test("un SKILL.md en CRLF garde son en-tête en tête de la copie pour Codex", (t) => {
  const dir = dossierDeTest(t);
  const skill = path.join(dir, ".claude", "skills", "studio");
  fs.mkdirSync(path.join(skill, "references"), { recursive: true });
  const source = "---\r\nname: studio\r\ndescription: fabrique des vidéos\r\n---\r\n# Studio\r\n\r\nTexte.\r\n";
  fs.writeFileSync(path.join(skill, "SKILL.md"), source);
  fs.writeFileSync(path.join(skill, "references", "son.md"), "a\r\nb\r\n");
  copierSkills(dir);
  const copie = fs.readFileSync(path.join(dir, ".agents", "skills", "studio", "SKILL.md"), "utf8");
  assert.ok(copie.startsWith("---\r\nname: studio\r\n"), "la copie commence toujours par l'en-tête");
  assert.match(copie, /^---\r\n[\s\S]*?\r\n---\r\n<!-- Copie générée : éditer \.claude\/skills\/studio\/ puis npm run sync -->\r\n# Studio/);
  assert.equal(copie.replace(/<!-- Copie générée[^\n]*\n/, ""), source, "rien d'autre ne change");
  assert.equal(fs.readFileSync(path.join(dir, ".agents", "skills", "studio", "references", "son.md"), "utf8"), "a\r\nb\r\n");
});

test("le tampon se pose après l'en-tête, avec BOM ou sans saut de ligne final", () => {
  const tampon = "<!-- Copie générée : éditer .claude/skills/x/ puis npm run sync -->";
  assert.equal(tamponner("---\nname: x\n---\n# X\n", "x"), `---\nname: x\n---\n${tampon}\n# X\n`);
  assert.equal(tamponner("\uFEFF---\r\nname: x\r\n---\r\nY", "x"), `\uFEFF---\r\nname: x\r\n---\r\n${tampon}\r\nY`);
  assert.equal(tamponner("---\nname: x\n---", "x"), `---\nname: x\n---\n${tampon}\n`);
  assert.equal(tamponner("# Sans en-tête\n", "x"), `${tampon}\n# Sans en-tête\n`);
});

test("une étape en échec n'arrête pas les suivantes et se dit en clair", (t) => {
  const vues = [];
  const avertissements = [];
  t.mock.method(console, "warn", (m) => avertissements.push(m));
  const echecs = lancerEtapes([
    ["un", () => vues.push("un")],
    ["deux", () => { throw new Error("disque plein"); }],
    ["trois", () => false],
    ["quatre", () => vues.push("quatre")],
  ]);
  assert.deepEqual(vues, ["un", "quatre"]);
  assert.deepEqual(echecs, ["deux", "trois"]);
  assert.match(avertissements.join("\n"), /deux : disque plein/);
  assert.match(messageIncomplet(echecs), /sync incomplet : relance `npm run sync` \(en échec : deux, trois\)/);
});

// Lancé hors du dossier complet (produit.json absent) : message clair et code 1 ; c'est le
// `|| exit 0` du postinstall qui laisse `npm ci` aller au bout.
test("un dossier incomplet le dit et sort en erreur", (t) => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "studio-sync-"));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  fs.mkdirSync(path.join(dir, "scripts"));
  fs.copyFileSync(path.join(RACINE, "scripts", "sync.mjs"), path.join(dir, "scripts", "sync.mjs"));
  const r = spawnSync(process.execPath, [path.join(dir, "scripts", "sync.mjs")], { cwd: dir, encoding: "utf8" });
  assert.equal(r.status, 1);
  assert.match(r.stderr, /sync incomplet : .*produit\.json.*relance `npm run sync`/);
  const npm = spawnSync(process.platform === "win32" ? "cmd" : "sh",
    process.platform === "win32" ? ["/c", "node scripts/sync.mjs || exit 0"] : ["-c", "node scripts/sync.mjs || exit 0"],
    { cwd: dir, encoding: "utf8" });
  assert.equal(npm.status, 0, "la commande du postinstall ne casse pas npm ci");
});
