

# Generated at 2022-06-13 07:07:54.079426
# Unit test for function parse_kv
def test_parse_kv():
    # Check handling of empty string
    assert parse_kv("") == {}

    # Test correct parsing of options
    assert parse_kv("a=1 b=2") == dict(a='1', b='2')
    assert parse_kv("c=3 d=4") == dict(c='3', d='4')
    assert parse_kv("e=5 f=6") == dict(e='5', f='6')
    assert parse_kv("g=7 h=8") == dict(g='7', h='8')
    assert parse_kv("i='1 2 3' j=2") == dict(i='1 2 3', j='2')
    assert parse_kv("k=3 l='1   2   3'") == dict(k='3', l='1   2   3')

# Generated at 2022-06-13 07:08:02.115441
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {u'foo': u'bar'}

    assert parse_kv('foo=bar baz') == {u'_raw_params': u'foo=bar baz'}
    assert parse_kv('foo=bar baz', check_raw=True) == {u'foo': u'bar', u'_raw_params': u'baz'}

    assert parse_kv('foo=bar\n baz') == {u'_raw_params': u'foo=bar\nbaz'}
    assert parse_kv('foo=bar\n baz', check_raw=True) == {u'foo': u'bar', u'_raw_params': u'baz'}


# Generated at 2022-06-13 07:08:11.233103
# Unit test for function parse_kv
def test_parse_kv():
    def parse_kv_test(t):
        return parse_kv(t[0], check_raw=t[2]) == t[1]

# Generated at 2022-06-13 07:08:18.531165
# Unit test for function parse_kv
def test_parse_kv():
    test1 = "first=1 second=2 third=3"
    expected1 = dict(first='1', second='2', third='3')
    assert parse_kv(test1) == expected1

    test2 = r"first='1' second='2' third='3'"
    expected2 = dict(first='1', second='2', third='3')
    assert parse_kv(test2) == expected2

    test3 = r"first='1' second='2' 'third=3'"
    expected3 = dict(first='1', second='2', _raw_params="'third=3'")
    assert parse_kv(test3) == expected3

# Generated at 2022-06-13 07:08:27.215426
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == dict(foo="bar")
    assert parse_kv('foo="bar"') == dict(foo="bar")
    assert parse_kv("foo='bar'") == dict(foo="bar")
    assert parse_kv("foo=bar+baz") == dict(foo="bar baz")
    assert parse_kv("foo='bar baz'") == dict(foo="bar baz")
    assert parse_kv("foo=bar baz") == dict(_raw_params="foo=bar baz")
    assert parse_kv("foo='bar baz'") == dict(_raw_params="foo='bar baz'")
    assert parse_kv("foo='bar baz' one=two") == dict(foo="bar baz", one="two")
    assert parse_k

# Generated at 2022-06-13 07:08:38.170089
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv('creates=/tmp/foo executable=/bin/bash removes=/tmp/bar warn=no')
    assert(options['creates'] == '/tmp/foo')
    assert(options['executable'] == '/bin/bash')
    assert(options['removes'] == '/tmp/bar')
    assert(options['warn'] == 'no')
    assert(not options.has_key('_raw_params'))
    options = parse_kv('creates=/tmp/foo executable=/bin/bash removes=/tmp/bar warn=no c=/tmp/baz d=/tmp/qux', check_raw=True)
    assert(options['creates'] == '/tmp/foo')
    assert(options['executable'] == '/bin/bash')
    assert(options['removes'] == '/tmp/bar')

# Generated at 2022-06-13 07:08:51.584984
# Unit test for function parse_kv
def test_parse_kv():
    def parse_and_check(s, expected, check_raw=False):
        assert parse_kv(s, check_raw=check_raw) == expected

    examples = (
        (u'start=true', {u'start': u'true'}),
        (u"name='Steve'", {u"name": u"'Steve'"}),
    )

    for s, expected in examples:
        yield (parse_and_check, s, expected, False)

    # raw_params
    s = u"name=Steve start=true"
    expected = {u"name": u"Steve", u"start": u"true", u"_raw_params": u"name=Steve start=true"}
    yield (parse_and_check, s, expected, True)

    # single-quoted string
    s = u

