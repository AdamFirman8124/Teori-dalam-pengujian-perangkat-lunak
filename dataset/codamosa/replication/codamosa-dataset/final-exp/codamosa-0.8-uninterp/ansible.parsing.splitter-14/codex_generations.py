

# Generated at 2022-06-13 07:07:39.402743
# Unit test for function split_args
def test_split_args():
    assert split_args("-V -f") == ["-V", "-f"]
    assert split_args("-V") == ["-V"]
    assert split_args("-f") == ["-f"]
    assert split_args("") == []
    assert split_args("foo bar") == ["foo", "bar"]
    assert split_args("foo bar baz") == ["foo", "bar", "baz"]
    assert split_args("-C /foo/bar -l someuser") == ["-C", "/foo/bar", "-l", "someuser"]
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    assert split_args("a=b c=d e=f") == ["a=b", "c=d", "e=f"]

# Generated at 2022-06-13 07:07:47.539288
# Unit test for function parse_kv
def test_parse_kv():
    args = "creates=/tmp/foo removes=/tmp/bar chdir=/tmp/baz executable=/bin/bash warn=yes stdin=hello stdin_add_newline=yes strip_empty_ends=yes"
    result = parse_kv(args)
    assert result['creates'] == '/tmp/foo'
    assert result['removes'] == '/tmp/bar'
    assert result['chdir'] == '/tmp/baz'
    assert result['executable'] == '/bin/bash'
    assert result['warn'] == 'yes'
    assert result['stdin'] == 'hello'
    assert result['stdin_add_newline'] == 'yes'
    assert result['strip_empty_ends'] == 'yes'

