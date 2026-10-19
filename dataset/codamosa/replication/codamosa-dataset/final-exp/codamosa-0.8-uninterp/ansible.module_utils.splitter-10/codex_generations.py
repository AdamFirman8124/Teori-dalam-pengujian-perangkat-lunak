

# Generated at 2022-06-13 04:31:16.823955
# Unit test for function split_args
def test_split_args():
    """
    function: test_split_args
    Split args and check the list of params without the quotes.
    """
    test1 = 'a=b c="foo bar"'
    params = split_args(test1)
    print(params)

    assert len(params) == 2
    assert params[0] == 'a=b'
    assert params[1] == 'c=foo bar'

    test2 = 'a=b c="foo \\\\\\" bar"'
    params = split_args(test2)
    print(params)

    assert len(params) == 2
    assert params[0] == 'a=b'
    assert params[1] == 'c=foo \\\\" bar'

    test3 = 'a=b c="foo \\\\\\"'
    params = split_args(test3)

# Generated at 2022-06-13 04:31:23.112346
# Unit test for function split_args
def test_split_args():
    # Test basic quote handling
    assert split_args('"foo bar"') == ['foo bar']
    assert split_args("'foo bar'") == ['foo bar']
    assert split_args('"foo bar" spam') == ['foo bar', 'spam']
    assert split_args('"foo bar" "spam eggs"') == ['foo bar', 'spam eggs']
    assert split_args('"foo bar" "spam eggs" ham') == ['foo bar', 'spam eggs', 'ham']
    assert split_args('foo=bar spam') == ['foo=bar', 'spam']
    assert split_args('foo=bar spam=eggs') == ['foo=bar', 'spam=eggs']

    # Test handling of args splitted over lines

# Generated at 2022-06-13 04:31:32.838116
# Unit test for function split_args
def test_split_args():
    assert split_args(u"a='b c'") == [u"a='b c'"]  # double quotes are not supported

    assert split_args(u"a=b c=d") == [u"a=b", u"c=d"]
    assert split_args(u"a=b c=d ") == [u"a=b", u"c=d"]
    assert split_args(u"   a=b c=d") == [u"a=b", u"c=d"]
    assert split_args(u"a=b  c=d  ") == [u"a=b", u"c=d"]
    assert split_args(u"a=b\nc=d") == [u"a=b", u"c=d"]

# Generated at 2022-06-13 04:31:39.154431
# Unit test for function split_args

# Generated at 2022-06-13 04:31:51.830229
# Unit test for function split_args
def test_split_args():
    f = split_args

    assert f("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert f("a=b c=\\\"foo bar\\\"") == ['a=b', 'c=\\\"foo bar\\\"']
    assert f("a=b 'c=foo bar'") == ['a=b', "'c=foo bar'"]
    assert f("foo='{{ bar[1].baz }}'") == ["foo='{{ bar[1].baz }}'"]
    assert f("foo='{{ bar.baz }}'") == ["foo='{{ bar.baz }}'"]
    assert f("foo='{% foo %}'") == ["foo='{% foo %}'"]

# Generated at 2022-06-13 04:32:04.057760
# Unit test for function split_args
def test_split_args():
    # Check for list of args
    assert split_args('foo') == ['foo']
    assert split_args('foo bar') == ['foo', 'bar']
    assert split_args('foo="bar baz"') == ['foo="bar baz"']
    assert split_args('foo="bar baz" cat') == ['foo="bar baz"', 'cat']
    assert split_args('foo "bar baz"') == ['foo', '"bar baz"']
    assert split_args('foo="bar baz" cat="one two"') == ['foo="bar baz"', 'cat="one two"']
    assert split_args('foo="bar baz" cat="one two"') == ['foo="bar baz"', 'cat="one two"']

# Generated at 2022-06-13 04:32:14.185255
# Unit test for function split_args
def test_split_args():
    """
    Make sure we correctly handle all the various conditions in
    the split_args function
    """
    print("Testing split_args")


