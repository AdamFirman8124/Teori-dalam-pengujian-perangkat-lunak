

# Generated at 2026-10-25 02:59:18.399717
# Unit test for constructor of class Token
def test_Token():
    value = {"key": "value"}
    token = Token(value, start_index=2, end_index=5, content="0123456789")

    assert token._value is value
    assert token._start_index == 2
    assert token._end_index == 5
    assert token._content == "0123456789"

# Generated at 2026-10-25 02:59:20.925867
# Unit test for method __repr__ of class Token

# Generated at 2026-10-25 02:59:23.341369
# Unit test for method __repr__ of class Token

# Generated at 2026-10-25 02:59:25.756911
# Unit test for method __repr__ of class Token

# Generated at 2026-10-25 02:59:28.173077
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 02:59:30.586476
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 02:59:33.001129
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 02:59:35.416766
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:37.831724
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:40.245779
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:42.662261
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 02:59:45.079447
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 02:59:47.494656
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 02:59:49.914206
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:52.326227
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:54.740533
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 02:59:57.156499
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 02:59:59.570462
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:00:01.985231
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:00:04.400117
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:06.815359
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:09.230721
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:11.644927
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:14.059752
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:16.476013
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:18.894629
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:21.313160
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:23.724368
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:26.140156
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:28.554939
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:30.969753
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:33.384457
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:35.803219
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:38.219002
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:40.631612
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:43.046733
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:45.463507
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:00:47.877031
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:00:50.293402
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:00:52.707721
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:00:59.691955
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Equality depends on value and source indexes, not content.
    assert token == ScalarToken("value", 1, 5, "different content")

    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 0, 5, " value")
    assert token != ScalarToken("value", 1, 6, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:01:06.747774
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"foo": "bar"}'
    key_token = ScalarToken("foo", 1, 5, content)
    value_token = ScalarToken("bar", 8, 12, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=13,
        content=content,
    )

    assert token._value == {key_token: value_token}
    assert token._start_index == 0
    assert token._end_index == 13
    assert token._content == content
    assert token._child_keys == {"foo": key_token}
    assert token._child_tokens == {"foo": value_token}

    assert token.value == {"foo": "bar"}
    assert token.string == content
    assert token.lookup(["foo"]) is value_token
    assert token.lookup_key(["foo"]) is key_token

# Generated at 2026-10-25 03:01:13.207131
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    # Tokens with the same value and indexes are equal.
    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "different content")

    # Value and token boundaries participate in equality.
    assert token != ScalarToken("other", 0, 4, "other")
    assert token != ScalarToken("value", 1, 4, " value")
    assert token != ScalarToken("value", 0, 3, "value")

    # A token is not equal to an unrelated object.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:01:23.751051
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    # Equality depends on value and source indexes.
    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "other content")

    # Each compared field can make tokens unequal.
    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 5, "value")

    # Non-token objects are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:01:26.168227
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:28.583197
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:30.997201
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:33.412396
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:35.827482
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:38.242092
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:40.656756
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:43.072655
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:45.486819
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:47.902379
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:50.318237
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:52.733301
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:01:55.152712
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:57.570659
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:01:59.984493
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:02.398282
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:04.812509
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:07.227493
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:09.641485
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:12.057159
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:14.474280
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:16.889082
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:19.305881
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:21.719901
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:24.135014
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:26.549850
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:28.964021
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:31.378457
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:33.794296
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:36.209493
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:02:38.625970
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:41.042027
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:02:46.900544
# Unit test for method __eq__ of class Token
def test_Token___eq__():left = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-25 03:02:55.502257
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
    assert token.lookup(["name"]) is name_value
    assert token.lookup_key(["age"]) is age_key
    assert token.string == content

# Generated at 2026-10-25 03:03:01.747262
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "012345")

    assert token == ScalarToken("value", 1, 3, "different content")
    assert token != ScalarToken("other", 1, 3, "012345")
    assert token != ScalarToken("value", 0, 3, "012345")
    assert token != ScalarToken("value", 1, 4, "012345")
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:03:10.213487
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken("name", 1, 6, content)
    value_token = ScalarToken("Alice", 9, 15, content)
    value = {key_token: value_token}

    token = DictToken(value, 0, 16, content)

    assert token._value is value
    assert token._start_index == 0
    assert token._end_index == 16
    assert token._content == content

    assert token._child_keys == {"name": key_token}
    assert token._child_tokens == {"name": value_token}

    assert token.value == {"name": "Alice"}
    assert token.string == content
    assert token.lookup(["name"]) is value_token
    assert token.lookup_key(["name"]) is key_token

# Generated at 2026-10-25 03:03:12.631760
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:15.045647
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:17.459701
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:19.878921
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:03:22.295258
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:03:24.712825
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:03:27.127326
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:29.541461
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:31.955701
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:34.368211
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:36.809203
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:39.196896
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:41.610607
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:44.025354
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:46.443160
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:48.860794
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:51.274775
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:53.690916
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:56.105023
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:03:58.519368
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:04.415513
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a":1}'

# Generated at 2026-10-25 03:04:13.428621
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

    token = DictToken(children, 0, 27, content)

    assert token._value is children
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

# Generated at 2026-10-25 03:04:23.466502
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

    assert token.string == content
    assert token.value == {"name": "Alice", "age": 30}

    assert token.lookup(["name"]) is name_value
    assert token.lookup(["age"]) is age_value
    assert token.lookup_key(["name"]) is name_key
    assert token.lookup_key(["age"]) is age_key

    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }
    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }

