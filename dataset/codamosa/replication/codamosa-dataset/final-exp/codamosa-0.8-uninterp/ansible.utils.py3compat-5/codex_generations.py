

# Generated at 2022-06-13 16:35:57.194431
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test TextEnviron.get
    """
    # Bytes string as value
    environ['A'] = 'A'
    assert environ['A'] == 'A'

    # Unicode string as value
    environ['B'] = u'B'
    assert environ['B'] == u'B'

    # Unicode-Escape encoded bytes string
    environ['C'] = "C\xe9"
    assert environ['C'] == u'C\xe9'

    # Unicode-Escape encoded bytes string
    environ['C'] = "C\xe9"
    assert environ['C'] == u'C\xe9'

    # Latin-1 as value
    environ['D'] = 'D\xe9'
    assert environ['D'] == u'D\xe9'

# Generated at 2022-06-13 16:36:02.714787
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env_backup = environ.copy()
    try:
        environ.clear()
        environ[u'foo'] = u'bar'
        environ[u'baz'] = 'yy'
        assert environ[u'foo'] == u'bar'
        assert environ[u'baz'] == u'yy'
    finally:
        environ.clear()
        environ.update(env_backup)


# Generated at 2022-06-13 16:36:06.711196
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({'byte': 'str', 'str': u'uni'}, 'utf-8')
    assert test_environ['byte'] == u'str'
    assert test_environ['str'] == u'uni'


# Generated at 2022-06-13 16:36:18.012788
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import copy
    import unittest

    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    class TestCase(unittest.TestCase):
        def test_getitem(self):
            with mock.patch('ansible.module_utils.os.environ', new={'TEST_VAR': '\u2713'}):
                with self.assertRaises(AttributeError):
                    # Need to copy the dict to avoid overwriting actual envvars
                    environ = _TextEnviron(copy.copy(os.environ))
                    self.assertEqual(environ['TEST_VAR'], '\u2713')
                env = _TextEnviron()
                self.assertEqual(env['TEST_VAR'], '\u2713')

   

# Generated at 2022-06-13 16:36:26.189145
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'foo': b'bar'})
    assert environ[b'foo'] == 'bar'
    assert environ[u'foo'] == 'bar'
    assert environ['foo'] == 'bar'

    environ = _TextEnviron({'foo': 'bar'})
    assert environ[b'foo'] == 'bar'
    assert environ[u'foo'] == 'bar'
    assert environ['foo'] == 'bar'

    environ = _TextEnviron({'foo': b'bar'})
    assert environ[b'foo'] == 'bar'
    assert environ[u'foo'] == 'bar'
    assert environ['foo'] == 'bar'

    environ = _TextEnviron({u'foo': u'bar'})

# Generated at 2022-06-13 16:36:34.953808
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """

    Args:
        parameters:  (<str>): The parameter to search in.
        parameters:  (<str>): The value to search for.
    Returns: True if the value is in the parameters.

    Raises:

    """
    # os.environ is a dict that we can't control.  We don't know the native type of the values in
    # os.environ.  So we can't change the test
    # We don't know the native type of the values in os.environ.  So we can't checks on the raw
    # values returned by os.environ
    # os.environ is a dict that we can't control.  We don't know the native type of the values in
    # os.environ.  So we can't change the test
    # We don't know the native type of the values in os

# Generated at 2022-06-13 16:36:40.403505
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['ANSIBLE_TEST_ENV_VAR'] = 'Test ' + chr(0xF0) + chr(0xA0) + chr(0x90) + chr(0x9F)
    assert environ['ANSIBLE_TEST_ENV_VAR'] == u'Test \U0001F40F'



# Generated at 2022-06-13 16:36:48.398063
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import tempfile

    with tempfile.TemporaryDirectory() as test_dir:
        # Setup environment with values we can control
        os.environ = {}
        environ._raw_environ = {}
        os.environ['TEST_PATH'] = os.path.join(test_dir, 'test')
        os.environ['TEST_PATH2'] = os.path.join(test_dir, u'桃')

        # Test normal value
        test_value = 'unit test value'
        environ['TEST_VALUE'] = test_value
        if PY3:
            assert environ['TEST_VALUE'] == test_value
        else:
            assert environ['TEST_VALUE'] == to_text(test_value)

        # Test non-strings (non-strings get converted to unicode)


# Generated at 2022-06-13 16:36:57.590187
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup test environ, with a custom encoding
    env = _TextEnviron({b'key1': b'value1', b'key2': b'value2'}, encoding='ascii')

    # Check for existing value
    assert env['key1'] == u'value1'
    assert env['key2'] == u'value2'

    # Check for missing value, then add it
    try:
        value = env['key3']
    except KeyError:
        pass
    else:
        assert False, 'KeyError not raised when missing key requested'
    env['key3'] = u'value3'
    assert env['key3'] == u'value3'

    # Check for invalid encoding of value

# Generated at 2022-06-13 16:37:07.291367
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:37:17.684479
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a temporary environment with different encoding than
    # sys.getfilesystemencoding()
    test_env = _TextEnviron(env=dict(), encoding='ascii')
    test_env[u"TEST"] = u"ABCD"
    assert test_env[u"TEST"] == u"ABCD", u"Environment variable not returned as unicode"
    assert test_env["TEST"] == u"ABCD", u"Environment variable not returned as unicode"
    test_env[u"TEST"] = b"ABCD"
    assert test_env[u"TEST"] == u"ABCD", u"Environment variable not correctly encoded"
    assert test_env["TEST"] == u"ABCD", u"Environment variable not correctly encoded"

# Generated at 2022-06-13 16:37:26.219437
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_env = {
        'int': 100,
        'str': u'value',
        'unicode': u'value with accent é',
        'bytes': b'bytes value',
        'byteswithaccent': b'bytes value with accent \xc3\xa9',
        'byteswithinvalid': b'bytes value with invalid \xff',
        'byteswithsurrogate': b'bytes value with surrogate \xed\xa0\x80',
        }

    env = _TextEnviron(raw_env, encoding='ascii')
    assert env['int'] == u'100'
    assert env['str'] == u'value'
    assert env['unicode'] == u'value with accent \xe9'
    assert env['bytes'] == u'bytes value'

# Generated at 2022-06-13 16:37:38.155895
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for correct conversion of environment variable values from bytes to text
    os.environ[to_bytes('strkey', encoding='utf-8')] = '\u8349\u9d5d\u90ab\u8349\u9d5d\u90ab'
    os.environ['bytestrkey'] = b'\xe8\x8d\x89\xe9\xb7\x9d\xe9\x82\xab\xe8\x8d\x89\xe9\xb7\x9d\xe9\x82\xab'
    os.environ['bytestrkey2'] = b'a'

# Generated at 2022-06-13 16:37:44.410815
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # A check that _TextEnviron(dict) works
    environ_dict = _TextEnviron(encoding='utf-8', env={'ANSIBLE_TEST': '0123456789'})
    assert b'0123456789' == environ_dict._raw_environ['ANSIBLE_TEST']
    assert '0123456789' == environ_dict['ANSIBLE_TEST']

    # A check that _TextEnviron(dict) works and that the cache holds the value
    environ_dict['ANSIBLE_TEST'] = '9876543210'
    assert b'9876543210' == environ_dict._raw_environ['ANSIBLE_TEST']
    assert '9876543210' == environ_dict['ANSIBLE_TEST']
    assert '9876543210' == en

# Generated at 2022-06-13 16:37:53.750190
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test getting the normal variables we expect to find
    assert environ['HOME'] == os.path.expanduser('~')
    assert environ['LC_ALL'] == 'C'
    if 'LC_ALL' in os.environ:
        assert environ['LC_ALL'] == os.environ['LC_ALL']

    # Test getting byte strings that are ascii
    environ['FOO'] = 'bar'
    assert environ['FOO'] == 'bar'

    # Test getting byte strings that aren't ascii
    environ['FOO'] = b'\xe9'
    assert environ['FOO'] == b'\xe9'.decode(errors='surrogate_or_strict')

    # Test getting text strings
    environ['FOO'] = u'\xe9'
    assert en

# Generated at 2022-06-13 16:37:56.713568
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['LANG'] = 'tr_TR.utf8'
    assert environ['LANG'] == u'tr_TR.utf8'

# Generated at 2022-06-13 16:38:05.936462
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_copy = environ.copy()
    environ_copy['TEST_STR'] = 'str'
    environ_copy['TEST_BYTES'] = b'bytes'
    assert environ_copy['TEST_STR'] == 'str'
    assert environ_copy['TEST_BYTES'] == 'bytes'
    del environ_copy
    try:
        os.environ['TEST_STR'] = 'str'
        os.environ['TEST_BYTES'] = b'bytes'
        assert environ['TEST_STR'] == 'str'
        assert environ['TEST_BYTES'] == 'bytes'
    finally:
        del os.environ['TEST_STR']
        del os.environ['TEST_BYTES']

# Generated at 2022-06-13 16:38:12.014549
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_str = 'PATH="test" test'
    environ_bytes = b'PATH="test" test'

    environ = _TextEnviron()
    environ[environ_str] = environ_bytes
    assert environ[environ_bytes] == environ_str
    assert environ[environ_str] == environ_str



# Generated at 2022-06-13 16:38:16.912796
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'TEST_VAR': '\u2683'}, encoding='utf-8')
    assert environ['TEST_VAR'] == '\u2683'
    # Test that the cache is used
    environ._raw_environ['TEST_VAR'] = '\u2683'.encode('utf-8')
    assert environ['TEST_VAR'] == '\u2683'


# Generated at 2022-06-13 16:38:22.221660
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environment = _TextEnviron({b'foo': b'bar'})
    assert environment['foo'] == u'bar'
    if PY3:
        assert type(environment['foo']) == str
    else:
        assert type(environment['foo']) == unicode

# Generated at 2022-06-13 16:38:35.129286
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:38:39.247880
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LANG'] == 'C.UTF-8'
    assert environ['TEST_ENCODING'] == u'Testing \u00c9ncoding'

# Generated at 2022-06-13 16:38:48.193939
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:38:51.063545
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    env = _TextEnviron()

    # Act
    env['PATH'] = 'foo/bar'

    # Assert
    assert env['PATH'] == 'foo/bar'

# Generated at 2022-06-13 16:39:00.980161
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test in ASCII
    environ_old = os.environ
    os.environ = {'TEST_THAT': 'abc'}
    environ_test = _TextEnviron()
    assert environ_test['TEST_THAT'] == u'abc'
    os.environ = environ_old

    # Test in UTF-8
    environ_old = os.environ
    os.environ = {'TEST_THAT': '\xd0\xb0'}
    environ_test = _TextEnviron()
    assert environ_test['TEST_THAT'] == u'\u0430'
    os.environ = environ_old

# Generated at 2022-06-13 16:39:07.047014
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    b_value = to_bytes(u'hi\u20ac', encoding=environ.encoding, nonstring='strict',
                       errors='surrogate_or_strict')
    b_key = to_bytes(u'key', encoding=environ.encoding, nonstring='strict',
                     errors='surrogate_or_strict')
    environ._raw_environ = {b_key: b_value}
    assert environ[u'key'] == u'hi\u20ac'


# Generated at 2022-06-13 16:39:16.546528
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that we get the correct values if the raw_environ cache is empty
    environ._raw_environ = {}
    environ._value_cache = {}
    assert environ['ONE'] == 'ONE'
    assert environ._raw_environ == {'ONE': b'ONE'}

    # Test that we get the correct values if the raw_environ cache has the value
    environ._raw_environ = {}
    environ._value_cache = {}
    environ._raw_environ['ONE'] = b'ONE'
    environ._value_cache[b'ONE'] = 'ONE'
    assert environ['ONE'] == 'ONE'
    assert environ._raw_environ == {'ONE': b'ONE'}

    # Test that we get the correct values if the raw_environ cache has a different value

# Generated at 2022-06-13 16:39:23.243682
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that the method behaves like os.environ on Python3
    environ['TESTVAR'] = 'test value'
    assert environ['TESTVAR'] == 'test value'
    if PY3:
        assert environ['TESTVAR'] is os.environ.__getitem__('TESTVAR')
    # Check that it handles different encodings properly
    environ['TESTVAR'] = 'test \u2122 value'
    assert environ['TESTVAR'] == u'test \u2122 value'
    # Check that it handles encodings that can not be decoded to unicode properly
    environ['TESTVAR'] = 'test \xe4 value'
    assert environ['TESTVAR'] == u'test \uFFFD value'


# Generated at 2022-06-13 16:39:33.165586
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:42.756165
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    class Test__TextEnviron___getitem__(unittest.TestCase):
        """
        Unit test for method __getitem__ of class _TextEnviron
        """
        #region Setup
        @classmethod
        def setUpClass(cls):
            cls.environ = _TextEnviron(encoding='utf-8')
            cls.variable_name = 'PYTHONUNBUFFERED'
            cls.variable_value = '1'
            cls.expected_value = cls.variable_value

        #endregion

        #region Testcases
        def test___getitem__(self):
            """Test __getitem__"""
            self.assertEquals(self.expected_value, self.environ[self.variable_name])

       

# Generated at 2022-06-13 16:39:54.404344
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class TestEnviron:
        def __getitem__(self, key):
            if key == "UNICODE_KEY":
                return b'\xc3\xb1'
            elif key == "ASCII_KEY":
                return b'test'
            else:
                return None
    env = _TextEnviron(TestEnviron(), 'utf-8')
    assert env['UNICODE_KEY'] == '\u00f1'
    assert env['ASCII_KEY'] == 'test'
    assert env['NOT_A_KEY'] is None


# Generated at 2022-06-13 16:40:03.143047
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test 1: key doesn't exist in environment
    try:
        environ['ansible_test_key']
        assert False, "text_environ['ansible_test_key'] should throw an exception"
    except KeyError:
        pass

    # Test 2: key exists but is not unicode compatible

# Generated at 2022-06-13 16:40:05.573905
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._value_cache = {}
    assert isinstance(environ['HOME'], str)
    assert isinstance(environ['PWD'], str)

# Generated at 2022-06-13 16:40:06.841542
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ["USERNAME"] == os.environ['USERNAME']

# Generated at 2022-06-13 16:40:07.753668
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    pass


# Generated at 2022-06-13 16:40:13.876634
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'bar': b'baz'})
    assert env['bar'] == 'baz'
    assert isinstance(env['bar'], str)
    assert env[b'bar'] == 'baz'
    assert isinstance(env[b'bar'], str)



# Generated at 2022-06-13 16:40:24.605363
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'key1': b'value1', b'key2': b'value2'})
    assert env[b'key1'] == u'value1'
    assert env[u'key1'] == u'value1'
    assert env[b'key2'] == u'value2'
    assert env[u'key2'] == u'value2'

    env = _TextEnviron({b'key1': u'value1', b'key2': u'value2'})
    assert env[b'key1'] == u'value1'
    assert env[u'key1'] == u'value1'
    assert env[b'key2'] == u'value2'
    assert env[u'key2'] == u'value2'



# Generated at 2022-06-13 16:40:31.054521
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.system('export TEST_UNICODE1=$(echo -ne "\xe2\x9d\x93")')
    os.system('export TEST_UNICODE2=$(echo -ne "\xe2\x9d\x93")')

    assert environ['TEST_UNICODE1'] == u'\u2713'
    assert environ['TEST_UNICODE2'] == u'\u2713'

# Generated at 2022-06-13 16:40:41.281063
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that a simple ascii string comes back as ascii
    assert environ.__getitem__('PATH') == ''

    # Test that it handles standard unicode stuff
    os.environ[u'SCHÖN'] = 'SCHÖN'
    assert environ.__getitem__(u'SCHÖN') == u'SCHÖN'

    # Test that it has a surrogate_or_strict error handler (in both PY3 and PY2)
    os.environ['SCHÖN'] = 'SCH\xf6N'.encode('latin-1')
    try:
        environ.__getitem__('SCHÖN')
    except UnicodeDecodeError:
        pass

# Generated at 2022-06-13 16:40:43.913182
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    key = 'PWD'
    value = environ[key]
    assert isinstance(value, str)

# Generated at 2022-06-13 16:40:51.597414
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.clear()
    environ['ANSIBLE_TEST_KEY'] = 'ANSIBLE_TEST_VALUE'

    # Test __getitem__: get value from environ
    assert environ['ANSIBLE_TEST_KEY'] == 'ANSIBLE_TEST_VALUE'

    # Test __getitem__: get value from cache
    assert environ['ANSIBLE_TEST_KEY'] == 'ANSIBLE_TEST_VALUE'



# Generated at 2022-06-13 16:41:00.806803
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes, to_text

    class Environ(dict):
        # For testing, make it so the bytes value of the key are the same as the key
        def __getitem__(self, key):
            return to_bytes(key)

    env_dict = Environ()
    env_dict[b'ascii'] = b'ascii'
    env_dict[b'utf8'] = b'\xe2\x9c\x93'
    env_dict[b'non_utf8'] = b'\xff'
    text_env = _TextEnviron(env=env_dict, encoding='latin-1')
    out = StringIO()
    # Test that non-utf8 characters are passed through un

# Generated at 2022-06-13 16:41:12.469951
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert to_text('test') == b'test'
    assert to_bytes('test') == u'test'
    assert to_text(u'test') == u'test'

    assert to_text('test', encoding=None) == u'test'
    assert to_text('test', encoding='utf-8') == u'test'

    assert to_text(b'test', encoding=None) == u'test'
    assert to_text(b'test', encoding='utf-8') == u'test'

    assert to_text(u'test', encoding=None) == u'test'
    assert to_text(u'test', encoding='utf-8') == u'test'

    assert to_text('test', errors='strict') == u'test'
    assert to_text('test', errors='replace') == u

# Generated at 2022-06-13 16:41:23.375078
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _DummyEnviron(object):
        _value = None
        def __getitem__(self, key):
            return self._value

        def __setitem__(self, key, value):
            self._value = value

    environ._raw_environ = _DummyEnviron()

    # Test that we cache the strings
    environ._raw_environ._value = 'asdf'
    cached_text = environ['foo']
    assert cached_text == 'asdf'
    assert environ._value_cache[environ._raw_environ._value] == cached_text
    assert environ['foo'] is cached_text

    # Test that we can handle unicode
    environ._raw_environ._value = u'\u1234'
    cached_text = environ['foo']
    assert cached_

# Generated at 2022-06-13 16:41:31.972008
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an empty dictionary
    env = {}
    # Create an instance of _TextEnviron with empty dictionary as argument
    text_environ = _TextEnviron(env)
    assert(0 == len(text_environ))
    # Add a new item in the empty dictionary
    env['abc'] = 'abc'
    # Check for the availability of the newly added item in environment object
    assert('abc' in text_environ)
    # Check for the value of the newly added item in environment object
    assert('abc' == text_environ['abc'])
    # Add a new item in the empty dictionary
    env['xyz'] = 'XYZ'
    # Check for the availability of the newly added item in environment object
    assert('xyz' in text_environ)
    # Check for the value of the newly added item in environment object


# Generated at 2022-06-13 16:41:40.516098
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    # Test a normal key
    envt = _TextEnviron({b'foo': b'bar'}, encoding='utf-8')
    assert isinstance(envt['foo'], str)

    # Test a weird unicodey key
    envt = _TextEnviron({b'foo\xe7': b'bar'}, encoding='utf-8')
    assert isinstance(envt['fooç'], str)

    # Test a weird unicodey value
    envt = _TextEnviron({b'foo': b'bar\xe7'}, encoding='utf-8')
    assert isinstance(envt['foo'], str)

    # Test a non-unicodey key

# Generated at 2022-06-13 16:41:46.278435
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that it raises key error if the key doesn't exist
    e = _TextEnviron()

    try:
        e['key does not exist']
    except KeyError:
        pass
    else:
        raise AssertionError('_TextEnviron should raise a KeyError exception when the key does not exist')

    # Test that it gets the value of an existing key
    if PY3:
        expected_value = 'utf-8'
    else:
        expected_value = u'utf-8'
    e = _TextEnviron({'lang': 'en_US.utf-8'})

    assert e['lang'] == e['lang'] == expected_value

# Generated at 2022-06-13 16:41:57.239781
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST_VAR_1'] = 'TEST VALUE 1'
    os.environ['TEST_VAR_2'] = 'TEST VALUE 2'
    assert isinstance(environ['TEST_VAR_1'], str)
    assert environ['TEST_VAR_1'] == 'TEST VALUE 1'
    assert isinstance(environ['TEST_VAR_2'], str)
    assert environ['TEST_VAR_2'] == 'TEST VALUE 2'
    os.environ['TEST_VAR_2'] = 'ÄËÏÖÜ'
    assert isinstance(environ['TEST_VAR_2'], str)

# Generated at 2022-06-13 16:42:07.954957
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test the _TextEnviron class with the default encoding
    environ = _TextEnviron()

    old_value = os.environ['USER']
    try:
        os.environ['USER'] = b'root'
        assert isinstance(environ['USER'], unicode)
        assert environ['USER'] == u'root'
    finally:
        os.environ['USER'] = old_value

    # Test the _TextEnviron class with utf-8 encoding
    environ = _TextEnviron(encoding='utf-8')

    old_value = os.environ['USER']

# Generated at 2022-06-13 16:42:18.260775
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:42:23.574556
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Ensure that if PY3 then the result is the same as os.environ
    assert environ['PATH'] == os.environ['PATH']



# Generated at 2022-06-13 16:42:33.472078
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that _TextEnviron.__getitem__ properly converts a b'str' to a str in
    Python2.
    """
    import json
    import tempfile
    import os
    import os.path
    import subprocess

    #
    # Create a python script which will print a variable
    # Note that this must be done in the temporary directory because we're
    # going to chdir to it
    #
    temp_dir = tempfile.mkdtemp()
    python_script_path = os.path.join(temp_dir, 'test.py')
    with open(python_script_path, 'w') as python_script:
        python_script.write("import os\n")
        python_script.write("import sys\n")

