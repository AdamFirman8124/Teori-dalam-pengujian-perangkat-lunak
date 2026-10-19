

# Generated at 2022-06-13 20:21:48.373435
# Unit test for function register
def test_register():
    from codecs import getdecoder
    from importlib import reload
    import sys

    reload(sys.modules[__name__])
    from .b64 import NAME

    getdecoder(NAME)

# Generated at 2022-06-13 20:21:55.132875
# Unit test for function register
def test_register():
    """Test if the ``b64`` is registered with Python."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore
    finally:
        # If the codec is registered, then the lookup error should not
        # be thrown.
        codecs.getdecoder(NAME)  # type: ignore
        # If we get here, then the codec is registered.


encoding = 'b64'

# Register the b64 codec with Python
register()


# Generated at 2022-06-13 20:21:58.237845
# Unit test for function register
def test_register():
    test_case_a = [
        '',
        'A',
        'AA',
        'AAA',
        'AAAA',
        'AAAAA',
        'AAAAAA',
        'AAAAAAA',
        'AAAAA\nAAAA'
    ]
    for test_case in test_case_a:
        encode(test_case)

# Generated at 2022-06-13 20:22:02.690593
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.lookup_error(NAME) is None
    codecs.lookup_error(NAME)
    codecs.lookup_error(NAME)
    codecs.lookup_error(NAME)
    codecs.lookup_error(NAME)


# Generated at 2022-06-13 20:22:12.509800
# Unit test for function encode
def test_encode():
    """
    Unit test for function encode
    """
    assert encode('Zm9v') == (b'foo', 4)
    assert encode('Zm9vYmFy') == (b'foobar', 8)
    assert encode('Zm9vYmFyZGVzYw==') == (b'foobardesc', 12)
    assert encode('Zm9vYmFyZGVzY2dh') == (b'foobardescga', 14)
    assert encode('Zm9vYmFyZGVzY2dhbA==') == (b'foobardescgal', 16)
    assert encode('Zm9vYmFyZGVzY2dhbGRl') == (b'foobardescgalde', 18)

# Generated at 2022-06-13 20:22:21.330969
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    _TEST_ENCODE_TXT = 'YQ=='
    _TEST_ENCODE_BYTES = b'a'
    _TEST_ENCODE_LEN = len(_TEST_ENCODE_TXT)

    VALUE = b'a'

    CODEC = codecs.lookup(NAME)    # type: ignore
    ENCODED = CODEC.encode(VALUE)

    assert ENCODED == (_TEST_ENCODE_BYTES, _TEST_ENCODE_LEN)



# Generated at 2022-06-13 20:22:26.205760
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    assert encode(b64_text) == (
        b'{"one":"dogs","two":[1,2,3],"three":4}',
        len(b64_text)
    )



# Generated at 2022-06-13 20:22:29.214998
# Unit test for function encode
def test_encode():
    encoded = "SGVsbG8gV29ybGQ="
    assert encode(encoded) == (b'Hello World', 15)

# Generated at 2022-06-13 20:22:32.515377
# Unit test for function register
def test_register():  # pylint: disable=W0108
    """Test that the ``b64`` codec is registered with Python."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:41.800417
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    from unittest.mock import patch

    with patch.object(codecs, 'register') as mock:
        # Call function under test.
        register()

        mock.assert_called_once()
        mock.assert_called_with(
            _get_codec_info
        )
        mock.reset_mock()
        with patch.object(codecs, 'getdecoder') as mock_getdecoder:
            mock_getdecoder.side_effect = LookupError()
            register()
            mock_getdecoder.assert_called_once()
            mock_getdecoder.assert_called_with(NAME)
            mock.assert_not_called()
            mock.reset_mock()

# Generated at 2022-06-13 20:22:48.349747
# Unit test for function register
def test_register():
    """Unit test for function register."""
    from codecs import CodecInfo
    from codecs import getdecoder

    register()  # register if not already registered.

    codec_info: CodecInfo = getdecoder(NAME)  # type: ignore
    assert codec_info.name == NAME

# Generated at 2022-06-13 20:22:49.940167
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    # assert codecs.getdecoder(NAME) is not None  # type: ignore

