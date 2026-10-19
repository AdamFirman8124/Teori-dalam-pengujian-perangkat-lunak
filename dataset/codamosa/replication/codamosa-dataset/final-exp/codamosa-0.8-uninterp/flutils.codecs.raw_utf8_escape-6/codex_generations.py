

# Generated at 2022-06-13 20:21:49.038926
# Unit test for function register
def test_register():
    # Make sure the codec is not already registered.
    # This can happen if function register() is called twice.
    codecs.lookup(NAME)


# Generated at 2022-06-13 20:21:50.829541
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:21:53.490568
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['_cache']
    assert isinstance(codecs.__dict__['_cache']['eutf8h'].getregentry(), codecs.CodecInfo)

# Generated at 2022-06-13 20:21:55.180840
# Unit test for function register
def test_register():
    register()
    codecs.encode('\x5f', 'eutf8h')
    codecs.decode(b'\\x5f', 'eutf8h')



# Generated at 2022-06-13 20:21:59.409028
# Unit test for function register
def test_register():
    register()
    print(codecs.lookup(NAME))
    print(NAME in codecs.getencoders())
    print(NAME in codecs.getdecoders())
    print(NAME in codecs.getincrementalencoders())
    print(NAME in codecs.getincrementaldecoders())
    print(NAME in codecs.getaliases())


if __name__ == "__main__":
    test_register()
    print(NAME)
    print('Byte:', codecs.encode(NAME, NAME))

# Generated at 2022-06-13 20:22:04.583249
# Unit test for function register
def test_register():
    # Register the codecs
    register()
    # Check the codecs were registered
    try:
        obj = codecs.getdecoder(NAME)  # type: ignore
    except LookupError:
        assert False, 'Codecs were not registered'
    # Check the codecs are the expected ones
    assert 'eutf8h' in str(obj), 'Unexpected codecs'

# Generated at 2022-06-13 20:22:06.615417
# Unit test for function register
def test_register():
    register()
    encoding_name = NAME
    result = codecs.getdecoder(encoding_name)
    assert result is not None



# Generated at 2022-06-13 20:22:11.737195
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)  # type: ignore
        # This statement must pass without raising a LookupError exception.
        codecs.getencoder(NAME)   # type: ignore


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:13.469507
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)    # no exception
    codecs.getdecoder(NAME)    # no exception



# Generated at 2022-06-13 20:22:16.344630
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:33.599172
# Unit test for function register
def test_register():
    import sys
    import _testcapi
    from types import ModuleType
    from unittest.mock import patch

    from typing import NamedTuple

    from . import codec_info

    class MockObj(NamedTuple):
        mock_get_codec_info: str
        mock_register: str
        mock_getencoder: str
        mock_getdecoder: str

    module: ModuleType = ModuleType('test_register')
    orig_paths = sys.path[:]
    orig_modules = sys.modules.copy()


# Generated at 2022-06-13 20:22:41.430656
# Unit test for function register
def test_register():
    codecs.register(codecs.CodecInfo(  # type: ignore
        name='somename',
        encode=encode,  # type: ignore[arg-type]
        decode=decode,  # type: ignore[arg-type]
    ))
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass  # codec was never registered
    else:
        raise AssertionError('Codec was already registered.')
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('Codec was not registered.')



# Generated at 2022-06-13 20:22:52.497896
# Unit test for function register
def test_register():
    register()
    # The following should not raise an exception.
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)
    codecs.lookup(NAME)
    # The following should raise an exception.
    try:
        codecs.getencoder('invalid')
    except LookupError:
        pass
    else:
        assert False
    try:
        codecs.getdecoder('invalid')
    except LookupError:
        pass
    else:
        assert False
    try:
        codecs.lookup('invalid')
    except LookupError:
        pass
    else:
        assert False



# Generated at 2022-06-13 20:22:53.454265
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:22:55.736672
# Unit test for function register
def test_register():
    import codecs
    register()
    codecs.getencoder(NAME)


# Generated at 2022-06-13 20:23:05.124875
# Unit test for function register
def test_register():
    from os import remove
    from os.path import join, exists
    from tempfile import gettempdir
    from importlib import util

    # Test step 1: check if the codec `NAME` is not registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise RuntimeError(
            'The codec %s was already registered.' % NAME
        )

    # Test step 2: register the codec `NAME`
    register()

    # Test step 3: check if the codec `NAME` is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError(
            'The codec %s was not registered.' % NAME
        )

    # Test step 4: create a temporary module
    # which contains just the line `import

