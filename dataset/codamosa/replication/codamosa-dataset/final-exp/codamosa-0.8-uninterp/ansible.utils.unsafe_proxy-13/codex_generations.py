

# Generated at 2022-06-13 16:46:39.161229
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.utils.unsafe_proxy import UnsafeProxy
    assert isinstance(UnsafeProxy('foo'), AnsibleUnsafeText)

# Generated at 2022-06-13 16:46:49.166409
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    import sys

    import ansible
    if sys.version_info >= (3, 0):
        assert UnsafeProxy('foo') == 'foo'
        assert UnsafeProxy(b'foo') == b'foo'
        assert UnsafeProxy(UnsafeProxy('foo')) == 'foo'
        assert UnsafeProxy(UnsafeProxy(b'foo')) == b'foo'
    else:
        assert UnsafeProxy('foo') == b'foo'
        assert UnsafeProxy(b'foo') == b'foo'
        assert UnsafeProxy(UnsafeProxy('foo')) == b'foo'
        assert UnsafeProxy(UnsafeProxy(b'foo')) == b'foo'
    assert UnsafeProxy(ansible.constants.DEFAULT_VAULT_ID_MATCH) == ansible.constants.DEFAULT_VA

# Generated at 2022-06-13 16:46:58.327128
# Unit test for function wrap_var
def test_wrap_var():
    assert type(wrap_var(b'foo bar')) is AnsibleUnsafeBytes
    assert type(wrap_var(u'foo bar')) is AnsibleUnsafeText
    assert type(wrap_var([1, 2, 3])) is list
    assert type(wrap_var((1, 2, 3))) is tuple
    assert type(wrap_var({'one': 1, 'two': 2})) is dict
    assert type(wrap_var(set([1, 2, 3]))) is set
    assert type(wrap_var(NativeJinjaText("{% if True %}True{% else %}False{% endif %}"))) is NativeJinjaUnsafeText
    assert type(wrap_var(None)) is type(None)

if __name__ == "__main__":
    test_wrap_var()

# Generated at 2022-06-13 16:47:06.222463
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    assert UnsafeProxy(b'1234') == b'1234'
    # Now check that it returns in the expected classes ansible defined class
    assert isinstance(UnsafeProxy(b'1234'), AnsibleUnsafeBytes)
    assert UnsafeProxy(u'1234') == u'1234'
    assert isinstance(UnsafeProxy(b'1234'), AnsibleUnsafeBytes)
    # Now check that it returns in the expected classes ansible defined class
    assert isinstance(UnsafeProxy(u'1234'), AnsibleUnsafeText)



# Generated at 2022-06-13 16:47:16.378658
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(''), AnsibleUnsafeText)
    assert isinstance(wrap_var(b''), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(AnsibleUnsafeText('foo')), AnsibleUnsafeText)
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'foo')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var({'foo': 'bar'}), dict)
    k, v = list(wrap_var({'foo': 'bar'}).items())[0]

# Generated at 2022-06-13 16:47:23.864470
# Unit test for function wrap_var
def test_wrap_var():
    from collections import namedtuple

    assert wrap_var(None) == None
    assert wrap_var(10) == 10

    # wrap object
    assert isinstance(wrap_var('abc'), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_bytes('abc')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'abc'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'abc'), AnsibleUnsafeBytes)

    assert wrap_var(UnsafeProxy('abc')) == 'abc'
    assert isinstance(wrap_var(UnsafeProxy(u'abc')), AnsibleUnsafeText)
    assert isinstance(wrap_var(UnsafeProxy(b'abc')), AnsibleUnsafeBytes)

    assert wrap_var(u'abc') == 'abc'


# Generated at 2022-06-13 16:47:32.472194
# Unit test for function wrap_var
def test_wrap_var():
    test_dict = {
        "key1": "value1",
        "key2": [
            "value2.0",
            "value2.1"
        ]
    }

    unsafe_dict = _wrap_dict(test_dict)

    assert isinstance(unsafe_dict, dict)
    assert isinstance(unsafe_dict["key2"], list)
    assert isinstance(unsafe_dict["key1"], type(test_dict["key1"]))
    assert isinstance(unsafe_dict["key2"][0], type(test_dict["key2"][0]))

    assert unsafe_dict["key1"].__UNSAFE__
    assert unsafe_dict["key2"].__UNSAFE__
    assert unsafe_dict["key2"][0].__UNSAFE__


# Generated at 2022-06-13 16:47:35.368189
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(1) == 1
    assert isinstance(wrap_var(u'bytes'), AnsibleUnsafeText)
    assert isinstance(wrap_var(1), AnsibleUnsafe) is False

# Generated at 2022-06-13 16:47:41.743518
# Unit test for function wrap_var
def test_wrap_var():
    # Test wrap_var() with a string.
    assert isinstance(wrap_var(u'a'), AnsibleUnsafeText)

    # Test wrap_var() with a list.
    assert isinstance(wrap_var([u'a']), list)

    # Test wrap_var() with a list of strings.
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

    # Test wrap_var() with a tuple.
    assert isinstance(wrap_var((u'a',)), tuple)

    # Test wrap_var() with a tuple of strings.
    assert isinstance(wrap_var((u'a',))[0], AnsibleUnsafeText)

    # Test wrap_var() with a dict.
    assert isinstance(wrap_var({u'a': u'b'}), dict)

# Generated at 2022-06-13 16:47:42.474458
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    obj = object()
    proxy = UnsafeProxy(obj)
    assert proxy == obj