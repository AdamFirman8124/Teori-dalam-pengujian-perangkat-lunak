

# Generated at 2022-06-13 20:21:44.445079
# Unit test for function register
def test_register():
    """Test the register() function."""
    register()
    codecs.getdecoder(NAME)  # pylint: disable=W0104



# Generated at 2022-06-13 20:21:55.369615
# Unit test for function encode
def test_encode():
    assert encode('AAECAwQFBgc=') == (b'\x00\x01\x02\x03\x04\x05\x06\x07', 12)
    assert encode('AAECAwQFBgc\n') == (b'\x00\x01\x02\x03\x04\x05\x06\x07', 12)
    assert encode('AAECAwQFBgc\n\n') == (b'\x00\x01\x02\x03\x04\x05\x06\x07', 12)
    assert encode('AAECAwQFBgc\n\ng==') == (b'\x00\x01\x02\x03\x04\x05\x06\x07', 12)

# Generated at 2022-06-13 20:21:56.691716
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:02.161542
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    base64_codec = codecs.getdecoder(NAME)
    assert base64_codec(b'Kg==', 'strict') == ('h', 3)
    assert base64_codec(b'Kg==', None) == ('h', 3)



# Generated at 2022-06-13 20:22:12.085616
# Unit test for function encode
def test_encode():
    """Test function encode()."""
    # pylint: disable=W0704
    # pylint: disable=W1619
    # pylint: disable=W0612
    import doctest
    import sys
    try:
        import logging
    except ImportError:
        logging = None
    try:
        import unittest
    except ImportError:
        unittest = None
        doctest = None
    try:
        import argparse
    except ImportError:
        argparse = None
    try:
        from pytype import load_pytd
    except ImportError:
        load_pytd = None
    try:
        from pytype import errors
    except ImportError:
        errors = None
    try:
        from pytype import typegraph
    except ImportError:
        typegraph = None

# Generated at 2022-06-13 20:22:19.343015
# Unit test for function encode
def test_encode():
    """ We will test what is described in the docstring
    """
    """
    Example 1

        Given:
            text = 'This is \n test'
            errors = 'strict'
        Expected:
            out = b'VGhpcyBpcyB0ZXN0'
            len_text = 11

    """
    text = "This is \n test"
    errors = "strict"
    excepted_out, excepted_len_text = b'VGhpcyBpcyB0ZXN0', 11
    assert encode(text, errors) == (excepted_out, excepted_len_text)



# Generated at 2022-06-13 20:22:26.477310
# Unit test for function register
def test_register():  # pragma: no cover
    """Unit testing for ``register`` function."""
    from codecs import Codec

    register()
    try:
        # verify that this 'Name' is a Codec.
        Codec[NAME]
    except KeyError:
        assert True  # pragma: no cover
    else:
        assert False  # pragma: no cover


# Generated at 2022-06-13 20:22:29.478330
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:40.037261
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    import unittest
    import sys

    class TestRegister(unittest.TestCase):
        """Unit test for function ``register``."""

        def test_register(self):
            """Test that register a codec with the same name as
            an existing codec raises a ValueError.
            """
            import argparse

            # Register the codec
            self.assertNotIn(NAME, codecs.getencodings())
            register()
            self.assertIn(NAME, codecs.getencodings())

            # Verify that the b64 codec exists in sys.modules.
            self.assertIn(NAME, sys.modules)

            # Unregister the codec
            # pylint: disable=protected-access
            del sys.modules[NAME]

# Generated at 2022-06-13 20:22:43.976852
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        name = NAME
        codecs.getdecoder(name)
    except LookupError:
        register()
        try:
            codecs.getdecoder(name)
        except LookupError:
            raise AssertionError(
                (
                    f'The codec {name} is expected to be registered but '
                    'is not registered.'
                )
            )



# Generated at 2022-06-13 20:22:52.731040
# Unit test for function register
def test_register():
    """Unit test for the function :func:`register()`."""
    register()
    b64_decoder = codecs.getdecoder(NAME)
    assert b64_decoder is not None

    b64_encoder = codecs.getencoder(NAME)
    assert b64_encoder is not None



