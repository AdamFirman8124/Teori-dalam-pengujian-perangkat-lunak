

# Generated at 2022-06-13 20:21:42.577979
# Unit test for function register
def test_register():
    codecs.getencoder('b64')

register()

# Generated at 2022-06-13 20:21:46.947097
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert 'b64' in codecs.encode.__code__.co_varnames
    assert 'b64' in codecs.decode.__code__.co_varnames
    print('test_register: PASS')


# Generated at 2022-06-13 20:21:49.420301
# Unit test for function register
def test_register():
    """Test the function register()."""
    register()
    codecs.getdecoder(NAME)

# pylint: enable=W0613

# Generated at 2022-06-13 20:21:57.634593
# Unit test for function register
def test_register():
    """Test the function register, but only when the
    module is run directly."""
    import sys
    if __name__ == '__main__':
        # pylint: disable=C0103
        from base64 import b64encode
        from codecs import getdecoder, getencoder
        from unittest import TestCase
        from typing import Any, Iterable

        class TestRegister(TestCase):
            """Test the function register.
            """
            __slots__: Iterable[str] = ()

            def test_register(
                    self,
            ) -> None:
                """Test the function register.
                """
                global NAME  # pylint: disable=W0603
                codecs.register(  # type: ignore
                    lambda n: n == NAME and None or None
                )
                self.assertRaises

# Generated at 2022-06-13 20:22:07.944741
# Unit test for function register
def test_register():
    """Test :func:`register`
    """
    # pylint: disable=C0103
    # pylint: disable=W0613
    # pylint: disable=C0115

    import sys
    import unittest

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()

    #
    # Get the codec.
    #
    from codecs import getdecoder
    from codecs import getencoder

    decoder = getdecoder(NAME)
    encoder = getencoder(NAME)

    #
    # Make sure that the codecs work.
    #

# Generated at 2022-06-13 20:22:16.737021
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # Unregister if necessary
    try:
        codecs.lookup(NAME)
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)
    assert not hasattr(codecs, NAME)
    # Re-register
    register()
    assert hasattr(codecs, NAME)
    codecs.lookup(NAME)
    codecs.lookup_error(NAME)
    # Unregister again
    codecs.unregister(NAME)
    assert not hasattr(codecs, NAME)



# Generated at 2022-06-13 20:22:24.686911
# Unit test for function encode
def test_encode():
    """Unit test for the function encode"""
    try:
        import unittest
    except ImportError:
        return
    class EncodeTests(unittest.TestCase):
        """Tests for the encode function"""

        def test_encode_empty(self):
            """Test encode with empty string"""
            actual = encode('')
            expected = (b'', 0)
            self.assertSequenceEqual(actual, expected)

        def test_encode_whitespaces(self):
            """Test encode with only whitespaces"""
            actual = encode('        ')
            expected = (b'', 0)
            self.assertSequenceEqual(actual, expected)


        def test_encode_good_input_short(self):
            """Test encode with good input (short)"""

# Generated at 2022-06-13 20:22:36.285510
# Unit test for function register
def test_register():
    """Test the function :func:`register`"""
    # Initialize
    codecs.search_function.__self__.cache.clear()

    # Assert that the 'b64' codec have not been register
    try:
        codecs.getdecoder('b64')
    except LookupError:
        pass
    else:
        assert False, "'b64' codec should not have been registered."

    # Register the codec
    register()

    # Assert that the 'b64' codec have been register
    try:
        codecs.getdecoder('b64')
    except LookupError:
        assert False, "'b64' codec should have been registered."
    else:
        pass

