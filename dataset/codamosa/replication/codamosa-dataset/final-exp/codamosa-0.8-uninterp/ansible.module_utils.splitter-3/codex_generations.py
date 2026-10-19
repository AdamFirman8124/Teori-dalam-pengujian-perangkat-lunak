

# Generated at 2022-06-13 04:31:14.470227
# Unit test for function split_args
def test_split_args():

    class TestPair:
        def __init__(self, inp, outp):
            self.inp = inp
            self.outp = outp


# Generated at 2022-06-13 04:31:20.416118
# Unit test for function split_args

# Generated at 2022-06-13 04:31:31.896217
# Unit test for function split_args
def test_split_args():

    params = split_args('a=b c="foo bar" ls')
    assert len(params) == 3
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'
    assert params[2] == 'ls'

    params = split_args('a=b c="foo bar" ls "with space"')
    assert len(params) == 4
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'
    assert params[2] == 'ls'
    assert params[3] == '"with space"'

    params = split_args('a=b c="foo bar" ls \'with space\'')
    assert len(params) == 4
    assert params[0] == 'a=b'

# Generated at 2022-06-13 04:31:38.342441
# Unit test for function split_args
def test_split_args():
    # "Test Unbalanced Quotes"
    try:
        split_args('"foo" bar')
        raise Exception("Expected an exception")
    except Exception:
        pass
    # "Test Unbalanced Quotes"
    try:
        split_args("'foo' bar")
        raise Exception("Expected an exception")
    except Exception:
        pass
    # "Test Balanced Quotes"
    assert split_args('"foo bar" baz') == ['foo bar', 'baz']
    # "Test Balanced Quotes"
    assert split_args("'foo bar' baz") == ['foo bar', 'baz']
    # "Test Unbalanced Braces"
    try:
        split_args('{{ foo }}')
        raise Exception("Expected an exception")
    except Exception:
        pass
    # "Test Unbalanced Br

# Generated at 2022-06-13 04:31:42.960439
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"abc"')
    assert is_quoted("'abc'")
    assert is_quoted("'ab'''c'")
    assert not is_quoted("'ab'''c")
    assert not is_quoted("'ab'''c")
    assert not is_quoted("'ab'''c'f")
    assert not is_quoted("ab'''c'")


# Generated at 2022-06-13 04:31:49.713223
# Unit test for function is_quoted
def test_is_quoted():
    # Empty string
    assert not is_quoted("")
    # Single quote
    assert is_quoted("'Single quote'")
    assert not is_quoted("Single quote'")
    assert is_quoted("'Single quote")
    # Double quote
    assert is_quoted('"Double quote"')
    assert not is_quoted('Double quote"')
    assert is_quoted('"Double quote')


# Generated at 2022-06-13 04:32:01.954697
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('"foo"') == 'foo'
    assert unquote('foo') == 'foo'
    assert unquote('"\\"foo\\""') == '"foo"'
    assert unquote("'foo'") == 'foo'
    assert unquote("'f\\'oo'") == "f'oo"
    assert unquote('"f\\"oo"') == 'f"oo'
    assert unquote('"foo') != '"foo'
    assert unquote('foo"') != 'foo"'
    assert unquote('\\"foo"') != '"foo"'
    assert unquote('"foo\\"') != 'foo"'
    assert unquote('""foo"') != '"foo"'

# Generated at 2022-06-13 04:32:04.145523
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('I\'m a happy string') is False
    assert is_quoted('"I\'m a happy string"') is True


# Generated at 2022-06-13 04:32:11.774836
# Unit test for function unquote
def test_unquote():
    result = unquote('"foo"')
    assert result == 'foo', "should be foo, got %s instead" % result

    result = unquote("'foo'")
    assert result == 'foo', "should be foo, got %s instead" % result

    result = unquote('"foo')
    assert result == '"foo', "should be 'foo', got %s instead" % result

    result = unquote("'foo")
    assert result == "'foo", "should be 'foo', got %s instead" % result

    result = unquote('foo')
    assert result == 'foo', "should be foo, got %s instead" % result

