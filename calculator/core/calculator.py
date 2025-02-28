class Calculator:
    def __init__(self, argument: str):
        self.argument = argument

    def validate(self) -> bool:
        # TO DO
        return self.argument == self.argument

    def convert(self) -> list:
        """Shunting Yard Algorithm
        """
        infix_expression = self.argument

        output, operators = [], []

        precedences = {'+': 0, '-': 0, '*': 1, '/': 1}

        for value in infix_expression.split(' '):
            if value in precedences.keys():
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
            else:
                output.append(value)

        while len(operators) > 0 and operators[0] != '(':
            output.append(operators.pop(0))

        postfix_expression = output

        return postfix_expression

    def operate(self, value_1: int, operator: str, value_2: int) -> int:
        if operator == '+':
            return value_1 + value_2
        elif operator == '-':
            return value_1 - value_2
        elif operator == '/':
            return value_1 / value_2
        elif operator == '*':
            return value_1 * value_2

    def calculate(self, postfix_expression: list) -> int:
        output = []

        operators = ['+', '-', '*', '/']

        for value in postfix_expression:
            if value in operators:
                item_1 = output.pop()
                item_2 = output.pop()
                output.append(self.operate(item_2, value, item_1))
            else:
                output.append(int(value))

        return output[0]
