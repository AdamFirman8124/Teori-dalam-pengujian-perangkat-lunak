

# Generated at 2022-06-13 04:31:17.403113
# Unit test for function split_args

# Generated at 2022-06-13 04:31:23.466629
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 04:31:26.762821
# Unit test for function split_args
def test_split_args():
    args = 'a="b c" d=\'e f\''
    expected_result = ['a="b c"', 'd=\'e f\'']
    assert split_args(args) == expected_result

# Generated at 2022-06-13 04:31:30.748044
# Unit test for function split_args
def test_split_args():

    assert split_args('') == []

    assert split_args('"foo bar"') == ['foo bar']

    assert split_args('foo bar') == ['foo', 'bar']

    assert split_args('foo = bar') == ['foo = bar']

    assert split_args('"foo = bar"') == ['foo = bar']

    assert split_args('foo = "bar"') == ['foo = "bar"']

    assert split_args('foo=bar') == ['foo=bar']

    assert split_args('foo=1') == ['foo=1']

    assert split_args('foo="bar"') == ['foo=bar']

    assert split_args('foo=bar key="val"') == ['foo=bar', 'key=val']


# Generated at 2022-06-13 04:31:42.115757
# Unit test for function split_args
def test_split_args():
    assert split_args("foo bar") == ['foo', 'bar']
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args("foo bar baz boom") == ['foo', 'bar', 'baz', 'boom']
    assert split_args("foo=bar") == ['foo=bar']
    assert split_args("foo=bar baz=boom") == ['foo=bar', 'baz=boom']
    assert split_args("foo=\"bar baz\"") == ['foo="bar baz"']
    assert split_args("foo=\"bar baz\" boom=\"bam\"") == ['foo="bar baz"', 'boom="bam"']

# Generated at 2022-06-13 04:31:53.447057
# Unit test for function split_args

# Generated at 2022-06-13 04:32:05.313737
# Unit test for function split_args
def test_split_args():
    # Any additional testing should use the python-decouple library,
    # https://pypi.python.org/pypi/python-decouple/
    import pprint
    # These should not fail
    myargs = 'a=b c="foo bar"'
    print(pprint.pformat(split_args(myargs)))
    myargs = "a=b c='foo bar'"
    print(pprint.pformat(split_args(myargs)))
    myargs = 'a=b c="foo bar"'
    print(pprint.pformat(split_args(myargs)))
    myargs = 'a=b c="foo bar"'
    print(pprint.pformat(split_args(myargs)))
    myargs = 'a=b c="foo bar"'

# Generated at 2022-06-13 04:32:14.892442
# Unit test for function split_args
def test_split_args():
    ''' test the split_args method '''
    # examples taken from the old shlex split in shell.py

# Generated at 2022-06-13 04:32:22.138321
# Unit test for function split_args
def test_split_args():
    actual_result = split_args('a=b c="foo bar" d="foo=bar" e="foobar" f="foo"bar" g="foo\"bar"')
    expected_result = ['a=b', 'c="foo bar"', 'd="foo=bar"', 'e="foobar"', 'f="foo"bar"', 'g="foo\"bar"']
    assert expected_result == actual_result, 'Expected: %s, but got: %s' % (expected_result, actual_result)

    actual_result = split_args("a='b c' d='foo bar'")
    expected_result = ['a=\'b c\'', 'd=\'foo bar\'']

# Generated at 2022-06-13 04:32:27.119491
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello"')
    assert is_quoted("'hello'")
    assert not is_quoted('"hello')
    assert not is_quoted("'hello")
    assert not is_quoted("hello")



# Generated at 2022-06-13 04:32:45.678500
# Unit test for function split_args
def test_split_args():

    # Test all arguments with whitespace in between
    args = "one two three four"
    result = split_args(args)
    assert result == ['one', 'two', 'three', 'four']

    # Test all arguments without any whitespace
    args = "onetwothreefour"
    result = split_args(args)
    assert result == ['onetwothreefour']

    # Test all arguments with newlines in between
    args = "one\ntwo\nthree\nfour"
    result = split_args(args)
    assert result == ['one', 'two', 'three', 'four']

    # Test all arguments with both whitespace and newlines in between
    args = "one two\nthree\nfour"
    result = split_args(args)

# Generated at 2022-06-13 04:32:54.044192
# Unit test for function split_args
def test_split_args():
    '''
    Test split_args() using unittest
    '''
    import unittest
    import os

    class TestSplitArgs(unittest.TestCase):

        def setUp(self):
            self.module = os.path.join(os.path.dirname(__file__), 'dummy')

        def test_split_args(self):
            self.assertEqual(split_args('a=b c="foo bar"'), ['a=b', 'c="foo bar"'])
            self.assertEqual(split_args('type=ip filter="ip and not arp"'), ['type=ip', 'filter="ip and not arp"'])

