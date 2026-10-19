

# Generated at 2022-06-13 07:07:30.153278
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz=qux') == {'foo': 'bar', 'baz': 'qux'}
    assert parse_kv('foo=bar baz=qux blah') == {'foo': 'bar', 'baz': 'qux', '_raw_params': 'blah'}
    assert parse_kv('foo=bar baz=qux blah=') == {'foo': 'bar', 'baz': 'qux', 'blah': '', '_raw_params': ''}
    assert parse_kv('foo=bar baz=qux blah= arg1 arg2') == {'foo': 'bar', 'baz': 'qux', 'blah': '', '_raw_params': 'arg1 arg2'}

# Generated at 2022-06-13 07:07:39.613321
# Unit test for function split_args

# Generated at 2022-06-13 07:07:45.886892
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a=b c='foo bar'") == [u'a=b', u"c='foo bar'"]
    assert split_args(u"a=b c=\"foo bar\"") == [u'a=b', u'c="foo bar"']
    assert split_args(u"a=b c='foo bar' d='foo bar'") == [u'a=b', u'c=\'foo bar\'', u"d='foo bar'"]
    assert split_args(u"a=b c=\"foo bar\" d=\"foo bar\"") == [u'a=b', u'c="foo bar"', u'd="foo bar"']

# Generated at 2022-06-13 07:07:55.638134
# Unit test for function split_args
def test_split_args():
    # Test of split args with an ordinary string
    result = split_args('hello world foo bar')
    assert result == ['hello', 'world', 'foo', 'bar']

    # Test of split args with an ordinary jinja2 string
    result = split_args('i am {{ foo }}, he is {{ bar }}')
    assert result == ['i', 'am', '{{', 'foo', '}}', ',', 'he', 'is', '{{', 'bar', '}}']

    result = split_args('{{foo | bar}}')
    assert result == ['{{', 'foo', '|', 'bar', '}}']

    result = split_args('{{ foo | bar }}')
    assert result == ['{{', 'foo', '|', 'bar', '}}']

    result = split_args('{{ foo.bar }}')

# Generated at 2022-06-13 07:08:03.437722
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=1 bar=2') == dict(foo='1', bar='2')
    assert parse_kv('foo="1 \"2" bar=2') == dict(foo='1 "2', bar='2')
    assert parse_kv('foo="1 \"2" bar=2') == dict(foo='1 "2', bar='2')
    assert parse_kv('foo="1 \"2" bar=2', check_raw=True) == dict(foo='1 "2', bar='2', _raw_params='foo="1 \"2" bar=2')
    assert parse_kv('foo="1 \"2" bar=2', check_raw=True) == dict(foo='1 "2', bar='2', _raw_params='foo="1 \"2" bar=2')

# Generated at 2022-06-13 07:08:11.951574
# Unit test for function parse_kv
def test_parse_kv():
    assert({u'foo': u'bar', u'bam': u'baz'} == parse_kv('foo="bar" bam=baz'))
    assert({u'foo': u'bar baz', u'bam': u'baz'} == parse_kv('foo="bar baz" bam=baz'))
    assert({u'foo': u'bar', u'bam': u'baz bax'} == parse_kv('foo=bar bam="baz bax"'))

# Generated at 2022-06-13 07:08:24.428290
# Unit test for function parse_kv
def test_parse_kv():
    # these tests are designed to be run with python2, but
    # in the future they should also be run with py3k
    # as unicode issues are likely to be uncovered
    assert dict(parse_kv('foo=bar')) == dict(foo=u'bar')
    assert dict(parse_kv('foo=bar baz="foo bar"')) == dict(foo=u'bar', baz=u'foo bar')
    assert dict(parse_kv('foo="bar baz" baz=blah')) == dict(foo='bar baz', baz=u'blah')
    assert dict(parse_kv('foo="bar baz" baz=blah')) == dict(foo='bar baz', baz=u'blah')

# Generated at 2022-06-13 07:08:35.828789
# Unit test for function parse_kv
def test_parse_kv():
    def _run(cmdline, expected_options, expected_params=None, check_raw=False,
             no_conversion=False):
        try:
            options = parse_kv(cmdline, check_raw=check_raw, no_conversion=no_conversion)
        except AnsibleParserError as e:  # pragma: no cover
            # only here for testing
            print('Error: {0}'.format(e.message))
            options = {}
        actual_options = sorted(options.keys())
        expected_options = sorted(expected_options)
        assert actual_options == expected_options, '\ngot: %s\nwant: %s' % (actual_options, expected_options)

        if expected_params is not None:
            assert options[u'_raw_params'] == expected_params
       

