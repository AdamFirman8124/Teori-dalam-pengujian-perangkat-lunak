

# Generated at 2022-06-13 20:21:51.468582
# Unit test for function register
def test_register():
    """Test function register."""
    # Check that the codec was already register, if it was already register
    # then unregister it
    try:
        codecs.lookup(NAME)
        codecs.unregister(NAME)
    except LookupError:
        pass

    # Register the codec
    register()
    codecs.lookup(NAME)
    codecs.unregister(NAME)



# Generated at 2022-06-13 20:21:58.792345
# Unit test for function encode
def test_encode():
    from .ascii import base64_ascii_chars
    from .random_data import random_bytes

    print(f'test_encode {NAME}')

    for i in range(1, 9):
        for j in range(10):
            # Get some random bytes.
            data_bytes = random_bytes(i)
            # Encode the random bytes as base64.
            encoded_bytes, _ = codecs.getencoder('b64')(data_bytes)
            # Decode the encoded bytes.
            decoded_bytes, _ = codecs.getdecoder('b64')(encoded_bytes)
            # Do a basic compare of the random bytes against the decoded
            # bytes.
            assert data_bytes == decoded_bytes

            # Encode the random bytes as base64 with the b64 encoding.


# Generated at 2022-06-13 20:22:01.863172
# Unit test for function register
def test_register():
    """Unit test for function :meth:`~register`."""
    register()
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:11.853826
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    d_obj: Optional[codecs.CodecInfo] = None
    e_obj: Optional[codecs.CodecInfo] = None
    try:
        d_obj = codecs.getdecoder(NAME)
        e_obj = codecs.getencoder('b64')
    except LookupError:
        pass
    if d_obj is None and e_obj is None:
        register()
        d_obj = codecs.getdecoder(NAME)
        e_obj = codecs.getencoder('b64')
    assert d_obj is not None
    assert e_obj is not None
    assert d_obj.name == NAME
    assert e_obj.name == 'b64'
    assert d_obj.decode is decode
    assert e_

# Generated at 2022-06-13 20:22:16.848491
# Unit test for function register
def test_register():
    import sys
    if NAME not in sys.modules:
        # The b64 codec has not yet been registered.
        codecs.register(_get_codec_info)  # type: ignore
        assert 'b64' in sys.modules
        assert sys.modules['b64'] is sys.modules[__name__]
    else:
        assert sys.modules['b64'] is sys.modules[__name__]



# Generated at 2022-06-13 20:22:22.791429
# Unit test for function register
def test_register():
    # pylint: disable=protected-access
    register()
    codecs.CodecInfo = type('CodecInfo', (), {})  # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'The b64 codec has not been registered.'
    else:
        assert True

# Generated at 2022-06-13 20:22:27.865537
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)
        return
    raise Exception('b64 codec should not be registered')

# Generated at 2022-06-13 20:22:38.579285
# Unit test for function encode
def test_encode():
    """Test the function encode"""
    src = 'YWJj'
    dst = b'abc'
    assert encode(src)[0] == dst
    src = 'YWJ\nj'
    dst = b'ab\nj'
    assert encode(src)[0] == dst
    src = 'YWJ\r\nj'
    dst = b'ab\r\nj'
    assert encode(src)[0] == dst
    src = 'YWJ \n\rj'
    dst = b'ab \n\rj'
    assert encode(src)[0] == dst
    src = '   YWJ \n\rj  '
    dst = b'   ab \n\rj  '
    assert encode(src)[0] == dst
    src = 'YWJj   '

# Generated at 2022-06-13 20:22:51.839429
# Unit test for function register
def test_register():
    # Get the current codecs
    codecs_obj = codecs.getdecoder(NAME)
    codecs_obj_type = type(codecs_obj)

    # Remove the b64 codec
    codecs.unregister(codecs_obj_type)

    # Register the b64 codec
    register()

    # Check that the b64 codec works.
    text = 'x' * 2000
    data = text.encode(NAME)

    # The current codecs, now has the b64 codec.  When the ``codec_object``
    # is extracted, and when the ``codec_obj_type`` is extracted, they
    # are not the same python object.  But they are the same type.
    codec_obj: codecs.CodecInfo = codecs.getdecoder(NAME)
    codec_obj_type

# Generated at 2022-06-13 20:22:53.718400
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert codecs.lookup(NAME) is not None

# Generated at 2022-06-13 20:23:00.151940
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.getencoder(NAME) and codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:23:04.759125
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) # type: ignore
    assert codecs.getencoder(NAME) # type: ignore


