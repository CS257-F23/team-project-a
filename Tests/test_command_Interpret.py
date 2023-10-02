import unittest
from commandInterpret import Command_line_interpreter
from load_data import take_exoplanet_data

class TestCommandLineInterpreter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        cls.cli = Command_line_interpreter(cls.data)


    def test_run_planet_info_valid(self):
        planet_name = "Earth"
        result = self.cli.run_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_run_planet_info_invalid(self):
        planet_name = "FAKEPLANET"
        result = self.cli.run_planet_info(planet_name)
        expected_error_message = f"No data available for desried planet"
        self.assertEqual(result, expected_error_message)



    def test_run_habitable_planets(self):
        planet_name

    def test_run_goldilocks_planet_outside(self):

    def test_run_goldilocks_planet_insde(self):

    def test_run_goldoilocks_planet_invaild(self):
        planet_name = "FAKEPLANET"
        result = self.capture_output(self.cli.run_goldilocks_planet, planet)
        expected_error_message = "No data available for desired planet"
    
    def test_run_specified_arg
        
        

