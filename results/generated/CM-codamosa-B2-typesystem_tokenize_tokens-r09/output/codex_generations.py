

# Generated at 2026-11-02 18:55:33.727100
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"a": {"b": 1}}'

    key_a = ScalarToken("a", 1, 2, content)
    key_b = ScalarToken("b", 7, 8, content)
    value_1 = ScalarToken(1, 12, 12, content)
    inner = DictToken({key_b: value_1}, 6, 13, content)
    outer = DictToken({key_a: inner}, 0, 14, content)

    # Lookup a nested key token.
    token = outer.lookup_key(["a", "b"])
    assert token == key_b
    assert token.value == "b"
    assert token.start == Position(1, 8, 7)
    assert token.end == Position(1, 9, 8)

    # Lookup a top-level key token.
    token = outer.lookup_key(["a"])
    assert token == key_a
    assert token.value == "a"
    assert token.start == Position(1, 2, 1)
    assert token.end == Position(1, 3, 2)

    # Lookup of a missing key raises KeyError.
    with pytest.raises(KeyError):
        outer.lookup_key(["a", "c"])

# Generated at 2026-11-02 18:56:51.029085
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(value="abc", start_index=0, end_index=2, content="abc")
    assert hash(token) == hash("abc")
    assert token.__hash__() == hash("abc")


def test_ScalarToken___hash___integer():
    token = ScalarToken(value=123, start_index=0, end_index=2, content="123")
    assert hash(token) == hash(123)


def test_ScalarToken___hash___equal_values_hash_equal():
    token_a = ScalarToken(value=1, start_index=0, end_index=0, content="1")
    token_b = ScalarToken(value=1, start_index=7, end_index=7, content="xx1")
    assert hash(token_a) == hash(token_b)


def test_ScalarToken___hash___different_values_hash_differ():
    token_a = ScalarToken(value=1, start_index=0, end_index=0, content="1")
    token_b = ScalarToken(value=2, start_index=0, end_index=0, content="2")
    assert hash(token_a) != hash(token_b)

# Generated at 2026-11-02 18:57:30.020884
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokenize.tokens import DictToken, ScalarToken
    from typesystem.base import Position

    # --- Basic construction with scalar children ---
    key_token = ScalarToken("key", 1, 5)
    value_token = ScalarToken("value", 8, 14)
    content = '{"key": "value"}'
    value = {key_token: value_token}

    token = DictToken(value, 0, len(content) - 1, content=content)

    # Attributes set via super().__init__
    assert token._value == value
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    # Child mappings built by the constructor
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}

    # Derived properties
    assert token.value == {"key": "value"}
    assert token.string == content
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, len(content), len(content) - 1)

    # --- Construction with multiple children ---
    key1 = ScalarToken("a", 0, 2)
    val1 = ScalarToken(1, 6, 6)
    key2 = ScalarToken("b", 10, 12)
    val2 = ScalarToken(2, 16, 16)
    content2 = '{"a": 1, "b": 2}'
    token2 = DictToken({key1: val1, key2: val2}, 0, len(content2) - 1, content=content2)

    assert token2._child_keys == {"a": key1, "b": key2}
    assert token2._child_tokens == {"a": val1, "b": val2}
    assert token2.value == {"a": 1, "b": 2}
    assert token2.lookup(["a"]) == val1
    assert token2.lookup_key(["b"]) == key2

    # --- Empty dict token ---
    empty_token = DictToken({}, 0, 1, content="{}")
    assert empty_token._child_keys == {}
    assert empty_token._child_tokens == {}
    assert empty_token.value == {}

    # --- Construction without content (default "") ---
    bare_token = DictToken({key1: val1}, 0, 5)
    assert bare_token._content == ""
    assert bare_token._child_keys == {"a": key1}
    assert bare_token._child_tokens == {"a": val1}
    assert bare_token.value == {"a": 1}

    # --- Nested dict token ---
    inner = DictToken({ScalarToken("x", 0, 2): ScalarToken(True, 4, 7)}, 0, 8)
    outer_key = ScalarToken("nested", 0, 7)
    outer = DictToken({outer_key: inner}, 0, 20, content='{"nested": {"x": true}}')
    assert outer._child_tokens == {"nested": inner}
    assert outer.value == {"nested": {"x": True}}
    assert outer.lookup(["nested", "x"]).value is True

    # --- repr and equality ---
    assert repr(token) == "DictToken('%s')" % content
    assert token == DictToken(value, 0, len(content) - 1, content=content)
    assert token != token2

# Generated at 2026-11-02 18:58:25.497849
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(value="test", start_index=0, end_index=3, content="test content")

    # Verify constructor attributes are set correctly
    assert token._value == "test"
    assert token._start_index == 0
    assert token._end_index == 3
    assert token._content == "test content"

    # Verify default content argument is empty string
    token_default = ScalarToken("value", 5, 9)
    assert token_default._content == ""

    # Verify value property returns the underlying scalar value
    assert token.value == "test"
    assert token_default.value == "value"

    # Verify hash is based on the scalar value
    assert hash(token) == hash("test")

    # Verify string property slices content by indices
    assert token.string == "tes"
    assert token_default.string == ""

    # Verify repr
    assert repr(token) == "ScalarToken('tes')"

    # Verify equality with an equivalent token
    token_other = ScalarToken("test", 0, 3, "test content")
    assert token == token_other

    # Verify inequality with different value
    token_diff = ScalarToken("other", 0, 3, "test content")
    assert not (token == token_diff)

# Generated at 2026-11-02 18:59:56.102526
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(value="abc", start_index=0, end_index=2, content="abc")
    assert hash(token) == hash("abc")


def test_ScalarToken___hash___integer_value():
    token = ScalarToken(value=42, start_index=1, end_index=2, content=" 42")
    assert hash(token) == hash(42)


def test_ScalarToken___hash___equal_tokens_hash_equal():
    token_one = ScalarToken(value="x", start_index=0, end_index=0, content="x")
    token_two = ScalarToken(value="x", start_index=0, end_index=0, content="x")
    assert hash(token_one) == hash(token_two)