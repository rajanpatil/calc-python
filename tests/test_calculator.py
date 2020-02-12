from calc.calculator import Calculator


def test_add_2_and_3():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_6_and_8():
    calc = Calculator()
    assert calc.add(6, 8) == 14
