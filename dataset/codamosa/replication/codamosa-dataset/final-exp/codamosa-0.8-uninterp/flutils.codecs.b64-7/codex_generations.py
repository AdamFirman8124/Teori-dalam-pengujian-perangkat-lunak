

# Generated at 2022-06-13 20:21:53.452953
# Unit test for function encode
def test_encode():
    # Internally, the bytes are of the form
    #   b'\xF0\x9F\x98\x84'
    # or, if you prefer,
    #   '\u1F604'.encode('utf-8')
    # which is base64:
    #   b'8J+YhA=='
    # as verified by:
    # python3 -c '\
    #   import base64; \
    #   print(base64.b64encode(b"\xF0\x9F\x98\x84"))'
    # This test case is from:
    # https://github.com/ChyronHego/emoji-encoding/blob/master/tests.py
    assert encode(b'\xF0\x9F\x98\x84')

# Generated at 2022-06-13 20:21:59.774834
# Unit test for function encode
def test_encode():
    # Test with a plain string that is already base64 encoded.
    text = 'dGVzdA=='
    out, _ = encode(text)
    assert out == b'test'

    # Test with a string that is not base64 encoded.
    text = 'test'
    try:
        encode(text)
        assert False
    except UnicodeEncodeError:
        assert True
    except Exception:
        assert False

    # Test with a string that is only a part of base64 encoded string.
    text = 'dGVzdA=='
    try:
        encode('dGVzdA')
        assert False
    except UnicodeEncodeError:
        assert True
    except Exception:
        assert False

    # Test with a string that is a base64 encoded string with whitespace

# Generated at 2022-06-13 20:22:01.907420
# Unit test for function register
def test_register():
    """Unit test for function :py:func:`.register`"""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:02.876571
# Unit test for function register
def test_register():
    codecs.lookup(NAME)


# Generated at 2022-06-13 20:22:06.152518
# Unit test for function register
def test_register():
    """Test the function register"""
    register()
    try:
        codecs.getdecoder(NAME)   # type: ignore
    except LookupError as e:
        raise AssertionError(e)



# Generated at 2022-06-13 20:22:08.875595
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:19.483097
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('=') == (b'', 0)
    assert encode('_') == (b'', 0)
    assert encode('\n') == (b'', 0)
    assert encode(' ') == (b'', 0)
    assert encode('a') == (b'', 0)
    assert encode('A') == (b'', 0)
    assert encode('9') == (b'', 0)
    assert encode('+') == (b'', 0)
    assert encode('/') == (b'', 0)
    assert encode('= ') == (b'', 0)
    assert encode('=\n') == (b'', 0)
    assert encode('=\t') == (b'', 0)



# Generated at 2022-06-13 20:22:23.185964
# Unit test for function register
def test_register():
    """Unit test the ``register()`` function."""
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:22:29.489141
# Unit test for function register
def test_register():
    """Verify that the `b64` codec is registered with Python."""
    import codecs

    codecs.getdecoder(NAME)  # type: ignore


# pylint: disable=wrong-import-position
if __name__ == "__main__":
    register()
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 20:22:31.971685
# Unit test for function register
def test_register():
    """Test function register."""
    register()
    obj = codecs.getdecoder(NAME)
    assert obj



# Generated at 2022-06-13 20:22:39.698138
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode(' ') == (b'MA==', 4)
    assert encode(' a') == (b'IGE=', 4)
    assert encode('  a') == (b'ICA=', 4)
    assert encode(' a ') == (b'IGU=', 4)
    assert encode('  a ') == (b'ICAg', 4)

# Generated at 2022-06-13 20:22:43.697658
# Unit test for function register
def test_register():
    """Unit test for function ``register``.

    This function is good for a unit test because it is called
    automatically when the module is loaded.
    """
    register()

# Generated at 2022-06-13 20:22:46.002332
# Unit test for function register
def test_register():
    """Testing the register() function."""
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:52.545310
# Unit test for function register
def test_register():  # pragma: no cover
    """Unit test for function register.
    """
    import codecs
    codecs.register(test_register)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            'The codec was not registered'
        )
    else:
        print('The codec was registered.')

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    test_register()

