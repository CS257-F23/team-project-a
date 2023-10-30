from math import *

class Goldilocks_Determiner:

    def __init__(self, dataSource):
        """
        Constructor for a Goldilocks Determiner.
        Saves an inputted DataSource object that can access the database.
        Param: DataSource
        Returns: none
        """
        self.dataSource = dataSource

    def get_stellar_lum(self, star_name):
        """ 
        Takes star name and returns it's stellar luminosity
        Param: string
        Return: float
        """
        host_info = self.dataSource.getHostInfo(star_name)
        if host_info[12] != None:
            stellar_lum = 10 ** float(host_info[7])
            return float(stellar_lum)
        else:
            return 0 # if no data available, keeps planet out of zone

    def get_sm_axis(self, planet_name):
        """
        Takes planet name and returns it's semi-major axis
        Param: string
        Returns: float
        """
        planet_info = self.dataSource.getPlanetInfo(planet_name)
        if planet_info[7] != None:
            sm_axis = planet_info[7]
            return float(sm_axis)
        else:
            return -1 # if no data available, keeps planet out of zone

    def determine_goldilocks_inner(self, star_name):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(star_name)
        inner_bound = sqrt(stellar_lum) * .95

        return inner_bound

    def determine_goldilocks_outer(self, star_name):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(star_name)
        outer_bound = sqrt(stellar_lum) * 1.4

        return outer_bound

    def found_in_goldilocks_zone(self, planet_name):
        """ 
        Takes planet name and returns boolean yes or no corresponding 
        with if the planet is within the bounds of it's goldilocks zone
        Param: string
        Returns: boolean
        """ 
        star_name = self.dataSource.getHostIdFromPlanet(planet_name)
        planet_stellar_dist = self.get_sm_axis(planet_name)
        inner = self.determine_goldilocks_inner(star_name)
        outer =  self.determine_goldilocks_outer(star_name)

        if inner < planet_stellar_dist < outer:
            return True
        elif inner == 0 or outer == 0 or planet_stellar_dist == -1:
            return None
        else:
            return False
        
    def is_in_goldilocks_zone(self, planet_name):
        if self.dataSource.getGoldilocks(planet_name):
            return True
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

    def create_habitable_column(self):
        """
        Creates a list of habitable planets using is_in_goldilocks_zone and iterating through the dictionary
        Param: none
        Returns: list
        """
        i = 1
        while i < 5524:
            current_planet = self.dataSource.getPlanetNameFromId(i)
            if self.is_in_goldilocks_zone(current_planet):
                self.dataSource.addvaluetoGoldilocks(current_planet, True)
            else:
                self.dataSource.addvaluetoGoldilocks(current_planet, False)
            i = i + 1

    def print_habitable_list(self):
        """
        Prints the list of habitable planets
        Param: none
        Returns: none
        """

        print("The habitable planets (by Solar Equivalent AU) found in this database are")
        for planet in list:
            print(planet)
    