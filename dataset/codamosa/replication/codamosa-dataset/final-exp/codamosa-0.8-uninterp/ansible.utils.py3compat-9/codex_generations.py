

# Generated at 2022-06-13 16:36:00.899393
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Unit test for method __getitem__ of class _TextEnviron"""
    import re

    environ['ANSIBLE_TEST_KEY'] = '\xe6\x9b\x9c\xe6\x9e\x97'
    value = environ['ANSIBLE_TEST_KEY']
    assert isinstance(value, text_type), 'Value under key should be unicode'
    assert re.match(u'^\u66f9\u6d97$', value), 'Value under key should be Unicode for 曜林'



# Generated at 2022-06-13 16:36:06.053149
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    expected_value = 'test__TextEnviron___getitem__ value'
    environ['test__TextEnviron___getitem__'] = expected_value
    value = environ['test__TextEnviron___getitem__']
    assert value == expected_value


# Generated at 2022-06-13 16:36:12.892493
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unit test for method __getitem__ of class _TextEnviron
    from ansible.module_utils.six import u as unicode

    # define the environment with 'key1' as a unicode which will be evaluated as a byte string
    test_env = _TextEnviron({'key1': 'abcdé', 'key2': unicode('aé', 'utf-8')})
    assert test_env['key1'] == 'abcdé'
    assert test_env['key2'] == 'aé'


# Generated at 2022-06-13 16:36:23.348496
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make sure it can read a valid utf-8 env var
    os.environ[b'ANSIBLE_TEST_UTF8'] = u'\xe1\x88\xb4'.encode('utf-8')
    assert environ[b'ANSIBLE_TEST_UTF8'] == u'\xe1\x88\xb4'

    # Make sure it raises the right exception when the env var is invalid utf-8
    os.environ[b'ANSIBLE_TEST_UTF8'] = b'\xff\xff'
    try:
        environ[b'ANSIBLE_TEST_UTF8']
        assert False
    except UnicodeDecodeError:
        assert True

    # Make sure it can read a valid ascii only env var
    os.environ[b'ANSIBLE_TEST_ASCII']

# Generated at 2022-06-13 16:36:28.991058
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron

    :return:
    """
    environ = _TextEnviron({"PWD": "哈哈"})
    assert environ['PWD'] == b'\xe5\x93\x88\xe5\x93\x88'.decode('utf-8')


if __name__ == '__main__':
    test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:36:37.536265
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from collections import namedtuple
    from ansible.module_utils.six import text_type
    if PY3:
        for value in ['foo', 'bar', b'baz']:
            environ = _TextEnviron({'testkey': value}, encoding='utf-8')
            assert isinstance(environ['testkey'], text_type)
            assert environ['testkey'] == 'baz'
    else:
        EnvironKey = namedtuple('EnvironKey', ['key', 'decoded_value'])

# Generated at 2022-06-13 16:36:38.389309
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os_environ_getitem__test(environ)

# Generated at 2022-06-13 16:36:47.293963
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import PY3
    with_bom_u8 = b'\xff\xfe#\x00p\x00a\x00t\x00h\x00=\x00\xc3\xbe\xc3\xbe\xc3\xbe\xc3\xbe'
    with_bom_u16 = b'\xff\xfe#\x00p\x00a\x00t\x00h\x00=\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfe'

# Generated at 2022-06-13 16:36:49.343132
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'KEY': b'foobar'})
    assert env['KEY'] == 'foobar'



# Generated at 2022-06-13 16:36:52.758323
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # If key is present in environ, __getitem__ returns value of environ[key] as text
    assert environ['HOME'] == os.environ['HOME']


# Generated at 2022-06-13 16:37:03.931431
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Verify that it returns the expected value if the key exists in the dict

    # Build a mock environment
    env = {'key1': 'value1', 'key2': u'value2', 'key3': 'value3'.encode('utf-8')}
    # Build an instance of the class
    text_environ = _TextEnviron(env)
    # Verify all three keys are present, and in the expected encoding
    assert u'value1' == text_environ['key1']
    assert u'value2' == text_environ['key2']
    assert u'value3' == text_environ['key3']



# Generated at 2022-06-13 16:37:08.009401
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_env = {b'FOO': b'BAR'}
    text_env = _TextEnviron(raw_env)

    assert text_env[b'FOO'] == u'BAR'
    assert text_env['FOO'] == u'BAR'
    assert text_env[u'fOO'] == u'BAR'
    assert text_env[u'FOO'] == u'BAR'