# Generated at 2022-06-13 20:22:54.900045
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getencoder(NAME)
    except LookupError:
        register()

# Generated at 2022-06-13 20:22:59.735306
# Unit test for function register
def test_register():
    import io
    register()

    # Encode the encoded string.
    output = io.StringIO()
    codecs.register()
    codecs.register()
    encoder = codecs.getencoder(NAME)
    encoder('hello, world')
    output.getvalue()

# Generated at 2022-06-13 20:23:03.308690
# Unit test for function encode
def test_encode():
    """Ensure that the function encode encodes the string in base64"""
    result = encode("Text to encode")
    assert result[0] == b'VGV4dCB0byBlbmNvZGU=\n'


# Generated at 2022-06-13 20:23:12.343859
# Unit test for function encode
def test_encode():
    """Unit test for function encode."""

# Generated at 2022-06-13 20:23:20.087609
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:23:32.241736
# Unit test for function encode
def test_encode(): #type:ignore
    # Tests that encode() with data other than a str (or unicode)
    #   raises a TypeError.
    def do_test_encode_type(obj: object) -> None:
        with pytest.raises(TypeError):
            encode(obj)

    do_test_encode_type(None)
    do_test_encode_type(False)
    do_test_encode_type(True)
    do_test_encode_type(12345)
    do_test_encode_type(1.2345)
    do_test_encode_type([None])
    do_test_encode_type({None: None})
    do_test_encode_type(b'a')

# Generated at 2022-06-13 20:23:35.436217
# Unit test for function register
def test_register():
    """Test that registers the ``b64`` codec to the Python system."""
    register()

# Generated at 2022-06-13 20:23:40.200908
# Unit test for function register
def test_register():
    # pylint: disable=W0612
    # noinspection PyUnusedLocal
    def dummy_decoder(data, *_):
        # type: (bytes, str) -> Tuple[str, int]
        return '', len(data)

    # noinspection PyUnusedLocal
    def dummy_encoder(text, *_):
        # type: (str, str) -> Tuple[bytes, int]
        return b'', len(text)
    # pylint: enable=W0612

    CODEC_NAME = 'dummy'

# Generated at 2022-06-13 20:23:47.599464
# Unit test for function encode
def test_encode():
    text = "bG9uZyB0ZXh0IHdpdGggdW5jb21tb24gY2hhcnMgc2hvdWxkIHRlc3QgY29ycmVjdGx5"
    assert encode(text)[0] == b"long text with uncommon chars should test correctly"
    assert encode(text)[1] == 64

# Generated at 2022-06-13 20:23:54.005907
# Unit test for function encode
def test_encode():
    assert encode('Zm9vYmFy') == b'foobar'
    assert encode('Zm9v YmFy') == b'foobar'
    assert encode('Zm9v\nYmFy') == b'foobar'
    assert encode('Zm9v\rYmFy') == b'foobar'
    assert encode('Zm9v\r\nYmFy') == b'foobar'
    assert encode('Zm9v\r\r\r\r\r\nYmFy') == b'foobar'
    assert encode('Zm9v\n\n\n\n\nYmFy') == b'foobar'
    assert encode('Zm9v\n  YmFy') == b'foobar'

# Generated at 2022-06-13 20:24:00.973282
# Unit test for function register
def test_register():
    """Unit test for function register"""
    import pickle                    # nosec

    with pickle.Unpickler('RegT.pickle') as unpickler:
        reg_t = unpickler.load()
    assert reg_t.load_module(NAME) == sys.modules[__name__]
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None

# Generated at 2022-06-13 20:24:10.415415
# Unit test for function encode
def test_encode():
    assert encode(
        '''
        B64hello world
    ''',
    ) == (b'hello world', 23)
    assert encode('B64hello world') == (b'hello world', 13)
    assert encode(
        '''
        B64hello
        world
    ''',
    ) == (b'hello\nworld', 21)
    assert encode(
        '''
        B64
        hello
        world
    ''',
    ) == (b'hello\nworld', 21)
    assert encode(
        '''
            B64
        hello
        world
    ''',
    ) == (b'hello\nworld', 25)



