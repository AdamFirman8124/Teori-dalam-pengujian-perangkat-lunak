

# Generated at 2022-06-13 16:36:03.600415
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # These tests fail if you're not using utf-8
    import locale
    if locale.getpreferredencoding() != 'UTF-8':
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    env = _TextEnviron({b'simple': b'a string'})
    assert env['simple'] == u'a string'
    env = _TextEnviron({b'with_unicode': u'Iñtërnâtiônàlizætiøn'.encode('utf-8')})
    assert env['with_unicode'] == u'Iñtërnâtiônàlizætiøn'
    env = _TextEnviron({b'invalid_utf8': b'\xFF\xFE\x00\x00'})


# Generated at 2022-06-13 16:36:06.041673
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['teststring'] = 'some value'
    assert type(environ['teststring']) is str
    assert environ['teststring'] == os.environ['teststring']

# Generated at 2022-06-13 16:36:10.500206
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Prepare the environment for the test
    old_TestEnviron = os.environ.copy()
    new_TestEnviron = {}
    os.environ = new_TestEnviron
    
    # Generate the string
    unicode_string = u'Test \u1234 string'
    # Convert the string to the encoding of the current system
    unicode_string_bytes = unicode_string.encode(sys.getfilesystemencoding())
    # Create the _TextEnviron object
    test_environ = _TextEnviron(env=os.environ, encoding=sys.getfilesystemencoding())
    # Put the string in the environ
    os.environ['ANSIBLE_TEST_ENVIRON'] = unicode_string_bytes
    # Check that the correct string is returned (without changing the value)
   

# Generated at 2022-06-13 16:36:21.510184
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest
    import mock

    class _TextEnvironTestCase(unittest.TestCase):
        def setUp(self):
            self.env = mock.MagicMock()
            self.environ = _TextEnviron(self.env)

    class ValueIsBytesTestCase(_TextEnvironTestCase):
        '''
        Test when a value is returned as bytes in Python2
        '''
        def test_value_cached(self):
            self.environ._value_cache['foo'] = 'foo'
            self.env.__getitem__ = mock.MagicMock(return_value='foo')
            self.assertEqual(self.environ.__getitem__('foo'), 'foo')
            self.env.__getitem__.assert_not_called()


# Generated at 2022-06-13 16:36:25.095948
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ["ANSIBLE_CORE_MODULE_UTILS"] == environ._raw_environ["ANSIBLE_CORE_MODULE_UTILS"]



# Generated at 2022-06-13 16:36:34.218988
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up
    import os
    import os as os2
    os2.environ = {'ANSIBLE_MODULE_ARGS': '{"test_key1": "test_value1"}'}
    fp = open('test_file', 'w')
    fp.write('test_value2')
    fp.close()
    test_dict = {'test_key3': 'test_value3'}

    # Run & check
    assert environ['ANSIBLE_MODULE_ARGS'] == '{"test_key1": "test_value1"}'
    assert environ['test_key4'] == os.environ['test_key4']
    assert environ['test_key5'] == os2.environ['test_key5']

# Generated at 2022-06-13 16:36:42.975791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # This is only applicable to Python 2
    if PY3:
        return

    # Test case 1: key is valid.
    # Test case 1.1: key is in environ.
    # Test case 1.1.1: value is a text string.
    os.environ['ANSIBLE_TEST_KEY_1'] = u'こんにちは'
    assert environ['ANSIBLE_TEST_KEY_1'] == u'こんにちは'
    del os.environ['ANSIBLE_TEST_KEY_1']

    # Test case 1.1.2: value is a byte string.
    os.environ['ANSIBLE_TEST_KEY_1'] = u'こんにちは'.encode('utf-8')

# Generated at 2022-06-13 16:36:54.056758
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_STRING'] = "This is a test"
    os.environ[b'ANSIBLE_BYTES'] = b"\xff\xf8\x00"
    os.environ['ANSIBLE_LATIN1'] = u'\u00c3\u00a8'
    os.environ[u'ANSIBLE_UNICODE'] = u'\u00c3\u00a9'

    # The string should just be returned as is
    assert environ[u'ANSIBLE_TEST_STRING'] == "This is a test"
    assert environ['ANSIBLE_TEST_STRING'] == "This is a test"
    assert environ[b'ANSIBLE_TEST_STRING'] == "This is a test"

# Generated at 2022-06-13 16:36:55.585963
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert isinstance(environ['HOME'], str)