# Generated at 2022-06-13 16:42:37.987864
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    original_native_env = os.environ
    try:
        environ['foo'] = 'bar'
        assert environ['foo'] == to_text('bar')
        environ['bar'] = b'baz'
        assert environ['bar'] == to_text(b'baz')
        os.environ = {b'foo': 'bar'}
        assert environ['foo'] == to_text('bar')
    finally:
        os.environ = original_native_env



# Generated at 2022-06-13 16:42:43.657990
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(encoding='utf-8')
    test_environ['PATH'] = b'\x44\x00\x44\x00'
    assert test_environ['PATH'] == '\u0044\u0044'
    test_environ = _TextEnviron(encoding='cp1252')
    test_environ['KEY'] = b'\x26\x27'
    assert test_environ['KEY'] == '&&'

# Generated at 2022-06-13 16:42:52.944145
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    from ansible.module_utils._text import to_bytes, to_native

    environ._raw_environ = {'key': to_bytes('value', encoding='utf-8', nonstring='strict',
                                            errors='surrogate_or_strict')}

    if PY3:
        # When running on Python3, the environment should not be decoded.  Just return
        # the value
        assert environ['key'] == 'value'
    else:
        # When running on Python2, the value should be decoded
        assert environ['key'] == to_text('value')

    # Make sure we're using the same encoding that Python3 does
    assert environ.encoding == sys.getfilesystemencoding()

    # Test that surrogate_or_strict errors get passed through

