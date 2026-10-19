

# Generated at 2022-06-13 16:35:57.471080
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # For this test we need to create a new _TextEnviron instance, because other tests in this
    # package may have modified the contents of the global environ object.
    e = _TextEnviron(encoding='utf-8')

    # Test for a known environment variable, PATH
    path_value = e['PATH']
    assert isinstance(path_value, str)

# Generated at 2022-06-13 16:36:05.218863
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Check that __getitem__ works correctly

    This is a regression test for bug #41034

    getitem should return unicode when PY3, else it should return the unicode decoded version of
    the value stored in os.environ
    """
    if PY3:
        # On Python3, the type of os.environ should be unicode
        assert isinstance(environ, _TextEnviron)
        assert isinstance(environ[b'PYTHONPATH'], str)
    else:
        # On Python2, the type of os.environ should be str
        assert isinstance(environ, _TextEnviron)
        assert isinstance(environ[b'PYTHONPATH'], unicode)

# Generated at 2022-06-13 16:36:15.233247
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test a "normal" string
    assert environ.get(u'test') is None, u'Expecting to not find string test'
    environ['test'] = u'Normal string'
    assert environ.get(u'test') == u'Normal string', u'Expecting to find string test'
    del environ[u'test']
    assert environ.get(u'test') is None, u'Expecting to not find string test'

    # test a string with unicode
    assert environ.get(u'test') is None, u'Expecting to not find string test'
    environ['test'] = u'\u20ac'
    assert environ.get(u'test') == u'\u20ac', u'Expecting to find string test'
    del environ[u'test']

# Generated at 2022-06-13 16:36:24.825098
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up test variables
    txtEnv = _TextEnviron()
    test_env = {"KEY_ONE": "VALUE_ONE",
                "KEY_TWO": b"VALUE_TWO",
                "KEY_THREE": u"VALUE_THREE",
                "KEY_FOUR": "VALUE_\xE9"
                }

    # Set the environment
    os.environ = test_env

    # Check values
    assert txtEnv['KEY_ONE'] == u"VALUE_ONE"
    assert txtEnv['KEY_TWO'] == u"VALUE_TWO"
    assert txtEnv['KEY_THREE'] == u"VALUE_THREE"
    assert txtEnv['KEY_FOUR'] == u"VALUE_\xe9"

    # Check with a bad encoding
    txt

# Generated at 2022-06-13 16:36:26.895914
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = u'\U0001F42D'
    assert environ['foo'] == u'\U0001F42D'

# Generated at 2022-06-13 16:36:34.807134
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_test = environ
    test_dic = {'ANSIBLE_MODULE_ARGS': """
    { "test_unicode": "\u5b54",
      "test_str": "ascii",
      "test_str_bytes": "\u5b54" }
    """
    }
    environ_test._raw_environ.clear()
    environ_test._raw_environ.update(test_dic)
    assert environ_test['ANSIBLE_MODULE_ARGS'] == test_dic['ANSIBLE_MODULE_ARGS']

# Generated at 2022-06-13 16:36:41.529547
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    good_values = (
        'foo',
        'föö',
        'f\xf6\xf6',
    )
    bad_values = (
        'f\xff\xf6\xf6',
        'f\xf6\xff\xf6',
        'f\xf6\xf6\xff',
    )

    for value in good_values:
        environ[value] = value
        assert environ[value] == value

    for value in bad_values:
        environ[value] = value
        assert environ[value] != value

# Generated at 2022-06-13 16:36:47.856186
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ1 = MutableMapping()
    environ1['foo'] = b'\xc3\xb2\xc2\xa1'
    environ1['bar'] = b'\xc2\xbf\xc3\xbf'.decode('utf-8')
    environ1['baz'] = 'spam'

    etext = _TextEnviron(env=environ1, encoding='utf-8')
    assert etext['bar'] == '¿ÿ'
    assert etext['foo'] == 'ôá'
    assert etext['baz'] == 'spam'



# Generated at 2022-06-13 16:36:56.089740
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Method test setup
    t_ = _TextEnviron(env=dict(LANG='en_US.UTF-8', noascii=u'\u5e9e'), encoding='utf-8')
    t_._raw_environ[to_bytes('LANG', encoding='utf-8')] = to_bytes('LANG', encoding='utf-8')
    t_._raw_environ[to_bytes('noascii', encoding='utf-8')] = to_bytes('noascii', encoding='utf-8')
    # Test 1
    # t__getitem___t_case_1 - first test for method __getitem__ of class _TextEnviron
    # Input:
    t__getitem___t_case_1_in_1 = 'noascii'
    # Input:


# Generated at 2022-06-13 16:37:06.429140
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup the environment
    #
    # Since we're trying to mimic os.environ, use sys.getfilesystemencoding() instead of utf-8
    # But, if the locale is set to use a utf-8 locale then os.systemencoding will be utf-8.
    # But, if the locale is set to use a utf-8 locale then os.systemencoding will be utf-8.
    encoding = sys.getfilesystemencoding()
    if encoding == 'utf-8':
        os_environ_dict = b'\xE3\x81\x82:b\xE3\x81\x82:c\xE3\x81\x82=d\xE3\x81\x82'

# Generated at 2022-06-13 16:37:16.740558
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test with a string value
    os.environ['test_string'] = 'test_string'
    assert environ['test_string'] == 'test_string'

    # Test a string value with a unicode character
    os.environ['test_unicode'] = "test_unicode_\u20ac"
    assert environ['test_unicode'] == "test_unicode_\u20ac"

    # Test with 2 unicode characters
    os.environ['test_unicode_2'] = "\u20ac_\u20ac"
    assert environ['test_unicode_2'] == "\u20ac_\u20ac"

    # Test an empty string
    os.environ['test_empty'] = ''
    assert environ['test_empty'] == ''

    # Test a non-string value (

# Generated at 2022-06-13 16:37:19.999868
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['PYTHONPATH'] = 'Basho'
    result = environ['PYTHONPATH']
    expected = u'Basho'
    assert result == expected


# Generated at 2022-06-13 16:37:23.647601
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({'test': 'foo', 'test2': 123, b'test3': 'sri'})
    assert env['test'] == 'foo'
    assert env['test2'] == 123
    assert env['test3'] == 'sri'



# Generated at 2022-06-13 16:37:30.242563
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import text_type
    env = _TextEnviron()
    env['TEST'] = 'Test'
    assert isinstance(env['TEST'], text_type)
    for key, value in env.items():
        assert isinstance(key, text_type)
        assert isinstance(value, text_type)


# Generated at 2022-06-13 16:37:34.746806
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    te = _TextEnviron({'foo': u'\u6709'})
    assert te['foo'] == u'\u6709'



# Generated at 2022-06-13 16:37:43.663758
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from hypothesis import given, example
    from hypothesis.strategies import binary, text
    from six import u
    import unittest

    def to_bytes_or_none(value):
        if value is not None:
            value = value.encode('utf-8')
        return value

    @given(binary(), binary())
    @example(None, None)
    @example(u('\U0001f638').encode('utf-8'), None)
    @example(None, u('test').encode('utf-8'))
    def test__getitem__examples(key, value):
        if key is None and value is None:
            # This is an example with unicode surrogate pairs.  os.environ does not decode
            # them.  So we cannot add them to the environment for the test to pass
            return



# Generated at 2022-06-13 16:37:53.118169
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    from ansible.module_utils._text import to_text

    # We need to reset os.environ back to its original state to not interfere with other
    # tests.  We also need to save and restore os.environ to get the unit test to function
    # properly.  Save off the original_os_environ now.
    original_os_environ = os.environ

    # Since this is a unit test and we're going to use os.environ as part of our test, we're going
    # to need to be able to clear it.  We want to make sure that we do not clear the original
    # os.environ so make a copy of os.environ
    os.environ = os.environ.copy()

    # set the ascii encoding so that we can test non-unicode strings
    test_

# Generated at 2022-06-13 16:38:03.209157
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    :type output: subprocess.Popen
    """

    import subprocess
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence


