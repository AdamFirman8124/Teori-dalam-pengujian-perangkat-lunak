

# Generated at 2022-06-13 07:07:34.854610
# Unit test for function split_args
def test_split_args():
    ARGS = [
        "a='b c'",
        "a='b c d'",
        "a=b c=d e=f",
        "a=b c=d e='f g'",
        "a=b c=d e='f g' h='i'",
    ]
    for arg in ARGS:
        args = split_args(arg)
        result = join_args(args)
        assert arg == result, "test_split_args() failed for input string: '%s' ,it gives %s" %(arg, result)


if __name__ == "__main__":
    test_split_args()

# Generated at 2022-06-13 07:07:42.480298
# Unit test for function parse_kv
def test_parse_kv():
    # q&d version
    try:
        import ast
    except:
        return


# Generated at 2022-06-13 07:07:54.438056
# Unit test for function split_args

# Generated at 2022-06-13 07:08:05.298163
# Unit test for function split_args
def test_split_args():
    args = "a=b c=\"foo bar\""
    test_result = split_args(args)
    assert test_result == [u'a=b', u'c="foo bar"']
    args = "a b=\"foo bar\""
    test_result = split_args(args)
    assert test_result == [u'a b="foo bar"']
    args = "a=b c='foo bar'"
    test_result = split_args(args)
    assert test_result == [u'a=b', u"c='foo bar'"]
    args = "a=\"foo bar\" b=\"foo baz\" c={{ foo }} d={{ bar }} e={{ baz }}"
    test_result = split_args(args)

