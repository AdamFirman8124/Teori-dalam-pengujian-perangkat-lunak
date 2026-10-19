

# Generated at 2022-06-22 11:19:22.150798
# Unit test for function set_constant
def test_set_constant():
    '''
    This is redefined here so it's not subject to
    the config.manager's
    '''
    v = {'foo': 'bar'}
    set_constant('foo', 'baz', v)
    assert v['foo'] == 'baz', 'set_constant did not set'

# Generated at 2022-06-22 11:19:25.251466
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant(['a', 'b'], 'msg', '2.0')
    assert len(seq) == 2


# Generated at 2022-06-22 11:19:32.551452
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    tuple_value = ('a', 'b', 'c')
    obj = _DeprecatedSequenceConstant(tuple_value, 'msg', 'version')
    # test individual index
    assert obj.__getitem__(0) == tuple_value[0]
    assert obj.__getitem__(1) == tuple_value[1]
    assert obj.__getitem__(2) == tuple_value[2]
    # test slice

# Generated at 2022-06-22 11:19:36.912183
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    list_1 = ['a', 'b', 'c']
    dsc_1 = _DeprecatedSequenceConstant(list_1, '', '9999')

    assert dsc_1[0] == 'a'


# Generated at 2022-06-22 11:19:45.074560
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([1, 2, 3], msg='msg', version='version')
    assert _DeprecatedSequenceConstant([1, 2, 3], msg='msg', version='version') == [1, 2, 3]
    assert len(_DeprecatedSequenceConstant([1, 2, 3], msg='msg', version='version')) == 3
    assert _DeprecatedSequenceConstant([1, 2, 3], msg='msg', version='version')[1] == 2

# Generated at 2022-06-22 11:19:49.258197
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test operation if index is within range
    v = _DeprecatedSequenceConstant([1, 2], '', '')
    assert v[0] == 1
    # Test operation if index is out of range
    v = _DeprecatedSequenceConstant([1], '', '')
    assert v[1] == None

# Generated at 2022-06-22 11:20:01.689941
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    class Mock(object):
        def __init__(self, name, **kwargs):
            self._name = name

        def deprecated(self, msg, **kwargs):
            print("%s: %s" % (self._name, msg))

    display = Mock("display")

    msgs = ["Hello, World!", "What did you expect?"]
    test_cases = [("Hello, World!", 0), ("What did you expect?", 1)]

    def pytest_funcarg__ds(request):
        return _DeprecatedSequenceConstant(("Hello, World!", "What did you expect?"), msg, version)

    version = '2.0'
    msg = "Hello, World!"
    ds = _DeprecatedSequenceConstant(("Hello, World!", "What did you expect?"), msg, version)


# Generated at 2022-06-22 11:20:05.175319
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    x = _DeprecatedSequenceConstant([1, 2, 3], "foo", "Bar")
    assert x[0] == 1
    assert x[1] == 2
    assert x[2] == 3



# Generated at 2022-06-22 11:20:07.145712
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR')
    assert FOO == 'BAR'

# Generated at 2022-06-22 11:20:10.873109
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    expected_length = 2
    actual_length = len(_DeprecatedSequenceConstant([1, 2], '', ''))
    assert expected_length == actual_length


# Generated at 2022-06-22 11:20:17.528770
# Unit test for function set_constant
def test_set_constant():
    # For each setting in the config
    for setting in config.data.get_settings():
        assert setting.name in vars()

# Generated at 2022-06-22 11:20:18.954513
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant(None, '', '')

# Generated at 2022-06-22 11:20:22.452443
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.module_utils.common.collections import Sequence
    assert len(_DeprecatedSequenceConstant([1, 2], "Test", "1.0")) == 2


# Generated at 2022-06-22 11:20:31.261842
# Unit test for function set_constant
def test_set_constant():
    assert an_int == 1
    assert a_bool is True
    assert a_dict['foo'] == 'bar'
    assert a_list[1] == 'c'
    assert a_string == 'asd'
    assert not a_none_value

