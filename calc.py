def power(num1: float, num2: float) -> float:
    """

    :param num1:
    :param num2:
    :return:
    """
    if num1 == 0 and num2 == 0:
        raise "0^0 is undefined"
    elif num2 < 0 and -1 < num1 < 1 and num1 != 0:
        raise "negative numbers cannot have square root"
    return num2 ** num1


def division(num1, num2):
    if num1 == 0:
        raise "division by 0 is undefined"
    return num2 / num1


def multiply(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num2 - num1


def minimum(num1, num2):
    """
    checks minimum of two numbers
    :param num1: first num to check
    :param num2: second num to check
    :return: the bigger num
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
    """
    result: int = 1
    print("stack here")
    if num < 0:
        raise "factorial only for non negative numbers"
    if num * 10 % 10 != 0:
        raise "factorial only for integer numbers"
    num = int(num)
    for i in range(1, num + 1):
        result *= i
    return result


def average(num1, num2) -> float:
    """
    calculates the average of two given numbers
    :param num1: first num
    :param num2: second num
    :return: their average
    """
    return (num1 + num2) / 2


def modulo(num1, num2) -> float:
    return num1 % num2


def negativity(num1) -> float:
    return -num1


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
             '~': (negativity, 6, 1)}

OPERANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ")", "!"]

PRE_OPERATOR_OPERANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "("]


def operator_priority(operator1: str, operator2: str) -> bool:
    if OPERATORS[operator1][1] >= OPERATORS[operator2][1]:
        return True
    return False


def check_negativity(equation_list: list, index: int) -> tuple:
    sign = -1
    index += 1
    try:
        char = equation_list[index]
    except:
        raise ValueError("equation cannot end with ~")
    while char == "-":
        sign *= -1
        index += 1
        if index < len(equation_list):
            char = equation_list[index]
        else:
            raise ValueError("equation cannot end with -")
    if char in PRE_OPERATOR_OPERANDS:
        make_sign = True
    else:
        raise ValueError("after ~ must come - or operand")
    return sign, index, make_sign, char
