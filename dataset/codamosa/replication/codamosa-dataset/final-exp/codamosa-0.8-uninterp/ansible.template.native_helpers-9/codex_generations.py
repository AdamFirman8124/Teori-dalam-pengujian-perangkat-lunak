

# Generated at 2022-06-22 12:01:11.094328
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1, 2]) == "12"
    assert ansible_native_concat(["a", 2]) == "a2"
    assert ansible_native_concat(["a", "b"]) == "ab"
    assert ansible_native_concat(NativeJinjaText('a')) == 'a'
    assert ansible_native_concat([NativeJinjaText('a'), NativeJinjaText('b')]) == 'ab'

# Generated at 2022-06-22 12:01:18.255475
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat('abc') == 'abc'
    assert ansible_native_concat([u'a', u'b']) == 'ab'
    assert ansible_native_concat(u'abc') == 'abc'
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat([1, u'b']) == '1b'
    assert ansible_native_concat([1, b'b']) == '1b'
    assert ansible_native_concat([1, 'b']) == '1b'
    assert ansible_native_concat(['b', 1]) == 'b1'

# Generated at 2022-06-22 12:01:30.826083
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([b'foo']) == b'foo'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([u'True']) == True
    assert ansible_native_concat([u'False']) == False
    assert ansible_native_concat([[1, 2, 3, 4], u'[', u',', u',', u']']) == [1, 2, 3, 4]
    assert ansible_native_concat([u'[', u'A,', u'1,', u']']) == u'[A,1,]'

# Generated at 2022-06-22 12:01:38.937711
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([u"foo", u"bar", u"baz"]) == u'foobarbaz'
    assert ansible_native_concat([1, u"bar", u"baz"]) == u'1barbaz'
    assert ansible_native_concat([1, u"bar", u"[1, 2, 3]"]) == [1, "bar", [1, 2, 3]]
    assert ansible_native_concat([1, u"bar", u"[1, 2, 3]", u"4"]) == [1, "bar", [1, 2, 3]]

# Generated at 2022-06-22 12:01:51.565339
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Simple concat
    assert ansible_native_concat([None, '1', '2', '3']) == '123'

    # Too complex to eval, so return string
    assert ansible_native_concat([None, '1+1']) == '1+1'

    # Eval to False
    assert ansible_native_concat([None, 'False']) is False
    assert ansible_native_concat([None, '[]']) == []
    assert ansible_native_concat([None, '{}']) == {}

    # Eval to True
    assert ansible_native_concat([None, 'True']) is True

    # Eval to a number
    assert ansible_native_concat([None, '1']) == 1

    # Eval to string
    assert ansible_native_concat

# Generated at 2022-06-22 12:02:03.586074
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['{{', 'foo', '}}']) == '{{foo}}'
    assert ansible_native_concat(['{{', 'foo', '}}']) == '{{foo}}'
    assert ansible_native_concat(['{{', 'foo', '}}']) == '{{foo}}'
    assert ansible_native_concat(['{{foo', '}}']) == '{{foo}}'
    assert ansible_native_concat(['{', '{', 'foo', '}', '}']) == '{{foo}}'
    assert ansible_native_concat(['a', '{{', 'foo', '}}', 'a']) == 'a{{foo}}a'

# Generated at 2022-06-22 12:02:14.617680
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # a string
    assert ansible_native_concat(['abc']) == 'abc'
    assert ansible_native_concat(['abc', 'def']) == 'abcdef'
    assert ansible_native_concat([1, 'abc']) == 1
    assert ansible_native_concat(['abc', 1]) == 'abc1'
    # an integer
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 'abc']) == 1
    assert ansible_native_concat(['abc', 1]) == 'abc1'
    # a float
    assert ansible_native_concat([1.0]) == 1.0

# Generated at 2022-06-22 12:02:26.471213
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    class TestYaml(AnsibleBaseYAMLObject):
        pass

    # Dict
    result = ansible_native_concat([
        AnsibleMapping(dict(test='test', test2='test2')),
        AnsibleMapping(dict(test3='test3', test4='test4')),
    ])

    assert result == dict(test='test', test2='test2', test3='test3', test4='test4')

    # List

# Generated at 2022-06-22 12:02:38.099351
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['1', '2']) == 12
    assert ansible_native_concat([None, None]) == ''
    assert ansible_native_concat([None, 'a']) == 'a'
    assert ansible_native_concat([None, ['a']]) == 'a'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', ['b'], 'c']) == 'abc'