if __version__ < '2.4':
    # Deprecated constants
    set_constant('_DEPRECATED_SHOW_SOME_SNIPPETS', _DeprecatedSequenceConstant(_DEPRECATED_SHOW_SOME_SNIPPETS,
                                                                               '`_DEPRECATED_SHOW_SOME_SNIPPETS`', '2.4'))

# Generated at 2022-06-22 11:20:37.952130
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a deprecated sequence constant"
    version = "2.9"
    value = ["test"]
    deprecated = _DeprecatedSequenceConstant(value, msg, version)
    assert isinstance(deprecated, Sequence)
    assert deprecated._value == value
    assert deprecated._msg == msg
    assert deprecated._version == version
    assert len(deprecated) == 1
    assert deprecated[0] == "test"

# Generated at 2022-06-22 11:20:41.832251
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'dummy_msg', 'dummy_version')
    assert len(dsc) == 3


# Generated at 2022-06-22 11:20:45.269630
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = _DeprecatedSequenceConstant(('foo', 'bar'), msg='test', version='2.8')
    assert 2 == len(seq)


# Generated at 2022-06-22 11:20:46.136635
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR', export=vars())
    assert FOO == 'BAR'

# Generated at 2022-06-22 11:20:49.491783
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'test msg'
    version = 'test version'
    test_list = [1, 2, 3]
    _DeprecatedSequenceConstant(test_list, msg, version)[1]
    assert 1

# Generated at 2022-06-22 11:20:53.837121
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    _DeprecatedSequenceConstant(value=[1, 2, 3], msg='msg', version='version')
    assert len(_DeprecatedSequenceConstant(value=[1, 2, 3], msg='msg', version='version')) == 3


# Generated at 2022-06-22 11:21:04.524720
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'test message', '2.8')
    assert constant[1] == 2

DOCUMENTABLE_PLUGINS.sort()

for constant in LOCALHOST, BOOL_TRUE, CONFIGURABLE_PLUGINS, DOCUMENTABLE_PLUGINS, COLLECTION_PTYPE_COMPAT:
    # Make immutable
    set_constant(constant.__name__, constant)

# Generated at 2022-06-22 11:21:09.513298
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    """Unit test to ensure the deprecated sequence constant returns the expected length."""

    # Create a sequence constant object and return the length of the object
    test_seq = _DeprecatedSequenceConstant(value=('Hello', 'World'), msg='test_msg', version='test_version')
    length = len(test_seq)

    # Assert that the length is equal to what we expect
    assert length == 2


# Generated at 2022-06-22 11:21:11.944742
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = _DeprecatedSequenceConstant([1, 2, 3], '', '')[1]
    assert value == 2

# Generated at 2022-06-22 11:21:20.489445
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    value = (1, 2, 'three')
    msg = 'This is a test'
    version = '2.0'
    test_obj = _DeprecatedSequenceConstant(value, msg, version)
    assert test_obj._value == value
    assert test_obj._msg == msg
    assert test_obj._version == version
    assert len(test_obj) == len(value)
    for i in range(len(value)):
        assert test_obj[i] == value[i]


# Generated at 2022-06-22 11:21:31.623990
# Unit test for function set_constant
def test_set_constant():
    local_var = {}
    set_constant('new_var', 'value', local_var)
    assert local_var['new_var'] == 'value'


# DEPRECATED SETTINGS FROM CONFIG, OR FROM CONSTANT VALUES
# Deprecated constants are converted to the new style and
# translated to the new setting using MAGIC_VARIABLE_MAPPING

# Generated at 2022-06-22 11:21:33.774584
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    s = _DeprecatedSequenceConstant('list', 'test msg', 'version')

test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:21:37.043852
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(tuple(), '', '')) == 0
    assert len(_DeprecatedSequenceConstant((1, 2, 3), '', '')) == 3


