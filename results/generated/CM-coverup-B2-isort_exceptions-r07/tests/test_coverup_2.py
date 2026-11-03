# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_stores_code_and_original_error():
    original_error = ValueError("invalid literal for ast.literal_eval")
    code = "isort:skip"

    error = LiteralParsingFailure(code=code, original_error=original_error)

    # Postconditions: the attributes set on lines 104-105 are correct
    assert error.code == code
    assert error.original_error is original_error

    # The message built on lines 99-103 mentions both the code and the original error
    message = str(error)
    assert f"isort failed to parse the given literal {code}" in message
    assert "ast.literal_eval" in message
    assert str(original_error) in message

    # Inheritance postconditions
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_literal_parsing_failure_can_be_raised_and_caught():
    original_error = SyntaxError("bad syntax")
    code = "isort:off"

    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code=code, original_error=original_error)

    assert exc_info.value.code == code
    assert exc_info.value.original_error is original_error
    assert code in str(exc_info.value)
    assert str(original_error) in str(exc_info.value)
