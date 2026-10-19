

# Generated at 2022-06-22 12:01:15.546995
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = [
        'foo',
        'bar'
    ]
    assert ansible_native_concat(nodes) == 'foobar'

    nodes = [
        'foo',
        'bar',
        1,
        2,
        3
    ]
    assert ansible_native_concat(nodes) == 'foobar123'

    nodes = [
        1,
        2,
        3,
        'foo',
        'bar'
    ]
    assert ansible_native_concat(nodes) == 'foobar'

    nodes = [
        1,
        2,
        3,
        'foo',
        'bar'
    ]
    assert ansible_native_concat(nodes) == 'foobar'


# Generated at 2022-06-22 12:01:28.034664
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    literal_eval_data = [
        "True",
        "1234",
        "'foo'",
        "['foo', 'bar']",
        "('foo', 'bar')",
        "('foo', 'bar', 'baz')",
        "{'baz': 'qux'}",
        "('a', True, 1234, ['foo', 'bar'], {'baz': 'qux'})",
    ]
    for data in literal_eval_data:
        assert ansible_native_concat([container_to_text(data)]), ast.literal_eval(data)

    # Empty string
    assert ansible_native_concat([]) is None

    # Single element sequence
    assert ansible_native_concat(["True"]) is True

    # Multiple element sequence
    assert ansible_native

# Generated at 2022-06-22 12:01:39.405683
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', 42, u'bar']) == u'foo42bar'
    assert ansible_native_concat([u'', u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'', u'', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'', u'', u'', u'bar']) == u'foobar'
    assert ans

