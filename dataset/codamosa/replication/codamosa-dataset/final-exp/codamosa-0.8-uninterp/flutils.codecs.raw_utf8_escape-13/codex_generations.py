

# Generated at 2022-06-13 20:21:48.792967
# Unit test for function register
def test_register():
    # pylint: disable=unused-import
    import test.test_eutf8h


register()  # type: ignore

# Generated at 2022-06-13 20:21:50.401735
# Unit test for function register
def test_register():
    register()

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:21:53.077865
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Codec was not successfully registered'
    else:
        assert True



# Generated at 2022-06-13 20:21:54.606233
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore


# Generated at 2022-06-13 20:21:56.342128
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:21:59.889151
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)
    codecs.register(_get_codec_info)

# Unit tests for function encode

# Generated at 2022-06-13 20:22:01.255992
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)



# Generated at 2022-06-13 20:22:01.813225
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:22:02.631005
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None

# Generated at 2022-06-13 20:22:03.251266
# Unit test for function register
def test_register():
    _ = register
    assert True



# Generated at 2022-06-13 20:22:06.032557
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:09.144394
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        return

    raise AssertionError('Codec is already registered')



# Generated at 2022-06-13 20:22:19.717584
# Unit test for function register
def test_register():
    sys_module = sys.modules[__name__]
    codecs_module = sys.modules['codecs']
    try:
        del sys_module.eutf8h_codec_info
    except AttributeError:
        pass
    try:
        del codecs_module.eutf8h_codec_info
    except AttributeError:
        pass

# Generated at 2022-06-13 20:22:33.963886
# Unit test for function register
def test_register():

    codecs.reset_cache()

    register()

    # Check that NAME is registered in codecs.
    assert codecs.getdecoder(NAME)


test_register()

if __name__ == '__main__':
    test_register()

    # Unit test for function encode()
    input_string = 'abc¥¦+\xc4\x81\u20ac'
    expected_bytes = (b'abc\\\\xa5\\\\xa6+\\\\xC4\\\\x81\\\\u20AC')
    expected_length = 10

    actual_bytes, actual_length = encode(input_string)

    assert actual_bytes == expected_bytes
    assert actual_length == expected_length

    # Unit test for function decode()

# Generated at 2022-06-13 20:22:36.564876
# Unit test for function register
def test_register():
    # Arrange
    # Act
    register()
    # Assert
    pass



# Generated at 2022-06-13 20:22:40.265862
# Unit test for function register
def test_register():
    register()
    obj: codecs.CodecInfo = codecs.getdecoder(NAME)  # type: ignore
    assert obj.name == NAME
    assert obj.encode == encode
    assert obj.decode == decode


# Generated at 2022-06-13 20:22:46.979132
# Unit test for function register
def test_register():
    # Clear all codecs information
    codecs.clear()
    # Assert NAME codec is not registered
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)
    # Register NAME codec
    register()
    # Assert NAME codec is registered
    codecs.getdecoder(NAME)   # does not raise

# Generated at 2022-06-13 20:22:57.488580
# Unit test for function register
def test_register():
    """
    Test for the function register
    """
    # Save the current registered codecs.
    codecs_copy = codecs.__dict__['_cache'].copy()
    codecs.__dict__['_cache'].clear()

    # Load the module to test.
    # noinspection PyUnresolvedReferences
    import eutf8h

    # Execute the function to test.
    try:
        eutf8h.register()
    finally:
        # Restore the saved registered codecs.
        codecs.__dict__['_cache'].clear()
        codecs.__dict__['_cache'].update(codecs_copy)

    # Verify the results of the test.
    assert NAME in codecs.__dict__['_cache']
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:02.076603
# Unit test for function register
def test_register():
    register()
    result = codecs.getdecoder(NAME)
    assert result[0] == decode
    assert result[1] == encode


# Generated at 2022-06-13 20:23:03.201944
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:07.831112
# Unit test for function register
def test_register():
    register()

codecs.register(_get_codec_info)   # type: ignore


# Generated at 2022-06-13 20:23:10.775023
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert True
    else:
        assert False



# Generated at 2022-06-13 20:23:11.307563
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:23:14.202136
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:23:17.990955
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None  # type: ignore
    assert codecs.getencoder(NAME) is not None  # type: ignore

