

# Generated at 2022-06-13 07:07:30.900897
# Unit test for function split_args
def test_split_args():
    # Test basic outcome of splitting args
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Test splitting args with empty args
    assert split_args('a=b c=') == ['a=b', 'c=']

    # Test splitting args with escaped quotes in quoted strings
    assert split_args('a=b c="foo\\"bar"') == ['a=b', 'c="foo\\"bar"']

    # Test splitting args with escaped quotes in quoted strings and equals
    assert split_args('a=b c="foo=bar"') == ['a=b', 'c="foo=bar"']

    # Test splitting args with escaped equals
    assert split_args('a=b c=foo\\=bar') == ['a=b', 'c=foo=bar']



# Generated at 2022-06-13 07:07:40.234305
# Unit test for function split_args
def test_split_args():
    # Test combinations of
    # 1. Whitespace
    # 2. Quotes
    # 3. Jinja2 blocks
    # 4. Line continuations
    #
    # The expected behavior is that split_args() will intelligently reassemble
    # those that may have been split over a jinja2 block or quotes.
    #
    # This test set is not meant to be exhaustive, but to cover some common
    # use cases.

    # Passing
    test = "a=b c=\"foo bar\" d={{ foo }}"
    params = split_args(test)
    assert params == ['a=b', 'c="foo bar"', 'd={{ foo }}']

    test = "a=b c=\"foo bar\" d={{ foo }}\ne=bar f=baz"
    params = split_args(test)
   

# Generated at 2022-06-13 07:07:45.935609
# Unit test for function split_args
def test_split_args():
    # Test all edge cases.
    args = "foo bar"
    assert split_args(args) == ["foo", "bar"]

    args = "foo=bar"
    assert split_args(args) == ["foo=bar"]

    args = "foo='bar'"
    assert split_args(args) == ["foo='bar'"]

    args = "foo=\"bar\""
    assert split_args(args) == ["foo=\"bar\""]

    args = "foo=bar bar"
    assert split_args(args) == ["foo=bar", "bar"]

    args = "foo=bar bar=baz"
    assert split_args(args) == ["foo=bar", "bar=baz"]

    args = "foo='bar baz'"
    assert split_args(args) == ["foo='bar baz'"]

   

# Generated at 2022-06-13 07:07:55.663770
# Unit test for function split_args
def test_split_args():
    assert join_args(split_args("a=b c=\"foo bar\"")) == "a=b c=\"foo bar\""
    assert join_args(split_args("  a=b c=\"foo bar\"")) == "  a=b c=\"foo bar\""
    assert join_args(split_args("a=b\n c=\"foo bar\"")) == "a=b\n c=\"foo bar\""
    assert join_args(split_args("a=b \\\nc=\"foo bar\"")) == "a=b \\\nc=\"foo bar\""
    assert join_args(split_args("a=b c=\\\"foo bar")) == "a=b c=\\\"foo bar"

# Generated at 2022-06-13 07:08:03.437982
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    def validate_results(options, expected, msg):
        expected = to_text(expected)
        for key, value in expected.items():
            key = to_text(key)
            option = to_text(value)
            if key == '_raw_params':
                test.assertEqual(option, options.get('_raw_params'),
                                 "raw params differ: %s\n"
                                 "actual: %s\n"
                                 "expected: %s" % (msg, options.get('_raw_params'), option))

# Generated at 2022-06-13 07:08:11.911795
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c="d" e=;}') == {u'a': u'b', u'c': u'd', u'e': u';}'}
    assert parse_kv('a=b c="d" e=;}', True) == {u'a': u'b', u'c': u'd', u'e': u';}', u'_raw_params': u'a=b c="d" e=;}'}
    assert parse_kv('a=b c="d" e=;}', False) == {u'a': u'b', u'c': u'd', u'e': u';}'}

# Generated at 2022-06-13 07:08:16.518605
# Unit test for function split_args

# Generated at 2022-06-13 07:08:26.659309
# Unit test for function parse_kv
def test_parse_kv():
    '''
    AnsibleModule tests for basic module utilities
    '''
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from test.unit.module_utils_common import AnsibleModule
    import ansible.module_utils.basic

    # function under test
    x = parse_kv('a=1 b= 2 c="foo bar" d="foo=bar" e=\'foo=bar\' f="\'foo bar\'" g="\\"foo bar\\"" h="\\"foo=bar\\""')
    put = AnsibleModule(  # noqa
        argument_spec={'x': dict(type='dict', required=True)},
        supports_check_mode=True,
    ).params['x']
   

