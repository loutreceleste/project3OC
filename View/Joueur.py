class MenuPlayer:

    def __init__(self, nom, prenom, date, ine, score):
        print("-----NOUVEAU JOUEUR-----")
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.ine = ine
        self.score = score

    @staticmethod
    def player_informations():
        nom = input("Votre nom: ")
        prenom = input("Votre prenom: ")
        date = input("Votre date de naissance (format AAAA-MM-JJ): ")
        ine = input("Votre INE: ")
        score = MenuPlayer.initial_score()
        return nom, prenom, date, ine, score

    @staticmethod
    def initial_score():
        while True:
            try:
                initial_score = int(input("Votre score initial: "))
                return initial_score
            except ValueError:
                print("Veuillez saisir un chiffre!")

    @staticmethod
    def nombre_de_joueurs():
        while True:
            try:
                nombre_de_joueurs = int(input("Nombre de participants au tournois: "))
                return nombre_de_joueurs
            except ValueError:
                print("Veuillez saisir un chiffre!")

    @staticmethod
    def nom_tournois():
        nom_tournoi = input("Entrez le nom du tournoi : ")
        return nom_tournoi

    @staticmethod
    def title_new_player():
        print("-----NOUVEAU JOUEUR-----")

    @staticmethod
    def title_show_data():
        print("-----DATA BASE-----")
