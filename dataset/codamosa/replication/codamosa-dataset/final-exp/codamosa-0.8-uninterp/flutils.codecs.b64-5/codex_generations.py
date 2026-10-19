

# Generated at 2022-06-13 20:21:50.983418
# Unit test for function register
def test_register():

    # pylint: disable=protected-access
    from asciistuff import codecs as asciistuff_codecs

    # Get the number of codecs before registering the 'b64' codec.
    codecs_before = len(codecs.__all__)

    # Check that the 'asciistuff_codecs' module does not have the b64
    # codec.
    assert NAME not in asciistuff_codecs.__all__

    # Register the 'b64' codec.
    register()

    # Get the number of codecs after registering the 'b64' codec.
    codecs_after = len(codecs.__all__)

    # Verify that the number of codecs has increased by 1.
    assert codecs_after == codecs_before + 1

    # Check that the 'asci

# Generated at 2022-06-13 20:21:56.343926
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__
    decoder = codecs.getdecoder(NAME)
    assert 'b64' == decoder.__code__.co_name
    assert 'strict' == decoder.__defaults__[0]
    assert 'strict' == decoder.__kwdefaults__['errors']
    assert ('text',) == decoder.__code__.co_varnames
    assert ('errors',) == decoder.__code__.co_varnames[1:]
    assert 'b64_encode' == codecs.getencoder('b64').__code__.co_name

# Generated at 2022-06-13 20:22:04.057544
# Unit test for function register
def test_register():
    """Test the function 'register()'."""
    register()
    result = (
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        == b'U0FCREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h'
                 b'5eg=='.decode(NAME)
    )
    assert result
test_register()

# Generated at 2022-06-13 20:22:13.783885
# Unit test for function register
def test_register():  # pragma: no cover
    """
    Unit test for function register.
    """
    import sys
    import unittest

    # pylint: disable=C0301
    sys.modules['codecs'] = codecs
    codecs.getdecoder = lambda name: None
    codecs.CodecInfo = codecs.CodecInfo
    codecs.register = lambda x: None
    decode = decode
    encode = encode

    # Prevent changes to the global namespace
    global decode_b64, encode_b64
    decode_b64 = decode
    encode_b64 = encode

    class TestRegister(unittest.TestCase):
        """
        TestRegister is a collection of unit tests for function register
        """
        def test_register(self):
            """
            Test function register.
            """
            actual = register

# Generated at 2022-06-13 20:22:19.752562
# Unit test for function encode
def test_encode():
    # Setup
    text = """
    ZXhhbXBsZS1mb3ItZ3VpZC50eHQ=
    """
    expected = """
    example-for-guid.txt
    """

    # Test
    actual = encode(text)

    # Validate
    assert expected == actual


# Generated at 2022-06-13 20:22:33.965569
# Unit test for function register
def test_register():
    """Test function register()"""
    from . import register as register_fn
    from os import unsetenv
    from os import getenv
    from os import environ
    from importlib import reload

    # Cleanup test environment variables.
    if 'PYTHONPATH' in environ:
        unsetenv('PYTHONPATH')

    # Replace the register function with a function that records the
    # environment variables.
    sys = __import__('sys')
    sys.path = []

    # Reload the module to remove 'register' from the module.
    reload(register_fn)
    from . import register as register_fn
    from . import codecs as codecs_module
    from . import NAME as codec_name

    importlib = __import__('importlib')

    env = {}

# Generated at 2022-06-13 20:22:38.239386
# Unit test for function register
def test_register():
    """Verify registering the ``b64`` codec with Python."""
    # unregister the codec to allow tests to be run multiple times
    codecs.unregister(NAME)
    register()
    assert codecs.getdecoder(NAME) is not None
    # unregister the codec to allow tests to be run multiple times
    codecs.unregister(NAME)



