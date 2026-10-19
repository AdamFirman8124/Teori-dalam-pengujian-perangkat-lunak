

# Generated at 2022-06-22 12:01:14.723845
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # should return None when an empty list is given
    assert ansible_native_concat(list()) is None

    # should return the string "1" when a list with a single element
    # containing the integer 1
    assert ansible_native_concat(list([1])) == '1'

    # should return the string "a" when a list with a single element
    # containing the string "a"
    assert ansible_native_concat(list(['a'])) == 'a'

    # should return the string "ab" when a list with two elements
    # containing the string "a" and the string "b"
    assert ansible_native_concat(list(['a', 'b'])) == 'ab'

    # should return the string "1" when a list with two elements
    # containing the integer 1 and the string "

# Generated at 2022-06-22 12:01:27.079617
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function ansible_native_concat, which is used to convert Jinja2
    nodes to Python objects, using the standard library `ast.literal_eval`
    function.
    """
    import unittest
    import json

    class TestAnsibleNativeConcat(unittest.TestCase):

        def test_issue_70276(self):
            """Test for Issue 70276
            https://github.com/ansible/ansible/issues/70276

            This test verifies that the Jinja2 node for an integer (Jinja2
            expression `1`) gets converted to a Python object with the value
            1.
            """
            class FakeJinja2Node():
                def __init__(self, value):
                    self.value = value

            node = FakeJinja2Node(1)
            self

# Generated at 2022-06-22 12:01:37.106526
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(iter([1])) == 1

    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat(iter([0])) == 0

    assert ansible_native_concat([u"foo"]) == u"foo"
    assert ansible_native_concat(iter([u"foo"])) == u"foo"

    assert ansible_native_concat([b"foo"]) == b"foo"
    assert ansible_native_concat(iter([b"foo"])) == b"foo"


# Generated at 2022-06-22 12:01:50.172610
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_native_concat(actual, expected):
        # assert type and value:
        assert expected == actual

        # assert that the function returns a native type:
        assert isinstance(actual, type(expected))

    assert_native_concat(ansible_native_concat(["", ""]), u"")
    assert_native_concat(ansible_native_concat([1, 2]), u"12")
    assert_native_concat(ansible_native_concat([1, "", ""]), u"1")
    assert_native_concat(ansible_native_concat([True, False]), u"TrueFalse")
    assert_native_concat(ansible_native_concat([True, "", ""]), True)


# Generated at 2022-06-22 12:02:02.577836
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_bytes

    module = AnsibleModule({})

    # It should return a single item as is
    assert ansible_native_concat([42]) == 42

    # It should concatenated strings
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'

    # It should concatenated strings and parse them if possible
    assert ansible_native_concat([u'1', u'2']) == 12
    assert ansible_native_concat([u'1.0', u'2.0']) == 1.0
    assert ansible_native_concat([u'1.0', u'2']) == 1.02
    assert ans

# Generated at 2022-06-22 12:02:13.812896
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Markup, Undefined
    from jinja2.nativetypes import Slice, slice_context
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.six import PY3


# Generated at 2022-06-22 12:02:26.096502
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([text_type(1)]) == 1
    assert ansible_native_concat([text_type(True)]) is True
    assert ansible_native_concat([text_type("1"), text_type("2")]) == "12"
    assert ansible_native_concat([text_type("1"), text_type("2")]) == "12"
    assert ansible_native_concat([text_type("1"), text_type("2"), text_type("3")]) == "123"
    assert ansible_native_concat([[text_type("1"), text_type("2")], [text_type("3"), text_type("4")]]) == ["1", "2", "3", "4"]

# Generated at 2022-06-22 12:02:37.768996
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.runtime import Context
    from jinja2.nodes import Name, Const, Concat, If, List, Getitem, Keyword, Call

    # name
    assert native_concat_wrapper(Name('v', 'load')).eval(Context()) == 'v'

    # const
    assert native_concat_wrapper(Const(1)).eval(Context()) == 1
    assert native_concat_wrapper(Const('a')).eval(Context()) == 'a'
    assert native_concat_wrapper(Const([1, 2, 3])).eval(Context()) == [1, 2, 3]

# Generated at 2022-06-22 12:02:47.994316
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat(['foo', 1, 2]) == u'foo12'
    assert ansible_native_concat(['foo ', 1, ',', 2]) == u'foo 1,2'
    assert ansible_native_concat(['foo ', 1, ',', 2, ' bar']) == u'foo 1,2 bar'
    assert ansible_native_concat(['foo ', 1, ',', 2, ' bar ']) == u'foo 1,2 bar '
    assert ansible_native_concat([' foo ', 1, ',', 2, ' bar ']) == u' foo 1,2 bar '

# Generated at 2022-06-22 12:03:00.055854
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == "12"

    # Test that our literal_eval logic short-circuits if the result is not a string
    assert ansible_native_concat([1, '2']) == 1

    # Test that literal_eval is called for strings
    assert ansible_native_concat(['1', '2']) == 1
    assert ansible_native_concat(['a', 'b']) == "ab"
    assert ansible_native_concat(['a,b']) == "a,b"
    assert ansible_native_concat(['a,', 'b']) == "a,b"

# Generated at 2022-06-22 12:03:13.684013
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None == ansible_native_concat(None)
    assert None == ansible_native_concat([])
    assert 'test' == ansible_native_concat(['test'])
    assert 'test' == ansible_native_concat(('test',))
    assert 'test' == ansible_native_concat('test')
    assert u'\u2018' == ansible_native_concat([u'\u2018'])
    assert u'\u2018' == ansible_native_concat((u'\u2018',))
    assert u'\u2018' == ansible_native_concat(u'\u2018')
    assert 'test' == ansible_native_concat(NativeJinjaText('test'))

# Generated at 2022-06-22 12:03:23.350604
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat((1, '+', 2)) == 3
    assert ansible_native_concat(('1', '+', 2)) == '1+2'
    assert ansible_native_concat((1, '+', '2')) == '1+2'
    assert ansible_native_concat(('1', '+', '2')) == '1+2'
    assert ansible_native_concat(('1', '+', '2', '+', '3')) == '1+2+3'
    assert ansible_native_concat(('1', '+', '2', 1, '+3')) == '1+2+13'
    assert ansible_native_concat(('string', '+', 'value')) == 'string+value'
    assert ansible

# Generated at 2022-06-22 12:03:33.976950
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_bytes

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.safe_eval import compile_expression

    from jinja2.runtime import Undefined

    from nose import SkipTest

    from nose.tools import assert_equal, assert_instance, assert_is

    try:
        import jinja2
    except ImportError:
        raise SkipTest("jinja2 is not installed")

    E = compile_expression('{{ value }}')

    def render_template(template, value):
        try:
            return template.render(value=value)
        except Undefined as e:
            return e

    U = Undefined

    template = jinja2.Template(E)


# Generated at 2022-06-22 12:03:43.127578
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat(['a', 'b']) == u'ab'
    assert ansible_native_concat([]) is None
    assert isinstance(ansible_native_concat(['1']), int)
    assert isinstance(ansible_native_concat(["1"]), int)
    assert isinstance(ansible_native_concat([1]), int)
    assert isinstance(ansible_native_concat(['a']), text_type)
    assert isinstance(ansible_native_concat(['a', 'b']), text_type)
    assert isinstance(ansible_native_concat(['a\nb']), text_type)

# Generated at 2022-06-22 12:03:54.577541
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([[1, 2, 3]]) == [1, 2, 3]
    assert ansible_native_concat([{}]) == {}

# Generated at 2022-06-22 12:04:04.680606
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import os
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.common.text.converters import to_text

    # a few tests copied from jinja2.nativetypes.
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == "12"
    assert ansible_native_concat([1, 2, 3]) == "123"
    assert ansible_native_concat(["1", "2"]) == "12"
    assert ansible_native_concat(["1", "2", "3"]) == "123"
    assert ansible_native_concat(("1", "2")) == "12"

# Generated at 2022-06-22 12:04:16.298563
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test empty input
    result = ansible_native_concat([])
    assert result is None

    # test single input
    data = dict(a=dict(b=1),
                c="c",
                d=[1, 2, 3],
                e=set(),
                f=range(3),
                g="  123\n")
    for key in data:
        with_vault = AnsibleVaultEncryptedUnicode(data[key])
        result = ansible_native_concat([key])
        assert result == key
        result = ansible_native_concat([with_vault])
        assert result == with_vault.data

    for key in data:
        result = ansible_native_concat([data[key]])
        assert result == data[key]

# Generated at 2022-06-22 12:04:27.765070
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    my_data = [
        [[1, 2, [3]], 4],
        {'a': [{u'b': [{u'c': u'foo'}, u'bar', 123]}], 'b': 'baz'},
        {'a': 'b', 'c': u"foo\'bar"}
    ]

    # We do a double conversion to ensure equality
    # for our purpose we can consider 'str(str(obj)) == str(obj)'
    # to be true
    if to_text(to_text(my_data)) != to_text(ansible_native_concat(my_data)):
        print(u'Expected: {}'.format(container_to_text(my_data)))

# Generated at 2022-06-22 12:04:36.262243
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['None']) == 'None'
    assert ansible_native_concat(['None', '1']) == 'None1'
    assert ansible_native_concat(u'None', 1) == u'None1'
    assert ansible_native_concat([u'None', 1]) == u'None1'
    assert ansible_native_concat([u'None', 1], u'2', 3) == u'None123'

# Generated at 2022-06-22 12:04:46.960905
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([100, 'b', 'c']) == [100, 'b', 'c']
    assert ansible_native_concat([100, True, 'c']) == [100, True, 'c']
    assert ansible_native_concat([100, True, 'c']) == [100, True, 'c']

    assert ansible_native_concat([100]) == 100
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([1.1]) == 1.1

    assert ansible_native_concat([StrictUndefined()]) is None
   

# Generated at 2022-06-22 12:04:59.895150
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    none = ansible_native_concat([])
    none_val = ansible_native_concat([StrictUndefined()])
    five = ansible_native_concat([5])
    five_str = ansible_native_concat(['5'])
    five_str_val = ansible_native_concat([StrictUndefined(), '5', StrictUndefined()])
    one_two_three = ansible_native_concat(['1', '2', '3'])
    one_two_three_val = ansible_native_concat([1, '2', StrictUndefined()])

    assert none is None
    assert none_val is None
    assert five == 5
    assert five_str == 5
    assert five_str_val == 5
    assert one_two_three == 123
   

# Generated at 2022-06-22 12:05:05.509885
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import ansible.plugins.filter.native as ansible_native
    result = ansible_native.ansible_native_concat(['a', 'b', 'c'])
    assert result == 'abc'
    result = ansible_native.ansible_native_concat(('a', 'b', 'c'))
    assert result == 'abc'

# Generated at 2022-06-22 12:05:12.268448
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import nodes
    from ansible.module_utils.native_jinja import native_concat as nc
    from ansible.module_utils.common.text.converters import to_native

    def test_equals(**kwargs):
        assert(ansible_native_concat(**kwargs) == nc(**kwargs))

    # Simple test case
    test_equals(nodes=[nodes.Const("1"), nodes.Const("2")])

    # Ignore anything not a Const
    test_equals(nodes=[nodes.Const("1"), nodes.Name("foo"), nodes.Const("2")])

    # More complicated test cases

    # The following should be passed into ast.literal_eval and converted to
    # native Python types.

# Generated at 2022-06-22 12:05:24.850639
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['string']) == 'string'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([[1, 2]]) == [1, 2]
    assert ansible_native_concat([(1, 2)]) == (1, 2)
    assert ansible_native_concat(['string', 1, [True]]) == 'string1[True]'
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([NativeJinjaText('test')]) == NativeJinjaText('test')

    assert ansible_native_concat([1, 2, 3]) == '123'

# Generated at 2022-06-22 12:05:35.613565
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject


# Generated at 2022-06-22 12:05:44.592401
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test string, int, floats and boolean type
    assert ansible_native_concat([1, None, 2, 'three']) == "1two3three"
    assert ansible_native_concat([' {{', '}} ']) == ' {{}} '
    assert ansible_native_concat(['one', '{{', '}}']) == 'one{{}}'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat([1.1]) == 1.1
    assert ansible_native_concat([.1]) == 0.1
    assert ansible_native_concat(['1.1']) == 1.1
    assert ansible_native_concat([True]) == True
    assert ansible

# Generated at 2022-06-22 12:05:55.766067
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', '', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo  ', '  bar']) == 'foo  bar'
    assert ansible_native_concat(['foo', '', '', 'bar']) == 'foobar'
    assert ansible_native_concat([' ', '  ', 'foo', '', '', 'bar', ' ']) == '  foo  bar '

    assert ansible_native_concat('foo') == 'foo'
    assert ansible_native_concat('') is None

    assert ansible_native_concat([1, 2]) == 12

# Generated at 2022-06-22 12:06:06.456349
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['1', 2, 3]) == '123'
    assert ansible_native_concat([1, '2', '3']) == '123'
    assert ansible_native_concat([1, ['2', '3'], 4]) == '123'
    assert ansible_native_concat([1, '2', '3', 4]) == '1234'
    assert ansible_native_concat(['1', '2', '3', '4']) == '1234'
    assert ansible_

# Generated at 2022-06-22 12:06:15.870555
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class TestUndefined(StrictUndefined):
        def __str__(self):
            raise self._undefined_exception_class('test')

    assert ansible_native_concat([container_to_text('  1234')]) == '  1234'
    assert ansible_native_concat([1234]) == 1234
    assert ansible_native_concat([container_to_text('  -1234')]) == -1234
    assert ansible_native_concat([container_to_text('  01234')]) == 1234
    assert ansible_native_concat([container_to_text('  0x1234')]) == 0x1234
    assert ansible_native_concat([container_to_text('  0o1234')]) == 0o1234
    assert ansible_native_con

# Generated at 2022-06-22 12:06:24.371476
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six import PY2, text_type
    import pytest

    # Test concat
    assert ansible_native_concat([1, 2]) == "12"
    if PY2:
        # Check the concat function is not creating bytestring
        assert isinstance(ansible_native_concat([1, 2]), text_type)

    # Test literaleval
    assert ansible_native_concat([1, '+', 2]) == 3
    assert ansible_native_concat(['"', 'abc', '"']) == "abc"
    assert ansible_native_concat(['"', 'abc', '"', '"', 'def', '"']) == "abc\"def"

    # Test undefined

# Generated at 2022-06-22 12:06:39.957179
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Test with simple strings
    assert ansible_native_concat(['1', '2']) == '12'

    # Test with tainted strings
    assert ansible_native_concat([AnsibleUnsafeText('1'), '2']) == '12'
    assert ansible_native_concat(['1', AnsibleUnsafeText('2')]) == '12'
    assert ansible_native_concat([AnsibleUnsafeText('1'), AnsibleUnsafeText('2')]) == '12'

    # Test with native numbers
    assert ansible_native_concat([1, 2]) == 12

    # Test with tainted numbers
    assert ansible_native_concat([AnsibleUnsafeText(1), 2]) == 12

# Generated at 2022-06-22 12:06:49.244867
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert ansible_native_concat([1, 'b', 2]) == '1b2'
    assert ansible_native_concat([{'a': 1}, {'b': 2}]) == [{'a': 1}, {'b': 2}]
    assert ansible_native_concat([{'a': 2}, 'b', 3]) == "{'a': 2}b3"
    assert ansible_native_concat([{'a': 2}, 'b', 3, {'c': 4}]) == "{'a': 2}b3{'c': 4}"
    assert ansible_native_con

# Generated at 2022-06-22 12:07:01.185345
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import json

    class MyDict(dict):
        def __str__(self):
            return json.dumps(self, sort_keys=True)

    v1 = {'a': 'b c'}
    v2 = {'a': 'b', 'b': 'c'}

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([v1, v2]) == '{"a": "b", "b": "c"}{"a": "b c"}'
    assert ansible_native_concat([v1, MyDict(v2)]) == '{"a": "b c"}{"a": "b", "b": "c"}'

# Generated at 2022-06-22 12:07:04.681491
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'



# Generated at 2022-06-22 12:07:16.772653
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Variable:
        # Use a class to create a mock type
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return repr(self.value)

    def literal_eval(value):
        if value == '-1':
            raise ValueError()
        if value == '-2':
            # Fall through to parsing
            raise SyntaxError()
        if value == '-3':
            raise MemoryError()
        return value

    ansible_native_concat._literal_eval = literal_eval

    # empty list
    assert ansible_native_concat(list()) == None

    # single item
    assert ansible_native_concat([Variable(None)]) == None

   

# Generated at 2022-06-22 12:07:19.293698
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(iter(range(9))) == 123456789



# Generated at 2022-06-22 12:07:30.339872
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check if function correctly short-circuits concatenation if a non-string
    # value is provided.
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat(['value']) == 'value'

    # Check if function correctly concatenates strings.
    assert ansible_native_concat(['first', 'second']) == 'firstsecond'

    # Check if function correctly parses a string as a python literal if it
    # can be parsed as one.
    assert ansible_native_concat(['{', '"key": "value"', '}']) == {
        'key': 'value'
    }

    # Check that if the string cannot be parsed as a python literal, it gets returned.

# Generated at 2022-06-22 12:07:41.745545
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    assert to_native('test') == "test"
    assert to_native('"test"') == "test"
    assert to_native('"test') == "\"test"
    assert to_native("123") == 123
    assert to_native("123.2") == 123.2
    assert to_native("123.2") == 123.2
    assert to_native("-1") == -1
    assert to_native("[1,2,3]") == [1, 2, 3]
    assert to_native("[1,2,3,4]") == [1, 2, 3, 4]
    assert to_native("[1,2,3,4]") == [1, 2, 3, 4]
    assert to_

# Generated at 2022-06-22 12:07:42.374984
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    pass



# Generated at 2022-06-22 12:07:53.440530
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([NativeJinjaText("foo")]) == "foo"
    assert ansible_native_concat([NativeJinjaText("foo"), NativeJinjaText("bar")]) == "foobar"
    assert ansible_native_concat([NativeJinjaText("foo"), NativeJinjaText("bar")]) == "foobar"
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.2]) == 1.2

    # Complex number
    assert ansible_native_concat([1.2j]) == 1.2j

    # TODO:

# Generated at 2022-06-22 12:08:09.811696
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, ' ']) == '1 '
    assert ansible_native_concat([1, ' ', 2]) == 3
    assert ansible_native_concat([1, ' ', 'a']) == '1 a'
    assert ansible_native_concat([1, ' ', 'a', ' ', 2]) == '1 a 2'
    assert ansible_native_concat(['a', ' ', 2]) == 'a 2'
    assert ansible_native_concat(['a', ' ', 'b']) == 'a b'
    assert ansible_native_concat([{'a': 1}, ' ']) == {'a': 1}

# Generated at 2022-06-22 12:08:18.117341
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    node1 = NativeJinjaText('foo')
    node2 = NativeJinjaText('bar')

    assert ansible_native_concat([node1]) == 'foo'
    assert ansible_native_concat([node1, node2]) == 'foobar'
    assert ansible_native_concat(islice([node1, node2], 1)) == 'foo'
    assert ansible_native_concat(islice([node1, node2], 2)) == 'foobar'
    assert ansible_native_concat(islice([node1, node2], 1, 2)) == 'bar'



# Generated at 2022-06-22 12:08:30.415239
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from jinja2.tests import env

    def template_data(tpl):
        return env.from_string(tpl).module_vars['__ansible_facts__']


# Generated at 2022-06-22 12:08:41.992465
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(["a"]) == "a"
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == "123"
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, [3]]) == [1, 2, [3]]
    assert ansible_native_concat([1, [2], 3]) == [1, 2, 3]
    assert ansible_native_concat([1, {'a': 2}, 3]) == [1, {"a": 2}, 3]
    assert ansible_native_concat

# Generated at 2022-06-22 12:08:53.674711
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test empty nodes
    assert ansible_native_concat([]) is None

    # test single node in nodes
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([True]) == True

    # test multiple nodes in nodes
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'

    # test nodes as generator
    assert ansible_native_concat(x for x in [1, 2]) == 12

# Generated at 2022-06-22 12:09:02.207059
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_str
    try:
        from ansible.module_utils.common.text.jinja_filters import ansible_native_concat
    except ImportError:
        ansible_native_concat = ansible_native_concat

    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1.1']) == 1.1
    assert ansible_native_concat(['{}']) == {}

    # not a very good test, but tests that ord(' ') == 32
    assert ansible_native_concat([' ']) == 32
    assert ansible

# Generated at 2022-06-22 12:09:11.514229
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat(range(5)) == [0, 1, 2, 3, 4]
    assert ansible_native_concat(reversed(range(5))) == [4, 3, 2, 1, 0]
    assert ansible_native_concat([1, '2', b'3', 4]) == '1234'
    assert ansible_native_concat(['1', '2', '3', 4]) == '1234'
    assert ansible_native_concat([1, 2, StrictUndefined(), 4]) == '12'
    assert ansible_native_concat([1, 2, StrictUndefined(), 4]) == '12'

# Generated at 2022-06-22 12:09:22.961237
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1, 2']) == '1, 2'
    assert ansible_native_concat([1, '2']) == 1
    assert ansible_native_concat(['1', 2]) == 1
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat(['1', u'2']) == '12'
    assert ansible_native_concat([u'1', '2']) == '12'
    assert ansible_native_concat([u'1', u'2']) == '12'
    assert ansible_native_concat(['1', '2.0']) == '1'
    assert ansible_native

# Generated at 2022-06-22 12:09:34.217549
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['a', 2]) == 'a2'
    assert ansible_native_concat([1, 'b']) == '1b'
    assert ansible_native_concat([1, 'b', 3]) == '1b3'
    assert ansible_native_concat([2, 3]) == 2
    assert ansible_native_concat([1, [2, 3]]) == '1[2, 3]'
    assert ansible_native_concat([1, '2', 3]) == '12'

# Generated at 2022-06-22 12:09:43.730925
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert isinstance(ansible_native_concat([1, '2', 3]), text_type)

    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'
    assert ansible_native_concat(['f', 'o', 'o', 'b', 'a', 'r', 'b', 'a', 'z']) == 'foobarbaz'

# Generated at 2022-06-22 12:10:00.937743
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """
    Unit test method to test the function ansible_native_concat
    :return:
    """
    # Bug fix: https://github.com/ansible/ansible/issues/70922
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([42, u'foo']) == '42foo'
    assert ansible_native_concat([42, 'foo']) == '42foo'
    assert ansible_native_concat([u'foo', 42]) == u'foo42'
    assert ansible_native_concat(['42', 'foo']) == '42foo'
    assert ansible_

# Generated at 2022-06-22 12:10:12.154763
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.collections import Mapping
    from jinja2 import Environment
    import tempfile

    env = Environment(extensions=['jinja2.ext.do', 'jinja2.ext.loopcontrols'])
    env.finalize = ansible_native_concat

    # simple test to test whether it can properly extract value
    # from a single node
    tmpl = env.from_string('{{ 42 }}')
    assert tmpl.render() == 42
    tmpl = env.from_string('{{ "foo" }}')
    assert tmpl.render() == "foo"

    # test the ability to parse strings with lists
    tmpl = env.from_string('{{ "[1, 2, 3]" }}')

# Generated at 2022-06-22 12:10:23.231134
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Minimal node list
    assert ansible_native_concat([]) is None

    # Single scalar node
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None]) is None

    # Multiple scalar nodes
    assert ansible_native_concat(['foo' for _ in range(10)]) == 'foofoofoofoofoofoofoofoofoofoo'

# Generated at 2022-06-22 12:10:33.976887
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    ansible_native_concat_tests = [
        (['a', 'b'], 'ab'),
        ('a', 'a'),
        ('12.5', 12.5),
        ('12', 12),
        ({'a': 'b'}, {'a': 'b'}),
        ([{'a': 'b'}, {'c': 'd'}], [{'a': 'b'}, {'c': 'd'}]),
        # AnsibleVaultEncryptedUnicode
        (AnsibleVaultEncryptedUnicode('a'), 'a'),
    ]
    for test in ansible_native_concat_tests:
        result = ansible_native_concat(test[0])

# Generated at 2022-06-22 12:10:42.298569
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    class TestSimpleValue:
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return str(self.value)

    class TestMultiValue:
        def __init__(self, values):
            self.values = values
        def __iter__(self):
            return iter(self.values)


# Generated at 2022-06-22 12:10:50.599266
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = (u'value1', u'value2', u'value3')
    actual = ansible_native_concat(nodes)
    assert actual == u'value1value2value3'

    nodes = (u'value1\nvalue2\n')
    actual = ansible_native_concat(nodes)
    assert actual == u'value1\nvalue2\n'

    nodes = (u'value1')
    actual = ansible_native_concat(nodes)
    assert actual == u'value1'

# Generated at 2022-06-22 12:11:00.766863
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1']) != '1'
    assert ansible_native_concat(['1.0']) == 1.0
    assert ansible_native_concat(['1.0']) != '1.0'
    assert ansible_native_concat(['True']) == True
    assert ansible_native_concat(['True']) != 'True'
    assert ansible_native_concat(['[1, 2, 3]']) == [1, 2, 3]