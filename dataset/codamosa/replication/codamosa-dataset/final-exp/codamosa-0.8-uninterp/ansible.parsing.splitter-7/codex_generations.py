

# Generated at 2022-06-13 07:07:40.652239
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'ab=c d=e') == {u'ab': u'c', u'd': u'e'}
    assert parse_kv(u'a"b=c" d"=e"') == {u'ab': u'c', u'd=e': u''}
    assert parse_kv(u'a"b=c" d"=e') == {u'ab': u'c', u'd': u'=e'}
    assert parse_kv(u'a"b=c" d"=e"') == {u'ab': u'c', u'd=e': u''}

# Generated at 2022-06-13 07:07:46.345258
# Unit test for function split_args

# Generated at 2022-06-13 07:07:55.891973
# Unit test for function split_args
def test_split_args():
    assert(split_args('a b c') == ['a', 'b', 'c'])
    assert(split_args('a "b c"') == ['a', '"b c"'])
    assert(split_args('a "b\\" c"') == ['a', '"b\\" c"'])
    assert(split_args('a "b\\" c"') == split_args('a "b\\\" c"'))
    assert(split_args('a "b\\" c"') == split_args('a "b\\\\" c"'))
    assert(split_args('a "b\\" c"') == split_args(r'a "b\\" c"'))
    assert(split_args(r'a "b\\" c"') == split_args('a "b\\\\" c"'))

# Generated at 2022-06-13 07:08:06.307246
# Unit test for function split_args
def test_split_args():
    # test 1: simple, no args
    test_list = [
        "",
        " ",
        "  ",
        "\t",
        "\n",
        " \t \n",
    ]
    for arg in test_list:
        assert split_args(arg) == [""]

    # test 2. just args

# Generated at 2022-06-13 07:08:13.728138
# Unit test for function split_args

# Generated at 2022-06-13 07:08:25.412858
# Unit test for function split_args

# Generated at 2022-06-13 07:08:37.269310
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('A=B C="D E"') == dict(A = "B", C = "D E")
    assert parse_kv('A=B=C') == dict(A = "B=C")
    assert parse_kv('"A=B" C=D') == dict(A = "B", C = "D")
    assert parse_kv('A=B "C=D"') == dict(A = "B", C = "D")
    assert parse_kv('A="B=C"="D"') == dict(A = "B=C=D")
    assert parse_kv('A=B "C=D" E="F G"') == dict(A = "B", C = "D", E = "F G")
   

# Generated at 2022-06-13 07:08:47.454061
# Unit test for function parse_kv
def test_parse_kv():
    # Test basic functionality
    x = parse_kv('a=1 b=2 c="3 3 3" d=\'4 4 4\'')
    assert x == {u'a':u'1', u'b':u'2', u'c':u'3 3 3', u'd':u'4 4 4'}, x

    # Test unicode functionality
    x = parse_kv('a="\\u03a9"')
    assert x == {u'a': u'\u03a9'}, x

    # Test single-char escapes
    x = parse_kv("a='\\n \\t \\007 \\n'")
    assert x == {u'a': u'\n \t \x07 \n'}, x


# Generated at 2022-06-13 07:08:52.508772
# Unit test for function split_args

# Generated at 2022-06-13 07:09:03.891338
# Unit test for function parse_kv
def test_parse_kv():
    test_str = "arg1=foo arg2=bar"
    test_str2 = "arg1=foo arg2=\"foo bar\" arg3=baz"
    test_str3 = "arg1=foo arg2='foo bar' arg3=baz"
    test_str4 = "arg1=foo arg2='foo bar' arg3=baz arg4='single space' "
    test_str6 = "arg1=foo arg2='foo bar' arg3=baz arg4='single space' arg5='leading space'"
    test_str5 = "arg1=foo arg2='foo bar' arg3=baz arg4='single space' arg5='leading space' arg6='trailing space '"
    test_str7 = "arg1='trailing space ' arg2='trailing space '"
    test_str

# Generated at 2022-06-13 07:09:37.428756
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('foo="bar"') == {u'foo': u'bar'}
    assert parse_kv('foo="bar two"') == {u'foo': u'bar two'}
    assert parse_kv('foo="bar two" dog="cat two"') == {u'foo': u'bar two', u'dog': u'cat two'}
    assert parse_kv('foo="bar=two" dog="cat=two"') == {u'foo': u'bar=two', u'dog': u'cat=two'}
    assert parse_kv('foo=bar dog=cat') == {u'foo': u'bar', u'dog': u'cat'}

