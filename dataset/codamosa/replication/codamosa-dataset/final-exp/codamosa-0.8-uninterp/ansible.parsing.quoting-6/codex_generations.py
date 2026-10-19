

# Generated at 2022-06-13 06:56:36.249554
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello"')
    assert is_quoted("'hello'")
    assert is_quoted('"hello\\""')
    assert not is_quoted('"hello\\"')
    assert not is_quoted('"hello\\"')
    assert not is_quoted('hello')



# Generated at 2022-06-13 06:56:37.694309
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello"')
    assert not is_quoted('foo')


# Generated at 2022-06-13 06:56:47.319503
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"') == True
    assert is_quoted("'test'") == True
    assert is_quoted('"test') == False
    assert is_quoted("'test") == False
    assert is_quoted('test"') == False
    assert is_quoted("test'") == False
    assert is_quoted('"test""') == False
    assert is_quoted("'test''") == False
    assert is_quoted('"test"test"') == False
    assert is_quoted("'test'test'") == False
    assert is_quoted('"test\"') == True    # the quote character is escaped
    assert is_quoted("'test\'") == True    # the quote character is escaped
    assert is_quoted('"') == True


# Generated at 2022-06-13 06:56:47.861600
# Unit test for function unquote
def test_unquote():
    pass

# Generated at 2022-06-13 06:56:51.754351
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted('foo')
    assert not is_quoted('"foo')
    assert not is_quoted('"fo\\o')
    assert is_quoted('"foo"')
    assert is_quoted('"foo\\""')
    assert is_quoted("'foo'")
    assert is_quoted("'foo\\''")


# Generated at 2022-06-13 06:56:57.065948
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote('"foo\\""') == 'foo\\"'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"foo\'bar"') == "foo\'bar"
    assert unquote('"foo"bar"') == 'foobar"'
    assert unquote('x"foo"') == 'x"foo"'
    assert unquote('"foo"x') == '"foo"x'
    assert unquote('x"foo"x') == 'x"foo"x'

# Generated at 2022-06-13 06:57:04.948524
# Unit test for function is_quoted
def test_is_quoted():
    data_test = [
        ('test', False),
        ('"test"', True),
        ('test"', False),
        ('"test', False),
        ('""', False),
        ('"test\\"', False),
        ("'test'", True),
        ("test'", False),
        ("'test", False),
        ("''", False),
        ("'test\\'", False),
    ]
    for (str, expected) in data_test:
        assert is_quoted(str) == expected


# Generated at 2022-06-13 06:57:09.254538
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"')
    assert is_quoted('"test\\""')
    assert is_quoted('\'test\'')
    assert not is_quoted('test')
    assert not is_quoted('\\"test"')


# Generated at 2022-06-13 06:57:13.734685
# Unit test for function unquote
def test_unquote():
    assert unquote("abcd") == "abcd"
    assert unquote("'abcd'") == "abcd"
    assert unquote("\"abcd\"") == "abcd"
    assert unquote("'a\\'bcd'") == "a'bcd"
    assert unquote("'abcd\\''") == "abcd'"


# Generated at 2022-06-13 06:57:21.639146
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello"')
    assert is_quoted('"hello"')
    assert not is_quoted('hello')
    assert not is_quoted('"hello')
    assert not is_quoted('hello"')
    assert is_quoted('"no spaces"')
    assert is_quoted('"spaces here"')
    assert is_quoted("'spaces here'")
    assert is_quoted(r'"\" hello"')
    assert is_quoted(r'"\" hello \" "')
