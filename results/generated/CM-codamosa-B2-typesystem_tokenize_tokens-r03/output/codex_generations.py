

# Generated at 2026-11-03 00:30:56.072852
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    from typesystem.base import Position

    # Constructor with all arguments
    token = ScalarToken(value=123, start_index=4, end_index=6, content="abc 123 xyz")
    assert token._value == 123
    assert token._start_index == 4
    assert token._end_index == 6
    assert token._content == "abc 123 xyz"

    # Value property returns the raw scalar value
    assert token.value == 123

    # String property slices content between start and end index (inclusive)
    assert token.string == "123"

    # Start/end positions computed from content
    assert token.start == Position(line_no=1, column_no=5, char_index=4)
    assert token.end == Position(line_no=1, column_no=7, char_index=6)

    # Constructor with default (empty) content
    token = ScalarToken("hello", 0, 4)
    assert token._value == "hello"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == ""
    assert token.value == "hello"
    assert token.string == ""

    # ScalarToken is hashable, hashing based on the underlying value
    assert hash(token) == hash("hello")

    # Equality with an equivalent token
    other = ScalarToken("hello", 0, 4)
    assert token == other
    assert token != ScalarToken("hello", 0, 3)
    assert token != ScalarToken("world", 0, 4)
    assert token != "hello"

    # Repr includes class name and string content
    token = ScalarToken(1, 0, 0, content="1")
    assert repr(token) == "ScalarToken('1')"

    # Works with non-string scalar values such as booleans and floats
    token = ScalarToken(True, 0, 3, content="true")
    assert token.value is True
    assert hash(token) == hash(True)

# Generated at 2026-11-03 00:32:29.062372
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "{'key': 'value'}"
    key_token = ScalarToken("key", 1, 5, content)
    value_token = ScalarToken("value", 7, 13, content)

    # Constructor with positional args
    token = DictToken({key_token: value_token}, 0, 15, content)
    assert token.value == {"key": "value"}
    assert token.string == content
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 16, 15)

    # Constructor with keyword args
    token = DictToken(value={key_token: value_token}, start_index=0, end_index=15, content=content)
    assert token.value == {"key": "value"}
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token
    assert repr(token) == "DictToken(%r)" % content
    assert token == DictToken({key_token: value_token}, 0, 15, content)
    assert token != value_token

    # Constructor with empty dict value
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty.start == Position(1, 1, 0)
    assert empty.end == Position(1, 2, 1)

# Generated at 2026-11-03 00:33:15.402623
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    # Hash of a scalar token equals the hash of its underlying value
    token = ScalarToken(value="hello", start_index=0, end_index=4, content='"hello"')
    assert hash(token) == hash("hello")

    # Hash consistency with equality: equal tokens have equal hashes
    same = ScalarToken(value="hello", start_index=0, end_index=4, content='"hello"')
    assert token == same
    assert hash(token) == hash(same)

    # Hash is based only on the value, not on indices
    other = ScalarToken(value="hello", start_index=10, end_index=14, content='xx"hello"yy')
    assert token != other
    assert hash(token) == hash(other)

    # Works with non-string scalar values
    int_token = ScalarToken(value=123, start_index=0, end_index=2, content="123")
    assert hash(int_token) == hash(123)

    none_token = ScalarToken(value=None, start_index=0, end_index=3, content="null")
    assert hash(none_token) == hash(None)

    # Tokens are usable in hash-based collections
    tokens = {token, other, same}
    assert len(tokens) == 2  # token and same collapse, other kept

    mapping = {int_token: "a"}
    mapping[ScalarToken(value=123, start_index=5, end_index=7, content="abc 123")] = "b"
    assert len(mapping) == 1
    assert mapping[int_token] == "b"

