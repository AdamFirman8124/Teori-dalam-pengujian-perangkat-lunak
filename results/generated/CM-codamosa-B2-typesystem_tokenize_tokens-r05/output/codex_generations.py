

# Generated at 2026-10-24 23:26:06.854745
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '{"a": 1, "b": [10, 20], "c": {"d": "x"}}'

    # Build token tree manually (values are Token instances for DictToken)
    scalar_1 = ScalarToken(1, 7, 7, content)
    scalar_10 = ScalarToken(10, 14, 15, content)
    scalar_20 = ScalarToken(20, 18, 19, content)
    list_b = ListToken([scalar_10, scalar_20], 11, 20, content)
    scalar_x = ScalarToken("x", 33, 35, content)
    dict_d = DictToken({ScalarToken("d", 30, 32, content): scalar_x}, 29, 36, content)
    key_a = ScalarToken("a", 1, 3, content)
    key_b = ScalarToken("b", 10, 12, content)
    key_c = ScalarToken("c", 23, 25, content)
    dict_root = DictToken(
        {key_a: scalar_1, key_b: list_b, key_c: dict_d}, 0, 37, content
    )

    # Lookup a nested scalar by index path
    token = dict_root.lookup(["b", 1])
    assert token.value == 20
    assert token.start == Position(line_no=1, column_no=19, index=18)
    assert token.end == Position(line_no=1, column_no=20, index=19)

    # Lookup a nested dict
    token = dict_root.lookup(["c"])
    assert token.value == {"d": "x"}

    # Lookup a deeply nested scalar
    token = dict_root.lookup(["c", "d"])
    assert token.value == "x"

    # Lookup the root itself (empty index)
    token = dict_root.lookup([])
    assert token is dict_root

# Generated at 2026-10-24 23:26:08.287414
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '{"a": 1, "b": [10, 20], "c": {"d": "x"}}'

    # Build token tree manually (values are Token instances for DictToken)
    scalar_1 = ScalarToken(1, 7, 7, content)
    scalar_10 = ScalarToken(10, 14, 15, content)
    scalar_20 = ScalarToken(20, 18, 19, content)
    list_b = ListToken([scalar_10, scalar_20], 11, 20, content)
    scalar_x = ScalarToken("x", 33, 35, content)
    dict_d = DictToken({ScalarToken("d", 30, 32, content): scalar_x}, 29, 36, content)
    key_a = ScalarToken("a", 1, 3, content)
    key_b = ScalarToken("b", 10, 12, content)
    key_c = ScalarToken("c", 23, 25, content)
    dict_root = DictToken(
        {key_a: scalar_1, key_b: list_b, key_c: dict_d}, 0, 37, content
    )

    # Lookup a nested scalar by index path
    token = dict_root.lookup(["b", 1])
    assert token.value == 20
    assert token.start == Position(line_no=1, column_no=19, index=18)
    assert token.end == Position(line_no=1, column_no=20, index=19)

    # Lookup a nested dict
    token = dict_root.lookup(["c"])
    assert token.value == {"d": "x"}

    # Lookup a deeply nested scalar
    token = dict_root.lookup(["c", "d"])
    assert token.value == "x"

    # Lookup the root itself (empty index)
    token = dict_root.lookup([])
    assert token is dict_root

# Generated at 2026-10-24 23:26:16.979756
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    assert token == ScalarToken("value", 1, 5, " value")
    assert token == ScalarToken("value", 1, 5, "different content")

    assert token != ScalarToken("other", 1, 5, " other")
    assert token != ScalarToken("value", 0, 5, "value")
    assert token != ScalarToken("value", 1, 4, " valu")
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:26:25.286597
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name":"Alice","age":30}'

    name_key = ScalarToken("name", 1, 6, content)
    name_value = ScalarToken("Alice", 8, 14, content)
    age_key = ScalarToken("age", 16, 20, content)
    age_value = ScalarToken(30, 22, 23, content)

    value = {
        name_key: name_value,
        age_key: age_value,
    }

    token = DictToken(value, 0, 24, content)

    assert token._value is value
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
    assert token.string == content
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key

# Generated at 2026-10-24 23:26:32.941301
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    assert token == token
    assert token == ScalarToken("value", 1, 5, "different content")
    assert token != ScalarToken("different", 1, 5, " value")
    assert token != ScalarToken("value", 2, 5, " value")
    assert token != ScalarToken("value", 1, 6, " value")
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:26:40.031613
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

    assert token.string == content
    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token
    assert token._child_tokens == {"name": value_token}
    assert token._child_keys == {"name": key_token}

