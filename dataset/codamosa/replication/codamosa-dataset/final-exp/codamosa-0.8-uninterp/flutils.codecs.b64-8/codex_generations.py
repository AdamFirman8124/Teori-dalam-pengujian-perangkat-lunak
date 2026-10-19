

# Generated at 2022-06-13 20:21:46.743542
# Unit test for function register
def test_register():
    """Register the ``b64`` codec to validate it works without error."""
    register()

# Generated at 2022-06-13 20:21:48.687008
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:21:51.064792
# Unit test for function register
def test_register():
    """Test :py:func:`b64.register`"""
    register()
    print('b64 registered')



# Generated at 2022-06-13 20:21:57.324905
# Unit test for function encode

# Generated at 2022-06-13 20:21:59.694271
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    register()


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:22:07.990010
# Unit test for function encode

# Generated at 2022-06-13 20:22:12.085018
# Unit test for function encode
def test_encode():
    test_string = '''
        eW91IGNhbid0IHJlYWQgdGhpcyB5ZS4=
    '''
    result = encode(test_string)
    assert result == (b'You can\'t read this ye.', len(test_string))



# Generated at 2022-06-13 20:22:18.401749
# Unit test for function register
def test_register():
    """Unit test for ``register``."""
    import sys

    # Capture the existing codec_info for the 'b64' codec.
    old_state = sys.modules[__name__].codec_info

    # Reset the 'b64' codec.
    sys.modules[__name__].codec_info = None

    # Register the 'b64' codec.
    register()

    # TODO: Write a unit test.

    # Reset the 'b64' codec to its previous state.
    sys.modules[__name__].codec_info = old_state



# Generated at 2022-06-13 20:22:28.566394
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import unittest
    import b64

    class TestRegister(unittest.TestCase):
        """Unit test for function register"""

        def test_register(self):
            """Unit test for function register"""
            register()
            self.assertIsInstance(
                codecs.getdecoder(NAME),
                codecs.CodecInfo,
            )

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRegister)
    unittest.TextTestRunner().run(suite)

# Generated at 2022-06-13 20:22:29.863344
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:33.314614
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:44.296482
# Unit test for function register
def test_register():
    """Test the register function of this module."""
    from unittest import TestCase, mock

    from io import BytesIO

    # Get a codecs object.
    codecs_mock = mock.Mock(spec=codecs)

    # Put 'dummy' in the registry
    codecs_mock.lookup.side_effect = LookupError('dummy')

    # Stash the original codecs
    orig_codecs = b64.codecs
    b64.codecs = codecs_mock

    # Verify that register() registers the codec
    register()
    codecs_mock.register.assert_called_once_with(mock.ANY)

    # Verify that register() doesn't register the codec again
    register()
    assert codecs_mock.register.call_count == 1



# Generated at 2022-06-13 20:22:48.330925
# Unit test for function register
def test_register():
    """Test that ``b64`` is registered."""
    register()
    assert(NAME in codecs.getdecoder(NAME).__name__)



# Generated at 2022-06-13 20:22:50.162651
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:22:53.718040
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder(b'aGVsbG8=') == ('hello', 4)



# Generated at 2022-06-13 20:22:56.573327
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()


# When run from the command line, register the ``b64`` codec.
if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:23:04.676271
# Unit test for function register
def test_register():
    """See if ``register`` works.

    The function ``register`` is not a function that needs to be tested
    in a regular way.  This function proves that ``register`` is functional.
    """
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:23:14.640108
# Unit test for function register
def test_register():
    """Test the behavior of the function :func:`~register`."""
    # pylint: disable=W0212
    # Register the function.

# Generated at 2022-06-13 20:23:19.330212
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:23:22.867043
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    register()
    # This will raise an exception if it does not register correctly.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:31.606411
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    import sys
    print(f"Registering {NAME!r} with Python.")
    sys.modules[NAME] = sys.modules[__name__]
    register()

# Generated at 2022-06-13 20:23:41.585061
# Unit test for function register
def test_register():
    """Test the :py:func:`register` function defined in this module."""
    import b64
    try:
        b64.register()
    except Exception as e:  # pylint: disable=broad-except
        pytest.skip(str(e))