# Generated at 2022-06-13 07:08:16.498327
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for function parse_kv
    '''
    import os
    import stat
    import tempfile
    import shutil

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary playbook
    fd, path = tempfile.mkstemp()

    # Create the playbook
    with os.fdopen(fd, 'w') as f:
        f.write('''
    - name: test parse_kv
      shell: cat /tmp/foo
      args:
        creates: /tmp/bar
    ''')

    # Change permissions of the playbook to ensure the test works
    # on systems where users have a umask that creates non-user-writable files

# Generated at 2022-06-13 07:08:23.045043
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args(' a=b') == ['a=b']
    assert split_args(' a=b ') == ['a=b']
    assert split_args(' a=b c=d') == ['a=b', 'c=d']
    assert split_args(' a=b c=d ') == ['a=b', 'c=d']
    assert split_args(' "a=b c=d"') == ['a=b c=d']
    assert split_args(" 'a=b c=d'") == ['a=b c=d']
    assert split_args(' a=b\\ c=d') == ['a=b c=d']
    assert split_args(' a=b\\\nc=d') == ['a=b c=d']
    assert split

# Generated at 2022-06-13 07:08:34.596442
# Unit test for function parse_kv
def test_parse_kv():
    # Test the option parsing with raw_params
    assert parse_kv('creates=/tmp/foobar removes=/tmp/baz') == dict(creates='/tmp/foobar', removes='/tmp/baz')
    assert parse_kv('arg1 arg2 arg3') == dict(_raw_params='arg1 arg2 arg3')

    # Test argument indexing and quoting
    assert parse_kv('''"arg1 arg2 arg3"''') == dict(_raw_params='arg1 arg2 arg3')
    assert parse_kv('''"arg1 arg2 arg3" x=2''') == dict(_raw_params='arg1 arg2 arg3', x='2')

# Generated at 2022-06-13 07:08:48.463218
# Unit test for function split_args
def test_split_args():
    """
    test case is the string that we'll parse,
    result is the expected list of tokens
    """

# Generated at 2022-06-13 07:09:00.160658
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('  ') == []
    assert split_args('\t') == []
    assert split_args(' \t') == []
    assert split_args('foo') == ['foo']
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo \t bar \t baz \t') == ['foo', 'bar', 'baz']
    assert split_args('foo\nbar\nbaz\n') == ['foo\n', 'bar\n', 'baz\n']
    assert split_args('foo\nbar\nbaz') == ['foo\n', 'bar\n', 'baz']

# Generated at 2022-06-13 07:09:10.200190
# Unit test for function parse_kv
def test_parse_kv():
    data = '''foo='bar baz' baz="bar'd" name=value "raw string" "'''"other raw string"'''"'''
    assert parse_kv(data, check_raw=True) == {'foo': 'bar baz', 'baz': "bar'd", 'name': 'value', '_raw_params': ["raw string", '""other raw string""']}
    # Removing check_raw param, verify that raw strings are ignored
    assert parse_kv(data) == {'foo': 'bar baz', 'baz': "bar'd", 'name': 'value'}

    data = 'foo=bar=baz'
    assert parse_kv(data, check_raw=True) == {'foo': 'bar=baz', '_raw_params': []}

# Generated at 2022-06-13 07:09:36.868734
# Unit test for function split_args

# Generated at 2022-06-13 07:09:39.628207
# Unit test for function split_args
def test_split_args():
    # Insert tests here
    # This is just a stub so that the directory can be packaged
    # with the test module.
    return False


# Generated at 2022-06-13 07:09:50.066629
# Unit test for function parse_kv
def test_parse_kv():
    assert str(parse_kv('a=1')) == "{u'a': u'1'}"
    assert str(parse_kv('a=1 b=2')) == "{u'a': u'1', u'b': u'2'}"
    assert str(parse_kv('a=1\tb=2')) == "{u'a': u'1', u'b': u'2'}"
    assert str(parse_kv('a=1 b=2 c=3')) == "{u'a': u'1', u'b': u'2', u'c': u'3'}"
    assert str(parse_kv('a=1 b="2 b"')) == "{u'a': u'1', u'b': u'2 b'}"

# Generated at 2022-06-13 07:09:58.544397
# Unit test for function split_args

# Generated at 2022-06-13 07:10:08.353816
# Unit test for function split_args
def test_split_args():
    # generate a list of random strings
    # to supply to the function
    import random
    import string
    def rndstr(string_length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))

    # each test run uses 3-5 random strings
    # and some random numbers of them
    # will be added to one or more
    # random jinja2 blocks
    for i in range(500):
        params = [rndstr(6) for x in range(random.randint(3, 5))]

        # Create a few random jinja2 blocks
        num_blocks = random.randint(1, 3)
        print_blocks = []
        block_blocks = []

# Generated at 2022-06-13 07:10:16.465627
# Unit test for function split_args
def test_split_args():
    input_v = """a=b c="foo bar" 'd e' f="{{x}}" g={{y}} 'h i' {% j %} k={{ z }}"""
    output_v = ['a=b', 'c="foo bar"', '\'d e\'', 'f="{{x}}"', 'g={{y}}', '\'h i\'', '{% j %}', 'k={{ z }}']
    assert split_args(input_v) == output_v

# Generated at 2022-06-13 07:10:25.135408
# Unit test for function split_args

# Generated at 2022-06-13 07:10:35.348577
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.common.collections import ImmutableDict
    import sys


# Generated at 2022-06-13 07:10:43.321407
# Unit test for function split_args
def test_split_args():
    assert 'test "test line" test' == join_args(split_args('test "test line" test'))
    assert 'test \\ "test line\\ test' == join_args(split_args('test \\\' "test line\\ test'))
    assert 'test "test line\\ test' == join_args(split_args('test \\\\\' "test line\\ test'))
    assert 'test "test line\\\\ test' == join_args(split_args('test \\\\\\\' "test line\\\\ test'))

# Generated at 2022-06-13 07:10:53.625850
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Test cases for the parse_kv function that converts
    a string of key/value items to a dict.
    '''

    # Arguments string has a single option
    assert parse_kv("user=root") == {"user": "root"}

    # Arguments string is empty
    assert parse_kv("") == {}

    # Arguments string has two options
    assert parse_kv("user=root foo=bar") == {"user": "root", "foo": "bar"}

    # Arguments string has two options separated by spaces
    assert parse_kv("user=root foo=bar") == {"user": "root", "foo": "bar"}

    # Arguments string has two options separated by a space and a comma

# Generated at 2022-06-13 07:11:11.450335
# Unit test for function split_args

# Generated at 2022-06-13 07:11:18.532557
# Unit test for function parse_kv
def test_parse_kv():
    # options = parse_kv(u"foo=bar baz=qux")
    options = parse_kv('foo=bar baz="qux quux" baz2=\\"qux quux\\"')
    assert len(options) == 2
    assert options["foo"] == "bar"
    assert options["baz"] == "qux quux"
    assert options["baz2"] == "qux quux"

    # options = parse_kv(u"foo=bar baz=qux", True)
    options = parse_kv('foo=bar baz="qux quux" baz2=\\"qux quux\\"', True)
    assert len(options) == 3
    assert options["foo"] == "bar"
    assert options["baz"] == "qux quux"
   