# Generated at 2022-06-13 20:23:13.642665
# Unit test for function register
def test_register():
    # Test that the 'b64' is not available.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Test that the 'b64' codec is registered.
    register()
    try:
        codecs.getdecoder(__name__.split('.')[-1])
    except LookupError:
        pytest.fail()



# Generated at 2022-06-13 20:23:20.262581
# Unit test for function register
def test_register():
    class TestCodec(codecs.Codec):
        def encode(self, input: str, errors: str = 'strict') -> Tuple[bytes, int]:
            return b'', 0
        def decode(self, input: bytes, errors: str = 'strict') -> Tuple[str, int]:
            return '', 0

    # Register the TestCodec
    codecs.register(TestCodec)

    # Ensure that the TestCodec is registered
    try:
        _ = codecs.getdecoder(TestCodec.__name__)
    except LookupError:
        raise AssertionError(
            f'Codec {TestCodec.__name__} is not registered with Python.'
        )

    register()

# Generated at 2022-06-13 20:23:23.747963
# Unit test for function encode
def test_encode():
    msg = "OmlvmlhZGVyHmFkbw=="
    assert encode(msg) == (b'Deceiver\xf4about', 12)



# Generated at 2022-06-13 20:23:29.867697
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    # Get the b64 codec info to verify the codec is present.
    codec_info = codecs.getdecoder(NAME)   # type: ignore
    assert codec_info.name == NAME, (
        'The codec name {} is not equal to the codec name {}.'
    ).format(NAME, codec_info.name)

    # Cleanup by removing the codec
    codec; del codec
    del codec_info


# Generated at 2022-06-13 20:23:33.484136
# Unit test for function register
def test_register():
    """Test the register() function with this module."""
    register()
    get_decoder = codecs.getdecoder(NAME)
    get_encoder = codecs.getencoder(NAME)
    assert get_decoder(b'YQ==') == ('a', 1)
    assert get_encoder('a') == (b'YQ==', 1)



# Generated at 2022-06-13 20:23:34.927046
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:23:39.094434
# Unit test for function register
def test_register():
    """Test that the b64 codec can be registered with Python"""
    register()

    # Make sure the codec is registered by getting the decoder.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:43.513215
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is _get_codec_info(NAME)
    assert codecs.getencoder(NAME) is _get_codec_info(NAME)



# Generated at 2022-06-13 20:23:52.198077
# Unit test for function register
def test_register():
    """Test that the b64 is registered with the codecs module."""
    codecs.register(_get_codec_info)  # type: ignore
    codec_info = codecs.lookup(NAME)
    assert codec_info.name == NAME
    assert codec_info.decode == decode  # type: ignore[arg-type]
    assert codec_info.encode == encode  # type: ignore[arg-type]


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:23:54.321882
# Unit test for function register
def test_register():
    """Unit test for register."""
    register()

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:56.245162
# Unit test for function encode
def test_encode():
    """Test encode"""
    print(encode('aGVsbG8='))


# Generated at 2022-06-13 20:24:07.895337
# Unit test for function register
def test_register():
    """This is the unit test for the ``register`` function.

    This unit test verifies that the ``register`` function is able to
    install the ``b64`` codec into the Python codecs system.
    """
    import sys
    import unittest
    try:
        codecs.getencoder(NAME)
    except LookupError:
        register()
        target = codecs.getencoder(NAME)
    else:
        target = None
    try:
        sys.modules['__main__'].register
    except KeyError:
        if target is None:
            print('WARNING: Unable to test the ``register`` function, '
                  'because no ``register`` function was found in the '
                  'global name space.')

# Generated at 2022-06-13 20:24:16.807089
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import doctest
    from typing import (
        Any,
        Callable,
        Tuple,
    )

    # noinspection Mypy
    def _get_decoder(name: str) -> Tuple[Callable[..., Any], Callable[..., Any]]:
        """Function to replace the codecs.getdecoder function."""
        if name != NAME:
            raise LookupError(f'mock invalid codec name: {name!r}')
        raise LookupError(f'mock LookupError: {name!r}')

    # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:24:18.590993
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()