test_unquote()

# Generated at 2022-06-13 04:32:15.297250
# Unit test for function unquote
def test_unquote():
    # files/fileglob.py:test_unquote()
    assert unquote("'test'") == "test"
    assert unquote("'test") == "'test"

# Generated at 2022-06-13 04:32:38.645380
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:32:48.933027
# Unit test for function split_args
def test_split_args():
    import traceback

# Generated at 2022-06-13 04:32:57.714012
# Unit test for function split_args

# Generated at 2022-06-13 04:33:08.127733
# Unit test for function split_args
def test_split_args():
    '''
    Run unit tests for split_args function
    '''
    from ansible.module_utils.common._text import to_bytes
    # shlex.split() is module in Python 2.6+
    import shlex
    try:
        from shlex import split as shlex_split
    except ImportError:
        # Python < 2.6
        shlex_split = shlex.split

    single_quoted_string = "'foo bar'"
    double_quoted_string = '"foo bar"'
    mixed_quoted_string = '"\'foo bar\'"'

    mixed_quote_ansible_argv = ["arg1=foo arg2='foo bar' arg3='foo bar' arg4=bar"]

# Generated at 2022-06-13 04:33:14.407621
# Unit test for function split_args

# Generated at 2022-06-13 04:33:21.709376
# Unit test for function split_args
def test_split_args():
    # TODO: move this unit test in a real unit test file
    argv = ["foo=bar", "baz='this is a \"string\"'", "meh='{\"foo\":\"bar\"}'", "one two three=four"]
    print("\nArguments: %s" % argv)
    print("\nSplitted arguments: %s" % split_args(" ".join(argv)))

# Generated at 2022-06-13 04:33:33.568063
# Unit test for function split_args
def test_split_args():
    args = "a=b c='foo bar' d=\"baz qux\" e={{ foo.bar }} f={{ 'foo bar'.split()|join(' ') }} g={{ 'foo ' ~ bar }}"
    results = split_args(args)
    assert results == ['a=b', "c='foo bar'", 'd="baz qux"', 'e={{ foo.bar }}',
                        "f={{ 'foo bar'.split()|join(' ') }}", "g={{ 'foo ' ~ bar }}"], results

    args = "a=b c='foo bar' d=\"baz qux\" e={{ foo.bar }} f={{ 'foo bar'.split()|join(' ') }} \\\ng={{ 'foo ' ~ bar }}"
    results = split_args(args)

# Generated at 2022-06-13 04:33:45.198032
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a='b c'") == ["a='b c'"]
    assert split_args("a='b\nc'") == ["a='b\nc'"]
    assert split_args("a=\"b\nc\"") == ["a=\"b\nc\""]
    assert split_args("a=\"b c\"") == ["a=\"b c\""]
    assert split_args("a=b c=\"d e\"") == ['a=b', 'c="d e"']
    assert split_args("a=\"b c\" d=\"e f\"") == ['a="b c"', 'd="e f"']

# Generated at 2022-06-13 04:33:55.401494
# Unit test for function split_args
def test_split_args():

    # Test a simple example
    a = "a=1 b=2"
    b = ['a=1', 'b=2']
    assert split_args(a) == b, "simple split test failed"

    # Make sure it works with quotes inside
    a = 'a=1 b="foo bar"'
    b = ['a=1', 'b="foo bar"']
    assert split_args(a) == b, "split with quotes inside test failed"

    # Make sure it works when no spaces exist
    a = 'a=1 b="foo bar"'
    b = ['a=1', 'b="foo bar"']
    assert split_args(a) == b, "split with no spaces test failed"

    # Make sure it works with quotes inside unbalanced
    a = 'a=1 b="foo bar'

