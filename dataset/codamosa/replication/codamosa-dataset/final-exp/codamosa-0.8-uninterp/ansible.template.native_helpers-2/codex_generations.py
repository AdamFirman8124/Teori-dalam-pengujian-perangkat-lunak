

# Generated at 2022-06-22 12:01:16.007436
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    env = jinja2.Environment(variable_start_string='[', variable_end_string=']', undefined=StrictUndefined)
    nodes = env.compile_expression('[a]|join(", ")').body.iter_child_nodes()
    assert ansible_native_concat(nodes) == 'a'

    nodes = env.compile_expression('[a, b]|join(", ")').body.iter_child_nodes()
    assert ansible_native_concat(nodes) == 'a, b'

    nodes = env.compile_expression('''
    [
        {% if True %}
            "a"
        {% else %}
            "b"
        {% endif %}
    ]
    ''').body.iter

# Generated at 2022-06-22 12:01:28.529712
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert 'foo' == ansible_native_concat([u'foo'])
    assert 'foobar' == ansible_native_concat([u'foo', u'bar'])
    assert ['foo', 'bar'] == ansible_native_concat([u'foo', u',', u'bar'])
    assert 100 == ansible_native_concat([u'1', u'0', u'0'])
    assert [u'foo', 100] == ansible_native_concat(
        [u'foo', u',', u'1', u'0', u'0']
    )
    assert 'foo bar' == ansible_native_concat([u'foo', u' ', u'bar'])

# Generated at 2022-06-22 12:01:37.862534
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test if nodes is a generator
    assert ansible_native_concat(n for n in [1]) == 1
    assert ansible_native_concat(n for n in ['1']) == '1'

    # Test if nodes is an iterable
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', 2, '3']) == '123'

    # Test if the results can be parsed by ast.literal_eval
    assert ansible_native_concat([1, 2]) == 3

# Generated at 2022-06-22 12:01:50.618639
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    from jinja2._compat import string_types, text_type

    class TestEnv(jinja2.Environment):
        def _generate(self, source, name, filename=None, defer_init=False):
            return jinja2.compiler.Generator(self, source, name, filename, defer_init)

        def _parse(self, source, name, filename, defer_init=False):
            return jinja2.parser.Parser(self, source, name, filename, defer_init).parse()

        def _compile_from_string(self, source, name, filename):
            return self._generate(self._parse(source, name, filename), name, filename, True)

    env = TestEnv(extensions=['jinja2.ext.i18n'])


