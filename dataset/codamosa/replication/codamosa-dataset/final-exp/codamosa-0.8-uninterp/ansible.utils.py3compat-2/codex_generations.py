

# Generated at 2022-06-13 16:35:58.133011
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # We've already confirmed this works (pylint complains we're redefining 'PY3' below):
    # pylint: disable=redefined-outer-name
    if PY3:
        # For Python3, we just want to verify that any os.environ value is returned as-is
        # instead of having to_text() try to decode it
        assert environ['PYTHONPATH'] == os.environ['PYTHONPATH']
    else:
        # For Python2 we want to see that we get a text version of the value
        #
        # PYTHONPATH is a unicode string in Python2, so let's not use that:
        assert environ['SHELL'] == u'/bin/bash'
        # Let's check something that's utf-8 and has non-ascii characters
        assert en

# Generated at 2022-06-13 16:36:05.445957
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import locale
    env = {
        'foo': 'bär',
        'bar': 'baz',
    }
    text_env = _TextEnviron(env=env)
    assert text_env['foo'] == u'bär'
    assert text_env['bar'] == u'baz'
    assert text_env['bad'] == u''
    env['foo'] = 'bär'.encode(locale.getpreferredencoding())
    env['bad'] = u'bäd'.encode(locale.getpreferredencoding())
    assert text_env['foo'] == u'bär'
    assert text_env['bad'] == u'bäd'

# Generated at 2022-06-13 16:36:07.662495
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ1 = _TextEnviron({'A': 'a'.encode('utf-8')})
    assert environ1['A'] == 'a'


# Generated at 2022-06-13 16:36:13.857611
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # env_var is a byte string
    dummy = 'dummy'
    env_var = b'key'
    env = {env_var: dummy}
    environ = _TextEnviron(env=env)

    # Test for different byte strings for key
    for key in (env_var, dummy):
        assert environ[key] is dummy

    # Test for text string for key
    assert environ[dummy] is dummy



# Generated at 2022-06-13 16:36:19.734465
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """ Test method __getitem__() of class _TextEnviron(). """
    environ = _TextEnviron(encoding='utf-8')
    # Test a key that we know exists.
    assert environ['PATH'] != u'\u0000'
    # Test a key that doesn't exist.
    assert environ['SHOULD_NOT_EXIST'] == u''

# Generated at 2022-06-13 16:36:23.457397
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['ANSIBLE_TEST'] = 'chars\xe8e'
    assert type(environ['ANSIBLE_TEST']) == unicode
    assert environ['ANSIBLE_TEST'] == u'chars\xe8e'
    assert environ['ANSIBLE_TEST'] == u'charsèe'

# Generated at 2022-06-13 16:36:33.102160
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ.clear()
    os.environ.update(test__TextEnviron___getitem__.test_values)
    del os.environ['test_ascii']

    os.environ.update({'test_bytes': to_bytes('test_text_bytes_with_UTF8_char_â', encoding='utf-8')})

    environ_test = _TextEnviron(encoding='utf-8')

    # testing with input being non-unicode
    assert environ_test['test_ascii'] == 'test_text_ascii'  # ascii be skipped
    if PY3:
        # python3 has all the variables encoded in unicode
        assert environ_test['test_bytes'] == 'test_text_bytes_with_UTF8_char_â'
        assert en

# Generated at 2022-06-13 16:36:39.223512
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    import os
    os.environ['FOO'] = 'bar'
    os.environ['FOO'] = 'bar'
    assert environ['FOO'] == 'bar'
    assert environ['FOO'] == 'bar'

# Generated at 2022-06-13 16:36:47.806799
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-locals
    import locale
    import unittest

    from ansible.module_utils.common.text.converters import to_bytes


# Generated at 2022-06-13 16:36:54.870715
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    var_name = b'TEST_VARIABLE_007'
    value = b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d'
    try:
        os.environ[var_name] = value
    except UnicodeDecodeError:
        # This is an invalid value.  Skip this test
        return

    assert environ[var_name] == value.decode('utf-8')
    del os.environ[var_name]


# Generated at 2022-06-13 16:36:58.421818
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['ansible_python_interpreter'] == sys.executable



