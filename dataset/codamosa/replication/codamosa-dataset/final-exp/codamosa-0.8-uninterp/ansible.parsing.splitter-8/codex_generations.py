

# Generated at 2022-06-13 07:07:48.011843
# Unit test for function split_args
def test_split_args():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_split_args()

# Generated at 2022-06-13 07:07:56.687884
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a=1') == {'a': '1'}
    assert parse_kv('a=') == {'a': ''}
    assert parse_kv(' a=b ') == {'a': 'b'}
    assert parse_kv(' a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a=b\\=c') == {'a': 'b=c'}
    assert parse_kv('a=b\\\\=c') == {'a': 'b\\=c'}

# Generated at 2022-06-13 07:08:06.797588
# Unit test for function split_args
def test_split_args():
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

# Generated at 2022-06-13 07:08:16.605805
# Unit test for function split_args
def test_split_args():
    '''
    Tests the split_args method.
    '''

    def make_quote_expr(expr):
        '''
        Encloses the expression in quotes.
        '''

        return '"{0}"'.format(expr)

    def test_split_args_template(expr, expected):
        """
        Tests the split_args method.

        This runs the test in both shown and templated form.
        """

        params = split_args(expr)
        assert params == expected, "Failed to parse '{0}'. Expected '{1}' but got '{2}'".format(expr, expected, params)

        expr = make_quote_expr(expr)
        params = split_args(expr)

# Generated at 2022-06-13 07:08:26.718196
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests.mock import patch

    with patch('ansible.parsing.dataloader.DataLoader') as mock_loader:
        mock_loader.return_value.file_exists = lambda x: True
        # No special characters
        args = join_args(split_args('hello world'))
        assert args == 'hello world'
        # Split on whitespace
        args = join_args(split_args('hello  world'))
        assert args == 'hello  world'
        # Split on whitespace, with newlines
        args = join_args(split_args('hello\nworld'))
        assert args == 'hello\nworld'
        # Split on whitespace, with newlines, and quotes
        args = join_args(split_args('hello "world dude"'))
        assert args

# Generated at 2022-06-13 07:08:37.816899
# Unit test for function split_args
def test_split_args():

    def _test(command_string, expected):
        result = split_args(command_string)
        assert result == expected

    # FIXME: also test with quotes removed and jinja2 bits templated
    #        to test the full spectrum of command line generation

    # FIXME: add tests for things like this which are invalid:
    #   {{ foo }}=bar
    #   a={{ foo }}
    #   a={{ foo }}
    _test(' ', [''])
    _test('  ', ['', ''])
    _test(' a ', ['a'])
    _test('    a ', ['a'])
    _test(' a    ', ['a'])
    _test(' a b ', ['a', 'b'])
    _test('   a b    ', ['a', 'b'])

# Generated at 2022-06-13 07:08:51.421550
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c="d e" f=g') == {u'a': u'b', u'c': u'd e', u'f': u'g'}
    assert parse_kv('a="b=c d" e=\'f g\' h=i') == {u'a': u'b=c d', u'e': u'f g', u'h': u'i'}
    assert parse_kv('a=b "c=c"') == {u'a': u'b', u'_raw_params': u'c=c'}
    assert parse_kv('a="b=c" "d=e"') == {u'a': u'b=c', u'_raw_params': u'd=e'}


# This is some code from the Python 2

# Generated at 2022-06-13 07:09:02.483110
# Unit test for function split_args
def test_split_args():
    assert split_args('{{"{{ ') == ["{{", "{ \"{{ \""]

# Generated at 2022-06-13 07:09:12.122425
# Unit test for function parse_kv
def test_parse_kv():
    # function parse_kv tests

    # Check if function parse_kv returns a dict
    assert isinstance(parse_kv(u'foo=bar'), dict)

    # Check if function parse_kv returns an empty dict
    assert isinstance(parse_kv(u'foo'), dict)

    # Check if function parse_kv returns a dict with a key when string has equal sign
    assert u'foo' in parse_kv(u'foo=bar')

    # Check if function parse_kv returns a dict with a key when string has no equal sign
    assert u'foo' in parse_kv(u'foo')

    # Check if function parse_kv returns a dict with a value when string has no equal sign
    assert u'foo' in parse_kv(u'foo')

    # Check if function parse_kv

