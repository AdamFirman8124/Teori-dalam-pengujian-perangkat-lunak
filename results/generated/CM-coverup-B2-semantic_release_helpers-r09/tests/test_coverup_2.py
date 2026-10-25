# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_return_value():
    logger = Mock()

    @LoggedFunction(logger)
    def combine(value, *, suffix):
        """Combine two strings."""
        return value + suffix

    result = combine(" hello ", suffix=" world ")

    assert result == " hello  world "
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Combine two strings."
    assert logger.debug.call_args_list == [
        call("combine('hello', suffix='world')"),
        call("combine ->  hello  world "),
    ]


def test_logged_function_does_not_log_none_return_value():
    logger = Mock()
    received = []

    @LoggedFunction(logger)
    def record(first, second=0):
        received.append((first, second))

    result = record(1, second=2)

    assert result is None
    assert received == [(1, 2)]
    logger.debug.assert_called_once_with("record(1, second=2)")
