import sys
from pathlib import Path
import pytest
import random

sys.path.insert(0, str(Path(__file__).parent.parent))

from game import determine_winner, get_computer_choice


def test_egalite():
    assert determine_winner("pierre", "pierre") == "Égalité"
    assert determine_winner("feuille", "feuille") == "Égalité"
    assert determine_winner("ciseaux", "ciseaux") == "Égalité"


def test_victoires_joueur():
    assert determine_winner("pierre", "ciseaux") == "Joueur"
    assert determine_winner("feuille", "pierre") == "Joueur"
    assert determine_winner("ciseaux", "feuille") == "Joueur"


def test_victoires_ordinateur():
    assert determine_winner("pierre", "feuille") == "Ordinateur"
    assert determine_winner("feuille", "ciseaux") == "Ordinateur"
    assert determine_winner("ciseaux", "pierre") == "Ordinateur"


# Tests pour entrées invalides
def test_invalid_input():
    """Teste une entrée invalide comme 'pierrex'"""
    with pytest.raises(ValueError):
        determine_winner("pierrex", "pierre")


def test_empty_string():
    """Teste une chaîne vide"""
    with pytest.raises(ValueError):
        determine_winner("", "pierre")


def test_invalid_both():
    """Teste deux entrées invalides"""
    with pytest.raises(ValueError):
        determine_winner("abc", "xyz")


def test_invalid_computer_input():
    """Si l'argument 'computer' est invalide, on doit lever ValueError"""
    with pytest.raises(ValueError):
        determine_winner("pierre", "invalid_choice")


def test_get_computer_choice_monkeypatch(monkeypatch):
    """Contrôler le comportement aléatoire en patchant random.choice"""
    monkeypatch.setattr(random, 'choice', lambda seq: 'feuille')
    assert get_computer_choice() == 'feuille'


def test_get_computer_choice_returns_valid():
    """S'assurer que la fonction renvoie toujours une valeur valide"""
    for _ in range(10):
        c = get_computer_choice()
        assert c in ["pierre", "feuille", "ciseaux"]