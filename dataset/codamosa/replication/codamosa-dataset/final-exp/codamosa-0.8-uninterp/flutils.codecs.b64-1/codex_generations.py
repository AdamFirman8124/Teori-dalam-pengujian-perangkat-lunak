

# Generated at 2022-06-13 20:21:47.804492
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)


# Register the codec when this module is loaded.
register()

# Generated at 2022-06-13 20:21:50.219553
# Unit test for function register
def test_register():
    """Test that the b64 codec has been registered with Python."""
    register()
    assert NAME in codecs.getencodings()


# Generated at 2022-06-13 20:21:56.829642
# Unit test for function encode
def test_encode():
    """Test case for function encode"""

# Generated at 2022-06-13 20:22:07.324282
# Unit test for function encode

# Generated at 2022-06-13 20:22:18.585680
# Unit test for function encode
def test_encode():
    test_string = '''
    aGVsbG8gd29ybGQ=
    '''

    result = encode(test_string)
    assert b'hello world' == result[0]
    assert len(test_string) == result[1]

    test_string = '''
    aGVsbG8gd29ybGQ=
    '''

    result = encode(test_string)
    assert b'hello world' == result[0]
    assert len(test_string) == result[1]

    test_string = '''
    aGVsbG8gd29ybGQ=
    '''

    result = encode(test_string)
    assert b'hello world' == result[0]
    assert len(test_string) == result[1]


# Generated at 2022-06-13 20:22:23.757319
# Unit test for function register
def test_register():
    """test_register"""
    register()
    assert codecs.lookup(NAME).name == NAME
    assert codecs.lookup(NAME).encode == encode
    assert codecs.lookup(NAME).decode == decode



# Generated at 2022-06-13 20:22:25.732730
# Unit test for function register
def test_register():
    """Test the function 'register'. """
    _ = NAME
    register()



# Generated at 2022-06-13 20:22:33.297941
# Unit test for function encode
def test_encode():
    result = list(map(
        lambda x: x[0],
        map(
            lambda x: encode(bytes(
                    list(map(lambda y: int(y, 16), x.split(' ')))
            )),
            test_b64_map.values()
        )
    ))
    for i in range(len(result)):
        assert result[i] == test_b64_map[i]


# Generated at 2022-06-13 20:22:42.275175
# Unit test for function encode
def test_encode():
    """Test the function :func:`encode`."""
    for test_dict in [
        {
            'name': 'basic text',
            'input': 'A test string.',
            'expected': b'A test string.',
        },
        {
            'name': 'multiline text',
            'input': """
                A test string.
                another line.
            """,
            'expected': b'A test string.another line.',
        },
    ]:
        with pytest.raises(UnicodeEncodeError) as exc_info:
            encode(test_dict['input'])
        assert exc_info.value.reason == (
            f'{test_dict["input"]!r} is not a proper bas64 character string: '
            'Incorrect padding'
        )


# Unit

# Generated at 2022-06-13 20:22:44.123355
# Unit test for function register
def test_register():
    import sys

    register()
    assert NAME in sys.modules



# Generated at 2022-06-13 20:22:49.972205
# Unit test for function register
def test_register():
    """The ``b64`` codec can be registered with Python."""
    register()
    import codecs
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:55.164331
# Unit test for function register
def test_register():

    # Verify the codec is not registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register the codec and verify it is registered.
    register()
    codecs.getdecoder(NAME)
#

# Generated at 2022-06-13 20:23:04.780492
# Unit test for function encode
def test_encode():
    # Test the negative case
    test_string = "Hello, World!"
    test_bytes = test_string.encode('utf-8')
    data = b'YmFzZTY0IGlzIGZ1bg==' # base64 is fun
    try:
        encode(data)
    except UnicodeEncodeError as e:
        assert str(e) == "b64: 'YmFzZTY0IGlzIGZ1bg==' is not a proper bas64 character string: Incorrect padding"
    # Test the positive case
    test_output = encode(test_bytes)
    assert type(test_output[0]) == type(test_bytes)
    for i in range(0, len(test_output[0])):
        assert test_output[0][i] == test_bytes[i]

