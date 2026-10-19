

# Generated at 2022-06-13 16:35:58.048334
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def sample_env():
        """Return a sample environment with a byte-based and text-based envvar"""
        env = os.environ.copy()
        env.update({b'FOO': b'bar', 'FOO': 'baz'})
        return env

    # If we're on Python 3, we expect the environment to work even though the examples use bytes
    if PY3:
        env = _TextEnviron(sample_env())
        assert env['FOO'] == 'baz'
        return

    # Bytes key is decoded to the text FOO
    env = _TextEnviron(sample_env(), encoding='utf-8')
    assert env[b'FOO'] == 'bar'

    # Text key is unchanged
    assert env['FOO'] == 'baz'

    # Non-ascii bytes encode

# Generated at 2022-06-13 16:36:07.784819
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test 1: Retrieve a unicode value from the environment
    os.environ['ANSIBLE_TEST_UNICODE_ENV'] = '€'
    assert environ['ANSIBLE_TEST_UNICODE_ENV'] == u'€'
    assert environ.encoding == 'utf-8'
    del os.environ['ANSIBLE_TEST_UNICODE_ENV']

    # Test 2: Retrieve a byte string from the environment
    os.environ['ANSIBLE_TEST_BYTE_ENV'] = b'\xe2\x82\xac'
    assert environ['ANSIBLE_TEST_BYTE_ENV'] == u'€'
    assert environ.encoding == 'utf-8'

# Generated at 2022-06-13 16:36:19.270578
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make sure the class returns byte strings as unicode
    test_env = _TextEnviron()
    test_env['LANG'] = u'en_US.UTF-8'
    assert isinstance(test_env['LANG'], unicode)

    # Make sure we can read a unicode value from the environment
    os.environ[u'LANG'] = u'ja_JP.UTF-8'
    assert isinstance(test_env['LANG'], unicode)

    # Make sure we can read a utf-8 encoded value from the environment and get it as unicode
    os.environ[u'LANG'] = b'ja_JP.UTF-8'
    assert isinstance(test_env['LANG'], unicode)

    # Make sure we can read a latin1 encoded value from the environment and get it

# Generated at 2022-06-13 16:36:24.772895
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ.__getitem__('LANG') == 'en_US.UTF-8'
    assert environ.__getitem__('BINARY_ENV') == u'\u2021'
    assert environ.__getitem__('UNICODE_ENV') == u'\u2022'


# Generated at 2022-06-13 16:36:28.870378
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = 'bar'
    assert environ['foo'] == 'bar'

    environ['foo'] = '\n'
    assert environ['foo'] == '\n'

    environ['foo'] = '\xfc'
    assert environ['foo'] == '\xfc'



# Generated at 2022-06-13 16:36:37.499984
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    #
    # The default key in os.environ is unset on both Python2 and Python3
    #
    assert 'DEFAULT' not in os.environ
    assert 'DEFAULT' not in environ
    #
    # Set a value in the local os.environ variable
    #
    os.environ['DEFAULT'] = b'asdf'
    #
    # With Python3, there's nothing extra we need to do to get the value back
    #
    assert os.environ['DEFAULT'] == u'asdf'
    if PY3:
        assert environ['DEFAULT'] == u'asdf'
    else:
        #
        # With Python2, we need to decode the value
        #
        assert environ['DEFAULT'] == u'asdf'
    #
    # Set a value in

# Generated at 2022-06-13 16:36:46.666169
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import sys

    # Verify that bytes values are returned and decoded on py2 but not on py3
    environ_test = _TextEnviron({b'foo': b'bar'}, encoding='ascii')
    assert environ_test[b'foo'] == u'bar' if not PY3 else b'bar'

    # Verify that unicode values are returned on py2 and py3
    environ_test = _TextEnviron({b'foo': u'bar'}, encoding='ascii')
    assert environ_test[b'foo'] == u'bar'

    # Verify that bad values are not decoded on py2 but are on py3
    environ_test = _TextEnviron({b'foo': b'bar\x80'}, encoding='ascii')

# Generated at 2022-06-13 16:36:54.113842
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _test_environment_variable(value, expected_output):
        env_mock = {}
        env_mock[value] = value
        environ_test = _TextEnviron(env=env_mock)
        assert environ_test[value] == expected_output

    _test_environment_variable('', '')
    _test_environment_variable('ascii', 'ascii')
    _test_environment_variable('\xe9\xe9\xe9', '\xe9\xe9\xe9')
    _test_environment_variable('\xe9\xe9\xe9\x0a', '\xe9\xe9\xe9\n')

