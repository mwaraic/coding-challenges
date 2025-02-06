from core.calculator import Calculator
import sys


def validate(argument: str):
    # TO DO
    return argument == argument


def convert(infix_expression: str):
    """Shunting Yard Algorithm
    """

    output, operators = [], []

    precedences = {'+': 0, '-': 0, '*': 1, '/': 1}

    for value in infix_expression:
        if ord('0') <= ord(value) <= ord('9'):
            output.append(value)
        elif value in precedences.keys():
            while len(operators) > 0 and operators[0] != '('  \
                    and precedences[operators[0]] >= precedences[value]:
                output.append(operators.pop(0))
            operators.insert(0, value)
        elif value == '(':
            operators.insert(0, value)
        elif value == ')':
            while len(operators) > 0 and operators[0] != '(':
                output.append(operators.pop(0))
            if len(operators) > 0 and operators[0] == '(':
                operators.pop(0)

    while len(operators) > 0 and operators[0] != '(':
        output.append(operators.pop(0))

    postfix_expression = ' '.join(output)

    return postfix_expression


def operate(x: int, operator: str, y: int):
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


def calculate(postfix_expression: str):
    output = []

    operators = ['+', '-', '*', '/']

    for value in postfix_expression:
        if ord('0') <= ord(value) <= ord('9'):
            output.append(int(value))
        elif value in operators:
            item_1 = output.pop()
            item_2 = output.pop()
            output.append(operate(item_2, value, item_1))

    return output[0]


if __name__ == "__main__":

    argument = sys.argv[1]

    is_valid = validate(argument)

    if is_valid:
        postfix_expression = convert(argument)
        print(calculate(postfix_expression))
    else:
        print('invalid argument')