# Generated at 2022-06-13 20:23:19.399861
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__

# Generated at 2022-06-13 20:23:25.021505
# Unit test for function register
def test_register():
    def test_codec_info() -> None:
        register()
        # assert codecs.getencoder(NAME) == encode
        # assert codecs.getdecoder(NAME) == decode

    test_codec_info()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:30.076933
# Unit test for function register
def test_register():
    from  test_eutf8h import test_decode, test_encode

    register()

    if NAME in codecs.getencoders():
        test_encode.register_passed()
    else:
        test_encode.register_failed()

    if NAME in codecs.getdecoders():
        test_decode.register_passed()
    else:
        test_decode.register_failed()

# Generated at 2022-06-13 20:23:33.395526
# Unit test for function register
def test_register():
    register()
    obj = codecs.getdecoder(NAME)
    assert obj.decode(b'\\x61') == ('a', 2)
    import pytest

    with pytest.raises(Exception):
        codecs.getencoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:23:47.536768
# Unit test for function register
def test_register():
    import os
    import unittest
    import sys
    import codecs
    import io
    import pytest

    # Execute the unit test only if run as main module.
    # The test will fail if run as an imported module
    if __name__ == '__main__':

        try:
            codecs.getdecoder(NAME)
        except LookupError:
            # The Unicode escape codec is not registered.
            # It needs to be registered.
            codecs.register(_get_codec_info)   # type: ignore

        # Test the register function
        register()

        # Import the unittest module
        import unittest  # noqa: F401

        # Create a new Python test suite.
        suite = unittest.TestSuite()

        # Add the test case to the test suite.

# Generated at 2022-06-13 20:23:56.554475
# Unit test for function register
def test_register():
    """Tests function :func:`register`.
    """
    register()


# Generated at 2022-06-13 20:24:01.040632
# Unit test for function register
def test_register():
    import sys
    import builtins

    if NAME in sys.modules:
        del sys.modules[NAME]
    del builtins.__dict__[NAME]
    register()
    assert getattr(builtins, NAME) == sys.modules[NAME]

# Generated at 2022-06-13 20:24:04.128202
# Unit test for function register
def test_register():
    """Tests for function ``register()``."""
    register()
    # Check for the existence of the codec.
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:24:06.471047
# Unit test for function register
def test_register():

    register()

    codecs.getencoder(NAME)  # type: ignore
    codecs.getdecoder(NAME)  # type: ignore



# Generated at 2022-06-13 20:24:09.596030
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore


# Generated at 2022-06-13 20:24:11.350824
# Unit test for function register
def test_register():  # type: ignore
    register()
    assert codecs.getdecoder(NAME) is not None


register()

# Generated at 2022-06-13 20:24:20.043493
# Unit test for function register
def test_register():
    register()

if __name__ == '__main__':
    register()
    data = 'Hello world! $\u03a3$'
    encoded_data, length = codecs.encode(data, NAME)
    assert(length == len(data))
    decoded_data, length = codecs.decode(encoded_data, NAME)
    assert(length == len(encoded_data))
    assert(len(encoded_data) > len(data))
    assert(data == decoded_data)
    assert(
        encoded_data ==
        b'Hello world! \\xce\\xa3'
    )

    assert(
        codecs.decode(b'\\xce\\xa3', NAME)[0] ==
        '\u03a3'
    )


# Generated at 2022-06-13 20:24:22.545537
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:24:24.530809
# Unit test for function register
def test_register():
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:24:25.856001
# Unit test for function register
def test_register():
    # This decoder can be registered multiple times without side effects.
    register()
    register()

# Generated at 2022-06-13 20:24:44.433327
# Unit test for function register
def test_register():
    register()
    assert 'eutf8h' in codecs.encode.__code__.co_names
    assert 'eutf8h' in codecs.decode.__code__.co_names



# Generated at 2022-06-13 20:24:47.340642
# Unit test for function register
def test_register():
    str_output = []
    with redirect_stdout(str_output):
        register()

    assert len(str_output) == 0



# Generated at 2022-06-13 20:24:53.910560
# Unit test for function register
def test_register():
    # Test that the encoding codec is not registered
    with pytest.raises(LookupError):
        codecs.getencoder(NAME)    # type: ignore
    # Test that the decoding codec is not registered
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)    # type: ignore
    # Test that the encoding codec is registered
    register()
    codecs.getencoder(NAME)    # type: ignore
    # Test that the decoding codec is registered
    register()
    codecs.getdecoder(NAME)    # type: ignore
    return

