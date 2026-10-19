

# Generated at 2022-06-13 16:35:58.841919
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """The __getitem__() method should return a text string corresponding to the given key from the
    environment.

    Note that the environment variable `TEST_GETITEM__KEY` must be set before running this test.
    """
    return (type(environ['TEST__GETITEM__KEY']) == str)


# Generated at 2022-06-13 16:36:06.667314
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:36:17.960940
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with a couple of unicode characters (should decode as utf-8)
    # Also verify that we can use the same key more than once (useful for convenience in
    # calling methods)
    fixed_string = u'foo\N{SNOWMAN}bar'
    encoded_string = fixed_string.encode('utf-8')

    environ['foo'] = fixed_string
    assert environ['foo'] == fixed_string
    assert environ['foo'] == fixed_string

    # Test with bytes which match a character set (should decode as utf-8)
    environ['foo'] = encoded_string
    assert environ['foo'] == fixed_string
    assert environ['foo'] == fixed_string

    # Test with bytes which do not match a character set (should error out as a non-text field)
    #


# Generated at 2022-06-13 16:36:19.066609
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _TextEnviron.__getitem__('foo')

# Generated at 2022-06-13 16:36:19.796558
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import six
    assert isinstance(environ['PATH'], six.text_type)



# Generated at 2022-06-13 16:36:22.309526
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''Test _TextEnviron.__getitem__'''
    os.environ.clear()
    environ['HOME'] = u'/home/user'
    assert isinstanc

# Generated at 2022-06-13 16:36:32.469150
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')

    os.environ['ANSIBLE_TEST_KEY_1'] = b'ANSIBLE_TEST_VALUE_1'
    assert env['ANSIBLE_TEST_KEY_1'] == u'\u00c0NSIBLE_TEST_VALUE_1' # with surrogate

    os.environ['ANSIBLE_TEST_KEY_2'] = b'\xc0\x90'
    assert env['ANSIBLE_TEST_KEY_2'] == u'\ufffd\ufffd' # with replacement (non-surrogate failure)

    os.environ['ANSIBLE_TEST_KEY_3'] = b'\x80'
    assert env['ANSIBLE_TEST_KEY_3'] == u'\ufffd' # with replacement (surrogate failure)

# Generated at 2022-06-13 16:36:34.324708
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    env['TEST'] = 'foo'

    assert env['TEST'] == u'foo'

# Generated at 2022-06-13 16:36:43.071373
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:36:54.090949
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    # simple test
    os.environ['FOO'] = 'bar'
    assert environ['FOO'] == 'bar'
    assert type(environ['FOO']) is type('bar')

    # test with non-ASCII value
    os.environ['FOO'] = 'André'
    assert environ['FOO'] == 'André'
    assert type(environ['FOO']) is type('André')

    # test with an environment variable that varies
    os.environ['FOO'] = 'bar'
    for i in range(10):
        if i % 2:
            os.environ['FOO'] = 'André'
        else:
            os.environ['FOO'] = 'bar'

# Generated at 2022-06-13 16:37:06.659332
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Given
    environ = _TextEnviron(encoding='utf-8')
    environ['TEST'] = 'STR'
    environ['TEST_BINARY'] = b'\x80\x81\x82\x83'
    environ['TEST_TEXT'] = u'\U0001f600'

    # When
    result = environ['TEST']

    # Then
    assert result == 'STR'
    assert type(result) is type('STR')

    # When
    result = environ['TEST_BINARY']

    # Then
    assert result == u'\u0080\u0081\u0082\u0083'
    assert type(result) is type(u'\u0080')

    # When
    result = environ['TEST_TEXT']

    #

# Generated at 2022-06-13 16:37:16.047079
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def fake_environ(env_key, default=None):
        if env_key == 'FOO':
            return 'bar'
        if env_key == 'BAR':
            return 'baz'
        raise KeyError

    def fake_environ_with_error(env_key, default=None):
        if env_key == 'FOO':
            raise UnicodeError
        raise KeyError

    import mock
    with mock.patch('os.environ') as raw_environ:
        raw_environ.__contains__.side_effect = fake_environ.__call__
        raw_environ.__getitem__.side_effect = fake_environ.__call__
        # Decode a key that's not in our cache
        assert b'bar' == environ._raw_environ['FOO']


# Generated at 2022-06-13 16:37:23.391822
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.update({
        'K1': '\xe9',
        'K2': '\xe9',
        'K3': b'\xe9',
        'K4': b'\xe9',
        'K5': b'\xe9',
    })
    assert environ['K1'] == 'é'
    assert environ['K2'] == 'é'
    assert environ['K3'] == 'é'
    assert environ['K4'] == 'é'
    assert environ['K5'] == 'é'



# Generated at 2022-06-13 16:37:26.748388
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    env['test'] = 'test'
    assert env['test'] == u'test'



# Generated at 2022-06-13 16:37:38.417784
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setter and getter: works
    environ["TEST_VARIABLE"] = "test_value"
    assert environ["TEST_VARIABLE"] == "test_value"

    # A byte string
    byte_string = "this is a byte string"
    environ["TEST_VARIABLE"] = byte_string
    assert environ["TEST_VARIABLE"] == byte_string

    # Unicode string with chars in 0x7F
    unicode_string = u"☺"
    environ["TEST_VARIABLE"] = unicode_string
    assert environ["TEST_VARIABLE"] == unicode_string

    # Unicode string with chars outside 0x7F
    unicode_string = u"☃"

# Generated at 2022-06-13 16:37:44.588558
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Simple case: value decoded properly
    result = environ['PYTHONPATH']
    assert isinstance(result, text_type)

    # Values not in the environment will throw a KeyError
    from pytest import raises
    with raises(KeyError):
        environ['_THIS_ENV_VAR_DOES_NOT_EXIST']

    # Values which are not decodable with the specified encoding will throw a UnicodeError
    not_utf8_b = b'\xA3'
    not_utf8_t = u'\u00A3'
    not_utf8_e = 'ascii'

# Generated at 2022-06-13 16:37:51.067087
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    global environ
    environ = _TextEnviron(env={'SOME_VARIABLE': 'a value'})
    assert environ['SOME_VARIABLE'] == 'a value'
    environ = _TextEnviron({b'SOME_VARIABLE': b'a value'}, 'utf-8')
    assert environ['SOME_VARIABLE'] == 'a value'
    environ = _TextEnviron({b'SOME_VARIABLE': b'a value'}, 'ascii')
    assert environ['SOME_VARIABLE'] == 'a value'
    environ = _TextEnviron({b'SOME_VARIABLE': u'a value'.encode('utf-8')}, 'utf-8')

# Generated at 2022-06-13 16:37:56.623724
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # os.environ does not contain 'a'
    assert not('a' in environ)
    environ['a'] = 'b'
    assert 'b' == environ['a']
    assert 'b' in environ

    environ['a'] = u'b'
    asser

# Generated at 2022-06-13 16:38:00.539243
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # create a mutable mapping object
    instance = _TextEnviron()

    # get item
    key = 'TEST_VAR'
    value = 'some text'
    instance[key] = value
    assert instance[key] == value

# Generated at 2022-06-13 16:38:06.405199
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class Environ(dict):
        """Mock class for os.environ"""
        def __getitem__(self, key):
            if key == 'foo':
                return 'bar-ascii'
            elif key == 'baz':
                return 'qux-utf8'
            raise NotImplementedError
    environ = _TextEnviron(env=Environ())

    expected = 'test-ascii'
    result = environ['foo'] + '-ascii'
    assert expected == result

    expected = 'test-utf8'
    result = environ['baz'] + '-utf8'
    assert expected == result

# Generated at 2022-06-13 16:38:19.160547
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test exception throwing of __getitem__()
    #mock_os_environ = [None]
    #mock_os_environ[0] = _TextEnviron()
    mock_os_environ = environ
    try:
        mock_os_environ[None]
    except KeyError as e:
        assert str(e) == 'None'

    # Test return-value types of __getitem__()
    try:
        env_key = mock_os_environ['SHELL']
        assert isinstance(env_key, str)
    except KeyError:
        # SHELL environment variable is not guaranteed to be set
        pass

    # Test non-existent environment variable

# Generated at 2022-06-13 16:38:30.325328
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test _TextEnviron.__getitem__() method."""
    from os import environ

    #
    # Setup
    #
    #    This test requires that the environment be in a specific state.  In order to fix the
    #    environment for this test, the test will create a subprocess to run the tests in and
    #    change the environment in the subprocess before running the test.
    #

    # TODO: move this into a common setup fixture in the future
    # If we aren't on python3, then set up a subprocess with a clean environment to run the tests
    # in
    if not PY3:
        # First, create a function to start the subprocess and set up the environment
        def _run_test(env_dict):
            import subprocess


# Generated at 2022-06-13 16:38:37.691097
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Some test data to test different encodings
    # For all tests, assume that the default encoding is 'utf-8'
    #
    # Latin-1 encoded string
    latin1_bytes = b'\xc3\xbc'
    # utf-8 encoded version of Latin-1
    utf8_bytes = b'\xc3\xbc'
    # utf-8 encoded version of a surrogate pair representing Latin-1
    surrogate_utf8_bytes = b'\xed\xbc\x8c'

    # key is Latin-1, value is surrogate pair
    surrogate_pair_key_bytes = b'\xc3\xbc'
    surrogate_pair_value_bytes = b'\xed\x9c\x80'

    # key is Latin-1, value is Latin-1
    latin

# Generated at 2022-06-13 16:38:42.792499
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Ensure that it returns valid unicode strings
    assert isinstance(environ[to_bytes('HOME')], unicode)

    # Ensure that it has access to os.environ values.
    expected = os.path.expanduser('~')
    if os.name == 'nt':
        expected = to_text(expected)
    assert environ[to_bytes('HOME')] == expected

    # Ensure that values are cached if they're not utf-8
    def stub_environ(key, default=None):
        if key == to_bytes('FOO'):
            return u'\u221e'.encode('Windows-1252')
        return os.environ.get(key, default)
    u_max = u'\u221e'
    utf_max = u_max.encode('utf-8')

# Generated at 2022-06-13 16:38:49.173869
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({b'test1': b'test_value'}, encoding='latin-1')
    if PY3:
        assert test_environ[b'test1'] == b'test_value'
    else:
        assert test_environ[b'test1'] == u'test_value'

# Generated at 2022-06-13 16:38:58.560013
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = os.environ.copy()

# Generated at 2022-06-13 16:39:00.292834
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # call method
    environ.__getitem__('__ansible_test_environment_variable__')



# Generated at 2022-06-13 16:39:08.785274
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ["VAR1"] == "foo"
    assert environ["VAR2"] == "bar"
    assert environ["VAR3"] == "baz"
    assert environ["VAR4"] == "qux"
    assert environ["VAR5"] == "quux"
    assert environ["VAR6"] == "corge"
    assert environ["VAR7"] == "grault"
    assert environ["VAR8"] == "garply"
    assert environ["VAR9"] == "waldo"
    assert environ["VAR10"] == "fred"
    assert environ["VAR11"] == "plugh"
    assert environ["VAR12"] == "xyzzy"
    assert environ["VAR13"] == "Thud"


# Generated at 2022-06-13 16:39:11.840794
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        environ['test'] = 'value'
        assert environ['test'] == 'value'
    finally:
        del environ['test']

# Generated at 2022-06-13 16:39:17.516345
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up variables
    my_environ = _TextEnviron({b'key1': b'bytesvalue1', b'key2': u'unicodevalue2'})

    assert(my_environ[b'key1'] == u'bytesvalue1')
    assert(my_environ[u'key2'] == u'unicodevalue2')

# Generated at 2022-06-13 16:39:32.329693
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:42.565441
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class MockOsModule(object):
        def __init__(self):
            self.environ = {}
            self.environ.update({'ANSIBLE_STDOUT_CALLBACK': 'default', 'PATH': '/usr/bin:/bin:/usr/sbin', 'LANG': 'en_US.UTF-8', 'PWD': '/home/ansible', 'SHLVL': '1', 'HOME': '/root', 'LOGNAME': 'root', 'PYTHONPATH': '/usr/local/lib/python3.6/dist-packages:/usr/lib/python3/dist-packages', '_': '/usr/bin/python3'})
    class MockSysModule(object):
        def __init__(self):
            self.getfilesystemencoding = lambda : 'utf-8'

# Generated at 2022-06-13 16:39:49.106213
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for keys which should get decoded to text
    for envvar in ('LC_ALL', 'LANG', 'LANGUAGE', 'LC_CTYPE', 'LC_MESSAGES'):
        os.environ[envvar] = 'en_US.UTF-8'.encode('utf-8')
        assert isinstance(environ[envvar], str)



# Generated at 2022-06-13 16:39:54.689979
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron

    In Python2, this should return text strings instead of byte strings
    """
    test_environ = _TextEnviron()

    # Test getitem
    assert test_environ['PATH'] == test_environ._raw_environ['PATH']



# Generated at 2022-06-13 16:40:03.679296
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a new environ class with a small cache
    dict_environ = dict()
    # Test 1: Normal case
    dict_environ['B'] = 'B'
    dict_environ['Bb'] = 'Bb'
    dict_environ['C'] = 'C'
    dict_environ['Cc'] = 'Cc'
    dict_environ['D'] = 'D'
    dict_environ['Dd'] = 'Dd'
    dict_environ['EF'] = 'EF'
    dict_environ['EFg'] = 'EFg'
    dict_environ['H'] = 'H'
    dict_environ['Hh'] = 'Hh'
    dict_environ['I'] = 'I'
    dict_environ['Ii'] = 'Ii'
   

# Generated at 2022-06-13 16:40:11.971422
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    env = dict()
    env["ANSIBLE_ANSIBLE_NLP_EXAMPLES"] = "yes"
    env["ANSIBLE_ANSIBLE_NLP_KOREAN"] = "no"
    env["ANSIBLE_ANSIBLE_NLP_JAPANESE"] = "no"
    env["ANSIBLE_ANSIBLE_NLP_CHINESE"] = "no"
    env["ANSIBLE_ANSIBLE_NLP_FILENAME"] = "../../samples/sample_korean.txt"

# Generated at 2022-06-13 16:40:22.597958
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Unit test to validate _TextEnviron.__getitem__()
    #
    # Note that the assertion methods used in this module have been chosen to provide the lowest
    # maintenance cost while still providing a solid understanding of the module's state when
    # inspected.  This is done since this module is imported by all other Ansible modules and made
    # available in their globals() dictionary.
    #
    # The choice of assertion methods must therefore be limited to those modules which can be safely
    # imported in this environment.

    # Assert that the _TextEnviron object has the correct behaviour for an empty dictionary
    test_dictionary = _TextEnviron()
    assert len(test_dictionary) == 0
    assert not 'key' in test_dictionary
    assert not 'key' in test_dictionary

# Generated at 2022-06-13 16:40:27.482665
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    with open('test_environment.txt', 'r') as fd:
        environ_list = [line.rstrip().split('=', 1) for line in fd]

    for key, value in environ_list:
        assert environ[key] == value



# Generated at 2022-06-13 16:40:36.444880
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    encode_tests = [
        ('abcdefghijklmnopqrstuvwxyz', 'utf-8'),
        ('~¡!@#$%^&*()_+=-`}{[]|\\;\':",./<>?', 'utf-8'),
        (u"¡Hola! ¿Cómo estás? Привет!", 'utf-8'),
    ]

# Generated at 2022-06-13 16:40:43.492991
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:41:02.456526
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that string values are returned as text objects
    # First check that the value is returned using bytes on python2
    environ_py2 = _TextEnviron(env={'key': 'value'})
    assert isinstance(environ_py2['key'], str)
    # Now check that the value is returned using text on python3
    environ_py3 = _TextEnviron(env={'key': 'value'})
    assert isinstance(environ_py3['key'], str)

    # Check that surrogate-escaped values are returned as text objects
    # First check that the value is returned using bytes on python2
    environ_py2 = _TextEnviron(env={'key': b'\xed\xa0\x80'})
    assert isinstance(environ_py2['key'], str)
   

# Generated at 2022-06-13 16:41:06.523353
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # arrange
    environ = _TextEnviron()
    environ["TEST"] = "abc"
    # act
    ret = environ["TEST"]
    # assert
    assert(ret == "abc")



# Generated at 2022-06-13 16:41:12.402414
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test the method __getitem__ of class _TextEnviron"""
    if not PY3:
        raw_environ = {'test': 'garçon'}
        env = _TextEnviron(env=raw_environ, encoding='utf-8')
        assert env['test'] == 'garçon'
        assert env['test'] != 'gar\xe7on'

        raw_environ = {'test': 'garçon'.encode('ascii', 'surrogateescape')}
        env = _TextEnviron(env=raw_environ, encoding='ascii')
        assert env['test'] == 'gar\udce7on'
        assert env['test'] != 'gar\xe7on'


# Generated at 2022-06-13 16:41:18.704992
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert to_text(b'foo') == environ[b'foo']
    assert to_text(b'foo') == environ[u'foo']
    assert to_text(b'foo') != environ[b'bar']
    assert to_text(b'foo') != environ[u'bar']
    assert u'unicode\u00E9' == environ[u'unicode\u00E9']


# Generated at 2022-06-13 16:41:20.355406
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == os.path.expanduser('~')

# Generated at 2022-06-13 16:41:29.288604
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for value type on Python3 (bytes!)
    if PY3:
        dummy_env = _TextEnviron({b'FOO': b'foo'}, encoding='utf-8')
        value = dummy_env['FOO']
        assert isinstance(value, bytes)

    # Test for value type on Python2 (text!)
    if not PY3:
        dummy_env = _TextEnviron({'FOO': 'foo'}, encoding='utf-8')
        value = dummy_env['FOO']
        assert isinstance(value, str)

    # Test for value when b'\xc3\xbc'.encode('utf-8') == b'\xfc'
    # https://github.com/ansible/ansible-modules-core/issues/3254

# Generated at 2022-06-13 16:41:39.168244
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up test
    environ._raw_environ = {
        'my_name_is': b'\xeb\x8b\xa4\xec\x9d\x80',
        'my_name_is_not': b'\xed\x95\xb4\xec\x88\x98'
    }
    environ._value_cache = {
        b'my_name_is': u'\uc548\uc758',
        b'my_name_is_not': u'\ud3b4\uc8c4'
    }

    # Test and verify
    assert environ['my_name_is'] == u'\uc548\uc758'
    assert environ['my_name_is_not'] == u'\ud3b4\uc8c4'

#

# Generated at 2022-06-13 16:41:42.488561
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST'] = 'test'
    assert environ['TEST'] == 'test'

    # Test non-ascii characters
    environ['TEST'] = u'\N{SNOWMAN}'
    assert environ['TEST'] == u'\N{SNOWMAN}'



# Generated at 2022-06-13 16:41:55.284008
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    original_environ = environ._raw_environ
    environ._raw_environ = {'str': 'str_value',
                            'bytes': to_bytes('bytes_value', encoding='utf-8', nonstring='strict',
                                              errors='surrogate_or_strict'),
                            # This string contains an invalid character in the specified encoding
                            'bytes_invalid': to_bytes('bytes_invalid_value\x80',
                                                      encoding='utf-8', nonstring='strict',
                                                      errors='surrogate_or_strict'),
                            }

    # str value
    assert 'str_value' == environ['str']
    # bytes value

# Generated at 2022-06-13 16:41:56.876154
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == '/root'
    assert environ.get('USER') == 'root'


# Generated at 2022-06-13 16:42:26.096384
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest
    import tempfile
    # Patch os.environ to be empty and then set os.environ['path'] to be some binary junk
    os.environ = {}
    path = to_bytes('\xc2\xa7\xcc\x80', encoding='utf-16-be')
    os.environ['path'] = path

    # Test __getitem__ on empty environment
    # Path should only return the raw bytes
    t_env = _TextEnviron()
    assert t_env['path'] == path

    # Test __getitem__ on existing environment with errors set to 'surrogate_or_strict'
    # Path should decode to a unicode error
    t_env = _TextEnviron(encoding='utf-8')

# Generated at 2022-06-13 16:42:28.645709
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['FOO'] = b'BAR'
    assert environ['FOO'] == 'BAR'
    os.environ['BAR'] = 'BAZ'
    assert environ['BAR'] == 'BAZ'
    assert environ['QUX'] == ""

# Generated at 2022-06-13 16:42:36.769356
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        # This encoding is utf-8 but with \udc80 substituted for the byte 0x80.  If we don't handle
        # surrogates properly, this will cause a UnicodeDecodeError when we try to decode it.
        env_bytes = to_bytes(u'something=\udc80', encoding=None)
        enc_file = os.path.join(tempdir, 'enc')
        with open(enc_file, 'wb') as f:
            f.write(env_bytes)
        env_path = to_bytes(os.path.join(tempdir, 'env.sh'))

# Generated at 2022-06-13 16:42:47.352066
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make an object to test with
    env = _TextEnviron(env=os.environ, encoding='utf-8')
    # Use a known existing environment variable
    assert isinstance(env['PATH'], text_type)

    # Verify that the test function is actually testing things and not just assuming the code works
    assert 'PATH' in env
    env['PATH'] = b'The path to the treasure\xC2\xA0 is buried in the Python docs'
    assert 'PATH' in env
    assert env['PATH'] == u'The path to the treasure\xC2\xA0 is buried in the Python docs'
    del env['PATH']
    assert 'PATH' not in env
    assert len(env) == len(os.environ)

    # Check that it works just fine if we try to look up the path of the ans

# Generated at 2022-06-13 16:42:58.498189
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from ansible.module_utils.six import PY3

    test_data = (
        (b'a', b'b', 'a=b'),
        (b'a', u'c', 'a=c'),
    )

    for key, value, os_env in test_data:
        with patch.dict(b'os.environ', {key: value}, clear=True), \
            patch(b'ansible.module_utils.common._collections_compat.PY3', new=PY3), \
            patch(b'ansible.module_utils.common.sys.getfilesystemencoding', return_value=b'ascii'):
            env = _TextEnviron()
           

# Generated at 2022-06-13 16:43:01.908621
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['test_test__TextEnviron___getitem__'] = 'test_test__TextEnviron___getitem__'
    assert environ['test_test__TextEnviron___getitem__'] == 'test_test__TextEnviron___getitem__'


# Generated at 2022-06-13 16:43:10.333726
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({to_bytes(key, encoding='utf-8', nonstring='strict',
                                 errors='surrogate_or_strict'):
                         to_bytes(value, encoding='utf-8', nonstring='strict',
                                  errors='surrogate_or_strict')
                         for key, value in {'a': u'я', 'b': u'Ё', 'c': u'Ω', 'd': u'☺'}.items()})
    eq_(env['a'], u'я')
    eq_(env['b'], u'Ё')
    eq_(env['c'], u'Ω')
    eq_(env['d'], u'☺')



# Generated at 2022-06-13 16:43:13.112871
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({b'foo': b'bar'}, encoding='utf-8')
    assert test_environ['foo'] == 'bar'



# Generated at 2022-06-13 16:43:22.542526
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common.collections import MutableMapping
    from os import environ
    from sys import getfilesystemencoding

    assert isinstance(environ, MutableMapping)
    try:
        assert isinstance(environ[b'PATH'], str)
    except NameError:
        assert isinstance(environ['PATH'], str)

    new_environ = _TextEnviron(env=environ)
    assert isinstance(new_environ['PATH'], str)

    new_environ_utf8 = _TextEnviron(env=environ, encoding='utf-8')
    assert isinstance(new_environ_utf8['PATH'], str)

    new_environ_latin_1 = _TextEnviron(env=environ, encoding='latin-1')

# Generated at 2022-06-13 16:43:31.712376
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    # Set the environ so that it does not match the system encoding
    os.environ[b'py-b'] = u'test-b'.encode('latin1')
    os.environ[b'py-u'] = u'test-u'.encode('utf-8')

    # Test that we get strings back authenticated
    text_env = _TextEnviron(env=os.environ)
    assert isinstance(text_env[b'py-b'], unicode)
    assert text_env[b'py-b'] == u'test-b'
    assert isinstance(text_env[b'py-u'], unicode)
    assert text_env[b'py-u'] == u'test-u'

    # Test that we get strings back and the error mode is

# Generated at 2022-06-13 16:44:33.107882
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # We can't test any of the cache or decoding features when we're running on Python3
    if PY3:
        return

    testEnv = _TextEnviron({'TEST_BYTES': b'\xc3\xbfu\x00\x00\x00\x00\x00\x00',
                            'TEST_BYTES_UNDECODABLE': b'\xffu\x00\x00\x00\x00\x00\x00',
                            'TEST_TEXT': u'\xffu\x00'}, encoding='ascii')
    # test byte string values in environment
    assert testEnv['TEST_TEXT'] == u'\xffu\x00'

# Generated at 2022-06-13 16:44:38.708152
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron()
    assert text_environ['HOME'] == environ.get('HOME')
    # Test for regression for BZ#1697326 - 'HOME' is always converted to unicode
    # regardless of whether 'ascii' encoding is specified or not.
    text_environ = _TextEnviron(encoding='ascii')
    assert text_environ['HOME'] == environ.get('HOME')

# Generated at 2022-06-13 16:44:43.947936
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    class TestBase(unittest.TestCase):
        def setUp(self):
            self.env = {}
            for key, val in os.environ.items():
                if not isinstance(key, str):
                    continue
                if not isinstance(val, str):
                    continue
                self.env[key] = val

        def tearDown(self):
            for key in list(self.env.keys()):
                if key in os.environ:
                    del os.environ[key]
            for key, val in self.env.items():
                os.environ[key] = val

        def test_decode_environ_with_ascii_encoding(self):
            _TextEnviron(self.env, encoding='ascii')



# Generated at 2022-06-13 16:44:53.765885
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Save the original state of the environment
    original_environ = dict(environ)

    # Test the decoding of the environment
    environ['key'] = b'I am an encoded bytestring'
    assert environ['key'] == u'I am an encoded bytestring'

    # Test when the environment is missing
    assert environ.get('missing_key', u'default') == u'default'
    try:
        environ['missing_key']
    except KeyError:
        pass
    else:
        assert False, "Expected KeyError when calling __getitem__ on a key not in the environment"

    # Test when the environment is unicode
    environ['key'] = u'I am a unicode string'
    assert environ['key'] == u'I am a unicode string'

    # Cleanup

# Generated at 2022-06-13 16:45:03.366632
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import unittest

    class _TextEnviron_GetItem_TestCase(unittest.TestCase):
        def setUp(self):
            self.env = _TextEnviron(env={'foo': 'bar'})

        def tearDown(self):
            del self.env

        # Test for value encoded as utf-8
        def test_encoded_as_utf8(self):
            self.env['foo'] = '\xe2\x9a\x93'
            self.assertEqual(self.env['foo'], u'\u2693')

        # Test for value encoded as latin1

# Generated at 2022-06-13 16:45:12.231236
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Use a surrogate because it's a unicode character that can't be encoded with utf-8
    environ['TEST_UNICODE_VAR'] = u'\udc80'
    if PY3:
        assert environ['TEST_UNICODE_VAR'] == u'\udc80', 'Python 3 should not encode environment'
        # environs are immutable
        del environ['TEST_UNICODE_VAR']
    else:
        assert environ['TEST_UNICODE_VAR'] == u'\udc80', 'Python 2 should allow surrogate'
        # environs are immutable
        del environ['TEST_UNICODE_VAR']

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 16:45:22.072254
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common._collections_compat import MutableMapping

    # Test byte strings to text decoding
    _environ = _TextEnviron({b'a': b'foo', b'b': 'bar'.encode('utf-8')})
    assert isinstance(_environ, MutableMapping)
    for key, value in {'a': 'foo', 'b': 'bar'}.items():
        assert _environ[key] == value
        assert isinstance(_environ[key], str)

    # Test non-ascii Unicode strings
    _environ = _TextEnviron({'a': '\u2019', 'b': 'bar'})
    assert isinstance(_environ, MutableMapping)

# Generated at 2022-06-13 16:45:29.694770
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from io import StringIO

    environ = _TextEnviron()
    orig_env = os.environ.copy()


# Generated at 2022-06-13 16:45:37.905230
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # _TextEnviron.__getitem__(to_bytes('key', 'utf-8'))
    if PY3:
        # _TextEnviron.__getitem__(to_bytes('key', 'utf-8').decode(sys.getfilesystemencoding()))
        # _TextEnviron.__getitem__(os.environ[b'key'])
        assert environ[to_bytes('key', 'utf-8')] == os.environ[b'key']
    else:
        # _TextEnviron.__getitem__(to_bytes('key', 'utf-8').decode('utf-8', 'surrogate_or_strict'))
        if os.environ.get('key') is None:
            assert environ[to_bytes('key', 'utf-8')] is None

# Generated at 2022-06-13 16:45:39.551460
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Object under test
    env = _TextEnviron()
    # Test method
    assert None is env['__NONE__']