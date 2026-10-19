

# Generated at 2022-06-13 16:35:49.080098
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Raise KeyError when accessing nonexistent key
    nonexistent_key = 'nonexistent_key'
    try:
        environ[nonexistent_key]
    except KeyError:
        pass
    else:
        raise AssertionError('Expected KeyError')

    # Return text for ascii key
    ascii_key = 'ascii_key'
    ascii_val = 'ascii_val'
    expected_text = 'ascii_val'
    environ[ascii_key] = ascii_val
    assert environ[ascii_key] == expected_text

    # Return text for unicode key
    unicode_key = 'unicode_key'
    unicode_val = u'unicode_val'
    expected_text = 'unicode_val'
   

# Generated at 2022-06-13 16:35:54.534707
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron()

    assert text_environ['HOME'] == os.environ['HOME']
    assert text_environ[os.environ['HOME']] == os.environ['HOME']
    assert text_environ[os.environ[b'HOME'].decode('utf-8')] == os.environ['HOME']

# Generated at 2022-06-13 16:36:03.707165
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Data
    key1 = 'test__TextEnviron___getitem___key1'
    key2 = 'test__TextEnviron___getitem___key2'
    key3 = 'test__TextEnviron___getitem___key3'
    value1 = u'test__TextEnviron___getitem___value1'
    value2 = b'test__TextEnviron___getitem___value2'
    value3 = value2.decode('utf-8')

    # Setup
    environ[key1] = value1
    environ[key2] = value2

    # Test
    assert environ[key1] == value1, 'Failed to get unicode value'
    assert isinstance(environ[key2], type(value1)), 'Value returned as wrong type'

# Generated at 2022-06-13 16:36:07.870356
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Method __getitem__ should return text string from the environment
    """
    os.environ['TEXT_ENVIRON_TEST'] = 'text from environment'
    assert isinstance(environ['TEXT_ENVIRON_TEST'], str)
    os.unsetenv('TEXT_ENVIRON_TEST')

# Generated at 2022-06-13 16:36:11.065032
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    environ['PATH'] = path
    assert path == environ['PATH']



# Generated at 2022-06-13 16:36:12.414407
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == u'/home/toshio'



# Generated at 2022-06-13 16:36:23.048121
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that keys can be retrieved as text
    assert environ['HOME'] == '/home/badger'

    # Test that keys retrieved as text while passing in a byte string
    assert environ[b'HOME'] == '/home/badger'

    # Test that keys can be retrieved while passing in a text string
    assert environ[u'HOME'] == '/home/badger'

    # Test that non-strings are not allowed
    try:
        environ[42]
        assert False, "Should not be able to retrieve environment keys by arbitrary types"
    except TypeError:
        pass

    # Test that unicode values can be retrieved
    os.environ['UNICODETEST'] = u'Français'
    assert environ['UNICODETEST'] == u'Français'

    # Test that unicode values can be retrieved

# Generated at 2022-06-13 16:36:32.808348
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    global environ

    assert environ.__getitem__(b'ANSIBLE_CALLBACK_WHITELIST') == u'profile_tasks, timer, v2_playbook_on_setup, v2_playbook_on_import_for_host'

    # Setup a fake environment with unicode text
    fake_environ = {b'1': u'\u01a1'.encode('utf-8')}
    # Setup a test instance
    test_instance = _TextEnviron(fake_environ, encoding='utf-8')
    # Test __getitem__(), which does the conversion and caching
    assert test_instance.__getitem__(b'1') == u'\u01a1'
    # Test that the cache contains the converted value

# Generated at 2022-06-13 16:36:38.165157
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest


# Generated at 2022-06-13 16:36:46.103453
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()

    def normal_env():
        return {'ASCII': '7bit',
                'LATIN1': 'I like coffee.',
                'LATIN2': "I \u0107\u0106\u017d\u017e like coffee.",
                'UTF8': "I \u2615\u2605\u2605 like coffee.",
                'LATIN1_SURROGATE': "\ud83c\udf7a",
                'UTF8_SURROGATE': "\ud83c\udf6c\U0001f3f3\U0001f3f3"}


# Generated at 2022-06-13 16:36:56.114792
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test _TextEnviron.__getitem__ with various python versions and environment variables.
    '''
    import tempfile
    import os

    # default
    environ = _TextEnviron(encoding='utf-8')
    assert environ['DEFAULT'] is None
    # an existing entry in the environment (ASCII string)
    preexisting_entry = tempfile.mkstemp()[1]
    os.environ[preexisting_entry] = 'value'
    environ = _TextEnviron(encoding='utf-8')
    assert environ[preexisting_entry] == 'value'
    del os.environ[preexisting_entry]
    # an existing entry in the environment (non-ASCII string)

# Generated at 2022-06-13 16:37:04.541764
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # set up environment variable
    test_key = 'ANSIBLE_TEST'
    test_value = 'ansible_test'

    # set the environment variable
    os.environ[test_key] = test_value

    # test __getitem__ of class _TextEnviron
    assert environ[test_key] == test_value

    # delete the environment variable
    del os.environ[test_key]

    # test __getitem__ of class _TextEnviron
    try:
        environ[test_key]
    except KeyError:
        pass
    else:
        assert False

# Generated at 2022-06-13 16:37:09.911018
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test _TextEnviron.__getitem__()"""
    # Test bytes as key
    environ = _TextEnviron({b'a': b'b'})
    assert environ[b'a'] == u'b'

    # Test str as key
    environ = _TextEnviron({'a': b'b'})
    assert environ['a'] == u'b'

    # Test bytes as value
    environ = _TextEnviron({'a': b'b'})
    assert environ['a'] == u'b'

    # Test str as value
    environ = _TextEnviron({'a': u'b'})
    assert environ['a'] == u'b'



