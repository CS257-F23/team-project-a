import subprocess
import unittest


from cl import *

class TestPlanetMethods(unittest.TestCase):

    def test_run_planet_info_valid(self):
        """
        Test that the command line method for planet info prints planet info
        for an inputted planet present in the data set
        """
        code = subprocess.Popen(['python3', '-u', "cl.py", '--planet_info', '11 Com b'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn('11 Com b', output.strip())



    def test_run_planet_info_invalid_string(self):
        """
        Test that the command line method for planet info prints the correct error message
        for an inputted planet not present in the data set
        """
        code = subprocess.Popen(['python3', '-u', "cl.py", '--planet_info', "FAKEPLANET"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()


    def test_run_planet_info_special_char(self):
        """
        Test that the command line method for planet info prints the correct error message
        for an inputted arbitrary string of special characters
        """
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        code = subprocess.Popen(['python3', '-u', "cl.py", '--planet_info', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()

    def test_run_planet_info_whitespaces(self):
        """
        Test that the command line method for planet info prints the correct error message
        for an inputted string of blank spaces
        """
        code = subprocess.Popen(['python3', '-u', "cl.py", '--planet_info', "       "],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()

    def test_run_goldilocks_planet_inside(self):
        """
        Test that the command line method for goldilocks planet prints that the 
        inputted planet is in the Goldilocks Zone for a planet that 
        is in the data set and the Goldilocks Zone
        """
        planet_name = "ups And d"
        code = subprocess.Popen(['python3', '-u', "cl.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), planet_name + " is in the goldilocks zone! (by Solar Equivalent AU)")
        code.terminate()


    def test_run_goldilocks_planet_outside(self):
        """
        Test that the command line method for goldilocks planet prints that the 
        inputted planet is not in the Goldilocks Zone for a planet that 
        is in the data set and not the Goldilocks Zone
        """
        planet_name = "Kepler-1777 b" 
        code = subprocess.Popen(['python3', '-u', "cl.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), planet_name + " is not in the goldilocks zone (by Solar Equivalent AU).")
        code.terminate()

    def test_run_goldilocks_planet_invaild(self):
        """
        Test that the command line method for goldilocks planet prints the correct error message
        for an inputted planet not present in the data set
        """
        planet_name = "FAKEPLANET"
        code = subprocess.Popen(['python3', '-u', "cl.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "No data available for desired planet")
        code.terminate()

    def test_run_habitable_planets(self):
        """
        Test that the command line method for habitable prints a 
        string of planets that are in the Goldilocks Zone
        """
        code = subprocess.Popen(['python3', '-u', "cl.py", '--habitable'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = code.communicate() 
        self.assertIn("TRAPPIST-1 e", output.strip())
        code.terminate()


        
