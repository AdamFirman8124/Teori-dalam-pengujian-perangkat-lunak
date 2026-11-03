

# Generated at 2026-11-03 05:32:30.925555
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"a": {"b": 1}}'

    # Build the token tree for {"a": {"b": 1}}
    key_a = ScalarToken("a", 1, 3, content)
    key_b = ScalarToken("b", 7, 9, content)
    value_1 = ScalarToken(1, 12, 12, content)
    inner_dict = DictToken({key_b: value_1}, 6, 13, content)
    root = DictToken({key_a: inner_dict}, 0, 13, content)

    # Top-level key lookup returns the key token itself
    assert root.lookup_key(["a"]) is key_a

    # Nested key lookup: resolves the child token first, then its key token
    assert root.lookup_key(["a", "b"]) is key_b

    # The returned key tokens expose the correct source string
    assert root.lookup_key(["a"]).string == '"a"'
    assert root.lookup_key(["a", "b"]).string == '"b"'

    # Positions of the returned key tokens
    assert root.lookup_key(["a"]).start == Position(1, 2, 1)
    assert root.lookup_key(["a", "b"]).start == Position(1, 8, 7)

# Generated at 2026-11-03 05:34:05.649191
# Unit test for constructor of class ListToken
def test_ListToken():
    scalar_1 = ScalarToken(1, 1, 1, content='[1, "a"]')
    scalar_2 = ScalarToken("a", 4, 6, content='[1, "a"]')
    token = ListToken([scalar_1, scalar_2], 0, 7, content='[1, "a"]')

    # Constructor stores attributes correctly
    assert token._value == [scalar_1, scalar_2]
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == '[1, "a"]'

    # Properties derived from constructor arguments
    assert token.string == '[1, "a"]'
    assert token.value == [1, "a"]
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=8, index=7)

    # Child token lookup built on stored value
    assert token._get_child_token(0) == scalar_1
    assert token.lookup([1]) == scalar_2

    # Default content argument
    empty_token = ListToken([], 0, 0)
    assert empty_token._content == ""
    assert empty_token.string == ""
    assert empty_token.value == []

    # Equality based on value and indices
    assert token == ListToken([scalar_1, scalar_2], 0, 7, content='[1, "a"]')
    assert token != scalar_1

    # repr
    assert repr(token) == "ListToken('[1, \"a\"]')"

# Generated at 2026-11-03 05:36:03.435536
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Equal tokens: same value, start index, and end index
    token_a = ScalarToken(value=1, start_index=0, end_index=2)
    token_b = ScalarToken(value=1, start_index=0, end_index=2)
    assert token_a == token_b
    assert token_b == token_a

    # Different values -> not equal
    token_c = ScalarToken(value=2, start_index=0, end_index=2)
    assert token_a != token_c
    assert token_c != token_a

    # Different start_index -> not equal
    token_d = ScalarToken(value=1, start_index=1, end_index=2)
    assert token_a != token_d
    assert token_d != token_a

    # Different end_index -> not equal
    token_e = ScalarToken(value=1, start_index=0, end_index=3)
    assert token_a != token_e
    assert token_e != token_a

    # Comparison against non-Token objects -> not equal
    assert token_a != 1
    assert token_a != "1"
    assert token_a != None  # noqa: E711
    assert token_a != [1]
    assert token_a != {"value": 1}

    # Content string does not affect equality
    token_f = ScalarToken(value=1, start_index=0, end_index=2, content="abc")
    token_g = ScalarToken(value=1, start_index=0, end_index=2, content="xyz")
    assert token_f == token_g

    # DictToken equality: equal when child tokens compare equal
    key_a = ScalarToken(value="a", start_index=0, end_index=2)
    val_a = ScalarToken(value=1, start_index=4, end_index=4)
    dict_a = DictToken(value={key_a: val_a}, start_index=0, end_index=6)
    key_b = ScalarToken(value="a", start_index=0, end_index=2)
    val_b = ScalarToken(value=1, start_index=4, end_index=4)
    dict_b = DictToken(value={key_b: val_b}, start_index=0, end_index=6)
    assert dict_a == dict_b
    assert dict_b == dict_a

    # DictToken inequality when values differ
    val_c = ScalarToken(value=2, start_index=4, end_index=4)
    dict_c = DictToken(value={key_a: val_c}, start_index=0, end_index=6)
    assert dict_a != dict_c

    # ListToken equality
    item_a = ScalarToken(value=1, start_index=0, end_index=0)
    item_b = ScalarToken(value=2, start_index=2, end_index=2)
    list_a = ListToken(value=[item_a, item_b], start_index=0, end_index=4)
    item_c = ScalarToken(value=1, start_index=0, end_index=0)
    item_d = ScalarToken(value=2, start_index=2, end_index=2)
    list_b = ListToken(value=[item_c, item_d], start_index=0, end_index=4)
    assert list_a == list_b
    assert list_b == list_a

    # ListToken inequality when element values differ
    item_e = ScalarToken(value=3, start_index=2, end_index=2)
    list_c = ListToken(value=[item_c, item_e], start_index=0, end_index=4)
    assert list_a != list_c

    # Token vs DictToken with same indices but different value types
    assert token_a != dict_a

# Generated at 2026-11-03 05:39:12.065048
# Unit test for constructor of class ListToken
def test_ListToken():
    value = [ScalarToken(1, 0, 0), ScalarToken(2, 3, 3)]
    token = ListToken(value, 0, 6, "[1, 2]")

    # Constructor stores the raw attributes
    assert token._value == value
    assert token._start_index == 0
    assert token._end_index == 6
    assert token._content == "[1, 2]"

    # Derived properties work correctly
    assert token.value == [1, 2]
    assert token.string == "[1, 2]"
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 7, 6)
    assert repr(token) == "ListToken('[1, 2]')"

    # Child token lookup through the constructed token
    assert token.lookup([0]).value == 1
    assert token.lookup([1]).value == 2

    # Equality against an identically constructed token
    other = ListToken([ScalarToken(1, 0, 0), ScalarToken(2, 3, 3)], 0, 6, "[1, 2]")
    assert token == other