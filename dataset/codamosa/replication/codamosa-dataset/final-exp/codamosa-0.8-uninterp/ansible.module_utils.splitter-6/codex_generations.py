

# Generated at 2022-06-13 04:31:22.249845
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('hello') == ['hello']
    assert split_args('hello "my friend"') == ['hello', '"my friend"']
    assert split_args('hello "my friend" foo=bar a=b c="I am a long \\') == ['hello', '"my friend"', 'foo=bar', 'a=b', 'c="I am a long \\']
    assert split_args('c="I am a long \\') == ['c="I am a long \\']
    assert split_args('"{\\"foo\\": \\"bar\\"}"') == ['"{\\"foo\\": \\"bar\\"}"']
    assert split_args('{{foo}}') == ['{{foo}}']

# Generated at 2022-06-13 04:31:32.371954
# Unit test for function split_args
def test_split_args():
    a = 'no quotes'
    assert split_args(a) == ['no', 'quotes']
    a = '"quoted string"'
    assert split_args(a) == ['quoted string']
    a = 'a=b c="foo bar"'
    assert split_args(a) == ['a=b', 'c="foo bar"']
    a = 'a=b c="foo\nbar"'
    assert split_args(a) == ['a=b', 'c="foo\nbar"']
    a = 'a=b c="foo\nbar"'
    assert split_args(a) == ['a=b', 'c="foo\nbar"']
    a = 'a=b c="foo\n\nbar"'

# Generated at 2022-06-13 04:31:35.502277
# Unit test for function unquote
def test_unquote():
    assert unquote('"abc"') == "abc"
    assert unquote("'abc'") == "abc"
    assert unquote('abc') == "abc"


# Generated at 2022-06-13 04:31:44.069558
# Unit test for function split_args
def test_split_args():
    '''Test the split_args function'''
    args = '''a='1 2' b=3 c="4 5" d={{ foo }} e='{{ foo }}' f="{{ bar }}" g=h {{ i }} "j k" "l" m
    {{ foo }} n=p o='{{ foo }}' p=q q="{{foo}}" "r s" "t"'''
    try:
        params = split_args(args)
    except Exception:
        raise AssertionError('Could not split args: {0}'.format(args))

    # Check that each key-value pair is in the resulting list
    # and that there are no extra key-value pairs

# Generated at 2022-06-13 04:31:47.763518
# Unit test for function unquote
def test_unquote():
    assert('foo bar' == unquote('"foo bar"'))
    assert('foo bar' == unquote("'foo bar'"))
    assert('foo bar' == unquote("foo bar"))

# Generated at 2022-06-13 04:31:58.766147
# Unit test for function split_args
def test_split_args():
    '''
    A bunch of test cases for the split_args function.
    '''
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('"a=b c=foo bar"') == ['"a=b c=foo bar"']
    assert split_args('a=b c="foo bar\\"') == ['a=b', 'c="foo bar\\"']
    assert split_args('a=b c="foo bar\\""') == ['a=b', 'c="foo bar\\""']
    assert split_args('a=b c="foo bar" d="') == ['a=b', 'c="foo bar"', 'd="']

# Generated at 2022-06-13 04:32:09.645167
# Unit test for function unquote
def test_unquote():
    assert unquote("") == ""
    assert unquote("'") == "'"
    assert unquote("\"") == "\""
    assert unquote("\"\"") == ""
    assert unquote("''") == ""
    assert unquote("'abc'") == "abc"
    assert unquote("\"abc\"") == "abc"
    assert unquote("\"'abc'\"") == "'abc'"
    assert unquote("'\"abc\"'") == "\"abc\""
    assert unquote("\"'abc'\"") == "'abc'"
    assert unquote("'''\"abc\"'''") == "'\"abc\"'"
    assert unquote("\"'abc\"'") == "'abc"



# Generated at 2022-06-13 04:32:20.392604
# Unit test for function split_args
def test_split_args():
    ''' tests the split arguments function '''

    tests = dict()
    tests['simple'] = ("a b c", ['a', 'b', 'c'])
    tests['var'] = ("a=b c=d", ['a=b', 'c=d'])
    tests['var_quotes'] = ('a=b c="foo bar"', ['a=b', 'c="foo bar"'])
    tests['print'] = ("a=b c='{{ foo }}'", ['a=b', "c='{{ foo }}'"])
    tests['block'] = ("a=b c='{% foo %}'", ['a=b', "c='{% foo %}'"])

