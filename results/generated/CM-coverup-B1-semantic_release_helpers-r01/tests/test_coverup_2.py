# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

from unittest import mock

import pytest

from semantic_release.helpers import LoggedFunction


def test_logged_function_init_stores_logger():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    assert logged.logger is logger


def test_logged_function_call_returns_wrapped_function():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    def my_func(a, b=2):
        """Docstring."""
        return a + b

    wrapped = logged(my_func)

    assert wrapped is not my_func
    assert wrapped.__name__ == "my_func"
    assert wrapped.__doc__ == "Docstring."
    assert wrapped.__wrapped__ is my_func
    assert logger.debug.call_count == 0


def test_logged_function_logs_args_kwargs_and_result():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def add(a, b=0):
        return a + b

    assert add(1, b=2) == 3
    assert logger.debug.call_args_list == [
        mock.call("add(1, b=2)"),
        mock.call("add -> 3"),
    ]


def test_logged_function_logs_multiple_args_and_kwargs():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def combine(a, b, c=None, d=None):
        return (a, b, c, d)

    result = combine(1, "  two  ", c=[3], d={"k": "v"})

    assert result == (1, "  two  ", [3], {"k": "v"})
    assert logger.debug.call_args_list == [
        mock.call("combine(1, 'two', c=[3], d={'k': 'v'})"),
        mock.call("combine -> (1, '  two  ', [3], {'k': 'v'})"),
    ]


def test_logged_function_with_no_arguments():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def constant():
        return 42

    assert constant() == 42
    assert logger.debug.call_args_list == [
        mock.call("constant()"),
        mock.call("constant -> 42"),
    ]


def test_logged_function_does_not_log_none_result():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def noop(x):
        return None

    assert noop("  hi  ") is None
    assert logger.debug.call_args_list == [mock.call("noop('hi')")]


def test_logged_function_propagates_exceptions_without_logging_result():
    logger = mock.MagicMock()
    logged = LoggedFunction(logger)

    @logged
    def boom(x):
        raise ValueError("kaboom")

    with pytest.raises(ValueError, match="kaboom"):
        boom(7)

    assert logger.debug.call_args_list == [mock.call("boom(7)")]