# Generated at 2022-06-13 20:22:55.726659
# Unit test for function register
def test_register():
    """Unit test for function register."""
    assert 'b64' not in codecs.__all__
    register()
    assert 'b64' in codecs.__all__
    assert codecs.lookup(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:58.603667
# Unit test for function register
def test_register():
    """Test to register the ``b64`` codec with Python."""
    codecs.lookup(NAME)


# Generated at 2022-06-13 20:23:03.459887
# Unit test for function register
def test_register():
    import builtins
    # pylint: disable=C0103,E0602
    builtins.__xonsh_env__ = None
    codecs.register = lambda x: None
    register()
    assert codecs.register.call_count == 1
    # pylint: enable=C0103,E0602

# Generated at 2022-06-13 20:23:07.680867
# Unit test for function register
def test_register():
    """Test the function 'register'."""
    # Remove the function '_get_codec_info' from the lookup table.
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        pass

    # Register the function '_get_codec_info'.
    register()

    # Verify that lookup was successful.
    codecs.lookup_error(NAME)   # type: ignore

# Generated at 2022-06-13 20:23:12.642708
# Unit test for function register
def test_register():
    """Test to ensure that the codec has been registered."""
    register()
    codec = codecs.getdecoder(NAME)
    assert isinstance(codec, codecs.CodecInfo)



# Generated at 2022-06-13 20:23:20.178027
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    # pylint: disable=W0612
    def test_decode(data: bytes, errors: str) -> Tuple[str, int]:
        return "decoded", 0

    codecs.register(
        codecs.CodecInfo(  # type: ignore
            name="test_codec",
            decode=test_decode,  # type: ignore[arg-type]
            encode=None,
        )
    )

# Generated at 2022-06-13 20:23:32.304060
# Unit test for function register
def test_register():
    # Unregister the given codec
    codecs.__dict__[NAME] = None

    # Register the given codec.
    register()

    # Test the register resulted in the correct codec being registered.
    assert NAME == codecs.getencoder(NAME)[2]  # type: ignore
    assert NAME == codecs.getdecoder(NAME)[2]  # type: ignore



# Generated at 2022-06-13 20:23:33.990492
# Unit test for function register
def test_register():
    dir(codecs.getdecoder(NAME))

# Generated at 2022-06-13 20:23:38.368869
# Unit test for function register
def test_register():
    assert 'b64' not in codecs._codec_search_path
    register()
    codecs._codec_search_path.index('b64')

# Generated at 2022-06-13 20:23:49.277804
# Unit test for function register
def test_register():
    """Unit test for function ``register``.

    Register the new codec name ``b64``.  Verify the
    new codec name can be used to decode and encode base64 characters.

    """
    register()

    encoded = codecs.encode('hello', 'b64')
    assert type(encoded) == bytes
    assert encoded == b'aGVsbG8='

    decoded, _len = codecs.decode(encoded, 'b64')
    assert type(decoded) == str
    assert decoded == 'hello'


# main
if __name__ == '__main__':
    test_register()
    print('Done!')

# Generated at 2022-06-13 20:23:50.052064
# Unit test for function register
def test_register():
    # register()
    return None



# Generated at 2022-06-13 20:23:53.912749
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.lookup(NAME)
    except LookupError:
        from b64codec.tests import test_register as tester
        tester.register()


# Unit tests for function decode

# Generated at 2022-06-13 20:24:03.609472
# Unit test for function encode
def test_encode():
    t1 = '''
    The quick brown fox jumps over the lazy dog.  The quick brown fox jumps
    over the lazy dog.
    '''
    b1 = encode(t1)[0]

    expected = (
        b'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4gIFRoZS'
        b'BxdWljayBicm93biBmb3gganVtcHMgb3ZlciB0aGUgbGF6eSBkb2cuCg=='
    )

    assert expected == b1


# Generated at 2022-06-13 20:24:08.647866
# Unit test for function register
def test_register():
    """Test function register

    Args:
        None

    Returns:
        None

    """
    assert NAME not in codecs.__dict__['_cache'].keys(), 'codec registered'
    register()
    assert NAME in codecs.__dict__['_cache'].keys(), 'codec not registered'


# Generated at 2022-06-13 20:24:10.246141
# Unit test for function register
def test_register():
    """Test if the codec is available to the codecs module."""
    assert not codecs.lookup(NAME)
    register()
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:24:18.014513
# Unit test for function register
def test_register():
    # Create a test string to encode.
    text = """\
        abcdefghijklmnopqrstuvwxyz
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        0123456789
        +/
    """

    # Create a memoryview object of the test string.
    mem_view = memoryview(text.encode('utf-8'))

    # Encoded the given data into base64 characters
    # pylint: disable=unused-variable
    encoded_str, length = codecs.encode(  # type: ignore
        mem_view,
        NAME,
    )

    encoded_str = encoded_str.decode('utf-8')

    # Decode the base64 characters into bytes
    # pylint: disable=unused-variable
    decoded_bytes

# Generated at 2022-06-13 20:24:23.762802
# Unit test for function register
def test_register():
    # pylint: disable=W0212,protected-access
    from b64 import codec
    # This will raise an Exception if the codec is not registered.
    codec._get_codec_info(NAME)    # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Attribute NAME is not registered.'

# Generated at 2022-06-13 20:24:27.215683
# Unit test for function register
def test_register():
    """Unit test for function :func:`register`"""
    # pylint: disable=W0603
    global NAME
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:40.176680
# Unit test for function encode
def test_encode():
    """Ensure that the function encode encodes as expected."""
    assert encode("aHR0cHM6Ly90b2xlbmdvLm5ldA==") == (b'https://tolle.ngo', 24)
    assert encode("Bw==") == (b'8', 2)
    assert encode("CQ==") == (b'9', 2)
    assert encode("Cg==") == (b':', 2)
    assert encode("Ew==") == (b'?', 2)
    assert encode("FQ==") == (b'@', 2)
    assert encode("Eg==") == (b'>', 2)
    assert encode("EA==") == (b'=', 2)
    assert encode("DQ==") == (b'<', 2)

# Generated at 2022-06-13 20:24:42.562846
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    assert encode('') != ''


# Generated at 2022-06-13 20:24:52.085855
# Unit test for function encode
def test_encode():
    """Unit test for function 'encode'"""

    # Some text to test the encode function with.
    test_text = """
        eW91IGNhbid0IHJlYWQgdGhpcyB5LWF3YXkgc2VjcmV0IGxhbmd1YWdlLiAgSSBkbyBu
        b3Qgc3VnZ2VzdCB5b3UgdHJ5Lgo=
    """

    # The expected output of the 'encode' function.
    test_output = """
        you can't read this y-away secret language.  I do not suggest you try.
    """

    test_input = test_text.strip()

# Generated at 2022-06-13 20:25:00.021357
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)

