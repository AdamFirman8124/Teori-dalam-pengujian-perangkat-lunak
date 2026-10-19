

# Generated at 2022-06-13 04:31:13.053297
# Unit test for function unquote
def test_unquote():
    s = 'foo'
    result = unquote(s)
    assert result == s

    s = '"foo"'
    result = unquote(s)
    assert result == 'foo'

    s = "foo'"
    result = unquote(s)
    assert result == s

    s = '"foo'
    result = unquote(s)
    assert result == s


# Generated at 2022-06-13 04:31:22.195403
# Unit test for function split_args

# Generated at 2022-06-13 04:31:27.524325
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted("")
    assert not is_quoted("foo")
    assert is_quoted("\"foo\"")
    assert is_quoted("\"foo")
    assert is_quoted("foo\"")
    assert is_quoted("'foo'")
    assert is_quoted("'foo")
    assert is_quoted("foo'")


# Generated at 2022-06-13 04:31:31.882305
# Unit test for function unquote
def test_unquote():
    assert unquote('""') == ''
    assert unquote('"Unquoted"') == 'Unquoted'
    assert unquote('""""') == '""'
    assert unquote('"""Unquoted"""') == '"Unquoted"'
    assert unquote('""""""') == '""""'
    assert unquote('"\"Quoted\""') == '"Quoted"'
    assert unquote('"\"\"Quoted\"\""') == '"\"Quoted\""'
    assert unquote('""\"Quoted\"""') == '"Quoted"'

    assert unquote("''") == ''
    assert unquote("'Unquoted'") == 'Unquoted'
    assert unquote("''''") == "''"
    assert unquote("'''Unquoted'''") == "'Unquoted'"
    assert un

# Generated at 2022-06-13 04:31:42.495842
# Unit test for function split_args
def test_split_args():

    from ansible.module_utils.six import PY2
    from ansible.module_utils import basic
    import sys

    class TestModule(basic.AnsibleModule):
        def __init__(self, *args, **kwargs):
            basic.AnsibleModule.__init__(self, *args, **kwargs)

    # test with a command that has a quoted arg
    cmd_test1 = "test cmd 'this is a quoted arg'"
    params = split_args(cmd_test1)
    # the params should be length 2, the first being the command, the second being the quoted arg
    # the second arg should have a single quote as the first character (to signify it was quoted)

# Generated at 2022-06-13 04:31:53.805562
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a=b c=\"foo bar\"") == [u"a=b", u"c=\"foo bar\""]
    assert split_args(u"a=b c=\"foo bar\" d='foo bar'") == [u"a=b", u"c=\"foo bar\"", u"d='foo bar'"]
    assert split_args(u"a=b c=\"foo \\\"bar\\\"\" d='foo \\\"bar\\\"'") == [u"a=b", u"c=\"foo \\\"bar\\\"\"", u"d='foo \\\"bar\\\"'"]

# Generated at 2022-06-13 04:32:05.713774
# Unit test for function split_args

# Generated at 2022-06-13 04:32:15.080216
# Unit test for function split_args
def test_split_args():
    '''
    (module_utils.basic.py) split args Unit tests
    '''

# Generated at 2022-06-13 04:32:22.214809
# Unit test for function split_args
def test_split_args():
    def should_not_raise(arg, exp_out):
        if exp_out != split_args(arg):
            raise AssertionError("split_args('%s') -> %s, expected %s" % (arg, split_args(arg), exp_out))
        if exp_out != split_args(arg+'\n'):
            raise AssertionError("split_args('%s\\n') -> %s, expected %s" % (arg, split_args(arg+'\n'), exp_out))
    def should_raise(arg):
        try:
            split_args(arg)
        except:
            return
        raise AssertionError("split_args('%s') failed to raise an exception" % arg)

    should_not_raise("a b c", ["a", "b", "c"])

# Generated at 2022-06-13 04:32:30.065658
# Unit test for function unquote
def test_unquote():
    test_cases = [
        ('"hello"', 'hello'),
        ('hello', 'hello'),
        ('"hello', '"hello'),
        ('hello"', 'hello"'),
        ('\'hello\'', 'hello'),
        ('\'hello', '\'hello'),
        ('hello\'', 'hello\''),
        ('"hello\'', '"hello\''),
        ('\'hello"', '\'hello"'),
    ]
    for t in test_cases:
        assert unquote(t[0]) == t[1]

