

# Generated at 2022-06-13 20:21:55.032020
# Unit test for function register
def test_register():
    """Test the function 'register()'"""

    register()
    m_register = 'a85d97949f'
    m_normal = 'abcd1234'
    m_register_str = m_register.encode(NAME)

    codecs.register(_get_codec_info)
    m_register_str2 = m_register.encode(NAME)

    assert m_register_str == m_register_str2

    m_register_bytes = codecs.escape_encode(m_register)[0]
    m_normal_bytes = codecs.escape_encode(m_normal)[0]
    m_register_str_bytes = m_register_str.decode(NAME)[0].encode(NAME)

# Generated at 2022-06-13 20:21:58.156323
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)  # should not raise exception
    else:
        raise AssertionError(
            'Codec for "eutf8h" is already registered. '
            'Register function should not have been called.'
        )

# Generated at 2022-06-13 20:22:01.115429
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    get_codec_info = codecs.getdecoder(NAME)
    assert get_codec_info


register()

# Generated at 2022-06-13 20:22:04.313816
# Unit test for function register
def test_register():
    import utf8h
    utf8h.register()
    from utf8h import decode
    result = decode(b'h\\x65\\x6Cl\\x6F')
    assert (result == ('hello', 8))

# Generated at 2022-06-13 20:22:05.780086
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:12.200948
# Unit test for function register
def test_register():
    """
    >>> import eutf8h
    >>> import codecs
    >>> codecs.getdecoder(eutf8h.NAME)
    Traceback (most recent call last):
    ...
    LookupError: 'eutf8h' is not a text encoding; use codecs.register() to register a text encoding
    >>> eutf8h.register()
    >>> codecs.getdecoder(eutf8h.NAME)
    <built-in method getdecoder of codecs module>
    """



# Generated at 2022-06-13 20:22:16.344226
# Unit test for function register
def test_register():
    from eutf8h import test_module_not_in_codec_search_path
    test_module_not_in_codec_search_path(__name__)
    register()
    import codecs
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:21.103171
# Unit test for function register
def test_register():

    # Register this codec.
    register()

    # Get the decoder function.
    decoder = codecs.getdecoder(NAME)

    # Make sure the same object was returned.
    assert decoder == decode

    # Make sure the codec was properly registered.
    assert codecs.lookup(NAME) == decode.__self__

# Generated at 2022-06-13 20:22:25.089596
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)  # noqa: F841
    codecs.getdecoder(NAME)  # noqa: F841



# Generated at 2022-06-13 20:22:27.478417
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore



# Generated at 2022-06-13 20:22:34.094187
# Unit test for function register
def test_register():
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    register()
    assert codec_info == codecs.getdecoder(NAME)
    assert codec_info == codecs.getencoder(NAME)



