

# Generated at 2022-06-12 21:15:07.523627
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CliArgs
    cli_args = CliArgs({})

    # Test default value, shallow copy, and deep copy
    cli_args.set('default_value', [1, 2])
    cli_args.set('shallow_value', [1, 2])
    cli_args.set('deep_value', [1, 2])
    default_function = cliargs_deferred_get('default_value')
    shallow_function = cliargs_deferred_get('shallow_value', shallowcopy=True)
    deep_function = cliargs_deferred_get('deep_value')
    assert default_function() == [1, 2]
    assert shallow_function() == [1, 2]
    assert deep_function() == [1, 2]

    #

# Generated at 2022-06-12 21:15:13.214895
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # First ensure that the function can call get on the inner object and get a value from
    # the object
    CLIARGS = CLIArgs({'foo': 'bar'})
    getter = cliargs_deferred_get('foo', default='baz')
    assert getter() == 'bar'

    # Now ensure it will look up the default if the requested key isn't there
    CLIARGS = CLIArgs({'other': 'foobar'})
    assert getter() == 'baz'

    # Test that shallow copies of dicts and lists get returned on shallowcopy=True
    CLIARGS = CLIArgs({'list': [1, 2, 3], 'dict': {'x': 'y', 'z': 'a'}})

# Generated at 2022-06-12 21:15:20.362629
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class global_mock_object(object):
        def __init__(self):
            self.args = {}

    _GLOBAL_MOCK_OBJECT = global_mock_object()

    def mock_global(name):
        if name == "CLIARGS":
            return _GLOBAL_MOCK_OBJECT.args
        raise ImportError("Don't use this")

    old_global = globals()["global"]
    globals()["global"] = mock_global

    # Test with shallow copy
    _GLOBAL_MOCK_OBJECT.args["testlist"] = ["This is a list"]
    testlist = cliargs_deferred_get("testlist", shallowcopy=True)
    assert _GLOBAL_MOCK_OBJECT.args["testlist"] is not testlist()
    assert _

# Generated at 2022-06-12 21:15:26.845136
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    inner = cliargs_deferred_get('foo')
    assert inner() is None

    inner = cliargs_deferred_get('foo', 'bar')
    assert inner() == 'bar'
    CLIARGS['foo'] = 'baz'
    assert inner() == 'baz'


# TODO: make this a Singleton (aka Borg) (aka a class with all functions/attributes bound to the class)

# TODO: current inventory
# TODO: current configuration
# TODO: current verbosity

# Generated at 2022-06-12 21:15:37.149937
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'a': 'A', 'b': [1, 2], 'c': {'a': 1, 'b': 2}}
    _init_global_context(cli_args)
    default_val = object()

    # Not found, use default
    assert cliargs_deferred_get('d')() is default_val

    # Found, but returns the same object
    assert cliargs_deferred_get('b')(default=default_val) is cliargs_deferred_get('b')(default=default_val)

    # Found, shallow copy is correct
    assert id(cliargs_deferred_get('b', shallowcopy=True)()) != id(cliargs_deferred_get('b', shallowcopy=True)())

# Generated at 2022-06-12 21:15:48.524941
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # CliArgs == {} returns a default value
    def assert_default(default, expected):
        CLIARGS = CLIArgs({})  # Clear out the global context
        assert cliargs_deferred_get('foo', default)(), expected

    assert_default(None, None)
    assert_default(1, 1)

    CLIARGS = CLIArgs({})  # Clear out the global context
    assert cliargs_deferred_get('verbosity', default=None, shallowcopy=True)() == None

    # CliArgs with a value returns that value
    def assert_value(value, expected, shallowcopy=False):
        CLIARGS = CLIArgs({'foo': value})  # Clear out the global context

# Generated at 2022-06-12 21:15:59.400748
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    # pylint: disable=too-few-public-methods
    class Options(object):
        def __init__(self):
            self.foo = 'foo'
            self.baz = 'baz'

    # Test with CLIARGS being unbound
    assert cliargs_deferred_get('foo')(None) is None
    assert cliargs_deferred_get('baz')(None) is None

    # Test with CLIARGS being set with default
    CLIARGS.update(Options())
    assert cliargs_deferred_get('foo')(None) == 'foo'
    assert cliargs_deferred_get('baz')(None) == 'baz'

    # Test with CLIARGS being set with custom value
    CLIAR

