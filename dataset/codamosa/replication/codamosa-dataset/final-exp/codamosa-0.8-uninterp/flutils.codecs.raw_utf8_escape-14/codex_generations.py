

# Generated at 2022-06-13 20:21:54.700735
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:21:57.369201
# Unit test for function register
def test_register():
    import sys

    try:
        del sys.modules['eutf8h']
    except KeyError:
        pass
    import eutf8h
    try:
        del sys.modules['eutf8h']
    except KeyError:
        pass



# Generated at 2022-06-13 20:21:58.541563
# Unit test for function register
def test_register():
    register()
    codecs.encode(NAME)

# Generated at 2022-06-13 20:21:59.481113
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:22:04.910620
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:22:05.917462
# Unit test for function register
def test_register():
    codecs.register(register)   # type: ignore

# Generated at 2022-06-13 20:22:16.643928
# Unit test for function register
def test_register():
    """Unit test for function :py:func:`register`.

    This function is also a functional test for the :py:mod:`eutf8h` module.
    The :py:mod:`codecs` module will not allow the same encoding from being
    registered more than once.  Therefore, this function unit test is also
    a functional test for the :py:mod:`eutf8h` module.

    """

    # If the encoding is already registered, then the module is already
    # tested.  Therefore, just return from the function.
    try:
        codecs.getdecoder(NAME)
        return
    except LookupError:
        pass

    # Register the encoding.
    register()

    # Get the codec info.

# Generated at 2022-06-13 20:22:18.201197
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:25.035441
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert True
    else:
        assert False

    try:
        codecs.register(_get_codec_info)
    except LookupError:
        assert False
    else:
        assert True



# Generated at 2022-06-13 20:22:29.148771
# Unit test for function register
def test_register():
    def test():
        register()
        try:
            codecs.getdecoder(NAME)
        except LookupError as e:
            raise AssertionError(e)

    test()


# Generated at 2022-06-13 20:23:01.896719
# Unit test for function register
def test_register():
    register()  # type: ignore
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:02.669607
# Unit test for function register
def test_register():
    register()
    register()



# Generated at 2022-06-13 20:23:12.239348
# Unit test for function register
def test_register():
    for name in (
        'eutf8h',
        'test.test_eutf8h.eutf8h',
        'test_eutf8h.eutf8h',
        'eutf8h.eutf8h',
    ):
        try:
            codecs.getdecoder(name)
        except LookupError:
            assert False, f'register(2) failed with {name}'



# Generated at 2022-06-13 20:23:16.886836
# Unit test for function register
def test_register():
    old_get_codec_info = codecs.getcodec  # type: ignore
    try:
        codecs.getcodec = _get_codec_info  # type: ignore
        register()
    finally:
        codecs.getcodec = old_get_codec_info  # type: ignore

# Generated at 2022-06-13 20:23:26.414098
# Unit test for function register
def test_register():
    """Unit test for function register().
    """
    # registration_info: Dict[str, Callable[[], None]] = {}
    # # noinspection SpellCheckingInspection
    # registration_info['py36'] = codecs.register(_get_codec_info)
    # # noinspection SpellCheckingInspection
    # registration_info['py37'] = codecs.register(_get_codec_info)
    # registration_info['py38'] = codecs.register(_get_codec_info)


# Tests for function encode

# Generated at 2022-06-13 20:23:27.155611
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:23:31.362355
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
    else:
        raise AssertionError('The codecs registry is broken.')
    finally:
        codecs.register(_get_codec_info)


# Generated at 2022-06-13 20:23:36.450647
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, "Codec eutf8h is not registered."
    else:
        assert True, "Codec eutf8h is registered."

register()

# Generated at 2022-06-13 20:23:37.586438
# Unit test for function register
def test_register():
    codecs.lookup(NAME)

# Generated at 2022-06-13 20:23:39.405737
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:24:20.817358
# Unit test for function register
def test_register():
    filepath = Path(__file__).parent.parent / 'codecs_eutf8h/__init__.py'
    with filepath.open(mode='r', encoding=NAME) as f:
        lines = f.read().splitlines()
    assert lines[0] == "'''"

# Generated at 2022-06-13 20:24:22.167348
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:24.610306
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore


# Generated at 2022-06-13 20:24:31.939532
# Unit test for function register
def test_register():
    import sys
    import unittest

    from . import _decode, _encode

    class TestRegister(unittest.TestCase):

        def test_register(self):
            from .__init__ import register
            register()
            with self.assertRaises(ImportError):
                from .__init__ import encode, decode

            name = __name__.split('.')[-1]
            codecs.register(_get_codec_info)
            _encode = codecs.getencoder(name)
            _decode = codecs.getdecoder(name)
            self.assertIsNotNone(_encode)
            self.assertIsNotNone(_decode)

        def test_register_already(self):
            from .__init__ import register
            register()
            register()


