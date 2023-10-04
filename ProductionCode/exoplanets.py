import argparse
from Goldilocks import Goldilocks_Determiner
from HabitablePlanets import Habitable_Finder
from PlanetAnalyzer import exoplanetAnalyzer
from load_data import take_exoplanet_data
# -*- coding: utf-8 -*-

exoplanet_data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')

def parse_command_line():
    """This is a docstring"""
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
    """ Checks if string planet name given is in the dataset: 
        if not, print error message and return false, otherwise return true
    """
    if planet_name not in exoplanet_data.keys():
        print("No data available for desired planet")
        return False
    else:
        return True


def run_planet_info(args):
    """this is another docstring, wow"""
    if verify_name_in_database(args.planet_info):
        exo_analyzer = exoplanetAnalyzer(exoplanet_data)
        exo_analyzer.print_planet_info(args.planet_info)

def run_goldilocks_planet(args):
    """whaaaat more docstrings???"""
    if verify_name_in_database(args.goldilocks_planet):
        goldilocks_determiner = Goldilocks_Determiner(exoplanet_data)
        goldilocks_determiner.print_goldilocks_zone(args.goldilocks_planet)

def run_habitable_planets():
    """"nope i give up on docstrings"""
    habitable_finder = Habitable_Finder(exoplanet_data)
    habitable_finder.print_habitable_list()

def main():
    """I refactored this so its now in more functions, yay"""
    args = parse_command_line()

    if args.planet_info:
        run_planet_info(args)
    elif args.goldilocks_planet:
        run_goldilocks_planet(args)
    elif args.habitable_planets:
        run_habitable_planets()

if __name__ == "__main__":
    main()