# A doctest for the encoding
__test__ = {
    'test_register': test_register,
}

# Register the codec
register()

# Generated at 2022-06-13 20:24:55.807681
# Unit test for function register
def test_register():
    assert_raises(LookupError, codecs.getdecoder, NAME)
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:24:58.397230
# Unit test for function register
def test_register():
    # Force the registration of the escape utf8 hexadecimal codec
    register()
    codecs.getencoder(NAME)     # type: ignore
    codecs.getdecoder(NAME)     # type: ignore



# Generated at 2022-06-13 20:24:59.717607
# Unit test for function register
def test_register():
    """Test function register"""
    register()


if __name__ == '__main__':
    register()

# Generated at 2022-06-13 20:25:00.832371
# Unit test for function register
def test_register():
    codecs.getdecoder = lambda x : "test string"
    register()


# Generated at 2022-06-13 20:25:01.874812
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:25:03.866485
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:06.200181
# Unit test for function register
def test_register():
    register()
    # Assert that the codec is registered
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:46.633912
# Unit test for function register
def test_register():
    import codecs
    from importlib import reload
    from . import eutf8h

    reload(codecs)
    reload(eutf8h)

    assert 'eutf8h' not in codecs.__dict__
    # assert 'eutf8h' not in codecs.__dict__['_cache']
    assert 'eutf8h' not in codecs.__dict__['_unknown_encoding']
    assert NAME not in codecs.__dict__['_cache']
    assert NAME not in codecs.__dict__['_unknown_encoding']

    eutf8h.register()

    assert 'eutf8h' in codecs.__dict__['_cache']
    assert 'eutf8h' not in codecs.__dict__['_unknown_encoding']
    assert NAME not in codecs.__dict

# Generated at 2022-06-13 20:25:48.978265
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['_cache']
    assert NAME in codecs.__dict__['_unknown']



# Generated at 2022-06-13 20:25:51.037218
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder('eutf8h')

# Generated at 2022-06-13 20:25:54.921500
# Unit test for function register
def test_register():
    # FIXME: This does not work since the function register is unable
    # to register the codec.
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:56.540580
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:26:01.672607
# Unit test for function register
def test_register():

    # Check that the codec is not registered
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        assert str(e) == 'unknown encoding: %s' % NAME
    else:
        raise ValueError('codec %s is registered' % NAME)

    # Register the codec
    register()

    # Check that the codec is registered
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:05.701819
# Unit test for function register
def test_register():
    u = u'a\u1234'
    x = u.encode(NAME)
    y = x.decode(NAME)
    assert y == u

# Generated at 2022-06-13 20:26:08.192731
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:26:13.058986
# Unit test for function register
def test_register():
    del codecs.decode
    del codecs.encode

    register()

    codecs.decode(b'\x61', NAME)
    codecs.encode('a', NAME)



# Generated at 2022-06-13 20:26:23.126618
# Unit test for function register
def test_register():
    import sys
    import pytest

    # noinspection PyPackageRequirements
    from hypothesis import given
    from hypothesis.strategies import text

    from .__main__ import REASON

    # noinspection PyShadowingNames
    @given(
        text(  # type: ignore
            min_size=1,
            min_codepoint=0x0,
            max_codepoint=sys.maxunicode,
        )
    )
    def test_text_encode_decode_loop(text_input):
        bytes_out = encode(text_input)[0]
        text_out = decode(bytes_out)[0]
        assert text_out == text_input

    test_text_encode_decode_loop()


# Generated at 2022-06-13 20:26:54.504066
# Unit test for function register
def test_register():
    import sys
    import copy
    from unittest import TestCase, mock
    from unittest.mock import MagicMock

    class Test_codecs:
        def __init__(self):
            self.mockdecoder = MagicMock

    class TestRegister(TestCase):
        def setUp(self):
            self.original_codecs = copy.copy(sys.modules['codecs'])
            sys.modules['codecs'] = Test_codecs()

        def tearDown(self):
            sys.modules['codecs'] = self.original_codecs

        @staticmethod
        def test_register():
            import codecs
            codecs.mockdecoder.side_effect = LookupError
            register()
            expected_result = NAME

