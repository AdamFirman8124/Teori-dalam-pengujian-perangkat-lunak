# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_attributes_and_message():
    """Executing LiteralParsingFailure.__init__ (lines 99-105) and verifying postconditions."""
    code = "isort:skip"
    original_error = ValueError("bad literal")

    error = LiteralParsingFailure(code, original_error)

    # Lines 99-103: message built via super().__init__
    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    # Line 104: self.code assignment
    assert error.code == code
    # Line 105: self.original_error assignment
    assert error.original_error is original_error
    # Inheritance postconditions
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_parsing_failure_raises_and_is_catchable():
    """Ensure the exception propagates and carries its state when raised."""
    code = "isort:off"
    original_error = SyntaxError("invalid syntax")

    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)

    assert exc_info.value.code == code
    assert exc_info.value.original_error is original_error
    assert code in str(exc_info.value)
    assert str(original_error) in str(exc_info.value)
