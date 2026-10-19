

# Generated at 2022-06-13 16:35:42.850119
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    This is a unittest function to test method __getitem__ of class _TextEnviron
    """
    env = _TextEnviron(encoding='utf-8')
    print(env['PATH'])
    print(env['PYTHONIOENCODING'])
    print(env['LANG'])
    print(env['LC_ALL'])

if __name__ == '__main__':
    test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:35:52.886079
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {b'FOO': b'bar', 'BAR': 'bat', 'BAZ': b'baz'}
    _environ = _TextEnviron(env, encoding='us-ascii')
    def test(v):
        return 'key %s should return proper unicode value' % v
    assert _environ[b'FOO'] == u'bar', test(b'FOO')
    assert _environ[b'FOO'.decode('ascii')] == u'bar', test(b'FOO'.decode('ascii'))
    assert _environ[u'FOO'] == u'bar', test(u'FOO')

# Generated at 2022-06-13 16:35:58.146972
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['KEY'] = 'VAL'
    assert environ['KEY'] == 'VAL'
    os.environ['KEY'] = b'VAL'
    assert environ['KEY'] == 'VAL'
    os.environ['KEY'] = '\xe9'
    assert environ['KEY'] == u'\u00e9'
    del os.environ['KEY']


# Generated at 2022-06-13 16:36:01.487456
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    o = _TextEnviron(env={
        b'foo': b'test foo',
        u'test': u'foo',
        b'bar': b'bar'
    })
    assert o[u'test'] == u'foo'
    assert o[b'foo'] == u'test foo'
    assert o[b'bar'] == u'bar'

# Generated at 2022-06-13 16:36:05.884019
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({'LANG': 'en_US.UTF-8'})
    assert test_environ['LANG'] == u'en_US.UTF-8'

# Generated at 2022-06-13 16:36:16.123960
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that this works on a straight subclass of dict
    # This is covered by the standard library tests.

    # Test that we can get items from the raw dict
    raw_env = os.environ
    if PY3:
        assert environ['PATH'] == raw_env['PATH']
        return
    assert environ['PATH'] == to_text(raw_env['PATH'], encoding='utf-8', nonstring='passthru', errors='surrogate_or_strict')
    # Test that we can get items from the cache
    os.environ['ANSIBLE_TEST_CACHE'] = 'foo'
    environ['ANSIBLE_TEST_CACHE']
    assert 'ANSIBLE_TEST_CACHE' in environ._value_cache
    assert environ._value_cache.get('foo')

# Generated at 2022-06-13 16:36:19.343166
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == '/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games'


# Generated at 2022-06-13 16:36:22.857957
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['test__TextEnviron___getitem__'] = u'value'
    assert environ['test__TextEnviron___getitem__'] == u'value'
    assert type(environ['test__TextEnviron___getitem__']) == type(u'')


# Generated at 2022-06-13 16:36:32.699475
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test a text value from the environment
    environ._raw_environ.clear()
    environ._value_cache.clear()
    env_key = 'TextEnvironUnitTestKey'
    env_value = 'TextEnvironUnitTestValue'
    environ[env_key] = env_value
    assert environ[env_key] == env_value
    assert env_key in environ           # Ensure it's actually in the environment
    assert environ._value_cache         # Ensure cache was updated

    # Ensure that cache is checked before making a new value
    environ._value_cache.clear()
    environ[env_key] = env_value
    assert not environ._value_cache[env_value]

    # Test a byte value from the environment
    environ._raw_environ.clear()
    environ._

# Generated at 2022-06-13 16:36:38.514918
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    _TextEnviron.__getitem__() should return text strings regardless of environment encoding.
    """
    env = _TextEnviron({b'ANSIBLE_SHOW_CUSTOM_STATS': b'0',
                        b'PATH': b'/bin:/usr/bin:/usr/local/bin',
                        b'USER': 'root'})
    assert b'0' == env[b'ANSIBLE_SHOW_CUSTOM_STATS']
    assert 'root' == env['USER']
    assert '/bin:/usr/bin:/usr/local/bin' == env['PATH']

# Generated at 2022-06-13 16:36:42.612546
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == u'/bin:/usr/bin:/usr/local/bin:/usr/local/sbin'
    assert isinstance(environ['PATH'], unicode)


# Generated at 2022-06-13 16:36:48.678018
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # assert 'LANG' in environ
    environ.clear()
    environ['LANG'] = u'en_US.UTF-8'
    assert environ['LANG'] != u'en_US.UTF-8'
    assert environ['LANG'] == 'en_US.UTF-8'


