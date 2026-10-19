

# Generated at 2022-06-22 12:01:16.278374
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # check if function exists
    assert callable(ansible_native_concat)

    # check if function returns the original object if only one object is passed
    assert ansible_native_concat('text') == 'text'
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat({'k': 'v'}) == {'k': 'v'}
    assert ansible_native_concat(['a', 'b']) == ['a', 'b']

    # check if the function returns the concatenated value of two strings
    assert ansible_native_concat(['text', 'text']) == 'texttext'

    # check if undefined values raise an exception
    from jinja2.runtime import StrictUndefined

# Generated at 2022-06-22 12:01:28.853064
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import textwrap
    from ansible.template import generate_ansible_native_concat_test_cases
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unicode import to_unicode

    test_cases = generate_ansible_native_concat_test_cases()

    for input_value, expected_output in test_cases:
        if input_value is None:
            input_value = 'None'
        elif isinstance(input_value, (int, float)):
            pass
        elif isinstance(input_value, AnsibleVaultEncryptedUnicode):
            input_value = input_value.data
        else:
            input_value = '"%s"' % input_value

# Generated at 2022-06-22 12:01:40.004590
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'abc']) == u'abc'
    assert ansible_native_concat([123]) == 123
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([u'abc', u'def']) == u'abcdef'
    assert ansible_native_concat([123, 456, 789]) == 123456789
    assert ansible_native_concat([True, False, True]) == u'TrueFalseTrue'
    assert ansible_native_concat([None, None, None]) == u'NonenoneNone'

# Generated at 2022-06-22 12:01:52.357154
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([b'foo']) == u'foo'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([NativeJinjaText(1)]) == 1
    assert ansible_native_concat([NativeJinjaText(u'foo')]) == u'foo'
    assert ansible_native_concat([NativeJinjaText({})]) == {}
    assert ansible_native_concat(x for x in [u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat(x for x in [u'foo', u'bar', u'baz']) == u'foobarbaz'

    assert ansible

# Generated at 2022-06-22 12:02:04.665785
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:02:15.126616
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b ']) == 'ab '
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', ' b ']) == ' a b '
    assert ansible_native_concat(['ab']) == 'ab'
    assert ansible_native_concat(['  ab']) == '  ab'

    assert ansible_native_concat(['a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b']) == u'ab'

# Generated at 2022-06-22 12:02:26.766441
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    class SomeClass:
        pass

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1], [2]) == '12'
    assert ansible_native_concat([1], [2], [3]) == '123'
    assert ansible_native_concat([1.5]) == 1.5
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([b'\x01\x02']) == b'\x01\x02'
    assert ansible_native_concat([text_type()]) == text_type()

# Generated at 2022-06-22 12:02:38.324473
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible_collections.ansible.builtin.tests.unit.compat import unittest
    from ansible.template import Templar

    class TestTemplar(Templar):
        def __init__(self):
            super(TestTemplar, self).__init__(None)

    class TestAnsibleNativeConcat(unittest.TestCase):

        def test_concat_string(self):
            t = TestTemplar()
            # Test concat one string
            nodes = t.template('one', None, None, None, convert_bare=True, fail_on_undefined=True)
            self.assertEqual(ansible_native_concat(nodes), 'one')
            # Test concat two strings