# Generated at 2022-06-13 04:32:27.329019
# Unit test for function is_quoted
def test_is_quoted():
    if not is_quoted('"abc"'):
        print('ERROR: "abc" should be quoted')
    if not is_quoted("'abc'"):
        print('ERROR: \'abc\' should be quoted')
    if is_quoted('"a\'"'):
        print('ERROR: "a\'" should not be quoted')
    if is_quoted('a'):
        print('ERROR: a should not be quoted')

# Generated at 2022-06-13 04:32:38.685901
# Unit test for function split_args
def test_split_args():
    import os
    import sys
    import yaml
    import json
    import pytest
    from ansible.compat.tests.mock import patch

    if not os.path.exists(sys.path[0] + "/test/units/modules/utils/test_split_args.yml"):
        pytest.skip("Can't find test/units/modules/utils/test_split_args.yml, not testing function split_args.")

    with open(sys.path[0] + "/test/units/modules/utils/test_split_args.yml", "r") as test_cases_file:
        test_cases = yaml.safe_load(test_cases_file)

# Generated at 2022-06-13 04:32:58.376717
# Unit test for function split_args

# Generated at 2022-06-13 04:33:08.630884
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    DATA = "arg1=val1 arg2=val2 'arg 3=val 3'"
    EXPECTED = ['arg1=val1', 'arg2=val2', "'arg 3=val 3'"]
    RESULT = split_args(DATA)
    assert RESULT == EXPECTED, "result was %s" % RESULT


# Generated at 2022-06-13 04:33:14.801553
# Unit test for function split_args
def test_split_args():
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'])
    assert(split_args('a=b c="foo  bar"') == ['a=b', 'c="foo  bar"'])
    assert(split_args('a=b c="foo\\" bar"') == ['a=b', 'c="foo\\" bar"'])
    assert(split_args('a=b c="foo bar\\""') == ['a=b', 'c="foo bar\\""'])
    assert(split_args('a=b c="foo\\\\\\" bar"') == ['a=b', 'c="foo\\\\\\" bar"'])

# Generated at 2022-06-13 04:33:27.523897
# Unit test for function split_args
def test_split_args():
    ''' unit test for function split_args '''

    # This is from a failed task from #2810.  It represents a difference between
    # shlex.split and split_args with respect to unescaped input.
    import shlex
    inp = 'apt-get -y -o "Dpkg::Options::=--force-confold" install python-software-properties'
    expected = ['apt-get', '-y', '-o', '"Dpkg::Options::=--force-confold"', 'install', 'python-software-properties']
    assert split_args(inp) == expected
    assert shlex.split(inp) == ['apt-get', '-y', '-o', "Dpkg::Options::=--force-confold", 'install', 'python-software-properties']

    # This is from a failed

# Generated at 2022-06-13 04:33:38.925846
# Unit test for function split_args
def test_split_args():
    data = """arg1 arg2=value arg3="a b" arg4='a b' arg5={{ foo }} arg6={{ foo | default('bar') }} arg7={{ ' ' }} arg8='a b=c' arg9="a b=c" arg10='a b=c' arg11="a 'b'" arg12='a "b"' arg13="a 'b' 'c'" arg14='a "b" "c"' arg15="a 'b' arg14='a "b" "c"'" arg16="a" arg17='a' arg18="a b" arg19={{ {{ {{a}} }} }} arg20='a b' arg21=a\
b arg22='a
b'"""
    # TODO: implement proper unit testing
    split_args(data)



# Generated at 2022-06-13 04:33:51.195877
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('a=b') == ['a=b']
    assert split_args('a="b c"') == ['a="b c"']
    assert split_args('a=b "c d"') == ['a=b', '"c d"']
    assert split_args("a='b c'") == ["a='b c'"]
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b c='d e'") == ['a=b', "c='d e'"]
    assert split_args("a=b 'c d'") == ['a=b', "'c d'"]

# Generated at 2022-06-13 04:34:00.743326
# Unit test for function split_args

# Generated at 2022-06-13 04:34:10.200557
# Unit test for function split_args

# Generated at 2022-06-13 04:34:20.082981
# Unit test for function split_args
def test_split_args():
    import pdb
    import sys
    # pdb.Pdb(stdin=sys.__stdin__, stdout=sys.__stderr__).set_trace()
    assert split_args("foo bar baz") == ["foo", "bar", "baz"]