# Generated at 2022-06-12 21:16:05.219297
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    old_args = {}
    # Test simple key retrieval
    assert cliargs_deferred_get('foo')(), None
    CLIARGS['foo'] = 1
    assert cliargs_deferred_get('foo')(), 1
    del CLIARGS['foo']
    # Test with default value
    assert cliargs_deferred_get('foo', default=2)(), 2
    CLIARGS['foo'] = 1
    assert cliargs_deferred_get('foo', default=2)(), 1
    del CLIARGS['foo']
    # Test shallow copy
    test_list = [1, 2, 3]
    CLIARGS['foo'] = test_list
    assert cliargs_deferred_get('foo', shallowcopy=True)() is not test_list
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:16:16.217551
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=redefined-outer-name, unused-variable
    import copy
    import doctest

    global CLIARGS
    CLIARGS = CLIArgs({'to_copy': 'original'})

    results = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert results.failed == 0
    assert results.attempted == 5
    do_copy = cliargs_deferred_get('to_copy', shallowcopy=True)
    assert do_copy() == 'original'
    do_copy_default = cliargs_deferred_get('to_copy_default', shallowcopy=True)
    assert do_copy_default() == 'default'
    do_copy_none = cliargs_deferred_get('to_copy_none', shallowcopy=True)
    assert do_

# Generated at 2022-06-12 21:16:25.448612
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    global CLIARGS
    # cliargs_deferred_get()
    #
    # If no cli arguments have been parsed
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('test')(key='test', default='spam') == 'spam'
    assert cliargs_deferred_get('test')(key='test') is None
    #
    # If cli arguments has been parsed
    CLIARGS = CLIArgs({'test': 'ham'})
    assert cliargs_deferred_get('test')(key='test', default='spam') == 'ham'
    assert cliargs_deferred_get('test')(key='test') == 'ham'
    #
    #

# Generated at 2022-06-12 21:16:42.617633
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo':'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz')() == None
    assert cliargs_deferred_get('baz', default='qux')() == 'qux'

# FIXME: We cannot reach these from the unit tests
#        - are they used at all?
#def context_consume(key, value):
#    '''Be sure to remove the key from the context after you are done with it'''
#    CLIARGS.consume(key, value)
#
#def context_consume_items(mapping):
#    '''Be sure to remove the key from the context after you are done with it'''
#    CLIARGS

# Generated at 2022-06-12 21:16:53.421868
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.config.manager import ConfigManager, UnfilteredConfigParser
    cliargs = {
        # NOTE: Don't use cli args that are tied to particular configuration
        # files in this test case as it will change the test results depending
        # on what configs are available in the test environment.
        'list': ['one', 'two', 'three'],
        'dict': {'a': 42, 'b': 'foo', 'c': ['x', 'y', 'z']},
        'empty': ()
    }
    _init_global_context(cliargs)
    assert cliargs_deferred_get('list')() == ['one', 'two', 'three']

# Generated at 2022-06-12 21:17:05.004124
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    global CLIARGS
    cli_args = {}

    _init_global_context(cli_args)
    assert (cliargs_deferred_get('foo', default='bar')() == CLIARGS['foo'])

    cli_args['foo'] = 'baz'
    _init_global_context(cli_args)
    assert (cliargs_deferred_get('foo', default='bar')() == CLIARGS['foo'])

    cli_args['foo'] = []
    _init_global_context(cli_args)
    assert (cliargs_deferred_get('foo', default='bar', shallowcopy=True)() == CLIARGS['foo'])
    cli_args['foo'].append('baz')

# Generated at 2022-06-12 21:17:15.551066
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS['a'] = 42
    CLIARGS['b'] = [1, 2, 3]
    CLIARGS['c'] = {'a': 42, 'b': 'the universe', 'c': [1, 2, 3]}
    CLIARGS['d'] = set([1, 2, 3])

    assert CLIARGS.get('a') == 42
    assert CLIARGS.get('b') == [1, 2, 3]
    assert CLIARGS.get('c') == {'a': 42, 'b': 'the universe', 'c': [1, 2, 3]}
    assert CLIARGS.get('d') == set([1, 2, 3])

    assert cliargs_deferred_get('a')() == 42

