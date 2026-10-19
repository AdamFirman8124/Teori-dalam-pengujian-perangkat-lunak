

# Generated at 2022-06-13 07:07:43.030187
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"") == {}
    assert parse_kv(u"foo=bar") == {u"foo": u"bar"}
    assert parse_kv(u"foo='bar'") == {u"foo": u"bar"}
    assert parse_kv(u"foo=\"bar\"") == {u"foo": u"bar"}
    assert parse_kv(u"foo=\"bar bar\"") == {u"foo": u"bar bar"}
    assert parse_kv(u"foo=\"bar \'bar\'\"") == {u"foo": u"bar 'bar'"}
    assert parse_kv(u"foo=\"bar \\\"bar\\\"\"") == {u"foo": u'bar "bar"'}

# Generated at 2022-06-13 07:07:54.481981
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('"a""b"') == ['"a""b"']
    assert split_args("echo {{ foo }}") == ['echo', '{{ foo }}']
    assert split_args("a=\"b{{ c }}d\"") == ['a="b{{ c }}d"']
    assert split_args("a={{ b }} c={{ d }}") == ['a={{ b }}', 'c={{ d }}']
    assert split_args("a='b{{ c }}d'") == ["a='b{{ c }}d'"]
    assert split_args('a="b{{ c }}d"') == ["a=\"b{{ c }}d\""]

# Generated at 2022-06-13 07:08:00.183306
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv(None) == {}
    assert parse_kv('foo=bar') == {'foo': 'bar'}
    assert parse_kv('foo=') == {'foo': ''}
    assert parse_kv('foo=bar bam=baz') == {'foo': 'bar', 'bam': 'baz'}
    assert parse_kv('foo="bar bam=baz"') == {'foo': 'bar bam=baz'}



# Generated at 2022-06-13 07:08:07.862618
# Unit test for function split_args

# Generated at 2022-06-13 07:08:16.855117
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {'foo': 'bar'}
    assert parse_kv('foo="bar bar" baz="one two"') == {'foo': 'bar bar', 'baz': 'one two'}
    assert parse_kv('foo="bar bar" baz="one two"') == {'foo': 'bar bar', 'baz': 'one two'}
    assert parse_kv('foo="one two" baz="bar bar"') == {'foo': 'one two', 'baz': 'bar bar'}
    assert parse_kv('foo="one two" baz="bar bar"') == {'foo': 'one two', 'baz': 'bar bar'}

# Generated at 2022-06-13 07:08:26.803441
# Unit test for function split_args
def test_split_args():
    assert split_args('''a=b c="foo bar"''') == ['a=b', 'c="foo bar"']
    assert split_args('''a=b c="foo bar"''', jinja=False) == ['a=b', 'c="foo bar"']
    assert split_args('''a=b c="foo bar"''', jinja=True) == ['a=b', 'c="foo bar"']
    assert split_args('''a=b c="foo bar"''', jinja=False) == ['a=b', 'c="foo bar"']

    assert split_args('''a=b c="foo bar"''') == ['a=b', 'c="foo bar"']

# Generated at 2022-06-13 07:08:37.885515
# Unit test for function split_args
def test_split_args():
    print("Testing split_args")
    assert split_args('"double quoted" \'single quoted\' unquoted') == ['"double quoted"', "'single quoted'", 'unquoted']
    assert split_args('"spaces inside" "double quotes" "but no spaces"') == ['"spaces inside"', '"double quotes"', '"but no spaces"']
    assert split_args('"quotes inside \'single quotes\'"') == ['"quotes inside \'single quotes\'"']
    assert split_args('"quotes inside \"double quotes\""') == ['"quotes inside \"double quotes\""']
    assert split_args('{{foo}} "{{bar}}"') == ['{{foo}}', '"{{bar}}"']