# from ansible.module_utils.remote_management.hpsa import split_args
# example input: "a=b c='foo bar'"
# example output: ['a=b', 'c='foo bar'']
# ansible/test/units/module_utils/test_remote_management_hpsa.py
# def test_split_args():
#     results = split_args("a=b c='foo bar' d=\"test'jkl\"")
#     assert results == ['a=b', "c='foo bar'", "d=\"test'

# Generated at 2022-06-13 04:34:29.092820
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\"\nd=\"foo bar\"\ne=\"foo bar\"") == ['a=b c="foo bar"', 'd="foo bar"', 'e="foo bar"']
    assert split_args("a=b c=\"foo \\\"bar\\\"\"\nd=\"foo bar\"\ne=\"foo bar\"") == ['a=b c="foo \\"bar\\""', 'd="foo bar"', 'e="foo bar"']

# Generated at 2022-06-13 04:34:46.942758
# Unit test for function split_args
def test_split_args():
    '''
    Test the splitting of args, where we expect to see
    a list of arguments with quotes and jinja2 blocks
    joined back together as if the initial string had
    never been split.
    '''
    expected = ['a=b', 'c="foo bar"', 'de f', 'g="hi"']
    input = 'a=b\nc="foo bar"\n de f\n  g="hi" '
    result = split_args(input)
    assert result == expected
    expected = ['a=b', 'c="foo', 'bar"', 'de f', 'g="hi"']
    input = 'a=b\nc="foo\nbar"\n de f\n  g="hi" '
    result = split_args(input)
    assert result == expected

# Generated at 2022-06-13 04:34:57.202810
# Unit test for function split_args
def test_split_args():
    """Testcases for the split_args function"""

    # simple cases
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo') == ['foo']

    # spaces in jinja2 blocks
    assert split_args('{{ foo }}') == ['{{ foo }}']
    assert split_args('{{ foo }} {{ bar }}') == ['{{ foo }}', '{{ bar }}']
    assert split_args('{{ "foo bar" }}') == ['{{ "foo bar" }}']
    assert split_args('{{ foo }}bar') == ['{{ foo }}bar']
    assert split_args('{{ foo }} bar') == ['{{ foo }}', 'bar']
    assert split_args('{{ foo }} {% bar %}') == ['{{ foo }}', '{% bar %}']

# Generated at 2022-06-13 04:35:07.670059
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest
    import ansible.module_utils.basic


# Generated at 2022-06-13 04:35:18.092584
# Unit test for function split_args

# Generated at 2022-06-13 04:35:26.208372
# Unit test for function split_args
def test_split_args():
    args = 'key=value another-key=another-value "a=b c=d"'
    result = split_args(args)
    assert result == ['key=value', 'another-key=another-value', 'a=b c=d'], result

    args = 'single-arg-without-spaces-or-equals'
    result = split_args(args)
    assert result == [args], result

    args = '{{ "a=b c=d" }}'
    result = split_args(args)
    assert result == [args], result

    args = "a=b 'c=d e=f'"
    result = split_args(args)
    assert result == [args], result

    args = 'a=b "c=d\ne=f"'
    result = split_args(args)

# Generated at 2022-06-13 04:35:37.184808
# Unit test for function split_args
def test_split_args():
    # We test a command line with several situations.
    # We include all the following characters: " ' ( ) { } [ ] \ \t \n
    # as well as variable expansion, in single/double quotes and braces, as well as unquoted.
    # The variable expansion characters are in the variable name, so we aren't testing variable syntax
    cmd = '"{var}" "nested \\"quotes\\"" \'{var}\' \'nested single\\\'quotes\\\'\' braced${{var}} "\\"double\\\\quote\\"\\t\\n" (parens $(((( )) )) {} \[brackets\] \\backslash)'
    params = split_args(cmd)
    # expected output: ['{"var"}', '"nested \\"quotes\\""', "'{var}'", "'nested single\\'quotes\\''

# Generated at 2022-06-13 04:35:46.764443
# Unit test for function split_args
def test_split_args():
    import sys
    #test empty string
    assert [] == split_args('')

    #test no jinja2 blocks
    assert ['foo', 'bar'] == split_args('foo bar')

    #test no jinja2 blocks with quotes
    assert ['foo', 'bar baz'] == split_args('foo "bar baz"')

    #test a jinja2 block with lots of whitespace
    assert ['foo', '{{', 'bar', '   ', 'baz', '}}'] == split_args('foo {{  bar   baz   }}')

    #test a jinja2 block with lots of whitespace and quotes
    assert ['foo', '{{', 'bar', '   ', 'baz', '}}', 'boo'] == split_args('foo {{  bar   baz   }}   boo')

    #test a

