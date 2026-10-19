

# Generated at 2022-06-13 04:31:12.172454
# Unit test for function split_args
def test_split_args():
    import copy


# Generated at 2022-06-13 04:31:19.105169
# Unit test for function split_args
def test_split_args():
    # these examples are from the original document that described the problem with parsing
    # args originally: https://github.com/ansible/ansible/issues/4040

    def _run(args, result):
        params = split_args(args)
        assert params == result, "%s != %s" % (params, result)

    _run("a=b c=d", ["a=b", "c=d"])
    _run("a=b 'c d'", ["a=b", "'c d'"])
    _run("a=b 'c d' e=f", ["a=b", "'c d'", "e=f"])
    _run("a=b \"c d\"", ["a=b", "\"c d\""])

# Generated at 2022-06-13 04:31:25.362788
# Unit test for function is_quoted
def test_is_quoted():
    assert not is_quoted("")
    assert not is_quoted("foo")
    assert is_quoted("foobar")
    assert is_quoted("'foobar'")
    assert is_quoted("\"foobar\"")
    assert not is_quoted("foo\"bar")


# Generated at 2022-06-13 04:31:28.034785
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("test") == False
    assert is_quoted("\'test\'") == True
    assert is_quoted("\"test\"") == True


# Generated at 2022-06-13 04:31:32.587616
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"')
    assert is_quoted("'foo'")
    assert not is_quoted('"foo\'')
    assert not is_quoted('\'foo"')
    assert not is_quoted('foo')
    assert not is_quoted('foo"')
    assert not is_quoted('"foo')



# Generated at 2022-06-13 04:31:38.414067
# Unit test for function is_quoted
def test_is_quoted():
    data = '"abcd efg hijk"'
    assert is_quoted(data)
    data = "'abcd'"
    assert is_quoted(data)
    data = "'abcd' efg 'hijk'"
    assert not is_quoted(data)
    data = ""
    assert not is_quoted(data)


# Generated at 2022-06-13 04:31:45.004682
# Unit test for function split_args
def test_split_args():
    import os
    import tempfile

    fd, tmpfilename = tempfile.mkstemp(prefix='ansible-test_split_args-')
    f = os.fdopen(fd, 'w')

    f.write("""
        '''
        this is a multiline
        string
        '''
        """)
    f.close()

    f = open(tmpfilename)
    test_content = f.read().strip()

    os.remove(tmpfilename)
    assert len(split_args(test_content)) == 1

    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']

# Generated at 2022-06-13 04:31:56.206748
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c=\"foo bar\" d='foo bar'") == ['a=b', "c=\"foo bar\"", "d='foo bar'"]
    assert split_args("a=b c=foo\\\nbar") == ['a=b', "c=foo\\"]
    assert split_args("a=b c={{foo}}") == ['a=b', "c={{foo}}"]
    assert split_args("a=b c='{{foo}} \\'") == ['a=b', "c='{{foo}} \\'"]

# Generated at 2022-06-13 04:32:08.523907
# Unit test for function split_args

# Generated at 2022-06-13 04:32:16.106329
# Unit test for function split_args
def test_split_args():
    x = 'a b="foo bar" c=\\" d="\"'
    x2 = "a='foo bar' b=\"a 'b' c\" c=\\"
    x3 = '''a="foo \'bar'" b=\\"'''
    x4 = '''a=b c=d e="foo bar"'''
    x5 = "a=b c='foo bar'"
    x6 = "a='foo'\"'bar'"
    x7 = "a=b c=d e='foo bar'"
    x8 = "a=b c='foo\\'bar'"
    x9 = "a=b c=\\'foo bar\\'"
    x10 = "a=b c='foo\nbar'"
    x11 = "a=b c=\\'foo\nbar\\'"

# Generated at 2022-06-13 04:32:40.620044
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest


