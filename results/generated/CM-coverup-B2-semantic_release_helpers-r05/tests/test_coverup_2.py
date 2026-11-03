# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest import mock

import logging

import pytest

from semantic_release.helpers import LoggedFunction


def test_logged_function_stores_logger():
    """Line 53: __init__ must store the given logger."""
    logger = logging.getLogger("test-logged-function")
    decorator = LoggedFunction(logger)
    assert decorator.logger is logger


def test_logged_function_logs_args_kwargs_and_result():
    """Lines 56-77: decorator wraps function, logs inputs and non-None result."""
    logger = mock.Mock(spec=logging.Logger)

    @LoggedFunction(logger)
    def add(a, b, *, c=0):
        """Add numbers."""
        return a + b + c

    # functools.wraps preserves the wrapped function's metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

    result = add(1, 2, c=3)
    assert result == 6

    # One debug call for the input, one for the result
    assert logger.debug.call_count == 2
    entry_log = logger.debug.call_args_list[0][0][0]
    assert entry_log == "add(1, 2, c=3)"
    exit_log = logger.debug.call_args_list[1][0][0]
    assert exit_log == "add -> 6"


def test_logged_function_string_args_are_formatted():
    """Lines 59-64: string args are quoted/stripped via format_arg."""
    logger = mock.Mock(spec=logging.Logger)

    @LoggedFunction(logger)
    def greet(name, punctuation):
        return f"Hello {name}{punctuation}"

    result = greet("world", "!")
    assert result == "Hello world!"

    entry_log = logger.debug.call_args_list[0][0][0]
    assert entry_log == "greet('world', '!')"


def test_logged_function_none_result_is_not_logged():
    """Branch at line 73: a None result must not produce a result log line."""
    logger = mock.Mock(spec=logging.Logger)

    @LoggedFunction(logger)
    def do_nothing():
        return None

    assert do_nothing() is None

    # Only the "input" debug message should have been emitted
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0][0][0] == "do_nothing()"
