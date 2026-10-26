

# Generated at 2026-10-25 11:07:26.501773
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(
        value="example",
        start_index=2,
        end_index=8,
        content='  "example"',
    )

    assert token._value == "example"
    assert token._start_index == 2
    assert token._end_index == 8
    assert token._content == '  "example"'
    assert token.value == "example"
    assert token.string == '"example'

# Generated at 2026-10-25 11:07:30.025269
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:07:32.753532
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:07:35.168057
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:07:37.754198
# Unit test for constructor of class ListToken

# Generated at 2026-10-25 11:07:40.408361
# Unit test for constructor of class ListToken

# Generated at 2026-10-25 11:07:42.823723
# Unit test for constructor of class ListToken

# Generated at 2026-10-25 11:07:45.240777
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 11:07:47.655180
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 11:07:53.684755
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():token = ScalarToken(42, 0, 1, "42")

# Generated at 2026-10-25 11:08:00.393351
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    value = "example"
    content = "0123456789"

    token = ScalarToken(
        value=value,
        start_index=2,
        end_index=5,
        content=content,
    )

    assert token._value == value
    assert token._start_index == 2
    assert token._end_index == 5
    assert token._content == content

    assert token.value == value
    assert token.string == "2345"

# Generated at 2026-10-25 11:08:15.303150
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-25 11:08:18.210718
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:27.836337
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:08:30.940364
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:37.086384
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:08:39.898329
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:42.314847
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:44.929584
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:47.683858
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:08:50.102653
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:08:52.515415
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:08:54.936109
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:57.349537
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:08:59.778922
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:09:02.193634
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:09:05.484244
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:09:08.373965
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:09:11.464060
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:09:27.560846
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:09:30.503823
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:09:50.675790
# Unit test for method __eq__ of class Token
def test_Token___eq__():first = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-25 11:09:59.898608
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:10:02.620602
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:10:05.067778
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:10:07.451995
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:10:08.884222
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-25 11:10:34.395348
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"abc": 1, "xyz": [1, 2, 3]}'

    # Equal tokens: same value, start_index, end_index
    token_1 = ScalarToken("abc", 1, 3, content)
    token_2 = ScalarToken("abc", 1, 3, content)
    assert token_1 == token_2
    assert token_2 == token_1

    # Not equal: different values
    token_3 = ScalarToken("xyz", 1, 3, content)
    assert token_1 != token_3

    # Not equal: different start_index
    token_4 = ScalarToken("abc", 2, 3, content)
    assert token_1 != token_4

    # Not equal: different end_index
    token_5 = ScalarToken("abc", 1, 4, content)
    assert token_1 != token_5

    # Not equal when compared against a non-Token object
    assert token_1 != "abc"
    assert token_1 != None  # noqa: E711

    # DictToken equality is based on resolved values
    dict_token_1 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    dict_token_2 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 == dict_token_2

    dict_token_3 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(2, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 != dict_token_3

# Generated at 2026-10-25 11:10:37.370533
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:10:40.238485
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:10:43.207837
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:10:46.176470
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:10:56.305330
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("hello", 0, 4, "hello")


# Generated at 2026-10-25 11:11:22.232037
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 0, 4, "value")


# Generated at 2026-10-25 11:11:25.292180
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:11:31.949395
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:11:35.021528
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:11:37.991280
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:11:40.859885
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"abc": 1, "xyz": [1, 2, 3]}'

    # Equal tokens: same value, start_index, end_index
    token_1 = ScalarToken("abc", 1, 3, content)
    token_2 = ScalarToken("abc", 1, 3, content)
    assert token_1 == token_2
    assert token_2 == token_1

    # Not equal: different values
    token_3 = ScalarToken("xyz", 1, 3, content)
    assert token_1 != token_3

    # Not equal: different start_index
    token_4 = ScalarToken("abc", 2, 3, content)
    assert token_1 != token_4

    # Not equal: different end_index
    token_5 = ScalarToken("abc", 1, 4, content)
    assert token_1 != token_5

    # Not equal when compared against a non-Token object
    assert token_1 != "abc"
    assert token_1 != None  # noqa: E711

    # DictToken equality is based on resolved values
    dict_token_1 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    dict_token_2 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 == dict_token_2

    dict_token_3 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(2, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 != dict_token_3

# Generated at 2026-10-25 11:11:43.828050
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:11:47.311357
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:11:50.082004
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:11:53.078397
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:11:58.076503
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:12:04.104173
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:12:06.526582
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:12:08.936625
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:12:11.734138
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("abc", 0, 2, "abc")

# Generated at 2026-10-25 11:12:36.020392
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 5, "0123456789")


