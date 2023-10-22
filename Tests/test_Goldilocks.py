import unittest
from ProductionCode.Exoplanet_Data_Loader import data_loader
from ProductionCode.Goldilocks import Goldilocks_Determiner

class TestGoldilocks(unittest.TestCase):
    def setUp(self):
        self.data = data_loader('Data/ExoplanetSimplifiedData.csv')
        self.determiner = Goldilocks_Determiner(self.data.exoplanetsByName)
    
    def test_get_stellar_lum_valid1(self):
        self.assertEqual()
    
    def test_get_stellar_lum_valid2(self):
        self.assertEqual()

    def test_get_stellar_lum_invalid(self):
        #a planet which does not have this data should return 0 
        self.assertEqual()

    def test_get_sm_axis_valid1(self):
        self.assertEqual()
    
    def test_get_sm_axis_valid2(self):
        self.assertEqual()

    def test_get_sm_axis_invalid(self):
        #a planet which does not have this data should return -1
        self.assertEqual()

    def test_det_gold_inner_valid(self):
        #example taken from /website/
        self.assertEqual()

    def test_det_gold_inner_invalid(self):
        #a planet which does not have this data should return 0 
        self.assertEqual()

    def test_det_gold_outer_valid(self):
        #example taken from /website/
        self.assertEqual()

    def test_det_gold_outer_invalid(self):
        #a planet which does not have this data should return 0 
        self.assertEqual()

# TO TEST: 
#          is_in_goldilocks_zone: 2 cases (in & out), 1 edge (need more info)
#          get_goldilocks_zone: 2 cases (in & out)
#          create_habitable_list: 2 cases, in and out
#          print_habitable_list: 2 cases, in and out

# Notes: possibly run google search on all planets found using habitable?
#           (remember to check if the Solar Equiv. AU method says it is goldilocks)


