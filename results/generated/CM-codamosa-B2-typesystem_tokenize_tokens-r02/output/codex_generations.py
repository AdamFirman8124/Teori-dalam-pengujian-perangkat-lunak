

# Generated at 2026-10-25 11:46:39.460758
# Unit test for constructor of class Token
def test_Token():
    # content is optional and defaults to ""
    token = Token("abc", 1, 3)
    assert token._value == "abc"
    assert token._start_index == 1
    assert token._end_index == 3
    assert token._content == ""

    # explicit content is stored as-is
    token = Token("abc", 1, 3, content="xabcd")
    assert token._content == "xabcd"
    assert token.string == "abc"  # slice is inclusive of end_index

    # the base class is abstract: value must be overridden
    token = Token("abc", 0, 2, content="abc")
    try:
        token.value
    except NotImplementedError:
        pass
    else:
        raise AssertionError("Token.value should raise NotImplementedError")

# Generated at 2026-10-25 11:46:42.532138
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:46:44.170485
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-25 11:46:49.990887
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 11:46:52.406849
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 11:46:54.821362
# Unit test for method lookup_key of class Token

# Generated at 2026-10-25 11:46:57.544805
# Unit test for constructor of class Token

# Generated at 2026-10-25 11:46:59.953383
# Unit test for constructor of class Token

# Generated at 2026-10-25 11:47:02.368356
# Unit test for constructor of class Token

# Generated at 2026-10-25 11:47:04.782603
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-25 11:47:21.196501
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():token = ScalarToken(42, 0, 1, "42")

# Generated at 2026-10-25 11:47:44.324026
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:47:49.894913
# Unit test for method __eq__ of class Token
def test_Token___eq__():content = '{"a": 1, "b": [2, 3]}'

# Generated at 2026-10-25 11:47:52.359397
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:47:54.772569
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:47:57.187792
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:47:59.601631
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:02.018271
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:04.434948
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:07.180731
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:09.595122
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:12.037901
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:14.450919
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:16.869181
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:19.280117
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:21.705141
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:24.206701
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:26.620654
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:48:29.042293
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:31.451548
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:33.866151
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:36.279558
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:38.693736
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:42.739837
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:48:45.689378
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:48:50.598827
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:48:53.709586
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

# Generated at 2026-10-25 11:48:56.822864
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

# Generated at 2026-10-25 11:48:59.866298
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:02.276302
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:04.690277
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:07.107135
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:09.766031
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:12.179593
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:14.594673
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:17.011950
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:19.430823
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:21.848951
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:24.261750
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:26.675095
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:29.088783
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:31.504621
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:33.919210
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:36.589279
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:39.004939
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:41.416474
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:43.829239
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:49:45.406085
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-25 11:49:48.491853
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:52.727397
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:49:55.863801
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:49:59.960392
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:50:03.136306
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:08.564869
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:50:11.604379
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:14.706315
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:50:19.928611
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:25.460540
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:50:30.383893
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

# Generated at 2026-10-25 11:50:33.030502
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:50:35.443316
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:50:38.244813
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:50:41.042869
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:43.459137
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:45.871582
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:48.286825
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:50:51.452360
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:50:54.475557
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:00.362020
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:51:05.098756
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:14.507737
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:51:23.927739
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:27.009120
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:51:29.415699
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:31.832098
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:34.246396
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:36.660633
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:39.243433
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:41.657111
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:51:44.071113
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:46.485414
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:48.902803
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:51.316619
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:53.733380
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:56.146233
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:51:58.975658
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:02.022351
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:52:05.401378
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:08.275348
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:52:11.326122
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

# Generated at 2026-10-25 11:52:17.384357
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

# Generated at 2026-10-25 11:52:38.784857
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

# Generated at 2026-10-25 11:52:41.545515
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:43.959230
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:46.373562
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:48.952510
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:51.551017
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:53.965431
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:56.379795
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:52:58.793857
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:01.208329
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:03.623762
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:06.111943
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:08.522123
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:10.934192
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:53:13.348845
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:53:15.762341
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:53:18.175295
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:53:20.605521
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:53:23.263488
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("abc", 0, 2, "abc")

# Generated at 2026-10-25 11:53:32.852043
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:35.597885
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:53:38.586471
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

# Generated at 2026-10-25 11:53:41.555776
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:53:44.428806
# Unit test for constructor of class DictToken
def test_DictToken():k = ScalarToken("a", 0, 0, "a: 1")

# Generated at 2026-10-25 11:54:02.445907
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:04.866507
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:07.282547
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:09.698211
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:12.112744
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:14.530481
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:18.116847
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:20.526506
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:22.978701
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:25.394254
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:27.807544
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:30.222988
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:32.636439
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:35.049386
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:37.461027
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:39.894371
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:42.298457
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:44.709482
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:54:47.124822
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:49.544543
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:51.958890
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:54.375104
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:56.793287
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:54:59.203448
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:55:01.618727
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:04.033212
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:06.446823
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:08.862385
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:11.276138
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:13.691351
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:16.107366
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:55:18.521271
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:55:20.935530
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:55:23.349307
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:25.764017
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:28.178569
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:34.445724
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:36.860360
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:39.275898
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:41.687838
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:44.103625
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:46.517834
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:48.984518
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:51.400335
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:53.815876
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:56.230354
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:55:58.644130
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:01.061157
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:03.477382
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:05.946314
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:08.348724
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:10.763096
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:13.179622
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:15.592111
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:18.009062
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:20.420344
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:22.835580
# Unit test for constructor of class DictToken

# Generated at 2026-10-25 11:56:25.248860
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:27.660673
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:30.074433
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:32.489808
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:34.904362
# Unit test for method __eq__ of class Token

# Generated at 2026-10-25 11:56:37.318002
# Unit test for method __eq__ of class Token