# Generated at 2022-06-13 07:08:49.193953
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('name: value') == {u'name': u'value'}

# Generated at 2022-06-13 07:09:00.873750
# Unit test for function parse_kv
def test_parse_kv():
    res = parse_kv('hello=world')
    assert res == {'hello': 'world'}
    res = parse_kv('hello="world"')
    assert res == {'hello': 'world'}
    res = parse_kv('hello="world" foo=bar')
    assert res == {'hello': 'world', 'foo': 'bar'}
    res = parse_kv('hello=world "foo=bar"')
    assert res == {'hello': 'world', u'_raw_params': '"foo=bar"'}
    res = parse_kv('hello=world "foo=bar" biz=baz')
    assert res == {'hello': 'world', u'biz': 'baz', u'_raw_params': '"foo=bar"'}

# Generated at 2022-06-13 07:09:38.786433
# Unit test for function split_args

# Generated at 2022-06-13 07:09:49.711598
# Unit test for function split_args
def test_split_args():
    import json

    def test(input, expected_output):
        output = split_args(input)
        assert output == expected_output, "For input: '%s' expected: %s but got: %s" % (input, json.dumps(expected_output), json.dumps(output))

    # no quotes
    test('a=b c=d', ['a=b', 'c=d'])

    # simple quoted key
    test('"a=b" "c=d"', ['a=b', 'c=d'])

    # quoted key with spaces
    test('"a= b" "c = d"', ['a= b', 'c = d'])

    # quoted key with escaped quotes
    test('a=\\"b c=\\"d', ['a="b', 'c="d'])

   

# Generated at 2022-06-13 07:09:58.519557
# Unit test for function split_args
def test_split_args():
    import sys
    import json

# Generated at 2022-06-13 07:10:08.354100
# Unit test for function split_args
def test_split_args():
    '''
    Test the split_args() function which is used by the command/shell
    invocation to properly match complex jinja2/quoted args.

    Due to the large number of specific cases, the generic test method
    here seems like the best method to ensure stability.
    '''

    def _test_split(test_input, expected_output, test_idx):
        '''
        This function runs a single test by calling split_args() on the input,
        and comparing the output to the expected output. If the test fails,
        it returns a descriptive error message or None if the test succeeds
        '''

        result = split_args(test_input)

# Generated at 2022-06-13 07:10:13.434427
# Unit test for function parse_kv
def test_parse_kv():
    import doctest
    # FIXME: some of these need to get backslash escapes added to them
    results = doctest.testmod(parse_kv)
    if results[0] > 0:
        raise AssertionError("parse_kv() failed")



# Generated at 2022-06-13 07:10:25.126521
# Unit test for function parse_kv
def test_parse_kv():
    # Test basic parsing
    kv = parse_kv('key1=value1 key2=value2')
    assert kv['key1'] == 'value1'
    assert kv['key2'] == 'value2'

    # Test mixed quoting
    kv = parse_kv('key1=value1 key2="value2" key3=\'value3')
    assert kv['key1'] == 'value1'
    assert kv['key2'] == 'value2'
    assert kv['key3'] == 'value3'

    # Test escaping
    kv = parse_kv('key1=value1 key2="value2 value2" key3=\'value3 value3\'')
    assert kv['key1'] == 'value1'
    assert kv['key2'] == 'value2 value2'

# Generated at 2022-06-13 07:10:35.322297
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv("app=blah block=foo")
    assert type(options) == dict
    assert len(options.keys()) == 2
    assert options['app'] == 'blah'
    assert options['block'] == 'foo'

    options = parse_kv("app=blah block=foo rest")
    assert type(options) == dict
    assert len(options.keys()) == 3
    assert options['app'] == 'blah'
    assert options['block'] == 'foo'
    assert options['_raw_params'] == 'rest'

    options = parse_kv("app=blah block=foo rest", check_raw=True)
    assert type(options) == dict
    assert len(options.keys()) == 4
    assert options['app'] == 'blah'

# Generated at 2022-06-13 07:10:43.350824
# Unit test for function split_args

