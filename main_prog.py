from stack import calc_postfix
from stack import convert_infix_to_postfix
from calculator_exception import CalculationError


def start_calculator():
    equation = input("please enter an equation, if you want to quit type exit or ^D\n")
    while equation != "exit":
        valid_equation = False
        try:
            result = convert_infix_to_postfix(equation)
            valid_equation = True
        except ValueError as e:
            print(e)
        if valid_equation:
            try:
                print("The result is", calc_postfix(result))
            except CalculationError as e1:
                print(e1)
        equation = input("please enter an equation, exit program\n")


def main():
    try:
        start_calculator()
    except (EOFError, KeyboardInterrupt):
        print("exiting program")


if __name__ == "__main__":
    main()
