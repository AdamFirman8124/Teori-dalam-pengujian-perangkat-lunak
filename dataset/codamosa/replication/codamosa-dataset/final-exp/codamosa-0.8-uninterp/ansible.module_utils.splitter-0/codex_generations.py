

# Generated at 2022-06-13 04:31:30.533367
# Unit test for function split_args

# Generated at 2022-06-13 04:31:42.079661
# Unit test for function split_args
def test_split_args():
    assert split_args("a=1 b=2") == ['a=1', 'b=2']
    assert split_args("'a=1 b=2'") == ["'a=1 b=2'"]
    assert split_args("foo bar") == ['foo', 'bar']
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args("a={{ b }} c={{ d }}") == ['a={{ b }}', 'c={{ d }}']
    assert split_args("a={{ b }} c='{{ d }}'") == ['a={{ b }}', "c='{{ d }}'"]

# Generated at 2022-06-13 04:31:53.447167
# Unit test for function split_args
def test_split_args():
    ''' unit tests split_args function against a data set of samples '''

    # read in all the samples, the first line of each sample is the args
    # string to test, the second line is the expected result
    fd = open(os.path.join(os.path.dirname(__file__), 'split_args_samples'), 'rb')
    samples = fd.read().split('\n\n')
    fd.close()

    # test each sample
    for sample in samples:
        if sample != '':
            args_test, expected = sample.split('\n')
            params_test = split_args(args_test)
            if params_test != expected:
                print("testing args: %s\n" % args_test)
                print("got %d params" % len(params_test))


# Generated at 2022-06-13 04:32:05.313665
# Unit test for function split_args
def test_split_args():
    # Test empty string
    if not split_args('') == []:
        return False

    # Test whitespaces
    if not split_args('    ') == []:
        return False

    if not split_args('  \n ') == []:
        return False

    # Test simple strings
    if not split_args('run') == ['run']:
        return False

    if not split_args('run run') == ['run', 'run']:
        return False

    # Test quoted strings
    if not split_args('"run"') == ['run']:
        return False

    if not split_args('"run run"') == ['run run']:
        return False

    if not split_args('"run run" run') == ['run run', 'run']:
        return False


# Generated at 2022-06-13 04:32:14.891331
# Unit test for function split_args

# Generated at 2022-06-13 04:32:27.119120
# Unit test for function split_args
def test_split_args():
    def check(data, expected_params):
        params = split_args(data)
        assert len(params) == len(expected_params), "split_args didn't return the correct number of params for %s" % data
        for x in range(0, len(params)):
            assert params[x] == expected_params[x], \
                "split_args didn't return the correct params for %s, element %d should be %s and got %s" % \
                (data, x, expected_params[x], params[x])

    check('foo=bar', ['foo=bar'])
    check('foo="bar baz"', ['foo="bar baz"'])

# Generated at 2022-06-13 04:32:38.645388
# Unit test for function split_args

# Generated at 2022-06-13 04:32:48.932206
# Unit test for function split_args
def test_split_args():
    '''
    make sure we are splitting args properly, with proper behavior for
    spaces inside quotes and jinja2 blocks
    '''
    def test_split(args):
        ''' helper for readable test lines '''
        return split_args(args)

    # These tests are intentionally simple and not too deep, as this function
    # is a little complex.  We should add more tests as needed, but generally
    # the expectation should be that this function behaves as well as
    # shlex.split in terms of edge cases.
    assert test_split("a=b c=d") == ['a=b', 'c=d']
    assert test_split("a=b 'foo bar'") == ['a=b', 'foo bar']
    assert test_split("a=b \"foo bar\"") == ['a=b', 'foo bar']


# Generated at 2022-06-13 04:32:55.658086
# Unit test for function split_args
def test_split_args():

    assert is_quoted("\"hello\"")
    assert is_quoted("'hello'")
    assert not is_quoted("hello")

    assert unquote("'hello'") == 'hello'
    assert unquote("\"hello\"") == 'hello'
    assert unquote("hello") == 'hello'

    assert split_args("foo") == ['foo']
    assert split_args("foo bar") == ['foo', 'bar']
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']

    assert split_args("foo='bar bar'") == ["foo='bar bar'"]
    assert split_args("foo=\"bar bar\"") == ['foo="bar bar"']
    assert split_args("foo=\"bar baz\"") == ['foo="bar baz"']


