

# Generated at 2022-06-13 16:46:37.473957
# Unit test for function wrap_var
def test_wrap_var():
    # Test strings
    test = "abc"
    assert test == wrap_var(test)
    assert isinstance(wrap_var(test), str)
    assert isinstance(wrap_var(test), AnsibleUnsafeText)
    test = u"abc"
    assert test == wrap_var(test)
    assert isinstance(wrap_var(test), str)
    assert isinstance(wrap_var(test), AnsibleUnsafeText)
    test = b"abc"
    assert test == wrap_var(test)
    assert isinstance(wrap_var(test), bytes)
    assert isinstance(wrap_var(test), AnsibleUnsafeBytes)

    # Test list
    test = [1,2,3]
    assert test == wrap_var(test)
    assert isinstance(wrap_var(test), list)
   

# Generated at 2022-06-13 16:46:48.091116
# Unit test for function wrap_var
def test_wrap_var():
    assert not isinstance(wrap_var('foo'), AnsibleUnsafe)
    assert not isinstance(wrap_var(b'foo'), AnsibleUnsafe)
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'foo')), AnsibleUnsafe)
    assert isinstance(wrap_var(AnsibleUnsafeText('foo')), AnsibleUnsafe)
    assert isinstance(wrap_var(NativeJinjaUnsafeText('foo')), NativeJinjaUnsafeText)

    wrapped_dict = wrap_var({'a': 'b'})
    assert isinstance(wrapped_dict, dict)
    assert not isinstance(wrapped_dict['a'], AnsibleUnsafe)

    wrapped_dict = wrap_var({'a': AnsibleUnsafeText('b')})

# Generated at 2022-06-13 16:46:57.897495
# Unit test for function wrap_var
def test_wrap_var():
    import json
    assert json.loads(json.dumps(wrap_var('foo'))) == 'foo'
    assert json.loads(json.dumps(wrap_var('bar'))) == 'bar'
    assert json.loads(json.dumps(wrap_var('baz'))) == 'baz'
    assert json.loads(json.dumps(wrap_var('foobar'))) == 'foobar'
    assert json.loads(json.dumps(wrap_var('barfoo'))) == 'barfoo'
    assert json.loads(json.dumps(wrap_var('barbaz'))) == 'barbaz'
    assert json.loads(json.dumps(wrap_var('foobaz'))) == 'foobaz'

# Generated at 2022-06-13 16:47:07.721230
# Unit test for function wrap_var
def test_wrap_var():
    # check if we return same object when given an AnsibleSafe object
    assert wrap_var(AnsibleUnsafeBytes())
    assert wrap_var(AnsibleUnsafeText())
    assert wrap_var(NativeJinjaUnsafeText())

    # check if we wrap dict
    unsafe_dict = dict(a=1, b=2)
    unsafe_dict['c'] = unsafe_dict
    wrapped_dict = wrap_var(unsafe_dict)
    for (k, v) in wrapped_dict.items():
        if k == 'c':
            assert v is wrapped_dict, 'should not have wrapped value'
        else:
            assert v.__UNSAFE__ is True, 'should have wrapped value'

    # check if we wrap set
    unsafe_set = set(['a', 'b', 'c'])
   

# Generated at 2022-06-13 16:47:17.266981
# Unit test for function wrap_var
def test_wrap_var():
    """Unittest for the function wrap_var"""
    # Check that a string is converted to a text
    assert isinstance(wrap_var("hello world"), AnsibleUnsafeText)
    assert wrap_var("hello world") == "hello world"

    # Check that a byte string is converted to a byte string
    assert isinstance(wrap_var(b"hello world"), AnsibleUnsafeBytes)
    assert wrap_var(b"hello world") == b"hello world"

    # Check that a list is converted to a list
    assert isinstance(wrap_var(["hello world"]), list)
    assert wrap_var(["hello world"]) == ["hello world"]

    # Check that a byte string in a list is converted to a byte string
    assert isinstance(wrap_var([b"hello world"])[0], AnsibleUnsafeBytes)


# Generated at 2022-06-13 16:47:21.807948
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSet
    from ansible.utils.native_jinja import NativeJinja2Text

    # Case: empty string
    v = ""
    assert wrap_var(v) is v
    assert type(wrap_var(v)) is AnsibleUnsafeText

    # Case: string
    v = "abc"
    assert wrap_var(v) is v
    assert type(wrap_var(v)) is AnsibleUnsafeText

    # Case: wrapped string
    v = AnsibleUnsafeText("abc")
    assert wrap_var(v) is v
    assert type(wrap_var(v)) is AnsibleUnsafeText

    # Case: AnsibleUnsafeBytes
    v = AnsibleUnsafeBytes(b"abc")

