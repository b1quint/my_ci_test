import unittest
import io
import sys

from dummy_package import greet_people


class TestGreetPeople(unittest.TestCase):

    def test_say_hello(self):

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        greet_people.say_hello('Stranger')  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual('Hello Stranger', captured_output.getvalue().strip())