# Generated at 2022-06-13 04:32:26.160531
# Unit test for function split_args
def test_split_args():
    # Test various edge cases with the split args method
    # and make sure we get back what we expect
    assert split_args('foo="bar baz" one=two') == ['foo="bar baz"', 'one=two']
    assert split_args('foo="bar \\"baz\\"" one=two') == ['foo="bar \\"baz\\""', 'one=two']
    assert split_args('foo="bar \\\\"baz\\\\\\\\" one=two') == ['foo="bar \\\\"baz\\\\\\\\"', 'one=two']
    assert split_args('foo="bar \\\\"baz\\\\\\\\" \\\\"one\\\\=two') == ['foo="bar \\\\"baz\\\\\\\\"', '\\\\"one\\\\=two']

# Generated at 2022-06-13 04:32:32.825336
# Unit test for function split_args
def test_split_args():
    from ansible.utils import jsonify
    from ansible.compat.tests import unittest

    class TestSplitArgs(unittest.TestCase):

        def test_split_args(self):

            # example of a nested jinja2 block that needs to be reassembled
            # since all of it is not on the same line
            data = {
                'args': u'echo "{{ foo }}"',
                'kwargs': {},
                '_uses_shell': True,
            }
            expected = u'echo "{{ foo }}"'
            params = split_args(jsonify(data, format=False))
            self.assertEqual(params[0], expected)

            # example of an arg that is split over multiple lines, and needs to
            # be reassembled for jinja2
            # since all of it is not

# Generated at 2022-06-13 04:32:35.583173
# Unit test for function unquote
def test_unquote():
    assert unquote('"string"') == "string"
    assert unquote("'string'") == "string"
    assert unquote("string") == "string"



# Generated at 2022-06-13 04:32:55.343324
# Unit test for function split_args
def test_split_args():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:33:06.149680
# Unit test for function split_args

# Generated at 2022-06-13 04:33:13.837806
# Unit test for function split_args
def test_split_args():
    ''' '''
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    try:
        split_args("a=b c=\"foo bar")
    except Exception as e:
        assert "unbalanced quotes" in str(e)

    assert split_args("a={{foo}} b=\"{{bar}}\"") == ['a={{foo}}', 'b="{{bar}}"']

    try:
        split_args("a={{foo}} b=\"{{bar}}\" c={{baz}}")
    except Exception as e:
        assert "unbalanced jinja2 blocks" in str(e)

    assert split_args("a=\"foo\\\"bar\" b=bar\\'foo") == ['a="foo\\"bar"', "b=bar\\'foo"]


# Generated at 2022-06-13 04:33:26.749258
# Unit test for function split_args
def test_split_args():
    ''' unit test for function split_args '''
    from ansible.test.test_runner_arguments import TestModuleArgsParser
    parser = TestModuleArgsParser()
    #parser.add_argument('args', help='list of arguments', nargs='*')
    #options = parser.parse_args()


# Generated at 2022-06-13 04:33:38.536668
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo \\"bar\\""') == ['a=b', 'c="foo \\"bar\\""']
    assert split_args('a=b c="a \\\\ b"') == ['a=b', 'c="a \\\\ b"']
    assert split_args(r'a=b c="a \\\\ b"') == ['a=b', 'c="a \\\\ b"']
    assert split_args('a=b c="a \\n b"') == ['a=b', 'c="a \\n b"']

# Generated at 2022-06-13 04:33:50.833724
# Unit test for function split_args