# Generated at 2022-06-13 16:38:13.491011
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env_0 = _TextEnviron()
    # Test with pre-converted byte strings
    env_0[b'bytes_val'] = b'bytes_val'
    assert env_0._raw_environ[b'bytes_val'] == b'bytes_val'
    assert env_0.__getitem__(b'bytes_val') == 'bytes_val'

    # Test with pre-converted unicode strings
    env_0[u'unicode_val'] = u'unicode_val'
    assert env_0._raw_environ['unicode_val'] == b'unicode_val'
    assert env_0.__getitem__(u'unicode_val') == 'unicode_val'

    env_1 = _TextEnviron()
    # Test with pre-converted byte strings
    env_

# Generated at 2022-06-13 16:38:17.712350
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # set the environment variable
    os.environ[to_bytes('mè')] = to_bytes('fýzík')

    # test
    key = to_text('mè')
    expected = to_text('fýzík')
    actual = environ[key]
    assert actual == expected, 'Expected %s, got %s' % (expected, actual)



# Generated at 2022-06-13 16:38:24.567054
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Unit test for method __getitem__ of class _TextEnviron

    :returns: None
    """
    _environ = _TextEnviron({b'1': b'foo',
                             b'2': b'\xc2\xa2'})

    assert _environ['1'] == 'foo'
    assert _environ['2'] == u'¢'



# Generated at 2022-06-13 16:38:29.834306
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    subject = _TextEnviron()
    subject['str'] = 'str'
    assert subject['str'] == 'str'
    subject['unicode'] = u'unicode'
    assert subject['unicode'] == u'unicode'
    subject['bytes'] = b'bytes'
    assert subject['bytes'] == u'bytes'


# Generated at 2022-06-13 16:38:31.508096
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    result = _TextEnviron(encoding='utf-8')['LC_CTYPE']
    assert result == 'en_US.utf-8'

# Generated at 2022-06-13 16:38:37.503951
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # _TextEnviron should return a text value even on Python 2
    assert isinstance(environ['PATH'], str)
    # _TextEnviron should return a text value even when the environment variable is not utf-8
    os.environ['UNICODE_PATH'] = b'\xe5\xe4\xf6\xc4'
    assert isinstance(environ['UNICODE_PATH'], str)
    assert environ['UNICODE_PATH'] == u'åäöÄ'

# Generated at 2022-06-13 16:38:47.551440
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test to_text and encoding bahavior of class _TextEnviron"""

    # Set text vars to unicode, decode them to bytes
    environ.update({
        'test_var_utf8': 'test_utf8',
    })

    assert environ['test_var_utf8'] == 'test_utf8'

    # Set bytes var to bytes, encode them to unicode
    environ.update({
        'test_bytes_var_utf8': 'test_bytes'.encode('utf-8'),
    })

    assert environ['test_bytes_var_utf8'] == 'test_bytes'

    # Set bytes var to bytes, encode them to unicode with nonstring='passthru'

