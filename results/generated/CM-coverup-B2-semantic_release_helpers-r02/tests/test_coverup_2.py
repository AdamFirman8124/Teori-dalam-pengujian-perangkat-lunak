# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest.mock import MagicMock
from semantic_release.helpers import LoggedFunction


def test_init_assigns_logger():
    mock_logger = MagicMock()
    decorator = LoggedFunction(mock_logger)
    assert decorator.logger is mock_logger


def test_call_with_args_and_return_value():
    mock_logger = MagicMock()
    decorator = LoggedFunction(mock_logger)

    @decorator
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3
    # functools.wraps preserved
    assert add.__name__ == "add"
    # entry log + exit log
    assert mock_logger.debug.call_count == 2
    entry_msg = mock_logger.debug.call_args_list[0][0][0]
    assert "add" in entry_msg
    assert "1" in entry_msg
    assert "2" in entry_msg
    exit_msg = mock_logger.debug.call_args_list[1][0][0]
    assert exit_msg == "add -> 3"


def test_call_with_kwargs_and_none_result():
    mock_logger = MagicMock()
    decorator = LoggedFunction(mock_logger)

    @decorator
    def greet(name="world"):
        return None

    result = greet(name="alice")
    assert result is None
    # only entry log when result is None
    assert mock_logger.debug.call_count == 1
    entry_msg = mock_logger.debug.call_args_list[0][0][0]
    assert "greet" in entry_msg
    assert "name" in entry_msg
    assert "alice" in entry_msg


def test_call_with_mixed_args_kwargs():
    mock_logger = MagicMock()
    decorator = LoggedFunction(mock_logger)

    @decorator
    def func(a, b=2):
        return a + b

    result = func(1, b=5)
    assert result == 6
    assert mock_logger.debug.call_count == 2
    entry_msg = mock_logger.debug.call_args_list[0][0][0]
    assert "func" in entry_msg
    assert "1" in entry_msg
    assert "b" in entry_msg
    assert "5" in entry_msg
    exit_msg = mock_logger.debug.call_args_list[1][0][0]
    assert "func -> 6" in exit_msg


def test_call_with_no_args():
    mock_logger = MagicMock()
    decorator = LoggedFunction(mock_logger)

    @decorator
    def no_args():
        return "hi"

    result = no_args()
    assert result == "hi"
    assert mock_logger.debug.call_count == 2
    entry_msg = mock_logger.debug.call_args_list[0][0][0]
    assert "no_args" in entry_msg
    exit_msg = mock_logger.debug.call_args_list[1][0][0]
    assert exit_msg == "no_args -> hi"
