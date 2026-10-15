import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync, spawnSync } from 'node:child_process';
import {
  VARIABLE, APP_ID, brancher, readBranchement, settingsPath, claudeHome, findApp, isProject, ouvrir,
  produit, dossierAppel, pasUnProjet,
} from './app-hyperframes.mjs';

const { code: CODE } = produit();

const script = path.join(path.dirname(fileURLToPath(import.meta.url)), 'app-hyperframes.mjs');
// Chaque test a sa propre config Claude Code temporaire, supprimée à la fin du test.
function configDir(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'studio-app-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  return dir;
}
// Configs de Claude Code et de Codex, et dossier personnel, dans le dossier du test : jamais ceux de
// la machine. Le dossier d'appel de npm (`npm test`) ne doit pas fuir dans le script.
function envDeTest(dir, extra = {}) {
  const env = { ...process.env, HOME: dir, USERPROFILE: dir, CLAUDE_CONFIG_DIR: dir, CODEX_HOME: path.join(dir, 'codex'), ...extra };
  delete env.INIT_CWD;
  delete env.npm_lifecycle_event;
  return env;
}
const cli = (dir, ...args) => execFileSync(process.execPath, [script, ...args], { encoding: 'utf8',
  env: envDeTest(dir), stdio: ['ignore', 'pipe', 'pipe'] });

test('la config est lue là où Claude Code et l’app la lisent', () => {
  assert.equal(claudeHome({ CLAUDE_CONFIG_DIR: '/x/claude' }, '/home/a'), '/x/claude');
  assert.equal(claudeHome({}, '/home/a'), path.join('/home/a', '.claude'));
  assert.equal(settingsPath({}, '/home/a'), path.join('/home/a', '.claude', 'settings.json'));
});

test('brancher crée la config si elle manque, sans sauvegarde inutile', (t) => {
  const file = path.join(configDir(t), 'sous-dossier', 'settings.json');
  const result = brancher(file);
  assert.equal(result.changed, true);
  assert.equal(result.backup, null);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { env: { [VARIABLE]: '1' } });
});

test('brancher garde tous les réglages existants, sauvegarde, puis ne refait rien', (t) => {
  const dir = configDir(t);
  const file = path.join(dir, 'settings.json');
  const before = { model: 'opus', env: { AUTRE: 'x' }, permissions: { allow: ['Bash(ls)'] } };
  fs.writeFileSync(file, JSON.stringify(before));
  const first = brancher(file, new Date('2026-10-06T10:00:00Z'));
  assert.equal(first.changed, true);
  assert.deepEqual(JSON.parse(fs.readFileSync(first.backup, 'utf8')), before);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')),
    { ...before, env: { AUTRE: 'x', [VARIABLE]: '1' } });
  const second = brancher(file);
  assert.equal(second.changed, false);
  assert.equal(fs.readdirSync(dir).filter((f) => f.includes(`avant-${CODE}`)).length, 1);
  assert.equal(readBranchement(file).branche, true);
});

