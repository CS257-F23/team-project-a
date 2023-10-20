def take_exoplanet_data():
    """
    Creates the hard-coded data. 
    Param: none
    Returns: dictionary 
    """
    hard_coded_database = {}
    hard_coded_database["ups And d"] = ["ups And d", "ups And", "2", "3", "0", "Radial Velocity",
                                        "1999", "Multiple Observatories", "2.513290", "12.500",
                                         "3257.74117", "1.56", "1.30", "0.525", "-20.66791",
                                          "132.00045"]
    return hard_coded_database

class exoplanetAnalyzer:
    def __init__(self, dictionary=None):
        """
        Constructor for an Exoplanet Analyzer.
        Uses the given dictionary or an empty one if not provided.
        Param: dictionary (optional)
        Returns: none
        """
        if dictionary is None:
            self.exoplanetDictionary = {}
        else:
            self.exoplanetDictionary = dictionary
    
    def get_planet_info(self, planetName):
        """
        Takes planet name and returns a list of info about that planet.
        Param: string
        Returns: list
        """
        return self.exoplanetDictionary[planetName]
    
    def get_info_labels(self):
        """
        Returns a list of labels that correspond with the info that 
        the lists gotten by get_planet_info provide
        Param: none
        Returns: list
        """
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Number of Moons: ", "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        return infoList