# Generated at 2022-06-13 07:08:37.781186
# Unit test for function split_args
def test_split_args():
    # This test is backed by a test_id to make it easier to trace the test to the related function
    def _test_arg_splitting(test_id, input_arg, expected):
        result = split_args(input_arg)
        assert expected == result, "{0}: Expected: {1} Received: {2}".format(test_id, expected, result)

    _test_arg_splitting('t1', u'', [])
    _test_arg_splitting('t2', u' \n', [])
    _test_arg_splitting('t3', u'a', [u'a'])
    _test_arg_splitting('t4', u'a b', [u'a', u'b'])

# Generated at 2022-06-13 07:08:48.408834
# Unit test for function split_args

# Generated at 2022-06-13 07:09:11.905409
# Unit test for function split_args
def test_split_args():
    # Test the case with no jinja2 or quotes
    result = split_args(u'foo=bar baz=qux')
    assert result == [u'foo=bar', u'baz=qux']
    # Test the case where there is a newline
    result = split_args(u'''foo=bar\nbaz=qux''')
    assert result == [u'foo=bar\n', u'baz=qux']
    # Test the case where there are jinja2 blocks
    result = split_args(u'''foo=bar create_dirs {{ file_paths }} baz=qux''')
    assert result == [u'foo=bar', u'create_dirs', u'''{{ file_paths }}''', u'baz=qux']
    # Test the case where there

# Generated at 2022-06-13 07:09:19.895481
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv("foo=one two=three four=", check_raw=True)
    assert options == {u'foo': u'one', u'two': u'three', u'four': u'', u'_raw_params': u'four='}, options

    options = parse_kv(r'foo=one two=three four=\n', check_raw=False)
    assert options == {u'two': u'three', u'foo': u'one'}, options

    options = parse_kv(r'foo=one two=three four=\n', check_raw=True)
    assert options == {u'two': u'three', u'foo': u'one', u'_raw_params': u'four=\\n'}, options


# Generated at 2022-06-13 07:09:34.931767
# Unit test for function parse_kv

# Generated at 2022-06-13 07:09:47.452055
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1") == {u'a': u'1'}
    assert parse_kv("a=1 b=2") == {u'a': u'1', u'b': u'2'}
    assert parse_kv("creates=/tmp/foo") == {u'creates': u'/tmp/foo'}
    assert parse_kv("removes=/tmp/foo") == {u'removes': u'/tmp/foo'}
    assert parse_kv("chdir=/tmp") == {u'chdir': u'/tmp'}
    assert parse_kv("executable=/bin/zsh") == {u'executable': u'/bin/zsh'}

# Generated at 2022-06-13 07:09:57.193555
# Unit test for function split_args
def test_split_args():
    # Test case where there is no quotes
    test_a = split_args(u'github_user=ansible github_repo=ansible git_branch=devel')
    assert test_a == ['github_user=ansible', 'github_repo=ansible', 'git_branch=devel']

    # Test case where args are split in the middle of double quotes
    test_b = split_args(u'github_user=ansible github_repo=ansible git_branch="devel with spaces"')
    assert test_b == ['github_user=ansible', 'github_repo=ansible', 'git_branch="devel with spaces"']

    # Test case where an arg is split in the middle of single quotes

# Generated at 2022-06-13 07:09:58.865413
# Unit test for function parse_kv
def test_parse_kv():
    # TODO: Write unit tests
    assert False


