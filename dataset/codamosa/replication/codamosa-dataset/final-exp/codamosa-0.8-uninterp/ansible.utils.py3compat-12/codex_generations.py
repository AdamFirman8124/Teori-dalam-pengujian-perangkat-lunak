

# Generated at 2022-06-13 16:35:54.930471
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron(encoding='utf-8')
    test_environ['ANSIBLE_CONFIG'] = 'tests/utils/ansible.cfg'
    assert test_environ['ANSIBLE_CONFIG'] == 'tests/utils/ansible.cfg'



# Generated at 2022-06-13 16:36:03.898049
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Can retrieve a unicode key from the environment
    key = 'Zz'
    value = b'0xff'
    os.environ[key] = value
    assert value == os.environ[key]
    # Can retrieve a unicode key which was encoded in the wrong encoding
    key = 'Zz'
    value = b'0xff'
    os.environ[key] = value
    assert value == os.environ[key]
    # If we set the environment variable to a unicode string, that is what we get back
    key = 'Zz'
    value = u'0xff'
    os.environ[key] = value
    assert value == os.environ[key]
    # If we ask for a non-unicode key, we get a byte string back
    key = b'Zz'
   

# Generated at 2022-06-13 16:36:06.599369
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    global environ
    environ = _TextEnviron(env={'A': 'B', b'C': b'D'}, encoding='utf-8')
    items = environ.items()
    print(items)

# Generated at 2022-06-13 16:36:14.650264
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test str
    assert environ.__getitem__('HOME') == os.environ['HOME']
    assert isinstance(environ.__getitem__('HOME'), str)

    # Test non-str
    os.environ['TEST_NONSTR'] = '1'
    environ['TEST_NONSTR'] = b'1'
    assert environ.__getitem__('TEST_NONSTR') == os.environ['TEST_NONSTR']
    assert isinstance(environ.__getitem__('TEST_NONSTR'), str)


# Generated at 2022-06-13 16:36:16.803633
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    assert environ['PYTHONIOENCODING'] == u'utf-8'

# Generated at 2022-06-13 16:36:18.935810
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({b'PYTHONPATH': b'foo:bar:baz'}, encoding='utf-8')
    assert test_environ['PYTHONPATH'] == u'foo:bar:baz'



# Generated at 2022-06-13 16:36:21.630415
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    env['key'] = b'value'
    assert 'value' == env['key']
    env['key'] = 'value'
    assert 'value' == env['key']

# Generated at 2022-06-13 16:36:26.321360
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # setup
    test_environ = _TextEnviron()
    test_environ.__setitem__('test_key', b'test_value')
    # test
    result = test_environ.__getitem__('test_key')
    assert result == 'test_value'

# Generated at 2022-06-13 16:36:34.766716
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    assert 'LANG' in environ, "Failed to find 'LANG' in {}".format(environ)
    assert environ['LANG'] == 'en_US.UTF-8'
    # If we set to a text string, we should get the text string back
    environ['LANG'] = 'en_US.ascii'
    assert environ['LANG'] == 'en_US.ascii'
    # If we set to a nonstring, we should get a text string back
    environ['LANG'] = 123
    assert environ['LANG'] == '123'

# Generated at 2022-06-13 16:36:45.333708
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import re
    import subprocess

    # The variable $LANG is a variable that contains trailing newline on some systems
    # and not on others.  We set it to a common value (en_US.UTF-8) and then capture
    # the value of $LANG from inside a subprocess
    env = os.environ.copy()
    env['LANG'] = 'en_US.UTF-8\n'
    proc = subprocess.Popen(['env'], env=env, stdout=subprocess.PIPE, universal_newlines=True)
    out, _err = proc.communicate()
    pattern = r'^LANG=en_US\.UTF-8$'
    matches = re.findall(pattern, out, re.MULTILINE)

# Generated at 2022-06-13 16:36:53.624968
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that we get the bytes back when we're on python2
    if not PY3:
        value = 'Hello World'
        environ._raw_environ[b'value'] = value
        assert (value == environ[b'value'])
        # Test that we get the text back when we're on python3
    else:
        value = 'Hello World'
        environ._raw_environ['value'] = value
        assert (value == environ['value'])


