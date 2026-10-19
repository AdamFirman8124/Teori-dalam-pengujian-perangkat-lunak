

# Generated at 2022-06-22 11:19:20.783804
# Unit test for function set_constant
def test_set_constant():

    test_dict = {}
    set_constant('SET_CONSTANT_TEST', 'SET_CONSTANT_VALUE', export=test_dict)
    assert test_dict['SET_CONSTANT_TEST'] == 'SET_CONSTANT_VALUE'

# Generated at 2022-06-22 11:19:23.947179
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant([1, 2, 3], "msg", "1.0")
    assert len(dsc) == 3

# Generated at 2022-06-22 11:19:34.012005
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test
    set_constant('TEST_CONST_1', None, export=vars(__builtin__))
    set_constant('TEST_CONST_2', None, export=vars(__builtin__))
    set_constant('TEST_CONST_3', None, export=vars(__builtin__))
    set_constant('TEST_CONST_4', None, export=vars(__builtin__))
    import mock

# Generated at 2022-06-22 11:19:35.980773
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([], '', '')

# Generated at 2022-06-22 11:19:38.837984
# Unit test for function set_constant
def test_set_constant():
    foo = 'bar'
    set_constant('foo', 'baz', locals())
    assert foo == 'baz'



# Generated at 2022-06-22 11:19:40.010682
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    class_instance = _DeprecatedSequenceConstant(value=[], msg='foo', version='bar')
    assert class_instance.__len__() == 0

# Generated at 2022-06-22 11:19:44.503235
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    x = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert x[0] == 1
    assert x[1] == 2
    assert x[2] == 3


# Generated at 2022-06-22 11:19:51.250439
# Unit test for function set_constant
def test_set_constant():
    assert 'DEFAULT_BECOME_PASS' in vars()

# this is a copy of the above for now, because it's used in other places
# in the code, but should be deprecated and then removed
MAGIC_VARIABLE_MAPPING.update(dict(
    inventory_hostname=('ansible_hostname', 'ansible_fqdn', 'ansible_nodename', 'inventory_hostname', 'ansible_ssh_host'),
    group_names=('group_names', 'ansible_group_names'),
    groups=('groups', 'ansible_groups'),
    inventory_dir=('inventory_dir', 'ansible_inventory_dir'),
    inventory_file=('inventory_file', 'ansible_inventory_file'),
))

# Generated at 2022-06-22 11:19:59.183571
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import unittest
    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def runTest(self):
            seq = _DeprecatedSequenceConstant(value=(1, 2), msg='aaa', version='bbb')
            self.assertIsInstance(seq[0], int)
            self.assertEqual(seq[0], 1)

    test = Test__DeprecatedSequenceConstant()
    test.runTest()


# Generated at 2022-06-22 11:20:08.788574
# Unit test for function set_constant
def test_set_constant():
    DEST = {}
    set_constant('SOMEVAR', 'somevalue', DEST)
    assert DEST == {'SOMEVAR': 'somevalue'}
# FIXME: remove once play_context mangling is removed
# FIXME: this uses to_text instead of to_unicode to handle both unicode and bytes py2/py3
__MAGIC_VARIABLE_MAPPING = {}
for key, value in MAGIC_VARIABLE_MAPPING.items():
    __MAGIC_VARIABLE_MAPPING[key] = tuple([to_text(val) for val in value])
MAGIC_VARIABLE_MAPPING = __MAGIC_VARIABLE_MAPPING
del __MAGIC_VARIABLE_MAPPING

# This function is used to convert Ans

# Generated at 2022-06-22 11:20:17.944201
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    deprecated_sequence_constant = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert isinstance(deprecated_sequence_constant, type)
    assert deprecated_sequence_constant[1] == 2
    assert len(deprecated_sequence_constant) == 3

# Generated at 2022-06-22 11:20:22.758779
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST1', 'test')
    set_constant('TEST2', 'test2')
    assert TEST1 == 'test'
    assert TEST2 == 'test2'

    set_constant('TEST3', ['t', 'e', 's', 't', '3'])
    assert TEST3 == ['t', 'e', 's', 't', '3']

# Generated at 2022-06-22 11:20:26.621663
# Unit test for function set_constant
def test_set_constant():
    ''' test_set_constant '''
    export = dict()
    set_constant('test_var', 'bar', export=export)
    assert export['test_var'] == 'bar'