# Generated at 2022-06-13 07:10:06.896743
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for function parse_kv
    '''

# Generated at 2022-06-13 07:10:20.196923
# Unit test for function split_args
def test_split_args():
    """
    Test the split_args function

    :return:
    """
    assert split_args(u"foo bar") == ["foo", "bar"]
    assert split_args(u"foo  bar") == ["foo", "bar"]
    assert split_args(u"foo=bar") == ["foo=bar"]
    assert split_args(u"foo=bar baz=foobar") == ["foo=bar", "baz=foobar"]
    assert split_args(u"/usr/bin/foo bar") == ["/usr/bin/foo", "bar"]
    assert split_args(u"/usr/bin/foo bar baz\\") == ["/usr/bin/foo", "bar", "baz\\"]
    assert split_args(u"foo='bar'") == ["foo='bar'"]
    assert split_

# Generated at 2022-06-13 07:10:32.587617
# Unit test for function split_args
def test_split_args():
    assert(split_args('a') == ['a'])
    assert(split_args('a b') == ['a', 'b'])
    assert(split_args('a   b  ') == ['a', 'b'])
    assert(split_args('a=b') == ['a=b'])
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c=foo bar'])
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c=foo bar'])
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c=foo bar'])
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c=foo bar'])

# Generated at 2022-06-13 07:10:41.812069
# Unit test for function split_args

# Generated at 2022-06-13 07:11:01.476657
# Unit test for function parse_kv
def test_parse_kv():
    pkv = lambda a: parse_kv(a, check_raw=True)

# Generated at 2022-06-13 07:11:09.623856
# Unit test for function parse_kv
def test_parse_kv():
    """Test that parse_kv() handles:
    - quotes
    - spaces
    - escaped quotes
    - escaped spaces
    - escaped backslashes
    - multiple equals signs
    - unquoted multi-word strings
    - unquoted strings with spaces
    - unquoted strings with quotes
    - unquoted strings with escaped quotes
    - unquoted strings with escaped spaces
    - unquoted strings with escaped backslashes
    - unquoted strings with multiple equals signs
    """
    def _t(arg_string, result):
        parsed = parse_kv(arg_string)
        assert parsed == result, '%s should be parsed to %s, got %s' % (arg_string, result, parsed)

    _t('foo=bar', {'foo': 'bar'})

# Generated at 2022-06-13 07:11:17.356912
# Unit test for function split_args

# Generated at 2022-06-13 07:11:27.516571
# Unit test for function parse_kv
def test_parse_kv():
    # first test with a simple (k,v) pair string and make sure it returns a dict
    args = 'key=value'
    assert isinstance(parse_kv(args), dict)

    # next, test with a string that contains raw parameters and make sure
    # they are placed in the '_raw_params' key of the returned dict
    args = 'key=value key2=value2 param1 param2'
    options = parse_kv(args)
    assert isinstance(options, dict)
    assert options['key'] == 'value'
    assert options['key2'] == 'value2'
    assert options['_raw_params'] == 'param1 param2'

    # next, test with a string that contains raw parameters and we set check_raw=False
    # in this case, we should not get any results in the '_raw

# Generated at 2022-06-13 07:11:40.995791
# Unit test for function parse_kv
def test_parse_kv():
    import json
    import unittest
    class TestParseKv(unittest.TestCase):
        def test_one_param(self):
            self.assertEqual(json.dumps(parse_kv(u'hello=world')), '{"hello": "world"}')
        def test_two_params(self):
            self.assertEqual(json.dumps(parse_kv(u'hello=world kitty=cat')), '{"hello": "world", "kitty": "cat"}')
        def test_two_params_with_spaces(self):
            self.assertEqual(json.dumps(parse_kv(u'hello = world  kitty = cat')), '{"hello": "world", "kitty": "cat"}')

# Generated at 2022-06-13 07:11:50.617679
# Unit test for function split_args
def test_split_args():
    assert split_args('"echo foo" "bar baz"') == ['echo foo', 'bar baz']
    assert split_args('"echo foo" "bar baz\\"') == ['echo foo', 'bar baz"']
    assert split_args('"echo foo" "bar baz\\\\"') == ['echo foo', 'bar baz\\']

# Generated at 2022-06-13 07:12:01.946080
# Unit test for function split_args

# Generated at 2022-06-13 07:12:09.235245
# Unit test for function parse_kv
def test_parse_kv():

    # Test parsing of a single argument with no equals
    assert parse_kv(u'hello') == {u'_raw_params': u'hello'}

    # Test parsing of a single argument with equals but no value
    assert parse_kv(u'hello=') == {u'hello': u''}

    # Test parsing of multiple arguments, one of which has no value
    assert parse_kv(u'hello= world') == {u'hello': u'world'}

    # Test parsing of a single argument with equals and a value
    assert parse_kv(u'hello=world') == {u'hello': u'world'}

    # Test parsing of a single argument with equals and a quoted value
    assert parse_kv(u'hello="world"') == {u'hello': u'world'}

    # Test parsing of

# Generated at 2022-06-13 07:12:17.000723
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:30.725854
# Unit test for function split_args
def test_split_args():
    '''
        Unit test for function split_args
        This tests the split_args function
        by splitting input strings, then using
        join_args to put the strings back together.
        If the function works properly, the original
        input string will be identical to the
        string that has been split and rejoined.
    '''
    test_string_list = [
        ''' "quoted string" bar=foo {# comment with {{ another comment }} #} ''',
        ''' foo bar=baz 'single quoted' "double quoted" "mixed 'single' quoted" baz=bat '''
    ]

    for test_string in test_string_list:
        parsed_arg_list = split_args(test_string)
        rejoined_string = join_args(parsed_arg_list)