# Generated at 2022-06-13 16:37:07.797728
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check if it's a MutableMapping
    assert issubclass(_TextEnviron, MutableMapping)

    # Check if env is being passed correctly to __init__
    class Test(object):
        def __getitem__(self, key):
            return "Success"
    test = _TextEnviron(env=Test())
    assert test["test"] == "Success"

    # Check the encoding parameter
    try:
        test = _TextEnviron(encoding="1234")
    except LookupError:
        pass
    else:
        assert False, "Invalid value of encoding should raise a LookupError"

    # Check if __getitem__ is returning a text string

# Generated at 2022-06-13 16:37:09.552963
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({b'foo': 'bar'})
    assert e['foo'] == 'bar'

# Generated at 2022-06-13 16:37:17.823697
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test different types of variables
    text_variable = 'Ansible_Text_Variable'
    byte_variable = 'Ansible_Byte_Variable'
    unicode_variable = 'Ansible_Unicode_Variable'

    environ[text_variable] = 'text'
    environ[byte_variable] = b'byte'
    environ[unicode_variable] = u'unicode'

    # Test corner case for caching
    old_tv = environ[text_variable]
    environ[text_variable] = 'new text'
    assert old_tv != environ[text_variable]

    # Test that all variables are decoded
    assert isinstance(environ[text_variable], text)
    assert isinstance(environ[byte_variable], text)

# Generated at 2022-06-13 16:37:26.290846
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_text, to_bytes

    class mock_environ(object):
        def __init__(self):
            self.mock_environ = {}

        def __getitem__(self, key):
            return self.mock_environ[key]

        def __setitem__(self, key, value):
            self.mock_environ[key] = value

        def __delitem__(self, key):
            del self.mock_environ[key]

        def __iter__(self):
            return iter(self.mock_environ)

        def __len__(self):
            return len(self.mock_environ)

    mock_env = mock_environ()

# Generated at 2022-06-13 16:37:29.929233
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'FOO': b'bar'}, encoding='utf-8')
    assert environ[b'FOO'] == u'bar'


# Generated at 2022-06-13 16:37:40.781266
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def check_return_types(env, env_is_getitem=True):
        for key, value in env.items():
            # Test bytes/text return for keys
            if key == 'PATH':
                key = u'PATH'  # OS X does weird things with the PATH key
            assert isinstance(key, str), 'Key %s must be a string: %s' % (key, type(key))

            # Test bytes/text return for values
            assert isinstance(value, str), 'Value for key %s is not a string, it is "%s": %s' % (key, value, type(value))

            # Test that all values are different

# Generated at 2022-06-13 16:37:49.301940
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest
    if not PY3:
        pytest.skip("Test only applies to Python3")

    # Unicode characters in the environment
    assert environ[to_text('\u00E9')] == '\u00E9'

    # Byte value in the environment
    assert environ[to_text('badger')] == '\u00E9'

    # Byte value for key, unicode value for item
    assert environ[to_bytes('badger')] == '\u00E9'

# Generated at 2022-06-13 16:38:01.037820
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Basic tests for _TextEnviron.__getitem__
    # We need to create a raw _TextEnviron because the singleton environ might not be what we expect.
    environ = _TextEnviron()
    assert environ['PATH'] == os.environ['PATH']
    os.environ['PATH'] = 'sme\xf8k^X'
    assert environ['PATH'] == os.environ['PATH']

    # Test non ascii values
    # FIXME: We can't reliably test this until we have a way to change the environ to get different
    # byte encodings
    #os.environ['PATH'] = '\xc3'
    #assert environ['PATH'] == u'\ufffd'

    # Test unicode values

# Generated at 2022-06-13 16:38:08.144334
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:38:19.216704
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    environ = _TextEnviron(encoding='utf-8')
    def _fake_environ(key):
        if key == 'USERNAME':
            return 'user'.encode('utf-8')
        elif key == 'PASSWORD':
            return 'pw'.encode('utf-8')

    # Test when key is str
    if sys.version_info[0] >= 3:
        environ._raw_environ = _fake_environ
        assert environ.__getitem__('USERNAME') == 'user'
        assert environ.__getitem__('PASSWORD') == 'pw'
    else:
        environ._raw_environ = _fake_environ
        assert environ.__getitem

