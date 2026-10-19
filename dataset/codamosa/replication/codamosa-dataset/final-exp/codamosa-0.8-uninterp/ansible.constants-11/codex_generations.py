

# Generated at 2022-06-22 11:19:23.570412
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(list(range(5)), 'test', '2.0')) == 5
    assert len(_DeprecatedSequenceConstant(range(5), 'test', '2.0')) == 5



# Generated at 2022-06-22 11:19:26.035726
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    result = _DeprecatedSequenceConstant(value=[1, 2, 3], msg="test msg", version="1")
    assert len(result) == 3


# Generated at 2022-06-22 11:19:31.108489
# Unit test for function set_constant
def test_set_constant():
    # FIXME: this is not making sure the data structure is correct
    set_constant('TEST_CONSTANT', 'TEST_VALUE', export=vars())
    assert TEST_CONSTANT == 'TEST_VALUE'


# A hack so we can ensure that become is always set when we
# invoke the PlayContext constructor, defaulting to False
MAGIC_VARIABLE_MAPPING['become_set_by_automation'] = ('ansible_become_set_by_automation',)

# Generated at 2022-06-22 11:19:36.235205
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    my_list = ['ice', 'cream']
    expected = ['ice', 'cream']
    actual = _DeprecatedSequenceConstant(value=my_list, msg='foo', version='2.12')
    assert expected == actual, 'Expected list to be returned unchanged'


# Generated at 2022-06-22 11:19:40.605739
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    value = ('a', 'b')
    msg = 'msg'
    version = 'version'

    constant = _DeprecatedSequenceConstant(value, msg, version)

    assert constant[0] == 'a'



# Generated at 2022-06-22 11:19:44.245704
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = _DeprecatedSequenceConstant((1, 2, 3), 'This sequence is deprecated', '2.10')
    assert len(x) == 3
    assert x[0] == 1

# Generated at 2022-06-22 11:19:48.247170
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = "foo"
    version = "bar"
    value = [1, 2, 3]
    seq = _DeprecatedSequenceConstant(value, msg, version)

    assert len(seq) == len(value)


# Generated at 2022-06-22 11:19:52.184426
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([1,2,3], 'Test message', '1.0')
    assert obj[0] == 1
    assert obj[1] == 2
    assert obj[2] == 3
    assert len(obj) == 3

# Generated at 2022-06-22 11:20:04.875277
# Unit test for function set_constant
def test_set_constant():
    # This function is not intended to be invoked, but merely to provide
    # test coverage to the 'set_constant' function above.
    #
    # Because we are not setting the constants globally,
    # we will run this only if being run by nose, rather than a normal invocation.
    #
    if __name__ != "__main__":
        set_constant('HELLO_WORLD', u'This is a test of the emergency broadcast system.')

        assert HELLO_WORLD == u'This is a test of the emergency broadcast system.', 'HELLO_WORLD not set'

        set_constant('HELLO_WORLD', u'This is a test of the emergency broadcast system.', export=globals())


# Generated at 2022-06-22 11:20:07.884364
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_constant = _DeprecatedSequenceConstant((1, 2, 3), "test_constant message", "2.5")
    assert len(test_constant) == 3

# Generated at 2022-06-22 11:20:13.323034
# Unit test for function set_constant
def test_set_constant():
    set_constant('test', True, export={})
    assert vars()['test']



# Generated at 2022-06-22 11:20:23.925747
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # check if the length of defined sequence is equal to length of
    # _DeprecatedSequenceConstant
    assert len(ActionBase._ACTION_CALLABLES) == len(_DeprecatedSequenceConstant(ActionBase._ACTION_CALLABLES, 'ActionBase._ACTION_CALLABLES is deprecated in favor of `ActionBase.get_action_callables()`.', '2.12'))
    # check if the value at index 2 is same for both the defined sequence and
    # _DeprecatedSequenceConstant
    assert ActionBase._ACTION_CALLABLES[2] == _DeprecatedSequenceConstant(ActionBase._ACTION_CALLABLES, 'ActionBase._ACTION_CALLABLES is deprecated in favor of `ActionBase.get_action_callables()`.', '2.12')[2]

# Generated at 2022-06-22 11:20:30.485070
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import mock

    x = _DeprecatedSequenceConstant([1, 2, 3], 'this is a message', '2.0')
    mock_warn = mock.Mock()
    with mock.patch('ansible.module_utils.basic.__warning', mock_warn):
        x[1]
    assert mock_warn.call_count == 1
    assert mock_warn.call_args[0][0] == 'this is a message'



