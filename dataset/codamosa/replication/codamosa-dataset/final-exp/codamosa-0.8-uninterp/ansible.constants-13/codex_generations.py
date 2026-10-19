

# Generated at 2022-06-22 11:19:24.338958
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_BECOME_METHOD == 'sudo'
    assert DEFAULT_SUDO_PASS == 'sudo'
    assert DEFAULT_SU_PASS == 'su'
    assert DEFAULT_REMOTE_USER == 'root'
    assert DEFAULT_REMOTE_PORT == 22
    assert DEFAULT_TIMEOUT == 10
    assert MAX_FAIL_PERCENTAGE == 0
    assert DEFAULT_TRANSPORT == 'smart'

# Generated at 2022-06-22 11:19:30.109313
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_seq = ['a', 'b', 'c']
    actual = _DeprecatedSequenceConstant(test_seq, 'test_seq not evaluated', '2.7')
    assert actual._value == test_seq
    assert actual._msg == 'test_seq not evaluated'
    assert actual._version == '2.7'
    assert len(test_seq) == len(actual)
    assert actual[0] == test_seq[0]
    assert isinstance(actual, Sequence)


# Generated at 2022-06-22 11:19:43.829206
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    import copy
    import sys
    import traceback

    class TestClass:
        ''' Build this class to test the constructor of _DeprecatedSequenceConstant '''

        def __init__(self, value, msg, version):
            self.value = value
            self.msg = msg
            self.version = version

        def test_action(self):
            ''' Test this method by calling the constructor of _DeprecatedSequenceConstant '''
            test_object = _DeprecatedSequenceConstant(self.value, self.msg, self.version)

            assert_list = []
            assert_list.append(test_object == self.value)
            assert_list.append(test_object.__len__() == len(self.value))

# Generated at 2022-06-22 11:19:46.391960
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    s = _DeprecatedSequenceConstant([1,2,3], 'msg', 'test')
    assert len(s) == 3
    assert s[1] == 2

# Generated at 2022-06-22 11:19:52.465687
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Ensure _DeprecatedSequenceConstant.__getitem__ does not throw an exception.
    # This is not a complete test for the method, merely a smoke test to ensure it does not throw an exception.
    # This test can be removed if a more comprehensive test is added that covers every possible scenario.
    from unittest import mock
    mock_warning_function = mock.MagicMock()
    _DeprecatedSequenceConstant(['foo', 'bar'], "Testing _DeprecatedSequenceConstant", "v2.10").__getitem__(0)
    _DeprecatedSequenceConstant(('foo', 'bar'), "Testing _DeprecatedSequenceConstant", "v2.10").__getitem__(0)

# Generated at 2022-06-22 11:20:05.124802
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = ['a', 'b', 'c']
    test_msg = 'Warning message'
    test_version = '2.9'
    test_dep_seq = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_dep_seq) == 3
    assert [test_dep_seq[i] for i in range(0, 3)] == test_value


# FIXME: to be deprecated/removed at 2.9 ... now that config is also
#        used by plugins, we need to preserve any existing values.

# Generated at 2022-06-22 11:20:07.490034
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_constant', 1)
    assert test_constant == 1

test_set_constant()

# Generated at 2022-06-22 11:20:10.349401
# Unit test for function set_constant
def test_set_constant():
    set_constant('a', True)

    if a:
        assert True
    else:
        assert False

# Generated at 2022-06-22 11:20:22.682229
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('foo', 42, export)
    assert export['foo'] == 42

test_set_constant()

# FIXME: these should be moved to utils/jinja
ACTION_NAMES = (
    _ACTION_DEBUG,
    _ACTION_IMPORT_PLAYBOOK,
    _ACTION_IMPORT_ROLE,
    _ACTION_IMPORT_TASKS,
    _ACTION_INCLUDE,
    _ACTION_INCLUDE_ROLE,
    _ACTION_INCLUDE_TASKS,
    _ACTION_INCLUDE_VARS,
    _ACTION_META,
    _ACTION_SETUP,
    _ACTION_SET_FACT,
)

VALID_EXTENSIONS = ('.yml', '.yaml', '.json')


# Generated at 2022-06-22 11:20:26.159063
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    deprecated_list = _DeprecatedSequenceConstant(value=list(), msg="Test", version="0.1")
    assert(len(deprecated_list) == 0)

