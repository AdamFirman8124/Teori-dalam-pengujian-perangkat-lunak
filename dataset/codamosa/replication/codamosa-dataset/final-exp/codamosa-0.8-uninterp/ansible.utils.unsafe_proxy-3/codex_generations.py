

# Generated at 2022-06-13 16:46:37.526845
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import iteritems
    from ansible.utils.unsafe_proxy import wrap_var, to_bytes, to_text
    import sys
    # Create some unicode strings
    unicode_foo = u'\u00F6'
    bytes_foo = unicode_foo.encode('utf-8')
    unsafe_foo = AnsibleUnsafeText(unicode_foo)

    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(wrap_var(None)), type(None))
    assert isinstance(wrap_var(unicode_foo), AnsibleUnsafeText)
    assert isinstance(wrap_var(wrap_var(unicode_foo)), AnsibleUnsafeText)

# Generated at 2022-06-13 16:46:48.129552
# Unit test for function wrap_var
def test_wrap_var():
    import json
    import ansible.plugins.loader
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six import text_type, binary_type
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils import basic

    def assert_unsafe(obj):
        assert isinstance(obj, AnsibleUnsafe), '%s is not an AnsibleUnsafe' % (obj)
        return obj

    # basic types
    assert_unsafe(wrap_var(None))
    assert_unsafe(wrap_var(1))
    assert_unsafe(wrap_var(1.0))
    # text_type
    assert_unsafe(wrap_var(u'foobar'))

# Generated at 2022-06-13 16:46:54.572680
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # string type test
    assert isinstance(UnsafeProxy(str()), AnsibleUnsafeText)
    assert isinstance(UnsafeProxy(b''), AnsibleUnsafeBytes)
    # Unsafe Type test
    assert isinstance(UnsafeProxy(AnsibleUnsafeText(str())), AnsibleUnsafeText)
    assert isinstance(UnsafeProxy(AnsibleUnsafeBytes(b'')), AnsibleUnsafeBytes)
    assert isinstance(UnsafeProxy(AnsibleUnsafeText(b'')), AnsibleUnsafeText)
    assert isinstance(UnsafeProxy(AnsibleUnsafeBytes(str())), AnsibleUnsafeBytes)
    # Mapping type test
    assert isinstance(UnsafeProxy({}), dict)
    # Sequence type test
    assert isinstance(UnsafeProxy([]), list)

# Generated at 2022-06-13 16:46:59.482456
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    assert isinstance(UnsafeProxy(b"abc"), binary_type)
    assert isinstance(UnsafeProxy(u"abc"), text_type)
    assert isinstance(UnsafeProxy(b"abc"), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(u"abc"), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(b"abc").encode('ascii'), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(u"abc").decode('ascii'), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(b"abc").encode(), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(u"abc").decode(), AnsibleUnsafe)

# Generated at 2022-06-13 16:47:08.282043
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.parsing.plugin_docs import read_docstring, unquote
    import os, re
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, '../module_common.py'))
    module_common_contents = f.read()
    docstrings = read_docstring(module_common_contents)
    args = re.findall('\[(.*?)\]', docstrings['DOCUMENTATION']['options'])

    for i in args:
        input_val = "parameter_{0}".format(i)
        output_val = unquote(input_val)

# Generated at 2022-06-13 16:47:14.393728
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.module_utils.six import PY2

    assert isinstance(UnsafeProxy("test"), AnsibleUnsafeText)
    assert isinstance(UnsafeProxy(u"test"), AnsibleUnsafeText)
    if PY2:
        assert isinstance(UnsafeProxy(b"test"), AnsibleUnsafeBytes)
    else:
        assert isinstance(UnsafeProxy(b"test"), AnsibleUnsafeText)

# Generated at 2022-06-13 16:47:18.504723
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('unicode string') == u'unicode string'
    assert wrap_var(b'byte string') == b'byte string'
    assert wrap_var(None) is None
    assert wrap_var(u'\xe9') == u'\xe9'

    assert isinstance(wrap_var(b'\xe9'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'\xe9'), AnsibleUnsafeText)
    assert isinstance(wrap_var(None), AnsibleUnsafeText)

    assert wrap_var(u'\xe9'.encode('utf-8')).encode('utf-8') == b'\xc3\xa9'
    assert wrap_var(b'\xc3\xa9'.decode('utf-8')).decode('utf-8') == u

