

# Generated at 2022-06-13 16:46:38.284775
# Unit test for function wrap_var
def test_wrap_var():
    import pytest

    import ansible.utils.unsafe_proxy

    v = ansible.utils.unsafe_proxy.wrap_var("foo")
    assert isinstance(v, ansible.utils.unsafe_proxy.AnsibleUnsafeText)
    assert v == "foo"

    v = ansible.utils.unsafe_proxy.wrap_var(b"foo")
    assert isinstance(v, ansible.utils.unsafe_proxy.AnsibleUnsafeBytes)
    assert v == "foo"

    v = ansible.utils.unsafe_proxy.wrap_var({'foo': 'bar'})
    assert isinstance(v, dict)
    assert v.get('foo') == "bar"

    v = ansible.utils.unsafe_proxy.wrap_var([b'foo', 'bar'])


# Generated at 2022-06-13 16:46:48.615825
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.utils.display import Display
    from ansible.module_utils.six import string_types, binary_type, text_type
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    assert wrap_var(None) is None

    assert repr(wrap_var("string")) == "u'string'"
    assert type(wrap_var("string")) is AnsibleUnsafeText
    assert isinstance(wrap_var("string"), string_types)
    assert isinstance(wrap_var("string"), text_type)

    assert repr(wrap_var(u"unicode")) == "u'unicode'"
    assert type(wrap_var(u"unicode")) is AnsibleUnsafeText
   

# Generated at 2022-06-13 16:46:57.944420
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    from ansible.module_utils.six import b, u

    assert wrap_var(None) is None
    assert wrap_var(42) == 42
    assert wrap_var(3.14) == 3.14
    assert wrap_var(b('foo')) == AnsibleUnsafeBytes(b('foo'))
    assert wrap_var(u(u'foo')) == AnsibleUnsafeText(u(u'foo'))
    assert wrap_var(u(u'\u00E9')) == AnsibleUnsafeText(u(u'\u00E9'))
    assert wrap_var(NativeJinjaText(u(''))) == NativeJinjaUnsafeText(u(''))

# Generated at 2022-06-13 16:47:08.196477
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('hello') == AnsibleUnsafeText('hello')
    assert isinstance(wrap_var('hello'), AnsibleUnsafeText)

    assert wrap_var(b'hello') == AnsibleUnsafeBytes(b'hello')
    assert isinstance(wrap_var(b'hello'), AnsibleUnsafeBytes)

    assert wrap_var(5) == 5
    assert isinstance(wrap_var(5), int)

    assert wrap_var(['a', 1, b'c']) == ['a', 1, AnsibleUnsafeBytes(b'c')]
    assert isinstance(wrap_var(['a', 1, b'c'])[0], AnsibleUnsafeText)
    assert isinstance(wrap_var(['a', 1, b'c'])[2], AnsibleUnsafeBytes)

    assert wrap_

# Generated at 2022-06-13 16:47:19.525427
# Unit test for function wrap_var
def test_wrap_var():
    import unittest
    import six

    class TestWrapVar(unittest.TestCase):

        def test_wrap_var_none(self):
            input_ = None
            expected = None
            output = wrap_var(input_)
            self.assertEqual(output, expected)

        def test_wrap_var_string(self):
            input_ = 'this is a test string'
            expected = AnsibleUnsafeText('this is a test string')
            output = wrap_var(input_)
            self.assertEqual(expected, output)
            self.assertEqual(type(output), AnsibleUnsafeText)

        def test_wrap_var_bytes(self):
            input_ = b'this is a test string'
            expected = AnsibleUnsafeBytes('this is a test string')

# Generated at 2022-06-13 16:47:25.800813
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.vars.unsafe_proxy import wrap_var
    # TODO: add more tests
    assert wrap_var("string") == "string"
    assert wrap_var(b"string") == b"string"
    assert wrap_var(1) == 1
    assert wrap_var(u"string") == u"string"

    dict_s = dict(a="a", b="b")
    dict_w = wrap_var(dict_s)
    assert dict_w == dict_s
    assert dict_w["a"] == "a"
    assert dict_w["b"] == "b"
    assert dict_w["a"] is dict_w["a"]
    assert dict_w["b"] is dict_w["b"]

    list_s = [1, 2, 3]
    list_w = wrap

# Generated at 2022-06-13 16:47:33.528492
# Unit test for function wrap_var
def test_wrap_var():
    from six import PY2
    assert isinstance(wrap_var("foo"), AnsibleUnsafeText)
    assert isinstance(wrap_var(b"foo"), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("أبجد"), AnsibleUnsafeText)
    assert isinstance(wrap_var(b"\xd8\xa3\xd8\xa8\xd8\xac\xd8\xaf"), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u"أبجد"), AnsibleUnsafeText)
    assert isinstance(wrap_var({'foo': 'bar', 'bar': 'foo'}), dict)

# Generated at 2022-06-13 16:47:40.575895
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None

    for unsafe_type in (AnsibleUnsafeText, NativeJinjaUnsafeText, AnsibleUnsafeBytes):
        assert isinstance(wrap_var(unsafe_type('foo')), unsafe_type)
        assert issubclass(unsafe_type, AnsibleUnsafe)

    # wrap_var() should not wrap string types
    for normal_string in (u'foo', to_bytes('foo'), b'foo'):
        assert wrap_var(normal_string) == normal_string

    # wrap_var() should not wrap bytes types when they are passed in as unicode
    assert wrap_var(u'foo') == u'foo'

    # wrap_var() should wrap bytes types when they are passed in as bytes

# Generated at 2022-06-13 16:47:49.450967
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('test') == 'test'
    assert wrap_var(AnsibleUnsafeText('test')) == 'test'
    assert wrap_var(AnsibleUnsafeBytes('test')) == 'test'
    assert wrap_var(AnsibleUnsafeBytes('test'.encode('utf-8'))) == 'test'
    assert wrap_var(AnsibleUnsafeText(AnsibleUnsafeBytes('test'.encode('utf-8')).decode('utf-8'))) == 'test'
    assert wrap_var(123) == 123
    assert wrap_var([1, 2, 3]) == [1, 2, 3]
    assert wrap_var((1, 2, 3)) == (1, 2, 3)

# Generated at 2022-06-13 16:47:58.530505
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.parsing.convert_bool import boolean
    import datetime
    import jinja2
    import sys

    assert wrap_var(None) is None
    assert wrap_var(3) == 3
    assert wrap_var(3.14) == 3.14
    assert wrap_var(True) is True
    assert wrap_var(False) is False
    assert wrap_var("1234") == u'1234'
    assert wrap_var(u"1234") == u'1234'
    assert wrap_var("1234") == u'1234'
    assert wrap_var(u"\u1234") == u'\u1234'
    assert wrap_var("\u1234") == u'\u1234'