# Generated at 2022-06-22 11:21:47.089256
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Create mock __init__
    class MockDeprecatedSequenceConstant:
        def __init__(self, value, msg, version):
            self._value = value
            self._msg = msg
            self._version = version

    # Create mock class
    class Mock:
        def __init__(self):
            self.instance = MockDeprecatedSequenceConstant(1, 'a', 'b')

        def warn(self, msg):
            # Mock method
            pass

    mock = Mock()

    _DeprecatedSequenceConstant.__getitem__(mock.instance, 'd')
    _DeprecatedSequenceConstant.__len__(mock.instance)


# Generated at 2022-06-22 11:21:58.081527
# Unit test for function set_constant
def test_set_constant():
    # Return a dict of all constants in global scope
    constants = dict((k, v) for k, v in globals().items() if k.upper() == k)
    # Set new const
    set_constant('TEST_SET_CONSTANT', 'foo')
    assert constants['TEST_SET_CONSTANT'] == 'foo'
    # No-op for existing constant
    set_constant('VERSION', '1.2.3')
    assert constants['VERSION'] == __version__
    # Set new const in custom scope
    set_constant('TEST_SET_CONSTANT', 'bar', export=vars(constants))
    assert constants['TEST_SET_CONSTANT'] == 'foo'
    assert 'TEST_SET_CONSTANT' not in locals()

# Generated at 2022-06-22 11:22:02.415898
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    ''' Verify the method __getitem__ of _DeprecatedSequenceConstant
    '''
    # Initialize _DeprecatedSequenceConstant
    dep_con = _DeprecatedSequenceConstant((1,2,3), 'test warning', '2.0')
    actual = dep_con.__getitem__(0)
    expected = 1
    assert actual == expected

# Generated at 2022-06-22 11:22:18.682850
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # _DeprecatedSequenceConstant should have __getitem__ method
    _DeprecatedSequenceConstant([1, 2, 3], 'msg', '2.9').__getitem__(1)
    _DeprecatedSequenceConstant([1, 2, 3], 'msg', '2.9')[1]

    # _DeprecatedSequenceConstant should emit a deprecation warning
    try:
        from ansible.utils.display import Display
        import warnings

        display = Display()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            _DeprecatedSequenceConstant([1, 2, 3], 'msg', '2.9')[1]
            assert w[0].category == DeprecationWarning
    except ImportError:
        pass  # don't use the display class

# Generated at 2022-06-22 11:22:28.722082
# Unit test for function set_constant
def test_set_constant():
    set_constant('FOO', 'BAR', export=globals())
    assert FOO == 'BAR'
    # Test that we can't overwrite a constant
    try:
        set_constant('FOO', 'BAZ', export=globals())
    except Exception as e:
        pass
    else:
        assert False, 'Should have failed to reassign constant'
    # Test that the original constant was not overwritten
    assert FOO == 'BAR'

# Add constants for deprecated keys
set_constant('HOST_KEY_CHECKING_DEPRECATED', (config.get_config_value('HOST_KEY_CHECKING'), config.get_config_value('DEPRECATED_HOST_KEY_CHECKING')))

# Generated at 2022-06-22 11:22:31.074137
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant((1, 2, 3), 'not a real message', '99.99.99')) == 3


# Generated at 2022-06-22 11:22:40.497239
# Unit test for function set_constant
def test_set_constant():
    assert 'DEFAULT_VAULT_ID_MATCH' == DEFAULT_VAULT_ID_MATCH
    assert 'DEFAULT_VAULT_PASSWORD_FILE' == DEFAULT_VAULT_PASSWORD_FILE
    assert 'DEFAULT_FORKS' == DEFAULT_FORKS
    assert '.vault_pass' == VAULT_PASSWORD_ENV_VAR
    assert 3 == DEFAULT_DEPRECATION_WARNINGS
    assert 'vault_password_file' == VAULT_PASSWORD_ENV_VAR_NAME

    assert EXECUTABLE_JSON != "executable_json"
    assert 'DEFAULT_ROLES_PATH' == DEFAULT_ROLES_PATH
    assert ['vars', 'defaults'] == DEFAULT_HASH_BEHAVIOUR