# Generated at 2022-06-13 16:37:12.579786
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = {"my_var": "foo"}
    text_env = _TextEnviron(env=test_env)
    assert text_env["my_var"] == "foo"

# Generated at 2022-06-13 16:37:24.581254
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron({'foo': 'bar', 'baz': 'qux'}, encoding='utf-8')
    text_environ['abc'] = 'def'
    text_environ['ghi'] = 'jkl'
    assert text_environ['foo'] == u'bar'
    assert text_environ['baz'] == u'qux'
    assert text_environ['abc'] == u'def'
    assert text_environ['ghi'] == u'jkl'


# Generated at 2022-06-13 16:37:35.740229
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  environ_instance = environ
  environ_dict = {}

  # With PY3 and with a valid key
  assert environ_instance["PATH"] == os.environ["PATH"]

  # With PY3 and with a key that doesn't exist
  try:
    environ_instance["ABSENT_KEY"]
  except KeyError as e:
    assert e.args[0] == u'ABSENT_KEY'
  else:
    assert 0, "KeyError exception not raised!"

  # With valid key
  assert environ_instance["PATH"] == os.environ["PATH"]

  # With a key that doesn't exist
  try:
    environ_instance["ABSENT_KEY"]
  except KeyError as e:
    assert e.args[0] == u'ABSENT_KEY'
 

# Generated at 2022-06-13 16:37:44.215534
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_native, to_text
    #create a byte string for the test
    byte_str = to_bytes(u'El Niño')
    environ_test = _TextEnviron({'name': byte_str})
    assert environ_test['name'] == u'El Niño'
    assert isinstance(environ_test['name'], str)
    #create an unicode string for the test
    unicode_str = u'El Niño'
    environ_test_2 = _TextEnviron({'name': unicode_str})
    assert environ_test_2['name'] == u'El Niño'
    assert isinstance(environ_test_2['name'], str)


# Generated at 2022-06-13 16:37:53.613778
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _read_env(e):
        with os.fdopen(e, 'rb') as env:
            return env.read()

    # My default locale is en_US.utf-8 but I don't have the locale installed on my travis build
    # machines.  This causes the test to fail there.  Instead, try to get the default encoding from
    # PYTHONIOENCODING which will always be set on Travis.  We'll use this as the default if
    # en_US.utf-8 fails.
    default_encoding = 'utf-8'
    try:
        default_encoding = locale.getdefaultlocale()[1]
    except ValueError:
        pass


