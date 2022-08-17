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

import unittest
from classes.employee import *

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    def setUp(self):
        self.employee = Employee('John', 'William', 48000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 53000)        

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 58000)

if __name__ == '__main__':
    unittest.main()


