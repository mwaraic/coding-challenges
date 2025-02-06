from calc import operate, calculate, convert, validate


class TestCalc:
    def test_validate(self):
        # TO DO
        assert validate('1 * 2') is True

    def test_convert(self):
        assert convert('1 * 2') == '1 2 *'

    def test_operate(self):
        assert operate(1, '+', 2) == 3
        assert operate(2, '-', 1) == 1
        assert operate(2, '*', 3) == 6
        assert operate(3, '/', 2) == 1.5

    def test_calculate(self):
        assert calculate('1 2 *') == 2