# Generated at 2022-06-13 20:24:20.517424
# Unit test for function register
def test_register():
    """Check that the b64 codec is registered."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:28.123838
# Unit test for function encode
def test_encode():
    """Test the base64 encoder"""
    assert encode(b'hello') == (b'aGVsbG8=', 5)
    assert encode(b'Hello, World!') == (b'SGVsbG8sIFdvcmxkIQ==', 14)
    # Test an empty string.
    assert encode(b'') == (b'', 0)
    # Test a string that contains only whitespace.
    assert encode('\n\t') == (b'', 0)



# Generated at 2022-06-13 20:24:38.421819
# Unit test for function encode
def test_encode():
    input_bytes_value = '1234'
    output_bytes_value = b'MTIzNA=='
    tst_str = '''
    MTIzNA==
    '''
    tst_bytes = '''
    MTIzNA==
    '''

    output_bytes, output_len = encode(tst_str)
    assert output_bytes == output_bytes_value
    assert output_len == 11

    output_bytes, output_len = encode(tst_bytes)
    assert output_bytes == output_bytes_value
    assert output_len == 11

    output_bytes, output_len = encode(input_bytes_value)
    assert output_bytes == output_bytes_value
    assert output_len == 4



# Generated at 2022-06-13 20:24:41.249178
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:24:45.373073
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:24:53.592683
# Unit test for function encode
def test_encode():
    """Test the function ``encode``."""
    text = """
    VENU
    S
    +1 (972) 591-6909
    """
    out, _ = encode(text)
    assert out == b'VENUS+1 (972) 591-6909'
    try:
        encode('RENO')
    except UnicodeEncodeError as e:
        assert str(e) == (
            "'b64' codec can't encode character '\\x4e' in position 0: "
            "b'RENO' is not a proper bas64 character string: Incorrect "
            "padding"
        )
    else:
        assert False, 'An UnicodeEncodeError should have been raised.'
    assert encode('') == (b'', 0)

# Generated at 2022-06-13 20:25:01.002364
# Unit test for function register
def test_register():
    """Ensure registration of the ``b64`` codec for Python works.

    The function ``register`` is called within this function to
    ensure the codecs is registered.
    """
    global codecs
    # noinspection PyUnresolvedReferences,PyProtectedMember
    import codecs
    # noinspection PyUnresolvedReferences
    import codecs_b64
    prev_lookup_error = None
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        prev_lookup_error = e
    else:
        raise AssertionError(
            'Codec should not have been registered by another app'
        )

    # Register the codec.
    codecs_b64.register()

# Generated at 2022-06-13 20:25:04.496874
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:06.649773
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:15.026996
# Unit test for function register
def test_register():
    # The first time 'register' is called, the codec should be registered
    # with Python.
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(f'Should be able to get the "{NAME}" codec, '
                             f'but {e}') from e

    # The second time 'register' is called, the codec should NOT be
    # registered.
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(f'Should be able to get the "{NAME}" codec, '
                             f'but {e}') from e


if __name__ == '__main__':
    import sys
    res = test_register()

# Generated at 2022-06-13 20:25:21.048781
# Unit test for function register
def test_register():
    # This will call the function 'register' if __name__ is equal to
    # '__main__'.
    if __name__ == '__main__':
        import codecs
        register()
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)
        print('All unit tests passed')


# Generated at 2022-06-13 20:25:23.040987
# Unit test for function register
def test_register():
    """Test the register function"""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:25.177617
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    _ = codecs.getdecoder(NAME)
    _ = codecs.getencoder(NAME)

# Generated at 2022-06-13 20:25:27.418889
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:25:39.306277
# Unit test for function register
def test_register():
    from _testcapi import register_module_2
    from importlib import _bootstrap

    def get_imp_mod_func(name: str) -> _bootstrap._ModuleFinder:
        module_finder = _bootstrap._ModuleFinder(_bootstrap._path_hooks)
        imp_mod_func = module_finder.find_module_2(name)
        return imp_mod_func

    # Registering module as a directory
    imp_mod_func = get_imp_mod_func(__name__)
    # type: ignore
    module: types.ModuleType = imp_mod_func.module
    module.__name__ = __name__
    register_module_2(module)

# Generated at 2022-06-13 20:25:41.907625
# Unit test for function register
def test_register():
    register()
    # Make sure that the codec was registered.
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:47.440696
# Unit test for function register
def test_register():
    from copy import copy

    from codecs import getdecoder

    register()
    # Assert that the b64 codec is not registered.
    with pytest.raises(LookupError):
        getdecoder(NAME)
    # Create the codecs {decode, encode} function from the base64 library.
    obj = codecs.CodecInfo(  # type: ignore
        name=NAME,
        decode=decode,  # type: ignore[arg-type]
        encode=encode,  # type: ignore[arg-type]
    )
    # Remove the codecs {decode, encode} function.
    codecs.CodecInfo  # type: ignore
    # Try getting the decoder.
    with pytest.raises(LookupError):
        getdecoder(NAME)


# Generated at 2022-06-13 20:25:57.354851
# Unit test for function encode
def test_encode():
    assert encode('aGVsbG8sIHdvcmxk', errors='strict') == (b'hello, world', 15)
    assert encode('c2hvY2s=', 'strict') == (b'shock', 6)
    assert (encode('bWVzc2FnZToNCnN1Y2Nlc3NmdWwgc2hvY2sNCg==', errors='strict') == (
        b'message:\nsuccessful shock\n',
        40
    ))
    try:
        encode('bWVzc2FnZQo=', 'strict')
        assert False
    except UnicodeEncodeError:
        pass



# Generated at 2022-06-13 20:25:59.349640
# Unit test for function register
def test_register():
    """Registers the ``b64`` codec with Python."""
    register()



# Generated at 2022-06-13 20:26:12.725547
# Unit test for function register
def test_register():
    """Test the :func:`~register` function."""

    # Get the current codec info.
    old_info = codecs.lookup(NAME)

    # Register the codec
    register()

    # Get the new codec info.
    new_info = codecs.lookup(NAME)

    # Validate the result.
    assert new_info is not old_info
    assert old_info is not None
    assert new_info is not None
    if old_info is not None:    # pragma: no cover
        assert old_info.name == NAME
        assert old_info.encode is not encode
        assert old_info.decode is not decode
    if new_info is not None:    # pragma: no cover
        assert new_info.name == NAME
        assert new_info.encode is encode

# Generated at 2022-06-13 20:26:22.922182
# Unit test for function register
def test_register():
    import sys
    import types
    from sys import modules  # type: ignore

    # Extract the function codecs.register
    register = codecs.register

    # Insert a mock function into the module 'encodings.base64' as
    # 'codecs.register'
    modules['encodings.base64'] = types.ModuleType('encodings.base64')
    setattr(sys.modules['encodings.base64'], 'codecs', types.ModuleType('codecs'))
    sys.modules['encodings.base64'].codecs.register = lambda x: x  # type: ignore

    # Call the function register
    register()

    # Restore the original function
    sys.modules['encodings.base64'].codecs.register = register


register()

# Generated at 2022-06-13 20:26:26.260828
# Unit test for function register
def test_register():
    """Test when the b64 codec is registered."""
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert "Error"
    else:
        assert "Register Success"


# Generated at 2022-06-13 20:26:29.174450
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()


# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:26:32.531345
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder(NAME)
    else:
        assert False


# Generated at 2022-06-13 20:26:52.255500
# Unit test for function register
def test_register():
    """test_register
    Test the function register().
    """
    import sys
    import unittest

    import json

    # Create a stream capture to capture the output.
    capture = StringCapture()

    # Register the codec.
    register()

    # Use a temporary dictionary to store the codec data.
    tmp_dict = {}

    # Get the encoding of the current sys.stdout
    encoding = sys.stdout.encoding

    # Get the registered codecs
    codec_data = codecs.encode(
        f'{sys.__stdout__.encoding}, ',
        NAME
    )
    tmp_dict['codecs'] = codec_data.decode(encoding)

    # Create a unicode string.

# Generated at 2022-06-13 20:27:04.646949
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # pylint: disable=W0612, W0613
    def check_register(name: str) -> None:
        """Registers the given ``name`` codec with Python"""
        codecs.register(lambda n: codecs.CodecInfo(  # type: ignore
            name=n,
            decode=lambda d, e: (name, len(d)),
            encode=lambda s, e: (bytes(s, 'ascii'), len(s)),
        ))

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail('Could not get registered decoder.')

# Generated at 2022-06-13 20:27:10.244352
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import sys

    try:
        del sys.modules[__name__]
    except KeyError:
        pass
    register()
    assert sys.modules[__name__] is not None
    # assert sys.modules[__name__].encode is not None
    # assert sys.modules[__name__].decode is not None
    # assert sys.modules[__name__].register is not None

# Generated at 2022-06-13 20:27:17.054474
# Unit test for function register
def test_register():
    """Unit test for register()."""
    from unittest.mock import patch

    patch_object = patch(
        f'{__name__}.codecs.register',
        autospec=True,
    )

    with patch_object as mock_register:
        register()
        mock_register.assert_called_once_with(  # type: ignore
            codecs.CodecInfo(  # type: ignore
                name=NAME,
                decode=decode,  # type: ignore[arg-type]
                encode=encode,  # type: ignore[arg-type]
            )
        )


# Generated at 2022-06-13 20:27:27.953535
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    import sys
    import codecs
    import unittest

    org_stdout = sys.stdout
    sys.stdout = sys.__stdout__
    codecs.register(_get_codec_info)
    # noinspection PyProtectedMember
    codec_info = codecs.__dict__['_codec_registry']['b64']

    class TestRegister(unittest.TestCase):
        """Test registering the 'b64' codec."""

        def test_decode(self):
            """Test decoding base64 bytes into Base64 characters."""
            b64_text = "cGxlYXN1cmUu"
            bytes_str = b"pleasure."

# Generated at 2022-06-13 20:27:34.482897
# Unit test for function encode
def test_encode():
    texts = (
        'c3VyZS4=',
        'c3VyZS4=\n',
        'c3VyZS4=\n\n',
        f'\n\nc3VyZS4=',
        f'\n\nc3VyZS4=',
        f'\n\nc3VyZS4=',
    )

    for text in texts:
        assert encode(text)[0] == b'sure.'



# Generated at 2022-06-13 20:27:37.926925
# Unit test for function register
def test_register():
    """unit test for function register"""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:27:49.379255
# Unit test for function register
def test_register():
    """Unittest for function register."""
    # Remove the codec if it is already registered
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    assert codecs.lookup_error(NAME) is not None

    # Unregister the codec to insure it is not registered.
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    assert codecs.lookup_error(NAME) is None

    # Register the codec.
    assert codecs.lookup_error(NAME) is None


# unit test for function decode

# Generated at 2022-06-13 20:27:54.092700
# Unit test for function register
def test_register():
    """Unit test for ``register``."""
    # Register the codec.
    register()

    # Get the codec info from the codec registry.
    codec_info = codecs.getdecoder(NAME)
    assert isinstance(codec_info, codecs.CodecInfo)   # type: ignore

    # Get the codec from the codec_info.
    codec = codec_info.getdecoder(NAME)
    assert callable(codec)



# Generated at 2022-06-13 20:27:59.141603
# Unit test for function register
def test_register():
    """Test function register."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(f"{NAME} codec is not registered: {e}")