# Generated at 2022-06-13 16:47:30.938317
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3

    def compare_output(input, output, depth=1):
        if depth > 4:
            return
        if isinstance(input, dict):
            for key in input:
                if not output[key] == wrap_var(input[key]):
                    assert False, "Failed to wrap dict key %s with input %s, output %s" % (key, input[key], output[key])
                compare_output(input[key], wrap_var(input[key]), depth + 1)

# Generated at 2022-06-13 16:47:38.827458
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence
    import collections

    s = 'string'
    assert s == wrap_var(s)
    assert isinstance(s, str)
    assert not isinstance(s, AnsibleUnsafeText)

    # Non-str types and immutable types wrapped as-is
    d = type(None)
    assert d == wrap_var(d)
    assert isinstance(d, type)
    assert not isinstance(d, AnsibleUnsafe)

    d = collections.defaultdict
    assert d == wrap_var(d)
    assert isinstance(d, type(collections.defaultdict))
    assert not isinstance(d, AnsibleUnsafe)

    # class wraps as-is
    class Foo: pass
    d = Foo

# Generated at 2022-06-13 16:47:48.454359
# Unit test for function wrap_var
def test_wrap_var():
    import json
    import six

    assert wrap_var(None) is None
    assert wrap_var('') == ''
    assert wrap_var('ansible') == 'ansible'
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(True)

    assert wrap_var(AnsibleUnsafeText('ansible')) == 'ansible'
    assert wrap_var(AnsibleUnsafeBytes(b'ansible')) == b'ansible'
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'ansible')), (bytes, six.binary_type))
    assert wrap_var(NativeJinjaText('ansible')) == 'ansible'

    seq = (1, 2, 3, 4, 5)
   

# Generated at 2022-06-13 16:47:57.766050
# Unit test for function wrap_var
def test_wrap_var():
    # dict
    assert wrap_var(dict(a=1, b=2)) == dict(a=1, b=2)
    assert wrap_var({'a': 1, 'b': 2}) == dict(a=1, b=2)
    assert wrap_var({'a': 1, b'b': 2}) == dict(a=1, b=2)
    assert wrap_var({b'a': 1, 'b': 2}) == dict(a=1, b=2)
    assert wrap_var({b'a': 1, b'b': 2}) == dict(a=1, b=2)

    # list
    assert wrap_var([1, 2, 3]) == [1, 2, 3]
    assert wrap_var([1, 2, to_bytes('3')]) == [1, 2, 3]


# Generated at 2022-06-13 16:48:05.809229
# Unit test for function wrap_var
def test_wrap_var():
    from .compat import PY3
    from ansible.module_utils.common.collections import is_sequence

    assert wrap_var(None) is None
    assert wrap_var(AnsibleUnsafeBytes(b'test')) == b'test'
    assert wrap_var(AnsibleUnsafeBytes('test')) == b'test'
    assert wrap_var(AnsibleUnsafeText(u'test')) == u'test'

    assert isinstance(wrap_var({'test': b'test'}), dict)
    assert isinstance(wrap_var({'test': u'test'}), dict)
    assert isinstance(wrap_var([b'test']), list)
    assert isinstance(wrap_var([u'test']), list)

# Generated at 2022-06-13 16:48:14.482959
# Unit test for function wrap_var
def test_wrap_var():
    import unittest2 as unittest

    class TestWrapVar(unittest.TestCase):
        def test_wrap_var_dict(self):
            value = {"msg": "success"}
            actual = wrap_var(value)
            expected = {
                "msg": AnsibleUnsafeText("success")
            }
            self.assertDictEqual(actual, expected)

        def test_wrap_var_unicode(self):
            value = u"sample string"
            actual = wrap_var(value)
            expected = AnsibleUnsafeText("sample string")
            self.assertEqual(actual, expected)

        def test_wrap_var_set(self):
            value = {"success", "failure"}
            actual = wrap_var(value)

# Generated at 2022-06-13 16:48:25.436931
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.module_utils.common.collections as collections
    import ansible.module_utils.common.json_utils as json
    import ansible.module_utils.six as six
    from ansible.module_utils.six import string_types

    assert wrap_var('foo') == 'foo'
    assert isinstance(wrap_var(['foo']), collections.Sequence)
    assert isinstance(wrap_var(('foo',)), collections.Sequence)
    assert isinstance(wrap_var(set(['foo'])), collections.Set)
    assert isinstance(wrap_var({'foo': 'bar'}), collections.Mapping)
    assert isinstance(wrap_var({'foo': 'bar'}).get('foo'), string_types)

