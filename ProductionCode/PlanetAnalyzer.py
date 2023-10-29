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
    
    def __init__(self, dataSource): 
        """
        Constructor for an Exoplanet Analyzer.
        Saves a given dictionary of planet info.
        Param: dictionary
        Returns: none 
        """
        self.dataSource = dataSource
    
    def get_planet_info(self, planetName):
        """
        Takes planet name and returns a list of info about that planet.
        Param: string
        Returns: list
        """
        return self.dataSource.getPlanetInfo(planetName)
    
    def format_planet_info(self, exoplanetInfo):
        """
        Takes a list of planet info and returns a 
        more readable string of data with appropriate labels.
        Param: list
        Returns: string
        """
        #The data in all the lists are already ordered as follows:
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        
        formatedInfoString = "Planet Info \n\n"
        s = 0
        #Creates a big string, one label and variable a line
        while (s <= 14):
            formatedInfoString = formatedInfoString + str(infoList[s]) + str(exoplanetInfo[s]) + "\n"
            s += 1 
        return formatedInfoString
    
    def format_info_for_list(self, exoplanetInfo):
        """
        Takes a list of planet info and returns a 
        more readable string of data with appropriate labels for HTML.
        Param: list
        Returns: list
        """
        #The data in all the lists are already ordered as follows:
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        
        formatedInfoList = ["Planet Info"]
        s = 0
        while (s <= 14):
            formatedInfoList.append(str(infoList[s] + str(exoplanetInfo[s])))
            s += 1 
        return formatedInfoList

    def get_formatted_planet_info_list(self, planet_name):
        """
        Takes planet name and returns a list of info about that planet.
        Param: string
        Returns: list
        """
        exoplanetInfo = self.get_planet_info(planet_name)
        formatedExoplanetInfo = self.format_info_for_list(exoplanetInfo)
        return(formatedExoplanetInfo)

    def get_formatted_planet_info(self, planetName):
        """
        Takes planet name and returns a string of info about that planet, formatted for printing.
        Param: string
        Returns: string
        """
        exoplanetInfo = self.get_planet_info(planetName)
        formatedExoplanetInfo = self.format_planet_info(exoplanetInfo)
        return(formatedExoplanetInfo)
    