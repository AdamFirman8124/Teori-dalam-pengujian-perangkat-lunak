

# Generated at 2022-06-13 06:56:41.433933
# Unit test for function unquote
def test_unquote():
    data = "!vault | $ANSIBLE_VAULT;1.1;AES256"
    assert unquote(data) == data
    data = "'!vault | $ANSIBLE_VAULT;1.1;AES256'"
    assert unquote(data) == data[1:-1]
    data = '"!vault | $ANSIBLE_VAULT;1.1;AES256"'
    assert unquote(data) == data[1:-1]

# Generated at 2022-06-13 06:56:49.848259
# Unit test for function unquote

# Generated at 2022-06-13 06:56:59.928412
# Unit test for function unquote
def test_unquote():
    assert is_quoted('"a b"') == True
    assert is_quoted('\'a b\'') == True
    assert is_quoted('') == False
    assert is_quoted('"') == False
    assert is_quoted('a b') == False
    assert is_quoted('"a b') == False
    assert is_quoted('a b"') == False
    assert is_quoted('a b') == False
    assert is_quoted('"ab\'"') == False
    assert unquote('"a b"') == 'a b'
    assert unquote('\'a b\'') == 'a b'
    assert unquote('') == ''

# Generated at 2022-06-13 06:57:03.556273
# Unit test for function unquote
def test_unquote():
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo') != 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote("'foo") != 'foo'

# Generated at 2022-06-13 06:57:13.646178
# Unit test for function unquote
def test_unquote():
    assert not is_quoted('Simple string')
    assert is_quoted('"Quoted string"')
    assert is_quoted("'Quoted string'")
    assert is_quoted('"Quote (") inside"')
    assert is_quoted("'Quote (') inside'")
    assert unquote('"Quoted string"') == 'Quoted string'
    assert unquote("'Quoted string'") == 'Quoted string'
    assert unquote('"Quote (") inside"') == 'Quote (") inside'
    assert unquote("'Quote (') inside'") == "Quote (') inside"
    assert unquote('Simple string') == 'Simple string'
    assert unquote('"Quote (\\") inside"') == 'Quote (") inside'
    assert unquote('"A\\\\B"') == 'A\\B'


# Generated at 2022-06-13 06:57:28.168063
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo"foo') == '"foo"foo'
    assert unquote('foo"foo"') == 'foo"foo"'
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo"foo') == '"foo"foo'
    assert unquote('foo"foo"') == 'foo"foo"'
    assert unquote('foo') == 'foo'
    assert unquote('\'foo\'') == 'foo'
    assert unquote('\'foo\'foo') == '\'foo\'foo'
    assert unquote('foo\'foo\'') == 'foo\'foo\''
    assert unquote('foo') == 'foo'
    assert unquote('') == ''
    assert un

# Generated at 2022-06-13 06:57:31.892418
# Unit test for function unquote
def test_unquote():
  assert unquote('foo') == unquote('"foo"') == unquote("'foo'") == unquote(u'"foo"') == 'foo'
  assert unquote('"foo"bar"') == '"foo"bar"'
  assert unquote('"foobar"') == 'foobar'
  assert unquote('') == ''

# Generated at 2022-06-13 06:57:37.294974
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo')  == '"foo'
    assert unquote('foo"')  == 'foo"'
    assert unquote('"foo\"') == 'foo\"'



# Generated at 2022-06-13 06:57:50.838141
# Unit test for function unquote
def test_unquote():
    assert unquote("foo") == "foo"
    assert unquote("'foo'") == "foo"
    assert unquote("\"foo\"") == "foo"
    assert unquote("'foo\'bar'") == "foo'bar"
    assert unquote("'foo\\'bar'") == "foo\\'bar"
    assert unquote("\"foo\"bar\"") == "foo\"bar"
    assert unquote("\"foo\\\"bar\"") == "foo\\\"bar"
    assert unquote("'foo\"bar'") == "foo\"bar"
    assert unquote("\"foo'bar\"") == "foo'bar"
    assert unquote("'foo") == "'foo"
    assert unquote("\"foo") == "\"foo"

# Generated at 2022-06-13 06:57:54.382598
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"') == True
    assert is_quoted("'bar'") == True
    assert is_quoted('"baz\\""') == False
    assert is_quoted("'foo'bar'") == False
    assert is_quoted('"baz"foo') == False
    assert is_quoted('baz') == False