# Generated at 2022-06-22 11:20:37.745709
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'message'
    version = '2.10'
    my_list = [1, 2, 3]
    my_con = _DeprecatedSequenceConstant(my_list, msg, version)
    assert len(my_con) == len(my_list)
    assert my_con[0] == my_list[0]
    assert my_con[1:] == my_list[1:]


# Generated at 2022-06-22 11:20:49.597588
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    '''
    >>> class A:
    ...     def __len__(self):
    ...         return 1
    ...
    >>> aOBJ = A()
    >>> aOBJ.__len__
    <method-wrapper '__len__' of A object at 0x7fefb2be4c88>
    >>> _DeprecatedSequenceConstant(aOBJ, 'this is a warning', '2.9').__len__()
    [DEPRECATED] this is a warning, to be removed in 2.9
    1
    >>> len(_DeprecatedSequenceConstant(aOBJ, 'this is a warning', '2.9'))
    [DEPRECATED] this is a warning, to be removed in 2.9
    1
    '''


# Generated at 2022-06-22 11:20:58.489644
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():

    class _TestSequence(object):
        def __init__(self, _list):
            self._list = _list

        def __len__(self):
            return len(self._list)

        def __getitem__(self, y):
            return self._list[y]

    obj = _DeprecatedSequenceConstant(_list=list(range(10)), msg='THIS IS A TEST', version='3.0')

    # test __len__
    assert len(obj) == len(_TestSequence(list(range(10))))

    # test __getitem__
    for i in range(10):
        assert obj[i] == _TestSequence(list(range(10)))[i]

# Generated at 2022-06-22 11:21:08.904759
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:21:13.346973
# Unit test for function set_constant
def test_set_constant():

    def f(name, value):
        set_constant(name, value, export=globals())

    assert 'ansible_connection' not in globals()
    f('ansible_connection', 'local')
    assert ansible_connection == 'local'

# Generated at 2022-06-22 11:21:23.426121
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    cases = [
        (['a', 'b', 'c'], 'no reason given', 'no time given', 3),
        (['a', 'b', 'c'], '', '', 3),
        (['a', 'b', 'c'], ' ', ' ', 3),
        (['a', 'b', 'c'], ' ', 'no time given', 3),
        (['a', 'b', 'c'], 'no reason given', '', 3),
    ]
    for value, msg, version, want in cases:
        c = _DeprecatedSequenceConstant(value, msg, version)
        got = c.__len__()
        assert got == want

# Generated at 2022-06-22 11:21:27.005060
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = _DeprecatedSequenceConstant(list(range(10)), 'a message', 'a version')
    assert seq[3] == 3
    assert len(seq) == 10
    assert seq[-1] == 9

# Generated at 2022-06-22 11:21:34.216166
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    v = []
    message = 'Test Message'
    version = '2.9'
    d = _DeprecatedSequenceConstant(v, message, version)
    assert(len(d) == len(v))
    for i in range(len(d)):
        assert(d[i] == v[i])


# Generated at 2022-06-22 11:21:42.943769
# Unit test for function set_constant
def test_set_constant():
    assert ALLOWED_INTERNAL_ADDRESSES == ["127.0.0.1", "localhost", "::1", "::ffff:127.0.0.1", "::ffff:0.0.0.1"]
    assert SSH_TRANSFER_METHOD == 'smart'
    assert HOST_KEY_CHECKING == True
    assert MODULE_COMPLEX_ARGS in ('aware', 'safe', 'naive')
    assert MODULE_COMPLEX_ARGS == 'safe'
    assert DEFAULT_UNDEFINED_VAR_BEHAVIOR == ('warn',)
    assert EXECUTABLE == '/usr/bin/python'
    assert ERRORS_FATAL == True
    assert DEFAULT_PRIVATE_KEY_FILE == '/etc/ansible/private_key'
    assert BECOME_ALLOW_

# Generated at 2022-06-22 11:21:45.231661
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    sequence = _DeprecatedSequenceConstant([1, 2, 3], 'test message', 'version 2')
    assert(len(sequence) == 3)

# Generated at 2022-06-22 11:21:49.687486
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    l = [1,2,3]
    ds = _DeprecatedSequenceConstant(l, "not a tuple", u'2.0')
    assert len(ds) == 3
    assert ds[0] == 1
    assert ds[2] == 3