# Generated at 2022-06-22 12:02:49.210307
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check string handling
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['special']) == 'special'
    assert ansible_native_concat(['special', 'special']) == 'specialspecial'
    assert ansible_native_concat(['\n', 'foo']) == '\nfoo'

    # Check that string concatenation is not special
    x = 'x'
    x *= 1000
    assert len(x) == 1000
    assert ansible_native_concat([x, x]) == x + x

    # Check that the string is parsed with ast.literal_eval
    assert ansible_native_concat(['True']) is True
    assert ansible_native_concat(['1,2,3']) == [1, 2, 3]

# Generated at 2022-06-22 12:02:57.604411
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.collections import recursive_diff
    import textwrap

    class FakeNode(object):
        def __init__(self, value):
            self.value = value

    class FakeUndefined(object):
        def __iter__(self):
            return iter([])

    def fake_compile(val):
        if val == '':
            return []
        elif isinstance(val, list):
            return [FakeNode(v) for v in val]
        elif val == 'undefined':
            return [FakeUndefined()]
        return [FakeNode(val)]

    assert ansible_native_concat(fake_compile('a')) == 'a'
    assert ansible_native_concat(fake_compile('a')) == 'a'
    assert ansible_native

# Generated at 2022-06-22 12:03:08.480222
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class TestNode(object):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    # Test single node
    assert ansible_native_concat([TestNode(1)]) == 1
    assert ansible_native_concat([TestNode('1')]) == 1
    assert ansible_native_concat([TestNode('a')]) == 'a'
    assert ansible_native_concat([TestNode(['a', 'b', 'c'])]) == ['a', 'b', 'c']
    assert ansible_native_concat([TestNode({'a': 1})]) == {'a': 1}

    # Test multiple nodes
    assert ansible_native_concat([TestNode(1), TestNode('1')]) == 2
   

# Generated at 2022-06-22 12:03:18.060825
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    import ansible.module_utils.urls.basic

    def _test_native_type(template, expected):
        native_concat = ansible.module_utils.jinja2.functions.NativeJinjaFilters(filters={'native_concat': ansible_native_concat}, undefined=StrictUndefined)
        out = to_native(native_concat.filters['native_concat']([template]))
        assert out == expected, "out: %s, expected: %s, template: %s" % (out, expected, template)

    _test_native_type(u'{{ "foo " | string | native_concat }}', u'foo ')

# Generated at 2022-06-22 12:03:29.289883
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest
    from ansible.module_utils.common.text.converters import to_unicode

    # Test with ansible_native_concat and with ansible_native_concat | string

# Generated at 2022-06-22 12:03:40.550135
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test exception case
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '1']) == '11'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([[1]]) == [1]
    assert ansible_native_concat([[1, 2]]) == [1, 2]
    assert ansible_native_concat(['a', 'b', 'c'])

# Generated at 2022-06-22 12:03:51.794691
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:04:03.205146
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:04:12.304743
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    from jinja2 import Environment, meta
    from jinja2.nativetypes import _parse_int

    # Number
    env = Environment(extensions=['jinja2.ext.do'])
    assert ansible_native_concat(env.compile_expression('1 + 1 + {{ 2 + 3 }}', undefined_to_none=True, final=False)) == 7
    assert ansible_native_concat(env.compile_expression('1 + 1 + {{ 2 + 3 }}', undefined_to_none=True, final=True)) == 7
    assert ansible_native_concat(env.compile_expression('1 + 1 + {{ 2 + 3 }}', undefined_to_none=False, final=False)) == 7

# Generated at 2022-06-22 12:04:21.257377
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([to_text('foo')]) == 'foo'
    assert ansible_native_concat([1, to_text('foo')]) == 1
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([to_text('foo'), to_text('bar')]) == 'foobar'
    assert ansible_native_concat([[], to_text('bar')]) == 'bar'
    assert ansible_native_concat([[], '']) == ''
    assert ansible_native_concat([[], None]) == 'None'
    assert ansible_native_concat([[], 'null']) == 'null'

# Generated at 2022-06-22 12:04:31.975415
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.runtime import Context
    from jinja2.nodes import Name
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    def _make_name(name):
        return Name(name, 'load')

    def _make_raw_name(*names):
        return [_make_name(name) for name in names]

    def _make_context(*names):
        return Context({t.name: t.name for t in names})

    def _make_vault(value):
        return AnsibleVaultEncryptedUnicode(value, b'test')