# Generated at 2022-06-22 12:01:51.955552
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test :func:`ansible_native_concat`"""
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([3]) == 3
    assert ansible_native_concat([3, 4]) == '34'
    assert ansible_native_concat([3, 4, 5]) == '345'
    assert ansible_native_concat(u'foo') == u'foo'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', u'baz']) == u'foobarbaz'

# Generated at 2022-06-22 12:02:03.928503
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    def Literal(value):
        return to_text(value)

    assert ansible_native_concat([42]) == Literal(42)
    assert ansible_native_concat([2, 3, 5, 7, 11, 13, 17]) == Literal(2)
    assert ansible_native_concat([Literal(3.14)]) == Literal(3.14)
    assert ansible_native_concat([True]) == Literal(True)
    assert ansible_native_concat([Literal(False)]) == Literal(False)
    assert ansible_native_concat([Literal(True), Literal(False)]) == Literal(True)
    assert ansible_native_concat([Literal('hello')]) == Literal('hello')
    assert ansible_native_con

# Generated at 2022-06-22 12:02:09.216619
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat([10]) == 10
    assert ansible_native_concat([10.0]) == 10.0
    assert ansible_native_concat(['abc']) == 'abc'
    assert ansible_native_concat([u'abc']) == u'abc'

    assert ansible_native_concat([u'abc', u'def']) == u'abcdef'
    assert ansible_native_concat(['abc', 'def']) == 'abcdef'
    assert ansible_native_concat([u'abc', 'def']) == u'abcdef'
    assert ansible_native_concat(['abc', u'def']) == u'abcdef'


# Generated at 2022-06-22 12:02:17.919264
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.six import string_types

    assert isinstance(ansible_native_concat(["one"]), string_types)
    assert isinstance(ansible_native_concat(["one", "two"]), string_types)
    assert isinstance(ansible_native_concat(["1", "2"]), int)
    assert isinstance(ansible_native_concat(["1", "2", "3"]), int)
    assert isinstance(ansible_native_concat(["1.0", "2.0"]), float)
    assert isinstance(ansible_native_concat(["1.0", "2.0", "3.0"]), float)

# Generated at 2022-06-22 12:02:21.616807
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["foo", "bar"]) == u"foobar"
    assert ansible_native_concat(["foo", {"bar": "baz"}, "quux"]) == u"foobazquux"



# Generated at 2022-06-22 12:02:33.401402
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat([1, 2]) == '12'

    # ast.literal_eval accepts numeric literals
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['0b01']) == 1
    assert ansible_native_concat(['0o1']) == 1
    assert ansible_native_concat(['0x1']) == 1
    assert isinstance(ansible_native_concat(['1']), int)

# Generated at 2022-06-22 12:02:45.050096
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(('1', '2')) == 12
    assert ansible_native_concat(('1', '2', '3')) == 123
    assert isinstance(ansible_native_concat(('1', '2', '3')), int)
    assert ansible_native_concat(('1', 'a')) == '1a'
    assert isinstance(ansible_native_concat(('1', 'a')), text_type)
    assert ansible_native_concat((['a'], 'b')) == ['a', 'b']
    assert isinstance(ansible_native_concat((['a'], 'b')), list)
    assert ansible_native_concat((['a'], ['b'])) == ['a', 'b']

# Generated at 2022-06-22 12:03:01.086126
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', ' bar']) == 'foo bar'
    assert ansible_native_concat(['foo ', ' bar']) == 'foo bar'
    assert ansible_native_concat([' foo ', ' bar']) == ' foo bar'
    assert ansible_native_concat([' foo ', ' bar ']) == ' foo bar '
    assert ansible_native_concat([' foo', 'bar ']) == ' foobar '
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'

# Generated at 2022-06-22 12:03:09.946886
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _test_res(value, expected):
        res = ansible_native_concat(value)
        assert res == expected, 'ansible_native_concat(%s) -> %s' % (value, res)

    # First test unicode with non-ascii characters
    _test_res([u'\u043f\u0440\u0438\u0432\u0435\u0442'], u'\u043f\u0440\u0438\u0432\u0435\u0442')

    # Test that unicode is not interpreted as a string

# Generated at 2022-06-22 12:03:20.816825
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test inputs with valid result
    assert ansible_native_concat(iter([1, 2, 3])) == 123
    assert ansible_native_concat(iter([1, ' ', 2, ' ', 3])) == 123
    assert ansible_native_concat(iter(['a', 'b', False, '', 'c'])) == 'abc'
    assert ansible_native_concat(iter(['[', 1, ',', 2, ']'])) == [1, 2]
    assert ansible_native_concat(iter(['{', 1, ':', 2, '}'])) == {1: 2}

    # Test inputs with exception ValueError
    assert ansible_native_concat(iter(['a', 'b', 'c'])) == 'abc'

# Generated at 2022-06-22 12:03:31.848331
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([u'one']) == u'one'
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, u'2', 3]) == [1, '2', 3]
    assert ansible_native_concat([[1], [2], [3]]) == [[1], [2], [3]]
    assert ansible_native_concat([[1], u'2', [3]]) == [[1], '2', [3]]
    assert ansible_native_concat([u'one', u'two', u'three']) == u'onetwothree'


# Generated at 2022-06-22 12:03:41.973111
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == "12"
    assert ansible_native_concat([1, 2, 3]) == "123"
    assert ansible_native_concat([1, 2, 3, 4]) == "1234"
    assert ansible_native_concat([1, 2, 3, 4, 5]) == "12345"
    assert ansible_native_concat([1, 2, 3, 4, 5, 6]) == "123456"
    assert ansible_native_concat([1, 2, 3, 4, 5, 6, 7]) == "1234567"
    assert ansible_native_concat([1, 2, 3, 4, 5, 6, 7, 8]) == "12345678"

# Generated at 2022-06-22 12:03:51.179242
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(islice(['1', 2], 2)) == '12'
    assert ansible_native_concat(islice([1, '2'], 2)) == '12'
    assert ansible_native_concat(islice(['1', '2'], 2)) == '12'

    assert ansible_native_concat(islice(['1', u'2'], 2)) == u'12'
    assert ansible_native_concat(islice([u'1', '2'], 2)) == u'12'
    assert ansible_native_concat(islice([u'1', u'2'], 2)) == u'12'

    assert ansible_native_concat(islice(['1', '2'], 1)) == '1'
    assert ansible_native

# Generated at 2022-06-22 12:04:00.253355
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Python 3.9+ started changing the literal_eval values
    # between 3.9.0 and 3.9.0rc2. So we need to adjust the
    # test depending on the Python version.
    import sys
    python_version = sys.version_info
    min_literal_eval_version = (3, 9)
    is_literal_eval_version = python_version >= min_literal_eval_version

    if is_literal_eval_version:
        float_value = float('Inf')
        float_str = 'Inf'
    else:
        float_value = 1e400
        float_str = '1e+400'


# Generated at 2022-06-22 12:04:10.523174
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'"a"']) == u'a'
    assert ansible_native_concat([u'"a"', u'"b"']) == u'ab'
    assert ansible_native_concat([u'12', u'34']) == 1234
    assert ansible_native_concat([u'"a"', u'12', u'34']) == u'a1234'
    assert ansible_native_concat([u'[', u'1', u',' u'2', u']']) == [1, 2]

# Generated at 2022-06-22 12:04:19.528840
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == 3
    assert ansible_native_concat(['1', '2', '3']) == 6
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat([text_type('foo'), text_type('bar')]) == 'foobar'
    assert ansible_native_concat(['1', '2', '*', '4', '5']) == '1*2*4*5'
    assert ansible_native_concat(['1', ',']) == '1,'


# Generated at 2022-06-22 12:04:30.106319
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_equal(nodes, expected_result):
        assert ansible_native_concat(nodes) == expected_result

    assert_equal([U('uni')], 'uni')
    assert_equal([[U('ansible'), U('is')], U('awesome')], ['ansible', 'is', 'awesome'])
    assert_equal([[U('ansible'), U('is')], U('awesome')], ['ansible', 'is', 'awesome'])
    assert_equal([U('foofoo'), U('barbar')], 'foofoobarbar')
    assert_equal([[], [[U('foofoo'), U('barbar')]], U('bazbaz')], ['bazbaz'])

# Generated at 2022-06-22 12:04:45.236806
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import unittest
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        add_file_common_args=True
    )

    class Test(unittest.TestCase):
        def test_one(self):
            self.assertEqual(ansible_native_concat((1,)), 1)

        def test_one_two(self):
            self.assertEqual(ansible_native_concat((1, 2)), u'12')

        def test_one_two_three(self):
            self.assertEqual(ansible_native_concat((1, 2, 3)), u'123')


# Generated at 2022-06-22 12:04:56.119502
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import builtins

    if isinstance(u'', builtins.str):
        string_types = builtins.str

    assert ansible_native_concat([]) is None

    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'foo', 1, 2, 3, 4, None]) == u'foo1234None'

    assert ansible_native_con

# Generated at 2022-06-22 12:05:07.921536
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', AnsibleVaultEncryptedUnicode(b'\x00')]) == u'foobar'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1, 2, 3, AnsibleVaultEncryptedUnicode(b'\x00')]) == u'123'
    assert ansible_native_concat([1, 2, 3, 4]) == u

# Generated at 2022-06-22 12:05:21.177177
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert isinstance(ansible_native_concat(['foo']), text_type)
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert isinstance(ansible_native_concat(['foo', 'bar']), text_type)

    assert ansible_native_concat(['foo', True, 123, 15.7, 'bar']) == 'fooTrue12315.7bar'
    assert isinstance(ansible_native_concat(['foo', True, 123, 15.7, 'bar']), text_type)

    s = 'foo'
    assert ansible_native_concat([s]) is s

    assert ansible_

# Generated at 2022-06-22 12:05:25.397652
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    cases = [
        (['a', 'b'], 'ab'),
        (['a', True], 'atrue'),
        (['a', u'b'], u'ab'),
        ([u'a', b'b'], u'ab'),
        (['{{a}}', 'b'], u'{{a}}b'),
        ([True, 'b'], u'trueb'),
        (['a', u'a', u'b'], u'aab'),
        (['1', '2', '3'], '123'),
        (['1', 2, '3'], '123'),
    ]

    for input, expected in cases:
        actual = container_to_text(ansible_native_concat(input))
        assert expected == actual

# Generated at 2022-06-22 12:05:35.011118
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, '2', 3]) == [1, 2, 3]
    assert ansible_native_concat(['1', '2', 3]) == '123'
    assert ansible_native_concat(['1', u'\ufffd', 3]) == u'1\ufffd3'
    assert ansible_native_concat(['1', u'\ufffd', 3]) == container_to_text([u'1\ufffd3'])
    assert isinstance(ansible_native_concat(['1', u'\ufffd', 3]), text_type)

# Generated at 2022-06-22 12:05:43.923943
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1

    nodes = (1, 2, 3)
    assert ansible_native_concat(nodes) == '123'

    nodes = (1, 2, 3)
    assert ansible_native_concat(nodes) == '123'

    nodes = (1, 2, 3, u'foo')
    assert ansible_native_concat(nodes) == '123foo'

    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'

    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'

    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'


# Generated at 2022-06-22 12:05:54.769519
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo\n', u'bar']) == u'foo\nbar'
    assert ansible_native_concat([u'\n', u'bar']) == u'\nbar'
    assert ansible_native_concat([u'foo\n', u'bar\n']) == u'foo\nbar\n'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', '{{ var }}']) == u'foobar{{ var }}'
    assert ansible_

# Generated at 2022-06-22 12:06:02.709197
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    data = {
        'values': [
            {
                'input': [literal_eval('123')],
                'output': 123,
            },
            {
                'input': [literal_eval('"123"')],
                'output': '123',
            },
            {
                'input': [None],
                'output': None,
            },
            {
                'input': [literal_eval('"abc"'), literal_eval('"cde"')],
                'output': 'abccde',
            },
        ],
    }

    for value in data['values']:
        assert value['output'] == ansible_native_concat(value['input'])



# Generated at 2022-06-22 12:06:12.024899
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Very basic unit test of the ``ansible_native_concat`` function."""
    import ast
    import random
    import string

    def _gen_random_string(length):
        """Return a random string with length ``length``."""
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    def _random_tests(tests, count):
        """Return a list of ``count`` random test cases.

        Every test case is a list of randomly chosen strings and values,
        e.g.:

            ['a', 'b', 1, 3.2, 'c', 42]

        which will be concatenated and parsed with ``ast.literal_eval``.
        """

