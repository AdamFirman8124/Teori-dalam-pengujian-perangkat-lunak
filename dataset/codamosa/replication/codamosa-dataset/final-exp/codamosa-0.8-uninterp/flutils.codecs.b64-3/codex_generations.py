

# Generated at 2022-06-13 20:21:49.357614
# Unit test for function register
def test_register():
    """Test the ``register`` function with Python."""
    # pylint: disable=import-outside-toplevel
    from .test import unit_test

    unit_test.register(NAME, register)


# Generated at 2022-06-13 20:21:52.195131
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    # pylint: disable=W0212
    if codecs.__dict__[NAME] is not _get_codec_info:
        register()



# Generated at 2022-06-13 20:21:59.178056
# Unit test for function encode

# Generated at 2022-06-13 20:22:09.571817
# Unit test for function encode

# Generated at 2022-06-13 20:22:19.713590
# Unit test for function register
def test_register():
    """Test the function register()."""
    import sys

    try:
        if NAME in sys.modules[__name__].__dict__:
            import importlib
            importlib.reload(sys.modules[__name__])
        else:
            import imp
            imp.reload(sys.modules[__name__])
    except AttributeError:
        import importlib
        importlib.reload(sys.modules[__name__])

    try:
        codecs.lookup_error(NAME)
    except LookupError:
        pass
    else:
        raise RuntimeError('NAME is not registered')

    register()

    try:
        codecs.lookup_error(NAME)
    except LookupError:
        raise RuntimeError('NAME is not registered')



# Generated at 2022-06-13 20:22:25.076573
# Unit test for function register
def test_register():
    """Test the function :func:`register`."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:37.983705
# Unit test for function encode
def test_encode():
    assert encode('a GVzdA==') == (b'a Test', 7)
    assert encode(b'a GVzdA==') == (b'a Test', 7)
    assert encode('a GVzdA==') == (b'a Test', 7)
    assert encode('\t a \nGVzdA==') == (b'a Test', 7)
    assert encode('aGVsbG8gd29ybGQ=') == (b'hello world', 12)
    assert encode('aGVsbG8gd29ybGQ=\r\n') == (b'hello world', 13)
    assert encode('aGVsbG8gd29ybGQ=\n') == (b'hello world', 13)

# Generated at 2022-06-13 20:22:50.084510
# Unit test for function encode
def test_encode():
    assert encode('a') == (b'YQ==\n', 2)
    assert encode('ab') == (b'YWI=\n', 3)
    assert encode('abc') == (b'YWJj\n', 4)
    assert encode('a'*32) == (b'YQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQYQ==\n', 66)


# Generated at 2022-06-13 20:22:56.428932
# Unit test for function register
def test_register():
    """Unit Test for function :func:`docutils_pygments_lexer.utils.b64_codec.register`
    """
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        assert codecs.getdecoder(NAME) is not None


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:22:59.469861
# Unit test for function register
def test_register():
    """
    The function register is called when the register function is imported.
    """
    register()

# Generated at 2022-06-13 20:23:04.676357
# Unit test for function register
def test_register():  # type: ignore
    """Unit test register function."""
    register()
    codecs.getdecoder(NAME)  # type: ignore


# Generated at 2022-06-13 20:23:12.879610
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    # pylint: disable=protected-access
    # pylint: disable=W0212
    assert NAME not in codecs._get_codec_cache()
    register()
    assert NAME in codecs._get_codec_cache()
    register()
    assert NAME in codecs._get_codec_cache()

# Generated at 2022-06-13 20:23:18.829821
# Unit test for function encode
def test_encode():
    assert encode('Ig==') == (b'Hi', 4)
    assert encode('') == (b'', 0)
    assert encode('Ig=') == (b'Hi', 3)
    assert encode('Ig') == (b'Hi', 2)
    assert encode('Ig') == encode('Ig=')
    assert encode('I') == (b'H', 1)
    assert encode('I') == encode('I=')
    assert encode('I') != encode('Ig=')
    assert encode('Ig==') != encode('Ig=')



# Generated at 2022-06-13 20:23:22.866848
# Unit test for function register
def test_register():
    """Test the function register()."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:23:33.321539
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore


register()


