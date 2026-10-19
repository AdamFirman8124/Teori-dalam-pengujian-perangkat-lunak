

# Generated at 2022-06-22 11:19:29.339892
# Unit test for function set_constant
def test_set_constant():
    # This is a way to do a unit test for the set_constant function.
    # The only reason it is here is because we don't know of any other way
    # to import ansible.constants without it running through the whole
    # "ensure we got all the settings" shtick.
    #
    # For the record, this is a bad idea and should be rewritten elsewhere.

    # TODO: use unittest.mock.patch and import from that instead?
    from collections import namedtuple
    from copy import deepcopy
    from ansible import constants
    from ansible.config.manager import ConfigManager

    TEST_CONSTANT = 'TEST_CONSTANT'
    TEST_VALUE = 'test value'
    orig_vars = deepcopy(vars())
    orig_globals = deepcopy(globals())

# Generated at 2022-06-22 11:19:34.348664
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.module_utils.common.collections import Sequence

    class Subclass(_DeprecatedSequenceConstant):
        def __init__(self, value, msg, version):
            super().__init__(value, msg, version)

    def test():
        sub = Subclass([0, 1, 2], 'msg', 'version')
        assert sub[1] == 1
    test()


# Generated at 2022-06-22 11:19:43.505514
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('test', 'teststring', export)
    assert export['test'] == 'teststring'
    set_constant('test', ['test', 'test'], export)
    assert export['test'] == ('test', 'test')
    set_constant('test', ('test', 'test'), export)
    assert export['test'] == ('test', 'test')
    set_constant('test', None, export)
    assert export['test'] is None


# Generated at 2022-06-22 11:19:48.476160
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "Warning message"
    test = _DeprecatedSequenceConstant(value = [1,2,3,4], msg = msg, version = "2.9")
    ret = len(test)
    assert ret == 4
    ret = test[2]
    assert ret == 3

# Generated at 2022-06-22 11:20:00.761263
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    for key, values in {'test1': (1, 5), 'test2': (5, 6)}.items():
        x = _DeprecatedSequenceConstant(values, 'test1', 'test2')
        assert len(x) == 2, 'len({}) should be 2 but is {}'.format(x, len(x))
        assert x[0] == 1, 'x[0] should be 1 but is {}'.format(x[0])


# Generated at 2022-06-22 11:20:05.671259
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    from ansible.units.machinery import _DeprecatedSequenceConstant
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    _DeprecatedSequenceConstant(BOOLEANS_TRUE, 'test message', '2.10')

# Generated at 2022-06-22 11:20:08.818178
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 'foo')
    assert TEST_CONSTANT == 'foo'


# Generated at 2022-06-22 11:20:18.913436
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    for k in ('connection', 'become'):
        assert MAGIC_VARIABLE_MAPPING[k] == _DeprecatedSequenceConstant(MAGIC_VARIABLE_MAPPING[k],
                                                                         'MAGIC_VARIABLE_MAPPING[%s] has been deprecated since Ansible 2.4. Use MAGIC_VARIABLE_MAPPING[%s] instead' % (k, k),
                                                                         '2.5')._value[0]

# Generated at 2022-06-22 11:20:29.734756
# Unit test for function set_constant
def test_set_constant():
    """ Function to test set_constant """
    config_constant = None
    default_constant = None
    set_constant('config_constant', 'CONFIG', {'default_constant': default_constant})
    assert vars()['config_constant'] == 'CONFIG'
    set_constant('default_constant', 'DEFAULT', {'config_constant': config_constant})
    assert vars()['default_constant'] == 'DEFAULT'
    # Check that vars() was not updated, which would break the config system
    assert 'config_constant' not in vars()
    assert 'default_constant' not in vars()

test_set_constant()

# Generated at 2022-06-22 11:20:32.235589
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    x = [1, 2, 3]
    y = _DeprecatedSequenceConstant(x, 'test warning', '2.9')
    assert y[1] == x[1]


