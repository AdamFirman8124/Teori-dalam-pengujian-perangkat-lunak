

# Generated at 2022-06-13 20:21:55.650098
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('eutf8h').name == NAME
# codecs.lookup_error(NAME).__code__.co_filename
# codecs.lookup_error(NAME).__code__.co_filename.__module__
# codecs.lookup_error(NAME).__code__.co_filename.__code__.co_name

'''
Note:
    See the documentation of the codecs module for the following:
    - register()
    - lookup_error()
    - CodecInfo
'''


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:21:57.248753
# Unit test for function register
def test_register():
    # Ensure that we have registered the codec.
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:01.578781
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    with pytest.raises(LookupError):
        codecs.register(_get_codec_info)   # type: ignore

    codecs.lookup(NAME)



# Generated at 2022-06-13 20:22:11.620491
# Unit test for function register
def test_register():
    import tempfile
    import os

    register()
    filename = '%s.py' % __name__

    # Write the source code to a temporary file
    with tempfile.NamedTemporaryFile('w+', suffix='.py', delete=False) as fp:
        fp.write('text = "This is a test.\\xe2\\x9d\\xa4"\n')
        fp.write('text2 = "Test 2.\\xe2\\x9d\\xa4"\n')
        fp.write('text3 = "Test 3.\\xe2\\x9d\\xa4"\n')
    source_file = fp.name

    # Write the compiled file to a temporary file
    compiled_file = '%s.pyc' % fp.name

    import py_compile
    py

# Generated at 2022-06-13 20:22:16.010273
# Unit test for function register
def test_register():  # pragma: no cover
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()

if __name__ == '__main__':  # pragma: no cover
    test_register()
    print("Registered codec %s" % NAME)

# Generated at 2022-06-13 20:22:20.271819
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        raise Exception('error already registered')

    register()

    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise Exception('error not registered')



# Generated at 2022-06-13 20:22:22.766597
# Unit test for function register
def test_register():
    # Test if same function is registered multiple times
    register()
    register()



# Generated at 2022-06-13 20:22:34.502583
# Unit test for function register
def test_register():
    from codecs import getdecoder, getencoder
    register()
    encoder = getencoder(NAME)
    decoder = getdecoder(NAME)
    org_str = r'\x80\x00\x00\x00\x6f\x6e\x6c\x79\x00' \
              r'\xE2\x88\x80\x00'
    enc_str, len_org_str = encoder(org_str)
    dec_str, len_enc_str = decoder(enc_str)
    assert org_str == dec_str
    assert len_org_str == len(org_str)
    assert len_enc_str == len(enc_str)

# Generated at 2022-06-13 20:22:36.940670
# Unit test for function register
def test_register():
    import codecs
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:22:37.967697
# Unit test for function register
def test_register():
    unregister()
    register()


# Generated at 2022-06-13 20:22:45.038573
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # type: ignore

# Generated at 2022-06-13 20:22:50.802604
# Unit test for function register
def test_register():  # pragma: no cover
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        print(f'Codec "{NAME}" not registered')

    register()

    codecs.getdecoder(NAME)
    print(f'Codec "{NAME}" registered')


# Generated at 2022-06-13 20:22:52.717693
# Unit test for function register
def test_register():
    register()
    decode('%')
    decode('\\')

test_register()

# Generated at 2022-06-13 20:22:55.363058
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)



# Generated at 2022-06-13 20:22:57.742200
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:01.674120
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:23:06.644887
# Unit test for function register
def test_register():
    """Test the :func:`register` function.
    """
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:23:07.647365
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:23:09.494392
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:23:11.414989
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None
    assert codecs.getdecoder(NAME) is not None

# Generated at 2022-06-13 20:23:27.320829
# Unit test for function register
def test_register():
    # Setup
    codecs.register(_get_codec_info)   # type: ignore

    # Exercise
    s = 'x\x01x\x01x'
    out = s.encode(NAME)

    # Verify
    assert out == b'x\x01x\x01x'