# Generated at 2022-06-13 07:09:02.627208
# Unit test for function split_args
def test_split_args():
    myargs = """a=b c="foo bar" "foo bar" 'foo bar'"""
    pieces = split_args(myargs)

    assert pieces == ['a=b', 'c="foo bar"', '"foo bar"', "'foo bar'"]

    # test with a variable number of spaces

# Generated at 2022-06-13 07:09:12.235007
# Unit test for function split_args
def test_split_args():
    # Record of tests.  Each list element is a 2-tuple of an arg string, and a list of expected results.
    # The list of results is joined to create the expected argument string.
    tests = []
    tests.append(('foo bar', ['foo', 'bar']))
    tests.append(('foo \\n bar', ['foo', '\\n', 'bar']))
    tests.append((r'foo "bar baz"', ['foo', '"bar baz"']))
    tests.append((r'foo "bar \\\" baz"', ['foo', r'"bar \" baz"']))
    tests.append((r'foo "bar \\\\\" baz"', ['foo', r'"bar \\\" baz"']))

# Generated at 2022-06-13 07:09:20.136228
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('name=bob') == dict(name='bob')
    assert parse_kv('"name= with spaces=bob"') == dict(name=u' with spaces', u=u'bob')
    assert parse_kv('name=bob,key=value') == dict(name='bob', key='value')
    assert parse_kv('name="bob,joe"') == dict(name='bob,joe')
    assert parse_kv('name="one=two,three=four"') == dict(name='one=two,three=four')
    assert parse_kv('name="one=two,three=four",foo=bar') == dict(name='one=two,three=four', foo='bar')

# Generated at 2022-06-13 07:09:34.694962
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args(u"a=b c=foo\nbar d=baz") == ['a=b', 'c=foo', 'bar', 'd=baz']
    assert split_args(u"a=b c=foo\\\nbar d=baz") == ['a=b', 'c=foo\\', 'bar', 'd=baz']
    assert split_args(u"a=\"{{ foo }}\" c=\"foo\nbar\"") == ['a="{{ foo }}"', 'c="foo', 'bar"']

# Generated at 2022-06-13 07:09:47.240077
# Unit test for function split_args
def test_split_args():
    """Unit test for split_args"""

    # the input and expected output for various tests

# Generated at 2022-06-13 07:09:56.948041
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u' a = 1  b= 2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u'a = \n 1 \t b= 2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u"a='1' b=\"2\"") == {u'a': u'1', u'b': u'2'}

# Generated at 2022-06-13 07:10:05.856748
# Unit test for function split_args

# Generated at 2022-06-13 07:10:10.788175
# Unit test for function split_args

# Generated at 2022-06-13 07:10:24.340492
# Unit test for function parse_kv
def test_parse_kv():
    """

    :return:
    """
    args = "creates=/tmp/test stdin=hello stdin_add_newline=yea strip_empty_ends=y maxlines=7"
    options = parse_kv(args, check_raw=False)
    assert options[u'creates'] == '/tmp/test'
    assert options[u'stdin'] == 'hello'
    assert options[u'stdin_add_newline'] == 'yea'
    assert options[u'strip_empty_ends'] == 'y'
    assert options[u'maxlines'] == '7'
    # parameter '7' will be treated as a raw parameter
    args = "nocolor=true creates=/tmp/test 7"
    options = parse_kv(args, check_raw=False)

# Generated at 2022-06-13 07:10:34.932571
# Unit test for function split_args
def test_split_args():
    # Single item
    assert split_args('test') == ['test']

    # Single item with spaces
    assert split_args('test with spaces') == ['test', 'with', 'spaces']

    # Basic quote test
    assert split_args('"test with spaces"') == ['test with spaces']

    # Basic quote test 2 - split_args supports both single and double quotes
    assert split_args('\'test with spaces\'') == ['test with spaces']

    # Basic quote test 3 - split_args supports both single and double quotes
    assert split_args('\'test with spaces"') == ['test with spaces']

    # Single item with spaces
    assert split_args('test with spaces') == ['test', 'with', 'spaces']

    # Single item with spaces

# Generated at 2022-06-13 07:10:42.997285
# Unit test for function split_args