# Generated at 2022-06-13 16:37:12.714086
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:37:20.954175
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({
        b"USER": b"foo",
        b"PASSWORD": b"PowerShell\xe2\x80\x93\xef\xbf\xbd\xef\xbf\xbd"
    })

    assert environ['USER'] == 'foo'
    assert environ['PASSWORD'] == 'PowerShell\u2013\ufffd\ufffd'


# Generated at 2022-06-13 16:37:27.772812
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(env={})

    # test non-unicode
    test_environ._raw_environ['non-unicode'] = 'non-unicode'

    if PY3:
        assert test_environ['non-unicode'] == 'non-unicode'  # noqa: F821
    else:
        assert test_environ['non-unicode'] == u'non-unicode'

    # test unicode
    test_environ._raw_environ['unicode'] = b'unicode'
    assert test_environ['unicode'] == u'unicode'

    # test surrogate-escape encoding
    test_environ._raw_environ['surrogate-escape-encoding'] = b'surrogate-escape-encoding\x80'
    assert test_

# Generated at 2022-06-13 16:37:28.848240
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'key': b'value'})
    assert environ['key'] == 'value'



# Generated at 2022-06-13 16:37:31.790007
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({'foo': 'bar'}, encoding='ascii')
    assert env['foo'] == u'bar'
    return


# Generated at 2022-06-13 16:37:42.274617
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()

    # Test with non-unicode keys and value
    key = 'DEPLOY_NOW_KEY'
    value = 'DEPLOY_NOW_VALUE'
    environ._raw_environ[key] = value

    # If os.environ is byte_string based, we need to decode using the specified encoding
    if PY3:
        assert environ[key] == value
    else:
        assert environ[key] == to_text(value)

    # Test with unicode keys and value
    key = u'DEPLOY_NOW_KEY_2'
    value = u'DEPLOY_NOW_VALUE_2'
    environ._raw_environ[key] = value

    # If os.environ is byte_string based, we need to decode using the specified encoding
   

# Generated at 2022-06-13 16:37:46.837598
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ1 = _TextEnviron(encoding='utf-8')
    environ2 = _TextEnviron(encoding='utf-8')

    environ1.__setitem__('name1', 'value1')
    environ2.__setitem__('name2', 'value2')

    # should be 'value1'
    assert environ1.__getitem__('name1') == 'value1'

    # should be 'value2'
    assert environ2.__getitem__('name2') == 'value2'


# Generated at 2022-06-13 16:37:55.846873
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import tempfile

    from ansible.module_utils.six import PY3

    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    if PY3:
        tmp_file.write(b'\xff')
    else:
        tmp_file.write(u'\uffff'.encode('utf-16'))
    tmp_file.close()

    os.environ['ANSIBLE_TEST_UTF16_FILE'] = tmp_file.name
    os.environ['ANSIBLE_TEST_UTF8_FILE'] = to_bytes(u'/\u2713')

    assert environ['ANSIBLE_TEST_UTF16_FILE'] == u'\uffff'
    assert environ['ANSIBLE_TEST_UTF8_FILE'] == u'/\u2713'

# Generated at 2022-06-13 16:38:02.477067
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # ============================================================================================
    #  test for __getitem__
    # ============================================================================================

    # Instance of class _TextEnviron
    text_environ = _TextEnviron(encoding='utf-8')
    text_environ.__setitem__('test_key', 'test_value')
    assert text_environ.__getitem__('test_key') == 'test_value'



# Generated at 2022-06-13 16:38:07.771431
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up
    env_orig = os.environ.copy()
    env_test = os.environ.copy()
    test_value = 'this is a test string'
    env_test[b'TEST_VALUE'] = test_value
    env = _TextEnviron(env=env_test, encoding='utf-8')

    # Run test
    result = env[b'TEST_VALUE']

    # Verify results & clean up
    assert result == test_value
    os.environ = env_orig



# Generated at 2022-06-13 16:38:09.304412
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['test'] = 'test'
    assert environ['test'] == 'test'

    # Check that we get correct values when values are not correctly encoded
    environ['test'] = u'\u0111'
    assert environ['test'] == u'\u0111'


