

# Generated at 2022-06-13 06:56:37.173096
# Unit test for function is_quoted
def test_is_quoted():
	assert not is_quoted('')
	assert not is_quoted('a')
	assert is_quoted('"a"')
	assert is_quoted("'a'")
	assert is_quoted('"ab"')
	assert is_quoted("'ab'")
	assert not is_quoted('\\"a\\"')
	assert not is_quoted("\\'a\\'")



# Generated at 2022-06-13 06:56:46.672356
# Unit test for function unquote
def test_unquote():
    assert unquote(u'hello') is u'hello'
    assert unquote(u'"hello"') is u'hello'
    assert unquote(u'"hello') is u'"hello'
    assert unquote(u"'hello'") is u'hello'
    assert unquote(u"'hello") is u"'" + u'hello'
    assert unquote(u"'he'llo") is u"'" + u"he'llo"
    assert unquote(u'"he\\"llo"') is u'he\\"llo'
    assert unquote(u'"\\"hello"') is u'"hello'
    assert unquote(u'"hello\\""') is u'hello\\"'
    assert unquote(u'"hello"') is u'hello'
    assert unquote(u'"he\'llo"') is u'he\'llo'
   

# Generated at 2022-06-13 06:56:49.501236
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'foo'")
    assert is_quoted('"foo"')

    assert not is_quoted("'fo\"o'")
    assert not is_quoted("'fo\\'o'")



# Generated at 2022-06-13 06:56:56.288647
# Unit test for function unquote
def test_unquote():
    testdata = [
        ('"foobar"', 'foobar'),
        ('"foo\\"bar"', '"foo"bar"'),
        ("'foobar'", 'foobar'),
        ("'foo\\'bar'", "'foo'bar'"),
        ('foobar"', 'foobar"'),
        ('foobar', 'foobar'),
    ]

    for data in testdata:
        assert unquote(data[0]) == data[1]

# Generated at 2022-06-13 06:56:59.928349
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'foo bar'") == True
    assert is_quoted("\"foo bar\"") == True
    assert is_quoted("'foo bar") == False


# Generated at 2022-06-13 06:57:05.236295
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello"') == "hello"
    assert unquote("'hello'") == "hello"
    assert unquote("'hel\'lo'") == "hel\'lo"
    assert unquote("'hel\"lo'") == "hel\"lo"
    assert unquote("'hello") == "'hello"
    assert unquote("hello'") == "hello'"


# Generated at 2022-06-13 06:57:11.005653
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'
    assert unquote("hello") == 'hello'
    assert unquote("'hello\\''") == "'hello'"
    assert unquote("'hello\\\\'") == "hello\\"
    assert unquote("'hello\\\\\\''") == "'hello\\'"
    assert unquote("'\\\\\\''") == "\\'"


# Generated at 2022-06-13 06:57:13.369006
# Unit test for function unquote
def test_unquote():

    assert 'foobar' == unquote('foobar')
    assert 'foo\'bar' == unquote('foo\'bar')
    assert 'foobar' == unquote('"foobar"')
    assert 'foo"bar' == unquote('"foo"bar"')
    assert 'foobar' == unquote('\'foobar\'')
    assert 'foo\'bar' == unquote('\'foo\'bar\'')

# Generated at 2022-06-13 06:57:27.825591
# Unit test for function unquote
def test_unquote():
    r = unquote('"test"')
    assert r == 'test'

    r = unquote("'test'")
    assert r == 'test'

    r = unquote('"""test"""')
    assert r == '"test"'

    r = unquote("'''test'''")
    assert r == "'test'"

    r = unquote("'''test'")
    assert r == "'''test'"

    r = unquote("'test'''")
    assert r == "'test'''"

    r = unquote("'test\"'")
    assert r == 'test"'

    r = unquote("'test'")
    assert r == 'test'

    r = unquote("'test''")
    assert r == "'test''"

    r = unquote("'test\"")

# Generated at 2022-06-13 06:57:35.528583
# Unit test for function unquote
def test_unquote():
    # unquote("foo") should return "foo"
    assert unquote("foo") == "foo"

    # unquote("\"foo\"") should return "foo"
    assert unquote("\"foo\"") == "foo"

    # unquote("'foo'") should return "foo"
    assert unquote("'foo'") == "foo"

    # unquote("\"fo'o\"") should return "fo'o"
    assert unquote("\"fo'o\"") == "fo'o"

    # unquote("'\"foo\"'") should return "'\"foo\"'"
    assert unquote("'\"foo\"'") == "'\"foo\"'"

    # unquote("foo") should return "'\"foo\"'"
    assert unquote("'\"foo\"'") == "'\"foo\"'"
