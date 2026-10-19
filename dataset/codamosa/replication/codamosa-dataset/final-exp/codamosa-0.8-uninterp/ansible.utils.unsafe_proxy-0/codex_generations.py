

# Generated at 2022-06-13 16:46:47.786545
# Unit test for function wrap_var
def test_wrap_var():
    import datetime
    from ansible.utils.unsafe_proxy import wrap_var as wrap_var
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText as AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes as AnsibleUnsafeBytes
    from ansible.utils.unsafe_proxy import NativeJinjaUnsafeText as NativeJinjaUnsafeText
    from ansible.utils.native_jinja import NativeJinjaText as NativeJinjaText
    # tests for strings
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)

    # tests for complex objects
    assert isinstance(wrap_var({'foo': u'bar'}), dict)

# Generated at 2022-06-13 16:46:57.860837
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import OrderedDict

    int_obj = 10
    str_obj = 'str'
    list_obj = ['str', 'str2']
    dict_obj = dict(k='v')
    dict_obj_ordered = OrderedDict(k='v')
    set_obj = set(['v'])
    bool_obj = True
    tuple_obj = ('str',)

    assert wrap_var(int_obj) == int_obj
    assert wrap_var(str_obj) == str_obj
    assert wrap_var(list_obj) == list_obj
    assert wrap_var(dict_obj) == dict_obj
    assert wrap_var(dict_obj_ordered) == dict_obj_ordered
    assert wrap_var(set_obj) == set_obj

# Generated at 2022-06-13 16:47:07.593837
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var({}) == {}, "wrap_var({}) failed"
    assert wrap_var({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}, "wrap_var({'a': 1, 'b': 2}) failed"
    assert wrap_var({'a': 1, 'b': None}) == {'a': 1, 'b': None}, "wrap_var({'a': 1, 'b': None}) failed"
    assert wrap_var({'a': 1, 'b': None}) == {'a': 1, 'b': None}, "wrap_var({'a': 1, 'b': None}) failed"
    assert wrap_var(['a', 'b']) == ['a', 'b'], "wrap_var(['a', 'b']) failed"

# Generated at 2022-06-13 16:47:17.240824
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    from ansible.utils.unsafe_proxy import UnsafeProxy

    display = Display()
    proxy = UnsafeProxy

    assert isinstance(wrap_var('s'), AnsibleUnsafeText)

    # No conversion type
    assert isinstance(wrap_var(b's'), AnsibleUnsafeBytes)

    # Conversion types
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var(1.0), float)

    # Lists
    l = [b'a', 1]
    assert isinstance(wrap_var(l), list)
    assert isinstance(wrap_var(l[0]), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(l[1]), int)

    # Tuples
    t = (b'a', 1)


# Generated at 2022-06-13 16:47:28.319592
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six.moves import builtins
    ansible_module = builtins.__import__("ansible.module_utils.basic", globals(), locals(), ['AnsibleModule'], 0)
    module = ansible_module.AnsibleModule(argument_spec=dict(wrap=dict(required=True, type='dict')))
    wrapped = wrap_var(module.params['wrap'])

    if not isinstance(wrapped["a"], AnsibleUnsafeText):
        module.fail_json(msg='`AnsibleUnsafeText` not wrapped')
        return

    if not isinstance(wrapped["b"], AnsibleUnsafeText):
        module.fail_json(msg='`AnsibleUnsafeText` not wrapped')
        return


# Generated at 2022-06-13 16:47:37.151328
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.compat.tests import unittest
    from ansible.utils.display import Display
    try:
        from collections import OrderedDict
    except ImportError:
        # python < 2.7
        from ansible.utils.ordereddict import OrderedDict

    display = Display()

    try:
        # python < 2.7
        from unittest.case import TestCase
    except ImportError:
        TestCase = unittest.TestCase

    class TestWrapVar(TestCase):

        def test_wrap_dict(self):
            hashes = [dict, OrderedDict]

# Generated at 2022-06-13 16:47:47.197349
# Unit test for function wrap_var
def test_wrap_var():
    assert AnsibleUnsafeBytes == type(wrap_var('foo'))
    assert AnsibleUnsafeText == type(wrap_var(u'foo'))
    assert AnsibleUnsafeText == type(wrap_var(NativeJinjaText(u'foo')))
    assert NativeJinjaUnsafeText == type(wrap_var(NativeJinjaUnsafeText(u'foo')))

    assert AnsibleUnsafeBytes == type(wrap_var(b'foo'))
    assert AnsibleUnsafeText == type(wrap_var(to_unsafe_text(b'foo')))
    assert AnsibleUnsafeBytes == type(wrap_var(to_unsafe_bytes(u'foo')))


# Generated at 2022-06-13 16:47:56.761209
# Unit test for function wrap_var
def test_wrap_var():
    import sys
    assert sys.version_info >= (2,7)
    import unittest
    class WrapVarTests(unittest.TestCase):

        def test_wrap_var_simple(self):
            a = "hello world"
            result = wrap_var(a)
            assert result == "hello world"

        def test_wrap_var_dict(self):
            a = {"hello":1, "world":2}
            result = wrap_var(a)
            assert isinstance(result, dict)
            assert result == {"hello":1, "world":2}

        def test_wrap_var_list(self):
            a = [1,2]
            result = wrap_var(a)
            assert isinstance(result, list)
            assert result == [1,2]


# Generated at 2022-06-13 16:48:05.022200
# Unit test for function wrap_var
def test_wrap_var():
    import collections
    from ansible.module_utils.six import string_types
    assert type(wrap_var("b")) == AnsibleUnsafeText
    assert type(wrap_var(u"b")) == AnsibleUnsafeText
    assert type(wrap_var("b".encode())) == AnsibleUnsafeBytes

    s = {'a': 'b', 'b': 'c'}
    assert type(wrap_var(s)) == dict
    for k, v in wrap_var(s).items():
        assert type(k) == AnsibleUnsafeText
        assert type(v) == AnsibleUnsafeText
    assert type(wrap_var(tuple(s))) == tuple
    assert type(wrap_var(list(s))) == list
    assert type(wrap_var(collections.OrderedDict(s))) == collections

# Generated at 2022-06-13 16:48:13.926622
# Unit test for function wrap_var
def test_wrap_var():

    assert wrap_var(None) is None

    assert wrap_var(123) == wrap_var(b'123') == wrap_var(u'123') == 123

    ansible_unsafe_text = wrap_var(u'abc')
    assert isinstance(ansible_unsafe_text, AnsibleUnsafeText)
    assert ansible_unsafe_text == u'abc'

    ansible_unsafe_bytes = wrap_var(b'abc')
    assert isinstance(ansible_unsafe_bytes, AnsibleUnsafeBytes)
    assert ansible_unsafe_bytes == b'abc'

    tuple_value = wrap_var((u'abc', b'def', 123))
    assert isinstance(tuple_value, tuple)
    assert isinstance(tuple_value[0], AnsibleUnsafeText)
   