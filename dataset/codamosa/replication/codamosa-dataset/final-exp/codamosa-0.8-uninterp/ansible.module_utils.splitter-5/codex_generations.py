

# Generated at 2022-06-13 04:31:12.765833
# Unit test for function split_args
def test_split_args():
    import sys
    import ansible.module_utils.basic

    if sys.version_info[0] >= 3:
        builtin_module = "builtins"
    else:
        builtin_module = "__builtin__"


# Generated at 2022-06-13 04:31:22.197500
# Unit test for function split_args
def test_split_args():
    args_str = "a=b 'c=d' e='f g' h='i j' 'k l'"

    # test with split on spaces
    params = split_args(args_str)
    assert params == ['a=b', 'c=d', 'e=f g', 'h=i j k l']

    # test with split on newlines
    params = split_args('\n'.join(args_str.split()))
    assert params == ['a=b', 'c=d', 'e=f g', 'h=i j', 'k l']

    # test with split on both spaces and newlines
    params = split_args('\n'.join(args_str.split()).replace(' ', '\n'))

# Generated at 2022-06-13 04:31:27.100049
# Unit test for function split_args

# Generated at 2022-06-13 04:31:34.651928
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b 'c=\"foo bar\"' d={{ e={{f}} }}") == ['a=b', 'c=\"foo bar\"', 'd={{ e={{f}} }}']
    assert split_args("a=b 'c=\"foo bar\"' d={{ e={{f}} }}") == split_args("a=b c=\"foo bar\" d={{ e={{f}} }}")
    assert split_args("a=b c=\"foo \\\"bar\"") == ['a=b', 'c=\"foo \\\"bar\"']

# Generated at 2022-06-13 04:31:45.292196
# Unit test for function split_args
def test_split_args():
    def check_it(args, expected):
        got = split_args(args)
        if expected != got:
            import difflib
            diff = difflib.unified_diff(expected, got)
            err = ""
            for line in diff:
                err += line
            raise AssertionError('test_split_args test failed (%s != %s):\n%s' % (expected, got, err))


# Generated at 2022-06-13 04:31:56.553660
# Unit test for function split_args
def test_split_args():
    # these first few should be easy
    assert split_args("foo") == ["foo"]
    assert split_args(" foo") == ["foo"]
    assert split_args(" foo ") == ["foo"]
    assert split_args(" foo bar ") == ["foo bar"]
    assert split_args(" foo bar baz ") == ["foo bar baz"]
    assert split_args("foo bar baz") == ["foo", "bar", "baz"]
    assert split_args("foo 'bar baz'") == ["foo", "'bar baz'"]
    assert split_args("foo \"bar baz\"") == ["foo", "\"bar baz\""]
    assert split_args("foo 'bar baz' zzz") == ["foo", "'bar baz'", "zzz"]

# Generated at 2022-06-13 04:32:03.827892
# Unit test for function is_quoted
def test_is_quoted():
    test_data = [
        'the quick brown fox jumped over the lazy dog',
        '"the quick brown fox jumped over the lazy dog"',
        "'the quick brown fox jumped over the lazy dog'",
        '""',
        "''",
    ]
    for d in test_data:
        assert is_quoted(d) == (d[0] == d[-1] == '"' or d[0] == d[-1] == "'")



# Generated at 2022-06-13 04:32:13.591106
# Unit test for function split_args
def test_split_args():
    # args without any jinja2 blocks or quotes
    print('test 1')
    args = 'foo bar baz'
    result = split_args(args)
    print(result)
    assert result == ['foo', 'bar', 'baz']

    # args with quoted values
    print('test 2')
    args = 'foo bar baz="hello world" cat'
    result = split_args(args)
    print(result)
    assert result == ['foo', 'bar', 'baz="hello world"', 'cat']

    # args with quoted values with spaces
    print('test 3')
    args = 'foo bar baz="hello world" cat'
    result = split_args(args)
    print(result)
    assert result == ['foo', 'bar', 'baz="hello world"', 'cat']

    #