if __name__ == '__main__':
    from typing import List

    from pytest import main  # type: ignore
    from sphinx.application import Sphinx

    __doc__ = __doc__

    def _sphinx_app_fake(app):
        """Fake the sphinx application.

        This would be referenced by sphinx, but we don't care.  We just
        need this to exist to make :func:`~test_register` pass.

        Args:
            app (:obj:`~Sphinx`): The Sphinx fake application object.
        """
        pass

    args: List[str] = []

# Generated at 2022-06-13 20:23:37.703745
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:23:44.062282
# Unit test for function register
def test_register():
    """Unit test for ``register`` function."""
    codecs.register(_get_codec_info)
    assert NAME in codecs.getencodings()
    assert NAME in codecs.getdecodings()
    assert str.encode(NAME, NAME) == b'SGVsbG8gV29ybGQ='



# Generated at 2022-06-13 20:23:45.910243
# Unit test for function encode
def test_encode():
    assert encode('V=') == (b'u', 2)

# Generated at 2022-06-13 20:23:48.217264
# Unit test for function register
def test_register():
    """Unit test for method ``register``."""
    codecs.register(_get_codec_info)   # type: ignore

# Generated at 2022-06-13 20:23:51.157816
# Unit test for function register
def test_register():
    """
    >>> register()
    >>> codecs.getdecoder(NAME)
    (<function decode at ...>, <function encode at ...>)
    """



# Generated at 2022-06-13 20:23:55.078314
# Unit test for function register
def test_register():                # pragma: no cover
    register()
    assert codecs.getencoder(NAME) != None
    assert codecs.getdecoder(NAME) != None

# Generated at 2022-06-13 20:23:59.959283
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder(NAME)()


if __name__ == '__main__':
    print('Executing doctest.')
    import doctest

    doctest.testmod()
    print('Executing unit tests.')
    test_register()

# Generated at 2022-06-13 20:24:10.948546
# Unit test for function register
def test_register():  # type: ignore[misc]
    """Test the :py:func:`register` function."""
    from b64codec.exceptions import CodecAlreadyRegistered

    def _test_get_codec_info(
            name: str,
            decoder: Optional[codecs.CodecInfo],
            encoder: Optional[codecs.CodecInfo]
    ) -> None:
        if name != NAME:
            return
        d = codecs.getdecoder(NAME)
        e = codecs.getencoder(NAME)
        assert d is not None
        assert e is not None
        assert e == encoder
        assert d == decoder


# Generated at 2022-06-13 20:24:12.539893
# Unit test for function register
def test_register():
    """"""
    register()
    assert NAME in codecs.getdecoder('b64')  # type: ignore

# Generated at 2022-06-13 20:24:19.415305
# Unit test for function encode
def test_encode():
    # Test by detaching the encode function from this file and calling it
    # directly.
    from b64_codec.b64 import encode

# Generated at 2022-06-13 20:24:34.142435
# Unit test for function encode
def test_encode():
    # Test case 1.
    test_input = b'''
    SSBsb3ZlIEF6dXJlIFN0eWxlIFBhcnQgMTE6IEV2ZW50IFRyYXZlbHMgJiBFdmVudCBTdHJpbmcg
    ZW1wbG95ZWVzLiBJcyBoaXMgc2NlbmFyaW8gdHJ1ZT8=
    '''
    expected = b'''
    I love Azure Style Part 11: Event Travels & Event String employees. Is his
    scenario true?
    '''

# Generated at 2022-06-13 20:24:38.461165
# Unit test for function register
def test_register():
    obj = _get_codec_info(NAME)
    assert obj is not None
    before = obj.getdecoder('test')
    assert before is None
    register()
    after = obj.getdecoder('test')
    assert after is not None


# noinspection PyDefaultArgument

# Generated at 2022-06-13 20:24:39.929274
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:24:43.116735
# Unit test for function register
def test_register():
    """Test the :func:`register` function."""
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:50.620751
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)


if __name__ == "__main__":
    print(decode('ABE'))
    print(decode('QQFC'))
    print(decode('QQ=='))
    print(decode(''))
    print(encode('ABE'))
    print(encode('QQFC'))
    print(encode('QQ=='))
    print(encode(''))

# Generated at 2022-06-13 20:24:55.510722
# Unit test for function register
def test_register():
    """Test the function ``register``."""
    register()
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None
    assert decoder[0].__name__ == 'decode'
    assert decoder[1].__name__ == 'decode'