# Generated at 2022-06-13 20:27:05.693995
# Unit test for function register
def test_register():
    """Test function register.

    This function is tested by testing the creation of a codec,
    and looking in the codecs dictionary to see if the new codec
    is there.  I suppose that there is a way to test if the
    codecs.encode and codecs.decode functions have been created,
    but I don't know how to do that.
    """

    # Initialize the codecs before any codecs are registered.
    _get_codec_info(NAME)

    # Create a test codec object.
    codec_obj = _get_codec_info(NAME)

    # Check that the codec is there.
    assert codec_obj is not None

    # Register the codec.
    register()

    # Check that the codec is there.
    codec_enc = codecs.getencoder(NAME)  # type: ignore
   

# Generated at 2022-06-13 20:27:08.042432
# Unit test for function register
def test_register():
    import eutf8h
    eutf8h.register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:27:10.273824
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False


# Generated at 2022-06-13 20:27:14.091929
# Unit test for function register
def test_register():
    """Test function for function register"""
    import codecs

    # Register the eutf8h codec.
    register()

    # Check that the codec is now available.
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:27:14.850425
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:27:17.052476
# Unit test for function register
def test_register():
    import sys
    # register()
    assert NAME in sys.modules
    assert NAME in sys.modules['encodings'].__all__


# Generated at 2022-06-13 20:27:18.789325
# Unit test for function register
def test_register():
    register()

# Unit test

# Generated at 2022-06-13 20:27:20.909524
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()



# Generated at 2022-06-13 20:27:23.842354
# Unit test for function register
def test_register():
    """ Test function register

    """
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:27.048026
# Unit test for function register
def test_register():
    # Test that NAME does not exist in codecs
    try:
        codecs.getencoder(NAME)
        raise AssertionError(
            'Encode test failed, NAME already registered'
        )
    except LookupError:
        pass

    try:
        codecs.getdecoder(NAME)
        raise AssertionError(
            'Decode test failed, NAME already registered'
        )
    except LookupError:
        pass

    # Register NAME
    register()

    # NAME should be registered now
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

if __name__ == '__main__':
    test_register()
    test_register()

# Generated at 2022-06-13 20:28:30.327956
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:28:32.389859
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:28:37.795193
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise Exception('Could not add codec info to the codecs module.') from e
    else:
        codecs.register(_get_codec_info)  # type: ignore
    return



# Generated at 2022-06-13 20:28:40.365782
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    codecs.lookup(NAME)


# Generated at 2022-06-13 20:28:42.998174
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass



# Generated at 2022-06-13 20:28:44.983776
# Unit test for function register
def test_register():
    """

    unit test for function register

    """
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:46.881249
# Unit test for function register
def test_register():
    # Verify that the codec can be registered
    register()


# Generated at 2022-06-13 20:28:48.984089
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:28:50.558629
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:54.101109
# Unit test for function register
def test_register():
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)

# Generated at 2022-06-13 20:30:55.507704
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None   # type: ignore



# Generated at 2022-06-13 20:30:57.233616
# Unit test for function register
def test_register():
    register()
    # check that the codec is registered
    codecs.getdecoder(NAME)

# Unit tests for function decode

# Generated at 2022-06-13 20:30:58.555373
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.encode('abcabcabc', NAME)

test_register()

# Generated at 2022-06-13 20:31:03.264248
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getencoder(NAME)
    except LookupError:
        register()
    else:
        raise Exception('register() failed to register the encoding.')



# Generated at 2022-06-13 20:31:04.033231
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:31:07.173711
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert not 'registered?'



# Generated at 2022-06-13 20:31:17.860076
# Unit test for function register
def test_register():
    """Unit test for function register."""
    test_input = str(range(256))
    try:
        _ = codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore

    # Verify the codecs.decode function works as expected.
    test_expect_str = reduce(
        lambda a, b: f'{a}{b}',
        _each_utf8_hex(test_input)
    )
    test_expect_bytes = test_expect_str.encode('utf-8')
    test_actual_str, _ = codecs.decode(test_expect_bytes, NAME)

# Generated at 2022-06-13 20:31:18.667830
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:31:19.155145
# Unit test for function register
def test_register():
    register()