# Generated at 2022-06-22 11:20:36.856552
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(list(range(5)), "msg", "version")) == 5


# Generated at 2022-06-22 11:20:46.390451
# Unit test for function set_constant
def test_set_constant():
    # test string
    assert ANSIBLE_NOCOWS == '1'
    # test unicode string
    assert ANSIBLE_CONFIG == to_text('/etc/ansible/ansible.cfg')
    # test integer
    assert DEFAULT_SUDO_PASS == 1234567890
    # test float
    assert DEFAULT_TIMEOUT == 60.0
    # test list
    assert ADDITIONAL_DEFAULT_JSON_FILTERS == [u'foo', u'bar', u'baz']
    # test bool
    assert ANSIBLE_DEBUG == True


# Generated at 2022-06-22 11:20:57.399023
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Create a sequence object
    test_sequence = _DeprecatedSequenceConstant((1, 2, 3), 'Test is DEPRECATED', 'v2.10')

    # Check for length
    assert len(test_sequence) == 3

    # Check for availability of an item
    assert test_sequence[0] == 1
    assert test_sequence[1] == 2
    assert test_sequence[2] == 3

    # Check if an item is not present
    try:
        test_sequence[3]
    except IndexError:
        pass
    else:
        assert False

    # Create an empty sequence
    empty_sequence = _DeprecatedSequenceConstant((), 'Empty sequence is DEPRECATED', 'v2.10')

    # Check for length
    assert len(empty_sequence) == 0

    # Check for an item

# Generated at 2022-06-22 11:21:00.533836
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    lst = _DeprecatedSequenceConstant(['foo', 'bar'], 'msg', '1.0')
    assert len(lst) == 2

# Generated at 2022-06-22 11:21:04.029600
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test empty string
    msg = "test"
    version = "2.0"
    value = ''
    assert len(_DeprecatedSequenceConstant(value, msg, version)) == len(value)

# Generated at 2022-06-22 11:21:06.936888
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    actual = _DeprecatedSequenceConstant(value=(), msg="", version="")
    assert 0 == len(actual)



# Generated at 2022-06-22 11:21:11.840634
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_constant = _DeprecatedSequenceConstant(value='value', msg='message', version='version')
    assert len(test_constant) == 7
    assert test_constant[0] == 'v'

# Generated at 2022-06-22 11:21:14.388722
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([1, 2, 3], 'message', 'version')[2] == 3


# Generated at 2022-06-22 11:21:16.612909
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant('hello', 'test warn', 'version')
    assert len(seq) == 5


# Generated at 2022-06-22 11:21:21.626912
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    s = _DeprecatedSequenceConstant(['a', 'b'], 'Testing', __version__)
    assert len(s) == 2
    assert s[0] == 'a'
    assert s[1] == 'b'
    assert isinstance(s, Sequence)

# Generated at 2022-06-22 11:21:31.177362
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class TestClass(object):
        def __init__(self):
            self.dict_var = {'key_var' : 'val_var'}

        def get_indexes(self, dep_var):
            return dep_var['key_var']

    dep_seq_const = _DeprecatedSequenceConstant(TestClass(), 'test message', '6.0')
    assert dep_seq_const.get_indexes(dep_seq_const) == 'val_var'

# Generated at 2022-06-22 11:21:38.135732
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test1: Test value and message of deprecation warnings
    sequence = _DeprecatedSequenceConstant([], 'old', '0.0')
    assert sequence[0] is None
    sequence = _DeprecatedSequenceConstant([2], 'old', '0.0')
    assert sequence[0] == 2
    sequence = _DeprecatedSequenceConstant([2], 'old', '0.0')
    assert sequence[1] is None



# Generated at 2022-06-22 11:21:49.548677
# Unit test for function set_constant
def test_set_constant():
    test_dict = {}

    # Test with non-default dict
    set_constant('foo', 'bar', export=test_dict)
    set_constant('baz', 'qux', export=test_dict)
    assert test_dict == {'foo': 'bar', 'baz': 'qux'}
    assert test_dict is not vars()

    # Test default dict
    set_constant('foo', 'bar')
    set_constant('baz', 'qux')
    assert vars() == {'foo': 'bar', 'baz': 'qux'}

