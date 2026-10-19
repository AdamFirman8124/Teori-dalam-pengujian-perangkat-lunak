

# Generated at 2022-06-22 11:19:20.629997
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    depconst = _DeprecatedSequenceConstant(1.0, 'test_msg', '2.8')
    assert len(depconst) == 1


# Generated at 2022-06-22 11:19:25.324188
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_values = [
        (_DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version'), 3),
    ]

    for value, expected in test_values:
        assert len(value) == expected



# Generated at 2022-06-22 11:19:28.752615
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant('foo', 'bar', 'baz')
    assert seq.__len__() == 3
    assert seq[0] == 'f'
    assert seq[2] == 'o'

# Generated at 2022-06-22 11:19:34.164843
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = _DeprecatedSequenceConstant(value=(1, 2, 3), msg='test_msg', version='test_version')
    assert value[0] == 1
    assert value[1] == 2
    assert value[2] == 3


# Generated at 2022-06-22 11:19:37.507278
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'test', '2.0')
    assert len(constant) == 3


# Generated at 2022-06-22 11:19:48.871702
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = ['foo', 'bar']
    deprecation_msg = 'This is a deprecated list'
    deprecation_version = 'v3.0'
    dep = _DeprecatedSequenceConstant(value, deprecation_msg, deprecation_version)
    assert len(dep) == len(value)
    assert dep[0] == value[0]
    assert dep[1] == value[1]


# CONSTANT DEPRECATIONS ###

for deprecated_opt in ('module_compression', 'control_path'):
    _deprecated(
        "The '{0}' configuration option was deprecated in version 2.10 and will be removed in a future version.".format(deprecated_opt),
        version='2.11'
    )


# Generated at 2022-06-22 11:19:54.280126
# Unit test for function set_constant
def test_set_constant():
    import ast
    import copy

    export = copy.copy(vars())
    var = "foo bar"

    set_constant("FOO_BAR", var)

    assert export != vars()
    assert ast.literal_eval("FOO_BAR") == var

# Generated at 2022-06-22 11:19:58.872231
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'test msg'
    version = '2.1'
    actual_value = [1, 2, 3]
    expected_value = actual_value[1]
    obj = _DeprecatedSequenceConstant(actual_value, msg, version)
    value = obj[1]
    assert expected_value == value

# Generated at 2022-06-22 11:20:04.151022
# Unit test for function set_constant
def test_set_constant():
    set_constant('testing', 'string')
    assert testing == 'string'
    set_constant('testing', ['one', 'two'])
    assert testing == ['one', 'two']


import ansible.constants
ansible.constants.__all__ = [k for k in globals().keys() if not k.startswith('_')]  # pylint: disable=undefined-variable

# Generated at 2022-06-22 11:20:14.632605
# Unit test for function set_constant
def test_set_constant():
    test_constants = {'A': 'a', 'B': 1, 'C': 1.1, 'D': True, 'E': False, 'F': None, 'G': [1, 'a'], 'H': {'a': 'b'},
                      'I': ('a', 1), 'J': {'a', 'b'}}
    for key, value in test_constants.items():
        set_constant(key, value)
        assert key in globals()
        assert globals()[key] == value
    set_constant('K', [1, 2, {'a': 'b'}, ('c', 'd')])
    assert globals()['K'] == [1, 2, {'a': 'b'}, ('c', 'd')]

# Generated at 2022-06-22 11:20:25.643475
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = _DeprecatedSequenceConstant([1, 2, 3], u'test', '2.9')
    # test __getitem__ method
    assert x[0] == 1
    assert x[1] == 2
    # test __len__ method
    assert len(x) == 3


# Generated at 2022-06-22 11:20:28.065605
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([1, 2, 3, 4], 'testing', '1.0')[1] == 2

# Generated at 2022-06-22 11:20:42.091944
# Unit test for function set_constant
def test_set_constant():
    # Set None
    example_dict = {'a': 'A'}
    set_constant('b', None, example_dict)
    assert 'b' in example_dict

    # Set string
    set_constant('a', 'a', example_dict)
    assert example_dict['a'] == 'a'

    # Test name is a number
    set_constant(1, '1', example_dict)
    assert example_dict['1'] == '1'

    # Test if name is valid
    assert_msg = r"Invalid variable name '(&)"
    try:
        set_constant('(&)', 'invalid', example_dict)
    except AssertionError as e:
        assert str(e) == assert_msg

