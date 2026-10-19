

# Generated at 2022-06-13 20:21:48.495656
# Unit test for function register
def test_register():
    """Unit test for the function register."""
    other_name = 'other_{}'.format(NAME)

    # Make sure the function raises the LookupError exception.
    with pytest.raises(AttributeError):
        codecs.getdecoder(other_name)

    register()

    # Make sure this does not raise the LookupError exception.
    codecs.getdecoder(NAME)

    # Ensure the 'other_b64' codec does not exist.
    with pytest.raises(AttributeError):
        codecs.getdecoder(other_name)


# Generated at 2022-06-13 20:21:50.877966
# Unit test for function register
def test_register():
    # Arrange
    # Act
    register()

    # Assert
    assert NAME in {  # type: ignore
        'b64',
    }

# Generated at 2022-06-13 20:21:57.219441
# Unit test for function encode
def test_encode():
    """Test the encode function"""

# Generated at 2022-06-13 20:22:04.988182
# Unit test for function register
def test_register():
    """Unit test for function register."""
    import unittest
    import sys

    # noinspection PyUnresolvedReferences
    class TestRegister(unittest.TestCase):
        """Unit test for function register."""

        def test_register(self):
            """Test function register."""
            sys.modules.pop('b64_codec.b64')
            import b64_codec.b64
            b64_codec.b64.register()
            codecs.getdecoder(NAME)

    unittest.main()



# Generated at 2022-06-13 20:22:09.934292
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
        assert False, "The codec should not be registered"
    except LookupError:
        pass
    register()
    obj = codecs.getdecoder(NAME)
    assert obj and isinstance(obj, tuple) and len(obj) == 2 and callable(obj[0])

# Generated at 2022-06-13 20:22:11.922554
# Unit test for function encode
def test_encode():
    assert encode('QQ==') == (b'\x01', 4)


# Generated at 2022-06-13 20:22:22.634421
# Unit test for function encode
def test_encode():
    # tests that a normal base64 string encodes properly
    assert encode( 'TW9uZ28gT25z') == (b'Mongo Ons', 11)
    # tests that a base64 string with spaces encodes properly
    assert encode('TW9u Z29P bnM=') == (b'Mongo Ons', 13)
    # tests that a base64 string with newlines and spaces encodes properly
    assert encode('TW9u\nZ29P\nb nM=') == (b'Mongo Ons', 17)
    # tests that a base64 string with tabs and spaces encodes properly
    assert encode('TW9u\tZ29P\tb nM=') == (b'Mongo Ons', 17)
    # tests that encoding a string that is not base64 raises an error
    assert encode('Not b64')

# Generated at 2022-06-13 20:22:26.184740
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.lookup(NAME)


register()


# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:22:31.781665
# Unit test for function register
def test_register():
    """Test to make sure that the b64 codec can be registered."""
    try:
        register()
    except Exception as e:  # pylint: disable=broad-except
        return f'{e}'
    output = codecs.decode(b'Hello World', NAME)
    return output

# Generated at 2022-06-13 20:22:35.121701
# Unit test for function register
def test_register():
    register()
    value: codecs.CodecInfo = codecs.getdecoder(NAME)   # type: ignore
    assert hasattr(value, 'encode')
    assert hasattr(value, 'decode')


# Generated at 2022-06-13 20:22:52.033824
# Unit test for function encode
def test_encode():
        """Unit test for `encode`."""

# Generated at 2022-06-13 20:22:54.379815
# Unit test for function register
def test_register():
    """Test to see if the ``b64`` codec is registered."""
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:58.873099
# Unit test for function register
def test_register():
    b64_codec = _get_codec_info(NAME)

    assert b64_codec is not None

    assert b64_codec.name == 'b64'
    assert b64_codec.encode == encode
    assert b64_codec.decode == decode



# Generated at 2022-06-13 20:23:14.561140
# Unit test for function encode
def test_encode():
    text_input = """
        c2FsdAXY6Q1QyU2FyQ0NlK2xzWmJsd0lxMGFteUczS3pKdW9hZ0NXO
        G1KU1BZT0VMZktpYmU4YWRmV2VCU2FkU2xlZHBhYlVlQ1FxQjVuYUdp
        YkIrcjJucEFrdXJFRnZVS014VVhJS3ZnM3Z2L1J5RkV5cXRsc21tMlN0
        WGpZSUxzZ3VUR0Q=
    """.strip()