# Generated at 2022-06-13 04:32:50.739288
# Unit test for function split_args
def test_split_args():
    # Note: the goal here is to verify the parsing behavior, not the actual args
    # that are returned.  The actual args are subject to change, based on use
    # cases that pop up.

    # trivial cases
    assert split_args("") == []
    assert split_args("a") == ["a"]
    assert split_args("a b") == ["a", "b"]

    # whitespace should be stripped
    assert split_args(" a b ") == ["a", "b"]

    # simple quotes pass through
    assert split_args("'a b'") == ["'a b'"]

    # but quotes are stripped when they wrap whitespace
    assert split_args("' a b '") == ["a b"]

    # this is the case for ec2_vol, for example

# Generated at 2022-06-13 04:33:01.766177
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo \\"bar\\""') == ['a=b', 'c="foo \\"bar\\""']
    assert split_args('a=b c="foo bar\\""') == ['a=b', 'c="foo bar\\""']

    # test that line continuations don't split tokens
    assert split_args('''a=b \
c=d''') == ['a=b', 'c=d']
    # and also that a trailing backslash doesn't create an empty token
    assert split_args('''a=b c=d\\''') == ['a=b', 'c=d\\']

    # test that the line continuation and line continuation with quotes
    #

# Generated at 2022-06-13 04:33:10.732884
# Unit test for function split_args
def test_split_args():
    ignored = ['module_defaults', 'playbook_dir', 'playbook_path', 'playbook_vars', 'playbook_vars_files', 'playbook_vars_prompt', 'playbook_vars_files_prompt', 'playbook_python_interpreter', 'playbook_ssh_common_args', 'playbook_ssh_extra_args', 'playbook_scp_extra_args', 'playbook_become_extra_args']

    # test_data contains a list of strings and the expected result of split_args on that string

# Generated at 2022-06-13 04:33:21.973793
# Unit test for function split_args

# Generated at 2022-06-13 04:33:33.852849
# Unit test for function split_args

# Generated at 2022-06-13 04:33:45.461153
# Unit test for function split_args
def test_split_args():
    assert split_args(u'foo=bar') == [u'foo=bar']
    assert split_args(u'foo="bar baz"') == [u'foo="bar baz"']
    assert split_args(u'foo="bar baz" bar=baz') == [u'foo="bar baz"', u'bar=baz']
    assert split_args(u'foo="bar \\"baz\\"') == [u'foo="bar \\"baz\\"']
    assert split_args(u'foo="bar baz') == [u'foo="bar baz']
    assert split_args(u'foo="bar') == [u'foo="bar']
    assert split_args(u'foo="bar\\"') == [u'foo="bar\\"']

# Generated at 2022-06-13 04:33:55.615178
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b "a=b c=d" x="foo bar"') == ['a=b', '"a=b c=d"', 'x="foo bar"']
    assert split_args(r'a=b "a=b c=d" x="foo\"bar"') == ['a=b', '"a=b c=d"', 'x="foo\"bar"']
    assert split_args(r"a=b 'a=b c=d' x='foo\"bar'") == ['a=b', "'a=b c=d'", "x='foo\"bar'"]

# Generated at 2022-06-13 04:34:05.435908
# Unit test for function split_args

# Generated at 2022-06-13 04:34:12.864610
# Unit test for function split_args
def test_split_args():
    # ensure that the ordering of args is preserved
    # when we split them
    split_unquoted = split_args("foo=bar baz=foo")
    assert split_unquoted == ['foo=bar', 'baz=foo']

    # Ensure that the ordering of args is preserved when we have quotes
    split_quoted = split_args("foo=bar baz='foo bar'")
    assert split_quoted == ['foo=bar', 'baz=\'foo bar\'']

    split_multi_line = split_args("foo=bar\nbaz=foo")
    assert split_multi_line == ['foo=bar\n', 'baz=foo']

    split_multi_line_and_quoted = split_args("foo=bar\nbaz='foo bar'")
    assert split_multi_line_and_qu

