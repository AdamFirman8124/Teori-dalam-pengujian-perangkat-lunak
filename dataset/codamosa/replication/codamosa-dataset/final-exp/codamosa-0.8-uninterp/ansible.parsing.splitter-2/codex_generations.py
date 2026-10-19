

# Generated at 2022-06-13 07:07:44.733159
# Unit test for function parse_kv

# Generated at 2022-06-13 07:07:55.148959
# Unit test for function split_args

# Generated at 2022-06-13 07:08:05.347968
# Unit test for function split_args
def test_split_args():
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo "bar \\"baz\\""') == ['foo', '"bar \\"baz\\""']
    assert split_args('foo "bar baz" test') == ['foo', '"bar baz"', 'test']
    assert split_args('{{ foo }} "bar baz" test') == ['{{ foo }}', '"bar baz"', 'test']
    assert split_args('{{ foo }} "bar baz" test') == ['{{ foo }}', '"bar baz"', 'test']
    assert split_args('{% foo %} "bar baz" test') == ['{% foo %}', '"bar baz"', 'test']

# Generated at 2022-06-13 07:08:13.173373
# Unit test for function parse_kv

# Generated at 2022-06-13 07:08:19.731973
# Unit test for function split_args
def test_split_args():
    # Simple tests
    assert split_args("a=1 b=2") == [u"a=1", u"b=2"]
    assert split_args("a=1 b=2 c=3") == [u"a=1", u"b=2", u"c=3"]
    assert split_args("a='1 2' b=2") == [u"a='1 2'", u"b=2"]
    assert split_args("a='1 2' b=\"3 4\"") == [u"a='1 2'", u"b=\"3 4\""]
    assert split_args("a='1 2' b=\"3 '4'\"") == [u"a='1 2'", u"b=\"3 '4'\""]

# Generated at 2022-06-13 07:08:27.685106
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"A=1 B=2", True) == {u'A': u'1', u'B': u'2', u'_raw_params': u''}
    assert parse_kv(u"A='1' B=\"2\"", True) == {u'A': u'1', u'B': u'2', u'_raw_params': u''}
    assert parse_kv(u"A=1 B=\"2\" C=\'3\'", True) == {u'A': u'1', u'B': u'2', u'C': u'3', u'_raw_params': u''}

# Generated at 2022-06-13 07:08:30.971268
# Unit test for function split_args
def test_split_args():
    args = '"one two three" four five'
    result = split_args(args)
    assert result == ['"one two three"', 'four', 'five']

# Generated at 2022-06-13 07:08:45.871512
# Unit test for function split_args
def test_split_args():
    import pytest
    # Test basic quoting and escaping
    cmd = u"cowsay moo 'don\\'t do it' \"don't do it\" don\\=t"
    split = split_args(cmd)
    assert split == [u'cowsay', u'moo', u"don't do it", u"don't do it", u'don\\=t']

    # Test that things inside braces stay together
    cmd = u'rabbitmqctl add_vhost {{ rabbitmq_vhost_name }}'
    split = split_args(cmd)
    assert split == [u'rabbitmqctl', u'add_vhost', u'{{', u'rabbitmq_vhost_name', u'}}']

    # Test that things inside quotes stay together

# Generated at 2022-06-13 07:08:51.775171
# Unit test for function parse_kv
def test_parse_kv():
    test_kv_string_1 = "key1=value1 key2=value2"
    test_kv_string_2 = "key1=value1 'key2=value2'"
    test_kv_string_3 = "key1=value1 'key2=value2' 'key2=value2'"
    test_kv_string_4 = "key1=value1 key3=value3 'key2=value2' key4=value4"
    test_kv_string_5 = "key1=value1 key2=value2 'key2=value2'"
    test_kv_string_6 = "key1=value1 key2=value2 \"key2=value2\""
    test_kv_string_7 = "key1=value1 key2=val=ue2"
    test

# Generated at 2022-06-13 07:09:02.814747
# Unit test for function split_args
def test_split_args():
    import argparse

    class Test():
        def __init(self):
            self.a=None
            self.b=None
            self.c=None
            self.d=None
            self.e=None
            self.f=None
            self.g=None
            self.h=None
            self.i=None
            self.j=None

    res=Test()
    parser=argparse.ArgumentParser()
    parser.add_argument('-a', dest='a')
    parser.add_argument('-b', dest='b')
    parser.add_argument('-c', dest='c')
    parser.add_argument('-d', dest='d')
    parser.add_argument('-e', dest='e')
    parser.add_argument('-f', dest='f')
    parser.add

