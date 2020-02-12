from calc.calculator import Calculator
import pytest


def test_add_2_plus_3():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_6_plus_8():
    calc = Calculator()
    assert calc.add(6, 8) == 14


def test_subtraction_4_minus_3():
    calc = Calculator()
    assert calc.sub(4, 3) == 1


def test_subtraction_9_minus_2():
    calc = Calculator()
    assert calc.sub(9, 2) == 7


def test_division_9_divide_by_3():
    calc = Calculator()

    assert calc.div(9, 3) == 3


def test_division_error_divide_by_zero():
    calc = Calculator()

    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)
