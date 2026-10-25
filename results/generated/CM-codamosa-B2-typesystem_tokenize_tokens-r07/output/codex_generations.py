

# Generated at 2026-10-24 11:27:04.096119
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    from typesystem.base import Position

    # Content: {"name": "alice", "meta": {"age": 30}}
    # Index map: 0:'{', 1-6:'"name"', 8-14:'"alice"', 16-21:'"meta"', 23-34:'"age": 30' ...
    content = '{"name": "alice", "meta": {"age": 30}}'

    # Build key/value tokens with their source positions
    name_key = ScalarToken("name", 1, 6)
    alice = ScalarToken("alice", 9, 15)
    meta_key = ScalarToken("meta", 18, 23)
    age_key = ScalarToken("age", 31, 35)
    thirty = ScalarToken(30, 38, 39)
    inner_dict = DictToken({age_key: thirty}, 29, 40, content)
    outer_dict = DictToken({name_key: alice, meta_key: inner_dict}, 0, 41, content)

    # 1. Top-level key lookup: key token for "name"
    key_token = outer_dict.lookup_key(["name"])
    assert key_token is name_key
    assert key_token.value == "name"
    assert key_token.string == '"name"'
    assert key_token.start == Position(line_no=1, column_no=2, index=1)
    assert key_token.end == Position(line_no=1, column_no=7, index=6)

    # 2. Nested key lookup: key token for "age" inside the inner dict
    key_token = outer_dict.lookup_key(["meta", "age"])
    assert key_token is age_key
    assert key_token.value == "age"
    assert key_token.string == '"age"'
    assert key_token.start.index == 31

    # 3. Key whose value is a dict â lookup_key must not be confused
    #    with child-token lookup
    key_token = outer_dict.lookup_key(["meta"])
    assert key_token is meta_key
    assert key_token.value == "meta"

    # 4. Missing key raises KeyError
    try:
        outer_dict.lookup_key(["missing"])
        raise AssertionError("expected KeyError")
    except KeyError:
        pass

    print("test_Token_lookup_key passed")

# Generated at 2026-10-24 11:27:14.929074
# Unit test for constructor of class ListToken
def test_ListToken():
    content = "[1, 2]"
    first = ScalarToken(1, 1, 1, content)
    second = ScalarToken(2, 4, 4, content)

    token = ListToken([first, second], 0, 5, content)

    assert token._value == [first, second]
    assert token._start_index == 0
    assert token._end_index == 5
    assert token._content == content
    assert token.string == "[1, 2]"
    assert token.value == [1, 2]
    assert token.lookup([]) is token
    assert token.lookup([0]) is first
    assert token.lookup([1]) is second
    assert repr(token) == "ListToken('[1, 2]')"

    empty = ListToken([], 0, 1, "[]")
    assert empty.value == []
    assert empty.string == "[]"

# Generated at 2026-10-24 11:27:32.564043
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value + same start/end indices -> equal
    assert ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 0, 2, "abc")

    # Content is NOT part of equality
    assert ScalarToken(1, 0, 0, "1") == ScalarToken(1, 0, 0, "different content")

    # Same value, different start index -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 1, 3, "abc"))

    # Same value, different end index -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 0, 1, "abc"))

    # Different value, same indices -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abd", 0, 2, "abd"))

    # Non-Token operands -> not equal (isinstance guard)
    assert not (ScalarToken("abc", 0, 2, "abc") == "abc")
    assert not (ScalarToken("abc", 0, 2, "abc") == None)  # noqa: E711
    assert not (ScalarToken("abc", 0, 2, "abc") == 42)

    # __ne__ is derived from __eq__
    assert ScalarToken("abc", 0, 2, "abc") != ScalarToken("abc", 1, 3, "abc")

    # Subclasses compare structurally via _get_value()
    content = '{"k": 1}'
    dict_a = DictToken(
        {ScalarToken("k", 1, 3, content): ScalarToken(1, 5, 5, content)}, 0, 6, content
    )
    dict_b = DictToken(
        {ScalarToken("k", 1, 3, content): ScalarToken(1, 5, 5, content)}, 0, 6, content
    )
    assert dict_a == dict_b
    assert not (dict_a == DictToken({ScalarToken("k", 1, 3, content): ScalarToken(2, 5, 5, content)}, 0, 6, content))

    list_a = ListToken([ScalarToken(1, 1, 1, "[1]")], 0, 2, "[1]")
    list_b = ListToken([ScalarToken(1, 1, 1, "[1]")], 0, 2, "[1]")
    assert list_a == list_b

    # Different container shapes with different values -> not equal

