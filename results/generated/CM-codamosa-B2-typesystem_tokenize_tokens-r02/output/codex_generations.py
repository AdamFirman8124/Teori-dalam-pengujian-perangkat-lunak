

# Generated at 2026-11-02 06:48:45.242326
# Unit test for constructor of class Token
def test_Token():
# nonce:a5436a10
    # Basic construction with all arguments
    token = Token("value", 0, 4, content="value")
    assert token._value == "value"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == "value"

    # Default content is an empty string
    token = Token(123, 3, 5)
    assert token._value == 123
    assert token._start_index == 3
    assert token._end_index == 5
    assert token._content == ""

    # string property slices content inclusively between indexes
    token = Token(None, 2, 6, content="hello world")
    assert token.string == "lo wo"

    # repr uses class name and string slice
    assert repr(token) == "Token('lo wo')"

    # start/end positions computed from content and indexes
    token = Token(None, 0, 7, content="hello\nworld")
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=2, column_no=2, index=7)

    # position when content slice is empty
    token = Token(None, 0, 0, content="")
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=1, index=0)

# Generated at 2026-11-02 06:48:55.089119
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [1, 2]}'

    # A token is equal to itself.
    token = ScalarToken("a", 0, 0, content)
    assert token == token

    # Tokens with identical values and identical indices are equal.
    assert token == ScalarToken("a", 0, 0, content)

    # Tokens with different values are not equal.
    assert token != ScalarToken("b", 0, 0, content)

    # Tokens with different start indices are not equal.
    assert token != ScalarToken("a", 1, 0, content)

    # Tokens with different end indices are not equal.
    assert token != ScalarToken("a", 0, 1, content)

    # Comparison against non-Token objects returns False.
    assert token != "a"
    assert token != 42
    assert token != None
    assert token != ("a", 0, 0)

    # Equality is based on the resolved value and indices, not the class.
    assert ScalarToken({"a": 1}, 0, 4, content) == DictToken(
        {ScalarToken("a", 0, 0, content): ScalarToken(1, 4, 4, content)},
        0,
        4,
        content,
    )

    # Inequality via != is the negation of __eq__.
    assert not (token != ScalarToken("a", 0, 0, content))
    assert not (token == ScalarToken("b", 0, 0, content))

# Generated at 2026-11-02 06:49:20.477152
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"a": 1, "b": 2}'
    key_a = ScalarToken("a", 1, 3)
    value_a = ScalarToken(1, 6, 6)
    key_b = ScalarToken("b", 9, 11)
    value_b = ScalarToken(2, 14, 14)
    dict_token = DictToken({key_a: value_a, key_b: value_b}, 0, 15, content)

    # Lookup the key token for "a" at the top level.
    token = dict_token.lookup_key(["a"])
    assert token == key_a
    assert token.value == "a"
    assert token.string == '"a"'
    assert token.start == Position(1, 2, 1)
    assert token.end == Position(1, 4, 3)

    # Lookup the key token for "b" at the top level.
    token = dict_token.lookup_key(["b"])
    assert token == key_b
    assert token.value == "b"
    assert token.string == '"b"'


# Unit test for method lookup_key of class Token (nested structure)
def test_Token_lookup_key_nested():
    content = '{"a": {"b": 1}}'
    key_a = ScalarToken("a", 1, 3)
    key_b = ScalarToken("b", 7, 9)
    value_b = ScalarToken(1, 12, 12)
    inner = DictToken({key_b: value_b}, 6, 13, content)
    outer = DictToken({key_a: inner}, 0, 14, content)

    # Lookup a key token nested one level deep.
    token = outer.lookup_key(["a", "b"])
    assert token == key_b
    assert token.value == "b"
    assert token.start == Position(1, 8, 7)

    # Lookup a top-level key token through the nested token.
    assert inner.lookup_key(["b"]) == key_b
    assert outer.lookup_key(["a"]) == key_a

