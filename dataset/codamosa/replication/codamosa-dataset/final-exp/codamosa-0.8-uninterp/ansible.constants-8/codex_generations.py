

# Generated at 2022-06-22 11:19:16.809161
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([], 'msg', 'version')

# Generated at 2022-06-22 11:19:21.832268
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant([1, 2, 3, 4], "msg", "2.9.0")
    assert len(seq) == 4, "_DeprecatedSequenceConstant.__len__() is expected to return the length of the original sequence"


# Generated at 2022-06-22 11:19:24.036515
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(('a', 'b'), 'foo', '2.9')) == 2

# Generated at 2022-06-22 11:19:25.653629
# Unit test for function set_constant
def test_set_constant():
    assert MY_CONSTANT == 'foo'


# Generated at 2022-06-22 11:19:28.703506
# Unit test for function set_constant
def test_set_constant():
    config = ConfigManager()
    for setting in config.data.get_settings():
        set_constant(setting.name, setting.value)
        assert vars()[setting.name] == setting.value

# Generated at 2022-06-22 11:19:30.409663
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([1,2,3], 'just a test', '2.4')

# Generated at 2022-06-22 11:19:35.644239
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    message = 'This option will be removed in Ansible 2.12.'
    o = _DeprecatedSequenceConstant(value=['1', '2', '3'], msg=message, version='Ansible 2.12')
    assert isinstance(o, _DeprecatedSequenceConstant)
    assert list(o) == ['1', '2', '3']
    assert str(o) == """ ['1', '2', '3']"""


# Generated at 2022-06-22 11:19:36.804857
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant_test = _DeprecatedSequenceConstant(None, '', '')
    assert len(constant_test) == 0


# Generated at 2022-06-22 11:19:48.449896
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Test():
        def __init__(self, value, msg, version):
            self._value = value
            self._msg = msg
            self._version = version

        def __getitem__(self, y):
            return self._value[y]

    import sys
    import io
    my_stdout = io.StringIO()
    sys.stdout = my_stdout

    import unittest
    class TestActionsModuleClass(unittest.TestCase):
        def test__DeprecatedSequenceConstant___getitem__(self):
            t = Test(('helloworld', ), 'testing', '2.9')
            for i in range(0, len(t)):
                t[i]

            output = my_stdout.getvalue()
            assert output == ''

    test__DeprecatedSequenceCon

# Generated at 2022-06-22 11:19:52.586293
# Unit test for function set_constant
def test_set_constant():
    assert 'DEFAULT_BECOME_METHOD' in globals()


# Generate blueprint constants
for blueprint in config.data.get_settings_blueprints():

    set_constant('BLUEPRINT_' + blueprint.name.upper(), blueprint.value)


# Generated at 2022-06-22 11:20:09.743256
# Unit test for function set_constant
def test_set_constant():
    # First, make sure it will raise an exception if we try to set an already
    # existing value
    try:
        set_constant('INTERNAL_RESULT_KEYS', ['add_host', 'add_group'])
    except (NameError, ValueError) as e:
        assert "is already defined" in str(e)

    # Second, make sure it will not raise an exception with a valid name
    try:
        set_constant('TESTING_SET_CONSTANT', ['add_host', 'add_group'])
    except Exception as e:
        assert False, "set_constant failed with a valid argument"

    # Third, make sure it will not raise an exception with a valid name
    # and an export dictionary
    export = {}

# Generated at 2022-06-22 11:20:17.149367
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    l = [1,2,3]
    dep = _DeprecatedSequenceConstant(value=l, msg="Do not use this method", version="2.9")
    assert dep[0] == 1
    assert dep[1] == 2
    assert dep[2] == 3


# Generated at 2022-06-22 11:20:23.177690
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'Ansible 2.5 is the last release that will support python2.6.'
    version = '2.6'

    constant_test = add_internal_fqcns(('test', ))
    test = _DeprecatedSequenceConstant(constant_test, msg, version)

    assert len(test) == 1
    assert test[0] == constant_test[0]

# Generated at 2022-06-22 11:20:27.965495
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant([1, 2, 3], 'msg', '2.11')
    length = len(seq)
    assert len(seq) == len([1, 2, 3])
    assert len(seq) == length
    assert length == 3


