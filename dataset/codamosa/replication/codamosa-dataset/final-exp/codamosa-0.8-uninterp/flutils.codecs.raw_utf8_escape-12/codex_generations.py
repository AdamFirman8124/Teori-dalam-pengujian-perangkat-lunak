

# Generated at 2022-06-13 20:21:50.982595
# Unit test for function register
def test_register():

    # Register the codec if it is not registered.
    register()

    # Get the codec info for the eutf8h codec.
    try:
        codec_info = codecs.getdecoder(NAME)
    except LookupError:
        msg = 'Unable to get codec info for the eutf8h codec'
        raise LookupError(msg) from None

    # Get the codec decode function.
    decode = codec_info.decode

    # Define the eutf8h escape bytes for the character 'A'.
    eutf8h_escape_bytes = b'\\x41'

    # Convert the eutf8h escape bytes into a string.
    text = decode(eutf8h_escape_bytes)[0]

    # Verify the string is the character 'A'.
    assert text == 'A'



# Generated at 2022-06-13 20:21:54.606705
# Unit test for function register
def test_register():
    del codecs.decode._codec_search_path[:]
    del codecs.decode._codec_search_cache

    register()
    actual = codecs.getdecoder(NAME)
    assert actual == decode
    assert NAME in codecs.decode._codec_search_path

# Generated at 2022-06-13 20:22:06.153287
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Run unit tests if this module is run directly.
if __name__ == '__main__':
    import unittest

    class TestUTF8Hex(unittest.TestCase):

        def test_encode(self):
            text_str = "This is a test."
            text_bytes_utf8 = text_str.encode('utf-8')
            text_bytes_utf8 = cast(bytes, text_bytes_utf8)
            out_bytes, len_text = encode(text_str)
            self.assertEqual(out_bytes, text_bytes_utf8)
            self.assertEqual(len_text, len(text_str))

            text_str = "This is a test.\u2713"
            text_bytes_utf

# Generated at 2022-06-13 20:22:07.228769
# Unit test for function register
def test_register():
    register()                                                 # type: ignore

# Generated at 2022-06-13 20:22:10.191970
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder('eutf8h')

# Generated at 2022-06-13 20:22:11.779307
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:12.283882
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:22:14.131171
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore



# Generated at 2022-06-13 20:22:20.966045
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getencoder(NAME)
    except LookupError:
        msg = 'Codecs.decoder() failed.'
        raise AssertionError(msg)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        msg = 'Codecs.decoder() failed.'
        raise AssertionError(msg)



# Generated at 2022-06-13 20:22:26.312157
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError('function register() failed')


if __name__ == '__main__':
    register()
    test_register()

# Generated at 2022-06-13 20:22:30.686260
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:22:36.984967
# Unit test for function register
def test_register():
    original_list = codecs.getdecoders()
    original_list = [i[0] for i in original_list]
    register()
    new_list = codecs.getdecoders()
    new_list = [i[0] for i in new_list]
    assert NAME in new_list and NAME not in original_list


# Generated at 2022-06-13 20:22:39.683452
# Unit test for function register
def test_register():
    print('')
    print('Testing register')
    register()


register()


# Generated at 2022-06-13 20:22:43.940114
# Unit test for function register
def test_register():
    with captured_output() as (out, err):
        codecs.lookup(NAME)
    assert out.getvalue().strip() == ''
    assert err.getvalue().strip() == ''
    register()



# Generated at 2022-06-13 20:22:46.790798
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)


# Generated at 2022-06-13 20:22:48.838603
# Unit test for function register
def test_register():
    register()
    name = NAME
    codecs.getdecoder(name)

# Generated at 2022-06-13 20:22:55.980601
# Unit test for function register
def test_register():
    """This function is to test the 'register' function."""
    old_getdecoder = codecs.getdecoder
    old_register = codecs.register
    try:
        # Mock the register and getdecoder functions to make unit testing possible.
        codecs.register = lambda *_args, **_kw: None  # type: ignore
        codecs.getdecoder = lambda x: x
        register()
    finally:
        codecs.getdecoder = old_getdecoder
        codecs.register = old_register