# NOTE: this set is used to enforce deprecation of module_utils not plugins

# Generated at 2022-06-22 11:21:52.409265
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test = _DeprecatedSequenceConstant((0, 1,), 'Testing __len__(): ', '3.0')
    assert len(test) == 3


# Generated at 2022-06-22 11:21:55.088332
# Unit test for function set_constant
def test_set_constant():
    set_constant(1, None, 1)
    set_constant(1, None, {'one': 1})
    set_constant('a', 'b')

# Generated at 2022-06-22 11:22:00.095033
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ('set_fact', 'include_tasks', 'meta')
    dep_msg = 'The include field should be a list of roles or tasks, the set_fact module is deprecated'
    dep_version = '2.17'
    dep_constant = _DeprecatedSequenceConstant(value, dep_msg, dep_version)
    assert len(dep_constant) == 3

# Generated at 2022-06-22 11:22:07.170140
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_value = ['a', 'b', 'c']
    test_msg = 'test_msg'
    test_version = 'test_version'

    test_obj = _DeprecatedSequenceConstant(test_value, test_msg, test_version)

    assert test_value[0] == test_obj[0]
    assert test_value[1] == test_obj[1]
    assert test_value[2] == test_obj[2]

# Generated at 2022-06-22 11:22:13.746672
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def check_value(value):
        return (value in ('DEBUG', 'INFO'))

    def check(value, expected_value):
        constant = _DeprecatedSequenceConstant(value, 'msg', '2.8')
        val = constant[0]
        assert expected_value == val
        assert check_value(val)

    check(['DEBUG', 'INFO'], 'DEBUG')
    check(_ACTION_ALL_INCLUDE_ROLE_TASKS, 'include_role')


# Generated at 2022-06-22 11:22:21.976973
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_TEST_CONSTANT_1', True, locals())
    local_test_value = locals()['ANSIBLE_TEST_CONSTANT_1']
    del locals()['ANSIBLE_TEST_CONSTANT_1']
    set_constant('ANSIBLE_TEST_CONSTANT_2', True)
    global_test_value = globals()['ANSIBLE_TEST_CONSTANT_2']
    del globals()['ANSIBLE_TEST_CONSTANT_2']
    assert local_test_value
    assert global_test_value



# Generated at 2022-06-22 11:22:24.942321
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant([1,2,3], "test", "2.0")
    assert len(a) == 3

# Generated at 2022-06-22 11:22:31.585831
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant([], '', '')
    assert len(seq) == 0
    seq = _DeprecatedSequenceConstant(['a', 'b'], '', '')
    assert len(seq) == 2

# Generated at 2022-06-22 11:22:35.012199
# Unit test for function set_constant
def test_set_constant():
    set_constant('name', 'value')
    assert 'name' in globals()
    assert globals()['name'] == 'value'
    del globals()['name']
    assert 'name' not in globals()


# Generated at 2022-06-22 11:22:46.285568
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def check_deprecated(obj, index, expected_value, expected_msg, expected_version):
        _msg, _version = '', ''
        obj.__getitem__(index)
        if _msg != expected_msg or _version != expected_version:
            raise Exception('Actual: %s, %s. Expected: %s, %s' % (_msg, _version, expected_msg, expected_version))
        obj[index]
        if _msg != expected_msg or _version != expected_version:
            raise Exception('Actual: %s, %s. Expected: %s, %s' % (_msg, _version, expected_msg, expected_version))

    check_deprecated(_DeprecatedSequenceConstant((1, 2, 3), 'msg', 'ver'), 1, 2, 'msg', 'ver')
   

# Generated at 2022-06-22 11:22:50.246221
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    s = _DeprecatedSequenceConstant(('a', 'b'), "msg", "version")
    assert isinstance(s, _DeprecatedSequenceConstant)
    assert len(s) == 2


