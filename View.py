class AllViewMenu:

    @staticmethod
    def main_menu():
        print("MENU PRINCIPAL")
        print("1) Menu Joueurs")
        print("2) Menu Tournoi")
        print("3) Quitter le programme")

    @staticmethod
    def player_menu():
        print("MENU JOUEURS")
        print("1) Informations des joueurs")
        print("2) Retour au menu principal")

    @staticmethod
    def tournament_menu():
        print("MENU TOURNOI")
        print("1) Informations du tournoi")
        print("2) Retour au menu principal")


class MenuPlayer:

    def __init__(self, nom, prenom, date, ine, score):
        print("INFORMATIONS DES JOUEURS")
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine
        self.score = score

    @staticmethod
    def player_informations():
        nom = input("Votre nom : ")
        prenom = input("Votre prenom: ")
        date = input("Votre date de naissance (format AAAA-MM-JJ): ")
        ine = input("Votre INE: ")
        score = input("Votre score initial: ")
        return nom, prenom, date, ine, score

    @staticmethod
    def nombre_de_joueurs():
        nombre_de_joueurs = int(input("Nombre de participants au tournois: "))
        return nombre_de_joueurs