# The 'register' function is called when this module is imported, but
# we do not want to do that for test_b64.py.  If the Python script that
# is running ends with 'test_b64.py', then do not import the module.
if not __name__.endswith('test_b64'):
    register()

# Generated at 2022-06-13 20:23:44.642830
# Unit test for function register
def test_register():
    """Ensure that the ``b64`` codec is registered."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:23:48.257931
# Unit test for function register
def test_register():
    """Test to ensure that the b64 codec is register with Python."""
    assert NAME not in codecs.__dict__['_cache']
    register()
    assert NAME in codecs.__dict__['_cache']

# Generated at 2022-06-13 20:23:52.333372
# Unit test for function encode
def test_encode():
    assert encode('RGVzYXJyYXRpbyAtIGJpZ25lc3MgaXMgZ3VhcmFudGVlZCE=') == (b'Desarra_to - bigness is guaranteed!', 44)


# Generated at 2022-06-13 20:23:58.520351
# Unit test for function encode
def test_encode():
    assert encode('A') == (b'A', 1)
    assert encode('SGVsbG8sIHdvcmxkIQ==') \
        == (  # type: ignore
            codecs.decode(  # type: ignore
                'SGVsbG8sIHdvcmxkIQ==', 'base64'
            ),
            24
        )



# Generated at 2022-06-13 20:24:02.593287
# Unit test for function encode
def test_encode():
    text0 = '''
    YWJj
    ZGVm
    '''
    expected00 = b'\x61\x62\x63\x64\x65\x66'
    expected01 = len(text0)
    assert encode(text0) == (expected00, expected01)

    text1 = '''
    YWJj
    ZGVm
    '''
    expected10 = b'dGhpcyBpcyB0ZXN0MQ=='
    expected11 = len(text1)
    assert encode(text1) == (expected10, expected11)



# Generated at 2022-06-13 20:24:13.302787
# Unit test for function register
def test_register():
    """Unit test function for function 'register'."""
    # pylint: disable=invalid-name
    # pylint: disable=no-member
    register()
    e = codecs.lookup_error('b64')
    codecs.lookup_error('b64')
    assert e.name == 'b64'
    assert e.encode(b'test', 'strict')[0] == 'dGVzdA'
    assert e.encode(b'test', 'ignore')[0] == 'dGVzdA'
    assert e.encode(b'test', 'replace')[0] == 'dGVzdA'
    assert e.encode(b'test', 'xmlcharrefreplace')[0] == 'dGVzdA'

# Generated at 2022-06-13 20:24:15.303715
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:20.934592
# Unit test for function encode
def test_encode():
    """Ensure that the text is converted to base64 bytes"""
    assert encode('YmFzZTY0')[0] == b'base64'
    assert encode('YmFzZTY0IC0gcmF3')[0] == b'base64 - raw'
    assert encode('YmFzZTY0IC0gZW5jb2RlZCAtIG5vdCByYXc=')[0] == b'base64 - encoded - not raw'
    assert encode('YmFzZTY0IC0gZW5jb2RlZCAtIG5vdCByYXcNCmxhbmcgPSBidWlsZC9uYXRpdmU=')[0] == b'base64 - encoded - not raw\nlang = build/native'


# Unit test

# Generated at 2022-06-13 20:24:27.896179
# Unit test for function register
def test_register():  # type: ignore
    """Unit test the ``register()`` function."""
    register()

# Generated at 2022-06-13 20:24:29.328085
# Unit test for function encode
def test_encode():
    assert encode('YWJj') == (b'abc', 4)


# Generated at 2022-06-13 20:24:32.552319
# Unit test for function register
def test_register():
    if hasattr(codecs, 'encode'):
        codecs.encode('this string', 'b64')
    else:
        codecs.encode('this string', NAME)


register()

# Generated at 2022-06-13 20:24:34.019223
# Unit test for function register
def test_register():
    from b64 import codec
    codec.register()



# Generated at 2022-06-13 20:24:42.000945
# Unit test for function encode
def test_encode():
    """Test the :meth:`encode()` function."""
    expected = b'\xcd\x8f\xc7\x1f\xa7\x9a\xaa\xa0\x81\xc7\xbb\x8f\x1c\x9b\x9b'
    actual, _ = encode(
        'w7bDv8S1Z6IbA6Fo0cS9zqzh4yI=\n',
    )
    print('expected=0x' + binascii.hexlify(expected).decode())
    print('actual=0x' + binascii.hexlify(actual).decode())
    assert expected == actual


# Generated at 2022-06-13 20:24:46.272820
# Unit test for function register
def test_register():
    register()
    assert NAME == codecs.getdecoder(NAME).name  # type: ignore

if __name__ == '__main__':
    # Run unit tests from the command line.
    import pytest
    pytest.main(args=['.', '-s'])

# Generated at 2022-06-13 20:24:56.291336
# Unit test for function register
def test_register():
    """Test function register"""
    import sys

    # Wrap testing in a function so that the sys.modules are not
    # changed by any test code but restored upon completion of the
    # test.
    def test():
        """Test function register"""
        try:
            # Remove the codec from the codecs module so that we can
            # test that it gets loaded.
            del sys.modules['encodings.b64']
        except KeyError:
            # The codec is not loaded at this point.
            pass

        try:
            # Verify the codec is not present.
            codecs.getdecoder(NAME)
        except LookupError:
            pass
        else:
            raise AssertionError(
                f'The codec encoding.{NAME!r} should not be'
                f'registered at this point.'
            )

        #

# Generated at 2022-06-13 20:24:59.276092
# Unit test for function register
def test_register():
    """Test for function register"""
    import codecs
    from typing import Optional
    from . import codec_info

    register()
    obj: Optional[codecs.CodecInfo] = \
        codecs.getdecoder(NAME)  # type: ignore
    assert obj == codec_info, f'{NAME!r} codec not registered properly'



# Generated at 2022-06-13 20:25:05.094019
# Unit test for function register
def test_register():
    """Verify the b64 codec is registered."""
    import codecs  # pylint: disable=import-outside-toplevel,unused-variable
    from . import b64
    b64.register()

    # noinspection PyUnresolvedReferences
    codecs.getdecoder(b64.NAME)



# Generated at 2022-06-13 20:25:14.312394
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('Y') == (b't', 1)
    assert encode('Zg==') == (b'f', 4)
    assert encode('Zm8=') == (b'fo', 4)
    assert encode('Zm9v') == (b'foo', 4)
    assert encode('Zm9vYg==') == (b'foob', 8)
    assert encode('Zm9vYmE=') == (b'fooba', 8)
    assert encode('Zm9vYmFy') == (b'foobar', 8)
    assert encode('SGVsbG8gd29ybGQh') == (b'Hello world!', 16)
    # The returned length of the value is correct.

# Generated at 2022-06-13 20:25:36.618648
# Unit test for function encode
def test_encode():
    """Test the ``encode`` function."""
    assert encode('eW91IGNhbid0IHJlYWQgdGhpcyE=') == (b"you can't read this!", 20)
    assert encode('eW91IGNhbid0IHJlYWQgdGhpcyE=\n') == (b"you can't read this!", 22)
    assert encode('eW91IGNhbid0IH\nJlYWQgdGhpcyE=') == (b"you can't read this!", 22)
    assert encode('eW91IGNhbid0IH\nJlYWQgdGhpcyE=\n') == (b"you can't read this!", 24)

# Generated at 2022-06-13 20:25:39.947143
# Unit test for function encode
def test_encode():
    result = encode("Test\nHere\nThis\tThat")
    assert result[0] == b'TestHereThisThat' and result[1] == 17



# Generated at 2022-06-13 20:25:46.672136
# Unit test for function register
def test_register():
    """Test the register function."""
    import sys
    d = {
        k: v
        for k, v in sys.modules['encodings'].__dict__.items()
        if k.startswith('__') is False
    }
    assert NAME not in d
    register()
    d = {
        k: v
        for k, v in sys.modules['encodings'].__dict__.items()
        if k.startswith('__') is False
    }
    assert NAME in d



# Generated at 2022-06-13 20:25:49.018821
# Unit test for function register
def test_register():
    codecs.register = Mock()
    register()
    codecs.register.assert_called_with(_get_codec_info)


# Generated at 2022-06-13 20:26:00.488210
# Unit test for function register
def test_register():
    """Unit test."""
    # pylint: disable=W0612
    # pylint: disable=W0613
    def _test(b64_str: _STR, hex_str: _STR):
        """Test the 'b64' codec.

        Args:
            b64_str (str): The string input.  The given string input can span
                across many lines and be indented any number of spaces.
            hex_str (str): The expected hex encoded string.
        """
        b64_str_obj = codecs.encode(b64_str, NAME)
        b64_str_exp = hex_str.encode('ascii')
        assert b64_str_exp == b64_str_obj

        # Make sure the b64 codec works for both bytes and bytearray.

# Generated at 2022-06-13 20:26:03.452993
# Unit test for function encode
def test_encode():
    encoded, length = encode('YWJj')
    assert encoded == b'abc'
    assert length == 4



# Generated at 2022-06-13 20:26:08.244999
# Unit test for function register
def test_register():
    """Test the register() function."""
    register()
    codecs.getdecoder(NAME)  # Should not raise LookupError


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:26:16.407401
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # Verify that this codec isn't already loaded.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('This codec is already loaded.')

    # Verify that it can be registered.
    register()

    # Verify that this codec is now loaded.
    codecs.getdecoder(NAME)      # type: ignore

# Generated at 2022-06-13 20:26:19.035378
# Unit test for function register
def test_register():
    """Unit test for function register.

    The function register() should have no side effects.
    """
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:28.014335
# Unit test for function encode
def test_encode():
    """Test the function, encode."""

    # Valid input

# Generated at 2022-06-13 20:26:56.082008
# Unit test for function register
def test_register():
    """Test function register"""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:27:06.365532
# Unit test for function encode
def test_encode():
    inp = '''
    SGVsbG8sIFdvcmxkIQ==
    '''

    exp = b'Hello, World!'
    out, _ = encode(inp)
    assert out == exp

    inp = '''
        SGVsbG8sIFdvcmxkIQ==
        '''

    out, _ = encode(inp)
    assert out == exp

    inp = '''
        R29vZGJ5ZSE=
        '''
    exp = b'Goodbye!'
    out, _ = encode(inp)
    assert out == exp

    try:
        inp = '''
            SGVsbG8sIFdvcmxkIQ
            '''
        encode(inp)
        assert False
    except UnicodeEncodeError:
        pass



# Generated at 2022-06-13 20:27:14.925807
# Unit test for function register
def test_register():
    # pylint: disable=W0212,W0703
    import sys
    old_getdecoder = sys.modules['codecs'].getdecoder

    try:
        getdecoder_list = []
        sys.modules['codecs'].getdecoder = lambda x: getdecoder_list.pop()

        # Cause the codecs.CodecInfo object to be None
        getdecoder_list.append(None)
        register()

        # Cause the codecs.CodecInfo object to be object
        getdecoder_list.append(object())
        register()

    finally:
        sys.modules['codecs'].getdecoder = old_getdecoder



# Generated at 2022-06-13 20:27:20.689238
# Unit test for function register
def test_register():
    # pylint: disable=unused-variable
    @register()
    def test_decode(data: _ByteString, errors: _STR = 'strict') -> Tuple[str, int]:
        return 'test', len(data)
    assert codecs.getdecoder(NAME)(b'abc').decode() == 'test'



# Generated at 2022-06-13 20:27:28.311772
# Unit test for function register
def test_register():
    """Test function register."""
    if NAME in ('base64', 'b64'):
        # Skip if the codec is the standard Python codec.
        return
    register()
    assert NAME in codecs.decode.cache  # type: ignore
    assert codecs.decode(NAME, b'', 'ignore') == (u'', 0)  # type: ignore
    assert codecs.encode(NAME, u'', 'ignore') == (b'', 0)  # type: ignore
    codecs.decode.cache.pop(NAME, None)  # type: ignore
    codecs.encode.cache.pop(NAME, None)  # type: ignore

# Generated at 2022-06-13 20:27:36.846279
# Unit test for function encode
def test_encode():
    """
    Test encode()
    """
    # -----------
    # Test Valid
    # -----------
    assert encode('YWJj\nZGVm\nZ2hp\naGxq\nbHN0\ndHV2\nd3h5\neHl6')[0] == b'abcdefghijklmnopqrstuvwxyz'
    assert encode('YQ==')[0] == b'a'
    assert encode('YWI=')[0] == b'ab'
    assert encode('YWJj')[0] == b'abc'
    assert encode('YWJjZA==')[0] == b'abcd'
    assert encode('YWJjZGU=')[0] == b'abcde'
    assert encode('YWJjZGVm')

# Generated at 2022-06-13 20:27:40.654952
# Unit test for function register
def test_register():
    """Test function ``register``."""
    old = codecs.getdecoder(NAME)
    codecs.register(_get_codec_info)
    new = codecs.getdecoder(NAME)
    assert old is new



# Generated at 2022-06-13 20:27:46.225521
# Unit test for function register
def test_register():  # pylint: disable=R0911
    """Unit test for function DB_get_codec_info."""
    from shimbase.database import Database
    from . import MockConnection

    test_db = Database(MockConnection, ':memory:')
    test_db.connect()
    test_db.createAllTables()
    test_db.close()


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:27:51.206293
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    obj = codecs.getdecoder(NAME)
    assert obj is not None
    assert decode is obj

    obj = codecs.getencoder(NAME)
    assert obj is not None
    assert encode is obj
    return



# Generated at 2022-06-13 20:28:03.081699
# Unit test for function encode

# Generated at 2022-06-13 20:29:04.270413
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:29:07.642813
# Unit test for function register
def test_register():
    """Assert the ``b64`` codec is not registered."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass

    # Register the codec
    register()

    # Assert register works
    codecs.getdecoder(NAME)  # type: ignore



