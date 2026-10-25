

# Generated at 2026-10-25 01:41:54.755433
# Unit test for constructor of class UnsafeProxy
def test_UnsafeProxy():
    from ansible.utils.unsafe_proxy import (
        UnsafeProxy,
        AnsibleUnsafe,
        AnsibleUnsafeText,
    )

    # unicode string -> wrapped in AnsibleUnsafeText, value preserved
    proxied = UnsafeProxy(u'foo')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'foo'

    # bytes are NOT wrapped by UnsafeProxy (only string_types are)
    b = b'foo'
    assert UnsafeProxy(b) is b

    # None passthrough
    assert UnsafeProxy(None) is None

    # non-string objects returned unchanged
    obj = object()
    assert UnsafeProxy(obj) is obj

    # already-unsafe values returned as the same object (no re-wrap)
    unsafe = AnsibleUnsafeText(u'foo')
    assert UnsafeProxy(unsafe) is unsafe

    # anything AnsibleUnsafe is returned untouched
    class _FakeUnsafe(AnsibleUnsafe):
        pass
    fake = _FakeUnsafe()
    assert UnsafeProxy(fake) is fake

# Generated at 2026-10-25 01:42:12.495031
# Unit test for function wrap_var
def test_wrap_var():
    # None and already-unsafe values are returned unchanged.
    assert module_0.wrap_var(None) is None

    unsafe_text = AnsibleUnsafeText(u'unsafe text')
    unsafe_bytes = AnsibleUnsafeBytes(b'unsafe bytes')
    assert module_0.wrap_var(unsafe_text) is unsafe_text
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Plain scalar values that do not require wrapping remain unchanged.
    marker = object()
    assert module_0.wrap_var(marker) is marker
    assert module_0.wrap_var(42) == 42

    # Text and bytes are wrapped in their corresponding unsafe types.
    wrapped_text = module_0.wrap_var(u'text')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == u'text'

    wrapped_bytes = module_0.wrap_var(b'bytes')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'bytes'

    # Native Jinja text retains its native context while becoming unsafe.
    wrapped_native = module_0.wrap_var(NativeJinjaText(u'native'))
    assert isinstance(wrapped_native, NativeJinjaUnsafeText)
    assert isinstance(wrapped_native, NativeJinjaText)
    assert isinstance(wrapped_native, AnsibleUnsafeText)
    assert wrapped_native == u'native'

    # Lists and tuples preserve their container types and are wrapped
    # recursively.
    wrapped_list = module_0.wrap_var([u'first', b'second'])
    assert isinstance(wrapped_list, list)
    assert isinstance(wrapped_list[0], AnsibleUnsafeText)
    assert isinstance(wrapped_list[1], AnsibleUnsafeBytes)

    wrapped_tuple = module_0.wrap_var((u'first', b'second'))
    assert isinstance(wrapped_tuple, tuple)
    assert isinstance(wrapped_tuple[0], AnsibleUnsafeText)
    assert isinstance(wrapped_tuple[1], AnsibleUnsafeBytes)

    # Mapping keys and values are wrapped recursively.
    source = {
        u'key': [u'value', b'bytes'],
        u'nested': {u'inner': u'result'},
    }
    wrapped_mapping = module_0.wrap_var(source)

    assert isinstance(wrapped_mapping, dict)
    assert wrapped_mapping is not source
    assert all(isinstance(key, AnsibleUnsafeText)
               for key in wrapped_mapping)

    wrapped_values = wrapped_mapping[u'key']
    assert isinstance(wrapped_values[0], AnsibleUnsafeText)
    assert isinstance(wrapped_values[1], AnsibleUnsafeBytes)

    wrapped_nested = wrapped_mapping[u'nested']
    nested_key = next(iter(wrapped_nested))
    assert isinstance(nested_key, AnsibleUnsafeText)
    assert isinstance(wrapped_nested[nested_key], AnsibleUnsafeText)

    # Sets are wrapped recursively.
    wrapped_set = module_0.wrap_var({u'alpha', u'beta'})
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText)
               for item in wrapped_set)

# Generated at 2026-10-25 01:42:21.349547
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    value = u'unsafe text \u2603'
    result = AnsibleUnsafeText(value)

    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, text_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == value
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 01:42:29.469593
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 01:42:32.951313
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():result = module_0.to_unsafe_bytes(b"secret")