# Generated at 2022-06-13 20:22:39.114690
# Unit test for function register
def test_register():
    # pylint: disable=C0103
    """Test function register."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:22:42.928254
# Unit test for function register
def test_register():
    """Test the register functions."""
    register()

    # The 'b64' codec should be able to be retrieved through the 'getencoder'
    # function.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:50.548650
# Unit test for function register
def test_register():
    """Register the ``b64`` codec with Python."""
    codecs.CONSTANTS.CODEC_ERROR_REGISTRY[NAME] = 'strict'
    register()
    assert codecs.getdecoder(NAME)      # noqa
    assert codecs.getencoder(NAME)      # noqa



# Generated at 2022-06-13 20:22:54.251989
# Unit test for function register
def test_register():
    global register
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            "b64 codec is not available after calling register()"
        )

# Generated at 2022-06-13 20:23:04.456477
# Unit test for function register
def test_register():  # nocover
    # Register the 'b64' codec.
    register()

    # Get the 'b64' codec.
    b64 = codecs.getdecoder(NAME)  # type: ignore
    assert b64 is not None

    # Check that the codec's name is 'b64'.
    assert b64.name == NAME

    # Check that the codec can encode a unicode string into b64 str.
    encoded_str, _ = b64.encode('B64')
    assert encoded_str == 'QjY0'

    # Check that the codec can decode b64 str into a unicode string.
    decoded_str, _ = b64.decode('QjY0')
    assert decoded_str == 'B64'

    # Register the 'b64' codec.
    register()

    # Get the '

# Generated at 2022-06-13 20:23:08.868636
# Unit test for function encode
def test_encode():
    b_data = b'lolol'
    str_data = 'lolol'
    data = str_data.encode('utf-8')
    with pytest.raises(UnicodeEncodeError):
        encode(b_data)
    with pytest.raises(UnicodeEncodeError):
        encode(data)
    assert encode(str_data)[0] == b_data



# Generated at 2022-06-13 20:23:10.550263
# Unit test for function register
def test_register():
    """Test the code register function."""
    register()



# Generated at 2022-06-13 20:23:15.096815
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)
    register()
    assert NAME == codecs.getdecoder(NAME).name  # type: ignore
    codecs.unregister(NAME)



# Generated at 2022-06-13 20:23:22.993214
# Unit test for function register
def test_register():
    """Unit test for function register"""
    expected_exception = None
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        expected_exception = e
    assert expected_exception is not None
    register()
    codec = None
    try:
        codec = codecs.getdecoder(NAME)
    except LookupError:
        pass
    assert codec is not None


# Generated at 2022-06-13 20:23:24.834992
# Unit test for function register
def test_register():
    """Test the register function."""
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:23:33.218513
# Unit test for function encode
def test_encode():
    """Test ``encode`` with these test cases."""

    def _valid(
        text: _STR,
        expected: _ByteString,
    ):
        """Assert that the given ``text`` encodes to the expected value."""
        val, length = encode(text)
        assert val == expected
        assert length == len(text)

    # Test case: 'YmVjYXVzZSBpdCdzIGEgcHJvb2Y='
    _valid(
        '''YmVjYXVzZSBpdCdzIGEgcHJvb2Y=''',
        b"because it's a proof"
    )

    # Test case: 'b3IgdGhlIHRyYWlsIG9mIGEgd2F0ZXIgdGltZXIu'
   

# Generated at 2022-06-13 20:23:36.610395
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    codecs.getdecoder(NAME)

# Test for function decode

# Generated at 2022-06-13 20:23:40.677568
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()


# Generated at 2022-06-13 20:23:44.917648
# Unit test for function register
def test_register():
    """Unit test for function register"""
    from unittest.mock import patch
    from . import binascii
    with patch.object(binascii, 'register'):
        register()

# Generated at 2022-06-13 20:23:48.637506
# Unit test for function register
def test_register():
    """Ensure the ``b64`` codec is registered with Python."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()  # pragma: no cover


# Generated at 2022-06-13 20:23:50.295972
# Unit test for function register
def test_register():
    """Test the register function"""
    register()
    codecs.getdecoder(NAME)             # type: ignore



# Generated at 2022-06-13 20:23:55.858067
# Unit test for function encode
def test_encode():
    assert b'QQ==' == encode('0')
    assert b'MTI=' == encode('12')
    assert b'MTIz' == encode('123')
    assert b'MTIzNA==' == encode('1234')
    assert b'MTIzNDU=' == encode('12345')
    assert b'MTIzNDU2' == encode('123456')


