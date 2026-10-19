

# Generated at 2022-06-13 16:35:42.433253
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._value_cache = {}
    environ.encoding = None
    environ._raw_environ = {'PATH': '/usr/bin', 'HOME': 'doe'}

    assert environ['HOME'] == 'doe'
    assert environ['HOME'] == environ['HOME']
    assert environ['PATH'] == '/usr/bin'
    assert environ['PATH'] == environ['PATH']


# Generated at 2022-06-13 16:35:52.463626
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import six
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_native
    import sys

    class _Test_TextEnviron(MutableMapping):
        """
        Utility class to return text strings from the environment instead of byte strings

        Mimics the behaviour of os.environ on Python3
        """
        def __init__(self, env=None):
            if env is None:
                env = os.environ
            self._raw_environ = env
            self._value_cache = {}
            # Since

# Generated at 2022-06-13 16:35:55.328359
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''Unit test for _TextEnviron.__getitem__'''
    env = _TextEnviron(encoding='utf-8')
    return os.environ.items() == env.items()

# Generated at 2022-06-13 16:35:58.217059
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    assert environ['PATH']   # Should not raise KeyError
    assert environ['SHELL']  # Should not raise KeyError



# Generated at 2022-06-13 16:36:03.887450
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # environ.__getitem__ returns a text string
    assert isinstance(environ['PATH'], str)
    # environ.__getitem__ returns the same text string consistently when given the same key
    assert environ['PATH'] is environ['PATH']
    # environ.__getitem__ returns the same text string consistently when given the same key
    # with different casing
    assert environ['PATH'] is environ['path']



# Generated at 2022-06-13 16:36:10.626653
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__(): # pylint: disable=invalid-name
    """_TextEnviron.__getitem__() should return text values for environment variables"""
    environ = _TextEnviron({b'a': b'1'}, encoding='ascii')
    assert environ[u'a'] == u'1'
    #
    # make sure that we continue to get the right values as the environment changes
    #
    environ[u'a'] = u'2'
    assert environ[u'a'] == u'2'



# Generated at 2022-06-13 16:36:19.920880
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({b'foo': 'bar', 'unicode': '\u00e9', 'utf8': '\xc3\xa9'},
                                encoding='latin-1')

    # Check normal case
    assert test_environ['foo'] == u'bar'

    # Check for unicode values that are not decodable with latin1
    assert test_environ['utf8'] == u'\ufffd\ufffd'

    # Check for unicode values that are encodable with latin1
    assert test_environ['unicode'] == u'\xE9'


# Generated at 2022-06-13 16:36:23.502548
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.clear()
    environ['test_key'] = 'test_value'
    value = environ['test_key']
    assert value == u'test_value'

# Generated at 2022-06-13 16:36:28.072956
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron(encoding='utf-8')
    test_env['test_value'] = u'unicode string'
    test_env['test_value_bytes'] = b'bytes string'

    assert test_env['test_value'] == u'unicode string'
    assert test_env['test_value_bytes'] == u'bytes string'

# Generated at 2022-06-13 16:36:36.221086
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test the cache
    environ._value_cache['TEST'] = 'test'
    assert 'test' == environ['TEST']

    # Test encoding
    environ['TEST'] = u'\U0001F48A'
    if PY3:
        assert u'\U0001F48A' == environ['TEST']
    else:
        assert u'\ud83d\udc8a' == environ['TEST']

    # Test non-string recognized encoding
    environ['TEST'] = b'\x00\x01\x02\x03'
    assert b'\x00\x01\x02\x03' == environ['TEST']

    # Test surrogate strict
    environ['TEST'] = '\ud83d\udc8a'

# Generated at 2022-06-13 16:36:46.157093
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test case #1:
    key = 'ANSIBLE_STRINGS_PLUGIN_TEST__UNITTEST__'
    value = 'this is a test'
    os.environ[key] = value
    assert environ[key] == value

    # Test case #2:
    key = 'ANSIBLE_STRINGS_PLUGIN_TEST__UNITTEST__'
    value = u'\u6c34'
    os.environ[key] = value
    assert environ[key] == value

    # Test case #3:
    key = 'ANSIBLE_STRINGS_PLUGIN_TEST__UNITTEST__'
    value = b'\xe6\xb0\xb4'
    os.environ[key] = value
    assert environ[key] == value

    # Cleanup the

# Generated at 2022-06-13 16:36:55.215887
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make sure that it handles byte strings
    os.environ[b'foo'] = b'abc\xe9def'
    env = _TextEnviron(os.environ)
    assert isinstance(env[b'foo'], str)
    assert env[b'foo'] == u'abcédef'
    # Make sure that it handles text strings
    os.environ['foo'] = 'abcédef'
    env = _TextEnviron(os.environ)
    assert isinstance(env['foo'], str)
    assert env['foo'] == u'abcédef'
    # Make sure it handles unicode
    os.environ[u'foo'] = u'abcédef'
    env = _TextEnviron(os.environ)
    assert isinstance(env[u'foo'], str)

# Generated at 2022-06-13 16:37:03.518680
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # read bytes
    assert environ._raw_environ['LC_ALL'] == b'en_US.UTF-8'
    if PY3:
        assert environ['LC_ALL'] == 'en_US.UTF-8'
    else:
        assert environ['LC_ALL'] == u'en_US.UTF-8'
    assert environ.encoding == 'utf-8'
    assert environ._value_cache[b'LC_ALL'] == u'en_US.UTF-8'


test__TextEnviron___getitem__()

# Generated at 2022-06-13 16:37:07.850779
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(env={b'PYTHONIOENCODING': b'utf-8'})
    assert isinstance(test_environ['PYTHONIOENCODING'], str)


# Generated at 2022-06-13 16:37:16.778337
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # We need an object to pass to the constructor
    os.environ['TEST_GETITEM'] = 'this is a test'
    environ = _TextEnviron()
    # Since we're using an empty encoding, it should match the raw value
    assert environ['TEST_GETITEM'] == 'this is a test'

    # Now set the encoding to 'utf-8' and try again
    environ.encoding = 'utf-8'
    assert environ['TEST_GETITEM'] == u'this is a test'

    # Now test that we can set the environment variable to a non-ascii value
    if PY3:
        os.environ['TEST_GETITEM'] = 'this is a \xE0\xA4\xA7 test'
    else:
        os.environ

# Generated at 2022-06-13 16:37:25.822750
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # This test is a copy of the unittest in six and modified to use ansible.module_utils._text.

    # Helper to populate os.environ
    def _update_environ(*args, **kwargs):
        # os.environ.update is a builtin in Python 2 and may have been
        # undermined by a previous test.
        if hasattr(os.environ, "update"):
            return os.environ.update(*args, **kwargs)
        os.environ.data.update(*args, **kwargs)

    # Values as unicode
    _update_environ({'UNICODE_TEST': 'abcdé'})

    # Values as bytes but without encoding

# Generated at 2022-06-13 16:37:28.196122
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LANG'] == 'en_US.UTF-8'


# Generated at 2022-06-13 16:37:32.444049
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Make sure that errors='surrogate_or_strict' is the default
    assert 'Test\udce2' == environ._TextEnviron.__getitem__(environ, b'ANSIBLE_TEST_ENV_KEY')


# Generated at 2022-06-13 16:37:42.518559
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method __getitem__ of class _TextEnviron

    >>> test__TextEnviron___getitem__()
    '''
    environ = _TextEnviron(encoding='utf-8')
    os.environ['ansible_module_utf8'] = b'\xe6\x88\x91\xe4\xbb\xac'

    # Testing different configurations of environment variables and unicode characters
    assert environ['ansible_module_utf8'] == u'我们'
    assert environ._raw_environ['ansible_module_utf8'] == b'\xe6\x88\x91\xe4\xbb\xac'
    assert environ.encoding == 'utf-8'
    del os.environ['ansible_module_utf8']