# Generated at 2022-06-22 11:20:34.603605
# Unit test for function set_constant
def test_set_constant():
    # 3 values are added to constants to be compared:
    # the first value with a key 'nested.key' is a dict
    # the second value with a key 'nested.key.foo' is a list
    # the third value with a key 'nested.key.bar' is a string
    # we will test that these values are correct, and that finding
    # a nested key will return the correct value
    values = {
        'nested.key': 10,
        'nested.key.foo': ['bar', 'foo'],
        'nested.key.bar': 'baz',
    }

    test_export = {}
    for key, value in values.items():
        set_constant(key, value, export=test_export)

    assert len(test_export) == 1

# Generated at 2022-06-22 11:20:43.490865
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Test:
        def warning(self, msg):
            self.warnings = msg

    t = Test()
    set_constant('t', t)

    s = _DeprecatedSequenceConstant(value=(), msg='msg', version='version')
    assert len(s) == 0

    s = _DeprecatedSequenceConstant(value=(1, 2, 3), msg='msg', version='version')
    assert len(s) == 3
    assert s[0] == 1
    assert s[1] == 2
    assert s[2] == 3

    assert t.warnings == 'msg, to be removed in version'
    assert t.warnings == 'msg, to be removed in version'
    assert t.warnings == 'msg, to be removed in version'


# Generated at 2022-06-22 11:20:46.696681
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_sequence = _DeprecatedSequenceConstant(['foo', 'bar'], 'message', 'version')
    assert len(test_sequence) == 2



# Generated at 2022-06-22 11:20:49.335014
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant([1, 2, 3], 't', 'v')
    assert len(a) == 3


# Generated at 2022-06-22 11:20:54.069552
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant((1, 2, 3, 4), 'msg', 'version')
    assert constant[0] == 1
    assert constant[1] == 2
    assert constant[2] == 3
    assert constant[3] == 4


# Generated at 2022-06-22 11:20:56.435290
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(value=[1, 2, 3], msg='incorrect msg', version='0.0.0')) == 3


# Generated at 2022-06-22 11:21:04.742630
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from mock import Mock, patch
    import sys

    with patch.object(_DeprecatedSequenceConstant, '__init__', return_value=None):
        m = Mock(_DeprecatedSequenceConstant)
        with patch.object(sys.stderr, 'write') as mock_stderr_write:
            m['foo']
            mock_stderr_write.assert_called_once_with(' [DEPRECATED] something, to be removed in 1.0\n')


# Generated at 2022-06-22 11:21:13.268750
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_sequence = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', '1.5')
    assert test_sequence[0] == 'a'
    assert test_sequence[1] == 'b'
    assert test_sequence[2] == 'c'


# Generated at 2022-06-22 11:21:16.764065
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant(('a', 'b', 'c'), 'msg', 'version')
    assert seq[0] == 'a'
    assert seq[1] == 'b'
    assert seq[2] == 'c'

# Generated at 2022-06-22 11:21:22.567512
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    tmp = _DeprecatedSequenceConstant((1,2,3), 'test', '2.0')
    assert tmp[0] == 1
    assert tmp[1:-1] == (2,)
    assert tmp[1:3] == (2, 3)
    assert tmp[0:5] == (1,2,3)


# Generated at 2022-06-22 11:21:26.350922
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    const = _DeprecatedSequenceConstant(value=[1,2,3], msg="I am deprecated", version="2.8")
    assert len(const) == 3
    assert const[1] == 2

# Generated at 2022-06-22 11:21:28.428758
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], "msg", "version")) == 0


# Generated at 2022-06-22 11:21:31.690706
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    c = _DeprecatedSequenceConstant(value='123', msg='my msg', version='1.1.1')
    assert len(c) == len('123')
    assert c[1] == '2'
    assert c.version == '1.1.1'
    assert c.msg == 'my msg'
    assert c._value == '123'

# Generated at 2022-06-22 11:21:41.804811
# Unit test for function set_constant
def test_set_constant():
    set_constant('magicstring', 'my_module', locals())
    assert locals()['magicstring'] == 'my_module'



# Generated at 2022-06-22 11:21:54.352769
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    test_cases = {
        'empty_list': {
            'value': [],
            'msg': 'Test of _DeprecatedSequenceConstant.__len__ with empty list',
            'version': '1.0.0',
            'expected_result': 0,
        },
        'non_empty_list': {
            'value': [1, 2, 3, 4],
            'msg': 'Test of _DeprecatedSequenceConstant.__len__ with non empty list',
            'version': '1.0.0',
            'expected_result': 4,
        },
    }

    for test_name, test_data in test_cases.items():
        test_value = _DeprecatedSequenceConstant(test_data['value'], test_data['msg'], test_data['version'])


