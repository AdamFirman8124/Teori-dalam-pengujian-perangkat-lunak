

# Generated at 2022-06-13 20:21:46.484983
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec eutf8h was not registered'
    else:
        assert True

# Generated at 2022-06-13 20:21:54.566749
# Unit test for function register
def test_register():
    # Try to clear the codecs cache, so we can re-register our
    # codec without causing an error.
    try:
        delattr(codecs, '_cache')
    except AttributeError:
        pass

    try:
        delattr(codecs, '_unknown_encoding_error')
    except AttributeError:
        pass

    try:
        delattr(codecs.encodings, NAME)
    except AttributeError:
        pass

    register()

test_register()

# Register our codec function with the codecs module, so we
# can use our codecimporter.
register()

# Generated at 2022-06-13 20:21:59.250711
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # The register function should register the codec.
        register()
        codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:21:59.893143
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:22:00.361263
# Unit test for function register
def test_register():
    register()

register()

# Generated at 2022-06-13 20:22:10.600526
# Unit test for function register
def test_register():
    from io import StringIO

    # Check to see if the codec was already registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:  # pragma: no cover
        codecs.register(_get_codec_info)

    # Create a file string for the codecs unit test.
    f = StringIO()
    f.write('\xe8\x99\x95\xef\xbf\xbd')
    f.seek(0)

    # Test if the codec can read in the string.
    codecs.getreader(NAME)(f).read()

    # Create a file string for the codecs unit test.
    f = StringIO()
    f.write('This is a codec test.')
    f.seek(0)

    # Test if the codec can write to the file.


# Generated at 2022-06-13 20:22:12.025803
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:21.103355
# Unit test for function register
def test_register():
    """Test the function register."""
    import sys
    codecs.register(_get_codec_info)
    reg_names = [t[0] for t in codecs.__registry__.items()]  # type: ignore
    assert NAME in reg_names
    assert NAME in sys.__stderr__.encoding
    del codecs.__registry__[NAME]  # type: ignore
    reg_names = [t[0] for t in codecs.__registry__.items()]  # type: ignore
    assert NAME not in reg_names
    assert NAME not in sys.__stderr__.encoding

# Generated at 2022-06-13 20:22:34.343781
# Unit test for function register
def test_register():
    NAME_CODECS = 'codecs'
    NAME_DATA = 'data'
    NAME_REGISTER = 'register'
    NAME_GETDECODER = 'getdecoder'

    # Import the codecs package into a local variable 'codecs_local'.
    try:
        codecs_local = __import__(NAME_CODECS)
    except ImportError:
        codecs_local = None
        pass

    # Import the codecs.__dict__['data'] package into a local variable
    # 'data_local'.
    try:
        data_local = getattr(codecs_local, NAME_DATA)
    except AttributeError:
        data_local = None
        pass

    # Import the codecs.__dict__['data'].__dict__['register'] function
    # package into a

# Generated at 2022-06-13 20:22:35.215410
# Unit test for function register
def test_register():
    pass

# Generated at 2022-06-13 20:22:41.055269
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        pytest.fail('Failure: codecs.getencoder')


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:22:44.614335
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.getencoder(NAME)
    except LookupError:
        raise Exception('Codec register failed!!')

# Generated at 2022-06-13 20:22:48.224157
# Unit test for function register
def test_register():
    register()
    codec_info = codecs.getdecoder(NAME)
    assert codec_info.name == NAME



# Generated at 2022-06-13 20:22:50.096883
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__  # type: ignore



# Generated at 2022-06-13 20:22:54.704175
# Unit test for function register
def test_register():
    register()
    assert NAME == codecs.getdecoder(NAME)(b'abc').decode()
    # noinspection PyProtectedMember
    assert NAME == codecs._codecs_cn.getdecoder(NAME)(b'abc').decode()

# Generated at 2022-06-13 20:22:56.282050
# Unit test for function register
def test_register():

    # Test the function.
    register()