# Generated at 2022-06-13 16:37:03.736799
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test1: Default environ variable
    assert environ['HOME'] == os.environ['HOME']
    # test2: New variable set in environ variable
    environ['TEST'] = 'TEST'
    assert environ['TEST'] == 'TEST'
    # test3: Variable set in environ variable changed to new value
    environ['TEST'] = 'TEST2'
    assert environ['TEST'] == 'TEST2'
    # test4: Variable removed from environ variable
    del environ['TEST']
    with pytest.raises(KeyError):
        environ['TEST']



# Generated at 2022-06-13 16:37:08.514061
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST_ONE'] = 'value one'
    os.environ['TEST_TWO'] = 'value two'
    expected_warnings = 'surrogateescape' in errors and sys.platform.startswith('linux')
    assert len(environ) == 2
    assert 'TEST_ONE' in environ
    assert 'TEST_TWO' in environ
    assert environ['TEST_ONE'] == 'value one'
    assert environ['TEST_TWO'] == 'value two'

# Generated at 2022-06-13 16:37:18.152406
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import StringIO

    def _check_unicode_envvar_value(p1, p2):
        """
        :param p1: bytes string
        :param p2: expected unicode strings
        :return: True | False
        """
        return (to_text(p1) == p2) or (to_text(p1, errors='surrogate_or_strict') == p2)

    t = TextEnviron()
    # text string ver.
    t['foo'] = 'bar'
    assert t['foo'] == 'bar'

    # bytes strings ver.
    t = TextEnviron()
    t['x'] = b'y'
    assert t['x'] == 'y'

    t = TextEnviron()

# Generated at 2022-06-13 16:37:26.481145
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import mock
    import sys
    import copy
    import os

    _original_environ = copy.deepcopy(os.environ)

# Generated at 2022-06-13 16:37:38.306219
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import tempfile
    fd, fname = tempfile.mkstemp()
    with open(fname, 'w') as f:
        f.write('foo')

    # Test non-latin character encoding
    os.environ['FOO'] = '\xed\x95\x9c\xea\xb8\x80'
    assert environ['FOO'] == u'\uc548\ub155'

    # Test that we get bytes back under Py2
    if not PY3:
        assert isinstance(environ['FOO'], str)

    # Test that using `nonstring='passthru'` gets us bytes
    os.environ['FOO'] = fname
    assert isinstance(environ['FOO'], str)
    assert environ['FOO'] == fname

    # Make

# Generated at 2022-06-13 16:37:39.182758
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # unittest_util.getPython
    pass

# Generated at 2022-06-13 16:37:51.583774
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Decode a simple element that doesn't need to be decoded
    test_dict = {b'ANSIBLE_FOO': 'bar'}
    te = _TextEnviron(test_dict)
    assert te['ANSIBLE_FOO'] == 'bar'

    # If we encode to utf-8 and decode back to utf-8, we should get the same value from the dict
    utf8_value = to_bytes('baz', encoding='utf-8')
    test_dict = {to_bytes('ANSIBLE_BAZ'): utf8_value}
    te = _TextEnviron(test_dict)
    assert te['ANSIBLE_BAZ'] == to_text(utf8_value)

    # Feed it a latin-1 value and decode as utf-8.  We should get the correct unicode literal.

# Generated at 2022-06-13 16:37:56.267627
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({b'ONE': b'one', b'TWO': b'two'})
    assert e[b'ONE'] == u'one'
    assert e[b'TWO'] == u'two'



# Generated at 2022-06-13 16:38:03.593211
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    environ = _TextEnviron(encoding='utf-8')

    # Test 1: Environment variable encoded in utf-8
    environ._raw_environ['TEST_VARIABLE'] = '$€банки'
    assert '$€банки' == environ['TEST_VARIABLE']

    # Test 2: Environment variable encoded in ascii
    environ._raw_environ['TEST_VARIABLE'] = b'abc123'
    assert 'abc123' == environ['TEST_VARIABLE']

# Generated at 2022-06-13 16:38:09.321286
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    e = _TextEnviron()
    try:
        e[u'test_key'] = u'test_value'
    except UnicodeEncodeError:
        return False
    except TypeError:
        return True
    else:
        return False


