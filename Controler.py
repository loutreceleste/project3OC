from View import AllView
from Modele import PlayersInformations


class MainMenu(AllView):
    def __init__(self):
        AllView.main_menu()
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


class PlayerMenu(AllView):
    def __init__(self):
        AllView.player_menu()
        user_choice = input("Votre choix: ")
        self.choice_player_menu(user_choice)

    def choice_player_menu(self, user_choice):
        if user_choice == "1":
            PlayersInformations()
        elif user_choice == "2":
            MainMenu()
        else:
            print("Erreur de saisie")
            self.__init__()


class TournamentMenu(AllView):
    def __init__(self):
        AllView.tournament_menu()
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
