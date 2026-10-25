

# Generated at 2026-10-24 15:57:54.133839
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 15:57:55.566648
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():content = '{"outer": {"inner": 42}}'

# Generated at 2026-10-24 15:58:20.283815
# Unit test for constructor of class ListToken
def test_ListToken():
    content = "[1, 2]"
    tok1 = ScalarToken(1, 1, 1, content)
    tok2 = ScalarToken(2, 4, 4, content)

    # Constructor with explicit content

# Generated at 2026-10-24 15:58:40.400534
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:58:43.487500
# Unit test for constructor of class ListToken
def test_ListToken():
    content = "[1, 2]"
    tok1 = ScalarToken(1, 1, 1, content)
    tok2 = ScalarToken(2, 4, 4, content)

    # Constructor with explicit content

# Generated at 2026-10-24 15:58:54.179033
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    # hash() delegates to the underlying value
    token = ScalarToken("hello", 0, 4, content="hello")
    assert hash(token) == hash("hello")
    assert isinstance(hash(token), int)

    token_int = ScalarToken(123, 0, 2, content="123")
    assert hash(token_int) == hash(123)

    token_none = ScalarToken(None, 0, 3, content="null")
    assert hash(token_none) == hash(None)

    # same value and same span: equal and same hash
    token_a = ScalarToken(42, 0, 1, content="42")
    token_b = ScalarToken(42, 0, 1, content="42")
    assert token_a == token_b
    assert hash(token_a) == hash(token_b)
    assert {token_a: "x"}[token_b] == "x"

    # same value but different span: same hash (hash only uses _value),
    # but not equal (eq uses span)
    token_c = ScalarToken(42, 5, 6, content="xxxxx42")
    assert hash(token_a) == hash(token_c)
    assert token_a != token_c

    # different values: different hashes
    assert hash(ScalarToken("a", 0, 0, content="a")) != hash(
        ScalarToken("b", 0, 0, content="b")
    )

# Generated at 2026-10-24 15:58:55.514376
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:58:56.894188
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:58:58.292250
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:58:59.699672
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:59:23.825200
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:59:25.361622
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:59:35.603238
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name":"Alice","age":30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 8, 14, content)
    age_key = ScalarToken("age", 16, 20, content)
    age_value = ScalarToken(30, 22, 23, content)

    token_values = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(token_values, 0, 24, content)

    assert token._value is token_values
    assert token._start_index == 0
    assert token._end_index == 24
    assert token._content == content

    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }
    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }

    assert token.value == {
        "name": "Alice",
        "age": 30,
    }

# Generated at 2026-10-24 15:59:45.844975
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    children = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(children, 0, len(content) - 1, content)

    assert token._value == children
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }
    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }

    assert token.value == {"name": "Alice", "age": 30}
    assert token.string == content
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key

# Generated at 2026-10-24 15:59:47.252826
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:59:56.119082
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=16,
        content=content,
    )

    assert token.string == content
    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 17, 16)

# Generated at 2026-10-24 16:00:04.394513
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    assert token == ScalarToken("value", 0, 4, "value")

    # Content is not part of equality.
    assert token == ScalarToken("value", 0, 4, "other")

    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 16:00:28.761217
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 2, 5, content)
    value_token = ScalarToken("Alice", 10, 14, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=len(content) - 1,
        content=content,
    )

    assert token._value == {key_token: value_token}
    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 16:00:45.355208
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 16:01:01.852636
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 16:01:52.113023
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 16:02:27.952298
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 16:03:22.245539
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 16:03:29.965820
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:03:31.323253
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:03:33.832127
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:03:36.249591
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:03:38.917697
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:03:41.334036
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:03:43.837680
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:03:46.250525
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:03:48.664780
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:03:51.077420
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:03:53.494777
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:10.251566
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:04:26.581911
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:04:27.922195
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:04:30.450526
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:32.957805
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:35.367806
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:37.781799
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:40.195545
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:42.614450
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:45.026722
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:47.479040
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:49.890813
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:04:52.302678
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:54.715697
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:57.127011
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:04:59.538934
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:01.951400
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:04.365868
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:15.479732
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Two tokens with identical value and identical start/end indices are equal.
    token1 = ScalarToken("a", start_index=0, end_index=2, content="abc")
    token2 = ScalarToken("a", start_index=0, end_index=2, content="abc")
    assert token1 == token2
    assert not token1 != token2

    # Different values are not equal.
    token3 = ScalarToken("b", start_index=0, end_index=2, content="abc")
    assert token1 != token3
    assert not token1 == token3

    # Same value but different start index is not equal.
    token4 = ScalarToken("a", start_index=1, end_index=2, content="abc")
    assert token1 != token4

    # Same value but different end index is not equal.
    token5 = ScalarToken("a", start_index=0, end_index=1, content="abc")
    assert token1 != token5

    # Comparison with a non-Token object is not equal.
    assert token1 != "a"
    assert token1 != None  # noqa: E711
    assert not token1 == "a"

    # Comparison with a different Token subclass but equal value/indices is equal,
    # since __eq__ only compares value and indices.
    token6 = Token("a", start_index=0, end_index=2, content="abc")
    token7 = ScalarToken("a", start_index=0, end_index=2, content="abc")
    assert token6 == token7

    # Equality is reflexive.
    assert token1 == token1

