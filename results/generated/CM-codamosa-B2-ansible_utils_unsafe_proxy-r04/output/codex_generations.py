

# Generated at 2026-10-24 06:17:04.088929
# Unit test for function wrap_var
def test_wrap_var():
    # Values that do not require wrapping remain unchanged.
    assert module_0.wrap_var(None) is None

    scalar = object()
    assert module_0.wrap_var(scalar) is scalar

    # Text and bytes are wrapped in their unsafe counterparts.
    wrapped_text = module_0.wrap_var("text")
    assert type(wrapped_text) is AnsibleUnsafeText
    assert wrapped_text == "text"

    wrapped_bytes = module_0.wrap_var(b"bytes")
    assert type(wrapped_bytes) is AnsibleUnsafeBytes
    assert wrapped_bytes == b"bytes"

    # Native Jinja text retains its native context while becoming unsafe.
    wrapped_native = module_0.wrap_var(NativeJinjaText("native"))
    assert type(wrapped_native) is NativeJinjaUnsafeText
    assert wrapped_native == "native"

    # Existing unsafe values are returned without being recreated.
    unsafe = AnsibleUnsafeText("already unsafe")
    assert module_0.wrap_var(unsafe) is unsafe

    # Containers are recursively wrapped.
    wrapped = module_0.wrap_var({
        "key": [
            "value",
            b"binary",
            ("tuple value",),
            {"set value"},
        ],
        1: None,
    })

    wrapped_key = next(key for key in wrapped if key == "key")
    assert type(wrapped_key) is AnsibleUnsafeText
    assert wrapped[1] is None

    values = wrapped[wrapped_key]
    assert isinstance(values, list)
    assert type(values[0]) is AnsibleUnsafeText
    assert type(values[1]) is AnsibleUnsafeBytes

    assert isinstance(values[2], tuple)
    assert type(values[2][0]) is AnsibleUnsafeText

    assert isinstance(values[3], set)
    set_value = next(iter(values[3]))
    assert type(set_value) is AnsibleUnsafeText

# Generated at 2026-10-24 06:17:21.350330
# Unit test for constructor of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes():
    b = AnsibleUnsafeBytes(b'foo')

    # constructor preserves the value and the bytes type
    assert b == b'foo'
    assert type(b) is AnsibleUnsafeBytes
    assert isinstance(b, binary_type)

    # unsafe marker is inherited
    assert isinstance(b, AnsibleUnsafe)
    assert getattr(b, '__UNSAFE__', False) is True

    # decode() must return unsafe text, not plain text
    decoded = b.decode()
    assert decoded == u'foo'
    assert type(decoded) is AnsibleUnsafeText
    assert isinstance(decoded, AnsibleUnsafe)
    assert isinstance(decoded, text_type)

    # and it round-trips back to unsafe bytes
    assert type(decoded.encode()) is AnsibleUnsafeBytes

# Generated at 2026-10-24 06:17:48.298198
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:18:04.665944
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:18:11.121054
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    unsafe = AnsibleUnsafe()

    assert isinstance(unsafe, AnsibleUnsafe)
    assert unsafe.__UNSAFE__ is True

# Generated at 2026-10-24 06:18:16.851534
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    unsafe = AnsibleUnsafe()

    assert isinstance(unsafe, AnsibleUnsafe)
    assert unsafe.__UNSAFE__ is True

# Generated at 2026-10-24 06:18:23.817352
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("hÃ©llo".encode("utf-8"))

    result = value.decode("utf-8", errors="strict")

    assert type(result) is AnsibleUnsafeText
    assert result == "hÃ©llo"
    assert result.__UNSAFE__ is True

# Generated at 2026-10-24 06:19:08.302934
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.display import Display


