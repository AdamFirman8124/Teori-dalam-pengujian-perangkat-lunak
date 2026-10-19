

# Generated at 2022-06-13 16:35:48.917048
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for _TextEnviron.__getitem__()
    """
    assert isinstance(environ['PATH'], str)
    assert isinstance(environ[b'PATH'], str)

    # Try a simple unicode value
    enc_value = u'\N{HIRAGANA LETTER TU}'
    enc_bytes = enc_value.encode('utf-8')
    raw_environ = {'name': enc_bytes}
    test_environ = _TextEnviron(env=raw_environ, encoding='utf-8')
    # Make sure it's text (type str on Python 3, unicode on Python2)
    assert isinstance(test_environ['name'], str)
    # Make sure we get the unicode value
    assert test_environ['name'] == enc_value



# Generated at 2022-06-13 16:35:59.241850
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import shutil
    import tempfile

    env = os.environ.copy()
    if b'PYTHONIOENCODING' in env:
        del env[b'PYTHONIOENCODING']
    if 'PYTHONIOENCODING' in env:
        del env['PYTHONIOENCODING']

    with tempfile.NamedTemporaryFile(suffix='.sh') as f:
        f.write(b'#!/bin/sh\n')
        for key in env:
            f.write(b'%s="%s"\n' % (key, env[key]))
        f.write(b'export %s' % b';'.join(env))
        f.flush()
        subprocess.call([f.name])


# Generated at 2022-06-13 16:36:04.915677
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    test__TextEnviron___getitem__()

    Test the method to retrieve a value from the Environment

    :param self:
    :return:
    '''
    assert isinstance(environ, _TextEnviron)
    assert isinstance(environ['PATH'], str)
    # Test with Unicode encoding a Magic Mock
    environ = _TextEnviron(encoding='unicode')
    assert isinstance(environ, _TextEnviron)
    assert isinstance(environ['PATH'], str)



# Generated at 2022-06-13 16:36:14.937347
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from textwrap import dedent
    from os import environ as _raw_environ

    def _assert_equal(expected, actual):
        assert isinstance(actual, type(expected))
        assert expected == actual

    environ_key = 'PATH'
    expected = dedent("""\
        /usr/lib/lightdm/lightdm
        /usr/local/sbin
        /usr/local/bin
        /usr/sbin
        /usr/bin
        /sbin
        /bin
        /usr/games
        /usr/local/games
        /snap/bin\
    """)
    environ[environ_key] = expected
    _assert_equal(expected, _raw_environ[environ_key])
    _assert_equal(expected, environ[environ_key])
    assert isinstance

# Generated at 2022-06-13 16:36:24.631349
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ._raw_environ == os.environ
    assert environ.encoding == 'utf-8'

    # byte strings
    environ._raw_environ[b'key1'] = b'value1'
    assert environ[b'key1'] == u'value1'
    environ.__delitem__(b'key1')

    # text strings
    environ._raw_environ[u'key2'] = u'value2'
    assert environ[u'key2'] == u'value2'
    environ.__delitem__(u'key2')

    # unicode characters
    environ._raw_environ[u'key3'] = u'caf\u00e9'
    assert environ[u'key3'] == u'caf\u00e9'


# Generated at 2022-06-13 16:36:29.386810
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'ascii': b'b', 'ascii': 'a', b'unicode': b'b'}, encoding='utf-8')
    assert env['ascii'] == u'a'
    assert env[u'ascii'] == u'a'
    assert env[b'unicode'] == u'b'
    assert env[u'unicode'] == u'b'

# Generated at 2022-06-13 16:36:37.857370
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import unittest

    from ansible.module_utils.six import PY2

    from ansible.module_utils.common._collections_compat import MutableMapping

    test_environment = {
        'test_foo_key': to_bytes('test_foo_value', encoding='utf-8'),
        'test_bar_key': to_bytes('test_bar_value', encoding='ascii', errors='surrogate_or_strict'),
        'test_baz_key': to_bytes('test_baz_value', encoding='utf-8'),
        'test_qux_key': to_bytes('test_qux_value', encoding='latin_1', errors='surrogate_or_strict'),
    }

    environ_class = _TextEnviron.__name__



# Generated at 2022-06-13 16:36:46.502125
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test returning values
    environ.clear()
    environ['foo'] = 'bar'
    environ['baz'] = 'quux'
    assert environ['foo'] == 'bar'
    assert environ['baz'] == 'quux'

    # Test get values in different encodings
    environ.clear()
    environ['foo'] = to_bytes(u'qux', encoding='utf-8')
    assert environ['foo'] == u'qux'

    environ['foo'] = to_bytes(u'qux', encoding='cp1252')
    assert environ['foo'] == u'qux'

if __name__ == '__main__':
    test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:36:55.402461
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    assert isinstance(environ, _TextEnviron)

    environ['THIS_IS_AN_ENV_VAR'] = b'YAY!'
    assert environ['THIS_IS_AN_ENV_VAR'] == u'YAY!'

    environ['UNICODE'] = u'Привет! This is UTF-8!'
    assert environ['UNICODE'] == u'Привет! This is UTF-8!'

    environ['UNICODE'] = 'Привет! Some garbage after it!'
    assert environ['UNICODE'] == u'Привет! Some garbage after it!'

    # Make sure we don't cache values that are changed during a run.

# Generated at 2022-06-13 16:37:02.950259
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that _TextEnviron.__getitem__() returns a text string.
    """
    import pytest
    if PY3:
        pytest.skip("Non-ascii text in os.environ is already text in python3")

    t_env = _TextEnviron(encoding='ascii')
    t_env['test'] = u'\u00E0 vos marques'
    assert isinstance(t_env['test'], text_type)



