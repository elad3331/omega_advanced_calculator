from stack import calc_postfix
from stack import convert_infix_to_postfix
from calculator_exception import CalculationError


def start_calculator():
    """
    function that gets input from the user- the equation. Tries to calc it.
    If the equation is not valid it prints the right error message.
    :return:
    """
    equation = input("please enter an equation, if you want to quit type exit or ^D\n")
    while equation != "exit":
        valid_equation = False
        try:
            result = convert_infix_to_postfix(equation)
            print(result)
            valid_equation = True
        except ValueError as e:
            print(e)
        if valid_equation:
            try:
                print("The result is", calc_postfix(result))
            except CalculationError as e1:
                print(e1)
        equation = input("please enter an equation, if you want to quit type exit or ^D\n")


def main():
    """
    main function. catches EOFError, KeyboardInterrupt if needed.
    :return:
    """
    try:
        start_calculator()
    except (EOFError, KeyboardInterrupt):
        print("exiting program")


if __name__ == "__main__":
    main()