# Generated at 2026-10-25 01:42:45.955550
# Unit test for function wrap_var
def test_wrap_var():
    # None and unsupported scalar types remain unchanged.
    assert module_0.wrap_var(None) is None

    number = 42
    assert module_0.wrap_var(number) is number

    # Text and bytes are wrapped with their corresponding unsafe types.
    wrapped_text = module_0.wrap_var("text")
    assert type(wrapped_text) is AnsibleUnsafeText
    assert wrapped_text == "text"

    wrapped_bytes = module_0.wrap_var(b"bytes")
    assert type(wrapped_bytes) is AnsibleUnsafeBytes
    assert wrapped_bytes == b"bytes"

    # Existing unsafe values are returned unchanged.
    unsafe_text = AnsibleUnsafeText("unsafe")
    assert module_0.wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b"unsafe")
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Native Jinja text retains its native-Jinja and unsafe context.
    native_text = NativeJinjaText("native")
    wrapped_native = module_0.wrap_var(native_text)
    assert type(wrapped_native) is NativeJinjaUnsafeText
    assert wrapped_native == "native"

    # Sequences retain their type and are wrapped recursively.
    wrapped_list = module_0.wrap_var(["one", b"two"])
    assert type(wrapped_list) is list
    assert type(wrapped_list[0]) is AnsibleUnsafeText
    assert type(wrapped_list[1]) is AnsibleUnsafeBytes

    wrapped_tuple = module_0.wrap_var(("one", b"two"))
    assert type(wrapped_tuple) is tuple
    assert type(wrapped_tuple[0]) is AnsibleUnsafeText
    assert type(wrapped_tuple[1]) is AnsibleUnsafeBytes

    # Mapping keys and values are wrapped recursively.
    wrapped_dict = module_0.wrap_var({"key": ["value"]})
    wrapped_key = next(iter(wrapped_dict))
    assert type(wrapped_key) is AnsibleUnsafeText
    assert type(wrapped_dict[wrapped_key][0]) is AnsibleUnsafeText

    # Set members are wrapped recursively.
    wrapped_set = module_0.wrap_var({"item"})
    wrapped_item = next(iter(wrapped_set))
    assert type(wrapped_item) is AnsibleUnsafeText
    assert wrapped_item == "item"

# Generated at 2026-10-25 01:42:51.484759
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'\xc3\xa9')

    result = value.decode(encoding='utf-8', errors='strict')

    assert result == '\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 01:43:07.826608
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 01:43:16.163385
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_text,
    )

    result = module_0.to_unsafe_text(b'caf\xc3\xa9')
    assert type(result) is AnsibleUnsafeText
    assert result == u'caf\xe9'
    assert result.__UNSAFE__ is True

    encoded = result.encode('utf-8')
    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == b'caf\xc3\xa9'

    roundtrip = encoded.decode('utf-8')
    assert type(roundtrip) is AnsibleUnsafeText
    assert roundtrip == u'caf\xe9'

    numeric = module_0.to_unsafe_text(42)
    assert type(numeric) is AnsibleUnsafeText
    assert numeric == u'42'

# Generated at 2026-10-25 01:43:17.489002
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 01:43:18.820011
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_text,
    )

    result = module_0.to_unsafe_text(b'caf\xc3\xa9')
    assert type(result) is AnsibleUnsafeText
    assert result == u'caf\xe9'
    assert result.__UNSAFE__ is True

    encoded = result.encode('utf-8')
    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == b'caf\xc3\xa9'

    roundtrip = encoded.decode('utf-8')
    assert type(roundtrip) is AnsibleUnsafeText
    assert roundtrip == u'caf\xe9'

    numeric = module_0.to_unsafe_text(42)
    assert type(numeric) is AnsibleUnsafeText
    assert numeric == u'42'

# Generated at 2026-10-25 01:43:25.587803
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    unsafe_bytes = AnsibleUnsafeBytes(b'hello')

    result = unsafe_bytes.decode('utf-8')

    assert result == 'hello'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 01:43:26.916024
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 01:43:28.348624
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_text,
    )

    result = module_0.to_unsafe_text(b'caf\xc3\xa9')
    assert type(result) is AnsibleUnsafeText
    assert result == u'caf\xe9'
    assert result.__UNSAFE__ is True

    encoded = result.encode('utf-8')
    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == b'caf\xc3\xa9'

    roundtrip = encoded.decode('utf-8')
    assert type(roundtrip) is AnsibleUnsafeText
    assert roundtrip == u'caf\xe9'

    numeric = module_0.to_unsafe_text(42)
    assert type(numeric) is AnsibleUnsafeText
    assert numeric == u'42'

