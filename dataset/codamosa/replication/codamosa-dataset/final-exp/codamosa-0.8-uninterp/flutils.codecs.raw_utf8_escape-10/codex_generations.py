

# Generated at 2022-06-13 20:21:52.110297
# Unit test for function register
def test_register():

    # Test if the unit test module is already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('Module already registered')

    # Register the unit test module.
    register()

    # Test if the unit test module is registered.
    actual = isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)
    expected = True
    assert actual == expected

# Generated at 2022-06-13 20:21:55.209927
# Unit test for function register
def test_register():
    """
    Registration of the 'eprint' codec only happens once.
    """
    # noinspection PyProtectedMember
    before = len(codecs.__all__)
    register()
    # noinspection PyProtectedMember
    after = len(codecs.__all__)
    assert before == after - 1

# Generated at 2022-06-13 20:21:57.846823
# Unit test for function register
def test_register():
    # Test registering the eutf8h codec.
    register()

    # Check that the codec is registered.
    codecs.getdecoder(NAME)

    # Check that attempting to register it again doesn't raise an
    # exception.
    register()


# Generated at 2022-06-13 20:21:59.570916
# Unit test for function register
def test_register():
    """Ensure we can import without issue."""
    register()


# Generated at 2022-06-13 20:22:00.972091
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:22:03.048964
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error(NAME) is not None
    assert codecs.lookup(NAME) is not None

# Generated at 2022-06-13 20:22:05.652624
# Unit test for function register
def test_register():
    # Function register() is not a unittest because this file itself
    # is not a module.
    codecs.register(_get_codec_info)  # type: ignore


# Generated at 2022-06-13 20:22:09.472766
# Unit test for function register
def test_register():
    print(f'testing: register()')
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise LookupError(f'unable to register eutf8h codec')



# Generated at 2022-06-13 20:22:12.547531
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    expected = 'eutf8h'
    actual = codecs.getdecoder('eutf8h')[0].__name__
    assert expected == actual
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:22:14.581582
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:22:19.168142
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:20.672767
# Unit test for function register
def test_register():
    pass



# Generated at 2022-06-13 20:22:28.810773
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(__name__.split('.')[-1])
    except LookupError:
        pass
    else:
        raise Exception(
            'Python module "{}" is already registered'.format(NAME)
        )
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception('Unable to register codec "{}"'.format(NAME))



# Generated at 2022-06-13 20:22:31.164219
# Unit test for function register
def test_register():
    if NAME == 'test_eutf8h':
        return
    register()
    return



# Generated at 2022-06-13 20:22:34.805936
# Unit test for function register
def test_register():
    test_code = 'eutf8h'
    codecs.register(_get_codec_info)   # type: ignore
    codecs.getdecoder(test_code)   # type: ignore

# Generated at 2022-06-13 20:22:38.776943
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False
    # Clean up
    codecs.unregister_error('eutf8h')
    codecs.unregister(NAME)



# Generated at 2022-06-13 20:22:41.117329
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:44.602312
# Unit test for function register
def test_register():
    """Test that :func:`register` registers the codecs.

    """
    codecs.register(_get_codec_info)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:56.072923
# Unit test for function register
def test_register():
    import sys
    import types

    # noinspection PyProtectedMember
    # noinspection PyUnresolvedReferences
    assert NAME not in sys.modules
    assert NAME not in sys.modules[__name__].__dict__
    assert NAME not in sys.modules[__name__].__dict__['__builtins__']

    register()

    # noinspection PyProtectedMember
    # noinspection PyUnresolvedReferences
    assert NAME in sys.modules[__name__].__dict__
    # noinspection PyUnresolvedReferences
    assert NAME in sys.modules[__name__].__dict__['__builtins__']
    # noinspection PyProtectedMember
    assert sys.modules[__name__].__dict__[NAME] is not None

# Generated at 2022-06-13 20:23:02.853318
# Unit test for function register
def test_register():
    """Run example code and verify success.

    Because the encoding is not in the ``codecs`` module by default,
    this test verifies that the ``register`` function adds it to the
    module.

    """
    register()

    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)
    # noinspection PyUnresolvedReferences
    codecs.getencoder(NAME)
    test_string = 'This is a string with a unicode char: ஐ.'
    encoded = encodestring(test_string.encode(NAME))
    decoded = decodestring(encoded)
    decoded = decoded.decode(NAME)

    assert decoded == 'This is a string with a unicode char: ஐ.'