# Generated at 2022-06-13 20:23:33.637076
# Unit test for function register
def test_register():
    import sys
    import pytest
    del sys.modules['eutf8h']
    from eutf8h import register
    from eutf8h import eutf8h
    register()
    assert eutf8h.getregentry() is not None
    with pytest.raises(LookupError):
        del sys.modules['eutf8h']
        from eutf8h import register
        register()



# Generated at 2022-06-13 20:23:36.237857
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:23:40.174126
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__['_cache']
    register()
    assert NAME in codecs.__dict__['_cache']
    # codecs.__dict__['_cache'].pop(NAME)

# Generated at 2022-06-13 20:23:41.482967
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:23:50.186363
# Unit test for function register
def test_register():
    # Unregister, to remove any previous registrations
    codecs.unregister(NAME)

    # Perform the function to be tested
    register()

    # Get the encoded text
    from . import _SAMPLE_TEXT
    encoded = _SAMPLE_TEXT.encode(NAME, 'strict')

    # Get the decoded text
    decoded = encoded.decode(NAME, 'strict')

    # If the sample text was not decoded correctly, then the test fails
    assert decoded == _SAMPLE_TEXT, 'Test failed'



# Generated at 2022-06-13 20:23:53.812682
# Unit test for function register
def test_register():
    import sys

    for name in NAME, NAME.lower(), NAME.upper():
        try:
            sys.modules[__name__].__loader__.load_module(name)
        except ImportError:
            continue
        else:
            # print('ImportError not raised.')
            return 1

    # print('ImportError raised. OK.')
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print('register():', test_register())

# Generated at 2022-06-13 20:23:57.383002
# Unit test for function register
def test_register():
    test_get_codec_info()
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError(str(e))



# Generated at 2022-06-13 20:24:00.678559
# Unit test for function register
def test_register():
    register()
    # noinspection PyPackageRequirements
    import codecs
    codec = codecs.getdecoder(NAME)
    assert codec



# Generated at 2022-06-13 20:24:03.609109
# Unit test for function register
def test_register():
    """Verify that the custom codec is registered."""
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        raise AssertionError from e


# Generated at 2022-06-13 20:24:29.515305
# Unit test for function register
def test_register():
    try:
        long_string = "Happy testing.\n" * 5000
        encoded_string = encode(long_string)[0]
        decoded_string = decode(encoded_string)[0]
        assert long_string == decoded_string
    except LookupError:
        pass

# Register the codec
register()

# Generated at 2022-06-13 20:24:32.114725
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error('eutf8h') == (decode, encode)

test_register()

# Generated at 2022-06-13 20:24:33.987254
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:24:35.366696
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:39.142849
# Unit test for function register
def test_register():
    NAME = 'eutf8h'
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:24:40.953556
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore

# Generated at 2022-06-13 20:24:43.778063
# Unit test for function register
def test_register():
    register()
    expected = 'eutf8h'
    actual = codecs.getdecoder(expected)
    assert expected == actual

# Generated at 2022-06-13 20:24:45.522584
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME).name == NAME

# Generated at 2022-06-13 20:24:46.114437
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:24:49.963815
# Unit test for function register
def test_register():
    import codecs
    try:
        codecs.getdecoder('eutf8h')
    except LookupError:
        register()
        codecs.getdecoder('eutf8h')
        codecs.getencoder('eutf8h')
        assert True



# Generated at 2022-06-13 20:25:04.358745
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__  # pylint: disable=no-member



# Generated at 2022-06-13 20:25:10.218228
# Unit test for function register
def test_register():
    old_registry: Optional[str] = None
    try:
        old_registry = codecs.register(None)
        register()
        assert NAME in codecs.lookup(NAME).name
    finally:
        if old_registry:
            codecs.register(old_registry)


register()

# Unit tests for function encode
# noinspection PyUnusedLocal

# Generated at 2022-06-13 20:25:14.975838
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, 'Failed to register codec eutf8h!'

# Create a codecs.CodecInfo type object 'obj' and register it.
obj = _get_codec_info(NAME)
codecs.register(obj)   # type: ignore


# Let the codecs.CodecInfo type object 'obj' be used to get the codec
# encoding class 'eutf8h_codec'.

