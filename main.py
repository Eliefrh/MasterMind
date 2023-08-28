import random
import sys
from colorama import init, Fore

init(autoreset=True)


def print_color(text, color):
    print(color + text)


titre = """
  ████   ███    ██  ██████  ██████ ██████  ██  ██ ████████
██   ██ ██ ██   ██    ██      ██   ██   ██ ██  ██ ██
███████ ██  ██  ██    ██      ██   ██████  ██  ██ ██   ███
██   ██ ██   ██ ██    ██      ██   ██   ██ ██  ██ ██    ██
██   ██ ██    ███     ██    ██████ ██████  ██████ ████████
"""


def generateur_code_secret(longueur):
    couleurs = ['R', 'G', 'B', 'Y', 'C', 'P']  # Replace with your desired color options
    code_secret = random.choices(couleurs, k=longueur)
    return code_secret


def evaluate_guess(code_secret, guess):
    bonne_position_couleur = 0
    bonne_couleur_mauvaise_position = 0

    for i in range(len(code_secret)):
        if guess[i] == code_secret[i]:
            bonne_position_couleur += 1
        elif guess[i] in code_secret:
            bonne_couleur_mauvaise_position += 1

    return bonne_position_couleur, bonne_couleur_mauvaise_position


def main():
    code_length = 4  # You can adjust the length of the secret code
    max_attempts = 1000  # You can adjust the maximum number of attempts
    jouer = 'P'
    quitter = 'Q'
    credit = 'C'

    secret_code = generateur_code_secret(code_length)
    print_color(titre, Fore.RED)

    reponse = input(
        "Choisissez " + '\033[92m' + f"{jouer}" + '\033[0m' + " pour jouer, " + '\033[92m' + f"{quitter}" + '\033[0m'
        + " pour quitter et " + '\033[92m' + f"{credit}" + '\033[0m' + " pour les crédits : \n")

    if reponse.upper() == jouer:
        for attempt in range(1, max_attempts + 1):
            guess = input("Entrez votre supposition : ").upper()

            if len(guess) != code_length or any(color not in 'RGBYCP' for color in guess):
                print("Invalid guess. Please enter a valid code.")
                continue

            exact_matches, color_matches = evaluate_guess(secret_code, guess)

            if exact_matches == code_length:
                print(f"Congratulations! You guessed the code {secret_code} correctly")
                break
            else:
                print(f"Exact matches: {exact_matches}, Color matches: {color_matches}")

            if attempt == max_attempts:
                print(f"Sorry, you've run out of attempts. The secret code was {secret_code}.")

    if reponse.upper() == credit:
        print(f"[!!??]")

    if reponse.upper() == quitter:
        sys.exit()
    else :
        main()




if __name__ == "__main__":
    main()