# Generated at 2022-06-13 04:33:01.718654
# Unit test for function unquote
def test_unquote():
    assert ('foo' == unquote("foo"))
    assert ('foo' == unquote('"foo"'))
    assert ('foo' == unquote("'foo'"))
    assert ('foo "bar"' == unquote('"foo \"bar\""'))
    assert ('foo "bar"' == unquote("'foo \"bar\"'"))
    assert ('foo \'bar\'' == unquote("'foo \'bar\''"))
    assert ('foo \'bar\'' == unquote("'foo \'bar\''"))



# Generated at 2022-06-13 04:33:07.394071
# Unit test for function unquote
def test_unquote():
    assert unquote('foo') == 'foo'
    assert unquote('"foo"') == 'foo'
    assert unquote('\'foo\'') == 'foo'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"""foo"""') == '"""foo"""'
    assert unquote('\'\'\'foo\'\'\'') == '\'\'\'foo\'\'\''


# Generated at 2022-06-13 04:33:14.629293
# Unit test for function split_args

# Generated at 2022-06-13 04:33:27.381043
# Unit test for function split_args

# Generated at 2022-06-13 04:33:39.170894
# Unit test for function split_args
def test_split_args():
    test_strings = [
        ['ls', '-l'],
        ['ls -l'],
        [''],
        ['a=b c="foo bar"']
    ]

    for test in test_strings:
        result = split_args(" ".join(test))
        assert set(result) == set(test)


# Generated at 2022-06-13 04:33:51.414153
# Unit test for function split_args
def test_split_args():

    def test_split(args, expected):
        params = split_args(args)
        assert params == expected, "input: %s\nexpected: %s\ngot: %s\n" % (args, expected, params)

    test_split('', [])
    test_split(' ', [])
    test_split('\n', ['\n'])
    test_split('a', ['a'])
    test_split('a b', ['a', 'b'])
    test_split('a "b c"', ['a', '"b c"'])
    test_split('a=b c="foo bar"', ['a=b', 'c="foo bar"'])

# Generated at 2022-06-13 04:34:00.978107
# Unit test for function split_args

# Generated at 2022-06-13 04:34:10.411193
# Unit test for function split_args

# Generated at 2022-06-13 04:34:29.588727
# Unit test for function split_args

# Generated at 2022-06-13 04:34:40.098900
# Unit test for function split_args
def test_split_args():
    '''
    This function is defined here for the purposes of unit testing
    '''
    # define the tests and their expected results

# Generated at 2022-06-13 04:34:47.092263
# Unit test for function split_args

# Generated at 2022-06-13 04:34:57.275717
# Unit test for function split_args
def test_split_args():
    ''' test split_args to make sure it works as expected '''
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    class TestSplitArgs(unittest.TestCase):
        ''' unit test class for split args functionality '''
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_unquote_basic(self):
            ''' basic unquote test '''
            self.assertEqual(unquote('foo'), 'foo')
            self.assertEqual(unquote('foo bar'), 'foo bar')
            self.assertEqual(unquote('"foo"'), 'foo')
            self.assertEqual(unquote('"foo bar"'), 'foo bar')
            self.assertEqual

# Generated at 2022-06-13 04:35:07.670719
# Unit test for function split_args

# Generated at 2022-06-13 04:35:18.135367
# Unit test for function split_args

# Generated at 2022-06-13 04:35:26.234713
# Unit test for function split_args
def test_split_args():
    assert split_args('foobar') == ['foobar']
    assert split_args('"foobar"') == ['"foobar"']
    assert split_args('"foo bar"') == ['"foo bar"']
    assert split_args(u"föobar") == [u"föobar"]
    assert split_args(u"föobar") == [u"föobar"]
    assert split_args("föobar") == ["föobar"]
    assert split_args("'föo'bar") == ["'föo'bar"]
    assert split_args('"föo"bar') == ['"föo"bar']
    assert split_args("'föo'bar") == ["'föo'bar"]

# Generated at 2022-06-13 04:35:37.181927
# Unit test for function split_args
def test_split_args():
    # a helper that makes it easier to test quoting
    def test_call(s):
        return split_args(s)

    # Basic tests for quoting
    assert test_call('"a=b"') == ['a=b']
    assert test_call("'a=b'") == ['a=b']

    # Test for alternating quoting
    assert test_call("'a b'c d'e f'") == ["a b'c d'e f"]

    # Test for quoted quotes
    assert test_call("'a\\'b'") == ["a'b"]
    assert test_call("\"a\\\"b\"") == ['a"b']

    # Test for escaped backslashes
    assert test_call("'a\\\\b'") == ['a\\b']

