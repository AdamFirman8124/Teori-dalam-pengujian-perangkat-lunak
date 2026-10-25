

# Generated at 2026-10-24 07:33:50.152233
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:33:52.778420
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:33:55.193188
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:33:57.605628
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:34:00.019694
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:02.434926
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:04.848195
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:07.260778
# Unit test for method lookup of class Token

# Generated at 2026-10-24 07:34:30.987098
# Unit test for method lookup of class Token
def test_Token_lookup():content = '{"a": [10, 20]}'

# Generated at 2026-10-24 07:34:33.408501
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:34:35.922901
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:34:38.340879
# Unit test for constructor of class Token

# Generated at 2026-10-24 07:34:40.754906
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:34:43.329293
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:34:45.745556
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:34:48.160846
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:50.574328
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:52.987983
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:34:55.401924
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:34:57.815214
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:00.232183
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:02.646785
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:05.391024
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:07.807671
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:10.226918
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:35:12.644739
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:35:15.056231
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:35:17.472853
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:35:19.886828
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:35:33.013093
# Unit test for method __eq__ of class Token
def test_Token___eq__():a = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-24 07:35:49.482155
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:35:51.898809
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:54.414934
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:56.949515
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:35:59.363129
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:01.776931
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:04.193686
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:06.609114
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:09.022937
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:11.437389
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:13.851877
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:36:16.266678
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:36:18.680776
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:36:21.094152
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:23.507645
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:36:25.921339
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:37:39.121631
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [1, 2]}'

    # Build tokens by hand so no parser import is needed.
    # Keys as ScalarTokens, values as ScalarToken / ListToken.
    key_a = ScalarToken("a", 1, 2, content)
    val_1 = ScalarToken(1, 5, 5, content)
    dict_token = DictToken({key_a: val_1}, 0, 5, content)

    key_a2 = ScalarToken("a", 1, 2, content)
    val_1b = ScalarToken(1, 5, 5, content)
    dict_token_2 = DictToken({key_a2: val_1b}, 0, 5, content)

    key_b = ScalarToken("b", 1, 2, content)
    dict_token_3 = DictToken({key_b: val_1}, 0, 5, content)

    scalar = ScalarToken(1, 5, 5, content)
    scalar_same = ScalarToken(1, 5, 5, content)
    scalar_diff_value = ScalarToken(2, 5, 5, content)
    scalar_diff_index = ScalarToken(1, 6, 6, content)

    # Equal value and identical indices -> equal
    assert scalar == scalar_same
    assert dict_token == dict_token_2

    # Different value -> not equal
    assert scalar != scalar_diff_value

    # Different start/end index -> not equal
    assert scalar != scalar_diff_index

    # DictToken compares by resolved value, not by key token identity
    assert dict_token != dict_token_3

    # Different value AND different indices -> not equal
    assert scalar != dict_token

    # Comparison with a non-Token object -> not equal, no exception
    assert scalar != 1
    assert scalar != "1"
    assert scalar is not None and (scalar == None) is False

    # __eq__ must not raise for dict-with-token vs plain comparisons
    assert dict_token != {"a": 1}

    # Hash consistency for ScalarToken: equal tokens have equal hashes
    assert hash(scalar) == hash(scalar_same)

