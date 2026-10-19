

# Generated at 2022-06-13 20:21:45.284456
# Unit test for function register
def test_register():
    """Test function register"""
    # The ``b64.NAME`` is already registered
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:21:50.124836
# Unit test for function register
def test_register():
    """Unit test for function register()."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'b64 codec not registered'
    else:
        pass



# Generated at 2022-06-13 20:21:58.047490
# Unit test for function encode
def test_encode():
    # Test encode normal string
    assert encode('b64') == (b'YjY0', 3)
    # Test encode with line break
    assert encode('b64\n') == (b'YjY0', 4)
    # Test encode with indentation
    assert encode(' b64 ') == (b'YjY0', 6)
    # Test encode with indentation and line break
    assert encode(' b64\n') == (b'YjY0', 7)
    # Test encode UserString
    assert encode(UserString('b64')) == (b'YjY0', 3)
    # Test encode UserString with line break
    assert encode(UserString('b64\n')) == (b'YjY0', 4)
    # Test encode UserString with indentation

# Generated at 2022-06-13 20:22:07.088721
# Unit test for function register
def test_register():
    """Test Register"""
    # Verify that the codec is not already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    rtn1 = codecs.getdecoder(NAME)
    assert rtn1 is not None
    assert rtn1.encode is not None
    assert rtn1.encode('') == ('', 0)
    assert rtn1.decode(b'') == ('', 0)
    assert rtn1.encode('') == ('', 0)
    assert rtn1.decode(b'') == ('', 0)

    # Verify that register doesn't fail when called more than once.
    register()



# Generated at 2022-06-13 20:22:18.402642
# Unit test for function encode
def test_encode():
    """Unit test for function encode.

    This test is meant to be run from the command line.
    """

# Generated at 2022-06-13 20:22:32.560870
# Unit test for function encode
def test_encode():
    # pylint: disable=W0108
    # pylint: disable=C0116
    # pylint: disable=W0105
    """Unit tests for b64.encode"""

# Generated at 2022-06-13 20:22:35.049351
# Unit test for function register
def test_register():
    """Ensure the register function works properly."""
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:39.132040
# Unit test for function register
def test_register():
    """Test the register function"""
    register()
    assert codecs.getencoder(NAME)[0](b'text') == (b'dGV4dA==', 4)
    assert codecs.getdecoder(NAME)(b'dGV4dA==') == ('text', 8)



# Generated at 2022-06-13 20:22:40.487206
# Unit test for function register
def test_register():
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:22:49.525861
# Unit test for function register
def test_register():
    """Unit test function."""
    from sys import modules
    from types import ModuleType

    if 'btb.utils.b64.codec' not in modules:
        register()
        assert NAME in modules, f"Codec not registered: {NAME!r}"
        codec_module = modules[NAME]
        assert isinstance(codec_module, ModuleType)
        assert hasattr(codec_module, 'decode')
        assert hasattr(codec_module, 'encode')



# Generated at 2022-06-13 20:23:02.774406
# Unit test for function register
def test_register():
    """Test the register function."""
    # Verify that the codec is not registered.
    try:
        # pylint: disable=W0612,W0613
        name, encoder, decoder = codecs.lookup(NAME)  # type: ignore

        # If we got here the codec was registered.  Unregister and test
        # the test function.
        codecs.unregister(codecs.lookup(NAME))
    except LookupError:
        pass

    # Verify that the 'b64' is not registered.
    codecs.lookup_error(NAME)

    # Register it.
    register()

    # Verify that the 'b64' was registered.

# Generated at 2022-06-13 20:23:03.685853
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:23:14.066115
# Unit test for function encode
def test_encode():
    """Unit tests for the encode() function"""
    from io import StringIO


# Generated at 2022-06-13 20:23:27.320557
# Unit test for function register
def test_register():
    import contextlib
    with contextlib.ExitStack() as stack:
        reg_bak = codecs.register
        stack.enter_context(
            contextlib.redirect_stderr(
                open(os.devnull, "w")
            )
        )
        stack.enter_context(
            contextlib.redirect_stdout(
                open(os.devnull, "w")
            )
        )
        codecs.register = unittest.mock.MagicMock()
        register()
        codecs.register.assert_called_once()
        codecs.register.reset_mock()

        register()
        codecs.register.assert_not_called()
    codecs.register = reg_bak


# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:23:38.950741
# Unit test for function encode
def test_encode():
    test_data_file_object =  open("test_data.txt", "r")
    test_data_file_object_contents = test_data_file_object.read()
    test_data_file_object_contents_result = test_data_file_object_contents.encode("b64")
    # test_data_file_object_contents_result_decoded = test_data_file_object_contents_result.decode("b64")
    test_data_file_object_contents_result_decoded,_ = decode(test_data_file_object_contents_result)
    return test_data_file_object_contents == test_data_file_object_contents_result_decoded


# Generated at 2022-06-13 20:23:51.061823
# Unit test for function encode
def test_encode():
    """Test the :func:`~.b64.encode` function."""

# Generated at 2022-06-13 20:23:54.277027
# Unit test for function register
def test_register():
    register()
    try:
        codecs.lookup(NAME)
    except LookupError as e:
        assert False, f'codecs.lookup({NAME}) returned {e} instead of "OK".'

# Generated at 2022-06-13 20:23:57.725194
# Unit test for function encode
def test_encode():
    assert encode('YQ==') == (b'a', 3)
    assert encode('YWI=') == (b'ab', 4)
    assert encode('YWJj') == (b'abc', 4)


# Generated at 2022-06-13 20:24:01.040741
# Unit test for function register
def test_register():  # pragma: no cover
    from . import _codec_test
    _codec_test.test_register(NAME)



# Generated at 2022-06-13 20:24:02.729066
# Unit test for function register
def test_register():  # pylint: disable=W0612
    codecs.register = lambda x: None
    register()


# Generated at 2022-06-13 20:24:04.850538
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder('b64')

# Generated at 2022-06-13 20:24:07.454559
# Unit test for function register
def test_register():
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:09.407897
# Unit test for function register
def test_register():
    from ..unittest import test_register

    test_register(register, NAME)

# Generated at 2022-06-13 20:24:14.387219
# Unit test for function encode
def test_encode():
    """Test the encode() function"""
    str1 = """
        The quick brown fox jumped over the lazy dog
    """
    str2 = """
        VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2c=
    """
    assert encode(str1)[0] == decode(str2)[0]



# Generated at 2022-06-13 20:24:15.477661
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME).name == NAME



# Generated at 2022-06-13 20:24:20.998866
# Unit test for function encode

# Generated at 2022-06-13 20:24:25.809956
# Unit test for function register
def test_register():
    PRE_REGISTER_COUNT = len(codecs.registered)

    register()

    POST_REGISTER_COUNT = len(codecs.registered)

    assert PRE_REGISTER_COUNT < POST_REGISTER_COUNT



# Generated at 2022-06-13 20:24:28.427821
# Unit test for function register
def test_register():
    # type: () -> None
    """Check that the ``b64`` codec was properly registered."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:24:36.668850