# Generated at 2022-06-13 16:36:53.868310
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Populate the environment dictionary with a bytes key and value
    key = b'TEST_KEY'
    value = b'Test value for unit test'

    assert key not in environ
    environ[key] = value

    assert key in environ
    assert environ[key] == 'Test value for unit test'



# Generated at 2022-06-13 16:36:56.506470
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    assert isinstance(environ, MutableMapping)

    environ['simple'] = 'simple'
    assert environ['simple'] == 'simple'

    with pytest.raises(KeyError):
        environ['non_existing']



# Generated at 2022-06-13 16:37:06.659334
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def create_raw_environ():
        raw_environ = {}
        # Strings decoded to unicode
        #   - key with umlaut: u'B\xf6se'
        #   - value with umlaut: u'f\xfcr'
        #   - key with control character: u'led\x03'
        #   - value with control character: u'\x1b[31mred\x1b[0m'
        # Strings decoded to surrogate escaped <str>
        #   - key with invalid: u'\udc80\udc80'
        #   - value with invalid: u'\udc80\udc80'

# Generated at 2022-06-13 16:37:15.123001
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from six.moves.urllib_request import ProxyHandler, build_opener, HTTPBasicAuthHandler
    proxy = ProxyHandler({
        'http': 'myproxy:8080',
        'https': 'myproxy:8080',
    })
    auth = HTTPBasicAuthHandler()
    auth.add_password(
        realm='PDT',
        uri='http://themis.pdtvitebsk.by:8080',
        user='USERNAME',
        passwd='PASSWORD',
    )
    opener = build_opener(proxy, auth)
    opener.open('http://www.python.org')
    assert environ["http_proxy"] == "myproxy:8080"

# Generated at 2022-06-13 16:37:18.407198
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    expected_value = 'value'
    env = _TextEnviron({'key': expected_value})
    assert env.__getitem__('key') == expected_value


# Generated at 2022-06-13 16:37:20.710582
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['key1'] = 'value1'
    assert environ['key1'] == 'value1'


# Generated at 2022-06-13 16:37:27.628172
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with a UTF-8 string
    testenviron = _TextEnviron()
    testenviron._raw_environ['TESTKEY'] = to_bytes('ümlaut')
    assert 'ümlaut' == testenviron['TESTKEY']
    # Test with a Latin-1 string
    testenviron = _TextEnviron(encoding='latin-1')
    testenviron._raw_environ['TESTKEY'] = to_bytes('ümlaut', encoding='latin-1')
    assert u'ümlaut' == testenviron['TESTKEY']
    # Test with a Unicode string
    testenviron = _TextEnviron()
    testenviron._raw_environ['TESTKEY'] = u'ümlaut'
    assert u'ümlaut' == testenviron['TESTKEY']



# Generated at 2022-06-13 16:37:29.390899
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == os.environ['HOME']

# Generated at 2022-06-13 16:37:42.357151
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:37:45.620265
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # arrange
    env = _TextEnviron({b'ANSIBLE_TEST_GET_ENV_VAR': 'test'}, encoding='utf-8')

    # act and assert
    assert env['ANSIBLE_TEST_GET_ENV_VAR'] == 'test'
    assert env[b'ANSIBLE_TEST_GET_ENV_VAR'] == 'test'



# Generated at 2022-06-13 16:37:50.533240
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST_VARIABLE'] = 'test value'
    # test that value is bytes
    assert isinstance(environ._raw_environ['TEST_VARIABLE'], bytes)
    # assert that the value returned is text
    assert isinstance(environ['TEST_VARIABLE'], text_type)



# Generated at 2022-06-13 16:38:01.656983
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    TEXI="""
       @chapter Module to test _TextEnviron class
       @cindex test_textenviron
    """

    def convert_string_list_to_dict(string_list):
        return_dict = {}

        for i in string_list:
            key, value = i.split('=', 1)
            return_dict[key] = value

        return return_dict

    def test_TextEnviron_on_python_2(environ_dict, encoding):
        test_environ = _TextEnviron(environ_dict, encoding)

