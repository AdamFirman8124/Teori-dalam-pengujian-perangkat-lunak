

# Generated at 2022-06-13 04:31:15.923209
# Unit test for function split_args

# Generated at 2022-06-13 04:31:28.695937
# Unit test for function is_quoted
def test_is_quoted():
    quoted_data = '"This is quoted"'
    assert is_quoted(quoted_data) is True
    
    unquoted_data = 'This is not quoted'
    assert is_quoted(unquoted_data) is False
    
    quoted_data_single_quote = "'This is quoted'"
    assert is_quoted(quoted_data_single_quote) is True

    partial_quoted_data = '"This is part quoted'
    assert is_quoted(partial_quoted_data) is False
    
    empty_quoted_data = '""'
    assert is_quoted(empty_quoted_data) is True
    
    empty_single_quoted_data = "''"
    assert is_quoted(empty_single_quoted_data) is True
    
    no_

# Generated at 2022-06-13 04:31:35.790023
# Unit test for function split_args

# Generated at 2022-06-13 04:31:44.133594
# Unit test for function split_args
def test_split_args():
    # Test simple args
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo', 'bar']
    assert split_args('a=b c="foo bar\\') == ['a=b', 'c="foo bar\\']
    assert split_args('a=b c="foo bar\\"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar\\" d=e') == ['a=b', 'c="foo bar"', 'd=e']
    assert split_args('a=b c=\\"foo bar"') == ['a=b', 'c="foo', 'bar"']
    assert split_args

# Generated at 2022-06-13 04:31:49.056294
# Unit test for function unquote
def test_unquote():
    assert unquote('') == ''
    assert unquote('foo') == 'foo'
    assert unquote('foo"') == 'foo"'
    assert unquote('"foo') == '"foo'
    assert unquote('"foo"') == 'foo'
    assert unquote("'foo'") == 'foo'
    assert unquote('"foo bar"') == 'foo bar'
    assert unquote('"foo \"bar\" bam"') == 'foo "bar" bam'
    assert unquote("'foo bar'") == 'foo bar'
    assert unquote("'foo \"bar\" bam'") == 'foo "bar" bam'
    assert unquote("'foo ' 'bar'") == "foo 'bar"
    assert unquote("\"foo \" 'bar'") == "foo 'bar"

# Generated at 2022-06-13 04:32:01.096768
# Unit test for function split_args
def test_split_args():

    # NOTE: these tests will fail if the code is changed such that any of the tests
    # should be returning something other than what they currently are.
    # all the tests take the form [args, expected result]

    # Test 1: test simple string
    cmd = "echo hello world"
    result = split_args(cmd)
    ex = ["echo", "hello", "world"]
    assert result == ex, "Depth 0 split failed, got: %s" % result

    # 2: test simple string with a quoted arg that hasn't been split
    cmd = "echo 'hello world'"
    result = split_args(cmd)
    ex = ["echo", "'hello world'"]
    assert result == ex, "Depth 0 split failed, got: %s" % result

    # 3: test simple string with a quoted arg that needs to be reassembled
    cmd

# Generated at 2022-06-13 04:32:05.231720
# Unit test for function unquote
def test_unquote():
    assert unquote("test") == "test"
    assert unquote("\"test\"") == "test"
    assert unquote("\"test") == "\"test"
    assert unquote("test\"") == "test\""
    assert unquote("\"te\"st\"") == "te\"st"


# Generated at 2022-06-13 04:32:15.978838
# Unit test for function unquote
def test_unquote():
    # Test for 2 cases: unquoted string and quoted string
    assert unquote("") == ""
    assert unquote("a") == "a"
    assert unquote("a\"") == "a\""
    assert unquote("\"a") == "\"a"
    assert unquote("\"a\"") == "a"
    assert unquote("\"a\"b") == "\"a\"b"
    assert unquote("\"a\"b\"") == "\"a\"b\""
    assert unquote("\"a\"\"\"b\"") == "\"ab"
    assert unquote("\"a\"\" \"\"b\"") == "\"a b"
    assert unquote("\"a'b\"") == "a'b"

    # The following should raise an exception