# Generated at 2022-06-22 11:20:41.749364
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    orig_len = len
    try:
        # mock __len__
        def stub__len__(self):
            return orig_len(self._value)

        _DeprecatedSequenceConstant.__len__ = stub__len__

        mock_value = (1, 2, 3)
        mock_msg = 'test_len'
        mock_version = '0.0.1'
        target = _DeprecatedSequenceConstant(mock_value, mock_msg, mock_version)
        actual = len(target)
        expected = 3
        assert actual == expected, 'actual is %s, expected is %s' % (actual, expected)
    finally:
        _DeprecatedSequenceConstant.__len__ = orig_len

# Generated at 2022-06-22 11:20:47.708713
# Unit test for function set_constant
def test_set_constant():
    global test_var

    assert 'test_var' not in globals()

    set_constant('test_var', 'value')
    assert test_var == 'value'

    set_constant('test_var', [1, 2, 3])
    assert test_var == [1, 2, 3]

    set_constant('test_var', dict(a='a', b='b'))
    assert test_var == dict(a='a', b='b')

    del test_var

# Generated at 2022-06-22 11:20:59.253815
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_BECOME_PASS == '~/.ansible/become-pass'


# FIXME: deprecate usage of the constants below and remove them (need to sanitize the whole code base first)
for item in ('PARAMIKO_RECORD_HOST_KEYS', 'USE_KERBEROS'):
    setattr(config, item, locals()[item])
CONNECTION_RETRIES = config.get_config_value('DEFAULT', 'connection_retries', 2)
DEFAULT_MODULE_NAME = config.get_config_value('DEFAULT', 'module_name', 'command')
DEFAULT_KEEP_REMOTE_FILES = config.get_config_value('DEFAULT', 'keep_remote_files', False)

# Generated at 2022-06-22 11:21:02.926723
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Check that _DeprecatedSequenceConstant behaves as expected
    lst = _DeprecatedSequenceConstant([1, 2, 3], 'test', '2.5')

    assert len(lst) == 3, 'Unexpect length'
    # Check that the message will be displayed
    assert len(lst) == 3, 'Unexpected length'



# Generated at 2022-06-22 11:21:06.811060
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_seq = _DeprecatedSequenceConstant(['one', 'two', 'three'], 'test message', '1.0')
    assert len(test_seq) == 3

# Generated at 2022-06-22 11:21:12.088462
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    # 1. Test when self._value is a list
    value = [1, 2, 3]
    msg = 'test'
    version = '1.0'
    expected_result = 3
    assert len(_DeprecatedSequenceConstant(value, msg, version)) == expected_result

    # 2. Test when self._value is a string
    value = 'test_str'
    expected_result = 9
    assert len(_DeprecatedSequenceConstant(value, msg, version)) == expected_result


# Generated at 2022-06-22 11:21:21.714850
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # not deprecated, items are given
    assert len(_DeprecatedSequenceConstant(['a', 'b'], "test", "3.0")) == 2
    # not deprecated, no items are given
    assert len(_DeprecatedSequenceConstant([], "test", "3.0")) == 0
    # deprecated, items are given
    assert len(_DeprecatedSequenceConstant(['a', 'b'], "test", "0.0")) == 2
    # deprecated, no items are given
    assert len(_DeprecatedSequenceConstant([], "test", "0.0")) == 0


# Generated at 2022-06-22 11:21:23.339767
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'test_msg', 'test_version')) == 3

# Generated at 2022-06-22 11:21:26.940810
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    msg = "msg1"
    version = "version1"

    value = _DeprecatedSequenceConstant(Sequence(), msg, version)

    assert msg in value[0]
    assert version in value[0]

# Generated at 2022-06-22 11:21:29.301047
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    obj = _DeprecatedSequenceConstant(['a', 'b'], 'message', 'version')
    assert len(obj) == 2


# Generated at 2022-06-22 11:21:37.823864
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant(None, u'a', u'b')
    assert len(a) == 0
    assert a[:] == []


# Validates a string against a blacklist of invalid characters

