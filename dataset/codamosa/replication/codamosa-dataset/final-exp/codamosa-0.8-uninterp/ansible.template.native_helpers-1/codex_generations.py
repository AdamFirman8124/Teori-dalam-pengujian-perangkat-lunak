

# Generated at 2022-06-22 12:01:15.122797
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.six import PY3
    import sys

    text_wrappers = (text_type,)
    if PY3:
        from ansible.module_utils.common.text.converters import to_text
        from ansible.module_utils.six.moves import builtins
        text_wrappers += (to_text, builtins.str)

    assert ansible_native_concat([]) is None
    assert isinstance(ansible_native_concat([1]), int)
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, 3]) == 123

# Generated at 2022-06-22 12:01:27.540802
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def ensure_native_concat(func):
        def wrapper(*args, **kwargs):
            nodes = func(*args, **kwargs)
            return isinstance(ansible_native_concat(nodes), (list, set, dict, text_type))
        return wrapper

    # Test for several nodes.
    @ensure_native_concat
    def test_nodes():
        return [1, 2, 3, 4]

    # Test for one node.
    @ensure_native_concat
    def test_one_node():
        return [1]

    # Test for undefined node.
    @ensure_native_concat
    def test_undefined_node():
        return [StrictUndefined()]

    assert test_nodes()
    assert test_one_node()
    assert test_undefined

# Generated at 2022-06-22 12:01:38.965939
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:01:51.564645
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from jinja2 import Template

    t = Template(u'{{ ansible_native_concat([{{ data }}, "foo", 42, 42., "bar", True, None, [1, 2]])'
                 u'| to_json }}')

    assert t.render(data="'bar'") == '"barfoo42.042barTrueNone[1, 2]"'
    assert t.render(data=42) == '"42foo42.042barTrueNone[1, 2]"'
    assert t.render(data=42.) == '"42.0foo42.042barTrueNone[1, 2]"'
    assert t.render(data=None) == '"Nonefoo42.042barTrueNone[1, 2]"'

# Generated at 2022-06-22 12:02:03.586564
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    # Define the example nested data structure
    data = {"foo": {"bar": [{"baz": 1}, {"baz": 2}], "fuz": "bar"}}

    # Test the data structure with the function
    assert to_native(data) == data

    # Test a variety of string concat combinations
    assert to_native("foo" "bar") == "foobar"
    assert to_native("foo" "bar" "baz") == "foobarbaz"
    assert to_native("foo" "bar" "baz" "fuz") == "foobarbazfuz"

    # Test a variety of integer concat combinations

