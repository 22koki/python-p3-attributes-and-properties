# lib/testing/person_test.py

import io
import sys
import unittest
from lib.person import Person

class TestPerson(unittest.TestCase):
    '''Person in person.py'''

    # ... other test cases ...

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        expected_output = "Name must be a string under 25 characters.\n"
        self.assertIn(expected_output, captured_out.getvalue())

    # ... other test cases ...
