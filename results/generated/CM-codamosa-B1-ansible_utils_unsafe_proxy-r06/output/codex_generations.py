

# Generated at 2026-10-25 14:12:57.294068
# Unit test for constructor of class AnsibleUnsafeText
def test_AnsibleUnsafeText():
    # basic construction preserves value
    v = AnsibleUnsafeText(u'hello')
    assert v == u'hello'
    assert str(v) == 'hello'

    # is marked unsafe and is a text type
    assert isinstance(v, str)
    assert isinstance(v, AnsibleUnsafe)
    assert v.__UNSAFE__ is True
    assert type(v) is AnsibleUnsafeText

    # empty / no-arg construction behaves like str
    assert AnsibleUnsafeText() == ''
    assert isinstance(AnsibleUnsafeText(), AnsibleUnsafeText)
    assert AnsibleUnsafeText(u'') == u''

    # unicode and special characters preserved
    u_str = u'hÃ©llo wÃ¶rld \U0001F600'
    assert AnsibleUnsafeText(u_str) == u_str

    # str-compatible coercion, still unsafe
    assert AnsibleUnsafeText(123) == '123'
    assert isinstance(AnsibleUnsafeText(123), AnsibleUnsafe)

    # re-wrapping an unsafe value stays unsafe
    assert isinstance(AnsibleUnsafeText(v), AnsibleUnsafeText)
    assert AnsibleUnsafeText(v) == 'hello'

    # unsafe context is preserved through encode()
    assert isinstance(v.encode('utf-8'), AnsibleUnsafeBytes)

# Generated at 2026-10-25 14:13:04.616336
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    result = module_0.to_unsafe_text(b'hello')

    assert result == u'hello'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, text_type)

# Generated at 2026-10-25 14:13:20.372901
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 14:13:24.980864
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():obj = AnsibleUnsafe()

# Generated at 2026-10-25 14:13:36.255382
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:13:37.994175
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("hello")

# Generated at 2026-10-25 14:13:46.072784
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():
    value = AnsibleUnsafeBytes(b'\xc3\xa9')
    result = value.decode(encoding='utf-8', errors='strict')

    assert result == '\u00e9'
    assert isinstance(result, AnsibleUnsafeText)
    assert result.__UNSAFE__ is True

# Generated at 2026-10-25 14:13:54.994692
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:14:02.877955
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("hello")

# Generated at 2026-10-25 14:14:29.399700
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch
    from ansible.utils.display import Display

    with patch.object(Display, 'deprecated') as deprecated:
        unsafe_value = AnsibleUnsafeText('already unsafe')
        assert UnsafeProxy(unsafe_value) is unsafe_value

        text_value = text_type('plain text')
        proxied_value = UnsafeProxy(text_value)
        assert isinstance(proxied_value, AnsibleUnsafeText)
        assert proxied_value == text_value

        non_string_value = object()
        assert UnsafeProxy(non_string_value) is non_string_value

        assert deprecated.call_count == 3
        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

