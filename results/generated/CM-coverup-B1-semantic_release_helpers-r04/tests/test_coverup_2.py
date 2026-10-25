# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import MagicMock

from semantic_release.helpers import LoggedFunction


def test_init_stores_logger():
    logger = MagicMock()
    decorator = LoggedFunction(logger)
    assert decorator.logger is logger


def test_call_with_positional_args_and_return_value():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def add(a, b):
        """Add two numbers."""
        return a + b

    wrapped = decorator(add)

    # functools.wraps preserved
    assert wrapped.__name__ == "add"

    result = wrapped(1, 2)

    assert result == 3
    # entry log + exit log
    assert logger.debug.call_count == 2
    entry_msg = logger.debug.call_args_list[0][0][0]
    assert "add" in entry_msg
    assert "1" in entry_msg
    assert "2" in entry_msg
    exit_msg = logger.debug.call_args_list[1][0][0]
    assert exit_msg == "add -> 3"


def test_call_with_kwargs_and_none_result_logs_once():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def greet(name, greeting="hello"):
        return None

    wrapped = decorator(greet)

    result = wrapped("world", greeting="hi")

    assert result is None
    # only entry log, no exit log when result is None
    assert logger.debug.call_count == 1
    entry_msg = logger.debug.call_args[0][0]
    assert "greet" in entry_msg
    assert "'world'" in entry_msg
    assert "greeting='hi'" in entry_msg


def test_call_with_no_args_and_string_result():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def get_value():
        return "val"

    wrapped = decorator(get_value)

    result = wrapped()

    assert result == "val"
    assert logger.debug.call_count == 2
    entry_msg = logger.debug.call_args_list[0][0][0]
    assert entry_msg == "get_value()"
    exit_msg = logger.debug.call_args_list[1][0][0]
    assert exit_msg == "get_value -> val"


def test_call_with_mixed_args_and_kwargs():
    logger = MagicMock()
    decorator = LoggedFunction(logger)

    def func(a, b=" default "):
        return a

    wrapped = decorator(func)

    result = wrapped(42, b=" padded ")

    assert result == 42
    assert logger.debug.call_count == 2
    entry_msg = logger.debug.call_args_list[0][0][0]
    # format_arg strips strings
    assert "42" in entry_msg
    assert "b='padded'" in entry_msg
    exit_msg = logger.debug.call_args_list[1][0][0]
    assert exit_msg == "func -> 42"
