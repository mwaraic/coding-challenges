from core.calculator import Calculator


class TestCalculator:
    obj = Calculator(1, 2)

    def test_init(self):
        assert self.obj.x == 1
        assert self.obj.y == 2

    def test_multiply(self):
        assert self.obj.multiply() == 2

    def test_add(self):
        assert self.obj.add() == 3

    def test_divide(self):
        assert self.obj.divide() == 0.50

    def test_subtract(self):
        assert self.obj.subtract() == -1
