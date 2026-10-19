

# Generated at 2022-06-13 07:08:06.498451
# Unit test for function split_args

# Generated at 2022-06-13 07:08:16.549159
# Unit test for function split_args
def test_split_args():
    f = open("test_args.txt")

    lines = f.readlines()

    for line in lines:
        if line.startswith("#"):
            continue

        if line.isspace():
            continue


# Generated at 2022-06-13 07:08:23.045067
# Unit test for function parse_kv
def test_parse_kv():
    # Test from https://github.com/ansible/ansible/blob/devel/test/units/modules/test_net_tools.py
    assert parse_kv("foo=bar baz=foo") == {u'foo': u'bar', u'baz': u'foo'}
    assert parse_kv("foo=bar bar=baz") == {u'foo': u'bar', u'bar': u'baz'}
    assert parse_kv("foo='bar baz'") == {u'foo': u'bar baz'}
    assert parse_kv("foo='bar baz' bar='foo'") == {u'foo': u'bar baz', u'bar': u'foo'}

# Generated at 2022-06-13 07:08:34.641717
# Unit test for function split_args

# Generated at 2022-06-13 07:08:46.171479
# Unit test for function split_args
def test_split_args():
    """Very basic unit tests for the split_args function"""
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.converters import to_bytes

    # This is a list of tuples (args as a string, expected result as a list)

# Generated at 2022-06-13 07:08:51.922203
# Unit test for function split_args
def test_split_args():
    args = 'ls -ltr /tmp || ls -ltr /opt || echo "I like trains"'
    params = split_args(args)
    assert params == ['ls', '-ltr', '/tmp', '||', 'ls', '-ltr', '/opt', '||', 'echo', '"I like trains"']

# Unit test function to check we can handle a line continuation
    args = 'ls -ltr \\\n/tmp \\\n|| ls -ltr /opt || echo "I like trains"'
    params = split_args(args)
    assert params == ['ls', '-ltr', '/tmp', '||', 'ls', '-ltr', '/opt', '||', 'echo', '"I like trains"']

# Unit test function to check we can handle a line continuation

# Generated at 2022-06-13 07:09:03.195005
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=b c="d e"') == {u'a': u'b', u'c': u'd e'}
    assert parse_kv(u'a=b c="d e"', check_raw=True) == {u'a': u'b', u'c': u'd e', u'_raw_params': u'a=b c="d e"'}
    assert parse_kv(u'a=b c=d e') == {u'a': u'b', u'c': u'd e'}
    assert parse_kv(u'a=b c=d e', check_raw=True) == {u'a': u'b', u'_raw_params': u'a=b', u'c': u'd e'}

# Generated at 2022-06-13 07:09:12.485451
# Unit test for function split_args

# Generated at 2022-06-13 07:09:20.746006
# Unit test for function split_args
def test_split_args():

    import sys
    import subprocess

    # run the test in a python3 env so we can use byte strings
    # See https://bugs.python.org/issue26163 for why we can't
    # just do "python3 -m pytest -v test_utils.py" from the command line
    py3 = subprocess.Popen([sys.executable, '-m', 'pytest', '-v', 'test_utils.py'], stdout=subprocess.PIPE)
    (stdout, stderr) = py3.communicate()
    print(stdout.decode().rstrip())
    sys.exit(py3.returncode)


# Generated at 2022-06-13 07:09:35.728579
# Unit test for function split_args

# Generated at 2022-06-13 07:10:05.821566
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('first=one') == { 'first': 'one' }
    assert parse_kv('first="one two"') == { 'first': 'one two' }
    assert parse_kv('first="one two" second=three') == { 'first': 'one two', 'second': 'three' }
    assert parse_kv('first="one two" second=three four') == { 'first': 'one two', '_raw_params': 'second=three four' }
    assert parse_kv('first="one two" second=three four five') == { 'first': 'one two', '_raw_params': 'second=three four five' }
    assert parse_kv('first=one\\ second=two') == { 'first': 'one second=two' }

# Generated at 2022-06-13 07:10:08.694105
# Unit test for function parse_kv
def test_parse_kv():
    args = "k1=val1 k2=\"val2\" k3='val3'"

    expected_result = {'k1': 'val1', 'k3': 'val3', 'k2': 'val2'}
    assert parse_kv(args) == expected_result