# Generated at 2022-06-13 20:23:12.930436
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert(str(codecs.lookup(NAME))) ==\
        "<codecs.CodecInfo object for encoding 'eutf8h'>",\
        "Unable to register codec 'eutf8h'"
    codecs.lookup_error('eutf8h')
    codecs.lookup_error(NAME)
    codecs.lookup_error('eutf-8h')
    assert(str(codecs.lookup_error('eutf-8h'))) ==\
        "<function _get_codec_info at 0x7ff7d31e1ea0>"


# Generated at 2022-06-13 20:23:17.303890
# Unit test for function register
def test_register():
    if NAME in codecs.aliases.aliases.keys():
        del codecs.aliases.aliases[NAME]
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:20.702356
# Unit test for function register
def test_register():
    """
    :return:
    """

    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:32.533922
# Unit test for function register
def test_register():
    assert codecs.lookup(NAME) == _get_codec_info(NAME)


if __name__ == '__main__':
    register()
    print('\nTesting encode(...)')
    print(f'\n{repr(encode(u"ABC"))}: {type(encode(u"ABC"))}')
    print(f'\n{repr(encode(u"ABC"))}: {type(encode(u"ABC"))}')
    print(f'\n{repr(encode(u"ABC"))}: {type(encode(u"ABC"))}')
    print(repr(encode(u"ABC DEF")))
    print(repr(encode(u"ABC\\u20DEF")))
    print(repr(encode(u"ABC\\ud800DEF")))


# Generated at 2022-06-13 20:23:39.110398
# Unit test for function register
def test_register():
    register()
    assert NAME == codecs.getencoder(NAME)('hello')[1]
    assert 'hello' == codecs.getdecoder(NAME)(b'hello')[0]

test_register()

# Generated at 2022-06-13 20:23:45.170766
# Unit test for function register
def test_register():
    import sys
    import os
    encodings_dir = os.path.dirname(sys.path[0])
    encodings_dir = os.path.join(encodings_dir, 'encodings')
    os.chdir(encodings_dir)
    register()
    codecs.lookup(NAME)
# End unit test for function register

# Generated at 2022-06-13 20:23:49.635806
# Unit test for function register
def test_register():
    """Test that register() successfully registers codec 'eutf8h'"""
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None


# Unit Test for function encode

# Generated at 2022-06-13 20:23:53.813984
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('expected codec is not registered')


# Generated at 2022-06-13 20:23:56.149071
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError



# Generated at 2022-06-13 20:24:00.567065
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)
    name = 'eutf8h'
    codecs.getencoder(name)
    codecs.getdecoder(name)


# Generated at 2022-06-13 20:24:11.468638
# Unit test for function register
def test_register():
    from codecs import getdecoder, getencoder, register
    import io
    import sys

    assert NAME not in (
        codec.name
        for codec in codecs._aliases.aliases.values()
    )

    # Register the encode/decode functions for the NAME codec.
    register(_get_codec_info)

    # Verify that the NAME codec is registered and that it can be used.
    assert NAME in (
        codec.name
        for codec in codecs._aliases.aliases.values()
    )

    # Verify that the NAME codec decodes correctly.
    assert (
        u'\u6e2c' == getdecoder(NAME)(b'\x6e\x2c')[0]  # type: ignore
    )

    # Verify that the NAME codec encodes correctly.

# Generated at 2022-06-13 20:24:13.368564
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:24:14.101562
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:16.391625
# Unit test for function register
def test_register():
    import sys
    import codecs
    sys.modules[__name__] = sys.modules['__main__']

# Generated at 2022-06-13 20:24:22.993405
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:30.264752
# Unit test for function register
def test_register():
    # type: () -> None
    """Unit test for function register"""
    #
    # Flush the codecs cache.
    #
    keys = list(codecs.cache.keys())
    for key in keys:
        del codecs.cache[key]
    #
    # Call register. This should not raise any exceptions.
    #
    register()



# Generated at 2022-06-13 20:24:35.649609
# Unit test for function register
def test_register():
    test_data = "Hello World"
    test_bytes = test_data.encode()
    register()
    test_encoded_bytes = cast(bytes, encode(test_data)[0])
    test_decode_str = decode(test_bytes)[0]
    assert(test_data == test_decode_str)
    assert(test_bytes == test_encoded_bytes)

# Generated at 2022-06-13 20:24:37.190400
# Unit test for function register
def test_register():
    for name in ('eutf8h', NAME):
        codecs.lookup(name)