# Generated at 2022-06-13 04:34:05.223544
# Unit test for function split_args
def test_split_args():
    '''
    data points for split_args()
    '''

# Generated at 2022-06-13 04:34:27.051807
# Unit test for function split_args
def test_split_args():
    '''
    Test each of the following cases

    1 - normal case
    2 - quoted string
    3 - quoted string with spaces
    4 - quoted string with escaped quotes
    5 - jinja2 templating
    6 - quoted string and jinja2 templating
    '''

# Generated at 2022-06-13 04:34:38.616007
# Unit test for function split_args
def test_split_args():

    # no special quoting/splitting needed, split on spaces
    # make sure we can split on multiple spaces as well
    assert split_args("a=1 b=2") == ['a=1', 'b=2']
    assert split_args("a=1  b=2") == ['a=1', 'b=2']

    # if a value needs to be quoted, make sure the quotes are preserved
    assert split_args("a=1 b='foo bar'") == ['a=1', "b='foo bar'"]

    # args may contain multiple lines, test that as well
    assert split_args("a=1 b='foo bar'\nc=3 d='foo bar'") == ['a=1', "b='foo bar'\nc=3", "d='foo bar'"]

    # test that a newline can be escaped

# Generated at 2022-06-13 04:34:46.114288
# Unit test for function split_args
def test_split_args():
    '''unit tests for pythons function split_args'''
    # assert what we expect to be true
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b c=d") != ['a=b', 'd']
    assert split_args("a=b c=d") != ['a=b', 'c=d', 'e=f']
    assert split_args("a=b 'c d' e={{f}} g {{h}}={{i}}") == ['a=b', "'c d'", 'e={{f}}', 'g', '{{h}}={{i}}']

# Generated at 2022-06-13 04:34:51.015136
# Unit test for function split_args
def test_split_args():
    # passing tests
    assert split_args('"a=b c" "foo bar"') == ['"a=b c"', '"foo bar"']
    assert split_args('"a=b c" "foo bar"') == split_args("'a=b c' 'foo bar'")
    assert split_args('"a=b c" "foo bar"') == split_args('"\'a=b c\'" "\'foo bar\'"')
    assert split_args('"a=b c" "foo bar"') != split_args('"\'a=b c\'" "\'foo bar\' "')
    assert split_args('"a=b c" "foo bar"') != split_args('"\'a=b c\'" "\'foo bar\'" ')

    # failure cases

# Generated at 2022-06-13 04:34:59.494323
# Unit test for function split_args
def test_split_args():
    '''
    Run the following tests to verify correct splitting of args.
    Each test will verify four things:
        1) that the resulting params are as expected
        2) that the number of params returned is as expected
        3) that the number of individual characters in the params matches the original arg length
            (this test is to verify that tokens were not lost or added during splitting)
        4) that params were split at the correct original location in the arg string

    Sometimes tokens will be parsed out of the arg string, look for the
    string 'PARSED' to see where that has occurred.
    '''

    def _split(args, results):
        params = split_args(args)
        if params != results:
            raise Exception("result did not match expected result")
        total_params_string_length = 0
        for param in params:
            total_params

# Generated at 2022-06-13 04:35:08.457134
# Unit test for function split_args
def test_split_args():
    # Test simple string with unquoted spaces
    assert split_args("test1 test2") == ['test1', 'test2']

    # Test string with quoted spaces
    assert split_args("test1 'test2 test3'") == ['test1', 'test2 test3']

    # Test string with quoted spaces, and unquoted spaces
    assert split_args("test1 'test2 test3' test4") == ['test1', 'test2 test3', 'test4']

    # Test string with quoted spaces, and unquoted spaces, and line continuation
    assert split_args("test1 'test2 test3' test4\\\ntest5") == ['test1', 'test2 test3', 'test4\ntest5']

    # Test jinja2 vars in unquoted string

