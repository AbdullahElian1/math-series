from math_series.series import *
from math_series import __version__


def test_version():
    assert __version__ == '0.1.0'



def test_zero():
    expected=0

    actual=fibonacci_series(0)

    assert expected==actual

def test_one():
    expected=1

    actual=fibonacci_series(1)

    assert expected==actual

def test_seven():
    expected=13

    actual=fibonacci_series(7)

    assert expected==actual

def test_negative_number():
    expected= "enter positive number"

    actual=fibonacci_series(-7)

    assert expected==actual   


    # test for lucas_series

def test_zero_for_lucas():
    expected=2

    actual=lucas_numbers(0)

    assert expected==actual

def test_one_for_lucas():
    expected=1

    actual=lucas_numbers(1)

    assert expected==actual

def test_seven_for_lucas():
    expected=29

    actual=lucas_numbers(7)

    assert expected==actual

def test_negative_number_for_lucas():
    expected= "enter positive number"

    actual=lucas_numbers(-7)

    assert expected==actual  


# test for other series

def test_zero_for_other():
    expected=0

    actual=sum_series(0)

    assert expected==actual

def test_one_for_other():
    expected=3

    actual=sum_series(1,4,3)

    assert expected==actual

def test_seven_for_other():
    expected=137

    actual=sum_series(7,9,5)

    assert expected==actual

def test_negative_number_for_other():
    expected= "enter positive number"

    actual=sum_series(-7)

    assert expected==actual   


