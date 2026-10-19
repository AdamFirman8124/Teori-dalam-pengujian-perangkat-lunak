

# Generated at 2022-06-13 04:31:06.193383
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('"foo"') == 'foo'
    assert unquote('foo') == 'foo'



# Generated at 2022-06-13 04:31:11.188350
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"test"') == True
    assert is_quoted("'test'") == True
    assert is_quoted("'test") == False
    assert is_quoted("test'") == False
    assert is_quoted('"test') == False
    assert is_quoted("test") == False



# Generated at 2022-06-13 04:31:15.316478
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('""') == ''
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote("'foo") == "'foo"
    assert unquote('"foo') == "\"foo"
    assert unquote("foo") == "foo"


# Generated at 2022-06-13 04:31:18.263174
# Unit test for function is_quoted
def test_is_quoted():
    data = '"foo"'
    assert is_quoted(data) == True
    # More than one argument
    data = 'foo "bar"'
    assert is_quoted(data) == False
    # More than one argument
    data = 'foo "bar" "baz"'
    assert is_quoted(data) == False


# Generated at 2022-06-13 04:31:30.199242
# Unit test for function split_args
def test_split_args():
    import pytest
    assert split_args("") == ['']
    assert split_args("one two three") == ['one', 'two', 'three']
    assert split_args("one 'two three'") == ['one', "'two three'"]
    assert split_args("one \"two\nthree\"") == ['one', '"two\nthree"']
    assert split_args("one \"two\nthree\" four\nfive six") == ['one', '"two\nthree"', 'four\nfive', 'six']
    assert split_args("one \"two\nthree\" four\nfive six\\\nseven") == ['one', '"two\nthree"', 'four\nfive', 'six\nseven']

    # bug #18582

# Generated at 2022-06-13 04:31:36.121731
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("'hello'")
    assert is_quoted('"hello"')
    assert not is_quoted("'hello")
    assert not is_quoted("hello'")
    assert not is_quoted('"hello')
    assert not is_quoted('hello"')


# Generated at 2022-06-13 04:31:39.194366
# Unit test for function unquote
def test_unquote():
    assert unquote('"abc"') == "abc"
    assert unquote("'abc'") == "abc"
    assert unquote('abc') == "abc"


# Generated at 2022-06-13 04:31:51.872895
# Unit test for function is_quoted
def test_is_quoted():
    # Tests that start and end with the same quotes are correctly identified by the function
    assert is_quoted('"foobar"') == True
    assert is_quoted("'foobar'") == True
    # Tests that start and end with different quotes are correctly identified by the function
    assert is_quoted('"foobar\'') == False
    assert is_quoted("'foobar\"") == False
    # Tests that start and end with a quote and a space respectively are correctly identified by the function
    assert is_quoted('"foobar ') == False
    assert is_quoted(" 'foobar") == False
    # Tests that start with a quote but not end with one are correctly identified by the function
    assert is_quoted('"foobar') == False
    assert is_quoted("'foobar") == False
    # Tests that start

# Generated at 2022-06-13 04:31:58.015778
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"foo"')
    assert is_quoted("'foo'")
    assert not is_quoted('"foo')
    assert not is_quoted("'foo")
    assert not is_quoted('foo"')
    assert not is_quoted("foo'")
    assert not is_quoted('foo')


# Generated at 2022-06-13 04:32:10.056210
# Unit test for function split_args
def test_split_args():
    tests = []

    tests.append(({'args': 'a=b c="foo bar"'}, ['a=b', 'c="foo bar"'], "basic strings"))
    tests.append(({'args': 'module: a=b c="foo bar"'}, ['module:', 'a=b', 'c="foo bar"'], "module keyword and basic strings"))
    tests.append(({'args': 'a="foo bar" c="hello world"'}, ['a="foo bar"', 'c="hello world"'], "quoted strings with spaces"))
    tests.append(({'args': 'a="foo bar" c="hello world" d={{ b }}'}, ['a="foo bar"', 'c="hello world"', 'd={{ b }}'], "quoted strings with mixed jinja2"))