_TEST_TEXT = (
    'YQoKZW52aXJvbm1lbnQgPSB7CiAgICAiZW52aXJvbm1lbnQiOiB7CiAgICAgICAg'
    'ImZpcnN0IjogdHJ1ZQogICAgfQogICAgfQoKZm9vID0gIiJkZGRkIgoKZm9vID0g'
    'ICJkZGRkIiAgaWYgIiJkZGRkIiA9PSAiIgpERUxFVEUgZm9vCkRFMUVURSBmb28K'
    'REVMRVRFIGZvbwo='
)




# Generated at 2022-06-13 20:25:04.304747
# Unit test for function encode
def test_encode():
    """Test the function ``encode``"""
    text = """
        aGVsbG8sIHdvcmxkIQ==
    """
    expected = b'hello, world!'
    data, _ = encode(text)
    assert data == expected

# Generated at 2022-06-13 20:25:12.219423
# Unit test for function register
def test_register():
    def get_decoder(encoding: str) -> codecs.CodecInfo:
        return codecs.getdecoder(encoding)  # type: ignore

    # Ensure the codec is not registered.
    try:
        get_decoder(NAME)
    except LookupError:
        # Expected failure
        pass
    else:
        # Unexpected success
        assert False

    # Register the ``b64`` codec
    register()

    # Ensure the codec is registered.
    try:
        get_decoder(NAME)
    except LookupError:
        # Unexpected failure
        assert False



# Generated at 2022-06-13 20:25:14.904371
# Unit test for function register
def test_register():
    """Test ``register``"""
    register()
    # now b64 should be registered with Python


if __name__ == '__main__':
    print(f'{register!r}')

