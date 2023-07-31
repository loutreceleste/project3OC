class AllViewMenu:

    @staticmethod
    def main_menu():
        print("-----MENU PRINCIPAL-----")
        print("1) Menu Joueurs")
        print("2) Menu Tournoi")
        print("3) Quitter le programme")

    @staticmethod
    def player_menu():
        print("-----MENU JOUEURS-----")
        print("1) Informations des joueurs")
        print("2) Visualiser la liste des joueurs")
        print("3) Retour au menu principal")

    @staticmethod
    def tournament_menu():
        print("-----MENU TOURNOI-----")
        print("1) Creer un nouveau tournoi")
        print("2) Visualiser les tournois")
        print("3) Retour au menu principal")

    @staticmethod
    def match_menu():
        print("-----MENU DES TOURNOIS-----")
        print("1) Generer les matchs")
        print("2) Retour au menu Tournois")
        print("3) Retour au menu principal")

    @staticmethod
    def erreur_de_saisie():
        print("Erreur de saisie!")


class MenuTournament:

    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques):
        print("-----INFORMATIONS DU TOURNOIS-----")
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombre_tours = nombre_tours
        self.numero_tours = numero_tour
        self.remarques = remarques

    @staticmethod
    def tournament_informations():
        nom = input("Nom du tournois: ")
        lieu = input("Lieu du tournois: ")
        dates = input("Dates du tournois: ")
        nombre_tours = 0
        numero_tour = input("Numero du tour: ")
        remarques = input("Remarques du directeur: ")
        return nom, lieu, dates, nombre_tours, numero_tour, remarques

    @staticmethod
    def participants_tournois():
        numero_ine = input("Numero INE du joueur: ")
        while True:
            try:
                score = int(input("Votre score: "))
                return numero_ine, score
            except ValueError:
                print("Veuillez saisir un chiffre!")


class MenuPlayer:

    def __init__(self, nom, prenom, date, ine, score):
        print("-----INFORMATIONS DES JOUEURS-----")
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine
        self.score = score

    @staticmethod
    def player_informations():
        nom = input("Votre nom: ")
        prenom = input("Votre prenom: ")
        date = input("Votre date de naissance (format AAAA-MM-JJ): ")
        ine = input("Votre INE: ")
        score = input("Votre score initial: ")
        return nom, prenom, date, ine, score

    @staticmethod
    def nombre_de_joueurs():
        while True:
            try:
                nombre_de_joueurs = int(input("Nombre de participants au tournois: "))
                return nombre_de_joueurs
            except ValueError:
                print("Veuillez saisir un chiffre!")

    @staticmethod
    def nom_tournois():
        nom_tournoi = input("Entrez le nom du tournoi : ")
        return nom_tournoi
