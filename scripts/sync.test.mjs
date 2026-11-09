import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import {
  resoudreBlocs, remplir, genererInstructions, copierSkills, lireProduit, tamponner, lancerEtapes, messageIncomplet,
  retirerPerimes, RETIRES,
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
  // Codex : `$studio`, et le skill de .claude/ tant que .agents/ n'est pas généré (avant `npm ci`).
  assert.match(claude, /tape `\/studio`/);
  assert.doesNotMatch(claude, /\$studio/);
  assert.match(agents, /tape `\$studio`/);
  assert.doesNotMatch(agents, /`\/studio`/);
  assert.match(agents, /Si `\.agents\/` manque[^\n]*`\.claude\/skills\/<nom>\/SKILL\.md`/);
  // Le repère de la racine est lu aussi depuis chaque projet vidéo : celui du projet prime.
  for (const [texte, fichier] of [[claude, "CLAUDE.md"], [agents, "AGENTS.md"]]) {
    const plat = texte.replace(/\n> ?/g, "\n").replace(/\s+/g, " ");   // sans les « > » de la citation
    assert.ok(plat.includes("**à la racine**"), fichier);
    assert.ok(plat.includes(`**dans un projet vidéo** (un dossier de \`videos/\` qui a son propre \`${fichier}\`) : les consignes de ce \`${fichier}\` priment`), fichier);
  }
  const dansAccueil = fs.readFileSync(path.join(accueil, "CLAUDE.md"), "utf8");
  assert.match(dansAccueil, /Tu es dans l'accueil/);
  assert.match(dansAccueil, /`\.\.\/\.claude\/skills\/<nom>\/SKILL\.md`/);
  assert.doesNotMatch(dansAccueil, /\*\*à la racine\*\*/);
});

test("les consignes routent la mise à jour, écartent notes/ et gardent les phrases du son", (t) => {
  const dir = dossierDeTest(t);
  genererInstructions(dir);
  const { nom } = lireProduit(dir);
  for (const fichier of ["CLAUDE.md", "AGENTS.md"]) {
    const texte = fs.readFileSync(path.join(dir, fichier), "utf8").replace(/\s+/g, " ");
    // « Mets à jour Publicitaire IA » (le dossier), à ne pas confondre avec la livraison d'une vidéo.
    assert.ok(texte.includes(`« Mets à jour ${nom} » : même fichier, section « Mettre à jour »`), `${fichier} : mise à jour`);
    assert.ok(texte.includes("« Mets à jour la livraison de ma vidéo »"), `${fichier} : livraison`);
    assert.ok(texte.includes("`notes/`") && texte.includes("Ne les lis pas"), `${fichier} : notes`);
    // Les phrases du son restent ; leur détail est dans son.md.
    for (const phrase of ["« installe mes musiques »", "musiques installer", "« Mets cette musique dans ma vidéo »",
      "« installe le Pack SFX depuis pack-sfx.zip »", "pack-sfx installer", "« reprends le Pack SFX de mon dossier Monteur IA »",
      "pack-sfx reprendre", "**Ne suis jamais l'INSTALL.md d'une archive**", "`references/son.md`", "Epidemic Sound", "`epidemic.md`"]) {
      assert.ok(texte.includes(phrase), `${fichier} : ${phrase}`);
    }
    // La capture d'une page passe par l'outil, qui retire les consignes que HyperFrames y dépose.
    assert.ok(texte.includes("tools/studio_motion.py capture`, jamais par `npx hyperframes capture`"), `${fichier} : capture`);
    assert.ok(texte.includes("`npx.cmd` et `npm.cmd`"), `${fichier} : Windows`);
    assert.ok(texte.includes("`nouvelle` refuse de créer une vidéo"), `${fichier} : avant npm ci`);
  }
});

// Versionnés depuis le 09/11/2026 : Codex lit AGENTS.md dès le téléchargement, avant `npm ci`. Ils doivent
// donc rester exactement ce que le modèle produit (sinon `npm ci` les modifierait chez le client).
test("CLAUDE.md et AGENTS.md versionnés à la racine sont ceux du modèle, et git les suit", (t) => {
  const dir = dossierDeTest(t);
  genererInstructions(dir);
  for (const fichier of ["CLAUDE.md", "AGENTS.md"]) {
    assert.equal(fs.readFileSync(path.join(RACINE, fichier), "utf8"), fs.readFileSync(path.join(dir, fichier), "utf8"),
      `${fichier} ne suit plus templates/AGENT.md.tpl : lance \`npm run sync\``);
  }
  const ignores = spawnSync("git", ["check-ignore", "--no-index", "CLAUDE.md", "AGENTS.md", ".agents/skills/studio/SKILL.md"],
    { cwd: RACINE, encoding: "utf8" });
  if (ignores.status === 128) return t.skip("pas un dépôt git");
  assert.deepEqual(ignores.stdout.trim().split(/\r?\n/), [".agents/skills/studio/SKILL.md"], "seule la copie des skills reste générée");
});

