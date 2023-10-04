import unittest
import argparse
from Goldilocks import Goldilocks_Determiner
from HabitablePlanets import Habitable_Finder
from PlanetAnalyzer import exoplanetAnalyzer
from load_data import take_exoplanet_data

class TestCommandLineInterpreter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        cls.cli = Command_line_interpreter(cls.data)

    def test_default_intialization(self):
        cli = Command_line_interpreter()
        self.assertIsInstance(cli.exoplanetDictionary, dict)
        self.assertEqual(len(cli.exoplanetDictionary), 0, "should be empty")

    def test_initialization_with_dict(self):
        my_data = {
            "Planet1": {"info1": "data1", "info2": "data2"},
            "Planet2": {"info1": "data3", "info2": "data4"}
        }
        cli = Command_line_interpreter(my_data)
        self.assertEqual(cli.exoplanetDictionary, my_data, "dictionary should be equal to exoplanet Dictionry")


    def test_initialization_with_non_dict(self):
        #raise TypeError if any structure other than a dictionary is passed
        with self.assertRaises(TypeError):
            cli = Command_line_interpreter("Not a dictionary")

if __name__ == "__main__":
    unittest.main()

class TestPlanetMethods(unittest.TestCase):

    def setUp(self):
        self.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        self.cli = Command_line_interpreter(self.data)

    def test_run_planet_info_valid(self):
        planet_name = "11 Com b"
        result = self.cli.run_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_run_planet_info_invalid(self):
        planet_name = "FAKEPLANET"
        result = self.cli.run_planet_info(planet_name)
        expected_error_message = f"No data available for desried planet"
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_string(self):
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        result = self.cli.run_planet_info(planet_name)
        expected_error_message = f"No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        result = self.cli.run_planet_info(planet_name)
        expected_error_message = f"No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_none(self):   
        result = self.cli.run_planet_info(None)
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_empty(self):
        result = self.cli.run_planet_info("")
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_non_string(self):
        result = self.cli.run_planet_info(354)
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_whitespaces(self):
        result = self.cli.run_planet_info("       ")
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_goldilocks_planet_inside(self):
        planet_name = "Kepler-186 f"
        result = self.cli.run_goldilocks_planet(planet_name)
        self.assertEqual(result, "Planet is inside the goldilocks zone")

    def test_run_goldilocks_planet_outsde(self):
        planet_name = "Kepler-1777 b" 
        result = self.cli.run_goldilocks_planet(planet_name)
        self.assertEqual(result, "Planet is outside the goldilocks zone")

    def test_run_goldilocks_planet_invaild(self):
        planet_name = "FAKEPLANET"
        result = self.capture_output(self.cli.run_goldilocks_planet, planet_name)
        expected_error_message = "No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_habitable_planets(self):
        result = self.cli.run_habitable_planets()
        self.assertIsInstance(result, list)

    def test_extract_info_and_goldilocks_intergration(self):
        planet_name = "Kepler-186 f"
        info_result = self.chi.run_planet(planet_name)
        self.assertIn(planet_name, info_result)
        goldilocks_status = self.cli.run_goldilocks_planet(planet_name)
        info_result = self.chi.run_planet(goldilocks_status, "Planet is inside the goldilocks zone")