# Generated at 2022-06-13 16:38:30.369363
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with default value of the argument 'encoding'.
    env = _TextEnviron()

    # Test without caching.
    env['test_key'] = b'test_value'
    value = env['test_key']
    assert value == 'test_value'

    # Test with caching.
    value = env['test_key']
    assert value == 'test_value'

    # Test with argument 'encoding'.
    env = _TextEnviron(encoding='cp1251')

    # Test without caching.
    env['test_key'] = b'test_value'
    value = env['test_key']
    assert value == 'test_value'

    # Test with caching.
    value = env['test_key']
    assert value == 'test_value'



# Generated at 2022-06-13 16:38:32.688857
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _environ = _TextEnviron()
    key = 'PATH'
    assert not isinstance(_environ[key], bytes)
    assert isinstance(_environ[key], str)


# Generated at 2022-06-13 16:38:34.098800
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['environment variable name'] = 'environment variable value'
    assert environ['environment variable name'] == 'environment variable value'

# Generated at 2022-06-13 16:38:40.194110
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The method __getitem__ of _TextEnviron depends on the object os.environ,
    # the object os.environ is shared by all the other modules, therefore,
    # we can't use the object environ created in the top of this module (by
    # default, it uses os.environ, which is not suitable for testing, because
    # it is a global variable).

    # For unit testing, we need to use a different object of type MutableMapping
    # for environ.  The two ways to do that are:
    #   1) Use the parameter "environ" of the constructor
    #   2) Use the method setitem of the object which already exists

    # Tests with parameter "environ" of the constructor
    # --------------------------------------------------

    # Test case: normal case
    environ_testing_case_1 = _Text

# Generated at 2022-06-13 16:38:48.744010
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {'foo': b'bar', 'baz': b'qux'}
    assert environ['foo'] == 'bar'
    assert environ['baz'] == 'qux'
    assert environ['foo'] == 'bar'
    assert environ['baz'] == 'qux'
    assert 'foo' in environ and 'baz' in environ
    assert environ.encoding == 'utf-8'
    assert len(environ) == 2

    # Modify value and ensure that still works
    environ['foo'] = 'foo'
    assert environ['foo'] == 'foo'
    assert environ['baz'] == 'qux'

    # Delete value and ensure that still works
    del environ['baz']
    assert environ['foo'] == 'foo'

# Generated at 2022-06-13 16:38:58.372185
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest

    class __TextEnviron___getitem__TestCase(unittest.TestCase):
        def setUp(self):
            class FakeEnv(dict):
                def __getitem__(self, key):
                    return '自動インストール' if key == 'LANG' else dict.__getitem__(self, key)

            self.env = FakeEnv()

# Generated at 2022-06-13 16:39:03.086918
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a mapping of text keys to raw bytes as would be found in os.environ
    raw_environ = {u'empty': b'', u'empty_ascii': b'', u'empty_utf8': b''}
    raw_environ[u'ascii_text'] = u'ascii'.encode(to_text(sys.getfilesystemencoding(), errors='surrogate_or_strict'))
    raw_environ[u'latin1_text'] = u'latin1'.encode('latin-1')
    raw_environ[u'utf8_text'] = u'utf8'.encode('utf-8')

# Generated at 2022-06-13 16:39:14.289615
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pre-condition: encodings in the environment are encoded in ASCII
    assert('ANSIBLE_TEST_UFT8' in os.environ)
    assert(isinstance(os.environ['ANSIBLE_TEST_UFT8'], bytes))
    assert(os.environ['ANSIBLE_TEST_UFT8'].decode('ascii') == 'TEST_UFT8')

    assert('ANSIBLE_TEST_NONASCII' in os.environ)
    assert(isinstance(os.environ['ANSIBLE_TEST_NONASCII'], bytes))
    assert(os.environ['ANSIBLE_TEST_NONASCII'].decode('utf-8') == u'TEST_NONASCII')

    # test: getitem of _TextEnviron with no argument


# Generated at 2022-06-13 16:39:22.378231
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:29.102780
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import json
    needed_vars = ['HOST', 'ARGS']
    environ_vars = [(key, environ[key]) for key in needed_vars]

    with open('/tmp/env.json', 'w') as f:
        f.write(json.dumps(environ_vars, indent=2))