# Generated at 2022-06-13 20:29:12.959436
# Unit test for function register
def test_register():
    """Unit test for function register"""
    def pop(name: str) -> Optional[codecs.CodecInfo]:
        try:
            return codecs.lookup(name)  # type: ignore
        except LookupError:
            return None


# Generated at 2022-06-13 20:29:18.116042
# Unit test for function register
def test_register():
    """Unit test that ensures the ``b64`` codec is registered with Python"""
    register()
    codec_info: codecs.CodecInfo = codecs.getdecoder(NAME)
    assert codec_info.name == NAME



# Generated at 2022-06-13 20:29:21.628845
# Unit test for function register
def test_register():
    """Verify that the ``b64`` codec is registered with Python."""
    register()
    text = 'SGVsbG8="'
    assert text.encode(NAME) == b'Hello'

# Generated at 2022-06-13 20:29:29.733120
# Unit test for function encode
def test_encode():
    assert encode('A')[0] == b'A'
    assert encode('a')[0] == b'a'
    assert encode('Z')[0] == b'Z'
    assert encode('z')[0] == b'z'
    assert encode('z1')[0] == b'z1'
    assert encode('Z1')[0] == b'Z1'
    assert encode('zB')[0] == b'zB'
    assert encode('ZB')[0] == b'ZB'
    assert encode('zG')[0] == b'zG'
    assert encode('ZG')[0] == b'ZG'
    assert encode('zD')[0] == b'zD'
    assert encode('ZD')[0] == b'ZD'
    assert encode

# Generated at 2022-06-13 20:29:32.100233
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:29:35.198361
# Unit test for function register
def test_register():
    """Unit test for function register"""
    _ = codecs.getdecoder(NAME)


# pylint: disable=W0613

# Generated at 2022-06-13 20:29:39.918411
# Unit test for function register
def test_register():
    """Test function register in module b64_codec."""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:29:50.327205
# Unit test for function register
def test_register():
    """Run the test for function register."""
    # Register the codec.
    register()

    # Get the codec by name
    b64_codec = codecs.getdecoder(NAME)

    # Check that 'b64_codec' has the correct decode method.
    from tests.test_decode import DecodersTestCase
    del DecodersTestCase.test_decode
    DecodersTestCase(decoder=b64_codec, codec_name=NAME)

    # Check that 'b64_codec' has the correct encode method.
    from tests.test_encode import EncodersTestCase
    del EncodersTestCase.test_encode
    EncodersTestCase(encoder=b64_codec, codec_name=NAME)

    # Remove the codec from the registered codecs.
    #