# Generated at 2022-06-13 04:32:31.346270
# Unit test for function split_args
def test_split_args():

    # Split simple vars
    assert split_args('foo=bar name=baz') == ['foo=bar', 'name=baz']

    # Split key / value pairs
    assert split_args('key=value') == ['key=value']

    # Split complex groups of key / value pairs
    assert split_args('key=value key2=value2') == ['key=value', 'key2=value2']
    assert split_args('key=value key2=value2 key3=value3') == ['key=value', 'key2=value2', 'key3=value3']

    # Split with spaces and equals
    assert split_args('key = value') == ['key=value']
    assert split_args('key= value') == ['key=value']

    # Split with quotes
    assert split_args('key="value"')

# Generated at 2022-06-13 04:32:42.176855
# Unit test for function split_args
def test_split_args():
    import copy

    def are_params_valid(expected, actual):
        if len(expected) != len(actual):
            return False

        for idx, param in enumerate(actual):
            if expected[idx] != param:
                return False

        return True

    # Basic test cases
    params = split_args("")
    assert are_params_valid(params, [])

    params = split_args("one")
    assert are_params_valid(params, ["one"])

    params = split_args("one two three")
    assert are_params_valid(params, ["one", "two", "three"])

    params = split_args("one two three\nfour five six")
    assert are_params_valid(params, ["one", "two", "three\nfour", "five", "six"])

   

# Generated at 2022-06-13 04:32:51.858434
# Unit test for function split_args
def test_split_args():
    assert split_args('foo="bar baz"') == ['foo=bar baz']
    assert split_args('a=1 b=2') ==  ['a=1', 'b=2']
    assert split_args('foo="bar \'baz qux\'"') == ['foo=bar \'baz qux\'']
    assert split_args('foo="bar \\"baz qux\\""') == ['foo=bar "baz qux"']
    assert split_args('foo="bar \\\\"baz qux\\\\""') == ['foo=bar \\baz qux\\']
    assert split_args('foo="bar baz" "bam baz"') == ['foo=bar baz', 'bam baz']

# Generated at 2022-06-13 04:33:02.967866
# Unit test for function split_args
def test_split_args():
    '''
    Perform tests on function split_args
    '''
    import os
    import shlex
    import sys
    import yaml
    this_dir = os.path.dirname(__file__)
    src_dir = os.path.join(this_dir, '..')

    if this_dir not in sys.path:
        sys.path.append(this_dir)

    input_file = os.path.join(src_dir, 'test', 'unit', 'argspec_testcases.yaml')
    test_cases = yaml.safe_load(open(input_file).read())
    for idx, test_case in enumerate(test_cases['argspec_test_cases']):

        print("\nTest case %d: %s" % (idx, test_case['testname']))

# Generated at 2022-06-13 04:33:11.653811
# Unit test for function split_args

# Generated at 2022-06-13 04:33:24.177865
# Unit test for function split_args
def test_split_args():

    # some basic tests to ensure that we can properly split/re-assemble args
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b 'c=d'") == ["a=b", "'c=d'"]
    assert split_args("a=b 'c=d e=f'") == ["a=b", "'c=d e=f'"]
    assert split_args("a=b c=\"d e=f\"") == ['a=b', 'c="d e=f"']
    assert split_args("a=b   c=d") == ['a=b', 'c=d']

    # Test that we can properly split/re-assemble args that contain new

# Generated at 2022-06-13 04:33:28.482096
# Unit test for function split_args
def test_split_args():
    # one param
    assert split_args("foo") == ["foo"]
    # multiple params
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    # no split
    assert split_args("foo bar") == ["foo bar"]
    # quoted string, don't split inside
    assert split_args("foo=\"bar baz\"") == ["foo=\"bar baz\""]
    # quoted string, don't split inside, even if we have newlines
    assert split_args("a=b \"foo\nbar\nbaz\"") == ["a=b", "\"foo\nbar\nbaz\""]
    # jinja2 variables
    assert split_args("a={{b}}") == ["a={{b}}"]
    # jinja2 blocks, don't split inside