# Generated at 2022-06-13 07:09:20.042567
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for function parse_kv.
    '''

    test1_str_in  = '''user=wesley
                uid=123
                groups=admin,users
                "password  =  LOL"
                append=yes
                '''
    test1_str_out = '''user=wesley
                uid=123
                groups=admin,users
                "password  =  LOL"
                append=yes
                '''
    test1_dict_out = {u'user': u'wesley', u'uid': u'123', u'groups': u'admin,users', u'password  =  LOL': u'', u'append': u'yes'}

# Generated at 2022-06-13 07:09:49.372236
# Unit test for function parse_kv
def test_parse_kv():
    expected = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
    args = 'k1=v1 k2="v2" k3="v3 space" k4=v4'
    assert expected == parse_kv(args)

    expected = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
    args = 'k1=v1\tk2="v2"\tk3="v3 space"\tk4=v4'
    assert expected == parse_kv(args)

    expected = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}


# Generated at 2022-06-13 07:09:58.357858
# Unit test for function split_args
def test_split_args():
    """Run tests for split_args"""
    # a complete list of coded test cases
    # each case is represented as a tuple of arguments to split_args
    # and the expected result

# Generated at 2022-06-13 07:10:06.618868
# Unit test for function split_args
def test_split_args():
    assert split_args(u"whoami") == [u"whoami"]
    assert split_args(u"whoami > /tmp/out") == [u"whoami", u">", u"/tmp/out"]
    assert split_args(u"whoami > '/tmp/out'") == [u"whoami", u">", u"'/tmp/out'"]
    assert split_args(u"whoami > \"/tmp/out\"") == [u"whoami", u">", u"\"/tmp/out\""]
    assert split_args(u"whoami | grep root | wc -l") == [u"whoami", u"|", u"grep", u"root", u"|", u"wc", u"-l"]
    assert split_args(u"whoami \\\n> /tmp/out")

# Generated at 2022-06-13 07:10:13.114924
# Unit test for function parse_kv
def test_parse_kv():
    # TODO: Data-driven / parameterized tests
    # TODO: Test various quoting scenarios
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('foo=bar baz=qux') == {u'foo': u'bar', u'baz': u'qux'}



# Generated at 2022-06-13 07:10:25.044300
# Unit test for function parse_kv

# Generated at 2022-06-13 07:10:35.293680
# Unit test for function parse_kv
def test_parse_kv():
    inp = 'a=1 b=2 c=3'
    assert parse_kv(inp) == {'a': '1', 'b': '2', 'c': '3'}
    inp = 'a=1"b=2" c=3'
    assert parse_kv(inp) == {'a': '1"b=2"', 'c': '3'}
    inp = 'a=1"b=2 c=3'
    assert parse_kv(inp) == {'a': '1"b=2', 'c': '3'}
    inp = 'a=1"b=2 c=3'

# Generated at 2022-06-13 07:10:43.293287
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a='1' b='2'") == {"a": "1", "b": "2"}
    assert parse_kv("a='1' b='2' c") == {"a": "1", "b": "2", "_raw_params": "c"}
    assert parse_kv("a='1' b='2' c='3 4'") == {"a": "1", "b": "2", "c": "3 4"}
    assert parse_kv("a='1' b='2' c=\"3 4\"") == {"a": "1", "b": "2", "c": "3 4"}

# Generated at 2022-06-13 07:10:53.594378
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('name=joe\ncolor=blue') == {'name': 'joe', 'color': 'blue'}
    assert parse_kv('name=joe color=blue') == {'name': 'joe', 'color': 'blue'}
    assert parse_kv('name=joe color=blue\nfood=sushi') == {'name': 'joe', 'color': 'blue', 'food': 'sushi'}
    assert parse_kv('name="joe" color=blue') == {'name': 'joe', 'color': 'blue'}
    assert parse_kv('name="joe johnson" color=blue') == {'name': 'joe johnson', 'color': 'blue'}

# Generated at 2022-06-13 07:10:57.586823
# Unit test for function split_args
def test_split_args():
    from ansibullbot.utils.text import split_args
    from ansibullbot.utils.extractors import is_j2_comment

# Generated at 2022-06-13 07:11:07.174904
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv("foo=") == {"foo": ""}
    assert parse_kv("foo= bar") == {"foo": "bar"}
    assert parse_kv("foo=bar x=y") == {"foo": "bar", "x": "y"}
    assert parse_kv("foo=bar x=y exec=True") == {"foo": "bar", "x": "y", "exec": "True"}
    assert parse_kv("foo=bar x=y exec=True", check_raw=True) == {"foo": "bar", "x": "y", "exec": "True"}

# Generated at 2022-06-13 07:11:20.040058
# Unit test for function split_args

# Generated at 2022-06-13 07:11:29.403853
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=2") == {'a': '1', 'b': '2'}
    assert parse_kv("a=1=2 b=2=3") == {'a': '1=2', 'b': '2=3'}
    assert parse_kv("a='1=2' b=2=3") == {'a': '1=2', 'b': '2=3'}
    assert parse_kv("a='1=2 b=2=3")['_raw_params'] == "a='1=2 b=2=3"
    assert parse_kv("a=1 b=2", check_raw=True) == {'a': '1', 'b': '2'}

# Generated at 2022-06-13 07:11:42.358119
# Unit test for function split_args
def test_split_args():
    # ansible module params are never templated, so we don't need to worry
    # about blocks
    # test empty
    assert split_args("") == []

    # test simple string
    assert split_args("a=b c=d") == [u'a=b', u'c=d']
    assert split_args("a=b c=d\ne=f") == [u'a=b c=d\ne=f']

    # test newlines
    assert split_args("a=b\n") == [u'a=b\n']
    assert split_args("a=b\ne=f") == [u'a=b\ne=f']
    assert split_args("a=b\ne=f\n") == [u'a=b\ne=f\n']
    assert split_args

# Generated at 2022-06-13 07:11:51.427925
# Unit test for function split_args
def test_split_args():
  def test_split_args(args):
    # FIXME: print_depth, block_depth, comment_depth should be zero
    params, print_depth, block_depth, comment_depth, inside_quotes = split_args(args)
    print(print_depth, block_depth, comment_depth, inside_quotes)
    return params

  def test_parse_kv(args):
    return parse_kv(args)

  # FIXME: negative tests
  # FIXME: test escapes
  # FIXME: test line continuation
  # FIXME: test {% .. %}
  # FIXME: test {# .. #}
  # FIXME: test {{ .. }}
  # FIXME: test quotes

# Generated at 2022-06-13 07:12:02.356314
# Unit test for function split_args
def test_split_args():
    # These are some tests that are really more focused on exec_command, but we need an easy place to put them
    assert split_args('a b="c c" d="e" f') == ['a', 'b="c c"', 'd="e"', 'f']
    assert split_args('a b="c d" e="f g"') == ['a', 'b="c d"', 'e="f g"']

    # if it's not balanced, it should throw an error
    try:
        split_args('a "b=c')
        assert False, "should have thrown an exception"
    except AnsibleParserError:
        pass

    # if it's not balanced, it should throw an error

# Generated at 2022-06-13 07:12:12.045813
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar one two=three four=five six') == {'foo': 'bar', '_raw_params': 'one two=three four=five six'}
    assert parse_kv('foo=bar foo=baz one two=three four=five six') == {'foo': 'baz', '_raw_params': 'one two=three four=five six'}
    assert parse_kv('foo=bar foo="baz one"') == {'foo': 'baz one'}
    assert parse_kv('foo=bar foo="baz one" bar="foo one"') == {'bar': 'foo one', 'foo': 'baz one'}

# Generated at 2022-06-13 07:12:18.479592
# Unit test for function split_args
def test_split_args():
    print("\n")
    print("TEST CASES:")

# Generated at 2022-06-13 07:12:31.673027
# Unit test for function split_args
def test_split_args():
    assert split_args("foo") == ['foo']
    assert split_args("foo=bar") == ['foo=bar']
    assert split_args("foo=\"bar zzz\"") == ['foo="bar zzz"']
    assert split_args("foo='bar zzz'") == ["foo='bar zzz'"]
    assert split_args("foo=\"bar \\\" zzz\"") == ['foo="bar \\" zzz"']
    assert split_args("foo='bar \\' zzz'") == ["foo='bar \\' zzz'"]
    assert split_args("foo=\"bar \\\\\" zzz\"") == ['foo="bar \\\\" zzz"']
    assert split_args("foo='bar \\\' zzz'") == ["foo='bar \\\' zzz'"]

# Generated at 2022-06-13 07:12:45.907891
# Unit test for function split_args
def test_split_args():
    ''' Test case for split_args() '''

    # Test 1. Set up four different args.
    args1 = 'a=b c="foo bar"'
    # Expected output: ['a=b', 'c="foo bar"']
    args2 = 'a=b c="foo bar" d="{{a" e=\'{{a}}\''
    # Expected output: ['a=b', 'c="foo bar"', 'd="{{a"', "e='{{a}}'"]
    args3 = 'a=b c="foo bar" d="{{a" e=\'{{a}}\' f={{a}} g=\'{{a}\''
    # Expected output: ['a=b', 'c="foo bar"', 'd="{{a"', "e='{{a}}'", 'f={{a}}', "g

# Generated at 2022-06-13 07:12:54.743370
# Unit test for function split_args
def test_split_args():
    # Empty args
    assert join_args(split_args("")) == ""

    # Args with basic whitespace splitting
    assert join_args(split_args(" ")) == " "
    assert join_args(split_args("  ")) == "  "
    assert join_args(split_args("\n")) == "\n"
    assert join_args(split_args("\n\n")) == "\n\n"
    assert join_args(split_args("foo bar baz")) == "foo bar baz"
    assert join_args(split_args("foo\nbar\nbaz")) == "foo\nbar\nbaz"
    assert join_args(split_args("foo\rbar\r\nbaz")) == "foo\rbar\r\nbaz"

# Generated at 2022-06-13 07:13:19.393194
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:26.270353
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test to confirm the shell argument parsing is working
    '''

    class TestData(object):
        pass

    # create a test data object and fill with some data
    data = TestData()
    data.test_set = {}

    # define the test cases for this unit test
    data.test_set['simple_cmd'] = dict(source_string=u"ls -ld /tmp/foo",
                                       expected_result={
                                           'cmd': 'ls -ld /tmp/foo',
                                           '_raw_params': 'ls -ld /tmp/foo',
                                       })