# Generated at 2022-06-13 04:35:19.206236
# Unit test for function split_args
def test_split_args():
    """
    Ensure that split_args works as documented.
    """

    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b 'c=foo bar'") == ['a=b', "'c=foo bar'"]
    assert split_args("a=b 'c={{ foo }}'") == ['a=b', "'c={{ foo }}'"]
    assert split_args("a=b 'c={{ foo }}' d={{ bar }}") == ['a=b', "'c={{ foo }}'", 'd={{ bar }}']

# Generated at 2022-06-13 04:35:25.546133
# Unit test for function split_args
def test_split_args():
    # Test 1:
    # Normal case:
    # Input:
    # argument1 argument2
    # Output:
    # [argument1, argument2]
    assert split_args("argument1 argument2") == ["argument1", "argument2"]

    # Test 2:
    # Normal case:
    # Input:
    # "argument1 argument2"
    # Output:
    # [argument1 argument2]
    assert split_args('"argument1 argument2"') == ["argument1 argument2"]

    # Test 3:
    # Normal case:
    # Input:
    # 'argument1 argument2'
    # Output:
    # [argument1 argument2]
    assert split_args("'argument1 argument2'") == ["argument1 argument2"]

    # Test 4:
    # Normal case:
    # Input:


# Generated at 2022-06-13 04:35:36.511403
# Unit test for function split_args
def test_split_args():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    to_text = lambda x: x
    if not isinstance('foo', str):
        to_text = lambda x: AnsibleUnsafeText(x)
    assert split_args("a='b c' d") == [to_text("a='b c'"), to_text("d")]
    assert split_args("a='b c'\nd") == [to_text("a='b c'"), to_text("d")]
    assert split_args("a='b c'\\\nd") == [to_text("a='b c'"), to_text("d")]
    assert split_args("a=\"b c\" d") == [to_text("a=\"b c\""), to_text("d")]

# Generated at 2022-06-13 04:35:43.925037
# Unit test for function split_args
def test_split_args():

    short_args = "foo=bar baz='hello world' qux='hello world' quxx=1234"
    short_args_split = ['foo=bar', "baz='hello world'", "qux='hello world'", 'quxx=1234']
    assert split_args(short_args) == short_args_split

    # test with a single item
    single_arg = "foo=bar"
    single_arg_split = ['foo=bar']
    assert split_args(single_arg) == single_arg_split

    # test with a single item quoted
    single_arg = "foo='bar'"
    single_arg_split = ["foo='bar'"]
    assert split_args(single_arg) == single_arg_split

    # test with a single item quoted and jinja2
    single_arg

# Generated at 2022-06-13 04:36:19.981869
# Unit test for function split_args
def test_split_args():
    tests = dict()
    tests["a=b c=d"] = ['a=b', 'c=d']
    tests["a=b 'c d'"] = ['a=b', "'c d'"]
    tests['a=b "c d"'] = ['a=b', '"c d"']
    tests["a=1 'b c' d=3"] = ['a=1', "'b c'", 'd=3']
    tests['a=1 "b c" d=3'] = ['a=1', '"b c"', 'd=3']
    tests["a=1 'b c' d=3 'e f'"] = ['a=1', "'b c'", 'd=3', "'e f'"]

# Generated at 2022-06-13 04:36:31.105840
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a="foo bar" c=b') == ['a="foo bar"', 'c=b']
    assert split_args('a=b c="foo\nbar"') == ['a=b', 'c="foo\nbar"']
    assert split_args('a=b c=\'foo\nbar\'') == ['a=b', 'c=\'foo\nbar\'']
    assert split_args('a=b c="foo\nbar" d="fizz buzz"') == ['a=b', 'c="foo\nbar"', 'd="fizz buzz"']

