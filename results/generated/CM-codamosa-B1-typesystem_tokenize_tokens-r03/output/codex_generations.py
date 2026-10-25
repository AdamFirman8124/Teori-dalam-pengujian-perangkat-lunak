

# Generated at 2026-10-24 19:39:43.996506
# Unit test for constructor of class Token

# Generated at 2026-10-24 19:39:46.415114
# Unit test for constructor of class Token

# Generated at 2026-10-24 19:39:48.961419
# Unit test for constructor of class Token

# Generated at 2026-10-24 19:39:51.379811
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 19:39:53.796916
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 19:39:56.215293
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 19:39:58.782051
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 19:40:01.204052
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 19:40:03.622559
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 19:40:06.040766
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 19:40:08.457789
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 19:40:36.171045
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():content = '{"outer": {"inner": 42}}'

# Generated at 2026-10-24 19:40:42.200094
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    value = "example"
    token = ScalarToken(value, start_index=0, end_index=6, content=value)

    assert hash(token) == hash(value)

# Generated at 2026-10-24 19:40:52.453032
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name":"Alice","age":30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 8, 14, content)
    age_key = ScalarToken("age", 16, 20, content)
    age_value = ScalarToken(30, 22, 23, content)

    children = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(children, 0, 24, content)

    assert token._value is children
    assert token._start_index == 0
    assert token._end_index == 24
    assert token._content == content

    assert token._child_keys["name"] is name_key
    assert token._child_keys["age"] is age_key
    assert token._child_tokens["name"] is name_value
    assert token._child_tokens["age"] is age_value

    assert token.value == {"name": "Alice", "age": 30}
    assert token.string == content
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key

# Generated at 2026-10-24 19:40:54.967013
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:40:57.383599
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:40:59.801007
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:41:02.218454
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:41:04.635404
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:41:07.050454
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:41:09.468345
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:11.886383
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:14.301732
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:16.719911
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:19.136046
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:21.551683
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:41:22.926343
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

# Generated at 2026-10-24 19:41:32.906227
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=len(content) - 1,
        content=content,
    )

    assert token.value == {"name": "Alice"}
    assert token.string == content

    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

    assert token._child_tokens == {"name": value_token}
    assert token._child_keys == {"name": key_token}

# Generated at 2026-10-24 19:41:42.683460
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    children = {key_token: value_token}

    token = DictToken(children, 0, len(content) - 1, content)

    assert token._value is children
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:41:44.004204
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

# Generated at 2026-10-24 19:41:45.329765
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

# Generated at 2026-10-24 19:41:56.647816
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

    assert token._value is children
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

# Generated at 2026-10-24 19:41:59.166882
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:42:01.586593
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:42:04.003080
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:42:06.418507
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:08.834541
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:11.251440
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:13.666834
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:16.082667
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:18.498920
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:20.915455
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:23.336473
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:25.755335
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:28.172627
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:30.589719
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:33.008246
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:42:34.367378
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

# Generated at 2026-10-24 19:42:45.339943
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

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:42:54.616623
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    token_mapping = {key_token: value_token}

    token = DictToken(token_mapping, 0, 16, content)

    # Verify inherited constructor state.
    assert token._value is token_mapping
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    # Verify DictToken's lookup mappings.
    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    # Verify observable behavior.
    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:42:55.935518
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

# Generated at 2026-10-24 19:43:04.472577
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)

    token = DictToken(
        value={key_token: value_token},
        start_index=0,
        end_index=16,
        content=content,
    )

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token
    assert token.string == content

# Generated at 2026-10-24 19:43:06.893664
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:09.309904
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:11.940234
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:14.356979
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:43:16.772669
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:43:19.192767
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:43:21.609909
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:24.027329
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:26.446379
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:28.864009
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:31.282612
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:33.700258
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:36.117842
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:43:45.205517
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": 1}'

# Generated at 2026-10-24 19:43:46.532019
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

# Generated at 2026-10-24 19:43:47.856160
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

# Generated at 2026-10-24 19:43:55.960574
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)

    token = DictToken(
        value={key_token: value_token},
        start_index=0,
        end_index=16,
        content=content,
    )

    assert token._value == {key_token: value_token}
    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:43:57.274095
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

# Generated at 2026-10-24 19:44:00.051057
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

# Generated at 2026-10-24 19:44:01.484467
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

# Generated at 2026-10-24 19:44:15.307981
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    raw_value = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(raw_value, 0, 27, content)

    assert token._value is raw_value
    assert token._start_index == 0
    assert token._end_index == 27
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

# Generated at 2026-10-24 19:44:17.952520
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:20.491766
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:22.907509
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:25.325817
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:27.897218
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:30.312083
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:32.728285
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:35.244619
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:37.663386
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:44:39.042774
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

# Generated at 2026-10-24 19:44:40.865777
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

# Generated at 2026-10-24 19:44:42.200121
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

# Generated at 2026-10-24 19:44:43.523481
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

# Generated at 2026-10-24 19:44:46.688296
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

# Generated at 2026-10-24 19:44:56.268416
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    token = DictToken(
        {
            name_key: name_value,
            age_key: age_value,
        },
        start_index=0,
        end_index=27,
        content=content,
    )

    assert token._value == {
        name_key: name_value,
        age_key: age_value,
    }
    assert token._start_index == 0
    assert token._end_index == 27
    assert token._content == content

    assert token._child_keys["name"] is name_key
    assert token._child_keys["age"] is age_key
    assert token._child_tokens["name"] is name_value
    assert token._child_tokens["age"] is age_value

    assert token.value == {"name": "Alice", "age": 30}
    assert token.string == content
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key

