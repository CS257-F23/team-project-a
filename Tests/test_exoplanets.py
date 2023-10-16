import subprocess
import unittest
import sys

sys.path.append("ProductionCode/")


from ProductionCode.exoplanets import *

class TestPlanetMethods(unittest.TestCase):

    def test_run_planet_info_valid(self):
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--planet_info', '11 Com b'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn('11 Com b', output.strip())



    def test_run_planet_info_invalid_string(self):
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--planet_info', "FAKEPLANET"],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()


    def test_run_planet_info_special_char(self):
        #test function's capcity to handle strings w/ special characters
        planet_name = "!@#$%^&*()"
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--planet_info', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()

    def test_run_planet_info_whitespaces(self):
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--planet_info', "       "],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        expected_error_message = "No data available for desired planet\n"
        self.assertEqual(output, expected_error_message)
        code.terminate()

    def test_run_goldilocks_planet_inside(self):
        planet_name = "ups And d"
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), planet_name + " is in the goldilocks zone! (by Solar Equivalent AU)")
        code.terminate()


    def test_run_goldilocks_planet_outside(self):
        planet_name = "Kepler-1777 b" 
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), planet_name + " is not in the goldilocks zone (by Solar Equivalent AU).")
        code.terminate()

    def test_run_goldilocks_planet_invaild(self):
        planet_name = "FAKEPLANET"
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--goldilocks_planet', planet_name],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "No data available for desired planet")
        code.terminate()

    def test_run_habitable_planets(self):
        code = subprocess.Popen(['python3', '-u', "ProductionCode/exoplanets.py", '--habitable'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = code.communicate() 
        self.assertIn("TRAPPIST-1 e", output.strip())
        code.terminate()


        