# Generated at 2022-06-13 20:25:16.912160
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:22.992299
# Unit test for function register
def test_register():
    register()
    out = codecs.decode('\\x41', 'eutf8h')
    assert out[0] == 'A'
    assert out[1] == 5
    out = codecs.decode(b'\\x41', 'eutf8h')
    assert out[0] == 'A'
    assert out[1] == 5



# Generated at 2022-06-13 20:25:24.218032
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)    # type: ignore

# Generated at 2022-06-13 20:25:26.411395
# Unit test for function register
def test_register():
    assert NAME not in codecs.__all__
    register()
    assert NAME in codecs.__all__



# Generated at 2022-06-13 20:25:36.620418
# Unit test for function register
def test_register():
    from os import environ
    from os.path import dirname
    from os.path import join

    from pytest import raises

    from eutf8h import NAME

    from eutf8h.main import cli

    # -- Given:
    # Unit test for function register
    # The name of the directory that holds this file.
    here_path = dirname(__file__)

    # The path to this file.
    this_file_path = __file__

    # The path to the file that holds the unit test for function register.
    this_file_name = this_file_path.split('/')[-1]

    # The path to the file that is used to test eutf8h register functionality.
    test_file_path = join(here_path, 'test', 'test_eutf8h_register.py')

# Generated at 2022-06-13 20:25:39.960992
# Unit test for function register
def test_register():
    from codecs import lookup
    _get_codec_info(NAME)
    assert lookup(NAME) is not None

register()

# Unit tests

# Generated at 2022-06-13 20:25:41.701891
# Unit test for function register
def test_register():
    register()
    codecs.lookup_error('eutf8h')

# Generated at 2022-06-13 20:26:06.761982
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:26:07.590121
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:26:10.240834
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:15.299926
# Unit test for function register
def test_register():

    # Initialize the following 'result' variable to None.
    result: Optional[Exception] = None

    # Test for a successful registration
    try:
        register()
    except Exception as e:
        result = e

    if result is not None:
        raise result



# Generated at 2022-06-13 20:26:18.041239
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)  # type: ignore
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    register()

# Generated at 2022-06-13 20:26:20.370653
# Unit test for function register
def test_register():
    NAME = 'eutf8h'
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:25.847304
# Unit test for function register
def test_register():
    class Test:
        def __init__(self) -> None:
            self.register = register
            self.NAME = NAME
    test = Test()
    try:
        test.register()
    except LookupError:
        assert test.NAME == NAME
        codecs.register(_get_codec_info)  # type: ignore


try:
    codecs.getdecoder(NAME)
except LookupError:
    register()

# Generated at 2022-06-13 20:26:37.257408
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore

# Example strings.
#
# Not all of these examples are valid escape sequences. For example,
# '\\x220' should be '\\x22' or '\\x20' since '\\x20' refers to a
# space. '\\x2' is invalid since it refers to a utf8 byte that is too
# small. However, these examples are necessary to test different edge
# cases.

# Generated at 2022-06-13 20:26:39.245682
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:26:44.016270
# Unit test for function register
def test_register():
    # Save the current codecs
    old_codecs = codecs.codecs
    # Register the codec
    register()
    # Make sure that it shows up
    assert 'eutf8h' in codecs.codecs
    # Restore the old codecs
    codecs.codecs = old_codecs



# Generated at 2022-06-13 20:27:41.249854
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None  # type: ignore
    assert codecs.getencoder(NAME) is not None  # type: ignore


# Generated at 2022-06-13 20:27:42.921611
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:48.023015
# Unit test for function register
def test_register():
    from imp import load_source
    import codecs
    codecs_reg = load_source('cn.codecs_reg', './codecs_reg.py')
    codecs_reg.register()  # Register is done in the function register

# Generated at 2022-06-13 20:27:48.585499
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:27:55.862241
# Unit test for function register
def test_register():
    
    # True case
    # When we don't have codec registered,
    # we expect to have no exception.
    try:
        codecs.getdecoder(NAME)
        raise AssertionError('register() failed.')
    except LookupError:
        pass
    register()
    # When we have codec registered,
    # we expect to have no exception.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError('register() failed.')
    codecs.register(_get_codec_info)  # type: ignore
    
    # False case
    # When we already have codec registered,
    # we expect to have codecs.LookupError.

