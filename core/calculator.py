class Calculator:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def divide(self):
        return self.x / self.y