# Generated at 2022-06-13 16:39:37.094028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _TestEnv(MutableMapping):
        def __init__(self, arg):
            self._arg = arg
        def __getitem__(self, key):
            return self._arg
        def __setitem__(self, key, value):
            pass
        def __delitem__(self, key):
            pass
        def __iter__(self):
            pass
        def __len__(self):
            pass
    encodings = ['utf-8', 'latin-1', 'gb2312']

    # Test with valid ASCII string
    text = 'this is a test string'
    expected_text = text
    for encoding in encodings:
        e = _TestEnv(to_bytes(text, encoding=encoding))
        env = _TextEnviron(env=e, encoding=encoding)

# Generated at 2022-06-13 16:39:45.586696
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ[to_bytes('foo')] = to_bytes('bar')
    assert environ['foo'] == 'bar'
    # Check the cache gets the correct value
    os.environ[to_bytes('foo')] == to_bytes('baz')
    assert environ['foo'] == 'bar'
    # But direct access to the raw environ sees the new value
    assert environ._raw_environ['foo'] == to_bytes('baz')
    # Make sure we can get unicode values
    os.environ[to_bytes('unicode_value_foo')] = to_bytes('\xe2\x92\xac')
    assert environ['unicode_value_foo'] == u'\u20ac'
    # Make sure we can get bytes values

# Generated at 2022-06-13 16:39:52.065067
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Tests str input
    s = '%s=%s' % ('key', 'str_val')
    environ[s] = s
    assert environ['key'] == 'str_val'

    # Tests unicode input
    s = '%s=%s' % ('key', u'unicode_val')
    environ[s] = s
    assert environ['key'] == u'unicode_val'


# Generated at 2022-06-13 16:40:01.488807
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # set up test state
    environ["a"] = to_bytes('é')
    environ["b"] = to_bytes('â')
    environ._raw_environ["c"] = to_bytes('é')
    environ._raw_environ["d"] = to_bytes('â')

    # set up expected result
    expected = 'é'
    #assert actual == expected
    if not (actual == expected):
        raise AssertionError('expected:<%(expected)s> actual:<%(actual)s>' % locals())

    # set up expected result
    expected = 'â'
    #assert actual == expected
    if not (actual == expected):
        raise AssertionError('expected:<%(expected)s> actual:<%(actual)s>' % locals())

    # set up expected result

# Generated at 2022-06-13 16:40:07.763763
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(env = {'ascii': 'ASCII',
                                  'utf8': 'UTF-8',
                                  'nonascii': '\xe2\x99\xa5'})

    assert environ['ascii'] == 'ASCII'
    assert environ['utf8'] == 'UTF-8'
    assert environ['nonascii'] == u'\u2665'


# Generated at 2022-06-13 16:40:19.499912
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    old_environ = os.environ.copy()
    os.environ.clear()

# Generated at 2022-06-13 16:40:29.323636
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make sure the class functions correctly given the correct inputs
    env = {to_bytes(u'PATH'): to_bytes(u'/usr/bin:/bin'),
           u'TEST': u'おはよう',
           u'TEST2': u'✓',
           to_bytes(u'TEST3'): u'✓',
           }
    e = _TextEnviron(env=env)
    assert u'/usr/bin:/bin' == e[u'PATH']
    assert u'おはよう' == e[u'TEST']
    assert u'✓' == e[u'TEST2']
    assert u'✓' == e[u'TEST3']

    # Make sure that decoding errors bubble up appropriately

# Generated at 2022-06-13 16:40:40.421913
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os_environ_fake = {b'PATH': b'/bin:/usr/bin:/usr/local/bin',
                       b'OO_CLI_PATH': b'/bin:/usr/bin:/usr/local/bin',
                       b'TEST_ENV_WITHOUT_PYTHON': b'Hello',
                       b'TEST_ENV_WITH_PYTHON': b'{"name":"Ram","address":"Pune"}'}
    test = _TextEnviron(env=os_environ_fake, encoding='utf-8')
    assert test[b'PATH'] == '\u05dc\u05e0\u05e1\u05e2\u05e3'