# Generated at 2022-06-13 04:32:21.643067
# Unit test for function split_args
def test_split_args():
    args = '''{% set x = {'k1':'v1', 'k2':'v2', 'k3':'v3'} %}
{{ x.k1 }}
{{ x.k2 }}
{{ x.k3 }}
'''
    result = split_args(args)
    assert len(result) == 15
    assert result[0] == '{%'
    assert result[1] == 'set'
    assert result[2] == 'x'
    assert result[3] == '='
    assert result[4] == '{'
    assert result[5] == "'k1':'v1',"
    assert result[6] == "'k2':'v2',"
    assert result[7] == "'k3':'v3'"
    assert result[8] == '}'
    assert result

# Generated at 2022-06-13 04:32:31.415393
# Unit test for function split_args
def test_split_args():
    assert split_args(u'a=b c="foo bar"') == [u'a=b', u'c="foo bar"']
    assert split_args(u'a=b c=') == [u'a=b', u'c=']
    assert split_args(u'a=b "c=') == [u'a=b', u'c=']
    assert split_args(u'a=b "c=" d=\\') == [u'a=b', u'c=', u'd=\\']
    assert split_args(u'a=b "c=\\" d=\\') == [u'a=b', u'c=" d=\\']

# Generated at 2022-06-13 04:32:53.771615
# Unit test for function split_args
def test_split_args():
    assert ['a=b', 'c="foo bar"'] == split_args("a=b c=\"foo bar\"")
    assert ['a=b', 'c="foo bar"', 'd="hello world"'] == split_args("a=b c=\"foo bar\" d=\"hello world\"")
    assert ['a=b', 'c="foo bar"', 'd="hello world"', 'e="hello\'world"'] == split_args("a=b c=\"foo bar\" d=\"hello world\" e=\"hello\'world\"")
    assert ['a=b', 'c="foo bar"', 'd="hello world"', 'e="hello\'world"', 'f="hello\\"world"'] == split_args("a=b c=\"foo bar\" d=\"hello world\" e=\"hello\'world\" f=\"hello\\\"world\"")

# Generated at 2022-06-13 04:33:04.689818
# Unit test for function split_args

# Generated at 2022-06-13 04:33:12.931544
# Unit test for function split_args
def test_split_args():
    # Basic tests
    assert split_args("") == []
    assert split_args("a=b") == ["a=b"]
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    assert split_args("a=b\nc=d") == ["a=b\n", "c=d"]
    # Test with quotes
    assert split_args("a='b c'") == ["a='b c'"]
    assert split_args("a='b c' d='e f'") == ["a='b c'", "d='e f'"]
    assert split_args("a='b c' 'd e'") == ["a='b c'", "'d e'"]

# Generated at 2022-06-13 04:33:25.660296
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\" d='baz foobar'") == ['a=b', 'c="foo bar"', "d='baz foobar'"]
    assert split_args("a=\"{{ b }}\"") == ['a="{{ b }}"']
    assert split_args("a=\"{{ b }}\" c=\"foo bar\"") == ['a="{{ b }}"', 'c="foo bar"']
    assert split_args("a=\"{{ b }}\" c=\"{{ d }}\"") == ['a="{{ b }}"', 'c="{{ d }}"']
    assert split_args("a=\"{{ b }}{{ c }}\"") == ['a="{{ b }}{{ c }}"']

# Generated at 2022-06-13 04:33:31.377221
# Unit test for function split_args
def test_split_args():

    def check(s1, s2):
        p1 = split_args(s1)
        p2 = split_args(s2)
        if p1 != p2:
            raise ValueError("%s != %s" % (p1, p2))

    check("", "")
    check(" ", "")
    check("a=b c=d", "a=b c=d")
    check("  a=b c=d", "a=b c=d")
    check("  a=b c=d  ", "a=b c=d")
    check("  a=b c=d  ", "  a=b c=d  ")
    check("a='b c=d'", "a='b c=d'")

# Generated at 2022-06-13 04:33:43.164776
# Unit test for function split_args
def test_split_args():
    """
    Test split_args function.
    """