# Generated at 2022-06-13 16:43:03.464235
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # This unit test will only run on Python 2
    if PY3:
        return

    # Make sure we aren't using the actual os.environ since we'll be changing it
    test_env = {'KEY1': 'value1'}
    environ = _TextEnviron(env=test_env)

    # Make sure we return a text object
    assert isinstance(environ['KEY1'], text_type)

    # Make sure that we don't double-encode
    test_env['KEY2'] = u'français'
    assert environ['KEY2'] == u'français'

    # Make sure that we don't double-encode utf-8 encoded bytes
    test_env['KEY3'] = b'fran%c3%a7ais'

# Generated at 2022-06-13 16:43:12.087749
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import StringIO

    # On Python2, the os.environ values are byte strings.  Let's make sure we can get the text of
    # a byte string out of our environment.
    class Py2Environ(object):
        def __init__(self):
            self.valuemap = {b'expected': b'\xC3\xA1'}

        def __getitem__(self, key):
            return self.valuemap[key]

    environ_obj = _TextEnviron(Py2Environ(), encoding='utf-8')

    # Make sure we get the right text value
    assert environ_obj['expected'] == 'á'

    # Make sure we don't get Python3's builtin text conversion
    old_stdout = sys.stdout
    sys

# Generated at 2022-06-13 16:43:21.966386
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Initial value
    assert environ['PATH'] == u'/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl'
    # Existing value
    assert environ['PATH'] == u'/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl'
    # New value
    environ['ANSIBLE'] = u'true'
    assert environ['ANSIBLE'] == u'true'
    # New value cached
    assert environ['ANSIBLE'] == u'true'
    # New value changed
    environ['ANSIBLE'] = u'false'

