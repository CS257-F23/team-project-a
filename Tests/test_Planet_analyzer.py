import unittest
import sys
sys.path.append("ProductionCode/")

from ProductionCode.PlanetAnalyzer import exoplanetAnalyzer
from ProductionCode.exoplanets import take_exoplanet_data


class TestGetPlanetInfo(unittest.TestCase):

    def setUp(self):
        self.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        self.analyzer = exoplanetAnalyzer(self.data)

    def test_get_info_valid(self):
        planet_name = "11 Com b"
        result = self.analyzer.get_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_get_info_invalid(self):
        planet_name = "FAKEPLANET"
        self.assertRaises(KeyError, self.analyzer.get_planet_info, planet_name)

    def test_get_info_string(self):
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        self.assertRaises(KeyError, self.analyzer.get_planet_info, planet_name)

    def test_get_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        self.assertRaises(KeyError, self.analyzer.get_planet_info, planet_name)

    def test_get_info_none(self):   
        self.assertRaises(KeyError, self.analyzer.get_planet_info, None)

    def test_get_info_empty(self):
        self.assertRaises(KeyError, self.analyzer.get_planet_info, "")

    def test_get_info_non_string(self):
        self.assertRaises(KeyError, self.analyzer.get_planet_info, 354)

    def test_get_info_whitespaces(self):
        self.assertRaises(KeyError, self.analyzer.get_planet_info, "       ")


class TestFormatPlanetInfo(unittest.TestCase):

    def setUp(self):
        self.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        self.analyzer = exoplanetAnalyzer(self.data)

    def test_format_info_valid(self):
        planet_name = "11 Com b"
        result = self.analyzer.format_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_format_info_invalid(self):
        planet_name = "FAKEPLANET"
        self.assertRaises(IndexError, self.analyzer.format_planet_info, planet_name)

    def test_format_info_string(self):
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        self.assertRaises(IndexError, self.analyzer.format_planet_info, planet_name)

    def test_format_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        self.assertRaises(IndexError, self.analyzer.format_planet_info, planet_name)

    def test_format_info_none(self):   
        self.assertRaises(TypeError, self.analyzer.format_planet_info, None)

    def test_format_info_empty(self):
        self.assertRaises(IndexError, self.analyzer.format_planet_info, "")

    def test_format_info_non_string(self):
        self.assertRaises(TypeError, self.analyzer.format_planet_info, 972)

    def test_format_info_whitespaces(self):
        self.assertRaises(IndexError, self.analyzer.format_planet_info, "      ")

class TestGetFormattedInfo(unittest.TestCase):

    def setUp(self):
        self.data = take_exoplanet_data('Data/ExoplanetSimplifiedData.csv')
        self.analyzer = exoplanetAnalyzer(self.data)

    def test_get_formatted_info_valid(self):
        planet_name = "11 Com b"
        result = self.analyzer.get_formatted_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_get_formatted_info_invalid(self):
        planet_name = "FAKEPLANET"
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, planet_name)

    def test_get_formatted_info_string(self):
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, planet_name)

    def test_get_formatted_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, planet_name)

    def test_get_formatted_info_none(self):  
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, None)

    def test_get_formatted_info_empty(self):
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, "")

    def test_get_formatted_info_non_string(self):
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, 586)

    def test_get_formatted_info_whitespaces(self):
        self.assertRaises(KeyError, self.analyzer.get_formatted_planet_info, "      ")