# Generated at 2022-06-22 11:20:37.276581
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Arrange
    ansible_version = __version__
    msg = 'In Ansible %s, this option was removed in favor of foo' % ansible_version
    test_value = [ 'foo', 'bar' ]
    sut = _DeprecatedSequenceConstant(test_value, msg, ansible_version)

    # Act
    len_sut = len(sut)

    # Assert
    assert len_sut == len(test_value)


# Generated at 2022-06-22 11:20:41.244541
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    sequence_constant = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', 'version1.2')
    assert sequence_constant[1] == 'b'

# Generated at 2022-06-22 11:20:43.694732
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant(['foo', 'bar'], 'Unit test', '2.9')
    assert len(constant) == 2



# Generated at 2022-06-22 11:20:54.067631
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    import io
    import unittest

    test_message = 'foo'
    test_version = '1.2.3'
    test_value = [1, 2, 3]

    source = io.StringIO()
    sys.stderr = source
    x = _DeprecatedSequenceConstant(test_value, test_message, test_version)
    x[0]

    sys.stderr = sys.__stderr__
    message = source.getvalue()
    source.close()
    assert message == ' [DEPRECATED] %s, to be removed in %s\n' % (test_message, test_version)



# Generated at 2022-06-22 11:21:02.223286
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    list = [1,2]
    invalid_list_index = 3
    msg = 'this variable is deprecated'
    version = '2.8'
    dsc = _DeprecatedSequenceConstant(list, msg, version)
    # test that the value is retrieved correctly
    assert(dsc[0] == list[0])
    # test that the message is printed correctly
    assert(dsc[0] == list[0])
    # test that the value is retrieved correctly
    assert(dsc[1] == list[1])
    # test that the message is printed correctly
    assert(dsc[1] == list[1])
    # test that the value for an invalid index is retrieved correctly
    assert(dsc[invalid_list_index] == list[invalid_list_index])
    # test that the message is printed correctly

# Generated at 2022-06-22 11:21:07.516879
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'this is a warning'
    version = '2.9'
    sequence = _DeprecatedSequenceConstant([1, 2, 3], msg, version)
    assert sequence._value == [1, 2, 3]
    assert sequence._msg == msg
    assert sequence._version == version
    assert len(sequence) == 3
    assert sequence[1] == 2

# Generated at 2022-06-22 11:21:20.313676
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant('value', 'msg', 'version')) == len('value')

# Generated at 2022-06-22 11:21:23.339508
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = 'foo'
    msg = 'This is a test'
    version = 'foo'
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert dsc['bar'] == 'foo'


# Generated at 2022-06-22 11:21:28.687777
# Unit test for function set_constant
def test_set_constant():
    dict1 = {}
    dict2 = {}
    set_constant('one', 1, export=dict1)
    set_constant('two', 2, export=dict2)

    assert dict1['one'] == 1
    assert 'one' not in dict2
    assert dict2['two'] == 2
    assert 'two' not in dict1

# Generated at 2022-06-22 11:21:34.974283
# Unit test for function set_constant
def test_set_constant():
    constants = dict(
        ansible_default_ipv4=dict(address_family=2, ipv6=False),
        ansible_default_ipv6=dict(address_family=2, ipv6=True),
        ansible_default=dict(address_family=2, ipv6=False),
        ansible_vault_password_file=True,
        ansible_vault_password_file2=True,
        ansible_vault_password_file3=True,
    )
    for name, val in constants.items():
        set_constant(name, val)


# Generated at 2022-06-22 11:21:37.401908
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(tuple(), 'test', '2.11')) == 0


# Generated at 2022-06-22 11:21:44.344062
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    CONST_LIST = ['value1', 'value2', 'value3']
    const = _DeprecatedSequenceConstant(CONST_LIST, 'message', 'version')

    assert len(const) == len(CONST_LIST)
    assert const[0] == CONST_LIST[0]
    assert const[1] == CONST_LIST[1]
    assert const[2] == CONST_LIST[2]

# Generated at 2022-06-22 11:21:47.877447
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dep_seq_constant = _DeprecatedSequenceConstant([], "", "")
    assert len(dep_seq_constant) == 0
    assert dep_seq_constant[0] == None

# Generated at 2022-06-22 11:21:51.519597
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    conf = _DeprecatedSequenceConstant([], 'msg', 'version')
    assert conf == []
    assert conf.__len__() == 0
    assert conf.__getitem__(0) == None


# Generated at 2022-06-22 11:21:53.897472
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant(value={'a':'b'}, msg='msg', version='2.2')
    assert obj['a'] == 'b'


