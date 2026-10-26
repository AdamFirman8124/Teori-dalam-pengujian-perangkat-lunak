

# Generated at 2026-10-25 07:54:26.011047
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    s = AnsibleUnsafeText("hello world")
    assert isinstance(s, text_type)
    assert isinstance(s, AnsibleUnsafe)
    assert isinstance(s, AnsibleUnsafeText)
    assert s == "hello world"
    assert str(s) == "hello world"
    assert s.__UNSAFE__ is True
    empty = AnsibleUnsafeText("")
    assert empty == ""
    assert isinstance(empty, AnsibleUnsafeText)
    assert empty.__UNSAFE__ is True
    default = AnsibleUnsafeText()
    assert default == ""
    assert isinstance(default, AnsibleUnsafeText)
    uni = AnsibleUnsafeText(u"h\u00e9llo \U0001f30d")
    assert uni == u"h\u00e9llo \U0001f30d"
    assert isinstance(uni, AnsibleUnsafeText)
    copy = AnsibleUnsafeText(s)
    assert copy == s
    assert isinstance(copy, AnsibleUnsafeText)
    assert copy.__UNSAFE__ is True

# Generated at 2026-10-25 07:54:27.452687
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

# Generated at 2026-10-25 07:54:29.871977
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:32.438952
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:34.852314
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:37.383782
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-25 07:54:39.802511
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-25 07:54:42.219917
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-25 07:54:44.635272
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 07:54:47.046841
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 07:54:49.459644
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 07:54:51.876504
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:54.290580
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:56.707070
# Unit test for function wrap_var

# Generated at 2026-10-25 07:54:58.105789
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

# Generated at 2026-10-25 07:54:59.508564
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

# Generated at 2026-10-25 07:55:02.477023
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:03.823220
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:55:05.181188
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

# Generated at 2026-10-25 07:55:09.205869
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:11.623340
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:32.370872
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:35.248142
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:36.569454
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:55:39.139339
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:55:41.815347
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:55:44.230480
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:55:46.644160
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:49.062234
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:51.474950
# Unit test for function wrap_var

# Generated at 2026-10-25 07:55:53.890067
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:55:56.306320
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:01.766664
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.vars.unsafe_proxy import UnsafeProxy, AnsibleUnsafeText

    # String input is wrapped in AnsibleUnsafeText

# Generated at 2026-10-25 07:56:04.635509
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:06.063041
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:07.447988
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

# Generated at 2026-10-25 07:56:08.832113
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

# Generated at 2026-10-25 07:56:11.625484
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:13.029694
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:16.103282
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:17.438371
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:20.213132
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:21.557022
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:24.397665
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:25.721444
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:28.498503
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:29.853094
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:56:32.384386
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:34.901711
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:37.451721
# Unit test for function wrap_var

# Generated at 2026-10-25 07:56:39.867985
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:42.505953
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:44.919425
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:47.335228
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:49.753101
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:52.164660
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:54.582422
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:56.998725
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:56:59.421291
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:01.836264
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:04.246961
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:06.662294
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:09.077715
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:11.492190
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:13.904677
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:16.319475
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:19.080698
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:20.496266
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:57:23.315494
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:24.650800
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:57:27.369941
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:28.705188
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:57:31.461606
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:32.796499
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:57:34.235403
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

# Generated at 2026-10-25 07:57:36.980216
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:39.554377
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:42.119346
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:44.536659
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:46.951841
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:49.368305
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:57:51.783839
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:54.438154
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:56.851643
# Unit test for function wrap_var

# Generated at 2026-10-25 07:57:59.265753
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:01.681312
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:04.158662
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:06.572005
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:08.985831
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:11.468404
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:13.937061
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:16.352339
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:18.766160
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:58:21.181771
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:23.595197
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:26.008781
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:29.223524
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:30.550660
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:58:31.988432
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

# Generated at 2026-10-25 07:58:33.316403
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

# Generated at 2026-10-25 07:58:34.753286
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

# Generated at 2026-10-25 07:58:37.530445
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:38.871716
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:58:40.273240
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