# Generated at 2022-06-13 16:37:45.620173
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron()
    assert e.get('KEY_THAT_DOES_NOT_EXIST', 'default') == 'default'
    if PY3:
        assert e.get('LANGUAGE') == 'en_US.UTF-8'
    else:
        assert e.get('LANGUAGE') == u'en_US.UTF-8'



# Generated at 2022-06-13 16:37:56.144402
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Run the test on a copy of the environ object
    testenv = _TextEnviron(encoding='utf-8')

    # Test for non-ascii characters in environment variable names
    key_unicode = u"\u6d4b\u8bd5"
    key_bytes = b"\xe6\xb5\x8b\xe8\xaf\x95"
    testenv[u"\u6d4b\u8bd5"] = u"\u6d4b\u8bd5"

    # Test for non-ascii characters in value of environment variable
    value_unicode = u"\u6d4b\u8bd5\u6d4b\u8bd5"

# Generated at 2022-06-13 16:38:01.928887
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.clear()
    environ.update(dict(X=to_bytes('a', encoding='utf-8')))
    environ.__getitem__('X')
    assert dict(environ) == dict(X=to_bytes('a', encoding='utf-8'))
    assert id(environ['X']) != id(environ._raw_environ['X'])



# Generated at 2022-06-13 16:38:08.494639
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test the method __getitem__ of class TextEnviron.
    '''
    import os
    import sys
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import MutableMapping

    class _TestEnviron(MutableMapping):
        """
        Utility class to return text strings from the environment instead of byte strings

        Mimics the behaviour of os.environ on Python3
        """
        def __init__(self, env=None, encoding=None):
            if env is None:
                env = os.environ
            self._raw_environ = env
            self._value_cache = {}

# Generated at 2022-06-13 16:38:12.469437
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    # Test a value in the environment
    assert env['HOME'] == os.environ['HOME']

    # Test a value not in the environment
    try:
        assert env['THISISNOTREAL'] == os.environ['THISISNOTREAL']
    except KeyError:
        pass


# Generated at 2022-06-13 16:38:19.884724
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import collections
    import tests.unit.utils.platform_mock as pm

    # Test for unexpected behavior on PY2 when an entry ends with a surrogate.  For details see:
    #   https://github.com/ansible/ansible/issues/64115
    if sys.version_info[0] == 2:
        temp_env = pm.Environment(
            SURROGATE_ENV_VARIABLE='foo\udcff',
        )
        with temp_env:
            # If we're unable to decode, the surrogate in the env var should result in a
            # UnicodeDecodeError
            with pm.AssertRaises(UnicodeDecodeError):
                os.environ['SURROGATE_ENV_VARIABLE'].encode('ascii')


# Generated at 2022-06-13 16:38:30.792340
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Set environment variable with an UTF-8 string
    os.environ['_TextEnviron'] = b'\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba'
    # Assert that it's created from a UTF-8 encoded bytes object
    assert os.environ.encode('UTF-8') == b'_TextEnviron=\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba'
    # Assert that it's resulted in a unicode-like object when getting from
    # module's environ
    assert type(environ['_TextEnviron']) == type(u'')
    # Assert that is returned correct value

# Generated at 2022-06-13 16:38:37.572803
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import unittest

    class test__TextEnviron__getitem__(unittest.TestCase):

        def setUp(self):
            self.test_env = _TextEnviron()

        def test_getitem_unicode(self):
            self.test_env['FOO'] = '\u043f\u0440\u0438\u0432\u0435\u0442'
            self.assertEqual(self.test_env['FOO'], 'привет')

    suite = unittest.TestLoader().loadTestsFromTestCase(test__TextEnviron__getitem__)
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-13 16:38:46.707065
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Given that the byte string for 'key1' is 'a2V5MQo='...
    assert 'a2V5MQo=' == to_bytes('key1\n')
    # And that a TextEnviron has been created which uses 'utf-8' as the encoding
    environ = _TextEnviron({'key1': 'a2V5MQo='}, encoding='utf-8')
    # When we access the value for 'key1'
    value = environ['key1']
    # Then the value should be the decoded string 'key1\n'
    assert 'key1\n' == value
    # And the type of the value should be text
    assert isinstance(value, str)

# Generated at 2022-06-13 16:38:54.307439
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    env['ascii'] = 'ascii_value'
    env['unicode'] = u'unicode_value'
    env['bytes'] = b'bytes_value'

    assert env['ascii'] == 'ascii_value'
    assert type(env['ascii']) == str
    assert env['unicode'] == u'unicode_value'
    assert type(env['unicode']) == str
    assert env['bytes'] == b'bytes_value'
    assert type(env['bytes']) == str



# Generated at 2022-06-13 16:39:02.706237
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Testing case when the key is not in the dictionary
    if True:
        try:
            environ['test_key']
        except KeyError as e:
            assert(str(e) == "'test_key'")
        else:
            raise Exception("'test_key' should not be in the dictionary")
    # Testing case when the key is in the dictionary
    if True:
        assert(environ['PATH'] == '/usr/bin:/bin:/usr/sbin:/sbin')
        assert(isinstance(environ['PATH'], str))


# Generated at 2022-06-13 16:39:13.671313
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    o = _TextEnviron({'Simple': 'Simple',
                     # os.environ will return bytes (Python 2) or text (Python 3)
                     # for non-string values.  Make sure decoding will work for both.
                     'bytes': b'service\xe9',
                     'nonstring': b'1'})
    assert o['Simple'] == 'Simple'
    assert u'serviceé' == o['bytes']
    # As above, os.environ will return bytes (Python 2) or text (Python 3)
    # for non-string values.  Simple test for a non-string value here as above.
    assert u'1' == o['nonstring']



# Generated at 2022-06-13 16:39:20.453425
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class _FakeSys():
        def __init__(self, defenc):
            self.getfilesystemencoding = lambda: defenc

    env = _TextEnviron(encoding='utf-8')
    sys = _FakeSys('utf-8')

    os.environ['ANSIBLE_TEST_KEY_UNICODE'] = u'foo'
    assert env['ANSIBLE_TEST_KEY_UNICODE'] == u'foo'

    os.environ['ANSIBLE_TEST_KEY_BYTES'] = b'bar'
    assert env['ANSIBLE_TEST_KEY_BYTES'] == u'bar'

    os.environ['ANSIBLE_TEST_KEY_TEXT'] = 'baz'
    assert env['ANSIBLE_TEST_KEY_TEXT'] == u'baz'


# Unit

# Generated at 2022-06-13 16:39:27.502555
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def _check_item(item):
        environ['item'] = item
        assert environ['item'] == item

    # Ensure that bytes or text gets passed through
    _check_item(b'x')
    _check_item('x')

    # Ensure that bytes or text gets passed through
    _check_item(b'\x00')
    _check_item('\u0000')

    # Ensure that surrogate escapes are returned
    _check_item(b'\xFF')
    _check_item('\ufffd')

# Generated at 2022-06-13 16:39:31.586228
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron({b'key1': b'testuring', b'key2': b'r\xc3\xb8dgr\xc3\xb8d'})
    assert text_environ[b'key1'] == u'testuring'
    assert text_environ[b'key2'] == u'r\u00f8dgr\u00f8d'

# Generated at 2022-06-13 16:39:35.059528
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({"TOTO":"toto"})
    assert environ['TOTO'] == "toto"


# Generated at 2022-06-13 16:39:39.926713
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test case 1: test with __getitem__ method when environment variable is key
    os.environ['test'] = 'test'
    assert environ['test'] == 'test'

    # Test case 2: test with __getitem__ method when given variable is not environment variable
    try:
        environ['test2']
    except KeyError:
        assert True



# Generated at 2022-06-13 16:39:51.411583
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ.__getitem__('HOME') == u'/home/ec2-user'
    assert environ.__getitem__('SHELL') == u'/bin/bash'
    assert environ.__getitem__('MAIL') == u'/var/spool/mail/ec2-user'
    assert environ.__getitem__('bogus') == u'bogus'
    #assert environ.__getitem__('/tmp') == u'/tmp'
    #assert environ.__getitem__('/tmp/') == u'/tmp/'
    assert environ.__getitem__('HOME/') == u'/home/ec2-user/'
    assert environ.__getitem__('HOME/test') == u'/home/ec2-user/test'

# Generated at 2022-06-13 16:39:54.541629
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # TODO(toshio): Write test using a mock environment where the value is not utf-8 compatible.
    assert environ['USER'] == os.environ.get('USER')

# Generated at 2022-06-13 16:40:03.174666
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Unit test for method __getitem__ of class _TextEnviron"""

    # Test data
    native_text_env = {}
    native_text_env[to_bytes('byte_string')] = to_bytes('byte_string')
    native_text_env[to_bytes('unicode_string')] = to_bytes('\u00E9'.encode('utf-8'))

    # Expected results
    expected_results = {}
    expected_results['byte_string'] = 'byte_string'
    expected_results['unicode_string'] = '\u00E9'

    # Execute code being tested
    test_instance = _TextEnviron(native_text_env, 'utf-8')

    # Verify test results

# Generated at 2022-06-13 16:40:08.910839
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    env = _TextEnviron()
    env['ascii'] = 'ascii'
    env['utf-8'] = '\u2271'

    if PY3:
        assert env['ascii'] == 'ascii'
        assert env['utf-8'] == '\u2271'
        return

    # _TextEnviron should return unicode
    assert env['ascii'] == u'ascii'
    assert env['utf-8'] == u'\u2271'

    # _TextEnviron should return a unicode object even if the environment variable changes during
    # the run
    env['utf-8'] = '\u2272'
    assert env['utf-8'] == u'\u2271'

    # _TextEnviron should return a unicode object encoded in utf-8 even

# Generated at 2022-06-13 16:40:18.988469
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # hack to set the value of os.environ to an empty dict
    global os
    oldos = os
    os = MockOS()
    os.environ = {}

    global environ
    oldenv = environ
    environ = _TextEnviron(env=os.environ)

    global sys
    oldsys = sys
    sys = MockSys(encoding='utf-8')

    environ['key'] = 'value'
    assert environ['key'] == 'value'

    os = oldos
    environ = oldenv
    sys = oldsys



# Generated at 2022-06-13 16:40:23.995297
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # mimic python2
    environ = _TextEnviron(encoding=None)
    assert environ['HOME'] == os.environ['HOME']
    # mimic python3
    environ = _TextEnviron(encoding='utf-8')
    assert environ['HOME'] == os.environ['HOME']

# Generated at 2022-06-13 16:40:31.224970
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron({b'a': '1', b'b': u'1'.encode('utf-8'), 'c': '1'})
    for i in range(4):
        if i % 2:
            text_environ['a'] = '2'
        else:
            text_environ[u'b'] = b'2'
        assert text_environ['a'] == '2'
        assert text_environ['b'] == '2'


# Generated at 2022-06-13 16:40:41.460066
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Tests for the __getitem__ method of TextEnviron

    :returns: None
    """
    from ansible.module_utils.common._collections_compat import MutableMapping

    # Create an object to test __getitem__ on
    env = MutableMapping({'text_key1': 'value1', b'bytes_key1': b'value1'})

    # Create a simple function for our test object to use
    def _getitem(key):
        return env[key]

    # Test that the code works with text keys and values
    assert 'value1' == env['text_key1']

    # Test the python3 emulation with text keys and text values
    env._getitem = _getitem
    assert 'value1' == env['text_key1']

    # Test that the code works with bytes keys

# Generated at 2022-06-13 16:40:51.878145
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test a byte string
    step = 'Test a byte string'
    env = {b'string': b'foo'}
    environ = _TextEnviron(env)
    assert to_text(env['string']) == environ['string'], step

    # Test a unicode string
    step = 'Test a unicode string'
    env = {u'string': u'foo'}
    environ = _TextEnviron(env)
    assert to_text(env['string']) == environ['string'], step

    # Test an invalid utf-8 string
    step = 'Test an invalid utf-8 string'
    env = {'string': '\x80foo'}
    environ = _TextEnviron(env)
    assert to_text(env['string'], errors='replace') == en

# Generated at 2022-06-13 16:41:01.686885
# Unit test for method __getitem__ of class _TextEnviron

# Generated at 2022-06-13 16:41:08.658228
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Tests that the environ object returns the expected text results when retrieveing text
    """


# Generated at 2022-06-13 16:41:16.095505
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # It should return a text string since we're not on Python3
    assert isinstance(environ['PATH'], text_type)
    # It should return the actual value of the environment variable.
    # Test by first setting the sys.executable environment variable and then
    # testing on that value.
    # Check that our environment variable differs from the default
    assert environ['PATH'] != os.environ['PATH']
    # Check that when we set the value, we get back the same value
    environ['PATH'] = os.environ['PATH']
    assert environ['PATH'] == os.environ['PATH']



# Generated at 2022-06-13 16:41:18.977156
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({to_bytes("LC_ALL"): to_bytes("C")}, encoding='utf-8')
    assert env[to_bytes("LC_ALL")] == u"C"


# Generated at 2022-06-13 16:41:27.913715
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    def assert_equals(expected, actual):
        assert expected == actual, '\nExpected: {0}\nActual: {1}'.format(expected, actual)

    def set_os_environ(str_):
        os.environ['TEXT_ENVIRON_TEST'] = to_bytes(str_, encoding='utf-8')

    def del_os_environ():
        del os.environ['TEXT_ENVIRON_TEST']

    environ_ = _TextEnviron()

    set_os_environ('Ansi¿ble')
    assert_equals('Ansi¿ble', environ_['TEXT_ENVIRON_TEST'])

    del_os_environ()

# Generated at 2022-06-13 16:41:40.853034
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test 'simple' unicode
    os.environ['ANSIBLE_UNICODE'] = 'aǅɐ'
    assert environ['ANSIBLE_UNICODE'] == u'aǅɐ'
    del os.environ['ANSIBLE_UNICODE']

    # Test utf-8 bytes
    os.environ['ANSIBLE_UNICODE'] = to_bytes(u'á', encoding=environ.encoding, nonstring='strict',
                                             errors='surrogate_or_strict')
    assert environ['ANSIBLE_UNICODE'] == u'á'
    del os.environ['ANSIBLE_UNICODE']

    # Test non-unicode
    os.environ['ANSIBLE_UNICODE'] = '1234'

# Generated at 2022-06-13 16:41:47.302001
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_orig = environ._raw_environ.copy()

    # Test if all values in the environment are already text, nothing should be changed.
    environ.clear()
    for key, value in environ_orig.items():
        value = value.decode(environ.encoding)
        environ[key] = value

    assert environ == environ_orig, 'os.environ should return all text values'

    # Test if all values in the environment are non-text, values should be encoded
    environ.clear()
    for key, value in environ_orig.items():
        value = value.replace(b'\xff', b'')
        environ[key] = value

    assert environ == environ_orig, 'os.environ should encode all non-text values'

    # Test if all values in

# Generated at 2022-06-13 16:41:57.835531
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['A'] = 'B'
    assert environ['A'] == 'B'

    import tempfile
    from ansible.module_utils._text import to_native

    # Test utf-8
    with tempfile.NamedTemporaryFile() as tmp_file:
        tmp_file.write(b'\xFE\xED\xFE\xED')
        tmp_file.flush()
        environ['UTF8'] = tmp_file.name
        assert environ['UTF8'] == to_native(environ['UTF8'])

    # Test latin1
    with tempfile.NamedTemporaryFile() as tmp_file:
        tmp_file.write(b'\xDE\xAD\xBE\xEF')
        tmp_file.flush()

# Generated at 2022-06-13 16:42:08.068233
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create an empty environment
    env = {}

    # Create a _TextEnviron object for our environment
    my_env = _TextEnviron(env)

    # Add a byte string to the environment
    env[b'PS1'] = b'$ '

    # Retrieve the byte string from the environment
    assert my_env[b'PS1'] == b'$ '

    # Retrieve the byte string from the environment using a unicode key
    assert my_env[u'PS1'] == b'$ '

    # Add an empty byte string to the environment
    env[b'http_proxy'] = b''

    # Retrieve the empty byte string from the environment
    assert my_env[b'http_proxy'] == b''

    # Retrieve the empty byte string from the environment using a unicode key

# Generated at 2022-06-13 16:42:18.338053
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    def run(environ, expected, expected_cached):
        for test_name, test_value in environ.items():
            r = env[test_name]
            assert isinstance(r, str)
            assert r == expected[test_name]
        for test_name, test_value in expected_cached.items():
            r = env._value_cache[test_name]
            assert isinstance(r, str)
            assert r == expected_cached[test_name]

    # test _TextEnviron without encoding
    environ = _TextEnviron()

# Generated at 2022-06-13 16:42:21.368274
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test without cache
    assert "text" == environ["text"]

    # Test with cache
    environ.encoding = 'ascii'
    assert "text" == environ["text"]

# Generated at 2022-06-13 16:42:31.050575
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unit test for method _TextEnviron.__getitem__ of class _TextEnviron
    # Test with encoding=utf-8 with both python2 and python3
    for encoding in (b'utf-8', 'utf-8'):
        for python_version in (2, 3):
            saved_python_version = sys.version_info
            sys.version_info = (3, 5, 3, 'final', 0)

            class TestEnviron(dict):
                pass


# Generated at 2022-06-13 16:42:35.175507
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == '/bin:/usr/bin:/usr/local/bin'
    environ['test_variable'] = 'test value'
    assert environ['test_variable'] == 'test value'
    del environ['test_variable']


# Generated at 2022-06-13 16:42:45.731715
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Only run this on Python 2.x
    if PY3:
        raise AssertionError("This test is only valid on Python 2.x")

    # Check that the encoding is set correctly
    assert environ.encoding == 'utf-8'

    # And that the environment doesn't change the encoding
    assert to_bytes('\u05e9\u05dc\u05d5\u05dd', encoding='utf-8') == \
           to_bytes(u'שלום', encoding='utf-8')

    # Do non-ascii strings come out correctly?
    # FIXME: should we do surrogates as well as non-ascii strings?  It's more robust but then you
    #        could end up with non-unicode strings.

# Generated at 2022-06-13 16:42:54.776233
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six.moves import builtins

    environ_items = {}

    # Python 2/3 differences in os.environ
    if PY3:
        for k, v in iteritems(os.environ):
            environ_items[k] = v
    else:  # Python 2
        for k, v in iteritems(os.environ):
            # In Python2 the key is a byte string and the value is a byte string
            environ_items[to_text(k, errors='surrogate_or_strict')] = v

    # Test when PY3 environ is a plain dictionary
    e = _TextEnviron(env=environ_items)

# Generated at 2022-06-13 16:43:06.467744
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Non-ascii characters in environ
    environ['MY_NAME'] = b'\xe1\xbc\xb1\xcf\x83\xcf\x84\xce\xbf\xcf\x82'
    assert environ['MY_NAME'] == u'ἱστός'


# Generated at 2022-06-13 16:43:07.659201
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == environ['PATH']


# Generated at 2022-06-13 16:43:11.999381
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    for key in ('HOME', 'PATH', 'USER'):
        assert environ[key] == os.environ[key]
    for key in os.environ:
        assert environ[key] == os.environ[key]


# Generated at 2022-06-13 16:43:21.903629
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test for decode with value of sys.getfilesystemencoding()
    env = _TextEnviron(encoding=sys.getfilesystemencoding())
    for k, v in os.environ.items():
        # Skip over values which are already text
        if isinstance(v, str):
            continue
        text_v = os.environ[k]
        b_v = to_bytes(to_text(v, errors='surrogate_or_strict'), env.encoding)
        assert text_v == b_v

    # Test for decode with utf-8
    env = _TextEnviron(encoding='utf-8')
    for k, v in os.environ.items():
        # Skip over values which are already text
        if isinstance(v, str):
            continue
        text_v = os

# Generated at 2022-06-13 16:43:31.642042
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test __getitem__ with str type on Python2
    plantestenv = {'A': 'hogehoge', 'B': 'fugafuga', 'C': 'piyopiyo'}
    env = _TextEnviron(plantestenv, encoding='utf-8')
    assert env['A'] == u'hogehoge'

    # Test __getitem__ with bytes type on Python2
    plantestenv = {b'A': b'hogehoge', 'B': b'fugafuga', 'C': b'piyopiyo'}
    env = _TextEnviron(plantestenv, encoding='utf-8')
    assert env['A'] == u'hogehoge'

    # Test __getitem__ with bytes type on Python3

# Generated at 2022-06-13 16:43:40.908182
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    environ[u'foo'] = b'bar'
    assert to_text(b'bar') == environ[u'foo']
    assert to_text(b'bar') == environ[b'foo']
    environ[b'foo'] = u'bar'
    assert to_text(b'bar') == environ[u'foo']
    assert to_text(b'bar') == environ[b'foo']
    environ[b'foo'] = b'bar'
    assert to_text(b'bar') == environ[u'foo']
    assert to_text(b'bar') == environ[b'foo']

# Generated at 2022-06-13 16:43:50.297461
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron
    """
    # First test when PY3 is set to True
    __py3_original_value = PY3
    PY3 = True
    try:
        old_environ = os.environ
        try:
            test_environ = _TextEnviron({'FOO': '\xc3\xbf'})
            assert test_environ['FOO'] == u'\xff'
        finally:
            os.environ = old_environ
    finally:
        PY3 = __py3_original_value

    # Now test when PY3 is False
    __py3_original_value = PY3
    PY3 = False

# Generated at 2022-06-13 16:43:57.018960
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {b'FOO': 'bar', b'FOO1': 'bar1'}
    environ.encoding = 'utf-8'
    assert environ[b'FOO'] == u'bar'
    assert environ[b'FOO1'] == u'bar1'
    assert environ[u'FOO'] == u'bar'
    assert environ[u'FOO1'] == u'bar1'
    assert environ['FOO'] == u'bar'
    assert environ['FOO1'] == u'bar1'
    # Since we're running py2, the keys should be byte strings
    assert list(environ.keys()) == [b'FOO', b'FOO1']



# Generated at 2022-06-13 16:44:08.993787
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_test = _TextEnviron({b'a': b'b', b'c': u'\u4f60\u597d'}, encoding='utf-8')
    assert b'b' == environ_test._raw_environ[b'a']
    assert u'\u4f60\u597d' == environ_test._raw_environ[b'c']
    assert u'b' == environ_test[b'a']
    assert u'\u4f60\u597d' == environ_test[b'c']
    assert u'\u4f60\u597d' == environ_test[u'c']


# Generated at 2022-06-13 16:44:10.102789
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['LANG'] == u'C'

# Generated at 2022-06-13 16:44:25.587957
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ['ANSIBLE_DEBUG'] = 'True'
    assert 'True' in environ['ANSIBLE_DEBUG']

# Generated at 2022-06-13 16:44:31.616046
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    value = environ['PATH']
    assert isinstance(value, str)
    if PY3:
        assert value == os.environ['PATH']
    else:
        assert value == to_text(os.environ['PATH'], encoding='utf-8', nonstring='passthru',
                                errors='surrogate_or_strict')

# Generated at 2022-06-13 16:44:33.828354
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron()
    assert test_env['__foo__'] == to_text(b'bar')



# Generated at 2022-06-13 16:44:42.819684
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    tmpenviron = _TextEnviron()
    tmpenviron['some_var'] = b'\xe4\xbd\xa0\xe5\xa5\xbd'

    # test valid utf-8 string
    assert tmpenviron['some_var'] == '你好'

    # test some bytes that are not valid utf-8
    try:
        tmpenviron['some_var'] = b'\x80'
    except UnicodeDecodeError as e:
        assert True
    else:
        assert False

    # test that str objects can be inserted and read correctly
    tmpenviron['some_var'] = '你好'
    assert tmpenviron['some_var'] == '你好'

    # test that str objects that are not valid utf-8 fail

# Generated at 2022-06-13 16:44:52.905817
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pdb; pdb.set_trace()
    # The following methods are not available on Python 2.7, so this function is only tested on
    # Python 3.6 and later
    if not sys.version_info > (3, 6):
        print('Test not run as it only works on Python 3.6 and later')
        return
    os.environ['foo'] = 'bar'
    assert os.environ['foo'].__class__ == str
    assert os.environ['foo'] == 'bar'
    # No decode errors
    os.environ['foo'] = b'bar\xff'
    assert os.environ['foo'].__class__ == str
    assert os.environ['foo'] == 'bar�'  # is '\ufffd'
    # Decode errors
    os.environ['foo']

# Generated at 2022-06-13 16:45:02.614549
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    sys.modules['os'] = os

    class fake_environ:
        def __init__(self):
            self.environ = {
                'PATH': b'\xe5\x90\x95\xe5\x90\x95\xe5\x90\x95',
                'LANG': 'fr_FR.UTF-8',
                'PYTHONPATH': '\xe5\x90\x95\xe5\x90\x95\xe5\x90\x95'
            }

        def __contains__(self, key):
            return key in self.environ

        def __getitem__(self, key):
            return self.environ[key]

        def iteritems(self):
            return self.environ.iteritems()


    test

# Generated at 2022-06-13 16:45:12.556934
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    os_environ = {'ANSIBLE_MODULE_ARGS': '{"a":"b"}',
                  'ANSIBLE_FOO_BAR': '{"a":"b"}',
                  'ANSIBLE_FAILED': '1',
                  'ANSIBLE_END_MESSAGE': '{"message": "This is the end"}'}
    ansible_environ = _TextEnviron(os_environ)
    # Test with an element key that only requires decoding
    assert ansible_environ['ANSIBLE_MODULE_ARGS'] == '{"a":"b"}'
    # Test with an element key that requires decoding and JSON parsing
    assert ansible_environ['ANSIBLE_FOO_BAR'] == '{"a":"b"}'
    # Test with an element key that requires decoding and JSON parsing
    # and is a boolean


# Generated at 2022-06-13 16:45:18.875304
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(env={'ansible_lang': b'en_US.utf8', 'ansible_env': u'value'})
    assert isinstance(environ['ansible_lang'], str)
    assert environ['ansible_lang'] == 'en_US.utf8'
    assert isinstance(environ['ansible_env'], str)
    assert environ['ansible_env'] == 'value'



# Generated at 2022-06-13 16:45:27.631753
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == to_text(os.environ['PATH'], encoding='utf-8', nonstring='passthru',
                                      errors='surrogate_or_strict')
    assert environ['HOME'] == to_text(os.environ['HOME'], encoding='utf-8', nonstring='passthru',
                                      errors='surrogate_or_strict')
    assert environ['USER'] == to_text(os.environ['USER'], encoding='utf-8', nonstring='passthru',
                                      errors='surrogate_or_strict')
    # Test unicode handling

# Generated at 2022-06-13 16:45:33.322151
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    class Environ(object):
        def __init__(self):
            self._value_cache = {}
            self.LANG = 'en_US.UTF-8'
            self.DANGLING_NONUTF8 = b'\x80 '

        def __getitem__(self, key):
            return self._value_cache.get(key, self.__dict__[key])

    # os.environ is of type MutableMapping; environ is of type _TextEnviron
    # If os.environ and environ are the same object, changing one, changes the other
    old_env = os.environ
    os.environ = Environ()

    # Python3 behaves like _TextEnviron