# Generated at 2022-06-22 12:06:25.296573
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['', 'foobar']) == u'foobar'
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'1', u'2']) == 3
    assert ansible_native_concat([u'1', u'2', u'3']) == u'123'
    assert ansible_native_concat([u'1b', u'2', u'3']) == u'1b23'
    assert ansible_native_concat([u'1', u'2b', u'3']) == u'123'

# Generated at 2022-06-22 12:06:37.523751
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    base_list = [u'foo', u'bar']
    assert ansible_native_concat(base_list) == u'foobar'

    with_native_jinja_text = [u'foo', NativeJinjaText(u'bar')]
    assert ansible_native_concat(with_native_jinja_text) == u'foobar'

    with_jinja_undefined = [u'foo', StrictUndefined()]
    assert ansible_native_concat(with_jinja_undefined) == u'foo'

    with_vault = [AnsibleVaultEncryptedUnicode(u'foo'), u'bar']
    assert ansible_native_concat(with_vault).data == u'foobar'


ansible_concat_native = ansible_native_con

# Generated at 2022-06-22 12:06:47.789861
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["abc", None]) == "abcNone"
    assert ansible_native_concat([None, "abc"]) == "Noneabc"
    assert ansible_native_concat(["abc", "def"]) == "abcdef"
    assert ansible_native_concat(["abc", {"k": "v"}, "def"]) == "abc{'k': 'v'}def"
    assert ansible_native_concat(["abc", ["def", "ghi"], "jkl"]) == "abc['def', 'ghi']jkl"
    assert ansible_native_concat(["abc", 42, "def"]) == "abc42def"
    assert ansible_native_concat([]) is None