# Generated at 2022-06-13 04:32:22.174991
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello, world"') == True
    assert is_quoted("'hello, world'") == True
    assert is_quoted('"hello, world') == False
    assert is_quoted("hello, world'") == False
    assert is_quoted('hello, world') == False


# Generated at 2022-06-13 04:32:25.063715
# Unit test for function is_quoted
def test_is_quoted():
    if is_quoted('"test1"'):
        return
    raise Exception("Expected quoted string")


# Generated at 2022-06-13 04:32:40.880767
# Unit test for function split_args
def test_split_args():
    ''' This is used when testing the module as a whole and module.params is used as
        the test data. It was not written as a true unit test.
    '''
    print(split_args(unicode(module.params)))

# Generated at 2022-06-13 04:32:50.973564
# Unit test for function split_args
def test_split_args():
    """
    Test function split_args to make sure it is translating args to list of args properly.
    """

# Generated at 2022-06-13 04:33:01.765585
# Unit test for function split_args

# Generated at 2022-06-13 04:33:10.732205
# Unit test for function split_args
def test_split_args():
    _test_split_args_check('''
    foo=bar
    ''', ['''foo=bar'''])
    _test_split_args_check('''
    foo=bar \\
    baz=qux
    ''', ['''foo=bar baz=qux'''])
    _test_split_args_check('''
    foo=bar
    baz=qux
    ''', ['''foo=bar''',
          '''baz=qux'''])
    _test_split_args_check('''
    foo=bar
    baz=qux \\
    fred=jake
    ''', ['''foo=bar''',
          '''baz=qux fred=jake'''])

# Generated at 2022-06-13 04:33:16.046078
# Unit test for function split_args
def test_split_args():
    def _test_args(to_test, expect):
        result = split_args(to_test)
        if expect != result:
            print("%s != %s" % (expect, result))
            raise Exception("split_args test failed")

    _test_args("a=1", ['a=1'])
    _test_args("a=1 b=2", ['a=1', 'b=2'])
    _test_args("a=1\nb=2", ['a=1\n', 'b=2'])
    _test_args("a=1 b=\"foo bar\"", ['a=1', 'b="foo bar"'])

    _test_args("a=\"{{ foo }}\"", ['a="{{ foo }}"'])

# Generated at 2022-06-13 04:33:29.054492
# Unit test for function split_args
def test_split_args():
    '''
    Make sure we split args in the same way as AnsibleModule did
    before it got updated to use this function.
    '''

# Generated at 2022-06-13 04:33:40.232833
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar" d') == ['a=b', 'c="foo bar"', 'd']
    assert split_args('a=b c="foo bar" "d e"') == ['a=b', 'c="foo bar"', '"d e"']
    assert split_args('a=b c="foo bar" "d=e"') == ['a=b', 'c="foo bar"', '"d=e"']
    assert split_args('a=b c="foo bar" "d=e f"') == ['a=b', 'c="foo bar"', '"d=e f"']

# Generated at 2022-06-13 04:33:52.280995
# Unit test for function split_args
def test_split_args():
    '''
    This is a test method for the function split_args listed above.
    It simply calls the function with a list of test cases and
    iterates over the results. Test cases are tuples with the following
    format:
        * args string
        * expected number of params
        * list of expected params
    '''