# Generated at 2022-06-13 20:23:03.666458
# Unit test for function register
def test_register():
    import codecs
    from binascii import Error
    from unittest import TestCase
    from unittest.mock import patch
    from unittest.mock import MagicMock

    class TestRegisterClass(TestCase):
        """Test the :func:`register` function."""
        @patch.object(codecs, 'register')
        def test_already_registered(self, mock_register):
            """Verify the codec is not registered if it already exists.

            Args:
                mock_register: Mocked :obj:`~codecs.register` function.
            """
            mock_codecs = MagicMock()

            def getdecoder(name: str) -> Optional[codecs.CodecInfo]:
                if name == NAME:
                    return mock_codecs
                return None
           

# Generated at 2022-06-13 20:23:06.068743
# Unit test for function register
def test_register():   # type: () -> None
    """Unit test for :py:func:`register`."""
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:23:11.902347
# Unit test for function register
def test_register():
    """Test the function register()."""
    from unittest.mock import patch

    with patch(
            'codecs.register',
            side_effect=LookupError
    ) as mock_register:
        register()
        mock_register.assert_called_once()
    with patch(
            'codecs.register',
            side_effect=Exception
    ) as mock_register:
        register()
        mock_register.assert_not_called()


# Generated at 2022-06-13 20:23:19.824338
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # Run the register function.
    register()

    # Get the codec info from Python.
    codec_info = codecs.getdecoder(NAME)   # type: ignore
    assert codec_info is not None

    # Ensure that the codec_info.name matches the NAME of the codec
    # we are registering.
    assert codec_info.name == NAME

    # Decode a string of base64 characters.

# Generated at 2022-06-13 20:23:32.136467
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert NAME in codecs.encode('', NAME)

# Generated at 2022-06-13 20:23:44.696152
# Unit test for function encode
def test_encode():
    # pylint: disable=C0103
    # This is a unit test, so we need to use the name 'test_encode'

    # Make a test string to encode
    src = '''
        V2hlbiBJIHdhbnQgdG8gZW5jb2RlIGEgc3RyaW5nIG9mIHRoZSBiYXNlNjQgY2hhcmFj
        dGVycyB0aGF0IGhhcyBibGFjayBsaW5lIGludGVuZGF0aW9uLCB5ZXQgbm8gbW9yZSBy
        dWxlcy4K
    '''

    # Get the bytes of the encoded text.
    encoded = encode(src)[0]

    # Convert the bytes into a string to

# Generated at 2022-06-13 20:23:46.385342
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    pass


# Generated at 2022-06-13 20:23:57.478061
# Unit test for function encode
def test_encode():
    # Test case 1
    # Test the case where the string is empty.
    # input
    text = ''
    # output
    expect_result = b''
    expect_length = 0
    result = encode(text)
    assert result == (expect_result, expect_length)

    # Test case 2
    # Test the case where the string is multi lines.
    # input
    text = '''
        Zm9vYmFy
        Ym9vCg==
    '''
    # output
    expect_result = b'foobarbov\n'
    expect_length = len(text)
    result = encode(text)
    assert result == (expect_result, expect_length)

    # Test case 3
    # Test the case where the string is one line.
    # input

# Generated at 2022-06-13 20:24:04.737706
# Unit test for function register
def test_register():
    """Unit test for function register."""

    # Reset the codec registry to its default state
    codecs.lookup_error('test')

    # Register the 'b64' codec
    register()

    # Get the codecs.CodecInfo object for the 'b64' codec
    codec_info = codecs.getdecoder(NAME)

    # Verify that the 'b64' codec is registered
    assert codec_info is not None



# Generated at 2022-06-13 20:24:16.215733
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    # Ensure that the 'b64' codec is not already registered.
    codecs.lookup_error = 'test_register'
    try:
        codecs.getencoder(NAME)
    except LookupError as e:
        if str(e) != 'test_register':
            raise
    else:
        raise Exception(
            f'{NAME!r} is already registered'
        )

    # Register the 'b64' codec.
    register()

    # Ensure that the 'b64' codec is now successfully registered.
    try:
        codecs.getencoder(NAME)
    except LookupError:
        raise Exception(
            f'{NAME!r} failed to register'
        )

# Generated at 2022-06-13 20:24:27.817840
# Unit test for function encode
def test_encode():
    """Unit Test for function ``encode``"""
    assert (
        encode('QmFzZTY0IGNoYXJhY3RlciBleGFtcGxl', errors='strict') == (
            b'Base64 character example',
            27
        )
    )