# Generated at 2022-06-12 21:17:20.883537
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliarg_deferred_get"""
    _init_global_context({'verbosity': 2, 'check': True, 'listhosts': True})

    assert cliargs_deferred_get('verbosity') == 2
    assert cliargs_deferred_get('check')

    # Cannot directly test that the cliargs is copied as we don't want to localize the global
    # cliargs and the cliargs is a namedtuple
    assert isinstance(cliargs_deferred_get('listhosts', shallowcopy=True), bool)

# Generated at 2022-06-12 21:17:32.141022
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.context_objects import CliArgs
    global CLIARGS

    test_dict = {'foo': 'bar', 'blip': 'blop'}
    test_list = ['foo', 'bar', 'blip']
    test_set = {'foo', 'bar', 'blip'}
    test_immutable_dict = ImmutableDict([('foo', 'bar'), ('blip', 'blop')])

    test_options = CliArgs(test_dict)

    CLIARGS = test_options

    test_default = cliargs_deferred_get('bar')
    assert test_default is None
    test_default = cliargs_deferred

# Generated at 2022-06-12 21:17:42.311338
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    original_CLIARGS = CLIARGS
    CLIARGS = CLIArgs({'a': [1, 2, 3], 'b': {'c': 'd'}, 'c': 'string'})

    # This should return a copy of the list
    result = cliargs_deferred_get('a', shallowcopy=True)()
    assert result == [1, 2, 3], result

    # This should return the original dict
    result = cliargs_deferred_get('b', shallowcopy=True)()
    assert result == {'c': 'd'}, result

    # This should return a copy of the set
    result = cliargs_deferred_get('c', shallowcopy=True)()
    assert result == 'string', result

    CLIARGS = original_CLIARGS

# Generated at 2022-06-12 21:17:52.731418
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # Create an empty object and then later replace it with a GlobalCLIArgs object
    class foo:
        pass
    testing_cliargs = foo
    testing_cliargs.allow_world_readable_tmpfiles = True

    # Create a GlobalCLIArgs objects
    _init_global_context(testing_cliargs)
    assert CLIARGS.allow_world_readable_tmpfiles is True

    # Test that the function returns the value provided by the GlobalCLIArgs object
    f = cliargs_deferred_get("allow_world_readable_tmpfiles")
    assert f() is True

    # Test that the function returns the default value when no such value is set in the
    #   GlobalCLIArgs object

# Generated at 2022-06-12 21:18:02.106777
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    orig = {'a': [1, 2], 'b': {'c': 1}, 'd': '1', 'e': {'c': 1}, 'f': '1'}
    global CLIARGS
    CLIARGS = CLIArgs(orig)

    # exists
    assert cliargs_deferred_get('a') == orig['a']
    assert cliargs_deferred_get('b') == orig['b']
    assert cliargs_deferred_get('d') == orig['d']
    assert cliargs_deferred_get('e') == orig['e']
    assert cliargs_deferred_get('f') == orig['f']
    # doesn't exist
    assert cliargs_deferred_get('x') is None
    # exists and shallowcopy
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:18:06.196721
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    expected_value = {'a': {'b': 'c'}}
    expected_shallowcopy = expected_value.copy()
    from ansible.utils.context_objects import CLIArgs
    _init_global_context(CLIArgs({}))
    assert CLIARGS == CLIArgs({})
    assert cliargs_deferred_get('key', default=expected_value)() == expected_value
    assert cliargs_deferred_get('key', default=expected_value, shallowcopy=True)() == expected_shallowcopy

# Generated at 2022-06-12 21:18:22.191865
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import types

    class Dummy(object):
        """Dummy class to test the closure of cliargs_deferred_get"""
        cliargs_deferred_get = cliargs_deferred_get

    def wrapper_function(func, *args, **kwargs):
        return func

    def func():
        return wrapper_function(cliargs_deferred_get, key='bar', shallowcopy=True)

    foo = Dummy()
    func = types.MethodType(func, foo)
    first_result = func()

    # Not sure how to test that this is a closure correctly

    outer_env = func.__globals__
    inner_env = first_result.__closure__[0].cell_contents

    assert inner_env['key'] == 'bar'

# Generated at 2022-06-12 21:18:32.627118
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def local_default():
        return 'Local default'
    # pylint: disable=global-statement
    global CLIARGS
    CLIARGS = CLIArgs({'a': 'foo'})
    value = cliargs_deferred_get('a')()
    assert value == 'foo'
    # Test value with no default, get None
    value = cliargs_deferred_get('b')()
    assert value is None
    # Test value with default
    value = cliargs_deferred_get('b', default='bar')()
    assert value == 'bar'
    # Test value with default func
    value = cliargs_deferred_get('b', default=local_default)()
    assert value == 'Local default'
    # Test value for shallow copy

# Generated at 2022-06-12 21:18:43.060204
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get function
    """

    from ansible.module_utils.common._collections_compat import (MutableSequence, MutableMapping, MutableSet)

    class Test:
        def __init__(self, name, shallowcopy):
            self._shallowcopy = shallowcopy
            self.name = name

        def __call__(self):
            if self._shallowcopy:
                return (self.name, 'shallow')
            else:
                return (self.name, 'deep')

    # Test dict
    dict_value = {'foo': 'bar'}
    cliargs_deferred_get('dict', default=dict_value, shallowcopy=False)().pop('foo') == 'bar'

