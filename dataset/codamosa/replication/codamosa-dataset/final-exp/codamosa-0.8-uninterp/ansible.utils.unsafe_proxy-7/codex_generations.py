

# Generated at 2022-06-13 16:46:47.230454
# Unit test for function wrap_var
def test_wrap_var():
    # Test wrap_var with str
    uns = wrap_var("foobar")
    assert(isinstance(uns, AnsibleUnsafeText))
    assert(isinstance(uns, text_type))

    # Test wrap_var with bytes
    uns = wrap_var(b"foobar")
    assert(isinstance(uns, AnsibleUnsafeBytes))
    assert(isinstance(uns, binary_type))

    # Test wrap_var with list containing str and bytes
    uns = wrap_var(["foobar", b"foobar"])
    assert(isinstance(uns, list))
    assert(isinstance(uns[0], AnsibleUnsafeText))
    assert(isinstance(uns[1], AnsibleUnsafeBytes))

    # Test wrap_var with dict containing str and bytes

# Generated at 2022-06-13 16:46:57.783966
# Unit test for function wrap_var
def test_wrap_var():
    """
    Test to ensure wrap_var maintains AnsibleUnsafe context
    """
    assert isinstance(wrap_var(None), type(None))
    ascii_bytes = b"hello"
    assert isinstance(wrap_var(ascii_bytes), AnsibleUnsafeBytes)
    ascii_text = text_type("hello")
    assert isinstance(wrap_var(ascii_text), AnsibleUnsafeText)
    jinja_str = NativeJinjaText(ascii_text)
    assert isinstance(wrap_var(jinja_str), AnsibleUnsafeText)

    ascii_dict = dict(a=ascii_text, b=ascii_bytes)
    with_none = dict(a=None, b=ascii_text)
    wrap_dict = wrap

# Generated at 2022-06-13 16:47:08.196406
# Unit test for function wrap_var
def test_wrap_var():
    # The following will raise an exception if wrap_var fails
    wrap_var(None)

    wrap_var(1)
    wrap_var(1.1)
    wrap_var(u'unicode')
    wrap_var(b'bytestring')

    wrap_var([1, 2, 3])
    wrap_var((1, 2, 3))

    wrap_var({u'a': 1, u'b': 2})

    item = wrap_var(u'unicode')
    assert isinstance(item, AnsibleUnsafeText)

    item = wrap_var(b'bytestring')
    assert isinstance(item, AnsibleUnsafeBytes)

    item = wrap_var({u'a': 1, u'b': 2})
    assert isinstance(item, dict)

# Generated at 2022-06-13 16:47:13.172176
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var
    v = wrap_var("test")

    assert(isinstance(v, string_types))
    assert(isinstance(v, AnsibleUnsafe))

# Generated at 2022-06-13 16:47:18.441300
# Unit test for function wrap_var
def test_wrap_var():
    """
    Run doctest unit tests for wrap_var()
    """
    import doctest
    import ansible.module_utils.common.collections
    results = doctest.testmod(ansible.module_utils.common.collections)

    if results.failed == 0:
        print("Success: %s tests passed." % results.attempted)


if __name__ == "__main__":
    test_wrap_var()

# Generated at 2022-06-13 16:47:25.127836
# Unit test for function wrap_var
def test_wrap_var():
    import pytest

    class Foo(object):
        def __str__(self):
            return 'foo'

    assert wrap_var(Foo()) == 'foo'

    assert wrap_var('foo') == AnsibleUnsafeText(u'foo')
    assert wrap_var(u'foo') == AnsibleUnsafeText(u'foo')
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert wrap_var(u'foo'.encode('utf-8')) == AnsibleUnsafeText(u'foo')
    assert wrap_var(u'foo'.encode('utf-8')) == AnsibleUnsafeBytes(b'foo')

    assert wrap_var(b'foo') == AnsibleUnsafeBytes(b'foo')

# Generated at 2022-06-13 16:47:35.033753
# Unit test for function wrap_var
def test_wrap_var():
    obj0 = dict(a=dict(b=2, c=3))
    assert wrap_var(obj0) == dict(a=dict(b=2, c=3))

    obj1 = dict(a=5, b=6, c=7)
    assert wrap_var(obj1) == dict(a=5, b=6, c=7)

    obj2 = dict(a='hello', b='world')
    assert wrap_var(obj2) == dict(a='hello', b='world')

    obj3 = dict(a=dict(b='hello', c='world'))
    assert wrap_var(obj3) == dict(a=dict(b='hello', c='world'))

    obj4 = dict(a=5, b=dict(c='hello', d='world'))
    assert wrap_var

# Generated at 2022-06-13 16:47:41.522784
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('test') == AnsibleUnsafeText('test')
    assert wrap_var(b'test') == AnsibleUnsafeBytes(b'test')
    assert wrap_var(u'test') == AnsibleUnsafeText(u'test')
    assert wrap_var(AnsibleUnsafeText('str')) == AnsibleUnsafeText('str')
    assert wrap_var(AnsibleUnsafeBytes(b'str')) == AnsibleUnsafeBytes(b'str')
    assert wrap_var(None) is None
    assert wrap_var(1) == 1
    assert wrap_var([1, '2', b'3']) == [1, AnsibleUnsafeText('2'), AnsibleUnsafeBytes(b'3')]

# Generated at 2022-06-13 16:47:49.957688
# Unit test for function wrap_var
def test_wrap_var():
    # Wrap non-unsafe variables
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(42), type(42))
    assert isinstance(wrap_var(42.0), type(42.0))
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert wrap_var(u'foo') == u'foo'
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert wrap_var(b'foo') == b'foo'

    # Wrap dict
    assert wrap_var({'foo': u'bar'}) == {'foo': AnsibleUnsafeText(u'bar')}

# Generated at 2022-06-13 16:47:54.722448
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert not isinstance(wrap_var(None), AnsibleUnsafeText)