# Generated at 2022-06-13 07:10:53.592520
# Unit test for function parse_kv
def test_parse_kv():
    '''
    unit test for function parse_kv
    '''
    assert parse_kv("foo=bar") == {u'foo': u'bar'}
    assert parse_kv("foo=bar x=y") == {u'foo': u'bar', u'x': u'y'}
    assert parse_kv("foo=bar x=y a=b") == {u'foo': u'bar', u'x': u'y', u'a': u'b'}
    assert parse_kv("foo=bar x=\"with spaces\"") == {u'foo': u'bar', u'x': u'with spaces'}
    assert parse_kv("foo=bar x=1,2,3") == {u'foo': u'bar', u'x': u'1,2,3'}



# Generated at 2022-06-13 07:11:00.587394
# Unit test for function split_args
def test_split_args():
    data = 'foo=%s' % ('bar')
    assert split_args(data) == ['foo=bar']
    data = 'foo=%s' % ('bar baz')
    assert split_args(data) == ['foo=bar baz']
    data = 'foo="%s"' % ('bar baz')
    assert split_args(data) == ['foo="bar baz"']
    data = 'foo=%s' % ('bar baz')
    assert split_args(data) == ['foo=bar baz']
    data = 'foo="%s"' % ('bar baz')
    assert split_args(data) == ['foo="bar baz"']
    data = 'foo="%s" bar=%s' % ('bar baz', 'def def')

# Generated at 2022-06-13 07:11:18.251179
# Unit test for function split_args
def test_split_args():
    # Test single line without quotes
    assert split_args("foo=bar baz=qux") == ['foo=bar', 'baz=qux']
    # Test multi-line without quotes
    assert split_args("foo=bar baz=qux\nboz=quux") == ['foo=bar baz=qux', 'boz=quux']
    # Test single line with quotes
    assert split_args("foo='bar baz' qux=quux") == ["foo='bar baz'", 'qux=quux']
    # Test multi-line with quotes
    assert split_args("foo='bar baz' qux=quux\nboz=quuuux") == ["foo='bar baz' qux=quux", 'boz=quuuux']
    # Test with a literal backslash
   

# Generated at 2022-06-13 07:11:28.517110
# Unit test for function split_args
def test_split_args():
    test_str = r'''
    a=b c="foo bar"
    d={{ foo }}
    e={% if foo %}f{% endif %}
    f=g {{h=i j=k}} l
    m='n o'
    p={{ q='r s' }}
    t="{{ u }} v"
    '''
    expected_results = [
        'a=b',
        'c="foo bar"',
        'd={{ foo }}',
        'e={% if foo %}f{% endif %}',
        'f=g {{h=i j=k}} l',
        "m='n o'",
        "p={{ q='r s' }}",
        't="{{ u }} v"',
    ]

    result = split_args(test_str)


# Generated at 2022-06-13 07:11:41.676520
# Unit test for function parse_kv

# Generated at 2022-06-13 07:11:51.026618
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b") == ["a=b"]
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    assert split_args("a=b c=d e=f") == ["a=b", "c=d", "e=f"]
    assert split_args("a='b=1 c=2'") == ["a='b=1 c=2'"]
    assert split_args("a='b=1 c=2' d='e=3 f=4'") == ["a='b=1 c=2'", "d='e=3 f=4'"]
    assert split_args("a=b c=\"d=1 e=2\"") == ["a=b", "c=\"d=1 e=2\""]