# Generated at 2022-06-13 04:34:02.534913
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args
    '''
    # Test simple case
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Test line continuation
    assert split_args('a=b c="foo\\\nbar"') == ['a=b', 'c="foo\\\nbar"']

    # Test with quotes in an argument
    assert split_args('a="foo bar" b="quoted \\"thing\\"" c=\'foo bar\' d=\'quoted \\\'thing\\\'\'') == ['a="foo bar"', 'b="quoted \\"thing\\""', 'c=\'foo bar\'', "d='quoted \\'thing\\''"]

    # Test with a jinja2 block in an argument
    assert split_

# Generated at 2022-06-13 04:34:11.176859
# Unit test for function split_args

# Generated at 2022-06-13 04:34:38.225485
# Unit test for function split_args
def test_split_args():
    # double quotes (")
    args = 'a=b c="d e"'
    params = split_args(args)
    assert params == [u"a=b", u"c=\"d e\""]

    args = '"a b c"'
    params = split_args(args)
    assert params == [u"\"a b c\""]

    args = '""'
    params = split_args(args)
    assert params == [u"\"\""]

    args = '"\\\""'
    params = split_args(args)
    assert params == [u"\"\\\"\""]

    args = 'a=b c="d\"e"'
    params = split_args(args)
    assert params == [u"a=b", u"c=\"d\\\"e\""]

    # single quotes (')
    args

# Generated at 2022-06-13 04:34:45.875575
# Unit test for function split_args
def test_split_args():
    import json

    def do_test(input_string, expected):
        result = split_args(input_string)
        if json.dumps(result) != json.dumps(expected):
            print("input_string:      " + input_string)
            print("expected:          " + json.dumps(expected))
            print("result:            " + json.dumps(result))
            raise Exception("split_args test failed")

    do_test('a=b', ['a=b'])
    do_test('a=b c="foo bar"', ['a=b', 'c="foo bar"'])
    do_test('a={{x}} "c={{y}}"', ['a={{x}}', '"c={{y}}"'])

# Generated at 2022-06-13 04:34:57.165626
# Unit test for function split_args
def test_split_args():
    ''' unit test for the split_args function '''

    # the args we're going to test with
    # the expected result is the last item in each of these

# Generated at 2022-06-13 04:35:05.961732
# Unit test for function split_args
def test_split_args():
    args = "ansible_ssh_user='foo bar' colons:in:it arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14 arg15 arg16 arg17 arg18 arg19 arg20 arg21 arg22 arg23 arg24 arg25 arg26 foo={{ bar }} arg27 arg28 arg29 arg30 arg31 arg32 arg33 arg34 arg35 arg36 arg37 arg38 arg39"
    results = split_args(args)
    assert len(results) == 44, results
    assert results[0] == "ansible_ssh_user='foo bar'", results[0]

# Generated at 2022-06-13 04:35:10.385705
# Unit test for function split_args
def test_split_args():
    ''' simple unit test for function split_args '''
    # simple split test
    assert split_args('a=int') == ['a=int']
    # test split in jinja2 block
    assert split_args('a={{ b }}') == ['a={{', 'b', '}}']
    # test split in jinja2 block with quotes
    assert split_args('a={{ "b" }}') == ['a={{', '"b"', '}}']
    # test split in quotes
    assert split_args('a="b c"') == ['a="b c"']
    # test split in quotes and in jinja2 block
    assert split_args('a="{{ b }} c"') == ['a="{{', 'b', '}} c"']
    # test unbalanced quotes

# Generated at 2022-06-13 04:35:21.229272
# Unit test for function split_args
def test_split_args():
    # Test 'simple' splitting
    test_input = "foo=bar baz='qux quux'"
    expected_result = ['foo=bar', 'baz=qux quux']
    result = split_args(test_input)
    assert result == expected_result, "expected '%s', got '%s'" % (expected_result, result)

    # Check proper depth handling
    test_input = '''foo=bar baz='qux quux' quuux="corge grault" garply="{{ waldo }}" plugh="{{ fred }}"  {{ xyzzy }}="thud"'''

# Generated at 2022-06-13 04:35:31.810707
# Unit test for function split_args
def test_split_args():
    # 1) example input/output from module_utils/argspec.py
    args = 'a=b c="foo bar"'
    res = split_args(args)
    assert(res == ['a=b', 'c="foo bar"'])

    # 2) real-life example:
    #      "df -h --total | awk '/^total/ {print $2}'" <-- note: no spaces around the pipe
    #  --> ['df -h --total', '|', "awk '/^total/ {print $2}'"]
    args = "df -h --total | awk '/^total/ {print $2}'"
    res = split_args(args)
    assert(res == ['df -h --total', '|', "awk '/^total/ {print $2}'"])

    # 3) test that whites

# Generated at 2022-06-13 04:35:41.050662
# Unit test for function split_args
def test_split_args():
    def split_and_rebuild(args):
        return " ".join(split_args(args))
    assert split_and_rebuild("a=b c='d e' f=\"g h\"") == "a=b c='d e' f=\"g h\""
    assert split_and_rebuild("a=\"b\"") == "a=\"b\""
    assert split_and_rebuild("a=\"b c' d e'\"") == "a=\"b c' d e'\""
    assert split_and_rebuild("a=\"b c' d e'\" f='g h'") == "a=\"b c' d e'\" f='g h'"

# Generated at 2022-06-13 04:35:47.164223
# Unit test for function split_args
def test_split_args():
    x = 'a=b c="foo bar"'
    assert split_args(x) == ['a=b', 'c="foo bar"']

    x = 'a="foo bar"'
    assert split_args(x) == ['a="foo bar"']

    x = 'a=b c="foo\' bar"'
    assert split_args(x) == ['a=b', 'c="foo\' bar"']

    x = 'a=b c="foo\' bar"'
    assert split_args(x) == ['a=b', 'c="foo\' bar"']

    x = 'a=b c="foo\' bar"'
    assert split_args(x) == ['a=b', 'c="foo\' bar"']

    x = 'a=b c="foo\' bar"'

# Generated at 2022-06-13 04:35:54.497848
# Unit test for function split_args
def test_split_args():
    ''' basic tests for function ansible.utils.split_args '''
    # no whitespace
    assert split_args('foo') == ['foo']
    # no whitespace, multiple params
    assert split_args('foo bar') == ['foo', 'bar']
    # whitespace, multiple params
    assert split_args('  foo   bar  ') == ['foo', 'bar']
    # whitespace and quotes
    assert split_args('  foo   "bar baz"  ') == ['foo', '"bar baz"']
    # whitespace and single quotes
    assert split_args('  foo   \'bar baz\'  ') == ['foo', '\'bar baz\'']
    # whitespace and quotes around multiple params

# Generated at 2022-06-13 04:36:20.815691
# Unit test for function split_args
def test_split_args():
    def _run_tests_for_function(function):
        # Test 1: basic case
        function('''a=b c="foo bar"''') == ['a=b', 'c="foo bar"']

        # Test 2: unbalanced quotes
        try:
            function('''a=b c="foo bar''')
        except Exception:
            pass

        # Test 3: unbalanced jinja2 block
        try:
            function('''a=b c="{{ foo bar''')
        except Exception:
            pass