# Generated at 2022-06-13 20:24:13.046849
# Unit test for function register
def test_register():
    """
    Unit test for function register()
    """
    register()

    # Assert that 'b64' can be used as an encoding argument.
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:24:20.774391
# Unit test for function register
def test_register():
    """Test function register.

    test_register is invoked by py.test.
    """
    register()
    # Since the 'register' function is only executed once,
    # we must catch the 'LookupError' to test that the module
    # is registered appropriately.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail(
            'register not executed appropriately or executed more than'
            ' once.'
        )
    except TypeError:
        pytest.fail(
            'Register failed.  TypeError is proprietary to pytest, but '
            'is caused by a TypeError.'
        )



# Generated at 2022-06-13 20:24:23.825122
# Unit test for function register
def test_register():

    # Call the function being tested
    register()



if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:30.597179
# Unit test for function register
def test_register():
    """Unit test for function register."""
    from unittest.mock import patch
    from . import b64
    import codecs
    patch_call = patch.object(
        codecs, 'register', autospec=True,
    )
    with patch_call as mock_register:  # type: Mock
        # Need to make the test function `register` name the same as the
        # function being tested so that the test function is called
        b64.register()
        assert mock_register.call_count == 1
        assert mock_register.call_args == call(b64._get_codec_info)


# Unit Test for function decode

# Generated at 2022-06-13 20:24:33.689219
# Unit test for function register
def test_register():
    pass


try:
    codecs.getdecoder(NAME)
except LookupError:
    register()



# Generated at 2022-06-13 20:24:35.554931
# Unit test for function register
def test_register():
    # pylint: disable=eval-used
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:42.700780
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    # noinspection PyUnresolvedReferences
    import sys
    # Get the current state of the 'b64' codec.
    orig_b64_decode = codecs.lookup('b64').decode

    # Register the 'base64' codec.
    codecs.register(_get_codec_info)

    # Ensure the 'b64' codec was added to the known codecs.

# Generated at 2022-06-13 20:24:43.725698
# Unit test for function register
def test_register():   # type: ignore
    pass


# Generated at 2022-06-13 20:24:52.886029
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None
    assert NAME in [x[0] for x in codecs.iterdecoders()]
    assert NAME in [x[0] for x in codecs.iterencoders()]


if __name__ == '__main__':
    # Register the ``encode`` and ``decode`` functions with Python
    register()

    # Example.
    # Encode the given bytes into base64
    # 'T051dG9z' is the resulting utf8 string that contains the base64 bytes
    # of the given input_bytes
    input_bytes = bytes([1, 2, 3, 4, 5])
    out, length = codecs.getencoder(NAME)(input_bytes)
   

# Generated at 2022-06-13 20:25:00.607258
# Unit test for function encode
def test_encode():
    assert encode('nngw', 'error') == (b'\\x9c', 4)
    assert encode('mngv', 'error') == (b'\\x9b', 4)
    assert encode('mjg3', 'error') == (b'\\x9a', 4)
    assert encode('mhg5', 'error') == (b'\\x99', 4)
    assert encode('meg2', 'error') == (b'\\x98', 4)
    assert encode('mcgz', 'error') == (b'\\x97', 4)
    assert encode('mbgx', 'error') == (b'\\x96', 4)
    assert encode('m9gv', 'error') == (b'\\x95', 4)

# Generated at 2022-06-13 20:25:03.819901
# Unit test for function register
def test_register():
    """Test register()"""
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder(b'abcdef', 'strict') == ('abcdef', 6)



# Generated at 2022-06-13 20:25:07.060979
# Unit test for function register
def test_register():
    """Ensure registering works."""
    # pylint: disable=unused-variable,unused-import
    from base64_codec import b64



# Generated at 2022-06-13 20:25:11.933382
# Unit test for function encode
def test_encode():
    with pytest.raises(UnicodeEncodeError):
        encode('AQEB/o=')

    text = 'AQEB/o='
    expected_data = b'\x01\x02\x03'
    actual_data, actual_length = encode(text)
    assert actual_data == expected_data
    assert actual_length == len(text)


