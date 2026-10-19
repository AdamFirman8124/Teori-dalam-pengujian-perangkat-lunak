

# Generated at 2022-06-13 07:07:40.840161
# Unit test for function split_args
def test_split_args():
    '''
    Test the split_args function against various input values.
    '''

    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 07:07:46.537274
# Unit test for function split_args

# Generated at 2022-06-13 07:07:55.975166
# Unit test for function split_args
def test_split_args():
    import os
    import glob

    test_file_base_abs_path = os.path.join(os.path.dirname(__file__), "test_split_args_test_files")
    test_file_base_path = os.path.relpath(test_file_base_abs_path)

    for test_file_name in glob.glob(os.path.join(test_file_base_path, "*.txt")):
        base_name = os.path.basename(test_file_name)

        test_file = open(test_file_name)
        test_data = to_text(test_file.read())
        test_file.close()

        test_data = to_text(test_data)


# Generated at 2022-06-13 07:08:03.573928
# Unit test for function parse_kv
def test_parse_kv():
    f = parse_kv
    # This function is just a wrapper around split_args, so we already tested
    # most of its functionality in test_split_args.
    #
    # This test only needs to verify that the resulting dict has its
    # keys/values properly unquoted, and its raw params properly recombined
    # into a single string

    # Some basically valid things

    # Simple boolean values
    assert f('a=1 b=no c=on d=true e=false f=yes g=y h=n') == {u'a': u'1', u'b': u'no', u'c': u'on', u'd': u'true', u'e': u'false', u'f': u'yes', u'g': u'y', u'h': u'n'}

    # Integers and floats


# Generated at 2022-06-13 07:08:12.028726
# Unit test for function split_args

# Generated at 2022-06-13 07:08:16.643344
# Unit test for function split_args
def test_split_args():
    """
    Test the split_args() function by providing input strings and checking the output.
    The output is checked against the expected output.
    """


# Generated at 2022-06-13 07:08:26.748461
# Unit test for function split_args
def test_split_args():
    import pytest

    # We can't use the testinfra fixtures, because the module itself is being tested.
    # So we use pytest.fixture instead.
    @pytest.fixture(scope='module')
    def fixture_ansible_module(tmp_path_factory):
        '''
        Empty AnsibleModule for AnsibleModule usage.
        '''
        from ansible.module_utils.basic import AnsibleModule

        path = str(tmp_path_factory.mktemp('data'))
        # The spec for AnsibleModule is a bit weird: it must be defined with ''.
        args = ''
        # For this test, fake the basic params using tmp_path_factory.mktemp().
        # This API is part of the testinfra fixtures.

# Generated at 2022-06-13 07:08:37.848228
# Unit test for function parse_kv
def test_parse_kv():
    kv = parse_kv('a=foo b="bar" c="{{test}}" d="baz"')
    assert kv == {u'a': u'foo', u'b': u'bar', u'c': u'{{test}}', u'd': u'baz'}
    kv = parse_kv('a=foo b= bar c="{{test}}" d= baz')
    assert kv == {u'a': u'foo', u'b': u'bar', u'c': u'{{test}}', u'd': u'baz'}
    kv = parse_kv('a=foo b= bar c="{{test}}" d= baz', check_raw=True)

# Generated at 2022-06-13 07:08:48.408779
# Unit test for function split_args

# Generated at 2022-06-13 07:09:00.113802
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a=b c=d" e=f') == {'a': 'b', 'c': 'd" e=f'}
    assert parse_kv('''a=b "a=b" a='b' "a=b"''') == {'a': 'b', 'a': 'b', 'a': 'b', 'a': 'b'}

# Generated at 2022-06-13 07:09:38.038593
# Unit test for function parse_kv
def test_parse_kv():
    assert {} == parse_kv('')
    assert {'a': 'b'} == parse_kv('a=b')
    assert {'a': 'b', 'c': 'd'} == parse_kv('  a     =     b  , c   = d')
    assert {'a': 'b', 'c': 'd'} == parse_kv('a=b,c=d')
    assert {'a': 'b', '_raw_params': 'c=d,e=f'} == parse_kv('a=b,c=d,e=f')

    assert {'a': 'b', 'c': 'd'} == parse_kv('a=b,c=d', True)

# Generated at 2022-06-13 07:09:49.401541
# Unit test for function split_args