# Generated at 2022-06-22 11:22:00.573925
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant(('a','b','c','d'), 'This is a message for test', '4.3')
    assert constant[1] == 'b'
    with warnings.catch_warnings(record=True) as w:
        assert constant[1] == 'b'
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "This is a message for test" in str(w[-1].message)


# Generated at 2022-06-22 11:22:25.155506
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')
    assert isinstance(value, Sequence)
    assert len(value) == 3
    assert value[0] == 1
    assert value[1] == 2
    assert value[2] == 3

# Generated at 2022-06-22 11:22:31.741540
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    '''
    This test case tests __len__ method of _DeprecatedSequenceConstant class.
    '''
    input_value_list = [{}, [], [1,2,3]]
    for input_value in input_value_list:
        deprecated_constant = _DeprecatedSequenceConstant(input_value, 'test_msg', 'test_version')
        assert len(deprecated_constant) == len(input_value)

# Generated at 2022-06-22 11:22:34.801511
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant([1,2,3], 'this is deprecated', '2.0')
    assert len(dsc) == 3
    assert dsc[0] == 1

# Generated at 2022-06-22 11:22:40.388311
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant(value=[1, 2, 4], msg='msg', version='v2.4')
    assert isinstance(a, Sequence)
    assert len(a) == 3
    assert a[0] == 1

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:22:43.141538
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')
    assert(len(test) == 3)

del config, setting, value

# Generated at 2022-06-22 11:22:45.759581
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], "This is a message", "2.0")
    assert len(constant) == 3


# Generated at 2022-06-22 11:22:51.449727
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    v = ['a', 'b', 'c']
    m = 'msg'
    p = '2.0'

    dsc = _DeprecatedSequenceConstant(v, m, p)
    assert len(dsc) == len(v)
    assert 2 == dsc[2]



# Generated at 2022-06-22 11:22:55.840987
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    l1 = ['a', 'b', 'c']
    dsc = _DeprecatedSequenceConstant(l1, 'msg', 'version')
    assert len(dsc) == len(l1)



# Generated at 2022-06-22 11:23:01.126347
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert(foo == 'bar')
    set_constant('foo', 'bar', vars())
    assert(foo == 'bar')
    set_constant('foo', 'bar', {'foo': 'notbar'})
    assert(foo == 'bar')


# Generated at 2022-06-22 11:23:06.026989
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    val = _DeprecatedSequenceConstant(['test'], 'test message', 'v2.4')
    assert val._value == ['test']
    assert val._msg == 'test message'
    assert val._version == 'v2.4'
    assert val[0] == 'test'


# Generated at 2022-06-22 11:23:50.302482
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test = _DeprecatedSequenceConstant(value=[1, 2, 3, 4], msg='test_msg', version='test_version')
    assert test[0] == 1
    assert test[2] == 3
    assert test[-1] == 4
    assert test[-4] == 1



# Generated at 2022-06-22 11:23:56.711310
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "msg"
    version = "version"
    value = [1, 2, 3]
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert dsc._value == value
    assert dsc._msg == msg
    assert dsc._version == version
    assert len(dsc) == len(value)
    assert dsc[0] == value[0]
    assert dsc[1] == value[1]
    assert dsc[2] == value[2]

# Generated at 2022-06-22 11:24:02.365696
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'a'
    version = 'b'
    value = 'c'
    constant = _DeprecatedSequenceConstant(value, msg, version)
    assert constant._value == value
    assert constant._msg == msg
    assert constant._version == version
    assert len(constant) == 1
    assert constant[0] == 'c'


# Generated at 2022-06-22 11:24:08.148448
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    # Object should behave like Sequence
    assert isinstance(_DeprecatedSequenceConstant([], None, None), Sequence)

    # Object should emit a warning message
    d = _DeprecatedSequenceConstant([1, 2, 3], 'This is a warning message', '2.0')

    assert d[1] == 2



# Generated at 2022-06-22 11:24:15.716868
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    TEST_DEPRECATED_SEQUENCE_CONSTANT = _DeprecatedSequenceConstant(value=('a', 'b'), msg='Testing', version='1.0.0')

    assert(len(TEST_DEPRECATED_SEQUENCE_CONSTANT) == 2)
    assert(TEST_DEPRECATED_SEQUENCE_CONSTANT[0] == 'a')
    assert(TEST_DEPRECATED_SEQUENCE_CONSTANT[1] == 'b')