# Generated at 2026-10-25 03:04:31.149555
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    assert token == ScalarToken("value", 0, 4, "value")
    assert token == ScalarToken("value", 0, 4, "other")  # content is not compared

    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")
    assert token != object()

# Generated at 2026-10-25 03:04:33.562455
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:35.978483
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:38.582674
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:40.994698
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:04:43.412688
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:04:45.825900
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:04:48.242049
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:50.655971
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:53.069705
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:55.484478
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:04:57.899339
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:00.313954
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:02.728611
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:05.142357
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:07.556128
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:09.971474
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:05:12.386565
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:05:14.801736
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:05:17.215508
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:19.630713
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:22.044847
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:05:24.462222
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:05:42.751956
# Unit test for method __eq__ of class Token
def test_Token___eq__():from typesystem.tokenize.token import ScalarToken


# Generated at 2026-10-25 03:05:51.937590
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "Alice"}'

    key_token = ScalarToken(
        value="name",
        start_index=1,
        end_index=6,
        content=content,
    )
    value_token = ScalarToken(
        value="Alice",
        start_index=9,
        end_index=15,
        content=content,
    )

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
    assert token._get_key_token("name") is key_token
    assert token._get_child_token("name") is value_token

    assert token.value == {"name": "Alice"}
    assert token.string == content

# Generated at 2026-10-25 03:05:59.694935
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

# Generated at 2026-10-25 03:06:06.684765
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Differences in value or indexes make tokens unequal.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A token is not equal to an object of another type.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:06:13.313708
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "abcde")

    # Equality depends on value and start/end indexes, not content.
    assert token == ScalarToken("value", 1, 3, "xxxxx")

    assert token != ScalarToken("different", 1, 3, "abcde")
    assert token != ScalarToken("value", 0, 3, "abcde")
    assert token != ScalarToken("value", 1, 4, "abcde")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:06:15.864922
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:06:18.279073
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:06:20.694329
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:06:23.107423
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:06:25.523382
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:06:31.873727
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a": 1}'

# Generated at 2026-10-25 03:06:42.421317
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

    assert token._child_keys == {
        "name": name_key,
        "age": age_key,
    }
    assert token._child_tokens == {
        "name": name_value,
        "age": age_value,
    }

    assert token._child_keys["name"] is name_key
    assert token._child_tokens["name"] is name_value
    assert token._child_keys["age"] is age_key
    assert token._child_tokens["age"] is age_value

# Generated at 2026-10-25 03:06:52.050324
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"answer": 42}'
    key_token = ScalarToken("answer", 1, 8, content)
    value_token = ScalarToken(42, 11, 12, content)

    token = DictToken(
        {key_token: value_token},
        start_index=0,
        end_index=len(content) - 1,
        content=content,
    )

    assert token.string == content
    assert token.value == {"answer": 42}
    assert token._child_keys == {"answer": key_token}
    assert token._child_tokens == {"answer": value_token}
    assert token.lookup(["answer"]) is value_token
    assert token.lookup_key(["answer"]) is key_token

# Generated at 2026-10-25 03:06:59.931389
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

# Generated at 2026-10-25 03:07:07.652797
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "abcd")

    # Equality depends on value and start/end indexes.
    assert token == ScalarToken("value", 1, 3, "different content")

    assert token != ScalarToken("different", 1, 3, "abcd")
    assert token != ScalarToken("value", 0, 3, "abcd")
    assert token != ScalarToken("value", 1, 4, "abcde")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:07:10.071048
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:07:12.486412
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:07:14.900078
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:07:17.315142
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:07:19.729992
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:07:22.145959
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:07:24.560700
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:07:26.976444
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:07:32.904474
# Unit test for method __eq__ of class Token
def test_Token___eq__():left = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-25 03:07:40.290233
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 0, 4, "value")

    # Equality depends on value and start/end indexes.
    assert token == ScalarToken("value", 0, 4, "other content")

    assert token != ScalarToken("different", 0, 4, "value")
    assert token != ScalarToken("value", 1, 4, "value")
    assert token != ScalarToken("value", 0, 3, "value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-25 03:07:49.440511
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Tokens are equal when their values and positions match.
    assert token == ScalarToken("value", 1, 5, " value")

    # Content itself is not considered by __eq__.
    assert token == ScalarToken("value", 1, 5, "different content")

    # Value and position differences make tokens unequal.
    assert token != ScalarToken("other", 1, 5, " other")
    assert token != ScalarToken("value", 0, 5, "value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A Token is never equal to an unrelated object.
    assert token != "value"
    assert token != None

# Generated at 2026-10-25 03:08:00.860146
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Value and both indexes participate in equality.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A Token cannot equal an instance of another type.
    assert token != object()

# Generated at 2026-10-25 03:08:03.276679
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:05.694490
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:08.110043
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:10.524446
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:12.939324
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:15.353999
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:17.769513
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:20.184944
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:22.600373
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:25.016021
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:27.431681
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:29.846850
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:32.261134
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:34.676860
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:37.091992
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:39.507052
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:41.921826
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:44.337088
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:46.754535
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:49.166124
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:51.585705
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 03:08:54.004161
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:56.420657
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:08:58.835420
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:01.249150
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:03.665730
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:06.081129
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:10.216346
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:12.631622
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 03:09:15.046315
# Unit test for constructor of class DictToken