# Generated at 2022-06-13 07:12:02.318533
# Unit test for function split_args
def test_split_args():
    assert(split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"])

    assert(split_args("a=b {{ a }}={{ b }}") == ['a=b', "{{ a }}={{ b }}"])

    assert(split_args("a=b {{ a }}={{ b }} {% if 1 == 0 %} c=d{% else %} c=d {% endif %}") == ['a=b', "{{ a }}={{ b }}", "{% if 1 == 0 %} c=d{% else %} c=d {% endif %}"])


# Generated at 2022-06-13 07:12:08.097146
# Unit test for function split_args
def test_split_args():
    # test that the splitting works as expected
    testargs = u'test "foo={{bar}}" baz=\'{{qux}}\' "foo=\\"{{bar}}\\"" baz=\\\'{{qux}}\\\''
    res = split_args(testargs)
    assert res == [u'test', u'foo={{bar}}', u'baz=\'{{qux}}\'', u'foo="{{bar}}"', u'baz=\'{{qux}}\'']

    # test that we can reconstruct the original args
    assert join_args(res) == testargs



# Generated at 2022-06-13 07:12:16.655870
# Unit test for function split_args
def test_split_args():
    def _check_split(value, expected):
        if expected == split_args(value):
            return True
        else:
            raise AssertionError("Split of '%s' does not match expected value. Got %s but expected %s." % (value, split_args(value), expected))

    _check_split("foo", ['foo'])
    _check_split("foo bar", ['foo', 'bar'])
    _check_split("foo\nbar", ['foo\n', 'bar'])
    _check_split("foo bar\nbaz", ['foo', 'bar\n', 'baz'])
    _check_split("foo\nbar\nbaz", ['foo\n', 'bar\n', 'baz'])

    _check_split("foo=\"bar baz\"", ['foo="bar baz"'])

# Generated at 2022-06-13 07:12:27.455383
# Unit test for function split_args
def test_split_args():

    args = "{{ foo }} {{bar = b*r}} {{ baz }}"
    result = split_args(args)
    assert result == ['{{ foo }}', '{{bar = b*r}}', '{{ baz }}']

    args = "{{ foo }} {{bar = b*r}} {{ baz }} "
    result = split_args(args)
    assert result == ['{{ foo }}', '{{bar = b*r}}', '{{ baz }}']

    args = "{{ foo }}\n{{bar = b*r}}\n{{ baz }}"
    result = split_args(args)
    assert result == ['{{ foo }}\n', '{{bar = b*r}}\n', '{{ baz }}']

    args = "{{ foo }}\n{{bar = b*r}}\n{{ baz }} "
    result

# Generated at 2022-06-13 07:12:32.624796
# Unit test for function split_args
def test_split_args():

    def _do_test(args, expected):
        actual = split_args(args)
        assert actual == expected, "actual: %s, expected: %s" % (actual, expected)

    _do_test(u'a=b', ['a=b'])
    _do_test(u'a="b c"', ['a="b c"'])
    _do_test(u"a='b c'", ["a='b c'"])
    _do_test(u"a='b \"c\" d'", ['a=\'b \\"c\\" d\''])
    _do_test(u'a=\'b "c" d\'', ['a=\'b "c" d\''])

# Generated at 2022-06-13 07:12:46.769834
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:04.489523
# Unit test for function split_args
def test_split_args():
    print("test split_args")
    # simple tokens

# Generated at 2022-06-13 07:13:15.979490
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:24.911596
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv(u'a=b c=d', check_raw=True) == {'a': 'b', 'c': 'd'}
    assert parse_kv(u'a=b c=d _raw_params=e f') == {'a': 'b', 'c': 'd', '_raw_params': 'e f'}
    assert parse_kv(u'a=b c=d _raw_params=e f', check_raw=True) == {'a': 'b', 'c': 'd', '_raw_params': 'e f'}

# Generated at 2022-06-13 07:13:34.771602
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b') == ['a=b']
    assert split_args('hello world') == ['hello', 'world']
    assert split_args(r'hello\ world') == ['hello world']
    assert split_args(r'hello\ world') == [u'hello world']
    assert split_args(r'hello\ world') == ['hello world']
    assert split_args(r'hello\\ world') == ['hello\\', 'world']
    assert split_args(r'hello\\ world') == [u'hello\\', u'world']
    assert split_args(r'hello\\ world') == ['hello\\', 'world']
    assert split_args(r'hello\\\ world') == ['hello\\ world']
    assert split_args(r'hello\\\ world') == [u'hello\\ world']
   

# Generated at 2022-06-13 07:13:41.316977
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=abc def="foo bar" baz="123 456"') == {u'foo': u'abc', u'baz': u'123 456', u'def': u'foo bar'}
    assert parse_kv('foo=abc\\ def="foo bar" baz="123\\ 456"') == {u'foo': u'abc def', u'baz': u'123 456'}
    assert parse_kv("foo=abc\\ def=\"foo bar\" baz=\"123\\ 456\"") == {u'foo': u'abc def', u'baz': u'123 456'}

# Generated at 2022-06-13 07:13:50.665115
# Unit test for function parse_kv
def test_parse_kv():
    def test(args, result):
        assert result == parse_kv(args), "Failed to parse: %s" % args

    test("a=1 b=2 c=3", dict(a='1', b='2', c='3'))
    test("c=1 d='2 3' e=4", dict(c='1', d='2 3', e='4'))
    test("'c=1 d=2'", dict(c='1', d='2'))
    test("c=1\\=2 d=2", dict(c='1=2', d='2'))
    test("c=\"1\\\"2\" d=2", dict(c='1"2', d='2'))
    test("key = value   another = foo", dict(key='value', another='foo'))

# Generated at 2022-06-13 07:13:56.252395
# Unit test for function parse_kv
def test_parse_kv():
    # Parse simple key-value pairs
    assert parse_kv('foo=bar bar=baz biz=bang') == dict(foo='bar', bar='baz', biz='bang')
    assert parse_kv('foo=bar,bar=baz') == dict(foo='bar', bar='baz')
    assert parse_kv('foo=bar,bar=baz', check_raw=True) == dict(foo='bar', bar='baz')
    assert parse_kv('foo=bar bar=baz', check_raw=True) == dict(foo='bar', bar='baz')
    # Parse key-value pairs with escaped quotes
    assert parse_kv('foo="bar" bar=baz biz="bang"') == dict(foo='bar', bar='baz', biz='bang')
    assert parse

# Generated at 2022-06-13 07:13:57.702127
# Unit test for function parse_kv
def test_parse_kv():
    os.system('python ./test.py')


# Generated at 2022-06-13 07:14:06.784315
# Unit test for function parse_kv
def test_parse_kv():
    args = "one=1 two=2 three='3 three'"
    assert parse_kv(args) == dict(one='1', two='2', three='3 three')
    args = "one=1 two=2 three='3\\ three'"
    assert parse_kv(args) == dict(one='1', two='2', three='3 three')
    args = 'one=1 two=2 three=\'3=three\''
    assert parse_kv(args) == dict(one='1', two='2', three='3=three')
    args = 'one=1 two=2 three=\'3\\=three\''
    assert parse_kv(args) == dict(one='1', two='2', three='3=three')

# Generated at 2022-06-13 07:14:13.700964
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=2") == dict(a="1", b="2")
    assert parse_kv("a='1 2' b=2") == dict(a="1 2", b="2")
    assert parse_kv("a=\\'1 2\\' b=2") == dict(a=u"'1 2'", b="2")
    assert parse_kv("a=\"1 2\" b=2") == dict(a="1 2", b="2")
    assert parse_kv("a=\\\"1 2\\\" b=2") == dict(a=u"\"1 2\"", b="2")
    assert parse_kv("'a=b c=d'") == dict(a='b c=d')

# Generated at 2022-06-13 07:14:29.346857
# Unit test for function split_args
def test_split_args():
    args = 'a b="foo bar" c="a b" d=\'e f\''
    assert split_args(args) == ['a', 'b="foo bar"', 'c="a b"', "d='e f'"]
    args = """a={{b c 'd e'}} f='g h' i="{{'j' 'k'}}" l=m
    n={{o p 'q{{r}}s'}}"""
    assert split_args(args) == ["a={{b c 'd e'}}", "f='g h'", "i=\"{{'j' 'k'}}\"", 'l=m', "n={{o p 'q{{r}}s'}}"]

# Generated at 2022-06-13 07:14:39.419925
# Unit test for function split_args
def test_split_args():
    args = "asdf=foo foo=bar \"baz={{ a_jinja_var }}\""
    assert split_args(args) == ['asdf=foo', 'foo=bar', 'baz={{ a_jinja_var }}']

    args = "\"asdf=foo {{ foo=\"asdf\" }}\" {{ bar=\"{{ baz }}\" }}"
    assert split_args(args) == ['asdf=foo {{ foo="asdf" }}', '{{ bar="{{ baz }}" }}']

    args = 'a=b c="foo bar"'
    assert split_args(args) == ['a=b', u'c="foo bar"']

    args = '"a=b" c="foo bar"'
    assert split_args(args) == [u'a=b', u'c="foo bar"']

   

# Generated at 2022-06-13 07:14:46.855007
# Unit test for function split_args

# Generated at 2022-06-13 07:14:56.032746
# Unit test for function parse_kv

# Generated at 2022-06-13 07:15:03.477616
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=1 b=2 c=3') == {'a': '1', 'b': '2', 'c': '3'}
    assert parse_kv(u"a='1 2' b='2 3' c='4 5'") == {'a': '1 2', 'b': '2 3', 'c': '4 5'}
    assert parse_kv(u"a='1 2' b='2 3' c='4 5' d") == {'a': '1 2', 'b': '2 3', 'c': '4 5', '_raw_params': 'd'}

# Generated at 2022-06-13 07:15:12.216363
# Unit test for function split_args

# Generated at 2022-06-13 07:15:18.934783
# Unit test for function split_args
def test_split_args():
    def _test_split_args(args, expected):
        params = split_args(args)
        assert params == expected, params
    _test_split_args('foo bar', ['foo', 'bar'])
    _test_split_args('foo "bar baz"', ['foo', '"bar baz"'])
    _test_split_args('foo "bar baz', ['foo', '"bar', 'baz'])
    _test_split_args('foo "bar \\\'baz', ['foo', '"bar \\\'baz'])
    _test_split_args('foo "bar \\"baz', ['foo', '"bar \\"baz'])
    _test_split_args('foo "bar \\"baz\\"', ['foo', '"bar \\"baz\\"'])
    _test

# Generated at 2022-06-13 07:15:28.682423
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"a=1 b=2") == dict(a=u"1", b=u"2")
    assert parse_kv(u"a='1 2' b='3 4'") == dict(a=u"1 2", b=u"3 4")
    assert parse_kv(u"a=\"1 2\" b=\"3 4\"") == dict(a=u"1 2", b=u"3 4")
    assert parse_kv(u"a=\"1 2\" b=3") == dict(a=u"1 2", b=u"3")
    assert parse_kv(u"a='1 2' b=3") == dict(a=u"1 2", b=u"3")

