

# Generated at 2022-06-13 20:21:51.730752
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)(b'a')[0] == 'a'
    assert codecs.getencoder(NAME)('a')[0] == b'a'



# Generated at 2022-06-13 20:21:54.647534
# Unit test for function register
def test_register():
    if NAME in codecs.__dict__:
        del codecs.__dict__[NAME]

    register()
    assert NAME in codecs.__dict__, 'Register method did not properly register'\
        ' codec'



# Generated at 2022-06-13 20:21:57.569067
# Unit test for function register
def test_register():
    if codecs.getdecoder(NAME):
        codecs.lookup_error(NAME)
        codecs.lookup_error(NAME)
    register()
    codecs.lookup_error(NAME)
    codecs.lookup_error(NAME)

test_register()

# Generated at 2022-06-13 20:22:01.719776
# Unit test for function register
def test_register():
    '''
    Test the function register()

    :return: None
    '''
    from codecs import lookup
    from eutf8h.main import NAME
    register()
    assert lookup(NAME) is not None


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:04.536145
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    try:
        codecs.lookup(NAME)
    except LookupError:
        register()
        codecs.lookup(NAME)

# Generated at 2022-06-13 20:22:07.847286
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    try:
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(e)



# Generated at 2022-06-13 20:22:10.063279
# Unit test for function register
def test_register():
    register()
    assert NAME == codecs.getdecoder(NAME).name


# Generated at 2022-06-13 20:22:19.288041
# Unit test for function register
def test_register():
    class Mock_getdecoder:
        def __call__(self, name):
            if name == NAME:
                raise LookupError

    mock_getdecoder = Mock_getdecoder()

    class Mock_register:
        def __init__(self):
            self.args = tuple()

        def __call__(self, *args, **kwargs):
            self.args = args, kwargs

        def reset(self):
            self.args = tuple()

    mock_register = Mock_register()

    class Mock_codecs:
        def __getattr__(self, name):
            if name == "getdecoder":
                return mock_getdecoder
            elif name == "register":
                return mock_register
            raise AttributeError


# Generated at 2022-06-13 20:22:21.312195
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:26.505623
# Unit test for function register
def test_register():
    register()

    # If the codec is registered, then the NAME should be in the aliases
    # of the codec's list.
    codecs_obj = codecs.lookup(NAME)
    aliases = codecs_obj.getaliases()
    assert NAME in aliases



# Generated at 2022-06-13 20:22:37.565215
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:38.858743
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:42.186968
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__.get('_cache', {})
    register()
    assert NAME in codecs.__dict__.get('_cache', {})



# Generated at 2022-06-13 20:22:53.393621
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise AssertionError('failed')
    register()
    codecs.getdecoder(NAME)     # type: ignore

if __name__ == '__main__':
    # Check that this codec is not already registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise LookupError(
            'The codec, "%s", is already registered' % NAME
        )
    codecs.register(_get_codec_info)
    # noinspection PyUnreachableCode
    codecs.getdecoder(NAME)     # type: ignore

# Generated at 2022-06-13 20:22:57.117069
# Unit test for function register
def test_register():
    """Tests the register() function

    """
    codecs.getdecoder(NAME)
    try:
        codecs.getdecoder('unknown')
        assert False
    except LookupError:
        pass


if __name__ == "__main__":
    test_register()

# Generated at 2022-06-13 20:23:00.415272
# Unit test for function register
def test_register():
    register()
    codec_info: codecs.CodecInfo = codecs.getdecoder(__name__.split('.')[-1])

    if not codec_info:
        raise RuntimeError("Failed to register codec")

    return


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:04.339363
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:07.881552
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.encode('', NAME).decode()
    assert NAME in codecs.decode(NAME.encode(), NAME)

# Generated at 2022-06-13 20:23:11.491689
# Unit test for function register
def test_register():
    for name in ('eutf8h'):
        try:
            codecs.getdecoder(name)
        except LookupError:
            codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:23:16.005166