# Generated at 2022-06-13 16:37:00.363339
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    This unit test check the method __getitem__ of the class _TextEnviron.
    """
    unit_test_env1 = _TextEnviron({'key1': b'value1', 'key2': 'value2'}, encoding='utf-8')
    assert unit_test_env1['key1'] == 'value1'
    assert type(unit_test_env1['key1']) == str
    assert unit_test_env1['key2'] == 'value2'
    assert type(unit_test_env1['key2']) == str
    unit_test_env2 = _TextEnviron({'key1': b'\xc3\xa9', 'key2': '\u00E9'}, encoding='utf-8')
    assert unit_test_env2['key1'] == ' é '
   

# Generated at 2022-06-13 16:37:08.009430
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test if returned value is an ascii string
    os.environ['test'] = 'test'
    assert isinstance(environ['test'], str)

    # Test if returned value is a unicode string
    os.environ['test'] = 'öäü'
    assert isinstance(environ['test'], to_text('öäü', 'utf-8'))

    # Test if returned value is a unicode string
    os.environ['test'] = 'öäü'.encode('utf-8')
    assert isinstance(environ['test'], to_text('öäü', 'utf-8'))

    # Delete the test environment key
    del os.environ['test']



# Generated at 2022-06-13 16:37:11.986359
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    te = _TextEnviron(encoding='cp1251')
    environ['BOGUS_VAR'] = b'\xf0\xfb\xf9\xee'
    assert environ[b'BOGUS_VAR'] == u'пый'

# Generated at 2022-06-13 16:37:24.508523
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test that we get unicode strings back from environ"""
    # Test that we get text strings back when we ask for standard environment variable names
    assert isinstance(environ[u'HOME'], unicode)
    assert isinstance(environ['HOME'], unicode)

    # Test that we get text strings back when we ask for variable names which are already unicode
    # strings
    assert isinstance(environ[u'TEST'], unicode)

    # Test that we get text strings back when we ask for variable names which are byte strings
    # encoded with the filesystem encoding
    environ[u'TEST'] = b'/tmp'
    assert isinstance(environ[u'TEST'], unicode)

    environ[b'TEST'] = b'/tmp'

# Generated at 2022-06-13 16:37:35.698068
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ1 = _TextEnviron({b'TEST1': b'TESTVALUE'})
    assert environ1[b'TEST1'] == u'TESTVALUE'
    # Caching of decoded values should work
    environ1._value_cache[b'TESTVALUE'] = u'CACHED'
    assert environ1[b'TEST1'] == u'CACHED'
    environ2 = _TextEnviron({b'TEST1': b'TESTVALUE'}, encoding='utf-16')
    assert environ2[b'TEST1'] == u'TESTVALUE'
    # Caching of decoded values should work
    environ2._value_cache[b'TESTVALUE'] = u'CACHED'

# Generated at 2022-06-13 16:37:42.357021
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    environ = _TextEnviron(encoding='utf-8')

    # Test for str or bytes
    value = os.environ['PATH'] if sys.version_info[0] == 2 else os.environ[b'PATH']

    # Test for str or bytes
    if sys.version_info[0] == 2:
        assert isinstance(environ['PATH'], str)
    else:
        assert isinstance(environ['PATH'], str)

    # Test for str or bytes
    assert environ['PATH'] == value



# Generated at 2022-06-13 16:37:48.977154
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unicode string in non-standard encoding
    os.environ['TEST_INPUT_1'] = '\xad\x89'.encode('EUC-JP', 'surrogateescape')
    # Unicode string in standard ascii encoding
    os.environ['TEST_INPUT_2'] = u'\u00ad'.encode('ascii', 'surrogateescape')
    # ASCII bytes in standard encoding
    os.environ['TEST_INPUT_3'] = b'\xad'
    # ASCII bytes in non-standard encoding
    os.environ['TEST_INPUT_5'] = b'\xad'.decode('ascii', 'surrogateescape').encode('EUC-JP', 'surrogateescape')
    # Unicode string in non-standard encoding which cannot be decoded


# Generated at 2022-06-13 16:37:58.847394
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test_bytes_environment_variable
    # bytes environment variable
    b_key = 'ANSIBILITY_TEST_\xc3\xa4\xc3\xb6\xc3\xbc'
    b_value = 'ANSIBILITY_TEST_\xc3\xa4\xc3\xb6\xc3\xbc'
    os.environ[b_key] = b_value
    try:
        assert environ[b_key] == b_value
    finally:
        del os.environ[b_key]

    # test_bytes_environment_variable_ascii_key
    # bytes environment variable with ascii-only key
    b_key = 'ANSIBILITY_TEST_'