# Generated at 2022-06-13 20:25:17.998785
# Unit test for function register
def test_register():
    """test for function register"""
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:25:22.955143
# Unit test for function register
def test_register():
    """Unit test register.

    Note:
        For some reason this test fails the first time this module is
        imported (but it works fine on subsequent imports).  That's
        why this function is tested in ``test/__init__.py``.
    """
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:33.536766
# Unit test for function register
def test_register():
    """Unit test for function register."""
    import re
    import io
    import unittest
    fp = io.StringIO()

    class TestRegistration(unittest.TestCase):  # noqa: N801
        def setUp(self):
            self.real_import = __builtins__.__import__
            __builtins__.__import__ = self.fake_import
            self.imported_packages: dict[str, bool] = {}
            self.register_called: bool = False

        def tearDown(self):
            __builtins__.__import__ = self.real_import


# Generated at 2022-06-13 20:25:45.135634
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec can be registered with Python."""
    # Make sure the codec is not already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, (
            'The function `register` was called when it should not have been.'
        )

    # Register the codec.
    register()

    # Make sure the codec is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'The codec was not registered as it should have been.'



# Generated at 2022-06-13 20:25:47.114255
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False

# Generated at 2022-06-13 20:25:58.289672
# Unit test for function encode
def test_encode():
    assert encode('')[0] == b''
    assert encode('\n')[0] == b''
    assert encode('\n\n\n')[0] == b''
    assert encode(' \n\n \n \n')[0] == b''
    assert encode(' \n\n \n \n ')[0] == b''
    assert encode('\t\t\t\t')[0] == b''
    assert encode(' \t\t\t\t ')[0] == b''
    assert encode(' \t\t\t\t\t ')[0] == b''
    assert encode(' \t\t\t\t \n')[0] == b''
    assert encode(' \t\t\t\t \n ')[0] == b''

# Generated at 2022-06-13 20:26:03.713116
# Unit test for function register
def test_register():
    from b64_codec.b64_codec import register

    register()
    bs = b'hello world'
    try:
        assert codecs.encode(bs, 'b64') == b'aGVsbG8gd29ybGQ='
    except LookupError:
        print()
        raise

    try:
        assert codecs.decode(b'aGVsbG8gd29ybGQ=', 'b64') == b'hello world'
    except LookupError:
        print()
        raise

# Generated at 2022-06-13 20:26:17.691213
# Unit test for function encode

# Generated at 2022-06-13 20:26:27.028776
# Unit test for function encode
def test_encode():
    # pylint: disable=line-too-long
    # Test a base64 string with spaces and newlines.
    assert b'hi' == encode(
        "aGk=",
        'strict'
    )[0]

    # Test a base64 string without spaces and newlines.
    assert b'hi' == encode("aGk=", 'strict')[0]

    # Test mixed base16, base64, and base85
    assert b'hi' == encode("aGkD", 'strict')[0]

    # Test a string with a trailing '=' character
    assert b'hi' == encode("aGk=", 'strict')[0]

    # Test a base64 string with spaces and newlines.

# Generated at 2022-06-13 20:26:34.575072
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import pytest  # type: ignore
    args = (NAME,)
    kwargs = {
        'decode': decode,
        'encode': encode
    }
    with pytest.raises(LookupError):
        codecs.getdecoder(*args)
    codecs.register(_get_codec_info)
    obj = codecs.getdecoder(*args)  # type: ignore
    assert obj == kwargs


# Generated at 2022-06-13 20:26:36.178079
# Unit test for function encode
def test_encode():
    assert encode('eHl6').decode() == 'fool'


# Generated at 2022-06-13 20:26:46.170688
# Unit test for function encode
def test_encode():
    # Test that encode encodes correctly with no trouble characters
    assert encode("aGVsbG8gd29ybGQ=")[0] == b"hello world"
    # Test that encode can handle strange case
    assert encode("aGVsbG8gU3RyYW5nZSBjYXNl")[0] == b"hello Strange case"
    # Test that encode encodes correctly with trouble characters

# Generated at 2022-06-13 20:26:53.274767
# Unit test for function register
def test_register():
    from unittest import TestCase
    from . import codecs_testing

    class TestRegister(TestCase):
        @staticmethod
        def test_register() -> None:
            codecs_testing.register_codec(NAME)

            b64 = codecs_testing.get_codec(NAME)
            assert b64.encode('a')[0] == 'YQ=='
            assert hasattr(b64, 'decode')

            assert b64.decode('YQ==')[0] == 'a'

            assert b64.encode('£')[0] == 'wqU='
            assert hasattr(b64, 'decode')

            assert b64.decode('wqU=')[0] == '£'

            assert b64.encode('£')[0] == 'wqU='

# Generated at 2022-06-13 20:27:02.028560
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    register()



# Generated at 2022-06-13 20:27:08.337901
# Unit test for function encode
def test_encode():
    assert encode('TmVvIEp1bGlhbg==') == (b'Neo Jullian', 14)
    assert encode('TmVvIEp1bGlhbg==', 'replace') == (b'Neo Jullian', 14)
    try:
        encode('TmV1IEp1bGlhbg==')
    except UnicodeEncodeError as error:
        assert error.start == 0
        assert error.end == 14
        assert error.reason == "b'Neu Jullian' is not a proper bas64 character string: Incorrect padding"
    assert encode('NE5F') == (b'NOE', 4)
    assert encode('NE5F') == (b'NOE', 4)

# Generated at 2022-06-13 20:27:11.963365
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import sys
    del sys.modules[__name__]
    register()
    import io
    import b64
    io.TextIOWrapper(io.BytesIO(b'hello'), encoding=b64.NAME).read()

# Generated at 2022-06-13 20:27:23.463367
# Unit test for function encode
def test_encode():
    """Unit test for function encode."""
    assert encode("I'm a string.\n")[0] == b"SSdtIGEgc3RyaW5nLg==\n"
    assert encode("I'm a string.\n")[1] == 16
    assert encode("***I'm a string.***\n")[0] == b"***SSdtIGEgc3RyaW5nLg==***\n"
    assert encode("***I'm a string.***\n")[1] == 20
    assert encode("  ***I'm a string.***  ")[0] == b"  ***SSdtIGEgc3RyaW5nLg==***  "
    assert encode("  ***I'm a string.***  ")[1] == 24

# Generated at 2022-06-13 20:27:25.308131
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:36.010540
# Unit test for function register

# Generated at 2022-06-13 20:27:37.306038
# Unit test for function register
def test_register():
    """Test Function"""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:41.700269
# Unit test for function register
def test_register():
    """Test to make sure the 'b64' codec is registered with Python."""
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Unable to find the %r codec.' % NAME



# Generated at 2022-06-13 20:27:44.832315
# Unit test for function encode
def test_encode():
    assert encode('Zm9vYmEK') == (b'fooba\n', 7)
    assert encode('Zm9vYg==') == (b'foob', 6)
    assert encode('Zm9v') == (b'foo', 4)


# Generated at 2022-06-13 20:27:47.411963
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:28:04.088421
# Unit test for function register
def test_register():
    """Test to ensure the ``b64`` codec is registered with Python."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:07.391182
