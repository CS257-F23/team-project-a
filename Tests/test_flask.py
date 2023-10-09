from app import *
import unittest

# This should be modfied for our team flask app!

class TestHomepage(unittest.TestCase):
    def test_route(self):
        """Tests that the homepage route gives the correct string"""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"Welcome to the exoplanet project! To look up planet info, use /planet_info/planet_name and to check goldilocks zone use /goldilocks_planet/planet_name", response.data)

class TestPlanetInfo(unittest.TestCase):
    def test_14_Her_b_info_route(self):
        """Test that using 14 Her b with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/14 Her b', follow_redirects=True)
        self.assertEqual(b'Planet Info \n\nPlanet Name: 14 Her b\nHost Name: 14 Her\nNumber of Stars: 1\nNumber of Planets: 2\nNumber of Moons: 0\nDiscovery Method: Radial Velocity\nDiscovery Year: 2002\nDiscovery Facility: W. M. Keck Observatory\nSemi-Major Axis: 2.774000\nPlanet Radius: 12.600\nPlanet Mass: 2559.47216\nStellar Radius: 0.93\nStellar Mass: 0.91\nStellar Luminosity: -0.153\nGalactic Latitude: 46.94447\nGalactic Longitude: 69.16849\n', response.data)
    
    def test_ups_And_d_info_route(self):
        """Test that using ups And d with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/ups And d', follow_redirects=True)
        self.assertEqual(b'Planet Info \n\nPlanet Name: ups And d\nHost Name: ups And\nNumber of Stars: 2\nNumber of Planets: 3\nNumber of Moons: 0\nDiscovery Method: Radial Velocity\nDiscovery Year: 1999\nDiscovery Facility: Multiple Observatories\nSemi-Major Axis: 2.513290\nPlanet Radius: 12.500\nPlanet Mass: 3257.74117\nStellar Radius: 1.56\nStellar Mass: 1.30\nStellar Luminosity: 0.525\nGalactic Latitude: -20.66791\nGalactic Longitude: 132.00045\n', response.data)

class TestGoldilocksPlanet(unittest.TestCase):
    def test_14_Her_b_goldilocks_route(self):
        """Test that using 14 Her b with the goldilocks_planet route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/goldilocks_planet/14 Her b', follow_redirects=True)
        self.assertEqual(b'14 Her b is not in the goldilocks zone (by Solar Equivalent AU).', response.data)
    
    def test_ups_And_d_goldilocks_route(self):
        """Test that using ups And d with the goldilocks_planet route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/goldilocks_planet/ups And d', follow_redirects=True)
        self.assertEqual(b'ups And d is in the goldilocks zone! (by Solar Equivalent AU)', response.data)


if __name__ == '__main__':
    unittest.main()