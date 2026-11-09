import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync, spawnSync } from 'node:child_process';
import {
  VARIABLE, APP_ID, brancher, debrancher, readBranchement, settingsPath, claudeHome, findApp, isProject, ouvrir,
  produit, dossierAppel, pasUnProjet, sourceWindows, installerWindows, DOSSIER_WIN, cibleReelle,
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

test('debrancher retire seulement la variable posée par brancher, sans rien restaurer', (t) => {
  const dir = configDir(t);
  const file = path.join(dir, 'settings.json');
  const avant = { model: 'opus', env: { AUTRE: 'x' }, permissions: { allow: ['Bash(ls)'] } };
  fs.writeFileSync(file, JSON.stringify(avant));
  brancher(file, new Date('2026-10-06T10:00:00Z'));
  // Un réglage changé après le branchement : debrancher le garde (aucune sauvegarde n'est restaurée).
  const branche = JSON.parse(fs.readFileSync(file, 'utf8'));
  fs.writeFileSync(file, JSON.stringify({ ...branche, model: 'sonnet' }));
  const r = debrancher(file, new Date('2026-11-09T10:00:00Z'));
  assert.equal(r.changed, true);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { ...avant, model: 'sonnet' });
  assert.equal(JSON.parse(fs.readFileSync(r.backup, 'utf8')).env[VARIABLE], '1', 'sauvegarde de ce qui était là');
  assert.equal(readBranchement(file).branche, false);
  assert.equal(debrancher(file).changed, false, 'refaire ne change rien');
  // Une config créée par brancher : la clé env, vide, part aussi ; le fichier reste.
  const neuf = path.join(dir, 'neuf', 'settings.json');
  brancher(neuf);
  debrancher(neuf);
  assert.deepEqual(JSON.parse(fs.readFileSync(neuf, 'utf8')), {});
  // Une valeur que brancher n'a pas posée (« 0 ») reste, comme une config illisible.
  const autre = path.join(dir, 'autre.json');
  fs.writeFileSync(autre, JSON.stringify({ env: { [VARIABLE]: '0' } }));
  assert.equal(debrancher(autre).changed, false);
  assert.equal(fs.readFileSync(autre, 'utf8'), JSON.stringify({ env: { [VARIABLE]: '0' } }));
  const casse = path.join(dir, 'casse.json');
  fs.writeFileSync(casse, '{ "env": ');
  assert.throws(() => debrancher(casse), /Rien n'a été modifié/);
  assert.equal(fs.readFileSync(casse, 'utf8'), '{ "env": ');
});

test('la ligne de commande débranche', (t) => {
  const dir = configDir(t);
  assert.match(cli(dir, 'debrancher'), /^Rien à débrancher/);
  assert.match(cli(dir, 'brancher'), /Pour revenir en arrière : .*debrancher/);
  assert.match(cli(dir, 'debrancher'), /^Débranché/);
  assert.match(cli(dir, 'etat'), /à brancher/);
});

test('un settings.json en lien symbolique reste un lien : sa cible est écrite', { skip: process.platform === 'win32' }, (t) => {
  const dir = configDir(t);
  const rangee = path.join(dir, 'dotfiles', 'claude-settings.json');
  fs.mkdirSync(path.dirname(rangee));
  fs.writeFileSync(rangee, JSON.stringify({ model: 'opus' }));
  const file = path.join(dir, 'settings.json');
  fs.symlinkSync(rangee, file);
  assert.equal(cibleReelle(file), fs.realpathSync(rangee));
  assert.equal(cibleReelle(path.join(dir, 'absent.json')), path.join(dir, 'absent.json'));
  brancher(file);
  assert.ok(fs.lstatSync(file).isSymbolicLink(), 'toujours un lien après brancher');
  assert.deepEqual(JSON.parse(fs.readFileSync(rangee, 'utf8')), { model: 'opus', env: { [VARIABLE]: '1' } });
  debrancher(file);
  assert.ok(fs.lstatSync(file).isSymbolicLink(), 'toujours un lien après debrancher');
  assert.deepEqual(JSON.parse(fs.readFileSync(rangee, 'utf8')), { model: 'opus' });
  // Un lien cassé (sa cible pas encore créée) : la cible est créée, le lien reste.
  const casse = path.join(dir, 'lien-casse.json');
  fs.symlinkSync(path.join(dir, 'ailleurs', 'settings.json'), casse);
  brancher(casse);
  assert.ok(fs.lstatSync(casse).isSymbolicLink());
  assert.equal(readBranchement(casse).branche, true);
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
  assert.match(noApp.how, /Ouvrir un dossier.*hyperframes\.studio\/studio/);
  // Windows (app disponible depuis octobre 2026) : l'app reçoit le dossier ; sans elle, le geste à la main.
  const win = [];
  assert.equal(ouvrir(dir, { platform: 'win32', app: 'C:\\L\\HyperFrames.exe', cli: null, launch: (...a) => win.push(a) }).opened, true);
  assert.deepEqual(win, [['C:\\L\\HyperFrames.exe', [dir]]]);
  assert.match(ouvrir(dir, { platform: 'win32', app: null, cli: null }).how, /Ctrl \+ O.*hyperframes\.studio\/studio/);
  // Linux : la CLI HyperFrames du dossier ouvre le projet dans l'app.
  const linux = [];
  assert.equal(ouvrir(dir, { platform: 'linux', app: null, cli: '/m/node_modules/.bin/hyperframes', run: (...a) => linux.push(a) }).opened, true);
  assert.deepEqual(linux, [['/m/node_modules/.bin/hyperframes', ['open', dir]]]);
  assert.match(ouvrir(dir, { platform: 'linux', app: null, cli: null }).how, /Ouvrir un dossier/);
});

test('l’app est cherchée dans les dossiers Applications du Mac et dans Programs sous Windows', () => {
  const seen = (paths) => (p) => paths.includes(p);
  assert.equal(findApp({ platform: 'darwin', home: '/Users/a', exists: seen(['/Users/a/Applications/HyperFrames.app']) }),
    '/Users/a/Applications/HyperFrames.app');
  assert.equal(findApp({ platform: 'darwin', home: '/Users/a', exists: seen([]) }), null);
  assert.equal(findApp({ platform: 'linux', exists: () => true }), null);
  const exe = 'C:\\Users\\a\\AppData\\Local\\Programs\\HyperFrames\\HyperFrames.exe';
  assert.equal(findApp({ platform: 'win32', env: { LOCALAPPDATA: 'C:\\Users\\a\\AppData\\Local' }, exists: seen([exe]) }), exe);
  assert.equal(findApp({ platform: 'win32', env: {}, exists: () => true }), null);
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

// Windows depuis le 02/11/2026 : l'app arrive en ZIP (HyperFrames-win-x64.zip → HyperFrames-win32-x64\HyperFrames.exe).
// Les chemins POSIX d'un dossier temporaire tiennent lieu de ceux de Windows ; `tar` décompresse le ZIP comme sous Windows.
function fauxWindows(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'studio-win-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  const env = { USERPROFILE: path.join(dir, 'user'), LOCALAPPDATA: path.join(dir, 'local'), APPDATA: path.join(dir, 'roaming') };
  fs.mkdirSync(path.join(env.USERPROFILE, 'Downloads'), { recursive: true });
  const app = path.join(dir, 'zip', DOSSIER_WIN);
  fs.mkdirSync(path.join(app, 'resources'), { recursive: true });
  fs.writeFileSync(path.join(app, 'HyperFrames.exe'), 'exe');
  fs.writeFileSync(path.join(app, 'resources', 'app.asar'), 'asar');
  return { dir, env, app, downloads: path.join(env.USERPROFILE, 'Downloads') };
}
const avecTar = (calls) => (cmd, args) => { calls.push(cmd); return cmd === 'tar' ? execFileSync(cmd, args) : ''; };

test('Windows : le ZIP téléchargé est rangé là où findApp la cherche, et mis au menu Démarrer', (t) => {
  const { env, downloads } = fauxWindows(t);
  execFileSync('tar', ['-a', '-cf', path.join(downloads, 'HyperFrames-win-x64.zip'), DOSSIER_WIN], { cwd: path.join(path.dirname(downloads), '..', 'zip') });
  assert.deepEqual(sourceWindows(downloads, { p: path }), { zip: path.join(downloads, 'HyperFrames-win-x64.zip') });
  const calls = [];
  const res = installerWindows({ env, p: path, run: avecTar(calls) });
  assert.equal(res.exe, path.join(env.LOCALAPPDATA, 'Programs', 'HyperFrames', 'HyperFrames.exe'));
  assert.ok(fs.existsSync(res.exe));
  assert.ok(fs.existsSync(path.join(env.LOCALAPPDATA, 'Programs', 'HyperFrames', 'resources', 'app.asar')));
  assert.ok(!fs.existsSync(path.join(env.LOCALAPPDATA, 'Programs', 'HyperFrames.nouvelle')), 'rien de provisoire ne reste');
  assert.deepEqual(calls, ['tar', 'powershell']);
  assert.match(res.raccourci, /Start Menu[\\/]Programs[\\/]HyperFrames\.lnk$/);
  // Refaire remplace l'app rangée, sans doublon.
  installerWindows({ env, p: path, run: avecTar([]) });
  assert.deepEqual(fs.readdirSync(path.join(env.LOCALAPPDATA, 'Programs')), ['HyperFrames']);
});

test('Windows : un dossier déjà décompressé par « Extraire tout » est pris tel quel', (t) => {
  const { env, app, downloads } = fauxWindows(t);
  fs.cpSync(app, path.join(downloads, 'HyperFrames-win-x64', DOSSIER_WIN), { recursive: true });
  assert.deepEqual(sourceWindows(downloads, { p: path }), { dossier: path.join(downloads, 'HyperFrames-win-x64', DOSSIER_WIN) });
  const calls = [];
  const res = installerWindows({ env, p: path, run: avecTar(calls) });
  assert.ok(fs.existsSync(res.exe));
  assert.deepEqual(calls, ['powershell'], 'rien à décompresser');
  assert.ok(fs.existsSync(path.join(downloads, 'HyperFrames-win-x64', DOSSIER_WIN, 'HyperFrames.exe')), 'Téléchargements reste intact');
});

test('Windows : un ZIP sans l’app nomme le bon chemin (antislash compris)', (t) => {
  const { env, downloads, dir } = fauxWindows(t);
  fs.mkdirSync(path.join(dir, 'autre', 'rien'), { recursive: true });
  fs.writeFileSync(path.join(dir, 'autre', 'rien', 'x.txt'), 'x');
  execFileSync('tar', ['-a', '-cf', path.join(downloads, 'HyperFrames-win-x64.zip'), 'rien'], { cwd: path.join(dir, 'autre') });
  assert.throws(() => installerWindows({ env, p: path, run: avecTar([]) }),
    (e) => e.message.includes(`ne contient pas ${DOSSIER_WIN}\\HyperFrames.exe`));
});

test('Windows : rien de téléchargé, ou un raccourci impossible, se dit sans casser', (t) => {
  const { env } = fauxWindows(t);
  assert.throws(() => installerWindows({ env, p: path, run: () => '' }), /aucun HyperFrames-win-x64\.zip/);
  assert.throws(() => installerWindows({ env: {}, p: path }), /LOCALAPPDATA/);
  const { env: env2, app, downloads } = fauxWindows(t);
  fs.cpSync(app, path.join(downloads, DOSSIER_WIN), { recursive: true });
  const res = installerWindows({ env: env2, p: path, run: (cmd) => { if (cmd === 'powershell') throw new Error('pas de COM'); return ''; } });
  assert.ok(fs.existsSync(res.exe));
  assert.equal(res.raccourci, null);
});
