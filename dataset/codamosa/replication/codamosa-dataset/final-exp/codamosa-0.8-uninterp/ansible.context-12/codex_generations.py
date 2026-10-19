

# Generated at 2022-06-12 21:15:09.038571
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import ansible.utils.context_objects as context_objects

    test_values = set(['hello', u'猫', {'a': 1}, [1, 2], (3, 4), True, False, None, 5.5, 56, set([5]), {'a': set([5])},
                       (5, set([5]))])
    for test_value in test_values:
        temp_global_context = context_objects.GlobalCLIArgs.from_options({'test_value': test_value})
        assert cliargs_deferred_get('test_value') == test_value
        assert cliargs_deferred_get('test_value', shallowcopy=True) != test_value
        assert cliargs_deferred_get('test_value', shallowcopy=True) == test_value

    # Should return

# Generated at 2022-06-12 21:15:17.439292
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': 'bar'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo') == 'bar'
    # Check default
    assert cliargs_deferred_get('baz') == None
    assert cliargs_deferred_get('baz', default='default') == 'default'

    # Check shallow copy
    cli_args['foo'] = [1, 2]
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo') is cli_args['foo']
    assert cliargs_deferred_get('foo', shallowcopy=True) == [1, 2]
    assert cliargs_deferred_get('foo', shallowcopy=True) is not cli_args['foo']

# Generated at 2022-06-12 21:15:28.393044
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    # pylint: disable=protected-access, too-few-public-methods
    class TestClass:
        """A class that we can get attributes from"""
        def __init__(self, **kwargs):
            self._value = kwargs

        def __getitem__(self, key):
            return self._value[key]

        def __contains__(self, key):
            return key in self._value

    obj = TestClass(test1=2, test2=[1, 2, 3], test3={'a': 'b'}, test4='c')

    def test_with_default(fake_cliargs):
        """Test getting a value that doesn't exist in the cliargs, but has a default"""

# Generated at 2022-06-12 21:15:37.887506
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible import context
    from ansible.module_utils.six import PY3

    class Context(object):
        cli_args = {'foo': 'bar'}

        def __init__(self, module_name, config, play_context, loader, templar, shared_loader_obj=None, arguments=None, set_type_defaults=True, variable_manager=None):
            pass

    context.CLIARGS = Context
    assert cliargs_deferred_get('foo')() == 'bar'

    context.CLIARGS = None
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='baz')() == 'baz'

    context.CLIARGS = {'foo': 'baz'}
   

# Generated at 2022-06-12 21:15:49.274558
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    enum = ('one', 'two', 'three')
    cli_args = {
        'foo': 'bar',
        'baz': 'qux',
        'lis': [1, 2, 3],
        'tup': (4, 5, 6),
        'dict': {'q': 'as', 'w': 'er'},
        'set': {'t', 'y'},
    }

    expected = {
        'foo': 'bar',
        'baz': 'qux',
        'lis': [1, 2, 3],
        'tup': (4, 5, 6),
        'dict': {'q': 'as', 'w': 'er'},
        'set': {'t', 'y'},
    }

    _init_global_context(cli_args)

