import unittest

from ProductionCode.PlanetAnalyzer import exoplanetAnalyzer
from ProductionCode.datasource import DataSource

#TODO: test basic get and list get methods

class TestGetPlanetInfo(unittest.TestCase):

    def setUp(self):
        """
        Creates an Exoplanet Analyzer filled with data on which tests
        can be run
        """
        self.data = DataSource()
        self.analyzer = exoplanetAnalyzer(self.data)

    def test_get_info_valid(self):
        """
        Test that inputting a planet in the data set into get_planet_info returns info 
        about that planet. 
        """
        planet_name = "11 Com b"
        result = self.analyzer.get_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_get_info_invalid(self):
        """Test that inputting a planet not in the data set into get_planet_info returns None"""
        planet_name = "FAKEPLANET"
        result = self.analyzer.get_planet_info(planet_name)
        self.assertEqual(None, result)

    def test_get_info_string(self):
        """Test that inputting an arbitray string into get_planet_info returns None"""
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        result = self.analyzer.get_planet_info(planet_name)
        self.assertEqual(None, result)

    def test_get_info_special_char(self):
        """
        Test that inputting a funky string with special characters
        into get_planet_info returns None
        """
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        result = self.analyzer.get_planet_info(planet_name)
        self.assertEqual(None, result)

    def test_get_info_none(self):  
        """Test that inputting nothing into get_planet_info returns None"""
        planet_name = None 
        result = self.analyzer.get_planet_info(planet_name)
        self.assertEqual(None, result)

    def test_get_info_empty(self):
        """Test that inputting an empty string into get_planet_info returns None"""
        self.assertEqual(None, self.analyzer.get_planet_info(""))

    def test_get_info_non_string(self):
        """
        Test that inputting a non-string (specifically tested with an integer)
        into get_planet_info returns None
        """
        self.assertEqual(None, self.analyzer.get_planet_info(354))

    def test_get_info_whitespaces(self):
        """Test that inputting a string of blank spaces into get_planet_info returns None"""
        self.assertEqual(None, self.analyzer.get_planet_info("       "))


class TestGetFormattedPlanetInfo(unittest.TestCase):

    def setUp(self):
        """
        Creates an Exoplanet Analyzer filled with data on which tests
        can be run
        """
        self.data = DataSource()
        self.analyzer = exoplanetAnalyzer(self.data)

    def test_get_format_info_valid(self):
        """
        Test that inputting a planet in the data set into get_formatted_planet_info
        returns formatted info about that planet. 
        """
        planet_name = "14 Her b"
        result = self.analyzer.get_formatted_planet_info(planet_name)
        self.assertIn(planet_name, result)

    def test_get_format_info_invalid(self):
        """
        Test that inputting a planet not in the data set 
        into get_formatted_planet_info raises an error
        """
        planet_name = "FAKEPLANET"
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, planet_name)

    def test_get_format_info_special_char(self):
        """
        Test that inputting a funky string with special characters 
        into get_formatted_planet_info raises an error
        """
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, planet_name)

    def test_get_format_info_none(self):   
        """
        Test that inputting nothing 
        into get_formatted_planet_info raises an error
        """
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, None)

    def test_get_format_info_empty(self):
        """
        Test that inputting an empty string 
        into get_formatted_planet_info raises an error
        """
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, "")

    def test_get_format_info_non_string(self):
        """
        Test that inputting a non-string (specifically tested with an integer) 
        into get_formatted_planet_info raises an error
        """
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, 972)

    def test_get_format_info_whitespaces(self):
        """
        Test that inputting a string made up of a bunch of blank spaces 
        into get_formatted_planet_info raises an error
        """
        self.assertRaises(TypeError, self.analyzer.get_formatted_planet_info, "      ")


