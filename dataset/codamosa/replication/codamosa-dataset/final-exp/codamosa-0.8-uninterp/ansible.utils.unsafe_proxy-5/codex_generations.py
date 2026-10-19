

# Generated at 2022-06-13 16:46:47.377032
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(to_unsafe_text('foo'), AnsibleUnsafeText)
    assert isinstance(to_unsafe_bytes(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(dict(foo=b'foo')), dict)
    assert isinstance(wrap_var(dict(foo=b'foo'))['foo'], AnsibleUnsafeBytes)
    assert isinstance(wrap_var([b'foo']), list)
    assert isinstance(wrap_var([b'foo'])[0], AnsibleUnsafeBytes)
    assert isinstance(wrap_var(tuple([b'foo'])), tuple)

# Generated at 2022-06-13 16:46:54.045987
# Unit test for function wrap_var
def test_wrap_var():
    import pytest
    from ansible.module_utils.six import unichr

    def assert_type_matches(v, t):
        assert type(wrap_var(v)) is t

    assert_type_matches(None, type(None))
    assert_type_matches(True, type(True))
    assert_type_matches(False, type(False))
    assert_type_matches(unichr(100), AnsibleUnsafeText)
    assert_type_matches(u"abc", AnsibleUnsafeText)
    assert_type_matches(b"abc", AnsibleUnsafeBytes)
    assert_type_matches([1, 2, 3], list)
    assert_type_matches((1, 2, 3), tuple)

# Generated at 2022-06-13 16:46:59.502368
# Unit test for function wrap_var
def test_wrap_var():

    import json
    import re
    import unittest

    # The following are the test cases:
    #   1.  Input                    f(x)                Output
    #   2.  ---------                ----                ------
    #   3.  None                     wrap_var(x)         None
    #   4.  True                     wrap_var(x)         True
    #   5.  False                    wrap_var(x)         False
    #   6.  Int                      wrap_var(x)         Int
    #   7.  Dict                     wrap_var(x)         Dict
    #   8.  List                     wrap_var(x)         List
    #   9.  Bytes                    wrap_var(x)         AnsibleUnsafeBytes
    #   10. Text                     wrap_var(x)         AnsibleUnsafeText
    #

# Generated at 2022-06-13 16:47:08.308446
# Unit test for function wrap_var
def test_wrap_var():
    import unittest
    import ansible.utils.unsafe_proxy

# Generated at 2022-06-13 16:47:19.592757
# Unit test for function wrap_var
def test_wrap_var():
    import struct

    assert wrap_var(None) is None
    assert isinstance(wrap_var(''), AnsibleUnsafeText)
    assert isinstance(wrap_var('test'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'test'), AnsibleUnsafeText)
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var(1.0), float)
    assert isinstance(wrap_var([]), list)
    assert isinstance(wrap_var([1, 2]), list)
    assert isinstance(wrap_var(tuple()), tuple)
    assert isinstance(wrap_var((1, 2)), tuple)
    assert isinstance(wrap_var(set()), set)
    assert isinstance(wrap_var({1, 2}), set)
    assert isinstance

# Generated at 2022-06-13 16:47:29.714799
# Unit test for function wrap_var
def test_wrap_var():
    import datetime
    import pytz

    # Standard string
    value = 'This is a string'
    assert isinstance(wrap_var(value), AnsibleUnsafeText)

    # Standard unicode string
    value = u'This is a unicode string'
    assert isinstance(wrap_var(value), AnsibleUnsafeText)

    # Standard byte string
    value = b'This is a byte string'
    assert isinstance(wrap_var(value), AnsibleUnsafeBytes)

    # Already unsafe byte string
    value = AnsibleUnsafeBytes(b'This is already unsafe')
    assert isinstance(wrap_var(value), AnsibleUnsafeBytes)

    # Already unsafe unicode string
    value = AnsibleUnsafeText(u'This is already unsafe')

# Generated at 2022-06-13 16:47:38.169138
# Unit test for function wrap_var
def test_wrap_var():
    import unittest

    class TestModule(unittest.TestCase):
        def test_wrap_var(self):
            unsafe_bytes = to_unsafe_bytes(b"hello")
            unsafe_text = to_unsafe_text(unsafe_bytes)
            self.assertTrue(isinstance(unsafe_bytes, AnsibleUnsafeBytes), "Unsafe bytes conversion is not working")
            self.assertTrue(isinstance(unsafe_text, AnsibleUnsafeText), "Unsafe text conversion is not working")
            self.assertTrue(isinstance(wrap_var({'a': unsafe_bytes}), AnsibleUnsafe), 'wrap_var is not working for a dictionary')
            self.assertTrue(isinstance(wrap_var(['a', unsafe_bytes]), AnsibleUnsafe), 'wrap_var is not working for a list')