# Generated at 2022-06-12 21:16:00.002087
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for function cliargs_deferred_get"""
    # pylint: disable=import-error,redefined-outer-name,unused-import
    import pytest
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.utils.context_objects import CLIArgs

    # Test the unparsed state, value is returned directly, no matter the type
    def foo():
        return 'foo'
    cliargs = CLIArgs(dict(a=foo, b=foo))
    assert cliargs_deferred_get('a')() == foo
    assert cliargs_deferred_get('b')() == foo

    # Test the parsed state
    cliargs.parse()
    assert cliargs_deferred_get('a')() == 'foo'
   

# Generated at 2022-06-12 21:16:11.385969
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test a value that is missing, test default value and then make sure that
    # a deepcopy wasn't performed.
    cli_args = CLIArgs({})
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'
    assert cliargs_deferred_get('foo', default='bar', shallowcopy=True)() == 'bar'

    # Test that a singleton is preserved
    cli_args = CLIArgs({'foo': 'bar'})
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() is cli_args['foo']

# Generated at 2022-06-12 21:16:22.017478
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Test with no default
    CLIARGS = CLIArgs(dict(test=dict(test=42)))
    test_func = cliargs_deferred_get('test')
    assert test_func() == dict(test=42)

    # Test with a default
    test_func = cliargs_deferred_get('other', default=dict(test=42))
    assert test_func() == dict(test=42)

    # Test with a shallowcopy
    # Note: this could probably be simplified if we just got rid of the shallowcopy functionality
    # in the real code
    test_func = cliargs_deferred_get('test', shallowcopy=True)
    assert test_func() == dict(test=42)
    assert test_func() is not CLIARGS.get('test')
    test

# Generated at 2022-06-12 21:16:32.306593
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_value(value):
        key = 'test'
        _init_global_context({key: value})
        func = cliargs_deferred_get(key)
        assert func() == value
        assert func() == func()

    test_value(None)
    test_value(True)
    test_value(False)
    test_value(1)
    test_value('Ansible')
    test_value(['a', 'b', 'c'])
    test_value(('a', 'b', 'c'))
    test_value({'a': 1, 'b': 2, 'c': 3})
    test_value({'a', 'b', 'c'})



# Generated at 2022-06-12 21:16:43.303682
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test default value
    cliargs = CLIArgs({})
    testfunc = cliargs_deferred_get('TESTKEY', 'DEFAULT')
    assert testfunc() == 'DEFAULT'

    # Test value from CLIArgs
    cliargs = CLIArgs({'TESTKEY': 'TESTVALUE'})
    testfunc = cliargs_deferred_get('TESTKEY', 'DEFAULT')
    assert testfunc() == 'TESTVALUE'

    # Test shallowcopy
    testval1 = [1]
    testval2 = [1]
    cliargs = CLIArgs({'TESTKEY': testval1})
    testfunc = cliargs_deferred_get('TESTKEY', 'DEFAULT', shallowcopy=True)
    testval1.append(2)
    assert testval1 == testval2

# Generated at 2022-06-12 21:16:55.621421
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = CLIArgs({'foo': 'bar'})
    foo = cliargs_deferred_get('foo')
    assert foo() == 'bar'
    other_cli_args = CLIArgs({'foo': 'not bar'})
    assert foo() == 'bar'
    CLIARGS.update(other_cli_args)
    assert foo() == 'not bar'
    foos = cliargs_deferred_get('foos', default=('foo', 'bar'))
    assert foos() == ('foo', 'bar')
    CLIARGS['foos'] = ['foo', 'bar', 'not foo']
    assert foos() == ['foo', 'bar', 'not foo']
    other_cli_args = CLIArgs({'foos': ['not foo', 'not bar']})

# Generated at 2022-06-12 21:17:07.058761
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    This is not a full unit test for the function but exercises the parts we use
    in FieldAttribute to make sure the function does what we need it to do.
    """
    class DummyCLIArgs(object):
        def __init__(self, defaults=None):
            self.dict = defaults or {}

        def __contains__(self, key):
            return key in self.dict

        def __getitem__(self, key):
            return self.dict[key]

        def get(self, key, default=None):
            return self.dict.get(key, default)


# Generated at 2022-06-12 21:17:17.459586
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def get_foo(value):
        def inner():
            return value
        return inner

    key = 'foo'
    value = 'bar'
    default = 'baz'
    CLIARGS.data = {'foo': value}

    # Setting it directly, not calling the deferred get  value
    assert cliargs_deferred_get(key, default)() == value

    # Calling the deferred get, but not setting it
    assert cliargs_deferred_get(key, default=default)() == default

    # Setting the value to a deferred get
    CLIARGS.data[key] = get_foo(value)
    assert cliargs_deferred_get(key, default=default)() == value

    # Setting the default to a deferred get
    CLIARGS.data = {}
    assert cliargs_deferred

# Generated at 2022-06-12 21:17:23.336790
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_default_value(deferred, expected):
        assert expected == deferred()
    # Test no default value
    deferred = cliargs_deferred_get('non-existent-key')
    assert_default_value(deferred, None)
    # Test with default value
    default = object()
    deferred = cliargs_deferred_get('non-existent-key', default=default)
    assert_default_value(deferred, default)
    # Test it works with CLIARGS replaced with a different object
    key = 'foo'
    value = 'bar'
    cliargs = {key: value}
    # Test no shallowcopy
    deferred = cliargs_deferred_get(key, shallowcopy=False)
    assert_default_value(deferred, value)
    # Test shallowcopy
    deferred = cl