# Generated at 2022-06-13 07:11:28.560256
# Unit test for function parse_kv
def test_parse_kv():
    assert(parse_kv("foo=bar baz=blam") == {u"foo": u"bar", u"baz": u"blam", u"_raw_params": u""})
    assert(parse_kv("foo=bar baz=blam one-two-three") == {u"foo": u"bar", u"baz": u"blam", u"_raw_params": u"one-two-three"})
    assert(parse_kv("foo=bar baz=blam one-two-three", check_raw=True) == {u"foo": u"bar", u"baz": u"blam", u"_raw_params": u"one-two-three"})

# Generated at 2022-06-13 07:11:41.736315
# Unit test for function parse_kv
def test_parse_kv():
    print("Testing function parse_kv")


# Generated at 2022-06-13 07:11:50.814186
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('this=that creates=foo') == {u'creates': u'foo', u'this': u'that'}
    assert parse_kv('this=that creates=foo bar') == {u'creates': u'foo', u'this': u'that', u'_raw_params': u'bar'}
    assert parse_kv('this=that creates="a b" bar') == {u'creates': u'a b', u'this': u'that', u'_raw_params': u'bar'}
    assert parse_kv('this=that creates="a=b" bar') == {u'creates': u'a=b', u'this': u'that', u'_raw_params': u'bar'}


# Generated at 2022-06-13 07:12:02.133009
# Unit test for function split_args

# Generated at 2022-06-13 07:12:09.380318
# Unit test for function split_args

# Generated at 2022-06-13 07:12:20.709875
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a=b c = d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('c= d=e') == {'c': 'd', 'd': 'e'}
    assert parse_kv('creates=/tmp/a b=c') == {'creates': '/tmp/a', 'b': 'c'}
    assert parse_kv('a="b c" d=e') == {'a': 'b c', 'd': 'e'}

# Generated at 2022-06-13 07:12:32.902351
# Unit test for function split_args
def test_split_args():
    import _ast
    import json


# Generated at 2022-06-13 07:12:46.893729
# Unit test for function split_args

# Generated at 2022-06-13 07:13:04.787418
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}

    assert parse_kv(None, check_raw=True) == {}

    # assert parse_kv('b=1') == {'b': '1', '_raw_params': None}
    assert parse_kv('b=1', check_raw=True) == {'b': '1'}

    # assert parse_kv('b=1 c=2') == {'b': '1', 'c': '2', '_raw_params': None}
    assert parse_kv('b=1 c=2', check_raw=True) == {'b': '1', 'c': '2'}


# Generated at 2022-06-13 07:13:16.506558
# Unit test for function split_args
def test_split_args():
  try:
    result = split_args('foo=bar a=b c="foo bar"')
    assert result == ['foo=bar', 'a=b', 'c="foo bar"']

    result = split_args('"foo bar" baz')
    assert result == ['foo bar', 'baz']

    result = split_args("'foo bar' baz")
    assert result == ['foo bar', 'baz']

    result = split_args('foo=bar c="foo bar" baz')
    assert result == ['foo=bar', 'c="foo bar"', 'baz']

    result = split_args('foo="bar baz"')
    assert result == ['foo="bar', 'baz"']
  except AssertionError as e:
    print(result)
    raise e
test_split_args()


# Generated at 2022-06-13 07:13:22.068504
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.module_utils.six import assertCountEqual
    test_string = 'name=ansible state=present something_else=foo=bar key=val'
    result_dict = parse_kv(test_string)
    assertCountEqual(result_dict, dict(name=u'ansible',state=u'present',something_else=u'foo=bar',key=u'val'))

# Generated at 2022-06-13 07:13:25.022650
# Unit test for function parse_kv
def test_parse_kv():
    result = parse_kv("k1=v1 k2=v2")
    assert len(result) == 2
    assert result['k1'] == 'v1'
    assert result['k2'] == 'v2'


# Generated at 2022-06-13 07:13:34.888750
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv(u'one=1 two=2 three=3')
    assert options['one'] == u'1'
    assert options['two'] == u'2'
    assert options['three'] == u'3'
    assert len(options) is 3

    options = parse_kv(u'one=1 two="quoted value" three=3')
    assert options['one'] == u'1'
    assert options['two'] == u'quoted value'
    assert options['three'] == u'3'
    assert len(options) is 3

    options = parse_kv(u'one=1 two="quote \'inside\' quoted value" three=3')
    assert options['one'] == u'1'
    assert options['two'] == u"quote 'inside' quoted value"
    assert options['three']

