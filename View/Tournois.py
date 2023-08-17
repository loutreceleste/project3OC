class MenuTournament:

    def __init__(self, nom, lieu, dates, nombre_tours, numero_tour, remarques):
        print("-----INFORMATIONS DU TOURNOIS-----")
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombre_tours = nombre_tours
        self.numero_tours = numero_tour
        self.remarques = remarques

    @staticmethod
    def tournament_informations():
        nom = input("Nom du tournois: ")
        lieu = input("Lieu du tournois: ")
        dates = input("Dates du tournois: ")
        nombre_tours = 4
        numero_tour = 1
        remarques = input("Remarques du directeur: ")
        return nom, lieu, dates, nombre_tours, numero_tour, remarques

    @staticmethod
    def participants_tournois():
        numero_ine = input("Numero INE du joueur: ")
        score = 0
        return numero_ine, score

    @staticmethod
    def nouveau_score():
        while True:
            try:
                new_score = eval(input("Nouveau score: "))
                return new_score
            except ValueError:
                print("Erreur")

    @staticmethod
    def titre_new_tournament():
        print("-----NOUVEAU TOURNOIS-----")

    @staticmethod
    def titre_acual_tournament():
        print("-----LES TOURNOIS EN COURS-----")

    @staticmethod
    def titre_end_round():
        print("-----FINIR ET RESEIGNER UN ROUND-----")

    @staticmethod
    def get_date():
        get_date = input("Date et heure de debut du Round: ")
        return get_date
