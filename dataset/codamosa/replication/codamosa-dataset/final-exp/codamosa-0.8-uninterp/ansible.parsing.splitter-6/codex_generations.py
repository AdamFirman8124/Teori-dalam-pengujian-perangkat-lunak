

# Generated at 2022-06-13 07:07:31.651828
# Unit test for function split_args
def test_split_args():
    print(split_args("""{{ foo }}"""))
    print(split_args("""{{ foo }} {{ bar }}"""))
    print(split_args("""{{ foo }} {{ bar }}  {{ baz qux }} """))
    print(split_args("""{{ foo }} {{ bar }} '{{ baz qux }}' """))
    print(split_args("""{{ foo }} {{ bar }} "{{ baz qux }}" """))
    print(split_args("""{{ foo }} {{ bar }} {{ baz qux }} {{ alpha beta }} """))
    print(split_args("""{{ foo }} {{ bar }} {{ baz qux }} {{ alpha beta }} {{ one two three }}"""))
    print(split_args("""{{ foo }} {{ bar }} {{ baz qux }} {{ alpha beta }} \\
{{ one two three }}"""))
   

# Generated at 2022-06-13 07:07:40.864911
# Unit test for function split_args
def test_split_args():
    # test basic string
    args = 'a=b c="foo bar"'
    result = split_args(args)
    assert result == ['a=b', 'c="foo bar"']

    # test command module args
    args = 'a=b c="foo bar" d={{ testvar }}'
    result = split_args(args)
    assert result == ['a=b', 'c="foo bar"', 'd={{ testvar }}']

    # test with spaces after the first equals sign
    args = 'a=b c="foo bar" d={{ testvar }} e="a=b"'
    result = split_args(args)
    assert result == ['a=b', 'c="foo bar"', 'd={{ testvar }}', 'e="a=b"']

    # test with spaces at the end of the string


# Generated at 2022-06-13 07:07:55.329355
# Unit test for function parse_kv
def test_parse_kv():
    from copy import copy

# Generated at 2022-06-13 07:08:05.613813
# Unit test for function split_args

# Generated at 2022-06-13 07:08:16.499441
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 07:08:21.206583
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv('foo=bar name=tim other=stuff'))
    print(parse_kv('remove=1 create=0 creates=test.txt removes=*.tmp'))
    print(parse_kv('chdir=foo executable=/bin/bash warn=no'))
    print(parse_kv('Creates=/does/not/exist'))
    print(parse_kv('stdin=myinfile.txt stdin_add_newline=True'))
    print(parse_kv('strip_empty_ends=True'))



# Generated at 2022-06-13 07:08:28.315453
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.common.parameters import Parameter

    # Load the NTC-templates module from the ntc-ansible repository
    from ansible.modules.network.ntc_templates import ntc_template_install
    result = ntc_template_install._process_args(ntc_template_install.argument_spec,
        dict(template_name='foo bar'), 'ntc_template_install')[1]
    
    # Make sure that the command arguments are split into a list
    assert isinstance(result['args'], Parameter)
    assert isinstance(result['args'].value, list)
    assert result['args'].value == ['name="foo bar"']

    # Make sure output is the same when run through both methods
    args = "name=foo bar baz"
    assert split_args

# Generated at 2022-06-13 07:08:40.047528
# Unit test for function parse_kv
def test_parse_kv():
    args = "a=1 b='2 3' c=4d=e"
    options = parse_kv(args, check_raw=True)
    assert options == {u'a':u'1', u'b':u'2 3', u'c': u'4d=e', u'_raw_params':u"a=1 b='2 3' c=4d=e"}

    args = "a=1 b='2=3' c=4d='e f'"
    options = parse_kv(args, check_raw=True)
    assert options == {u'a':u'1', u'b':u'2=3', u'c': u'4d=e f', u'_raw_params':u"a=1 b='2=3' c=4d='e f'"}

    args

# Generated at 2022-06-13 07:08:52.709305
# Unit test for function split_args
def test_split_args():
    '''
    "command" is the input to the split_args function
    "expect" is expected output from the split_args function
    "join" is the input to the join_args function
    '''

