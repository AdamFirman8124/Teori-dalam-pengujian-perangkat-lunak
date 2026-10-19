

# Generated at 2022-06-13 20:21:50.124000
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:21:58.071049
# Unit test for function register
def test_register():
    register()
    c = codecs.getdecoder(NAME)
    assert c is not None


if __name__ == "__main__":
    # Run unit tests
    test_register()
    codecs.register(_get_codec_info)
    print('Testing decode(...):')
    s = b'\\x48\\x65\\x6c\\x6c\\x6f\\x20\\x77\\x6f\\x72\\x6c\\x64'
    print(s)

    print(decode(s))
    s = b'\\x00\\x01\\x02\\x03'
    print(s)
    print(decode(s))

# Generated at 2022-06-13 20:22:01.390967
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    try:
        codecs.getdecoder(NAME)
    except LookupError as _:
        raise AssertionError
    return

# Generated at 2022-06-13 20:22:02.785766
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME)



# Generated at 2022-06-13 20:22:05.739314
# Unit test for function register
def test_register():
    codecs.getdecoder(NAME)  # Shouldn't raise a LookupError
    codecs.register(_get_codec_info)  # Shouldn't raise an AssertionError


# Generated at 2022-06-13 20:22:07.089684
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore



# Generated at 2022-06-13 20:22:10.105304
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)   # type: ignore


# Generated at 2022-06-13 20:22:13.974569
# Unit test for function register
def test_register():
    # Make sure the codec is not registered before calling register.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        register()
        codecs.getdecoder(NAME)
        return
    else:
        raise LookupError('Codec already registered.')

# Generated at 2022-06-13 20:22:19.635058
# Unit test for function register
def test_register():
    original = sys.getdefaultencoding()
    sys.setdefaultencoding('utf-8')
    old = codecs.lookup(NAME)
    register()
    new = codecs.lookup(NAME)
    assert old != new
    sys.setdefaultencoding(original)



# Generated at 2022-06-13 20:22:33.905050
# Unit test for function register
def test_register():
    from sys import version_info
    if version_info.major == 3 and version_info.minor == 6:
        # Registering and unregistering for python3.6 does not work.

        # register()
        # assert codecs.getencoder(NAME) is not None
        # assert codecs.getdecoder(NAME) is not None
        #
        # codecs.unregister(_get_codec_info)
        # try:
        #     codecs.getencoder(NAME)
        # except LookupError:
        #     codecs.getdecoder(NAME)
        #     assert True
        # else:
        #     assert False
        assert True
    else:
        try:
            codecs.getencoder(NAME)
        except LookupError:
            assert True
            register()
            assert codec

# Generated at 2022-06-13 20:22:51.269614
# Unit test for function register
def test_register():

    # Escape the utf-8 string 'Über' which is 'U\u0308ber' in
    # python.
    #
    # The code below produces the following output::
    #
    #     b'U\\xcc\\x88ber'
    #     Über
    #
    register()

    str_input = 'U\u0308ber'
    str_input_escaped = 'U\\u0308ber'

    # Escape the string 'Über' that has been converted to unicode.
    str_input_escaped_bytes = str_input_escaped.encode(NAME)
    str_input_escaped_bytes_reverted = str_input_escaped_bytes.decode(NAME)

    # Check that the string is the same
    assert str_input_escaped

# Generated at 2022-06-13 20:22:52.976236
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:22:53.945550
# Unit test for function register
def test_register():
    register()
    return



# Generated at 2022-06-13 20:22:56.114429
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)

# Generated at 2022-06-13 20:22:58.339554
# Unit test for function register
def test_register():
    register()
    codec_info = codecs.getdecoder(NAME)  # type: ignore
    assert codec_info.name == NAME


if __name__ == "__main__":
    test_register()

# Generated at 2022-06-13 20:23:00.659254
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:23:13.804444
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        print(f'Registering codec: {NAME}')
        codecs.register(_get_codec_info)   # type: ignore
        print(f'Registering codec: {NAME}')
    else:
        print(f'Codec: {NAME} has already been registered')


# test_register()

#
# def main():
#     """The main function.
#     """
#     test_register()
#
#
# if __name__ == '__main__':
#     main()

