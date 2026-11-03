# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_on_right_calls_success_handler():
    """case() on a Right instance must invoke the success handler with the
    wrapped value and never touch the error handler (covers lines 33-34)."""
    right = Right(42)

    def error(value):
        raise AssertionError("error handler must not be called for Right")

    success_calls = []

    def success(value):
        success_calls.append(value)
        return value * 2

    result = right.case(error, success)

    assert result == 84
    assert success_calls == [42]
    assert right.is_right() is True


def test_case_on_left_calls_error_handler():
    """case() on a Left instance must invoke the error handler with the
    wrapped value and never touch the success handler (covers lines 33 and 35)."""
    left = Left("boom")

    def success(value):
        raise AssertionError("success handler must not be called for Left")

    error_calls = []

    def error(value):
        error_calls.append(value)
        return "handled: {}".format(value)

    result = left.case(error, success)

    assert result == "handled: boom"
    assert error_calls == ["boom"]
    assert left.is_right() is False
