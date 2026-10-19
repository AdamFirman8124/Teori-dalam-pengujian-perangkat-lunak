

# Generated at 2022-06-13 06:56:34.112148
# Unit test for function unquote
def test_unquote():
    assert unquote('"abc"') == "abc"
    assert unquote('"abc') == '"abc'
    assert unquote('abc"') == 'abc"'
    assert unquote('"a\\"c"') == 'a\\"c'


# Generated at 2022-06-13 06:56:39.733737
# Unit test for function unquote
def test_unquote():
    ''' unit test for unquote '''
    assert unquote('"foo"') == 'foo'
    assert unquote('bar') == 'bar'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"fo\\"o"') == 'fo\\"o'

# Generated at 2022-06-13 06:56:45.181046
# Unit test for function unquote
def test_unquote():
    assert unquote('"/bin/nice"') == '/bin/nice'
    assert unquote("'\"/bin/nice\"'") == '"/bin/nice"'
    assert unquote(" '/bin/nice' ") == " '/bin/nice' "
    assert unquote('/bin/nice') == '/bin/nice'


# Generated at 2022-06-13 06:56:52.830282
# Unit test for function unquote
def test_unquote():
    assert not is_quoted('')
    assert not is_quoted('"')
    assert not is_quoted('\'')
    assert not is_quoted('\\"')
    assert not is_quoted('\\\'')
    assert not is_quoted('"\'')
    assert not is_quoted('""')
    assert not is_quoted('\'\'')
    assert not is_quoted('?\'')
    assert not is_quoted('A"')
    assert not is_quoted('A"\'')
    assert not is_quoted('"A')
    assert not is_quoted('\'A')
    assert is_quoted('\'A\'')
    assert is_quoted('"A"')
    assert is_quoted('\'A\'\'')
   

# Generated at 2022-06-13 06:57:03.708650
# Unit test for function unquote
def test_unquote():
    data = " 'unquoted string'"
    assert unquote(data) == 'unquoted string'
    data = ' "quoted string"'
    assert unquote(data) == 'quoted string'
    data = '"quoted string with spaces"'
    assert unquote(data) == 'quoted string with spaces'
    data = '"quoted string with spaces and \'singles quotes\'"'
    assert unquote(data) == 'quoted string with spaces and \'singles quotes\''
    data = '"quoted string with spaces and "double quotes""'
    assert unquote(data) == 'quoted string with spaces and "double quotes"'
    # Test escaped quotes
    data = '"quoted string with escaped \\"quotes\\""'

# Generated at 2022-06-13 06:57:09.960248
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == 'test'
    assert unquote('this is not quoted') == 'this is not quoted'
    assert unquote("'test'") == 'test'
    assert unquote("'test1' test2 'test3'") == 'test1\' test2 \'test3'
    assert unquote("\"test1\" test2 \"test3\"") == 'test1\' test2 \'test3'

# Generated at 2022-06-13 06:57:19.294049
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"')                == 'foo'
    assert unquote('"fo\"o"')              == 'fo\"o'
    assert unquote('"\"foo\""')            == '\"foo\"'
    assert unquote('"foo bar"')            == 'foo bar'
    assert unquote('"foo\\"bar"')          == 'foo\\"bar'
    assert unquote('"foobar"')             == 'foobar'
    assert unquote('\'"foo"\'')            == '\'foo\''
    assert unquote('\'"fo\\"o"\'')         == '\'fo\\"o\''
    assert unquote('\'"\\"foo\\""\'')      == '\'\\"foo\\"\''

# Generated at 2022-06-13 06:57:27.359422
# Unit test for function unquote
def test_unquote():
    assert is_quoted('"foo"')
    assert not is_quoted('foo"')
    assert not is_quoted('"foo')
    assert not is_quoted('')
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"foo\\"') == 'foo\\"'
    assert unquote('\'foo"') == '\'foo"'
    assert unquote('\'foo\'') == 'foo'
    assert unquote('"foo"bar') == '"foo"bar'
    assert unquote('') == ''


# Generated at 2022-06-13 06:57:31.106775
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"')
    assert is_quoted("'test'")
    assert is_quoted('"test\\"test"')
    assert not is_quoted('test')
    assert not is_quoted('')
    assert not is_quoted('"""')
    assert not is_quoted('"test"other')


# Generated at 2022-06-13 06:57:38.660503
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'hello'")
    assert is_quoted('"hello"')
    assert is_quoted('"hello') == False
    assert is_quoted("'hello") == False
    assert is_quoted('"hello\\"') == False
    assert is_quoted("'hello\\'") == False
    assert is_quoted("hello") == False
    assert is_quoted("'hell''o'") == False
    assert is_quoted("'hell'o'") == False
    assert is_quoted("''") == False
    