# Generated at 2026-10-25 07:58:41.724445
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

# Generated at 2026-10-25 07:58:43.149425
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

# Generated at 2026-10-25 07:58:44.591312
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

# Generated at 2026-10-25 07:58:45.913847
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

# Generated at 2026-10-25 07:58:47.301583
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

# Generated at 2026-10-25 07:58:48.634426
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

# Generated at 2026-10-25 07:58:51.447005
# Unit test for function wrap_var

# Generated at 2026-10-25 07:58:52.792719
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 07:58:54.213936
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

# Generated at 2026-10-25 07:58:55.545703
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

# Generated at 2026-10-25 07:58:58.235242
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:00.803360
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:03.216014
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:05.823087
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:08.241564
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:10.654162
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:13.068794
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:15.666166
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:18.136519
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:20.532100
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:22.947680
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:25.573173
# Unit test for function wrap_var

# Generated at 2026-10-25 07:59:27.987825
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:30.402986
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:32.814851
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:35.228029
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:37.642622
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:40.054809
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:42.468434
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:44.882480
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:47.303703
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:49.717342
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:52.134465
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:54.547768
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:56.964829
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 07:59:59.379005
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:01.793171
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:04.269057
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:06.683026
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:09.095558
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:11.546553
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:13.958783
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:16.373421
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:18.788274
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:21.206017
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:23.626648
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:26.032616
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:28.921081
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.vars.unsafe_proxy import UnsafeProxy, AnsibleUnsafeText

    # String input is wrapped in AnsibleUnsafeText

# Generated at 2026-10-25 08:00:30.482499
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

# Generated at 2026-10-25 08:00:31.899605
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

# Generated at 2026-10-25 08:00:33.332870
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

# Generated at 2026-10-25 08:00:34.698251
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

# Generated at 2026-10-25 08:00:36.081023
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

# Generated at 2026-10-25 08:00:37.531018
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

# Generated at 2026-10-25 08:00:39.950774
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

# Generated at 2026-10-25 08:00:41.319938
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

# Generated at 2026-10-25 08:00:42.754727
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

# Generated at 2026-10-25 08:00:44.150058
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

# Generated at 2026-10-25 08:00:45.622577
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

# Generated at 2026-10-25 08:00:47.053791
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

# Generated at 2026-10-25 08:00:48.488186
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

# Generated at 2026-10-25 08:00:51.355898
# Unit test for function wrap_var

# Generated at 2026-10-25 08:00:52.787770
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:00:55.321450
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:00:57.737175
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:00.152208
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:02.567361
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:04.981361
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:07.395753
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:13.720992
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:16.137290
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:18.551853
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:20.966603
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:23.380795
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:25.794967
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:28.210824
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:30.626365
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:33.037239
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:35.450757
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:37.865491
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:40.279705
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:42.693620
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:45.107073
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:47.522572
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:49.938267
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:01:52.353867
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 08:02:00.068629
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("example")

# Generated at 2026-10-25 08:02:01.602177
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

# Generated at 2026-10-25 08:02:02.944640
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

# Generated at 2026-10-25 08:02:04.366401
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

# Generated at 2026-10-25 08:02:07.144447
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:08.564697
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:02:24.030292
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:26.445104
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:28.859337
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:31.273057
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:33.687106
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:36.101364
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:38.515392
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:40.930751
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:43.348588
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:45.766965
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:48.180278
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:50.594246
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:53.008549
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:55.422991
# Unit test for function wrap_var

# Generated at 2026-10-25 08:02:56.999109
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:02:59.868041
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:01.416603
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:03:04.375417
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:05.807095
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:03:08.777227
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:10.209617
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:03:13.077948
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:14.446200
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:03:17.279000
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:18.709363
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2

# Generated at 2026-10-25 08:03:46.462305
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:49.000686
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:51.575848
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:54.010047
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:56.422511
# Unit test for function wrap_var

# Generated at 2026-10-25 08:03:58.035309
# Unit test for function wrap_var
def test_wrap_var():from ansible.module_utils.six import PY2