# Generated at 2022-06-13 20:22:41.862921
# Unit test for function register
def test_register():
    """Unit test function register."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:22:53.724311
# Unit test for function encode
def test_encode():
    """Unit test for function ``encode``."""
    # Test 1
    text = '''  
    aWQ6IG15c2VydmljZTp7ZW50cnlfdHlwZTogc2VydmljZSwgbmFtZTogc2FtcGxlIHNlcnZpY2UsIGNvbW1h
    bnk6IHNhbXBsZSBjb21wYW55   
    '''
    out, consumed = encode(text)
    #print(out)
    expected = b'id: myservice:{entry_type: service, name: sample service, company: sample company'
    assert out == expected
    assert consumed == len(text)

    # Test 2

# Generated at 2022-06-13 20:23:01.919062
# Unit test for function register
def test_register():  # pylint: disable=R0915

    import os
    import json
    import pathlib

    # There is no way to unregister a codec with the builtin 'codecs'
    # module.
    #
    # If the 'b64' codec is already registered with Python, then
    # attempting to register it again will result in an error.
    #
    # To avoid this error, if the 'b64' codec is already registered,
    # then do not attempt to register it.
    #
    # When the 'b64' codec is first registered with Python, the
    # 'codecs.py' file is updated with the 'b64' codec.  The updated
    # 'codecs.py' file is used when the next Python program is run.
    #
    # For example, if this Python program is executed twice, then

# Generated at 2022-06-13 20:23:15.575385
# Unit test for function encode

# Generated at 2022-06-13 20:23:16.815244
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:23:30.288036
# Unit test for function register
def test_register():
    """Test function `register`."""

    def _helper(data: bytes, errors: str,
                text: str, text_bytes: bytes) -> None:

        # Test decode with bytes.
        tup = codecs.decode(data, NAME, errors)  # type: ignore
        assert tup[0] == text
        assert tup[0] != text_bytes
        assert tup[1] == len(data)

        # Test decode with bytearray.
        tup = codecs.decode(bytearray(data), NAME, errors)   # type: ignore
        assert tup[0] == text
        assert tup[0] != text_bytes
        assert tup[1] == len(data)

        # Test encode with text.

# Generated at 2022-06-13 20:23:32.209229
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:23:34.436068
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)


# Generated at 2022-06-13 20:23:43.021277
# Unit test for function register
def test_register():
    """Unit test for function ``register``"""
    # pylint: disable=W0612
    # Test for register function.  Test for 'calc-codec-b64' at codecs
    codecs_registry = codecs._registry   # type: ignore
    register()
    # Test for 'calc-codec-b64' at codecs
    assert name in codecs_registry
    assert codecs_registry[name] == info


# Generated at 2022-06-13 20:23:52.378224
# Unit test for function register
def test_register():
    """Test that the b64 codec is registered."""
    # Before we call register() the b64 codec should not be found.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)

    # Now call register()
    register()

    # Now we should be able to get the decoder and encoder.
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Unit tests for function encode
# pylint: disable=C0103

# Generated at 2022-06-13 20:23:56.638697
# Unit test for function register
def test_register():
    """Test ``b64`` registered in Python."""
    register()
    assert codecs.getencoder(NAME) is encode   # type: ignore
    assert codecs.getdecoder(NAME) is decode   # type: ignore
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:24:08.273880
# Unit test for function encode
def test_encode():
    """Test the :func:`~encoding.b64.encode` function.
    """
    result = encode('HW')
    assert result == (b'HW', 2)

    result = encode('HU')
    assert result == (b'HU', 2)

    result = encode('H')
    assert result == (b'H', 1)

    result = encode('HW1\n')
    assert result == (b'HW1', 3)

    result = encode('HW1\nHW2')
    assert result == (b'HW1\nHW2', 5)

    result = encode('HW1\nHW2\n')
    assert result == (b'HW1\nHW2', 5)

    result = encode('HW1\n   HW2')


# Generated at 2022-06-13 20:24:13.603461
# Unit test for function register
def test_register():
    """Test function 'register'."""
    # pylint: disable=protected-access
    assert NAME not in codecs.__dict__['_cache']
    assert NAME not in codecs.__dict__['_unknown_encoding']

    register()
    assert NAME in codecs.__dict__['_cache']
    assert NAME not in codecs.__dict__['_unknown_encoding']



# Generated at 2022-06-13 20:24:18.748369
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert NAME in codecs.__all__

# Generated at 2022-06-13 20:24:24.491401
# Unit test for function encode
def test_encode():
    assert encode('dGhlIHNhbXBsZSBub25jZQ==') == (b'the simple nonce', 23)
    assert encode('aGVsbG8gd29ybGQ=') == (b'hello world', 15)
    assert encode('YWJj') == (b'abc', 4)


# Generated at 2022-06-13 20:24:27.643735
# Unit test for function register
def test_register():
    registry = codecs.registry                                 # type: ignore
    registry.append(codecs.CodecInfo('test_register', register))

# Generated at 2022-06-13 20:24:28.314109
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:32.034675
# Unit test for function register
def test_register():
    """Test to make sure that the given codec is a properly registered
    codec.  This function should be called in the unit tests only.
    """
    register()
    assert NAME in codecs.encode('', NAME).decode(NAME)

# Generated at 2022-06-13 20:24:35.085258
# Unit test for function register
def test_register():
    register()
    try:
        assert NAME in codecs.getdecoder(NAME).name
    except LookupError:
        assert False, '"b64" codec not registered'



# Generated at 2022-06-13 20:24:42.491157
# Unit test for function encode
def test_encode():
    """Unit test for module-level function 'encode'."""
    assert encode('') == (b'', 0)
    assert encode('Test') == (b'VGVzdA==', 4)
    assert encode('Test\nn') == (b'VGVzdG4=', 6)
    assert encode('\tTest\n') == (b'VGVzdA==', 8)
    assert encode('\tTest\n\n') == (b'VGVzdA==', 9)
    assert encode('  Test  ') == (b'VGVzdA==', 9)
    assert encode('  Test') == (b'VGVzdA==', 7)
    assert encode('Test\t') == (b'VGVzdA==', 6)
    assert encode('VGVzdA==')

# Generated at 2022-06-13 20:24:51.294178
# Unit test for function encode
def test_encode():
    assert encode('a') == (b'A==', 1)
    assert encode('ab') == (b'YWI=', 2)
    assert encode('abc') == (b'YWJj', 3)
    assert encode('abcd') == (b'YWJjZA==', 4)
    assert encode('z') == (b'eg==', 1)
    assert encode('z1') == (b'egE=', 2)
    assert encode('z12') == (b'egEy', 3)
    assert encode('z123') == (b'egEyMw==', 4)
    assert encode('abcdefgh') == (b'YWJjZGVmZ2g=', 8)


# Generated at 2022-06-13 20:24:57.264506
# Unit test for function encode
def test_encode():    # type: ignore
    assert encode('QQ==') == (b'A', 4)
    assert encode('8J+RkA==') == (b'test!', 10)
    assert encode('8J+RkQ==') == (b'test2', 10)
    assert encode('8J+\r') == (b'te', 5)
    assert encode('\r+RkA==') == (b'est!', 9)

    assert encode('QQ+++') == (b'A', 4)



# Generated at 2022-06-13 20:24:58.438299
# Unit test for function register
def test_register():
    """Test function register"""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:08.542828
# Unit test for function encode
def test_encode():
    """Test the ``encode`` function.
    """
    # Test converting base64 text into decoded bytes.
    text = '''
    bm90IGJhc2U2NA==
    '''
    assert encode(text) == (b'not base64', 17)



# Generated at 2022-06-13 20:25:10.783392
# Unit test for function register
def test_register():
    assert codecs.lookup(NAME) is None
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:16.981616
# Unit test for function register
def test_register():    # type: ignore # pragma: no cover
    """Test function register."""

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, 'Codec already registered'

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec not registered'
    else:
        assert True, 'Codec registered'



# Generated at 2022-06-13 20:25:22.556864
# Unit test for function register
def test_register():
    """Unit test for function register().

    This function has no return value.  The assert methods are used for
    the testing.
    """
    register()
    result = codecs.getdecoder(NAME)
    assert result[0].name == NAME
    assert result[0].decode == decode
    assert result[0].encode == encode



# Generated at 2022-06-13 20:25:27.988275
# Unit test for function register
def test_register():  # pragma: no cover
    # Simplest test case is to call this function in a Python session with
    # the following:
    # >>> import b64
    # >>> b64.register()
    #
    # This function will raise an error if the b64 codec is already registered.
    register()


if __name__ == '__main__':
    # pragma: no cover
    test_register()

# Generated at 2022-06-13 20:25:31.562321
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None
    assert codecs.lookup_error('strict') is not None


if __name__ == '__main__':
    register()



# Generated at 2022-06-13 20:25:34.530366
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    register()

    codec_info = codecs.getdecoder(NAME)   # type: ignore
    assert codec_info.name == NAME



# Generated at 2022-06-13 20:25:43.164261
# Unit test for function register
def test_register():
    """Test the function register
    """
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)  # type: ignore

    coder = codecs.getdecoder(NAME)
    encoded_text = "UEFTU1ZJTEU="
    expected = "TESTVALUE"
    decoded, size = coder(encoded_text)
    assert decoded == expected
    assert size == len(encoded_text)

# Generated at 2022-06-13 20:25:58.882274
# Unit test for function encode
def test_encode():
    """Test function ``encode``."""

# Generated at 2022-06-13 20:26:12.349761
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    import os
    import re
    import sys
    import unittest
    from common.cryptography import get_salt
    from common.cryptography import pbkdf2_sha256
    from common.cryptography import pbkdf2_sha512
    from common.cryptography import random_string
    from common.cryptography import sha256
    from common.cryptography import sha512

    class TestSHA256(unittest.TestCase):
        """
        Unit test for the :func:`~common.cryptography.sha256` function.
        """
        def test_single_words(self):
            self

# Generated at 2022-06-13 20:26:21.705914
# Unit test for function register
def test_register():
    codec_name = 'b64'

    assert codecs.getdecoder(codec_name) is None

    register()

    assert codecs.getdecoder(codec_name) is not None



# Generated at 2022-06-13 20:26:23.658558
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert isinstance(obj, codecs.CodecInfo)


# Generated at 2022-06-13 20:26:25.063269
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None

# Generated at 2022-06-13 20:26:29.368712
# Unit test for function register
def test_register():
    """Test function 'register'."""
    assert callable(register)
    register()
    assert NAME in codecs.getdecoder('b64')


# Generated at 2022-06-13 20:26:31.462406
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:40.856765
# Unit test for function register
def test_register():
    """Unit test for function register"""
    def _test_codec():
        """Convert a string of 'b64' characters to bytes and back again."""
        # Convert the given 'b64' character string into bytes.
        in_str = 'dGhpcyBpcyBzb21ldGhpbmcgZWxzZQ=='
        b64_bytes, len_b64_bytes = codecs.decode(  # type: ignore
            in_str,
            NAME
        )
        assert len_b64_bytes == len(in_str)

        # Convert the 'b64_bytes' into a string of 'b64' characters.
        out_str, len_out_str = codecs.encode(  # type: ignore
            b64_bytes,
            NAME
        )
        assert len_out

# Generated at 2022-06-13 20:26:44.694042
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    # Register the codec.
    register()

    # Check that the codec is now registered.
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:45.602141
# Unit test for function register
def test_register():
    """Unit test for the register() function"""
    register()

# Generated at 2022-06-13 20:26:47.826322
# Unit test for function register
def test_register():  # noqa
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)
    return


# Generated at 2022-06-13 20:26:52.225424
# Unit test for function register
def test_register():
    """Test the codecs.register function."""
    # Nothing to do here.  The test_<something> function is called by
    # the test_<something> function directly.
    pass



# Generated at 2022-06-13 20:27:08.460908
# Unit test for function register
def test_register():
    """Test for function register"""
    register()
    # Need to test that 'b64' is found by getdecoder.
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:27:11.772960
# Unit test for function register
def test_register():
    """This is a unit test to verify that function register() works properly
    """
    register()
    print("registration successful")

if __name__ == '__main__':
    # Unit test for function register
    test_register()

# Generated at 2022-06-13 20:27:15.803071
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
        assert codecs.getdecoder(NAME) is not None
    else:
        assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:27:25.897952
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # ##########
    # Arrange #
    # ##########
    # Capture the output of the 'print' function.
    _out, sys.stdout = sys.stdout, StringIO()

    # ##############
    # Act & Assert #
    # ##############
    # Register the 'b64' codec.
    register()

    # Ensure that registering the 'b64' codec created no output.
    assert sys.stdout.getvalue() == ''

    # Restore the prior 'stdout' reference.
    sys.stdout = _out


# Unit tests for function encode.

# Generated at 2022-06-13 20:27:26.807590
# Unit test for function register
def test_register():
    _ = register()

# Generated at 2022-06-13 20:27:34.699417
# Unit test for function register
def test_register():
    """Unit test for function register."""
    global NAME
    NAME_REVERSE = f'{NAME}.reverse'
    register()
    try:
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)

        with pytest.raises(LookupError):
            codecs.getdecoder(NAME_REVERSE)
        with pytest.raises(LookupError):
            codecs.getencoder(NAME_REVERSE)
    finally:
        codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:27:38.693865
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:49.579657
# Unit test for function register
def test_register():  # pragma: no cover
    """Test the b64 codec's register function."""
    codecs.register(_get_codec_info)
    expected = ('test', 3)
    given = codecs.decode('.dGVzdA==', 'b64')
    assert given == expected
    codecs.register(_get_codec_info)
    expected = 'dGVzdA=='
    given = codecs.encode(given[0], 'b64')
    assert given == expected


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:53.160790
# Unit test for function encode
def test_encode():
    # pylint: disable=missing-function-docstring
    assert encode(
        'dmFsdWU=',
        errors='strict'
    ) == (b'value', 9)



