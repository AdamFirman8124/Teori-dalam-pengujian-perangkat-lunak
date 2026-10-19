

# Generated at 2022-06-13 04:31:10.809827
# Unit test for function split_args
def test_split_args():

    args = "a=b c=\"foo bar\" d=\"foo bar\nsecond line\""
    parsed = split_args(args)
    assert parsed == ['a=b', 'c="foo bar"', 'd="foo bar\nsecond line"'], parsed

    args = "a=\"b c\""
    parsed = split_args(args)
    assert parsed == ['a="b c"'], parsed

    args = "a=b c=foo\\\nbar d=baz"
    parsed = split_args(args)
    assert parsed == ['a=b', 'c=foo\nbar', 'd=baz'], parsed

    args = "{{lookup('pipe', 'command arg1 arg2')}}"
    parsed = split_args(args)

# Generated at 2022-06-13 04:31:14.664118
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('foo') == False
    assert is_quoted('"foo"') == True
    assert is_quoted("'foo'") == True
    assert is_quoted("'foo") == False
    assert is_quoted('foo\'') == False
    assert is_quoted('"foo\'') == False


# Generated at 2022-06-13 04:31:16.325334
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"') is True
    assert is_quoted("'foo'") is True
    assert is_quoted('foo') is False



# Generated at 2022-06-13 04:31:22.814871
# Unit test for function split_args
def test_split_args():
    '''
    This tests the output of the split_args function against a
    variety of different input (arg strings)
    '''
    test_input = dict()
    test_input['test_equal'] = dict()
    test_input['test_equal']['input'] = 'a=b c="foo bar" d=\'foo bar\''
    test_input['test_equal']['outcome'] = ['a=b', 'c="foo bar"', 'd=\'foo bar\'']
    test_input['test_equal']['comment'] = 'ensure that split_args returns the same array it was given'

    test_input['test_quotes'] = dict()
    test_input['test_quotes']['input'] = 'a="b c" d=\'e f\''

# Generated at 2022-06-13 04:31:32.674122
# Unit test for function split_args
def test_split_args():
    print("Running tests for function split_args:")

    from ansible.module_utils._text import to_text
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    def test_case(test_in, test_out):
        test_out = [to_text(x) for x in test_out]
        test_in = to_text(test_in)
        test_res = split_args(test_in)
        if test_res == test_out:
            print('Input string: %s\nOutput string: %s\nTest result: PASS' % (test_in, test_res))
            return 1
        else:
            print('Input string: %s\nExpected output: %s\nTest result: FAIL' % (test_in, test_out))
            return 0

# Generated at 2022-06-13 04:31:42.903489
# Unit test for function split_args
def test_split_args():

    # very simple test for unbalanced quotes
    try:
        split_args('foo="bar')
        assert False, "unbalanced quotes not detected"
    except Exception:
        pass

    # very simple test for unbalanced quotes
    try:
        split_args('foo=\'bar')
        assert False, "unbalanced quotes not detected"
    except Exception:
        pass

    # very simple test for unbalanced quotes
    try:
        split_args('foo="bar\'')
        assert False, "unbalanced quotes not detected"
    except Exception:
        pass

    # make sure white space splitting works
    assert split_args('a=1 b=2') == ['a=1', 'b=2']

    # make sure that a line continuation doesn't mess anything up
    # and that we preserve the structure

# Generated at 2022-06-13 04:31:48.654124
# Unit test for function is_quoted
def test_is_quoted():
    assert (is_quoted("'foo'") == True)
    assert (is_quoted("'foo") == False)
    assert (is_quoted('"foo"') == True)
    assert (is_quoted('"foo') == False)
    assert (is_quoted('foo') == False)


# Generated at 2022-06-13 04:31:56.390670
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'asdf'") is True
    assert is_quoted('"asdf"') is True
    assert is_quoted('"asdf\'"') is True
    assert is_quoted('') is False
    assert is_quoted('asdf') is False
    assert is_quoted('\'asdf') is False
    assert is_quoted('asdf"') is False
    assert is_quoted('"asdf') is False
    assert is_quoted('asdf\'') is False