# Generated at 2022-06-12 21:18:50.193490
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = 'bar'
    deferred_get = cliargs_deferred_get('foo')
    assert 'bar' == deferred_get()
    CLIARGS['foo'] = 'baz'
    assert 'baz' == deferred_get()

    CLIARGS['bar'] = ['foo', 'bar']
    deferred_get = cliargs_deferred_get('bar', shallowcopy=True)
    assert deferred_get() == ['foo', 'bar']
    CLIARGS['bar'].append('baz')
    assert deferred_get() == ['foo', 'bar', 'baz']

    CLIARGS['baz'] = {'baz': 'foo'}
    deferred_get = cliargs_deferred_get('baz', shallowcopy=True)

# Generated at 2022-06-12 21:19:01.012023
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class cliargs_deferred_getTester():
        def test_get_default(self):
            def test_func():
                return
            assert cliargs_deferred_get('key', default=test_func)() is test_func

            assert cliargs_deferred_get('key', default='foo')() == 'foo'

            assert cliargs_deferred_get('key', default='foo', shallowcopy=True)() == 'foo'

            assert cliargs_deferred_get('key', default=set(['foo']))() == set(['foo'])

            assert cliargs_deferred_get('key', default=set(['foo']), shallowcopy=True)() == set(['foo'])

        def test_get_set(self):
            global CLIARGS

            CLIARGS = Global

# Generated at 2022-06-12 21:19:08.375142
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # ensure that the global context is initialized
    global CLIARGS
    CLIARGS = CLIArgs(dict(one=1, two=2))
    assert cliargs_deferred_get('one')() == 1
    # test shallowcopy = true
    assert cliargs_deferred_get('two', shallowcopy=True)() == 2
    assert cliargs_deferred_get('two', shallowcopy=False)() == 2
    # test fallback to default
    assert cliargs_deferred_get('three', default=3)() == 3

# Generated at 2022-06-12 21:19:17.502444
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeArgs(object):
        pass
    args = FakeArgs()
    args.force_color = True
    args.verbosity = 3
    args.host_key_checking = False
    args.listhosts = False

    _init_global_context(args)
    assert cliargs_deferred_get('force_color')() is True
    assert cliargs_deferred_get('verbosity')() == 3
    assert cliargs_deferred_get('host_key_checking')() is False
    assert cliargs_deferred_get('listhosts')() is False
    assert cliargs_deferred_get('not_there')() is None
    assert cliargs_deferred_get('not_there', default=['default'])() == ['default']

# Generated at 2022-06-12 21:19:26.353086
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test function is a closure over getting a key from CLIARGS
    global CLIARGS
    # Try setting value of a key and make sure it is returned
    CLIARGS.update({'test_key': 'test_value'})
    assert cliargs_deferred_get('test_key')() == 'test_value'
    # Try getting value of a key that is not set and make sure default is returned
    assert cliargs_deferred_get('test_key_not_set', default='default_value')() == 'default_value'
    # Test shallowcopy functionality
    # Test list
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == ['test_value']
    # Test dict

