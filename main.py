from controler.principal import MainMenu
from modele.player import DataBasePlayers
from modele.tournament import DataBaseTournament

# Initialise the two database and run the program.
databasetournament = DataBaseTournament()
databaseplayer = DataBasePlayers()
main = MainMenu()
