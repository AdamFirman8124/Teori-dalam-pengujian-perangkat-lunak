

# Generated at 2022-06-13 16:35:58.175395
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from os import environ
    from os import putenv
    from sys import getfilesystemencoding
    from sys import setfilesystemencoding
    from unittest import TestCase
    from six import PY2, PY3, text_type

    # PY3: no-op
    if PY3:
        print('Python 3. Do nothing.')
        return

    # Set up initial env with text values
    environ.update(
        {
            'STR1': 'abcdef',
            'STR2': 'abcdef',
            'STR3': '\xc2\x80',
            'STR4': '\xe3\x81\x82',
        }
    )

    # Mock-up (1) PY2 with system encoding = utf-8, (2) PY2 with system encoding = cp9

# Generated at 2022-06-13 16:35:59.820396
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    environ['test'] = 'test'
    assert isinstance(environ['test'], str)



# Generated at 2022-06-13 16:36:06.675565
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    os.environ["FOO"] = '\xa3'
    try:
        te = _TextEnviron(encoding="iso-8859-15")
        assert te['FOO'] == u'¤'
        te2 = _TextEnviron(env=te, encoding="latin-1")
        assert te2['FOO'] == u'Â£'
    finally:
        del os.environ["FOO"]



# Generated at 2022-06-13 16:36:10.190194
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _env = _TextEnviron(encoding='utf-8')
    for key, value in os.environ.items():
        assert _env[key] == to_text(value, encoding='utf-8')


# Generated at 2022-06-13 16:36:16.114435
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    env['LANG'] = 'en_US.UTF-8'
    assert to_text(env['LANG']) == u'en_US.UTF-8'
    env['LANG'] = u'en_US.UTF-8'
    assert to_text(env['LANG']) == u'en_US.UTF-8'


# Generated at 2022-06-13 16:36:19.271106
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Arrange
    # Act
    output = type(environ).__name__
    # Assert
    assert output == '_TextEnviron'

# Generated at 2022-06-13 16:36:20.773605
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ["TEST"] = "test"

    assert environ["TEST"] == u"test"

# Generated at 2022-06-13 16:36:32.026059
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:36:38.193795
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test using str as the key
    assert environ['PATH'] == '/bin:/usr/bin'

    # Test using bytes as the key
    assert environ[b'PATH'] == '/bin:/usr/bin'

    # Test non-existent key
    try:
        environ['ANSIBLE_TEST']
        assert False, "An exception should have been raised"
    except KeyError:
        pass

    # Test overwriting an environment variable
    environ['ANSIBLE_TEST'] = 'xyz'
    assert environ['ANSIBLE_TEST'] == 'xyz'



# Generated at 2022-06-13 16:36:46.129966
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with PY3
    environ._raw_environ = {b'ANSIBLE_HOST_KEY_CHECKING': b'true'}
    environ._value_cache = {}
    assert environ.__getitem__(b'ANSIBLE_HOST_KEY_CHECKING') == u'true'
    assert len(environ._value_cache) == 0

    # Test with PY2
    environ._raw_environ = {}
    environ._value_cache = {}
    environ._raw_environ[b'ANSIBLE_HOST_KEY_CHECKING'] = b'true'
    assert environ.__getitem__(b'ANSIBLE_HOST_KEY_CHECKING') == u'true'
    assert len(environ._value_cache) == 1

# Generated at 2022-06-13 16:36:56.231593
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = os.environ.copy()
    env[u'foo'] = u'bar'
    env[b'foo2'] = b'bar2'
    env[b'foo3'] = u'bar3'
    env[b'foo4'] = u'\u00e9'
    env[b'foo5'] = b'\xc3\xa9'
    text_environ = _TextEnviron(env)
    assert text_environ[u'foo'] == u'bar'
    assert text_environ[b'foo2'] == u'bar2'
    assert text_environ[b'foo3'] == u'bar3'

# Generated at 2022-06-13 16:37:00.377923
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['test_var'] = 'test_value'
    assert environ['test_var'] == 'test_value'
    assert environ._value_cache['test_value'] == 'test_value'


# Generated at 2022-06-13 16:37:05.049446
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert environ['PATH'] == os.environ['PATH']  # string test
    assert environ['PATH'] != os.environ[b'PATH']  # bytes-string test
    assert environ['PATH'] != os.environ[u'PATH']  # unicode-string test
    assert environ['PATH'] == os.environ.get('PATH')  # get method
    assert environ['PATH'] != os.environ.get(b'PATH')  # get method with bytes
    assert environ['PATH'] != os.environ.get(u'PATH')  # get method with unicode
    # Test that method does not do any key transformations
    # (e.g. convert to lowercase)
    # get method

