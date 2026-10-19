

# Generated at 2022-06-13 20:21:48.687342
# Unit test for function register
def test_register():
    codecs.register(encoding_error='ignore')
    register()
    assert NAME == codecs.lookup(NAME).name



# Generated at 2022-06-13 20:21:54.166202
# Unit test for function register
def test_register():
    # Remove the 'b64' codec from the codecs cache.
    codecs.cache.pop('b64', None)
    # Make sure that 'b64' codec is NOT in the codecs cache.
    assert 'b64' not in codecs.cache
    # Register the 'b64' codec with Python.
    register()
    # Make sure that the 'b64' codec IS in the codecs cache.
    assert 'b64' in codecs.cache

# Generated at 2022-06-13 20:21:56.344228
# Unit test for function register
def test_register():
    """Test that the b64 codec was successfully registered."""
    codecs.register(_get_codec_info)
    codecs.getdecoder(NAME)

# Run unit tests when run from the command line

# Generated at 2022-06-13 20:22:02.594047
# Unit test for function encode
def test_encode():
    assert encode('YWJjMTIzIT8kKiYoKSctPUB+') == (b'abc123!?$*&()\'-=@~', 28)
    assert encode('ZHVtbXkgY29kZQ==') == (b'dummy code', 14)
    assert encode('ZHVtbXkK') == (b'dummy\n', 8)
    return True


# Generated at 2022-06-13 20:22:04.270995
# Unit test for function register
def test_register():
    register()
    _ = codecs.getdecoder(NAME)
    # End unit test for function register



# Generated at 2022-06-13 20:22:07.322513
# Unit test for function encode
def test_encode():
    """Unit test for function encode."""
    a = encode('aGVsbG8gd29ybGQ=')
    assert a == (b'hello world', 14)



# Generated at 2022-06-13 20:22:11.228613
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    register()

    codec_info = codecs.getdecoder(NAME)
    assert codec_info.name == NAME
    assert codec_info.encode == encode
    assert codec_info.decode == decode



# Generated at 2022-06-13 20:22:15.173567
# Unit test for function register
def test_register():  # pragma: no cover
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    raise RuntimeError(
        'This Python module is not supported to run as a standalone program. '
        'Use the bin/pytest to execute unit test or use the  '
        'bin/pylint to check for code errors.'
    )

