

# Generated at 2026-10-25 10:58:53.847638
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 10:58:56.426918
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 10:58:58.844309
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-25 10:59:01.261956
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:03.674607
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:06.088204
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:08.503086
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:10.920109
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:13.333382
# Unit test for constructor of class NativeJinjaUnsafeText

# Generated at 2026-10-25 10:59:15.747826
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 10:59:18.248456
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 10:59:20.666484
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-25 10:59:23.077804
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-25 10:59:31.372251
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText

# Generated at 2026-10-25 10:59:32.881412
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

# Generated at 2026-10-25 10:59:34.325970
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

# Generated at 2026-10-25 10:59:35.671090
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

# Generated at 2026-10-25 10:59:37.018356
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

# Generated at 2026-10-25 10:59:38.380867
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

# Generated at 2026-10-25 10:59:39.756085
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

# Generated at 2026-10-25 10:59:42.728596
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

# Generated at 2026-10-25 10:59:44.111581
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

# Generated at 2026-10-25 10:59:46.258221
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

# Generated at 2026-10-25 10:59:49.109955
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

# Generated at 2026-10-25 10:59:50.468991
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

# Generated at 2026-10-25 10:59:52.885700
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:59:55.302969
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 10:59:57.720458
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:00.188892
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:02.560552
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:04.975961
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:07.390576
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:09.803929
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:12.222595
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:14.635412
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:17.049945
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:19.464250
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:22.374904
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:24.795337
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:27.213504
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:29.640104
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:32.054901
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:34.471259
# Unit test for function wrap_var

# Generated at 2026-10-25 11:00:36.884598
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:39.299559
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:41.715128
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:44.131226
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:46.544103
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:48.959518
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:51.375988
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:53.792722
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:56.208328
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:00:58.622969
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:01.122702
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:03.533764
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:05.947189
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:08.361019
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:10.774527
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:13.186725
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:15.600636
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:18.014639
# Unit test for function wrap_var

# Generated at 2026-10-25 11:01:20.431420
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:22.847187
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:25.263636
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:27.756368
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:30.134448
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:32.548973
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:34.967528
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:37.383719
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:39.795107
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:42.211809
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:44.624569
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:47.038684
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:49.450787
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:51.870801
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:54.283187
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:56.698359
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:01:59.112075
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:02:01.530607
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:02:03.949312
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:02:06.363291
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-25 11:02:08.776803
# Unit test for method __new__ of class UnsafeProxy