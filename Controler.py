import json

import View
from View import AllViewMenu
from View import MenuPlayer
from Modele import Player, Tournament
from random import shuffle


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
            View.AllViewMenu.erreur_de_saisie()
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
                print("-----NOUVEAU JOUEUR-----")
                infos_joueur = MenuPlayer.player_informations()
                player = Player(*infos_joueur)
                player.insert()
            PlayerMenu()
        elif user_choice == "2":
            print("-----DATA BASE-----")
            player = Player("", "", "", "", "")
            player.show_all()
            PlayerMenu()
        elif user_choice == "3":
            MainMenu()
        else:
            View.AllViewMenu.erreur_de_saisie()
            self.__init__()


class TournamentMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.tournament_menu()
        user_choice = input("Votre choix: ")
        self.choice_tournament_menu(user_choice)

    def choice_tournament_menu(self, user_choice):
        if user_choice == "1":
            print("-----NOUVEAU TOURNOIS-----")
            infos_tournois = View.MenuTournament.tournament_informations()
            nombre_de_participants = View.MenuPlayer.nombre_de_joueurs()
            joueurs = []
            for i in range(nombre_de_participants):
                joueur = View.MenuTournament.participants_tournois()
                joueurs.append(joueur)
            tournament = Tournament(*infos_tournois, joueurs)
            tournament.insert()
            TournamentMenu()
        elif user_choice == "2":
            print("-----LES TOURNOIS EN COURS-----")
            tournament = Tournament("", "", "", "", "", "", "")
            tournament.show_all()
            TournamentsMatch()
        elif user_choice == "3":
            MainMenu()
        else:
            View.AllViewMenu.erreur_de_saisie()
            self.__init__()


class TournamentsMatch:

    def __init__(self):
        AllViewMenu.match_menu()
        user_choice = input("Votre choix: ")
        self.choice_tournament_match(user_choice)

    def choice_tournament_match(self, user_choise):
        if user_choise == "1":
            tournoi = MenuPlayer.nom_tournois()
            joueurs = Tournament.get_tournament_players(tournoi)
            date = input("Date et heure de debut : ")
            numero_round = int(input("Numero du Round: "))
            duels = [f'Round {numero_round}', date]
            shuffle(joueurs)
            for i in range(1, len(joueurs), 2):
                duels.append((joueurs[i - 1], 'vs', joueurs[i]))
            with open('databasetournament.json', 'r') as fichier:
                donnees = json.load(fichier)
                donnees["Liste des tours"] = []
                donnees["Liste des tours"].append(duels)
            with open('databasetournament.json', 'w') as fichier:
                json.dump(donnees, fichier)
            TournamentMenu()
        elif user_choise == "2":
            TournamentMenu()
        elif user_choise == "3":
            MainMenu()
        else:
            View.AllViewMenu.erreur_de_saisie()
            self.__init__()