# Generated at 2022-06-13 07:09:49.125704
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args(' ') == []
    assert split_args('   ') == []
    assert split_args('\n') == []
    assert split_args('foo') == ['foo']
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo \n bar') == ['foo', 'bar']
    assert split_args('foo\nbar\n') == ['foo', 'bar']
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo bar baz ') == ['foo', 'bar', 'baz']
    assert split_args('foo  bar') == ['foo', 'bar']
    assert split_args(' foo  bar') == ['foo', 'bar']


# Generated at 2022-06-13 07:09:58.357778
# Unit test for function split_args
def test_split_args():
    assert split_args("foo") == ["foo"]
    assert split_args("foo=bar") == ["foo=bar"]
    assert split_args("foo='bar'") == ["foo='bar'"]
    assert split_args("foo=\"bar\"") == ["foo=\"bar\""]
    assert split_args("foo=bar baz=zab") == ["foo=bar", "baz=zab"]
    assert split_args("foo=bar 'baz zab") == ["foo=bar", "'baz zab"]
    assert split_args("foo=bar \"baz zab") == ["foo=bar", "\"baz zab"]
    assert split_args("foo=bar foo2=bar2 'baz zab") == ["foo=bar", "foo2=bar2", "'baz zab"]
    assert split_args

# Generated at 2022-06-13 07:10:08.136467
# Unit test for function split_args

# Generated at 2022-06-13 07:10:20.657440
# Unit test for function split_args
def test_split_args():
    assert split_args(u"foo") == [u"foo"]
    assert split_args(u"foo bar") == [u"foo", u"bar"]
    assert split_args(u"foo\\ bar") == [u"foo bar"]
    assert split_args(u"foo \\\n bar") == [u"foo \\", u"bar"]
    assert split_args(u"'foo bar'") == [u"'foo bar'"]
    assert split_args(u"\"foo bar\"") == [u"\"foo bar\""]
    assert split_args(u"\"foo \\\nbar\"") == [u'"foo \\', u'bar"']
    assert split_args(u"foo='bar baz'") == [u"foo='bar baz'"]

# Generated at 2022-06-13 07:10:32.795631
# Unit test for function split_args
def test_split_args():
    '''
    Unit tests for function split_args
    '''
    # Each list of inputs/outputs for tests are in the following format
    # idx 0 - input args
    # idx 1 - output [list]
    # idx 2 - error (True or False)

