import argparse
from exoplanets import exoplanetAnalyzer, Goldilocks_Determiner, take_exoplanet_data


def main():
    parser = argparse.ArgumentParser(description='Exoplanet Data Analyzer')

    #look up info about an exoplanet by its name
    parser.add_argument('--planet_info', metavar='Planet Name', type=str,
                        help='Look up info about an exoplanet by its name')

    #get a list of planets between X and Y astronomical units away from Earth
    parser.add_argument('--distance_range_from_Earth', metavar=('Low', 'High'), nargs=2,
                        type=str, help='Get a list of planets between X and Y astronomical units away from Earth')

    #look up whether that planet is a goldilocks “planet” (in it’s star’s habitable zone) or not
    parser.add_argument('--goldilocks_planet', metavar='Planet Name', type=str,
                        help='Look up whether that planet is a goldilocks planet (in its star’s habitable zone) or not')

    #get a list of planets in the habitable zone
    parser.add_argument('--habitable_planets', action='store_true',
                        help='Get a list of planets in the habitable zone')

    args = parser.parse_args()

    if args.planet_info:
        exoplanetFinder.print_planet_info(args.planet_info)
    elif args.distance_range_from_Earth:
        pass
    elif args.goldilocks_planet:
        pass
    elif args.habitable_planets:
        pass

if __name__ == "__main__":
    main()
