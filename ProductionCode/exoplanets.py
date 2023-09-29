from math import *
from exoplanet_data_reader import *

class Goldilocks_Determiner:
    def __init__(self) -> None:
        pass

    def get_stellar_lum(self, planet_name):
        """ Takes planet name and returns it's stellar luminosity"""
        planet_info = exoplanetDictionary[planet_name]
        stellar_lum = 10 ** float(planet_info[13])
        
        return float(stellar_lum)

    def get_sm_axis(self, planet_name):
        """ Takes planet name and returns it's semi-major axis"""
        planet_info = exoplanetDictionary[planet_name]
        sm_axis = planet_info[8]
        
        return float(sm_axis)

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

if __name__ == "__main__" :
    exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    goldilocks = Goldilocks_Determiner()
    test1 = goldilocks.is_in_goldilocks_zone("Kepler-22 b")
    test2 = goldilocks.is_in_goldilocks_zone("Kepler-224 b")
    print(test1)
    print(test2)