# Generated at 2022-06-13 20:23:13.653284
# Unit test for function register
def test_register():
    import sys
    import io
    import unittest

    class Test_register(unittest.TestCase):
        @staticmethod
        def _test_register():
            samples = [
                r'\x31',
                '做\\xE4\\\\xBD\\xA0好',
            ]
            for sample in samples:
                data = cast(bytes, sample.encode(NAME))
                result = data.decode(NAME)
                expected = sample
                assert result == expected, 'result: %s' % result

        def test_register(self):
            sys.stdout = io.StringIO()
            self._test_register()
            result = sys.stdout.getvalue()
            expected = ''
            self.assertEqual(result, expected)


# Generated at 2022-06-13 20:23:15.040603
# Unit test for function register
def test_register():
    import codecs
    register()
    codecs.getdecoder('eutf8h')

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:16.819064
# Unit test for function register
def test_register():
    register()

    assert codecs.lookup(NAME).name == NAME



# Generated at 2022-06-13 20:23:21.201282
# Unit test for function register
def test_register():  # pragma: nocover
    register()
    # noinspection PyUnresolvedReferences
    decode_func = codecs.getdecoder(NAME)
    assert decode_func is not None


# Generated at 2022-06-13 20:23:24.491608
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:23:26.002767
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:31.046203
# Unit test for function register
def test_register():
    buf = b'\\xe5\\x8d\\x97\\xe6\\x98\\x8e\\xe5\\x9c\\x9f'
    str_expected = '南明土'
    register()
    str_actual = buf.decode('eutf8h')
    assert str_expected == str_actual


# Generated at 2022-06-13 20:23:36.220980
# Unit test for function register
def test_register():
    register()
    test_str = 'Text: \\xe2\\x9d\\xa4'
    e_str = test_str.encode(NAME)
    s_str = e_str.decode(NAME)
    assert test_str == s_str

# Generated at 2022-06-13 20:23:38.104501
# Unit test for function register
def test_register():
    register()
    import codecs
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:42.760436
# Unit test for function register
def test_register():
    c = codecs.getdecoder(NAME)
    assert c is not None
    assert isinstance(c, tuple)
    assert len(c) == 2
    assert c[0] == decode
    assert c[1] == 0

# Generated at 2022-06-13 20:23:44.204716
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:23:47.149072
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME).name == NAME

test_register()  # will register the codec if not previously registered

# Generated at 2022-06-13 20:23:50.181218
# Unit test for function register
def test_register():
    import sys
    register()
    if 'eutf8h' not in sys.__dict__['_enabled_streams']:
        raise AssertionError(
            'Codec not registered: %r' % NAME,
        )



# Generated at 2022-06-13 20:24:00.415363
# Unit test for function register
def test_register():
    #
    # Test if codec is registered.
    #
    name = __name__.split('.')[-1]
    try:
        codecs.getdecoder(name)
    except LookupError:
        try:
            codecs.getencoder(name)
        except LookupError:
            obj = _get_codec_info(name)
            codecs.register(obj)
            assert codecs.getencoder(name) is obj
            assert codecs.getdecoder(name) is obj
            return
    raise RuntimeError(
        'codec already registered: %s' % name
    )


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:06.143638
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None

register()

del codecs

# Generated at 2022-06-13 20:24:09.692713
# Unit test for function register
def test_register():
    register()

    assert codecs.lookup_error == 'lookup_error'  # pylint: disable=no-member
    assert codecs.name == NAME  # pylint: disable=no-member

# Generated at 2022-06-13 20:24:14.952831
# Unit test for function register
def test_register():
    codecs.register(
        lambda name: name == 'eutf8h' and codecs.CodecInfo(
            name='eutf8h',
            encode=encode,
            decode=decode
        )
    )
    bts = codecs.encode('\u1F680', 'eutf8h')
    assert bts == b'\\xf0\\x9f\\x9a\\x80'


# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:24:18.864056
# Unit test for function register
def test_register():
    # Reset the codecs cache so that 'register' is called. It should be
    # automatically available after it's called once.
    del codecs.decode.cache[NAME]
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:29.282055
# Unit test for function register
def test_register():
    NAME_REF = 'eutf8h'
    register()
    codecs_decoder_tuple = codecs.getdecoder(NAME_REF)
    decoder = codecs_decoder_tuple[0]
    assert decoder(b'\xe1\x88\xb4').__class__ == tuple
    assert decoder(b'\xe1\x88\xb4')[0] == '\u1234'
    assert decoder(b'\xe1\x88\xb4')[1] == 3
    assert codecs.getencoder(NAME_REF).__class__ == tuple
    assert codecs.getencoder(NAME_REF)[0](  # type: ignore
        '\u1234').__class__ == tuple

# Generated at 2022-06-13 20:24:39.573389
# Unit test for function register
def test_register():
    # Register the codec
    register()

    # Get the registered encoding function
    reg_encoder = codecs.getencoder(NAME)   # type: ignore

    # Test encoding

    # Use the registered encoder to encode a string
    out, consumed = reg_encoder('Hello, world!')  # type: ignore
    assert out == b'Hello\\32\\world\\33\\\\21\\\\22\\'
    assert consumed == 13

    # Use the registered encoder to encode a str object
    out, consumed = reg_encoder(UserString('Hello, world!'))  # type: ignore
    assert out == b'Hello\\32\\world\\33\\\\21\\\\22\\'
    assert consumed == 13

    reg_decoder = codecs.getdecoder(NAME)   # type: ignore

    # Test decoding

    # Use

# Generated at 2022-06-13 20:24:42.413847
# Unit test for function register
def test_register():
    # codecs.getencoder('eutf8h')
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:47.447753
# Unit test for function register
def test_register():
    NAME = 'eutf8h'
    def coder():
        raise LookupError()

    def checker():
        return codecs.CodecInfo(
            name=NAME,
            encode=coder,
            decode=coder,
        )

    codecs.register(checker)
    register()

# Generated at 2022-06-13 20:24:50.584686
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)[0] == decode
    assert codecs.lookup(NAME)[1] == encode

if __name__ == '__main__':
    test_register()
    test_encode()
    test_decode()

# Generated at 2022-06-13 20:24:52.097897
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:05.884474
# Unit test for function register
def test_register():
    register()
    obj1 = codecs.getencoder(NAME)  # type: ignore
    obj2 = codecs.getdecoder(NAME)  # type: ignore
    encoding = obj1.__module__ + '.' + obj1.__qualname__
    decoding = obj2.__module__ + '.' + obj2.__qualname__
    assert encoding == 'eutf8h._get_codec_info'
    assert decoding == 'eutf8h._get_codec_info'



# Generated at 2022-06-13 20:25:12.019343
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError()
    codecs.register(_get_codec_info)  # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:23.847249
# Unit test for function register
def test_register():
    from sys import modules
    from subprocess import (
        Popen,
        PIPE,
    )
    from io import StringIO
    from contextlib import redirect_stdout
    import pytest

    with StringIO() as stderr_bytes:
        with redirect_stdout(stderr_bytes):
            proc = Popen(  # nosec
                args=['python3', '-m', 'codecs', 'search_function'],
                stdout=PIPE,
                stderr=PIPE,
                universal_newlines=True
            )
            stdout_bytes, _stderr_bytes = proc.communicate()
            if stdout_bytes is None:
                stdout_bytes = stderr_bytes.getvalue()
            output = stdout_bytes.splitlines()

# Generated at 2022-06-13 20:25:24.773961
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:25:28.282545
# Unit test for function register
def test_register():
    """
    >>> test_register()
    >>> codecs.getdecoder(NAME)
    <function decode at ...>
    """
    register()


if __name__ == '__main__':
    from doctest import testmod
    testmod()

# Generated at 2022-06-13 20:25:31.507705
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False
    else:
        assert True


# Generated at 2022-06-13 20:25:32.441214
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:33.444499
# Unit test for function register
def test_register():
    # Call the function
    register()

# Generated at 2022-06-13 20:25:35.658349
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:25:38.919078
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('Codec was not successfully registered')