# Generated at 2022-06-13 20:22:57.102611
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:00.069316
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:23:02.104388
# Unit test for function register
def test_register():
    register()

codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:23:17.104022
# Unit test for function register
def test_register():
    """
    This function tests the function register() and the encoder
    and decoder named after this module.

    """
    # Register our codec.
    register()

    text, bytes_ = codecs.getencoder(NAME)('snowman: ☃')  # type: ignore
    assert bytes_ == len('snowman: ☃')
    assert text == b'snowman: \xe2\x98\x83'

    in_string, consumed = codecs.getdecoder(NAME)(text)  # type: ignore
    assert consumed == len(text)
    assert in_string == 'snowman: ☃'

# Generated at 2022-06-13 20:23:26.655678
# Unit test for function register
def test_register():
    # test1: codecs already registered
    register()

    # test2: codecs not yet register
    codecs.register(lambda name: None)
    global NAME
    old_name = NAME
    NAME = 'this_is_a_new_name'
    register()
    codecs.register(lambda name: None)
    codecs.register(lambda name: None)
    Name = NAME
    NAME = old_name

    # test3: codecs has been registered, but name has changed
    codecs.register(lambda name: None)
    register()

# Generated at 2022-06-13 20:23:30.385607
# Unit test for function register
def test_register():
    from tests.test_bazinga import register_decode_timeout

    register_decode_timeout()


if __name__ == '__main__':
    import sys
    sys.exit(1)

# Generated at 2022-06-13 20:23:32.476707
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:23:44.811120
# Unit test for function register
def test_register():
    import sys
    import tbx
    import codecs

    file_path = tbx.file_path_from_module(__file__)
    file_path = str(file_path)

    with tbx.pushd(file_path):
        # noinspection PyUnresolvedReferences
        import eutf8h

    # Add the directory that contains the 'eutf8h.py' module
    # to the search path.
    sys.path.append(file_path)

    # Dynamically import the '_get_codec_info' function.
    from eutf8h import _get_codec_info

    # Register the codec.
    codecs.register(_get_codec_info)

    codec_info = codecs.getdecoder(NAME)

    assert codec_info is not None



# Generated at 2022-06-13 20:23:47.679582
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


if __name__ == '__main__':
    pass

# Generated at 2022-06-13 20:23:48.317282
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:23:54.219511
# Unit test for function register
def test_register():
    assert codecs.lookup_error("eutf8h") == (None, None, 'strict')
    register()
    assert codecs.lookup_error("eutf8h") == (encode, decode, 'strict')
    register()
    register()
    assert codecs.lookup_error("eutf8h") == (encode, decode, 'strict')



# Generated at 2022-06-13 20:24:05.910846
# Unit test for function register
def test_register():
    register()
    out_bytes_1, out_len_1 = codecs.encode('a', 'eutf8h')
    out_bytes_2, out_len_2 = codecs.encode('\x82', 'eutf8h')
    out_bytes_3, out_len_3 = codecs.encode('\u1f6c8', 'eutf8h')

    assert out_bytes_1 == b'a'
    assert out_len_1 == 1
    assert out_bytes_2 == b'\\x82'
    assert out_len_2 == 1
    assert out_bytes_3 == b'\\xf0\\x9f\\x9b\\x88'
    assert out_len_3 == 1


# Generated at 2022-06-13 20:24:06.939973
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:23.469457
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:24:26.977065
# Unit test for function register
def test_register():
    """Unit test for function register."""
    before = codecs.getencoder(NAME)  # type: ignore
    register()
    after = codecs.getencoder(NAME)   # type: ignore
    assert before != after



# Generated at 2022-06-13 20:24:30.536830
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)   # type: ignore


if __name__ == "__main__":
    register()
    cod = codecs.getdecoder(NAME)  # type: ignore
    data = "\\x65\\x6C\\x65\\x6E'.decode('eutf8h')"
    print(cod(data)[0])

# Generated at 2022-06-13 20:24:32.432307
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    import tests.test_encodings
# End unit test

# Generated at 2022-06-13 20:24:33.101145
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:34.658221
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:36.931636
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()  # initial call to register the codec
    register()  # subsequent calls should have no effect

