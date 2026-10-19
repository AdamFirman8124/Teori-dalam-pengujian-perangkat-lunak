

# Generated at 2022-06-13 20:21:46.490701
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:21:49.603500
# Unit test for function register
def test_register():
    """Test the :function:`~_codec_b64.register` function."""
    register()
    codecs.getdecoder(NAME)          # type: ignore



# Generated at 2022-06-13 20:21:51.685462
# Unit test for function register
def test_register():
    """Test the register function."""
    assert NAME not in codecs.__all__

    register()

    assert NAME in codecs.__all__



# Generated at 2022-06-13 20:21:55.353306
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # noinspection PyProtectedMember
    for member in (
        'getdecoder',
        'getencoder',
    ):
        assert not hasattr(codecs, member)
    register()
    for member in (
        'getdecoder',
        'getencoder',
    ):
        assert hasattr(codecs, member)
    return


# Generated at 2022-06-13 20:22:06.237007
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    # Get the codec from Python
    codec = codecs.getdecoder(NAME)    # type: ignore

    # Test the encode function.
    assert codecs.encode(
        codecs.encode(
            codecs.encode(b'AZaz09_+/=', 'b64'),
            'b64'
        ),
        'b64'
    ) == b'QVoqMDBfKz0='

    # Test the decode function
    assert codecs.decode(
        codecs.decode(
            codecs.decode(b'QVoqMDBfKz0=', 'b64'),
            'b64'
        ),
        'b64'
    ) == b'AZaz09_+/='

# Generated at 2022-06-13 20:22:06.919345
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:22:16.493330
# Unit test for function register
def test_register():
    """Unit test for function register.

    This function verifies that the codec can be registered with Python.
    """
    # pylint: disable=protected-access
    # noinspection PyUnresolvedReferences
    from b64 import codec as b64_codec

    # Make sure the codec has not been registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register the codec.
    b64_codec.register()

    # Make sure the codec was registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail(f'Codec "{NAME}" was not registered')



# Generated at 2022-06-13 20:22:20.918883
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    try:
        codec = codecs.getdecoder(NAME)  # type: ignore
    except LookupError:
        print(f'\n{NAME!r} is not a valid codec.')
        return
    assert codec



# Generated at 2022-06-13 20:22:29.994459
# Unit test for function register
def test_register():
    # pylint: disable=W0212
    # noinspection PyProtectedMember
    _o = codecs.CodecInfo(  # type: ignore
        name=NAME,
        decode=decode,  # type: ignore[arg-type]
        encode=encode,  # type: ignore[arg-type]
    )
    codecs.register(_get_codec_info)  # type: ignore
    assert _o is codecs.getdecoder(NAME)  # type: ignore



# Generated at 2022-06-13 20:22:33.719502
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
        raise Exception('Expected to fail.')
    except LookupError:
        pass
    register()
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:22:41.613781
# Unit test for function register
def test_register():
    # if typer is not installed, then `code --install-extension typer.typer`
    from typer import run_app, echo, Exit
    import contextlib

    @contextlib.contextmanager
    def codec_registered():
        register()
        try:
            yield
        finally:
            codecs.register(_get_codec_info)

    def test_function():
        try:
            with codec_registered():
                codecs.getdecoder(NAME)
        except Exception:
            raise Exit(1)

    run_app(test_function)
    echo('Codec is registered')



# Generated at 2022-06-13 20:22:43.016290
# Unit test for function register
def test_register():
    _ = register()



# Generated at 2022-06-13 20:22:48.631094
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        assert False, (
            f'Expected the "{NAME}" codec to already be registered.  '
            f'Use this codecs as stand alone module and not as part of '
            f'another module'
        )


register()

# Generated at 2022-06-13 20:22:51.979419
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    import b64codec
    codecs.register(b64codec._get_codec_info)


register()