# Generated at 2022-06-13 16:37:15.087568
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['foo'] = u'bar'
    assert environ['foo'] == u'bar'
    assert type(environ['foo']) == unicode, u'environ[u\'foo\'] should be unicode'
    assert type(environ['foo']) is not str, u'environ[u\'foo\'] should not be str'

    # Test surrogateescape
    environ['baz'] = u'\udc75'.encode('utf-16-le')
    assert type(environ['baz']) == unicode, u'environ[u\'baz\'] should be unicode'
    assert type(environ['baz']) is not str, u'environ[u\'baz\'] should not be str'

# Generated at 2022-06-13 16:37:17.557957
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ__getitem__('PATH') == environ__getitem__('PATH')


# Generated at 2022-06-13 16:37:24.689725
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'foo': b'bar', b'bar': b'foo'}, encoding='utf-8')
    assert env[b'foo'] == u'bar'
    assert env[u'foo'] == u'bar'
    # Any iterable object should be accepted
    assert env[(1, 2, 3)] == u'foo'
    # But only the equivalent text form of the binary key will work
    # This is to mimic the same behaviour as os.environ
    assert env[b'bar'] == u'foo'
    assert env[u'bar'] != u'foo'


# Generated at 2022-06-13 16:37:35.858533
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from .common import TestCase

    class Test_TextEnviron(TestCase):
        def setUp(self):
            super(Test_TextEnviron, self).setUp()
            self.environ = _TextEnviron()

        def test__TextEnviron___getitem__(self, ):
            env = dict(LANG='C', LANGUAGE='de_DE', LC_ALL='en_US.UTF8')

            self.environ = _TextEnviron({k: to_bytes(v, encoding='utf-8', errors='strict')
                                         for k, v in env.items()})
            self.assertEqual(env['LANG'], self.environ['LANG'])
            self.assertEqual(env['LANGUAGE'], self.environ['LANGUAGE'])

# Generated at 2022-06-13 16:37:44.564274
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # ******************************************************************************
    # *                            Happy path tests                               *
    # ******************************************************************************
    # Testing raw byte strings decoded to python string using utf-8
    os.environ['UTF8_PY'] = b'\xc3\x80'
    assert environ['UTF8_PY'] == 'À'

    # Testing raw byte strings decoded to unicode string using latin-1
    os.environ['LATIN1_PY'] = b'\xc0'
    assert environ['LATIN1_PY'] == 'À'

    # Testing raw byte strings decoded to unicode string using utf-16-be
    os.environ['UTF16BE_PY'] = b'\x00\xc0'

# Generated at 2022-06-13 16:37:53.886749
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test 1: test int
    try:
        test_environ = _TextEnviron({'test_int': '1'})
        result = test_environ['test_int']
        assert result == '1', "test__TextEnviron___getitem__(): Fail: Returned value is not 1"
    except (AssertionError, Exception):
        print("test__TextEnviron___getitem__(): Fail")
    else:
        print("test__TextEnviron___getitem__(): Pass")

    # Test 2: test string

