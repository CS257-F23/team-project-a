#should test verify name in database, and maybe just check that a couple planets end up in the database it creates?
import unittest

from ProductionCode.datasource import DataSource


class TestDataLoader(unittest.TestCase):

    def setUp(self):
        """
        Creates an Exoplanet Analyzer filled with data on which tests
        can be run
        """
        self.data = DataSource()

    def test_verify_name_in_database_valid(self):
        """
        Test that inputting a planet that's in the data set into
        verity_name_in_database returns the boolean True
        """
        self.assertEqual(self.data.verify_name_in_database("14 Her b"), True)

    def test_verify_name_in_database_invalid(self):
        """
        Test that inputting a planet that's not in the data set into
        verity_name_in_database returns the boolean False
        """
        self.assertEqual(self.data.verify_name_in_database("Her 14 b"), False)
    
    
class TestGetPlanetInfo(unittest.TestCase):

    def setUp(self):
        """
        Creates an Exoplanet Analyzer filled with data on which tests
        can be run
        """
        self.dataSource = DataSource()

    def test_get_info_valid(self):
        """
        Test that inputting a planet in the data set into get_planet_info returns info 
        about that planet. 
        """
        planet_name = "11 Com b"
        result = self.dataSource.getPlanetInfo(planet_name)
        self.assertIn(planet_name, result)

    def test_get_info_invalid(self):
        """Test that inputting a planet not in the data set into get_planet_info returns None"""
        planet_name = "FAKEPLANET"
        result = self.dataSource.getPlanetInfo(planet_name)
        self.assertEqual(None, result)

    def test_get_info_string(self):
        """Test that inputting an arbitray string into get_planet_info returns None"""
        #test function's capactiy to handle random strings
        planet_name = "randomSTRINGNOTaPLANET"
        result = self.dataSource.getPlanetInfo(planet_name)
        self.assertEqual(None, result)

    def test_get_info_special_char(self):
        """
        Test that inputting a funky string with special characters
        into get_planet_info returns None
        """
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        result = self.dataSource.getPlanetInfo(planet_name)
        self.assertEqual(None, result)

    def test_get_info_none(self):  
        """Test that inputting nothing into get_planet_info returns None"""
        planet_name = None 
        result = self.dataSource.getPlanetInfo(planet_name)
        self.assertEqual(None, result)

    def test_get_info_empty(self):
        """Test that inputting an empty string into get_planet_info returns None"""
        self.assertEqual(None, self.dataSource.getPlanetInfo(""))

    def test_get_info_non_string(self):
        """
        Test that inputting a non-string (specifically tested with an integer)
        into get_planet_info returns None
        """
        self.assertEqual(None, self.dataSource.getPlanetInfo(354))

    def test_get_info_whitespaces(self):
        """Test that inputting a string of blank spaces into get_planet_info returns None"""
        self.assertEqual(None, self.dataSource.getPlanetInfo("       "))
