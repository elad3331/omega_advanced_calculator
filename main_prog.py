from stack import calc_postfix
from stack import convert_infix_to_postfix


def main():
    equation = input("please enter an equation, if you want to quit type exit\n")
    while equation != "exit":
        try:
            result = convert_infix_to_postfix(equation)
            print("the result of the equation is", calc_postfix(result))
        except (ValueError,EOFError) as e:
            print(e)
        equation = input("please enter an equation, exit program\n")


if __name__ == "__main__":
    main()