# Generated at 2022-06-13 20:23:14.768339
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('\n') == (b'\n', 1)
    assert encode('\n\n') == (b'\n\n', 2)
    assert encode('\n\n\n') == (b'\n\n\n', 3)
    assert encode('S') == (b'Uw==', 1)
    assert encode('SA') == (b'U0E=', 1)
    assert encode('SAB') == (b'U0FC', 1)
    assert encode('SABA') == (b'U0FCQQ==', 1)
    assert encode('SABAC') == (b'U0FCQ0M=', 1)
    assert encode('SABACO') == (b'U0FCQ09P', 1)

# Generated at 2022-06-13 20:23:18.247084
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:20.668715
# Unit test for function register
def test_register():
    """Test the ``b64`` codec registration."""
    register()

    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:30.586703
# Unit test for function register
def test_register():
    """Test function register and the module codecs."""
    import sys

    # Ensure that the regioster fucntion works.
    register()

    # Ensure that the codec was properly registered
    assert getattr(sys.modules['codecs'], '__all__', None) is not None

    try:
        assert codecs.getdecoder(NAME) is not None
    except LookupError:
        assert False, f'unable to locate decoder for {NAME}'

    try:
        assert codecs.getencoder(NAME) is not None
    except LookupError:
        assert False, f'unable to locate encoder for {NAME}'

# Generated at 2022-06-13 20:23:32.667260
# Unit test for function register
def test_register():   # pylint: disable=R0201,W0613
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:35.808450
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    try:
        register()
    except:
        assert False, 'register failed.'
    assert True



# Generated at 2022-06-13 20:23:42.562285
# Unit test for function register
def test_register():
    # Test registering the codec for the first time.
    register()
    decoder = codecs.getdecoder(NAME)
    assert NAME == decoder.__name__

    # Test re-registering the codec.  This should not cause an error.
    register()
    decoder = codecs.getdecoder(NAME)
    assert NAME == decoder.__name__

# Generated at 2022-06-13 20:23:49.614999
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    from coders.encodings import register

    register()

# Generated at 2022-06-13 20:23:51.157728
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # noqa
    codecs.getencoder(NAME)  # noqa



# Generated at 2022-06-13 20:24:02.629863
# Unit test for function encode
def test_encode():
    # only run test in case this doesn't run as a module
    # unit test will otherwise run twice
    if __name__ != '__main__':
        return
    import os
    import sys
    import unittest

    class TestB64Encoder(unittest.TestCase):
        """ Tests for function encode """

        def test_encode(self):
            """Encode a base64 string"""
            username = b'admin'
            encoded = b'YWRtaW4='
            self.assertEqual(
                base64.b64encode(username),
                encoded
            )

        def test_encode_two(self):
            """Encode a longer base64 string"""
            username = b'administrator'
            encoded = b'YWRtaW5pc3RyYXRvcg=='

# Generated at 2022-06-13 20:24:07.623682
# Unit test for function register
def test_register():
    from unittest.mock import patch

    with patch('codecs.register', create=True) as mock:
        register()
        mock.assert_called_once()
        call = mock.call_args
        assert call.kwargs == {
            'search_function': _get_codec_info,
        }



# Generated at 2022-06-13 20:24:10.638509
# Unit test for function register
def test_register():
    """Test function register()"""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None

# Generated at 2022-06-13 20:24:18.270735
# Unit test for function register
def test_register():
    """Test function 'b64.register'"""
    TEST_REGISTER = 'test_register'

    # Empty the codecs
    codecs.clear_cache()

    # Make sure the TEST_REGISTER codec is not registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(TEST_REGISTER)

    # Register the TEST_REGISTER codec
    codecs.register(TEST_REGISTER, codecs.BOM_UTF8, 'ignore')

    # Get the TEST_REGISTER codec
    codec = codecs.getdecoder(TEST_REGISTER)
    assert codec

    # Get the TEST_REGISTER codec again
    codec = codecs.getdecoder(TEST_REGISTER)
    assert codec

    # Empty the codecs
    codecs.clear_cache()

    #

# Generated at 2022-06-13 20:24:20.203597
# Unit test for function register
def test_register():
    assert 'b64' not in codecs.__dict__
    register()
    assert 'b64' in codecs.__dict__

