

# Generated at 2022-06-13 20:21:46.404540
# Unit test for function register
def test_register():
    """Test function register"""
    register()
    assert codecs.getencoder(NAME) is not None


if __name__ == '__main__':
    register()
    test_register()

# Generated at 2022-06-13 20:21:52.526594
# Unit test for function register
def test_register():
    """Unit tests for the function register in this module."""
    from codecs import getdecoder, getencoder
    try:
        getdecoder(NAME)
        raise Exception(
            f'The "{NAME}" codec should not be registered at the start of test'
        )
    except LookupError:
        pass

    try:
        getencoder(NAME)
        raise Exception(
            f'The "{NAME}" codec should not be registered at the start of test'
        )
    except LookupError:
        pass

    register()
    assert getdecoder(NAME)
    assert getencoder(NAME)



# Generated at 2022-06-13 20:21:53.740017
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    register()



# Generated at 2022-06-13 20:21:56.042841
# Unit test for function register
def test_register():
    from codecs import getencoder, getdecoder, lookup
    register()
    name = 'b64'
    assert getencoder(name) == encode
    assert getdecoder(name) == decode
    assert lookup(name)    # type: ignore


# Generated at 2022-06-13 20:21:58.449941
# Unit test for function register
def test_register():
    register()

    # Test that the b64 codec has been correctly registered.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:01.767497
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:06.300683
# Unit test for function encode
def test_encode():
    """Unit test for function ``encode``."""
    assert encode(b'abcd') == (b'YWJjZA==', 4)
    assert encode(b'abcd', errors='ignore') == (b'YWJjZA==', 4)
    assert encode(b'abcd', errors='replace') == (b'YWJjZA==', 4)
    assert encode(b'abcd', errors='xmlcharrefreplace') == (b'YWJjZA==', 4)
    assert encode(b'abcd', errors='strict') == (b'YWJjZA==', 4)
    assert encode(b'abcd', errors='backslashreplace') == (b'YWJjZA==', 4)

# Generated at 2022-06-13 20:22:12.045913
# Unit test for function register
def test_register():
    # pylint: disable=W0106
    """Test the ``register()`` function."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


# Execute this module's unit tests when this module is run as a script.
if __name__ == '__main__':
    remove_log_handlers()
    add_stderr_log_handler()
    unittest_main()

# Generated at 2022-06-13 20:22:14.159269
# Unit test for function register
def test_register():
    """Test if ``b64`` codec is registered."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:22:19.516371
# Unit test for function register
def test_register():
    """Test the :function:`register` function."""
    codecs.getdecoder(NAME)


if __name__ == "__main__":
    print(f"Running {NAME} module unit tests...")
    test_register()
    print("Tests completed.")

# Generated at 2022-06-13 20:22:34.572695
# Unit test for function encode
def test_encode():
    """Test the encode function."""
    def _test(
            text: str,
            expected: bytes
    ) -> None:
        nonlocal test_encoded_in, test_encoded_out, test_len
        test_encoded_in = text.encode('utf-8')
        test_encoded_out, test_len = encode(text)

# Generated at 2022-06-13 20:22:40.695931
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    codecs.lookup_error('ignore')
    codecs.lookup_error('replace')
    codecs.lookup_error('strict')
    codecs.lookup_error('xmlcharrefreplace')

    try:
        codecs.lookup_error('unknown')
    except LookupError:
        pass

    register()
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        assert False


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:53.393626
# Unit test for function register
def test_register():
    """Test case for function register"""
    from test.common import CaptureStdout
    from typing import Optional

    # Register the 'b64' codec
    register()

    # Get the 'b64' codec.
    codec = codecs.getdecoder(NAME)  # type: Optional[codecs.CodecInfo]

    # Ensure that the 'b64' codec is registered
    assert isinstance(codec, codecs.CodecInfo)

    # Ensure that the 'b64' codec can decode a string of base 64 characters
    # into bytes

