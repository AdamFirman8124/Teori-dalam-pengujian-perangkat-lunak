

# Generated at 2022-06-13 04:31:14.631153
# Unit test for function unquote
def test_unquote():
    print("unquote('\"\"')=", unquote('""'))
    print("unquote('\'\'')=", unquote("''"))
    print("unquote('')=", unquote(''))
    print("unquote('\"foo\"')=", unquote('"foo"'))
    print("unquote('\'foo\'')=", unquote("'foo'"))
    print("unquote('\'\"\'')=", unquote("'\"'"))
    print("unquote('\"\'\"')=", unquote("\"'\""))
    print("unquote('foo')=", unquote('foo'))
    print("unquote('\"foo')=", unquote('"foo'))
    print("unquote('foo\"')=", unquote('foo"'))

# Generated at 2022-06-13 04:31:20.547224
# Unit test for function split_args
def test_split_args():
    '''Make sure quotes and jinja2 work.'''

# Generated at 2022-06-13 04:31:31.933648
# Unit test for function split_args
def test_split_args():
    args = "foo=bar baz=foo"
    assert split_args(args) == ["foo=bar", "baz=foo"]

    args = "a='foo bar'"
    assert split_args(args) == ["a='foo bar'"]

    args = "b=\"foo bar\""
    assert split_args(args) == ["b=\"foo bar\""]

    args = "a='foo bar' b=\"foo bar\""
    assert split_args(args) == ["a='foo bar'", 'b="foo bar"']

    # make sure we can split on '=' as well, to handle k=v pairs like
    # in 'with_items:'
    args = "a=foo b=bar"
    assert split_args(args) == ["a=foo", 'b=bar']

    # split on '=' inside quotes

# Generated at 2022-06-13 04:31:36.121869
# Unit test for function unquote
def test_unquote():
    assert 'bar' == unquote('bar')
    assert 'bar' == unquote('"bar"')
    assert 'bar' == unquote("'bar'")
    assert 'bar' == unquote("'bar")


# Generated at 2022-06-13 04:31:43.927524
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted("foo")
    assert is_quoted("\"foo\"")
    assert is_quoted("\"foo")
    assert is_quoted("'foo'")
    assert is_quoted("'foo")
    assert is_quoted("''foo''")
    assert is_quoted("''foo")
    assert is_quoted("''foo'")
    assert is_quoted("\"\"foo\"\"")
    assert is_quoted("\"\"foo")
    assert is_quoted("\"\"foo\"")
    assert is_quoted('\"\"foo')
    assert is_quoted('\"\"foo\"')
    assert not is_quoted('')
    assert not is_quoted('foo')


# Generated at 2022-06-13 04:31:55.739565
# Unit test for function split_args
def test_split_args():
    # test basic case with no blocks or quotes
    a = split_args("one two three four five")
    assert a == ['one', 'two', 'three', 'four', 'five'], "%s != %s" % (a, ['one', 'two', 'three', 'four', 'five'])
    # test quoted strings
    a = split_args("""one 'two three' four five""")
    assert a == ['one', 'two three', 'four', 'five'], "%s != %s" % (a, ['one', 'two three', 'four', 'five'])
    # test multiline quoted strings
    a = split_args("""one "two
three" four""")

# Generated at 2022-06-13 04:32:08.270995
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('a') == 'a'
    assert unquote('a"') == 'a"'
    assert unquote('"a') == '"a'
    assert unquote('"a"') == 'a'
    assert unquote("'a'") == 'a'
    assert unquote(r"'a'") == r"'a'"
    assert unquote('"a\\""') == 'a"'
    assert unquote(r"'a\\\''") == r"a\'"
    assert unquote(r"'a')") == r"'a')"
    assert unquote(r"'a\\')") == r"a\')"
    assert unquote(r"'a\''") == r"a'"
    assert unquote('"a\\""') == 'a"'
    assert unquote