# Generated at 2022-06-13 20:27:57.352872
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.lookup(NAME) is not None
    codecs.lookup_error('loose')


# Unit tests for function encode

# Generated at 2022-06-13 20:28:19.058680
# Unit test for function encode
def test_encode():
    """Unit test that verifies the function ``encode`` encodes the
    given text into base64 bytes.
    """
    assert encode(
        text=
        ('TGV0J3MgdGhyb3cgdGhlIHByaW1lcyB0aHJvdWdoIGEgZnVuZG'
         'xpbmcgYW5kIHNlZSB3aGV0aGVyIGFueSBvZiB0aGVtIGhleCB0'
         'aGVtLg==')
    ) == (b'Let\'s throw the primes through a funding and see whether any of '
          b'them hex them.', 128)

# Generated at 2022-06-13 20:28:28.329082
# Unit test for function encode
def test_encode():
    """Unit test for function ``encode``."""
    from pytest import raises
    with raises(UnicodeEncodeError):
        encode('$9F')
    assert encode('4AvVhmFLUs0KTA3Kprsdag==')[0] == b'\x50\x51\x52\x53\x54\x55\x56\x57'
    assert encode('4AvVhmFLUs0KTA3Kprsdag==')[1] == 22
    assert encode('4AvVhmFLUs0KTA3Kprsdag==') == (b'\x50\x51\x52\x53\x54\x55\x56\x57', 22)

