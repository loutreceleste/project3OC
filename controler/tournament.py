import modele.tournament
import view.tournament
from view.principal import AllViewMenu
from view.tournament import MenuTournament
from modele.tournament import Tournament
from controler.principal import MainMenu
from random import shuffle
import json


class TournamentMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.tournament_menu()
        user_choice = AllViewMenu.choise()
        self.choice_tournament_menu(user_choice)

    def choice_tournament_menu(self, user_choice):

        if user_choice == "1":
            MenuTournament.title_new_tournament()
            date_instant = modele.tournament.Tournament.date_time_now()
            tournament_infos = MenuTournament.tournament_informations()
            try:
                tournament_data = modele.tournament.Tournament.read_in_database_tournament()
                name_tournament_data = tournament_infos[0]
                name_tournament_json = [tournoi["Nom"] for tournoi in tournament_data["_default"].values()]
                if name_tournament_data not in name_tournament_json:
                    number_of_participants = MenuTournament.number_of_players()
                    players = []
                    for i in range(number_of_participants):
                        players = MenuTournament.tournament_participants()
                        players.append(players)
                    duels = [f"--ROUND 1--, Début du Round 1 le: {date_instant}"]
                    shuffle(players)
                    for i in range(0, len(players) - 1, 2):
                        duel = [players[i - 1][0], players[i][0], 0]
                        duels.append(duel)
                    tournament = Tournament(*tournament_infos, players, duels)
                    tournament.insert()
                    TournamentMenu()
                else:
                    view.tournament.MenuTournament.tournament_allready_exist()
                    TournamentMenu()
            except json.JSONDecodeError:
                date_instant = modele.tournament.Tournament.date_time_now()
                number_of_participants = MenuTournament.number_of_players()
                players = []
                for i in range(number_of_participants):
                    players = MenuTournament.tournament_participants()
                    players.append(players)
                duels = [f"--ROUND 1--, Début du Round 1 le: {date_instant}"]
                shuffle(players)
                for i in range(0, len(players) - 1, 2):
                    duel = [players[i - 1][0], players[i][0], 0]
                    duels.append(duel)
                tournament = Tournament(*tournament_infos, players, duels)
                tournament.insert()
                TournamentMenu()

        elif user_choice == "2":
            try:
                MenuTournament.title_tournaments()
                view.tournament.MenuTournament.show_all_informations()
                view.principal.AllViewMenu.in_tournament_menu()
                user_choice = AllViewMenu.choise()

                if user_choice == "1":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_tournament_infos(tournament_name)
                    view.tournament.MenuTournament.show_informations_tournament(tournament_name)
                    TournamentMenu()

                elif user_choice == "2":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_players_tournament(tournament_name)
                    view.tournament.MenuTournament.get_all_sorted_tournament_players(tournament_name)
                    TournamentMenu()

                elif user_choice == "3":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_duel_tournament(tournament_name)
                    view.tournament.MenuTournament.show_duel_informations(tournament_name)
                    TournamentMenu()

                elif user_choice == "4":
                    TournamentMenu()

                else:
                    view.tournament.MenuTournament.error_scoring_1_4()
                    TournamentMenu()

            except json.JSONDecodeError:
                view.tournament.MenuTournament.no_tournament()
                TournamentMenu()

        elif user_choice == "3":
            try:
                MenuTournament.title_end_round()
                tournament_name = MenuTournament.tournament_name()
                players = Tournament.get_all_tournament_players(tournament_name)
                last_matches = Tournament.get_lasts_tournament_matchs(tournament_name)
                all_matches = Tournament.get_all_tournament_matchs(tournament_name)
                players_half = Tournament.get_half_tournament_players()
                lap_number = Tournament.get_number_of_round(tournament_name)

                if lap_number is not None and 1 <= lap_number <= 3:
                    data = modele.tournament.Tournament.read_in_database_tournament()
                    round_number = lap_number
                    view.tournament.MenuTournament.title_round_result(round_number)
                    view.tournament.MenuTournament.point_explanation()
                    date_instant = modele.tournament.Tournament.date_time_now()

                    for match in last_matches:
                        print(match)
                        while True:
                            results = view.tournament.MenuTournament.input_result_duels()
                            try:
                                num = int(results)
                                if 1 <= num <= 3:
                                    break
                                else:
                                    view.tournament.MenuTournament.error_scoring_1_3()
                            except ValueError:
                                view.tournament.MenuTournament.error_scoring_1_3()
                        match[-1] = num
                        if num == 1:
                            winnner = match[0]
                            for players in players:
                                if players[0] == winnner:
                                    players[1] += 1
                        if num == 2:
                            winnner = match[1]
                            for players in players:
                                if players[0] == winnner:
                                    players[1] += 1
                        if num == 3:
                            winnner1 = match[0]
                            winnner2 = match[1]
                            for players in players:
                                if players[0] == winnner1:
                                    players[1] += 0.5
                            for players in players:
                                if players[0] == winnner2:
                                    players[1] += 0.5

                    sorted_players = sorted(players, reverse=True, key=lambda item: item[1])
                    duels = [f"Fin du Round {round_number} le: {date_instant}, --ROUND {round_number + 1}--, "
                             f"Début du Round {round_number + 1} le: {date_instant}"]

                    i = 0
                    while i < len(players) - 1:
                        unique_duel_found = False

                        for j in range(i + 1, len(players)):
                            new_duel = [players[i][0], players[j][0], 0]
                            duel_already_done = any(
                                (new_duel[:2] == match[:2] or new_duel[:2] == match[1::-1]) for match in all_matches)

                            if not duel_already_done:
                                duels.append(new_duel)
                                players.pop(j)
                                players.pop(i)
                                unique_duel_found = True
                                break

                        if not unique_duel_found:
                            forced_duel = [players[i][0], players[i + 1][0], 0]
                            duels.append(forced_duel)
                            players.pop(i + 1)
                            players.pop(i)

                    for tournament_id, tournament_data in data["_default"].items():
                        if tournament_data["Nom"] == tournament_name:
                            tournament_data["Liste des tours"][-players_half:] = last_matches
                            tournament_data["Joueurs"] = sorted_players
                            tournament_data["Liste des tours"] += duels
                            tournament_data["Numéro de tour"] += 1
                    modele.tournament.Tournament.write_in_database_tournament(data)
                    TournamentMenu()

                elif lap_number is not None and lap_number == 4:
                    last_matches = Tournament.get_lasts_tournament_matchs(tournament_name)
                    players = Tournament.get_all_tournament_players(tournament_name)
                    view.tournament.MenuTournament.title_round_4()
                    view.tournament.MenuTournament.point_explanation()
                    date_instant = modele.tournament.Tournament.date_time_now()

                    for match in last_matches:
                        print(match)
                        while True:
                            results = view.tournament.MenuTournament.input_result_duels()
                            try:
                                num = int(results)
                                if 1 <= num <= 3:
                                    break
                                else:
                                    view.tournament.MenuTournament.error_scoring_1_3()
                            except ValueError:
                                view.tournament.MenuTournament.error_scoring_1_3()
                        match[-1] = num
                        if num == 1:
                            winnner = match[0]
                            for players in players:
                                if players[0] == winnner:
                                    players[1] += 1
                        if num == 2:
                            winnner = match[1]
                            for players in players:
                                if players[0] == winnner:
                                    players[1] += 1
                        if num == 3:
                            winnner1 = match[0]
                            winnner2 = match[1]
                            for players in players:
                                if players[0] == winnner1:
                                    players[1] += 0.5
                            for players in players:
                                if players[0] == winnner2:
                                    players[1] += 0.5

                    sorted_players = sorted(players, reverse=True, key=lambda item: item[1])
                    data = modele.tournament.Tournament.read_in_database_tournament()
                    for tournament_id, tournament_data in data["_default"].items():
                        if tournament_data["Nom"] == tournament_name:
                            tournament_data["Liste des tours"][-players_half:] = [f"{last_matches}, "
                                                                                  f"Fin du Round 4 le: {date_instant}"]
                            tournament_data["Joueurs"] = sorted_players
                            tournament_data["Numéro de tour"] = 0
                    modele.tournament.Tournament.write_in_database_tournament(data)
                    TournamentMenu()

                elif lap_number == 0:
                    view.tournament.MenuTournament.tournament_finish()
                    TournamentMenu()

                else:
                    view.tournament.MenuTournament.tournament_does_not_exist()
                    TournamentMenu()

            except json.JSONDecodeError:
                view.tournament.MenuTournament.no_tournament()
                TournamentMenu()

        elif user_choice == "4":
            MainMenu()

        else:
            AllViewMenu.input_error()
            self.__init__()
