class AllViewMenu:

    @staticmethod
    def main_menu():
        print()
        print("-----MENU PRINCIPAL-----")
        print("1) Menu Joueurs")
        print("2) Menu Tournoi")
        print("3) Quitter le programme")

    @staticmethod
    def player_menu():
        print()
        print("-----MENU JOUEUR-----")
        print("1) Renseigner un nouveau joueur")
        print("2) Affichage la liste des joueurs")
        print("3) Retour au Menu Principal")

    @staticmethod
    def tournament_menu():
        print()
        print("-----MENU TOURNOI-----")
        print("1) Creer et initialiser un nouveau tournoi")
        print("2) Visualiser les tournois en cours")
        print("3) Finir et renseigner un round")
        print("4) Retour au Menu Principal")

    @staticmethod
    def in_tournament_menu():
        print()
        print("--Informations complementaires--")
        print("1) Obtenir toutes les informations sur un tournoi.")
        print("2) Liste des participants par ordre alphabetique.")
        print("3) Liste de tous les tours du tournoi et de tous les matchs du tour.")
        print("4) Revenir au Menu Tournoi.")

    @staticmethod
    def erreur_de_saisie():
        print("Erreur de saisie!")

    @staticmethod
    def choise():
        choise = input("Votre choix: ")
        return choise