# Generated at 2026-10-24 07:37:41.854604
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:37:43.228577
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:37:45.908115
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:37:48.547408
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:37:51.695580
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:37:54.218191
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:37:56.717726
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:37:59.219654
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:01.635011
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:04.048677
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:06.464378
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:08.878800
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:11.315889
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:13.718962
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:16.137698
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:18.554458
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:20.977379
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:23.389012
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:25.804647
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:28.221909
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:30.632985
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:33.047412
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:35.461640
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:38:37.877561
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:40.295479
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:38:41.707509
# Unit test for method __eq__ of class Token
def test_Token___eq__():a = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-24 07:38:44.482821
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:38:47.177955
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:39:03.654298
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:39:06.436431
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:39:22.932210
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:39:26.275988
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:28.690107
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:31.104669
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:33.522004
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:39:36.088966
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:39:38.601834
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:39:41.013337
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:43.426973
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:45.847950
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:48.258901
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:50.673366
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:53.087088
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:55.506007
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:39:57.921319
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:40:00.339411
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 07:40:02.749633
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:40:05.164443
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:40:07.583258
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:40:24.270638
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:40:58.268383
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Token is abstract (_get_value raises), so test via ScalarToken.
    base = ScalarToken("hello", 0, 4, content="hello world")

    # Equal: same value, start_index and end_index.
    same = ScalarToken("hello", 0, 4, content="hello world")
    assert base == same
    assert same == base
    assert not (base != same)

    # Content is ignored by __eq__.
    other_content = ScalarToken("hello", 0, 4, content="different")
    assert base == other_content

    # Different value -> not equal.
    diff_value = ScalarToken("bye", 0, 4, content="hello world")
    assert base != diff_value
    assert not (base == diff_value)

    # Different start_index -> not equal.
    diff_start = ScalarToken("hello", 1, 4, content="hello world")
    assert base != diff_start
    assert not (base == diff_start)

    # Different end_index -> not equal.
    diff_end = ScalarToken("hello", 0, 5, content="hello world")
    assert base != diff_end
    assert not (base == diff_end)

    # Non-Token other -> not equal.
    assert not (base == "hello")
    assert base != "hello"
    assert not (base == None)
    assert base != None
    assert not (base == 123)
    assert base != 123

# Generated at 2026-10-24 07:41:00.983481
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:41:17.416369
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:41:44.448707
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "abcde")

    # Equality depends on value and start/end indexes, not content.
    assert token == ScalarToken("value", 1, 3, "xxxxx")

    assert token != ScalarToken("different", 1, 3, "abcde")
    assert token != ScalarToken("value", 0, 3, "abcde")
    assert token != ScalarToken("value", 1, 4, "abcde")
    assert token != object()

# Generated at 2026-10-24 07:41:47.316086
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:41:50.502894
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:42:15.086985
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "01234")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Different value or position makes tokens unequal.
    assert token != ScalarToken("other", 1, 3, "01234")
    assert token != ScalarToken("value", 0, 3, "01234")
    assert token != ScalarToken("value", 1, 4, "01234")

    # A Token cannot equal an unrelated object.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 07:42:31.655835
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Token is abstract (_get_value raises), so test via ScalarToken.
    base = ScalarToken("hello", 0, 4, content="hello world")

    # Equal: same value, start_index and end_index.
    same = ScalarToken("hello", 0, 4, content="hello world")
    assert base == same
    assert same == base
    assert not (base != same)

    # Content is ignored by __eq__.
    other_content = ScalarToken("hello", 0, 4, content="different")
    assert base == other_content

    # Different value -> not equal.
    diff_value = ScalarToken("bye", 0, 4, content="hello world")
    assert base != diff_value
    assert not (base == diff_value)

    # Different start_index -> not equal.
    diff_start = ScalarToken("hello", 1, 4, content="hello world")
    assert base != diff_start
    assert not (base == diff_start)

    # Different end_index -> not equal.
    diff_end = ScalarToken("hello", 0, 5, content="hello world")
    assert base != diff_end
    assert not (base == diff_end)

    # Non-Token other -> not equal.
    assert not (base == "hello")
    assert base != "hello"
    assert not (base == None)
    assert base != None
    assert not (base == 123)
    assert base != 123