# Generated at 2022-06-13 20:24:25.686012
# Unit test for function register
def test_register(): # type: ignore[no-redef]
    """Unit test for function register."""
    from sys import modules  # type: ignore
    from b64 import register  # type: ignore

    del modules['b64']
    register()
    assert modules['b64'] is not None



# Generated at 2022-06-13 20:24:31.678298
# Unit test for function register
def test_register():
    """Unit tests for the register function."""
    register()
    obj = codecs.getdecoder(NAME)   # type: ignore
    assert obj is not None
    enc_obj = codecs.getencoder(NAME)  # type: ignore
    assert enc_obj is not None



# Generated at 2022-06-13 20:24:34.795069
# Unit test for function register
def test_register():
    # Should not raise any exception.
    register()


# pylint: disable=W0613
# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:24:46.262791
# Unit test for function encode
def test_encode():
    assert(
        encode('TmVzdGl2ZSBmbHVlYm9jaG8sIEkgbXkgcmlzZSB3aWxsIGJlIG15IGJlYXNl,') ==
        (b'Nestive flueboco, I my rise will be my base,', 63)
    )



# Generated at 2022-06-13 20:24:49.558292
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# pylint: disable=missing-docstring

# Generated at 2022-06-13 20:24:54.220801
# Unit test for function register
def test_register():
    """

    Returns:

    """
    register()
    assert NAME == 'b64'
    text = 'Hello, World!'
    assert bytes(text, "b64") == text.encode()
    assert bytes(text.encode(), "b64") == text.encode()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:55.742414