# Generated at 2022-06-13 16:38:50.369612
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test = _TextEnviron(encoding='utf-8')
    test['foo'] = 'bar'
    assert test['foo'] == 'bar'
    return


# Generated at 2022-06-13 16:38:54.390664
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    weird_envvar = u'w\u00e4eird'

    # Set the value to something non-ascii
    environ[weird_envvar] = u'v\u00e4lue'
    # Make sure we can retrieve it
    assert environ[weird_envvar] == u'v\u00e4lue'

# Generated at 2022-06-13 16:39:05.113769
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import tempfile
    import platform
    environ_cp = os.environ.copy()

    default_encoding = sys.getfilesystemencoding()

    # Encoding is identical on all platforms
    if platform.system() == 'Windows':
        encoding = 'mbcs'
    else:
        encoding = 'utf-8'

    # Run tests in a temporary directory to ensure no files from other tests are used

# Generated at 2022-06-13 16:39:11.444004
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The tests below in the if PY3 block need to use os.environb.  Otherwise the results returned
    # by os.environ will be text instead of bytes
    if PY3:
        real_environ = os.environb
    else:
        real_environ = os.environ

    # When fetching something that is already in the cache return the cached text
    env = _TextEnviron({b'ANSIBLE_CACHING_TEST': b'cachedvalue'})
    env._value_cache = {b'cachedvalue': 'textcachedvalue'}
    assert env['ANSIBLE_CACHING_TEST'] == 'textcachedvalue'

    # When something is not in the cache, return the decoded value

# Generated at 2022-06-13 16:39:18.986257
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding() instead of
    # utf-8
    global_encoding = sys.getfilesystemencoding()
    utf8_encoding = 'utf-8'

# Generated at 2022-06-13 16:39:28.118012
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The following uses of assert assume that _TextEnviron is used as a replacement for
    # os.environ.  When that's the case, os.environ contains bytestrings and _TextEnviron
    # contains unicode strings.  If _TextEnviron is constructed manually, it will have whatever
    # type of strings you put into it.
    assert b'HOME' in os.environ
    assert 'HOME' not in environ
    assert os.environ[b'HOME'] == environ['HOME']