# Generated at 2022-06-13 16:38:01.364444
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Test return value type and value of method __getitem__ of class _TextEnviron
    """
    my_env = _TextEnviron(encoding='utf-8')
    if sys.version_info[0] == 2:
        assert isinstance(my_env['HOME'], unicode)
        assert my_env['HOME'] == u'C:\\Users\\toshio'
    elif sys.version_info[0] == 3:
        assert isinstance(my_env['HOME'], str)
        assert my_env['HOME'] == 'C:\\Users\\toshio'



# Generated at 2022-06-13 16:38:09.050908
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ[b"PATH"].__class__ == str

    # Test that pre-encoded unicode gets preserved
    environ[b"ANSIBLE_TEST_KEY"] = "Voil\xc3\xa0!"

    # Test that post-encoded unicode works
    environ["ANSIBLE_TEST_KEY_2"] = to_bytes("Voil\xc3\xa0!", encoding="utf-8")

    # Test that bytes get converted
    environ["ANSIBLE_TEST_KEY_3"] = b"Voil\xc3\xa0!"
    assert environ["ANSIBLE_TEST_KEY"] == "Voil\xc3\xa0!"
    assert environ["ANSIBLE_TEST_KEY_2"] == "Voil\xc3\xa0!"

# Generated at 2022-06-13 16:38:14.071315
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST'] = 'test'
    assert environ['TEST'] == 'test'
    assert type(environ['TEST']) is str

    environ['TEST'] = 'あいうえお'
    assert environ['TEST'] == 'あいうえお'
    assert type(environ['TEST']) is str



# Generated at 2022-06-13 16:38:22.802624
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test unicode encoding
    os.environ['str_utf8'] = '\xe3\x82\xb0\xe3\x83\xbc\xe3\x82\xb0\xe3\x83\xab'.decode('utf-8')
    assert environ['str_utf8'] == u'グーグル'

    # Test non-unicode encoding
    os.environ['str_ascii'] = 'test'
    assert environ['str_ascii'] == u'test'


# Generated at 2022-06-13 16:38:32.880063
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test text env var
    assert 'HELLO' == environ['HELLO']
    # Test adding non-ASCII env var
    try:
        del environ['HELLO']
    except KeyError:
        pass
    environ['HELLO'] = 'H€LLØ'
    assert 'H€LLØ' == environ['HELLO']
    # Test accessing an env var which was added after we started running
    del environ['HELLO']
    os.environ['HELLO'] = 'H€LLØ'
    assert 'H€LLØ' == environ['HELLO']
    # Test accessing an env var which was added after we started running
    os.environ['HELLO'] = 'HELLO'

# Generated at 2022-06-13 16:38:35.447491
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ["TEST_KEY"] = "test_x"
    environ = _TextEnviron(env=os.environ, encoding='UTF-8')
    assert environ["TEST_KEY"] == "test_x"


# Generated at 2022-06-13 16:38:40.085368
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {'a': '1\x80', 'b': '2'}
    environ._value_cache = {}
    assert environ['a'] == u'1\ufffd'

# Generated at 2022-06-13 16:38:42.409040
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    assert isinstance(env['PATH'], str)

# Generated at 2022-06-13 16:38:49.865119
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Variables
    input_environ = {
        'key1': 'value1',
        'key2': 'value2'.encode('utf-8'),
        'key3': 'value3'.encode('GBK'),
        'key4': 'value4'.encode('utf-8', 'surrogateescape'),
    }

    expected_environ = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
    }

    # Assertions
    environ = _TextEnviron(env=input_environ, encoding='utf-8')
    for key in expected_environ:
        value = environ[key]
        assert isinstance(value, str)

# Generated at 2022-06-13 16:38:54.036569
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    try:
        os.environ[u'test_utf8'] = u'test_value'
        assert env[u'test_utf8'] == u'test_value'
    finally:
        del os.environ[u'test_utf8']



# Generated at 2022-06-13 16:39:04.899314
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os

    # Normal string
    os.environ['test_string'] = 'test'
    assert environ['test_string'] == 'test'

    # UTF-8 encoded string
    os.environ['test_string'] = '\xc3\x89'
    assert environ['test_string'] == u'\u00c9'

    # Latin-1 encoded string
    os.environ['test_string'] = '\xc9'
    assert environ['test_string'] == u'\u00c9'

    # Bad UTF-8 encoded string
    os.environ['test_string'] = '\x80'
    try:
        environ['test_string']
    except UnicodeDecodeError:
        pass
    else:
        raise Exception('UnicodeDecodeError not raised')


# Generated at 2022-06-13 16:39:15.783107
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Unit test for method __getitem__ of class _TextEnviron
    # NOTE: This method is used for Ansible to unify the behavior of Py2 and 3.
    #       This test is used to check that it mimics the behavior of Py3.

    env = _TextEnviron(env={})
    env[u"\u732b\u304b\u304c\u304d"] = u"\u304f\u304e\u304d\u3053"
    assert env[u"\u732b\u304b\u304c\u304d"] == u"\u304f\u304e\u304d\u3053"

    env = _TextEnviron(env={"key": "value"})
    assert env[u"key"] == u"value"

    env = _TextEn

# Generated at 2022-06-13 16:39:17.294858
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == u'/home/user'


# Generated at 2022-06-13 16:39:29.169242
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:39:37.157183
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Note: This test will actually modify environ.  In some cases, this may break other unit
    # tests.  We may want to change this to use a special environ object whose getitem() is
    # overridden to return the right data instead to avoid these conflicts.
    test_data = [
        ('PYTHONIOENCODING', 'utf-8'),
        ('LC_ALL', 'UTF-8'),
        ('LC_CTYPE', 'UTF-8'),
        (b'PYTHONIOENCODING', 'utf-8'),
        (b'LC_ALL', 'UTF-8'),
        (b'LC_CTYPE', 'UTF-8'),
    ]
    for key, expected in test_data:
        environ[key] = expected

# Generated at 2022-06-13 16:39:42.322859
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({
        'one': '1',
        to_bytes('two'): to_bytes('2'),
    })
    assert test_environ['one'] == '1'
    assert test_environ['two'] == '2'
    assert test_environ[to_bytes('one')] == '1'  # pylint: disable=unsubscriptable-object
    assert test_environ[to_bytes('two')] == '2'  # pylint: disable=unsubscriptable-object
    test_environ.encoding = 'utf-8'
    assert test_environ[to_bytes('one')] == '1'  # pylint: disable=unsubscriptable-object
    assert test_environ[to_bytes('two')] == '2' 

# Generated at 2022-06-13 16:39:54.985641
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # 1. UTF-8 encoded bytestring
    os.environ[to_bytes('test__TextEnviron___getitem__', encoding='ascii')] = to_bytes('\xe9')
    assert environ[to_bytes('test__TextEnviron___getitem__', encoding='ascii')] == u'\xe9'
    del os.environ[to_bytes('test__TextEnviron___getitem__', encoding='ascii')]

    # 2. Non UTF-8 encoded bytestring
    os.environ[to_bytes('test__TextEnviron___getitem__', encoding='ascii')] = to_bytes('\xff')
    assert environ[to_bytes('test__TextEnviron___getitem__', encoding='ascii')] == u'\xff'
    del os.en

# Generated at 2022-06-13 16:40:01.663552
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _compare_results(test_item, test_expected):
        # As a sanity check, we call the method directly
        result = environ.__getitem__(test_item)
        assert result == test_expected and isinstance(result, str)
        # Now we call the method like a user would to fetch an arbitrary environment variable
        result = environ[test_item]
        assert result == test_expected and isinstance(result, str)

    # The below tests are trying to test a variety of scenarios that we could encounter
    # when we parse the environment.

    # Test one:  Make sure that the key exists and that we get the correct
    # decoded value
    # The below values are from running env on my Fedora 28 workstation
    _compare_results('XDG_SESSION_ID', '4')
    _compare

# Generated at 2022-06-13 16:40:11.192330
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ[b'foo'] = b'bar'
    os.environ[b'foo2'] = b'bar'
    os.environ[b'foo3'] = b'bar'
    os.environ[b'foo4'] = b'bar'
    os.environ[b'foo5'] = b'bar'
    os.environ[b'foo6'] = b'bar'
    assert environ[b'foo'] == 'bar'
    assert environ[b'foo2'] == 'bar'
    assert environ[b'foo3'] == 'bar'

    os.environ[b'foo'] = b'\xd0\xae'
    assert environ[b'foo'] == '\u04ae'


# Generated at 2022-06-13 16:40:14.767396
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')
    assert env['PYTHONPATH'] == os.environ['PYTHONPATH']
    assert isinstance(env['PYTHONPATH'], str)

# Generated at 2022-06-13 16:40:21.265013
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test converting to text
    result = environ['PATH']
    assert isinstance(result, unicode)
    assert len(result) > 0

    # Test not converting to text
    result = environ['PWD']
    assert isinstance(result, bytes)
    assert len(result) > 0

    # Test os.environ returning bytes, Python3 returning text
    result = environ['HOME']
    if PY3:
        assert isinstance(result, unicode)
    else:
        assert isinstance(result, bytes)



# Generated at 2022-06-13 16:40:32.885777
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test valid UTF-8 environment variable
    orig_environ = os.environ.copy()
    os.environ.clear()

# Generated at 2022-06-13 16:40:41.995211
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    if sys.version_info[0] != 3:
        d = {b'python3': b'3'}
        environ = _TextEnviron(d)
        assert environ.get(b'python3') == u'3'
        assert environ.get('python3') == u'3'
        assert environ[b'python3'] == u'3'
        assert environ[u'python3'] == u'3'
    else:
        d = {b'python3': b'3'}
        environ = _TextEnviron(d)
        assert environ.get(b'python3') == b'3'
        assert environ.get('python3') == b'3'
        assert environ[b'python3'] == b'3'
        assert en

# Generated at 2022-06-13 16:40:52.241199
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:41:00.076172
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Unittest for method __getitem__ of class _TextEnviron"""
    class _Environ(dict):
        # pylint: disable=arguments-differ,super-init-not-called
        def __getitem__(self, key):
            return dict.__getitem__(self, key).encode('utf-8')
    _environ = _Environ.fromkeys(['PYTHONPATH', 'PATH'], u'\u263a')
    environ = _TextEnviron(env=_environ)
    assert u'\u263a' == environ['PATH']