# Generated at 2022-06-13 16:38:06.357120
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Unit test for TextEnviron.get"""
    # pylint: disable=protected-access
    # XXX: Need __setitem__ to be tested in a separate unit test as this method is not set up to
    # test __setitem__
    os.environ['test_encoding'] = b'\xe3\x83\x86\xe3\x82\xb9\xe3\x83\x88'
    try:
        text_environ = _TextEnviron()
        assert text_environ['test_encoding'] == u'テスト'
        assert u'テスト' == text_environ['test_encoding']
    finally:
        del os.environ['test_encoding']



# Generated at 2022-06-13 16:38:14.289325
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    e = _TextEnviron()
    assert e['a'] == ''
    assert e['b'] == ''
    e['a'] = 'abc'
    assert e['a'] == 'abc'
    assert e['b'] == ''
    assert e['c'] == ''



# Generated at 2022-06-13 16:38:15.416000
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH'] == os.environ['PATH']

# Generated at 2022-06-13 16:38:17.387379
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ["test_value"] = "key"
    assert "key" == environ["test_value"]
    del environ["test_value"]


# Generated at 2022-06-13 16:38:19.038889
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['PATH']


# Generated at 2022-06-13 16:38:29.814461
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Test for method __getitem__ of class _TextEnviron
    '''
    # The user has set ANSIBLE_CONFIG to a specific config file
    environ.update({'ANSIBLE_CONFIG': '/home/user/ansible.cfg'})

    # If PY3 is true, we expect to get the env value without decoding
    if PY3:
        assert to_bytes('ANSIBLE_CONFIG') == environ[to_bytes('ANSIBLE_CONFIG')]

    # If PY3 is false, we expect to decode the env value, using
    # sys.getfilesystemencoding()
    else:
        assert to_text('ANSIBLE_CONFIG') == environ[to_bytes('ANSIBLE_CONFIG')]



# Generated at 2022-06-13 16:38:31.508097
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron({'a': '1', 'b': '2'}, 'utf-8')
    assert env['a'] == '1'

# Generated at 2022-06-13 16:38:38.122857
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Create the input data
    environ_dict = {'foo': u'bar', u'baz': b'qux', 'quux': b'\xe2\x80\x99'}
    # Create the object
    test_object = _TextEnviron(env=environ_dict)
    # Set up the expected results
    expected_result = {'foo': u'bar', 'baz': u'qux', 'quux': u'\u2019'}
    # Perform the test
    result = {k: test_object[k] for k in environ_dict}
    # Verify the result
    assert result == expected_result, 'Expected: {0}, Received: {1}'.format(expected_result, result)


# Generated at 2022-06-13 16:38:47.581531
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test that we can get a value from an environment variable
    assert environ['HOME'] == ''
    # Test that we can get a value from an environment variable that has changed
    os.environ['HOME'] = '/home/user1'
    assert environ['HOME'] == '/home/user1'
    del os.environ['HOME']
    # Test that we can get a value from an environment variable that changed back
    assert environ['HOME'] == ''
    os.environ['HOME'] = '/home/user1'
    assert environ['HOME'] == '/home/user1'
    # Test that we can get a value from an environment variable that contained a value that needed
    # to be decoded
    os.environ['HOME'] = u'utf8\u20ac'

# Generated at 2022-06-13 16:38:55.233905
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    try:
        environ.update({'a': to_bytes(u'a\u00a5', encoding='utf-8', nonstring='strict',
                                      errors='surrogate_or_strict')})
        print(environ['a'])
        assert(environ['a'] == u'a\u00a5')
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
        assert(False)
    except UnicodeEncodeError:
        print("UnicodeEncodeError")
        assert(False)
    except KeyError:
        print("KeyError")
        assert(False)


# Generated at 2022-06-13 16:39:01.324102
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _environ = _TextEnviron(encoding='iso-8859-15')
    # Ensure we get text back for ascii strings
    assert _environ['foo'] == u'bar'
    # Ensure we get text back for non-ascii strings
    assert _environ.get(u'unicöde') == u'ëncöding'



# Generated at 2022-06-13 16:39:08.522393
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ2 = _TextEnviron({b'ANSIBLE_MODULE_ARGS': b'{"foo":"bar"}',
                             b'ANSIBLE_MODULE_NAME': b'ping'},
                            encoding='utf-8')
    assert environ2[b'ANSIBLE_MODULE_ARGS'] == u'{"foo":"bar"}'

# Generated at 2022-06-13 16:39:11.581451
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron({'key1':'value1','key2':'value2'}, encoding='utf-8')
    environ['key3'] = 'value3'
    assert environ['key3'] == 'value3'
    assert 'key3' in environ
    assert len(environ) == 3
    del environ['key3']
    assert 'key3' not in environ
    assert len(environ) == 2

# Generated at 2022-06-13 16:39:14.487390
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['a'] == u'b'
    assert environ['c'] == to_text(b'\x80', encoding='utf-8', nonstring='passthru',
                                   errors='surrogate_or_strict')

# Generated at 2022-06-13 16:39:17.474717
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    expected = "value"
    env["key"] = "value"
    assert env["key"] == expected


# Generated at 2022-06-13 16:39:24.026669
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    assert environ['PATH'] == os.environ['PATH']
    assert environ['PATH'] == os.environ['PATH']
    assert environ['PATH'] == u'{0}:{1}'.format(os.path.dirname(__file__), os.environ['PATH'])


# Generated at 2022-06-13 16:39:32.290958
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # When PY3 is True, the method __getitem__ should return the value without modification
    environ._raw_environ['default_encoding'] = 'utf-8'
    assert environ.encoding == 'utf-8'
    assert environ['default_encoding'] == 'utf-8'

    # When PY3 is True, the method __getitem__ should return the value without modification
    environ._raw_environ['default_encoding'] = b'utf-8'
    assert environ.encoding == 'utf-8'
    assert environ['default_encoding'] == 'utf-8'

# Generated at 2022-06-13 16:39:39.890346
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """Test the __getitem__ method of _TextEnviron"""
    test_environ = _TextEnviron({b"TEST": b"1\xe9"}, 'utf-8')
    if PY3:
        assert test_environ[b"TEST"] == "1\xe9"
    else:
        assert test_environ[b"TEST"] == u"1\xe9"
    assert test_environ[u"TEST"] == u"1\xe9"


# Generated at 2022-06-13 16:39:41.947350
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    environ['mykey'] = 'myvalue'
    assert isinstance(environ['mykey'], text_type)

# Generated at 2022-06-13 16:39:47.288517
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ_copy = os.environ.copy()
    for env_var in environ_copy:
        assert environ[env_var] == os.environ[env_var], '{}: {} != {}'.format(env_var, environ[env_var], os.environ[env_var])

# Generated at 2022-06-13 16:39:57.299904
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit tests for _TextEnviron.__getitem__
    """

    environ = _TextEnviron(env=dict(), encoding='utf-8')
    value = 'test'

    # Test that we can retrieve strings from an empty environment
    environ['test'] = value
    assert environ['test'] == value

    # Test that we can retrieve strings from a environment with mixed byte and text strings
    environ_tmp = os.environ.copy()
    environ_tmp.update({to_text(key): value for key in environ_tmp.keys()})
    environ = _TextEnviron(env=environ_tmp, encoding='utf-8')
    assert environ['test'] == value



