

# Generated at 2026-11-02 22:36:09.577289
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    assert isinstance(module_0.to_unsafe_text(u'foo'), AnsibleUnsafeText)
    assert isinstance(module_0.to_unsafe_text(u'foo'), AnsibleUnsafe)
    assert module_0.to_unsafe_text(u'foo') == u'foo'

    # bytes input should be converted to unsafe text
    assert isinstance(module_0.to_unsafe_text(b'foo'), AnsibleUnsafeText)
    assert module_0.to_unsafe_text(b'foo') == u'foo'

    # non-string input is converted via to_text
    assert isinstance(module_0.to_unsafe_text(1), AnsibleUnsafeText)
    assert module_0.to_unsafe_text(1) == u'1'

    # None passes through unchanged
    assert module_0.to_unsafe_text(None) is None

    # already unsafe text is returned unchanged
    unsafe = AnsibleUnsafeText(u'foo')
    assert module_0.to_unsafe_text(unsafe) is unsafe

# Generated at 2026-11-02 22:37:55.461221
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    from ansible.module_utils._text import to_bytes
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText, AnsibleUnsafe

    # Basic string conversion returns unsafe bytes
    res = module_0.to_unsafe_bytes(u'to_unsafe_bytes')
    assert isinstance(res, AnsibleUnsafeBytes)
    assert isinstance(res, AnsibleUnsafe)
    assert res == to_bytes(u'to_unsafe_bytes')
    assert res.__UNSAFE__ is True

    # Bytes input is wrapped as unsafe bytes
    res = module_0.to_unsafe_bytes(b'already_bytes')
    assert isinstance(res, AnsibleUnsafeBytes)
    assert res == b'already_bytes'

    # Unicode with non-ascii characters and explicit encoding
    res = module_0.to_unsafe_bytes(u'töst', encoding='utf-8')
    assert isinstance(res, AnsibleUnsafeBytes)
    assert res == to_bytes(u'töst', encoding='utf-8')

    # Passing kwargs through to to_bytes (errors handling)
    res = module_0.to_unsafe_bytes(u'to_unsafe_bytes', errors='surrogate_or_strict')
    assert isinstance(res, AnsibleUnsafeBytes)
    assert res == b'to_unsafe_bytes'

    # Decoding unsafe bytes should preserve unsafe context
    decoded = res.decode()
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'to_unsafe_bytes'

    # None input: to_bytes(None) produces b'' wrapped as unsafe
    res = module_0.to_unsafe_bytes(None)
    assert isinstance(res, AnsibleUnsafeBytes)

    # Numeric input is converted to bytes
    res = module_0.to_unsafe_bytes(1234)
    assert isinstance(res, AnsibleUnsafeBytes)
    assert res == b'1234'

    # Already unsafe values remain unsafe when re-wrapped
    already_unsafe = module_0.to_unsafe_bytes(u'unsafe_once')
    res = module_0.to_unsafe_bytes(already_unsafe)
    assert isinstance(res, AnsibleUnsafeBytes)
    assert res == already_unsafe

# Generated at 2026-11-02 22:39:44.416762
# Unit test for function wrap_var
def test_wrap_var():
    generator = None
    import pytest
    from ansible.utils.unsafe import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        NativeJinjaUnsafeText,
        wrap_var,
    )
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.six import binary_type, text_type
    try:
        from ansible.module_utils.common.text.converters import to_bytes, to_text
    except Exception:
        pass
    from ansible.utils.native_jinja import NativeJinjaText

    # None passthrough
    assert module_0.wrap_var(None) is None

    # Strings are wrapped
    assert isinstance(module_0.wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(module_0.wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert module_0.wrap_var(u'foo') == u'foo'
    assert module_0.wrap_var(b'foo') == b'foo'

    # Already unsafe values are returned unchanged (same object)
    unsafe_text = AnsibleUnsafeText(u'foo')
    assert module_0.wrap_var(unsafe_text) is unsafe_text
    unsafe_bytes = AnsibleUnsafeBytes(b'foo')
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Other scalars are returned unchanged
    assert module_0.wrap_var(1) == 1
    assert not isinstance(module_0.wrap_var(1), AnsibleUnsafe)
    assert module_0.wrap_var(1.5) == 1.5
    assert not isinstance(module_0.wrap_var(1.5), AnsibleUnsafe)
    assert module_0.wrap_var(True) is True
    assert not isinstance(module_0.wrap_var(True), AnsibleUnsafe)

    # Lists are wrapped recursively
    value = [u'foo', u'bar']
    result = module_0.wrap_var(value)
    assert isinstance(result, list)
    assert result == [u'foo', u'bar']
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)

    # Nested lists
    value = [[u'foo'], [u'bar']]
    result = module_0.wrap_var(value)
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result)
    assert all(isinstance(sub, AnsibleUnsafeText) for item in result for sub in item)

    # Tuples are wrapped recursively
    value = (u'foo', u'bar')
    result = module_0.wrap_var(value)
    assert isinstance(result, tuple)
    assert result == (u'foo', u'bar')
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)

    # Generators are not wrapped (not a concrete sequence type)
    def _gen():
        yield u'foo'
    assert not isinstance(module_0.wrap_var(_gen()), AnsibleUnsafe)

    # Dicts are wrapped, keys and values
    value = {u'foo': u'bar', u'baz': [u'qux']}
    result = module_0.wrap_var(value)
    assert isinstance(result, dict)
    assert result == {u'foo': u'bar', u'baz': [u'qux']}
    assert all(isinstance(k, AnsibleUnsafeText) for k in result)
    assert all(isinstance(v, AnsibleUnsafeText) for v in result.values())
    assert all(isinstance(sub, AnsibleUnsafeText) for v in result.values() if isinstance(v, list) for sub in v)

    # Sets are wrapped
    value = set([u'foo', u'bar'])
    result = module_0.wrap_var(value)
    assert isinstance(result, set)
    assert result == set([u'foo', u'bar'])
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)

    # NativeJinjaText becomes NativeJinjaUnsafeText
    value = NativeJinjaText(u'foo')
    result = module_0.wrap_var(value)
    assert isinstance(result, NativeJinjaUnsafeText)
    assert result == u'foo'

    # NativeJinjaText inside a container is preserved as unsafe native text
    value = [NativeJinjaText(u'foo')]
    result = module_0.wrap_var(value)
    assert isinstance(result[0], NativeJinjaUnsafeText)

    # Unsafe container elements
    value = [AnsibleUnsafeText(u'foo')]
    result = module_0.wrap_var(value)
    assert isinstance(result[0], AnsibleUnsafeText)

    value = {AnsibleUnsafeText(u'foo'): AnsibleUnsafeText(u'bar')}
    result = module_0.wrap_var(value)
    assert all(isinstance(k, AnsibleUnsafeText) and isinstance(v, AnsibleUnsafeText) for k, v in result.items())

    value = set([AnsibleUnsafeText(u'foo')])
    result = module_0.wrap_var(value)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)

    # Mixed nested structure
    value = {
        u'list': [u'foo', 1],
        u'dict': {u'key': u'value'},
        u'set': set([u'set_item']),
        u'text': u'text',
        u'bytes': b'bytes',
        u'none': None,
        u'int': 1,
        u'float': 1.5,
        u'bool': False,
    }
    result = module_0.wrap_var(value)
    assert isinstance(result, dict)
    assert all(isinstance(k, AnsibleUnsafeText) for k in result)
    assert isinstance(result[u'list'], list)
    assert isinstance(result[u'list'][0], AnsibleUnsafeText)
    assert result[u'list'][1] == 1
    assert not isinstance(result[u'list'][1], AnsibleUnsafe)
    assert isinstance(result[u'dict'], dict)
    assert isinstance(result[u'dict'][u'key'], AnsibleUnsafeText)
    assert isinstance(result[u'set'], set)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result[u'set'])
    assert isinstance(result[u'text'], AnsibleUnsafeText)
    assert isinstance(result[u'bytes'], AnsibleUnsafeBytes)
    assert result[u'none'] is None
    assert result[u'int'] == 1
    assert result[u'float'] == 1.5
    assert result[u'bool'] is False

    # Encoding/decoding preserves unsafe context
    unsafe = module_0.wrap_var(u'foo')
    encoded = unsafe.encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    decoded = encoded.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'foo'

    unsafe = module_0.wrap_var(b'foo')
    decoded = unsafe.decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'foo'