# Generated at 2022-06-22 12:06:54.494455
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    node_success = lambda x: {'value': x, 'type': 'success', 'lineno': 1, 'col_offset': 1}
    node_undefined = {'lineno': 1, 'col_offset': 1, 'type': 'undefined'}

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([node_success(1)]) == 1
    assert ansible_native_concat([node_success("1")]) == 1
    assert ansible_native_concat([node_success("1"), node_success("2")]) == "12"
    assert ansible_native_concat([node_success("1"), node_success("2"), node_success("3")]) == "123"

# Generated at 2022-06-22 12:07:06.288507
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['test']) == 'test'
    assert ansible_native_concat(['test', 'test']) == 'testtest'
    assert ansible_native_concat([None, 'test']) == 'test'
    assert ansible_native_concat(['test', None]) == 'test'
    assert ansible_native_concat([1, 'test', 2]) == '1test2'
    assert ansible_native_concat([1, None, 2]) == '12'
    assert ansible_native_concat(['test', '1', '2', '3']) == 'test123'
    assert ansible_native_concat([True, False, None]) is False

# Generated at 2022-06-22 12:07:15.414762
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_equivalent(value, expected_value, expected_text_value):
        assert value == expected_value
        assert container_to_text(value) == text_type(expected_text_value)
        assert text_type(value) == text_type(expected_text_value)

    assert_equivalent(ansible_native_concat([]), None, '')
    assert_equivalent(ansible_native_concat([1]), 1, '1')

    assert_equivalent(ansible_native_concat((1, 2)), '12', '12')
    assert_equivalent(ansible_native_concat([1, 2]), '12', '12')
    assert_equivalent(ansible_native_concat((1, 2, 3)), '123', '123')

