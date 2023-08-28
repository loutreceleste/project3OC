class MenuPlayer:

    def __init__(self, nom, prenom, date, ine):
        print()
        print("-----NOUVEAU JOUEUR-----")
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
    def nombre_de_joueurs():
        while True:
            try:
                nombre_de_joueurs = int(input("Nombre de participants au tournoi: "))
                return nombre_de_joueurs
            except ValueError:
                print("Veuillez saisir un chiffre!")

    @staticmethod
    def nom_tournois():
        nom_tournoi = input("Entrez le nom du tournoi: ")
        return nom_tournoi

    @staticmethod
    def title_new_player():
        print()
        print("-----NOUVEAU JOUEUR-----")

    @staticmethod
    def title_show_data():
        print()
        print("-----LISTE DES JOUEURS PARTICIPANTS-----")