# Generated at 2022-06-13 04:32:50.699717
# Unit test for function split_args
def test_split_args():

    tests = [
        ("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"']),
        ("a=b\\\nc='foo bar'", ['a=b\nc=\'foo bar\'']),
        ("a=b d='foo bar'", ['a=b', "d='foo bar'"]),
    ]

    for args, result in tests:
        assert split_args(args) == result

    # unquote tests

# Generated at 2022-06-13 04:33:01.766605
# Unit test for function split_args

# Generated at 2022-06-13 04:33:10.732831
# Unit test for function split_args

# Generated at 2022-06-13 04:33:16.643248
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\" d={{ foo }}") == ['a=b', 'c="foo bar"', 'd={{', 'foo', '}}']
    assert split_args("a=b c=\"foo bar\" d={{ foo }} e=\"{{ foo }}\"") == ['a=b', 'c="foo bar"', 'd={{', 'foo', '}}', 'e="{{', 'foo', '}}"']

# Generated at 2022-06-13 04:33:29.154465
# Unit test for function split_args
def test_split_args():
    '''
    This function contains tests for the function `split_args`.
    '''
    class TestCase:
        def __init__(self, name, input, expected):
            self.name = name
            self.input = input
            self.expected = expected

# Generated at 2022-06-13 04:33:40.334513
# Unit test for function split_args
def test_split_args():
    assert split_args("a=1 b=2") == ["a=1", "b=2"]
    assert split_args("a='b c'") == ['a=\'b c\'']
    assert split_args("a='b c' d='e f'") == ['a=\'b c\'', 'd=\'e f\'']
    assert split_args("a='b \"c\" d'") == ['a=\'b "c" d\'']
    assert split_args("a='b c' 'd e'") == ['a=\'b c\'', "'d e'"]
    assert split_args("a='b c'\n'd e'") == ['a=\'b c\'\n\'d e\'']

# Generated at 2022-06-13 04:33:52.361469
# Unit test for function split_args
def test_split_args():
    ''' test the quick and dirty args splitting'''

# Generated at 2022-06-13 04:34:02.581001
# Unit test for function split_args

# Generated at 2022-06-13 04:34:08.394560
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.common.collections import TypeMapping
    import os

    # test_cases is a file with a testcase in each line of the form
    # <testcase_description>,<function_argument>,<function_expected_return>
    test_cases_file = os.path.dirname(__file__) + '/../../test/utils/testcases/split_args'
    try:
        test_cases = open(test_cases_file, 'r').readlines()
    except:
        print('WARNING: Could not read testcase file ' + test_cases_file + '. Testcase file must be in utils/testcases/ directory')
        return

    # test_case_result contains the <function_argument>:<function_expected_return> pairs
    test_case_result = TypeMapping()
    #

# Generated at 2022-06-13 04:34:14.698924
# Unit test for function split_args
def test_split_args():
    # simple args
    assert split_args('a=1 b="foo bar"') == ['a=1', 'b="foo bar"']

    # embedded spaces
    assert split_args('a=1 b="foo bar"') == ['a=1', 'b="foo bar"']

    # escaped quotes
    assert split_args('a=1 b="foo \\"bar\\""') == ['a=1', 'b="foo \\"bar\\""']

    # single quoted
    assert split_args("a=1 b='foo bar'") == ['a=1', "b='foo bar'"]

    # unbalanced quotes
    try:
        split_args("a=1 b='foo bar")
        raise AssertionError('Unbalanced quote did not cause exception')
    except Exception:
        pass

    # jinja2 blocks
   

# Generated at 2022-06-13 04:34:31.573651
# Unit test for function split_args
def test_split_args():
    args = 'a=b c="foo bar"'
    params = split_args(args)
    assert len(params) == 2
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'

    args = 'a=b c="foo \\\\\\\\ bar"'
    params = split_args(args)
    assert len(params) == 2
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo \\\\\\\\ bar"'

    args = 'a=b c="foo bar'
    try:
        params = split_args(args)
    except Exception:
        pass

    args = 'a=b c="foo bar'
    try:
        params = split_args(args)
    except Exception:
        pass


