

# Generated at 2026-10-25 01:06:45.204816
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    value = u'Hello, ä¸ç'
    unsafe_value = AnsibleUnsafeText(value)

    assert type(unsafe_value) is AnsibleUnsafeText
    assert isinstance(unsafe_value, text_type)
    assert isinstance(unsafe_value, AnsibleUnsafe)
    assert unsafe_value == value
    assert unsafe_value.__UNSAFE__ is True

# Generated at 2026-10-25 01:06:51.401160
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    value = text_type('test value')
    result = AnsibleUnsafeText(value)

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, text_type)
    assert result == value
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 01:06:53.820320
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 01:06:56.236624
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 01:06:58.650552
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 01:07:01.066603
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 01:07:03.482451
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 01:07:05.895784
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 01:07:08.309923
# Unit test for function wrap_var

# Generated at 2026-10-25 01:07:10.725744
# Unit test for function wrap_var

# Generated at 2026-10-25 01:07:13.140683
# Unit test for function wrap_var

# Generated at 2026-10-25 01:07:15.790874
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:07:18.308280
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:07:20.721899
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:07:44.902905
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

# Generated at 2026-10-25 01:07:58.421525
# Unit test for function wrap_var
def test_wrap_var():
    # Values that should remain unchanged
    assert module_0.wrap_var(None) is None

    unchanged = object()
    assert module_0.wrap_var(unchanged) is unchanged
    assert module_0.wrap_var(42) == 42

    # Already unsafe values should not be wrapped again
    unsafe_text = AnsibleUnsafeText(u'already unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Text and bytes
    wrapped_text = module_0.wrap_var(u'example')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == u'example'

    wrapped_bytes = module_0.wrap_var(b'example')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'example'

    # Encoding and decoding must preserve the unsafe marker
    assert isinstance(wrapped_text.encode('utf-8'), AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes.decode('utf-8'), AnsibleUnsafeText)

    # Native Jinja text retains its native-Jinja and unsafe types
    wrapped_native = module_0.wrap_var(NativeJinjaText(u'native'))
    assert isinstance(wrapped_native, NativeJinjaUnsafeText)
    assert isinstance(wrapped_native, NativeJinjaText)
    assert isinstance(wrapped_native, AnsibleUnsafeText)
    assert wrapped_native == u'native'

    # Sequences are recursively wrapped and retain their type
    wrapped_list = module_0.wrap_var([u'one', b'two', 3])
    assert isinstance(wrapped_list, list)
    assert isinstance(wrapped_list[0], AnsibleUnsafeText)
    assert isinstance(wrapped_list[1], AnsibleUnsafeBytes)
    assert wrapped_list[2] == 3

    wrapped_tuple = module_0.wrap_var((u'one', b'two'))
    assert isinstance(wrapped_tuple, tuple)
    assert isinstance(wrapped_tuple[0], AnsibleUnsafeText)
    assert isinstance(wrapped_tuple[1], AnsibleUnsafeBytes)

    # Mapping keys and values are recursively wrapped
    wrapped_dict = module_0.wrap_var({u'key': [u'value']})
    wrapped_key = next(iter(wrapped_dict))
    assert isinstance(wrapped_key, AnsibleUnsafeText)
    assert isinstance(wrapped_dict[wrapped_key][0], AnsibleUnsafeText)

    # Sets are recursively wrapped
    wrapped_set = module_0.wrap_var({u'text', b'bytes'})
    assert isinstance(wrapped_set, set)
    assert any(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)
    assert any(isinstance(item, AnsibleUnsafeBytes) for item in wrapped_set)

# Generated at 2026-10-25 01:08:00.844661
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:03.261200
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:05.675452
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:08.243857
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:10.767123
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:13.183571
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:15.601638
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:18.020473
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:20.435126
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:22.850446
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:08:28.422045
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("hello")

# Generated at 2026-10-25 01:08:29.860823
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

# Generated at 2026-10-25 01:08:31.289283
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

# Generated at 2026-10-25 01:08:32.825946
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

# Generated at 2026-10-25 01:08:34.199936
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

# Generated at 2026-10-25 01:08:35.589671
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

# Generated at 2026-10-25 01:08:37.023561
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

# Generated at 2026-10-25 01:08:38.458348
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

# Generated at 2026-10-25 01:08:39.893077
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

# Generated at 2026-10-25 01:08:41.331722
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

# Generated at 2026-10-25 01:08:42.707594
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

# Generated at 2026-10-25 01:08:44.099627
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

# Generated at 2026-10-25 01:08:45.523499
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

# Generated at 2026-10-25 01:08:46.957955
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

# Generated at 2026-10-25 01:08:48.399289
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

# Generated at 2026-10-25 01:08:49.824707
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

# Generated at 2026-10-25 01:08:51.360614
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

# Generated at 2026-10-25 01:08:52.998886
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

# Generated at 2026-10-25 01:08:54.387441
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

# Generated at 2026-10-25 01:08:55.784838
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

# Generated at 2026-10-25 01:08:57.198476
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

# Generated at 2026-10-25 01:08:58.630433
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

# Generated at 2026-10-25 01:08:59.997143
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

# Generated at 2026-10-25 01:09:02.690040
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:05.101707
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:07.515649
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:10.024908
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:12.441331
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:14.856088
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:17.271212
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:19.686870
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:22.101445
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:24.516347
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:26.931041
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 01:09:35.187888
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-25 01:09:36.622033
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

# Generated at 2026-10-25 01:09:38.055441
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

# Generated at 2026-10-25 01:09:39.488568
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

# Generated at 2026-10-25 01:09:40.921863
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

# Generated at 2026-10-25 01:09:42.360452
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

# Generated at 2026-10-25 01:09:43.717048
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

# Generated at 2026-10-25 01:09:45.124674
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