from core.calculator import Calculator
import sys


def run(x: int, operator: str, y: int):
    obj = Calculator(x, y)

    if operator == '*':
        result = obj.multiply()

    elif operator == '/':
        result = obj.divide()

    elif operator == '-':
        result = obj.subtract()

    elif operator == '+':
        result = obj.add()

    return result


def verify(argument: str):
    if isinstance(argument, str):
        if len(argument.split()) == 3:
            if argument.split()[1] in ['*', '-', '+', '/']:
                if ord('0') <= ord(argument.split()[0]) <= ord('9'):
                    if ord('0') <= ord(argument.split()[2]) <= ord('9'):
                        return True
    return False


if __name__ == "__main__":

    argument = sys.argv[1]

    result = verify(argument)

    if result:
        argument = argument.split()
        print(run(int(argument[0]), argument[1], int(argument[2])))
    else:
        print('Please provide correct argument')