# Generated at 2026-10-25 11:12:38.919673
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:12:41.749513
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:12:44.654654
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:12:47.522237
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:12:49.940099
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:12:52.383701
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:12:54.803769
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:12:57.220888
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:12:59.642169
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:02.060863
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:04.480003
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:06.900427
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:09.317101
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:11.732406
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:13:13.170438
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-25 11:13:33.501431
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"abc": 1, "xyz": [1, 2, 3]}'

    # Equal tokens: same value, start_index, end_index
    token_1 = ScalarToken("abc", 1, 3, content)
    token_2 = ScalarToken("abc", 1, 3, content)
    assert token_1 == token_2
    assert token_2 == token_1

    # Not equal: different values
    token_3 = ScalarToken("xyz", 1, 3, content)
    assert token_1 != token_3

    # Not equal: different start_index
    token_4 = ScalarToken("abc", 2, 3, content)
    assert token_1 != token_4

    # Not equal: different end_index
    token_5 = ScalarToken("abc", 1, 4, content)
    assert token_1 != token_5

    # Not equal when compared against a non-Token object
    assert token_1 != "abc"
    assert token_1 != None  # noqa: E711

    # DictToken equality is based on resolved values
    dict_token_1 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    dict_token_2 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 == dict_token_2

    dict_token_3 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(2, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 != dict_token_3

# Generated at 2026-10-25 11:13:36.366197
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:13:52.327305
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:14:44.057103
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 0, 4, "value")


# Generated at 2026-10-25 11:16:06.698333
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"abc": 1, "xyz": [1, 2, 3]}'

    # Equal tokens: same value, start_index, end_index
    token_1 = ScalarToken("abc", 1, 3, content)
    token_2 = ScalarToken("abc", 1, 3, content)
    assert token_1 == token_2
    assert token_2 == token_1

    # Not equal: different values
    token_3 = ScalarToken("xyz", 1, 3, content)
    assert token_1 != token_3

    # Not equal: different start_index
    token_4 = ScalarToken("abc", 2, 3, content)
    assert token_1 != token_4

    # Not equal: different end_index
    token_5 = ScalarToken("abc", 1, 4, content)
    assert token_1 != token_5

    # Not equal when compared against a non-Token object
    assert token_1 != "abc"
    assert token_1 != None  # noqa: E711

    # DictToken equality is based on resolved values
    dict_token_1 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    dict_token_2 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 == dict_token_2

    dict_token_3 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(2, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 != dict_token_3

# Generated at 2026-10-25 11:16:30.862006
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 3, " value")


# Generated at 2026-10-25 11:16:37.407790
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = '{"abc": 1, "xyz": [1, 2, 3]}'

    # Equal tokens: same value, start_index, end_index
    token_1 = ScalarToken("abc", 1, 3, content)
    token_2 = ScalarToken("abc", 1, 3, content)
    assert token_1 == token_2
    assert token_2 == token_1

    # Not equal: different values
    token_3 = ScalarToken("xyz", 1, 3, content)
    assert token_1 != token_3

    # Not equal: different start_index
    token_4 = ScalarToken("abc", 2, 3, content)
    assert token_1 != token_4

    # Not equal: different end_index
    token_5 = ScalarToken("abc", 1, 4, content)
    assert token_1 != token_5

    # Not equal when compared against a non-Token object
    assert token_1 != "abc"
    assert token_1 != None  # noqa: E711

    # DictToken equality is based on resolved values
    dict_token_1 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    dict_token_2 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(1, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 == dict_token_2

    dict_token_3 = DictToken(
        {ScalarToken("abc", 1, 3, content): ScalarToken(2, 6, 6, content)},
        0,
        6,
        content,
    )
    assert dict_token_1 != dict_token_3

# Generated at 2026-10-25 11:16:58.403341
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:17:00.718970
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-25 11:17:11.614157
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:17:14.685789
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:17:17.654388
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:17:33.452072
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")