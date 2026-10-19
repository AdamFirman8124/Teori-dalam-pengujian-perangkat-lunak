

# Generated at 2022-06-13 20:21:46.751141
# Unit test for function register
def test_register():
    _ = register()


register()

# Generated at 2022-06-13 20:21:48.319662
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:21:50.737894
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) != None
    assert codecs.getencoder(NAME) != None


# Generated at 2022-06-13 20:21:51.685583
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:21:52.954333
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:21:56.726751
# Unit test for function register
def test_register():
    # Register the encoding
    register()
    # Check the codec exists
    codecs.getencoder(NAME)    # type: ignore
    codecs.getdecoder(NAME)    # type: ignore
    # Remove the encoding
    codecs.lookup(NAME).name  # type: ignore
    codecs.lookup_error(NAME)  # type: ignore



# Generated at 2022-06-13 20:21:59.477298
# Unit test for function register
def test_register():
    # This unit test is not really a test. It is a hack to have Pytest
    # recognize this module and run the above doctests.
    register()

# Generated at 2022-06-13 20:22:00.485380
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:02.605458
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getimplementation(NAME)



# Generated at 2022-06-13 20:22:05.244576
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.lookup(NAME)
    except LookupError:
        assert False
    else:
        assert True


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:15.028440
# Unit test for function register
def test_register():
    """Test function _register."""
    register()

    try:
        codecs.getencoder(NAME)
    except LookupError:
        assert False, 'Failed to register encoder!'

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Failed to register decoder!'



# Generated at 2022-06-13 20:22:16.304168
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:22:22.943746
# Unit test for function register
def test_register():
    register()
    encoded_text = "a"
    out, n_encoded_text_consumed = codecs.getencoder(NAME)(encoded_text)
    assert out == b"a"
    assert n_encoded_text_consumed == 1

    decoded_bytes = b"a"
    out, n_decoded_bytes_consumed = codecs.getdecoder(NAME)(decoded_bytes)
    assert out == "a"
    assert n_decoded_bytes_consumed == 1



# Generated at 2022-06-13 20:22:25.319959
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('eutf8h') == (decode, encode)

# Generated at 2022-06-13 20:22:33.001777
# Unit test for function register
def test_register():
    NAME = __name__.split('.')[-1]
    codecs.register(_get_codec_info)   # type: ignore
    # codecs.getdecoder(NAME)
    # Register the codec
    register()
    codecs.getdecoder(NAME)
    # codecs.register(_get_codec_info)   # type: ignore
    # codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:34.438903
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:35.312484
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:37.800391
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None

# Generated at 2022-06-13 20:22:39.776378
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:43.754970
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:22:51.005877
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:54.967570
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Failed to register _get_codec_info'


# Generated at 2022-06-13 20:22:57.206862
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    assert codecs.getdecoder(NAME).name == NAME  # type: ignore



# Generated at 2022-06-13 20:23:14.010314
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)

if __name__ == '__main__':
    import argparse

    # noinspection PyTypeChecker
    def main():
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '-e', '--encode',
            action='store_true',
            help=(
                'Encode the given file writer_name to escaped utf8 '
                'hexadecimal and then write to the given file output.'
            )
        )

# Generated at 2022-06-13 20:23:15.482302
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:23:21.922044
# Unit test for function register
def test_register():
    """
    Unit test for function register
    """
    try:
        import _testcapi

        assert 'utf8_hex' in _testcapi.getcodec_error_encode()
        assert 'utf8_hex' in _testcapi.getcodec_error_decode()
    except ImportError:
        pass

# Generated at 2022-06-13 20:23:31.165389
# Unit test for function register
def test_register():
    """

    """

    codecs.__dict__.pop('_cache', None)
    codecs.__dict__.pop('_unknown_encoding_error', None)
    codecs.__dict__['_cache'] = {}
    codecs.__dict__['_unknown_encoding_error'] = None

    register()

    assert NAME in codecs.__dict__['_cache']
    assert NAME in codecs.__dict__['_cache']['decoders']
    assert NAME in codecs.__dict__['_cache']['codecs']



# Generated at 2022-06-13 20:23:36.406580
# Unit test for function register
def test_register():
    register()
    name = 'eutf8h'
    decode = codecs.getdecoder(name)  # type: ignore
    data = b'\\xC3\\xB8'
    text = decode(data)[0]
    assert text == 'ø', text

# Generated at 2022-06-13 20:23:40.397478
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None


