from core.calculator import Calculator
import sys


def run(x, operator, y):
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


if __name__ == "__main__":

    args = sys.argv[1].split()

    print(run(int(args[0]), args[1], int(args[2])))