# Generated at 2022-06-22 11:21:59.376408
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'test message for _DeprecatedSequenceConstant'
    version = '2.0'
    value = ['a', 'b', 'c']
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert len(value) == len(dsc)
    assert value[0] == dsc[0]


# Generated at 2022-06-22 11:22:04.782667
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    d = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', '2.14.0')
    assert d.__getitem__(0) == 'a'
    assert d.__getitem__(1) == 'b'
    assert d.__getitem__(2) == 'c'


# Generated at 2022-06-22 11:22:21.434901
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'message'
    version = 'version'

    constant = _DeprecatedSequenceConstant(
        value=['value1', 'value2'],
        msg=msg,
        version=version,
    )

    result = constant[0]

    assert result == 'value1'
    assert constant.__len__() == 2



# Generated at 2022-06-22 11:22:27.288403
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    deprecated_obj = _DeprecatedSequenceConstant(value=['a', 'b', 'c', 'd'], msg='Test message', version='2.0.0')
    assert isinstance(deprecated_obj, Sequence)
    assert isinstance(deprecated_obj, _DeprecatedSequenceConstant)
    assert deprecated_obj[0] == 'a'
    assert deprecated_obj[1] == 'b'
    assert len(deprecated_obj) == 4

# Generated at 2022-06-22 11:22:35.341068
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(set([])) == 0
    assert len(set((_ACTION_IMPORT_PLAYBOOK))) == 1
    assert len(set((_ACTION_IMPORT_PLAYBOOK, _ACTION_INCLUDE))) == 2
    assert len(set((_ACTION_IMPORT_PLAYBOOK, _ACTION_INCLUDE, _ACTION_IMPORT_PLAYBOOK))) == 2
    assert len(set((_ACTION_IMPORT_PLAYBOOK, _ACTION_INCLUDE, _ACTION_IMPORT_PLAYBOOK, _ACTION_SET_FACT))) == 3



# Generated at 2022-06-22 11:22:38.301646
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([], 'test_msg', '1.0')[0] == []


# Generated at 2022-06-22 11:22:41.278249
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    obj = _DeprecatedSequenceConstant(value=[], msg='', version='')
    try:
        obj[1]
    except Exception:
        raise AssertionError()

# Generated at 2022-06-22 11:22:44.072241
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    actual = _DeprecatedSequenceConstant(['a','b','c'], 'test message', 'test version').__getitem__(1)
    assert actual == 'b'

# Generated at 2022-06-22 11:22:48.434961
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    mock_msg = 'Some msg'
    mock_version = '2.8'
    mock_value = ['a', 'b']
    sequence_constant = _DeprecatedSequenceConstant(mock_value, mock_msg, mock_version)
    assert sequence_constant[0] == 'a'
    assert sequence_constant[1] == 'b'


# Generated at 2022-06-22 11:22:51.077866
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    foo = _DeprecatedSequenceConstant([1,2,3], 'test', '2.12')
    assert len(foo) == 3


# Generated at 2022-06-22 11:22:56.874075
# Unit test for function set_constant
def test_set_constant():
    set_constant('A', 'B')
    assert A == 'B'
    set_constant('A', 'C', dict())
    assert A == 'B'
    set_constant('A', 'C', dict(A='B'))
    assert A == 'B'

# Generated at 2022-06-22 11:22:59.412963
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    a = _DeprecatedSequenceConstant(["a"], "msg", "ver")
    assert a[0] == "a"


# Generated at 2022-06-22 11:23:34.483042
# Unit test for function set_constant
def test_set_constant():
    from ansible.constants import DEFAULT_HOST_LIST

    set_constant('DEFAULT_HOST_LIST', 'localhost')
    assert DEFAULT_HOST_LIST == 'localhost'
    set_constant('DEFAULT_HOST_LIST', '127.0.0.1')

# sets locale to C
# This is to prevent unicode decode errors when trying to
# compare hostnames and IPs that contain out-of-range characters.
# We don't care about the coding, just how they compare,
# so we set to C.
from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
from ansible.module_utils._text import to_text
import os
import platform

# This is normally set in the CLI code, but if ansible
# is being used as a

# Generated at 2022-06-22 11:23:37.426766
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Test(object):
        def __getitem__(self, value):
            return True
    seq_constant = _DeprecatedSequenceConstant(Test(), 'Test', '2.10')
    assert bool(seq_constant[0]) is True

# Generated at 2022-06-22 11:23:42.683253
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    s = _DeprecatedSequenceConstant()
    assert s._value == tuple(), s._value
    assert s._msg == '', s._msg
    assert s._version == '', s._version
    s = _DeprecatedSequenceConstant(value='value', msg='msg', version='version')
    assert s._value == ('value', ), s._value
    assert s._msg == 'msg', s._msg
    assert s._version == 'version', s._version