# Generated at 2022-06-13 07:09:21.600431
# Unit test for function split_args

# Generated at 2022-06-13 07:09:23.376446
# Unit test for function split_args
def test_split_args():
    # simply returns the same string when given a string with no characters
    # that are significant to splitting args
    assert split_args('a b c') == ['a', 'b', 'c']



# Generated at 2022-06-13 07:09:36.788048
# Unit test for function split_args
def test_split_args():

    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']

    # The extra spaces on `foo` are important.
    assert split_args('foo bar baz') != [' foo', 'bar', 'baz']

    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo "bar baz"') != ['foo', '"bar', 'baz"']

    assert split_args('foo "bar baz') == ['foo', '"bar', 'baz']
    assert split_args('foo "bar baz') != ['foo', '"bar baz']

    assert split_args('foo bar "baz') == ['foo', 'bar', '"baz']

# Generated at 2022-06-13 07:09:48.737035
# Unit test for function split_args
def test_split_args():
    doc = """
    - name: test split args
      command: cat {{ item }}
      with_items:
        - fileA
        - 'file \"B'
        - "file 'C"
        - file '"D'
        - file \"'E\"
        - '"fileF"'
        - "'fileG"
        - file 'H'
    """

    args = parse_kv('a=b c="foo bar" d=\'bar foo\' e="foo \'bar\' baz" f=\'bar "baz" foo\'', check_raw=False)
    assert args == dict(a='b', c='foo bar', d='bar foo',
                        e="foo \'bar\' baz", f='bar "baz" foo')

    params = split_args(doc)
    # Verify split_args returns the correct value

# Generated at 2022-06-13 07:09:58.180404
# Unit test for function split_args
def test_split_args():

    # test that a simple command is split on whitespace
    assert split_args('test "a b c"') == ['test', '"a b c"']

    # test some more complex commands
    assert split_args('test "a b c" {{ d }}') == ['test', '"a b c"', '{{', 'd', '}}']
    assert split_args('test "a b c" {{ d }} e') == ['test', '"a b c"', '{{', 'd', '}}', 'e']
    assert split_args('test "a b c" {{ d }} e {{ f }}') == ['test', '"a b c"', '{{', 'd', '}}', 'e', '{{', 'f', '}}']

# Generated at 2022-06-13 07:09:58.576510
# Unit test for function parse_kv
def test_parse_kv():
    pass



# Generated at 2022-06-13 07:10:08.386589
# Unit test for function parse_kv
def test_parse_kv():
    assert type(parse_kv('a=b c=d')) == dict
    assert parse_kv('a=b c=d') == dict(a='b',c='d')
    assert parse_kv('a=b "c=d e"' ) == dict(a='b', _raw_params='"c=d e"')
    assert parse_kv('a="b=c d"') == dict(a='b=c d')
    assert parse_kv('a="b=\\"c d"') == dict(a='b="c d')
    assert parse_kv('a=b=c') == dict(a='b=c')

# Generated at 2022-06-13 07:10:14.293271
# Unit test for function parse_kv
def test_parse_kv():
    inp = """a='b c' d='"e' f=g 'h'=i"""
    assert parse_kv(inp) == {u'a': u'b c', u'd': u'"e', u'f': u'g', u'h': u'i'}


# Generated at 2022-06-13 07:10:24.268034
# Unit test for function split_args
def test_split_args():
    # Note: the tests here only test the "join_args" function
    # against the "split_args" function. The actual parsing logic
    # is tested elsewhere.
    args = "foo=bar baz=\"{{ foo }}\""
    assert join_args(split_args(args)) == args

    args = "foo=bar"
    assert join_args(split_args(args)) == args

    args = "foo='bar'"
    assert join_args(split_args(args)) == args

    args = "foo=\"bar\""
    assert join_args(split_args(args)) == args

    args = "foo=bar baz=\"{{ foo }}\""
    assert join_args(split_args(args)) == args

    args = "foo=bar baz=\"{{ foo }}\""

