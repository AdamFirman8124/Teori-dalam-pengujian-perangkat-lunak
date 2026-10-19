

# Generated at 2022-06-13 06:56:34.113438
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('hello') is False
    assert is_quoted('') is False
    assert is_quoted('"hello"') is True
    assert is_quoted("'hello'") is True
    assert is_quoted("'hello\"") is False
    assert is_quoted('"hello\"') is False


# Generated at 2022-06-13 06:56:42.056859
# Unit test for function is_quoted
def test_is_quoted():
    test_cases = [
        ('cd', False),
        ('"cd"', True),
        ("'cd'", True),
        ('"c"d"', False),
        ('cd"', False),
        ('"cd', False),
        ('"c\\"d"', True),
    ]

    for item in test_cases:
        assert(is_quoted(item[0]) == item[1]), "Failed to verify quoted string for '{0}'".format(item[0])



# Generated at 2022-06-13 06:56:51.255780
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted('"abc')
    assert not is_quoted("'abc")
    assert not is_quoted('a"bc')
    assert not is_quoted("a'bc")
    assert not is_quoted('"ab""c')
    assert not is_quoted("'ab''c")
    assert not is_quoted('"ab"c')
    assert not is_quoted("'ab'c")
    assert not is_quoted('a"b"c')
    assert not is_quoted("a'b'c")
    assert not is_quoted('"abc"d')
    assert not is_quoted("'abc'd")
    assert not is_quoted('"abc\\"')
    assert not is_quoted("'abc\\'")

# Generated at 2022-06-13 06:56:56.871504
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"')
    assert is_quoted("'test'")
    assert not is_quoted('test')
    assert not is_quoted('"test')
    assert not is_quoted('"test\\"')
    assert is_quoted('"test\\""')

# Generated at 2022-06-13 06:57:08.702788
# Unit test for function unquote
def test_unquote():
    """Tests for unquote"""
    assert unquote('"abc"') == 'abc'
    assert unquote("'abc'") == 'abc'
    assert unquote("'a'") == "a"
    assert unquote('"a"') == "a"
    assert unquote("'\'a'") == "\'a"
    assert unquote("\"\\\"a\"") == "\"a"
    assert unquote('\'"a"') == '\'"a"'
    assert unquote('"\'a\'"') == "'a'"
    assert unquote("'\"a\"'") == '"a"'
    assert unquote("'/a/b/'") == "/a/b/"
    assert unquote("'/a/b/'") == "/a/b/"

# Generated at 2022-06-13 06:57:14.897496
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'hello'") == True
    assert is_quoted('"hello"') == True
    assert is_quoted('"hello\\""') == False
    assert is_quoted("'hello\\''") == False
    assert is_quoted("hello") == False
    assert is_quoted("") == False
    assert is_quoted("''") == False
    assert is_quoted("'") == False
    assert is_quoted("'hello") == False


# Generated at 2022-06-13 06:57:18.663960
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'s'")
    assert is_quoted("'s")==False
    assert is_quoted("s'")==False
    assert is_quoted("'s\\'")==False


# Generated at 2022-06-13 06:57:24.401761
# Unit test for function unquote
def test_unquote():
    assert unquote('abc') == 'abc'
    assert unquote('"abc"') == 'abc'
    assert unquote("'abc'") == 'abc'
    assert unquote('"a\\"bc"') == 'a\\"bc'
    assert unquote("'a\\'bc'") == "a\\'bc"
    assert unquote('"a\tbc"') == 'a\tbc'
    assert unquote("'a\tbc'") == 'a\tbc'

# Generated at 2022-06-13 06:57:32.308085
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('\'\'') == ''
    assert unquote('\'') == '\''
    assert unquote('"') == '"'
    assert unquote('"\'') == '"\''
    assert unquote('\'a\'') == 'a'
    assert unquote('"a"') == 'a'
    assert unquote('"a\'') == 'a\''
    assert unquote('\'a"') == 'a"'
    assert unquote('\'"') == '\'"'
    assert unquote('"\'') == '"\''


# Generated at 2022-06-13 06:57:39.945232
# Unit test for function unquote
def test_unquote():
    assert unquote("'foo'") == "foo"
    assert unquote('"foo"') == "foo"
    assert unquote('"foo') != "foo"
    assert unquote("'foo") != "foo"
    assert unquote('"foo\'') != "foo'"
    assert unquote("'foo\"") != 'foo"'
    assert unquote('foo') == 'foo'