# Generated at 2026-10-24 06:19:16.860553
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("cafÃ©".encode("utf-8"))

    result = value.decode("utf-8", errors="strict")

    assert result == "cafÃ©"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-24 06:19:39.899756
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    value = u'hello \N{SNOWMAN}'

    result = module_0.to_unsafe_bytes(value, encoding='utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == value.encode('utf-8')

    # Decoding must preserve the unsafe context.
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == value

# Generated at 2026-10-24 06:20:06.219362
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    with patch('ansible.utils.display.Display') as mock_display:
        # Existing unsafe values are returned unchanged.
        unsafe_value = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_value) is unsafe_value

        # Text values are converted to AnsibleUnsafeText.
        result = UnsafeProxy('value')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == 'value'

        # Non-string values are returned unchanged.
        original = object()
        assert UnsafeProxy(original) is original

        assert mock_display.return_value.deprecated.call_count == 3
        mock_display.return_value.deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-24 06:20:12.052509
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("cafÃ©".encode("utf-8"))

    result = value.decode(encoding="utf-8")

    assert result == "cafÃ©"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-24 06:20:40.724851
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    # 1. text -> unsafe bytes, value preserved
    result = module_0.to_unsafe_bytes(u'hello')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == b'hello'

    # 2. bytes -> unsafe bytes
    result = module_0.to_unsafe_bytes(b'hello')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'hello'

    # 3. utf-8 unicode round-trip
    result = module_0.to_unsafe_bytes(u'caf\xe9')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == u'caf\xe9'.encode('utf-8')
    assert result.decode('utf-8') == u'caf\xe9'

    # 4. kwargs are passed through to to_bytes
    result = module_0.to_unsafe_bytes(u'caf\xe9', encoding='latin-1')
    assert result == u'caf\xe9'.encode('latin-1')

    # 5. empty string
    result = module_0.to_unsafe_bytes(u'')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b''

# Generated at 2026-10-24 06:21:20.868549
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import call, patch

    message = (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
    )
    expected_deprecation = call(
        message,
        version='2.13',
        collection_name='ansible.builtin',
    )

    with patch('ansible.utils.display.Display') as mock_display:
        # Existing unsafe values must be returned unchanged.
        unsafe = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe) is unsafe

        # Text values must be converted to unsafe text.
        wrapped = UnsafeProxy('value')
        assert type(wrapped) is AnsibleUnsafeText
        assert wrapped == 'value'

        # Non-string values must be returned unchanged.
        value = object()
        assert UnsafeProxy(value) is value

        assert mock_display.call_count == 3
        assert mock_display.return_value.deprecated.call_args_list == [
            expected_deprecation,
            expected_deprecation,
            expected_deprecation,
        ]

# Generated at 2026-10-24 06:21:30.699540
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    result = module_0.to_unsafe_text(b'\xff', encoding='latin-1')

    assert result == u'\xff'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-24 06:22:26.462888
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:22:27.842133
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:22:57.738122
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch

# Generated at 2026-10-24 06:23:00.308597
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:02.722537
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:05.139364
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:07.550929
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:09.964978
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:12.378914
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:14.795944
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:23:22.416366
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():value = UnsafeProxy("secret")

# Generated at 2026-10-24 06:23:49.860074
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch

# Generated at 2026-10-24 06:24:07.557356
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:24:10.069201
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:24:12.578348
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:24:14.995443
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:24:17.409774
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:24:25.118613
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("example")

# Generated at 2026-10-24 06:24:50.785330
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    with patch('ansible.utils.display.Display.deprecated') as deprecated:
        text = 'example'
        wrapped_text = UnsafeProxy(text)

        assert isinstance(wrapped_text, AnsibleUnsafeText)
        assert wrapped_text == text
        assert wrapped_text is not text

        unsafe_text = AnsibleUnsafeText(text)
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'example')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        marker = object()
        assert UnsafeProxy(marker) is marker
        assert UnsafeProxy(None) is None

        assert deprecated.call_count == 5
        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-24 06:25:08.781489
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:11.196686
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:13.611159
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:16.026200
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:18.440115
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:20.854796
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:23.268992
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:25.683545
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:28.098119
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:30.513142
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:25:31.922923
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:26:07.623917
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from unittest.mock import patch

# Generated at 2026-10-24 06:26:10.041238
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:12.463525
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:14.877940
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:17.375083
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:19.790342
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:22.208387
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:24.632339
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:27.038235
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:29.454372
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:31.869393
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:34.284376
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:36.697700
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:39.112170
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:41.527806
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:43.941383
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:46.355980
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:48.771112
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:26:51.184617
# Unit test for method __new__ of class UnsafeProxy