# Generated at 2022-06-13 04:36:42.034312
# Unit test for function split_args
def test_split_args():
    #FIXME: add k=v test
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo \\\'bar\\\'"') == ['a=b', "c=\"foo 'bar'\""]
    assert split_args('a=b c="foo \\"bar\\""') == ['a=b', 'c="foo \\"bar\\""']
    assert split_args('a=b c="foo') == ['a=b', 'c="foo']
    assert split_args('a=b c=\\"foo') == ['a=b', 'c=\\"foo']
    assert split_args('a=b c=\\"foo\\"') == ['a=b', 'c=\\"foo\\"']
   

# Generated at 2022-06-13 04:36:50.944346
# Unit test for function split_args
def test_split_args():

    def is_valid(args, expect):

        results = split_args(args)
        if results != expect:
            raise Exception("failed: argument string '%s' returned '%s' which != '%s'" % (args, results, expect))
        else:
            print("passed: '%s' returned '%s'" % (args, results))

    is_valid("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    is_valid("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    is_valid("a=b 'c=foo bar'", ['a=b', "'c=foo bar'"])

# Generated at 2022-06-13 04:36:59.336291
# Unit test for function split_args
def test_split_args():
    ''' run module as a unit test '''
    import types

    # results of split_args when run with different input

# Generated at 2022-06-13 04:37:10.508654
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):
        def test_escaped_backslash(self):
            # unittest uses \ to escape special characters like \n
            # we want to test an escaped backslash, so we have to double it up
            test_string = 'echo \\\\n'
            result = ['echo', '\\\\n']
            self.assertEqual(split_args(test_string), result)

        def test_empty_string(self):
            self.assertEqual(split_args(""), [])

        def test_one_word(self):
            test_string = 'test'
            result = ['test']
            self.assertEqual(split_args(test_string), result)


# Generated at 2022-06-13 04:37:22.150153
# Unit test for function split_args

# Generated at 2022-06-13 04:37:33.871585
# Unit test for function split_args
def test_split_args():
    params = "foo=bar bam=baz"
    assert split_args(params) == ['foo=bar', 'bam=baz']

    params = "foo=\"bar bar\" baz=bah"
    assert split_args(params) == ['foo="bar bar"', 'baz=bah']

    params = "foo=bar\nbar=foo"
    assert split_args(params) == ['foo=bar\nbar=foo']

    params = "foo=bar\nbar=foo\n"
    assert split_args(params) == ['foo=bar\nbar=foo\n']

    params = "foo=bar bar=baz"
    assert split_args(params) == ['foo=bar', 'bar=baz']

    params = "foo='bar bar' baz=bah"
    assert split_

# Generated at 2022-06-13 04:37:43.832856
# Unit test for function split_args
def test_split_args():
    import unittest
    class TestSplitArgs(unittest.TestCase):
        def test_split_args(self):

            # Split on simple whitespace
            args = "a simple arg string"
            self.assertEqual(split_args(args), args.split())

            # Split on mixed whitespace
            args = """  spaces at front
            mixed newlines and spaces on this line
            """
            correct_result = [
                'spaces',
                'at',
                'front',
                'mixed',
                'newlines',
                'and',
                'spaces',
                'on',
                'this',
                'line'
            ]
            self.assertEqual(split_args(args), correct_result)

            # Split with quotes

# Generated at 2022-06-13 04:37:53.152339
# Unit test for function split_args

# Generated at 2022-06-13 04:39:12.487038
# Unit test for function split_args
def test_split_args():

    # Test all combinations of quoting, (simple) jinja, and line breaks
    # within short command line strings.  These are likely to be small
    # enough so that the initial split on line breaks is unnecessary,
    # but this test is designed to work even when run in a larger
    # environment where that happens.

    from pprint import pprint
    params = None

    def test_params(item):
        # Return True if the given `params` list matches what we
        # expect for the given `item` string.

        # Simple "word" items should produce a single item of
        # the same value.
        if not ('"' in item or "'" in item or ' ' in item):
            return params == [item]

        # Otherwise, there should be multiple items, and the
        # first item should be equal to the given string with
        #

