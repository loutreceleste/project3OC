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
                        date_debut = input("Date et heure de debut du Round 1: ")
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
                        print("Ce nom de tournois existe deja!")
                        TournamentMenu()
            except json.JSONDecodeError:
                date_debut = input("Date et heure de debut du Round 1: ")
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
            tournament = Tournament("", "", "", "", "", "", "", "")
            print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")
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

            if numero_tour is not None and 1 <= numero_tour <= 3:
                with open('databasetournament.json', 'r') as json_file:
                    data = json.load(json_file)
                numero_round = numero_tour
                print(f"-----RESULTATS ROUND {numero_round}-----")
                print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")
                date_fin = input(f"Date et heure de fin du Round {numero_round}: ")

                for match in last_matches:
                        print(match)
                        while True:
                            resultat = input('Resultat: ')
                            try:
                                num = int(resultat)
                                if 1 <= num <= 3:
                                    break
                                else:
                                    print("Veuillez saisir un chiffre entre 1 et 3.")
                            except ValueError:
                                print("Veuillez saisir un chiffre entre 1 et 3.")
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

                date_debut = input(f"Date et heure de debut du Round {numero_round + 1}: ")

                duels = [f"Fin du Round {numero_round} le: {date_fin}, --ROUND {numero_round + 1}--, Debut du Round{numero_round + 1} le: {date_debut}"]
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
                with open('databasetournament.json', 'w') as json_file:
                    json.dump(data, json_file)
                TournamentMenu()

            elif numero_tour is not None and numero_tour == 4:
                last_matches = Tournament.get_last_tournament_match(tournoi)
                joueurs = Tournament.get_tournament_players(tournoi)
                print("-----RESULTATS ROUND 4-----")
                print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")
                date_fin = input("Date et heure de fin du Round 4: ")
                for match in last_matches:
                    print(match)
                    while True:
                        resultat = input('Resultat: ')
                        try:
                            num = int(resultat)
                            if 1 <= num <= 3:
                                break
                            else:
                                print("Veuillez saisir un chiffre entre 1 et 3.")
                        except ValueError:
                            print("Veuillez saisir un chiffre entre 1 et 3.")
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

                with open('databasetournament.json', 'r') as json_file:
                    data = json.load(json_file)
                for tournament_id, tournament_data in data["_default"].items():
                    if tournament_data["Nom"] == tournoi:
                        tournament_data["Liste des tours"][-players_half:] = [f"{last_matches}, Fin du Round 4 le: {date_fin}"]
                        tournament_data["Joueurs"] = sorted_players
                        tournament_data["Numero de tour"] = 0
                with open('databasetournament.json', 'w') as json_file:
                    json.dump(data, json_file)
                TournamentMenu()

            elif numero_tour == 0:
                print("Ce tournois est terminé")
                TournamentMenu()

            else:
                print("Ce tournois n'existe pas")
                TournamentMenu()

        elif user_choice == "4":
            MainMenu()

        else:
            AllViewMenu.erreur_de_saisie()
            self.__init__()
