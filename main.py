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
    compteur = 0

    #while (compteur <= len(code_secret)):


    for i in range(len(code_secret) ):
             if guess[i] == copie[i] and len(list_guess) < len(copie):
                list_guess.append("!")
                copie[i] = ""

             elif guess[i] in copie and len(list_guess) < len(copie):
                 list_guess.append("?")

    for j in range(len(list_guess)):

              if guess[j] not in copie and list_guess[j] != "!":
                  list_guess[j] = ""

    for c in list_guess:
         if c == "":
          list_guess.remove(c)

    for k in list_guess:
         if k == "":
          list_guess.remove(k)


    return guess, list_guess


def main():
    code_length = 4
    max_attempts = 1000
    jouer = 'P'
    quitter = 'Q'
    credit = 'C'

    secret_code = generateur_code_secret(code_length)
    print (secret_code)
    resultat = (''.join(map(str, secret_code)))
    print(resultat)
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

            if guess.upper() == resultat:
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
