from View.Principal import AllViewMenu
from View.Joueur import MenuPlayer
from Modele.Joueur import Player


class PlayerMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.player_menu()
        user_choice = AllViewMenu.choise()
        self.choice_player_menu(user_choice)

    def choice_player_menu(self, user_choice):

        from Controler.Principal import MainMenu

        if user_choice == "1":
            MenuPlayer.title_new_player()
            infos_joueur = MenuPlayer.player_informations()
            player = Player(*infos_joueur)
            player.insert()
            PlayerMenu()

        elif user_choice == "2":
            MenuPlayer.title_show_data()
            player = Player("", "", "", "")
            player.show_all()
            PlayerMenu()

        elif user_choice == "3":
            MainMenu()

        else:
            AllViewMenu.erreur_de_saisie()
            self.__init__()
