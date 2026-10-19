

# Generated at 2022-06-13 16:46:47.232463
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    from ansible.module_utils.six import binary_type, text_type
    import jinja2

    display = Display()

    display.deprecated('DEPRECATED TEST', '2.13', collection_name='ansible.builtin')

    assert isinstance('unsafe', AnsibleUnsafeText)
    assert isinstance(b'unsafe', AnsibleUnsafeBytes)

    assert isinstance(wrap_var('unsafe'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'unsafe'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(NativeJinjaUnsafeText(text_type('unsafe'))), NativeJinjaUnsafeText)


# Generated at 2022-06-13 16:46:57.784139
# Unit test for function wrap_var
def test_wrap_var():
    import operator
    class foobar(object):
        pass

    for value in [
        123,
        123.0,
        True,
        False,
        None,
        'unsafe_str',
        b'unsafe_bytes',
        AnsibleUnsafeBytes(b'AnsibleUnsafeBytes'),
        AnsibleUnsafeText(u'AnsibleUnsafeText'),
        foobar,
    ]:
        assert wrap_var(value) is value

    # Test a tuple
    test_tuple = ('a', 'b')
    test_tuple_w = wrap_var(test_tuple)
    assert operator.isSequenceType(test_tuple_w) and not isinstance(test_tuple_w, typing.Mapping)

# Generated at 2022-06-13 16:47:08.226182
# Unit test for function wrap_var
def test_wrap_var():
    assert type(wrap_var(None)) == type(None)
    assert type(wrap_var('foo')) == AnsibleUnsafeText
    assert type(wrap_var(b'foo')) == AnsibleUnsafeBytes
    assert type(wrap_var({'foo': 'bar'})) == dict
    assert type(wrap_var({'foo': b'bar'})['foo']) == AnsibleUnsafeBytes
    assert type(wrap_var({'foo': 'bar', 'baz': b'qux'})['baz']) == AnsibleUnsafeBytes
    assert type(wrap_var(['foo', b'bar'])) == list
    assert type(wrap_var({'foo': ['foobar', b'barbaz']})['foo']) == list

# Generated at 2022-06-13 16:47:13.587973
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.utils.unsafe_proxy import _wrap_sequence
    from ansible.utils.unsafe_proxy import _wrap_dict
    from ansible.utils.unsafe_proxy import _wrap_set

    assert wrap_var(None) is None
    a = wrap_var(b"foo")
    assert isinstance(a, AnsibleUnsafeBytes)
    a = wrap_var(u"foo")
    assert isinstance(a, AnsibleUnsafeText)
    a = wrap_var(b"foo")
    assert isinstance(a, AnsibleUnsafeBytes)
    a = wrap_var([b"foo", u"bar"])
    assert isinstance(a, list)
    assert isinstance(a[0], AnsibleUnsafeBytes)


# Generated at 2022-06-13 16:47:22.211794
# Unit test for function wrap_var
def test_wrap_var():
    # Testing for strings
    assert isinstance(wrap_var('hello'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'hello'), AnsibleUnsafeBytes)

    # Testing for dict
    data = dict(foo='bar', baz='qux')

    wrap_data = wrap_var(data)
    assert isinstance(wrap_data['foo'], AnsibleUnsafeText)
    assert isinstance(wrap_data['baz'], AnsibleUnsafeText)

    # Testing for list
    data = ['hello world', b'foo bar', 'baz qux']

    wrap_data = wrap_var(data)
    assert isinstance(wrap_data[0], AnsibleUnsafeText)
    assert isinstance(wrap_data[1], AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:47:31.849932
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import string_types
    import collections
    import jinja2
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(True), type(True))
    assert isinstance(wrap_var(False), type(False))
    assert isinstance(wrap_var(1), type(1))
    assert isinstance(wrap_var(1.0), type(1.0))
    assert isinstance(wrap_var(""), string_types)
    assert isinstance(wrap_var(""), AnsibleUnsafeText)
    assert isinstance(wrap_var("a\x00b"), string_types)
    assert isinstance(wrap_var("a\x00b"), AnsibleUnsafeText)

# Generated at 2022-06-13 16:47:43.404746
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var
    # Test dict
    assert wrap_var({'a': 'b'}) == {to_unsafe_text('a'): to_unsafe_text('b')}, "wrap_var failed on dict"
    # Test list
    assert wrap_var(['a', 'b']) == [to_unsafe_text('a'), to_unsafe_text('b')], "wrap_var failed on list"
    # Test tuple
    assert wrap_var(('a', 'b')) == (to_unsafe_text('a'), to_unsafe_text('b')), "wrap_var failed on tuple"
    # Test set

# Generated at 2022-06-13 16:47:54.322633
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils import basic
    import json

    complex_data = {
        'unicode': u'\u2713',
        'list': [1, 2, 3, {'a': 1, 'b': 2}],
        'tuple': (4, 5, 6, [7, {'tuple': 'tuple'}]),
        'dict': {'k1': 'v1', 'k2': (1, 2, 3)},
        'int': 1,
        'float': 1.1,
        'None': None,
        'bool': True,
        'set': set([1, 2, 3]),
    }
    unsafe_data = wrap_var(complex_data)


# Generated at 2022-06-13 16:48:03.490136
# Unit test for function wrap_var
def test_wrap_var():
    import collections
    import copy

    class Dummy(str):
        pass

    assert (wrap_var(None) is None)
    assert (wrap_var(True) is True)
    assert (wrap_var(False) is False)
    assert (wrap_var(0) == 0)
    assert (wrap_var(1) == 1)
    assert (wrap_var(0.5) == 0.5)
    assert (wrap_var(float('nan')) == float('nan'))
    assert (wrap_var(float('inf')) == float('inf'))
    assert (wrap_var(float('-inf')) == float('-inf'))
    assert (wrap_var(u'foo') == AnsibleUnsafeText(u'foo'))

# Generated at 2022-06-13 16:48:09.293276
# Unit test for function wrap_var
def test_wrap_var():
    # Start with testing the base type
    assert type(wrap_var(True)) == bool
    assert type(wrap_var(False)) == bool
    assert type(wrap_var(1)) == int
    assert type(wrap_var(1.0)) == float
    assert type(wrap_var(b'1.0')) == AnsibleUnsafeBytes
    assert type(wrap_var(u'1.0')) == AnsibleUnsafeText

    # Test list/set/tuple type
    assert type(wrap_var([1, 2, 3])) == list
    assert type(wrap_var((1, 2, 3))) == tuple
    assert type(wrap_var({1, 2, 3})) == set
    assert type(wrap_var('123')) == AnsibleUnsafeText

    # Test dict type

# Generated at 2022-06-13 16:48:24.558363
# Unit test for function wrap_var
def test_wrap_var():
    # A basic test that we at least get to the expected types
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var([]), list)
    assert isinstance(wrap_var({}), dict)
    assert isinstance(wrap_var('abc'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'abc'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'abc'), AnsibleUnsafeBytes)

    # Test that routine returns AnsibleUnsafe when given as input
    assert isinstance(wrap_var(AnsibleUnsafeText('abc')), AnsibleUnsafeText)
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'abc')), AnsibleUnsafeBytes)

    # Test that deep recursion is safe
    assert wrap_var