# Generated at 2022-06-13 16:39:31.404064
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron({b'one': b'1', b'two': b'2', b'three': b'3'})

    assert test_env['one'] == u'1'
    assert test_env['two'] == u'2'
    assert test_env['three'] == u'3'


# Generated at 2022-06-13 16:39:37.250326
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['ANSIBLE_STDOUT_CALLBACK'] = 'json'
    if PY3:
        assert environ['ANSIBLE_STDOUT_CALLBACK'] == 'json'
    else:
        assert environ['ANSIBLE_STDOUT_CALLBACK'] == u'json'


# Generated at 2022-06-13 16:39:45.688430
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    test_environ = environ._TextEnviron()
    # If the answer is not correct, the following line throws an exception
    test_environ.__getitem__('HOME') == os.environ.__getitem__('HOME')
    # If the answer is not correct, the following line throws an exception
    test_environ.__getitem__('HOME') == os.environ['HOME']
    # If the answer is not correct, the following line throws an exception
    test_environ['HOME'] == os.environ.__getitem__('HOME')
    # If the answer is not correct, the following line throws an exception
    test_environ['HOME'] == os.environ['HOME']
    # If the answer is not correct, the following line throws an exception

# Generated at 2022-06-13 16:39:56.784012
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if os.name == 'nt':
        raise AssertionError("This method is intended to be used in a Unix-like environment")

    import tempfile
    temp_env_dict = {'BLUE': 'red', 'GREEN': 'yellow'}


# Generated at 2022-06-13 16:40:05.367965
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_text

    binary_value = b'\xff\xfe\xfd\xfc'

    # In this first test, we will see what happens when we have a binary value in the environment
    # when we ask for the python2-style default environment
    os.environ[b'binary_value'] = binary_value

    # Get the environment as it is on python2 systems by default
    raw_environ = os.environ

    # Expected raw value is the binary value we put into the environment
    assert raw_environ[b'binary_value'] == binary_value

    # Expected text value is the python2-style string

# Generated at 2022-06-13 16:40:17.223781
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    my_environ = _TextEnviron({u'x': u'10', u'y': u'4.2'})
    assert my_environ['x'] == u'10'
    assert my_environ['y'] == u'4.2'

    assert my_environ[u'x'] == u'10'
    assert my_environ[u'y'] == u'4.2'

    assert my_environ[b'x'] == u'10'
    assert my_environ[b'y'] == u'4.2'

    assert my_environ[to_bytes(u'x', encoding='utf-8')] == u'10'
    assert my_environ[to_bytes(u'y', encoding='utf-8')] == u'4.2'

    assert my_environ

# Generated at 2022-06-13 16:40:27.322899
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for proper decoding
    env = dict(
        var1 = to_bytes('\xe4\xbd\xa0\xe5\xa5\xbd', encoding='utf-8'),
        var2 = to_bytes('漢字', encoding='utf-8'),
        var3 = b'Hello, world',
        var4 = to_bytes('\xf1\x88\x80\x80', encoding='utf-16'),
    )

    t_env = _TextEnviron(env, encoding='utf-8')

    assert t_env['var1'] == u'你好'
    assert t_env['var2'] == u'漢字'
    assert t_env['var3'] == u'Hello, world'

# Generated at 2022-06-13 16:40:36.165733
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=unused-variable
    class EnvStub(object):
        # pylint: disable=too-few-public-methods,no-self-use
        def __init__(self, env):
            self.env = env
            self.values = {}

        def __getitem__(self, key):
            return self.env[key]

        def __contains__(self, key):
            return key in self.env

        def __setitem__(self, key, value):
            self.values[key] = value

        def __delitem__(self, key):
            del self.values[key]

    # pylint: disable=protected-access
    # Test surrogate escapes
    test_env = EnvStub({b'key': b'\xff\xd8'})


