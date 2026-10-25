

# Generated at 2026-10-25 02:39:14.167654
# Unit test for function wrap_var
def test_wrap_var():
    # Values that should remain unchanged
    assert module_0.wrap_var(None) is None

    obj = object()
    assert module_0.wrap_var(obj) is obj

    unsafe_text = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Text and bytes
    wrapped_text = module_0.wrap_var('text')
    assert type(wrapped_text) is AnsibleUnsafeText
    assert wrapped_text == 'text'

    wrapped_bytes = module_0.wrap_var(b'bytes')
    assert type(wrapped_bytes) is AnsibleUnsafeBytes
    assert wrapped_bytes == b'bytes'

    # Native Jinja text
    wrapped_native = module_0.wrap_var(NativeJinjaText('native'))
    assert type(wrapped_native) is NativeJinjaUnsafeText
    assert wrapped_native == 'native'

    # Sequences preserve their container type
    wrapped_list = module_0.wrap_var(['one', b'two'])
    assert type(wrapped_list) is list
    assert type(wrapped_list[0]) is AnsibleUnsafeText
    assert type(wrapped_list[1]) is AnsibleUnsafeBytes

    wrapped_tuple = module_0.wrap_var(('one', b'two'))
    assert type(wrapped_tuple) is tuple
    assert type(wrapped_tuple[0]) is AnsibleUnsafeText
    assert type(wrapped_tuple[1]) is AnsibleUnsafeBytes

    # Sets are recursively wrapped
    wrapped_set = module_0.wrap_var({'one', 'two'})
    assert type(wrapped_set) is set
    assert all(type(item) is AnsibleUnsafeText for item in wrapped_set)

    # Mappings wrap both keys and values recursively
    wrapped_dict = module_0.wrap_var({
        'key': ['value', {'nested': b'data'}],
    })

    wrapped_key = next(iter(wrapped_dict))
    assert type(wrapped_key) is AnsibleUnsafeText

    wrapped_value = wrapped_dict[wrapped_key]
    assert type(wrapped_value) is list
    assert type(wrapped_value[0]) is AnsibleUnsafeText

    nested_key = next(iter(wrapped_value[1]))
    assert type(nested_key) is AnsibleUnsafeText
    assert type(wrapped_value[1][nested_key]) is AnsibleUnsafeBytes

# Generated at 2026-10-25 02:39:19.984506
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'\xc3\xa9')
    result = value.decode(encoding='utf-8', errors='strict')

    assert result == '\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 02:39:22.511289
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 02:39:25.038357
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 02:39:27.575652
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 02:39:29.991476
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:32.582793
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:34.997878
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:37.411980
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:39.830583
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:42.243812
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:44.657856
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:47.074419
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:49.489854
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:39:51.906041
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:54.320513
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:56.737148
# Unit test for function wrap_var

# Generated at 2026-10-25 02:39:59.151178
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:01.566564
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:03.982344
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:05.425435
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

# Generated at 2026-10-25 02:40:06.810558
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

# Generated at 2026-10-25 02:40:13.062867
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    value = AnsibleUnsafeText(u'caf\u00e9')

    result = value.encode('utf-8')

    assert result == b'caf\xc3\xa9'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 02:40:14.497734
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

# Generated at 2026-10-25 02:40:22.690187
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'\xc3\xa9')

    result = value.decode(encoding='utf-8', errors='strict')

    assert result == '\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 02:40:28.159119
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("cafÃ©".encode("utf-8"))

    result = value.decode("utf-8", errors="strict")

    assert result == "cafÃ©"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 02:40:36.205444
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    value = AnsibleUnsafeText(u'\u00e9')

    result = value.encode('utf-8')

    assert result == b'\xc3\xa9'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 02:40:38.977881
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:41.392540
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:43.810630
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:46.372742
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:48.787631
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:51.202393
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:40:53.616986
# Unit test for function wrap_var

# Generated at 2026-10-25 02:40:56.033247
# Unit test for function wrap_var

# Generated at 2026-10-25 02:40:58.448284
# Unit test for function wrap_var

# Generated at 2026-10-25 02:41:00.862959
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:41:03.278366
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:41:14.812459
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-25 02:41:16.247224
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

# Generated at 2026-10-25 02:41:17.677207
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

# Generated at 2026-10-25 02:41:19.111071
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

# Generated at 2026-10-25 02:41:20.544730
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

# Generated at 2026-10-25 02:41:21.986633
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

# Generated at 2026-10-25 02:41:23.412393
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

# Generated at 2026-10-25 02:41:24.849070
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

# Generated at 2026-10-25 02:41:26.279080
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

# Generated at 2026-10-25 02:41:27.712703
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

# Generated at 2026-10-25 02:41:29.152154
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

# Generated at 2026-10-25 02:41:30.588081
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

# Generated at 2026-10-25 02:41:42.076277
# Unit test for function wrap_var
def test_wrap_var():
    # None and unsupported scalar types are returned unchanged.
    assert module_0.wrap_var(None) is None
    assert module_0.wrap_var(42) == 42
    assert type(module_0.wrap_var(42)) is int

    # Existing unsafe values are not wrapped again.
    unsafe_text = AnsibleUnsafeText(u'already unsafe')
    unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Text and bytes receive their corresponding unsafe types.
    wrapped_text = module_0.wrap_var(u'text')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == u'text'

    wrapped_bytes = module_0.wrap_var(b'bytes')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'bytes'

    # Native Jinja text retains its native context and becomes unsafe.
    native_text = NativeJinjaText(u'native')
    wrapped_native = module_0.wrap_var(native_text)
    assert isinstance(wrapped_native, NativeJinjaUnsafeText)
    assert wrapped_native == native_text

    # Containers are recursively wrapped while preserving sequence types.
    wrapped_dict = module_0.wrap_var({
        u'key': [u'value', b'bytes'],
        u'nested': {u'inner': u'text'},
    })
    assert isinstance(wrapped_dict, dict)
    assert isinstance(next(iter(wrapped_dict)), AnsibleUnsafeText)
    assert isinstance(wrapped_dict[u'key'], list)
    assert isinstance(wrapped_dict[u'key'][0], AnsibleUnsafeText)
    assert isinstance(wrapped_dict[u'key'][1], AnsibleUnsafeBytes)
    assert isinstance(wrapped_dict[u'nested'][u'inner'], AnsibleUnsafeText)

    wrapped_tuple = module_0.wrap_var((u'one', b'two'))
    assert isinstance(wrapped_tuple, tuple)
    assert isinstance(wrapped_tuple[0], AnsibleUnsafeText)
    assert isinstance(wrapped_tuple[1], AnsibleUnsafeBytes)

    wrapped_set = module_0.wrap_var({u'one', u'two'})
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

# Generated at 2026-10-25 02:41:44.604172
# Unit test for function wrap_var

# Generated at 2026-10-25 02:41:47.147474
# Unit test for function wrap_var

# Generated at 2026-10-25 02:41:49.563320
# Unit test for function wrap_var

# Generated at 2026-10-25 02:41:51.981013
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:41:54.391696
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:41:56.807093
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:41:59.221897
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:42:01.637020
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:42:04.052120
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:42:06.466817
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 02:42:14.921630
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch
