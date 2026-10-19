

# Generated at 2022-06-13 16:35:58.512511
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # text returned when decoding as utf-8 is the same as what's in the environment
    assert environ['LANG'] == 'en_US.UTF-8'
    assert environ['HOME'] == '/root'
    assert environ['TZ'] == 'Asia/Kolkata'
    assert environ['LC_TIME'] == 'en_US.utf8'
    assert environ['G_BROKEN_FILENAMES'] == '1'
    assert environ['PATH'] == '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin'


# Generated at 2022-06-13 16:36:06.456142
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Tests for normal usage
    assert environ['HOME'] == u'/home/user'
    assert environ['HOME'] == u'/home/user'

    # Tests for multiple non-ASCII characters
    assert environ['PYTHONIOENCODING'] == u'UTF-8'

    # Test for non-ASCII with surrogates and strict mode
    environ['KEY'] = u'\uD800\uDF00'
    try:
        # Under python2 this is a surrogateescape error and will always fail.  Under python3,
        # the surrogateescape error is not raised because the surrogates were invalid when this
        # module was imported and the exception is converted into a surrogate_or_strict error
        assert False
    except UnicodeEncodeError as e:
        assert u'surrogate' in to_text(e)

# Generated at 2022-06-13 16:36:16.802284
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Existing variables that are text strings
    assert environ['PATH'] == environ._raw_environ['PATH']
    assert environ[u'PATH'] == environ._raw_environ[u'PATH']
    assert environ['PATH'] == environ._value_cache[environ._raw_environ['PATH']]

    environ[u'ANSIBLE_TEST'] = b'foo \xc3\xa9\xc3\xa9'
    if PY3:
        assert environ[u'ANSIBLE_TEST'] == environ._raw_environ['ANSIBLE_TEST']
        assert environ[u'ANSIBLE_TEST'] == environ._raw_environ['ANSIBLE_TEST'].decode('utf-8')
        assert environ[u'ANSIBLE_TEST'] == environ._

# Generated at 2022-06-13 16:36:21.056197
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os


# Generated at 2022-06-13 16:36:32.190904
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    is_class = True
    environ = _TextEnviron(encoding='utf-8')
    # Normal value
    os.environ['a'] = '1'
    if environ['a'] == '1':
        return True
    del os.environ['a']

    # Bytearray value
    os.environ['a'] = b'2'
    if environ['a'] == '2':
        return True
    del os.environ['a']

    # Unicode value
    os.environ['a'] = '3'
    if environ['a'] == u'3':
        return True
    del os.environ['a']

    # Unicode value bytearray
    os.environ['a'] = u'4'.encode('utf-8')

# Generated at 2022-06-13 16:36:38.904017
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The purpose of this test is to reproduce the difference between Python 2.7 and Python 3.7.
    # Python 2.7 returns a string for os.environ['HOME'], which is bytes on a POSIX system.
    # Python 3.7 returns a string for os.environ['HOME'], which is str on a POSIX system.
    # So, when we run this test, it will fail on Python 2.7.
    # But, this test is only supporsed to run on Python 2.7, so the reason for the failure is
    # expected and it's not a bug.
    expected_type = str if PY3 else bytes
    assert isinstance(environ['HOME'], expected_type)

# Generated at 2022-06-13 16:36:49.566181
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text

    # Create a new class so that the tests won't impact the real environ
    class _TextEnviron(MutableMapping):
        def __init__(self, env=None, encoding='utf-8'):
            if env is None:
                env = os.environ
            self._raw_environ = env
            self._value_cache = {}
            self.encoding = encoding
        def __delitem__(self, key):
            del self._raw_environ[key]
        def __getitem__(self, key):
            value = self._raw_environ[key]
           

# Generated at 2022-06-13 16:36:58.215390
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # env variable which is already unicode
    assert u'foo' == environ['PYTHONPATH']

    # env variable which must be encoded
    assert to_text('foo') == environ[to_bytes('PYTHONPATH', encoding=environ.encoding,
                                              nonstring='strict', errors='surrogate_or_strict')]

    # utf-8 env variable
    assert to_text('foo', encoding='utf-8') == environ[to_bytes('PYTHONPATH', encoding=environ.encoding,
                                                                nonstring='strict', errors='surrogate_or_strict')]

    # iso-8859-1 env variable