# Generated at 2022-06-13 04:34:41.781927
# Unit test for function split_args

# Generated at 2022-06-13 04:34:53.115578
# Unit test for function split_args
def test_split_args():
    # Test basic module run
    args = 'a=b c="foo bar"'
    result = ['a=b', 'c="foo bar"']
    assert split_args(args) == result

    # Test quote inside module args
    args = 'a=b c="foo bar"'
    result = ['a=b', 'c="foo bar"']
    assert split_args(args) == result

    # Test jinja2 and quotes in module args
    args = 'a={{ b }} c="{{ foo }} bar"'
    result = ['a={{ b }}', 'c="{{ foo }} bar"']
    assert split_args(args) == result

    # Test multiple jinja2 and quotes in module args
    args = 'a={{ b }} c="{{ foo }} bar" d="{{ foo }} bar"'

# Generated at 2022-06-13 04:35:05.141990
# Unit test for function split_args
def test_split_args():

    def parse_split_args(args):
        params = split_args(args)
        return [unquote(x) for x in params]

    assert parse_split_args('a=b c="foo bar"') == ['a=b', 'c=foo bar']
    assert parse_split_args('a=b c="foo \'bar\'"') == ['a=b', 'c=foo \'bar\'']
    assert parse_split_args('a=b c="foo \'bar\'"') == ['a=b', 'c=foo \'bar\'']
    assert parse_split_args('a=b c="foo \'bar\' \"baz\""') == ['a=b', 'c=foo \'bar\' "baz"']

# Generated at 2022-06-13 04:35:13.748610
# Unit test for function split_args
def test_split_args():
    print("in test_split_args")

# Generated at 2022-06-13 04:35:23.410536
# Unit test for function split_args
def test_split_args():
    # basic list of params
    data = 'a=1 b=2'

    # split on space
    result = split_args(data)
    assert len(result) == 2
    assert 'a=1' in result
    assert 'b=2' in result

    # basic params with quotes, whitespace, and newlines
    data = 'a="1 2" b="3\n4" c=5'
    result = split_args(data)
    assert len(result) == 3
    assert 'a="1 2"' in result
    assert 'b="3\n4"' in result
    assert 'c=5' in result

    # now with escaped quotes and escapes
    data = 'a="1 \"2\"" b=\\"3\\" c=\\ d="4\\'
    result = split_args(data)
   

# Generated at 2022-06-13 04:35:33.680507
# Unit test for function split_args
def test_split_args():
    "This is just a sanity check, not a full test."
    assert split_args("a=1 b=2 c='foo bar' d=\"{{ foo }}\"") == ['a=1', 'b=2', 'c=\'foo bar\'', 'd="{{ foo }}"']
    assert split_args("a=1 b=2 c='foo bar' d=\"{{ foo }}\"") == split_args("a=1\n b=2\n c='foo bar' d=\"{{ foo }}\"")
    assert split_args("a=1  b=2 c='foo bar' d=\"{{ foo }}\"") == split_args("a=1\n b=2\n c='foo bar' d=\"{{ foo }}\"")

# Generated at 2022-06-13 04:35:42.599758
# Unit test for function split_args

# Generated at 2022-06-13 04:35:49.254127
# Unit test for function split_args
def test_split_args():
    ''' unit test for split_args '''

    # check a simple case
    assert split_args("foo bar biz baz") == ['foo', 'bar', 'biz', 'baz']

    # make sure we can split on newlines
    assert split_args("foo=bar\nbiz=baz") == ['foo=bar', 'biz=baz']

    # make sure we can split on newlines
    assert split_args("foo=bar\nbiz=baz\n") == ['foo=bar', 'biz=baz']

    # use quotes and make sure they are preserved
    assert split_args("foo='bar biz' baz='spam'") == ['foo=\'bar biz\'', 'baz=\'spam\'']

    # make sure we can handle quotes inside of jinja2 {{ }} blocks
   

# Generated at 2022-06-13 04:35:57.662127
# Unit test for function split_args
def test_split_args():

    # simple test case
    args = "foo=bar baz=\"{{ foo }} and {{ bar }}\""
    params = split_args(args)

    assert params[0] == 'foo=bar'
    assert params[1] == 'baz="{{ foo }} and {{ bar }}"'

    # simple test case with empty list of args
    args = ""
    params = split_args(args)

    assert params == []

    # when the unquoted params are split over a newline, reassembly works
    args = "foo=bar baz=\"{{ foo }} and {{ bar }}\""
    params = split_args(args)

    assert params[0] == 'foo=bar'
    assert params[1] == 'baz="{{ foo }} and {{ bar }}"'


