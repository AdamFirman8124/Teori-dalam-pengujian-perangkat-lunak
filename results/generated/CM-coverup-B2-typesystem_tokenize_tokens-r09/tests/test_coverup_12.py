# file: project/typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

from typesystem.base import Position
from typesystem.tokenize.tokens import Token


def test_token_end_returns_position_for_end_index():
    token = Token("abc", 0, 2, content="abc")
    end = token.end
    assert isinstance(end, Position)
    assert end == token._get_position(2)
    assert end == Position(1, 3, 2)


def test_token_end_with_multiline_content():
    token = Token("b", 2, 3, content="a\nb")
    end = token.end
    assert isinstance(end, Position)
    assert end == token._get_position(3)
    assert end == Position(2, 1, 3)


def test_token_end_with_empty_content():
    token = Token("", 0, 0, content="")
    end = token.end
    assert isinstance(end, Position)
    assert end == token._get_position(0)
    assert end == Position(1, 1, 0)


def test_token_end_uses_end_index_not_start_index():
    token = Token("xyz", 1, 2, content="xyz")
    assert token.end == token._get_position(2)
    assert token.end != token.start