# Generated at 2022-06-13 04:32:19.324097
# Unit test for function split_args
def test_split_args():
    '''
    The intention of this function is to test the arguments splitting
    '''
    import yaml
    from collections import namedtuple
    import json
    import os

    # Get absolute path for the test data dir.
    # It is assumed that the dir contains only .yaml files which are
    # test data for this function.
    test_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'arguments_splitting')

    test_result = namedtuple("TestResult", "result, expected")
    tests_data = {}

    # Read test data from the dir
    for test_data_file_name in [x for x in os.listdir(test_dir_path) if x.endswith('.yaml')]:
        test_data_file_

# Generated at 2022-06-13 04:32:30.336677
# Unit test for function split_args
def test_split_args():
    ''' test_split_args '''

    failed = False

    def assert_results(input_string, expected_array):
        ''' helper function to assert results are correct '''
        results = split_args(input_string)
        if expected_array != results:
            print("Failed asserting\nInput: %s\nExpected: %s\nGot: %s" % (input_string, expected_array, results))
            return False
        return True

    # Assert that we get the results we expect given a variety of inputs
    input_string = '-a hello -b world'
    expected_array = ['-a', 'hello', '-b', 'world']
    assert_results(input_string, expected_array)

    input_string = '-a "hello world"'

# Generated at 2022-06-13 04:32:36.695713
# Unit test for function is_quoted
def test_is_quoted():

    assert is_quoted('"abc"')
    assert is_quoted("'abc'")
    assert is_quoted("''")
    assert is_quoted('""')
    assert not is_quoted("'abc")
    assert not is_quoted("abc")
    assert not is_quoted("")
    assert not is_quoted(None)


# Generated at 2022-06-13 04:32:55.442383
# Unit test for function split_args

# Generated at 2022-06-13 04:33:06.237005
# Unit test for function split_args

# Generated at 2022-06-13 04:33:13.892885
# Unit test for function split_args
def test_split_args():
    print("Testing function split_args of module utils")

    def split_test(test_input, test_result):
        if split_args(test_input) == test_result:
            print('PASS')
        else:
            print('FAIL')
            print('INPUT: ', test_input)
            print('RESULT:', split_args(test_input))
            print('EXPECTED:', test_result)

    split_test('a=b', ['a=b'])
    split_test('a = b', ['a=b'])
    split_test('a = b \\', ['a=b'])
    split_test('a = b \\', ['a=b'])
    split_test('a= b \\', ['a=b'])

# Generated at 2022-06-13 04:33:26.835340
# Unit test for function split_args

# Generated at 2022-06-13 04:33:34.038605
# Unit test for function split_args
def test_split_args():
    input = '''"foo" 'bar' baz=frop'''
    output = ['foo', 'bar', 'baz=frop']
    test_output = split_args(input)
    assert output == test_output
    input = '''"foo" "bar" baz=frop'''
    output = ['foo', 'bar', 'baz=frop']
    test_output = split_args(input)
    assert output == test_output

# Generated at 2022-06-13 04:33:45.628361
# Unit test for function split_args
def test_split_args():
    '''
    Tests for function split_args
    '''

    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"') != ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar') != ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar" "') != ['a=b', 'c="foo bar" "']
    assert split_args('a=b c="foo bar" "') != ['a=b', 'c="foo', 'bar" "']
    assert split_args('a=b c="foo bar" "') != ['a=b', 'c="foo bar"', '"']

# Generated at 2022-06-13 04:33:55.753522
# Unit test for function split_args
def test_split_args():
    ''' test case for function split_args '''
    from ansible.compat import quote
    from nose.tools import (
        assert_equals,
        assert_raises,
    )

    assert_equals(split_args(''), [])
    assert_equals(split_args('a'), ['a'])
    assert_equals(split_args('a b'), ['a', 'b'])
    assert_equals(split_args('a "b c"'), ['a', '"b c"'])
    assert_equals(split_args('a=b'), ['a=b'])
    assert_equals(split_args('a=b c=d'), ['a=b', 'c=d'])

