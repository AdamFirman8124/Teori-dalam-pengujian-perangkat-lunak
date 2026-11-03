

# Generated at 2026-11-02 14:17:31.040907
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    # Construct with a plain unicode string
    obj = AnsibleUnsafeText(u'hello')
    assert isinstance(obj, AnsibleUnsafeText)
    assert isinstance(obj, text_type)
    assert isinstance(obj, AnsibleUnsafe)
    assert obj == u'hello'
    assert obj.__UNSAFE__ is True

    # Construct with an empty string
    empty = AnsibleUnsafeText(u'')
    assert isinstance(empty, AnsibleUnsafeText)
    assert empty == u''
    assert empty.__UNSAFE__ is True

    # Constructing from an existing AnsibleUnsafeText preserves type and value
    again = AnsibleUnsafeText(obj)
    assert isinstance(again, AnsibleUnsafeText)
    assert again == u'hello'
    assert again.__UNSAFE__ is True

    # Constructor should behave like str's constructor (repr/str conversions)
    from_str = AnsibleUnsafeText(str(123))
    assert from_str == u'123'
    assert from_str.__UNSAFE__ is True

# Generated at 2026-11-02 14:18:58.949005
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    with patch('ansible.utils.display.Display') as mock_display_cls:
        # Already unsafe objects are returned as-is
        unsafe_text = AnsibleUnsafeText(u'already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        # Text strings are wrapped in AnsibleUnsafeText
        result = UnsafeProxy(u'some string')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == u'some string'
        assert result.__UNSAFE__ is True

        # bytes are not string_types, so they pass through unchanged
        b_val = b'bytes value'
        assert UnsafeProxy(b_val) is b_val

        # Non-string objects are returned unchanged
        for value in (None, 42, 3.14, [1, 2], {'a': 1}, (1, 2), object()):
            assert UnsafeProxy(value) is value

        # Deprecation warning is issued on each call
        assert mock_display_cls.return_value.deprecated.call_count == 8

# Generated at 2026-11-02 14:20:29.615762
# Unit test for function wrap_var
def test_wrap_var():
    # None should pass through unchanged
    assert module_0.wrap_var(None) is None

    # Strings should be wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'trusted string')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == u'trusted string'

    # Bytes should be wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'trusted bytes')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'trusted bytes'

    # Already unsafe values should be returned unchanged (not re-wrapped)
    unsafe_text = AnsibleUnsafeText(u'unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'unsafe')
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Lists should be wrapped, with each element wrapped as well
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert not isinstance(wrapped_list, AnsibleUnsafe)
    for item in wrapped_list:
        assert isinstance(item, AnsibleUnsafeText)
    assert wrapped_list == [u'a', u'b']

    # Tuples should be wrapped, with each element wrapped as well
    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    for item in wrapped_tuple:
        assert isinstance(item, AnsibleUnsafeText)
    assert wrapped_tuple == (u'a', u'b')

    # Sets should be wrapped, with each element wrapped as well
    wrapped_set = module_0.wrap_var({u'a', u'b'})
    assert isinstance(wrapped_set, set)
    for item in wrapped_set:
        assert isinstance(item, AnsibleUnsafeText)
    assert wrapped_set == {u'a', u'b'}

    # Dicts should be wrapped, with keys and values wrapped as well
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    assert not isinstance(wrapped_dict, AnsibleUnsafe)
    for key, value in wrapped_dict.items():
        assert isinstance(key, AnsibleUnsafeText)
        assert isinstance(value, AnsibleUnsafeText)
    assert wrapped_dict == {u'key': u'value'}

    # Nested structures should be fully wrapped
    nested = module_0.wrap_var({u'list': [u'a', {u'key': u'val'}], u'set': {u'x'}, u'tuple': (u'y',)})
    assert isinstance(nested, dict)
    for key, value in nested.items():
        assert isinstance(key, AnsibleUnsafeText)
    assert isinstance(nested[u'list'], list)
    assert isinstance(nested[u'list'][0], AnsibleUnsafeText)
    assert isinstance(nested[u'list'][1], dict)
    assert isinstance(nested[u'list'][1][u'key'], AnsibleUnsafeText)
    assert isinstance(nested[u'set'], set)
    for item in nested[u'set']:
        assert isinstance(item, AnsibleUnsafeText)
    assert isinstance(nested[u'tuple'], tuple)
    for item in nested[u'tuple']:
        assert isinstance(item, AnsibleUnsafeText)

    # NativeJinjaText should be wrapped in NativeJinjaUnsafeText
    from ansible.module_utils.six import PY3
    try:
        from ansible.utils.native_jinja import NativeJinjaText
        native = NativeJinjaText(u'native template value')
        wrapped_native = module_0.wrap_var(native)
        from ansible.vars.unsafe import NativeJinjaUnsafeText
        assert isinstance(wrapped_native, NativeJinjaUnsafeText)
        assert wrapped_native == u'native template value'
    except ImportError:
        pass

    # Non-string, non-container types should pass through unchanged
    assert module_0.wrap_var(1) == 1
    assert module_0.wrap_var(1.5) == 1.5
    assert module_0.wrap_var(True) is True

    # Empty containers
    assert module_0.wrap_var([]) == []
    assert module_0.wrap_var({}) == {}
    assert module_0.wrap_var(()) == ()
    assert module_0.wrap_var(set()) == set()

    # AnsibleUnsafeText.encode should return AnsibleUnsafeBytes
    unsafe_text = AnsibleUnsafeText(u'test')
    encoded = unsafe_text.encode()
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'test'

    # AnsibleUnsafeBytes.decode should return AnsibleUnsafeText
    unsafe_bytes = AnsibleUnsafeBytes(b'test')
    decoded = unsafe_bytes.decode()
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'test'

# Generated at 2026-11-02 14:21:31.276288
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    # Construct from a plain text string
    unsafe = AnsibleUnsafeText(u'test string')
    assert isinstance(unsafe, AnsibleUnsafeText)
    assert isinstance(unsafe, text_type)
    assert isinstance(unsafe, AnsibleUnsafe)
    assert unsafe.__UNSAFE__ is True
    assert unsafe == u'test string'

    # Construct from an empty string
    empty = AnsibleUnsafeText(u'')
    assert isinstance(empty, AnsibleUnsafeText)
    assert empty == u''
    assert empty.__UNSAFE__ is True

    # encode() should maintain the unsafe context
    encoded = unsafe.encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, binary_type)
    assert encoded == b'test string'
    assert encoded.__UNSAFE__ is True

    # decode() should round-trip back into unsafe text
    decoded = encoded.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'test string'
    assert decoded.__UNSAFE__ is True

    # Constructing from an existing unsafe text should keep the value intact
    again = AnsibleUnsafeText(decoded)
    assert isinstance(again, AnsibleUnsafeText)
    assert again == u'test string'
    assert again.__UNSAFE__ is True

# Generated at 2026-11-02 14:23:16.030770
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    # Constructing from plain bytes should preserve the value
    unsafe_bytes = AnsibleUnsafeBytes(b'hello')
    assert unsafe_bytes == b'hello'
    assert isinstance(unsafe_bytes, binary_type)
    assert isinstance(unsafe_bytes, AnsibleUnsafe)
    assert unsafe_bytes.__UNSAFE__ is True

    # Empty bytes should also be wrapped
    empty_unsafe = AnsibleUnsafeBytes(b'')
    assert empty_unsafe == b''
    assert empty_unsafe.__UNSAFE__ is True

    # Constructing from a bytearray
    from_bytesarray = AnsibleUnsafeBytes(bytearray(b'data'))
    assert from_bytesarray == b'data'
    assert from_bytesarray.__UNSAFE__ is True

    # decode() should maintain the unsafe context via AnsibleUnsafeText
    decoded = unsafe_bytes.decode()
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == 'hello'
    assert decoded.__UNSAFE__ is True

    # decode() with explicit args/kwargs should also stay unsafe
    decoded_utf8 = AnsibleUnsafeBytes(b'world').decode('utf-8', errors='strict')
    assert isinstance(decoded_utf8, AnsibleUnsafeText)
    assert decoded_utf8 == 'world'
    assert decoded_utf8.__UNSAFE__ is True