# Generated at 2022-06-13 16:38:16.503617
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _test_getitem(environ):
        # Mimic a TestEnv that would be set up by a TestCase
        environ['ANSIBLE_TEST_DATA_ROOT'] = u'/usr/share/ansible/tests/data'

        if PY3:
            expected = u'/usr/share/ansible/tests/data'
            assert environ[u'ANSIBLE_TEST_DATA_ROOT'] == expected
            assert environ[b'ANSIBLE_TEST_DATA_ROOT'] == expected
        else:
            expected = u'/usr/share/ansible/tests/data'
            assert environ[u'ANSIBLE_TEST_DATA_ROOT'] == expected
            assert environ['ANSIBLE_TEST_DATA_ROOT'] == expected

    # Test os.environ as the base environ

# Generated at 2022-06-13 16:38:23.469749
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    global environ
    environ = _TextEnviron(encoding='utf-8')
    expected = u"é" * 200
    environ.__setitem__(u"TEST", expected)
    assert isinstance(environ.__getitem__(u"TEST"), str)
    assert environ.__getitem__(u"TEST") == expected


# Generated at 2022-06-13 16:38:32.989349
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()

    old_coding = sys.getfilesystemencoding()
    try:
        sys.setfilesystemencoding('ascii')
        assert env['PYTHONPATH'] == os.environ['PYTHONPATH']

        sys.setfilesystemencoding('utf-8')
        assert env['PYTHONPATH'] == os.environ['PYTHONPATH']

        sys.setfilesystemencoding('utf-8')
        os.environ['PYTHONPATH'] = u'uni\ufffd\ufffd\ufffdr\ufffds'
        assert env['PYTHONPATH'] == u'uni\ufffd\ufffd\ufffdr\ufffds'

    finally:
        sys.setfilesystemencoding(old_coding)

    #

# Generated at 2022-06-13 16:38:34.985739
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ["LANG"] = "fr_FR.utf8"
    assert environ["LANG"] == u'fr_FR.utf8'