# Generated at 2022-06-13 20:24:39.811796
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None


if __name__ == '__main__':
    register_test()

# Generated at 2022-06-13 20:24:43.884510
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME).__name__
    assert NAME in codecs.getencoder(NAME).__name__

# Unit tests for function decode

# Generated at 2022-06-13 20:24:47.291186
# Unit test for function register
def test_register():
    original = codecs.lookup(NAME)
    register()
    registered = codecs.lookup(NAME)
    assert original is None and registered is not None



# Generated at 2022-06-13 20:24:48.597406
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:49.390929
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:24:50.552948
# Unit test for function register
def test_register():
    register()
    # re-registering should pass.
    register()



# Generated at 2022-06-13 20:25:08.671890
# Unit test for function register
def test_register():
    register()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:25:12.269561
# Unit test for function register
def test_register():
    """
    Unit test for function register.
    """

    assert 'eutf8h' in codecs.encode.__annotations__['return'].__args__
    assert 'eutf8h' in codecs.decode.__annotations__['return'].__args__

# Generated at 2022-06-13 20:25:14.561620
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:25:18.500318
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
        assert False
    except LookupError:
        pass
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:22.047848
# Unit test for function register
def test_register():
    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(f'Registered {NAME} but lookup failed.') from e



# Generated at 2022-06-13 20:25:23.331922
# Unit test for function register
def test_register():   # type: ignore
    register()
    name = 'eutf8h'
    codecs.getdecoder(name)
    codecs.getencoder(name)



# Generated at 2022-06-13 20:25:27.335412
# Unit test for function register
def test_register():

    try:
        codecs.getdecoder(NAME)
        raise RuntimeError('Unit test register - The NAME is already registered.')
    except LookupError:
        codecs.register(_get_codec_info)

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise RuntimeError('Unit test register - The NAME is not registered.')


# Generated at 2022-06-13 20:25:30.828019
# Unit test for function register
def test_register():
    """Test the :obj:`register` function."""

    # Call the register function.
    register()

    # Test that the encoding was registered.
    assert codecs.lookup(NAME) is not None



# Generated at 2022-06-13 20:25:31.969850
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:25:33.357796
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:26:02.018349
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    print('Success')

# Generated at 2022-06-13 20:26:06.517097
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getencoders()
    assert NAME in codecs.getdecoders()


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:18.774669
# Unit test for function register
def test_register():
    import sys

    register()
    codecs.encode(b'abc', NAME)
    codecs.decode(b'abc', NAME)

    try:
        if sys.version_info >= (3, 7):
            codecs.encode(b'\\x80', NAME)
        else:
            codecs.encode(b'\\x80', NAME)
    except UnicodeEncodeError as e:
        assert e.encoding.lower() == NAME.lower()
        assert e.object == b'\\x80'
        assert e.start == 0
        assert e.end == 4
        assert e.reason == 'invalid continuation byte'
    else:
        raise AssertionError('Expected UnicodeEncodeError')


# Generated at 2022-06-13 20:26:21.026339
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:22.716399
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:26:24.147586
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:26:27.779925
# Unit test for function register
def test_register():
    register()
    codec = codecs.lookup(NAME)
    assert codec.name == NAME
    assert codec.encode('hello')[0] == b'h\\x65\\x6c\\x6c\\x6f'
    assert codec.decode(b'h\\x65\\x6c\\x6c\\x6f')[0] == 'hello'

# Generated at 2022-06-13 20:26:38.730757
# Unit test for function register
def test_register():
    import sys
    m = sys.modules[__name__]
    if m.__name__ in sys.builtin_module_names:
        raise AssertionError(
            "Test function test_register is not available for "
            "built-in module %s" % m.__file__)

    def is_codec_in_registry(codec_name):
        for _, encoder, decoder, _ in codecs.__dict__['_cache']:
            if codec_name in (encoder, decoder):
                return True
        return False

    # Assume that the codec is not registered
    codec_name = m.NAME
    assert not is_codec_in_registry(codec_name)

    # Register the codec.
    m.register()

    # Check that the codec is registered

# Generated at 2022-06-13 20:26:41.720957
# Unit test for function register
def test_register():
    # Verify that the codec name is not yet registered.
    assert codecs.getdecoder(NAME) is None