# Generated at 2022-06-13 04:34:00.147061
# Unit test for function split_args
def test_split_args():
    import random, string

    def generate_random_string(length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

    def generate_random_whitespace(min, max):
        whitespace = ' '
        if random.random() < 0.5:
            whitespace += '\n'
        return whitespace * random.randint(min, max)

    def generate_random_token():
        token = ''
        if random.random() < 0.2:
            token += '{%'
        if random.random() < 0.2:
            token += generate_random_string(random.randint(0, 4))
        if random.random() < 0.2:
            token += '%}'

# Generated at 2022-06-13 04:34:09.673157
# Unit test for function split_args
def test_split_args():
    in_str = '''
    ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
    '''
    out_str = ['ansible_ssh_user=ubuntu', 'ansible_ssh_private_key_file=~/.ssh/id_rsa']
    assert split_args(in_str) == out_str

    in_str = '''
    a=b c="foo bar"
    '''
    out_str = ['a=b', 'c="foo bar"']
    assert split_args(in_str) == out_str

    in_str = '''
    a=b c="foo bar  \'"
    '''
    out_str = ['a=b', 'c="foo bar  \'"']

# Generated at 2022-06-13 04:34:15.461860
# Unit test for function split_args
def test_split_args():
    '''test_split_args unit test'''


# Generated at 2022-06-13 04:34:25.993710
# Unit test for function split_args
def test_split_args():
    from ansible import constants as C
    C.DEFAULT_MODULE_ARGS = "FOO=BAR"
    assert split_args("FOO=BAR") == ["FOO=BAR"]
    assert split_args("FOO=\"BAR\"") == ['FOO="BAR"']
    assert split_args("FOO='BAR'") == ["FOO='BAR'"]
    assert split_args("FOO=\"BAR BAZ\"") == ['FOO="BAR BAZ"']
    assert split_args("FOO='BAR BAZ'") == ["FOO='BAR BAZ'"]
    assert split_args("FOO=\"BAR BAZ\" QWE=\"ASD\" QAZ") == ['FOO="BAR BAZ"', 'QWE="ASD"', 'QAZ']

# Generated at 2022-06-13 04:34:46.038820
# Unit test for function split_args
def test_split_args():
    # Test of normal arg splitting
    args = "a=b c=d"
    assert split_args(args) == ['a=b', 'c=d']

    # Test with jinja2 block
    args = "a=b c={{ d }}"
    assert split_args(args) == ['a=b', 'c={{ d }}']

    # Test with quotes
    args = 'a=b c="foo bar"'
    assert split_args(args) == ['a=b', 'c="foo bar"']

    # Test with jinja2 block and quotes
    args = 'a=b c={{ "foo bar" }}'
    assert split_args(args) == ['a=b', 'c={{ "foo bar" }}']

    # Test with empty string
    args = ''

# Generated at 2022-06-13 04:34:50.973052
# Unit test for function split_args
def test_split_args():
    # Test regular args
    assert split_args('a=b c="d e"') == ['a=b', 'c="d e"']
    # Test args with spaces in quotes
    assert split_args('a=b c="d e f"') == ['a=b', 'c="d e f"']
    # Test args with spaces in quotes and escaped quotes
    assert split_args('a=b c="d e \"f\" g"') == ['a=b', 'c="d e \"f\" g"']
    # Test args with spaces in quotes and escaped spaces
    assert split_args('a=b c="d\\ e"') == ['a=b', 'c="d\\ e"']
    # Test args with spaces in quotes and escaped spaces and escaped quotes

# Generated at 2022-06-13 04:35:02.343298
# Unit test for function split_args
def test_split_args():
    # simple case where everything is quoted by itself
    # this is the easiest case for split_args to handle
    assert split_args('a="b c" d="e f"') == ['a="b c"', 'd="e f"']

    # when quotes are nested within a jinja2 block and vice-versa
    assert split_args('a="{{foo}}" b={{"{{"}} c="{% if x %} X {% endif %}"') == ['a="{{foo}}"', 'b={{"{{"}}', 'c="{% if x %} X {% endif %}"']

    # properly handle quotes inside jinja2 blocks that might be unclosed
    assert split_args('a="{{foo}}') == ['a="{{foo}}']

# Generated at 2022-06-13 04:35:09.771257
# Unit test for function split_args

# Generated at 2022-06-13 04:35:20.653169
# Unit test for function split_args
def test_split_args():
    failed = False

# Generated at 2022-06-13 04:35:31.762418
# Unit test for function split_args

# Generated at 2022-06-13 04:35:41.022973
# Unit test for function split_args

# Generated at 2022-06-13 04:35:48.144555
# Unit test for function split_args
def test_split_args():

    import pytest


# Generated at 2022-06-13 04:35:56.418719
# Unit test for function split_args
def test_split_args():
    ''' test split_args functionality '''
    import sys
    import datetime
    import traceback

# Generated at 2022-06-13 04:36:04.402616
# Unit test for function split_args

# Generated at 2022-06-13 04:36:47.065346
# Unit test for function split_args

# Generated at 2022-06-13 04:36:57.219503
# Unit test for function split_args
def test_split_args():

    # Test 1: Split on spaces, no quotes or jinja2
    args = "one two three four five six"
    result = split_args(args)
    assert result == ['one', 'two', 'three', 'four', 'five', 'six']

    # Test 2: Split on newlines, no quotes or jinja2
    args = "one\ntwo\n\nthree\nfour\nfive\nsix"
    result = split_args(args)
    assert result == ['one', 'two', '\nthree', 'four', 'five', 'six']

    # Test 3: Split on newlines, with quotes and line continuations
    args = "one\n\ntwo 'three\nthree'\nfour\nfive six\\\nseven eight\nnine"
    result = split_args(args)


# Generated at 2022-06-13 04:37:03.018581
# Unit test for function split_args
def test_split_args():
    data = 'a=b key1="quote1" c="foo bar" key2="quot\'e2"'
    res = split_args(data)
    assert res == ['a=b', 'key1="quote1"', 'c="foo bar"', "key2=\"quot'e2\""]

    data = 'a=b key1="quote1" c="foo bar" key2="quote2'
    try:
        res = split_args(data)
        assert False, "Expected Exception"
    except Exception:
        pass

    data = """a=b
    c="foo bar"
    "d=e f=g"
    h="i 'j' k"
    l="m \"n\" o" p=q
    """
    res = split_args(data)

# Generated at 2022-06-13 04:37:07.816010
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b 'c=foo bar'") == ['a=b', "c=foo bar"]
    assert split_args("a=b 'c:foo bar'") == ['a=b', "c:foo bar"]
    assert split_args("a=b c='foo bar'") == ['a=b', "c='foo bar'"]
    assert split_args("a=b c=\"foo \\\"bar\\\"\"") == ['a=b', 'c="foo \\"bar\\""']
    assert split_args("a=b 'c=foo bar' d='foo bar'") == ['a=b', "c=foo bar", "d='foo bar'"]
    assert split_args

# Generated at 2022-06-13 04:37:13.588159
# Unit test for function split_args
def test_split_args():
    # Split on space, but not inside quoted string
    # 'a=b c="foo bar"' -> ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

    # Split on space, but not inside jinja2 block
    # '{{ foo }} {{bar}}' -> ['{{ foo }}', '{{bar}}']
    assert split_args('{{ foo }} {{bar}}') == ['{{ foo }}', '{{bar}}']

    # Split on space, but not inside quoted string or jinja2 block
    # '{{ foo }} a="{{bar}}"' -> ['{{ foo }}', 'a="{{bar}}"']

# Generated at 2022-06-13 04:37:23.759635
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c='foo bar'") == ['a=b', 'c=\'foo bar\'']
    assert split_args("a=b c=\"foo\\\"bar\"") == ['a=b', 'c="foo\"bar"']
    assert split_args("a=b c=\"foo\"\"bar\"") == ['a=b', 'c="foo""bar"']
    assert split_args("a=b c=\"foo\\'bar\"") == ['a=b', 'c="foo\'bar"']

# Generated at 2022-06-13 04:37:34.889393
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args("a='foo bar'") == ["a='foo bar'"]
    assert split_args("a=b \\\nc=d") == ["a=b", "c=d"]
    assert split_args("a=b \\") == ["a=b"]
    assert split_args("a=b \\\nc=d \\\ne=f") == ["a=b", "c=d", "e=f"]
    assert split_args("a=b c=d e=f") == ["a=b", "c=d", "e=f"]
    assert split_args("a=b c=d e=f") == ["a=b", "c=d", "e=f"]
   

# Generated at 2022-06-13 04:37:44.644496
# Unit test for function split_args

# Generated at 2022-06-13 04:37:53.675581
# Unit test for function split_args
def test_split_args():
    import unittest2 as unittest

    class TestSplitArgsUnquoted(unittest.TestCase):
        def _test_unquoted(self, args, expected_params):
            params = split_args(args)
            message = "input args: %s\ngenerated params: %s\nexpected params: %s" % (args, params, expected_params)
            self.assertEqual(params, expected_params, message)

        def test_no_args(self):
            self._test_unquoted('', [])

        def test_no_args_whitespace(self):
            self._test_unquoted('    ', [])

        def test_one_arg(self):
            self._test_unquoted('foo', ['foo'])


# Generated at 2022-06-13 04:38:01.380301
# Unit test for function split_args
def test_split_args():

    assert split_args('') == []
    assert split_args('   ') == []
    assert split_args('one') == ['one']
    assert split_args('one two') == ['one', 'two']
    assert split_args('one "two three"') == ['one', '"two three"']
    assert split_args('one "two three" four') == ['one', '"two three"', 'four']
    assert split_args('one "two ""three"" four"') == ['one', '"two ""three"" four"']

    assert split_args('one \\\\ two') == ['one', '\\\\', 'two']
    assert split_args('one \\\\ "two three"') == ['one', '\\\\', '"two three"']


# Generated at 2022-06-13 04:39:14.008791
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\" d={{ e }}") == ['a=b', 'c="foo bar"', 'd={{', 'e', '}}']
    assert split_args("- name='foo bar'") == ['-', 'name=\'foo bar\'']
    assert split_args("- name='foo bar' - debug") == ['-', 'name=\'foo bar\'', '-', 'debug']
    assert split_args("foo={{ bar }}") == ['foo={{', 'bar', '}}']
    assert split_args("foo={{ bar }}\nfoo2=bar2") == ['foo={{', 'bar', '}}\nfoo2=bar2']


