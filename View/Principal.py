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
        print("1) Creer et initialiser un nouveau tournoi")
        print("2) Visualiser les tournois en cours")
        print("3) Finir et renseigner un round")
        print("4) Retour au menu principal")

    @staticmethod
    def erreur_de_saisie():
        print("Erreur de saisie!")

    @staticmethod
    def choise():
        choise = input("Votre choix: ")
        return choise