# Generated at 2022-06-13 16:38:03.643933
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest
    import six

    class Test(unittest.TestCase):
        def setUp(self):
            self.env_var_keys = set(['PATH', 'PWD', 'LANG'])
            self.env_var_values = set(['/usr/bin', '/home', 'en_US.UTF-8'])
            self.env = _TextEnviron(env=os.environ)
            self.python3_or_later = sys.version_info[0] >= 3

        def test__TextEnviron___getitem__not_python_3(self):
            """
            Make sure __getitem__ returns text string when using Python < 3
            """
            if self.python3_or_later:
                self.skipTest("Can't run this test on Python 3")
            import locale
           

# Generated at 2022-06-13 16:38:12.265315
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST_ENV1'] = 'FOO'
    environ = _TextEnviron()
    assert environ['TEST_ENV1'] == u'FOO'
    assert environ.get('TEST_ENV1') == u'FOO'
    assert environ.get('TEST_ENV1', 'BAR') == u'FOO'

    os.environ['TEST_ENV2'] = b'FOO'
    environ = _TextEnviron()
    assert environ['TEST_ENV2'] == u'FOO'
    assert environ.get('TEST_ENV2') == u'FOO'
    assert environ.get('TEST_ENV2', 'BAR') == u'FOO'


# Generated at 2022-06-13 16:38:27.677961
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ2 = _TextEnviron({b'FOO': b'foo', b'BAR': b'bar'}, encoding='utf-8')
    assert isinstance(environ2['FOO'], str)
    assert isinstance(environ2['BAR'], str)

    # Test non-ascii
    environ2[b'BAD'] = b'\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd1\x80\xd0\xb0'
    assert isinstance(environ2['BAD'], str)
    assert len(environ2) == 3

    # Test changing values
    environ2[b'BAD'] = b'new value'

# Generated at 2022-06-13 16:38:35.684214
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({'a': '1', 'b': '2', b'c': '3', u'a': '1'}, encoding='utf-8')
    assert environ['a'] == '1'
    assert environ['b'] == '2'
    assert environ['c'] == '3'
    if not PY3:
        # On Python 2, the 'a' value is used from the kwargs because of
        # https://stackoverflow.com/questions/7194747/why-does-dict-update-override-values-in-python
        assert environ[u'a'] == '1'
    else:
        assert environ[u'a'] == '1'
        assert environ['b'.encode()] == '2'

# Generated at 2022-06-13 16:38:46.376026
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # test byte string
    byte_string = "µ¢£¤¥¦¬\xbd\xbe"
    os.environ[b'test_byte_string'] = byte_string
    assert environ[b'test_byte_string'] == byte_string

    # test text string
    text_string = "µ¢£¤¥¦¬\u0bd0\u1fbe"
    os.environ[u'test_text_string'] = text_string
    assert environ[u'test_text_string'] == text_string

    del os.environ[b'test_byte_string']
    del os.environ[u'test_text_string']



# Generated at 2022-06-13 16:38:56.195591
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY2, u

    os.environ['LANG'] = b'C.UTF-8'
    fse = sys.getfilesystemencoding()
    if PY2:
        assert environ['LANG'] == u('C.UTF-8')
    else:
        assert environ['LANG'] == 'C.UTF-8'

    if not PY2:
        return

    environ = _TextEnviron(encoding='utf-8')
    os.environ['LANG'] = to_bytes('pt_BR.UTF-8', encoding=fse)
    # Should raise UnicodeError on Python2
    try:
        environ['LANG']
        assert False
    except UnicodeError:
        pass


# Generated at 2022-06-13 16:39:00.075352
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron({b'test_key': b'\xc0\xa9'}, encoding='utf-8')
    assert e[b'test_key'] == u'\ufffd\ufffd'

# Generated at 2022-06-13 16:39:08.688958
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    source = os.environ.copy()

