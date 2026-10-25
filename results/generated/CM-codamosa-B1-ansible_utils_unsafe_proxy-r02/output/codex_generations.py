

# Generated at 2026-10-24 06:32:30.464775
# Unit test for constructor of class UnsafeProxy
def test_UnsafeProxy():value = text_type('unsafe')

# Generated at 2026-10-24 06:32:31.777691
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

# Generated at 2026-10-24 06:32:36.402661
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    unsafe = AnsibleUnsafe()

    assert isinstance(unsafe, AnsibleUnsafe)
    assert unsafe.__UNSAFE__ is True

# Generated at 2026-10-24 06:32:49.828863
# Unit test for function wrap_var
def test_wrap_var():
    # None and already unsafe values are returned unchanged.
    assert module_0.wrap_var(None) is None

    unsafe_text = AnsibleUnsafeText('already unsafe')
    unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
    assert module_0.wrap_var(unsafe_text) is unsafe_text
    assert module_0.wrap_var(unsafe_bytes) is unsafe_bytes

    # Scalar strings are wrapped with the appropriate unsafe type.
    wrapped_text = module_0.wrap_var('text')
    assert isinstance(wrapped_text, AnsibleUnsafeText)
    assert wrapped_text == 'text'

    wrapped_bytes = module_0.wrap_var(b'bytes')
    assert isinstance(wrapped_bytes, AnsibleUnsafeBytes)
    assert wrapped_bytes == b'bytes'

    native_text = NativeJinjaText('native')
    wrapped_native = module_0.wrap_var(native_text)
    assert isinstance(wrapped_native, NativeJinjaUnsafeText)
    assert wrapped_native == native_text

    # Conversions retain the unsafe marker.
    assert isinstance(wrapped_text.encode(), AnsibleUnsafeBytes)
    assert isinstance(wrapped_bytes.decode(), AnsibleUnsafeText)

    # Containers are preserved and recursively wrapped.
    wrapped_list = module_0.wrap_var(['text', b'bytes', 42, None])
    assert type(wrapped_list) is list
    assert isinstance(wrapped_list[0], AnsibleUnsafeText)
    assert isinstance(wrapped_list[1], AnsibleUnsafeBytes)
    assert wrapped_list[2] == 42
    assert wrapped_list[3] is None

    wrapped_tuple = module_0.wrap_var(('text', b'bytes'))
    assert type(wrapped_tuple) is tuple
    assert isinstance(wrapped_tuple[0], AnsibleUnsafeText)
    assert isinstance(wrapped_tuple[1], AnsibleUnsafeBytes)

    wrapped_set = module_0.wrap_var({'text'})
    assert type(wrapped_set) is set
    assert len(wrapped_set) == 1
    assert isinstance(next(iter(wrapped_set)), AnsibleUnsafeText)

    wrapped_dict = module_0.wrap_var({'key': ['value', b'data']})
    assert type(wrapped_dict) is dict

    wrapped_key = next(iter(wrapped_dict))
    assert isinstance(wrapped_key, AnsibleUnsafeText)
    assert isinstance(wrapped_dict[wrapped_key][0], AnsibleUnsafeText)
    assert isinstance(wrapped_dict[wrapped_key][1], AnsibleUnsafeBytes)

    # Unsupported scalar types remain unchanged.
    marker = object()
    assert module_0.wrap_var(marker) is marker
    assert module_0.wrap_var(123) == 123

# Generated at 2026-10-24 06:33:09.483102
# Unit test for constructor of class NativeJinjaUnsafeText
def test_NativeJinjaUnsafeText():
    from ansible.module_utils.six import text_type
    from ansible.utils.native_jinja import NativeJinjaText

    value = u'some jinja text'
    obj = NativeJinjaUnsafeText(value)

    # Constructor stores the value correctly
    assert obj == value
    assert str(obj) == value

    # Correct type inheritance
    assert isinstance(obj, NativeJinjaUnsafeText)
    assert isinstance(obj, NativeJinjaText)
    assert isinstance(obj, AnsibleUnsafeText)
    assert isinstance(obj, text_type)
    assert isinstance(obj, AnsibleUnsafe)

    # Marked as unsafe
    assert obj.__UNSAFE__ is True

    # Type conversions preserve the unsafe context
    encoded = obj.encode()
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded.__UNSAFE__ is True
    assert encoded.decode() == value
    assert isinstance(encoded.decode(), AnsibleUnsafeText)