# Generated at 2026-10-25 01:43:33.572278
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'caf\xc3\xa9')

    result = value.decode('utf-8', errors='strict')

    assert result == 'caf\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 01:43:35.004683
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 01:43:36.391227
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        to_unsafe_text,
    )

    result = module_0.to_unsafe_text(b'caf\xc3\xa9')
    assert type(result) is AnsibleUnsafeText
    assert result == u'caf\xe9'
    assert result.__UNSAFE__ is True

    encoded = result.encode('utf-8')
    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == b'caf\xc3\xa9'

    roundtrip = encoded.decode('utf-8')
    assert type(roundtrip) is AnsibleUnsafeText
    assert roundtrip == u'caf\xe9'

    numeric = module_0.to_unsafe_text(42)
    assert type(numeric) is AnsibleUnsafeText
    assert numeric == u'42'

# Generated at 2026-10-25 01:43:37.873021
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:43:44.988459
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    value = AnsibleUnsafeText(u'unsafe \u2603')

    result = value.encode('utf-8', errors='strict')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'unsafe \xe2\x98\x83'

# Generated at 2026-10-25 01:43:47.559983
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 01:43:50.241920
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 01:43:52.657995
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 01:43:55.072103
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:43:57.487938
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:43:59.902123
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:02.318419
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:04.733517
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:07.310456
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:09.724856
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:12.139982
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:21.907992
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-25 01:44:23.338253
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:24.773618
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:26.149063
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:27.658537
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:29.072579
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:30.506636
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:31.939913
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:33.362013
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:34.806843
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:36.240405
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:37.674687
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:39.116409
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:40.550716
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:41.976008
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:43.409270
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:44.944771
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:46.379719
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:47.737530
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:44:50.264573
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:52.680863
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:55.209801
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:44:57.619664
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:00.034745
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:02.644298
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:05.060622
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:07.476167
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:09.892609
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:12.307734
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:14.723409
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:17.137937
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:19.554632
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:21.968759
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:24.384293
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:26.798780
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:29.214283
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:31.630331
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:45:49.154860
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.display import Display


# Generated at 2026-10-25 01:45:50.546173
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:45:52.026955
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:45:54.885210
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:45:56.317956
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:45:57.753769
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:45:59.187898
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:00.619093
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:02.155585
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:03.590312
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:05.024724
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:06.410451
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    """Unit test for UnsafeProxy.__new__ passthrough / wrapping logic."""
    dep_msg = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain str -> AnsibleUnsafeText with same value
        obj = UnsafeProxy('hello')
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, AnsibleUnsafe)
        assert isinstance(obj, string_types)
        assert obj == 'hello'
        assert obj.__UNSAFE__ is True
        MockDisplay.return_value.deprecated.assert_called_once_with(
            dep_msg, version='2.13', collection_name='ansible.builtin'
        )
        MockDisplay.reset_mock()

        # 2. empty str still wrapped
        obj = UnsafeProxy('')
        assert type(obj) is AnsibleUnsafeText
        assert obj == ''
        MockDisplay.reset_mock()

        # 3. already unsafe is returned unchanged (identity)
        unsafe_text = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        plain_unsafe = AnsibleUnsafe()
        assert UnsafeProxy(plain_unsafe) is plain_unsafe
        MockDisplay.reset_mock()

        # 4. non-string, non-unsafe is returned unchanged
        for value in [None, 42, 3.14, ['a'], ('a',), {'a': 1}, object()]:
            # use a fresh sentinel for mutable/object() to check identity
            result = UnsafeProxy(value)
            assert result is value

        # 5. extra *args/**kwargs are ignored but still deprecate
        result = UnsafeProxy('hi', None, foo='bar')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'hi'
        assert MockDisplay.return_value.deprecated

# Generated at 2026-10-25 01:46:08.953360
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:46:11.489022
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:46:13.912993
# Unit test for method __new__ of class UnsafeProxy