# Generated at 2022-06-13 16:38:07.569725
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()

    # Test when value == bytes
    os.environ['LANG'] = 'en_US.utf-8'
    assert environ['LANG'] == 'en_US.utf-8'

    # Test when value == unicode
    os.environ['LANG'] = 'en_US.utf-8'
    assert environ['LANG'] == 'en_US.utf-8'
    del os.environ['LANG']

    # Test when value != bytes and != unicode
    os.environ['LANG'] = ['en_US.utf-8']
    assert environ['LANG'] == 'en_US.utf-8'

    del os.environ['LANG']


# Generated at 2022-06-13 16:38:15.847740
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    # Check byte string
    test_dict = os.environ.copy()
    test_dict[b'ANSIBLE_TEST_GETITEM_BYTE'] = b'test value'
    test_env = _TextEnviron(env=test_dict)
    assert test_env[b'ANSIBLE_TEST_GETITEM_BYTE'] == u'test value'
    # Check text string
    test_dict = os.environ.copy()
    test_dict[u'ANSIBLE_TEST_GETITEM_TEXT'] = u'test value'
    test_env = _TextEnviron(env=test_dict)
    assert test_env[u'ANSIBLE_TEST_GETITEM_TEXT'] == u'test value'
    # Check that cache prevents needless re-conversion
    del test

# Generated at 2022-06-13 16:38:26.541173
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that an environment variable stored as bytes is converted to a text string using the
    # given encoding
    environ._raw_environ[b'foo'] = b'bar'
    assert environ[b'foo'] == u'bar'
    assert environ['foo'] == u'bar'
    # Test that an environment variable stored as text which is not valid in the given encoding
    # raises ValueError
    environ._raw_environ[b'baz'] = b'\xf7'
    try:
        environ['baz']
        assert False    # If we get here, we got a unicode string for the key instead of the expected ValueError
    except ValueError:
        pass



# Generated at 2022-06-13 16:38:28.876975
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LANG'] == 'en_US.UTF-8'

# Generated at 2022-06-13 16:38:33.611677
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test valid Unicode
    os.environ['text_env'] = '£☭'
    assert '£☭' == environ['text_env']

    # Test that decoding errors raise a UnicodeDecodeError
    os.environ['text_env'] = b'\xff'
    try:
        environ['text_env']
    except UnicodeDecodeError:
        pass
    else:
        # Should have raised UnicodeDecodeError
        assert False



# Generated at 2022-06-13 16:38:34.985169
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    assert env['PATH'] == environ['PATH']



# Generated at 2022-06-13 16:38:46.853568
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_vectors = (
        (u'HELLO', u'Hi'),
        (u'ANSIBLE_LANG', u'some_value'),
        (u'ANSIBLE_LANG', u'Значение'),
        (u'ANSIBLE_LANG', u'\u043f'),
        (u'ANSIBLE_LANG', u'\ud800\udf3a'),
    )
    for key, value in test_vectors:
        environ[key] = value
        assert environ[key] == value

# Generated at 2022-06-13 16:38:56.230795
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text
    import os
    import sys
    assert sys.version_info[0] < 3, "This test shouldn't be run on Python3"
    assert os.environ['LANG'] != 'UTF-8', "os.environ shouldn't already be testing as UTF-8"
    assert to_text(os.environ['LANG']) == to_text(u'C'), "os.environ should have default LANG"
    os.environ['LANG'] = 'UTF-8'
    assert os.environ['LANG'] != to_text(u'UTF-8'), "os.environ should be returning byte string"
    text_environ = _TextEnviron()

# Generated at 2022-06-13 16:39:06.602426
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    to_unicode_via_def = lambda key: to_text(environ[key], 'utf-8')
    # An empty environment variable
    environ['EMPTY'] = ''
    assert to_unicode_via_def('EMPTY') == u''
    # A unicode environment variable
    environ['UNICODE'] = u'Всем привет'
    assert to_unicode_via_def('UNICODE') == u'Всем привет'
    # An ascii environment variable
    environ['ASCII'] = 'Hello all'
    assert to_unicode_via_def('ASCII') == u'Hello all'
    # A latin1

# Generated at 2022-06-13 16:39:15.113945
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create Mock for class
    _TextEnviron = create_autospec(_TextEnviron)
    # Create a class object for test
    _TextEnviron_obj = _TextEnviron(encoding='utf-8')
    
    # set environment variables
    _TextEnviron_obj._raw_environ = {'var1': 'v1', 'var2': 'v2'}
    
    # test return value
    assert _TextEnviron_obj['var1'] == 'v1'
    assert _TextEnviron_obj['var2'] == 'v2'
    assert _TextEnviron_obj['var3'] == 'v3'
    