# Generated at 2022-06-22 12:07:27.028148
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # This test is copied directly from upstream Jinja2 3.2.
    # TODO update the tests when we update Jinja2
    import jinja2
    env = jinja2.Environment()
    env.finalize = ansible_native_concat

    assert env.from_string('{{ "foo" + "bar" }}').render() == 'foobar'
    assert env.from_string('{{ "foo" + ["x", "y", "z"]|join }}').render() == 'fooxyz'
    assert env.from_string('{{ [1, 2] + [3, 4] }}').render() == [1, 2, 3, 4]

    assert env.from_string('{{ ["x", "y", "z"]|join }}').render() == 'xyz'

# Generated at 2022-06-22 12:07:39.173165
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # TODO move to unit tests

    # pylint: disable=unused-argument
    def literal(nodes):
        return ansible_native_concat(nodes)

    def literal_string(nodes):
        v = literal(nodes)
        return 'literal string: %s' % container_to_text(v)

    def literal_int(nodes):
        v = literal(nodes)
        return v if isinstance(v, int) else 'not an int'

    def literal_long(nodes):
        v = literal(nodes)
        # int is a subclass of long in Python 2
        return v if isinstance(v, int) else 'not an long'

    def literal_float(nodes):
        v = literal(nodes)

# Generated at 2022-06-22 12:07:50.116319
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['[1, 2]']) == [1, 2]
    assert ansible_native_concat(['{"k": "v"}']) == {"k": "v"}

    assert ansible_native_concat([False, 'bar']) == 'Falsebar'
    assert ansible_native_concat([
        '',
        True,
        '',
        [],
        '',
        (),
        '',
        {},
        '',
        'foo'
    ]) == 'True[](){"foo"}'

# Generated at 2022-06-22 12:08:02.557898
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == u'a'
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1, 2, 'a', 3]) == u'12a3'
    assert ansible_native_concat(['a', 2, 3]) == u'a23'
    assert ansible_native_concat(['a', 2, 3]) == u'a23'
    assert ansible_native_concat([-1, -2]) == u'-1-2'
    assert ansible_native_concat(['a', 2, 3]) == u'a23'


# Generated at 2022-06-22 12:08:14.940804
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with invalid arguments
    assert ansible_native_concat(None) is None

    # Test with valid arguments
    assert ansible_native_concat(["a", "b", "c"]) == "abc"
    assert ansible_native_concat(["a", "b", "c", 1]) == "abc"
    assert ansible_native_concat(["a", "b", "c", 1, 3.14, []]) == "abc"

    # Test with valid arguments that can be parsed by ast.literal_eval
    assert ansible_native_concat(["1", "2", "3"]) == 123
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(["1.23", "4.56", "7.89"])

# Generated at 2022-06-22 12:08:26.650702
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 'b']) == '1b'
    assert ansible_native_concat([1, [2, 3]]) == [1, [2, 3]]
    assert ansible_native_concat([1, [2, 3]], ['b']) == [1, [2, 3]]
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', 'c']) == u'abc'
    assert ansible_native_concat([u'a', u'b', [u'c', u'd']]) == [u'a', u'b', [u'c', u'd']]

# Generated at 2022-06-22 12:08:38.737651
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, 2, 3, 4]) == u'1234'
    assert ansible_native_concat([1, 2, 3, 4, 5, 6]) == u'123456'
    assert ansible_native_concat([u'abc\tabc']) == u'abc\tabc'
    assert ansible_native_concat([u'abc\tdef']) == u'abc\tdef'
    assert ansible_native_concat([u'abc\ndef']) == u'abc\ndef'
    assert ansible_native_concat([u'abc\rabc']) == u'abc\rabc'

