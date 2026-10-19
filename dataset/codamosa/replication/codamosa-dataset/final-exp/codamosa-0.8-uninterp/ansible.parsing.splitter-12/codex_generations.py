

# Generated at 2022-06-13 07:07:42.072197
# Unit test for function parse_kv
def test_parse_kv():
    raw_string_result = parse_kv('foo=bar baz=qux biz="boz"', True)
    assert '_raw_params' not in raw_string_result
    assert 'foo' in raw_string_result
    assert 'bar' in raw_string_result.values()
    assert 'baz' in raw_string_result
    assert 'qux' in raw_string_result.values()
    assert 'biz' in raw_string_result
    assert 'boz' in raw_string_result.values()

    raw_string_result = parse_kv('foo=bar baz=qux biz="boz"', False)
    assert '_raw_params' not in raw_string_result
    assert 'foo' in raw_string_result
    assert 'bar' in raw_string_result

# Generated at 2022-06-13 07:07:54.260041
# Unit test for function parse_kv

# Generated at 2022-06-13 07:08:05.036233
# Unit test for function split_args

# Generated at 2022-06-13 07:08:12.969814
# Unit test for function split_args
def test_split_args():
    def test(s, r):
        result = split_args(s)
        if result != r:
            raise AssertionError("parsing {0} yielded {1} instead of {2}".format(s, result, r))

    test("foo", ["foo"])
    test("foo\nbar", ["foo", "\nbar"])
    test("foo bar", ["foo", "bar"])
    test("foo bar baz", ["foo", "bar", "baz"])
    test("foo bar\nbaz", ["foo", "bar\nbaz"])
    test("foo\nbar baz", ["foo\nbar", "baz"])
    test(r"foo\nbar\\baz", ["foo\nbar\\baz"])

# Generated at 2022-06-13 07:08:17.443179
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=b") == {"a": "b"}
    assert parse_kv("a=b c=d") == {"a": "b", "c": "d"}
    assert parse_kv("a='b c'") == {"a": "b c"}
    assert parse_kv("a='b c' d='e f'") == {"a": "b c", "d": "e f"}
    assert parse_kv("a=b c='d e'") == {"a": "b", "c": "d e"}
    assert parse_kv("a='b c' d=") == {"a": "b c", "d": ""}
    assert parse_kv("a=b c=''") == {"a": "b", "c": ""}

# Generated at 2022-06-13 07:08:27.010989
# Unit test for function split_args
def test_split_args():
    def join_split(arg_str):
        return join_args(split_args(arg_str))

    # Test basic splitting on spaces
    assert 'a b c' == join_split('a b c')
    # Test quote stripping
    assert 'a b" c' == join_split('a b" c')
    # Test newline handling
    assert 'a b\nc' == join_split('a b\nc')
    # Test jinja2 variable replacement
    assert 'a {{ var }} c' == join_split('a {{ var }} c')
    # Test jinja2 if/then/else handling
    assert 'a {% if var %}b{% else %}c{% endif %} d' == join_split('a {% if var %}b{% else %}c{% endif %} d')
   

# Generated at 2022-06-13 07:08:38.026323
# Unit test for function split_args
def test_split_args():
    '''
    test yaml parsing
    '''

# Generated at 2022-06-13 07:08:51.505528
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"a=b c='d e' f=g") == {u'a': u'b', u'c': u'd e', u'f': u'g'}
    assert parse_kv(u"a=b c='d=e' f=g") == {u'a': u'b', u'c': u'd=e', u'f': u'g'}
    assert parse_kv(u"a=b c='d=e' f=g", check_raw=True) == {u'a': u'b', u'c': u'd=e', u'f': u'g', u'_raw_params': u"a=b c='d=e' f=g"}

# Generated at 2022-06-13 07:09:02.524441
# Unit test for function split_args