# Generated at 2022-06-13 07:13:36.101087
# Unit test for function split_args
def test_split_args():
    import unittest

    class KVParserTestCase(unittest.TestCase):
        ''' unit test for parsing kv strings '''

        def test_nones(self):
            opts = parse_kv(None)
            self.assertTrue(len(opts) == 0)

        def test_normal(self):
            opts = parse_kv('foo=bar key="another value"')
            self.assertTrue('foo' in opts)
            self.assertTrue(opts['foo'] == 'bar')
            self.assertTrue('key' in opts)
            self.assertTrue(opts['key'] == 'another value')

        def test_junk(self):
            opts = parse_kv('bar')
            self.assertTrue('_raw_params' in opts)
            self

# Generated at 2022-06-13 07:13:41.539178
# Unit test for function split_args
def test_split_args():
    '''
    Tests for split_args
    '''

    # Test parsing an empty string
    data = {}
    data['input'] = ''
    data['expect'] = []
    yield check_split_args, data, 'Empty string'

    # test a simple unquoted string
    data = {}
    data['input'] = 'foo bar baz'
    data['expect'] = ['foo', 'bar', 'baz']
    yield check_split_args, data, 'Unquoted string'

    # test a simple quoted string
    data = {}
    data['input'] = '"foo bar"'
    data['expect'] = ['foo bar']
    yield check_split_args, data, 'Quoted string'

    # test a string with an escaped quote
    data = {}