# Generated at 2022-06-13 20:23:03.277523
# Unit test for function encode
def test_encode():
    # type: () -> None
    """Test the encode function."""
    # encode
    assert encode('QQ==') == (b'A', 3)
    assert encode('QQ=') == (b'A', 3)
    assert encode('QQ') == (b'A', 3)

    assert encode('QUE=') == (b'AU', 4)
    assert encode('QUE') == (b'AU', 4)

    assert encode('QUFB') == (b'AUA', 4)

    assert encode('QUFBQQ==') == (b'AUAA', 6)
    assert encode('QUFBQQ=') == (b'AUAA', 6)
    assert encode('QUFBQQ') == (b'AUAA', 6)

    assert encode('QUFBQUE=') == (b'AUAU', 6)

# Generated at 2022-06-13 20:23:11.377981
# Unit test for function encode
def test_encode():
    assert encode('aGVsbG8gd29ybGQK') == (b'hello world', 16)
    assert encode('aGVsbG8gd29ybGQ=') == (b'hello world', 16)
    assert encode('aGVsbG8gd29ybGQ') == (b'hello world', 16)
    assert encode('aGVsbG8gd29ybGQ\r\n') == (b'hello world', 16)
    assert encode('\naGVsbG8gd29ybGQ\n\n') == (b'hello world', 16)
    try:
        encode('')
        assert False
    except Error:
        assert True

# Generated at 2022-06-13 20:23:16.444533
# Unit test for function register
def test_register():
    """Test for function register."""
    # Delete the registered codec.

# Generated at 2022-06-13 20:23:18.440593
# Unit test for function encode
def test_encode():
    assert encode('dGVzdA==') == (b'test', 6)

# Generated at 2022-06-13 20:23:25.197196
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    # Test that the b64 codec is registered.
    assert 'b64' in codecs.__all__
    # Test the 'b64' is registered as a decoder.
    codecs.getdecoder('b64')
    # Test the 'b64' is registered as a encoder.
    codecs.getencoder('b64')

# Generated at 2022-06-13 20:23:28.250199
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    result = codecs.getdecoder(__name__.split('.')[-1])
    assert result == _get_codec_info(__name__.split('.')[-1])   # type: ignore


# Generated at 2022-06-13 20:23:33.463258
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    import sys

    if sys.version_info[:2] < (3, 0):
        raise NotImplementedError(
            'Test only valid for Python 3.x'
        )
    assert NAME not in codecs.getdecoder(NAME)
    register()
    assert NAME in codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:37.218347
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pytest.fail(f'The codec {NAME!r} failed to register.')

# Generated at 2022-06-13 20:23:49.829871
# Unit test for function register
def test_register():
    """Function, named :func:`~test_register`, is a
    unit test for a module's function named :func:`register`.

    The :func:`~test_register` function is a test function for the
    :func:`register` function.  It is not intended to be called
    directly.  It is called by a test framework to test the
    :func:`register` function.

    In normal use, the :func:`register` function is called when a
    Python program starts execution.  The :func:`register` function
    tells Python that the ``b64`` codec exists.
    """
    # First, unregister the codec.  This makes it possible to test the
    # register function.  Remove this test function if you want to
    # test the register function.
    codecs.unregister_error(NAME)

   

# Generated at 2022-06-13 20:23:52.152633
# Unit test for function register
def test_register():
    """Test whether the codec was registered."""
    register()
    codec = codecs.getdecoder(NAME)
    assert codec is not None


# Generated at 2022-06-13 20:23:57.572123
# Unit test for function encode
def test_encode():
    """ Unit test for function encode
    """
    # Arrange
    expected = b'Hello World!'
    text = '''\
       SGVsbG8gV29ybGQ=
    '''

    # Act
    out, length = encode(text)

    # Assert
    assert expected == out
    assert length == len(text)


# Generated at 2022-06-13 20:24:05.214544
# Unit test for function encode
def test_encode():
    """Test encode function"""
    import random
    import string

    random_string = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(100)
    )
    encoded_bytes, consume_len = encode(random_string)
    assert consume_len == 100
    decoded_string = codecs.decode(encoded_bytes, NAME)
    assert random_string == decoded_string



# Generated at 2022-06-13 20:24:12.802178
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)  # type: ignore

if __name__ == '__main__':
    if __package__ is None and not hasattr(sys, 'frozen'):
        # direct call of __main__.py
        import os.path
        path = os.path.realpath(os.path.abspath(__file__))
        sys.path.insert(0, os.path.dirname(os.path.dirname(path)))
    import pytest    # type: ignore
    pytest.main([__file__])

