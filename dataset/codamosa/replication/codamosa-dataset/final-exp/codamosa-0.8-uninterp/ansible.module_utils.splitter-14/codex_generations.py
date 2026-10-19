

# Generated at 2022-06-13 04:31:22.275207
# Unit test for function unquote
def test_unquote():
    test_cases = [
        ('test', 'test'),
        ('"test"', 'test'),
        ('""', ''),
        ('"test', '"test'),
        ('"test', '"test'),
        ('test"', 'test"'),
        ("'test'", 'test'),
        ('""', ''),
        ("'test", "'test"),
        ("'test", "'test"),
        ("test'", "test'"),
    ]
    for payload, expected in test_cases:
        actual = unquote(payload)
        assert expected == actual, '%s != %s' % (expected, actual)



# Generated at 2022-06-13 04:31:32.408015
# Unit test for function split_args
def test_split_args():
    args = ''' foo=bar key=value key2="asdf asdf" key3="fjdk fjdk" "asdf asdf" key4=foo 'bar'=baz'''
    params = split_args(args)
    assert len(params) == 5, params
    assert params == ['foo=bar', 'key=value', 'key2="asdf asdf"', 'key3="fjdk fjdk"', '"asdf asdf" key4=foo \'bar\'=baz'], params
    args = '''foo=bar key=value key2="asdf asdf" key3="fjdk fjdk" "asdf asdf" key4=foo 'bar'=baz'''
    params = split_args(args)
    assert len(params) == 5, params

# Generated at 2022-06-13 04:31:39.068589
# Unit test for function unquote
def test_unquote():
    assert "bar" == unquote("'bar'")
    assert "bar" == unquote('"bar"')
    assert "bar" == unquote("'bar")
    assert "bar" == unquote('"bar')
    assert '"bar"' == unquote("'" + "\"bar\"" + "'")
    assert "'bar'" == unquote('"' + "'bar'" + '"')