# Generated at 2026-11-03 00:33:51.231414
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("a", 0, 0, content="a")

    # Equal tokens: same value, start index, and end index.
    assert token == ScalarToken("a", 0, 0, content="a")

    # Different value.
    assert token != ScalarToken("b", 0, 0, content="b")

    # Different start index.
    assert token != ScalarToken("a", 1, 1, content="a")

    # Different end index.
    assert token != ScalarToken("a", 0, 1, content="a")

    # Comparison against non-Token objects is always unequal.
    assert token != "a"
    assert token != None
    assert token != object()

    # Equality works through subclass _get_value() implementations.
    list_token = ListToken(
        [ScalarToken(1, 0, 0), ScalarToken(2, 2, 2)], 0, 2, content="[1, 2]"
    )
    assert list_token == ListToken(
        [ScalarToken(1, 0, 0), ScalarToken(2, 2, 2)], 0, 2, content="[1, 2]"
    )
    assert list_token != ListToken(
        [ScalarToken(1, 0, 0), ScalarToken(3, 2, 2)], 0, 2, content="[1, 3]"
    )
    assert list_token != token

# Generated at 2026-11-03 00:34:42.872909
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    # Construct with all arguments
    token = ScalarToken(value="abc", start_index=0, end_index=2, content='"abc"')
    assert token._value == "abc"
    assert token._start_index == 0
    assert token._end_index == 2
    assert token._content == '"abc"'

    # Construct with default content
    token_default = ScalarToken(value=42, start_index=5, end_index=6)
    assert token_default._value == 42
    assert token_default._start_index == 5
    assert token_default._end_index == 6
    assert token_default._content == ""

    # value property returns the underlying value
    assert token.value == "abc"
    assert token_default.value == 42

    # string property slices the content
    assert token.string == "abc"

    # hash is based on the underlying value
    assert hash(token) == hash("abc")
    assert hash(token_default) == hash(42)

    # repr includes class name and string representation
    assert repr(token) == "ScalarToken('abc')"

    # equality compares value, start_index and end_index
    assert token == ScalarToken("abc", 0, 2)
    assert token != ScalarToken("xyz", 0, 2)
    assert token != ScalarToken("abc", 1, 2)
    assert token != ScalarToken("abc", 0, 1)
    assert token != "abc"
    assert token != None  # noqa: E711

# Generated at 2026-11-03 00:35:17.467841
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("a", 0, 0, content="abc")

    # Equal tokens: same value, start_index, end_index
    assert token == ScalarToken("a", 0, 0, content="xyz")

    # Different value
    assert not token == ScalarToken("b", 0, 0, content="abc")

    # Different start_index
    assert not token == ScalarToken("a", 1, 0, content="abc")

    # Different end_index
    assert not token == ScalarToken("a", 0, 1, content="abc")

    # Not a Token instance
    assert not token == "a"
    assert not token == None

    # Inequality operator works via default __ne__
    assert token != ScalarToken("b", 0, 0, content="abc")
    assert not (token != ScalarToken("a", 0, 0, content="abc"))

# Generated at 2026-11-03 00:36:27.314286
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    key_token = ScalarToken("key", 1, 5, content)
    value_token = ScalarToken("value", 8, 14, content)

    token = DictToken({key_token: value_token}, 0, 15, content)

    # Constructor builds child key/token maps from the dict of tokens
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}

    # Value is resolved recursively from child tokens
    assert token.value == {"key": "value"}

    # String is sliced from the source content
    assert token.string == content

    # Start/end positions
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 16, 15)

    # Child and key lookups
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

    # repr uses the sliced string
    assert repr(token) == "DictToken('" + content + "')"

    # Equality with an identically constructed token
    other = DictToken(
        {ScalarToken("key", 1, 5, content): ScalarToken("value", 8, 14, content)},
        0,
        15,
        content,
    )
    assert token == other
    assert token != key_token

    # Constructor with default (empty) content
    bare = DictToken({ScalarToken("k", 0, 0): ScalarToken(1, 0, 0)}, 0, 0)
    assert bare.value == {"k": 1}
    assert bare.string == ""
    assert bare.start == Position(1, 1, 0)
    assert bare.end == Position(1, 1, 0)

    # Nested dict tokens
    nested_content = '{"a": {"b": 1}}'
    b_key = ScalarToken("b", 7, 9, nested_content)
    b_val = ScalarToken(1, 12, 12, nested_content)
    inner = DictToken({b_key: b_val}, 6, 13, nested_content)
    a_key = ScalarToken("a", 1, 3, nested_content)
    outer = DictToken({a_key: inner}, 0, 14, nested_content)

    assert outer.value == {"a": {"b": 1}}
    assert outer.lookup(["a", "b"]) == b_val
    assert outer.lookup_key(["a", "b"]) == b_key
    assert outer.start == Position(1, 1, 0)
    assert outer.end == Position(1, 15, 14)