# Generated at 2022-06-22 12:04:47.100691
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.text.converters import to_list, to_bool


# Generated at 2022-06-22 12:04:57.410063
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test 1:
    # Expect concat works
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'

    # Test 2:
    # Expect concat works even if list is not strings
    assert ansible_native_concat([12, 34]) == '1234'

    # Test 3:
    # Expect concat works even if list is non-strings and non-ints
    assert ansible_native_concat([12, 'bar', 34]) == '12bar34'

    # Test 4:
    # Expect concat works with generators
    assert ansible_native_concat(x for x in [12, 'bar', 34]) == '12bar34'

    # Test 5:
    # Expect concat works with generators and different delimiter

# Generated at 2022-06-22 12:05:08.550298
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.converters import container_to_text
    from ansible.module_utils.common.collections import is_sequence
    from jinja2.runtime import StrictUndefined


# Generated at 2022-06-22 12:05:21.725905
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    a = 'xenon'
    b = 'argon'
    c = 'helium'
    d = 'helium'
    e = 'helium'

    expected = u'xenon, argon, helium'
    result = ansible_native_concat([a, b, c])

    assert result == expected

    expected = '[xenon, argon, helium]'
    result = ansible_native_concat([a, b, c])

    assert result == expected

    expected = ('[{"helium": "a colorless, odorless gas" }, {"helium": "a '
                'colorless, odorless gas"}]')
   

# Generated at 2022-06-22 12:05:33.811803
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat([0, '0']) == '00'
    assert ansible_native_concat(['0', 0]) == '00'
    assert ansible_native_concat(['0', 1, 2]) == '012'
    assert ansible_native_concat(['0', '1', '2']) == '012'

    assert ansible_native_concat(['0', ['1', '2', '3']]) == '0[1, 2, 3]'
    assert ansible_native_concat(['0', ('1', '2', '3')]) == '0(1, 2, 3)'

# Generated at 2022-06-22 12:05:44.489297
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    def _do_test(input, expected_output):
        output = ansible_native_concat(input)
        assert output == expected_output

    # empty sequence
    _do_test([], None)

    # single item
    _do_test([1], 1)
    _do_test(['a'], 'a')
    _do_test(['a', 'b'], 'ab')
    _do_test([1, 'a'], '1a')
    _do_test([1, 'a', 'b'], '1ab')
    _do_test([1, 'a', 'b', 2], '1ab2')
    _do_test([1, 'a', 'b', 2, 'c'], '1ab2c')

    # generator with single item

# Generated at 2022-06-22 12:05:55.609648
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'

    # Concatenate strings
    assert ansible_native_concat(['abc', 'def']) == 'abcdef'
    assert ansible_native_concat([u'abc', u'def']) == u'abcdef'
    assert ansible_native_concat(['a', u'bc']) == u'abc'

    # Concatenate other types and strings
    assert ansible_native_concat([['foo', 'bar'], 'baz']) == ['foo', 'bar', 'baz']
    assert ansible_native_concat(['foo', ['bar', 'baz']]) == ['foo', 'bar', 'baz']
    assert ansible_native

# Generated at 2022-06-22 12:06:03.460237
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([{}]) == {}

    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ans

# Generated at 2022-06-22 12:06:08.635860
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 1, 'b', 'c']) == 'a1bc'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([1, 2, 'a', 'b', 'c']) == '12abc'



# Generated at 2022-06-22 12:06:19.151204
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """
    >>> test_ansible_native_concat()

    """
    import doctest
    from jinja2.runtime import Context
    from ansible.module_utils import basic
    from ansible.module_utils.six import PY2

    module_args = {}
    basic._ANSIBLE_ARGS = to_text(basic._ANSIBLE_ARGS)
    if PY2:
        basic.ANSIBLE_MODULE_ARGS = to_text(basic.ANSIBLE_MODULE_ARGS)
    if basic._ANSIBLE_ARGS == '{}':
        # the environment the tests run in doesn't have the required
        # information to initialize the basic._ANSIBLE_ARGS dict,
        # but that isn't required for the doctest
        basic._ANSIBLE_ARGS = basic.ANSIBLE_MODULE_

