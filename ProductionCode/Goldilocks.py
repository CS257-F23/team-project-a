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
        if host_info[0][6] != None:
            stellar_lum = 10 ** float(host_info[0][6])
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
        """
        if self.dataSource.getGoldilocksValue(planet_name)[0][0] == True:
            return True
        elif self.dataSource.getGoldilocksValue(planet_name)[0][0] == False:
            return False
        else:
            return None
        
    def setGoldilocks(self, in_goldilocks, planet_name):
        """
        Takes planet name and sets corresponding in_goldilocks value to given boolean
        """
        cursor = self.dataSource.connection.cursor()
        if in_goldilocks == 'NULL':
            query = "UPDATE exoplanet_data SET in_goldilocks=NULL WHERE planet_name=%s;"
            cursor.execute(query, (planet_name,))
        else:
            query = "UPDATE exoplanet_data SET in_goldilocks=%s WHERE planet_name=%s;"
            cursor.execute(query, (in_goldilocks, planet_name,))
        self.dataSource.connection.commit()
    
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

    def update_habitable_column(self):
        """
        Updates the in_goldilocks column using determine_in_goldilocks_zone and iterating through the planet ids.
        Param: none
        Returns: none
        """
        i = 1
        while i < 5524:
            current_planet = self.dataSource.getPlanetNameFromId(i)
            if self.determine_in_goldilocks_zone(current_planet):
                self.setGoldilocks(True, current_planet)
            elif self.determine_in_goldilocks_zone(current_planet) == None:
                self.setGoldilocks('NULL', current_planet)
            else:
                self.setGoldilocks(False, current_planet)
            i = i + 1

    def get_habitable_list(self):
        """
        Returns the list of habitable planets
        Param: none
        Returns: list
        """

        cursor = self.dataSource.connection.cursor()
        query = "SELECT planet_name FROM exoplanet_data WHERE in_goldilocks= True;"
        cursor.execute(query,)
        planets = cursor.fetchall()
        habitable_planets = self.dataSource.formatPlanetList(planets)
        return habitable_planets
        
    def print_habitable_list(self):
        """
        Prints the list of habitable planets
        Param: none
        Returns: none
        """

        print("The habitable planets (by Solar Equivalent AU) found in this database are")
        cursor = self.dataSource.connection.cursor()
        query = "SELECT planet_name FROM exoplanet_data;"
        cursor.execute(query,)
        planets = cursor.fetchall()
        for planet in planets:
            if self.is_in_goldilocks_zone(planet):
                print(planet[0])