# Generated at 2022-06-13 16:37:15.308419
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Python 2.7
    env = {b'LANG': 'en_US.UTF-8'.encode('utf-8'), b'SHELL': '/bin/bash'.encode('utf-8'),}
    environ = _TextEnviron(env=env)
    assert isinstance(environ['LANG'], unicode)
    assert environ['LANG'] == u'en_US.UTF-8'
    assert isinstance(environ['SHELL'], unicode)
    assert environ['SHELL'] == u'/bin/bash'

    # Python 3.4-3.6
    env = {'LANG': 'en_US.UTF-8', 'SHELL': '/bin/bash',}
    environ = _TextEnviron(env=env)

# Generated at 2022-06-13 16:37:21.003283
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.update({'env_str': u'测试', 'env_bytes': b'\xe6\xb5\x8b\xe8\xaf\x95'})
    key_list = [u'env_str', 'env_bytes']
    for key in key_list:
        assert environ[key] == '测试'


# Generated at 2022-06-13 16:37:27.795438
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that the proxy returns text strings when called with text strings
    assert isinstance(environ['LANG'], str)
    assert isinstance(environ['LC_ALL'], str)
    # Test that the proxy returns text strings when called with a byte string
    assert isinstance(environ.__getitem__(b'LANG'), str)
    assert isinstance(environ.__getitem__(b'LC_ALL'), str)
    # Test that the proxy returns text strings when called with a byte string of a different
    # encoding than the underlying os.environ
    assert isinstance(environ.__getitem__(b'LANG', encoding='latin-1'), str)
    assert isinstance(environ.__getitem__(b'LC_ALL', encoding='latin-1'), str)
    # Test that the proxy returns

# Generated at 2022-06-13 16:37:38.895319
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # _TextEnviron should return unicode strings when running on Python 2
    # When running on Python 3, _TextEnviron should return the same strings as os.environ
    # _TextEnviron caches the decoded results of the environment variables so it only decodes each
    # variable once even if it changes during a run
    if PY3:
        # Python 3.x's os.environ should return strings
        assert isinstance(os.environ['HOME'], str)
    else:
        # Python 2.x's os.environ should return bytestrings
        assert isinstance(os.environ['HOME'], bytes)

    # _TextEnviron should return unicode strings
    assert isinstance(environ['HOME'], str)

    # _TextEnviron should only decode the environment variable once
    home = os.environ['HOME']

