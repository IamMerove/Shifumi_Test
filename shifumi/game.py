import random

def get_computer_choice():
    return random.choice(["pierre", "feuille", "ciseaux"])

def determine_winner(player, computer):
    # Vérifier que les choix sont valides (DEDANS la fonction)
    valid = ["pierre", "feuille", "ciseaux"]
    
    if player not in valid:
        raise ValueError(f"Choix invalide: {player}")
    
    if computer not in valid:
        raise ValueError(f"Choix invalide: {computer}")
    
    # Ensuite le reste du code
    if player == computer:
        return "Égalité"
    elif (
        (player == "pierre" and computer == "ciseaux") or
        (player == "feuille" and computer == "pierre") or
        (player == "ciseaux" and computer == "feuille")
    ):
        return "Joueur"
    else:
        return "Ordinateur"