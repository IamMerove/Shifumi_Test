"""Petit runner de vérification sans pytest.

Ce script exécute quelques vérifications rapides (sans pytest) pour valider
les nouveaux comportements testés par `shifumi/tests/test_game.py`.
Il permet de vérifier le comportement sur une machine où pytest n'est pas installé.
"""
import sys
import random
from pathlib import Path

# Ajuster le path pour importer le package shifumi
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from shifumi.game import determine_winner, get_computer_choice


def assert_raises(exc_type, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        if isinstance(e, exc_type):
            return True
        else:
            print(f"Expected {exc_type}, got {type(e)}: {e}")
            return False
    print(f"Expected exception {exc_type} but no exception was raised")
    return False


def run():
    failures = 0

    # test_invalid_computer_input
    if not assert_raises(ValueError, determine_winner, "pierre", "invalid_choice"):
        failures += 1

    # test_get_computer_choice_monkeypatch - simulate by temporarily patching random.choice
    old_choice = random.choice
    try:
        random.choice = lambda seq: 'feuille'
        if get_computer_choice() != 'feuille':
            print('get_computer_choice did not return expected value when patched')
            failures += 1
    finally:
        random.choice = old_choice

    # test_get_computer_choice_returns_valid
    valid = {"pierre", "feuille", "ciseaux"}
    for _ in range(10):
        c = get_computer_choice()
        if c not in valid:
            print(f'Invalid choice returned: {c}')
            failures += 1
            break

    if failures == 0:
        print('Quick checks passed')
        return 0
    else:
        print(f'{failures} quick checks failed')
        return 2


if __name__ == '__main__':
    sys.exit(run())
