# file: project/typesystem/tokenize/tokens.py:40-47
# asked: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}
# gained: {"lines": [44, 45, 46, 47], "branches": [[45, 46], [45, 47]]}

from typesystem.tokenize.tokens import Token


class _ContainerToken(Token):
    """Minimal Token subclass that supports child token lookups by key."""

    def __init__(self, value, start_index, end_index, content="", children=None):
        super().__init__(value, start_index, end_index, content)
        self._children = dict(children or {})

    def _get_value(self):
        return self._value

    def _get_child_token(self, key):
        return self._children[key]


def test_lookup_with_empty_index_returns_self():
    # Covers 'token = self' and 'return token' with the loop body skipped.
    # Note: base Token.value raises NotImplementedError, so inspect _value.
    token = Token(value="scalar", start_index=0, end_index=6, content="scalar")

    result = token.lookup([])

    assert result is token
    assert result._value == "scalar"


def test_lookup_with_single_key_returns_child_token():
    # Covers the loop body 'token = token._get_child_token(key)' once.
    content = '{"a": 1}'
    child = _ContainerToken(1, 6, 7, content=content)
    root = _ContainerToken({"a": 1}, 0, 8, content=content, children={"a": child})

    result = root.lookup(["a"])

    assert result is child
    assert result.value == 1


def test_lookup_with_nested_index_traverses_structure():
    # Covers repeated iterations of the loop body across nesting levels.
    content = '{"a": {"b": 2}}'
    grandchild = _ContainerToken(2, 11, 12, content=content)
    child = _ContainerToken(
        {"b": 2}, 6, 13, content=content, children={"b": grandchild}
    )
    root = _ContainerToken(
        {"a": {"b": 2}}, 0, 14, content=content, children={"a": child}
    )

    assert root.lookup(["a"]) is child
    assert root.lookup(["a", "b"]) is grandchild
    assert root.lookup(["a", "b"]).value == 2


def test_lookup_passes_each_key_to_get_child_token(monkeypatch):
    # Verifies lookup delegates to _get_child_token with the index keys,
    # patching only the test-local instance so no global state is touched.
    root = Token("root", 0, 10)
    child = Token("child", 5, 10)
    received_keys = []

    def fake_get_child_token(key):
        received_keys.append(key)
        return child

    monkeypatch.setattr(
        root, "_get_child_token", fake_get_child_token, raising=False
    )

    result = root.lookup(["k"])

    assert result is child
    assert received_keys == ["k"]