# Generated at 2022-06-13 04:35:55.494188
# Unit test for function split_args
def test_split_args():
    ''' test cases for splitting args '''
    def _test(args, exp):
        ''' assert that args is split into exp '''
        res = split_args(args)
        if res != exp:
            raise AssertionError('failed to split args. got [%s], expected [%s] from [%s]' % (res, exp, args))
    _test('', [])
    _test('a=b c=d', ['a=b', 'c=d'])
    _test('a=b "c d"', ['a=b', '"c d"'])
    _test('a=b "c d" e=f', ['a=b', '"c d"', 'e=f'])

# Generated at 2022-06-13 04:36:03.723486
# Unit test for function split_args
def test_split_args():
    """Run a simple unit test for this module"""
    import json
    print("=== testing args split ===")

# Generated at 2022-06-13 04:36:15.385967
# Unit test for function split_args

# Generated at 2022-06-13 04:36:37.199136
# Unit test for function split_args

# Generated at 2022-06-13 04:36:41.860721
# Unit test for function split_args
def test_split_args():
    '''
    Test for split_args
    '''


# Generated at 2022-06-13 04:36:50.811524
# Unit test for function split_args

# Generated at 2022-06-13 04:36:59.726131
# Unit test for function split_args
def test_split_args():
    '''Test split_args'''


# Generated at 2022-06-13 04:37:11.208960
# Unit test for function split_args
def test_split_args():
    def t(args,result):
        args_split = split_args(args)
        if result != args_split:
            print("FAILED")
            print("args: %s" % args)
            print("need: %s" % result)
            print("got:  %s" % args_split)
            raise Exception("split_args test failed")
    print("starting split_args tests")

    t("a=b c=\"foo bar\"", ["a=b", "c=\"foo bar\""])

    # make sure quotes can be escaped
    t("\"foo bar\"", ["\"foo bar\""])
    t("\"foo \\\" bar\"", ["\"foo \\\" bar\""])
    t("\"\\\"\"", ["\"\\\"\""])

    # make sure we don't get fooled by unmatched quotes

# Generated at 2022-06-13 04:37:22.646613
# Unit test for function split_args

# Generated at 2022-06-13 04:37:34.468347
# Unit test for function split_args
def test_split_args():
    def check(input, expected):
        result = split_args(input)
        if result != expected:
            raise Exception("split_args failed on input=%s, expected=%s, got %s" % (input, expected, result))

    check("foo=bar baz='boo far'", ['foo=bar', "baz='boo far'"])
    check("foo=bar baz='boo far' bam='bar'", ['foo=bar', "baz='boo far'", "bam='bar'"])
    check("foo=bar baz='boo far' bam='bar'", ['foo=bar', "baz='boo far'", "bam='bar'"])

# Generated at 2022-06-13 04:37:44.347562
# Unit test for function split_args
def test_split_args():
    '''
    This function tests the function split_args
    '''
    def _convert_args_to_params(args):
        '''
        This function converts an array of arguments to a list of parameters.
        The parameters are the same as the arguments expect they are split on the delim "="
        '''
        params = {}
        for arg in args:
            items = arg.split("=", 1)
            if len(items) == 2:
                params[items[0]] = items[1]
        return params

    def _test_params(string_to_parse, expected_params):
        '''
        This function handle the test for the string_to_parse and the expected_params.
        '''
        # Parse the given string
        params = split_args(string_to_parse)
        # Convert params to

# Generated at 2022-06-13 04:37:53.486107
# Unit test for function split_args
def test_split_args():
    # basic case
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]

    # nested jinja2
    test_string = '''run_once: true

shell: "{{ ansible_env.SHELL }}"

test: "{{ test_var }}"

test2: "{{ test_var2 }}"
'''
    assert split_args(test_string) == ['run_once:', 'true',
                                       'shell:', '"{{ ansible_env.SHELL }}"',
                                       'test:', '"{{ test_var }}"',
                                       'test2:', '"{{ test_var2 }}"\n']

    # multiple jinja2 blocks and other types

# Generated at 2022-06-13 04:38:04.216132
# Unit test for function split_args

# Generated at 2022-06-13 04:38:53.168466
# Unit test for function split_args