# Generated at 2022-06-13 07:13:50.807418
# Unit test for function split_args
def test_split_args():

    def assert_split_args(input_string, expected):
        actual = split_args(input_string)
        assert expected == actual, "Expected: {0}, Actual: {1} (Input: {2})".format(expected, actual, input_string)

    assert_split_args("\"a\" 'b' cd", ["\"a\"", "'b'", "cd"])
    assert_split_args("a=b c=\"foo bar\"", ["a=b", "c=\"foo bar\""])
    assert_split_args("a='b \"c' d=\"e f\"", ["a='b \"c'", "d=\"e f\""])
    assert_split_args("a='b \"c' d='e f'", ["a='b \"c'", "d='e f'"])
    assert_split_

# Generated at 2022-06-13 07:14:05.194194
# Unit test for function split_args
def test_split_args():
    assert split_args("") == []
    assert split_args("one two") == ["one", "two"]
    assert split_args("one\ntwo") == ["one\n", "two"]
    assert split_args("one two\nthree") == ["one", "two\n", "three"]
    assert split_args("'one two'") == ["'one two'"]
    assert split_args("'one two' three") == ["'one two'", "three"]
    assert split_args("'one two'\nthree") == ["'one two'\n", "three"]
    assert split_args('"one two"') == ['"one two"']
    assert split_args('"one two" three') == ['"one two"', "three"]