# Generated at 2022-06-13 07:10:21.887937
# Unit test for function parse_kv
def test_parse_kv():
    kv_string = 'foo=bar bam=true fie="" fum="foobar"'
    parsed = {
        'bam': 'true',
        'foo': 'bar',
        'fie': '',
        'fum': 'foobar',
    }
    assert parsed == parse_kv(kv_string), "K/V string parsing did not match expected output"
    raw_params = [
        'foo=bar',
        'bam=true',
        'fie=""',
        'fum="foobar"',
    ]
    assert raw_params == parse_kv(kv_string, check_raw=True)['_raw_params'], \
        'Able to parse raw list of k/v options'



# Generated at 2022-06-13 07:10:33.242281
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("") == {}
    assert parse_kv("a=b") == {u'a': u'b'}
    assert parse_kv("a=b=c") == {u'a': u'b=c'}
    assert parse_kv("a='b=c'") == {u'a': u'b=c'}
    assert parse_kv("a=\"b=c\"") == {u'a': u'b=c'}
    assert parse_kv("a=b c=d") == {u'a': u'b', u'c': u'd'}
    assert parse_kv("a='b c'") == {u'a': u'b c'}

# Generated at 2022-06-13 07:10:41.879426
# Unit test for function split_args
def test_split_args():
    assert ['echo', 'foo bar', '{{car}}', '{{baz}}', 'foobar', '{% foo %}'] == split_args('echo foo bar {{car}} {{baz}} foobar {% foo %}')
    assert ['"foo bar"'] == split_args('"foo bar"')
    assert ['"foo bar"', '"baz"', '"{{foo}}"'] == split_args('"foo bar" "baz" "{{foo}}"')
    assert ['"foo bar"', '"baz"', '"{{foo}}"', '"{% foo %}"'] == split_args('"foo bar" "baz" "{{foo}}" "{% foo %}"')
    assert ['"foo bar"', '"baz', 'foo', 'bar"', '"{% foo %}"'] == split

# Generated at 2022-06-13 07:10:46.273124
# Unit test for function split_args
def test_split_args():
    # Test 1 : {% abc %} = "cdf"
    args = '{% abc %} = "cdf"'
    result = split_args(args)
    assert result == ['{% abc %}', '=', '"cdf"']

    # Test 2 : {% abc %} = "cdf"
    args = '{% abc %} = "cd\\"f"'
    result = split_args(args)
    assert result == ['{% abc %}', '=', '"cd\\"f"']

    # Test 3 : abc = "cd\\"f"
    args = 'abc = "cd\\"f"\nefg'
    result = split_args(args)
    assert result == ['abc', '=', '"cd\\"f"\nefg']

   

# Generated at 2022-06-13 07:10:55.206728
# Unit test for function parse_kv

# Generated at 2022-06-13 07:11:01.938323
# Unit test for function split_args
def test_split_args():
    '''
    Python 3.2 doesn't support unittest.skip, so we make it a module level function
    so we can skip it easily.
    '''
    import unittest

    class TestSplitArgs(unittest.TestCase):
        '''
        Unit tests for AnsibleModule.split_args
        '''
        def setUp(self):
            # we want to run this test even if skip tests is enabled,
            # so we default to False and only set to True if we [really] can't test
            self._can_test = False

        def is_unquote_avail(self):
            '''
            Test function to determine if we have unquote available
            '''

# Generated at 2022-06-13 07:11:10.074877
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv('foo="bar baz" hoge=fuga'))
    print(parse_kv('foo="bar baz" hoge="\\"fuga\\""'))
    print(parse_kv('foo="bar baz" hoge=\'\\"fuga\\"\''))
    print(parse_kv('foo="bar baz" hoge="\\\\"fuga\\\\""'))
    print(parse_kv('foo="bar baz" hoge=\'\\\\"fuga\\\\"\''))
    print(parse_kv('foo="bar baz" hoge="\\\\\\"fuga\\\\\\""'))
    print(parse_kv('foo="bar baz" hoge=\'\\\\\\"fuga\\\\\\"\''))

