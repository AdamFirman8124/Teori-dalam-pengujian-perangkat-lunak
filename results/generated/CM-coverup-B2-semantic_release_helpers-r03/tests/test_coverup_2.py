# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import MagicMock

import pytest

from semantic_release.helpers import LoggedFunction


def test_logged_function_init():
    """Instantiating LoggedFunction stores the logger (line 53)."""
    logger = MagicMock(name="logger")
    decorator = LoggedFunction(logger)
    assert decorator.logger is logger


def test_logged_function_logs_args_kwargs_and_result():
    """
    Applying the decorator and calling the wrapped function exercises
    lines 56-75, including the truthy branch of 'result is not None'.
    """
    logger = MagicMock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def add(a, b, *, suffix=""):
        return a + b + suffix

    # functools.wraps should preserve the wrapped function's metadata
    assert add.__name__ == "add"

    result = add(1, 2, suffix=3)

    assert result == 6

    # Input arguments were logged before the call
    first_debug_call = logger.debug.call_args_list[0]
    assert first_debug_call.args[0] == "add(1, 2, suffix=3)"

    # The return value was logged after the call
    second_debug_call = logger.debug.call_args_list[1]
    assert second_debug_call.args[0] == "add -> 6"

    assert logger.debug.call_count == 2


def test_logged_function_none_result_not_logged():
    """
    When the wrapped function returns None, the result is not logged
    (covers the falsy branch of 'result is not None').
    """
    logger = MagicMock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def do_nothing(value):
        return None

    result = do_nothing("some value")

    assert result is None

    # Only the pre-call log of arguments happened
    assert logger.debug.call_count == 1
    assert logger.debug.call_args.args[0] == "do_nothing('some value')"


def test_logged_function_no_args():
    """A function called with no arguments logs empty parens and its result."""
    logger = MagicMock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def answer():
        return 42

    assert answer() == 42
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[0].args[0] == "answer()"
    assert logger.debug.call_args_list[1].args[0] == "answer -> 42"


def test_logged_function_string_args_are_quoted():
    """String arguments are formatted via format_arg with surrounding quotes."""
    logger = MagicMock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def greet(name, punctuation):
        return name + punctuation

    assert greet("Bob ", "!") == "Bob !"
    assert logger.debug.call_args_list[0].args[0] == "greet('Bob', '!')"
    assert logger.debug.call_args_list[1].args[0] == "greet -> Bob !"