# Generated at 2022-06-13 16:37:07.659372
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PYTHONPATH'] == environ['PYTHONPATH']
    assert environ["LANG"] == environ["LANG"]
    assert environ["LANGUAGE"] == environ["LANGUAGE"]
    assert environ["HOSTNAME"] == environ["HOSTNAME"]
    assert environ["SHELL"] == environ["SHELL"]
    assert environ["USER"] == environ["USER"]
    assert environ["HOME"] == environ["HOME"]
    assert environ["PATH"] == environ["PATH"]
    assert environ["PWD"] == environ["PWD"]
    assert environ["OLDPWD"] == environ["OLDPWD"]
    assert environ["TERM"] == environ["TERM"]
    assert environ["XDG_SEAT"] == environ

# Generated at 2022-06-13 16:37:16.603995
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that the environment variable that are set to byte strings are converted to text
    # strings
    environ._raw_environ['foo'] = 'bar'
    assert environ['foo'] == 'bar'
    # If a conversion is not possible, that an exception is raised:
    bad = to_bytes('\u20ac', encoding='latin-1', errors='surrogate_or_strict')
    environ._raw_environ['foo'] = bad
    try:
        environ['foo']
    except UnicodeDecodeError as e:
        assert e.args[1] == bad
        assert e.args[3] == 0
        assert e.args[4] == len(bad)
    else:
        assert False, 'Expected UnicodeDecodeError, got no exception'

    # Test that the environment variable that are set

# Generated at 2022-06-13 16:37:23.897631
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    assert type(env['PATH']) is str
    assert env['PATH'] == os.getenv('PATH')

    # With a different encoding
    env = _TextEnviron(encoding='latin-1')
    assert type(env['PATH']) is str
    assert env['PATH'] == os.getenv('PATH').decode('latin-1', errors='strict')


# Generated at 2022-06-13 16:37:34.591730
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import PY2
    raw_environ = {'FOO': b'\x05\x8b\x03\x99'}
    if PY2:
        expected = u'\u0005\u202b\u0003\xe2\x82\xac'
    else:
        # Python3 correctly returns the bytes unadulterated
        expected = b'\x05\x8b\x03\x99'
    text_environ = _TextEnviron(raw_environ)
    assert expected == to_text(text_environ['FOO'])


# Generated at 2022-06-13 16:37:43.509796
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    #
    # Set up
    #
    # Create a test environment
    #
    import tempfile

    tmpdir = tempfile.mkdtemp()
    environ = _TextEnviron()
    environ['key'] = 'value'

    # Create a file on disk
    #
    # We're going to treat this file as an executable.  So it's important
    # that we create it as something that can be executed.
    #
    # To do that, we create the file and then use os.chmod() to make it
    # executable.
    #
    # We don't want to set the umask to a value allowing other users
    # on the system to execute the file.  So we create the file with
    # no permissions and then add in the needed permissions.
    #
    # The goal of creating the file is to then

# Generated at 2022-06-13 16:37:51.105066
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    my_environ = _TextEnviron()
    assert to_text('foo') in my_environ
    os.environ[to_text('foo')] = to_text('bar')
    assert to_text('bar') == my_environ[to_text('foo')]

    # Make sure that the 'bar' value is cached
    os.environ[to_text('foo')] = to_text('baz')
    assert to_text('bar') == my_environ[to_text('foo')]
    del os.environ[to_text('foo')]



# Generated at 2022-06-13 16:38:02.093374
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY2

    class TestEnviron(object):
        def __init__(self):
            self._environ = {}

        def __getitem__(self, name):
            return self._environ[name]

        def __iter__(self):
            for value in self._environ.values():
                yield value

        def __setitem__(self, name, value):
            self._environ[name] = value

        def __delitem__(self, name):
            del self._environ[name]

        def __len__(self):
            return len(self._environ)

    if PY2:
        key = 'key'
        value_str = u'value \u7FFD'
        value_bytes = value_str.encode('utf-8')

