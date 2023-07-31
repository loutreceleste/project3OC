from tinydb import TinyDB
import json


class DataBaseTournament:
    def __init__(self):
        self.db = TinyDB('databaseplayers.json')


class DataBasePlayers:
    def __init__(self):
        self.db = TinyDB('databasetournament.json')


class Tournament:

    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques, joueurs):
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombre_tours = nombre_tours
        self.numero_tours = numero_tour
        self.remarques = remarques
        self.joueurs = joueurs
        self.db = TinyDB('databasetournament.json')

    def add_participant(self, joueur):
        self.joueurs.append(joueur)

    def insert(self):
        self.db.insert(
            {
                "Nom": self.nom,
                "Lieu": self.lieu,
                "Dates": self.dates,
                "Nombre de tours": self.nombre_tours,
                "Numero de tour": self.numero_tours,
                "Remarques": self.remarques,
                "Joueurs": self.joueurs
            }
        )

    def show_all(self):
        all_data = self.db.all()
        for data in all_data:
            print(data)

    @staticmethod
    def get_tournament_players(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        return tournoi.get("Joueurs", [])
        except json.JSONDecodeError:
            print("ERREUR:")


class Player:

    def __init__(self, nom, prenom, date, ine, score):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine
        self.score = score
        self.db = TinyDB('databaseplayers.json')

    def insert(self):
        self.db.insert(
            {
                "Nom": self.nom,
                "Prenom": self.prenom,
                "Date": self.date,
                "INE": self.ine,
                "Score": self.score
            }
        )

    def show_all(self):
        all_data = self.db.all()
        for data in all_data:
            print(data)
