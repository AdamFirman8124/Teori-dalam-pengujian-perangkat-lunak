

# Generated at 2022-06-13 20:21:47.032868
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:21:48.993134
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('eutf8h')
    assert codecs.lookup(NAME)

# Generated at 2022-06-13 20:21:54.369579
# Unit test for function register
def test_register():

    codecs.register(_get_codec_info)
    assert codecs.lookup_error('eutf8h') is UnicodeEncodeError
    assert codecs.lookup_error('eutf8h') is UnicodeDecodeError
    try:
        codecs.lookup_error('eutf8h')
    except LookupError:
        pass
    else:
        raise AssertionError('This should not happen')



# Generated at 2022-06-13 20:22:06.114632
# Unit test for function register
def test_register():
    register()
    byte_str = b'\xe2\x82\xac\xed\xa0\xbc\xed\xb5\x8c\xed\xa0\xbc\xf0\x9f\x90\xb8'
    encoded_str, read_chars = codecs.getencoder(NAME)(byte_str)
    # utf8_byte_str = b'\\xe2\\x82\\xac\\xed\\xa0\\xbc\\xed\\xb5\\x8c\\xed\\xa0\\xbc\\xf0\\x9f\\x90\\xb8'
    # assert utf8_byte_str == encoded_str

# Generated at 2022-06-13 20:22:07.573121
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.lookup(NAME).name

# Generated at 2022-06-13 20:22:10.519413
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)  # type: ignore[func-returns-value]

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:11.957821
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME).name == NAME



# Generated at 2022-06-13 20:22:13.783772
# Unit test for function register
def test_register():
    register()

    # Ensure the register function actually registers the codec.
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:22:16.298141
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:22.916516
# Unit test for function register
def test_register():
    from sys import version_info
    if version_info[0] >= 3:
        from typing import Any
        from sys import modules

        if 'codecs' in modules:
            codec_info = codecs.getdecoder(NAME)  # type: Optional[Any]
            assert codec_info is not None
            # assert codec_info.name == NAME
            assert codec_info.encode == encode    # type: ignore[arg-type]
            assert codec_info.decode == decode    # type: ignore[arg-type]


# Generated at 2022-06-13 20:22:30.571071
# Unit test for function register
def test_register():
    """Coverage test.
    """
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:22:34.779551
# Unit test for function register
def test_register():
    NAME_VAL = __name__.split('.')[-1]
    codecs.register(_get_codec_info)

    codecs.lookup_error('strict')

    assert codecs.lookup(NAME_VAL).name == NAME_VAL


test_register()

# Generated at 2022-06-13 20:22:36.303214
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:39.770172
# Unit test for function register
def test_register():
    try:
        register()
    except LookupError:
        assert True
    assert NAME == codecs.getdecoder(NAME)[0]


# Generated at 2022-06-13 20:22:42.059903
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder('eutf8h')

test_register()

# Generated at 2022-06-13 20:22:43.940197
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:47.618685
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:22:50.035337
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)

# Generated at 2022-06-13 20:22:52.018532
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:55.441105
# Unit test for function register
def test_register():
    with pytest.raises(LookupError):
        _ = codecs.getdecoder(NAME)
    register()
    _ = codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:00.020496
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:23:04.001781
# Unit test for function register
def test_register():
    # Check that the eutf8h codec has been registered
    assert(codecs.lookup(NAME) is not None)



# Generated at 2022-06-13 20:23:12.239310
# Unit test for function register
def test_register():
    """
    Test the function register for module eutf8h.
    """
    register()
    try:
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)
        print('Register function for module eutf8h works correctly.')
    except LookupError:
        print('Register function for module eutf8h does NOT work correctly.')

# Generated at 2022-06-13 20:23:19.417078
# Unit test for function register
def test_register():
    from . import codecs_register, codecs_unregister
    codecs_unregister.unregister('eutf8h')
    test_passed = False
    try:
        codecs.getdecoder('eutf8h')
    except LookupError:
        test_passed = True
    assert test_passed
    codecs_register.register()
    codecs.getdecoder('eutf8h')
    test_passed = False
    try:
        codecs.getdecoder('eutf8h')
    except LookupError:
        test_passed = True
    assert not test_passed


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:21.918876
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        register()



# Generated at 2022-06-13 20:23:30.720281
# Unit test for function register
def test_register():
    import codecs  # type: ignore
    import sys

    sys.modules[__name__] = None

    try:
        from eutf8h import codec
    except ImportError:
        from . import codec

    try:
        sys.modules[__name__] = codec
        codec.register()
        codecs.getencoder(codec.NAME)  # type: ignore
        codecs.getdecoder(codec.NAME)  # type: ignore
    except LookupError:
        raise
    finally:
        sys.modules[__name__] = None

# Generated at 2022-06-13 20:23:33.489246
# Unit test for function register
def test_register():
    """Unit test for function register()"""
    # noinspection PyBroadException
    try:
        register()
    except Exception as e:
        assert False, f'Unexpected exception of type {e.__class__.__name__}'
    else:
        assert True



