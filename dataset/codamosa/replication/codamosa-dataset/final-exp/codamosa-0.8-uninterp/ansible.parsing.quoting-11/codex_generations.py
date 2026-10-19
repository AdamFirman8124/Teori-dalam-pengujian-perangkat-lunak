

# Generated at 2022-06-13 06:56:42.172620
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote("'bar'") == 'bar'
    assert unquote('baz') == 'baz'
    assert unquote('"baz"') == 'baz'
    assert unquote('""') == ''
    assert unquote("''") == ''
    assert unquote('"foo\\"bar"') == 'foo\\"bar'
    assert unquote("'foo\\'bar'") == 'foo\\\'bar'
    assert unquote('"foo\\\\"bar"') == 'foo\\\\"bar'
    assert unquote('"foo\\"bar"') == 'foo\\"bar'
    assert unquote('"foo\\"bar"') == 'foo\\"bar'
    assert unquote('"foo\\\\\\"bar"') == 'foo\\\\\\"bar'

# Generated at 2022-06-13 06:56:47.565071
# Unit test for function is_quoted
def test_is_quoted():
    # Boolean Return
    assert is_quoted('"string"') is True
    assert is_quoted('foobar') is False
    # Type
    assert isinstance(is_quoted('foobar'), bool)
    # Single character
    assert is_quoted('"') is False
    assert is_quoted('') is False
    assert is_quoted('\\') is False


# Generated at 2022-06-13 06:56:52.391668
# Unit test for function is_quoted
def test_is_quoted():
    # Pass case
    assert (is_quoted("'This is a string'") == True)
    
    # Fail cases
    assert (is_quoted('This is a "normal string"') == False)
    assert (is_quoted('This is a normal string') == False)
    assert (is_quoted('This is "a normal string" with space') == False)
    assert (is_quoted('This is a normal string" with space') == False)


# Generated at 2022-06-13 06:56:58.376977
# Unit test for function unquote
def test_unquote():
    assert unquote(r'') == r''
    assert unquote(r'"') == r'"'
    assert unquote(r'"foo') == r'"foo'
    assert unquote(r"'") == r"'"
    assert unquote(r"'foo") == r"'foo"
    assert unquote(r'foo') == r'foo'
    assert unquote(r'foo"') == r'foo"'
    assert unquote(r'foo"bar"') == r'foo"bar"'
    assert unquote(r'"foo"') == r'foo'
    assert unquote(r"'foo'") == r'foo'
    assert unquote(r'"foo"bar"') == r'"foo"bar"'
    assert unquote(r'"foo"bar"baz"') == r'"foo"bar"baz"'

# Generated at 2022-06-13 06:57:02.288599
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('"abc"') == 'abc'
    assert unquote('abc') == 'abc'
    assert unquote('"a"b"') == 'a"b'

# Generated at 2022-06-13 06:57:12.452007
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello world"') == 'hello world'
    assert unquote("'hello world'") == 'hello world'
    assert unquote('hello world') == 'hello world'
    assert unquote('"hello world') == '"hello world'
    assert unquote("'hello world") == "'hello world"
    assert unquote('hello world"') == 'hello world"'
    assert unquote('hello world\'"') == 'hello world\'"'
    assert unquote(r'"hello world\"') == r'hello world\"'
    assert unquote(r'"hello\" world"') == r'hello\" world'
    assert unquote('"hello" world"') == '"hello" world"'
    assert unquote('"""hello"""') == '"""hello"""'

# Generated at 2022-06-13 06:57:23.643539
# Unit test for function unquote
def test_unquote():
    assert unquote('"abc"') == 'abc'
    assert unquote('"a\\"bc"') == 'a\\"bc'
    assert unquote("'abc'") == 'abc'
    assert unquote('"\"abc\""') == '"abc"'
    assert unquote('\'"abc"\'') == "'abc'"
    assert unquote('"abc"d') == '"abc"d'
    assert unquote('\'"abc\'') == '\'"abc\''
    assert unquote('"abc') == '"abc'
    assert unquote('abc"') == 'abc"'
    assert unquote('"abc\ndef"') == '"abc\ndef"'

# Generated at 2022-06-13 06:57:35.722508
# Unit test for function unquote
def test_unquote():
    assert unquote("'a'") == 'a'
    assert unquote('"a"') == 'a'
    assert unquote('"a\'a"') == "a'a"
    assert unquote("'a\"a'") == 'a"a'
    assert unquote("a\'a") == "a'a"
    assert unquote('a"a') == 'a"a'
    assert unquote('"a"b"') == 'a"b'
    assert unquote("'a'b'") == 'a\'b'
    assert unquote('a') == 'a'
    assert is_quoted("'a'")
    assert is_quoted('"a"')
    assert not is_quoted('"a\\"a"')
    assert not is_quoted("'a\"a'")


# Generated at 2022-06-13 06:57:41.272144
# Unit test for function unquote
def test_unquote():
    assert unquote('"test1"') == 'test1'
    assert unquote('test1') == 'test1'
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('""""') == '""'



# Generated at 2022-06-13 06:57:47.374596
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello world"') == True
    assert is_quoted('"hello world') == False
    assert is_quoted('hello world"') == False
    assert is_quoted('hello world') == False
    assert is_quoted('hello "world"') == False