# Generated at 2022-06-13 16:40:44.200119
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    os.environ['ANSIBLE_TEST'] = 'foobar'
    os.environ['ANSIBLE_TEST_BYTES'] = b'\x80'
    assert environ['ANSIBLE_TEST'] == u'foobar'
    assert environ['ANSIBLE_TEST_BYTES'] == u'\x80'
    del os.environ['ANSIBLE_TEST']
    del os.environ['ANSIBLE_TEST_BYTES']


# Generated at 2022-06-13 16:40:54.634670
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that environment variables containing UTF-8 are decoded
    u_env = _TextEnviron({b'ANSIBLE_TEST_VAR': to_bytes(u'\N{SNOWMAN}')})
    assert u_env[b'ANSIBLE_TEST_VAR'] == u'\N{SNOWMAN}'
    # Test that environment variables containing invalid UTF-8 are decoded as surrogates
    invalid_env = _TextEnviron({'ANSIBLE_TEST_VAR': b'\xc3\x28'})
    assert invalid_env[b'ANSIBLE_TEST_VAR'] == u'\ufffd('


# Generated at 2022-06-13 16:41:03.408418
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    class TestClass__TextEnviron(unittest.TestCase):
        def setUp(self):
            # Handle PY2 and 3 in the test suite
            self.environ = _TextEnviron(env={'byte_string_1': b'foo', 'text_string_1': u'bar'})
            self.environ_bytes = _TextEnviron(env={'byte_string_1': b'foo', 'text_string_1': u'bar'}, encoding='utf-8')

        def test__getitem__byte_string(self):
            if PY3:
                # Under Python3, byte strings are passed through unchanged
                self.assertEqual(self.environ['byte_string_1'], b'foo')

# Generated at 2022-06-13 16:41:14.613199
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    # decode error
    # Cannot decode bytes in position 1-2: truncated \xXX escape
    env._raw_environ['ANSIBLE_TEST_1'] = '\xff'
    try:
        assert env['ANSIBLE_TEST_1'] is None
    except UnicodeDecodeError:
        pass
    # surrogateescape error
    env._raw_environ['ANSIBLE_TEST_2'] = '\xe8\xbf\xbf'
    try:
        assert env['ANSIBLE_TEST_2'] is None
    except UnicodeDecodeError:
        pass
    # nonstring 'passthru'
    env._raw_environ['ANSIBLE_TEST_3'] = b'\xe8\xbf\xbf'

# Generated at 2022-06-13 16:41:18.824332
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    actual = environ['PATH']
    expected = os.environ['PATH']
    assert actual == expected, \
        '''  actual: {!r}
    expected: {!r}'''.format(actual, expected)