# Generated at 2022-06-13 16:38:38.637314
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Tests method __getitem__ of class _TextEnviron

    :result: 3. Asserts are used to confirm that the yielded value is instance of
      :py:class:`str` and not :py:class:`bytes`
    """
    te = _TextEnviron({'ANSI_COLORS_DISABLED': '1'})
    assert isinstance(te['ANSI_COLORS_DISABLED'], str)

# Generated at 2022-06-13 16:38:42.126913
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron(env={b'A': b'B', 'C': 'D'})
    assert e['A'] == 'B'
    assert e['C'] == 'D'

# Generated at 2022-06-13 16:38:48.863280
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_test = _TextEnviron({})
    # Undecoded values are cached
    environ_test._raw_environ["foo"] = b'bar'
    assert environ_test['foo'] == 'bar'
    assert environ_test._value_cache[b'bar'] == 'bar'

    # Values are cached off of undecoded values
    environ_test._raw_environ["foo"] = b'baz'
    assert environ_test['foo'] == 'baz'
    assert environ_test._value_cache[b'bar'] == 'bar'
    assert environ_test._value_cache[b'baz'] == 'baz'


# Generated at 2022-06-13 16:38:59.268552
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if not PY3:
        # Transcode environment variables to bytes for Python2
        test_env = {key: to_bytes(value, encoding='utf-8', nonstring='strict',
                                  errors='surrogate_or_strict')
                    for key, value in os.environ.items()}
    else:
        test_env = os.environ
    test = _TextEnviron(env=test_env, encoding='utf-8')
    for key, value in os.environ.items():
        assert value == test[key]

# Generated at 2022-06-13 16:39:08.119528
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with a single byte string value
    environ_mock = {b'ANSIBLE_TEST_KEY': b'test-value'}
    text_environ = _TextEnviron(env=environ_mock)
    assert text_environ['ANSIBLE_TEST_KEY'] == 'test-value'

    # Test with a unicode string value
    environ_mock['ANSIBLE_TEST_KEY'] = b"\xc2\xa9"
    # Note: If the unicode is interpreted as a latin1 string, this is u'\xa9'
    assert text_environ['ANSIBLE_TEST_KEY'] == u'©'

    # Test with a variable changing during runtime
    environ_mock['ANSIBLE_TEST_KEY'] = b'test-value'
    assert text_en

# Generated at 2022-06-13 16:39:19.067979
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class Environ(MutableMapping):
        def __init__(self, *pairs, **kwargs):
            self.items = dict(*pairs, **kwargs)

        def __delitem__(self, key):
            del self.items[key]

        def __getitem__(self, key):
            return self.items[key]

        def __setitem__(self, key, value):
            self.items[key] = value

        def __iter__(self):
            return iter(self.items)

        def __len__(self):
            return len(self.items)

    import mock

    encodings = ('ascii', 'utf-8', 'utf-16')

# Generated at 2022-06-13 16:39:30.268575
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Current process's environment and the _TextEnviron object should be identical
    # for Python 3 since it supports unicode environment variables
    if PY3:
        assert(environ == os.environ)

    # In Python 2, the _TextEnviron object should return unicode, whereas the os module's object
    # returns bytes
    if not PY3:
        assert(type(environ['PATH']) is unicode)
        assert(type(os.environ['PATH']) is str)
        # The values in the two environment should be the same
        assert(environ['PATH'] == os.environ['PATH'])
        # Standard environment variables should be the same in both the raw environment and the
        # _TextEnviron object
        assert environ['PATH'] != u'Does not exist'
        assert environ['PATH'] != ''

# Generated at 2022-06-13 16:39:40.888111
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from tests.unit.compat import unittest
    '''
    _TextEnviron.__getitem__ returns text string.
    '''
    class Test___getitem__(unittest.TestCase):
        def setUp(self):
            self.expected_text = u'foo'
            self.expected_bytes = b'foo'
            self.expected_encoding = 'utf-8'
            self.expected_arg = 'foo_key'
            self.expected_result = u'bar'
            self.real_environ = {self.expected_arg : self.expected_bytes}
            self.test_environ = _TextEnviron(env=self.real_environ, encoding=self.expected_encoding)
            self.test_environ[self.expected_arg] = self.expected_text

       

# Generated at 2022-06-13 16:39:45.894195
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    return _TextEnviron({'str_ascii': 'ascii_string',
                         'str_latin1': u'latin1_string',
                         'str_utf8': u'utf8_string',
                         'bytes_ascii': b'ascii_bytes',
                         'bytes_latin1': b'latin1_bytes',
                         'bytes_utf8': b'utf8_bytes'}, 'utf-8')



# Generated at 2022-06-13 16:39:56.641138
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Mock os.environ
    del environ._raw_environ
    environ._raw_environ = dict((to_bytes(key, 'utf-8', 'strict'), to_bytes(value, 'utf-8', 'strict')) for key, value in {
        'ascii_key': 'ascii_value',
        'latin1_key': 'latin1_äöü',
        'utf8_key': 'utf8_üñíçóé',
    }.items())

    assert environ['ascii_key'] == 'ascii_value'
    assert environ['latin1_key'] == 'latin1_äöü'
    assert environ['utf8_key'] == 'utf8_üñíçóé'

# Generated at 2022-06-13 16:40:02.000784
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'key1': b'value1', b'key2': b'value2',
                        u'key3': u'value3', b'key4': u'value4'})

    assert env['key1'] == u'value1'
    assert env['key2'] == u'value2'
    assert env['key3'] == u'value3'
    assert env['key4'] == u'value4'


# Generated at 2022-06-13 16:40:11.216105
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class Environ(object):
        def __init__(self):
            # Population of os.environ for testing
            self.var1 = 'value1'
            self.var2 = u'value2'
            self.var3 = 'value3'
            self.var4 = u'value4'
            self.var5 = 'value5'
            self.var6 = u'value6'
            self.var7 = 'value7'
            self.var8 = 'value8'
            self.var9 = u'value9'
            self.var10 = u'value10'
            self.var11 = 'value11'
            self.var12 = 'value12'
            # This is a bad value that should error out when strict decoding is used.

# Generated at 2022-06-13 16:40:19.614554
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    getitem_args = [
        {'key': 'GIT_ASKPASS', 'value': os.environ['GIT_ASKPASS']},
        {'key': 'GIT_ASKPASS', 'value': 'something_else'},
    ]
    for kwargs in getitem_args:
        text_environ = _TextEnviron(
            env={kwargs['key']: kwargs['value']},
            encoding='utf-8',
        )
        assert isinstance(text_environ[kwargs['key']], unicode), \
            '_TextEnviron.__getitem__ method did not return unicode string on Python2'

# Generated at 2022-06-13 16:40:27.006828
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Create the object
    text_environ = _TextEnviron(env=None, encoding='utf-8')

    # Test the cases
    assert text_environ['LANG'] == u'en_US.UTF-8'
    assert text_environ.get('LANG') == u'en_US.UTF-8'

# Generated at 2022-06-13 16:40:35.924301
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Subtest_1
    # test that a unicode key will retrieve a unicode value
    os.environ['unicode'] = 'bar'
    assert environ['unicode'] == 'bar'
    assert type(environ['unicode']) != bytes

    # Subtest_2
    # test that a byte key will retrieve a unicode value
    os.environ['byte'] = 'bar'.encode()
    assert environ['byte'] == 'bar'
    assert type(environ['byte']) != bytes

    # Subtest_3
    # test that a unicode key using a non-default encoding will not retrieve a unicode value
    os.environ['unicode'] = 'bar'
    environ_unicode = _TextEnviron({'unicode': 'bar'}, encoding='latin-1')
    assert en

# Generated at 2022-06-13 16:40:43.262176
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PWD'] == '/home/peter'
    os.environ['PWD'] = '/home/peter'.encode('utf-8')
    assert environ['PWD'] == '/home/peter'

    # We don't have any way to force an ASCII path into the environment.  But we can at least test
    # that we can retrieve ASCII paths from the environment
    assert environ['PWD'] == '/home/peter'

    # Test decoding path with multi-byte characters
    os.environ['PWD'] = '/home/pěter'.encode('utf-8')
    assert environ['PWD'] == '/home/pěter'

    del os.environ['PWD']

# Generated at 2022-06-13 16:40:53.156834
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Encoding test, non-Unicode text in value
    environ['TEST_VAR_1'] = 'Développé'
    assert environ['TEST_VAR_1'] == u'Développé'

    # Encoding test, Unicode text in value
    environ['TEST_VAR_2'] = u'Développé'
    assert environ['TEST_VAR_2'] == u'Développé'

    # Encoding test, byte strings in value, UTF-8 encoded
    environ['TEST_VAR_3'] = b'D\xc3\xa9velopp\xc3\xa9'
    assert environ['TEST_VAR_3'] == u'Développé'

    # Encoding test, byte strings in value, ISO-

# Generated at 2022-06-13 16:40:58.882917
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    byte_val = {u'byte_val': to_bytes(u'has non-ascii: é', encoding='utf-8')}
    text_val = {u'text_val': u'has non-ascii: é'}
    test_environ = _TextEnviron(byte_val)

    for key in byte_val:
        assert test_environ[key] == text_val[key]

# Generated at 2022-06-13 16:41:00.751293
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_STRING'] = 'test_string'
    assert environ['TEST_STRING'] == u'test_string'



# Generated at 2022-06-13 16:41:12.425747
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    key = 'test_key'
    ascii_value = u'ascii'
    ascii_bytes = b'ascii'
    utf8_value = u'\u3053\u3093\u306b\u3061\u306f'
    utf8_bytes = u'\u3053\u3093\u306b\u3061\u306f'.encode('utf-8')
    u8_environ = _TextEnviron(encoding='utf-8')
    ascii_environ = _TextEnviron(encoding='ascii')
    # Test for PY2
    if not PY3:
        # Test the utf8 value on PY2
        u8_environ[key] = utf8_bytes
        assert utf8_value

# Generated at 2022-06-13 16:41:13.319082
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ[b'TEST'] == 'test'

# Generated at 2022-06-13 16:41:15.129675
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    If a value is already decoded to text, then return the cached value
    """
    environ._value_cache['foo'] = 'bar'
    assert environ['foo'] == 'bar'