# Generated at 2022-06-13 07:09:12.122462
# Unit test for function split_args
def test_split_args():
    '''
    Ensure that the argument splitter works as expected.
    '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    params = {}

# Generated at 2022-06-13 07:09:36.197790
# Unit test for function split_args
def test_split_args():
    from nose.tools import assert_equal, assert_true
    from ansible import errors
    # Test simple command
    assert_equal(split_args("/bin/true"), ["/bin/true"])
    assert_equal(split_args("/bin/true arg1 arg2 arg3"), ["/bin/true", "arg1", "arg2", "arg3"])
    # Test quoting
    assert_equal(split_args("/usr/bin/ls 'string1 string2'"), ["/usr/bin/ls", "'string1 string2'"])
    assert_equal(split_args("/usr/bin/ls \"string1 string2\""), ["/usr/bin/ls", "\"string1 string2\""])

# Generated at 2022-06-13 07:09:48.270674
# Unit test for function split_args
def test_split_args():
    assert split_args(r'foo="bar baz"') == ['foo=bar baz']
    assert split_args(r"foo='bar baz'") == ['foo=bar baz']
    assert split_args(r'foo=bar baz') == ['foo=bar', 'baz']
    assert split_args(r"foo=bar baz") == ['foo=bar', 'baz']
    assert split_args(r"foo='bar baz' bar") == ['foo=bar baz', 'bar']
    assert split_args(r"foo='bar baz' bar") == ['foo=bar baz', 'bar']
    assert split_args(r"foo='bar \"baz' bar") == ['foo=bar "baz', 'bar']

# Generated at 2022-06-13 07:09:57.785245
# Unit test for function split_args
def test_split_args():
    '''
    This test contains a bunch of test cases that should be parsed appropriately
    for the split_args function.
    the tests are in the following format:
    ( "input string", "output list", "string to be parsed at parse_kv()", "output of parse_kv" )
    '''

# Generated at 2022-06-13 07:10:06.217482
# Unit test for function split_args
def test_split_args():

    # Normal test cases
    assert(split_args(r"foo bar") == ["foo", "bar"])
    assert(split_args(r"foo bar baz") == ["foo", "bar", "baz"])
    assert(split_args(r"foo bar\nbaz") == ["foo", "bar\n", "baz"])
    assert(split_args(r"foo\ bar baz") == ["foo bar", "baz"])
    assert(split_args(r"foo\ bar\ baz") == ["foo bar", "baz"])
    assert(split_args(r"foo\\bar baz") == ["foo\\bar", "baz"])
    assert(split_args(r"foo\ bar\\ba-z") == ["foo bar\\ba-z"])

# Generated at 2022-06-13 07:10:16.966417
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=simple b="with spaces" c="this=that"') == {'a':'simple', 'b':'with spaces', 'c':'this=that'}
    assert parse_kv('a=simple b="with spaces" c="this=that"', check_raw=True) == {'a':'simple', 'b':'with spaces', 'c':'this=that', '_raw_params':'a=simple b=\"with spaces\" c=\"this=that\"'}



# Generated at 2022-06-13 07:10:25.345468
# Unit test for function split_args
def test_split_args():
    # test a valid parameter string
    args = 'a=b c=\'foo bar\' d="hello world"'
    params = split_args(args)
    assert(params == ['a=b', 'c=\'foo bar\'', 'd="hello world"'])

    # test some input with nested jinja2 blocks
    # the key is that parameters being passed to ansible modules
    # that aren't quoted should be in quotes, so this is a valid param
    # string, but won't work as expected if we split it naively
    args = 'echo "{{ foo }}"'
    params = split_args(args)
    assert(params == ['echo', '"{{ foo }}"'])

    # test some input with nested jinja2 blocks and quotes
    args = 'echo {{ foo }} "{{ bar }}"'

# Generated at 2022-06-13 07:10:29.397222
# Unit test for function parse_kv
def test_parse_kv():
    os.chdir('/Users/jcammarata/Projects/ansible/lib/ansible/modules/commands')
    args = "a=b c='d e' f=\"g h\" i=\\\"j k\\\""
    print(parse_kv(args))

# Generated at 2022-06-13 07:10:39.142511
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo', 'bar']
    assert split_args('"a=b c" d="foo \'bar"') == ['a=b c', 'd="foo', "'bar"]
    assert split_args("a='b c' d=\"foo \\\"bar\"") == ['a=b c', 'd=foo "bar']
    assert split_args("a='b c' d=foo\\ bar") == ['a=b c', 'd=foo bar']
    assert split_args("a=\\'b\\ c\\' d=foo\\ bar") == ["a='b c'", 'd=foo bar']
    assert split_

# Generated at 2022-06-13 07:10:45.514868
# Unit test for function parse_kv
def test_parse_kv():
    options = {}
    options.update(parse_kv("arg1=val1"))
    assert len(options) == 1
    assert options["arg1"] == "val1"

    options = {}
    options.update(parse_kv("arg1=val1 arg2=val2"))
    assert len(options) == 2
    assert options["arg1"] == "val1"
    assert options["arg2"] == "val2"

    options = {}
    options.update(parse_kv("arg1=val1 arg2=val2 arg3 arg4=val4"))
    assert len(options) == 3
    assert options["arg1"] == "val1"
    assert options["arg2"] == "val2"
    assert options["_raw_params"] == "arg3 arg4=val4"

    options = {}

# Generated at 2022-06-13 07:10:54.938153
# Unit test for function split_args
def test_split_args():
    '''
    This is the start of a unit test for the split_args() function.
    '''

    assert split_args('a=b c=d e=f') == ['a=b', 'c=d', 'e=f']
    assert split_args('a=b "quoted=thing"') == ['a=b', '"quoted=thing"']
    assert split_args('a=b "quoted=thing" c=d') == ['a=b', '"quoted=thing"', 'c=d']
    assert split_args('a=b !vars d=e') == ['a=b', '!vars', 'd=e']
    assert split_args('a=b "quoted !vars"') == ['a=b', '"quoted !vars"']
    assert split_

# Generated at 2022-06-13 07:11:10.528828
# Unit test for function parse_kv

# Generated at 2022-06-13 07:11:17.980081
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv('a=1 b=2', check_raw=True) == {u'a': u'1', u'b': u'2'}
    assert parse_kv('a=1 b=2 c') == {u'a': u'1', u'b': u'2'}
    assert parse_kv('a=1 b=2 c', check_raw=True) == {u'a': u'1', u'b': u'2', u'_raw_params': u'c'}
    assert parse_kv('a=1 b=2 c d') == {u'a': u'1', u'b': u'2'}

# Generated at 2022-06-13 07:11:28.322640
# Unit test for function split_args
def test_split_args():
    '''
    Test function split_args
    '''
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c=\'foo bar\'') == ['a=b', 'c=\'foo bar\'']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\') == ['a=b', 'c="foo bar\\']
    assert split_args('a=b c="foo bar\\"') == ['a=b', 'c="foo bar\\"']

# Generated at 2022-06-13 07:11:41.493291
# Unit test for function parse_kv
def test_parse_kv():
    # test single key/value
    d = parse_kv("key=value")
    assert d == {'key': 'value'}
    d = parse_kv("key='value'")
    assert d == {'key': 'value'}
    d = parse_kv("key=\"value\"")
    assert d == {'key': 'value'}
    d = parse_kv("key=\"quoted key\"=value")
    assert d == {'key': "quoted key=value"}
    d = parse_kv("key=='quoted value'")
    assert d == {'key': "quoted value"}
    d = parse_kv("key=\"quoted key\"=\"quoted value\"")
    assert d == {'key': "quoted key=quoted value"}

    # test multiple key/value

# Generated at 2022-06-13 07:11:50.907710
# Unit test for function split_args
def test_split_args():
    print("Testing split_args")
    params = split_args("{{ item }}")
    assert params == ["{{", "item", "}}"]

    params = split_args("{{ item }} -o")
    assert params == ["{{", "item", "}}", "-o"]

    params = split_args("{{ item }} -o {{ not_item }}")
    assert params == ["{{", "item", "}}", "-o", "{{", "not_item", "}}"]

    params = split_args("{{ item }} -o {{ not_item }} blah")
    assert params == ["{{", "item", "}}", "-o", "{{", "not_item", "}}", "blah"]

    params = split_args("{{ item }} -o {{ not_item }}\nblah")

# Generated at 2022-06-13 07:12:02.245821
# Unit test for function parse_kv
def test_parse_kv():
    print("Basic split_args")
    assert split_args("") == []
    assert split_args(" ") == []
    assert split_args("a") == ['a']
    assert split_args(" a ") == ['a']
    assert split_args(" a b ") == ['a b']
    assert split_args("a=\"a b\"") == ['a="a b"']
    assert split_args("a=\"a b\" c") == ['a="a b"', 'c']
    assert split_args("a=\"a b\" c d") == ['a="a b"', 'c d']
    assert split_args("a=\"a b\" c=\"d e\"") == ['a="a b"', 'c="d e"']

# Generated at 2022-06-13 07:12:09.491791
# Unit test for function split_args

# Generated at 2022-06-13 07:12:17.192698
# Unit test for function split_args
def test_split_args():
    '''
    test the arg splitter
    '''


# Generated at 2022-06-13 07:12:30.816754
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('one=1 two=2', check_raw=True) == dict(one='1', two='2')
    assert parse_kv('one=1 two=2', check_raw=False) == dict(one='1', two='2')
    assert parse_kv('one=1 two=2', check_raw=True) == dict(one='1', two='2')
    assert parse_kv('one="1" two="2"', check_raw=True) == dict(one='1', two='2')
    assert parse_kv('one=1 two="2"', check_raw=True) == dict(one='1', two='2')
    assert parse_kv('one="1" two=2', check_raw=True) == dict(one='1', two='2')
    assert parse

# Generated at 2022-06-13 07:12:45.152781
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(args=None) == {}
    assert parse_kv(args='') == {}
    assert parse_kv(args='a') == {}
    assert parse_kv(args='a=') == {}
    assert parse_kv(args='a=b') == {'a': 'b'}
    assert parse_kv(args='a= b') == {'a': 'b'}
    assert parse_kv(args='a = b') == {'a': 'b'}
    assert parse_kv(args='a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv(args='a=b c = d') == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-13 07:13:06.095179
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for split_args.
    '''
    # These functions are pulled from the ansible.utils.unicode.split_args() unit tests
    # with minor modifications.
    def _assert_split_eq(string, expected):
        result = split_args(string)
        if result != expected:
            raise AssertionError('Expected split_args(%r) to return %r, got %s instead' % (string, expected, result))

    def _assert_join_eq(string, expected):
        result = join_args(string)
        if result != expected:
            raise AssertionError('Expected join_args(%r) to return %r, got %s instead' % (string, expected, result))