# Generated at 2022-06-13 04:33:39.783691
# Unit test for function split_args
def test_split_args():

    failed = []

    # simple args
    if split_args("/bin/foo") != ['/bin/foo']:
        failed.append("failed on /bin/foo")

    # simple args with whitespace
    if split_args("/bin/foo   bar") != ['/bin/foo', 'bar']:
        failed.append("failed on /bin/foo   bar")

    # quoted args with whitespace
    if split_args("/bin/foo 'bar baz'") != ['/bin/foo', 'bar baz']:
        failed.append("failed on /bin/foo 'bar baz'")

    # quoted args with escaped quotes

# Generated at 2022-06-13 04:33:51.971181
# Unit test for function split_args
def test_split_args():
    '''
    the purpose of this test is to confirm that the split_args
    function works as expected
    '''

    # confirm error detection on unbalanced jinja2 tokens and quotes

# Generated at 2022-06-13 04:34:02.094535
# Unit test for function split_args
def test_split_args():
    # A simple test with regular args
    result = split_args("a=1 b=foo 'c d'")
    assert result == ["a=1", "b=foo", "'c d'"]

    # A test with whitespace in an arg
    result = split_args("a=b c='foo bar'")
    assert result == ["a=b", "c='foo bar'"]

    # test for comments
    result = split_args('a=b c="#foo bar" d="foo#bar" e="foo#bar#baz" f=\'foo#bar\' g="#foo\nbar"')
    assert result == ['a=b', 'c="#foo bar"', 'd="foo#bar"', 'e="foo#bar#baz"', "f='foo#bar'", 'g="#foo\nbar"']

   

# Generated at 2022-06-13 04:34:25.374135
# Unit test for function split_args
def test_split_args():
    '''
    This function is not used by the codebase in any way, it is
    just used for the unit test.
    '''

# Generated at 2022-06-13 04:34:31.943390
# Unit test for function split_args
def test_split_args():
    assert(split_args("a='b c'") == ["a='b c'"])
    assert(split_args("a='b c' d='e f'") == ["a='b c'", "d='e f'"])
    assert(split_args("a='b c' 'd e'") == ["a='b c'", "'d e'"])
    assert(split_args("a b='c d'") == ["a", "b='c d'"])
    assert(split_args("a='b c' d='e''f'") == ["a='b c'", "d='e''f'"])
    assert(split_args("a 'b c'") == ['a', "'b c'"])

# Generated at 2022-06-13 04:34:39.447218
# Unit test for function split_args
def test_split_args():
    # No quotes or jinja2 blocks
    assert split_args('simple text') == ['simple', 'text']
    # Quoted strings
    assert split_args('"simple string"') == ['simple string']
    assert split_args('"simple string" "another string"') == ['simple string', 'another string']
    assert split_args('"simple string" string "another string"') == ['simple string', 'string', 'another string']
    assert split_args('"simple string" string "another string" "yet another"') == ['simple string', 'string', 'another string', 'yet another']
    assert split_args('"simple string" string "another string" "yet another" "and another"') == ['simple string', 'string', 'another string', 'yet another', 'and another']

# Generated at 2022-06-13 04:34:48.752185
# Unit test for function split_args
def test_split_args():
    # Split args with no quoting and/or jinja2 blocks
    test_arg = "a=b c=d"
    expected = ['a=b', 'c=d']
    args = split_args(test_arg)
    assert args == expected

    # Split args with quotes (single and double), but no jinja2 blocks
    test_arg = 'a=b c="foo bar" d=\'baz buz\''
    expected = ['a=b', 'c="foo bar"', 'd=\'baz buz\'']
    args = split_args(test_arg)
    assert args == expected

    # Split args with jinja2 blocks but no quotes

# Generated at 2022-06-13 04:34:58.372162
# Unit test for function split_args
def test_split_args():
    # initialize counters and exit flag
    i = 0
    f = 0

    # initialize test data

