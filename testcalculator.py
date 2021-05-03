import pytest
import pythoncalculator

from calculatorfunc import *
#from com.automationpanda.example.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0


def test_subtract():
    value = sub(NUMBER_1, NUMBER_2)
    assert value == 1.0




def test_multiply():
    value = mult(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    value = div(NUMBER_1, NUMBER_2)
    assert value == 1.5