# Generated at 2022-06-13 07:07:56.573950
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for function parse_kv
    '''

    # standard test
    test_string = 'k1=v1 k2=v2'
    ret = parse_kv(test_string)
    assert ret == {"k1": "v1", "k2": "v2"}

    # test with raw params
    test_string = 'k1=v1 k2=v2 k3'
    ret = parse_kv(test_string, check_raw=True)
    assert ret == {"k1": "v1", "k2": "v2", "_raw_params": "k3"}

    # test with escaped quotes
    test_string = r"k1=\"v1\" k2=\'v2\'"
    ret = parse_kv(test_string)

# Generated at 2022-06-13 07:08:03.778183
# Unit test for function parse_kv
def test_parse_kv():
    orig_args = "file=/tmp/file1 state=present mode=600 other_params foo=bar"
    args = parse_kv(orig_args)
    assert(args == { u'file': u'/tmp/file1', u'mode': u'600', u'state': u'present', u'_raw_params': u'other_params foo=bar' })
    orig_args = "file=/tmp/file1 state=present mode=600"
    args = parse_kv(orig_args)
    assert(args == { u'file': u'/tmp/file1', u'mode': u'600', u'state': u'present' })
    orig_args = "file=/tmp/file1 state=present"
    args = parse_kv(orig_args)

# Generated at 2022-06-13 07:08:12.198355
# Unit test for function split_args
def test_split_args():
    def assert_equal(in_args, expected):
        with open('/tmp/t.yml', 'w') as f:
            f.write(in_args)
        parsed = False
        with open('/tmp/t.yml') as f:
            for line in f.readlines():
                out_args = split_args(line.strip())
                if expected and out_args == expected:
                    parsed = True
                    break
                else:
                    raise Exception("failed to parse '{0}' with result '{1}'".format(line.strip(), out_args))
        if not parsed:
            raise Exception("failed to parse '{0}' with result '{1}'".format(in_args, out_args))


# Generated at 2022-06-13 07:08:16.796634
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a=b c=\"foo bar\"") == [u'a=b', u'c="foo bar"']
    assert split_args(u"a=b c=\"foo bar") == [u'a=b', u'c="foo bar']
    assert split_args(u"a=b c='foo bar") == [u'a=b', u"c='foo bar"]
    assert split_args(u"foo='bar\"") == [u"foo='bar\""]
    assert split_args(u"foo=\"bar'") == [u'foo="bar\'']
    assert split_args(u"foo='bar\\'") == [u"foo='bar\\'"]

# Generated at 2022-06-13 07:08:26.804018
# Unit test for function parse_kv
def test_parse_kv():
    from mock import Mock, patch
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 07:08:37.883525
# Unit test for function parse_kv

# Generated at 2022-06-13 07:08:48.409169
# Unit test for function split_args
def test_split_args():
    assert split_args('a=1 b="2" c=3') == ['a=1', 'b="2"', 'c=3']
    assert split_args('a="{{foo}}" b="{{bar}}" c=3') == ['a="{{foo}}"', 'b="{{bar}}"', 'c=3']
    assert split_args('''a="{{foo}}" b="{{bar}}" c=3''') == ['''a="{{foo}}"''', '''b="{{bar}}"''', '''c=3''']
    assert split_args('''a="{{foo}}"\nb="{{bar}}" c=3''') == ['''a="{{foo}}"\n''', '''b="{{bar}}"''', '''c=3''']

# Generated at 2022-06-13 07:09:00.113795
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=b c=d") == {'a': 'b', 'c': 'd'}
    assert parse_kv("a='b' c=\"d\"") == {'a': 'b', 'c': 'd'}
    assert parse_kv("a='b c' c=\"d e\"") == {'a': 'b c', 'c': 'd e'}
    assert parse_kv("a='b=c' c=\"d=e\"") == {'a': 'b=c', 'c': 'd=e'}
    assert parse_kv("a=\"b=c\" c='d=e'") == {'a': 'b=c', 'c': 'd=e'}

# Generated at 2022-06-13 07:09:23.257964
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'foo') == {u'foo': None}
    assert parse_kv(u'foo="bar \"baz\""') == {u'foo': u'"bar \\"baz\\""'}
    assert parse_kv(u'foo="bar \"baz\"" spam') == {u'foo': u'"bar \\"baz\\""', u'spam': None}
    assert parse_kv(u'foo=bar spam') == {u'foo': u'bar', u'spam': None}
    assert parse_kv(u'foo="bar" baz=eggs') == {u'foo': u'"bar"', u'baz': u'eggs'}

# Generated at 2022-06-13 07:09:36.729899
# Unit test for function split_args
def test_split_args():
    args = '''x={{ y }} z={{ a.b.c }} d={{ (1 + foo) }} a={{ b | c }} e={{ "foo" }} f={{ 'foo' }} g={{ 3 if foo else 4 }} h={{ [1,2,3] }} i={{ {'k': 'v'} }} j={{ {1: 2, 2: 3} }} k=1 l={{ foo if bar else "a b" }} m={{ foo if bar else 'a b' }} n={{ foo if bar else ''' ''' + "a b" }} o={{ foo if bar else ''' ''' + 'a b' }}'''

# Generated at 2022-06-13 07:09:48.698682
# Unit test for function parse_kv

# Generated at 2022-06-13 07:09:58.147851
# Unit test for function split_args

# Generated at 2022-06-13 07:10:03.421831
# Unit test for function split_args
def test_split_args():
    test_input = 'echo "this is a test" {{ foo }} {% bar %} {# baz #}'

    expected_result = ['echo', '"this is a test"', '{{', 'foo', '}}', '{%', 'bar', '%}', '{#', 'baz', '#}']

    actual_result = split_args(test_input)

    assert expected_result == actual_result



# Generated at 2022-06-13 07:10:10.812313
# Unit test for function parse_kv
def test_parse_kv():
    data = u"""creates=/tmp/foo removes=/tmp/bar warn=no executable=/some/path creates=/another/path"""
    opts = parse_kv(data, check_raw=True)
    assert opts[u'warn'] == u'no'
    assert opts[u'executable'] == u'/some/path'
    assert opts[u'creates'] == u'/tmp/foo'
    assert opts[u'removes'] == u'/tmp/bar'
    assert opts[u'_raw_params'] == u"creates=/another/path"

    data = u"""some space separated parameters"""
    opts = parse_kv(data, check_raw=True)
    assert opts == {}

    data = u""""this=is a test" x=y "another=test"""
   

# Generated at 2022-06-13 07:10:22.299927
# Unit test for function split_args

# Generated at 2022-06-13 07:10:33.457534
# Unit test for function split_args
def test_split_args():
    '''
    Unit tests for function split_args, who handles the arguments
    passed to the different modules. This function is working
    together with the function join_args, who is called from the
    remote module.
    '''
    # Test 0: Simple test
    args = 'arg1="foo bar"'
    assert split_args(args) == ['arg1="foo bar"']

    # Test 1: Test with newline inside double quotes
    args = 'arg1="foo\nbar"'
    assert split_args(args) == ['arg1="foo\nbar"']

    # Test 2: Test with space inside double quotes
    args = 'arg1="foo bar"'
    assert split_args(args) == ['arg1="foo bar"']

    # Test 3 - Test with space inside double quotes with space before opening double quotes

# Generated at 2022-06-13 07:10:41.909926
# Unit test for function split_args
def test_split_args():


    # Basic example
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # single quoted expressions aren't parsed, and are kept as one string
    assert split_args('a=\'"$b"\'') == ['a=\'"$b"\'']

    # Unquoted expressions are kept as one string
    assert split_args('a=$b') == ['a=$b']

    # multiple jinja2 {{ }} and {% %} blocks can be nested

# Generated at 2022-06-13 07:10:53.060545
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u'a=1 "b=2 c=3" d=4') == {u'a': u'1', u'b': u'2 c=3', u'd': u'4'}
    assert parse_kv(u'a="1 2" b=4') == {u'a': u'1 2', u'b': u'4'}
    assert parse_kv(u'a="1=2" b=4') == {u'a': u'1=2', u'b': u'4'}

# Generated at 2022-06-13 07:11:04.011008
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar", True) == dict(foo=u'bar')
    assert parse_kv("foo=\"bar\"", True) == dict(foo=u'bar')
    assert parse_kv("foo=bar_and_baz", True) == dict(foo=u'bar_and_baz')
    assert parse_kv("foo=bar\\ bar", True) == dict(foo=u'bar bar')
    assert parse_kv("foo=bar\\=baz", True) == dict(foo=u'bar=baz')
    assert parse_kv("foo=bar\\nbar", True) == dict(foo=u'bar\nbar')
    assert parse_kv("foo=\"bar\\\"bar\"", True) == dict(foo=u'bar"bar')
    assert parse_k

# Generated at 2022-06-13 07:11:10.775579
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    # Quotes should be stripped and the value is unquoted
    assert parse_kv(r"a='b' c=d") == {'a': 'b', 'c': 'd'}
    assert parse_kv(r"a='b c'") == {'a': 'b c'}
    assert parse_kv(r"""a='b\' c'""") == {'a': "b' c"}
    assert parse_kv(r'a="b\' c"') == {'a': "b' c"}
    # Just check that this does not throw an exception
    parse_kv(r'a="b\" c"')


# Generated at 2022-06-13 07:11:18.082280
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c=d e=f') == {u'a': u'b', u'e': u'f', u'c': u'd'}
    assert parse_kv('a=b c=d e=f', check_raw=True) == {u'a': u'b', u'e': u'f', u'c': u'd'}
    assert parse_kv('a=b c=d e=f g h') == {u'a': u'b', u'e': u'f', u'c': u'd'}

# Generated at 2022-06-13 07:11:28.468554
# Unit test for function split_args

# Generated at 2022-06-13 07:11:41.615072
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b=2 c=3') == dict(a='1', b='2', c='3')
    assert parse_kv('a=1 b="2 c=3"') == dict(a='1', b='2 c=3')
    assert parse_kv('a=1 b=\'2 c=3\'') == dict(a='1', b='2 c=3')
    assert parse_kv('creates=/tmp/this does not go in here') == dict(creates='/tmp/this', _raw_params='does not go in here')
    assert parse_kv('a=1 b=zsh c="echo hello world"', check_raw=True) == dict(a='1', b='zsh', _raw_params='c="echo hello world"')
    assert parse_

# Generated at 2022-06-13 07:11:50.998250
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a="b c=d"') == {'a': 'b c=d'}
    assert parse_kv('a=b" c=d"') == {'a': 'b c=d'}
    assert parse_kv('a=b c="d e"') == {'a': 'b', 'c': 'd e'}
    assert parse_kv('a=b c=d e') == {'a': 'b', 'c': 'd', '_raw_params': 'e'}

# Generated at 2022-06-13 07:12:02.318825
# Unit test for function parse_kv
def test_parse_kv():
    def _check(input_, expected_output):
        actual_output = parse_kv(input_)
        assert actual_output == expected_output, "actual_output is %s" % actual_output

    # Test handling of lists
    _check(
        'creates=/foo/bar removes=/foo/baz',
        {
            u'creates': '/foo/bar',
            u'removes': '/foo/baz',
        },
    )

    # Test handling of raw params
    _check(
        'some_command --some-option "some_value"',
        {
            u'_raw_params': 'some_command --some-option "some_value"',
        },
    )

    # Test handling of lists with raw params

# Generated at 2022-06-13 07:12:09.519683
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=b c='d d' e='f=g' h='i j'") == parse_kv("a=b c='d d' e='f=g' h='i j'", check_raw=True) == {"a": "b", "c": "d d", "e": "f=g", "h": "i j", "_raw_params": "a=b c='d d' e='f=g' h='i j'"}
    assert parse_kv("a=b c='d d' e='f=g' h='i j'", check_raw=False) == {"a": "b", "c": "d d", "e": "f=g", "h": "i j"}

# Generated at 2022-06-13 07:12:16.520961
# Unit test for function parse_kv
def test_parse_kv():
    text = 'k1=v1 k2==v2 k3="v3" k4="v 4" "k5=v 5"'

    options = parse_kv(text)

    assert options == {'k1':u'v1', 'k2':u'=v2', 'k3':u'v3', 'k4':u'v 4', '_raw_params':u'"k5=v 5"'}

# similar to shlex.split, but preserves empty args and does not break on quoted whitespace

# Generated at 2022-06-13 07:12:30.492005
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a=b c=d e=f') == {u'a': u'b', u'c': u'd', u'e': u'f'}
    assert parse_kv('a="b c" d="e f"') == {u'a': u'b c', u'd': u'e f'}
    assert parse_kv('a="b c')['_raw_params'] == 'a="b c'
    assert parse_kv('a="b c" d="e f')['_raw_params'] == 'a="b c" d="e f'

# Generated at 2022-06-13 07:12:48.943220
# Unit test for function parse_kv
def test_parse_kv():
    test_args = [
        "firstarg=firstval secondarg=secondval",
    ]
    for test_arg in test_args:
        test_arg = to_text(test_arg)
        print("{0}".format(test_arg))
        parsed_arg = parse_kv(test_arg)
        print("{0}".format(parsed_arg))
        print("{0}".format(type(parsed_arg)))
        # makesure we have a dictionary
        assert isinstance(parsed_arg, dict)
        # make sure we have the correct values for each key
        assert parsed_arg['firstarg'] == u'firstval'
        assert parsed_arg['secondarg'] == u'secondval'

# Generated at 2022-06-13 07:12:58.746714
# Unit test for function split_args
def test_split_args():
    #test basic functionality
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'])
    assert(split_args('a=b \'quoted and space\' c="foo bar"') == ['a=b', '\'quoted and space\'', 'c="foo bar"'])
    assert(split_args('a=b "quoted and space" c="foo bar"') == ['a=b', '"quoted and space"', 'c="foo bar"'])
    assert(split_args('a=b "quoted and space" c="foo bar"') == ['a=b', '"quoted and space"', 'c="foo bar"'])

# Generated at 2022-06-13 07:13:06.287346
# Unit test for function parse_kv
def test_parse_kv():
    args = "foo=bar zaz=meow"
    expected_args = {u"foo":"bar", u"zaz":"meow", u"_raw_params": "foo=bar zaz=meow"}
    res_args = parse_kv(args)
    assert res_args == expected_args

    args = "\"foo bar\"=baz"
    expected_args = {u"foo bar":"baz", u"_raw_params": "\"foo bar\"=baz"}
    res_args = parse_kv(args)
    assert res_args == expected_args

    args = "foo=bar zaz=meow \"foo bar\"=baz"

# Generated at 2022-06-13 07:13:17.859270
# Unit test for function parse_kv
def test_parse_kv():
    # Test simple case
    args = "arg1=some value with spaces=foo"
    parsed = parse_kv(args)
    assert 'arg1' in parsed
    assert parsed['arg1'] == 'some value with spaces=foo'

    # Test args with flags only
    args = "arg1 arg2=3 arg3"
    parsed = parse_kv(args)
    assert len(parsed) == 1
    assert '_raw_params' in parsed
    assert parsed['_raw_params'] == args

    # Test args with escaped quotes
    args = r'"arg1=\"arg1value\"" arg2=\'arg2value\''
    parsed = parse_kv(args)
    assert len(parsed) == 2
    assert 'arg1' in parsed

# Generated at 2022-06-13 07:13:25.668593
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:35.522661
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:39.570615
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("hello") == {'_raw_params': u'hello'}
    assert parse_kv("hello world") == {'_raw_params': u'hello world'}
    assert parse_kv("hello key=value world") == {'_raw_params': u'hello', 'key': u'value world'}


'''
Splits args on spaces, but allows for quotes, double quotes, and escaping
of spaces and quotes with backslash
'''


# Generated at 2022-06-13 07:13:49.525606
# Unit test for function parse_kv
def test_parse_kv():
    # Test with no args
    assert parse_kv(None) == {}
    # Test with no key/value args
    assert parse_kv("dominion") == {}
    # Test parsing one key/value pair
    assert parse_kv("a=b") == {'a': 'b'}
    # Test parsing multiple key/value pairs
    assert parse_kv("a=b c='d e'") == {'a': 'b', 'c': 'd e'}
    # Test parsing escaped equal signs
    assert parse_kv("a\\=b c\\=d") == {'a=b': 'c=d'}
    # Test parsing escaped equal signs mixed with normal values
    assert parse_kv("a\\=b=c\\=d") == {'a=b': 'c=d'}
    #

# Generated at 2022-06-13 07:14:03.994649
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('arg1=foo arg2=bar') == {u'arg1': u'foo', u'arg2': u'bar'}
    assert parse_kv('arg1=baz arg2=bar arg3 arg4') == {u'arg1': u'baz', u'arg2': u'bar', u'_raw_params': u'arg3 arg4'}
    assert parse_kv('arg=asdf\\=foo') == {u'arg': u'asdf=foo'}
    assert parse_kv('novalue expect_failure="foo') == {u'_raw_params': u'novalue expect_failure="foo'}
    assert parse_kv('arg="foo bar"') == {u'arg': u'foo bar'}

# Generated at 2022-06-13 07:14:11.660936
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:28.813176
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Test function parse_kv
    '''

    # empty string
    args = ''
    # with check_raw = True
    options = parse_kv(args, check_raw=True)
    assert options == {}, "Empty string does not return {} (check_raw=True)"
    # with check_raw = False
    options = parse_kv(args, check_raw=False)
    assert options == {}, "Empty string does not return {} (check_raw=False)"

    # single string
    args = 'a=b'
    # with check_raw = True
    options = parse_kv(args, check_raw=True)
    assert options == {'a': 'b'}, "Single string does not return {'a': 'b'} (check_raw=True)"
    # with check_