# Generated at 2026-11-03 00:37:59.062614
# Unit test for method lookup of class Token
def test_Token_lookup():
    # Lookup within a DictToken
    content = '{"name": "Alice"}'
    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    dict_token = DictToken({key_token: value_token}, 0, 16, content)

    result = dict_token.lookup(["name"])
    assert result == value_token
    assert result.value == "Alice"
    assert result.string == '"Alice"'
    assert result.start == Position(1, 10, 9)
    assert result.end == Position(1, 16, 15)

    # Lookup within a ListToken
    content = "[1, 2]"
    first = ScalarToken(1, 1, 1, content)
    second = ScalarToken(2, 4, 4, content)
    list_token = ListToken([first, second], 0, 5, content)

    assert list_token.lookup([0]) == first
    assert list_token.lookup([1]) == second
    assert list_token.lookup([0]).value == 1

    # Lookup with a nested index (dict -> list -> dict)
    content = '{"a": [1, {"b": 2}]}'
    key_a = ScalarToken("a", 1, 3, content)
    one = ScalarToken(1, 7, 7, content)
    key_b = ScalarToken("b", 11, 13, content)
    two = ScalarToken(2, 16, 16, content)
    inner = DictToken({key_b: two}, 10, 17, content)
    items = ListToken([one, inner], 6, 18, content)
    outer = DictToken({key_a: items}, 0, 19, content)

    assert outer.lookup(["a", 1, "b"]) == two
    assert outer.lookup(["a", 1, "b"]).value == 2
    assert outer.lookup(["a"]).value == [1, {"b": 2}]

    # Empty index returns the token itself
    scalar = ScalarToken(42, 0, 1, "42")
    assert scalar.lookup([]) == scalar

    # Missing key raises KeyError
    with pytest.raises(KeyError):
        dict_token.lookup(["missing"])

    # Out of range index raises IndexError
    with pytest.raises(IndexError):
        list_token.lookup([5])

# Generated at 2026-11-03 00:39:48.007392
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"a": 1, "b": [2, 3]}'
    key_a = ScalarToken("a", 2, 2, content)
    key_b = ScalarToken("b", 10, 10, content)
    value_1 = ScalarToken(1, 6, 6, content)
    scalar_2 = ScalarToken(2, 15, 15, content)
    scalar_3 = ScalarToken(3, 18, 18, content)
    list_token = ListToken([scalar_2, scalar_3], 14, 19, content)

    token = DictToken({key_a: value_1, key_b: list_token}, 0, 20, content)

    # Constructor should index child key tokens and child value tokens
    assert token._value == {key_a: value_1, key_b: list_token}
    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_tokens == {"a": value_1, "b": list_token}

    # Resolved value should map key token values to value token values
    assert token.value == {"a": 1, "b": [2, 3]}

    # String and position properties
    assert token.string == content
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 21, 20)

    # Lookup of child tokens and key tokens
    assert token.lookup(["a"]).value == 1
    assert token.lookup(["b", 0]).value == 2
    assert token.lookup_key(["a"]) == key_a
    assert token.lookup_key(["b"]) == key_b

    # Equality against an identical token
    same = DictToken(
        {ScalarToken("a", 2, 2, content): ScalarToken(1, 6, 6, content),
         ScalarToken("b", 10, 10, content): ListToken(
             [ScalarToken(2, 15, 15, content), ScalarToken(3, 18, 18, content)],
             14, 19, content)},
        0, 20, content,
    )
    assert token == same

    # Empty dictionary token
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}
    assert empty.string == "{}"
    assert empty.start == Position(1, 1, 0)
    assert empty.end == Position(1, 2, 1)