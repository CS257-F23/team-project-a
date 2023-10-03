from math import *
import csv 
import sys

def take_exoplanet_data(exoplanetData) :
    """
    Takes a csv file of exoplanet data and returns a 
    dictionary of planets keyed to lists containing 
    all the info about them. 
    """
    #Make an empty dictionary
    exoplanetsByName = {}

    with open(exoplanetData, 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        #Save all the important data from each planet
        for row in datareader:
            planetName = row['pl_name']
            hostName = row['hostname']
            numberOfStars = row['sy_snum']
            numberOfPlanets = row['sy_pnum']
            numberOfMoons = row['sy_mnum']
            discoveryMethod = row['discoverymethod']
            discoveryYear = row['disc_year']
            discoveryFacility = row['disc_facility']
            semiMajorAxis = row ['pl_orbsmax']
            planetRadius = row['pl_rade']
            planetMass = row['pl_bmasse']
            stellarRadius = row ['st_rad']
            stellarMass = row['st_mass']
            stellarLuminosity = row ['st_lum']
            galacticLatitude = row ['glat']
            galacticLongitude = row ['glon']

            #Make that planet an entry in the dictionary
            if planetName not in exoplanetsByName :
                #Put the data in a list 
                exoplanetsByName[planetName] = [planetName, hostName, numberOfStars, numberOfPlanets,
                                                numberOfMoons, discoveryMethod, discoveryYear, discoveryFacility, 
                                                semiMajorAxis, planetRadius, planetMass, stellarRadius, stellarMass, 
                                                stellarLuminosity, galacticLatitude, galacticLongitude]
                
        
        return exoplanetsByName
                

class exoplanetAnalyzer:
    def __init__(self, dictionary=None):
        """
        Constructor for an Exoplanet Analyzer.
        Uses an empty dictionary in place of a given one. 
        """
        if dictionary is None:
            self.exoplanetDictionary = {}
        else:
            self.exoplanetDictionary = dictionary

    def __init__(self, dictionary): 
        """
        Constructor for an Exoplanet Analyzer.
        Saves a given dictionary of planet info. 
        """
        self.exoplanetDictionary = dictionary

    def create_dictionary_from_csv(self, file):
        """ 
        Takes a csv file of planet info,
        and saves it as a dictionary for the Exoplanet Analyzer to use.
        """
        self.exoplanetDictionary = take_exoplanet_data(file)
    
    def get_planet_info(self, planetName):
        """Takes planet name and returns a list of info about that planet."""
        return self.exoplanetDictionary[planetName]
    
    def format_planet_info(self, exoplanetInfo):
        """
        Takes a list of planet info and returns a 
        more readable string of data with appropriate labels.
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
    
    def print_planet_info(self, planetName):
        """ Takes planet name and prints all the info about it. """
        exoplanetInfo = self.get_planet_info(planetName)
        formatedExoplanetInfo = self.format_planet_info(exoplanetInfo)
        print(formatedExoplanetInfo)

        

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
            return 0

    def get_sm_axis(self, planet_name):
        """ Takes planet name and returns it's semi-major axis"""
        planet_info = self.exoplanetDictionary[planet_name]
        if planet_info[8] != '':
            sm_axis = planet_info[8]
            return float(sm_axis)
        else:
            return -1

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
        " Takes planet name and prints a nice message about if it is in the goldilocks zone"
        if self.is_in_goldilocks_zone(planet_name):
            print(planet_name, 'is in the goldilocks zone! (by Solar Equivalent AU)')
        else:
            print(planet_name, 'is not in the goldilocks zone (by Solar Equivalent AU).')

class Habitable_Finder:
    def __init__(self):
        """
        Constructor for a Habitable Finder.
        Uses an empty dictionary in place of a given one. 
        """
        self.exoplanetDictionary = {}

    def __init__(self, dict):
        """
        Constructor for a Habitable Finder.
        Saves a given dictionary of planet info. 
        """
        self.exoplanetDictionary = dict

    def create_habitable_list(self):
        "Creates a list of habitable planets using is_in_goldilocks_zone and iterating through the dictionary"
        habitable_planets = []
        goldilocks_det = Goldilocks_Determiner(self.exoplanetDictionary)
        for planet in self.exoplanetDictionary:
            if goldilocks_det.is_in_goldilocks_zone(planet):
                habitable_planets.append(planet)

        return habitable_planets
    
    def print_habitable_list(self):
        "Prints the list of habitable planets"
        list = self.create_habitable_list()
        print("The habitable planets (by Solar Equivalent AU) found in this database are")
        for planet in list:
            print(planet)

if __name__ == "__main__" :
    #test stuff
    exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    exo_analyzer = exoplanetAnalyzer(exoplanetDictionary)
    gold_det = Goldilocks_Determiner(exoplanetDictionary)
    hab_finder = Habitable_Finder(exoplanetDictionary)
    #exo_analyzer.print_planet_info('WASP-41 c')
    #gold_det.print_goldilocks_zone('14 Her b')
    #hab_finder.print_habitable_list()