# Generated at 2022-06-13 04:33:53.962879
# Unit test for function split_args
def test_split_args():
    # TODO: update tests so they're not as brittle
    assert split_args('') == ['']
    assert split_args('    ') == ['']
    assert split_args('"foo bar"') == ['foo bar']
    assert split_args("foo='bar baz'") == ["foo='bar baz'"]
    assert split_args('""') == ['']
    assert split_args("''") == ['']
    assert split_args('"foo bar') == ['foo bar']
    assert split_args("foo='bar baz") == ["foo='bar baz"]
    assert split_args('"foo bar " foobaz') == ['foo bar ', 'foobaz']
    assert split_args("foo='bar baz ' foobaz") == ["foo='bar baz '", 'foobaz']

# Generated at 2022-06-13 04:34:03.871565
# Unit test for function split_args
def test_split_args():
    assert split_args("src=/tmp/foo.yml dest=/tmp/bar.yml") == ["src=/tmp/foo.yml", "dest=/tmp/bar.yml"]
    assert split_args("src='/tmp/foo.yml' dest=\"/tmp/bar.yml\"") == ["src=/tmp/foo.yml", "dest=/tmp/bar.yml"]
    assert split_args("src='/tmp/foo.yml' dest=\"/tmp/bar.yml\"") == ["src=/tmp/foo.yml", "dest=/tmp/bar.yml"]
    assert split_args("src='/tmp/foo.yml' dest=\"/tmp/bar.yml\"") == ["src=/tmp/foo.yml", "dest=/tmp/bar.yml"]

# Generated at 2022-06-13 04:34:08.612109
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"')
    assert is_quoted("'test'")
    assert not is_quoted('test"')
    assert not is_quoted('test')
    assert not is_quoted('"test')
    assert is_quoted('""')
    assert not is_quoted('\'test')
    assert is_quoted('\'\'')


# Generated at 2022-06-13 04:34:14.792653
# Unit test for function split_args
def test_split_args():
    ''' ensure that split_args properly handles all cases '''

    assert split_args('ls -l') == ['ls', '-l']
    assert split_args('ls "foo bar"') == ['ls', '"foo bar"']
    assert split_args('ls "foo bar') == ['ls', '"foo bar']
    assert split_args('ls "foo bar\\') == ['ls', '"foo bar\\']
    assert split_args('ls "foo bar" baz') == ['ls', '"foo bar"', 'baz']
    assert split_args('ls "foo bar"\\') == ['ls', '"foo bar"\\']
    assert split_args('ls "foo bar"\\\n\\') == ['ls', '"foo bar"\\\n\\']

# Generated at 2022-06-13 04:34:36.891999
# Unit test for function split_args
def test_split_args():

    tests = dict()
    tests['simple'] = ('foo=bar baz=biz', ['foo=bar', 'baz=biz'])
    tests['mixed'] = ('foo="bar baz" biz=baz', ['foo="bar baz"', 'biz=baz'])
    tests['complex'] = ('{"foo":"bar baz"}', ['{"foo":"bar baz"}'])
    tests['complex2'] = ('{"foo":"bar baz"} {"foo2":"bar2 baz2"}', ['{"foo":"bar baz"}', '{"foo2":"bar2 baz2"}'])
    tests['jinja'] = ('{% foo bar %}', ['{% foo bar %}'])
    tests['jinja2'] = ('{{ foo bar }}', ['{{ foo bar }}'])
    tests['jinja3']

# Generated at 2022-06-13 04:34:45.150088
# Unit test for function split_args
def test_split_args():
    ''' simple unit test for module argument splitting '''

    # basic sanity test
    a = split_args("a=1")
    assert len(a) == 1
    assert a[0] == 'a=1'

    a = split_args("a=2 b=2")
    assert len(a) == 2
    assert a[0] == 'a=2' and a[1] == 'b=2'

    # test with escaped characters
    a = split_args("a=\"foo\\\\\" b=2 c=3")
    assert len(a) == 3
    assert a[0] == 'a="foo\\\\"' and a[1] == 'b=2' and a[2] == 'c=3'

    # test with escaped quotes inside quotes