# Generated at 2022-06-13 07:14:11.115290
# Unit test for function split_args
def test_split_args():
    import ansible.module_utils.common._collections_compat as collections  # noqa

    # tests is a dict of dicts keyed by the input arg with each value being the expected output

# Generated at 2022-06-13 07:14:25.651283
# Unit test for function split_args
def test_split_args():
    # Assert that strings with no problematic patterns return an identical list
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Multiple values for the same key
    assert split_args('a=b a=c') == ['a=b', 'a=c']

    # Simple block
    assert split_args('a=b c={{foo}} d=e') == ['a=b', 'c={{foo}}', 'd=e']

    # Nested quotes
    assert split_args('a=b c=\'{{foo}}\'') == ['a=b', 'c=\'{{foo}}\'']
    assert split_args('a=b c="{{foo}}"') == ['a=b', 'c="{{foo}}"']

# Generated at 2022-06-13 07:14:36.420910
# Unit test for function parse_kv
def test_parse_kv():

    # Tests for parse_kv with check_raw set to false
    assert parse_kv("path=/foo creates=/tmp/foo1") == {'path': '/foo', u'creates': u'/tmp/foo1'}
    assert parse_kv("path=/foo creates=/tmp/foo1") != {'path': '/foo', u'_raw_params': u'creates=/tmp/foo1'}
    assert parse_kv("path=/foo creates=/tmp/foo1") != {'path': '/foo', u'_raw_params': u'path=/foo creates=/tmp/foo1'}
    assert parse_kv("path=/foo creates=/tmp/foo1") != {'path': '/foo', u'creates': u'/tmp/foo1', u'_raw_params': u''}

    # Tests for parse_

# Generated at 2022-06-13 07:14:44.224502
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a=b\\ c=d') == {'a': 'b c=d'}
    assert parse_kv('a=b\\=c') == {'a': 'b=c'}
    assert parse_kv('a=b\\ c') == {'a': 'b c'}
    assert parse_kv('a="b\\ c"') == {'a': 'b\\ c'}
    assert parse_kv('a="b c"') == {'a': 'b c'}

# Generated at 2022-06-13 07:15:03.071411
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b=2 c=3') == dict(a='1', b='2', c='3')
    assert parse_kv('a=1 b=2 c=3 d') == dict(a='1', b='2', c='3', _raw_params='d')
    assert parse_kv('a=1 b=2 c=3 "d e"') == dict(a='1', b='2', c='3', _raw_params='"d e"')
    assert parse_kv('a=1 b=2 c=3 d\\ e') == dict(a='1', b='2', c='3', _raw_params='d e')

# Generated at 2022-06-13 07:15:12.081634
# Unit test for function split_args

# Generated at 2022-06-13 07:15:13.386078
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=2 c=3") == {'a': '1', 'c': '3', 'b': '2'}



# Generated at 2022-06-13 07:15:19.511215
# Unit test for function split_args
def test_split_args():
    args = 'a=b c="foo bar"'
    expected = ['a=b', 'c="foo bar"']
    result = split_args(args)
    assert result == expected, "%s != %s" % (result, expected)

    args = "a=b c='foo bar'"
    expected = ['a=b', "c='foo bar'"]
    result = split_args(args)
    assert result == expected

    args = "a=b quux='foo bar' c='foo bar'"
    expected = ['a=b', 'quux=\'foo bar\'', "c='foo bar'"]
    result = split_args(args)
    assert result == expected

    args = "a=b quux=\"foo bar\" c='foo bar'"

# Generated at 2022-06-13 07:15:28.991192
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b='1 2' c='1\"2' d=\"1'2\"") == dict(a='1', b='1 2', c='1"2', d="1'2")
    assert parse_kv("a=1 b='1 2' c='1\"2' d=\"1'2\"", check_raw=True) == dict(a='1', b='1 2', c='1"2', d="1'2", _raw_params=["a=1", "b='1 2'",  "c='1\\\"2'", "d=\"1'2\\\""])

