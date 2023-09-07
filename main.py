import random
import sys
from colorama import init, Fore
import time

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


def generer_code_secret(longueur):
    couleurs = ['R', 'G', 'B', 'Y', 'C', 'P']
    code_secret = random.choices(couleurs, k=longueur)
    return code_secret


def evaluer_indice(code_secret, indice):
    liste_indice = []
    copie = code_secret.copy()

    for i in range(len(code_secret)):
        # Vérifier si la lettre existe dans la liste et à la bonne position
        if indice[i] == copie[i] and len(liste_indice) < len(copie):
            liste_indice.append("!")
            copie[i] = ""

        # Vérifier la presence de la lettre dans la liste, mais mauvaise position
        elif indice[i] in copie and len(liste_indice) < len(copie):
            liste_indice.append("?")

    for j in range(len(liste_indice)):
        # Vérifier et effacer les caractères qui sont déjà évalués
        if indice[j] not in copie and liste_indice[j] != "!":
            liste_indice[j] = ""

        # enlever les caractères vides avant retourner evaluation
    for c in liste_indice:
        if c == "":
            liste_indice.remove(c)

    for k in liste_indice:
        if k == "":
            liste_indice.remove(k)

    return indice, liste_indice


# afficher les 3 point une après l'autre avec un delay de 0.5
def afficher_points(nbr_points, retard):
    for _ in range(nbr_points):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(retard)


def main():
    code_longueur = 4
    max_essayes = 1000
    jouer = 'P'
    quitter = 'Q'
    credit = 'C'

    code_secret = generer_code_secret(code_longueur)
    resultat = (''.join(map(str, code_secret)))
    print_color(titre, Fore.RED)

    # recevoir la réponse de l'utilisateur/e pour les options de la menue
    reponse = input(
        "Choisissez " + '\033[92m' + f"{jouer}" + '\033[0m' + " pour jouer, " + '\033[92m' + f"{quitter}" + '\033[0m'
        + " pour quitter et " + '\033[92m' + f"{credit}" + '\033[0m' + " pour les crédits : \n>>>")

    # l'option "j" est pour commencer le jeu
    if reponse.upper() == jouer:
        for essaye in range(1, max_essayes + 1):
            indice = input("Entrez votre supposition : \n>>> ").upper()

            if len(indice) != code_longueur or any(couleur not in 'RGBYCP' for couleur in indice):
                print("supposition invalide. SVP entrez un code valide.")
                continue

            bonne_couleur_position, bonne_couleur = evaluer_indice(code_secret, indice)

            if indice.upper() == resultat:
                print(f"félicitations! Vous avez deviné le code {code_secret} correctly")
                break
            else:
                print(f" {bonne_couleur_position}, {bonne_couleur}")

    # l'option "c" est pour afficher le nom de l'équipe et les membres
    if reponse.upper() == credit:
        print('\033[92m' + "Nom de l'équipe :" + '\033[0m' + "AntiBug \n" + '\033[92m' + "Les membres :"
              + '\033[0m' + " Khalil, Elie et Dina")
        main()

    # l'option "q" est pour quitter le jeu
    if reponse.upper() == quitter:
        afficher_points(3, 0.5)
        sys.exit()


if __name__ == "__main__":
    main()