# Generated at 2022-06-13 16:47:27.070377
# Unit test for function wrap_var
def test_wrap_var():
    # Test string, int, float
    assert wrap_var(1) == 1
    assert wrap_var('string') == 'string'
    assert wrap_var(1.0) == 1.0

    # Test dict
    assert wrap_var({'a': 'b'}) == {'a': 'b'}
    assert wrap_var({1: {2: 3}}) == {1: {2: 3}}

    # Test list
    test_list = [{'a': {'b': 'c'}}, [1, 2, 3]]
    assert wrap_var(test_list) == test_list

# Generated at 2022-06-13 16:47:36.241329
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():

    # AnsibleUnsafeBytes is unchanged
    assert type(UnsafeProxy(AnsibleUnsafeBytes(b'foo'))) is AnsibleUnsafeBytes
    assert type(UnsafeProxy(AnsibleUnsafeText('foo'))) is AnsibleUnsafeText

    # bytes is wrapped in AnsibleUnsafeBytes
    assert type(UnsafeProxy(b'foo')) is AnsibleUnsafeBytes

    # text is wrapped in AnsibleUnsafeText
    assert type(UnsafeProxy('foo')) is AnsibleUnsafeText

    # dict is wrapped recursively
    assert isinstance(UnsafeProxy({'foo': 'bar'}), dict)

    # list is wrapped recursively
    assert isinstance(UnsafeProxy(['foo', 'bar']), list)

    # stringified dict is wrapped in AnsibleUnsafeText

# Generated at 2022-06-13 16:47:40.073839
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    assert UnsafeProxy(None) is None
    assert UnsafeProxy('hello world') == 'hello world'
    assert isinstance(UnsafeProxy(None), UnsafeProxy)
    assert isinstance(UnsafeProxy('hello world'), UnsafeProxy)

# Generated at 2022-06-13 16:47:45.324728
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    unsafe = UnsafeProxy("foo")
    assert isinstance(unsafe, AnsibleUnsafeText)
    assert unsafe.__UNSAFE__
    assert unsafe == u'foo'


# Generated at 2022-06-13 16:47:55.634939
# Unit test for function wrap_var
def test_wrap_var():
    # TODO: Write tests for *all* AnsibleUnsafe functions
    # (Currently we only test for the AnsibleUnsafeText class and don't have
    # coverage for the others)
    from ansible.module_utils.six import text_type

    assert isinstance(wrap_var("_unicode_"), text_type)
    assert isinstance(wrap_var(b"_bytes_"), binary_type)
    assert isinstance(wrap_var(u"_unicode_"), text_type)
    assert isinstance(wrap_var(AnsibleUnsafeText("_unicode_")), text_type)
    assert isinstance(wrap_var(AnsibleUnsafeBytes("_bytes_")), binary_type)

    assert isinstance(wrap_var("_unicode_").encode("utf-8"), binary_type)


# Generated at 2022-06-13 16:48:04.321460
# Unit test for function wrap_var
def test_wrap_var():
    import json
    import yaml
    from ansible.module_utils.common._collections_compat import OrderedDict

    s = u'你好'
    s_u = wrap_var(s)
    assert isinstance(s_u, AnsibleUnsafeText)

    b = s.encode('utf-8')
    b_u = wrap_var(b)
    assert isinstance(b_u, AnsibleUnsafeBytes)

    d = {'a': 1, 'b': 'hello world', 'c': [1, 2, 3]}
    d_u = wrap_var(d)
    assert isinstance(d_u, dict)
    assert isinstance(d_u['b'], AnsibleUnsafeText)
    assert isinstance(d_u['c'], list)