# Generated at 2022-06-13 20:22:59.678775
# Unit test for function register
def test_register():
    """Test function register()."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(f"codecs.getdecoder({NAME!r}) should have "
                             "failed, but it did not.")
    register()

    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:23:10.240313
# Unit test for function register
def test_register():
    """Test the b64.register() function."""
    print('Testing b64.register()')
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
    try:
        codecs.getencoder(NAME)
    except LookupError:
        register()

    # Verify the presence of the b64 codec.
    assert codecs.lookup(NAME) is not None



# Generated at 2022-06-13 20:23:15.729945
# Unit test for function register
def test_register():
    """Unit test for function register."""
    assert NAME in {
        name
        for name in codecs.__dict__.get('_cache', {}).keys()
        if name is not None
    }
    assert NAME in {
        name
        for name in codecs.__dict__.get('_unknown_encoding_cache', {}).keys()
        if name is not None
    }


test_register()

# Generated at 2022-06-13 20:23:16.499041
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:23:18.508372
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()

# Generated at 2022-06-13 20:23:31.233176
# Unit test for function encode
def test_encode():
    """Unit test for function encode.

    Args:
        None

    Returns:
        None
    """
    expected = b'\xda\xb8\x81\x9a\x81\x90\x8c\xba'
    b64_string = '6r+G6r+9'
    result = codecs.decode(b64_string)
    assert expected == result
    expected = b'\x9e\x87\xcb\x80\xcb\x97\xc6\xb7'
    b64_string = '5rqr5rqr'
    result = codecs.decode(b64_string)
    assert expected == result
    expected = b'\x87\xcb\x80\xcb\x97\xc6\xb7\x9e'

# Generated at 2022-06-13 20:23:44.218677
# Unit test for function encode

# Generated at 2022-06-13 20:23:49.653435
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) == decode
    assert codecs.getencoder(NAME) == encode
    try:
        codecs.getdecoder('b64a')
    except LookupError:
        pass
    else:
        assert False



# Generated at 2022-06-13 20:23:51.598032
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:23:56.941247
# Unit test for function encode
def test_encode():
    assert encode('Hello')[0] == b'SGVsbG8='
    assert encode('Hello', errors='strict')[0] == b'SGVsbG8='
    assert encode('Hello', errors='replace')[0] == b'SGVsbG8='
    assert encode('Hello', errors='ignore')[0] == b'SGVsbG8='

# Generated at 2022-06-13 20:24:08.556002
# Unit test for function register
def test_register():
    """Unit tests for function ``register``"""
    # pylint: disable=protected-access
    from . import b64 as b64_module  # pylint: disable=cyclic-import
    from .b64 import _get_codec_info as get_codec_info

    # Test that function register registers:
    #   - Decoder
    #   - Encoder
    #   - Name
    # pylint: disable=W0703
    assert (
        NAME == 'b64'
        and b64_module.decode == get_codec_info(NAME).decode
        and b64_module.encode == get_codec_info(NAME).encode
    )
    return



# Generated at 2022-06-13 20:24:17.316485
# Unit test for function encode

# Generated at 2022-06-13 20:24:22.220846
# Unit test for function register
def test_register():
    """Unit Test for function :func:`register`."""
    register()
    assert codecs.getencoder(NAME)('a') == ('YQ==', 1)
    assert codecs.getdecoder(NAME)(b'YXNz') == ('ass', 3)


# Generated at 2022-06-13 20:24:25.800163
# Unit test for function register
def test_register():
    """Unit test function for function ``register``."""
    import types
    import unittest

    def _get_codec_info(name: str) -> Optional[codecs.CodecInfo]:
        assert name == NAME
        return NAME

    class CodecType(types.TypeType):
        def __init__(self, codec_info):
            super().__init__(codec_info)

        def decode(
            self,
            data: _ByteString,
            errors: _STR = 'strict'
        ) -> Tuple[str, int]:
            return str(data), len(data)

        def encode(
            self,
            text: _STR,
            errors: _STR = 'strict'
        ) -> Tuple[bytes, int]:
            return bytes(text), len(text)


# Generated at 2022-06-13 20:24:30.962739
# Unit test for function register
def test_register():
    """Unit-test the function ``register``."""
    # Unregister the 'NAME' codec.
    try:
        codecs.lookup(NAME).name
    except LookupError:
        pass
    else:
        codecs.unregister(codecs.lookup(NAME))

    # Register the 'NAME' codec.
    register()

    # Check that the 'NAME' codec is registered.
    assert codecs.lookup(NAME).name == NAME
    codecs.unregister(codecs.lookup(NAME))

# Generated at 2022-06-13 20:24:36.581279
# Unit test for function register
def test_register():
    """
    Ensure that the ``b64`` codec is registered.
    """
    assert NAME not in codecs.__dict__['_codec_aliases']['streamreader']
    register()
    assert NAME in codecs.__dict__['_codec_aliases']['streamreader']
    assert NAME not in codecs.__dict__['_codec_aliases']['streamwriter']

# Generated at 2022-06-13 20:24:38.422300
# Unit test for function register
def test_register():
    """Unit test for function register."""
    assert codecs.getdecoder(NAME)

register()

# Generated at 2022-06-13 20:24:44.277176
# Unit test for function register
def test_register():       # pylint: disable=unused-variable
    """Unit test for function register"""
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:24:52.314652
# Unit test for function encode
def test_encode():
    text = 'W3BtPgo8Ym9keT4KICA8aW1nIHNyYz0iZGF0YTppbWFnZS9wbmc7YmFzZTY0LHYtUT" \
           "cKW3BtPgo8Ym9keT4KICA8aW1nIHNyYz0iZGF0YTppbWFnZS9wbmc7YmFzZTY0LHYtUT'
    out = encode(text)
    assert out[1] == len(text)
    assert out[0] == base64.decodebytes(text.encode('utf-8'))


# Generated at 2022-06-13 20:24:54.299966
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:24:55.820235
# Unit test for function register
def test_register():
    """Test register"""
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:24:59.057757
# Unit test for function register
def test_register():
    """Test for register()"""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            'The codec "b64" should not be registered before the '
            'test is run.'
        )
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:25:10.994544
# Unit test for function register
def test_register():
    """Unit tests for function register."""
    # Ensure the 'NAME' codec is not registered.
    try:
        # Try to get the codec info.
        codecs.getdecoder(NAME)
        # If this code is reached, that means the codec is already
        # registered and we need to unregister it.
        codecs.unregister(NAME)
    except LookupError:
        # If we get an error, that means that it was not registered and
        # nothing needs to be done.
        pass

    # Make sure it is not registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register.
    register()

    # Get the codec info
    codec = codecs.getdecoder(NAME)

    # Unregister the codec.

# Generated at 2022-06-13 20:25:13.646551
# Unit test for function register
def test_register():
    """Test the register function.

    This test makes sure that the codec registers itself with Python.
    """
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:16.811347
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None   # type: ignore
    assert codecs.getencoder(NAME) is not None   # type: ignore


# Generated at 2022-06-13 20:25:18.622532
# Unit test for function register
def test_register():
    register()

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:29.859256
# Unit test for function encode

# Generated at 2022-06-13 20:25:46.310129
# Unit test for function register
def test_register():
    """Test the function register."""
    codecs.register = Mock()
    register()
    assert codecs.register.call_count == 1
    assert codecs.register.call_args == call(_get_codec_info)
    codecs.register.reset_mock()


if __name__ == '__main__':
    import sys
    import unittest

    class Tester(unittest.TestCase):
        """Unit test class."""

        def test_encode(self) -> None:
            """Test the encode function."""
            self.assertEqual(
                encode('aGVsbG8=\n'),
                (b'hello', 8)
            )

# Generated at 2022-06-13 20:25:57.516061
# Unit test for function register
def test_register():
    """Test the ``register`` function.

    """
    # Get the list of registered codecs and save the list.
    registered = sorted(codecs.registered_codecs())

    # Remove the b64 encoder if it exists.
    try:
        codecs.lookup(NAME)
        codecs.unregister(NAME)
    except LookupError:
        pass

    # Verify that the b64 codec is not registered.
    try:
        codecs.lookup(NAME)
    except LookupError:
        pass
    else:
        # The b64 codec is registered.  Fail the test.
        assert False, 'The b64 codec is registered and should not be'

    # Register the codec.
    codecs.register(_get_codec_info)   # type: ignore

    # Verify that the b64 codec is

# Generated at 2022-06-13 20:26:01.887150
# Unit test for function register
def test_register():
    """Unit test for function
    :data:`register<b64.codec.register>`."""
    codecs.lookup_error('b64')

    register()
    try:
        codecs.lookup_error('b64')
    except LookupError:
        pass
    else:
        raise AssertionError('b64 not registered')



# Generated at 2022-06-13 20:26:15.797042
# Unit test for function encode
def test_encode():
    """Test the function :func:`encode` against the more than 30
    test cases contained in the file ``test_cases.py``.
    """
    import test_cases
    from test_cases import (  # noqa
        GOOD_TESTS,
        BAD_TESTS,
    )

    # A call to "encode()" should produce the same results as the
    # equivalent call to "decodebytes()"
    for i in GOOD_TESTS:
        result = test_cases.decodebytes(i)
        actual = encode(i)
        assert result == actual

    # A call to "encode()" should fail as the equivalent call to
    # "decodebytes()"

# Generated at 2022-06-13 20:26:25.143079
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    # pylint: disable=W0603
    # Disable global variable warnings
    global _get_codec_info, NAME
    # Registering a codec with the same name will cause a
    # LookupError to be raised.  So, change the name to a
    # unique value. Then, restore to original value.
    orig_name = NAME
    NAME = 'another'
    try:
        register()
    except LookupError:
        # If no exception is raised, then the codec was already registered
        # with Python.
        pass

# Generated at 2022-06-13 20:26:29.369002
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:26:32.318589
# Unit test for function register
def test_register():   # pragma: no cover
    """
    Unit test for function register
    """
    # Make sure that we can call the ``register`` function without error
    register()



# Generated at 2022-06-13 20:26:41.610177
# Unit test for function encode
def test_encode():
    src = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb2"
    src += "4sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBh"
    src += "bmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYn"
    src += "kgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVk"

# Generated at 2022-06-13 20:26:46.650891
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)


if __name__ == '__main__':
    import unittest

    class TestCase(unittest.TestCase):
        """ Test case for ``register``."""

        def test_register(self):
            """ Test case for ``register``."""
            register()

    unittest.main()

# Generated at 2022-06-13 20:27:00.156670
# Unit test for function encode
def test_encode():
    '''
    Test the encode function
    '''
    assert encode('YmFzZTY0') == (b'base64', 6)
    assert encode('y') == (b'YQ==', 1)
    assert encode('yo') == (b'YW8=', 2)
    assert encode('yom') == (b'YW9t', 3)
    assert encode('yoma') == (b'YW9tYQ==', 4)
    try:
        encode('\n')
        assert False
    except UnicodeEncodeError:
        assert True
    try:
        encode('\t')
        assert False
    except UnicodeEncodeError:
        assert True
    assert encode('\tYmFzZTY0') == (b'base64', 6)

# Generated at 2022-06-13 20:27:10.015148
# Unit test for function register
def test_register():  # noqa: F811
    """Test function :func:`register`."""
    if not hasattr(codecs.lookup, '__test__'):
        return
    register()
    codecs.lookup(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:16.899232
# Unit test for function register
def test_register():
    """Test the register function."""
    from importlib import reload
    import codecs

    reload(codecs)
    register()

    assert codecs.getencoder(NAME) != None   # type: ignore
    assert codecs.getdecoder(NAME) != None   # type: ignore

    assert codecs.encode(b'hello', NAME) == (b'aGVsbG8=', 5)   # type: ignore
    assert codecs.decode(b'aGVsbG8=', NAME) == ('hello', 5)   # type: ignore


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:20.223853
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec is registered."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:25.132227
# Unit test for function register
def test_register():
    orig_getdecoder = codecs.getdecoder
    codecs.getdecoder = None
    try:
        register()
        codecs.getdecoder(NAME)
    finally:
        codecs.getdecoder = orig_getdecoder

# Unit-test for function decode

# Generated at 2022-06-13 20:27:28.566859
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert obj.decode is decode



# Generated at 2022-06-13 20:27:36.955323
# Unit test for function encode
def test_encode():
    """Test the encoding function."""
    # Test non-ASCII, Unicode string.  These characters will be encoded into
    # bytes with the utf8 codec.
    assert encode('\u2580')[0] == b'gA=='
    assert encode('\u2581')[0] == b'gQ=='

    # Test spaces, tabs, newlines
    assert encode('\n')[0] == b''
    assert encode('\t')[0] == b''
    assert encode(' ')[0] == b''

    # Test leading and trailing whitespace
    assert encode(' \n \t \t \n \n \n \t \t \t \n \n  A==')[0] == b'A=='
    assert encode('\t\t\t\t  A==')[0] == b

# Generated at 2022-06-13 20:27:39.217976
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    register()
    assert codecs.lookup(NAME)


# Generated at 2022-06-13 20:27:41.783162
# Unit test for function register
def test_register():
    """Test calling the register() function."""
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:43.770415
# Unit test for function register
def test_register():
    """Test the register function"""
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:27:47.062628
# Unit test for function register
def test_register():
    """Unit test for the function register()."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:01.065724
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError('The codecs.register function failed')