# Generated at 2022-06-13 20:24:18.401217
# Unit test for function register
def test_register():  # type: ignore
    """
    Test function ``register``.

    This function is only executed if the module is called from the command
    line.  It is not executed if the module is imported.

    This function is hard to test and is only a sanity check.

    :return: None
    """
    import sys
    answer = codecs.getdecoder(NAME)
    print(answer)

if __name__ == '__main__':
    test_register()   # pragma: no cover

# Generated at 2022-06-13 20:24:25.226852
# Unit test for function register
def test_register():
    """Test function :func:`register`."""
    # Test with an unregistered name
    # noinspection PyUnresolvedReferences
    codecs.__all__.pop(NAME, None)
    assert NAME not in codecs.__all__
    register()
    assert NAME in codecs.__all__

    # Test with an already registered name
    register()
    assert NAME in codecs.__all__


# Generated at 2022-06-13 20:24:27.298557
# Unit test for function register
def test_register():
    """Test for function register."""
    B64 = NAME
    codecs.getdecoder(B64)
    codecs.getencoder(B64)

# Generated at 2022-06-13 20:24:39.502950
# Unit test for function register
def test_register():
    """Test the :py:func:`register` function."""
    # Verify the b64 codec is not register by making a call to
    # 'getdecoder'.  This call to getdecoder will raise a LookupError
    # exception if the b64 codec is not register.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # The b64 codec is not register, so call register.
        register()

        # Verify the register function worked by calling 'getdecoder'.
        # The getdecoder function will raise a LookupError exception if
        # the b64 codec was not register.
        codecs.getdecoder(NAME)


# invoke the register function when this module is loaded.
register()

# Generated at 2022-06-13 20:24:46.262620
# Unit test for function register
def test_register():
    """Test function register() from ``b64`` codec."""
    print('TEST: b64.test_register()')
    # The first call to register() will register the 'b64' codec with
    # Python.  Subsequent calls to register() with do nothing.  Regardless,
    # calling register() from the main module will register the 'b64' codec
    # with Python.
    register()



# Generated at 2022-06-13 20:24:50.094588
# Unit test for function encode
def test_encode():
    text_input = '`\n|\n}\n>\n'
    text_bytes = 'YH4KfAo+Cg=='
    out, _ = encode(text_input)
    assert out == text_bytes.encode('utf-8')


# Generated at 2022-06-13 20:24:59.088758
# Unit test for function encode
def test_encode():

    # Test with single line string.
    s = '''
        QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    '''
    text, len_ = encode(s)
    assert text == b'Alice:open sesame'
    assert len_ == len(s)
    assert encode(s) == encode(UserString(s))

    # Test with multi-line string.
    s = '''
        QWxhZGRpbjpvcGVu
        IHNlc2FtZQ==
    '''
    text, len_ = encode(s)
    assert text == b'Alice:open sesame'
    assert len_ == len(s)

    # Test with extra whitespace.

# Generated at 2022-06-13 20:25:03.114756
# Unit test for function register
def test_register():
    """Tests the function register."""
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:12.534394
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    codec_info = codecs.CodecInfo(  # type: ignore
        name=NAME,
        decode=decode,  # type: ignore[arg-type]
        encode=encode,  # type: ignore[arg-type]
    )
    codecs.register(lambda x: codec_info if x == NAME else None)
    assert codecs.getdecoder(NAME) == codec_info.decode
    assert codecs.getencoder(NAME) == codec_info.encode
    assert codecs.getdecoder(NAME + '_') is None
    assert codecs.getencoder(NAME + '_') is None



# Generated at 2022-06-13 20:25:24.259996
# Unit test for function encode
def test_encode():
    """Test that the 'encode' function is able to convert multi-line
    base64 content into bytes."""