# Generated at 2022-06-13 16:48:13.493388
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cStringIO as StringIO

    if PY3:
        from io import StringIO

    for data in [
        'abc',
        u'abc',
        to_bytes('abc'),
        to_text(b'abc'),
        ['abc', 'def'],
        dict(a=1, b=2, c=3),
    ]:
        proxy_data = UnsafeProxy(data)
        assert type(proxy_data) is AnsibleUnsafeText
        assert isinstance(proxy_data, AnsibleUnsafe)
        if isinstance(data, dict):
            assert dict(proxy_data) == {'a': '1', 'b': '2', 'c': '3'}

# Generated at 2022-06-13 16:48:24.963534
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():

    from ansible.module_utils.six import PY2
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils.common.collections import is_sequence

    assert isinstance(UnsafeProxy('ascii'), AnsibleUnsafeText)

    # This is not the ideal type to check but it is the first thing that comes to mind.
    assert isinstance(UnsafeProxy(b'ascii'), AnsibleUnsafeBytes)

    # Checks that tuple, list, and set are wrapped in an unsafe container.
    assert is_sequence(UnsafeProxy(())) and not isinstance(UnsafeProxy(()), tuple)
    assert is_sequence(UnsafeProxy([])) and not isinstance(UnsafeProxy([]), list)

# Generated at 2022-06-13 16:48:34.448045
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    import sys
    from ansible.module_utils._text import to_text

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    module = AnsibleModule(argument_spec={})
    module.warn = Mock()

    class TestUnsafeProxy(unittest.TestCase):
        def test_without_arguments(self):
            proxy = UnsafeProxy()
            self.assertTrue(isinstance(proxy, UnsafeProxy))

        def test_string_conversion(self):
            text_value = "test"
            result = UnsafeProxy(text_value)
            self.assertTrue(isinstance(result, AnsibleUnsafeText))
            self.assertTrue('UNSAFE' in result.__repr__())

# Generated at 2022-06-13 16:48:44.433500
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    import sys
    import unittest
    class TestUnsafeProxy___new__(unittest.TestCase):
        def test_int(self):
            obj = UnsafeProxy(3)
            self.assertEqual(obj, 3)
            self.assertIsInstance(obj, int)

        def test_string(self):
            obj = UnsafeProxy('test')
            self.assertEqual(obj, 'test')
            self.assertIsInstance(obj, AnsibleUnsafeText)

        def test_unicode(self):
            obj = UnsafeProxy(u'test')
            self.assertEqual(obj, u'test')
            if sys.version_info[0] == 2:
                self.assertIsInstance(obj, AnsibleUnsafeText)

# Generated at 2022-06-13 16:48:54.851406
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.module_utils.common.collections import is_sequence
    from six import PY3, string_types, text_type, binary_type

    astr = b'abc'
    atext = u'abc'
    listener = [None, None]

    # try with a string
    a1 = UnsafeProxy(astr)
    assert isinstance(a1, string_types)
    assert isinstance(a1, AnsibleUnsafe)
    assert isinstance(a1, binary_type)
    assert a1 == astr

    # if we have python 3 astr and a1 are not instances of basestring as string_types
    # is a class and binary_type is not and thus for python 2 string_types will be a tuple
    # and binary_type will be part of it, for python 3 binary_type is

# Generated at 2022-06-13 16:49:01.917773
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    display = Display()
    from ansible.module_utils.six import text_type
    import collections
    import sys

    s = 'test'
    assert isinstance(s, text_type), 'This is a text string'
    bs = wrap_var(s)
    assert isinstance(bs, AnsibleUnsafeText), 'AnsibleUnsafeText is not the same as text_type'
    assert type(bs) == type(s), 'Wrap AnsibleUnsafeText has the same type'
    assert bs == 'test', 'Wrap AnsibleUnsafeText has the same content'
    assert s == bs, 'AnsibleUnsafeText(AnsibleUnsafeText) is equal to AnsibleUnsafeText'

    s = u'test'

# Generated at 2022-06-13 16:49:12.430210
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3
    if PY3:
        import types
        orig_wrap_var = types.FunctionType(wrap_var.__code__, wrap_var.__globals__, name='wrap_var',
                                           argdefs=wrap_var.__defaults__, closure=wrap_var.__closure__)
    else:
        orig_wrap_var = wrap_var

    def test_wrap_var(value, expected):
        assert orig_wrap_var(value) == expected, "wrap_var({0}) failed".format(repr(value))

    test_wrap_var(1, 1)
    test_wrap_var(set(), set())
    test_wrap_var({}, {})
    test_wrap_var([], [])
    test_wrap_