# Generated at 2022-06-13 20:25:50.858385
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:57.315626
# Unit test for function register
def test_register():
    '''
    >>> import codecs
    >>> codecs.getdecoder('eutf8h')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    LookupError: unknown encoding: eutf8h
    >>> import eutf8h
    >>> eutf8h.register()
    >>> codecs.getdecoder('eutf8h')
    <built-in function codec_info_encode_eutf8h>
    '''
    pass

# Generated at 2022-06-13 20:26:04.717638
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    from . import utf8h

    # codecs.getencoder('eutf8h')
    # codecs.getdecoder('eutf8h')
    # utf8h = codecs.getencoder('eutf8h')  # type: ignore
    # codecs.getdecoder('eutf8h')
    # utf8h.encode('\u9fff')
    # codecs.getdecoder('eutf8h')

    utf8h.register()

    assert codecs.lookup(NAME).name == NAME

    str_ = '\u97ff'
    out = utf8h.encode(str_)
    assert out == (b'\\xe9\\x9f\\xbf', 1)

    # Test that the string is passed

# Generated at 2022-06-13 20:26:09.950435
# Unit test for function register
def test_register():
    # Check that NAME is NOT a known codec
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Register NAME
    codecs.register(_get_codec_info)

    # Check that NAME is a known codec
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:12.201252
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:14.090897
# Unit test for function register
def test_register():
    """Test function register()."""
    register()



# Generated at 2022-06-13 20:26:14.868313
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:26:17.517311
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)
    try:
        codecs.register(_get_codec_info)
    except Exception as e:
        raise AssertionError(e)


# Generated at 2022-06-13 20:26:26.067619
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore
    utf8_bytes = b'\xf0\x90\x8d\x86'
    str_hex = 'a\\xf0\\x90\\x8d\\x86'
    assert codecs.encode(str_hex, NAME) == utf8_bytes
    assert codecs.decode(utf8_bytes, NAME) == str_hex
    assert codecs.decode(b'\\x00', NAME) == '\\x00'


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:30.954139
# Unit test for function register
def test_register():
    # codecs.register(_get_codec_info)
    register()
    # Get the codec_info instance for this encoder
    codec_info = codecs.getdecoder(NAME)
    assert codec_info is not None



# Generated at 2022-06-13 20:27:06.415475
# Unit test for function register

# Generated at 2022-06-13 20:27:15.797807
# Unit test for function register
def test_register():
    test_str = '\\x61\\x62\\x63\n'
    test_bytes = codecs.escape_decode(test_str.encode('utf-8'))[0]
    test_str2 = codecs.escape_decode(test_str.encode('utf-8'))[0].decode('utf-8')
    assert test_str2 == 'abc'
    print(test_bytes)
    print(test_str2)
    register()
    test_bytes2 = codecs.escape_decode(test_str.encode('utf-8'))[0]
    test_str3 = codecs.escape_decode(test_str.encode('utf-8'))[0].decode('utf-8')
    assert test_str3 == test_str2
    assert test

# Generated at 2022-06-13 20:27:27.379706
# Unit test for function register
def test_register():
    from itertools import islice
    from operator import itemgetter
    from . import unicode_constants as uc
    register()
    a = codecs.getdecoder(NAME)  # type: ignore
    assert a[0] is decode
    assert a[1] is encode
    assert a[2] == 'strict'
    assert a[3] == 'strict'
    a = codecs.iterdecode(uc.BYTES_EUTF8H, NAME)
    assert isinstance(a, codecs.IncrementalDecoder)
    assert next(a) == (uc.STR_EUTF8H + '', 6)
    assert next(a) == ('', 0)

    a = codecs.iterencode(uc.STR_EUTF8H, NAME)

# Generated at 2022-06-13 20:27:31.182884
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:27:33.380857
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)  # type: ignore