# Generated at 2022-06-13 20:22:35.407914
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:38.297639
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`."""
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:40.713773
# Unit test for function register
def test_register():
    # This can be tested only in the main thread.
    if is_main_thread():
        register()



# Generated at 2022-06-13 20:22:42.472666
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:44.315635
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:48.386059
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)  # no exception



# Generated at 2022-06-13 20:22:50.351548
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:22:53.407424
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:22:56.655450
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:23:02.320776
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:23:07.220733
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    actual = codecs.getdecoder(NAME)
    expected = (_get_codec_info(NAME)).decode
    assert actual is expected

# Generated at 2022-06-13 20:23:08.968210
# Unit test for function register
def test_register():
    from test.test_eutf8h import IsCodecInfo
    register()
    codec_info = codecs.getdecoder(NAME)
    assert IsCodecInfo(codec_info) is True



# Generated at 2022-06-13 20:23:14.202376
# Unit test for function register
def test_register():
    from StringIO import StringIO
    import sys

    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        register()
        output = out.getvalue().strip()
        assert output == '', output
    finally:
        sys.stdout = saved_stdout



# Generated at 2022-06-13 20:23:16.810350
# Unit test for function register
def test_register():

    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:19.971286
# Unit test for function register
def test_register():
    register()
    decode_func = codecs.getdecoder(NAME)
    decode_func(b'\\x41\\x42')

# Generated at 2022-06-13 20:23:22.488854
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:23:27.812910
# Unit test for function register
def test_register():
    register()
    assert codecs.encode(b'\xe2\x82\xa1', NAME) == b'\\xE2\\x82\\xA1'
    assert codecs.decode(b'\\xE2\\x82\\xA1', NAME) == '\u20A1'

# Generated at 2022-06-13 20:23:29.866631
# Unit test for function register
def test_register():
    from encoding_glob import register as g_register
    g_register('eutf8h')



# Generated at 2022-06-13 20:23:36.168968
# Unit test for function register
def test_register():
    import types
    import sys
    import unittest

    # Remove the module eutf8h from the current scope.
    if NAME in sys.modules:
        del sys.modules[NAME]

    # Re-import the module eutf8h under the name 'module', but
    # don't execute the module's code.
    exec("import eutf8h as module")

    # Create a mock function called 'load_module'.
    def load_module(
            name: str,
            *args: types.Any,
            **kwargs: types.Any
    ) -> types.ModuleType:
        print("load_module call:")
        print("    name: %s" % name)
        print("    args: %s" % str(args))
        print("    kwargs: %s" % str(kwargs))

       

# Generated at 2022-06-13 20:23:43.737056
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:47.664435
# Unit test for function register
def test_register():
    register()
    for codec_name in codecs.getencodings():
        if codec_name[0] == NAME:
            return
    assert False, 'register failed'



# Generated at 2022-06-13 20:23:58.796360
# Unit test for function register
def test_register():
    import sys
    import unittest
    import unicodedata
    import io

    class TestRegister(unittest.TestCase):
        def test_register(self):
            # Register the EUT8H codec
            register()

            # Get the decoder and encoder for EUT8H
            decoder = codecs.getdecoder(NAME)
            encoder = codecs.getencoder(NAME)

            def test_utf8_hex(self, utf8_hex: str) -> None:
                expected_bytes = bytes.fromhex(utf8_hex)
                expected_str = expected_bytes.decode('utf-8')

                bytes_in, length_read = encoder(expected_str)
                self.assertEqual(length_read, len(expected_str))


# Generated at 2022-06-13 20:24:02.019430
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)  # type: ignore
    assert obj.__class__.__name__ == 'CodecInfo'



# Generated at 2022-06-13 20:24:03.009226
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:24:04.232614
# Unit test for function register
def test_register():               # pragma: no cover
    register()

# Generated at 2022-06-13 20:24:05.964732
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            'The codec encoder function failed to register.'
        )



# Generated at 2022-06-13 20:24:08.648082
# Unit test for function register
def test_register():
    """Test the function register.
    """
    register()
    codec_info = codecs.getdecoder(NAME)
    assert codec_info.name == NAME


# Generated at 2022-06-13 20:24:10.551096
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)
    register()



# Generated at 2022-06-13 20:24:14.690573
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('ERROR: register(): Codec already registered')

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('ERROR: register(): Codec not registered')


# Generated at 2022-06-13 20:24:36.491515
# Unit test for function register
def test_register():
    register()
    assert isinstance(
        codecs.getdecoder(NAME),
        codecs.CodecInfo)
    assert isinstance(
        codecs.getencoder(NAME),
        codecs.CodecInfo)


# Generated at 2022-06-13 20:24:38.338206
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Unit tests for function _get_codec_info

# Generated at 2022-06-13 20:24:44.724198
# Unit test for function register
def test_register():
    import sys

    assert sys.__dict__.get('__codecs_hashed_cache', None) is None
    register()
    assert sys.__dict__.get('__codecs_hashed_cache', None) is not None
    assert sys.__dict__.get('__codecs_hashed_cache') == {NAME: None}



# Generated at 2022-06-13 20:24:48.585604
# Unit test for function register
def test_register():
    # Register the codec
    codecs.register(_get_codec_info)      # type: ignore

    # Ensure the encoding was registered.
    obj = codecs.lookup(NAME)
    assert obj.name == NAME



# Generated at 2022-06-13 20:24:50.853512
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail('Failed to register.')


# Generated at 2022-06-13 20:24:52.177597
# Unit test for function register
def test_register():

    register()


register()

# Generated at 2022-06-13 20:24:53.346834
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:54.596364
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getencodings()



# Generated at 2022-06-13 20:25:01.002085
# Unit test for function register
def test_register():
    """Test that the codec has been registered."""
    # Remove the last registered codec, which will be this module's codec
    # as this should be the last module imported.
    if codecs.codecs_last_index > 1:
        codecs.codecs_last_index -= 1

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        has_registered = False
    else:
        has_registered = True

    assert not has_registered

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        has_registered = False
    else:
        has_registered = True

    assert has_registered



# Generated at 2022-06-13 20:25:02.906573
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:25:34.278279
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:37.234741
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # type: ignore



# Generated at 2022-06-13 20:25:38.917996
# Unit test for function register
def test_register():
    register()

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:41.752452
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:25:43.934326
# Unit test for function register
def test_register():
    """
    Test function eutf8h.codec.register()
    """

    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:44.775217
# Unit test for function register
def test_register():
    register()  # noqa

# Generated at 2022-06-13 20:25:45.484925
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:25:56.277972
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


if __name__ == '__main__':
    register()
    for i in range(0, 256):
        if i == 0:
            char = '\\x00'
        elif i < 32 or i > 127:
            char = r'\x%s' % hex(i)[2:]
        else:
            char = chr(i)
        try:
            data, _ = encode(char)
            out, _ = decode(data)
        except UnicodeEncodeError:
            data = None
            out = None
        print(r'%r "%s" 0x%s %r' % (char, char, char, data))
        print(out)

# Generated at 2022-06-13 20:25:58.802028
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder is decode

# Generated at 2022-06-13 20:26:12.338299
# Unit test for function register
def test_register():
    from codecs import CodecInfo
    from collections.abc import Sequence
    from functools import reduce

    from io import BytesIO
    from io import TextIOWrapper

    from typing import Sequence as _Sequence

    from . import _assert
    from . import _eq
    from . import _raise

    line = 'decode 我爱你\u263a'
    words = ((line + '\n') * 5).encode('utf-8')

    buf = BytesIO(words)
    text = TextIOWrapper(buf, encoding=NAME)
    lines = cast(_Sequence[str], text.readlines())
    _assert(isinstance(lines, Sequence))
    out = reduce(lambda s, x: s + x, lines, '')
    _eq(line * 5, out)

   

# Generated at 2022-06-13 20:27:15.372386
# Unit test for function register
def test_register():
    assert NAME not in codecs.getdecoder('X')

# Generated at 2022-06-13 20:27:18.950341
# Unit test for function register
def test_register():
    register()
    # noinspection PyTypeChecker
    assert codecs.getdecoder(NAME)
    assert codecs.lookup(NAME)



# Generated at 2022-06-13 20:27:21.634858
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:27:22.504896
# Unit test for function register
def test_register():
    register()
    return codecs.lookup(NAME)

# Generated at 2022-06-13 20:27:23.786624
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__

# Generated at 2022-06-13 20:27:26.112747
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    obj = codecs.getdecoder(NAME)
    assert obj[0]().decode is decode

# Generated at 2022-06-13 20:27:36.192583
# Unit test for function register
def test_register():
    import os
    import sys
    import pickle
    # First try to register codecs
    register()
    # Reload the codecs module
    if sys.version_info < (3, 6):
        # Reload module for Python 3.5 and below
        import imp
        importlib.reload(imp)
        importlib.reload(codecs)
    else:
        # Reload module for Python 3.6 and above
        import importlib
        importlib.reload(codecs)
    # Create the test string
    test_str = 'Hello World, こんにちは世界'
    encoded = test_str.encode('eutf8h')
    decoded = encoded.decode('eutf8h')
    assert test_str == decoded
    # Make sure that the codecs data is saved

# Generated at 2022-06-13 20:27:42.325627
# Unit test for function register
def test_register():
    """
    Demonstrates that the unicode codec eutf8h can be registered and
    used.
    """
    s = 'A Unicode\u03c0 symbol'
    s_escaped = 'A Unicode\\u03c0 symbol'
    result = s.encode(NAME)
    assert isinstance(result, bytes)
    result = result.decode(NAME)
    assert result == s_escaped



# Generated at 2022-06-13 20:27:48.787050
# Unit test for function register
def test_register():
    register()
    assert NAME == 'eutf8h'
    utf8_bytes = b'\xe2\x82\xac'
    out = codecs.decode(utf8_bytes, NAME)
    assert out == '\u20ac'
    utf8_bytes = b'\xe2\x82\xac'
    out = codecs.decode(utf8_bytes, NAME)
    assert out == '\u20ac'



# Generated at 2022-06-13 20:27:53.345777
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
        del codecs.decode_error_registry[NAME]
        del codecs.encode_error_registry[NAME]
        del codecs.register_error[NAME]
        del codecs.codec_aliases[NAME]
    else:
        raise RuntimeError

# Generated at 2022-06-13 20:28:56.144804
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise Exception('This test cannot run if register is not available.')
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception(
            'Codec not registered successfully. This should not happen.'
        )



# Generated at 2022-06-13 20:29:00.180394
# Unit test for function register
def test_register():
    register()
    encoded_str = encode("中文")
    decoded_str = decode(encoded_str[0])
    assert encoded_str[0] == b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'
    assert decoded_str == ("中文", 0)

# Generated at 2022-06-13 20:29:02.248005
# Unit test for function register
def test_register():
    import codecs
    codecs.lookup('eutf8h')
    assert True



# Generated at 2022-06-13 20:29:06.379717
# Unit test for function register
def test_register():
    """Unit test for function register"""

    # We need to clean up the codecs registry before starting the test
    # so we can get a known starting state.
    deregister()

    register()
    encoder = codecs.getencoder(NAME)
    assert encoder is not None
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None



# Generated at 2022-06-13 20:29:07.601853
# Unit test for function register
def test_register():
    register()

    codecs.lookup(NAME)



# Generated at 2022-06-13 20:29:09.000406
# Unit test for function register
def test_register():
    codecs.lookup('eutf8h')
    codecs.lookup('eutf8h')



# Generated at 2022-06-13 20:29:18.508458
# Unit test for function register
def test_register():
    # Create the codecs registry
    codecs._cache = dict()
    codecs._unknown_error_encode = object()

    # Register this codec
    register()

    # Check that the codec is now registered
    codecs_info = codecs._cache[NAME]
    assert codecs_info.name == NAME
    assert codecs_info.encode == encode
    assert codecs_info.decode == decode
    assert codecs_info.incrementalencoder == None
    assert codecs_info.incrementaldecoder == None
    assert codecs_info.streamreader == None
    assert codecs_info.streamwriter == None



# Generated at 2022-06-13 20:29:20.407365
# Unit test for function register
def test_register():
    """Test for function register

    """
    register()



# Generated at 2022-06-13 20:29:29.327192
# Unit test for function register
def test_register():
    class UserString(str):
        pass
    class MockCodecs:
        def __init__(self, codecs_data: str):
            self.data = codecs_data

        def register(self, codec_info: codecs.CodecInfo):
            self.data[codec_info.name] = codec_info

        def lookup(self, codec_name: str) -> codecs.CodecInfo:
            return self.data[codec_name]

    codecs_obj = MockCodecs({})
    register()
    assert codecs_obj.data[NAME].name == NAME
    assert codecs_obj.data[NAME].encode('') == (b'', 0)
    assert codecs_obj.data[NAME].decode(b'') == ('', 0)
    # assert codecs_obj

# Generated at 2022-06-13 20:29:30.316276
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:31:47.712379
# Unit test for function register
def test_register():
    register()
    utf8 = '\\U0001f600'
    latin1 = '\xf0\x9f\x98\x80'
    utf8_h = '\\xf0\\x9f\\x98\\x80'
    assert utf8.encode('eutf8h') == latin1.encode('latin1')
    assert utf8_h.encode('eutf8h') == latin1.encode('latin1')
    assert latin1.encode('latin1').decode('eutf8h') == utf8


if __name__ == '__main__':
    test_register()