# Unit test for function register
def test_register():
    """Unit test for the function ``register``."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:56.892202
# Unit test for function register
def test_register():
    """Unit test for ``register()``."""
    register()



# Generated at 2022-06-13 20:24:59.647211
# Unit test for function encode
def test_encode():
    """
    test :function encode
    """
    encoded = codecs.encode("SURENDRA", "b64")
    assert encoded.decode('utf-8') == 'U1VSRU5EUkE='

#Unit test for function decode

# Generated at 2022-06-13 20:25:11.336858
# Unit test for function encode
def test_encode():
    """Test the encode function."""
    assert(encode("")[0] == b"")
    assert(encode("\n",) == b"")
    assert(encode("\t")[0] == b"")
    assert(encode("\t\n")[0] == b"")
    assert(encode("\n\n")[0] == b"")
    assert(encode("\n\t\n")[0] == b"")
    assert(encode("\n\n\n")[0] == b"")
    assert(encode("\n\n\t\n")[0] == b"")
    assert(encode("Zg==")[0] == b"f")
    assert(encode("Zm8=",)[0] == b"fo")
   

# Generated at 2022-06-13 20:25:14.065383
# Unit test for function register
def test_register():
    """Test the codec registration works."""
    register()
    assert codecs.lookup(NAME) == _get_codec_info(NAME)



# Generated at 2022-06-13 20:25:16.908530
# Unit test for function encode
def test_encode():
    assert encode('"Hello World"') == (b'SGVsbG8gV29ybGQ=', 13)



# Generated at 2022-06-13 20:25:24.012593
# Unit test for function register
def test_register():
    """Unit test for function register."""
    result = codecs.getdecoder(NAME)
    assert result[0].__name__ == NAME


# Execute the module directly when run as a program.
if __name__ == '__main__':
    # Register the custom b64 codec.
    register()

    # Call the built-in doctest module to automatically check the module
    # examples in the docstring.
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:25:31.761318
# Unit test for function register
def test_register():
    """Test the given register() function."""
    register()
    codec = codecs.getdecoder(NAME)     # type: ignore
    assert codec is not None
    assert codec[0] == decode
    codec = codecs.getencoder(NAME)     # type: ignore
    assert codec is not None
    assert codec[0] == encode

# Generated at 2022-06-13 20:25:38.219806
# Unit test for function register
def test_register():
    import sys

    # Remove the ``register`` function from the module system
    del sys.modules[__name__].register

    # Register the ``b64`` codec with Python
    register()

    # Import the ``b64`` codec
    import b64 as b64_module  # type: ignore

    # Dereference the ``b64`` codec's name
    name = b64_module.NAME

    # Get the ``b64`` codec
    codec_info = b64_module._get_codec_info(name)  # type: ignore

    # Assert that the ``b64`` codec is not None
    assert codec_info is not None

# Generated at 2022-06-13 20:25:40.449003
# Unit test for function register
def test_register():
    """Test function register."""
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:43.454030
# Unit test for function encode
def test_encode():
    """
    >>> test_encode()
    b'Leap year.'
    """
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 20:25:55.803085
# Unit test for function register
def test_register():    # pragma: no cover
    """Unit test to ensure the codec is registered properly."""
    # Check if the codec is already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # Run the register function.
        register()

    # Verify that the codec is correctly registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # If the codec is not registered, raise an error.
        raise AssertionError(
            f'The {NAME} codec was not registered properly.'
        )


# Unit Test for function decode

# Generated at 2022-06-13 20:25:57.798627
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:26:04.908880
# Unit test for function register
def test_register():
    import sys
    import pytest

    def get_decoder(name):
        try:
            return codecs.getdecoder(name)
        except LookupError:
            return None

    test_codec_name = 'b64'

    # Save current registered codecs
    original_codecs = dict(codecs.__dict__['_cache'])

    if get_decoder(test_codec_name) is None:
        # Register the codec
        register()
        assert get_decoder(test_codec_name) is not None
    else:
        # Remove the codec
        del codecs.__dict__['_cache'][test_codec_name]
        assert get_decoder(test_codec_name) is None
    # Restore saved codecs

# Generated at 2022-06-13 20:26:14.863235
# Unit test for function register
def test_register():
    import sys

    # Remove the module from the sys.modules so a fresh copy
    # of this module is imported when the b64 codec is registered.
    sys.modules.pop(__name__, None)

    from . import b64  # pylint: disable=import-outside-toplevel

    # Register the codec with Python
    b64.register()

    # Get the codec
    codec = codecs.getdecoder(b64.NAME)

    # Make sure the codec exists.
    assert codec is not None



# Generated at 2022-06-13 20:26:18.339149
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # pylint: disable=W0612, W0613
    def codec_check(in_bytes: bytes, in_str: str) -> None:
        """Convert a string to bytes and back again.

        Args:
            in_bytes (bytes): The input bytes that will be converted
                to a string.
            in_str (str): The string that is created from the input
                bytes.
        """
        # Convert the 'in_str' to 'out_bytes'.
        out_bytes, length_in_str = codecs.getencoder(NAME)(in_str)
        assert length_in_str == len(in_str)

        # Verify the 'in_bytes' and 'out_bytes' are the same.
        assert in_bytes == out_bytes

        # Convert

# Generated at 2022-06-13 20:26:27.551859
# Unit test for function encode
def test_encode():
    """Test function encode()
    """
    assert encode('') == (b'', 0)
    assert encode('Zg==') == (b'f', 4)
    assert encode('Zm8=') == (b'fo', 4)
    assert encode('Zm9v') == (b'foo', 4)
    assert encode('Zm9vYg==') == (b'foob', 8)
    assert encode('Zm9vYmE=') == (b'fooba', 8)
    assert encode('Zm9vYmFy') == (b'foobar', 8)
    assert encode('AA==') == (b'\x00', 4)
    assert encode('AAA=') == (b'\x00\x00', 4)

# Generated at 2022-06-13 20:26:37.610687
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert NAME in codecs.getdecoder(NAME)   # type: ignore
    assert NAME in codecs.getencoder(NAME)   # type: ignore
    assert codecs.encode("abc", NAME)[0] == b'YWJj'
    assert codecs.decode("YWJj", NAME)[0] == 'abc'

# Register the 'b64' with Python.
register()

# Generated at 2022-06-13 20:26:47.131355
# Unit test for function register
def test_register():
    def assign_to_codecs_getencoder():
        codecs.getencoder(NAME)
    def assign_to_codecs_getdecoder():
        codecs.getdecoder(NAME)
    def assign_to_codecs_getincrementalencoder():
        codecs.getincrementalencoder(NAME)
    def assign_to_codecs_getincrementaldecoder():
        codecs.getincrementaldecoder(NAME)
    assign_to_codecs_getdecoder.__annotations__ = {}
    assign_to_codecs_getencoder.__annotations__ = {}
    assign_to_codecs_getincrementalencoder.__annotations__ = {}
    assign_to_codecs_getincrementaldecoder.__annotations__ = {}


# Generated at 2022-06-13 20:26:52.155103
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # If the codec was not registered, the test failed.
        assert False, f'Codec {NAME!r} not found'


# Generated at 2022-06-13 20:26:54.966660
# Unit test for function register
def test_register():
    """Test that codec is found when looking for ``b64``."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:59.939071