# Generated at 2022-06-13 04:34:56.711775
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b") == ['a=b']
    assert split_args('a="foo bar"') == ['a="foo bar"']
    assert split_args('a="foo bar" d=c') == ['a="foo bar"', 'd=c']
    assert split_args('arg1="foo bar" arg2="baz \'qux\' 123"') == ['arg1="foo bar"', 'arg2="baz \'qux\' 123"']
    assert split_args('a={{foo}} b="foo bar" d="{{biz}}"') == ['a={{foo}}', 'b="foo bar"', 'd="{{biz}}"']

# Generated at 2022-06-13 04:35:07.640377
# Unit test for function split_args
def test_split_args():
    # Prompt for jinja2 template only supports one line for the command
    # To simulate multi-line commands, we use strings with '\n' in them.
    # Note that the command should end with '\n' to indicate end of command.
    #   command with no args
    assert split_args('command') == ['command']
    assert split_args('command\n') == ['command\n']
    #   command with one arg
    assert split_args('command arg') == ['command', 'arg']
    assert split_args('command arg\n') == ['command', 'arg\n']
    #   command with multiple args
    assert split_args('command arg1 arg2') == ['command', 'arg1', 'arg2']

# Generated at 2022-06-13 04:35:18.092558
# Unit test for function split_args
def test_split_args():

    assert split_args("") == [], "splitting '' should give us back an empty list"
    assert split_args("a=b") == ['a=b'], "splitting 'a=b' should give us back a single param"
    assert split_args("a=b c=d") == ['a=b', 'c=d'], "splitting 'a=b c=d' should give us back two params"
    assert split_args("a=\"b c\"") == ['a="b c"'], "splitting 'a=\"b c\"' should give us back a single param"
    assert split_args("a=\"b c\" d=e") == ['a="b c"', 'd=e'], "splitting 'a=\"b c\" d=e' should give us back two params"

# Generated at 2022-06-13 04:35:26.208495
# Unit test for function split_args
def test_split_args():
    # Argument without quotes
    args = 'key value'
    result = split_args(args)
    assert result == ['key', 'value']

    # Argument with quotes
    args = 'key "value 1" "value 2"'
    result = split_args(args)
    assert result == ['key', '"value 1"', '"value 2"']

    # Argument with single quotes
    args = 'key \'value 1\' \'value 2\''
    result = split_args(args)
    assert result == ['key', "'value 1'", "'value 2'"]

    # Empty string
    args = ''
    result = split_args(args)
    assert result == ['']

    # Argument with backslash
    args = r'key value\ 1 value\ 2'
    result = split_args(args)

# Generated at 2022-06-13 04:35:37.181614
# Unit test for function split_args

# Generated at 2022-06-13 04:35:46.724602
# Unit test for function split_args

# Generated at 2022-06-13 04:35:55.466479
# Unit test for function split_args

# Generated at 2022-06-13 04:36:03.689695
# Unit test for function split_args
def test_split_args():
    # Simple key value pair
    assert split_args('a=b') == ['a=b']

    # Simple key value pair with whitespace
    assert split_args(' a = b ') == ['a=b']

    # Simple key value pair with whitespace and quotes
    assert split_args('a = "b"') == ['a=b']

    # empty string
    assert split_args('') == []

    # whitespace only
    assert split_args('  ') == []

    # Multi-line output
    assert split_args('a=b\nc="d"') == ['a=b', 'c=d']

    # Nested jinja2 block
    assert split_args('a={{ b }}') == ['a={{ b }}']

    # Multi-line output with nested jinja2 block
    assert split

# Generated at 2022-06-13 04:36:46.584673
# Unit test for function split_args
def test_split_args():
    # Test that several simple, good cases work

    for args in ["", "a=b c='d e' f=' g  h '", "a=b c='d e' f=' g h '",
                 "a=b c='d e' f=' g '' h '", "a=b c='d e' f=' g \" h '"]:
        assert args.split() == split_args(args)

    # Test that backslash escapes are passed through, and that newlines
    # are preserved.

    assert ['foo\\bar', 'baz=\\' '\n', 'bif'] == split_args('foo\\bar baz=\\ \n bif')

    # Test that backslash escapes are passed through, and that newlines
    # are preserved even when they occur within quotes.