# Generated at 2022-06-13 16:41:10.817801
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    mock_environ = {'TEST_KEY_1': b'\xc3\x89', 'TEST_KEY_2': b'\xc3\x89', b'TEST_KEY_3': b'\xc3\xb2'}

    text_environ = _TextEnviron(mock_environ, encoding='latin-1')

    item_1 = text_environ['TEST_KEY_1']
    assert item_1 == u'\xc9'
    item_2 = text_environ['TEST_KEY_2']
    assert item_2 == u'\xc9'
    item_3 = text_environ[b'TEST_KEY_3']
    assert item_3 == u'\xb2'

# Generated at 2022-06-13 16:41:16.169330
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['a'] = 'a'
    assert environ['a'] == 'a'
    environ['b'] = b'b'
    assert environ['b'] == 'b'
    environ['c'] = u'c'
    assert environ['c'] == 'c'
    environ['d'] = os.environ.get('d')
    assert environ['d'] == os.environ.get('d')

# Generated at 2022-06-13 16:41:26.163763
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron(encoding='utf-8')

    # Test that non-string values are returned without decoding
    env._raw_environ = {'int': 1}
    assert env['int'] == 1
    env._raw_environ = {'float': 1.0}
    assert env['float'] == 1.0

    # Test that unicode values are returned without decoding
    env._raw_environ = {'unicode': u'unicode'}
    assert env['unicode'] == u'unicode'

    # Test that ascii values are returned without decoding
    env._raw_environ = {'ascii': u'ascii'.encode()}
    assert env['ascii'] == u'ascii'

    # Test that values that are not decodable by the default encoding are returned without