if __name__ == "__main__":
    test_register()

# Generated at 2022-06-13 20:23:43.597597
# Unit test for function register
def test_register():
    register()
    try:
        assert codecs.getdecoder(NAME) is not None
    except LookupError:
        assert False

# Generated at 2022-06-13 20:24:05.166238
# Unit test for function register
def test_register():
    register()
    d = 'some\\x05\\x10escaped\\x11\\x20utf8\\x21\\x30hexadecimal\\x31\\x40chars'
    assert d.encode('eutf8h') == b'some\\x05\\x10escaped\\x11\\x20utf8\\x21\\x30hexadecimal\\x31\\x40chars'
    assert d.decode('eutf8h') == 'some\x05\x10escaped\x11\x20utf8\x21\x30hexadecimal\x31\x40chars'

# Generated at 2022-06-13 20:24:06.143691
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:24:12.588171
# Unit test for function register
def test_register():
    """
    Test for correct registration of codecs.

    """

    import codecs
    import eutf8h

    try:
        codecs.getdecoder(NAME)
        raise RuntimeError('eutf8h was already registered')
    except LookupError:
        pass

    eutf8h.register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError('eutf8h was not registered')


# Generated at 2022-06-13 20:24:14.577614
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
        logged = True
    except LookupError:
        logged = False
    assert logged


# Generated at 2022-06-13 20:24:19.468228
# Unit test for function register
def test_register():
    # make sure the codec is not registered to start
    try:
        codecs.getdecoder(NAME)
        assert False
    except LookupError:
        pass

    # register the codec
    register()

    # make sure the codec is registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False


# Generated at 2022-06-13 20:24:20.324328
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:24:24.606516
# Unit test for function register
def test_register():
    # assert(False)
    register()
    x = codecs.getencoder(NAME)
    y = codecs.getdecoder(NAME)
    assert(x is not None)
    assert(y is not None)

# Generated at 2022-06-13 20:24:26.054819
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:36.174609
# Unit test for function register
def test_register():
    """
    Test function register
    """
    # Get the list of registered codecs
    codecs_list = [_.name for _ in codecs.__dict__['_cache'].values()]

    # Register the codecs
    register()

    # Get the list of registered codecs
    codecs_list_a = [_.name for _ in codecs.__dict__['_cache'].values()]

    # Check that the codecs are registered
    assert len(codecs_list) < len(codecs_list_a)



# Generated at 2022-06-13 20:24:38.049927
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore

# unit test for function encode

# Generated at 2022-06-13 20:24:56.771111
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)



# Generated at 2022-06-13 20:25:02.380697
# Unit test for function register
def test_register():
    """Unit test for function :obj:`register`.
    """
    import io
    import unittest

    class TestRegisterAll(unittest.TestCase):
        def test_register_all(self):
            register()
            file_buffer = io.StringIO()
            print("ABCDEFG", file=file_buffer)
            file_buffer.seek(0)
            data_str = file_buffer.read()
            data_str_bytes = bytes(data_str, 'eutf8h')
            data_str_out = data_str_bytes.decode('eutf8h')
            self.assertEqual(data_str, data_str_out)

    unittest.main()

# Generated at 2022-06-13 20:25:12.956387
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    # Unit test for function _get_codec_info
    from typing import Type
    from unittest import TestCase

    class _Test_get_codec_info(TestCase):
        def _test_get_codec_info(self) -> None:
            self.assertIsInstance(_get_codec_info(NAME), Type[codecs.CodecInfo])

    test_register()
    _Test_get_codec_info()._test_get_codec_info()

    # Unit test for function decode
    from unittest import TestCase

    class _Test_decode(TestCase):
        def _test_decode(self) -> None:
            name = NAME

# Generated at 2022-06-13 20:25:15.320024
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:19.655077
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:24.219126
# Unit test for function register
def test_register():
    def _test_register():
        register()
        codecs.getdecoder(NAME)

    assert_raises_regex(
        LookupError,
        "unknown encoding: '" + NAME + "'",
        _test_register,
    )


# noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:25:34.969337
# Unit test for function register
def test_register():
    import sys
    import os

    save_sys_modules = sys.modules
    save_name = __name__
    save_path = os.getcwd()

# Generated at 2022-06-13 20:25:37.966263
# Unit test for function register
def test_register():
    """Test the function register
    """
    # Test the register function without error
    codecs.register(_get_codec_info)


# Generated at 2022-06-13 20:25:39.851673
# Unit test for function register
def test_register():
    register()
    # codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:42.813085
