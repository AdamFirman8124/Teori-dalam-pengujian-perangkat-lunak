

# Generated at 2022-06-13 06:56:35.267752
# Unit test for function is_quoted
def test_is_quoted():
    if not is_quoted("'unquoted string'"):
        raise AssertionError("Invalid output from is_quoted. Expected True, got False")

    if is_quoted("'unquoted 'string''"):
        raise AssertionError("Invalid output from is_quoted. Expected False, got True")



# Generated at 2022-06-13 06:56:43.882724
# Unit test for function unquote
def test_unquote():
    assert unquote("") == ""
    assert unquote("'asd'") == "asd"
    assert unquote("'asd") == "'asd"
    assert unquote("asd'") == "asd'"
    assert unquote("asd") == "asd"
    assert unquote("'asd\'asd") == "asd'asd"
    assert unquote("\"asd\"") == "asd"
    assert unquote("\"asd") == "\"asd"
    assert unquote("asd\"") == "asd\""
    assert unquote("asd") == "asd"
    assert unquote("\"asd\\\"asd") == "asd\"asd"
    assert unquote('"s")s(s"s(s\'s)s"s)s"')

# Generated at 2022-06-13 06:56:47.773248
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'
    assert unquote("hello'") == "hello'"
    assert unquote("'hello") == "'hello"
    assert unquote("'hello'world'") == "'hello'world'"

# --- end of unquote function ---

# Generated at 2022-06-13 06:56:51.719992
# Unit test for function is_quoted
def test_is_quoted():
    ''' tests for is_quoted '''
    assert(is_quoted('"foo"') == True)
    assert(is_quoted('"foo\\"') == False)
    assert(is_quoted('foo"') == False)
    assert(is_quoted('"foo') == False)
    assert(is_quoted('foo') == False)


# Generated at 2022-06-13 06:56:54.292833
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'
    assert unquote('hello') == 'hello'
    assert unquote('"hello') == '"hello'
    assert unquote("'hello") == "'hello"

# Generated at 2022-06-13 06:57:05.190565
# Unit test for function unquote
def test_unquote():
    assert unquote('"abc"') == 'abc'
    assert unquote("'abc'") == 'abc'
    assert unquote("'a\\'bc'") == "a'bc"
    assert unquote("''") == ''
    assert unquote('""') == ''
    assert unquote('"a\\"bc"') == 'a"bc'
    assert unquote('"""a"""') == '"a"'
    assert unquote("'a\\\"bc'") == 'a"bc'
    assert unquote("'a\"bc'") == 'a"bc'
    assert unquote("'abc'", "'") == 'abc'
    assert unquote("'a\\'bc'", "'") == "a'bc"
    assert unquote("''", "'") == ''

# Generated at 2022-06-13 06:57:10.556584
# Unit test for function unquote
def test_unquote():
    assert unquote('"this is a test"') == "this is a test"
    assert unquote("'this is a test'") == "this is a test"
    assert unquote('"this is a \"test"') == 'this is a "test'
    assert unquote('this is a test') == "this is a test"
    assert unquote('"this is a test') == '"this is a test'

# Generated at 2022-06-13 06:57:14.537288
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('"') == '"'
    assert unquote('foo') == 'foo'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"foo"') == 'foo'

# Generated at 2022-06-13 06:57:28.567080
# Unit test for function unquote
def test_unquote():
    assert unquote("'foo'") == "foo"
    assert unquote("'foo") == "'foo"
    assert unquote("'foo\\''") == "'foo\\''"
    assert unquote("'foo\\\\'") == "'foo\\\\'"
    assert unquote("'foo\\\\\\''") == "'foo\\\\\\''"
    assert unquote("'foo\\'") == "'foo\\'"
    assert unquote("'foo\\\\''") == "foo\\\\"
    assert unquote('"foo"') == "foo"
    assert unquote('"foo"') == "foo"
    assert unquote('"foo\\""') == '"foo\\"'
    assert unquote('"foo\\\\"') == '"foo\\\\"'
    assert unquote('"foo\\\\\\""') == '"foo\\\\\\"'

# Generated at 2022-06-13 06:57:35.203390
# Unit test for function unquote
def test_unquote():
    assert(unquote("data") == "data")
    assert(unquote("'data'") == "data")
    assert(unquote('"data"') == "data")
    assert(unquote("'quoted data'") == "quoted data")
    assert(unquote('"quoted data"') == "quoted data")

    assert(unquote('"quoted \\"data\\""') == 'quoted "data"')
    assert(unquote("'quoted \\'data\\''") == 'quoted \'data\'')