# Generated at 2022-06-13 16:43:31.128677
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        # Let's imagine that the user has set this variable in the environment
        os.environ['UNICODE_VARIABLE'] = b'\xe5'
        # And has this variable set to a regular ascii variable
        os.environ['ASCII_VARIABLE'] = b'foobar'
        # We should get a unicode text string instead of a byte string
        assert environ['ASCII_VARIABLE'] == 'foobar'
        assert environ['UNICODE_VARIABLE'] == u'\u0105'
    finally:
        del os.environ['UNICODE_VARIABLE']
        del os.environ['ASCII_VARIABLE']


# Generated at 2022-06-13 16:43:37.177579
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # set up _TextEnviron object
    e_o = _TextEnviron()
    assert isinstance(e_o, _TextEnviron)

    # set up environment
    os.environ['TEST_0'] = b'TEST_0'

    # get value of item, check if it is a text string
    assert isinstance(e_o['TEST_0'], str)

    # cleanup
    del os.environ['TEST_0']



# Generated at 2022-06-13 16:43:54.189714
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a temporary class that inherits from _TextEnviron but overrides __getitem__
    class _TextEnviron_verifier(_TextEnviron):
        def __init__(self, validate_data):
            self.validate_data = validate_data
            self.validate_data_index = 0
            super(_TextEnviron_verifier, self).__init__()

        def __getitem__(self, key):
            validate_data = self.validate_data[self.validate_data_index]

            # The key passed to __getitem__ should be the first item in the validate_data list
            if key != validate_data[0]:
                raise ValueError("Expected key '{}' got '{}'".format(validate_data[0], key))

            # Return the expected value from the second item in