# Generated at 2022-06-13 20:23:22.929061
# Unit test for function register
def test_register():
    sys_modules = sys.modules[__name__]
    codecs = sys_modules.__getattribute__('codecs')
    register = sys_modules.__getattribute__('register')
    getencoder = codecs.__getattribute__('getencoder')
    getdecoder = codecs.__getattribute__('getdecoder')
    NAME = sys_modules.__getattribute__('NAME')
    getencoder(NAME)
    getdecoder(NAME)
    assert True



# Generated at 2022-06-13 20:23:25.257841
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup_error(NAME).__name__ == 'lookup_error'

# Generated at 2022-06-13 20:23:30.243958
# Unit test for function register
def test_register():
    """Test that the codec was registered"""

    # Remove the codec from the global codec dictionary.
    # This is used to ensure that the codec was registered.
    if NAME in codecs.__dict__['_cache']:
        del codecs.__dict__['_cache'][NAME]

    # Register the codec
    register()

    # Get the codec.
    codecs.getdecoder(NAME)

# Test for function encode

# Generated at 2022-06-13 20:23:43.018210
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['_cache']
    assert NAME in codecs.__dict__['_unknown']
    assert codecs.getdecoder(NAME) is not None
    assert codecs.getencoder(NAME) is not None


# Generated at 2022-06-13 20:23:45.471950
# Unit test for function register
def test_register():
    register()

    assert codecs.getdecoder(NAME) is not None


# Generated at 2022-06-13 20:23:51.868359
# Unit test for function register
def test_register():
    """Unit test for function 'register()'."""

    # Check that the codec is registered.
    try:
        codecs.getdecoder(NAME)
        msg = 'codec already registered'
        assert False, msg
    except LookupError:
        pass

    # Try to register the codec.
    register()

    # Check that the codec is registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        msg = 'failed to register codec'
        assert False, msg

    print('test_register(): Ok')



# Generated at 2022-06-13 20:23:54.729286
# Unit test for function register
def test_register():

    # Register the codec
    register()

    # Verify the codec is registered.
    codec = codecs.getdecoder(NAME)
    assert NAME == codec.__name__

# Generated at 2022-06-13 20:23:55.846177
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:23:58.796090
# Unit test for function register
def test_register():
    assert NAME == 'eutf8h'
    register()
    codecs.getdecoder(NAME)
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:24:01.236066
# Unit test for function register
def test_register():
    print('')
    print('Testing register')
    print('----------------')
    register()



# Generated at 2022-06-13 20:24:02.966329
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)  # should not raise.



# Generated at 2022-06-13 20:24:04.220267
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:24:05.610749
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        assert False, f'({NAME}) should be a registered codec: {e}'


# Generated at 2022-06-13 20:24:23.136684
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)

# Generated at 2022-06-13 20:24:28.011350
# Unit test for function register
def test_register():
    register()
    try:
        codecs.getdecoder(NAME)
    except LookupError as e:
        print('FAILED: %s' % str(e))
        sys.exit(1)


# Unit tests for function encode

# Generated at 2022-06-13 20:24:36.742328
# Unit test for function register
def test_register():
    register()

    utf8h = codecs.getdecoder(NAME)
    assert utf8h is not None

    bytes_in = b'\\x40\\xff'
    str_out, num_in_used = utf8h(bytes_in)
    str_good = '@\u037f'
    assert str_out == str_good
    assert num_in_used == len(bytes_in)

# Generated at 2022-06-13 20:24:39.780194
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    """
    >>> test_register()
    >>> import codecs
    >>> codecs.getdecoder('eutf8h')
    <function decode at 0x...>
    """
    register()



# Generated at 2022-06-13 20:24:47.435815
# Unit test for function register
def test_register():
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        pass
    else:
        assert False, "Codec was already registered"
    register()
    codecs.getdecoder(NAME)
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        assert False, (
            "Codec registration failed, "
            "getdecoder was not defined after register"
        )

# Generated at 2022-06-13 20:24:49.061031
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:24:51.467025
# Unit test for function register
def test_register():
    """Test the function :obj:`register` by testing what happens if
    the codec info is registered twice.
    """
    register()
    register()

# Generated at 2022-06-13 20:24:53.816129
# Unit test for function register
def test_register():
    assert NAME not in codecs.__dict__['_cache']
    register()
    assert NAME in codecs.__dict__['_cache']