# Generated at 2022-06-13 20:24:38.540908
# Unit test for function register
def test_register():
    """Register the ``b64`` codec with Python."""
    from codecs import lookup
    from typing import Callable
    from nbqa_codec.b64 import codec
    from nbqa_codec.b64 import codecs
    from nbqa_codec.b64 import codec_info
    from nbqa_codec.b64 import decode
    from nbqa_codec.b64 import encode

    # pylint: disable=unsubscriptable-object

    # Register the ``b64`` codec with Python.
    codec.register()

    # Verify the decoder function.
    b64_decoder: Callable = lookup(name=codec.NAME).decode
    assert b64_decoder(data=codecs.encode(text='Hello World'))\
        == ('Hello World', 11)

# Generated at 2022-06-13 20:24:41.303752
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None
    assert decoder == decode



# Generated at 2022-06-13 20:24:43.519567
# Unit test for function register
def test_register():  # pragma: no cover
    """Unit test for function :func:`~b64.register`"""
    register()

# Generated at 2022-06-13 20:24:47.341743
# Unit test for function register
def test_register():
    """Unit test for function register"""
    codecs.getregentry('b64')
    codecs.getencoder('b64')
    codecs.getdecoder('b64')


# Generated at 2022-06-13 20:24:49.596582
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('b64') is None
    assert codecs.lookup_error('b64_errors') is None



# Generated at 2022-06-13 20:24:58.572325
# Unit test for function register
def test_register():
    # Provide a dummy getencoder
    def getencoder(name):
        return None
    # Provide a dummy getdecoder
    def getdecoder(name):
        return None
    # Provide a dummy lookup
    def lookup(name):
        return None

    # Save the current codec functions
    old_getencoder = codecs.getencoder
    old_getdecoder = codecs.getdecoder
    old_lookup = codecs.lookup
    old_register = codecs.register

    # Setup the dummy functions
    codecs.getencoder = getencoder
    codecs.getdecoder = getdecoder
    codecs.lookup = lookup
    # Setup the dummy register function
    codecs.register = lambda x: None

    # Test that the register function does not raise an error
    register()

    # Restore

# Generated at 2022-06-13 20:25:04.819144
# Unit test for function register
def test_register():
    codecs.register(lambda *args: None)
    assert not hasattr(codecs, 'b64_decode')
    assert not hasattr(codecs, 'b64_encode')
    register()
    assert hasattr(codecs, 'b64_decode')
    assert hasattr(codecs, 'b64_encode')