# Generated at 2022-06-13 04:33:06.408118
# Unit test for function split_args
def test_split_args():
    assert (list(split_args('a=b c="foo bar"')) == ['a=b', 'c="foo bar"'])
    assert (list(split_args('a= b c = "foo bar"')) == ['a=', 'b', 'c', '=', '"foo bar"'])
    assert (list(split_args('a=b c="foo\nbar"')) == ['a=b', 'c="foo\nbar"'])
    assert (list(split_args('a=b c="foo\\\\nbar"')) == ['a=b', 'c="foo\\\\nbar"'])
    assert (list(split_args('a=b c="foo\\nbar"')) == ['a=b', 'c="foo\\nbar"'])

# Generated at 2022-06-13 04:33:30.797172
# Unit test for function split_args
def test_split_args():
    # simple test case
    result = split_args('echo this is a test')
    assert result == ['echo', 'this', 'is', 'a', 'test']

    # test case with quotes at start and end of string
    result = split_args('"echo this is a test"')
    assert result == ['echo this is a test']

    # test case with quotes at end of string
    result = split_args('echo this is a test"')
    assert result == ['echo', 'this', 'is', 'a', 'test"']

    # test case with quotes at start of string
    result = split_args('"echo this is a test')
    assert result == ['"echo', 'this', 'is', 'a', 'test']

    # test case with quotes inside string
    result = split_args('echo "this is a test"')

# Generated at 2022-06-13 04:33:42.751752
# Unit test for function split_args
def test_split_args():
    '''
    Test suite for splitting args.
    '''

    # Basic test case 1: no args
    assert split_args('') == []

    # Basic test case 2: one arg
    assert split_args('foo') == ['foo']

    # Basic test case 3: multiple args
    assert split_args('foo,bar,baz') == ['foo', 'bar', 'baz']

    # Basic test case 4: split on space
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']

    # Jinja2 test case 1: unquoted strings should be preserved
    assert split_args('ansible_python_interpreter "{% foo %}  "') == ['ansible_python_interpreter', '"{%', 'foo', '%}', '"']

    # Jinja

# Generated at 2022-06-13 04:33:53.689163
# Unit test for function split_args
def test_split_args():
    from nose.plugins.attrib import attr
    from ansible.utils.unsafe_proxy import AnsibleUnsafe
    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):
        @attr('network')
        def test_split_args_http_header(self):
            args = "access_token={{ lookup('http', 'http://example.com', headers=dict(Authorization='Bearer {{ mytoken }}'), validate_certs=False).json.access_token }}"
            results = split_args(args)
            self.assertEqual(results, ['access_token={{ lookup(\'http\', \'http://example.com\', headers=dict(Authorization=\'Bearer {{ mytoken }}\'), validate_certs=False).json.access_token }}'])



# Generated at 2022-06-13 04:34:03.577341
# Unit test for function split_args
def test_split_args():
    # Simple cases
    assert split_args('') == ['']
    assert split_args(' ') == ['']
    assert split_args('   ') == ['']
    assert split_args('a') == ['a']
    assert split_args('   a   ') == ['a']
    assert split_args('a b') == ['a', 'b']
    assert split_args('   a   b   ') == ['a', 'b']
    assert split_args('a b ') == ['a', 'b']
    # Quoted strings
    assert split_args('"a b"') == ['a b']
    assert split_args("'a b'") == ['a b']
    assert split_args('"a b" a') == ['a b', 'a']

# Generated at 2022-06-13 04:34:05.009443
# Unit test for function split_args
def test_split_args():
     # TODO implement some test cases here
     pass


# Generated at 2022-06-13 04:34:12.590043
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils._text import to_text
    assert split_args('') == []
    assert split_args('one') == ['one']
    assert split_args('one two') == ['one', 'two']
    assert split_args('"one two"') == ['one two']
    assert split_args("'one two'") == ['one two']
    assert split_args('"one two""three four"') == ['one twothree four']
    assert split_args("'one two''three four'") == ['one twothree four']
    assert split_args('one "two three" four') == ['one', 'two three', 'four']
    assert split_args("one 'two three' four") == ['one', 'two three', 'four']
    assert split_args('"one two"" three four"')

# Generated at 2022-06-13 04:34:24.337931
# Unit test for function split_args
def test_split_args():
    import sys
    import os
    import difflib

    files = os.listdir('test/units/utils/')
    for file in files:
        if file.endswith('.orig') or file.endswith('.after'):
            with open('test/utils/' + file, 'r') as f:
                expected = f.readlines()
            with open('test/utils/' + file[:-5] + 'after', 'w') as f:
                for line in split_args(' '.join(expected)):
                    f.write('%s\n' % line)

    files = os.listdir('test/units/utils/')

# Generated at 2022-06-13 04:34:31.334999
# Unit test for function split_args