# Generated at 2022-06-13 07:10:34.898601
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('x=1 y=2') == dict(x='1', y='2')
    assert parse_kv('wibble=1 x=2') == dict(wibble='1', x='2')
    assert parse_kv('wibble=1 x=2', check_raw=True) == dict(wibble='1', x='2', _raw_params=u'wibble=1 x=2')
    assert parse_kv('x=1 y=2', check_raw=True) == dict(x='1', y='2', _raw_params=u'x=1 y=2')


# Generated at 2022-06-13 07:10:52.004484
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a=b c=d') == {u'a': u'b', u'c': u'd'}
    assert parse_kv(u'a=b c="d e"') == {u'a': u'b', u'c': u'd e'}
    assert parse_kv(u'a=b c="d e" f="g h"') == {u'a': u'b', u'c': u'd e', u'f': u'g h'}
    assert parse_kv("a='b c'") == {u'a': u'b c'}
    assert parse

# Generated at 2022-06-13 07:10:57.878304
# Unit test for function split_args

# Generated at 2022-06-13 07:11:07.210625
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv('a=b c=d'))
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    print(parse_kv('a=b c="d=e f=g"'))
    assert parse_kv('a=b c="d=e f=g"') == {'a': 'b', 'c': 'd=e f=g'}
    print(parse_kv('a=b c=\'d=e f=g\''))
    assert parse_kv('a=b c=\'d=e f=g\'') == {'a': 'b', 'c': 'd=e f=g'}