# Generated at 2022-06-13 16:49:22.500097
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    if PY3:
        unicode = str
    else:
        import __builtin__ as builtins

    assert isinstance(wrap_var("some string"), AnsibleUnsafeText)
    assert isinstance(wrap_var(u"some string"), AnsibleUnsafeText)
    assert isinstance(wrap_var(AnsibleUnsafeText("some string")), AnsibleUnsafeText)
    assert isinstance(wrap_var(AnsibleUnsafeBytes("some string")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(dict({"some": "string"})), dict)

# Generated at 2022-06-13 16:49:33.092621
# Unit test for function wrap_var
def test_wrap_var():
    import sys

    assert wrap_var('foo') == AnsibleUnsafeText('foo')
    assert wrap_var(b'foo') == AnsibleUnsafeBytes(b'foo')
    assert wrap_var(AnsibleUnsafeText('foo')) == AnsibleUnsafeText('foo')
    assert wrap_var(AnsibleUnsafeBytes(b'foo')) == AnsibleUnsafeBytes(b'foo')
    assert wrap_var(['foo', 'bar']) == AnsibleUnsafeText('foo,bar')
    assert wrap_var(('foo', 'bar')) == AnsibleUnsafeText('foo,bar')
    assert wrap_var({'foo': 'bar'}) == AnsibleUnsafeText('foo=bar')
    assert wrap_var(dict(((1, 'foo'), (2, 'bar')))) == Ansible

# Generated at 2022-06-13 16:49:41.405125
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) == None
    assert wrap_var(True) == True
    assert wrap_var(False) == False
    assert wrap_var(4) == 4
    assert wrap_var(4.1) == 4.1
    assert wrap_var({"a": 1}) == {'a': 1}
    assert wrap_var(["a", 1]) == ['a', 1]
    assert wrap_var(("a", 1)) == ('a', 1)
    assert wrap_var({'a': 1, 'c': 3, 'b': 2}) == {'a': 1, 'c': 3, 'b': 2}
    assert isinstance(wrap_var({"a": 1}), dict)
    assert isinstance(wrap_var(["a", 1]), list)

# Generated at 2022-06-13 16:49:51.924713
# Unit test for function wrap_var
def test_wrap_var():
    assert (isinstance(wrap_var(None), type(None)))
    assert (isinstance(wrap_var(123), int))
    assert (isinstance(wrap_var(123.1), float))
    assert (isinstance(wrap_var('str'), AnsibleUnsafeText))
    assert (isinstance(wrap_var(u'unicode'), AnsibleUnsafeText))
    assert (isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes))
    assert (isinstance(wrap_var(b'bytes'.decode('utf-8')), AnsibleUnsafeText))
    assert (isinstance(wrap_var([1,2,3]), list))
    assert (isinstance(wrap_var((1,2,3)), tuple))
    assert (isinstance(wrap_var({1:2}), dict))

# Generated at 2022-06-13 16:50:03.431434
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(u"foo") == u"foo"
    assert isinstance(wrap_var(u"foo"), AnsibleUnsafeText)
    assert wrap_var(b"foo") == b"foo"
    assert isinstance(wrap_var(b"foo"), AnsibleUnsafeBytes)
    assert wrap_var(None) is None
    assert isinstance(wrap_var(None), type(None))
    assert wrap_var(u"foo".encode("utf-8")) == u"foo".encode("utf-8")
    assert wrap_var(u"foo".encode("utf-8")) == u"foo".encode("utf-8")
    assert isinstance(wrap_var(u"foo".encode("utf-8")), AnsibleUnsafeBytes)
    assert wrap_var(b"foo") == b

