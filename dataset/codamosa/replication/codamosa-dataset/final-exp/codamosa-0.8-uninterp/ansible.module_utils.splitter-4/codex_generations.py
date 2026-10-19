

# Generated at 2022-06-13 04:31:16.571686
# Unit test for function split_args
def test_split_args():

    # Simple args
    (rc, stdout, stderr) = assert_split_args("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    (rc, stdout, stderr) = assert_split_args("a=b", ['a=b'])

    # Args with embedded newlines
    (rc, stdout, stderr) = assert_split_args("a=b\nc='foo bar' d=foo\\\ne=bar", ['a=b\n', "c='foo bar'", 'd=foo\n', 'e=bar'])

    # Args with embedded quotes
    (rc, stdout, stderr) = assert_split_args('a=b c="foo bar"', ['a=b', 'c="foo bar"'])

# Generated at 2022-06-13 04:31:23.016019
# Unit test for function split_args
def test_split_args():
    # Standard Cases
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"\ndef="hi \\"hi\\""') == ['a=b', 'c="foo bar"\ndef="hi \\"hi\\""']
    assert split_args('a=b c="foo bar"\ndef="hi \\"hi\\""') == ['a=b', 'c="foo bar"\ndef="hi \\"hi\\""']
    assert split_args('a=b c="foo bar" ') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2022-06-13 04:31:32.787333
# Unit test for function split_args
def test_split_args():
    # simple test with basic args
    simple_test_args = "foo=bar baz=qux"
    simple_test_result = ['foo=bar', 'baz=qux']
    simple_test_parsed = split_args(simple_test_args)

    assert simple_test_result == simple_test_parsed

    # test with quoted args
    quoted_test_args = "foo='bar baz' one=\"qux quux\""
    quoted_test_result = ["foo='bar baz'", 'one="qux quux"']
    quoted_test_parsed = split_args(quoted_test_args)

    assert quoted_test_result == quoted_test_parsed

    # test with jinja2 blocks

# Generated at 2022-06-13 04:31:39.014624
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('"hello world"') == True
    assert is_quoted("'hello world'") == True
    assert is_quoted('"hello world') == False
    assert is_quoted("'hello world") == False
    assert is_quoted('hello world"') == False
    assert is_quoted("hello world'") == False


# Generated at 2022-06-13 04:31:48.395974
# Unit test for function unquote
def test_unquote():
    # Test case 1 :
    test_input = '"Unquoted input"'
    expected_result = 'Unquoted input'
    recieved_result = unquote(test_input)
    assert recieved_result == expected_result
    # Test case 2 :
    test_input = "This is 'test' case"
    expected_result = "This is 'test' case"
    recieved_result = unquote(test_input)
    assert recieved_result == expected_result



# Generated at 2022-06-13 04:31:52.432587
# Unit test for function unquote
def test_unquote():
    assert unquote("abcd") == "abcd"
    assert unquote("\"abcd\"") == "abcd"
    assert unquote("'abcd'") == "abcd"
    assert unquote("'a'b'c'd'") == "'a'b'c'd'"


# Generated at 2022-06-13 04:31:58.915739
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted('') is False
    assert is_quoted('"""') is False
    assert is_quoted("'''") is False
    assert is_quoted('"a"') is True
    assert is_quoted("'b'") is True
    assert is_quoted('"abc"') is True
    assert is_quoted("'abc'") is True


# Generated at 2022-06-13 04:32:10.714851
# Unit test for function split_args
def test_split_args():
    # test for github issue #37437

    # Setup
    test_cases = []
    test_cases.append((['a=b', 'c="foo bar"', 'e=f', 'g=h'], "a=b c=\"foo bar\"\ne=f\ng=h"))
    test_cases.append((['a=b', 'c="foo bar"', 'e=f', 'g=h'], "a=b c=\"foo bar\"\ne=f\ng=h\n"))
    test_cases.append((['a=b', 'c="foo bar"', 'e=f', 'g=h'], "a=b c=\"foo bar\"\ne=f\ng=h\n\n"))

# Generated at 2022-06-13 04:32:17.257827
# Unit test for function unquote
def test_unquote():
    assert unquote('hello world') == 'hello world'
    assert unquote('"hello world"') == 'hello world'
    assert unquote('"hello \'world"') == 'hello \'world'
    assert unquote('\'hello "world\'') == 'hello "world'
    assert unquote('"hello \'world\'"') == 'hello \'world\''


# Generated at 2022-06-13 04:32:21.838924
# Unit test for function is_quoted
def test_is_quoted():
    assert is_quoted("hello") is False
    assert is_quoted("'hello'") is True
    assert is_quoted('"hello"') is True
    assert is_quoted('hello"') is False
    assert is_quoted('"hello') is False
    assert is_quoted("'hello") is False
    assert is_quoted("hello'") is False
    assert is_quoted("'hello\'s'") is True
    assert is_quoted("\"hello\'s\"") is True


# Generated at 2022-06-13 04:32:43.906987
# Unit test for function split_args
def test_split_args():
    import ansible.constants as C
    from units.compat.mock import patch
    from ansible.module_utils import basic

    # Retrieve the function to test, which is a function nested inside module basic
    split_args_function = getattr(basic, "split_args")

    # Test split with quotes
    literal_test = "command a=\"b c d\" e='f g h' i=j"
    parsed_test = ['command', 'a="b c d"', "e='f g h'", 'i=j']
    assert split_args_function(literal_test) == parsed_test

    # Test split with backslash
    literal_test = "command a=b\\\\c d=e\\\\ f=g"

# Generated at 2022-06-13 04:32:52.721609
# Unit test for function split_args
def test_split_args():
    '''
    Unit tests for the function split_args for various scenarios that this function
    should handle properly.

    To run this test, execute this module as a script, like so:
    python lib/ansible/utils/module_docs_fragments.py

    The output should indicate if any tests failed, or if all tests passed.
    '''


# Generated at 2022-06-13 04:33:03.362874
# Unit test for function split_args
def test_split_args():
    assert split_args(u'echo "{{ a }}"') == ['echo', '"{{ a }}"']
    assert split_args(u"echo '{{ a }}'") == ['echo', "'{{ a }}'"]
    assert split_args(u"echo '{% if a %}'\necho '{{ a }}'\necho '{% endif %}'") == ["echo '{% if a %}'", "echo '{{ a }}'", "echo '{% endif %}'"]
    assert split_args(u"{{ a }}\necho {{ a }}\n{% if a %}echo {{ a }}{% endif %}") == ['{{ a }}', 'echo {{ a }}', '{% if a %}echo {{ a }}{% endif %}']

# Generated at 2022-06-13 04:33:08.432829
# Unit test for function split_args
def test_split_args():
    import sys
    import unittest

    if sys.version_info >= (3, 0):
        unittest = unittest.TestCase('__init__')  # pylint: disable=invalid-name

    # Tests for basic functionality
    unittest.assertEqual(split_args('a=b c="foo bar"'), ['a=b', 'c="foo bar"'])
    unittest.assertEqual(split_args('a=b c="foo bar" "d=e f=g"'), ['a=b', 'c="foo bar"', '"d=e f=g"'])

# Generated at 2022-06-13 04:33:14.629041
# Unit test for function split_args
def test_split_args():
    assert(split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"'])
    assert(split_args('a=b c="foo bar" d=\'foo bar\'') == ['a=b', 'c="foo bar"', "d='foo bar'"])
    assert(split_args('a=b c=" foo bar" d=\' foo bar\'') == ['a=b', 'c=" foo bar"', "d=' foo bar'"])
    assert(split_args('a=b c=\\"foo bar\\"') == ['a=b', 'c=\\"foo bar\\"'])
    assert(split_args('a=b c=\\"foo bar\\"') == ['a=b', 'c=\\"foo bar\\"'])

# Generated at 2022-06-13 04:33:27.381152
# Unit test for function split_args
def test_split_args():
    def _test_split(input, expected_output):
        o = split_args(input)
        if o != expected_output:
            print("FAILURE")
            print("INPUT:")
            print(input)
            print("EXPECTED:")
            print(expected_output)
            print("ACTUAL:")
            print(o)
            raise Exception("TEST FAILED")

    _test_split('', [])
    _test_split('   ', [])
    _test_split('"\\""', ['"'])
    _test_split('\\', ['\\'])
    _test_split('\\\\', ['\\\\'])
    _test_split('"a', ['"a'])
    _test_split('"a\\"', ['"a"'])

# Generated at 2022-06-13 04:33:39.170234
# Unit test for function split_args
def test_split_args():
    # The following tests are taken from the documentation for shlex.split:
    assert split_args("spam") == ['spam']
    assert split_args("spam, eggs") == ['spam,', 'eggs']
    assert split_args("spam, eggs, and ham") == ['spam, eggs, and ham']
    assert split_args("'spam, eggs, and ham'") == ["'spam, eggs, and ham'"]
    assert split_args("'spam, eggs, and ham' and cheese") == ["'spam, eggs, and ham'", 'and', 'cheese']
    assert split_args("spam ") == ['spam']
    assert split_args("spam, eggs and ham") == ['spam,', 'eggs', 'and', 'ham']

    # The following tests are taken

# Generated at 2022-06-13 04:33:51.414220
# Unit test for function split_args

# Generated at 2022-06-13 04:34:00.978643
# Unit test for function split_args
def test_split_args():

    args = ''
    params = split_args(args)
    assert params == []
    args = 'a=b'
    params = split_args(args)
    assert params == ['a=b']
    args = ' a=b'
    params = split_args(args)
    assert params == ['a=b']
    args = ' a=b '
    params = split_args(args)
    assert params == ['a=b']
    args = ' a=b c="foo bar"'
    params = split_args(args)
    assert params == ['a=b', 'c="foo bar"']
    args = ' a=b c="foo bar" '
    params = split_args(args)
    assert params == ['a=b', 'c="foo bar"']

# Generated at 2022-06-13 04:34:10.411461
# Unit test for function split_args

# Generated at 2022-06-13 04:34:33.911311
# Unit test for function split_args
def test_split_args():
    import sys

    # testcases/results tuples

# Generated at 2022-06-13 04:34:43.655802
# Unit test for function split_args
def test_split_args():
    ''' Unit test for utils.split_args '''


# Generated at 2022-06-13 04:34:55.931846
# Unit test for function split_args
def test_split_args():
    # basic test
    arg = "foo bar baz"
    params = split_args(arg)
    assert params == ['foo', 'bar', 'baz']

    # test with quoted arg
    arg = "foo bar 'baz' bat"
    params = split_args(arg)
    assert params == ['foo', 'bar', 'baz', 'bat']

    # test with quoted arg
    arg = "foo bar 'baz bat'"
    params = split_args(arg)
    assert params == ['foo', 'bar', 'baz bat']

    # test with quoted arg with spaces
    arg = "foo bar 'baz bat bing'"
    params = split_args(arg)
    assert params == ['foo', 'bar', 'baz bat bing']

    # test with quoted arg with escaped quote

# Generated at 2022-06-13 04:35:07.139531
# Unit test for function split_args
def test_split_args():
    import pytest
    def assert_split_args(args, expected):
        result = split_args(args)
        assert result == expected, "expected '%s' but got '%s'" % (' '.join(expected), ' '.join(result))
    assert_split_args("a=b c='foo bar'", ['a=b', "c='foo bar'"])
    assert_split_args('a=b c="foo bar"', ['a=b', 'c="foo bar"'])
    assert_split_args('a=b c="foo bar baz"', ['a=b', 'c="foo bar baz"'])
    assert_split_args('a=b c="foo bar baz" one two three', ['a=b', 'c="foo bar baz"', 'one', 'two', 'three'])
   

# Generated at 2022-06-13 04:35:17.765664
# Unit test for function split_args

# Generated at 2022-06-13 04:35:26.000613
# Unit test for function split_args
def test_split_args():
    '''
    Unit test for the split_args function - the goal here is to make sure
    that any strings that are part of a jinja2 expression are not broken apart
    incorrectly by the whitespace splitting.
    '''
    def run_tests(tests, expected, function=split_args):
        for idx, test in enumerate(tests):
            params = function(test['args'])
            if params != test['expected']:
                print("TEST %s FAILED, expected: %s, got: %s" % (idx, test['expected'], params))
                assert False
        print("%s tests passed" % expected)


# Generated at 2022-06-13 04:35:36.984551
# Unit test for function split_args
def test_split_args():
    '''unit test for function above'''

    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b 'c=foo bar'") == ['a=b', "'c=foo bar'"]
    assert split_args("a=b \"c=foo bar\"") == ['a=b', '"c=foo bar"']
    assert split_args("a=\"foo bar\"") == ['a="foo bar"']
    assert split_args("a=\"foo bar\" b=\"baz qux\"") == ['a="foo bar"', 'b="baz qux"']
    assert split_args("a=\"foo bar\" b='baz qux'") == ['a="foo bar"', "b='baz qux'"]
    assert split

# Generated at 2022-06-13 04:35:45.095681
# Unit test for function split_args
def test_split_args():
    assert split_args("a=b c='d e' f='g''h'") == ['a=b', "c='d e'", "f='g''h'"]
    assert split_args("a=b c='d e' f='g''h i'") == ['a=b', "c='d e'", "f='g''h i'"]
    assert split_args("a=b c='d e' f='g''h' i=1") == ['a=b', "c='d e'", "f='g''h'", 'i=1']
    assert split_args("'a=b c='d e' f='g''h i j' k=1'") == ["'a=b c='d e' f='g''h i j' k=1'"]

# Generated at 2022-06-13 04:35:51.113541
# Unit test for function split_args

# Generated at 2022-06-13 04:36:00.395590
# Unit test for function split_args
def test_split_args():
    import unittest as ut

    class TestSequenceFunctions(ut.TestCase):

        def setUp(self):
            self.sep = '\n'

        def test_split_args(self):
            arg_string = '''
            arg1 arg2="arg2 value" arg3=qwerty arg4='arg4 value' arg5="arg5 value with spaces"
            arg6=arg6value arg7=quo"ted arg8=quo'ted arg9={{jinj2 block quoted arg10=should fail}}
            arg11="should fail}} arg12="should fail}} arg13="should fail}} arg14='should fail}'
            arg15="should fail}' arg16='should fail}'
            '''

            args = split_args(arg_string)


# Generated at 2022-06-13 04:36:17.431552
# Unit test for function split_args
def test_split_args():
    assert split_args('foo=bar key="val"') == ['foo=bar', 'key="val"']



# Generated at 2022-06-13 04:36:22.378964
# Unit test for function split_args
def test_split_args():
    all_passed = True
    function = 'split_args'
    data = dict()

    data['no list'] = dict(
        args='a=b c=d e=f g h',
        params=['a=b', 'c=d', 'e=f', 'g', 'h'],
    )
    data['list'] = dict(
        args='a=b c=d e=f "g h" i=j k="l m"',
        params=['a=b', 'c=d', 'e=f', '"g h"', 'i=j', 'k="l m"'],
    )

# Generated at 2022-06-13 04:36:32.740958
# Unit test for function split_args
def test_split_args():
    import sys
    import re

    arg_tests = dict()

    def quote_for_shell(arg):
        '''Quote argument for use in shells like bash and cmd.exe'''
        if arg == '':
            return "''"

        result = re.match(r"(^[a-zA-Z0-9._/-]+$)", arg)
        if result and len(arg) == len(result.group()):
            return arg
        else:
            if sys.platform.startswith('win'):
                # Need to handle things like "C:\Program Files\something"
                if re.match(r'[-./\\a-zA-Z0-9_:]+$', arg):
                    return arg

                # Need to handle things like "\\host\share\some file.txt"

# Generated at 2022-06-13 04:36:43.363480
# Unit test for function split_args
def test_split_args():
    assert split_args(u"one t\wo thr\tee") == [u"one", u"t\wo", u"thr\tee"]
    assert split_args(u"one {# one #}") == [u"one"]
    assert split_args(u"{# one #}two") == [u"two"]
    assert split_args(u"one{# one #}two") == [u"one{# one #}two"]
    assert split_args(u"one {# one #}two{# one #}") == [u"one", u"two{# one #}"]
    assert split_args(u"one {# one #}two{# one #}three") == [u"one", u"two{# one #}three"]

# Generated at 2022-06-13 04:36:52.663757
# Unit test for function split_args
def test_split_args():

    assert split_args('"foo bar"') == ['foo bar']
    assert split_args('foo bar') == ['foo', 'bar']

    assert split_args('foo "bar baz"') == ['foo', 'bar baz']
    assert split_args('foo="bar baz"') == ['foo=bar baz']

    assert split_args('foo "bar \'baz qux\'"') == ['foo', 'bar \'baz qux\'']
    assert split_args('foo=\'bar "baz qux"\'') == ['foo=bar "baz qux"']

    assert split_args('foo bar "foo bar" baz') == ['foo', 'bar', 'foo bar', 'baz']

    # test the special case of the last character

# Generated at 2022-06-13 04:37:00.422634
# Unit test for function split_args

# Generated at 2022-06-13 04:37:12.053508
# Unit test for function split_args
def test_split_args():
    '''
    runs tests to verify the split_args function is returning
    the correct results.
    '''
    from ansible.module_utils.common._collections_compat import Mapping


# Generated at 2022-06-13 04:37:23.265236
# Unit test for function split_args
def test_split_args():
    import unittest
    class SplitArgsTestCase(unittest.TestCase):

        class ModuleFailException(Exception):
            def __init__(self, value):
                self.value = value
            def __str__(self):
                return repr(self.value)

        def check_args(self, expected, args):
            try:
                result = split_args(args)
            except self.ModuleFailException as e:
                result = e.value
            msg = "For argument '%s' got %s instead of %s" % (args, result, expected)
            self.assertEquals(expected, result, msg)

        def test_args_1(self):
            ''' test basic splitting on spaces '''
            args = 'a=b c="foo bar"'

# Generated at 2022-06-13 04:37:34.849013
# Unit test for function split_args

# Generated at 2022-06-13 04:37:44.611145
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b "c=foo bar"') == ['a=b', '"c=foo bar"']
    assert split_args('a=b "c=foo\nbar"') == ['a=b', '"c=foo\nbar"']
    assert split_args('a=b "c=foo\nbar\\\ndoo"') == ['a=b', '"c=foo\nbar\ndoo"']
    assert split_args('a=b "c=foo\nbar\\\ndoo\ndah"') == ['a=b', '"c=foo\nbar\ndoo\ndah"']

# Generated at 2022-06-13 04:38:30.475467
# Unit test for function split_args
def test_split_args():
    params = split_args('a=b c="foo bar"\ne="1 2 3"')
    assert len(params) == 3
    assert params[0] == 'a=b'
    assert params[1] == 'c="foo bar"'
    assert params[2] == 'e="1 2 3"'

    params = split_args('"a b c"')
    assert len(params) == 1
    assert params[0] == '"a b c"'

    params = split_args("'''a b c'''")
    assert len(params) == 1
    assert params[0] == "'''a b c'''"

    params = split_args("'''a\nb c'''")
    assert len(params) == 1
    assert params[0] == "'''a\nb c'''"


# Generated at 2022-06-13 04:38:37.280962
# Unit test for function split_args
def test_split_args():
    ''' tests for arg parsing logic '''

    # Simple test cases
    assert split_args('"foo bar"') == ['foo bar']
    assert split_args("'foo bar'") == ['foo bar']

    # Make sure that line continuations are handled
    assert split_args("a=b \\\n c=d") == ['a=b', 'c=d']

    # Test parsing of strings with quotes inside quotes
    assert split_args("foo=\"bar \\\" baz\"") == ['foo=bar \\" baz']
    assert split_args("foo=\"bar \\' baz\"") == ["foo=bar ' baz"]
    assert split_args("foo='bar \" baz'") == ['foo=bar " baz']

# Generated at 2022-06-13 04:38:49.118064
# Unit test for function split_args
def test_split_args():

    assert split_args("a=b c=\"foo bar\"") == ['a=b', 'c="foo bar"']
    assert split_args("a=b c=\"foo bar\" d={{foo}} e={% bar %} f={# bar #}") == ['a=b',
                                                                                   'c="foo bar"',
                                                                                   'd={{foo}}',
                                                                                   'e={% bar %}',
                                                                                   'f={# bar #}']
    assert split_args("a=\"{{foo}}\" b=\"{% bar %}\" c=\"{# bar #}\"") == ['a="{{foo}}"',
                                                                            'b="{% bar %}"',
                                                                            'c="{# bar #}"']

# Generated at 2022-06-13 04:38:59.968125
# Unit test for function split_args
def test_split_args():
    args = 'first_arg "foo bar" third_arg'
    assert split_args(args) == ['first_arg', '"foo bar"', 'third_arg']

    args = 'first_arg "foo bar" "{{foo" third_arg'
    assert split_args(args) == ['first_arg', '"foo bar"', '"{{foo"', 'third_arg']

    args = r'''first_arg "foo bar" "{{foo" third_arg {% for x in y %}
    {# {{ foo bar baz
    the quick brown fox jumps over the lazy dog
    %} {# foo bar baz #}'''

# Generated at 2022-06-13 04:39:09.832076
# Unit test for function split_args
def test_split_args():

    assert split_args('a=b key="{{ foo }}"') == ['a=b', 'key="{{ foo }}"']
    assert split_args('a=b key="{{ a }}" key2="{{ b }}"') == ['a=b', 'key="{{ a }}"', 'key2="{{ b }}"']
    assert split_args('a=b key="{{ a }} {{ b }}"') == ['a=b', 'key="{{ a }} {{ b }}"']
    assert split_args('a=b key="{{ a }} {{ b }}" key2="{{ c }}"') == ['a=b', 'key="{{ a }} {{ b }}"', 'key2="{{ c }}"']

# Generated at 2022-06-13 04:39:16.788041
# Unit test for function split_args

# Generated at 2022-06-13 04:39:26.593278
# Unit test for function split_args
def test_split_args():
    ''' test split args '''
    # these are the inputs and expected outputs

# Generated at 2022-06-13 04:39:34.741459
# Unit test for function split_args
def test_split_args():
    import json
    import sys


# Generated at 2022-06-13 04:39:42.701157
# Unit test for function split_args
def test_split_args():

    # test basic args
    s = "a=b c='d e' f={{foo}}"
    assert split_args(s) == ['a=b', "c='d e'", 'f={{foo}}']

    # test arg with newline
    s = "a=b c='d e \n f'"
    assert split_args(s) == ['a=b', "c='d e \n f'"]

    # test arg with line continuation
    s = "a=b c='d e \\ \n f'"
    assert split_args(s) == ['a=b', "c='d e \\ \n f'"]

    # test args with both newline and line continuation
    s = "a=b c='d e \\ \n f'\n g='h i \n j'"

# Generated at 2022-06-13 04:39:53.218503
# Unit test for function split_args