# Generated at 2022-06-13 04:34:41.521854
# Unit test for function split_args

# Generated at 2022-06-13 04:34:52.670568
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b \'c="foo bar"\'') == ['a=b', '\'c="foo bar"\'']
    assert split_args("a=b 'c=\"foo bar\"'") == ['a=b', '\'c="foo bar"\'']
    assert split_args("a=b 'c=\"foo bar\"' d='foo'bar'") == ['a=b', '\'c="foo bar"\'', 'd=\'foo\'bar\'']
    assert split_args('echo "foo\\nbar"') == ['echo', '"foo\\nbar"']

# Generated at 2022-06-13 04:35:04.850108
# Unit test for function split_args

# Generated at 2022-06-13 04:35:12.899815
# Unit test for function split_args
def test_split_args():
    def assert_split_args(args, expected):
        actual = split_args(args)
        assert actual == expected, 'error parsing "%s", expected=%s, actual=%s' % (args, expected, actual)

    # Test that simple args with no quotes or jinja2 processing work
    assert_split_args('foo bar baz', ['foo', 'bar', 'baz'])

    # Test that multiple lines works
    assert_split_args('foo\nbar\nbaz', ['foo\n', 'bar\n', 'baz'])

    # Test that single quotes work
    assert_split_args('foo bar "baz" bax', ['foo', 'bar', '"baz"', 'bax'])

    # Test that escaped=True lets single quotes pass through

# Generated at 2022-06-13 04:35:22.914109
# Unit test for function split_args

# Generated at 2022-06-13 04:35:27.764760
# Unit test for function split_args
def test_split_args():
    # test empty string
    assert split_args('') == []

    # test single word
    assert split_args('foobar') == ['foobar']

    # test single quoted word
    assert split_args(r'"foo bar"') == [r'"foo bar"']
    assert split_args(r"'foo bar'") == [r"'foo bar'"]
    assert split_args(r"a=b") == ['a=b']

    # test quoted string with quote in it
    assert split_args(r'"foo \' bar"') == [r'"foo \' bar"']
    assert split_args(r'"foo "bar" baz"') == [r'"foo "bar" baz"']

    # test quoted string with escaped quote in it

# Generated at 2022-06-13 04:35:38.931957
# Unit test for function split_args

# Generated at 2022-06-13 04:35:45.792700
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"{{ foo }}\"") == ['a=b', 'c="{{ foo }}"']
    assert split_args("a=b c=\"{{ foo }}\" e='abc'") == ['a=b', 'c="{{ foo }}"', 'e=\'abc\'']
    assert split_args("a=b c='{{ foo }}' e=\"abc\"") == ['a=b', 'c=\'{{ foo }}\'', 'e="abc"']

# Generated at 2022-06-13 04:35:54.746348
# Unit test for function split_args

# Generated at 2022-06-13 04:36:03.076935
# Unit test for function split_args
def test_split_args():
    ''' A test routine for split_args '''
    import pprint

# Generated at 2022-06-13 04:36:57.147908
# Unit test for function split_args

# Generated at 2022-06-13 04:37:02.974613
# Unit test for function split_args
def test_split_args():
    def test(args, expected):
        result = split_args(args)
        assert result == expected, 'failed to split_args(%s): expected %s, got %s' % (args, result, expected)
    test('a=b c="foo bar" d=\'foo bar\' e="foo\'bar" f=\'foo"bar\'', ['a=b', 'c="foo bar"', "d='foo bar'", 'e="foo\'bar"', 'f=\'foo"bar\''])
    test('a=foo bar', ['a=foo bar'])
    test('a="foo bar"', ['a="foo bar"'])
    test('a=b c=c', ['a=b', 'c=c'])

