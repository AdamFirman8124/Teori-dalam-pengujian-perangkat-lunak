# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_return_value():
    logger = Mock()
    invocations = []

    @LoggedFunction(logger)
    def combine(text, number, *, suffix):
        """Combine the supplied values."""
        invocations.append((text, number, suffix))
        return 42

    result = combine("  value  ", 7, suffix="  end  ")

    assert result == 42
    assert invocations == [("  value  ", 7, "  end  ")]
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Combine the supplied values."
    assert combine.__wrapped__ is not None
    assert logger.debug.call_args_list == [
        call("combine('value', 7, suffix='end')"),
        call("combine -> 42"),
    ]


def test_logged_function_does_not_log_a_none_return_value():
    logger = Mock()
    invocation_count = 0

    @LoggedFunction(logger)
    def perform_action():
        nonlocal invocation_count
        invocation_count += 1

    result = perform_action()

    assert result is None
    assert invocation_count == 1
    logger.debug.assert_called_once_with("perform_action()")
