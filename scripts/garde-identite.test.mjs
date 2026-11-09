import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { decision, HYPERFRAMES_INTERDITES } from '../.claude/hooks/garde-identite.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const GARDE = path.join(root, '.claude/hooks/garde-identite.mjs');
const refuse = (tool_name, tool_input) => decision({ tool_name, tool_input })?.hookSpecificOutput.permissionDecision === 'deny';

test("une adresse email dans un en-tête HTTP vers un site est refusée", () => {
  for (const command of [
    'curl -s -A "MonBot/1.0 (julie.martin@gmail.com)" "https://commons.wikimedia.org/w/api.php"',
    'UA="MonBot/1.0 (julie.martin@gmail.com)"; curl -sL -A "$UA" -o a.png "https://upload.wikimedia.org/a.png"',
    "curl -H 'X-User-Email: julie.martin@gmail.com' https://site-tiers.com/api",
    'curl --header "From: client@boutique.fr" https://site-tiers.com',
    'wget --user-agent="Agent (julie.martin@gmail.com)" https://site-tiers.com',
    "node -e \"fetch('https://x.io', { headers: { 'User-Agent': 'bot (julie.martin@gmail.com)' } })\"",
    "python3 -c \"import requests; requests.get('https://x.io', headers={'X-Operator': 'julie.martin@gmail.com'})\"",
  ]) assert.ok(refuse('Bash', { command }), command);
  assert.ok(refuse('PowerShell', { command: 'Invoke-WebRequest https://x.io -UserAgent "bot (julie.martin@gmail.com)"' }));
  assert.ok(refuse('PowerShell', { command: "irm https://x.io -Headers @{ 'X-User' = 'julie.martin@gmail.com' }" }));
  assert.ok(refuse('WebFetch', { url: 'https://site-tiers.com/agents?user=julie.martin%40gmail.com', prompt: 'x' }));
});

test("le travail normal passe, adresses comprises hors des en-têtes", () => {
  for (const command of [
    'curl -s -A "Mozilla/5.0" https://commons.wikimedia.org/w/api.php',
    'curl -s -H "Authorization: Bearer $HEYGEN_API_KEY" https://api.heygen.com/v2/voices',
    'grep -H "julie.martin@gmail.com" -r reels/',
    'grep -A 5 "julie.martin@gmail.com" brand.config.json',
    'git commit -m "contact : julie.martin@gmail.com"',
    "curl -s -H 'Content-Type: application/json' -d '{\"email\":\"julie.martin@gmail.com\"}' http://localhost:3000/api",
    'curl -s -H "X-Test: jean@example.com" https://site-tiers.com',
    'python3 tools/finaliser.py "reels/ma-video · 2026-10-23"',
    'npx hyperframes render',
  ]) assert.ok(!refuse('Bash', { command }), command);
  assert.ok(!refuse('WebFetch', { url: 'http://localhost:3002/?email=julie.martin%40gmail.com', prompt: 'x' }));
  assert.ok(!refuse('WebFetch', { url: 'https://hyperframes.heygen.com/docs', prompt: 'x' }));
  assert.ok(!refuse('Read', { file_path: '/tmp/x' }));
});

test('lancé comme Claude Code le lance, il refuse en JSON et laisse passer sans rien écrire', () => {
  const lancer = (entree) => spawnSync(process.execPath, [GARDE], { input: entree, encoding: 'utf8' });
  const refus = lancer(JSON.stringify({ tool_name: 'Bash', tool_input: { command: 'curl -A "bot (julie.martin@gmail.com)" https://x.io' } }));
  assert.equal(refus.status, 0);
  assert.equal(JSON.parse(refus.stdout).hookSpecificOutput.permissionDecision, 'deny');
  for (const entree of [JSON.stringify({ tool_name: 'Bash', tool_input: { command: 'ls' } }), 'pas du JSON', '']) {
    const r = lancer(entree);
    assert.equal(r.status, 0);
    assert.equal(r.stdout, '');
  }
});

// Le réglage tel que Claude Code l'exécute (sh -c sur Mac, Git Bash sur Windows) : il remplace lui-même
// ${CLAUDE_PROJECT_DIR}. « ; exit 0 » (valable aussi sous PowerShell) garde le silence quand Node.js
// n'est pas trouvé : sans lui, chaque commande afficherait « hook error » à la personne.
const reglage = JSON.parse(fs.readFileSync(path.join(root, '.claude/settings.json'), 'utf8'));
const [entree] = reglage.hooks.PreToolUse;
const commande = entree.hooks[0].command.replaceAll('${CLAUDE_PROJECT_DIR}', root);
const viaLeReglage = (PATH, appel) => spawnSync('/bin/sh', ['-c', commande], { input: JSON.stringify(appel), encoding: 'utf8',
  env: { ...process.env, PATH } });