# Generated at 2022-06-13 16:43:56.240832
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    subunit_testenv = _TextEnviron({'ANSIBLE_PAYLOAD': 'TEST'}, encoding='utf-8')
    assert subunit_testenv['ANSIBLE_PAYLOAD'] == 'TEST'


# Generated at 2022-06-13 16:43:59.226328
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Reset the cache and the raw environ
    environ._value_cache = {}
    environ._raw_environ = {'foo': 'bar'}
    assert environ['foo'] == 'bar'
    assert environ._value_cache == {'bar': 'bar'}


# Generated at 2022-06-13 16:44:06.730706
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_NET_PASSWORD'] = '$ANSIBLE_NET_USERNAME'
    os.environ['ANSIBLE_NET_USERNAME'] = '$ANSIBLE_NET_PASSWORD'
    assert(environ['ANSIBLE_NET_PASSWORD'] == '$ANSIBLE_NET_USERNAME')
    assert(environ['ANSIBLE_NET_USERNAME'] == '$ANSIBLE_NET_PASSWORD')


# Generated at 2022-06-13 16:44:16.624062
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def make_from_bytes(b):
        return b.decode(encoding='utf-8')

    def contains_non_ascii_bytes(b):
        for c in b:
            if ord(c) >= 128:
                return True
        return False

    def contains_non_ascii_text(s):
        for c in s:
            if ord(c) >= 128:
                return True
        return False

    class _Environ:
        def __init__(self, seed=None, encoding=None):
            self.encoding = encoding
            if seed is None:
                seed = {}
            self.seed = seed
            self._environ = dict(seed)
            self._key_cache = {}