# Generated at 2022-06-13 07:14:39.029199
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("") == {}
    assert parse_kv(None) == {}
    assert parse_kv("a=b") == {'a': 'b'}
    assert parse_kv("a=b c=d") == {'a': 'b', 'c': 'd'}
    assert parse_kv("a=b c=d e=f") == {'a': 'b', 'c': 'd', 'e': 'f'}
    assert parse_kv('a=b c="d e" f="g h"') == {'a': 'b', 'c': 'd e', 'f': 'g h'}

    assert parse_kv("a=\"b')\" c=d") == {'a': "b')", 'c': 'd'}

    # FIXME: add tests for

# Generated at 2022-06-13 07:14:46.493738
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo="bar nose"') == {u'foo': u'"bar nose"'}
    assert parse_kv('foo=bar nose') == {u'foo': u'bar', u'_raw_params': u'nose'}
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('foo=bar bar=foo') == {u'foo': u'bar', u'bar': u'foo'}
    assert parse_kv('foo="bar bar"') == {u'foo': u'"bar bar"'}
    assert parse_kv('foo="bar bar bar"') == {u'foo': u'"bar bar bar"'}

# Generated at 2022-06-13 07:14:55.996517
# Unit test for function split_args
def test_split_args():

    # AssertionError: ['a=b', 'c="foo bar"'] != ['a=b', 'c="foo', 'bar"']
    #assert ['a=b', 'c="foo bar"'] == split_args('a=b c="foo bar"')

    assert ['a=b', 'c="foo bar"'] == split_args('a=b\nc="foo bar"')
    assert ['a=b', 'c="foo bar"'] == split_args('a=b \nc="foo bar"')
    assert ['a=b', 'c="foo bar"'] == split_args('a=b\n c="foo bar"')
    assert ['a=b', 'c="foo bar"'] == split_args('a=b \n c="foo bar"')