# Generated at 2022-06-22 11:20:44.533027
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")
    assert len(sequence) == len([1, 2, 3])


# Generated at 2022-06-22 11:20:48.200339
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    a = _DeprecatedSequenceConstant([1, 2, 3], 'xyz', '1.2.1')
    assert(a[0] == 1)
    assert(a[-1] == 3)


# Generated at 2022-06-22 11:20:53.266934
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    '''
    Set x to an instance of _DeprecatedSequenceConstant,
    then try to get x[0]
    '''
    x = _DeprecatedSequenceConstant((1, 2, 3), 'msg', 'version')
    assert x[0] == 1

# Generated at 2022-06-22 11:21:06.823614
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.module_utils.common.collections import _DeprecatedSequenceConstant
    lst = [1, 2, 3]
    # Test for _DeprecatedSequenceConstant when the list is non-empty
    dsc = _DeprecatedSequenceConstant(value=lst, msg="msg", version="version")
    assert(lst[0] == dsc[0])
    assert(lst[1] == dsc[1])
    assert(lst[2] == dsc[2])
    # Test for _DeprecatedSequenceConstant when the list is empty
    dsc = _DeprecatedSequenceConstant(value=[], msg="msg", version="version")
    assert(dsc[0] == None)
    assert(dsc[1] == None)

# Generated at 2022-06-22 11:21:11.140950
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    '''
    Test __getitem__() of _DeprecatedSequenceConstant
    '''
    # _DeprecatedSequenceConstant()
    assert _DeprecatedSequenceConstant(value=(), msg='testing', version='1.0') == ()
    # _DeprecatedSequenceConstant() with value
    assert _DeprecatedSequenceConstant(value=(1, ), msg='testing', version='1.0')[0] == 1
    # _DeprecatedSequenceConstant() with unmatching value
    assert _DeprecatedSequenceConstant(value=(1, ), msg='testing', version='1.0')[1] is None


# Generated at 2022-06-22 11:21:14.959111
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_constant = _DeprecatedSequenceConstant([1, 2, 3], "foo deprecated", "1.2")
    assert test_constant[0] == 1
    assert len(test_constant) == 3


# Generated at 2022-06-22 11:21:18.388023
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "this is a message"
    version = "1.0"
    value = [1,2]
    sc = _DeprecatedSequenceConstant(value, msg, version)
    assert sc.__len__() == 2

# Generated at 2022-06-22 11:21:32.127018
# Unit test for function set_constant
def test_set_constant():
    globals()['TEST_VALUE'] = 'ask'
    set_constant('TEST_VALUE', 'a value')
    assert TEST_VALUE == 'a value'

# Generated at 2022-06-22 11:21:38.277247
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = [1, 2, 3]
    msg = 'test_msg'
    version = 'v1'
    deprecated = _DeprecatedSequenceConstant(value, msg, version)
    assert deprecated._value == value
    assert deprecated._msg == msg
    assert deprecated._version == version

# TODO: expand this list to cover all constants

# Generated at 2022-06-22 11:21:49.594448
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    deprecated_values = [
        ('what', 'It was an example', '1.5'),
        ('the', "It's deprecated too", '1.5')
    ]
    test_values = [
        ('foo', 'never mind', '2.0'),
        ('bar', 'never mind', '2.0')
    ]
    ans = _DeprecatedSequenceConstant(deprecated_values, 'It was an example', '1.5')
    assert(isinstance(ans, _DeprecatedSequenceConstant))
    assert(len(ans) == 2)
    assert(ans[0] == [('what', 'It was an example', '1.5')])
    assert(ans[1] == [('the', "It's deprecated too", '1.5')])
    ans.append(test_values)

# Generated at 2022-06-22 11:21:52.086382
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([1,2,3], "message", "2.11")) == 3


