import unittest
import argparse
from Goldilocks import Goldilocks_Determiner
from HabitablePlanets import Habitable_Finder
from PlanetAnalyzer import exoplanetAnalyzer
from load_data import take_exoplanet_data


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
        info_result = self.chi.run_planet_info(planet_name)
        self.assertIn(planet_name, info_result)
        goldilocks_status = self.cli.run_goldilocks_planet(planet_name)
        self.assertEqual(goldilocks_status, "Planet is inside the goldilocks zone")
        