# Generated at 2022-06-13 16:37:06.061413
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # os.environ.__dict__ is the dictionary that underlies os.environ.  It's not public
    # but we need to access it to test this method.  (Python3 makes this easier to do).
    import os
    os.environ = _TextEnviron(env=os.environ.__dict__)
    os.environ['test_string'] = b'abc'
    assert os.environ['test_string'] == u'abc'
    os.environ['test_string'] = b'\xe2\x98\x83'
    assert os.environ['test_string'] == u'\u2603'
    # We can also test that we cache based off of the raw value
    os.environ['test_string'] = b'\xe2\x98\x83'

# Generated at 2022-06-13 16:37:11.689801
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(env={b'b': b'b'}, encoding='latin1')
    assert b'b' in env
    assert env[b'b'] == 'b'

# Generated at 2022-06-13 16:37:24.473104
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def mock_env():
        return {b'TESTNAME': b'test\xc3\xbc',
                b'TESTNAME_TWO': b'test\xc3\xbc_two',
                'TESTNAME_THREE': 'test\xc3\xbc_three',
                'TESTNAME_FOUR': 'test\xc3\xbc_four'}


# Generated at 2022-06-13 16:37:28.046971
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._value_cache = {}
    environ._raw_environ = {'foo': 'foo value'}
    results = environ['foo']
    assert results == 'foo value'


# Generated at 2022-06-13 16:37:39.149064
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Encoding is 'utf-8' by default.
    text_environ = _TextEnviron()

    # Test _TextEnviron.__getitem__
    test_key = 'ANSIBLE_STRING_OR_BINARY'
    test_value = u'テスト ﾊﾟｽﾜｰﾄﾞ'
    environ[test_key] = test_value
    assert text_environ[test_key] == test_value

    # Test surrograte characters
    test_key = 'ANSIBLE_SURROGATES'

# Generated at 2022-06-13 16:37:44.940028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Use CP1251
    environ = _TextEnviron({b'ANS_KEY': b'\xd0\x9c\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbb\xd1\x8e\xd1\x87'},
                           encoding='cp1251')
    assert environ['ANS_KEY'] == 'Мой ключ'
    environ = _TextEnviron({'ANS_KEY': b'\xd0\x9c\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbb\xd1\x8e\xd1\x87'},
                           encoding='cp1251')
    assert environ['ANS_KEY'] == 'Мой ключ'

# Generated at 2022-06-13 16:37:53.985259
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_environ = {u'Á_лôñ': u'Đátä', 'B_foo': b'\x80\xd0\x80', 'C_foo': 'föö'}
    text_environ = _TextEnviron(raw_environ)

    assert u'Đátä' == text_environ[u'Á_лôñ']  # Unicode key, unicode value

    assert u'\x80\x80' == text_environ['B_foo']  # Byte string key, byte string value
    # Unicode key, byte string value isn't tested since we don't expect that to happen in practice

    assert u'föö' == text_environ['C_foo']       # Byte string key, unicode value

    assert u'\x80\x80' == text_

# Generated at 2022-06-13 16:37:58.536224
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    ''' Unit test for method __getitem__ of class _TextEnviron'''

    # Create a test enviroment
    tmp_environ = _TextEnviron()
    tmp_environ['HOME'] = '/Users/testuser'

    # Test that getitem works
    assert '/Users/testuser' == tmp_environ['HOME']

# Generated at 2022-06-13 16:37:59.092803
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
        pass

# Generated at 2022-06-13 16:38:07.153584
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # initialize variables needed for the following tests
    original_environ = environ._raw_environ
    # os.environ is case-sensitive, so we need two keys to test case-insensitivity.
    environ['TEST_KEY'] = 'testing'
    environ['test_key'] = 'testing'
    # TODO: future warning: using a dict comprehension as default value in runtime is deprecated
    # os.environ.copy() is deprecated (used as the default value of environ):
    # use dict.fromkeys(os.environ) instead
    # TODO: future warning: encode_errors defaults to 'strict'

    # the mapping protocol through dict.__getitem__
    assert environ['TEST_KEY'] == 'testing'
    assert environ['test_key'] == 'testing'

    # .get()
   

# Generated at 2022-06-13 16:38:11.729670
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=line-too-long
    assert environ['abc'] == u'abc'
    assert environ['üńîćødé'] == u'üńîćødé'
    assert environ['üńîćødé'.encode('utf-8')] == u'üńîćødé'
    assert environ['üńîćødé'.encode('latin-1')] == u'üńîćødé'