# Generated at 2022-06-22 11:23:48.038752
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    array = ['a', 'b', 'c', 'd']
    const_array = _DeprecatedSequenceConstant(array, 'testing deprecation', '2.9')
    assert len(const_array) == 4
    assert const_array[0] == 'a'
    assert const_array[1] == 'b'
    assert const_array[2] == 'c'
    assert const_array[3] == 'd'

# Generated at 2022-06-22 11:23:50.202845
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    _DeprecatedSequenceConstant(['a', 'b', 'c'], 'Test message', '1.0')(1)

# Generated at 2022-06-22 11:23:52.165187
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant(('foo', 'bar'), 'some message', '3.0')

# Generated at 2022-06-22 11:23:54.969674
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant(value=[1,2,3], msg="test_msg", version="test_version")
    assert len(d) == 3
    return

# Generated at 2022-06-22 11:24:03.635419
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():

    class TestDeprecatedSequenceConstant(object):

        def test__init__(self, mocker):
            ''' constructor '''
            mocker.patch('ansible.constants._deprecated')

            class A(object): pass
            msg = 'msg'
            version = 'version'
            a = A()
            o = _DeprecatedSequenceConstant(a, msg, version)
            assert o._msg == msg
            assert o._version == version
            assert o._value == a
            # already deprecated
            _DeprecatedSequenceConstant(a, msg, version)
            _DeprecatedSequenceConstant(a, msg, version)

        def test___len__(self, mocker):
            ''' returns length of _value '''
            mocker.patch('ansible.constants._deprecated')


# Generated at 2022-06-22 11:24:12.434489
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = ('string', )
    test_msg = 'This is a test message.'
    test_version = '1.5'

    dsc = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert dsc._value == test_value
    assert dsc._msg == test_msg
    assert dsc._version == test_version
    assert len(dsc) == len(test_value)
    assert dsc[0] == test_value[0]

_BREAKING_VERSION_FORMAT = config.get_config_value('BREAKING_VERSION_FORMAT')

# Generated at 2022-06-22 11:24:14.078689
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant([0, 1, 2], 'Message', '2.9')
    assert len(dsc) == len([0, 1, 2])

# Generated at 2022-06-22 11:25:09.116324
# Unit test for function set_constant
def test_set_constant():
    # test for overriding default value with constant
    set_constant('DEFAULT_BECOME_PASS', 'test_pass', globals())
    assert DEFAULT_BECOME_PASS == 'test_pass'

    set_constant('DEFAULT_BECOME_PASS', None, globals())
    assert DEFAULT_BECOME_PASS is None

# Generated at 2022-06-22 11:25:13.089893
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'test message'
    dsc = _DeprecatedSequenceConstant([1, 2], msg, '0.999')
    assert len(dsc) == 2
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert len(dsc) == 2


# Generated at 2022-06-22 11:25:23.290973
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = (1, 2, 3)
    assert _DeprecatedSequenceConstant(test_value, 'msg', '1.0') == _DeprecatedSequenceConstant(test_value, 'msg', '1.0')
    assert _DeprecatedSequenceConstant(test_value, 'msg', '1.0') != _DeprecatedSequenceConstant((1, 2, 4), 'msg', '1.0')
    assert len(_DeprecatedSequenceConstant(test_value, 'msg', '1.0')) == 3
    assert _DeprecatedSequenceConstant(test_value, 'msg', '1.0')[0] == 1
    assert _DeprecatedSequenceConstant(test_value, 'msg', '1.0')[1] == 2

# Generated at 2022-06-22 11:25:30.877234
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    EXPECTED_MSG = 'msg'
    EXPECTED_VERSION = 'version'
    EXPECTED_LEN = 2
    EXPECTED_VAL = 1

    sut = _DeprecatedSequenceConstant([0, 1], EXPECTED_MSG, EXPECTED_VERSION)
    assert len(sut) == EXPECTED_LEN
    assert sut[1] == EXPECTED_VAL



__all__ = ('__version__', )

# Generated at 2022-06-22 11:25:36.153425
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant([1, 2], 'message', '1.0')
    assert len(dsc) == 2
    assert dsc[0] == 1
    assert dsc[1] == 2
    assert dsc._value == [1, 2]
    assert dsc._msg == 'message'
    assert dsc._version == '1.0'



# Generated at 2022-06-22 11:25:42.606472
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'no longer valid', '2.0')
    assert len(a) == 3

