from calc.calculator import Calculator
import pytest


class TestCalculator:

    def setup(self):
        self.calc = Calculator()

    def test_addition_2_plus_3(self):
        assert self.calc.add(2, 3) == 5

    def test_addition_6_plus_8(self):
        assert self.calc.add(6, 8) == 14

    def test_subtraction_4_minus_3(self):
        assert self.calc.sub(4, 3) == 1

    def test_subtraction_9_minus_2(self):
        assert self.calc.sub(9, 2) == 7

    def test_division_9_divide_by_3(self):
        assert self.calc.div(9, 3) == 3

    def test_division_error_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(5, 0)