# Generated at 2022-06-13 16:39:19.067480
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron()
    key_to_value = {
        'HOME': os.path.expanduser('~'),
        'PATH': os.pathsep.join((os.getcwd(), os.environ['PATH'])),
        'PATH.UTF8': os.path.expanduser(u'~'),
        'DERP': u'\u00c9',
        'DERP.UTF8': u'\u00c9',
        'DERP.LATIN1': b'\xc9',
    }
    for key, value in key_to_value.items():
        assert text_environ[key] == value, text_environ[key]



# Generated at 2022-06-13 16:39:26.626576
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def my_assert(_, expected, key):
        assert(expected == environ[key])

    accented_string = '\xe5\xe4\xf6'
    # Python2 -> Python2
    if PY3:
        my_assert(None, accented_string, 'py2_accented')
    else:
        try:
            environ['py2_accented']
            assert False
        except UnicodeEncodeError:
            pass
        except Exception as e:
            assert False, "Unexpected Exception: " + str(e)

    # Python2 -> Python3
    if PY3:
        my_assert(None, accented_string, 'py2_accented')

# Generated at 2022-06-13 16:39:34.223519
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """

    # Test for encoding utf-8
    environ = _TextEnviron(encoding='utf-8')
    environ['LANG'] = 'en_US.UTF-8'

    assert environ['LANG'] == 'en_US.UTF-8'

    # Test for encoding latin-1
    environ = _TextEnviron(encoding='latin-1')
    environ['LANG'] = 'en_US.UTF-8'.encode('latin-1')

    assert environ['LANG'] == 'en_US.UTF-8'

# Generated at 2022-06-13 16:39:43.125188
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'ANSIBLE_TEST_VAR': b'\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'})
    assert env['ANSIBLE_TEST_VAR'] == u'Тест'
    # Test caching
    assert env['ANSIBLE_TEST_VAR'] == u'Тест'
    env[b'ANSIBLE_TEST_VAR'] = b'\xd0\xa2'
    assert env['ANSIBLE_TEST_VAR'] == u'Т'
    env[b'ANSIBLE_TEST_VAR'] = b'\xd0\xa2'
    assert env['ANSIBLE_TEST_VAR'] == u'Т'

# Generated at 2022-06-13 16:39:55.547763
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    sample_text = u'ABC\u1234'
    b_sample_text = sample_text.encode('utf-8')
    t_env = _TextEnviron({b_sample_text: b_sample_text}, encoding='utf-8')

    assert t_env[b_sample_text] == sample_text
    assert t_env[sample_text] == sample_text

# Generated at 2022-06-13 16:39:57.576984
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['spam'] = 'eggs'
    assert 'eggs' == environ['spam']



# Generated at 2022-06-13 16:40:00.545281
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # GIVEN
    e = _TextEnviron()

    # WHEN
    v = e["PATH"]

    # THEN
    assert isinstance(v, text_type)
    assert len(e) == len(os.environ)



# Generated at 2022-06-13 16:40:01.445440
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    pass


# Generated at 2022-06-13 16:40:11.192526
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an environment with UTF8-encoded text inside
    utf8_environ = {to_bytes('name_ascii'): to_bytes('value_ascii'),
                    to_bytes('name_utf8'): to_bytes('value_\xe2\x88\xa1', encoding='utf-8')}
    text_environ = _TextEnviron(env=utf8_environ, encoding='utf-8')

    # The original data still exists
    assert text_environ[to_text('name_ascii')] == to_text('value_ascii')
    assert text_environ[to_text('name_utf8')] == to_text('value_\xe2\x88\xa1')

    # If the data is unicode on the python3 side, it is not converted
   

# Generated at 2022-06-13 16:40:21.085322
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from cs.platform.web.rest.utils import environ
    # test the return value of a key in os.environ
    assert environ['HOME'] == os.environ['HOME']
    # test the return value of a key in os.environ using surrogates
    os.environ['ANSIBLE_ARGS_TEST'] = '\uDC80\uDD31'
    assert environ['ANSIBLE_ARGS_TEST'] == '\uDC80\uDD31'
    # test the return value of a key in os.environ using surrogates
    os.environ['ANSIBLE_ARGS_TEST'] = '\uDC81\uDD32'
    assert environ['ANSIBLE_ARGS_TEST'] == '\uDC81\uDD32'
    # test the return value of a key that is

# Generated at 2022-06-13 16:40:30.087708
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test the method __getitem__ of the class _TextEnviron
    """

    # the path for the tests directory in the ansible repository
    test_data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'test', 'units', 'module_utils', 'common')
    # the path for the files used in the test_shlex_quotes tests
    test_data_path = os.path.join(test_data_path, 'test_win_path_module')

    # On windows, the default encoding used by python for the environment is utf-8 but we want to use
    # a different encoding for this test
    env1 = _TextEnviron({}, encoding='utf-16')
    value_expected = u'test_value'
   