# Unit test for function register
def test_register():
    """Test the ``register()`` function by calling it and verifying
    that the codec is registered.
    """
    register()
    if NAME not in codecs.__all__:   # type: ignore[attr-defined]
        raise AssertionError("failed to register the b64 codec")

# Generated at 2022-06-13 20:27:07.667268
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    assert encode('YQ==')[0] == b'a'
    assert encode('YWI=')[0] == b'ab'
    assert encode('YWJj')[0] == b'abc'
    assert encode('YWJjZA==')[0] == b'abcd'
    assert encode('YWJjZGU=')[0] == b'abcde'
    assert encode('YWJjZGVm')[0] == b'abcdef'
    assert encode('YWJjZGVmZw==')[0] == b'abcdefg'
    assert encode('YWJjZGVmZ2g=')[0] == b'abcdefgh'
    assert encode('YWJjZGVmZ2hp')[0] == b

# Generated at 2022-06-13 20:27:08.927110
# Unit test for function register
def test_register():      # pragma: no cover
    codecs.register(None) # type: ignore

# Generated at 2022-06-13 20:27:17.448989
# Unit test for function register
def test_register():
    """Test that the b64 codec is registered"""
    # Get the codec information from the codecs.getdecoder function.
    try:
        codec_info = codecs.getdecoder(NAME)        # type: ignore
    except LookupError as e:
        # The lookup error was raised.  A codec was not registered.
        assert False, f'Codec not registered: {e}'
    else:
        # The codec info was found.  Now make sure the decode and encode
        # functions are the same as our functions.
        assert (
            codec_info.decode == decode and
            codec_info.encode == encode
        )

if __name__ == '__main__':
    # Unit test for function encode
    def test_encode():
        """Test that the b64 encode function works"""

# Generated at 2022-06-13 20:27:24.038062
# Unit test for function register
def test_register():
    """Unit test for the function register"""
    register()

    assert NAME in [_[0] for _ in codecs.lookup_error('strict')]
    assert NAME in [_.name for _ in codecs.iterdecoders()]
    assert NAME in [_.name for _ in codecs.iterencoders()]


# Unit Test for function encode

# Generated at 2022-06-13 20:27:29.427231
# Unit test for function register
def test_register():
    import codecs
    from _b64 import register
    register()
    str_encoded = codecs.encode('Hello World!', 'b64')
    str_decoded = codecs.decode(str_encoded, 'b64')
    assert str_decoded == 'Hello World!'
    assert codecs.decode(b'SGVsbG8NCldvcmxkIQ==', 'b64') == 'Hello\nWorld!'
    assert codecs.decode(b'SGVsbG8NCldvcmxkIQ==\r', 'b64') == 'Hello\nWorld!'



# Generated at 2022-06-13 20:27:46.530762
# Unit test for function register
def test_register():
    register()

    # Verify that the decoder exists.
    try:
        # noinspection PyUnusedLocal
        decoder = codecs.getdecoder(NAME)
    except LookupError:
        assert False  # noqa

    # Verify that the encoder exists.
    try:
        # noinspection PyUnusedLocal
        encoder = codecs.getencoder(NAME)
    except LookupError:
        assert False  # noqa



# Generated at 2022-06-13 20:27:55.033523
# Unit test for function encode
def test_encode():
    assert encode('wew') == (b'cGV3', 3)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew  \n') == (b'cGV3', 6)
    assert encode('wew  \n') == (b'cGV3', 6)
    assert encode('wew\n') == (b'cGV3', 4)
    assert encode('wew\n') == (b'cGV3', 4)

