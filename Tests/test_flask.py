import unittest
from app import *

class TestHomepage(unittest.TestCase):
    def test_route(self):
        """Test that the homepage route gives the correct string"""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Welcome to the Exoplanet Info Getter!", response.data)

class TestPlanetInfo(unittest.TestCase):
    def test_14_Her_b_info_route(self):
        """Test that using 14 Her b with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/14 Her b', follow_redirects=True)
        self.assertIn(b'Galactic Latitude: 46.94447', response.data)
    
    def test_ups_And_d_info_route(self):
        """Test that using ups And d with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/ups And d', follow_redirects=True)
        self.assertIn(b'Host Name: ups And', response.data)

class TestAbout(unittest.TestCase):
    def test_14_Her_b_info_route(self):
        """Test that the about route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/about', follow_redirects=True)
        self.assertIn(b'The exoplanet info getter supports the following functionality', response.data)