# Generated at 2022-06-13 16:40:40.718086
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # setup
    environ = _TextEnviron(encoding='utf-8')
    # test 1
    assert isinstance(environ['ANSIBLE_LIBRARY'], str)
    assert environ['ANSIBLE_LIBRARY'] == "/usr/share/ansible"
    # test 2
    environ['ANSIBLE_LIBRARY'] = b"b'c'"
    assert isinstance(environ['ANSIBLE_LIBRARY'], str)
    assert environ['ANSIBLE_LIBRARY'] == "b'c'"
    # test 3
    environ['ANSIBLE_LIBRARY'] = "b'c'"
    assert isinstance(environ['ANSIBLE_LIBRARY'], str)
    assert environ['ANSIBLE_LIBRARY'] == "b'c'"


# Generated at 2022-06-13 16:40:44.261127
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  from os import environ
  environ["environ_test"] = "ABC\u2018DEF"
  assert environ["environ_test"] == u'ABC\u2018DEF'

# Generated at 2022-06-13 16:40:54.123943
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest

    class _TextEnviron___getitem__(unittest.TestCase):
        def test_encoding(self):
            test_environ = _TextEnviron({'a': to_bytes('aa', encoding='ascii', nonstring='strict')})
            self.assertEqual(test_environ['a'], to_text('aa', encoding='ascii'))

        def test_nonstring(self):
            test_environ = _TextEnviron({'a': to_bytes(1, encoding='ascii', nonstring='strict')})
            self.assertEqual(test_environ['a'], '1')


# Generated at 2022-06-13 16:41:06.228748
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Environment variables can not contain NUL bytes.  An environment variable with a NUL
    # will have its contents truncated at the first NUL.  Thus it's not possible to have an
    # environ key which is an unprintable character.
    from ansible.module_utils.six import u
    assert environ[u('__name__')] == u('__main__')


# Generated at 2022-06-13 16:41:12.309851
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ.clear()
    environ._value_cache.clear()
    environ._raw_environ[b'ANSIBLE_MODULE_ARGS'] = b'{"my_arg": "my_val"}'

    assert environ[u'ANSIBLE_MODULE_ARGS'] == u'{"my_arg": "my_val"}'
    if PY3:
        # if we're running on Python3 we should have cached the value since it was unaltered
        assert environ._value_cache[b'{"my_arg": "my_val"}'] == u'{"my_arg": "my_val"}'

# Generated at 2022-06-13 16:41:14.520587
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_FOO'] = 'foo'
    assert environ['ANSIBLE_TEST_FOO'] == 'foo'



# Generated at 2022-06-13 16:41:19.565249
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()

    # Input is a key existing in env
    in_key = "PWD"
    out_value = environ[in_key]

    # Input is a key not existing in env
    with pytest.raises(KeyError):
        environ["ABC"]


# Generated at 2022-06-13 16:41:22.545322
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_object = _TextEnviron(encoding='utf-8')
    assert test_object['PYTHONPATH'] == environ['PYTHONPATH']



