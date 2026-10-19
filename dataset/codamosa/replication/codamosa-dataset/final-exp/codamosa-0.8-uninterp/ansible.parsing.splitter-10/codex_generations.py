

# Generated at 2022-06-13 07:08:03.173393
# Unit test for function split_args
def test_split_args():
    assert split_args("var1=foo var2=bar") == [u"var1=foo", u"var2=bar"]
    assert split_args("var1=foo var2=bar\nvar3=baz") == [u"var1=foo", u"var2=bar\n", u"var3=baz"]
    # Inside quotes
    assert split_args("var1=foo var2='bar'") == [u"var1=foo", u"var2='bar'"]
    assert split_args("var1=foo var2=\"bar\"") == [u"var1=foo", u'var2="bar"']
    # Escaped quotes
    assert split_args("var1=foo var2=\\'bar\\'") == [u"var1=foo", u"var2=\\'bar\\'"]

# Generated at 2022-06-13 07:08:11.810321
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == dict(foo='bar')
    assert parse_kv('foo="bar"') == dict(foo='bar')
    assert parse_kv('foo=bar baz=foobar') == dict(foo='bar', baz='foobar')
    assert parse_kv(u"foo='bar' bar=\"baz\"") == dict(foo='bar', bar='baz')
    assert parse_kv(u"foo=bar 'baz' foo=bar foobar='foo baz'") == dict(foo='bar', foobar='foo baz')
    assert parse_kv(u"foo=bar 'baz' foo=bar foobar='foo baz'") == dict(foo='bar', foobar='foo baz')

# Generated at 2022-06-13 07:08:24.303812
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv(args="x=1 y=2 z=3"))
    print(parse_kv(args=["x=1", "y=2", "z=3"]))
    print(parse_kv(args="x=1 y=2 z=3", check_raw=True))
    print(parse_kv(args="x=1 y=2 z=3", check_raw="true"))
    print(parse_kv(args="x=1 y=2 z=3", check_raw=True))
    print(parse_kv(args="x=1 y=2 z=3", check_raw="True"))
    print(parse_kv(args="x=1 y=2 z=3", check_raw="TRUE"))

# Generated at 2022-06-13 07:08:35.706151
# Unit test for function parse_kv

