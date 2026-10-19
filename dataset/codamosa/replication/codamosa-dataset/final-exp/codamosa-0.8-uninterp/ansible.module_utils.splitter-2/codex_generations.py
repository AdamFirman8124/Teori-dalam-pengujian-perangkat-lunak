

# Generated at 2022-06-13 04:31:15.993434
# Unit test for function unquote
def test_unquote():
    # If a string is quoted at both ends, it is removed
    assert unquote('"test"') == 'test'
    assert unquote("'test'") == 'test'

    # If a string is not quoted at both ends, it is not removed
    assert unquote('"test') != 'test'
    assert unquote("'test") != 'test'
    assert unquote('test"') != 'test'
    assert unquote('test') == 'test'


# Generated at 2022-06-13 04:31:23.080780
# Unit test for function unquote
def test_unquote():
    assert unquote('"foo"') == 'foo'
    assert unquote('"foo') == '"foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('""') == ''
    assert unquote('""foo"') == '""foo"'
    assert unquote('"foo""') == '"foo"'



# Generated at 2022-06-13 04:31:32.813487
# Unit test for function split_args
def test_split_args():

    # Note that the test cases below are not exhaustive but have been added
    # mostly to document the changes that have been made compared to the
    # original implementation. The test cases should be expanded if the
    # function is further modified.

    # Tests for simple cases
    assert split_args('') == []
    assert split_args(' one') == ['one']
    assert split_args('one ') == ['one']
    assert split_args(' one ') == ['one']
    assert split_args('one two') == ['one', 'two']
    assert split_args('one \ntwo') == ['one', 'two']
    assert split_args('one \n two') == ['one', 'two']
    assert split_args('one two three') == ['one', 'two', 'three']
    assert split_args(' one two three ')

# Generated at 2022-06-13 04:31:42.989218
# Unit test for function split_args

# Generated at 2022-06-13 04:31:54.244732
# Unit test for function split_args
def test_split_args():

    print("test_split_args(): STARTING")

    usage = "fetch program=http url=http://somesite/somescript dest=/tmp/filename.txt"
    usage_splitted = split_args(usage)
    assert usage_splitted == ['program=http', 'url=http://somesite/somescript', 'dest=/tmp/filename.txt']

    usage = "fetch program=http url={{ http_url }} dest=/tmp/filename.txt"
    usage_splitted = split_args(usage)
    assert usage_splitted == ['program=http', 'url={{ http_url }}', 'dest=/tmp/filename.txt']

    usage = "fetch program=http url='{{ http_url }}' dest=/tmp/filename.txt"
    usage_splitted = split_args(usage)
   

# Generated at 2022-06-13 04:32:01.096716
# Unit test for function split_args
def test_split_args():
    data = 'key1=val1  key2="{{foo}} bar {{baz}}"  key3=\'{{fie}} bar {{fum}}\''
    result = split_args(data)
    assert result == ['key1=val1', 'key2="{{foo}} bar {{baz}}"', "key3='{{fie}} bar {{fum}}'"]



# Generated at 2022-06-13 04:32:07.523223
# Unit test for function split_args
def test_split_args():

    def assert_split_results(args, result):
        assert split_args(args) == result

    # no quotes, no jinja2, no newlines
    assert_split_results("foo=bar baz=foo", ["foo=bar", "baz=foo"])
    # a bunch of whitespace, but no quotes or jinja2 or newlines
    assert_split_results("  foo=bar   baz=foo     ", ["foo=bar", "baz=foo"])
    # newlines, no quotes, no jinja2
    assert_split_results("foo=bar\nbaz=foo", ["foo=bar\n", "baz=foo"])
    # quotes, no jinja2, no newlines

# Generated at 2022-06-13 04:32:13.069103
# Unit test for function unquote
def test_unquote():
    ''' unquote should remove first and last quote from a string '''
    assert unquote('"abc"') == 'abc'
    assert unquote("'abc'") == 'abc'
    assert unquote('abc') == 'abc'
    assert unquote('ab"c') == 'ab"c'
    assert unquote('"abc') == '"abc'

# Generated at 2022-06-13 04:32:21.389200
# Unit test for function split_args
def test_split_args():
    import sys
    if sys.version_info[0] < 3:
        # Python 2 unicode tests
        assert split_args(u"foo") == ["foo"]
        assert split_args(u'foo "bar baz"') == [u'foo', u'"bar baz"']
        assert split_args(u'foo "bar baz" \\') == [u'foo', u'"bar baz"']
        assert split_args(u'foo "bar baz" \\' + u'\n' + u'foo2') == [u'foo', u'"bar baz"\nfoo2']
        assert split_args(u'foo "bar baz" \\' + u'\n\n' + u'foo2') == [u'foo', u'"bar baz"\n\nfoo2']
        assert split