# Generated at 2022-06-13 07:13:17.610461
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz=qux') == {'baz': 'qux', 'foo': 'bar'}
    assert parse_kv('foo=bar baz=') == {'baz': '', 'foo': 'bar'}
    assert parse_kv('foo=bar baz') == {'foo': 'bar', '_raw_params': 'baz'}
    assert parse_kv('foo=bar baz=qux a=b=c') == {'a': 'b=c', 'baz': 'qux', 'foo': 'bar'}
    assert parse_kv('foo="bar" baz=\\"qux\\"') == {'baz': '"qux"', 'foo': 'bar'}

# Generated at 2022-06-13 07:13:25.527034
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar biz=baz') == {
        'foo': 'bar',
        'biz': 'baz',
    }

    assert parse_kv('foo=bar=baz fiz=biz') == {
        'foo': 'bar=baz',
        'fiz': 'biz',
    }

    assert parse_kv('foo="bar baz" fiz=biz') == {
        'foo': 'bar baz',
        'fiz': 'biz',
    }

    # newline preserved
    assert parse_kv('foo="bar\nbaz" fiz=biz') == {
        'foo': 'bar\nbaz',
        'fiz': 'biz',
    }

    # newline preserved

# Generated at 2022-06-13 07:13:35.407362
# Unit test for function split_args

