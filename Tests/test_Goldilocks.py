# import unittest
# from ProductionCode.Exoplanet_Data_Loader import data_loader
# from ProductionCode.Goldilocks import Goldilocks_Determiner

# class TestGoldilocks(unittest.TestCase):
#     def setUp(self):
#         """
#         Creates a Goldilocks Determiner filled with data on which tests
#         can be run
#         """
#         self.data = data_loader('Data/ExoplanetSimplifiedData.csv')
#         self.determiner = Goldilocks_Determiner(self.data.exoplanetsByName)
    
#     def test_get_stellar_lum_valid1(self):
#         self.assertEqual()
    
#     def test_get_stellar_lum_invalid(self):
#         """
#         Test that inputting a planet that doesn't have any data for stellar luminosity
#         into get_stellar_luminosity returns the integer 0
#         """
#         #a planet which does not have this data should return 0 
#         self.assertEqual()

#     def test_get_sm_axis_valid1(self):
#         planet_name = "11 Com b"
#         det_sm = self.determiner.get_sm_axis(planet_name)
#         self.assertEqual(det_sm, 1.178000)

#     def test_get_sm_axis_invalid(self):
#         """
#         Test that inputting a planet that doesn't have any data for sm axis
#         into get_sm_axis returns the integer -1
#         """
#         #a planet which does not have this data should return -1
#         self.assertEqual()

#     def test_det_gold_inner_valid(self):
#         """
#         Test that inputting a planet that has data for stellar luminosity
#         into determine_goldilocks_inner returns the corretly computed inner bound
#         """
#         #example taken from /website/
#         self.assertEqual()

#     def test_det_gold_inner_invalid(self):
#         """
#         Test that inputting a planet that doesn't have any data for stellar luminosity
#         into determine_goldilocks_inner returns the integer 0
#         """
#         #a planet which does not have this data should return 0 
#         self.assertEqual()

#     def test_det_gold_outer_valid(self):
#         """
#         Test that inputting a planet that has data for stellar luminosity
#         into determine_goldilocks_outer returns the corretly computed outer bound
#         """
#         #example taken from /website/
#         self.assertEqual()

#     def test_det_gold_outer_invalid(self):
#         """
#         Test that inputting a planet that doesn't have any data for stellar luminosity
#         into determine_goldilocks_outer returns the integer 0
#         """
#         #a planet which does not have this data should return 0 
#         self.assertEqual()

# TO TEST: 
#          is_in_goldilocks_zone: 2 cases (in & out), 1 edge (need more info)
#          get_goldilocks_zone: 2 cases (in & out)
#          create_habitable_list: 2 cases, in and out
#          print_habitable_list: 2 cases, in and out



