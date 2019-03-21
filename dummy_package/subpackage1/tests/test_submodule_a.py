
from dummy_package.subpackage1 import submoduleA


def test_my_method_1():

    my_string = 's'
    my_result = submoduleA.my_method1(my_string)

    assert my_result == my_string * 5
    assert False


def test_my_method_2():

    my_string = 's'
    my_results = submoduleA.my_method2(my_string)

    assert my_results == my_string * 5

