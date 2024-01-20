import pytest
from stack import calc_postfix
from stack import convert_infix_to_postfix
from calculator_exception import CalculationError


def calculate(equation: str) -> float:
    return calc_postfix(convert_infix_to_postfix(equation))


def test_syntax_1():
    with pytest.raises(ValueError):
        calculate("5!^4^")


def test_syntax_2():
    with pytest.raises(ValueError):
        calculate("-~-5")


def test_syntax_3():
    with pytest.raises(ValueError):
        calculate("()")


def test_syntax_4():
    with pytest.raises(ValueError):
        calculate("7^4.%!")


def test_syntax_5():
    with pytest.raises(ValueError):
        calculate("12*(24!))")


def test_syntax_6():
    with pytest.raises(ValueError):
        calculate("")


def test_syntax_7():
    with pytest.raises(ValueError):
        calculate("         ")


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


def test_equation_1():
    assert calculate("~(5.2$3.8)*(4.1^2)+6.9*2.3^3+1.7+789.6#") == 28.2403



def test_equation_2():
    assert calculate("(-4)^2+(8/2)*(1 + 3)-5* 2") == 22.0


def test_equation_3():
    assert calculate("6!*(2 + 10)/2 +(5^2-10) + 3!") == 4341.0


def test_equation_4():
    assert calculate("((15 % 4)*3)^2-7*(4/2)+10/2") == 72.0


def test_equation_5():
    assert calculate("(8.5^2-5.2*-(3.7@2)+~-4.3+6.0!/123.9)*2.4") == 233.2347312348



def test_equation_6():
    assert calculate("~(5 * 2)@3 + 4!/2-1+(-2)^2") == 11.5


def test_equation_7():
    assert calculate("4! + 2 * (5 - 3^2) + (4 * 2 - 1) - 3!") == 17.0


def test_equation_8():
    assert calculate("10/(2 + 3)$3 + (3^2! - 1) + 4/2@4") == 11.3333333333


def test_equation_9():
    assert calculate("15%(4^2)-7$3-~-2!^3+5") == 5.0


def test_equation_10():
    assert calculate("(8^2-5*-(3@2)+~-4+6!)/2") == 400.25


def test_equation_11():
    assert calculate("(~-3 -2  $4)*-5-6^2+-1") == -32.0


def test_equation_12():
    assert calculate("10^2/-2+~-4*-(3&-2)+5!") == 78.0


def test_equation_13():
    assert calculate("(~-6$-3)*-4+-2^3--7/2+-1") == -29.5


def test_equation_14():
    assert calculate("15%(4^--1)-7$3!!#-~-2") == -8.0


def test_equation_15():
    assert calculate("((3&-6 + 4)$8)-(2^2+1)+5") == 8.0


def test_equation_16():
    assert calculate("(10+5)*2 / (3---1)+4!-2") == 37.0


def test_equation_17():
    assert calculate("12.3%4.1+-6.2*---3.7^2-(-4.9$2.1)+(999.3)#") == -49.978
