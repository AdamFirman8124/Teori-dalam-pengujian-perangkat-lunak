

# Generated at 2026-10-25 08:25:55.716081
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 08:25:58.273627
# Unit test for function to_unsafe_text

# Generated at 2026-10-25 08:26:05.039596
# Unit test for function to_unsafe_text
def test_to_unsafe_text():result = module_0.to_unsafe_text(b"hello", encoding="utf-8")

# Generated at 2026-10-25 08:26:06.579783
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    # str input -> wrapped as AnsibleUnsafeBytes
    result = module_0.to_unsafe_bytes(u'test string')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'test string'
    assert getattr(result, '__UNSAFE__', False) is True

    # already-bytes input -> still wrapped
    result = module_0.to_unsafe_bytes(b'raw bytes')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'raw bytes'

    # None passes through unchanged
    assert module_0.to_unsafe_bytes(None) is None

    # decode() on the result keeps the unsafe context
    decoded = module_0.to_unsafe_bytes(u'test string').decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'test string'

# Generated at 2026-10-25 08:26:09.546896
# Unit test for function wrap_var

# Generated at 2026-10-25 08:26:11.109629
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:26:24.601566
# Unit test for constructor of class NativeJinjaUnsafeText
def test_NativeJinjaUnsafeText():
    # wrap_var must add the unsafe marker *and* keep the native-jinja marker
    wrapped = wrap_var(NativeJinjaText('unsafe value'))

    assert type(wrapped) is NativeJinjaUnsafeText
    assert isinstance(wrapped, NativeJinjaText)
    assert isinstance(wrapped, AnsibleUnsafeText)
    assert isinstance(wrapped, AnsibleUnsafe)
    assert wrapped == 'unsafe value'

    # encode() inherited from AnsibleUnsafeText keeps unsafe context
    encoded = wrapped.encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'unsafe value'

    # decode() returns plain unsafe text, not the native-jinja subclass
    decoded = encoded.decode('utf-8')
    assert type(decoded) is AnsibleUnsafeText
    assert decoded == 'unsafe value'

    # already-unsafe values are returned unchanged (idempotent)
    assert wrap_var(wrapped) is wrapped

    # plain text gains unsafe but must NOT gain the native-jinja marker
    plain = wrap_var('plain')
    assert type(plain) is AnsibleUnsafeText
    assert not isinstance(plain, NativeJinjaText)

# Generated at 2026-10-25 08:26:27.026207
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 08:26:29.443122
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 08:26:31.861144
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 08:26:34.295615
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:36.714489
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:39.311537
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:41.727069
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:44.145497
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:46.562056
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:26:48.981486
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:26:51.576911
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:26:53.995580
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:26:56.449631
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:26:58.876532
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:27:01.298388
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:27:03.716525
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:27:06.136624
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-25 08:27:10.886503
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():value = b"hello world"

# Generated at 2026-10-25 08:27:12.422091
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:27:19.574536
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'hello \xe2\x98\x83')

    decoded = value.decode('utf-8')

    assert decoded == 'hello \u2603'
    assert isinstance(decoded, AnsibleUnsafeText)
    assert isinstance(decoded, AnsibleUnsafe)
    assert decoded.__UNSAFE__ is True

# Generated at 2026-10-25 08:27:26.926923
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("cafÃ©".encode("utf-8"))

    result = value.decode(encoding="utf-8")

    assert result == "cafÃ©"
    assert isinstance(result, AnsibleUnsafeText)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 08:27:32.162852
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes("hÃ©llo".encode("utf-8"))

    result = value.decode(encoding="utf-8")

    assert result == "hÃ©llo"
    assert isinstance(result, AnsibleUnsafeText)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 08:27:38.919833
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    unsafe_bytes = AnsibleUnsafeBytes(b'\xc3\xa9')
    result = unsafe_bytes.decode('utf-8')

    assert result == '\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)