# Generated at 2022-06-13 16:47:48.013441
# Unit test for function wrap_var
def test_wrap_var():
    import unittest

    class WrapVarTests(unittest.TestCase):
        def test_wrap_is_recursive(self):
            v = {
                'k1': [1, 2, 3, {'k2': 'v2'}],
                'k2': u'v2',
            }
            wrapped_v = wrap_var(v)
            self.assertIsInstance(wrapped_v, dict)
            self.assertIsInstance(wrapped_v['k1'], list)
            self.assertIsInstance(wrapped_v['k1'][3], dict)
            self.assertIsInstance(wrapped_v['k1'][3]['k2'], AnsibleUnsafeText)
            self.assertIsInstance(wrapped_v['k2'], AnsibleUnsafeText)

       

# Generated at 2022-06-13 16:47:57.242376
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3

    if PY3:
        return

    assert isinstance(wrap_var("x"), AnsibleUnsafeText)
    assert isinstance(wrap_var(u"x"), AnsibleUnsafeText)
    assert isinstance(wrap_var("x".encode("utf-8")), AnsibleUnsafeText)
    assert isinstance(wrap_var("x".encode("utf-8").decode("utf-8")), AnsibleUnsafeText)
    assert isinstance(wrap_var("x".decode("utf-8")), AnsibleUnsafeText)

    import jinja2
    j2_t = jinja2.Template("{{ x }}")
    assert isinstance(wrap_var(j2_t.module), NativeJinjaUnsafeText)

# Generated at 2022-06-13 16:48:05.316148
# Unit test for function wrap_var
def test_wrap_var():
    #Test wrap var with dict
    data = {"a":1,"b":2}
    result = wrap_var(data)
    assert isinstance(result, dict)
    assert isinstance(result["a"], int)
    assert isinstance(result["b"], int)

    #Test wrap var with list
    data = [1,2,3]
    result = wrap_var(data)
    assert isinstance(result, list)
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
    assert isinstance(result[2], int)

    #Test wrap var with tuple
    data = (1,2,3)
    result = wrap_var(data)
    assert isinstance(result, tuple)
    assert isinstance(result[0], int)

# Generated at 2022-06-13 16:48:15.120966
# Unit test for function wrap_var
def test_wrap_var():
    # Test for set
    x = set(['a', 'b', 'c'])
    y = wrap_var(x)
    assert y == set([b'a', b'b', b'c'])
    assert y[1] == b'b'
    # Test for list
    x = [x, 'test']
    y = wrap_var(x)
    assert y == [set([b'a', b'b', b'c']), b'test']
    assert y[1] == b'test'
    # Test for dict
    x = {'x': 'test', 'y': 1}
    y = wrap_var(x)
    assert y == {b'x': b'test', b'y': 1}
    assert y[b'x'] == b'test'
    # Test for recursion

