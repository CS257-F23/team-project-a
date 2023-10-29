import unittest
from ProductionCode.datasource import DataSource
from ProductionCode.Goldilocks import Goldilocks_Determiner

class TestGoldilocks(unittest.TestCase):
    def setUp(self):
        """
        Creates a Goldilocks Determiner filled with data on which tests
        can be run
        """
        self.data = DataSource()
        self.determiner = Goldilocks_Determiner(self.data)
    
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
        planet_name = "CI Tau b"
        det_sm = self.determiner.get_sm_axis(planet_name)
        self.assertEqual(det_sm, -1)

    def test_det_gold_inner_valid(self):
        """
        Test that inputting a planet that has data for stellar luminosity
        into determine_goldilocks_inner returns the correctly computed inner bound
        """
        # example from https://www.planetarybiology.com/calculating_habitable_zone.html
        planet_name = "Kepler-22 b"
        #using rounding equals because no websites report as many sig figs
        self.assertEqual(round(self.determiner.determine_goldilocks_inner(planet_name), 2), 0.76)

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
        # example from https://www.planetarybiology.com/calculating_habitable_zone.html
        planet_name = "Kepler-22 b"
        #using rounding equals because no websites report as many sig figs
        self.assertEqual(round(self.determiner.determine_goldilocks_outer(planet_name), 1), 1.1)

    def test_det_gold_outer_invalid(self):
        """
        Test that inputting a planet that doesn't have any data for stellar luminosity
        into determine_goldilocks_outer returns the integer 0
        """
        #a planet which does not have this data should return 0 
        self.assertEqual(self.determiner.determine_goldilocks_inner("HIP 79098 AB b"), 0)
    
    
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

    # def test_something(self):
    #     """
    #     Test that inputting a planet with x info
    #     into some function returns whatever it should return
    #     """
    #     planet_name = ""
    #     self.assertEqual(self.determiner.function(planet_name), expected_return)

# TO TEST: 
#          get_goldilocks_zone: 2 cases (in & out)
#          create_habitable_list: 2 cases, in and out
#          print_habitable_list: 2 cases, in and out



