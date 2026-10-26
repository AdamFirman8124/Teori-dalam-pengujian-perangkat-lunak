# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_initializes_message_and_attributes():
    code = "{'invalid': object()}"
    original_error = ValueError("malformed literal")

    error = LiteralParsingFailure(code, original_error)

    expected_message = (
        f"isort failed to parse the given literal {code}. "
        "It's important to note that isort literal sorting only supports "
        f"simple literals parsable by ast.literal_eval which gave the exception of "
        f"{original_error}."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.code is code
    assert error.original_error is original_error