# Generated at 2022-06-13 20:28:07.537470
# Unit test for function register
def test_register():
    """Test registering the codec."""
    from unittest.mock import patch

    # This should work if the codec is already register.
    register()

    # but if we unregister the codec, we should be able to register it.
    with patch('codecs.__all__', new=[]):
        unregister()
        register()

# Generated at 2022-06-13 20:28:16.476978
# Unit test for function encode
def test_encode():
    # TypeError: encode() takes from 1 to 2 positional arguments but 3 were
    # given.
    with pytest.raises(TypeError) as e:
        encode(str, str, str)
    assert e.value.args == (
        'encode() takes from 1 to 2 positional arguments but 3 were given',
    )

    # TypeError: encode() takes 1 positional argument but 3 were given.
    with pytest.raises(TypeError) as e:
        encode(str, str, str, str)
    assert e.value.args == (
        'encode() takes 1 positional argument but 3 were given',
    )

    # TypeError: encode() takes 1 positional argument but 2 were given.
    with pytest.raises(TypeError) as e:
        encode(str, str)

# Generated at 2022-06-13 20:28:21.713532
# Unit test for function register
def test_register():
    """Test function register."""
    import codecs
    old_decoder = None
    old_encoder = None
    try:
        old_decoder = codecs.lookup(NAME).decode
        old_encoder = codecs.lookup(NAME).encode
    except LookupError:
        pass

    register()
    new_decoder = codecs.getdecoder(NAME)
    new_encoder = codecs.getencoder(NAME)

    assert old_decoder != new_decoder
    assert old_encoder != new_encoder


