#Header Comments
#
#

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

        

if __name__ == "__main__" : 
    exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    exoplanetFinder = exoplanetAnalyzer(exoplanetDictionary)
    exoplanetFinder.print_planet_info('14 Her b')