# Generated at 2022-06-13 04:32:02.888512
# Unit test for function unquote
def test_unquote():
    ''' test unquote() function '''
    assert unquote("'content'") == "content"
    assert unquote('"content"') == "content"
    assert unquote("'content") != 'content'
    assert unquote("content") == "content"
    assert unquote("'con''tent'") == "con'tent"
    assert unquote("'con''tent") != "con'tent"

# Generated at 2022-06-13 04:32:04.970608
# Unit test for function unquote
def test_unquote():
    assert unquote('"test"') == "test"
    assert unquote("'test'") == "test"
    assert unquote('"test') == '"test'
    assert unquote("'test") == "'test"


# Generated at 2022-06-13 04:32:21.913398
# Unit test for function split_args

# Generated at 2022-06-13 04:32:31.524665
# Unit test for function split_args
def test_split_args():

    # test a simple split
    assert split_args('-v foo=bar baz=quux') == ['-v', 'foo=bar', 'baz=quux']

    # test a multi-line split
    assert split_args('foo=bar \\\nbaz=quux') == ['foo=bar', 'baz=quux']

    # test a split inside quotes
    assert split_args('foo=bar baz="quux zsh"') == ['foo=bar', 'baz="quux zsh"']

    # test a not-quite-fully quoted and split string
    assert split_args('foo=bar baz="quux zsh') == ['foo=bar', 'baz="quux zsh']

    # test a split inside jinja2 tags

# Generated at 2022-06-13 04:32:42.216857
# Unit test for function split_args
def test_split_args():
    # no args
    assert(split_args('') == [])
    # single arg
    assert(split_args('foo') == ['foo'])
    # single arg with quotes
    assert(split_args('"bar"') == ['bar'])
    # single arg with single quotes
    assert(split_args('\'bar\'') == ['bar'])
    # two args, no quotes
    assert(split_args('foo bar') == ['foo', 'bar'])
    # two args, one quoted
    assert(split_args('foo "bar baz"') == ['foo', 'bar baz'])
    # two args, both quoted
    assert(split_args('"foo bar" "foo baz"') == ['foo bar', 'foo baz'])
    # two args, quoted across multiple lines

# Generated at 2022-06-13 04:32:51.894993
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\\n foo bar"') == ['a=b', 'c="foo bar foo bar"']
    assert split_args('a=b c="foo bar\\\n foo bar" d="foo bar"') == ['a=b', 'c="foo bar foo bar"', 'd="foo bar"']
    assert split_args('a=b c="foo bar\\\n foo bar" d="foo bar" e=f g=h') == ['a=b', 'c="foo bar foo bar"', 'd="foo bar"', 'e=f', 'g=h']

# Generated at 2022-06-13 04:33:03.012681
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo') == ['a=b', 'c="foo']
    assert split_args('a=b c=\'foo bar\'') == ['a=b', 'c=\'foo bar\'']
    assert split_args('a=b c=\'foo bar') == ['a=b', 'c=\'foo bar']
    assert split_args('a=b c=\'foo') == ['a=b', 'c=\'foo']
    assert split_args('a=b c="{{foo}}') == ['a=b', 'c="{{foo}}']


# Generated at 2022-06-13 04:33:11.683939
# Unit test for function split_args
def test_split_args():
    ''' unit tests for split_args()'''
    import os

    # basic test
    assert split_args('one two') == ['one', 'two']

    # test quotes
    assert split_args('one "two three"') == ['one', '"two three"']

    # test jinja2
    assert split_args('one {{foo}}') == ['one', '{{foo}}']
    assert split_args('one {{foo}} {{bar}}') == ['one', '{{foo}}', '{{bar}}']

    # test jinja2 in quotes
    assert split_args('one "{{foo}}"') == ['one', '"{{foo}}"']
    assert split_args("one '{{foo}}'") == ['one', "'{{foo}}'"]

# Generated at 2022-06-13 04:33:24.181828
# Unit test for function split_args
def test_split_args():
    # Tests to make sure split_args can handle strings specified in a multiline fashion
    # Each test case is of the form result, string to split, comment explaining the test case

    test_cases = []

    # These tests check the basic functionality of the code, if it can handle quotes and jinja2 blocks
    test_cases.append((['"a=b', 'c="foo bar"'], '''"a=b" c="foo bar"''', 'should split on spaces, but not inside of quotes'))

    test_cases.append((['"a=b', 'c="foo bar"'], '''"a=b"  \
c="foo bar"''', 'should split on spaces, but not inside of quotes. Should handle trailing \\ with quotes ending the line'))