# Generated at 2022-06-13 04:32:31.297894
# Unit test for function unquote
def test_unquote():

    # Following string should remove the starting and ending quotes
    data = '"hello"'
    expected = 'hello'
    assert unquote(data) == expected, 'Expected "%s" and got "%s"' % (expected, unquote(data))

    # Following string should leave the starting and ending quotes
    data = r'"hello world"'
    expected = r'"hello world"'
    assert unquote(data) == expected, 'Expected "%s" and got "%s"' % (expected, unquote(data))

    # Following string should remove the starting and ending quotes
    data = '"hello'
    expected = '"hello'
    assert unquote(data) == expected, 'Expected "%s" and got "%s"' % (expected, unquote(data))

    # Following string should remove the starting and ending quotes
    data = r"'hello world'"


# Generated at 2022-06-13 04:32:52.331048
# Unit test for function split_args

# Generated at 2022-06-13 04:33:03.363098
# Unit test for function split_args
def test_split_args():
    '''unit test for function split_args'''
    # arg, expected result

# Generated at 2022-06-13 04:33:11.971009
# Unit test for function split_args
def test_split_args():
    print("\nRunning function split_args with following unit tests:")

    fp = open(__file__, 'rt')
    text = fp.read()
    fp.close()
    lines = text.split('\n')

    # Test 1

# Generated at 2022-06-13 04:33:24.484190
# Unit test for function split_args

# Generated at 2022-06-13 04:33:36.458843
# Unit test for function split_args
def test_split_args():
    # testing various combinations of nesting quotes and jinja2 blocks

    # test nested jinja2 {{ }} blocks
    args_list = ['{{ foo }}{{ foo }}', '"{{ foo }}" "{{ foo }}"', '{{ "foo" }} {{ "foo" }}', '"{{ \'foo\' }}" "{{ \'foo\' }}"', '{{ "{{ foo }}" }} {{ "{{ foo }}" }}', '"{{ \'{{ foo }}\' }}" "{{ \'{{ foo }}\' }}"']
    for args in args_list:
        params = split_args(args)
        assert len(params) == 1
        assert isinstance(params[0], str)
        assert params[0] == args
        assert len(params[0]) > 0

    # test nested jinja2 {{ }} blocks inside quotes

# Generated at 2022-06-13 04:33:48.633927
# Unit test for function split_args
def test_split_args():
    ''' split_args unittest'''
    # Basic test
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    # Nested quotes
    assert split_args('a="b c="foo bar""') == ['a="b c="foo bar""']
    # Backrefs
    assert split_args('a="b c=\"foo bar\""') == ['a="b c=\"foo bar\""']
    # Nested backrefs
    assert split_args('a="b c=\"foo \\\"bar\""') == ['a="b c=\"foo \\\"bar\""']
    # Nested backrefs
    assert split_args('a="b c=\"foo \\\"bar\""') == ['a="b c=\"foo \\\"bar\""']

# Generated at 2022-06-13 04:34:00.282513
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar" "a=b c=d"') == ['a=b', 'c="foo bar"', '"a=b c=d"']
    assert split_args('a=b c="foo bar" "a=b c=d"') == ['a=b', 'c="foo bar"', '"a=b c=d"']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]

# Generated at 2022-06-13 04:34:09.779676
# Unit test for function split_args

# Generated at 2022-06-13 04:34:15.524319
# Unit test for function split_args

# Generated at 2022-06-13 04:34:26.073777
# Unit test for function split_args
def test_split_args():
    '''
    Test split_args
    '''

# Generated at 2022-06-13 04:34:46.397151
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=1 'a=2'") == ['a=1', "'a=2'"]
    assert split_args("a=1 'a=2' 'a=\"foo bar\"' a='foo \n bar' a='foo \\\\n bar' a='foo \\\\n bar'") == ['a=1', "'a=2'", "'a=\"foo bar\"'", "a='foo \n bar'", "a='foo \\\\n bar'", "a='foo \\\\\n bar'"]

# Generated at 2022-06-13 04:34:54.726191
# Unit test for function split_args
def test_split_args():
    print("Testing split_args function")
    print("- Testing comments (failures are expected)")
    split_args('# Comment')
    split_args('# Comment\n')
    split_args('# Comment\n# Comment')
    split_args('# Comment {% foo %}\n')
    split_args('# Comment {% foo %}')
    split_args('# Comment {% foo %}\n# Comment {% foo %}')
    split_args('{# Comment #}\n')
    split_args('{# Comment #}\n{# Comment #}')
    print("- Testing quotes")
    assert split_args('"This is a long sentence"') == ['This is a long sentence']