# Generated at 2022-06-13 20:22:16.972905
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:24.183124
# Unit test for function register
def test_register():  # pragma: no branch
    """Check that the register function works correctly."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:  # pragma: no cover
        raise Exception(f'{NAME!r} is already registered')
    register()
    codecs.getdecoder(NAME)

## Unit test for function encode

# Generated at 2022-06-13 20:22:32.818863
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert True
    else:
        assert False
        
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False
    else:
        assert True

# Generated at 2022-06-13 20:22:34.502479
# Unit test for function register
def test_register():
    """Test for the register function."""
    register()



# Generated at 2022-06-13 20:22:37.693213
# Unit test for function register
def test_register():
    """Test for function register."""
    # Add the codec to the codec table.
    register()

    # Check that the codec was added.
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:39.464764
# Unit test for function encode
def test_encode():
    assert encode('TWFu') == (b'Man', 4)



# Generated at 2022-06-13 20:22:40.259794
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:22:43.999391
# Unit test for function register
def test_register():
    """Test the 'register' function.

    This test only works if the codec has not been previously registered.
    """
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:22:55.289452
# Unit test for function register
def test_register():
    # Register the codec 'b64'.
    register()

    # Get the codecs 'b64' decoder.
    dec_func = codecs.getdecoder(NAME)

    # Make sure the codecs 'b64' decoder is the same as the codec b64 decoder
    # 'decode'.
    assert dec_func == decode
    assert dec_func.__name__ == NAME
    assert dec_func.__doc__ == decode.__doc__

    # Get the codecs 'b64' encoder.
    enc_func = codecs.getencoder(NAME)

    # Make sure the codecs 'b64' encoer is the same as the codec b64
    # encoder 'encode'.
    assert enc_func == encode
    assert enc_func.__name__ == NAME
    assert enc_func.__doc

# Generated at 2022-06-13 20:22:58.286261
# Unit test for function register
def test_register():
    register()
    result = codecs.getdecoder(NAME)
    assert result[0].__name__ == NAME

# Generated at 2022-06-13 20:23:06.237045
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    codecs.register(_get_codec_info)   # type: ignore
    codecs.getdecoder(NAME)


if __name__ == "__main__":
    test_register()

# Generated at 2022-06-13 20:23:16.245342
# Unit test for function register
def test_register():
    import sys

    # Clean out the b64 codec from the Python encodings and codec maps.
    # Remove the codec from the Python codec tables.
    for encoding in {'b64'}:
        try:
            del sys.modules[f'encodings.{encoding}']
        except KeyError:
            pass

        # Remove the codec from the Python codec tables.
        for table in (codecs.encode, codecs.decode):
            try:
                del table[encoding]
            except KeyError:
                pass

        # Remove the codec from the Python encoding/decoding registry.
        registry_key = codecs.codecs.lookup(encoding).name
        try:
            del codecs.__registry__[registry_key]
        except KeyError:
            pass

    # Register the codecs

# Generated at 2022-06-13 20:23:21.983603
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:23:24.783983
# Unit test for function register
def test_register():  # pylint: disable=W0613
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:32.396243
# Unit test for function register
def test_register():
    """Verify that the b64 codec is registered."""
    register()
    decoder = codecs.getdecoder(NAME)
    encoder = codecs.getencoder(NAME)
    orig_encoded = 'AAjbCAk='
    orig_decoded = b'\x02\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00'
    decoded, _ = decoder(orig_encoded)
    encoded, _ = encoder(orig_decoded)
    assert decoded == orig_encoded
    assert encoded == orig_encoded.encode('utf-8')



# Generated at 2022-06-13 20:23:38.937743
# Unit test for function register
def test_register():
    test_str = "The quick brown fox jumped over the lazy dog."
    codecs.getdecoder(NAME)
    b64_str = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu"
    assert b64_str == test_str.encode(NAME)



# Generated at 2022-06-13 20:23:46.826415
# Unit test for function register
def test_register():
    old_codecs = None
    try:
        old_codecs = codecs.lookup_error(NAME)
    except LookupError:
        pass
    register()
    codecs.lookup_error(NAME)
    register()
    if old_codecs is not None:
        codecs.register_error(NAME, old_codecs)
    else:
        codecs.register_error(NAME, None)

# Generated at 2022-06-13 20:23:53.741889
# Unit test for function encode
def test_encode():
    assert encode('Zm9v') == (b'foo',4)
    assert encode('YWJj') == (b'abc',4)
    assert encode('YWJjZA==') == (b'abcd',6)
    assert encode('YWJjZA') == (b'abcd',5)
    assert encode('YWJjZA=') == (b'abcd',5)
    assert encode('\nZm9v\n') == (b'foo',8)
    assert encode('\n\nZm9v\n\n') == (b'foo',10)
    assert encode('\nZm9v\t') == (b'foo',8)
    assert encode('\tZm9v\n') == (b'foo',8)

# Generated at 2022-06-13 20:23:57.286383
# Unit test for function register
def test_register():
    """Test :meth:`b64.register` function."""
    register()
    codecs.getencoder(NAME)

# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :

# Generated at 2022-06-13 20:24:05.699169
# Unit test for function register
def test_register():
    """Test the register() function.

    Args:
        None.

    Returns:
        None.
    """
    # Save the current state of the register codecs.
    # pylint: disable=W0603
    global _OLD_CODECS_MAP
    _OLD_CODECS_MAP = copy(codecs.__dict__.get('_cache').copy())

    register()
    # Make sure that the codec is registered
    codecs.getdecoder(NAME)


# Unit test function for function encode

# Generated at 2022-06-13 20:24:08.742253
# Unit test for function register
def test_register():
    # Unregister the codec
    codecs.lookup_error(NAME)
    # Test that registering the codec succeeds.
    register()
    # Check that the codec name is registered.
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:24:17.395572
# Unit test for function encode
def test_encode():
    """Unit test for function ``encode``."""

# Generated at 2022-06-13 20:24:30.417628
# Unit test for function encode
def test_encode():
    """Unit Test for the function encode."""
    # Test case that is base64 valid.
    assert encode('aGVsbG8gd29ybGQ=') == (b'hello world', 14)
    assert encode('') == (b'', 0)
    assert encode('\n\n\n\n') == (b'', 0)
    assert encode('  \n  ') == (b'', 0)

    # Test cases that are not valid base64.
    try:
        encode('aGVsbG8gd29ybGQ')
    except Exception as e:
        assert isinstance(e, UnicodeEncodeError)

# Generated at 2022-06-13 20:24:33.642853
# Unit test for function register
def test_register():
    """Unit test function :meth:`~register`"""
    register()
    assert NAME in codecs.getencoders()
    assert NAME in codecs.getdecoders()



# Generated at 2022-06-13 20:24:35.507504
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:38.339369
# Unit test for function register
def test_register():
    """Test the register function."""
    print(test_register.__doc__)
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:24:50.079035
# Unit test for function encode
def test_encode():
    """Test for the correct conversion of a base64 character string into a
    bytes string.
    """
    text_1 = (
        'c3RyZWFtIHRvIG1lbW9yeSB3aXRob3V0IHBsYWNlaG9sZGVyIGluc3Ryd'
        'WN0aW9ucw=='
    )
    text_2 = 'IFVubGVhZGluZyBpdC4g'
    text_3 = (
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA='
        'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg'
    )

# Generated at 2022-06-13 20:24:52.097512
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None



# Generated at 2022-06-13 20:24:57.536984
# Unit test for function register
def test_register():
    """Unit test for function: test_register"""
    # Register the codec.
    register()

    # Get the codec info with the name of this codec.
    codec_info_obj = codecs.getdecoder(NAME)  # type: ignore

    # Verify that the codec info is for this codec.
    assert codec_info_obj.name == NAME
    assert codec_info_obj.decode is decode   # type: ignore
    assert codec_info_obj.encode is encode   # type: ignore

# Generated at 2022-06-13 20:25:03.396469
# Unit test for function register
def test_register():
    """Unit test to verify the codec has been registered."""
    register()
    decoded, usecs = codecs.getdecoder(NAME)(
        'aGVsbG8gd29ybGQK'
    )
    assert decoded == 'hello world\n'
    assert usecs == 16


if __name__ == '__main__':
    register()
    # How to test the conversion.
    # >>> b64 = 'aGVsbG8gd29ybGQK'
    # >>> import codecs
    # >>> codecs.decode(b64, 'b64')
    # b'hello world\n'
    # >>> codecs.encode('hello world\n', 'b64')
    # b'aGVsbG8gd29ybGQK'
    #

# Generated at 2022-06-13 20:25:13.570619
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    assert NAME not in codecs.getencodings()
    assert NAME not in codecs.getdecodings()

    codec_info = codecs.lookup(NAME)  # type: ignore

    # unittest for codecs.lookup(NAME)
    def test_lookup():
        """Test the result of the ``lookup`` function."""
        assert codec_info.name == NAME
        assert codec_info.encode == encode
        assert codec_info.decode == decode

    test_lookup()

    # unittest for codecs.getencoder(NAME)
    def test_getencoder():
        """Test the result of the ``getencoder`` function."""
        _, encoder = codecs.getencoder(NAME)
        assert encoder == encode



# Generated at 2022-06-13 20:25:25.221354
# Unit test for function register
def test_register():
    # pylint: disable=W0612
    # noinspection PyUnusedLocal
    from b64codec import b64
    from io import StringIO
    from sys import stdout
    from types import ModuleType

    assert NAME not in globals()
    register()
    assert isinstance(b64, ModuleType)  # noqa
    assert isinstance(b64.Codec, type)
    assert isinstance(b64.TextIOWrapper, type)
    assert isinstance(b64.open, type)
    assert isinstance(b64.register, type)
    assert isinstance(b64.test_register, type)
    assert isinstance(b64.encode, type)
    assert isinstance(b64.decode, type)
    b64.register()
    test_file = StringIO()
   

# Generated at 2022-06-13 20:25:37.756976
# Unit test for function encode
def test_encode():
    # pylint: disable=C0103
    """Test function encode."""
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from . import b64


# Generated at 2022-06-13 20:25:38.491468
# Unit test for function register
def test_register():
    register_codec()

# Generated at 2022-06-13 20:25:39.899012
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:25:40.506586
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:25:43.857429
# Unit test for function register
def test_register():
    assert 'b64' not in codecs.__dict__['_cache']
    register()
    assert 'b64' in codecs.__dict__['_cache']


# Unit tests for function decode

# Generated at 2022-06-13 20:25:57.447276
# Unit test for function register
def test_register():
    """Test function ``register``"""
    # pylint: disable=W0603
    global codecs
    codecs = get_mock_codecs()

    register()
    assert_equal(
        codecs.getdecoder(NAME),
        codecs.CodecInfo(  # type: ignore
            name=NAME,
            decode=decode,  # type: ignore[arg-type]
            encode=encode,  # type: ignore[arg-type]
        )
    )
    codecs = get_mock_codecs()
    register()
    assert_equal(
        codecs.register.call_count,
        1
    )



# Generated at 2022-06-13 20:26:00.703358
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    result = codecs.getdecoder(NAME)
    assert result is not None


# Test coverage.
if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:06.203623
# Unit test for function register
def test_register():
    """Test the function :func:`~register`."""
    # Confirm that the given codec is registered.
    register()
    assert codecs.lookup(NAME) is not None


if __name__ == '__main__':
    test_register()
    print('All tests pass')

# Generated at 2022-06-13 20:26:12.709700
# Unit test for function register
def test_register():
    codecs.register(lambda name: None)                 # type: ignore
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)                         # type: ignore
    register()
    assert codecs.getdecoder(NAME) is not None          # type: ignore



# Generated at 2022-06-13 20:26:15.929166
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert True
    else:
        assert False



# Generated at 2022-06-13 20:26:24.484280
# Unit test for function register
def test_register():
    """test_register unit test"""
    register()
    assert NAME in codecs.getdecoder('b64')


# pylint: disable=unused-argument

# Generated at 2022-06-13 20:26:30.778632
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    # saves the current registered codecs to a local variable.
    prev_codecs = codecs.__dict__['_cache'].copy()
    prev_codec_aliases = codecs.__dict__['_unknown_encoding_copy'].copy()

    # Register the b64 codec
    register()

    # Function 'register' should not have removed any codecs from codecs._cache
    assert len(codecs.__dict__['_cache']) >= len(prev_codecs)
    for key in codecs.__dict__['_cache']:
        if key in prev_codecs:
            assert codecs.__dict__['_cache'][key] == prev_codecs[key]

    # Function 'register' should not have modified codecs._

# Generated at 2022-06-13 20:26:40.155603
# Unit test for function encode
def test_encode():
    import pytest


# Generated at 2022-06-13 20:26:43.710264
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:26:47.516463
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
        assert False, 'Name of custom codec was already registered.'
    except LookupError:
        pass
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:26:51.517858
# Unit test for function register
def test_register():
    """Unit test for function :py:func:`register`"""
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:54.286027
# Unit test for function register
def test_register():
    """Test of 'b64.register'"""
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:27:05.617815
# Unit test for function register
def test_register():
    """Test the function register."""
    # Unregister the 'b64' codec, if it has already been registered.
    try:
        codecs.lookup_error(NAME)
        codecs.unregister(NAME)
    except LookupError:
        pass

    # Verify that the 'b64' codec has not been registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            f'Python was able to decode {NAME!r} without calling the '
            f'function "register()"'
        )

    # Call the function register.
    # Register the 'b64' codec.
    register()

    # Verify that the 'b64' codec has been registered.

# Generated at 2022-06-13 20:27:07.214179
# Unit test for function register
def test_register():
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:27:15.035143
# Unit test for function register
def test_register():
    import unittest.mock
    with unittest.mock.patch(
        'pyt.register_for_decode', unittest.mock.Mock(return_value=None)
    ) as mock_decode:
        with unittest.mock.patch(
            'pyt.register_for_encode', unittest.mock.Mock(return_value=None)
        ) as mock_encode:
            register()
            mock_decode.assert_called_once_with(NAME, decode)
            mock_encode.assert_called_once_with(NAME, encode)


register()

# Generated at 2022-06-13 20:27:29.100870
# Unit test for function encode
def test_encode():
    text_input = """
    H4sICG2QyVwC/92WKW+bMBDHv9kZ9JRmZM8/7V1jogp/s0sPY3YyrQoVu+Td0R7ZuMSiB6W8UvTCr
    +2lYBwUeW8zvBgHZ9f+LgAAAP//
    """
    text_input_str = str(text_input)

# Generated at 2022-06-13 20:27:37.220185
# Unit test for function encode
def test_encode():
    # Test that the function encode() works as expected.
    b64_codec = codecs.getencoder(NAME)

    # Assert that encode of nothing returns nothing.
    assert b64_codec('', 'surrogateescape') == (b'', 0)

    # Assert that encode of a single space returns a single space.
    assert b64_codec(' ', 'surrogateescape') == (b'', 0)

    # Assert that encode of a single tab returns a single tab.
    assert b64_codec('\t', 'surrogateescape') == (b'', 0)

    # Assert that encode of a single line returns a single line.
    assert b64_codec('\n', 'surrogateescape') == (b'', 0)

    # Assert that the encode of the empty string returns the

# Generated at 2022-06-13 20:27:48.238728
# Unit test for function encode
def test_encode():  # pylint: disable=R0912,R0916
    """Test library functionality."""
    from utils import get_test_data


# Generated at 2022-06-13 20:27:49.096853
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()

# Generated at 2022-06-13 20:27:56.124292
# Unit test for function register
def test_register():
    """Test functionality of function register."""
    # Get all the codec names that are registered
    codec_names = list(codecs.__all__)

    # Remove this codec from that list if it is there.
    if NAME in codec_names:
        codec_names.remove(NAME)

    # Register this codec
    register()

    # Test if this codec was registered
    assert NAME in codecs.__all__

    # Get all the codec names that are registered
    new_codec_names = list(codecs.__all__)

    # Test if the this codec was registered by its absence in the new list
    # of codec names that is now registered.
    assert NAME not in new_codec_names

    # Test if all the codecs that were registered before are still
    # in the list of registered codecs.
    assert len

# Generated at 2022-06-13 20:27:58.246069
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:28:02.764543
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`."""
    codecs.register(_get_codec_info)  # type: ignore



