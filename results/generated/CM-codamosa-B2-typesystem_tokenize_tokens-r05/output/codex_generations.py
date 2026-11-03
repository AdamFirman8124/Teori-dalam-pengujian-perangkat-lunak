

# Generated at 2026-11-01 23:47:56.845443
# Unit test for method lookup of class Token
def test_Token_lookup():
    # Build a nested structure: {"example": [123]}
    key_token = ScalarToken("example", 0, 8)
    value_token = ScalarToken(123, 12, 14)
    inner_list = ListToken([value_token], 11, 15)
    dict_token = DictToken({key_token: inner_list}, 0, 17, content='{"example": [123]}')

    # Lookup a direct child by key
    assert dict_token.lookup(["example"]) == inner_list

    # Lookup a nested child via a list index
    assert dict_token.lookup(["example", 0]) == value_token

    # Empty index returns the token itself
    assert dict_token.lookup([]) == dict_token

    # Missing key raises KeyError
    try:
        dict_token.lookup(["missing"])
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")

# Generated at 2026-11-01 23:48:33.277030
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '{"a": [1, 2, {"b": "hello"}]}'

    # Build token tree mirroring the content string
    hello = ScalarToken("hello", 19, 25, content)
    b_key = ScalarToken("b", 14, 16, content)
    inner_dict = DictToken({b_key: hello}, 13, 26, content)
    one = ScalarToken(1, 7, 7, content)
    two = ScalarToken(2, 10, 10, content)
    inner_list = ListToken([one, two, inner_dict], 6, 27, content)
    a_key = ScalarToken("a", 1, 3, content)
    root = DictToken({a_key: inner_list}, 0, 28, content)

    # Empty index returns the token itself
    assert root.lookup([]) is root

    # Single key lookup into a dict token
    assert root.lookup(["a"]) is inner_list

    # Integer index lookup into a list token
    assert root.lookup(["a", 0]) is one
    assert root.lookup(["a", 1]) is two
    assert root.lookup(["a", 2]) is inner_dict

    # Deeply nested lookup through dict -> list -> dict
    assert root.lookup(["a", 2, "b"]) is hello
    assert root.lookup(["a", 2, "b"]).value == "hello"
    assert root.lookup(["a", 2, "b"]).string == '"hello"'
    assert root.lookup(["a", 2, "b"]).start == Position(1, 20, 19)
    assert root.lookup(["a", 2, "b"]).end == Position(1, 26, 25)

    # Looking up a missing key raises KeyError
    import pytest

    with pytest.raises(KeyError):
        root.lookup(["missing"])

    with pytest.raises(KeyError):
        root.lookup(["a", 5])

    with pytest.raises(KeyError):
        root.lookup(["a", 2, "c"])

# Generated at 2026-11-01 23:49:34.424332
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken(value=1, start_index=0, end_index=3, content="[1]")

    # Same class, same value, same start/end indices -> equal
    assert token == ScalarToken(1, 0, 3, content="xyz")
    assert ScalarToken(1, 0, 3) == token

    # Different value -> not equal
    assert token != ScalarToken(2, 0, 3)
    assert not (token == ScalarToken(2, 0, 3))

    # Different start_index -> not equal
    assert token != ScalarToken(1, 1, 3)

    # Different end_index -> not equal
    assert token != ScalarToken(1, 0, 4)

    # Comparison against non-Token objects -> not equal
    assert token != 1
    assert token != "1"
    assert token != None
    assert token != [1]
    assert token != {}

    # Different container token types holding different values -> not equal
    dict_token = DictToken({}, 0, 1)
    list_token = ListToken([], 0, 1)
    assert dict_token != list_token
    assert not (dict_token == list_token)

    # DictTokens built from equivalent child tokens compare equal by resolved value
    key1 = ScalarToken("a", 1, 1, content='"a"')
    val1 = ScalarToken(1, 4, 4, content="1")
    dict_token_a = DictToken({key1: val1}, 0, 5, content='{"a": 1}')

    key2 = ScalarToken("a", 1, 1, content='"a"')
    val2 = ScalarToken(1, 4, 4, content="1")
    dict_token_b = DictToken({key2: val2}, 0, 5, content='{"a": 1}')

    assert dict_token_a == dict_token_b

    # Same resolved value but different indices -> not equal
    dict_token_c = DictToken({ScalarToken("a", 9, 9): ScalarToken(1, 12, 12)}, 7, 8)
    assert dict_token_a != dict_token_c