# Generated at 2022-06-13 07:13:41.782101
# Unit test for function split_args
def test_split_args():
    '''
    Unit tests for function split_args in module
    '''

    # Base case, no nesting
    assert split_args("a=b c=d") == ['a=b', 'c=d']

    # Simple nesting of single {{ }}
    assert split_args("a=b c={{ d }} e=f") == ['a=b', 'c={{ d }}', 'e=f']

    # Simple nesting of single {% %}
    assert split_args("a=b c={{ d }} e=f") == ['a=b', 'c={{ d }}', 'e=f']

    # Simple nesting of single {# #}
    assert split_args("a=b c={{ d }} e=f") == ['a=b', 'c={{ d }}', 'e=f']

    # Nesting of

# Generated at 2022-06-13 07:13:51.020096
# Unit test for function split_args
def test_split_args():
    assert split_args("foo bar") == ['foo', 'bar']

    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']

    assert split_args("foo bar=baz") == ['foo', 'bar=baz']

    assert split_args("foo space bar") == ['foo', 'space', 'bar']

    assert split_args("foo bar baz qux=corge") == ['foo', 'bar', 'baz', 'qux=corge']

    assert split_args("foo bar=\'baz qux\'") == ['foo', 'bar=\'baz qux\'']

    assert split_args("foo bar=baz\\ qux") == ['foo', 'bar=baz\\ qux']