# Generated at 2022-06-13 16:38:16.518256
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text
    from unittest import TestCase
    from unittest.mock import patch, MagicMock

    class MockDict(dict):
        def __getitem__(self, key):
            return self[key]
        def __delitem__(self, key):
            del self[key]
        def __setitem__(self, key, value):
            self[key] = value

    class Test_TextEnviron(TestCase):
        def test_test__TextEnviron___getitem__(self):
            value = b'secret'
            env = _TextEnviron(env={'key': value})
            env['key'] = 'password'
            self.assertEqual(env['key'], 'password')

# Generated at 2022-06-13 16:38:23.518520
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    env._raw_environ = {b'name': b'value'}
    result = env.__getitem__("name")
    assert result == u'value'

    env._raw_environ = {u'name': u'value'}
    result = env.__getitem__("name")
    assert result == u'value'

# Generated at 2022-06-13 16:38:34.399448
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''Set environment variable, retrieve it and delete it.
    Assert that the retrieved value is the expected text string.
    '''
    # Test for an environment variable which should be ASCII text
    key = 'ANSIBLE_TEST_VAR'
    value = 'test'
    os.environ[key] = value
    assert value == environ[key]
    del os.environ[key]

    # Test for an environment variable which should start out as bytes then get converted to
    # unicode in the os.environ dictionary
    key = 'ANSIBLE_TEST_VAR'
    value = b'\xe9\xa9\x99'
    os.environ[key] = value
    assert b'\xe9\xa9\x99' == os.environ[key]
    assert u'驙'

# Generated at 2022-06-13 16:38:45.392251
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    import unittest
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils._text import to_text, to_bytes, to_native
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.environment import environ, _TextEnviron

    old_stdout = sys.stdout
    sys.stdout = BytesIO()

    class Environ(MutableMapping):
        """
        Unit test: Use this class to force UTF-8, non-ascii environment variable values
        """

# Generated at 2022-06-13 16:38:49.069734
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test get method, initialized with "ABC"
    testee = _TextEnviron(env=dict(A="ABC"))

    assert testee["A"] == u"ABC"

# Generated at 2022-06-13 16:38:58.504171
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    # Note that there isn't a good way to test UTF-8 because it's not a safe choice for ansible
    # settings.  If this test is run via tox, then the tests are run under UTF-8.  If running it in
    # the source directory then it will be the locale's choice of encoding.
    #
    # So instead we test that an encoding with non-ascii chars converts properly
    if os.path.exists('.env'):
        for line in open('.env'):
            if line.startswith('ASCII_ENCODING='):
                os.environ[line.split('=')[0]] = line.split('=')[1].rstrip()
                break
        else:
            raise AssertionError("Could not find ASCII_ENCODING in .env")

# Generated at 2022-06-13 16:39:07.548121
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    _raw_environ = {b'aa': b'10', b'bb': b'20'}

    class __raw_environ():
        def __getitem__(self, key):
            return _raw_environ[key]
        def __len__(self):
            return len(_raw_environ)
        def __iter__(self):
            return _raw_environ.__iter__()

    environ = _TextEnviron(env=__raw_environ())

    if PY3:
        assert environ['aa'] == b'10'
        assert environ['bb'] == b'20'
    else:
        assert environ['aa'] == u'10'
        assert environ['bb'] == u'20'

    assert len(environ) == 2
    assert len(_raw_environ)

# Generated at 2022-06-13 16:39:18.068534
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import sys
    import os
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import MutableMapping

    class _TextEnviron(MutableMapping):
        """
        Utility class to return text strings from the environment instead of byte strings

        Mimics the behaviour of os.environ on Python3
        """
        def __init__(self, env=None, encoding=None):
            if env is None:
                env = os.environ
            self._raw_environ = env
            self._value_cache = {}
            # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
            # instead of utf-8

# Generated at 2022-06-13 16:39:22.333665
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == u'/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/tools/node/bin:/tools/google-cloud-sdk/bin'

# Generated at 2022-06-13 16:39:32.447827
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    import unittest

    class test__TextEnviron___getitem__(unittest.TestCase):
        def test_type(self):
            import os

            # TextEnviron is a dict
            assert isinstance(environ, dict)

            # TextEnviron is a dict compatible with Python3 dict
            assert hasattr(environ, "__setitem__")
            assert hasattr(environ, "__getitem__")
            assert hasattr(environ, "__delitem__")
            assert hasattr(environ, "__iter__")

            # No problem to use the dict
            assert environ["PATH"] == os.environ["PATH"]

        def test_unicode_key(self):

            import sys
            from ansible.module_utils.common._collections_compat import MutableMapping

            text_en

# Generated at 2022-06-13 16:39:42.630877
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def fake_getfilesystemencoding():
        return 'utf-8'

    def revert_getfilesystemencoding():
        sys.getfilesystemencoding = orig_sys_getfilesystemencoding

    orig_sys_getfilesystemencoding = sys.getfilesystemencoding
    sys.getfilesystemencoding = fake_getfilesystemencoding

    # Python2, ascii value
    env = _TextEnviron({'test': u'\xe9'.encode('utf-8')})
    assert env['test'] == u'\xe9'

    # Python2, bytes value decoded to non-ascii
    env = _TextEnviron({'test': '\xe9'})
    assert env['test'] == u'\xe9'

    # Python2, bytes value decoded to ascii
    env

# Generated at 2022-06-13 16:39:55.220235
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = os.environ.copy()
    env['value_str'] = 'str_value'
    env['value_bytes'] = b'bytes_value'
    if PY3:
        env['value_str_decoded_as_bytes'] = str('str_value_decoded_as_bytes')
    else:
        env['value_str_decoded_as_bytes'] = 'str_value_decoded_as_bytes'
    env = _TextEnviron(env, encoding='utf-8')
    assert 'value_str' in env
    assert 'value_bytes' in env
    assert 'value_str_decoded_as_bytes' in env
    assert env['value_str'] == 'str_value'
    assert env['value_bytes'] == 'bytes_value'

# Generated at 2022-06-13 16:40:07.983352
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Env is a dictionary but must not be updated from outside
    environ = _TextEnviron({b'foo': b'bar'})
    assert environ['foo'] == u'bar'

    # Env is a dictionary but must not be updated from outside
    dictEnv = {b'foo': b'bar'}
    environ = _TextEnviron(dictEnv)
    assert environ['foo'] == u'bar'
    dictEnv[b'foo'] = b'bar2'
    # Should not be updated
    assert environ['foo'] == u'bar'

    # Env is a dictionary but must not be updated from outside
    dictEnv = {b'foo': b'bar'}
    environ = _TextEnviron(dictEnv)
    assert environ['foo'] == u'bar'


# Generated at 2022-06-13 16:40:19.505013
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class TestEnviron(object):
        def __init__(self, value):
            self._value = value

        def __getitem__(self, key):
            return self._value

        def __delitem__(self, key):
            pass

        def __setitem__(self, key, value):
            pass

        def __iter__(self):
            return self._value.__iter__()

        def __len__(self):
            return len(self._value)

    class UTF8Environ(TestEnviron):
        def __getitem__(self, key):
            # note that the test string has both bytes and unicode
            return b'\xc3\xa9'.decode('utf-8')


# Generated at 2022-06-13 16:40:29.323628
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _OSEnviron(object):
        def __init__(self):
            self.data = {
                b'key': b'value',
                b'key2': u'value2',
                'key3': b'value3',
                'key4': u'value4',
            }
        def __getitem__(self, key):
            return self.data[key]
        def __setitem__(self, key, value):
            self.data[key] = value
        def __delitem__(self, key):
            del self.data[key]
        def __iter__(self):
            return iter(self.data)
        def __len__(self):
            return len(self.data)
    NONE_DATA = {}
    NONE_DATA.update(b'key', b'value')

# Generated at 2022-06-13 16:40:31.107219
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == os.environ['HOME']

# Generated at 2022-06-13 16:40:41.309762
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    import ansible.module_utils.six

    environ_test = _TextEnviron(encoding='utf-8')

    # key not found
    assert environ_test['FOO'] == ''

    # key is byte string, value is byte string
    environ_test._raw_environ['key_as_bytes'] = to_bytes('bar_as_bytes', encoding='utf-8')
    assert environ_test['key_as_bytes'] == 'bar_as_bytes'

    # key is byte string, value is text string
    environ_test._raw_environ['key_as_bytes'] = to_text('bar_as_text', errors='surrogate_or_strict')
    assert environ_test['key_as_bytes'] == 'bar_as_text'

    # key is text string,

# Generated at 2022-06-13 16:40:47.963230
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # create an instance of _TextEnviron
    __instance = _TextEnviron()

    # Return text string from the environment instead of byte strings
    __expected = 'export DJANGO_SETTINGS_MODULE="app.settings"\n'
    __actual = __instance.__getitem__('LABEL_TRAVIS_TEST_PYTHON_VERSIONS')
    if __expected != __actual:
        raise Exception('TestID: TEST_1 failed: expected: %s, actual: %s' % (
            __expected, __actual))


if __name__ == '__main__':
    # Run the unit test
    test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:40:55.267425
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that strinngs are decoded
    decoded_val = 'decoded_val'
    environ = _TextEnviron({'key': decoded_val.encode(environ.encoding)})
    assert environ['key'] == decoded_val

    # Check that unicode strings are returned as is
    unicode_val = 'unicode_val'
    environ = _TextEnviron({'key': unicode_val})
    assert environ['key'] == unicode_val

    # Check that bytes which cannot be decoded are returned as is
    invalid_bytes = b'\xff'
    environ = _TextEnviron({'key': invalid_bytes})
    assert environ['key'] == invalid_bytes



# Generated at 2022-06-13 16:40:58.759881
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'F\xc3\xa1bio': b'Brasil'}, encoding='utf-8')
    assert env['Fábio'] == u'Brasil'


# Generated at 2022-06-13 16:41:05.712740
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {'utf-8': 'a', 'latin-1': b'b\xa0\xa1', 'surrogate': b'c\xed\xa0\x80d'}
    environ._value_cache = {}

    assert environ['utf-8'] == 'a'
    assert environ['latin-1'] == u'b\xa0\xa1'
    # Surrogate pairs should be removed
    assert environ['surrogate'] == u'cd'

    environ._value_cache = {b'a': u'a2', b'b\xa0\xa1': u'b\xa0\xa1', b'c\xed\xa0\x80d': u'cd'}

    assert environ['utf-8'] == 'a2'


# Generated at 2022-06-13 16:41:14.405995
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    print('Testing method __getitem__ of class _TextEnviron')
    import sys
    import os
    from ansible.module_utils.six import PY3

    # Set an expected environment variable
    key = 'ANSIBLE_TEST_ENCODING'
    expected_value = 'あ'
    if not PY3:
        expected_value = expected_value.decode(environ.encoding)
    os.environ[key] = expected_value

    # Make sure that we get the expected environment variable back
    assert(environ[key] == expected_value)
    print('Success!')


# Generated at 2022-06-13 16:41:22.637545
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_test = _TextEnviron()
    assert set(environ_test.keys()) == set(os.environ.keys())
    assert environ_test['PWD'] == os.environ['PWD']
    assert environ_test['PWD'].__class__ == os.environ['PWD'].__class__


# Generated at 2022-06-13 16:41:29.151969
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron(env=dict(foo=b'bar'))
    assert e['foo'] == 'bar'

    e = _TextEnviron(env=dict(foo='bar'))
    assert e['foo'] == 'bar'

    e = _TextEnviron(env=dict(foo=u'bar', baz=u'p\N{LATIN SMALL LETTER SHARP S}ng'))
    assert e['foo'] == 'bar'
    assert e['baz'] == u'p\N{LATIN SMALL LETTER SHARP S}ng'


# Generated at 2022-06-13 16:41:39.062535
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Construct with the raw environ that would be returned by the system
    host_environ = _TextEnviron(encoding='utf-8')

    # Keys and values that should be returned as byte strings
    byte_keys = [
        b'PATH',
        b'LANG',
        b'PWD',
        b'SHELL',
        b'USER',
        b'HOME',
        b'LOGNAME',
        b'TMPDIR',
        b'TMPDIR',
        b'TERM',
        b'SELINUX_LEVEL_REQUESTED',
        b'SELINUX_ROLE_REQUESTED',
        b'SELINUX_USE_CURRENT_RANGE',
    ]

# Generated at 2022-06-13 16:41:46.079774
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up environment variables which will be tested below
    os.environ[b'LEGACY_BYTES_ENV_VAR'] = b'byte\xc3\xb1g'
    os.environ[u'LEGACY_UNICODE_ENV_VAR'] = u'unicode\xf1g'
    if hasattr(os, 'fsencode'):
        os.environ[u'FS_ENCODE_UNICODE_ENV_VAR'] = u'unicode\xf1g'

    # If we're on Python3, then os.environ already returns text strings
    if PY3:
        assert b'LEGACY_BYTES_ENV_VAR' in os.environ

# Generated at 2022-06-13 16:41:50.227890
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PYTHONPATH'] == u'/usr/lib/python2.7/site-packages:/usr/lib/python2.7/site-packages/asn1crypto-0.24.0-py2.7.egg'

# Generated at 2022-06-13 16:41:56.261138
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''Test method __getitem__ of class _TextEnviron'''
    env = _TextEnviron()
    env.encoding = 'utf-8'
    env._raw_environ = {'key1': b'foo', 'key2': u'bar'}
    env._value_cache = {}
    env.__getitem__('key1')
    assert env._value_cache == {b'foo': u'foo'}