# Generated at 2022-06-13 20:23:18.738676
# Unit test for function register
def test_register():
    """Unit test to verify the 'b64' codec is registered with Python."""
    register()

    codecs.getdecoder('b64')


# Unit test 'b64' codec.

# Generated at 2022-06-13 20:23:22.805829
# Unit test for function register
def test_register():
    """Unit test for function register"""
    try:
        codecs.lookup(NAME)
    except LookupError:
        register()
        codecs.lookup(NAME)



# Generated at 2022-06-13 20:23:32.242631
# Unit test for function register
def test_register():
    """Register the codec with Python's codec registry."""
    codecs_info = codecs.lookup(NAME)
    assert codecs_info.name == NAME
    assert isinstance(codecs_info.encode, type(encode))
    assert isinstance(codecs_info.decode, type(decode))

    # Make sure the 'b64' function is not redefined.
    with pytest.raises(NameError):
        # pylint: disable=function-redefined
        def encode(text: _STR, errors: _STR = 'strict') -> bytes:  # type: ignore
            pass



# Generated at 2022-06-13 20:23:36.291197
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec is registered with Python."""
    register()
    assert 'b64' in codecs.__dict__['_cache']


# Generated at 2022-06-13 20:23:39.215534
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:23:50.839897
# Unit test for function register
def test_register():    # pragma: no cover
    # pylint: disable=W0612, W0613
    def encode(string: _STR, errors: str = 'strict') -> bytes:
        return bytes('')

    def decode(bytes_: bytes, errors: str = 'strict') -> _STR:
        return ''

    codecs.CodecInfo(
        name='test',
        encode=encode,  # type: ignore[arg-type]
        decode=decode,  # type: ignore[arg-type]
    )
    codecs.register(lambda x: codecs.CodecInfo(
        name='test',
        encode=encode,  # type: ignore[arg-type]
        decode=decode,  # type: ignore[arg-type]
    ))
    register()
    register()
    register

# Generated at 2022-06-13 20:23:56.245132
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:24:00.264709
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert NAME in codecs.getdecoder(NAME)  # type: ignore
    assert NAME in codecs.getencoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:24:05.213957
# Unit test for function encode
def test_encode():
    """Unit test for function :func:`.encode`"""
    x = encode("aGVsbG8gd29ybGQ=")
    assert x == (b'hello world', 14)
    x = encode("TUlOIGFuZCBFWFRS")
    assert x == (b'MIN and EATS', 14)



# Generated at 2022-06-13 20:24:06.216815
# Unit test for function register
def test_register():
    """Invoke register() and verify the codec 'b64' is registered."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:09.255542
# Unit test for function register
def test_register():
    """Test function register()"""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:24:11.341886
# Unit test for function encode
def test_encode():
    assert encode('aGVsbG8gd29ybGQ=') == (b'hello world', 14)



# Generated at 2022-06-13 20:24:18.693564
# Unit test for function encode
def test_encode():
    input1 = "This is the first line.\nThis is the second line."
    expected1 = b'This is the first line.\nThis is the second line.'
    output1 = encode(input1)[0]
    assert output1 == expected1
    input2 = "This\nis\n\none\n\n\nat\tthe\t\ttop."
    expected2 = b'This\nis\none\nat\tthe\ttop.'
    output2 = encode(input2)[0]
    assert output2 == expected2
    input3 = "This\nis\n\none\n\n\nat\tthe\t\ttop."
    expected3 = b'This is one at the top.'
    output3 = encode(input3, errors='ignore')[0]
    assert output3 == expected3
    input

# Generated at 2022-06-13 20:24:22.865261
# Unit test for function register
def test_register():                     # pragma: no cover
    """Ensure that the b64 codec was registered."""
    register()
    try:
        codecs.getdecoder(NAME)
        assert True
    except LookupError:
        assert False



# Generated at 2022-06-13 20:24:26.485377
# Unit test for function register
def test_register():
    """Test function 'register'."""
    # pylint: disable=W0110
    # W0110: Unreachable code
    out = codecs.getdecoder(NAME)
    assert out is not None

# Generated at 2022-06-13 20:24:37.490249
# Unit test for function encode
def test_encode():
    from unittest import TestCase, main as unit_test_main

    class TestEncode(TestCase):
        """Test the encode function."""

        # pylint: disable=R0201
        # noinspection PyUnusedLocal
        def setUp(self) -> None:
            """Set up the encode testing"""