# Generated at 2022-06-13 16:41:25.995273
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # value = string
    # key = string, value = string
    from ansible.module_utils.six import u
    test_env = _TextEnviron({'string': 'string'}, 'utf-8')
    assert test_env['string'] == u('string')

    # key = bytes, value = string
    test_env = _TextEnviron({b'string': 'string'}, 'utf-8')
    assert test_env['string'] == u('string')

    # key = string, value = bytes
    test_env = _TextEnviron({'string': b'string'}, 'utf-8')
    assert test_env['string'] == u('string')

    # key = bytes, value = bytes

# Generated at 2022-06-13 16:41:38.798463
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Create an instance of _TextEnviron
    environ = _TextEnviron()
    # getenv() returns bytes on Python 2
    if not PY3:
        env_value = environ[b'HOME']

    # getenv() returns text on Python 3
    if PY3:
        env_value = environ['HOME']

    # getenv() returns text on Python 2 with an encoding of utf-8
    if not PY3:
        environ = _TextEnviron(encoding='utf-8')
        env_value = environ[b'HOME']

    # getenv() returns text on Python 2 with an encoding of latin1
    if not PY3:
        environ = _TextEnviron(encoding='latin1')
        env_value = environ[b'HOME']

# Generated at 2022-06-13 16:41:45.939852
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    sys.path.append('../')
    from test.unit.module_utils.common._collections_compat import unittest, Mock

    class TestCase(unittest.TestCase):
        def test__getitem__():
            # Arrange
            expected_result = 'unit_test_result'

            # Act
            unit_under_test = _TextEnviron(os.environ, encoding='utf-8')
            actual_result = unit_under_test.__getitem__('LANG')

            # Assert
            self.assertEqual(actual_result, expected_result)

    # Kick off unittest
    mock_obj = Mock()
    mock_obj.unit_test_result = 'unit_test_result'
    mock_obj.environ = {'LANG': 'unit_test_result'}