# Generated at 2022-06-13 16:38:04.507936
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _environ = _TextEnviron({'ANSIBLE_ANSIBLE_MODULE_UTILS': 'test-value'})

    assert _environ['ANSIBLE_ANSIBLE_MODULE_UTILS'] == 'test-value'


# Generated at 2022-06-13 16:38:09.047492
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PYTHONIOENCODING'] == 'utf-8'

if __name__ == '__main__':
    test__TextEnviron___getitem__()
    print('All tests passed')

# Generated at 2022-06-13 16:38:16.374817
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:38:28.462167
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import PY3

    # Create a test with all of the possible different environment variable value types
    test_env = {b'bytes_only': b'bytes_only',
                u'unicode_only': u'unicode_only',
                'unicode_and_bytes': (u'unicode_and_bytes' + os.fsencode(u'unicode_and_bytes')),
                }

    # Ensure that we can't directly pass a test_env variable through to _TextEnviron
    try:
        result = _TextEnviron(test_env, encoding='utf-8')
    except TypeError:
        # We expect a TypeError
        result = None
        pass


# Generated at 2022-06-13 16:38:32.851206
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six.moves.builtins import unicode
    assert 'PyPy' in true_environ

    assert isinstance(environ['PyPy'], unicode)



# Generated at 2022-06-13 16:38:40.241494
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six.moves.urllib.parse import quote_plus

    an_int = 12345
    an_int_as_text = to_text(an_int)

    booleans = [True, False]
    booleans_text = [to_text(boolean) for boolean in booleans]

    a_float = 0.12345
    a_float_as_text = to_text(a_float)

    a_bytes = to_bytes('some bytes')
    a_bytes_as_text = to_text(a_bytes)
    a_bytes_url_escaped = quote_plus(to_bytes(a_bytes))

    a_text = 'some text'
    a_text_as_text = to_text(a_text)
    a_text_

# Generated at 2022-06-13 16:38:48.768255
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The purpose of this method unit test is to provide maximum code coverage
    # (100%) of method __getitem__ and to validate that foreign language
    # characters are correctly converted to unicode under Python 2.
    # The code coverage of the other methods is implicitly tested by the code
    # coverage of the code using the environ variable defined above.

    # Setup
    # 0. Remove the 'LC_ALL' environment variable so that the following
    #    assertions are not affected by it.  See Travis CI Configuration File
    #    for more details.
    #    https://docs.travis-ci.com/user/customizing-the-build/#Build-Matrix
    if 'LC_ALL' in os.environ:
        del os.environ['LC_ALL']
    # 1. Create a dictionary for the environment variables and set the
    #    environment variable

# Generated at 2022-06-13 16:38:58.356652
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if not PY3:
        result = environ['TESTENVIRON']
        assert type(result) is str, 'type of result of __getitem__ is not str'

        # Test if decoding is done properly
        os.environ['TESTENVIRON'] = u'héllo'
        environ['TESTENVIRON'] = u'héllo'
        assert environ['TESTENVIRON'] == u'héllo', 'Decoding is not done properly'

        # Test if encoding is done properly for non-unicode
        environ['TESTENVIRON'] = 'héllo'
        assert environ['TESTENVIRON'] == u'héllo', 'Encoding is not done properly for non-unicode'

        # Test if encoding is done properly for bytear

# Generated at 2022-06-13 16:39:07.436493
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Tests for function '_TextEnviron.__getitem__'
    tests = [
        {
            'name': 'Normal case',
            'in': {'key': 'PATH'},
            'out': {'return_value': environ['PATH'], 'exception': None},
        },
        {
            'name': 'KeyError case',
            'in': {'key': 'BAD_KEY'},
            'out': {
                'return_value': None,
                'exception': KeyError,
            },
        },
    ]

    for test in tests:
        if test['out']['exception']:
            try:
                tmp = environ[test['in']['key']]
            except test['out']['exception'] as e:
                tmp = e

# Generated at 2022-06-13 16:39:11.950165
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    env = _TextEnviron({b'dummy_key_1': b'dummy_value_1', b'dummy_key_2': b'dummy_value_2'})

    # Act and Assert
    assert env[b'dummy_key_1'] == u'dummy_value_1'
    assert env[b'dummy_key_2'] == u'dummy_value_2'



