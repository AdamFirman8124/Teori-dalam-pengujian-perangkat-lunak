

# Generated at 2022-06-13 04:31:12.425565
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'example'")
    assert is_quoted('"example"')
    assert not is_quoted("example")


# Generated at 2022-06-13 04:31:16.371216
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'foo'")
    assert is_quoted('"foo"')
    assert not is_quoted('"foo\'')
    assert not is_quoted("'foo\"")
    assert not is_quoted('foo')
    assert not is_quoted('"foo')
    assert not is_quoted("'foo")


# Generated at 2022-06-13 04:31:21.563132
# Unit test for function unquote
def test_unquote():
    print("Testing unquote:")

    inputs = [
        '"foo"',
        "'foo'",
        '"foo',
        "'foo",
        'foo"',
        'foo\'',
        '"\'foo"',
        'foo\'"',
        '\'foo"',
        'foo\'"',
        '\'foo\'',
        '"foo"bar',
        'foo"bar"',
        '"bar"foo',
        'bar"foo"',
        '"foobar"',
        'foobar',
        ''
    ]

# Generated at 2022-06-13 04:31:32.078695
# Unit test for function split_args
def test_split_args():
    ''' unit test for function split_args '''
    # test quotes
    params = split_args('"foo bar"')
    assert params == ['"foo bar"'], "quoted string failed"
    params = split_args("'foo bar'")
    assert params == ["'foo bar'"], "quoted string failed"

    # test escaped quotes
    params = split_args('"foo bar" "foo bar"')
    assert params == ['"foo bar"', '"foo bar"'], "escaped quotes failed"
    params = split_args('"foobar" "foo\"bar" "foo bar"')
    assert params == ['"foobar"', '"foo\"bar"', '"foo bar"'], "escaped quotes failed"

    # test escaped newlines

# Generated at 2022-06-13 04:31:42.614311
# Unit test for function split_args
def test_split_args():
    # Test with no args and empty args
    assert split_args('') == []
    # Test with just a variable
    assert split_args('{{ variable }}') == ['{{ variable }}']
    # Test with a variable and some data
    assert split_args('{{ variable }} somedata') == ['{{ variable }}', 'somedata']
    # Test with a variable and some data, with quotes
    assert split_args('{{ variable }} "somedata"') == ['{{ variable }}', '"somedata"']
    # Test with a variable and some data, with quotes, with a line continuation
    assert split_args('{{ variable }} "som\\\nedata"') == ['{{ variable }}', '"som\\\nedata"']
    # Test with a variable and some data, with quotes, with a line continuation, with a newline


# Generated at 2022-06-13 04:31:53.891755
# Unit test for function split_args
def test_split_args():
    """
    This function tests split_args() for different input args.
    """
    result = split_args("a=b c=\"foo bar\"")
    assert result == ['a=b', 'c="foo bar"'], "split_args failed"

    result = split_args("a=\"foo bar\" c=\"foo bar\"")
    assert result == ['a="foo bar"', 'c="foo bar"'], "split_args failed"

    result = split_args("a={{b}} c=\"foo bar\"")
    assert result == ['a={{b}}', 'c="foo bar"'], "split_args failed"

    result = split_args("a={{b}} c=\"foo {{bar}}\"")
    assert result == ['a={{b}}', 'c="foo {{bar}}"'], "split_args failed"


# Generated at 2022-06-13 04:32:06.436992
# Unit test for function split_args

# Generated at 2022-06-13 04:32:17.345275
# Unit test for function split_args
def test_split_args():

    def _test_split_args(arg_string, expected_result):
        '''
        utility function that returns the result of split_args
        and does a basic sanity check against an expected result
        '''
        result = split_args(arg_string)
        if len(result) != len(expected_result):
            raise Exception("Expected result and test result do not appear to be equal lengths.")
        return result

    # basic test of normal args
    test_string = "foo=bar baz='hello world'"
    expected = ['foo=bar', 'baz=hello world']
    result = _test_split_args(test_string, expected)
    if result != expected:
        raise Exception("Basic param splitting test did not pass.")

    # test with quotes in params

