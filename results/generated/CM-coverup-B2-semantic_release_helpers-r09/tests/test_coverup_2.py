# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

import logging
from unittest import mock

from semantic_release.helpers import LoggedFunction


def test_logged_function_logs_input_and_result():
    """Covers lines 53, 56-57, 59-64, 70, 73-75, 77 (non-None result branch)."""
    logger = mock.Mock(spec=logging.Logger)
    decorator = LoggedFunction(logger)

    # Line 53: the logger passed to the constructor is stored on the instance
    assert decorator.logger is logger

    @decorator
    def add(a, b, *, c=0):
        """Add two numbers."""
        return a + b + c

    # Lines 56-57, 77: decoration returns a wrapper that preserves metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

    result = add(1, 2, c=3)

    # Lines 70, 75: the wrapped function's return value is passed through
    assert result == 6

    # Lines 59-64: input message; line 74: result message (result is not None)
    logger.debug.assert_has_calls(
        [mock.call("add(1, 2, c=3)"), mock.call("add -> 6")]
    )
    assert logger.debug.call_count == 2


def test_logged_function_string_args_are_quoted_and_stripped():
    """Covers lines 59-64 with str args/kwargs (format_arg quoting/stripping)."""
    logger = mock.Mock(spec=logging.Logger)

    @LoggedFunction(logger)
    def concat(a, b, sep=" "):
        return f"{a}{sep}{b}"

    result = concat("foo", "bar", sep="-")

    assert result == "foo-bar"
    logger.debug.assert_has_calls(
        [
            mock.call("concat('foo', 'bar', sep='-')"),
            mock.call("concat -> foo-bar"),
        ]
    )
    assert logger.debug.call_count == 2


def test_logged_function_none_result_is_not_logged():
    """Covers line 73 (False branch) and line 75: None result returned, not logged."""
    logger = mock.Mock(spec=logging.Logger)

    @LoggedFunction(logger)
    def do_nothing():
        pass

    result = do_nothing()

    assert result is None
    # Only the "input" message is logged; the None result is not
    logger.debug.assert_called_once_with("do_nothing()")