# Generated at 2022-06-13 07:15:38.918718
# Unit test for function parse_kv
def test_parse_kv():
    # Empty string
    assert parse_kv('') == {}

    # Empty key
    assert parse_kv('=') == {}

    # Empty value
    assert parse_kv('key=') == {u'key': u''}

    # Filled key and value
    assert parse_kv('key=value') == {u'key': u'value'}

    # Escaped values in value
    assert parse_kv(r'key=value\=baz=qux') == {u'key': u'value=baz=qux'}

    # Escaped quotes in value
    assert parse_kv(r"key=value\'\"baz") == {u'key': u'value\'"baz'}

    # Escaped values in key

# Generated at 2022-06-13 07:15:41.877315
# Unit test for function parse_kv
def test_parse_kv():
    print("Testing module")
    assert parse_kv("f='{test}'") == {'f': '{test}'}

if __name__ == "__main__":
    test_parse_kv()
# END UTILITY FUNCTION



# Generated at 2022-06-13 07:15:54.715500
# Unit test for function parse_kv
def test_parse_kv():
    # Basic kv
    assert parse_kv('a=1 b=2') == {'a': '1', 'b': '2'}
    # Handle quotes
    assert parse_kv(r'a=foo b="1 two" c=\'3 bar\'') == {'a': 'foo', 'b': '1 two', 'c': '3 bar'}
    # Handle escaped quotes
    assert parse_kv(r'a=foo b="\"1 two\"" c="\'3 bar\'"') == {'a': 'foo', 'b': '"1 two"', 'c': '\'3 bar\''}
    # Handle +, see #15393

