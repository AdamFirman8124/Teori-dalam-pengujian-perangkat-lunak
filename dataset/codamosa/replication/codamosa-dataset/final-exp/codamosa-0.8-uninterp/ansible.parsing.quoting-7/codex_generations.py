

# Generated at 2022-06-13 06:56:41.096715
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote('"foo bar"') == 'foo bar'
    assert unquote("'foo bar'") == 'foo bar'
    assert unquote('\\"foo') == '\\"foo'
    assert unquote("\\'foo") == "\\'foo"
    assert unquote('foo') == 'foo'

    assert unquote('"foo" bar') == '"foo" bar'
    assert unquote("'foo' bar") == "'foo' bar"
    assert unquote('"foo bar" bar') == '"foo bar" bar'
    assert unquote("'foo bar' bar") == "'foo bar' bar"
    assert unquote('"foo') == '"foo'

# Generated at 2022-06-13 06:56:48.597353
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"') == True
    assert is_quoted("'foo'") == True
    assert is_quoted('"foo') == False
    assert is_quoted("'foo") == False
    assert is_quoted('foo"') == False
    assert is_quoted("foo'") == False
    assert is_quoted('"foo\'s"') == False
    assert is_quoted('"foo\\"s"') == False
    assert is_quoted('"foo\\\\"s"') == False
    assert is_quoted('"foo"s') == False


# Generated at 2022-06-13 06:56:55.659559
# Unit test for function unquote
def test_unquote():
    # Quoted string -> clean string
    string = '"Hello, World!"'
    assert unquote(string) == 'Hello, World!'
    # Quoted string with extra quotes -> clean string
    string = '"""Hello, World!"""'
    assert unquote(string) == 'Hello, World!'
    # Quoted string with extra quotes and internal quote -> clean string
    string = '"""Hello, "World"!"""'
    assert unquote(string) == 'Hello, "World"!'
    # Quoted string with spaces -> clean string
    string = "'''Hello      ,       World!'''"
    assert unquote(string) == 'Hello      ,       World!'
    # Quoted string with escaped quotes -> clean string
    string = "'Hello, \\'World\\'!'"
    assert unquote(string) == "Hello, 'World'!"

# Generated at 2022-06-13 06:57:06.804988
# Unit test for function unquote
def test_unquote():
    assert unquote('"testing"') == 'testing'
    assert unquote("'testing'") == 'testing'
    assert unquote('"testing') == '"testing'
    assert unquote("'testing") == "'testing"
    assert unquote('') == ''
    assert unquote('"testing with a \\ char"') == 'testing with a \\ char'
    assert unquote("'testing with a \\ char'") == "testing with a \\ char"
    assert unquote('"testing with a \\" double char"') == 'testing with a " double char'
    assert unquote('"testing with a \\" double char"  ') == 'testing with a " double char'
    assert unquote('"testing with a \' single char"') == 'testing with a \' single char'
    assert unquote("'testing with a \' single char'")

# Generated at 2022-06-13 06:57:11.160804
# Unit test for function unquote
def test_unquote():
    assert unquote("hello") == "hello"
    assert unquote('hello') == 'hello'
    assert unquote('"hello"') == "hello"
    assert unquote("'hello'") == "hello"
    assert unquote('"hello\\""') == '"hello"'
    assert unquote("'hello\\''") == "'hello'"

# Generated at 2022-06-13 06:57:18.469131
# Unit test for function unquote
def test_unquote():
    assert 'abc' == unquote('abc')
    assert 'abc' == unquote('"abc"')
    assert 'abc' == unquote("'abc'")
    assert 'ab"c' == unquote('ab"c')
    assert 'ab"c' == unquote('"ab\\"c"')
    assert "ab'c" == unquote("ab'c")
    assert "ab'c" == unquote("'ab\\'c'")
    assert 'ab\\"c' == unquote('ab\\"c')
    assert 'ab\\"c' == unquote('ab\\"c"')
    assert '"abc' == unquote('"abc')
    assert 'abc"' == unquote('abc"')

# Generated at 2022-06-13 06:57:20.463424
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == 'test'
    assert unquote("'test'") == 'test'


# Generated at 2022-06-13 06:57:26.002700
# Unit test for function unquote
def test_unquote():
    assert is_quoted('"""')
    assert not is_quoted('"""\'')
    assert unquote('"abc"') == 'abc'
    assert unquote('"abc') == '"abc'
    assert unquote('abc"') == 'abc"'


# Generated at 2022-06-13 06:57:35.171308
# Unit test for function unquote
def test_unquote():
    print("test unquote")
    assert(unquote('"c"') == 'c')
    assert(unquote('""') == '')
    assert(unquote('"abc') == 'abc')
    assert(unquote('abc"') == 'abc"')
    assert(unquote('"abc\\"efg"') == 'abc\\"efg')
    assert(unquote('"abc\\\'"efg"') == 'abc\\\'"efg')
    # https://github.com/ansible/ansible/issues/12809
    assert(unquote('"abc\\\\\\\\"efg"') == 'abc\\\\"efg')
    # https://github.com/ansible/ansible/issues/12809
    assert(unquote('"abc\\\'"efg"') == 'abc\\\'"efg')
   

# Generated at 2022-06-13 06:57:49.978866
# Unit test for function unquote
def test_unquote():
    assert unquote('test') == 'test'
    assert unquote('test"test') == 'test"test'
    assert unquote('test\'test') == 'test\'test'
    assert unquote('"test"') == 'test'
    assert unquote('"test')  == '"test'
    assert unquote('test"')  == 'test"'
    assert unquote('"test"test"') == 'test"test"'
    assert unquote('"test"test"test"') == 'test"test"test'
    assert unquote('"test\"test"') == 'test"test'
    assert unquote('"test\\"test"') == 'test\\"test'
    assert unquote('\'test\\\'test\'') == 'test\\\'test'