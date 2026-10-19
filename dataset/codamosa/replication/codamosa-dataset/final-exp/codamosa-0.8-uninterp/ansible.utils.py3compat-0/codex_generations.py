

# Generated at 2022-06-13 16:35:46.153955
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    class _FakeOsEnviron(MutableMapping):
        """
        Mimics os.environ.

        Functions as a dictionary where keys are byte strings and values are byte strings on
        Python2 and unicode strings on Python3.
        """
        def __init__(self, data):
            self._raw_environ = data

        def __delitem__(self, key):
            del self._raw_environ[key]

        def __getitem__(self, key):
            return self._raw_environ[key]

        def __setitem__(self, key, value):
            self._raw_environ[key] = value

        def __iter__(self):
            return self._raw_environ.__iter__()

        def __len__(self):
            return len(self._raw_environ)

   

# Generated at 2022-06-13 16:35:56.259451
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Some test values
    text_value = 'äbc'
    raw_value = to_bytes(text_value, 'utf-8')

    test_environ = _TextEnviron()

    # Return the value decoded according to the encoding
    test_environ._raw_environ['foo'] = raw_value
    assert test_environ['foo'] == text_value

    # Return the value decoded according to the encoding from the cache if available
    assert test_environ['foo'] == text_value

    # Return the value decoded according to the encoding from the cache if the raw_environ
    # itself changes
    test_environ._raw_environ['foo'] = b'foo'
    assert test_environ['foo'] == text_value



# Generated at 2022-06-13 16:35:58.676994
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    assert (env['HOME'] == u'/root' or env['HOME'] == u'C:\\Users\\Administrator')

# Generated at 2022-06-13 16:36:03.335540
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH']

    os.environ['TEST_UNIT_TEST_1-2&3'] = 'hyi hwee hoo'
    assert environ['TEST_UNIT_TEST_1-2&3'] == 'hyi hwee hoo'
    del os.environ['TEST_UNIT_TEST_1-2&3']


# Generated at 2022-06-13 16:36:06.297723
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # e.g.
    # ansible-python-shell -m os -a "env PYTHONPATH='' python -m doctest -v module_utils.six.env.py"
    environ = _TextEnviron(encoding='utf-8')
    assert environ['PYTHONPATH'] == ''

