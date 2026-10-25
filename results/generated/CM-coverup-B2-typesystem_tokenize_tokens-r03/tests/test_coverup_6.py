# file: project/typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

from typesystem.tokenize.tokens import Token


def test_lookup_key_uses_parent_index_and_returns_key_token(monkeypatch):
    root = Token(value=None, start_index=0, end_index=0, content="")
    expected = object()
    calls = []

    class ParentToken:
        def _get_key_token(self, key):
            calls.append(("get_key_token", key))
            return expected

    parent = ParentToken()

    def fake_lookup(self, index):
        calls.append(("lookup", self, index))
        return parent

    monkeypatch.setattr(Token, "lookup", fake_lookup)

    index = ["parent", "child"]
    result = root.lookup_key(index)

    assert result is expected
    assert calls == [
        ("lookup", root, ["parent"]),
        ("get_key_token", "child"),
    ]
    assert index == ["parent", "child"]
