import datetime


class PlayersInformations:
    players_informations = []

    def __init__(self):
        self.players_informations = []
        nom = input("Nom: ")
        prenom = input("Prenom: ")
        print("Date de naissance en format AAAA-MM-JJ:")
        date_text = input("")
        while not self.validation(date_text):
            date_text = input("")

    @staticmethod
    def validation(date_text):
        try:
            datetime.date.fromisoformat(date_text)
        except ValueError:
            print("Le format incorrect, veuillez utiliser le format AAAA-MM-JJ pour indiquer une date: ")