# Generated at 2022-06-13 20:28:23.921996
# Unit test for function register
def test_register():
    """Should be able to call the function register."""
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:28:26.261073
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`"""
    # Register the 'b64' codec the first time.
    register()
    # Try to register the 'b64' codec the second time.
    register()

# Generated at 2022-06-13 20:28:27.999614
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:28:29.196924
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:28:35.144080
# Unit test for function register
def test_register():
    register()
    encoder = codecs.getencoder(NAME)
    decoder = codecs.getdecoder(NAME)
    assert encoder
    assert decoder
    assert encoder(b'abcdefg')[0] == 'YWJjZGVmZw=='
    assert decoder(encoder(b'abcdefg')[0])[0] == b'abcdefg'


# Generated at 2022-06-13 20:28:37.626548
# Unit test for function register
def test_register():
    # pylint: disable=C0111,W0612
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:10.363508
# Unit test for function register
def test_register():
    # pylint: disable=W0612, W0613
    def test_decode(
            data: _ByteString,
    ) -> Tuple[str, int]:
        """Decode the given ``data`` into a string."""
        # Encode the given 'data' as utf8.
        data_bytes = bytes(data)
        input_str = data_bytes.decode('utf-8')

        # Decode the utf8 string into base64 bytes.

# Generated at 2022-06-13 20:29:12.581498
# Unit test for function register
def test_register():
    """Test the register() function."""
    register()
    codecs.getdecoder(NAME)


# Unit test function helper function

# Generated at 2022-06-13 20:29:14.889261
# Unit test for function register
def test_register():
    import sys
    register()
    assert sys.getdefaultencoding() == 'utf-8'

# Generated at 2022-06-13 20:29:20.768039
# Unit test for function register
def test_register():
    assert getattr(codecs, 'getdecoder', None) is not None
    try:
        codecs.getdecoder('b64')
    except LookupError as e:
        if e.args[0] == 'unknown encoding: b64':
            register()
            assert codecs.getdecoder('b64') is not None
            return
        raise



# Generated at 2022-06-13 20:29:21.823144
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()

# Generated at 2022-06-13 20:29:25.185385
# Unit test for function encode
def test_encode():
    """Test encode"""

    expected = b'\x8f\xddz\x85\r\xd2\xcf\x8d\xa0\xca\x87\xb3\xa3\xa9\xaf'
    actual = encode('hctf{d3c0d3_m0r3_t1m3}')
    assert expected == actual[0]

# Generated at 2022-06-13 20:29:34.448461
# Unit test for function encode
def test_encode():
    # pylint: disable=W0631
    # noinspection PyShadowingNames
    def encode(text: _STR) -> bytes:
        return decode(text)[0]
    assert encode('') == b''
    assert encode(' ') == b''
    assert encode('         ') == b''
    assert encode('''
        \t  \n
    ''') == b''

# Generated at 2022-06-13 20:29:35.908514
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    # codecs.getdecoder(NAME) should not raise a LookupError
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:29:48.463445
# Unit test for function encode

# Generated at 2022-06-13 20:30:03.076015
# Unit test for function encode
def test_encode():
    """
    Test the encode function.
    """
    # Test that given a base64 character string, that the encode function
    # will convert it into the given bytes.
    base64string = '''
        AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRobHB0eHyAhIiMkJSYnKCkqKywtLi8=
    '''
    bs = base64.b64decode(base64string)
    stdout, _ = encode(base64string)
    assert stdout == bs

    # Test that the encode function can handle multi-line base64 str.

# Generated at 2022-06-13 20:31:02.226103
# Unit test for function register
def test_register():  # pylint: disable=R0915
    """Test that the b64u codec registration works as expected."""
    #
    # Make sure that the registration of the 'b64' codec succeeds.
    #

    # Register the 'b64' codec.
    register()

    # Install a hook to catch the registering of the b64 codec a second time.
    hook_func = None
    hook_arg = None

    def hook_function(name: str, *args: Any) -> None:
        """Catch the exception when the 'b64' codec is registered a second
        time.
        """
        nonlocal hook_func
        nonlocal hook_arg

        hook_func = hook_function
        hook_arg = (name, *args)

    hook_func = hook_function

# Generated at 2022-06-13 20:31:12.004373
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    # Call the codecs.getdecoder function to test for the existence
    # of the NAME, which should not exist.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, f'{NAME} codec should not exist.'

    # Call the register function to register the NAME codec.
    register()

    # Call the codecs.getdecoder function to test for the existence
    # of the NAME, which should exist and be a CodecInfo object.
    ret = codecs.getdecoder(NAME)
    assert isinstance(ret, codecs.CodecInfo)



# Generated at 2022-06-13 20:31:18.630351
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    import codecs
    from b64 import register
    register()

    error: str = ''
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        error = (
            f'{NAME!r} not found as a codec even after '
            f'calling the function {register.__name__}.'
        )

    if len(error) > 0:
        raise SystemExit(error)


# Generated at 2022-06-13 20:31:22.991512
# Unit test for function register
def test_register():  # pragma: no cover
    register()

    text = """\
    A-AAAAB9/hgAAAAAAAEAAAAAAAAAAAAEAAAABAAAAAAAAAAEAAAAAAwAAAAAAAAAAAAAA
    AAAEAAAAAAAAAAQAAAAAAAAABAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    """
    # With our codec registered, the text should decode into its original
    # value.
    text_bytes = codecs.decode(text, NAME)
    assert text_bytes.decode() == 'Single Line Text'


# Unit tests for the Base64 Codec

# Generated at 2022-06-13 20:31:26.388812
# Unit test for function register
def test_register():
    """Test that this module can be registered with Python."""
    register()
    assert NAME in codecs._codec_search_path  # type: ignore



# Generated at 2022-06-13 20:31:30.963634
# Unit test for function encode
def test_encode():
    str_input = 'QmFzZTY0IC8gdXRmOCBjb252ZXJ0ZXI='
    output = 'Base64 / utf8 converter'
    output_bytes = 'Base64 / utf8 converter'.encode('utf8')
    assert encode(str_input)[0] == output_bytes



# Generated at 2022-06-13 20:31:33.712707
# Unit test for function register
def test_register():
    """Test the function register."""
    reg = register()
    assert reg is None



# Generated at 2022-06-13 20:31:35.494626
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME) # type: ignore
    codecs.getencoder(NAME) # type: ignore


# Generated at 2022-06-13 20:31:43.313146
# Unit test for function register
def test_register():
    """Unit test that verifies that the codec is properly registered."""
    codecs.register(_get_codec_info)  # type: ignore
    obj = codecs.getdecoder(NAME)  # type: ignore
    if obj is None:
        raise AssertionError("Codec not registered.")
    codecs.register(_get_codec_info)  # type: ignore


# pylint: disable=R0914