# Generated at 2022-06-13 16:38:28.294614
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test valid environment variable
    key = 'PATH'
    value = environ.__getitem__(key)
    assert isinstance(value, str)

    # Test valid environment variable with surrogate characters
    key = 'ANSIBLE_TEST_SURROGATES'
    value_bytes = 'The quick brown fox \uD800 jumps over the lazy dog'
    os.environ[key] = value_bytes
    value2 = environ.__getitem__(key)
    assert isinstance(value2, str)
    assert environ[key] == value2

    # Test invalid environment variable
    key = 'ANSIBLE_TEST_INVALID'
    value_bytes = 'The quick brown fox \xd8 jumps over the lazy dog'
    os.environ[key] = value_bytes

# Generated at 2022-06-13 16:38:34.174227
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = os.environ.copy()
    te = _TextEnviron(env=test_environ)
    assert te['PATH'] == to_text(test_environ['PATH'], encoding='utf-8', nonstring='passthru', errors='surrogate_or_strict')
    test_environ['TEST'] = 'föö'
    assert te['TEST'] == to_text(test_environ['TEST'], encoding='utf-8', nonstring='passthru', errors='surrogate_or_strict')


# Generated at 2022-06-13 16:38:45.080553
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """ Verify that _TextEnviron.__getitem__ returns text instead of bytes
    """
    # Python 2
    if not PY3:
        # In Python 2, os.environ returns byte strings
        assert isinstance(os.environ['HOME'], str)

        # In Python 2, passing a non-existant key should raise a KeyError
        import sys
        if sys.version_info[1] > 6:
            # In Python 2.7 and later, the keyerror from os.environ is a UnicodeKeyError
            try:
                os.environ['not-a-real-key']
            except KeyError:
                e_type = sys.exc_info()[0]
                assert e_type == UnicodeKeyError

                # These tests require asking for a key that does not exist.  Since we'll be looking
                #

# Generated at 2022-06-13 16:38:51.014247
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'key_bytes': b'value_bytes'})
    assert u'value_bytes' == env[b'key_bytes']
    env = _TextEnviron({'key_unicode': 'value_unicode'})
    assert u'value_unicode' == env[b'key_unicode']

# Generated at 2022-06-13 16:39:00.979224
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # If the original environment variable is a text variable, it should return as a text variable
    assert isinstance(environ['PATH'], str)

    # If the original environment variable is not a text variable, we should attempt to decode it
    os.environ['BADGER'] = os.urandom(10)
    assert isinstance(environ['BADGER'], str)
    del os.environ['BADGER']

    # If the environment variable has no encoding, we should return the original
    os.environ['BADGER'] = None
    assert isinstance(environ['BADGER'], type(None))
    del os.environ['BADGER']