# Generated at 2022-06-13 07:11:17.727415
# Unit test for function split_args

# Generated at 2022-06-13 07:11:36.723772
# Unit test for function split_args
def test_split_args():
    assert [] == split_args('')
    assert ['ls'] == split_args('ls')
    assert ['tag=self'] == split_args('tag=self')
    assert ['tag=self_service'] == split_args('tag=self_service')
    assert ['echo', '"Hello World"'] == split_args('echo "Hello World"')
    assert ['echo', "Hello World"] == split_args(u'echo Hello World')
    assert ['echo', "Hello\nWorld"] == split_args(u'echo Hello\nWorld')
    assert ['echo', "Hello\nWorld"] == split_args(u'echo Hello\nWorld')
    assert ['ls', '-l /home'] == split_args('ls -l /home')
    assert ['ls -l /home'] == split_args('ls -l /home')

# Generated at 2022-06-13 07:11:47.430147
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("one=1") == {'one': u'1'}
    assert parse_kv("one=1 two=2") == {'one': u'1', 'two': u'2'}
    assert parse_kv("one=1 two=2 three=3") == {'one': u'1', 'two': u'2', 'three': u'3'}
    assert parse_kv("one two three four") == {u'_raw_params': u'one two three four'}
    assert parse_kv("one two three=four") == {u'three': u'four', u'_raw_params': u'one two'}

# Generated at 2022-06-13 07:11:53.904039
# Unit test for function split_args

# Generated at 2022-06-13 07:12:03.394435
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"a=b c=d") == dict(a="b", c="d")
    assert parse_kv(u'a=b c="d"') == dict(a="b", c="d")
    assert parse_kv(u"a=b c='d'") == dict(a="b", c="d")
    assert parse_kv(u"a=b c=d e='f=g'") == dict(a="b", c="d", e="f=g")
    assert parse_kv(u"a=b c=d e='f=\"g\"'") == dict(a="b", c="d", e='f="g"')

# Generated at 2022-06-13 07:12:11.053617
# Unit test for function split_args

# Generated at 2022-06-13 07:12:18.050822
# Unit test for function split_args

# Generated at 2022-06-13 07:12:31.414222
# Unit test for function parse_kv
def test_parse_kv():
    '''
    This is unit test for function parse_kv.
    '''
    assert parse_kv('a=b verbose') == {'a': 'b', '_raw_params': 'verbose'}
    assert parse_kv('a=b=c') == {'a': 'b=c'}
    assert parse_kv('a=b=c', check_raw=True) == {'a': 'b=c', '_raw_params': 'a=b=c'}
    assert parse_kv('=b=c') == {'': 'b=c'}
    assert parse_kv('a=b=c', check_raw=True) == {'a': 'b=c', '_raw_params': 'a=b=c'}

# Generated at 2022-06-13 07:12:45.725635
# Unit test for function parse_kv
def test_parse_kv():
    opt = parse_kv("foo=bar")
    assert opt == dict(foo="bar")

    opt = parse_kv("foo=bar baz=qux")
    assert opt == dict(foo="bar", baz="qux")

    opt = parse_kv("foo=bar baz=qux cat")
    assert opt == dict(foo="bar", baz="qux", _raw_params="cat")

    opt = parse_kv("foo=bar baz=qux cat dog")
    assert opt == dict(foo="bar", baz="qux", _raw_params="cat dog")

    # test some exotic stuff
    opt = parse_kv("foo bar baz=\"qux = dog = hen\"")
    assert opt == dict(foo=True, baz="qux = dog = hen")

#

# Generated at 2022-06-13 07:12:54.608023
# Unit test for function split_args
def test_split_args():
    assert split_args("foo=bar baz=quux") == ['foo=bar', 'baz=quux']
    assert split_args("foo=bar baz=quux\\") == ['foo=bar', 'baz=quux\\']
    assert split_args("bar baz=quux foo=bar") == ['bar', 'baz=quux', 'foo=bar']
    assert split_args("bar foo='baz  quux'") == ['bar', "foo='baz  quux'"]
    assert split_args("bar foo='baz  quux'") == ['bar', "foo='baz  quux'"]
    assert split_args("bar foo='baz  quux'") == ['bar', "foo='baz  quux'"]