# Generated at 2022-06-13 04:39:18.401872
# Unit test for function split_args
def test_split_args():
    # Testing with double quotes
    args_string = 'a=b c="foo bar"'
    expected_params = ['a=b', 'c="foo bar"']
    assert split_args(args_string) == expected_params

    # Testing with single quotes
    args_string = "a=b c='foo bar'"
    expected_params = ['a=b', "c='foo bar'"]
    assert split_args(args_string) == expected_params

    # Testing with both single and double quotes
    args_string = "a=b c='foo bar' d='bar baz'"
    expected_params = ['a=b', "c='foo bar'", "d='bar baz'"]
    assert split_args(args_string) == expected_params

    # Testing with single and double quotes and spaces in the value
    args_

# Generated at 2022-06-13 04:39:27.305762
# Unit test for function split_args

# Generated at 2022-06-13 04:39:35.819826
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args
    '''
    import sys

    args = "a=b c='d e f' g=\"$h {{ i|d() }} j\" k={{ l|d() }} \"m n\""

    # test the standard result

# Generated at 2022-06-13 04:39:43.336132
# Unit test for function split_args
def test_split_args():
    args = 'a=b c="foo bar" "foo bar"'
    params = split_args(args)

    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'
    assert params[2] == '"foo bar"'

    args = 'a={{a}} "foo bar"'
    params = split_args(args)

    assert params[0] == 'a={{a}}'
    assert params[1] == '"foo bar"'

    args = 'a={{ foo }} "foo bar={{ b }}"'
    params = split_args(args)

    assert params[0] == 'a={{ foo }}'
    assert params[1] == '"foo bar={{ b }}"'


# Generated at 2022-06-13 04:39:53.489110
# Unit test for function split_args

# Generated at 2022-06-13 04:40:02.293002
# Unit test for function split_args

# Generated at 2022-06-13 04:40:09.648227
# Unit test for function split_args
def test_split_args():
    '''Split arguments unit test'''

    import ast

    args_list = []
    args = 'key=value another=one'
    args_list.append((args, ['key=value', 'another=one']))
    args = 'key="value another" another=one'
    args_list.append((args, ['key="value another"', 'another=one']))
    args = 'key=value another="one two"'
    args_list.append((args, ['key=value', 'another="one two"']))
    args = 'key="value another" another="one two"'
    args_list.append((args, ['key="value another"', 'another="one two"']))
    args = 'var={{ foo.bar }} another=one'

# Generated at 2022-06-13 04:40:20.348489
# Unit test for function split_args
def test_split_args():
    # Single line args
    test = 'a=b c="foo bar"'
    result = split_args(test)
    assert result == ['a=b', 'c="foo bar"']

    # Single line args with newlines
    test = 'a=b\nc="foo bar"'
    result = split_args(test)
    assert result == ['a=b\n', 'c="foo bar"']

    # Multiline args
    test = 'a=b\nc="foo\nbar"'
    result = split_args(test)
    assert result == ['a=b\n', 'c="foo\n', 'bar"']

    # Key value pairs
    test = 'a=b c="foo bar"'
    result = dict(x.split("=", 1) for x in split_args(test))
    assert result

# Generated at 2022-06-13 04:40:29.911300
# Unit test for function split_args
def test_split_args():
    result = split_args('michaelfrohlich.cloud.vm_template image="asdfasdf" networks "asdfasdf"')
    assert result == ['michaelfrohlich.cloud.vm_template', 'image="asdfasdf"', 'networks', '"asdfasdf"']

    result = split_args("michaelfrohlich.cloud.vm_template image='asdfasdf' networks 'asdfasdf'")
    assert result == ['michaelfrohlich.cloud.vm_template', 'image=\'asdfasdf\'', 'networks', '\'asdfasdf\'']

    result = split_args("michaelfrohlich.cloud.vm_template image='''asdfasdf''' networks '''asdfasdf'''")