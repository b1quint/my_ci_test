"""

Within this module, I intent to save one class and on method that will be use to salute people. Why? Just for testing
the Read The Docs. Judge me.

"""


def say_hello(name):
    """
    A dummy method used to say Hello World to someone.

    Parameters
    ----------
        name : str
            The name of the person that you want to salute.
    """
    print("Hello {:s}".format(name))


class GreetingRobot:
    """
    This is a very sympathetic robot that salutes people and introduces itself.

    Parameters
    ----------
        name : str
            The robot's name. It uses it to introduce itself. How polite...
    """
    def __init__(self, name):
        self.name

    def greet(self):
        """
        This is when our polite robot introduces itself.
        """
        print("Hi! My name is {:s}".format(self.name))