# Generated at 2022-06-13 04:36:31.743401
# Unit test for function split_args
def test_split_args():
    # simple args that should be unchanged
    assert split_args("a=1") == ["a=1"]
    assert split_args("a=1 b=2") == ["a=1", "b=2"]
    assert split_args("a=1 b='2 3'") == ["a=1", "b='2 3'"]
    assert split_args("a=1 b=2 c=3") == ["a=1", "b=2", "c=3"]
    assert split_args("a=1 b='2 3' c=3") == ["a=1", "b='2 3'", "c=3"]
    assert split_args("a=1 b='2 3' c=3 d='4 5'") == ["a=1", "b='2 3'", "c=3", "d='4 5'"]


# Generated at 2022-06-13 04:36:42.538158
# Unit test for function split_args
def test_split_args():
    '''
    These tests ensure the function for splitting arguments works
    as advertised. The code is complicated enough that it likely
    needs to be tested in this manner.

    The tests are defined as tuples of (input, output) arguments.
    '''

# Generated at 2022-06-13 04:36:51.848336
# Unit test for function split_args
def test_split_args():
    '''Unit test for function split_args'''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert split_args("foo") == ["foo"]
    assert split_args("foo bar") == ["foo", "bar"]
    assert split_args("foo=bar") == ["foo=bar"]
    assert split_args("foo=\"bar baz\"") == ["foo=bar baz"]
    assert split_args("foo='bar baz'") == ["foo=bar baz"]
    assert split_args("\"foo\"") == ["foo"]
    assert split_args("'foo'") == ["foo"]
    assert split_args("foo=\"{{bar}}\"") == ["foo={{bar}}"]
    assert split_args("foo=\"{{bar}} baz\"") == ["foo={{bar}} baz"]

# Generated at 2022-06-13 04:36:59.717032
# Unit test for function split_args

# Generated at 2022-06-13 04:37:04.738781
# Unit test for function split_args
def test_split_args():
    # Just basic tests for now to make sure the function works in a few basic cases.
    # More tests should be added for special cases, quoting, etc.
    assert split_args('') == []
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c='foo bar' d='foo bar' e='foo bar'") == ['a=b', "c='foo bar'", "d='foo bar'", "e='foo bar'"]

    # tests for jinja2 blocks

