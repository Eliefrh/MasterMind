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
    list_guess = []
    copie = code_secret.copy()

    for i in range(len(code_secret)):
        print(copie)
        if guess[i] == copie[i]:
           list_guess.append("!")
           copie[i] ==" "
        continue

        if guess[i] != code_secret[i] and guess[i] in copie[i] :
            list_guess.append("?")


        if guess[i] not in copie[i]:
            list_guess.append(" ")


        # vrai = False
        # if guess[i] == code_secret[i]:
        #     list_guess.append("!")
        #     vrai = True
        #
        # if guess[i] in code_secret and vrai == False:
        #
        #         list_guess.append("?")
        #
        #
        # if guess[i] not in code_secret :
        #     list_guess.append(" ")




    # for i in range(len(code_secret)):
    #     if  guess[i] not in code_secret and len(list_guess) != len(guess):
    #         list_guess.append(" ")
    #     if guess[i] == code_secret[i] and len(list_guess) != len(guess):
    #      #bonne_position_couleur += 1
    #         list_guess.append("!")
    #
    #
    #     if guess[i] in code_secret and len(list_guess) != len(guess) : list_guess.append("?")




        # if guess[i] in code_secret:
        #
        #     bonne_couleur_mauvaise_position += 1
        #     list_guess.append("?")
        # else :
        #     list_guess.append(" ")


    return guess, list_guess
           #bonne_position_couleur * "!", bonne_couleur_mauvaise_position * "?"


def main():
    code_length = 4
    max_attempts = 1000
    jouer = 'P'
    quitter = 'Q'
    credit = 'C'

    secret_code = generateur_code_secret(code_length)
    print (secret_code)
    print_color(titre, Fore.RED)

    reponse = input(
        "Choisissez " + '\033[92m' + f"{jouer}" + '\033[0m' + " pour jouer, " + '\033[92m' + f"{quitter}" + '\033[0m'
        + " pour quitter et " + '\033[92m' + f"{credit}" + '\033[0m' + " pour les crédits : \n>>>")


    if reponse.upper() == jouer:
        for attempt in range(1, max_attempts + 1):
            guess = input("Entrez votre supposition : \n>>> ").upper()

            if len(guess) != code_length or any(color not in 'RGBYCP' for color in guess):
                print("supposition invalide. SVP entrez un code valide.")
                continue

            exact_matches, color_matches = evaluate_guess(secret_code, guess)


            if exact_matches == secret_code:
                print(f"félicitations! Vous avez deviné le code {secret_code} correctly")
                break
            else:
                print(f" {exact_matches}, {color_matches}")


    if reponse.upper() == credit:
        print("Nom de l'équipe : AntiBug \nKhalil, Elie et Dina")
        main()

    if reponse.upper() == quitter:
        sys.exit()





if __name__ == "__main__":
    main()