# Generated at 2022-06-13 16:48:34.131174
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(u"unicode string"), AnsibleUnsafeText)
    assert isinstance(wrap_var(b"byte string"), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("bytestring-auto-decoded"), AnsibleUnsafeText)
    assert isinstance(wrap_var(dict(name="value")), dict)
    assert isinstance(wrap_var(list(("value", "value2"))), list)
    assert isinstance(wrap_var(("value", "value2")), tuple)
    assert isinstance(wrap_var(set(("value", "value2"))), set)
    assert isinstance(wrap_var(NativeJinjaText(u"text")), NativeJinjaUnsafeText)


# Generated at 2022-06-13 16:48:44.198153
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.module_utils.common.collections
    from ansible.module_utils.six import string_types

    # Test string_types
    assert wrap_var("") is not ""
    assert wrap_var("") is not b""
    assert wrap_var("") == u""
    assert wrap_var("") == b""
    assert wrap_var("abc") is not "abc"
    assert wrap_var("abc") is not b"abc"
    assert wrap_var("abc") == u"abc"
    assert wrap_var("abc") == b"abc"
    assert wrap_var(u"") is not ""
    assert wrap_var(u"") is not b""
    assert wrap_var(u"") == u""
    assert wrap_var(u"") == b""

# Generated at 2022-06-13 16:48:54.729974
# Unit test for function wrap_var
def test_wrap_var():
    # Test None
    assert wrap_var(None) is None

    # Test string
    assert wrap_var("abc") == "abc"
    assert isinstance(wrap_var("abc"), AnsibleUnsafeText)

    # Test tuple
    assert wrap_var(("a", "b")) == ("a", "b")
    assert isinstance(wrap_var(("a", "b")), tuple)
    assert isinstance(wrap_var(("a", "b"))[0], AnsibleUnsafeText)

    # Test list
    assert wrap_var(["a", "b"]) == ["a", "b"]
    assert isinstance(wrap_var(["a", "b"]), list)
    assert isinstance(wrap_var(["a", "b"])[0], AnsibleUnsafeText)

    # Test set
    assert wrap