# Generated at 2022-06-22 11:21:55.983840
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Mock(object):
        def __init__(self, value, msg, version):
            self.msg = msg
            self.version = version
            self.value = value

        def deprecated(self, msg, version=None):
            assert self.msg == msg
            assert self.version == version
    original_func = _deprecated
    dummy = _DeprecatedSequenceConstant('foo', 'msg', 'version')
    assert dummy[0] == 'foo'
    try:
        _deprecated = Mock
        _ = dummy[0]
    finally:
        _deprecated = original_func

# Generated at 2022-06-22 11:22:05.195612
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_value = _DeprecatedSequenceConstant(value='test_value', msg='test_msg', version='1.2.3')
    assert isinstance(test_value, string_types)
    assert len(test_value) == 11
    assert test_value[0] == 't'
    assert test_value[1] == 'e'
    assert test_value[2] == 's'
    assert test_value[3] == 't'
    assert test_value[4] == '_'
    assert test_value[5] == 'v'
    assert test_value[6] == 'a'
    assert test_value[7] == 'l'
    assert test_value[8] == 'u'
    assert test_value[9] == 'e'

# FIXME: remove the warnings and the

# Generated at 2022-06-22 11:22:08.123461
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant([1, 2, 3], 'This is a message', '2.10')
    assert len(seq) == 3


# Generated at 2022-06-22 11:22:17.503692
# Unit test for function set_constant
def test_set_constant():
    '''
    Ensure that the set_constant function works as expected.
    '''

    data = {'int': 1000,
            'str_parsed': 'test{{color}}test',
            'str': 'test',
            'incorrect_parsed': '{{color}}{{color',
            'dictionary': {'key': 'value'},
            'list_parsed': '[1,2,3,4,"{{color}}"]',
            'list': [1, 2, 3, 4, 5],
            'bool': True,
            'none': None}

    # Create a test namespace to be populated
    export = {}

    # Populate the test namespace
    for key, value in data.items():
        set_constant(key, value, export=export)

    # Test the namespace to ensure that everything is

# Generated at 2022-06-22 11:22:21.697502
# Unit test for function set_constant
def test_set_constant():

    sett = dict()
    sett['name'] = 'test'
    sett['value'] = 'value'

    set_constant(sett['name'], sett['value'], export=sett)
    assert sett['value'] == 'value'
    assert sett['test'] == 'value'



# Generated at 2022-06-22 11:22:26.476384
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dummy_value = [1, 2]
    dummy_msg = "msg"
    dummy_version = "version"
    dummy_sequence = _DeprecatedSequenceConstant(value=dummy_value, msg=dummy_msg, version=dummy_version)
    assert dummy_sequence.__len__() == len(dummy_value)

# Generated at 2022-06-22 11:22:36.102938
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Test constructor and __len__
    obj = _DeprecatedSequenceConstant([1, 2, 3], 'Message', '2.11')
    assert len(obj) == 3

    # Test __getitem__
    assert obj[0] == 1
    assert obj[2] == 3
    with pytest.raises(IndexError):
        obj[3]

    # Test __iter__
    l = []
    for i in obj:
        l.append(i)
    assert l == [1, 2, 3]

# Generated at 2022-06-22 11:22:47.117830
# Unit test for function set_constant
def test_set_constant():
    assert CONNECTION_LOADER
    assert ACTION_PLUGIN_PATH
    assert DEFAULT_DEBUG
    assert DEFAULT_SUDO
    assert DEFAULT_SUDO_FLAGS
    assert DEFAULT_SUDO_EXE
    assert DEFAULT_SU_EXE
    assert DEFAULT_SU_FLAGS
    assert BECOME
    assert BECOME_USER
    assert BECOME_METHOD
    assert DEFAULT_BECOME_METHOD
    assert DEFAULT_BECOME_ERROR_STRATEGY
    assert DEFAULT_BECOME_ALL
    assert DEFAULT_BECOME_ASK_PASS
    assert DEFAULT_CHARSET
    assert DEFAULT_CUSTOM_VENV
    assert DEFAULT_HOST_KEY_CHECKING
    assert DEFAULT_HOST_KEY_CHECKING


# Generated at 2022-06-22 11:22:51.640341
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant(value=['a'], msg="use 'b' instead", version='4.0')
    assert len(a) == 1
    assert a[0] == 'a'