# Generated at 2022-06-13 07:09:04.061432
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b="2" c=3') == {'a': '1', 'b': '2', 'c': '3'}
    assert parse_kv('"foo"=bar') == {'"foo"': 'bar'}
    assert parse_kv('\\"foo\\"=bar') == {'\\"foo\\"': 'bar'}
    assert parse_kv('a="\\"x\\""') == {'a': '\\"x\\"'}
    assert parse_kv('a=\\" x\\"') == {'a': '\\" x\\"'}
    assert parse_kv('a="foo bar"') == {'a': 'foo bar'}
    assert parse_kv('"a"="b"') == {'a': 'b'}

# Generated at 2022-06-13 07:09:22.058725
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo="a=b" bar="c=d e=f"') == {u'foo': u'a=b', u'bar': u'c=d e=f'}
    assert parse_kv('foo="a=b" bar="c=d e=f"') == {u'foo': u'a=b', u'bar': u'c=d e=f'}
    assert parse_kv('foo="a=b" bar="c=d e=f"') == {u'foo': u'a=b', u'bar': u'c=d e=f'}
    assert parse_kv('foo="a=b" bar="c=d e=f"') == {u'foo': u'a=b', u'bar': u'c=d e=f'}

# Generated at 2022-06-13 07:09:36.268119
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c="d e" f="g=h"') == {u'a': u'b', u'c': u'd e', u'f': u'g=h'}
    assert parse_kv('sudo="--option=value"') == {u'sudo': u'--option=value'}
    assert parse_kv('with spaces=one') == {u'with spaces': u'one'}
    assert parse_kv('with spaces="one two"') == {u'with spaces': u'one two'}
    assert parse_kv("_raw_params=a=b c='d e' f=\"g=h\"") == {u'_raw_params': u"a=b c='d e' f=\"g=h\""}

# Generated at 2022-06-13 07:09:48.308638
# Unit test for function parse_kv
def test_parse_kv():
    # expect dictionary
    assert parse_kv('a=1 b="2"') == {u'a': u'1', u'b': u'2'}
    # expect dictionary
    assert parse_kv('a=1 b="2" c=b') == {u'a': u'1', u'b': u'2', u'c': u'b'}
    # expect dictionary
    # check unexpected value
    assert parse_kv('a=1 b="2" c=b') == {u'a': u'1', u'b': u'2', u'c': u'b'}
    # expect dictionary
    # check no value
    assert parse_kv('a= b="2" c=') == {u'a': u'', u'b': u'2', u'c': u''}

# Generated at 2022-06-13 07:09:57.819895
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for the parse_kv function.
    '''
    # Dummy objects for testing
    class DummyModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    def test(module, args, check_raw, expected_result):
        options = parse_kv(args, check_raw)
        module.assertTrue(isinstance(options, dict))
        module.assertEqual(options, expected_result)

    import unittest

# Generated at 2022-06-13 07:10:07.497956
# Unit test for function parse_kv
def test_parse_kv():
    def test(input, output):
        assert output == parse_kv(input)
    yield test, None, {}
    yield test, '', {}
    yield test, 'a=A', {'a': 'A'}
    yield test, ' a    =    A ', {'a': 'A'}
    yield test, 'a=A b=B', {'a': 'A', 'b': 'B'}
    yield test, 'a=A b=B c=C', {'a': 'A', 'b': 'B', 'c': 'C'}
    yield test, 'a=A  b=B c=C', {'a': 'A', 'b': 'B', 'c': 'C'}
    yield test, 'a=A a=B', {'a': 'B'}
    yield test

# Generated at 2022-06-13 07:10:21.212873
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=2 c=3") == {u'a': u'1', u'c': u'3', u'b': u'2'}
    assert parse_kv("a=1 b=2 c='3 4'") == {u'a': u'1', u'c': u'3 4', u'b': u'2'}
    assert parse_kv("a=1 b=2 c=\"3 4\"") == {u'a': u'1', u'c': u'3 4', u'b': u'2'}
    assert parse_kv("a=1 b=2 c=\"3\"d\"") == {u'a': u'1', u'c': u'3"d', u'b': u'2'}

# Generated at 2022-06-13 07:10:29.960972
# Unit test for function split_args
def test_split_args():
    '''
    tests the custom shlex that splits out command arguments
    '''
    test_input = "command arg1=foo arg2='foo bar'"

    expected = [u'command', u'arg1=foo', u"arg2='foo bar'"]
    result = split_args(test_input)

    assert result == expected


test_template = '''
- name: test command module
  command: "{{ ansible_env.HOME }}/mycommand {{ ansible_env.HOSTNAME }}"