# Generated at 2022-06-13 07:12:49.585143
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\" d="e f') == ['a=b', 'c="foo bar\\"', 'd="e f']
    assert split_args('a=b c="foo bar\\"') == ['a=b', 'c="foo bar\\"']
    assert split_args(r"a=b c='foo bar\'") == ['a=b', "c='foo bar\\'"], "failure in handling literal quotes"

# Generated at 2022-06-13 07:12:59.542678
# Unit test for function split_args

# Generated at 2022-06-13 07:13:06.694385
# Unit test for function split_args
def test_split_args():
    import pytest


# Generated at 2022-06-13 07:13:18.246758
# Unit test for function parse_kv
def test_parse_kv():
    # empty string
    assert parse_kv('') == {}

    # flat
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}

    # quoted strings
    assert parse_kv('a="  b  " c="  d  "') == {'a': '  b  ', 'c': '  d  '}

    # escaped quotes
    assert parse_kv('a=\\"b\\" c=\\"d\\"') == {'a': '"b"', 'c': '"d"'}

    # quoted escaped quotes
    assert parse_kv('a="\\"b\\"" c="\\"d\\""') == {'a': '\\"b\\"', 'c': '\\"d\\"'}

    # positional

# Generated at 2022-06-13 07:13:25.871217
# Unit test for function split_args
def test_split_args():
    def assert_split(args, expected):
        actual = split_args(args)
        assert actual == expected, '''split_args("%s") expected "%s", got "%s"''' % (args, expected, actual)

    assert_split("foo \"bar baz\" quux", ['foo', '"bar baz"', 'quux'])
    assert_split("foo 'bar baz' quux", ['foo', "'bar baz'", 'quux'])
    assert_split("foo 'bar baz' \"quux larry\"", ['foo', "'bar baz'", '"quux larry"'])

# Generated at 2022-06-13 07:13:35.720077
# Unit test for function split_args
def test_split_args():
    assert split_args("ls -l /") == ["ls", "-l", "/"]
    assert split_args("ls -l / ") == ["ls", "-l", "/"]
    assert split_args(" ls -l") == ["ls", "-l"]
    assert split_args("ls -l") == ["ls", "-l"]
    assert split_args("ls -l / ") == ["ls", "-l", "/"]
    assert split_args("ls -l \'foo bar\'") == ["ls", "-l", "foo bar"]
    assert split_args("ls -l \"foo bar\"") == ["ls", "-l", "foo bar"]
    assert split_args("ls -l \"foo bar\" baz") == ["ls", "-l", "foo bar", "baz"]

# Generated at 2022-06-13 07:13:41.062976
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b cd=e f= g h i="j k" l=\'m n\' o=\\"p\\" q=\\\\"r\\\\ s=\\\'t\\\'\"u v\" w') == {'a': 'b', 'cd': 'e', 'f': '', 'g': None, 'h': None, 'i': 'j k', 'l': 'm n', 'o': '"p"', 'q': '\\"r\\', 's': '\'t\'', 'u v': None, 'w': None, '_raw_params': 'g h i="j k" l=\'m n\' o=\\"p\\" q=\\\\"r\\\\ s=\\\'t\\\'\"u v\" w'}

# Generated at 2022-06-13 07:13:44.040219
# Unit test for function split_args
def test_split_args():
    # TODO: write a real unit test for this (not a simple test of the test)
    assert split_args(u'a=b c="foo bar"')[0] == 'a=b'

# Generated at 2022-06-13 07:13:50.431970
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('user=robert password=foo user=frank') == {u'password': u'foo', u'user': u'frank', u'_raw_params': u'user=robert password=foo user=frank'}
    assert parse_kv('user=robert password=foo user=frank', False) == {u'password': u'foo', u'user': u'frank'}
    assert parse_kv('user=robert password=foo', True) == {u'password': u'foo', u'user': u'robert', u'_raw_params': u'user=robert password=foo'}
    assert parse_kv('user=robert password=foo', False) == {u'password': u'foo', u'user': u'robert'}
    assert parse