# Generated at 2022-06-22 11:22:55.183598
# Unit test for function set_constant
def test_set_constant():
    set_constant('test_var', 'var_value', locals())
    assert test_var == 'var_value'
    del test_var

# Generated at 2022-06-22 11:22:59.743677
# Unit test for function set_constant
def test_set_constant():
    '''unit test for function set_constant'''
    assert 'REJECT_EXTS' in globals()
    assert 'localhost' not in globals()
    assert 'DEFAULT_BECOME_PASS' in globals()
    assert 'DEFAULT_PASSWORD_CHARS' in globals()
    assert 'DEFAULT_REMOTE_PASS' in globals()



# Generated at 2022-06-22 11:23:01.753026
# Unit test for function set_constant
def test_set_constant():
    set_constant('test', 'will set')
    assert vars()['test'] == 'will set'

# Generated at 2022-06-22 11:23:07.466154
# Unit test for function set_constant
def test_set_constant():
    from ansible.constants import set_constant
    opt = dict()
    set_constant('test_set_constant', ['test_value'], opt)
    assert opt['test_set_constant'] == ['test_value']
    set_constant('test_set_constant', 'test_value2', opt)
    assert opt['test_set_constant'] == 'test_value2'
    set_constant('test_set_constant', {'test_value3': 'test'}, opt)
    assert opt['test_set_constant'] == {'test_value3': 'test'}
    set_constant('test_set_constant', 'self', opt)
    assert opt['test_set_constant'] == 'self'

# Generated at 2022-06-22 11:23:18.126105
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR', locals())
    assert FOO == 'BAR'
    assert locals()['FOO'] == 'BAR'
    set_constant('FOO', 'BAZ', locals())
    assert FOO == 'BAZ'
    assert locals()['FOO'] == 'BAZ'
    set_constant('FOO', 'BAR', export={'FOO': 'BAZ'})
    assert FOO == 'BAR'
    assert locals()['FOO'] == 'BAZ'
    set_constant('FOO', 'BAZ', export=locals())
    assert FOO == 'BAZ'
    assert locals()['FOO'] == 'BAZ'
    set_constant('FOO', 'BAR')
    assert FOO == 'BAR'
    assert locals

# Generated at 2022-06-22 11:23:21.946545
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('foo', 'foo', export)
    assert export['foo'] == 'foo'

    set_constant('baz', 'baz', export)
    assert export['baz'] == 'baz'


# Generated at 2022-06-22 11:23:25.215349
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant([1, 2, 3], 'test message', '2.5')
    assert len(seq) == len([1, 2, 3])



# Generated at 2022-06-22 11:23:33.315254
# Unit test for function set_constant
def test_set_constant():
    ''' test set_constant '''
    assert set_constant('FOO', 'bar') == {'FOO': 'bar'}

# Generated at 2022-06-22 11:23:42.460652
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    # Make sure that we are deprecating the old configuration variable settings
    # as well as the variable names

    # Define the variable that we are going to deprecate and provide a message
    # and the version in which this variable is going to be removed in

    DEPRECATED_VARS = ['DEPRECATED_VERSION']
    DEPRECATED_MSG = 'We have deprecated this variable'
    DEPRECATED_VERSION = '2.11'

    # Define a list of objects that we are going to append with
    # _DeprecatedSequenceConstant objects
    DEPRECATED_VARS_LIST = []

    # Iterate through the list of deprecated variables and check if the version
    # defined above is present in __version__

# Generated at 2022-06-22 11:23:50.885143
# Unit test for function set_constant
def test_set_constant():
    set_constant('constant_var_name', 'var_value')
    assert constant_var_name == 'var_value'
test_set_constant()

# CONSTANTS FROM SETTINGS - END

VAULT_VERSION_MIN = 1.0
VAULT_VERSION_MAX = 1.0

# NOTE: There are some cases where these settings
# need to be used before the config values are
# initialized, so these cannot be moved above
# the config settings. The ConfigManager will
# be rewritten in the future to make this easier
# to manage.
DEFAULT_MODULE_NAME = 'command'
DEFAULT_MODULE_PATH = None
DEFAULT_SUDO = False
DEFAULT_SUDO_USER = "root"
DEFAULT_SU = False
DEFAULT_SU_USER = "root"
DE