# Generated at 2022-06-12 21:17:34.009122
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args_dict = {'d': {'e': 5}, 'l': [1, 2, 3], 's': {1, 2, 3}}
    _init_global_context(cli_args_dict)
    assert cliargs_deferred_get('d')() == {'e': 5}
    assert cliargs_deferred_get('l')() == [1, 2, 3]
    assert cliargs_deferred_get('s')() == {1, 2, 3}
    assert cliargs_deferred_get('default')() is None
    assert cliargs_deferred_get('d', shallowcopy=True)() == {'e': 5}
    assert cliargs_deferred_get('l', shallowcopy=True)() == [1, 2, 3]
    assert cliargs

# Generated at 2022-06-12 21:17:43.619094
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = CLIArgs(dict(ANSIBLE_CONFIG='/foo/bar'))
    global CLIARGS
    orig_cliargs = CLIARGS

# Generated at 2022-06-12 21:17:47.539392
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIA = CLIArgs({'test': 'test'})
    deferred = cliargs_deferred_get('test')
    assert deferred() == 'test'
    CLIARGS = CLIA
    assert deferred() == 'test'

# Generated at 2022-06-12 21:17:57.792958
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Test that it causes a syntax error when called directly
    try:
        _init_global_context({})
        cliargs_deferred_get()
    except SyntaxError:
        pass
    else:
        raise AssertionError('Expected cliargs_deferred_get to cause a SyntaxError')

    cliargs_deferred_get = cliargs_deferred_get('connection', default='local')
    assert cliargs_deferred_get() == 'local'

    _init_global_context({'connection': 'smart'})
    assert cliargs_deferred_get() == 'smart'

    # Verify that it doesn't matter if the function is called before or after the
    # context has been set
    CLIARGS = CLIArgs({'connection': 'ssh'})
   

# Generated at 2022-06-12 21:18:00.304044
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import types
    from ansible.module_utils.common.collections import MutableMapping

    assert type(cliargs_deferred_get('nothing-here')) == types.FunctionType


# In Ansible proper, this is called from the CLI code after parsing the args

# Generated at 2022-06-12 21:18:06.170468
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # test with a list
    deferred_get = cliargs_deferred_get('foo', default=[1, 2, 3])
    assert deferred_get() == [1, 2, 3]
    CLIARGS['foo'] = [4, 5, 6]
    assert deferred_get() == [4, 5, 6]

    # test with a dictionary
    deferred_get = cliargs_deferred_get('foo', default={1: 'a', 2: 'b'})
    assert deferred_get() == {1: 'a', 2: 'b'}
    CLIARGS['foo'] = {3: 'c', 4: 'd'}
    assert deferred_get() == {3: 'c', 4: 'd'}

    # test with a string

# Generated at 2022-06-12 21:18:19.495276
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_data = {'1': '2', 3: ['4'], 5: {'6': '7'}}
    CLIARGS.update(test_data)
    get_default = cliargs_deferred_get('99', '100')
    get_key = cliargs_deferred_get('1')
    get_key_seq = cliargs_deferred_get('3')
    get_key_shallow = cliargs_deferred_get('3', shallowcopy=True)
    get_key_mapping = cliargs_deferred_get('5')
    get_key_mapping_shallow = cliargs_deferred_get('5', shallowcopy=True)
    get_key_shallow_mutable = cliargs_deferred_get(5, shallowcopy=True)
   

# Generated at 2022-06-12 21:18:27.923066
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Before CLIARGS have been processed
    assert cliargs_deferred_get('foo') is None
    assert cliargs_deferred_get('foo', 'bar') == 'bar'

    # During CLIARGS processing
    _init_global_context({'foo': 'baz'})
    assert cliargs_deferred_get('foo') == 'baz'
    assert cliargs_deferred_get('foo', 'bar') == 'baz'
    assert cliargs_deferred_get('foo', shallowcopy=True) == 'baz'

    _init_global_context({'foo': ['bar', 'baz']})
    assert cliargs_deferred_get('foo') == ['bar', 'baz']