# Generated at 2022-06-13 07:14:58.515330
# Unit test for function parse_kv
def test_parse_kv():
    s = "Hello var=World"
    d = parse_kv(s)
    assert len(d) == 1
    assert 'var' in d
    assert d['var'] == 'World'



# Generated at 2022-06-13 07:15:12.597036
# Unit test for function split_args
def test_split_args():
    """
    Unit test for function split_args()
    """
    # Split args with simple string
    assert split_args("foo bar") == ["foo", "bar"]

    # Split args with newlines
    assert split_args("foo\nbar baz\nfoo bar") == ["foo\nbar", "baz\nfoo", "bar"]

    # Split args with newlines and spaces
    assert split_args("foo  bar\nbaz\tfoo\nbar") == ["foo", "bar\nbaz\tfoo\nbar"]

    # Split args with quoted string
    assert split_args("foo bar baz='foo bar'") == ["foo", "bar", "baz='foo bar'"]

    # Split args with quoted strings

# Generated at 2022-06-13 07:15:19.023613
# Unit test for function parse_kv
def test_parse_kv():
    result = parse_kv('fizz=buzz bazz=foo')
    assert result == {'fizz': 'buzz', 'bazz': 'foo'}

    result = parse_kv('fizz=buzz bazz=foo bar')
    assert result == {'fizz': 'buzz', 'bazz': 'foo', '_raw_params': 'bar'}

    result = parse_kv('fizz=buzz bazz="foo bar" bar=foo')
    assert result == {'fizz': 'buzz', 'bazz': 'foo bar', 'bar': 'foo', '_raw_params': 'bar=foo'}

    result = parse_kv('fizz=buzz bazz="foo bar')

