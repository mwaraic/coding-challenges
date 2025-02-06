import sys
from core.calculator import Calculator


if __name__ == "__main__":

    argument = sys.argv[1]

    obj = Calculator(argument)

    is_valid = obj.validate()

    if is_valid:
        postfix_expression = obj.convert()
        print(obj.calculate(postfix_expression))
    else:
        print('invalid argument')