# Generated at 2022-06-13 16:40:12.306259
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test decoding nonascii chars
    environ['unicodestr'] = u'\u6c34\u5206\u8c37'
    assert b'\xe6\xb0\xb4\xe5\x88\x86\xe8\xb2\xa9' == os.environ[b'unicodestr']
    assert u'\u6c34\u5206\u8c37' == environ[b'unicodestr']

    with open('/dev/null', mode='wb') as fp:
        # Test surrogate escapes on PY2
        environ['badutf'] = u'\ufeff'
        assert b'\xef\xbb\xbf' == os.environ[b'badutf']

# Generated at 2022-06-13 16:40:22.929599
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # _TextEnviron(env) with env in not None
    environ_test1 = _TextEnviron({'a':'b', 'c':'d'})
    assert environ_test1._raw_environ['a'] == b'b'
    assert environ_test1._raw_environ['c'] == b'd'
    assert environ_test1['a'] == 'b'
    assert environ_test1['c'] == 'd'

    # _TextEnviron(env, encoding) with env not None and encoding not None
    environ_test2 = _TextEnviron({'a':'b', 'c':'d'}, encoding='utf-8')
    assert environ_test2._raw_environ['a'] == b'b'

# Generated at 2022-06-13 16:40:26.789721
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    print("----test__TextEnviron___getitem__----")
    print("---test__TextEnviron___getitem__---")
    print("--test__TextEnviron___getitem__--")

    from ansible.module_utils.common._collections_compat import MutableMapping