# Generated at 2026-10-24 23:26:46.366978
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Tokens with the same value and indexes are equal.
    assert token == ScalarToken("value", 1, 5, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 0, 5, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:26:47.814976
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '{"a": 1, "b": [10, 20], "c": {"d": "x"}}'

    # Build token tree manually (values are Token instances for DictToken)
    scalar_1 = ScalarToken(1, 7, 7, content)
    scalar_10 = ScalarToken(10, 14, 15, content)
    scalar_20 = ScalarToken(20, 18, 19, content)
    list_b = ListToken([scalar_10, scalar_20], 11, 20, content)
    scalar_x = ScalarToken("x", 33, 35, content)
    dict_d = DictToken({ScalarToken("d", 30, 32, content): scalar_x}, 29, 36, content)
    key_a = ScalarToken("a", 1, 3, content)
    key_b = ScalarToken("b", 10, 12, content)
    key_c = ScalarToken("c", 23, 25, content)
    dict_root = DictToken(
        {key_a: scalar_1, key_b: list_b, key_c: dict_d}, 0, 37, content
    )

    # Lookup a nested scalar by index path
    token = dict_root.lookup(["b", 1])
    assert token.value == 20
    assert token.start == Position(line_no=1, column_no=19, index=18)
    assert token.end == Position(line_no=1, column_no=20, index=19)

    # Lookup a nested dict
    token = dict_root.lookup(["c"])
    assert token.value == {"d": "x"}

    # Lookup a deeply nested scalar
    token = dict_root.lookup(["c", "d"])
    assert token.value == "x"

    # Lookup the root itself (empty index)
    token = dict_root.lookup([])
    assert token is dict_root

# Generated at 2026-10-24 23:26:56.629438
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

# Generated at 2026-10-24 23:27:03.748631
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"outer": {"inner": 1}}'

    outer_key = ScalarToken("outer", 1, 7, content)
    inner_key = ScalarToken("inner", 11, 17, content)
    inner_value = ScalarToken(1, 20, 20, content)

    inner_dict = DictToken(
        {inner_key: inner_value},
        10,
        21,
        content,
    )
    root = DictToken(
        {outer_key: inner_dict},
        0,
        22,
        content,
    )

    assert root.lookup_key(["outer"]) is outer_key
    assert root.lookup_key(["outer", "inner"]) is inner_key

# Generated at 2026-10-24 23:27:12.082972
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    children = {key_token: value_token}

    token = DictToken(children, 0, 16, content)

    assert token._value is children
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 23:27:20.583949
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": 42}'
    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken(42, 9, 10, content)
    values = {key_token: value_token}

    token = DictToken(values, 0, 11, content)

    assert token._value is values
    assert token._start_index == 0
    assert token._end_index == 11
    assert token._content == content

    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token

    assert token.value == {"name": 42}
    assert token.string == content
    assert token._get_key_token("name") is key_token
    assert token._get_child_token("name") is value_token

# Generated at 2026-10-24 23:27:28.366161
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    content = '{"outer": {"inner": 1}}'

    outer_key = ScalarToken("outer", 1, 7, content)
    inner_key = ScalarToken("inner", 11, 17, content)
    inner_value = ScalarToken(1, 20, 20, content)

    inner_dict = DictToken({inner_key: inner_value}, 10, 21, content)
    root_dict = DictToken({outer_key: inner_dict}, 0, 22, content)

    assert root_dict.lookup_key(["outer"]) is outer_key
    assert root_dict.lookup_key(["outer", "inner"]) is inner_key

# Generated at 2026-10-24 23:27:29.801497
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '{"a": 1, "b": [10, 20], "c": {"d": "x"}}'

    # Build token tree manually (values are Token instances for DictToken)
    scalar_1 = ScalarToken(1, 7, 7, content)
    scalar_10 = ScalarToken(10, 14, 15, content)
    scalar_20 = ScalarToken(20, 18, 19, content)
    list_b = ListToken([scalar_10, scalar_20], 11, 20, content)
    scalar_x = ScalarToken("x", 33, 35, content)
    dict_d = DictToken({ScalarToken("d", 30, 32, content): scalar_x}, 29, 36, content)
    key_a = ScalarToken("a", 1, 3, content)
    key_b = ScalarToken("b", 10, 12, content)
    key_c = ScalarToken("c", 23, 25, content)
    dict_root = DictToken(
        {key_a: scalar_1, key_b: list_b, key_c: dict_d}, 0, 37, content
    )

    # Lookup a nested scalar by index path
    token = dict_root.lookup(["b", 1])
    assert token.value == 20
    assert token.start == Position(line_no=1, column_no=19, index=18)
    assert token.end == Position(line_no=1, column_no=20, index=19)

    # Lookup a nested dict
    token = dict_root.lookup(["c"])
    assert token.value == {"d": "x"}

    # Lookup a deeply nested scalar
    token = dict_root.lookup(["c", "d"])
    assert token.value == "x"

    # Lookup the root itself (empty index)
    token = dict_root.lookup([])
    assert token is dict_root