# Generated at 2022-06-22 11:24:03.506119
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class MyPrivateSequenceConstant(_DeprecatedSequenceConstant):
        # This class has a method to test __getitem__ of the base class.
        # its method is invoked at the end of this method.
        def test__getitem__(self):
            self.__getitem__(0)

# Generated at 2022-06-22 11:24:12.409594
# Unit test for function set_constant
def test_set_constant():
    assert len(__version__) > 5  # Must have at least major, minor and fix level
    assert len(ANSIBLE_CALLBACK_WHITELIST) > 1
    assert len(ANSIBLE_CONFIG) > 1
    assert len(ANSIBLE_INVENTORY) > 1
    assert len(ANSIBLE_LIBRARY) > 1
    assert len(ANSIBLE_ROLES_PATH) > 1
    assert len(ANSIBLE_ROLES_PATH) > 1
    assert len(ANSIBLE_ROLES_PATH) > 1
    assert len(ANSIBLE_TEST_PYTHON_INTERPRETER) > 1
    assert len(DEFAULT_HASH_BEHAVIOUR) > 1
    assert len(DEFAULT_HASH_BEHAVIOUR) > 1

# Generated at 2022-06-22 11:24:14.521489
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    o1 = _DeprecatedSequenceConstant(value=['a', 'b', 'c'], msg='test message', version='2.0')
    assert(len(o1) == 3)
    assert('a' in o1)



# Generated at 2022-06-22 11:24:16.562245
# Unit test for function set_constant
def test_set_constant():
    var = {}
    set_constant('name', 'value', var)
    assert var['name'] == 'value'

# Generated at 2022-06-22 11:24:18.336897
# Unit test for function set_constant
def test_set_constant():
    set_constant('TEST_CONST', 'TESTING')
    assert TEST_CONST == 'TESTING'

# Generated at 2022-06-22 11:24:29.202804
# Unit test for function set_constant
def test_set_constant():
    """Tests the set_constant function for specific values."""
    for x in ('ANSIBLE_INVENTORY_PLUGINS', 'ANSIBLE_HOST_KEY_CHECKING'):
        assert(getattr(config.data, x).value == globals()[x])

_MOVED_TO_ACTION = frozenset((
    'check_mode', 'delete_remote_tmp_on_context_failure', 'delete_remote_tmp',
    'force_handlers', 'gather_facts', 'get_checksum', 'loop_control',
    'no_log', 'remote_checksum', 'replay_role_paths', 'role_paths',
    'run_once', 'su', 'sudo', 'sudo_user', 'su_user', 'su_pass', 'vault_password',
))

# Generated at 2022-06-22 11:24:37.844546
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # create a constant
    msg = 'This is a test for deprecated sequence constant'
    version = '2.9'
    x = ('a', 'b', 'c')
    # use constructor to create instance of _DeprecatedSequenceConstant
    y = _DeprecatedSequenceConstant(x, msg, version)
    # check function __len__
    assert len(y) == 3
    # check function __getitem__
    assert y[1] == 'b'

if __name__ == '__main__':
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:24:49.689083
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant([1,'2',3,4], 'This is a test message', '2.0')

# Generated at 2022-06-22 11:24:51.175773
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(list(range(5)), 'msg', '1.2')) == 5

# Generated at 2022-06-22 11:24:57.088448
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_ACTION_SETUP) == len(_ACTION_DEBUG) == len(_ACTION_SET_FACT) == 2
    assert len(_ACTION_ALL_PROPER_INCLUDE_IMPORT_ROLES) == 2
    assert len(_ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS) == 2
    assert len(_ACTION_ALL_INCLUDE_ROLE_TASKS) == 3
    assert len(_ACTION_ALL_INCLUDE_TASKS) == 3
    assert len(_ACTION_FACT_GATHERING) == len(_ACTION_ALL_INCLUDE_TASKS) + len(_ACTION_IMPORT_TASKS) == 4


# Generated at 2022-06-22 11:24:59.913628
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert len(c) == 3

# Generated at 2022-06-22 11:25:04.663610
# Unit test for function set_constant
def test_set_constant():
    test_globals = {}
    set_constant('foo', 'bar', test_globals)
    set_constant('baz', 'qux', test_globals)
    assert test_globals['foo'] == 'bar'
    assert test_globals['baz'] == 'qux'