'''



# Generated at 2022-06-13 07:10:39.473146
# Unit test for function split_args
def test_split_args():
    assert split_args('') == ['']
    assert split_args(' ') == [' ']
    assert split_args('\n') == ['\n']
    assert split_args(' \n ') == [' \n ']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"\nd="foo bar"') == ['a=b', 'c="foo bar"\nd="foo bar"'], 'first quote works'
    assert split_args('a=b c="foo bar"\nd="foo bar"\ne="foo bar"') == ['a=b', 'c="foo bar"\nd="foo bar"\ne="foo bar"'], 'multiple quotes with newlines works'
    assert split_args

# Generated at 2022-06-13 07:10:45.514200
# Unit test for function parse_kv
def test_parse_kv():
    result = parse_kv('a=b c="hello world"')
    assert result == {'a': 'b', 'c': 'hello world'}
    result = parse_kv('a=b c=hello\\ world')
    assert result == {'a': 'b', 'c': 'hello world'}
    result = parse_kv('a=b c=hello\\=world')
    assert result == {'a': 'b', 'c': 'hello=world'}
    result = parse_kv('a=b c=hello\\=world d=foo bar')
    assert result == {'a': 'b', 'c': 'hello=world', '_raw_params': 'd=foo bar'}


#
# split_args()
#

# Generated at 2022-06-13 07:10:51.232649
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Test parser function parse_kv
    '''

    test_arg = u'a=b c="d e" f="g\"hi"'
    expected = {u'a': u'b', u'c': u'd e', u'f': u'g\"hi'}
    result = parse_kv(test_arg)
    assert result == expected


# Generated at 2022-06-13 07:11:17.697796
# Unit test for function split_args
def test_split_args():
    '''
    Run a unit test for function split_args
    '''
    import json

# Generated at 2022-06-13 07:11:27.878533
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest
    from ansible.module_utils import basic


# Generated at 2022-06-13 07:11:41.307537
# Unit test for function parse_kv
def test_parse_kv():
    # Test 1
    args = '''a=1 b=2 c=3'''
    result = parse_kv(args, check_raw=False)
    assert(result['a'] == '1')
    assert(result['b'] == '2')
    assert(result['c'] == '3')

    # Test 2, using quoting within the value
    args = '''a=1\ b=2\ c=3'''
    result = parse_kv(args, check_raw=False)
    assert(result['a'] == '1\ b')
    assert(result['b'] == '2\ c')
    assert(result['c'] == '3')

    # Test 3, using quoting within the value
    args = '''a=1\ b=2\ c=a\=b'''
    result = parse

# Generated at 2022-06-13 07:11:45.369859
# Unit test for function parse_kv
def test_parse_kv():
    s = 'foo=bar biz=baz one key=value'
    assert parse_kv(s) == {'foo': 'bar', 'biz': 'baz', 'key': 'value', '_raw_params': 'one'}


# Generated at 2022-06-13 07:11:52.897490
# Unit test for function split_args
def test_split_args():
    args = "creates=foo removes=bar"
    assert split_args(args) == ["creates=foo", "removes=bar"]
    args = "creates=foo removes={{ bar }}"
    assert split_args(args) == ["creates=foo", "removes={{ bar }}"]
    args = 'This is a - "single quoted" string'
    assert split_args(args) == ['This', 'is', 'a', '-', '"single quoted"', 'string']
    args = "This is a - 'single quoted' string"
    assert split_args(args) == ['This', 'is', 'a', '-', "'single quoted'", 'string']
    args = "creates=/tmp/foo.txt"
    assert split_args(args) == ['creates=/tmp/foo.txt']