# Generated at 2022-06-13 07:09:58.147635
# Unit test for function split_args
def test_split_args():
    assert split_args(u'a=b c="foo bar"') == [u'a=b', u'c="foo bar"']
    assert split_args(u'a=b c="foo bar"\nd=e f="g h"') == [u'a=b', u'c="foo bar"\nd=e', u'f="g h"']
    assert split_args(u"a b='c d' e='{f: g, h: i} j'") == [u'a', u"b='c d'", u"e='{f: g, h: i} j'"]
    assert split_args(u"key=value \\\nk2=v2") == [u'key=value', u'k2=v2']


# Generated at 2022-06-13 07:10:06.449540
# Unit test for function parse_kv

# Generated at 2022-06-13 07:10:20.154839
# Unit test for function split_args
def test_split_args():
    '''
    This is not a true unit test, since it is not self-contained,
    but a basic test of functionality is available here.

    to run:
    python -c "from utils.module_docs_fragments import *; test_split_args()"
    '''


# Generated at 2022-06-13 07:10:26.993616
# Unit test for function parse_kv
def test_parse_kv():
    # Test parse_kv function
    my_args = "k1=v1 \"k2 = v2\" 'k3 =v3'"
    my_result = parse_kv(my_args)
    assert my_result == dict(k1='v1', k2='v2', k3='v3')



# Generated at 2022-06-13 07:10:36.213308
# Unit test for function split_args
def test_split_args():
    input = '"foo" "foo bar"'
    output = ['foo', 'foo bar']
    assert split_args(input) == output

    input = 'foo bar baz=qux'
    output = ['foo', 'bar', 'baz=qux']
    assert split_args(input) == output

    input = 'foo bar baz="qux spider"'
    output = ['foo', 'bar', 'baz="qux spider"']
    assert split_args(input) == output

    input = 'foo bar baz="qux spider'
    output = ['foo', 'bar', 'baz="qux', 'spider']
    assert split_args(input) == output

    input = 'foo bar baz=\\"qux spider\\"'

# Generated at 2022-06-13 07:10:43.761118
# Unit test for function split_args

# Generated at 2022-06-13 07:10:53.918721
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"name=value") == {"name": "value"}
    assert parse_kv(u"name=value spaces=none") == {"name": "value", "spaces": "none"}
    assert parse_kv(u"name=value spaces=all") == {"name": "value", "spaces": "all"}
    assert parse_kv(u"name=value spaces=some spaces in value") == {"name": "value", "spaces": "some spaces in value"}
    assert parse_kv(u"name=value spaces='some spaces in value'") == {"name": "value", "spaces": "some spaces in value"}
    assert parse_kv(u"name=value spaces=\"some spaces in value\"") == {"name": "value", "spaces": "some spaces in value"}
    assert parse

# Generated at 2022-06-13 07:10:54.875550
# Unit test for function split_args
def test_split_args():
    # FIXME: Remove this comment when this function is unit tested.
    pass

# Generated at 2022-06-13 07:11:18.359836
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv(u'a=b') == {'a': 'b'}
    assert parse_kv('a="b c"') == {'a': 'b c'}
    assert parse_kv(u'a="b c"') == {'a': 'b c'}
    assert parse_kv('a="b=c"') == {'a': 'b=c'}
    assert parse_kv(u'a="b=c"') == {'a': 'b=c'}
    assert parse_kv('a="b=c d"') == {'a': 'b=c d'}

# Generated at 2022-06-13 07:11:23.242266
# Unit test for function split_args
def test_split_args():
    def assert_split(args, expected):
        """Assert that args is split into the tokens in expected."""
        assert split_args(args) == expected

    assert_split("'a \" b c'", ["'a \" b c'"])
    assert_split("'a \" b c' 'd e f'", ["'a \" b c'", "'d e f'"])
    assert_split("'a \" b c' 'd e f' g h i", ["'a \" b c'", "'d e f'", "g", "h", "i"])
    assert_split("'a \" b c'\n'd e f' g h i", ["'a \" b c'\n'd e f'", "g", "h", "i"])

# Generated at 2022-06-13 07:11:37.081599
# Unit test for function split_args
def test_split_args():
    # Basic test
    assert split_args('one') == ['one']
    # Test with whitespace
    assert split_args('one two') == ['one', 'two']
    # Basic test with a quoted string
    assert split_args('one "two"') == ['one', '"two"']
    # Test with various characters
    assert split_args('one "t\u00F6\u0308\u0300o t\u00FC\u0308"') == ['one', '"t\u00F6\u0308\u0300o t\u00FC\u0308"']
    # Test with nested quoting
    assert split_args('one "t\\"wo"') == ['one', '"t\\"wo"']
    # Test with nested quoting and continuing