# Generated at 2022-06-22 12:02:02.885645
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:02:14.066926
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Unit test for ansible_native_concat"""

    def assert_equal(a, b, msg=""):
        assert a == b, "{0}: {1} != {2}".format(msg, a, b)

    assert_equal(ansible_native_concat([]), None, "empty test")

    assert_equal(ansible_native_concat([1]), 1, "single number")
    assert_equal(ansible_native_concat([1.1]), 1.1, "single float")
    assert_equal(ansible_native_concat(["a"]), "a", "single string")

    assert_equal(ansible_native_concat([1, 2, 3]), "123", "number concat")

# Generated at 2022-06-22 12:02:26.160832
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    "Test function used by integration tests"
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([u'a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([u'a', u'b']) == 'ab'
    assert ansible_native_concat([u'a', 'b']) == 'ab'
    assert ansible_native_concat([u'a', 1]) == 'a1'
    assert ansible_native_concat([u'a', True]) == 'aTrue'
    assert ansible_native_concat(['a', 1]) == 'a1'

# Generated at 2022-06-22 12:02:34.039727
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None is ansible_native_concat([])
    assert None is ansible_native_concat([None])
    assert '' == ansible_native_concat([''])
    assert 'foo' == ansible_native_concat(['foo'])
    assert 1 == ansible_native_concat([1])
    assert [1, 2, 3] == ansible_native_concat([[1, 2, 3]])
    assert {'k': 'v'} == ansible_native_concat([{'k': 'v'}])
    assert {'k1': 'v1', 'k2': 'v2'} == ansible_native_concat([{'k1': 'v1'}, {'k2': 'v2'}])
    assert 'foobar' == ansible_native_concat

# Generated at 2022-06-22 12:02:45.955111
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import datetime
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 'a', 3]) == '1a3'
    assert ansible_native_concat([1, u'a', 3]) == '1a3'
    assert ansible_native_concat([True, 'a', 3]) == 'Truea3'
    assert ansible_native_concat(['a', 'b', 'c']).endswith('abc')
    assert ansible_native_concat([1, 2, 3, 4]).endswith('1234')

# Generated at 2022-06-22 12:02:50.884024
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['bar']) == 'bar'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(iter(['foo', 'bar'])) == 'foobar'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat(['foo', 42]) == 'foo42'
    assert ansible_native_concat([["foo", "bar"], "baz"]) == ["foo", "bar", "baz"]
    assert ansible_native_concat(['[1,2,3]', '[4,5,6]']) == [1, 2, 3, 4, 5, 6]
    assert ansible_native_

# Generated at 2022-06-22 12:03:06.162669
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment()
    env.native_concatenation = True
    t = env.from_string("{{ [1, 2, 3] }}")
    assert t.render() == [1, 2, 3]

    t = env.from_string("{{ [1, 2, 3] | join(', ') }}")
    assert t.render() == '1, 2, 3'

    t = env.from_string("{{ ['a', 'b', 'c'] | join(', ') }}")
    assert t.render() == 'a, b, c'

    t = env.from_string('{{ "abceabcf" | regex_replace("abc", "zzz") }}')
    assert t.render() == 'zzzeabcf'


# Generated at 2022-06-22 12:03:17.248763
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 'b', 'c', 'd']) == 'abcd'
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, 3, 4]) == 1234

# Generated at 2022-06-22 12:03:28.613114
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:03:36.705891
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == u'ab'
    assert ansible_native_concat(['a', ['b', 'c']]) == u'a[u\'b\', u\'c\']'
    assert ansible_native_concat([[['a', 'b'], 'c']]) == u'[u\'ab\', u\'c\']'
    assert ansible_native_concat([[['a', ['b']], 'c']]) == u'[u\'a[u\\\'b\\\']\', u\'c\']'
    assert ansible

# Generated at 2022-06-22 12:03:48.291309
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def check(output, *inputs):
        assert output == ansible_native_concat(inputs)
        assert output == ansible_native_concat([inputs[0], inputs[1]])

    check(u'\u00a7', u'\u00a7')
    check(u'\ufeff', u'\ufeff')
    check(u'\U0001f43e', u'\U0001f43e')
    check(u'\U00010000', u'\U00010000')
    check(u'\U0010ffff', u'\U0010ffff')
    check(u'\u00a7', u'\u00a7', u'\u00A7')

# Generated at 2022-06-22 12:04:00.169447
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml = '''
    - 1
    - 2
    - 3
    '''

    loader = AnsibleLoader(yaml, None)
    code = loader.get_single_data()
    jinja_nodes = code.children[0][1]
    assert [1, 2, 3] == ansible_native_concat(jinja_nodes)

    yaml = '3'
    loader = AnsibleLoader(yaml, None)
    code = loader.get_single_data()
    jinja_nodes = code.children[0][1]
    assert 3 == ansible_native_concat(jinja_nodes)

    yaml = '3 | string'

# Generated at 2022-06-22 12:04:10.448497
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, 2, 3, 4]) == u'1234'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([1, u'foo', True]) == u'1fooTrue'
    assert ansible_native_concat([1, u'foo', True]) == u'1fooTrue'
    assert ansible_native_concat([u'one', u'two']) == u'one' + u'two'
    assert ansible_native_concat([u'one', u' ', u'two']) == u'one two'

# Generated at 2022-06-22 12:04:22.635596
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["a", "b", "c"]) == "abc"
    assert ansible_native_concat(["1", "2", "3"]) == "123"
    assert ansible_native_concat(["1", ["2", "3"]]) == "1[u'2', u'3']"
    assert ansible_native_concat(["1", {"foo": "bar"}]) == "1{u'foo': u'bar'}"
    assert ansible_native_concat(["a", 1, "b", 2.1, "c", {"foo": "bar"}]) == "a1b2.1c{u'foo': u'bar'}"
    assert ansible_native_concat([1, 2, 3]) == 123

# Generated at 2022-06-22 12:04:31.905129
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test ansible_native_concat function."""

# Generated at 2022-06-22 12:04:43.587966
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import container_to_text
    from ansible.module_utils.common.text.formatters import to_nice_str
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils.six import string_types
    from types import GeneratorType
    import ast
    import types

    def check_ansible_native_concat(expected, *inputs):
        nodes = list(inputs)
        ansible_native_concat_result = ansible_native_concat(nodes)

# Generated at 2022-06-22 12:04:56.775023
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test the given node of different types
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat(['0']) == 0
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat(['True']) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat(['False']) is False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['None']) is None
    assert ansible_native_concat([u'']) == u''
    assert ansible_native_concat([u'1']) == 1
    # Test the given nodes of different types