# Generated at 2022-06-12 21:19:32.265851
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that the cliargs_deferred_get closure works"""
    # pylint: disable=unused-variable, protected-access
    # This is a test function that's imported by unit tests.  Don't disable any of it

    # Gather up the current CLIARGS for later
    fake_args = CLIARGS
    empty_args = CLIArgs({})

    # Start by testing the basic functionality
    value = 'foo'
    inner = cliargs_deferred_get('foo', default=value)
    CLIARGS.__dict__.clear()
    assert inner() is value

    # Now test that we get the right value when the key is the default
    value = 'foo'
    inner = cliargs_deferred_get('foo', default=value)
    CLIARGS.__dict__.clear()
    CLI

# Generated at 2022-06-12 21:19:42.098547
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = {'foo': 'bar', 'baz': ['baz1', 'baz2']}

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz')() == ['baz1', 'baz2']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('baz', shallowcopy=True)() == ['baz1', 'baz2']

    # When ``default`` argument is provided, ``Item.get()`` is used.
    assert cliargs_deferred_get('xyz', default={'xyz': 'xyz'})() == {'xyz': 'xyz'}
    assert cliargs

# Generated at 2022-06-12 21:19:56.855375
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get(key='foo')() is None
    assert cliargs_deferred_get(key='foo', default=True)() is True
    # Py2/3 compat for these tests
    CLIARGS._data['foo'] = True
    assert cliargs_deferred_get(key='foo', shallowcopy=True)() is True
    assert cliargs_deferred_get(key='foo', shallowcopy=True)() is True
    CLIARGS._data['foo'] = {'answer': 42, 'question': 'life'}
    assert cliargs_deferred_get(key='foo', shallowcopy=True)() == {'answer': 42, 'question': 'life'}

# Generated at 2022-06-12 21:20:00.118847
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.setdefault('MAKE_IT_SO', 'Number 1')
    assert cliargs_deferred_get('MAKE_IT_SO', default='Nope')() == 'Number 1'
    assert cliargs_deferred_get('MAKE_IT_SO_NOT', default='Yup')() == 'Yup'

# Generated at 2022-06-12 21:20:09.856268
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for ``cliargs_deferred_get``"""
    import ansible.utils.context_objects
    from ansible.module_utils.six import u
    from ansible.module_utils.six import PY3

    ansible.utils.context_objects.CLIARGS = dict(
        ansible_module_mock=u('foo'),
        ansible_module_mock_list=[u('foo'), u('bar'), u('baz'),],
        ansible_module_mock_dict={u('foo'): u('bar'), u('baz'): u('qux'),},
    )

    if PY3:
        # Python 3 does not have a cmp parameter for assertDictEqual
        def cmp_dict_equal(dict1, dict2):
            return dict1 == dict2
   

# Generated at 2022-06-12 21:20:19.503068
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    class CliArgs(Mapping):
        def get(self, key, default=None):
            if key == 'shallow_list':
                return ['a']
            elif key == 'shallow_dict':
                return {'a': 1}
            elif key == 'shallow_set':
                return set('a')
            elif key == 'deep_list':
                return [{'a': 1}]
            elif key == 'deep_dict':
                return {'a': [1]}

        def __getitem__(self, key):
            return getattr(self, key)

    CLIARGS = CliArgs()
    # Test shallow copy for each type
    for key in ('shallow_list', 'shallow_dict', 'shallow_set'):
        default = cli

# Generated at 2022-06-12 21:20:29.421268
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {
        'test_dict': {'test_key': 'test_value'},
        'test_seq': ['test_value1', 'test_value2'],
        'test_set': {'test_value1', 'test_value2'},
    }

    _init_global_context(cli_args)

    assert cliargs_deferred_get('not_in_cli_args', default='default_not_in_cli_args') == 'default_not_in_cli_args'
    assert cliargs_deferred_get('not_in_cli_args') == None

    assert cliargs_deferred_get('test_dict') == {'test_key': 'test_value'}
    assert cliargs_deferred_get('test_dict', shallowcopy=True)

# Generated at 2022-06-12 21:20:39.537791
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Our target function
    from ansible.utils.context_objects import cliargs_deferred_get

    # We need to mock out the functions that should have been called from the previous
    # invocation of this function to set up the GlobalCLIArgs
    from ansible.utils.context_objects import CLIARGS
    def _reset_command_line_args():
        global CLIARGS
        CLIARGS = CLIArgs({})

    # We are going to replace the functions that should have been called in the previous
    # invocation of this function
    from ansible.module_utils._text import to_native
    import copy
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.context_objects import GlobalCLIArgs, CLIArgs


# Generated at 2022-06-12 21:20:44.703112
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=global-variable-not-assigned,global-statement
    global CLIARGS

    CLIARGS = CLIArgs({})

    assert cliargs_deferred_get('foo')() is None

    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'

    assert cliargs_deferred_get('foo', default='baz')() == 'bar'

    assert cliargs_deferred_get('bar', default='baz')() == 'baz'

    CLIARGS['foo'] = ['bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']

    CLIARGS['foo'] = set(['bar'])