# Generated at 2022-06-13 20:24:34.606518
# Unit test for function register
def test_register():
    if __name__ == '__main__':
        register()
        print(f'Codec registered: { codecs.lookup(NAME) }.')



# Generated at 2022-06-13 20:24:35.555244
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:37.448732
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    # codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:42.414527
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None
    # This is an application of my codec, so this test should fail
    # (but it doesn't).
    try:
        codecs.getencoder('cp_1252')
    except LookupError:
        pass
    else:
        assert False, 'The cp_1252 encoder was found'
    try:
        codecs.getdecoder('cp_1252')
    except LookupError:
        pass
    else:
        assert False, 'The cp_1252 decoder was found'
    try:
        codecs.getencoder('this_codec_does_not_exist')
    except LookupError:
        pass

# Generated at 2022-06-13 20:24:52.026669
# Unit test for function register
def test_register():
    """
    Test the function register.
    """
    register()
    utf8_hex_decoder = codecs.getdecoder(NAME)

    # Basic test case
    result_tuple_1 = utf8_hex_decoder(b'abc')
    assert result_tuple_1 == ('abc', 3)

    result_tuple_2 = utf8_hex_decoder(b'\\xE2\\x94\\x80\\xE2\\x94\\x80')
    assert result_tuple_2 == ('▀▀', 10)

    result_tuple_3 = utf8_hex_decoder(b'\\xE2\\x94\\x80\\xE2\\x94\\x80', errors='replace')
    assert result_tuple_3 == ('▀▀', 10)



# Generated at 2022-06-13 20:24:53.647881
# Unit test for function register
def test_register():
    """Test the function register()."""
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:13.127879
# Unit test for function register
def test_register():
    from sys import modules
    register()
    assert modules[NAME] is not None


if __name__ == '__main__':
    from sys import modules
    register()
    assert modules[NAME] is not None

# Generated at 2022-06-13 20:25:14.950428
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore



# Generated at 2022-06-13 20:25:19.305438
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getincrementalencoder(NAME), codecs.IncrementalEncoder)
    assert isinstance(codecs.getincrementaldecoder(NAME), codecs.IncrementalDecoder)

# Generated at 2022-06-13 20:25:19.965246
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:25:23.133419
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    text = '\\u3042'
    codecs.decode(text, 'eutf8h')


# Generated at 2022-06-13 20:25:30.779058
# Unit test for function register
def test_register():
    """
    Unit test for function register.

    .. code-block:: python

       import encodings

       # Get the codec object of 'eutf8h'
       codec = encodings.getdecoder('eutf8h')

       # A string of escaped utf8 hexadecimal.
       text1 = '\\xe3\\x81\\x82H\\x68\\xe0\\xb8\\xa1\\x61\\x69'

       # Convert the string into bytes
       text1_bytes = text1.encode('eutf8h')

       # Convert the bytes back into a string
       text1_str = text1_bytes.decode('eutf8h')

       print(text1_str)
    """

    # Register the function into python
    register()

    # Get the codec object of 'eutf8h'

# Generated at 2022-06-13 20:25:33.443761
# Unit test for function register
def test_register():
    register()
    s = 'A'
    data_bytes = s.encode(NAME)
    out = data_bytes.decode(NAME)
    assert out == s

# Generated at 2022-06-13 20:25:45.492523
# Unit test for function register
def test_register():
    assert [__name__, NAME] == [
        'eutf8h',
        __name__.split('.')[-1]
    ]
    test_texts = {
        'abc': 'abc',
        'abc\u03b1': 'abc\\u03b1',
        'a❤c': 'a\\u2764c',
        'a\ud835\udd0a': 'a\\U0001d50a',
    }
    for text_orig, text_escaped in test_texts.items():
        text_bytes_utf8 = text_escaped.encode('utf-8')
        assert text_orig == text_escaped.encode('eutf8h').decode('utf-8')
        assert text_bytes_utf8 == text_orig.encode('eutf8h')

# Generated at 2022-06-13 20:25:48.758522
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:00.241647
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    output_bytes: bytes = codecs.encode(    # type: ignore
                text='A',
                encoding=NAME,
            )
    assert output_bytes == b'A'
    output_bytes = codecs.encode(    # type: ignore
                text='A',
                encoding='eutf8h'
            )
    assert output_bytes == b'A'
    output_bytes = codecs.encode(    # type: ignore
                text='A',
                encoding='eutf8h'
            )
    assert output_bytes == b'A'

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:35.529272
# Unit test for function register
def test_register():
    register()
    codecs.lookup_error(NAME)  # type: ignore



# Generated at 2022-06-13 20:26:37.237897
# Unit test for function register
def test_register():
    codecs.getencoder('eutf8h')
    codecs.getdecoder('eutf8h')


