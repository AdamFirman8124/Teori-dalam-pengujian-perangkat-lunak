# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_return_value():
    logger = Mock()
    received = []

    @LoggedFunction(logger)
    def combine(prefix, number=0):
        """Combine the supplied values."""
        received.append((prefix, number))
        return f"{prefix.strip()}:{number}"

    result = combine(" value ", number=2)

    assert result == "value:2"
    assert received == [(" value ", 2)]
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Combine the supplied values."
    assert logger.debug.call_args_list == [
        call("combine('value', number=2)"),
        call("combine -> value:2"),
    ]


def test_logged_function_does_not_log_a_none_return_value():
    logger = Mock()
    received = []

    @LoggedFunction(logger)
    def record(value):
        received.append(value)

    result = record(" item ")

    assert result is None
    assert received == [" item "]
    logger.debug.assert_called_once_with("record('item')")