# Generated at 2022-06-13 20:24:44.969820
# Unit test for function register
def test_register():
    """Unit test for function register."""
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:24:49.344381
# Unit test for function register
def test_register():  # pylint: disable=R0914
    """Unit test for function register."""
    register()
    buff = bytes([0x80, 0x80, 0xFF, 0x00])
    actual = NAME.encode(buff)
    expected = 'gOD/AAAA'
    assert actual == expected

# Generated at 2022-06-13 20:24:50.564478
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:53.855623
# Unit test for function encode
def test_encode():
    assert(encode('SGVsbG8gd29ybGQ=') == (b'Hello world', 14))
    assert(encode('TWFu') == (b'Man', 3))


# Generated at 2022-06-13 20:24:55.705859
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:57.413217
# Unit test for function register
def test_register():
    """Test the ``codecs.register`` call."""
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:25:03.319414
# Unit test for function encode
def test_encode():
    """Test encode with various inputs.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.
    """

# Generated at 2022-06-13 20:25:08.197831
# Unit test for function register
def test_register():
    """Test registering the ``b64`` codec with Python."""
    codecs.register(_get_codec_info)   # type: ignore
    exists = True
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        exists = False
    assert exists



# Generated at 2022-06-13 20:25:15.781478
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""

    # Test encoder for the case where the given 'text' is a str.
    # Type is str
    text = (
        "This is a test to see if the encoder works"
        "I am trying to test to see if this works"
    )
    bytes_text = encode(text)[0]
    utf8_string = bytes_text.decode('utf-8')
    assert utf8_string == text

    # Type is UserString
    text = UserString(
        "This is a test to see if the encoder works"
        "I am trying to test to see if this works"
    )
    bytes_text = encode(text)[0]
    utf8_string = bytes_text.decode('utf-8')

# Generated at 2022-06-13 20:25:27.375518
# Unit test for function encode
def test_encode():
    # Gives expected bytes with minimal input
    assert encode('SGVsbG8gd29ybGQhIQ==') == (b'Hello world!!', 18)

    # Gives expected bytes with extra spaces
    assert encode('        SGVsbG8gd29ybGQhIQ==        ') == (b'Hello world!!', 18)

    # Gives expected bytes with newlines
    assert encode(
        '''
            SGVsbG8gd29ybGQhIQ==
        '''.strip()
    ) == (b'Hello world!!', 18)

    # Gives expected bytes with extra spaces and newlines
    assert encode(
        '''
            SGVsbG8gd29ybGQhIQ==



        '''.strip()
    ) == (b'Hello world!!', 18)

    # Gives

# Generated at 2022-06-13 20:25:43.890371
# Unit test for function register
def test_register():
    old_registry = codecs.REGISTRY
    try:
        codecs.REGISTRY = []
        register()
        try:
            codecs.getdecoder(NAME)
        except LookupError:
            raise
    finally:
        codecs.REGISTRY = old_registry

# Generated at 2022-06-13 20:25:45.491733
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # pylint: disable=C0116
    register()


# Generated at 2022-06-13 20:25:56.624843
# Unit test for function encode
def test_encode():
    def single_test(text: str, expected: bytes) -> None:
        out, _ = encode(text)
        assert out == expected
    single_test(
        '''
        czerwony jest najlepszy
        '''
        ,
        b'emVyb3duIGlzIG5hamVzdHk='
    )

# Generated at 2022-06-13 20:25:58.945164
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)  # Should not raise


# Generated at 2022-06-13 20:26:01.748992
# Unit test for function register
def test_register():
    """Test function register"""
    register()
    assert codecs.lookup_error('b64') == (decode, encode)

# Generated at 2022-06-13 20:26:15.574226
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('', 'strict') == (b'', 0)
    assert encode('', 'ignore') == (b'', 0)
    assert encode('', 'replace') == (b'', 0)
    assert encode(' ', 'strict') == (b'', 1)
    assert encode(' ', 'ignore') == (b'', 1)
    assert encode(' ', 'replace') == (b'', 1)
    assert encode('\t', 'strict') == (b'', 1)
    assert encode('\t', 'ignore') == (b'', 1)
    assert encode('\t', 'replace') == (b'', 1)
    assert encode('  ', 'strict') == (b'', 2)

