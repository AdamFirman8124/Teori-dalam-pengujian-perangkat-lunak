

# Generated at 2022-06-13 07:07:57.592192
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b=foo') == { 'a': '1', 'b': 'foo' }
    assert parse_kv('a=1 b="foo"') == { 'a': '1', 'b': 'foo' }
    assert parse_kv('a=1 b=foo c=') == { 'a': '1', 'b': 'foo', 'c': '' }
    assert parse_kv('a=1 b="foo bar"') == { 'a': '1', 'b': 'foo bar' }
    assert parse_kv('a=1 b="foo \'bar\'"') == { 'a': '1', 'b': 'foo \'bar\'' }

# Generated at 2022-06-13 07:08:02.283125
# Unit test for function parse_kv
def test_parse_kv():
    #test basics
    assert parse_kv('k1=v1 k2=v2') == {'k1': 'v1', 'k2': 'v2'}
    assert parse_kv('k1=v1 k2=v2 k3 "arg1 arg2"') == {'k1': 'v1', 'k2': 'v2', '_raw_params': 'k3 "arg1 arg2"'}
    assert parse_kv('k1=v1 k2=v2 k3 \'arg1 arg2\'') == {'k1': 'v1', 'k2': 'v2', '_raw_params': 'k3 \'arg1 arg2\''}

# Generated at 2022-06-13 07:08:11.351442
# Unit test for function split_args
def test_split_args():
    def assert_split_args(inp, expected):
        actual = split_args(inp)
        assert actual == expected, 'split_args({!r}) -> {!r} != expected {!r}'.format(inp, actual, expected)

    # No quotes
    assert_split_args('foo bar baz', ['foo', 'bar', 'baz'])

    # No quotes with newlines
    assert_split_args('foo\nbar\nbaz', ['foo', 'bar', 'baz'])

    # Double quotes
    assert_split_args('foo "bar baz"', ['foo', '"bar baz"'])
    assert_split_args('foo "bar" "baz"', ['foo', '"bar"', '"baz"'])

# Generated at 2022-06-13 07:08:18.638977
# Unit test for function parse_kv
def test_parse_kv():
    keys = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
    }
    values = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
    }
    args = ' '.join([u'%s=%s' % (k, v) for k, v in keys.items()])
   

# Generated at 2022-06-13 07:08:27.627012
# Unit test for function split_args

# Generated at 2022-06-13 07:08:38.384186
# Unit test for function split_args

# Generated at 2022-06-13 07:08:51.663086
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert parse_kv('foo=bar baz=foobar') == dict(foo='bar', baz='foobar')
    assert parse_kv(u'foo=bar baz="foobar"') == dict(foo='bar', baz='foobar')
    # literal string using single quotes
    assert parse_kv(u'foo=bar baz=\'foobar\'') == dict(foo='bar', baz='foobar')
    # literal string using double quotes
    assert parse_kv(u'foo=bar baz="foobar"') == dict(foo='bar', baz='foobar')
    # literal string using double quotes with an escaped double quote
    assert parse_kv(u'foo=bar baz="foo\\"bar"')

# Generated at 2022-06-13 07:09:02.766816
# Unit test for function split_args
def test_split_args():
    # Test that split_args() works with when there are no quotes
    assert split_args('') == []
    assert split_args(' a  b ') == ['a', 'b']

    # Test that it works with basic quotes
    assert split_args('"a b c"') == ['a b c']
    assert split_args("'a b c'") == ['a b c']
    assert split_args("'a \" b'") == ['a \" b']
    assert split_args('"a \' b"') == ['a \' b']

    # Test that it works with escaped quotes
    assert split_args('"a \\" b"') == ['a " b']
    assert split_args("'a \\\' b'") == ['a \' b']

    # Test that it works with quotes within quotes
    assert split_args