# Generated at 2022-06-13 04:36:57.039639
# Unit test for function split_args
def test_split_args():

    assert split_args('') == []

    assert split_args('"foo bar"') == ['"foo bar"']

    assert split_args('"foo \n bar"') == ['"foo \n bar"']

    assert split_args('"foo \n bar" "baz \n quux"') == ['"foo \n bar"', '"baz \n quux"']

    assert split_args('a=b') == ['a=b']

    assert split_args('a=b\n c=d') == ['a=b\n', 'c=d']

    assert split_args('a=b\n c=d \n e=f') == ['a=b\n', 'c=d', 'e=f']


# Generated at 2022-06-13 04:37:02.903095
# Unit test for function split_args
def test_split_args():
    fails = []

    # Test that plain args can be split
    test = split_args('echo foo')
    if test != ['echo', 'foo']:
        fails.append("Plain args fail: {}".format(test))

    # Test that quoted arg can be split
    test = split_args('echo "foo bar"')
    if test != ['echo', '"foo bar"']:
        fails.append("Quoted arg fail: {}".format(test))

    # Test that split args can be reassembled inside quotes
    test = split_args('echo "foo bar"')
    if test != ['echo', '"foo bar"']:
        fails.append("Split arg fail: {}".format(test))

    # Test that quoted args can be split when multiple args are used

# Generated at 2022-06-13 04:37:07.676297
# Unit test for function split_args

# Generated at 2022-06-13 04:37:20.533767
# Unit test for function split_args
def test_split_args():
    # Verify basic functionality
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']

    # Verify that a escaped newline character is returned as part of the same argument
    assert split_args("a=b\\\nc=d") == ['a=b\\\nc=d']

    # Verify that a escaped newline character is returned as part of the same argument
    # even when the line continues on the next line
    assert split_args("a=b\\\n  c=d") == ['a=b\\\n  c=d']

    # Verify a quoted string that spans multiple lines is returned as a single argument
    assert split_args("msg: \"this is\na multi-line string\"") == ['msg: "this is\na multi-line string"']

    # Verify a quoted string

# Generated at 2022-06-13 04:37:31.969350
# Unit test for function split_args

# Generated at 2022-06-13 04:37:42.316522
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):

        def test_split_args_basic(self):
            # Ensure split_args works on a simple string
            data = 'hello world'
            results = split_args(data)
            self.assertEqual(results, ['hello', 'world'])

        def test_split_args_basic_quotes(self):
            # Ensure split_args works on a string with quotes
            data = 'hello "world"'
            results = split_args(data)
            self.assertEqual(results, ['hello', '"world"'])

        def test_split_args_basic_double_quotes(self):
            # Ensure split_args works on a string with double quotes
            data = 'hello "world" it is'
           

# Generated at 2022-06-13 04:37:48.486412
# Unit test for function split_args
def test_split_args():
    ''' unit test for function split_args '''

    # Test basic parsing of simple args
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args("foo=bar baz=qux") == ['foo=bar', 'baz=qux']
    assert split_args("foo='bar baz' qux='bar baz'") == ["foo='bar baz'", "qux='bar baz'"]

    # Test parsing of line continuations
    # A line continuation is when a space-separated token is followed by a
    # backslash ('\') character.  This should allow the token to be parsed
    # as a single token, even though it would normally be interpreted as
    # two tokens separated by a space.

# Generated at 2022-06-13 04:37:59.072144
# Unit test for function split_args
def test_split_args():

    def check_args(input, expected):

        output = split_args(input)
        if expected != output:
            print("ERROR: split_args output mismatch")
            print("Expected:")
            print(expected)
            print("Got:")
            print(output)

    # Simple
    check_args("a=b c=d e=\"foo bar\"", [ 'a=b', 'c=d', 'e="foo bar"' ] )

    # Quoted with escaped quotes
    check_args(r"a=\"b\" c=\"foo\\\"bar\"", [ 'a="b"', 'c="foo\"bar"' ])

    # Quoted with escaped quotes
    check_args(r"a='b' c='foo\\\"bar'", [ "a='b'", 'c=\'foo"bar\'' ])

    # Qu