# Generated at 2022-06-12 21:20:47.704641
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options(dict(foo=1, bar=2, baz=[1, 2, 3]))
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 1
    assert cliargs_deferred_get('bar')() == 2
    assert cliargs_deferred_get('baz')() == [1, 2, 3]
    assert cliargs_deferred_get('baz', shallowcopy=True)() == [1, 2, 3]

# Generated at 2022-06-12 21:20:57.934906
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test for function cliargs_deferred_get"""
    cli_args = dict(
        test_default_top_level=None,
        test_default_delegated=None,
        test_value_top_level=42,
        test_value_delegated=dict(
            inner1=44,
            inner2=49,
            inners=dict(
                inner21=52,
            ),
        ),
        test_default_none=None,
    )
    _init_global_context(cli_args)

    test_default_top_level = cliargs_deferred_get('test_default_top_level')
    test_default_delegated = cliargs_deferred_get('test_default_delegated', default=dict(inner22=52))
    test_default

# Generated at 2022-06-12 21:21:09.227838
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    from ansible.module_utils.common.collections import list_of_strings

    def good_values(value, default, copy=False):
        c = CLIArgs(copy)
        assert value == cliargs_deferred_get(value, default=default)(), "value==%s, type==%s" % (repr(value), type(value))

    # Test simple values
    good_values('string', 'string', True)
    good_values(1, 1, True)
    good_values(1.0, 1.0, True)
    good_values([], [], True)
    good_values({}, {}, True)
    good_values([1, 'string', 1.0], [1, 'string', 1.0], True)
    good

# Generated at 2022-06-12 21:21:22.709650
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz')() is None
    assert cliargs_deferred_get('baz', default='foo')() == 'foo'
    assert cliargs_deferred_get('baz', default='foo', shallowcopy=True)() == 'foo'
    # We don't support direct setting of types other than sequences, Mappings, and Sets
    # But since Mappings and Sets aren't actually overridden by the base class, we'll
    # test that we handle them here.  We'll also throw in sequences in case we get lazy
    # and change the shallowcopy default to True
    seq = tuple('abc')
    assert cliargs

# Generated at 2022-06-12 21:21:33.314978
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'bar': ['baz', 'qux'], 'baz': {'quux': 'quuz'},
                       'qux': {'corge', 'grault'}})

    assert cliargs_deferred_get('foo')().value == 'bar'
    assert cliargs_deferred_get('foo', default='quux')().value == 'bar'
    assert cliargs_deferred_get('quux', default='quuz')().value == 'quuz'
    assert cliargs_deferred_get('bar')().value == ['baz', 'qux']
    assert cliargs_deferred_get('bar', shallowcopy=True)().value == ['baz', 'qux']
    assert cli

# Generated at 2022-06-12 21:21:43.770353
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    In the tests, we want to make sure that we can set the new ``CLIARGS``
    and it won't affect calls to cliargs_deferred_get.  This is important
    because we are going to be replacing ``CLIARGS`` with a singleton as
    part of the ansible run.
    """
    mydict = {'a': 1}
    mylist = [1, 2]
    myset = set(['a', 'b'])
    mystr = 'hello'

    assert cliargs_deferred_get('a', default=mystr)() == mystr
    assert cliargs_deferred_get('a', default=mylist)() == mylist
    assert cliargs_deferred_get('a', default=mydict)() == mydict
    assert cliargs_def

# Generated at 2022-06-12 21:21:48.462004
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')(), 'bar'
    assert cliargs_deferred_get('baz')(), None
    assert cliargs_deferred_get('baz', 'one')(), 'one'

# Generated at 2022-06-12 21:21:59.096476
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Defer getting from CLIARGS until it's set.
    # get_dg returns a function that when called is the same as CLIARGS.get()
    get_dg = cliargs_deferred_get('foo', default='bar')
    assert callable(get_dg)

    # CLIARGS is not yet set
    with pytest.raises(RuntimeError):
        CLIARGS.get('fail', default='bar')

    # but the function we created continues to work
    assert get_dg() == 'bar'

    # Use the function we created to set the value
    CLIARGS = CLIArgs({'foo': 'qux'})
    assert CLIARGS.get('foo', default='bar') == 'qux'
    assert get_dg() == 'qux'