# Generated at 2022-06-13 04:39:03.433087
# Unit test for function split_args
def test_split_args():
    # split_args Examples:
    # a=b c="foo bar"
    # ['a=b', 'c="foo bar"']
    # a=b c="foo bar d
    # ef"
    # ['a=b', 'c="foo bar\ndef"']
    # "foo bar d
    # ef"
    # ['foo bar\ndef']

    # Simple test
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    # Test that spaces inside quotes are preserved
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    # Test that newlines inside quotes are preserved.

# Generated at 2022-06-13 04:39:12.809538
# Unit test for function split_args
def test_split_args():
    '''
    Run split arguments test suite
    '''

# Generated at 2022-06-13 04:39:18.544959
# Unit test for function split_args
def test_split_args():
    ''' return list of split arguments used with module '''
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\" # comment d=\"{{ foo }}\" e=\"{{ foo }}\'bar\'{{ baz }}\"") == ['a=b', 'c="foo bar"', "# comment", 'd="{{ foo }}"', 'e="{{ foo }}\'bar\'{{ baz }}"']

# Generated at 2022-06-13 04:39:27.303233
# Unit test for function split_args
def test_split_args():
    args = "key1=value1   key2='value 2'  key3=value3"
    params = split_args(args)
    assert isinstance(params, list)
    assert 'key1=value1' in params
    assert 'key2=\'value 2\'' in params
    assert 'key3=value3' in params
    assert len(params) == 3
    assert params[2] == 'key3=value3'

    # Split newlines
    args = ("key1=value1 \n"
            "key2='value 2' \n"
            "key3=value3")
    params = split_args(args)
    assert isinstance(params, list)
    assert 'key1=value1' in params
    assert 'key2=\'value 2\'' in params

# Generated at 2022-06-13 04:39:35.820165
# Unit test for function split_args
def test_split_args():

    from nose.tools import assert_equals

    # Basic list of args
    test = '''a=b c="foo bar"' "d 'e f'" "q=r s=t"'''
    results = split_args(test)
    assert_equals(results, ['a=b', 'c="foo bar"', "'d 'e f'", '"q=r s=t"'])

    # Jinja2 blocks
    test = '''"{{ foo }}" '{{bar}}' "{{ baz }}"' "{{ qux }}" '{{ foobar }}' "{{ barbaz }}"' "{{ quxbaz }}"'''
    results = split_args(test)

# Generated at 2022-06-13 04:39:41.874554
# Unit test for function split_args
def test_split_args():
    import unittest

    class TestSplitArgs(unittest.TestCase):

        def setUp(self):
            self.args1 = "key=value"
            self.args2 = "that equal=sign is escaped"
            self.args3 = "a = b = c"
            self.args4 = "a=b c=d"
            self.args5 = "a=b c='foo bar'"
            self.args6 = "a=b c=d e='foo bar'"
            self.args7 = "a=b c=d e='foo bar' f=g"
            self.args8 = "a=b c=d e='foo bar baz' f=g"
            self.args9 = "a=b c=d e='foo 'bar' baz' f=g"
            self.args10

# Generated at 2022-06-13 04:39:52.982769
# Unit test for function split_args

# Generated at 2022-06-13 04:40:01.860338
# Unit test for function split_args
def test_split_args():
    '''
    Run a series of tests for the split_args function,
    in order to make sure it works as expected.
    '''
    import unittest

    class TestSplitArgs(unittest.TestCase):

        def test_split_args_no_args(self):
            '''
            Test the split_args function with an empty string,
            to make sure it returns an empty list.
            '''
            result = split_args('')
            self.assertEqual(result, [])

        def test_split_args_simple_args(self):
            '''
            Test the split_args function with a simple string with
            some args, to make sure it splits the args properly.
            '''
            result = split_args('arg1 arg2 arg3')

# Generated at 2022-06-13 04:40:12.146132
# Unit test for function split_args
def test_split_args():
    if not split_args('"foo bar"') == ['foo bar']:
        print('[unittest_split_args] Failed on: "foo bar"')
    if not split_args('{{foo}} "bar baz"') == ['{{foo}}', 'bar baz']:
        print('[unittest_split_args] Failed on: {{foo}} "bar baz"')
    if not split_args('{{foo}} "bar baz" {{blammo}}') == ['{{foo}}', 'bar baz', '{{blammo}}']:
        print('[unittest_split_args] Failed on: {{foo}} "bar baz" {{blammo}}')