# Generated at 2022-06-13 04:39:18.746916
# Unit test for function split_args

# Generated at 2022-06-13 04:39:27.337568
# Unit test for function split_args

# Generated at 2022-06-13 04:39:35.866686
# Unit test for function split_args

# Generated at 2022-06-13 04:39:43.364251
# Unit test for function split_args

# Generated at 2022-06-13 04:39:48.700014
# Unit test for function split_args
def test_split_args():
    '''
    split_args unit tests
    '''

    if _get_quote_state('foo bar', None) != None:
        raise Exception('simple parameter did not return None quote')
    if _get_quote_state('"foo bar', None) != '"':
        raise Exception('starting quoted string did not return the quote character')
    if _get_quote_state('"foo bar"', None) != None:
        raise Exception('ending quoted string did not return None')
    if _get_quote_state('"foo bar\" baz', '"') != '"':
        raise Exception('ending quoted string in escaped quotes did not return the quote character')
    if _get_quote_state('"foo bar\" baz"', '"') != None:
        raise Exception('ending quoted string in escaped quotes did not return None')

# Generated at 2022-06-13 04:39:58.239441
# Unit test for function split_args
def test_split_args():
    '''
    This is a simple function to execute test cases
    for the split_args function.
    '''
    # a dictionary of input arg strings with their expected result values
    # these test cases will be used to compare with the actual output

