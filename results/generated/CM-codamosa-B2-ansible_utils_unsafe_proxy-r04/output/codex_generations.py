

# Generated at 2026-11-02 21:28:29.900972
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        NativeJinjaUnsafeText,
        wrap_var,
    )
    from ansible.utils.native_jinja import NativeJinjaText

    # None and non-string scalars pass through unchanged
    assert module_0.wrap_var(None) is None
    assert module_0.wrap_var(1) == 1
    assert not isinstance(module_0.wrap_var(1), AnsibleUnsafe)
    assert module_0.wrap_var(1.0) == 1.0
    assert not isinstance(module_0.wrap_var(1.0), AnsibleUnsafe)
    assert module_0.wrap_var(True) is True
    assert not isinstance(module_0.wrap_var(True), AnsibleUnsafe)

    # Text is wrapped in AnsibleUnsafeText
    wrapped = module_0.wrap_var(u'trusted')
    assert isinstance(wrapped, AnsibleUnsafeText)
    assert isinstance(wrapped, AnsibleUnsafe)
    assert wrapped == u'trusted'

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped = module_0.wrap_var(b'trusted')
    assert isinstance(wrapped, AnsibleUnsafeBytes)
    assert isinstance(wrapped, AnsibleUnsafe)
    assert wrapped == b'trusted'

    # encode/decode preserve the unsafe context
    assert isinstance(wrapped.decode('utf-8'), AnsibleUnsafeText)
    assert isinstance(AnsibleUnsafeText(u'trusted').encode('utf-8'), AnsibleUnsafeBytes)

    # NativeJinjaText is wrapped in NativeJinjaUnsafeText
    wrapped = module_0.wrap_var(NativeJinjaText(u'trusted'))
    assert isinstance(wrapped, NativeJinjaUnsafeText)
    assert wrapped == u'trusted'

    # Lists
    wrapped = module_0.wrap_var([u'one', u'two'])
    assert isinstance(wrapped, list)
    assert wrapped == [u'one', u'two']
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped)

    # Tuples
    wrapped = module_0.wrap_var((u'one', u'two'))
    assert isinstance(wrapped, tuple)
    assert wrapped == (u'one', u'two')
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped)

    # Sets
    wrapped = module_0.wrap_var(set([u'one', u'two']))
    assert isinstance(wrapped, set)
    assert wrapped == set([u'one', u'two'])
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped)

    # Dicts (both keys and values are wrapped)
    wrapped = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped, dict)
    assert wrapped == {u'key': u'value'}
    assert all(isinstance(key, AnsibleUnsafeText) for key in wrapped)
    assert all(isinstance(value, AnsibleUnsafeText) for value in wrapped.values())

    # Nested containers are recursively wrapped
    wrapped = module_0.wrap_var({u'list': [u'one', u'two'],
                        u'dict': {u'key': u'value'},
                        u'text': u'text'})
    assert isinstance(wrapped[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped[u'list'])
    assert isinstance(wrapped[u'dict'], dict)
    assert isinstance(wrapped[u'dict'][u'key'], AnsibleUnsafeText)

# Generated at 2026-11-02 21:29:21.127126
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    """Test the AnsibleUnsafeBytes constructor and its behavior."""
    # Creating an instance with bytes
    obj = AnsibleUnsafeBytes(b'foo')

    # The value should be preserved as bytes
    assert obj == b'foo'

    # It should be marked as unsafe
    assert obj.__UNSAFE__ is True
    assert isinstance(obj, AnsibleUnsafe)
    assert isinstance(obj, binary_type)

    # decode should return an unsafe text object
    decoded = obj.decode()
    assert decoded == u'foo'
    assert isinstance(decoded, AnsibleUnsafeText)
    assert isinstance(decoded, text_type)
    assert decoded.__UNSAFE__ is True

    # decode with explicit args/kwargs should also remain unsafe
    decoded2 = obj.decode('utf-8', errors='strict')
    assert decoded2 == u'foo'
    assert isinstance(decoded2, AnsibleUnsafeText)
    assert decoded2.__UNSAFE__ is True

    # encode on the decoded text should return unsafe bytes again
    reencoded = decoded.encode()
    assert reencoded == b'foo'
    assert isinstance(reencoded, AnsibleUnsafeBytes)
    assert reencoded.__UNSAFE__ is True

    # empty bytes should also work
    empty = AnsibleUnsafeBytes(b'')
    assert empty == b''
    assert empty.__UNSAFE__ is True

    # non-ascii bytes should work too
    nonascii = AnsibleUnsafeBytes(b'\xc3\xa9')
    assert nonascii.decode() == u'\xe9'
    assert nonascii.decode().__UNSAFE__ is True

# Generated at 2026-11-02 21:31:27.982026
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already unsafe objects are returned as-is (same object identity)
    unsafe_text = AnsibleUnsafeText(u'testing')
    assert UnsafeProxy(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'testing')
    assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

    # Text strings get wrapped in AnsibleUnsafeText
    proxied = UnsafeProxy(u'testing')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert not isinstance(proxied, AnsibleUnsafeBytes)
    assert proxied == u'testing'
    assert getattr(proxied, '__UNSAFE__', False) is True

    # Byte strings are not converted by UnsafeProxy (only string_types are wrapped)
    raw = b'testing'
    assert UnsafeProxy(raw) is raw
    assert not isinstance(UnsafeProxy(raw), AnsibleUnsafe)

    # Non-string values pass through untouched
    assert UnsafeProxy(None) is None

    container = [u'a', u'b']
    assert UnsafeProxy(container) is container
    assert not isinstance(container, AnsibleUnsafe)

# Generated at 2026-11-02 21:33:42.842127
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    instance = AnsibleUnsafe()
    assert isinstance(instance, AnsibleUnsafe)
    assert instance.__UNSAFE__ is True
    assert AnsibleUnsafe.__UNSAFE__ is True
    # AnsibleUnsafe is a plain object, not a string/bytes type
    assert not isinstance(instance, string_types)
    assert not isinstance(instance, binary_type)