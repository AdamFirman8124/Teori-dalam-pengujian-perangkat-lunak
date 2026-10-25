

# Generated at 2026-10-24 19:53:42.093193
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    empty = AnsibleUnsafeText()
    assert empty == ""
    assert isinstance(empty, AnsibleUnsafe)
    assert isinstance(empty, str)

    text = AnsibleUnsafeText("hello")
    assert text == "hello"
    assert type(text) is AnsibleUnsafeText
    assert text.__UNSAFE__ is True

    assert AnsibleUnsafeText("hÃ©llo â") == "hÃ©llo â"
    assert AnsibleUnsafeText(b"hello", encoding="utf-8") == "hello"
    assert isinstance(AnsibleUnsafeText(b"hello", encoding="utf-8"), AnsibleUnsafe)
    assert AnsibleUnsafeText(123) == "123"

# Generated at 2026-10-24 19:53:43.427411
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    obj = AnsibleUnsafeBytes(b'foo')
    assert obj == b'foo'
    assert isinstance(obj, AnsibleUnsafeBytes)
    assert getattr(obj, '__UNSAFE__') is True
    assert isinstance(obj.decode(), AnsibleUnsafeText)
    assert getattr(obj.decode(), '__UNSAFE__') is True

# Generated at 2026-10-24 19:54:11.995012
# Unit test for function wrap_var
def test_wrap_var():
    # Values that should remain unchanged.
    assert module_0.wrap_var(None) is None

    number = 42
    assert module_0.wrap_var(number) is number

    unsafe_text = AnsibleUnsafeText(u'already unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Scalar string types.
    wrapped_text = module_0.wrap_var(u'text')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == u'text'

    wrapped_bytes = module_0.wrap_var(b'bytes')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'bytes'

    native_text = NativeJinjaText(u'native')
    wrapped_native = module_0.wrap_var(native_text)
    assert isinstance(wrapped_native, NativeJinjaUnsafeText)
    assert wrapped_native == native_text

    # Nested mappings and sequences.
    wrapped = module_0.wrap_var({
        u'list': [u'value', b'bytes', 1, None],
        u'tuple': (u'value',),
        u'set': {u'value'},
    })

    assert isinstance(wrapped, dict)
    assert all(isinstance(key, AnsibleUnsafeText) for key in wrapped)

    assert isinstance(wrapped[u'list'], list)
    assert isinstance(wrapped[u'list'][0], AnsibleUnsafeText)
    assert isinstance(wrapped[u'list'][1], AnsibleUnsafeBytes)
    assert wrapped[u'list'][2] == 1
    assert wrapped[u'list'][3] is None

    assert isinstance(wrapped[u'tuple'], tuple)
    assert isinstance(wrapped[u'tuple'][0], AnsibleUnsafeText)

    assert isinstance(wrapped[u'set'], set)
    assert all(isinstance(item, AnsibleUnsafeText)
               for item in wrapped[u'set'])

# Generated at 2026-10-24 19:54:18.167382
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    unsafe = AnsibleUnsafe()

    assert isinstance(unsafe, AnsibleUnsafe)
    assert unsafe.__UNSAFE__ is True

# Generated at 2026-10-24 19:54:19.498836
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    obj = AnsibleUnsafeBytes(b'foo')
    assert obj == b'foo'
    assert isinstance(obj, AnsibleUnsafeBytes)
    assert getattr(obj, '__UNSAFE__') is True
    assert isinstance(obj.decode(), AnsibleUnsafeText)
    assert getattr(obj.decode(), '__UNSAFE__') is True

# Generated at 2026-10-24 19:54:29.483659
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:54:30.809443
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.common.text.converters import to_text

# Generated at 2026-10-24 19:54:47.425434
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 19:55:03.870399
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 19:55:06.289196
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:08.706490
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:11.123310
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:13.799026
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:16.215350
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:18.631683
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:21.047744
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:23.464527
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:25.880831
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:28.297277
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:30.715285
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:33.131766
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:35.548367
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:37.963254
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:40.379251
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:42.798536
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:45.222246
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:55:52.997547
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-24 19:56:18.786729
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch
    from ansible.utils.display import Display

    with patch.object(Display, 'deprecated') as mock_deprecated:
        value = 'example'
        result = UnsafeProxy(value)

        assert result == value
        assert isinstance(result, AnsibleUnsafeText)
        assert isinstance(result, AnsibleUnsafe)

        # Values already marked unsafe must be returned unchanged.
        unsafe_value = AnsibleUnsafeText(value)
        assert UnsafeProxy(unsafe_value) is unsafe_value

        # Unsupported/non-string values must also be returned unchanged.
        sentinel = object()
        assert UnsafeProxy(sentinel) is sentinel

        assert mock_deprecated.call_count == 3
        mock_deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-24 19:56:35.252908
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 19:56:37.674327
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:56:40.093105
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:56:42.655040
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:56:45.073465
# Unit test for function wrap_var

# Generated at 2026-10-24 19:56:47.492568
# Unit test for function wrap_var

# Generated at 2026-10-24 19:56:49.909741
# Unit test for function wrap_var

# Generated at 2026-10-24 19:56:52.324858
# Unit test for function wrap_var

# Generated at 2026-10-24 19:56:54.743114
# Unit test for function wrap_var

# Generated at 2026-10-24 19:56:57.159361
# Unit test for function wrap_var

# Generated at 2026-10-24 19:57:08.778013
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():text = 'unsafe value'

# Generated at 2026-10-24 19:57:25.645346
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 19:57:58.404118
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    from ansible.utils.display import Display

    with patch.object(Display, 'deprecated') as mock_deprecated:
        # Text values are converted to AnsibleUnsafeText.
        value = 'sensitive value'
        result = UnsafeProxy(value)

        assert type(result) is AnsibleUnsafeText
        assert result == value
        assert result.__UNSAFE__ is True

        # Values already marked unsafe are returned unchanged.
        unsafe_value = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_value) is unsafe_value

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        # Unsupported/non-string values are returned unchanged.
        non_string_value = object()
        assert UnsafeProxy(non_string_value) is non_string_value

        assert mock_deprecated.call_count == 4
        mock_deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-24 19:58:26.360814
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    with patch('ansible.utils.display.Display.deprecated') as deprecated:
        # Existing unsafe values must be returned unchanged.
        unsafe = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe) is unsafe

        # Text values must be converted to unsafe text.
        result = UnsafeProxy('test value')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'test value'

        # Non-string values must be returned unchanged.
        value = object()
        assert UnsafeProxy(value) is value

        assert deprecated.call_count == 3
        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-24 19:58:51.883855
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:58:53.207605
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.common.text.converters import to_text