# Generated at 2022-06-13 04:37:16.608826
# Unit test for function split_args

# Generated at 2022-06-13 04:37:24.786908
# Unit test for function split_args
def test_split_args():
    '''test for the function split_args'''

    #our test cases for the function split_args

# Generated at 2022-06-13 04:37:36.220783
# Unit test for function split_args

# Generated at 2022-06-13 04:37:45.361791
# Unit test for function split_args
def test_split_args():

    import sys
    import os
    import unittest
    import tempfile
    from pathlib import Path

    from test.common import tmp_path

    if sys.platform == 'win32':
        src_path = Path(os.path.abspath(__file__)).parent
        if isinstance(tmp_path, str):
            tmp_path = Path(os.path.abspath(tmp_path))
        if not tmp_path.is_dir():
            tmp_path.mkdir()
        tmp_path = str(tmp_path)
        os.chdir(tmp_path)
    else:
        src_path = os.path.abspath(__file__)

    class TestSplitArgs(unittest.TestCase):

        def setUp(self):
            pass


# Generated at 2022-06-13 04:38:17.565792
# Unit test for function split_args
def test_split_args():
    ''' test for string.split_args '''

# Generated at 2022-06-13 04:38:20.125609
# Unit test for function split_args
def test_split_args():
    split_args("a=b c=\"foo bar\"")
    split_args("a=b c=\"foo \\\" bar\"")



# Generated at 2022-06-13 04:38:29.579268
# Unit test for function split_args
def test_split_args():
    test_args_1 = ("key1=value1 key2=value2 key3='a b c' key4='a \\\n b \\\n c'")
    test_out_1 = ['key1=value1', "key2=value2", "key3='a b c'", "key4='a \\\n b \\\n c'"]
    assert (split_args(test_args_1) == test_out_1)

    test_args_2 = ("key1=value1 key2=value2 key3=\"a b c\" key4=\"a \\\n b \\\n c\"")
    test_out_2 = ['key1=value1', "key2=value2", 'key3="a b c"', 'key4="a \\\n b \\\n c"']

# Generated at 2022-06-13 04:38:36.649085
# Unit test for function split_args
def test_split_args():
    test_string = "pam:!:17:17:pam_mount password entry:/home/pam:/bin/bash"
    result = split_args(test_string)
    assert len(result) == 7
    assert result[0] == "pam:!:17:17:pam_mount password entry:/home/pam:/bin/bash"

    test_string = "pam:!:17:17:pam_mount password entry:/home/pam:/bin/bash\\\n\\"
    result = split_args(test_string)
    assert len(result) == 7
    assert result[0] == "pam:!:17:17:pam_mount password entry:/home/pam:/bin/bash\n\\"


# Generated at 2022-06-13 04:38:48.686204
# Unit test for function split_args
def test_split_args():

    def _normalize(data):
        ''' normalizes data to make it easier to assert '''
        if isinstance(data, list):
            return [x.strip() for x in data]
        if isinstance(data, basestring):
            return data.strip()
        return data

    def test(args, expected):
        expected = _normalize(expected)
        result = _normalize(split_args(args))
        if result != expected:
            raise AssertionError("split_args('%s') returned %s, expected %s" % (args, result, expected))

    test('foo=bar name="baz foz"', ['foo=bar', 'name="baz foz"'])
    test('"foo"="bar"', '"foo"="bar"')

# Generated at 2022-06-13 04:38:59.590781
# Unit test for function split_args
def test_split_args():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    def assert_args(args, expect_args):
        assert split_args(args) == expect_args

    class UTF8(object):
        nbsp = '\xc2\xa0'

    assert_args(' a=b  c="foo bar" ', ['a=b', 'c="foo bar"'])
    assert_args(' a=b  c="foo\nbar" ', ['a=b', 'c="foo\nbar"'])
    assert_args(' a=b  c="foo\\"bar" ', ['a=b', 'c="foo\\"bar"'])