# Generated at 2022-06-13 07:09:12.306394
# Unit test for function parse_kv
def test_parse_kv():
    args = "creates=/tmp/foo executable=/bin/bash remov es=/tmp/bar"
    options = parse_kv(args, check_raw=True)
    assert options[u'_raw_params'] == u"executable=/bin/bash remov es=/tmp/bar"
    args = 'blah="foo bar" bletch=\'{"a":1}\' zoinks={"a":1}'
    options = parse_kv(args, check_raw=True)
    assert options[u'_raw_params'] == u"bletch=\'{\"a\":1}\'"
    args = "spam={{ pig }} ham={{ cow }}"
    options = parse_kv(args, check_raw=True)

# Generated at 2022-06-13 07:09:20.595094
# Unit test for function split_args
def test_split_args():
    '''
    This function verifies that the results of split_args()
    are equivalent to the output of a shell on the same
    string for simple and complex cases
    '''
    # these are dictionary items, each of which contains an input and expected output
    # we use the expected outputs to verify
    # the results of split_args

# Generated at 2022-06-13 07:09:53.974358
# Unit test for function parse_kv
def test_parse_kv():
    args = "arg1=val1 arg2='12/34'"
    options = parse_kv(args)
    assert len(options) == 2
    assert options['arg1'] == 'val1'
    assert options['arg2'] == '12/34'

    options = parse_kv(args, check_raw=True)
    assert len(options) == 3
    assert options[u'_raw_params'] == "arg2='12/34'"

    args = "arg1=12/34"
    options = parse_kv(args, check_raw=True)
    assert len(options) == 2
    assert options[u'arg1'] == '12/34'

    args = "arg1='\\c\\Program Files (x86)' arg2='C:\\Program Files (x86)'"
    options = parse

# Generated at 2022-06-13 07:10:05.041099
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar baz=quux") == {"foo":"bar", "baz":"quux"}
    assert parse_kv("foo=bar baz=quux other") == {"foo":"bar", "baz":"quux", "_raw_params": "other"}
    assert parse_kv("foo=bar baz=quux") == {"foo":"bar", "baz":"quux"}
    assert parse_kv("foo=bar baz=quux") == {"foo":"bar", "baz":"quux"}
    assert parse_kv("foo=bar baz=quux") == {"foo":"bar", "baz":"quux"}
    assert parse_kv("foo=bar baz=quux") == {"foo":"bar", "baz":"quux"}

# Generated at 2022-06-13 07:10:11.601678
# Unit test for function split_args
def test_split_args():
    """ Static test for split_args method """
    # Test 1
    args = '''a=b
    b="c"
    c='d'
    d=\\
    e
    f='''
    result = ['a=b', 'b="c"', 'c=\'d\'', 'd=\\\n    e\n    f=', '']
    assert split_args(args) == result

    # Test 2
    args = '''a=b c="foo bar" d=eee e='f'
   g=\\
    h'''
    result = ['a=b', 'c="foo bar"', 'd=eee', "e='f'", '\n   g=\\\n    h']
    assert split_args(args) == result

    # Test 3

# Generated at 2022-06-13 07:10:24.584072
# Unit test for function parse_kv

# Generated at 2022-06-13 07:10:35.054632
# Unit test for function parse_kv

# Generated at 2022-06-13 07:10:43.092635
# Unit test for function parse_kv
def test_parse_kv():

    # Function does not accept None as an argument.
    assert parse_kv(None) == {}

    # A string with no = character or a string with one = character should
    # be returned as a one-item dict with a key of "_raw_params" and the
    # original function argument as a value.
    assert parse_kv("a string for testing") == {"_raw_params": "a string for testing"}
    assert parse_kv("a=string for testing") == {"_raw_params": "a=string for testing"}

    # Strings with multiple = characters should be turned into key/value pairs.
    # With check_raw being set to False, all key/value pairs should be made,
    # and no _raw_params key should be present.

# Generated at 2022-06-13 07:10:53.593068
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'foo=bar baz=qux color="blue"') == {
        u'foo': u'bar', u'baz': u'qux', u'color': u'blue'
    }
    assert parse_kv(u'foo="spam spam spam"') == {u'foo': u'spam spam spam'}
    assert parse_kv(u"foo='bar bar bar'") == {u'foo': u'bar bar bar'}
    assert parse_kv(u"foo=bar baz='qux qux'") == {u'foo': u'bar', u'baz': u'qux qux'}