# Unit test for function register
def test_register():
    # Remove the b64 codec from the `codecs` if it is registered.
    try:
        codecs.lookup(f'{NAME}')
    except LookupError:
        pass
    else:
        codecs.lookup(f'{NAME}').name  # pylint: disable=pointless-statement

    # Register this codec with `codecs`.
    register()

    # Confirm that the `codecs` lookup works as expected.
    codecs.lookup(f'{NAME}').name  # pylint: disable=pointless-statement



# Generated at 2022-06-13 20:24:43.074295
# Unit test for function encode
def test_encode():
    # input the string
    text = 'SGVsbG8gd29ybGQ='
    result = encode(text)
    assert result == (b'Hello world', 15)

    # input string with spaces and newline
    text = 'SGVsbG8gd29y\nbGQ='
    result = encode(text)
    assert result == (b'Hello worl', 13)

    # input string with invalid characters
    text = 'SGVsbG8gd29ybG3='
    try:
        encode(text)
    except UnicodeEncodeError as e:
        assert e.reason == ('b64',
                            'SGVsbG8gd29ybG3=\u2028',
                            0,
                            0,
                            "'' is not a proper bas64 character string: Incorrect padding")


# Generated at 2022-06-13 20:24:45.917587
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME) # Just to confirm its registered



# Generated at 2022-06-13 20:24:53.868074
# Unit test for function register
def test_register():
    """Unit test for function register"""
    imp.reload(codecs)

# Generated at 2022-06-13 20:24:56.910700
# Unit test for function register
def test_register():
    """Register the ``b64`` codec with Python."""
    # Ensure the codec is not already registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # Register the codec
        register()

        # Ensure the codec is now registered
        codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:00.168600
# Unit test for function register
def test_register():
    """Test the function :func:`~viewpoint.utils.codec.b64.register`."""

    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

    try:
        register()
    except Exception as e:
        raise AssertionError(e)



