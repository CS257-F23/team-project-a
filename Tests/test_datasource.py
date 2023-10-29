#should test verify name in database, and maybe just check that a couple planets end up in the database it creates?
import unittest

from ProductionCode.datasource import DataSource


class TestDataLoader(unittest.TestCase):

    def setUp(self):
        """
        Creates an Exoplanet Analyzer filled with data on which tests
        can be run
        """
        self.data = DataSource()

    def test_verify_name_in_database_valid(self):
        """
        Test that inputting a planet that's in the data set into
        verity_name_in_database returns the boolean True
        """
        self.assertEqual(self.data.verify_name_in_database("14 Her b"), True)

    def test_verify_name_in_database_invalid(self):
        """
        Test that inputting a planet that's not in the data set into
        verity_name_in_database returns the boolean False
        """
        self.assertEqual(self.data.verify_name_in_database("Her 14 b"), False)
    