# Generated at 2026-10-24 06:33:27.178975
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:29.700817
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:32.115953
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:34.530161
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:36.946935
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:39.360047
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:33:56.993490
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:34:03.983866
# Unit test for function to_unsafe_text
def test_to_unsafe_text():from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, to_unsafe_text

# Generated at 2026-10-24 06:34:17.076642
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = unsafe_text.encode('utf-8')

    # encodes to the expected bytes
    assert unsafe_bytes == b'foo'

    # the unsafe marker survives the encode
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes.__UNSAFE__ is True

    # ...and survives the round trip back to text
    round_tripped = unsafe_bytes.decode('utf-8')
    assert round_tripped == u'foo'
    assert isinstance(round_tripped, AnsibleUnsafeText)

# Generated at 2026-10-24 06:34:18.678223
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = unsafe_text.encode('utf-8')

    # encodes to the expected bytes
    assert unsafe_bytes == b'foo'

    # the unsafe marker survives the encode
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes.__UNSAFE__ is True

    # ...and survives the round trip back to text
    round_tripped = unsafe_bytes.decode('utf-8')
    assert round_tripped == u'foo'
    assert isinstance(round_tripped, AnsibleUnsafeText)

# Generated at 2026-10-24 06:34:43.483319
# Unit test for function to_unsafe_bytes
def test_to_unsafe_bytes():
    from ansible.module_utils._text import to_bytes

    # basic case: returns AnsibleUnsafeBytes with correct value
    result = module_0.to_unsafe_bytes('foo')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'foo'
    assert result.__UNSAFE__ is True

    # encoding kwargs are passed through to to_bytes
    result = module_0.to_unsafe_bytes(u'fÃ¶Ã¶', encoding='utf-8')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == to_bytes(u'fÃ¶Ã¶', encoding='utf-8')

    # already-unsafe bytes are returned as-is (same object)
    unsafe = AnsibleUnsafeBytes(b'bar')
    assert module_0.to_unsafe_bytes(unsafe) is unsafe

    # decode() keeps the unsafe context
    result = module_0.to_unsafe_bytes('baz').decode()
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'baz'
    assert result.__UNSAFE__ is True

    # non-string input is passed through wrap_var untouched
    assert module_0.to_unsafe_bytes(None) is None

# Generated at 2026-10-24 06:34:44.805682
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = unsafe_text.encode('utf-8')

    # encodes to the expected bytes
    assert unsafe_bytes == b'foo'

    # the unsafe marker survives the encode
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes.__UNSAFE__ is True

    # ...and survives the round trip back to text
    round_tripped = unsafe_bytes.decode('utf-8')
    assert round_tripped == u'foo'
    assert isinstance(round_tripped, AnsibleUnsafeText)

# Generated at 2026-10-24 06:34:55.361936
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 06:35:02.211094
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():from ansible.module_utils.common.text.converters import to_bytes


# Generated at 2026-10-24 06:35:03.542169
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 06:35:04.855715
# Unit test for method decode of class AnsibleUnsafeBytes
def test_AnsibleUnsafeBytes_decode():from ansible.module_utils.common.text.converters import to_bytes


# Generated at 2026-10-24 06:35:21.575197
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

# Generated at 2026-10-24 06:35:23.990576
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:35:26.404099
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:35:28.819900
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:35:31.234731
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:35:33.648783
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:35:36.062984
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:35:38.478344
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:35:40.894515
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 06:35:52.142147
# Unit test for function to_unsafe_text
def test_to_unsafe_text():result = module_0.to_unsafe_text(u'unsafe value')

# Generated at 2026-10-24 06:36:00.375349
# Unit test for function to_unsafe_text
def test_to_unsafe_text():
    from ansible.module_utils._text import to_text

    # Plain text input becomes unsafe text
    result = module_0.to_unsafe_text('foo')
    assert isinstance(result, AnsibleUnsafeText)
    assert result == 'foo'
    assert hasattr(result, '__UNSAFE__')
    assert result.__UNSAFE__ is True

    # Bytes input is converted to unsafe text
    result = to_unsafe_bytes(b'bar')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'bar'
    assert hasattr(result, '__UNSAFE__')

    # Encoding unsafe text keeps the unsafe context
    encoded = result.decode().encode('utf-8')
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert encoded == b'bar'

    # Decoding unsafe bytes keeps the unsafe context
    decoded = to_unsafe_bytes('baz').decode('utf-8')
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == 'baz'

    # Already-unsafe values pass through unchanged (same object)
    already = AnsibleUnsafeText('safe-check')
    assert module_0.to_unsafe_text(already) is already

    # Keyword arguments are forwarded (encoding/errors)
    result = module_0.to_unsafe_text('qux', encoding='utf-8', errors='strict')
    assert isinstance(result, AnsibleUnsafeText)
    assert result == 'qux'