# Generated at 2022-06-22 11:25:08.866503
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    sequence = ['a', 'b', 'c']
    deprecated_sequence = _DeprecatedSequenceConstant(sequence, 'msg', 'version')

    assert sequence == deprecated_sequence
    assert len(sequence) == len(deprecated_sequence)
    assert sequence[0] == deprecated_sequence[0]


# Generated at 2022-06-22 11:25:11.035715
# Unit test for function set_constant
def test_set_constant():
    set_constant("test", True)
    assert vars()["test"] is True
    del vars()["test"]



# Generated at 2022-06-22 11:25:13.448114
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant([1, 2, 3, 4], 'test', '2.8')
    assert c.__len__() == 4


# Generated at 2022-06-22 11:25:16.522131
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_sequence = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    assert len(test_sequence) == 3


# Generated at 2022-06-22 11:25:18.541947
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'msg', 'version')
    assert len(c) == 3

# Generated at 2022-06-22 11:25:50.788916
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test valid behavior
    seq = _DeprecatedSequenceConstant(value=('test', ), msg='msg', version='version')
    assert seq[0] == 'test'
    # Test exception
    seq = _DeprecatedSequenceConstant(value=(), msg='msg', version='version')
    try:
        seq[0]
        assert False
    except IndexError:
        assert True


# Generated at 2022-06-22 11:25:54.581758
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = _DeprecatedSequenceConstant(value = ('a', 'b', 'c'), msg = "X is deprecated", version = "1.3.0")
    assert len(x) == 3
    assert x[0] + x[2] == 'ac'

# Generated at 2022-06-22 11:26:02.199307
# Unit test for function set_constant
def test_set_constant():
    test_constant = {}
    set_constant('ansible_host', '127.0.0.1', test_constant)
    assert test_constant['ansible_host'] == '127.0.0.1'


# Override constants with env vars
for env_name, config_name in config.ENV_OVERRIDES.items():
    # Since all config values are stored as strings, we need to convert
    # the environment variable to a string
    env_val = str(os.environ.get(env_name))
    if env_val:
        set_constant(config_name, env_val)

# Generated at 2022-06-22 11:26:07.300909
# Unit test for function set_constant
def test_set_constant():
    # Test previous behavior
    set_constant('TEST_CONSTANT', 1)
    assert TEST_CONSTANT == 1
    # Test new behavior
    export = {}
    set_constant('TEST_CONSTANT', 2, export=export)
    assert TEST_CONSTANT == 1  # constant was not set globally
    assert export['TEST_CONSTANT'] == 2  # constant was set in the provided export



# Generated at 2022-06-22 11:26:15.501737
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    class TMPAction(object):
        def __init__(self, name):
            self.name = name

    for action in [TMPAction('foo'), TMPAction('bar'), TMPAction('baz')]:
        dsc = _DeprecatedSequenceConstant(value=[action], msg='msg', version='version')
        assert dsc.__len__() == 1
        assert dsc.__getitem__(0) == action
        assert dsc._msg == 'msg'
        assert dsc._version == 'version'


# class used for testing

# Generated at 2022-06-22 11:26:23.536422
# Unit test for function set_constant
def test_set_constant():
    for name in globals().keys():
        if name not in ['test_set_constant']:
            assert globals()[name] == locals()[name], "Constant '%s' is not set properly" % name

# FIXME: some of these should be configuration options or moved elsewhere

# FIXME: consts should not be in vars()

# Generated at 2022-06-22 11:26:27.021961
# Unit test for function set_constant
def test_set_constant():
    ''' Test set_constant function '''
    test_dict = {}
    set_constant("TEST_CONSTANT", 1, export=test_dict)
    assert test_dict['TEST_CONSTANT'] == 1

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

# Generated at 2022-06-22 11:26:29.370116
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    depseq = _DeprecatedSequenceConstant([0], 'msg', 'version')
    assert depseq[0] == 0

# Generated at 2022-06-22 11:26:34.047697
# Unit test for function set_constant
def test_set_constant():
    test_dict = {}
    set_constant("TEST-CONSTANT", "test-value", export=test_dict)
    assert test_dict['TEST-CONSTANT'] == "test-value"

# Generated at 2022-06-22 11:26:36.388732
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert isinstance(_DeprecatedSequenceConstant(['a', 'b'], 'msg', 'version'), Sequence)

# Generated at 2022-06-22 11:27:44.440040
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    obj = _DeprecatedSequenceConstant([1,2,3], 'this is a warning', '0.0')
    assert len(obj) == 3, "length of obj is equal to 3"
    assert obj[0] == 1, "index of obj is equal to 1"