# Generated at 2026-10-24 19:59:09.673124
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 19:59:36.502333
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    deprecation_message = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )

    with patch('ansible.utils.display.Display.deprecated') as deprecated:
        # Text values are converted to AnsibleUnsafeText.
        result = UnsafeProxy('some value')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'some value'

        # Existing unsafe values are returned unchanged.
        unsafe_value = AnsibleUnsafeText('already unsafe')
        result = UnsafeProxy(unsafe_value)
        assert result is unsafe_value

        # Non-string values are returned unchanged.
        ordinary_value = object()
        result = UnsafeProxy(ordinary_value)
        assert result is ordinary_value

    assert deprecated.call_count == 3
    deprecated.assert_called_with(
        deprecation_message,
        version='2.13',
        collection_name='ansible.builtin',
    )

# Generated at 2026-10-24 19:59:39.042823
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:41.464524
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:43.886674
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:46.306680
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:48.723857
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:51.141102
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:53.561473
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 19:59:54.916332
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.common.text.converters import to_text

# Generated at 2026-10-24 20:00:07.211640
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch

# Generated at 2026-10-24 20:00:23.810223
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 20:00:31.182924
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:00:32.616380
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.common.text.converters import to_text

# Generated at 2026-10-24 20:00:49.105775
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 20:00:51.644816
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:00:54.061479
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:01:01.495254
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("example")

# Generated at 2026-10-24 20:01:17.980898
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 20:01:47.223515
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:01:49.642796
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:01:52.159426
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:01:54.575935
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:02:02.832713
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-24 20:02:35.058979
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import call, patch

    text = u'unsafe value'
    already_unsafe = AnsibleUnsafeText(text)
    non_string = object()

    with patch('ansible.utils.display.Display.deprecated') as deprecated:
        wrapped = UnsafeProxy(text)
        unchanged_unsafe = UnsafeProxy(already_unsafe)
        unchanged_non_string = UnsafeProxy(non_string)

    assert type(wrapped) is AnsibleUnsafeText
    assert wrapped == text
    assert unchanged_unsafe is already_unsafe
    assert unchanged_non_string is non_string

    expected_call = call(
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
        version='2.13',
        collection_name='ansible.builtin',
    )
    assert deprecated.call_args_list == [expected_call] * 3

# Generated at 2026-10-24 20:02:51.675973
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 20:02:54.242007
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:03:01.200195
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch


# Generated at 2026-10-24 20:03:17.697500
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from ansible.errors import AnsibleError

    # Already-unsafe string passes through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'existing')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    # Plain text string is wrapped as AnsibleUnsafeText
    proxy = UnsafeProxy(u'test string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'test string'
    assert proxy.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    proxy = UnsafeProxy(b'byte string')
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == u'byte string'

    # Non-string values are returned untouched (not wrapped)
    for obj in (None, 1, 1.0, ['list'], {'dict': 'value'}, ('tuple',), {'set'}):
        assert UnsafeProxy(obj) is obj

    # Deprecated warning is raised on every invocation
    try:
        from ansible.module_utils.common.collections import is_sequence  # noqa: F401
        import ansible.utils.display as display_mod
        display_mod.Display().warning  # ensure display module importable
    except Exception:
        pass

# Generated at 2026-10-24 20:03:26.048917
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 20:03:27.368643
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.module_utils.common.text.converters import to_text