# Generated at 2022-06-13 16:44:21.989861
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an instance of _TextEnviron
    my_environ = _TextEnviron({b'key1': b'value1', b'key2': u'value2'})
    # Test __getitem__
    assert my_environ[b'key1'] == u'value1'
    assert my_environ[b'key2'] == u'value2'


# Generated at 2022-06-13 16:44:33.360455
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:44:41.514103
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes, to_text
    env_var = u'€ÿöÿåöÿèïÿéöÿ'
    if PY2:
        encoded_env_var = b'\xe2\x82\xac\xc3\xbf\xc3\xb6\xc3\xbf\xc3\xa5\xc3\xb6\xc3\xbf\xc3\xa8\xc3\xaf\xc3\xbf\xc3\xa9\xc3\xb6\xc3\xbf'
    else:
        encoded_env_var = env_var

    te = _TextEnviron({env_var: encoded_env_var})
    assert to_text

# Generated at 2022-06-13 16:44:51.664530
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:44:59.206028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_ENV'] = to_text('ASCII value')
    assert environ['TEST_ENV'] == 'ASCII value'

    environ['TEST_ENV'] = to_text('non-ASCII value', encoding='utf-8')
    assert environ['TEST_ENV'] == 'non-ASCII value'

    if PY3:
        environ['TEST_ENV'] = 'non-ASCII value'
        assert environ['TEST_ENV'] == 'non-ASCII value'