test('le réglage de Claude Code lance ce garde-fou avant les commandes et les pages lues', () => {
  assert.equal(entree.matcher, 'Bash|PowerShell|WebFetch');
  const r = viaLeReglage(`${path.dirname(process.execPath)}:/usr/bin:/bin`,
    { tool_name: 'WebFetch', tool_input: { url: 'https://x.io/?u=julie.martin%40gmail.com' } });
  assert.equal(r.status, 0);
  assert.equal(JSON.parse(r.stdout).hookSpecificOutput.permissionDecision, 'deny');
});

test("sans Node.js visible, le réglage se tait au lieu d'afficher une erreur", { skip: process.platform === 'win32' }, () => {
  const r = viaLeReglage('/nulle-part', { tool_name: 'Bash', tool_input: { command: 'ls' } });
  assert.equal(r.status, 0);
  assert.equal(r.stdout, '');
});

// ---------------------------------------------------------------------------------------------------------
// Les commandes de HyperFrames qui envoient quelque chose hors de l'ordinateur (revue du 09/11/2026 : elles ne
// tenaient qu'au texte des consignes). Claude Code les refuse par permissions.deny et par ce garde-fou ;
// Codex, qui n'a pas ces règles, par ce garde-fou seulement.
// ---------------------------------------------------------------------------------------------------------
test("les commandes de HyperFrames qui sortent de l'ordinateur sont refusées, sous toutes leurs formes", () => {
  assert.deepEqual([...HYPERFRAMES_INTERDITES].sort(),
    ['auth', 'cloud', 'cloudrun', 'events', 'feedback', 'lambda', 'publish', 'usage']);
  for (const sous of HYPERFRAMES_INTERDITES) {
    assert.ok(refuse('Bash', { command: `npx hyperframes ${sous}` }), sous);
    assert.ok(refuse('PowerShell', { command: `npx.cmd hyperframes ${sous} --help` }), sous);
  }
  for (const command of [
    'cd "videos/Offre · 2026-11-09/Offre · Reel" && npx hyperframes publish --yes',
    'npx -y hyperframes@0.9.26 feedback "super outil"',
    'npm exec hyperframes -- auth login',
    'node node_modules/hyperframes/bin/hyperframes.mjs usage',
    './node_modules/.bin/hyperframes events',
    "bash -lc 'npx hyperframes lambda deploy'",
    'cmd /c "npx.cmd hyperframes cloudrun deploy"',
    'FOO=1 timeout 60 npx hyperframes --verbose cloud deploy',
    'ls\nnpx hyperframes publish',
  ]) assert.ok(refuse('Bash', { command }), command);
  assert.ok(refuse('PowerShell', { command: '& npx.cmd hyperframes publish' }));
  // Une commande en liste de mots.
  assert.ok(refuse('Bash', { command: ['bash', '-lc', 'npx hyperframes publish'] }));
});

test("le travail normal avec HyperFrames passe, et une phrase qui cite une commande interdite aussi", () => {
  for (const command of [
    'npx hyperframes check', 'npx hyperframes lint', 'npx hyperframes snapshot --at 1.5', 'npx.cmd hyperframes render',
    'npx hyperframes telemetry disable', 'npx hyperframes browser ensure', 'npx hyperframes render -o publish.mp4',
    'npm run render', 'grep -rn "hyperframes publish" .claude/skills', 'echo "jamais npx hyperframes publish"',
    'ls hyperframes-auth', 'npx hyperframes publishing',
  ]) assert.ok(!refuse('Bash', { command }), command);
});

test("la liste des commandes interdites est la même dans les consignes et dans les réglages de Claude Code", () => {
  const modele = fs.readFileSync(path.join(root, 'templates/AGENT.md.tpl'), 'utf8').replace(/\s+/g, ' ');
  const ligne = modele.slice(modele.indexOf('**Jamais** `hyperframes'), modele.indexOf('rien ne quitte son ordinateur sans lui'));
  for (const sous of HYPERFRAMES_INTERDITES) assert.match(ligne, new RegExp(`\`(hyperframes )?${sous}\``), `consignes : ${sous}`);
  const { deny, allow, ask } = reglage.permissions;
  const attendu = HYPERFRAMES_INTERDITES.flatMap((sous) => ['Bash', 'PowerShell'].flatMap((outil) =>
    ['npx', 'npx.cmd'].map((npx) => `${outil}(${npx} hyperframes ${sous} *)`)));
  assert.deepEqual([...deny].sort(), [...attendu].sort());
  // Autorisés sans demande : nos propres outils seulement.
  const NOS_OUTILS = /^(Bash|PowerShell)\((python3? (\.\.\/\.\.\/\.\.\/)?tools\/studio_motion\.py|npx(\.cmd)? hyperframes (check|lint|snapshot|render)|npm(\.cmd)? run (check|render)) \*\)$/;
  for (const regle of allow) assert.match(regle, NOS_OUTILS);
  for (const regle of ['Bash(python3 tools/studio_motion.py *)', 'Bash(python ../../../tools/studio_motion.py *)',
    'Bash(npx hyperframes render *)', 'Bash(npm run check *)', 'PowerShell(npx.cmd hyperframes check *)']) {
    assert.ok(allow.includes(regle), regle);
  }
  // Une génération payante (HeyGen, `--confirme`) redemande toujours l'accord, malgré l'autorisation de l'outil.
  assert.deepEqual(ask, ['Bash(*--confirme*)', 'PowerShell(*--confirme*)']);
});

