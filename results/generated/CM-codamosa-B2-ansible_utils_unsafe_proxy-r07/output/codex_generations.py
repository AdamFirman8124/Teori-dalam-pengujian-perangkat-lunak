

# Generated at 2026-11-03 05:38:10.492029
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    # Test basic construction
    unsafe_text = AnsibleUnsafeText('test string')
    assert unsafe_text == 'test string'
    assert isinstance(unsafe_text, AnsibleUnsafeText)
    assert isinstance(unsafe_text, text_type)
    assert isinstance(unsafe_text, AnsibleUnsafe)
    assert unsafe_text.__UNSAFE__ is True

    # Test empty string
    empty_unsafe = AnsibleUnsafeText()
    assert empty_unsafe == ''
    assert empty_unsafe.__UNSAFE__ is True

    # Test unicode content
    unicode_unsafe = AnsibleUnsafeText(u'tëst ünicode')
    assert unicode_unsafe == u'tëst ünicode'
    assert unicode_unsafe.__UNSAFE__ is True

    # Test encode maintains unsafe context
    encoded = unsafe_text.encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, binary_type)
    assert isinstance(encoded, AnsibleUnsafe)
    assert encoded == b'test string'
    assert encoded.__UNSAFE__ is True

    # Test decode of encoded value maintains unsafe context
    decoded = encoded.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == 'test string'
    assert decoded.__UNSAFE__ is True

    # Test string operations preserve value
    assert unsafe_text.upper() == 'TEST STRING'
    assert unsafe_text + ' appended' == 'test string appended'

# Generated at 2026-11-03 05:40:26.989726
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    unsafe_bytes = AnsibleUnsafeBytes(b"hello")

    # Should be a bytes type and flagged as unsafe
    assert isinstance(unsafe_bytes, binary_type)
    assert isinstance(unsafe_bytes, AnsibleUnsafe)
    assert unsafe_bytes.__UNSAFE__ is True

    # Value should be preserved
    assert unsafe_bytes == b"hello"

    # Decoding should maintain the unsafe context
    decoded = unsafe_bytes.decode()
    assert decoded == u"hello"
    assert isinstance(decoded, AnsibleUnsafeText)
    assert isinstance(decoded, text_type)
    assert decoded.__UNSAFE__ is True

# Generated at 2026-11-03 05:42:41.133258
# Unit test for function wrap_var
def test_wrap_var():
    # None stays None
    assert module_0.wrap_var(None) is None

    # Text strings become AnsibleUnsafeText
    unsafe_text = module_0.wrap_var(u'true')
    assert isinstance(unsafe_text, AnsibleUnsafeText)
    assert unsafe_text == u'true'
    assert getattr(unsafe_text, '__UNSAFE__', False) is True

    # Byte strings become AnsibleUnsafeBytes
    unsafe_bytes = module_0.wrap_var(b'true')
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes == b'true'
    assert getattr(unsafe_bytes, '__UNSAFE__', False) is True

    # Lists and tuples are wrapped per element, preserving the container type
    unsafe_list = module_0.wrap_var([u'one', u'two'])
    assert isinstance(unsafe_list, list)
    assert unsafe_list == [u'one', u'two']
    assert all(isinstance(item, AnsibleUnsafeText) for item in unsafe_list)

    unsafe_tuple = module_0.wrap_var((u'one', u'two'))
    assert isinstance(unsafe_tuple, tuple)
    assert unsafe_tuple == (u'one', u'two')
    assert all(isinstance(item, AnsibleUnsafeText) for item in unsafe_tuple)

    # Sets are wrapped per element
    unsafe_set = module_0.wrap_var({u'one', u'two'})
    assert isinstance(unsafe_set, set)
    assert unsafe_set == {u'one', u'two'}
    assert all(isinstance(item, AnsibleUnsafeText) for item in unsafe_set)

    # Mappings wrap both keys and values
    unsafe_dict = module_0.wrap_var({u'one': u'two'})
    assert isinstance(unsafe_dict, dict)
    assert unsafe_dict == {u'one': u'two'}
    for key, value in unsafe_dict.items():
        assert isinstance(key, AnsibleUnsafeText)
        assert isinstance(value, AnsibleUnsafeText)

    # Nested containers are wrapped recursively
    unsafe_nested = module_0.wrap_var({
        u'list': [u'one', [u'two']],
        u'dict': {u'key': u'value'},
        u'tuple': (u'three',),
    })
    assert isinstance(unsafe_nested[u'list'][0], AnsibleUnsafeText)
    assert isinstance(unsafe_nested[u'list'][1][0], AnsibleUnsafeText)
    assert isinstance(unsafe_nested[u'dict'][u'key'], AnsibleUnsafeText)
    assert isinstance(unsafe_nested[u'dict'][u'key'], AnsibleUnsafeText)
    assert isinstance(unsafe_nested[u'tuple'][0], AnsibleUnsafeText)

    # NativeJinjaText becomes NativeJinjaUnsafeText
    unsafe_native = module_0.wrap_var(NativeJinjaText(u'native'))
    assert isinstance(unsafe_native, NativeJinjaUnsafeText)
    assert unsafe_native == u'native'

    # Values already marked unsafe are returned unchanged
    already_unsafe = AnsibleUnsafeText(u'unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Non-string scalars pass through untouched
    assert module_0.wrap_var(1) == 1
    assert module_0.wrap_var(1.5) == 1.5
    assert module_0.wrap_var(True) is True
    assert module_0.wrap_var(False) is False

    # Type conversions preserve unsafe context
    assert isinstance(unsafe_text.encode('utf-8'), AnsibleUnsafeBytes)
    assert isinstance(unsafe_bytes.decode('utf-8'), AnsibleUnsafeText)

# Generated at 2026-11-03 05:45:10.943546
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    """Test the AnsibleUnsafe class constructor."""
    # Instantiation should succeed and mark the object as unsafe
    obj = AnsibleUnsafe()

    assert isinstance(obj, AnsibleUnsafe)
    assert obj.__UNSAFE__ is True

    # The unsafe marker is a class attribute, available on the class itself
    assert AnsibleUnsafe.__UNSAFE__ is True

    # Subclasses of AnsibleUnsafe should also be marked unsafe
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes

    text_obj = AnsibleUnsafeText(u'some text')
    assert isinstance(text_obj, AnsibleUnsafe)
    assert text_obj.__UNSAFE__ is True

    bytes_obj = AnsibleUnsafeBytes(b'some bytes')
    assert isinstance(bytes_obj, AnsibleUnsafe)
    assert bytes_obj.__UNSAFE__ is True