# Generated at 2022-06-13 16:41:32.922982
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEST_ENV_VAR'] = 'foo'
    assert environ['TEST_ENV_VAR'] == 'foo'

    environ['TEST_ENV_VAR'] = b'bar'
    assert environ['TEST_ENV_VAR'] == 'bar'

    # TODO: Add tests for surrogate_or_strict, xmlcharrefreplace, backslashreplace, and
    #       namereplace.  And add those conversions to the implementation.

# Generated at 2022-06-13 16:41:39.533167
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # By default, the encoding variable should be set to use sys.getfilesystemencoding()
    obj = _TextEnviron()
    # Ensure that the new value is stored and retrieved with the same encoding
    obj[u'foo'] = u'bar'
    assert obj[u'foo'] == u'bar'
    # Ensure that we can modify the encoding and the encoding will be honored
    obj = _TextEnviron(encoding='latin-1')
    obj[u'foo'] = u'bar'
    assert isinstance(obj[u'foo'], text_type)
    assert obj[u'foo'] == u'bar'

# Generated at 2022-06-13 16:41:43.782666
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set up environ
    environ['TEST1'] = 'This is a basic ascii string'
    environ['TEST2'] = 'This is a unicode string: \u201C'

    # Make sure we get expected results
    assert environ['TEST1'] == 'This is a basic ascii string'
    assert environ['TEST2'] == u'This is a unicode string: \u201C'


# Generated at 2022-06-13 16:41:56.784700
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest

    class __TextEnviron__getitem__TestCase(unittest.TestCase):
        def test_key_found(self):
            def _get_item(key):
                return environ[key]

            old_environ = os.environ
            os.environ = {'foo': 'bar'}
            environ = _TextEnviron()
            os.environ = old_environ
            self.assertEqual(_get_item('foo'), 'bar')

        def test_key_not_found(self):
            def _get_item(key):
                return environ.get(key)

            old_environ = os.environ
            os.environ = {'foo': 'bar'}
            environ = _TextEnviron()
            os.environ = old_environ