# Generated at 2022-06-13 20:25:01.367911
# Unit test for function register
def test_register():
    name = __name__.split('.')[-1]
    # Register the codec and retrieve the 'codecs' object.
    register()
    codecs.getdecoder(name)


if __name__ == '__main__':
    # Run the unit tests.
    test_register()

### END b64codec.py

### BEGIN b64incrementer.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Increment a base64 encoded string, returning the incremented string."""
import sys
from typing import Union

from b64codec import decode, encode

_STR = Union[str, bytes]



# Generated at 2022-06-13 20:25:02.423096
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:25:09.002900
# Unit test for function register
def test_register():
    """Unit test for registering the codec with Python."""
    original_decoder = codecs.getdecoder(NAME)
    try:
        codecs.unregister_error(NAME)
    except LookupError:
        pass
    assert original_decoder is None or original_decoder.name != NAME
    register()
    assert codecs.getdecoder(NAME).encode.__name__ == encode.__name__



# Generated at 2022-06-13 20:25:10.867249
# Unit test for function register
def test_register():
    """Test for function 'register'."""
    register()
    assert NAME in codecs.getencodings()



# Generated at 2022-06-13 20:25:13.646808
# Unit test for function register
def test_register():
    """Test that the b64 codec is registered."""
    register()
    codecs.getdecoder(NAME)


# Generated at 2022-06-13 20:25:25.315719
# Unit test for function encode
def test_encode():
    """Test the function :func:`encode`."""
    input_str = 'PDwKU0lHTl9TVEFSVCA9IDEuMTsKU0lHTl9FTkQgPSAxLjI7CkFERElO'

# Generated at 2022-06-13 20:25:34.489704
# Unit test for function register
def test_register():
    """Call the __name__ + '.register' function.

    The test_register() function is only used for the unit test.  This function
    is not used in production.  In this file, the register() function is also
    called at the end of this module.  The unit test does not call the
    register() function at the bottom of this module.  Instead, the unit test
    calls the register() function from the importable module.
    """
    register()


# Import the register function into the current namespace.
register()


# pylint: disable=C0103,W0106,W0122
# noinspection PyUnreachableCode,PyUnboundLocalVariable

# Generated at 2022-06-13 20:25:39.599102
# Unit test for function register
def test_register():
    """Unit test for function register."""
    register()
    codecs.getdecoder(NAME)


__all__ = [
    'NAME',
    'decode',
    'encode',
    'register',
    'test_register',
]

# Generated at 2022-06-13 20:25:50.081167
# Unit test for function register
def test_register():
    """Test the function register()."""
    import sys
    import types
    register()
    if 'b64' not in sys.modules[__name__].__dict__:
        raise AssertionError(
            'The codec b64 is not in the module.'
        )
    else:
        codecs.lookup(NAME)
        codecs.getdecoder(NAME)
        codecs.getencoder(NAME)
        assert isinstance(
            sys.modules[__name__].__dict__['b64'],
            types.ModuleType
        )
        assert isinstance(
            codecs.CodecInfo,
            type(sys.modules[__name__].__dict__['b64'].CodecInfo)
        )

# Generated at 2022-06-13 20:25:54.493587
# Unit test for function register
def test_register():
    """Unit test for ``b64.register()``."""
    register()
    assert NAME in codecs.getdecoder('b64')



# Generated at 2022-06-13 20:25:55.748985
# Unit test for function register
def test_register():
    """Test register"""
    register()



# Generated at 2022-06-13 20:26:03.878768
# Unit test for function register
def test_register():
    # pylint: disable=protected-access
    # pylint: disable=unused-variable
    # Register the 'b64' codec with python.
    register()

    # Verify the codec exists.
    func_decode = codecs.getdecoder(NAME)
    func_encode = codecs.getencoder(NAME)
    assert func_decode is not None
    assert func_encode is not None

    # Verify the codec functions exist and they meet the interface
    # requirements.
    try:
        func_decode(b'YQ==')
        func_encode('a')
    except Exception as e:
        raise AssertionError(
            'The codecs functions do not meet the interface requirements.'
            f'  {e}'
        )


test_register()