# Generated at 2022-06-13 04:36:32.490403
# Unit test for function split_args
def test_split_args():
    '''
    Tests for function split_args

    Includes cases that should split, cases that shouldn't, and various random
    edge cases.
    '''
    import random
    import string

    # Cases that should split, and what they should be split into

# Generated at 2022-06-13 04:36:43.122841
# Unit test for function split_args
def test_split_args():
    # TODO: Use a test framework to run this unit test
    import json
    data = '''a=b c="d e" f='g h' i="j'k'l" m='n"o"p'\nq="r''s"'''
    result = split_args(data)
    assert result == ['a=b', 'c="d e"', "f='g h'", "i=\"j'k'l\"", 'm=\'n"o"p\'', 'q="r\'\'s"']

    # Here we use the "json" module to make sure the output are real strings/lists.
    # Otherwise, the assert would check for only the same type, not the same object
    result_json = json.dumps(result)

# Generated at 2022-06-13 04:36:52.360824
# Unit test for function split_args

# Generated at 2022-06-13 04:37:00.185135
# Unit test for function split_args
def test_split_args():
    '''
    this test method is used during development and when $ python unit tests
    is run from the root of the source tree.
    '''
    assert split_args("foo='bar baz'") == ["foo='bar baz'"]
    assert split_args("foo='bar baz' id=5") == ["foo='bar baz'", 'id=5']
    assert split_args("foo='bar baz' id=5 name=foo") == ["foo='bar baz'", 'id=5', 'name=foo']
    assert split_args("foo='bar baz' name=foo") == ["foo='bar baz'", 'name=foo']
    assert split_args("foo=\"bar baz\" name=foo") == ['foo="bar baz"', 'name=foo']

# Generated at 2022-06-13 04:37:11.804077
# Unit test for function split_args
def test_split_args():
    # simple test
    (rc, out, err) = split_args("a=b c=d")
    assert rc == ['a=b', 'c=d']

    # simple test
    (rc, out, err) = split_args("a=b c=d e=f")
    assert rc == ['a=b', 'c=d', 'e=f']

    # simple test
    (rc, out, err) = split_args("a=b c=d 'e=f'")
    assert rc == ['a=b', 'c=d', 'e=f']

    # simple test
    (rc, out, err) = split_args("a=b c=d \"e=f\"")
    assert rc == ['a=b', 'c=d', 'e=f']

    # simple test

# Generated at 2022-06-13 04:37:23.083031
# Unit test for function split_args
def test_split_args():
    res = split_args('foo="bar baz"')
    assert res == ['foo=bar baz']
    res = split_args('foo="bar baz" noquote=foobar')
    assert res == ['foo=bar baz', 'noquote=foobar']
    res = split_args('foo="bar \\"baz\\""')
    assert res == ['foo=bar "baz"']
    res = split_args('foo="bar \\"baz\\""')
    assert res == ['foo=bar "baz"']
    res = split_args('foo="bar \\"baz\\\\""')
    assert res == ['foo=bar "baz\\"']
    res = split_args('foo="bar \\\\"baz\\\\""')
    assert res == ['foo=bar \\"baz\\"']
   

# Generated at 2022-06-13 04:37:34.849382
# Unit test for function split_args
def test_split_args():
    ''' simple unit tests for function split_args '''

    def assert_args_equal(expected, input):
        actual = split_args(input)
        assert expected == actual, "Expected '%s' but got '%s'" % (expected, actual)

    assert_args_equal(['a=b', 'c="foo bar"'], 'a=b c="foo bar"')
    assert_args_equal(['a=b c="foo', 'bar"'], 'a=b c="foo\nbar"')
    assert_args_equal(['a=b c="foo\\', 'bar'], 'a=b c="foo\\\nbar')
    assert_args_equal(['a=b c="foo\\', 'bar"'], 'a=b c="foo\\\nbar"')