# Generated at 2022-06-13 16:50:09.543471
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(b'hello') == b'hello'
    assert wrap_var(u'hello') == u'hello'
    assert wrap_var(b'\x00') == b'\x00'
    assert wrap_var(u'\x00') == u'\x00'
    assert wrap_var({b'k': b'v'}) == {b'k': b'v'}
    assert wrap_var({u'k': u'v'}) == {u'k': u'v'}
    assert wrap_var((b'k', b'v')) == (b'k', b'v')
    assert wrap_var((u'k', u'v')) == (u'k', u'v')

# Generated at 2022-06-13 16:50:17.282377
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_sequence

    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var("abc"), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_bytes("xyz")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(7), int)
    assert isinstance(wrap_var(7.0), float)
    assert isinstance(wrap_var(["a", "b"]), list)
    assert is_sequence(wrap_var("s"))
    assert isinstance(wrap_var("s"), AnsibleUnsafeText)
    assert isinstance(wrap_var(("a", "b")), tuple)

# Generated at 2022-06-13 16:50:23.142969
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var('abcd'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'abcd'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'abcd'), AnsibleUnsafeBytes)

    assert isinstance(wrap_var(u'abcd'.encode('utf-8')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(b'abcd'.decode('utf-8')), AnsibleUnsafeText)

    assert isinstance(wrap_var({'b': 'asdf', u'b': u'asdf'}), dict)
    assert isinstance(wrap_var({'b': 'asdf', u'b': u'asdf'})['b'], AnsibleUnsafeText)

# Generated at 2022-06-13 16:50:32.237186
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import list_of_sets

    from ansible.utils.unsafe_proxy import (
        wrap_var,
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_bytes,
        to_unsafe_text,
    )

    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'unicode'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'.decode()), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'unicode'.encode()), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(1), AnsibleUnsafe)

# Generated at 2022-06-13 16:50:41.233962
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('abc') == u'abc'
    assert isinstance(wrap_var(u'abc'), AnsibleUnsafeText)
    assert wrap_var(u'abc') == wrap_var(u'abc')
    assert isinstance(wrap_var('abc'), AnsibleUnsafeText)
    assert wrap_var(u'abc') != wrap_var('abc')
    assert wrap_var(u'abc') == wrap_var(b'abc')
    assert wrap_var(u'abc') == wrap_var(b'abc'.decode())
    assert wrap_var([u'abc']) == [u'abc']
    assert isinstance(wrap_var([u'abc']), list)
    assert wrap_var([u'abc']) == wrap_var([u'abc'])

# Generated at 2022-06-13 16:50:54.454078
# Unit test for function wrap_var
def test_wrap_var():

    # Dict and List
    data = {
        'some_dict': {
            'some_value': 'some_value',
            'some_key': 'some_key',
            'some_sequence': [
                'some_value',
                'some_value2'
            ]
        },
        'some_list': [
            'some_value',
            'some_value2'
        ]
    }

    assert isinstance(data['some_dict']['some_value'], str)
    assert isinstance(data['some_dict']['some_key'], str)
    assert isinstance(data['some_dict']['some_sequence'], list)
    assert isinstance(data['some_dict']['some_sequence'][0], str)

# Generated at 2022-06-13 16:50:59.791293
# Unit test for function wrap_var
def test_wrap_var():
    # Mapping Types
    assert isinstance(wrap_var({'A':'hello'}), dict)
    assert isinstance(wrap_var({'A':'hello'})['A'], AnsibleUnsafeText)
    assert isinstance(wrap_var({'A': AnsibleUnsafeText('hello')}), dict)
    assert isinstance(wrap_var({'A': AnsibleUnsafeText('hello')})['A'], AnsibleUnsafeText)

    # Sequence Types
    assert isinstance(wrap_var(['A', 'hello']), list)
    assert isinstance(wrap_var(['A', 'hello'])[1], AnsibleUnsafeText)
    assert isinstance(wrap_var((('A'), ('hello'))), tuple)

# Generated at 2022-06-13 16:51:06.353985
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import text_type, PY3
    from ansible.module_utils.six.moves import UserDict
    if PY3:
        int_types = (int,)
    else:
        int_types = (int, long)

# Generated at 2022-06-13 16:51:14.434538
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_sequence

    class DummyObject(object):
        def __repr__(self):
            return '<DummyObject>'

    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(DummyObject()), AnsibleUnsafe)
    assert isinstance(wrap_var('Hello World!'), text_type)
    assert isinstance(wrap_var(to_bytes('Hello World!')), binary_type)

    # Ensure wrap_var() is idempotent
    assert wrap_var(wrap_var(wrap_var(wrap_var('Hello World!')))) == wrap_var(wrap_var('Hello World!'))

    # Ensure wrap_var()

