

# Generated at 2022-06-13 06:56:39.022015
# Unit test for function unquote
def test_unquote():
    assert is_quoted('"testing"')
    assert is_quoted("'testing'")
    assert not is_quoted("'testing")
    assert not is_quoted("testing'")
    assert not is_quoted('"testing')
    assert not is_quoted("testing")

    assert unquote('"testing"') == "testing"
    assert unquote("'testing'") == "testing"
    assert unquote("'testing") == "'testing"
    assert unquote("testing'") == "testing'"
    assert unquote('"testing') == '"testing'
    assert unquote("testing") == "testing"

# Generated at 2022-06-13 06:56:43.429136
# Unit test for function unquote
def test_unquote():
    """
    Test that the unquote function works as expected, but with
    different types of string.
    """
    assert unquote("'test'") == 'test'
    assert unquote("''test'") == "''test'"

# Generated at 2022-06-13 06:56:46.301540
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote('\'foo\'') == 'foo'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'


# Generated at 2022-06-13 06:56:50.429027
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"testing"')
    assert not is_quoted('testing"')
    assert not is_quoted('"testing')
    assert not is_quoted('"testing\'')
    assert not is_quoted('\'testing"')
    assert is_quoted('"testing"')
    assert not is_quoted('"testing\\""')


# Generated at 2022-06-13 06:56:53.775548
# Unit test for function unquote
def test_unquote():
    tests = {
        '': '',
        '"': '"',
        '""': '',
        '"a': 'a',
        'a"': 'a',
        '"a"': 'a',
        '"\\"': '"',
        '"\"a"': '"a'
    }

    for test in tests:
        assert unquote(test) == tests[test]


# Generated at 2022-06-13 06:56:56.090396
# Unit test for function unquote
def test_unquote():
    assert unquote('foobar') == 'foobar'
    assert unquote('"foobar"') == 'foobar'
    assert unquote('\'foobar\'') == 'foobar'
    assert unquote('\\"foobar') == '\\"foobar'

# Generated at 2022-06-13 06:57:05.136622
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'
    assert unquote('"hello" world') == '"hello" world'
    assert unquote('hello"') == 'hello"'
    assert unquote('"hello') == '"hello'
    assert unquote('hello') == 'hello'
    assert unquote('hel\'lo') == 'hel\'lo'
    assert unquote('hel"lo') == 'hel"lo'
    assert unquote('hel\\"lo') == 'hel\\"lo'
    assert unquote('hel\\\\"lo') == 'hel\\\\"lo'

# Generated at 2022-06-13 06:57:15.010741
# Unit test for function is_quoted
def test_is_quoted():
    '''
        test_is_quoted: unit test for is_quoted
        If this fails, then you must fix    is_quoted    above.
    '''
    tests_that_should_be_quoted = [
        '""',
        '"a"',
        '"\\"',
        '"\\\\"',
        '"hi"',
        "'hi'",
        '"\\"hi\\""',
        "'\\'hi\\''",
    ]
    tests_that_should_not_be_quoted = [
        '"',
        "'",
        'a',
        '"hi',
        "'hi",
        'hi"',
        'hi"',
        '\"',
        '\\"',
    ]

# Generated at 2022-06-13 06:57:20.911028
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == 'test'
    assert unquote('"test') == '"test'
    assert unquote('test') == 'test'
    assert unquote('"test\\""') == '"test\\""'
    assert unquote('\\"test\\"') == '\\"test\\"'
    assert unquote('') == ''
    print('unquote PASSED')


# Generated at 2022-06-13 06:57:25.476180
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == 'test'
    assert unquote("'test'") == 'test'
    assert unquote("'test") == "'test"
    assert unquote("test'") == "test'"