# Generated at 2022-06-13 20:28:04.701615
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:28:14.978916
# Unit test for function encode
def test_encode():
    # Test Case 1
    input_text = '''
    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    '''
    expected_output = b'I am killing your brain like a poisonous mushroom'
    output, length = encode(input_text)
    assert(output == expected_output)
    assert(length == len(input_text))

    # Test Case 2
    input_text = '''
    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    '''
    expected_output = b'I am killing your brain like a poisonous mushroom'

# Generated at 2022-06-13 20:28:17.996721
# Unit test for function register
def test_register():
    """Test for function `register`"""
    register()
    # pylint: disable=W0212
    assert codecs.codecs_registered[NAME] is _get_codec_info



# Generated at 2022-06-13 20:28:32.435567
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


register()

# Generated at 2022-06-13 20:28:40.205785
# Unit test for function register
def test_register():
    """Test the register function of this module."""
    import builtins

    try:
        builtins.open
    except AttributeError:
        import __builtin__ as builtins
    # Remove the B64 codec if it has already been registered.
    if NAME in builtins.__dict__.get('__all__'):
        delattr(builtins, NAME)

    # Register the B64 codec.
    register()
    # Make sure the codec is registered.
    assert NAME in builtins.__dict__.get('__all__')

# Generated at 2022-06-13 20:28:43.797739
# Unit test for function register
def test_register():
    """Test registering the codec."""
    # pylint:disable=W0612
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)