# Unit tests for function encode

# Generated at 2022-06-13 20:28:30.791128
# Unit test for function encode
def test_encode():
    inout = [
        ('\x00\x00', 'AAAA'),
        ('\x01\x01', 'AQEB'),
        ('\x01\x00', 'AQAA'),
        ('\x00\x01', 'AAAB'),
        ('\x03\x00', 'AwAA'),
        ('\x00\x03', 'AAAJ'),
        ('\x00\x03\x00', 'AAAJ'),
        ('\x00\x03\x00\x00', 'AAAJAAAA'),
    ]
    for in_, out in inout:
        assert encode(in_)[0] == out.encode('utf-8')


# Generated at 2022-06-13 20:28:36.821011
# Unit test for function register
def test_register():
    """Unit test for function register."""
    def get_decoder(name: str) -> codecs.CodecInfo:
        """Return the codec decoder function for the given ``name``."""
        return codecs.lookup(name).decode  # type: ignore

    try:
        get_decoder(NAME)
    except LookupError:
        register()
        assert get_decoder(NAME)



# Generated at 2022-06-13 20:28:39.200066
# Unit test for function register
def test_register():
    from . import test_register
    test_register.register(NAME, _get_codec_info)


# Unit tests for this module.

# Generated at 2022-06-13 20:28:41.037299
# Unit test for function register
def test_register():
    """mock.patch will change the object pointed to by sys.modules.
    """
    register()