# Unit test for function register
def test_register():
    print(f'{NAME} is not registered')
    register()
    registered_codec = codecs.getencoder(NAME)
    assert registered_codec is not None
    print(f'{NAME} is registered')


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:21.596766
# Unit test for function register
def test_register():
    register()
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:25.826864
# Unit test for function register
def test_register():
    """Test that the NAME codec is defined."""
    import codecs
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(f"{NAME} codec not registered.")


# Generated at 2022-06-13 20:23:34.873188
# Unit test for function register
def test_register():
    if codecs.getdecoder(NAME):
        codecs.register(lambda name: None if name != NAME else codecs.CodecInfo(  # type: ignore
            name=NAME,
            encode=encode,  # type: ignore[arg-type]
            decode=decode,  # type: ignore[arg-type]
        ))
    register()
    if codecs.getdecoder(NAME):
        assert codecs.getdecoder(NAME)(b'X') == ('X', 1)
        assert codecs.getencoder(NAME)('X') == (b'X', 1)
        assert codecs.lookup(NAME).encode('xyz') == (b'xyz', 3)

# Generated at 2022-06-13 20:23:36.862093
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:42.628705
# Unit test for function register
def test_register():
    register()
    data = b"testing testing 123, \\x77"
    result = data.decode('eutf8h')
    message = "should match 'testing testing 123, \\x77'"
    assert result == 'testing testing 123, w', message


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:52.255922
# Unit test for function register
def test_register():
    # Create a temporary file object and a temporary directory
    # object, that will be removed as soon as they are no longer
    # referenced.
    with tempfile.TemporaryDirectory() as tempdir:
        # Get the path to the temporary directory.
        tempdir_name = os.path.normpath(tempdir)

        # Create a temporary file, which will be removed when the
        # with block is exited.
        with tempfile.NamedTemporaryFile(
            mode='w',
            dir=tempdir_name,
            encoding='utf-8'
        ) as temp_file:
            # Get the path to the temporary file.
            temp_file_name = os.path.normpath(temp_file.name)

            # Write some Python code to the temporary file, which will
            # attempt to import the module 'test_codec_

# Generated at 2022-06-13 20:23:56.894819
# Unit test for function register
def test_register():
    reset = []
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        reset.append('reset')

    register()
    codecs.getdecoder(NAME)

    if reset:
        codecs.lookup(NAME).__dict__   # type: ignore



# Generated at 2022-06-13 20:23:57.811887
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:00.617200
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__
    codecs.__dict__ = {}



# Generated at 2022-06-13 20:24:02.716187
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None
    codecs.lookup(NAME)


# Generated at 2022-06-13 20:24:14.400697
# Unit test for function register
def test_register():
    import sys
    import sysconfig
    from importlib.util import find_spec
    from os import path

    script_dir_path = path.dirname(path.realpath(__file__))
    script_dir_path = path.join(script_dir_path, '..')
    script_dir_path = path.abspath(path.normpath(script_dir_path))
    # On Windows, this is something like:
    #   C:\\Users\\me\\AppData\\Local\\Temp\\3\\pycharm-packaging\\eutf8h\\src
    sys.path.append(script_dir_path)

    ########################################################################
    # Import the module to be tested
    ########################################################################
    from eutf8h import eutf8h
    assert eutf8h is not None


# Generated at 2022-06-13 20:24:16.667241
# Unit test for function register
def test_register():
    register()
    d = codecs.getdecoder(NAME)
    d(b'\\x41\\x42')

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:26.227711
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    # Test once
    assert codecs.getdecoder(NAME) is not None
    # Test twice raises LookupError
    try:
        codecs.register(_get_codec_info)
    except LookupError:
        pass
    else:
        raise AssertionError(
            'codecs.register(_get_codec_info) should have raised '
            'a LookupError'
        )
    # Cleanup test
    codecs._cache.clear()
    codecs._unknown_encoding_error.clear()


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:24:27.541295
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:29.145650
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:30.675829
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:34.658289
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__
    register()
    assert NAME in codecs.__dict__
    codecs.__dict__.pop(NAME)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:24:39.431162