# Generated at 2022-06-13 07:15:28.754723
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz=quux') == {'foo': 'bar', 'baz': 'quux'}
    assert parse_kv('foo="bar baz"') == {'foo': 'bar baz'}
    assert parse_kv('foo="bar\"baz"') == {'foo': 'bar"baz'}
    assert parse_kv('foo="bar \'baz\'"') == {'foo': 'bar \'baz\''}
    assert parse_kv('foo=bar "baz quux" fred=bob') == {'foo': 'bar', '_raw_params': '"baz quux"', 'fred': 'bob'}

# Generated at 2022-06-13 07:15:39.034642
# Unit test for function split_args
def test_split_args():
    import nose
    import nose.tools
    from ansible.compat.tests.mock import patch, Mock
    import ansible.compat.tests.module_utils.basic

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()


# Generated at 2022-06-13 07:15:48.542286
# Unit test for function parse_kv
def test_parse_kv():
    ''' 
    Unit test for function parse_kv
    '''

    print("\n---\nStarting unit test for parse_kv")

    #```
    #       if "=" in x:
    #            # split the string on the first unescaped '='
    #            k, v = split_args(x, '=', 1, True)
    #```

# Generated at 2022-06-13 07:16:03.149668
# Unit test for function parse_kv
def test_parse_kv():
    mystring=u'install=1 cache=1'
    mydict=parse_kv(mystring, check_raw=False)
    assert u'install' in mydict
    assert u'1' in mydict[u'install']

    mystring=u'install=1 cache=1'
    mydict=parse_kv(mystring, check_raw=True)
    assert u'install' in mydict
    assert u'1' in mydict[u'install']
    assert u'_raw_params' in mydict
    assert u'cache=1' in mydict[u'_raw_params']

    mystring=u'install=1 cache=1'
    mydict=parse_kv(mystring)
    assert u'install' in mydict

