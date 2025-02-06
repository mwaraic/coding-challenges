class Calculator:
    def __init__(self, argument: str):
        self.argument = argument

    def validate(self):
        # TO DO
        return self.argument == self.argument

    def convert(self):
        """Shunting Yard Algorithm
        """
        infix_expression = self.argument

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

    def operate(self, value_1: int, operator: str, value_2: int):
        if operator == '+':
            return value_1 + value_2
        elif operator == '-':
            return value_1 - value_2
        elif operator == '/':
            return value_1 / value_2
        elif operator == '*':
            return value_1 * value_2

    def calculate(self, postfix_expression: str):
        output = []

        operators = ['+', '-', '*', '/']

        for value in postfix_expression:
            if ord('0') <= ord(value) <= ord('9'):
                output.append(int(value))
            elif value in operators:
                item_1 = output.pop()
                item_2 = output.pop()
                output.append(self.operate(item_2, value, item_1))

        return output[0]
