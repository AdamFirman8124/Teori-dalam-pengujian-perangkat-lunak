# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_initialization() -> None:
    code = '{"invalid": object()}'
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert isinstance(error, ISortError)
    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
