# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import Mock, call

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_arguments_and_non_none_result():
    logger = Mock()

    @LoggedFunction(logger)
    def combine(first, second, *, suffix):
        """Combine values."""
        return "ok"

    result = combine(" left ", 2, suffix=" done ")

    assert result == "ok"
    assert combine.__name__ == "combine"
    assert combine.__doc__ == "Combine values."
    assert logger.debug.call_args_list == [
        call("combine('left', 2, suffix='done')"),
        call("combine -> ok"),
    ]


def test_logged_function_with_no_arguments_and_none_result():
    logger = Mock()
    calls = []

    @LoggedFunction(logger)
    def no_result():
        calls.append("called")

    result = no_result()

    assert result is None
    assert calls == ["called"]
    logger.debug.assert_called_once_with("no_result()")