# Generated at 2022-06-13 07:10:53.656299
# Unit test for function parse_kv
def test_parse_kv():
    opts = parse_kv("key=value key2=value2")
    assert(opts['key'] == 'value')
    assert(opts['key2'] == 'value2')
    assert(len(opts) == 2)

    opts = parse_kv("key=value key2=value2 --extra-args")
    assert(opts['key'] == 'value')
    assert(opts['key2'] == 'value2')
    assert(opts['_raw_params'] == "--extra-args")
    assert(len(opts) == 3)

    opts = parse_kv("key=\"value=1\" key2=value2 --extra-args")
    assert(opts['key'] == 'value=1')
    assert(opts['key2'] == 'value2')

# Generated at 2022-06-13 07:10:59.527914
# Unit test for function split_args

# Generated at 2022-06-13 07:11:15.979296
# Unit test for function split_args
def test_split_args():

    # test for '\n' being preserved
    s = '''
'''.strip()
    res = split_args(s)
    # print(res)
    assert res == ['']

    # test for ' ' being preserved
    s = '''
    
'''.strip()
    res = split_args(s)
    # print(res)
    assert res == ['', '']

    s = '''
     a     b    
'''.strip()
    res = split_args(s)
    # print(res)
    assert res == ['', 'a', 'b', '']

    s = '''
     a     b
c d    e   
'''.strip()
    res = split_args(s)
    # print(res)

# Generated at 2022-06-13 07:11:26.937750
# Unit test for function split_args
def test_split_args():
    '''
    This test is directly based on the code of the split_args() function.
    The input `args` string is used to generate a list of tokens, and
    the function is called to generate a list of parsed tokens from `args`.
    These lists of tokens are then compared.
    '''
    import json
    #
    # parameters for this test
    #
    # list of input strings to be tested

# Generated at 2022-06-13 07:11:40.391808
# Unit test for function parse_kv
def test_parse_kv():
    # Test basic functionality
    print('Testing parse_kv...')
    assert(parse_kv('count=45') == {'count': '45'})
    assert(parse_kv('count=45', True) == {'count': '45'})
    assert(parse_kv('count=45, size=3') == {'count': '45', 'size': '3'})
    assert(parse_kv('count=45, size=3', True) == {'count': '45', 'size': '3'})

    # Test escaped quotes and equals in the middle of the string
    assert(parse_kv('count=45, key="fo=o", size=3') == {'count': '45', 'key': 'fo=o', 'size': '3'})

# Generated at 2022-06-13 07:11:50.193189
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar baz=quux') == {'foo': "bar", 'baz': "quux"}
    assert parse_kv('foo="bar" baz=quux') == {'foo': "bar", 'baz': "quux"}
    assert parse_kv("foo='bar' baz=quux") == {'foo': "bar", 'baz': "quux"}
    assert parse_kv("foo={{bar}}") == {'foo': "{{bar}}"}
    assert parse_kv('foo="bar" baz="""quux"""') == {'foo': "bar", 'baz': "quux"}
    assert parse_kv("foo='bar' baz='\"quux\"'") == {'foo': "bar", 'baz': "\"quux\""}

# Generated at 2022-06-13 07:12:01.442968
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=1 b="2 3" c=4') == {u'a': u'1', u'c': u'4', u'b': u'2 3'}
    assert parse_kv(u'a=1 b=\'2 3\' c=4') == {u'a': u'1', u'c': u'4', u'b': u'2 3'}
    assert parse_kv(u'a=1 b=\'2\'\'3\' c=4') == {u'a': u'1', u'c': u'4', u'b': u"2'3"}

# Generated at 2022-06-13 07:12:08.877743
# Unit test for function split_args

# Generated at 2022-06-13 07:12:16.773165
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:30.555249
# Unit test for function parse_kv
def test_parse_kv():
    args = "executable=/bin/foo chdir=/tmp cat /path/to/file"
    assert parse_kv(args, check_raw=True) == {
        u'executable': u'/bin/foo',
        u'chdir': u'/tmp',
        u'_raw_params': u'cat /path/to/file'}

    args = "executable=/bin/foo abc='def ghi' jkl='a=b c=d'"
    assert parse_kv(args, check_raw=True) == {
        u'executable': u'/bin/foo',
        u'abc': u'def ghi',
        u'jkl': u'a=b c=d'}


