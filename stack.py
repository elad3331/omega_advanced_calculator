from advanced_calc.calc import OPERATORS
from advanced_calc.calc import OPERANDS
from advanced_calc.calc import PRE_OPERATOR_OPERANDS
from advanced_calc.calc import check_negativity


def calc_postfix(equation: list) -> float:
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
                stack.append(OPERATORS[operator][0](num1))
            else:
                num2 = stack.pop()
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
        print("char", char)
        print("last char", last_char)
        if char.isdigit():
            # NEEDS TO CHANGE
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
                except:
                    raise ValueError("number isn't valid")
                if make_sign:
                    return_list.append(num * sign)
                else:
                    return_list.append(num)
                make_sign = False
                # dummy digital numbers
                last_char = "1"
            else:
                raise ValueError("number must follow preoperands' operators or binary operators")

        elif char == "(":
            if last_char in OPERANDS:
                raise ValueError("oeperator must be before (")
            last_char = "("
            stack.append("(")
            i += 1

        elif char == ")":
            last_char = ")"

            try:
                while stack[-1] != "(":
                    return_list.append(stack.pop())
            except:
                raise ValueError(") cannot appear before matching (")

            stack.pop()
            if sign == -1:
                return_list.append("~")
                sign = 1
            i += 1

        elif char in OPERATORS.keys():
            operator_position = OPERATORS[char][2]
            # for pre operands' operators

            if operator_position == 1:
                if last_char != "" and last_char not in OPERATORS.keys() and last_char != "(":
                    raise ValueError(char, " must be after operator or first in equation")
                else:
                    if char == "~":
                        sign, i, make_sign, asf = check_negativity(equation_list, i)
                        i -= 1
            # for non preoperands' operators
            else:
                if last_char not in OPERANDS:
                    raise ValueError(char, " must be after operand")

            while len(stack) != 0 and stack[-1] != "(" and OPERATORS[char][1] <= OPERATORS[stack[-1]][1]:
                return_list.append(stack.pop())
            stack.append(char)
            i += 1
            last_char = char

        else:
            raise ValueError("invalid character in equation")
    if last_char not in OPERANDS:
        raise ValueError("last char in equation should be operand")
    while len(stack) != 0:
        if stack[-1] == "(":
            raise ValueError("number of ( and ) doesnt match")
        return_list.append(stack.pop())
    print(return_list)
    return return_list


print(calc_postfix(convert_infix_to_postfix("54/3+4")))
