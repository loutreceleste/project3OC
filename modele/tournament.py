from tinydb import TinyDB
import json
from datetime import datetime
import view.tournament

class DataBaseTournament:
    def __init__(self):
        self.db = TinyDB('databaseplayers.json')

class Tournament:
    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques, joueurs, liste_des_tours):
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombre_tours = nombre_tours
        self.numero_tours = numero_tour
        self.remarques = remarques
        self.joueurs = joueurs
        self.liste_des_tours = liste_des_tours
        self.db = TinyDB('databasetournament.json')

    def insert(self):
        self.db.insert(
            {
                "Nom": self.nom,
                "Lieu": self.lieu,
                "Dates": self.dates,
                "Nombre de tours": self.nombre_tours,
                "Numéro de tour": self.numero_tours,
                "Remarques": self.remarques,
                "Joueurs": self.joueurs,
                "Liste des tours": self.liste_des_tours
            }
        )

    @staticmethod
    def get_all_tournament_players(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournament_dict = data.get("_default", {})
                for tournament in tournament_dict.values():
                    if tournament.get("Nom") == tournament_name:
                        return tournament.get("Joueurs", [])
        except TypeError:
            view.tournament.MenuTournament.error()

    @staticmethod
    def get_half_tournament_players():
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournament_dict = data.get("_default", {})
                for players in tournament_dict.values():
                    return int(len(players.get("Joueurs", [])) // 2)
        except TypeError:
            view.tournament.MenuTournament.error()

    @staticmethod
    def get_lasts_tournament_matchs(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for joueurs in tournois_dict.values():
                    nombre_de_joueurs = len(joueurs.get("Joueurs", [])) // 2
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == tournament_name:
                        liste_de_tours = tournoi.get("Liste des tours", [])
                        return liste_de_tours[-nombre_de_joueurs:]
        except TypeError:
            view.tournament.MenuTournament.error()

    @staticmethod
    def get_all_tournament_matchs(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
            for tournoi in tournois_dict.values():
                if tournoi.get("Nom") == tournament_name:
                    return tournoi.get("Liste des tours", [])
        except TypeError:
            view.tournament.MenuTournament.error()

    @staticmethod
    def get_number_of_round(tournament_name):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == tournament_name:
                        return tournoi.get("Numéro de tour")
        except TypeError:
            view.tournament.MenuTournament.error()

    @staticmethod
    def write_in_database_tournament(data):
        with open('databasetournament.json', 'w') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def read_in_database_tournament():
        with open('databasetournament.json', 'r') as json_file:
            return json.load(json_file)

    @staticmethod
    def date_time_now():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
