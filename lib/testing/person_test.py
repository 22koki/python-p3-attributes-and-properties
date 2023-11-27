# lib/testing/person_test.py

import io
import sys
import unittest
from lib.person import Person

class TestPerson(unittest.TestCase):
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name="Guido", job="Engineer")
        self.assertEqual(type(guido), Person)

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        expected_output = "Name must be a string under 25 characters.\n"
        self.assertIn(expected_output, captured_out.getvalue())

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name=123, job="Teacher")
        sys.stdout = sys.__stdout__
        expected_output = "Name must be a string under 25 characters.\n"
        self.assertIn(expected_output, captured_out.getvalue())

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="What do people do on their day off? Can't lie around - that's their job.", job="Doctor")
        sys.stdout = sys.__stdout__
        expected_output = "Name must be a string under 25 characters.\n"
        self.assertIn(expected_output, captured_out.getvalue())

    def test_valid_name(self):
        '''saves name if string under 25 characters.'''
        alice = Person(name="Alice", job="Artist")
        self.assertEqual(alice.name, "Alice")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="Bob", job="Plumber")
        sys.stdout = sys.__stdout__
        expected_output = "Job must be in the list of approved jobs.\n"
        self.assertIn(expected_output, captured_out.getvalue())

    def test_job_in_list(self):
        '''saves job if in job list.'''
        bob = Person(name="Bob", job="Engineer")
        self.assertEqual(bob.job, "Engineer")

if __name__ == '__main__':
    unittest.main()