# Generated at 2022-06-13 16:37:47.064776
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    my_environ = _TextEnviron(encoding='utf-8')

    print("Test 1")
    test_key = 'USER'
    print("os.environ before: " + repr(os.environ[test_key]))
    print("my_environ before: " + repr(my_environ[test_key]))
    os.environ[test_key] = 'bob'
    my_environ[test_key] = 'bob'
    print("os.environ after: " + repr(os.environ[test_key]))
    print("my_environ after: " + repr(my_environ[test_key]))
    assert my_environ[test_key] == u'bob'

    print("Test 2")
    test_key = 'USER'
    test

# Generated at 2022-06-13 16:37:52.895347
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    assert env['LC_ALL'] == to_text(os.environ['LC_ALL'], encoding='utf-8')
    # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
    # instead of utf-8
    env.encoding = 'latin-1'
    assert env['LC_ALL'] == to_text(os.environ['LC_ALL'], encoding='latin-1')



# Generated at 2022-06-13 16:38:03.014893
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import tempfile
    if PY3:
        from unittest.mock import patch
    else:
        from mock import patch

    # Test with no environment variables
    with patch('os.environ', {}):
        env = _TextEnviron()
        assert env.get('good') is None
        with pytest.raises(KeyError):
            env['good']

    # Test with a good key
    with patch('os.environ', {'good': 'abc'}):
        env = _TextEnviron()
        assert env['good'] == 'abc'

    # Test with a bad key
    with patch('os.environ', {'bad_key': b'\xff'}):
        env = _TextEnviron()

# Generated at 2022-06-13 16:38:07.004150
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
   # Input parameters

   # Expected results
   expected = u'中文'

   # Actual results
   actual = environ[u'ANSIBLE_MODULE_ARGS']

   # Assertions
   assert expected == actual

# Generated at 2022-06-13 16:38:13.893702
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env_copy = environ.copy()
    environ.clear()
    try:
        # Test 'unicode' -> 'unicode'
        environ['foo'] = u'FOO'
        assert environ['foo'] == u'FOO'
        # Test 'str(bytes)' -> 'unicode'
        environ['bar'] = "BAR"
        assert environ['bar'] == u'BAR'
        # Test 'byte' -> 'unicode'
        environ['quux'] = b"QUUX"
        assert environ['quux'] == u'QUUX'
    finally:
        environ.clear()
        environ.update(env_copy)


# Generated at 2022-06-13 16:38:16.802276
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Python 2
    import ansible.module_utils._text
    if not PY3:
        assert ansible.module_utils._text.environ['PYTHONPATH'] == u'.'.encode('utf-8')

    # Python 3
    else:
        assert ansible.module_utils._text.environ['PYTHONPATH'] == u'.'


# Generated at 2022-06-13 16:38:32.804747
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:38:34.211379
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['BLAH'] == u''
    assert environ.encoding == 'utf-8'



# Generated at 2022-06-13 16:38:35.135698
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  environ['key'] = '\xe9'
  assert environ['key'] == 'é'



# Generated at 2022-06-13 16:38:46.486104
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_env = _TextEnviron({b'ANSIBLE_TEST': b'bytes_value',
                             'ANSIBLE_TEST2': 'unicode_value'})
    # First, test the __getitem__ method of _TextEnviron
    assert text_env['ANSIBLE_TEST'] == u'bytes_value'
    assert text_env['ANSIBLE_TEST2'] == u'unicode_value'

    # Now, test the __getitem__ method of the underlying data structure to ensure that the values
    # we read in were byte-strings
    assert text_env._raw_environ[b'ANSIBLE_TEST'] == b'bytes_value'
    assert text_env._raw_environ[u'ANSIBLE_TEST2'] == u'unicode_value'

    text_env = _TextEnviron

# Generated at 2022-06-13 16:38:50.865198
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'key': b'value', b'key2': b'value2'}, encoding='utf-8')
    assert environ[b'key'] == u'value'
    assert environ['key2'] == u'value2'