# Generated at 2022-06-13 20:28:46.198684
# Unit test for function register
def test_register():
    """Unit test for ``register``."""
    register()
    try:
        codecs.lookup_error(NAME)
        assert True
    except LookupError:
        assert False

    try:
        codecs.lookup_error(NAME)
        assert True
    except LookupError:
        assert False



# Generated at 2022-06-13 20:28:47.763290
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:58.620476
# Unit test for function register
def test_register():
    """Test registration of the b64 codec."""
    import imp
    import sys

    # Define a dummy module
    mod = imp.new_module('test')
    # Make a copy of the module name space
    mod_name_space = mod.__dict__
    # Initialize the module
    exec('from b64_codec import register\n'
         'register()',
         mod_name_space )
    # Add the module to the current session.
    sys.modules['test'] = mod

    # Verify that the 'b64' codec is registered.
    assert 'b64' in codecs.open(__file__, encoding='utf-8').read()

    # Remove the module from the current session.
    del sys.modules['test']


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:29:00.140275
# Unit test for function register
def test_register():
    """Unit test for function register"""


# pylint: disable=unused-argument

# Generated at 2022-06-13 20:29:03.285216
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert(codecs.getdecoder(NAME) is not None)

# Generated at 2022-06-13 20:29:10.851154
# Unit test for function encode
def test_encode():
    """Test the encode function."""
    assert encode('') == (b'', 0)
    assert encode('AQ==') == (b'\x00', 4)
    assert encode('x') == (b'x', 1)
    assert encode('\nx') == (b'x', 2)
    assert encode('xx') == (b'xx', 2)
    assert encode('\n\nxx\n') == (b'xx', 4)
    assert encode('\n\nxx  \n') == (b'xx', 5)
    assert encode('\n\nxx \n\n') == (b'xx', 5)
    assert encode('\n\nxx  \n\n') == (b'xx', 6)