# Generated at 2022-06-13 04:37:07.780628
# Unit test for function split_args
def test_split_args():
    # Test that the args are split correctly
    args = "a=b c=\"foo bar\""
    params = split_args(args)
    assert(params == ['a=b', 'c="foo bar"'])

    # Test that line continuation is handled correctly
    args = "a=b \\\nc=\"foo bar\""
    params = split_args(args)
    assert(params == ['a=b', '\nc="foo bar"'])

    # Test that quotes and line continuation are handled correctly
    args = "a=b \\\nc=\"foo \\\nbar\""
    params = split_args(args)
    assert(params == ['a=b', '\nc="foo \\\nbar"'])

    # Test that jinja2 blocks are handled correctly

# Generated at 2022-06-13 04:37:20.667248
# Unit test for function split_args
def test_split_args():
    assert split_args("") == []
    assert split_args("foo=bar") == ['foo=bar']
    assert split_args("foo='x y'") == ['foo=\'x y\'']
    assert split_args("foo=\"x y\"") == ['foo="x y"']
    assert split_args("foo=bar \"x y\" baz='a b'") == ['foo=bar', '"x y"', "baz='a b'"]
    assert split_args("foo={{ bar }}") == ['foo={{ bar }}']
    assert split_args("foo=\"{{ bar }}\"") == ['foo="{{ bar }}"']
    assert split_args("foo=\"{{ bar }}baz\"") == ['foo="{{ bar }}baz"']

# Generated at 2022-06-13 04:37:32.121129
# Unit test for function split_args
def test_split_args():
    assert split_args('foo=bar key=\'value with spaces\'') == ['foo=bar', 'key=\'value with spaces\'']
    assert split_args('foo=bar key=\'value with spaces\'') == ['foo=bar', 'key=\'value with spaces\'']
    assert split_args('foo=bar "key=\'value with spaces\'"') == ['foo=bar', '"key=\'value with spaces\'"']
    assert split_args('foo=bar "key=\'value with spaces\' ') == ['foo=bar', '"key=\'value with spaces\' ']
    assert split_args('foo=bar "key=\'value with spaces\'\\') == ['foo=bar', '"key=\'value with spaces\'\\']

# Generated at 2022-06-13 04:37:40.726763
# Unit test for function split_args
def test_split_args():
    assert split_args('"a=b" c="foo bar"') == ['"a=b"', 'c="foo bar"']
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b\nc="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b \nc="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"\\\nd=') == ['a=b', 'c="foo bar"d=']
    assert split_args('a=b c="foo bar"\\\nd=e') == ['a=b', 'c="foo bar"d=e']