# Generated at 2022-06-13 07:16:00.496548
# Unit test for function split_args
def test_split_args():
    import unittest
    import sys
    class TestSplitArgs(unittest.TestCase):
        def runTest(self):
            # Tests from the action plugin unit tests
            self.assertEqual(split_args(''), [])
            self.assertEqual(split_args('test1'), ['test1'])
            self.assertEqual(split_args('test1 test2'), ['test1', 'test2'])
            self.assertEqual(split_args('test1  test2'), ['test1', 'test2'])
            self.assertEqual(split_args(' test1 '), ['test1'])
            self.assertEqual(split_args(r'\test1'), [r'\test1'])

# Generated at 2022-06-13 07:16:11.215180
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('chdir=/root daemonize=true') == {"chdir": "/root", "daemonize": "true"}
    assert parse_kv('chdir=/root daemonize=true', check_raw=True) == {"chdir": "/root", "daemonize": "true"}
    assert parse_kv('user=foo group=bar chdir=/root daemonize=true') == {"user": "foo", "group": "bar", "chdir": "/root", "daemonize": "true"}
    assert parse_kv('user=foo group=bar chdir=/root daemonize=true', check_raw=True) == {"user": "foo", "group": "bar", "chdir": "/root", "daemonize": "true"}

# Generated at 2022-06-13 07:16:17.235989
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(
        argument_spec = dict(
            args = dict(required=True),
        )
    )

    def _assert_no_diff(a, b, msg):
        if a != b:
            m._diff = True
            m.fail_json(msg='%s: expected %s, got %s' % (msg, a, b))

    # Re-run function with real module to generate a diff
    def _assert_equal(a, b, msg):
        _assert_no_diff(a, b, msg)
        if m._diff:
            m.fail_json(msg='%s: expected %s, got %s' % (msg, a, b))

    # A dict of input/expected pairs
    test_data