# Generated at 2022-06-13 16:41:56.941743
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test for method __getitem__ of class _TextEnviron
    """
    from ansible.module_utils.common._collections_compat import MutableMapping
    import os
    import types

    te = _TextEnviron()
    assert isinstance(te, MutableMapping), '_TextEnviron isinstance check failed'

    os.environ[b'TEST_VAR'] = b'\xe0\xe1\xe2'
    assert te['TEST_VAR'] == u'\xe0\xe1\xe2', '_TextEnviron "TEST_VAR" getattr value failed'

    os.environ[b'TEST_VAR_1'] = b'\x00\x00\x00'

# Generated at 2022-06-13 16:42:06.852447
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from unittest.mock import MagicMock
    mock_environ = MagicMock()
    mock_environ.__getitem__.return_value = '{{ test }}'
    mock_environ.__setitem__ = MagicMock()
    mock_environ.__delitem__ = MagicMock()
    mock_environ.__contains__ = MagicMock()
    mock_environ.__iter__ = MagicMock()
    mock_environ.__len__ = MagicMock()
    text_environ = _TextEnviron(env=mock_environ)
    assert text_environ['test'] == '{{ test }}'
    mock_environ.__getitem__.assert_called_with('test')

# Generated at 2022-06-13 16:42:17.602541
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes, to_unicode
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.converters import to_str
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.text import to_bytes
    from ansible.module_utils.common.text import to_text
    from ansible.module_utils.common.text import to_native
    from ansible.module_utils.common.text import to_str
    to_bytes('foo')
    to_text('foo')
    to_native('foo')
    to

# Generated at 2022-06-13 16:42:22.259563
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_encoding = 'ascii'
    e = _TextEnviron(encoding=test_encoding)
    assert e['HOME'] == '{}'.format(os.getenv(b'HOME').decode(test_encoding))
    assert e['HOME'] == '{}'.format(os.getenv('HOME'))



# Generated at 2022-06-13 16:42:26.089770
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    env['key1'] = b'\xd6\xd0\xce\xc4'
    assert 'key1' in env
    assert env['key1'] == '\u4f60\u4f60'
    assert isinstance(env['key1'], str)
    del env['key1']

# Generated at 2022-06-13 16:42:34.180762
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test with regular ascii char
    environ['KEY1'] = 'ab'
    assert environ['KEY1'] == u'ab'

    # Test with bytestring
    environ_bytestring = _TextEnviron(encoding='iso-8859-1')
    environ_bytestring['KEY2'] = 'ab'
    assert environ_bytestring['KEY2'] == u'ab'

    # Test with unicode char
    environ_unicode = _TextEnviron(encoding='us-ascii')
    environ_unicode['KEY3'] = u'\xab'
    assert environ_unicode['KEY3'] == u'\ufffd'

    environ_unicode_utf8 = _TextEnviron(encoding='utf-8')
    environ_unicode_

# Generated at 2022-06-13 16:42:38.036476
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Setup
    env = _TextEnviron({b'FOO': b'bar'})

    # Test
    assert env['FOO'] == u'bar'

# Generated at 2022-06-13 16:42:42.787632
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Case 1: Key present
    environ = _TextEnviron({'key': 'value'})
    assert environ['key'] == 'value'

    # Case 2: Key not present
    try:
        environ['key']
        raise AssertionError('Expected KeyError')
    except KeyError:
        # Expected
        pass


# Generated at 2022-06-13 16:42:57.642912
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class MockOs():
        def __init__(self):
            self.env = {
                'a': b'a',
                'b': 'b'
            }

        def __getitem__(self, key):
            return self.env[key]

    class MockSys():
        def __init__(self):
            self.encoding = 'utf-8'

        def getfilesystemencoding(self):
            return self.encoding

    env = _TextEnviron(encoding='utf-8', env=MockOs())
    sys_mock = MockSys()
    sys.getfilesystemencoding = sys_mock.getfilesystemencoding
    assert env['b'] == 'b'
    assert env['a'] == u'a'

# Generated at 2022-06-13 16:43:05.903910
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Assign the global variable 'environ' to local variable '_environ'
    _environ = environ

    # Set the encoding of attribute '_environ' to 'gbk'
    _environ.encoding = 'gbk'

    # Assign a copy of the global variable 'os.environ' to local variable '_raw_environ'
    _raw_environ = dict(os.environ)

    # Build a dictionary variable named 'env' with two items:
    # ('key1', 'value1') and ('key2', 'value2')
    env = dict(key1='value1', key2='value2')

    # Append to the global variable 'os.environ' two items: ('key1', 'value1') and ('key2', 'value2')
    os.environ.update(env)

# Generated at 2022-06-13 16:43:18.158805
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['unicode_key'] = 'UTF-8_à_é_ì_ö_ù_ñ_ç'
    os.environ['str_key'] = 'ISO-8859-1_à_é_ì_ö_ù_ñ_ç'
    os.environ['bytes_key'] = 'ISO-8859-1_à_é_ì_ö_ù_ñ_ç'.encode('iso-8859-1')

    # Test with UTF-8 encoded key and no cache
    os.environ.pop('bytes_key')
    env = _TextEnviron()
    assert env['unicode_key'] == 'UTF-8_à_é_ì_ö_ù_ñ_ç'

# Generated at 2022-06-13 16:43:24.829078
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # unit test to ensure proper functionality of method __getitem__ of class _TextEnviron
    ut_test_name = 'test__TextEnviron___getitem__()'
    ut_test_description = 'unit test to ensure proper functionality of method __getitem__ of class _TextEnviron'
    print("\n")
    print("### Performing test : " + ut_test_name + " ###")
    print("\n")
    print("Description of test : " + ut_test_description + "\n")
    print("\n")

# Generated at 2022-06-13 16:43:30.347730
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    raw_environ = {
        b'ANSIBLING_NULL': '',
        b'ANSIBLING_VOID': None,
        b'ANSIBLING_BAD': b'\xe9',
        b'ANSIBLING_GOOD': 'ansible',
    }
    environ_ = _TextEnviron(raw_environ)
    assert environ_['ANSIBLING_NULL'] == ''

# Generated at 2022-06-13 16:43:34.874851
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['blah'] = 'abc'
    assert environ['blah'] == 'abc'

    environ['blah'] = b'abc'
    assert environ['blah'] == 'abc'

    environ['blah'] = u'abc'
    assert environ['blah'] == 'abc'


# Generated at 2022-06-13 16:43:44.365724
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test scenario:
        - test __getitem__ with different values
        - test __setitem__ with different values
    """
    result_getitem = _TextEnviron()['PATH']
    assert result_getitem == '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    result_setitem_new = _TextEnviron()
    result_setitem_new['test'] = 'value'
    assert result_setitem_new['test'] == 'value'
    result_setitem_existing = _TextEnviron()
    result_setitem_existing['test'] = 'newvalue'
    assert result_setitem_existing['test'] == 'newvalue'