# Generated at 2022-06-13 04:40:07.269845
# Unit test for function split_args
def test_split_args():
    # Simple non-complex tests
    assert split_args("a=b c=d") == ["a=b", "c=d"]
    assert split_args("a=b c='d e'") == ["a=b", "c='d e'"]
    assert split_args("a=b c=\"d e\"") == ["a=b", "c=\"d e\""]
    assert split_args("a=b c=\"d\"\"e\"") == ["a=b", "c=\"d\"\"e\""]
    assert split_args("a=b c='d''e'") == ["a=b", "c='d''e'"]
    assert split_args("a=b c='d\\'e'") == ["a=b", "c='d\\'e'"]

# Generated at 2022-06-13 04:40:17.728082
# Unit test for function split_args
def test_split_args():
    ''' returns variable containing test for function "split_args":
        split_args(args) => test
    '''
    # no jinja2 block, no quotes

# Generated at 2022-06-13 04:40:27.837957
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo\\"bar\\""') == ['a=b', 'c="foo\\"bar\\""']
    assert split_args('a=b c="foo') == ['a=b', 'c="foo']
    assert split_args('a=b c=\\"foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo bar') == ['a=b', 'c="foo bar']
    assert split_args('a=b c="foo \\"bar"') == ['a=b', 'c="foo \\"bar"']