# Generated at 2022-06-13 04:38:05.111142
# Unit test for function split_args

# Generated at 2022-06-13 04:39:20.388050
# Unit test for function split_args

# Generated at 2022-06-13 04:39:29.046222
# Unit test for function split_args
def test_split_args():
    # An empty arg string should work
    assert split_args("") == []

    # A simple arg string should work
    assert split_args("foo=bar") == ["foo=bar"]

    # Quotes should work
    assert split_args("foo='this is a quote'") == ["foo='this is a quote'"]

    # Quotes with spaces should work
    assert split_args("foo='this is a quote' bar='another one'") == ["foo='this is a quote'", "bar='another one'"]

    # Quoted quotes should work
    assert split_args("foo='this is \"a quote\"'") == ["foo='this is \"a quote\"'"]

    # Single quotes should work
    assert split_args("foo=\"this is a quote\"") == ["foo=\"this is a quote\""]

    # Arguments without quotes should

# Generated at 2022-06-13 04:39:36.707286
# Unit test for function split_args
def test_split_args():
    assert split_args("") == []
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a='b c'") == ['a=\'b c\'']
    assert split_args("a='b c' d='e f'") == ['a=\'b c\'', 'd=\'e f\'']
    assert split_args("a='b c' d='e f'") == ['a=\'b c\'', 'd=\'e f\'']
    assert split_args("a='b c' d='e f' g") == ['a=\'b c\'', 'd=\'e f\'', 'g']

# Generated at 2022-06-13 04:39:42.430606
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    import ansible.utils.template
    from ansible.utils.template import unsafe_variable_fail

    nil_args = [
        "",
        " ",
        "\t",
        "\n",
    ]

    for nil_arg in nil_args:
        assert [] == split_args(nil_arg)

    def runner(args_str, args_list):
        actual_args_list = split_args(args_str)
        assert args_list == actual_args_list, "String '%s' split incorrectly into %s instead of %s" \
                                              % (args_str, actual_args_list, args_list)


# Generated at 2022-06-13 04:39:47.944964
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', 'c=\'foo bar\'']
    assert split_args("a=b c=foo\\ bar") == ['a=b', 'c=foo bar']
    assert split_args("a=b c={{ foo }}") == ['a=b', 'c={{ foo }}']
    assert split_args("a=b c={{ 'foo' }}") == ['a=b', 'c={{ \'foo\' }}']

# Generated at 2022-06-13 04:39:56.952912
# Unit test for function split_args

# Generated at 2022-06-13 04:40:05.116231
# Unit test for function split_args
def test_split_args():
    assert split_args("test") == ['test']
    assert split_args("test \"foo bar\"") == ['test', '"foo bar"']
    assert split_args("test\n\"foo bar\"") == ['test', '"foo bar"']
    assert split_args("test \"foo bar\"\n") == ['test', '"foo bar"']
    assert split_args("test \"foo\nbar\"") == ['test', '"foo\nbar"']
    assert split_args("test \"foo\\\nbar\"") == ['test', '"foobar"']
    assert split_args("test\n\"foo\\\nbar\"") == ['test', '"foobar"']
    assert split_args("test\n\"foo\\\nbar\"\n") == ['test', '"foobar"']

# Generated at 2022-06-13 04:40:12.171986
# Unit test for function split_args
def test_split_args():
    result = split_args('foo bar')
    assert result == ['foo', 'bar']

    result = split_args('foo "bar baz"')
    assert result == ['foo', '"bar baz"']

    result = split_args('foo "bar baz" jinja2="foo bar"')
    assert result == ['foo', '"bar baz"', 'jinja2="foo bar"']

    result = split_args('foo "bar baz" jinja2={{foo}}')
    assert result == ['foo', '"bar baz"', 'jinja2={{foo}}']

    result = split_args('foo "bar baz" jinja2={{foo}} \\')
    assert result == ['foo', '"bar baz"', 'jinja2={{foo}}']

    result = split_

# Generated at 2022-06-13 04:40:22.786697
# Unit test for function split_args

# Generated at 2022-06-13 04:40:31.289023
# Unit test for function split_args