# Generated at 2022-06-13 16:43:52.523544
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that it works with utf-8
    environ = _TextEnviron({'ascii': b'ascii', 'unicode': b'unicode\xc3\xaf\xc2\xbb\xc2\xbf'},
                           encoding='utf-8')
    assert environ['ascii'] == 'ascii'
    assert environ['unicode'] == 'unicodeï»¿'

    # Check that it works with japanese

# Generated at 2022-06-13 16:43:54.564767
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'ANSIBLE_SHOW_CUSTOM_STATS': b'true'})
    assert env[b'ANSIBLE_SHOW_CUSTOM_STATS'] == u'true'

# Generated at 2022-06-13 16:43:57.465908
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ['ANSIBLE_TEST_TEXT_ENVIRON_VALUE'] = '汉字'
    try:
        assert environ['ANSIBLE_TEST_TEXT_ENVIRON_VALUE'] == '汉字'
    except UnicodeDecodeError:
        raise AssertionError("_TextEnviron is not encoding the values into text")



# Generated at 2022-06-13 16:44:17.389899
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Check that we return unicode strings
    environ = _TextEnviron(encoding='utf-8')
    assert isinstance(environ['HOME'], unicode)
    # Check that we return the same value despite the cache being initially empty
    assert environ['HOME'] == environ['HOME']
    # Changing the encoding should change what is returned
    environ = _TextEnviron(encoding='latin1')
    assert environ['HOME'] == u'C:\\Users\\toshio'
    # Changing the environment variable should change what is returned
    os.environ['HOME'] = 'foobar'
    assert environ['HOME'] == u'foobar'
    # Changing the encoding should also change what is returned
    environ = _TextEnviron(encoding='latin1')
    assert environ['HOME'] == u''