# Generated at 2026-10-24 23:27:35.430332
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(value=None, start_index=1, end_index=3, content="012345")

    assert repr(token) == "Token('123')"

# Generated at 2026-10-24 23:27:45.266305
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

# Generated at 2026-10-24 23:27:54.068497
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

    token = DictToken(value, 0, len(content) - 1, content)

    assert token._value is value
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
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key
    assert token.string == content

# Generated at 2026-10-24 23:27:56.600832
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:27:59.118323
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:28:07.071468
# Unit test for method __eq__ of class Token
def test_Token___eq__():left = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-24 23:28:15.371557
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Differences in value or position make tokens unequal.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # Tokens are not equal to objects of other types.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:28:23.048613
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Equal when value and indexes match; content is not considered.
    assert token == ScalarToken("value", 1, 5, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 2, 5, " value")
    assert token != ScalarToken("value", 1, 6, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:28:29.180232
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'
    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    token_value = {key_token: value_token}

    token = DictToken(token_value, 0, len(content) - 1, content)

    assert token._value is token_value
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}
    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token

    assert token.value == {"name": "Alice"}
    assert token.string == content

# Generated at 2026-10-24 23:28:39.919632
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Tokens are equal when value and indexes match.
    assert token == ScalarToken("value", 1, 5, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 2, 5, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # Non-Token instances are never equal.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:28:42.444650
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:28:44.862732
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:28:47.277687
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:28:49.694730
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:28:52.113460
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:28:54.684315
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:28:57.106053
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:28:59.524381
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:29:01.945012
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:29:04.359369
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:29:21.312544
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a": 1, "b": 2}'

# Generated at 2026-10-24 23:29:27.671619
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Value and both indexes participate in equality.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A Token is not equal to an unrelated object.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:29:35.037826
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Equality depends on value and start/end indexes, not source content.
    assert token == ScalarToken("value", 1, 3, "different content")

    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()
    assert token != None

# Generated at 2026-10-24 23:29:42.415199
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
    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token

    assert token.value == {"name": "Alice"}
    assert token.string == content

# Generated at 2026-10-24 23:29:50.393486
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 0, 4, "other")

    # Value and both indexes participate in equality.
    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")

    # A token is never equal to an unrelated object.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:29:53.038811
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:29:55.456991
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:29:57.873814
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:00.290617
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:02.706613
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:05.124494
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:07.543364
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:09.963224
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:12.378818
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:14.796418
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:17.220138
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:19.635794
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:22.054355
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:24.472323
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:26.891809
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:29.311940
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:31.727133
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:34.144579
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:36.561664
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:38.979026
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:41.400103
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:43.820353
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:46.236445
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:48.654440
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:30:51.071008
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:53.486966
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:55.906188
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:30:58.322681
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:31:00.740081
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:31:03.158008
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:31:12.542616
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 3, " value")

# Generated at 2026-10-24 23:31:21.106972
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    assert token == ScalarToken("value", 1, 3, "different content")
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")
    assert token != object()

# Generated at 2026-10-24 23:31:29.821525
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

# Generated at 2026-10-24 23:31:38.120887
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    token_mapping = {key_token: value_token}

    token = DictToken(token_mapping, 0, 16, content)

    assert token._value == token_mapping
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token
    assert token.string == content

# Generated at 2026-10-24 23:31:46.441185
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
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token
    assert token.string == content

# Generated at 2026-10-24 23:31:56.653805
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'
    key_token = ScalarToken("name", 2, 5, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    children = {key_token: value_token}

    token = DictToken(children, 0, len(content) - 1, content)

    assert token._value is children
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content
    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token
    assert token.value == {"name": "Alice"}
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-24 23:31:59.071787
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:32:01.488463
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:32:04.095772
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:32:06.513759
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:08.929558
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:11.345688
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:13.763200
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:16.180233
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:18.595630
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:32:27.786146
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 5, " value")


# Generated at 2026-10-24 23:32:38.023402
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
    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

