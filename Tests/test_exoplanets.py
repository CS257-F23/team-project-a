import subprocess
import unittest
from ProductionCode.load_data import take_exoplanet_data
from ProductionCode.exoplanets import *


class TestPlanetMethods(unittest.TestCase):

    def setUp(self):
        self.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')

    def test_run_planet_info_valid(self):
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--planet_info', '11 Com b'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = code.communicate() 
        self.assertIn('11 Com b', output.strip())

    def test_run_planet_info_invalid(self):
        planet_name = "FAKEPLANET"
        result = run_planet_info(planet_name)
        expected_error_message = f"No data available for desried planet"
        self.assert(result, expected_error_message)

    def test_run_planet_info_string(self):
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        result = run_planet_info(planet_name)
        expected_error_message = f"No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        result = run_planet_info(planet_name)
        expected_error_message = f"No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_none(self):   
        result = run_planet_info(None)
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_empty(self):
        result = run_planet_info("")
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_non_string(self):
        result = run_planet_info(354)
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_planet_info_whitespaces(self):
        result = run_planet_info("       ")
        expected_error_message = f'No data available for desired planet'
        self.assertEqual(result, expected_error_message)

    def test_run_goldilocks_planet_inside(self):
        planet_name = "Kepler-186 f"
        result = run_goldilocks_planet(planet_name)
        self.assertEqual(result, "Planet is inside the goldilocks zone")

    def test_run_goldilocks_planet_outsde(self):
        planet_name = "Kepler-1777 b" 
        result = run_goldilocks_planet(planet_name)
        self.assertEqual(result, "Planet is outside the goldilocks zone")

    def test_run_goldilocks_planet_invaild(self):
        planet_name = "FAKEPLANET"
        result = self.capture_output(run_goldilocks_planet, planet_name)
        expected_error_message = "No data available for desired planet"
        self.assertEqual(result, expected_error_message)

    def test_run_habitable_planets(self):
        result = run_habitable_planets()
        self.assertIsInstance(result, list)

    def test_extract_info_and_goldilocks_intergration(self):
        planet_name = "Kepler-186 f"
        info_result = self.chi.run_planet_info(planet_name)
        self.assertIn(planet_name, info_result)
        goldilocks_status = run_goldilocks_planet(planet_name)
        self.assertEqual(goldilocks_status, "Planet is inside the goldilocks zone")
        