# Generated at 2022-06-13 16:39:01.323584
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {b'foo': 'this is a byte string'}
    assert environ[b'foo'] == 'this is a byte string'
    environ._raw_environ[b'foo'] = 'this is a text string'
    assert environ[b'foo'] == 'this is a text string'
    environ._raw_environ[b'fuu'] = b'this is a byte string'
    assert environ[b'fuu'] == 'this is a byte string'
    environ._raw_environ[b'fuu'] = u'this is a text string'
    assert environ[b'fuu'] == 'this is a text string'



# Generated at 2022-06-13 16:39:04.899379
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Ensures the method get the environment variables in text strings
    """

    environ["AA"] = "A" + chr(0x80) + "B"
    assert environ["AA"] == "A" + chr(0x80) + "B"

# Generated at 2022-06-13 16:39:15.421324
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Create a new environment variable
    # Do not replace existing environment variables with the same name
    os.environ.setdefault('TEST_NEW_VAR', '__NEW_VAR__')

    # Create a new environment variable with the same value as an existing environment variable
    # Do not replace existing environment variables with the same name
    os.environ.setdefault('TEST_SAME_VAL_AS_PATH', 'PATH')
    os.environ.setdefault('TEST_SAME_VAL_AS_LANG', 'C.UTF-8')

    # Create a new environment variable with a different value from an existing environment variable
    os.environ['TEST_DIFF_VAL_FROM_PATH'] = 'PATH'

# Generated at 2022-06-13 16:39:22.809586
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    # Tests
    #
    # 1. passing in unicode values on python 2
    # 2. passing in byte strings on python 2
    # 3. passing in unicode values on python 3
    # 4. passing in byte strings on python 3
    # 5. passing in non-string values raises an error on python 2
    # 6. passing in non-string values raises an error on python 3
    # 7. unicode values already in the environment get returned as unicode
    # 8. byte strings already in the environment get returned as unicode
    # 9. Attempting to get a nonexistent item raises an error
    #
    # Cases 1-6: All of these involve setting the environment variable
    # Cases 7-9: All of these involve getting the environment variable


# Generated at 2022-06-13 16:39:32.867276
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import sys
    if PY2:
        default_encoding = 'ascii'
        test_encoding = sys.getfilesystemencoding()
    else:
        default_encoding = sys.getfilesystemencoding()
        test_encoding = 'utf-8'
    # Default encoding
    environ_default_encoding = _TextEnviron()
    os.environ[to_bytes("TEST", encoding=default_encoding)] = "value"
    assert environ_default_encoding['TEST'] == "value"
    del os.environ[to_bytes("TEST", encoding=default_encoding)]
    # Non default encoding
    environ_non_default = _TextEnviron(encoding=test_encoding)

# Generated at 2022-06-13 16:39:47.684027
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Set Unicode variable
    key = 'FOREIGN_VARIABLE'
    value_text = u'\u00c5ngstr\u00f6m'
    value_bytes = value_text.encode()
    os.environ[key] = value_bytes
    value_text_returned = environ[key]
    assert value_text_returned == value_text

    # Set non-Unicode variable
    key = 'SYSTEM_VARIABLE'
    value = 'PWD'
    os.environ[key] = value
    value_returned = environ[key]
    assert value_returned == value



# Generated at 2022-06-13 16:39:58.037161
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Initialize the raw environment
    test_environ = {}
    test_environ[b'ANSIBLE_NET_SSH_KEYFILE'] = b'/home/toshio/.ssh/id_rsa'
    test_environ[b'COW'] = b'MOO'
    test_environ[b'BRAIN'] = b'100'
    test_environ[b'LANG'] = b'en_US.utf8'
    test_environ[b'PATH'] = b'/bin:/usr/bin'
    test_environ[b'PYTHONPATH'] = b'/home/toshio/src/ansible/lib/ansible/modules/network/'
    test_environ[b'PYTHONIOENCODING'] = b'utf8'

# Generated at 2022-06-13 16:40:06.224629
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    from sys import getfilesystemencoding
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import PY3

    # Fake out os.environ to a dict containing byte strings

# Generated at 2022-06-13 16:40:17.976670
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        del environ['PYTHONPATH']
    except KeyError:
        pass
    environ['PYTHONPATH'] = u'/foo/bar'
    assert environ['PYTHONPATH'] == u'/foo/bar'

    # encode the value to a different encoding
    environ['PYTHONPATH'] = u'/foo/bär'.encode('latin1')
    assert environ['PYTHONPATH'] == u'/foo/bär'

    # test when environment variable is set before environ is created
    # encode the value to a different encoding
    os.environ['PYTHONPATH'] = u'/foo/bär\udcc3'.encode('utf-32-le')

# Generated at 2022-06-13 16:40:19.954050
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['TEST'] == u'TEST'
    assert environ['TEST_NOT_SET'] == u''


# Generated at 2022-06-13 16:40:26.016730
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test passing a text key
    assert environ[to_text('PATH', errors='surrogate_or_strict')] == os.environ.get('PATH')

    # Test passing a byte string key
    assert environ[to_bytes('PATH', encoding='utf-8', errors='surrogate_or_strict')] == os.environ.get('PATH')



# Generated at 2022-06-13 16:40:28.991608
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Ensure that we get a text string back
    assert isinstance(environ['HOME'], str), 'environ["HOME"] should be a text string instance'


# Generated at 2022-06-13 16:40:37.732648
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert len(environ) > 0, len(environ)
    # It should return a unicode string
    assert isinstance(environ['PATH'], unicode)
    # It should return the same string if we keep hitting the same key
    valid = environ['PATH']
    assert valid == environ['PATH'], (valid, environ['PATH'])

    # It should raise the same exception as os.environ
    try:
        invalid = environ['nonexistent']
        assert False, invalid
    except KeyError:
        pass



# Generated at 2022-06-13 16:40:41.551695
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = '\u00e5'
    assert environ['foo'] == '\u00e5'

    environ['foo'] = '\xfe\xff'
    assert environ['foo'] == '\u00fe\ufffd'

    environ['foo'] = '\xfe'
    assert environ['foo'] == '\ufffd'



# Generated at 2022-06-13 16:40:46.994662
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = 'bar'
    assert environ['foo'] == 'bar'
    environ['spam'] = b'eggs'
    assert environ['spam'] == 'eggs'
    environ['spam'] = b'b\xc3\xa4'
    assert environ['spam'] == u'bä'

# Generated at 2022-06-13 16:41:02.352438
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = 'bar'
    assert isinstance(environ['foo'], str)
    assert environ['foo'] == 'bar'
    assert isinstance(environ._raw_environ['foo'], bytes)
    assert environ._raw_environ['foo'] == b'bar'
    assert isinstance(environ._value_cache[b'bar'], str)
    assert environ._value_cache[b'bar'] == 'bar'

# Generated at 2022-06-13 16:41:07.622876
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    bytes_result = os.environ['LANG']
    text_result = environ['LANG']

    assert(isinstance(bytes_result, bytes))
    assert(isinstance(text_result, unicode))
    assert(bytes_result.decode('utf-8') == text_result)


# Generated at 2022-06-13 16:41:17.170086
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up testing environment.
    if PY3:
        # If we're on python3, then os.environ returns unicode strings and we can just test to ensure
        # that we get the same value back
        environ_var = 'PYTHONPATH'
        sys_environ_value = os.environ[environ_var]
        test_environ_value = _TextEnviron()[environ_var]
        assert test_environ_value == sys_environ_value, 'Value mismatch for Unicode environment'
    else:
        # If we're on python2, os.environ returns byte strings.  So we encode a unicode string and
        # ensure that we're getting back the decoded value
        my_environ = {'TEST_VAR': 'This is a test'}
        # Use a mock

# Generated at 2022-06-13 16:41:27.034868
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron

    To run this test,
      # Install pytest
      pip install pytest

      # Run the test. The -k sets the test to only run the test matching this name
      pytest unit/utils/environment.py -k test__TextEnviron___getitem__
    """
    # Test whether the output text is correct
    assert environ['TEST_ENV_VAR'] == u'TEST_ENV_VAR_VAL'

    # Test whether the cache is working
    environ['TEST_ENV_VAR'] = u'TEST_ENV_VAR_NEW_VAL'
    assert environ['TEST_ENV_VAR'] == u'TEST_ENV_VAR_NEW_VAL'
    # Reset environment variable