# Generated at 2022-06-13 20:25:07.900484
# Unit test for function register
def test_register():
    """Unit test for function 'register'"""
    register()
    codecs.getcodec(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:16.761321
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec was registered with Python."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:27.848300
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import sys
    from io import TextIOWrapper

    # Remove the b64 codec from the Python codecs if present.
    try:
        del sys.modules['b64']
    except KeyError:
        pass

    # Remove the b64 codec from the Python codecs if present.
    try:
        codecs.unregister(NAME)
    except LookupError:
        pass

    # Try to import the b64 module.  This will fail if the b64 module
    # has not been previously imported because the module no longer
    # exists in sys.modules.

# Generated at 2022-06-13 20:25:31.449460
# Unit test for function register
def test_register():
    register()
    assert(codecs.getdecoder(NAME) is not None)
    assert(codecs.getencoder(NAME) is not None)
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:25:38.942065
# Unit test for function register
def test_register():
    """Test ``test_register``."""
    # In the following, the value of 'codecs.getdecoder(NAME)' is not
    # used; it is simply used to exercise the try/except block in the
    # 'register' function.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass

    # The function 'register' is called.
    register()

    # The 'register' function should have now registered the codec
    # 'b64'.  This can be verified by calling the 'codecs.getdecoder'
    # function with the 'NAME' of the codec.  If the codec is
    # registered, then 'getdecoder' should no longer generate an
    # exception.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:43.453955
# Unit test for function register
def test_register():
    """Test that the codec is registered."""
    register()
    try:
        codecs.lookup(NAME)
    except LookupError as e:
        raise RuntimeError(
            f'Failed to register the {NAME} codec'
        ) from e



# Generated at 2022-06-13 20:25:49.129602
# Unit test for function register
def test_register():
    """Unit test function ``register``.
    """
    # Register the codec.
    register()

    # Verify that the codec was registered.
    assert __name__ in codecs.getdecoder(NAME).__module__



# Generated at 2022-06-13 20:25:52.410310
# Unit test for function register
def test_register():
    """Test for function register."""
    register()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:25:56.845299
# Unit test for function encode
def test_encode():
    """Unit test for function encode."""
    # noinspection SpellCheckingInspection
    assert encode('SGVsbG8gV29ybGQh') == (b'Hello World!', 14)



# Generated at 2022-06-13 20:25:59.570657
# Unit test for function register
def test_register():
    """Test that the register function works as intended."""
    register()


# This block needs to be at the end of the file.
# At the top of the file is where this module's name is defined.
register()

# Generated at 2022-06-13 20:26:12.993107
# Unit test for function encode
def test_encode():
    """Test the ``encode()`` function."""
    result = encode('YmFzZTY0IGVuY29kZWQK')
    assert result == (b'base64 encoded\n', 15)

    result = encode('QmFzZTY0IGVuY29kZWQK')
    assert result == (b'Base64 encoded\n', 15)

    result = encode('IkJhc2U2NCBlbmNvZGVkCg==')
    assert result == (b'"Base64 encoded\n"\n', 19)

    result = encode('CiJCYXNlNjQgZW5jb2RlZAo=\n')
    assert result == (b'"Base64 encoded\n"\n', 19)


# Generated at 2022-06-13 20:26:20.465165
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('b64') is None

# Generated at 2022-06-13 20:26:23.987426
# Unit test for function register
def test_register():
    """Unit test for registering the ``b64`` codec with Python."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    _ = codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:30.475141
# Unit test for function register
def test_register():
    """Test register() function."""
    codecs.register(_get_codec_info)   # type: ignore


# pylint: disable=C0103
if __name__ == '__main__':
    register()

    test_input = '\n'.join(
        map(
            str,
            [
                'aGVsbG8gd29ybGQh',
                'aGVsbG8gd29ybGQh',
                '',
                'aGVsbG8gd29ybGQh',
            ]
        )
    )
    # noinspection PyUnresolvedReferences
    test_string = test_input.encode(NAME)
    test_bytes = test_string.encode('utf-8')

# Generated at 2022-06-13 20:26:33.818522
# Unit test for function register
def test_register():
    register()
    info = codecs.getdecoder(NAME)
    assert info.name == NAME
    assert decode('a') == ('YQ==', 1)
    assert encode('YQ==') == (b'a', 1)

# Generated at 2022-06-13 20:26:36.133656
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec is registered with Python."""
    register()
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:26:38.404271
# Unit test for function register
def test_register():
    code_info = codecs.lookup(NAME)
    assert code_info.name == NAME


test_register()



# Generated at 2022-06-13 20:26:39.247044
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:42.252469
# Unit test for function register
def test_register():
    import sys

    # noinspection PyProtectedMember
    assert NAME not in sys.modules[__name__].__dict__
    # noinspection PyProtectedMember
    assert NAME not in sys.modules[b64.__name__].__dict__

    register()

    # noinspection PyProtectedMember
    assert NAME in sys.modules[b64.__name__].__dict__



# Generated at 2022-06-13 20:26:44.240317
# Unit test for function register
def test_register():
    assert codecs.lookup_error('strict') == codecs.strict_errors



# Generated at 2022-06-13 20:26:52.204494
# Unit test for function register
def test_register():
    register()
    try:
        # noinspection PyPackageRequirements
        from hypothesis import given
        from hypothesis import strategies as st

        @given(st.text())
        def test_encode_decode(input_str: str) -> None:
            input_bytes = str(input_str).encode()
            output_bytes = codecs.encode(input_bytes, NAME)  # type: ignore[call-arg]
            encoded_str = output_bytes.decode('utf-8')
            assert encoded_str.strip() == input_str.strip()

            output_str = codecs.decode(input_str, NAME)  # type: ignore[call-arg]
            assert output_str == input_bytes

    except ImportError:
        pass

test_register()

# Generated at 2022-06-13 20:27:15.609557
# Unit test for function register
def test_register():
    """Test the functio to register the codec."""
    # Verify the codec is not currently registered.
    try:
        codecs.getdecoder('b64')
        assert False, 'b64 is alreay registered'
    except LookupError:
        pass

    # Register the codec.
    register()

    def _check(
            text: _STR,
            data: bytes,
            encoder: bytes,
            decoder: str
    ) -> None:
        """Check the given ``text`` and ``data`` parameters."""
        # Encode.
        encoded_bytes = encoder(text)
        assert encoded_bytes == data

        # Decode.
        decoded_text, decoded_bytes_length = decoder(data)
        assert decoded_bytes_length == len(data)
        assert decoded_

# Generated at 2022-06-13 20:27:27.286182
# Unit test for function encode
def test_encode():
    """Unit test for function encode."""
    # simple test
    output, _ = encode(
        'dGVzdGluZw=='.strip(),
    )
    assert output == b'testing'

    # standard test

# Generated at 2022-06-13 20:27:29.898191
# Unit test for function encode
def test_encode():
    assert encode('U3R1ZmY=') == (b'Stuff', 6)



# Generated at 2022-06-13 20:27:31.941413
# Unit test for function encode
def test_encode():
    assert encode('YWJjZGVm') == \
        (b'abcdef', 6)


# Generated at 2022-06-13 20:27:34.952263
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    register()
    assert codecs.getencoder(NAME) is encode
    assert codecs.getdecoder(NAME) is decode


if __name__ == '__main__':
    # Run the unit test
    test_register()

# Generated at 2022-06-13 20:27:42.437161
# Unit test for function register
def test_register():
    from unittest import TestCase

    class Test(TestCase):
        def test_register(self):
            self.assertNotIn(
                NAME,
                codecs.__dict__
            )
            register()
            self.assertIn(
                NAME,
                codecs.__dict__
            )

    test = Test('test_register')
    test.test_register()


# Generated at 2022-06-13 20:27:44.562298
# Unit test for function register
def test_register():
    """Test the function register()"""
    register()



# Generated at 2022-06-13 20:27:53.637431
# Unit test for function register
def test_register():
    def test_import(name):
        """Test for import of given 'name'"""
        try:
            import_module(name)
        except ImportError:
            msg = (
                f'ImportError: Could not import the \'{name}\' module.  '
                'This module is compiled into Python and should always be '
                'available.'
            )
            raise ImportError(msg)

    test_import('codecs')
    codecs.register(_get_codec_info)   # type: ignore


# Test encoding and decoding of the base64 characters

# Generated at 2022-06-13 20:28:06.294046
# Unit test for function encode
def test_encode():
    """Unit test for the encode function.

    Raises:
        AssertionError: If the function does not pass the test.
    """

# Generated at 2022-06-13 20:28:15.850018
# Unit test for function encode
def test_encode():
    # pylint: disable=W0612
    # noinspection PyUnusedLocal
    def _test(text: str, expected_result: bytes) -> None:
        """Test the `encode` function.

        Args:
            text (str): The string that is to be converted into the base64
                decoded bytes.
            expected_result (bytes): The expected base64 decoded bytes.
        """
        actual_result, consumed = encode(text)

        assert expected_result == actual_result
        assert consumed == len(text)

    _test(
        r'Y29kZWM=',
        b'codec'
    )

    _test(
        r"""
        Y29kZWM=
        """,
        b'codec'
    )


# Generated at 2022-06-13 20:28:32.218276
# Unit test for function encode
def test_encode():
    assert encode('Yg==') == (b'a', 6)


# Generated at 2022-06-13 20:28:33.859983
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)