# Generated at 2022-06-22 11:22:42.223346
# Unit test for function set_constant
def test_set_constant():
    constants = {}
    set_constant('constant_test', 'foo', constants)
    assert constants['constant_test'] == 'foo'

# Generated at 2022-06-22 11:22:45.382023
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert _DeprecatedSequenceConstant([], "msg", "version").__len__() == 0
    assert _DeprecatedSequenceConstant(["a"], "msg", "version").__len__() == 1

# Generated at 2022-06-22 11:22:52.736769
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from units.mock.loader import DictDataLoader
    ldr = DictDataLoader({})
    assert len(_DeprecatedSequenceConstant([], 'test', '999.9')) == 0
    assert len(_DeprecatedSequenceConstant((), 'test', '999.9')) == 0
    assert len(_DeprecatedSequenceConstant(ldr.get_basedir(), 'test', '999.9')) == len(ldr.get_basedir())


# Generated at 2022-06-22 11:22:56.598325
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant(value=(1, 2, 3), msg='test msg', version='2.6')
    assert len(a) == 3
    assert a[1] == 2


# Generated at 2022-06-22 11:23:00.909093
# Unit test for function set_constant
def test_set_constant():
    import sys

    module = type(sys)('__main__')

    set_constant('FOO', 'bar')
    assert FOO == 'bar'

    set_constant('FOO', 'bar', export=module.__dict__)
    assert module.FOO == 'bar'

# Generated at 2022-06-22 11:23:04.817915
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    foo = _DeprecatedSequenceConstant(value=['foo', 'bar'], msg="Heyo!", version="2.9")
    assert foo[0] == 'foo'
    assert foo[1] == 'bar'



# Generated at 2022-06-22 11:23:19.789770
# Unit test for function set_constant
def test_set_constant():
    assert DEFAULT_BECOME_PASS is None
    assert COLOR_CODES['yellow'] == u'0;33'

# Generated at 2022-06-22 11:23:25.215744
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant_test = _DeprecatedSequenceConstant(
        ['a', 'b', 'c'],
        'some_message',
        '2.11'
    )
    assert len(constant_test) == 3
    assert constant_test[0] == 'a'
    assert constant_test[1] == 'b'
    assert constant_test[2] == 'c'

# Generated at 2022-06-22 11:23:30.375167
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq = [1, 2, 3]
    msg = "Sequence constant is deprecated."
    ver = "2.9"
    const = _DeprecatedSequenceConstant(value=seq, msg=msg, version=ver)
    assert const.__getitem__(0) == seq[0]



# Generated at 2022-06-22 11:23:33.315068
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant(('a', 'b', 'c'), 'msg', 'version')[1] == 'b'


# Generated at 2022-06-22 11:23:36.237048
# Unit test for function set_constant
def test_set_constant():
    set_constant('ABC', 'test')
    assert ABC == 'test'
    assert ABC == 'test'


# Backwards compatible constants for things that were previously global variables
# These should be considered deprecated, and should not be used in new code

# Generated at 2022-06-22 11:23:38.719765
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    n = _DeprecatedSequenceConstant(['a', 'b'], 'msg', 'version')
    assert n[0] == n[1] == 'a'
    assert n[-1] == 'b'


# Generated at 2022-06-22 11:23:41.036787
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert [1, 2, 3][0] == _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')[0]

# Generated at 2022-06-22 11:23:42.306194
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    two_element_list = _DeprecatedSequenceConstant([1, 2], 'msg', 'version')
    assert len(two_element_list) == 2
    assert two_element_list[1] == 2