# Generated at 2022-06-13 20:23:07.026521
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    # noinspection PyUnresolvedReferences
    assert codecs.getdecoder(NAME) is decode
    # noinspection PyUnresolvedReferences
    assert codecs.getencoder(NAME) is encode



# Generated at 2022-06-13 20:23:11.149059
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME), 'Failed to register the encoder'
    assert codecs.getdecoder(NAME), 'Failed to register the decoder'


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:23:16.244797
# Unit test for function register
def test_register():
    import sys
    this_module = sys.modules[__name__]
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            f'Codec {this_module} already registered.'
        )
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:23:19.912205
# Unit test for function register
def test_register():
    register()
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    pass

# Generated at 2022-06-13 20:23:32.176966
# Unit test for function register
def test_register():
    """Unit test for the method :meth:`register`."""

    from sys import getdefaultencoding

    # Are any codecs registered?
    assert len(codecs.cache) < 1

    # Register this encoding
    register()

    # Are there codecs now?
    assert len(codecs.cache) >= 1

    # Get the default encoding
    old_default_encoding = getdefaultencoding()

    # for each of the codecs that are now available
    for k in codecs.cache:
        # if the current encoding is not the default encoding,
        # then skip over this codec.
        if k == old_default_encoding:
            continue

        # Set the default encoding to the current encoding.
        codecs.lookup(k).set_default_encoding()

        # try to register the encoding again


# Generated at 2022-06-13 20:23:35.425288
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:23:38.995417
# Unit test for function register
def test_register():

    # Call the function
    assert NAME not in codecs.__all__
    register()
    assert NAME in codecs.__all__


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:40.614331
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:41.422853
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:23:48.130155
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()  # type: ignore
    text = codecs.decode('abc\\xE2\\x80\\x99', NAME)
    assert text == 'abc\xE2\x80\x99'
    data = codecs.encode(text, NAME)
    assert data.decode() == r'abc\\xe2\\x80\\x99'

# Generated at 2022-06-13 20:23:51.475089
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:23:53.180046
# Unit test for function register
def test_register():  # pragma: no cover
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:00.061971
# Unit test for function register
def test_register():
    register()
    encoder = codecs.getencoder(NAME)
    assert encoder is not None
    encoder('abc', 'strict')  # type: ignore

    decoder = codecs.getdecoder(NAME)
    assert decoder is not None
    decoder(b'abc', 'strict')  # type: ignore

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:01.093053
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:11.955096
# Unit test for function register
def test_register():   # pragma: no cover
    register()
    cls = codecs.getdecoder(NAME)
    assert cls is not None
    text = '"abcd\\xE7"'
    data = '"abcd\\\\xE7"'
    data_bytes = data.encode('utf8')
    out_bytes, _ = codecs.escape_encode(data_bytes)
    out_text, _ = codecs.escape_decode(data_bytes)
    assert text == out_text
    assert data == out_bytes.decode('utf8')
    out_bytes, _ = codecs.escape_encode(data_bytes, NAME)
    assert out_bytes != data
    out_bytes, _ = cls.encode(text)
    assert out_bytes != data
    out_text, _ = cls

# Generated at 2022-06-13 20:24:14.690691
# Unit test for function register
def test_register():
    ret = codecs.getdecoder(NAME)
    assert ret == (decode, 0)  # type: ignore

    ret = codecs.getencoder(NAME)
    assert ret == (encode, 0)  # type: ignore



# Generated at 2022-06-13 20:24:15.792102
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getencodings()

# Generated at 2022-06-13 20:24:17.496919
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:20.443218
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False  # Unit test failed.
    assert True  # Unit test succeeded.