# Unit test for function encode
def test_encode():
    """Unit test for function encode"""
    assert encode(r'SGVsbG8gV29ybGQh') == (b'Hello World!', 20)



# Generated at 2022-06-13 20:28:14.179817
# Unit test for function register
def test_register():
    """Test that the function register registers the codec with Python."""
    # Try and get the 'b64' type.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # If the 'b64' type does not exist, then register it.
        register()

    # Get the codec for 'b64' type.
    codec = codecs.getdecoder(NAME)

    # Check that the codec name is 'b64'.
    assert codec.name == NAME


# Register the codec.
register()

# Generated at 2022-06-13 20:28:16.315952
# Unit test for function register
def test_register():
    codecs.lookup_error('b64')  # To make sure the codec does not exist.
    register()
    codecs.lookup_error('b64')  # Should not raise exception if worked.



# Generated at 2022-06-13 20:28:17.916626
# Unit test for function register
def test_register():
    """Unit test for the :func:`.register` function."""
    codecs.lookup(NAME)

register()

# Generated at 2022-06-13 20:28:19.406222
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:24.088512
# Unit test for function encode
def test_encode():
    text = "AA==    \n    BB==  \nCC==\ndD==  "
    out, length = encode(text)
    assert out == b'\x00\x10\x00\x11'
    assert length == len(text)



# Generated at 2022-06-13 20:28:30.524433
# Unit test for function register
def test_register():
    """Test the function ``register()``."""
    # pylint: disable=missing-docstring
    import sys
    # Save the state of the 'codecs' module.
    old_module_state = sys.modules.copy()
    # Create a fake module to register.
    fake_module = type(sys)(NAME)
    fake_module.register = register
    sys.modules[NAME] = fake_module
    try:
        # Register the module.
        fake_module.register()
        # Ensure the codec was properly registered.
        codecs.getdecoder(NAME)
    finally:
        # Restore the state of the 'codecs' module to its
        # pre-test condition.
        sys.modules.clear()
        sys.modules.update(old_module_state)