# Generated at 2022-06-13 20:26:38.892106
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:26:47.585565
# Unit test for function register
def test_register():
    # register the codec
    register()

    # Decode using the codec
    try:
        text_input = str('\\xc0\\xa9')
        text_bytes_utf8 = codecs.getdecoder(NAME)(text_input)
    except Exception as e:
        assert False, f'Decode failure due to {e}'
    else:
        expected = bytes('é', encoding='utf8')
        if text_bytes_utf8 != expected:
            assert text_bytes_utf8 == expected, f'Decode failure'

    # Unregister the codec
    try:
        codecs.unregister(NAME)
    except Exception as e:
        assert False, f'Unregister failure due to {e}'



# Generated at 2022-06-13 20:26:54.530882
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('NAME should not be able to lookup.')

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('NAME should be available to lookup.')



# Generated at 2022-06-13 20:27:05.720056
# Unit test for function register
def test_register():
    list_str = [
        '',
        'Hello World\\x20',
        '\\x20',
        '\\u1234\\u5678',
        '\\0',
        '\\00',
        '\\a',
        '\\x0a',
        '\\u000a',
        '\\U0000000A',
        '\\x41\\x42\\x43\\x44\\x45\\x46\\x47\\x48',
        '\\x48\\x47\\x46\\x45\\x44\\x43\\x42\\x41\\x20',
        '\\u9fa5\\u4e00',
    ]

# Generated at 2022-06-13 20:27:08.758221
# Unit test for function register
def test_register():
    """Unit test for the function register().
    """
    register()
    expected = 'eutf8h'
    actual = codecs.getdecoder(NAME).__name__
    assert expected == actual


register()

# Generated at 2022-06-13 20:27:09.972299
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:27:14.744332
# Unit test for function register
def test_register():
    codec = None
    try:
        codec = codecs.getdecoder(NAME)
    except LookupError:
        pass
    if codec is None:
        register()
        codec = codecs.getdecoder(NAME)
    return codec


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    print(test_register())

# Generated at 2022-06-13 20:27:18.947850
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            "Failed to register codec '%s'." % NAME
        )


# Generated at 2022-06-13 20:28:41.194037
# Unit test for function register
def test_register():

    from sys import modules
    from pytest import raises, mark

    from .eutf8h import NAME

    # Register the codec.
    register()

    # Get the codec.
    codec = codecs.getdecoder(NAME)

    # Validate the codec is the expected codec.
    assert codec is not None
    assert codec == _get_codec_info(NAME)
    assert codec.__class__ == codecs.CodecInfo

    # Unregister the codec.
    assert codecs.unregister(NAME)

    # Validate the codec has been unregistered.
    with raises(LookupError):
        codecs.lookup(NAME)

    # Validate module is reloaded.
    from_importlib = modules['eutf8h']
    assert from_importlib is not None

# Generated at 2022-06-13 20:28:46.586941
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # The codec 'eutf8h' is not registered.
        # Register it.
        register()
        assert True is True
    else:
        # The codec 'eutf8h' is already registered.
        assert True is True
    return



# Generated at 2022-06-13 20:28:48.078502
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:28:58.697520
# Unit test for function register
def test_register():
    file_data = '''
    if NAME == '__main__':
        register()
    '''
    with open(__file__, encoding='utf-8') as f:
        file_content = f.read()
    try:
        assert file_content[-1*len(file_data):] == file_data
    except AssertionError:
        print('WARNING: The function register() needs to be called in file %s' % __file__)
        print('WARNING: to register the codec. See the src/__init__.py file for register()')
        print('WARNING: for the codec.')
        # Register the codec manually to test the utf8 hexadecimal codec.
        register()


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:29:00.559770
# Unit test for function register
def test_register():
    if not codecs.lookup(NAME):
        register()
        if not codecs.lookup(NAME):
            raise Exception('Failed registering the codec')

# Generated at 2022-06-13 20:29:09.334728
# Unit test for function register
def test_register():
    def test_codec_info(input_text: str, expected_text: str) -> None:
        # When we do the encode, we want to get back the expected bytes
        # that represent the utf8 hexadecimal version.
        out_bytes = input_text.encode(NAME)
        out_str = out_bytes.decode(NAME)
        print(out_str, expected_text)
        assert out_str == expected_text

        # When we reverse the encode / decode, we want to get back
        # the original input text.
        out_str2 = out_str.encode(NAME).decode(NAME)
        assert out_str2 == input_text

    register()


# Generated at 2022-06-13 20:29:12.261229
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:15.514197
# Unit test for function register
def test_register():
    register()
    codecs.decode(r'\x32\x37', 'eutf8h')
    codecs.encode(r'27', 'eutf8h')

# Generated at 2022-06-13 20:29:20.458446
# Unit test for function register
def test_register():
    register()
    got = codecs.getdecoder(NAME)
    assert got[0].__module__.endswith('pyteutf8h')
    assert got[1].__module__.endswith('pyteutf8h')


if __name__ == "__main__":
    test_register()

# Generated at 2022-06-13 20:29:24.843748
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    finally:
        assert codecs.getdecoder(NAME)  # type: ignore
