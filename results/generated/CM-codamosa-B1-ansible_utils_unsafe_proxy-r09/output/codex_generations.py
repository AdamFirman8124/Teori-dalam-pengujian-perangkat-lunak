

# Generated at 2026-10-25 10:44:08.076850
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:44:10.625860
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:13.039886
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:15.457106
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:18.132106
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:20.794415
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:23.208749
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:44:25.623969
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 10:44:28.039692
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 10:44:30.455145
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-25 10:44:32.872115
# Unit test for function wrap_var

# Generated at 2026-10-25 10:44:35.286807
# Unit test for function wrap_var

# Generated at 2026-10-25 10:44:37.700886
# Unit test for function wrap_var

# Generated at 2026-10-25 10:44:40.116949
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:44:47.948594
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():v = AnsibleUnsafeText(u'hello')

# Generated at 2026-10-25 10:44:50.405879
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:44:51.847099
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:44:53.252534
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:44:54.580568
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:44:55.913498
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:44:57.371738
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:44:58.804421
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:45:01.828866
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:45:03.219241
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:45:04.672594
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:45:06.165038
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

# Generated at 2026-10-25 10:45:07.833960
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

# Generated at 2026-10-25 10:45:10.239752
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:45:13.001148
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:15.420472
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:17.838819
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:20.254551
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:45:22.906057
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:45:25.638803
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:45:28.053144
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:30.467851
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:32.886932
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:35.300543
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:37.716818
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:40.132221
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:45:46.296699
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.module_utils.six import binary_type
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # Encoding a plain unsafe text should return unsafe bytes
    unsafe_text = AnsibleUnsafeText(u'test string')
    result = unsafe_text.encode('utf-8')
    assert isinstance(result, binary_type)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'test string'
    assert result.__UNSAFE__ is True

    # Encoding with explicit args/kwargs should preserve unsafe context
    result2 = unsafe_text.encode(encoding='utf-8', errors='strict')
    assert isinstance(result2, AnsibleUnsafeBytes)
    assert result2 == b'test string'

    # Non-ascii content round-trips through encode while staying unsafe
    unsafe_unicode = AnsibleUnsafeText(u'caf\u00e9')
    result3 = unsafe_unicode.encode('utf-8')
    assert isinstance(result3, AnsibleUnsafeBytes)
    assert result3 == u'caf\u00e9'.encode('utf-8')

    # Decoding the unsafe bytes keeps the unsafe context (chained conversion)
    decoded = result3.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert isinstance(decoded, AnsibleUnsafe)
    assert decoded == u'caf\u00e9'

# Generated at 2026-10-25 10:45:47.829965
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:45:49.203877
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:04.135767
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

# Generated at 2026-10-25 10:46:05.498448
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:08.537990
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:09.974802
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:25.130365
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

# Generated at 2026-10-25 10:46:26.665234
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:28.191475
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:29.642248
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:31.191002
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe

    # module_0.encode() must return bytes that retain the unsafe marker
    unsafe_text = AnsibleUnsafeText(u'tÃ¶ encode')
    result = unsafe_text.encode('utf-8')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == u'tÃ¶ encode'.encode('utf-8')

    # default args (utf-8) also work
    assert isinstance(unsafe_text.encode(), AnsibleUnsafeBytes)

    # decode() round-trip keeps unsafe context too
    decoded = result.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'tÃ¶ encode'

# Generated at 2026-10-25 10:46:37.041517
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:38.582625
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:39.977371
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:43.151489
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:44.690140
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:46.121906
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:47.463773
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:48.861486
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:50.216271
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:52.898286
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:54.420041
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:55.756933
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:57.109021
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:46:58.614382
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:00.151646
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:01.991685
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:03.384955
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:04.962843
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:06.395928
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:07.828693
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:10.287216
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:11.822955
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:13.380834
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:14.792775
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:16.313070
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:17.715855
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, text_type, binary_type

    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Already-unsafe values pass through unchanged (no re-wrapping)
    already_unsafe = AnsibleUnsafeText('already unsafe')
    assert module_0.wrap_var(already_unsafe) is already_unsafe
    already_unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(already_unsafe_bytes) is already_unsafe_bytes

    # Text is wrapped in AnsibleUnsafeText
    wrapped_text = module_0.wrap_var(u'text value')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert isinstance(wrapped_text, text_type)
    assert wrapped_text == u'text value'
    assert getattr(wrapped_text, '__UNSAFE__', False) is True

    # Bytes are wrapped in AnsibleUnsafeBytes
    wrapped_bytes = module_0.wrap_var(b'byte value')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes, binary_type)
    assert wrapped_bytes == b'byte value'
    assert getattr(wrapped_bytes, '__UNSAFE__', False) is True

    # Dicts: keys and values are both wrapped
    wrapped_dict = module_0.wrap_var({u'key': u'value'})
    assert isinstance(wrapped_dict, dict)
    for k, v in wrapped_dict.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
    assert wrapped_dict[u'key'] == u'value'

    # Nested dict: recursion wraps inner containers too
    nested = module_0.wrap_var({u'outer': {u'inner': u'leaf'}})
    inner = nested[u'outer']
    assert isinstance(inner, dict)
    for v in inner.values():
        assert isinstance(v, AnsibleUnsafeText)

    # Lists and tuples: sequence type is preserved, items wrapped
    wrapped_list = module_0.wrap_var([u'a', u'b'])
    assert isinstance(wrapped_list, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)

    wrapped_tuple = module_0.wrap_var((u'a', u'b'))
    assert isinstance(wrapped_tuple, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)

    # Nested sequence inside dict
    nested_seq = module_0.wrap_var({u'list': [u'a', u'b']})
    assert isinstance(nested_seq[u'list'], list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in nested_seq[u'list'])

    # Sets: items are wrapped
    wrapped_set = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(wrapped_set, set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_set)

    # NativeJinjaText is wrapped as NativeJinjaUnsafeText
    njt = NativeJinjaText(u'{{ template }}')
    wrapped_njt = module_0.wrap_var(njt)
    assert isinstance(wrapped_njt, NativeJinjaUnsafeText)
    assert isinstance(wrapped_njt, NativeJinjaText)
    assert isinstance(wrapped_njt, AnsibleUnsafeText)
    assert wrapped_njt == u'{{ template }}'

    # Conversion helpers
    assert isinstance(to_unsafe_bytes(u'x'), AnsibleUnsafeBytes)
    assert isinstance(to_unsafe_text(b'x'), AnsibleUnsafeText)

    # Mixed container with None values: None items stay None
    mixed = module_0.wrap_var({u'k': None})
    assert mixed[u'k'] is None

    print('test_wrap_var passed')


if __name__ == '__main__':
    test_wrap_var()

# Generated at 2026-10-25 10:47:20.430967
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:22.847922
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:25.720328
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:28.139954
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:30.553053
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:32.970869
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:35.507082
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:37.846786
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:40.262858
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:43.068822
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:45.479952
# Unit test for function wrap_var

# Generated at 2026-10-25 10:47:47.894233
# Unit test for function wrap_var