# Generated at 2022-06-13 20:24:01.924930
# Unit test for function encode
def test_encode():
    assert encode('NDg3NDg3NDgzNDg3NDgzNDgzNDgzNDg3NDgwMDAwMDAwMDAwMDAwMTIzNDU2Nzg5MDIzNDU2Nzg5') == (b'48748748347487483474874834748708000000000000000012345678902345678', 112)


# Generated at 2022-06-13 20:24:12.336272
# Unit test for function register
def test_register():
    """Ensure the ``b64`` codec can be registered with Python."""
    # Ensure the 'b64' codec is not already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise ValueError('The b64 codec should not be registered.')
    # Ensure the 'b64' codec can be registered.
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise ValueError('The b64 codec should be registered.')
    finally:
        # The codecs.unregister function is a Python 3.8+ feature.
        unregister()   # type: ignore


# noinspection PySameParameterValue

# Generated at 2022-06-13 20:24:19.291171
# Unit test for function encode
def test_encode():
    """Example unit tests for the ``encode`` function."""
    # Case 1:
    # Input:
    #   text = '\n'.join([
    #       'SGVsbG8gd29ybGQ=',
    #       '',
    #       'QW5kIHRoYXQ=',
    #       '',
    #       'SXMgdGhhdCByaWdodA=='
    #   ])
    # Expect:
    #   b'Hello world\nAnd that\nIs that right'

# Generated at 2022-06-13 20:24:22.625373
# Unit test for function register
def test_register():
    """Unit test for register function."""
    import codecs
    from ._b64 import register
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:29.481023
# Unit test for function register
def test_register():
    """Unit tests for registering the ``b64`` Codec."""
    import b64codec
    old_registry = b64codec.NAME.lower() in (x.lower() for x in codecs.BASE_ENCODING)  # noqa
    register()
    new_registry = b64codec.NAME.lower() in (x.lower() for x in codecs.BASE_ENCODING)  # noqa
    assert old_registry == False
    assert new_registry == True


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:24:36.288767
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    assert NAME == codec.name

test_register()

# Generated at 2022-06-13 20:24:41.452033
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass  # It is as expected because there is no 'b64' codec registered.
    else:
        raise AssertionError('There should not be a \'b64\' codec registered.')

    # Register the 'b64' codec
    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('There should be a \'b64\' codec registered.')



# Generated at 2022-06-13 20:24:45.472104
# Unit test for function register
def test_register():
    register()
    assert __name__ + '.decode' == codecs.getdecoder(NAME).__name__
    assert __name__ + '.encode' == codecs.getencoder(NAME).__name__



# Generated at 2022-06-13 20:24:53.642506
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('A') == (b'A', 1)
    assert encode('AA') == (b'AA', 2)
    assert encode('AAA') == (b'AAA', 3)
    assert encode('AAAA') == (b'AAAA', 4)
    assert encode('AAAAA') == (b'AAAAA', 5)
    assert encode('AAAAAA') == (b'AAAAAA', 6)
    assert encode('AAAAAAA') == (b'AAAAAAA', 7)
    assert encode('AAAAAAAA') == (b'AAAAAAAA', 8)
    assert encode('AAAAAAAAA') == (b'AAAAAAAAA', 9)
    assert encode('AAAAAAAAAA') == (b'AAAAAAAAAA', 10)
    assert encode('AAAAAAAAAAA') == (b'AAAAAAAAAAA', 11)

# Generated at 2022-06-13 20:24:55.920497
# Unit test for function encode
def test_encode():
    assert encode('wo') == (b'bw==', 2)
    assert encode('wow') == (b'b3c=', 3)
    assert encode('wow!') == (b'b3ch', 4)


# Generated at 2022-06-13 20:24:57.057130
# Unit test for function register
def test_register():
    """Test the register() function."""
    register()
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:24:57.494068
# Unit test for function register
def test_register():
    pass

# Generated at 2022-06-13 20:25:01.916691
# Unit test for function encode
def test_encode():
    assert (
        encode(
            'YQouZm9vLmJhcgo=',
        )[0]
        == b'a.foo.bar'
    )
    assert (
        encode(
            'YQouZm9\n'
            'vLmJhcgo=',
        )[0]
        == b'a.foo.bar'
    )
    assert (
        encode(
            'YQouZm9vLmJhcgo=',
        )[0]
        == b'a.foo.bar'
    )
    assert (
        encode(
            'YQou        Zm9vLmJhcgo=',
        )[0]
        == b'a.foo.bar'
    )