# Generated at 2022-06-13 04:35:46.763209
# Unit test for function split_args
def test_split_args():
    # Simple case
    assert split_args('foo=bar baz="bam mam"') == ['foo=bar', 'baz="bam mam"']

    # Quotes inside jinja2
    assert split_args('foo="{% if foobar \'barbaz\' %}bar{% endif %}"') == ['foo="{% if foobar \'barbaz\' %}bar{% endif %}"']

    # Jinja2 inside quotes
    assert split_args('foo="{% if foobar %}bar{% endif %} baz"') == ['foo="{% if foobar %}bar{% endif %} baz"']

    # Line continuation
    assert split_args('foo=bar baz\nbam') == ['foo=bar', 'baz\nbam']

    # Multi lines arg in quotes
   

# Generated at 2022-06-13 04:35:55.494600
# Unit test for function split_args
def test_split_args():
    '''
    Test split_args with all of the crazy edge cases
    '''

    # this is some of the worst, most horrible python code I've ever written.
    # and I'm proud of it.
    def test(args, expected):
        actual = split_args(args)
        if actual != expected:
            print("#----------------------------\n"
                  "{0}\n"
                  "Expected:\n"
                  "{1}\n"
                  "Actual:\n"
                  "{2}\n"
                  "#----------------------------".format(args, expected, actual))
        assert actual == expected

    # basic
    test('a=b c="foo bar"', ['a=b', 'c="foo bar"'])

    # simple jinja2 blocks with spaces between

# Generated at 2022-06-13 04:36:29.257136
# Unit test for function split_args
def test_split_args():
    '''
    This method is used for unit testing the split_args() function with the
    appropriate input and output.
    '''

# Generated at 2022-06-13 04:36:35.753045
# Unit test for function split_args
def test_split_args():
    args = """a=b c="foo bar" 'd e' f='g "h i" j'"""
    params = split_args(args)
    assert params == ['a=b', 'c="foo bar"', "'d e'", 'f=\'g "h i" j\'']

    params = split_args(u"""a=b c="Привет" 'd e' f='g "h i" j'""")
    assert params == ['a=b', u'c="Привет"', "'d e'", 'f=\'g "h i" j\'']

    params = split_args(u"""a=b c="Привет" 'd e' f="g \\"h i\\" j" """)
    #print(params)
   

# Generated at 2022-06-13 04:36:46.167832
# Unit test for function split_args
def test_split_args():
    '''Test function split_args'''
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    with patch('ansible.module_utils._text.split_args') as mock:
        mock.return_value = ['token1', 'token2', 'token3']
        result = split_args('token1 token2 token3')
        assert result == ['token1', 'token2', 'token3']

        mock.return_value = ['token1', 'token2', 'token3']
        result = split_args('token1 \\\n token2 \\\n token3')
        assert result == ['token1', 'token2', 'token3']

        mock.return_value = ['token1', 'token2', 'token3']

# Generated at 2022-06-13 04:36:57.003257
# Unit test for function split_args
def test_split_args():
    # Test 1
    # Example command:
    # /usr/bin/nova --os-username=admin --os-password=admin \
    #        --os-tenant-name=admin --os-auth-url=http://127.0.0.1:5000/v2.0 image-list
    # Convert to:
    # nova image-list --os-username "admin" --os-password "admin" \
    #        --os-tenant-name "admin" --os-auth-url "http://127.0.0.1:5000/v2.0"

    args = '/usr/bin/nova --os-username=admin --os-password=admin --os-tenant-name=admin --os-auth-url=http://127.0.0.1:5000/v2.0 image-list'
    args

# Generated at 2022-06-13 04:37:02.878195
# Unit test for function split_args

# Generated at 2022-06-13 04:37:15.153463
# Unit test for function split_args
def test_split_args():
    """
    Tests for function split_args.
    These tests should fail if we change the way split_args behaves.
    """
    # tests if split_args works with base cases
    assert split_args("") == []
    assert split_args("test") == ['test']
    assert split_args("  test") == ['test']
    assert split_args("test  ") == ['test']
    assert split_args("test  test") == ['test', 'test']
    assert split_args("test=test test=test") == ['test=test', 'test=test']

    # tests if split_args works with quotes
    assert split_args("test='test test'") == ["test='test test'"]
    assert split_args("test=\"test test\"") == ["test=\"test test\""]

# Generated at 2022-06-13 04:37:24.108815
# Unit test for function split_args
def test_split_args():
    ''' test split_args function '''

    # This is a soft test, as it is impossible to ensure that
    # we're going to expect exactly what we're going to get
    # after this function is done.

    params = split_args("a=b c=\"foo bar\"")
    assert params == ['a=b', 'c="foo bar"']

    params = split_args("a=b c=\"foo \\\"bar\\\"\"")
    assert params == ['a=b', 'c="foo \\"bar\\""']

    # This doesn't always pass.  Sometimes the split occurs after the newline,
    # and sometimes it occurs before.  Either way, the end result is the same
    # and the arguments have been parsed as we would intend.
    params = split_args("a=b \\ \nc=\"foo bar\"")
   