# Generated at 2022-06-22 12:02:48.079579
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test results of ansible_native_concat function.
    """
    # Generate list of (nodes, expected) test data pairs.
    test_data = []

    # Single node, no concatenation.
    test_data.append(
        (
            [ast.parse('42')],
            42,
        ),
    )
    test_data.append(
        (
            [ast.parse('"Hello"')],
            'Hello',
        ),
    )

    # Single node, with concatenation.
    test_data.append(
        (
            [ast.parse('42'), ast.parse('" World"')],
            '42 World',
        ),
    )

    # Nested list of nodes, no concatenation.

# Generated at 2022-06-22 12:03:00.595433
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Basic types are not changed
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert ansible_native_concat([1, 'b', 'c']) == [1, 'b', 'c']
    assert ansible_native_concat([{1: 5}, 'b', 'c']) == [{1: 5}, 'b', 'c']

    # Concat strings
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([1, 'b', 'c']) == '1bc'

# Generated at 2022-06-22 12:03:16.906813
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:03:28.257163
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', 2]) == 1
    assert ansible_native_concat([' 1', 2]) == ' 12'
    assert ansible_native_concat([container_to_text({'test': 'value'}, pretty=False)]) == '{\n  "test": "value"\n}'
    assert ansible_native_concat([container_to_text({'test': 'value'}, pretty=True)]) == '{\n    "test": "value"\n}'

# Generated at 2022-06-22 12:03:39.341060
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', u'baz']) == u'foobarbaz'
    assert ansible_native_concat([u'true']) is True
    assert ansible_native_concat([u'false']) is False
    assert ansible_native_concat([u'']) == u''
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'1.0']) == 1.0

# Generated at 2022-06-22 12:03:50.372932
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Foo():
        def __init__(self, str):
            self.str = str

        def __repr__(self):
            return self.str

    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([u'1']) == u'1'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.1]) == 1.1
    assert ansible_native_concat(['1', '1']) == '11'
    assert ansible_native_concat([u'1', u'1']) == u'11'
    assert ansible_native_concat([1, 1]) == '11'
    assert ansible_native

# Generated at 2022-06-22 12:04:01.958143
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    string = to_text(ansible_native_concat(['123', '456', '789']))
    assert string == '123456789'
    string = to_text(ansible_native_concat(['123', '456', '789']))
    assert string == '123456789'
    string = container_to_text(
        ansible_native_concat(['123', '456', ['789', ['0']]])
    )
    assert string == '[\'123\', \'456\', [\'789\', [\'0\']]]'
    string = container_to_text(
        ansible_native_concat(['123', '456', ['789', ['0']]])
    )
    assert string == '[\'123\', \'456\', [\'789\', [\'0\']]]'
   

# Generated at 2022-06-22 12:04:11.728218
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([1, 'a', 2]) == 12
    assert ansible_native_concat(['1', 'a', 2]) == '1a2'
    assert ansible_native_concat([1, 'a', '2']) == 12
    assert ansible_native_concat([1, 2, None]) is None
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['[', '{', '1', '2', '}', ']']) == '[{1 2}]'

# Generated at 2022-06-22 12:04:20.361781
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import Templar

    t = Templar(loader=None)
    # run through to_native to convert to ansible native types
    # rather than native Python types
    assert to_native(t.template('{{ [1, 2] + [3, 4] }}')) == [1, 2, 3, 4]
    assert to_native(t.template(u'{{ [1, 2] + [3, 4] }}')) == [1, 2, 3, 4]
    assert to_native(t.template(u'{{ (1, 2) + (3, 4) }}')) == (1, 2, 3, 4)

# Generated at 2022-06-22 12:04:30.212481
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([u'42']) == 42
    assert ansible_native_concat([u' 42']) == u' 42'
    assert ansible_native_concat([u'42 ']) == u'42 '
    assert ansible_native_concat([u' 42 ']) == u' 42 '
    assert ansible_native_concat([u'42', u'42']) == u'4242'
    assert ansible_native_concat([u'42', u' 42']) == u'42 42'
    assert ansible_native_concat([u'42 ', u'42']) == u'42 42'

# Generated at 2022-06-22 12:04:37.205549
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat(map(int, '123')) == u'123'
    assert ansible_native_concat([1, 2.0]) == u'12.0'
    assert ansible_native_concat([1, 2.0, 3.0]) == u'12.03.0'
    assert ansible_native_concat(map(float, '123')) == u'123.0'
    assert ansible_native_concat([1, None]) == u'1None'
    assert ans

# Generated at 2022-06-22 12:04:40.900272
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test case for Compiler.visit_Concat
    # https://github.com/pallets/jinja/blob/6d68b1fc32d937187e6e7f6c22908da7ce3f53ee/src/jinja2/compiler.py#L400-L407
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([2]) == 2
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat(['a']) == 'a'

    # Test case for Compiler.visit_BinOp
    # https://github.com/pallets/jinja/blob/6d68b1fc32d937187e6e7f6c22908da7ce3f53ee/

# Generated at 2022-06-22 12:04:57.475778
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None == ansible_native_concat([])

    assert 1 == ansible_native_concat([1])

    assert "hello" == ansible_native_concat(["hello"])

    assert "1" == ansible_native_concat(["1"])

    assert "hello goodbye" == ansible_native_concat(["hello", " ", "goodbye"])

    assert "hello goodbye" == ansible_native_concat(["hello ", "goodbye"])

    assert u"hello goodbye" == ansible_native_concat([u"hello", " ", "goodbye"])

    assert u"hello goodbye" == ansible_native_concat([u"hello ", "goodbye"])

    assert ["hello", "goodbye"] == ansible_native_concat(['["hello", "goodbye"]'])

# Generated at 2022-06-22 12:05:08.586540
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class FakeUndefined():
        def __str__(self):
            raise Exception('Fail')
        __unicode__ = __str__

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == "12"
    assert ansible_native_concat([1, 2, 3]) == "123"
    assert ansible_native_concat(['a', 2, 3]) == "a23"
    assert ansible_native_concat(['a', 'b', 'c']) == "abc"
    assert ansible_native_concat(['a', 'b', 'c']) == "abc"
    assert ansible_native_concat(['a', 'b', 'c']) == "abc"

# Generated at 2022-06-22 12:05:21.808341
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # This test is taken from nativetypes.py in jinja2
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([False, True]) == False
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([('a', 'b'), ('c', 'd')]) == ('ab', 'cd')
    assert ansible_native_concat([1, 'a', 2, 'b', 3, 'c']) == '1a2b3c'
    assert isinstance(ansible_native_concat([1, 2]), int)

# Generated at 2022-06-22 12:05:33.892399
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test if a string is returned as is
    assert (
        ansible_native_concat([u'foo\n']) ==
        u'foo\n'
    )

    # test if a list is returned as is
    assert (
        ansible_native_concat([[u'foo', u'bar']]) ==
        [u'foo', u'bar']
    )

    # test if a dict is returned as is
    assert (
        ansible_native_concat([{u'foo': u'bar'}]) ==
        {u'foo': u'bar'}
    )

    # test if a float is returned as is
    assert (
        ansible_native_concat([42.42]) ==
        42.42
    )

    # test if an integer is returned as is

# Generated at 2022-06-22 12:05:44.588783
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # TODO: ansible_vault
    def get_node(value):
        # Return the node from a Jinja template like {% set data = value %}.
        # This is a helper function for testing.
        # Parameter "value" can be a Python native type, an already compiled
        # node, or a Jinja template string.
        if not isinstance(value, string_types):
            tmpl = '{{ data }}'
            if isinstance(value, types.GeneratorType):
                tmpl = '{% for _ in data %}{% endfor %}'
        else:
            tmpl = '{% set data = {} %}{{ data }}'.format(value)

        env = jinja2.Environment(trim_blocks=True)

# Generated at 2022-06-22 12:05:55.717106
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Cases for single node
    assert ansible_native_concat([3]) == 3
    assert ansible_native_concat(['a']) == 'a'

    # Cases for multiple nodes
    assert ansible_native_concat([3, ' ']) == '3 '
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'

    # Cases for dynamic list of nodes
    assert ansible_native_concat(x for x in [1, 2, 3]) == '123'
    assert ansible_native_concat(x for x in [1, ' ', 2, ' ', 3]) == '1 2 3'
    assert ansible_native_concat(x for x in [1, ' ', 2, ' ', 3]).strip() == '1 2 3'

    # Cases for literal

# Generated at 2022-06-22 12:06:06.458010
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment(extensions=['jinja2.ext.nativetypes'])
    assert env.from_string('"{{ [1] }}"').render() == '"[1]"'
    assert env.from_string('{{ [1] }}').render() == '[1]'
    assert env.from_string('{% if [1] %}{{ [1] }}{% endif %}').render() == '[1]'
    assert env.from_string('{{ "foo" }} {{ "bar" }}').render() == 'foo bar'
    assert env.from_string('"{{ "foo" }}" "{{ "bar" }}"').render() == '"foo" "bar"'

# Generated at 2022-06-22 12:06:13.125911
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3, 4]) == 10
    assert ansible_native_concat([1, 2, 3, 'a']) == '1a'
    assert ansible_native_concat(['a', 2, 3, 'a']) == 'a2a'
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a']) != 'b'
    assert ansible_native_concat(['a']) != b'a'



# Generated at 2022-06-22 12:06:23.112156
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'

# Generated at 2022-06-22 12:06:35.116728
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([1, u'b']) == u'1b'
    assert ansible_native_concat([u'a', 1]) == u'a1'
    assert ansible_native_concat([u' a ', u' b ']) == u' a  b '
    assert ansible_native_concat([u'\thello ', u' world ', u'!']) == u'\thello  world !'
    assert ansible_native_concat([1, 2, 3, 4, 5]) == 12345

# Generated at 2022-06-22 12:06:49.443702
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([None, 1, 2, 3, None, None]) == 123

    assert ansible_native_concat([True, ' is ', False, ' and ', True, ' is ', True]) == 'True is False and True is True'

    assert ansible_native_concat([True, 2, 3, 4, None, None]) == 'True234'

    assert ansible_native_concat([1, 2, 3, None, 4, 5, None]) == 12345

    assert ansible_native_concat([None, None, None]) is None

    assert ansible_native_concat([None]) is None

    assert ansible_native_concat([]) is None

    assert ansible_native_concat([b'123']) == 123


# Generated at 2022-06-22 12:07:00.135405
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['example']) == 'example'
    assert ansible_native_concat(['example', 'example']) == 'exampleexample'
    assert ansible_native_concat([1, '2']) == 12
    assert ansible_native_concat(['1', '2']) == 12
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([1, '2', '3']) == 123
    assert ansible_native_concat([1, '2', True]) == [1, '2', True]



# Generated at 2022-06-22 12:07:11.677203
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:07:21.033034
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == to_text('foobar')
    assert ansible_native_concat(['foo', '{{ bar }}']) == to_text('foo{{ bar }}')
    assert ansible_native_concat(['{{ foo }}', 'bar']) == to_text('{{ foo }}bar')
    assert ansible_native_concat(['{{ foo }}', '{{ bar }}']) == to_text('{{ foo }}{{ bar }}')

    assert ansible_native_concat(['foo']) == to_text('foo')
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1.0']) == 1.0

    assert ansible_native_concat(['True']) is True
   

# Generated at 2022-06-22 12:07:32.268154
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    t = Templar(loader=AnsibleLoader, undefined=StrictUndefined, tmplpath='dummy', variables={}, jinja_native_concat=ansible_native_concat)

    # Test normal use cases
    assert t.template('{{ [1, 2, 3] }}') == container_to_text([1, 2, 3]) == '1,2,3'
    assert t.template('{{ [1, 2, 3] | to_json }}') == '[1, 2, 3]'
    assert t.template('{{ "{{ ansible_hostname }}" }}') == '{{ ansible_hostname }}'
   

# Generated at 2022-06-22 12:07:43.265691
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat(['0']) == '0'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat(['True']) == 'True'
    assert ansible_native_concat([False]) == False

# Generated at 2022-06-22 12:07:54.615287
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with a single (non-iterable) node
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['2']) == '2'
    assert ansible_native_concat(['2.1']) == '2.1'
    assert ansible_native_concat([2]) == 2
    assert ansible_native_concat([2.1]) == 2.1
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([[1, 2, 3]]) == '[1, 2, 3]'

# Generated at 2022-06-22 12:08:07.397664
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert callable(ansible_native_concat) or callable(ansible_native_concat.__wrapped__)

    # test_nested_data_compiled_node
    nested_data = ansible_native_concat([NativeJinjaText(container_to_text(1))])
    assert nested_data == 1

    # test_nested_data_many_compiled_nodes
    with_nested_data = ansible_native_concat([NativeJinjaText(container_to_text(1)), NativeJinjaText(container_to_text(2))])
    assert with_nested_data == '12'

    # test_nested_data_list

# Generated at 2022-06-22 12:08:16.842902
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['test ', 'string']) == 'test string'
    assert ansible_native_concat(['5', '+5']) == 10
    assert ansible_native_concat(['test_', 'string']) == 'test_string'
    assert ansible_native_concat(['test string']) == 'test string'
    assert ansible_native_concat(['test', 'string']) == 'teststring'
    assert ansible_native_concat([u'unicode ', u'string']) == u'unicode string'
    assert isinstance(ansible_native_concat([u'unicode ', u'string']), text_type)
    assert ansible_native_concat(['5.5']) == 5.5

# Generated at 2022-06-22 12:08:28.940574
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import yaml
    from ansible.module_utils.common.collections import is_sequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    # https://github.com/pallets/jinja/blob/master/src/jinja2/nativetypes.py
    # Test cases from nativetypes.py

# Generated at 2022-06-22 12:08:49.873531
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    test_values = {
        'nodes': [None, None],
        'expected_return': None,
        'description': "Check concatenation of two None nodes returns None"
    }
    assert ansible_native_concat(test_values['nodes']) == test_values['expected_return'], test_values['description']

    test_values = {
        'nodes': [None, 0],
        'expected_return': 0,
        'description': "Check concatenation of None and 0 returns 0"
    }
    assert ansible_native_concat(test_values['nodes']) == test_values['expected_return'], test_values['description']


# Generated at 2022-06-22 12:09:01.598344
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.module_utils.common.text.converters import to_bytes

    assert ansible_native_concat(['x', 'y']) == 'xy'
    assert ansible_native_concat('xy') == 'xy'
    assert ansible_native_concat(['x', to_unicode('y')]) == 'xy'
    assert ansible_native_concat(['x', 'y']) != 'XX'
    assert ansible_native_concat(['x', to_unicode('y')]) != 'XX'
    assert ansible_native_concat(None) is None
    assert ansible_native_

# Generated at 2022-06-22 12:09:12.291295
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # value types
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.1]) == 1.1
    assert ansible_native_concat(['string']) == 'string'
    assert ansible_native_concat([u'unicode']) == u'unicode'
    assert ansible_native_concat([b'bytes']) == b'bytes'

    # native types
    assert ansible_native_concat([u'{"foo": "bar"}']) == dict(foo='bar')
    assert ansible_native_concat([u'"string" "string"']) == u'stringstring'

    # complex native types

# Generated at 2022-06-22 12:09:23.866750
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert not ansible_native_concat([])

    for value in ('', 'foo', 1, 1.0, ('a', 'b'), ('a',)):
        assert ansible_native_concat([value]) == value

    for values in (
            [('a',), 'b'],
            ['a', ('b',)],
            [('a',), ('b',)],
            ['a', 'b'],
            [1, 2],
            [1.0, 2.0],
    ):
        assert ansible_native_concat(values) == container_to_text(values)

    node = text_type  # this is what is returned on a | string filter

# Generated at 2022-06-22 12:09:59.119335
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:04.216523
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test Jinja2 native type implementation ansible_native_concat."""

    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['True']) is True
    assert ansible_native_concat(['False']) is False
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, 'foo']) == '123foo'
    assert ansible_native_concat(['[1, 2]', '[3, 4]']) == [1, 2, 3, 4]

