

# Generated at 2026-10-24 15:40:29.341527
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    # Constructor with explicit content
    content = "hello world"
    token = ScalarToken("hello", 0, 4, content)

    # constructor stored state
    assert token._value == "hello"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == content

    # public behavior derived from constructor
    assert token.value == "hello"
    assert token.string == "hello"
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 5, 4)
    assert hash(token) == hash("hello")
    assert repr(token) == "ScalarToken('hello')"

    # Constructor with default content=""
    default_token = ScalarToken(42, 0, 1)
    assert default_token._value == 42
    assert default_token._start_index == 0
    assert default_token._end_index == 1
    assert default_token._content == ""
    assert default_token.value == 42
    assert default_token.string == ""

# Generated at 2026-10-24 15:40:49.616965
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:41:11.427423
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

# Generated at 2026-10-24 15:41:59.024113
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 15:42:33.961687
# Unit test for method __eq__ of class Token
def test_Token___eq__():t1 = ScalarToken("x", 0, 0, "x")

# Generated at 2026-10-24 15:42:37.137053
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    # Constructor with explicit content
    content = "hello world"
    token = ScalarToken("hello", 0, 4, content)

    # constructor stored state
    assert token._value == "hello"
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == content

    # public behavior derived from constructor
    assert token.value == "hello"
    assert token.string == "hello"
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 5, 4)
    assert hash(token) == hash("hello")
    assert repr(token) == "ScalarToken('hello')"

    # Constructor with default content=""
    default_token = ScalarToken(42, 0, 1)
    assert default_token._value == 42
    assert default_token._start_index == 0
    assert default_token._end_index == 1
    assert default_token._content == ""
    assert default_token.value == 42
    assert default_token.string == ""

# Generated at 2026-10-24 15:43:17.993789
# Unit test for method lookup_key of class Token

# Generated at 2026-10-24 15:43:35.609104
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():content = '{"outer": {"inner": 42}}'

# Generated at 2026-10-24 15:43:56.805357
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:44:15.031342
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:45:06.231174
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:45:26.415068
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:46:35.357666
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:47:03.671669
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:47:23.040274
# Unit test for method lookup of class Token
def test_Token_lookup():key_token = ScalarToken("items", 0, 4, "items")

# Generated at 2026-10-24 15:47:24.472156
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:47:25.948557
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:47:50.687002
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:47:52.074723
# Unit test for method lookup of class Token
def test_Token_lookup():key_token = ScalarToken("items", 0, 4, "items")

# Generated at 2026-10-24 15:48:10.308587
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:48:12.990034
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:48:15.501219
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:48:17.909531
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:48:20.322727
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:48:22.747774
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:48:25.160101
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:48:26.729034
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:48:59.044726
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:49:01.714896
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:49:04.233660
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:49:06.767775
# Unit test for method lookup of class Token

# Generated at 2026-10-24 15:49:09.435247
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:49:11.848011
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:49:14.261185
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 15:49:16.674442
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 15:49:19.087429
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 15:49:21.670536
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 15:49:24.083585
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 15:49:43.942900
# Unit test for method __eq__ of class Token
def test_Token___eq__():token1 = ScalarToken("hello", 0, 4, content="hello")

# Generated at 2026-10-24 15:49:45.376898
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:49:46.808539
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:49:48.241873
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:49:49.675625
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)

# Generated at 2026-10-24 15:49:51.211760
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:49:52.749626
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:50:09.235448
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:50:10.771608
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # equal: same value, same start/end
    t1 = ScalarToken("hello", 0, 4, content="hello")
    t2 = ScalarToken("hello", 0, 4, content="hello")
    assert t1 == t2
    assert t2 == t1

# Generated at 2026-10-24 15:50:12.306223
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"name": "alice", "age": 30}'

    key1 = ScalarToken("name", start_index=1, end_index=6, content=content)
    val1 = ScalarToken("alice", start_index=9, end_index=15, content=content)