# Generated at 2022-06-13 04:34:05.601881
# Unit test for function split_args

# Generated at 2022-06-13 04:34:12.967863
# Unit test for function split_args

# Generated at 2022-06-13 04:34:24.868623
# Unit test for function split_args
def test_split_args():
    # sanity check
    split_args_result = split_args('foo=bar key="val"')
    assert split_args_result == ['foo=bar', 'key="val"']
    split_args_result = split_args('foo=bar key="val" ')
    assert split_args_result == ['foo=bar', 'key="val"']

    # now test with a jinja block
    split_args_result = split_args('foo="{{ hostvars[inventory_hostname][\'ansible_\' + eth1][\'ipv4\'][\'address\'] }}"')
    assert split_args_result == ['foo="{{ hostvars[inventory_hostname][\'ansible_\' + eth1][\'ipv4\'][\'address\'] }}"']
    # test if it ends with \\
    split_

# Generated at 2022-06-13 04:34:55.885254
# Unit test for function split_args
def test_split_args():
    # test unquoted args
    args = " arg1 arg2 arg3 arg4 "
    res = split_args(args)
    assert ['arg1', 'arg2', 'arg3', 'arg4'] == res

    # test quoted args
    args = ' arg1 arg2="quoted arg" arg3'
    res = split_args(args)
    assert ['arg1', 'arg2="quoted arg"', 'arg3'] == res

    # test quoted args with whitespace
    args = ' arg1 arg2="quoted \n arg"'
    res = split_args(args)
    assert ['arg1', 'arg2="quoted \n arg"'] == res

    # test quoted args with escaped quotes
    args = r''' arg1 arg2="quoted \"arg\"" arg3 '''
    res = split_

# Generated at 2022-06-13 04:35:07.104496
# Unit test for function split_args
def test_split_args():

    # "{{ foo }}"bar" -> ["{{ foo }}", "bar"]
    def test_simple_quoted(input, result):
        assert split_args(input) == result

    test_simple_quoted('"{{ foo }}"bar', ['{{ foo }}', 'bar'])

    # "{{ foo }}"bar" -> ["{{ foo }}bar"]
    def test_simple_quoted_merge(input, result):
        assert split_args(input) == result

    test_simple_quoted_merge('"{{ foo }}bar', ['{{ foo }}bar'])

    # "{{ foo }}"bar baz" -> ["{{ foo }}bar baz"]
    def test_simple_quoted_merge_multiple(input, result):
        assert split_args(input) == result

    test_simple_quoted_mer

# Generated at 2022-06-13 04:35:17.715706
# Unit test for function split_args
def test_split_args():
    # Simple test
    params = split_args("a=b c='foo bar'")
    assert params == ['a=b', "c='foo bar'"], params

    # base64-encoded string as argument
    params = split_args("a=b c='Zm9vIGJhcg=='")
    assert params == ['a=b', "c='Zm9vIGJhcg=='"], params

    # base64-encoded string as argument, split across 2 lines
    params = split_args("a=b c='Zm9vIGJh\ncg=='")
    assert params == ['a=b', "c='Zm9vIGJh\ncg=='"], params

    # Jinja2 syntax
    params = split_args("a=b c='{{foo}}'")
    assert params

# Generated at 2022-06-13 04:35:25.970701
# Unit test for function split_args

# Generated at 2022-06-13 04:35:36.949071
# Unit test for function split_args

# Generated at 2022-06-13 04:35:44.469630
# Unit test for function split_args
def test_split_args():
    ''' Test function split_args '''
    assert split_args('') == []
    assert split_args('  ') == []
    assert split_args(None) == []
    assert split_args('one') == ['one']
    assert split_args('one two') == ['one', 'two']
    assert split_args(' one  two ') == ['one', 'two']
    assert split_args('one two "three four"') == ['one', 'two', '"three four"']
    assert split_args('one two "three four" five') == ['one', 'two', '"three four"', 'five']
    assert split_args('one two "three \'four five\'" six') == ['one', 'two', '"three \'four five\'"', 'six']