# Generated at 2022-06-13 16:39:05.114966
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test __getitem__ when self._raw_environ[key] may not be in self._value_cache yet
    '''

# Generated at 2022-06-13 16:39:08.976319
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import re
    import unittest
    import tempfile
    import pytest

    if not PY3:
        from io import open
        from ansible.module_utils.t_helpers import just_some_binary_data

        class Test_TextEnviron___getitem__(unittest.TestCase):
            encoding = 'utf-8'
            octets = b'Ah\xe4l\xf0!'
            text = u'Ahälð!'

            def test_valid_utf8(self):
                environ = self.create_environ()
                self.assertEqual(environ[self.name], self.text)

            def test_surrogate_errors(self):
                environ = self.create_environ(errors='surrogateescape')

# Generated at 2022-06-13 16:39:15.229841
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with surrogate_or_strict errors
    # Success case - surrogate_or_strict
    original_environ = os.environ.copy()
    try:
        environ.clear()
        environ['ANSIBLE_TEST_KEY'] = b'\xf1\x90\x80\x80'
        assert environ['ANSIBLE_TEST_KEY'] == u'\U00010000'

    finally:
        environ.clear()
        environ.update(original_environ)


# Generated at 2022-06-13 16:39:22.787441
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def get_key(env, key):
        try:
            return env[key]
        except KeyError:
            return 'not found'

    ascii_test_env = _TextEnviron({b'ascii_bytes': b'ascii', 'unicode_str': '\u00E4'}, encoding='ascii')
    assert get_key(ascii_test_env, 'ascii_bytes') == u'ascii'
    assert get_key(ascii_test_env, 'unicode_str') == u'ä'
    assert get_key(ascii_test_env, 'not-found') == 'not found'
    if not PY3:
        assert isinstance(get_key(ascii_test_env, 'ascii_bytes'), unicode)

# Generated at 2022-06-13 16:39:32.830440
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an object for testing
    s = _TextEnviron(encoding='utf-8')
    # Create a dict for testing
    a = {
        'value1': b'bytes_value1',
        'value2': 'text_value2',
        'value3': 1,
    }
    # Set the dict as the source dict of our object
    s._raw_environ = a

    #
    # Test that if the value is bytes, it's decoded
    #

    # Update the cache
    s['value1']

    assert s['value1'] == 'bytes_value1'

    #
    # Test that if the value is text, is returned as it is
    #

    s['value2']

    assert s['value2'] == 'text_value2'

    #
    # Test that if the value

# Generated at 2022-06-13 16:39:49.908422
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_text

    environ = _TextEnviron()
    original_env = os.environ.copy()
    os.environ['TEST_VARIABLE'] = 'abc'
    assert(environ['TEST_VARIABLE'] == to_text('abc'))
    del os.environ['TEST_VARIABLE']
    os.environ.update(original_env)


# Generated at 2022-06-13 16:39:59.211711
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create some environment variables.  These are all in ASCII so that the
    # encoding does not come into play.  Also, the unit test for six's
    # StringIO.StringIO will check the non-ASCII case
    os.environ['TEST_ENV__1'] = 'moo'
    os.environ['TEST_ENV__2'] = 'bar'
    os.environ['TEST_ENV__3'] = 'baz'
    # Check that it behaves like os.environ both on Python2 and Python3
    assert os.environ['TEST_ENV__1'] == 'moo'
    assert environ['TEST_ENV__1'] == 'moo'
    assert os.environ['TEST_ENV__2'] == 'bar'

# Generated at 2022-06-13 16:40:00.450849
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    newenv = _TextEnviron()
    assert newenv['PYTHONPATH'] is None

# Generated at 2022-06-13 16:40:07.483285
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'foo': b'1234', b'bar': b'5678'}, encoding='ascii')
    assert env[u'foo'] == u'1234'
    assert env[u'bar'] == u'5678'
    assert env[b'foo'] == u'1234'
    assert env[b'bar'] == u'5678'

    env = _TextEnviron({b'foo': u'¥'.encode('cp932'), b'bar': b'5678'}, encoding='cp932')
    assert env[u'foo'] == u'¥'
    assert env[u'bar'] == u'5678'
    assert env[b'foo'] == u'¥'
    assert env[b'bar'] == u'5678'


# Unit test

# Generated at 2022-06-13 16:40:19.306251
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class FakeEnvironDict(dict):
        def __getitem__(self, key):
            # This function is *only* for testing __getitem__.  All other functions are just
            # pass-throughs to _raw_environ.
            if key == 'NO_SUCH_KEY':
                raise KeyError('NO_SUCH_KEY')
            if 'utf16_' in key:
                # os.environ is ascii by default, these should be utf-16 encoded
                retval = to_bytes(dict.__getitem__(self, key), encoding='utf-16')
            else:
                retval = dict.__getitem__(self, key).encode('ascii')
            return retval


# Generated at 2022-06-13 16:40:29.199396
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class TestEnviron(MutableMapping):
        def __init__(self):
            self.env = {}

        def __getitem__(self, key):
            return self.env[key]

        def __setitem__(self, key, value):
            self.env[key] = value

        def __delitem__(self, key):
            del self.env[key]

        def __iter__(self):
            return iter(self.env)

        def __len__(self):
            return len(self.env)

    # Test case for key which has non-ASCII character
    env = TestEnviron()
    env['NON-ASCII'] = b'\xF8'
    text_env = _TextEnviron(env)

# Generated at 2022-06-13 16:40:36.436930
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test that we are returning different values for different environments
    # this will also test that we caching correctly
    assert os.getenv('LANG') != 'abc123'
    environ['LANG'] = 'abc123'
    try:
        assert environ['LANG'] == 'abc123'
        assert environ['LANG'] != os.getenv('LANG')
    finally:
        del environ['LANG']

# Generated at 2022-06-13 16:40:41.048418
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(env={'foo': 'ＡＢＣａｂｃ', 'bar': 'ÄÖÜäöü'}, encoding='utf-8')
    assert(env['foo'] == 'ＡＢＣａｂｃ')
    assert(env['bar'] == 'ÄÖÜäöü')


# Generated at 2022-06-13 16:40:51.390981
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test the getitem method.
    '''
    # Create an instance of the class.
    test_obj = _TextEnviron()
    # Get the value for the requested key.
    result = test_obj['test_key']
    # Verify the value of the result.
    assert result == 'test_value'
    # Verify the size of the cache.
    assert len(test_obj._value_cache) == 1
    # Get the same value again.
    result = test_obj['test_key']
    # Verify the value of the result.
    assert result == 'test_value'
    # Verify the cache size did not change.
    assert len(test_obj._value_cache) == 1
    # Get the value for a different key.
    result = test_obj['other_key']
    # Verify the