# Generated at 2022-06-13 07:12:02.748909
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv('command=echo "Hello World" > /tmp/helloworld.txt creates=/tmp/helloworld.txt')
    assert options['command'] == 'echo "Hello World" > /tmp/helloworld.txt'
    assert options['creates'] == '/tmp/helloworld.txt'
    # Ensure raw_params is not set
    assert '_raw_params' not in options
    options = parse_kv('command=echo "Hello World" > /tmp/helloworld.txt creates=/tmp/helloworld.txt', check_raw=True)
    assert options['command'] == 'echo "Hello World" > /tmp/helloworld.txt'
    assert options['creates'] == '/tmp/helloworld.txt'
    # And check raw_params
    assert options['_raw_params']

# Generated at 2022-06-13 07:12:10.565936
# Unit test for function parse_kv
def test_parse_kv():
    import os
    # Test 1:
    # Verify if parse_kv ignores the first space when the first argument is a string
    # Input: parse_kv("param1=value1 param2=value2 param3=value3")
    # Expected output: {'param2': 'value2', 'param3': 'value3', 'param1': 'value1', '_raw_params': 'param1=value1 param2=value2 param3=value3'}
    kv_test1 = parse_kv("param1=value1 param2=value2 param3=value3")
    assert(kv_test1 == {'param2': 'value2', 'param3': 'value3', 'param1': 'value1', '_raw_params': 'param1=value1 param2=value2 param3=value3'})

# Generated at 2022-06-13 07:12:17.848670
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:31.252632
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a=b c=d') == {u'a': u'b', u'c': u'd'}

    assert parse_kv('a=b args=foo') == {u'a': u'b', u'args': u'foo'}
    assert parse_kv("a=b args='foo bar'") == {u'a': u'b', u'args': u'foo bar'}
    assert parse_kv("a=b args=\"foo bar\"") == {u'a': u'b', u'args': u'foo bar'}


# Generated at 2022-06-13 07:12:45.534034
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv('1=2 3=4 5=6')
    assert options['1'] == '2'
    assert options['3'] == '4'
    assert options['5'] == '6'

    options = parse_kv('1=2 3=4 5=6', check_raw=True)
    assert options['1'] == '2'
    assert options['3'] == '4'
    assert options['5'] == '6'

    options = parse_kv('1=2 3=4 5=6 arg1 arg2 arg3', check_raw=True)
    assert options['1'] == '2'
    assert options['3'] == '4'
    assert options['5'] == '6'
    assert options['_raw_params'] == 'arg1 arg2 arg3'
    # -- END unit test

# Generated at 2022-06-13 07:13:05.921065
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\" baz"') == ['a=b', 'c="foo bar\\" baz"']
    assert split_args('a=b c="foo bar\\" baz"') == ['a=b', 'c="foo bar\\" baz"']
    assert split_args('a=b c="{{"') == ['a=b', 'c="{{']
    assert split_args('a=b c="{{"') == ['a=b', 'c="{{']
    assert split_args('foo "bar baz') == ['foo', '"bar baz']


# Generated at 2022-06-13 07:13:10.918917
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('foo=bar bar') == {u'foo': u'bar bar'}
    assert parse_kv('foo=bar bar foo=baz') == {u'foo': u'baz'}
    assert parse_kv('foo=bar bar foo=baz foo="bam zam"') == {u'foo': u'bam zam'}
    assert parse_kv('foo=bar bar foo=baz foo="bam zam" foo=bam') == {u'foo': u'bam'}
    assert parse_kv('foo="bam zam"') == {u'foo': u'bam zam'}

