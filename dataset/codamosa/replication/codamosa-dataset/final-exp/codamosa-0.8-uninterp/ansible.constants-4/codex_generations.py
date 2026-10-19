

# Generated at 2022-06-22 11:19:18.813691
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant([1, 2, 3, 4], "test", "1.0")
    assert seq[0] == 1
    assert seq[2:4] == [3, 4]
    assert seq[::-1] == [4, 3, 2, 1]
    assert seq[:1] == [1]
    assert seq[3] == 4

# Generated at 2022-06-22 11:19:28.750367
# Unit test for function set_constant
def test_set_constant():
    _test_x = {}
    _test_y = {}
    set_constant('test_value', 'foo', _test_x)
    assert _test_x['test_value'] == 'foo'
    assert 'test_value' not in _test_y
    # reset to prevent test pollution
    _test_x.pop('test_value', None)
    set_constant('test_value', 'foo', export=_test_x)
    assert _test_x['test_value'] == 'foo'
    assert 'test_value' not in _test_y
    # reset to prevent test pollution
    _test_x.pop('test_value', None)

# Generated at 2022-06-22 11:19:33.732561
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = [1, 2]
    msg = 'test'
    version = '2.0'
    ds = _DeprecatedSequenceConstant(value, msg, version)
    assert len(ds) == len(value)

# Generated at 2022-06-22 11:19:42.189831
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant((1, 2, 'a', 'b'), 'some message', 'v2.0') == (1, 2, 'a', 'b')
    assert _DeprecatedSequenceConstant({'a': 1, 'b': 2}, 'some other message', 'v2.1') is not None
    assert _DeprecatedSequenceConstant([1, 2, 3, 4], 'some other message', 'v2.2') == [1, 2, 3, 4]


# Generated at 2022-06-22 11:19:44.805787
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], "abc", "abc")) == 0


# Generated at 2022-06-22 11:19:52.880161
# Unit test for function set_constant
def test_set_constant():
    import sys
    d = {}
    set_constant('ALLOWED_HOSTS', ['localhost', '127.0.0.1'], d)
    assert d['ALLOWED_HOSTS'] == ['localhost', '127.0.0.1']
    assert sys.modules['ansible.constants'] is not None
    set_constant('ALLOWED_HOSTS', ['0.0.0.0'], d)
    assert d['ALLOWED_HOSTS'] == ['0.0.0.0']
    assert sys.modules['ansible.constants'] is not None

# Generated at 2022-06-22 11:19:57.001564
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    v = _DeprecatedSequenceConstant([1, 2], 'test_msg', '1.2')
    assert len(v) == 2


# Generated at 2022-06-22 11:19:59.633667
# Unit test for function set_constant
def test_set_constant():
    ret_val = dict()
    set_constant("test_k", "test_v", ret_val)
    assert ret_val['test_k'] == "test_v"

# Generated at 2022-06-22 11:20:02.926720
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = "value"
    msg = "msg"
    version = "version"
    obj = _DeprecatedSequenceConstant(value, msg, version)
    assert len(obj) == len(value)


# Generated at 2022-06-22 11:20:07.297924
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    dummy_value = []
    dummy_msg = 'msg'
    dummy_version = 'version'
    dsc = _DeprecatedSequenceConstant(dummy_value, dummy_msg, dummy_version)
    assert len(dsc) == len(dummy_value)



# Generated at 2022-06-22 11:20:22.645184
# Unit test for function set_constant
def test_set_constant():
    # Reset config data
    cm = ConfigManager()
    display = cm.data.get_setting_value('DEFAULT_STDOUT_CALLBACK')
    display.value = 'default'
    cm.process_config_data()
    assert cm.data.get_setting_value('DEFAULT_STDOUT_CALLBACK') == 'default'
    # Test change display setting
    set_constant('DEFAULT_STDOUT_CALLBACK', 'debug', export=vars())
    cm.process_config_data()
    assert cm.data.get_setting_value('DEFAULT_STDOUT_CALLBACK') == 'debug'


# constants for hosts
# TODO: consider moving to a different file
HOST_NAME = 'name'  # unique hostname
HOST_NAME_VARIABLE = 'inventory_hostname'  # unique host

