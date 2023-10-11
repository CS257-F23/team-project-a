from ProductionCode.load_data import take_exoplanet_data

class exoplanetAnalyzer:
    def __init__(self):
        """
        Constructor for an Exoplanet Analyzer.
        Uses an empty dictionary in place of a given one. 
        Param: none
        Returns: none
        """
        self.exoplanetDictionary = {}
    
    def __init__(self, dictionary): 
        """
        Constructor for an Exoplanet Analyzer.
        Saves a given dictionary of planet info.
        Param: dictionary
        Returns: none 
        """
        self.exoplanetDictionary = dictionary

    def create_dictionary_from_csv(self, file):
        """ 
        Takes a csv file of planet info,
        and saves it as a dictionary for the Exoplanet Analyzer to use.
        Param: string
        Returns: none
        """
        self.exoplanetDictionary = take_exoplanet_data(file)
    
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

        