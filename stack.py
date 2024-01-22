from calc import OPERATORS
from calc import OPERANDS
from calc import operator_priority
from calc import check_negativity
from calc import check_minuses
from calc import OPEN_PARENTHESES
from calc import CLOSER_PARENTHESES


def calc_postfix(equation: list) -> float:
    """
    function that gets valid postfix equation in list and calcs it
    :param equation: the list that represents the equation (each cell is operator or operand)
    :return: the answer of the equation
    """
    stack = []
    for i in range(0, len(equation)):
        element = equation[i]
        if type(element) is float:
            stack.append(element)
        elif element in OPERATORS.keys():
            operator = element
            num1 = stack.pop()
            # if operator works only on one operand
            if OPERATORS[operator][2] != 2:
                stack.append(round(OPERATORS[operator][0](num1), 10))
            else:
                num2 = stack.pop()
                stack.append(round(OPERATORS[operator][0](num1, num2), 10))
    return stack.pop()


def convert_infix_to_postfix(equation: str) -> list:
    """
    function that gets infix equation in string. converts it to postfix
    :param equation: the string that represents the equation
    :return: valid postfix equation (if possible)
    :raises: ValueError if the equation syntax is invalid
    """
    # assuming all spaces are typed by mistake, so I remove them
    equation = equation.replace(" ", "")
    equation = equation.replace("\t", "")
    last_char = ""
    stack = []
    return_list = []
    equation_list = list(equation)
    i = 0
    counter = 1
    while i < len(equation_list):
        tmp_str = ""
        char = equation_list[i]
        if char.isdigit() or char == ".":
            if (last_char in OPERATORS.keys() and last_char not in OPERANDS) or last_char == "" or last_char == "(":
                while char.isdigit() or char == ".":
                    tmp_str += char
                    i += 1
                    if i < len(equation_list):
                        char = equation_list[i]
                    else:
                        break
                try:
                    num = float(tmp_str)
                except (SyntaxError, ValueError):
                    raise ValueError("number isn't valid")
                return_list.append(num)
                # dummy digital numbers
                last_char = "1"
            else:
                raise ValueError("number must follow preoperands' operators or binary operators")
        elif char == OPEN_PARENTHESES:
            if last_char in OPERANDS:
                raise ValueError("oeperator must be before ( or first in equation")
            last_char = OPEN_PARENTHESES
            stack.append(OPEN_PARENTHESES)
            i += 1
        elif char == CLOSER_PARENTHESES:
            if last_char == OPEN_PARENTHESES:
                raise ValueError(") cannot appear right after (")
            last_char = CLOSER_PARENTHESES
            try:
                while stack[-1] != OPEN_PARENTHESES:
                    return_list.append(stack.pop())
            except IndexError:
                raise ValueError(") cannot appear before matching (")
            stack.pop()
            i += 1
        elif char in OPERATORS.keys() and char != "_":
            operator_position = OPERATORS[char][2]
            # for pre operands' operators
            if operator_position == 1:
                if last_char != "" and last_char not in OPERATORS.keys() and last_char != OPEN_PARENTHESES:
                    raise ValueError(char, " must be after operator or first in equation")
                else:
                    if char == "~":
                        counter, i = check_negativity(equation_list, i)
            # for non preoperands' operators
            else:
                # can be binary or unary minus
                if char == "-":
                    counter, i = check_minuses(equation_list, i)
                    char = equation_list[i - counter + 1]
                elif last_char not in OPERANDS:
                    raise ValueError(char + " must be after operand")
            while len(stack) != 0 and stack[-1] != OPEN_PARENTHESES and operator_priority(char, stack[-1]) and (
                    stack[-1] != '_' != char):
                return_list.append(stack.pop())
            while counter > 0:
                stack.append(char)
                counter -= 1
            counter = 1
            i += 1
            last_char = char
        else:
            raise ValueError("invalid character in equation")
    if last_char not in OPERANDS:
        raise ValueError("equation must end with operand or post operand operator")
    while len(stack) != 0:
        if stack[-1] == OPEN_PARENTHESES:
            raise ValueError("number of ( and ) doesnt match")
        return_list.append(stack.pop())
    return return_list
