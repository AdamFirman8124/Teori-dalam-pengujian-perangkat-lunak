

# Generated at 2022-06-13 20:21:54.896433
# Unit test for function register
def test_register():
    # Unregister the codec.
    try:
        codecs.decode_error_registry.pop(NAME)    # type: ignore
        codecs.lookup_error_registry.pop(NAME)    # type: ignore
    except KeyError:
        pass

    # Register the codec.
    register()

    # Verify the codec is registered.
    text = 'encode'
    out_bytes = f'\\{hex(ord(text[0]))[1:]}'
    out_bytes += f'\\{hex(ord(text[1]))[1:]}'
    out_bytes += f'\\{hex(ord(text[2]))[1:]}'
    out_bytes += f'\\{hex(ord(text[3]))[1:]}'

# Generated at 2022-06-13 20:22:00.874257
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['__all__'], 'Codec not registered'
    _ = codecs.getencoder(NAME)
    _ = codecs.getdecoder(NAME)
    assert NAME in codecs.__dict__['_cache'], 'Codec not cached'


# Generated at 2022-06-13 20:22:03.308900
# Unit test for function register
def test_register():  # pragma: no cover
    register()
    name = 'eutf8h'
    codecs.getdecoder(name)
    codecs.getencoder(name)

# Generated at 2022-06-13 20:22:10.239567
# Unit test for function register
def test_register():
    import sys
    import unittest

    class TestRegister(unittest.TestCase):
        def setUp(self):
            try:
                self.result = codecs.lookup(NAME)
            except LookupError:
                self.result = None

        def tearDown(self):
            if __name__ == '__main__':
                sys.exit()

        def test_register(self):
            register()
            self.assertIsNotNone(self.result)

    unittest.main()

# Generated at 2022-06-13 20:22:19.459165
# Unit test for function register
def test_register():
    import sys
    from io import StringIO
    from unittest import TestCase, main as unittest_main

    # Load the codecs module after we have registered our codec
    # so that it has a chance to override the existing 'eutf8h'
    # codec.
    import codecs

    test_string: str = 'abc𝌆𝌆'
    expected_string: str = 'abc\\xf0\\x9d\\x8c\\x86\\xf0\\x9d\\x8c\\x86'

    if sys.version_info < (3, 6):
        test_string = codecs.decode(
            codecs.encode(test_string, 'unicode_escape'),
            'unicode_escape',
        )

# Generated at 2022-06-13 20:22:23.605507
# Unit test for function register
def test_register():
    register()
    try:
        codecs.lookup_error(NAME)
    except LookupError:
        assert False
    else:
        assert True


# Generated at 2022-06-13 20:22:24.955728
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:22:27.865226
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['_cache']
    assert NAME in codecs.__dict__['_unknown']


# Generated at 2022-06-13 20:22:30.920350
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo),  \
        'register did not register the codec'

# Generated at 2022-06-13 20:22:33.459370
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)

register()

# Generated at 2022-06-13 20:22:43.693567
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError('Test failed: Function codecs.register failed.')

if __name__ == '__main__':
    # Testing
    import unittest

    class TestModule(unittest.TestCase):
        def test_register(self):
            # We want to make sure we don't raise an exception.
            test_register()

    unittest.main()
    # End Testing

# Generated at 2022-06-13 20:22:47.077867
# Unit test for function register
def test_register():
    register()
    foo: bytes = b'\\x61'
    content = codecs.decode(foo, NAME)
    assert content == 'a'



# Generated at 2022-06-13 20:22:50.165003
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:52.976672
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:22:56.203164
# Unit test for function register
def test_register():
    assert NAME in codecs.decode(b'', NAME)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:12.879501
# Unit test for function register
def test_register():
    from io import StringIO
    buf = StringIO()
    codecs.register(_get_codec_info)
    bytes_str = "Pranav's" + chr(0xE2) + chr(0x80) + chr(0xA6) \
        + " encoding"
    bytes_str += chr(0xE2) + chr(0x80) + chr(0xA6)
    b = bytes_str.encode(NAME)    # type: ignore
    u = b.decode(NAME)            # type: ignore
    buf.write(b)
    buf.flush()