# Generated at 2022-06-13 07:12:40.616419
# Unit test for function split_args
def test_split_args():
    assert split_args(u'a') == [u'a']
    assert split_args(u'a b') == [u'a', u'b']
    assert split_args(u'a\\ b') == [u'ab']
    assert split_args(u'a\\\nb') == [u'a\\', u'nb']
    assert split_args(u'  a      b\n  c  d') == [u'a', u'b\n  c', u'd']
    assert split_args(u"{{a}} {{b}}") == [u'{{a}}', u'{{b}}']
    assert split_args(u"{{a}} {{b}} {% c %}") == [u'{{a}}', u'{{b}}', u'{%', u'c', u'%}']


# Generated at 2022-06-13 07:12:50.830878
# Unit test for function split_args
def test_split_args():
    '''
    unit tests for function split_args
    '''
    def assert_result(input_str, expected_result):
        '''
        helper function to verify the result of split_args
        '''
        result = split_args(input_str)
        if result != expected_result:
            sys.stderr.write('ERROR:\n\tinput: %s\nexpected: %s\ngot: %s\n' % (input_str, expected_result, result))
            raise SystemExit()


# Generated at 2022-06-13 07:13:02.373934
# Unit test for function split_args
def test_split_args():
    print("Testing split_args...")
    test_pairs = [ ("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"'])]
    for args_in, expect in test_pairs:
        result = split_args(args_in)
        if result != expect:
            print("split_args('%s') returned %s and should have returned %s" % (args_in, result, expect))


# Generated at 2022-06-13 07:13:08.517267
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u'a=1 b=2 c') == {u'a': u'1', u'b': u'2', u'_raw_params': u'c'}
    assert parse_kv(u'a=1 b=2 c=') == {u'a': u'1', u'b': u'2', u'_raw_params': u'c='}
    assert parse_kv(u"a=1 b='foo'") == {u'a': u'1', u'b': u"'foo'"}

# Generated at 2022-06-13 07:13:19.745942
# Unit test for function split_args
def test_split_args():
    # Tests that an index error is raised when an argument string is incorrectly
    # terminated.
    try:
        split_args(u"a=")
        assert False
    except IndexError as e:
        assert type(e) == IndexError

    # Tests that a value error is raised when the argument string contains a
    # quote character that is unterminated.
    try:
        split_args(u'"foo" "bar')
        assert False
    except ValueError as e:
        assert u"no closing quotation" in str(e).lower()

    # Tests that a quoted string that contains spaces is correctly reassembled
    # when it was split by whitespace.
    assert split_args(u'"foo bar"') == [u'"foo bar"']

    # Tests that a quoted string that contains escaped quotes is correctly reassembled
    # when it was split

# Generated at 2022-06-13 07:13:25.107111
# Unit test for function split_args
def test_split_args():
    import sys
    import traceback
    # Variables that are used in the test cases, in some cases the
    # variables will be mutated. To reduce the number of times that a
    # variable will be initialized, it is initialized here rather than
    # in the test case that uses it.
    # This allows the same variables to be used in multiple test cases.
    args_str = None
    params_list = None

    for idx, test_case in enumerate(TEST_CASES):
        # Set the test-specific variables to their initial values
        args_str, params_list = test_case[:2]

        # Verify that a TypeError exception is raised if the args
        # argument is of the wrong type.
        wrong_types = (None, 123, 1.23, [], test_case)

# Generated at 2022-06-13 07:13:34.963439
# Unit test for function split_args
def test_split_args():
    print("\n===== split_args =====")

# Generated at 2022-06-13 07:13:40.238432
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv(u'a=\u4e02 b=2') == {u'a': u'\u4e02', u'b': u'2'}
    assert parse_kv(u'a="quoted string" b=2') == {u'a': u'"quoted string"', u'b': u'2'}
    assert parse_kv(u'a="quote\"d string" b=2') == {u'a': u'"quote\"d string"', u'b': u'2'}

# Generated at 2022-06-13 07:13:49.907777
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(args='a="b b" c="d d"') == {u'a': u'b b', u'c': u'd d'}
    assert parse_kv(args='a=b b c=d d') == {u'a': u'b b', u'c': u'd d'}
    assert parse_kv(args='a=b=c\\ d e="f\\"g"') == {u'a': u'b=c d', u'e': u'f"g'}
    assert parse_kv(args='a="b" c="d"') == {u'a': u'b', u'c': u'd'}

# Generated at 2022-06-13 07:14:04.420492
# Unit test for function split_args
def test_split_args():
    import re
    # Test cases with passing output

# Generated at 2022-06-13 07:14:11.977690
# Unit test for function parse_kv
def test_parse_kv():
    def _test_kv(arg_string, expected_result):
        actual_result = parse_kv(arg_string)
        assert actual_result == expected_result, u"arg_string=%s, actual_result=%s" % (arg_string, actual_result)

    # Examples from: https://docs.python.org/2/library/string.html#format-string-syntax
    _test_kv(u"a=1, b=2, c=3", {u"a": u"1", u"b": u"2", u"c": u"3"})
    _test_kv(u'a="1", b="2", c="3"', {u"a": u"1", u"b": u"2", u"c": u"3"})
    _test_k

# Generated at 2022-06-13 07:14:20.082114
# Unit test for function parse_kv
def test_parse_kv():
    args = "a=b c='d e' f=g 'h i'=\"j k\""
    result = parse_kv(args)
    assert result == {u'a': u'b', u'f': u'g', u'c': u'\'d e\'', u'h i': u'"j k"', '_raw_params': u"a=b c='d e' f=g 'h i'=\"j k\""}



# Generated at 2022-06-13 07:14:36.344734
# Unit test for function split_args
def test_split_args():
    # trivial cases
    assert split_args("ec2_group=foo") == ['ec2_group=foo']
    assert split_args("") == []

    params = split_args("ec2_group=foo,ec2_group=bar,ec2_group=baz")
    assert params[0] == 'ec2_group=foo,ec2_group=bar,ec2_group=baz'
    assert params[1:] == []

    # test escaping inside a quoted string
    params = split_args("cmd=\'a b c\'")
    assert params == ['cmd=\'a b c\'']

    params = split_args("cmd=a\\ b\\ c")
    assert params == ['cmd=a b c']

    # test quoted strings with whitespace inside

# Generated at 2022-06-13 07:14:44.157182
# Unit test for function split_args

# Generated at 2022-06-13 07:14:50.176228
# Unit test for function parse_kv
def test_parse_kv():
    # basic test
    assert parse_kv("'a=b c='d'") == dict(a="b", c="d")
    assert parse_kv('"a=b c=\'d\'"') == dict(a="b", c="d")
    assert parse_kv("a=b c=d e=f") == dict(a="b", c="d", e="f")

    # test quoting
    assert parse_kv("foo=bar") == dict(foo="bar")
    assert parse_kv("foo='bar'") == dict(foo="bar")
    assert parse_kv("foo='bar baz'") == dict(foo="bar baz")
    assert parse_kv('foo="bar"') == dict(foo="bar")

# Generated at 2022-06-13 07:14:55.634657
# Unit test for function parse_kv
def test_parse_kv():
    assert(parse_kv('key1=value1') == {u'key1': u'value1'})
    assert(parse_kv('key1=value1 key2=value2 key3=value3') == {u'key1': u'value1', u'key2': u'value2', u'key3': u'value3'})
    assert(parse_kv('') == {})
    assert(parse_kv(None) == {})


# Generated at 2022-06-13 07:15:03.133382
# Unit test for function parse_kv
def test_parse_kv():
    '''
    THIS IS A UNIT TESTS for the parse_kv() function.
    '''
    import os
    import tempfile
    tf = os.path.join(tempfile.gettempdir(),'test_parse_kv.txt')
    if os.path.exists(tf): os.remove(tf)
    fw = open(tf,'w')

# Generated at 2022-06-13 07:15:12.116796
# Unit test for function split_args
def test_split_args():
    def t(args, expected):
        actual = split_args(args)
        if actual == expected:
            print('+', args)
        else:
            print('!', args)
            print('  expected:', expected, sep='')
            print('  actual:  ', actual, sep='')
    t('', [])
    t('foo bar', ['foo', 'bar'])
    t('foo bar baz', ['foo', 'bar', 'baz'])
    t('foo "bar baz"', ['foo', '"bar baz"'])
    t('foobar', ['foobar'])
    t('foo bar\\', ['foo', 'bar\\'])
    t('foo bar\\\nbaz', ['foo', 'bar\\\n', 'baz'])

# Generated at 2022-06-13 07:15:22.927197
# Unit test for function parse_kv
def test_parse_kv():
    args = u'a=b c="d e" f="g\'h" i="""j k"""'
    options = parse_kv(args)
    assert len(options) == 4
    assert options['a'] == u'b'
    assert options['c'] == u'd e'
    assert options['f'] == u"g'h"
    assert options['i'] == u'j k'

    args = u'a=b \'c=d e\' f="g\'h" i="""j k"""'
    options = parse_kv(args)
    assert len(options) == 4
    assert options['a'] == u'b'
    assert options['c'] == u'd e'
    assert options['f'] == u"g'h"
    assert options['i'] == u'j k'

    args

# Generated at 2022-06-13 07:15:31.428071
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for the split_args function
    '''
    FAILED = False

    def _test(x, expected, test_name=None):
        global FAILED  # pylint: disable=global-statement
        res = split_args(x)
        if res != expected:
            print(u"ERROR: split_args failed on {0}\nEXPECTED:\n{1} (type: {2})\nACTUAL:\n{3} (type: {4})".format(x, expected, type(expected), res, type(res)))
            FAILED = True
        else:
            print(u"SUCCESS: split_args succeeded on input {0}".format(x) +
                  ('' if test_name is None else u" [{0}]".format(test_name)))



# Generated at 2022-06-13 07:15:41.084661
# Unit test for function parse_kv
def test_parse_kv():
    result = parse_kv('a=b c=d')
    assert result == dict(a='b', c='d')

    result = parse_kv('a=b c=d e')
    assert result == dict(a='b', c='d', _raw_params='e')

    result = parse_kv('a=b c=d e', check_raw=False)
    assert result == dict(a='b', c='d')

    result = parse_kv('a=b c=d e=f x=y')
    assert result == dict(a='b', c='d', e='f', x='y', _raw_params='')

    result = parse_kv('a=b c=d e=f x=y', check_raw=False)

# Generated at 2022-06-13 07:15:50.685045
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('one=1 two=2 three=3') == {'one': '1', 'two': '2', 'three': '3'}
    assert parse_kv('one=1 two=2 three=3 x=') == {'one': '1', 'two': '2', 'three': '3', 'x': ''}
    assert parse_kv('one=1 two=2 three=3 x= key_without_value') == {'one': '1', 'two': '2', 'three': '3', 'x': '', '_raw_params': 'key_without_value'}

# Generated at 2022-06-13 07:16:15.553650
# Unit test for function split_args
def test_split_args():
    tests = dict(shell='a=b c="foo bar"',
                 args_list=['a=b', 'c="foo bar"'])
    assert split_args(tests['shell']) == tests['args_list']

    tests = dict(shell='a="foo bar" b',
                 args_list=['a="foo bar"', 'b'])
    assert split_args(tests['shell']) == tests['args_list']

    tests = dict(shell='a="foo bar" b="foo\nbar" c',
                 args_list=['a="foo bar"', 'b="foo\nbar"', 'c'])
    assert split_args(tests['shell']) == tests['args_list']


# Generated at 2022-06-13 07:16:25.367000
# Unit test for function split_args

# Generated at 2022-06-13 07:16:31.949212
# Unit test for function split_args

# Generated at 2022-06-13 07:16:37.327895
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:49.556170
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"foo=bar", False) == {u"foo": u"bar"}
    assert parse_kv(u"foo=bar", True) == {u"foo": u"bar"}
    assert parse_kv(u"foo = bar", False) == {u"foo": u"bar"}
    assert parse_kv(u"foo = bar", True) == {u"foo": u"bar"}
    assert parse_kv(u"foo='bar baz'", False) == {u"foo": u"bar baz"}
    assert parse_kv(u"foo='bar baz'", True) == {u"foo": u"bar baz"}
    assert parse_kv(u"foo = 'bar baz'", False) == {u"foo": u"bar baz"}
   

# Generated at 2022-06-13 07:16:57.523170
# Unit test for function split_args
def test_split_args():
    # test empty input
    assert split_args('') == []

    # test simple case
    options = split_args('hello')
    assert len(options) == 1
    assert options[0] == 'hello'

    # test simple options
    options = split_args('a=b c=d')
    assert len(options) == 2
    assert options[0] == 'a=b'
    assert options[1] == 'c=d'

    # test options with spaces
    options = split_args('a=b c=foo bar')
    assert len(options) == 2
    assert options[0] == 'a=b'
    assert options[1] == 'c=foo bar'

    options = split_args('a=b c="foo bar"')
    assert len(options) == 2