# Generated at 2022-06-13 16:49:01.898474
# Unit test for function wrap_var
def test_wrap_var():
    import json

    def assertEqual(lhs, rhs):
        if lhs != rhs:
            raise AssertionError('%s != %s' % (lhs, rhs))

    # Test UnsafeProxy with various strings
    assertEqual(type(UnsafeProxy('foo')), AnsibleUnsafeText)
    assertEqual(type(UnsafeProxy(b'foo')), AnsibleUnsafeBytes)
    assertEqual(type(UnsafeProxy(u'foo')), AnsibleUnsafeText)
    assertEqual(type(UnsafeProxy(r'foo')), AnsibleUnsafeText)
    assertEqual(type(UnsafeProxy(repr(r'foo'))), AnsibleUnsafeText)

# Generated at 2022-06-13 16:49:12.428128
# Unit test for function wrap_var
def test_wrap_var():
    """ Unit test for function wrap_var """
    import ansible.utils.unsafe_proxy

    # Test a simple string
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var("Hello World"), ansible.utils.unsafe_proxy.AnsibleUnsafeText)

    # Test a simple dictionary
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var({"Hello": "World"}), dict)

    # Test a simple list
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var(["Hello", "World"]), list)

    # Test a simple set
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var({"Hello", "World"}), set)

    # Test a NativeJinjaText type

# Generated at 2022-06-13 16:49:20.985706
# Unit test for function wrap_var
def test_wrap_var():
    import types
    import inspect

    def _check_proxy(v):
        return inspect.isclass(v) and issubclass(v, AnsibleUnsafe)

    assert _check_proxy(wrap_var(None))
    assert _check_proxy(wrap_var(1))
    assert _check_proxy(wrap_var(1.2))
    assert _check_proxy(wrap_var({}))
    assert _check_proxy(wrap_var({1: 2}))
    assert _check_proxy(wrap_var({'a': 2}))
    assert _check_proxy(wrap_var(set()))
    assert _check_proxy(wrap_var([1, 2, 3]))
    assert _check_proxy(wrap_var((lambda: 1, 2)))

# Generated at 2022-06-13 16:49:31.872568
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import StringIO, StringIO
    import sys

    import pytest
    from pytest import raises

    from ansible.module_utils.six.moves import StringIO
    import ansible.module_utils.basic

    # ansible.module_utils.basic.AnsibleModule calls basic.get_exception, which calls wrap_var
    # Unit test to capture exception tracebacks
    testargs = ['ansible/modules/system/test_template.py', 'foo=bar']
    st = StringIO()


# Generated at 2022-06-13 16:49:40.895016
# Unit test for function wrap_var
def test_wrap_var():
    '''
    Test function wrap_var using assert
    '''

    assert wrap_var(None) is None
    assert wrap_var(True) == True
    assert wrap_var(False) == False
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0

    assert wrap_var(b'foo') == AnsibleUnsafeBytes(b'foo')
    assert wrap_var('foo') == AnsibleUnsafeText('foo')

    assert wrap_var(tuple((1, 2, 3))) == (1, 2, 3)
    assert wrap_var([1, 2, 3]) == [1, 2, 3]

    assert wrap_var(set((1, 2, 3))) == set((1, 2, 3))

# Generated at 2022-06-13 16:49:49.468869
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var({'foo': 'bar'}), dict)
    assert isinstance(wrap_var([b'foo', 'bar']), list)
    assert isinstance(wrap_var((b'foo', 'bar')), tuple)
    assert isinstance(wrap_var(set([b'foo', 'bar'])), set)