# Generated at 2022-06-22 11:23:03.072421
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    import warnings
    import unittest.mock
    import textwrap

    msg = "some text"
    version = "some version"
    value = ["some value"]

    with unittest.mock.patch.object(sys, 'stderr', new_callable=unittest.mock.Mock) as mock_stderr:
        with warnings.catch_warnings(record=True) as w:
            obj = _DeprecatedSequenceConstant(value, msg, version)
            obj_value = obj[0]
            assert obj_value == value[0]

        mock_stderr.write.assert_called_with(textwrap.dedent(''' 
            [DEPRECATED] {}, to be removed in {}
        '''.format(msg, version)))
        assert issubclass

# Generated at 2022-06-22 11:23:14.500011
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_HOST_LIST == [u'all']
    assert DEFAULT_REMOTE_TMP == u'$HOME/.ansible/tmp'
    assert DEFAULT_SUDO_PASS == u''
    assert DEFAULT_SUDO_USER == u'root'
    assert DEFAULT_SYSLOG_FACILITY == u'LOG_USER'
    assert DEFAULT_TIMEOUT == 10
    assert DYNAMIC_INVENTORY_SOURCES == u''
    assert HOST_KEY_CHECKING == True
    assert HOST_KEY_CHECKING_DEFAULT == True
    assert INVENTORY_IGNORE_EXTS == [u'.tmp', u'.swp']

# Generated at 2022-06-22 11:23:20.437667
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    warnings_list = []
    def warning(msg):
        warnings_list.append(msg)

    seq = _DeprecatedSequenceConstant([1, 2, 3], "Abc", "1.0")
    assert len(seq) == 3
    assert len(warnings_list) == 1
    assert warnings_list[0] == ' [DEPRECATED] Abc, to be removed in 1.0'



# Generated at 2022-06-22 11:23:25.062330
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class_instance = _DeprecatedSequenceConstant(tuple('ABC'), 'msg', 'version')
    assert class_instance[0] == 'A'
    assert class_instance[1] == 'B'
    assert class_instance[2] == 'C'
    assert len(class_instance) == 3

# Generated at 2022-06-22 11:23:29.226618
# Unit test for function set_constant
def test_set_constant():
    test_dict = {}
    set_constant("test", "value", test_dict)
    assert test_dict == {"test": "value"}
    set_constant("test_1", 1, test_dict)
    assert test_dict == {"test": "value", "test_1": 1}

# Generated at 2022-06-22 11:23:37.520351
# Unit test for function set_constant
def test_set_constant():
    # Test without specifying the 'export' parameter
    set_constant('TEST_CONSTANT', 'foo')
    assert TEST_CONSTANT == 'foo'
    # Test with an empty dict passed for the 'export' parameter
    set_constant('TEST_CONSTANT', 'bar', export={})
    assert TEST_CONSTANT == 'foo'
    from ansible.module_utils import basic
    # Test with a dict passed for the 'export' parameter
    set_constant('TEST_CONSTANT', 'bar', export=basic.__dict__)
    assert TEST_CONSTANT == 'bar'

# Generated at 2022-06-22 11:23:45.970118
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'Removed after Ansible 2.1'
    version = '2.2'
    test_var = _DeprecatedSequenceConstant(ADD_GROUP_VARS, msg, version)
    assert 'add_group' in test_var
    assert isinstance(test_var, _DeprecatedSequenceConstant)
    assert len(test_var) == len(ADD_GROUP_VARS)

# Generated at 2022-06-22 11:23:52.578101
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_msg = 'dummy test message'
    test_version = '1.0'
    test_value = [1, 2]
    test_obj = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert test_obj._msg == test_msg
    assert test_obj._version == test_version
    assert test_obj._value == test_value
    assert len(test_obj) == 2
    assert test_obj[1] == 2


# Generated at 2022-06-22 11:23:56.163524
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_sequence = _DeprecatedSequenceConstant([1, 2, 3], 'Test message', '2.0')
    assert test_sequence[0] == 1
    assert test_sequence[1] == 2
    assert test_sequence[2] == 3


