from shifumi.game import determine_winner

def test_win_conditions():
    assert determine_winner("rock", "scissors") == "win"
    assert determine_winner("paper", "rock") == "win"
    assert determine_winner("scissors", "paper") == "win"

def test_tie():
    assert determine_winner("rock", "rock") == "tie"

def test_invalid_input():
    assert determine_winner("banana", "rock") == "lose"  # à corriger