# Generated at 2022-06-13 20:26:17.140167
# Unit test for function register
def test_register():
    register()
    _ = codecs.getdecoder(NAME)
    _ = codecs.getencoder(NAME)

# Generated at 2022-06-13 20:26:22.567442
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    text_1 = 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ'
    text_2 = '''aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hj
        UQ'''
    text_3 = '''    aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hj
        UQ'''


# Generated at 2022-06-13 20:26:23.987933
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:26:34.297433
# Unit test for function encode
def test_encode():
    # pylint: disable=line-too-long
    encoding_table = {
        # text: (text, length, bytes)
        'SGVsbG8gV29ybGQh': (
            'SGVsbG8gV29ybGQh',
            14,
            b'Hello World!'
        )
    }
    # pylint: enable=line-too-long
    for encoded_text, expected_encode in encoding_table.items():
        text, length, decoded_bytes = expected_encode
        assert length == len(text)
        assert decoded_bytes == encode(encoded_text)[0]



# Generated at 2022-06-13 20:27:03.718405
# Unit test for function register
def test_register():
    """Unit test for function register."""
    import doctest
    from . import util
    code = util.get_test_code(__file__)
    results = doctest.testmod(code)
    if results.failed > 0:
        raise Exception(f'{results.failed} test(s) failed')

# Generated at 2022-06-13 20:27:08.307181
# Unit test for function register
def test_register():
    """Test the function register."""
    # noinspection PyUnresolvedReferences
    from lib.codec import codec_b64 as module

    assert hasattr(module, 'register')
    assert callable(module.register)

    register()

    from codecs import getdecoder

    assert getdecoder(NAME) is not None


# Generated at 2022-06-13 20:27:17.113994
# Unit test for function encode
def test_encode():
    data = "AAA="
    assert encode(data) == (b'\x00', 4)

    data = "AAAA"
    assert encode(data) == (b'\x00\x00', 4)

    data = "AA=="
    assert encode(data) == (b'\x00\x00', 4)

    data = "AA"
    assert encode(data) == (b'\x00', 2)

    data = "A"
    assert encode(data) == (b'\x00', 1)

    data = "abc"
    assert encode(data) == (b'\x00\x00', 3)

    data = "ABC"
    assert encode(data) == (b'\x00\x00\x00', 3)

    data = "ABCD"

# Generated at 2022-06-13 20:27:20.954438
# Unit test for function encode
def test_encode():   # pragma: no cover
    # convert input text of base64 characters into base64 decoded bytes
    print("\nConvert input text of base64 characters into base64 decoded bytes\n")
    text1 = "Zm9vYmFy"
    print(f"text1: {text1}")
    print(f"type(text1): {type(text1)}")
    print(f"encode(text1): {encode(text1)}")
    text2 = "SGVsbG9Xb3JsZA=="
    print(f"text2: {text2}")
    print(f"type(text2): {type(text2)}")
    print(f"encode(text2): {encode(text2)}")



# Generated at 2022-06-13 20:27:29.426984
# Unit test for function register
def test_register():
    """Register the base64 codec."""
    codecs.getdecoder(NAME + '.')
    if NAME not in codecs.decode.__globals__:
        raise RuntimeError(
            f'Could not register {NAME} as a codec.'
        )
    # there is no way to unregister the codec
    # so leave it registered
#     del(codecs.decode.__globals__[NAME])
#     try:
#         codecs.getdecoder(NAME + '.')
#     except LookupError:
#         pass
#     else:
#         raise RuntimeError(
#             '{} codec was not unregistered.'.format(NAME)
#         )


# pylint: disable=C0111
# Initialize on import.

# Generated at 2022-06-13 20:27:37.432154
# Unit test for function encode
def test_encode():
    """Test the function "encode".
    """
    print(test_encode.__doc__)

    def _print(*args):
        """Wrapper for print for readability.
        """
        # pylint: disable=W0104
        print(*args)

    def _test(text: _STR, result: bytes, **kwargs):
        """Test the function.
        """
        # pylint: disable=W0613
        _errors = 'strict' if 'errors' not in kwargs else kwargs['errors']
        _print(f'{test_encode.__doc__}:')
        _print(f'text::{text!r}')
        _print(f'result::{result!r}')
        _print(f'errors::{_errors!r}')
        _

# Generated at 2022-06-13 20:27:39.761653
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert NAME in codecs.getcodecs()


