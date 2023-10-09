from math import *

class Goldilocks_Determiner:
    def __init__(self):
        """
        Constructor for a Goldilocks Determiner.
        Uses an empty dictionary in place of a given one. 
        """
        self.exoplanetDictionary = {}

    def __init__(self, dict):
        """
        Constructor for a Goldilocks Determiner.
        Saves a given dictionary of planet info. 
        """
        self.exoplanetDictionary = dict

    def get_stellar_lum(self, planet_name):
        """ Takes planet name and returns it's stellar luminosity"""
        planet_info = self.exoplanetDictionary[planet_name]
        if planet_info[13] != '':
            stellar_lum = 10 ** float(planet_info[13])
            return float(stellar_lum)
        else:
            return 0 # if no data available, keeps planet out of zone

    def get_sm_axis(self, planet_name):
        """ Takes planet name and returns it's semi-major axis"""
        planet_info = self.exoplanetDictionary[planet_name]
        if planet_info[8] != '':
            sm_axis = planet_info[8]
            return float(sm_axis)
        else:
            return -1 # if no data available, keeps planet out of zone

    def determine_goldilocks_inner(self, planet_name):
        """ Takes planet name and uses returns an ordered pair (inner, outer) bound"""
        stellar_lum = self.get_stellar_lum(planet_name)
        inner_bound = sqrt(stellar_lum / 1.1)

        return inner_bound

    def determine_goldilocks_outer(self, planet_name):
        """ Takes planet name and uses returns an ordered pair (inner, outer) bound"""
        stellar_lum = self.get_stellar_lum(planet_name)
        outer_bound = sqrt(stellar_lum / 0.53)

        return outer_bound

    def is_in_goldilocks_zone(self, planet_name):
        """ Takes planet name and returns boolean yes or no corresponding 
            with if the planet is within the bounds of it's goldilocks zone 
        """
        planet_stellar_dist = self.get_sm_axis(planet_name)
        inner = self.determine_goldilocks_inner(planet_name)
        outer =  self.determine_goldilocks_outer(planet_name)

        if inner < planet_stellar_dist < outer:
            return True
        else:
            return False
        
    def print_goldilocks_zone(self, planet_name):
        """ Takes planet name and prints a nice message about if it is in the goldilocks zone"""
        if self.is_in_goldilocks_zone(planet_name):
            print(planet_name, 'is in the goldilocks zone! (by Solar Equivalent AU)')
        else:
            print(planet_name, 'is not in the goldilocks zone (by Solar Equivalent AU).')