# Generated at 2022-06-22 11:23:50.781854
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    """This is a unit test for the method __len__ of class _DeprecatedSequenceConstant"""
    import os
    import sys
    import doctest

    # The following is to make sure that we are running this unit test from the directory
    # where the script is located.
    # If this variable is True, run the test only if the variable RUN_UNIT_TEST is set as
    # an environment variable and the variable is set to 'True'
    # if this variable is False, run the test
    # This variable is set to True only by the unit test module.
    RUN_UNIT_TEST_ONLY_IF_SET_ENVIRONMENT_VARIABLE = True
    if RUN_UNIT_TEST_ONLY_IF_SET_ENVIRONMENT_VARIABLE:
        run_only_if_

# Generated at 2022-06-22 11:24:03.441401
# Unit test for function set_constant
def test_set_constant():
    ''' Test if setting constants is working '''

    try:
        from ansible.utils.display import Display
        from ansible.playbook.play_context import PlayContext
    except Exception as e:
        # Not all plugins need this, we don't care
        # to test if set_constant works or not in
        # those cases
        return

    from ast import literal_eval

    display = Display()
    play_context = PlayContext()
    magic_variable_dictionary = dict()

    set_constant('VERSION', 'A.B.C.D')
    assert VERSION == 'A.B.C.D'

    set_constant('REJECT_EXTS', 'a.b.c.d')
    assert literal_eval(REJECT_EXTS) == ('a.b.c.d',)

    set

# Generated at 2022-06-22 11:24:40.755863
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # We expect no exception for following code.
    _DeprecatedSequenceConstant([], "Hello", "World")

# The following deprecated variables are for backwards compatibility for variables that have moved to config.
# TODO: remove after 2.10.
# FIXME: we have no good way to auto-find variables in the above set_constants call that are not in default_config.yml
# FIXME: instead, we will manually update this list when anything is removed

# FIXME: this is a flag that can only be removed when we make all the above config variables dynamic.
#        Note that this is required when some variables are changed at runtime
_config_is_dynamic = False


# Generated at 2022-06-22 11:24:43.423740
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a_deprecated_list = _DeprecatedSequenceConstant([1, 2, 3], 'test', '2.0')
    assert len(a_deprecated_list) == 3

# Generated at 2022-06-22 11:24:50.013111
# Unit test for function set_constant
def test_set_constant():
    assert set_constant('FOO', 'bar') == {'FOO': 'bar'}
    assert set_constant('FOO', 'baz', dict(FOO='bar')) == {'FOO': 'baz'}
    assert 'FOO' not in globals()


# UNIT TESTING? # FIXME: make this a noop in unit tests, somehow?
_warning('\'config_file\' is assigned but never used')

# Generated at 2022-06-22 11:24:52.541393
# Unit test for function set_constant
def test_set_constant():
    out = {}
    set_constant('foo', 'bar', export=out)
    assert out['foo'] == 'bar'


# Generated at 2022-06-22 11:24:55.637266
# Unit test for function set_constant
def test_set_constant():
    test_constant = {}
    set_constant('test', 42, test_constant)
    assert test_constant['test'] == 42


# Generated at 2022-06-22 11:24:57.778966
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant([], '', '')) == 0
    assert len(_DeprecatedSequenceConstant([1, 2], '', '')) == 2


# Generated at 2022-06-22 11:25:03.518426
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ['foo', 'bar']
    msg = 'test'
    version = '1.0'
    c = _DeprecatedSequenceConstant(value, msg, version)
    assert len(c) == 2
    assert c[0] == 'foo'
    assert c[1] == 'bar'


# Generated at 2022-06-22 11:25:06.556802
# Unit test for function set_constant
def test_set_constant():
    __testing_constant_list__ = {}
    set_constant('test', 'testvalue', export=__testing_constant_list__)
    assert __testing_constant_list__['test'] == 'testvalue'