# Generated at 2022-06-22 11:21:56.240822
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant('value', 'msg', 'version')
    assert obj._msg == 'msg'
    assert obj._version == 'version'
    assert obj._value == 'value'
    assert len(obj) == len('value')
    assert obj[0] == 'v'


# Generated at 2022-06-22 11:21:59.695108
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    sequence = _DeprecatedSequenceConstant( ('a', 'b', 'c'), 'test', '2.8')
    assert sequence[0] == 'a'
    assert sequence[1] == 'b'
    assert sequence[2] == 'c'

# Generated at 2022-06-22 11:22:03.019398
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_sequence = _DeprecatedSequenceConstant({"foo": "bar"}, "This is deprecated", version="2.0")

    assert len(test_sequence) == 1
    assert test_sequence["foo"] == "bar"

# Generated at 2022-06-22 11:22:09.847037
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'test deprecated'
    version = '1.2.3'
    value = [1, 2, 3]
    sequence = _DeprecatedSequenceConstant(value, msg, version)
    assert tuple(sequence) == tuple(value)
    assert len(sequence) == len(value)
    assert sequence[0] == value[0]
    assert sequence[1] == value[1]
    assert sequence[2] == value[2]

# Generated at 2022-06-22 11:22:17.259917
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant(['a', 'b'], 'test message', 'TEST VERSION')
    assert len(constant) == 2
    assert constant[0] == 'a'
    assert constant[1] == 'b'

if __name__ == '__main__':
    import sys
    for name in dir():
        if name.startswith('__'):
            continue
        obj = getattr(sys.modules[__name__], name)
        if not callable(obj):
            print("{0:<24} {1:>16} {2}".format(name, type(obj), obj))

# Generated at 2022-06-22 11:22:21.586965
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    d = _DeprecatedSequenceConstant(['a', 'b'], 'msg', '1.0')
    assert d[0] == 'a', d[0]
    assert not hasattr(d, '_msg')
    assert not hasattr(d, '_version')


# Generated at 2022-06-22 11:22:45.515128
# Unit test for function set_constant
def test_set_constant():

    from tempfile import mkdtemp
    from shutil import rmtree
    from ansible.config.manager import ConfigManager
    from ansible.module_utils.six import PY3

    test_dir = mkdtemp()
    tmp_config = test_dir + "/ansible.cfg"


# Generated at 2022-06-22 11:22:55.780196
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test for change in number of elements
    test1 = _DeprecatedSequenceConstant([1, 2, 3, 4], 'Testing Message', '2.9')
    test2 = _DeprecatedSequenceConstant([1, 2], 'Testing Message', '2.9')
    assert test1.__len__() == test2.__len__()
    # Test for change in type of elements
    test1 = _DeprecatedSequenceConstant([1, 2, 3, 4], 'Testing Message', '2.9')
    test2 = _DeprecatedSequenceConstant([1, 2, '3', '4'], 'Testing Message', '2.9')
    assert test1.__getitem__(2) == test2.__getitem__(2)
    # Test for change in order of elements
    test1 = _DeprecatedSequ

# Generated at 2022-06-22 11:23:07.722079
# Unit test for function set_constant
def test_set_constant():
    import sys
    import types
    global_vars = sys.modules[__name__].__dict__
    set_constant('A', 'B')
    assert global_vars.get('A') == 'B'
    set_constant('C', 1)
    assert global_vars.get('C') == 1
    set_constant('D', True, export=global_vars)
    assert global_vars.get('D') is True
    set_constant('E', [1, 2, 3])
    assert global_vars.get('E') == [1, 2, 3]
    set_constant('F', [])
    assert global_vars.get('F') == []
    set_constant('G', dict(a=1, b=2))
    assert global_vars.get

# Generated at 2022-06-22 11:23:12.656962
# Unit test for function set_constant
def test_set_constant():
    ''' set_constant does what it says '''
    test_dict = {}
    assert test_dict.get('foo') is None, "Failed to initialize test dictionary"
    set_constant('foo', 'bar', export=test_dict)
    assert test_dict.get('foo') == 'bar', "Failed to set constant to dictionary"

# Generated at 2022-06-22 11:23:16.300376
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq_const = _DeprecatedSequenceConstant([1, 2, 3, 4, 5], 'This is just test', 'v2.8')
    assert len(seq_const) == 5, 'len should be 2'


