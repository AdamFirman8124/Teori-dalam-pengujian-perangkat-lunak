# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

from isort.exceptions import LiteralParsingFailure


def test_literal_parsing_failure_initialization() -> None:
    code = '{"invalid": value}'
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    expected_message = (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.code == code
    assert error.original_error is original_error