# Generated at 2022-06-12 21:18:38.784383
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from six import moves
    from ansible.utils.context_objects import CLITestArgs

    cliargs = CLITestArgs({'c': [1, 2, 3], 'd': {'xyz': 12, 'abc': 'foo'}, 'p': 1, 'f': 'def', 'str': 'abc'})
    _init_global_context(cliargs)

    fget = cliargs_deferred_get('c')
    assert fget() == [1, 2, 3]
    assert fget() is not cliargs['c']

    fget = cliargs_deferred_get('d')
    assert fget() == {'xyz': 12, 'abc': 'foo'}
    assert fget() is not cliargs['d']


# Generated at 2022-06-12 21:18:48.393624
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""

    # Make a temporary CLIArgs object to test with
    global CLIARGS
    temp_cli_args = CLIARGS
    class DummyCLIArgs(CLIArgs):
        def __init__(self, data):
            self._data = data
        def __getitem__(self, key):
            return self._data[key]
    CLIARGS = DummyCLIArgs(dict(foo='bar', baz=[1, 2, 3]))

    # Test the inner function before we do our closure thing
    inner = cliargs_deferred_get('baz')
    assert inner() == [1, 2, 3]

    # Test the closure
    closure = inner()
    assert closure() == [1, 2, 3]

    # Change the CLI arguments and

# Generated at 2022-06-12 21:18:55.793687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'foo': 'bar'})

    # This is the real test of the function
    assert 'bar' == cliargs_deferred_get('foo', default='baz')()

    # These are really just tests of the outer cliargs_deferred_get and not the closure
    # implementation
    assert 'baz' == cliargs_deferred_get('baz', default='baz')()
    assert None == cliargs_deferred_get('baz')()



# Generated at 2022-06-12 21:19:03.378128
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({"hello": "world"})
    assert cliargs_deferred_get('hello') == 'world'
    assert cliargs_deferred_get('hello', 'default') == 'world'
    assert cliargs_deferred_get('idontexist', 'default') == 'default'
    assert cliargs_deferred_get('idontexist', 'default', shallowcopy=True) == 'default'
    CLIARGS = CLIArgs({
        "dict": {'a': 1, 'b': 2},
        "list": [1,2,3],
        "set": {1,2,3},
    })
    assert cliargs_deferred_get('dict') == {'a': 1, 'b': 2}
    assert cliargs_deferred_

# Generated at 2022-06-12 21:19:11.637945
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import ansible.utils.display
    display = ansible.utils.display
    assert cliargs_deferred_get('verbosity', None, True) == display.VERBOSITY
    assert cliargs_deferred_get('verbose', False, True) is False
    assert cliargs_deferred_get('something', 'default', True) == 'default'


# This is an import rather than a function call to ensure that the module that imports
# this function has a chance to set the version
CLIARGS.get_deferred('module_version')

# Generated at 2022-06-12 21:19:19.079075
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.context_objects import Context
    from ansible.module_utils.common._collections_compat import MutableMapping

    # this is our "final" state of CLIARGS

# Generated at 2022-06-12 21:19:23.035835
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cli_args = {}
    CLIARGS = CLIArgs(cli_args)
    get_vault_password = cliargs_deferred_get('vault_password')
    cli_args['vault_password'] = 'test_password'
    assert 'test_password' == get_vault_password()

# Generated at 2022-06-12 21:19:30.102255
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that we can get the empty key
    cli_args = {}
    _init_global_context(cli_args)

    f = cliargs_deferred_get('foo')
    assert f() is None

    # Test we can set a key and get it
    cli_args = {'foo': 'bar'}
    _init_global_context(cli_args)
    f = cliargs_deferred_get('foo')
    assert f() == 'bar'

    # Test that we get the default if no value is set
    cli_args = {}
    _init_global_context(cli_args)
    f = cliargs_deferred_get('foo', default='baz')
    assert f() == 'baz'