# Generated at 2022-06-22 12:05:08.224073
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # These tests do not cover all possible data types. They are meant to
    # cover the most important use cases.
    # https://github.com/ansible/ansible/issues/70831#issuecomment-664924351
    # https://github.com/ansible/ansible/issues/70831#issuecomment-664944575

    # Values should be returned as-is when possible.
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([1.2]) == 1.2
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat(['    True']) is True
    assert ansible_native_

# Generated at 2022-06-22 12:05:21.572638
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml import loader

    source_1 = 'foo'
    source_2 = 'baz'
    source_3 = 'qux'
    source_4 = 'spam'
    source_5 = 'ham'
    source_6 = 'foo'
    source_7 = loader.LoadedYAMLObject('{eggs: bacon}')


# Generated at 2022-06-22 12:05:33.690382
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat(["a", "b", "c"]) == "abc"
    assert ansible_native_concat(["a", 1, "c"]) == "a1c"
    assert ansible_native_concat([1, [2, 3], 4]) == [1, [2, 3], 4]
    assert ansible_native_concat([1, {"a": "A"}, "c"]) == [1, {"a": "A"}, "c"]
    assert ansible_native_concat([1, 2]) == [1, 2]
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(["a", 2]) == "a2"

# Generated at 2022-06-22 12:05:44.386257
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert container_to_text(ansible_native_concat([1, 2, 3])) == '123'
    assert container_to_text(ansible_native_concat([1, 2, u'3'])) == '123'
    assert container_to_text(ansible_native_concat([1, u'2', u'3'])) == '123'
    assert container_to_text(ansible_native_concat([True, u'2', u'3'])) == 'True23'
    assert container_to_text(ansible_native_concat([u'2', u'3'])) == '23'
    assert container_to_text(ansible_native_concat([u'2'])) == '2'
    assert container_to_text(ansible_native_concat([])) is None

# Generated at 2022-06-22 12:05:55.476382
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a', 'b', 'c']) == 'a'
    assert ansible_native_concat(['a', 1, 'c']) == 'a1c'
    assert ansible_native_concat(['a', AnsibleVaultEncryptedUnicode('abc')]) == 'abc'
    assert ansible_native_concat(["a", NativeJinjaText('a'), NativeJinjaText('b'), 'c']) == 'ab'
    assert ansible_native_con

# Generated at 2022-06-22 12:06:03.390999
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.parsing.yaml.data import AnsibleVaultEncryptedUnicode
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat([1, 2, '3']) == '123'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', '2', '3']) == 1
    assert ansible_native_concat([' 1', 2, '3']) == '123'
    assert ans

# Generated at 2022-06-22 12:06:12.513094
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with a concatenation with an integer and a string
    result = ansible_native_concat([1, 'user'])
    assert result == '1user'

    # Test with a concatenation with an integer and a boolean
    result = ansible_native_concat([1, True])
    assert result == '1True'

    # Test with a single string
    result = ansible_native_concat(['user'])
    assert result == 'user'

    # Test with a sequence of nodes
    result = ansible_native_concat([1, '.', 'user'])
    assert result == '1.user'

    # Test with a multiline string
    result = ansible_native_concat(['Hello World\n'])
    assert result == 'Hello World\n'

    # Test with a

# Generated at 2022-06-22 12:06:22.787954
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Setup
    node_list = [NativeJinjaText(str(x)) for x in range(10)]
    node_list[0].is_safe_variable = True
    node_list[3].is_safe_variable = True
    node_list[5].is_safe_variable = True
    node_list[9].is_safe_variable = True

    # Expected Results
    results_list = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        0,
        "0123456789",
        "0123456789",
        "0\n3\n5\n9"
    ]

    # Actual Results
    results = []
    results.append(ansible_native_concat(node_list))

# Generated at 2022-06-22 12:06:34.692640
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    assert ansible_native_concat([]) is None

    # native_concat concatenates multiple strings into a single
    # string.
    assert ansible_native_concat([u'file', u'a']) == u'filea'
    assert ansible_native_concat([u'file', u'', u'a']) == u'filea'
    assert ansible_native_concat([u'file', u'a', u'', u'b']) == u'fileab'

    # native_concat returns a single node as-is.
    assert ansible_native_concat([u'file']) == u'file'

# Generated at 2022-06-22 12:06:52.465668
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check if a single value is returned back
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([2.0]) == 2.0
    assert ansible_native_concat([container_to_text(['a', 'b'])]) == container_to_text(['a', 'b'])
    assert ansible_native_concat([container_to_text({'a': 'b', 'c': 'd'})]) == container_to_text({'a': 'b', 'c': 'd'})

    # Check if concatenation of multiple values works
    assert ansible_native_concat([1, 2, 3]) == 123