# Generated at 2022-06-13 20:28:31.547875
# Unit test for function register
def test_register():
    """Run the ``register`` function."""
    register()

# Generated at 2022-06-13 20:28:39.327425
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    register()
    assert NAME in str(codecs.__all__)


if __name__ == '__main__':
    register()
    print(f'{NAME} is now registered.')
    print(f'{NAME} codecs.__all__ =', codecs.__all__)
    print(f'{NAME} codecs.__version__ =', codecs.__version__)
    print(f'{NAME} codecs.lookup(name={NAME}) =', codecs.lookup(NAME))

# Generated at 2022-06-13 20:29:04.577518
# Unit test for function encode
def test_encode():
    assert encode('AQIDBAUGBwgJCgsMDQ4PEA==') == (b'\x01\x02\x03\x04\x05\x06\x07\x08\x09', 24), encode('AQIDBAUGBwgJCgsMDQ4PEA==')
    assert encode('AQIDBAUGBwgJCgsMDQ4PEA') == (b'\x01\x02\x03\x04\x05\x06\x07\x08\t', 22), encode('AQIDBAUGBwgJCgsMDQ4PEA')

# Generated at 2022-06-13 20:29:11.619708
# Unit test for function register
def test_register():
    """Test :func:`~b64.register`.  This test is run by pytest."""
    # noinspection PyUnresolvedReferences
    import pytest
    import sys

    @pytest.mark.parametrize("module", [None, sys.modules[__name__]])
    def do_test(module):
        """Test :func:`~b64.register`.

        Args:
            module (Optional[module]): The module to *register*.  If the
                value is None, the module will not be registered.
        """
        if module is None:
            # Save the module in a variable so the variable can be deleted.
            # (module is a weakref)
            m = sys.modules[__name__]
            del sys.modules[__name__]

# Generated at 2022-06-13 20:29:14.467104
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert NAME in codecs.getdecoder(NAME)(b'', NAME)[0]



# Generated at 2022-06-13 20:29:24.572585
# Unit test for function encode
def test_encode():
    assert encode('A') == (b'\x00', 1)
    assert encode('A=') == (b'\x00', 1)
    assert encode('A==') == (b'\x00', 1)
    assert encode('A$') == (b'\x00', 1)
    assert encode('A==', 'strict') == (b'\x00', 1)
    assert encode('') == (b'', 0)
    assert encode('AQ==') == (b'\x01', 1)
    assert encode('AQ==', 'strict') == (b'\x01', 1)
    assert encode('AQg=') == (b'\x01\x00', 1)
    assert encode('AQg=', 'strict') == (b'\x01\x00', 1)


# Generated at 2022-06-13 20:29:26.832899
# Unit test for function register
def test_register():
    """Run module functions that are not tested elsewhere."""
    codecs.register(_get_codec_info)    # type: ignore

# Generated at 2022-06-13 20:29:29.752630
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # pylint: disable=protected-access
    assert codecs._search_function in codecs._register.funcs
    codecs._search_function(NAME)

# Generated at 2022-06-13 20:29:34.984753
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None

# pylint: disable=W0621
# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:29:45.584224
# Unit test for function register
def test_register():
    import sys
    import unittest
    register()
    x = 0
    for index, item in enumerate(sys.modules['codecs']._registry):
        if item == (NAME, _get_codec_info):
            x = 1
            break
    else:
        x = 0
        raise unittest.SkipTest(
            'codecs.register did not work'
        )
    if index != 2:
        raise unittest.SkipTest(
            'codecs.register added codec that is not at index 2'
        )
    return x



# Generated at 2022-06-13 20:29:46.569949
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:29:48.387617
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:30:16.649776
# Unit test for function encode
def test_encode():
    """Test function :func:`encode`."""
    assert encode('a') == (b'a', 1)
    assert encode('b') == (b'b', 1)
    assert encode('c') == (b'c', 1)
    assert encode('d') == (b'd', 1)
    assert encode('e') == (b'e', 1)
    assert encode('f') == (b'f', 1)
    assert encode('g') == (b'g', 1)
    assert encode('h') == (b'h', 1)
    assert encode('i') == (b'i', 1)
    assert encode('j') == (b'j', 1)
    assert encode('k') == (b'k', 1)
    assert encode('l') == (b'l', 1)
    assert encode('m')

