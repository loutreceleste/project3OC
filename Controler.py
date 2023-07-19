from View import AllViewMenu
from View import MenuPlayer
from Modele import Player


class MainMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.main_menu()
        user_choice = input("Votre choix: ")
        self.choice_main_menu(user_choice)

    def choice_main_menu(self, user_choice):
        if user_choice == "1":
            PlayerMenu()
        elif user_choice == "2":
            TournamentMenu()
        elif user_choice == "3":
            exit()
        else:
            print("Erreur de saisie!")
            self.__init__()


class PlayerMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.player_menu()
        user_choice = input("Votre choix: ")
        self.choice_player_menu(user_choice)

    def choice_player_menu(self, user_choice):
        if user_choice == "1":
            nombre_de_joueurs = MenuPlayer.nombre_de_joueurs()
            for i in range(nombre_de_joueurs):
                print("NOUVEAU JOUEUR")
                infos_joueur = MenuPlayer.player_informations()
                player = Player(*infos_joueur)
                player.insert()
        elif user_choice == "2":
            MainMenu()
        else:
            print("Erreur de saisie")
            self.__init__()


class TournamentMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.tournament_menu()
        user_choice = input("Votre choix: ")
        self.choice_tournament_menu(user_choice)

    def choice_tournament_menu(self, user_choice):
        if user_choice == "1":
            pass
        elif user_choice == "2":
            MainMenu()
        else:
            print("Erreur de saisie")
            self.__init__()


class InformationJoueur(AllViewMenu):
    def __init__(self, nom, prenom, date, ine, score):
        MenuPlayer.player_informations()
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine
        self.score = score