# Generated at 2022-06-13 04:32:29.944331
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.parsing.convert_bool import boolean
    def split(args):
        return split_args(args)

    def assert_equal(a, b):
        assert a == b, "%s is not equal to %s" % (a, b)

    # Simple argument
    assert_equal(
        split("foo=bar other=baz"),
        ["foo=bar", "other=baz"]
    )

    # Empty argument
    assert_equal(
        split("foo=bar other="),
        ["foo=bar", "other="]
    )

    # Empty argument with space
    assert_equal(
        split("foo=bar other= "),
        ["foo=bar", "other= "]
    )

    # Empty argument with space and other value

# Generated at 2022-06-13 04:32:40.925004
# Unit test for function unquote
def test_unquote():

    print("===test_unquote===")

    def verify(a, b):
        a = unquote(a)
        if a != b:
            print("FAIL: %s != %s" % (a, b))
        else:
            print("%s == %s" % (a, b))

    testcase = [
        ('arg1', 'arg1'),
        ('"arg1"', 'arg1'),
        ("'arg1'", 'arg1'),
        (u'arg1', u'arg1'),
        (u'"arg1"', u'arg1'),
        (u"'arg1'", u'arg1'),
        (u'arg1', 'arg1'),
        (u'"arg1"', 'arg1'),
        (u"'arg1'", 'arg1'),
    ]

   

# Generated at 2022-06-13 04:33:00.727617
# Unit test for function split_args

# Generated at 2022-06-13 04:33:09.941069
# Unit test for function split_args

# Generated at 2022-06-13 04:33:16.143850
# Unit test for function split_args
def test_split_args():
    # basic test
    assert split_args("a=1 b=2") == ["a=1", "b=2"]

    # split at newline
    assert split_args("a=1\nb=2") == ["a=1\n", "b=2"]

    # normal quotes
    assert split_args("a=1 b='foo bar' c=\"foo bar\" d=1\"foo\"bar") == ['a=1', "b='foo bar'", 'c="foo bar"', 'd=1"foo"bar']

    # test that line continuation splits the quoted block
    assert split_args("a=1 b='foo \\\nbar'") == ['a=1', "b='foo \\\n", "bar'"]

    # test that if you escape the line continuation character inside quotes it is not split

# Generated at 2022-06-13 04:33:28.671410
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args("foo 'bar baz'") == ['foo', "'bar baz'"]
    assert split_args("foo\\ bar") == ['foobar']
    assert split_args("foobar") == ['foobar']
    assert split_args("foo\"ba'r") == ["foo\"ba'r"]
    assert split_args("\"foo\\\"ba'r\"") == ['foo"ba\'r']
    assert split_args("\"foo\\\"ba'r baz\"") == ['foo"ba\'r baz']

if __name__ == '__main__':
    test_split_args()

# Generated at 2022-06-13 04:33:30.795518
# Unit test for function split_args
def test_split_args():
    text = u'''module: win_ping\nargs: "foo={{ foo }}" # a comment'''
    split_args(text)

# Generated at 2022-06-13 04:33:42.751831
# Unit test for function split_args
def test_split_args():
    # test only
    from ansible import constants
    constants.CLIARGS = None

    from ansible.module_utils.basic import AnsibleModule

    def _test(
        args,
        expected_params,
        expected_rc,
        expected_stderr,
    ):
        ''' args is the string to split, expected_params is a list of the
        expected results, expected_rc is the expected return code, and
        expected_stderr is the expected stderr string to print '''

        module = AnsibleModule(argument_spec={})

        rc = 0
        params = []
        try:
            params = split_args(args)
        except Exception as e:
            rc = 1
            stderr = "%s" % e.message

        # If the test catches an exception, but the test's expected_