# Generated at 2022-06-13 20:25:23.723455
# Unit test for function register
def test_register():
    import os
    _, _, registered_codecs = codecs.lookup(NAME)
    assert registered_codecs is None
    register()
    _, _, registered_codecs = codecs.lookup(NAME)
    assert registered_codecs is not None


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Test the 'base64' character codec."
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help="Test the codec."
    )
    parser.add_argument(
        '--register',
        action='store_true',
        help="Register the codec with the Python codec system.",
        default=True,
    )
    args = parser.parse_args()

# Generated at 2022-06-13 20:25:27.914519
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()



# Generated at 2022-06-13 20:25:33.006659
# Unit test for function register
def test_register():
    """Test the register() function."""
    # Given
    _ = globals().pop('codecs', None)

    # When
    register()

    # Then
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()  # pragma: no cover

# Generated at 2022-06-13 20:25:35.389443
# Unit test for function register
def test_register():
    """Unit test for the function register."""
    register()
    assert NAME in codecs._cache
    assert NAME in codecs._cache_encodings



# Generated at 2022-06-13 20:25:38.140989
# Unit test for function register
def test_register():
    """Test registration of ``b64`` codec with Python."""
    register()
    assert NAME in codecs.getdecoder('b64')

# Generated at 2022-06-13 20:25:41.904321
# Unit test for function register
def test_register():
    """Unit test for function b64.register"""

    import codecs
    codecs.register(_get_codec_info)
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:43.286365
# Unit test for function register
def test_register():
    """Unit test for `register`."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:25:46.545864
# Unit test for function register
def test_register():   # pragma: no cover
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:50.420380
# Unit test for function register
def test_register():
    """Test for :func:`~.register`"""
    from .test_b64 import test_funcs
    register()
    test_funcs.test_register(NAME)

# Generated at 2022-06-13 20:25:53.700710
# Unit test for function register
def test_register():
    """Test that the codec is registered."""
    register()
    codecs.getdecoder(NAME)

register()



# Generated at 2022-06-13 20:25:57.395453
# Unit test for function encode
def test_encode():
    """Ensure that the ``encode`` function works as expected."""
    assert encode('QWxhZGRpbjpvcGVuIHNlc2FtZQ==') == (
        b'Aladdin:open sesame',
        24
    )



# Generated at 2022-06-13 20:26:03.390464
# Unit test for function register
def test_register():
    # Verify that the b64 codec can be registered.
    # This test is intended to be used by the function in unit
    # tests.
    register()



# Generated at 2022-06-13 20:26:16.777502
# Unit test for function encode
def test_encode():
    """
    """
    encoder = encode
    test_data = (
        ("", b""),
        ("f", b"Zg=="),
        ("fo", b"Zm8="),
        ("foo", b"Zm9v"),
        ("foob", b"Zm9vYg=="),
        ("fooba", b"Zm9vYmE="),
        ("foobar", b"Zm9vYmFy"),
    )
    for test_str, exp_bytes in test_data:
        act_bytes, _ = encoder(test_str)
        assert exp_bytes == act_bytes
    # This should raise an error.

# Generated at 2022-06-13 20:26:21.529935
# Unit test for function register
def test_register():
    """Unit test for function register"""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        test = codecs.getdecoder(NAME)
        # Unit test:
        assert test.encode.__name__ == encode.__name__
        assert test.decode.__name__ == decode.__name__

# Generated at 2022-06-13 20:26:24.402692
# Unit test for function register
def test_register():
    """Test for ensuring the ``b64`` codec is registered.

    To test, execute the following commands::

        python -m pytest b64.py

    """
    register()
    assert NAME in codecs.__all__

# Generated at 2022-06-13 20:26:30.528259
# Unit test for function encode
def test_encode():
    """Test the :obj:`b64.encode` function."""
    TEST_VALUE = 'SGVsbG8gV29ybGQhIyMjIyMj'
    EXPECTED_VALUE = b'Hello World!!!!'
    actual = encode(TEST_VALUE)
    assert actual == (EXPECTED_VALUE, len(TEST_VALUE))

    # Test encoding a non-base64 byte string.
    NON_BASE64 = (
        'Hello World\n'
        'This is not base64 characters and should raise an error.'
    )
    try:
        encode(NON_BASE64)
    except UnicodeEncodeError:
        pass
    else:
        assert False, 'Failed to raise UnicodeEncodeError.'



# Generated at 2022-06-13 20:26:39.960733
# Unit test for function encode
def test_encode():
    """Test the ``encode`` function."""
    assert encode('A') == (b'QQ==', 1)
    assert encode('A\nB') == (b'QQ==', 3)
    assert encode('A\nB\nC') == (b'QQ==', 5)
    assert encode('A\nB\nC\nD') == (b'QQ==', 7)
    assert encode('A\nB\nC\nD\nE') == (b'QQ==', 9)
    assert encode('A\nB\nC\nD\nE\nF') == (b'QQ==', 11)

    assert encode('AA') == (b'QUI=', 2)
    assert encode('AA\nBB') == (b'QUI=', 4)

# Generated at 2022-06-13 20:26:43.823745
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)   # If we get here and do not raise an exception the decoder is registered.



# Generated at 2022-06-13 20:26:52.126990
# Unit test for function encode

# Generated at 2022-06-13 20:27:04.580351
# Unit test for function register
def test_register():
    """Test the b64.register() function"""
    # pylint: disable=W0212
    try:
        codecs.getdecoder(NAME)
        # The codec is already registered, unregister it so we can
        # execute the tests.
        codecs.lookup(NAME).__delitem__('decode')
    except LookupError:
        # The codec is not registered, pass over the except clause,
        # and to the else clause so we can execute the tests.
        pass
    else:
        # The codec is already registered.  Unregister it, so we can
        # execute the tests.
        codecs.lookup(NAME).__delitem__('decode')

    # Test register().  The codec should not be registered.
    assert NAME not in codecs.__all__   # type: ignore
    assert NAME

# Generated at 2022-06-13 20:27:06.406142
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:27:15.568211
# Unit test for function register
def test_register():
    """Test the function 'register()'."""
    # Register b64 codec
    register()

    assert codecs.getdecoder(NAME)
    assert NAME in codecs.decode.__code__.co_names
    assert codecs.getencoder(NAME)
    assert NAME in codecs.encode.__code__.co_names



# Generated at 2022-06-13 20:27:19.261932
# Unit test for function register
def test_register():
    register()  # type: ignore
    assert NAME == codecs.getdecoder(NAME).name
    assert NAME == codecs.getencoder(NAME).name



# Generated at 2022-06-13 20:27:26.183534
# Unit test for function register
def test_register():
    # Because of the way Python's import system works, the top level module
    # is not always the module that is being unit tested...
    lcls = locals()
    lcls['b64'] = lcls.pop('b64')
    lcls['test'] = lcls.pop('test')
    lcls['test_register'] = lcls.pop('test_register')
    import doctest
    doctest.testmod(lcls)


register()

# Generated at 2022-06-13 20:27:30.724980
# Unit test for function register
def test_register():
    """Test the register function."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:27:37.815727