# Generated at 2022-06-22 11:21:43.923831
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Check that constructor is working as expected
    value = ('foo', 'bar')
    msg = 'My msg'
    version = '2.0'
    deprecated_seq = _DeprecatedSequenceConstant(value, msg, version)
    assert deprecated_seq._value == value
    assert deprecated_seq._msg == msg
    assert deprecated_seq._version == version


# Generated at 2022-06-22 11:21:46.089359
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')
    assert constant[0] == 1


# Generated at 2022-06-22 11:21:48.469317
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    for _ in range(0, 10):
        assert len(_DeprecatedSequenceConstant([], '', '')) == 0

# Generated at 2022-06-22 11:21:53.089136
# Unit test for function set_constant
def test_set_constant():
    constants = {}
    set_constant('ANSIBLE_TEST', 123, export=constants)
    assert constants['ANSIBLE_TEST'] == 123

    set_constant('ANSIBLE_TEST_2', 'abc', export=constants)
    assert constants['ANSIBLE_TEST_2'] == 'abc'

# Generated at 2022-06-22 11:21:59.099952
# Unit test for function set_constant
def test_set_constant():
    '''asserts the first argument of a call to set_constant matches second'''
    def _set_constant(*args):
        '''helper function for testing'''
        set_constant(*args)
    try:
        _set_constant('TEST_CONSTANT', 5)
        assert TEST_CONSTANT == 5
    except NameError:
        assert False, "NameError: Failed to set constant"
test_set_constant()

# Generated at 2022-06-22 11:22:01.385332
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    VALUE = ('a', 'b')
    OBJ = _DeprecatedSequenceConstant(VALUE, 'msg', 'version')

    assert len(VALUE) == len(OBJ)

# Generated at 2022-06-22 11:22:12.738813
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    import unittest
    class AssertClass(unittest.TestCase):
        def test__DeprecatedSequenceConstant(self):
            self.assertIsInstance(_DeprecatedSequenceConstant(value=[], msg="msg", version="2.3"), _DeprecatedSequenceConstant)
            self.assertRaises(TypeError, _DeprecatedSequenceConstant, value=None, msg="msg", version="2.3")
            self.assertRaises(TypeError, _DeprecatedSequenceConstant, value=list, msg="msg", version="2.3")
            self.assertRaises(TypeError, _DeprecatedSequenceConstant, value=[], msg=1, version="2.3")
            self.assertRaises(TypeError, _DeprecatedSequenceConstant, value=[], msg="msg", version=None)
   

# Generated at 2022-06-22 11:22:15.826854
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = _DeprecatedSequenceConstant(['a', 'b'], 'msg', '1.0')

    assert len(test_value) == 2

# Generated at 2022-06-22 11:22:19.898441
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_VERSION == __version__
    assert ANSIBLE_TRANSPORT == 'smart'
    assert ANSIBLE_TIMEOUT == 10
    assert DEFAULT_KEEP_REMOTE_FILES == False

# Generated at 2022-06-22 11:22:28.830335
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['k1', 'k2'], 'msg', 'ver')) == 2


# Generated at 2022-06-22 11:22:31.206570
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], '', '')) == 0


# Generated at 2022-06-22 11:22:39.344045
# Unit test for function set_constant
def test_set_constant():
    assert set_constant('x', 5) == {'x': 5}
    assert set_constant('x', 'foo') == {'x': 'foo'}
    assert set_constant('x', 5, {'y': 1}) == {'y': 1, 'x': 5}
    assert set_constant('x', 'foo', {'y': 1}) == {'y': 1, 'x': 'foo'}
    assert set_constant('x', 5, {'x': 1}) == {'x': 5}
    assert set_constant('x', 'foo', {'x': 1}) == {'x': 'foo'}



# Generated at 2022-06-22 11:22:49.174628
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # Test class attribute _msg
    def msg_method():
        return 'testing message'

    def version_method():
        return '3.1.0'

    # Test class attribute _value
    random_list = [1,2,3,4,5]

    _value = _DeprecatedSequenceConstant(random_list,
                                         msg_method,
                                         version_method)

    assert _value._value == random_list
    assert _value._msg == 'testing message'
    assert _value._version == '3.1.0'

    assert _value[0] == 1
    assert _value[-1] == 5

    # Test list length
    assert len(random_list) == len(_value)

    # Test list slicing
    assert random_list[1] == _value[1]
    assert random_