# Generated at 2022-06-13 20:28:45.857584
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    # codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:57.515200
# Unit test for function encode
def test_encode():
    """Unit test for ``encode()``"""
    assert encode('YQ==') == (b'a', 4)
    assert encode('cw==') == (b'3', 4)
    assert encode('cXVpY2s=') == (b'quick', 8)
    assert encode('cXVpY2sgc2Fz') == (b'quick sas', 14)
    assert encode('cXVpY2sgc2FzIGRvZw==') == (b'quick sas dog', 22)
    assert encode('cXVpY2sgc2FzIGRvZyBzaG91bGQ=') == (
        b'quick sas dog should', 30)

# Generated at 2022-06-13 20:29:06.566194
# Unit test for function register
def test_register():
    # Import the standard library codecs module.
    # If a user has b64 installed, then codecs and b64.codecs will be
    # different modules.
    codecs2 = __import__('codecs')
    assert codecs2.__name__ != 'b64.codecs'

    # Register the b64 codecs module with the standard library codecs.
    b64.codecs.register()

    # Try to get the 'b64' encoder function from the standard library codecs
    # module.
    try:
        _ = codecs2.getencoder(NAME)
    except LookupError:
        raise AssertionError(
            f'Failed to register the b64 codec: '
            f'codecs.getencoder("{NAME}") raised LookupError'
        )

    #

