import pytest
from stack import calc_postfix
from stack import convert_infix_to_postfix
from calculator_exception import CalculationError


def calculate(equation: str) -> float:
    return calc_postfix(convert_infix_to_postfix(equation))


@pytest.mark.parametrize("equation, error", [
    ("5!^4^", ValueError),
    ("-~-5", ValueError),
    ("()", ValueError),
    ("7^4.%!", ValueError),
    ("12*(24!))", ValueError),
    ("", ValueError),
    ("         ", ValueError),
])
def test_syntax(equation, error):
    with pytest.raises(error):
        calculate(equation)


def test_operators_addition():
    assert calculate("5+6") == 11.0


def test_operators_subtraction():
    assert calculate("8.5-3") == 5.5


def test_operators_power():
    assert calculate("2^3") == 8.0
    with pytest.raises(CalculationError):
        calculate("(-2)^0.6")
        calculate("0^~5")
        calculate("~5^0.1")


def test_operators_division():
    assert calculate("10/2") == 5.0
    with pytest.raises(CalculationError):
        calculate("-2/0")


def test_operators_multiply():
    assert calculate("5*6") == 30.0


def test_operators_factorial():
    assert calculate("4!") == 24.0


def test_operators_maximum():
    assert calculate("5$6") == 6.0


def test_operators_minimum():
    assert calculate("5&6") == 5.0


def test_operators_modulo():
    assert calculate("7%2") == 1.0
    with pytest.raises(CalculationError):
        calculate("6%0")


def test_operators_average():
    assert calculate("5@6") == 5.5


def test_operators_negativity():
    assert calculate("~5") == -5.0


def test_operators_digits_sum():
    assert calculate("12.3#") == 6.0


@pytest.mark.parametrize("equation, answer", [
    ("~(5.2$3.8)*(4.1^2)+6.9*2.3^3+1.7+789.6#", 28.2403),
    ("(-4)^2+(8/2)*(1 + 3)-5* 2", 22.0),
    ("6!*(2 + 10)/2 +(5^2-10) + 3!", 4341.0),
    ("((15 % 4)*3)^2-7*(4/2)+10/2", 72.0),
    ("(8.5^2-5.2*-(3.7@2)+~-4.3+6.0!/123.9)*2.4", 233.2347312348),
    ("~(5 * 2)@3 + 4!/2-1+(-2)^2", 11.5),
    ("4! + 2 * (5 - 3^2) + (4 * 2 - 1) - 3!", 17.0),
    ("10/(2 + 3)$3 + (3^2! - 1) + 4/2@4", 11.3333333333),
    ("15%(4^2)-7$3-~-2!^3+5", 5.0),
    ("(8^2-5*-(3@2)+~-4+6!)/2", 400.25),
    ("(~-3 -2  $4)*-5-6^2+-1", -32.0),
    ("10^2/-2+~-4*-(3&-2)+5!", 78.0),
    ("(~-6$-3)*-4+-2^3--7/2+(---1)", -29.5),
    ("15%(4^--1)-7$3!!#-~-2", -8.0),
    ("((3&-6 + 4)$8)-(2^2+1)+5", 8.0),
    ("(10+5)*2 / (3---1)+4!-2", 37.0),
    ("12.3%4.1+-6.2*---3.7^2-(-4.9$2.1)+(999.3)#", -49.978),
])
def test_equations(equation, answer):
    assert calculate(equation) == answer