# Generated at 2022-06-13 04:33:53.734265
# Unit test for function split_args
def test_split_args():
    import sys

    def do_test(args, results):
        args = split_args(args)
        if args != results:
            print("%s != %s" % (args, results))
            sys.exit(1)

    do_test("", [])
    do_test("foo", ["foo"])
    do_test("foo 'bar baz'", ["foo", "'bar baz'"])
    do_test("foo \"bar baz\"", ["foo", "\"bar baz\""])
    do_test("foo 'bar \" baz'", ["foo", "'bar \" baz'"])
    do_test("foo \"bar ' baz\"", ["foo", "\"bar ' baz\""])
    do_test("foo 'bar ' baz", ["foo", "'bar '", "baz"])

# Generated at 2022-06-13 04:34:03.620117
# Unit test for function split_args
def test_split_args():
    '''
    This function tests to make sure that the arguments are split properly
    by split_args and that it handles embedded quotes and jinja2 blocks properly.
    '''

    # The arguments we will test the function on

# Generated at 2022-06-13 04:34:11.757028
# Unit test for function unquote
def test_unquote():
    ''' unit tests for function unquote '''

    # Simple
    assert unquote('') == ''
    assert unquote('abc') == 'abc'

    # Empty quotes
    assert unquote('""') == ''
    assert unquote("''") == ''

    # Simple quotes
    assert unquote('"abc"') == 'abc'
    assert unquote("'abc'") == 'abc'

    # Double chars
    assert unquote('"a""bc"') == 'a"bc'
    assert unquote("'a''bc'") == 'a\'bc'

    # Mix
    assert unquote('"a\'bc"') == "a'bc"
    assert unquote('\'a"bc\'') == 'a"bc'

    # Not matching quotes

# Generated at 2022-06-13 04:34:23.020558
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('one') == ['one']
    assert split_args('one two') == ['one', 'two']
    assert split_args('one "two three"') == ['one', '"two three"']
    assert split_args('one "two three" four') == ['one', '"two three"', 'four']
    assert split_args('one "two three" four\\') == ['one', '"two three"', 'four\\']
    assert split_args('one "two three" four\\\nfive') == ['one', '"two three"', 'four\nfive']
    assert split_args('"one \\"two\\" three"') == ['"one \\"two\\" three"']

# Generated at 2022-06-13 04:34:43.557169
# Unit test for function split_args
def test_split_args():

    # test splitting with some basics
    assert split_args("") == []
    assert split_args("a=b") == ['a=b']
    assert split_args("a='b b'") == ["a='b b'"]
    assert split_args("a=\"b b\"") == ['a="b b"']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b\nc=d") == ['a=b', 'c=d']
    assert split_args("a=b c=d e=f") == ['a=b', 'c=d', 'e=f']
    assert split_args("a=b\nc=d\ne=f") == ['a=b', 'c=d', 'e=f']

    # now

# Generated at 2022-06-13 04:34:55.844626
# Unit test for function split_args
def test_split_args():
    # no args passed
    args = ''
    params = split_args(args)
    assert len(params) == 0

    # single arg
    args = 'arg1'
    params = split_args(args)
    assert len(params) == 1
    assert params[0] == 'arg1'

    # two args
    args = 'arg1 arg2'
    params = split_args(args)
    assert len(params) == 2
    assert params[0] == 'arg1'
    assert params[1] == 'arg2'

    # arg with quotes - double
    args = 'arg1 "arg2"'
    params = split_args(args)
    assert len(params) == 2
    assert params[0] == 'arg1'
    assert params[1] == '"arg2"'

    # arg with

# Generated at 2022-06-13 04:35:07.069285
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args(' a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar" ') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"\n') == ['a=b', 'c="foo bar"\n']
    assert split_args('a=b c="foo bar\n"') == ['a=b', 'c="foo bar\n"']