# Generated at 2022-06-13 16:40:41.184497
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    _TextEnviron.__getitem__ should return text strings when passed to the dict interface
    """
    # Make a dict with bytes the value to make sure we're converting that to text
    raw_env = {'one': b'bytes', 'two': to_bytes('accents', encoding='utf-8')}
    text_env = _TextEnviron(raw_env, encoding='utf-8')

    assert 'bytes' == text_env['one']
    assert u'accents' == text_env['two']

# Generated at 2022-06-13 16:40:54.072347
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    textenviron = _TextEnviron({'b': 'baz', 'a': 'foo', 'c': 'bar'})

    assert textenviron['b'] == 'baz'
    assert textenviron['a'] == 'foo'
    assert textenviron['c'] == 'bar'

    textenviron._raw_environ = {'b': 'Baz', 'a': 'Foo', 'c': 'Bar'}

    assert textenviron['b'] == 'Baz'
    assert textenviron['a'] == 'Foo'
    assert textenviron['c'] == 'Bar'

    textenviron._raw_environ = {'b': 'Baz', 'a': 'Foo'}

    assert textenviron['b'] == 'Baz'
    assert textenviron['a'] == 'Foo'

# Generated at 2022-06-13 16:41:01.647028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({'string': 'a',
                            'bytes': b'b',
                            'unicode': u'c',
                            'text_bytes': '\xc3\xa9',
                            'text_unicode': u'\u00e9'})
    assert environ['string'] == 'a'
    assert environ['bytes'] == u'b'
    assert environ['unicode'] == u'c'
    assert environ['text_bytes'] == u'\u00e9'
    assert environ['text_unicode'] == u'\u00e9'


# Generated at 2022-06-13 16:41:03.962980
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST'] = 'testValue'
    assert environ['TEST'] == 'testValue'


# Generated at 2022-06-13 16:41:08.698624
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_KEY'] = u'I am a unicøde string'
    assert os.environ['ANSIBLE_TEST_KEY'] == u'I am a unicøde string'
    del os.environ['ANSIBLE_TEST_KEY']

# Generated at 2022-06-13 16:41:17.736792
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def test_it(test_input, expected_result):
        # Setup
        env = _TextEnviron()
        env.encoding = 'utf-8'
        env._raw_environ = {
            'ansible_key': 'value'
        }
        env._raw_environ[test_input] = 'ansible_key'
        # Exercise
        result = env[test_input]
        # Verify
        assert result == expected_result
        # Cleanup - none necessary

    if PY3:
        test_it('ansible_key'.encode('utf-8'), 'value')
        test_it('ansible_key', 'value')
    else:
        test_it(b'ansible_key', u'value')
        test_it(u'ansible_key', u'value')

# Generated at 2022-06-13 16:41:24.936267
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Check that we get the same results as os.environ does on the same platform"""
    from ansible.module_utils._compat_test_case import AnsibleCompatTestCase

    class TestCase(AnsibleCompatTestCase):
        def setUp(self):
            self.test_environ = _TextEnviron()

        def test_key_exists(self):
            # test that a key that exists returns the same on _TextEnviron as it does on os.environ
            key_in_bytes = b'TEST'
            key_in_text = key_in_bytes.decode("utf-8")
            value_in_bytes = b'value'
            value_in_text = value_in_bytes.decode("utf-8")
            os.environ[key_in_bytes] = value_in_

# Generated at 2022-06-13 16:41:36.122127
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Variable encode will set to the value of the item, encoded to bytes and stored in environ.
    # If a raw string appears in the environment, this should be a no-op.
    encode = b"raw"

    # For each tuple in the list below, the first element is the string that will be stored in
    # environ. The second element is the value that is expected to be returned by __getitem__.
    # The third element (if present) is the value that is expected to be returned when environ is
    # passed to os.getenv.

# Generated at 2022-06-13 16:41:40.132353
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with Python3
    sys.version_info = (3, 5, 1)
    assert environ['LANG'] == 'en_US.UTF-8'
    # Test with Python2
    sys.version_info = (2, 7, 9)
    assert environ['LANG'] == 'en_US.UTF-8'



# Generated at 2022-06-13 16:41:43.748738
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    with pytest.raises(KeyError):
        _TextEnviron()['spam'] != 'eggs'
    _TextEnviron()['ANSIBLE_TEST_SPAM'] = 'eggs'
    assert _TextEnviron()['ANSIBLE_TEST_SPAM'] == 'eggs'
    del _TextEnviron()['ANSIBLE_TEST_SPAM']