# Generated at 2022-06-13 20:29:08.286717
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec can be registered."""
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:29:16.128053
# Unit test for function register
def test_register():
    """Unit test for the function :func:`register`."""
    # pylint: disable=W0612
    # noinspection PyUnusedLocal
    def _f():
        encoder = codecs.getencoder(NAME)
        decoder = codecs.getdecoder(NAME)
        stream_reader = codecs.getreader(NAME)
        stream_writer = codecs.getwriter(NAME)
    register()
    _f()



# Generated at 2022-06-13 20:29:29.585138
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('f') == (b'ZA==', 1)
    assert encode('fo') == (b'Zm8=', 2)
    assert encode('foo') == (b'Zm9v', 3)
    assert encode('foob') == (b'Zm9vYg==', 4)
    assert encode('fooba') == (b'Zm9vYmE=', 5)
    assert encode('foobar') == (b'Zm9vYmFy', 6)
    assert encode("f\no\no") == (b'Zm9v', 3)
    assert encode("f\no\no\nb\na\nr") == (b'Zm9vYmFy', 6)



# Generated at 2022-06-13 20:29:43.829452
# Unit test for function encode
def test_encode():
    """Test function encode."""
    # pylint: disable=no-self-use
    text = (
        'SGVsbG8gV29ybGQgU3VwZXIgU3RyZWFtIGJ1dCBzbyBsb25nIGFzIGl0IGlzIHN1Y2ggYS'
        'Bsb25nIHRleHQgSSBhbSBzdHJhaWdodCBtb3ZpbmcgdG8gYW5vdGhlciBsaW5l'
    )
    expected = b'Hello World Super Stream but so long as it is such a long text I am straight moving to another line'
    result, length = encode(text, 'strict')
    assert result == expected
    assert length == len(text)


# Unit test

# Generated at 2022-06-13 20:30:22.416372
# Unit test for function encode
def test_encode():
    pass
    def _test(text: str, expected: bytes):
        result, length = encode(text)
        assert result == expected, (
            f'{text!r} is not properly encoded to: '
            f'{expected!r}'
        )

# Generated at 2022-06-13 20:30:25.600643
# Unit test for function register
def test_register():
    register()
    result = codecs.getdecoder(NAME)
    assert result is not None
    assert result.name == NAME



# Generated at 2022-06-13 20:30:27.811275
# Unit test for function register
def test_register():
    """Test that the ``register`` function is correctly registering the
    ``b64`` codec with Python.
    """
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:30:36.930391
# Unit test for function encode

# Generated at 2022-06-13 20:30:39.659504
# Unit test for function register
def test_register():
    from unittest.mock import patch
    register()
    with patch('codecs.register') as patched_register:
        register()
        patched_register.assert_not_called()

# Generated at 2022-06-13 20:30:41.105283
# Unit test for function register
def test_register():
    """Test that the codec registers"""
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:30:43.423168
# Unit test for function register
def test_register():
    """Test the module's ``register`` function."""
    register()
    codecs.getdecoder(NAME)  # No error means that it is registered.



# Generated at 2022-06-13 20:30:45.397753
# Unit test for function register
def test_register():
    """Test that the b64 function exists."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:30:50.377920
# Unit test for function register
def test_register():
    """Unit test for ``b64.register``"""
    codecs.register(_get_codec_info)
    if NAME not in codecs.getencodings():
        raise Exception('Codec not registered')



# Generated at 2022-06-13 20:30:53.459639
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    assert codecs.getdecoder(NAME) is not None  # type: ignore