# Generated at 2022-06-13 07:14:05.389601
# Unit test for function split_args
def test_split_args():
    assert split_args("Hello World") == ["Hello", "World"]
    assert split_args("Hello\nWorld") == ["Hello\nWorld"]
    assert split_args("Hello\nWorld\n") == ["Hello\nWorld\n"]
    assert split_args("Hello\nWorld\n\n") == ["Hello\nWorld\n\n"]
    assert split_args("Hello World\n") == ["Hello", "World\n"]
    assert split_args("Hello\nWorld ") == ["Hello\nWorld"]
    assert split_args("Hello \"World\"") == ["Hello", "\"World\""]
    assert split_args("Hello 'World'") == ["Hello", "'World'"]
    assert split_args("Hello \"Wor\\\"ld\"") == ["Hello", "\"Wor\\\"ld\""]

# Generated at 2022-06-13 07:14:11.305681
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:25.793551
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("key=value") == {"key": "value"}
    assert parse_kv("key=value   ") == {"key": "value"}
    assert parse_kv("key=value with white space") == {"key": "value with white space"}
    assert parse_kv("key\t=\tvalue with tab") == {"key": "value with tab"}
    assert parse_kv("key value") == {}
    assert parse_kv("key = value") == {"key": "value"}
    assert parse_kv("key==value") == {"key": "=value"}
    assert parse_kv("key=value with =") == {"key": "value with ="}
    assert parse_kv("key=value with white space before =") == {"key": "value with white space before ="}
    assert parse

# Generated at 2022-06-13 07:14:36.570042
# Unit test for function split_args
def test_split_args():

    assert split_args('') == []
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('"a=b c=d"') == ['"a=b c=d"']
    assert split_args('a="b c" d') == ['a="b c"', 'd']
    assert split_args(r'a=b\ c=d') == ['a=b c=d']
    assert split_args(r'a=b\\ c=d') == ['a=b\\', 'c=d']
    assert split_args('a={{ a }} b={{b }}') == ['a={{', 'a', '}}', 'b={{b', '}}']


# Generated at 2022-06-13 07:14:50.037996
# Unit test for function split_args
def test_split_args():
    def assert_split(args, expected):
        result = split_args(args)
        assert result == expected, '''test_split_args: %r
Return:      %r
Expected:    %r''' % (args, result, expected)

    assert_split('foo', ['foo'])
    assert_split(' foo ', ['foo'])
    assert_split('foo bar', ['foo', 'bar'])
    assert_split('foo      bar', ['foo', 'bar'])
    assert_split('foo \nbar', ['foo', 'bar'])
    assert_split('foo \n bar', ['foo', 'bar'])
    assert_split('foo "bar"', ['foo', 'bar'])
    assert_split('foo "bar baz"', ['foo', 'bar baz'])