# Generated at 2022-06-13 16:41:54.968767
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that method __getitem__ of class _TextEnviron returns text even when given bytes.
    """
    # Test case 1: should return the text variable when given the text variable.
    text_environ = _TextEnviron({'text_variable': 'value_text'})
    assert text_environ['text_variable'] == 'value_text'

    # Test case 2: should return the text variable when given the bytes variable.
    bytes_environ = _TextEnviron({'bytes_variable'.encode('utf-8'): 'value_bytes'.encode('utf-8')})
    assert bytes_environ[u'bytes_variable'] == 'value_bytes'


# Generated at 2022-06-13 16:42:10.222997
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test: raw value is text
    test_raw_environ = {'key1': u'value1', 'key2': u'value2'}
    test_text_environ = _TextEnviron(test_raw_environ)
    assert test_text_environ['key1'] == u'value1'
    assert test_text_environ['key2'] == u'value2'

    # Test: raw value is bytes
    test_raw_environ = {'key1': b'value1', 'key2': b'value2'}
    test_text_environ = _TextEnviron(test_raw_environ)
    assert test_text_environ['key1'] == u'value1'
    assert test_text_environ['key2'] == u'value2'

    # Test: raw

# Generated at 2022-06-13 16:42:13.412126
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    expected = '花'
    environ['unicode'] = expected
    assert environ['unicode'] == expected
    assert isinstance(environ['unicode'], type(u""))



# Generated at 2022-06-13 16:42:17.842982
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TestKey'] = u'ABC123'
    assert environ['TestKey'] == u'ABC123'

    environ['TestKey'] = u'\u1234'
    assert environ['TestKey'] == u'\u1234'

# Generated at 2022-06-13 16:42:23.743546
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'PYTHONPATH': to_bytes(u'.:temp:a:b:c:d:e', encoding='utf-8', nonstring='strict', errors='surrogate_or_strict')}, encoding='utf-8')

    result = env[b'PYTHONPATH']
    expected = u'.:temp:a:b:c:d:e'

    assert result == expected, 'Failed to get item from unicode environment variable'

# Generated at 2022-06-13 16:42:28.833845
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # 1. Set the following variables
    key = 'TEST_KEY'
    value = to_bytes(u'тест')
    # 2. Call the code to be tested
    environ[key] = value
    result = environ[key]
    # 3. Assert results
    assert result == u'тест'

# Generated at 2022-06-13 16:42:39.875192
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # assert that the getitem method returns the converted bytes to text
    environ._raw_environ[b'abc'] = b'abc'
    assert environ['abc'] == 'abc'

    # assert that the getitem method returns the value from the cache if the raw value is identical
    # to another raw value
    environ._value_cache[b'abc'] = 'cba'
    assert environ['abc'] == 'cba'
    environ._value_cache[b'xyz'] = 'zyx'
    assert environ._value_cache[b'abc'] == 'cba'
    assert environ._value_cache[b'xyz'] == 'zyx'

    # assert that an error is thrown if the encoding is invalid and errors=strict

# Generated at 2022-06-13 16:42:50.584359
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_utf8_encoded = _TextEnviron(env={"foo": "bar"}, encoding="utf-8")
    assert environ_utf8_encoded["foo"] == "bar"

    environ_utf8_encoded = _TextEnviron(env={"foo": "bar\u1234"}, encoding="utf-8")
    # By default, we replace invalid characters with u'<xFFFD>' per the warning in the six module
    assert environ_utf8_encoded["foo"] == "bar\uFFFD"

    environ_utf8_encoded = _TextEnviron(env={"foo": "bar\u1234"}, encoding="utf-8", errors="ignore")
    assert environ_utf8_encoded["foo"] == "bar"

    environ_utf8_encoded = _TextEn

# Generated at 2022-06-13 16:43:01.883734
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    key = 'blessed_new_var'
    # In the following, the bytes are utf-8:decodeable, however, encoding to utf-8
    # from iso-8859-1 (which is what 'locale.getpreferredencoding()' returns for me)
    # will fail.  So we have to use surrogateescape
    value_unicode = u'\ufffd\ufffd\ufffd\ufffd\ufffd\u0131\ufffd\ufffd\ufffd\ufffd\ufffd'
    value_bytes = '\xfd\xfd\xfd\xfd\xfd\xfd\xfd\xfd\xfd\xfd'
    os.environ[key] = value_bytes
    environ = _TextEnviron(encoding='iso-8859-1')
   

# Generated at 2022-06-13 16:43:10.886326
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    # Create a simple environment variable that we can control
    os.environ['ANSIBLE_TEST_STR'] = u'\u1234'

    # _TextEnviron.__getitem__ needs a parameter called "key"
    # that should be of type string
    # return a unicode string

    class Test__TextEnviron___getitem__Params(unittest.TestCase):

        def test_key_is_not_string(self):
            self.assertRaises(UnicodeEncodeError, environ.__getitem__, b'ANSIBLE_TEST_STR')

# Generated at 2022-06-13 16:43:15.653458
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    with patch.object(os, 'environ', {b'a': b'b', u'c': u'd'}):
        environ = _TextEnviron(env=os.environ)
        assert environ['a'] == u'b'
        assert environ['c'] == u'd'

# Generated at 2022-06-13 16:43:35.589530
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_VAR'] = b'F\xc3\xb6\xc3\xb6B\xc3\xa4R'
    if PY3:
        assert environ['ANSIBLE_TEST_VAR'] == 'FööBäR'
    else:
        assert environ['ANSIBLE_TEST_VAR'] == u'FööBäR'
    del os.environ['ANSIBLE_TEST_VAR']


# Generated at 2022-06-13 16:43:45.629445
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup the environment
    os.environ['ANSIBLE_TEST_TEXTENVIRON_NONSTRING'] = 'abcde\xac\xed\x00\x05'
    os.environ['ANSIBLE_TEST_TEXTENVIRON_ECCTAG'] = 'abcde\xff'
    os.environ['ANSIBLE_TEST_TEXTENVIRON_ECCSURROGATE'] = '\udc00\ud800'
    os.environ['ANSIBLE_TEST_TEXTENVIRON_ECC'] = '\xe5\xf6\xe5\xf6'

    environ = _TextEnviron(encoding='utf-8')


# Generated at 2022-06-13 16:43:49.260893
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    actual = environ['ANSIBLE_PYTHON_INTERPRETER']
    expected = '/usr/bin/python3'
    assert actual == expected, 'The method __getitem__ of _TextEnviron class does not work as expected'


# Generated at 2022-06-13 16:43:56.150095
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test when running on Python2
    # Make sure that the test environment and the class under test are set up as they would be when
    # running on Python2
    environ['PYTHONPATH'] = '/home/ansible/devel/lib/python2.7/site-packages'
    environ['PYTHONIOENCODING'] = 'UTF-8'

    # Test getting a value that is already in the correct encoding
    assert environ['PYTHONPATH'] == '/home/ansible/devel/lib/python2.7/site-packages'

    # Test getting a value that is not in the correct encoding (one that was added by an earlier
    # version of this module)
    environ['TEST_GETITEM_VALUE'] = 'test_\xc3\x85_value'

# Generated at 2022-06-13 16:43:58.690485
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    _TextEnviron.__getitem__ test fixture
    '''
    test_env = {'foo': 'déjà vu'}
    text_environ = _TextEnviron(env=test_env)

    assert text_environ['foo'] == 'déjà vu'



# Generated at 2022-06-13 16:44:03.242986
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    assert env[to_bytes('x', encoding=env.encoding)] == to_text(b'x', encoding=env.encoding)
    assert env[to_bytes('x', encoding=env.encoding)] == u'x'


# Generated at 2022-06-13 16:44:08.288610
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_KEY'] = u'\u04c4'
    assert environ['TEST_KEY'] == u'\u04c4'
    environ['TEST_KEY'] = '\xc4'
    assert environ['TEST_KEY'] == '\xc4'


# Generated at 2022-06-13 16:44:17.231182
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with un-encoded values
    b_v1 = b'abc'
    environ[b_v1] = b_v1
    assert environ[b_v1] == u'abc'

    # Test with encoded values
    b_v2 = b'\xc3\x9cber'
    environ[b_v2] = b_v2
    assert environ[b_v2] == u'\xdcber'

    # Test with cache of previously used value
    b_v2_2 = b'\xc3\x9cber'
    environ[b_v2_2] = b_v2
    assert environ[b_v2_2] == u'\xdcber'

# Generated at 2022-06-13 16:44:18.527068
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Nothing to do here because class _TextEnviron is used strictly in the context of class ModuleBase
    pass

# Generated at 2022-06-13 16:44:27.201537
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    #pylint: disable=anomalous-backslash-in-string
    #pylint: disable=line-too-long
    if sys.version_info < (3, 0):
        assert environ['PYTHONIOENCODING'] == 'UTF-8'
        assert environ['PYTHONIOENCODING'] == 'UTF-8'
        assert environ['PYTHONIOENCODING'] == u'UTF-8'
    else:
        assert environ['PYTHONIOENCODING'] == 'UTF-8'

# Generated at 2022-06-13 16:44:56.832799
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    environ_ = _TextEnviron(env={b'key': b'value'}, encoding='utf-8')

    # Act
    result = environ_['key']

    # Assert
    assert result == 'value'



# Generated at 2022-06-13 16:45:04.982543
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        del os.environ['TEST_KEY']
    except KeyError:
        pass
    os.environ['TEST_KEY'] = 'foo'
    # Since unit tests may be run in any language, ensure we don't
    # come across a language that's not utf-8
    if environ['TEST_KEY'] != 'foo':
        raise AssertionError('Env variable did not match')

    os.environ['TEST_KEY'] = '\xe4'
    if environ['TEST_KEY'] != '\xe4':
        raise AssertionError('Env variable did not match')

    os.environ['TEST_KEY'] = '\x81\xe4'
    if environ['TEST_KEY'] != '\x81\xe4':
        raise Assertion

# Generated at 2022-06-13 16:45:09.182828
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    env = _TextEnviron()
    assert env['HOME'] == os.environ['HOME']

    # Test just the caching by manually deleting the cache and making sure it gets recreated
    env._value_cache.clear()
    assert env['HOME'] == os.environ['HOME']
    assert env['HOME'] is env['HOME']

# Generated at 2022-06-13 16:45:20.072277
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ[b'TEST_KEY'] = b'test_value'
    environ[b'TEST_KEY'] = b'test_value'
    assert environ[b'TEST_KEY'] == u'test_value'
    assert environ[u'TEST_KEY'] == u'test_value'
    environ[u'TEST_KEY'] = 'test_value'
    assert environ[b'TEST_KEY'] == u'test_value'
    assert environ[u'TEST_KEY'] == u'test_value'
    environ[b'TEST_KEY'] = u'test_value'
    assert environ[b'TEST_KEY'] == u'test_value'
    assert environ[u'TEST_KEY'] == u'test_value'
    os

# Generated at 2022-06-13 16:45:28.262089
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    A method that checks if the _TextEnviron.__getitem__() method behaves
    as expected when the KEY is present in the environment.
    """
    environ['PYTHON3_PATH'] = '/usr/local/bin/python3'
    # Assert that the value is a Text type. In Python 2, the value will be
    # bytes (str in Python 2) while the value in Python 3 will be of type Text
    # (str in Python 3).
    assert type(environ['PYTHON3_PATH']) == str
    # Assert that environ['PYTHON3_PATH'] == '/usr/local/bin/python3'
    assert environ['PYTHON3_PATH'] == '/usr/local/bin/python3'
    del environ['PYTHON3_PATH']