# Generated at 2022-06-13 16:45:23.229987
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:45:30.471055
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set national characters and check in public method
    test_native_env = {'PYTHONPATH': b'/home/\xd0\x92\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xba',
                       'LANG': 'ru_RU.UTF-8',
                       'LANGUAGE': 'ru:en'}
    environ._raw_environ = test_native_env.copy()

    assert environ['LANG'] == 'ru_RU.UTF-8'
    if PY3:
        assert environ['PYTHONPATH'] == '/home/\u0412\u0435\u0440\u043e\u043d\u0438\u043a'

# Generated at 2022-06-13 16:45:34.922637
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test on Python2
    if sys.version_info[0] == 2:
        assert isinstance(environ['toto'], unicode)
    # Test on Python3
    else:
        assert isinstance(environ['toto'], str)


if __name__ == "__main__":
    import pytest
    pytest.main(args=['-xrf', __file__, '-v'])

# Generated at 2022-06-13 16:45:38.900986
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron(encoding='utf-8')
    text_environ["ANSIBLE_PYTHON_INTERPRETER"] = "/usr/bin/python3"
    assert text_environ["ANSIBLE_PYTHON_INTERPRETER"] == u"/usr/bin/python3"
    assert not PY3

# Generated at 2022-06-13 16:45:43.395572
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({b'PATH': b'blah', b'TEST': u'\u263A'.encode('utf-8')})
    assert e[b'PATH'] == 'blah'
    assert isinstance(e[b'PATH'], type(u'blah'))
    assert e[b'TEST'] == u'\u263A'
    assert isinstance(e[b'TEST'], type(u'\u263A'))


# Generated at 2022-06-13 16:45:47.072929
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({'TEXT_ENVIRON': 'text'}, encoding='utf-8')
    assert environ['TEXT_ENVIRON'] == 'text'