# Generated at 2022-06-13 04:35:08.229695
# Unit test for function split_args
def test_split_args():
    # Tests simulating a real command
    args = '''
     action: some_action
     host: somehost.example.com
     path: /some/path
     something_else: "The quick brown fox jumped over the lazy dog"
    '''
    params = split_args(args)
    assert len(params) == 4
    assert params[0] == 'action: some_action'
    assert params[1] == 'host: somehost.example.com'
    assert params[2] == 'path: /some/path'
    assert params[3] == 'something_else: "The quick brown fox jumped over the lazy dog"'

    # Test with first line being empty string

# Generated at 2022-06-13 04:35:19.020028
# Unit test for function split_args

# Generated at 2022-06-13 04:35:26.641969
# Unit test for function split_args

# Generated at 2022-06-13 04:35:37.666364
# Unit test for function split_args
def test_split_args():
    assert(split_args("one two") == ['one', 'two'])
    assert(split_args("one two three four") == ['one', 'two', 'three', 'four'])
    assert(split_args("one='a b' two='c d'") == ['one=\'a b\'', 'two=\'c d\''])
    assert(split_args("one=\"a b\" two=\"c d\"") == ['one="a b"', 'two="c d"'])
    assert(split_args("one=\"a 'b'\" two=\"'c' d\"") == ['one="a \'b\'"', 'two="\'c\' d"'])

# Generated at 2022-06-13 04:35:47.165949
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo"d=abc"') == ['a=b', 'c="foo"d=abc"']
    assert split_args('a=b c="foo"d=abc') == ['a=b', 'c="foo"d=abc']
    assert split_args('a=b c="foo\\"bar"') == ['a=b', 'c="foo\\"bar"']
    assert split_args('a=b c="foo\nbar"') == ['a=b', 'c="foo\nbar"']
    assert split_args('a=b c=foo\nbar') == ['a=b', 'c=foo\nbar']
    assert split_args

# Generated at 2022-06-13 04:36:06.024955
# Unit test for function split_args

# Generated at 2022-06-13 04:36:16.620640
# Unit test for function split_args
def test_split_args():
    # normal cases
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b c="d e"') == ['a=b', 'c="d e"']

    # unterminated quoted string is rejected
    try:
        split_args('a=b c="d e')
    except Exception as e:
        assert 'unbalanced quotes' in str(e)

    # jinja2 blocks
    assert split_args('a=b c="d {{e}} f"') == ['a=b', 'c="d {{e}} f"']
    assert split_args('a=b c="d {{e}} {{f}}"') == ['a=b', 'c="d {{e}} {{f}}"']

# Generated at 2022-06-13 04:36:26.443784
# Unit test for function split_args
def test_split_args():
    # pylint: disable=no-self-use
    assert split_args('') == []
    assert split_args('a=1') == ['a=1']
    assert split_args('a=1 b=2') == ['a=1', 'b=2']
    assert split_args('a=1 b=2 c=3') == ['a=1', 'b=2', 'c=3']
    assert split_args('a=1 b=2\n c=3') == ['a=1', 'b=2', 'c=3']
    assert split_args('a=1\n b=2 c=3') == ['a=1', 'b=2', 'c=3']

# Generated at 2022-06-13 04:36:34.414138
# Unit test for function split_args

# Generated at 2022-06-13 04:36:45.352131
# Unit test for function split_args
def test_split_args():

    def _assert(test_data, expected):
        actual = split_args(test_data)
        assert actual == expected, "%s != %s, diff=%s" % (actual, expected, set(actual) ^ set(expected))

    _assert('a=b c="foo bar"', ['a=b ', 'c="foo bar"'])
    _assert('a=b c="foo bar" d= e="foo bar"', ['a=b ', 'c="foo bar" ', 'd= ', 'e="foo bar"'])
    _assert('a=b c="foo bar"\\\n'
            'd=\\\n'
            'e="foo bar"', ['a=b ', 'c="foo bar"\nd=\ne="foo bar"'])