# Generated at 2022-06-13 20:25:12.612112
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('\x00') == (b'AAAA', 4)
    assert encode('A') == (b'QQ==', 2)
    assert encode('B') == (b'Qg==', 2)
    assert encode('AB') == (b'QUI=', 3)
    assert encode('Z') == (b'Wg==', 2)
    assert encode('0') == (b'MA==', 2)
    assert encode('9') == (b'OQ==', 2)
    assert encode('.') == (b'Lg==', 2)
    assert encode('/') == (b'Lw==', 2)
    assert encode('\xFF') == (b'//8=', 4)

# Generated at 2022-06-13 20:25:15.469392
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    register()
    obj = codecs.getdecoder(NAME)  # type: ignore
    assert obj is not None



# Generated at 2022-06-13 20:25:23.682209
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec is registered with Python."""
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:31.702296
# Unit test for function register
def test_register():
    from b64.codec.b64 import register as register_inner
    from importlib import reload
    import b64.codec.b64

    # Set up for the test.
    # The status of the codec is cached in the variable '_g_available'.
    # The cache variable is defined on the module.
    b64.codec.b64._g_available = False
    reload(b64.codec.b64)

    # Call the function to test.
    register_inner()

    # Verify the test.
    assert b64.codec.b64._g_available is True

# Generated at 2022-06-13 20:25:39.333626
# Unit test for function register
def test_register():
    """Test the the ``register()`` function."""
    from functools import partial
    from pytest import raises
    from . import util

    def test(register_func: callable) -> None:
        with util.GlobalRegister(register_func):
            assert codecs.lookup(NAME) is not None
            assert codecs.getdecoder(NAME) is not None
            assert codecs.getencoder(NAME) is not None
            with raises(UnicodeDecodeError):
                # noinspection PyUnresolvedReferences
                codecs.decode('\x00', NAME)
            with raises(UnicodeEncodeError):
                # noinspection PyUnresolvedReferences
                codecs.encode(0x00, NAME)

    assert codecs.lookup(NAME) is None
    assert codecs.getdec

# Generated at 2022-06-13 20:25:41.905611
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    assert NAME == codecs.getdecoder(NAME).name


# Generated at 2022-06-13 20:25:44.393603
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME)     # type: ignore


register()

# Generated at 2022-06-13 20:25:49.657076
# Unit test for function register
def test_register():
    """Test registration of ``b64`` codec"""
    register()
    assert NAME == codecs.lookup(NAME).name  # type: ignore
    # Cleanup
    codecs.lookup(NAME).name = NAME


# Unit tests for function encode

# Generated at 2022-06-13 20:25:51.732780
# Unit test for function register
def test_register():
    """Test :func:`register`"""
    register()


# Generated at 2022-06-13 20:25:55.340943
# Unit test for function encode
def test_encode():
    assert encode('aGVsbG8=') == (b'hello', 6)
    assert encode('VGhpcyBpcyBhIHN0cmluZw==') == (b'This is a string', 18)


# Generated at 2022-06-13 20:25:58.005813
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.lookup(NAME)
    except LookupError:
        register()
        codecs.lookup(NAME)  # noqa



# Generated at 2022-06-13 20:26:02.773159
# Unit test for function register
def test_register():
    """Unit test for function register()"""
    from . import test_b64_decode, test_b64_encode
    register()
    # Set the codecs to the registerd encoding.
    codecs.register(lambda name: codecs.lookup(NAME) if name == 'b64' else None)
    test_b64_decode.test_decode()
    test_b64_encode.test_encode()

# Generated at 2022-06-13 20:26:09.918893
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:16.654197
# Unit test for function register
def test_register():
    """Test function register."""
    register()
    obj = codecs.getdecoder(NAME)
    assert isinstance(obj, (tuple, list))
    assert len(obj) == 2
    decoder = obj[0]
    assert isinstance(decoder, codecs.CodecInfo)
    assert decoder.name == NAME
    assert decoder.decode == decode
    assert decoder.encode == encode

# Generated at 2022-06-13 20:26:25.105391
# Unit test for function register
def test_register():

    # pylint: disable=C0321,C0330,W0612
    codecs.Reset()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise RuntimeError(
            'If this test fails, then the "b64" codec might be '
            'registered by default with Python.'
        )

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError(
            'If this test fails, then the "b64" codec failed to register '
            'with Python.'
        )

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:29.824772
# Unit test for function register
def test_register():
    """
    Test the function register.

    Returns:
        None
    """
    register()
    codecs.getencoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:31.125540
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False
    assert True



# Generated at 2022-06-13 20:26:32.613121
# Unit test for function register
def test_register():    # type: ignore
    register()
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:26:34.585148
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:26:36.930415
# Unit test for function register
def test_register():
    """Ensure that ``regist()`` will register the ``b64`` codec."""
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:43.561079
# Unit test for function register
def test_register():
    old_codec_info = codecs.lookup(NAME)
    codecs.register(  # type: ignore
        lambda name: None if name == NAME else old_codec_info
    )
    try:
        register()
        codec_info = codecs.lookup(NAME)
        assert codec_info.name == NAME
        assert codec_info.encode == encode
        assert codec_info.decode == decode
    finally:
        codecs.register(old_codec_info)

# Generated at 2022-06-13 20:26:51.722270
# Unit test for function encode
def test_encode():
    """Test encode() with a number of different input strings."""
    assert encode('Ym94RG93bg==')[0] == b'boxDown'
    assert encode('') == (b'', 0)
    assert encode(' ') == (b'', 0)
    assert encode('VGVzdCBzYW1wbGUuLi4KCQk=') == (b'Test sample...\n\n', 0)
    assert encode('\nVGVzdCBzYW1wbGUuLi4KCQk=') == (b'Test sample...\n\n', 0)
    assert encode('\n\nVGVzdCBzYW1wbGUuLi4KCQk=') == (b'Test sample...\n\n', 0)



# Generated at 2022-06-13 20:27:05.011802
# Unit test for function register
def test_register():
    """Unit test for the function register."""
    # Remove the previous test codec.
    codecs.unregister(NAME)

    # Check that the codec has been removed.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Add the test codec.
    codecs.register(_get_codec_info)

    # Check that the codec has been successfully added.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:08.590407
# Unit test for function register
def test_register():
    """
    This is a unit test for function register
    """
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError(f'Failed to register codec b64.')


# Generated at 2022-06-13 20:27:17.082619
# Unit test for function register
def test_register():
    """Test the codec registration."""
    # Try to access the codec before it is registered.
    try:
        codecs.getdecoder(NAME)
        assert False, 'Codec should not exist before registration'
    except LookupError:
        pass
    # Register the codec:
    register()
    # Try to access the codec after it is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec should exist after registration'
    # Registering it again should be a no-op.
    register()
    # Try to access the codec after it is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec should exist after 2nd registration'

# Generated at 2022-06-13 20:27:20.275796
# Unit test for function register
def test_register():
    """Test the register function"""
    register()
    from b64 import NAME
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:27:24.466835
# Unit test for function register
def test_register():
    """
    Verify the ``b64`` encoder can be registered in the
    python codecs module.
    """
    # pylint: disable=W0212
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:28.566607
# Unit test for function register
def test_register():
    """Test the function :func:`register`
    """
    # Verify the function is registered.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:32.537315
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    # Check the given codec was registered.
    codecs.getdecoder(NAME)
    # Check the given codec is the same object as this module.
    assert codecs.getdecoder(NAME) == codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:37.770825
# Unit test for function register
def test_register():
    """Test registration of the ``b64`` codec."""
    codecs.lookup_error = 'ignore'
    register()
    codec = codecs.getdecoder(NAME)  # type: ignore
    assert isinstance(codec, codecs.CodecInfo)
    assert codec.name == NAME


# Generated at 2022-06-13 20:27:41.699336
# Unit test for function encode
def test_encode():
    """Test the encode function"""
    text = "aGVsbG8="
    errors = "strict"
    out, out_length = encode(text, errors)
    assert out == b'hello'
    assert out_length == 8


# Generated at 2022-06-13 20:27:52.041687
# Unit test for function register
def test_register():
    # pylint: disable=R0914
    #         Too many local variables (16/15)
    # pylint: disable=R0201
    #         Method could be a function
    """Unit test for the register function"""
    # Create the test strings
    my_str = (
        'Here is a string that needs to be converted to base64 characters.'
    )
    my_b64 = (
        'SGhlcmUgaXMgYSBzdHJpbmcgdGhhdCBuZWVkcyB0byBiZSBjb252ZXJ0ZWQgdG8gY'
        'mFzZTY0IGNoYXJhY3RlcnMu'
    )

    # Convert the string into base64 characters for the comparison.

# Generated at 2022-06-13 20:28:14.512208
# Unit test for function register
def test_register():
    """Test the register function."""
    # Test where the ``b64`` codec is not yet registerd.
    try:
        # Try to get the codec info
        codecs.lookup(NAME)
    except LookupError:
        # The ``b64`` codec is not yet registered.
        # Register the ``b64`` codec,
        register()

        # Get the codec info.
        codec_info = codecs.lookup(NAME)

        # Exercise the codec_info encode and decode functions
        # for the various input types.
        # Use a repeated string of the same character.
        # The repeated character is repeated,
        # so the repeated string must be a multiple of 4 bytes,
        # because 4 base64 bytes can only encode 3 ascii bytes.
        # The repeated character is a ascii character so that it
        # is

# Generated at 2022-06-13 20:28:17.282594
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('b64')
    assert codecs.lookup_error('b64').name == 'b64'



# Generated at 2022-06-13 20:28:18.418397
# Unit test for function register
def test_register():
    import codecs
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:28.123404
# Unit test for function register
def test_register():

    # This is the list of all the codecs.
    codecs_list = list(codecs._codecs_cn.keys())  # type: ignore

    # Add the 'b64' codec to the codecs list.  We need to move the
    # register function to the top of this module so PyCharm will
    # recognize that the codecs has been registered and allow us to
    # import b64 below.
    register()

    # Change to the 'b64' directory and import the 'decode' function.
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))
    from b64 import decode

    # Verify that the 'b64' codec was added to the codecs.
    # Make sure the 'b64' codec was added to the codecs list.
    assert NAME

# Generated at 2022-06-13 20:28:39.469089
# Unit test for function encode
def test_encode():
    assert encode('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t') == (
        b"I'm killing your brain like a poisonous mushroom",
        len('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    )
    assert encode('dXRmOCcpIGlzIGVub3VnaC4=') == (
        b"utf8' is enough.",
        len('dXRmOCcpIGlzIGVub3VnaC4=')
    )

# Generated at 2022-06-13 20:28:40.713905
# Unit test for function register
def test_register():
    register()
    c = codecs.getdecoder(NAME)
    assert c is not None

# Generated at 2022-06-13 20:28:44.137681
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    codecs.getencoder(NAME)   # type: ignore
# /Unit test for function register



# Generated at 2022-06-13 20:28:44.946738
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:28:48.079086
# Unit test for function encode
def test_encode():
    """
    The test_encode function.
    """
    assert encode('Zm9v') == (b'foo', 4)



# Generated at 2022-06-13 20:28:51.627989
# Unit test for function encode
def test_encode():
    encoded = encode('TWFqb3IgTmljaG9sZXMgb2YgQ2FydG9zaA==')
    assert encoded == (b'Major Nicholas of Cartouche', 39)



# Generated at 2022-06-13 20:29:17.717784
# Unit test for function register
def test_register():
    encode('test')
    decode('test'.encode('utf-8'))

register()

# Generated at 2022-06-13 20:29:21.079079
# Unit test for function register
def test_register():

    register()
    b64 = codecs.getdecoder(NAME)

    assert b64 is not None
    assert b64 == decode  # type: ignore[comparison-overlap]



# Generated at 2022-06-13 20:29:22.921047
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:29:24.837069
# Unit test for function register
def test_register():

    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail('b64 codec failed to register')


# Generated at 2022-06-13 20:29:29.049446
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # Get the codec.
    codecs.getdecoder(NAME)   # type: ignore
    codecs.getencoder(NAME)   # type: ignore

# Generated at 2022-06-13 20:29:32.731666
# Unit test for function register
def test_register():
    """Test function 'register'."""
    codecs.register(_get_codec_info)   # type: ignore
    # Remove the codec.  This is necessary to avoid a warning
    # when running this test multiple times.

# Generated at 2022-06-13 20:29:34.968504
# Unit test for function register
def test_register():
    """Unit tests for the function register.
    """
    import sys
    register()
    assert NAME in sys.modules
    assert NAME in sys.modules['encodings'].__all__

# Generated at 2022-06-13 20:29:47.975738
# Unit test for function encode
def test_encode():
    assert encode(b'Test') == (b'VGVzdA==', 4)
    assert encode(b' Test') == (b'IFRlc3Q=', 5)
    assert encode(b'  Test') == (b'ICBUZXN0', 7)
    assert encode('Test') == (b'VGVzdA==', 4)
    assert encode(' Test') == (b'IFRlc3Q=', 5)
    assert encode('  Test') == (b'ICBUZXN0', 7)
    assert encode('\nTest') == (b'VGVzdA==', 5)
    assert encode('\n Test') == (b'IFRlc3Q=', 6)
    assert encode('Line1\nLine2') == (b'LinexCTGluZTI=', 11)

# Generated at 2022-06-13 20:29:51.104337
# Unit test for function register
def test_register():
    """Unit test for function register()"""
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:30:00.010249
# Unit test for function register
def test_register():
    """Test the codec registration."""
    name = NAME
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(name)
    except LookupError as e:
        raise RuntimeError(
            f'Failed to load codec {name!r}.'
        ) from e
    finally:
        del codecs.codecs_map[name]
        del codecs.code_search_function_cache[name]

# Generated at 2022-06-13 20:30:58.489385
# Unit test for function register
def test_register():
    """Unit test for function register"""
    codecs.register = unittest.mock.MagicMock()
    codecs.getdecoder = unittest.mock.MagicMock()
    register()
    codecs.register.assert_called_once()



# Generated at 2022-06-13 20:31:10.724395
# Unit test for function register
def test_register():
    """Unit test for the function :func:`.b64.register`"""
    try:
        codecs.getdecoder(NAME)
        raise AssertionError(
            'The b64 codec is already registered with Python'
        )
    except LookupError:
        pass

    try:
        # Register the b64 codec.
        codecs.register(_get_codec_info)  # type: ignore
        raise AssertionError(
            'The b64 codec is already registered with Python'
        )
    except ValueError:
        pass

    # Register the b64 codec.
    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            'The b64 codec is not registered with Python'
        )



# Generated at 2022-06-13 20:31:15.310401
# Unit test for function register
def test_register():
    # This unit test can only be run in the command line.
    # Running it in an IDE will cause it to fail.
    import sys
    assert sys.argv[0].endswith('conftest.py'), 'can only run in command line'

# pylint: enable=W0613

# Generated at 2022-06-13 20:31:18.669540
# Unit test for function register
def test_register():
    """Test the :func:`~register` function."""
    import sys
    if sys.version_info >= (3, 8):
        return
    import codecs

    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:31:19.897379
# Unit test for function register
def test_register():
    """Unit test to ensure the codec is registered."""
    register()
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:31:31.683137
# Unit test for function encode
def test_encode():
    assert encode('ewogICJzdWIiOiAiVGVzdCIsCiAgIm5hbWUiOiAiSm9obiBEb2UiLAogICJhZG1pbiI6IHRydWUsCiAgImNsaWVudCI6IHRydWUsCiAgImV4cCI6IDE0MjUzNzg5MjEKfQ==')[0] == b'{"sub": "Test","name": "John Doe","admin": true,"client": true,"exp": 1425378921}'

# Generated at 2022-06-13 20:31:33.760828
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:31:35.792929
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:31:39.808602
# Unit test for function register
def test_register():
    """Test that the b64 codec can be registered."""
    codecs.register(_get_codec_info)   # type: ignore

