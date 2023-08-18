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
                with open('databasetournament.json', 'r') as json_file:
                    tournament_data = json.load(json_file)
                    nom_tournoi_data = infos_tournois[0]
                    noms_tournois_json = [tournoi["Nom"] for tournoi in tournament_data["_default"].values()]
                    if nom_tournoi_data not in noms_tournois_json:
                        nombre_de_participants = MenuPlayer.nombre_de_joueurs()
                        joueurs = []
                        for i in range(nombre_de_participants):
                            joueur = MenuTournament.participants_tournois()
                            joueurs.append(joueur)
                        duels = []
                        shuffle(joueurs)
                        for i in range(0, len(joueurs) - 1, 2):
                            duel = [joueurs[i - 1][0], joueurs[i][0], 0]
                            duels.append(duel)
                        tournament = Tournament(*infos_tournois, joueurs, duels)
                        tournament.insert()
                        TournamentMenu()
                    else:
                        print("Ce nom de tournois existe deja!")
                        TournamentMenu()
            except json.JSONDecodeError:
                nombre_de_participants = MenuPlayer.nombre_de_joueurs()
                joueurs = []
                for i in range(nombre_de_participants):
                    joueur = MenuTournament.participants_tournois()
                    joueurs.append(joueur)
                duels = []
                shuffle(joueurs)
                for i in range(0, len(joueurs) - 1, 2):
                    duel = [joueurs[i - 1][0], joueurs[i][0], 0]
                    duels.append(duel)
                tournament = Tournament(*infos_tournois, joueurs, duels)
                tournament.insert()
                TournamentMenu()

        elif user_choice == "2":
            print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")
            MenuTournament.titre_acual_tournament()
            tournament = Tournament("", "", "", "", "", "", "", "")
            tournament.show_all()
            TournamentMenu()

        elif user_choice == "3":
            MenuTournament.titre_end_round()
            tournoi = MenuPlayer.nom_tournois()
            joueurs = Tournament.get_tournament_players(tournoi)
            last_matches = Tournament.get_last_tournament_match(tournoi)
            all_matches = Tournament.get_all_tournament_match(tournoi)
            players_half = Tournament.get_tournament_players_half()
            numero_tour = Tournament.get_number_of_round(tournoi)

            if numero_tour is not None and numero_tour <= 3:
                with open('databasetournament.json', 'r') as json_file:
                    data = json.load(json_file)
                numero_round = numero_tour
                print(f"-----RESULTATS ROUND {numero_round}-----")
                print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")

                for match in last_matches:
                    print(match)
                    resultat = int(input('Resultat: '))
                    match[-1] = resultat
                    if resultat == 1:
                        winnner = match[0]
                        for joueur in joueurs:
                            if joueur[0] == winnner:
                                joueur[1] += 1
                    if resultat == 2:
                        winnner = match[1]
                        for joueur in joueurs:
                            if joueur[0] == winnner:
                                joueur[1] += 1
                    if resultat == 3:
                        winnner1 = match[0]
                        winnner2 = match[1]
                        for joueur in joueurs:
                            if joueur[0] == winnner1:
                                joueur[1] += 0.5
                        for joueur in joueurs:
                            if joueur[0] == winnner2:
                                joueur[1] += 0.5
                        print(joueurs)
                sorted_players = sorted(joueurs, reverse=True, key=lambda item: item[1])

                duels = []
                for i in range(0, len(joueurs) - 1, 2):
                    new_duel = [sorted_players[i - 1][0], sorted_players[i][0], 0]
                    duel_already_done = any(new_duel == match[:2] or new_duel == match[1::-1] for match in all_matches)

                    while duel_already_done is True:
                        i += 2
                        if i >= len(joueurs) - 1:
                            break
                        new_duel = [sorted_players[i - 1][0], sorted_players[i][0], 0]
                        duel_already_done = any(new_duel == match[:2] or new_duel == match[1::-1] for match in all_matches)
                    duels.append(new_duel)
                for tournament_id, tournament_data in data["_default"].items():
                    if tournament_data["Nom"] == tournoi:
                        tournament_data["Liste des tours"][-players_half:] = last_matches
                        tournament_data["Joueurs"] = sorted_players
                        tournament_data["Liste des tours"] += duels
                        tournament_data["Numero de tour"] += 1
                with open('databasetournament.json', 'w') as json_file:
                    json.dump(data, json_file)
                TournamentMenu()

            elif numero_tour is not None and numero_tour == 4:
                players = dict(joueurs)
                last_matches = Tournament.get_last_tournament_match(tournoi)
                print("-----RESULTATS ROUND 4-----")
                print("1p = match gagné / 0p = match perdu / 0.5p = match nul")
                for match in last_matches:
                    print(match)
                    resultat = int(input('Resultat: '))
                    match[-1] = resultat
                sorted_players = dict(sorted(players.items(), key=lambda item: item[1]))
                update_players_score = list(sorted_players.items())
                with open('databasetournament.json', 'r') as json_file:
                    data = json.load(json_file)
                for tournament_id, tournament_data in data["_default"].items():
                    if tournament_data["Nom"] == tournoi:
                        tournament_data["Liste des tours"][-players_half:] = last_matches
                        tournament_data["Joueurs"] = update_players_score
                with open('databasetournament.json', 'w') as json_file:
                    json.dump(data, json_file)
                TournamentMenu()
            else:
                print("Ce tournois est deja fini ou n'existe pas")
                TournamentMenu()

        elif user_choice == "4":
            MainMenu()

        else:
            AllViewMenu.erreur_de_saisie()
            self.__init__()
