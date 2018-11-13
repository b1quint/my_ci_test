import unittest
import io
import sys

from ..greet_people import say_hello


class TestGreetPeople(unittest.TestCase):

    def test_say_hello(self):

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        say_hello('Stranger')  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual('Hello Stranger', capturedOutput.getvalue())