# Generated at 2022-06-13 07:14:04.847498
# Unit test for function parse_kv
def test_parse_kv():
    args = """foo='bar' param=hello_world "something else"="other thing" key=value param=value 'some value'="some value" """

    parsed = parse_kv(args)
    assert parsed['foo'] == 'bar'
    assert parsed['param'] == 'value'
    assert parsed['"something else"'] == 'other thing'
    assert parsed['key'] == 'value'
    assert parsed["'some value'"] == 'some value'
    assert len(parsed) == 5

    parsed = parse_kv(args, check_raw=True)
    import pprint
    pprint.pprint(parsed)
    assert parsed['foo'] == 'bar'
    assert parsed['param'] == 'value'
    assert parsed['"something else"'] == 'other thing'
    assert parsed['key']

# Generated at 2022-06-13 07:14:12.997626
# Unit test for function parse_kv
def test_parse_kv():
    pass



# Generated at 2022-06-13 07:14:26.992889
# Unit test for function split_args
def test_split_args():
    '''
    This is a basic unit test which compares expected output to the split_args
    function on a list of input strings. It is not exhaustive.
    '''

# Generated at 2022-06-13 07:14:37.805070
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == {u'foo': u'bar'}
    assert parse_kv("foo=\"bar\"") == {u'foo': u'bar'}
    assert parse_kv("foo=\"bar\" baz=qux") == {u'foo': u'bar', u'baz': u'qux'}
    assert parse_kv("foo=bar baz=qux") == {u'foo': u'bar', u'baz': u'qux'}
    assert parse_kv("foo=bar baz=qux something_else") == {u'foo': u'bar', u'baz': u'qux', u'_raw_params': u'something_else'}

# Generated at 2022-06-13 07:14:45.521785
# Unit test for function parse_kv
def test_parse_kv():
    args = [
        "_raw_params=''",
        "warn=noexec",
        "creates=''",
        "chdir=''",
        "executable=None",
        "removes=''",
        "stdin=None",
        "strip_empty_ends=True",
        "stdin_add_newline=True"
    ]


# Generated at 2022-06-13 07:14:55.743489
# Unit test for function parse_kv
def test_parse_kv():
    def _test_parse_kv(opt, check_raw=False, verbose=False):
        ret = parse_kv(opt, check_raw=check_raw)
        if verbose:
            print("--test '%s' vs '%s' ret=%s" % (opt, _test_val(ret), _test_val(ret) == opt))
        return ret
    def _test_val(ret):
        kv_out = []
        for k in sorted(ret.keys()):
            v = ret.get(k, None)
            if k and k == '_raw_params':
                kv_out.append(v)
            else:
                kv_out.append("%s=%s" % (k, v))
        return " ".join(kv_out)

# Generated at 2022-06-13 07:15:03.265233
# Unit test for function split_args
def test_split_args():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # only run the unit tests on py26 and py27
    # because Python 3.2 doesn't support unittest2
    # and python < 2.6 doesn't support the nice
    # unittests from 2.6 onwards
    import sys
    if sys.version_info[0:2] != (2, 6):
        return

    import unittest2 as unittest
    class TestSplitArgs(unittest.TestCase):
        '''
        This class exercises split_args()
        '''

        def setUp(self):
            self._vault_password = '$6$hello'


# Generated at 2022-06-13 07:15:15.641888
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz') == {u'foo': u'bar', u'_raw_params': u'baz'}
    assert parse_kv('foo=bar baz=blah') == {u'foo': u'bar', u'baz': u'blah'}
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('foo=bar', check_raw=False) == {u'foo': u'bar'}
    assert parse_kv('foo=bar baz', check_raw=False) == {u'foo': u'bar', u'_raw_params': u'baz'}



# Generated at 2022-06-13 07:15:26.609157
# Unit test for function split_args
def test_split_args():
    assert split_args('a b') == ['a', 'b']
    assert split_args('a b c') == ['a', 'b', 'c']
    assert split_args('a "b c"') == ['a', '"b c"']
    assert split_args('a "b c d"') == ['a', '"b c d"']
    assert split_args('a "b c" d') == ['a', '"b c"', 'd']
    assert split_args('a "b c') == ['a', '"b', 'c']
    assert split_args('a "b c') == ['a', '"b', 'c']
    assert split_args('a b" c') == ['a', 'b" c']

# Generated at 2022-06-13 07:15:37.606876
# Unit test for function parse_kv
def test_parse_kv():
    '''parse_kv is used in shell and command modules so I want to
    make sure it parses all argument strings correctly.

    I've written a unit test for it but I didn't want to add the
    dependency just for that one module. If a shell/command parameter
    ends up with a bug, this is probably where the bug is.'''

