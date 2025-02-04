from calc import verify, run


class TestCalc:
    def test_run(self):
        assert run(1, '+', 2) == 3
        assert run(2, '-', 1) == 1
        assert run(2, '*', 3) == 6
        assert run(3, '/', 2) == 1.5

    def test_verify(self):
        assert verify('1 + 2') is True
        assert verify('2 - 1') is True
        assert verify('2 * 3') is True
        assert verify('3 / 2') is True

    def test_args_verify(self):
        assert verify(1) is False

    def test_args_length_verify(self):
        assert verify('1') is False

    def test_args_operator_verify(self):
        assert verify('1 ( 2') is False

    def test_args_params_verify(self):
        assert verify('A * 2') is False
        assert verify('1 * B') is False