# Generated at 2022-06-13 20:23:37.220075
# Unit test for function register
def test_register():
    register()
    # Check to see if codec has been registered by checking getdecoder
    assert NAME in {i.name for i in codecs.getdecoder(NAME)}



# Generated at 2022-06-13 20:23:39.901792
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:42.492197
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:23:49.891163
# Unit test for function register
def test_register():
    register()
    import codecs
    codecs.getdecoder(NAME)

register()

# Generated at 2022-06-13 20:23:51.886400
# Unit test for function register
def test_register():
    if not pkgutil.find_loader(NAME):
        test_register.__globals__[NAME] = importlib.import_module(NAME)

# Generated at 2022-06-13 20:23:53.258252
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:24:05.215589
# Unit test for function register
def test_register():

    _get_decoder = codecs.getdecoder(NAME)
    out = _get_decoder(b'\\x48\\x65\\x6c\\x6c\\x6f')  # b'Hello'
    assert out[0] == 'Hello'
    assert out[1] == len(b'\\x48\\x65\\x6c\\x6c\\x6f')

    _get_encoder = codecs.getencoder(NAME)
    out = _get_encoder('Hello')
    assert out[0] == b'\\x48\\x65\\x6c\\x6c\\x6f'
    assert out[1] == len('Hello')


if __name__ == '__main__':
    import doctest

# Generated at 2022-06-13 20:24:10.268628
# Unit test for function register
def test_register():
    """Test the register function."""
    # unregister the codec first
    try:
        codecs.unregister(NAME)
    except LookupError:
        pass
    # get the codec
    codecs.getencoder(NAME)
    # unregister the codec again
    codecs.unregister(NAME)



# Generated at 2022-06-13 20:24:10.983296
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:11.519010
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:12.605852
# Unit test for function register
def test_register():

    # Should not raise an exception
    register()



# Generated at 2022-06-13 20:24:14.336695
# Unit test for function register
def test_register():
    import sys
    if sys.version_info.minor >= 6:
        register()
        codecs.getencoder(NAME)

# Generated at 2022-06-13 20:24:15.742652
# Unit test for function register
def test_register():
    NAME = 'eutf8h'
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:27.792259
# Unit test for function register
def test_register():
    register()
    str(b'abc'.decode(NAME))



# Generated at 2022-06-13 20:24:29.585981
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None


# Generated at 2022-06-13 20:24:33.399987
# Unit test for function register
def test_register():
    """Test that the escaped utf8 hexadecimal codec is properly registered
    with the codecs module.
    """
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:34.857564
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:42.402451
# Unit test for function register
def test_register():
    # Run Codecs Registry Methods
    register()
    # Call the codec register method to register the escape utf8 hexadecimal
    # codec.

    # Convert a string into escaped utf8 hexadecimal bytes.
    input_str = 'This is a 字符串.'  # "This is a 字符串."
    input_bytes = input_str.encode(NAME, 'strict')
    assert input_bytes == (
        'This is a \\xe5\\xad\\x97\\xe7\\xac\\xa6\\xe4\\xb8\\xb2.'
        .encode('utf-8')
    )
    # Convert escaped utf8 hexadecimal bytes into a string.
    output_str = input_bytes.decode(NAME, 'strict')

# Generated at 2022-06-13 20:24:51.997225
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    import sys

    test_codecs = sys.modules['codecs']

    def _get_codecs_getdecoder(name: str):
        return test_codecs.getdecoder(name)

    _getdecoder = test_codecs.getdecoder
    test_codecs.getdecoder = _get_codecs_getdecoder

    def _get_codecs_register(codec: codecs.CodecInfo):
        return test_codecs.register(codec)
    _register = test_codecs.register
    test_codecs.register = _get_codecs_register

    with pytest.raises(LookupError):
        _getdecoder(NAME)
    register()
    _

# Generated at 2022-06-13 20:24:52.998301
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:58.606818
# Unit test for function register
def test_register():
    import pytest
    from eutf8h import __name__ as modname
    from eutf8h import NAME as codename

    with pytest.raises(LookupError):
        codecs.getdecoder(codename)

    register()

    codec_info = codecs.getdecoder(codename)
    import types
    assert isinstance(codec_info, types.MethodType)

    assert codec_info.__module__ == modname
    assert codec_info.__name__ == '_get_codec_info'



# Generated at 2022-06-13 20:25:03.777284
# Unit test for function register
def test_register():
    register()
    codecs.decode(r'\x41', NAME)  # noqa: WPS420, E501, WPS601
    codecs.encode(r'A', NAME)  # noqa: WPS420, E501, WPS601

# Generated at 2022-06-13 20:25:06.567698
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:30.059344
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:25:31.613000
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:25:32.560374
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:25:34.059247
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:25:40.306810
# Unit test for function register
def test_register():
    #
    # Create a mock codecs registry
    #
    codecs_registry_original = codecs.__dict__.get("_cache")
    codecs_register_original = codecs.__dict__.get("register")

    class FakeCodec:

        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return self.name == other.name

    def fake_get_decoder(name):
        if name == 'fake':
            raise LookupError()
        if name == 'fake2':
            return FakeCodec(name)
        raise LookupError('Invalid codec name:  %s' % name)

    def fake_get_encoder(name):
        if name == 'fake':
            raise LookupError()