# Generated at 2022-06-13 07:10:59.503035
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {'foo': u'bar'}
    assert parse_kv('foo=bar baz=foobar') == {'foo': u'bar', 'baz': u'foobar'}
    assert parse_kv('foo={{bar}}') == {'foo': u'{{bar}}'}
    assert parse_kv('foo="bar baz"') == {'foo': u'bar baz'}
    assert parse_kv("foo='bar baz'") == {'foo': u'bar baz'}
    assert parse_kv('foo="bar baz" bing=bazbang') == {'foo': u'bar baz', 'bing': u'bazbang'}

# Generated at 2022-06-13 07:11:07.921287
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=b c=d") == {u'a': u'b', u'c': u'd'}
    assert parse_kv("a=b c=d e") == {u'a': u'b', u'c': u'd', u'_raw_params': u'e'}
    assert parse_kv("a=b d=e b=c", check_raw=True) == {u'a': u'b', u'_raw_params': u'b=c', u'd': u'e'}
    assert parse_kv("a=b d=e 'b=c'", check_raw=True) == {u'a': u'b', u'_raw_params': u'"b=c"', u'd': u'e'}

# Generated at 2022-06-13 07:11:16.191508
# Unit test for function split_args

# Generated at 2022-06-13 07:11:42.637253
# Unit test for function parse_kv

# Generated at 2022-06-13 07:11:51.608522
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"key=value") == {u'key': u'value'}
    assert parse_kv(u"key=value key2=value2") == {u'key': u'value', u'key2': u'value2'}
    assert parse_kv(u"key=value key2='value2'") == {u'key': u'value', u'key2': u'value2'}
    assert parse_kv(u"key=\"value\"") == {u'key': u'value'}
    assert parse_kv(u"key=\"value\" key2=\"value2\"") == {u'key': u'value', u'key2': u'value2'}

# Generated at 2022-06-13 07:12:02.355923
# Unit test for function split_args

# Generated at 2022-06-13 07:12:06.436932
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('arg1=foo arg2=bar') == {u'arg2': u'bar', u'arg1': u'foo'}
    assert parse_kv('arg1="foo=bar" arg2=bar') == {u'arg2': u'bar', u'arg1': u'foo=bar'}
    assert parse_kv('arg1="foo=bar arg3=charlie" arg2=bar') == {u'arg2': u'bar', 'arg1': u'foo=bar arg3=charlie'}
    assert parse_kv('arg1="foo=bar arg3=charlie" arg2=bar') == {u'arg2': u'bar', 'arg1': u'foo=bar arg3=charlie'}

# Generated at 2022-06-13 07:12:15.707084
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}

    assert parse_kv('') == {}

    assert parse_kv('one=two three=four') == {'one': 'two', 'three': 'four'}

    assert parse_kv('one=two three=four', check_raw=True) == {'one': 'two', 'three': 'four', '_raw_params': ''}

    assert parse_kv('a=b c="d e"') == {'a': 'b', 'c': 'd e'}

    assert parse_kv('a=b c="d e"', check_raw=True) == {'a': 'b', 'c': 'd e', '_raw_params': ''}


# Generated at 2022-06-13 07:12:29.684357
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {'foo': 'bar'}
    assert parse_kv(' "foo=bar" ') == {'foo': 'bar'}
    assert parse_kv('foo="bar"') == {'foo': 'bar'}
    assert parse_kv('foo="bar biz"') == {'foo': 'bar biz'}
    assert parse_kv('foo="bar \\"biz\\" baz"') == {'foo': 'bar "biz" baz'}
    assert parse_kv('foo={bar}') == {'foo': '{bar}'}
    assert parse_kv('foo=bar  biz=biz') == {'foo': 'bar', 'biz': 'biz'}

# Generated at 2022-06-13 07:12:40.010829
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo\\" bar"') == ['a=b', 'c="foo\\" bar"']
    assert split_args('a=b c="foo\\\\" bar"') == ['a=b', 'c="foo\\\\" bar"']
    assert split_args(u'a=b c="foo\u1234"') == ['a=b', u'c="foo\u1234"']
    assert split_args(u'a=b c="foo\U00012345"') == ['a=b', u'c="foo\U00012345"']

