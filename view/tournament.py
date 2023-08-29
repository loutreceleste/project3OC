import json


class MenuTournament:

    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques):
        print("\n-----INFORMATIONS DU TOURNOI-----")
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombre_tours = nombre_tours
        self.numero_tours = numero_tour
        self.remarques = remarques

    @staticmethod
    def tournament_informations():
        nom = input("Nom du tournoi: ")
        lieu = input("Lieu du tournoi: ")
        dates = input("Dates du tournoi: ")
        nombre_tours = 4
        numero_tour = 1
        remarques = input("Remarques du directeur: ")
        return nom, lieu, dates, nombre_tours, numero_tour, remarques

    @staticmethod
    def tournament_participants():
        numero_ine = input("Numéro INE du joueur: ")
        score = 0
        return numero_ine, score

    @staticmethod
    def tournament_name():
        return input("Entrez le nom du tournoi: ")

    @staticmethod
    def title_new_tournament():
        print("\n-----CRÉER UN NOUVEAU TOURNOI-----")

    @staticmethod
    def title_tournaments():
        print("\n-----LES TOURNOIS EN COURS-----")

    @staticmethod
    def title_duel_tournament(nom_tournois):
        print(f"\n-----TOURS ET MATCHS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def title_players_tournament(nom_tournois):
        print(f"\n-----JOUEURS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def title_tournament_infos(nom_tournois):
        print(f"\n-----TOUTES LES INFOS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def title_end_round():
        print("\n-----FINIR ET RENSEIGNER UN ROUND-----")

    @staticmethod
    def point_explanation():
        print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore à jouer.")

    @staticmethod
    def tournament_allready_exist():
        print("Ce nom de tournoi existe déjà!")

    @staticmethod
    def error_scoring_1_3():
        print("Veuillez saisir un chiffre entre 1 et 3.")

    @staticmethod
    def error_scoring_1_4():
        print("Veuillez saisir un chiffre entre 1 et 4.")

    @staticmethod
    def input_result_duels():
        return input('Résultat du duel: ')

    @staticmethod
    def title_round_result(numero_round):
        print(f"\n-----RESULTATS ROUND {numero_round}-----")

    @staticmethod
    def title_round_4():
        print("\n-----RÉSULTAT ROUND 4-----")

    @staticmethod
    def error():
        print("ERREUR.")

    @staticmethod
    def tournament_finish():
        print("Ce tournois est deja terminé!")

    @staticmethod
    def tournament_does_not_exist():
        print("Ce tournoi n'existe pas!")

    @staticmethod
    def no_tournament():
        print("Aucun tournoi à afficher!")

    @staticmethod
    def number_of_players():
        while True:
            try:
                return int(input("Nombre de participants au tournoi: "))
            except ValueError:
                print("Veuillez saisir un chiffre!")

    @staticmethod
    def get_all_sorted_tournament_players(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournament_dict = data.get("_default", {})
                for tournamant in tournament_dict.values():
                    if tournamant.get("Nom") == tournament_name:
                        players_and_score = tournamant.get("Joueurs", [])
                        players = [item[0] for item in players_and_score]
                        print(players.sort())
                        break
                else:
                    MenuTournament.tournament_does_not_exist()
        except json.JSONDecodeError:
            MenuTournament.no_tournament()
        except TypeError:
            MenuTournament.error()

    @staticmethod
    def show_informations_tournament(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournament_dict = data.get("_default", {})
                for tournament in tournament_dict.values():
                    if tournament.get("Nom") == tournament_name:
                        print(tournament)
                        break
                else:
                    MenuTournament.tournament_does_not_exist()
        except json.JSONDecodeError:
            MenuTournament.no_tournament()
        except TypeError:
            MenuTournament.error()

    @staticmethod
    def show_all_informations():
        with open('databasetournament.json', 'r') as json_file:
            data = json.load(json_file)
            for tournament_id, tournament_data in data["_default"].items():
                print("Nom:", tournament_data["Nom"], "/",
                      "Lieu:", tournament_data["Lieu"], "/",
                      "Dates:", tournament_data["Dates"], "/",
                      "Nombre de tours:", tournament_data["Nombre de tours"], "/",
                      "Numéro de tour:", tournament_data["Numéro de tour"])

    @staticmethod
    def show_duel_informations(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournament_dict = data.get("_default", {})
                for tournament in tournament_dict.values():
                    if tournament.get("Nom") == tournament_name:
                        duels = list(tournament.items())
                        print(duels[0], duels[-1])
                        break
                else:
                    MenuTournament.tournament_does_not_exist()
        except json.JSONDecodeError:
            MenuTournament.no_tournament()
        except TypeError:
            MenuTournament.error()
