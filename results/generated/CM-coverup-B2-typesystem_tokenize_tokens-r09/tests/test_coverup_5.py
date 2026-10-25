# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import Token


def test_token_equality_with_matching_values_and_indexes(monkeypatch):
    monkeypatch.setattr(Token, "_get_value", lambda self: self._value)

    left = Token("value", 1, 5)
    right = Token("value", 1, 5)

    assert left == right


def test_token_equality_rejects_each_difference(monkeypatch):
    monkeypatch.setattr(Token, "_get_value", lambda self: self._value)

    token = Token("value", 1, 5)

    assert not (token == object())
    assert not (token == Token("different", 1, 5))
    assert not (token == Token("value", 2, 5))
    assert not (token == Token("value", 1, 6))
