import argparse
import csv
from Goldilocks import Goldilocks_Determiner
from PlanetAnalyzer import exoplanetAnalyzer
# -*- coding: utf-8 -*-

def take_exoplanet_data(exoplanetData) :
    """
    Takes a csv file of exoplanet data and returns a 
    dictionary of planets keyed to lists containing 
    all the info about them. 
    Param: string
    Returns: dictionary
    """
    #Make an empty dictionary
    exoplanetsByName = {}

    with open(exoplanetData, 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            exoplanetsByName = add_row_of_data_to_dictionary(row, exoplanetsByName)

        return exoplanetsByName

def add_row_of_data_to_dictionary(row, exoplanetsByName):
    """
    Helper function for take_exoplanet_data. 
    Adds one planet's worth of info into a growing dictionary of info by planet.
    Param: dictionary, dictionary 
    Returns: dictionary
    """

    #Save all the important data from each planet
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

def parse_command_line():
    """
    Parses command line and returns list of parsed args
    Param: none
    Returns: list
    """
    parser = argparse.ArgumentParser(description='Exoplanet Data Analyzer')

    #look up info about an exoplanet by its name
    parser.add_argument('--planet_info', metavar='Planet Name', type=str,
                        help='Look up info about an exoplanet by its name')

    # look up whether that planet is a goldilocks "planet" (in its star's habitable zone) or not
    parser.add_argument('--goldilocks_planet', metavar='Planet Name', type=str,
                    help='Look up whether that planet is a goldilocks planet (in its star\'s habitable zone) or not')

    #get a list of planets in the habitable zone
    parser.add_argument('--habitable_planets', action='store_true',
                        help='Get a list of planets in the habitable zone')

    return parser.parse_args()

def verify_name_in_database(planet_name):
    """
    Checks if string planet name given is in the dataset: 
    if not, print error message and return false, otherwise return true
    Param: string
    Returns: boolean
    """
    if planet_name not in exoplanet_data.keys():
        print("No data available for desired planet")
        return False
    else:
        return True

exoplanet_data = take_exoplanet_data("Data/ExoplanetSimplifiedData.csv")

def run_planet_info(planet_name):
    """
    Takes name of planet, if the given planet is the dataset, prints get_planet_info
    Param: string
    Returns: none
    """
    if verify_name_in_database(planet_name):
        exo_analyzer = exoplanetAnalyzer(exoplanet_data)
        print(exo_analyzer.get_formatted_planet_info(planet_name))

def run_goldilocks_planet(planet_name):
    """
    Takes name of planet, if the given planet is the dataset, prints get_goldilocks_zone
    Param: string
    Returns: none
    """
    if verify_name_in_database(planet_name):
        goldilocks_determiner = Goldilocks_Determiner(exoplanet_data)
        result = goldilocks_determiner.get_goldilocks_zone(planet_name)
        formatted = result[0]+ " " + result[1]
        print(formatted)

def run_habitable_planets():
    """"
    Runs print_habitable_list
    Param: none
    Returns: none
    """
    goldilocks_determiner = Goldilocks_Determiner(exoplanet_data)
    goldilocks_determiner.print_habitable_list()


def main():
    """Parses command line arguments and runs the correct function based on the given args"""
    args = parse_command_line()

    if args.planet_info:
        run_planet_info(args.planet_info)
    elif args.goldilocks_planet:
        run_goldilocks_planet(args.goldilocks_planet)
    elif args.habitable_planets:
        run_habitable_planets()


if __name__ == "__main__":
    main()
