import sys
from exoplanets import exoplanetAnalyzer, Goldilocks_Determiner, take_exoplanet_data


def run_planet_info(planet_name, exoplanetDictionary):
    exoplanetFinder = exoplanetAnalyzer(exoplanetDictionary)
    exoplanetFinder.print_planet_info(planet_name)

def run_goldilocks_planet(planet_name, exoplanetDictionary):
    goldilocks = Goldilocks_Determiner(exoplanetDictionary)
    goldilocks.is_in_goldilocks_zone(planet_name)

def main():
    exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    function_to_run = sys.argv[1]
    if function_to_run == "--planet_info":
        run_planet_info(sys.argv[2], exoplanetDictionary)

    elif function_to_run == "--goldilocks_planet":
        print(run_goldilocks_planet(sys.argv[2], exoplanetDictionary))

    else:
        print("exoplanet.py Usage: usage statement")


if __name__ == "__main__":
    main()