# Generated at 2022-06-13 16:39:22.764181
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    _TextEnviron() -> object with mapping protocol

    Create an object with the same API as os.environ but return unicode objects
    instead of bytes objects.
    '''

    # We want to check for differences in behavior in the file encoding
    # so it's necessary to change the file encoding.  But we don't want to
    # affect other tests that might run simultaneously so save the old
    # encoding value to restore later.
    old_file_encoding = sys.getfilesystemencoding()

# Generated at 2022-06-13 16:39:27.648503
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_env = {'a': 'a'}

    text_env = _TextEnviron(raw_env, encoding='utf-8')
    if PY3:
        assert text_env['a'] == 'a'
    else:
        assert text_env['a'] == u'a'

# Unit Test for method __setitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:31.061775
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(encoding='utf-8')
    assert test_environ['HOME'] is not None
#End of method __getitem__ of class _TextEnviron


# Generated at 2022-06-13 16:39:41.691682
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    __test__ = u"""
    os.environ is a dict of byte strings and unicode strings

    The byte strings are only present in the Python2 env so the class
    needs to have a way to encode to unicode on those Python versions.
    """
    def _getitem_test(env_raw, expected):
        try:
            env_raw[b'python_version_raw'] = sys.version_info
            env_raw[b'python_version'] = sys.version
        except UnicodeDecodeError:
            return False
        env = _TextEnviron(env=env_raw)
        for key in expected:
            if env[key] != expected[key]:
                return False
        return True


# Generated at 2022-06-13 16:39:52.849863
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test bytes strings
    environ = _TextEnviron({b'foo': b'bar'})
    assert environ[b'foo'] == u'bar'
    assert environ.encoding == 'utf-8'

    # Test text strings
    environ = _TextEnviron({u'foo': u'bar'})
    assert environ[u'foo'] == u'bar'
    assert environ.encoding == 'utf-8'

    environ = _TextEnviron({'foo': 'bar'}, encoding='ascii')
    assert environ[u'foo'] == u'bar'
    assert environ['foo'] == 'bar'
    assert environ.encoding == 'ascii'



# Generated at 2022-06-13 16:39:55.760444
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_mock = _TextEnviron(env={b'foo': b'bar'}, encoding='utf-8')
    assert environ_mock.__getitem__('foo') == 'bar'

# Generated at 2022-06-13 16:40:17.178303
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest
    import tempfile
    import os
    import shutil

    test_files_top = tempfile.mkdtemp()

    # Set the environment variable to a directory that has
    # no encoding issues.
    os.environ['ANSIBLE_TEST_VAR'] = test_files_top

    class _TextEnvironTest(unittest.TestCase):

        def test__getitem__(self):
            if PY3:
                value = os.environ['ANSIBLE_TEST_VAR']
                expected = os.environ['ANSIBLE_TEST_VAR']
            else:
                value = os.environ[u'ANSIBLE_TEST_VAR']
                expected = os.environ['ANSIBLE_TEST_VAR']
            self.assertEqual(value, expected)

# Generated at 2022-06-13 16:40:27.289533
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    test_environ = {'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8'}
    environ_utf8 = _TextEnviron(test_environ, encoding='utf-8')
    environ_ascii = _TextEnviron(test_environ, encoding='ascii')

    assert 'C.UTF-8' == environ_utf8['LANG']
    assert 'C.UTF-8' == environ_utf8['LC_ALL']

    with pytest.raises(UnicodeEncodeError):
        environ_ascii['LANG']

    with pytest.raises(UnicodeEncodeError):
        environ_ascii['LC_ALL']

    with pytest.raises(KeyError):
        environ

# Generated at 2022-06-13 16:40:30.261791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=unused-variable
    os.environ['abc'] = 'abc'
    # pylint: enable=unused-variable
    assert environ['abc'] == u'abc'

# Generated at 2022-06-13 16:40:38.833087
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # TODO: the environment variable encoding is platform-dependent, and there is no solid way to test this
    #       on all platforms. The following code only works on my machine (windows).
    assert environ['PYTHONIOENCODING'] == 'UTF-8'
    # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
    # instead of utf-8
    assert 'PYTHONIOENCODING' in environ
    assert 'PATH' in environ

test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:40:50.159377
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The goal here is to get code coverage on the code path which determines the value's encoding.
    # We can't do that in a unit test because Python3's os.environ always returns text.  Instead we
    # make environ a non-mapping object and simulate the different code paths by having the
    # __getitem__ call work differently.
    from ansible.module_utils.six.moves import cStringIO as StringIO
    # Make sure we're picking up our own environ and not the builtin Python one
    assert not isinstance(environ, _TextEnviron)

    def _environ_bytes(self, key):
        """environ.__getitem__ which returns values as bytes"""
        return self._raw_environ[key]


# Generated at 2022-06-13 16:41:00.237223
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """To run unit tests for localhost:
    python -m pytest
    or
    python -m pytest test_name
    """

    # Test with PY3
    if PY3:
        env = _TextEnviron()
        assert os.environ.__getitem__(b'HOME') == env.__getitem__(b'HOME')
        assert isinstance(env.__getitem__(b'HOME'), str)

    # Test with PY2
    else:
        env = _TextEnviron(encoding='iso-8859-1')

# Generated at 2022-06-13 16:41:07.764434
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:41:17.263222
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from tempfile import mkdtemp
    import shutil

    # Test 3: Verify that we don't raise errors for keys with undecodable values
    # This is in the context of Bug #29894
    environ['TEST_KEY'] = b'\x8f'
    assert environ['TEST_KEY'] == u'\ufffd'

    # Test 2: Verify that we don't raise errors for keys with values that can be decoded
    environ['TEST_KEY'] = 'abcde'
    assert environ['TEST_KEY'] == u'abcde'

    # Test 1: Verify that we don't raise errors for keys that do not exist

# Generated at 2022-06-13 16:41:27.114577
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class Env:
        def __init__(self):
            self.data = {}
            self.get = self.data.get
            self.__getitem__ = self.data.__getitem__
        def __setitem__(self, key, value):
            self.data[to_bytes(key, encoding='utf-8')] = to_bytes(value, encoding='utf-8')

    env = Env()
    env['ANSIBLE_DEBUG'] = b'1'
    environ = _TextEnviron(env)
    assert environ['ANSIBLE_DEBUG'] == u'1'
    # Unicode codepoints with the high bit set.  These are outside the ASCII range but are
    # representable in utf-8 or cp1252

# Generated at 2022-06-13 16:41:37.586147
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that accessing the environment works
    assert environ['SHELL'] == '/bin/bash'

    # Test that doing a getitem with a text value works
    assert environ[u'SHELL'] == '/bin/bash'

    # Test that doing a getitem with a text value works
    assert environ[u'SHELL'] == '/bin/bash'

    # Test that doing a getitem with a bytes value that is ascii works
    assert environ[b'SHELL'] == '/bin/bash'

    # Test that doing a getitem with a bytes value that is UTF-8 works

# Generated at 2022-06-13 16:42:00.501735
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The system default should be byte strings
    assert isinstance(os.environ.get('LANG'), bytes)
    # Test with _TextEnviron
    assert isinstance(environ.get('LANG'), unicode)


# Generated at 2022-06-13 16:42:09.632049
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    # Test no key
    def test__TextEnviron___getitem__no_key():
        environ_empty = _TextEnviron(env={})
        if PY3:
            try:
                environ_empty['TEST_KEY']
                assert False, 'No exception raised'
            except KeyError:
                pass
        else:
            try:
                environ_empty['TEST_KEY']
                assert False, 'No exception raised'
            except KeyError:
                pass

    # Test with a key
    def test__TextEnviron___getitem__with_key():
        environ_empty = _TextEnviron(env={'TEST_KEY': 'TEST_VALUE'})

# Generated at 2022-06-13 16:42:18.357215
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    expected_result = u'aëbécød∂'
    from ansible.module_utils._text import to_text
    environ['test_key'] = expected_result
    actual_result = to_text(environ['test_key'], errors='surrogate_or_strict')
    assert u'test_key' in environ
    if actual_result != expected_result:
        raise AssertionError
    expected_result = u'a\udce9\\b\udce8c\udcf8d\ud835\udcbc'
    environ['test_key'] = expected_result
    actual_result = to_text(environ['test_key'], errors='surrogate_or_strict')
    assert u'test_key' in environ

# Generated at 2022-06-13 16:42:24.803012
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    environ = _TextEnviron(encoding='latin-1')
    environ["key"] = "val"

    # test with key value pair in _raw_environ
    assert _TextEnviron.__getitem__(environ, "key") == "val", "incorrect key value pair in TextEnviron"

    # test with missing key value pair in _raw_environ
    try:
        environ["miss"]
    except KeyError:
        assert True, "correct missing key value pair in TextEnviron"
    else:
        assert False, "incorrect missing key value pair in TextEnviron"


# Generated at 2022-06-13 16:42:29.182018
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    assert u'\u20ac' in env[u'PYTHONPATH'] # Euro in the environment

    for k in env:
        assert isinstance(env[k], str) if PY3 else isinstance(env[k], unicode)

# Generated at 2022-06-13 16:42:33.765033
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Checks that if the value is a str, it is returned unchanged
    assert environ.__getitem__('LANG') == 'en_US.UTF-8'

    # Checks that if the value is not a str, it is returned as a str
    environ['TEST'] = b'test'
    assert environ.__getitem__('TEST') == 'test'


# Generated at 2022-06-13 16:42:37.057469
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ.__getitem__('LC_ALL') == 'C'
    assert environ.__getitem__('LC_ALL') == 'C'
    assert environ.__getitem__('LC_ALL') == 'C'
    assert environ.__getitem__('LC_ALL') == 'C'


# Generated at 2022-06-13 16:42:38.563465
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == os.environ['HOME']

# Generated at 2022-06-13 16:42:41.161251
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH']
    assert environ.get('PATH') is not None
    assert environ['PATH'] is environ.get('PATH')

# Generated at 2022-06-13 16:42:48.899855
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:43:39.845994
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(env={})
    try:
        # test non-string key
        environ[1]
        assert False
    except KeyError:
        pass


# Generated at 2022-06-13 16:43:48.455281
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six.moves import builtins
    # set the builtin os.environ to known values

# Generated at 2022-06-13 16:43:50.258003
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(env={'A': 'B'}, encoding='utf-8')
    assert env['A'] == u'B'

# Generated at 2022-06-13 16:43:51.378224
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert '1' == environ['PYTHON_VERSION']

# Generated at 2022-06-13 16:43:52.431039
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _TextEnviron.__getitem__()

# Generated at 2022-06-13 16:43:55.177472
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that the values returned are text types
    assert isinstance(environ['PATH'], str)
    assert isinstance(environ['PATHEXT'], str)
    # Check that encoding is handled properly
    assert environ['PATH'].encode('cp437') == os.environ[b'PATH']



# Generated at 2022-06-13 16:43:57.738131
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_CONFIG'] = 'my_ansible_config'
    assert environ['ANSIBLE_CONFIG'] == u'my_ansible_config'


# Generated at 2022-06-13 16:44:09.715420
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=redefined-variable-type

    from .compat import unittest

    class FakeEnviron(object):
        def __getitem__(self, key):
            # This is the same as the mock data in os_get_version()
            if key == 'OS_MOCK_ENV':
                return b'{"os_version": "16.04", "os_family": "debian"}'
            return b'foo bar'

    class TestGetitem(unittest.TestCase):
        def test_getitem_key(self):
            # Make sure that a standard key returns a string
            e = _TextEnviron(env=FakeEnviron())
            self.assertIsInstance(e['foo'], str)
            # Make sure that mock data returns a string

# Generated at 2022-06-13 16:44:18.925929
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.clear()
    import random
    import string
    import tempfile

    # Ensure that we can access things which are already Unicode on PY3
    def check_unicode_on_py3(data):
        environ['SOME_DATA'] = data
        value = environ['SOME_DATA']
        assert value == data
        del environ['SOME_DATA']
    check_unicode_on_py3(to_text('some data'))
    check_unicode_on_py3(to_text(u'some data'))

    # Ensure that the data we set in the environment is getting decoded
    def check_decoded_on_py2(data, expected_text):
        if not PY3:
            environ['SOME_DATA'] = data

# Generated at 2022-06-13 16:44:31.087341
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    environ = _TextEnviron(os.environ)

    # __getitem__, when given a unicode key, returns a unicode string
    assert isinstance(environ['SHELL'], str)
    # __getitem__, when given a byte string key, returns a unicode string
    assert isinstance(environ[b'SHELL'], str)
    # __getitem__, when given a key that is missing, raises a KeyError
    try:
        environ['_SHELL']
    except KeyError:
        pass
    else:
        assert False, 'Missing variable did not raise a KeyError'

    # __getitem__, when given a variable that was encoded before, returns the correct unicode
    # string.  It does not attempt to re-decode the variable