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

    # Postconditions: attributes are stored correctly (lines 104-105)
    assert error.code == code
    assert error.original_error is original_error

    # The message built by super().__init__ (lines 99-103) contains all parts
    message = str(error)
    assert "isort failed to parse the given literal isort:skip." in message
    assert (
        "It's important to note that isort literal sorting only supports "
        "simple literals parsable by ast.literal_eval" in message
    )
    assert "which gave the exception of bad literal." in message

    # Inheritance postcondition
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_parsing_failure_with_various_errors():
    """Ensure __init__ works with different exception types and codes."""
    for code, original_error in [
        ("isort:off", SyntaxError("invalid syntax")),
        ("", KeyError("missing")),
    ]:
        error = LiteralParsingFailure(code, original_error)
        assert error.code == code
        assert error.original_error is original_error
        assert f"given literal {code}." in str(error)
        assert f"exception of {original_error}." in str(error)