# Generated at 2022-06-13 04:33:36.085364
# Unit test for function split_args

# Generated at 2022-06-13 04:33:47.578472
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b\n') == ['a=b\n']
    assert split_args('a=b\nc=d') == ['a=b\n', 'c=d']
    assert split_args('a=b\nc="d e"') == ['a=b\n', 'c="d e"']
    assert split_args('a=b\nc="d \\\\ e"') == ['a=b\n', 'c="d \\\\ e"']
    assert split_args('a=b\nc="d e\\\nf"') == ['a=b\n', 'c="d e\\\n', 'f"']

# Generated at 2022-06-13 04:33:56.551275
# Unit test for function split_args
def test_split_args():
    def _run_test(input, output, msg):
        result = split_args(input)
        if result == output:
            return True
        print("Test failed: {}, got {} but expected {}".format(msg, result, output))

    assert(_run_test("foo bar baz", ["foo", "bar", "baz"], "simple 3 arg test"))
    assert(_run_test("foo'bar baz", ["foobar", "baz"], "test single quote"))
    assert(_run_test("foo'bar baz'foo", ["foobar", "baz'foo"], "test single quote 2"))
    assert(_run_test("foo\"bar baz", ["foo\"bar", "baz"], "test double quote"))
    assert(_run_test("'\"'", ['"'], "test single then double quote"))

# Generated at 2022-06-13 04:34:25.253857
# Unit test for function split_args
def test_split_args():
    # split on spaces and preserve whitespace
    assert split_args("ansible-doc -l") == ['ansible-doc', '-l']

    assert split_args("ansible-doc -l\nanother") == ['ansible-doc', '-l', '\nanother']

    # handle quotes, spaces and newlines
    assert split_args("ansible-doc -l\n  -a foo='bar baz' \\\n  -b 'foo bar'") == ['ansible-doc', '-l', '\n', '  -a', "foo='bar baz'", '\\\n', "  -b", "'foo bar'"]


# Generated at 2022-06-13 04:34:31.873847
# Unit test for function split_args

# Generated at 2022-06-13 04:34:36.279772
# Unit test for function split_args
def test_split_args():
    # simple case
    assert split_args(u'foo=bar') == split_args(u'foo=bar')
    assert split_args(u'foo="bar baz"') == split_args(u'foo="bar baz"')

    # simple case with line break
    assert split_args(u'foo=bar\nbaz=boz') == split_args(u'foo=bar\nbaz=boz')
    assert split_args(u'foo="bar baz"\nbaz=boz') == split_args(u'foo="bar baz"\nbaz=boz')

    # simple case with line continuation
    assert split_args(u'foo=bar \\baz=boz') == split_args(u'foo=bar baz=boz')

# Generated at 2022-06-13 04:34:44.845433
# Unit test for function split_args
def test_split_args():
    '''
    This makes sure split_args does the right thing with different types
    of quoting and jinja2 blocks, including nested and intermixed
    '''