# Unit test to verify that REJECT_EXTS contains .pyc when running on py2
# Using assertRaises to verify that we have a .pyc in the tuple

# Generated at 2022-06-22 11:25:50.289497
# Unit test for function set_constant
def test_set_constant():
    CONFIG_ITEM = ('config', 'item', 'value')
    SET_CONSTANT_TEST = set_constant(*CONFIG_ITEM)
    assert isinstance(SET_CONSTANT_TEST, dict)
    assert len(SET_CONSTANT_TEST) == 1
    assert SET_CONSTANT_TEST == vars()
    assert vars()['config'] == 'item'
    assert vars()['value'] == 'value'

# Generated at 2022-06-22 11:25:52.094091
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], msg='msg', version='2.9')) == 3

# Generated at 2022-06-22 11:25:56.645430
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant(1, 'test', '2.9') == 1
    assert _DeprecatedSequenceConstant((1, 2), 'test', '2.9')[1] == 2
    assert len(_DeprecatedSequenceConstant((1, 2, 3), 'test2', '2.9')) == 3

# Generated at 2022-06-22 11:25:57.109732
# Unit test for function set_constant
def test_set_constant():
    assert True

# Generated at 2022-06-22 11:26:54.441503
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Note: This method will be used in linters
    test_value = [1, 2]
    test_msg = 'test_msg'
    test_version = '2.10'
    test_item = _DeprecatedSequenceConstant(test_value, test_msg, test_version)
    assert len(test_item) == len(test_value)


# Generated at 2022-06-22 11:27:03.058040
# Unit test for function set_constant
def test_set_constant():
    def test_func():
        set_constant('test_constant', 1234, vars())
    test_func()

    if 'test_constant' in vars() and vars()['test_constant'] == 1234:
        pass  # the function works, don't raise an assertion error
    else:
        raise AssertionError('set_constant() is not working properly')
test_set_constant()

# Unless deprecation warnings have been disabled, warn about deprecated constants
if config.data.get_config_value('deprecation_warnings'):
    for msg, version in config.DEPRECATIONS:
        _deprecated(msg, version)

# Generated at 2022-06-22 11:27:04.905894
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(value=[1, 2, 3], msg='msg', version='version')) == 3

# Generated at 2022-06-22 11:27:12.987205
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # valid case
    obj = _DeprecatedSequenceConstant(value=[1, 2, 3], msg="test msg", version="version")
    assert obj[0] == 1
    assert obj[1] == 2
    assert obj[2] == 3
    # invalid case
    try:
        obj[3]
    except IndexError:
        # IndexError: list index out of range(3)
        pass

if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-x', __file__, '-v']))

# Generated at 2022-06-22 11:27:22.515885
# Unit test for function set_constant
def test_set_constant():
    test_settings = {'foo': 1, 'bar': 'baz', 'blip': '{{blap}}'}
    test_env = {'blap': 2}
    test_export = {}
    for key, value in test_settings.items():
        set_constant(key, value, test_export)

    assert test_export == {'foo': 1, 'bar': 'baz', 'blip': '{{blap}}'}

    # now test variable substitution
    set_constant('blip', test_settings['blip'], test_export, vars=test_env)
    assert test_export['blip'] == 2

# Generated at 2022-06-22 11:27:25.181405
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    foo = _DeprecatedSequenceConstant("foo", "bar", "1.2")
    assert foo._value == "foo"
    assert foo[0] == "f"

# Generated at 2022-06-22 11:27:33.148680
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    test_values = [
        ((_ACTION_IMPORT_PLAYBOOK, "msg", "version"), _ACTION_IMPORT_PLAYBOOK, "msg", "version"),
        ((_ACTION_IMPORT_ROLE, "msg", "version"), _ACTION_IMPORT_ROLE, "msg", "version"),
        ((_ACTION_INCLUDE, "msg", "version"), _ACTION_INCLUDE, "msg", "version")
    ]

    for test_value in test_values:
        dsc = _DeprecatedSequenceConstant(*test_value[:-2])
        assert dsc[0] == test_value[-2][0]

# Generated at 2022-06-22 11:27:37.380178
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class_inst = _DeprecatedSequenceConstant(value=(1, 2, 3), msg='Test message', version='1.0')
    assert len(class_inst) == 3
    assert class_inst[1] == 2

# Generated at 2022-06-22 11:27:46.580220
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Setup data for testcase
    data = ('a', 'b')
    msg = 'dummy'
    version = '1.0.0'

# Generated at 2022-06-22 11:27:48.841567
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['a','b','c'], 'deprecated', '2.8')) == 3