# Generated at 2022-06-22 11:27:50.053316
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import pytest
    sequence = (1, 2)
    t = _DeprecatedSequenceConstant(sequence, '', '')
    assert t.__getitem__(1) == sequence[1]
    with pytest.raises(IndexError):
        t.__getitem__(-1)
    with pytest.raises(IndexError):
        t.__getitem__(len(sequence))


# Generated at 2022-06-22 11:27:59.805191
# Unit test for function set_constant
def test_set_constant():
    old_ANSIBLE_FORKS = ANSIBLE_FORKS
    if isinstance(ANSIBLE_FORKS, (list, tuple)):
        ANSIBLE_FORKS = ANSIBLE_FORKS[-1]
    set_constant('ANSIBLE_FORKS', 99999999999)
    assert 99999999999 == ANSIBLE_FORKS
    set_constant('ANSIBLE_FORKS', old_ANSIBLE_FORKS)


# Remove magic variables defined in config if necessary
# FIXME: remove once play_context mangling is removed
for var in COMMON_CONNECTION_VARS:
    if var in MAGIC_VARIABLE_MAPPING:
        MAGIC_VARIABLE_MAPPING[var] = (var, )

# special case for ansible_connection as it's not in the config

# Generated at 2022-06-22 11:28:07.638676
# Unit test for function set_constant
def test_set_constant():
    assert ANSIBLE_NOCOWS is config.data.get_config_value('ANSIBLE_NOCOWS')

# Hack for tests to make sure we don't have undefined constants
for plug in DOCUMENTABLE_PLUGINS:
    set_constant(plug.upper() + '_PLUGIN_MIN_VERSION', __version__)
    set_constant(plug.upper() + '_PLUGIN_MAX_VERSION', __version__)

# The list of deprecated constants below is also used by the
# documentation Sphinx extension to detect/warn about usage of them
# a warning will be provided if they are used in a play

# Generated at 2022-06-22 11:28:09.869916
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant((), None, None)

# Generated at 2022-06-22 11:28:15.483558
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant([1, 2, 3], '1, 2, 3', '3.0.0')
    assert constant._value == [1, 2, 3]
    assert constant._msg == '1, 2, 3'
    assert constant._version == '3.0.0'
    assert len(constant) == 3
    assert constant[0] == 1


# Generated at 2022-06-22 11:28:22.657753
# Unit test for function set_constant
def test_set_constant():
    set_constant('ANSIBLE_FOO', 1)
    set_constant('ANSIBLE_BAR', [1, 2, 3])
    set_constant('ANSIBLE_WIBBLE', dict(a=1, b=2, c=3))
    set_constant('ANSIBLE_QUUX', 'hello')

    assert ANSIBLE_FOO == 1
    assert ANSIBLE_BAR == [1, 2, 3]
    assert ANSIBLE_WIBBLE == dict(a=1, b=2, c=3)
    assert ANSIBLE_QUUX == 'hello'

# Generated at 2022-06-22 11:28:28.823294
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    testobj = _DeprecatedSequenceConstant(['test1', 'test2', 'test3'], 'test msg', 'test ver')
    assert isinstance(testobj, _DeprecatedSequenceConstant)
    assert len(testobj) == 3
    assert testobj[0] == 'test1'
    assert testobj[1] == 'test2'
    assert testobj[2] == 'test3'

# Additional constants
DEFAULT_SUDO_PASS = _DeprecatedSequenceConstant(DEFAULT_BECOME_PASS, 'DEFAULT_SUDO_PASS is deprecated in favor of DEFAULT_BECOME_PASS', '2.4')

# Generated at 2022-06-22 11:28:31.281835
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert list(_DeprecatedSequenceConstant(['alpha', 'beta'], 'msg', 'version')) == ['alpha', 'beta']

# Generated at 2022-06-22 11:28:37.904019
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = [1, 2, 3]
    deprecated_sequence_constant = _DeprecatedSequenceConstant(value, 'Message', 'version')
    # test __getitem__
    assert deprecated_sequence_constant[0] == 1

if __name__ == '__main__':
    import os
    import sys
    import unittest
    sys.path.insert(0, os.path.abspath('..'))
    from ansible.module_utils import basic

    test__DeprecatedSequenceConstant___getitem__()