# Generated at 2022-06-13 16:40:28.802718
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['ANSIBLE_CONFIG'] == u'/etc/ansible/ansible.cfg'

# Generated at 2022-06-13 16:40:31.012047
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    _TextEnviron.__getitem__(environ, 'ansible_python_interpreter')

# Generated at 2022-06-13 16:40:37.413179
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_environ = _TextEnviron({'LANG': 'en_US.UTF-8'}, encoding='utf-8')
    if PY3:
        assert test_environ['LANG'] == u'en_US.UTF-8'
    else:
        assert test_environ['LANG'] == u'en_US.UTF-8'



# Generated at 2022-06-13 16:40:40.970336
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    text_environ = _TextEnviron()
    # Check if it works for normal case
    try:
        text_environ['PWD']
    except KeyError:
        assert False
    # Check if it works for non-existing environment variables
    try:
        text_environ['NOTEXIST']
    except KeyError:
        assert True


# Generated at 2022-06-13 16:40:51.356121
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    if PY3:
        os.environ[b'ANSIBLE_TEXT_ENV_TEST'] = b'foo'
    else:
        os.environ[b'ANSIBLE_TEXT_ENV_TEST'] = b'\x00'
    # Test whether caching behavior
    assert environ[b'ANSIBLE_TEXT_ENV_TEST'] == u'\x00'
    if PY3:
        os.environ[b'ANSIBLE_TEXT_ENV_TEST'] = b'bar'
    else:
        os.environ[b'ANSIBLE_TEXT_ENV_TEST'] = b'\x01'
    assert environ[b'ANSIBLE_TEXT_ENV_TEST'] == u'\x00'


# Generated at 2022-06-13 16:40:54.740699
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    key = u'SHELL'
    value = environ[key]
    assert isinstance(value, unicode)