# Generated at 2022-06-13 07:14:58.692590
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("arg1=val1 arg2='val 2' arg3=\"val 3\"", check_raw=False) ==\
        {u"arg1": u"val1", u"arg2": u"val 2", u"arg3": u"val 3"}
    assert parse_kv("arg1=val1 arg2=val\\=2 arg3=val\\\\=3", check_raw=False) ==\
        {u"arg1": u"val1", u"arg2": u"val=2", u"arg3": u"val\\=3"}
    assert parse_kv("arg1=val1 arg2=val\\u0020", check_raw=False) ==\
        {u"arg1": u"val1", u"arg2": u"val "}

# Generated at 2022-06-13 07:15:05.465435
# Unit test for function parse_kv
def test_parse_kv():
    # Ported from shell/command.py
    raw = u'mkdir -p "a dir" with=args'
    parsed = {u'mkdir': u'-p', u'a dir': u'with=args', u'_raw_params': u'"a dir" with=args'}
    assert parse_kv(raw, check_raw=True) == parsed

    raw = u"echo 'a'\\='b'"
    parsed = {u'_raw_params': u"echo 'a'\\='b'"}
    assert parse_kv(raw, check_raw=True) == parsed

    raw = u"echo 'a'\\='b' 'c'"
    parsed = {u'_raw_params': u"echo 'a'\\='b' 'c'"}

# Generated at 2022-06-13 07:15:16.533230
# Unit test for function split_args
def test_split_args():
    print("Testing function split_args")
    assert(
        split_args('a=b c="foo bar"') ==
        ["a=b", "c=\"foo bar\""]
    )
    assert(
        split_args(r'a=b c="foo\ bar"') ==
        ["a=b", r"c=\"foo\ bar\""]
    )
    assert(
        split_args(r'a=b c=foo\ bar d="foo bar"') ==
        ["a=b", r"c=foo\ bar", "d=\"foo bar\""]
    )

# Generated at 2022-06-13 07:15:27.379239
# Unit test for function split_args
def test_split_args():
    args = 'echo "hello world" {# comment #} {% macro test(name="val") %}{% endmacro %} {{ variable }}'
    result = split_args(args)
    assert result == [u'echo', u'"hello world"', u'{#', u'comment', u'#}', u'{%', u'macro', u'test(name="val")', u'%}', u'{%', u'endmacro', u'%}', u'{{', u'variable', u'}}']

    args = 'echo "hello world"'
    result = split_args(args)
    assert result == [u'echo', u'"hello world"']

    args = 'echo "hello world" {% macro test(name="val") %}{% endmacro %}'

# Generated at 2022-06-13 07:15:38.087673
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Check that escaped quotes work
    assert parse_kv('foo="bar \"baz\""') == {u'foo': to_text(u'bar "baz"')}
    assert parse_kv("foo='bar \"baz\"'") == {u'foo': to_text(u'bar "baz"')}
    assert parse_kv("foo='bar \'baz\'', bar=\"foo bar\", baz=\"foo bar\",") == {
        u'foo': to_text(u'bar \'baz\''),
        u'bar': to_text(u'foo bar'),
        u'baz': to_text(u'foo bar'),
    }


# Generated at 2022-06-13 07:15:47.801084
# Unit test for function split_args
def test_split_args():
    import pprint

    def assert_split(input, expected):
        output = split_args(input)
        if output != expected:
            print("Expected:")
            print(pprint.pformat(expected))
            print()
            print("Output:")
            print(pprint.pformat(output))
            assert output == expected

    assert_split("a=b c=\"foo bar\" d='hello world' e", [u'a=b', u'c="foo bar"', u"d='hello world'", u'e'])
    assert_split("a=b c=\"foo bar\" d='hello world' e\nf", [u'a=b', u'c="foo bar"', u"d='hello world'", u'e\nf'])

# Generated at 2022-06-13 07:15:54.776346
# Unit test for function parse_kv
def test_parse_kv():
    # Parse single key/value pair
    res = parse_kv('foo=bar')
    assert res == {u'foo': u'bar'}

    # Parse multiple key/value pairs
    res = parse_kv('foo=bar biz=baz')
    assert res == {u'foo': u'bar', u'biz': u'baz'}

    # Parse multiple key/value pairs with whitespace
    res = parse_kv('  foo =   bar biz = baz  bat  bam  =  baz ')
    assert res == {u'foo': u'bar', u'biz': u'baz', u'bat  bam': u'baz'}

    # Parse values with internal quotes