# Generated at 2022-06-13 04:34:56.524003
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(object):

        def __init__(self, argument_spec, supports_check_mode=False, bypass_checks=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.bypass_checks = bypass_checks

        def fail_json(self, *args, **kwargs):
            raise AssertionError('fail_json should not be called')

        def exit_json(self, *args, **kwargs):
            print('exit_json should not be called')


# Generated at 2022-06-13 04:35:07.576114
# Unit test for function split_args
def test_split_args():
    def test_assert_equal(args, expected):
        assert expected == split_args(args)

    test_assert_equal('"foo bar"', ['foo bar'])
    test_assert_equal("'foo bar'", ['foo bar'])
    test_assert_equal('"foo bar" "foo bar"', ['foo bar', 'foo bar'])
    test_assert_equal("'foo bar' 'foo bar'", ['foo bar', 'foo bar'])

    test_assert_equal("[[ foo ]]", [['foo']])
    test_assert_equal("[foo]", [['foo']])
    test_assert_equal("[foo, bar]", [['foo, bar']])

    test_assert_equal("a=b c=d", ['a=b', 'c=d'])
    test

# Generated at 2022-06-13 04:35:18.001402
# Unit test for function split_args

# Generated at 2022-06-13 04:35:26.149141
# Unit test for function split_args

# Generated at 2022-06-13 04:35:37.120821
# Unit test for function split_args
def test_split_args():

    def assert_split_args(test_input, expected_output):
        output = split_args(test_input)
        assert output == expected_output, "split_args(%s) = %s, expected %s" % (test_input, output, expected_output)

    assert_split_args("a=b c=d", ["a=b", "c=d"])
    assert_split_args("a='b c'", ["a='b c'"])
    assert_split_args("a='b c' d='e f'", ["a='b c'", "d='e f'"])
    assert_split_args("a='b c' d='e f' g='h i'", ["a='b c'", "d='e f'", "g='h i'"])
    assert_split_

# Generated at 2022-06-13 04:35:45.198898
# Unit test for function split_args
def test_split_args():
    from textwrap import dedent

    a = split_args('a=b c="foo bar"')
    assert a == ['a=b', 'c="foo bar"']

    a = split_args('a=b c="foo bar')
    assert a == ['a=b', 'c="foo bar']

    a = split_args('a=b c="foo bar ')
    assert a == ['a=b', 'c="foo bar ']

    a = split_args('a=b c="foo bar\\ ')
    assert a == ['a=b', 'c="foo bar ']

    a = split_args('a=b c="foo bar\\\\ ')
    assert a == ['a=b', 'c="foo bar\\ ']

    a = split_args('a=b c="foo bar"\\ ')
   

# Generated at 2022-06-13 04:36:17.060015
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule

    # Test a single quoted string
    args = "a='b c'"
    assert split_args(args) == ['a=b c'], "'%s' should have been split into 1 item, a=b c" % args

    # Test a doubly quoted string
    args = 'a="b c"'
    assert split_args(args) == ['a=b c'], "'%s' should have been split into 1 item, a=b c" % args

    # Test that quoted values are unquoted before being returned
    args = 'a="b c"'
    assert split_args(args) == ['a=b c'], "'%s' should have been split into 1 item, a=b c" % args

    # Test a quoted string with an escaped quote

# Generated at 2022-06-13 04:36:22.172073
# Unit test for function split_args
def test_split_args():

    def run_test(args, expect):
        params = split_args(args)
        if params != expect:
            raise Exception("split_args(%s) returned %s but expected %s" % (args, params, expect))

    run_test("a=b c=d", ['a=b', 'c=d'])
    run_test("a=b c=\"foo bar\"", ['a=b', 'c=\"foo bar\"'])
    run_test("a=b c='foo bar'", ['a=b', 'c=\'foo bar\''])
    run_test("a=b c=\"foo bar's\"", ['a=b', 'c=\"foo bar\'s\"'])
    run_test("a=b c=\"foo\nbar\"", ['a=b', 'c=\"foo\nbar\"'])

# Generated at 2022-06-13 04:36:32.587314
# Unit test for function split_args
def test_split_args():
    '''Simple test function for split_args'''

    test_strings = list()
    compare_strings = list()

    # Normal Examples
    test_strings.append("""some_key: some value""")
    compare_strings.append(['some_key:', 'some', 'value'])

    test_strings.append("""some_key: some value with spaces""")
    compare_strings.append(['some_key:', 'some', 'value', 'with', 'spaces'])

    test_strings.append("""some_key: some "value with spaces" """)
    compare_strings.append(['some_key:', 'some', '"value with spaces" '])

    # multiline
    test_strings.append("""some_key: some "value with spaces"
    second_line: foo""")


# Generated at 2022-06-13 04:36:43.204571
# Unit test for function split_args
def test_split_args():
    # Simple cases
    assert ['a=b', 'c="foo bar"'] == split_args('a=b c="foo bar"')
    assert ['a=b', 'c=d', 'e=f'] == split_args('a=b c=d e=f')
    assert ['a=b', 'c="foo bar"', 'e=f'] == split_args('a=b c="foo bar" e=f')
    assert ['a="foo', 'bar"'] == split_args('a="foo\nbar"')
    assert ['"foo bar"'] == split_args('"foo bar"')
    assert ['a="foo bar"'] == split_args('a="foo bar"')

# Generated at 2022-06-13 04:36:52.432435
# Unit test for function split_args
def test_split_args():
    # Testing for multiple args with jinja blocks mixed in.
    args = " key=value jinja=\"{{ foo }}\" "
    params = split_args(args)

    assert len(params) == 2
    assert params[0] == 'key=value'
    assert params[1] == 'jinja="{{ foo }}"'

    # Testing for multiple args with multiple jinja blocks mixed in.
    args = " key=value jinja=\"{{ foo }}\" {{ bar }} \"{{ baz }}\" "
    params = split_args(args)

    assert len(params) == 2
    assert params[0] == 'key=value'
    assert params[1] == 'jinja="{{ foo }}" {{ bar }} "{{ baz }}"'

    # Testing for multiple args with an unended jinja block

# Generated at 2022-06-13 04:37:00.219275
# Unit test for function split_args

# Generated at 2022-06-13 04:37:11.804983
# Unit test for function split_args
def test_split_args():
    # Test basic functionality
    params = split_args('test1 test2 test3')
    assert params == ['test1', 'test2', 'test3']

    # Test basic functionality with double quotes
    params = split_args('test1 test2 test3')
    assert params == ['test1', 'test2', 'test3']

    # Test line continuation character
    params = split_args('test1 \\\ntest2')
    assert params == ['test1', 'test2']

    # Test empty strings
    params = split_args('')
    assert params == ['']

    # Test newlines
    params = split_args('test1 \ntest2')
    assert params == ['test1', 'test2']

    # Test single quotes
    params = split_args('test1 test2 test3')

# Generated at 2022-06-13 04:37:16.152594
# Unit test for function split_args
def test_split_args():
    '''
    Test split_args with a few basic test cases
    '''

    # Test case 0
    args = 'a=b c="foo bar" d="foo bar" e=bar'
    params = split_args(args)
    assert params == ['a=b', 'c="foo bar"', 'd="foo bar"', 'e=bar'], "test case failed"

    # Test case 1
    args = 'a="b c" "d e" "f g"'
    params = split_args(args)
    assert params == ['a="b c"', '"d e"', '"f g"'], "test case failed"

    # Test case 2
    args = 'a="b\" c" "d\' e" "f g"'
    params = split_args(args)

# Generated at 2022-06-13 04:37:24.577827
# Unit test for function split_args
def test_split_args():
    # testing for various sets of args in single quotes
    assert split_args('') == []
    assert split_args('a') == ['a']
    assert split_args("'a'") == ['a']
    assert split_args("' a '") == ['a']
    assert split_args(" 'a' ") == ['a']
    assert split_args(" 'a' 'b' ") == ['a', 'b']
    assert split_args(" 'a'   'b' ") == ['a', 'b']
    assert split_args(" 'a b' ") == ['a b']
    assert split_args(" 'a'  'b c' ") == ['a', 'b c']
    assert split_args(" 'a'  'b \" c' ") == ['a', 'b \" c']

    #

# Generated at 2022-06-13 04:37:36.020068
# Unit test for function split_args
def test_split_args():

    # test simple case that should come back quoted
    result = split_args("foo")
    assert result == ['foo']

    # a simple case that should come back unquoted
    result = split_args('foo bar')
    assert result == ['foo', 'bar']

    # quotes should cause the params to come back quoted
    result = split_args('"foo bar" baz')
    assert result == ['"foo bar"', 'baz']

    # double quotes should cause the params to come back quoted
    result = split_args("'foo bar' baz")
    assert result == ["'foo bar'", 'baz']

    # quotes within a single arg should cause the arg to come back quoted
    result = split_args("foo bar'")
    assert result == ["foo bar'"]

    # quotes over multiple args should cause the args to come

# Generated at 2022-06-13 04:38:35.583507
# Unit test for function split_args
def test_split_args():
    ''' the idea here is that the input and output dicts define a series of inputs and outputs to test.
    the input is a string, and the expected ouput is a list of strings that should be compared against
    the actual output of split_args '''

# Generated at 2022-06-13 04:38:41.102798
# Unit test for function split_args
def test_split_args():

    def assert_execution(args, result):
        actual = split_args(args)
        if actual != result:
            from difflib import unified_diff
            raise AssertionError("split_args(%r) != %r:\n%s" % (
                args, result, '\n'.join(unified_diff(pprint.pformat(result).splitlines(),
                                                     pprint.pformat(actual).splitlines()))))

    assert_execution("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    assert_execution('a=b c=""', ['a=b', 'c=""', ])
    assert_execution('a="foo bar" b=\'foo bar\'', ['a="foo bar"', "b='foo bar'"])

# Generated at 2022-06-13 04:38:50.577587
# Unit test for function split_args
def test_split_args():
    '''
    test a number of variations that we may encounter.
    '''

    # this is the list of tuples we use to compare the
    # parsed args to what they should be

# Generated at 2022-06-13 04:39:00.657504
# Unit test for function split_args
def test_split_args():
    '''
    Test for function split_args.
    '''
    import pytest
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:39:10.919194
# Unit test for function split_args
def test_split_args():
    # tests that the split_args function can reassemble tokens split over
    # quotes or jinja2 blocks correctly.

    # these two are for storing the original and result of the reassembly
    # for purposes of comparison/validation
    orig = []
    result = []

    # used for testing quotes
    quote_strings = [
        "foo bar",
        "foo \"bar\"",
        "foo 'bar'",
        "\"foo bar\"",
        "'foo bar'",
        "\"foo 'bar'\"",
        "'foo \"bar\"'",
        '"foo \'bar\'"',
        "'foo \"bar\"'",
        "foo bar baz",
        "'foo bar' baz",
        "'foo' \"bar\" baz",
        "'\"foo' bar\" baz"
    ]

    # used

# Generated at 2022-06-13 04:39:20.407265
# Unit test for function split_args
def test_split_args():
    results = split_args('a=b c="foo bar"')
    assert len(results) == 2
    assert results[0] == 'a=b'
    assert results[1] == 'c="foo bar"'
    results = split_args('a=b c="foo \\"bar\\""')
    assert len(results) == 2
    assert results[0] == 'a=b'
    assert results[1] == 'c="foo \\"bar\\""'
    results = split_args('a=b c="foo \\"b\\na\\nr\\""')
    assert len(results) == 2
    assert results[0] == 'a=b'
    assert results[1] == 'c="foo \\"b\\na\\nr\\""'

# Generated at 2022-06-13 04:39:31.171279
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a=b c="d e f"') == ['a=b', 'c="d e f"']
    assert split_args('a=b c="d e f" d="g h"') == ['a=b', 'c="d e f"', 'd="g h"']
    assert split_args('a=b c="d e f" d="g h" e="i j"') == ['a=b', 'c="d e f"', 'd="g h"', 'e="i j"']

# Generated at 2022-06-13 04:39:36.682854
# Unit test for function split_args
def test_split_args():

    """ Unit test for function split_args """

    val = "copy: src={{ src_file }} dest={{ dest_file }}"
    result = split_args(val)
    assert result == ["copy:", "src={{", "src_file", "}}", "dest={{", "dest_file", "}}"]

    val2 = "copy: src={{ src_file }} dest={{ dest_file }} validate='md5'"
    result2 = split_args(val2)
    assert result2 == ["copy:", "src={{", "src_file", "}}", "dest={{", "dest_file", "}}", "validate='md5'"]

    val3 = "copy: src={{ src_file }} dest={{ dest_file }} validate=sha1"
    result3 = split_args(val3)

# Generated at 2022-06-13 04:39:43.973010
# Unit test for function split_args
def test_split_args():
    """Test split_args.

    A series of tests are created for each item in ``arg_cases``.
    The first item in each tuple is the arg string, the second item is
    the expected result.

    """

# Generated at 2022-06-13 04:39:54.041757
# Unit test for function split_args
def test_split_args():

    assert split_args('a=1 b="foo bar"') == [u'a=1', u'b="foo bar"']
    assert split_args('a=1 b="foo bar') == [u'a=1', u'b="foo bar']
    assert split_args('a=1 b="foo \\"bar\\""') == [u'a=1', u'b="foo \\"bar\\""']
    assert split_args('a=1 b="foo \\"bar\\"" c=3') == [u'a=1', u'b="foo \\"bar\\""', u'c=3']
    assert split_args("a=1 b=foo\"bar' c=3") == [u'a=1', u'b=foo"bar', u"c=3"]