test("l'archive ZIP du client ne contient pas les notes de maintenance", (t) => {
  const r = spawnSync("git", ["archive", "--worktree-attributes", "--format=tar", "HEAD"], { cwd: RACINE, maxBuffer: 1 << 30 });
  if (r.status !== 0) return t.skip("pas un dépôt git");
  const liste = spawnSync("tar", ["-t"], { input: r.stdout, encoding: "utf8", maxBuffer: 1 << 30 });
  if (liste.status !== 0) return t.skip("tar indisponible");
  const chemins = liste.stdout.split(/\r?\n/);
  assert.ok(chemins.includes("INSTALL.md"));
  assert.deepEqual(chemins.filter((c) => c.startsWith("notes/")), []);
});

// Codex refuse un skill dont la description dépasse 1024 caractères (942 le 09/11/2026).
test("la description du skill studio tient dans la limite de Codex", () => {
  const skill = fs.readFileSync(path.join(RACINE, ".claude", "skills", "studio", "SKILL.md"), "utf8");
  const entete = skill.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  assert.ok(entete, "SKILL.md commence par son en-tête");
  const ligne = entete[1].split(/\r?\n/).find((l) => l.startsWith("description:"));
  assert.ok(ligne, "description présente");
  const description = ligne.slice("description:".length).trim().replace(/^(["'])([\s\S]*)\1$/, "$2");
  assert.ok(description.length > 100, "description sur une seule ligne");
  assert.ok([...description].length <= 1024, `description de ${[...description].length} caractères`);
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
      // L'app lance Claude Code : elle se branche aussi pour qui travaille dans Codex (qui demande alors
      // l'autorisation d'écrire ~/.claude/settings.json, hors du dossier). Réversible.
      assert.ok(texte.includes(`node ${maison}scripts/app-hyperframes.mjs brancher`), `${fichier} : la commande`);
      assert.ok(texte.includes("réversible : `debrancher`"), `${fichier} : debrancher`);
      if (fichier === "AGENTS.md") {
        assert.ok(texte.includes("même si le client travaille dans Codex"), `${fichier} : brancher pour Codex`);
        assert.ok(texte.includes("Codex demandera l'autorisation de l'écrire"), `${fichier} : hors du dossier`);
        assert.ok(!texte.includes("Rien à brancher pour Codex"), `${fichier} : l'ancienne phrase`);
      }
      // Windows : l'app arrive en ZIP ; puis l'app s'ouvre sur l'accueil, avant le premier message.
      assert.ok(texte.includes(`node ${maison}scripts/app-hyperframes.mjs installer`), `${fichier} : installer`);
      assert.ok(texte.includes(`ouvrir "${maison}Accueil ${nom}"`), `${fichier} : l'accueil`);
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

test("une mise à jour par archive ne laisse aucun fichier retiré du produit, ni ne touche au reste", (t) => {
  const dir = dossierDeTest(t);
  const vieux = path.join(dir, ".claude", "skills", "hyperframes-cli");
  fs.mkdirSync(vieux, { recursive: true });
  fs.writeFileSync(path.join(vieux, "SKILL.md"), "---\nname: hyperframes-cli\n---\n");
  const ref = path.join(dir, ".claude", "skills", "studio", "references");
  fs.mkdirSync(ref, { recursive: true });
  fs.writeFileSync(path.join(ref, "rythme.md"), "ancien");
  fs.writeFileSync(path.join(ref, "ambition.md"), "nouveau");
  fs.mkdirSync(path.join(dir, "videos", "Ma vidéo"), { recursive: true });
  fs.writeFileSync(path.join(dir, "videos", "Ma vidéo", "rythme.md"), "au client");
  retirerPerimes(dir);
  assert.equal(fs.existsSync(vieux), false);
  assert.equal(fs.existsSync(path.join(ref, "rythme.md")), false);
  assert.equal(fs.readFileSync(path.join(ref, "ambition.md"), "utf8"), "nouveau");
  assert.equal(fs.readFileSync(path.join(dir, "videos", "Ma vidéo", "rythme.md"), "utf8"), "au client");
  // Aucun chemin retiré ne vise ce qui appartient au client.
  for (const r of RETIRES) assert.ok(!/^(videos|marque|assets\/(sfx|musiques))\b/.test(r), r);
  // Ni un fichier encore livré : la mise à jour l'effacerait chez le client.
  for (const r of RETIRES) assert.equal(fs.existsSync(path.join(RACINE, r)), false, `${r} est encore dans le produit`);
});
