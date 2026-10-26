# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import LiteralParsingFailure


def test_literal_parsing_failure_message_and_attributes():
    code = "sort_within_sections"
    original_error = ValueError("invalid literal for int() with base 10: 'abc'")

    exc = LiteralParsingFailure(code, original_error)

    # Lines 99-103: message is built via super().__init__
    assert (
        str(exc)
        == "isort failed to parse the given literal sort_within_sections. "
        "It's important to note that isort literal sorting only supports simple "
        "literals parsable by ast.literal_eval which gave the exception of "
        "invalid literal for int() with base 10: 'abc'."
    )
    # Line 104: code attribute is set
    assert exc.code == code
    # Line 105: original_error attribute is set
    assert exc.original_error is original_error
    # Postcondition: it is an ISortError / Exception subclass instance
    assert isinstance(exc, Exception)


def test_literal_parsing_failure_with_different_inputs():
    code = "literal_type"
    original_error = SyntaxError("unexpected EOF while parsing")

    exc = LiteralParsingFailure(code, original_error)

    assert code in str(exc)
    assert str(original_error) in str(exc)
    assert exc.code == code
    assert exc.original_error is original_error