# Generated at 2022-06-22 12:10:14.983803
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Ensure that the function returns the exact same results as Jinja2
    # StrictUndefined class.
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([StrictUndefined()]) is StrictUndefined
    assert ansible_native_concat([StrictUndefined(), 1]) is StrictUndefined
    assert ansible_native_concat([2, StrictUndefined()]) is StrictUndefined
    assert ansible_native_concat([1, 2, 3]) == '123'

# Generated at 2022-06-22 12:10:26.582092
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.template import TemplateError

    # Test empty list of nodes
    assert ansible_native_concat([]) == None

    # Literal values
    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([False]) == False
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([42.0]) == 42.0
    assert ansible_native_concat(["42"]) == "42"
    assert ansible_native_concat(["42.0"]) == "42.0"
    assert ansible_native_concat([AnsibleVaultEncryptedUnicode('vaulted_42')]) == 'vaulted_42'

# Generated at 2022-06-22 12:10:36.459594
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:42.653813
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, DictLoader
    from textwrap import dedent

    env = Environment(
        loader=DictLoader(
            {
                'template.j2': dedent(
                    '''\
                    {{ [
                        '1.2.3',
                        '4.5.6',
                    ]|join('.') }}
                    '''
                )
            }
        )
    )
    # Add concat filter to environment
    env.filters['concat'] = ansible_native_concat

    template = env.get_template('template.j2')
    assert template.render() == '1.2.3.4.5.6'



# Generated at 2022-06-22 12:11:05.905828
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat(['1', 2]) == '12'
    assert ansible_native_concat(['1', '2']) == '1' '2'
    assert ansible_native_concat([u'\u1d57']) == u'\u1d57'
    assert ansible_native_concat([u'\u1d57', u'\u1d58']) == u'\u1d57\u1d58'