# Generated at 2022-06-13 20:25:35.008550
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # pylint: disable=W0612
    # pylint: disable=W0212
    register()
    from . import b64
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

    data_bytes = b'\xe4\xb8\xad\xe6\x96\x87'
    encoded_str = '5Lit'

    encoded_bytes, _ = codecs.getencoder(NAME)(data_bytes)
    encoded_str_conv = encoded_bytes.decode('utf-8')
    assert encoded_str_conv == encoded_str

    decode_bytes, _ = codecs.getdecoder(NAME)(encoded_str_conv)
    assert decode_bytes == data_bytes

    # Call codecs.getencoder

# Generated at 2022-06-13 20:25:46.294625
# Unit test for function register
def test_register():
    import sys
    from binascii import Error
    from pprint import pformat
    from textwrap import dedent

    from function import register

    def test_register(err: _STR = 'strict') -> _STR:
        try:
            register()
        except Exception as e:
            out = str(e)
        else:
            out = ''
        return out

    def test_decode_error(
            text: _STR,
            err: _STR = 'strict'
    ) -> _STR:
        try:
            _ = codecs.decode(text, NAME, err)
        except Error as e:
            out = str(e)
        else:
            out = ''
        return out


# Generated at 2022-06-13 20:25:57.476367
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.register(_get_codec_info)
    except TypeError:
        pass
    encode, decode, reader, writer, incrementaldecoder, increment_encode = \
        codecs.lookup(NAME)

    assert encode(
        'AQIDBAU='
    ) == (b'\x01\x02\x03\x04\x05', 8)

    assert decode(b'\x01\x02\x03\x04\x05') == ('AQIDBAQ=', 6)

    assert decode(
        b'\x00\x01\x02\x03\x04\x05',
    ) == ('AAECAwQF', 6)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:11.402521
# Unit test for function register
def test_register():
    from typing import NoReturn

    def is_registered() -> bool:
        codecs.getdecoder(NAME)
        return True

    if is_registered():
        return None

    try:
        register()
    except Exception as e:
        raise AssertionError(
            'Failed to register the b64 codec with Python.'
        ) from e
    else:
        assert is_registered()


if __name__ == '__main__':
    import sys
    test_register()
    sys.exit(0)

# Generated at 2022-06-13 20:26:15.299079
# Unit test for function register
def test_register():
    # Test that the function 'register' will actually register the
    # 'b64' codec with Python.
    codecs.register(_get_codec_info)
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:26:24.860527
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # Call function register.
    register()

    # Get encoder function
    encoder = codecs.getencoder(NAME)

    # Test the encoder function
    assert encoder(b'abcdefghijklmnop') == (
        'YWJjZGVmZ2hpamtsbW5vcA==', len(b'abcdefghijklmnop')
    )

    # Get decoder function
    decoder = codecs.getdecoder(NAME)

    # Test the decoder function
    assert decoder('YWJjZGVmZ2hpamtsbW5vcA==') == (
        b'abcdefghijklmnop', len('YWJjZGVmZ2hpamtsbW5vcA==')
    )

    # Get

# Generated at 2022-06-13 20:26:33.235357
# Unit test for function register
def test_register():
    """Validate the registration of the `b64` codec."""
    codecs.register(_get_codec_info)
    res = codecs.getdecoder(NAME)
    assert res.decode == decode     # type: ignore
    assert res.encode == encode     # type: ignore
    codecs.register(_get_codec_info)
    second_res = codecs.getdecoder(NAME)
    assert second_res is None


# Generated at 2022-06-13 20:26:39.291753
# Unit test for function register
def test_register():
    """Unit test for function register"""
    # Get the registered codecs.
    registered_codecs = codecs._get_codec_search_path()  # type: ignore
    registered_codecs += codecs._get_aliases()  # type: ignore

    # The 'b64' codec MUST NOT be in the list of registered codecs
    assert NAME not in registered_codecs

    register()

    # The 'b64' codec MUST be in the list of registered codecs
    assert NAME in registered_codecs

test_register()

# Generated at 2022-06-13 20:26:44.877595
# Unit test for function register
def test_register():
    """Test function: register()"""
    codecs.unregister(NAME)
    register()
    text = 'AQIDBA=='
    buf = bytes(range(5))
    decoded_tpl = codecs.decode(text, NAME)
    assert buf == decoded_tpl[0]
    encoded = codecs.encode(buf, NAME)
    assert text == encoded.decode('utf-8')