# Generated at 2022-06-13 04:37:47.637717
# Unit test for function split_args
def test_split_args():
    def split_test(args, result):
        assert split_args(args) == result

    split_test("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    split_test("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"'])
    split_test("a=b c=\"foo bar\" \\", ['a=b', 'c="foo bar" \\'])
    split_test("a=b c=\\\"foo bar\\\"", ['a=b', 'c=\\"foo bar\\"'])
    split_test("a=b c=\\'foo bar\\'", ['a=b', "c=\\'foo bar\\'"])

    # make sure this works with escaped newlines

# Generated at 2022-06-13 04:37:54.643619
# Unit test for function split_args
def test_split_args():
    # Test some simple cases that should not be split on spaces
    assert split_args('abc def') == ['abc def']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Test a case where a jinja2 block is not ended, but quotes are
    assert split_args('a="foo \"bar' + '\\\n' + 'baz\""') == ['a="foo \"barbaz\""']

    # Test a case where quotes are not ended, but a jinja2 block is
    assert split_args('a="foo bar' + '\\\n' + 'baz"}') == ['a="foo barbaz"}']

    # Test a case where a jinja2 block is split on spaces
    assert split_args('a=\"{{ foo }}\"')

# Generated at 2022-06-13 04:38:02.064263
# Unit test for function split_args

# Generated at 2022-06-13 04:38:13.940917
# Unit test for function split_args
def test_split_args():

    # test a basic example of splitting args
    args = 'a=b c="foo bar"'
    args_list = ['a=b', 'c="foo bar"']
    assert split_args(args) == args_list

    # test quoting inside of double quotes
    args = 'c="foo bar"'
    args_list = ['c="foo bar"']
    assert split_args(args) == args_list

    # test that the shell handles single quotes the same way
    args = "c='foo bar'"
    args_list = ['c="foo bar"']
    assert split_args(args) == args_list

    # test that single quotes are preserved within double quotes
    args = 'c="foo \'bar\'"'
    args_list = ['c="foo \'bar\'"']
    assert split_args(args) == args_

# Generated at 2022-06-13 04:39:43.499072
# Unit test for function split_args

# Generated at 2022-06-13 04:39:48.813563
# Unit test for function split_args
def test_split_args():

    def _test_split_args(args, expected_result):
        result = split_args(args)
        print("\nOriginal input: " + args)
        print("Split tokens: ", result)
        print("Expected split tokens: ", expected_result)

        if len(result) != len(expected_result):
            print("\nSplit args result does not match expected result\n")
            return False

        for idx, item in enumerate(expected_result):
            if result[idx] != item:
                print("\nSplit args result does not match expected result\n")
                return False

        return True

    assert _test_split_args("", [])
    assert _test_split_args("hello world", ["hello", "world"])

# Generated at 2022-06-13 04:39:58.319160
# Unit test for function split_args

# Generated at 2022-06-13 04:40:05.668765
# Unit test for function split_args

# Generated at 2022-06-13 04:40:12.555739
# Unit test for function split_args

# Generated at 2022-06-13 04:40:23.145788
# Unit test for function split_args
def test_split_args():
    '''
    Returns true if split_args function works as intended, false otherwise
    '''

    # Test string, should return ['a', 'b', 'c', 'd']
    test_string_1 = 'a\nb\n c  d'
    if split_args(test_string_1) != ['a', 'b', 'c', 'd']:
        return False

    # Test string 2, should return ['a', 'b', 'c', 'd']
    test_string_2 = 'a \nb c\n d'
    if split_args(test_string_2) != ['a', 'b c', 'd']:
        return False

    # Test string 3, should return ['a', 'b', 'c', 'd']
    test_string_3 = 'a \nb "c \nc" d'


# Generated at 2022-06-13 04:40:31.522500
# Unit test for function split_args
def test_split_args():
    '''Unit tests for function split_args'''

    #Simple test for splitting
    assert (split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"])

    #Test with line continuation
    assert (split_args("a=1 \\\nb=2\nc=3") == ['a=1', 'b=2\nc=3'])

    #Test with line continuation in quotes
    assert (split_args("a=\"\\\nb\"") == ['a="\nb"'])

    #Test with line continuation inside a string
    assert (split_args("a=\\\nfoo") == ['a=foo'])

    #Test with a comment
    assert (split_args("#a") == [])

    #Test inside a comment

# Generated at 2022-06-13 04:40:41.841241
# Unit test for function split_args
def test_split_args():
    # Basic test case
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]

    # More complex test case.
    # Here we check for the full set of escaping capabilities.
    # Unfortunately, we need to duplicate the escape characters
    # for Python syntax string literals and for Jinja templates.

# Generated at 2022-06-13 04:40:50.488989
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c='foo bar' d=\"{{ foo }} and {{ bar }}\"") == ['a=b', "c='foo bar'", 'd="{{ foo }} and {{ bar }}"']
    assert split_args("a=b c=\"foo bar\" d='{{ foo }} and {{ bar }}'") == ['a=b', 'c="foo bar"', "d='{{ foo }} and {{ bar }}'"]
    assert split_args("a='b c' d=\"'foo' bar\"") == ["a='b c'", 'd="\'foo\' bar"']
    assert split_args("d=\"'foo' bar\" a='b c'") == ['d="\'foo\' bar"', "a='b c'"]