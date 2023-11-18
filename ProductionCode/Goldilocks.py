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

    def get_stellar_lum(self, star_id):
        """ 
        Takes star name and returns it's stellar luminosity
        Param: string
        Return: float
        """
        host_info = self.dataSource.getHostInfo(star_id)
        unformatted_stellar_lum = host_info[0][6]
        if unformatted_stellar_lum != None:
            stellar_lum = 10 ** float(unformatted_stellar_lum)
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
        sm_axis = planet_info[7]
        if sm_axis != None:
            return float(sm_axis)
        else:
            return -1 # if no data available, keeps planet out of zone

    def determine_goldilocks_inner(self, star_id):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(star_id)
        inner_bound = sqrt(stellar_lum) * .95

        return inner_bound

    def determine_goldilocks_outer(self, star_id):
        """
        Takes planet name and uses returns an ordered pair (inner, outer) bound
        Param: string
        Returns: float
        """
        stellar_lum = self.get_stellar_lum(star_id)
        outer_bound = sqrt(stellar_lum) * 1.4

        return outer_bound

    def determine_in_goldilocks_zone(self, planet_name):
        """ 
        Takes planet name and returns boolean yes or no corresponding 
        with if the planet is within the bounds of it's goldilocks zone,
        for use in updating database.
        Param: string
        Returns: boolean
        """ 
        star_id = self.dataSource.getHostIdFromPlanet(planet_name)[0][0]
        planet_stellar_dist = self.get_sm_axis(planet_name)
        inner = self.determine_goldilocks_inner(star_id)
        outer =  self.determine_goldilocks_outer(star_id)

        if inner < planet_stellar_dist < outer:
            return True
        elif inner == 0 or outer == 0 or planet_stellar_dist == -1:
            return None
        else:
            return False
        
    def is_in_goldilocks_zone(self, planet_name):
        """
        Takes planet name and returns true or false depending on if it is in the goldilocks zone
        Param: string
        Returns: boolean
        """
        if self.dataSource.getGoldilocksValue(planet_name) == True:
            return True
        elif self.dataSource.getGoldilocksValue(planet_name) == False:
            return False
        else:
            return None
        
    
    def get_goldilocks_zone(self, planet_name):
        """
        Takes planet name and returns a nice message about if it is in the goldilocks zone
        Param: string
        Returns: string
        """
        if self.is_in_goldilocks_zone(planet_name):
            return(planet_name + ' is in the goldilocks zone! (by Solar Equivalent AU)')
        elif self.is_in_goldilocks_zone(planet_name) == None:
            string_to_return = str('Unfortunately, the database does not contain sufficient information to determine if ' + planet_name + ' is in the goldilocks zone')
            return(string_to_return)
        else:
            return(planet_name + ' is not in the goldilocks zone (by Solar Equivalent AU).')

    def update_habitable_column(self):
        """
        Updates the in_goldilocks column using determine_in_goldilocks_zone and iterating through the planet ids.
        Param: none
        Returns: none
        """
        planet_count = 1
        total_number_of_planets = 5524
        while planet_count < total_number_of_planets:
            current_planet = self.dataSource.getPlanetNameFromId(i)
            if self.determine_in_goldilocks_zone(current_planet):
                self.dataSource.setGoldilocks(True, current_planet)
            elif self.determine_in_goldilocks_zone(current_planet) == None:
                self.dataSource.setGoldilocks('NULL', current_planet)
            else:
                self.dataSource.setGoldilocks(False, current_planet)
            planet_count = planet_count + 1