# Generated at 2022-06-13 20:28:30.957991
# Unit test for function register
def test_register():
    register()  # type: ignore
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:28:41.324527
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None
    expected = ('The quick brown fox jumped over the big log.', None)
    output = codec(
        'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgYmlnIGxvZy4=',
        None
    )
    assert output == expected
    output = codec(
        'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgYmlnIGxvZy4=',
        None
    )
    assert output == expected
    codec = codecs.getencoder(NAME)
    assert codec is not None
   

# Generated at 2022-06-13 20:28:42.998631
# Unit test for function encode
def test_encode():
    assert isinstance(encode('', 'strict'), type(bytes()))



# Generated at 2022-06-13 20:28:50.601398
# Unit test for function register
def test_register():
    """Test the register() function."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)  # type: ignore
    register()
    try:
        assert codecs.getdecoder(NAME)
    finally:
        # noinspection PyUnboundLocalVariable
        codecs.unregister(NAME)  # type: ignore

# Generated at 2022-06-13 20:28:54.703721
# Unit test for function register
def test_register():
    # pylint: disable=W0612,W0613
    def _test_register(name: str, func: Callable) -> bool:
        try:
            codecs.lookup(NAME)
        except LookupError:
            return False
        return True

    assert _test_register(NAME, register)


register()

# Generated at 2022-06-13 20:28:57.632324
# Unit test for function register
def test_register():
    """Test function register()."""
    # Verify that 'b64' is a valid codec.
    codecs.getencoder(NAME)  # type: ignore


register()

# Generated at 2022-06-13 20:29:03.521969
# Unit test for function register
def test_register():
    """Unit test for :func:`register`.

    Calling :func:`register` twice causes
    :func:`register` to raise an exception.
    """
    register()
    register()


try:
    register()
except Exception as e:
    import sys
    import traceback
    exc_info = sys.exc_info()
    error_msg = traceback.format_exception(*exc_info[:3])
    print(''.join(error_msg))
    raise e

# Generated at 2022-06-13 20:29:04.688372
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:35.062702
# Unit test for function register
def test_register():    # type: ignore
    """Test the register() function."""
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


if __name__ == '__main__':
    codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:29:43.186990
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
    obj = codecs.getdecoder(NAME)
    assert obj is not None
    assert obj.decode is decode
    assert obj.encode is encode



# Generated at 2022-06-13 20:29:45.475076
# Unit test for function register
def test_register():
    """Test the register method."""
    assert codecs.lookup(NAME) is None
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:29:47.113212
# Unit test for function encode
def test_encode():
    assert encode('YQ==') == (b'a', 3)



# Generated at 2022-06-13 20:29:50.474574
# Unit test for function register
def test_register():
    """Test for function register"""
    assert NAME not in codecs.getdecoder(NAME)
    register()
    assert NAME in codecs.getdecoder(NAME)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:29:53.687896
# Unit test for function register
def test_register():
    from codecs import getdecoder as codecs_getdecoder
    from errors import register as register_errors

    register_errors()
    codecs_getdecoder(NAME)

# Generated at 2022-06-13 20:29:55.352857
# Unit test for function register
def test_register():
    """Tests the function register."""
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)  # type: ignore



# Generated at 2022-06-13 20:29:57.541570
# Unit test for function encode
def test_encode():
    test_input = ('Zm9vYmFy')
    test_input_bytes = test_input.encode('utf-8')
    enc_b_str, _ = encode(test_input)

    assert enc_b_str == test_input_bytes



# Generated at 2022-06-13 20:30:01.284338
# Unit test for function encode
def test_encode():
    # Test for b64.encode(s, errors)
    cr = '\n'
    string = (f'T'
              f'e'
              f'x'
              f't')
    result = 'VGV4dA=='
    error = 'strict'
    assert encode(string, error) == (codecs.decode(result, 'base64'), len(string))


# Generated at 2022-06-13 20:30:07.419397
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode(' \t\n') == (b'', 0)
    assert encode('AQIDBAU=') == (b'\x01\x02\x03\x04\x05', 8)
    assert encode('\x01\x02\x03\x04\x05') == (b'AQIDBAU=', 8)
    assert encode(b'\x01\x02\x03\x04\x05') == (b'AQIDBAU=', 8)

# Generated at 2022-06-13 20:31:16.960437
# Unit test for function register
def test_register():
    """Unit test for function register"""
    from b64_codec.base64_codec import NAME
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None

# Generated at 2022-06-13 20:31:19.150655
# Unit test for function register
def test_register():
    """Tests for the function register."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:31:24.615581
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert isinstance(codecs.getencoder(NAME), codecs.CodecInfo)  # type: ignore
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)  # type: ignore

# Generated at 2022-06-13 20:31:33.601983
# Unit test for function encode
def test_encode():
    # Given
    text = (
        'AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRoaWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4e'
        'XpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0NTY3ODkrLw=='
    )

# Generated at 2022-06-13 20:31:38.018365
# Unit test for function encode
def test_encode():
    """Unit test for the ``encode`` function."""
    try:
        import doctest
    except ModuleNotFoundError:
        print(
            '\n'
            '*****************************************************************'
            '\n'
            '  WARNING: The doctest module is not installed.  The unittest for'
            '\n'
            '           the ``encode`` function will not be run.'
            '\n'
            '*****************************************************************'
            '\n'
        )
    else:
        doctest.testmod()



# Generated at 2022-06-13 20:31:42.928573
# Unit test for function register
def test_register():
    """Unit test for register"""
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None

