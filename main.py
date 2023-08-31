import random
import sys
from colorama import init, Fore

init(autoreset=True)


def print_couleur(texte, couleur):
    print(couleur + texte)


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
    return ['R', 'B', 'B', 'R']


def evaluation_indice(code_secret, indice):
    bonne_position_couleur = []
   # bonne_couleur_mauvaise_position = []

    for i in range(len(code_secret)):
        if indice[i] == code_secret[i]:
            bonne_position_couleur.append('!')
        elif indice[i] in code_secret :
            bonne_position_couleur.append('?')            
    return bonne_position_couleur 


def main():
    longueur_code = 4  
    max_essaye = 100
    jouer = 'P'
    quitter = 'Q'
    credit = 'C'

    code_secret = generateur_code_secret(longueur_code)
    print_couleur(titre, Fore.RED)

    print(code_secret)

    reponse = input(
        "Choisissez " + '\033[92m' + f"{jouer}" + '\033[0m' + " pour jouer, " + '\033[92m' + f"{quitter}" + '\033[0m'
        + " pour quitter et " + '\033[92m' + f"{credit}" + '\033[0m' + " pour les crédits : \n>>>")


    if reponse.upper() == jouer:
        for attempt in range(1, max_essaye + 1):
            indice = input("Entrez votre supposition : \n>>> ").upper()

            if len(indice) != longueur_code or any(color not in 'RGBYCP' for color in indice):
                print("supposition invalide. SVP entrez un code valide.")
                continue

            couleur_position_exacte = evaluation_indice(code_secret, indice)


            if couleur_position_exacte == code_secret:
                print(f"félicitations! Vous avez deviné le code {code_secret} correctly")
                break
            else:
                print(f"{couleur_position_exacte}")


    if reponse.upper() == credit:
        print("Équipe : AntiBug \nLes membres: Khalil, Elie et Dina")
        main()

    if reponse.upper() == quitter:
        sys.exit()





if __name__ == "__main__":
    main()