# Generated at 2022-06-12 21:19:42.285219
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the ``cliargs_deferred_get`` function"""
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    def _ret_type(value):
        if is_sequence(value):
            return type(value[:])
        elif isinstance(value, (Mapping, Set)):
            return type(value.copy())
        return type(value)

    # Boolean Value
    _init_global_context({'verbosity': 1})
    assert CLIARGS['verbosity'] is True
    assert cliargs_deferred_get('verbosity')() is True

    # Sequence Value
    _init_global_context({'check_hosts_file': ['hosts_file']})
    assert CLIAR

# Generated at 2022-06-12 21:19:50.410119
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    try:
        CLIARGS.update(dict(f=1, g=dict(h=3)))
        assert cliargs_deferred_get('f')() == 1
        assert cliargs_deferred_get('g')() == dict(h=3)
        assert cliargs_deferred_get('g', shallowcopy=True)() == dict(h=3)
        assert cliargs_deferred_get('h', default='?')() == '?'
        assert cliargs_deferred_get('h', default='?')() == '?'
    finally:
        CLIARGS = CLIArgs({})

# Generated at 2022-06-12 21:19:58.131833
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # setup and test cliargs_deferred_get with normal defaults
    CLIARGS.update({'host_key_checking': True})
    host_key_checking_getter = cliargs_deferred_get('host_key_checking')
    assert host_key_checking_getter() is True

    # setup and test cliargs_deferred_get with custom defaults
    host_key_checking_getter = cliargs_deferred_get('host_key_checking', 1)
    assert host_key_checking_getter() == 1

    # setup and test cliargs_deferred_get with non-existent key
    another_key = cliargs_deferred_get('non_existent', 1, shallowcopy=True)
    assert another_key() == 1
    another_key_shallow = cliargs_

# Generated at 2022-06-12 21:20:08.887760
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    orig = CLIARGS
    CLIARGS = CLIArgs({'foo': ['bar']})

    # Test with a regular value
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']
    # Test with default value
    assert cliargs_deferred_get('no-such-key', default='baz')() == 'baz'
    assert cliargs_deferred_get('no-such-key', default='baz', shallowcopy=True)() == 'baz'

    # Test shallow copy
    list_from_deferred_get = cliargs_deferred_get('foo', shallowcopy=True)()
    assert list_from_deferred_get == ['bar']


# Generated at 2022-06-12 21:20:18.674725
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    import pytest
    from ansible.utils.context_objects import GlobalCLIArgs

    def test_fixture(mocker):
        _init_global_context(GlobalCLIArgs.from_options({'tty': False, 'v': 2}))
        mocker.patch('ansible.utils.context._cliargs_get', side_effect=cliargs_deferred_get)
        return cliargs_deferred_get

    @pytest.mark.parametrize('key', ['tty', 'v', 'orderless_keys'])
    def test_get_known_key(mocker, key):
        get = test_fixture(mocker)
        assert CLIARGS[key] == get(key)()

    def test_get_unkonwn_key(mocker):
        get = test_

# Generated at 2022-06-12 21:20:29.034734
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest
    from .common import CliArgs
    _init_global_context(CliArgs({'test': 'value',
                                  'test1': ('a', 'b', 'c', 'd'),
                                  'test2': 'abcd',
                                  'test3': [1, 2, 3, 4],
                                  'test4': {'a': 1, 'b': 2}}))
    assert cliargs_deferred_get('test')() == 'value'
    assert cliargs_deferred_get('test1')() == ('a', 'b', 'c', 'd')
    assert cliargs_deferred_get('test2')() == 'abcd'
    assert cliargs_deferred_get('test3')() == [1, 2, 3, 4]
    assert cliargs_

# Generated at 2022-06-12 21:20:36.493378
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the closure over CLIARGS.get with shallow copy functionality"""
    # pylint: disable=unused-variable
    global CLIARGS
    CLIARGS = CLIArgs({'a': [1, 2, 3], 'c': {'d': 1, 'e': 2}})
    assert cliargs_deferred_get('a', default='foo') == [1, 2, 3]
    assert cliargs_deferred_get('b', default='foo') == 'foo'
    # pylint: enable=unused-variable



# Generated at 2022-06-12 21:20:47.030260
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=protected-access
    cli_args = {'inventory': ['/etc/ansible/hosts'],
                'tags': ['pre_run'],
                'noop': True}
    _init_global_context(cli_args)
    assert CLIARGS._dict == cli_args
    assert cliargs_deferred_get('inventory')() == cli_args['inventory']
    assert cliargs_deferred_get('tags')() == cli_args['tags']
    assert cliargs_deferred_get('tags', shallowcopy=True)() == cli_args['tags']
    assert cliargs_deferred_get('noop')() == cli_args['noop']

