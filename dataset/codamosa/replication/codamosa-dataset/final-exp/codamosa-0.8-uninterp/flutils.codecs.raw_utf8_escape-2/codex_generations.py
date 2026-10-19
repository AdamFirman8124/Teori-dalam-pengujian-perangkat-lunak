

# Generated at 2022-06-13 20:21:47.401370
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.lookup_error('eutf8h') == decode



# Generated at 2022-06-13 20:21:50.027263
# Unit test for function register
def test_register():
    """Test that codec is properly registered"""
    assert codecs.getdecoder(__name__.split('.')[-1]) is not None

# Generated at 2022-06-13 20:21:50.649849
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:21:51.947176
# Unit test for function register
def test_register():
    register()
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:21:53.862802
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


_CODEC_PARAMS = dict(
    name=NAME,
)

# Generated at 2022-06-13 20:21:54.719996
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:21:56.828976
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(f'Codec {NAME} lookup failed.') from e



# Generated at 2022-06-13 20:21:57.816729
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:22:02.305216
# Unit test for function register
def test_register():
    register()
    # This line below can't be unit tested due to the fact that once a codec is
    # registered, it remains that way for the duration of the program.
    # assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:22:03.225577
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:10.317342
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__
    register()
    assert NAME in codecs.__dict__

    codec_info_member = codecs.__dict__[NAME]

    text = 'hello'

    assert text.encode(NAME) == text.encode('utf-8')

    assert text.encode(NAME) == b'hello'


test_register()

# Generated at 2022-06-13 20:22:19.515159
# Unit test for function register
def test_register():
    import sys
    import types
    # Test function register
    register()
    module = sys.modules[__name__]

    # test.org module should have
    # the following attributes
    assert hasattr(module, NAME)
    assert isinstance(module.NAME,  str)
    assert module.NAME == NAME

    codec_info = codecs.lookup(NAME)

    # Codec_info should have name = NAME
    assert hasattr(codec_info, 'name')
    assert isinstance(codec_info.name, str)
    assert codec_info.name == NAME

    # Codec_info should have encode and decode functions
    assert hasattr(codec_info, 'encode')
    assert isinstance(codec_info.encode, types.FunctionType)


# Generated at 2022-06-13 20:22:24.410428
# Unit test for function register
def test_register():
    out = codecs.getencoder(NAME)  # type: ignore
    assert out == encode
    out = codecs.getdecoder(NAME)  # type: ignore
    assert out == decode



# Generated at 2022-06-13 20:22:30.572727
# Unit test for function register
def test_register():
    import io
    import sys

    try:
        f = io.StringIO()
        sys.stdout = f

        register()
        codecs.lookup(NAME)
        assert f.getvalue() == ''
    finally:
        sys.stdout = sys.__stdout__  # type: ignore



# Generated at 2022-06-13 20:22:31.781464
# Unit test for function register
def test_register():
    """ Testing function register()"""
    register()

# Generated at 2022-06-13 20:22:36.303449
# Unit test for function register
def test_register():
    try:
        register()
    except LookupError:
        # This can happen if another thread is in the register function
        pass


if __name__ == '__main__' or __name__ == 'builtins':
    test_register()

# Generated at 2022-06-13 20:22:42.373250
# Unit test for function register
def test_register():
    codecs_num_encodings__init = codecs.getencoder(NAME)
    codecs_num_encodings__func = _get_codec_info(NAME)
    assert codecs_num_encodings__init.__code__ is codecs_num_encodings__func.__code__



# Generated at 2022-06-13 20:22:45.149336
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:22:48.284006
# Unit test for function register
def test_register():
    register()
    assert "eutf8h" in f"{codecs.getdecoder(NAME)}"



# Generated at 2022-06-13 20:22:49.649738
# Unit test for function register
def test_register():
    register()
    # Check if the encoding is registered
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:22:56.391925
# Unit test for function register
def test_register():
    register()
    try:
        str.encode('\\u2713', 'eutf8h')
    except LookupError:
        assert False, 'The codec eutf8h is not registered'
    return



# Generated at 2022-06-13 20:23:07.715203
# Unit test for function register
def test_register():
    """Test function register()."""
    import sys

    # Remove the register() function if present
    sys.modules['escape_utf8_hexadecimal'].register = register
    register()
    encode_func = codecs.getencoder(NAME)
    decode_func = codecs.getdecoder(NAME)
    assert NAME in sys.modules['escape_utf8_hexadecimal'].__all__
    assert encode_func == encode
    assert decode_func == decode



# Generated at 2022-06-13 20:23:10.663002
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise


# Generated at 2022-06-13 20:23:15.549151
# Unit test for function register
def test_register():
    """
    :return:
    """

    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