# Generated at 2022-06-13 04:36:56.315538
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo bar "bar baz"') == ['foo', 'bar', '"bar baz"']
    assert split_args('foo bar "bar \'baz"') == ['foo', 'bar', '"bar \'baz"']
    assert split_args('foo bar "bar \\"baz"') == ['foo', 'bar', '"bar \\"baz"']
    assert split_args('foo bar "bar {{ baz )}') == ['foo', 'bar', '"bar {{ baz )}']
    assert split_args('foo bar "bar {{ baz }') == ['foo', 'bar', '"bar {{ baz }']

# Generated at 2022-06-13 04:37:03.269162
# Unit test for function split_args
def test_split_args():
    def assert_split(args, should_split):
        split = split_args(args)
        assert split == should_split, '%s => %s (should be %s)' % (args, split, should_split)

    assert_split('foo=bar', ['foo=bar'])
    assert_split('foo=bar baz', ['foo=bar', 'baz'])
    assert_split('foo=bar baz=quux', ['foo=bar', 'baz=quux'])
    assert_split('foo=bar baz\nquux', ['foo=bar', 'baz\nquux'])
    assert_split('foo=bar baz\\\nquux', ['foo=bar', 'baz\\\nquux'])

# Generated at 2022-06-13 04:37:15.208380
# Unit test for function split_args

# Generated at 2022-06-13 04:37:24.158916
# Unit test for function split_args

# Generated at 2022-06-13 04:37:35.308388
# Unit test for function split_args

# Generated at 2022-06-13 04:38:13.684693
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args('value with embedded "double quotes"') == ['value', 'with', 'embedded', '"double quotes"']
    assert split_args("a=b c=\'foo bar\'") == ['a=b', "c=\'foo bar\'"]
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo', 'bar']

# Generated at 2022-06-13 04:38:19.622322
# Unit test for function split_args
def test_split_args():
    # when not inside quotes, whitespace splits args
    assert split_args('a  b') == ['a', 'b']

    # newlines can be escaped
    assert split_args('a  b\c  d') == ['a', 'b\nc', 'd']

    # with quoted arguments, whitespace inside quotes is not a split char
    assert split_args('a "b c" d') == ['a', '"b c"', 'd']

    # whitespace is significant inside single quotes
    assert split_args("a 'b  c' d") == ['a', "'b  c'", 'd']

    # quotes can be escaped if inside quotes
    assert split_args('a "b \\"c d" e') == ['a', '"b \\"c d"', 'e']

    # inside jinja2 block braces,

# Generated at 2022-06-13 04:38:29.130188
# Unit test for function split_args
def test_split_args():
    test = "foo bar baz"
    result = split_args(test)
    assert result == ['foo', 'bar', 'baz']
    test = "foo='bar baz'"
    result = split_args(test)
    assert result == ["foo='bar baz'"]
    test = "foo='bar \\"
    test += "baz'"
    result = split_args(test)
    assert result == ["foo='bar baz'"]

    test = "foo='bar baz' bam=bat"
    result = split_args(test)
    assert result == ["foo='bar baz'", "bam=bat"]

    test = "foo=bar bam=bat \"foobar bam\""
    result = split_args(test)

# Generated at 2022-06-13 04:38:36.328964
# Unit test for function split_args
def test_split_args():
    '''
    Run all of the split_args unit tests to validate the logic of split_args
    '''

    import os
    import sys
    import datetime
    import glob
    import re
    import tokenize
    import token

    def read_file(filename):
        """
        Read a file into an array of tokens.

        The array contains the token type and token string.
        """
        toks = []
        with open(filename) as f:
            for toknum, tokval, _, _, _ in tokenize.generate_tokens(f.readline):
                toks.append((token.tok_name[toknum], tokval))
        return toks