# Generated at 2022-06-13 04:31:51.786302
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for function split_args
    '''
    # test quotes
    original = 'foo="bar baz"'
    params = split_args(original)
    assert params == ['foo="bar baz"']
    original = 'foo="bar baz" bar="foo bar"'
    params = split_args(original)
    assert params == ['foo="bar baz"', 'bar="foo bar"']
    original = 'foo="bar baz" bar="foo \'bar\'"'
    params = split_args(original)
    assert params == ['foo="bar baz"', 'bar="foo \'bar\'"']
    original = 'foo="bar baz" bar="foo \'bar\'"'
    params = split_args(original)

# Generated at 2022-06-13 04:31:57.092141
# Unit test for function unquote
def test_unquote():
    assert unquote('"hello world"') == 'hello world'
    assert unquote("'hello world'") == 'hello world'
    assert unquote("'hello world") != 'hello world'
    assert unquote("hello world'") != 'hello world'
    assert unquote("hello world") == 'hello world'



# Generated at 2022-06-13 04:32:09.292030
# Unit test for function split_args

# Generated at 2022-06-13 04:32:20.212605
# Unit test for function split_args

# Generated at 2022-06-13 04:32:26.008911
# Unit test for function unquote
def test_unquote():
    in_out = [('"abc"', 'abc'),
              ("'abc'", 'abc'),
              ('abc', 'abc'),
              ('"ab\'c"', 'ab\'c'),
              ("'ab\"c'", 'ab\"c')]

    for i in in_out:
        assert i[1] == unquote(i[0])

# Generated at 2022-06-13 04:32:32.749898
# Unit test for function split_args
def test_split_args():
    # test basic arg string
    # example input: a=b c="foo bar"
    # example output: ['a=b', 'c="foo bar"']
    input = 'a=b c="foo bar"'
    output = ['a=b', 'c="foo bar"']
    assert split_args(input) == output

    # test that splitting and rejoining works
    input = 'a=b c="foo bar"'
    assert " ".join(split_args(input)) == input

    # test that quotes can contain jinja2
    input = "'a=b c=\"{{ foo }}\"'"
    output = ["'a=b c=\"{{ foo }}\"'"]
    assert split_args(input) == output

    # test that quotes can be used inside jinja2

# Generated at 2022-06-13 04:32:43.442309
# Unit test for function split_args
def test_split_args():
    assert split_args('a=1 b="foo bar" c="foo\\"bar" d=\'foo\\\'bar\'') == ['a=1', 'b="foo bar"', 'c="foo\\"bar"', 'd=\'foo\\\'bar\'']
    assert split_args('a=1 b=c d=e f=\'foo bar\'') == ['a=1', 'b=c', 'd=e', 'f=\'foo bar\'']
    assert split_args('a=1 b=\'foo bar\' c=foo d=bar e=\'{% if test %}{% endif %}\'') == ['a=1', 'b=\'foo bar\'', 'c=foo', 'd=bar', 'e=\'{% if test %}{% endif %}\'']

# Generated at 2022-06-13 04:33:04.604565
# Unit test for function split_args
def test_split_args():

    results = split_args("")
    assert results == []

    results = split_args("a=b c=d")
    assert results == ["a=b", "c=d"]

    results = split_args("a=b c=d 'a=b c=d'")
    assert results == ["a=b", "c=d", "'a=b c=d'"]

    results = split_args("a=b c=d 'a=b c=d' \"a=b c=d\"")
    assert results == ["a=b", "c=d", "'a=b c=d'", '"a=b c=d"']


# Generated at 2022-06-13 04:33:12.873225
# Unit test for function split_args
def test_split_args():
    """
    Test function split_args
    """
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import re
    import string

    def _check_args(args, expected):
        result = split_args(args)
        if expected != result:
            print("**** args='%s' expected='%s' result='%s'" % (args, expected, result))
        assert expected == result

    # Quotes and escapes
    _check_args(r"""a='foo bar'""",
                [r"""a='foo bar'"""])

    _check_args(r"""a="foo bar" b="foo\ bar" c='foo\ bar'""",
                [r"""a="foo bar" b="foo\ bar" c='foo\ bar'"""])


# Generated at 2022-06-13 04:33:25.658002
# Unit test for function split_args
def test_split_args():
    # normal quotes
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    # nesting quotes
    assert split_args("a=b c=\"foo 'bar'\"") == ['a=b', "c=\"foo 'bar'\""]
    # backslash-escaped quotes
    assert split_args("a=b c=\"foo \\\"bar\\\"\"") == ['a=b', "c=\"foo \\\"bar\\\"\""]
    # double quotes inside single quotes
    assert split_args("a=b c='\"'") == ['a=b', "c='\"'"]
    # single quotes inside double quotes
    assert split_args('a=b c="\'"') == ['a=b', 'c="\'"']
    # quotes inside jinja2

# Generated at 2022-06-13 04:33:37.413643
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    assert split_args("a=b c='foo bar'") == ["a=b", "c='foo bar'"]
    assert split_args("a=b c=\"foo bar\"") == ["a=b", "c=\"foo bar\""]
    assert split_args("a\n=\nb\nc\n=\nd") == ["a\n=\nb", "c\n=\nd"]
    assert split_args("a='b c' d=e f=g") == ["a='b c'", "d=e", "f=g"]

# Generated at 2022-06-13 04:33:49.651939
# Unit test for function split_args
def test_split_args():
    assert split_args("-a") == ["-a"]
    assert split_args("-a -b -c") == ["-a", "-b", "-c"]
    assert split_args("-a -b -c='foo bar'") == ["-a", "-b", "-c='foo bar'"]
    assert split_args("-a -b -c='foo' -d='bar'") == ["-a", "-b", "-c='foo'", "-d='bar'"]
    assert split_args("-a -b -c='foo bar' --extra-vars='baz=qux'") == ["-a", "-b", "-c='foo bar'", "--extra-vars='baz=qux'"]

# Generated at 2022-06-13 04:33:58.595024
# Unit test for function split_args

# Generated at 2022-06-13 04:34:08.144865
# Unit test for function split_args
def test_split_args():
    simple_inputs = {
        'foo': ['foo'],
        'foo bar': ['foo', 'bar'],
        'foo bar baz': ['foo', 'bar', 'baz'],
        'foo bar "baz qux"': ['foo', 'bar', 'baz qux'],
        'foo bar "baz \'qux\'"': ['foo', 'bar', 'baz \'qux\''],
    }

    for test_input in simple_inputs:
        expected = simple_inputs[test_input]
        actual = split_args(test_input)
        if expected != actual:
            raise Exception("For simple test input '%s', expected split_args to return %s, but got %s" % (test_input, expected, actual))


# Generated at 2022-06-13 04:34:17.299095
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args("a=b 'c=foo bar'") == ['a=b', "'c=foo bar'"]
    assert split_args("a=b 'c=foo bar' d='1 2'") == ['a=b', "'c=foo bar'", "d='1 2'"]
    assert split_args("a=b 'c=\"foo bar\"' d='1 2'") == ['a=b', "'c=\"foo bar\"'", "d='1 2'"]
    assert split_args("a=b 'c=\"foo bar\"' d=\"1 2\"") == ['a=b', "'c=\"foo bar\"'", 'd="1 2"']

# Generated at 2022-06-13 04:34:27.574275
# Unit test for function split_args

# Generated at 2022-06-13 04:34:38.699326
# Unit test for function split_args

# Generated at 2022-06-13 04:35:08.372930
# Unit test for function split_args
def test_split_args():

    def test(args, expected):
        if expected != split_args(args):
            print("TEST FAIL: for '%s' got '%s' expected '%s'" %
                  (args, split_args(args), expected))

    test("aaa bbb ccc", ['aaa', 'bbb', 'ccc'])
    test("a='b b' c='d d'", ['a=\'b b\'', 'c=\'d d\''])
    test("a='b b' c='d d'", ['a=\'b b\'', 'c=\'d d\''])
    test("a=\"b b\" c=\"d d\"", ['a="b b"', 'c="d d"'])
    test("a=b c=d", ['a=b', 'c=d'])

# Generated at 2022-06-13 04:35:19.065140
# Unit test for function split_args
def test_split_args():
    data = '''
    a=b c="foo bar"
    d={% if e %}
        foo={{ bar }}
        bar={{ baz }}
    {% else %}
        foo=banana
    {% endif %}
    '''
    params = split_args(data)
    assert len(params) == 6
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'
    assert params[2] == 'd={% if e %}\n        foo={{ bar }}\n        bar={{ baz }}\n    {% else %}\n        foo=banana\n    {% endif %}\n    '
    assert params[3] == 'foo={{ bar }}'
    assert params[4] == 'bar={{ baz }}'
   

# Generated at 2022-06-13 04:35:26.668728
# Unit test for function split_args

# Generated at 2022-06-13 04:35:37.698823
# Unit test for function split_args

# Generated at 2022-06-13 04:35:40.769868
# Unit test for function split_args
def test_split_args():
    import sys
    import doctest
    import json
    num_failed, num_tests = doctest.testmod(split_args)
    sys.exit(num_failed)

if __name__ == '__main__':
    test_split_args()

# Generated at 2022-06-13 04:35:47.901784
# Unit test for function split_args
def test_split_args():
    # NOTE: This test was adapted from the shlex module's test suite.  We have
    # to reimplement it here because the original split_args function did not
    # handle all of these use cases.

    # test for simple splitting (no quoting/escaping)
    assert split_args('a b c') == ['a', 'b', 'c']

    # test for quotes
    assert split_args('"a b" x') == ['a b', 'x']
    assert split_args('a "b c"') == ['a', 'b c']
    assert split_args('"a \\"b\\" c"') == ['a "b" c']
    # tests for escaped quotes
    assert split_args(r'a \"b') == ['a', '\\"b']
    # test for escaped backslashes
    assert split_args

# Generated at 2022-06-13 04:35:56.284634
# Unit test for function split_args
def test_split_args():
    import sys
    import os
    from ansible.module_utils import basic

    # test normal args with various quoting
    test = "foo bar baz=foobar foob=barbaz barbaz='foo bar' baz='foo bar baz' bazzinga"
    answer = ['foo', 'bar', 'baz=foobar', 'foob=barbaz', "barbaz='foo bar'", "baz='foo bar baz'", 'bazzinga']
    if split_args(test) != answer:
        print("FAILED: test_split_args: test %s failed, output: %s" % (test, str(split_args(test))))
        sys.exit(1)

    # test quotes over spaces, quotes with newlines, and single quotes with spaces

# Generated at 2022-06-13 04:36:04.372571
# Unit test for function split_args
def test_split_args():

    def _run_test(args, expected):
        params = split_args(args)
        if expected != params:
            raise AssertionError("split_args(%s) = %s does not equal expected %s" % (args, params, expected))


# Generated at 2022-06-13 04:36:15.832466
# Unit test for function split_args

# Generated at 2022-06-13 04:36:24.860314
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import OrderedDict
    import pytest


# Generated at 2022-06-13 04:36:57.454877
# Unit test for function split_args
def test_split_args():
    test = [
        ("a=b foo='foo bar'", ['a=b', "foo='foo bar'"]),
        ("a=b foo='foo bar' bar={{ foo }}", ['a=b', "foo='foo bar'", "bar={{ foo }}"]),
        ("a=b foo='foo bar' bar={{ foo }}\nbaz={{ bar }}", ['a=b', "foo='foo bar'", "bar={{ foo }}\nbaz={{ bar }}"]),
    ]

    for t in test:
        assert split_args(t[0]) == t[1]

    # Final test to make sure its handles being used in a loop
    data = """
a=b
foo='foo bar'
bar={{ foo }}
"""

# Generated at 2022-06-13 04:37:08.599731
# Unit test for function split_args
def test_split_args():

    # Helper function to remove any quotes, since the result of
    # the split_args function should never have quotes
    def remove_quotes(list):
        return [x.replace('"', '').replace("'", '') for x in list]

    assert(remove_quotes(split_args('a=b c="foo bar"')) == ['a=b', 'c=foo bar'])
    assert(remove_quotes(split_args('a=b c="foo bar"    d="foo bar baz"')) == ['a=b', 'c=foo bar', 'd=foo bar baz'])
    assert(remove_quotes(split_args('a=b c="foo bar" d=\'foo bar baz\'')) == ['a=b', 'c=foo bar', 'd=foo bar baz'])
   

# Generated at 2022-06-13 04:37:21.198799
# Unit test for function split_args
def test_split_args():
    class TestCases(object):
        def __init__(self, args, result):
            self.args = args
            self.result = result


# Generated at 2022-06-13 04:37:32.725618
# Unit test for function split_args
def test_split_args():
    '''test for function split_args'''


# Generated at 2022-06-13 04:37:41.190613
# Unit test for function split_args
def test_split_args():
    # No change
    assert split_args('foo') == ['foo']

    # Change quotes only
    assert split_args('foo "bar"') == ['foo', '"bar"']
    assert split_args("foo 'bar'") == ['foo', "'bar'"]
    assert split_args('"foo bar"') == ['"foo bar"']
    assert split_args("'foo bar'") == ["'foo bar'"]

    # Change no quotes
    assert split_args('foo "bar" baz') == ['foo', '"bar"', 'baz']
    assert split_args('foo "bar baz" buzz') == ['foo', '"bar baz"', 'buzz']

    # Change quotes and quotes only
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']


# Generated at 2022-06-13 04:37:47.946882
# Unit test for function split_args

# Generated at 2022-06-13 04:37:54.747598
# Unit test for function split_args
def test_split_args():
    assert(split_args("echo 'foo bar'") == ['echo', "'foo bar'"])
    assert(split_args("echo 'foo bar baz'") == ['echo', "'foo bar baz'"])
    assert(split_args("echo 'foo bar' 'baz qux'") == ['echo', "'foo bar'", "'baz qux'"])
    assert(split_args('echo "foo bar"') == ['echo', '"foo bar"'])
    assert(split_args('echo "foo bar baz"') == ['echo', '"foo bar baz"'])
    assert(split_args('echo "foo bar" "baz qux"') == ['echo', '"foo bar"', '"baz qux"'])

# Generated at 2022-06-13 04:38:02.153920
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('foo="bar \\"baz\\""') == ['foo="bar \\"baz\\""']
    assert split_args('foo="bar \\\\"baz\\\\""') == ['foo="bar \\\\"baz\\\\""']
    assert split_args('foo="bar \\\\\\"baz\\\\\\\\""') == ['foo="bar \\\\\\"baz\\\\\\\\""']
    assert split_args('foo="bar \\\\\\\\"baz\\\\\\\\\\\\""') == ['foo="bar \\\\\\\\"baz\\\\\\\\\\\\""']

# Generated at 2022-06-13 04:38:14.009514
# Unit test for function split_args
def test_split_args():

    _test = ['a=b', 'c="foo bar"']
    _expect = [('a=b', ''), ('c', 'foo bar')]
    _result = []
    for _arg in split_args(_test[0]):
        _x = _arg.split('=', 1)
        if len(_x) == 1:
            _result.append((_x[0], ''))
        else:
            _result.append(tuple(_x))
    assert _result == _expect
    for _arg in split_args(_test[1]):
        _x = _arg.split('=', 1)
        if len(_x) == 1:
            _result.append((_x[0], ''))
        else:
            _result.append(tuple(_x))
    assert _result == _ex

# Generated at 2022-06-13 04:38:25.056292
# Unit test for function split_args

# Generated at 2022-06-13 04:39:03.908822
# Unit test for function split_args

# Generated at 2022-06-13 04:39:07.663545
# Unit test for function split_args
def test_split_args():
    import sys
    import json

    # load test cases
    with open('test/unit/utils/test_args.json') as f:
        test_cases = json.load(f)

    # run test cases

# Generated at 2022-06-13 04:39:11.123341
# Unit test for function split_args
def test_split_args():
    import sys

    argv = list(sys.argv)
    del argv[0]
    args = " ".join(argv)
    print(split_args(args))


if __name__ == '__main__':
    test_split_args()

# Generated at 2022-06-13 04:39:21.226104
# Unit test for function split_args
def test_split_args():
    assert split_args('ls -l /foo/ "sp ace" "qu\\\"ote"') == ['ls', '-l', '/foo/', '"sp ace"', '"qu\\"ote"']
    assert split_args('ls -l "/foo bar/baz"') == ['ls', '-l', '"/foo bar/baz"']
    assert split_args('ls -l /foo') == ['ls', '-l', '/foo']
    assert split_args('ls {{ foo }}') == ['ls', '{{ foo }}']
    assert split_args('ls {% foo %}') == ['ls', '{% foo %}']
    assert split_args('ls {{ foo }}{% foo %}') == ['ls', '{{ foo }}{% foo %}']

# Generated at 2022-06-13 04:39:29.704929
# Unit test for function split_args
def test_split_args():
    # Test split_args
    s = '''#!/bin/sh
    echo {{ ansible_managed }}
    echo 'some text'
    echo "some text"
    echo "some 'text'"
    echo some "text"
    echo "some text 'text'"
    echo "some text" "some text"
    echo {{ "some text" }}
    echo "some text" {{ "some text" }}
    echo {{ ansible_managed }}
    echo 'some text'
    echo "some text"
    echo "some 'text'"
    echo some "text"
    echo "some text 'text'"
    echo "some text" "some text"
    echo {{ "some text" }}
    echo "some text" {{ "some text" }}'''

    params = split_args(s)
    print(params)

    assert params

# Generated at 2022-06-13 04:39:37.185176
# Unit test for function split_args
def test_split_args():
    result = split_args('foo="bar baz"')
    assert result == ['foo=bar baz']

    result = split_args('foo="bar baz')
    assert result == ['foo=bar baz']

    result = split_args('foo="bar baz\\"')
    assert result == ['foo=bar baz"']

    result = split_args("foo='bar baz'")
    assert result == ['foo=bar baz']

    result = split_args("foo='bar baz")
    assert result == ['foo=bar baz']

    result = split_args("foo='bar baz\\'")
    assert result == ["foo=bar baz'"]

    result = split_args("""foo=bar baz'""")
    assert result == ["foo=bar", "baz'"]


# Generated at 2022-06-13 04:39:44.293357
# Unit test for function split_args
def test_split_args():
    '''
    Test cases for the split_args function
    '''

# Generated at 2022-06-13 04:39:54.317005
# Unit test for function split_args
def test_split_args():

    assert split_args("") == []
    assert split_args("a=b") == ['a=b']
    assert split_args("a=b c=d") == ['a=b', 'c=d']
    assert split_args("a=b 'c d'") == ['a=b', "'c d'"]
    assert split_args('a=b "c d"') == ['a=b', '"c d"']
    assert split_args("a=b 'c\"d'") == ['a=b', '\'c"d\'']
    assert split_args("a=b \"c'd\"") == ['a=b', '"c\'d"']

# Generated at 2022-06-13 04:40:02.929148
# Unit test for function split_args
def test_split_args():
    """
    runs unit tests on the split_args method above
    """
    # A list of tuples, first element is the arg string, second element
    # is the result we expect

# Generated at 2022-06-13 04:40:10.262475
# Unit test for function split_args
def test_split_args():

    # test simple values
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo "bar \\"baz\\""') == ['foo', '"bar \\"baz\\""']
    assert split_args("foo 'bar baz'") == ['foo', "'bar baz'"]
    assert split_args("foo='bar baz'") == ["foo='bar baz'"]
    assert split_args("foo='bar \" baz'") == ["foo='bar \" baz'"]
    assert split_args("foo='bar \\\" baz'") == ["foo='bar \\\" baz'"]
    assert split_args("foo='bar baz '")