# Generated at 2022-06-13 04:35:50.609407
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('a=b') == ['a=b']
    assert split_args('a="1 2"') == ['a="1 2"']
    assert split_args('a="1 2\\"') == ['a="1 2\\"']
    assert split_args('a="1 2\\"    b=c') == ['a="1 2\\"', 'b=c']
    assert split_args('a="b \\"c d\\""') == ['a="b \\"c d\\""']
    assert split_args('a=b "c d"=e') == ['a=b', '"c d"=e']
    assert split_args('a=b "c d"\\=e') == ['a=b', '"c d"\\=e']

# Generated at 2022-06-13 04:35:57.733994
# Unit test for function split_args
def test_split_args(): # pylint: disable=missing-docstring
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a={{ b }} c="foo bar"') == ['a={{ b }}', 'c="foo bar"']
    assert split_args('a={{ b }} c="{{ foo }} {{ bar }}"') == ['a={{ b }}', 'c="{{ foo }} {{ bar }}"']
    assert split_args('a={{ b }} c="{{ foo }} {{ bar }}" d={% if True %}hi{% endif %}') == ['a={{ b }}', 'c="{{ foo }} {{ bar }}"', 'd={% if True %}hi{% endif %}']

# Generated at 2022-06-13 04:36:05.353998
# Unit test for function split_args
def test_split_args():

    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):

        def check(self, arg_string, expect_list):
            arg_list = split_args(arg_string)
            self.assertEqual(arg_list, expect_list)

        def test_split_args_basic(self):
            '''Test basic functionality'''
            self.check('a=b c="foo bar"', ['a=b', 'c="foo bar"'])

            self.check('a=b c="foo bar" d="a=b c=d"', ['a=b', 'c="foo bar"', 'd="a=b c=d"'])


# Generated at 2022-06-13 04:36:16.173830
# Unit test for function split_args
def test_split_args():
    test_cases = []
    wanted_result = []
    test_case_wanted_result = []

    test_cases.append('This is a single arg')
    wanted_result.append(['This is a single arg'])
    test_cases.append('This is a single arg\n\n')
    wanted_result.append(['This is a single arg\n\n'])
    test_cases.append('This is a single\n multiline arg\n\n')
    wanted_result.append(['This is a single\n multiline arg\n\n'])
    test_cases.append('This is a single\nmultiline arg\n\n')
    wanted_result.append(['This is a single\nmultiline arg\n\n'])

# Generated at 2022-06-13 04:37:08.701256
# Unit test for function split_args
def test_split_args():
    '''
      Simple unit test for function split_args
    '''

    # test simple case
    assert split_args('') == []
    assert split_args('a=1') == ['a=1']

    # test a case multiple parameters
    params = split_args('a=1 b=2')
    assert params == ['a=1', 'b=2']
    params = split_args(' a = 1 b = 2 ')
    assert params == ['a=1', 'b=2']

    # test a case with quoted parens
    params = split_args('a=1 b="2 3"')
    assert params == ['a=1', 'b="2 3"']

    # should strip quotes if they match, preserving spaces

# Generated at 2022-06-13 04:37:20.933518
# Unit test for function split_args
def test_split_args():
    ''' unit test will try to call the split_args method and see the effects '''
    cmd = "ansible all -m ping --arg1 'foo bar' --arg2=baz"
    result = split_args(cmd)
    assert result[0] == "ansible"
    assert result[1] == "all"
    assert result[2] == "-m"
    assert result[3] == "ping"
    assert result[4] == "--arg1"
    assert result[5] == "foo bar"
    assert result[6] == "--arg2=baz"

    cmd = "ansible all -m ping --args=\"foo bar\" "
    result = split_args(cmd)
    assert result[0] == "ansible"
    assert result[1] == "all"
    assert result[2]