# Generated at 2022-06-13 20:25:02.269234
# Unit test for function register
def test_register():
    """Test function register()."""
    import codecs
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:06.404114
# Unit test for function register
def test_register():
    assert NAME not in codecs.getencodings()
    register()
    assert NAME in codecs.getencodings()
    assert NAME in codecs.getdecoders()
    assert NAME in codecs.getencoders()


# Generated at 2022-06-13 20:25:11.763388
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('the codec should not yet be registered')
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('the codec should now be registered')
    else:
        pass



# Generated at 2022-06-13 20:25:14.065810
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    import codecs
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:25.728832
# Unit test for function encode
def test_encode():
    assert encode('Zm9v') == b'foo'
    assert encode('Zm9 v') == b'foo'
    assert encode('Zm9 v\n') == b'foo'
    assert encode('Zm9 v\r\n') == b'foo'
    assert encode('') == b''
    assert encode(' ') == b''
    assert encode(' \n\r\n   ') == b''
    assert encode('\n') == b''
    assert encode('\n\n') == b''
    assert encode(' \n\n   ') == b''
    assert encode('\n  ') == b''
    assert encode('\n \n ') == b''
    assert encode('abc') == b'YWJj'

# Generated at 2022-06-13 20:25:28.521758
# Unit test for function register
def test_register():
    """Test the register function."""
    codecs.register(_get_codec_info)   # type: ignore
    codecs.getdecoder(NAME)

register()

# Generated at 2022-06-13 20:25:38.304742
# Unit test for function register
def test_register():
    """Unit test for function register"""
    with mock.patch('codecs.register') as mock_register:
        register()

    mock_register.assert_called_once()


if __name__ == '__main__':
    import sys
    import unittest

    class TestDecode(unittest.TestCase):
        """Unit tests for the decode function."""

        # pylint: disable=too-many-public-methods

        def test_basic(self):
            """When basic input is given, bytes output is returned.

            When any of the lines contain whitespace, the return line endings
            are normalized.
            """

# Generated at 2022-06-13 20:25:43.313365
# Unit test for function register
def test_register():
    """Test the :func:`register` function"""
    codecs.register(_get_codec_info)  # type: ignore
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)
    del codecs.decode  # type: ignore


# Generated at 2022-06-13 20:25:49.055818
# Unit test for function register
def test_register():
    """Test registering this module."""
    # Module 'codecs' has no 'register' member
    # pylint: disable=E1101
    register()
    assert NAME in codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:53.481261
# Unit test for function register
def test_register():
    """
    Unit Test for the function register.
    """
    # Register the b64 module.
    register()
    # Make sure we can access the b64 codec.
    codecs.getdecoder(NAME)   # type: ignore

# Generated at 2022-06-13 20:25:58.946445
# Unit test for function register
def test_register():
    """Test the register() function."""
    # Assert the codec of NAME 'b64' is not registered.
    with pytest.raises(LookupError):
        _ = codecs.getdecoder(NAME)

    # Register the NAME 'b64' codec.
    register()

    # Assert name 'b64' codec is registered.
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:26:12.453020
# Unit test for function register
def test_register():

    # Remove the codec if it is currently registered.
    try:
        codecs.lookup(NAME)
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)

    register()

    codec = codecs.lookup(NAME)

    # Test the encode functionality.
    str_input = '''
        abcdefghijklmnopqrstuvwxyz
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        0123456789
        +/
    '''
    str_out, str_len = codec.encode(str_input)
    str_in = codec.decode(str_out)[0]

    assert str_input == str_in

    # Remove the codec.
    codecs

# Generated at 2022-06-13 20:26:16.514605
# Unit test for function register
def test_register():
    """Test function :func:`register`."""
    # Register the 'b64' codec
    register()

    # Ensure the 'b64' codec is registered
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:19.112395
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    out, len_ = encode('hello world')
    assert out == b'aGVsbG8gd29ybGQ=\n'
    assert len_ == 11



# Generated at 2022-06-13 20:26:26.862746
# Unit test for function encode
def test_encode():
    """Test the encode function."""
    print(test_encode.__doc__)
    assert encode('YQ==', None) == (b'a', 3)
    assert encode('YWI=', None) == (b'ab', 4)
    assert encode('YWJj', None) == (b'abc', 4)
    assert encode('YWJjZA==', None) == (b'abcd', 8)
    assert encode('YWJjZGU=', None) == (b'abcde', 8)
    assert encode('YWJjZGVm', None) == (b'abcdef', 8)