# Generated at 2022-06-13 16:41:32.093579
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Convert to bytes if needed
    def to_bytes(string):
        if PY3:
            return string
        return to_text(string, encoding='utf-8').encode('utf-8')

    # Check that the decoded string is the same as the original string
    def check_decode(string, decode=True):
        if decode:
            assert environ[to_bytes(string)] == to_text(string, encoding='utf-8')
        else:
            assert environ[to_bytes(string)] == string

    # Check that the string can be decoded with the encoding specified
    def check_decode_encoding(string, encoding):
        assert environ[to_bytes(string)] == to_text(string, encoding=encoding)

    # Can't decode any characters with `ascii'
    check_

# Generated at 2022-06-13 16:41:41.906372
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_cache = _TextEnviron()
    # If the value is a text string, then it will return the text string
    environ_cache._raw_environ = {u'FOO': u'bar'}
    assert environ_cache[u'FOO'] == u'bar'
    assert environ_cache[u'FOO'] is environ_cache[u'FOO']

    # If the value is a byte string, it will be decoded to text and returned as text
    environ_cache._raw_environ = {u'FOO': u'bar'.encode('utf-8')}
    assert environ_cache[u'FOO'] == u'bar'
    assert environ_cache[u'FOO'] is environ_cache[u'FOO']

# Generated at 2022-06-13 16:41:43.237773
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()

    assert env['PATH'] == '/usr/bin'


# Generated at 2022-06-13 16:41:55.888996
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that we handle unicode.  This is somewhat redundant since this was already tested in
    # test_six's TextTestCase.test__getitem__
    #
    # Note that if the environment variable is set, we will hit the cached value instead of the
    # raw value which means that the encoding should be cached the first time it is accessed.
    # This is why we first delete the valiable if it is set.
    if 'UNICODETEST' in environ:
        del environ['UNICODETEST']
    environ['UNICODETEST'] = u'\N{Snowman}'
    assert environ['UNICODETEST'] == u'\N{Snowman}'

    # Test that we handle non-local characters on PY3
    #
    # Note that if the environment variable is set, we will hit

# Generated at 2022-06-13 16:42:00.151792
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test values that are not in self._value_cache
    env = _TextEnviron({b'foo': b'\xc3\xa0'})
    actual = env['foo']
    expected = u'\xe0'
    assert actual == expected

    # Test values that are in self._value_cache
    env = _TextEnviron({b'foo': b'\xc3\xa0'})
    env._value_cache[b'\xc3\xa0'] = u'\xe0'
    actual = env['foo']
    expected = u'\xe0'
    assert actual == expected



# Generated at 2022-06-13 16:42:23.541015
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if PY3:
        assert environ['PATH'] == os.environ['PATH']
        assert environ[u'PATH'] == os.environ['PATH']
        assert environ['PATH'] == os.environ[u'PATH']
        assert environ[u'PATH'] == os.environ[u'PATH']
    else:
        assert environ['PATH'] == os.environ['PATH'].decode('utf-8')
        assert environ[u'PATH'] == os.environ['PATH'].decode('utf-8')
        assert environ['PATH'] == os.environ[u'PATH'].decode('utf-8')
        assert environ[u'PATH'] == os.environ[u'PATH'].decode('utf-8')


# Generated at 2022-06-13 16:42:31.766995
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    mock_environ = {
        b'SOME_KEY': b'de\xe4d\xf6c\xfci\xdfed\xf8\x9f',
        b'PYTHONIOENCODING': b'utf-8',
    }
    texts = _TextEnviron(mock_environ, encoding='utf-8')
    assert texts[b'SOME_KEY'] == u'de\xe4d\xf6c\xfci\xdfed\xf8\x9f'
    assert texts[b'PYTHONIOENCODING'] == 'utf-8'



# Generated at 2022-06-13 16:42:38.736683
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class TestEnv(MutableMapping):
        def __init__(self, values):
            self.data = values

        def __delitem__(self, key):
            del self.data[key]

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value

        def __iter__(self):
            return iter(self.data)

        def __len__(self):
            return len(self.data)

    # Check the identity transform on the environment vars
    test_environ = TestEnv({"FÖÖBAR": "BÄR", "BAZ": "QUX"})
    test_environ_text = _TextEnviron(test_environ)
   