// ---------------------------------------------------------------------------------------------------------
// Codex : `.codex/hooks.json` lance le même garde-fou. Codex exécute la commande avec `$SHELL -lc` (Mac,
// Linux) ou `cmd.exe /C` (Windows, `commandWindows`), depuis le dossier où il travaille : la racine, ou un
// projet vidéo plus bas. Il ne donne aucune variable pour la racine : la commande cherche le script en
// remontant les dossiers.
// ---------------------------------------------------------------------------------------------------------
const codex = JSON.parse(fs.readFileSync(path.join(root, '.codex/hooks.json'), 'utf8'));
const [groupe] = codex.hooks.PreToolUse;
const [crochet] = groupe.hooks;
const codeJs = (c) => /^node -e "([^"]*)"/.exec(c)?.[1];
const appelCodex = (command, cwd) => JSON.stringify({
  session_id: 's', transcript_path: null, cwd, hook_event_name: 'PreToolUse', model: 'gpt-5.5', turn_id: 't',
  permission_mode: 'default', tool_name: 'Bash', tool_use_id: 'u', tool_input: { command },
});

test('le réglage de Codex a la forme attendue et ne vise que les commandes', () => {
  assert.deepEqual(Object.keys(codex), ['hooks']);
  assert.deepEqual(Object.keys(codex.hooks), ['PreToolUse']);
  assert.ok(new RegExp(groupe.matcher).test('Bash'));
  for (const autre of ['apply_patch', 'mcp__x__bash', 'update_plan']) assert.ok(!new RegExp(groupe.matcher).test(autre), autre);
  assert.equal(crochet.type, 'command');
  assert.ok(crochet.timeout <= 30);
  // Le même code JS sous les deux formes : sans « $ », « ` », « \ » ni « ! » (sh, entre guillemets
  // doubles), sans « % » (cmd.exe).
  assert.ok(codeJs(crochet.command), 'command : node -e "…"');
  assert.equal(codeJs(crochet.commandWindows), codeJs(crochet.command));
  assert.equal(crochet.commandWindows, `node -e "${codeJs(crochet.command)}"`);
  assert.doesNotMatch(codeJs(crochet.command), /[$`\\!%"]/);
  assert.match(crochet.command, /"; exit 0$/);
});

test('lancé comme Codex le lance, depuis la racine ou un projet vidéo, il refuse ; ailleurs, il se tait', { skip: process.platform === 'win32' }, (t) => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'garde-codex-'));
  const ailleurs = fs.mkdtempSync(path.join(os.tmpdir(), 'ailleurs-'));
  t.after(() => {
    fs.rmSync(dir, { recursive: true, force: true });
    fs.rmSync(ailleurs, { recursive: true, force: true });
  });
  fs.mkdirSync(path.join(dir, '.claude/hooks'), { recursive: true });
  fs.copyFileSync(GARDE, path.join(dir, '.claude/hooks/garde-identite.mjs'));
  const projet = path.join(dir, 'videos', 'Offre · 2026-11-09', 'Offre · Reel');
  fs.mkdirSync(projet, { recursive: true });
  const PATH = `${path.dirname(process.execPath)}:/usr/bin:/bin`;
  const lancer = (command, cwd, chemin = PATH) => spawnSync('/bin/sh', ['-lc', crochet.command],
    { cwd, input: appelCodex(command, cwd), encoding: 'utf8', env: { ...process.env, PATH: chemin } });
  for (const cwd of [dir, projet]) {
    for (const command of ['npx hyperframes publish', 'curl -A "bot (julie.martin@gmail.com)" https://x.io']) {
      const r = lancer(command, cwd);
      assert.equal(r.status, 0, r.stderr);
      assert.equal(JSON.parse(r.stdout).hookSpecificOutput.permissionDecision, 'deny', `${command} depuis ${path.basename(cwd)}`);
    }
    const ok = lancer('npx hyperframes check', cwd);
    assert.equal(ok.status, 0);
    assert.equal(ok.stdout, '');
  }
  const hors = lancer('npx hyperframes publish', ailleurs);
  assert.equal(hors.status, 0);
  assert.equal(hors.stdout, '', 'hors du dossier, rien à garder');
  const sansNode = lancer('npx hyperframes publish', dir, '/nulle-part');
  assert.equal(sansNode.status, 0, 'sans Node.js, il se tait');
  assert.equal(sansNode.stdout, '');
  // Le code de Windows, lancé sans shell (cmd.exe /C le passe tel quel à node).
  const win = spawnSync(process.execPath, ['-e', codeJs(crochet.commandWindows)],
    { cwd: projet, input: appelCodex('npx.cmd hyperframes cloud deploy', projet), encoding: 'utf8' });
  assert.equal(JSON.parse(win.stdout).hookSpecificOutput.permissionDecision, 'deny');
});