# Generated at 2022-06-22 12:07:04.397704
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Pass array to ansible_native_concat, as it will be expected to fail
    assert ansible_native_concat(['7', 1]) == '7'
    # Pass object to ansible_native_concat, as it will be expected to fail
    assert ansible_native_concat({'7': 1}) == '7'
    # Pass object to ansible_native_concat, as it will be expected to fail
    assert ansible_native_concat([7, 1]) == 7
    # Pass object to ansible_native_concat, as it will be expected to fail
    assert ansible_native_concat([7, 1]) == 7
    # Pass object to ansible_native_concat, as it will be expected to fail
    assert ansible_native_concat([7, 1]) == 7
    # Pass

# Generated at 2022-06-22 12:07:14.631967
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native, to_text

    # The following input values are used in the tests:
    # value            - input value (could be scalar or list of values)
    # expected_output  - expected output value, e.g. after using string filter
    # expected_type    - expected output type
    # expected_error   - if given, what error msg should be detected, if any


# Generated at 2022-06-22 12:07:23.802801
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["hello"]) == "hello"
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(["hello", "world"]) == "helloworld"
    assert ansible_native_concat(["hello", " ", "world"]) == "hello world"
    assert ansible_native_concat([None, " ", "world"]) == " world"
    assert ansible_native_concat(["hello", " ", None]) == "hello "
    assert ansible_native_concat([None, None, None]) is None
    assert ansible_native_concat([None, " ", None]) is None
    assert ansible_native_concat(["", " ", ""]) == " "

# Generated at 2022-06-22 12:07:29.310487
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # https://github.com/pallets/jinja/issues/1200
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat(['{{ a }}', '2']) == '{{ a }}2'
    assert ansible_native_concat(['1', '2']) == 1



# Generated at 2022-06-22 12:07:41.061526
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    var_one = {"list1":['A', 'B', 'C']}
    var_two = {"list2":['D', 'E', 'F']}
    var_three = {"list3":['G', 'H', 'I']}
    var_four = {"list4":['J', 'K', 'L']}
    list_of_lists = [var_one, var_two, var_three, var_four]
    expected = "['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']"
    var_str = AnsibleDumper().represent_list(list_of_lists)

# Generated at 2022-06-22 12:07:51.680923
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """
    Test cases to validate the ansible_native_concat method
    :return:
    """
    # Test cases with NULL value
    null_value = [None, '']
    for item in null_value:
        actual = ansible_native_concat(item)
        assert actual == None

    # Test cases with single node
    single_node = [1, True, 'a']
    expected = [1, True, 'a']
    for index in range(len(single_node)):
        actual = ansible_native_concat(single_node[index])
        assert actual == expected[index]

    # Test cases with single node string and boolean
    single_node_string = ['a', True]
    expected = ['a', True]

# Generated at 2022-06-22 12:07:59.067667
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.runtime import Undefined
    assert ansible_native_concat([Undefined()]) is None
    assert ansible_native_concat(['abc']) == 'abc'
    assert ansible_native_concat([1, 'b', 2]) == '1b2'
    assert ansible_native_concat([1, 'b', 2]) == '1b2'

# Generated at 2022-06-22 12:08:11.236981
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat(['a', 'b', 'c']) == 'a'
    assert ansible_native_concat([1, 'b', 'c']) == 1
    assert ansible_native_concat([1, 2, 3]) == '1'
    assert ansible_native_concat(['[1, 2, 3]']) == [1, 2, 3]
    assert ansible_native_concat(['[1, 2, 3]']) == '1'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 1]) == 'a'

# Generated at 2022-06-22 12:08:22.584999
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible_collections.ansible.community.tests.unit.module_utils.compat import unittest

    class TestNativeConcat(unittest.TestCase):
        def test_list(self):
            self.assertEqual(
                ansible_native_concat([u'foo', u'bar']),
                u'foobar'
            )

        def test_dict(self):
            self.assertEqual(
                ansible_native_concat({u'foo': u'bar'}),
                {u'foo': u'bar'}
            )

        def test_string(self):
            self.assertEqual(
                ansible_native_concat(u'foo'),
                u'foo'
            )


# Generated at 2022-06-22 12:08:38.467174
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '1, 2'
    assert ansible_native_concat([1, None, 2]) == '1, None, 2'
    assert ansible_native_concat(['1', 2]) == '12'
    assert ansible_native_concat(['1', None, 2]) == '1None2'
    assert ansible_native_concat([b'foo', b'bar']) == 'foobar'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat(['foo', u'bar']) == u'foobar'