# Generated at 2022-06-13 04:35:06.236203
# Unit test for function split_args
def test_split_args():
    # test simple args
    out = split_args('this is a string')
    assert out == ['this', 'is', 'a', 'string']

    # Test args with jinja2 block
    out = split_args('this string has {{foo}} jinja2 inside')
    assert out == ['this', 'string', 'has', '{{foo}}', 'jinja2', 'inside']

    # Test args with jinja2 block and quotes inside block
    out = split_args('this string has {{foo "bar baz"}} jinja2 inside')
    assert out == ['this', 'string', 'has', '{{foo "bar baz"}}', 'jinja2', 'inside']

    # Test args with jinja2 block and quotes outside block
    out = split_args('this string has "foo bar" inside')
   

# Generated at 2022-06-13 04:35:16.022575
# Unit test for function split_args

# Generated at 2022-06-13 04:35:21.181894
# Unit test for function split_args
def test_split_args():
    '''
    Test for function split_args
    '''

    # Basic test - simple args with no quoting or other oddities
    basic = 'a=b c="foo bar"'
    args = split_args(basic)
    assert len(args) == 2
    assert args[0] == 'a=b'
    assert args[1] == 'c="foo bar"'

    # Quotes inside quotes - testing double and single quotes
    quote1 = "a=b c='d e'"
    quote2 = 'a=b c="d e"'
    args1 = split_args(quote1)
    args2 = split_args(quote2)
    assert len(args1) == 2
    assert args1[0] == 'a=b'
    assert args1[1] == "c='d e'"

# Generated at 2022-06-13 04:35:27.850056
# Unit test for function split_args
def test_split_args():
    # All of these should pass
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a={{foo}} b="{% foo %}" c="foo" d=\'bar\' e=\\') == ['a={{foo}}', 'b="{% foo %}"', 'c="foo"', 'd=\'bar\'', 'e=\\']
    assert split_args('a="""{{ foo }} and {% if bar %} bar {% else %} not bar {% endif %}"""') == ['a="""{{ foo }} and {% if bar %} bar {% else %} not bar {% endif %}"""']
    assert split_args('a=\\') == ['a=\\']

# Generated at 2022-06-13 04:35:32.829256
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo 1"') == ['a=b', 'c="foo 1"']
    assert split_args('a=b c="foo 1') == ['a=b', 'c="foo 1']
    assert split_args('a=b c="foo 1\n') == ['a=b', 'c="foo 1']
    assert split_args('a=b c="foo 1"\n') == ['a=b', 'c="foo 1"']
    assert split_args('a=b c="foo 1\\\n') == ['a=b', 'c="foo 1\\']
    assert split_args('a=b c="foo 1\\\n d="bar 2"') == ['a=b', 'c="foo 1\\\n', 'd="bar 2"']

# Generated at 2022-06-13 04:35:41.956870
# Unit test for function split_args
def test_split_args():
    assert split_args("a=1") == ['a=1']
    assert split_args("a='1'") == ["a='1'"]
    assert split_args("a='1' b=2") == ['a=\'1\'', 'b=2']
    assert split_args("a='1' b=\"2\"") == ['a=\'1\'', 'b="2"']
    assert split_args("a='1' b=\"2\" c=3") == ['a=\'1\'', 'b="2"', 'c=3']
    assert split_args("a='1' b=\"2 3\" c=4") == ['a=\'1\'', 'b="2 3"', 'c=4']

# Generated at 2022-06-13 04:35:47.496347
# Unit test for function split_args
def test_split_args():
    assert split_args('"a=b" c="foo bar"') == ['"a=b"', 'c="foo bar"']
    assert split_args('"a=b c="foo bar"') == ['"a=b c="foo bar"']
    assert split_args('"a=b" c=\'foo bar\'') == ['"a=b"', "c='foo bar'"]
    assert split_args('"a=b" c="foo bar" d="foo \'bar\'" e=bar') == ['"a=b"', 'c="foo bar"', 'd="foo \'bar\'"', 'e=bar']
    assert split_args('"foo bar"') == ['"foo bar"']
    assert split_args('"foo bar') == ['"foo bar']

# Generated at 2022-06-13 04:35:53.554453
# Unit test for function split_args
def test_split_args():
    assert split_args(b'a=b c="foo bar"') == [b'a=b', b'c="foo bar"']
    assert split_args(b'a=b c="a=b"') == [b'a=b', b'c="a=b"']
    assert split_args(b'a=b c="foo bar" d="a=b"') == [b'a=b', b'c="foo bar"', b'd="a=b"']