# Generated at 2022-06-22 11:23:59.417417
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant([1, 2, 3], 'msg', '2.0')
    assert len(a) == 3
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 3



# Generated at 2022-06-22 11:24:00.958969
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar', locals())
    assert foo == 'bar'



# Generated at 2022-06-22 11:24:03.600923
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    p = _DeprecatedSequenceConstant(['test'], 'Foo', '2.3')
    assert p[0] == 'test'
    assert len(p) == 1

# Generated at 2022-06-22 11:24:08.374343
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "THIS IS A TEST MESSAGE"
    version = "1.2.3"
    actual = _DeprecatedSequenceConstant(list(range(3)), msg, version)
    expected = len(list(range(3)))
    assert actual == expected


# Generated at 2022-06-22 11:24:12.095711
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    var = _DeprecatedSequenceConstant(value=['a', 'b', 'c'], msg="deprecated", version="0.0.1")
    assert len(var) == 3


# Generated at 2022-06-22 11:24:16.932694
# Unit test for function set_constant
def test_set_constant():
    ns = {}
    set_constant('FOO', 'bar', export=ns)
    set_constant('NESTED', {'foo': 'bar'}, export=ns)
    assert ns['FOO'] == 'bar'
    assert ns['NESTED'] == {'foo': 'bar'}

# Generated at 2022-06-22 11:24:19.061491
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant(['a'], 'msg', '1.0')
    assert len(seq) == 1


# Generated at 2022-06-22 11:24:27.502962
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = "msg"
    version = "version"
    test = _DeprecatedSequenceConstant(["1", "2", "3"], msg, version)

    assert len(test) == 3


# Generated at 2022-06-22 11:24:30.164731
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant((), 'msg', 'version')
    assert len(dsc) == 0



# Generated at 2022-06-22 11:24:34.000350
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_value = [1, 2, 3]
    d = _DeprecatedSequenceConstant(test_value, msg='test', version='2.9')

    assert d.__getitem__(0) == test_value[0]



# Generated at 2022-06-22 11:24:44.049803
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test with a list of integers
    seq = _DeprecatedSequenceConstant([1, 2, 3], 'foo', 'bar')
    assert len(seq) == 3
    # Test with a list of strings
    seq = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'foo', 'bar')
    assert len(seq) == 3
    # Test with an empty list
    seq = _DeprecatedSequenceConstant([], 'foo', 'bar')
    assert len(seq) == 0
    # Test with a list of strings with None
    seq = _DeprecatedSequenceConstant(['a', None, 'c'], 'foo', 'bar')
    assert len(seq) == 3



# Generated at 2022-06-22 11:24:47.472864
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant(('a', 'b'), 'message', '2.10')
    len(constant)
    assert len(constant) == 2


# Generated at 2022-06-22 11:24:49.973003
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    s = _DeprecatedSequenceConstant([1, 2, 3, 4], 'test_msg', '2.2')
    assert s[1] == 2

# Generated at 2022-06-22 11:24:54.263823
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = ['a', 'b', 'c']
    y = _DeprecatedSequenceConstant(x, 'test msg', '2.8')


if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:25:01.989195
# Unit test for function set_constant
def test_set_constant():
    assert(set_constant('color_codes', 'black', vars()) == COLOR_CODES)
    assert(set_constant('color_codes', 'black', vars()) == COLOR_CODES)
    assert(set_constant('color_codes', 'COLOR_CODES', vars()) == COLOR_CODES)
    assert(set_constant('color_codes', 'reject_exts', vars()) == REJECT_EXTS)
    assert(set_constant('color_codes', 'reject_exts', vars()) == REJECT_EXTS)
    assert(set_constant('color_codes', 'REJECT_EXTS', vars()) == REJECT_EXTS)