# Generated at 2022-06-13 07:16:12.920079
# Unit test for function split_args
def test_split_args():
    # Test 1
    args = "a=b c=\"foo bar\""
    result = split_args(args)
    expected = ['a=b', 'c="foo bar"']
    assert result == expected

    # Test 2
    args = "a=b c=\"foo bar\"\nd=e f=\"bar foo\""
    result = split_args(args)
    expected = ['a=b', 'c="foo bar"', 'd=e', 'f="bar foo"']
    assert result == expected

    # Test 3
    args = "a=b {{c=\"foo bar\"}}\nd=e f=\"bar foo\""
    result = split_args(args)
    expected = ['a=b', '{{c="foo bar"}}', 'd=e', 'f="bar foo"']
    assert result == expected



# Generated at 2022-06-13 07:16:21.733246
# Unit test for function split_args
def test_split_args():
    '''
    For Ansible modules, we need to support parsing arguments to
    module parameters. That means we need to support splitting out
    spaces, but not when they are inside of quotes.
    '''

    # need to support splitting with quotes and spaces, but no newlines
    test_input = 'a="b c" d="e f" g'
    result = split_args(test_input)
    assert result == ['a="b c"', 'd="e f"', 'g'], "split_args with quotes and spaces failed"

    # need to support splitting with quotes, but no newlines
    test_input = 'a="b c" d="e f" g'
    result = split_args(test_input)