# Generated at 2022-06-13 16:42:04.051491
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # This may be good enough as long as we are talking to the same Python version on which we are
    # running.  May want to do something fancier later, like use pytest fixtures
    # https://docs.pytest.org/en/latest/fixture.html
    sys.stdout.write("Testing method __getitem__ of class _TextEnviron")
    environ["TESTKEY"] = "TEST VALUE"
    assert environ['TESTKEY'] == "TEST VALUE"
    environ["TESTKEY"] = "TEST VALUE2"
    assert environ['TESTKEY'] == "TEST VALUE2"

    if not PY3:
        # Test that we get a unicode value back from the environment
        assert type(environ['TESTKEY']) == str



# Generated at 2022-06-13 16:42:15.671930
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text

    # Plain text
    os.environ['HELLO'] = 'world'
    assert environ['HELLO'] == 'world'

    # Bytes
    os.environ['HELLO'] = b'world'
    assert environ['HELLO'] == 'world'

    # Non-ascii text
    os.environ['HELLO'] = u'\u0404'
    assert environ['HELLO'] == u'\u0404'

    # Non-ascii bytes
    os.environ['HELLO'] = b'\x04'
    assert environ['HELLO'] == u'\u0004'

    # Surrogate pair

# Generated at 2022-06-13 16:42:22.019548
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'ANSIBLE_TEST': b'\xed\x95\x9c\xea\xb5\xad\xec\x96\xb4 \xea\xb5\xad\xed\x9a\xb0\xeb\xb2\x95\xec\x8b\xa4\xea\xb1\xb0'})
    assert env[u'ANSIBLE_TEST'] == u'한국어 국략법실거리'

# Generated at 2022-06-13 16:42:30.820311
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():  # pylint: disable=invalid-name
    raw_environ = {
        b'ANSIBLE_TEST_UNSET_ENV': b'fake_value',
        b'ANSIBLE_TEST_ENCODED_ENV': b'\xe2\x98\x83\xe2\x98\x83',
        b'ANSIBLE_TEST_DECODED_ENV': u'\u2603\u2603',
    }
    text_environ = _TextEnviron(raw_environ, encoding='utf-8')
    for key in text_environ:
        assert isinstance(text_environ[key], str), '__getitem__ is not returning str'

# Generated at 2022-06-13 16:42:35.281791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ['TEST_VAR_1'] = 'TEST_VALUE_1'
    assert environ['TEST_VAR_1'] == 'TEST_VALUE_1'
    environ._raw_environ['TEST_VAR_2'] = b'TEST_VALUE_2'
    assert environ['TEST_VAR_2'] == 'TEST_VALUE_2'

# Generated at 2022-06-13 16:42:40.868477
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # _TextEnviron should return a text string if decoding of environment variable is successful
    assert isinstance(environ['PYTHONPATH'], str)

    # _TextEnviron should return a text string even if decoding of environment variable is not
    # successful
    assert isinstance(environ['ABCDEFGHIJKLMNOP'], str)



# Generated at 2022-06-13 16:42:50.673919
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Set up a text environment
    os.environ['ANSIBLE_TEXT'] = 'Text value'

    # Mock up a test environment
    class TestEnvironment(object):
        # Create an environment variable to test __getitem__
        def __init__(self):
            self.test_value = 'Test value'
            os.environ['ANSIBLE_TEST'] = self.test_value

        # Delete our test variable
        def __del__(self):
            del os.environ['ANSIBLE_TEST']

        # Get our test variable as a unicode object
        def get_unicode(self):
            return to_text(self.test_value)

        # Get our test variable as a byte string
        def get_bytes(self):
            return to_bytes(self.test_value)

    # Arrange for our test

# Generated at 2022-06-13 16:43:01.884628
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for encoding
    env = _TextEnviron(encoding='latin-1')
    env['FOO'] = b'\xa3'  # Latin-1 '£'
    assert env['FOO'] == u'£'
    env['BAR'] = b'\xf1'  # Latin-1 'ñ'
    assert env['BAR'] == u'ñ'

    # Test for surrogate_or_strict
    env = _TextEnviron(encoding='latin-1')
    try:
        env['FOO'] = b'\xc3\xb1'  # Latin-1 'ñ' but mistakenly encoded in utf-8
        assert 0, 'Expected ValueError'
    except ValueError:
        pass
    assert u'¢' not in env  # ensure we didn't break the dict along the way

# Generated at 2022-06-13 16:43:03.587318
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ["abcdef"] = "abcdef"

    assert environ["abcdef"] == "abcdef"