# Generated at 2022-06-13 04:37:44.612285
# Unit test for function split_args
def test_split_args():
    input = 'a=b c="foo bar" e="$(zoo boo)" f="{% if True %}foo{% else %}bar{% endif %}" g=\'$(zoo boo)\' j=\'yo\'k\''
    expected = ['a=b', 'c="foo bar"', 'e="$(zoo boo)"', 'f="{% if True %}foo{% else %}bar{% endif %}"', 'g=\'$(zoo boo)\'', "j=\'yo'k\'"]

    result = split_args(input)
    assert(expected == result)

    expected = ['arg1', 'arg2="foo bar"']
    input = 'arg1\narg2="foo bar"'
    result = split_args(input)
    assert(expected == result)


# Generated at 2022-06-13 04:37:53.649402
# Unit test for function split_args
def test_split_args():
    t = {}
    t['a=b c="foo bar"'] = ['a=b', 'c="foo bar"']
    t['c="foo bar" a=b'] = ['c="foo bar"', 'a=b']
    t['a=b'] = ['a=b']
    t['a=b c=d'] = ['a=b', 'c=d']
    t['a="b c" d="e f"'] = ['a="b c"', 'd="e f"']
    t['a="b c" d="e\'f"'] = ['a="b c"', "d=\'e\'f\'"]
    t['a="b c" d=\'e"f\''] = ['a="b c"', 'd="e\'f"']

# Generated at 2022-06-13 04:38:04.412304
# Unit test for function split_args

# Generated at 2022-06-13 04:38:38.961044
# Unit test for function split_args
def test_split_args():
    ''' returns a list of tests for param parsing '''

    # simple param parsing
    yield (split_args, ("a=b c=d e=f"), ['a=b', 'c=d', 'e=f'])
    # param parsing with escaped chars
    yield (split_args, ("a=b c=d\\ e=f"), ['a=b', 'c=d e=f'])
    # param parsing with escaped newlines
    yield (split_args, ("a=b \\\nc=d \\\ne=f"), ['a=b\nc=d\ne=f'])
    # param parsing with escaped newlines, extra spaces
    yield (split_args, ("a=b \\\n  c=d \\\n  e=f"), ['a=b\nc=d\ne=f'])
    # param

# Generated at 2022-06-13 04:38:49.525183
# Unit test for function split_args
def test_split_args():
    assert split_args("") == []
    assert split_args("one") == ["one"]
    assert split_args("one two") == ["one", "two"]
    assert split_args('one "two three"') == ["one", '"two three"']
    assert split_args('one "two three" four') == ["one", '"two three"', "four"]
    assert split_args('one "two three" "four five"') == ["one", '"two three"', '"four five"']
    assert split_args('foo="one two"') == ['foo="one two"']
    assert split_args('one=1 two=2') == ['one=1', 'two=2']

# Generated at 2022-06-13 04:38:55.042202
# Unit test for function split_args

# Generated at 2022-06-13 04:39:04.499354
# Unit test for function split_args
def test_split_args():
    args1 = 'a=b c="foo bar"'
    assert split_args(args1) == ['a=b', 'c="foo bar"']
    args2 = 'a=b "c={{foo}} d={{bar}}"'
    assert split_args(args2) == ['a=b', 'c={{foo}} d={{bar}}']
    args3 = "a=b 'c={{foo}} d={{bar}}'"
    assert split_args(args3) == ['a=b', "c={{foo}} d={{bar}}"]
    args4 = "a=b 'c={{foo}} d=\"{{bar}}\"'"
    assert split_args(args4) == ['a=b', 'c={{foo}} d="{{bar}}"']

# Generated at 2022-06-13 04:39:13.922163
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("\"") == ['"']
    assert split_args("'") == ["'"]
    assert split_args("a 'b c'") == ['a', "'b c'"]
    assert split_args("a \"b c\"") == ['a', '"b c"']
    assert split_args("a {{'b c'}}") == ['a', "{{'b c'}}"]
    assert split_args("a {{ \"b c\" }}") == ['a', "{{ \"b c\" }}"]
    assert split_args("a {% if True %} b c {% endif %}") == ['a', "{% if True %} b c {% endif %}"]
    assert split_args