# Generated at 2022-06-13 07:11:12.781870
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Function to unit test function parse_kv.
    '''

    # We will use dictionary comprehension to compare expected and actual results.

    # Set of parameters that do not require quotes


# Generated at 2022-06-13 07:11:22.844593
# Unit test for function parse_kv
def test_parse_kv():

    kv_strings = [
        # String with quoted values
        'username="foo" password="bar"',
        # String with unquoted values
        'username=foo password=bar',
        # String with escaped values
        'username="foo\"bar" password="bar\\"foo"',
        # String with escaped escapes
        'username="foo\\\\bar" password="bar\\\\foo"',
    ]

    for kv_string in kv_strings:
        kv = parse_kv(kv_string)
        assert len(kv) == 2
        assert kv['username'] == 'foo"bar'
        assert kv['password'] == 'bar\\"foo'

    # String with a free form parameter
    kv = parse_kv('username="foo" password="bar" "something else"')

# Generated at 2022-06-13 07:11:27.126717
# Unit test for function parse_kv
def test_parse_kv():
    args = to_text("foo=bar bar='baz baz' boo=1 baz=\"'\"")
    assert parse_kv(args) == {u'foo': u'bar', u'bar': u'baz baz', u'boo': u'1', u'baz': u"'"}



# Generated at 2022-06-13 07:11:35.738631
# Unit test for function split_args

# Generated at 2022-06-13 07:11:39.425337
# Unit test for function parse_kv
def test_parse_kv():
    input_str = 'a=1 b="2" c=3 d=4'
    assert parse_kv(input_str) == {"a": "1", "b": "2", "c": "3", "d": "4"}



# Generated at 2022-06-13 07:11:49.818107
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar" "foo bar baz"') == ['a=b', 'c="foo bar"', '"foo bar baz"']
    assert split_args('a=b c="foo bar" "foo bar baz"\\') == ['a=b', 'c="foo bar"', '"foo bar baz"\\']
    assert split_args('a=b c="foo bar" "foo bar baz"\\\nx=y') == ['a=b', 'c="foo bar"', '"foo bar baz"\\\nx=y']

# Generated at 2022-06-13 07:12:01.054161
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar", True) == {'foo': 'bar', '_raw_params': 'foo=bar'}
    assert parse_kv("foo='bar'", True) == {'foo': 'bar', '_raw_params': "foo='bar'"}
    assert parse_kv("foo=", True) == {'foo': '', '_raw_params': 'foo='}
    assert parse_kv("", True) == {'_raw_params': ''}
    assert parse_kv("foo=bar") == {'foo': 'bar'}
    assert parse_kv("foo='bar'") == {'foo': 'bar'}
    assert parse_kv("foo=bar'la'la") == {'foo': "bar'la'la"}

# Generated at 2022-06-13 07:12:16.377212
# Unit test for function split_args
def test_split_args():
    assert(split_args('foo "bar baz"') == ['foo', '"bar baz"'])
    assert(split_args('foo "bar \\"baz"') == ['foo', '"bar \\"baz'])
    assert(split_args('foo "bar \\" baz"') == ['foo', '"bar \\" baz"'])
    assert(split_args('foo "bar \\"baz\\""') == ['foo', '"bar \\"baz\\""'])
    assert(split_args('foo "bar \\\\"baz"') == ['foo', '"bar \\\\"baz'])
    assert(split_args('foo "bar baz" \\') == ['foo', '"bar baz" \\'])

# Generated at 2022-06-13 07:12:30.299475
# Unit test for function parse_kv
def test_parse_kv():
    # from ansible.module_utils.basic import AnsibleModule
    # module = AnsibleModule(argument_spec={})
    class AnsibleModule:
        def __init__(self, argument_spec):
            pass
    module=AnsibleModule(argument_spec={})
    module.exit_json = lambda x: x

# Generated at 2022-06-13 07:12:40.434491
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode

# Generated at 2022-06-13 07:12:50.722478
# Unit test for function split_args
def test_split_args():
    assert split_args(u'creates=hello world') == [u'creates=hello', u'world']
    assert split_args(u'creates=hello world;python -m tests.test_utils_module') == [u'creates=hello', u'world', u';python -m tests.test_utils_module']
    assert split_args(u'creates=hello world;exec "python -m tests.test_utils_module"') == [u'creates=hello', u'world', u';exec "python -m tests.test_utils_module"']

# Generated at 2022-06-13 07:13:00.744578
# Unit test for function split_args
def test_split_args():
    assert split_args(r'echo hello world') == ['echo', 'hello', 'world']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args(r'a=b c="foo\\ bar"') == ['a=b', 'c="foo\\ bar"']
    assert split_args(r'''a=b c='foo bar' d="foo bar"''') == ['a=b', "c='foo bar'", 'd="foo bar"']
    assert split_args(r'''a=b c="foo bar" d='foo bar' e="foo bar"''') == ['a=b', 'c="foo bar"', "d='foo bar'", 'e="foo bar"']

# Generated at 2022-06-13 07:13:07.514052
# Unit test for function parse_kv
def test_parse_kv():

    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a=b c=d') == {u'a': u'b', u'c': u'd'}
    assert parse_kv('c=d a=b') == {u'a': u'b', u'c': u'd'}
    assert parse_kv('a=b c=d e=f') == {u'a': u'b', u'c': u'd', u'e': u'f'}
    assert parse_kv('a="b c"') == {u'a': u'b c'}
    assert parse_kv('a="b=c"') == {u'a': u'b=c'}

# Generated at 2022-06-13 07:13:18.904385
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foobar=1 test=2 test2=3') == {u'foobar': u'1', u'test': u'2', u'test2': u'3'}
    assert parse_kv('test="some_test" test2=3') == {u'test': u'some_test', u'test2': u'3'}
    assert parse_kv('testing foobar="some_test" test2=3') == {u'_raw_params': u'testing foobar="some_test" test2=3'}
    assert parse_kv('testing test_1="some test" test2=3') == {u'_raw_params': u'testing test_1="some test" test2=3'}

# Generated at 2022-06-13 07:13:26.070471
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:35.928964
# Unit test for function split_args

# Generated at 2022-06-13 07:13:41.333129
# Unit test for function split_args
def test_split_args():
    import sys
    from ansible.module_utils.basic import AnsibleModule

    sys_version_info = sys.version_info[:2]
    # Python 2.6 does not have assertRaisesRegexp
    if sys_version_info == (2, 6):
        from ansible.module_utils.basic import AnsibleModule
        from ansible.utils.unicode import to_bytes
        from ansible.errors import AnsibleParserError
        # for Python 3 compatibility, we're going to use a lambda
        # to wrap our call, as then we can use the six
        # wraps decorator to use the same name

# Generated at 2022-06-13 07:13:54.466566
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"foo=bar baz=qux") == \
        {u"foo": u"bar", u"baz": u"qux"}
    assert parse_kv(u'foo=bar "baz=qux"') == \
        {u"foo": u"bar", u"baz=qux": None}
    assert parse_kv(u"foo=bar baz=qux _raw_params='a b'") == \
        {u"foo": u"bar", u"baz": u"qux", u"_raw_params": u"a b"}

# Generated at 2022-06-13 07:14:08.465914
# Unit test for function split_args
def test_split_args():
    '''
    Verify that split_args and join_args behave properly.
    '''
    from tempfile import NamedTemporaryFile
    from copy import copy
    import json

    test_file = NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 07:14:14.920502
# Unit test for function split_args
def test_split_args():
    print ("Testing split_args()")
    # function test_quoting(self):
    # simple case, nothing special
    sample = '''foo=bar key="with space"'''
    result = split_args(sample)
    assert result == ['foo=bar', 'key="with space"'], "split_args failure:" + repr(result)

    # make sure spaces are preserved
    sample = '''foo=bar   key="with space"'''
    result = split_args(sample)
    assert result == ['foo=bar', '  key="with space"'], "split_args failure:" + repr(result)

    # make sure quotes are preserved
    sample = '''foo=bar   key="with space"'''
    result = split_args(sample)

# Generated at 2022-06-13 07:14:20.562234
# Unit test for function parse_kv
def test_parse_kv():
    # Normal runs
    d1 = parse_kv("key1=value1 key2=value2")
    assert d1['key1'] == 'value1'
    assert d1['key2'] == 'value2'
    d2 = parse_kv("key1=value1 key2=value2 key3=value3")
    assert d2['key1'] == 'value1'
    assert d2['key2'] == 'value2'
    assert d2['key3'] == 'value3'

    # raw runs
    # when check_raw is set to True, args are not set as a key=value pair;
    # instead, they are added to the special_args list

# Generated at 2022-06-13 07:14:24.384492
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('k1=v1 k2=v2') == {'k1': 'v1', 'k2': 'v2'}



# Generated at 2022-06-13 07:14:30.603724
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=b c="d e" f="g=h"') == {u'a': 'b', u'c': 'd e', u'f': 'g=h'}
    assert parse_kv(u'a=1,2,3') == {u'a': '1,2,3'}
    assert parse_kv(u'a=1,2,3', check_raw=True) == {u'a': '1,2,3', u'_raw_params': 'a=1,2,3'}
    assert parse_kv(u'a=1,2=3') == {u'a': '1,2=3'}

# Generated at 2022-06-13 07:14:40.526518
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:47.644616
# Unit test for function parse_kv
def test_parse_kv():
    test_string = '''
        key1=value1\=value2 key2=value3 "value4=value5" key3="key4=value6" key5
    '''
    assert parse_kv(test_string) == {'key1': 'value1=value2', 'key2': 'value3', 'key5': None, 'key3': 'key4=value6', '_raw_params': 'value4=value5'}
    assert parse_kv(test_string, check_raw=True) == {'key1': 'value1=value2', 'key2': 'value3', 'key5': None, 'key3': 'key4=value6', '_raw_params': 'value4=value5'}

# Generated at 2022-06-13 07:14:56.478931
# Unit test for function split_args
def test_split_args():
    def run_test(args, expected):
        args_split = split_args(args)
        args_joined = join_args(args_split)
        assert args == args_joined, (u"Parse/join error for {0} : {1}".format(args, args_joined))
        assert args_split == expected

    run_test(u'echo "hello"', [u'echo', u'"hello"'])
    run_test(u'echo "hello world"', [u'echo', u'"hello world"'])
    run_test(u'echo "hello\nworld"', [u'echo', u'"hello\nworld"'])
    run_test(u'echo "hello\\"world"', [u'echo', u'"hello"world"'])

# Generated at 2022-06-13 07:15:02.339546
# Unit test for function parse_kv
def test_parse_kv():
    args = 'var1=simple var2=value with spaces var3="a value" "var4=unquoted"'
    assert parse_kv(args) == {
        u'var1': u'simple',
        u'var2': u'value with spaces',
        u'var3': u'a value',
        u'_raw_params': u'var4=unquoted'
    }


# http://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python

# Generated at 2022-06-13 07:15:15.911785
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a="b"') == {u'a': u'"b"'}
    assert parse_kv('a=b c=d') == {u'a': u'b', u'c': u'd'}
    assert parse_kv('a="b b" c=d') == {u'a': u'"b b"', u'c': u'd'}
    assert parse_kv('a=b=c') == {u'a': u'b=c'}
    assert parse_kv('a=b\\=c') == {u'a': u'b=c'}
    assert parse

# Generated at 2022-06-13 07:15:26.773984
# Unit test for function parse_kv

# Generated at 2022-06-13 07:15:36.271402
# Unit test for function parse_kv
def test_parse_kv():
    import json

    data_json = '''
    {
    "arg1" : "val1",
    "arg2" : "val2",
    "arg3" : "val3",
    "_raw_params" : "arg4=val4 arg5=val5",
    "arg6" : "val6"
    }
    '''
    data_dict = json.loads(data_json)
    ansible_module_cli_args = "arg1=val1 arg2=val2 arg3=val3 arg4=val4 arg5=val5 arg6=val6"
    assert parse_kv(ansible_module_cli_args) == data_dict



# Generated at 2022-06-13 07:15:43.728041
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"a=b") == {u"a": u"b"}
    assert parse_kv(u"a=\"b\"") == {u"a": u"\"b\""}
    assert parse_kv(u'a=b\"') == {u'a': u'b\"'}
    assert parse_kv(u'a=b\\"') == {u'a': u'b\"'}
    assert parse_kv(u"a=b c") == {u'a': u'b', u'_raw_params': u'c'}
    assert parse_kv(u"a=b\\\\\\\" c") == {u'a': u'b\\\"', u'_raw_params': u'c'}

# Generated at 2022-06-13 07:15:52.531083
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a='b'") == {"a": "b"}
    assert parse_kv("a='b', c, d='e'") == {"a": "b", "c": None, "d": "e"}
    assert parse_kv("a='b', c, d='e'") == {"a": "b", "c": None, "d": "e"}
    assert parse_kv("a='b' c d='e'") == {"a": "b", "c": None, "d": "e"}
    assert parse_kv("a='b', c=d='e'") == {"a": "b", "c": "d=e"}
    assert parse_kv("a='b', c='d=e'") == {"a": "b", "c": "d=e"}
   

# Generated at 2022-06-13 07:16:05.308311
# Unit test for function parse_kv
def test_parse_kv():
    # Test 1
    options=parse_kv("--long-option='arg with spaces' --another-option=foo\\=bar")
    assert options == {'long-option': 'arg with spaces', 'another-option': 'foo=bar'}

    # Test 2
    options=parse_kv("--long-option='arg with spaces' --another-option=foo\\=bar -i filename")
    assert options == {'long-option': 'arg with spaces', 'another-option': 'foo=bar'}

    # Test 3
    options=parse_kv("--long-option='arg with spaces' --another-option=foo\\=bar --non-option-arg -i filename")

# Generated at 2022-06-13 07:16:14.282135
# Unit test for function split_args

# Generated at 2022-06-13 07:16:23.567417
# Unit test for function split_args

# Generated at 2022-06-13 07:16:30.779483
# Unit test for function split_args

# Generated at 2022-06-13 07:16:38.649790
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:54.751974
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Convert a string of key/value items to a dict. If any free-form params
    are found and the check_raw option is set to True, they will be added
    to a new parameter called '_raw_params'. If check_raw is not enabled,
    they will simply be ignored.
    '''

    options = {}
    args = "ssh -o IdentityFile=/tmp/foo"
    if args is not None:
        try:
            vargs = split_args(args)
        except IndexError as e:
            raise AnsibleParserError("Unable to parse argument string", orig_exc=e)
        except ValueError as ve:
            if 'no closing quotation' in str(ve).lower():
                raise AnsibleParserError("error parsing argument string, try quoting the entire line.", orig_exc=ve)

# Generated at 2022-06-13 07:17:06.478458
# Unit test for function parse_kv
def test_parse_kv():
    for args in ["", "=", "=a", "a", "a=", "a=b"]:
        ret = parse_kv(args)
        assert ret == {}

    for args in ["arg", "arg arg", "arg arg arg"]:
        ret = parse_kv(args, check_raw=True)
        assert ret == {"_raw_params": args}

    for args in ["a=b", "a=b c=d", "a=b c=d e=f"]:
        ret = parse_kv(args)
        assert len(ret) == 1
        for k, v in ret.items():
            assert k in args
            assert v in args