# Generated at 2022-06-13 16:43:18.922245
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping

    # TODO - This needs to be fixed
    # This needs to test the functionality of all of the paths in the class but it's hard to test
    # since we're trying to mock out a lot of things in order to test them
    # Before we can test this, what's required is to test the parts of the class that mock out os
    # This is a fork of six's environment implementation in Lib/test/test_six.py which is under the
    # MIT license
    # This is an instance of the class, not the class itself

# Generated at 2022-06-13 16:43:24.464686
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os.environ = {
        b'a_key_with_a_normal_value': b'A normal string',
        b'a_key_with_a_binary_string': b'\xc3\xbc',
        b'a_key_with_a_text_string': '\xc3\xbc'
    }

    env = _TextEnviron()

    # Test that we get the expected values
    assert env[u'a_key_with_a_normal_value'] == u'A normal string'
    assert env[u'a_key_with_a_binary_string'] == u'\xc3\xbc'
    assert env[u'a_key_with_a_text_string'] == u'\xc3\xbc'

    # Test that we don't corrupt our cache
    assert env

# Generated at 2022-06-13 16:43:30.632686
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_cases = [
        ('', '', 'utf-8'),
        ('a', 'a', 'utf-8'),
        ('a\xe1', 'a\xe1', 'utf-8'),
        ('a\xe1', 'a\xc3\xa1', 'latin-1'),
        ('a\xe1', 'a\xc3\xa1', 'utf-8'),
    ]
    for key, raw_value, encoding in test_cases:
        yield check__TextEnviron___getitem__, key, raw_value, encoding



# Generated at 2022-06-13 16:43:34.804770
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {
        'a': 'a\u1234',
        'b': 'x\x95'
    }
    assert environ['a'] == 'a\u1234'
    assert environ['b'] == 'x\ufffd'


# Generated at 2022-06-13 16:43:44.887009
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    new_env = _TextEnviron({b'foo': b'bar', b'baz': '\xE9'})
    assert new_env['foo'] == u'bar'
    assert new_env['baz'] == '\xE9'

    new_env = _TextEnviron({b'foo': b'bar', b'baz': '\xE9'}, encoding='iso-8859-15')
    assert new_env['foo'] == u'bar'
    assert new_env['baz'] == '\xE9'

    new_env = _TextEnviron({b'foo': b'bar', b'baz': '\xE9'}, encoding='utf-8')
    assert new_env['foo'] == u'bar'

# Generated at 2022-06-13 16:43:50.568516
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({b'test_bytes': b'foo'}, encoding='utf-8')
    assert environ[b'test_bytes'] == 'foo'
    assert not isinstance(environ[b'test_bytes'], bytes)
    environ = _TextEnviron({u'test_unicode': u'foo'}, encoding='utf-8')
    assert environ[u'test_unicode'] == 'foo'
    assert not isinstance(environ[u'test_unicode'], str)


# Generated at 2022-06-13 16:43:58.319464
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest

    class Test__TextEnviron___getitem__(unittest.TestCase):
        def test_unicode_value(self):
            test_environ = _TextEnviron()
            key = '漢字'
            value = '語'
            test_environ[key] = value
            self.assertEqual(test_environ[key], value)

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test__TextEnviron___getitem__))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)


if __name__ == '__main__':
    test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:44:10.359141
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import unittest

    try:
        encoding = sys.getfilesystemencoding()
    except AttributeError:
        encoding = None
    test_dict = {b'USER': os.getenv('USER').encode(encoding) if PY3 else os.getenv('USER'),
                 b'LANG': os.getenv('LANG').encode(encoding) if PY3 else os.getenv('LANG'),
                 b'HOME': os.getenv('HOME').encode(encoding) if PY3 else os.getenv('HOME'),
                 b'WRONG': b'\xc3\x28',
                 b'CODING': b'utf8'}
    if not PY3:
        del test_dict[b'WRONG']
    test_environ = _TextEnviron

# Generated at 2022-06-13 16:44:16.521871
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    environ_orig = {b'UTF8': b'value1', 'ascii': 'value2', 'Latin1': 'value3'.encode('latin1')}
    environ_mock = _TextEnviron(env=environ_orig, encoding='utf-8')

    assert environ_mock['UTF8'] == 'value1'
    assert environ_mock['ascii'] == 'value2'
    assert environ_mock['Latin1'] == 'value3'