# Generated at 2022-06-13 04:39:19.236375
# Unit test for function split_args
def test_split_args():
    assert split_args("foo=bar baz=qux") == ['foo=bar', 'baz=qux']
    assert split_args("foo=bar baz='qux with spaces'") == ['foo=bar', "baz='qux with spaces'"]
    assert split_args("foo=bar baz='qux with spaces'") == ['foo=bar', "baz='qux with spaces'"]
    assert split_args("foo=bar baz='qux with spaces'") == ['foo=bar', "baz='qux with spaces'"]
    assert split_args("foo=bar baz='qux with spaces'") == ['foo=bar', "baz='qux with spaces'"]

# Generated at 2022-06-13 04:39:27.499759
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(
            test_param = dict(type='str', required=True),
        ),
        supports_check_mode=False,
    )


# Generated at 2022-06-13 04:39:34.897534
# Unit test for function split_args
def test_split_args():
    ''' Run unit tests for function split_args '''
    # Simple test
    results = split_args('key1=val1 key2=val2')
    assert len(results) == 2
    assert results[0] == 'key1=val1'
    assert results[1] == 'key2=val2'

    # Simple, quoted test
    results = split_args('key1=val1 key2="val2"')
    assert len(results) == 2
    assert results[0] == 'key1=val1'
    assert results[1] == 'key2="val2"'

    # Simple, quoted test
    results = split_args("key1=val1 key2='val2'")
    assert len(results) == 2
    assert results[0] == 'key1=val1'

# Generated at 2022-06-13 04:39:42.761564
# Unit test for function split_args
def test_split_args():
    '''
    this is the Python equivalent of the ruby tests,
    it's here if you want to run it on its own
    '''


# Generated at 2022-06-13 04:39:53.296886
# Unit test for function split_args
def test_split_args():
    import pytest
    from ansible.utils import split_args
    # Test 0 - unquoted args
    result = split_args("foo=bar biz=boz")
    assert result == ['foo=bar', 'biz=boz']
    result = split_args("foo=bar\nbiz=boz")
    assert result == ['foo=bar', 'biz=boz']
    result = split_args("foo=bar\n\nbiz=boz")
    assert result == ['foo=bar\n', 'biz=boz']
    result = split_args("foo=bar\n\nbiz=boz\n")
    assert result == ['foo=bar\n', 'biz=boz\n']
    result = split_args("foo=bar\n\nbiz=boz\n\n")

# Generated at 2022-06-13 04:40:27.189124
# Unit test for function split_args
def test_split_args():
    # The provided tests are taken from
    # https://github.com/ansible/ansible/blob/devel/test/units/modules/utils.py
    # and slightly simplified.

    # Note that various combinations of nested, double and single quotes are
    # not possible in the Ansible command line. Therefore we do not test
    # these cases here. (Apart from the fact that we do not provide tests
    # for `verbatim`.)

    # The following tests are not part of the test suite and are added here
    # to test functionality that is not handled by the other tests.

    # test issue https://github.com/ansible/ansible/issues/57549
    # Test that a line continuation at the end of a line works
    assert split_args("a=b c=d\\") == ["a=b", "c=d"]

# Generated at 2022-06-13 04:40:33.753774
# Unit test for function split_args

# Generated at 2022-06-13 04:40:43.968483
# Unit test for function split_args
def test_split_args():

    assert split_args("one two") == ['one', 'two']
    assert split_args("one 'two three'") == ["one", "'two three'"]
    assert split_args("one 'two three'") == ["one", "'two three'"]

    # test a complicated one, with a lot of nesting
    assert split_args("""
    one {{ two }}
    {% if four %}
    {{ three }}{% else %}
    {% if five %}{% endif %}
    {% endif %}
    """) == ["one", "{{ two }}", "{% if four %}", "{{ three }}{% else %}", "{% if five %}{% endif %}", "{% endif %}"]

    # make sure we preserve the newlines properly

# Generated at 2022-06-13 04:40:52.700290
# Unit test for function split_args
def test_split_args():
    '''
    This tests various combinations of command line arguments
    '''
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b c=d e=f") == ['a=b', 'c=d', 'e=f']
    assert split_args("") == ['']
    assert split_args("a=b 'c=d e=f' g=h") == ['a=b', 'c=d e=f', 'g=h']
    assert split_args("a=b \"c=d e=f\" g=h") == ['a=b', 'c=d e=f', 'g=h']