if __name__ == '__main__':
    import sys
    register()
    test_register()
    sys.exit(0)

# Generated at 2022-06-13 20:23:14.435890
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME).name


# Generated at 2022-06-13 20:23:20.809127
# Unit test for function register
def test_register():
    if NAME in codecs.__dict__.get('_cache', {}):
        del codecs._cache[NAME]
    try:
        codecs.lookup_error(NAME)
        assert False
    except LookupError:
        pass
    register()
    codecs.lookup_error(NAME)



# Generated at 2022-06-13 20:23:30.822084
# Unit test for function register
def test_register():
    from prance import ResolvingParser
    import codecs
    codecs.getdecoder(NAME)
    swagger_file = 'tests/fixtures/api-with-refs/swagger_2.0/default.yaml'
    parser = ResolvingParser(str(swagger_file))
    parser.parse_from_file(str(swagger_file))
    str_data = parser.specification['info']['title']
    bytes_data = codecs.encode(str_data, 'eutf8h')
    assert str_data == codecs.decode(bytes_data, 'eutf8h')

# Generated at 2022-06-13 20:23:33.957527
# Unit test for function register
def test_register():
    register()

    assert NAME == codecs.getdecoder(NAME).__name__
    assert NAME == codecs.lookup(NAME).__name__

    # Register again to test the already registered exception.
    try:
        register()
    except ValueError:
        pass
    else:
        raise Exception('Failed to raise a ValueError.')



# Generated at 2022-06-13 20:23:42.890570
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)   # type: ignore[arg-type]


codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:23:51.517029
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder('eutf8h')
    except LookupError as e:
        raise AssertionError(e)
    try:
        codecs.getencoder('eutf8h')
    except LookupError as e:
        raise AssertionError(e)


encode.__doc__ = codecs.encode.__doc__.replace(
    'str',
    'str or :obj:`~UserString`',
)

decode.__doc__ = codecs.decode.__doc__.replace(
    'str',
    'str or :obj:`~UserString`',
)

# Generated at 2022-06-13 20:23:53.965656
# Unit test for function register
def test_register():
    register()
    assert isinstance(
        codecs.getdecoder(NAME),
        codecs.CodecInfo
    )



# Generated at 2022-06-13 20:23:55.487686
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:23:58.423339
# Unit test for function register
def test_register():
    register()

    # Verify that the 'eutf8h' codec was registered.
    ci = codecs.lookup(NAME)
    assert ci.name == NAME



# Generated at 2022-06-13 20:24:01.733593
# Unit test for function register
def test_register():
    register()
    assert NAME in dir(codecs)
    assert NAME in dir(encodings)

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:24:02.628407
# Unit test for function register
def test_register():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:24:06.059505
# Unit test for function register
def test_register():
    """Ensure that the codec is registered
    """
    register()
    # TODO: Figure out how to actually test this more than hoping it works
    codecs.getdecoder(NAME) # Should not throw exception

# Generated at 2022-06-13 20:24:09.960075
# Unit test for function register
def test_register():
    assert 'eutf8h' not in codecs.__all__
    register()
    assert 'eutf8h' in codecs.__all__


# For compatability with Python 2.6, 2.7 and 3.0

# Generated at 2022-06-13 20:24:12.038729
# Unit test for function register
def test_register():
    register()

    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:24:29.214477
# Unit test for function register
def test_register():
    # Make sure that the codec is not registered
    # before running the unit test.
    try:
        codecs.lookup_error(NAME)
        raise AssertionError(
            f"{NAME} codec should not be registered "
            f"prior to unit testing"
        )
    except LookupError:
        pass
    register()
    # Make sure that the codec is registered when
    # the function ``register`` is called.
    try:
        codecs.lookup_error(NAME)
    except LookupError as e:
        raise AssertionError(
            f"{NAME} codec should have been registered "
            f"during unit test but did not: {e}"
        )
    # If the code was already registered, then the
    # following should raise a LookupError.

