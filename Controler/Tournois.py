import Modele.Tournois
import View.Tournois
from View.Principal import AllViewMenu
from View.Joueur import MenuPlayer
from View.Tournois import MenuTournament
from Modele.Tournois import Tournament
from Controler.Principal import MainMenu
from random import shuffle
import json


class TournamentMenu(AllViewMenu):
    def __init__(self):
        AllViewMenu.tournament_menu()
        user_choice = AllViewMenu.choise()
        self.choice_tournament_menu(user_choice)

    def choice_tournament_menu(self, user_choice):

        if user_choice == "1":
            MenuTournament.titre_new_tournament()
            infos_tournois = MenuTournament.tournament_informations()
            try:
                tournament_data = Modele.Tournois.Tournament.read_in_database_tournament()
                nom_tournoi_data = infos_tournois[0]
                noms_tournois_json = [tournoi["Nom"] for tournoi in tournament_data["_default"].values()]
                if nom_tournoi_data not in noms_tournois_json:
                    date_debut = View.Tournois.MenuTournament.start_date_round_1()
                    nombre_de_participants = MenuPlayer.nombre_de_joueurs()
                    joueurs = []
                    for i in range(nombre_de_participants):
                        joueur = MenuTournament.participants_tournois()
                        joueurs.append(joueur)
                    duels = [f"--ROUND 1--, Debut du Round 1 le:{date_debut}"]
                    shuffle(joueurs)
                    for i in range(0, len(joueurs) - 1, 2):
                        duel = [joueurs[i - 1][0], joueurs[i][0], 0]
                        duels.append(duel)
                    tournament = Tournament(*infos_tournois, joueurs, duels)
                    tournament.insert()
                    TournamentMenu()
                else:
                    View.Tournois.MenuTournament.tournament_allready_exist()
                    TournamentMenu()
            except json.JSONDecodeError:
                date_debut = View.Tournois.MenuTournament.start_date_round_1()
                nombre_de_participants = MenuPlayer.nombre_de_joueurs()
                joueurs = []
                for i in range(nombre_de_participants):
                    joueur = MenuTournament.participants_tournois()
                    joueurs.append(joueur)
                duels = [f"--ROUND 1--, Debut du Round 1 le: {date_debut}"]
                shuffle(joueurs)
                for i in range(0, len(joueurs) - 1, 2):
                    duel = [joueurs[i - 1][0], joueurs[i][0], 0]
                    duels.append(duel)
                tournament = Tournament(*infos_tournois, joueurs, duels)
                tournament.insert()
                TournamentMenu()

        elif user_choice == "2":
            MenuTournament.titre_acual_tournament()
            tournament = Tournament("", "", "", "",
                                    "", "", "", "")
            View.Tournois.MenuTournament.point_explanation()
            tournament.show_all_informations()
            TournamentMenu()

        elif user_choice == "3":
            MenuTournament.titre_end_round()
            tournoi = MenuPlayer.nom_tournois()
            joueurs = Tournament.get_all_tournament_players(tournoi)
            last_matches = Tournament.get_lasts_tournament_matchs(tournoi)
            all_matches = Tournament.get_all_tournament_matchs(tournoi)
            players_half = Tournament.get_half_tournament_players()
            numero_tour = Tournament.get_number_of_round(tournoi)

            if numero_tour is not None and 1 <= numero_tour <= 3:
                data = Modele.Tournois.Tournament.read_in_database_tournament()
                numero_round = numero_tour
                View.Tournois.MenuTournament.title_round_result(numero_round)
                View.Tournois.MenuTournament.point_explanation()
                date_fin = View.Tournois.MenuTournament.end_round_date(numero_round)

                for match in last_matches:
                        print(match)
                        while True:
                            resultat = View.Tournois.MenuTournament.input_result_duels()
                            try:
                                num = int(resultat)
                                if 1 <= num <= 3:
                                    break
                                else:
                                    View.Tournois.MenuTournament.error_scoring()
                            except ValueError:
                                View.Tournois.MenuTournament.error_scoring()
                        match[-1] = num
                        if num == 1:
                            winnner = match[0]
                            for joueur in joueurs:
                                if joueur[0] == winnner:
                                    joueur[1] += 1
                        if num == 2:
                            winnner = match[1]
                            for joueur in joueurs:
                                if joueur[0] == winnner:
                                    joueur[1] += 1
                        if num == 3:
                            winnner1 = match[0]
                            winnner2 = match[1]
                            for joueur in joueurs:
                                if joueur[0] == winnner1:
                                    joueur[1] += 0.5
                            for joueur in joueurs:
                                if joueur[0] == winnner2:
                                    joueur[1] += 0.5


                sorted_players = sorted(joueurs, reverse=True, key=lambda item: item[1])
                date_debut = View.Tournois.MenuTournament.start_round_date(numero_round)
                duels = [f"Fin du Round {numero_round} le: {date_fin}, --ROUND {numero_round + 1}--, "
                         f"Debut du Round {numero_round + 1} le: {date_debut}"]

                i = 0
                while i < len(joueurs) - 1:
                    unique_duel_found = False

                    for j in range(i + 1, len(joueurs)):
                        new_duel = [joueurs[i][0], joueurs[j][0], 0]
                        duel_already_done = any(
                            (new_duel[:2] == match[:2] or new_duel[:2] == match[1::-1]) for match in all_matches)

                        if not duel_already_done:
                            duels.append(new_duel)
                            joueurs.pop(j)
                            joueurs.pop(i)
                            unique_duel_found = True
                            break

                    if not unique_duel_found:
                        forced_duel = [joueurs[i][0], joueurs[i + 1][0], 0]
                        duels.append(forced_duel)
                        joueurs.pop(i + 1)
                        joueurs.pop(i)

                for tournament_id, tournament_data in data["_default"].items():
                    if tournament_data["Nom"] == tournoi:
                        tournament_data["Liste des tours"][-players_half:] = last_matches
                        tournament_data["Joueurs"] = sorted_players
                        tournament_data["Liste des tours"] += duels
                        tournament_data["Numero de tour"] += 1
                Modele.Tournois.Tournament.write_in_database_tournament(data)
                TournamentMenu()

            elif numero_tour is not None and numero_tour == 4:
                last_matches = Tournament.get_lasts_tournament_matchs(tournoi)
                joueurs = Tournament.get_all_tournament_players(tournoi)
                View.Tournois.MenuTournament.title_round_4()
                View.Tournois.MenuTournament.point_explanation()
                date_fin = View.Tournois.MenuTournament.end_date_round_4()
                for match in last_matches:
                    print(match)
                    while True:
                        resultat = View.Tournois.MenuTournament.input_result_duels()
                        try:
                            num = int(resultat)
                            if 1 <= num <= 3:
                                break
                            else:
                                View.Tournois.MenuTournament.error_scoring()
                        except ValueError:
                            View.Tournois.MenuTournament.error_scoring()
                    match[-1] = num
                    if num == 1:
                        winnner = match[0]
                        for joueur in joueurs:
                            if joueur[0] == winnner:
                                joueur[1] += 1
                    if num == 2:
                        winnner = match[1]
                        for joueur in joueurs:
                            if joueur[0] == winnner:
                                joueur[1] += 1
                    if num == 3:
                        winnner1 = match[0]
                        winnner2 = match[1]
                        for joueur in joueurs:
                            if joueur[0] == winnner1:
                                joueur[1] += 0.5
                        for joueur in joueurs:
                            if joueur[0] == winnner2:
                                joueur[1] += 0.5

                sorted_players = sorted(joueurs, reverse=True, key=lambda item: item[1])

                data = Modele.Tournois.Tournament.read_in_database_tournament()
                for tournament_id, tournament_data in data["_default"].items():
                    if tournament_data["Nom"] == tournoi:
                        tournament_data["Liste des tours"][-players_half:] = [f"{last_matches}, "
                                                                              f"Fin du Round 4 le: {date_fin}"]
                        tournament_data["Joueurs"] = sorted_players
                        tournament_data["Numero de tour"] = 0
                Modele.Tournois.Tournament.write_in_database_tournament(data)
                TournamentMenu()

            elif numero_tour == 0:
                View.Tournois.MenuTournament.tournament_finish()
                TournamentMenu()

            else:
                View.Tournois.MenuTournament.tournament_does_not_exist()
                TournamentMenu()

        elif user_choice == "4":
            MainMenu()

        else:
            AllViewMenu.erreur_de_saisie()
            self.__init__()
