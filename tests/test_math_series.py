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


    

