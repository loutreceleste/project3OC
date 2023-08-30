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

        # First part used to initiate tournament ant create duels randomly.
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
                    # Part of creating players for tounament.
                    for i in range(number_of_participants):
                        player = MenuTournament.tournament_participants()
                        players.append(player)
                    duels = [f"--ROUND 1--, Début du Round 1 le: {date_instant}"]
                    # Part of creating randoms duels.
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
                # Part of creating players for tounament.
                for i in range(number_of_participants):
                    player = MenuTournament.tournament_participants()
                    players.append(player)
                duels = [f"--ROUND 1--, Début du Round 1 le: {date_instant}"]
                # Part of creating randoms duels.
                shuffle(players)
                for i in range(0, len(players) - 1, 2):
                    duel = [players[i - 1][0], players[i][0], 0]
                    duels.append(duel)
                tournament = Tournament(*tournament_infos, players, duels)
                tournament.insert()
                TournamentMenu()

        # Part used to see all information needed.
        elif user_choice == "2":
            try:
                # Geting and printing basic information of a unique tournament.
                MenuTournament.title_tournaments()
                view.tournament.MenuTournament.show_basic_informations_tournament()
                view.principal.AllViewMenu.in_tournament_menu()
                user_choice = AllViewMenu.choise()

                # Geting and printing all information of a unique tournament.
                if user_choice == "1":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_tournament_infos(tournament_name)
                    view.tournament.MenuTournament.point_explanation()
                    view.tournament.MenuTournament.show_all_informations_tournament(tournament_name)
                    TournamentMenu()

                # Geting and printing sorted players of a unique tournament.
                elif user_choice == "2":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_players_tournament(tournament_name)
                    view.tournament.MenuTournament.get_all_sorted_tournament_players(tournament_name)
                    TournamentMenu()

                # Geting and printing sorted players of a unique tournament.
                elif user_choice == "3":
                    tournament_name = MenuTournament.tournament_name()
                    view.tournament.MenuTournament.title_duel_tournament(tournament_name)
                    view.tournament.MenuTournament.point_explanation()
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

        # Part used to inform of duels results.
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

                    # Part to inform duels.
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
                            for player in players:
                                if player[0] == winnner:
                                    player[1] += 1
                        if num == 2:
                            winnner = match[1]
                            for player in players:
                                if player[0] == winnner:
                                    player[1] += 1
                        if num == 3:
                            winnner1 = match[0]
                            winnner2 = match[1]
                            for player in players:
                                if player[0] == winnner1:
                                    player[1] += 0.5
                            for player in players:
                                if player[0] == winnner2:
                                    player[1] += 0.5

                    # Sorting the players according to their points.
                    sorted_players = sorted(players, reverse=True, key=lambda item: item[1])
                    duels = [f"Fin du Round {round_number} le: {date_instant}, --ROUND {round_number + 1}--, "
                             f"Début du Round {round_number + 1} le: {date_instant}"]

                    # Part of creating new duels which have not yet been played.
                    i = 0
                    while i < len(sorted_players) - 1:
                        # We notice that we don't have found a unique duel already.
                        unique_duel_found = False

                        for j in range(i + 1, len(sorted_players)):
                            # Create a random duel for start.
                            new_duel = [sorted_players[i][0], sorted_players[j][0], 0]
                            # Will ask the database if the duel is already done or not.
                            duel_already_done = any(
                                (new_duel[:2] == match[:2] or new_duel[:2] == match[1::-1]) for match in all_matches)

                            # If duel not already done it will remouve the players and append the new duel in the list.
                            if not duel_already_done:
                                duels.append(new_duel)
                                sorted_players.pop(j)
                                sorted_players.pop(i)
                                # Change unique_duel_found in True to stop the precesus and switch to next duel.
                                unique_duel_found = True
                                break

                        # If no unique duel found it will force to make a duel no matter if it already donne or not.
                        if not unique_duel_found:
                            forced_duel = [sorted_players[i][0], sorted_players[i + 1][0], 0]
                            duels.append(forced_duel)
                            sorted_players.pop(i + 1)
                            sorted_players.pop(i)

                    # The first one is going to be empty.
                    sorted_players2 = sorted(players, reverse=True, key=lambda item: item[1])

                    for tournament_id, tournament_data in data["_default"].items():
                        if tournament_data["Nom"] == tournament_name:
                            tournament_data["Liste des tours"][-players_half:] = last_matches
                            tournament_data["Joueurs"] = sorted_players2
                            tournament_data["Liste des tours"] += duels
                            tournament_data["Numéro de tour"] += 1
                    modele.tournament.Tournament.write_in_database_tournament(data)
                    TournamentMenu()

                # At this lap number we ask not to generate others duels as we are at the end of the tournament.
                elif lap_number is not None and lap_number == 4:
                    last_matches = Tournament.get_lasts_tournament_matchs(tournament_name)
                    players = Tournament.get_all_tournament_players(tournament_name)
                    view.tournament.MenuTournament.title_round_4()
                    view.tournament.MenuTournament.point_explanation()
                    date_instant = modele.tournament.Tournament.date_time_now()

                    # Part to inform duels.
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
                            for player in players:
                                if player[0] == winnner:
                                    player[1] += 1
                        if num == 2:
                            winnner = match[1]
                            for player in players:
                                if player[0] == winnner:
                                    player[1] += 1
                        if num == 3:
                            winnner1 = match[0]
                            winnner2 = match[1]
                            for player in players:
                                if player[0] == winnner1:
                                    player[1] += 0.5
                            for player in players:
                                if player[0] == winnner2:
                                    player[1] += 0.5

                    # Sorting the players according to their points.
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

                # At this lap number we affirm that the tournament is finish.
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