# Generated at 2026-10-24 06:36:01.712044
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = unsafe_text.encode('utf-8')

    # encodes to the expected bytes
    assert unsafe_bytes == b'foo'

    # the unsafe marker survives the encode
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes.__UNSAFE__ is True

    # ...and survives the round trip back to text
    round_tripped = unsafe_bytes.decode('utf-8')
    assert round_tripped == u'foo'
    assert isinstance(round_tripped, AnsibleUnsafeText)

# Generated at 2026-10-24 06:36:03.078466
# Unit test for method encode of class AnsibleUnsafeText
def test_AnsibleUnsafeText_encode():
    unsafe_text = AnsibleUnsafeText(u'foo')
    unsafe_bytes = unsafe_text.encode('utf-8')

    # encodes to the expected bytes
    assert unsafe_bytes == b'foo'

    # the unsafe marker survives the encode
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert unsafe_bytes.__UNSAFE__ is True

    # ...and survives the round trip back to text
    round_tripped = unsafe_bytes.decode('utf-8')
    assert round_tripped == u'foo'
    assert isinstance(round_tripped, AnsibleUnsafeText)

# Generated at 2026-10-24 06:36:20.772708
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:23.189215
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:25.745313
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:28.159729
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:36:30.573747
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:36:32.988614
# Unit test for method encode of class AnsibleUnsafeText

# Generated at 2026-10-24 06:36:35.403432
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:37.819517
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:40.235050
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:42.648083
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:45.061086
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:47.476704
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:49.890913
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:52.303314
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:54.718360
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:57.133334
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:36:59.547923
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:01.971844
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:04.376566
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:05.822759
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:37:41.454333
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:43.870856
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:46.421686
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:48.836563
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:51.252186
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:37:53.679165
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:07.619299
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:09.305685
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:38:27.007289
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:29.422838
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:31.838929
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:34.255845
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:36.668067
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:39.082128
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:41.497113
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:43.912949
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:46.332627
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:48.748698
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:51.168203
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:53.581117
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:55.994647
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:38:58.408674
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:00.842776
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:03.260793
# Unit test for function wrap_var

# Generated at 2026-10-24 06:39:05.671633
# Unit test for function wrap_var

# Generated at 2026-10-24 06:39:08.086589
# Unit test for function wrap_var

# Generated at 2026-10-24 06:39:10.501307
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:12.918749
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:15.331419
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:17.745535
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:20.160763
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:22.575927
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:24.989280
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:27.402381
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:29.814486
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:32.238324
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:34.647133
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:37.059214
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:39.724021
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:39:41.171754
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:39:59.060601
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:40:00.519265
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:40:18.315021
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:40:19.699246
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import AnsibleUnsafeText, UnsafeProxy

# Generated at 2026-10-24 06:40:31.541639
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:34.096814
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:36.517320
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:38.927946
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:41.478489
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:43.894651
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:46.311989
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:48.731655
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:51.152257
# Unit test for function wrap_var

# Generated at 2026-10-24 06:40:53.568157
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:40:55.979456
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:07.594848
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():import warnings


# Generated at 2026-10-24 06:41:25.390730
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:27.808088
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:30.224717
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:32.639613
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:35.061733
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:37.476423
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:39.889644
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:42.304392
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:44.719250
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:47.132362
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:49.546618
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:51.961790
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:41:54.378366
# Unit test for function wrap_var

# Generated at 2026-10-24 06:41:56.792497
# Unit test for function wrap_var

# Generated at 2026-10-24 06:41:59.208079
# Unit test for function wrap_var

# Generated at 2026-10-24 06:42:01.627312
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:42:04.041654
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:42:06.455776
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:42:08.869053
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:42:11.283541
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 06:42:13.696890
# Unit test for method __new__ of class UnsafeProxy