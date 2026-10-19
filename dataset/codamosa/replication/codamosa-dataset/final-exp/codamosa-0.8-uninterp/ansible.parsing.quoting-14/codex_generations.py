

# Generated at 2022-06-13 06:56:41.829644
# Unit test for function unquote
def test_unquote():
    '''
    Test unquote against multiple cases
    '''

    # Test string with double quotes
    assert unquote('"This is a double quoted string"') == 'This is a double quoted string'

    # Test string with single quotes
    assert unquote("'This is a single quoted string'") == "This is a single quoted string"

    # Test string with escaped quotes
    assert unquote("'This is a string with \'single quotes\' inside'") == "This is a string with 'single quotes' inside"

    # Test single length string
    assert unquote("'") == "'"

    # Test unquoted string
    assert unquote("This is an unquoted string") == "This is an unquoted string"



# Generated at 2022-06-13 06:56:47.237102
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"') == True
    assert is_quoted('"foo"bar') == False
    assert is_quoted('foo"') == False
    assert is_quoted('"foo') == False
    assert is_quoted('"foo""') == False
    assert is_quoted('"foo\"') == False
    assert is_quoted('"foo\""') == False



# Generated at 2022-06-13 06:56:54.679209
# Unit test for function unquote
def test_unquote():

    assert( unquote('') == '' )
    assert( unquote(None) == None )
    assert( unquote('a') == 'a' )
    assert( unquote('any') == 'any' )
    assert( unquote('"a"') == 'a' )
    assert( unquote('"any"') == 'any' )
    assert( unquote('"""a"""') == '"""a"""' )
    assert( unquote('"""any"""') == '"""any"""' )
    assert( unquote('"any') == '"any' )
    assert( unquote('any"') == 'any"' )
    assert( unquote('"a') == '"a' )
    assert( unquote('a"') == 'a"' )
    assert( unquote('\'a\'') == 'a' )


# Generated at 2022-06-13 06:57:00.109084
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'abc'") == True
    assert is_quoted("'abc") == False
    assert is_quoted('"abc"') == True
    assert is_quoted('"abc') == False
    assert is_quoted('"ab\'c"') == True
    assert is_quoted("'ab\"c'") == True


# Generated at 2022-06-13 06:57:10.502573
# Unit test for function unquote
def test_unquote():
    assert is_quoted("'foo'")
    assert is_quoted('"foo"')
    assert is_quoted("'foo\\'bar'")
    assert is_quoted('"foo\'"bar"')
    assert is_quoted('"foo\'bar"')
    assert is_quoted("'foo bar'")
    assert is_quoted('"foo bar"')
    assert not is_quoted("foo")
    assert not is_quoted("'foo")
    assert not is_quoted("foo'")
    assert not is_quoted("foo'bar")
    assert not is_quoted("foo\\")
    assert not is_quoted("foo'\\")
    assert not is_quoted("'\\")
    assert not is_quoted("'")

# Generated at 2022-06-13 06:57:20.459501
# Unit test for function unquote
def test_unquote():
    assert unquote('"abcdef"') == 'abcdef'
    assert unquote('"abcdef\\"') == 'abcdef"'
    assert unquote('"abcdef"\\""') == 'abcdef""'
    assert unquote('"abcdef\\\'"') == 'abcdef\''
    assert unquote('"abcdef\\\'\\""') == 'abcdef\'"'
    assert unquote('\'abcdef\'') == 'abcdef'
    assert unquote('\'abcdef\\\'') == 'abcdef\''
    assert unquote('\'abcdef\'\\""') == 'abcdef""'
    assert unquote('\'abcdef\\"\\\'') == 'abcdef"\''
    assert unquote('abcd\\"efg') == 'abcd\\"efg'

# Generated at 2022-06-13 06:57:27.486648
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('""')
    assert is_quoted("''")
    assert is_quoted('"foo"')
    assert is_quoted("'foo'")
    assert not is_quoted('"foo\'"')
    assert not is_quoted('foo')
    assert not is_quoted('""foo"')
    assert not is_quoted("''foo'")

# Generated at 2022-06-13 06:57:37.801156
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo"bar') == '"foo"bar'
    assert unquote('foo"bar') == 'foo"bar'
    assert unquote('"foo"bar"') == '"foo"bar"'
    assert unquote('"foo\"bar"') == 'foo"bar'
    assert unquote("'foo'") == 'foo'
    assert unquote("'foo'bar") == "'foo'bar"
    assert unquote("foo'bar") == "foo'bar"
    assert unquote("'foo'bar'") == "'foo'bar'"
    assert unquote("'foo\'bar'") == "foo'bar"

# Generated at 2022-06-13 06:57:45.661080
# Unit test for function unquote
def test_unquote():
    assert unquote('"Foo"') == 'Foo'
    assert unquote("'Foo'") == 'Foo'
    assert unquote('Foo') == 'Foo'
    assert unquote('"Foo\\""') == 'Foo"'
    assert unquote('"Foo\\\\"') == 'Foo\\'
    assert unquote('"Foo\\"Bar"') == 'Foo"Bar'

# Generated at 2022-06-13 06:57:50.452721
# Unit test for function unquote
def test_unquote():
    test_list = [
         ('"foo"', 'foo'),
         ("'foo'", 'foo'),
         ('"foo\\"bar"', 'foo\\"bar'),
         ("'foo\\'bar'", 'foo\\\'bar'),
         ('"foo bar"', '"foo bar"'),
         ('foo', 'foo'),
    ]

    for data, expected in test_list:
        assert unquote(data) == expected