# Generated at 2022-06-22 11:25:12.187108
# Unit test for function set_constant
def test_set_constant():
    import sys

    def my_print(message):
        sys.stderr.write(' [WARNING] %s\n' % (message))

    _warning = my_print
    test_config = ConfigManager()
    set_constant('config_test', test_config.data.get_settings()[0].value)
    set_constant('config_test2', test_config.data.get_settings()[1].value)
    assert config_test == test_config.data.get_settings()[0].value
    assert config_test2 == test_config.data.get_settings()[1].value


# FIXME: remove once we're sure we don't need it
# NOTE: this should never be documented

# Generated at 2022-06-22 11:25:22.763158
# Unit test for function set_constant
def test_set_constant():
    # In order for the config imports to take effect, this needs to be run
    # before all the constants are defined.

    from ansible.module_utils.six import PY3
    from ansible.constants import DEFAULT_LOG_PATH, DEFAULT_KEEP_REMOTE_FILES

    # Basic test
    set_constant('TEST1', 1)
    assert TEST1 == 1

    # Can't override constants
    try:
        set_constant('DEFAULT_LOG_PATH', "/dev/null")
        assert False
    except AssertionError:
        pass

    # Templating test
    set_constant('TEST2', '{{ TEST1 }}')
    assert TEST2 == 1

    # Escape test
    set_constant('TEST3', '{{ TEST2 }}\\')

# Generated at 2022-06-22 11:25:51.553078
# Unit test for function set_constant
def test_set_constant():
    set_constant('MY_NEW_CONSTANT', True)
    assert MY_NEW_CONSTANT is True

# Generated at 2022-06-22 11:25:56.830454
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Setup
    constant_name = 'test'
    constant_value = [1, 2]
    constant_msg = 'test message'
    constant_version = '1.2.3'

    # Execute
    result = _DeprecatedSequenceConstant(constant_value, constant_msg, constant_version)[0]

    # Assert
    assert result == constant_value[0]



# Generated at 2022-06-22 11:26:01.813163
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_values = (
        (['hello'], 'test_message', '2.0', 1),
        (['hello', 'world'], 'test_message', '2.0', 2),
    )

    for value, msg, version, expected in test_values:
        dsc = _DeprecatedSequenceConstant(value, msg, version)
        assert expected == len(dsc)


# Generated at 2022-06-22 11:26:04.653154
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant(value=['a', 'b', 'c'], msg='test', version='1.0')
    assert len(dsc) == 3


# Generated at 2022-06-22 11:26:11.541931
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    import mock
    import types
    x = _DeprecatedSequenceConstant([1, 2, 3], "This is a test", "1.2.3")
    # Check if __getitem__ returns the expected item
    assert x[0] == 1
    # Check if __deprecated is called with the correct arguments
    with mock.patch('ansible.module_utils.basic.deprecated', return_value=None) as mocked_deprecated:
        x[1]
        assert mocked_deprecated.called
        assert mocked_deprecated.call_args[0] == ("This is a test", "1.2.3")


# Generated at 2022-06-22 11:26:15.480683
# Unit test for function set_constant
def test_set_constant():
    import sys
    if 'ansible.config.constants.set_constant' not in sys.modules:
        raise ImportError('Set constant was not set')


if __name__ == '__main__':
    test_set_constant()

# Generated at 2022-06-22 11:26:25.202846
# Unit test for function set_constant
def test_set_constant():

    # make sure there are no collisions with builtins
    try:
        set_constant('True', 'foo')
    except Exception as e:
        assert "is already defined" in str(e)

    # make sure there are no collisions with stdlib
    try:
        set_constant('pwd', 'foo')
    except Exception as e:
        assert "is already defined" in str(e)

    # making sure we can actually set a constant
    try:
        set_constant('foo', 'bar')
        foo = 'bar'
    except Exception as e:
        assert "is already defined" not in str(e)

    # make sure it is not a keyword
    try:
        set_constant('with', 'bar')
    except Exception as e:
        assert "is a python keyword" in str(e)