# Generated at 2022-06-22 11:25:12.916519
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    my_list = [1, 2, 3]
    _msg = "Test message"
    _version = "1.8.0"
    my_object = _DeprecatedSequenceConstant(my_list, _msg, _version)
    my_object[1]
    assert len(my_object) == 3
    assert _msg in str(my_object)
    assert _version in str(my_object)
    assert str(my_object) is not ''

# Generate deprecated constants and warnings

# Generated at 2022-06-22 11:25:18.863632
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    pattern = r'^ \[DEPRECATED\] This is a test for method __len__ of class _DeprecatedSequenceConstant, to be removed in 2.0\n$'
    dsc = _DeprecatedSequenceConstant([1, 2, 3], 'This is a test for method __len__ of class _DeprecatedSequenceConstant', '2.0')
    assert re.match(pattern, dsc.__len__())


# Generated at 2022-06-22 11:26:34.383584
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dc = _DeprecatedSequenceConstant([], 'msg', 'version')
    dc[0]


# Generated at 2022-06-22 11:26:36.207984
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert foo == 'bar'

# Generated at 2022-06-22 11:26:46.630898
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    from ansible.module_utils.common.collections import Sequence
    old_version = '2.5'
    dep_seq_const = _DeprecatedSequenceConstant('test_const', 'deprecated_msg', old_version)
    assert dep_seq_const[0] == 't'
    assert dep_seq_const[1] == 'e'
    assert dep_seq_const[2] == 's'
    assert dep_seq_const[3] == 't'
    assert dep_seq_const[-1] == 't'
    assert dep_seq_const[-2] == 's'
    assert dep_seq_const[-3] == 'e'
    assert dep_seq_const[-4] == 't'
    assert dep_seq_const[2:4] == 'st'
   

# Generated at 2022-06-22 11:26:52.723613
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    listtest = _DeprecatedSequenceConstant(['foo', 'bar'], 'testmsg', 'testver')

    assert(listtest[0] == 'foo')
    assert(listtest[1] == 'bar')
    assert(len(listtest) == 2)
    assert('foo' in listtest)

# Generated at 2022-06-22 11:27:03.303408
# Unit test for function set_constant
def test_set_constant():
    test_data = {
        'test_str': 'foo',
        'test_bool': True,
        'test_int': 10,
        'test_list': ['foo', 'bar'],
        'test_dict': {'key': 'value'},
    }
    export = {}
    for name, value in test_data.items():
        set_constant(name, value, export)
        assert export[name] == value


# Backwards compat
DEFAULT_BECOME_EXE = BECOME_EXE  # TODO: remove me in 2.10
DEFAULT_BECOME_METHOD = BECOME_METHOD  # TODO: remove me in 2.10
DEFAULT_BECOME_USER = BECOME_USER  # TODO: remove me in 2.10
DEFAULT_SUDO

# Generated at 2022-06-22 11:27:06.675384
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    from ansible.module_utils.common.text.converters import to_list
    v = _DeprecatedSequenceConstant(to_list('abc'), 'bad', '1.0')
    assert len(v) == 3


# Generated at 2022-06-22 11:27:10.490201
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(['foo', 'bar'], "", "2.10")) == 2
    assert len(_DeprecatedSequenceConstant([], "", "2.10")) == 0

# Generated at 2022-06-22 11:27:13.028516
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    a = _DeprecatedSequenceConstant(('a', ), 'msg', '1.0.0')
    assert len(a) == 1
    assert a[0] == 'a'



# Generated at 2022-06-22 11:27:17.248390
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant([1,2,3,4], "msg", "version")
    b = len(a)
    assert(b == 4)

# Generated at 2022-06-22 11:27:19.638912
# Unit test for function set_constant
def test_set_constant():
    set_constant("test_constant", True)
    import __main__
    assert __main__.test_constant == True

