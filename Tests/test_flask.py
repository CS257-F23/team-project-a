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
    def test_about_page(self):
        """Test that the about route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/about', follow_redirects=True)
        self.assertIn(b'The exoplanet info getter supports the following functionality', response.data)

class TestLearn(unittest.TestCase):
    def test_learn_page(self):
        """Test that the learn route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/learn', follow_redirects=True)
        self.assertIn(b'What is the Goldilocks Zone?', response.data)

class TestAvailable(unittest.TestCase):
    def test_available_page(self):
        """Test that the available_planets route contains a real planet"""
        self.app = app.test_client()
        response = self.app.get('/available_planets', follow_redirects=True)
        self.assertIn(b'24 Boo b', response.data)

class TestHabitable(unittest.TestCase):
    def test_habitable_page_valid(self):
        """Test that the habitable_planets route contains a habitable planet"""
        self.app = app.test_client()
        response = self.app.get('/habitable_planets', follow_redirects=True)
        self.assertIn(b'TRAPPIST-1 e', response.data)




