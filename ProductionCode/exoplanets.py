from load_data import take_exoplanet_data
from commandInterpret import Command_line_interpreter

if __name__ == "__main__" :
    #test stuff
    #exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    #exo_analyzer = exoplanetAnalyzer(exoplanetDictionary)
    #gold_det = Goldilocks_Determiner(exoplanetDictionary)
    #hab_finder = Habitable_Finder(exoplanetDictionary)
    #exo_analyzer.print_planet_info('WASP-41 c')
    #gold_det.print_goldilocks_zone('14 Her b')
    #hab_finder.print_habitable_list()
    exoplanetDictionary = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
    command_line_interpreter = Command_line_interpreter(exoplanetDictionary)
    command_line_interpreter.run_specified_arg()