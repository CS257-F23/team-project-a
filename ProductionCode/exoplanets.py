import argparse
from ProductionCode.Goldilocks import Goldilocks_Determiner
from ProductionCode.HabitablePlanets import Habitable_Finder
from ProductionCode.PlanetAnalyzer import exoplanetAnalyzer
from ProductionCode.load_data import take_exoplanet_data
# -*- coding: utf-8 -*-

exoplanet_data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')

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


def run_planet_info(args):
    """
    Takes list of command line args, if the given planet is the dataset, runs print_planet_info on it
    Param: list
    Returns: none
    """
    if verify_name_in_database(args.planet_info):
        exo_analyzer = exoplanetAnalyzer(exoplanet_data)
        exo_analyzer.print_planet_info(args.planet_info)

def run_goldilocks_planet(args):
    """
    Takes list of command line args, if the given planet is the dataset, runs print_goldilocks_zone on it
    Param: list
    Returns: none
    """
    if verify_name_in_database(args.goldilocks_planet):
        goldilocks_determiner = Goldilocks_Determiner(exoplanet_data)
        goldilocks_determiner.print_goldilocks_zone(args.goldilocks_planet)

def run_habitable_planets():
    """"
    Runs print_habitable_list
    Param: none
    Returns: none
    """
    habitable_finder = Habitable_Finder(exoplanet_data)
    habitable_finder.print_habitable_list()

def main():
    """Parses command line arguments and runs the correct function based on the given args"""
    args = parse_command_line()

    if args.planet_info:
        run_planet_info(args)
    elif args.goldilocks_planet:
        run_goldilocks_planet(args)
    elif args.habitable_planets:
        run_habitable_planets()

if __name__ == "__main__":
    main()