# Generated at 2022-06-13 16:42:43.576145
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['TEST_VAR_1'] = '1'
    os.environ['TEST_VAR_2'] = '2'
    assert environ['TEST_VAR_1'] == '1'
    assert environ['TEST_VAR_2'] == '2'
    assert environ['TEST_VAR_1'] == '1'



# Generated at 2022-06-13 16:42:52.868442
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import six
    from ansible.module_utils.six.moves import builtins

    for encoding in ('utf-8', 'latin1'):
        for module_name in ('ansible.module_utils.common._collections_compat', 'six'):
            for py_version, compatibility in (
                    (3, True),
                    (6, True),
                    (7, True),
                    (8, True)
            ):
                env = {'A': 'B', 'utf8_key': 'utf8_value', 'utf8_key2': 'utfé'.encode('utf-8')}
                environ = _TextEnviron(env=env, encoding=encoding)

# Generated at 2022-06-13 16:43:03.383715
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from os import environ
    import unittest

    # Basic smoke test
    assert environ['PATH'] == os.environ['PATH']

    # Test that python2-unicode and python3-unicode are decoded to python3-unicode
    class UnicodeKv(unittest.TestCase):
        key = u'foo'
        deafult_value = u'bar'
        p2_unicode_value = 'agrz'
        p3_unicode_value = 'agrz'
        encoded_value = p2_unicode_value.encode('utf-8')

        def setUp(self):
            self._old_value = os.getenv(self.key, None)
            os.environ[self.key] = self.encoded_value