# Generated at 2022-06-13 04:37:32.474467
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.splitter import split_args

    assert split_args('"foo bar" "baz boz"') == ['"foo bar"', '"baz boz"']
    assert split_args('foo="bar baz" boz=zoinks') == ['foo="bar baz"', 'boz=zoinks']
    assert split_args('foo="bar baz" "boz zoinks"') == ['foo="bar baz"', '"boz zoinks"']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('foo="bar baz') == ['foo="bar baz']
    assert split_args('foo="bar baz') == ['foo="bar baz']

# Generated at 2022-06-13 04:37:41.091359
# Unit test for function split_args
def test_split_args():
    '''Function to generate proper and improper strings that tests split_args()'''
    str_list=[]

# Generated at 2022-06-13 04:37:47.869908
# Unit test for function split_args

# Generated at 2022-06-13 04:37:54.747134
# Unit test for function split_args
def test_split_args():

    # Example of a double quoted string with an equals sign inside.
    # This should end up as a single item in the list.
    args = 'ansible_ssh_port="22"'
    params = split_args(args)
    assert params == ['ansible_ssh_port="22"'], params

    # Example of a bare string containing equals signs.
    # This should end up as a single item in the list (without quotes).
    args = 'ansible_ssh_port=22'
    params = split_args(args)
    assert params == ['ansible_ssh_port=22'], params

    # Example of a bare string containing quotes.
    # This should end up as a single item in the list (without quotes).
    args = 'ansible_ssh_port="22'
    params = split_args(args)

# Generated at 2022-06-13 04:38:02.156397
# Unit test for function split_args
def test_split_args():

    # Simple test 1
    args = 'a=1 b=2 c="foo bar"'
    params = split_args(args)
    assert params == ['a=1', 'b=2', 'c="foo bar"']

    # Simple test 2
    args = 'a=1 b="foo \\\'bar\\\'" c=\'d e f\''
    params = split_args(args)
    assert params == ['a=1', 'b="foo \'bar\'"', 'c=\'d e f\'']

    # Test with jinja2 blocks
    args = 'a=1 b="foo \\\'{% bar %}\\\'" c=\'d e f\''
    params = split_args(args)

# Generated at 2022-06-13 04:38:14.009447
# Unit test for function split_args

# Generated at 2022-06-13 04:38:25.061468
# Unit test for function split_args
def test_split_args():
    assert split_args(" a=b \\") == ['a=b', '\\']
    assert split_args(" a=b '\\'") == ['a=b', "\\"]
    assert split_args(' a=b "\\"') == ['a=b', "\\"]
    assert split_args(' a=b "\\""\\""') == ['a=b', "\"\""]
    assert split_args(' a=b "foo bar"') == ['a=b', '"foo bar"']
    assert split_args(' a=b "foo " \\\'bar\\\' " baz"') == ['a=b', '"foo "', "'bar'", '" baz"']
    assert split_args(' a=b "foo \' bar"') == ['a=b', "'foo ' bar'"]

# Generated at 2022-06-13 04:38:33.833574
# Unit test for function split_args
def test_split_args():

    # test the original problem that inspired this code change, ensuring that
    # when we are inside quotes, we don't split on spaces, but that things
    # continue to be split on newlines. Also ensure we properly handle when
    # a quote is at the end of the string, with no following token

    result = split_args('a=1 b="foo bar" c=3')
    assert result == ['a=1', 'b="foo bar"', 'c=3']

    result = split_args('a=1 b="foo bar c=4" c=3')
    assert result == ['a=1', 'b="foo bar', 'c=4"', 'c=3']

    result = split_args('a=1 b="foo bar" c="3')

