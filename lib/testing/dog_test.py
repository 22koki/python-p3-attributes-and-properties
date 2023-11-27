# lib/testing/dog_test.py

import io
import sys
import unittest
from lib.dog import Dog

class TestDog(unittest.TestCase):
    '''Dog in dog.py'''

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="")
        sys.stdout = sys.__stdout__
        print("Actual Output:", captured_out.getvalue())  # Add this line for debugging
