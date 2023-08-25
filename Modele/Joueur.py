from tinydb import TinyDB


class DataBasePlayers:
    def __init__(self):
        self.db = TinyDB('databasetournament.json')


class Player:

    def __init__(self, nom, prenom, date, ine):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine

        self.db = TinyDB('databaseplayers.json')

    def insert(self):
        self.db.insert(
            {
                "Nom": self.nom,
                "Prenom": self.prenom,
                "Date": self.date,
                "INE": self.ine,
            }
        )

    def show_all(self):
        all_data = self.db.all()
        all_data = sorted(all_data, key=lambda k: k['Nom'])
        for data in all_data:
            print(data)
