from View.Principal import AllViewMenu


class MainMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.main_menu()
        user_choice = AllViewMenu.choise()
        self.choice_main_menu(user_choice)

    def choice_main_menu(self, user_choice):

        from Controler.Joueur import PlayerMenu
        from Controler.Tournois import TournamentMenu

        if user_choice == "1":
            PlayerMenu()

        elif user_choice == "2":
            TournamentMenu()

        elif user_choice == "3":
            exit()

        else:
            AllViewMenu.erreur_de_saisie()
            self.__init__()