# Generated at 2022-06-13 20:28:35.502812
# Unit test for function register
def test_register():  # pylint: disable=W0613
    """Unit test for function register."""
    register()

# Generated at 2022-06-13 20:28:39.509171
# Unit test for function encode
def test_encode():
    assert encode(
        '''
        JXIyMGNtRnVjR3hzUFE9PQ==
        ''',
        errors='ignore'
    ) == (b'2bdcFuYGwQQ=', 39)



# Generated at 2022-06-13 20:28:45.307499
# Unit test for function register
def test_register():
    try:
        # Try to get the b64 codec.
        codecs.getdecoder(NAME)
    except LookupError:
        # The b64 codec does not exist.
        pass
    else:
        # The b64 codec already exists, do not register it again.
        return

    # Register the b64 codec.
    register()

    # Try to get the b64 codec again.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:51.144894
# Unit test for function register
def test_register():
    """Unit test for register"""
    register()
    assert NAME in codecs.encode("test", NAME)
    assert "test" in codecs.decode("dGVzdA==", NAME)



if __name__ == '__main__':
    print("For example usage, run test_b64.py")

# Generated at 2022-06-13 20:28:53.702666
# Unit test for function register
def test_register():
    """Test function register"""
    from codecs import getdecoder
    from codecs import getencoder
    register()
    getdecoder(NAME)
    getencoder(NAME)


# Generated at 2022-06-13 20:29:00.302920
# Unit test for function register
def test_register():

    # First ensure codec is not already registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # codec is not registered
        pass
    else:
        raise AssertionError('Codec is already registered')

    # Then register it
    register()

    # And ensure codec is now registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('Codec is not registered')