# Generated at 2022-06-13 20:24:30.792445
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:40.404028
# Unit test for function register
def test_register():
    test_cases = [
        (1, 'ASCII', 1, False),
        (1, 'eutf8h', 1, False),
        (1, 'eutf8h', 1, False),
        (1, 'eutf8h', 1, True),
    ]

    for c in test_cases:
        c_expected = c[0]
        c_func = c[1]
        c_case = c[2]
        c_exception = c[3]

        # Prepare expected and given values
        expected = c_expected
        exception = c_exception

        # The function to call
        func = getattr(sys.modules[__name__], c_func)

        # Prepare call arguments
        call_args = ()
        if c_case == 1:
            call_args = (1,)

       

# Generated at 2022-06-13 20:24:44.433435
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise RuntimeError

    register()
    codecs.getdecoder(NAME)


test_register()

# Generated at 2022-06-13 20:24:45.676260
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:24:53.760837
# Unit test for function register
def test_register():
    register()
    # noinspection PyUnresolvedReferences
    codecs.getencoder(NAME)
    # noinspection PyUnresolvedReferences
    codecs.getdecoder(NAME)
    codecs.lookup(NAME)


__version__ = '0.2.2'
__author__ = 'Keith F. Prussing'
__author_email__ = 'kprussing@bigfoot.com'
__url__ = 'https://github.com/kprussing/eutf8h'
__description__ = 'Extended unicode format 8 hexadecimal codec'

# Generated at 2022-06-13 20:24:55.625748
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:57.637515
# Unit test for function register
def test_register():
    """ Unit test for function register()

    """
    register()
    actual = codecs.getdecoder(NAME)
    assert callable(actual)

# Generated at 2022-06-13 20:25:00.304187
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise ValueError("Codecs has already been registered")
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise ValueError("Codecs did not register")
    else:
        pass


# Generated at 2022-06-13 20:25:02.773265
# Unit test for function register
def test_register():
    class TestObject(object):
        def test_register_passes(self):
            register()
    TestObject().test_register_passes()



# Generated at 2022-06-13 20:25:23.131616
# Unit test for function register
def test_register():
    expected_name_decode = NAME + '.decode'
    expected_name_encode = NAME + '.encode'
    register()
    ret_decode = codecs.getdecoder(NAME)
    ret_encode = codecs.getencoder(NAME)
    assert ret_decode.__name__ == expected_name_decode
    assert ret_encode.__name__ == expected_name_encode



# Generated at 2022-06-13 20:25:25.600043
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:25:26.698599
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:30.571762
# Unit test for function register
def test_register():
    # Register the codec.
    register()

    # Verify that the codec is registered.
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:25:32.066619
# Unit test for function register
def test_register():
    from eutf8h import register
    register()



# Generated at 2022-06-13 20:25:33.444712
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:35.425211
# Unit test for function register
def test_register():
    import lib3to6.tests.support.stdlib_test as stdlib_test
    stdlib_test.register()

register()

# Generated at 2022-06-13 20:25:37.229295
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:39.648423
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:25:40.636097
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:26:12.572649
# Unit test for function register
def test_register():
    name = NAME
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(name)
    except LookupError:
        raise AssertionError('Codec %s not registered' % name)



# Generated at 2022-06-13 20:26:14.924779
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)

# Generated at 2022-06-13 20:26:15.871876
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:26:17.938390
# Unit test for function register
def test_register():
    register()
    code = codecs.getdecoder(NAME)
    __, _ = code(b'\xF0', errors=None)
    return True


# Generated at 2022-06-13 20:26:20.636768
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    import pytest
    pytest.main(args=['', __file__])

# Generated at 2022-06-13 20:26:23.183928
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'No getdecoder(%s) found.' % NAME