# Generated at 2022-06-13 16:41:28.401741
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    This function tests the method __getitem__ of class _TextEnviron.
    '''

    # Test data
    environ_None = None
    environ_Foo = {
        'BAR': 'baz',
        'BAR2': b'baz',
        'BAR3': 'baz\xe9',
        'BAR4': to_bytes('baz\xe9', encoding='utf-8', nonstring='strict', errors='surrogate_or_strict')
    }

    environ_utf = _TextEnviron(environ_Foo, encoding='utf-8')
    assert environ_utf['BAR'] == 'baz'
    assert environ_utf['BAR2'] == 'baz'

# Generated at 2022-06-13 16:41:32.877348
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {u'ANSIBLE_ROLES_PATH': b'/foo/bar'}
    te = _TextEnviron(env, encoding='utf-8')
    assert te['ANSIBLE_ROLES_PATH'] == u'/foo/bar'


# Generated at 2022-06-13 16:41:40.908750
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for PY3
    class _os:
        environ = {}
        @staticmethod
        def getfilesystemencoding():
            return 'utf-8'
    _sys = sys
    _sys.getfilesystemencoding = _os.getfilesystemencoding
    sys = _sys
    os = _os
    environ = _TextEnviron(env=os.environ, encoding=os.getfilesystemencoding())
    environ['key'] = 'value'
    assert environ['key'] == 'value'
    assert environ._value_cache == {}

    # Test for not PY3
    class _os:
        environ = {}
        @staticmethod
        def getfilesystemencoding():
            return 'utf-8'
    _sys = sys

# Generated at 2022-06-13 16:41:44.217734
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(env={"a": "b", "b": "Ã±"}, encoding='utf-8')
    res = environ["a"]
    assert isinstance(res, str)
    assert "b" == res
    res = environ["b"]
    assert isinstance(res, str)
    assert "Ã±" == res

# Generated at 2022-06-13 16:41:54.516327
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import unittest
    from ansible.module_utils._text import to_bytes, to_text

    not_valid_utf8 = b'\xa0'
    valid_utf8 = b'\xc2\xa0'

    class Tests(unittest.TestCase):

        def test_not_valid_utf8(self):

            os.environ.clear()
            os.environ.update({b'not_utf8': not_valid_utf8})
            environ = _TextEnviron(encoding='utf-8')
            value = environ[b'not_utf8']
            self.asser

# Generated at 2022-06-13 16:42:00.293418
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ.clear()
    environ._raw_environ['KEY1'] = b'hello'
    environ._raw_environ['KEY2'] = b'\xc2\xa1hello'

    # All values are native python text in Python3
    if PY3:
        assert environ['KEY1'] == 'hello'
        assert environ['KEY2'] == '¡hello'
    else:
        assert environ['KEY1'] == u'hello'
        assert environ['KEY2'] == u'¡hello'
        # Make sure that the encoding is cached in Python2
        assert environ._value_cache[b'\xc2\xa1hello'] == u'¡hello'

    # Verify that the cached values get returned again
    assert environ['KEY1'] == 'hello'


# Generated at 2022-06-13 16:42:18.636464
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unicode code point U+200B (Zero Width Space) in UTF-8 encoding
    # Note: When viewing this as UTF-8 in a text editor, it will appear to be an empty string
    # This is an example of a 'non-character' in Unicode.  It has a defined meaning but is not
    # designed for use in text.
    # https://stackoverflow.com/questions/24387778/what-is-a-noncharacter-in-unicode/24390323#24390323
    emtpy_variable_name = b'\xe2\x80\x8b'

    # Unicode code point U+200B (Zero Width Space) in UTF-8 encoding
    # Note: When viewing this as UTF-8 in a text editor, it will appear to be an empty string
    # This is an example of a '

# Generated at 2022-06-13 16:42:27.218945
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['BYTES_VALUE'] = to_text('\xa5', 'ascii', errors='surrogate_or_strict')
    os.environ['TEXT_VALUE'] = to_text('\u00a5', encoding='ascii', errors='surrogate_or_strict')

    my_environ = _TextEnviron(encoding='ascii')

    assert my_environ['BYTES_VALUE'] == to_text('\xa5', 'ascii', errors='surrogate_or_strict')
    assert my_environ['TEXT_VALUE'] == to_text('\u00a5', encoding='ascii', errors='surrogate_or_strict')

    del os.environ['BYTES_VALUE']

# Generated at 2022-06-13 16:42:35.784283
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    cache = environ._value_cache

    # Initial state
    assert len(cache) == 0

    # Getting a value for the first time should decode it correctly
    assert environ[b'ANSIBLE_MODULE_ARGS'] == u'\u00e5'

    # Getting a value for the second time should return the cached value
    assert environ[b'ANSIBLE_MODULE_ARGS'] == u'\u00e5'
    assert len(cache) == 1

    # Changing the value should cause the cache to be cleared
    environ[b'ANSIBLE_MODULE_ARGS'] = b'\xc3\xb8'
    assert environ[b'ANSIBLE_MODULE_ARGS'] == u'\u00f8'
    assert len(cache) == 1

# Generated at 2022-06-13 16:42:40.744790
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method _TextEnviron.__getitem__
    '''
    # Known Latin 1 Byte String
    assert environ[to_bytes('EnvVar', 'utf-8')] == to_text('Test String', 'utf-8')
    # Known Unicode String
    assert environ[to_bytes('Home', 'utf-8')] == to_text(u'C:\\Users\\Test', 'utf-8')
    # Non-byte-sting (should pass through)
    assert environ[to_bytes('PATH', 'utf-8')] == '/bin:/usr/bin'
    # Known Key with bad encoding (should fail)