# Generated at 2022-06-13 16:41:31.675505
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    old_environ = environ._raw_environ
    try:
        test_val = "abc\n"
        environ._raw_environ = {'test': test_val}
        assert test_val == environ['test']
    finally:
        environ._raw_environ = old_environ

# Generated at 2022-06-13 16:41:40.400094
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.text.sanitizers.init import environ

    # Test case - get unicode value
    env = {u'WEB_SERVER_URL': u'http://websrv.mycompany.com/myapp'}
    env_text = _TextEnviron(env, encoding='utf-8')
    assert isinstance(env_text.__getitem__(u'WEB_SERVER_URL'), unicode)

# Generated at 2022-06-13 16:41:47.032409
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=unused-variable
    te = _TextEnviron()
    te['unicode'] = u'Björk Guðmundsdóttir'
    te['utf-8'] = 'Björk Guðmundsdóttir'.encode('utf-8')
    te['utf-16-le'] = 'Björk Guðmundsdóttir'.encode('utf-16-le')
    te['latin-1'] = 'Björk Guðmundsdóttir'.encode('latin-1')

    assert te['unicode'] == u'Björk Guðmundsdóttir'
    assert te['utf-8'] == u'Björk Guðmundsdóttir'

# Generated at 2022-06-13 16:41:52.409791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # class _TextEnviron
    # -- Unit test for method __getitem__ of class _TextEnviron
    # -- Purpose: test method __getitem__ of class _TextEnviron

    # Class variables

    # local variables

    # test method __getitem__ of class _TextEnviron

    assert(id(environ) == id(_TextEnviron()))