# Generated at 2022-06-22 12:06:33.510490
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Test 1: pass in a native type and verify that it is returned unmodified
    test_value = 'this is a test string'
    assert ansible_native_concat([test_value]) == test_value
    test_value = 1
    assert ansible_native_concat([test_value]) == test_value
    test_value = set([1, 2, 3])
    assert ansible_native_concat([test_value]) == test_value

    # Test 2: pass in a list of two native types and confirm they are concatenated together
    test_value_1 = 'this is a test string'
    test_value_2 = 42

# Generated at 2022-06-22 12:06:44.879244
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    '''Test function :function:`ansible_native_concat`.'''
    try:
        from ansible.parsing.yaml import objects
    except ImportError:
        objects = None

    # single node
    assert ansible_native_concat([7]) == 7
    assert ansible_native_concat(['7']) == '7'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([container_to_text('7')]) == '7'

    # multiple nodes
    assert ansible_native_concat([7, '7']) == '77'
    assert ansible_native_concat([7, '7']).__class__ is text_type
    assert ansible_native_concat([container_to_text('7'), '7'])

# Generated at 2022-06-22 12:06:52.895708
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # pylint: disable=protected-access
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['ab', 'cd']) == 'abcd'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 'aaa']) == '1aaa'
    assert ansible_native_concat([1, 2.5]) == '12.5'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['\n123', '\n456']) == '\n123\n456'

# Generated at 2022-06-22 12:07:03.635873
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import doctest
    import jinja2
    import jinja2.nativetypes

    env = jinja2.Environment()
    env.concat = ansible_native_concat

    # [(args, expect)]

# Generated at 2022-06-22 12:07:14.108956
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', None]) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([None, u'a', u'b']) == u'ab'
    assert ansible_native_concat([None, None, None]) is None
    assert ansible_native_concat([u'10']) == 10
    assert ansible_native_concat([u'True']) is True
    assert ansible_native

# Generated at 2022-06-22 12:07:23.392214
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([b'foo']) == u'foo'

    assert ansible_native_concat([b'foo', b'bar']) == u'foobar'
    assert ansible_native_concat([b'foo', 1]) == u'foo1'
    assert ansible_native_concat([1, b'bar']) == u'1bar'
    assert ansible_native_concat([1, 2]) == u'12'

    assert ansible_native_concat([1, b'2', u'3']) == u'123'
    assert ansible_native_concat([(b'foo', b'bar'), (1, 2)]) == u'foo, bar, 1, 2'

    assert ansible_native_

# Generated at 2022-06-22 12:07:30.151038
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(iter([])) == None
    assert ansible_native_concat(iter([NativeJinjaText(['a'])])) == 'a'
    assert ansible_native_concat(iter([NativeJinjaText(['a']), NativeJinjaText(['b'])])) == 'ab'
    assert ansible_native_concat(iter([NativeJinjaText(['a']), '1.0'])) == 'a1.0'
    assert ansible_native_concat(iter([NativeJinjaText(['a']), '1.0'])) != 1.0
    assert ansible_native_concat(iter([NativeJinjaText(['a']), '1'])) == 1



# Generated at 2022-06-22 12:07:41.697639
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["string1", "string2"]) == "string1string2"
    assert ansible_native_concat(["string1", "string2", "string3", "string4"]) == "string1string2string3string4"

    assert ansible_native_concat(["string1", "1"]) == "string11"
    assert ansible_native_concat(["string1", "1", "string2", "2"]) == "string11string22"

    assert ansible_native_concat([1, 2, 3, 4, 5, 6]) == "123456"
    assert ansible_native_concat(["1", 2, 3, 4, 5, 6, "7"]) == "1234567"


# Generated at 2022-06-22 12:07:52.904417
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = [
        u'{{',
        u'vault_password_file',
        u'}}',
    ]
    assert u'{{ vault_password_file }}' == ansible_native_concat(nodes)

    nodes = [
        u'foo',
        u' ',
        u'bar',
    ]
    assert u'foo bar' == ansible_native_concat(nodes)

    nodes = [
        u'',
        u'foo',
        u' ',
        u'bar',
    ]
    assert u'foo bar' == ansible_native_concat(nodes)

    nodes = [
        u'foo',
        u' ',
        u'bar',
        u'',
    ]