# Generated at 2022-06-13 20:24:54.675736
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:24:59.276758
# Unit test for function register
def test_register():
    if NAME in codecs.__dict__['_cache']:
        del codecs.__dict__['_cache'][NAME]
    if NAME in codecs.__dict__['_unknown']:
        del codecs.__dict__['_unknown'][NAME]

    register()

    assert NAME in codecs.__dict__['_cache']
    assert NAME not in codecs.__dict__['_unknown']


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    import pytest
    import sys
    pytest.main(sys.argv)

# Generated at 2022-06-13 20:25:34.189290
# Unit test for function register
def test_register():
    import codecs
    register()
    codecs.getdecoder(NAME)  # should not raise LookupError

# Generated at 2022-06-13 20:25:37.307673
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert callable(decoder)
    assert NAME in set(codecs.__dict__['_cache'].keys())
    assert NAME in set(codecs.__dict__['_unknown_encoding_error'].keys())



# Generated at 2022-06-13 20:25:40.097388
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:42.664588
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.getdecoder(NAME) is not None  # type: ignore



# Generated at 2022-06-13 20:25:45.214912
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:25:48.536488
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)   # type: ignore
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:25:56.276248
# Unit test for function register
def test_register():
    # See
    # https://stackoverflow.com/questions/7578795/how-to-unittest-python-relative-imports
    import sys
    import os
    # Add the parent directory to the path.
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    NAME = 'eutf8h'
    codecs.register(lambda n: get_codec_info(n, NAME))

# Generated at 2022-06-13 20:25:57.921574
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.getdecoder('eutf8h') # type: ignore



# Generated at 2022-06-13 20:26:00.434895
# Unit test for function register
def test_register():
    # noinspection PyProtectedMember
    if NAME in codecs._cache:
        # noinspection PyProtectedMember
        del codecs._cache[NAME]
    register()

# Generated at 2022-06-13 20:26:04.372866
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:34.329687
# Unit test for function register
def test_register():
    import sys
    import doctest
    sys.path.insert(0, '.')
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    del sys.path[0]


# Generated at 2022-06-13 20:26:40.325733
# Unit test for function register
def test_register():
    import sys
    import types

    saved_sys_modules = sys.modules.copy()

    sys.modules[__name__] = types.ModuleType(__name__)
    try:
        register()
        assert NAME in codecs.getdecoder(NAME)
        assert f'{__name__}.{NAME}' in codecs.getdecoder(f'{__name__}.{NAME}')
    finally:
        sys.modules.clear()
        sys.modules.update(saved_sys_modules)
        del saved_sys_modules



# Generated at 2022-06-13 20:26:43.552138
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    assert codecs.lookup(NAME) == _get_codec_info(NAME)

register()

# Generated at 2022-06-13 20:26:51.491388
# Unit test for function register
def test_register():
    register()
    assert NAME in codecs.__dict__['_cache']
    assert NAME in codecs.__dict__['_unknown_encoding_error']
    assert NAME in codecs.__dict__['_codecs_cn']
    assert NAME in codecs.__dict__['_codecs_hk']
    assert NAME in codecs.__dict__['_codecs_iso2022']
    assert NAME in codecs.__dict__['_codecs_jp']
    assert NAME in codecs.__dict__['_codecs_kr']
    assert NAME in codecs.__dict__['_codecs_tw']
    print('register() test passed')


if __name__ == '__main__':
    test_register()

# Generated at 2022-06-13 20:26:54.780294
# Unit test for function register
def test_register():
    """Unit test for function register"""

    codecs.register = Mock()
    register()
    codecs.register.assert_called_with(_get_codec_info)


# Generated at 2022-06-13 20:26:57.769308
# Unit test for function register
def test_register():  # pragma: no cover
    register()
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:26:59.045799
# Unit test for function register
def test_register():  # pragma: no cover
    register()

# Generated at 2022-06-13 20:27:05.637294
# Unit test for function register
def test_register():
    # make sure NAME is not already registered
    first_test = True
    try:
        codecs.getdecoder(NAME)
        if first_test:
            first_test = False
            raise AssertionError(
                "NAME should not already be registered."
            )
    except LookupError:
        pass

    try:
        register()
        codecs.getdecoder(NAME)
    except LookupError:
        raise AssertionError(
            "NAME should be registered now."
        )

# Generated at 2022-06-13 20:27:08.336088
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    codecs.getencoder(NAME)
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:27:09.792315
# Unit test for function register
def test_register():
    register()
    assert codecs.lookup(NAME) is not None


