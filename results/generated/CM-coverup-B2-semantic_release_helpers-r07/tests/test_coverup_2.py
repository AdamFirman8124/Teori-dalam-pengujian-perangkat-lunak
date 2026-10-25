# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_return_value():
    logger = Mock()

    @LoggedFunction(logger)
    def example(value, *, enabled=False):
        """Example docstring."""
        return "completed"

    result = example("  text  ", enabled=True)

    assert result == "completed"
    assert example.__name__ == "example"
    assert example.__doc__ == "Example docstring."
    assert logger.debug.call_args_list == [
        call("example('text', enabled=True)"),
        call("example -> completed"),
    ]


def test_logged_function_does_not_log_none_return_value():
    logger = Mock()

    @LoggedFunction(logger)
    def no_result():
        return None

    result = no_result()

    assert result is None
    logger.debug.assert_called_once_with("no_result()")