# Generated at 2022-06-22 12:07:59.838763
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import contextfunction, Environment, Undefined, undefined, meta

    class Undef(Undefined):
        assume_undefined = True

    # We need to monkey-patch NativeJinjaText and StrictUndefined
    # to be able to unit test them because this is not how
    # these classes are normally used.
    # See also: https://github.com/pallets/jinja/pull/1202
    def __add__(self, other):
        return self.__class__(self.data + to_text(other))

    NativeJinjaText.__add__ = __add__
    StrictUndefined.__add__ = __add__

    # We need to monkey-patch the undefined class from a
    # scope of the jinja2 module to be able to unit test
    # it because this is not how

# Generated at 2022-06-22 12:08:13.015613
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Simple test cases
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([1, 'foo']) == '1foo'
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['{', 'f', 'o', 'o', '}']) == '{foo}'
    assert ansible_native_concat(['[', 'f', 'o', 'o', ']']) == '[foo]'

# Generated at 2022-06-22 12:08:24.306678
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    err_msg = "Failed to concat %s expected %s got %s"

    # Test 1: Concatenation without literal eval
    test_input = [1, 2.0, 'test']
    expected = "12.0test"
    assert ansible_native_concat(test_input) == expected, err_msg % (test_input, expected, ansible_native_concat(test_input))

    # Test 2: Concatenation with literal eval
    test_input = ['[', 1, ']']
    expected = [1]
    assert ansible_native_concat(test_input) == expected, err_msg % (test_input, expected, ansible_native_concat(test_input))

    # Test 3: Concatenation with incorrect literal eval

# Generated at 2022-06-22 12:08:36.575915
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    node = types.GeneratorType(
        ansible_native_concat,
        ((), {}),
    )
    assert ansible_native_concat(node) is None

    node = [u'foo']
    assert ansible_native_concat(node) == u'foo'

    node = (u'foo', u'bar')
    assert ansible_native_concat(node) == u'foobar'

    node = u'foo'
    assert ansible_native_concat(node) == u'foo'

    node = u'[1, 2, 3]'
    assert ansible_native_concat(node) == [1, 2, 3]

    node = u'{1, 2, 3}'
    assert ansible_native_concat(node) == {1, 2, 3}

   

# Generated at 2022-06-22 12:08:45.018234
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(
        ['foo']
    ) == 'foo'
    assert ansible_native_concat([
        '',
        None,
        'foo',
        u'\u185f',
        []
    ]) == 'foo'
    assert ansible_native_concat([
        'foo',
        None,
        'bar',
        u'\u185f',
        [1, 2, 3],
        None,
    ]) == u'foobar'
    assert ansible_native_concat([
        '',
        None,
        'foo',
        u'\u185f',
        -1,
    ]) == -1

# Generated at 2022-06-22 12:08:56.694124
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.common.text.converters import to_text, to_native

    assert ansible_native_concat([]) == None

    assert ansible_native_concat(['foo']) == to_text('foo')
    assert ansible_native_concat([True]) == to_text('True')
    assert ansible_native_concat(['123']) == to_text('123')
    assert ansible_native_concat(['foo-123']) == to_text('foo-123')
    assert ansible_native_concat([Sequence]) == Sequence

    assert ansible_native_concat([1, '2']) == to_native(to_text('12'))
    assert ansible_native

# Generated at 2022-06-22 12:09:08.386456
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([42, 10]) == '4210'
    assert ansible_native_concat([42, 10, u'a']) == '4210a'

    # ansible_native_concat is used for expression evaluation.
    # Because some of the expressions are in the form of list[0], it is
    # important for this function to return a list as-is.
    assert ansible_native_concat([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    # If a list is returned from ansible_native_concat,
    # container_to_text should be called on the result.

# Generated at 2022-06-22 12:09:16.540247
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['abc']) == 'abc'
    assert ansible_native_concat([('1',), ('2',), ('3',)]) == '123'
    assert ansible_native_concat([1, '2', 3.0]) == '123.0'



# Generated at 2022-06-22 12:09:28.008692
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([2, 3]) == 5
    assert ansible_native_concat(['foo', 'bar']) == u'foobar'
    assert ansible_native_concat([u'\u1234', 'bar']) == u'\u1234bar'
    assert ansible_native_concat([2, 3, 4]) == u'234'
    assert ansible_native_concat(['foo', 'bar', 1]) == u'foobar1'
    assert ansible_native_concat([1, u'\u1234']) == 1
    assert ansible_native_concat(['foo', 'bar', 1, u'\u1234']) == u'foobar1\u1234'
    assert ansible_native_concat([2]) == 2
    assert ans

# Generated at 2022-06-22 12:09:38.583836
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3, 4]) == 123
    assert ansible_native_concat([1, " 2", 3, 4]) is None
    assert ansible_native_concat(["str1", "str2", 3, 4]) == "str1str23"
    assert ansible_native_concat(["str1", " str2", " str3", " str4"]) == "str1 str2 str3"
    assert ansible_native_concat(["{'key': 'value'}", "str2", " str3", " str4"]) == "{'key': 'value'}str2"
    assert ansible_native_concat(["[1, 2, 3]", "str2", " str3", " str4"]) == "[1, 2, 3]str2"