# Generated at 2022-06-22 11:22:52.500146
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    testvalue = [1, 2]
    testmsg = "message"
    testversion = "2.3"
    _DeprecatedSequenceConstant(testvalue, testmsg, testversion)

# Generated at 2022-06-22 11:23:04.713136
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class TestClass(object):

        def __init__(self, msg, version='1.1'):
            self.value = [1, 2, 3, 4, 5]
            self.msg = msg
            self.version = version

        def __len__(self):
            return len(self.value)

        def __getitem__(self, y):
            return self.value[y]

    testobj = TestClass('Test object')
    test_obj1 = _DeprecatedSequenceConstant(testobj, testobj.msg, testobj.version)

    assert len(test_obj1) == len(testobj)
    assert test_obj1[0] == testobj[0]
    assert test_obj1[1] == testobj[1]

test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:23:13.948147
# Unit test for function set_constant
def test_set_constant():
    for setting in config.data.get_settings():
        if setting.origin != 'default':
            continue

        from ansible.config.constants import set_constant

        # This can't be tested in a sane way, because it will pick
        # up stuff from this file, the config file, and any other
        # file that has been imported.
        if setting.name in ('DEFAULT_ROLES_PATH', 'DEFAULT_ROLES_PATH_ANSIBLE_GALAXY', 'DEFAULT_ROLES_PATH_ANSIBLE_COLLECTIONS'):
            continue

        assert config.get_config_value(setting.name) == value

# Generated at 2022-06-22 11:23:17.115089
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([1,2,3], "blah", "1.4")
    assert len(a)  == 3
    assert a[1] == 2


# Generated at 2022-06-22 11:23:22.952356
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    my_list = ['first', 'second']
    msg = "Test Message"
    version = "2.0"

    dsc = _DeprecatedSequenceConstant(my_list, msg, version)
    assert dsc.__getitem__(0) == my_list[0]
    assert dsc.__getitem__(1) == my_list[1]

# Generated at 2022-06-22 11:23:28.109660
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    tuple_msg = (1, 2, 3)
    msg = 'this is my message'
    version = '2.9'
    const = _DeprecatedSequenceConstant(tuple_msg, msg, version)
    assert const.__len__() == len(tuple_msg)
    assert const.__getitem__(1) == tuple_msg[1]

# Generated at 2022-06-22 11:23:43.452738
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    x = _DeprecatedSequenceConstant(('foo', 'bar'), 'msg', 'version')
    assert x[0] == 'foo'
    assert x[1] == 'bar'


# Generated at 2022-06-22 11:23:47.281706
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = _DeprecatedSequenceConstant(
        [0, 1, 2],
        msg="Unittest message",
        version="Unittest version"
    )
    assert value[0] == 0
    assert value[1] == 1
    assert value[2] == 2


# Generated at 2022-06-22 11:23:57.099512
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    from ansible.module_utils.six import PY2, PY3
    if PY2:
        # Make sure __getslice__ is not called
        # (http://stackoverflow.com/a/54589564/723090)
        class FailOnGetSlice(object):
            def __getitem__(self, i):
                return 2

            def __getslice__(self, i, j):
                assert 0
        fail = FailOnGetSlice()[1:2]

        # string-like object
        x = _DeprecatedSequenceConstant('hello world', '%s is deprecated as of Ansible 2.13', '3.0')
        assert len(x) == len('hello world')
        assert x[0:5] == 'hello'

        # list-like object

# Generated at 2022-06-22 11:24:01.400206
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # test for exception
    with pytest.raises(Exception):
        _DeprecatedSequenceConstant(None, None, None).__getitem__(None)
    # test for no exception
    _DeprecatedSequenceConstant([], 'testmsg', 'testver').__getitem__(None)



# Generated at 2022-06-22 11:24:03.756074
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    a = _DeprecatedSequenceConstant((1, 2), 'getitem() test', 'v2.0')
    assert a[0] == 1
    assert a[1] == 2

# Generated at 2022-06-22 11:24:07.417882
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c1 = _DeprecatedSequenceConstant(['1', '2', '3'], 'msg', 'version')
    assert(len(c1) == 3)