if __name__ == '__main__':
    test_register()

    # noinspection PyUnresolvedReferences
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:23:18.052516
# Unit test for function register
def test_register():
    # Test for the case when codec is already registered.
    register()
    register()



# Generated at 2022-06-13 20:23:24.244100
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None
    assert isinstance(codec, codecs.CodecInfo)
    assert NAME == codec.name
    assert encode is codec.encode
    assert decode is codec.decode


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:26.708823
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
#   codecs.getencoder(NAME)



if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:39.063753
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getdecoder('eutf8h')
    except LookupError as e:
        codecs.register(eutf8h.codec.register)
        test_text_bytes_utf8 = b'\\x53\\x6f\\x6d\\x65\\x20\\x68\\xc3\\xa5\\x72\\x20\\x68\\xc3\\xa4\\x72\\x20\\x68\\xc3\\xab\\x72'
        test_text_string = 'Some hår här hër'
        test_text_string_bytes, test_text_string_length = codecs.getdecoder('eutf8h')(test_text_bytes_utf8)
        assert test_text_string_bytes == test_text_string
       

# Generated at 2022-06-13 20:23:45.380639
# Unit test for function register
def test_register():
    codec = codecs.lookup(NAME)
    assert codec is not None
    assert codec.encode(u'\u1234') == (b'\\xe1\\x88\\xb4', 1)
    assert codec.decode(b'\\xe1\\x88\\xb4') == ('ሴ', 3)


# Generated at 2022-06-13 20:23:48.084253
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getencodings()
    assert NAME in codecs.getdecodings()



# Generated at 2022-06-13 20:23:55.584119
# Unit test for function register
def test_register():
    register()

# Run register, and define the codecs
register()

# Define the corresponding decoders and encoders
eutf8h_encode = codecs.getencoder(NAME)
eutf8h_decode = codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:58.519317
# Unit test for function register
def test_register():

    # Register the codec and get the decoder.
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None



# Generated at 2022-06-13 20:24:01.426725
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:24:02.715821
# Unit test for function register
def test_register():
    register()
    assert (codecs.lookup(NAME))

# Generated at 2022-06-13 20:24:13.329538
# Unit test for function register
def test_register():
    # Make sure the codec is not registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False

    # Register the codec and test if it is registered.
    codecs.register(_get_codec_info)
    decoder = None
    try:
        decoder = codecs.getdecoder(NAME)
    except LookupError:
        assert False
    assert decoder is not None
    assert decoder.__name__ == NAME



# Generated at 2022-06-13 20:24:18.788804
# Unit test for function register
def test_register():
    assert codecs.lookup_error('strict') == 'strict'
    assert codecs.lookup_error('replace') == 'replace'
    assert codecs.lookup_error('ignore') == 'ignore'

    register()
    assert codecs.lookup_error('strict') == 'strict'
    assert codecs.lookup_error('replace') == 'replace'
    assert codecs.lookup_error('ignore') == 'ignore'



# Generated at 2022-06-13 20:24:21.074184
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False
    assert True

register()


# Testing function encoding

# Generated at 2022-06-13 20:24:25.856417
# Unit test for function register
def test_register():
    # Need to have this function to test the proper registration of the
    # codec. This is to specifically test the line:
    # codecs.getdecoder(NAME)
    try:
        register()
    except LookupError:
        pass



# Generated at 2022-06-13 20:24:32.592918
# Unit test for function register
def test_register():
    register()
    u_str = 'Hello world!\n'
    data = '\\x48\\x65\\x6c\\x6c\\x6f\\x20\\x77\\x6f\\x72\\x6c' \
           '\\x64\\x21\\x0a'
    data = codecs.escape_decode(data)[0]
    assert codecs.encode(u_str, 'eutf8h')[0] == data


if __name__ == '__main__':
    register()
    u_str = 'Hello world!\n'
    data = '\\x48\\x65\\x6c\\x6c\\x6f\\x20\\x77\\x6f\\x72\\x6c' \
           '\\x64\\x21\\x0a'
   

# Generated at 2022-06-13 20:24:35.323469
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.getencoder(NAME)
    except LookupError:
        assert False



# Generated at 2022-06-13 20:24:50.041070
# Unit test for function register
def test_register():
    register()
    codecs.decode(b"\\x65\\x66\\x67", NAME)  # type: ignore
    if codecs.decode(b"\\x65\\x66\\x67", NAME) != 'efg':
        raise AssertionError("test_register: codecs.decode not working.")
    if codecs.encode("abc", NAME) != b"\\x61\\x62\\x63":
        raise AssertionError("test_register: codecs.encode not working.")
    codecs.decode(b"\\x65\\x66\\x67", NAME)

# Generated at 2022-06-13 20:24:52.378655
# Unit test for function register
def test_register():
    register()
    dec = codecs.getdecoder(NAME)
    assert dec