# Generated at 2026-10-24 19:44:57.702844
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

# Generated at 2026-10-24 19:44:59.030266
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

# Generated at 2026-10-24 19:45:09.382477
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

    assert token._value is children
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

# Generated at 2026-10-24 19:45:18.900681
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    token = DictToken(
        {
            name_key: name_value,
            age_key: age_value,
        },
        0,
        27,
        content,
    )

    assert token._value == {
        name_key: name_value,
        age_key: age_value,
    }
    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }
    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }

    assert token.value == {"name": "Alice", "age": 30}
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key
    assert token.string == content

# Generated at 2026-10-24 19:45:21.322044
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:45:23.740667
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:45:26.162844
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:45:28.578765
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:30.995784
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:33.414244
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:35.834182
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:38.251491
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:40.673199
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:45:50.745837
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    children = {key_token: value_token}

    token = DictToken(children, 0, len(content) - 1, content)

    assert token._value is children
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.string == content
    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:45:58.017206
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

# Generated at 2026-10-24 19:45:59.353601
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

# Generated at 2026-10-24 19:46:00.783234
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

# Generated at 2026-10-24 19:46:02.430999
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

# Generated at 2026-10-24 19:46:03.804913
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

# Generated at 2026-10-24 19:46:05.201524
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

# Generated at 2026-10-24 19:46:06.525835
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

# Generated at 2026-10-24 19:46:07.948394
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

# Generated at 2026-10-24 19:46:18.905516
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

    assert token._value is children
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

    assert token.value == {
        "name": "Alice",
        "age": 30,
    }
    assert token.string == content

    assert token._get_key_token("name") is name_key
    assert token._get_child_token("name") is name_value
    assert token._get_key_token("age") is age_key
    assert token._get_child_token("age") is age_value

# Generated at 2026-10-24 19:46:21.326890
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:46:23.745359
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:46:26.161874
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:46:37.649722
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:46:40.223561
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:46:46.764802
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 3, " value")

# Generated at 2026-10-24 19:46:54.748007
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    token_mapping = {key_token: value_token}

    token = DictToken(token_mapping, 0, 16, content)

    assert token._value is token_mapping
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:46:56.155517
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

# Generated at 2026-10-24 19:47:03.648958
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"a": 1}'

    key_token = ScalarToken("a", 1, 3, content)
    value_token = ScalarToken(1, 6, 6, content)
    raw_value = {key_token: value_token}

    token = DictToken(raw_value, 0, 7, content)

    assert token._value is raw_value
    assert token._start_index == 0
    assert token._end_index == 7
    assert token._content == content

    assert token._child_keys == {"a": key_token}
    assert token._child_tokens == {"a": value_token}
    assert token.value == {"a": 1}
    assert token.string == content
    assert token.lookup(["a"]) is value_token
    assert token.lookup_key(["a"]) is key_token

# Generated at 2026-10-24 19:47:04.982918
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

# Generated at 2026-10-24 19:47:06.318554
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

# Generated at 2026-10-24 19:47:16.454395
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

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:47:24.511798
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name":"Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 8, 14, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=len(content) - 1,
        content=content,
    )

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 19:47:27.040132
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:29.455714
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:31.975793
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:34.394141
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:36.814417
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:39.227573
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 19:47:48.091695
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

# Generated at 2026-10-24 19:47:49.414738
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

# Generated at 2026-10-24 19:47:50.737170
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

# Generated at 2026-10-24 19:47:52.055535
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

# Generated at 2026-10-24 19:47:53.378763
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

# Generated at 2026-10-24 19:47:54.700192
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

# Generated at 2026-10-24 19:47:56.035255
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

# Generated at 2026-10-24 19:47:57.357538
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

# Generated at 2026-10-24 19:48:07.380411
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    value = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(value, 0, 27, content)

    assert token._value is value
    assert token._start_index == 0
    assert token._end_index == 27
    assert token._content == content

    assert token._child_keys["name"] is name_key
    assert token._child_keys["age"] is age_key
    assert token._child_tokens["name"] is name_value
    assert token._child_tokens["age"] is age_value

    assert token.value == {"name": "Alice", "age": 30}
    assert token.string == content
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key

# Generated at 2026-10-24 19:48:09.930602
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:12.348819
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:14.767741
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:32.873688
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:35.294702
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:37.713194
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:40.286994
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:42.701317
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:45.117266
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:47.535937
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:49.953063
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:52.369745
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:54.786766
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:57.202908
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:48:59.619518
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:49:02.034814
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:49:04.453372
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:49:06.872250
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:49:09.288797
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 19:49:16.326876
# Unit test for method __eq__ of class Token
def test_Token___eq__():left = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-24 19:49:17.653776
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

# Generated at 2026-10-24 19:49:26.605256
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    raw_value = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(raw_value, 0, len(content) - 1, content)

    assert token._value is raw_value
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

# Generated at 2026-10-24 19:49:36.334772
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice", "age": 30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 9, 15, content)
    age_key = ScalarToken("age", 18, 22, content)
    age_value = ScalarToken(30, 25, 26, content)

    token = DictToken(
        {
            name_key: name_value,
            age_key: age_value,
        },
        0,
        len(content) - 1,
        content,
    )

    assert token.string == content
    assert token.value == {"name": "Alice", "age": 30}

    assert token.lookup(["name"]) is name_value
    assert token.lookup(["age"]) is age_value
    assert token.lookup_key(["name"]) is name_key
    assert token.lookup_key(["age"]) is age_key

    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }
    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }

# Generated at 2026-10-24 19:49:37.650353
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