# Generated at 2022-06-13 07:11:47.787882
# Unit test for function parse_kv
def test_parse_kv():
    # Test 1
    test_data = 'creates=/root/test_file warn=yes executable=/bin/bash'
    assert parse_kv(test_data, check_raw=True) == {'creates': '/root/test_file', 'warn': 'yes', 'executable': '/bin/bash'}
    # Test 2
    test_data = 'creates=/root/test_file warn=yes executable=/bin/bash'
    assert parse_kv(test_data, check_raw=False) == {'executable': '/bin/bash', 'creates': '/root/test_file', 'warn': 'yes'}
    # Test 3
    test_data = 'creates=/root/test_file warn=yes _raw_params="some raw params"'

# Generated at 2022-06-13 07:11:51.729736
# Unit test for function parse_kv
def test_parse_kv():
    kv_input = '''
    docker_extra_args="--log-opt max-size=10m --log-opt max-file=3"
    '''
    kv_output = parse_kv(kv_input)
    assert kv_output == {u'docker_extra_args': u'--log-opt max-size=10m --log-opt max-file=3'}

# Generated at 2022-06-13 07:12:02.391630
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('name=test arg="a 1"') == {u'name': u'test', u'arg': u'a 1'}
    assert parse_kv('name=test arg="a 1"', check_raw=True) == {u'name': u'test', u'arg': u'a 1', u'_raw_params': u'"a 1"'}
    assert parse_kv('name=test arg="a \'1\'" b=test') == {u'name': u'test', u'arg': u"a '1'", u'b': u'test'}

# Generated at 2022-06-13 07:12:10.112738
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a') == ['a']
    assert split_args('/some/path/to/something') == ['/some/path/to/something']
    assert split_args('/some/path/to/something --opt1 --opt2') == ['/some/path/to/something --opt1 --opt2']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a="b c"') == ['a="b c"']

# Generated at 2022-06-13 07:12:17.618301
# Unit test for function split_args

# Generated at 2022-06-13 07:12:23.590139
# Unit test for function parse_kv
def test_parse_kv():
    dict = {
        'arg1': u'val1',
        'arg2': u'val2',
        '_raw_params': u'arg3 arg4 arg5',
    }
    assert dict == parse_kv('arg1=val1 arg2=val2 arg3 arg4 arg5', check_raw=True)

# Generated at 2022-06-13 07:12:34.310841
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:57.369009
# Unit test for function split_args
def test_split_args():
    error_msg = "Expected '{0}', but got '{1}' instead"

    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"'], "Expected ['a=b', 'c=\"foo bar\"'], but got {0} instead".format(split_args("a=b c=\"foo bar\""))
    assert split_args("a=b c=\"foo bar\" 'd e'") == ['a=b', 'c="foo bar"', "'d e'"], "Expected ['a=b', 'c=\"foo bar\"', \"'d e'\"], but got {0} instead".format(split_args("a=b c=\"foo bar\" 'd e'"))

    # TODO: remove this check when jinja2 stops swallowing newlines
    #assert split_

# Generated at 2022-06-13 07:13:05.511273
# Unit test for function split_args
def test_split_args():
    """
    Unit test for split_args (and join_args).

    Tests the following special cases:
        - Comments
        - Line continuations
        - Quoted multi-line values
        - Multi-line arguments
        - Multiple special cases in sequence
        - Jinja2 statements (print, block and comment)
    """
    import re

    # Test data

# Generated at 2022-06-13 07:13:16.601464
# Unit test for function parse_kv
def test_parse_kv():
    options = {
        'create': None,
        'echo': True
    }
    assert parse_kv("create= echo=1 ", check_raw=True) == options

    options = {
        'foo': None,
        'bar': '1',
        'baz': '1'
    }
    assert parse_kv("foo= bar='1' baz=\"1\" ", check_raw=True) == options

    options = {
        'foo': None,
        'bar': '1',
        'baz': '1'
    }
    assert parse_kv("foo= bar=\"1\" baz='1' ", check_raw=True) == options

    options = {
        'foo': None,
        'bar': None,
        'baz': '1'
    }
    assert parse_k

# Generated at 2022-06-13 07:13:25.097159
# Unit test for function split_args

# Generated at 2022-06-13 07:13:34.963228
# Unit test for function split_args
def test_split_args():

    # It's not easy to test this count of jinja2 blocks, but I think this is probably good enough
    print_depth = _count_jinja2_blocks('foo', 0, "{{", "}}")
    assert print_depth == 0

    print_depth = _count_jinja2_blocks('foo {{', 1, "{{", "}}")
    assert print_depth == 1

    print_depth = _count_jinja2_blocks('{{', 1, "{{", "}}")
    assert print_depth == 0

    print_depth = _count_jinja2_blocks('}}', 1, "{{", "}}")
    assert print_depth == 0

    print_depth = _count_jinja2_blocks('foo {{ bar }}', 1, "{{", "}}")
    assert print_depth == 1

    print_depth

