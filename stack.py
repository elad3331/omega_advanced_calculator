from advanced_calc.calc import OPERATORS
from advanced_calc.calc import OPERANDS


def calc_postfix(equation: list) -> float:
    stack = []
    for i in range(0, len(equation)):
        tmp_str = ""
        char = equation[i]
        while char.isdigit():
            tmp_str += char
            i += 1

        if char in OPERATORS.keys():
            operator = stack.pop()
            num1 = float(stack.pop())
            if operator == "!" or operator == "~":
                stack.append(OPERATORS[operator][0](num1))
            else:
                num2 = float(stack.pop())
                stack.append(OPERATORS[operator][0](num1, num2))

    return stack.pop()


def convert_infix_to_postfix(equation: str):
    # assuming all spaces are typed by mistake, so I remove them
    equation = equation.replace(" ", "")
    print(equation)
    last_char = ""
    stack = []
    return_list = []
    equation_list = list(equation)
    i = 0
    # in order to check if number is positive or negative
    sign = 1
    make_sign = False
    while i < len(equation_list):
        tmp_str = ""
        char = equation_list[i]
        print(char)
        if char.isdigit():
            # NEEDS TO CHANGE
            if last_char == "!":
                raise ValueError("operands cannot come right after !")
            if last_char != "" and last_char not in OPERATORS.keys():
                raise ValueError("operands must be first in equation or come after operator")
            while char.isdigit():
                tmp_str += char
                i += 1
                if i < len(equation_list):
                    char = equation_list[i]
                else:
                    break

            if char == ".":
                tmp_str += char
                i += 1
                try:
                    char = equation_list[i]
                except IndexError:
                    raise "after . there must be digit"
                if not char.isdigit():
                    raise ValueError("wrong sentence syntax")
                while char.isdigit():
                    tmp_str += char
                    i += 1
                    if i < len(equation_list):
                        char = equation_list[i]
                    else:
                        break
            if make_sign:
                return_list.append(float(tmp_str) * sign)
            else:
                return_list.append(float(tmp_str))
            make_sign = False
            # dummy digital numbers
            last_char = "1"

        elif char == "(":
            last_char = "("
            stack.append("(")
            i += 1

        elif char == ")":
            last_char = ")"
            while stack[-1] != "(":
                return_list.append(stack.pop())
            stack.pop()
            if sign == -1:
                return_list.append("~")
                sign = 1
            i += 1

        elif char in OPERATORS.keys():
            operator_position = OPERATORS[char][2]
            # for pre operands' operators
            if operator_position == 1:
                if last_char != "" and last_char not in OPERATORS.keys():
                    raise ValueError(char, " must be after operator or first in equation")
                else:
                    # implement later
                    pass
            # for binary operators
            elif operator_position == 2:
                if last_char not in OPERANDS:
                    raise ValueError(char, " must be after operand")
                else:
                    # implement later
                    pass
            else:
                if last_char not in OPERANDS:
                    raise ValueError(char, " must be after operand")
                else:
                    # implement later
                    pass


        else:
            raise ValueError("invalid character in equation")
    if not last_char.isdigit() and last_char != ")" and last_char != "!":
        raise ValueError("wrong syntax")
    while len(stack) != 0:
        return_list.append(stack.pop())
    print(return_list)


convert_infix_to_postfix("!4^2")