# Generated at 2022-06-13 04:39:09.413542
# Unit test for function split_args
def test_split_args():
    assert split_args("this is an unquoted string") == [u'this', u'is', u'an', u'unquoted', u'string']
    assert split_args("this is a 'quoted string'") == [u'this', u'is', u'a', u'"quoted string"']
    assert split_args('this is a "quoted string"') == [u'this', u'is', u'a', u'"quoted string"']
    assert split_args("this is an \"'escaped quoted string'\"") == [u'this', u'is', u'an', u'"\'escaped quoted string\'"']
    assert split_args("this is a backslash \\") == [u'this', u'is', u'a', u'backslash', u'\\']
    assert split

# Generated at 2022-06-13 04:39:19.804975
# Unit test for function split_args

# Generated at 2022-06-13 04:39:24.154274
# Unit test for function split_args
def test_split_args():
    # import needed parts of ansible.module_utils.basic
    import sys
    import os
    # import unit test support
    import tests.support as support

    # specify the temppath
    temppath = support.TESTFN

    # test simple cases
    testinput = "a b c"
    assert split_args(testinput) == testinput.split()

    # test quoted cases
    testinput = "a='b c'"
    assert split_args(testinput) == testinput.split()
    testinput = 'a="b c"'
    assert split_args(testinput) == testinput.split()
    testinput = 'a="b \'c\'"'
    assert split_args(testinput) == testinput.split()
    testinput = "a='b \"c\"'"

# Generated at 2022-06-13 04:39:33.098310
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c=\'foo bar\'') == ['a=b', 'c=\'foo bar\'']
    assert split_args("a=b 'foo bar'") == ['a=b', '\'foo bar\'']
    assert split_args("a=b 'foo bar") == ['a=b', "'foo bar"]
    assert split_args("a=b \"foo bar") == ['a=b', '"foo bar']
    assert split_args("a=b 'foo bar\\'s'") == ['a=b', "'foo bar\\'s'"]
    assert split_args("a=b 'foo bar'\\") == ['a=b', "'foo bar'"]
   

# Generated at 2022-06-13 04:40:24.693464
# Unit test for function split_args
def test_split_args():
    assert split_args("") == []
    assert split_args("a=1") == ['a=1']
    assert split_args("a=1\n") == ['a=1']
    assert split_args("a=1 b=2") == ['a=1', 'b=2']
    assert split_args("a=1 \\\nb=2") == ['a=1', 'b=2']
    assert split_args("a=1 \\\n\nb=2") == ['a=1', 'b=2']
    assert split_args("a=1 \\\n \\\nb=2") == ['a=1', 'b=2']
    assert split_args("a=1 \\\n \\\n \\\nb=2") == ['a=1', 'b=2']

# Generated at 2022-06-13 04:40:28.836142
# Unit test for function split_args

# Generated at 2022-06-13 04:40:34.745737
# Unit test for function split_args
def test_split_args():
    # Simple case
    test_input = "a b c"
    test_output = ['a', 'b', 'c']
    assert split_args(test_input) == test_output, "simple split_args failed"

    # Whitespace and quote case
    test_input = "a 'b c' d"
    test_output = ['a', "'b c'", 'd']
    assert split_args(test_input) == test_output, "whitespace + quote split_args failed"

    # Jinja2 block case
    test_input = "a {% b c %} d"
    test_output = ['a', '{% b c %}', 'd']
    assert split_args(test_input) == test_output, "jinja2 block split_args failed"

    # Jinja2 print case
   

# Generated at 2022-06-13 04:40:45.060355
# Unit test for function split_args
def test_split_args():

    # Empty args
    args = ''
    assert split_args(args) == []

    # Single item
    args = 'one'
    assert split_args(args) == ['one']

    # Single quoted item
    args = '"one"'
    assert split_args(args) == ['"one"']

    # Single quoted item with space
    args = '"one two"'
    assert split_args(args) == ['"one two"']

    # Three items
    args = 'one two three'
    assert split_args(args) == ['one', 'two', 'three']

    # Three items with spaces
    args = ' one  two   three'
    assert split_args(args) == ['one', 'two', 'three']

    # Three items with spaces and quotes

# Generated at 2022-06-13 04:40:54.870636
# Unit test for function split_args
def test_split_args():
    def test_split_args_internal(test_arguments, expected_output, expected_output_msg):
        test_output = split_args(test_arguments)
        assert test_output == expected_output, expected_output_msg + ':\n  expected: ' + str(expected_output) + '\n  received: ' + str(test_output)