# Generated at 2022-06-22 11:24:15.006825
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR', export=vars())
    assert FOO == 'BAR'
    set_constant('FOO', 'BAZ', export=vars())
    assert FOO == 'BAZ'
    set_constant('FOO', ['BAR'], export=vars())
    assert FOO == ['BAR']
    set_constant('FOO', ['BAZ'], export=vars())
    assert FOO == ['BAZ']

# Generated at 2022-06-22 11:24:16.933398
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(None, None, None)) is None


# Generated at 2022-06-22 11:24:27.629913
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test with valid value of msg and version
    value = ['abc','def','xyz']
    msg = "msg"
    version = "version"
    test = _DeprecatedSequenceConstant(value, msg, version)
    assert(len(test) == 3)
    assert(test[0] == 'abc')
    assert(test[1] == 'def')
    assert(test[2] == 'xyz')

    # Test with invalid value of msg and version
    value = ['abc','def','xyz']
    invalid_type_msg = test
    invalid_type_version = test
    test = _DeprecatedSequenceConstant(value, invalid_type_msg, invalid_type_version)
    assert(len(test) == 3)
    assert(test[0] == 'abc')

# Generated at 2022-06-22 11:24:32.799759
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dict = _DeprecatedSequenceConstant(value=('a', 'b', 'c'), msg="This is a message", version="1.0")
    assert dict[0] == 'a'
    assert dict[1] == 'b'
    assert dict[2] == 'c'

# Generated at 2022-06-22 11:24:48.878728
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_ANSIBLE_CONFIG', 'TEST_ANSIBLE_CONFIG_VALUE')
    assert globals()['TEST_ANSIBLE_CONFIG'] == 'TEST_ANSIBLE_CONFIG_VALUE'

# Generated at 2022-06-22 11:24:52.074803
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_value = 'value'
    test_msg = 'msg'
    test_version = 'version'
    test_DeprecatedSequenceConstant = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert test_DeprecatedSequenceConstant[0] == test_value

# Generated at 2022-06-22 11:24:56.220009
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert len(a) == 3
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 3

# Generated at 2022-06-22 11:25:01.499853
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    set_constant('INTERNAL_RESULT_KEYS', ('foo',))
    assert INTERNAL_RESULT_KEYS[0] == 'foo'

if __name__ == '__main__':
    import pytest
    pytest.main(['-xvs', __file__])

# Generated at 2022-06-22 11:25:03.998843
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant([1, 2], 'msg', 'version'), _DeprecatedSequenceConstant)


# Generated at 2022-06-22 11:25:06.604633
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant([1,2,3], 'test', '2.0')
    assert len(constant) == 3


# Generated at 2022-06-22 11:25:12.273645
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from unittest import TestCase

    class MyTestCase(TestCase):
        def test__getitem__(self):
            self.assertEqual(_DeprecatedSequenceConstant(
                value=['a', 'b', 'c'],
                msg='msg',
                version='version'
            )[1], 'b')
    my_test_case = MyTestCase()
    my_test_case.test__getitem__()


# Generated at 2022-06-22 11:25:20.826992
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """Ensure the `DeprecatedSequenceConstant` behaves as expected."""
    # Test the _DeprecatedSequenceConstant behaves as expected, i.e. the getitem method
    # behaves as a standard sequence's getitem.
    d = _DeprecatedSequenceConstant((1, 2, 3), '', '')
    assert d[1] == 2
    assert slice(1, 3) == slice(1, 3)

    # Test the _DeprecatedSequenceConstant raises an IndexError when the index is out of range.
    class _CustomException(Exception):
        pass

    try:
        d[3]
    except IndexError:
        pass
    else:
        raise _CustomException('IndexError not raised!')

    # Test the _DeprecatedSequenceConstant raises a TypeError when the index is not int.

# Generated at 2022-06-22 11:25:22.951711
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], '', '')) == 3, '__len__ method of class _DeprecatedSequenceConstant does not work'

# Generated at 2022-06-22 11:25:27.914382
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    """ Unit test for method __getitem__ of class _DeprecatedSequenceConstant """
    seq = _DeprecatedSequenceConstant((1, 2, 3), 'This is deprecated', 'v3.4')
    assert seq[0] == 1
    assert seq[1] == 2
    assert seq[2] == 3

