from calc import OPERATORS
from calc import OPERANDS
from calc import operator_priority
from calc import check_negativity
from calc import check_minuses


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
                if len(stack) == 0 and operator == '-':
                    stack.append(OPERATORS[operator][0](num1, 0))
                else:
                    num2 = stack.pop()
                    stack.append(OPERATORS[operator][0](num1, num2))
    return stack.pop()


def convert_infix_to_postfix(equation: str):
    # assuming all spaces are typed by mistake, so I remove them
    equation = equation.replace(" ", "")
    last_char = ""
    stack = []
    return_list = []
    equation_list = list(equation)
    i = 0
    counter = 1
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
                return_list.append(num)
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
            if last_char == "(":
                raise ValueError(") cannot appear right after (")
            last_char = ")"
            try:
                while stack[-1] != "(":
                    return_list.append(stack.pop())
            except:
                raise ValueError(") cannot appear before matching (")
            stack.pop()
            i += 1
        elif char in OPERATORS.keys():
            operator_position = OPERATORS[char][2]
            # for pre operands' operators
            if operator_position == 1:
                if last_char != "" and last_char not in OPERATORS.keys() and last_char != "(":
                    raise ValueError(char, " must be after operator or first in equation")
                else:
                    if char == "~":
                        counter, i = check_negativity(equation_list, i)
            # for non preoperands' operators
            else:
                # can be binary or unary minus
                if char == "-":
                    counter, i, equation_list = check_minuses(equation_list, i)
                    char = equation_list[i-counter+1]
                    print("equation ", equation_list[i])
                elif last_char not in OPERANDS:
                    raise ValueError(char, " must be after operand")
            while len(stack) != 0 and stack[-1] != "(" and operator_priority(char, stack[-1]):
                print("appends it ", stack[-1], i)
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
        raise ValueError("last char in equation should be operand")
    while len(stack) != 0:
        if stack[-1] == "(":
            raise ValueError("number of ( and ) doesnt match")
        return_list.append(stack.pop())
    print(return_list)
    return return_list