# Generated at 2022-06-13 07:13:04.001560
# Unit test for function split_args
def test_split_args():

    assert split_args(u'a="b c d"') == [u'a=', u'"b c d"']
    assert split_args(u'a="b c \\\\ d"') == [u'a=', u'"b c \\\\\\\\ d"']
    assert split_args(u'a="b c = d"') == [u'a=', u'"b c = d"']
    assert split_args(u"a='b c = d'") == [u'a=', u"'b c = d'"]
    assert split_args(u'a=b c=d') == [u'a=b', u'c=d']
    assert split_args(u'a=b c=d n=m') == [u'a=b', u'c=d', u'n=m']

# Generated at 2022-06-13 07:13:46.485067
# Unit test for function parse_kv
def test_parse_kv():
    arguments = 'key1=value1 key2="value 2" "key 3"="value 3" "key 4"="value 4" "with backslash"=\\"value 5'
    options = parse_kv(arguments)
    assert options == {"key1": "value1", "key2": "value 2", "key 3": "value 3", "key 4": "value 4", "with backslash": '\"value 5', "_raw_params": '"with backslash"=\\"value 5'}



# Generated at 2022-06-13 07:13:53.290727
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == dict(foo="bar")
    assert parse_kv("foo=\"bar\"") == dict(foo="bar")
    assert parse_kv("foo=\"bar baz\"") == dict(foo="bar baz")
    assert parse_kv("foo='bar'") == dict(foo="bar")
    assert parse_kv("foo='bar baz'") == dict(foo="bar baz")
    assert parse_kv("foo=bar baz") == dict(foo="bar baz")
    assert parse_kv("foo=bar", check_raw=True) == dict(foo="bar")
    assert parse_kv("foo=\"bar baz\"", check_raw=True) == dict(foo="bar baz")

# Generated at 2022-06-13 07:13:56.362479
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils import basic
    import doctest

    doctest.testmod(basic, verbose=False)
test_split_args()

# Generated at 2022-06-13 07:14:09.804342
# Unit test for function split_args

# Generated at 2022-06-13 07:14:24.314363
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:28.523159
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('arg1=foo arg2=bar') == {'arg1': u'foo', 'arg2': u'bar'}
    assert parse_kv('arg1=foo arg2=bar arg3=foo\ bar') == {'arg1': u'foo', 'arg2': u'bar', 'arg3': u'foo bar'}
    # escaped equals sign in argument
    assert parse_kv('arg1=foo arg2=bar\=foo arg3=foo\ bar') == {'arg1': u'foo', 'arg2': u'bar=foo', 'arg3': u'foo bar'}
    # escaped equals sign in argument, escaped space in value

# Generated at 2022-06-13 07:14:38.923603
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('foo') == {u'_raw_params': u'foo'}
    assert parse_kv('foo bar') == {u'_raw_params': u'foo bar'}
    assert parse_kv(' foo  bar ') == {u'_raw_params': u'foo  bar'}
    assert parse_kv(' foo  =  bar ') == {u'_raw_params': u'foo  =', u'bar': u''}
    assert parse_kv(' foo  =  bar ') == parse_kv('foo  =  bar')
    assert parse_kv('foo=bar') == {u'foo': u'bar'}

# Generated at 2022-06-13 07:14:46.404966
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("k1=v1 k2=v2") == {u'k1': u'v1', u'k2': u'v2'}
    assert parse_kv("k1='v1' k2='v2'") == {u'k1': u'v1', u'k2': u'v2'}
    assert parse_kv("k1=\"v1\" k2=\"v2\"") == {u'k1': u'v1', u'k2': u'v2'}
    assert parse_kv("k1=v1 k2=\"v2\" k3='v3'") == {u'k1': u'v1', u'k2': u'v2', u'k3': u'v3'}

# Generated at 2022-06-13 07:14:55.925538
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv('a=b c=d'))
    print(parse_kv('a="b c"'))
    print(parse_kv('a="b \\"c\\""'))
    print(parse_kv('a=b c="d e"'))
    print(parse_kv('a=b c=\'d e\''))
    print(parse_kv('a=b c="d \'e\'"'))
    print(parse_kv('a=b c="d \"e\""'))
    print(parse_kv('a=b c="d \\\\\\"e\\\\\\""'))
    print(parse_kv('a=b c="d e" f'))
    print(parse_kv('a=b c="d e" f', check_raw=True))