# Generated at 2022-06-13 04:37:35.268808
# Unit test for function split_args
def test_split_args():
    # FIXME: make this a proper unit test and put it with the other modules
    from ansible.compat import shlex_split


# Generated at 2022-06-13 04:37:44.918556
# Unit test for function split_args
def test_split_args():

    assert split_args("") == []
    assert split_args("   ") == []
    assert split_args("\n") == []
    assert split_args(" \n ") == []
    assert split_args("one") == ["one"]
    assert split_args(" one ") == ["one"]
    assert split_args("one two") == ["one", "two"]
    assert split_args("one two three") == ["one", "two", "three"]
    assert split_args("one 'two' three") == ["one", "'two'", "three"]
    assert split_args("one \"two\" three") == ["one", '"two"', "three"]
    assert split_args("one 'two") == ["one", "'two"]
    assert split_args("one 'two three") == ["one", "'two three"]


# Generated at 2022-06-13 04:37:53.879788
# Unit test for function split_args
def test_split_args():
    '''
    This function unit tests the split_args function.  The goal of the function is to
    split args passed from a playbook into a list by spaces, but if the space is between
    two quotes, it is preserved.
    '''

    def run_test(args, expected, msg):
        result = split_args(args)
        if result != expected:
            raise AssertionError('\nExpected: %s\nReceived: %s\n%s' % (expected, result, msg))

    run_test('', [], 'Splitting empty string failed')
    run_test(' ', [' '], 'Splitting single space failed')
    run_test('  ', [' ', ' '], 'Splitting multiple spaces failed')
    run_test('a=b', ['a=b'], 'Splitting var assignment failed')
   

# Generated at 2022-06-13 04:38:33.085496
# Unit test for function split_args

# Generated at 2022-06-13 04:38:42.628606
# Unit test for function split_args
def test_split_args():
    '''
    This is a basic test suite for the split_args function.
    It takes no arguments and runs a few test cases,
    and if all pass, prints "Success".  If any of the tests
    fail, it prints an error message and returns 1.
    '''
    import types

    def assert_equal(a, b):
        if a != b:
            raise Exception("%s != %s" % (a, b))

    def assert_type(a, b):
        if type(a) != b:
            raise Exception("type(%s) = %s, not %s" % (a, type(a), b))

    def assert_is_list(a):
        assert_type(a, types.ListType)


# Generated at 2022-06-13 04:38:51.609848
# Unit test for function split_args

# Generated at 2022-06-13 04:39:01.668620
# Unit test for function split_args

# Generated at 2022-06-13 04:39:06.200898
# Unit test for function split_args
def test_split_args():
    '''
    these are some sample args and the expected params that should be parsed from them
    '''

# Generated at 2022-06-13 04:39:14.741369
# Unit test for function split_args

# Generated at 2022-06-13 04:39:25.539553
# Unit test for function split_args
def test_split_args():
    import sys
    fails = 0

    def assert_equal(x, y, msg=None, summary_msg=None):
        ''' assert two items are equal with an optional message, and increment the counter of test failures '''
        global fails
        if x != y:
            if msg:
                print("%s, expected: %s, got: %s" % (msg, x, y))
            elif summary_msg:
                print("%s, expected: %s, got: %s" % (summary_msg, x, y))
            else:
                print("expected: %s, got: %s" % (x, y))
            fails += 1

    def test_no_args():
        input = ""
        output = []

# Generated at 2022-06-13 04:39:33.634561
# Unit test for function split_args
def test_split_args():
    # testing with a module
    module = 'shell'
    args = dict(
        _raw_params='ls -l /tmp',
        _uses_shell=True,
    )

    # the _raw_params value is what we're testing
    # args will be used by the module, we're just verifying that
    # the _raw_params value gets split into _uses_shell, executable and _raw_params
    # correctly
    expected = dict(
        _raw_params=['ls', '-l', '/tmp'],
        _uses_shell=True,
        executable='/bin/sh',
        chdir=None,
    )

    # the split_args function will be called by the module code
    # in get_bin_path()

# Generated at 2022-06-13 04:39:40.566150
# Unit test for function split_args

# Generated at 2022-06-13 04:39:51.728514
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar" d=') == ['a=b', 'c="foo bar"', 'd=']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo', 'bar']
    assert split_args('a=b c="foo\nbar') == ['a=b', 'c="foo\nbar']
    assert split_args('a=b c="foo\\\nbar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo\nbar\nbaz"') == ['a=b', 'c="foo\nbar\nbaz"']