# Generated at 2022-06-13 16:44:19.629080
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({b'ANSIBLE_TEST1': b'value1', 'ANSIBLE_TEST2': 'value2'})

    assert env['ANSIBLE_TEST1'] == 'value1'
    assert env['ANSIBLE_TEST2'] == 'value2'

# Generated at 2022-06-13 16:44:37.589073
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    __init__ = _TextEnviron.__init__
    __getitem__ = _TextEnviron.__getitem__
    class T(object): pass
    t = T()
    t.encoding = 'utf-8'

# Generated at 2022-06-13 16:44:45.111478
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import configparser  # pylint: disable=import-error,redefined-builtin
    from ansible.module_utils._text import to_native, to_text
    import tempfile
    import os

    # pylint: disable=unused-variable
    def setup_temp_config(config_text):
        '''Create a temp config file and set the environment to use the temp config file'''
        # Save stdout and stderr so we can restore them
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        stdout = StringIO()
        stderr = StringIO()
        sys.stdout = stdout
        sys.stderr = stderr



# Generated at 2022-06-13 16:44:49.895987
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron({
        to_bytes('str_key'): to_bytes('str_value'),
        to_bytes('unicode_key'): to_bytes('unicode_value')
    }, 'ascii')

    assert text_environ['str_key'] == 'str_value'
    assert text_environ['unicode_key'] == 'unicode_value'

# Generated at 2022-06-13 16:44:53.338872
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {}
    env['key'] = b'value'
    t = _TextEnviron(env, encoding='utf-8')
    assert 'value' == t['key']



# Generated at 2022-06-13 16:45:02.982368
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_bak = environ._raw_environ
    environ._raw_environ = {}
    environ._raw_environ['aaa'] = 'ascii'
    environ._raw_environ['bbb'] = '\xe4'.encode('utf-8')
    environ._raw_environ['ccc'] = '\xe4'
    environ._raw_environ['ddd'] = '\xe4\xf6'
    environ._raw_environ['eee'] = '\xe4\xf6\xe4'
    assert environ['aaa'] == 'ascii'
    assert environ['bbb'] == '\xe4'
    assert environ['ccc'] == '\xe4'
    assert environ['ddd'] == '\xe4\xf6'
   

# Generated at 2022-06-13 16:45:12.586190
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six.moves import builtins

    getattr(builtins, '__test__', False)
    if hasattr(builtins, "__test__") and not getattr(builtins, '__test__'):
        return

    from ansible.module_utils.common._collections_compat import MutableMapping
    import tempfile

    testdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(testdir, '\xe6\x96\xb0\xe5\x96\x84'))
    os.chdir(os.path.join(testdir, '\xe6\x96\xb0\xe5\x96\x84'))

# Generated at 2022-06-13 16:45:22.872265
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _RawEnviron(object):
        def __init__(self):
            # xxx We'll need to do some more testing to decide how to handle non-utf-8 bytes in the
            # environment.  For now, simulate a valid utf-8 environment
            self._environ = {b'\xc2\xb5': b'\xc2\xb5', b'\xca\xbc': b'\xca\xbc'}

        def __getitem__(self, key):
            return self._environ[key]
    env = _TextEnviron(env=_RawEnviron())

    # Simple ascii strings
    assert env[b'foo'] == u'foo'
    assert env[u'foo'] == u'foo'

    # Unicode characters that can be encoded as ascii.

# Generated at 2022-06-13 16:45:24.776600
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == u'/usr/local/bin:/usr/bin:/bin'
test__TextEnviron___getitem__()


# Generated at 2022-06-13 16:45:29.903311
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['TEXTENVIRON_TEST'] = b'\xed\xa0\xbc\xed\xb6\x8c\xed\xa0\xbc\xed\xb6\x8c\xed\x9a\x92\xed\x83\xa3\xed\x8e\xba'

# Generated at 2022-06-13 16:45:38.092997
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that __getitem__ returns an undecoded byte string
    environ = _TextEnviron()
    environ._raw_environ = {b'ANSIBLE_TEST_VAR': b'foo'}
    assert environ[b'ANSIBLE_TEST_VAR'] == b'foo'

    # Test that __getitem__ returns an undecoded byte string when Python 3
    environ = _TextEnviron()
    environ._raw_environ = {'ANSIBLE_TEST_VAR': b'foo'}
    assert environ[b'ANSIBLE_TEST_VAR'] == b'foo'

    environ = _TextEnviron()
    environ._raw_environ = {'ANSIBLE_TEST_VAR': 'foo'}