# Generated at 2026-11-02 22:40:55.276523
# Unit test for constructor of class NativeJinjaUnsafeText
def test_NativeJinjaUnsafeText():
    # Construction with a plain text value
    njut = NativeJinjaUnsafeText(u'foo')
    assert njut == u'foo'
    assert isinstance(njut, NativeJinjaUnsafeText)
    assert isinstance(njut, NativeJinjaText)
    assert isinstance(njut, AnsibleUnsafeText)
    assert isinstance(njut, AnsibleUnsafe)
    assert isinstance(njut, text_type)
    assert getattr(njut, '__UNSAFE__', False) is True

    # NativeJinjaText behavior is preserved (is_template defaults to False)
    assert njut.is_template is False

    # is_template keyword argument is honored
    template_text = NativeJinjaUnsafeText(u'{{ bar }}', is_template=True)
    assert template_text == u'{{ bar }}'
    assert template_text.is_template is True
    assert isinstance(template_text, AnsibleUnsafe)

    # Encoding maintains the unsafe context
    encoded = njut.encode('utf-8')
    assert encoded == b'foo'
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, AnsibleUnsafe)

    # Decoding the unsafe bytes returns unsafe text again
    decoded = encoded.decode('utf-8')
    assert decoded == u'foo'
    assert isinstance(decoded, AnsibleUnsafeText)
    assert isinstance(decoded, AnsibleUnsafe)

# Generated at 2026-11-02 22:43:05.222230
# Unit test for constructor of class NativeJinjaUnsafeText
def test_NativeJinjaUnsafeText():
    '''Constructor test for NativeJinjaUnsafeText'''
    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        NativeJinjaText,
        NativeJinjaUnsafeText,
    )

    # Construction from a plain string
    obj = NativeJinjaUnsafeText(u'test string')
    assert isinstance(obj, NativeJinjaUnsafeText)
    assert isinstance(obj, NativeJinjaText)
    assert isinstance(obj, AnsibleUnsafeText)
    assert isinstance(obj, AnsibleUnsafe)
    assert obj == u'test string'
    assert obj.__UNSAFE__ is True

    # Construction from an existing AnsibleUnsafeText
    unsafe_text = AnsibleUnsafeText(u'unsafe')
    obj2 = NativeJinjaUnsafeText(unsafe_text)
    assert isinstance(obj2, NativeJinjaUnsafeText)
    assert obj2 == u'unsafe'
    assert obj2.__UNSAFE__ is True

    # Construction from NativeJinjaText
    nj_text = NativeJinjaText(u'native')
    obj3 = NativeJinjaUnsafeText(nj_text)
    assert isinstance(obj3, NativeJinjaUnsafeText)
    assert isinstance(obj3, NativeJinjaText)
    assert obj3 == u'native'
    assert obj3.__UNSAFE__ is True

    # encode preserves unsafe context
    encoded = obj.encode()
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'test string'
    assert encoded.__UNSAFE__ is True

    # decode preserves unsafe context
    decoded = encoded.decode()
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == u'test string'
    assert decoded.__UNSAFE__ is True