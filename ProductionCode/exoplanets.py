from math import *
import csv 

def take_exoplanet_data(exoplanetData) :
    exoplanetsByName = {}

    with open(exoplanetData, 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
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

            if planetName not in exoplanetsByName :
                exoplanetsByName[planetName] = [planetName, hostName, numberOfStars, numberOfPlanets,
                                                numberOfMoons, discoveryMethod, discoveryYear, discoveryFacility, 
                                                semiMajorAxis, planetRadius, planetMass, stellarRadius, stellarMass, 
                                                stellarLuminosity, galacticLatitude, galacticLongitude]
                
        
        return exoplanetsByName
                

class exoplanetAnalyzer:
    def __init__(self):
        self.exoplanetDictionary = {}
    
    def __init__(self, dictionary): 
        self.exoplanetDictionary = dictionary

    def create_dictionary_from_csv(self, file):
        self.exoplanetDictionary = take_exoplanet_data(file)
    
    def get_planet_info(self, planetName):
        return self.exoplanetDictionary[planetName]
    
    def format_planet_info(self, exoplanetInfo):
        infoList = ["Planet Name: ", "Host Name: ", "Number of Stars: ", "Number of Planets: ",
                    "Number of Moons: ", "Discovery Method: ", "Discovery Year: ",
                    "Discovery Facility: ", "Semi-Major Axis: ", "Planet Radius: ", "Planet Mass: ",
                    "Stellar Radius: ", "Stellar Mass: ", "Stellar Luminosity: ", 
                    "Galactic Latitude: ", "Galactic Longitude: "]
        formatedInfoString = "Planet Info \n"
        s = 0
        while (s <= 15):
            formatedInfoString = formatedInfoString + infoList[s] + exoplanetInfo[s] + "\n"
            s += 1 
        return formatedInfoString
    
    def print_planet_info(self, planetName):
        exoplanetInfo = self.get_planet_info(planetName)
        formatedExoplanetInfo = self.format_planet_info(exoplanetInfo)
        print(formatedExoplanetInfo)

        

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
    exoplanetFinder = exoplanetAnalyzer(exoplanetDictionary)
    exoplanetFinder.print_planet_info('14 Her b')
    goldilocks = Goldilocks_Determiner()
    test1 = goldilocks.is_in_goldilocks_zone("Kepler-22 b")
    test2 = goldilocks.is_in_goldilocks_zone("Kepler-224 b")
    print(test1)
    print(test2)