# Generated at 2022-06-13 20:30:07.951577
# Unit test for function register
def test_register():
    """Tests for the function register()"""
    assert NAME not in codecs.encode.__code__.co_names
    register()
    assert NAME in codecs.encode.__code__.co_names
    test_input = str('\n'.join('0' * 99))
    assert codecs.encode(test_input, 'b64') == ('0' * 84, 99)
    assert codecs.decode(test_input.encode('utf-8'), 'b64') == (
        '0' * 84, 99
    )
    test_input = str('\n'.join('0' * 100))
    assert codecs.encode(test_input, 'b64') == ('0' * 85, 100)

# Generated at 2022-06-13 20:30:18.568027
# Unit test for function encode
def test_encode():
    print('testing function encode')
    test_data = (
        # The expected result following the given input
        (b'hello', b'aGVsbG8='),
        (b'hello world', b'aGVsbG8gd29ybGQ='),
        (b'hello\nworld', b'aGVsbG8Kd29ybGQ=')
    )
    for test_input, expected_result in test_data:
        actual_result, _ = encode(
            codecs.decode(test_input, 'utf-8')  # type: ignore
        )
        assert actual_result == expected_result
        print('  encode(', codecs.decode(test_input, 'utf-8'), ') = ', actual_result.decode(), '==', expected_result.decode())

# Generated at 2022-06-13 20:30:20.779197
# Unit test for function register
def test_register():
    """A function to unit test the function register."""
    register()
    assert codecs.lookup(NAME).name == NAME

# Generated at 2022-06-13 20:30:22.392338
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    register()



# Generated at 2022-06-13 20:30:25.907546
# Unit test for function register
def test_register():
    """Test :meth:`register`."""
    original_name = NAME
    NAME = 'non_existing'
    register()
    NAME = original_name



# Generated at 2022-06-13 20:30:27.449406
# Unit test for function register
def test_register():
    """Unit test for ``register``"""
    register()

# Generated at 2022-06-13 20:30:30.914642
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # Test failed.
        assert False



# Generated at 2022-06-13 20:30:35.678457
# Unit test for function register
def test_register():
    """Unit test for function register."""
    assert _get_codec_info('b64') is None

    # Register the 'b64' codec and verify that the codec was registered.
    register()
    assert _get_codec_info('b64') is not None



# Generated at 2022-06-13 20:30:44.562815
# Unit test for function encode
def test_encode():
    assert encode('QQ==') == (b'A', 2)
    assert encode('RQ==') == (b'RA', 3)
    assert encode('RWE=') == (b'RAB', 4)
    assert encode('RWRhdGE=') == (b'RADATA', 12)
    assert encode('RWE=') == (b'RAB', 1)
    assert encode('RWRhdGE=') == (b'RADATA', 2)
    assert encode('RQ==') == (b'RA', 1)
    assert encode('RWE=') == (b'RAB', 1)
    assert encode('RWRhdGE=') == (b'RADATA', 2)
    assert encode('RQ==') == (b'RA', 1)

# Generated at 2022-06-13 20:30:54.433869
# Unit test for function encode
def test_encode():
    assert encode('SGVsbG8sIFdvcmxkIQ=='), b'Hello, World!'
    assert encode('SGVsbG8sIFdvcmxkIQ==\n')
    assert encode('SGVsbG8sIFdvcmxkIQ==\n\n')
    assert encode('SGVsbG8sIFdvcmxkIQ==\n\n\n')
    assert encode('\nSGVsbG8sIFdvcmxkIQ==\n\n')

