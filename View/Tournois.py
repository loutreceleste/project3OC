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
    def titre_new_tournament():
        print("-----NOUVEAU TOURNOIS-----")

    @staticmethod
    def titre_acual_tournament():
        print("-----LES TOURNOIS EN COURS-----")

    @staticmethod
    def titre_end_round():
        print("-----FINIR ET RESEIGNER UN ROUND-----")

    @staticmethod
    def point_explanation():
        print("1 = joueur 1 qui gagne / 2 = joueur 2 qui gagne / 3 = match nul / 0 = match encore a jouer")

    @staticmethod
    def tournament_allready_exist():
        print("Ce nom de tournois existe deja!")

    @staticmethod
    def error_scoring():
        print("Veuillez saisir un chiffre entre 1 et 3.")

    @staticmethod
    def input_result_duels():
        result = input('Resultat du duel: ')
        return result

    @staticmethod
    def end_round_date(numero_round):
        end_date = input(f"Date et heure de fin du Round {numero_round}: ")
        return end_date

    @staticmethod
    def start_round_date(numero_round):
        start_date = input(f"Date et heure de debut du Round {numero_round + 1}: ")
        return start_date

    @staticmethod
    def title_round_result(numero_round):
        print(f"-----RESULTATS ROUND {numero_round}-----")

    @staticmethod
    def title_round_4():
        print("-----RESULTATS ROUND 4-----")

    @staticmethod
    def end_date_round_4():
        end_date = input("Date et heure de fin du Round 4: ")
        return end_date

    @staticmethod
    def start_date_round_1():
        start_date = input("Date et heure de debut du Round 1: ")
        return start_date

    @staticmethod
    def error():
        print("ERREUR")

    @staticmethod
    def tournament_finish():
        print("Ce tournois est deja terminé!")

    @staticmethod
    def tournament_does_not_exist():
        print("Ce tournois n'existe pas!")