# Generated at 2022-06-13 04:40:04.949132
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('"a=b" "c=d"') == ['a=b', 'c=d']
    assert split_args('"a={{b}}" "c={{d}}"') == ['a={{b}}', 'c={{d}}']
    assert split_args('"{%a%}" "{%c%}"') == ['{%a%}', '{%c%}']
    assert split_args('"a={{b}}"\n'
                      '"c={{d}}"\n'
                      '"{%a%}"\n'
                      '"{%c%}"') == ['a={{b}}\n', 'c={{d}}\n', '{%a%}\n', '{%c%}']

# Generated at 2022-06-13 04:40:12.043287
# Unit test for function split_args
def test_split_args():
    '''simple unittest for function split_args'''

    assert split_args(u'foo=bar') == [u'foo=bar']
    assert split_args(u'foo=bar "blah=blah blah"') == [u'foo=bar', u'"blah=blah blah"']
    assert split_args(u'foo=bar "blah=blah blah"') == [u'foo=bar', u'"blah=blah blah"']
    assert split_args(u'foo=bar blah=blah blah') == [u'foo=bar', u'blah=blah', u'blah']
    assert split_args(u'foo=bar "blah=blah \'blah\'"') == [u'foo=bar', u'"blah=blah \'blah\'"']
   

# Generated at 2022-06-13 04:40:22.102243
# Unit test for function split_args

# Generated at 2022-06-13 04:40:27.031132
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo "bar baz') == ['"foo bar baz']
    assert split_args('foo "bar baz\\') == ['"foo bar baz\\']
    assert split_args('foo "bar baz\\"') == ['"foo bar baz\\"']
    assert split_args('foo "bar \" baz"') == ['foo', '"bar \" baz"']
    assert split_args('foo "bar \' baz"') == ['foo', '"bar \' baz"']
    assert split_args("foo 'bar \" baz'") == ["foo", "'bar \" baz'"]



# Generated at 2022-06-13 04:40:32.141526
# Unit test for function split_args
def test_split_args():
    assert split_args("a=1 b=2") == ['a=1', 'b=2']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args('''a=b c='foo bar' d="{{foobar}}" e={{foo}} f={{foo}} g='{{bar}}' h="\\"foo\\"" i="a b"''') == \
        ['a=b', "c='foo bar'", 'd="{{foobar}}"', 'e={{foo}}', 'f={{foo}}', "g='{{bar}}'", 'h="\\"foo\\""', 'i="a b"']

# Generated at 2022-06-13 04:40:42.540845
# Unit test for function split_args
def test_split_args():
    # Test simple split on whitespace
    assert split_args("arg1 arg2 arg3") == ["arg1", "arg2", "arg3"]

    # Test embedding of whitespace in quotes
    assert split_args("arg1 'arg2 with whitespace' arg3") == ["arg1", "arg2 with whitespace", "arg3"]

    # Test that quotes can be nested
    assert split_args('arg1 "arg2 with whitespace \'embedded in quotes\'" arg3') == ["arg1", "arg2 with whitespace 'embedded in quotes'", "arg3"]

    # Test that whitespace is not split inside of jinja2 blocks
    assert split_args("arg1 {{ arg2 with whitespace }} arg3") == ["arg1", "{{ arg2 with whitespace }}", "arg3"]

    # Test that whitespace is

# Generated at 2022-06-13 04:40:51.208981
# Unit test for function split_args
def test_split_args():
    testcases = dict()
    testcases[""] = []
    testcases["a=b"] = ["a=b"]
    testcases["a=b c=d"] = ["a=b", "c=d"]
    testcases['a="b c"'] = ["a=\"b c\""]

    # Test single quotes
    testcases["a='b c'"] = ['a=\'b c\'']
    testcases['a="b \'c d\'"'] = ['a="b \'c d\'"']

    # Test newlines
    testcases['a=1\nb=2'] = ['a=1\n', 'b=2']
    testcases['a=1\nb=\'2\''] = ['a=1\n', 'b=\'2\'']

    # Test escaped newlines