# Generated at 2022-06-22 11:23:22.502062
# Unit test for function set_constant
def test_set_constant():
    my_dict = {}
    set_constant('test_constant', 'test_value', export=my_dict)
    assert my_dict['test_constant'] == 'test_value'
    set_constant('test_constant', 'new_value', export=my_dict)
    assert my_dict['test_constant'] == 'test_value'

# Generated at 2022-06-22 11:23:24.265842
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # tests:
    # _DeprecatedSequenceConstant({1, 2}, "msg", "version")[0] == 1
    assert _DeprecatedSequenceConstant({1, 2}, "msg", "version")[0] == 1


# Generated at 2022-06-22 11:23:35.394211
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    class _Test(object):
        """ Dummy class used as warning receiver"""

        def __init__(self, method_name):
            self.called = False
            setattr(self, method_name, self._called)

        def _called(self, *args):
            self.called = True

    # First test the normal case where a _DeprecatedSequenceConstant is
    # accessed without warnings
    test = _Test('warning')
    result = _DeprecatedSequenceConstant([1, 2, 3], 'message', '1.0')('warning')
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3
    assert not test.called

    # Now check that after we trigger the warning, the warning is sent
    # each time we access the _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:23:39.876074
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = (1, 2)
    msg = 'message'
    version = '6.0'
    obj = _DeprecatedSequenceConstant(value, msg, version)
    assert obj._value == value
    assert obj._msg == msg
    assert obj._version == version
    assert len(obj) == len(value)
    assert obj[0] == value[0]
    obj.append(4)
    assert obj[2] == 4

# Generated at 2022-06-22 11:23:43.673677
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = "msg"
    version = "version"
    value = "value"
    x = _DeprecatedSequenceConstant(value, msg, version)
    assert x[0] == value[0]



# Generated at 2022-06-22 11:24:05.645543
# Unit test for function set_constant
def test_set_constant():
    '''unit tests for function set_constant'''

# Generated at 2022-06-22 11:24:12.184824
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class _Test__DeprecatedSequenceConstant:
        def __init__(self):
            self.calls = 0
            self.msgs = []

        def deprecated(self, msg, version):
            self.calls += 1
            self.msgs.append((msg, version))

    display = _Test__DeprecatedSequenceConstant()
    msg = 'Unable to load yaml file. please install python-yaml'
    msg_version = '2.3'
    a = _DeprecatedSequenceConstant(('foo',), msg, msg_version)
    a[0]
    assert display.calls == 1
    assert (msg, msg_version) == display.msgs[0]


# Generated at 2022-06-22 11:24:14.281069
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'this is a test message'
    version = '2.10'
    seq_constant = _DeprecatedSequenceConstant([1, 2, 3], msg, version)

    assert seq_constant[1] == 2



# Generated at 2022-06-22 11:24:15.717252
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    v = [1, 2, 3]
    o = _DeprecatedSequenceConstant(v, '', '')
    assert len(v) == len(o)


# Generated at 2022-06-22 11:24:26.443379
# Unit test for function set_constant
def test_set_constant():
    constants1 = {}
    constants2 = {}

    # should have no effect on existing dicts
    set_constant('test1', 'foo', constants1)
    set_constant('test2', 'foo', constants2)
    assert 'test1' not in vars()
    assert 'test2' not in vars()
    assert constants1.get('test1') == 'foo'
    assert constants2.get('test2') == 'foo'
    assert constants1.get('test2') is None
    assert constants2.get('test1') is None

    # should set in global dict
    set_constant('test3', 'foo')
    assert 'test3' in vars()
    assert vars()['test3'] == 'foo'



# Generated at 2022-06-22 11:24:33.199040
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # Create a _DeprecatedSequenceConstant object
    test = _DeprecatedSequenceConstant(['a', 'b'], 'msg', 'version')
    # The type returned must be AnsibleUnsafeText
    assert isinstance(test[0], AnsibleUnsafeText)
    assert isinstance(test[1], AnsibleUnsafeText)