# Generated at 2022-06-12 21:20:57.407836
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the function returns the default if CLIARGS is empty
    default = object()
    assert cliargs_deferred_get('foo', default=default)() is default
    assert cliargs_deferred_get('foo', default=default, shallowcopy=True)() is default

    # Test the function returns the key value if CLIARGS is set
    key = 'bar'
    value = object()
    assert cliargs_deferred_get(key, default=default)() is value
    assert cliargs_deferred_get(key, default=default, shallowcopy=True)() is value
    CLIARGS[key] = value

    # Test the function returns the  for sequence types
    sequence = [object()]
    assert cliargs_deferred_get('sequence', default=default)() == sequence
    assert cli

# Generated at 2022-06-12 21:21:09.165577
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get() works as expected"""
    class CLIArgsStub(object):
        """A stub of CLIArgs object which fakes the behavior of getting a value from a dict"""
        def __init__(self, dict_value):
            self.dict_value = dict_value

        def get(self, key, default=None):
            if key in self.dict_value:
                return self.dict_value[key]
            return default

    # value is a dict
    global CLIARGS
    assert cliargs_deferred_get('test_key')('test_default')() == 'test_default'
    CLIARGS = CLIArgsStub({'test_key': 'test_value'})
    assert cliargs_deferred_get('test_key')('test_default')()

# Generated at 2022-06-12 21:21:21.958112
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that deferred_get works as expected"""
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})

    # Check that the closure actually works
    dg = cliargs_deferred_get('foo')
    assert dg() == 'bar'

    # Check that shallow copy works as expected
    list_value = [1, 2, 3, 4]
    CLIARGS['foo'] = list_value
    dg = cliargs_deferred_get('foo', shallowcopy=True)
    assert dg() == list_value
    assert dg() is not list_value

    dict_value = {1: 'a', 2: 'b'}
    CLIARGS['foo'] = dict_value
    dg = cliargs_deferred_

# Generated at 2022-06-12 21:21:32.822687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': ['bar'], 'baz': 'wibble'})
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs_deferred_get('baz')() == 'wibble'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']
    assert cliargs_deferred_get('baz', shallowcopy=True)() == 'wibble'
    CLIARGS = CLIArgs({'foo': ['bar']})
    assert cliargs_deferred_get('foo', default=['wibble'])() == ['bar']
    assert cliargs_deferred_get('baz', default=['wibble'])() == ['wibble']
    assert cliargs_deferred

# Generated at 2022-06-12 21:21:39.467123
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # These are used by the parsing code to set the CLIARGS
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'bar': ['baz', 'qux']})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() == ['baz', 'qux']
    assert cliargs_deferred_get('baz')() is None
    assert cliargs_deferred_get('baz', 'blah')() == 'blah'
    assert cliargs_deferred_get('bar', shallowcopy=True)() == ['baz', 'qux']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