# Generated at 2022-06-13 20:24:23.352883
# Unit test for function register
def test_register():
    """Test function :func:`register`."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:30.168357
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)



# Generated at 2022-06-13 20:24:33.642962
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, "Couldn't retrieve codec."
    # TODO: Implement test_register



# Generated at 2022-06-13 20:24:40.572824
# Unit test for function register
def test_register():
    original_getdecoder = codecs.getdecoder

    def _getdecoder(name: str) -> codecs.CodecInfo:
        if name == NAME:
            return codecs.CodecInfo(  # type: ignore
                name=NAME,
                encode=encode,  # type: ignore[arg-type]
                decode=decode,  # type: ignore[arg-type]
            )
        raise LookupError()

    codecs.getdecoder = _getdecoder
    try:
        register()
    finally:
        codecs.getdecoder = original_getdecoder



# Generated at 2022-06-13 20:24:41.722211
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:24:51.666839
# Unit test for function register
def test_register():
    import sys
    import tempfile
    import codecs
    import os

    byte_str_in = b'\x24\xe2\x82\xac\xf0\xa4\xad\xa2'
    test_file = tempfile.NamedTemporaryFile(delete=False)
    test_file.write(byte_str_in)
    test_file.close()

    assert not hasattr(sys.modules['codecs'], NAME)

    register()

    assert hasattr(sys.modules['codecs'], NAME)

    str_out = codecs.decode(byte_str_in, NAME)

    assert str_out == '$€𤭢'


# Generated at 2022-06-13 20:24:55.932757
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    test_register()
    data = b'\\xc3\\xa9'
    text = 'é'
    out = data.decode(NAME)
    assert out == text, f'"{out}"'
    out = text.encode(NAME)
    assert out == data, f'"{out}"'

# Generated at 2022-06-13 20:24:59.748234
# Unit test for function register
def test_register():
    # Test to see if the codec exists.
    got_it = False
    try:
        codecs.getdecoder(NAME)
        got_it = True
    except LookupError:
        assert got_it is False
    # Register the codec.
    register()
    # Test to see if the codec exists.
    got_it = False
    try:
        codecs.getdecoder(NAME)
        got_it = True
    except LookupError:
        assert got_it is False



# Generated at 2022-06-13 20:25:01.897693
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)
    assert codecs.getincrementalencoder(NAME)
    assert codecs.getincrementaldecoder(NAME)

# Unit tests for function encode

# Generated at 2022-06-13 20:25:04.956946
# Unit test for function register
def test_register():
    register()
    out = b'hello'
    expected = b'hello'
    assert codecs.decode(out, NAME) == expected



# Generated at 2022-06-13 20:25:07.164216
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)

if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:25:23.599078
# Unit test for function register
def test_register():
    import codecs
    codecs.register(_get_codec_info)

    assert NAME in {
        codec_name for codec_name, obj in codecs.__dict__.items()  # type: ignore
        if isinstance(obj, codecs.CodecInfo)  # type: ignore
    }


register()

# Generated at 2022-06-13 20:25:27.420187
# Unit test for function register
def test_register():
    # Make sure that the NAME codec is not registered
    assert NAME not in codecs.get_aliases()['decode']

    # Register the NAME codec
    register()

    # Make sure that the NAME codec is registered
    assert NAME in codecs.get_aliases()['decode']

# Generated at 2022-06-13 20:25:30.112219
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:33.535411
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getencodings()


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    import pytest

    pytest.main(['-v', __file__])

# Generated at 2022-06-13 20:25:37.475848
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    assert codecs.getdecoder(NAME) is not None  # type: ignore


# Generated at 2022-06-13 20:25:40.245871
# Unit test for function register
def test_register():
    register()


codecs.register(_get_codec_info)

__all__ = ['encode', 'decode', 'register']

# Generated at 2022-06-13 20:25:46.335213
# Unit test for function register
def test_register():
    import doctest
    from eutf8h import codec_eutf8h
    try:
        codec_eutf8h.register()
        assert doctest.testmod(codec_eutf8h,
                               report=False,
                               optionflags=doctest.ELLIPSIS)
        # print('doctest result: ' + str(result))
        # print('doctest.testmod end')
    except SystemExit as e:
        pass


# Generated at 2022-06-13 20:25:48.255012
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:25:56.009265
# Unit test for function register
def test_register():
    """Test the function register.

    This function just verifies that the codec was not previously
    registered and that the function will properly register it.
    """

    # Unregister the codec, if it was previously registered.
    try:
        codecs.lookup(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)

    # Register the codec.
    register()

    # Check that the function properly registered the codec.
    codecs.lookup(NAME)



# Generated at 2022-06-13 20:25:58.337825
# Unit test for function register
def test_register():
    register()
    print(codecs.decode(b'\\x41\\x42\\x43', NAME))


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:24.442829
# Unit test for function register
def test_register():
    getdecoder = codecs.getdecoder('eutf8h')
    getencoder = codecs.getencoder('eutf8h')
    assert getdecoder == decode and getencoder == encode


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:26.213809
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:26:27.959198
# Unit test for function register
def test_register():
    register()

# Unit test of the functions decode, encode

# Generated at 2022-06-13 20:26:30.421102
# Unit test for function register
def test_register():
    register()
    # codecs.register(_get_codec_info)


# Generated at 2022-06-13 20:26:31.916058
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:26:37.712157
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    # noinspection PyUnresolvedReferences
    assert codecs.lookup(NAME).decode('hello', errors='strict') == 'hello'
    assert codecs.lookup(NAME).encode('hello', errors='strict') == b'hello'
    assert codecs.lookup(NAME).name == NAME
    codecs.unregister(NAME)  # type: ignore



# Generated at 2022-06-13 20:26:38.265533
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:26:44.584631
# Unit test for function register
def test_register():
    # import any_pythonic_function
    # # Import any_pythonic_function.string.eutf8h
    # from any_pythonic_function import string
    # from any_pythonic_function.string import eutf8h

    # Verify that the NAME is assigned to the correct codec name.
    assert NAME == 'eutf8h'

    # Unregister the codec if it is registered
    if NAME in codecs.__dict__:
        del codecs.__dict__[NAME]

    # Test the imported codecs.__dict__
    assert NAME not in codecs.__dict__

    # Test the register function, which adds the NAME to codecs.__dict__
    register()

    # Test the imported codecs.__dict__
    assert NAME in codecs.__dict__


# Generated at 2022-06-13 20:26:47.271556
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__['_cache']
    register()
    assert NAME in codecs.__dict__['_cache']
    del codecs.__dict__['_cache'][NAME]


# Unit test

# Generated at 2022-06-13 20:26:51.375472
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder(NAME) is not None

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:42.795866
# Unit test for function register
def test_register():
    from codecs import lookup  # type: ignore
    register()
    codecs = lookup(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:46.152034
# Unit test for function register
def test_register():
    print(codecs.getdecoder(NAME))
    register()
    print(codecs.getdecoder(NAME))



# Generated at 2022-06-13 20:27:48.198170
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:50.694243
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:27:52.106070
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert obj.name == NAME


# Generated at 2022-06-13 20:27:56.294329
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        print('Error: codecs.getdecoder failed to find the registered codec')


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:57.711979
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:58.858603
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:03.321294
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)[-1] == 'utf-8 hexadecimal'


# Generated at 2022-06-13 20:28:06.777510
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:30:01.936333
# Unit test for function register
def test_register():
    # Try to import a module that uses NAME for encoding
    import io
    import sys

    # If NAME is not registered then an exception should be raised.
    try:
        io.StringIO(text='test', encoding=NAME)
    except LookupError:
        pass
    else:
        raise AssertionError(
            'The NAME, "%s", is registered but should not be.' % NAME
        )
    register()


# Generated at 2022-06-13 20:30:07.657019
# Unit test for function register
def test_register():
    codecs.getdecoder = Mock(side_effect=LookupError)
    codecs.register = Mock()
    try:
        register()
        assert codecs.register.called
    finally:
        del codecs.getdecoder
        del codecs.register


# Generated at 2022-06-13 20:30:09.164047
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:30:10.294919
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:21.207000
# Unit test for function register
def test_register():

    # Convert the string '\x80\x81\x82' into utf8 bytes.
    # This is a simple string, with no utf8 hexadecimal sequences.
    # The bytes are: \xc2\x80\xc2\x81\xc2\x82
    test_str = '\x80\x81\x82'

    # Convert the utf8 bytes into escaped utf8 hexadecimal.
    # This is the expected result. The characters are: \\xc2\\x80\\xc2\\x81\\xc2\\x82
    test_out_str_expected = '\\xc2\\x80\\xc2\\x81\\xc2\\x82'

    test_bytes_utf8 = test_str.encode('utf-8')

# Generated at 2022-06-13 20:30:28.368995
# Unit test for function register
def test_register():
    from test.support import import_fresh_module
    error_registry = import_fresh_module(
        'encodings.utf_8_h',
        fresh=['encodings'],
        blocked=['_codecs', 'codecs']
    )
    error_registry.register()

    import encodings.utf_8_h
    assert encodings.utf_8_h.NAME in encodings.aliases.aliases



# Generated at 2022-06-13 20:30:31.154091
# Unit test for function register
def test_register():
    register()
    # noinspection PyTypeChecker
    codecs.getdecoder(NAME)  # should not throw an exception



# Generated at 2022-06-13 20:30:41.791044
# Unit test for function register
def test_register():
    # Create a temp file to write the test data to.
    tmp_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 20:30:43.389504
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:30:45.584029
# Unit test for function register
def test_register():
    try:
        codec = codecs.getdecoder(NAME)
    except LookupError:
        codec = None
        codecs.register(_get_codec_info)  # type: ignore
    assert codec is not None