# test_register


# Generated at 2022-06-13 20:24:54.340569
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:25:00.344527
# Unit test for function register
def test_register():
    import unittest.mock

    class _MockLookupError(LookupError):
        def __init__(self, name: str):
            self._name = name

        def __str__(self) -> str:  # pragma: no cover
            return self._name

    class _MockCodecs:
        def getdecoder(self, name: str):
            raise _MockLookupError(name)

        def register(self, codec_info: codecs.CodecInfo):
            pass

    codecs.getdecoder = unittest.mock.Mock(side_effect=_MockLookupError)
    codecs.CodecInfo = unittest.mock.Mock()
    codecs.register = unittest.mock.Mock()

    register()

    codecs.get

# Generated at 2022-06-13 20:25:01.450025
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:02.492381
# Unit test for function register
def test_register():
    """Test 'register' function."""
    register()

# Generated at 2022-06-13 20:25:03.175848
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:25:08.543842
# Unit test for function register
def test_register():
    from types import ModuleType
    module = ModuleType('_test_register')
    module.__loader__ = None  # type: ignore
    module.__package__ = None  # type: ignore
    module.test_register = register
    module.test_register()

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:10.012645
# Unit test for function register
def test_register():
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:25:14.453866
# Unit test for function register
def test_register():
    class Mock:
        def __init__(self):
            self.count = 0

        def __call__(self,
                     name: Union[str, UserString]
                     ) -> Optional[codecs.CodecInfo]:
            self.count += 1
            return _get_codec_info(name)

    m = Mock()
    codecs.register = m  # type: ignore
    register()
    assert m.count == 1



# Generated at 2022-06-13 20:25:35.389573
# Unit test for function register
def test_register():
    global codecs
    import sys

    codecs_mod = sys.modules['codecs']
    codecs_orig = codecs_mod.__dict__.copy()

    # Remove codec named NAME. Test

# Generated at 2022-06-13 20:25:38.139916
# Unit test for function register
def test_register():
    NAME = __name__.split('.')[-1]

    code = codecs.getdecoder(NAME)
    assert code



# Generated at 2022-06-13 20:25:43.891378
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    from pytest import mark
    from sys import version_info

    _mark = mark.skipif(
        version_info.minor < 7,
        reason='requires Python 3.7 or higher'
    )

    def _test_register():
        codecs.lookup(NAME)

    _mark(_test_register)



# Generated at 2022-06-13 20:25:54.995306
# Unit test for function register
def test_register():
    from io import BytesIO
    from io import StringIO
    from codecs import getreader
    from codecs import getwriter
    from codecs import getdecoder
    from codecs import getencoder
    register()

    _in = cast(BytesIO, BytesIO(b'\\xe3'))
    _out = cast(StringIO, StringIO())
    _in_reader = cast(codecs.StreamReader, getreader(NAME)(_in))
    _out_writer = cast(codecs.StreamWriter, getwriter(NAME)(_out))

    in_char = _in_reader.read(1)
    while in_char:
        _out_writer.write(in_char)
        in_char = _in_reader.read(1)

    _out.seek(0)

# Generated at 2022-06-13 20:25:58.045533
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        codecs.lookup(NAME)

    # Register the codec
    register()

    codecs.lookup(NAME)

# Generated at 2022-06-13 20:25:59.625954
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:03.639442
# Unit test for function register
def test_register():
    """
    Test the 'register' function.
    """
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:13.342764
# Unit test for function register
def test_register():
    register()
    utf8_ehex_bytes = b'\\xE6\\x97\\xA5\\xE6\\x9C\\xAC\\xE8\\xAA\\x9E'
    utf8_ehex_str = utf8_ehex_bytes.decode('eutf8h')
    assert utf8_ehex_str == '日本語'
    utf8_bytes = utf8_ehex_str.encode('utf8')
    assert utf8_bytes == utf8_ehex_bytes

# Generated at 2022-06-13 20:26:19.074075
# Unit test for function register
def test_register():
    register()
    try:
        # Due to the cache used in the function codecs.lookup, the
        # function _get_codec_info will not be called the second time
        # during the same Python instance.
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)
    except LookupError as e:
        raise AssertionError(f"Test register failed: {e}")


# Unit test of function encode

# Generated at 2022-06-13 20:26:21.387749
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()



# Generated at 2022-06-13 20:26:50.276443
# Unit test for function register
def test_register():
    codecs.register = lambda x: None
    register()

# Generated at 2022-06-13 20:26:51.886344
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:26:56.658215
# Unit test for function register
def test_register():
    import sys
    import unittest

    class TestRegister(unittest.TestCase):

        def test_register(self):
            register()
            self.assertIn('eutf8h', sys.getfilesystemencoding())

    unittest.main()