# Generated at 2022-06-13 07:12:45.886482
# Unit test for function split_args
def test_split_args():
    # Test double quoted strings
    args = 'foo="{{ bar }}" baz=\'{{ qux }}\' bing={{ bong }}'
    print("test_split_args: ", args)
    params = split_args(args)
    print("test_split_args: ", params)
    assert params == ['foo="{{ bar }}"', "baz='{{ qux }}'", 'bing={{ bong }}']
    args = '{{ baz }}="{{ bar }}" baz=\'{{ qux }}\' bing={{ bong }}'
    print("test_split_args: ", args)
    params = split_args(args)
    print("test_split_args: ", params)

# Generated at 2022-06-13 07:12:54.743765
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv('one=1') == {'one': '1'}
    assert parse_kv('one=1 two=2') == {'one': '1', 'two': '2'}
    assert parse_kv('one=one two=two three=three') == {'one': 'one', 'two': 'two', 'three': 'three'}
    assert parse_kv('one=one two=two three=three') == {'one': 'one', 'two': 'two', 'three': 'three'}
    assert parse_kv('one="two two"') == {'one': 'two two'}
    assert parse_kv("one=two two") == {'one': 'two two'}

# Generated at 2022-06-13 07:13:04.104883
# Unit test for function parse_kv
def test_parse_kv():
    cmd = "foo=bar baz='hello world'"
    options = parse_kv(cmd)
    assert options == dict(foo='bar', baz='hello world')

    cmd = "foo=bar\nbaz='hello world'\n"
    options = parse_kv(cmd)
    assert options == dict(foo='bar', baz='hello world')

    cmd = '''foo=bar
    baz='hello world'
    '''
    options = parse_kv(cmd)
    assert options == dict(foo='bar', baz='hello world')

    cmd = "foo=bar baz='hello world'"
    options = parse_kv(cmd, check_raw=True)

# Generated at 2022-06-13 07:14:27.667786
# Unit test for function split_args
def test_split_args():
    # test line continuation
    result = split_args(r'''module: name=testflow register: flow_result - name: run task on hosts
  debug: msg="{{item}}"
  with_items: "{{flow_result.results}}" ''')
    assert result == ['module:', 'name=testflow', 'register:', 'flow_result', '-', 'name:', 'run task on hosts', 'debug:', 'msg="{{item}}"', 'with_items:', '"{{flow_result.results}}"']

    # test nested quotes
    result2 = split_args(r'''name: test my command
  shell: /bin/foo "with spaces" 'and args'" ''')

# Generated at 2022-06-13 07:14:38.336647
# Unit test for function split_args
def test_split_args():
    # this test includes a set of quotes, jinja, and newlines
    # all at the same time
    args = '''"testing 1 2 3 4 5 6 7 8 9 10 11 12" {% if testing %} foo bar ''' + \
        '''baz {{ test }} "testing more" \n more \n testing \n {% endif %} '''
    params = split_args(args)
    assert params == [' "testing 1 2 3 4 5 6 7 8 9 10 11 12" ', ' {% if testing %} foo bar baz {{ test }} "testing more" ', ' more ', ' testing ', ' {% endif %} ']

    # testing quotes inside a jinja2 block, with spaces

# Generated at 2022-06-13 07:14:45.892290
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:55.780289
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.module_utils.common._collections_compat import Sequence
    assert parse_kv(
        'a=b,c=d,e=f', check_raw=True) == dict(a='b', c='d', e='f')
    assert parse_kv(
        'a=b,c=d,e=f,g=h', check_raw=True) == dict(a='b', c='d', e='f', g='h')
    assert parse_kv(
        'a=b,c=d,e=f,g=h') == dict(a='b', c='d', e='f', g='h')
    assert parse_kv(
        'a=b c=d') == dict(a='b', c='d')

