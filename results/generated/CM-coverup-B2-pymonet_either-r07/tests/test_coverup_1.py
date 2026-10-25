# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_calls_success_on_right():
    right = Right(42)

    def error(value):
        raise AssertionError("error handler should not be called for Right")

    result = right.case(error, lambda value: value + 1)

    assert result == 43


def test_case_calls_error_on_left():
    left = Left("boom")

    def success(value):
        raise AssertionError("success handler should not be called for Left")

    result = left.case(lambda value: value + "!", success)

    assert result == "boom!"