# Generated at 2022-06-22 11:20:24.794511
# Unit test for function set_constant
def test_set_constant():
    assert getattr(DEFAULT_BECOME_PASS, '__module__') == 'ansible.config.constants'

# Generated at 2022-06-22 11:20:33.924931
# Unit test for function set_constant
def test_set_constant():
    ''' set_constant should create a unique constant for each value '''
    import sys
    import types

    mod = types.ModuleType('__main__')
    for k, v in sys.modules.items():
        if k != '__main__':
            mod.__dict__[k] = v

    set_constant('test_constant', 42, export=mod.__dict__)
    assert mod.test_constant == 42
    assert sys.modules['__main__'].test_constant == 42

    # Try a default constant
    set_constant('test_constant_default', '{{ test_constant }}', export=mod.__dict__)
    assert mod.test_constant_default == 42
    assert sys.modules['__main__'].test_constant_default == 42

    # Try a

# Generated at 2022-06-22 11:20:46.522782
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test 1
    # Test the case when the value is a list
    value = [1, 2, 3]
    msg = "this is a message"
    version = "1.0"
    c = _DeprecatedSequenceConstant(value, msg, version)
    assert c._value == value
    assert c._msg == msg
    assert c._version == version
    assert c[0] == 1
    assert c[1] == 2
    assert c[2] == 3
    assert len(c) == 3

    # Test 2
    # Test the case when the value is a tuple
    value = (1, 2, 3)
    c = _DeprecatedSequenceConstant(value, msg, version)
    assert c._value == value
    assert c._msg == msg
    assert c._version == version

# Generated at 2022-06-22 11:20:52.907394
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    item = _DeprecatedSequenceConstant([], None, None)
    assert item.__len__() == 0
    assert item.__getitem__(0) is None
    assert item.__getitem__(None) is None
    assert item.__getitem__('a') is None
    assert item.__getitem__((1, 2, 3)) is None

# Generated at 2022-06-22 11:21:06.527256
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # Test invalid
    val = _DeprecatedSequenceConstant(None, None, None)
    try:
        val.__getitem__(1)
    except Exception as e:
        assert e.__class__.__name__ == 'AssertionError'
        assert str(e) == '_value is not set to a value'

    # Test invalid
    try:
        val.__getitem__('key')
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
        assert str(e) == 'list indices must be integers, not str'

    # Test valid
    val._value = []
    assert val.__getitem__(0) == []
    val._value = None

# Generated at 2022-06-22 11:21:08.986647
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = ['value1', 'value2']
    test_msg = 'message'
    test_version = 'version'
    _DeprecatedSequenceConstant(test_value, test_msg, test_version)


# Generated at 2022-06-22 11:21:12.568333
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_INTERNAL_TEST', 'FOO')
    assert ANSIBLE_INTERNAL_TEST == 'FOO'



# Generated at 2022-06-22 11:21:21.808028
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    import unittest.mock
    a = _DeprecatedSequenceConstant(value=['a'], msg='test', version='1.1')
    assert len(a) == 1

    with unittest.mock.patch('ansible.utils.config.utils._deprecated') as mocked:
        # Deprecated warning message is not displayed
        len(a)
        assert not mocked.called

        # Deprecated warning message is displayed
        a.test__invalid_attribute__ = ''
        with unittest.mock.raises(AttributeError):
            len(a)
        assert mocked.called

# Generated at 2022-06-22 11:21:25.972253
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    try:
        dsc = _DeprecatedSequenceConstant(['a'], 'msg', 'version')
    except Exception as e:
        assert False, "{0}".format(e)


if __name__ == '__main__':
    import sys
    import unittest
    sys.argv.append('--verbose')
    unittest.main(failfast=True, buffer=True)

# Generated at 2022-06-22 11:21:37.402282
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    fake_version = '2.0'
    x = _DeprecatedSequenceConstant(["all_the_things"], "", fake_version)
    x.__getitem__(0)
    assert x[0] == "all_the_things"