# Generated at 2022-06-13 16:36:16.593581
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test method __getitem__ of class _TextEnviron"""
    # pylint: disable=unused-argument
    _TextEnviron__getitem__ = _TextEnviron().__getitem__
    # pylint: enable=unused-argument

    _TextEnviron().__getitem__.__annotations__ == {'key': str, 'return': str}

    test_data = [
        (b'foo', 'foo'),
        ('foo', 'foo'),
        (u'foo', 'foo'),
        (b'\x00baz\x00', '\x00baz\x00'),
    ]


# Generated at 2022-06-13 16:36:25.685832
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method __getitem__ of class _TextEnviron

    :return: None
    '''
    import pytest

    if PY3:
        return

    # Both key and value are unicode
    environ[u'one'] = u'één'
    assert environ[u'one'] == u'één'
    # Only key is unicode
    environ[u'one'] = 'één'
    assert environ[u'one'] == u'één'
    # Only value is unicode
    environ['one'] = u'één'
    assert environ['one'] == u'één'
    # Neither value nor key are unicode
    environ['one'] = 'één'
    assert environ['one'] == u'één'


# Unit test

# Generated at 2022-06-13 16:36:32.025741
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    encoded = '\N{SNOWMAN}'
    decoded = u'\N{SNOWMAN}'

    # If we're not on Python3, then check that we're doing the UTF-8 decoding
    if not PY3:
        assert u'\N{SNOWMAN}' != '\N{SNOWMAN}'
        assert environ[encoded] == u'\N{SNOWMAN}'
        assert environ[decoded] == u'\N{SNOWMAN}'

# Generated at 2022-06-13 16:36:37.820834
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['a'] = 1
    assert 'a' in environ
    assert environ['a'] == '1'

    environ['b'] = u'b'
    assert 'b' in environ
    assert environ['b'] == 'b'

    environ['c'] = u'c'.encode('utf-8')
    assert 'c' in environ
    assert environ['c'] == 'c'

    environ['d'] = u'd'.encode('latin-1')
    assert 'd' in environ
    assert environ['d'] == 'd'

    environ['e'] = None
    assert 'e' in environ
    assert environ['e'] == 'None'

    environ['f'] = 0
    assert 'f' in environ

# Generated at 2022-06-13 16:36:40.249020
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    environ['a'] = 'b'
    # Exercise
    # Verify
    assert 'b' == environ['a']


# Generated at 2022-06-13 16:36:53.952291
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['ANSIBLE_TEST_KEY'] = u'PASS'
    assert environ['ANSIBLE_TEST_KEY'] == u'PASS'
    environ['ANSIBLE_TEST_KEY'] = b'PASS'
    assert environ['ANSIBLE_TEST_KEY'] == u'PASS'
    environ['ANSIBLE_TEST_KEY'] = u'ø'.encode('utf-8')
    assert environ['ANSIBLE_TEST_KEY'] == u'ø'
    environ['ANSIBLE_TEST_KEY'] = u'ø'.encode('latin-1')
    assert environ['ANSIBLE_TEST_KEY'] == u'ø'
    environ['ANSIBLE_TEST_KEY'] = 'PASS'
    assert environ['ANSIBLE_TEST_KEY'] == u'PASS'


# Generated at 2022-06-13 16:37:00.580806
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _SimpleEnviron(object):
        def __getitem__(self, key):
            return self.environ[key]

    class _ComplexEnviron(object):
        def __getitem__(self, key):
            return self.environ[key]

    class _ComplexEnviron2(object):
        def __getitem__(self, key):
            return self.environ[key]

    _complex_environ = _ComplexEnviron()
    _complex_environ2 = _ComplexEnviron2()

    _env = _TextEnviron()

    _env._raw_environ = _SimpleEnviron()
    _env._raw_environ.environ = {'a': b'1'}
    assert _env['a'] == u'1'

    _env._raw_environ = _

# Generated at 2022-06-13 16:37:04.707209
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # simple positive cases
    environ_copy = dict(environ)  # copy the original os.environ just in case things go sideways
    for key in environ.keys():
        try:
            assert isinstance(environ[key], str)
        except UnicodeDecodeError:
            raise Exception("Unexpected exception from `environ[%s]`" % key)
    # simple negative case
    try:
        environ['this_key_should_not_exist']
    except KeyError:
        pass  # pass the test
    else:
        raise Exception("Unexpected behaviour: KeyError exception not raised")
    # restore changed environment
    os.environ.clear()
    for key in environ_copy:
        os.environ[key] = environ_copy[key]



# Generated at 2022-06-13 16:37:14.755869
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['UTF8'] = 'UTF8'
    os.environ['BYTE_ASCII'] = b'BYTE_ASCII'
    os.environ['BYTE_UTF8'] = b'BYTE_UTF8'.decode('utf-8')
    os.environ['BYTE_UTF8_INVALID'] = u'\udc00'.encode('utf-8')
    os.environ['UNICODE'] = u'UNICODE'
    os.environ['UNICODE_INVALID'] = u'\udc00'
    # Normally the module_utils.six.environ object is used.  In this unit test
    # we're creating a new object to test __getitem__ on.

# Generated at 2022-06-13 16:37:24.978574
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_environ = os.environ.copy()
    os.environ.clear()
    os.environ['ANSIBLE_TEST_ENV_VAR'] = '__C_UNDER_SCORE__'
    assert environ['ANSIBLE_TEST_ENV_VAR'] == '__C_UNDER_SCORE__'
    os.environ.clear()
    os.environ['ANSIBLE_TEST_ENV_VAR'] = '__C_uNdER_ScOrE__'
    assert environ['ANSIBLE_TEST_ENV_VAR'] == '__C_uNdER_ScOrE__'
    os.environ.clear()

# Generated at 2022-06-13 16:37:27.647348
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == u'/usr/bin'
    assert environ['LANG'] == u'C'



# Generated at 2022-06-13 16:37:32.444049
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_TEXTENVIRON_UTF8'] = u'\u00EB'
    assert 'TEST_TEXTENVIRON_UTF8' in environ
    assert environ['TEST_TEXTENVIRON_UTF8'] == u'\u00EB'



# Generated at 2022-06-13 16:37:42.526106
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import json

    # Set environment variable
    os.environ['ANSIBLE'] = b'true'
    # Check that returned object is str and not bytes or unicode
    assert isinstance(environ['ANSIBLE'], str)
    assert environ['ANSIBLE'] == u'true'

    # Check that json can accept the value
    assert json.loads(environ['ANSIBLE'])

    # Change the returned type to unicode and check the result
    os.environ['ANSIBLE'] = u'true'
    assert environ['ANSIBLE'] == u'true'

    # Check that json can accept the value
    assert json.loads(environ['ANSIBLE'])

    # Change the returned type to bytes and check the result
    os.environ['ANSIBLE'] = b'true'

# Generated at 2022-06-13 16:37:45.066798
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_copy = environ.copy()
    test_key = 'TEST_KEY'
    test_value = 'TEST_VALUE'
    environ_copy[test_key] = test_value
    assert environ_copy[test_key] == test_value


# Generated at 2022-06-13 16:37:51.068454
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method __getitem__ of class _TextEnviron
    '''
    e = _TextEnviron({b'KEY-1': b'value-1', b'KEY-2': b'value-2', b'KEY-3': u'value-3'})
    assert e[b'KEY-1'] == 'value-1'
    assert e['KEY-1'] == 'value-1'
    assert e[u'KEY-1'] == 'value-1'

# Generated at 2022-06-13 16:37:59.560459
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    env = {'str': 'str', 'bytes': 'bytes'.encode()}
    expected = {'str': 'str',
                'bytes': to_text('bytes', nonstring='passthru')}

    # Act
    result = {}
    ret = _TextEnviron(env=env)
    for key in env:
        result[key] = ret[key]

    # Assert
    assert expected == result

# Generated at 2022-06-13 16:38:07.575455
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import MutableMapping

    # default encoding
    encoding = os.sys.getfilesystemencoding()

    # save old os.environ
    old_environ = os.environ

# Generated at 2022-06-13 16:38:11.482334
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """__getitem__ supports both byte and text strings as keys"""
    environ[u'foo'] = u'bar'
    assert environ[u'foo'] == u'bar'
    assert environ['foo'] == u'bar'
    assert environ[b'foo'] == u'bar'



# Generated at 2022-06-13 16:38:16.277220
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    import ansible.module_utils.environ

    # set the class variable to a dictionary
    ansible.module_utils.environ.environ_ = {'ANSIBLE_MODULE_ARGS': ''}
    # run the method __getitem__
    result = ansible.module_utils.environ.environ_[ 'ANSIBLE_MODULE_ARGS' ]
    # assert result is a string
    assert isinstance(result, str)

# Generated at 2022-06-13 16:38:28.468851
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # type: () -> None
    from six import StringIO

    ENV_VARS = {b'HOME': u'/home/badger',
                b'PWD': u'/home/badger',
                b'SHELL': u'/bin/sh',
                b'SHLVL': b'1',
                b'TERM': u'xterm'}
    environ_backup = os.environ
    os.environ = ENV_VARS

# Generated at 2022-06-13 16:38:32.385288
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['non-unicode'] = b'\xff'
    assert environ['non-unicode'] == u'\ufffd'



# Generated at 2022-06-13 16:38:39.676487
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils._text import to_bytes, to_native, to_text

    environ = _TextEnviron(env={}, encoding='utf-8')

    # I really, really hope that nobody is using a UTF-16 surrogate pair for an environment
    # variable name.  It's unlikely, but this is the unit test for it, so here goes:
    environ[u'\ud83d\udc00'] = u'\ud83d\udc00'.encode('utf-8')
    assert environ[u'\ud83d\udc00'] == u'\ud83d\udc00'

# Generated at 2022-06-13 16:38:42.314992
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    actual_result = environ['PATH']

    import os

    assert actual_result == os.environ['PATH']


# Generated at 2022-06-13 16:38:48.106698
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'PYTHONPATH': b'/usr/lib/python', b'PYTHONIOENCODING': b'utf-8'})
    assert environ[b'PYTHONPATH'] == u'/usr/lib/python'
    assert environ[u'PYTHONPATH'] == u'/usr/lib/python'
    assert environ[u'PYTHONIOENCODING'] == u'utf-8'
    assert environ[u'PYTHONIOENCODING'] == u'utf-8'


# Generated at 2022-06-13 16:38:55.352394
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import ctypes
    _environ = ctypes.cast(
        ctypes.py_object(environ._raw_environ),
        ctypes.POINTER(ctypes.c_char_p)
    ).contents

    # no modification
    assert environ['PATH'] == _environ[0].decode(sys.getfilesystemencoding())

    environ['PATH'] += ':foo'
    assert environ['PATH'] == _environ[0].decode(sys.getfilesystemencoding())
    assert environ['PATH'] != _environ[0].decode(sys.getfilesystemencoding())

# Generated at 2022-06-13 16:39:03.161431
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(env={'A': b'\xE1'}, encoding='latin-1')
    assert environ['A'] == u'\xe1'



# Generated at 2022-06-13 16:39:14.291000
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:18.329849
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        assert isinstance(environ["PATH"], str)
    except KeyError:
        # On macOS, PATH is set to /usr/bin:/bin:/usr/sbin:/sbin,
        # which is not utf-8 decodable.
        pass


# Generated at 2022-06-13 16:39:20.050345
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    pass


test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:39:28.956387
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class MockEnviron(object):
        def __init__(self):
            self.env = {
                'FOO': u'\u1234',
                'BAR': 'foo\x11\x22\x33\x44\x55\x66',
            }

        def __getitem__(self, key):
            return self.env[key]

    env = _TextEnviron(MockEnviron(), encoding='utf-8')
    assert env['FOO'] == u'\u1234'
    assert env['BAR'] == u'foo\x11\x22\x33\x44\x55\x66'



# Generated at 2022-06-13 16:39:36.997433
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test new values
    environ._value_cache = {}
    assert environ['LANG'] == to_text(os.getenv('LANG')) == to_text('en_US.UTF-8')

    # Test cached values
    environ._value_cache = {}
    assert environ['LANG'] == to_text(os.getenv('LANG')) == to_text('en_US.UTF-8')
    assert len(environ._value_cache) == 1
    assert environ['LANG'] == to_text(os.getenv('LANG')) == to_text('en_US.UTF-8')
    assert len(environ._value_cache) == 1

    # Test new values for multiple variables
    environ._value_cache = {}
    assert environ['LANG'] == to_text

# Generated at 2022-06-13 16:39:41.982599
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test with key:value encoding
    test_environ = _TextEnviron(env={b'ANSIBLE_FOO': b'bar'}, encoding='utf-8')
    assert test_environ[b'ANSIBLE_FOO'] == 'bar'
    # test with no encoding
    test_environ = _TextEnviron(env={'ANSIBLE_FOO': 'bar'})
    assert test_environ['ANSIBLE_FOO'] == 'bar'


# Generated at 2022-06-13 16:39:53.992963
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Given a key
    key = 'test_key'
    # When the key is not present in the environment
    # Then it should raise KeyError
    try:
        environ[key]
    except KeyError:
        pass
    # Given a key and a value
    value = u"Bödvar"
    # When the key and value are set in the environment
    environ[key] = value
    # Then __getitem__ should return the value
    assert environ[key] == value
    # When the key is deleted from the environment
    del environ[key]
    # Then it should raise KeyError
    try:
        environ[key]
    except KeyError:
        pass
    # When the key is set in the environment to the value and the value is subsequently modified
    environ[key] = value
    en

# Generated at 2022-06-13 16:40:02.850611
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    environ = _TextEnviron(encoding='utf-8')
    os.environ['ANSIBLE_TEST_ANSIBLE_MODULE_UTILS_UTILS_TEXT_ENVIRON_KEY'] = 'test'
    assert isinstance(environ['ANSIBLE_TEST_ANSIBLE_MODULE_UTILS_UTILS_TEXT_ENVIRON_KEY'], str)
    # On python3, os.environ already returns str, so we won't need to use encoding
    key_value = os.environ['ANSIBLE_TEST_ANSIBLE_MODULE_UTILS_UTILS_TEXT_ENVIRON_KEY']
    if not PY3:
        key_value = key_value.decode(sys.getfilesystemencoding())

# Generated at 2022-06-13 16:40:09.619178
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method __getitem__ of class _TextEnviron

    :return: True if unit test passed
    '''

    environ = _TextEnviron()
    environ['test'] = 'user'
    assert environ['test'] == 'user'
    assert environ._raw_environ['test'] == 'user'

    environ = _TextEnviron()
    environ['test'] = b'user'
    assert environ['test'] == 'user'
    assert environ._raw_environ['test'] == b'user'
    return True

# Generated at 2022-06-13 16:40:32.378792
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check conversion of text string in os.environ
    environ['text_key'] = 'text_value'
    if PY3:
        assert isinstance(environ['text_key'], str)
    else:
        assert isinstance(environ['text_key'], unicode)
    assert environ['text_key'] == 'text_value'

    # Check conversion of bytes string in os.environ
    environ['bytes_key'] = b'bytes_value'
    if PY3:
        assert isinstance(environ['bytes_key'], str)
    else:
        assert isinstance(environ['bytes_key'], unicode)
    assert environ['bytes_key'] == u'bytes_value'


# Generated at 2022-06-13 16:40:39.188434
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    environ_copy = {}
    for k in environ:
        environ_copy[k] = environ[k]
    # Test
    if not PY3:
        for k in environ_copy:
            assert(isinstance(k, str))
        assert(isinstance(environ_copy['PATH'], str))
    # Teardown
    for k in environ_copy:
        environ[k] = environ_copy[k]


# Generated at 2022-06-13 16:40:50.558317
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    # Save old values of the test variables
    old_testenv_value = os.environ.get('TESTENV', None)
    old_testenv_value_encoding = sys.getfilesystemencoding()

    # Value is a string
    os.environ['TESTENV'] = 'foo'
    assert environ['TESTENV'] == u'foo'

    # Value is a string encoded in the environment's character set
    os.environ['TESTENV'] = u'foo'.encode(old_testenv_value_encoding)
    assert environ['TESTENV'] == u'foo'

    # Restore the old values
    if old_testenv_value is None:
        del os.environ['TESTENV']

# Generated at 2022-06-13 16:40:57.116534
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    print(environ['PYTHONIOENCODING'])
    environ['PYTHONIOENCODING'] = 'utf-8'
    print(environ['PYTHONIOENCODING'])
    environ['PYTHONIOENCODING'] = 'windows-1252'
    print(environ['PYTHONIOENCODING'])
    del environ['PYTHONIOENCODING']



# Generated at 2022-06-13 16:40:58.801361
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert isinstance(_TextEnviron()[''], type(to_text(b'', encoding='utf-8')))

# Generated at 2022-06-13 16:41:05.728812
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Item in os.environ as unicode gets returned as unicode
    assert isinstance(environ['PYTHONPATH'], unicode)

    # Item in os.environ as bytes gets returned as unicode
    assert isinstance(environ[str('PYTHONPATH')], unicode)

    # Item in os.environ which isn't valid in the filesystem encoding gets returned decoded using utf-8
    environ['ANSIBLE_TEST_VAR'] = '\xe4\xf6\xfc\xc4\xd6\xdc\xdf'
    assert isinstance(environ['ANSIBLE_TEST_VAR'], unicode)
    assert environ['ANSIBLE_TEST_VAR'] == u'\xe4\xf6\xfc\xc4\xd6\xdc\xdf'


# Generated at 2022-06-13 16:41:16.280888
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8', env={b'foo': b'bar'})
    assert env.encoding == 'utf-8'
    assert env._raw_environ == {b'foo': b'bar'}
    assert env._value_cache == {}

    assert env['foo'] == u'bar'
    assert env._raw_environ == {b'foo': b'bar'}
    assert env._value_cache == {b'bar': u'bar'}

    assert env['foo'] == u'bar'
    assert env._raw_environ == {b'foo': b'bar'}
    assert env._value_cache == {b'bar': u'bar'}

    env['foo'] = u'baz'

# Generated at 2022-06-13 16:41:24.378105
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with existing values.
    assert environ['LANG'] == 'en_US.UTF-8'
    assert environ['LC_CTYPE'] == 'en_US.UTF-8'
    assert environ['LC_ALL'] == ''

    # Test that values are decoded
    assert not isinstance(environ['LANG'], bytes)
    assert not isinstance(environ['LC_CTYPE'], bytes)
    assert not isinstance(environ['LC_ALL'], bytes)

    # Test with missing values.
    try:
        environ['no such variable']
        assert False
    except KeyError:
        pass

# Generated at 2022-06-13 16:41:29.254822
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    os.environ[b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'] = 'value'
    import ansible.module_utils.common
    assert ansible.module_utils.common.environ[u'あいうえお'] == 'value'


# Generated at 2022-06-13 16:41:39.170937
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # This mimics the way os.environ works on Python3
    e = _TextEnviron(env={'foo': 'bar', 'bar': 'baz'}, encoding=None)
    assert e['foo'] == 'bar'
    assert e['bar'] == 'baz'
    assert e['noexist'] == ''

    # This mimics the way os.environ works on Python2 since we use utf-8
    if sys.version_info.major < 3:
        assert e['foo'] == 'bar'
        assert e['bar'] == 'baz'
        assert e['noexist'] == ''

    # Encoding should override whatever is in sys.getfilesystemencoding() if it's set

# Generated at 2022-06-13 16:42:16.902555
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Define a non-default encoding to test the __init__ method.
    environ_test = _TextEnviron(encoding='latin1')
    assert len(environ) == len(environ_test)
    # Make sure the tests below don't change any of our environment variables.
    original_value = str(environ.get('PATH'))
    try:
        if PY3:
            # Test that it returns unicode values on Python3
            value = environ['PATH']
            assert isinstance(value, str)
        else:
            # Test that it returns unicode values on Python2
            value = environ['PATH']
            assert isinstance(value, unicode)
    finally:
        # Ensure that we don't leave anything changed.
        os.environ['PATH'] = original_value

# Generated at 2022-06-13 16:42:19.419203
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    env = _TextEnviron()

    # Execute
    result = env['HOME']

    # Assert
    assert isinstance(result, str)

# Generated at 2022-06-13 16:42:28.831887
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {to_bytes('a'): to_bytes('b'), to_bytes('c'): to_bytes('d')}
    # Test that if the value is already in the cache, we don't decode it again
    environ._value_cache = {to_bytes('b'): to_bytes('b')}
    assert to_bytes('b') == environ[to_bytes('a')]
    # Test that if we haven't decoded the value before, we do decode it and store it in the cache
    environ._value_cache = {to_bytes('b'): to_bytes('b')}
    assert to_bytes('d') == environ[to_bytes('c')]
    assert to_bytes('d') == environ._value_cache[to_bytes('c')]
    # Test that

# Generated at 2022-06-13 16:42:32.097918
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()

    # The following test only pass on a python setup with the LC_ALL environment
    # variable set to en_US.UTF-8
    if 'LC_ALL' in environ:
        assert environ['LC_ALL'] == u'en_US.UTF-8'


# Generated at 2022-06-13 16:42:38.912899
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    values = {
        u'': u'',
        u'key1': u'value1',
        u'¯\\_(ツ)_/¯': u'¯\\_(ツ)_/¯',
        u'x': u'\u2508',
        u'y': u'\U0001f43b',
        u'z': u'\U0001F3F3\uFE0F\u200D\U0001F308'
    }
    if sys.getfilesystemencoding() == 'ascii':
        values[u'z'] = u'\U0001F3F3\uFE0F\u200D\uFFFD'
    env = _TextEnviron(encoding='utf-8')
    for key in values:
        env.__setitem__(key, values[key])

# Generated at 2022-06-13 16:42:47.417331
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import struct


# Generated at 2022-06-13 16:42:58.564661
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test for pass-through for non-unicode
    environ.update({u'é'.encode('utf-8') : u'é'.encode('utf-8')})
    assert environ[u'é'.encode('utf-8')] == u'é'

    # test for surrogate handling for non-unicode
    environ[u'é'.encode('utf-16')] = u'é'
    if PY3:
        assert environ[u'é'.encode('utf-16')] == u'é'
    else:
        assert environ[u'é'.encode('utf-16')] == u'\udcc1'

    # test for pass-through for unicode
    environ.update({u'é': u'é'})
    if PY3:
        assert environ

# Generated at 2022-06-13 16:43:00.050689
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['variable'] = 'value'
    
    assert environ['variable'] == 'value'


# Generated at 2022-06-13 16:43:10.148675
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['LIST'] = 'list1, list2'
    assert environ['LIST'] == 'list1, list2'
    environ['DICT'] = '{ "key": "value" }'
    assert environ['DICT'] == '{ "key": "value" }'
    environ['TUPLE'] = '(tuple1, tuple2)'
    assert environ['TUPLE'] == '(tuple1, tuple2)'
    environ['UNICODE'] = to_bytes('\u00e5'.encode('utf-8'))
    assert environ['UNICODE'] == '\u00e5'
    environ['BYTE'] = '\x00\x01\x02\x03'
    assert environ['BYTE'] == '\x00\x01\x02\x03'

# Generated at 2022-06-13 16:43:19.529970
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Testing byte string keys
    byte_key = b'foo'
    byte_value = b'bar'
    environ[byte_key] = byte_value
    assert isinstance(environ[byte_key], str)
    assert environ[byte_key] == to_text(byte_value, 'utf-8')

    # Testing text string keys
    text_key = 'foo'
    text_value = 'bar'
    environ[text_key] = text_value
    assert isinstance(environ[text_key], str)
    assert environ[text_key] == to_text(text_value, 'utf-8')



# Generated at 2022-06-13 16:43:54.173870
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # SetUp
    for op in ['==', '!=']:
        for env in [b'LANG=en_US.UTF-8', b'LANG=pt_BR.UTF-8']:
            # Arrange
            environ_name, environ_value = env.split(b'=', 1)
            os_environ = {environ_name.decode('utf-8'): environ_value.decode('utf-8')}

            # Act
            env = _TextEnviron(env=os_environ)
            env_value = env[environ_name.decode('utf-8')]

            # Assert
            assert eval(f'env_value {op} environ_value'), '{} {} {} does not evaluate as True'.format(env_value, op, environ_value)

# Generated at 2022-06-13 16:43:56.510064
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = {b'test': b'\xed\x98\x95\xed\x98\x95'}
    env = _TextEnviron(test_env, encoding='utf-8')

    assert env['test'] == '\ud558\ud558'

# Generated at 2022-06-13 16:44:02.199476
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = {}
    test_environ['text_string'] = 'this_is_a_string'
    test_environ['bytes_string'] = to_bytes('this_is_a_string')
    test_environ['bad_encoding_string'] = to_bytes('this_is_a_string', encoding='latin1')

    # Test retrieving from a regular dict
    test_env = _TextEnviron(test_environ)
    assert test_env['text_string'] == 'this_is_a_string'
    assert test_env['bytes_string'] == 'this_is_a_string'

    # Test retrieving from a regular dict w/ a bad encoding
    if PY3:
        assert test_env['bad_encoding_string'] == 'this_is_a_string'
   

# Generated at 2022-06-13 16:44:13.083933
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'b': b'\xff',
                           'c': '\xff'})

    # Returns the value as unicode text
    assert environ['b'] == '\ufffd'
    assert environ['c'] == '\xff'

    # Returns the value as bytes
    assert environ['b'] == '\ufffd'
    assert environ['c'] == '\xff'

    # Returns the value as text when a non-standard encoding is used
    assert environ['b'] == '\ufffd'
    assert environ['c'] == '\xff'

    # Works the same when the bytes are not ASCII
    assert environ['b'] == '\ufffd'
    assert environ['c'] == '\ufffd'


# Generated at 2022-06-13 16:44:20.948584
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _TestEnviron(object):
        def __init__(self, env_dict):
            self._env_dict=env_dict
        def __getitem__(self, key):
            return self._env_dict[key]

    env_dict={"1": "1",
              "2": "2",
              "3": "3"}
    raw_environ=_TestEnviron(env_dict)

    env=_TextEnviron(env=raw_environ,encoding="utf-8")
    if PY3:
        assert env["1"]=="1"
        assert env["2"]=="2"
        assert env["3"]=="3"
    else:
        assert env["1"]==u"1"
        assert env["2"]==u"2"

# Generated at 2022-06-13 16:44:31.042053
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    tempEnviron = {'key1': 'value1', 'key2': 'value2'}
    _TextEnviron._raw_environ = tempEnviron

    if PY3:
        # Note that Python3's os.environ doesn't decode items in the environment, it returns them
        # as byte strings so we match that behaviour
        expected = tempEnviron
    else:
        expected = {'key1': 'value1', 'key2': 'value2'}

    # Act
    result = _TextEnviron()

    # Assert
    assert result['key1'] == expected['key1']
    assert result['key2'] == expected['key2']

# Generated at 2022-06-13 16:44:40.324600
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    env = _TextEnviron()
    os.environ.clear()

    # Test: None
    key = 'ANSIBLE_TEST_1'
    # unicode
    os.environ[key] = '\u00e9'
    assert env[key] == '\u00e9'
    # byte string
    os.environ[key] = b'\xc3\xa9'
    assert env[key] == '\u00e9'

    # Test: encoding
    key = 'ANSIBLE_TEST_2'
    # unicode
    os.environ[key] = '\u00e9'
    assert env[key] == '\u00e9'
    # byte string
    os.environ[key] = b'\xc3\xa9'

# Generated at 2022-06-13 16:44:47.582442
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # To test that getitem() returns the correct values and not just any text value
    environ['environ_test_key'] = r'environ_test_value: \xe1\xb9\xa1'
    assert environ[r'environ_test_key'] == r'environ_test_value: \xe1\xb9\xa1'
    del environ['environ_test_key']



# Generated at 2022-06-13 16:44:57.694299
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environment = {'ANSIBLE_MODULE_ARGS': '{}', 'ANSIBLE_MODULE_NAME': 'debug', 'LANG': 'en_US.UTF-8', 'PWD': '/home/jg/ansible/ansible-modules-core/cloud/cloudflare', 'SHLVL': '1', 'TEST_ENV': 'working', 'TEST_ENV_UNICODE': 'äöüß', 'TEST_ENV_UTF8': '☃', '_': '/usr/bin/python'}
    test_environ = _TextEnviron()
    test_environ._raw_environ = test_environment
    assert test_environ.get('TEST_ENV') == test_environment['TEST_ENV']

# Generated at 2022-06-13 16:45:05.545026
# Unit test for method __getitem__ of class _TextEnviron