import argparse
from Goldilocks import Goldilocks_Determiner
from HabitablePlanets import Habitable_Finder
from PlanetAnalyzer import exoplanetAnalyzer
from load_data import take_exoplanet_data
# -*- coding: utf-8 -*-


def main():
    parser = argparse.ArgumentParser(description='Exoplanet Data Analyzer')

    #look up info about an exoplanet by its name
    parser.add_argument('--planet_info', metavar='Planet Name', type=str,
                        help='Look up info about an exoplanet by its name')

    #get a list of planets between X and Y astronomical units away from Earth
    parser.add_argument('--distance_range_from_Earth', metavar=('Low', 'High'), nargs=2,
                        type=str, help='Get a list of planets between X and Y astronomical units away from Earth')

    # look up whether that planet is a goldilocks "planet" (in its star's habitable zone) or not
    parser.add_argument('--goldilocks_planet', metavar='Planet Name', type=str,
                    help='Look up whether that planet is a goldilocks planet (in its star\'s habitable zone) or not')

    #get a list of planets in the habitable zone
    parser.add_argument('--habitable_planets', action='store_true',
                        help='Get a list of planets in the habitable zone')

    args = parser.parse_args()

    exoplanet_data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')

    if args.planet_info:
        exo_analyzer = exoplanetAnalyzer(exoplanet_data)
        exo_analyzer.print_planet_info(args.planet_info)
    elif args.goldilocks_planet:
        goldilocks_determiner = Goldilocks_Determiner(exoplanet_data)
        goldilocks_determiner.print_goldilocks_zone(args.goldilocks_planet)
    elif args.habitable_planets:
        habitable_finder = Habitable_Finder(exoplanet_data)
        habitable_finder.print_habitable_list()

if __name__ == "__main__":
    main()