# Generated at 2022-06-13 07:15:39.219485
# Unit test for function parse_kv
def test_parse_kv():
    # Test for simple parsing
    example = "key=value"
    expected_output = {'key': 'value'}
    assert parse_kv(example) == expected_output

    # Make sure items are properly unquoted
    example = "key=\"quoted value\""
    expected_output = {'key': 'quoted value'}
    assert parse_kv(example) == expected_output

    # Test for combining single quoted and double quoted items
    example = 'key="foo bar" key2=\'this is a test\' key3="some \'quoted\' text" key4=\'for "testing"'

# Generated at 2022-06-13 07:15:45.729724
# Unit test for function split_args
def test_split_args():
    # Test basic whitepace splitting behavior
    assert split_args('a b c') == ['a', 'b', 'c']
    assert split_args('a b "c d"') == ['a', 'b', 'c d']
    assert split_args('a b = c d') == ['a', 'b = c d']

    # Test that newlines are respected
    assert split_args('a\nb') == ['a\n', 'b']

    # Test that escaping is respected
    assert split_args('a b\\ c') == ['a', 'b c']

    # Test that unbalanced quotes do not split
    assert split_args('a"b') == ['a"b']

    # Test quote splitting
    assert split_args('a "b c"') == ['a', 'b c']

# Generated at 2022-06-13 07:16:00.416776
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:11.147981
# Unit test for function parse_kv
def test_parse_kv():
    result = parse_kv('arg1=foo arg2=bar')
    assert result == {'arg1': 'foo', 'arg2': 'bar'}

    result = parse_kv('arg1=foo arg2=bar arg3')
    assert result == {'arg1': 'foo', 'arg2': 'bar', '_raw_params': 'arg3'}

    result = parse_kv('arg1=foo arg2=bar arg3', check_raw=False)
    assert result == {'arg1': 'foo', 'arg2': 'bar'}

    result = parse_kv('arg1=foo "arg2=bar with spaces" arg3')
    assert result == {'arg1': 'foo', 'arg2': 'bar with spaces', '_raw_params': 'arg3'}

    result = parse_

# Generated at 2022-06-13 07:16:17.194367
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('foo=bar baz=bat') == {u'foo': u'bar', u'baz': u'bat'}
    assert parse_kv('foo  =  bar  baz  =  bat') == {u'foo': u'bar', u'baz': u'bat'}
    assert parse_kv('foo=bar\nbaz=bat') == {u'foo': u'bar baz=bat'}

# Generated at 2022-06-13 07:16:37.681796
# Unit test for function split_args
def test_split_args():

    assert(
        split_args("a=b c='foo bar' d='food \"bar\"' e=\"foo 'bar'\" f=\\")
        == ['a=b', "c='foo bar'", 'd=\'food "bar"\'', 'e="foo \'bar\'"', 'f=\\']
    )
    assert(
        split_args("a='b c' d='foo bar' e='food \"bar\"' f=\"foo \"\"bar\"\"\" g=\"foo 'bar'\" h=\\")
        == ['a=\'b c\'', "d='foo bar'", 'e=\'food "bar"\'', 'f="foo """bar""""', 'g="foo \'bar\'"', 'h=\\']
    )

# Generated at 2022-06-13 07:16:51.154426
# Unit test for function parse_kv
def test_parse_kv():
    data = u'foo=bar baz="qux test" a="1 2 3" b="a=b" c="a=b c=d"'
    parsed_kv = parse_kv(data)
    assert parsed_kv.get(u"foo") == u"bar"
    assert parsed_kv.get(u"baz") == u"qux test"
    assert parsed_kv.get(u"a") == u"1 2 3"
    assert parsed_kv.get(u"b") == u"a=b"
    assert parsed_kv.get(u"c") == u"a=b c=d"
    assert parsed_kv.get(u"_raw_params") is None

    parsed_kv = parse_kv(data, check_raw=True)

# Generated at 2022-06-13 07:16:58.143734
# Unit test for function split_args
def test_split_args():
    assert split_args('foo {{bar}} baz') == ['foo', '{{', 'bar', '}}', 'baz']
    assert split_args('foo {{bar\n baz') == ['foo', '{{', 'bar\n', 'baz']
    assert split_args('foo "{{ bar }}" baz') == ['foo', '"{{', 'bar', '}}"', 'baz']
    assert split_args('foo "{{ bar"\n baz') == ['foo', '"{{', 'bar"\n', 'baz']
    assert split_args('foo "{{ bar \'baz\' }}" quux') == ['foo', '"{{', 'bar', "'baz'", '}}"', 'quux']