# Generated at 2022-06-22 12:08:45.755061
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native


# Generated at 2022-06-22 12:08:57.399773
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([[1, 2]]) == [1, 2]
    assert ansible_native_concat([(1, 2)]) == (1, 2)
    assert ansible_native_concat([{'a': 1}]) == {'a': 1}
    assert ansible_native_concat(["1", "2"]) == "12"
    assert ansible_native_concat([1, "2"]) == "12"
    assert ansible_native_concat

# Generated at 2022-06-22 12:09:09.026337
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six.moves import builtins
    from ansible.template import Templar

    def _compile_node(t, data):
        templar = Templar(t.loader, t, t._shared_loader_obj)
        return templar.template(data, fail_on_undefined=True)


# Generated at 2022-06-22 12:09:18.493522
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat("foo") == "foo"
    assert ansible_native_concat("foo") != "bar"
    assert ansible_native_concat(["foo", "bar"]) == "foobar"
    assert ansible_native_concat(["foo", "bar"]) != "barfoo"
    assert ansible_native_concat(["foo", "bar"]) != "foo"
    assert ansible_native_concat(["foo", u"bar"]) == "foobar"
    assert ansible_native_concat(["foo", u"bar"]) != u"foobar"



# Generated at 2022-06-22 12:09:59.022385
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:04.102864
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    data = {
        'undefined_1': StrictUndefined(),
        'undefined_2': StrictUndefined(),
    }

    assert ansible_native_concat(['a', data, 'b', 'c']) == [
        'a',
        data,
        'b',
        'c'
    ]

    assert ansible_native_concat(container_to_text([
        'a',
        data,
        'b',
        'c'
    ])) == [
        'a',
        data,
        'b',
        'c'
    ]


# Generated at 2022-06-22 12:10:14.068638
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['1', 2, 3]) == '123'
    assert ansible_native_concat(['1', 'foo', '3']) == '1foo3'
    assert ansible_native_concat(['1', 2, 'foo']) == '1foo'
    assert ansible_native_concat([2]) == 2
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['"foo"']) == '"foo"'



# Generated at 2022-06-22 12:10:25.607811
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common._collections_compat import from_v2_list

    assert ansible_native_concat(from_v2_list(['1', '2', '3'])) == '123'
    assert ansible_native_concat(from_v2_list(['a', 'b', 'c'])) == 'abc'
    assert ansible_native_concat(from_v2_list(['1', '2', 3])) == '123'
    assert ansible_native_concat(from_v2_list(['one', 'two', 'three'])) == 'onetwothree'
    assert ansible_native_concat(from_v2_list(['-4', '5', '6'])) == '-456'

# Generated at 2022-06-22 12:10:35.717095
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    # This is a simple repr for AnsibleBaseYAMLObject, not completely
    # accurate but enough for unit tests
    BaseYAMLObject = lambda data: AnsibleBaseYAMLObject(data)

    # The code below is a copy-paste from the original Jinja test suite with
    # some modifications to make it work with ansible_native_concat.

# Generated at 2022-06-22 12:10:49.788648
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foobar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'
    assert ansible_native_concat(['foo', 'bar', 'baz', 'foobarbaz']) == 'foobarbazfoobarbaz'
    assert ansible_native_concat(['foo', 'bar', 'baz', 'foobarbaz', 'newline', '\n']) == 'foobarbazfoobarbaznewline\n'

# Generated at 2022-06-22 12:11:00.082826
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Note that a number of test cases are present in ``test_min Jinja tests``.
    result = ansible_native_concat([3])
    assert 3 == result

    result = ansible_native_concat([False])
    assert False == result

    result = ansible_native_concat(['foo', 3, True])
    assert 'foo3True' == result

    # literal_eval should be able to change some strings to bools, ints, etc.
    result = ansible_native_concat(['True', False])
    assert True == result

    result = ansible_native_concat(['1', False])
    assert 1 == result

    result = ansible_native_concat(['0', False])
    assert 0 == result

    result = ansible_native_concat(['False', False])


# Generated at 2022-06-22 12:11:07.588151
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # handles various concat cases
    assert ansible_native_concat(["", ""]) == ""
    assert ansible_native_concat([u"", u""]) == u""
    assert ansible_native_concat(["1", ""]) == "1"
    assert ansible_native_concat(["1", "1"]) == "11"
    assert ansible_native_concat([u"", u"1"]) == u"1"
    assert ansible_native_concat([u"1", u""]) == u"1"
    assert ansible_native_concat([u"1", u"1"]) == u"11"
    assert ansible_native_concat([u"", 1]) == u"1"