# Generated at 2022-06-13 16:41:03.498872
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    DESCRIPTION:
        This function verifies that the __getitem__ function of class
        _TextEnviron returns the value of an environment variable as a text
        object.

    BEHAVIOR:
        The __getitem__ function of class _TextEnviron takes a single
        parameter, the name of an environment variable.  If the variable is
        defined, that variable's value is returned.  If the variable is
        not defined, the function raises a KeyError exception.

    EXPECTED RESULTS:
        Verify that the __getitem__ function returns the value of a defined
        environment variable as a text object.  Verify that the function
        raises a KeyError exception when attempting to return the value of
        a non-existent environment variable.
    """
    import os
    import sys


# Generated at 2022-06-13 16:41:22.463505
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Test with a text value
    assert environ['USER'] == 'root'
    # Test with a bytes value
    assert environ[u'LANG'] == u'en_US.UTF-8'
    # Test with a non-utf-8 value
    assert environ['USER'] == u'root'


# Generated at 2022-06-13 16:41:25.169450
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ['HOME'] == to_text(os.environ['HOME'], encoding='utf-8')
    assert environ['HOME'] == os.environ['HOME']



# Generated at 2022-06-13 16:41:32.934829
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
  # test with single byte unicode
  environ['test'] = '\u00a0'
  assert environ['test'] == '\u00a0'
  # test with double byte unicode
  environ['test'] = '\u0100'
  assert environ['test'] == '\u0100'
  # test with 3 and 4 byte unicode
  environ['test'] = '\U00010000'
  assert environ['test'] == '\U00010000'
  environ['test'] = '\U00010000'
  assert environ['test'] == '\U00010000'
  # test with unicode surrogate pairs
  environ['test'] = '\ud800\udc00'
  assert environ['test'] == '\ud800\udc00'

# Generated at 2022-06-13 16:41:36.939886
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron()
    key = "ANSIBLE_REMOTE_USER"
    value = environ[key]
    print(value)


# Generated at 2022-06-13 16:41:44.660452
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class MockEnv(object):
        """
        Mock object of os.environ which returns non-string keys
        """
        def __getitem__(self, key):
            if key == 'string':
                return 'value'
            elif key == 'byte':
                return b'value'
            elif key == 'int':
                return 1
            elif key == 'float':
                return 1.1

    test_obj = _TextEnviron(env=MockEnv())

    # python2
    if not PY3:
        # test case of str type
        assert test_obj['string'] == u'value'
        # test case of bytes type
        assert test_obj['byte'] == u'value'
        # test case of int type
        assert test_obj['int'] == u'1'
        #

# Generated at 2022-06-13 16:41:56.666156
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys
    import unittest

    class Test___TextEnviron___getitem__(unittest.TestCase):
        def setUp(self):
            self.old_environ = dict(os.environ)

        def tearDown(self):
            os.environ = self.old_environ

        def test_passthru(self):
            os.environ = {'LANG': 'en_US.utf8', 'PYTHONPATH': 'foo:bar:baz'}
            environ = _TextEnviron(encoding='utf-8')

            for key in os.environ:
                assert os.environ[key] == environ[key]


# Generated at 2022-06-13 16:42:03.710235
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    class utils(object):
        pass

    # Define test data
    environ_values = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Save original value of 'environ' in a module
    orig_environ = environ._raw_environ
    environ._raw_environ = environ_values
    # Test lhs and rhs of '==' if they are equal
    assert environ['key1'] == 'value1'
    assert environ['key2'] == 'value2'
    assert environ['key3'] == 'value3'
    # Restore original value of 'environ' in a module
    environ._raw_environ = orig_environ



# Generated at 2022-06-13 16:42:13.861415
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ.encoding == 'utf-8'

    # Ensure environment variable exist and is encoded in ANSI
    os.environ['a'] = 'a'
    os.environ['b'] = 'б'

    # Ansi environment variable is decoded
    assert environ['a'] == 'a'

    # Unicode environment variable is decoded to unicode
    assert environ['b'] == u'б'

    # If a key is not found than should be raised KeyError
    try:
        c = environ['c']
    except KeyError as e:
        assert str(e) == "'c'"


# Generated at 2022-06-13 16:42:17.940049
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    if PY3:
        assert env['ENV'] == os.environ['ENV']
    else:
        assert env['ENV'] == os.environ['ENV'].encode(sys.getfilesystemencoding()).decode(sys.getfilesystemencoding())

# Generated at 2022-06-13 16:42:26.767118
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Initialize test environment
    environ['TEST_KEY_1'] = 'value1'
    environ['TEST_KEY_2'] = 'value2'
    environ['TEST_KEY_3'] = 'value3'
    os.environ['TEST_KEY_1'] = 'value1'
    os.environ['TEST_KEY_2'] = 'value2'
    os.environ['TEST_KEY_3'] = 'value3'

    # Unit test for method __getitem__ of class _TextEnviron
    # Positive test: put unicode key
    assert environ['TEST_KEY_1'] == os.environ['TEST_KEY_1']

    # Positive test: put byte key

# Generated at 2022-06-13 16:42:56.228862
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = {}
    txt_env = _TextEnviron(env)
    env['key'] = 'val'
    assert txt_env['key'] == 'val'

    env['key'] = b'val'
    assert txt_env['key'] == 'val'

    env['key'] = 'val'
    assert txt_env['key'] == 'val'



# Generated at 2022-06-13 16:43:04.931120
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # test with PY3
    os.environ['TEST_ENV'] = 'abc中文'
    os.environ['TEST_ENV_NONASCII'] = '中文'
    os.environ['TEST_ENV_EMPTY'] = ''
    env = _TextEnviron(encoding='utf-8')

    assert os.environ['TEST_ENV'] == 'abc中文'
    assert env['TEST_ENV'] == 'abc中文'

    assert os.environ['TEST_ENV_NONASCII'] == '中文'
    assert env['TEST_ENV_NONASCII'] == '中文'

    assert os.environ['TEST_ENV_EMPTY'] == ''

# Generated at 2022-06-13 16:43:16.674206
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ = _TextEnviron(encoding='utf-8')
    environ['text_key'] = 'value with ᴜɴɪᴄᴏᴅᴇ'
    assert environ['text_key'] == 'value with ᴜɴɪᴄᴏᴅᴇ'

    environ = _TextEnviron(encoding='utf-8')
    environ['invalid_utf8_key'] = b'value with invalid \xc3\x62\xc3\xa5\n'
    assert environ['invalid_utf8_key'] == 'value with invalid \ufffd\ufffd\ufffd\n'

    environ = _TextEnviron(encoding='utf-8')

# Generated at 2022-06-13 16:43:24.292837
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils.six import StringIO

    # Test with a unicode key set with a unicode value
    key = '\u00e4\u00f6\u00fc'
    environ[key] = key
    assert environ[key] == key

    # Test with a unicode key set with a byte string value
    key = '\u00e4\u00f6\u00fc'
    environ[key] = to_bytes(key, encoding='utf-8')
    assert environ[key] == key

    # Test with a byte string key set with a unicode value
    key = to_bytes(key, encoding='utf-8')
    environ[key] = key
    assert environ[key] == key

    # Test with a byte string key set with a byte string value
   

# Generated at 2022-06-13 16:43:32.380295
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Testing the entire _TextEnviron class is a bit cumbersome, so just test the __getitem__
    # method
    class environ(object):
        '''
        Dummy class to imitate os.environ
        '''
        def __init__(self, value):
            self._value = value
        def __getitem__(self, key):
            return self._value

    # Make sure the behavior matches os.environ when decoding works
    _TextEnviron(environ('this is a utf-8 string'))['key'] == os.environ['key']
    # Make sure the behavior matches os.environ when decoding fails
    # (Technically this is only true on Python3, but it's not worth caring about Python2 here)

# Generated at 2022-06-13 16:43:37.853264
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    env = _TextEnviron()
    os.environ['LANG'] = 'en_US.UTF-8'
    assert os.environ['LANG'] == env['LANG'] == 'en_US.UTF-8'
    os.environ['LANG'] = b'en_US.UTF-8'
    assert os.environ['LANG'] == env['LANG'] == 'en_US.UTF-8'


# Generated at 2022-06-13 16:43:42.618791
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import pytest

    ret = _TextEnviron({'foo': 'bar'})
    assert ret['foo'] == 'bar'

    ret = _TextEnviron({u'foo': u'bar'})
    if PY3:
        assert ret['foo'] == u'bar'
    else:
        assert ret['foo'] == 'bar'

# Generated at 2022-06-13 16:43:44.226754
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    '''
    Unit test for method __getitem__ of class _TextEnviron
    '''
    env = _TextEnviron()
    assert env['PATH'] is not None

# Generated at 2022-06-13 16:43:49.944106
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    testenv = _TextEnviron(encoding='utf-8')
    testenv['TEST_VAR'] = "This is a test"
    assert testenv['TEST_VAR'] == "This is a test"
    testenv['TEST_VAR'] = "This is a test\u30b3"
    assert testenv['TEST_VAR'] == "This is a test\u30b3"


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 16:43:54.007808
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ.clear()
    assert len(environ) == 0
    assert environ.get('TEST_KEY', None) == None
    environ['TEST_KEY'] = 'test value'
    assert environ['TEST_KEY'] == 'test value'
    environ.clear()
    assert len(environ) == 0
    assert environ.get('TEST_KEY', None) == None

# Generated at 2022-06-13 16:44:54.573862
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    dummy_environ = {}
    dummy_environ['DUMMY_VAR'] = 'dummy_var'
    dummy_environ[b'DUMMY_VAR_BYTES'] = b'dummy_var_bytes'
    dummy_environ[u'DUMMY_VAR_UNICODE'] = u'dummy_var_unicode'
    dummy_environ[b'DUMMY_VAR_BYTES_UNICODE'] = u'dummy_var_bytes_unicode'
    dummy_environ[u'DUMMY_VAR_UNICODE_BYTES'] = b'dummy_var_unicode_bytes'
    for key in dummy_environ:
        dummy_env = _TextEnviron(env={}, encoding='utf-8')
        dummy_env[key] = dummy

# Generated at 2022-06-13 16:45:03.619615
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    import os
    import sys

    # Set some environment variables
    os.environ['test1'] = 'Value'
    os.environ['test2'] = 'Value2'
    os.environ['test3'] = b'Value3'
    os.environ['test4'] = b'Value4'

    # Test with defaults
    result = environ['test1']
    assert result == 'Value'

    result = environ['test2']
    assert result == 'Value2'

    result = environ['test3']
    assert result == b'Value3'

    result = environ['test4']
    assert result == b'Value4'

    # Set some environment variables
    os.environ['test1'] = b'Value'
    os.environ['test2'] = b'Value2'

    #

# Generated at 2022-06-13 16:45:07.215064
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    test_env = _TextEnviron(env={'ANSIBLE_TEST_VAR': u'ansible'})
    assert test_env['ANSIBLE_TEST_VAR'] == u'ansible'



# Generated at 2022-06-13 16:45:14.843985
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text
    import os

    environ['TEST_UNICODE'] = u'\u03b1\u03b2\u03b3'.encode('utf-8')
    assert to_text(u'\u03b1\u03b2\u03b3') == environ['TEST_UNICODE']

    # Test that we get unicode back out of the environment on all Python versions
    assert os.environ['TEST_UNICODE'] == u'\u03b1\u03b2\u03b3'.encode('utf-8')
    assert environ['TEST_UNICODE'] == to_text(u'\u03b1\u03b2\u03b3')

    # Test that we can get

# Generated at 2022-06-13 16:45:21.368173
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    """
    Unit test for method __getitem__ of class _TextEnviron

    :return:
    """
    dicts = dict()
    dicts['key1'] = '123'
    dicts['key2'] = '你好'
    dicts['key3'] = 'test'
    obj = _TextEnviron(env=dicts)
    assert obj['key1'] == '123'
    assert obj['key2'] == '你好'
    assert obj['key3'] == 'test'



# Generated at 2022-06-13 16:45:24.410875
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    assert environ["LANG"] == "en_US.UTF-8"
    assert environ["THIS_IS_A_KEY_THAT_WONT_EXIST"] == "THIS_IS_A_KEY_THAT_WONT_EXIST"

# Generated at 2022-06-13 16:45:31.176185
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    from ansible.module_utils._text import to_bytes, to_text

    # Setup
    key = u'ANSIBLE_TEST_STRING'
    value = u'Iñtërnâtiônàlizætiøn'

    # Need to delete the key if it already exists so that the test will run properly on Windows
    # where environ never actually deletes a key.
    # Windows: even if 'del environ[key]' is called, the key still exists
    environ.pop(key, None)

    # Execute
    environ[key] = value
    test_value = environ[key]

    # Ensure we don't get a duplicate value in the cache
    test_value_2 = environ[key]

    # Test
    assert value == test_value
    assert test_value == test_

# Generated at 2022-06-13 16:45:39.217709
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    environ._raw_environ = {u'Ключ': u'Значение'}
    assert environ[u'Ключ'] == u'Значение'
    environ._raw_environ = {u'Ключ': u'\u2603'}
    assert environ[u'Ключ'] == u'☃'
    environ._raw_environ = {u'Ключ': u'\U0001f61c'}
    assert environ[u'Ключ'] == u'😜'

# Generated at 2022-06-13 16:45:45.310849
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():

    # Test Strings in: cp1252
    #
    # Strings out: utf-8
    # os.environ[u'\u0411\u0435\u0437Dir']
    tstEnv_env = {'\xda\xa1\xe5\x97': 'test'}
    tstEnv_x = _TextEnviron(env=tstEnv_env, encoding='utf-8')
    assert tstEnv_x['\xda\xa1\xe5\x97'] == u'test'

    # Strings in: utf-8
    #
    # Strings out: utf-8
    # os.environ[u'\u0411\u0435\u0437Dir']

# Generated at 2022-06-13 16:45:54.837822
# Unit test for method __getitem__ of class _TextEnviron
def test__TextEnviron___getitem__():
    # Unit test for method __getitem__ of class _TextEnviron
    # Test creation
    text_environ = _TextEnviron(encoding='ascii')
    # Test unicode values
    os.environ['ANSIBLE_TEST_UNICODE_KEY'] = u'test'
    assert text_environ['ANSIBLE_TEST_UNICODE_KEY'] == 'test'
    # Test byte values
    os.environ['ANSIBLE_TEST_BYTES_KEY'] = b'test'
    assert text_environ['ANSIBLE_TEST_BYTES_KEY'] == 'test'
    # Test non-ascii unicode values
    os.environ['ANSIBLE_TEST_NONASCII_KEY'] = u'Ω'