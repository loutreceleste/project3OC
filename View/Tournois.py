import json


class MenuTournament:

    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques):
        print()
        print("-----INFORMATIONS DU TOURNOI-----")
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
    def participants_tournois():
        numero_ine = input("Numéro INE du joueur: ")
        score = 0
        return numero_ine, score

    @staticmethod
    def titre_new_tournament():
        print()
        print("-----CRÉER UN NOUVEAU TOURNOI-----")

    @staticmethod
    def titre_tournaments():
        print()
        print("-----LES TOURNOIS EN COURS-----")

    @staticmethod
    def titre_duel_tournament(nom_tournois):
        print()
        print(f"-----TOURS ET MATCHS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def titre_players_tournament(nom_tournois):
        print()
        print(f"-----JOUEURS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def titre_info_tournament(nom_tournois):
        print()
        print(f"-----TOUTES LES INFOS DU TOURNOI {nom_tournois.upper()}-----")

    @staticmethod
    def titre_end_round():
        print()
        print("-----FINIR ET RENSEIGNER UN ROUND-----")

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
        result = input('Résultat du duel: ')
        return result

    @staticmethod
    def title_round_result(numero_round):
        print()
        print(f"-----RESULTATS ROUND {numero_round}-----")

    @staticmethod
    def title_round_4():
        print()
        print("-----RÉSULTAT ROUND 4-----")

    @staticmethod
    def end_date_round_4():
        end_date = input("Date et heure de fin du Round 4: ")
        return end_date

    @staticmethod
    def start_date_round_1():
        start_date = input("Date et heure de début du Round 1: ")
        return start_date

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
    def get_all_sorted_tournament_players(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        players_and_score = tournoi.get("Joueurs", [])
                        players = [item[0] for item in players_and_score]
                        players.sort()
                        print(players)
                        break
                else:
                    MenuTournament.tournament_does_not_exist()
        except json.JSONDecodeError:
            MenuTournament.no_tournament()
        except TypeError:
            MenuTournament.error()

    @staticmethod
    def show_informations_tournament(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        print(tournoi)
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
    def show_duel_informations(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        duels = list(tournoi.items())
                        print(duels[0], duels[-1])
                        break
                else:
                    MenuTournament.tournament_does_not_exist()
        except json.JSONDecodeError:
            MenuTournament.no_tournament()
        except TypeError:
            MenuTournament.error()