# Generated at 2022-06-13 16:48:25.833079
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.six import binary_type, text_type
    from ansible.utils.native_jinja import NativeJinjaText

    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(True), type(True))
    assert isinstance(wrap_var(False), type(False))
    assert isinstance(wrap_var(123), type(123))
    assert isinstance(wrap_var(3.14), type(3.14))
    assert isinstance(wrap_var('value'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'value'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:48:34.905179
# Unit test for function wrap_var
def test_wrap_var():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestUnsafeProxy(unittest.TestCase):
        def test_wrap_var(self):
            from ansible.parsing.yaml.objects import AnsibleUnicode
            self.assertIsInstance(wrap_var('foobar'), AnsibleUnsafeText)
            self.assertIsInstance(wrap_var(b'foobar'), AnsibleUnsafeBytes)
            self.assertIsInstance(wrap_var(AnsibleUnicode('foobar')), AnsibleUnsafeText)
            self.assertIsInstance(wrap_var(AnsibleUnsafeText(u'foobar')), AnsibleUnsafeText)

# Generated at 2022-06-13 16:48:44.906848
# Unit test for function wrap_var
def test_wrap_var():
    import inspect
    import types

    # Test all core types and some non core types, with associated test cases
    # This tuple structure is: (test_type, test_value, expected_type)

# Generated at 2022-06-13 16:48:55.263297
# Unit test for function wrap_var
def test_wrap_var():
    import json

    d = {'a': True, 'b': 'hello', 'c': {'d': 'hello', 'e': False}, 'f': ['a', True], 'g': ('a', 'b', False), 'h': {'a', 'b'}}
    e = wrap_var(d)
    assert json.dumps(d) == json.dumps(e)

    s = 'abcdef'
    assert isinstance(s, text_type)
    s = wrap_var(s)
    assert isinstance(s, text_type)
    assert isinstance(s, AnsibleUnsafe)

    s = ['a', 'b', 'c']
    assert not isinstance(s, AnsibleUnsafe)
    s = wrap_var(s)
    assert not isinstance(s, AnsibleUnsafe)


# Generated at 2022-06-13 16:49:02.179783
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils.common.collections import is_sequence, is_set, is_mapping
    from ansible.module_utils.common._collections_compat import Mapping, Set, Sequence, Hashable
    from ansible.utils.display import Display
    from ansible.module_utils.common.text.converters import to_bytes, to_text

    def _test_wrap(v, recurse=True, instance_type=None, is_mapping=None, is_sequence=None, is_set=None, is_hashable=None, isinstance_type=None):
        v = wrap_var(v)
        Display().vvvv(u'wrapped %s of type %s' % (v, type(v)))


# Generated at 2022-06-13 16:49:10.474911
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var("") == AnsibleUnsafeText(to_text(""))
    assert isinstance(wrap_var(""), AnsibleUnsafeText)
    assert wrap_var(1) == 1
    assert wrap_var(['test']) == _wrap_sequence(['test'])
    assert wrap_var(('test',)) == _wrap_sequence(('test',))
    assert wrap_var(dict(a=1)) == _wrap_dict(dict(a=1))
    assert wrap_var(set(['test'])) == _wrap_set(set(['test']))
    assert isinstance(wrap_var(AnsibleUnsafeText(to_text(""))), AnsibleUnsafeText)

# Generated at 2022-06-13 16:49:19.747489
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    display = Display()
    test_string = u'Hello World'
    test_string_unsafe = AnsibleUnsafeText(u'Hello World')
    test_dict = {'k1': test_string_unsafe, 'k2': test_string}
    test_dict_unsafe = {'k1': test_string_unsafe, 'k2': test_string_unsafe}
    test_list = [test_string_unsafe, test_string]
    test_list_unsafe = [test_string_unsafe, test_string_unsafe]
    test_set = {test_string_unsafe, test_string}
    test_set_unsafe = {test_string_unsafe, test_string_unsafe}

# Generated at 2022-06-13 16:49:30.984276
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import queue

    # Mapping types
    test_dict = {'foo': 'bar'}
    assert isinstance(wrap_var(test_dict), dict)
    assert not isinstance(wrap_var(test_dict)['foo'], AnsibleUnsafe)

    test_dict = {b'foo': 'bar'}
    assert isinstance(wrap_var(test_dict), dict)
    assert isinstance(wrap_var(test_dict)[b'foo'], AnsibleUnsafe)
    assert not isinstance(wrap_var(test_dict)['foo'], AnsibleUnsafe)

    test_dict = {u'foo': 'bar'}

# Generated at 2022-06-13 16:49:40.610135
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3
    if not PY3:
        assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
        assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
        assert isinstance(wrap_var(b'foo'.decode('utf-8')), AnsibleUnsafeText)
        assert isinstance(wrap_var(u'foo'.encode('utf-8')), AnsibleUnsafeBytes)
    else:
        assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
        assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
        assert isinstance(wrap_var('foo'.encode('utf-8')), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:49:52.950906
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_dict
    from ansible.module_utils.common.collections import is_sequence, is_set
    from ansible.module_utils.six import binary_type, text_type

    assert wrap_var(None) is None
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)

    assert isinstance(wrap_var({u'key': u'value'}), dict)
    assert isinstance(wrap_var([u'item1', u'item2']), list)
    assert isinstance(wrap_var((u'item1', u'item2')), tuple)

# Generated at 2022-06-13 16:50:04.278925
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var

    # Integer
    assert(wrap_var(1) == 1)

    # Float
    assert(wrap_var(1.0) == 1.0)

    # String
    assert(wrap_var("Text") == u"Text")

    # Dictionary
    d = dict(a=1, b="Text")
    assert(wrap_var(d) == {u"a": 1, u"b": u"Text"})

    # List
    l = [1, 2, u"Text"]
    assert(wrap_var(l) == [1, 2, u"Text"])

    # Set
    a_set = set(l)
    assert(wrap_var(a_set) == set([1, 2, u"Text"]))

    # Tuple


# Generated at 2022-06-13 16:50:15.577890
# Unit test for function wrap_var
def test_wrap_var():
    v = 'abc'
    # Testing if a string is wrapped with AnsibleUnsafeText
    assert isinstance(wrap_var(v), AnsibleUnsafeText)

    v = AnsibleUnsafeBytes('abc')
    wrap_var(v)
    # This line above should be safe, since it's a subclass of AnsibleUnsafeBytes
    assert isinstance(wrap_var(v), AnsibleUnsafeBytes)

    v = {'a': 'b', 'c': 'd'}
    # Testing a dictionary is wrapped
    assert isinstance(wrap_var(v), dict)
    assert isinstance(wrap_var(v)['a'], AnsibleUnsafeText)
    assert isinstance(wrap_var(v)['c'], AnsibleUnsafeText)

    v = ['a', 'b', 'c']
    # Testing

# Generated at 2022-06-13 16:50:27.257848
# Unit test for function wrap_var
def test_wrap_var():
    F = wrap_var
    assert isinstance(F("123"), AnsibleUnsafeText)
    assert F("123") == "123"

    assert isinstance(F(b"123"), AnsibleUnsafeBytes)
    assert F(b"123") == b"123"

    assert isinstance(F(NativeJinjaText("123")), NativeJinjaUnsafeText)

    assert isinstance(F(None), type(None))
    assert F(None) is None

    assert isinstance(F({"foo": "bar"}), dict)
    assert F({"foo": "bar"}) == {"foo": "bar"}
    assert isinstance(F({"foo": "bar"})["foo"], AnsibleUnsafeText)
    assert F({"foo": "bar"})["foo"] == "bar"


# Generated at 2022-06-13 16:50:34.385679
# Unit test for function wrap_var
def test_wrap_var():
    import datetime
    import time
    import dateutil.parser

    # Load some test strings to ensure they are properly wrapped

# Generated at 2022-06-13 16:50:42.801589
# Unit test for function wrap_var
def test_wrap_var():

    assert wrap_var(None) is None
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var(3.14), float)
    assert isinstance(wrap_var(True), bool)
    assert isinstance(wrap_var(False), bool)

    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'baz'), AnsibleUnsafeBytes)

    assert isinstance(wrap_var({}), dict)
    assert isinstance(wrap_var({u'foo': None}), dict)
    assert isinstance(wrap_var({u'foo': u'bar'}), dict)
    assert isinstance(wrap_var({u'foo': 1}), dict)