# Unit test for function register
def test_register():
    from test.codec_tests import (
        test_register,
        test_encode,
        test_decode
    )
    register()
    test_register(NAME)
    test_encode(NAME)
    test_decode(NAME)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:24:50.691311
# Unit test for function register
def test_register():
    """Test if the function register() is working correctly.
    """
    # First, make sure the codec is NOT registered
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # If it is not registered, then try to register it.
        print('The codec is not registered yet. Registering it.')
        codecs.register(_get_codec_info)
    else:
        # If it is registered, then unregister it.
        codecs.lookup(NAME).decode('', errors='strict')
        print('The codec is registered. Unregistering it.')
        codecs.lookup(NAME).decode('', errors='strict')

    # Try to register it again.

# Generated at 2022-06-13 20:24:58.253227
# Unit test for function register
def test_register():
    # Arrange
    expected = "abc"
    expected_len = 3
    s = "abc".encode(NAME)
    # Act
    register()
    actual, actual_len = codecs.getdecoder(NAME)(s)
    # Assert
    assert actual == expected
    assert actual_len == expected_len
    print(
        "actual={actual} actual_len={actual_len} "
        "expected={expected} expected_len={expected_len}".format(
            actual=actual,
            actual_len=actual_len,
            expected=expected,
            expected_len=expected_len,
        )
    )

test_register()


# Main

# Generated at 2022-06-13 20:25:11.679408
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder(NAME) == _get_codec_info(NAME)


# noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:25:13.984364
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME)
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:16.266473
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:17.997864
# Unit test for function register
def test_register():
    """
    Test for function register
    """
    register()



# Generated at 2022-06-13 20:25:22.004466
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('Codec not found')

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:25:25.431957
# Unit test for function register
def test_register():
    register()


# # Unit test for function encode
# def test_encode():
#     encode('abc', 'strict')
#
#
# # Unit test for function decode
# def test_decode():
#     decode('abc', 'strict')

# Generated at 2022-06-13 20:25:27.323639
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:29.605593
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME)()


# Generated at 2022-06-13 20:25:31.564796
# Unit test for function register
def test_register():
    """Unit test for function register."""

    register()
    codecs.getdecoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:25:33.296120
# Unit test for function register
def test_register():
    # codecs.getdecoder('eutf8h')

    assert codecs.lookup(NAME) is not None

# Generated at 2022-06-13 20:25:55.048769
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # For type checking

# Generated at 2022-06-13 20:25:57.354202
# Unit test for function register
def test_register():
    """Test module function register()."""
    if NAME not in codecs.__all__:
        register()
        assert NAME in codecs.__all__



# Generated at 2022-06-13 20:26:00.887423
# Unit test for function register
def test_register():
    """Unit Tests for function register"""
    # Call function register
    register()

    # Verify that the registered codec name is in the codecs list.
    assert NAME in codecs.getdecoder(NAME).__self__.name


# Unit tests for function encode

# Generated at 2022-06-13 20:26:07.386630
# Unit test for function register
def test_register():
    register()
    codec_info = codecs.getdecoder(NAME)
    out, consume = codec_info('\xf0\x9f\x8d\xb0')
    if out != '🍰':
        raise ValueError(
            f'Unexpected result, got {out} instead of \'🍰\'.'
        )

# Generated at 2022-06-13 20:26:12.766313
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME)
    assert codecs.lookup(NAME)
    assert NAME in codecs.lookup(NAME)
    assert codecs.lookup(NAME) == NAME



# Generated at 2022-06-13 20:26:17.429450
# Unit test for function register
def test_register():
    codecs.register(None)
    try:
        codecs.getdecoder(NAME)
        assert False, 'the codec must not be registered yet.'
    except LookupError:
        pass

    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:24.656027
# Unit test for function register
def test_register():
    # Check that the codec info is registered.
    codecs.getdecoder(NAME)
    # Check the codecs.CodecInfo object matches the _get_codec_info object.
    codecs_obj = codecs.getdecoder(NAME)
    get_codec_info_obj = _get_codec_info(NAME)
    assert codecs_obj == get_codec_info_obj