# Generated at 2022-06-13 07:13:41.397781
# Unit test for function parse_kv
def test_parse_kv():
#def main():
    arg_string = 'foo=bar baz="bah humbug" bing=bong foo="foo the bar"'

    options = parse_kv(arg_string)
    assert(options['foo'] == 'bar')
    assert(options['baz'] == 'bah humbug')
    assert(options['bing'] == 'bong')
    assert(options['foo'] == 'foo the bar')

    arg_string2 = 'foo=bar baz="bah humbug" bing=bong foo="foo the bar"'
    options = parse_kv(arg_string2, check_raw=True)
    assert(options['foo'] == 'bar')
    assert(options['baz'] == 'bah humbug')
    assert(options['bing'] == 'bong')

# Generated at 2022-06-13 07:13:50.700425
# Unit test for function split_args

# Generated at 2022-06-13 07:14:02.252852
# Unit test for function parse_kv
def test_parse_kv():
    expected = {u'arg1': u'/tmp/hello',
                u'arg2': u'${test}',
                u'arg3': u'world3',
                u'arg4': u'world4',
                u'arg5': u'world5',
                u'arg6': u'world6'}

    raw_input = u"arg1='/tmp/hello' arg2='${test}' arg3=world3 arg4=world4 arg5=\"world5\" arg6=\"world6\""

    assert parse_kv(raw_input) == expected


# Splits the line into arguments, keeping quotes.

# Generated at 2022-06-13 07:14:10.214565
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('ansible_ssh_host=localhost ansible_ssh_pass=hunter2') == {'ansible_ssh_host': 'localhost', 'ansible_ssh_pass': 'hunter2'}
    assert parse_kv('ansible_ssh_host="localhost" ansible_ssh_pass=hunter2') == {'ansible_ssh_host': 'localhost', 'ansible_ssh_pass': 'hunter2'}
    assert parse_kv('ansible_ssh_host="local host" ansible_ssh_pass=hunter2') == {'ansible_ssh_host': 'local host', 'ansible_ssh_pass': 'hunter2'}

# Generated at 2022-06-13 07:14:19.114496
# Unit test for function split_args
def test_split_args():
    # test with a simple string
    assert split_args("a b c d e") == ["a", "b", "c", "d", "e"]

    # test with a string that has quotes in it
    assert split_args("a b='hello world' c='d e' f") == ["a", "b='hello world'", "c='d e'", "f"]

    # test with a string that has quotes in it, but with a variety of whitespace
    assert split_args("a    b='hello world' c='d e'\nf") == ["a", "b='hello world'", "c='d e'", "f"]

    # test with a string that has a jinja block in it

# Generated at 2022-06-13 07:14:42.464640
# Unit test for function split_args
def test_split_args():
    ''' This function tests the function split_args
    '''

    # Test the case when we have a command with a quoted arg
    quoted = b"foo='\n'"
    result = split_args(quoted)
    assert result[0] == "foo='"
    assert result[1] == "'"

    # Test the case when we have a command with a quoted arg with a newline inside
    quoted = b"foo='\nbar'"
    result = split_args(quoted)
    assert result[0] == "foo='\nbar'"

    # Test the case when we have a command with a quoted arg with a newline inside
    quoted = b"foo='\"bar\"'"
    result = split_args(quoted)
    assert result[0] == "foo='\"bar\"'"

    # Test the case when we have

# Generated at 2022-06-13 07:14:48.998643
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo \\\"bar baz\\\"') == ['foo', '\\\\"bar', 'baz\\\\"']
    assert split_args('foo "bar') == ['foo', '"bar']
    assert split_args('foo """bar""" baz') == ['foo', '"""bar"""', 'baz']
    assert split_args('foo "bar') == ['foo', '"bar']
    assert split_args('foo "bar baz') == ['foo', '"bar baz']

# Generated at 2022-06-13 07:14:57.910473
# Unit test for function split_args

# Generated at 2022-06-13 07:15:12.112582
# Unit test for function parse_kv
def test_parse_kv():
    kv_dicts = []
    kv_dicts.append(parse_kv('foo=bar'))
    kv_dicts.append(parse_kv('foo=bar key=val'))
    kv_dicts.append(parse_kv('foo="bar key=val"'))
    kv_dicts.append(parse_kv('foo=bar key="val key=val"'))
    kv_dicts.append(parse_kv('foo=b ar'))
    kv_dicts.append(parse_kv('foo="b ar"'))
    kv_dicts.append(parse_kv('foo=b\ ar'))
    kv_dicts.append(parse_kv('foo="b\ ar"'))