# Generated at 2022-06-13 20:26:52.627267
# Unit test for function register
def test_register():
    """Unit test for function register"""

# Generated at 2022-06-13 20:27:00.638163
# Unit test for function register
def test_register():
    """Test function register."""
    # pylint: disable=W0612
    # noinspection PyUnresolvedReferences
    from .test_helper import TestHelper

    from .common import NAME

    try:
        TestHelper.pytest_set_test_environment()
        TestHelper.register_codec_test(NAME=NAME, CODEC=__name__)
    finally:
        TestHelper.pytest_unregister_codec_test(NAME=NAME)

# Generated at 2022-06-13 20:27:11.681761
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # Un-register the b64 codec if it exists.
    try:
        codecs.lookup(NAME)  # This will raise LookupError if not registered.
        codecs.unregister(NAME)
    except LookupError:
        pass
    else:
        assert False, 'The b64 codec should not be registered.'

    # Ensure the b64 is not registered.
    try:
        codecs.lookup(NAME)
    except LookupError:
        pass
    else:
        assert False, 'The b64 codec should not be registered.'

    # Register the b64 codec and ensure is is registered.
    register()
    try:
        codecs.lookup(NAME)
    except LookupError:
        assert False, 'The b64 codec should be registered.'

# Generated at 2022-06-13 20:27:12.984879
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:27.265378
# Unit test for function encode
def test_encode():
    """Test the ``encode`` function."""
    assert encode(
        """
        YQ==
        """.strip()
    ) == (
        b'a',
        13
    )
    assert encode(
        """
        YWI=
        """.strip()
    ) == (
        b'ab',
        13
    )
    assert encode(
        """
        YWJj
        """.strip()
    ) == (
        b'abc',
        10
    )
    assert encode(
        """
        YWJjZA==
        """.strip()
    ) == (
        b'abcd',
        15
    )

# Generated at 2022-06-13 20:27:30.781000
# Unit test for function register
def test_register():
    register()
    codec_info = codecs.getdecoder(NAME)
    assert codec_info is not None


# Generated at 2022-06-13 20:27:32.369119
# Unit test for function encode
def test_encode():
    """Unit test for function :func:`encode`."""
    pass



# Generated at 2022-06-13 20:27:35.514726
# Unit test for function register
def test_register():
    """Test the function register"""
    register()
    assert codecs.getencoder(NAME)


# Generated at 2022-06-13 20:27:50.316589
# Unit test for function register
def test_register():
    """Test that register registers the codec as expected."""
    # unregister the codec if it is already registered
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister_error(NAME)
        try:
            codecs.lookup_error(NAME)
        except LookupError:
            pass
        else:
            raise ValueError(
                f'Failed to unregister {NAME} codec.'
            )

    # Register the codec.
    register()

    # Get the codec.
    codec = codecs.lookup_error(NAME)

    # Verify that the codec is what we expect.
    if codec.name != NAME:
        raise ValueError("'b64' codec not registered as 'b64'")

# Generated at 2022-06-13 20:27:53.404929
# Unit test for function register
def test_register():
    register()
    import _testcapi
    # pylint: disable=no-member
    assert _testcapi.codec_lookup(NAME) == _get_codec_info(NAME)



# Generated at 2022-06-13 20:27:58.111483
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert obj.encode('hi') == b'aGk='
    assert obj.decode(b'aGk=') == 'hi'


# Generated at 2022-06-13 20:28:09.757875
# Unit test for function register
def test_register():
    import sys
    import pytest
    # Make sure that 'b64' is NOT yet registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
    assert NAME not in sys.modules

    # Register the 'b64' codec.
    register()
    obj: codecs.CodecInfo
    obj = codecs.getdecoder(NAME)  # type: ignore
    assert obj.name == NAME
    assert obj.decode == decode     # type: ignore[attr-defined]
    assert obj.encode == encode     # type: ignore[attr-defined]