# Generated at 2022-06-12 21:22:10.280721
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'plugin_list': ['action']})
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    default = AnsibleUnsafeText(u'\u789a')
    # Case: CLIARGS has the key and we are using the default
    assert cliargs_deferred_get('plugin_list') == ['action']
    # Case: CLIARGS does not have the key and we are using the default
    assert cliargs_deferred_get('plugin_path', ['action']) == ['action']
    # Case: CLIARGS does not have the key and we are using the default with a shallowcopy
    assert cliargs_deferred_get('plugin_path', ['action'], shallowcopy=True) == ['action']
    # Case: CLIARGS does

# Generated at 2022-06-12 21:22:20.361698
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS = CLIArgs({'test_key': ['1', '2']})
    assert cliargs_deferred_get('test_key')() == ['1', '2']
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == ['1', '2']
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == ['1', '2']
    assert cliargs_deferred_get('test_key', default={'1': '2'}, shallowcopy=True)() == {'1': '2'}
    assert cliargs_deferred_get('test_key', default={'1': '2'}, shallowcopy=True)() == {'1': '2'}

# Generated at 2022-06-12 21:22:27.507780
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Note: CLIArgs is not a singleton so we can do this in a test
    from ansible.module_utils._text import to_bytes, to_text
    mycliargs = CLIArgs({"LIST": [1, 2, 3, 4], "DICT": {"a": 1}, "SET": {1, 2, 3, 4}})
    def test_list():
        return cliargs_deferred_get("LIST")
    def test_dict():
        return cliargs_deferred_get("DICT")
    def test_set():
        return cliargs_deferred_get("SET")
    def test_list_shallow():
        return cliargs_deferred_get("LIST", shallowcopy=True)

# Generated at 2022-06-12 21:22:39.250232
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests to validate cliargs_deferred_get function

    Run as part of the unit tests

    :arg verbose: Passed verbatim to pytest.main
    :arg verbose: Passed verbatim to pytest.main
    """
    import ansible.module_utils.common.context as context
    import pytest
    context._init_global_context({})
    context.CLIARGS.set('foo', 'bar')
    assert context.cliargs_deferred_get('foo')() == 'bar'
    context.CLIARGS.set('foo', [1, 2, 3])
    assert context.cliargs_deferred_get('foo')() == [1, 2, 3]
    assert context.cliargs_deferred_get('foo', shallowcopy=True)() == [1, 2, 3]

# Generated at 2022-06-12 21:22:47.445602
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import tempfile
    import shutil
    _tempdir = tempfile.mkdtemp()

# Generated at 2022-06-12 21:23:07.757473
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    dct = {'foo': 'bar', 'baz': 'qux'}
    s = Set(['a', 'b'])
    m = Mapping([('a', 'b'), ('c', 'd')])
    tests = [
        ('list', ['a', 'b', 'c'], ['a', 'b', 'c']),
        ('tuple',  ('a', 'b', 'c'), ('a', 'b', 'c')),
        ('dict', dict(a=1, b=2), dict(a=1, b=2)),
        ('set', s, s.copy()),
        ('mapping', m, m.copy()),
        ('int', 1, 1),
        ('float', 1.0, 1.0),
        ('str', 'a', 'a'),
    ]

# Generated at 2022-06-12 21:23:16.841597
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = dict(foo="foo", bar=123, baz=[1, 2, 3], frob=set(["a", "b", "c"]))
    _init_global_context(cli_args)
    assert CLIARGS["foo"] == "foo"
    assert CLIARGS["bar"] == 123
    assert CLIARGS["baz"] == [1, 2, 3]
    assert CLIARGS["frob"] == set(["a", "b", "c"])
    func = cliargs_deferred_get('foo')
    assert func() == "foo"
    func = cliargs_deferred_get('bar')
    assert func() == 123
    func = cliargs_deferred_get('baz', shallowcopy=True)
    assert func() == [1, 2, 3]


# Generated at 2022-06-12 21:23:26.200790
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function ``cliargs_deferred_get``"""
    # pylint: disable=redefined-outer-name
    cliargs = CLIArgs({'foo': [], 'bar': {}, 'baz': {'biz': 'baz'}})
    global CLIARGS
    CLIARGS = cliargs
    assert cliargs_deferred_get('foo')() == []
    assert cliargs_deferred_get('bar')() == {}
    assert cliargs_deferred_get('baz')() == {'biz': 'baz'}

    # Now test that we get shallow copies back
    assert cliargs_deferred_get('foo', shallowcopy=True)() == []
    assert cliargs_deferred_get('bar', shallowcopy=True)() == {}
    assert cli

