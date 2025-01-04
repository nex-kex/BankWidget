from src.decorators import log


def test_log_error(capsys):
    @log()
    def mistake():
        raise ValueError("Guaranteed error")

    mistake()
    captured = capsys.readouterr()
    assert captured.out[:49] == "mistake executed with an error: Guaranteed error."


def test_log_no_errors(capsys):
    @log()
    def multiply(x, y):
        return x * y

    multiply(3, 7)
    captured = capsys.readouterr()
    assert (
        captured.out[:82] + captured.out[93:-2]
        == "multiply executed with no errors. Input args: (3, 7), kwargs: {}. Execution time: seconds."
    )