# Generated at 2026-11-02 06:49:38.021156
# Unit test for constructor of class Token
def test_Token():
    # Test constructor with all arguments provided
    token = Token(value="example", start_index=0, end_index=6, content="example text")
    assert token._value == "example"
    assert token._start_index == 0
    assert token._end_index == 6
    assert token._content == "example text"
    assert token.string == "example"

    # Test constructor with default content (empty string)
    token = Token(value=42, start_index=3, end_index=5)
    assert token._value == 42
    assert token._start_index == 3
    assert token._end_index == 5
    assert token._content == ""

    # Test constructor with various value types
    token = Token(value=[1, 2, 3], start_index=10, end_index=20, content="some content")
    assert token._value == [1, 2, 3]
    assert token._start_index == 10
    assert token._end_index == 20
    assert token._content == "some content"

# Generated at 2026-11-02 06:50:13.891613
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(value=None, start_index=0, end_index=4, content="hello")
    assert repr(token) == "Token('hello')"

    token = Token(value=None, start_index=2, end_index=4, content="hello world")
    assert repr(token) == "Token('llo')"

    token = ScalarToken(value=1, start_index=0, end_index=2, content="12345")
    assert repr(token) == "ScalarToken('123')"

# Generated at 2026-11-02 06:50:50.275529
# Unit test for constructor of class DictToken
def test_DictToken():
    # Constructor with positional arguments
    content = '{"key": "value"}'
    key_token = ScalarToken("key", 1, 5, content=content)
    value_token = ScalarToken("value", 8, 14, content=content)
    dict_value = {key_token: value_token}

    token = DictToken(dict_value, 0, 15, content)
    assert token._value == dict_value
    assert token._start_index == 0
    assert token._end_index == 15
    assert token._content == content
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}
    assert token.value == {"key": "value"}
    assert token.string == content

    # Constructor with keyword arguments
    token = DictToken(value=dict_value, start_index=2, end_index=15, content=content)
    assert token._value == dict_value
    assert token._start_index == 2
    assert token._end_index == 15
    assert token._content == content
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}

    # Constructor with multiple keys
    content = '{"a": 1, "b": 2}'
    key_a = ScalarToken("a", 1, 3, content=content)
    val_a = ScalarToken(1, 6, 6, content=content)
    key_b = ScalarToken("b", 9, 11, content=content)
    val_b = ScalarToken(2, 14, 14, content=content)

    token = DictToken({key_a: val_a, key_b: val_b}, 0, 15, content)
    assert token._child_keys == {"a": key_a, "b": key_b}
    assert token._child_tokens == {"a": val_a, "b": val_b}
    assert token.value == {"a": 1, "b": 2}

    # Constructor with an empty dictionary
    empty = DictToken({}, 0, 1, content="{}")
    assert empty._child_keys == {}
    assert empty._child_tokens == {}
    assert empty.value == {}
    assert empty._content == "{}"

# Generated at 2026-11-02 06:51:50.184118
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    content = '{"key": "value"}'

    key_token = ScalarToken("key", 1, 5, content=content)
    value_token = ScalarToken("value", 8, 14, content=content)

    # Construct with positional arguments
    token = DictToken({key_token: value_token}, 0, 15, content)

    # Constructor builds child key/token mappings from the raw value
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}

    # Value resolves nested token values
    assert token.value == {"key": "value"}

    # String, start and end positions derived from content
    assert token.string == content
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 16, 15)

    # Repr uses the class name and the token string
    assert repr(token) == "DictToken('" + content + "')"

    # Lookup of child tokens, key tokens, and empty index
    assert token.lookup(["key"]) == value_token
    assert token.lookup([]) == token
    assert token.lookup_key(["key"]) == key_token

    # Construct with keyword arguments
    token2 = DictToken(
        value={key_token: value_token}, start_index=0, end_index=15, content=content
    )
    assert token2 == token
    assert token2.value == {"key": "value"}
    assert token2.string == content