# Generated at 2022-06-22 11:24:39.806109
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = "This is a deprecated message"
    version = "2.9"
    value = 1
    c = _DeprecatedSequenceConstant(value, msg, version)
    if c.__len__() == 1:
        print("test__DeprecatedSequenceConstant___len__ pass")
    else:
        print("test__DeprecatedSequenceConstant___len__ fail")


# Generated at 2022-06-22 11:24:46.991109
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import pytest
    called = [False]
    def _warning(msg):
        called[0] = True
    def _deprecated(msg, version):
        called[0] = True
    setattr(_DeprecatedSequenceConstant, '_deprecated', _deprecated)
    setattr(_DeprecatedSequenceConstant, '_warning', _warning)
    a = _DeprecatedSequenceConstant([1, 2, 3], 'foo', 'bar')
    assert called == [False]
    assert a[1] == 2
    assert called == [True]


# Generated at 2022-06-22 11:24:51.586496
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_sequence_constant = _DeprecatedSequenceConstant(value=('delapouite', 'carlos-abeya', 'sbed'),
                                                         msg='This is a test',
                                                         version='1.0')

    assert len(test_sequence_constant) == 3
    assert test_sequence_constant[2] == 'sbed'

# Generated at 2022-06-22 11:24:56.627554
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    version = '2.12'
    deprecated_modules = ('uri', 'urllib')
    msg = "Imported modules {0} are deprecated, use the module {} instead".format(', '.join(deprecated_modules), 'xxx')
    _DeprecatedSequenceConstant(deprecated_modules, msg, version)

# Generated at 2022-06-22 11:25:14.887790
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    l = ('first', 'second')
    dsc = _DeprecatedSequenceConstant(l, 'test_message', '3.0.0')
    assert len(dsc) == len(l)
    assert dsc[0] == l[0]
    assert dsc[1] == l[1]

# Generated at 2022-06-22 11:25:16.980201
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONSTANT', 'value', globals())
    assert TEST_CONSTANT == 'value'

# Generated at 2022-06-22 11:25:21.023385
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dep_seq_constant_obj = _DeprecatedSequenceConstant(value=[1, 2], msg='this is a test message', version='2.4')
    assert dep_seq_constant_obj.__getitem__(0) == 1



# Generated at 2022-06-22 11:25:22.376869
# Unit test for function set_constant
def test_set_constant():

    assert DEFAULT_HOST_LIST == '/etc/ansible/hosts'

# Generated at 2022-06-22 11:25:25.727224
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(add_internal_fqcns((_DeprecatedSequenceConstant(['a', 'b', 'c'], 'test', '2.9'),))) == 3


# Generated at 2022-06-22 11:25:36.814812
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    '''Unit test for constructor of class _DeprecatedSequenceConstant.'''
    # For some reason, the constructor of class _DeprecatedSequenceConstant can only be invoked
    # from the outer scope, otherwise, the test will fail. WTF?
    global _ACCEPTED_KEYS
    _ACCEPTED_KEYS = _DeprecatedSequenceConstant(value=['a', 'b'], msg='This is a test', version='2.10')

# DEBUGGING/DEV
try:
    import __main__ as mod_main
except Exception:
    import sys
    mod_main = sys.modules['__main__']

DEBUG = "ANSIBLE_DEBUG" in os.environ or "ANSIBLE_LOG_PATH" in os.environ


# Generated at 2022-06-22 11:25:40.472245
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert_equal(len(_DeprecatedSequenceConstant(['items'], 'msg', 'version')), len(['items']))



# Generated at 2022-06-22 11:25:43.923787
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = (1, 2, 3)
    msg = 'msg'
    version = 'version'
    dep_seq_const = _DeprecatedSequenceConstant(value, msg, version)
    assert len(dep_seq_const) == len(value)


# Generated at 2022-06-22 11:25:51.230811
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # test string
    x = _DeprecatedSequenceConstant('abc', 'msg', '3.0')
    assert len(x) == 3

    # test dict
    x = _DeprecatedSequenceConstant({'a': 'b'}, 'msg', '3.0')
    assert len(x) == 1

    # test list
    x = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', '3.0')
    assert len(x) == 3