# Unit tests for function decode()

# Generated at 2022-06-13 20:29:09.137022
# Unit test for function register
def test_register():
    codecs_ = codecs
    codecs.register = lambda x: None  # type: ignore
    register()
    codecs.register = codecs_



# Generated at 2022-06-13 20:29:21.004116
# Unit test for function register
def test_register():

    # pylint: disable=unused-variable
    # pylint: disable=unused-argument

    # Create a mocked function for 'codecs.register'.
    def mock_codecs_register(obj: codecs.CodecInfo) -> None:
        # Verify the 'obj' that was given to the mocked function is
        # the expected value.
        assert obj.encode(b'', 'strict') == ('', 0)

    # Build the mocked codecs 'register' function.
    mocked_codecs_register = Mock(side_effect=mock_codecs_register)

    # Build the mocked codec.
    mock_codecs = MagicMock(spec=codecs)
    mock_codecs.register = mocked_codecs_register

    # Build the mocked module.
    mock_

# Generated at 2022-06-13 20:30:03.661471
# Unit test for function register
def test_register():    #   pragma: no cover
    from os import devnull
    from sys import stdout
    from textwrap import dedent

    # Redirect stderr to /dev/null
    stdout_fd = stdout.fileno()
    devnull_fd = open(devnull, 'w')
    save_stderr = os.dup(stdout_fd)
    os.dup2(devnull_fd, stdout_fd)

    # Register the codec
    register()

    # Restore stderr
    os.dup2(save_stderr, stdout_fd)
    os.close(save_stderr)

    # The codec should be registered

# Generated at 2022-06-13 20:30:10.527517
# Unit test for function register
def test_register():
    """Verify that function register works properly by unregistering the
    ``b64`` codec, then registering it again."""
    # Unregister the 'b64' codec.
    try:
        codecs.lookup(NAME)
    except LookupError:
        pass
    else:
        codecs.lookup(NAME).name  # pylint: disable=pointless-statement

    # Register the 'b64' codec again.
    register()

# Generated at 2022-06-13 20:30:13.881768
# Unit test for function encode
def test_encode():
    assert encode('abcdefghijklmnopqrstuvwxyz') == (bytes(range(26)), 26)
    assert encode('') == (bytes(0), 0)


# Generated at 2022-06-13 20:30:23.133519
# Unit test for function register
def test_register():
    """Test ``register`` by updating the codec registry and then asserting
    the registry is updated."""
    # Initialize the codec registry.
    register()  # nosec

    # Pull the codec information for the codec.
    codec_info = codecs.getdecoder(NAME)

    # Make sure the codec information is valid.
    assert codec_info is not None

    # Test encode string to bytes
    my_text_string = 'b-a-64'
    my_bytes, _ = codec_info.encode(my_text_string)
    expected_bytes = my_text_string.encode('utf-8')
    assert my_bytes == expected_bytes

    # Test decode bytes to string
    my_bytes = my_text_string.encode('utf-8')
    expected_str = my_text_string
    dec

# Generated at 2022-06-13 20:30:31.762801
# Unit test for function register
def test_register():
    """
    Unit test the 'register' function.
    """
    register()
    # Make sure the 'NAME' codec is registered.
    assert codecs.lookup(NAME) == (
        encode,
        decode,
        codecs.StreamReader(None, errors='strict'),
        codecs.StreamWriter(None, errors='strict'),
    )


if __name__ == '__main__':
    # Execute the unit tests only if this module is run directly.
    import pytest

    pytest.main([__file__, '-v', '-s'])

# Generated at 2022-06-13 20:30:36.487599
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)
    if b'\x80' == bytes([128]):
        assert bytes('cA==', NAME).decode(NAME) == '\\x80'


# Unit tests for function decode

# Generated at 2022-06-13 20:30:40.523463
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    try:
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)
    except LookupError as e:
        assert False, f'register() failed to register: {e}'

# Unit tests for function encode

# Generated at 2022-06-13 20:30:44.236095
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.lookup(NAME) == codecs.CodecInfo(
        name=NAME,
        encode=encode,
        decode=decode,
    )

# Generated at 2022-06-13 20:30:49.455420
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import sys
    if NAME in sys.modules:
        del sys.modules[NAME]

    register()
    assert NAME in sys.modules
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:30:53.850195
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)

if __name__ == '__main__':
    import doctest
    doctest.testmod()