# Generated at 2022-06-12 21:21:46.806016
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Module function cliargs_deferred_get"""
    global CLIARGS

    CLIARGS = CLIArgs({'list': [1, 2, 3], 'dict': {'foo': 'bar'}, 'str': 'abc'})
    assert cliargs_deferred_get('list')() == [1, 2, 3]
    assert cliargs_deferred_get('dict')() == {'foo': 'bar'}
    assert cliargs_deferred_get('str')() == 'abc'

    # Test defaulting
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'

    # Test shallow copy

# Generated at 2022-06-12 21:21:57.869058
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('unknown key')() is None
    CLIARGS['key'] = 'value'
    assert cliargs_deferred_get('key')() == 'value'
    assert cliargs_deferred_get('unknown key', default='value')() == 'value'
    assert cliargs_deferred_get('unknown key', default=['value'], shallowcopy=True)() == ['value']
    assert cliargs_deferred_get('unknown key', default=('value',), shallowcopy=True)() == ('value',)
    assert cliargs_deferred_get('unknown key', default={'key': 'value'}, shallowcopy=True)() == {'key': 'value'}

# Generated at 2022-06-12 21:22:09.089632
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unsubscriptable-object
    a = dict(a=1, b='foo', c=[1, 2, 3, 4])
    _init_global_context(a)
    f1 = cliargs_deferred_get('a')
    assert f1() == 1

    f2 = cliargs_deferred_get('b')
    assert f2() == 'foo'

    f3 = cliargs_deferred_get('c')
    assert f3() == [1, 2, 3, 4]
    assert f3() is not a['c']

    # Make sure we're able to return the shallow copies
    f4 = cliargs_deferred_get('c', shallowcopy=True)
    assert f4() == [1, 2, 3, 4]
    assert f4()

# Generated at 2022-06-12 21:22:19.186105
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': {'bar': 'baz', 'qux': 'quux'}, 'quux': ['quuux', 'quuuux']}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo') == {'bar': 'baz', 'qux': 'quux'}
    assert cliargs_deferred_get('foo', shallowcopy=True) == {'bar': 'baz', 'qux': 'quux'}
    assert cliargs_deferred_get('quux') == ['quuux', 'quuuux']
    assert cliargs_deferred_get('quux', shallowcopy=True) == ['quuux', 'quuuux']
    assert cliargs_deferred_get('barf') is None


# Generated at 2022-06-12 21:22:26.985137
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=unused-argument
    global CLIARGS
    CLIARGS = CLIArgs(dict(testarg=dict(foo='spam')))
    assert cliargs_deferred_get('testarg') == dict(foo='spam')
    assert cliargs_deferred_get('testarg') is not cliargs_deferred_get('testarg')
    assert cliargs_deferred_get('testarg', shallowcopy=True) is not cliargs_deferred_get('testarg', shallowcopy=True)
    assert cliargs_deferred_get('testarg', shallowcopy=True) == cliargs_deferred_get('testarg', shallowcopy=True)
    assert cliargs_deferred_get('testarg', SHALLOWcopy=True) is not cliargs_deferred_get

# Generated at 2022-06-12 21:22:38.724950
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    CLIARGS['newkey'] = 'newvalue'
    assert cliargs_deferred_get('newkey')() == 'newvalue'
    assert cliargs_deferred_get('newkey', default='newdefault')() == 'newvalue'
    assert cliargs_deferred_get('notset')() is None
    assert cliargs_deferred_get('notset', default='newdefault')() == 'newdefault'

    cliargs = CLIArgs({'newkey': 'newvalue'})
    cliargs_args = GlobalCLIArgs.from_options(cliargs)
    assert cliargs_args['newkey'] == 'newvalue'
    assert cliargs_args.get('newkey', 'notset') == 'newvalue'

# Generated at 2022-06-12 21:22:47.190538
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._options['option1'] = 'first'
    CLIARGS._options['option2'] = 'second'
    fn1 = cliargs_deferred_get('option1', 'default1')
    fn2 = cliargs_deferred_get('option2', 'default2')
    fn3 = cliargs_deferred_get('option3', 'default3')
    assert fn1() == 'first'
    assert fn2() == 'second'
    assert fn3() == 'default3'
    CLIARGS._options['option4'] = []
    fn4 = cliargs_deferred_get('option4', ['default4'])
    assert fn4() == []
    fn5 = cliargs_deferred_get('option4', [['default5']])
    assert fn5() == []


# Generated at 2022-06-12 21:23:05.549328
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    old_CLIARGS = CLIARGS
    try:
        CLIARGS = CLIArgs({})

        fn = cliargs_deferred_get('key', default=5)
        assert fn() == 5

        CLIARGS = CLIArgs({'key': 'value'})
        assert fn() == 'value'

        fn = cliargs_deferred_get('key2', default=5)
        assert fn() == 5

        CLIARGS = CLIArgs({'key2': 'value'})
        assert fn() == 'value'

        LIARGS = CLIArgs({'key2': 'value'})
        fn = cliargs_deferred_get('key2', default=5)
        assert fn() == 'value'
    finally:
        CLIARGS = old_CLIARGS

# Generated at 2022-06-12 21:23:15.493705
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=redefined-outer-name

    # This is only needed when testing outside of ansible-test
    from ansible.cli import CLI

    test_cli_args = ['ansible-playbook', '--extra-vars', '{"a": 1, "b": 2}']
    parser = CLI.base_parser(connect_opts=True, meta_opts=True, runas_opts=True, subset_opts=True, check_opts=True, runtask_opts=True, vault_opts=True)
    options, args = parser.parse_args(test_cli_args)
    _init_global_context(options)

    assert cliargs_deferred_get('extra_vars')['a'] == 1

# Generated at 2022-06-12 21:23:25.024603
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    global CLIARGS
    CLIARGS = GlobalCLIArgs()

# Generated at 2022-06-12 21:23:34.175706
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert CLIARGS == CLIArgs({})

    CLIARGS = GlobalCLIArgs(dict(foo=42, bar=dict(a='hello')))

    assert cliargs_deferred_get('foo')() == 42
    assert cliargs_deferred_get('bar')() == dict(a='hello')
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 42
    assert cliargs_deferred_get('bar', shallowcopy=True)() == dict(a='hello')

    CLIARGS = GlobalCLIArgs(dict(foo='monkey', bar=dict(a=['hello'], b=[1, 2, 3])))

    assert cliargs_deferred_get('foo')() == 'monkey'
    assert cliargs_deferred_get('bar')

# Generated at 2022-06-12 21:23:44.227080
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    expected_results = {
        'a': 1,
        'b': [1, 2, 3],
        'c': {'a': 1, 'b': 2},
        'd': set([1, 2, 3])
    }
    import copy
    test_results = {}
    for key in expected_results:
        test_results[key] = cliargs_deferred_get(key, shallowcopy=True)()

    CLIARGS.from_options(expected_results)

    # Test the normal return value
    for key in expected_results:
        assert test_results[key] is expected_results[key]

    # Test the shallowcopy
    for key in expected_results:
        if is_sequence(expected_results[key]):
            assert test

# Generated at 2022-06-12 21:23:51.515825
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('inventories')().__name__ == 'list'
    assert cliargs_deferred_get('inventories', shallowcopy=True)().__name__ == 'list'
    assert cliargs_deferred_get('inventories', default=set)().__name__ == 'set'
    assert cliargs_deferred_get('inventories', default=set, shallowcopy=True)().__name__ == 'set'
    assert cliargs_deferred_get('inventories', default={})().__class__.__name__ == 'dict'
    assert cliargs_deferred_get('inventories', default={}, shallowcopy=True)().__class__.__name__ == 'dict'

# Generated at 2022-06-12 21:24:02.770280
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Ensure that the deferred getter works as expected"""
    global CLIARGS
    # Test with a side effect of CLIARGS being replaced
    CLIARGS = CLIArgs({})
    # Test that it returns the default if not set
    default = 'hello world'
    get_default = cliargs_deferred_get('some_key', default=default)
    assert get_default() == default

    # Test that it returns the original value for basic data types
    for value in (True, 2, 2.5, 'hello world'):
        CLIARGS = CLIArgs({'some_key': value})
        get_value = cliargs_deferred_get('some_key')
        assert get_value() == value

    # Test that it returns a copy for containers
    for value in ([], (), set(), {}):
        CLIAR