# Generated at 2022-06-13 16:42:48.531688
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test Unicode
    environ['test1'] = u'Unicode'
    assert environ['test1'] == u'Unicode'

    # Test text
    environ['test2'] = to_text('text', encoding='utf-8')
    assert environ['test2'] == to_text('text', encoding='utf-8')

    # Test bytes
    environ['test3'] = to_bytes('bytes', encoding='utf-8')
    assert environ['test3'] == to_text('bytes', encoding='utf-8')



# Generated at 2022-06-13 16:42:53.109137
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if not PY3:
        assert environ['PATH'] == to_text(os.environ['PATH'], encoding='utf-8', nonstring='passthru',
                                          errors='surrogate_or_strict')


# Generated at 2022-06-13 16:42:54.846258
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Assert valid test
    assert environ["LANG"] == u'C.UTF-8'


# Generated at 2022-06-13 16:43:05.777415
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Value is undecoded unicode
    environ[u'test_key'] = u'\u5317\u4eb0'
    assert environ[u'test_key'] == u'\u5317\u4eb0'
    assert isinstance(environ[u'test_key'], unicode)

    # Value is already unicode
    environ[u'test_key2'] = u'\u8056\u5229\u65af'
    assert environ[u'test_key2'] == u'\u8056\u5229\u65af'

    # Using the raw environment should return byte strings
    assert isinstance(environ._raw_environ[u'test_key'], bytes)

# Generated at 2022-06-13 16:43:07.619980
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_ = _TextEnviron({'FOO': 'bar'})
    assert environ_['FOO'] == 'bar'

# Generated at 2022-06-13 16:43:11.954501
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['CUSTOMER_NAME'] == 'John Doe'
    assert environ['CUSTOMER_SURNAME'] == u'Rambo'
    assert environ['CUSTOMER_NUMBER'] == u'007'


# Generated at 2022-06-13 16:43:31.754375
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    env['THIS'] = u'That'
    assert env['THIS'] == 'That'



# Generated at 2022-06-13 16:43:37.101384
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_tuple = (('TRUE', 'True'), ('FALSE', 'False'), ('NULL', ''))
    environ_dict = dict(environ_tuple)
    environ = _TextEnviron(environ_dict)

    assert environ['TRUE'] == 'True'
    assert environ['FALSE'] == 'False'
    assert environ['NULL'] == ''



# Generated at 2022-06-13 16:43:44.041448
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron({b'foo': b'bar'}, encoding='utf-8')
    assert 'bar' == test_env['foo']

    test_env = _TextEnviron({u'foo': u'bar'}, encoding='utf-8')
    assert 'bar' == test_env['foo']

    test_env = _TextEnviron({'foo': 'bar'}, encoding='utf-8')
    assert 'bar' == test_env['foo']


# Generated at 2022-06-13 16:43:50.683934
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that __getitem__ doesn't decode environment variables that haven't been decoded yet
    # pylint: disable=protected-access
    # pylint: disable=redefined-outer-name
    import os
    import sys
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.six import PY3

    cls_attributes = {'_raw_environ': {}, '_value_cache': {}, 'encoding': 'utf-8'}

# Generated at 2022-06-13 16:43:57.219045
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # environ is a global variable which is always available at this point in a run.
    assert isinstance(environ, _TextEnviron)
    assert len(environ) > 0
    # Everything we've been able to test so far tells us that PY3 is correct
    assert environ._raw_environ == os.environ
    # So we're going to cheat a little here to ensure that all the necessary attributes are set
    environ._value_cache = {}
    environ.encoding = 'utf-8'

    # Key is a text string
    assert environ.get('SHELL') == os.environ.get('SHELL')

    # Key is a byte string
    assert environ.get(b'SHELL') == os.environ.get(b'SHELL')

    # Undecoded byte string
    undecoded

# Generated at 2022-06-13 16:44:00.125133
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {b'k': b'v'}
    t_env = _TextEnviron(env=env)
    assert t_env['k'] == 'v'


# Generated at 2022-06-13 16:44:09.405522
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if not PY3:
        assert 'utf-8' != environ.encoding
        environ['test-unicode'] = 'Iñtërnâtiônàlizætiøn'
        # Verify that we return unicode strings instead of bytes objects
        value = environ['test-unicode']
        assert isinstance(value, str)
        assert value == 'Iñtërnâtiônàlizætiøn'
        # Verify that we can return keys that have been set in the middle of a run
        assert environ['test-key'] == 'test-value'