# Generated at 2022-06-13 16:42:03.645933
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = {b'byte': b'byteval', b'text_utf8': to_bytes('text_utf8_val', errors='strict', encoding='utf-8'),
                    b'text_latin1': to_bytes('text_latin1_val', errors='strict', encoding='latin1'),
                    b'invalid_utf8': to_bytes('inval\xc3\x28id', errors='ignore', encoding='utf-8')}
    test_env = _TextEnviron(test_environ, encoding='utf-8')
    assert test_env[b'byte'] == 'byteval'
    assert test_env[b'text_utf8'] == 'text_utf8_val'

# Generated at 2022-06-13 16:42:15.394030
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up an immutable input to test with
    environ = _TextEnviron({b'a': b'b', b'c': b'd'})

    assert environ[b'a'] == u'b'
    assert environ[u'a'] == u'b'
    assert environ['a'] == u'b'

    assert environ[b'c'] == u'd'
    assert environ[u'c'] == u'd'
    assert environ['c'] == u'd'

    # Test with a non-ascii string
    if PY3:
        assert environ[u'ちょっと'] == u'ちょっと'

# Generated at 2022-06-13 16:42:22.457537
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_VAR'] = b'hello world'
    assert environ['TEST_VAR'] == u'hello world'
    environ['TEST_VAR'] = u'hello world'
    assert environ['TEST_VAR'] == u'hello world'
    environ['TEST_VAR'] = b'goodbye world'
    assert environ['TEST_VAR'] == u'goodbye world'
    environ['TEST_VAR'] = u'goodbye world'
    assert environ['TEST_VAR'] == u'goodbye world'
    del environ['TEST_VAR']