# Generated at 2022-06-13 16:45:30.529135
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({b'a': b'h llo'})
    assert e[b'a'] == u'h llo'


# Generated at 2022-06-13 16:45:38.632354
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Verify that _TextEnviron.__getitem__ works when a key is not cached
    """

    # Create a _TextEnviron
    te = _TextEnviron(env={b'key': b'value'})

    # Ensure that we get back a text value
    assert isinstance(te['key'], str)

    # Ensure that the value is decoded correctly when we get it back
    assert te['key'] == u'value'

    # Ensure that the value is cached
    assert len(te._value_cache) == 1

    # Ensure that the value is stored in the cache in decoded form
    assert list(te._value_cache.keys())[0] == b'value'
    assert list(te._value_cache.values())[0] == u'value'



# Generated at 2022-06-13 16:45:44.986089
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Remove CDPATH from os.environ so that we can set it for our unit tests
    # Otherwise we will get a false positive
    if 'CDPATH' in environ:
        del environ['CDPATH']

    # Set the environment variables with byte strings
    environ[b'TEST1'] = b'abcdef'
    environ[b'TEST2'] = b'\xe5\xc0\xb5'
    environ[b'TEST3'] = b'\xec\xa9'

    # Try fetching values and expect back a text string
    assert environ[b'TEST1'] == u'abcdef'
    assert environ[b'TEST2'] == u'\u5c0b'
    assert environ[b'TEST3'] == u'\uc619'


# Generated at 2022-06-13 16:45:54.611026
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_backup = environ
    sys_environ_backup = sys.environ