# Generated at 2022-06-13 20:26:24.606722
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:26:25.796246
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:26:37.223403
# Unit test for function register
def test_register():

    ##########################################################################
    # Add 2nd codec eutf8h.
    ##########################################################################

    codecs.register(_get_codec_info)   # type: ignore

    ##########################################################################
    # Test codec lookup
    ##########################################################################

    assert codecs.lookup(NAME) == codecs.lookup('eutf8h')

    ##########################################################################
    # Test codec encode
    ##########################################################################

    # Test various utf8 hexadecimal strings.

# Generated at 2022-06-13 20:26:39.208646
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:41.858860
# Unit test for function register
def test_register():
    # Assert that when NAME is not registered an exception is thrown.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    # Assert that when NAME is registered no exception is thrown.
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:44.980958
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) == codecs.CodecInfo(
        name='eutf8h',
        encode=encode,
        decode=decode
    )
    codecs.lookup(NAME).increment_success_count()


# Generated at 2022-06-13 20:27:46.469633
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:48.420379
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:27:50.912785
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    register()
    print('Registered')

# TODO write tests

# Generated at 2022-06-13 20:27:52.797357
# Unit test for function register
def test_register():
    # Load the codecs module.
    _ = codecs.decode

    # Load the module.
    _ = codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:28:04.904266
# Unit test for function register
def test_register():
    from re import sub, search
    from io import StringIO
    import sys

    # Get the text that is printed to stdout when the codec is
    # registered.
    string_io = StringIO()
    _stdout_backup = sys.stdout
    sys.stdout = string_io
    register()
    sys.stdout = _stdout_backup
    string_io.seek(0)
    stdout_text = string_io.read()

    # Make sure that the stdout text is showing
    # that the codec has been registered.
    match_obj = search(
        '(?<=registering encoding )'
        '(?P<name>'
        '[A-Za-z0-9\_]+)'
        '(?= - )',
        stdout_text
    )
    assert match

# Generated at 2022-06-13 20:28:08.269080
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
        print('Test passed')
    except LookupError:
        print('Test failed')


# Generated at 2022-06-13 20:28:13.234643
# Unit test for function register
def test_register():
    codecs._cache.clear()               # type: ignore
    delattr(sys.modules[__name__], 'register')
    cmd = 'from %s import register; register()' % __name__
    exec(cmd, globals(), globals())
    assert sys.modules[__name__].register == register
    codecs._cache.clear()               # type: ignore


# Generated at 2022-06-13 20:28:17.041325
# Unit test for function register
def test_register():
    # Get a list of codecs from the codecs module.
    codec_list = list(codecs.__dict__.keys())

    # The eutf8h codec should not be registered.
    assert 'eutf8h' not in codec_list
    register()
    codec_list = list(codecs.__dict__.keys())
    assert 'eutf8h' in codec_list

# Generated at 2022-06-13 20:30:28.760945
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass

    # Call function.
    register()

    # Check that the name is registered.
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:33.684102
# Unit test for function register
def test_register():
    """Test that codec can be registered
    """
    # Decode the string using the codec.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    out = codecs.decode(b'\\xC2\\xA2', NAME)
    assert isinstance(out, str)
    assert out == '¢'

# Generated at 2022-06-13 20:30:35.613572
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:30:37.462201
# Unit test for function register
def test_register():  # pragma: no cover
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:41.064256
# Unit test for function register
def test_register():
    # Reset the codec registry
    codecs.reset()
    # Register the eutf8h codec
    register()
    # Verify the codec was registered
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:30:43.908035
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    from . import _test_eutf8h_codec_impl
    register()
    _test_eutf8h_codec_impl.test_eutf8h_codec_impl(NAME)

# Generated at 2022-06-13 20:30:45.137030
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:30:47.699628
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore



# Generated at 2022-06-13 20:30:49.033229
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:30:53.850366
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    obj = codecs.getdecoder(NAME)
    assert obj is not None


if __name__ == '__main__':
    register()
    test_register()