# Generated at 2022-06-13 16:42:25.749724
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The `unicode` on python 2 is the same as `str` on python 3.
    try:
        unicode
    except NameError:
        unicode = str

    # Test that it returns unicode on python 2.
    assert isinstance(environ['LANG'], unicode)



# Generated at 2022-06-13 16:42:40.182449
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['IBM_DEFAULT_CODE_PAGE'] = '1252'  # Western Europe
    assert environ['IBM_DEFAULT_CODE_PAGE'] == '1252'

# Generated at 2022-06-13 16:42:50.364856
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest

    expected_value = {'TEST': to_bytes('blah', encoding='utf-8', nonstring='strict', errors='surrogate_or_strict')}
    assert_value = {'TEST': 'blah'}
    environ = _TextEnviron(expected_value, 'utf-8')
    assert environ == assert_value
    environ['TEST2'] = 'blah2'
    assert_value['TEST2'] = 'blah2'
    assert environ == assert_value
    del environ['TEST2']
    assert len(environ) == 1
    with pytest.raises(KeyError):
        environ['TEST2']
    assert len(environ) == 1



# Generated at 2022-06-13 16:42:55.269827
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({to_bytes('asciivalue'): to_bytes('asciistring')})
    if not PY3:
        result = environ[to_bytes('asciivalue')]
        assert result == to_text('asciistring')


