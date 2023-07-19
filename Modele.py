import datetime
from tinydb import TinyDB


class DataBasePlayers:
    def __init__(self):
        self.db = TinyDB('databaseplayers.json')


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

    @staticmethod
    def validation(self, date):
        try:
            datetime.date.fromisoformat(date)
        except ValueError:
            print("Le format incorrect, veuillez utiliser le format AAAA-MM-JJ pour indiquer une date: ")
