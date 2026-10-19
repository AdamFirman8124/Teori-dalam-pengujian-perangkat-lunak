

# Generated at 2022-06-13 16:46:42.891585
# Unit test for function wrap_var
def test_wrap_var():
    examples = [
        {"a": 1, "b": "foo"},
        {"a": 1, "b": "foo", "c": {"d": "bar"}},
        ["foo", {"a": 1, "b": "bar"}, "baz"],
        (1, 2, 3, 4),
        set(["foo", "bar"]),
        to_text(b"foo"),
        to_bytes(u"bar"),
        NativeJinjaText(u"baz"),
        None,
    ]

    for ex in examples:
        assert not isinstance(wrap_var(ex), AnsibleUnsafe)
        assert wrap_var(ex) == ex

# Generated at 2022-06-13 16:46:51.465996
# Unit test for function wrap_var
def test_wrap_var():
    # test int
    assert wrap_var(1) == 1
    # test str
    assert wrap_var(u"str") == AnsibleUnsafeText(u"str")
    assert wrap_var(to_text(b"str")) == AnsibleUnsafeText(u"str")
    assert wrap_var(to_text(b"\x80str")) == AnsibleUnsafeText(u"\uFFFDstr")
    assert wrap_var(to_text(b"\x80str", errors='surrogate_or_strict')) == AnsibleUnsafeText(u"\uFFFDstr")
    assert wrap_var(to_text(b"\x80str", errors='strict')) == AnsibleUnsafeText(u"\uFFFDstr")
    assert wrap_var(u"中") == Ansible

# Generated at 2022-06-13 16:46:57.380813
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var({}), dict)

    assert isinstance(wrap_var(set()), set)

    assert isinstance(wrap_var(['foo']), list)
    assert isinstance(wrap_var((1, 2)), tuple)
    assert isinstance(wrap_var(['foo']), list)

    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)



# Generated at 2022-06-13 16:47:08.130491
# Unit test for function wrap_var
def test_wrap_var():
    import copy

    class Foo(object):
        pass

    foo = Foo()
    foo.bar = {
        'hello': 'world',
        'ping': ['pong', 'pang']
    }
    foo.bar['bar'] = foo.bar

    unsafe_foo = wrap_var(foo)
    assert foo is not unsafe_foo
    assert foo.bar is not unsafe_foo.bar
    assert foo.bar['hello'] is not unsafe_foo.bar['hello']
    assert foo.bar['ping'] is not unsafe_foo.bar['ping']
    assert foo.bar['ping'][0] is not unsafe_foo.bar['ping'][0]
    assert foo.bar['ping'][1] is not unsafe_foo.bar['ping'][1]
    assert foo.bar['bar'] is foo.bar
   

# Generated at 2022-06-13 16:47:17.315334
# Unit test for function wrap_var
def test_wrap_var():
    # Mapping
    test_dict = {
        'string': 'abc',
        'bytes': b'def',
        'unicode': u'ghi',
        'int': 1,
        'list': [u'a', b'b', 'c'],
        'dict': {
            'string': 'abc',
            'bytes': b'def',
            'unicode': u'ghi',
            'int': 1,
            'list': [u'a', b'b', 'c'],
        },
        'tuple': (u'a', 1, b'c'),
        'set': set([u'a', b'b', 'c']),
    }

# Generated at 2022-06-13 16:47:28.367895
# Unit test for function wrap_var
def test_wrap_var():
    # Test a few simple types just to ensure that they make it through correctly
    assert wrap_var(None) is None
    assert wrap_var(True) is True
    assert wrap_var(1) == 1

    # Test that a string is returned as an AnsibleUnsafeText
    s = 'simple string'
    assert isinstance(wrap_var(s), AnsibleUnsafeText)

    # Test that a dict is returned with AnsibleUnsafeText keys and values
    d = {'key1': 'value1', 'key2': 'value2'}
    wd = wrap_var(d)
    for key in wd.keys():
        assert isinstance(key, AnsibleUnsafeText)
    for value in wd.values():
        assert isinstance(value, AnsibleUnsafeText)

    # Test that a list is returned

# Generated at 2022-06-13 16:47:37.183847
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.module_utils as module_utils

    # Test basic usage of wrap_var
    unwrapped_foo_dict = {'foo': 'bar', 'baz': {'qux': 1}}
    wrapped_foo_dict = module_utils.basic._wrap_var(unwrapped_foo_dict)
    assert isinstance(unwrapped_foo_dict, dict)
    assert isinstance(wrapped_foo_dict, dict)
    assert isinstance(wrapped_foo_dict['foo'], module_utils.basic.AnsibleUnsafeText)
    assert isinstance(wrapped_foo_dict['baz'], dict)
    assert isinstance(wrapped_foo_dict['baz']['qux'], module_utils.basic.AnsibleUnsafeText)

    # Test wrap_var with no

# Generated at 2022-06-13 16:47:47.209002
# Unit test for function wrap_var
def test_wrap_var():
    import json

    def assert_wrap_var(raw, expected):
        """Helper function to simplify testing"""
        wrapped = wrap_var(raw)
        assert isinstance(wrapped, type(expected))
        assert wrapped == expected

    # These are from the original test case in the recipe
    assert_wrap_var('abc', 'abc')
    assert_wrap_var(2, 2)
    assert_wrap_var(('a', 'b'), ('a', 'b'))
    assert_wrap_var({'a': 'b'}, {'a': 'b'})
    assert_wrap_var('2.5', '2.5')
    assert_wrap_var({'a': {'b': 'c'}}, {'a': {'b': 'c'}})

# Generated at 2022-06-13 16:47:56.793345
# Unit test for function wrap_var
def test_wrap_var():

    import ansible.module_utils.basic
    import ansible.module_utils.urls
    import ansible.module_utils.six
    import ansible.module_utils.network
    import ansible.module_utils.common.text
    import ansible.module_utils.common.warnings
    import ansible.module_utils.connection
    import ansible.module_utils.ec2
    import ansible.module_utils.parsing.convert_bool
    import ansible.module_utils.parsing.convert_datetime
    import ansible.module_utils.parsing.convert_ips

    import os
    import sys
    import yaml
    import traceback


# Generated at 2022-06-13 16:48:04.122617
# Unit test for function wrap_var
def test_wrap_var():
    import sys
    from ansible.utils.unsafe_proxy import wrap_var

    # We only test the unsafe case, since safe tests are less interesting
    # and redundant with existing tests
    assert isinstance(wrap_var("foo"), AnsibleUnsafeText)
    assert isinstance(wrap_var("foo".encode("utf-8")), AnsibleUnsafeBytes)
    alist = wrap_var(list("foo"))
    assert isinstance(alist, list)
    for ch in alist:
        assert isinstance(ch, AnsibleUnsafeText)
    assert isinstance(wrap_var("foo"), AnsibleUnsafeText)
    assert isinstance(wrap_var("foo".encode("utf-8")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var((dict(a=1), list("foo"))), tuple)