# Generated at 2022-06-13 07:15:22.928800
# Unit test for function parse_kv
def test_parse_kv():
    # tests for parsing non-string
    kv = parse_kv(None)
    assert kv == {}, 'None value not parsed as empty dict'
    # tests for parsing simple key value pairs
    kv = parse_kv('a=1 b=2 c=3')
    assert kv == {'a': '1', 'b': '2', 'c': '3'}, 'k=v pairs not parsed as dict'
    # tests for parsing quoted string
    kv = parse_kv('a="b c"')
    assert kv == {'a': 'b c'}, 'quoted string not parsed as one value'
    # tests for parsing escaped quotes
    kv = parse_kv('a="b\"c"')

# Generated at 2022-06-13 07:15:31.427859
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c=d e=f') == dict(a='b', c='d', e='f')
    assert parse_kv('a=b "c=d" e="f=g"') == dict(a='b', c='d', e='f=g')
    assert parse_kv('a=b "c=d" e="f=g"') == dict(a='b', c='d', e='f=g')
    assert parse_kv("a=b 'c=d' e='f=g'") == dict(a='b', c='d', e='f=g')

# Generated at 2022-06-13 07:15:36.376751
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a=b c=\"foo bar\"") == [u'a=b', u'c="foo bar"']
    assert split_args(u"a=b c=\\\"foo bar\\\"") == [u'a=b', u'c="foo bar"']
    assert split_args(u"a=b c={{ foo }}{{ bar }}") == [u'a=b', u'c={{ foo }}{{ bar }}']
    assert split_args(u"a=b c={{ foo }}\\{{ foo }}") == [u'a=b', u'c={{ foo }}{{ foo }}']
    assert split_args(u"a=b c=\\{{ foo }}") == [u'a=b', u'c={{ foo }}']

# Generated at 2022-06-13 07:15:43.786518
# Unit test for function split_args
def test_split_args():
    def _assert_result(input_args, expected_array):
        result = split_args(input_args)
        if result != expected_array:
            raise AssertionError('Expected: {0}\nActual: {1}'.format(expected_array, result))
    _assert_result('foo bar baz',
                   ['foo', 'bar', 'baz'])
    _assert_result('foo "bar baz"',
                   ['foo', '"bar baz"'])
    _assert_result('foo "bar baz" quux',
                   ['foo', '"bar baz"', 'quux'])
    _assert_result('foo "bar baz quux"',
                   ['foo', '"bar baz quux"'])

# Generated at 2022-06-13 07:15:52.531151
# Unit test for function parse_kv
def test_parse_kv():
    x = parse_kv("one=1 two=2 three=3 no_equal= no_value=")
    assert x['one'] == "1"
    assert x['two'] == "2"
    assert x['three'] == "3"
    assert x['no_equal'] == ""
    assert x['no_value'] == ""

    x = parse_kv("one=\"this is a test\" two='this is also a test' three=3")
    assert x['one'] == "this is a test"
    assert x['two'] == "this is also a test"
    assert x['three'] == "3"

    x = parse_kv("one=foo two=two three=3 \"four equal four\"='4=4'")
    assert x['one'] == "foo"

# Generated at 2022-06-13 07:16:05.280708
# Unit test for function split_args

# Generated at 2022-06-13 07:16:48.477600
# Unit test for function split_args
def test_split_args():
    '''
    A function to test the output of split_args to
    make sure it is doing what we expect.
    '''

    # the list of patterns we are using to test the arg splitter

# Generated at 2022-06-13 07:16:51.349664
# Unit test for function split_args
def test_split_args():
    args = 'foo bar baz=moo'
    assert split_args(args) == args.split(' ')

# Generated at 2022-06-13 07:16:58.216365
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b') == ['a=b']
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a="b b"') == ['a="b b"']
    assert split_args('a="b b" c=d') == ['a="b b"', 'c=d']
    assert split_args('a="b b" c="d d"') == ['a="b b"', 'c="d d"']
    assert split_args('a=b c="d d"') == ['a=b', 'c="d d"']
    assert split_args('a=b c=\'d d\'') == ['a=b', 'c=\'d d\'']

# Generated at 2022-06-13 07:17:09.731395
# Unit test for function split_args