# Generated at 2022-06-13 07:08:48.416790
# Unit test for function split_args
def test_split_args():
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.playbook.play_context import PlayContext

    # Test simple args
    assert split_args(' "a=b c=d"\nfoo="bar baz"') == ['a=b c=d', 'foo="bar baz"']

    # Test escaping quotes
    assert split_args(r'a\="b"') == [r'a="b"']
    assert split_args(r'a\\"') == [r'a\\']

    # Test escaping equals
    assert split_args(r'a\=b') == [r'a=b']
    assert split_args(r'a\\=b') == [r'a\=b']

    # Test newlines

# Generated at 2022-06-13 07:09:00.113744
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == {u'foo': u'bar'}
    assert parse_kv("foo=bar baz=quux") == {u'foo': u'bar', u'baz': u'quux'}
    assert parse_kv("foo=bar 'baz quux'='abc 123'") == {u'foo': u'bar', u'baz quux': u'abc 123'}
    assert parse_kv("foo=bar 'baz quux'='abc 123'") == {u'foo': u'bar', u'baz quux': u'abc 123'}
    assert parse_kv("foo=bar 'baz quux'=\"abc 123\"") == {u'foo': u'bar', u'baz quux': u'abc 123'}
    assert parse

# Generated at 2022-06-13 07:09:10.164066
# Unit test for function split_args
def test_split_args():
    # This is used for unit testing and also a great way to test this function
    # manually
    import os
    import sys

    # This approach can't handle the case of quotes in the path itself
    data_file = os.path.join(sys.argv[1], 'test.args')

    # read the file and parse it
    with open(data_file, 'rb') as f:
        file_contents = f.read()
        f.close()

        # yes this is hideous.
        # the reason we do this is that the args file is written by humans and we
        # have to find any "escaped" chars and do the python unescaping,
        # otherwise it will mess up the tests

        file_contents = file_contents.replace('\\r', '\r')
        file_contents = file_contents