# Generated at 2022-06-13 20:26:38.135739
# Unit test for function encode
def test_encode():
    # Create some unicode strings to decode
    # pylint: disable=C0330
    test_strings = (
        # A normal string of base64 characters.
        'VGhpcyBpcyBhIHN0cmluZyE=',
        # A normal string of base64 characters with spaces.
        'VGhpcyBpcyBhIHN0cmluZyE=      ',
        # A normal string of base64 characters with spaces and newlines.
        'VGhpcyBpcyBhIHN0cmluZyE=\n  \n',
        """
        VGhpcyBpcyBhIHN0cmluZyE=
        """,
    )

    # Create the correct values to which we will compare our results.

# Generated at 2022-06-13 20:26:50.623033
# Unit test for function encode
def test_encode():
    assert encode("QQ==") == (b'A', 4)
    assert encode("QQ==") == (b'A', 4)
    assert encode("QQ==") == (b'A', 4)
    assert encode("QQ==\r\n") == (b'A', 6)
    assert encode("QQ== \r\n") == (b'A', 7)
    assert encode("QQ==\n") == (b'A', 5)
    assert encode("QQ=\n=\n") == (b'A', 7)
    assert encode("QQ==\n\n") == (b'A', 6)
    assert encode("QQ\n==\n\n") == (b'A', 8)

# Generated at 2022-06-13 20:27:01.006881
# Unit test for function encode
def test_encode():
    """Function that tests the encode function

    Returns:
        Boolean: True if tests pass.
    """
    out, _ = encode('huJ0YXN0DQo=')
    assert out == b'\x00\x01\x02\x03\x04'

    out, _ = encode('huJ0YXN0DQo=\x00')
    assert out == b'\x00\x01\x02\x03\x04\x00'

    out, _ = encode('')
    assert out == b''

    out, _ = encode('\n\n')
    assert out == b''


# Generated at 2022-06-13 20:27:03.479137
# Unit test for function register
def test_register():
    """Test the register function."""
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:05.540239
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:08.211176
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    register()
    # This test asserts that the ``register`` function succeeds.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:17.054496
# Unit test for function register
def test_register():
    # pylint: disable=W0603
    # noinspection PyUnresolvedReferences
    try:
        import b_base64_codec
        del b_base64_codec
    except ImportError:
        # The codec is not installed.
        return

    globals()['codecs'] = mock.MagicMock(spec=codecs)
    codecs.getdecoder.side_effect = LookupError
    codecs.register.assert_not_called()

    register()
    codecs.register.assert_called_once()
    codecs.getdecoder.assert_called_once()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Test register'
    )
    args = parser.parse_args()

    test

# Generated at 2022-06-13 20:27:19.263621
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:23.462879
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail(
            'Failed to register codec "{}"'.format(
                NAME
            )
        )



# Generated at 2022-06-13 20:27:29.230164
# Unit test for function register
def test_register():
    """Register the b64 codec with Python."""
    import codecs
    # First make sure that we can't get the decoder as it isn't registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise RuntimeError(
            "We shouldn't be able to get the decoder for the b64 codec "
            "as it hasn't been registered with the codecs module."
        )

    register()

    # Now we should be able to get the decoder for the 'b64' codec.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:33.953868
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    import sys
    from importlib import reload
    codecs.unregister(NAME)
    reload(sys.modules[__name__])
    register()
    assert NAME in dict(codecs.getencoders())
    assert NAME in dict(codecs.getdecoders())



# Generated at 2022-06-13 20:27:42.509504
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:27:53.906296
# Unit test for function register
def test_register():
    """Test function `codecs.register`."""
    # Make sure the codec is not registered in this location.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise Exception(
            f'{NAME!r} is already registered for this module')

    # Register the codec for this module.
    register()

    # Make sure the codec is now registered in this location, and then
    # cleanup the registration.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception(
            f'{NAME!r} is not registered for this module')
    else:
        codecs.unregister_error(NAME)   # type: ignore



# Generated at 2022-06-13 20:27:58.170419
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail("Failed to register function register.")



# Generated at 2022-06-13 20:28:02.693717
# Unit test for function encode
def test_encode():
    assert encode('Zm9v\nYmFy\n') == (b'foobar', 14)