# Generated at 2022-06-13 16:44:22.266682
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron

    A good string should return a text object that matches the input.
    """
    os.environ['FOO'] = 'a'
    text_environ = _TextEnviron()
    assert text_environ['FOO'] == 'a'


# Generated at 2022-06-13 16:44:33.572141
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  from io import BytesIO

# Generated at 2022-06-13 16:44:41.619794
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set some dummy environment variables
    environ['myvar1'] = 'myval1'
    environ['myvar2'] = 'myval2'

    # Set some bad bytes in environment variables
    environ['myvar3'] = '\x00\x01\x02'  # Bad bytes with no encoding
    environ['myvar4'] = '\x00\x01\x02'.encode('latin1')  # Bad bytes with latin1 encoding
    environ['myvar5'] = '\x00\x01\x02'.encode('utf-8')  # Bad bytes with utf-8 encoding

    # Test the normal case of an environment variable containing text
    assert environ['myvar1'] == 'myval1'

    # Test the normal case of an environment variable containing unicode

# Generated at 2022-06-13 16:44:49.810940
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    unit test for method __getitem__ of class _TextEnviron
    '''

    # environment variable with utf-8 value
    key = 'TEST_VAR'
    value = 'はじめまして。よろしくお願いします'
    environ[key] = value
    assert value == environ[key]

    # environment variable with non-utf-8 value
    key = 'TEST_VAR'
    value = b'\x90\x90\x90\x90\x90'
    environ[key] = value
    assert value == environ[key]

# Generated at 2022-06-13 16:44:53.836053
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # values in environment are byte strings
    if not PY3:
        assert isinstance(environ['PWD'], unicode)
    # values in environment are unicode strings
    else:
        assert isinstance(environ['PWD'], str)


# Generated at 2022-06-13 16:45:03.413518
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:45:08.622400
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    expected_result = u'\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442'
    os.environ['key'] = expected_result
    # Act
    result = _TextEnviron()['key']
    # Assert
    assert result == expected_result


# Generated at 2022-06-13 16:45:19.888549
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for the method __getitem__ of the class _TextEnviron

    The __getitem__ method is the most complex method of the _TextEnviron class.  The tests here
    are to validate that it works correctly and behaves like the os.environ on Python3.

    The test cases in this method were verified by running the equivalent code on Python2 and
    Python3.
    """
    # Test case 1: String key that exists in the environment
    # Expected result: key returns the value from the environment as a string with unicode
    # characters in it.
    assert isinstance(environ['HOME'], str)
    assert u'-' in environ['HOME']

    # Test case 2: Non-string key (ex. bool) that exists in the environment
    # Expected result: KeyError is raised
    import pytest
   

# Generated at 2022-06-13 16:45:23.713833
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({b'key-bytes': b'value-bytes', 'key-text': 'value-text'})
    assert test_environ['key-bytes'] == 'value-bytes'
    assert test_environ['key-text'] == 'value-text'



# Generated at 2022-06-13 16:45:57.557386
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import text_type
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six._six import b

    environ = _TextEnviron(encoding='utf-8')

    if PY3:
        # If we're on Python3 os.environ should be a text_type dictionary
        assert isinstance(os.environ, text_type)
    else:
        # If we're on Python2 os.environ should be a byte string dictionary
        assert isinstance(os.environ, MutableMapping)

    assert isinstance(environ, MutableMapping)
    if 'PYTHONPATH' in os.environ:
        del os.environ['PYTHONPATH']
    os.environ['PYTHONPATH']