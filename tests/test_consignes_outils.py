"""Les consignes et les outils se tiennent : chaque `studio_motion.py <commande> --option` cité dans le
skill, les gabarits d'instructions, INSTALL.md et README.md existe dans le parseur de l'outil, et
chaque `app-hyperframes.mjs <commande>` existe dans le script.

Né de la revue du 09/11/2026 : 186 appels sur 221 concordaient, les autres citaient une option ou une
action que l'outil n'avait pas (ou plus). Une IA qui suit la consigne tombait alors sur une erreur
d'argparse, sans savoir quoi faire.

Lancer : python3 -m unittest discover -s tests
"""
from __future__ import annotations

import argparse
import bisect
import re
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "tools"))

import studio_motion as sm  # noqa: E402


def fichiers_de_consignes() -> list[Path]:
    skill = RACINE / ".claude" / "skills" / "studio"
    return sorted(
        [*skill.rglob("*.md"), *(RACINE / "templates").glob("*.tpl"), *(RACINE / "templates" / "projet").glob("*.tpl"),
         RACINE / "INSTALL.md", RACINE / "README.md"])


def morceaux(texte: str) -> list[tuple[int, str]]:
    """(ligne, texte) de chaque ligne d'un bloc de code et de chaque `code en ligne` (même coupé par un
    retour à la ligne)."""
    sortie, dans_bloc = [], False
    lignes = texte.split("\n")
    for i, ligne in enumerate(lignes, 1):
        if ligne.strip().startswith("```"):
            dans_bloc = not dans_bloc
        elif dans_bloc and ligne.strip():
            sortie.append((i, ligne.strip()))
    debuts = [0]
    for ligne in lignes:
        debuts.append(debuts[-1] + len(ligne) + 1)
    hors_blocs = re.sub(r"```.*?```", lambda m: re.sub(r"[^\n]", " ", m.group(0)), texte, flags=re.S)
    for m in re.finditer(r"`([^`\n]+(?:\n[^`\n]+)?)`", hors_blocs):
        sortie.append((bisect.bisect_right(debuts, m.start()), re.sub(r"\s+", " ", m.group(1)).strip()))
    return sortie


def sous_commandes(p: argparse.ArgumentParser) -> dict[str, argparse.ArgumentParser]:
    action = next(a for a in p._actions if isinstance(a, argparse._SubParsersAction))
    return dict(action.choices)


def premiere_position(p: argparse.ArgumentParser) -> argparse.Action | None:
    """Le premier argument de position d'une commande (son action : `musiques prendre`, `voix caler`)."""
    return next((a for a in p._actions if not a.option_strings and a.dest != "help"), None)


OPTION = re.compile(r"(?<![\w/-])--[a-z][a-z0-9-]*")


def ecarts_studio_motion() -> list[str]:
    commandes = sous_commandes(sm.parseur())
    return [e for f in fichiers_de_consignes()
            for e in ecarts_dans(f.relative_to(RACINE), f.read_text(encoding="utf-8"), commandes)]


def ecarts_dans(nom, texte: str, commandes: dict[str, argparse.ArgumentParser]) -> list[str]:
    """Les appels de studio_motion.py de `texte` que le parseur ne connaît pas (commande, option, action)."""
    ecarts = []
    for ligne, s in morceaux(texte):
        s = s.replace("’", "'")
        m = re.search(r"studio_motion\.py\s+([a-z][a-z-]*)(.*)", s)
        explicite = m is not None
        if not m:
            # La forme courte du texte, « `musiques prendre --a` », « `mastering … --cible -20` » : seules
            # ses options se vérifient (« voix off », « style 3 » ne sont pas des commandes).
            m = re.match(r"([a-z][a-z-]*)(\s.*)$", s)
            if not m or m.group(1) not in commandes or not OPTION.search(m.group(2)):
                continue
        commande, reste = m.group(1), re.split(r"\s+#\s|\s+→\s", m.group(2))[0]
        if commande not in commandes:
            ecarts.append(f"{nom}:{ligne} : `{commande}` n'est pas une commande de studio_motion.py ({s})")
            continue
        sous = commandes[commande]
        for option in OPTION.findall(reste):
            if option not in sous._option_string_actions:
                ecarts.append(f"{nom}:{ligne} : `{commande} {option}` n'existe pas dans studio_motion.py ({s})")
        # L'action citée (`musiques prendre`, `heygen connecter`) : parmi celles de la commande.
        position = premiere_position(sous)
        mot = (reste.split() or [""])[0]
        if explicite and position is not None and position.choices and re.fullmatch(r"[a-z][a-z-]*", mot) \
                and mot not in position.choices:
            ecarts.append(f"{nom}:{ligne} : `{commande} {mot}` n'est pas une action de studio_motion.py "
                          f"({', '.join(position.choices)}) ({s})")
    return ecarts


def ecarts_app_hyperframes() -> list[str]:
    script = (RACINE / "scripts" / "app-hyperframes.mjs").read_text(encoding="utf-8")
    connues = set(re.findall(r'command === "([a-z-]+)"', script))
    ecarts = []
    for f in fichiers_de_consignes():
        nom = f.relative_to(RACINE)
        for ligne, s in morceaux(f.read_text(encoding="utf-8")):
            for commande in re.findall(r"app-hyperframes\.mjs\s+([a-z][a-z-]*)", s):
                if commande not in connues:
                    ecarts.append(f"{nom}:{ligne} : `app-hyperframes.mjs {commande}` n'existe pas ({s})")
    return ecarts


class ConsignesEtOutils(unittest.TestCase):
    def test_l_extraction_trouve_les_appels(self):
        """Le test ne passe pas à vide : les consignes citent bien des dizaines d'appels."""
        appels = [s for f in fichiers_de_consignes() for _l, s in morceaux(f.read_text(encoding="utf-8"))
                  if "studio_motion.py " in s]
        self.assertGreater(len(appels), 50)
        self.assertIn("musiques", sous_commandes(sm.parseur()))

    def test_l_extraction_repere_les_ecarts(self):
        texte = ("Lance `python3 tools/studio_motion.py planche x.mp4 --inexistante`, puis\n"
                 "```bash\npython3 ../../../tools/studio_motion.py musiques prendre 2 --a 8   # --pas-vu\n```\n"
                 "et `mastering … --cible -20`, `son … --fort`, `python3 tools/studio_motion.py musiques piocher`,\n"
                 "`python3 tools/studio_motion.py\nmagie x`, la `voix off`, le `style 3`.")
        ecarts = ecarts_dans("essai.md", texte, sous_commandes(sm.parseur()))
        self.assertEqual(len(ecarts), 4, "\n".join(ecarts))
        for attendu in ("essai.md:1 : `planche --inexistante`", "essai.md:5 : `son --fort`",
                        "essai.md:5 : `musiques piocher` n'est pas une action", "essai.md:6 : `magie` n'est pas une commande"):
            self.assertTrue(any(e.startswith(attendu) for e in ecarts), (attendu, ecarts))

    def test_chaque_option_citee_existe(self):
        ecarts = ecarts_studio_motion()
        self.assertEqual(ecarts, [], "\n" + "\n".join(ecarts))

    def test_chaque_commande_de_l_app_citee_existe(self):
        ecarts = ecarts_app_hyperframes()
        self.assertEqual(ecarts, [], "\n" + "\n".join(ecarts))


if __name__ == "__main__":
    unittest.main()
