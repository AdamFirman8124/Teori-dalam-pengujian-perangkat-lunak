# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_calls_success_handler_on_right():
    """case() on a Right instance must invoke only the success handler with the value
    and return its result (covers lines 33-34, True branch)."""
    calls = []

    def error(value):
        calls.append(("error", value))
        return "error-result"

    def success(value):
        calls.append(("success", value))
        return "success-result"

    either = Right(42)
    result = either.case(error, success)

    assert result == "success-result"
    assert calls == [("success", 42)]


def test_case_calls_error_handler_on_left():
    """case() on a Left instance must invoke only the error handler with the value
    and return its result (covers lines 33 and 35, False branch)."""
    calls = []

    def error(value):
        calls.append(("error", value))
        return "error-result"

    def success(value):
        calls.append(("success", value))
        return "success-result"

    either = Left("boom")
    result = either.case(error, success)

    assert result == "error-result"
    assert calls == [("error", "boom")]
