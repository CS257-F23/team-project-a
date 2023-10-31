import unittest
import math
from ProductionCode.Exoplanet_Data_Loader import data_loader
from ProductionCode.Goldilocks import Goldilocks_Determiner

class TestGoldilocks(unittest.TestCase):
    def setUp(self):
        """
        Creates a Goldilocks Determiner filled with data on which tests
        can be run
        """
        self.data = data_loader('Data/ExoplanetSimplifiedData.csv')
        self.determiner = Goldilocks_Determiner(self.data.exoplanetsByName)
    
    def test_get_stellar_lum_valid1(self):
        self.assertEqual(self.determiner.get_stellar_lum("14 And b"), 10 ** 1.840)

    def test_get_stellar_lum_invalid(self):
        """
        Test that inputting a planet that doesn't have any data for stellar luminosity
        into get_stellar_luminosity returns the integer 0
        """
        #a planet which does not have this data should return 0 
        self.assertEqual(self.determiner.get_stellar_lum("HIP 79098 AB b"), 0)

    def test_get_sm_axis_valid1(self):
        planet_name = "11 Com b"
        det_sm = self.determiner.get_sm_axis(planet_name)
        self.assertEqual(det_sm, 1.178000)

    def test_get_sm_axis_invalid(self):
        """
        Test that inputting a planet that doesn't have any data for sm axis
        into get_sm_axis returns the integer -1
        """
        #a planet which does not have this data should return -1
        self.assertEqual()

    def test_det_gold_inner_valid(self):
        """
        Test that inputting a planet that has data for stellar luminosity
        into determine_goldilocks_inner returns the corretly computed inner bound
        """
        #example taken from /website/
        self.assertEqual()

    def test_det_gold_inner_invalid(self):
        """
        Test that inputting a planet that doesn't have any data for stellar luminosity
        into determine_goldilocks_inner returns the integer 0
        """
        #a planet which does not have this data should return 0 
        self.assertEqual(self.determiner.determine_goldilocks_inner("HIP 79098 AB b"), 0)

    def test_det_gold_outer_valid(self):
        """
        Test that inputting a planet that has data for stellar luminosity
        into determine_goldilocks_outer returns the corretly computed outer bound
        """
        #example taken from /website/
        self.assertEqual()

    def test_det_gold_outer_invalid(self):
        """
        Test that inputting a planet that doesn't have any data for stellar luminosity
        into determine_goldilocks_outer returns the integer 0
        """
        #a planet which does not have this data should return 0 
        self.assertEqual(self.determiner.determine_goldilocks_outer("HIP 79098 AB b"), 0)
        
    def test_is_in_goldilocks_zone_true(self):
        """
        Test that inputting a planet which is calculated to be in the habitable zone
        into is_in_goldilocks_zone returns True
        """
        planet_name = "TRAPPIST-1 e"
        self.assertEqual(self.determiner.is_in_goldilocks_zone(planet_name), True)

    def test_is_in_goldilocks_zone_false(self):
        """
        Test that inputting a planet which is calculated to not be in the habitable zone
        into is_in_goldilocks_zone returns False
        """
        planet_name = "14 Her b"
        self.assertEqual(self.determiner.is_in_goldilocks_zone(planet_name), False)

    def test_is_in_goldilocks_zone_unclear(self):
        """
        Test that inputting a planet which is missing info
        into is_in_goldilocks_zone returns None
        """
        planet_name = "HIP 79098 AB b"
        self.assertEqual(self.determiner.is_in_goldilocks_zone(planet_name), None)
        
    def test_get_goldilocks_zone_true(self):
        """
        Test that inputting a planet inside the goldilocks zone
        into get_goldilocks_zone returns the correct string
        """
        planet_name = "ups And d"
        expected_return = 'ups And d is in the goldilocks zone! (by Solar Equivalent AU)'
        self.assertEqual(self.determiner.get_goldilocks_zone(planet_name), expected_return)

    def test_get_goldilocks_zone_false(self):
        """
        Test that inputting a planet outside the goldilocks zone
        into get_goldilocks_zone returns the correct string
        """
        planet_name = "tau Boo b"
        expected_return = 'tau Boo b is not in the goldilocks zone (by Solar Equivalent AU).'
        self.assertEqual(self.determiner.get_goldilocks_zone(planet_name), expected_return)
        
    def test_get_goldilocks_zone_unclear(self):
        """
        Test that inputting a planet with insufficient information
        into get_goldilocks_zone returns the correct string
        """
        planet_name = 'HIP 79098 AB b'
        expected_return = 'Unfortunately, the database does not contain sufficient information to determine if HIP 79098 AB b is in the goldilocks zone (by Solar Equivalent AU).'
        self.assertEqual(self.determiner.get_goldilocks_zone(planet_name), expected_return)
        
# TO TEST: 
#          create_habitable_list: 2 cases, in and out
#          print_habitable_list: 2 cases, in and out