# Unit test for function register
def test_register():
    import sys

    # The 'b64' codec should not already be in the codec map.
    sys_getdecoder = sys.getdecoder(NAME)
    assert sys_getdecoder is None

    # Register the 'b64' codec.
    register()

    # The 'b64' codec should now be in the codec map.
    getdecoder = codecs.getdecoder(NAME)
    assert getdecoder is not None

    # pylint: disable=W0613
    def getdecoder_wrapper(errors=None):  # pylint: disable=unused-argument
        return None, None
    # pylint: enable=W0613

    # The codec map should not be reassigned to 'getdecoder_wrapper'.
    codecs.getdecoder = getdecoder_wrapper
    register()
    assert get

# Generated at 2022-06-13 20:27:48.700930
# Unit test for function encode
def test_encode():
    """Unit test for ``encode``."""
    import os

    # Test when the input string is empty.
    s = ''
    expected = b''
    actual, _ = encode(s)
    assert actual == expected, (
        'When the input string is empty, the actual conversion is '
        f'{actual!r}. It must be {expected!r}.'
    )

    # Test when the input string is a single line without whitespace.
    s = 'Hello world!'
    expected = b'SGVsbG8gd29ybGQh'
    actual, _ = encode(s)
    assert actual == expected, (
        'When the input string is a single line without whitespace, '
        f'the actual conversion is {actual!r}. It must be {expected!r}.'
    )

    # Test when the