# Generated at 2026-10-24 11:27:34.988469
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:37.409604
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:39.828290
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:42.249670
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:44.660554
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:47.080278
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:27:49.497122
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:27:51.915472
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:27:54.334359
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:27:56.754228
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:27:59.174730
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:28:01.589877
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:28:04.006423
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:28:06.435652
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:28:08.850845
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:28:10.487776
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    from typesystem.base import Position

    # Content: {"name": "alice", "meta": {"age": 30}}
    # Index map: 0:'{', 1-6:'"name"', 8-14:'"alice"', 16-21:'"meta"', 23-34:'"age": 30' ...
    content = '{"name": "alice", "meta": {"age": 30}}'

    # Build key/value tokens with their source positions
    name_key = ScalarToken("name", 1, 6)
    alice = ScalarToken("alice", 9, 15)
    meta_key = ScalarToken("meta", 18, 23)
    age_key = ScalarToken("age", 31, 35)
    thirty = ScalarToken(30, 38, 39)
    inner_dict = DictToken({age_key: thirty}, 29, 40, content)
    outer_dict = DictToken({name_key: alice, meta_key: inner_dict}, 0, 41, content)

    # 1. Top-level key lookup: key token for "name"
    key_token = outer_dict.lookup_key(["name"])
    assert key_token is name_key
    assert key_token.value == "name"
    assert key_token.string == '"name"'
    assert key_token.start == Position(line_no=1, column_no=2, index=1)
    assert key_token.end == Position(line_no=1, column_no=7, index=6)

    # 2. Nested key lookup: key token for "age" inside the inner dict
    key_token = outer_dict.lookup_key(["meta", "age"])
    assert key_token is age_key
    assert key_token.value == "age"
    assert key_token.string == '"age"'
    assert key_token.start.index == 31

    # 3. Key whose value is a dict â lookup_key must not be confused
    #    with child-token lookup
    key_token = outer_dict.lookup_key(["meta"])
    assert key_token is meta_key
    assert key_token.value == "meta"

    # 4. Missing key raises KeyError
    try:
        outer_dict.lookup_key(["missing"])
        raise AssertionError("expected KeyError")
    except KeyError:
        pass

    print("test_Token_lookup_key passed")

# Generated at 2026-10-24 11:28:27.144019
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:28:52.535941
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"outer": {"name": "Alice"}}'

    outer_key = ScalarToken("outer", 1, 7, content)
    name_key = ScalarToken("name", 11, 16, content)
    name_value = ScalarToken("Alice", 19, 25, content)

    inner = DictToken({name_key: name_value}, 10, 26, content)
    root = DictToken({outer_key: inner}, 0, 27, content)

    assert root.lookup_key(["outer"]) is outer_key
    assert root.lookup_key(["outer", "name"]) is name_key
    assert root.lookup_key(["outer", "name"]).string == '"name"'

# Generated at 2026-10-24 11:28:54.956089
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:28:57.588412
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:00.005539
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:02.424448
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:29:04.845690
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:29:07.394753
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:29:09.811174
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 11:29:17.802678
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():content = '{"a": 1, "b": [2, 3]}'

# Generated at 2026-10-24 11:29:19.980895
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:21.413643
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:22.727315
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:24.093677
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:25.434833
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:26.745327
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:28.064484
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:29.410984
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:30.754682
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:32.076111
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:33.388882
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:34.719448
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:36.159162
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:37.488079
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:38.801357
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:40.121193
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:41.442781
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:42.758428
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:45.268161
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:47.790257
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:50.297852
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:52.712646
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:55.270313
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:57.684265
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:00.101080
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:02.519671
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:04.936283
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:07.861201
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:10.423178
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:12.839340
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:15.257088
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:17.673292
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:20.090874
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:22.512166
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:24.927567
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:27.350825
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:29.771167
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:32.190650
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:34.608953
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:37.025332
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:39.441865
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:41.859796
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:44.275525
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:46.693984
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:49.110142
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:51.526894
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:53.943468
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:56.361826
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:58.776498
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:01.192750
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:03.610980
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:06.027993
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:08.445506
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:10.862708
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:13.282038
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:20.298430
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": 1}'

# Generated at 2026-10-24 11:31:21.634776
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:23.064723
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:24.381704
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:25.698434
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:27.010379
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:28.325418
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:29.635657
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:30.953246
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:32.382994
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:33.693908
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:36.752581
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:38.427636
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:39.806814
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:41.190654
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:42.527857
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:43.853162
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:45.189774
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:46.514491
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:49.030238
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:51.447333
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:53.868205
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:56.281477
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:58.699256
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:01.119144
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:05.823553
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:08.244327
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:10.968756
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:13.382793
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:15.800733
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:18.219454
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:20.633632
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:23.049976
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:25.468352
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:27.885639
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:30.301297
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:32.717252
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:35.134520
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:37.550604
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:39.967034
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:42.382314
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:44.801959
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:47.217191
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:49.633774
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:52.053379
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:12.761288
# Unit test for constructor of class DictToken
def test_DictToken():import typesystem.tokenize.tokens as _  # noqa: F401  (module context kept minimal)


# Generated at 2026-10-24 11:33:14.089414
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:15.412018
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:16.729086
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:19.106580
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:20.434433
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:21.783574
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:23.111283
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:24.419673
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:25.735633
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:27.184809
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:28.495943
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:29.939916
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:32.361367
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:34.780203
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:37.230886
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:43.494401
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:46.109369
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:48.527238
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:50.945533
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:53.364791
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:55.780325
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:57.163623
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:58.565981
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:59.892285
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:01.209177
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:02.543054
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:03.859182
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:05.167904
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:06.488185
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:33.269159
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:35.688114
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:38.103682
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:40.519859
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:42.939155
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:45.356118
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:47.908733
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:50.327489
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:52.743431
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:55.162701
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:57.581931
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:59.999651
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:02.414763
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:04.833369
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:07.248579
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:08.677957
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:09.989222
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:11.344629
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:12.860977
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:14.284784
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:32.865465
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:35.377524
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:37.794254
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:40.211291
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:42.637774
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:45.059425
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:47.480092
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:49.894664
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:52.311849
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:54.729332
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:57.147438
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:59.564078
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:01.983217
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:04.401318
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:06.818091
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:09.236910
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:11.651843
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:14.069827
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:16.487151
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:18.905752
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:21.321352
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:23.739326
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:26.155672
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:28.572700
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:30.990796
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:33.408210
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:35.824463
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:38.243352
# Unit test for constructor of class DictToken