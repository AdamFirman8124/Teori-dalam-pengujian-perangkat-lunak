

# Generated at 2022-06-13 06:56:34.419950
# Unit test for function unquote
def test_unquote():
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote('"foo"\\"') == 'foo"\\'
    assert unquote("'foo'\\'") == "foo'\\"


# Generated at 2022-06-13 06:56:42.917965
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foobar"')
    assert is_quoted("'foobar'")
    assert is_quoted('"foo\\"bar"')  # escaped quote
    assert is_quoted("'foo\\'bar'")  # escaped quote
    assert not is_quoted('"foo"bar"')
    assert not is_quoted('\\"foobar\\"')
    assert not is_quoted('')
    assert not is_quoted('foobar')
    assert not is_quoted('"foobar')
    assert not is_quoted('foobar"')


# Generated at 2022-06-13 06:56:50.659119
# Unit test for function is_quoted
def test_is_quoted():
    # By definition if is_quoted returns true for a string, it also unquotes it
    assert is_quoted(''' "abcd" ''')
    assert is_quoted(''' 'abcd' ''')
    assert is_quoted('''  "abcd"  ''')
    assert is_quoted('''  'abcd'  ''')
    assert not is_quoted(''' abcd ''')
    assert not is_quoted(''' "abcd ''')
    assert not is_quoted(''' abcd" ''')
    assert not is_quoted(''' a"bc"d ''')


# Generated at 2022-06-13 06:56:54.386959
# Unit test for function unquote
def test_unquote():
    strings = [
            ['"foo"', "foo"],
            ['"\'"', "\""],
            ["'\"'", '"'],
            ["'\\''", "'"],
            ["'foo'", "foo"],
            ["'foo\'bar'", "foo'bar"],
            ["'bar\\''", "bar'"]
    ]
    for (test_string, expected_string) in strings:
        assert unquote(test_string) == expected_string

# Generated at 2022-06-13 06:56:59.036111
# Unit test for function unquote
def test_unquote():
    # Simple test case which checks whether function unquote is working correctly
    assert unquote('"hello"') == 'hello'
    assert unquote("'hello'") == 'hello'

    # Test case where there are quotes within the string
    assert unquote("'hel\"lo'") == 'hel"lo'


# Generated at 2022-06-13 06:57:05.563987
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("''") == True
    assert is_quoted("'foo'") == True
    assert is_quoted("'foo") == False
    assert is_quoted("foo'") == False
    assert is_quoted("'''") == False
    assert is_quoted("'foo''") == False
    assert is_quoted("'foo\\'") == True


# Generated at 2022-06-13 06:57:08.989583
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'foo'") == True
    assert is_quoted("'foo") == False
    assert is_quoted("'food'") == True
    assert is_quoted("'fo\\'od'") == False


# Generated at 2022-06-13 06:57:15.770868
# Unit test for function unquote
def test_unquote():
    assert is_quoted("'test'") == True
    assert is_quoted("'test")  == False
    assert is_quoted("test'")  == False
    assert is_quoted("\"test\"") == True
    assert is_quoted("\"test") == False
    assert is_quoted("test\"") == False
    assert unquote("'test'") == "test"
    assert unquote("\"test\"") == "test"
    assert unquote("test") == "test"
    assert unquote("\"\"test\"\"") == "\"test\""


# Generated at 2022-06-13 06:57:21.598594
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"') == True
    assert is_quoted("'foo'") == True
    assert is_quoted("\"foo\"") == True
    assert is_quoted("'foo") == False
    assert is_quoted("foo\"") == False
    assert is_quoted("foo") == False
    assert is_quoted("") == False
    assert is_quoted("'foo\\'") == False


# Generated at 2022-06-13 06:57:32.683456
# Unit test for function unquote
def test_unquote():
    from ansible.compat.tests import unittest

    class TestUnquote(unittest.TestCase):
        def test_no_quote(self):
            def _check(u):
                self.assertEqual(unquote(u), u)
                self.assertEqual(is_quoted(u), False)
            # Try a range of inputs
            for u in ['abc', 'abc"def', 'abc\'def', 'abc"def\'ghi']:
                _check(u)

        def test_simple_quote(self):
            def _check(u, e):
                self.assertEqual(unquote(u), e)
                self.assertEqual(is_quoted(u), True)
            _check('"abc"', 'abc')