# Generated at 2022-06-13 07:16:26.604272
# Unit test for function parse_kv
def test_parse_kv():

    #function parse_kv(args, check_raw=False):
    #
    # Convert a string of key/value items to a dict. If any free-form params
    # are found and the check_raw option is set to True, they will be added
    # to a new parameter called '_raw_params'. If check_raw is not enabled,
    # they will simply be ignored.
    #
    #args = u'a=b c="d" e="f=g" h=i=j k="l=m" "#n=o" "p q=r" s=t'

    a='a=b c="d" e="f=g" h=i=j k="l=m" "#n=o" "p q=r" s=t'

    #args = u'a=b c=\\"d\\

# Generated at 2022-06-13 07:16:36.828346
# Unit test for function split_args
def test_split_args():
    raw = (
        'a=b c="foo bar" d="{{ foo }} \\\\ {{ bar }}" '
        'e="{% foo %} \\\\ {% bar %}" f="{# foo #} \\\\ {# bar #}" '
        'g="{{ foo }} {% foo %} {# foo %}" h="{% foo %} {{ foo }} {# foo %}"'
    )

# Generated at 2022-06-13 07:16:50.450551
# Unit test for function parse_kv
def test_parse_kv():
    # test basic parsing
    (result, leftover) = parse_kv("foo=bar baz=quux")
    assert 'foo' in result
    assert result['foo'] == u'bar'
    assert 'baz' in result
    assert result['baz'] == u'quux'
    assert u'_raw_params' not in result

    # test quotes
    (result, leftover) = parse_kv("foo='bar baz'")
    assert 'foo' in result
    assert result['foo'] == u'bar baz'
    assert u'_raw_params' not in result

    (result, leftover) = parse_kv('foo="bar baz"')
    assert 'foo' in result
    assert result['foo'] == u'bar baz'
    assert u'_raw_params' not in result



# Generated at 2022-06-13 07:16:57.686887
# Unit test for function parse_kv
def test_parse_kv():
    expected = {
        u'_raw_params': u'"This is a string with embedded ="',
        u'ansible_become_user': u'"root"',
        u'ansible_check_mode': u'"off"',
        u'ansible_verbosity': u'"4"',
        u'other_arg': u'"foo=bar"',
        u'string': u'"this is a string"',
    }
    parsed = parse_kv(u'ansible_verbosity="4" ANSIBLE_CHECK_MODE=off string="this is a string" other_arg="foo=bar" ansible_become_user="root" _raw_params="\\"This is a string with embedded =\\""')
    assert parsed == expected

# Split args

# Generated at 2022-06-13 07:17:09.692360
# Unit test for function split_args
def test_split_args():
    assert split_args('"{{ foo }}"') == ['{{ foo }}']
    assert split_args('"a=b" "c=d" e=f') == [u'a=b', u'c=d', u'e=f']
    assert split_args('"a=b c=d" e=f') == [u'a=b c=d', u'e=f']
    assert split_args('"a=b c=d" "e=f"') == [u'a=b c=d', u'e=f']
    assert split_args("a=b c='d e'") == [u'a=b', u"c='d e'"]
    assert split_args("a=b c='d e'") == [u'a=b', u"c='d e'"]
   