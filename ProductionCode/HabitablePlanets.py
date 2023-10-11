from ProductionCode.Goldilocks import Goldilocks_Determiner

class Habitable_Finder:
    def __init__(self):
        """
        Constructor for a Habitable Finder.
        Uses an empty dictionary in place of a given one. 
        Param: none
        Returns: none
        """
        self.exoplanetDictionary = {}

    def __init__(self, dict):
        """
        Constructor for a Habitable Finder.
        Saves a given dictionary of planet info. 
        Param: dictionary 
        Returns: none
        """
        self.exoplanetDictionary = dict

    def create_habitable_list(self):
        """
        Creates a list of habitable planets using is_in_goldilocks_zone and iterating through the dictionary
        Param: none
        Returns: list
        """
        habitable_planets = []
        goldilocks_det = Goldilocks_Determiner(self.exoplanetDictionary)
        for planet in self.exoplanetDictionary:
            if goldilocks_det.is_in_goldilocks_zone(planet):
                habitable_planets.append(planet)

        return habitable_planets
    
    def print_habitable_list(self):
        """
        Prints the list of habitable planets
        Param: none
        Returns: none
        """
        list = self.create_habitable_list()
        print("The habitable planets (by Solar Equivalent AU) found in this database are")
        for planet in list:
            print(planet)