# Generated at 2022-06-22 12:02:14.617678
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test for Ansible custom Jinja2 concat function"""

    # Test for a single node, its value is returned
    val = ansible_native_concat([1])
    assert val == 1

    # Test for a value that can be parsed with ast.literal_eval
    val = ansible_native_concat([u'"hello"'])
    assert val == "hello"

    # Test for concatenation of nodes and characters
    val = ansible_native_concat([1, u'-', u'hello'])
    assert val == "1-hello"

    # Test for a single node that cannot be parsed with ast.literal_eval
    val = ansible_native_concat([u'{"key": "value"}'])
    assert val == '{"key": "value"}'

    # Test for no nodes

# Generated at 2022-06-22 12:02:26.472577
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test conversion of native types
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat([1, '2', 3, True]) == '123True'
    assert ansible_native_concat(['1', 2, '3', True]) == '123True'
    assert ansible_native_concat([1, '2', 3, True]) == '123True'
    assert ansible_native_concat(['1', '1']) == '11'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([True, False, False]) == 'TrueFalseFalse'
    assert ansible_native_concat

# Generated at 2022-06-22 12:02:38.052151
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.text.converters import container_to_text

    env = jinja2.Environment(extensions=[])
    env.filters.update(ansible_native=ansible_native_concat)

    def run(input, output):
        assert ansible_native_concat(input) == to_native(output)
        assert env.from_string(u'{{ [%s] | ansible_native }}' % u', '.join(map(jinja2.Markup.escape, input))).render() == output

    run([u'a'], u'a')
    run([u'a', u'b'], u'ab')

# Generated at 2022-06-22 12:02:49.210214
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test native_concat
    from jinja2.environment import Environment
    from jinja2 import StrictUndefined, Undefined
    env = Environment(undefined=StrictUndefined)
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([Undefined(name='Test_Undefined'), 2]) == Undefined(name='Test_Undefined')
    assert ansible_native_concat([1, Undefined(name='Test_Undefined')]) == Undefined(name='Test_Undefined')
    assert ansible_native_concat([1, 2, 3]) == '123'

# Generated at 2022-06-22 12:02:56.581940
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # TODO: Move this test to the testcases
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([u'a', u'b']) == u'ab'

    assert ansible_native_concat(['a', True]) == 'aTrue'
    assert ansible_native_concat(['a', None]) == 'aNone'
    assert ansible_native_concat([True, None]) == 'TrueNone'

    assert ansible_native_concat(['a', 20, 45]) == 'a2045'

# Generated at 2022-06-22 12:03:09.335511
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['123']) == '123'
    assert ansible_native_concat(['123', '456']) == '123456'
    assert ansible_native_concat(['123', '456', '789']) == '123456789'
    assert ansible_native_concat(['123', 5, '789']) == '1235789'
    assert ansible_native_concat([123, 5, 789]) == 1235789
    assert ansible_native_concat(['123', 5, 789]) == '1235789'
    assert ansible_native_concat(['yes']) == 'yes'
    assert ansible_native_concat(['"yes"']) == 'yes'
    assert ans

# Generated at 2022-06-22 12:03:20.542613
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template import Templar

    assert ansible_native_concat([]) is None

    t = Templar(None)

    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([43.0]) == 43.0
    assert ansible_native_concat(['42']) == '42'
    assert ansible_native_concat([t.template('"42"', convert_bare=True)]) == '42'
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([['hello']]) == ['hello']

# Generated at 2022-06-22 12:03:31.554366
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import MappingType

    # Test that native concat returns None for an empty list
    assert ansible_native_concat([]) is None

    # Test that native concat returns the single value for a single entry list
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([{'a': 'b'}]) == {'a': 'b'}
    assert ansible_native_concat([{}]) == {}
    assert ansible_native_concat(['a']) == u'a'
    assert ansible_native_concat([u'a']) == u'a'

    # Test that native concat returns the concatenated values for a given list

# Generated at 2022-06-22 12:03:41.829084
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'1']) != u'1'
    assert ansible_native_concat([u'1.0']) == 1.0
    assert ansible_native_concat([u'1.0']) != u'1.0'
    assert ansible_native_concat([u'1 + 2']) == u'1 + 2'
    assert ansible_native_concat([u'1 + 2']) != 3
    assert ansible_native_concat([u'[1, 2, 3]']) == [1, 2, 3]

# Generated at 2022-06-22 12:03:51.024886
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    '''
    ansible_native_concat
    '''

    class UndefinedValue(StrictUndefined):
        pass

    class UndefinedValue2(StrictUndefined):
        pass

    # Nodes and Values
    nodes = [u"ansible", False, UndefinedValue(undefined_hint=u"hint")]
    values = [u'ansible', False, UndefinedValue(undefined_hint=u'hint')]

    # Expected Results
    result = u'ansibleFalse{{ hint }}'
    result2 = False

    # Test
    assert result == container_to_text(ansible_native_concat(nodes))
    assert isinstance(ansible_native_concat(nodes), text_type)

# Generated at 2022-06-22 12:04:00.121342
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    try:
        import jinja2
        has_jinja = True
    except ImportError:
        has_jinja = False

    if not has_jinja:
        return

    env = jinja2.Environment(
        # NativeJinjaText objects can be processed using ansible's native
        # concatenation.
        native_concatenation_enabled=True,
        extensions=['jinja2.ext.do'])
    env.filters['vault'] = ansible_vault_decrypt


# Generated at 2022-06-22 12:04:10.484733
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['foo', '1', 'bar', '2', 'baz', '3']) == 'foo1bar2baz3'

    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, 3.0]) == 123.
    assert ansible_native_concat([1, 2, 3.1]) == '123.1'

# Generated at 2022-06-22 12:04:19.495745
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['123']) == 123

    assert ansible_native_concat(['baz']) == 'baz'
    assert ansible_native_concat(['abc', 'def', 12]) == u'abcdef12'
    assert ansible_native_concat(['abc', '\n', 'def', '\r', '12']) == u"abc\ndef\r12"
    assert isinstance(ansible_native_concat(['abc', 'def'])[0], text_type)


# Generated at 2022-06-22 12:04:29.730719
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def check(data, expected_result):
        if data is None:
            result = ansible_native_concat(data)
        else:
            result = ansible_native_concat(iter(data))

        assert result == expected_result, \
            'ansible_native_concat(%r) == %r, expected %r' % (data, result, expected_result)

    # These tests are based on tests from Jinja2
    # https://github.com/pallets/jinja/blob/master/tests/test_nativetypes.py

    # NOTE: type annotations are for python 3.7+

    # tests for empty string
    check(iter([]), None)

    # tests for str and unicode objects
    check(['foo'], 'foo')

# Generated at 2022-06-22 12:04:36.942937
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([
        NativeJinjaText(u'{"a": "foo"}|from_json.a')
    ]) == u'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.2]) == 1.2
    assert ansible_native_concat([
        NativeJinjaText(u'{"a": "foo"}|from_json.a'),
        NativeJinjaText(u'foo')
    ]) == u'foofoo'

# Generated at 2022-06-22 12:04:55.153597
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    v1 = 'teststring'
    v2 = 'teststring'
    v3 = 'teststring'
    assert ansible_native_concat(v1) == 'teststring'

    v1 = 'teststring'
    v2 = 'teststring'
    v3 = 'teststring'
    assert ansible_native_concat([v1]) == 'teststring'
    assert ansible_native_concat([v1, v2]) == 'teststringteststring'
    assert ansible_native_concat([v1, v2, v3]) == 'teststringteststringteststring'
    assert ansible_native_concat([v1.split(), v2.split(), v3.split()]) == [['teststring'], ['teststring'], ['teststring']]

# Generated at 2022-06-22 12:05:07.766808
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 2, 3, 4, 5]) == u'12345'
    assert ansible_native_concat(('first', 'second', 'third')) == u'firstsecondthird'
    assert ansible_native_concat(({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})) == \
        u"{'a': 1, 'b': 2}{'c': 3, 'd': 4}{'e': 5, 'f': 6}"

# Generated at 2022-06-22 12:05:21.127272
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert ansible_native_concat([1, ('foo', 'bar', 3)]) == [1, ('foo', 'bar', 3)]
    assert ansible_native_concat([1, ('foo', 'bar', 3), 4]) == [1, ('foo', 'bar', 3), 4]
    assert ansible_native_concat([1, ('foo', 'bar', 3), 4, 5]) == [1, ('foo', 'bar', 3), 4, 5]
    assert ansible_native_concat([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


# Generated at 2022-06-22 12:05:33.334099
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    a = "abc"
    b = "def"
    assert ansible_native_concat([a]) == a
    assert ansible_native_concat([b]) == b
    assert ansible_native_concat([a, b]) == u"abcdef"
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([u"{", "1", "}"]) == u"{1}"
    assert ansible_native_concat([u"[", u"1", u"2", u"]"]) == u"[12]"
    assert ansible_native_concat([u"{", u"'1'", ":", "2", "}"]) == u"{'1': 2}"
    assert ansible_native_

# Generated at 2022-06-22 12:05:41.560228
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native, to_text
    from ansible.module_utils.six import integer_types
    # Note "to_native" is deliberately not passed to the collection of nodes
    def assert_ansible_native_concat(nodes, expected, name=None):
        nodes = [to_text(item) if isinstance(item, string_types) else item for item in nodes]
        if not name:
            name = nodes
        actual = ansible_native_concat(nodes)
        assert actual == expected, "nodes: %s, %s %r != %r" % (name, type(actual), actual, expected)

# Generated at 2022-06-22 12:05:51.853409
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'

    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 2]) == 'a2'
    assert ansible_native_concat(['a', [1, 2]]) == 'a[1, 2]'

    assert ansible_native_concat(['3']) == 3
    assert ansible_native_concat(['3', '4']) == 3
    assert ansible_native_concat([3, '4'])

# Generated at 2022-06-22 12:06:01.600241
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    from ansible.parsing.yaml.data import AnsibleVaultEncryptedYAMLObject
    from ansible.parsing.yaml.loader import AnsibleVaultLibYAMLObjectLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Note that assert_equal here is not going to catch native python types like
    # dict and list, because they are unpacked on assignment to compare their
    # elements. So don't assert_equal on complex datatypes.
    def assert_equal(value1, value2):
        if value1 != value2:
            raise AssertionError("%s != %s" % (value1, value2))


# Generated at 2022-06-22 12:06:09.087857
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['a', 1]) == 'a1'
    assert ansible_native_concat([u'\u00A9', u'\u00AE']) == u'\u00A9\u00AE'
    assert ansible_native_concat([u'a', u'\u00A9'])

# Generated at 2022-06-22 12:06:18.427424
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    res = ansible_native_concat(["hello", "world"])
    assert res == "helloworld"

    res = ansible_native_concat([None, "world"])
    assert res == "world"

    res = ansible_native_concat([["hello", "world"]])
    assert res == ["hello", "world"]

    res = ansible_native_concat(["[", "hello", ",", None, "world", "]"])
    assert res == ["hello", "world"]

    # test to see if literal_eval will strip out leading spaces
    res = ansible_native_concat(["     hello", "world"])
    assert res == "     helloworld"



# Generated at 2022-06-22 12:06:25.373852
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([u'a']) == 'a'
    assert ansible_native_concat([1, 'A']) == '1A'
    assert ansible_native_concat([{'a': 'A'}, {'b': 'B'}]) == "{'a': 'A'}{'b': 'B'}"

# Generated at 2022-06-22 12:06:39.239407
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # String concatenation
    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(('foo', 'bar')) == 'foobar'

    # Python native types
    assert ansible_native_concat([100]) == 100
    assert ansible_native_concat([100.0]) == 100.0
    assert ansible_native_concat([True]) is True

    # String list concatenation
    assert ansible_native_concat([[u'foo', u'bar'], ['foo', 'bar']]) == 'foobarfoobar'

# Generated at 2022-06-22 12:06:47.649582
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1.0, 2.0]) == '1.02.0'
    assert ansible_native_concat([1, 2.0]) == '12.0'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat([1, {'a': 2}, 3]) == '1{u\'a\': 2}3'

# Generated at 2022-06-22 12:06:59.347456
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', '\nb', '\nc']) == 'a\nb\nc'
    assert ansible_native_concat(['a', 'b', 'c\n']) == 'abc\n'
    assert ansible_native_concat(['a', '!', 'b']) == 'a!b'
    assert ansible_native_concat(['a', '!', '', 'b']) == 'a!b'

# Generated at 2022-06-22 12:07:05.171779
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat((0,)) == 0
    assert ansible_native_concat((0, 1)) == '01'
    assert ansible_native_concat(('0', '1')) == '01'
    assert ansible_native_concat((0, '1')) == '01'



# Generated at 2022-06-22 12:07:17.093922
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['str', AnsibleVaultEncryptedUnicode('encrypted_str')]) == 'strencrypted_str'
    assert ansible_native_concat(['str', 1]) == 'str1'
    assert ansible_native_concat(['str', '1']) == 'str1'
    assert ansible_native_concat(['str', 1, '1']) == 'str1111'
    assert ansible_native_concat(['str', 1.0, '1.0']) == 'str1.01.0'
    assert ansible_native_concat(['str', '1.0', 1.0]) == 'str1.01.0'
    assert ansible_native_concat(['str', '"foo"']) == 'str"foo"'
    assert ansible

# Generated at 2022-06-22 12:07:26.228682
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    class FakeNode:
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return '<%s %r>' % (type(self).__name__, self.value)

        def __str__(self):
            return str(self.value)

    nodes = [FakeNode('1'), FakeNode('2')]
    expect = '12'
    result = ansible_native_concat(nodes)
    assert result == expect

    nodes = [FakeNode('1')]
    expect = '1'
    result = ansible_native_concat(nodes)
    assert result == expect

    nodes = [FakeNode(1)]
    expect = 1
    result = ansible_native_concat(nodes)
    assert result == expect


# Generated at 2022-06-22 12:07:38.346434
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([3.14]) == 3.14
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([False]) == False
    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([b'foo']) == b'foo'
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([['foo', 'bar'], 'baz']) == ['foo', 'bar', 'baz']

# Generated at 2022-06-22 12:07:48.115554
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.module_utils.common.text.converters import to_text, to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    if not isinstance(unicode, type(None)):
        # Python 2
        u_type = unicode
    else:
        # Python 3
        u_type = str

    # None
    assert ansible_native_concat([]) is None

    # Single string
    assert ansible_native_concat(['ansible']) == u'ansible'
    assert ansible_native_concat([to_bytes('ansible')]) == u'ansible'

# Generated at 2022-06-22 12:07:59.645457
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test ast.literal_eval correct eval
    assert(ansible_native_concat([ast.literal_eval('5')]) == 5)

    # test ast.literal_eval incorrect eval (return string)
    assert(ansible_native_concat([ast.literal_eval('5a')]) == u'5a')

    # simple concat with one string
    assert(ansible_native_concat([u'foo']) == u'foo')

    # simple concat with two strings
    assert(ansible_native_concat([u'foo', u'bar']) == u'foobar')

    # simple concat with two strings in a generator
    assert(ansible_native_concat(chain([u'foo'], [u'bar'])) == u'foobar')

    # simple concat with two

# Generated at 2022-06-22 12:08:11.627799
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'

    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == [1, '2', 3]
    assert ansible_native_concat([1, 'foo', 2, 'bar', 3]) == [1, 'foo', 2, 'bar', 3]

    assert ansible_native_concat([None, [2], 3]) == [None, [2], 3]

# Generated at 2022-06-22 12:08:32.978765
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'
    assert ansible_native_concat(['foo', 'bar', 42]) == 'foobar42'
    assert ansible_native_concat(['foo', 'bar', '42']) == 'foobar42'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([42, 'bar', 42]) == '42bar42'
    assert ansible_native_concat([42, 'bar', '42']) == '42bar42'
    assert ansible_native_concat([42, 42]) == '4242'
    assert ansible_native_concat([42, 42, 'foo']) == '424242'
    assert ansible_native_concat

# Generated at 2022-06-22 12:08:43.558410
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat((1,)) == 1
    assert ansible_native_concat(('foo', 'bar')) == 'foobar'
    assert ansible_native_concat(('foo', 'bar')) == 'foobar'
    text_1 = NativeJinjaText("foo")
    text_2 = NativeJinjaText("bar")
    assert ansible_native_concat((text_1, text_2)) == 'foobar'

    assert ansible_native_concat(('1', '2')) == 3
    assert ansible_native_concat(('True', 'False')) is False
    assert ansible_native_concat(('False', 'True')) is True
    assert ansible_native_concat(('foo',)) == 'foo'
    assert ansible_native

# Generated at 2022-06-22 12:08:55.451227
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.text import Jinja2String
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert u'abc' == ansible_native_concat(['abc'])
    assert u'abc' == ansible_native_concat(['a', 'b', 'c'])
    assert u'abc' == ansible_native_concat(['a', u'bc'])
    assert u'abc' == ansible_native_concat([u'a', 'bc'])
    assert u'abc' == ansible_native_concat([u'a', u'bc'])
    assert 123 == ansible_native_concat([123])

# Generated at 2022-06-22 12:09:07.418037
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:09:18.665775
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, 'str', 3]) == '1str3'
    assert ansible_native_concat(['1', 'str', '3']) == '1str3'
    assert ansible_native_concat([1, 'str', '3']) == u'1str3'

    # Strings that cannot be parsed with ast.literal_eval should not be
    # parsed with ast.literal_eval
    assert ansible_native_concat(['1str3']) == '1str3'
    assert ansible_native_concat(['1', 'str', '3']) == '1str3'

# Generated at 2022-06-22 12:09:59.169826
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:03.204286
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['False', 'False']) == 'FalseFalse'
    assert ansible_native_concat(['False', 'False']) == 'FalseFalse'
    assert ansible_native_concat(['True', 'False']) == 'TrueFalse'
    assert ansible_native_concat(['True', 'True']) == 'TrueTrue'
    assert ansible_native_concat(['True', '   True']) == 'True   True'
    assert ansible_native_concat(['True', '\tTrue']) == 'True\tTrue'

# Generated at 2022-06-22 12:10:14.593262
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # The function ansible_native_concat does not change the type of
    # the arguments, so we don't need to test strings, numbers, and
    # bools separately.
    class FakeData:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

        __unicode__ = __str__

        def __repr__(self):
            return 'FakeData: %s' % self.value

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert (ansible_native_concat((FakeData('a'), FakeData('b'))) ==
            'FakeData: aFakeData: b')

# Generated at 2022-06-22 12:10:26.157379
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Unit tests for ansible_native_concat. These tests are inspired by the
    unit test for native concatenate found in Jinja2.
    """
    # Strings, unicode and integers can be concatenated without
    # needing to use ast literal_eval
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 6, 'c']) == 'a6c'

    # Dictionaries are not concatenated
    assert ansible_native_concat(['a', {'key1': 'value1'}, 'c']) == 'a{\'key1\': \'value1\'}c'

    # Complex expression

# Generated at 2022-06-22 12:10:33.740575
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['foo', 1, 'bar']) == 'foo1bar'
    assert ansible_native_concat([{'x': 'foo'}]) == {'x': 'foo'}



# Generated at 2022-06-22 12:11:03.358269
# Unit test for function ansible_native_concat