# Generated at 2026-10-24 07:42:48.146818
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:42:52.036932
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:42:54.740143
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:42:57.428044
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    # Build child key/value tokens.
    key1 = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1 = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2 = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1 = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2 = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token = ListToken([item1, item2], 26, 30, '{"name": "Alice", "scores": [1, 2]}')

    # Construct DictToken: value is a dict mapping key Tokens to value Tokens.
    token = DictToken(
        {key1: value1, key2: list_token},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )

    # Constructor stores raw inputs.
    assert token._start_index == 0
    assert token._end_index == 31
    assert token._content == '{"name": "Alice", "scores": [1, 2]}'
    assert set(token._child_keys.keys()) == {"name", "scores"}
    assert set(token._child_tokens.keys()) == {"name", "scores"}

    # Key tokens are the original Token instances.
    assert token._child_keys["name"] is key1
    assert token._child_keys["scores"] is key2
    assert token._child_tokens["name"] is value1
    assert token._child_tokens["scores"] is list_token

    # _get_value resolves recursively to plain Python types.
    assert token.value == {"name": "Alice", "scores": [1, 2]}

    # string property slices content by indices.
    assert token.string == '{"name": "Alice", "scores": [1, 2]}'

    # Child token lookup via index path.
    assert token.lookup(["name"]).value == "Alice"
    assert token.lookup(["scores", 0]).value == 1
    assert token.lookup(["scores", 1]).value == 2

    # Key token lookup via lookup_key.
    assert token.lookup_key(["name"]) is key1
    assert token.lookup_key(["scores"]) is key2

    # Positions computed from content.
    assert token.start == Position(1, 1, 0)
    assert token.lookup(["name"]).start == Position(1, 2, 1)

    # Equality against an identically constructed DictToken.
    key1b = ScalarToken("name", 0, 5, '{"name": "Alice", "scores": [1, 2]}')
    value1b = ScalarToken("Alice", 8, 14, '{"name": "Alice", "scores": [1, 2]}')
    key2b = ScalarToken("scores", 17, 24, '{"name": "Alice", "scores": [1, 2]}')
    item1b = ScalarToken(1, 27, 27, '{"name": "Alice", "scores": [1, 2]}')
    item2b = ScalarToken(2, 29, 29, '{"name": "Alice", "scores": [1, 2]}')
    list_token_b = ListToken([item1b, item2b], 26, 30, '{"name": "Alice", "scores": [1, 2]}')
    token_b = DictToken(
        {key1b: value1b, key2b: list_token_b},
        0,
        31,
        '{"name": "Alice", "scores": [1, 2]}',
    )
    assert token == token_b

    # Inequality against a different token.
    assert token != list_token

    # repr contains class name and string.
    assert repr(token) == "DictToken('{\"name\": \"Alice\", \"scores\": [1, 2]}')"

    # Empty dict constructor.
    empty = DictToken({}, 0, 1, "{}")
    assert empty.value == {}
    assert empty._child_keys == {}
    assert empty._child_tokens == {}

# Generated at 2026-10-24 07:43:13.949071
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:43:37.397041
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"a": 1, "b": [true, null]}'

    # Equal tokens: same value, same start/end indices.
    token = ScalarToken("a", 1, 2, content)
    assert token == ScalarToken("a", 1, 2, content)

    # A token is equal to itself.
    assert token == token

    # Not equal: different values.
    assert token != ScalarToken("b", 1, 2, content)

    # Not equal: different start index.
    assert token != ScalarToken("a", 0, 2, content)

    # Not equal: different end index.
    assert token != ScalarToken("a", 1, 3, content)

    # Not equal: different types (compare against plain object).
    assert token != "a"
    assert token != None

    # Not equal: different Token subclasses with same underlying value.
    dict_token = DictToken({}, 0, 1, content)
    list_token = ListToken([], 0, 1, content)
    assert dict_token != list_token

    # DictToken equality is based on the resolved value, not dict identity.
    dict_token_a = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    dict_token_b = DictToken(
        {ScalarToken("x", 0, 1, content): ScalarToken(1, 5, 6, content)}, 0, 6, content
    )
    assert dict_token_a == dict_token_b

    # DictToken vs ScalarToken: different resolved values.
    assert dict_token_a != ScalarToken("x", 0, 6, content)

    # ListToken equality is based on the resolved value.
    list_a = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_b = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(2, 3, 4, content)], 0, 4, content
    )
    list_c = ListToken(
        [ScalarToken(1, 0, 1, content), ScalarToken(3, 3, 4, content)], 0, 4, content
    )
    assert list_a == list_b
    assert list_a != list_c

    # Empty content is fine â equality only uses value and indices.
    assert ScalarToken(None, 0, 0) == ScalarToken(None, 0, 0)

# Generated at 2026-10-24 07:43:39.917956
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:43:42.342848
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 07:43:44.760763
# Unit test for constructor of class DictToken