# Generated at 2022-06-13 16:43:12.023319
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    ansible/module_utils/python_version_compat.py:_TextEnviron._getitem_
    '''
    from ...pytest_common import CommonTesingClass

    class _TextEnvironTest(CommonTesingClass):
        def __init__(self):
            super(_TextEnvironTest, self).__init__()

            self.test_state = self.TestState()
            self.test_state.result = dict()
            self.test_state.obj = _TextEnviron()

        # check env.__getitem__(key)
        #
        # check that value is stored and returned when key is not in self._value_cache
        def test_getter_none(self):
            test_value = b'bar'
            # monkey patching
            self.test_state.obj._raw

# Generated at 2022-06-13 16:43:21.935381
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # The value of the environment variable 'ANSI_COLORS_DISABLED' needs some special handling
    # ansible_vault_password is set by the ansible-vault create command since v2.4, so don't set a
    # value in order to avoid stepping on the user's value
    env = {'ANSI_COLORS_DISABLED': '1', 'LC_ALL': 'C', 'HOME': '/home/auser'}

    environ = _TextEnviron(env)

    assert environ['ANSI_COLORS_DISABLED'] == '1'
    assert environ['LC_ALL'] == 'C'
    assert environ['HOME'] == '/home/auser'

    environ = _TextEnviron()

    assert environ['HOME'] == '/home/auser'

# Generated at 2022-06-13 16:43:28.503925
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test that __getitem__ returns text strings from the environment instead of byte strings and
    mimics the behaviour of os.environ on Python3
    """
    # The following code is from os.environ documentation:
    # https://docs.python.org/3/library/os.html#os.environ
    for k, v in environ.items():
        print('{0}={1}'.format(k, v))


# Generated at 2022-06-13 16:43:39.076723
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _():
        # Testing with a dict which contains both binary and text values
        an_env = _TextEnviron({'ansible_foo': '\x80', 'ansible_bar': u'\u1234'})
        assert an_env['ansible_foo'] == '\x80'
        assert an_env['ansible_bar'] == u'\u1234'

        # Testing with a dict which contains only binary values
        an_env = _TextEnviron({'ansible_foo': '\x80'})
        assert an_env['ansible_foo'] == '\x80'

        # Testing with a dict which contains only text values
        an_env = _TextEnviron({'ansible_foo': u'\u1234'})

# Generated at 2022-06-13 16:44:17.970063
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  # Test of all byte string keys
  byte_env = {}
  byte_env[b'ASCII_BYTE_STRING'] = to_bytes('test', errors='surrogate_or_strict')
  byte_env[b'UTF8_BYTE_STRING'] = to_bytes('b\xc3\xb8ker', encoding='utf-8', errors='surrogate_or_strict')
  byte_env[b'UTF8_BYTE_STRING_BAD'] = to_bytes('b\xc3\xb8ke\xc3', encoding='utf-8', errors='surrogate_or_strict')

# Generated at 2022-06-13 16:44:29.416040
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest.mock
    env = {b'BYTES': b'bytes'}
    text_env = _TextEnviron(env)

    with unittest.mock.patch('ansible.module_utils._text.to_text', new=lambda x, y, z: 'decoded %s' % x):
        assert 'decoded bytes' == text_env[b'BYTES']
        assert 'decoded bytes' == text_env['BYTES']
        assert 'decoded bytes' == text_env['BYTES']
        assert 1 == len(text_env._value_cache)
        text_env.encoding = 'encoding'
        assert 'decoded bytes' == text_env[b'BYTES']


# Generated at 2022-06-13 16:44:33.273397
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Run test to check if os.environ['TERM'] is returned as text.
    if PY3:
        assert isinstance(environ[to_text("TERM")], str)
    else:
        assert isinstance(environ[to_text("TERM")], unicode)

# Generated at 2022-06-13 16:44:41.456582
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import six

    env = _TextEnviron()

    # This works fine if we're on the same platform as the calling code
    # because native strings will get translated to the correct type
    env['FOO'] = 'foo'
    assert env['FOO'] == 'foo'

    # If we're not on the same platform, we'll have to manually convert
    # If we're on Python2 and the converted string is binary, we try to
    # perform a conversion
    env['FOO'] = to_bytes('foo', encoding='ascii')
    assert env['FOO'] == six.u('foo')

    # If the converted string is text, we don't try to convert it
    env['FOO'] = to_text(b'foo', encoding='ascii')
    assert env['FOO'] == six.u('foo')

   

# Generated at 2022-06-13 16:44:47.110256
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test __getitem__ with a non-unicode value
    environ[b'a'] = b'b'
    assert environ[b'a'] == 'b'

    # test __getitem__ with a unicode value
    environ[b'b'] = u'b'
    assert environ[b'b'] == u'b'



# Generated at 2022-06-13 16:44:57.379803
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest

    _TextEnviron.__getitem__(environ, "LANG")
    _TextEnviron.__getitem__(environ, "LANG")

    raw_environ = {b"LANG": b"blah"}
    environ = _TextEnviron(env=raw_environ, encoding='utf-8')
    text = _TextEnviron.__getitem__(environ, "LANG")
    assert type(text) is str
    assert text == "blah"

    raw_environ = {b"LANG": b"bl\xc3\xa4h"}
    environ = _TextEnviron(env=raw_environ, encoding='utf-8')
    text = _TextEnviron.__getitem__(environ, "LANG")
    assert type(text) is str

# Generated at 2022-06-13 16:45:05.373196
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # set the PY3 variable to False
    old_py3 = PY3
    PY3 = False
    # Set the os.environ
    old_env = os.environ
    os.environ = {'one': 'one', 'two': 'two'}
    # Inits a _TextEnviron
    environ = _TextEnviron()

    # assert that __getitem__ return the good value of the key in text
    assert environ['one'] == 'one'
    assert environ['two'] == 'two'

    # Set the os.environ to None
    os.environ = None

    # assert that __getitem__ raise a KeyError when the key is missing
    try:
        environ['three']
    except KeyError:
        assert True
    else:
        assert False

    # set

# Generated at 2022-06-13 16:45:07.081806
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == b'/Users/toshio'.decode('utf-8')


# Generated at 2022-06-13 16:45:07.724118
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    pass

# Generated at 2022-06-13 16:45:10.452452
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    v = _TextEnviron(encoding='ascii')
    v['a'] = 'b'
    assert v['a'] == u'b'
    assert isinstance(v['a'], text_type)