# Generated at 2022-06-13 20:25:51.548196
# Unit test for function register
def test_register():
    register()
    utf8h = codecs.getencoder(NAME)
    utf8hh = codecs.getdecoder(NAME)
    data = 'Děkuji předem za pomoc.'
    utf8_bytes = data.encode('utf-8')
    # Convert to escaped utf8 hexadecimal bytes.
    out_bytes, x = utf8h(data)
    out_bytes = utf8_bytes + out_bytes
    assert out_bytes == b'D\xe4kuji p\xa5edem za pomoc.D\\xe4kuji p\\xa5edem za pomoc.'
    # Convert back to utf-8 bytes.
    out_str, x = utf8h(out_bytes)

# Generated at 2022-06-13 20:25:53.344683
# Unit test for function register
def test_register():
    """Test function register."""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:02.447250
# Unit test for function register
def test_register():
    # Save the current codec; This is needed to avoid interfering with other
    # tests.
    saved_get_codec = codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:26:09.826949
# Unit test for function register
def test_register():
    # make sure that 'eutf8h' codec is not registered.
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register the 'eutf8h' codec.
    register()

    # Now that the codec is registered, the codecs.getdecoder()
    # should work.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:14.478072
# Unit test for function register
def test_register():
    actual = codecs.getdecoder(NAME)
    assert actual  # tests if the NAME is registered
    expected = _get_codec_info(NAME)
    assert actual is expected  # tests if the NAME is registered


# Generated at 2022-06-13 20:27:01.797074
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:04.000161
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info) # type: ignore
    assert codecs.lookup(NAME)

# Generated at 2022-06-13 20:27:05.836132
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is encode
    assert codecs.getdecoder(NAME) is decode



# Generated at 2022-06-13 20:27:07.380217
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:11.432329
# Unit test for function register
def test_register():
    assert codecs.lookup_error('eutf8h')
    assert codecs.lookup_error('eutf8h') is codecs.lookup_error('eutf8hex')
    # assert codecs.lookup_error('eutf8h') is codecs.lookup_error('eutf8hex')

# Generated at 2022-06-13 20:27:13.813999
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None   # type: ignore
    assert codecs.getencoder(NAME) is not None   # type: ignore



# Generated at 2022-06-13 20:27:22.081240
# Unit test for function register
def test_register():

    codecs.register(_get_codec_info)

    def _test_register_codecinfo() -> None:
        # Test registering the codecinfo
        codecs.getdecoder(NAME)

    # Test exception
    try:
        codecs.register(_get_codec_info)
    except AssertionError:
        _test_register_codecinfo()
    else:
        raise AssertionError('AssertionError not raised.')
    # Test registering the codecinfo


# Generated at 2022-06-13 20:27:25.898820
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False


if __name__ == '__main__':
    raise(NotImplementedError('Run tests with `python setup.py test`.'))

# Generated at 2022-06-13 20:27:31.357845
# Unit test for function register
def test_register():
    register()
    try:
        codecs.lookup(NAME)  # type: ignore
    except LookupError:
        raise AssertionError(
            "codecs.lookup(%s) raised LookupError" % repr(NAME)
        )



# Generated at 2022-06-13 20:27:32.634478
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__



# Generated at 2022-06-13 20:29:16.707976
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:29:20.515165
# Unit test for function register
def test_register():
    """Test the function :py:func:`.register`.
    """
    register()
    obj = codecs.getdecoder(NAME)
    assert obj is not None


# Generated at 2022-06-13 20:29:21.900784
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:23.580591
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)

# Unit Test for function get_codec_info

# Generated at 2022-06-13 20:29:25.237860
# Unit test for function register
def test_register():
    # This test is not strictly needed, but it's good to check that the
    # registration process works.
    register()



# Generated at 2022-06-13 20:29:27.245515
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:29.249191
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:29:32.265761
# Unit test for function register
def test_register():
    # Try to register the codec.
    register()

    # Check if the codec exists.
    codec = codecs.getdecoder(NAME)    # type: ignore
    assert codec is not None



# Generated at 2022-06-13 20:29:36.438099
# Unit test for function register
def test_register():
    """Test the function register."""

    # NOTE: The function decode is already registered when the library
    #       is loaded.  So, the 'LookupError' is not raised.
    register()


# Run unit test
if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:29:48.709334
# Unit test for function register
def test_register():
    from hypothesis import assume, given, strategies as st
    import sys
    import os
    import tempfile

    @given(
        s = st.text(),
        e = st.text(),
    )
    def test_encode(
            s,
            e
    ):
        assume(e != 'surrogateescape')
        enc, _ = encode(s, e)
        assert enc != b''

    @given(
        s = st.binary(),
        e = st.text(),
    )
    def test_decode(
            s: bytes,
            e: str
    ):
        assume(e != 'surrogateescape')
        try:
            _, _ = decode(s, e)
        except UnicodeDecodeError:
            pass

    # Test encodings
    # Test memoryview object