# Generated at 2022-06-13 16:43:04.610458
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test normal parameters
    environ['TEST1'] = 'a'
    assert environ['TEST1'] == 'a'
    assert environ._raw_environ['TEST1'] == b'a'

    # Test parameter value which contains unicode characters
    environ['TEST2'] = u'b\u1234'
    assert environ['TEST2'] == u'b\u1234'
    assert environ._raw_environ['TEST2'] == b'b\xe1\x88\xb4'

    # Test after the content of an environment variable changes
    environ['TEST3'] = 'c'
    assert environ['TEST3'] == 'c'
    assert environ._raw_environ['TEST3'] == b'c'

# Generated at 2022-06-13 16:43:08.653395
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST1'] = 'TEST1'
    os.environ['TEST2'] = 'É'
    os.environ['TEST3'] = '。'

    assert environ['TEST1'] == 'TEST1'
    assert environ['TEST2'] == u'\xc9'
    assert environ['TEST3'] == u'\u3002'

    assert environ['TEST1'] == 'TEST1'
    assert environ['TEST2'] == u'\xc9'
    assert environ['TEST3'] == u'\u3002'

# Generated at 2022-06-13 16:43:20.185092
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Verify that the __getitem__ function works as expected.
    """
    # Verify that we get text back from a known value
    assert isinstance(environ['PATH'], str)
    # Verify that we get text back from a known value that is a bytes type
    known_value = b'\xc3\xa9'
    os.environ[to_bytes('KNOWN_VALUE', encoding='ascii')] = known_value
    assert environ['KNOWN_VALUE'] == to_text(known_value, encoding='utf-8')
    # Verify that we get non-textual values back
    assert environ['KNOWN_VALUE'] is not None
    os.environ[to_bytes('KNOWN_VALUE', encoding='ascii')] = b'True'
    assert environ['KNOWN_VALUE'] is True

# Generated at 2022-06-13 16:43:25.630955
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # This test requires the following Python 3 conversion methods:
    # - to_text
    # - to_bytes
    # - sys.getfilesystemencoding
    # - bytes.__eq__
    # - str.__eq__
    # - str.encode

    # Import the required method implementations to use with Python 2
    from ansible.module_utils.six import to_text, to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping
    from sys import getfilesystemencoding

    # Assign the required method implementations to use with Python 2
    sys.getfilesystemencoding = getfilesystemencoding

    # Additional Python 2 units imports because the Python 3 to_bytes is used with the
    # Python 2 bytes.__eq__ method
    from six import u

    # Python 2 bytes.

# Generated at 2022-06-13 16:43:32.991128
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    fake_env = {}
    # Ensure that the env we pass in is the one we're using for our tests
    test_env = _TextEnviron(fake_env)

    # Simple value test
    fake_env['test'] = 'abc'
    assert test_env['test'] == 'abc'

    if not PY3:
        # Test value encoding
        fake_env['test_encoding'] = b'\xc3\xbc'
        assert test_env['test_encoding'] == '\u00fc'

        # Test that cached values are used
        test_env['test_cached'] = b'\xc3\xbc'
        fake_env['test_cached'] = b'\xc2\xbc'
        assert test_env['test_cached'] == '\u00fc'

        # Test

# Generated at 2022-06-13 16:43:43.546940
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Verify that it retrieves a simple value, handling the bytes to text
    # conversion correctly (including surrogate escaping, not just strict)
    os.environ['ANSIBLE_TEST_VAL'] = b'\xff\xf6\xe2\xc4\x00'
    val = environ['ANSIBLE_TEST_VAL']

# Generated at 2022-06-13 16:43:49.640490
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ.clear()
    os.environ['TEST_VARIABLE'] = 'TEST_VALUE'
    os.environ['TEST_VALUE_2'] = 'TEST_VALUE_2'
    environ = _TextEnviron()
    assert isinstance(environ.get('TEST_VARIABLE'), str)
    assert environ['TEST_VARIABLE'] == 'TEST_VALUE'
    assert environ['TEST_VALUE_2'] == 'TEST_VALUE_2'
    os.environ.clear()


# Generated at 2022-06-13 16:44:19.109770
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()

    # unset
    if '_ANSIBLE_TEST_UNSET' in env:
        del env['_ANSIBLE_TEST_UNSET']
    assert '_ANSIBLE_TEST_UNSET' not in env

    # bytes
    env['_ANSIBLE_TEST_BYTES'] = b'bar'
    assert env['_ANSIBLE_TEST_BYTES'] == 'bar'

    # text
    env['_ANSIBLE_TEST_TEXT'] = 'foo'
    assert env['_ANSIBLE_TEST_TEXT'] == 'foo'

    # unicode
    py2_only = 'unicode'
    env[py2_only] = u'\xe9'
    assert env[py2_only] == '\xe9'

    # non-string

# Generated at 2022-06-13 16:44:31.222828
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that key not in os.environ throws KeyError
    environ_keys = environ.keys()
    # We are using ascii here rather than utf-8 to avoid having to encode/decode the string.  We
    # set the encoding to utf-8 so that non-ascii characters will work.
    key = 'ansible_test_key'
    while key in environ_keys:
        key += '1'

    try:
        environ[key]
    except KeyError:
        pass
    else:
        raise AssertionError('ansible.module_utils.six.moves.environ should throw KeyError when '
                             'key not in os.environ')

    # Test that encoding/decoding works

# Generated at 2022-06-13 16:44:40.439846
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Assume that the environment variable 'LANG' is set.  We can test unicode, however, for systems
    # which don't have LANG set, we need to set one.
    try:
        environ['LANG']
    except KeyError:
        environ['LANG'] = 'C'

    # unicode
    # To test unicode, we need to have an environment variable that changes its value during the run.
    # It's hard to pick a variable that will change its value consistently but not have side effects.
    # So, instead of having the variable change its value, we're going to force the variable to change
    # its value by reading it before and after changing the variable to make sure that it doesn't
    # cache properties from the variable.
    lang = environ['LANG']
    # _value_cache should be empty since we haven

# Generated at 2022-06-13 16:44:50.199375
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that utf-8 characters are handled correctly
    env = _TextEnviron({'foo': '\xc3\xa6\xc3\xb8\xc3\xa5'})
    assert env['foo'] == u'æøå'

    # Test that surrogate escapes are handled correctly
    env = _TextEnviron({'foo': b'\xc3\x28'})
    assert env['foo'] == u'\udcc3('

    # Test that surrogates are handled correctly
    env = _TextEnviron({'foo': b'\xed\xa0\x80'})
    assert env['foo'] == u'\ud800'

# Unit tests for method __setitem__ of class _TextEnviron

# Generated at 2022-06-13 16:45:00.734117
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    PY3 = sys.version_info[0] == 3
    NONSTRING = 'passthru' if PY3 else 'strict'

    # When there is a string UTF-8 value in the environment
    environ['STRING_UTF8'] = '\u1234'
    assert environ['STRING_UTF8'] == '\u1234'
    # When there is a byte string UTF-8 value in the environment
    environ['BYTES_UTF8'] = to_bytes('\u1234')
    assert environ['BYTES_UTF8'] == '\u1234'

    # When there is a string value with encoding set to non compatible encoding
    environ['STRING1'] = 'x'

# Generated at 2022-06-13 16:45:03.224005
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] is not None
    assert environ['PYTHONIOENCODING'] is not None
    assert environ['HOME'].startswith('/')


# Generated at 2022-06-13 16:45:05.833829
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange&Act
    env = _TextEnviron()

    # Assert
    assert isinstance(env['PATH'], type(''))

# Generated at 2022-06-13 16:45:14.017389
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    The method __getitem__ provides a way to return text string from the environment instead of byte
    strings. Like Python3's os.environ.
    """
    # Create a test environment
    env = {
        'boolean_true': b'true',
        'boolean_false': b'false',
        'list': b'[1, 2, 3]',
    }

    # Check for text strings return
    environ = _TextEnviron(env=env)
    assert environ['boolean_true'] == 'true'
    assert environ['boolean_false'] == 'false'
    assert environ['list'] == '[1, 2, 3]'
    assert environ['list'] == b'[1, 2, 3]'

    # Check for byte strings return