if __name__ == '__main__':
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:32.066333
# Unit test for function register
def test_register():
    from conftest import (
        delete_registered_name,
        register_and_get_codec_info,
    )
    delete_registered_name(NAME)
    with register_and_get_codec_info(NAME, _get_codec_info) as (
            codec_info, reg_name):
        assert reg_name == NAME



# Generated at 2022-06-13 20:26:34.329621
# Unit test for function register
def test_register():
    try:
        register()
    except Exception:
        assert False, 'Call to register function failed.'


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:36.958917
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getencoder(NAME)
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:24.823527
# Unit test for function register
def test_register():
    register()
    data = b'\\x58'
    actual = data.decode('eutf8h')
    expect = 'X'
    assert actual == expect

register()

# Generated at 2022-06-13 20:27:26.989092
# Unit test for function register
def test_register():
    assert all(
        (
            register,
        )
    )



# Generated at 2022-06-13 20:27:28.966137
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:27:31.487392
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:32.023704
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:27:33.223341
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:27:35.858225
# Unit test for function register
def test_register():
    register()
    assert(NAME in codecs.getdecoder('eutf8h'))



# Generated at 2022-06-13 20:27:40.220450
# Unit test for function register
def test_register():
    register()
    encoded = '◓'.encode(NAME)
    assert encoded == b'\\xe2\\x97\\x93'
    decoded = encoded.decode(NAME)
    assert decoded == '◓'


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:42.923873
# Unit test for function register
def test_register():
    codecs.register = lambda: None
    # noinspection PyUnusedLocal
    codecs.getdecoder = lambda x: None  # type: ignore
    register()

# Generated at 2022-06-13 20:27:43.755273
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:29:20.643859
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:29:21.710330
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:29:26.210685
# Unit test for function register
def test_register():
    # Test that NAME is not registered
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        # codec not registered
        assert True
    else:
        # codec registered
        assert False

    # Test that NAME is registered after running register()
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        # codec not registered
        assert False
    else:
        # codec registered
        assert True



# Generated at 2022-06-13 20:29:29.149781
# Unit test for function register
def test_register():
    register()
    codec = codecs.getdecoder(NAME)
    name_codec = codec.__name__
    actual_name = 'eutf8h'
    assert name_codec == actual_name


# Generated at 2022-06-13 20:29:31.505229
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__
    register()
    assert NAME in codecs.__dict__



# Generated at 2022-06-13 20:29:45.987847
# Unit test for function register
def test_register():
    from codecs import Codec, CodecInfo
    from functools import partial

    # Verify that the codec named 'eutf8h' is not registered.
    assert 'eutf8h' not in codecs.decode.cache

    # Register the codec.
    register()

    # Verify that the codec named 'eutf8h' is registered.
    assert 'eutf8h' in codecs.decode.cache

    # Verify that all the expected properties are set.
    codec_info = codecs.decode.cache['eutf8h']
    assert isinstance(codec_info, CodecInfo)
    assert isinstance(codec_info.encode, partial)  # type: ignore
    assert isinstance(codec_info.decode, partial)  # type: ignore

    # Register the codec again.
    register()




# Generated at 2022-06-13 20:29:51.905663
# Unit test for function register
def test_register():
    register()

    # noinspection PyUnresolvedReferences
    assert codecs.getdecoder(NAME) is decode  # type: ignore
    # noinspection PyUnresolvedReferences
    assert codecs.getencoder(NAME) is encode  # type: ignore
    # noinspection PyUnresolvedReferences
    assert codecs.getreader(NAME) is codecs.getreader('utf-8')  # type: ignore
    # noinspection PyUnresolvedReferences
    assert codecs.getwriter(NAME) is codecs.getwriter('utf-8')  # type: ignore



# Generated at 2022-06-13 20:29:54.346644
# Unit test for function register
def test_register():
    g = globals()
    f = g['_get_codec_info']
    codecs.register(f)



# Generated at 2022-06-13 20:29:55.614280
# Unit test for function register
def test_register():
    """Test the function `register()`"""
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:29:56.405016
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)