# Generated at 2026-10-25 14:14:57.765588
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.unsafe_proxy import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        NativeJinjaUnsafeText,
        wrap_var,
    )
    from ansible.utils.native_jinja import NativeJinjaText

    # None passes through untouched
    assert module_0.wrap_var(None) is None

    # Already-unsafe values are returned as the same object (no double wrapping)
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = AnsibleUnsafeBytes(b'foo')
    assert module_0.wrap_var(unsafe_text) is unsafe_text
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Plain text -> AnsibleUnsafeText
    result = module_0.wrap_var(u'foo')
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'foo'
    assert type(result) is AnsibleUnsafeText

    # Plain bytes -> AnsibleUnsafeBytes
    result = module_0.wrap_var(b'foo')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'foo'
    assert type(result) is AnsibleUnsafeBytes

    # NativeJinjaText -> NativeJinjaUnsafeText (and stays a NativeJinjaText)
    result = module_0.wrap_var(NativeJinjaText(u'foo'))
    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, NativeJinjaText)
    assert result == u'foo'

    # Non-string, non-container values are returned unchanged
    for value in (1, 1.5, True, False, object()):
        assert module_0.wrap_var(value) is value

    # dict: keys and values are both wrapped, original is not mutated
    original = {u'key': u'value'}
    result = module_0.wrap_var(original)
    assert result is not original
    assert original == {u'key': u'value'}
    assert type(original[u'key']) is type(u'')
    (key, value), = result.items()
    assert isinstance(key, AnsibleUnsafeText)
    assert isinstance(value, AnsibleUnsafeText)
    assert key == u'key'
    assert value == u'value'

    # list: wrapped in place-preserving order, type preserved
    result = module_0.wrap_var([u'a', u'b'])
    assert type(result) is list
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert result == [u'a', u'b']

    # tuple: type preserved
    result = module_0.wrap_var((u'a', u'b'))
    assert type(result) is tuple
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert result == (u'a', u'b')

    # set: items wrapped, still hashable and comparable
    result = module_0.wrap_var({u'a', u'b'})
    assert type(result) is set
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert result == {u'a', u'b'}

    # deeply nested structures are fully wrapped
    result = module_0.wrap_var({u'k': [u'a', (b'b', {u'c': u'd'})]})
    assert isinstance(result, dict)
    key = next(iter(result))
    assert isinstance(key, AnsibleUnsafeText)
    inner_list = result[key]
    assert type(inner_list) is list
    assert isinstance(inner_list[0], AnsibleUnsafeText)
    inner_tuple = inner_list[1]
    assert type(inner_tuple) is tuple
    assert isinstance(inner_tuple[0], AnsibleUnsafeBytes)
    inner_dict = inner_tuple[1]
    assert isinstance(inner_dict, dict)
    (inner_key, inner_value), = inner_dict.items()
    assert isinstance(inner_key, AnsibleUnsafeText)
    assert isinstance(inner_value, AnsibleUnsafeText)
    assert inner_value == u'd'

    # type conversions on unsafe strings keep the unsafe context
    encoded = module_0.wrap_var(u'foo').encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'foo'
    decoded = encoded.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'foo'

    # mixed-type containers: only strings/bytes get wrapped
    result = module_0.wrap_var([1, u'a', b'b', None])
    assert result[0] == 1
    assert type(result[0]) is int
    assert isinstance(result[1], AnsibleUnsafeText)
    assert isinstance(result[2], AnsibleUnsafeBytes)
    assert result[3] is None

# Generated at 2026-10-25 14:15:17.630359
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch

    from ansible.module_utils.six import string_types
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        UnsafeProxy,
    )

    with patch('ansible.utils.display.Display') as MockDisplay:
        # 1. plain text -> AnsibleUnsafeText
        res = UnsafeProxy(u'hello')
        assert isinstance(res, AnsibleUnsafeText)
        assert res == u'hello'
        # deprecation is emitted on every call
        assert MockDisplay.return_value.deprecated.called
        args, kwargs = MockDisplay.return_value.deprecated.call_args
        assert 'UnsafeProxy is being deprecated' in args[0]
        assert kwargs == {'version': '2.13', 'collection_name': 'ansible.builtin'}

        MockDisplay.reset_mock()

        # 2. empty text string
        res = UnsafeProxy(u'')
        assert isinstance(res, AnsibleUnsafeText)
        assert res == u''

        # 3. AnsibleUnsafe instances are returned unchanged (same object)
        for unsafe_obj in [
            AnsibleUnsafe(),
            AnsibleUnsafeText(u'already unsafe'),
            AnsibleUnsafeBytes(b'already unsafe'),
        ]:
            MockDisplay.reset_mock()
            res = UnsafeProxy(unsafe_obj)
            assert res is unsafe_obj
            assert MockDisplay.return_value.deprecated.called

        # 4. non-string, non-unsafe types are returned unchanged
        for obj in [None, 42, 3.14, True, ['a'], ('a',), {'a': 1}, object()]:
            res = UnsafeProxy(obj)
            assert res is obj

        # 5. bytes behaviour follows `string_types` check (py3: bytes is not wrapped)
        b = b'bytes input'
        res = UnsafeProxy(b)
        if isinstance(b, string_types):
            assert isinstance(res, AnsibleUnsafeText)
        else:
            assert res is b

# Generated at 2026-10-25 14:15:20.324879
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:22.916641
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:25.330721
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:27.919648
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:30.337976
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:32.756023
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:35.248711
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:37.620763
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:40.036121
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:42.449850
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:43.978567
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("hello")

# Generated at 2026-10-25 14:15:52.447053
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 14:15:53.879706
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():result = UnsafeProxy("hello")

# Generated at 2026-10-25 14:16:09.445291
# Unit test for function wrap_var
def test_wrap_var():assert module_0.wrap_var(None) is None