# Generated at 2022-06-22 11:21:45.638804
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'msg'
    version = 'version'
    value = [1,2,3]

    dsc = _DeprecatedSequenceConstant(value, msg, version)

    assert dsc[0] == value[0]
    assert dsc[1] == value[1]
    assert dsc[2] == value[2]

    assert dsc[-1] == value[-1]
    assert dsc[-2] == value[-2]
    assert dsc[-3] == value[-3]


# Generated at 2022-06-22 11:21:48.806476
# Unit test for function set_constant
def test_set_constant():
    dict = {}
    set_constant('TEST', 'TEST_VALUE', dict)
    assert dict.get('TEST') == 'TEST_VALUE'

# Generated at 2022-06-22 11:21:57.164026
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg1 = 'test_msg_1'
    msg2 = 'test_msg_2'
    version1 = 'test_version_1'
    version2 = 'test_version_2'
    value = ['a', 'b', 'c']
    dsc = _DeprecatedSequenceConstant(value, msg1, version1)
    dsc._msg = msg2
    dsc._version = version2
    assert dsc._msg == msg2
    assert dsc._value == value
    assert dsc._version == version2
    for v in value:
        assert v in dsc
    assert len(dsc) == len(value)
    assert dsc[0] == value[0] and dsc[1] == value[1] and dsc[2] == value[2]

# Generated at 2022-06-22 11:22:00.867583
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq_constant = _DeprecatedSequenceConstant([1, 2, 3], 'this is a test', '2.9')
    assert [1, 2, 3] == seq_constant
    assert 3 == len(seq_constant)
    assert 2 == seq_constant[1]

# Generated at 2022-06-22 11:22:05.068654
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant(tuple(['a', 'b', 'c']), 'test', '2.7')
    return dsc.__getitem__(1) == 'b'


# Generated at 2022-06-22 11:22:08.478891
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.module_utils.common.collections import _DeprecatedSequenceConstant
    assert len(_DeprecatedSequenceConstant(['A'], 'foo', '1.0')) == 1


# Generated at 2022-06-22 11:22:14.346088
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(['a', 'b'], 'test', '2.0')
    assert c[0] == 'a'
    assert c[1] == 'b'
    assert len(c) == 2
    assert c.__str__() == '[\'a\', \'b\']'
    assert c.__repr__() == '_DeprecatedSequenceConstant([\'a\', \'b\'], test, 2.0)'

# Generated at 2022-06-22 11:22:20.534755
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # INPUT
    msg = u"This is a test warning message"
    version = 2.3

    # EXPECTED OUTPUT
    expected_msg = u"This is a test warning message, to be removed in 2.3"

    # OUTPUT
    dep = _DeprecatedSequenceConstant([1, 2, 3], msg, version)
    _deprecated(msg, version)

    # TEST
    assert expected_msg in dep

# Generated at 2022-06-22 11:22:23.988229
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    v = _DeprecatedSequenceConstant(range(1, 5), 'test msg', 'test version')
    assert v[2] == 3

# Generated at 2022-06-22 11:22:40.223571
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.module_utils.common.collections import list_of_lists
    assert len(_DeprecatedSequenceConstant(list_of_lists(), 'msg', 'v')) == len(list_of_lists())



# Generated at 2022-06-22 11:22:44.758768
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence_constant = _DeprecatedSequenceConstant([1, 2, 3], "test_msg", "2.9")
    assert sequence_constant[0] == 1
    assert sequence_constant[1] == 2
    assert sequence_constant[2] == 3



# Generated at 2022-06-22 11:22:55.158222
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test case 1: len of value is 0
    value = ()
    msg = "test message 1"
    version = "1.0"
    a = _DeprecatedSequenceConstant(value, msg, version)
    assert len(a) == 0

    # Test case 2: len of value is 1
    value = ('test',)
    msg = "test message 2"
    version = "1.0"
    a = _DeprecatedSequenceConstant(value, msg, version)
    assert len(a) == 1

    # Test case 3: len of value is not 0
    value = ('test', 'test1')
    msg = "test message 3"
    version = "1.0"
    a = _DeprecatedSequenceConstant(value, msg, version)
    assert len(a) == 2

# Unit