# Generated at 2022-06-22 11:26:02.926552
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert len(INTERNAL_RESULT_KEYS) == 2
    assert len(_DeprecatedSequenceConstant(INTERNAL_RESULT_KEYS, "this message should appear twice.", "2.10")) == 2

    assert len(_DeprecatedSequenceConstant(['a','b','c','d'], "this message should appear four times.", "3.10")) == 4
    assert _DeprecatedSequenceConstant(['a','b','c','d'], "this message should appear four times.", "3.10")[0] == 'a'
    assert _DeprecatedSequenceConstant(['a','b','c','d'], "this message should appear four times.", "3.10")[1] == 'b'

# Generated at 2022-06-22 11:26:05.410901
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([1, 2, 3], "hello", "1.0") == [1, 2, 3]

# Generated at 2022-06-22 11:26:15.027197
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test when the message is a string
    tsc = _DeprecatedSequenceConstant([1, 2, 3], 'abc', '2.6')
    assert len(tsc) == 3, 'The method __len__ failed to return the length of the object.'

    # Test when the message is a list
    tsc = _DeprecatedSequenceConstant([1, 2, 3], ['abc'], '2.6')
    assert len(tsc) == 3, 'The method __len__ failed to return the length of the object.'

    # Test when the message is a tuple
    tsc = _DeprecatedSequenceConstant([1, 2, 3], ('abc',), '2.6')
    assert len(tsc) == 3, 'The method __len__ failed to return the length of the object.'


# Generated at 2022-06-22 11:26:23.351072
# Unit test for function set_constant
def test_set_constant():
    import ansible.constants as C
    set_constant('TEST_CONSTANT_A', 'A')
    set_constant('TEST_CONSTANT_B', 'B')
    assert C.TEST_CONSTANT_A == 'A'
    assert C.TEST_CONSTANT_B == 'B'
    assert hasattr(C, 'TEST_CONSTANT_A')
    assert hasattr(C, 'TEST_CONSTANT_B')

# Constant for stdout/stderr encoding
DEFAULT_STDOUT_ENCODING = 'utf-8'
DEFAULT_STDERR_ENCODING = 'utf-8'

# Generated at 2022-06-22 11:26:30.434454
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    """
    This is a unit test to check if creating and using your own class
    which subclasses Sequence works, in case of using _DeprecatedSequenceConstant.
    """
    from ansible.module_utils.six import PY3
    a = _DeprecatedSequenceConstant([], 'This is a warning message.', '2.9')
    if PY3:
        assert(isinstance(a, Sequence))
    assert(len(a) == 0)
    assert(a[0] == None)


# Generated at 2022-06-22 11:26:34.217724
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq_cons = _DeprecatedSequenceConstant([1,2,3,4], "Should not use", "2.9")
    assert len(seq_cons) == 4

# Generated at 2022-06-22 11:26:45.132400
# Unit test for function set_constant

# Generated at 2022-06-22 11:26:53.404898
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    from ansible.utils.vars import AnsibleVars
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader

    context = dict(var0='var0', var1='var1')
    loader = DataLoader()
    options = dict(vars=dict(A='B', C='D'))
    var_manager = AnsibleVars(loader=loader, context=context, options=options)

    value = _DeprecatedSequenceConstant(value=[u'{{var0}}', u'{{var1}}'], msg='deprecated', version='1.0')
    assert value == [u'var0', u'var1']

# Generated at 2022-06-22 11:27:04.289596
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # __getitem__ of class _DeprecatedSequenceConstant should return the indexed item of _DeprecatedSequenceConstant"s _value and call _deprecated method
    from ansible.module_utils.parsing.convert_bool import BOOLEANS
    from unittest.mock import Mock
    global _deprecated
    mock_deprecated = _deprecated

    seq = _DeprecatedSequenceConstant('a', 'b', 'c')
    assert seq[0] == 'a'
    seq = _DeprecatedSequenceConstant(BOOLEANS, 'b', 'c')
    assert seq[0] == True

    _deprecated = Mock()
    seq = _DeprecatedSequenceConstant('a', 'b', 'c')
    seq[0]

# Generated at 2022-06-22 11:27:06.997891
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant([0, 1], 'test', '2.0')
    assert len(dsc) == 2
    assert dsc[0] == 0