# Generated at 2022-06-13 20:24:40.116979
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore
        return

    raise Exception('"%s" is already registered' % NAME)

# Generated at 2022-06-13 20:24:43.736031
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:24:46.268450
# Unit test for function register
def test_register():
    register()
    # There should now be a registered decoder for the eutf8h codec
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:24.576842
# Unit test for function register
def test_register():
    from importlib import reload, import_module
    from functools import reduce

    register()
    text_str = '\u20AC'
    encoded_text = codecs.encode(text_str, NAME)

    decoded_text, consumed = codecs.decode(encoded_text, NAME)
    assert isinstance(encoded_text, bytes)
    assert text_str == decoded_text
    assert len(encoded_text) == consumed
    assert reduce(lambda a,b: f'{a}{b}', _each_utf8_hex(text_str))\
           == encoded_text.decode('utf-8')

    reload(import_module(NAME))
    print('{} module has been reloaded'.format(NAME))
    register()
    text_str = '\u20AC'
   

# Generated at 2022-06-13 20:25:28.173638
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder('eutf8h') is not None


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:30.013353
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:25:32.297463
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:35.461058
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert isinstance(obj, codecs.CodecInfo)
    assert obj.name == NAME
    assert obj.encode == encode
    assert obj.decode == decode


# Generated at 2022-06-13 20:25:40.682115
# Unit test for function register
def test_register():
    # Test with the codec already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # The codec is not already registered. This shouldn't happen.
        assert False

    # Test the codec being registered
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:25:45.411255
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, 'Codec was already registered'

    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec was not registered'



# Generated at 2022-06-13 20:25:46.856033
# Unit test for function register
def test_register():
    NAME = 'test'
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:25:50.120542
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
        return True
    return False

# Generated at 2022-06-13 20:25:54.601576
# Unit test for function register
def test_register():
    codecs._cache.clear()
    codecs._unknown_encoding_error.cache_clear()
    register()
    actual = codecs.getencoder(NAME)
    assert actual == encode

# Generated at 2022-06-13 20:26:12.703840
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:26:20.703130
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    """Test function 'register' registers the codec."""
    import tempfile

    register()

    # Test that the codec was registered.
    try:
        codecs.lookup(NAME)
    except LookupError:
        assert False, "Codec was not registered"

    # Test that the codec can read the test file.
    with tempfile.TemporaryDirectory() as tmpdirname:
        utf8_filename = tmpdirname + '/utf8_file.txt'
        eutf8h_filename = tmpdirname + '/eutf8h_file.txt'

        utf8_file = open(utf8_filename, 'w')
        utf8_file.write('Hi!\n')
        utf8_file.write(chr(0x00A1))


# Generated at 2022-06-13 20:26:22.852201
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)
    return

# Generated at 2022-06-13 20:26:29.763471
# Unit test for function register
def test_register():
    from mypy_extensions import NoReturn
    from unittest import mock
    from collections import UserString
    from typing import Callable, Any, Tuple, Optional, TypeVar
    from typing_extensions import TypedDict

    Callable_MOCK_CODECS_REGISTER = Callable[
        [Callable[[str], Optional[codecs.CodecInfo]]],
        None
    ]

    class MockCodecsRegister(TypedDict, total=False):
        register: Callable_MOCK_CODECS_REGISTER

    mock_codecs_register = cast(
        MockCodecsRegister,
        mock.Mock()
    )


# Generated at 2022-06-13 20:26:32.995846
# Unit test for function register
def test_register():
    # Test the register function registers and does not unregister.
    for _ in range(2):
        register()
        codecs.getdecoder(NAME)   # type: ignore



# Generated at 2022-06-13 20:26:35.599272
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:37.687581
# Unit test for function register
def test_register():
    """ Unit test code for function register. """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:26:39.567039
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    print(__doc__)

# Generated at 2022-06-13 20:26:40.331394
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:26:41.770064
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:15.745797
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None  # type: ignore
    assert codecs.getdecoder(NAME) is not None  # type: ignore
    with pytest.raises(LookupError):
        del codecs.encode  # type: ignore
    with pytest.raises(LookupError):
        del codecs.decode  # type: ignore