# Generated at 2022-06-13 20:28:01.833729
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # pylint: disable=redefined-outer-name
    assert NAME not in codecs.getencoders()
    assert NAME not in codecs.getdecoders()
    register()
    assert NAME in codecs.getencoders()
    assert NAME in codecs.getdecoders()
    # pylint: enable=redefined-outer-name


register()


# Generated at 2022-06-13 20:28:13.598402
# Unit test for function encode
def test_encode():
    """Test the encoding function."""
    line1 = '.. ..'
    line2 = '.. ..'
    line3 = ''
    line4 = '  .. .. ..'

    # Test empty input.
    assert encode('') == (
        b'',
        0,
    )
    assert encode('\n') == (
        b'',
        1,
    )
    assert encode('\n\n') == (
        b'',
        2,
    )

    # Test non-base64 input.
    non_b64 = 'I am not a base64 string.'
    with pytest.raises(UnicodeEncodeError, match='{!r} is not a proper'.format(non_b64)):
        encode(non_b64)

    # Test different input cases.
    assert encode

# Generated at 2022-06-13 20:28:19.819498
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    import sys
    import unittest

    class TestRegister(unittest.TestCase):
        """TestCase for function ``register``."""

        @classmethod
        def setUpClass(cls):
            """Set up for the test suite."""
            register()

        def test_codec_found(self) -> None:
            """Verify that the ``b64`` codec is installed."""
            with self.subTest(name='b64 decode'):
                self.assertIn(NAME, codecs.__dict__)
            with self.subTest(name='b64 encode'):
                self.assertIn(NAME, codecs.__dict__)


# Generated at 2022-06-13 20:28:22.328364
# Unit test for function register
def test_register():
    """Validate the function 'register' in this module."""
    register()



# Generated at 2022-06-13 20:28:26.045141
# Unit test for function encode
def test_encode():
    input_text = b'abcd'
    expected_output, expected_length = codecs.decode(input_text, 'base64')
    actual_output, actual_length = encode(input_text)
    assert expected_output == actual_output
    assert expected_length == actual_length



# Generated at 2022-06-13 20:28:32.877343
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    output = (b'The quick brown fox jumps over the lazy dog.', 43)
    assert encode(
        '''VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4='''
    ) == output


# Generated at 2022-06-13 20:28:38.208936
# Unit test for function register
def test_register():
    codecs.getencoder(NAME)
#
#
# # Unit test for function encode
# def test_encode():
#     assert(encode('aGVsbG8=') == b'hello')
#
#
# # Unit test for function decode
# def test_decode():
#     assert(decode(b'hello') == 'aGVsbG8=')

# Generated at 2022-06-13 20:28:41.541545
# Unit test for function register
def test_register():
    """Test function b64.register"""
    codecs.register = mock.MagicMock()
    codecs.getdecoder = mock.MagicMock()
    register()
    codecs.register.assert_called_once()



# Generated at 2022-06-13 20:29:12.106991
# Unit test for function encode
def test_encode():
    utf16_bytes = b'I\x00 \x00a\x00m\x00 \x00t\x00e\x00s\x00t\x00i\x00n\x00g\x00 \x00b\x00a\x00s\x00e\x006\x004\x00 \x00c\x00o\x00d\x00e\x00c\x00 \x00d\x00e\x00c\x00o\x00d\x00e\x00r\x00.\x000\x00'
    text = "I am testing base64 code\ncodec decoder."
    assert encode(text) == (utf16_bytes, 1)

# Generated at 2022-06-13 20:29:16.609790
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__['_cache']  # type: ignore

    register()
    assert NAME in codecs.__dict__['_cache']  # type: ignore



# Generated at 2022-06-13 20:29:22.510270
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # Call the function 'register'.
    register()

    codec = codecs.getdecoder(NAME)  # type: Optional[codecs.CodecInfo]
    assert codec is not None
    assert codec.name == NAME

    codec = codecs.getencoder(NAME)  # type: Optional[codecs.CodecInfo]
    assert codec is not None
    assert codec.name == NAME