# Generated at 2022-06-13 07:13:40.083381
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("key1=val1 key2=val2") == {u'key1': u'val1', u'key2': u'val2'}
    assert parse_kv("key1=val1= val2=val2") == {u'key1': u'val1=', u'key2': u'val2'}
    assert parse_kv("key1=val1\\= val2=val2") == {u'key1': u'val1=', u'key2': u'val2'}
    assert parse_kv("key1=val1\\\\ val2=val2") == {u'key1': u'val1\\', u'key2': u'val2'}

# Generated at 2022-06-13 07:13:49.739396
# Unit test for function parse_kv
def test_parse_kv():
    def check(args, expected):
        check_raw = bool(expected.get('_raw_params'))
        actual = parse_kv(args, check_raw=check_raw)

        assert actual == expected, "parse_kv(%r) got %r expected %r" % (args, actual, expected)
    check("a=b c=d", {"a": "b", "c": "d"})
    check("a=b c=d", {"a": "b", "c": "d"})
    check("a=b c=d", {"a": "b", "c": "d"})
    check("a=b c=d", {"a": "b", "c": "d"})
    check("a=b c=d", {"a": "b", "c": "d"})
    check

# Generated at 2022-06-13 07:14:04.277285
# Unit test for function split_args
def test_split_args():
    from os import urandom
    from random import randint

    def alphanumeric():
        x = randint(48, 122)
        if x not in range(58, 65) and x not in range(91, 97):
            return chr(x)
        return alphanumeric()

    def gen_random_args():
        args = urandom(randint(10, 20))
        args_list = []
        for i in range(0, len(args)):
            if args[i] == ' ':
                args_list.append(alphanumeric() + str(randint(100, 900)))
            elif args[i] == '\n':
                args_list.append(alphanumeric() + str(randint(100, 900)))
        return ' '.join(args_list)


# Generated at 2022-06-13 07:14:11.886061
# Unit test for function split_args
def test_split_args():
    class TestCase(object):
        """
        Class to test join_args and split_args.
        """
        def __init__(self, args, result):
            """
            Constructor.
            :param args: The string of arguments.
            :param result The expected result.
            """
            self.args = args
            self.result = result


# Generated at 2022-06-13 07:14:26.417732
# Unit test for function split_args
def test_split_args():
    # base case
    assert ['a=b', 'c="foo bar"'] == split_args("a=b c='foo bar'")

    # interpolation inside of a string
    assert ['a=b', 'c="foo bar{{foo}}"'] == split_args("a=b c='foo bar{{foo}}'")

    # expansion inside a string
    assert ['a=b', 'c="foo bar{%foo%}"'] == split_args("a=b c='foo bar{%foo%}'")

    # expansion inside a string, with other characters
    assert ['a=b', 'c="foo bar{%foo%}bar"'] == split_args("a=b c='foo bar{%foo%}bar'")

    # interpolation separated by space, with expansion

# Generated at 2022-06-13 07:14:50.296378
# Unit test for function parse_kv
def test_parse_kv():
    def assert_args(args, opts):
        assert parse_kv(args) == opts
        assert parse_kv('"%s"' % args) == opts

    assert_args("create mode=0600 owner=root path=/etc/sudoers.d/10-deploy", {u'create': u'', u'mode': u'0600', u'owner': u'root', u'path': u'/etc/sudoers.d/10-deploy'})
    assert_args("path='/etc/sudoers.d/10-deploy' mode='0600' owner='root' create", {u'create': u'', u'mode': u'0600', u'owner': u'root', u'path': u'/etc/sudoers.d/10-deploy'})

# Generated at 2022-06-13 07:14:58.888502
# Unit test for function parse_kv
def test_parse_kv():
  assert parse_kv('foo=bar') == {'foo':'bar'}
  assert parse_kv('foo=bar baz') == {'foo':'bar', '_raw_params':'baz'}
  assert parse_kv('foo=bar baz=bam') == {'foo':'bar', 'baz':'bam'}
  assert parse_kv('foo=bar baz=bam foo=foobar') == {'foo':'foobar', 'baz':'bam'}
  assert parse_kv('foo="bar" baz=bam foo=foobar') == {'foo':'foobar', 'baz':'bam'}