# Generated at 2022-06-13 04:35:17.666844
# Unit test for function split_args

# Generated at 2022-06-13 04:35:25.941215
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE


# Generated at 2022-06-13 04:35:31.093014
# Unit test for function split_args

# Generated at 2022-06-13 04:35:40.422815
# Unit test for function split_args
def test_split_args():
    import sys
    import os
    import subprocess

    # run unittest via python so we can use the -v flag
    # if the test fails, we should see the error output
    # if the test succeeds, we should see nothing at all
    cmd = [sys.executable, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_split_args.py')]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdout, stderr) = p.communicate()
    if p.returncode != 0:
        print(stdout)

if __name__ == '__main__':
    test_split_args()

# Generated at 2022-06-13 04:35:47.625958
# Unit test for function split_args

# Generated at 2022-06-13 04:35:56.094621
# Unit test for function split_args
def test_split_args():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # These are all examples of valid command line arguments that have been
    # split across multiple lines with a backslash as the last character.
    #
    # For more examples, see the implementation of ExpandArgs (formerly
    # ExpandModuleArgs()) in lib/ansible/runner/action_plugins/expand_args.py.
    assert split_args(u'a="b c"') == [u'a=b c']
    assert split_args(u'a="b c\\"') == [u'a=b c"']
    assert split_args(u'a="b\\\\c"') == [u'a=b\\c']

# Generated at 2022-06-13 04:36:04.237453
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar\'') == ['a=b', 'c="foo bar\'']
    assert split_args('a=b c="foo \'bar\'"') == ['a=b', 'c="foo \'bar\'"']
    assert split_args('a=b c="foo \'bar\'"') == ['a=b', 'c="foo \'bar\'"']
    assert split_args('a=b c="{% if foo %} bar {% endif %}"') == ['a=b', 'c="{% if foo %} bar {% endif %}"']

# Generated at 2022-06-13 04:36:28.793612
# Unit test for function split_args
def test_split_args():
    assert split_args('a=1') == ['a=1']
    assert split_args('a=1\\\nb=2\\\nc=3') == ['a=1\nb=2\nc=3']
    assert split_args('a=1 \\\n b=2') == ['a=1', 'b=2']
    assert split_args('a="b c" d="e f"') == ['a="b c"', 'd="e f"']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a=b c="d e"') == ['a=b', 'c="d e"']
    assert split_args('a=b c="d') == ['a=b', 'c="d']

# Generated at 2022-06-13 04:36:39.065500
# Unit test for function split_args
def test_split_args():
    # Test splitting of simple arguments
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Test splitting with multiple whitespace characters
    assert split_args('a=b  c="foo bar"') == ['a=b', 'c="foo bar"']

    # Test splitting with newline characters
    assert split_args('a=b\nc="foo bar"') == ['a=b', 'c="foo bar"']

    # Test splitting with jinja blocks
    assert split_args('a=b c="{{ foo }}" d={{ bar }}') == ['a=b', 'c="{{ foo }}"', 'd={{ bar }}']

    # Test splitting with jinja blocks and newlines

# Generated at 2022-06-13 04:36:48.990570
# Unit test for function split_args
def test_split_args():
    args = "rm -rf /tmp/foo a=b c='foo bar' C=\"foo bar\" \"a b\""

    # some tests that show the behavior of this function
    # may be useful, but aren't necessary since the
    # old behavior kept around for backwards compatibility
    # is not entirely equivalent to this

    #print 'testing', args
    #print 'OLD: ', shlex.split(args)
    #print 'NEW: ', split_args(args)

    #assert shlex.split(args) == split_args(args)

    args = """foo='{{unquoted}}' '{{quoted}}' """
    #print 'testing', args
    #print 'OLD: ', shlex.split(args)
    #print 'NEW: ', split_args(args)

# Generated at 2022-06-13 04:36:58.497807
# Unit test for function split_args