# Generated at 2022-06-13 20:27:55.937856
# Unit test for function register
def test_register():
    """Assert that the ``register()`` function registers the ``b64``
    codec."""
    from os import environ
    from os.path import join
    from subprocess import (
        Popen,
        PIPE,
    )
    from sys import executable
    from tempfile import mkdtemp

    # Generate a temporary directory.
    temp_dir = mkdtemp()

    # Generate a script to import the 'register()' function and execute it.
    script = join(temp_dir, 'test_register_script.py')
    with open(script, mode='w') as f:
        f.write('''\
import pycodecs.b64
pycodecs.b64.register()
''')

    # Execute the script.

# Generated at 2022-06-13 20:27:58.053925
# Unit test for function register
def test_register():
    codecs.lookup_error = LookupError
    assert codecs.lookup_error == LookupError



# Generated at 2022-06-13 20:28:10.202548
# Unit test for function encode
def test_encode():
    assert encode('QQ==') == (b'A', 4)
    assert encode('cw==') == (b'2', 4)
    assert encode('dA==') == (b'M', 4)
    assert encode('TWE=') == (b'12', 4)
    assert encode('dGVzdA==') == (b'test', 8)
    assert encode('Z2FzZg==\n') == (b'gase', 8)
    assert encode('Z2FzZg==\n') == (b'gase', 8)
    assert encode('Z2FzZg==\n') == (b'gase', 8)
    assert encode('M2Y=') == (b'3f', 4)


# Generated at 2022-06-13 20:28:18.061979
# Unit test for function encode
def test_encode():
    """Test the encode function."""
    from encon.tests.base64_test import TEST_VECTOR, DATA

    def _encode_test():
        """Create a generator that yields the test cases."""
        yield TEST_VECTOR
        yield '\n'.join(TEST_VECTOR.split())
        yield '\n'.join(TEST_VECTOR.split()[1:])
        yield '\n\n'.join(TEST_VECTOR.split())
        yield '\n\n'.join(TEST_VECTOR.split()[1:])
        yield '\n'.join(['\t{}\t'.format(x) for x in TEST_VECTOR.split()])

# Generated at 2022-06-13 20:28:41.398211
# Unit test for function encode
def test_encode():
    assert encode('Ymlu\nYmFzZTY0Cg==') == (b'bin\nbase64\n', 26)
    assert encode('Ymlu\nYmFzZTY0Cg=' ) == (b'bin\nbase64\n', 25)
    assert encode('Ymlu\nYmFzZTY0Cg' ) == (b'bin\nbase64\n', 24)
    assert encode('Ymlu\nYmFzZTY0C' ) == (b'bin\nbase64', 20)
    assert encode('Ymlu\nYmFzZTY0' ) == (b'bin\nbase64', 16)
    assert encode('Ymlu\nYmFzZTY' ) == (b'bin\nbase6', 12)
   

# Generated at 2022-06-13 20:28:49.444272
# Unit test for function register
def test_register():
    """Test :func:`register()`."""
    register()
    codec_info = codecs.getdecoder(NAME)

    # Make sure the correct codec is registered.
    assert codec_info.name == NAME
    # pylint: disable=E1123
    assert codec_info.decode()[0] == 'Zm9vIGJhcg=='
    assert codec_info.encode()[0] == b'YmFyIGZvbw=='

# Generated at 2022-06-13 20:28:59.377610
# Unit test for function encode
def test_encode():
    # A simple test case.
    assert encode('THROW AWAY!') == (b'MTJRPVdBU1kh', 11)

    # Test that encode can accept a UserString.
    assert encode(UserString('THROW AWAY!')) == (b'MTJRPVdBU1kh', 11)

    # Test that encode can accept multi-line base64 strings.
    assert encode('  \n   THROW AWAY!  \n  ') == (b'MTJRPVdBU1kh', 11)

    # Test that encode can decode multi-line base64 strings.