# Generated at 2022-06-13 20:28:05.117472
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:15.228139
# Unit test for function encode
def test_encode():
    assert encode('QUJDRA==') == (b'ABC', 6)
    assert encode('QUJD\nRA==') == (b'ABC', 6)
    assert encode('QUJD\nRA==\n') == (b'ABC', 6)
    assert encode('QUJD\nRA==\n\n') == (b'ABC', 6)
    assert encode('QUJD\nRA==\n\n\n') == (b'ABC', 6)
    assert encode('\nQUJD\nRA==') == (b'ABC', 6)
    assert encode('\nQUJD\nRA==\n') == (b'ABC', 6)
    assert encode('\nQUJD\nRA==\n\n') == (b'ABC', 6)

# Generated at 2022-06-13 20:28:19.719920
# Unit test for function register
def test_register():
    """Test the register function."""
    register()

    # This should work
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise RuntimeError(f'Failed to register codec: {e}') from e

    # This should be ignored.
    register()

# Generated at 2022-06-13 20:28:24.326621
# Unit test for function register
def test_register():
    """Test the functionality of the ``register()`` function."""
    # Reset the codecs registry.
    codecs.codec_registry.clear()

    # Register the codec.
    register()

    # Get the codec.
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:28:27.951022
# Unit test for function register
def test_register():  # pragma: no cover
    """Unit test of the ``register()`` function."""
    try:
        # Register the codecs module.
        register()
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, (
            'Base64 codecs not registered.'
            '  Check that register() function is working.'
        )



# Generated at 2022-06-13 20:28:35.060104
# Unit test for function register
def test_register():
    """Test the register() function."""
    assert isinstance(codecs.getencoder(NAME), codecs.CodecInfo)
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)
    assert isinstance(codecs.getincrementalencoder(NAME), codecs.CodecInfo)
    assert isinstance(codecs.getincrementaldecoder(NAME), codecs.CodecInfo)



# Generated at 2022-06-13 20:28:53.742111
# Unit test for function register
def test_register():
    """Unit test for function register.

    Tests:
        register: When the ``b64`` codec has not been registered,
        then a LookupError exception is thrown.
    """
    try:
        codecs.getdecoder('b64')
    except LookupError:
        register()
        assert 'b64' in codecs.__dict__
        assert codecs.lookup('b64') is not None



# Generated at 2022-06-13 20:29:03.991852
# Unit test for function encode
def test_encode():
    """Test the function 'encode'."""
    # pylint: disable=C0330
    # pylint: disable=C0326
    tests = [
        (
            'U3dhZ2dlciByb2NrcyE=',
            'Swagger rocks!'
        ),
        (
            'U3dhZ2dlciByb2NrcyE=',
            '    Swagger  rocks   !'
        ),
        (
            'U3dhZ2dlciByb2NrcyE=',
            ' Swagger\n rocks  !'
        ),
        (
            'U3dhZ2dlciByb2NrcyE=',
            '  \nSwagger\n  \n  rocks  \n  !'
        ),
    ]

# Generated at 2022-06-13 20:29:07.362337
# Unit test for function register
def test_register():
    codec_info = codecs.lookup(NAME)
    assert codec_info.name == NAME
    assert codec_info.decode(b'YWJj', 'strict') == ('abc', 3)
    assert codec_info.encode('abc', 'strict') == (b'YWJj', 3)

# Generated at 2022-06-13 20:29:11.233264
# Unit test for function register
def test_register():
    """Unit test for the function register."""
    try:
        codecs.getdecoder(NAME)
        raise Exception(
            f'The codec {NAME!r} should not be registered'
        )
    except LookupError:
        register()
        try:
            codecs.getdecoder(NAME)
        except LookupError:
            raise Exception(
                f'The codec {NAME!r} should be registered'
            )

# Generated at 2022-06-13 20:29:19.279445
# Unit test for function register
def test_register():  # type: ignore
    """Register the ``b64`` codec with Python."""
    import lib
    import codecs

    lib.codec.b64.register()

    codecs.getdecoder(lib.codec.b64.NAME)
    codecs.getencoder(lib.codec.b64.NAME)


# pylint: disable=W0613
# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:29:21.900974
# Unit test for function register
def test_register():
    assert NAME not in codecs.getencodings()
    register()
    assert NAME in codecs.getencodings()