# Generated at 2022-06-13 07:10:41.845792
# Unit test for function split_args
def test_split_args():
    class TestCase:
        def __init__(self, args, result):
            self.args = args
            self.result = result
    cases = []
    cases.append(TestCase("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"']))
    cases.append(TestCase("/bin/foo --bar \"up down\" --baz=3", ['/bin/foo', '--bar', '"up down"', '--baz=3']))
    cases.append(TestCase("/bin/foo --bar \"up \\\"down\" --baz=3", ['/bin/foo', '--bar', '"up \\\"down"', '--baz=3']))

# Generated at 2022-06-13 07:10:53.024601
# Unit test for function split_args
def test_split_args():
    """
    :return:
    """
    print("Starting split_args unit test...")

# Generated at 2022-06-13 07:10:58.921608
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args(r'''a=b c="foo bar" d='foo bar' e='foo\'bar' f="foo\"bar" g="foo'bar"''') == [
        'a=b', 'c="foo bar"', "d='foo bar'", r"e='foo\'bar'", r'f="foo\"bar"', r"g='foo\'bar'",
    ]

# Generated at 2022-06-13 07:11:07.719401
# Unit test for function parse_kv
def test_parse_kv():
    # Test parse_kv() with a variety of simple options
    assert parse_kv("a=b") == {'a': 'b'}
    assert parse_kv("a='b'") == {'a': 'b'}
    assert parse_kv("a=\"b\"") == {'a': 'b'}
    assert parse_kv("a=\"b=c d\"") == {'a': 'b=c d'}
    assert parse_kv("a='b=c d'") == {'a': 'b=c d'}
    assert parse_kv("a=b c=d") == {'a': 'b', 'c': 'd'}
    assert parse_kv("a=b c=\"d e\"") == {'a': 'b', 'c': 'd e'}


# Generated at 2022-06-13 07:11:27.034477
# Unit test for function split_args
def test_split_args():
    assert split_args("{{ shell_output }}") == ["{{", "shell_output", "}}"]
    assert split_args("a=b c=\"foo bar\"") == ["a=b", "c=\"foo bar\""]
    assert split_args("a b c {{ shell_output }}") == ["a", "b", "c", "{{", "shell_output", "}}"]
    assert split_args("a b c {{shell_output}}") == ["a", "b", "c", "{{shell_output}}"]
    assert split_args("a b c {{{{ shell_output }}}}") == ["a", "b", "c", "{{{{", "shell_output", "}}}}"]

# Generated at 2022-06-13 07:11:35.661634
# Unit test for function split_args
def test_split_args():

    assert split_args("") == []

    assert split_args("foo=bar baz") == [u'foo=bar', u'baz']
    assert split_args("baz foo=bar") == [u'baz', u'foo=bar']
    assert split_args("foo='bar baz'") == [u"foo='bar baz'"]
    assert split_args("foo='bar \"baz\"'") == [u'foo=\'bar "baz"\'']
    assert split_args("foo=bar baz=\"foo bar\"") == [u'foo=bar', u'baz="foo bar"']
    assert split_args("foo='\"bar baz\"'") == [u"foo='\"bar baz\"'"]

# Generated at 2022-06-13 07:11:46.504553
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo="bar baz"') == {u'foo': u'bar baz'}
    assert parse_kv('foo="bar baz') == {u'foo': u'bar baz'}
    assert parse_kv('foo="bar baz fuz') == {u'foo': u'bar baz fuz'}
    assert parse_kv('foo="bar baz fuz\\') == {u'foo': u'bar baz fuz\\'}
    assert parse_kv('foo="bar baz fuz\\"') == {u'foo': u'bar baz fuz\"'}
    assert parse_kv('foo="bar+baz+fuz\\"') == {u'foo': u'bar+baz+fuz\"'}

# Generated at 2022-06-13 07:11:53.559235
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args
    '''


# Generated at 2022-06-13 07:12:03.058413
# Unit test for function split_args
def test_split_args():
    # base case, no quotes or jinja2 blocks
    x = 'a=b c="foo bar"'
    assert split_args(x) == ['a=b', 'c="foo bar"']

    # base case, no quotes or jinja2 blocks
    x = 'a=b c="foo bar"'
    assert split_args(x) == ['a=b', 'c="foo bar"']

    # base case, no quotes or jinja2 blocks
    x = 'a=b c="foo bar"'
    assert split_args(x) == ['a=b', 'c="foo bar"']

    # simple case, single quoted string

# Generated at 2022-06-13 07:12:12.978953
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:24.619362
# Unit test for function split_args
def test_split_args():
    def _test(args, expected_result):
        result = split_args(args)
        assert result == expected_result, result

    _test('a=b c="foo bar"', ['a=b', 'c="foo bar"'])
    _test("a=b c='foo bar'", ['a=b', "c='foo bar'"])

    _test("a=b c\=d", ['a=b', "c=d"])
    _test("a=b c\=\\=d", ['a=b', "c==d"])
    _test("a=b c\'\\=d", ['a=b', "c'=d"])
    _test("a=b c'\\=d'", ['a=b', "c'=d'"])

# Generated at 2022-06-13 07:12:30.917445
# Unit test for function parse_kv
def test_parse_kv():
    # Test a simple key-value pair
    assert parse_kv("foo=bar") == dict(foo='bar')
    # Test a simple key-value pair with leading / trailing spaces
    assert parse_kv("  foo  =  bar  ") == dict(foo='bar')
    # Test a key-value pair with no equals sign
    assert parse_kv("foo=bar baz") == dict(foo='bar', _raw_params='baz')
    # Test a key-value pair with an escaped equals sign
    assert parse_kv("foo\\=bar=baz") == dict(foo='bar', _raw_params='baz')
    # Test a key-value pair with an escaped backslash

# Generated at 2022-06-13 07:12:45.217747
# Unit test for function split_args
def test_split_args():
    assert split_args('') == ['']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo', 'bar']
    assert split_args('a=b c="foo bar\"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c={{ foo }}') == ['a=b', 'c={{', 'foo', '}}']

# Generated at 2022-06-13 07:12:53.866607
# Unit test for function split_args
def test_split_args():
    # these test cases are going to be a map of
    # the original string, and the resulting split string
    # that should be returned
    tests = {}
    tests['foo=bar baz="one two three"'] = ['foo=bar', 'baz="one two three"']
    tests['foo=bar baz="one two three" quux=true'] = ['foo=bar', 'baz="one two three"', 'quux=true']
    tests['foo=bar baz="one two three" quux=true'] = ['foo=bar', 'baz="one two three"', 'quux=true']
    tests['foo=bar baz="one two three" quux=true'] = ['foo=bar', 'baz="one two three"', 'quux=true']

# Generated at 2022-06-13 07:13:13.058998
# Unit test for function parse_kv
def test_parse_kv():

    # Test parsing the empty string
    assert [] == split_args('')

    # Test parsing the empty list
    assert [] == split_args([])

    # Test parsing positional args
    assert ['arg1', 'arg2'] == split_args('arg1 arg2')
    assert ['arg1', 'arg2'] == split_args('arg1 "arg2"')
    assert ['arg1', 'arg2'] == split_args('arg1 "arg2" ')
    assert ['arg1', 'arg2'] == split_args('"arg1" arg2')
    assert ['arg1', 'arg2'] == split_args(' "arg1" arg2')

    # Test parsing argument with key=value and positional args

# Generated at 2022-06-13 07:13:23.538049
# Unit test for function split_args
def test_split_args():
    '''
    Return a tuple of args that should be replaced with a new list of args and the new list of args to replace it with
    '''

# Generated at 2022-06-13 07:13:33.359877
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == dict(foo="bar")
    assert parse_kv("foo= bar") == dict(foo="bar")
    assert parse_kv("foo=ba'r") == dict(foo="ba'r")
    assert parse_kv("  foo  =  bar  ") == dict(foo="bar")
    assert parse_kv("foo='bar'") == dict(foo="bar")
    assert parse_kv("foo='bar baz'") == dict(foo="bar baz")
    assert parse_kv("foo=bar,barz=baz") == dict(foo="bar", barz="baz")
    assert parse_kv("foo=\"bar\"") == dict(foo="bar")

# Generated at 2022-06-13 07:13:40.429837
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c={{ foo }}") == ['a=b', 'c={{ foo }}']
    assert split_args("a=b c='{{ foo }}'") == ['a=b', "c='{{ foo }}'"]
    assert split_args("a=b c=\"{{ foo }}\"") == ['a=b', 'c="{{ foo }}"']
    assert split_args("a=b c={{ foo }} d={{ bar }}") == ['a=b', 'c={{ foo }}', 'd={{ bar }}']

# Generated at 2022-06-13 07:13:50.111316
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"') != ['a=b', 'c="foo bar']
    assert split_args('a\'b=c') == ["a'b=c"]
    assert split_args('a=b c="foo bar') != ["a=b", "c=\"foo bar"]
    assert split_args('a=b c="foo bar\\"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\"') != ['a=b', 'c="foo bar\\"']
    assert split_args('a=b c="foo bar\\\'"') == ['a=b', 'c="foo bar\'"']
   

# Generated at 2022-06-13 07:13:54.334972
# Unit test for function parse_kv
def test_parse_kv():
    item = "Hello=world foo='bar baz' bam=bat"
    assert parse_kv(item) == {"Hello": "world", "foo": "bar baz", "bam": "bat"}

# Generated at 2022-06-13 07:14:08.299750
# Unit test for function parse_kv
def test_parse_kv():
    ''' Tests for the parse_kv function '''
    result = parse_kv(None, False)
    assert result == {}

    result = parse_kv('', False)
    assert result == {}

    result = parse_kv('a=b c=d')
    assert result == {'a': 'b', 'c': 'd'}

    result = parse_kv('a=b c=d', True)
    assert result == {'a': 'b', 'c': 'd'}

    result = parse_kv('a=b c=d', True)
    assert result == {'a': 'b', 'c': 'd'}

    result = parse_kv('a=b c=d _raw_params=foo bar baz')

# Generated at 2022-06-13 07:14:14.795172
# Unit test for function split_args
def test_split_args():
    # with quotes
    assert split_args(r"hello 'world'") == [u'hello', u"'world'"]
    assert split_args(r"hello \"world\"") == [u'hello', u'"world"']
    assert split_args(r"hello world\\'s") == [u'hello', u"world's"]
    assert split_args(r'hello world\\"s') == [u'hello', u'world"s']

    # with jinja2
    assert split_args(r"hello {% world %}") == [u'hello', u'{%', u'world', u'%}']
    assert split_args(r"hello {{ world }}") == [u'hello', u'{{', u'world', u'}}']
    assert split_args(r"hello {# world #}")

# Generated at 2022-06-13 07:14:18.660425
# Unit test for function parse_kv
def test_parse_kv():
    kv_result=parse_kv('key1=value1 key2=value2 key3="value3" key4=\'value4\'')
    assert kv_result=={u'key1': 'value1',u'key2': 'value2', u'key3': 'value3', u'key4': 'value4'}


# Generated at 2022-06-13 07:14:29.187382
# Unit test for function split_args

# Generated at 2022-06-13 07:14:46.196173
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=\"c\" c='d'") == {"a":"1", "b":"c", "c":"d"}
    assert parse_kv("a=1\tb=c\tc='d'") == {"a":"1", "b":"c", "c":"d"}
    assert parse_kv("a=1\nb=c\nc=d") == {"a":"1", "b":"c", "c":"d"}
    assert parse_kv("a = 1\nb = c\nc = d") == {"a":"1", "b":"c", "c":"d"}
    assert parse_kv("a=1 b=c c=d") == {"a":"1", "b":"c", "c":"d"}

# Generated at 2022-06-13 07:14:55.889926
# Unit test for function split_args
def test_split_args():
    assert(split_args("hello world") == ["hello", "world"])
    assert(split_args("foo=\"bar baz\"") == ["foo=\"bar baz\""])
    assert(split_args("foo=\"bar baz\" x=y") == ["foo=\"bar baz\"", "x=y"])
    assert(split_args("foo=\"bar baz\" x=y\nblah=haha") == ["foo=\"bar baz\" x=y", "blah=haha"])
    assert(split_args("foo=\"bar baz\"\nblah=haha") == ["foo=\"bar baz\"", "blah=haha"])
    assert(split_args("foo=he said \"hi there\"") == ['foo=he', 'said', '"hi there"'])

# Generated at 2022-06-13 07:15:03.370657
# Unit test for function parse_kv
def test_parse_kv():
    # No args string
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv('   ') == {}
    # Single argument
    assert parse_kv('k1=v1') == {'k1': 'v1'}
    assert parse_kv(' k1 = v1 ') == {'k1': 'v1'}
    assert parse_kv('k1=v1 k2=v2') == {'k1': 'v1', 'k2': 'v2'}
    # Multiple arguments
    assert parse_kv('k1=v1 k2=v2') == {'k1': 'v1', 'k2': 'v2'}
    # Escaped arguments

# Generated at 2022-06-13 07:15:12.151436
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo bar "baz qux"') == ['foo', 'bar', '"baz qux"']
    assert split_args('foo bar "baz qux') == ['foo', 'bar', '"baz', 'qux']
    assert split_args('foo bar baz" qux') == ['foo', 'bar', 'baz" qux']
    assert split_args('foo bar baz qux"') == ['foo', 'bar', 'baz qux"']
    assert split_args('"foo bar baz" qux') == ['"foo bar baz"', 'qux']
    assert split_args('"foo bar baz" qux') == ['"foo bar baz"', 'qux']
    assert split_

# Generated at 2022-06-13 07:15:18.923799
# Unit test for function parse_kv

# Generated at 2022-06-13 07:15:28.682989
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=b') == {u'a': u'b'}
    assert parse_kv(u'a="b=c"') == {u'a': u'b=c'}
    assert parse_kv(u'a="b=c" d=e') == {u'a': u'b=c', u'd': u'e'}
    assert parse_kv(u'a="b=c" "d=e f"') == {u'a': u'b=c', u'd=e f': u''}
    assert parse_kv(u'a="b=c" "d=e f"') == {u'a': u'b=c', u'd=e f': u''}

# Generated at 2022-06-13 07:15:38.918702
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('key=val,key=val') == {u'key' : u'val'}
    assert parse_kv('env[foo]=bar') == {u'env[foo]' : u'bar'}
    assert parse_kv('key="val"') == {u'key' : u'val'}
    assert parse_kv('key="val1 val2"') == {u'key' : u'val1 val2'}
    assert parse_kv('key="val1 val2,val3"') == {u'key' : u'val1 val2,val3'}
    assert parse_kv('key=val1 val2,val3') == {u'key' : u'val1', u'val2' : u'val3'}

# Generated at 2022-06-13 07:15:45.507573
# Unit test for function parse_kv
def test_parse_kv():
    args = 'foo=bar baz=qux'
    result = parse_kv(args, check_raw=False)
    wanted = {u'foo': u'bar', u'baz': u'qux'}
    assert result == wanted
    result = parse_kv(args, check_raw=True)
    assert result == wanted

    args = 'foo=bar baz'
    result = parse_kv(args, check_raw=False)
    wanted = {u'foo': u'bar'}
    assert result == wanted
    result  = parse_kv(args, check_raw=True)
    wanted = {u'foo': u'bar', u'_raw_params': u'baz'}
    assert result == wanted

    args = 'creates=foo bar'
    result = parse_k

# Generated at 2022-06-13 07:16:00.148601
# Unit test for function parse_kv
def test_parse_kv():

    s = "foo=bar"
    assert parse_kv(s) == {'foo': 'bar'}

    s = "foo=bar"
    assert parse_kv(s, check_raw=True) == {'foo': 'bar'}

    s = "foo=bar splat=flim"
    assert parse_kv(s) == {'foo': 'bar', 'splat': 'flim'}

    s = "foo=bar splat=flim"
    assert parse_kv(s, check_raw=True) == {'foo': 'bar', 'splat': 'flim'}

    s = "foo=bar splat=flim flam=baz"

# Generated at 2022-06-13 07:16:11.027723
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz=qux') == {'baz': 'qux', 'foo': 'bar'}
    assert parse_kv('foo="bar" baz="qux"') == {'baz': 'qux', 'foo': 'bar'}
    assert parse_kv('foo=\'bar\' baz=\'qux\'') == {'baz': 'qux', 'foo': 'bar'}
    assert parse_kv('foo="bar \" baz=\'qux\'"') == {'foo': 'bar " baz=\'qux\''}
    assert parse_kv('foo=bar baz=qux ssh -l') == {'baz': 'qux', 'foo': 'bar', '_raw_params': 'ssh -l'}
    assert parse_

# Generated at 2022-06-13 07:16:28.922993
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None, check_raw=False) is None
    assert parse_kv('', check_raw=False) == {}
    assert parse_kv('  ', check_raw=False) == {}
    assert parse_kv('=', check_raw=False) == {}
    assert parse_kv(' = ', check_raw=False) == {}
    assert parse_kv(' = ', check_raw=True) == {}
    assert parse_kv(' = foo', check_raw=True) == {'_raw_params': ' = foo'}
    assert parse_kv(' =foo', check_raw=True) == {'_raw_params': ' =foo'}
    assert parse_kv(' = foo ', check_raw=True) == {'_raw_params': ' = foo '}

# Generated at 2022-06-13 07:16:34.852001
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar\\') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar\\\n') == ['a=b', 'c="foo bar']
    assert split_args('a=b "c=\'foo bar') == ['a=b', '"c=\'foo bar']

# Generated at 2022-06-13 07:16:48.606259
# Unit test for function split_args
def test_split_args():
    def _assert(split_args, args, expected):
        split = split_args(args)
        joined = join_args(split)
        assert args == joined

    # Test escaped quotes
    _assert(split_args, u'foo bar "Z\\"OMG"', u'foo bar "Z\\"OMG"')
    _assert(split_args, u"foo bar 'Z\\'OMG'", u"foo bar 'Z\\'OMG'")

    # Test basic args
    _assert(split_args, u"foo bar", u"foo bar")
    _assert(split_args, u"foo bar  burp", u"foo bar  burp")
    _assert(split_args, u"foo bar\nbaz", u"foo bar\nbaz")

# Generated at 2022-06-13 07:16:57.081103
# Unit test for function parse_kv
def test_parse_kv():
    # Basic test
    options = parse_kv("foo=bar baz=qux")
    assert options == {u'foo': u'bar', u'baz': u'qux'}
    # test with escaping
    options = parse_kv("foo='with\\ bsp' bar=in\\ quotes baz=no_quotes")
    assert options == {u'foo': u'with bsp', u'bar': u'in quotes', u'baz': u'no_quotes'}
    # test with empty values
    options = parse_kv("foo= bar=true baz=")
    assert options == {u'foo': u'', u'bar': u'true', u'baz': u''}
    # test with no values
    options = parse_kv("foo bar baz")
    assert options

# Generated at 2022-06-13 07:17:09.305657
# Unit test for function parse_kv
def test_parse_kv():
    import pytest