# Generated at 2022-06-13 20:29:02.866470
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    # pylint: disable=W0603
    # pylint: disable=W0612
    # pylint: disable=C0103
    global register
    register()
    del register

# Generated at 2022-06-13 20:29:10.331501
# Unit test for function register
def test_register():
    """Open a new interpreter, save the ``__builtin__``
    module, then register the ``b64`` codec and attempt
    to unregister the ``b64`` codec a few times.
    """
    if '__builtin__' in sys.modules:
        builtin_module: Optional[module] = sys.modules['__builtin__']
    else:
        builtin_module = None
    builtins_backup = builtins.__dict__.get('codecs', None)
    builtins.__dict__['codecs'] = codecs
    register()
    if builtin_module:
        sys.modules['__builtin__'] = builtin_module
    builtins.__dict__['codecs'] = builtins_backup



# Generated at 2022-06-13 20:29:21.902544
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # Register the b64 codec with Python.
    register()

    # Verify that the b64 codec can be found by Python.
    try:
        decoder = codecs.getdecoder(NAME)
    except LookupError:
        assert False, (
            'The b64 codec could not be found after registering.'
        )

    # Verify that the b64 codec returns the correct values.
    # pylint: disable=protected-access
    assert decoder[0](b'SGVsbG8gd29ybGQh') == (
        'Hello world!',
        14
    ), (
        'The b64 codec returns the wrong decoding for the string, '
        '"SGVsbG8gd29ybGQh".'
    )


# Generated at 2022-06-13 20:29:29.421243
# Unit test for function register
def test_register():
    """Test function register."""
    register()  # Ignoring the return value.
    try:
        codecs.getencoder(NAME)
    except LookupError:
        raise AssertionError(
            'Register error: '
            'Failed to register the b64 codec.'
        )
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            'Register error: '
            'Failed to register the b64 codec.'
        )
    try:
        codecs.lookup(NAME)
    except LookupError:
        raise AssertionError(
            'Register error: '
            'Failed to register the b64 codec.'
        )