# Generated at 2022-06-13 20:27:53.452027
# Unit test for function encode
def test_encode():
    # Test the input of an empty string.
    test_text = ''
    expected_bytes = b''
    expected_int = 0
    actual_bytes, actual_int = encode(test_text)
    assert actual_bytes == expected_bytes, (
        f'encode({test_bytes}) returned {actual_bytes}, expected '
        f'{expected_bytes}'
    )
    assert actual_int == expected_int, (
        f'encode({test_text}) returned {actual_int}, expected '
        f'{expected_int}'
    )

    # Test the input of a single line
    test_text = 'aGVsbG8gd29ybGQ='
    expected_bytes = b'hello world'
    expected_int = len(test_text)

# Generated at 2022-06-13 20:28:03.859704
# Unit test for function register
def test_register():
    # Make sure that the codec has not been registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, 'Codec is already registered'

    # Register the codec
    register()

    # Make sure that the codec has been registered.
    codec = codecs.getdecoder(NAME)

    assert codec is not None, 'Codec is not registered'


# pylint: disable=C0103
decode_str = codecs.register(_get_codec_info)(decode)
encode_str = codecs.register(_get_codec_info)(encode)



# Generated at 2022-06-13 20:28:09.194478
# Unit test for function register
def test_register():
    """Verify the function register() works correctly."""
    register()
    enc = 'RmFtaWx5IENoZWVy'
    data_expected = b'Family Cheer'
    data_actual = codecs.decode(enc, NAME)
    assert data_actual == data_expected



# Generated at 2022-06-13 20:29:02.866370
# Unit test for function register
def test_register():
    """Test the :obj:`register` function.

    Registering a codec twice should raise a LookupError.
    """
    register()
    with pytest.raises(LookupError):
        codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:29:04.781394
# Unit test for function register
def test_register():
    """Register the ``b64`` codec with Python."""
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:29:08.380397
# Unit test for function register
def test_register():
    """Test function register"""
    codecs.register(_get_codec_info)
    # Check that the register function gets the codec.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False   # The test failed since the codec wasn't found.
    else:
        assert True    # The test passed.


# Generated at 2022-06-13 20:29:10.955629
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:29:24.844217
# Unit test for function encode
def test_encode():
    """Verify the function ``encode`` works."""
    output = encode(
        text='''
        ZW5jb2Rpbmc6IGNvZGVjX3Rlc3QuanMgYnkgU3lzdGVtIEV5ZSBUaHJlYWR5XG4gICAgICAgICAgICAgICAgICAgICAgICAgIENvcHlyaWdodCAoRCkgMjAxN1xu
        '''
    )
    assert output[0] == b'\xda\x02\x1a\x17encoding: codec_test.js by System Eye Thready\nCopyright (c) 2017'
    assert output[1] == 181



# Generated at 2022-06-13 20:29:30.740566
# Unit test for function register
def test_register():
    """Test the codec registration."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise ValueError(f'{NAME} is already registered')
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise ValueError(f'{NAME} failed to register')
    else:
        pass



# Generated at 2022-06-13 20:29:31.548761
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:29:35.987769
# Unit test for function register
def test_register():
    """Test the the ``b64`` codec is registered after calling register().
    """
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            f'The {NAME!r} codec is already registered.'
        )

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            f'The {NAME!r} codec is not registered.'
        )



# Generated at 2022-06-13 20:29:43.087783
# Unit test for function register
def test_register():
    """Test the module's ``register`` function."""
    import sys
    try:
        register()
    except Exception as e:  # pylint: disable=broad-except
        print(
            'FAILED: module.register() => {}'.format(e),
            file=sys.stderr,
        )
        raise



# Generated at 2022-06-13 20:29:51.526621
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    # If the codec has not been register, the 'register' call should
    #  successfully register the codec.
    register()
    # Cleanup
    codecs.lookup(NAME).decode = None
    codecs.lookup(NAME).encode = None
    codecs.lookup(NAME).incrementalencoder = None
    codecs.lookup(NAME).incrementaldecoder = None
    codecs.lookup(NAME).streamreader = None
    codecs.lookup(NAME).streamwriter = None
    # If the codec has already been register, the 'register' call should
    #  not attempt to register the codec again.  This is determined by
    #  the fact that that if register() is called a second time, no
    #  exception should be raised.
