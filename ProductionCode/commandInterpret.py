import sys
from PlanetAnalyzer import exoplanetAnalyzer
from Goldilocks import Goldilocks_Determiner
from HabitablePlanets import Habitable_Finder

class Command_line_interpreter:
    def __init__(self) -> None:
        """
        Constructor for a Command Line Interpreter.
        Uses an empty dictionary in place of a given one. 
        """
        self.exoplanetDictionary = {}

    def __init__(self, dict):
        """
        Constructor for a Command Line Interpreter.
        Saves a given dictionary of planet info. 
        """
        self.exoplanetDictionary = dict

    def run_planet_info(self, planet_name):
        " Takes a planet name and runs print_planet_info on that planet"
        exoplanetFinder = exoplanetAnalyzer(self.exoplanetDictionary)
        exoplanetFinder.print_planet_info(planet_name)

    def run_goldilocks_planet(self, planet_name):
        " Takes a planet name and runs print_goldilocks on that planet"
        goldilocks = Goldilocks_Determiner(self.exoplanetDictionary)
        goldilocks.print_goldilocks_zone(planet_name)
    
    def run_habitable_planets(self):
        " Runs print_habitable_list"
        hab_finder = Habitable_Finder(self.exoplanetDictionary)
        hab_finder.print_habitable_list()

        
    def run_specified_arg(self):
        " If args are valid, runs the specified function, else prints usage statement"
        if sys.argv[1] == "--habitable_planets":
            self.run_habitable_planets()

        elif len(sys.argv) >= 3: 
            if sys.argv[1] == "--planet_info":
                self.run_planet_info(sys.argv[2])

            elif sys.argv[1] == "--goldilocks_planet":
                self.run_goldilocks_planet(sys.argv[2])
            
            else:
                print("exoplanet.py Usage: usage statement")

        else:
            print("exoplanet.py Usage: usage statement")