# Generated at 2022-06-13 20:27:35.899986
# Unit test for function register
def test_register():
    register()
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:45.026226
# Unit test for function register
def test_register():
    # Get the original codecs list
    original_codecs = codecs.lookup(NAME)
    # Unregister the codecs
    codecs.unregister(NAME)
    # Get the codecs list to confirm that they have been unregistered
    codecs_unregistered = codecs.lookup(NAME)
    # Register the codecs
    register()
    # Get the codecs list to confirm that they are registered
    codecs_registered = codecs.lookup(NAME)
    # Unregister the codecs
    codecs.unregister(NAME)
    # Register the original codecs
    codecs.register(original_codecs)

    assert original_codecs == codecs_registered
    assert codecs_unregistered is None

# Generated at 2022-06-13 20:27:49.505620
# Unit test for function register
def test_register():
    register()
    print(codecs.lookup_error('strict'))
    print(codecs.lookup_error(NAME))
    print(codecs.lookup_error('strict'))
    return



# Generated at 2022-06-13 20:27:56.282669
# Unit test for function register
def test_register():
    """test the register function"""

    def test_encode(text: str, errors: str) -> None:
        """call the encode function"""
        try:
            import eutf8h
            eutf8h.encode(text, errors)
        except UnicodeEncodeError as e:
            raise Exception(
                f'{text!r} (errors={errors!r}) failed: {e.reason} '
                f'({e.object[e.start:e.end]})')

    def test_decode(data: bytes, errors: str) -> None:
        """call the decode function"""

# Generated at 2022-06-13 20:27:59.309155
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:02.086482
# Unit test for function register
def test_register():
    # There is this weird 'super' magic that must be used
    # to get a module's '__name__' and '__file__' attributes
    # to register correctly.
    # See the comment here:
    # https://stackoverflow.com/a/36123367/1709587
    # We could not find a better solution than using the
    # super magic.
    __name__ = __name__
    __file__ = __file__

    register()

    codecs.lookup_error('strict')

# Generated at 2022-06-13 20:29:03.391820
# Unit test for function register
def test_register():
    register()
    codecs.lookup('eutf8h')

# Generated at 2022-06-13 20:29:07.126816
# Unit test for function register
def test_register():
    import unittest

    register()
    # Making sure the register function works by trying to get the
    # decoder of the registered codec.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise unittest.SkipTest(
            'Registering codec (%s) failed.' % NAME
        )



# Generated at 2022-06-13 20:29:08.586325
# Unit test for function register
def test_register():
    register()
    encode('abcd')
    decode(b'abcd')



# Generated at 2022-06-13 20:29:13.131387
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        msg = f'Failed to get codec decoder for name {NAME}'
        print(f'\n{msg}\n{e}')
        raise


# Generated at 2022-06-13 20:29:27.607098
# Unit test for function register
def test_register():
    # pylint: disable=import-outside-toplevel
    import sys
    import builtins
    # pylint: enable=import-outside-toplevel
    import mock

    sys.modules['codecs'] = mock.Mock()
    builtins.__import__ = mock.Mock()
    builtins.__import__.return_value = codecs

    mock_register = mock.Mock()
    mock_register.getdecoder.side_effect = [LookupError(), None]
    mock_register.register = mock.Mock()

    codecs.return_value = mock_register

    try:
        register()
        assert mock_register.register.called
    finally:
        del sys.modules['codecs']
        del builtins.__import__

# Generated at 2022-06-13 20:29:32.953895
# Unit test for function register
def test_register():
    import sys
    import io

    if NAME in sys.modules.keys():
        raise Exception('Cannot run unit test, because module is already imported.')

    sys.modules[NAME] = True
    register()

# Generated at 2022-06-13 20:29:34.043743
# Unit test for function register
def test_register():
    _ = register()



# Generated at 2022-06-13 20:29:34.480890
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:29:36.136073
# Unit test for function register
def test_register():
    """Test the function register."""
    register()
    assert NAME in codecs.getdecoder('aliases')
    # assert NAME in codecs.getencoder('aliases')



# Generated at 2022-06-13 20:31:44.877105
# Unit test for function register
def test_register():
    codecs.register(lambda name: None if name != NAME else _get_codec_info(name))
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('LookupError')