# Generated at 2022-06-13 20:26:51.216939
# Unit test for function register
def test_register():
    testcases = [
        {
            'text': 'H\u00e9ll\u00f8 \u2603',
            'compare': 'H\\xE9ll\\xF8 \\xE2\\x98\\x83',
            'encoding': NAME,
        },
    ]
    for testcase in testcases:
        text = testcase['text']
        compare = testcase['compare']
        encoding = testcase['encoding']

        encoded_text = text.encode(encoding)
        assert isinstance(encoded_text, bytes)
        assert encoded_text == compare.encode('utf-8')

        decoded_text = encoded_text.decode(encoding)
        assert isinstance(decoded_text, str)
        assert decoded_text == compare
        assert decoded_

# Generated at 2022-06-13 20:27:49.749537
# Unit test for function register
def test_register():
    # Test if the codecs.getdecoder will succeed upon codecs.register
    # and subsequent call to codecs.getdecoder.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:27:51.867120
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:28:03.757060
# Unit test for function register
def test_register():
    import codecs
    from sys import modules

    # Test if the encoding is already defined
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        # Test if the encoding was not registered
        assert NAME not in codecs.__dict__

        # Test if the encoding was not loaded
        assert f'{__package__}.{NAME}' not in modules

        register()

        # Test if the encoding was registered
        assert NAME in codecs.__dict__

        # Test if the encoding was loaded
        assert f'{__package__}.{NAME}' in modules

    # Test if the encoding was defined
    assert NAME in codecs.__dict__

    # Test if the encoding was loaded
    assert f'{__package__}.{NAME}' in modules

    # Test if the encoding is defined

# Generated at 2022-06-13 20:28:07.671803
# Unit test for function register
def test_register():
    register()
    try:
        chr(0x1f637).encode('eutf8h')
    except LookupError:
        pytest.fail()  # pragma: no cover



# Generated at 2022-06-13 20:28:10.566346
# Unit test for function register
def test_register():
    try:
        register()
    except Exception as err:
        raise AssertionError(err)
#   Return success
    return True

if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:28:11.409647
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:28:18.675559
# Unit test for function register
def test_register():
    register()

    # Try to re-register the codec, which should be a no-op
    register()

    # Get the codec decoder and encoder
    codec_info = codecs.lookup(NAME)
    codec_decoder = cast(codecs.IncrementalDecoder, codec_info.incrementaldecoder)
    codec_encoder = cast(codecs.IncrementalEncoder, codec_info.incrementalencoder)

    # Initialize the codec encoder and decoder
    codec_decoder.setstate(None)
    codec_encoder.setstate(None)

    # Test the codec encode function
    chars_in = 'us-ascii'
    char_bytes_out, num_chars_consumed = encode(chars_in)

# Generated at 2022-06-13 20:28:21.404751
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)


# Generated at 2022-06-13 20:28:22.609530
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:28:26.009439
# Unit test for function register
def test_register():
    """Create a codecs.CodecInfo and register the codec. Makes sure that
    the codec is registered."""

    register()

    assert codecs.getdecoder(NAME) is not None


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:30:39.573547
# Unit test for function register
def test_register():
    for func_name in 'encode', 'decode':
        assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:30:41.461203
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert isinstance(codecs.getdecoder(NAME), codecs.CodecInfo)



# Generated at 2022-06-13 20:30:42.254380
# Unit test for function register
def test_register():
    register()




# Generated at 2022-06-13 20:30:45.754737
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, 'codecs.getdecoder(NAME) should have thrown a LookupError'

    register()
    test = codecs.getdecoder(NAME)  # type: ignore
    assert callable(test), 'test should be callable'


# Generated at 2022-06-13 20:30:48.154024
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:49.141614
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:30:58.925173
# Unit test for function register
def test_register():
    import sys
    register()
    assert NAME in sys.__dict__, \
        """
        The module `{NAME}` is not registered in the interpreter.
        This can happen if the module is run directly, because the
        module's 'register()' function is not called.
        """.format(NAME=NAME)
    assert sys.__dict__[NAME] == __name__, \
        """
        A module `{name}` is registered, but it is not this module.
        """.format(name=sys.__dict__[NAME])
    assert NAME in sys.modules, \
        """
        The module `{NAME}` is not registered in the interpreter.
        This can happen if the module is run directly, because the
        module's 'register()' function is not called.
        """.format(NAME=NAME)



# Generated at 2022-06-13 20:31:02.900550
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass

    register()

    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:31:04.077939
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:31:05.701563
# Unit test for function register
def test_register():
    assert NAME in codecs.__dict__['name']