# Generated at 2022-06-13 16:41:56.808865
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Source: https://docs.python.org/2/library/os.html#os.environ
    TEST_ENVIRON = to_bytes('{"HOME": "/home/user", "GATEWAY_INTERFACE": "CGI/1.1", "COLUMNS": "80"}')
    # 1: Get raw environment
    test_env = _TextEnviron(env=TEST_ENVIRON, encoding='utf-8')
    # 2: Get profile directory, environ['HOME']
    assert test_env['HOME'] == to_text('/home/user', encoding='utf-8')
    # 3: Get gateway, environ['GATEWAY_INTERFACE']
    assert test_env['GATEWAY_INTERFACE'] == to_text('CGI/1.1', encoding='utf-8')
    # 4:

# Generated at 2022-06-13 16:42:04.080595
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    my_environ = _TextEnviron({'test': b'M\xc3\xb6nchengladbach'})

    # Test that we get text back out
    val = my_environ['test']
    assert isinstance(val, bytes)
    assert val == b'M\xc3\xb6nchengladbach'

    # Test that we get back cached values when the same key is called multiple times
    val2 = my_environ['test']
    assert val is val2

    # Test that the cache is cleared when the underlying value changes
    my_environ['test'] = b'\xc3\xb6\xc3\xb6\xc3\xb6'
    val3 = my_environ['test']
    assert val != val3
    assert val3 is my_environ['test']

    # Test

# Generated at 2022-06-13 16:42:34.908517
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    class _TextEnvironTest(unittest.TestCase):
        """
        Class to test method _TextEnviron.__getitem__()
        """
        def test_getitem__on_Python_3(self):
            """
            Tests method _TextEnviron.__getitem__() on Python 3

            Assumes that os.environ returns a Python 3 string, which is true on all the Python
            versions tested.

            Python 3 strings are already a text string.
            """
            # Create a environ object to test
            environ = _TextEnviron()
            # Assert that the value of the environment variable is identical
            self.assertEqual(environ['PATH'], os.environ['PATH'])


# Generated at 2022-06-13 16:42:43.810967
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    nonascii = u'киба'
    unprintable = u'\x00'
    surrogate = u'\U00010000'
    environ['unicode'] = nonascii
    environ['unprintable'] = unprintable
    environ['surrogate'] = surrogate

    assert environ['unicode'] == nonascii
    assert environ['unprintable'] == unprintable
    assert environ['surrogate'] == surrogate

    del environ['unicode']
    del environ['unprintable']
    del environ['surrogate']

 # Unit test for method __setitem__ of class _TextEnviron