# Generated at 2022-06-13 20:27:16.461304
# Unit test for function register
def test_register():
    pass



# Generated at 2022-06-13 20:27:19.849559
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('strict') == codecs.lookup_error('eutf8h')



# Generated at 2022-06-13 20:27:22.645355
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        print(e)



# Generated at 2022-06-13 20:27:24.281235
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:27:28.858847
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        print(f'{NAME} registered')


# Generated at 2022-06-13 20:27:37.089059
# Unit test for function register
def test_register():
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
    register()
    codecs.getdecoder(NAME)


# Main script. This runs when eutf8h.py is run directly by python.
if __name__ == '__main__':
    # Print a table of test cases.
    from .test_cases import test_cases

    print('Printing test table:\n')
    for name, text, expected in test_cases:
        # noinspection PyUnresolvedReferences
        bytes_, _ = encode(text, 'strict')
        str_, _ = decode(bytes_, 'strict')
        if bytes_ != expected:
            err = 'FAIL'
        else:
            err = '    '
        s_ = name.ljust(20)
        s

# Generated at 2022-06-13 20:27:39.368979
# Unit test for function register
def test_register():
    codecs.lookup(NAME)
    x = codecs.lookup(NAME)
    assert x is not None



# Generated at 2022-06-13 20:27:40.040279
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:27:50.994680
# Unit test for function register
def test_register():
    register()

    # Checking the encode function.
    s = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \'and what is the use of a book,\' thought Alice \'without pictures or conversation?\'\n'
    utf8_bytes = s.encode(NAME)
    # utf8_bytes = codecs.escape_encode(s)[0]
    s_decoded = utf8_bytes.decode(NAME)
    s_encoded = s_decoded.encode(NAME)
    s_decoded_2 = s_encoded.decode(NAME)
    print(s)
    print(utf8_bytes)

# Generated at 2022-06-13 20:29:00.314224
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
        decoder = codecs.getdecoder(NAME)
        codecs.unregister(NAME)
        assert decoder is not None
    else:
        decoder = codecs.getdecoder(NAME)
        assert decoder is not None



# Generated at 2022-06-13 20:29:02.366848
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:29:04.308664
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:29:06.341933
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    register()
    print('python implementation of eutf8h loaded and registered')

# Generated at 2022-06-13 20:29:17.545267
# Unit test for function register
def test_register():
    import time
    import sys
    if sys.version_info.major == 3:
        str_type = str
    elif sys.version_info.major == 2:
        str_type = unicode
    else:
        raise ImportError(
            'eutf8h module is not supported for python %s.%s' % (
            sys.version_info.major,
            sys.version_info.minor,
        ))

    for i in range(sys.version_info.major):
        register()

    # Do some asserts.
    #
    # Assert the 'eutf8h' codec is registered.
    info = codecs.lookup(NAME)
    info = cast(codecs.CodecInfo, info)

    # Assert the 'eutf8h' codec can encode/decode.
    #

# Generated at 2022-06-13 20:29:19.327530
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:20.762325
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:29:28.260487
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        decoder = codecs.getdecoder(NAME)   # type: ignore
        assert decoder is not None
        assert decoder[0] == decode
        assert decoder[1] == None
        assert decoder[2] == 'strict'
        encoder = codecs.getencoder(NAME)   # type: ignore
        assert encoder is not None
        assert encoder[0] == encode
        assert encoder[1] == None
        assert encoder[2] == 'strict'
    finally:
        codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:29:33.512677
# Unit test for function register
def test_register():
    # Test 1:
    # Test the register function
    register()
    with pytest.raises(AttributeError):
        codecs.lookup(NAME)
    try:
        codecs.lookup(NAME)
    except LookupError as e:
        assert str(e) == 'unknown encoding: eutf8h'
    else:
        pytest.fail('AttributeError not raised')


# Unit test to test the encode function

# Generated at 2022-06-13 20:29:36.438813
# Unit test for function register
def test_register():
    try:
        codecs.lookup(NAME)
    except LookupError:
        register()
        codecs.lookup(NAME)