# Generated at 2022-06-13 16:39:21.538106
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that environment values get coerced to text strings

    This is important on Python2 where os.environ is a mutable mapping of bytes by default (i.e.
    Keys and values are both bytes.  This class makes the keys text and the values text as well.
    """
    # Note: The builtin os.environ is used in the tests because that's the object that our
    # environ object above wraps and will be wrapped by when the PY3 check above is removed.
    # Furthermore, this is the version that Ansible will run on and the one we really care about.
    #
    # Note: This test only runs when this module is called directly.  It doesn't run when this is
    # imported into a module as a library.
    #
    # First set up the data to be tested.

# Generated at 2022-06-13 16:39:31.853791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _MockText(object):
        def __init__(self):
            self._val = ''

        def __eq__(self, other):
            return self._val == other

        def __getitem__(self, key):
            if key == slice(None, None, 1):
                return self._val
            raise NotImplementedError

        def __setitem__(self, key, value):
            if key == slice(None, None, 1):
                self._val = value
            else:
                raise NotImplementedError

    class _MockEnviron(dict):
        def __getitem__(self, key):
            if key == 'TEST_VAR':
                return b'\xc3\xa9'  # b'\xe9' is latin-1, b'\xc3\xa9'

# Generated at 2022-06-13 16:39:36.231843
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron(encoding='utf-8')
    assert e['HOME'] == to_text(to_bytes('HOME'), encoding='utf-8', nonstring='passthru')

# Generated at 2022-06-13 16:39:38.055282
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert 'non ascii: ä' == environ['non ascii: ä']

# Generated at 2022-06-13 16:39:39.852998
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  assert(environ['PATH'] == '/bogus/path:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin')

# Generated at 2022-06-13 16:39:54.581850
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    utf8_encoded_env = {
        'FOO': 'FOO'.encode('utf-8'),
        'BAR': 'BAR'.encode('utf-8'),
    }
    iso8859_encoded_env = {
        'FOO': 'FOO'.encode('iso8859-1'),
        'BAR': 'BAR'.encode('iso8859-1'),
    }

    if PY3:
        # __getitem__ should return the same strings returned by os.environ on Python3
        assert _TextEnviron()['FOO'] == 'FOO'
        assert _TextEnviron()['BAR'] == 'BAR'
        assert _TextEnviron(env=utf8_encoded_env)['FOO'] == 'FOO'

# Generated at 2022-06-13 16:40:03.206184
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    current = dict(environ)

    # Check non-unicode value
    environ['TEST_A'] = b'\xff'
    assert environ['TEST_A'] == u'\ufffd'
    assert b'\xff' not in environ

    # Check unicode value
    environ['TEST_B'] = u'\ufffd'
    assert environ['TEST_B'] == u'\ufffd'

    # Check unicode-surrogate value
    environ['TEST_C'] = u'\ufffd\uD83D\uDCA9'  # The string is '�💩'
    assert environ['TEST_C'] == u'\uffff\uD83D\uDCA9'  # The string is '�💩'

    # Check unicode

# Generated at 2022-06-13 16:40:11.736154
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    This section tests the function __getitem__ of class TextEnviron
    """
    import os
    # os.environ returns byte strings on Python2 so we can simply set one
    # here.  We only need to check that the decoding works in the second case
    os.environ['foo'] = 'a'
    myenviron = _TextEnviron(env={b'bar': b'b'})
    # This is the first case.  We set a byte string and get a text string
    assert myenviron['foo'] == 'a'
    # This is the second case.  We set a byte string and get a text string
    assert myenviron['bar'] == 'b'
    # This tests that the object works with things that aren't in the dict

# Generated at 2022-06-13 16:40:15.321686
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({"k1": "byte/str", "k2": u"unicode"})

    assert u"byte/str" == e["k1"]
    assert u"unicode" == e["k2"]



# Generated at 2022-06-13 16:40:16.275158
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['KERNEL'] == 'ansible'

# Generated at 2022-06-13 16:40:24.417028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _TextEnvironFake(object):
        def __getitem__(self, key):
            return b'\xed\x9a\x8d\xed\x8d\xb0\xed\x83\x80\xed\x8b\xbb'

    fake_environ = _TextEnvironFake()
    text_environ = _TextEnviron(env=fake_environ)
    assert text_environ['foo'] == u'\ud7a5\ud68d\ud0b0\udc80\udcbb'

# Generated at 2022-06-13 16:40:34.264005
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['utf-8_key'] = 'utf-8_value'
    os.environ['ascii_key'] = 'ascii_value'

    assert type(os.environ) is not _TextEnviron
    assert isinstance(environ, _TextEnviron)

    # ansible-test does setup in a way which doesn't actually run the code in utils/module_docs_fragments/module_common.py
    # So, we need to manually call the method.
    environ._ensure_text_items()

    expected_environ_keys = {'utf-8_key', 'ascii_key'}
    actual_environ_keys = set(environ.keys())
    assert expected_environ_keys == actual_environ_keys


# Generated at 2022-06-13 16:40:36.489936
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ["ANSIBLE_CORE_TEST_KEY"] = to_bytes(u'\u2423', encoding='utf-8', nonstring='strict', errors='surrogate_or_strict')
    assert environ["ANSIBLE_CORE_TEST_KEY"] == u'\u2423'
    del os.environ["ANSIBLE_CORE_TEST_KEY"]

# Generated at 2022-06-13 16:40:41.031152
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == 'C:\\Windows\\system32;C:\\Windows'
    # On Python 2, os.environ['PATH'] == 'C:\\Windows\\system32;C:\\Windows'.encode('utf-8')
    # On Python 3, os.environ['PATH'] == 'C:\\Windows\\system32;C:\\Windows'
    assert isinstance(environ['PATH'], str)



# Generated at 2022-06-13 16:40:44.970903
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['MYVAR'] = b'J\xfcnker'  # Jünker
    assert environ['MYVAR'] == u'Jünker'



# Generated at 2022-06-13 16:40:52.427633
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert to_bytes(environ['USER'], encoding=environ.encoding, nonstring='strict',
                    errors='surrogate_or_strict') == environ._raw_environ['USER']

# Generated at 2022-06-13 16:41:01.269022
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_text
    if PY3:
        # If we're running on Python3, assert that this method just forwards to the underlying dict
        environ = _TextEnviron({'key': 'value'})
        assert environ['key'] == 'value'
        assert environ.encoding == sys.getfilesystemencoding()
    else:
        # If we're running on Python2, assert that we get the value decoded in the correct encoding
        environ = _TextEnviron({'key': u'value'})
        assert environ['key'] == to_text(u'value', encoding='utf-8')
        assert environ.encoding == 'utf-8'

# Generated at 2022-06-13 16:41:07.301711
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
     # Set up the test, initialize variables and save the state of os.environ
    environ['newkey'] = 'newvalue'
    saved_environ = os.environ.copy()
    # Run the function being tested
    result = environ['newkey']
    result_type = type(result)
    # Check the results against what we expected
    assert result == 'newvalue'
    if PY3:
        assert result_type is str
    else:
        assert result_type is unicode
    # Restore the state of os.environ
    os.environ = saved_environ



# Generated at 2022-06-13 16:41:14.813854
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_KEY1'] = u'result'
    expected_result = to_bytes(u'result', encoding='utf-8', nonstring='strict',
                               errors='surrogate_or_strict')
    assert isinstance(environ['TEST_KEY1'], type(u''))
    assert environ['TEST_KEY1'] == u'result'
    assert environ._raw_environ['TEST_KEY1'] == expected_result
    assert environ._value_cache[expected_result] == u'result'



# Generated at 2022-06-13 16:41:25.867606
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test when Python is running within UTF-8 locale
    environ.encoding = 'utf-8'

    # Test for where key does not exist in os.environ
    environ._raw_environ = {b'key1': b'value1'}
    try:
        environ['key2']
        assert False
    except KeyError:
        pass

    # Test for non-str value and non-str key
    environ._raw_environ = {b'key1': b'value1'}
    key = b'key1'
    true_value = 'value1'
    try:
        assert environ[key] == true_value
    except KeyError:
        pass

    # Test for non-str value and str key

# Generated at 2022-06-13 16:41:36.437933
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  myfile = open("foo_bar.txt", "w")
  myfile.write("foo")
  myfile.close()

  environ["foo"] = "bar"
  if not isinstance(environ["foo"], str):
    raise ValueError("Test failed: environ[\"foo\"] should be a string, but is " + type(environ["foo"]).__name__)
  environ["foo"] = 123
  if not isinstance(environ["foo"], str):
    raise ValueError("Test failed: environ[\"foo\"] should still be a string, but is " + type(environ["foo"]).__name__)

  # try to get an environment variable which does not exist

# Generated at 2022-06-13 16:41:44.347203
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """ This method tests the __getitem__ method of class _TextEnviron """
    from ansible.module_utils.six import PY3
    # test_environ is a 'dict' on PY3 and an os._Environ on PY2
    test_environ = _TextEnviron()

    if PY3:
        # A cache should be used to convert the value to text
        # first time, should not be in cache, so do the conversion
        assert test_environ['testkey'] == 'testvalue'
        # second time, should be in the cache
        assert test_environ['testkey'] == 'testvalue'

# Generated at 2022-06-13 16:41:53.243196
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import ansible_collections

    ansible_collections_path = os.path.dirname(ansible_collections.__file__)
    environ['ANSIBLE_COLLECTIONS_PATHS'] = os.path.join(ansible_collections_path,
                                                        'ansible_collections')

    assert isinstance(environ['ANSIBLE_COLLECTIONS_PATHS'], str),\
    'Unexpected type: environ["ANSIBLE_COLLECTIONS_PATHS"] is not of type str'

# Generated at 2022-06-13 16:41:59.456262
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test data & values
    input_set1 = {u'key1': u'value', u'key2': u'value'}
    input_set2 = {u'латинские буквы': u'value', u'ййй': u'значение'}
    input_set3 = {u'key1': 'value', u'латинские буквы': u'value', u'key2': 'value'}
    input_set4 = {b'key1': b'value', b'key2': b'value'}

# Generated at 2022-06-13 16:42:09.369836
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_PYTHON_INTERPRETER'] = '/usr/bin/python3'
    environ = _TextEnviron(encoding='utf-8')
    assert environ['ANSIBLE_PYTHON_INTERPRETER'] == '/usr/bin/python3'
    # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding() instead of utf-8
    os.environ['testvar'] = 'tfátést'
    environ = _TextEnviron(encoding='utf-8')
    assert environ['testvar'] == 'tfátést'
    try:
        import locale
    except ImportError:
        assert True

# Generated at 2022-06-13 16:42:23.121139
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils import text_environ
    # Arrange
    sut = text_environ.environ

    # Act

    actual_0 = sut['PATH']
    actual_1 = sut['LANG']
    actual_2 = sut['USER']

    # Assert
    assert actual_0 is not None
    assert actual_1 is not None
    assert actual_2 is not None

# Generated at 2022-06-13 16:42:25.425662
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    tmp_environ = _TextEnviron(encoding='utf-8')
    assert {'ANSIBLE_TEST_KEY1': '¡Hola!'} == tmp_environ._raw_environ



# Generated at 2022-06-13 16:42:34.830554
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with getdefaultencoding - fake environ is only used in tests
    fake_environ = {
        'strstr': 'strstr',
        'unicode': u'unicode',
        'bytes': b'bytes',
        'text1': to_text(b'text1', encoding='utf-8', nonstring='passthru'),
        'text2': to_text(u'text2', encoding='utf-8', nonstring='passthru')
    }
    test_environ = _TextEnviron(env=fake_environ)

    assert isinstance(test_environ['strstr'], str)
    assert isinstance(test_environ['unicode'], str)
    assert isinstance(test_environ['bytes'], str)

# Generated at 2022-06-13 16:42:39.162028
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_VAR'] = 'utf-8 string é'
    assert isinstance(environ['TEST_VAR'], unicode)
    assert environ['TEST_VAR'] == 'utf-8 string é'


# Generated at 2022-06-13 16:42:47.551469
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # When Python 2 and an environment key is set to a text string, it should be converted to bytes
    # in the environ dict and returned as a text string
    environ['FOO'] = 'bar'
    if PY3:
        assert isinstance(environ['FOO'], str)
        assert environ['FOO'] == 'bar'
    else:
        assert isinstance(environ['FOO'], unicode)
        assert environ['FOO'] == u'bar'

    # When Python 3 and an environment key is set to a bytestring, it should be returned as a text
    # string.
    environ['FOO'] = b'bar'
    if PY3:
        assert isinstance(environ['FOO'], str)
        assert environ['FOO'] == 'bar'

# Generated at 2022-06-13 16:42:58.681968
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    _TextEnviron() class method __getitem__
    '''

    # Test when converting bytes to text with surrogateescape fails
    old_environ = os.environ
    try:
        os.environ = {b'foo': b'\x80'}
        environ = _TextEnviron(env=os.environ, encoding='utf-8')
        environ['foo']
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError('UnicodeDecodeError not raised')

    # Test when converting text to bytes with surrogateescape fails
    old_environ = os.environ

# Generated at 2022-06-13 16:43:06.658247
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test case for method __getitem__ of class _TextEnviron
    '''

    import os

    # create a dict
    kvpair = {'key1': 'value1', 'key2': 'value2'}
    # set env(save in os.environ)
    for k, v in kvpair.items():
        os.environ[k] = v
    # create a _TextEnviron instance
    t = _TextEnviron()
    # test exist env
    for k, v in kvpair.items():
        print(t[k])
        assert t[k] == v
    # test not exist env
    try:
        print(t['key3'])
    except KeyError:
        pass
    else:
        raise KeyError
    # remove env

# Generated at 2022-06-13 16:43:13.773361
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that the __getitem__ method handles different values of environment variables.
    """
    env = _TextEnviron({'a': 'x', 'b': 1, 'c': 'é'})
    assert env['a'] == u'x'
    assert env['b'] == u'1'
    assert env['c'] == u'é'

    # if the value is already unicode, leave it that way
    env = _TextEnviron({'a': u'x', 'b': u'1', 'c': u'é'})
    assert env['a'] == u'x'
    assert env['b'] == u'1'
    assert env['c'] == u'é'

    if not PY3:
        # bytes values with non-ascii characters will be decoded
        env = _TextEnviron

# Generated at 2022-06-13 16:43:19.247949
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env_var1 = 'TEST_ENV_VAR1'
    env_var2 = 'TEST_ENV_VAR2'
    env_var3 = 'TEST_ENV_VAR3'
    if env_var1 in environ:
        del environ[env_var1]
    if env_var2 in environ:
        del environ[env_var2]
    if env_var3 in environ:
        del environ[env_var3]
    # Test decoding
    environ[env_var1] = b'\xc3\x98'
    assert environ[env_var1] == u'\u00d8'
    environ[env_var2] = b'\xe2\x81\xa7'

# Generated at 2022-06-13 16:43:24.003733
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import MutableMapping

    class Test_TextEnviron(unittest.TestCase):
        def test_getitem_returns_unicode(self):
            environ = _TextEnviron()
            self.assertIsInstance(environ['PATH'], type(u' '))

    suite = unittest.TestLoader().loadTestsFromTestCase(Test_TextEnviron)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 16:43:50.139821
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({to_bytes('foo'): to_bytes('bar'), to_bytes('bin'): to_bytes('baz')})
    environ.update(env)
    assert environ['foo'] == 'bar'
    assert environ['bin'] == 'baz'
    environ.pop('foo')
    assert 'foo' not in environ
    environ.pop('bin')
    assert 'bin' not in environ


# Generated at 2022-06-13 16:43:56.920327
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    print('test__TextEnviron___getitem__()')

    # first, be sure we can set and get values in environ
    environ['HOME'] = u'äüö'
    assert isinstance(environ['HOME'], str)
    assert environ['HOME'] == u'äüö'
    del environ['HOME']

    # now, verify that variables set in environ first are passed to us as unicode and not binary
    os.environ['ÄÖÜ'] = u'äöü'.encode('utf-8')
    assert isinstance(environ['ÄÖÜ'], str)
    assert environ['ÄÖÜ'] == u'äöü'

    # set some binary strings to test decoding

# Generated at 2022-06-13 16:44:08.843830
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # - use a new object to avoid contaminating os.environ
    env = _TextEnviron()
    # - test list of existing items
    existing_items = {
        "foo_str": "bar",
        "foo_bytes": b"bar",
        "foo_int": 42,
    }
    for key, value in existing_items.items():
        if not PY3:
            if isinstance(value, int):
                # Python2 does not allow setting an int in os.environ
                continue

# Generated at 2022-06-13 16:44:18.274300
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron.
    """
    # PYTHON-1223.  If the key in the environment is not utf-8, it should raise an exception
    e = _TextEnviron(env={'C': b'\xff'})
    try:
        e['C']
    except UnicodeDecodeError:
        pass
    else:
        assert False, "non-utf-8 string should raise an exception"

    # Non-ascii byte string for the key
    # PY2: if the string is ascii, it does not raise an exception, even if it is not utf-8,
    # because it does not use the specified encoding.

# Generated at 2022-06-13 16:44:30.263070
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    original_environ = environ._raw_environ.get('HOME')
    assert original_environ is not None
    # Test with the original undecoded value
    assert environ._raw_environ['HOME'] == original_environ
    # Test with the decoded value
    assert environ['HOME'] == to_text(original_environ, encoding='utf-8', nonstring='passthru',
                                      errors='surrogate_or_strict')

    # Test with a value which is changed during a run
    # This is the devilish case where the environ is changed but we are using the cached value
    # instead of the new value.
    # We don't have a way to get the cached values of os.environ and the newly passed in
    # environment variables so we can't test this fully.
    # However, the cached

# Generated at 2022-06-13 16:44:39.020711
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    expected_keys = ['a', 'b', 'c']
    expected_values = ['1', '2', '3']
    raw_environ = dict(zip(expected_keys, expected_values))
    te = _TextEnviron(raw_environ, encoding='utf-8')
    assert expected_keys == sorted(te.keys()), 'Keys do not match'
    assert len(expected_values) == len(list(te.values())), 'Number of values is wrong: %s' % list(te.values())
    for expected_value in expected_values:
        assert expected_value in list(te.values()), 'Value %s is not in environment' % expected_value
    assert sorted(expected_values) == sorted(list(te.values())), 'Value does not match'



# Generated at 2022-06-13 16:44:51.039194
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({'b': b'\xe2\x9a\x82\xe2\x99\xaa\xe2\x8f\xa9', 'c': 'z'})
    assert e['b'] == '☂☺︩'
    assert e['c'] == 'z'
    assert e.get('b') == '☂☺︩'
    assert e.get('c') == 'z'
    assert e.get('does_not_exist') is None
    assert e.get('does_not_exist', 'default') == 'default'
    # Make sure that an existing byte key can still be read

# Generated at 2022-06-13 16:45:01.446899
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''test__TextEnviron___getitem__'''
    # Case 1: Test string value of env variable
    environ['test'] = 'test_string'
    assert environ['test'] == 'test_string'
    assert environ['test'] == environ._raw_environ['test']

    # Case 2: Test bytes value of env variable
    environ['test2'] = b'test_bytes'
    assert environ['test2'] == 'test_bytes'
    assert environ['test2'] == environ._raw_environ['test2']

    # Case 3: Test unicode value of env variable
    environ['test3'] = u'test_unicode'
    assert environ['test3'] == 'test_unicode'

# Generated at 2022-06-13 16:45:05.544266
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_utf8 = _TextEnviron({'foo': '\xe5\xad\xb8\xe8\xa7\x84\xe6\x9b\xb8\xe9\x9c\x93\xe8\xb5\x84\xe6\x96\x99'}, encoding='utf-8')
    assert environ_utf8['foo'] == '學规書霓资料'

# Generated at 2022-06-13 16:45:13.860434
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test English characters
    for string in ('ABC', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'):
        # Test text->text
        x = _TextEnviron({'foo': string})
        assert x['foo'] == string

        # Test raw->text
        x = _TextEnviron(_raw_environ={'foo': string}, encoding='utf-8')
        assert x['foo'] == string

        # Test raw->text
        x = _TextEnviron(_raw_environ={'foo': string}, encoding='utf-16')
        assert x['foo'] == string

    # Test a variety of Unicode characters