# Generated at 2022-06-13 07:13:22.149176
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo= bar=\tbaz=') == {'foo': '', 'bar': '', 'baz': ''}
    assert parse_kv('foo=bar') == {'foo': 'bar'}
    assert parse_kv('foo="bar"') == {'foo': 'bar'}
    assert parse_kv('foo=\'bar\'') == {'foo': 'bar'}
    assert parse_kv('foo="bar\nbaz"') == {'foo': 'bar\nbaz'}
    assert parse_kv('foo="bar "') == {'foo': 'bar '}
    assert parse_kv('foo="bar" ') == {'foo': 'bar'}

# Generated at 2022-06-13 07:13:32.067626
# Unit test for function split_args
def test_split_args():
    def do_test(expected, input, msg):
        result = split_args(input)
        if result != expected:
            print(msg)
            print("Expected : {0}".format(expected))
            print("Got      : {0}".format(result))
            raise AssertionError

    do_test([], '', 'split_args() should handle empty input')
    do_test(['echo'], 'echo', 'split_args() should handle plain commands')
    do_test(['echo', 'hello'], 'echo hello', 'split_args() should handle simple args')
    do_test(['echo', 'hello world'], 'echo "hello world"', 'split_args() should handle quoted args')

# Generated at 2022-06-13 07:13:39.421734
# Unit test for function split_args

# Generated at 2022-06-13 07:13:44.154336
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'foo=bar baz=qux') == {u'foo': u'bar', u'baz': u'qux'}
    assert parse_kv(u'foo=bar=baz') == {u'foo': u'bar=baz'}
    assert parse_kv(u'foo="bar baz"') == {u'foo': u'bar baz'}
    assert parse_kv(u"foo=bar'baz'") == {u'foo': u"bar'baz'"}
    assert parse_kv(u'foo=bar\\baz') == {u'foo': u'bar\\baz'}
    assert parse_kv(u'foo=bar\\=baz') == {u'foo': u'bar=baz'}
    assert parse

# Generated at 2022-06-13 07:13:50.623283
# Unit test for function split_args

# Generated at 2022-06-13 07:14:05.056382
# Unit test for function split_args
def test_split_args():

    print("testing split args")

    assert split_args('a=b c="foo bar" d="foo \'bar\' gee"') == ['a=b', 'c="foo bar"', 'd="foo \'bar\' gee"']
    assert split_args('a=b c="foo bar" d="foo \'bar\' gee\\"') == ['a=b', 'c="foo bar"', 'd="foo \'bar\' gee"']
    assert split_args('a=b c="foo bar" d="foo \'bar\' gee"\\') == ['a=b', 'c="foo bar"', 'd="foo \'bar\' gee"']

# Generated at 2022-06-13 07:14:10.214892
# Unit test for function split_args
def test_split_args():

    input_args = u"hello world how are 'you doing' today? foo=bar baz={{ bing }} thing='{{ foo }} {{ bar }}'"
    expected_output = [u'hello', u'world', u'how', u'are', u'you doing', u'today?', u"foo=bar", u"baz={{ bing }}", u"thing='{{ foo }} {{ bar }}'"]

    actual_output = split_args(input_args)

    assert actual_output == expected_output

# Generated at 2022-06-13 07:14:16.804416
# Unit test for function split_args

# Generated at 2022-06-13 07:15:14.101162
# Unit test for function parse_kv
def test_parse_kv():
    assert u'test' == parse_kv(" test=123 ")["test"]
    assert u'test' == parse_kv(" test='123' ")["test"]
    assert u'test' == parse_kv(" test=\"123\" ")["test"]
    assert u'"test"' == parse_kv(" \"test\"=123 ")["\"test\""]
    assert u'test' == parse_kv(" test=123", True)["test"]
    assert u'test' == parse_kv(" test='123'", True)["test"]
    assert u'test' == parse_kv(" test=\"123\"", True)["test"]
    assert u'"test"' == parse_kv(" \"test\"=123", True)["\"test\""]