# Generated at 2022-06-22 11:26:00.841358
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_INVENTORY_ENABLED', 'test', export=globals())
    assert ANSIBLE_INVENTORY_ENABLED == 'test'


# setup some special config values that need cleanup
HOST_KEY_CHECKING = to_text(HOST_KEY_CHECKING, errors='surrogate_or_strict')
SUDO_EXE = to_text(SUDO_EXE, errors='surrogate_or_strict')
SUDO_FLAGS = to_text(SUDO_FLAGS, errors='surrogate_or_strict')

DEFAULT_CONNECTION_PLUGIN = to_text(DEFAULT_CONNECTION_PLUGIN, errors='surrogate_or_strict')

# FIXME: remove once play_context

# Generated at 2022-06-22 11:26:25.415977
# Unit test for function set_constant
def test_set_constant():
    original_value = DEFAULT_BECOME_PASS
    set_constant('test_one', 'a')
    assert 'a' == test_one
    assert original_value == DEFAULT_BECOME_PASS

    set_constant('test_two', 'b')
    assert 'b' == test_two
    assert 'a' == test_one
    assert original_value == DEFAULT_BECOME_PASS

    # change the global value
    set_constant('DEFAULT_BECOME_PASS', 'c')
    assert 'c' == DEFAULT_BECOME_PASS
    assert 'b' == test_two
    assert 'a' == test_one

# Generated at 2022-06-22 11:26:27.287137
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant((1,2,3), "", "")
    assert len(dsc) == 3


# Generated at 2022-06-22 11:26:35.446900
# Unit test for function set_constant
def test_set_constant():
    localvars = {}
    set_constant('FOO', 'BAR', localvars)
    assert 'FOO' in localvars
    assert localvars['FOO'] == 'BAR'
    set_constant('FOO', 'BAZ', localvars)
    assert localvars['FOO'] == 'BAR'
    set_constant('FOO', 'BAZ', localvars, force=True)
    assert localvars['FOO'] == 'BAZ'

# Generated at 2022-06-22 11:26:41.340110
# Unit test for function set_constant
def test_set_constant():
    test_constant = {}
    test_constant_name = "_CONSTANT_FOR_UNIT_TEST"
    test_constant_value = "This is a contant for unit test"
    set_constant(test_constant_name, test_constant_value, export=test_constant)
    assert test_constant[test_constant_name] == test_constant_value

# Generated at 2022-06-22 11:26:43.356014
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((1, 2, 3), "msg", "version")) == 3

# Generated at 2022-06-22 11:26:55.355655
# Unit test for function set_constant
def test_set_constant():
    global config
    for setting in config.data.get_settings():
        value = setting.value
        set_constant(setting.name, value)
        if setting.name == 'DEFAULT_BECOME_PASS':
            assert vars()[setting.name] is None
        elif setting.name == 'DEFAULT_PASSWORD_CHARS':
            assert vars()[setting.name] == DEFAULT_PASSWORD_CHARS
        elif setting.name == 'DEFAULT_REMOTE_PASS':
            assert vars()[setting.name] is None
        elif setting.name == 'DEFAULT_SUBSET':
            assert vars()[setting.name] is None
        elif setting.name == 'MODULE_REQUIRE_ARGS':
            assert vars()[setting.name] == MODULE_REQUIRE

# Generated at 2022-06-22 11:27:05.217714
# Unit test for function set_constant
def test_set_constant():
    assert set_constant('MY_CONSTANT', 'BAR', dict()) == dict(MY_CONSTANT="BAR")


# Set to true when we're running from a git checkout, false when from an
# Ansible release tarball.
#
# We set this ourselves so that we can detect this in places where we need to
# treat a git version differently than a release tarball version.
#
# See https://github.com/ansible/ansible/issues/6048
#
# We set this after the config is initialized because setup.py reads the config
# and this value needs to be set in the config before setup.py can import from
# this file. This is also why this is a global (so setup.py can access it
# without any extra initialization).
IS_PERSISTENT = False



# Generated at 2022-06-22 11:27:11.038963
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import unittest
    class Test__DeprecatedSequenceConstant(unittest.TestCase):
        def runTest(self):
            value = tuple([1, 2, 3])
            msg = "test"
            version = "1.0"

            test_object = _DeprecatedSequenceConstant(value, msg, version)

            for index in range(len(test_object)):
                assert test_object[index] == value[index]
    unit_test = Test__DeprecatedSequenceConstant()
    unit_test.runTest()

