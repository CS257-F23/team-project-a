from math import *

class Goldilocks_Determiner:
    def __init__(self):
        """
        Constructor for a Goldilocks Determiner.
        Uses an empty dictionary in place of a given one. 
        Param: none
        Returns: none
        """
        self.exoplanetDictionary = {}

    def __init__(self, datasource):
        """
        Constructor for a Goldilocks Determiner.
        Saves a given dictionary of planet info. 
        Param: dictionary
        Returns: none
        """
        self.datasource = datasource

    def get_stellar_lum(self, planet_name):
        """ 
        Takes planet name and returns it's stellar luminosity
        Param: string
        Return: float
        """
        planet_info = self.datasource.getPlanetInfo(planet_name)
        if planet_info[12] != None:
            stellar_lum = 10 ** float(planet_info[12])
            return float(stellar_lum)
        else:
            return 0 # if no data available, keeps planet out of zone

    def get_sm_axis(self, planet_name):
        """
        Takes planet name and returns it's semi-major axis
        Param: string
        Returns: float
        """
        planet_info = self.datasource.getPlanetInfo(planet_name)
        if planet_info[7] != None:
            sm_axis = planet_info[7]
            return float(sm_axis)
        else:
            return -1 # if no data available, keeps planet out of zone

    def determine_goldilocks_inner(self, planet_name):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(planet_name)
        inner_bound = sqrt(stellar_lum / 1.1)

        return inner_bound

    def determine_goldilocks_outer(self, planet_name):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(planet_name)
        outer_bound = sqrt(stellar_lum / 0.53)

        return outer_bound

    def is_in_goldilocks_zone(self, planet_name):
        """ 
        Takes planet name and returns boolean yes or no corresponding 
        with if the planet is within the bounds of it's goldilocks zone
        Param: string
        Returns: boolean
        """ 
        planet_stellar_dist = self.get_sm_axis(planet_name)
        inner = self.determine_goldilocks_inner(planet_name)
        outer =  self.determine_goldilocks_outer(planet_name)

        if inner < planet_stellar_dist < outer:
            return True
        elif inner == 0 or outer == 0 or planet_stellar_dist == -1:
            return None
        else:
            return False
        
    def get_goldilocks_zone(self, planet_name):
        """
        Takes planet name and returns a nice message about if it is in the goldilocks zone
        Param: string
        Returns: string
        """
        if self.is_in_goldilocks_zone(planet_name):
            return(planet_name + ' is in the goldilocks zone! (by Solar Equivalent AU)')
        elif self.is_in_goldilocks_zone(planet_name) == None:
            string_to_return = str('Unfortunately, the database does not contain sufficient information to determine if ' + planet_name + ' is in the goldilocks zone (by Solar Equivalent AU).')
            return(string_to_return)
        else:
            return(planet_name + ' is not in the goldilocks zone (by Solar Equivalent AU).')

    def create_habitable_list(self):
        """
        Creates a list of habitable planets using is_in_goldilocks_zone and iterating through the dictionary
        Param: none
        Returns: list
        """
        habitable_planets = []
        i = 1
        while i < 5524:
            current_planet = self.datasource.getPlanetNameFromId(i)
            if self.is_in_goldilocks_zone(current_planet):
                habitable_planets.append(current_planet)
            i = i + 1

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