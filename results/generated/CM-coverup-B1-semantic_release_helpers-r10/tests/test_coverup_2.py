# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import MagicMock
from semantic_release.helpers import LoggedFunction


def test_logged_function_init_stores_logger():
    logger = MagicMock()
    decorator = LoggedFunction(logger)
    assert decorator.logger is logger


def test_logged_function_with_args_and_return_value():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def my_func(a, b):
        """my doc"""
        return a + b

    wrapped = decorator(my_func)
    # functools.wraps preserved metadata
    assert wrapped.__name__ == "my_func"
    assert wrapped.__doc__ == "my doc"

    result = wrapped(1, 2)

    assert result == 3
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "my_func(1, 2)"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == "my_func -> 3"


def test_logged_function_with_args_kwargs_and_string_formatting():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def greet(name, greeting="hello"):
        return f"{greeting} {name}"

    wrapped = decorator(greet)
    result = wrapped("  world  ", greeting="  hi  ")

    # format_arg strips strings and adds quotes
    assert result == "  hi     world  "
    assert logger.debug.call_count == 2
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "greet('world', greeting='hi')"
    second_call = logger.debug.call_args_list[1][0][0]
    assert second_call == f"greet -> {result}"


def test_logged_function_none_result_logs_once():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def do_nothing(x, y=None):
        return None

    wrapped = decorator(do_nothing)
    result = wrapped(10, y=20)

    assert result is None
    # only entry log, no return-value log
    assert logger.debug.call_count == 1
    first_call = logger.debug.call_args_list[0][0][0]
    assert first_call == "do_nothing(10, y=20)"


def test_logged_function_no_args_no_kwargs():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def get_value():
        return 42

    wrapped = decorator(get_value)
    result = wrapped()

    assert result == 42
    assert logger.debug.call_count == 2
    assert logger.debug.call_args_list[0][0][0] == "get_value()"
    assert logger.debug.call_args_list[1][0][0] == "get_value -> 42"
