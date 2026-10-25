# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

from isort.exceptions import ISortError, LiteralParsingFailure


def test_literal_parsing_failure_init_attributes():
    code = "['b', 'a',]"
    original_error = ValueError("malformed node")
    exc = LiteralParsingFailure(code, original_error)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.code == code
    assert exc.original_error is original_error
    assert exc.args[0] == str(exc)


def test_literal_parsing_failure_message_contents():
    code = "{1, 2,}"
    original_error = SyntaxError("unexpected EOF")
    exc = LiteralParsingFailure(code, original_error)
    msg = str(exc)
    assert code in msg
    assert str(original_error) in msg
    assert "isort failed to parse the given literal" in msg
    assert "ast.literal_eval" in msg


def test_literal_parsing_failure_raise_and_catch():
    code = "my_code"
    original_error = TypeError("bad type")
    with __import__("pytest").raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)
    assert exc_info.value.code == code
    assert exc_info.value.original_error is original_error
    assert code in str(exc_info.value)