# Generated at 2022-06-13 20:30:22.446388
# Unit test for function register
def test_register():
    """Unit test for function register."""
    very_old_register = register

    def register():
        raise Exception()

    try:
        test_register.__code__ = test_register.__code__.replace(
            b'function',
            b'function!!!'
        )
        very_old_register()
    except Exception:
        pass
    finally:
        register = very_old_register


# pylint: enable=W0613

register()

# Generated at 2022-06-13 20:30:25.599891
# Unit test for function encode
def test_encode():    # type: ignore
    assert encode('YWJjZGVm') == (
        b'abcdef',
        8
    )


# Generated at 2022-06-13 20:30:26.480876
# Unit test for function register
def test_register():
    assert codecs.lookup(NAME)



# Generated at 2022-06-13 20:30:34.423862
# Unit test for function register
def test_register():
    register()
    format_str = '{:.<70} {!r}'
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, (
            format_str.format(
                f'{NAME!r} codec not registered in codecs.getdecoder',
                False
            )
        )

    try:
        codecs.getencoder(NAME)
    except LookupError:
        assert False, (
            format_str.format(
                f'{NAME!r} codec not registered in codecs.getencoder',
                False
            )
        )



# Generated at 2022-06-13 20:30:42.073208
# Unit test for function register
def test_register():
    import codecs

    codecs.register(_get_codec_info)  # type: ignore
    # pylint: disable=protected-access
    assert codecs.__all__['b64'] == __name__ + '._get_codec_info'
    assert 'b64' in codecs.__dict__
    assert codecs.getencoder(NAME).__self__._codec_info == 'b64'
    assert codecs.getdecoder(NAME).__self__._codec_info == 'b64'
    # pylint: enable=protected-access


# Generated at 2022-06-13 20:30:43.391798
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:30:48.118477
# Unit test for function register
def test_register():
    """Unit test for the function register."""
    codecs_getdecoder = codecs.getdecoder(NAME)

    def getdecoder(
            codec_name: str
    ) -> Tuple[Optional[codecs.CodecInfo], Optional[str]]:
        """Fake the codecs.getdecoder function so that the ``b64`` codec is
        not registered.

        Args:
            codec_name (str): The name of the codec

        Returns:
            codecs.CodecInfo: Returned if the ``codec_name`` is ``b64``
        """
        if codec_name == NAME:
            return None, None
        return codecs_getdecoder(codec_name)


# Generated at 2022-06-13 20:30:56.474046
# Unit test for function register
def test_register():
    # Test that the codec is already register.  This should succeed.
    codecs.getdecoder(NAME)

    # Unregister the codec.  This should succeed.
    codecs.unregister(NAME)

    # Test that the codec is now unregistered.  This should fail.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register the codec.  This should succeed.
    register()

    # Test that the codec is now registered.  This should succeed.
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:30:57.636475
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

register()

# Generated at 2022-06-13 20:31:33.805573
# Unit test for function register
def test_register():
    """Test the :func:`~b64.register` function."""
    register()



# Generated at 2022-06-13 20:31:36.795007
# Unit test for function register
def test_register():
    """Unregister the ``b64`` codec.

    This is an internal test.  If this fails, the Python interpreter
    will not recognize the ``b64`` codec.
    """
    codecs.unregister(NAME)
    register()
    assert codecs.lookup(NAME)[0] is None   # type: ignore

# Generated at 2022-06-13 20:31:49.510119
# Unit test for function encode
def test_encode():
    # Test basic functionality
    assert encode('/w==')[0] == b'f'
    assert encode('Zg==')[0] == b'f'
    assert encode('Zm8=')[0] == b'fo'
    assert encode('Zm9v')[0] == b'foo'
    assert encode('Zm9vYg==')[0] == b'foob'
    assert encode('Zm9vYmE=')[0] == b'fooba'
    assert encode('Zm9vYmFy')[0] == b'foobar'
    assert encode('/w==')[1] == 4
    assert encode('/w==')[1] == 4
    assert encode('Zm9vYmFy')[1] == 12