# Generated at 2022-06-13 07:15:03.400770
# Unit test for function parse_kv
def test_parse_kv():
    ''' validation test for parse_kv function '''
    from ansible.parsing.vault import VaultLib
    vault = VaultLib(None)
    ciphertext = vault.encrypt("foo\nbar\nbaz\n")

    base_kwargs = dict(
        argument_spec=dict(
            foo=dict(type='str'),
            bar=dict(type='int'),
            baz=dict(type='bool'),
            arg4=dict(type='list'),
            arg5=dict(type='dict'),
            arg6=dict(type='vault'),
        ),
        supports_check_mode=False,
    )

    # FIXME: add more test cases

# Generated at 2022-06-13 07:15:26.658235
# Unit test for function split_args

# Generated at 2022-06-13 07:15:37.606557
# Unit test for function split_args
def test_split_args():
    import sys
    import socket
    assert split_args(u"b=1 c=2") == [u'b=1', u'c=2']
    assert split_args(u"b=1   c=2") == [u'b=1', u'c=2']
    assert split_args(u"b=1\nc=2") == [u'b=1\n', u'c=2']
    assert split_args(u"b=1\n c=2") == [u'b=1\n', u'c=2']
    assert split_args(u"b=1 \\ c=2") == [u'b=1', u'c=2']
    assert split_args(u"b=1 \\ c=2") == [u'b=1', u'c=2']
   

# Generated at 2022-06-13 07:15:44.634223
# Unit test for function split_args

# Generated at 2022-06-13 07:15:53.189094
# Unit test for function split_args

# Generated at 2022-06-13 07:16:05.507835
# Unit test for function split_args
def test_split_args():
    # args with empty string
    assert split_args('') == []
    # simple args with no quotes
    assert split_args('foo bar') == ['foo', 'bar']
    # args on multiple lines, no quotes
    assert split_args('foo\nbar') == ['foo', 'bar']
    # args on multiple lines with spaces, no quotes
    assert split_args('foo\n   bar') == ['foo', 'bar']
    # args on multiple lines with spaces, no quotes
    assert split_args('foo\n   bar') == ['foo', 'bar']
    # args with a single-quoted string
    assert split_args("'foo bar' a=b") == ["'foo bar'", 'a=b']
    # args with a double-quoted string
    assert split_args('"foo bar" a=b')

# Generated at 2022-06-13 07:16:14.423379
# Unit test for function parse_kv
def test_parse_kv():
    test_command_line = "a=b c=d e='f g' h=i j=k"
    results = parse_kv(test_command_line)
    assert results['a'] == 'b'
    assert results['c'] == 'd'
    assert results['e'] == "f g"
    assert results['h'] == "i"
    assert results['j'] == "k"
    assert results.has_key('_raw_params') is False

# Code for splitting command line arguments was adopted from
# http://stackoverflow.com/questions/4356491/python-splitting-a-command-line-in-tokens-for-shlex-split-in-python-2-4
# Author: Andrew Moffat
# License: MIT


# Generated at 2022-06-13 07:16:23.741531
# Unit test for function split_args

# Generated at 2022-06-13 07:16:34.698971
# Unit test for function split_args

# Generated at 2022-06-13 07:16:48.408207
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('k1=v1 k2=v2') == {'k1': 'v1', 'k2': 'v2'}
    assert parse_kv('k1=v1 k2=v2 k3=v3') == {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    assert parse_kv('k1=v1 k2=v2 k3=v3 k4=v4 k5=v5') == {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}

# Generated at 2022-06-13 07:16:54.224403
# Unit test for function parse_kv
def test_parse_kv():
    test_result = parse_kv(args=u'arg1=value1 arg2=value2 arg3=value3')
    assert test_result[u'arg1'] == u'value1'
    assert test_result[u'arg2'] == u'value2'
    assert test_result[u'arg3'] == u'value3'
    assert u'_raw_params' not in test_result
