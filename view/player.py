class MenuPlayer:

    def __init__(self, nom, prenom, date, ine):
        print("\n-----NOUVEAU JOUEUR-----")
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine

    @staticmethod
    def player_informations():
        nom = input("Votre nom: ")
        prenom = input("Votre prénom: ")
        date = input("Votre date de naissance: ")
        ine = input("Votre INE: ")
        return nom, prenom, date, ine

    @staticmethod
    def title_new_player():
        print("\n-----NOUVEAU JOUEUR-----")

    @staticmethod
    def title_show_data_player():
        print("\n-----LISTE DES JOUEURS PARTICIPANTS-----")

    @staticmethod
    def no_players():
        print("Aucun joueur à afficher!")
