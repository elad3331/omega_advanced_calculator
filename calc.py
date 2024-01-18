from math import pow
from calculator_exception import CalculationError


def power(num1: float, num2: float) -> float:
    """
    function that calcs power of numbers
    :param num1:
    :param num2:
    :return:
    """
    if num1 == 0 and num2 == 0:
        raise CalculationError("0^0 is undefined")
    elif num2 < 0 and -1 < num1 < 1 and num1 != 0:
        raise CalculationError("negative numbers cannot have square root")
    try:
        result = pow(num2, num1)
    except OverflowError:
        raise CalculationError("number too big - result is inf")
    return result


def division(num1, num2):
    """
    function that calcs division of two numbers
    :param num1: denominator
    :param num2: numerator
    :return: denominator/numerator
    :raise
    """
    if num1 == 0:
        raise CalculationError("division by 0 is undefined")
    return num2 / num1


def multiply(num1: float, num2: float) -> float:
    """
    calcs multiplication
    :param num1: first number
    :param num2: second number
    :return: the result of num1*num2
    """
    return num1 * num2


def addition(num1: float, num2: float) -> float:
    """
    calcs addition
    :param num1: first number
    :param num2: second number
    :return: the result of num1+num2
    """
    return num1 + num2


def subtraction(num1: float, num2: float) -> float:
    """
    calcs subtraction
    :param num1: first number
    :param num2: second number
    :return: the result of num2-num1
    """
    return num2 - num1


def minimum(num1: float, num2: float) -> float:
    """
    checks minimum of two numbers
    :param num1: first num to check
    :param num2: second num to check
    :return: the smaller num
    """
    if num1 < num2:
        return num1
    return num2


def maximum(num1: float, num2: float) -> float:
    """
    checks maximum of two numbers
    :param num1: first num to check
    :param num2: second num to check
    :return: the bigger num
    """
    if num1 > num2:
        return num1
    return num2


def factorial(num: int) -> int:
    """
    calculates factorial of given number
    :param num: int because only integer numbers have factorial
    :return: the factorial of this number
    :raises
    """
    result: int = 1
    if num < 0:
        raise CalculationError("factorial only for non negative numbers")
    if num * 10 % 10 != 0:
        raise CalculationError("factorial only for integer numbers")
    num = int(num)
    for i in range(1, num + 1):
        result *= i
    return result


def average(num1: float, num2: float) -> float:
    """
    calculates the average of two given numbers
    :param num1: first num
    :param num2: second num
    :return: their average
    """
    return (num1 + num2) / 2


def modulo(num1: float, num2: float) -> float:
    """

    :param num1:
    :param num2:
    :return:
    """
    return num2 % num1


def negativity(num1: float) -> float:
    """
    calcs negativity of given number
    :param num1: the number to calc
    :return: -num1
    """
    return -num1


def digits_sum(num1: float) -> int:
    if num1 < 0:
        raise CalculationError("# works only for positive numbers")
    sum_of_num = 0
    num1 = str(num1)
    for char in num1:
        if char.isdigit():
            sum_of_num += int(char)
    return sum_of_num


# dict of operators and their functions
"""
1 value: function
2 value: priority
3 value: pre operand, binary operand or post operand (1,2,3)

"""

OPERATORS = {"+": (addition, 1, 2),
             "-": (subtraction, 1, 2),
             "^": (power, 3, 2),
             "/": (division, 2, 2),
             "*": (multiply, 2, 2),
             "!": (factorial, 6, 3),
             "$": (maximum, 5, 2),
             "&": (minimum, 5, 2),
             "%": (modulo, 4, 2),
             "@": (average, 5, 2),
             '~': (negativity, 6, 1),
             '#': (digits_sum, 6, 3)}

OPERANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ")", "!", "#"]

PRE_OPERATOR_OPERANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "("]

OPEN_PARENTHESES = "("
CLOSER_PARENTHESES = ")"
def operator_priority(operator1: str, operator2: str) -> bool:
    """
    function that returns true if first's operator priority is greater than
    second's operator priority. Else returns false
    :param operator1: current operator in equation
    :param operator2: operator that is in the top of the stack
    :return: true or false
    """
    if OPERATORS[operator1][1] <= OPERATORS[operator2][1]:
        return True
    return False


def check_negativity(equation_list: list, index: int) -> tuple:
    """
    function that being called when there is ~ in equation
    :param equation_list:
    :param index:
    :return:
    """
    counter = 1
    index += 1
    try:
        char = equation_list[index]
    except IndexError:
        raise ValueError("equation cannot end with ~")
    while char == "-":
        counter += 1
        index += 1
        if index < len(equation_list):
            char = equation_list[index]
        else:
            raise ValueError("equation cannot end with -")
    if char not in PRE_OPERATOR_OPERANDS:
        raise ValueError("after ~ must come - or operand")
    index -= 1
    return counter, index


def check_minuses(equation_list: list, index: int):
    """
    function that being called when there is minus in equation
    :param equation_list: the list of the equation; passed by reference
    :param index: the current index in list
    :return:
    """
    # if the minus is the first char in equation or first char after (
    counter = 0
    if index == 0 or equation_list[index - 1] == "(":
        while equation_list[index] == "-":
            counter += 1
            index += 1
        return counter, index - 1
    elif equation_list[index - 1] in OPERATORS:
        equation_list[index] = "~"
        counter, index = check_negativity(equation_list, index)
        return counter, index
    # if last char is operand
    else:
        try:
            char = equation_list[index + 1]
        except IndexError:
            raise ValueError("equation cannot end with -")
        if char == '-':
            equation_list[index + 1] = '~'
    return 1, index