# Generated at 2022-06-13 20:29:31.767353
# Unit test for function register
def test_register():
    """Test that the ``b64`` codec can be registered with Python."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:29:37.411171
# Unit test for function encode
def test_encode():  # pylint: disable=R0914
    """Ensure the `encode` function works as expected."""
    s = u'''\
        TlRMTVNTUAACAAAAAAAAACgAAAABggAAU3J2Tm9uY2UAAAAAAAAAAA==
    '''
    r = base64.b64decode(s)

    assert encode(s) == (r, len(s))

    s = u'''IyEvYmluL3NoCmVjaG8gIkhlbGxvIFdvcmxkISIK'''
    r = base64.b64decode(s)

    assert encode(s) == (r, len(s))


# Generated at 2022-06-13 20:29:48.958632
# Unit test for function register
def test_register():
    # Simulate a fresh Python interpreter.
    try:
        del sys.modules['b64']
    except KeyError:
        pass
    try:
        del sys.modules['b64.codec']
    except KeyError:
        pass
    try:
        del sys.modules[__name__]
    except KeyError:
        pass
    try:
        del sys.modules[__name__.rsplit('.', 1)[0]]
    except KeyError:
        pass

    # Import the 'register()' function.
    from b64 import codec
    import b64
    assert codec.register == b64.codec.register == register

    # Ensure the 'b64' module was imported and that it was imported
    # correctly.

# Generated at 2022-06-13 20:30:07.555725
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:30:18.129352
# Unit test for function encode
def test_encode():
    """test_encode

    Basic testing for the function ``encode``.
    """

# Generated at 2022-06-13 20:30:20.703263
# Unit test for function register
def test_register():
    assert not NAME in codecs._codec_search_cache
    register()
    assert NAME in codecs._codec_search_cache



# Generated at 2022-06-13 20:30:22.706173
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:29.937200
# Unit test for function register
def test_register():
    """Test function register.

    This function is used as a unit test by 'pytest' with the following
    command line:

    ::

        $ pytest -s --cov=pytypedecls --cov=pyb64codecs -vv tests
    """
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Failed to register codec'



# Generated at 2022-06-13 20:30:37.196034
# Unit test for function register
def test_register():
    """Test the function :obj:`b64.register`."""
    # pylint: disable=W0212
    table = codecs.__dict__['_MAGIC_REGISTRY']

    # Make sure the Codec is not registered.
    assert NAME not in table

    # Register the Codec
    register()

    # Test that the Codec was registered.
    table = codecs.__dict__['_MAGIC_REGISTRY']
    assert NAME in table



# Generated at 2022-06-13 20:30:45.508116
# Unit test for function encode

# Generated at 2022-06-13 20:30:49.503214
# Unit test for function register
def test_register():
    """Test function register."""
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:30:59.126617
# Unit test for function register
def test_register():
    from importlib import reload
    import sys

    # Remove the module from sys
    try:
        del sys.modules['b64_codec']
    except KeyError:
        pass

    # Reload the module so that it starts fresh
    b64_codec = reload(sys.modules['_b64_codec'])

    # Try to get the 'b64' codec.
    try:
        codecs.getdecoder('b64')
    except LookupError as e:
        if str(e).strip() == "unknown error: 'b64'":
            raise AssertionError(
                'The codec was not registered.'
            ) from e

    def test_encode(text: _STR, result: _STR) -> None:
        out = b64_codec.encode(text)

# Generated at 2022-06-13 20:31:06.309364
# Unit test for function encode
def test_encode():
    # type: () -> None
    """Unit test for ``encode``"""
    assert encode('TElDQ1BFTUQ=\n') == (b'MIDCAMED', 11)
    assert encode('QUJDREVGRw==\n') == (b'ABCDEFG\x0b', 11)
    assert encode('QUJD\nREVGRw==\n') == (b'ABC\nDEFG\x0b', 12)

# Generated at 2022-06-13 20:31:26.147020
# Unit test for function register
def test_register():
    """Register the codec then unregister it.

    xdoctest lib/b64_codec.py register
    """
    register()
    register()

    # codecs.register(register)
    # codecs.register(register)  # raises LookupError



# Generated at 2022-06-13 20:31:31.814945
# Unit test for function register
def test_register():
    # Clean up the codec registry.
    try:
        codecs.lookup(NAME)
        codecs.unregister(NAME)
    except LookupError:
        pass

    # Verify that the codec is not registered.
    with pytest.raises(LookupError):
        codecs.lookup(NAME)

    # Register the codec.
    register()

    # Verify that the codec is registered.
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:31:38.746779
# Unit test for function encode
def test_encode():
    assert len(encode('eGlhbw==')) == 2
    assert encode('eGlhbw==')[0] == b'\xe7\x94\x9f'
    assert encode('eGlhbw==')[1] == 8
    assert len(encode('YWJjZA==', 'ignore')) == 2
    assert encode('YWJjZA==', 'ignore')[0] == b'abcd'
    assert encode('YWJjZA==', 'ignore')[1] == 8
    assert len(encode('eGlhbw==', 'ignore')) == 2
    assert encode('eGlhbw==', 'ignore')[0] == b'\xe7\x94\x9f'
    assert encode('eGlhbw==', 'ignore')[1]

# Generated at 2022-06-13 20:31:43.083395
# Unit test for function register
def test_register():
    """Test the register function."""
    import sys
    import types

    # Remove the b64 module from the Python path before doing this test.
    for name in list(sys.modules.keys()):
        if name.startswith('b64_codec'):
            del sys.modules[name]

    import b64_codec
    b64_codec.register()
    # Make sure it is on the list of string codecs.
    assert 'b64' in codecs.__dict__['_codec_aliases']['string']
    # Make sure the codec is registered.
    codecs.getencoder(NAME)

    del codecs.__dict__['_codec_aliases']['string']['b64']

    # Make sure it is not already part of the codec search path.

# Generated at 2022-06-13 20:31:48.978458
# Unit test for function register
def test_register():
    """Unit-test for function register."""

    # Verify that the codec is not registered
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register the codec.
    register()

    # Verify that the codec is registered.
    codecs.getdecoder(NAME)

