"""

This is a submodule living inside subpackage1.

"""

import os


def my_method1(p):
    """
    This is the doctring used on subpackage1. It has nothing to do with the `rtd_test.greet_people` module.

    Parameters
    ----------
        p : str
            I have no idea why this should be a string.
    """
    return p * 5


def my_method2(o):
    """
    This is anoooother doctring of a method living inside package1. Why? Just because I wanted to have more than one.

    Parameters
    ----------
        o : int
            Note that this parameter should be a string because it wanted to be different.

    Returns
    -------
        Five times 'o'
    """
    return 5 * o


class MyClass:
    """
    A dummy class with no contructor.
    """
    def __init__(self):
        self.my_attribute = None

    def public_method(self, an_int_number):
        """
        And I am doing all this to simulate a complete package. Seems boring but makes me understand it easier.

        Parameters
        ----------
            an_int_number : bool
                This is a bad variable name
        """
        self.my_attribute = an_int_number
