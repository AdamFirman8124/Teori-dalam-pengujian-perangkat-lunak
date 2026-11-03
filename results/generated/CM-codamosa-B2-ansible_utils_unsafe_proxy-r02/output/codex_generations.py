

# Generated at 2026-11-02 19:45:42.869427
# Unit test for function wrap_var
def test_wrap_var():
    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Text is wrapped in AnsibleUnsafeText
    text = u'This is a string'
    unsafe_text = module_0.wrap_var(text)
    assert unsafe_text == text
    assert isinstance(unsafe_text, AnsibleUnsafeText)
    assert not isinstance(unsafe_text, AnsibleUnsafeBytes)
    assert unsafe_text.__UNSAFE__ is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    b_text = b'This is a byte string'
    unsafe_bytes = module_0.wrap_var(b_text)
    assert unsafe_bytes == b_text
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert not isinstance(unsafe_bytes, AnsibleUnsafeText)
    assert unsafe_bytes.__UNSAFE__ is True

    # Already unsafe objects pass through untouched
    already_unsafe = AnsibleUnsafeText(u'This is a string')
    assert module_0.wrap_var(already_unsafe) is already_unsafe

    # Lists are wrapped element by element
    lst = [u'This is a string', u'This is another string']
    unsafe_lst = module_0.wrap_var(lst)
    assert unsafe_lst == lst
    assert isinstance(unsafe_lst, list)
    assert not isinstance(unsafe_lst, AnsibleUnsafe)
    assert all(isinstance(i, AnsibleUnsafeText) for i in unsafe_lst)

    # Tuples are wrapped element by element
    tup = (u'This is a string', u'This is another string')
    unsafe_tup = module_0.wrap_var(tup)
    assert unsafe_tup == tup
    assert isinstance(unsafe_tup, tuple)
    assert all(isinstance(i, AnsibleUnsafeText) for i in unsafe_tup)

    # Dicts are wrapped for both keys and values
    dct = {u'This is a string': u'This is another string'}
    unsafe_dct = module_0.wrap_var(dct)
    assert unsafe_dct == dct
    assert isinstance(unsafe_dct, dict)
    assert not isinstance(unsafe_dct, AnsibleUnsafe)
    for key, value in unsafe_dct.items():
        assert isinstance(key, AnsibleUnsafeText)
        assert isinstance(value, AnsibleUnsafeText)

    # Sets are wrapped element by element
    st = set([u'This is a string', u'This is another string'])
    unsafe_st = module_0.wrap_var(st)
    assert unsafe_st == st
    assert isinstance(unsafe_st, set)
    assert all(isinstance(i, AnsibleUnsafeText) for i in unsafe_st)

    # Nested structures are wrapped recursively
    nested = {
        u'string': u'This is a string',
        u'bytes': b'This is a byte string',
        u'list': [u'This is a string', 1, None],
        u'dict': {u'This is a string': u'This is another string'},
    }
    unsafe_nested = module_0.wrap_var(nested)
    assert unsafe_nested == nested
    assert isinstance(unsafe_nested[u'string'], AnsibleUnsafeText)
    assert isinstance(unsafe_nested[u'bytes'], AnsibleUnsafeBytes)
    assert isinstance(unsafe_nested[u'list'][0], AnsibleUnsafeText)
    assert unsafe_nested[u'list'][1] == 1
    assert unsafe_nested[u'list'][2] is None
    assert isinstance(unsafe_nested[u'dict'][u'This is a string'], AnsibleUnsafeText)

    # NativeJinjaText becomes NativeJinjaUnsafeText
    nj_text = NativeJinjaText(u'This is a string')
    unsafe_nj_text = module_0.wrap_var(nj_text)
    assert unsafe_nj_text == nj_text
    assert isinstance(unsafe_nj_text, NativeJinjaUnsafeText)
    assert isinstance(unsafe_nj_text, AnsibleUnsafeText)

    # Non-string scalar types are returned unwrapped
    assert module_0.wrap_var(1) == 1
    assert not isinstance(module_0.wrap_var(1), AnsibleUnsafe)
    assert module_0.wrap_var(True) is True

    # Encoding unsafe text yields unsafe bytes
    encoded = module_0.wrap_var(u'This is a string').encode()
    assert isinstance(encoded, AnsibleUnsafeBytes)
    # Decoding unsafe bytes yields unsafe text
    decoded = encoded.decode()
    assert isinstance(decoded, AnsibleUnsafeText)

    # to_unsafe_text / to_unsafe_bytes helpers
    assert isinstance(to_unsafe_text(u'This is a string'), AnsibleUnsafeText)
    assert isinstance(to_unsafe_bytes(u'This is a string'), AnsibleUnsafeBytes)

# Generated at 2026-11-02 19:47:46.139775
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    # Simple decode with default arguments
    unsafe_bytes = AnsibleUnsafeBytes(b"foo")
    decoded = unsafe_bytes.decode()
    assert decoded == "foo"
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded.__UNSAFE__ is True

    # Decode with positional arguments (encoding, errors)
    unsafe_bytes = AnsibleUnsafeBytes(b"bar")
    decoded = unsafe_bytes.decode("utf-8", "strict")
    assert decoded == "bar"
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded.__UNSAFE__ is True

    # Decode with keyword arguments
    unsafe_bytes = AnsibleUnsafeBytes(b"baz")
    decoded = unsafe_bytes.decode(encoding="utf-8", errors="strict")
    assert decoded == "baz"
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded.__UNSAFE__ is True

    # Decode non-ascii bytes
    unsafe_bytes = AnsibleUnsafeBytes(u'\xe9'.encode('utf-8'))
    decoded = unsafe_bytes.decode("utf-8")
    assert decoded == u'\xe9'
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded.__UNSAFE__ is True

    # Decode empty bytes
    unsafe_bytes = AnsibleUnsafeBytes(b"")
    decoded = unsafe_bytes.decode()
    assert decoded == ""
    assert isinstance(decoded, AnsibleUnsafeText)

# Generated at 2026-11-02 19:50:18.415868
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    from ansible.utils.unsafe import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_bytes,
    )
    from ansible.module_utils.six import binary_type

    # Basic unicode string -> unsafe bytes
    result = module_0.to_unsafe_bytes(u'foo')
    assert isinstance(result, binary_type)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'foo'
    assert result.__UNSAFE__ is True

    # decode() preserves the unsafe context
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'foo'
    assert decoded.__UNSAFE__ is True

    # Keyword arguments are passed through to to_bytes()
    result = module_0.to_unsafe_bytes(u'café', encoding='utf-8', errors='strict')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'caf\xc3\xa9'

    # Bytes input is wrapped as-is
    result = module_0.to_unsafe_bytes(b'bar')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'bar'

    # Already-unsafe bytes pass through unchanged (not re-wrapped)
    already_unsafe = AnsibleUnsafeBytes(b'baz')
    assert module_0.to_unsafe_bytes(already_unsafe) is already_unsafe

# Generated at 2026-11-02 19:52:07.880896
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    obj = AnsibleUnsafeText(u'testing')
    encoded = obj.encode()

    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'testing'
    assert encoded.__UNSAFE__ is True
    assert isinstance(encoded, AnsibleUnsafe)