# Generated at 2022-06-22 12:09:47.049728
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    list_of_ints = [1, 2, 3]
    list_of_mixed_types = [1, "this is a jinja2 string", 3]
    list_of_texts = [u'content', u'file']
    list_of_decrypted_vaults = [u'foobar', u'baz']
    list_of_vaults = [AnsibleVaultEncryptedUnicode(u'foobar'), AnsibleVaultEncryptedUnicode(u'baz')]
    list_of_mixed_dicts = [{u'key1': u'value1'}, {u'key2': u'value2'}]

# Generated at 2022-06-22 12:10:00.606607
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    native_types = (
        1,
        1.1,
        u'foo',
        b'foo',
        True,
        False,
    )

    # string and native types
    for first in native_types:
        yield _test_ansible_native_concat, first, native_types

    # generator
    def gen():
        for x in native_types:
            yield x
    yield _test_ansible_native_concat, gen(), native_types



# Generated at 2022-06-22 12:10:11.855080
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:22.255794
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None == ansible_native_concat([])
    assert None == ansible_native_concat([None])
    assert "abc" == ansible_native_concat(["abc"])
    assert "\n" == ansible_native_concat(["\n"])
    assert "abc" == ansible_native_concat(["a", "b", "c"])
    assert "a\nb\nc" == ansible_native_concat(["a", "\n", "b", "\n", "c"])
    assert 666 == ansible_native_concat(["666"])
    assert 666 == ansible_native_concat(["6", "6", "6"])
    assert 666 == ansible_native_concat([666])

# Generated at 2022-06-22 12:10:33.609300
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_unicode
    from jinja2.sandbox import ImmutableSandboxedEnvironment
    from jinja2.exceptions import UndefinedError
    env = ImmutableSandboxedEnvironment()
    assert ansible_native_concat(env.compile_expression('"Hello" | string')) == 'Hello'
    assert ansible_native_concat(env.compile_expression('"Hello" "World" | string')) == 'Hello' + ' ' + 'World'
    assert ansible_native_concat(env.compile_expression('"Hello" | to_yaml')) == 'Hello'
    assert ansible_native_concat(env.compile_expression('True | to_yaml')) == 'true'
    assert ansible_

# Generated at 2022-06-22 12:10:41.892295
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Evaluate to a boolean

    assert ansible_native_concat([True, False]) is True
    assert ansible_native_concat([True, True]) is True
    assert ansible_native_concat([False, False]) is False
    assert ansible_native_concat([False, True]) is True
    assert ansible_native_concat([True, u'cat']) is True
    assert ansible_native_concat([False, u'cat']) is False
    assert ansible_native_concat([u'cat', True]) is True
    assert ansible_native_concat([u'cat', False]) is False

    # Evaluate to an integer

    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat([u'1', 2]) == 3
   

# Generated at 2022-06-22 12:10:53.550176
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat([1, 2, '3']) == '123'
    assert ansible_native_concat([1, None, 3]) == '13'
    assert ansible_native_concat([1, None, '3']) == '13'
    assert ansible_native_concat([1, '', 3]) == '13'
    assert ansible_native_concat([1, '\n', 3]) == '1\n3'

# Generated at 2022-06-22 12:11:05.809847
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Debatable cases
    assert ansible_native_concat(None) is None
    assert ansible_native_concat([]) is None
    assert ansible_native_concat('') is None
    assert ansible_native_concat(123) == 123
    assert ansible_native_concat(True)
    assert ansible_native_concat(False) is False
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat(['1', 2]) == '12'
