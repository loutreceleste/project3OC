from tinydb import TinyDB
import json


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
                "Joueurs": self.joueurs,
                "Liste des tours": self.liste_des_tours
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
        except TypeError:
            print("ERREUR:")

    @staticmethod
    def get_tournament_players_half():
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for joueurs in tournois_dict.values():
                    nombre_de_joueurs = len(joueurs.get("Joueurs", [])) // 2
                    return int(nombre_de_joueurs)
        except json.JSONDecodeError:
            print("ERREUR:")
        except TypeError:
            print("ERREUR:")

    @staticmethod
    def get_tournament_match(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for joueurs in tournois_dict.values():
                    nombre_de_joueurs = len(joueurs.get("Joueurs", [])) // 2
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        liste_de_tours = tournoi.get("Liste des tours", [])
                        derniers_tours = liste_de_tours[-nombre_de_joueurs:]
                        return derniers_tours

        except json.JSONDecodeError:
            print("ERREUR:")
        except TypeError:
            print("ERREUR:")

    @staticmethod
    def get_number_of_round(nom_tournoi):
        try:
            with open('databasetournament.json') as json_file:
                data = json.load(json_file)
                tournois_dict = data.get("_default", {})
                for tournoi in tournois_dict.values():
                    if tournoi.get("Nom") == nom_tournoi:
                        return tournoi.get("Numero de tour")
        except TypeError:
            print("ERREUR:")

