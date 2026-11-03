# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_stores_code_and_original_error():
    original_error = ValueError("invalid literal for ast.literal_eval")
    code = "isort:off"

    error = LiteralParsingFailure(code, original_error)

    # Postconditions: the attributes passed to the constructor are stored.
    assert error.code == code
    assert error.original_error is original_error

    # The exception participates in the isort exception hierarchy.
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_parsing_failure_message_contains_code_and_error():
    original_error = SyntaxError("unexpected token")
    code = "isort:on"

    error = LiteralParsingFailure(code, original_error)

    message = str(error)
    # The formatted message produced in __init__ must mention the code,
    # the explanation about literal sorting, and the original error.
    assert f"isort failed to parse the given literal {code}." in message
    assert (
        "isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval" in message
    )
    assert f"gave the exception of {original_error}." in message