# Generated at 2022-06-13 20:26:10.661085
# Unit test for function register
def test_register():
    """Test the register function."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:26:18.389617
# Unit test for function encode
def test_encode():
    """Test function `encode`"""
    assert encode(b'abcde')[0] == b'YWJjZGU='
    assert encode(b'abcde\n')[0] == b'YWJjZGU='
    assert encode(b'abcde\n', 'strict')[0] == b'YWJjZGU='
    assert encode(b'abcde\n')[1] == 6
    assert encode(b'abcde\n')[1] == 6
    assert encode(b'abcde')[1] == 5


# Generated at 2022-06-13 20:26:27.551666
# Unit test for function encode
def test_encode():
    r"""
    Test function encode().

    If a unit test fails, then print the following to the console:

        * The data used for the unit test.
        * The expected result.
        * The actual result, which is the exception when running encode().
    """

    # Create a dictionary of unit test data
    data = {
        "JGVsbG8gd29ybGQ=" : b"Hello world",
        "dGVzdA==" : b"test",
        "dGVzdCB3b3JsZA==" : b"test world"
    }

    # For each dictionary item, use encode to convert a base64 character
    # string into UTF-8 bytes.  Compare the returned bytes with the expected
    # bytes.


# Generated at 2022-06-13 20:26:30.633907
# Unit test for function register
def test_register():
    register()
    assert codecs.getencoder(NAME) is not None



# Generated at 2022-06-13 20:26:33.633191
# Unit test for function register
def test_register():
    """Test function :meth:`~register`"""
    with mock.patch('codecs.register') as m_register:
        register()
        m_register.assert_called_once()



# Generated at 2022-06-13 20:26:37.249794
# Unit test for function register
def test_register():
    """Unit test for function ``register``"""
    register()
    assert codecs.getencoder(NAME)[0](b'abc') == (b'YWJj', 3)
    assert codecs.getdecoder(NAME)[0]('YWJj') == ('abc', 3)


register()

# Generated at 2022-06-13 20:26:42.003941
# Unit test for function register
def test_register():
    """Unit test for function register."""
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        codecs.unregister(NAME)  # type: ignore

    register()
    try:
        codecs.getdecoder(NAME)  # type: ignore
    except LookupError:
        assert False, \
            'Failed to register the b64 codec.'
    else:
        assert True, \
            'Succeded in registering the b64 codec.'



# Generated at 2022-06-13 20:27:01.555165
# Unit test for function register

# Generated at 2022-06-13 20:27:11.264335
# Unit test for function register
def test_register():
    """Test the register() function."""
    from codecs import getdecoder, getencoder

    # Assert that the 'b64' codec isn't installed.
    with pytest.raises(LookupError):
        codec = getencoder('b64')

    # Install the 'b64' codec.
    register()

    # Assert that  the 'b64' codec is now installed.
    codec = getencoder('b64')
    assert codec

    # Assert that the 'b64' codec is installed.
    codec = getdecoder('b64')
    assert codec


if __name__ == '__main__':
    register()
    print('The b64 codec is installed.')

# Generated at 2022-06-13 20:27:15.494289
# Unit test for function register
def test_register():  # pragma: no cover
    # pylint: disable=global-statement
    global NAME

    NAME = 'test_register'

    # Register the codec.
    register()

    # Get the decoder to ensure it was registered properly.
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:27:27.201519
# Unit test for function encode
def test_encode():
    """Test the encode function."""

# Generated at 2022-06-13 20:27:31.445038
# Unit test for function register
def test_register():
    """Unit test for function ``register``."""
    import sys
    sys.modules.pop('b64_codec', None)
    import b64_codec   # noqa: F401



# Generated at 2022-06-13 20:27:38.121303
# Unit test for function register
def test_register():
    """Test the ``register`` function."""
    import sys
    if hasattr(sys.modules[__name__], 'codec_registrar'):
        del sys.modules[__name__].codec_registrar
        del sys.modules[__name__].codecs

    import base64
    from binascii import Error
    import codecs

    import b64


# Generated at 2022-06-13 20:27:47.216305
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__all__
    decoder = codecs.getdecoder(NAME)  # type: ignore
    assert decoder(b'\x00\x00\x00\x00')[0] == ''
    assert decoder(b'\x00\x00\x00\x00')[1] == 4
    assert decoder(b'')[0] == ''
    assert decoder(b'')[1] == 0

# Generated at 2022-06-13 20:27:50.309326
# Unit test for function register
def test_register():
    """Test function register()."""
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None

# Generated at 2022-06-13 20:27:54.204986
# Unit test for function register
def test_register():
    """Test the register function of module."""
    register()

    # pylint: disable=import-outside-toplevel
    import codecs

    codecs.lookup(NAME)


if __name__ == '__main__':
    import pytest

    pytest.main(args=[".", "--capture=no", "--doctest-modules", "-v"])

# Generated at 2022-06-13 20:28:01.065426
# Unit test for function register
def test_register():
    """Test the function register"""
    import sys
    import unittest

    class RegisterTests(unittest.TestCase):
        """Test Register function."""

        def test_register(self: unittest.TestCase) -> None:
            """Test Function register"""
            register()
            self.assertIn(NAME, sys.modules)

    unittest.main(verbosity=2)

# Generated at 2022-06-13 20:28:14.728567
# Unit test for function register
def test_register():
    """Test the function register."""
    codecs.register(_get_codec_info)

# Generated at 2022-06-13 20:28:16.026997
# Unit test for function register
def test_register():
    register()
    assert(codecs.lookup(NAME) is not None)


# Generated at 2022-06-13 20:28:21.455197
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # pylint: disable=C0103, R0914
    import sys
    import unittest

    class TestRegister(unittest.TestCase):
        """Test the b64.register function.

        The test is run by unittest.main which searches for any class
        that starts with Test and has a constructor that takes no
        arguments.
        """

        def setUp(self):
            """Called before each test method is run."""
            pass

        def tearDown(self):
            """Called after each test method is run."""
            pass

        def test_register(self):
            """Test the b64.register function."""
            import b64
            # Registering the codec with Python
            b64.register()
            # Get the codecs.CodecInfo object for

# Generated at 2022-06-13 20:28:24.005632
# Unit test for function register
def test_register():
    """Unit test for function register"""
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:28:29.909860
# Unit test for function encode
def test_encode():
    """Test the encode function"""
    assert encode('SGVsbG8sIHdvcmxkIQ==') == (b'Hello, world!', 18)
    try:
        encode('SGVsbG8sIHdvcmxkIQ')
    except UnicodeEncodeError as e:
        assert e.object == 'SGVsbG8sIHdvcmxkIQ'
        assert e.start == 0
        assert e.end == 17
        assert (
            str(e) ==
            r"'SGVsbG8sIHdvcmxkIQ' is not a proper bas64 character string: "
            r"Incorrect padding"
        )


# Generated at 2022-06-13 20:28:36.342448
# Unit test for function register
def test_register():
    """Unit test for register()"""
    codecs.register(_get_codec_info)
    assert NAME in codecs.getencodings()
    assert NAME in codecs.getdecodings()
    codecs.unregister(_get_codec_info)

if __name__ == '__main__':
    test_register()
    print(encode('TWFyeW8gSmVmZmVyc29uIFNlcmVrYQ=='))

# Generated at 2022-06-13 20:28:40.743049
# Unit test for function register
def test_register():
    """Test the register function."""
    # pylint: disable=import-outside-toplevel
    import codecs

    # First, register the encoding.
    register()

    # Verify that the encoding was registered.
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:28:45.090204
# Unit test for function register
def test_register():
    """Test codec registration."""
    register()
    # Get the encoder
    encoder = codecs.getencoder(NAME)
    assert encoder

    # Get the decoder
    decoder = codecs.getdecoder(NAME)
    assert decoder



# Generated at 2022-06-13 20:28:56.555744
# Unit test for function register
def test_register():
    """Test for function register"""
    tests: Tuple[str, _STR, bytes] = (
        ('b64', 'This is a test', b'VGhpcyBpcyBhIHRlc3Q\n'),
        ('b64', 'Hello World', b'SGVsbG8gV29ybGQ\n'),
        ('b64', 'Test 1 2 3', b'VGVzdCAxIDIgMw==\n'),
        ('b64', '&+/', b'Jisv\n'),
    )
    register()
    for encode_name, text, bytes_expected in tests:
        codec_info = codecs.lookup(encode_name)  # type: ignore
        if not codec_info:
            raise LookupError(encode_name)
        out, consumed = codec

# Generated at 2022-06-13 20:29:04.500632
# Unit test for function register
def test_register():
    """Unit test for function register."""
    # pylint: disable=protected-access
    if NAME in codecs.__encodings_map__ \
        and codecs.__encodings_map__[NAME] is _get_codec_info:

        # If the 'b64' codec is registered, then unregister it.
        # pylint: disable=no-member
        codecs.unregister(NAME)

    register()
    assert NAME in codecs.__encodings_map__
    assert codecs.__encodings_map__[NAME] is _get_codec_info  # type: ignore



# Generated at 2022-06-13 20:29:29.189057
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:29:36.445247
# Unit test for function encode
def test_encode():
    """Unit test for the encode function."""
    # Test for valid utf8 strings
    assert(encode('a')[0] == b'YQ==')
    assert(encode('ab')[0] == b'YWI=')
    assert(encode('abc')[0] == b'YWJj')
    assert(encode('abcd')[0] == b'YWJjZA==')
    assert(encode('\x00\x01\x02\x03\x04\x05\x06\x07')[0] ==
           b'AAECAwQFBgcICQ==')

# Generated at 2022-06-13 20:29:39.633629
# Unit test for function register
def test_register():
    """Do the type annotations for register meet mypy requirements?"""
    register()  # type: ignore[no-effect]

# Generated at 2022-06-13 20:29:49.920560
# Unit test for function register
def test_register():
    register()
    d = codecs.getdecoder(NAME)
    assert d is not None
    e = codecs.getencoder(NAME)
    assert e is not None
    s = 'aHR0cHM6Ly9zdGF0aWMudGhlYmF0b2Rvb3JzLmNvbQ=='
    b = e(s)
    assert b[0] == s.encode('ascii')
    assert b[1] == len(s)
    decoded = d(b[0])
    assert decoded[0] == s
    assert decoded[1] == len(b[0])
    assert decoded[0] == 'https://static.thebatozors.com'



# Generated at 2022-06-13 20:29:53.314960
# Unit test for function register
def test_register():
    """Unit test for function register"""
    register()
    assert codecs.getdecoder(NAME)
    assert codecs.getencoder(NAME)


# Generated at 2022-06-13 20:30:07.623006
# Unit test for function register
def test_register():
    """Unit test for the function ``register``."""
    register()
    assert NAME in codecs.getencodings()
    assert NAME in codecs.getdecodings()


# pylint: disable=C0413
# noinspection PyUnresolvedReferences
if __name__ == '__main__':
    # To automatically register
    #   >>> import base64_conversion
    #   >>> base64_conversion.register()
    test_register()

    print(codecs.decode('U2VhcmNoIGNvb2tpZSAjMS4=', 'b64'))

    print(
        codecs.encode(
            'Мама мыла раму.',
            'b64',
        )
    )

# Generated at 2022-06-13 20:30:10.365654
# Unit test for function register
def test_register():
    """Test the register function."""
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:30:21.242168
# Unit test for function register
def test_register():

    if NAME not in codecs.__all__:
        print(
            f'INFO: {NAME} codec is not yet register with Python, '
            'will now register it.'
        )
        register()

    # Test the codec.
    # The value of the string should be the base64 representation of the
    # bytes given in the 'encoded_bytes' variable.

# Generated at 2022-06-13 20:30:32.796749
# Unit test for function register
def test_register():  # pragma: no cover
    obj = codecs.getdecoder(NAME)
    assert obj  # nosec
    assert obj(b'YQ==') == ('a', 2)   # nosec
    assert obj(b'YWE=') == ('aa', 3)   # nosec
    assert obj(b'YWFh') == ('aaa', 4)   # nosec
    assert obj(b'YWFhYQ==') == ('aaaa', 6)  # nosec
    assert obj(b'YWFhYWE=') == ('aaaaa', 7)  # nosec
    assert obj(b'YWFhYWFh') == ('aaaaaa', 8)  # nosec
    assert obj(b'YWFhYWFhYQ==') == ('aaaaaaa', 10)  # nosec

# Generated at 2022-06-13 20:30:35.562723
# Unit test for function register
def test_register():
    """Test function ``register``."""
    codecs.lookup_error('not_found')
    register()
    codecs.lookup_error('b64')



# Generated at 2022-06-13 20:31:37.249977
# Unit test for function register
def test_register():
    """Test the behavior of the register() function."""
    try:
        codecs.getencoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore

    # Test that the encoder is registered.
    assert codecs.getencoder(NAME) is not None

    # Test that the decoder is registered.
    assert codecs.getdecoder(NAME) is not None

    # Reset the codecs for other tests.
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:31:38.572192
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:31:52.393678
# Unit test for function encode
def test_encode():
    """Test function 'encode'"""
