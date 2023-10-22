import unittest
from app import *

class TestHomepage(unittest.TestCase):
    def test_route(self):
        """Test that the homepage route gives the correct string"""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Use underscores in place of spaces.", response.data)

class TestPlanetInfo(unittest.TestCase):
    def test_14_Her_b_info_route(self):
        """Test that using 14 Her b with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/14 Her b', follow_redirects=True)
        self.assertIn(b'Galactic Latitude: 46.94447<br>Galactic Longitude: 69.16849', response.data)
    
    def test_ups_And_d_info_route(self):
        """Test that using ups And d with the planet_info route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/planet_info/ups And d', follow_redirects=True)
        self.assertIn(b'Planet Name: ups And d<br>Host Name: ups And', response.data)

class TestGoldilocksPlanet(unittest.TestCase):
    def test_14_Her_b_goldilocks_route(self):
        """Test that using 14 Her b with the goldilocks_planet route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/check_goldilocks/14 Her b', follow_redirects=True)
        self.assertIn(b'14 Her b is not in the Goldilocks Zone. (by Solar Equivalent AU)', response.data)
        
    def test_ups_And_d_goldilocks_route(self):
        """Test that using ups And d with the goldilocks_planet route outputs the correct string"""
        self.app = app.test_client()
        response = self.app.get('/check_goldilocks/ups And d', follow_redirects=True)
        self.assertIn(b'ups And d is in the Goldilocks Zone! (by Solar Equivalent AU)', response.data)
class TestErrorMessages(unittest.TestCase):
    def test_404(self):
        """Test that the 404 message appears when a nonexistant url is entered."""
        self.app = app.test_client()
        response = self.app.get('/gildilicks_plinet/down_or_d', follow_redirects=True)
        self.assertIn(b'far out in space, buddy!', response.data)

if __name__ == '__main__':
    unittest.main()