# Generated at 2022-06-22 11:23:00.047373
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'This is message'
    value = ('value1', 'value2')
    dsc = _DeprecatedSequenceConstant(value, msg, 'version')

    assert len(dsc) == len(value)
    assert dsc[0] == value[0]



# Generated at 2022-06-22 11:23:04.818336
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    # test constructor of class _DeprecatedSequenceConstant
    assert _DeprecatedSequenceConstant(('a', 'b'), 'foo', 'bar')


# run these if this is the 'main' file
if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:23:09.621179
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    msg = 'test msg'
    version = 'test version'
    value = AnsibleCollectionLoader()
    _DeprecatedSequenceConstant(value, msg, version)
    _DeprecatedSequenceConstant(None, None, None)


# Generated at 2022-06-22 11:23:17.873608
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant((), 'msg', '1.2'), Sequence)
    assert isinstance(_DeprecatedSequenceConstant([], 'msg', '1.2'), Sequence)
    # Test __len__
    assert len(_DeprecatedSequenceConstant((), 'msg', '1.2')) == 0
    assert len(_DeprecatedSequenceConstant([], 'msg', '1.2')) == 0
    # Test __getitem__
    assert _DeprecatedSequenceConstant((), 'msg', '1.2')[0] is None
    assert _DeprecatedSequenceConstant([], 'msg', '1.2')[0] is None


# Generated at 2022-06-22 11:23:28.963789
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant([], "test", "2.7")
    assert constant._version == "2.7"
    assert constant._msg == "test"
    assert constant._value == []
    assert constant[:] == []
    assert len(constant) == 0


# NEXT STEP: setup constants available to modules, plugins and jinja2
# which were set by config settings above.

# Options which were previously boolean values, but now have sub-options
# which also have True/False values.
BOOLEAN_PREVIOUSLY_SINGLETON = ('accelerate', 'diff')

# Options which can be specified as a boolean value or as a string with
# values "yes", "on", "1", "true" or "no", "off", "0", "false"
BOOL_OR_STR

# Generated at 2022-06-22 11:23:31.722259
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant((1, 2, 3), 'msg', '2.0')
    assert constant[1] == 2


# Generated at 2022-06-22 11:23:35.128421
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant(value=[1, 2, 3, 4], msg='this stuff is deprecated', version='2.0')
    assert len(dsc) == 4


# Generated at 2022-06-22 11:24:37.415084
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = ['a', 'b', 'c']
    msg = 'test'
    version = '2.0'
    seq = _DeprecatedSequenceConstant(value, msg, version)
    assert seq[2] == 'c'


# Generated at 2022-06-22 11:24:40.478192
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant([1, 2], 'Warning', '1.0')
    assert len(seq) == 2
    assert seq[0] == 1
    assert seq[1] == 2

# Generated at 2022-06-22 11:24:44.669721
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    input = [1, 2, 3]
    dsc = _DeprecatedSequenceConstant(value=input, msg='msg', version='version')
    assert len(dsc) == 3
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert dsc[2] == 3

# Generated at 2022-06-22 11:24:48.341908
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_CONFIG == 'dummy_config'
    assert ANSIBLE_HOST_KEY_CHECKING == True
    assert ANSIBLE_RETRY_FILES_ENABLED == False
    assert ANSIBLE_KEEP_REMOTE_FILES == True
    assert ANSIBLE_FORKS == 3

# Generated at 2022-06-22 11:24:50.151478
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant(['foo'], "msg", '2.9')
    assert 1 == len(seq)



# Generated at 2022-06-22 11:24:59.898860
# Unit test for function set_constant
def test_set_constant():
    # generate a dict of vars to use in the tests
    vardict = {'foo':'bar'}

    # set a var
    set_constant('foo','baz',export=vardict)
    assert vardict['foo'] == 'baz'

    # set a var that should have been overwritten
    set_constant('baz','foo',export=vardict)
    assert vardict['baz'] == 'foo'

    # set a constant to override an already existing var
    set_constant('baz','bar',export=vardict)
    assert vardict['baz'] == 'bar'

    # set an int
    set_constant('baz',1,export=vardict)
    assert vardict['baz'] == 1

    # set an underscore_var
    set_constant

