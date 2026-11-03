# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from unittest.mock import Mock

from pymonet.either import Left, Right


def test_case_calls_success_handler_on_right():
    """case() on a Right must call only the success handler with the value
    and return its result (covers lines 33-34)."""
    right = Right(42)

    error_handler = Mock(name="error_handler")
    success_handler = Mock(name="success_handler", return_value="success-result")

    result = right.case(error_handler, success_handler)

    success_handler.assert_called_once_with(42)
    error_handler.assert_not_called()
    assert result == "success-result"


def test_case_calls_error_handler_on_left():
    """case() on a Left must call only the error handler with the value
    and return its result (covers line 35)."""
    left = Left("boom")

    error_handler = Mock(name="error_handler", return_value="error-result")
    success_handler = Mock(name="success_handler")

    result = left.case(error_handler, success_handler)

    error_handler.assert_called_once_with("boom")
    success_handler.assert_not_called()
    assert result == "error-result"
