import argparse
from ProductionCode.Goldilocks import Goldilocks_Determiner
from ProductionCode.PlanetAnalyzer import exoplanetAnalyzer
from ProductionCode.datasource import DataSource

# -*- coding: utf-8 -*-*

datasource = DataSource()

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

    # get a list of planets in the habitable zone
    parser.add_argument('--habitable_planets', action='store_true',
                        help='Get a list of planets in the habitable zone')

    return parser.parse_args()


def run_planet_info(planet_name):
    """
    Takes name of planet, if the given planet is the dataset, prints get_planet_info
    Param: string
    Returns: none
    """
    if datasource.verify_name_in_database(planet_name):
        exo_analyzer = exoplanetAnalyzer(datasource)
        print(exo_analyzer.get_formatted_planet_info(planet_name))
    else:
        print("No data available for desired planet")

def run_goldilocks_planet(planet_name):
    """
    Takes name of planet, if the given planet is the dataset, prints get_goldilocks_zone
    Param: string
    Returns: none
    """
    if datasource.verify_name_in_database(planet_name):
        goldilocks_determiner = Goldilocks_Determiner(datasource)
        result = goldilocks_determiner.get_goldilocks_zone(planet_name)
        print(result)
    else:
        print("No data available for desired planet")

def run_habitable_planets():
    """"
    Runs print_habitable_list
    Param: none
    Returns: none
    """
    datasource.printHabitablePlanetList()


def main():
    """Parses command line arguments and runs the correct function based on the given args"""
    args = parse_command_line()

    if args.planet_info:
        run_planet_info(args.planet_info)
    elif args.goldilocks_planet:
        run_goldilocks_planet(args.goldilocks_planet)
    elif args.habitable_planets:
        run_habitable_planets()
    else:
        print("usage: exoplanets.py [-h] [--planet_info Planet Name] [--goldilocks_planet Planet Name] [--habitable_planets]")


if __name__ == "__main__":
    main()