# Unit test for function register
def test_register():
    """Test that the codec is registered.
    """
    try:
        register()
    except LookupError:
        assert False
    else:
        assert True



# Generated at 2022-06-13 20:26:21.660999
# Unit test for function register
def test_register():
    assert NAME == 'eutf8h'
    register()



# Generated at 2022-06-13 20:26:24.188973
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.lookup_error('eutf8h')
    assert register() == None  # type: ignore

# Generated at 2022-06-13 20:26:25.102721
# Unit test for function register
def test_register():
    register()

register()

# Generated at 2022-06-13 20:26:26.632378
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:27.819544
# Unit test for function register
def test_register():
    register()
    register()

# Generated at 2022-06-13 20:26:29.321801
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:26:39.245723
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

    # s = '\\u2665'
    # print(s.encode('utf8').decode('unicode_escape'))
    # print(s.encode('utf8').decode('unicode_escape').encode('latin1').decode('utf8'))
    # print(s.encode('utf8').decode('unicode_escape').encode('latin1'))
    # print(s.encode('utf8').decode('unicode_escape').encode('latin1').decode('utf8').encode('latin1'))
    # print(s.encode('utf8').decode('unicode_escape').encode('latin1

# Generated at 2022-06-13 20:26:40.892448
# Unit test for function register
def test_register():
    import test.test_eutf8h
    test.test_eutf8h.test_register()

# Generated at 2022-06-13 20:26:43.630931
# Unit test for function register
def test_register():
    register()
    try:
        b"".decode(NAME) # type: ignore
    except LookupError:
        assert False


# Generated at 2022-06-13 20:26:44.131401
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:28:11.823978
# Unit test for function register
def test_register():
    register()
    obj = codecs.getencoder(NAME)
    assert obj[0].__name__ == 'encode'
    obj2 = codecs.getdecoder(NAME)
    assert obj2[0].__name__ == 'decode'



# Generated at 2022-06-13 20:28:14.240960
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    register()
    obj = codecs.getdecoder(NAME)
    assert obj is not None
    assert obj.decode is decode
    assert callable(obj.decode)
    assert not hasattr(obj, 'encode')
    assert obj.encode is None
    assert obj.name == NAME



# Generated at 2022-06-13 20:28:14.763843
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:28:17.876662
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


if __name__ == '__main__':
    register()
    test_register()

# Generated at 2022-06-13 20:28:23.355137
# Unit test for function register
def test_register():
    import sys
    import builtins
    # Register encoding
    register()
    # check if encoding is in codecs.decoder
    sys.modules['__builtin__'] = builtins
    try:
        assert NAME in codecs.decoder.keys()
    except Exception:
        assert NAME in codecs.decoder.keys()


# Generated at 2022-06-13 20:28:26.472071
# Unit test for function register
def test_register():
    encode_func = codecs.getencoder('eutf8h') # type: ignore
    assert encode_func == encode

    decode_func = codecs.getdecoder('eutf8h')  # type: ignore
    assert decode_func == decode



# Generated at 2022-06-13 20:28:30.591444
# Unit test for function register
def test_register():
    """This function tests that the codec has been registered.
    """
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:28:32.261984
# Unit test for function register
def test_register():
    register()
    mute = codecs.getdecoder(NAME)
    assert mute is not None

# Generated at 2022-06-13 20:28:38.001575
# Unit test for function register
def test_register():
    register()
    with pytest.raises(LookupError):
        codecs.getencoder(NAME)
    encoder, decode = codecs.getencoder(NAME)  # type: ignore
    assert encode is encoder  # type: ignore
    assert decode is encoder  # type: ignore


ENCODING = 'eutf8h'

# Create aliases
# noinspection PyIncorrectDocstring

# Generated at 2022-06-13 20:28:45.063545
# Unit test for function register
def test_register():
    # codecs.__all__ is list, so I cannot use a set
    codecs_all = list(codecs.__all__)
    if NAME in codecs_all:
        codecs_all.remove(NAME)
    assert NAME not in codecs_all
    register()
    codecs_all = list(codecs.__all__)
    if NAME in codecs_all:
        codecs_all.remove(NAME)
    assert NAME not in codecs_all
    # noinspection PyUnresolvedReferences
    codecs.remove(NAME)
    codecs_all = list(codecs.__all__)
    if NAME in codecs_all:
        codecs_all.remove(NAME)
    assert NAME not in codecs_all