# Generated at 2022-06-13 16:42:50.616494
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({'a': 'x'}, 'ascii')
    assert environ['a'] == 'x'
    environ = _TextEnviron({b'a': b'x'}, 'ascii')
    assert environ['a'] == 'x'
    environ = _TextEnviron({'a': b'x'}, 'ascii')
    assert environ['a'] == 'x'
    environ = _TextEnviron({b'a': 'x'}, 'ascii')
    assert environ['a'] == 'x'



# Generated at 2022-06-13 16:43:01.884081
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text
    class MockEnviron(MutableMapping):
        def __init__(self):
            self._values = {
                to_bytes('mybytes', encoding='ascii'): to_bytes('mybytes', encoding='ascii'),
                b'mybytes2': b'mybytes2',
                to_bytes('myunicode', encoding='utf8'): to_bytes('myunicode', encoding='utf8'),
                to_bytes('myunicode2', encoding='utf8'): to_bytes('myunicode2', encoding='utf8'),
                'myunicode3': 'myunicode3',
                None: None,
            }

        def __delitem__(self, key):
            del self._values[key]


# Generated at 2022-06-13 16:43:04.901445
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {b'ANSIBLE_COW_SELECTION': b'random'}
    text_env = _TextEnviron(env=env, encoding='utf-8')
    assert text_env[u'ANSIBLE_COW_SELECTION'] == u'random'


# Generated at 2022-06-13 16:43:06.809401
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # type: () -> None
    environ['TEST_UTF8'] = u'Spéciàl chàrs'
    assert isinstance(environ['TEST_UTF8'], str)



# Generated at 2022-06-13 16:43:15.996850
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Good case
    environ = _TextEnviron(encoding='utf-8')
    environ['ABC'] = 'DEF'
    assert environ['ABC'] == 'DEF'

    # Bad case
    environ = _TextEnviron(encoding='utf-8')
    environ['ABC'] = b'\x80'
    try:
        environ['ABC']
    except Exception as error:
        assert isinstance(error, UnicodeDecodeError)
    else:
        raise AssertionError('UnicodeDecodeError not raised')


# Generated at 2022-06-13 16:43:23.935560
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common.collections_compat import MutableMapping
    import mock

    orig_environ = os.environ
    # Use mock.patch.dict() because the environ object we are trying to set is a MagicMock and it
    # isn't compatible with the _TextEnviron object being created.
    with mock.patch.dict('os.environ',
                         {'some_str': u'foo', 'some_unicode': u'\U0001f603', 'some_bytes': b'bar'}):
        text_env = _TextEnviron(os.environ)
        assert isinstance(text_env, MutableMapping)
        if PY3:
            assert text_env['some_str'] == u'foo'

# Generated at 2022-06-13 16:43:28.206166
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    mock_environ = {b'hello': b'world', 'hi': 'there'}

    result1 = _TextEnviron(mock_environ)['hello']
    assert result1 == 'world'

    result2 = _TextEnviron(mock_environ)['hi']
    assert result2 == 'there'



# Generated at 2022-06-13 16:43:30.492563
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({'ansible_python_interpreter': b'/usr/bin/python3'})
    assert env['ansible_python_interpreter'] == '/usr/bin/python3'

# Generated at 2022-06-13 16:43:55.988855
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test function __getitem__ of class _TextEnviron
    '''
    text_environ = _TextEnviron()
    # Test expected success
    result = text_environ.__getitem__('SHELL')
    assert result.startswith(u'/bin')
    # Test error condition
    text_environ['SHELL'] = 'value'
    try:
        result = text_environ.__getitem__('SHELL')
    except:
        result = None
    # Test expected success
    assert result is None


# Generated at 2022-06-13 16:44:01.980190
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test that we return items of the right types
    '''
    # Test make sure we return a text value when encoding is utf-8
    os.environ[to_text('foo', 'utf-8')] = to_bytes('\xc3\xa9\xc3\xae', 'utf-8')
    _environ = _TextEnviron(env={to_bytes('foo', 'utf-8'): to_bytes('\xc3\xa9\xc3\xae', 'utf-8')},
                            encoding='utf-8')
    assert u"\u00e9\u00ee" == _environ[to_text('foo', 'utf-8')]

    # Test that we can decode a latin1 encoded value correctly