# Generated at 2022-06-13 16:44:18.678612
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:44:20.246519
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PWD'] == u'/home/a.badger/src/python3-ansible'

# Generated at 2022-06-13 16:44:32.772582
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Testing "normal" values
    bytes_string = b"foo"
    text_string = u"foo"
    utf8_bytes = b'\xF0\x9F\x92\xA9'
    utf8_text = u'\U0001F4A9'
    cp1252_bytes = b'\x99'
    cp1252_text = u'\u0099'
    test = _TextEnviron({u'foo': bytes_string})
    assert isinstance(test[u'foo'], text_string.__class__)
    assert test[u'foo'] == text_string
    test = _TextEnviron({bytes_string: text_string})
    assert isinstance(test[bytes_string], text_string.__class__)
    assert test[bytes_string] == text

# Generated at 2022-06-13 16:45:07.082645
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    environ['name'] = 'value'
    assert environ['name'] == 'value'



# Generated at 2022-06-13 16:45:11.215884
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({'hello': b'world', 'other': u'universe', 'int': 1, 'empty': None})
    assert 'world' == env['hello']
    assert u'universe' == env['other']
    assert u'1' == env['int']
    assert u'None' == env['empty']



# Generated at 2022-06-13 16:45:14.888409
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(env={b'ANSIBLE_MODULE_ARGS': b'{}'})
    assert env[b'ANSIBLE_MODULE_ARGS'] == u'{}'
    assert env['ANSIBLE_MODULE_ARGS'] == u'{}'


# Generated at 2022-06-13 16:45:24.291279
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # pylint: disable=protected-access
    environ = _TextEnviron()
    # unicode should be returned when the environment variable is unicode
    environ._raw_environ[u'foo'] = u'bar'
    assert(isinstance(environ[u'foo'], str))
    assert(environ._raw_environ[u'foo'] == u'bar')
    assert(environ[u'foo'] == u'bar')
    # str should be returned when the environment variable is str
    environ._raw_environ[u'foo'] = u'bar'
    assert(isinstance(environ['foo'], str))
    assert(environ._raw_environ['foo'] == u'bar')
    assert(environ['foo'] == u'bar')



# Generated at 2022-06-13 16:45:30.417106
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(encoding='latin-1')
    assert test_environ._raw_environ == os.environ
    test_environ._raw_environ['val1'] = '\xa9'
    test_environ._raw_environ['val2'] = 'value'
    assert test_environ['val1'] == '\xa9'
    assert test_environ['val2'] == 'value'


# Generated at 2022-06-13 16:45:36.666547
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Create our own dict
    my_dict = {}
    my_dict[b'foo'] = 'bar'

    # Create a TextEnviron
    my_text_environ = _TextEnviron(env=my_dict, encoding='utf-8')

    # Test with a valid key and encoding
    assert my_text_environ['foo'] == 'bar'

    # Test with a valid key and encoding == None
    my_text_environ = _TextEnviron(env=my_dict, encoding=None)

    # Test with a valid key and encoding
    assert my_text_environ['foo'] == 'bar'

# Generated at 2022-06-13 16:45:43.739152
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create a mock environment variable
    environ['TEST_ENCODE_VARIABLE'] = b'foo'

    # Call __getitem__ with and without a cached value
    assert environ.__getitem__('TEST_ENCODE_VARIABLE') == 'foo'
    assert environ['TEST_ENCODE_VARIABLE'] == 'foo'

    # Call __getitem__ on a value which has already been cached
    assert environ['TEST_ENCODE_VARIABLE'] == 'foo'

    # Call __getitem__ on a value which is not present in the environment
    with pytest.raises(KeyError):
        assert environ.__getitem__('TEST_ENCODE_VARIABLE_NOT_SET')

# Generated at 2022-06-13 16:45:47.876754
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = {'foo': b'bar',
                'baz': 'baz'}
    environ = _TextEnviron(test_env)
    assert environ['foo'] == 'bar'
    assert environ['baz'] == 'baz'