# Generated at 2022-06-12 21:24:03.929531
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('foo', False)()

# Generated at 2022-06-12 21:24:15.548929
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from copy import copy, deepcopy
    from unittest import TestCase

    class TestContextObjects(TestCase):
        def test_cliargs_deferred_get(self):
            CLIARGS = GlobalCLIArgs({'test': 'testvalue'})

# Generated at 2022-06-12 21:24:27.209478
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    @pytest.fixture
    def fake_cliargs():
        return CLIArgs(dict(
            a=1, b=2, c=[3, 4], d={'one': 1, 'two': 2},
            e=set(('three', 'four'))
        ))

    @pytest.fixture
    def patch_cliargs(monkeypatch, fake_cliargs):
        monkeypatch.setattr('ansible.utils.context_objects.CLIARGS', fake_cliargs)

    with patch_cliargs:
        cliargs_default = cliargs_deferred_get('a', 10)
        assert cliargs_default() == 1

        cliargs_default = cliargs_deferred_get('b', 11)
        assert cliargs_default() == 2

        cli

# Generated at 2022-06-12 21:24:57.002607
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import nose.tools

    cliargs = CLIArgs({'foo': 123, 'bar': 'xyz'})
    getter = cliargs_deferred_get('foo')
    nose.tools.assert_equal(getter(), 123)
    nose.tools.assert_equal(getter(), 123)
    getter = cliargs_deferred_get('bar')
    nose.tools.assert_equal(getter(), 'xyz')
    nose.tools.assert_equal(getter(), 'xyz')
    getter = cliargs_deferred_get('froz')
    nose.tools.assert_is(getter(), None)
    getter = cliargs_deferred_get('froz', default='qux')
    nose.tools.assert_equal(getter(), 'qux')

    cl