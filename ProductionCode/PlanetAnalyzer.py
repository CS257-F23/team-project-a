from ProductionCode.load_data import take_exoplanet_data

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
    
    def __init__(self, dictionary): 
        """
        Constructor for an Exoplanet Analyzer.
        Saves a given dictionary of planet info.
        Param: dictionary
        Returns: none 
        """
        self.exoplanetDictionary = dictionary

    
    
    def get_planet_info(self, planetName):
        """
        Takes planet name and returns a list of info about that planet.
        Param: string
        Returns: list
        """
        return self.exoplanetDictionary[planetName]
    
    def format_planet_info(self, exoplanetInfo):
        """
        Takes a list of planet info and returns a 
        more readable string of data with appropriate labels.
        Param: list
        Returns: string
        """
        #The data in all the lists are already ordered as follows:
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Number of Moons: ", "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        
        formatedInfoString = "Planet Info \n\n"
        s = 0
        #Creates a big string, one label and variable a line
        while (s <= 15):
            formatedInfoString = formatedInfoString + infoList[s] + exoplanetInfo[s] + "\n"
            s += 1 
        return formatedInfoString
    
    def format_info_for_html(self, exoplanetInfo):
        """
        Takes a list of planet info and returns a 
        more readable string of data with appropriate labels for HTML.
        Param: list
        Returns: string
        """
        #The data in all the lists are already ordered as follows:
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Number of Moons: ", "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        
        formatedInfoString = "Planet Info \n\n"
        s = 0
        #Creates a big string, one label and variable a line
        while (s <= 15):
            formatedInfoString = formatedInfoString + infoList[s] + exoplanetInfo[s] + "<br>"
            s += 1 
        return formatedInfoString

    def get_formatted_planet_info(self, planetName):
        """
        Takes planet name and returns a string of info about that planet, formatted for printing.
        Param: string
        Returns: string
        """
        exoplanetInfo = self.get_planet_info(planetName)
        formatedExoplanetInfo = self.format_planet_info(exoplanetInfo)
        return(formatedExoplanetInfo)
    
    def print_planet_info(self, planetName):
        """ 
        Takes planet name and prints all the info about it. 
        Param: string
        Returns: none
        """
        formatedExoplanetInfo = self.get_formatted_planet_info(planetName)
        print(formatedExoplanetInfo)