# Generated at 2022-06-13 04:37:04.608497
# Unit test for function split_args
def test_split_args():

        assert split_args("a=b c=d") == ['a=b', 'c=d']
        assert split_args("a=b 'c=d e=f' g=h") == ['a=b', "'c=d e=f'", 'g=h']
        assert split_args("a=b c='d e=f' g=h") == ['a=b', "c='d", 'e=f\'', 'g=h']
        assert split_args("\"a=b\" \"c=d e=f\" g=h") == ['a=b', "c=d e=f", 'g=h']
        assert split_args("'a=b c=d' e='f g' i=j") == ['a=b c=d', 'e=f g', 'i=j']

# Generated at 2022-06-13 04:37:16.458783
# Unit test for function split_args

# Generated at 2022-06-13 04:37:24.741157
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=d e={{foo}}") == ['a=b', 'c=d', 'e={{foo}}']
    assert split_args("a=b c=d e={{foo}}\nf=g") == ['a=b', 'c=d', 'e={{foo}}\n', 'f=g']
    assert split_args("a=b c=d e=123\nf=g") == ['a=b', 'c=d', 'e=123\n', 'f=g']
    assert split_args("a=b c=d e=123\nf=g") == ['a=b', 'c=d', 'e=123\n', 'f=g']

# Generated at 2022-06-13 04:37:36.182266
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('"foo bar baz"') == ['foo bar baz']
    assert split_args('foo bar "baz foobar"') == ['foo', 'bar', 'baz foobar']
    assert split_args('foo="bar baz"') == ['foo=bar baz']
    assert split_args('foo="bar baz" foobar') == ['foo=bar baz', 'foobar']
    assert split_args('foo="bar baz" \\\nfoobar') == ['foo=bar baz foobar']
    assert split_args('foo="bar \\\nbaz" \\\nfoobar') == ['foo=bar baz', 'foobar']

# Generated at 2022-06-13 04:37:45.362935
# Unit test for function split_args
def test_split_args():
    import json

    def check_split(a, e):
        r = split_args(a)
        assert r == e or json.dumps(r) == json.dumps(e)
        for i in range(len(r)):
            assert len(r[i]) > 0


# Generated at 2022-06-13 04:37:49.417382
# Unit test for function split_args
def test_split_args():
    import doctest
    try:
        doctest.testmod()
    except:
        return False
    return True

# Generated at 2022-06-13 04:38:25.964409
# Unit test for function split_args
def test_split_args():
    '''
    for testing purposes,
    This is not a true unit test as it does not use the unittest package,
    it is merely here to help development
    '''


# Generated at 2022-06-13 04:38:34.574167
# Unit test for function split_args

# Generated at 2022-06-13 04:38:40.330414
# Unit test for function split_args

# Generated at 2022-06-13 04:38:44.937418
# Unit test for function split_args

# Generated at 2022-06-13 04:38:52.182275
# Unit test for function split_args

# Generated at 2022-06-13 04:39:02.446827
# Unit test for function split_args
def test_split_args():
    assert split_args("a='b c'") == ['a=\'b c\'']
    assert split_args("a='b c' d=\"e f\"") == ['a=\'b c\'', 'd="e f"']
    assert split_args("a='b c' 'd e'") == ['a=\'b c\'', '\'d e\'']
    assert split_args("a='b c' 'd e'") == ['a=\'b c\'', '\'d e\'']
    assert split_args("a='b c' 'd e'\\") == ['a=\'b c\'', '\'d e\'']
    assert split_args("a='b c' 'd e' \\\nf") == ['a=\'b c\'', '\'d e\' f']
    assert split_args