# Generated at 2022-06-13 20:29:29.854147
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`"""
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    # Test the 'b64' codec.
    import unittest

    class TestDecode(unittest.TestCase):
        """Unit Test for function :func:`decode`"""

        def test_decode(self):
            """Test for :func:`decode`"""
            self.assertEqual(decode(b'\x00\x11\x22\x33'), ('AQID', 4))
            self.assertEqual(decode(b''), ('', 0))
            self.assertEqual(decode(b'\x00\x22\x33\x11'), ('AgQJ', 4))
            self.assertE

# Generated at 2022-06-13 20:29:44.190988
# Unit test for function register
def test_register():
    # Mark that the register function is to be tested.
    global register_tested

    # Ensure the b64 codec is not registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            "Expected the b64 codec to not be registered before "
            "running test_register()"
        )

    # Register the codec.
    register()

    # Ensure the codec is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            "Expected the b64 codec to be registered after "
            "running test_register()"
        )
    else:
        # Mark the register function as instead.
        register_tested = True


# Generated at 2022-06-13 20:29:51.825983
# Unit test for function encode
def test_encode():
    tests = [
        (
            'string',
            b'string'
        ),
        (
            'YWJj',
            b'abc'
        ),
        (
            'WW91ciBpbWFnZSdzIHZpYnJhdGVkIGNvbnRhaW5zIGEgYmFkIHN0cmluZyBvZiBiYXNlNjQgc3ltYm9scy4uLg==',
            b"Your image's vibriated contains a bad string of base64 symbols..."
        ),
    ]
    for test in tests:
        encoded = test[0]
        decoded = test[1]
        assert encode(encoded)[0] == decoded



# Generated at 2022-06-13 20:29:59.279856
# Unit test for function encode
def test_encode():

    def test1():
        text = ("VGVzdHMgZm9yIGRlY29kZSBNYXJpYWJsZSB0ZXN0cyBmb3IgZGVjb2RlIG1hcm"
                "lhYmxlIHRlc3RzIGZvciBkZWNvZGUgbWFyaWFibGUgdGVzdHMgZm9yIGRlY29kZS"
                "BtYXJpYWJsZSB0ZXN0cyBmb3IgZGVjb2RlIG1hcmlhYmxlLg==")
        text_utf8 = text.encode('utf-8')
        text_bytes = base64.b16decode(text_utf8)
        out, cnt = encode(text)

# Generated at 2022-06-13 20:30:30.097275
# Unit test for function register
def test_register():
    """Test the register method"""
    from confluent_cos_backend.cos_backend_impl import register as register_impl
    register()
    register_impl()

# Generated at 2022-06-13 20:30:32.795806
# Unit test for function register
def test_register():
    """Test that 'b64' codec is registered."""
    register()
    assert 'b64' in codecs.decode.__code__.co_varnames

# Unit tests for function decode

# Generated at 2022-06-13 20:30:42.834149
# Unit test for function register
def test_register():  # pylint: disable=W0613

    # Test that codecs.register is called correctly.
    # pylint: disable=W0621
    def mock_register(
            codec_info: codecs.CodecInfo
    ) -> None:
        assert codec_info.name == NAME
        assert codec_info.decode == decode
        assert codec_info.encode == encode

    # pylint: disable=W0621
    def mock_getdecoder(name):
        raise LookupError

    mock_getencoder = mock_getdecoder

    # Monkey patch the codecs module to test 'register()'
    import unittest.mock as mock

# Generated at 2022-06-13 20:30:44.666455
# Unit test for function register
def test_register():
    """Unit test for register()"""
    from .test_b64 import b64_codec_info
    codecs.register(b64_codec_info)


register()

# Generated at 2022-06-13 20:30:49.186530
# Unit test for function register
def test_register():
    register()
    did_register = True
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        did_register = False
    assert did_register



# Generated at 2022-06-13 20:30:50.794946
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:30:54.473584
# Unit test for function register
def test_register():
    """Unit test the register function."""
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:31:00.936428
# Unit test for function register
def test_register():
    """Test the register() function."""
    import sys
    import unittest
    from base64 import b64decode, b64encode

    class TestRegister(unittest.TestCase):
        """Test the register function."""

        def test_register(self: 'TestRegister') -> None:
            """Test the register function."""
            # Register the 'b64' codec with Python
            register()

# Generated at 2022-06-13 20:31:11.963446
# Unit test for function register
def test_register():
    """Test function register()."""
    # NOTE: codecs.lookup(NAME) will return b64.decode
    #       codecs.getdecoder(NAME) will return b64.decode
    decode(b'\x00\x00\x00')

# Generated at 2022-06-13 20:31:20.689981
# Unit test for function encode
def test_encode():
    # Ensure the 'encode' function is registered.
    register()

    # input_text is the regular base64 string and can span across many
    # lines and be indented and have spaces.