from core.calculator import Calculator


class TestCalculator:
    obj = Calculator('1 * 2')

    def test_validate(self):
        # TO DO
        assert self.obj.validate('1 * 2') is True

    def test_convert(self):
        assert self.obj.convert() == '1 2 *'

    def test_operate(self):
        assert self.obj.operate(1, '+', 2) == 3
        assert self.obj.operate(2, '-', 1) == 1
        assert self.obj.operate(2, '*', 3) == 6
        assert self.obj.operate(3, '/', 2) == 1.5

    def test_calculate(self):
        assert self.obj.calculate('1 2 *') == 2