# Generated at 2022-06-13 04:34:41.444870
# Unit test for function split_args
def test_split_args():
    ''' Test to see if the split_args function works as expected '''

# Generated at 2022-06-13 04:34:47.904390
# Unit test for function split_args
def test_split_args():
    test_results = []
    test_results.append(split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'])
    test_args = ("a='b c' d='foo bar' e='1 2 3' f='1\n2\n3' g='1\\'2\\'3' h=\"foo\"bar\"\" i='1 2'3 4'5 6' j=foo\\ bar k='l m'")

# Generated at 2022-06-13 04:35:09.341670
# Unit test for function split_args

# Generated at 2022-06-13 04:35:19.469665
# Unit test for function split_args
def test_split_args():
    # These are tests for function split_args
    import sys
    import os
    import ansible.module_utils.splitter as splitter

    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = ['-a', 'foo bar', '-b=test', '-c={{foo}}', '-d="{{foo}}" bcd', '-f', '"a=b c=d"', '-g', '"a=b c={{ foo }}" d=e']

    for arg in args:
        print("arg: %s" % arg)
        params = splitter.split_args(arg)
        print("params: %s" % (params))
        print("")

# Generated at 2022-06-13 04:35:25.672738
# Unit test for function split_args
def test_split_args():
    assert split_args('') == [], 'split_args with empty string returns empty list'
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'], \
        'split_args with simple kvp returns two strings'
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'], \
        'split_args with simple kvp returns two strings'
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'], \
        'split_args with simple kvp returns two strings'
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'], \
        'split_args with simple kvp returns two strings'


# Generated at 2022-06-13 04:35:36.623461
# Unit test for function split_args
def test_split_args():

    test_arg_string = 'a=b c="foo bar"'
    arg_list = split_args(test_arg_string)

    assert arg_list == ['a=b', 'c="foo bar"']

    test_arg_string = 'c="foo\nbar"'
    arg_list = split_args(test_arg_string)

    assert arg_list == ['c="foo\nbar"']

    test_arg_string = 'c="foo\n\\\nbar"'
    arg_list = split_args(test_arg_string)

    assert arg_list == ['c="foo\nbar"']

    test_arg_string = "c='foo bar'"
    arg_list = split_args(test_arg_string)

    assert arg_list == ["c='foo bar'"]

    test_arg

# Generated at 2022-06-13 04:35:44.079482
# Unit test for function split_args
def test_split_args():
    assert split_args("foo") == ['foo']
    assert split_args("foo bar") == ['foo', 'bar']
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args("foo=bar") == ["foo=bar"]
    assert split_args("foo='bar baz'") == ["foo='bar baz'"]
    assert split_args("foo='bar baz' one=two") == ["foo='bar baz'", "one=two"]
    assert split_args("foo='bar baz' one=two three=four") == ["foo='bar baz'", "one=two", "three=four"]

# Generated at 2022-06-13 04:35:53.938735
# Unit test for function split_args
def test_split_args():
    '''
    This function tests the split_args function to ensure it works as expected
    '''

    def assert_split(input, output):
        '''
        This is a wrapper to assert that split_args works and pretty print the result
        '''
        result = split_args(input)
        assert result == output, "'%s' resulted in %s instead of %s" % (input, result, output)

    assert_split("a=b c='d e'", ['a=b', "c='d e'"])
    assert_split("a=b c={{d}}", ['a=b', 'c={{d}}'])
    assert_split("a=b c={{ d }}", ['a=b', 'c={{ d }}'])

# Generated at 2022-06-13 04:36:02.333733
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestSplitArgs(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_split_args_simple(self):
            data = "a=b c=\"foo bar\""
            result = split_args(data)
            self.assertEqual(result, ['a=b', 'c="foo bar"'])

        def test_split_args_complex(self):
            data = '''"foo bar" b="hello world" c='this is a test' 'foo'=bar'''
            result = split_args(data)

# Generated at 2022-06-13 04:36:06.648813
# Unit test for function split_args
def test_split_args():
    import ansible.module_utils.basic
    print("Running split_args tests")

# Generated at 2022-06-13 04:36:17.089502
# Unit test for function split_args
def test_split_args():
    # Test command 1
    # Input
    command = 'ntpdate ntp1.example.com'
    # Expected output
    expected = ['ntpdate', 'ntp1.example.com']
    # Actual output
    actual = split_args(command)
    # Check result
    if actual != expected:
        raise AssertionError('Actual output does not match expected output')

    # Test command 2
    # Input
    command = '''keystone user-role-add --user admin --tenant admin --role admin
    keystone user-role-add --user demo --tenant service --role Member'''
    # Expected output

# Generated at 2022-06-13 04:36:27.246585
# Unit test for function split_args
def test_split_args():
    result_list = split_args("a=b c='foo bar' d=\"{{ foo }}\"")
    assert result_list == ['a=b', "c='foo bar'", 'd="{{ foo }}"']

    result_list = split_args("a='b c='\" d=\"'{{ foo }}\"")
    assert result_list == ["a='b", "c='\"", "d=\"'{{", 'foo', '}}"']

    result_list = split_args("a={{ foo }} c='foo bar' d=\"{{ foo }}\"")
    assert result_list == ['a={{ foo }}', "c='foo bar'", 'd="{{ foo }}"']


# Generated at 2022-06-13 04:37:02.649363
# Unit test for function split_args
def test_split_args():
    args = '"foo bar" 1=2 name={{inventory_hostname}}'
    expected = ['foo bar', '1=2', 'name={{inventory_hostname}}']
    result = split_args(args)

    assert expected == result

    args = '"foo bar" 1=2 name={{inventory_hostname}} path=/foo/bar/baz'
    expected = ['foo bar', '1=2', 'name={{inventory_hostname}}', 'path=/foo/bar/baz']
    result = split_args(args)

    assert expected == result

    args = 'name={{inventory_hostname}} path=/foo/bar/baz'
    expected = ['name={{inventory_hostname}}', 'path=/foo/bar/baz']
    result = split_args(args)

    assert expected == result

# Generated at 2022-06-13 04:37:15.154068
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar" d=') == ['a=b', 'c="foo bar"', 'd=']
    assert split_args('') == []
    assert split_args('""') == ['']
    assert split_args('"" ""') == ['', '']
    assert split_args('"foo\nbar"') == ['foo\nbar']
    assert split_args('"foo\nbar" "baz"') == ['foo\nbar', 'baz']
    assert split_args('foo\nbar "baz"') == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 04:37:19.165312
# Unit test for function split_args
def test_split_args():
    # basic argument split
    assert split_args('foo=1 bar="baz foo"') == ['foo=1', 'bar=baz foo']
    # multiple jinja2 blocks
    assert split_args('foo={{1}} {{2}}') == ['foo={{1}}', '{{2}}']
    # split over newlines
    assert split_args('foo=1\nbar=2') == ['foo=1', 'bar=2']
    # quoted values
    assert split_args('foo="bar baz"\nbar="biz baz"') == ['foo=bar baz', 'bar=biz baz']
    # jinja2 blocks inside quotes
    assert split_args('foo="{{bar}}" baz') == ['foo={{bar}}', 'baz']
    # escape next character
    assert split_args

# Generated at 2022-06-13 04:37:25.875377
# Unit test for function split_args

# Generated at 2022-06-13 04:37:36.459700
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args.
    '''

    # Test a few simple cases first
    assert split_args('foo="bar" baz=') == ['foo=bar', 'baz=']
    assert split_args('foo="bar" baz="foo bar"') == ['foo=bar', 'baz=foo bar']
    assert split_args('foo="bar" baz=foo\\ bar') == ['foo=bar', 'baz=foo bar']
    assert split_args("foo=bar baz='foo bar'") == ['foo=bar', "baz=foo bar"]
    assert split_args("foo=bar baz='foo'\\''bar'") == ['foo=bar', "baz=foo'bar"]

# Generated at 2022-06-13 04:37:45.537668
# Unit test for function split_args
def test_split_args():

    print("Split args" + '-' * 50)

# Generated at 2022-06-13 04:37:54.158220
# Unit test for function split_args
def test_split_args():
    '''
    test the split_args function, which takes a string of args and then
    intelligently splits them apart while preserving quotes, jinja2
    blocks and other such things
    '''

    # empty args should return an empty list
    assert split_args("") == []

    # args without any quoting or other problems should split on whitespace
    assert split_args("a=b c=d") == ["a=b", "c=d"]

    # any characters after the first space should be preserved
    assert split_args("a=b c=d d") == ["a=b", "c=d d"]

    # quoted args should still be aggregated
    assert split_args("a=b c='d d'") == ["a=b", "c='d d'"]

    # however, quotes inside the args are ok and should not cause

# Generated at 2022-06-13 04:38:01.630689
# Unit test for function split_args
def test_split_args():

    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']

    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]

    assert split_args("a=b c=\"foo \\\"bar\\\"\"") == ['a=b', "c=\"foo \\\"bar\\\"\""]

    assert split_args("a=b c='foo \\\'bar\\\''") == ['a=b', "c='foo \\\'bar\\\''"]

    assert split_args("a=b c=\\'foo bar\\'") == ['a=b', "c=\\'foo", 'bar\\\'']


# Generated at 2022-06-13 04:38:13.580485
# Unit test for function split_args
def test_split_args():
    res = split_args("a=b c=\"foo bar\" d='foo bar' e={{ foo }}")
    assert len(res) == 5
    assert "a=b" in res
    assert "c=\"foo bar\"" in res
    assert "d='foo bar'" in res
    assert "e={{ foo }}" in res

    res = split_args("a=" * 100)
    assert len(res) == 1
    assert res[0] == "a=" * 100

    res = split_args("a=\"foo bar\"" + " " * 100 + "b=c")
    assert len(res) == 2
    assert "a=\"foo bar\"" in res
    assert "b=c" in res


# Generated at 2022-06-13 04:38:19.566602
# Unit test for function split_args

# Generated at 2022-06-13 04:39:32.625613
# Unit test for function split_args

# Generated at 2022-06-13 04:39:40.116061
# Unit test for function split_args
def test_split_args():
    # This test case is from issue #5660, comments from jimi-c
    assert split_args('vim "foo bar"') == ['vim', '"foo bar"']
    assert split_args('vim "foo bar') == ['vim', '"foo bar']

    assert split_args('vim "foo bar') == ['vim', '"foo bar']
    assert split_args("vim 'foo bar") == ['vim', "'foo bar"]
    assert split_args('vim "foo \'bar') == ['vim', '"foo \'bar']
    assert split_args('vim "foo \'bar"') == ['vim', '"foo \'bar"']

    assert split_args('vim "foo \\"bar') == ['vim', '"foo \\"bar']

# Generated at 2022-06-13 04:39:46.169179
# Unit test for function split_args
def test_split_args():

    # Simple test case
    args = "a=b 'c d'"
    assert split_args(args) == ['a=b', "'c d'"]

    # Test case with line continuation characters
    arg_string = "one \\\ntwo\\\n three\\\n   four"
    expected_result = ['one', 'two', 'three', 'four']
    assert split_args(arg_string) == expected_result

    # Test case with line continuation characters and quotes
    arg_string = "one \\\ntwo 'three\\\n   four' five"
    expected_result = ['one', 'two', "'three\\\n   four'", 'five']
    assert split_args(arg_string) == expected_result

    # Test case with backslashes and quotes

# Generated at 2022-06-13 04:39:56.106230
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    # when used as a module, this runs a unit test
    # this section checks that the args parser works
    # as expected and produces what we expect
    def _test_str(x, y):
        if not y:
            y = []
        result = split_args(x)
        assert result == y, "expected %s, got %s for test string %s" % (y, result, x)

    def _test_list(x, y):
        if not y:
            y = []
        result = split_args(' '.join(x))
        assert result == y, "expected %s, got %s for test string %s" % (y, result, x)


# Generated at 2022-06-13 04:40:04.364179
# Unit test for function split_args
def test_split_args():

    # assert basic functionality
    assert split_args("this is a test") == ['this', 'is', 'a', 'test']
    assert split_args("this 'is a' test") == ['this', "'is a'", 'test']
    assert split_args("this \"is a\" test") == ['this', '"is a"', 'test']
    assert split_args("this \\ is a test") == ['this', 'is a', 'test']

    # single jinja2 blocks
    assert split_args("this {{is}} a test") == ['this', '{{is}}', 'a', 'test']
    assert split_args("this {%is%} a test") == ['this', '{%is%}', 'a', 'test']

# Generated at 2022-06-13 04:40:11.593179
# Unit test for function split_args
def test_split_args():
    # quoting tests
    if split_args("foo=bar") != ['foo=bar']:
        raise Exception("simple args error")
    if split_args("foo='bar bar'") != ['foo=\'bar bar\'']:
        raise Exception("simple quote error")
    if split_args("foo=\"bar bar\"") != ['foo="bar bar"']:
        raise Exception("simple double quote error")
    if split_args("foo=\"bar bar\" bar=foo") != ['foo="bar bar"', 'bar=foo']:
        raise Exception("double quote with unquoted arg error")
    if split_args("foo=\"bar bar\" 'bar=foo'") != ['foo="bar bar"', "'bar=foo'"]:
        raise Exception("double quote with single quote arg error")

# Generated at 2022-06-13 04:40:21.703571
# Unit test for function split_args

# Generated at 2022-06-13 04:40:30.904281
# Unit test for function split_args
def test_split_args():
    import json

# Generated at 2022-06-13 04:40:36.177115
# Unit test for function split_args

# Generated at 2022-06-13 04:40:40.485859
# Unit test for function split_args