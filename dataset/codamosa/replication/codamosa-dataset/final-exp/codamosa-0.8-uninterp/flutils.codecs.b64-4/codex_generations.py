

# Generated at 2022-06-13 20:21:50.751896
# Unit test for function encode

# Generated at 2022-06-13 20:21:55.570231
# Unit test for function register
def test_register():
    try:
        # noinspection PyStatementEffect
        codecs.getdecoder(NAME)
    except LookupError:
        # The codec is not yet registered; so, register it.
        register()

        # Verify that the codec is registered.
        codecs.getdecoder(NAME)
    else:
        # The codec is already registered.  Nothing to do, but we need
        # to reset the cache so that the changes are applied.
        # noinspection PyStatementEffect
        codecs.lookup(NAME)


# Generated at 2022-06-13 20:21:58.741515
# Unit test for function register
def test_register():
    """Test the registration of the 'b64' codec"""
    # Make sure the codec is not registered
    with pytest.raises(LookupError):
        codecs.getdecoder('b64')

    # Register the 'b64' codec
    register()

    # Make sure the codec is registered by getting the codec.
    codecs.getdecoder('b64')



# Generated at 2022-06-13 20:22:01.287065
# Unit test for function encode
def test_encode():
    # Arrange
    input_str = "dGVzdA=="
    expected_str = b"test"

    # Act
    bytes_actual, _ = encode(input_str)

    # Assert
    assert bytes_actual == expected_str



# Generated at 2022-06-13 20:22:03.758860
# Unit test for function register
def test_register():
    """Unit test for function register"""
    codecs.register(_get_codec_info)   # type: ignore


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:13.387083
# Unit test for function encode
def test_encode():
    def test_corner_cases():
        # Corner cases
        assert encode('') == (b'', 0)  # Empty string
        assert encode(' ') == (b'', 0)  # Empty string
        assert encode('\r\n') == (b'', 0)  # Empty string
        encoded, n = encode('aGVsbG8gd29ybGQ=')
        assert encoded == b'hello world'
        assert n == len('aGVsbG8gd29ybGQ=')
        encoded, n = encode('  aGVsbG8gd29ybGQ=')
        assert encoded == b'hello world'
        assert n == len('aGVsbG8gd29ybGQ=')