# Generated at 2022-06-13 16:48:32.687937
# Unit test for function wrap_var
def test_wrap_var():
    import os

# Generated at 2022-06-13 16:48:43.107041
# Unit test for function wrap_var
def test_wrap_var():
    class SafeBytes(binary_type):
        def __new__(cls, string):
            return binary_type.__new__(cls, string)

    class SafeText(text_type):
        def __new__(cls, string):
            return text_type.__new__(cls, string)

    # Test some objects that should pass through
    assert wrap_var(None) is None
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(u"test") == u"test"
    assert wrap_var("test") == u"test"
    assert wrap_var(b"test") == b"test"
    assert wrap_var(1j) == 1j
    assert wrap_var(AnsibleUnsafeText("test")) == Ans

# Generated at 2022-06-13 16:48:50.749138
# Unit test for function wrap_var
def test_wrap_var():
    # Dict
    assert isinstance(_wrap_dict({'test': 1}), dict)
    assert isinstance(_wrap_dict({'test': 1}).get('test'), AnsibleUnsafe)
    assert isinstance(_wrap_dict({'test': 1}).get('test'), AnsibleUnsafe)
    assert isinstance(_wrap_dict({'test': 1}).get('test').__UNSAFE__, True)
    # Sequence
    assert isinstance(_wrap_sequence(['test', 1]), list)
    assert isinstance(_wrap_sequence(('test', 1)), tuple)
    assert isinstance(_wrap_sequence(('test', 1))[0], AnsibleUnsafe)
    assert isinstance(_wrap_sequence(('test', 1))[1], AnsibleUnsafe)

# Generated at 2022-06-13 16:48:59.438128
# Unit test for function wrap_var
def test_wrap_var():
    import sys
    assert sys.version_info >= (2, 7)
    # wrap_var should return AnsibleUnsafeBytes/AnsibleUnsafeText
    # but replace the type of original string if it is already
    # AnsibleUnsafeBytes/AnsibleUnsafeText/NativeJinjaText
    assert wrap_var("string") == to_unsafe_text("string")
    assert type(wrap_var("string")) == AnsibleUnsafeText
    assert wrap_var("string".encode()) == to_unsafe_bytes("string")
    assert type(wrap_var("string".encode())) == AnsibleUnsafeBytes
    assert wrap_var(AnsibleUnsafeText("string")) == to_unsafe_text("string")
    assert type(wrap_var(AnsibleUnsafeText("string"))) == Ansible

# Generated at 2022-06-13 16:49:07.666767
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    display = Display()

    def assert_var_is_flag(var, value):
        assert var == value or value not in var
        display.deprecated(msg='test message', version='2.13',
                           collection_name='test_collection_name')
        assert var._deprecations == display._deprecations

    def assert_var_still_has_value(var, value):
        assert var == value


# Generated at 2022-06-13 16:49:15.068727
# Unit test for function wrap_var
def test_wrap_var():
    class TestAnsibleUnsafe(AnsibleUnsafe):
        pass

    class TestAnsibleUnsafeText(AnsibleUnsafeText):
        pass

    # Test: AnsibleUnsafe returns unchanged
    assert wrap_var(AnsibleUnsafe()) == AnsibleUnsafe()
    assert wrap_var(TestAnsibleUnsafe()) == TestAnsibleUnsafe()
    assert wrap_var(AnsibleUnsafeText()) == AnsibleUnsafeText()
    assert wrap_var(TestAnsibleUnsafeText()) == TestAnsibleUnsafeText()
    assert wrap_var(AnsibleUnsafeBytes()) == AnsibleUnsafeBytes()

    # Test: type wrappers
    assert wrap_var('foo') == AnsibleUnsafeText('foo')
    assert type(wrap_var('foo')) == AnsibleUn

# Generated at 2022-06-13 16:49:22.680324
# Unit test for function wrap_var
def test_wrap_var():
    """
    Test that we can properly wrap variables with ansible_unsafe wrapper
    and unwrap them again.
    """

    import copy

    list_var = ['foo', 'bar']
    dict_var = dict(a=1, b=2)
    
    assert wrap_var(list_var) == ['foo', 'bar']
    assert wrap_var(dict_var) == dict(a=1, b=2)

    # Wrap the variables with ansible_unsafe
    assert id(wrap_var(list_var)) != id(list_var)
    assert id(wrap_var(dict_var)) != id(dict_var)

    wrapped_list_var = wrap_var(list_var)
    wrapped_dict_var = wrap_var(dict_var)