# Generated at 2022-06-13 20:27:06.598865
# Unit test for function register
def test_register():
    import codecs

    register()
    codecs.getencoder(NAME)


# def test_encode() -> None:
#     import codecs
#     import binascii
#     import unittest
#
#     register()
#
#     if True:
#         buf_1, _ = codecs.getencoder(NAME)('abcdefg')
#         buf_2, _ = codecs.getencoder('unicode_escape')('abcdefg')
#         assert buf_1 == buf_2
#
#         buf_1, _ = codecs.getencoder(NAME)('a\n')
#         buf_2, _ = codecs.getencoder('unicode_escape')('a\n')
#         assert buf_1 == buf_2
#
#         buf_1

# Generated at 2022-06-13 20:27:07.502634
# Unit test for function register
def test_register():
    pass



# Generated at 2022-06-13 20:27:08.461294
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:27:10.357408
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:27:12.895593
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
        register()
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:16.811832
# Unit test for function register
def test_register():
    # codecs.getdecoder('mytest') # raises "LookupError: 'mytest' is not a
    # text encoding; use codecs.lookup() to obtain a codec object."
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:27.893785
# Unit test for function register
def test_register():
    # verify that the codec is not registered
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        assert str(e) == 'unknown encoding: %s' % NAME
    else:
        assert False, 'the codec should not be registered'

    register()

    # verify that the codec is registered
    try:
        decoder = codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'codecs.getdecoder() failed'

    assert decoder(b'\\x30') == ('0', 2)
    assert decoder(b'\\x30\\x31') == ('01', 3)
    assert decoder(b'\\x30', 'strict') == ('0', 2)

# Generated at 2022-06-13 20:28:36.735246
# Unit test for function register
def test_register():
    # Test the registration of the codec.
    import sys
    import codecs

    if 'eutf8h' in codecs.__dict__['cache']:
        codecs.__dict__['cache'].pop('eutf8h')
    assert 'eutf8h' not in codecs.__dict__['cache']

    assert 'eutf8h' not in sys.modules

    # Register this codec.
    register()

    import eutf8h

    assert eutf8h.__name__ == 'eutf8h'

    assert 'eutf8h' in codecs.__dict__['cache']
    assert 'eutf8h' in sys.modules



# Generated at 2022-06-13 20:28:39.453151
# Unit test for function register
def test_register():
    register()

    assert NAME in codecs.__dict__['__all_encodings__']
    assert NAME in codecs.__dict__['__all_decodings__']



# Generated at 2022-06-13 20:28:40.425668
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:28:42.040245
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:28:44.367571
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:28:50.067090
# Unit test for function register
def test_register():
    register()
    # Assert that NAME is registered as a codec
    coding, encoding = codecs.lookup(NAME)
    assert NAME in encoding
    # Assert that NAME is registered as a codec
    coding, decoding = codecs.lookup(NAME)
    assert NAME in decoding



# Generated at 2022-06-13 20:28:55.421316
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass  # codec not registered yet
    else:
        raise AssertionError(
            f'{NAME} codec is already registered'
        )
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            f'{NAME} codec not registered'
        )

# Generated at 2022-06-13 20:28:57.076544
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore

# Generated at 2022-06-13 20:28:57.907659
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:29:04.152948
# Unit test for function register
def test_register():
    register()
    test_string = 'Unicode string: ©©©'
    test_unicode_string = 'Unicode string: \\u00a9\\u00a9\\u00a9'
    test_bytes = test_unicode_string.encode()

    assert type(test_string) is str
    assert type(test_bytes) is bytes
    assert test_string == codecs.decode(test_bytes, NAME)
    assert test_bytes == codecs.encode(test_string, NAME)

# Generated at 2022-06-13 20:31:19.696314
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:31:21.412484
# Unit test for function register
def test_register():
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:31:29.325762
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception(
            'The escape_utf8_hexadecimal codec is not available.')
    try:
        codecs.lookup(NAME)
    except LookupError:
        raise Exception(
            'The escape_utf8_hexadecimal codec is not available.')



# Generated at 2022-06-13 20:31:30.843188
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:31:36.603029
# Unit test for function register
def test_register():
    # codecs.getdecoder('eutf8h')
    for __name__ in (NAME, NAME.upper(), NAME.lower()):
        try:
            codecs.getdecoder(__name__)
            break
        except LookupError:
            pass
    else:
        codecs.register(_get_codec_info)  # type: ignore
        codecs.getdecoder(NAME)

# Unit tests

# Generated at 2022-06-13 20:31:40.768803
# Unit test for function register
def test_register():
    import codecs
    register()
    codecs.getdecoder(NAME)
# /Unit test for function register


# noinspection PyPep8Naming