# Generated at 2022-06-22 11:24:18.762774
# Unit test for function set_constant
def test_set_constant():
    ''' sets constants and returns resolved options dict '''
    export = {}
    set_constant('name', 'value', export)
    assert 'name' in export
    assert export['name'] == 'value'



# Generated at 2022-06-22 11:24:24.720008
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(value=["a", "b"], msg="testing", version="2.1") == ["a", "b"]
    assert _DeprecatedSequenceConstant(value=["a"], msg="testing", version="2.1") != ["a", "b"]
    assert _DeprecatedSequenceConstant(value=[], msg="testing", version="2.1") == []


# Generated at 2022-06-22 11:24:27.716703
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant(value=[1,2,3], msg='Test', version='1.0')
    value = obj[1]
    assert value == 2


# Generated at 2022-06-22 11:24:32.554399
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant([1, 2, 3], 'hello', 'world')
    assert len(dsc) == 3
# End of unit test for method __len__ of class _DeprecatedSequenceConstant


# Generated at 2022-06-22 11:24:40.728887
# Unit test for function set_constant
def test_set_constant():
    # Test string
    set_constant('TEST_STRING', "This is a test")
    assert TEST_STRING == "This is a test"

    # Test tuple
    set_constant('TEST_TUPLE', ("a", "b"))
    assert TEST_TUPLE == ("a", "b")

    # Test dict
    set_constant('TEST_DICT', {'a': 1, 'b': 2})
    assert TEST_DICT == {'a': 1, 'b': 2}



# Generated at 2022-06-22 11:26:55.691787
# Unit test for function set_constant
def test_set_constant():
    assert getattr(all, 'TEST', None) is None
    set_constant('TEST', True, export=all)
    assert getattr(all, 'TEST', True) is True

# Generated at 2022-06-22 11:27:00.255718
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = ['this', 'that']
    msg = 'this is a message'
    version = '2.10'
    seq = _DeprecatedSequenceConstant(value, msg, version)
    assert seq[0] == 'this'
    assert seq[1] == 'that'
    assert len(seq) == len(value)

# Generated at 2022-06-22 11:27:01.615149
# Unit test for function set_constant
def test_set_constant():
    set_constant('name', 'test')
    assert 'test' == name

# Generated at 2022-06-22 11:27:06.347000
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = ['x', 'y']
    test_msg = 'fake-msg'
    test_version = 'fake-version'
    test_const = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_const) == len(test_value)
    assert test_const[0] == test_value[0]

# Generated at 2022-06-22 11:27:09.251095
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert _DeprecatedSequenceConstant([1, 2], 'test', '1.0') == [1, 2]
    assert len(_DeprecatedSequenceConstant([1, 2], 'test', '1.0')) == 2


# Generated at 2022-06-22 11:27:17.136788
# Unit test for function set_constant
def test_set_constant():
    '''function set_constant().
    '''
    _test_ns = {}
    set_constant('test', 'foo', _test_ns)
    assert _test_ns['test'] == 'foo'
    set_constant('test2', {'foo': 'bar'}, _test_ns)
    assert _test_ns['test2'] == {'foo': 'bar'}
    set_constant('test3', template_from_string("{{ test }}"), _test_ns)
    assert _test_ns['test3'] == '{{ test }}'
    set_constant('test3', "{{ test }}", _test_ns)
    assert _test_ns['test3'] == 'foo'
    set_constant('test3', "{{ test2.foo }}", _test_ns)
    assert _

# Generated at 2022-06-22 11:27:20.249057
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_value = ['a', 'b', 'c']
    test_instance = _DeprecatedSequenceConstant(test_value, 'msg', 'version')
    assert len(test_instance) == 3

# Generated at 2022-06-22 11:27:23.395689
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence = _DeprecatedSequenceConstant([1, 2], 'msg', 'version')
    assert sequence[0] == 1
    assert sequence[1] == 2
    assert sequence[-1] == 2
    assert len(sequence) == 2

# Generated at 2022-06-22 11:27:29.800926
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    var_name = 'inventory'
    msg = "The %s option is deprecated, use the inventory_dir option instead." % var_name
    version = "2.9"
    dep_seq = _DeprecatedSequenceConstant(to_text(getattr(config, var_name)), msg, version)
    assert len(dep_seq) == 2
    assert dep_seq[0] == '/etc/ansible/hosts'
    assert dep_seq[1] == '~/.ansible/hosts'

# Generated at 2022-06-22 11:27:32.299709
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], '', '')) == 0