# Generated at 2022-06-13 16:40:57.825716
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    ### This test is a little complicated due to the caching that happens
    ###
    ### The following tests are a little dangerous and can fail if something happens to the
    ### environment while they are running.  But they are not likely to be reliably repeatable
    ### to indicate that there is a problem.

    # Check that the raw bytes are returned for byte strings
    env_value = b'bar'
    environ['foo'] = env_value
    assert environ['foo'] == env_value

    # Check that the cached value is returned
    assert environ['foo'] == env_value

    # Check that the cached value is returned even if the environment value changes
    env_value = b'baz'
    environ['foo'] = env_value
    assert environ['foo'] == env_value

    # Check that the raw bytes are returned for text strings
   

# Generated at 2022-06-13 16:41:18.623543
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert environ['ABC'] == os.environ['ABC']
    assert environ['ABC'] == environ['ABC']


# Generated at 2022-06-13 16:41:28.220520
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import shutil
    import tempfile
    from ansible.module_utils.six import StringIO

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 16:41:31.167599
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['a'] = 'b'

    # test normal status
    result = environ['a']
    assert result == u'b'


# Generated at 2022-06-13 16:41:39.096667
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup test
    os.environ["ANSIBLE_TESTING"] = u"foo äöü"
    with open(u"/tmp/foo äöü", "w") as fp:
        fp.write("")
    os.environ["ANSIBLE_TESTING_PATH"] = u"/tmp/" + u"foo äöü"

    # Test
    assert environ["ANSIBLE_TESTING"] == u"foo äöü"
    assert environ["ANSIBLE_TESTING_PATH"] == u"/tmp/foo äöü"

    # Teardown test
    del os.environ["ANSIBLE_TESTING"]