# Generated at 2022-06-13 20:29:29.752445
# Unit test for function encode
def test_encode():
    # Base64 Decode
    # "VGhpcyBhIHN0cmluZyB3aXRoIGNoYXJhY3RlcnMh"
    # ==> "This a string with characters!"

    decoded_str: bytes = b"This a string with characters!"
    test_str: str = "This a string with characters!"
    encoded_str: str = "VGhpcyBhIHN0cmluZyB3aXRoIGNoYXJhY3RlcnMh"

    assert encode(test_str) == (decoded_str, len(test_str))
    assert decode(decoded_str) == (encoded_str, len(decoded_str))



# Generated at 2022-06-13 20:29:33.208237
# Unit test for function register
def test_register():
    """Encode input using the b64 codec.  The input is a string
    consisting of only lowercase letters."""
    register()
    assert codecs.getdecoder(NAME)   # type: ignore
    assert codecs.getencoder(NAME)   # type: ignore



# Generated at 2022-06-13 20:29:34.781348
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    assert codecs.getdecoder(NAME)[0] == decode

# Generated at 2022-06-13 20:29:38.764118
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    assert None


codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:29:45.440997
# Unit test for function register
def test_register():
    """Test the b64.register() function."""
    # Get the current b64 codec.  If it does not exist, then register
    # b64 with Python.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, f"The {NAME} codec is not registered"



# Generated at 2022-06-13 20:29:47.418591
# Unit test for function register
def test_register():
    """Unit Test for function register"""
    register()
    _ = codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:49.863962
# Unit test for function register
def test_register():
    """Unit test for :func:`register`."""
    # Verify the 'b64' codec is not already present.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
    # Register the codec.
    register()
    # Verify the 'b64' codec exists.
    codecs.getdecoder(NAME)
    # Verify the, 'b64' codec can encode.
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:30:24.119241
# Unit test for function encode
def test_encode():
    assert encode(
        """
        foo bar
        baz qux
        """
    )[0] == b'Zm9vIGJhcgpiYXogcXV4'
    assert encode(
        """
        Zm9vIGJhcgpiYXogcXV4
        """
    )[0] == b'Zm9vIGJhcgpiYXogcXV4'
    assert encode('')[0] == b''
    assert encode('  \n\t ')[0] == b''
    return


# Generated at 2022-06-13 20:30:26.521445
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # Shouldn't raise exception.
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:30:28.368006
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore


# Generated at 2022-06-13 20:30:32.557924
# Unit test for function encode
def test_encode():
    """Test encoding of a text into base64 bytes."""
    the_text = '''
        YmxhaAo=
    '''
    the_bytes, _ = encode(the_text)
    assert the_bytes == b'blah\n'



# Generated at 2022-06-13 20:30:36.642333
# Unit test for function register
def test_register():
    """
    Test that 'register()' actually registers the codec with Python.
    """
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:30:39.692991
# Unit test for function register
def test_register():
    """Register the codec to test it."""
    register()


if __name__ == '__main__':
    print('Running unit tests...')
    test_register()
    print('Done.')

# Generated at 2022-06-13 20:30:44.961769
# Unit test for function register
def test_register():
    """Unit test for the register() function"""

    def _get_decoder(name: str) -> codecs.CodecInfo:
        """Get the decoder for the given name.

        Args:
            name (str): The name of the codec to get the decoder for.
        """
        return codecs.getdecoder(name)

    register()

    decoder = _get_decoder(NAME)

    assert NAME == decoder.name
    assert decode == decoder.decode
    assert encode == decoder.encode


# Generated at 2022-06-13 20:30:47.552776
# Unit test for function register
def test_register():
    """Test function register"""
    register()
    assert NAME in codecs.getencodings()



# Generated at 2022-06-13 20:30:49.821636
# Unit test for function register
def test_register():
    """Test registering the codecs."""
    register()



# Generated at 2022-06-13 20:30:51.774584
# Unit test for function register
def test_register():
    """Test the codec registration."""
    import codecs
    register()
    codecs.getdecoder('b64')