# Generated at 2022-06-22 11:27:17.613362
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import os
    import tempfile

    config_path = os.path.join(tempfile.gettempdir(), 'ansible.cfg')
    with open(config_path, 'w') as f:
        f.write('[defaults]\n')
        f.write('deprecation_warnings = False\n')

    d = _DeprecatedSequenceConstant(value=['test'],
                                    msg="test_msg",
                                    version='2.9')

    os.environ.pop('ANSIBLE_DEPRECATION_WARNINGS', None)
    assert d[0] == 'test'

    os.environ.pop('ANSIBLE_DEPRECATION_WARNINGS', None)
    os.environ['ANSIBLE_DEPRECATION_WARNINGS'] = 'True'
    assert d[0] == 'test'

# Generated at 2022-06-22 11:27:19.953979
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    import pytest
    with pytest.raises(DeprecationWarning):
        len(CONNECTION_PLUGIN_PATH)


# Generated at 2022-06-22 11:27:52.318757
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    ds = _DeprecatedSequenceConstant(value=(1, 3, 2, 4), msg="msg", version="version")
    assert len(ds) == 4

# Generated at 2022-06-22 11:28:01.586767
# Unit test for function set_constant
def test_set_constant():
    os.environ['ANSIBLE_TEST_FOO'] = 'foo'
    set_constant('FOO', 'bar')
    assert FOO == 'bar'
    set_constant('FOO', '{{ ansible_test_foo }}')
    assert FOO == 'foo'
    set_constant('FOO', '{{ ansible_test_foo }}', export={
        'ansible_test_foo': 'not_foo'
        })
    assert FOO == 'not_foo'

# FIXME: remove
# NOTE: for unit tests and when running from a source checkout, this value is always None
if config.config_file:
    CONFIG_FILE = config.config_file

if config.DEFAULT_ROLES_PATH:
    DEFAULT_ROLES_PATH = config.DEFAULT_ROL

# Generated at 2022-06-22 11:28:05.893448
# Unit test for function set_constant
def test_set_constant():
    var = {}
    set_constant('test1', 'test')
    set_constant('test2', 'test2', export=var)
    assert ANSIBLE_PERSISTENT_CONNECT_TIMEOUT == 60
    assert var['test2'] == 'test2'
    assert test1 == 'test'

# Generated at 2022-06-22 11:28:07.436004
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant('abc', 'msg', 'version')) == 3

# Generated at 2022-06-22 11:28:15.846628
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "this is a test"
    s = _DeprecatedSequenceConstant(value=(1, 2, 3), msg = msg, version = "2.9")

    assert len(s) == 3
    assert s[1] == 2

    new_msg = "this is a test_new"
    new_version = "2.9.1"
    s = _DeprecatedSequenceConstant(value=(1, 2, 3), msg = new_msg, version = new_version)
    assert len(s) == 3
    assert s[1] == 2

# Generated at 2022-06-22 11:28:20.596787
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'test deprecated message'
    version = '2.10'
    test_value = ['test']
    test_constant = _DeprecatedSequenceConstant(test_value, msg, version)
    assert len(test_constant) == 1
    assert test_constant[0] == 'test'
    assert test_constant.as_list() == test_value

# Generated at 2022-06-22 11:28:21.643855
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(['x'], 'a', 'b')[0] == 'x'

# Generated at 2022-06-22 11:28:23.982050
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant((1, 2, 3), msg='msg', version='version')
    assert len(sequence) == 3


# Generated at 2022-06-22 11:28:26.429661
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = [1, 2, 3]
    msg = 'This is a deprecated test'
    version = '2.9.4'
    D = _DeprecatedSequenceConstant(value, msg, version)
    assert D[1] == 2

# Generated at 2022-06-22 11:28:30.612688
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([1, 2, 3], 'test msg', '2.10')
    assert isinstance(obj, Sequence)


if __name__ == "__main__":
    test__DeprecatedSequenceConstant()