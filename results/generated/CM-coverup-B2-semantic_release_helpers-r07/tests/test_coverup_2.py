# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

import unittest.mock as mock

import pytest

from semantic_release.helpers import LoggedFunction


def test_logged_function_init_stores_logger():
    """Line 53: __init__ must store the logger on the instance."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)
    assert decorator.logger is logger


def test_logged_function_wraps_preserves_metadata_and_logs_call_and_result():
    """Lines 56-77: decorating a function wraps it, logs inputs and result."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def add(a, b=0):
        """Add two numbers."""
        return a + b

    # functools.wraps (line 56) preserves the wrapped function's metadata
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."

    result = add(1, b=2)
    assert result == 3

    # Two debug calls expected: one for the input, one for the result
    assert logger.debug.call_count == 2
    input_msg = logger.debug.call_args_list[0].args[0]
    assert input_msg == "add(1, b=2)"
    result_msg = logger.debug.call_args_list[1].args[0]
    assert result_msg == "add -> 3"


def test_logged_function_none_result_is_not_logged():
    """Branch at line 73: a None result must not produce a result log line."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def do_nothing():
        return None

    result = do_nothing()
    assert result is None

    # Only the input log line, no "do_nothing -> ..." line
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0].args[0] == "do_nothing()"


def test_logged_function_falsy_result_is_still_logged():
    """Branch at line 73: falsy-but-not-None results must still be logged."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def zero():
        return 0

    assert zero() == 0
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[1].args[0] == "zero -> 0"


def test_logged_function_string_args_are_formatted_with_quotes():
    """Lines 59-64: string args go through format_arg (stripped and quoted)."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)

    @decorator
    def greet(name, punctuation):
        return "hello"

    result = greet(" world ", punctuation="!")
    assert result == "hello"

    input_msg = logger.debug.call_args_list[0].args[0]
    assert input_msg == "greet('world', punctuation='!')"


def test_logged_function_applied_explicitly_and_exception_propagates():
    """Lines 56-77: decorator usable without @-syntax; exceptions propagate."""
    logger = mock.Mock(name="logger")
    decorator = LoggedFunction(logger)

    def boom():
        raise ValueError("boom")

    wrapped = decorator(boom)
    assert wrapped.__name__ == "boom"

    with pytest.raises(ValueError, match="boom"):
        wrapped()

    # The input was still logged before the exception was raised
    assert logger.debug.call_count == 1
    assert logger.debug.call_args_list[0].args[0] == "boom()"