# Generated at 2022-06-13 04:38:48.001514
# Unit test for function split_args
def test_split_args():
    re1 = ['a=b', 'c="foo bar"']
    re2 = ['a="foo \\"bar\\""']
    re3 = ['a="foo \\"bar\\"', 'b="baz"']
    re4 = ['a=b', 'c="foo bar"']
    re5 = ['a="foo \\"bar\\""']
    re6 = ['a="foo \\"bar\\"', 'b="baz"']
    re7 = ['"foo \\"bar\\""']
    re8 = ['a="baz', 'qux"']
    re9 = ["a=b"]
    re10 = ['a=b', 'c=d', 'e="single quote \\\'inside\\\'"']
    re11 = ['a=b']

# Generated at 2022-06-13 04:38:58.670600
# Unit test for function split_args

# Generated at 2022-06-13 04:39:05.551374
# Unit test for function split_args

# Generated at 2022-06-13 04:39:14.686167
# Unit test for function split_args
def test_split_args():
    # Test basic argument splitting
    args = split_args('foo bar "baz qux"')
    assert args == ['foo', 'bar', 'baz qux'], "Arguments were not split correctly"

    # Test splitting with line continuation
    args = split_args('foo \\\nbar "baz qux"')
    assert args == ['foo', 'bar', 'baz qux'], "Arguments were not split correctly with line continuation"

    # Test splitting with escaped double quote
    args = split_args('foo bar "baz\"qux"')
    assert args == ['foo', 'bar', 'baz"qux'], "Arguments were not split correctly with escaped double quote"

    # Test splitting with escaped single quote
    args = split_args('foo bar \'baz\\\'qux\'')

# Generated at 2022-06-13 04:39:25.476463
# Unit test for function split_args
def test_split_args():
    # Tests for valid split_args results
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"\ndef=g hi="j k"') == ['a=b', 'c="foo bar"\ndef=g', 'hi="j k"']
    assert split_args('{{inventory_hostname}} a=b') == ['{{inventory_hostname}}', 'a=b']
    assert split_args('a="b c" d="e f"') == ['a="b c"', 'd="e f"']
    assert split_args('a="b c" d="e f"') == ['a="b c"', 'd="e f"']

# Generated at 2022-06-13 04:39:33.607548
# Unit test for function split_args

# Generated at 2022-06-13 04:40:12.001556
# Unit test for function split_args

# Generated at 2022-06-13 04:40:22.028171
# Unit test for function split_args
def test_split_args():
    assert split_args('key1=val1 key2="val2 with spaces" key3="val3\\nwith\\nnewlines\\n"') == ['key1=val1', 'key2=val2 with spaces', 'key3="val3\nwith\nnewlines\n"']
    assert split_args('key1=val1 key2="val2 with spaces" key3="val3\nwith\nnewlines\n"') == ['key1=val1', 'key2=val2 with spaces', 'key3="val3\nwith\nnewlines\n"']

# Generated at 2022-06-13 04:40:31.138930
# Unit test for function split_args

# Generated at 2022-06-13 04:40:36.341930
# Unit test for function split_args
def test_split_args():
    '''
    make sure we always have the expected number of tokens,
    and that they match the expected values
    '''

    tokens = split_args("a=b c=d")
    assert len(tokens) == 2
    assert tokens[0] == 'a=b'
    assert tokens[1] == 'c=d'

    tokens = split_args("a=b 'c=d' #foo")
    assert len(tokens) == 2
    assert tokens[0] == 'a=b'
    assert tokens[1] == "'c=d'"

    tokens = split_args("a=b c=d #foo")
    assert len(tokens) == 2
    assert tokens[0] == 'a=b'
    assert tokens[1] == 'c=d'


# Generated at 2022-06-13 04:40:46.777234
# Unit test for function split_args
def test_split_args():
    assert split_args("foo bar baz") == [u"foo", u"bar", u"baz"]
    assert split_args("foo 'bar baz'") == [u"foo", u"'bar baz'"]
    assert split_args("foo \"bar baz\"") == [u"foo", u"\"bar baz\""]
    assert split_args("foo 'bar baz' woo hoo") == [u"foo", u"'bar baz'", u"woo", u"hoo"]
    assert split_args("foo \"bar baz\" woo hoo") == [u"foo", u"\"bar baz\"", u"woo", u"hoo"]