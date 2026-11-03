# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_attributes_and_message():
    """Executing lines 99-105: __init__ of LiteralParsingFailure."""
    code = "isort:skip"
    original_error = ValueError("bad literal")

    error = LiteralParsingFailure(code, original_error)

    # Postconditions: attributes are stored correctly (lines 104-105).
    assert error.code == code
    assert error.original_error is original_error

    # The message built in super().__init__ (lines 99-103) includes both inputs.
    message = str(error)
    assert code in message
    assert str(original_error) in message
    assert "isort failed to parse the given literal" in message
    assert "ast.literal_eval" in message

    # Inheritance postconditions.
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_parsing_failure_with_various_errors():
    """Ensure the constructor works with different exception types."""
    for original_error in (SyntaxError("syntax problem"), KeyError("missing")):
        error = LiteralParsingFailure("isort:off", original_error)
        assert error.code == "isort:off"
        assert error.original_error is original_error
        assert str(original_error) in str(error)