# Generated at 2022-06-13 07:15:47.545454
# Unit test for function parse_kv
def test_parse_kv():
    '''This function tests the result of a parse_kv
    '''
    test_str1 = u'key1=value1 key2=value2'
    result_dict1 = parse_kv(test_str1)
    assert(result_dict1[u'key1'] == u'value1')
    assert(result_dict1[u'key2'] == u'value2')

    test_str2 = u"key1='value1' key2=\"value2\""
    result_dict2 = parse_kv(test_str2)
    assert(result_dict2[u'key1'] == u'value1')
    assert(result_dict2[u'key2'] == u'value2')


# Generated at 2022-06-13 07:16:12.637564
# Unit test for function parse_kv
def test_parse_kv():
    # basic
    test_parse_kv_helper("a=b", {"a": "b"})
    # basic with spaces
    test_parse_kv_helper(" a = b ", {"a": "b"})
    # basic multi-word value
    test_parse_kv_helper("a=b c", {"a": "b c"})
    # multiple key/value pairs
    test_parse_kv_helper("a=b c=d", {"a": "b", "c": "d"})
    # quotes
    test_parse_kv_helper("a='b c' d='e f'", {"a": "b c", "d": "e f"})

# Generated at 2022-06-13 07:16:21.527185
# Unit test for function split_args
def test_split_args():
    actuals = []

    actuals.append(split_args('"foo bar" baz'))
    actuals.append(split_args('foo=$HOME/user/bar "baz" "bang boom"'))
    actuals.append(split_args('foo=$HOME/user/bar "baz" "bang boom" "xyz = 123"'))
    actuals.append(split_args('foo=$HOME/user/bar "baz" "bang boom" "xyz = 123" abc=123'))
    actuals.append(split_args('foo=$HOME/user/bar "baz" "bang boom" "xyz = 123" abc=123 xyz=123'))

# Generated at 2022-06-13 07:16:29.142615
# Unit test for function split_args
def test_split_args():
    import random
    import string
    import pytest

    quotes = ['', '"', "'"]
    blocks = ['', '{%', '%}', '{{', '}}', '{#', '#}']

    # Make a random set of arguments for testing
    def random_args(depth=0):
        pieces = []
        while True:
            # Each piece can be either a string or a block
            if random.random() > .7 and depth < 5:
                piece = random_block(depth)
            else:
                piece = random_string()
            pieces.append(piece)
            # After each piece, we may either end, or continue
            if random.random() > .6:
                break
        return ' '.join(pieces).strip()

    # Make a random string for testing
    def random_string():
        return

# Generated at 2022-06-13 07:16:38.042354
# Unit test for function split_args
def test_split_args():
    # simple string
    assert split_args("a=b c=d") == ["a=b", "c=d"]

    # simple string with quoted entries
    assert split_args("a=b c='foo bar' d=\"foo bar\"") == ["a=b", "c='foo bar'", 'd="foo bar"']

    # simple string with escaped quotes
    assert split_args("a=b c='foo bar' d=\"foo bar\" e=\"foo\\\\\"bar\" f='foo\\\\\\'bar'") == ["a=b", "c='foo bar'", 'd="foo bar"', 'e="foo\\\\"bar"', "f='foo\\\\'bar'"]

    # simple string with escaped backslash

# Generated at 2022-06-13 07:16:51.479239
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Test function parse_kv
    '''
    # simple test
    assert parse_kv('a=b c="d" e=f') == {'a': 'b', 'c': 'd', 'e': 'f'}
    # unicode test
    assert parse_kv('a=b c="d" e=f unicode_val="unicodé"') == {'a': 'b', 'c': 'd', 'e': 'f', 'unicode_val': u'unicodé'}
    # unicode escape test
    assert parse_kv('a=b c="d" e=f unicode_val="unicode\\xe9"') == {'a': 'b', 'c': 'd', 'e': 'f', 'unicode_val': u'unicodé'}
   

# Generated at 2022-06-13 07:16:58.229327
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('key1=val1 key2=val2 key3=val3') == {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    assert parse_kv('key1=val1') == {'key1': 'val1'}
    assert parse_kv('key1') == {}
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('foo bar') == {'_raw_params': 'foo bar'}
    assert parse_kv('foo bar', check_raw=False) == {}
    assert parse_kv('chdir=/tmp creates=foo') == {'_raw_params': 'creates=foo', 'chdir': '/tmp'}
    assert parse_k