# Generated at 2022-06-13 04:39:12.007677
# Unit test for function split_args
def test_split_args():
    result = split_args("a=b c=\"foo bar\"")
    assert result == ['a=b', 'c="foo bar"']
    result = split_args("a=b c='foo bar'")
    assert result == ['a=b', "c='foo bar'"]
    result = split_args("foo='bar baz'")
    assert result == ["foo='bar baz'"]
    result = split_args("foo=\"bar baz\"")
    assert result == ["foo=\"bar baz\""]
    result = split_args("foo={% if bar %}baz{% endif %}zab")
    assert result == ["foo={% if bar %}baz{% endif %}zab"]
    result = split_args("foo={{ bar }}zab")

# Generated at 2022-06-13 04:39:22.530320
# Unit test for function split_args

# Generated at 2022-06-13 04:39:32.566797
# Unit test for function split_args
def test_split_args():
    assert split_args(r"a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args(r'''a=b c='foo bar' 'd e' "f g" h=\'i j\' "k \'l m n\' o"''') == ['a=b', "c='foo bar'", "'d e'", '"f g"', "h='i j'", '"k \'l m n\' o"']
    assert split_args(r"a=b c='foo bar' 'd e' \"f g\" h=\'i j\' \"k \'l m n\' o\"") == ['a=b', "c='foo bar'", "'d e'", '"f g"', "h='i j'", '"k \'l m n\' o"']


# Generated at 2022-06-13 04:39:40.068771
# Unit test for function split_args
def test_split_args():
    class TestCase:
        pass

    # Compare result of split_args() to expected result
    def test(data, expected):
        result = split_args(data)
        if result == expected:
            return
        else:
            TestCase.errors = True
            print("split_args error; return value: %s; expected value: %s" % (result, expected))
            print("split_args error; test data: %s" % data)

    # Set this to True on failure
    TestCase.errors = False

    # Test cases
    test("a=b c=\"foo bar\"",['a=b', 'c="foo bar"'])
    test("a=b c=\"foo bar\"",['a=b', 'c="foo bar"'])

# Generated at 2022-06-13 04:40:26.990136
# Unit test for function split_args
def test_split_args():

    print("Testing split_args")

    print("nested jinja2 print statements")
    data = "var1={{ foo }}{{ bar }} var2={{ baz }}"
    result = split_args(data)
    assert result == ['var1={{ foo }}{{ bar }}', 'var2={{ baz }}']

    print("nested jinja2 print statements in quotes")
    data = "var1='{{ foo }}{{ bar }}' var2='{{ baz }}'"
    result = split_args(data)
    assert result == ["var1='{{ foo }}{{ bar }}'", "var2='{{ baz }}'"]

    print("nested jinja2 tags in quotes")
    data = "var1='{% foo %}{% bar %}' var2='{% baz %}'"

# Generated at 2022-06-13 04:40:33.624604
# Unit test for function split_args
def test_split_args():
    params = split_args('foo bar')
    assert ' '.join(params) == 'foo bar'

    params = split_args('foo bar "bar baz"')
    assert ' '.join(params) == 'foo bar "bar baz"'

    params = split_args('foo bar "bar baz" \'foo bar\'')
    assert ' '.join(params) == 'foo bar "bar baz" \'foo bar\''

    params = split_args('foo "bar baz" \'foo bar\'')
    assert ' '.join(params) == 'foo "bar baz" \'foo bar\''

    params = split_args('foo bar "bar baz\' \'foo bar"')
    assert ' '.join(params) == 'foo bar "bar baz\' \'foo bar"'


# Generated at 2022-06-13 04:40:43.849452
# Unit test for function split_args
def test_split_args():
    # simple case
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # strings only
    assert split_args('"a b" "c d"') == ['"a b"', '"c d"']

    # escape characters
    assert split_args(r'a\ b "c\nd"') == [r'a\ b', r'"c\nd"']

    # whitespace handling
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # multi-line
    assert split_args('a=b \nc="foo \nbar"') == ['a=b', 'c="foo \nbar"']

    # multi-line

# Generated at 2022-06-13 04:40:52.538192
# Unit test for function split_args