# Generated at 2022-06-13 16:41:42.519232
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    unit test function:
    method: __getitem__() of class _TextEnviron
    '''
    env = _TextEnviron(encoding='utf-8')
    expected = 'toto'
    env['toto'] = expected.encode('utf-8')
    assert env['toto'] == expected



# Generated at 2022-06-13 16:41:48.426897
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Fail if 'a' and 'b' are the same value, which would mean something's wrong with the caching.
    assert environ['a'].encode('utf-8') != environ['b'].encode('utf-8')
    assert environ['a'] == environ['b']
    assert environ['c'] == b'b'.decode('utf-8')
    assert environ['c'] == environ['b']

    # Fail if 'a' is the same value that 'd' returns, which would mean that the caching code doesn't
    # catch the case where the value needs decoding
    assert environ['a'].encode('latin-1') != environ['d'].encode('latin-1')
    assert environ['a'] == environ['d']

# Generated at 2022-06-13 16:41:54.675444
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test _TextEnviron.__getitem__
    """
    t_env = _TextEnviron({'utf8': u'\u20ac'})
    assert t_env['utf8'] == u'\u20ac'
    t_env = _TextEnviron({b'utf8': b'\xe2\x82\xac'})
    assert t_env['utf8'] == u'\u20ac'



# Generated at 2022-06-13 16:41:57.687979
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['LANG'] = 'en_US.UTF-8'
    result = str(os.environ['LANG']) == 'en_US.UTF-8'
    del os.environ['LANG']

    assert result is True

# Generated at 2022-06-13 16:42:01.040902
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Function to test a method __getitem__ of class _TextEnviron """
    object = _TextEnviron()
    instance = object()
    # test that unittest is working.
    assert( isinstance( object, object) )
    # test that unittest is working.
    assert( isinstance( instance, object) )
    # test that a method __getitem__ of class _TextEnviron works.
    assert( hasattr( instance, '__getitem__') )


# Generated at 2022-06-13 16:42:04.406190
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # one byte strings are the same on py2 and py3, so we can use those
    assert environ[b'PATH']


# Generated at 2022-06-13 16:42:50.702314
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes, to_text, to_native
    import codecs

    # Lazy way of generating a unique, non existing filename
    def tmp_fname():
        import tempfile
        return tempfile.mktemp()

    # Lazy way of making sure a file exists and is empty
    def open_fname(fname, mode='ab'):
        with open(fname, mode) as fh:
            pass

    # Lazy way of reading a file
    def read_fname(fname):
        with open(fname, 'rb') as fh:
            return fh.read()


# Generated at 2022-06-13 16:42:59.817762
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Prepare test data
    test_data = {
        'test1': 'test1',
        'test2': b'test2',
        'test3': u'test3',
        'test4': 'test\xea\xb9\x8c\xec\x9d\xb4\xeb\xa1\x9c',
    }

    for key, value in test_data.items():
        if PY3:
            imported_value = environ[key]
        else:
            imported_value = environ[key]
        assert imported_value == value

test__TextEnviron___getitem__()



# Generated at 2022-06-13 16:43:07.293946
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _test(encoding, raw_environ, expected):
        e = _TextEnviron(raw_environ, encoding)
        assert sorted(e.keys()) == sorted(expected.keys()), \
            "Encoding: {0} - Keys {1} != Expected: {2}".format(encoding, e.keys(), expected.keys())
        for k, v in expected.items():
            assert e[k] == v, \
                "Encoding: {0} - Key {1} - Value {2} != Expected: {3}".format(encoding, k, e[k], v)

    _test('utf-8', {'key1': 'value1'}, {'key1': 'value1'})

# Generated at 2022-06-13 16:43:19.217155
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test the _TextEnviron.__getitem__ method with the default environment strings provided
    environ = _TextEnviron(encoding='utf-8')
    for key, value in os.environ.items():
        assert environ[key] == value

    # Test the _TextEnviron.__getitem__ method with a custom environment that is pre-populated with
    # byte strings
    custom_env = {u'ANSIBLY_VAR_ONE': u'ONE', u'ANSIBLY_VAR_TWO': u'TWO'}
    environ = _TextEnviron(custom_env)
    for key, value in custom_env.items():
        assert environ[key] == value

    # Test the _TextEnviron.__getitem__ method with a custom environment dictionary that is
    # pre-pop

# Generated at 2022-06-13 16:43:24.782924
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    from ansible.module_utils._text import to_bytes

    def helper(env, key):
        fsencoding = sys.getfilesystemencoding()
        decode = to_bytes(key, encoding=fsencoding, nonstring='strict', errors='surrogate_or_strict')
        return env[key]

    # Assert that new keys are supported
    os.environ['new_key'] = 'new_value'
    assert environ['new_key'] == 'new_value'
    del os.environ['new_key']

    # Assert that keys which are bytes strings are decoded and cached

# Generated at 2022-06-13 16:43:32.442247
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Initialize
    test_dict = {'A': b'A', 'B': u'B', 'C': b'C', 'D': u'D', 'E': b'E', 'F': u'F', 'G': b'G', 'H': u'H'}
    return_dict = {'A': u'A', 'B': u'B', 'C': u'C', 'D': u'D', 'E': u'E', 'F': u'F', 'G': u'G', 'H': u'H'}

    # Create object and test method
    environ = _TextEnviron(test_dict)
    for key in return_dict:
        assert environ[key] == return_dict[key]



# Generated at 2022-06-13 16:43:43.427898
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    foo = u'Björk Guðmundsdóttir'
    bar = 'Björk Guðmundsdóttir'
    assert to_bytes(foo, encoding='utf-8') == to_bytes(bar, encoding='utf-8')
    assert to_text(foo, encoding='utf-8') == to_text(bar, encoding='utf-8')

    assert environ[to_bytes(foo, encoding='utf-8')] == to_text(foo, encoding='utf-8')
    assert environ[to_text(foo, encoding='utf-8')] == to_text(foo, encoding='utf-8')

# Generated at 2022-06-13 16:43:45.550028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    test_data = to_text(b'\xc3\xb8', encoding='utf-8')

    assert test_data == u'\xf8'


# Generated at 2022-06-13 16:43:46.641584
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ.__getitem__('PATH') == os.environ.get('PATH')

# Generated at 2022-06-13 16:43:54.042531
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test method under normal circumstances
    testvar = 'TESTVAR'
    testvalue = u'Test value'
    testosvar = {testvar: testvalue}
    testenviron = _TextEnviron(testosvar, encoding='utf-8')
    assert (testenviron[testvar] == testvalue), "__TextEnviron___getitem__() failed normal"
    # Test method with a variable key
    testosvar = {u'{0}={1}'.format(testvar, testvalue): testvalue}
    testenviron = _TextEnviron(testosvar, encoding='utf-8')
    assert (testenviron[testvar] == testvalue), "__TextEnviron___getitem__() failed variable key"


# Generated at 2022-06-13 16:45:11.017468
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    unicode_name = u'\xc7\xfc'
    byte_name = b'\xc3\x87\xc3\xbc'

    environ[unicode_name] = byte_name

    assert environ[unicode_name] == unicode_name
    assert environ[byte_name] == unicode_name

# Generated at 2022-06-13 16:45:17.240345
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    textenviron = _TextEnviron()
    # If a key exists, the value is returned decoded
    os.environ['normal_string'] = u'\uC9C4'
    assert textenviron['normal_string'] == u'\uC9C4'
    # If a key exists, and can't be decoded, it will be passed through unmodified
    os.environ['non_utf8'] = '\xff'
    assert textenviron['non_utf8'] == '\xff'



# Generated at 2022-06-13 16:45:26.334118
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'key': b'value'}, 'utf-8')
    assert environ['key'] == 'value'

    environ = _TextEnviron({'key': 'value'}, 'utf-8')
    assert environ['key'] == 'value'

    # unicode in environment gets returned as unicode
    environ = _TextEnviron({'key': u'value'}, 'utf-8')
    assert environ['key'] == 'value'

    # invalid utf-8 in environment gets returned as surrogate escapes
    environ = _TextEnviron({'key': b'\xff'}, 'utf-8')
    assert environ['key'] == u'\udcff'

    # invalid utf-8 in environment gets returned as surrogate escapes

# Generated at 2022-06-13 16:45:29.504388
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_env = {b"key_1": b"value_one"}
    encoding = 'utf-8'
    text_environ = _TextEnviron(raw_env, encoding=encoding)

    # key exists in the raw environment
    assert text_environ.__getitem__("key_1") == "value_one"



# Generated at 2022-06-13 16:45:36.157922
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Also tests str handling
    environ.clear()
    environ['test'] = 'value'
    assert u'value' == environ['test']
    # Also tests bytes handling
    test_bytes = b'\xe5\x94\x8c\xe5\x9f\xba\xe5\x9c\xba\xe5\x99\xa8\xe7\x8e\xaf\xe5\xa2\x83\xe5\x90\xa7'
    environ[b'test2'] = test_bytes
    assert test_bytes.decode('utf-8') == environ['test2']

# Generated at 2022-06-13 16:45:43.367361
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # TEST 1: name 'PY3' has value 'False'
    # EXPECTED: 'True'
    PY3 = False
    environ._raw_environ = {'a': 'b'}
    assert 'b' == environ['a']

    # TEST 2: name 'PY3' has value 'True'
    # EXPECTED: 'True'
    PY3 = True
    environ._raw_environ = {'a': 'b'}
    assert 'b' == environ['a']

    # TEST 3: name 'environ.encoding' has value '1'
    # EXPECTED: 'True'
    environ.encoding = '1'
    environ._raw_environ = {'a': 'b'}
    assert 'b' == environ['a']

   

# Generated at 2022-06-13 16:45:48.097462
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test unicode string
    environ = _TextEnviron({'key':'value'})
    assert environ['key'] == u'value'

    # test non-unicode string
    environ = _TextEnviron({'key':b'value'})
    assert environ['key'] == u'value'

# Generated at 2022-06-13 16:45:56.700669
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert isinstance(environ, _TextEnviron)

    # When key valid and cached
    key = 'MY_ENV_VALUE'
    value = 'this is valid'
    environ._value_cache[key] = value
    assert environ[key] == value

    # When key valid and not cached
    key = 'MY_ENV_VALUE'
    value = 'this is valid'
    del environ._value_cache[key]
    environ._raw_environ[key] = value
    assert environ[key] == value

    # When key invalid and not cached
    key = 'MY_ENV_VALUE'
    value = '\xff'
    del environ._value_cache[key]
    environ._raw_environ[key] = value