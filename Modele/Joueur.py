from tinydb import TinyDB
import json


class DataBasePlayers:
    def __init__(self):
        self.db = TinyDB('databasetournament.json')


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