# Generated at 2022-06-13 07:15:12.724516
# Unit test for function parse_kv
def test_parse_kv():
    # Ensure that parse_kv (when called with check_raw=True) is able to identify
    # and ignore command line parameters that it cannot process.

    # We should be able to process an empty list of options
    options = parse_kv(u"", check_raw=True)
    assert len(options) == 0

    # We should be able to process a single key-value pair
    options = parse_kv(u"one=two", check_raw=True)
    assert len(options) == 1
    assert options[u'one'] == u'two'

    # We should be able to process a single parameter with two equals signs (since it will be ignored)
    options = parse_kv(u"one=two=three", check_raw=True)
    assert len(options) == 1

# Generated at 2022-06-13 07:15:23.816277
# Unit test for function split_args
def test_split_args():
    assert split_args(u'''echo {'foo': 'bar', 'baz': ['ansible', 'rocks']}''') == [u'''echo {'foo': 'bar', 'baz': ['ansible', 'rocks']}''']
    assert split_args(u'echo {a: {b: c}}') == [u'echo', u'{a:', u'{b:', u'c}}']
    assert split_args(u'echo "a: {b: c}"') == [u'echo', u'"a: {b: c}"']
    assert split_args(u'echo "a: {b: c}" \\') == [u'echo', u'"a: {b: c}"', u'\\']

# Generated at 2022-06-13 07:15:31.877308
# Unit test for function split_args
def test_split_args():
    a = "{{a}}"
    b = "{{a}} {{b}}"
    c = "{{a}} {{b}} {{c}}"
    d = "{{a}} {{b}} '{{c}}'"
    e = "{{a}} {{b}} '{{c}}' {{d}}"
    f = "{{a}} 'not quotes'"
    g = "{{a}} {{b}} 'not quotes'"
    h = "{{a}} 'not quotes' {{b}}"
    i = "{{a}} 'not quotes' {{b}} '{c}'"
    j = "{{a}} 'not {quotes}}' {{b}} '{c}'"
    k = "{{a}} 'not {quotes}' {{b}} '{c}'"

# Generated at 2022-06-13 07:15:40.947512
# Unit test for function parse_kv

# Generated at 2022-06-13 07:15:50.236194
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("ANSIBLE_MODULE_ARGS='--name=Joe --state=present'") == {u'ANSIBLE_MODULE_ARGS': u'--name=Joe --state=present'}
    assert parse_kv("a=b c=d") == {u'a': u'b', u'c': u'd'}
    assert parse_kv("a='b' c=\"d\"") == {u'a': u'b', u'c': u'd'}
    assert parse_kv("a='b=c' c=\"d=e\"") == {u'a': u'b=c', u'c': u'd=e'}
    assert parse_kv("a='b=' c=\"d=\"") == {u'a': u'b=', u'c': u'd='}


# Generated at 2022-06-13 07:16:04.464446
# Unit test for function split_args

# Generated at 2022-06-13 07:16:13.730698
# Unit test for function split_args
def test_split_args():
    def _test_split_args(args, expected, desc):
        actual = split_args(args)
        try:
            assert actual == expected
        except AssertionError as e:
            e.args = (u"test_split_args failure. {0}".format(desc),)
            raise

    assert split_args('') == []
    assert split_args('foo') == ['foo']
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo   bar') == ['foo', 'bar']
    assert split_args('foo bar   ') == ['foo', 'bar']
    assert split_args('foo bar baz   ') == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 07:16:22.776399
# Unit test for function split_args
def test_split_args():
    assert split_args('a b c') == ['a', 'b', 'c']
    assert split_args('a b c ') == ['a', 'b', 'c']
    assert split_args(' a b c') == ['a', 'b', 'c']
    assert split_args('a b c ') == ['a', 'b', 'c']
    assert split_args('a b "0"') == ['a', 'b', '"0"']
    assert split_args('a b "0" ') == ['a', 'b', '"0"']
    assert split_args('a b "0" c') == ['a', 'b', '"0"', 'c']
    assert split_args('a b "0" =') == ['a', 'b', '"0"', '=']
    assert split_

# Generated at 2022-06-13 07:17:10.115618
# Unit test for function split_args
def test_split_args():
    import unittest
    import sys
    from ansible.module_utils._text import to_bytes
    class TestSplitArgs(unittest.TestCase):
        def test_split_args_simple(self):
            r = split_args("a=b c=d")
            self.assertEqual(r, ["a=b", "c=d"])

        def test_split_args_line_continuation(self):
            r = split_args("a=b \\ c=d")
            self.assertEqual(r, ["a=b", "c=d"])

        def test_split_args_whitespace(self):
            r = split_args("a=b   c=d")
            self.assertEqual(r, ["a=b", "c=d"])
