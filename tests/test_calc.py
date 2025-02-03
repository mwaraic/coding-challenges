from calc import verify


class TestCalc:
    def test_verify(self):
        assert verify('1 * 2') is True

    def test_args_verify(self):
        assert verify(1) is False

    def test_args_length_verify(self):
        assert verify('1') is False

    def test_args_operator_verify(self):
        assert verify('1 ( 2') is False

    def test_args_params_verify(self):
        assert verify('A * 2') is False
        assert verify('1 * B') is False