# Generated at 2026-11-01 23:50:46.430096
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    key_token = ScalarToken("key", 1, 5, content=content)
    value_token = ScalarToken("value", 8, 14, content=content)
    dict_token = DictToken({key_token: value_token}, 0, 15, content=content)

    # Constructor stores the raw token parts.
    assert dict_token._value == {key_token: value_token}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 15
    assert dict_token._content == content

    # Constructor indexes child key tokens and child value tokens.
    assert dict_token._child_keys == {"key": key_token}
    assert dict_token._child_tokens == {"key": value_token}

    # The value property resolves nested token values.
    assert dict_token.value == {"key": "value"}

    # String and positions are derived from content and indices.
    assert dict_token.string == content
    assert dict_token.start == Position(1, 1, 0)
    assert dict_token.end == Position(1, 16, 15)

    # Child tokens and key tokens can be looked up.
    assert dict_token.lookup(["key"]) == value_token
    assert dict_token.lookup_key(["key"]) == key_token

    # An empty dict token is handled correctly.
    empty_token = DictToken({}, 0, 1, content="{}")
    assert empty_token.value == {}
    assert empty_token._child_keys == {}
    assert empty_token._child_tokens == {}

# Generated at 2026-11-01 23:52:02.798714
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # A token equals itself.
    token = ScalarToken("a", 0, 0)
    assert token == token

    # Two tokens with the same value and indexes are equal.
    assert ScalarToken("a", 0, 0) == ScalarToken("a", 0, 0)

    # Content is not part of equality.
    assert ScalarToken("a", 0, 0, content="abc") == ScalarToken("a", 0, 0, content="xyz")

    # Different values are not equal.
    assert ScalarToken("a", 0, 0) != ScalarToken("b", 0, 0)

    # Different start indexes are not equal.
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Different end indexes are not equal.
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 0, 2)

    # Comparison against non-Token objects returns False (not NotImplemented).
    assert ScalarToken("a", 0, 0).__eq__("a") is False
    assert ScalarToken("a", 0, 0) != "a"
    assert ScalarToken(1, 0, 0) != 1
    assert ScalarToken(None, 0, 0) != None  # noqa: E711

    # DictToken equality is based on resolved values and outer indexes.
    def make_dict_token(key_start=0, key_end=4, value_start=7, value_end=13):
        return DictToken(
            {
                ScalarToken("key", key_start, key_end): ScalarToken(
                    "value", value_start, value_end
                )
            },
            start_index=0,
            end_index=14,
            content='{"key": "value"}',
        )

    assert make_dict_token() == make_dict_token()

    # Child token indexes don't affect equality, only resolved values do.
    assert make_dict_token(2, 6, 9, 15) == make_dict_token()

    assert make_dict_token() != ScalarToken("key", 0, 4)

    # ListToken equality is based on resolved values and outer indexes.
    def make_list_token(second=2):
        return ListToken(
            [ScalarToken(1, 0, 0), ScalarToken(second, 2, 2)],
            start_index=0,
            end_index=3,
            content="[1, %d]" % second,
        )

    assert make_list_token() == make_list_token()
    assert make_list_token() != make_list_token(second=3)
    assert make_list_token() != ScalarToken(1, 0, 0)

    # Different subclasses with equal resolved values and indexes are equal.
    assert ScalarToken([1], 0, 2) == ListToken([ScalarToken(1, 0, 0)], 0, 2)

# Generated at 2026-11-01 23:53:35.169473
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a": 123}'

# Generated at 2026-11-01 23:55:30.366674
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # Base Token: repr uses class name and the sliced string from content
    token = Token(value=None, start_index=0, end_index=4, content="hello")
    assert repr(token) == "Token('hello')"

    # Single character slice
    token = Token(value=None, start_index=2, end_index=2, content="abc")
    assert repr(token) == "Token('c')"

    # String containing a quote character is escaped by repr
    token = Token(value=None, start_index=0, end_index=2, content="a'b")
    assert repr(token) == 'Token("a\'b")'

    # ScalarToken: repr reflects the subclass name and content slice
    token = ScalarToken(value=42, start_index=1, end_index=3, content="abc 123 def")
    assert repr(token) == "ScalarToken(' 123')"

    # DictToken with empty dict value
    token = DictToken(value={}, start_index=0, end_index=1, content="{}")
    assert repr(token) == "DictToken('{}')"

    # ListToken with empty list value
    token = ListToken(value=[], start_index=0, end_index=1, content="[]")
    assert repr(token) == "ListToken('[]')"

    # Default content (empty string) with valid indices yields empty slice
    token = Token(value=None, start_index=0, end_index=0)
    assert repr(token) == "Token('')"

# Generated at 2026-11-01 23:56:44.610346
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = ScalarToken("abc", 0, 2, content="abc")
    assert repr(token) == "ScalarToken('abc')"

    token = ScalarToken("abc", 3, 7, content="key: 'abc',")
    assert repr(token) == "ScalarToken(\"'abc'\")"

    token = ScalarToken(123, 1, 3, content="[123]")
    assert repr(token) == "ScalarToken('123')"