# Generated at 2022-06-13 20:28:14.548488
# Unit test for function register
def test_register():
    """Test the function ``register`` with the Python ``codecs`` module."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError()

    register()

    # pylint: disable=W0612
    # noinspection PyUnusedLocal
    decoder = codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:25.390464
# Unit test for function register
def test_register():
    """Insure that :func:`register` functions as expected."""
    # Test 1:
    #        Test that the 'b64' codec is not register in the standard
    #        codecs.  To do this, try to use the  'b64' codec
    #        and catch the LookupError exception.
    try:
        codecs.getdecoder('b64')
    except LookupError:
        pass
    else:
        raise AssertionError(
            "The 'b64' codec was already registered in the standard codecs"
        )

    # Test 2:
    #        Register the 'b64' codec.
    register()

    # Test 3:
    #        Test that the 'b64' codec is now registered and that the
    #        'encode' and 'decode' functions are correct.

# Generated at 2022-06-13 20:28:55.421126
# Unit test for function register
def test_register():
    """Test the :obj:`~.register` function."""
    encode_func = codecs.getencoder(NAME)
    assert encode_func is encode
    decode_func = codecs.getdecoder(NAME)
    assert decode_func is decode
# pylint: enable=W0613

# Generated at 2022-06-13 20:28:58.101827
# Unit test for function register
def test_register():
    """Unit test for function register"""
    codecs.lookup_error('b64')


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:28:59.339689
# Unit test for function register
def test_register():
    """Test the register function."""
    register()



# Generated at 2022-06-13 20:29:08.319620
# Unit test for function encode
def test_encode():
    assert encode('') == (b'', 0)
    assert encode('A') == (b'A', 1)
    assert encode('AA') == (b'A', 1)
    assert encode('AAA') == (b'A', 1)
    assert encode('AAAA') == (b'AAAA', 4)
    assert encode('AAAAA') == (b'A', 1)
    assert encode('AAAAAA') == (b'AAA', 3)
    assert encode('TsMB') == (b'TsMB', 4)
    assert encode('TsMB\n') == (b'TsMB', 4)
    assert encode('TsMB\n\n') == (b'TsMB', 4)
    assert encode(' TsMB') == (b'TsMB', 4)
    assert encode(' TsMB ') == (b'TsMB', 4)
   

# Generated at 2022-06-13 20:29:18.509270
# Unit test for function register
def test_register():
    """Test the function register."""
    import sys

    # make sure that NAME is not already in the list of codecs.
    assert sys.getdefaultencoding() != NAME
    assert NAME not in sys.modules['encodings'].aliases.aliases

    # Register the b64 codec.
    register()

    # Assert that the NAME was registered with Python.
    assert NAME in sys.modules['encodings'].aliases.aliases

    # Test the codecs attribute.
    assert sys.getdefaultencoding() != NAME
    assert NAME not in sys.modules['encodings'].aliases.aliases


# Test the encoding of the codec.

# Generated at 2022-06-13 20:29:28.027853
# Unit test for function register
def test_register():
    """Unit test for function register."""
    import codecs
    from unittest import TestCase, mock

    class MockCodec(TestCase):
        """Test case class for the codecs.CodecInfo object."""

        def __init__(self, *argv, **kwargs):
            """Initialize a test object."""
            super().__init__(*argv, **kwargs)
            self.name = NAME

    class TestRegister(TestCase):
        """Unit test for the register function."""

        def test_get_decoder_exc(self):
            """Test that an exception is raised when the codec
            is not registered."""
            with self.assertRaises(Exception):
                codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:29:31.301105
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    codecs.register(lambda x: None)
    assert NAME not in codecs.getencoders()
    codecs.unregister(NAME)
    assert NAME not in codecs.getencoders()
    register()
    assert NAME in codecs.getencoders()
    codecs.unregister(NAME)
    assert NAME not in codecs.getencoders()



# Generated at 2022-06-13 20:29:34.363540
# Unit test for function register
def test_register():
    """Unit test for function register()."""
    # Register the codec b64.
    register()

    # Get the codec b64.
    codecs.getdecoder(NAME)

    # Get the codec b64.
    # noinspection PyUnusedLocal
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:29:36.042643
# Unit test for function register
def test_register():
    assert 'b64' not in codecs.__dict__['lookup_table']
    register()
    assert 'b64' in codecs.__dict__['lookup_table']
    register()

# Generated at 2022-06-13 20:29:45.837806
# Unit test for function register
def test_register():
    # pylint: disable=W0612
    # noinspection PyUnresolvedReferences
    from codecs import encode

    register()
    data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    data_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    encoded = encode(data_str, 'b64')
    assert encoded == data



# Generated at 2022-06-13 20:30:46.375507
# Unit test for function register
def test_register():
    """Ensure function register() correctly registers itself with Python"""
    from unittest.mock import patch

    # Patch the 'codecs.register()' function
    with patch('codecs.register', create=True) as mock_register:
        # Call the register function under test.
        register()

        # Assert the 'mock_register' method was called.
        mock_register.assert_called_with(_get_codec_info)



# Generated at 2022-06-13 20:30:49.931410
# Unit test for function encode
def test_encode():
    """This is a example unit test for function ``encode``.
    """
    assert encode('') == (b"", 0)



# Generated at 2022-06-13 20:30:54.473392
# Unit test for function register
def test_register():
    """Example usage of the :func:`register` function.
    """
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

if sys.version_info < (3, 8):
    register()

# Generated at 2022-06-13 20:31:00.935359
# Unit test for function encode
def test_encode():
    """Unit test function: b64.encode()"""
    assert encode('') == (b'', 0)
    with pytest.raises(UnicodeEncodeError):
        encode('x')
    assert encode('YQ==') == (b'a', 12)
    assert encode('YWI=') == (b'ab', 12)
    assert encode('YWJj') == (b'abc', 12)
    assert encode('YWJjZA==') == (b'abcd', 12)
    assert encode('YWJjZGU=') == (b'abcde', 12)
    assert encode('YWJjZGVm') == (b'abcdef', 12)
    assert encode('YWJjZGVmZw==') == (b'abcdefg', 12)

# Generated at 2022-06-13 20:31:02.591404
# Unit test for function register
def test_register():
    """Unit tests for function register."""
    register()
    try:
        codecs.getdecoder(NAME)     # type: ignore
    except LookupError as e:
        raise Exception(f'{NAME} was not properly register: {e}') from e


# Generated at 2022-06-13 20:31:05.351074
# Unit test for function register
def test_register():
    import sys
    register()
    assert NAME in sys.modules
    assert sys.modules[NAME] == sys.modules[__name__]

# Generated at 2022-06-13 20:31:15.413354
# Unit test for function register
def test_register():
    # Ensure base64 is not already register
    try:
        codecs.getdecoder(NAME)
        raise Exception(
            f'Expected LookupError to be thrown when trying to get'
            f'the decoder for {NAME!r}'
        )
    except LookupError:
        pass
    register()
    # Ensure base64 is now register
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception(
            f'Failed to register the {NAME!r} decoder'
        )
    try:
        codecs.getencoder(NAME)
    except LookupError:
        raise Exception(
            f'Failed to register the {NAME!r} encoder'
        )



# Generated at 2022-06-13 20:31:18.738729
# Unit test for function register
def test_register():
    """Verify that the ``b64`` codec actually is registered with Python."""
    import b64
    b64.register()
    assert codecs.getdecoder('b64') is not None  # type: ignore



# Generated at 2022-06-13 20:31:31.050105
# Unit test for function register
def test_register():
    """Unit test for module register"""
    register()

    try:
        codecs.getencoder(NAME)
    except LookupError:
        raise AssertionError(
            'Codec not registered: codecs.getencoder("b64")'
        )
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            'Codec not registered: codecs.getdecoder(NAME)'
        )
    assert codecs.encode(b'foo', NAME) == b'Zm9v'
    assert codecs.decode(b'Zm9v', NAME) == 'foo'
    assert codecs.encode(b'foo\nbar', NAME) == b'Zm9vCmJhcg=='
    assert codecs.dec

# Generated at 2022-06-13 20:31:34.742949
# Unit test for function register
def test_register():
    """Run unit test against ``b64`` module."""
    import doctest  # type: ignore
    doctest.testmod(verbose=False)


if __name__ == '__main__':
    test_register()