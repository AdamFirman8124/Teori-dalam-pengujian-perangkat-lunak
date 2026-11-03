# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_on_right_invokes_success_handler_only():
    """case() on a Right must call only the success handler with the wrapped
    value and return its result (covers the True branch of line 33 and line 34)."""
    calls = []

    def error(value):
        calls.append(("error", value))
        return "error: {}".format(value)

    def success(value):
        calls.append(("success", value))
        return "success: {}".format(value)

    result = Right(42).case(error, success)

    # Postcondition: success handler ran with the wrapped value and its
    # return value was propagated; the error handler was never invoked.
    assert result == "success: 42"
    assert calls == [("success", 42)]


def test_case_on_left_invokes_error_handler_only():
    """case() on a Left must call only the error handler with the wrapped
    value and return its result (covers the False branch of line 33 and line 35)."""
    calls = []

    def error(value):
        calls.append(("error", value))
        return "error: {}".format(value)

    def success(value):
        calls.append(("success", value))
        return "success: {}".format(value)

    result = Left("boom").case(error, success)

    # Postcondition: error handler ran with the wrapped value and its
    # return value was propagated; the success handler was never invoked.
    assert result == "error: boom"
    assert calls == [("error", "boom")]
