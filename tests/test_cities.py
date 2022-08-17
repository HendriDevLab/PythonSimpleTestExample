import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
 
# importing
import unittest
from functions.city_functions import get_city_country_formatted

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_city_country = get_city_country_formatted('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_city_country = get_city_country_formatted('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