# Generated at 2022-06-13 16:44:13.208917
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a test environment with several unicode characters
    os.environ['key1'] = u'value1'
    os.environ['key2'] = u'value2'
    os.environ['key3'] = u'中文'

    # Make sure that a for loop returns unicode bytes
    for key, value in os.environ.items():
        if hasattr(value, 'decode'):
            assert isinstance(value, bytes)
            assert isinstance(value.decode(sys.getfilesystemencoding()), unicode)

    # Get the value of all three keys and make sure they're unicode
    assert u'value1' == environ['key1']
    assert u'value2' == environ['key2']
    assert u'中文' == environ['key3']

    #

# Generated at 2022-06-13 16:44:17.313235
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'key1': b'value1', b'key2': b'value2'})  # pylint: disable=redefined-outer-name
    for key, value in env.items():
        assert isinstance(key, str)
        assert isinstance(value, str)



# Generated at 2022-06-13 16:44:23.930961
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import text_type
    e = _TextEnviron({b'A': b'a', 'B': u'\u2119'})
    assert e['A'] == u'a'
    assert isinstance(e['A'], text_type)
    assert e['B'] == u'\u2119'
    assert isinstance(e['B'], text_type)



# Generated at 2022-06-13 16:44:26.041563
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  env = _TextEnviron()
  env['key1'] = 'value1'
  assert env['key1'] == 'value1'


# Generated at 2022-06-13 16:44:37.329399
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Initialize an instance of _TextEnviron with the demo environment
    env = _TextEnviron({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}, encoding='utf-8')

    # Check that the demo environment is properly cached
    assert len(env) == 3
    assert 'key1' in env
    assert 'key2' in env
    assert 'key3' in env

    # Check that direct access works as expected
    assert env['key1'] == 'value1'
    assert env['key2'] == 'value2'
    assert env['key3'] == 'value3'

    # Check that access after updating a key works as expected
    env['key1'] = 'value4'
    assert env['key1'] == 'value4'

# Generated at 2022-06-13 16:44:44.903021
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import sys
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import MutableMapping, Iterable
    from ansible.module_utils.common.text_env import _TextEnviron

    assert isinstance(environ, MutableMapping)
    # Returns expected result
    if PY3:
        from os import environ as _environ
        assert environ == _environ
    else:
        from os import environ as _environ
        assert isinstance(_environ, MutableMapping)
        assert len(environ) == len(_environ)
        assert list(environ.keys()) == list(_environ.keys())

# Generated at 2022-06-13 16:44:56.846692
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Run the method on the object for each item in the test_data
    for test_item in test__TextEnviron___getitem__.test_data:
        test_name, test_in, expected_out = test_item
        # Call the function
        actual_out = environ.__getitem__(test_in)
        # Test the result
        if actual_out != expected_out:
            raise Exception('Out did not match: actual: %s expected: %s' % (actual_out, expected_out))


# Generated at 2022-06-13 16:44:59.845081
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Check that _TextEnviron.__getitem__(item) returns a text type for any value of item
    """
    for env_variable in environ:
        assert isinstance(environ[env_variable], text_type)

# Generated at 2022-06-13 16:45:41.498166
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env_item = os.environ.__getitem__

    # Test multibyte values
    key = 'SSH_CLIENT'
    value_bytes = env_item(key)
    # Test nonstring values
    key = 'SHLVL'
    value_bytes = env_item(key)

    # Test different encoding values
    # Test no encoding provided
    env = _TextEnviron(encoding=None)
    value_text_default = env[key]
    # Test utf-8 encoding provided
    env = _TextEnviron(encoding='utf-8')
    value_text_utf8 = env[key]
    # Test system encoding provided
    env = _TextEnviron(encoding=sys.getfilesystemencoding())
    value_text_sys = env[key]

    # Test grabbing variables twice