# Generated at 2026-11-02 06:53:01.764574
# Unit test for constructor of class DictToken
def test_DictToken():
    # Construct a DictToken from a mapping of key tokens to value tokens.
    key_token = ScalarToken("key", 0, 4, content='"key": "value"')
    value_token = ScalarToken("value", 6, 12, content='"key": "value"')
    token = DictToken({key_token: value_token}, 0, 13, content='"key": "value"')

    # Constructor should store the raw value, indices and content.
    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == 13
    assert token._content == '"key": "value"'

    # Constructor should build child key/token lookup tables.
    assert token._child_keys == {"key": key_token}
    assert token._child_tokens == {"key": value_token}

    # Derived properties.
    assert token.value == {"key": "value"}
    assert token.string == '"key": "value"'
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 14, 13)
    assert repr(token) == "DictToken('\"key\": \"value\"')"

    # Lookup within the constructed structure.
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

    # Equality against an identically constructed token.
    same = DictToken({key_token: value_token}, 0, 13, content='"key": "value"')
    assert token == same
    assert token != DictToken({}, 0, 13, content='"key": "value"')

    # Empty dictionary.
    empty = DictToken({}, 0, 1, content="{}")

# Generated at 2026-11-02 06:55:44.472634
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("a", 0, 0, content="a")

    # Equal tokens: same value, start index, and end index.
    assert token == ScalarToken("a", 0, 0, content="a")

    # Different value.
    assert token != ScalarToken("b", 0, 0, content="b")

    # Different start index.
    assert token != ScalarToken("a", 1, 1, content="ab")

    # Different end index.
    assert token != ScalarToken("a", 0, 1, content="ab")

    # Not a Token instance.
    assert token != "a"
    assert token != 123
    assert token != None

# Generated at 2026-11-02 06:57:08.566681
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Two tokens with same value, start_index, and end_index are equal
    assert ScalarToken("a", 1, 2) == ScalarToken("a", 1, 2)

    # Different value
    assert ScalarToken("a", 1, 2) != ScalarToken("b", 1, 2)

    # Different start_index
    assert ScalarToken("a", 1, 2) != ScalarToken("a", 0, 2)

    # Different end_index
    assert ScalarToken("a", 1, 2) != ScalarToken("a", 1, 3)

    # Comparison against non-Token objects
    assert ScalarToken("a", 1, 2) != "a"
    assert not (ScalarToken("a", 1, 2) == None)

    # Token is not equal to a different Token subclass with different value
    assert ScalarToken("a", 1, 2) != ListToken([ScalarToken("a", 1, 2)], 1, 2)

    # DictToken equality is based on derived (recursive) values and indices
    dict_value_1 = {ScalarToken("key", 0, 4): ScalarToken(1, 6, 6)}
    dict_value_2 = {ScalarToken("key", 0, 4): ScalarToken(1, 6, 6)}
    assert DictToken(dict_value_1, 0, 6) == DictToken(dict_value_2, 0, 6)
    assert DictToken(dict_value_1, 0, 6) != DictToken(dict_value_2, 0, 7)

    # Same indices but different derived values
    dict_value_3 = {ScalarToken("key", 0, 4): ScalarToken(2, 6, 6)}
    assert DictToken(dict_value_1, 0, 6) != DictToken(dict_value_3, 0, 6)

    # ListToken equality is based on derived (recursive) values and indices
    list_value_1 = [ScalarToken("a", 0, 0), ScalarToken("b", 2, 2)]
    list_value_2 = [ScalarToken("a", 0, 0), ScalarToken("b", 2, 2)]
    assert ListToken(list_value_1, 0, 2) == ListToken(list_value_2, 0, 2)
    assert ListToken(list_value_1, 0, 2) != ListToken(list_value_2, 0, 3)
    assert ListToken(list_value_1, 0, 2) != ListToken([ScalarToken("a", 0, 0)], 0, 2)

    # Equality against objects of unrelated types
    assert ListToken(list_value_1, 0, 2) != {"a": "b"}
    assert ListToken(list_value_1, 0, 2) != ["a", "b"]