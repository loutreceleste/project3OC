from view.principal import AllViewMenu
from view.player import MenuPlayer
from modele.player import Player


class PlayerMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.player_menu()
        user_choice = AllViewMenu.choise()
        self.choice_player_menu(user_choice)

    def choice_player_menu(self, user_choice):

        from controler.principal import MainMenu

        if user_choice == "1":
            MenuPlayer.title_new_player()
            player = Player(*MenuPlayer.player_informations())
            player.insert()
            PlayerMenu()

        elif user_choice == "2":
            MenuPlayer.title_show_data_player()
            player = Player("", "", "", "")
            player.show_all()
            PlayerMenu()

        elif user_choice == "3":
            MainMenu()

        else:
            AllViewMenu.input_error()
            self.__init__()
