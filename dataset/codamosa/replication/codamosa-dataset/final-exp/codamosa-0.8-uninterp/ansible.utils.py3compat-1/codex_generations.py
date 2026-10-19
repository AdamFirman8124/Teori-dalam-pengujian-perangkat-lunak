

# Generated at 2022-06-13 16:36:02.434894
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_native
    # Check for non-existing variable
    try:
        environ['doesnt_exist']
    except KeyError:
        pass
    else:
        raise AssertionError(to_native("""KeyError not raised when trying to access non-existent environment variable."""))

    # Check that we get the value when the variable exists
    os.environ['my_var'] = to_bytes('my_value', encoding='utf-8', nonstring='strict')
    assert environ['my_var'] == 'my_value'

    # Check that we get the value decoded
    os.environ['my_var'] = b'\x85'
    assert environ['my_var'] == u'\u2022'

# Generated at 2022-06-13 16:36:13.360536
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''Test the __getitem__ method of class _TextEnviron'''
    print('Test the __getitem__ method of class _TextEnviron')
    # initialize
    test_environ = _TextEnviron()
    # test a nonexistent variable
    nonexistent_key = 'NONEXISTENT'
    try:
        print('Check nonexistent variable %s' % nonexistent_key)
        assert test_environ[nonexistent_key] is False
    except KeyError as e:
        print('%s is a nonexistent variable' % nonexistent_key)
        assert True
    except AssertionError:
        raise AssertionError('__getitem__: KeyError was not thrown for nonexistent variable %s'
                             % nonexistent_key)
    # test a variable with a byte value
    test_key = 'BYTE_VALUE'
   

# Generated at 2022-06-13 16:36:15.531325
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert isinstance(environ['PATH'], str), 'Failed to convert to text.'

# Generated at 2022-06-13 16:36:25.012995
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import unittest

    env = _TextEnviron(encoding='utf-8')
    env['foo'] = 'bar'
    os.environ['foo'] = 'bar'
    env['baz'] = b'qux'
    os.environ['baz'] = b'qux'
    env['enc_error'] = b'\xff'
    os.environ['enc_error'] = b'\xff'


# Generated at 2022-06-13 16:36:34.219748
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # regular usage
    assert environ['HOME'] == os.environ['HOME']

    # non-ascii character
    non_ascii = '\N{SNOWMAN}'
    os.environ['ANSIBLE_TEST_NON-ASCII'] = non_ascii
    assert environ['ANSIBLE_TEST_NON-ASCII'] == non_ascii

    # non-ascii character with surrogate

# Generated at 2022-06-13 16:36:44.538691
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # load os.environ into a test environment
    test_environ = _TextEnviron()
    # example: content of os.environ, with various type of values
    # {'PYTHONPATH': '.:testdir',
    #  'HOME': '/home/user',
    #  'UNDEFINED': None,
    #  'PYTHONIOENCODING': 'UTF-8',
    #  'USER': 'user',
    #  'PWD': '/home/user/ansible',
    #  'LANG': 'en_US.UTF-8',
    #  'SHELL': '/bin/bash',
    #  'PATH': '/home/user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/user/.local/bin:/

# Generated at 2022-06-13 16:36:53.843113
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LANG'] == u'C.UTF-8'
    assert isinstance(environ['LANG'], unicode)
    if os.name != 'nt':
        assert environ['PATH'] == u'/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
        assert isinstance(environ['PATH'], unicode)
    else:
        assert environ['PATH'] == u'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\'  # noqa: E501
        assert isinstance(environ['PATH'], unicode)
      

# Generated at 2022-06-13 16:37:00.311263
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_env = os.environ.copy()
    os.environ['KEY'] = 'value'
    os.environ['KEY_WITH_ESCAPED'] = r'value_with_\:_escaped'
    os.environ['KEY_WITH_NON_ASCII'] = u'value_with_\u20ac_non_ascii'
    assert 'value' == environ['KEY']
    assert u'value_with_:_escaped' == environ['KEY_WITH_ESCAPED']
    assert u'value_with_€_non_ascii' == environ['KEY_WITH_NON_ASCII']
    os.environ.clear()
    os.environ.update(raw_env)

# Generated at 2022-06-13 16:37:04.080907
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LC_ALL'] == 'en_US.utf-8'
    assert environ['LC_ALL'] == environ['LC_ALL']  # Cache works
    assert environ['LC_ALL'] == environ['LC_ALL']  # Test cache a second time

# Generated at 2022-06-13 16:37:10.221507
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test passing string and unicode in, getting string and unicode out
    raw = {'ascii': 'ascii',
           'unicode': u'\xe9'.encode('latin-1'),
           'utf-8': u'\xe9'.encode('utf-8'),
           'invalid-utf8': u'\xe9'.encode('utf-8')[:1],
           'invalid-latin1': u'\xe9'.encode('latin-1')[:1],
           }
    env = _TextEnviron(env=raw, encoding='utf-8')
    # ascii
    assert env['ascii'] == u'ascii'
    assert type(env['ascii']) == type(u'')
    # Latin-1

# Generated at 2022-06-13 16:37:24.468962
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_variable = 'test'
    unicode_variable = u'résumé'
    binary_variable = b'thisis\x01a\x01test'

    # Make sure we're testing the right class
    assert environ.__class__ == _TextEnviron

    # Start off with empty os.environ and fill it up
    environ._raw_environ = {}
    environ._raw_environ[text_variable] = text_variable
    environ._raw_environ[unicode_variable] = unicode_variable.encode('utf-8')
    environ._raw_environ[binary_variable] = binary_variable

    # Make sure the getitem method works
    assert environ[text_variable] == text_variable
    assert environ[unicode_variable] == unicode_variable
    assert en

# Generated at 2022-06-13 16:37:33.356565
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a dummy environment
    path = 'some/path'
    env = {
        b'BADGER_PATH': path
    }

    # Check that we get the value back in bytes since we are asking for a raw environment
    env_raw = _TextEnviron(env)
    assert env_raw['BADGER_PATH'] == path

    # Check that we get the value back decoded as utf-8
    env_text = _TextEnviron(env, encoding='utf-8')
    assert env_text['BADGER_PATH'] == path.decode('utf-8')

# Generated at 2022-06-13 16:37:42.708021
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    # Validate that the method can successfully retrieve a standard
    # value.
    result = environ['PATH']
    expected = os.environ['PATH']
    assert result == expected
    # Validate that the method can successfully retrieve a value
    # that is known to throw UnicodeDecodeError.
    result = environ['USER']
    expected = os.environ['USER']
    # Note that if the test is run under a user that has a Unicode
    # character in the username, is will cause the test to fail.
    # The non-UTF-8 environment variable is only used for this
    # test.
    assert result == expected
    # Validate that the method can successfully retrieve a byte
    # string and convert it to text.
    result = en

# Generated at 2022-06-13 16:37:44.087492
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert environ['LANG'] == to_text(os.environ['LANG'], encoding='utf-8')

# Generated at 2022-06-13 16:37:53.477753
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'test1': b'value1', b'test2': b'value2',
                        u'unicode1': u'value3', u'unicode2': u'value4'})
    assert b'test1' in env
    assert b'test2' in env
    assert u'unicode1' in env
    assert u'unicode2' in env
    assert env['test1'] == u'value1'
    assert env['test2'] == u'value2'
    assert env[u'unicode1'] == u'value3'
    assert env[u'unicode2'] == u'value4'
    env[u'unicode3'] = u'value5'
    env[b'test3'] = u'value6'
    assert u'unicode3' in env

# Generated at 2022-06-13 16:38:03.502857
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = os.environ.copy()
    testenv = _TextEnviron(env)

    # Check that we can get entries from the environment
    #
    # Start with byte strings.  PY2 will decode to unicode and PY3 should just pass through as
    # unicode strings
    for var in env:
        if PY3:
            assert isinstance(testenv[var], str)
        else:
            assert isinstance(testenv[var], unicode)
        assert os.environ[var] == env[var] == testenv._raw_environ[var] == testenv[var]

    # Verify that unicode strings are passed through

# Generated at 2022-06-13 16:38:05.553721
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    e = _TextEnviron({b'LANG': b'en_US.UTF-8', })

    assert e['LANG'] == u'en_US.UTF-8'

# Generated at 2022-06-13 16:38:15.293262
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    value_bytes = b'\xff'
    value_text = to_text(value_bytes, encoding='utf-8')

    environ._raw_environ = {'key': value_bytes}
    # First pass
    assert environ['key'] == value_text
    assert environ._value_cache == {value_bytes: value_text}
    # Second pass
    assert environ['key'] == value_text
    assert environ._value_cache == {value_bytes: value_text}
    # Third pass, cached value is still correct
    environ._value_cache[value_bytes] = 'wrong'
    assert environ['key'] == 'wrong'
    assert environ._value_cache == {value_bytes: 'wrong'}


# Generated at 2022-06-13 16:38:26.264918
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with Latin 1, UTF-8, and a non-decodable byte string
    env = _TextEnviron({b'ascii': b'ascii', b'latin1': b'\xe9', b'utf8': b'\xc4\x93', b'non': b'\xff'})
    env.encoding = 'utf-8'
    # Test ASCII
    assert env['ascii'] == u'ascii'
    # Test latin1
    assert env['latin1'] == u'é'
    # Test UTF-8
    assert env['utf8'] == u'ē'
    # Test non-decodable ascii
    assert env['non'] == u'\ufffd'

# Generated at 2022-06-13 16:38:28.393547
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == os.environ['PATH']

# Generated at 2022-06-13 16:38:37.808771
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test string without decoding
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    import os
    if PY3:
        raise Exception('Python 2 Only')
    if not isinstance(os.environ, MutableMapping):
        raise Exception('os.environ have to be a Mutable Mapping')
    input_value = os.environ['PATH']
    if not isinstance(input_value, bytes):
        raise Exception('Test data have to be a bytes type')
    text = to_text(input_value, encoding='utf-8', nonstring='passthru', errors='surrogate_or_strict')

# Generated at 2022-06-13 16:38:43.548425
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    obj = _TextEnviron(encoding='utf-8')
    obj['foo'] = 'bar'
    assert obj['foo'] == 'bar'
    obj['foo'] = b'baz'
    assert obj['foo'] == 'baz'
    obj['foo'] = to_bytes('quux', encoding='utf-8')
    assert obj['foo'] == 'quux'

# Generated at 2022-06-13 16:38:54.511687
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test valid ascii
    new_environ = _TextEnviron({'a': 'abcde'}, encoding='utf-8')
    assert new_environ['a'] == 'abcde'

    # Test valid utf-8
    new_environ = _TextEnviron({'a': 'Георгий'.encode('utf-8')}, encoding='utf-8')
    assert new_environ['a'] == 'Георгий'

    # Test invalid utf-8
    new_environ = _TextEnviron({'a': b'\x80'}, encoding='utf-8')
    try:
        new_environ['a']
    except UnicodeDecodeError:
        assert True
    else:
        assert False

    # Test cp1251


# Generated at 2022-06-13 16:38:59.171062
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ["ANSIBLE_COMMON_TEST_KEY"] = "ANSIBLE_COMMON_TEST_VALUE"
    assert environ.get("ANSIBLE_COMMON_TEST_KEY") == u'ANSIBLE_COMMON_TEST_VALUE'


# Generated at 2022-06-13 16:39:08.015197
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an instance of _TextEnviron with an encoding parameter of utf-8
    environ = _TextEnviron(encoding='utf-8')

    # Test retrieval of a unicode environment variable
    environ['FOO'] = u'f\u00f4\u00f4'
    if PY3:
        assert environ['FOO'] == u'f\u00f4\u00f4'
    else:
        assert environ['FOO'] == u'f\xf4\xf4'
    del environ['FOO']

    # Test retrieval of an 8-bit encoded environment variable
    environ['FOO'] = 'f\xc3\xb4\xc3\xb4'
    assert environ['FOO'] == u'f\u00f4\u00f4'
    del en

# Generated at 2022-06-13 16:39:11.804951
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY2, PY3
    if PY2:
        return
    environ["foo"] = b"bar"
    # We are expecting the result to be unicode
    assert isinstance(environ["foo"], str)

# Generated at 2022-06-13 16:39:15.812310
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert(environ['HOME'] == os.environ['HOME'])
    assert(environ['HOME'] == os.environ['HOME'].decode(sys.getfilesystemencoding()))



# Generated at 2022-06-13 16:39:25.821301
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test the __getitem__ method of the _TextEnviron class

    # Set the environment to test.  We're going to add something that we'll want to pick up in the
    # output as well as some system variables that might be used by other tests
    # pylint: disable=anomalous-backslash-in-string
    os.environ = {'TEST': 'TESTING', 'HOME': '/Users/testuser', 'LC_ALL': 'en_US.UTF-8'}
    text_env = _TextEnviron(encoding='utf-8')

    # Verify we get the correct text for the variables we set
    assert text_env['TEST'] == 'TESTING'
    assert text_env['HOME'] == '/Users/testuser'

# Generated at 2022-06-13 16:39:30.588726
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['бабушка'] = 'авокадо'
    local_environ = _TextEnviron(encoding='utf-8')
    assert local_environ['бабушка'] == 'авокадо'

# Generated at 2022-06-13 16:39:37.859327
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    baz = b'\xe2\x98\x83'
    foo = {'unicode_key': b'unicode_value',
           b'unicode_key_bytes': b'unicode_value_bytes',
           'utf8_key': baz,
           b'utf8_key_bytes': baz,
           'ascii_key': b'ascii_value',
           b'ascii_key_bytes': b'ascii_value_bytes',
           'missing_encoding_key': 'missing_encoding_value',
           b'missing_encoding_key_bytes': 'missing_encoding_value_bytes',
          }
    t = _TextEnviron(foo, encoding='utf-8')
    assert t['unicode_key'] == u'unicode_value'


# Generated at 2022-06-13 16:39:43.985300
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PYTHONDONTWRITEBYTECODE'] == u'1'

# Generated at 2022-06-13 16:39:47.974346
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    key="PaTh"
    os.environ[key]="/usr/local/bin:/usr/bin/:/bin:"
    result=environ[key]

    assert (result=="/usr/local/bin:/usr/bin/:/bin:")

# Generated at 2022-06-13 16:39:50.386223
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_VAR_1'] = 'ANSIBLE TEST VAR 1'
    os.environ['ANSIBLE_TEST_VAR_2'] = b'ANSIBLE TEST VAR 2'
    assert environ['ANSIBLE_TEST_VAR_1'] == 'ANSIBLE TEST VAR 1'
    assert environ['ANSIBLE_TEST_VAR_2'] == 'ANSIBLE TEST VAR 2'

# Generated at 2022-06-13 16:39:58.067617
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['Key1'] = '12345'
    environ['Key2'] = b'12345'
    environ['Key3'] = 12345

    assert len(environ) == 3

    assert environ['Key1'] == u'12345'
    assert environ['Key2'] == u'12345'
    assert environ['Key3'] == u'12345'

    del environ['Key1']

    assert len(environ) == 2

    # Test non-existing key
    try:
        environ['Key4']
        assert False, 'This code should not be reached'
    except KeyError:
        pass

# Generated at 2022-06-13 16:40:00.754031
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(env={'foo': 'bar'}, encoding='ascii')
    assert env['foo'] == 'bar'
    assert type(env['foo']) is str


# Generated at 2022-06-13 16:40:07.630901
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from contextlib import ExitStack
    from ansible.module_utils import six
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    os_environ = os.environ
    os.environ = {}
    # Create a new _TextEnviron.
    environ = _TextEnviron()
    assert isinstance(environ, _TextEnviron)
    assert isinstance(environ, MutableMapping)
    # Test that _TextEnviron has an attribute _encoding that is equal to 'utf-8'.
    environ_encoding = getattr(environ, '_encoding')
    assert isinstance(environ_encoding, six.text_type)
    assert environ_encoding == 'utf-8'


# Generated at 2022-06-13 16:40:19.459209
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unit test for method __getitem__ of class _TextEnviron
    environ['answer'] = u'42'
    assert environ['answer'] == u'42'

    # Test for utf-8
    environ['utf8'] = u'€'

    if sys.platform == 'win32':
        assert environ['utf8'] == u'€'
    else:
        assert environ['utf8'] == u'\u20ac'

    environ['utf8'] = u'€'.encode('utf-8')
    assert environ['utf8'] == u'\u20ac'

    environ['utf8'] = u'€'.encode('utf-8').decode()
    assert environ['utf8'] == u'\u20ac'

    # Test for latin-1
    environ

# Generated at 2022-06-13 16:40:29.299185
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that the behavior of _TextEnviron.__getitem__ works as expected in both Python 2 and
    Python 3
    """
    # Test that an existing key is returned
    # pylint: disable=line-too-long
    # First, let's make sure we can get back text under Python 2
    assert isinstance(environ['PATH'], str)
    # And now let's make sure that we can get back text under Python 3
    assert isinstance(environ['PATH'], str)
    # And now let's make sure that if one of the values is bytes, we still get back text
    os.environ[b'PATH'] = b'/usr/bin'
    assert isinstance(environ['PATH'], str)

    # Test that a missing key is returned
    # pylint: disable=line-too-long

# Generated at 2022-06-13 16:40:40.421897
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ASCII'] = 'test'
    os.environ['BYTES'] = 'test'.encode('utf-8')
    os.environ['UNICODE'] = u'Привет!'
    os.environ['FOLDER'] = u'À Bientôt'.encode('cp1251')
    os.environ['NONASCII'] = u'À Bientôt'.encode('utf-8')
    os.environ['BYTES'] = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

    assert environ['ASCII'] == u'test'
    assert environ['BYTES'] == u'test'
    assert en

# Generated at 2022-06-13 16:40:51.055964
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    os.environ['KEY1'] = b'\xc2\xa2'
    os.environ['KEY2'] = b'\x80'
    os.environ['KEY3'] = b''
    os.environ['KEY4'] = b'\x00'

    text_environ = _TextEnviron()

    assert text_environ['KEY1'] == u'¢'
    assert text_environ['KEY2'] == u'\ufffd'
    assert text_environ['KEY3'] == u''
    assert text_environ['KEY4'] == u'\x00'

    try:
        text_environ['KEY5']
    except KeyError:
        pass
    else:
        raise AssertionError('KeyError not raised')


if __name__ == '__main__':
    test

# Generated at 2022-06-13 16:41:06.691287
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if not PY3:
        if sys.version_info.major == 2 and sys.version_info.minor == 7 and sys.version_info.micro == 12:
            # The tests here assume that the linux implementation of Python2.7.12 will
            # have the bug fix and we get the unicode back from os.environ.  However, in
            # practice, 2.7.12 is the first version to fix this bug and not all 2.7.12
            # distributions will have the fix.  If we don't detect the fix, then these
            # tests will trigger an exception.  Skip that.
            pass
        else:
            assert isinstance(environ['PYTHONPATH'], unicode)

    environ['test_unicode'] = u'dummy'

# Generated at 2022-06-13 16:41:12.154318
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Mimic the real os.environ so we can set the encoding to be used
    env = {b'PYTHONIOENCODING': b'utf-8'}
    te = _TextEnviron(env=env)
    assert te.encoding == 'utf-8'
    assert isinstance(te['PYTHONIOENCODING'], text_type)
    assert te['PYTHONIOENCODING'] == 'utf-8'

    # Test that the cache works
    env[b'PYTHONIOENCODING'] = b'ascii'
    assert te['PYTHONIOENCODING'] == 'utf-8'
    assert b'PYTHONIOENCODING' in env

# Generated at 2022-06-13 16:41:19.379170
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest

    # Assert __getitem__ works correctly when PY3 is true
    with pytest.raises(KeyError):
        environ['non_existent_key']
    with pytest.raises(TypeError):
        environ[1]
    environ[u'föö'] = u'föö'
    assert environ[u'föö'] == u'föö'
    assert environ['föö'] == u'föö'

    # Assert __getitem__ works correctly when PY3 is false
    with pytest.raises(KeyError):
        environ['non_existent_key']
    with pytest.raises(TypeError):
        environ[1]
    environ[u'föö'] = u'föö'
    assert environ

# Generated at 2022-06-13 16:41:26.872617
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    os.environ["TEST_KEY"] = "value"
    assert environ["TEST_KEY"] == "value", "Method __getitem__ of _TextEnviron should have returned 'value', but returned '{}' instead.".format(environ["TEST_KEY"])
    del os.environ["TEST_KEY"]
    try:
        del os.environ["TEST_KEY"]
    except:
        pytest.fail("Method __getitem__ of _TextEnviron should have deleted the key/value pair from the actual os.environ, but it did not.")



# Generated at 2022-06-13 16:41:37.231450
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    from io import BytesIO
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes, to_text

    class MockEnviron(MutableMapping):
        def __init__(self):
            self.data = {'byte_value': b'\xd8\xf9\xed\xa3',
                         'text_value': u'\ufffd\ufffd\u0d0a',
                         }

        def __delitem__(self, key):
            del self.data[key]

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value


# Generated at 2022-06-13 16:41:38.642874
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert isinstance(environ['BAR'], str)
    assert environ['BAR'] == 'bar2'

# Generated at 2022-06-13 16:41:39.981984
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['foo'] == u'bar'



# Generated at 2022-06-13 16:41:42.768025
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # get the value with normal ASCII
    assert environ['HOME'] == u'/Users/jschwartz'

    # get the value with a non-ASCII character
    assert environ['PATH'] == u'/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'

# Generated at 2022-06-13 16:41:48.584214
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # keys for environment variables
    key = 'ThisIsATestEnvironKey'
    other_key = 'ThisIsAnotherTestEnvironKey'
    # Unicode value
    unicode_value = 'TéstUnicodeValúe'
    # UTF-8 Bytes value
    utf8_value = 'TéstUnicodeValúe'.encode('utf-8')
    # UTF-8 Bytes value with surrogate (\ud800\udc00)
    surrogate_value = b'\xed\xa0\x80\xed\xb0\x80\xed\xa0\x80\xed\xb0\x80'
    # GBK-encoded Bytes value
    gbk_value = 'TéstUnicodeValúe'.encode('gbk', 'surrogateescape')

# Generated at 2022-06-13 16:41:56.744892
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == u"/bin:/usr/bin"

    # set PY3 False
    PY3 = False
    # env = os.environ
    # assert 'PATH' in env, "PATH should be in env"
    # env_value = env['PATH']
    # assert env_value == u"/bin:/usr/bin", "env_value should be /bin:/usr/bin"
    # assert isinstance(env_value, unicode), "env_value should be unicode"
    # assert not isinstance(env_value, bytes), "env_value should not be bytes"


# Generated at 2022-06-13 16:42:19.852684
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_strings = {b'test': u'test',  b'test2\xff': u'test2\ufffd',
                    b'test3\xc3\x9f': u'test3\xdf'}
    for k, v in test_strings.items():
        environ[k] = k
        assert environ[k] == v, "Environ encoding failure"

# Generated at 2022-06-13 16:42:22.916461
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = {b'PATH': b'/usr/bin:/usr/local/bin', b'HOME': b'/home/user'}
    text_environ = _TextEnviron(env=test_env, encoding='utf-8')

    assert isinstance(text_environ['PATH'], str)

# Generated at 2022-06-13 16:42:32.975466
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2

    # Test Python2 behaviour
    e = _TextEnviron({to_bytes('HELLO'): to_bytes('world')}, encoding='utf-8')
    # Test that __getitem__ is calling to_text correctly
    assert e['HELLO'] == u'world'
    # Test that values aren't being cached
    e._raw_environ[to_bytes('HELLO')] = to_bytes('cached')
    assert e['HELLO'] == u'world'
    # Test that we return unicode objects on Python2
    assert isinstance(e['HELLO'], str if PY2 else bytes)

    # Test Python3 behaviour

    # Test that it works on Python3
   

# Generated at 2022-06-13 16:42:39.303561
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from tempfile import TemporaryDirectory
    from ansible.module_utils._text import escape_control_chars
    from ansible.module_utils.six.moves import shlex_quote
    from tempfile import TemporaryDirectory

    non_default_encodings = (
        'latin-1',
        'utf-16',
        'utf-32',
    )

    test_strings = (
        'string',
        '~$&*!@#$^\n\t',
        u'\U0001f9b0\U0001f9b1',
    )

    test_data = []
    for test_string in test_strings:
        # Bytes string keys with bytes string values
        # Python3: Return value unchanged
        # Python2: Return text with default encoding (utf-8)
        key = shlex_

# Generated at 2022-06-13 16:42:43.192163
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    env = {'ANSIBLE_CONFIG': 'cfg/ansible.cfg', 'ANSIBLE_CALLBACK_WHITELIST' : 'profile_tasks, timer'}

    encodings = (
        'utf-8',
        'cp1251',
    )

    expected = {
        'utf-8': {
            'ANSIBLE_CONFIG': 'cfg/ansible.cfg',
            'ANSIBLE_CALLBACK_WHITELIST': 'profile_tasks, timer',
        },
        'cp1251': {
            'ANSIBLE_CONFIG': 'cfg/ansible.cfg',
            'ANSIBLE_CALLBACK_WHITELIST': 'profile_tasks, timer',
        }
    }

    for encoding in encodings:
        # Act
        result = _

# Generated at 2022-06-13 16:42:48.149909
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['MY_VAR'] = 'my_value'
    assert environ['MY_VAR'] == 'my_value'
    environ['MY_VAR'] = 'ваша_сторона'
    assert environ['MY_VAR'] == 'ваша_сторона'


# Generated at 2022-06-13 16:42:58.998627
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test for PY3
    environ._raw_environ = {b'key1': b'\xe9\xa6\x81\xe5\xb2\x99',
                            b'key2': u'\u8f86\u6ee1\u5927\u5730\u6d32\u5de5\u4fe1\u6258\u7ba1\u4efb\u8ba4',
                            b'key3': u'\u8f86\u6ee1\xe5\x9f\x8e\xe5\xb8\x82\xe7\xa7\x91\xe6\x8a\x80\xe8\x81\x94\xe7\xb3\xbb'}

# Generated at 2022-06-13 16:43:05.276748
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  assert(environ['PYTHONIOENCODING'] == 'utf-8')
  #assert(environ['PYTHONIOENCODING'] == environ['PYTHONIOENCODING'])
  assert(environ['PYTHONIOENCODING'] != environ['PYTHONIOENCODING'])


# Generated at 2022-06-13 16:43:14.528032
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Running the method
    result = environ.__getitem__('PATH')

    # Verifying the content of variable result
    assert type(result) == str
    if sys.platform != 'win32':
        assert result == '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    else:
        assert result == 'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\'


# Generated at 2022-06-13 16:43:17.738140
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    os.environ['ANSIBLE_TEST_GETITEM'] = '\xe1'
    del environ['ANSIBLE_TEST_GETITEM']
    os.environ['ANSIBLE_TEST_GETITEM'] = '\xe1'
    assert environ['ANSIBLE_TEST_GETITEM'] == '\xe1'
    del environ['ANSIBLE_TEST_GETITEM']
    assert 'ANSIBLE_TEST_GETITEM' not in os.environ


# Generated at 2022-06-13 16:43:55.646368
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert isinstance(environ['PATH'], str)



# Generated at 2022-06-13 16:43:57.139134
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['TERM'] == 'xterm-256color'


# Generated at 2022-06-13 16:44:09.091071
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron()

    def _test_getitem(key, expected_value, key_bytes=None):
        try:
            got_value = test_env[key]
        except KeyError:
            got_value = None
        assert got_value == expected_value, "Failed on key: %s Expected: %s Got: %s" % (key, expected_value, got_value)
        if key_bytes is not None:
            try:
                got_value = test_env[key_bytes]
            except KeyError:
                got_value = None
            assert got_value == expected_value, "Failed on key: %s Expected: %s Got: %s" % (key_bytes, expected_value, got_value)

    # Test environment variables and their unicode representations
    #

# Generated at 2022-06-13 16:44:15.563052
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    encodings = [None, 'utf-8', 'iso-8859-1', 'iso-8859-15']
    value = to_bytes('ansible')
    key = 'ANSIBLE'

    for encoding in encodings:
        env = _TextEnviron({key: value}, encoding=encoding)
        if encoding is None or encoding == 'utf-8':
            assert env[key] == to_text(value)
        else:
            assert env[key] == to_text(value, encoding=encoding)

# Generated at 2022-06-13 16:44:20.362151
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    #  Save the original os.environ temporarily
    original_obtenv = environ._raw_environ

    # Create a dict of test data
    import codecs

# Generated at 2022-06-13 16:44:26.768372
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert 'TESTENV' not in environ
    assert (environ['TESTENV'] is None)

    environ['TESTENV'] = 'TESTVALUE'
    assert (environ['TESTENV'] == 'TESTVALUE')

    environ.__delitem__('TESTENV')
    assert 'TESTENV' not in environ

# Generated at 2022-06-13 16:44:32.934038
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        environ['TEST_VARIABLE']
    except KeyError:
        pass
    else:
        del environ['TEST_VARIABLE']
    environ['TEST_VARIABLE'] = 'Test value'
    assert environ['TEST_VARIABLE'] == 'Test value'
    del environ['TEST_VARIABLE']


# Generated at 2022-06-13 16:44:41.256384
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {
        # ascii keys and values
        'var1': 'value1',

        # ascii key, unicode value
        'var2': to_bytes('漢字'),

        # non-ascii keys and values
        '漢字': '漢字',
        '漢字1': 'value2',

        # non-ascii key, ascii value
        '漢字2': 'value3',

        # non-ascii key, unicode value
        '漢字3': '漢字1',

        # illegal utf-8
        'var3': b'\x00',
    }

    # Keys and values should be returned as text
    assert environ['var1']

# Generated at 2022-06-13 16:44:51.662875
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set an environment variable for testing, in bytes so that it is not already a text string
    os.environ[b'TEST_ENVIRON_VAR'] = b'STRING'
    # Verify that accessing the variable (which is in bytes) works on both 2 and 3
    assert environ[b'TEST_ENVIRON_VAR'] == 'STRING'
    # And we've cached the value, should be able to lookup the text string value
    assert environ['TEST_ENVIRON_VAR'] == 'STRING'
    # Verify that we cache the bytes->text conversion so changing the byte value does not affect
    # the text value returned
    os.environ[b'TEST_ENVIRON_VAR'] = b'OTHER STRING'

# Generated at 2022-06-13 16:45:01.888871
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    global environ
    environ = _TextEnviron(encoding='utf-8')

    environ['ascii'] = 'foo'
    assert environ['ascii'] == u'foo'
    environ['utf8'] = b'\xc3\xa9'
    assert environ['utf8'] == u'\u00e9'
    environ['latin1'] = b'\xe9'
    assert environ['latin1'] == u'\u00e9'
    environ['badutf8'] = b'\xff'
    try:
        environ['badutf8']
    except UnicodeDecodeError:
        pass
    else:
        assert False, 'Bad UTF8 did not raise an error'
    environ['mixedutf8'] = b'\xc3\xff'
   