# Generated at 2022-06-13 07:16:04.695274
# Unit test for function split_args
def test_split_args():
    import pytest
    # simple test case with whitespace and line continuation
    test_result = split_args("foo=bar \\ --baz")
    assert test_result == ['foo=bar', '\\', '--baz']

    test_result = split_args("foo={{ bar }}")
    assert test_result == ['foo={{', 'bar', '}}']

    test_result = split_args("foo=\"{{ bar }}\"")
    assert test_result == ['foo="{{ bar }}"']

    test_result = split_args("foo=\"{{ bar }} \\\" \"")
    assert test_result == ['foo="{{ bar }} \\\" "']

    test_result = split_args("foo='{{ bar }}'")
    assert test_result == ["foo='{{ bar }}'"]

    test_result = split_args

# Generated at 2022-06-13 07:16:13.907238
# Unit test for function split_args

# Generated at 2022-06-13 07:16:27.556714
# Unit test for function split_args
def test_split_args():
    print('Testing nested blocks and quotes')
    cmd = '''{{this.stdout.stdout.results | stringify | regex_replace('(\\"|\\n|\\r|\\t|\\f|\\b)', '')}}|
    regex_search("(\\s|^|=){{{{item[0]}}}}=([0-9]+\\.)?([0-9]+\\.)?([0-9]+\\.)?([0-9]+)(\\s|\\Z|$)")'''

# Generated at 2022-06-13 07:16:30.093598
# Unit test for function parse_kv
def test_parse_kv():
    assert {
            u'_raw_params': u'a=b',
            u'a': u'b'
            } == parse_kv(u'a=b')


# Generated at 2022-06-13 07:16:35.820748
# Unit test for function parse_kv
def test_parse_kv():
    assert (parse_kv('foo=bar') == {'foo': 'bar'})
    assert (parse_kv('foo="bar baz"') == {'foo': 'bar baz'})
    assert (parse_kv('foo=bar\\=baz') == {'foo': 'bar=baz'})
    assert (parse_kv('foo="bar\\=baz"') == {'foo': 'bar=baz'})
    assert (parse_kv('foo=bar\\ baz') == {'foo': 'bar baz'})
    assert (parse_kv('foo="bar\\ baz"') == {'foo': 'bar baz'})
    assert (parse_kv('foo="bar baz"') == {'foo': 'bar baz'})

# Generated at 2022-06-13 07:16:49.505214
# Unit test for function parse_kv
def test_parse_kv():
    # Test for a simple kv
    assert parse_kv("key value with space") == {"key": "value with space"}

    # Test for a simple kv with quotes
    assert parse_kv("key \"value with space\"") == {"key": "value with space"}

    # Test for a complex kv
    assert parse_kv("key=value val=value") == {"key": "value", "val": "value"}

    # Test for a complex kv with an escaped equals
    assert parse_kv("key=value val\\=ue") == {"key": "value", "val=ue": None}

    # Test for a complex kv with an escaped quotes
    assert parse_kv("key='value' val=\"value\"") == {"key": "value", "val": "value"}

    # Test for a complex kv with a

# Generated at 2022-06-13 07:16:57.493808
# Unit test for function split_args
def test_split_args():
    '''
    parser: arg splitting functions: split and join
    '''

    params = split_args('foo=bar')
    assert params == ['foo=bar']

    params = split_args("foo=\"bar baz\"")
    assert params == ['foo="bar baz"']

    params = split_args("foo=\"bar' baz\"")
    assert params == ["foo=\"bar' baz\""]

    params = split_args("foo='bar\" baz'")
    assert params == ["foo='bar\" baz'"]

    params = split_args("foo=\"bar baz\"'")
    assert params == ["foo=\"bar baz\"'"]

    params = split_args("foo=bar \"baz quux\"")
    assert params == ["foo=bar", "\"baz quux\""]

    params = split