# Generated at 2022-06-22 11:25:03.803958
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dep_seq_constant_test = _DeprecatedSequenceConstant([1, 2, 3], "This is a test message", "2.10")
    assert len(dep_seq_constant_test) == 3
    assert dep_seq_constant_test[0] is 1
    assert dep_seq_constant_test[1] is 2
    assert dep_seq_constant_test[2] is 3

# Generated at 2022-06-22 11:25:08.825937
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'bar')
    assert FOO == 'bar'
    set_constant('FOO', 'bar2')
    assert FOO == 'bar2'

    global BAR
    set_constant('BAR', 'bar')
    assert BAR == 'bar'
    set_constant('BAR', 'bar2')
    assert BAR == 'bar2'

# Generated at 2022-06-22 11:25:15.756687
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    TEST_VALUE = ['test1', 'test2']
    TEST_MSG = 'test message'
    TEST_VERSION = 'test version'

    test_obj = _DeprecatedSequenceConstant(value=TEST_VALUE, msg=TEST_MSG, version=TEST_VERSION)
    assert len(test_obj) == 2
    assert test_obj[0] == 'test1'
    assert test_obj[1] == 'test2'



# Generated at 2022-06-22 11:25:18.825563
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def test(value, msg, version):
        dsc = _DeprecatedSequenceConstant(value, msg, version)
        assert dsc[0] == value[0]

    test([42, 123], 'msg', 'version')


# Generated at 2022-06-22 11:27:02.404592
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_obj = _DeprecatedSequenceConstant(value='ansible', msg='Testing', version='v2.8')
    assert test_obj[3] == 'i'


# Generated at 2022-06-22 11:27:08.093097
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import tests.unit

    # create test object
    x = _DeprecatedSequenceConstant(value=[1, 2, 3], msg='testing', version='2.5')
    assert x[1] == 2

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    test__DeprecatedSequenceConstant___getitem__()

# Generated at 2022-06-22 11:27:11.507823
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant([1, 2], "warning message", "2.0")
    assert constant[0] == 1
    assert constant[1] == 2



# Generated at 2022-06-22 11:27:13.029206
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant((), 'msg', 'version')
    len(c)



# Generated at 2022-06-22 11:27:14.892036
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    CONST = _DeprecatedSequenceConstant(value=(1, 2, 3), msg='test msg', version='2.0')
    assert CONST[1] == 2


# Generated at 2022-06-22 11:27:17.021731
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(('b', 'c'), 'msg', 'version')[1] == 'c'

# Generated at 2022-06-22 11:27:26.023510
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    new_const_value = _DeprecatedSequenceConstant(value=("item1", "item2"),
                                                  msg="Please use new_const_value instead of old_const_value.",
                                                  version="2.8")
    assert "Please use new_const_value instead of old_const_value." in _DEPRECATED_MSG
    assert "2.8" in _DEPRECATED_MSG
    assert new_const_value[0] == "item1"
    assert new_const_value[1] == "item2"
    assert len(new_const_value) == 2

# UNIT TESTS FOR THIS FILE ARE IN test/unit/constants_loader_test.py

# Generated at 2022-06-22 11:27:32.306534
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'msg'
    version = 'version'
    DEVNULL = open('/dev/null', 'w')
    import sys
    try:
        sys.stderr = DEVNULL
        c = _DeprecatedSequenceConstant(value=[1, 2, 3, 4], msg=msg, version=version)
        assert c[1] == 2
        assert c[3] == 4
        assert c[-1] == 4
    finally:
        sys.stderr = sys.__stderr__
        DEVNULL.close()

# Generated at 2022-06-22 11:27:37.611775
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ['dummy']
    msg = 'This is a dummy message'
    version = '2.3'
    test_obj1 = _DeprecatedSequenceConstant(value, msg, version)
    len_obj1 = len(test_obj1)
    assert(len_obj1 == 1)


# Generated at 2022-06-22 11:27:41.327592
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    deprecated_message = 'use list instead of tuple'
    old = _DeprecatedSequenceConstant(('x',), deprecated_message, '2.11')
    assert old[0] == 'x'
    assert old == ('x',)
    assert old[-1] == 'x'
    assert old[-1] == 'x'