# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_return_value():
    logger = Mock()

    @LoggedFunction(logger)
    def combine(value, *, count):
        """Example function."""
        return value.strip() * count

    result = combine(" x ", count=2)

    assert result == "xx"
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Example function."
    assert logger.debug.call_args_list == [
        call("combine('x', count=2)"),
        call("combine -> xx"),
    ]


def test_logged_function_does_not_log_none_return_value():
    logger = Mock()

    @LoggedFunction(logger)
    def perform_action():
        return None

    result = perform_action()

    assert result is None
    logger.debug.assert_called_once_with("perform_action()")