# Generated at 2022-06-13 16:51:23.410162
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import list_of_unique_strings
    class X: pass
    x = X()
    result = wrap_var(x)
    assert id(result) == id(x)
    assert result is x

    result = wrap_var([None])
    assert isinstance(result, list)
    assert result == [None]

    result = wrap_var((None,))
    assert isinstance(result, tuple)
    assert result == (None,)

    result = wrap_var('\x00')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'\x00'

    result = wrap_var(u'\u0000')
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'\u0000'

    result = wrap

# Generated at 2022-06-13 16:51:34.222995
# Unit test for function wrap_var
def test_wrap_var():
    import pytest

    # Test from pytest_ansible_targets.targets.wrap_var
    assert wrap_var(None) is None

    v = wrap_var('hello')
    assert isinstance(v, AnsibleUnsafeText)

    v = AnsibleUnsafeText('hello')
    assert wrap_var(v) is v

    assert wrap_var(b'hello') is b'hello'

    v = wrap_var(set([1, 2, 3]))
    assert isinstance(v, set)
    assert isinstance(v.pop(), AnsibleUnsafeText)

    v = wrap_var(list([1, 2, 3]))
    assert isinstance(v, list)
    assert isinstance(v[0], AnsibleUnsafeText)


# Generated at 2022-06-13 16:51:41.521564
# Unit test for function wrap_var
def test_wrap_var():
    # Create a test object that has some methods to verify that they
    # also get wrapped.
    class TestClass(object):
        def method(self):
            return "method_return_value"
        @property
        def str(self):
            return "property_return_value"
        @staticmethod
        def staticmethod():
            return "staticmethod_return_value"

    # Create a data structure to test wrapping

# Generated at 2022-06-13 16:51:49.821743
# Unit test for function wrap_var
def test_wrap_var():
    # Basic types
    assert wrap_var(None) is None
    assert wrap_var(False) is False
    assert wrap_var(True) is True
    assert wrap_var(0) == 0
    assert wrap_var(b'abc') == to_unsafe_bytes('abc')
    assert wrap_var(u'abc') == to_unsafe_text('abc')
    assert wrap_var(u'\x00') == to_unsafe_text('\x00')

    # NativeJinjaText
    assert wrap_var(NativeJinjaText(u'abc')) == NativeJinjaUnsafeText(u'abc')
    assert wrap_var(NativeJinjaText(u'\x00')) == NativeJinjaUnsafeText(u'\x00')

# Generated at 2022-06-13 16:51:59.833758
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    v1 = AnsibleUnsafeBytes(b'abc')
    assert wrap_var(v1) is v1
    v2 = AnsibleUnsafeText(u'def')
    assert wrap_var(v2) is v2
    for v3 in [u'def', b'def']:
        v3 = wrap_var(v3)
        assert isinstance(v3, AnsibleUnsafeText)
        assert v3 == u'def'
        v4 = wrap_var(v3)
        assert isinstance(v4, AnsibleUnsafeText)
        assert v4 == u'def'

# Generated at 2022-06-13 16:52:07.780592
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3

    # Test wrap_var for Sequences
    input_variable = [b"b_val1", b"b_val2"]
    expected_variable = [AnsibleUnsafeBytes(b'b_val1'), AnsibleUnsafeBytes(b'b_val2')]
    returned_variable = wrap_var(input_variable)
    assert(isinstance(returned_variable, type(input_variable)))
    assert(expected_variable == returned_variable)

    input_variable = [u"u_val1", u"u_val2"]
    expected_variable = [AnsibleUnsafeText(u'u_val1'), AnsibleUnsafeText(u'u_val2')]
    returned_variable = wrap_var(input_variable)