# Generated at 2022-06-22 12:08:48.626343
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Undef(StrictUndefined):
        def __add__(self, other):
            return 42

    assert ansible_native_concat([Undef() + Undef()]) == 42
    assert ansible_native_concat([u'foo', Undef()]) == u'foo'
    assert ansible_native_concat([u'foo', Undef(), 42]) == u'foo42'
    assert ansible_native_concat([u'foo', Undef(), {1: Undef()}]) == u"foo{1: Undefined}"

    class Str(NativeJinjaText):
        def __add__(self, other):
            return 42

    assert ansible_native_concat([Str(u'foo'), Str(u'bar')]) == 42

# Generated at 2022-06-22 12:08:59.245132
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([{'foo': 'bar'}]) == {'foo': 'bar'}
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 42]) == 'foo42'
    assert ansible_native_concat(['foo', 'true']) == 'footrue'
    assert ansible_native_concat(['foo', True]) == 'footrue'

# Generated at 2022-06-22 12:09:10.610203
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', 'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', '\u2299bar']) == u'foo\u2299bar'
    assert ansible_native_concat([123, 'bar']) == u'123bar'
    assert ansible_native_concat([123, u'bar']) == u'123bar'
    assert ansible_native_concat([123, u'bar', None]) == u'123barNone'
    assert ansible_native_concat([None, '123', u'bar']) == u'None123bar'

# Generated at 2022-06-22 12:09:21.661786
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _test(test_str, expected):
        class Test(object):
            def __str__(self):
                return "test"

            def __repr__(self):
                return "test"

        class DummyVaulted(object):
            def __init__(self, data):
                self.data = data

            def __str__(self):
                return "vaulted"

            def __repr__(self):
                return "vaulted"

        assert ansible_native_concat(test_str) == expected

        # test with a vault
        test_vaulted = DummyVaulted(test_str)
        assert ansible_native_concat([test_vaulted]) == container_to_text(expected)

        # test with a non-string
        test_obj = Test()


# Generated at 2022-06-22 12:09:58.874008
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:10.717588
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    native_string = NativeJinjaText('foo')
    vault = AnsibleVaultEncryptedUnicode('foo', b'bar')
    empty = ''
    test_list = [True, False, None, 1, 1.0, 'foo', u'foo', native_string, vault, empty]
    for item in test_list:
        result = ansible_native_concat([item])
        assert item == result, "Expected '%s', got '%s' (%s)" % (item, result, type(result))
        result = ansible_native_concat([item, item])
        assert container_to_text(item + item) == container_to_text(result), \
            "Expected '%s', got '%s' (%s)" % (item + item, result, type(result))

# Generated at 2022-06-22 12:10:21.535359
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Function call given a single argument
    assert ansible_native_concat(['str']) == u'str'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([False]) == False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['$x']) == u'$x'
    assert ansible_native_concat([NativeJinjaText('$x')]) == NativeJinjaText('$x')

    # Function call given multiple arguments
    assert ansible_native_concat(['$x', '$y']) == u'$x$y'

# Generated at 2022-06-22 12:10:37.530727
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 2, 3, 'a', 'b', 'c']) == '123abc'
    assert ansible_native_concat(['1', 2, '3', 'a', 'b', 'c']) == '123abc'

# Generated at 2022-06-22 12:10:48.222045
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'a', 'b', 'c']) == u'abc'
    assert ansible_native_concat(((u'a'), (u'b'), (u'c'))) == u'abc'
    assert ansible_native_concat(iter(['a', 2, ['b', 'c'], {u'd': u'e'}])) == u'a2bce'
    assert ansible_native_concat(iter([u'a', u'b', u'c'])) == u'abc'
    assert ansible_native_concat(iter([u'a', 3, u'b', u'c', 1, u'd', u'e'])) == u'a3bc1de'

# Generated at 2022-06-22 12:10:59.244572
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template.safe_eval import ansible_template_expression
    from nose.plugins.skip import SkipTest
    from nose.tools import assert_equal, assert_raises

    literal_in = u"10 < 5"
    literal_out = 5

    implicit_in = u"10 < foo"
    implicit_out = u"10 < foo"

    concat_in = u'"10" < foo'
    concat_out = u"10 < foo"

    literal_eval_error_in = u"[1,2,3,4,5"
    literal_eval_error_out = u"[1,2,3,4,5"


# Generated at 2022-06-22 12:11:00.779186
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # TODO: add unit tests
    pass

# Generated at 2022-06-22 12:11:07.850948
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2