# Generated at 2022-06-13 07:08:49.112549
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Unit test for function parse_kv
    '''
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv(' ') == {}
    assert parse_kv('   ') == {}
    assert parse_kv('=') == {}
    assert parse_kv('=a') == {}
    assert parse_kv('a=') == {'a':''}
    assert parse_kv('a=a') == {'a':'a'}
    assert parse_kv('a = a') == {'a': 'a'}
    assert parse_kv('a= a') == {'a': 'a'}
    assert parse_kv('a =a') == {'a': 'a'}
    assert parse_k

# Generated at 2022-06-13 07:09:00.794703
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1 b=2 c=3') == {u'a': u'1', u'b': u'2', u'c': u'3'}
    assert parse_kv('a=1 + b =2 + c = 3') == {u'a': u'1', u'b': u'2', u'c': u'3'}
    assert parse_kv('   a=1   b=2   c=3') == {u'a': u'1', u'b': u'2', u'c': u'3'}
    assert parse_kv('a=1 b="this is a test" c=3') == {u'a': u'1', u'b': u'this is a test', u'c': u'3'}

# Generated at 2022-06-13 07:09:10.743422
# Unit test for function parse_kv

# Generated at 2022-06-13 07:09:19.184332
# Unit test for function parse_kv
def test_parse_kv():

    import os
    import pprint

    test_cases = {
        'a=1 b=2': { u'a': u'1', u'b': u'2' },
        'a=1 c="foo bar"': { u'a': u'1', u'c': u'foo bar' },
        'convert\'n=yes a=1': { u'convertn': u'yes', u'a': u'1' },
    }

    parser = AnsibleModule(
        argument_spec = dict(
            my_arg = dict()
        ),
        supports_check_mode = True
    )

    # include a brief sanity check to ensure we are
    # actually parsing correctly with quoted markers

# Generated at 2022-06-13 07:09:34.008908
# Unit test for function split_args
def test_split_args():
    test_data = []
    test_data.append(dict(
        args=u'foo=bar group={{ group_name }}',
        expected=['foo=bar', 'group={{ group_name }}'],
    ))
    test_data.append(dict(
        args=u'foo="bar bar bar bar"',
        expected=['foo="bar bar bar bar"'],
    ))
    test_data.append(dict(
        args=u'foo="bar',
        expected=['foo="bar'],
    ))
    test_data.append(dict(
        args=u'foo="bar\\',
        expected=['foo="bar\\'],
    ))
    test_data.append(dict(
        args=u'foo="bar\\"',
        expected=['foo="bar"'],
    ))


# Generated at 2022-06-13 07:09:40.161462
# Unit test for function parse_kv
def test_parse_kv():
    in_str = u"/bin/example -o foo=56 -o baz -o lala='--lala=123 -a -b'; /bin/true"
    out_dict = parse_kv(in_str)
    assert u'foo' in out_dict
    assert out_dict[u'foo'] == u'56'
    assert u'baz' in out_dict
    assert out_dict[u'baz'] == True
    assert u'lala' in out_dict
    assert out_dict[u'lala'] == "--lala=123 -a -b"
    assert u'_raw_params' in out_dict
    assert out_dict[u'_raw_params'] == u"/bin/true"


# Generated at 2022-06-13 07:09:58.386261
# Unit test for function split_args
def test_split_args():
    assert split_args('/bin/foo --arg1 value1 --arg2 value2') == [u'/bin/foo', u'--arg1', u'value1', u'--arg2', u'value2']
    assert split_args('"This is a long argument"') == [u'"This is a long argument"']
    assert split_args('"This is a long argument') == [u'"This is a long argument']
    assert split_args('"a=b c=d" e="f g"') == [u'"a=b c=d"', u'e="f g"']

# Generated at 2022-06-13 07:10:06.653738
# Unit test for function split_args
def test_split_args():
    assert split_args(u'foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args(u"foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args(u"foo 'bar baz'") == ['foo', "'bar baz'"]
    assert split_args(u'foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args(u"foo 'bar baz'") == ['foo', "'bar baz'"]
    assert split_args(u"foo 'bar\\' baz'") == ['foo', "'bar\\' baz'"]
    assert split_args(u"foo 'bar\\'baz'") == ['foo', "'bar\\'baz'"]

# Generated at 2022-06-13 07:10:10.528436
# Unit test for function split_args
def test_split_args():
    test = ['a=1', 'b=2', 'c="hello\nworld"']
    assert test == split_args(join_args(test))

# Generated at 2022-06-13 07:10:22.065330
# Unit test for function split_args
def test_split_args():
    # Test for bug # 16019 - split_args broken with jinja2 when combined with multiple args
    input = '{{foo}} "{{bar}}" {{ baz }}'
    output = ['{{foo}}', '"{{bar}}"', '{{ baz }}']
    assert split_args(input) == output

    # Test for bug #19081 - split_args broken with jinja2 when using braces as argument
    input = '{{foo}} "{{bar}}" {{ baz }} {{{ qux }}}'
    output = ['{{foo}}', '"{{bar}}"', '{{ baz }}', '{{{ qux }}}']
    assert split_args(input) == output

    # Test multi-line args
    input = '{{foo}} "{{bar}}" \\\n{{ baz }}\n{{qux}}'

# Generated at 2022-06-13 07:10:33.311730
# Unit test for function parse_kv
def test_parse_kv():
    from unittest import TestCase
    class MyTest(TestCase):
        def test_basic(self):
            self.assertEqual(parse_kv("asked=no"), {'asked': 'no'})

            cmd = "echo 'hello' 'world'"
            self.assertEqual(parse_kv(cmd), {u'_raw_params': cmd})

        def test_quoting(self):
            self.assertEqual(parse_kv("asked=no name='world'"),
                             {u'name': u'world', u'asked': u'no'})
            self.assertEqual(parse_kv("asked=no name=\"world\""),
                             {u'name': u'world', u'asked': u'no'})

# Generated at 2022-06-13 07:10:40.283975
# Unit test for function split_args

# Generated at 2022-06-13 07:10:46.060726
# Unit test for function parse_kv
def test_parse_kv():
    """ Test parse_kv function """

    assert parse_kv(None) == {}

    assert parse_kv(u"a=b") == {"a": "b"}

    assert parse_kv(u"a") == {"_raw_params": "a"}

    assert parse_kv(u"a=b c=d") == {"a": "b", "c": "d"}

    assert parse_kv(u"a=b c=d e") == {"a": "b", "c": "d", "_raw_params": "e"}

    assert parse_kv(u"path=~/.ssh/id_rsa") == {"path": "~/.ssh/id_rsa"}


# Generated at 2022-06-13 07:10:55.093350
# Unit test for function parse_kv
def test_parse_kv():

    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('a=b c="d d"') == {u'a': u'b', u'c': u'd d'}
    assert parse_kv('') == {}
    assert parse_kv('a=b c="d=e f"') == {u'a': u'b', u'c': u'd=e f'}
    assert parse_kv('a=b c="d=e f') == {u'a': u'b', u'c': u'"d', u'_raw_params': u'a=b c="d=e f'}

# Generated at 2022-06-13 07:11:01.866851
# Unit test for function split_args

# Generated at 2022-06-13 07:11:10.937348
# Unit test for function split_args
def test_split_args():
    import unittest

# Generated at 2022-06-13 07:11:28.986373
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('greeting=hello world') == {u'greeting': u'hello world'}
    assert parse_kv('greeting=hello world urgreeting=goodbye') == {u'greeting': u'hello world', u'urgreeting': u'goodbye'}
    assert parse_kv('greeting="hello     world"') == {u'greeting': u'hello     world'}
    assert parse_kv('greeting="hello=world"') == {u'greeting': u'hello=world'}
    assert parse_kv('greeting="hello=world" urgreeting="goodbye=world"') == {u'greeting': u'hello=world', u'urgreeting': u'goodbye=world'}
    assert parse_

# Generated at 2022-06-13 07:11:35.654171
# Unit test for function parse_kv
def test_parse_kv():
    # Tested separately as a unit test
    pass


TASK_ATTRIBUTE_MATCHER = re.compile(r'''
                                    ^(?P<attribute>#?\w+)        # attribute name
                                    (\s*:\s*(?P<value>.*))?      # optional value
                                    $''', re.VERBOSE)


# Generated at 2022-06-13 07:11:45.572377
# Unit test for function split_args
def test_split_args():
    def foo(args, expected):
        result = split_args(args)
        if result != expected:
            print("failed to split {0}, got {1} instead of {2}".format(args, result, expected))
    foo("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"'])
    foo("a=b c=\"foo\nbar\"", ['a=b', 'c="foo\nbar"'])
    foo("a=b c=\"foo\nbar\n\"", ['a=b', 'c="foo\nbar\n"'])
    foo("a=b c=\"foo\nbar\"\n", ['a=b', 'c="foo\nbar"\n'])

# Generated at 2022-06-13 07:11:53.023500
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:02.819096
# Unit test for function split_args
def test_split_args():
    assert split_args(u"an=arg") == [u"an=arg"]
    assert split_args(u"an='arg'") == [u"an='arg'"]
    assert split_args(u"an=\"arg\"") == [u"an=\"arg\""]
    assert split_args(u"an=arg another=\"with spaces\"") == [u"an=arg", u"another=\"with spaces\""]
    assert split_args(u"an=arg another=\"with spaces\"") == [u"an=arg", u"another=\"with spaces\""]
    assert split_args(u"an=arg another='with spaces'") == [u"an=arg", u"another='with spaces'"]

# Generated at 2022-06-13 07:12:10.637445
# Unit test for function parse_kv

# Generated at 2022-06-13 07:12:17.872030
# Unit test for function split_args
def test_split_args():
    assert split_args(u'foo') == ['foo']
    assert split_args(u'foo bar') == ['foo', 'bar']
    assert split_args(u'"foo bar"') == [u'"foo bar"']
    assert split_args(u'foo "bar"') == ['foo', u'"bar"']
    assert split_args(u'foo "bar baz"') == ['foo', u'"bar baz"']
    assert split_args(u'foo "bar baz" spam') == ['foo', u'"bar baz"', 'spam']
    assert split_args(u'foo "bar \\"baz\\"" spam') == ['foo', u'"bar \\"baz\\""', 'spam']

# Generated at 2022-06-13 07:12:29.156380
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=2') == {u'a': u'2'}
    assert parse_kv('a=foo') == {u'a': u'foo'}
    assert parse_kv('a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv('a=1 b="foo bar"') == {u'a': u'1', u'b': u'foo bar'}
    assert parse_kv('a=1 b="foo bar') == {u'a': u'1', u'b': u'foo bar'}



# Generated at 2022-06-13 07:12:32.024147
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv("a=b c=d")
    assert options["a"] == u"b"
    assert options["c"] == u"d"



# Generated at 2022-06-13 07:12:36.247580
# Unit test for function parse_kv
def test_parse_kv():
        assert parse_kv('chdir="/foo" dog = cat') == {u'chdir': u'"/foo"', u'dog': u'cat'}



# Generated at 2022-06-13 07:12:53.253739
# Unit test for function split_args
def test_split_args():
    def _split_args(args):
        params = split_args(args)
        print(''.join(params))
        return params

    _split_args(r'''a=b c="foo bar"''')
    print('--')
    _split_args(r'''a=b c="foo\=bar"''')
    print('--')
    _split_args(r'''a=b c="foo\=bar" d=foo\ bar''')
    print('--')
    _split_args(r"""a=b c="foo=bar" d=foo\ bar""")
    print('--')
    _split_args(r'''a=b c="foo=bar" d=foo\ bar''')
    print('--')

# Generated at 2022-06-13 07:13:03.121790
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar\'') == ['a=b', 'c="foo bar\'']
    assert split_args('c="foo bar') == ['c="foo bar']
    assert split_args('c="foo bar\\') == ['c="foo bar\\']
    assert split_args('a=b c=\'foo bar\'') == ['a=b', "c='foo bar'"]
    assert split_args('a=b c=\'foo bar') == ['a=b', "c='foo bar"]

# Generated at 2022-06-13 07:13:13.369975
# Unit test for function split_args

# Generated at 2022-06-13 07:13:23.702709
# Unit test for function split_args
def test_split_args():
    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(split_args('a=b c="foo bar"'), ['a=b', 'c="foo bar"'])

        def test_no_equals(self):
            self.assertEqual(split_args('a b c'), ['a', 'b', 'c'])

        def test_newlines(self):
            self.assertEqual(split_args('a b c\nd e f\ng h i'), ['a', 'b', 'c\nd', 'e', 'f\ng', 'h', 'i'])


# Generated at 2022-06-13 07:13:33.573788
# Unit test for function parse_kv
def test_parse_kv():
    # Test parse_kv
    assert parse_kv("foo=foo bar=bar") == {u'bar': u'bar', u'foo': u'foo'}
    assert parse_kv("notakey foo=foo") == {u'foo': u'foo'}
    assert parse_kv("notakey foo=foo", check_raw=True) == {u'_raw_params': u'notakey foo=foo'}
    assert parse_kv("foo=foo bar=bar creates=baz", check_raw=True) == {u'bar': u'bar', u'foo': u'foo', u'creates': u'baz'}

# Generated at 2022-06-13 07:13:40.550396
# Unit test for function split_args
def test_split_args():
    args = ("name: a=b c=\"foo bar\" d='foo ba r' \\\n"
            "e=\"foobar\" f='foo bar' g='foo\\'s bar'")
    test = split_args(args)
    assert test == [u"name:", u"a=b", u"c=\"foo bar\"", u"d='foo ba r'",
                    u"e=\"foobar\"", u"f='foo bar'", u"g='foo\\'s bar'"]

    args = ("name: \"{{ lookup('foo', \"bar\") }}\"")
    test = split_args(args)
    assert test == [u"name:", u"\"{{ lookup('foo', \"bar\") }}\""]


# Generated at 2022-06-13 07:13:50.272380
# Unit test for function split_args
def test_split_args():
    '''
    Run tests on the split_args() function.
    '''
    from collections import namedtuple
    TestCase = namedtuple('TestCase', ['in_args', 'out_args'])


# Generated at 2022-06-13 07:14:04.707163
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    try:
        import json
    except ImportError:
        import simplejson as json

    # Test the many different quoting options
    x = "foo=bar"
    assert parse_kv(x) == {'foo': 'bar'}
    x = "foo='bar'"
    assert parse_kv(x) == {'foo': 'bar'}
    x = 'foo="bar"'
    assert parse_kv(x) == {'foo': 'bar'}
    x = "foo=bar five=six"
    assert parse_kv(x) == {'foo': 'bar', 'five': 'six'}
    x = "foo=bar\\ bar"
    assert parse_kv(x) == {'foo': 'bar bar'}

# Generated at 2022-06-13 07:14:12.252694
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:20.254322
# Unit test for function split_args
def test_split_args():
    assert ['echo', 'foo bar'] == split_args("echo foo bar")
    assert ['echo', 'foo bar'] == split_args("echo   foo bar")
    assert ['echo', 'foo bar'] == split_args("echo foo   bar")
    assert ['echo', 'foo bar'] == split_args("echo \tfoo \tbar")
    assert ['echo', 'foo bar'] == split_args("echo foo \tbar")
    assert ['echo', 'foo bar'] == split_args("echo   foo \tbar")
    assert ['echo', 'foo bar'] == split_args("echo \tfoo bar")
    assert ['echo', 'foo bar'] == split_args("echo \tfoo \t\tbar")
    assert ['echo', 'foo bar'] == split_args("echo   foo \t\tbar")

# Generated at 2022-06-13 07:14:40.626981
# Unit test for function split_args
def test_split_args():
    args = ""
    assert split_args(args) == []
    args = "a=b c=d"
    assert split_args(args) == ['a=b', 'c=d']
    args = "a='a' b=\"b\" c="
    assert split_args(args) == ['a=\'a\'', 'b="b"', 'c=']
    args = "a=\"b c"
    assert split_args(args) == ['a="b c']
    args = "a=\"b c\""
    assert split_args(args) == ['a="b c"']
    args = "a=\"b c\"d"
    assert split_args(args) == ['a="b c"d']
    args = "a=\"b c"
    assert split_args(args) == ['a="b c']

# Generated at 2022-06-13 07:14:47.924522
# Unit test for function parse_kv
def test_parse_kv():
    # don't test this unless we are running a unicode python
    # since we are testing unicode handling
    import sys
    if sys.version_info[0] < 3:
        assert sys.version_info[0] == 3
    assert {'a': '1', 'b': '2', 'c': '3'} == parse_kv("a=1 b=2 c=3")
    assert {'a': '1', 'b': '2', 'c': '3'} == parse_kv("a=1   b=2    c=3")
    assert {'a': '1', 'b': '2', 'c': '3'} == parse_kv("a=1 b=2   c=3")

# Generated at 2022-06-13 07:14:56.931747
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"a=b") == {u"a": u"b"}

    assert parse_kv(u"a=b \"c\"=d") == {u"a": u"b", u"c": u"d"}

    assert parse_kv(u"a=b \"c\"=\"d e\"") == {u"a": u"b", u"c": u"d e"}

    assert parse_kv(u"a=b \"c\"=\"d\\ e\"") == {u"a": u"b", u"c": u"d\\ e"}

    assert parse_kv(u"a=b \"c\"=\"d\\\"e\"") == {u"a": u"b", u"c": u"d\"e"}


# Generated at 2022-06-13 07:15:07.904812
# Unit test for function parse_kv
def test_parse_kv():
    parameter_string = 'a=b c="d e f" g="h \'i\'"'
    expected_result = {
        u'a': u'b',
        u'c': u'd e f',
        u'g': u"h 'i'",
        u'_raw_params': u'a=b c="d e f" g="h \'i\'"',
    }
    assert parse_kv(parameter_string, check_raw=True) == expected_result
    assert parse_kv(parameter_string)['a'] == expected_result['a']


# Generated at 2022-06-13 07:15:16.032935
# Unit test for function split_args

# Generated at 2022-06-13 07:15:26.897717
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('one=1 two=2') == {'one': 1, 'two': 2}
    assert parse_kv('one=1 two=2 three=3') == {'one': 1, 'two': 2, 'three': 3}
    assert parse_kv('one= 1 two= 2 three = 3') == {'one': 1, 'two': 2, 'three': 3}
    assert parse_kv('ONE=1 two=2 THREE = 3') == {'ONE': 1, 'two': 2, 'THREE': 3}
    assert parse_kv('ONE="1 two 3" TWO=2 THREE=3') == {'ONE': u'1 two 3', 'TWO': 2, 'THREE': 3}

# Generated at 2022-06-13 07:15:37.686118
# Unit test for function split_args

# Generated at 2022-06-13 07:15:44.691665
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('foo=bar') == {'foo': 'bar'}
    assert parse_kv(' foo=bar') == {'foo': 'bar'}
    assert parse_kv(' foo =bar') == {'foo': 'bar'}
    assert parse_kv(' foo= bar') == {'foo': 'bar'}
    assert parse_kv(' foo = bar') == {'foo': 'bar'}
    assert parse_kv(' foo=bar ') == {'foo': 'bar'}
    assert parse_kv('foo=bar ') == {'foo': 'bar'}
    assert parse_kv(' foo=bar baz=qux') == {'foo': 'bar', 'baz': 'qux'}
    assert parse_

# Generated at 2022-06-13 07:15:53.212589
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=simple b="with space" c="this=that" d=\'these="quotes"\'') == dict(a='simple', b='with space', c='this=that', d='these="quotes"', _raw_params=None)
    assert parse_kv('a=simple b="with space" c=\'this=that\' d=\'these="quotes"\'') == dict(a='simple', b='with space', c='this=that', d='these="quotes"', _raw_params=None)
    assert parse_kv('a=simple b="with space" c="a\\=b" d=\'a\\=b\'') == dict(a='simple', b='with space', c='a=b', d='a=b', _raw_params=None)

# Generated at 2022-06-13 07:16:05.541364
# Unit test for function split_args
def test_split_args():
    result = split_args("-a \"foo bar\"")
    assert result == ['-a', '"foo bar"']
    result = split_args("-a \"--bar fuu\"")
    assert result == ['-a', '"--bar fuu"']
    result = split_args("-a -b-c 'foo bar'")
    assert result == ['-a', '-b-c', "'foo bar'"]
    result = split_args("-a \"foo bar\" -b \"{{ foo }}\"")
    assert result == ['-a', '"foo bar"', '-b', '"{{ foo }}"']
    result = split_args("-a \"foo bar\" -b \"{{ foo }}\" 'customer_logs'")

# Generated at 2022-06-13 07:16:50.075246
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:57.740430
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1") == {u'a': u'1'}
    assert parse_kv("a=1 b=2 c=3") == {u'a': u'1', u'b': u'2', u'c': u'3'}
    assert parse_kv("a=1,b=2,c=3") == {u'a': u'1,b=2,c=3'}
    assert parse_kv("a=1,b=2 c=3") == {u'a': u'1,b=2', u'c': u'3'}
    assert parse_kv("a=b=c=3") == {u'a': u'b=c=3'}

# Generated at 2022-06-13 07:17:03.111049
# Unit test for function split_args
def test_split_args():
    passed = 0
    failed = 0