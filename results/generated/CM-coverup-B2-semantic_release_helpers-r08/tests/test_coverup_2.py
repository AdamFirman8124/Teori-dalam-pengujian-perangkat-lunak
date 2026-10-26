# file: project/semantic_release/helpers.py:42-77
# asked: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [53, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

import logging
from unittest import mock

import pytest

from semantic_release.helpers import LoggedFunction


@pytest.fixture
def mock_logger():
    """A mock logger that records debug() calls."""
    logger = mock.Mock(spec=logging.Logger)
    return logger


def test_logged_function_stores_logger(mock_logger):
    lf = LoggedFunction(mock_logger)
    assert lf.logger is mock_logger


def test_logged_function_logs_args_and_result(mock_logger):
    lf = LoggedFunction(mock_logger)

    @lf
    def add(a, b=0):
        return a + b

    result = add(1, b=2)

    assert result == 3
    # functools.wraps preserves metadata
    assert add.__name__ == "add"
    # Two debug calls: one for input args, one for the result
    assert mock_logger.debug.call_count == 2
    first_call = mock_logger.debug.call_args_list[0][0][0]
    second_call = mock_logger.debug.call_args_list[1][0][0]
    assert first_call == "add(1, b=2)"
    assert second_call == "add -> 3"


def test_logged_function_string_args_are_quoted(mock_logger):
    lf = LoggedFunction(mock_logger)

    @lf
    def greet(name):
        return None

    result = greet(" world ")

    assert result is None
    # Only the input-args debug call happens; no result log for None
    assert mock_logger.debug.call_count == 1
    logged = mock_logger.debug.call_args_list[0][0][0]
    # format_arg strips and quotes strings
    assert logged == "greet('world')"


def test_logged_function_returns_none_without_result_log(mock_logger):
    lf = LoggedFunction(mock_logger)

    @lf
    def nothing():
        return None

    result = nothing()

    assert result is None
    assert mock_logger.debug.call_count == 1
    logged = mock_logger.debug.call_args_list[0][0][0]
    assert logged == "nothing()"


def test_logged_function_with_real_logger(caplog):
    lf = LoggedFunction(logging.getLogger("test.logged_function"))

    @lf
    def multiply(x, y):
        return x * y

    with caplog.at_level(logging.DEBUG, logger="test.logged_function"):
        result = multiply(3, y=4)

    assert result == 12
    messages = [rec.message for rec in caplog.records]
    assert "multiply(3, y=4)" in messages
    assert "multiply -> 12" in messages
