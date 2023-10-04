import unittest
#TESTS NOT COPMPLETE IN THIS FILE
from ProductionCode.HabitablePlanets import Habitable_Finder

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

def test_habitatability_feature(self):
    habitable_planets
    


