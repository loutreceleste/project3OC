from view.principal import AllViewMenu


class MainMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.main_menu()
        user_choice = AllViewMenu.choise()
        self.choice_main_menu(user_choice)

    def choice_main_menu(self, user_choice):

        from controler.player import PlayerMenu
        from controler.tournament import TournamentMenu

        if user_choice == "1":
            PlayerMenu()

        elif user_choice == "2":
            TournamentMenu()

        elif user_choice == "3":
            exit()

        else:
            AllViewMenu.input_error()
            self.__init__()