# Generated at 2022-06-13 16:50:49.902359
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(1) == 1
    assert wrap_var('string') == u'string'
    assert wrap_var(u'Unicode') == u'Unicode'
    assert wrap_var(_wrap_dict(dict(a=1, b='string'))) == dict(a=1, b=u'string')
    assert wrap_var(_wrap_sequence([1, 'string'])) == [1, u'string']
    assert wrap_var(_wrap_set(set(('item1', 'item2')))) == set((u'item1', u'item2'))
    assert wrap_var(u'Unicode' + b'Bytes') == u'UnicodeBytes'

# Generated at 2022-06-13 16:50:55.134122
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.builtin.unsafe_proxy._compat as _compat
    from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafe
    from itertools import chain

    def test_is_instance(x, cls):
        assert isinstance(x, cls)
        assert type(x) != cls
        assert isinstance(type(x), type(cls))
        assert type(type(x)) is type(type(cls))

    test_is_instance(wrap_var('foo'), AnsibleUnsafe)
    test_is_instance(wrap_var(b'bar'), AnsibleUnsafe)

    assert 'foo' == wrap_var('foo')
    assert b'bar' == wrap_var(b'bar')

    obj = object()

# Generated at 2022-06-13 16:51:00.301562
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(b'foo') == 'foo'
    assert wrap_var('foo') == 'foo'
    assert wrap_var(b'foo') is not b'foo'
    assert wrap_var('foo') is not 'foo'
    assert isinstance(wrap_var('foo'), text_type)
    assert isinstance(wrap_var(b'foo'), text_type)
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeText)
    assert wrap_var(b'foo').__UNSAFE__
    assert wrap_var('foo').__UNSAFE__
    assert wrap_var(u'foo').__UNSAFE__

# Generated at 2022-06-13 16:51:06.635429
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2

    class FakeBytes(unicode):
        pass

    class FakeUnicode(str):
        pass

    # Py2
    if PY2:
        assert isinstance(wrap_var(FakeBytes(u'foo')), unicode)
        assert isinstance(wrap_var(FakeUnicode(u'foo')), unicode)

    # Py3
    else:
        assert isinstance(wrap_var(FakeBytes(u'foo')), str)
        assert isinstance(wrap_var(FakeUnicode(u'foo')), str)

    assert isinstance(wrap_var(dict(((u'foo', u'bar'),))), dict)
    assert isinstance(wrap_var(set((u'foo', u'bar'))), set)