# Generated at 2022-06-13 16:45:23.999294
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def get_environ(env=None, encoding=None):
        return _TextEnviron(env=env, encoding=encoding)

    if PY3:
        assert get_environ()['PATH']
        assert get_environ({b'PATH': b'C:\\\\WINDOWS'})['PATH'] == 'C:\\WINDOWS'
        assert get_environ({'PATH': 'C:\\\\WINDOWS'})['PATH'] == 'C:\\WINDOWS'
        assert get_environ(env={'PATH': 'C:\\\\WINDOWS'}, encoding='ascii')['PATH'] == 'C:\\WINDOWS'

    else:
        assert get_environ()['PATH']
        assert get_environ({b'PATH': b'C:\\\\WINDOWS'})['PATH'] == u'C:\\WINDOWS'

# Generated at 2022-06-13 16:45:33.738911
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    # TEST 1: Text key in environment -> bytes value returned as text
    environ['MY_KEY_1'] = 'MY_VALUE_1'
    assert 'MY_VALUE_1' == environ['MY_KEY_1']

    # TEST 2: Text key in environment -> non-ascii value returned as text
    environ['MY_KEY_2'] = 'MY_VALUE_2\u263a'
    assert 'MY_VALUE_2\u263a' == environ['MY_KEY_2']

    # TEST 3: Text key in environment -> bytes value returned as text with utf-8 error handling
    environ['MY_KEY_3'] = b'MY_VALUE_3\xc2\xa2'
    assert 'MY_VALUE_3\xa2' == environ['MY_KEY_3']

   