# Generated at 2022-06-13 04:36:33.709537
# Unit test for function split_args
def test_split_args():
    # simple args with no quotes
    assert split_args("a=b c='foo bar'") == ["a=b", "c='foo bar'"]
    # simple args with quotes
    assert split_args("a=\"b c\"") == ["a=\"b c\""]
    # simple args with double quotes
    assert split_args('a="b c"') == ['a="b c"']
    # args with a backslash, quotes, and spaces
    assert split_args("a=\"b \\\"c\"") == ["a=\"b \\\"c\""]
    # args with quotes and spaces, and a line continuation backslash
    assert split_args("a=\"b c\\\nd\"") == ["a=\"b c\\\nd\""]
    # args with quotes, spaces, and a line continuation backslash
    assert split_args

# Generated at 2022-06-13 04:36:44.384926
# Unit test for function split_args

# Generated at 2022-06-13 04:36:55.890925
# Unit test for function split_args
def test_split_args():

    # make sure non-strings become strings
    assert split_args(3) == ['3']
    assert split_args(dict(foo='bar')) == ['{"foo": "bar"}']
    assert split_args(dict(foo=dict(bar='baz'))) == ['{"foo": {"bar": "baz"}}']

    # make sure regular strings work
    def assert_tokens(args, tokens, msg=None):
        msg = msg or "assert_tokens failed: %s != %s" % (args, tokens)
        assert split_args(args) == tokens, msg

    assert_tokens('', [])
    assert_tokens('foo bar', ['foo', 'bar'])
    assert_tokens('foo   bar', ['foo', 'bar'])

# Generated at 2022-06-13 04:37:03.244395
# Unit test for function split_args

# Generated at 2022-06-13 04:37:15.208455
# Unit test for function split_args
def test_split_args():
    # Test 1: Unquoted string
    res = split_args("a=b c=d")
    assert res == ['a=b', 'c=d']

    # Test 2: Quoted string
    res = split_args("a='b c' d='e f'")
    assert res == ["a='b c'", "d='e f'"]

    # Test 3: Multiple line input
    res = split_args("a='b c'\nd='e f'")
    assert res == ["a='b c'\n", "d='e f'"]

    # Test 4: Multiple line input. Last line continuation
    res = split_args("a='b c'\nd='e f'\\")
    assert res == ["a='b c'\n", "d='e f'"]

    # Test 5: Line continuation

# Generated at 2022-06-13 04:37:24.133869
# Unit test for function split_args
def test_split_args():
    '''Test function split_args'''

    assert split_args('') == ['']
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a= b=') == ['a=', 'b=']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=1 c={{ foo }}') == ['a=1', 'c={{ foo }}']
    assert split_args('a=1 c={{ foo }} d="hello {{ foo }}"') == ['a=1', 'c={{ foo }}', 'd="hello {{ foo }}"']

# Generated at 2022-06-13 04:37:35.268695
# Unit test for function split_args

# Generated at 2022-06-13 04:37:44.948590
# Unit test for function split_args

# Generated at 2022-06-13 04:37:53.878439
# Unit test for function split_args
def test_split_args():
    ''' test for splitting arguments in the same way we expect module parameters to be passed in '''

    d = {}

    d['a b'] = ['a', 'b']
    d['a=b'] = ['a=b']
    d['a="b c"'] = ['a="b c"']
    d['a="b c" d="e f"'] = ['a="b c"', 'd="e f"']
    d['a=b c="foo bar"'] = ['a=b', 'c="foo bar"']
    d['a="b c" d=e f=g'] = ['a="b c"', 'd=e', 'f=g']

# Generated at 2022-06-13 04:38:01.443391
# Unit test for function split_args
def test_split_args():

    def _assert(args, expected):
        params = split_args(args)
        assert params == expected, "problem with input %s, expected %s, got %s" % (args, expected, params)

    _assert('foo=bar baz="single quoted"', ['foo=bar', 'baz="single quoted"'])

    _assert('foo="spam eggs"', ['foo="spam eggs"'])

    _assert('foo="spam eggs" bar="{{ foobar }}"', ['foo="spam eggs"', 'bar="{{ foobar }}"'])

    _assert('bar={{ foobar }}', ['bar={{ foobar }}'])

    _assert('bar {{ foobar }}\nfoo=baz', ['bar {{ foobar }}\nfoo=baz'])