# Generated at 2022-06-13 07:09:36.817334
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Utility function to test parse_kv()
    '''
    mylist = []

    # Simple tests:
    mylist.append( (u"foo=bar", {u"foo": u"bar"}) )
    mylist.append( (u"foo='bar baz'", {u"foo": u"bar baz"}) )
    mylist.append( (u"a=b c='d e' f='g h'", {u"a": u"b", u"c": u"d e", u"f": u"g h"}) )
    mylist.append( (u"a=b 'c d'=foo", {u"a": u"b", u"c d": u"foo"}) )

    # empty values

# Generated at 2022-06-13 07:09:48.772685
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('create=true') == {u'create': u'true'}
    assert parse_kv('create=true time="2013-09-18 11:29:31"') == {u'time': '"2013-09-18 11:29:31"', u'create': u'true'}
    assert parse_kv('create=true time="2013-09-18 11:29:31" state=present') == {u'time': '"2013-09-18 11:29:31"', u'create': u'true', u'state': u'present'}

# Generated at 2022-06-13 07:09:58.179686
# Unit test for function split_args
def test_split_args():
    args = 'a=b c="foo bar" \nd="foo bar" e=\'foo bar\' f={{ bar }} g=foo{% bar %}h=foo{# bar #}i=foo\nj=baz'

    # double quote test
    cmd = ['a=b', 'c="foo bar"', 'd="foo bar"', 'e=\'foo bar\'', 'f={{ bar }}', 'g=foo{% bar %}h=foo{# bar #}i=foo\nj=baz']
    assert split_args(args) == cmd

    # single quote test

# Generated at 2022-06-13 07:10:03.801459
# Unit test for function parse_kv
def test_parse_kv():
    # Make sure that we don't mutate the original args
    from copy import deepcopy
    test_data = deepcopy(TEST_DATA)

    for args, expected_options in test_data:
        options = parse_kv(args, check_raw=False)
        assert options == expected_options

        options = parse_kv(args, check_raw=True)
        assert options == expected_options


# Unit tests for function join_args

# Generated at 2022-06-13 07:10:11.031463
# Unit test for function split_args
def test_split_args():
    class MockAssertionError(Exception):
        pass

    def mock_assert_equals(expected, observed):
        if expected != observed:
            raise MockAssertionError("%s != %s" % (expected, observed))

    def mock_assert(test):
        if not test:
            raise MockAssertionError("Assertion Error")

    old_assert_equals = __builtin__.assert_equals

# Generated at 2022-06-13 07:10:24.411709
# Unit test for function parse_kv
def test_parse_kv():
    # some simple tests
    assert parse_kv('a=b') == {u'a': u'b'}
    assert parse_kv('a=b c=d') == {u'a': u'b', u'c': u'd'}
    assert parse_kv('a=b\\ c=d') == {u'a': u'b c=d'}
    assert parse_kv('a="b c"') == {u'a': u'b c'}
    assert parse_kv("a='b c'") == {u'a': u'b c'}
    assert parse_kv("a='b c' d=e") == {u'a': u'b c', u'd': u'e'}

# Generated at 2022-06-13 07:10:31.167109
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("") == {}
    assert parse_kv("foo=bar") == {'foo': 'bar'}
    assert parse_kv("foo=bar bar=baz") == {'foo': 'bar', 'bar': 'baz'}
    assert parse_kv("foo='bar bar'") == {'foo': 'bar bar'}
    assert parse_kv("foo='bar bar' bar=baz") == {'foo': 'bar bar', 'bar': 'baz'}



# Generated at 2022-06-13 07:10:40.946722
# Unit test for function split_args
def test_split_args():
    # test args over newline and spaces
    # for recursive cases see below
    assert split_args('') == []
    assert split_args('foo') == ['foo']
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo bar baz\nfoo bar baz') == ['foo', 'bar', 'baz\nfoo', 'bar', 'baz']
    assert split_args('foo bar baz\nfoo bar baz\n') == ['foo', 'bar', 'baz\nfoo', 'bar', 'baz\n']
    assert split_args('foo\nbar') == ['foo', 'bar']

# Generated at 2022-06-13 07:10:52.005210
# Unit test for function split_args
def test_split_args():
    assert split_args('') == []
    assert split_args('"foo"') == ['foo']
    assert split_args('"foo "bar"') == ['foo', 'bar']
    assert split_args('"foo bar"\n') == ['foo bar\n']
    assert split_args('"foo bar"\n"hello world"') == ['foo bar\n', 'hello world']
    assert split_args('foo\nbar') == ['foo\n', 'bar']
    assert split_args('foo\nbar\nbaz') == ['foo\n', 'bar\n', 'baz']
    assert split_args('foo\nbar baz') == ['foo\n', 'bar', 'baz']

# Generated at 2022-06-13 07:10:59.062005
# Unit test for function parse_kv
def test_parse_kv():
    args = u"foo='bar baz' bam=baz key=value"
    expected = {u'foo': u"bar baz", u"bam": u"baz", u"key": u"value"}
    actual = parse_kv(args)
    assert actual == expected, actual

    # key=value pairs with quotes can contain = characters
    args = u"foo=\"a=b\" bam=baz"
    expected = {u'foo': u"a=b", u"bam": u"baz"}
    actual = parse_kv(args)
    assert actual == expected, actual

    # value can be quoted, key cannot
    args = u"foo=\"a=b\" 'bam=baz'"

# Generated at 2022-06-13 07:11:11.772861
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv(
        "one simple string=baz foo='with spaces' bar=\"with spaces\" quux={{ bork }}")
    assert options == {
        u'one': u'simple',
        u'string': u'baz',
        u'foo': u'with spaces',
        u'bar': u'with spaces',
        u'quux': u'{{ bork }}',
        u'_raw_params': u"string baz foo='with spaces' bar=\"with spaces\" quux={{ bork }}"
    }

    options = parse_kv(
        "one simple string=baz foo='with spaces' bar=\"with spaces\" quux={{ bork }}", check_raw=True)

# Generated at 2022-06-13 07:11:18.786572
# Unit test for function split_args

# Generated at 2022-06-13 07:11:28.560765
# Unit test for function parse_kv
def test_parse_kv():
    """
    Unit test for function parse_kv
    """
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # simple key-value pair
    assert parse_kv('test=value') == {"test": "value"}
    # key-value pairs
    assert parse_kv('test1=value1 test2=value2') == {"test1": "value1", "test2": "value2"}
    # combination of key-value pair and free-form parameters
    assert parse_kv('test1=value1 test2=value2 value3 value4') == {"test1": "value1", "test2": "value2", "_raw_params": "value3 value4"}
    # escaped characters

# Generated at 2022-06-13 07:11:36.524112
# Unit test for function split_args
def test_split_args():
    import sys
    import inspect
    import json

    def describe(itm):
        if type(itm) in [str, unicode]:
            return itm
        elif type(itm) in [list, tuple]:
            return '[' + ','.join(map(describe, itm)) + ']'
        else:
            return json.dumps(itm)

    def test_args(args, expected):

        print("Split '%s' into '%s'" % (describe(args), describe(expected)))

        if type(args) in [list, tuple]:
            args = join_args(args)
        result = split_args(args)


# Generated at 2022-06-13 07:11:47.192693
# Unit test for function split_args
def test_split_args():
    test = split_args
    assert test('') == [], 'should return an empty list'
    assert test('a=b') == ['a=b'], 'simple'
    assert test('foo="bar baz"') == ['foo="bar baz"'], 'quotes'
    assert test('a=b c="foo bar"') == ['a=b', 'c="foo bar"'], 'two args'
    assert test('{{ foo }}') == ['{{ foo }}'], 'jinja2 print'
    assert test('{{ foo }} bar="baz"') == ['{{ foo }}', 'bar="baz"'], 'jinja2 and string'
    assert test('foo bar {{ foo }} baz') == ['foo', 'bar', '{{ foo }}', 'baz'], 'string, jinja2 and string'

# Generated at 2022-06-13 07:11:53.798292
# Unit test for function parse_kv
def test_parse_kv():
    # Test empty arguments
    assert parse_kv('') == {}
    # Test one key-value argument
    assert parse_kv('a=b') == {'a': 'b'}
    # Test one key-value argument with spaces around the =
    assert parse_kv('  a = b  ') == {'a': 'b'}
    # Test two key-value arguments
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    # Test two key-value arguments with spaces around the =
    assert parse_kv('  a = b  c = d  ') == {'a': 'b', 'c': 'd'}
    # Test key ends with =
    assert parse_kv('a=') == {'a': ''}


# Generated at 2022-06-13 07:11:54.855849
# Unit test for function parse_kv
def test_parse_kv():
    assert False

# Generated at 2022-06-13 07:12:03.818578
# Unit test for function split_args
def test_split_args():
    '''
    Tests for validity of various types of arguments and use of tokens. This includes
    making sure that quotes are properly retained and that jinja2 block arguments
    are properly retained without whitespace removal.
    '''
    # Test plain arguments
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('foo bar="baz"') == ['foo', 'bar="baz"']
    assert split_args('foo bar="baz boo"') == ['foo', 'bar="baz boo"']
    assert split_args('foo=bar baz=boo') == ['foo=bar', 'baz=boo']

# Generated at 2022-06-13 07:12:11.754500
# Unit test for function parse_kv
def test_parse_kv():
    # first we try the happy path
    assert parse_kv(u"foo=bar bar=foo") == {u"foo": u"bar", u"bar": u"foo"}
    # then we try something a little tricker
    assert parse_kv(u"foo=bar bar=foo baz") == {u"foo": u"bar", u"bar": u"foo", u"_raw_params": u"baz"}
    # then something trickier still
    assert parse_kv(u"foo=bar bar=foo baz quux=\"x y\"") == {u"foo": u"bar", u"bar": u"foo", u"_raw_params": u"baz quux=\"x y\""}
    # and a corner case

# Generated at 2022-06-13 07:12:18.345939
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("creates=/tmp/foo") == {u'creates': u'/tmp/foo'}
    assert parse_kv("creates=/tmp/foo removes=/tmp/bar") == {u'creates': u'/tmp/foo', u'removes': u'/tmp/bar'}
    assert parse_kv("creates=/tmp/foo removes=/tmp/bar chdir=/tmp _raw_params=' once more '") == {u'creates': u'/tmp/foo', u'removes': u'/tmp/bar', u'chdir': u'/tmp', u'_raw_params': u" once more "}

# Generated at 2022-06-13 07:12:31.961941
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv(' foo = bar ') == {u'foo': u'bar'}
    assert parse_kv('foo:="bar baz"') == {u'foo': u'bar baz'}
    assert parse_kv('foo=bar baz') == {u'foo': u'bar', u'baz': u''}
    assert parse_kv('a=1 b=2') == {u'a': u'1', u'b': u'2'}
    assert parse_kv('=" 1 " b=2') == {u'b': u'2'}
    assert parse_kv('a=1') == {u'a': u'1'}

# Generated at 2022-06-13 07:12:46.156598
# Unit test for function split_args
def test_split_args():
    def split_test(test_input, expected, desc):
        def split_and_assert(input, expected):
            actual = split_args(input)
            assert actual == expected, "Expected %r, but got %r" % (expected, actual)

        # Test with input through stdin
        split_and_assert("<<< %s" % test_input, expected)
        split_and_assert('<<EOF\n%s\nEOF' % test_input, expected)

        # Test with param
        split_and_assert(test_input, expected)

        # Test string with spaces
        split_and_assert('"%s"' % test_input, ["%s" % test_input])


# Generated at 2022-06-13 07:12:55.027813
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv(' "foo=bar baz" ') == {'foo': 'bar baz'}
    assert parse_kv('foo="bar baz"') == {'foo': 'bar baz'}
    assert parse_kv('foo="bar baz" one=two') == {'foo': 'bar baz', 'one': 'two'}
    assert parse_kv('foo="bar \'baz" one=two') == {'foo': 'bar \'baz', 'one': 'two'}
    assert parse_kv('foo=bar one="one two three"') == {'foo': 'bar', 'one': 'one two three'}

# Generated at 2022-06-13 07:13:04.335448
# Unit test for function split_args
def test_split_args():
    from ansible.parsing.split import unquote

    # expected, actual

# Generated at 2022-06-13 07:13:09.858920
# Unit test for function split_args

# Generated at 2022-06-13 07:13:20.977761
# Unit test for function parse_kv
def test_parse_kv():
    # parse_kv: simple test
    assert parse_kv('foo=bar') == {'foo': 'bar'}

    # parse_kv: test quoted values
    assert parse_kv("foo='bar baz'") == {"foo": "bar baz"}

    # parse_kv: test escaped quotes inside quoted values
    assert parse_kv("foo='bar \\'baz\\''") == {'foo': "bar 'baz'"}

    # parse_kv: test escaped quotes inside quoted values
    assert parse_kv("foo='bar \"baz\"'") == {'foo': 'bar "baz"'}

    # parse_kv: test escaped equals inside quoted values
    assert parse_kv("foo='bar \\=baz'") == {'foo': 'bar =baz'}

    # parse

# Generated at 2022-06-13 07:13:25.875276
# Unit test for function split_args
def test_split_args():
    print("Testing function split_args")
    from ansible.modules.system import service

# Generated at 2022-06-13 07:13:35.719677
# Unit test for function split_args
def test_split_args():
    assert split_args('foo bar baz') == ['foo', 'bar', 'baz']
    assert split_args('a=1 b=2') == ['a=1', 'b=2']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('foo="bar baz') == ['foo="bar', 'baz']
    assert split_args('foo="bar baz\\') == ['foo="bar', 'baz\\']

# Generated at 2022-06-13 07:13:41.064604
# Unit test for function parse_kv
def test_parse_kv():
    # basics
    assert parse_kv(u'') == {}
    assert parse_kv(u'a=b') == {u'a': u'b'}
    assert parse_kv(u'a=b c=d') == {u'a': u'b', u'c': u'd'}
    assert parse_kv(u'a=b "c d"=e') == {u'a': u'b', u'c d': u'e'}
    assert parse_kv(u'a=b "c d"="e f"') == {u'c d': u'e f', u'a': u'b'}

# Generated at 2022-06-13 07:13:48.146693
# Unit test for function split_args
def test_split_args():
    test_data = [
        ("a=b c=\"foo bar\"", ['a=b', 'c="foo bar"']),
        ("a=b\nc=\"foo bar\"", ['a=b\n', 'c="foo bar"']),
        ("a=b c=\"foo bar", ['a=b', 'c="foo bar']),
        ("a=b c=\"foo bar\\", ['a=b', 'c=\\"foo bar\\']),
    ]
    for args, expected_result in test_data:
        assert split_args(args) == expected_result

# Generated at 2022-06-13 07:14:10.656985
# Unit test for function split_args
def test_split_args():
    assert split_args("foo bar baz") == ['foo', 'bar', 'baz']
    assert split_args("foo bar=baz") == ['foo', 'bar=baz']
    assert split_args("foo=bar baz=boo") == ['foo=bar', 'baz=boo']
    assert split_args("foo=bar baz=boo\\") == ['foo=bar', 'baz=boo']
    assert split_args("foo=bar baz=boo bar") == ['foo=bar', 'baz=boo bar']
    assert split_args("foo=bar baz=boo bar\\") == ['foo=bar', 'baz=boo bar']
    assert split_args("foo='bar baz'") == ["foo='bar baz'"]

# Generated at 2022-06-13 07:14:25.160566
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("A=1") == dict(A='1')
    assert parse_kv("Bar Baz=1") == dict(Bar_Baz='1')
    assert parse_kv("Baz=foo=bar") == dict(Baz='foo=bar')
    assert parse_kv("Baz=foo=bar", True) == dict(Baz='foo=bar')
    assert parse_kv("Baz=foo\\=bar=baz") == dict(Baz='foo=bar=baz')
    assert parse_kv("Baz=foo\\=bar baz", True) == dict(Baz='foo=bar baz')
    assert parse_kv("Baz=''") == dict(Baz='')
    assert parse_kv("Baz=\"\"") == dict(Baz='')

# Generated at 2022-06-13 07:14:35.679583
# Unit test for function split_args
def test_split_args():
    # Basic test with no linebreaks, no params, no quotes, no jinja2, no extra whitespaces
    assert split_args('abc def') == ['abc', 'def']
    # Basic test with no linebreaks, no params, no quotes, no jinja2
    assert split_args('   abc   def   ') == ['abc', 'def']
    # Basic test with no linebreaks, but params, no quotes, no jinja2
    assert split_args(' abc=def ghi=jkl ') == ['abc=def', 'ghi=jkl']
    # Test with linebreaks, no params, no quotes, no jinja2
    assert split_args('abc\ndef') == ['abc', 'def']
    assert split_args('abc\n def') == ['abc', 'def']
    assert split_

# Generated at 2022-06-13 07:14:43.770001
# Unit test for function parse_kv
def test_parse_kv():
    # test parsing normal options
    assert parse_kv('foo=bar baz=quux') == dict(foo='bar', baz='quux')
    assert parse_kv('foo="bar baz" quux=blah') == dict(foo='"bar baz"', quux='blah')
    # test parsing options with escapes
    assert parse_kv('foo=bar\\ baz quux=blah') == dict(foo='bar baz', quux='blah')
    # test parsing options with embedded quotes
    assert parse_kv('foo=bar"baz"blah quux=\'hoge\'') == dict(foo='bar"baz"blah', quux="'hoge'")

    # test parsing options with embedded quotes

# Generated at 2022-06-13 07:14:49.941544
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("creates=/tmp/foo creates=/tmp/bar arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14 arg15 arg16 arg17") == \
        {u'creates': u'/tmp/foo', u'_raw_params': u'creates=/tmp/bar arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10 arg11 arg12 arg13 arg14 arg15 arg16 arg17'}

# Generated at 2022-06-13 07:14:58.622214
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u'foo=bar=rab', check_raw=True) == {u'foo': u'bar=rab', u'_raw_params': u'foo=bar=rab'}
    assert parse_kv('foo=bar=rab', check_raw=True) == {u'foo': u'bar=rab', u'_raw_params': u'foo=bar=rab'}
    assert parse_kv('foo=bar=rab', check_raw=False) == {u'foo': u'bar=rab'}
    assert parse_kv(u'foo=bar=rab', check_raw=False) == {u'foo': u'bar=rab'}
    assert parse_kv(u'foo=bar=rab') == {u'foo': u'bar=rab'}
    assert parse_

# Generated at 2022-06-13 07:15:05.407864
# Unit test for function parse_kv
def test_parse_kv():
    def parse(args):
        return parse_kv(args, check_raw=True)

    assert parse('a=b c=d e=f') == {'a': 'b', 'c': 'd', 'e': 'f', '_raw_params': ''}
    assert parse('a=b c=d g h=i') == {'a': 'b', 'c': 'd', 'h': 'i', '_raw_params': 'g'}
    assert parse('a=b c=d g "h=i"') == {'a': 'b', 'c': 'd', '_raw_params': 'g "h=i"'}

# Generated at 2022-06-13 07:15:13.531054
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("") == {}
    assert parse_kv("foo=bar") == {"foo" : "bar"}
    assert parse_kv("foo='bar baz'") == {"foo" : "bar baz"}
    assert parse_kv("foo=bar=baz") == {"foo" : "bar=baz"}
    assert parse_kv("foo='bar=baz'") == {"foo" : "bar=baz"}
    assert parse_kv("foo='bar=baz' bar='baz=foo'") == {"foo" : "bar=baz", "bar" : "baz=foo"}
    assert parse_kv("foo='ba r=ba z' bar=baz=foo") == {"foo" : "ba r=ba z", "bar" : "baz=foo"}
   

# Generated at 2022-06-13 07:15:24.083502
# Unit test for function parse_kv
def test_parse_kv():
    assert(parse_kv(None) == {})
    assert(parse_kv(u'') == {})
    assert(parse_kv(u'a=b') == {u'a': u'b'})
    assert(parse_kv(u'a=b c=d') == {u'a': u'b', u'c': u'd'})
    assert(parse_kv(u"a='b c' d='e f'") == {u'a': u'b c', u'd': u'e f'})
    assert(parse_kv(u"a=\"b c\" d=\"e f\"") == {u'a': u'b c', u'd': u'e f'})

# Generated at 2022-06-13 07:15:32.013664
# Unit test for function parse_kv
def test_parse_kv():
    arg_string = "creates=/etc/yum.repos.d/epel.repo executable=/bin/bash removes=/etc/yum.repos.d/epel.repo"
    assert parse_kv(arg_string) ==  {u'creates': u'/etc/yum.repos.d/epel.repo', u'removes': u'/etc/yum.repos.d/epel.repo', u'executable': u'/bin/bash'}

    # Testing with unicode characters
    arg_string = u"creates=\u2605 stdin=\u2605"
    assert parse_kv(arg_string) == {u'creates': u'\u2605', u'stdin': u'\u2605'}


# Quote escapes adapted from Python's

# Generated at 2022-06-13 07:15:49.899537
# Unit test for function parse_kv

# Generated at 2022-06-13 07:15:52.767331
# Unit test for function parse_kv
def test_parse_kv():
    parse_kv("a=1")

# Parses the input argument to split it into list

# Generated at 2022-06-13 07:16:05.378746
# Unit test for function parse_kv
def test_parse_kv():
    # basic positional args
    a1 = """myprogram arg1 arg2 --foo bar --baz=spam """
    r_a1 = parse_kv(a1, check_raw=False)
    assert r_a1['_raw_params'] == 'arg1 arg2 --foo bar --baz=spam '

    # basic key/value args
    a2 = """myprogram --foo bar --baz=spam"""
    r_a2 = parse_kv(a2)
    assert r_a2['foo'] == 'bar'
    assert r_a2['baz'] == 'spam'

    # escaped quotes
    a3 = """myprogram --foo=\\"bar\\" --baz=\'spam\'"""
    r_a3 = parse_kv(a3)
    assert r_a

# Generated at 2022-06-13 07:16:14.309955
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:23.601436
# Unit test for function split_args
def test_split_args():
    split = split_args(u'a=b c="foo bar"')
    assert split == ['a=b', 'c="foo bar"']

    # Test for multiple whitespace
    split = split_args(u'a=b c="foo    bar"')
    assert split == ['a=b', 'c="foo    bar"']

    # Test for escaped quotes
    split = split_args(u'a=b c="foo \\" bar"')
    assert split == ['a=b', 'c="foo \\" bar"']

    # Test for quotes mixing with block tags
    split = split_args(u'a=b c="foo {% bar "')
    assert split == ['a=b', 'c="foo {% bar "']

    # Quotes inside of blocks

# Generated at 2022-06-13 07:16:34.580524
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == dict(foo='bar')
    assert parse_kv("foo='bar'") == dict(foo='bar')
    assert parse_kv("foo='bar baz'") == dict(foo='bar baz')
    assert parse_kv("foo=bar baz") == dict(foo='bar', _raw_params='baz')
    assert parse_kv("foo='bar baz' norf=quux") == dict(foo='bar baz', norf='quux')
    assert parse_kv("foo='bar baz' norf=\"quux'bar\"") == dict(foo='bar baz', norf="quux'bar")
    assert parse_kv("foo='bar baz' norf=\"quux'bar\" bip=\"corge'garply\"") == dict

# Generated at 2022-06-13 07:16:48.276322
# Unit test for function parse_kv
def test_parse_kv():
    # Positive test cases
    assert parse_kv("creates=/tmp/foo executable=/bin/foobar") == dict(creates='/tmp/foo', executable='/bin/foobar')
    assert parse_kv("creates=/tmp/foo executable=/bin/foobar", check_raw=True) == dict(creates='/tmp/foo', executable='/bin/foobar')
    assert parse_kv("executable=/bin/foobar", check_raw=True) == dict(executable='/bin/foobar')
    assert parse_kv("/bin/foobar", check_raw=True) == dict(_raw_params='/bin/foobar')
    assert parse_kv("/bin/foobar", check_raw=True) == dict(_raw_params='/bin/foobar')

# Generated at 2022-06-13 07:16:53.613404
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils import given_vars

    cmd = """foo='hello world' bar="hello world" baz=hello\ world blah=hello\\=world foo2="hello=world" """
    assert(parse_kv(cmd) == dict(foo="hello world", bar="hello world", baz="hello world", blah="hello=world", foo2="hello=world"))



# Generated at 2022-06-13 07:17:05.336302
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('one two=three four="five six" seven=eight nine') == {u'two': u'three', u'four': u'five six', u'seven': u'eight', u'_raw_params': u'one nine'}
    assert parse_kv('creates=/tmp/a file=/tmp/b') == {u'creates': u'/tmp/a', u'file': u'/tmp/b'}
    assert parse_kv('creates=/tmp/a file=/tmp/b', check_raw=True) == {u'creates': u'/tmp/a', u'file': u'/tmp/b', u'_raw_params': u'file=/tmp/b'}