# Generated at 2022-06-13 07:15:07.024187
# Unit test for function parse_kv
def test_parse_kv():
    in_1 = "foo=bar baz=qux"
    out_1 = {
        u'foo': u'bar',
        u'baz': u'qux'
    }
    assert parse_kv(in_1) == out_1
    in_2 = "foo=bar=baz"
    out_2 = {
        u'foo': u'bar=baz'
    }
    assert parse_kv(in_2) == out_2
    in_3 = "foo=bar=baz qux"
    out_3 = {
        u'foo': u'bar=baz',
        u'_raw_params': u'qux'
    }
    assert parse_kv(in_3, check_raw=True) == out_3

# Generated at 2022-06-13 07:15:15.228874
# Unit test for function split_args
def test_split_args():
    assert split_args(u"foo bar baz") == [u"foo", u"bar", u"baz"]
    assert split_args(u"foo bar baz\n") == [u"foo bar baz\n"]
    assert split_args(u"foo\nbar baz") == [u"foo\n", u"bar", u"baz"]
    assert split_args(u'foo bar "baz bat"') == [u'foo', u'bar', u'"baz bat"']
    assert split_args(u"foo bar=bat") == [u"foo", u"bar=bat"]
    assert split_args(u'foo bar=\'bat\'') == [u'foo', u"bar='bat'"]

# Generated at 2022-06-13 07:15:26.093160
# Unit test for function split_args

# Generated at 2022-06-13 07:15:33.134901
# Unit test for function parse_kv
def test_parse_kv():
    from nose.tools import assert_equal
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    x = parse_kv('x=3 y="foo bar" z="foo \"bar\"" n=null v=')
    assert_equal(x, {u'x': u'3', u'y': u'foo bar', u'z': u'foo "bar"', u'n': None, u'v': None})

    x = parse_kv('x=3 y="foo bar" z="foo \"bar\"" n=null v=', check_raw=True)

# Generated at 2022-06-13 07:15:41.721141
# Unit test for function split_args
def test_split_args():
    import nose
    import sys
    from ansible.module_utils.basic import jsonify

    results = []


# Generated at 2022-06-13 07:15:51.227836
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"foo=bar bar=baz") == {
        u'foo': u'bar',
        u'bar': u'baz',
    }
    assert parse_kv(u"foo=bar bar=baz", check_raw=True) == {
        u'foo': u'bar',
        u'bar': u'baz',
        u'_raw_params': u'bar=baz',
    }
    assert parse_kv(u"foo=bar bar=baz bar='baz bax'", check_raw=True) == {
        u'foo': u'bar',
        u'bar': u'baz bax',
        u'_raw_params': u'bar="baz bax"',
    }

# Generated at 2022-06-13 07:16:34.659174
# Unit test for function split_args
def test_split_args():
    assert [
        'a=1',
        'b=2',
        ] == split_args("a=1 b=2")
    assert [
        'a=1',
        'b=2',
        ] == split_args("a=1 \nb=2")

    # unterminated quotes
    try:
        assert not split_args("a=1 b='2")
        assert False, "Expected failure"
    except AnsibleParserError:
        pass

    assert [
        'a=1',
        'b="2',
        ] == split_args("a=1 b='2'")
    assert [
        'a=1',
        'b="2',
        ] == split_args("a=1 b=\"2\"")


# Generated at 2022-06-13 07:16:48.407296
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {'foo':'bar'}
    assert parse_kv('foo=bar arg1 arg2') == {'foo':'bar', '_raw_params':'arg1 arg2'}
    assert parse_kv('foo=bar arg1 arg2', check_raw=False) == {'foo':'bar'}

# Generated at 2022-06-13 07:16:56.992146
# Unit test for function parse_kv
def test_parse_kv():

    def check_results(input, results):
        assert(parse_kv(input) == results)

    check_results("", {})
    check_results("foo=stuff", {u'foo': u'stuff'})
    check_results("foo='stuff'", {u'foo': u'stuff'})
    check_results("foo=\"stuff\"", {u'foo': u'stuff'})
    check_results("foo=stuff v=bar", {u'foo': u'stuff', u'v': u'bar'})
    check_results("foo='stuff v=bar'", {u'foo': u'stuff v=bar'})
    check_results("foo=\"stuff v=bar\"", {u'foo': u'stuff v=bar'})