# Generated at 2022-06-13 20:28:11.030150
# Unit test for function register
def test_register():
    try:
        codecs.getencoder(NAME)
    except LookupError:
        codecs.register(_get_codec_info)

    encoding = codecs.lookup(NAME)
    assert NAME == encoding.name
    assert encode == encoding.encode
    assert decode == encoding.decode


# Generated at 2022-06-13 20:28:12.940628
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME) is not None



# Generated at 2022-06-13 20:28:16.317096
# Unit test for function register
def test_register():
    register()
    decoder_info = codecs.getdecoder(NAME)

    assert isinstance(decoder_info, tuple)
    assert len(decoder_info) == 2
    assert isinstance(decoder_info[0], codecs.CodecInfo)
    assert decoder_info[1] == None



# Generated at 2022-06-13 20:28:17.245353
# Unit test for function register
def test_register():
    register()


# Generated at 2022-06-13 20:28:17.801704
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:28:21.758168
# Unit test for function register
def test_register():
    """Test the function register()."""
    from eutf8h import codec_eutf8h

    assert codecs.getdecoder('eutf8h') == codec_eutf8h.decode

# Generated at 2022-06-13 20:28:24.290013
# Unit test for function register
def test_register():
    register()
    assert codecs.getdecoder(NAME)


if __name__ == '__main__':
    test_register()
    print('Test OK')

# Generated at 2022-06-13 20:28:25.112527
# Unit test for function register
def test_register():
    register()



# Generated at 2022-06-13 20:28:27.590196
# Unit test for function register
def test_register():
    '''
    Test that the codec gets registered in the codecs library.
    '''
    # noinspection PyUnresolvedReferences
    from encodings import eutf8h
    eutf8h.register()



# Generated at 2022-06-13 20:28:31.152148
# Unit test for function register
def test_register():
    register()

    # Assert that this particular codec has been registered.
    try:
        codecs.getdecoder(NAME)
    except LookupError:
        raise



# Generated at 2022-06-13 20:30:50.430990
# Unit test for function register
def test_register():
    register()
    codecs.getdecoder(NAME)



# Generated at 2022-06-13 20:30:51.815103
# Unit test for function register
def test_register():
    _get_codec_info(NAME)



# Generated at 2022-06-13 20:30:57.637216
# Unit test for function register
def test_register():
    class MyBytes:
        def __init__(self, bytes_: bytes):
            self.bytes_ = bytes_

        def __bytes__(self):
            return self.bytes_

        def __eq__(self, other):
            return self.bytes_ == bytes(other)

    b'\xe5\xa4\xa7' == MyBytes(b'\xe5\xa4\xa7')


register()
del register



# Generated at 2022-06-13 20:31:00.899815
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)


if __name__ == '__main__':
    test_register()



# Generated at 2022-06-13 20:31:02.893097
# Unit test for function register
def test_register():
    register()
    codecs.getencoder(NAME)



# Generated at 2022-06-13 20:31:10.004344
# Unit test for function register
def test_register():
    # noinspection PyUnresolvedReferences
    """

    >>> test_register()
    True
    """
    expected = True
    actual = True
    try:
        register()
    except LookupError:
        actual = False
    finally:
        assert expected == actual


__alll__ = ['encode',
            'decode',
            'register',
            ]

# Local Variables:
# compile-command: "python3 -m pytest -v utf8h.py"
# End:

# Generated at 2022-06-13 20:31:15.920907
# Unit test for function register
def test_register():
    register()
    decoder = codecs.getdecoder(NAME)
    assert callable(decoder)
    assert decoder(b'A', 'replace') == ('A', 1)
    assert decoder(b'\xff', 'replace') == ('\ufffd', 1)
    assert decoder(b'A', 'ignore') == ('', 1)
    assert decoder(b'\xff', 'ignore') == ('', 1)



# Generated at 2022-06-13 20:31:19.896316
# Unit test for function register
def test_register():
    codecs.register(_get_codec_info)
    actual_1 = codecs.getencoder(NAME)  # type: ignore
    codecs.register(_get_codec_info)
    actual_2 = codecs.getencoder(NAME)  # type: ignore
    assert actual_1 is actual_2



# Generated at 2022-06-13 20:31:20.637314
# Unit test for function register
def test_register():
    register()

# Generated at 2022-06-13 20:31:23.972091
# Unit test for function register
def test_register():
    import codecs
    register()
    # noinspection PyTypeChecker
    codecs.getdecoder(NAME)

