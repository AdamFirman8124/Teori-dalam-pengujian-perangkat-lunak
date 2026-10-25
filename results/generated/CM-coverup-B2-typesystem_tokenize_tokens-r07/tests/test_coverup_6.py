# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from typesystem.tokenize.tokens import Token


def test_lookup_key_nested_index(monkeypatch):
    root = Token({"a": {"b": 1}}, 0, 10, content="")
    intermediate = Token({"b": 1}, 0, 10, content="")
    expected = Token("b", 1, 2, content="")

    child_calls = []

    def fake_get_child_token(self, key):
        child_calls.append((self, key))
        assert self is root
        assert key == "a"
        return intermediate

    def fake_get_key_token(self, key):
        assert self is intermediate
        assert key == "b"
        return expected

    monkeypatch.setattr(Token, "_get_child_token", fake_get_child_token)
    monkeypatch.setattr(Token, "_get_key_token", fake_get_key_token)

    result = root.lookup_key(["a", "b"])

    assert result is expected
    assert child_calls == [(root, "a")]


def test_lookup_key_single_key(monkeypatch):
    root = Token({"a": 1}, 0, 10, content="")
    expected = Token("a", 1, 2, content="")

    def fail_get_child_token(self, key):
        raise AssertionError("_get_child_token should not be called for empty prefix")

    def fake_get_key_token(self, key):
        assert self is root
        assert key == "a"
        return expected

    monkeypatch.setattr(Token, "_get_child_token", fail_get_child_token)
    monkeypatch.setattr(Token, "_get_key_token", fake_get_key_token)

    result = root.lookup_key(["a"])

    assert result is expected