# Generated at 2026-10-25 08:27:41.339894
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:43.758463
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:46.172616
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:48.588979
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:51.005055
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:53.423578
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:56.231935
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:27:58.649849
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:01.092784
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:03.554742
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:05.972964
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:08.390562
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:10.811654
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:13.246913
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:15.662670
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:18.084031
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:20.502854
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:22.921362
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:25.336336
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:27.855139
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:30.265111
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:32.682645
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:35.100011
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:37.521459
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:39.937157
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:42.354293
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:44.771979
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:47.188238
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:49.754117
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:52.096106
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:54.509102
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:56.928676
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:28:59.346752
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:00.920478
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:02.400572
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:03.831639
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:05.287285
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:06.682449
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:08.134017
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:09.567375
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:10.945908
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:12.412182
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:13.754518
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:15.201961
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:16.614053
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:18.012128
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:19.399216
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:21.239755
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:29:23.661264
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:26.077926
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:28.500075
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:30.915706
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:33.331887
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:35.747775
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:38.168687
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:40.612189
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:43.029414
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:45.446045
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:47.861240
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:50.276340
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:52.848301
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:55.123978
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:29:57.540196
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:00.073161
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:02.485113
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:04.901235
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:07.316401
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:15.204483
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy.__new__(UnsafeProxy, "hello")

# Generated at 2026-10-25 08:30:16.808444
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:18.141702
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:19.812197
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:21.251847
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:22.949645
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:24.318322
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:25.750979
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:27.398440
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:28.823122
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:30.241573
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:31.696242
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:33.142011
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:34.865210
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:36.196729
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:37.573373
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:38.961578
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:30:41.505625
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:44.029941
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:46.448626
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:50.178385
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:52.763853
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:55.180578
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:30:57.772647
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:00.189582
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:02.609366
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:05.027927
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:07.443973
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:09.862656
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:12.280604
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:23.109465
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():unsafe = AnsibleUnsafeText("already unsafe")

# Generated at 2026-10-25 08:31:24.535626
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:25.966299
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:27.325588
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:28.877321
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:30.366697
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:31.903913
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:38.611423
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:39.993086
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:41.529573
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:43.043793
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Already-unsafe values pass through unchanged (same object)
    already_unsafe = AnsibleUnsafeText(u'trusted')
    assert UnsafeProxy(already_unsafe) is already_unsafe

    already_unsafe_bytes = AnsibleUnsafeBytes(b'trusted')
    assert UnsafeProxy(already_unsafe_bytes) is already_unsafe_bytes

    # Text input is converted to AnsibleUnsafeText
    proxied = UnsafeProxy(u'some string')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert isinstance(proxied, text_type)
    assert proxied == u'some string'

    # Byte input is converted to text, then wrapped
    proxied = UnsafeProxy(b'some bytes')
    assert isinstance(proxied, AnsibleUnsafeText)
    assert proxied == u'some bytes'

    # Non-string values are returned untouched (not wrapped)
    for unchanged in (None, 1, 1.5, True, [u'list'], {u'dict': u'val'}, (u'tuple',)):
        assert UnsafeProxy(unchanged) is unchanged
        assert not isinstance(UnsafeProxy(unchanged), AnsibleUnsafe)


@patch('ansible.utils.unsafe_proxy.Display')
def test_UnsafeProxy___new___is_deprecated(mock_display):
    # UnsafeProxy emits a deprecation warning; wrap_var is the replacement
    UnsafeProxy(u'string')
    mock_display.return_value.deprecated.assert_called_once()

    # Replacement API: wrap_var produces the same unsafe types without deprecation
    assert isinstance(wrap_var(u'string'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'bytes'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([u'a']), list)
    assert isinstance(wrap_var([u'a'])[0], AnsibleUnsafeText)

# Generated at 2026-10-25 08:31:45.487674
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:47.905020
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:50.320277
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:52.736762
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:55.338334
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:31:57.754535
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:00.175423
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:02.591087
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:05.007631
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:07.430462
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:09.843910
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:12.258427
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:14.677475
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:17.135668
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:19.554507
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:21.968360
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:24.387348
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:32:26.805761
# Unit test for method __new__ of class UnsafeProxy