# Generated at 2022-06-22 11:26:27.699559
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant([1, 2, 3], 'msg', '1.0')
    assert len(c) == 3


# Generated at 2022-06-22 11:26:39.006828
# Unit test for function set_constant
def test_set_constant():
    # This is a unit test for set_constant function
    # It is not called by default.
    # Run this test explicitly if any changes to
    # set_constant function is made.
    import os
    import sys

    debug = False

    prefx = "DEFAULT_"
    export = {}
    set_constant("DEFAULT_FORKS", "20", export)
    set_constant("DEFAULT_REMOTE_USER", "root", export)
    set_constant("DEFAULT_SUDO_EXE", "/usr/bin/sudo", export)
    set_constant("DEFAULT_SUDO_USER", "", export)
    set_constant("DEFAULT_SUDO", False, export)
    set_constant("DEFAULT_SUDO_PASS", False, export)
    set_

# Generated at 2022-06-22 11:26:40.323195
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_set_constant', 'foo')
    assert test_set_constant == 'foo'

# Generated at 2022-06-22 11:27:39.121503
# Unit test for function set_constant
def test_set_constant():
    bogus = {'foo':'bar'}
    set_constant('test_constant', 'foo', export=bogus)
    assert bogus['test_constant'] == 'foo'


# Generated at 2022-06-22 11:27:42.387183
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'a'
    version = '1.0'
    constant = _DeprecatedSequenceConstant(['a'], msg, version)
    assert constant[0] == 'a'



# Generated at 2022-06-22 11:27:53.126620
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from io import StringIO
    import sys
    from ansible.module_utils._text import to_text

    stdout_buf = StringIO()

    #original_stdout = sys.stdout
    sys.stdout = stdout_buf

    # Creates a _DeprecatedSequenceConstant object
    constant = _DeprecatedSequenceConstant([1, 2], "msg", "2.0")
    # Calls the __getitem__ method
    constant[0]

    sys.stdout = sys.__stdout__
    stdout_buf.flush()
    stdout_buf.seek(0)
    # Tests the output of the __getitem__ method
    assert to_text(stdout_buf.read()) == u' [DEPRECATED] msg, to be removed in 2.0\n'

# Generated at 2022-06-22 11:27:56.725168
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant(value=[1, 2], msg="msg", version="ver")
    assert len(constant) == 2
    assert constant[0] == 1
    assert constant[1] == 2



# Generated at 2022-06-22 11:28:01.159035
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    CONSTANT = _DeprecatedSequenceConstant(value=('a', 1), msg="msg", version='2.0')
    assert len(CONSTANT) == 2
    assert CONSTANT[0] == 'a'
    assert CONSTANT[1] == 1

if __name__ == '__main__':
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-22 11:28:03.198756
# Unit test for function set_constant
def test_set_constant():

    assert ANSIBLE_CACHE_PLUGIN == 'jsonfile'
    assert ANSIBLE_CACHE_PLUGIN_TIMEOUT == 3600


# Generated at 2022-06-22 11:28:06.647597
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = "This is test message"
    version = "2.5"
    value = [1, 2, 3]
    deprecated = _DeprecatedSequenceConstant(value, msg, version)
    assert deprecated.__getitem__(1) == value[1]


# Generated at 2022-06-22 11:28:12.249849
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # FIXME: why is the class not marked with pytest.mark.parametrize?
    #
    # @pytest.mark.parametrize('value, msg, version, expected', [
    # ])
    # def test(value, msg, version, expected):
    #     assert _DeprecatedSequenceConstant(value, msg, version) == expected
    pass

# Generated at 2022-06-22 11:28:16.336845
# Unit test for function set_constant
def test_set_constant():
    target = {}
    set_constant('test1', 1, target)
    assert target['test1'] == 1

    # set_constant('test2', '{{test1}}', target)
    # assert target['test2'] == 1


# Generated at 2022-06-22 11:28:18.100345
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    t = _DeprecatedSequenceConstant([1], "msg", "version")
    assert len(t) == 1