# Generated at 2026-10-24 16:05:16.803924
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:05:18.246054
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:05:19.679160
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:05:21.111855
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 16:05:37.527418
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:05:40.139646
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:05:42.551700
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:05:44.965171
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:05:47.499136
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:49.912359
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:52.325728
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:05:54.738904
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:05:57.151367
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:05:59.565204
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:01.977363
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:04.390464
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:06.806496
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:13.586388
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:15.999301
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:18.417733
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:20.835401
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:23.243813
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:25.657075
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:28.069570
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:30.487049
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:32.895624
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:35.308581
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:37.721038
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:40.133417
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:42.546470
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:44.959732
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:47.383257
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:06:49.795745
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:52.212662
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:54.629737
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 16:06:57.042340
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 16:07:03.646204
# Unit test for method __eq__ of class Token
def test_Token___eq__():token1 = Token("abc", 0, 2, content="abcdef")

# Generated at 2026-10-24 16:07:04.979743
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:07:06.361405
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 16:07:07.765713
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:13.424164
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:14.746471
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:16.087493
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same

# Generated at 2026-10-24 16:07:17.417276
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:18.737056
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:35.360207
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value, same indices -> equal
    token = ScalarToken(value="a", start_index=0, end_index=0, content="abc")
    assert token == ScalarToken(value="a", start_index=0, end_index=0, content="abc")

    # Same value, different start_index -> not equal
    assert token != ScalarToken(value="a", start_index=1, end_index=0, content="abc")

    # Same value, different end_index -> not equal
    assert token != ScalarToken(value="a", start_index=0, end_index=1, content="abc")

    # Same indices, different value -> not equal
    assert token != ScalarToken(value="b", start_index=0, end_index=0, content="abc")

    # Comparing against a non-Token -> not equal
    assert token != "a"
    assert not token == None  # noqa: E711

    # Equality is based on _get_value(), so a DictToken equals another
    # DictToken with an equivalent structure (not necessarily identical
    # key/value token instances).
    dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    other_dict_token = DictToken(
        value={ScalarToken("key", 0, 2): ScalarToken("value", 5, 9)},
        start_index=0,
        end_index=11,
        content='{"key": "value"}',
    )
    assert dict_token == other_dict_token

    # Two ScalarTokens wrapping equivalent values but at different
    # positions are still not equal (position is part of equality).
    assert ScalarToken("a", 0, 0) != ScalarToken("a", 1, 1)

    # Reflexivity
    assert token == token

# Generated at 2026-10-24 16:07:51.847303
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 16:08:08.332979
# Unit test for constructor of class DictToken
def test_DictToken():
    # Build child tokens (keys and values) first
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "age": 30}')
    value1 = ScalarToken("Alice", 9, 15, '{"name": "Alice", "age": 30}')
    key2 = ScalarToken("age", 19, 23, '{"name": "Alice", "age": 30}')
    value2 = ScalarToken(30, 26, 27, '{"name": "Alice", "age": 30}')

    token = DictToken(
        {key1: value1, key2: value2},
        start_index=0,
        end_index=28,
        content='{"name": "Alice", "age": 30}',
    )

    # Constructor stores the raw value unchanged
    assert token._value == {key1: value1, key2: value2}
    assert token._start_index == 0
    assert token._end_index == 28
    assert token._content == '{"name": "Alice", "age": 30}'

    # Constructor builds child key lookup: raw key value -> key Token
    assert token._child_keys == {"name": key1, "age": key2}

    # Constructor builds child token lookup: raw key value -> value Token
    assert token._child_tokens == {"name": value1, "age": value2}

    # Recursively resolved plain-Python value
    assert token.value == {"name": "Alice", "age": 30}

    # lookup() uses the child token map built in the constructor
    assert token.lookup(["name"]) is value1
    assert token.lookup(["age"]) is value2

    # lookup_key() uses the child key map built in the constructor
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["age"]) is key2

    # string property slices content by indices
    assert token.string == '{"name": "Alice", "age": 30}'

    # Positions derived from content + indices
    assert token.start == Position(line_no=1, column_no=1, index=0)
    assert token.end == Position(line_no=1, column_no=29, index=28)

    # __eq__ compares resolved value plus start/end indices
    key_dup = ScalarToken("name", 0, 5, token._content)
    value_dup = ScalarToken("Alice", 9, 15, token._content)
    same = DictToken({key_dup: value_dup}, 0, 28, token._content)
    assert token == same