# Generated at 2022-06-13 20:27:59.366874
# Unit test for function register
def test_register():
    if NAME in codecs.getregisteredencodings():

        codecs.unregister(NAME)

    register()

    assert NAME in codecs.getregisteredencodings()

    codecs.unregister(NAME)

# Generated at 2022-06-13 20:28:01.497557
# Unit test for function register
def test_register():
    register()   # type: ignore


# Generated at 2022-06-13 20:28:05.727559
# Unit test for function register
def test_register():
    # This is better than testing the __loader__ attribute of module globals
    # because is more simple, and at the same time it is no less reliable.
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:07.599918
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:28:09.989160
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    codecs.getdecoder(NAME)  # type: ignore



# Generated at 2022-06-13 20:30:13.630739
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False


# Generated at 2022-06-13 20:30:16.125762
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)
    assert 1


# Generated at 2022-06-13 20:30:22.475064
# Unit test for function register
def test_register():
    from test import support
    import unittest

    class RegisterTestCase(unittest.TestCase):

        def test_register(self):
            self.assertIsNone(
                cast(Optional[codecs.CodecInfo],
                     codecs.getdecoder(NAME)),
            )
            register()
            self.assertIsInstance(
                cast(Optional[codecs.CodecInfo],
                     codecs.getdecoder(NAME)),
                codecs.CodecInfo,
            )

    support.run_unittest(RegisterTestCase)

# Generated at 2022-06-13 20:30:25.261151
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:27.530617
# Unit test for function register
def test_register():
    # Use: export PYTHONPATH="$PWD"
    from eutf8h import register
    register()



# Generated at 2022-06-13 20:30:32.436141
# Unit test for function register
def test_register():
    from eutf8h import codec
    codec.register()
    data = 'keñ\x7f'
    try:
        data.encode(NAME)
    except LookupError:
        raise AssertionError('Cannot find codec ' + NAME)


# vim: set filetype=python ts=4 sw=4 sts=4 expandtab:

# Generated at 2022-06-13 20:30:42.250390
# Unit test for function register
def test_register():
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from _testcapi import INT_FROM_LONG
    else:
        from _testcapi import INT_FROM_LONG as _INT_FROM_LONG

    register()

    # Test for the decode function.
    assert decode(b'abc')[0] == 'abc'
    assert decode(br'\x65')[0] == 'e'
    assert decode(br'\x65\x65')[0] == 'ee'
    assert decode(br'\xe6')[0] == 'æ'
    assert decode(br'\xe6\xe6')[0] == 'ææ'
    assert decode(br'\xe6\x65')[0] == 'æe'

# Generated at 2022-06-13 20:30:43.303345
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:30:48.203850
# Unit test for function register
def test_register():
    from typing import Generator

    def _get_codec_info(name: str) -> Optional[codecs.CodecInfo]:
        return

    def _test_function_get_codec_info():
        yield NAME, _get_codec_info, None

    for name, func, expected in _test_function_get_codec_info():
        actual = func(name)
        assert actual == expected

    def _test_function_predicate():
        yield 'foo', NAME, True
        yield NAME, NAME, False

    def _test_function_codecs_register(name: str) -> Generator[None, None, None]:
        if name != NAME:
            try:
                codecs.getdecoder(NAME)
            except LookupError:
                codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:30:58.555566
# Unit test for function register
def test_register():
    import pytest
    expected: Optional[bytes] = None
    test_data: bytes = b''
    with pytest.raises(LookupError):
        actual: Optional[bytes] = codecs.decode(test_data, NAME)
    register()
    actual: Optional[bytes] = codecs.decode(test_data, NAME)
    assert actual == expected, 'codecs.decode(b'', \'eutf8h\')'
    test_data: bytes = b'\\x4A\\x4B\\x4C\\x4D\\x4E'
    expected: Optional[bytes] = b'JKLMN'
    actual: Optional[bytes] = codecs.decode(test_data, NAME)