# Generated at 2022-06-13 04:39:10.008807
# Unit test for function split_args
def test_split_args():
    '''
    tests for the split_args function
    '''

    # if this was called directly, run the tests
    from units.compat.mock import patch, MagicMock
    from collections import namedtuple

    # this is needed so that the args being parsed don't try to resolve
    # as a jinja2 template
    mock_module = MagicMock()
    mock_module.params = namedtuple('FakeModuleParams', 'no_log')
    mock_module.params.no_log = False

    # this is needed to make sure the args parser doesn't try to do a lookup
    # for the hostvars dictionary
    mock_variable_manager = MagicMock()
    mock_variable_manager.get_vars = MagicMock()

    # patch the get_module function so we can mock out the module and variable

# Generated at 2022-06-13 04:39:19.889342
# Unit test for function split_args
def test_split_args():
    def test_split(input):
        result = split_args(input)
        print("input: %s\noutput: %s\n" % (input, result))
        return result

    test_split('mike')
    test_split('mike   daniel toby')
    test_split(' mike   daniel toby ')
    test_split(' mike daniel toby ')
    test_split(' mike daniel toby')
    test_split('"mike daniel toby"')
    test_split("'mike daniel toby'")
    test_split("mike\n daniel  toby")
    test_split("mike\n daniel  toby\n")
    test_split("mike\ndaniel\ntoby")

# Generated at 2022-06-13 04:39:30.021525
# Unit test for function split_args
def test_split_args():
    def test(args, expect_args, expect_kwargs):
        result_args, result_kwargs = parse_kv(args)
        if result_args != expect_args or result_kwargs != expect_kwargs:
            print("%r" % args)
            print("expect_args=%r result_args=%r" % (expect_args, result_args))
            print("expect_kwargs=%r result_kwargs=%r" % (expect_kwargs, result_kwargs))
            assert False
    test("", [], {})
    test("a=b", [], {'a': 'b'})
    test("a='b b'", [], {'a': 'b b'})

# Generated at 2022-06-13 04:39:36.437919
# Unit test for function split_args

# Generated at 2022-06-13 04:39:43.777421
# Unit test for function split_args
def test_split_args():
    '''
    Tests for function split_args. This function is used to
    split arguments for ansible modules into a list, being careful
    of quoting and escaping rules. This function is also used in
    the CLI code for parsing argument lines.
    '''


# Generated at 2022-06-13 04:39:53.867892
# Unit test for function split_args
def test_split_args():
    test_data = '''a=b c="foo bar"
          d={{ e
          f=g
          }}
          h=i
          j=k
          foo="
          bar"
          baz='
          bam'
          bang="b\"o\"om"
          boom='b\'o\'om'
          l="
          m=n o=p
          q=r
          s=t
          "
          u={{v}}'''

# Generated at 2022-06-13 04:40:02.537533
# Unit test for function split_args
def test_split_args():
    assert split_args("a=1 b=2") == ["a=1", "b=2"]
    assert split_args("a=1 b=2\n") == ["a=1", "b=2\n"]
    assert split_args("a={{ foo }}") == ["a={{ foo }}"]
    assert split_args("a={{ foo }} b={{ bar }}") == ["a={{ foo }}", "b={{ bar }}"]
    assert split_args("a={{ foo }}\nb={{ bar }}") == ["a={{ foo }}\n", "b={{ bar }}"]
    assert split_args(r"""a={{ "foo" }}""") == [r"""a={{ "foo" }}"""]
    assert split_args(r"""a={{ "foo" }} b={{ "bar" }}""")

# Generated at 2022-06-13 04:40:12.709506
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="{{ foo }}"') == ['a=b', 'c="{{ foo }}"']
    assert split_args('a=b c="{{ foo }} bar"') == ['a=b', 'c="{{ foo }} bar"']
    assert split_args('a=b c="bar {{ foo }}"') == ['a=b', 'c="bar {{ foo }}"']
    assert split_args('a=b c={% foo %}') == ['a=b', 'c={% foo %}']
    assert split_args('a=b c={% foo bar %}') == ['a=b', 'c={% foo bar %}']

# Generated at 2022-06-13 04:40:23.336933
# Unit test for function split_args
def test_split_args():
    assert split_args("''") == ["''"]
    assert split_args("a='b c'") == ["a='b c'"]
    assert split_args("a='b c' 'd e' f") == ["a='b c'", "'d e'", "f"]
    assert split_args("a='b c' \"d e\" f") == ["a='b c'", '"d e"', "f"]
    assert split_args("a=\"{{foo}} d\" e") == ['a="{{foo}} d"', "e"]
    assert split_args("a=b 'c d' e={{foo}}") == ["a=b", "'c d'", "e={{foo}}"]

# Generated at 2022-06-13 04:40:31.633968
# Unit test for function split_args