# Generated at 2022-06-13 07:15:20.008692
# Unit test for function split_args
def test_split_args():
    # Does not handle unbalanced quotes, that is outside the scope of this unit test
    assert split_args('"foo bar"') == ['"foo bar"']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('foo="bar baz" bar=baz') == ['foo="bar baz"', 'bar=baz']
    assert split_args('foo="bar baz" bar=baz qux') == ['foo="bar baz"', 'bar=baz', 'qux']
    assert split_args('foo="bar baz" \\\nbar=baz qux') == ['foo="bar baz"', 'bar=baz', 'qux']

# Generated at 2022-06-13 07:15:29.310255
# Unit test for function parse_kv
def test_parse_kv():
    # generate some random key=value pairs
    import random
    from string import ascii_letters
    n = random.randint(1, 10)
    kvs = ['{0}={1}'.format(
        ''.join(random.sample(ascii_letters, random.randint(5, 10))),
        ''.join(random.sample(ascii_letters, random.randint(5, 10)))
    ) for _ in range(n)]
    params = ' '.join(kvs)
    # generate some random raw params
    n = random.randint(1, 10)
    raw = [''.join(random.sample(ascii_letters, random.randint(5, 10)))
           for _ in range(n)]

# Generated at 2022-06-13 07:15:39.375799
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args
    '''

# Generated at 2022-06-13 07:15:45.821013
# Unit test for function split_args

# Generated at 2022-06-13 07:15:54.144043
# Unit test for function parse_kv
def test_parse_kv():
    with open('test.txt', 'r') as cases:
        for case in cases:
            if case.startswith('#'):
                continue
            case = case.strip()
            if case == '':
                continue
            k, v = case.split(' = ', 1)
            res = parse_kv(k)
            assert res == eval(v), '{0} != {1}'.format(res, eval(v))

# Generated at 2022-06-13 07:16:00.124608
# Unit test for function parse_kv
def test_parse_kv():
    # Testing parsing with simple args
    assert parse_kv('foo=bar abc=def') == {u'foo': u'bar', u'abc': u'def'}
    # Testing parsing with escaped chars
    assert parse_kv(u"foo=bar baz='this is a string with spaces' abc=\"this is another \\'string\\' with quotes\"") == {u'foo': u'bar', u'baz': u'this is a string with spaces', u'abc': u"this is another \\'string\\' with quotes"}
    # Testing parsing with escaped chars and backslashes

# Generated at 2022-06-13 07:16:05.418039
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a\n=\nb c") == ["a", "=", "b", "c"]
    assert split_args(u"foo='bar baz'") == ["foo=bar baz"]
    assert split_args(u"foo='bar baz'") != ["foo", "=", "bar baz"]
    assert split_args(u"foo='bar baz'") != ["foo", "=", "bar", "baz"]
    assert split_args(u"foo='bar baz'") != ["foo=bar", "baz"]
    assert split_args(u"foo='bar baz'") != ["foo=bar baz"]

# Generated at 2022-06-13 07:16:14.340503
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=b c="d e" f=\'g h\'') == {u'a': u'b', u'c': u'd e', u'f': u'g h'}
    assert parse_kv('a=1 c="2" f=3') == {u'a': u'1', u'c': u'2', u'f': u'3'}
    assert parse_kv('a=1 c=2 f=3') == {u'a': u'1', u'c': u'2', u'f': u'3'}
    assert parse_kv('a=1 c=2 f=3 d') == {u'a': u'1', u'c': u'2', u'f': u'3'}

# Generated at 2022-06-13 07:16:23.672076
# Unit test for function parse_kv
def test_parse_kv():
    #example1-1
    args = "option1=val1 option2=val2"
    assert parse_kv(args) == {'option2': 'val2', 'option1': 'val1'}
    #example1-2
    #if args does not contain '=', then the raw parameter will not be assigned.
    args = "option1 val2"
    assert parse_kv(args) == {}
    #example2
    #if args does not contain '=' and check_raw is true, then the raw parameter will be assigned
    args = "option1 val2"
    assert parse_kv(args, check_raw=True) == {'_raw_params': 'option1 val2'}
    #example3
    #if args contains '=', then the raw parameter will not be assigned.