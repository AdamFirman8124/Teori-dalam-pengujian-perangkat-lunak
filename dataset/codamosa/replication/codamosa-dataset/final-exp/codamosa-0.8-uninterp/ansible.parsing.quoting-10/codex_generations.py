

# Generated at 2022-06-13 06:56:37.843821
# Unit test for function is_quoted
def test_is_quoted():

    assert not is_quoted('yes')
    assert not is_quoted('')
    assert is_quoted('"test"')
    assert is_quoted('"test\\"')
    assert is_quoted('"test""')
    assert not is_quoted('"test')
    assert is_quoted("'test'")
    assert is_quoted("'test\\'")
    assert is_quoted("'test''")
    assert not is_quoted("'test")


# Unit test function unquote

# Generated at 2022-06-13 06:56:41.593704
# Unit test for function unquote
def test_unquote():
    assert unquote('"example"') == 'example'
    assert unquote('"abc\\"def"') == 'abc"def'
    assert unquote('"abc\\"def"ghi') == '"abc\\"def"ghi'
    assert unquote('example') == 'example'



# Generated at 2022-06-13 06:56:49.369013
# Unit test for function unquote
def test_unquote():
    assert unquote("'a'") == 'a'
    assert unquote('"a"') == 'a'
    assert unquote("'a\"'") == 'a"'
    assert unquote('"a\'"') == "a'"
    assert unquote("\\'a'") == "'a'"
    assert unquote('\\"a"') == '"a"'
    assert unquote("") == ""
    assert unquote("'") == "'"
    assert unquote('"') == '"'
    assert unquote("a") == "a"
    assert unquote("'a") == "'a"
    assert unquote('"a') == '"a'

# Generated at 2022-06-13 06:56:54.059854
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote('"f\\"oo"') == 'f\\"oo'
    assert unquote('foo') == 'foo'



# Generated at 2022-06-13 06:57:04.947944
# Unit test for function unquote
def test_unquote():
    assert is_quoted('"shell"')
    assert unquote('"shell"') == 'shell'
    assert unquote('"shell') == '"shell'
    assert unquote('shell"') == 'shell"'
    assert unquote('"shell') == '"shell'
    assert unquote('shell"') == 'shell"'
    assert unquote('"') == '"'
    assert unquote('""') == ''
    assert unquote('""') == ''
    assert unquote('"\'"') == '\''
    assert unquote('"\\"') == '\\'
    assert unquote('"""') == '"'
    assert unquote('"\\"\\"') == '""'
    assert unquote('" "') == ' '
    assert unquote('"\\\\"') == '\\\\'

# Generated at 2022-06-13 06:57:10.129737
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('') is False
    assert is_quoted('foo') is False
    assert is_quoted('"foo"') is True
    assert is_quoted('\'foo\'') is True
    assert is_quoted(r'"\'"') is True
    assert is_quoted(r'"\\"') is True


# Generated at 2022-06-13 06:57:20.222953
# Unit test for function unquote
def test_unquote():

    assert unquote('some string') == 'some string'
    assert unquote('"some string"') == 'some string'
    assert unquote("'some string'") == 'some string'

# Generated at 2022-06-13 06:57:29.181862
# Unit test for function is_quoted
def test_is_quoted():
    ''' test module functions: is_quoted '''
    assert is_quoted('"abc"') == True
    assert is_quoted('\'abc\'') == True
    assert is_quoted('"ab\'c"') == False
    assert is_quoted('\'ab"c\'') == False
    assert is_quoted('"ab\\"c"') == False
    assert is_quoted('\'ab\\"c\'') == False
    assert is_quoted('abc') == False


# Generated at 2022-06-13 06:57:33.344484
# Unit test for function is_quoted
def test_is_quoted():
    assert False == is_quoted('aaaaaaaaaaa')
    assert True  == is_quoted('"aaaaaaaaaaa"')
    assert False == is_quoted('"aaaaaaaaaa')
    assert False == is_quoted('"aaaaaaaaaaa"bbb')
    assert True  == is_quoted('"aaa \\ aaaa"bb')


# Generated at 2022-06-13 06:57:38.873412
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == "test"
    assert unquote('"test') == '"test'
    assert unquote('test"') == 'test"'
    assert unquote('t"e"s"t') == 't"e"s"t'