test('une config illisible n’est jamais écrasée', (t) => {
  const dir = configDir(t);
  for (const [name, content] of [['casse.json', '{ "model": '], ['env.json', '{"env": "texte"}'], ['liste.json', '[]']]) {
    const file = path.join(dir, name);
    fs.writeFileSync(file, content);
    assert.throws(() => brancher(file), /Rien n'a été modifié/);
    assert.equal(fs.readFileSync(file, 'utf8'), content);
  }
  assert.deepEqual(fs.readdirSync(dir).sort(), ['casse.json', 'env.json', 'liste.json']);
});

test('la ligne de commande dit l’état, branche, puis confirme', (t) => {
  const dir = configDir(t);
  assert.match(cli(dir, 'etat'), /à brancher/);
  assert.match(cli(dir, 'brancher'), /^Branché/);
  assert.match(cli(dir, 'brancher'), /^Déjà branché/);
  assert.match(cli(dir, 'etat'), /lit les instructions/);
  assert.match(cli(dir, 'etat'), /Codex : rien à brancher/);
  assert.equal(JSON.parse(cli(dir, 'etat', '--json')).branche, true);
});

test('seul un vrai projet HyperFrames s’ouvre dans l’app', (t) => {
  const dir = configDir(t);
  assert.equal(isProject(dir), false);
  assert.throws(() => ouvrir(dir, { platform: 'darwin', app: '/Applications/HyperFrames.app', run: () => {} }),
    /n'est pas un projet HyperFrames/);
  fs.writeFileSync(path.join(dir, 'index.html'), '<!doctype html>');
  assert.equal(isProject(dir), false);
  fs.writeFileSync(path.join(dir, 'meta.json'), '{}');
  assert.equal(isProject(dir), true);

  const calls = [];
  const opened = ouvrir(dir, { platform: 'darwin', app: '/Applications/HyperFrames.app', run: (...a) => calls.push(a) });
  assert.equal(opened.opened, true);
  assert.deepEqual(calls, [['open', ['-b', APP_ID, dir]]]);

  const noApp = ouvrir(dir, { platform: 'darwin', app: null, cli: null, run: () => assert.fail('rien à lancer') });
  assert.match(noApp.how, /Ouvrir un dossier.*hyperframes\.dev\/studio/);
  assert.match(ouvrir(dir, { platform: 'win32', app: null, cli: null }).how, /pas encore sous Windows/);
  // Linux : la CLI HyperFrames du dossier ouvre le projet dans l'app.
  const linux = [];
  assert.equal(ouvrir(dir, { platform: 'linux', app: null, cli: '/m/node_modules/.bin/hyperframes', run: (...a) => linux.push(a) }).opened, true);
  assert.deepEqual(linux, [['/m/node_modules/.bin/hyperframes', ['open', dir]]]);
  assert.match(ouvrir(dir, { platform: 'linux', app: null, cli: null }).how, /Ouvrir un dossier/);
});

test('l’app est cherchée dans les deux dossiers Applications du Mac seulement', () => {
  const seen = (paths) => (p) => paths.includes(p);
  assert.equal(findApp({ platform: 'darwin', home: '/Users/a', exists: seen(['/Users/a/Applications/HyperFrames.app']) }),
    '/Users/a/Applications/HyperFrames.app');
  assert.equal(findApp({ platform: 'darwin', home: '/Users/a', exists: seen([]) }), null);
  assert.equal(findApp({ platform: 'linux', exists: () => true }), null);
});

// Les consignes générées font quelques Kio, sous la limite de 32 Kio de Codex : rien à y régler.
test('brancher ne touche jamais à la config de Codex', (t) => {
  const dir = configDir(t);
  const codex = path.join(dir, 'codex');
  fs.mkdirSync(codex);
  const toml = 'model = "gpt-5"\n\n[profiles.rapide]\nmodel = "gpt-5-mini"\n';
  fs.writeFileSync(path.join(codex, 'config.toml'), toml);
  const sortie = cli(dir, 'brancher');
  assert.doesNotMatch(sortie, /Codex/);
  assert.deepEqual(fs.readdirSync(codex), ['config.toml'], 'ni sauvegarde ni fichier temporaire');
  assert.equal(fs.readFileSync(path.join(codex, 'config.toml'), 'utf8'), toml);
  assert.equal(readBranchement(path.join(dir, 'settings.json')).branche, true, 'Claude Code, lui, est branché');
});

test('une config Claude Code illisible fait échouer brancher sans rien écraser', (t) => {
  const dir = configDir(t);
  fs.writeFileSync(path.join(dir, 'settings.json'), '{ "model": ');
  const r = spawnSync(process.execPath, [script, 'brancher'], { encoding: 'utf8', env: envDeTest(dir) });
  assert.equal(r.status, 1, 'échec signalé');
  assert.match(r.stderr, /Claude Code : .*JSON illisible/);
  assert.equal(fs.readFileSync(path.join(dir, 'settings.json'), 'utf8'), '{ "model": ', 'jamais écrasée');
  assert.deepEqual(fs.readdirSync(dir), ['settings.json']);
});

// `npm run app` s'exécute à la racine même lancé depuis l'accueil (sans package.json) : un chemin
// relatif doit se lire depuis le dossier où la commande a été tapée.
test('un chemin relatif se lit depuis le dossier où la commande est tapée', (t) => {
  assert.equal(dossierAppel({ npm_lifecycle_event: 'app', INIT_CWD: '/d/accueil' }, '/d'), '/d/accueil');
  assert.equal(dossierAppel({ npm_lifecycle_event: 'test', INIT_CWD: '/ailleurs' }, '/d'), '/d');
  assert.equal(dossierAppel({}, '/d'), '/d');
  const dir = configDir(t);
  const accueil = path.join(dir, 'Accueil');
  fs.mkdirSync(accueil);
  for (const f of ['index.html', 'meta.json']) fs.writeFileSync(path.join(accueil, f), '{}');
  const calls = [];
  const r = ouvrir('.', { platform: 'darwin', app: '/Applications/HyperFrames.app', run: (...a) => calls.push(a), depuis: accueil });
  assert.equal(r.target, accueil);
  assert.deepEqual(calls, [['open', ['-b', APP_ID, accueil]]]);
});

/** Un dossier Publicitaire IA miniature : le script, produit.json, une vidéo et son projet. */
function dossierProduit(t) {
  const racine = path.join(fs.realpathSync(configDir(t)), 'Publicitaire IA');
  fs.mkdirSync(path.join(racine, 'scripts'), { recursive: true });
  fs.copyFileSync(script, path.join(racine, 'scripts', 'app-hyperframes.mjs'));
  fs.copyFileSync(path.join(path.dirname(script), '..', 'produit.json'), path.join(racine, 'produit.json'));
  const video = path.join(racine, 'videos', 'Ma pub · 2026-10-14');
  const projet = path.join(video, 'reel');
  fs.mkdirSync(projet, { recursive: true });
  fs.writeFileSync(path.join(video, 'OFFRE.json'), '{}');
  for (const f of ['index.html', 'meta.json']) fs.writeFileSync(path.join(projet, f), '{}');
  // Le projet a son propre package.json : `npm run app` n'y existe pas.
  fs.writeFileSync(path.join(projet, 'package.json'), '{"scripts":{"render":"hyperframes render"}}');
  return { racine, video, projet };
}

test('depuis un projet de vidéo, node ../../../scripts/app-hyperframes.mjs ouvrir . ouvre ce projet', (t) => {
  const { racine, projet } = dossierProduit(t);
  // Un faux `open` en tête du PATH : rien ne se lance pour de vrai, même si l'app est installée.
  const bin = path.join(racine, '..', 'bin');
  fs.mkdirSync(bin);
  const journal = path.join(racine, '..', 'open.log');
  fs.writeFileSync(path.join(bin, 'open'), '#!/bin/sh\necho "$@" > "$FAUX_OPEN_LOG"\n', { mode: 0o755 });
  const r = spawnSync(process.execPath, ['../../../scripts/app-hyperframes.mjs', 'ouvrir', '.'], {
    cwd: projet, encoding: 'utf8',
    env: envDeTest(path.join(racine, '..'), { PATH: `${bin}${path.delimiter}${process.env.PATH}`, FAUX_OPEN_LOG: journal }),
  });
  assert.equal(r.status, 0, r.stderr);
  if (/^Ouvert dans l'app/.test(r.stdout)) {
    assert.equal(r.stdout.trim(), `Ouvert dans l'app : ${projet}`);
    assert.equal(fs.readFileSync(journal, 'utf8').trim(), `-b ${APP_ID} ${projet}`);
  } else if (process.platform !== 'win32') {
    assert.match(r.stdout, new RegExp(projet.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')), 'le geste à faire nomme ce projet');
  }
});

test('un dossier qui n’est pas un projet oriente vers la bonne commande', (t) => {
  const { racine, video, projet } = dossierProduit(t);
  const r = spawnSync(process.execPath, ['../../scripts/app-hyperframes.mjs', 'ouvrir', '.'], { cwd: video, encoding: 'utf8', env: envDeTest(racine) });
  assert.equal(r.status, 1);
  assert.match(r.stderr, /dossier d'une vidéo : ouvre l'un de ses projets \(reel\), par exemple node \.\.[\\/]\.\.[\\/]scripts[\\/]app-hyperframes\.mjs ouvrir reel/);
  assert.match(pasUnProjet(racine, racine), /est le dossier .* lui-même, pas un projet de l'app/);
  assert.match(pasUnProjet(path.join(racine, 'nulle-part'), racine), /introuvable/);
  assert.match(pasUnProjet(path.join(racine, 'videos'), racine), /n'est pas un projet HyperFrames/);
  const vide = path.join(racine, 'vide');
  fs.mkdirSync(vide);
  assert.match(pasUnProjet(vide, racine), /n'est pas un projet HyperFrames.*node \.\.\/\.\.\/\.\.\/scripts\/app-hyperframes\.mjs ouvrir \./);
  const usage = spawnSync(process.execPath, ['../../../scripts/app-hyperframes.mjs'], { cwd: projet, encoding: 'utf8', env: envDeTest(racine) });
  assert.equal(usage.status, 2);
  assert.match(usage.stderr, /Usage : node \.\.[\\/]\.\.[\\/]\.\.[\\/]scripts[\\/]app-hyperframes\.mjs etat/);
});
