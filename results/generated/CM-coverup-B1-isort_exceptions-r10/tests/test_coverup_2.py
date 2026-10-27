# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_attributes_and_message():
    code = "my_broken_literal"
    original_error = ValueError("malformed node")
    exc = LiteralParsingFailure(code, original_error)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.code == code
    assert exc.original_error is original_error
    message = str(exc)
    assert code in message
    assert str(original_error) in message
    assert "ast.literal_eval" in message
    assert "isort failed to parse the given literal" in message
    assert exc.args[0] == message


def test_literal_parsing_failure_raised_and_caught():
    code = "[1, 2,"
    original_error = SyntaxError("unexpected EOF")
    with __import__("pytest").raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)
    exc = exc_info.value
    assert exc.code == code
    assert exc.original_error is original_error
    assert code in str(exc)
    assert str(original_error) in str(exc)


def test_literal_parsing_failure_preserves_original_error_identity():
    code = "{'a': 1,}"
    original_error = TypeError("literal error")
    exc = LiteralParsingFailure(code=code, original_error=original_error)
    assert exc.code == code
    assert exc.original_error is original_error
    assert "isort literal sorting only supports simple literals" in str(exc)