# Generated at 2022-06-12 21:23:36.249954
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for the deferred_get() function"""

    # Currently takes cliargs as its init method
    test_cliargs = {'foo': 'bar', 'baz': [1, 2, 3], 'lists': [1, 2, 3], 'dicts': {'a': 1, 'b': 2}}
    global CLIARGS
    CLIARGS = CLIArgs(test_cliargs)
    fn = cliargs_deferred_get('foo', 'zug')
    assert fn() == 'bar'
    fn = cliargs_deferred_get('missing', 'zug')
    assert fn() == 'zug'
    fn = cliargs_deferred_get('baz', shallowcopy=True)
    assert fn() == [1, 2, 3]

# Generated at 2022-06-12 21:23:45.529120
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get functions correctly"""

    class Foo(object):
        """Test object"""
        val = cliargs_deferred_get('test', '42')

    class Bar(object):
        """Test object that does a shallow copy of the value"""
        val = cliargs_deferred_get('test', '42', shallowcopy=True)

    # The first time, there is no value.  So we should get the default
    foo = Foo()
    assert foo.val == '42'

    # The second time, there is a value.  So we should get the value
    foo = Foo()
    CLIARGS['test'] = 'ansible'
    assert foo.val == 'ansible'

    # Test that the shallow copy gives us a copy of the value, not the reference
    bar = Bar()

# Generated at 2022-06-12 21:23:50.862700
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'answer': 42})
    assert cliargs_deferred_get('foo', 'baz')() == 'bar'
    assert cliargs_deferred_get('answer', 42)() == 42
    assert cliargs_deferred_get('baz', 'baz')() == 'baz'

# Generated at 2022-06-12 21:24:02.162703
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    def singleton_factory(arg):
        def inner():
            return arg
        return inner

    cli_args = {'a': 1, 'b': [1, 2], 'c': {'d': 3, 'e': 4}, 'd': set((1, 2, 3))}
    _init_global_context(cli_args)

    assert cli_args == CLIARGS.as_dict()

    ref_copy = cli_args.copy()
    ref_copy['b'] = [1, 2]
    ref_copy['c'] = {'d': 3, 'e': 4}
    ref_copy['d'] = set((1, 2, 3))


# Generated at 2022-06-12 21:24:07.568823
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_value(key, value):
        # Check that the first use works
        value1 = cliargs_deferred_get(key)()
        # Check that the new CLIARGS object is not effected by the first use of the closure
        value2 = cliargs_deferred_get(key)()

        assert value1 == value2
        assert value1 == value

    def assert_shallowcopy(key, value):
        global CLIARGS

        # Check that the first use works
        value1 = cliargs_deferred_get(key, shallowcopy=True)()
        # Check that the new CLIARGS object is not effected by the first use of the closure
        value2 = cliargs_deferred_get(key, shallowcopy=True)()

        assert value1 == value2
        assert value1 == value

       

# Generated at 2022-06-12 21:24:18.724824
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_dict():
        cli_args = {'foo': {'bar': {}}}

        # Test getting a value from a nested dictionary
        assert cliargs_deferred_get('foo')().get('bar', None) == {}

        # Test that a top level key that doesn't exist returns the default
        assert cliargs_deferred_get('bar', default=0)() == 0

        # Test that a nested key that doesn't exist returns the default
        assert cliargs_deferred_get('foo').get('baz', default=0) == 0

        # Test that a nested key that doesn't exist returns the default
        assert cliargs_deferred_get('foo', default={}).get('baz', default=0) == 0

        # Test that a nested key that doesn't exist returns the default
        assert cli

# Generated at 2022-06-12 21:24:30.199882
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=missing-docstring
    global CLIARGS  # pylint: disable=global-statement,invalid-name
    CLIARGS = CLIArgs({'foo': {'bar': {'baz': 'ding'}}})

    inner = cliargs_deferred_get('foo.bar')
    assert {'baz': 'ding'} == inner()
    assert {'baz': 'ding'} == inner()
    assert {'baz': 'ding'} != inner()

    inner = cliargs_deferred_get('foo.bar', shallowcopy=True)
    assert {'baz': 'ding'} == inner()
    assert {'baz': 'ding'} != inner()
    assert {'baz': 'ding'} == inner()