# Generated at 2026-10-24 23:32:46.830177
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    # Tokens with the same value and boundaries are equal.
    assert token == ScalarToken("value", 0, 4, "value")

    # Content itself is not part of the equality comparison.
    assert token == ScalarToken("value", 0, 4, "other")

    # Value and token boundaries are part of the comparison.
    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")

    # A Token is not equal to an instance of another type.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:32:53.998000
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "other")  # Content is ignored.

    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")
    assert token != "value"
    assert token != None  # noqa: E711

# Generated at 2026-10-24 23:33:05.467774
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "content")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Value and both indexes participate in equality.
    assert token != ScalarToken("other", 1, 3, "content")
    assert token != ScalarToken("value", 0, 3, "content")
    assert token != ScalarToken("value", 1, 4, "content")

    # Objects that are not tokens are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:33:11.919714
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "different content")

    assert token != ScalarToken("other", 0, 4, "other")
    assert token != ScalarToken("value", 1, 4, " value")
    assert token != ScalarToken("value", 0, 3, "value")
    assert token != object()

# Generated at 2026-10-24 23:33:14.338982
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:33:20.314415
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("a", 0, 0, "a")

# Generated at 2026-10-24 23:33:27.518356
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    token_mapping = {key_token: value_token}

    token = DictToken(token_mapping, 0, len(content) - 1, content)

    assert token._value is token_mapping
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}
    assert token.value == {"name": "Alice"}
    assert token.string == content

# Generated at 2026-10-24 23:33:35.462115
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "012345")

    # Tokens are equal when value and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 3, "012345")
    assert token != ScalarToken("value", 0, 3, "012345")
    assert token != ScalarToken("value", 1, 4, "012345")

    # Tokens are not equal to instances of unrelated types.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:33:42.433426
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value ")

    # Equal when value and indexes match; content is not part of equality.
    assert token == ScalarToken("value", 1, 5, "different content")

    assert token != ScalarToken("other", 1, 5, " value ")
    assert token != ScalarToken("value", 0, 5, " value ")
    assert token != ScalarToken("value", 1, 6, " value ")
    assert token != "not a token"

# Generated at 2026-10-24 23:33:49.397454
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "other")  # Content is not compared.

    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")
    assert token != object()

# Generated at 2026-10-24 23:33:55.657354
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    assert token == ScalarToken("value", 1, 3, " value")
    assert token == ScalarToken("value", 1, 3, "different content")

    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")
    assert token != "not a token"

# Generated at 2026-10-24 23:34:02.093711
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when value and source indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A token cannot equal an unrelated object.
    assert token != "value"
    assert token != object()
    assert token != None

# Generated at 2026-10-24 23:34:04.513893
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:07.037180
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:09.452828
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:11.870543
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:14.286496
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:16.701861
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:19.120265
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:21.538907
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:34:28.514112
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a": 1}'

# Generated at 2026-10-24 23:34:35.638084
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Equality depends on value and start/end indexes, but not content.
    assert token == ScalarToken("value", 1, 3, "different content")

    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:34:43.960928
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "01234")

    # Tokens are equal when their values and index ranges match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Differences in value or position make tokens unequal.
    assert token != ScalarToken("other", 1, 3, "01234")
    assert token != ScalarToken("value", 0, 3, "01234")
    assert token != ScalarToken("value", 1, 4, "01234")

    # A token is never equal to an unrelated object.
    assert token != "value"
    assert token != None

# Generated at 2026-10-24 23:34:51.760522
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

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == len(content) - 1
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}
    assert token._child_keys["name"] is key_token
    assert token._child_tokens["name"] is value_token

    assert token.value == {"name": "Alice"}
    assert token.string == content

# Generated at 2026-10-24 23:34:58.845706
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Tokens with the same value and indices are equal.
    assert token == ScalarToken("value", 1, 5, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 2, 5, " value")
    assert token != ScalarToken("value", 1, 6, " value")

    # A Token is not equal to an unrelated object.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 23:35:01.265646
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:03.682043
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:06.240347
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:08.660507
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:11.077510
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:13.493837
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:16.063671
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:18.482211
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:20.901001
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:23.317702
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:25.735529
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:28.151665
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:30.568636
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:32.985068
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:35.405311
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:37.821149
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:40.240748
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:42.658948
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:35:45.738854
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:48.156082
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:50.573429
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:52.986908
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:55.403337
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:35:57.819707
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 23:36:00.234186
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:36:02.654158
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 23:36:05.071396
# Unit test for method __eq__ of class Token