# Generated at 2022-06-13 20:22:23.588895
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`."""
    try:
        codecs.getencoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            f'{NAME} should not be in the codecs registry when '
            f'this test begins'
        )
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            f'{NAME} should not be in the codecs registry when '
            f'this test begins'
        )
    code_obj = _get_codec_info(NAME)

# Generated at 2022-06-13 20:22:36.985049
# Unit test for function encode

# Generated at 2022-06-13 20:22:40.649400
# Unit test for function register
def test_register():
    """Test for the function 'register'."""
    import codecs

    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)   # type: ignore



# Generated at 2022-06-13 20:22:44.543423
# Unit test for function register
def test_register():
    """Test the function register."""
    import sys  # type: ignore
    assert NAME not in sys.modules

    register()
    assert NAME in sys.modules


# Generated at 2022-06-13 20:22:53.987442
# Unit test for function register
def test_register():
    # Unregister the codec 'b64' to test that the function 'register'
    # can register the 'b64' codec correctly.
    #
    # NOTE: We cannot register the 'b64' codec with the function
    # 'register' unless it have been unregistered.
    codecs.unregister(NAME)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.lookup(NAME)
        codecs.lookup(NAME)
    else:
        raise AssertionError(
            ' register() should have raised an AssertionError.'
        )

# Generated at 2022-06-13 20:22:57.236683
# Unit test for function register
def test_register():
    """Unit Test for function register"""
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder
    encoder = codecs.getencoder(NAME)
    assert encoder



# Generated at 2022-06-13 20:23:02.054188
# Unit test for function encode
def test_encode():
    test_text = (
        'YWJj\tZGVm\nZ2hp\tamts\nbW5v\ncGFy\n'
        'cXV3\ndHJ1\ndXl6'
    )
    expected = b'abc\x00def\x00ghi\x00jkl\x00mno\x00pqr\x00stu\x00vwx\x00yz'
    actual, _ = encode(test_text)
    assert actual == expected



# Generated at 2022-06-13 20:23:06.971363
# Unit test for function register
def test_register():
    """Unit test for function register"""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore


# Generated at 2022-06-13 20:23:14.461840
# Unit test for function encode
def test_encode():
    """Unit test for function ``encode``."""
    result = encode('bWFyY2Vs')
    assert isinstance(result, tuple)
    assert result[0] == b'\xe2\x80\xac\xcc\x81\xcd\x82\xe2\x81\x88'
    assert result[1] == len('bWFyY2Vs')



# Generated at 2022-06-13 20:23:17.391785
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec is registered."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:24.854746
# Unit test for function register
def test_register():
    """Unit test function register."""
    register()
    assert codecs.getdecoder('Base64') is not None
    assert codecs.getencoder('Base64') is not None


if __name__ == '__main__':
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:23:27.058866
# Unit test for function register
def test_register():
    """Test the register function."""
    global register
    codecs.register = lambda x: None
    register()
    assert codecs.register == codecs.register



# Generated at 2022-06-13 20:23:39.233692
# Unit test for function register
def test_register():
    from difflib import unified_diff
    from io import StringIO
    from unittest.mock import patch
    import b64codec

    # This is a string with a preamble.
    str_input = (
        "SGVsbG8sIFdvcmxkIQo="
    )

    out = b64codec.b64decode(str_input)
    expected = (
        b'Hello, World!'
    )
    assert out == expected

    # Register the codec so that the module is not imported by codecs.
    # The patch hook is called when the module is imported.
    with patch(
            'b64codec.register',
            wraps=b64codec.register
    ) as _mock_register:
        _mock_register.assert_not_called()

        # This is

# Generated at 2022-06-13 20:23:41.295717
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:23:45.169807
# Unit test for function encode
def test_encode():
    test_encode_decode(
        encode,
        decode
    )



# Generated at 2022-06-13 20:23:47.611348
# Unit test for function register
def test_register():
    """Test the codec registration"""
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:23:58.710079
# Unit test for function encode
def test_encode():
    """Test the :func:`~encode` function."""
    assert encode('AA==') == (b'\0', 4)
    assert encode('AA') == (b'\0', 2)
    assert encode('AA== ', 'ignore') == (b'\0', 4)
    assert encode('AA1') == (b'\0', 2)
    assert encode('ABC====') == (b'\0', 2)
    assert encode('====ABC') == (b'\0', 0)
    assert encode('A==B') == (b'\0', 4)
    assert encode('A=B') == (b'\0', 3)
    assert encode('A=B', 'ignore') == (b'\0', 1)
    assert encode('a==b') == (b'\0', 4)

# Generated at 2022-06-13 20:24:05.545809
# Unit test for function register
def test_register():
    expected_name = NAME
    codecs.register(_codec_info)
    try:
        decoder = codecs.getdecoder(expected_name)
        (result, _) = decoder(b'\xde\xad\xbe\xef')
        actual_name = result
        assert expected_name == actual_name
    finally:
        del codecs.decode[expected_name]



# Generated at 2022-06-13 20:24:07.406984
# Unit test for function register
def test_register():
    register()

# pylint: disable=C0111
# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:24:14.804460
# Unit test for function register
def test_register():
    """Register the ``b64`` codec with Python."""
    # Assert the b64 codec is not registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # b64 codec is not registered.
        pass
    else:
        raise AssertionError(f'The b64 codec is registered')

    # Register the codec
    register()

    # Assert the b64 codec is registered.
    obj = codecs.getdecoder(NAME)
    if obj is None:
        raise AssertionError(f'The b64 codec is not registered')



# Generated at 2022-06-13 20:24:20.681343
# Unit test for function encode
def test_encode():
    # Type test
    # assert isinstance(encode(b'test'), bytes)
    assert encode('bGVhc3VyZS4=')[0] == b'leasure.'
    # assert isinstance(encode('bGVhc3VyZS4='), bytes)
    # assert isinstance(encode('bGVhc3VyZS4=', ''), bytes)
    # assert isinstance(encode('bGVhc3VyZS4=', 'strict'), bytes)

    # Test expected behavior
    assert encode(b'leasure.')[0] == b'bGVhc3VyZS4='
    assert encode('leasure.')[0] == b'bGVhc3VyZS4='

# Generated at 2022-06-13 20:24:25.141337
# Unit test for function register
def test_register():
    """Test registering the ``b64`` codec."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:29.038430
# Unit test for function register
def test_register():
    """Unit test for function register."""
    import sys

    if sys.modules['b64'].register != register:
        raise AssertionError(
            f'Expected sys.modules["b64"].register to be {register!r}.\n'
            f'Found {sys.modules["b64"].register!r}.'
        )



# Generated at 2022-06-13 20:24:32.935601
# Unit test for function register
def test_register():
    """Ensure that the ``register()`` function works as expected."""
    register()

    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None
    assert codecs.lookup(NAME) is not None



# Generated at 2022-06-13 20:24:39.455193
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # Register the 'b64' codec with Python.
    register()

    # Ensure that we can get the codec.
    codecs.getdecoder('b64')



# Generated at 2022-06-13 20:24:41.671097
# Unit test for function register
def test_register():
    """Test function, to ensure interface contract is honored."""
    register()

# Generated at 2022-06-13 20:24:43.269013
# Unit test for function register
def test_register():
    """Ensure b64.register works."""
    register()



# Generated at 2022-06-13 20:24:52.627250
# Unit test for function encode
def test_encode():
    """Unit tests for the ``encode`` function."""
    assert encode('') == (b'', 0)
    assert encode('') == (b'', 0)
    assert encode(
        'SGVsbG8sIHdvcmxkIQ=='
    ) == (
        b'Hello, world!',
        22
    )

# Generated at 2022-06-13 20:24:57.760830
# Unit test for function register
def test_register():
    """Unit test for function register"""
    c_info = _get_codec_info(NAME)
    codecs.register(_get_codec_info)  # type: ignore
    codec_info = codecs.getdecoder(NAME)
    assert codec_info.tuple == c_info.tuple  # type: ignore


if __name__ == '__main__':
    import pytest
    pytest.main(
        [__file__]
    )

# Generated at 2022-06-13 20:25:09.716315
# Unit test for function register
def test_register():
    """Test the 'register' function."""
    from io import StringIO
    from sys import stderr
    from unittest import TestCase
    from unittest.mock import patch

    from codecs import register as codec_register

    class TestRegister(TestCase):
        """Test the 'register' function."""

        def test_register(self):
            """Test the 'register' function."""
            with patch.object(StringIO, '__init__') as mock_stringio:
                mock_stringio.return_value = None
                with patch.object(codecs, 'register') as mock_codec_register:
                    mock_codec_register.return_value = None
                    register()
                    codec_register.assert_called_once_with(_get_codec_info)

# Generated at 2022-06-13 20:25:10.867800
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:25:21.450737
# Unit test for function encode
def test_encode():
    """Tests for the ``encode`` function."""
    # Given text that has been properly base64 encoded
    # When the text is given to the 'encode' function.
    # Then the proper base bytes are returned.
    from base64 import b64encode
    assert b64encode(encode('AB')[0]) == b'AB=='

    # Given text that has been improperly base64 encoded.
    # When the text is given to the 'encode' function.
    # Then the 'UnicodeEncodeError' is raise.
    try:
        encode('AB=')
        assert False
    except UnicodeEncodeError:
        pass



# Generated at 2022-06-13 20:25:27.275270
# Unit test for function register
def test_register():
    prefix = __name__ + '.test_register(): '
    expected = 'utf-8'

    register()
    actual = codecs.decode(b'YQ==', 'b64')
    if actual != expected:
        raise AssertionError(f'{prefix}failed')

    codecs.encode(expected, 'b64')
    if actual != expected:
        raise AssertionError(f'{prefix}failed')

# Generated at 2022-06-13 20:25:29.909303
# Unit test for function register
def test_register():
    """Test registering the ``b64`` codec."""
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:44.063166
# Unit test for function register
def test_register():
    """Verify the b64 codec is registered."""
    from base64 import b64encode

    codecs.register(_get_codec_info)
    # Send the same data that was read back into the function to convert it to
    # base64.
    expected = '1234'.encode('ascii')
    expected_b64 = b64encode(expected)
    encode(expected_b64)

# Generated at 2022-06-13 20:25:48.343695
# Unit test for function register
def test_register():
    """Unit test for the ``register`` function."""
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)
    assert codecs.getincrementalencoder(NAME)
    assert codecs.getincrementaldecoder(NAME)


# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:25:57.146238
# Unit test for function register
def test_register():
    """Test for the ``register()`` function"""
    codecs_info_before = codecs.list_encodings()

    register()
    codecs_info_after = codecs.list_encodings()

    added_codec_names = sorted(
        set(codecs_info_after) - set(codecs_info_before)
    )

    assert len(added_codec_names) == 1
    assert added_codec_names[0] == NAME

    codec = codecs.lookup(added_codec_names[0])
    assert codec.name == NAME


# Generated at 2022-06-13 20:26:07.569998
# Unit test for function register
def test_register():
    """Test to ensure that the codec exists."""
    import pytest
    from codecs import getdecoder
    register()
    assert getdecoder(NAME)


if __name__ == '__main__':
    import os
    import sys
    import unittest
    from io import StringIO

    register()

# Generated at 2022-06-13 20:26:11.286807
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None


# Test function encode

# Generated at 2022-06-13 20:26:12.637561
# Unit test for function register
def test_register():
    """Test the register function"""
    register()

# Generated at 2022-06-13 20:26:14.488701
# Unit test for function register
def test_register():
    # This function is tested by test_codec.py.
    pass



# Generated at 2022-06-13 20:26:17.034912
# Unit test for function encode
def test_encode():
    assert decode(b'AQIDBAUGBwgJCg==') == b'\x01\x02\x03\x04\x05\x06\x07\x08'

# Generated at 2022-06-13 20:26:26.389671
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    codecs.register(_get_codec_info)
    try:
        # Convert the bytes 'raw_bytes' into the base64 encoded Unicode
        # string 'utf_str'.
        raw_bytes = b'\xf2\xb2\xbd\xf0\x9f\xa4\x94'
        utf_str = codecs.decode(raw_bytes, NAME)
        # Convert the Unicode string 'utf_str' into the base64 decoded bytes
        # 'dec_bytes'.
        dec_bytes = codecs.encode(utf_str, NAME)
        assert raw_bytes == dec_bytes
    finally:
        codecs.register(codecs.getdecoder(NAME))

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:27.560654
# Unit test for function register
def test_register():
    # Make sure it registers.
    register()

# Generated at 2022-06-13 20:27:01.666393
# Unit test for function encode

# Generated at 2022-06-13 20:27:11.641080
# Unit test for function register
def test_register():
    import sys
    from rndx.typing import CodecInfoT

    # Remove the codec we are going to test from the mapping.
    sys.modules['b64'].remove_codec()

    register()

    codec_info: CodecInfoT = codecs.CodecInfo(  # type: ignore
        name='b64',
        decode=_get_codec_info('b64').decode,  # type: ignore[arg-type]
        encode=_get_codec_info('b64').encode,  # type: ignore[arg-type]
    )
    try:
        assert codec_info.decode == decode
        assert codec_info.encode == encode
    finally:
        remove_codec()



# Generated at 2022-06-13 20:27:20.172767
# Unit test for function register
def test_register():
    """Test function register in the b64 module."""
    # pylint: disable=C0103
    #  Register a codec to use for the tests
    import codecs
    codecs.register(_get_codec_info)   # type: ignore
    # Make sure that the codec is registered and that the codec name is
    # as expected
    from binascii_bytes.b64 import NAME
    codec = codecs.getdecoder(NAME)    # type: ignore
    assert codec is not None
    assert NAME == codec.__name__
    assert codec.decode is decode


# Generated at 2022-06-13 20:27:22.550550
# Unit test for function register
def test_register():
    """Unit test for function register."""
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:27:26.579714
# Unit test for function encode
def test_encode():
    assert encode("dGVzdA==") == (b'test', 6)
    assert encode("dGVzdGluZw==") == (b'testing', 10)
    assert encode("dGVzdGluZ3Rlc3Rpbmc=") == (b'testingtesting', 18)


# Generated at 2022-06-13 20:27:33.381050
# Unit test for function register
def test_register():
    """Unit test for function register()."""
    codecs.unregister_error('strict')
    try:
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)
    finally:
        codecs.register_error('strict')
    assert True


# Generated at 2022-06-13 20:27:36.267877
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:27:40.852917
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(
            f"{NAME!r} codec failed to register: {e}"
        ) from e



# Generated at 2022-06-13 20:27:53.802560
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('' + ' ') == (b'', 0)
    assert encode(' ') == (b'', 0)
    assert encode(' ' + ' ') == (b'', 0)
    assert encode(' ' + '\n') == (b'', 0)
    assert encode('\n') == (b'', 0)
    assert encode('\n' + '\n') == (b'', 0)
    assert encode('\n' + ' ') == (b'', 0)
    assert encode('\n' + '  ') == (b'', 0)
    assert encode('  ') == (b'', 0)
    assert encode('  ' + ' ') == (b'', 0)

# Generated at 2022-06-13 20:27:57.120655
# Unit test for function register
def test_register():
    # Register the b64 codec.
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:28:49.219446
# Unit test for function register
def test_register():
    assert codecs.lookup(NAME) is not None

# Generated at 2022-06-13 20:28:51.474289
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    coder = codecs.getdecoder(NAME)
    assert coder is not None



# Generated at 2022-06-13 20:29:01.076516
# Unit test for function encode
def test_encode():  # pylint: disable=too-many-branches
    """Unit test to demonstrate encoding functionality."""
    # Setup.

# Generated at 2022-06-13 20:29:06.750144
# Unit test for function register
def test_register():
    """Test the register function."""
    # Ensure the codec does not already exist with 'codecs'.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # Register the 'b64' module with python.
        register()

    codectools = codecs.lookup(NAME)
    b64_codec = codecs.getdecoder(NAME)

    assert codectools == b64_codec



# Generated at 2022-06-13 20:29:07.729646
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:14.411552
# Unit test for function register
def test_register():
    """Unit test for function register"""

    from . import lib_b64

    lib_b64.register()

    try:
        codecs.getencoder(NAME)      # type: ignore
        codecs.getdecoder(NAME)      # type: ignore
    except LookupError as e:
        from traceback import print_exc
        print_exc()
        raise e


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:29:16.558666
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:29:19.445870
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None
    assert codec[0](
        'QQ=='
    ) == (b'A', 4)

# Generated at 2022-06-13 20:29:23.734602
# Unit test for function register
def test_register():
    """The test runner for test_register()."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()
    print('Success: module b64.')

# Generated at 2022-06-13 20:29:25.614100
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:31:14.562831
# Unit test for function register
def test_register():
    """Verify the registration for the ``b64`` encoding."""
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:31:16.342546
# Unit test for function register
def test_register():
    """Test registering the codec in python."""
    register()
    codecs.getdecoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:31:22.041867
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    # Unit test the functions
    test_register()

    # Decode base64 data
    b64_str = (
        '''
        Zm9vCmJhcgo=
        '''
    )
    data, _ = encode(b64_str)
    print(data)

    # Encode bytes into a base64 string
    data = b'foo\nbar\n'
    b64_str, _ = decode(data)
    print(b64_str)
    print(b64_str.encode('ascii'))

# Generated at 2022-06-13 20:31:24.914634
# Unit test for function register
def test_register():
    register()
    # noinspection PyTypeChecker
    assert codecs.getdecoder(NAME) is not None   # type: ignore


# Generated at 2022-06-13 20:31:31.964059
# Unit test for function register
def test_register():
    """Unit test for the register function."""

    # pylint: disable=W0703
    try:
        registered = {
            codecs.getencoder(NAME),
            codecs.getdecoder(NAME)
        }
    except LookupError:
        registered = {None, None}
    register()
    if registered != {
            codecs.getencoder(NAME),
            codecs.getdecoder(NAME)
    }:
        raise AssertionError(
            f"The codecs failed to register for {NAME!r}")


register()

# Generated at 2022-06-13 20:31:33.601028
# Unit test for function register
def test_register():
    """Test function :func:`register`"""
    register()
    # Verify that the register() function worked
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:31:39.557521
# Unit test for function register
def test_register():
    """Test the function register()."""
    import sys
    import io
    import tempfile
    # Save the original state of sys.stdout.
    saved_stdout = sys.stdout
    # Create a fake file to capture the output from the codecs.register()
    # call.  Use a context manager to automatically close the file.
    with tempfile.TemporaryFile() as temp_file:
        # Set sys.stdout to the fake file.
        sys.stdout = io.TextIOWrapper(temp_file, 'utf-8', write_through=True)
        try:
            # Call the codecs.register() and capture the output.
            register()
        finally:
            # Restore the original stdout.
            sys.stdout = saved_stdout
        # Reset the file position back to the beginning.
       