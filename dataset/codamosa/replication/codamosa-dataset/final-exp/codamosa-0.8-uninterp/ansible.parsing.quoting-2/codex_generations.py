

# Generated at 2022-06-13 06:56:41.307508
# Unit test for function unquote
def test_unquote():
    ''' return true if unquote works correctly '''
    pass_cases = [
        ('"string"', 'string'),
        ('\'string\'', 'string'),
        ('"escaped\"string"', 'escaped"string'),
        ('\'escaped\\\'string\'', 'escaped\'string'),
        ('unquoted', 'unquoted'),
        ('"doublequoteatend"', 'doublequoteatend"')
    ]
    for case in pass_cases:
        assert case[1] == unquote(case[0])

    fail_cases = [
        ('"string', 'string'),
        ('\'string', 'string'),
        ('string"', 'string"')
    ]
    for case in fail_cases:
        assert case[1] == unquote(case[0])


# Generated at 2022-06-13 06:56:46.425654
# Unit test for function unquote
def test_unquote():
    quoted=["''","''''","'abcd'","'abcd''","'abcd''efgh'",'"abcd"']
    unquoted=["","'","abcd","abcd'","abcd'efgh",'abcd']
    for q,u in zip(quoted,unquoted):
        assert unquote(q) ==u


# Generated at 2022-06-13 06:56:51.182465
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"')
    assert is_quoted("'bar'")
    assert is_quoted("'bar'")
    assert is_quoted('"foo\\"bar"')
    assert not is_quoted('"foo"bar"')
    assert not is_quoted('\\"foobar"')
    assert not is_quoted('"foobar\\"')
    assert not is_quoted('foo')


# Generated at 2022-06-13 06:56:55.521818
# Unit test for function unquote
def test_unquote():
    assert unquote('"testing"') == 'testing'
    assert unquote('"testing""') == 'testing"'
    assert unquote('testing') == 'testing'


# Generated at 2022-06-13 06:57:00.294765
# Unit test for function unquote
def test_unquote():
    assert is_quoted("'Quote'")
    assert unquote("'Quote'") == 'Quote'
    assert is_quoted('"Quote"')
    assert unquote('"Quote"') == 'Quote'

    assert not is_quoted('No Quote')
    assert unquote('No Quote') == 'No Quote'

    assert is_quoted(r'"C:\Program Files"')
    assert unquote(r'"C:\Program Files"') == r"C:\Program Files"

    assert is_quoted(r"'C:\Program Files'")
    assert unquote(r"'C:\Program Files'") == r"C:\Program Files"

    assert is_quoted(r"'no escaping \' allowed'")
    assert unquote(r"'no escaping \' allowed'") == r"no escaping \' allowed"


# Generated at 2022-06-13 06:57:03.289381
# Unit test for function unquote
def test_unquote():
    assert unquote('"testing"') == 'testing'
    assert unquote("'testing'") == 'testing'
    assert unquote("testing") == 'testing'


# Generated at 2022-06-13 06:57:07.320714
# Unit test for function unquote
def test_unquote():
    import pytest

    test_values = (
        ('foo', 'foo'),
        ('"foo"', 'foo'),
        ("'foo'", 'foo'),
        ('"foo\\"bar"', '"foo\\"bar"'),
        ('"foo"bar"', '"foo"bar"'),
        ('"foo"bar\\"', '"foo"bar\\"'),
        ('\\"foobar', '\\"foobar'),
        (r'"foo\"bar"', 'foo\"bar'),
        ("'foo'bar'", "'foo'bar'"),
        ("'foo'bar\\'", "'foo'bar\\'"),
        ("\\'foobar", "\\'foobar"),
        (r"'foo\'bar'", "foo\'bar"),
    )


# Generated at 2022-06-13 06:57:16.461750
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted('')
    assert is_quoted('"testing"')
    assert is_quoted("'testing'")
    assert  not is_quoted('unquoted')
    assert not is_quoted('"testing')
    assert not is_quoted("'testing")
    assert not is_quoted('"testing" ')
    assert not is_quoted("'testing' ")
    assert  not is_quoted('"testing\\"')
    assert  not is_quoted("'testing\\'")
    assert  not is_quoted('\\"testing')
    assert  not is_quoted("\\'testing")
    assert  not is_quoted('"testin\\\\g"')
    assert  not is_quoted("'testin\\\\g'")
    assert  not is_

# Generated at 2022-06-13 06:57:22.711675
# Unit test for function unquote
def test_unquote():
    data = ("'foo'", '"foo"', "'foo bar'", '"foo bar"', "'foo bar's", '"foo bar"s', "'foo bar\'s'", '"foo bar\"s"')
    expect = ('foo', 'foo', 'foo bar', 'foo bar', "'foo bar's", '"foo bar"s', 'foo bar\'s', 'foo bar\"s')
    for i, value in enumerate(data):
        result = unquote(value)
        assert expect[i] == result


# Generated at 2022-06-13 06:57:29.826114
# Unit test for function unquote
def test_unquote():
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('\'foo\'') == 'foo'
    assert unquote('') == ''
    assert unquote(' ') == ' '
    assert unquote('"') == '"'
    assert unquote('" "') == ' '
    assert unquote('foo"') == 'foo"'
    assert unquote('"foo') == '"foo'