# Generated at 2022-06-13 07:16:31.878262
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a="b"') == {'a': 'b'}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a=b c=d', check_raw=True) == {'a': 'b', 'c': 'd'}

    assert parse_kv('a=b c=d arg1 arg2 arg3') == {
        'a': 'b', 'c': 'd', '_raw_params': 'arg1 arg2 arg3'}

# Generated at 2022-06-13 07:16:37.290976
# Unit test for function split_args
def test_split_args():
    import json
    import pprint


# Generated at 2022-06-13 07:16:51.023554
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'state="present"', check_raw=True) == {u'state': u'"present"'}
    assert parse_kv(u'creates=/tmp/penguins', check_raw=True) == {u'creates': u'/tmp/penguins'}
    assert parse_kv(u'state="present" creates=/tmp/penguins', check_raw=True) == {u'state': u'"present"', u'creates': u'/tmp/penguins'}
    assert parse_kv(u'creates=/tmp/penguins state="present"', check_raw=True) == {u'creates': u'/tmp/penguins', u'state': u'"present"'}
    # FIXME: This testcase raises an exception:
    #

# Generated at 2022-06-13 07:16:58.096657
# Unit test for function parse_kv
def test_parse_kv():
  # test1
  assert parse_kv(u'test=a b=c', False) == {u'test': u'a', u'b': u'c'}
  # test2
  assert parse_kv(u'echo "hello my name is" "my name is"', True) == {u'_raw_params': u'echo "hello my name is" "my name is"'}
  # test3
  assert parse_kv(u'hello=world hello1=world1 a=b=c') == {u'a': u'b=c', u'hello': u'world', u'hello1': u'world1'}
  # test4
  assert parse_kv(u'a=b\\=c') == {u'a': u'b=c'}
  # test5