# Generated at 2022-06-22 11:28:05.983184
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    # test constructor
    t = (1, 2, 4)
    dsc = _DeprecatedSequenceConstant(t, "testing deprecated", "2.10")

    assert dsc._value == t
    assert dsc._msg == "testing deprecated"
    assert dsc._version == "2.10"

    # test __len__()
    assert len(dsc) == 3

    # test __getitem__()
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert dsc[2] == 4

DEFAULT_TREE_DIR = TREE_DIR
DEFAULT_LOAD_CALLBACK_PLUGINS = LOAD_CALLBACK_PLUGINS
DEFAULT_CALLBACK_WHITELIST = CALLBACK_WHITELIST
DEFAULT_STDOUT_CALLBACK = STD

# Generated at 2022-06-22 11:28:10.380906
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant('string', 'msg', 'version')
    assert seq[0] == 's'
    assert seq[2:4] == 'ri'
    assert seq[4] == 'n'


# Generated at 2022-06-22 11:28:18.277217
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    '''
    Verify _DeprecatedSequenceConstant.__getitem__ method sends a warning and returns a value
    '''
    import warnings
    message = 'testing __getitem__'

    with warnings.catch_warnings(record=True) as captured_warnings:
        warnings.simplefilter('always')
        result = _DeprecatedSequenceConstant([1, 2, 3], message, '2.6').__getitem__(1)
        assert captured_warnings and message in str(captured_warnings[0]), "No warning captured"
        assert result == 2, "Did not return expected value"

# Generated at 2022-06-22 11:28:27.055790
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert foo == 'bar'


# Deprecation constants

# Ansible 2.9
BECOME_METHODS_DEPRECATED = add_internal_fqcns(('su', ))
DELEGATE_TO_HOSTS_DEPRECATED = add_internal_fqcns(('ansible_ssh_host', 'ansible_host'))
DELEGATE_TO_USERS_DEPRECATED = add_internal_fqcns(('ansible_ssh_user', 'ansible_user'))
DELEGATE_TO_PASSWORDS_DEPRECATED = add_internal_fqcns(('ansible_ssh_pass', 'ansible_password'))
DELEGATE_TO_PORTS_DEPRECATED = add_internal_fq

# Generated at 2022-06-22 11:28:36.688709
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Case 1
    class_test = _DeprecatedSequenceConstant(value = ('A', 'B', 'C'), msg = "test_msg", version = 'test_version')
    assert len(class_test) == 3
    # Case 2
    class_test = _DeprecatedSequenceConstant(value = [1, 2, 3], msg = "test_msg", version = 'test_version')
    assert len(class_test) == 3
    # Case 3
    class_test = _DeprecatedSequenceConstant(value = {'A': 'B', 'C': 'D'}, msg = "test_msg", version = 'test_version')
    assert len(class_test) == 2


# Generated at 2022-06-22 11:28:39.272691
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.module_utils.common.collections import Sequence
    sequence = [1, 2, 3, 4]
    _DeprecatedSequenceConstant(sequence, 'some message', 'some version')

# Generated at 2022-06-22 11:28:45.502431
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    ''' Create a _DeprecatedSequenceConstant object and make sure it works '''
    value = [1, 2, 3]
    msg = 'This message is being tested'
    version = 'version 2.0'
    _D_S_C = _DeprecatedSequenceConstant(value=value, msg=msg, version=version)
    assert len(_D_S_C) == len(value)
    assert _D_S_C[1] == value[1]

# Generated at 2022-06-22 11:28:48.725248
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    list1 = [1,2,3,4]
    message = "Set this to false instead"
    deprecation_version = "2.11"
    test_obj = _DeprecatedSequenceConstant(list1,message,deprecation_version)
    assert test_obj[0] == list1[0]

# Generated at 2022-06-22 11:28:59.407453
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test initialization
    _DeprecatedSequenceConstant([], '', __version__)



# Generated at 2022-06-22 11:29:02.759218
# Unit test for function set_constant
def test_set_constant():
    # create a namespace to set constants in
    export = {}
    # set a constant in an alternate namespace
    set_constant('FOO', 'bar', export)
    assert export.get('FOO') == 'bar', 'failed to set constant in alternate namespace'
