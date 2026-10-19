

# Generated at 2022-06-12 21:15:06.256386
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    global CLIARGS

    # Initial state
    assert not CLIARGS

    # Deferred value before setting CLIARGS (will get default value)
    deferred_keys = [
        cliargs_deferred_get('a', 'defaulta'),
        cliargs_deferred_get('b', 'defaultb'),
    ]

    # Setting CLIARGS (will set values for cliargs_deferred_get keys)
    CLIARGS = GlobalCLIArgs.from_options(dict(a='valuea', b='valueb'))

    # Value deferred before setting CLIARGS (should get default value)
    assert deferred_keys[0]() == 'defaulta'
    assert deferred_keys[1]() == 'defaultb'

    # Deferred value after setting CLIARGS

# Generated at 2022-06-12 21:15:15.430976
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({"a": 1})
    assert cliargs_deferred_get("a")() == 1
    # Anything not in CLIARGS has the default value None
    assert cliargs_deferred_get("b")() is None
    # Can also provide a different default value
    assert cliargs_deferred_get("b", default=2)() == 2
    # We can also shallow-copy the result
    CLIARGS.update({"c": "some string"})
    assert cliargs_deferred_get("c", shallowcopy=True)() == "some string"
    CLIARGS.update({"c": "another string"})
    assert cliargs_deferred_get("c", shallowcopy=True)() == "some string"

# Generated at 2022-06-12 21:15:25.451268
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    def test(cli_args, key, default, shallowcopy, expected):
        cli = CLIArgs(cli_args)
        inner_func = cliargs_deferred_get(key, default, shallowcopy)
        assert inner_func() == expected
    test({}, 'fake_key', 'default', False, 'default')
    test({'fake_key': 'value'}, 'fake_key', 'default', False, 'value')
    test({'fake_key': 'value'}, 'fake_key', 'default', True, 'value')
    test({'fake_key': ['value']}, 'fake_key', 'default', False, ['value'])
    test({'fake_key': ['value']}, 'fake_key', 'default', True, ['value'])


# Generated at 2022-06-12 21:15:35.926650
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    options = {'foo': 'bar'}
    global CLIARGS
    CLIARGS = CLIArgs(options)
    assert cliargs_deferred_get('foo') == 'bar'
    assert cliargs_deferred_get('bar', default='baz') == 'baz'
    assert cliargs_deferred_get('foo', shallowcopy=True) == 'bar'
    assert id(cliargs_deferred_get('bar', default=[])) != id(cliargs_deferred_get('bar', default=[]))
    assert id(cliargs_deferred_get('bar', default=[])) != id(cliargs_deferred_get('bar', default=[], shallowcopy=True))

# Generated at 2022-06-12 21:15:47.468423
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cliargs_val = dict(a=dict(b=[1, 2, 3]), c=True)
    CLIARGS = CLIArgs(cliargs_val)

    assert cliargs_val == cliargs_deferred_get('a')()
    assert cliargs_val['a'] == cliargs_deferred_get('a', shallowcopy=True)()
    assert cliargs_val['a']['b'] == cliargs_deferred_get('a', 'b')()
    assert cliargs_val['a']['b'] == cliargs_deferred_get('a', 'b', shallowcopy=True)()
    assert cliargs_val['c'] == cliargs_deferred_get('c')()
    assert cliargs_val['c'] == cl

# Generated at 2022-06-12 21:15:58.191222
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.config.manager import ConfigManager

    cli_args = ConfigManager(args=['--tags', 'foo', '--skip-tags', 'bar'])
    _init_global_context(cli_args)

    foo_deferred_get = cliargs_deferred_get('tags')
    assert foo_deferred_get() == ['foo']
    # Deferred test so it's deterministic, even if we change the implementation of
    # cliargs_deferred_get.
    assert foo_deferred_get() == foo_deferred_get()

    foo_deferred_get = cliargs_deferred_get('tags', shallowcopy=True)
    assert foo_deferred_get() == ['foo']
    # Deferred test so it's deterministic, even if we change the implementation of
    # cli

# Generated at 2022-06-12 21:16:04.790241
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from .context import CliArgs
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.utils.context_objects import CliArgsException

    with CliArgs(dict()) as cliargs:
        cliargs['host_pattern'] = '*'
        cliargs['connection'] = 'local'

        getter = cliargs_deferred_get('host_pattern')
        assert getter() is None
        _init_global_context(cliargs)
        getter = cliargs_deferred_get('host_pattern')
        assert getter() == '*'
        getter = cliargs_deferred_get('connection')
        assert getter() == 'local'
        # Get a value that does not exist
        getter = cliargs_deferred_get('foobar')

# Generated at 2022-06-12 21:16:12.906566
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'name': 'test'})

    test_func = cliargs_deferred_get('name')
    assert test_func() == 'test'

    CLIARGS = CLIArgs({})
    assert test_func() is None

    CLIARGS = CLIArgs({'list': [1, 2, 3]})
    test_func = cliargs_deferred_get('list', shallowcopy=True)
    assert test_func() == [1, 2, 3]
    assert test_func() is not [1, 2, 3]

# Generated at 2022-06-12 21:16:21.788826
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Validate that deferred returns the values that they should"""
    # Initialize the global context objects
    _init_global_context(dict(foo=1, bar=None))
    assert cliargs_deferred_get('foo')() == 1
    assert cliargs_deferred_get('bar')() == None
    # make sure that shallow copies work
    array = [1, 2, 3]
    obj = cliargs_deferred_get('foo', shallowcopy=True)()
    assert obj == 1
    assert id(obj) != id(array)
    obj = cliargs_deferred_get('bar', shallowcopy=True)()
    assert obj is None

# Generated at 2022-06-12 21:16:33.444994
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Make sure the cliargs_deferred get works as expected"""
    # This is a dirty hack but until I can find a better way if I don't do this then
    # the stdout/stderr capture in ``ansible/test/unit/utils/context_objects.py`` will
    # fail
    import sys
    import warnings

    stderr = sys.stderr
    stdout = sys.stdout
    sys.stdout = sys.stderr = open('/dev/null', 'w')
    warnings.filterwarnings('error')


# Generated at 2022-06-12 21:16:44.801830
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(key=dict(a=1, b=2), key2=[1,2,3], key3=1))
    assert cliargs_deferred_get('key')() == dict(a=1,b=2)
    assert cliargs_deferred_get('key2')() == [1,2,3]
    assert cliargs_deferred_get('key3')() == 1
    assert cliargs_deferred_get('noexist')() is None
    assert cliargs_deferred_get('noexist', default=1)() == 1

    assert cliargs_deferred_get('key', shallowcopy=True)() != dict(a=1,b=2)

# Generated at 2022-06-12 21:16:55.043531
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    # __name__ is something else in the context of the ansible-playbook process
    import __main__ as orig_main
    import mock
    import sys
    import ansible.cli.playbook

    old_args = sys.argv[:]
    old_main = sys.modules[orig_main.__name__]
    cli_args = {}

    # Simulate the begin_playbook() function being called to set the context

# Generated at 2022-06-12 21:17:06.545259
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Check ``cliargs_deferred_get`` works as expected"""

    global CLIARGS
    from ansible.utils.context_objects import CLIArgs

    CLIARGS = CLIArgs({'test': {'test': {'test': 'yes'}}})
    assert cliargs_deferred_get('test')() == {'test': {'test': 'yes'}}
    assert cliargs_deferred_get('test')() is CLIARGS['test']

    assert cliargs_deferred_get('test', shallowcopy=True)() == {'test': {'test': 'yes'}}
    assert cliargs_deferred_get('test', shallowcopy=True)() is not CLIARGS['test']

    # Test default never gets returned if it is a mapping
    default = {'test': 'yes'}
   

# Generated at 2022-06-12 21:17:12.397524
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import is_sequence

    class C(object):
        pass

    class D(C):
        pass

    class E(D):
        pass

    CLIARGS.clear()

    assert cliargs_deferred_get('missing')(default='abc') == 'abc'
    assert cliargs_deferred_get('missing', default='abc')() == 'abc'
    assert cliargs_deferred_get('missing', default='abc') == 'abc'

    assert cliargs_deferred_get('missing', default=None)() is None
    assert cliargs_deferred_get('missing', default=None) == None

    CLIARGS['s'] = 's'
    CLIARGS['i'] = 10

# Generated at 2022-06-12 21:17:20.772614
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Set up a random CLIArgs with a small number of overlapping values
    from ansible.cli import CLI
    cli_args = CLI.parse()[0]
    cli_args.foo = cli_args.bar = cli_args.baz = ['a', 'b', 'c']
    _init_global_context(cli_args)

    # Set up a function to get the value of each key from CLIARGS
    fns = {}
    for key in ['foo', 'bar', 'nope']:
        fns[key] = cliargs_deferred_get(key, shallowcopy=True)

    # Check that they return the same value as CLIARGS.get if we call them
    assert sorted(fns.keys()) == sorted(cli_args.keys())

# Generated at 2022-06-12 21:17:32.048856
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test function cliargs_deferred_get
    from ansible.module_utils.common.collections import ImmutableDict
    # Test with no args
    cli_args = {}
    _init_global_context(cli_args)
    f = cliargs_deferred_get('foo')
    assert f() is None
    # Test with default
    f = cliargs_deferred_get('foo', default='bar')
    assert f() == 'bar'
    # Test overriding the default
    cli_args['foo'] = 'baz'
    _init_global_context(cli_args)
    assert f() == 'baz'
    # Test that we get a shallow copy of the passed in object
    cli_args['foo'] = [1, 2, 3]
    _init_global_context

# Generated at 2022-06-12 21:17:34.851303
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.setdefault('key', 'value')
    assert cliargs_deferred_get('key')() == 'value'

# Generated at 2022-06-12 21:17:41.583511
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('missing')(), None
    assert cliargs_deferred_get('missing', 5)(), 5
    assert cliargs_deferred_get('missing', 0, True)() == 0
    assert cliargs_deferred_get('missing', [], True)() == []
    assert cliargs_deferred_get('missing', {}, True)() == {}
    assert cliargs_deferred_get('missing', {5, 6}, True)() == {5, 6}

# Generated at 2022-06-12 21:17:52.229161
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # Make sure the base case of getting an option with a default works
    CLIARGS = GlobalCLIArgs({})
    get_foo = cliargs_deferred_get('foo', default='default')
    assert CLIARGS.get('foo', default='default') == 'default'

    assert get_foo() == 'default'

    # Make sure the base case of getting an option without a default works
    CLIARGS = GlobalCLIArgs({})
    get_foo = cliargs_deferred_get('foo', default=None)
    assert CLIARGS.get('foo', default=None) is None

    assert get_foo() is None

    # Make sure the base case of getting an option without a default works
    CLIARGS = GlobalCLIArgs({'foo': 'bar'})

# Generated at 2022-06-12 21:18:01.721698
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('test_key')() is None
    CLIARGS['test_key'] = True
    assert cliargs_deferred_get('test_key')() is True
    CLIARGS['test_key'] = False
    assert cliargs_deferred_get('test_key')() is False
    CLIARGS['test_key'] = 1
    assert cliargs_deferred_get('test_key')() == 1
    CLIARGS['test_key'] = 'one'
    assert cliargs_deferred_get('test_key')() == 'one'
    CLIARGS['test_key'] = [1, 2, 3]
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == [1, 2, 3]
    assert cli

# Generated at 2022-06-12 21:18:16.383597
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    CLIARGS['foo'] = 'bar'

    # Ensure we get out the proper value
    assert cliargs_deferred_get('foo')() == 'bar'

    # Ensure errors bubble up through
    try:
        cliargs_deferred_get('baz')()
    except KeyError:
        pass
    else:
        raise AssertionError('Did not get KeyError when fetching non-existing key')

    # Ensure we get the default value
    assert cliargs_deferred_get('baz', default='qux')() == 'qux'

    # Ensure that the returned value is a shallow copy of the original
    # Note: we don't

# Generated at 2022-06-12 21:18:25.753091
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Setup
    global CLIARGS
    og_cliargs = CLIARGS
    CLIARGS = CLIArgs({"foo": "bar"})

    # Tests
    assert cliargs_deferred_get("foo")() == "bar"
    assert cliargs_deferred_get("foo", shallowcopy=True)() != "bar"
    assert cliargs_deferred_get("foo", shallowcopy=True)() == ["bar"]
    assert cliargs_deferred_get("foo", default="baz")() == "bar"
    assert cliargs_deferred_get("foo", default="baz", shallowcopy=True)() == "bar"
    assert cliargs_deferred_get("baz")() is None

    # Teardown
    CLIARGS = og_cliargs

# Generated at 2022-06-12 21:18:37.334514
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that it works with CLIARGS as a mock
    test_args = dict(foo='bar')
    with mock.patch.dict(globals(), {'CLIARGS': mock.Mock(spec=CLIArgs, **test_args)}):
        assert cliargs_deferred_get('foo', default='baz')() == 'bar'
        assert cliargs_deferred_get('bar', default='baz')() == 'baz'
    # Test that it works when CLIARGS has been replaced by another mock
    test_args = dict(foo='bar')
    CLIARGS = mock.Mock(spec=CLIArgs, **test_args)
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'

# Generated at 2022-06-12 21:18:47.307301
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class CLIArgs_Testing(dict):
        def get(self, key):
            return self[key]
    global CLIARGS
    CLIARGS = CLIArgs_Testing()
    CLIARGS['force_color'] = False
    CLIARGS['diff'] = False
    CLIARGS['tree'] = None
    CLIARGS['host_key_checking'] = False
    CLIARGS['listhosts'] = False
    CLIARGS['listtasks'] = False
    CLIARGS['listtags'] = False

    CLIARGS['any_errors_fatal'] = False
    CLIARGS['interpreter_python'] = '/usr/bin/python'
    CLIARGS['connection'] = 'smart'
    CLIARGS['namespace'] = False
    CLIARGS['forks'] = 5

# Generated at 2022-06-12 21:18:58.078492
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _populate_cliargs():
        # Defer the population of CLIARGS to the end of this function so that we can setup
        # some data to test with.  The only requirement is that it happens before the
        # test_cliargs_deferred_get function returns
        global CLIARGS
        CLIARGS = GlobalCLIArgs.from_options({'test_key': 'test_value'})
    _populate_cliargs()
    assert cliargs_deferred_get('test_key')() == 'test_value'
    assert cliargs_deferred_get('test_key_noexist')() is None
    assert cliargs_deferred_get('test_key_noexist', default='test_value')() == 'test_value'

# Generated at 2022-06-12 21:19:08.375208
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    _init_global_context({})
    # Test getting a nonexistent value
    nonexistent_value = cliargs_deferred_get('nonexistent')
    assert nonexistent_value() is None
    # Test getting a shallow value
    shallow_value = cliargs_deferred_get('_ansible_argv', default=['-m', 'ping'])
    ansible_argv = shallow_value(shallowcopy=True)
    assert ansible_argv == ['-m', 'ping']
    # Modify the original
    CLIARGS._ansible_argv = ['-m', 'shell']
    # Check that the cached value is still the same
    assert ansible_argv == ['-m', 'ping']
    # Get a fresh value
    ans

# Generated at 2022-06-12 21:19:17.736349
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def inner(default=None, shallowcopy=False):
        return cliargs_deferred_get('foo', default=default, shallowcopy=shallowcopy)()
    test_cliargs = CLIArgs({'foo': 42})
    global CLIARGS
    CLIARGS = test_cliargs
    assert inner() == 42
    CLIARGS = CLIArgs()
    assert inner(default=43) == 43
    CLIARGS = test_cliargs
    assert inner(default=43) == 42
    assert inner([1, 2, 3], shallowcopy=True) == [1, 2, 3]
    assert inner({'bar': 'baz'}, shallowcopy=True) == {'bar': 'baz'}
    assert inner(set((1, 2, 3)), shallowcopy=True) == set((1, 2, 3))

# Generated at 2022-06-12 21:19:26.531762
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_with(cliargs_value, expected_result, shallowcopy=False):
        global CLIARGS
        orig_cliargs = CLIARGS

        try:
            CLIARGS = CLIArgs({'ansible_test': cliargs_value})
            actual_result = cliargs_deferred_get('ansible_test', shallowcopy=shallowcopy)()
            assert actual_result == expected_result
        finally:
            CLIARGS = orig_cliargs

    # Test fallback to default with multiple types
    test_with(None, 'ansible_default')
    test_with('ansible_value', 'ansible_value')
    test_with((1, 2), (1, 2))
    test_with({'a': 1}, {'a': 1})

    # Test shallow copy or not
    test_

# Generated at 2022-06-12 21:19:38.039375
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    cli_args = dict(foo=42)
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() == 42
    assert cliargs_deferred_get('bar')() is None
    assert cliargs_deferred_get('bar', default=10)() == 10
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 42
    assert cliargs_deferred_get('bar', shallowcopy=True)() is None
    assert cliargs_deferred_get('bar', shallowcopy=True, default=10)() == 10
    from ansible.module_utils.common.collections import ImmutableDict, ImmutableList

# Generated at 2022-06-12 21:19:49.192791
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    "Unit test for function cliargs_deferred_get"
    def cli_args(**kwargs):
        return CLIArgs(kwargs)
    def test_func(value, default, shallowcopy, result):
        global CLIARGS
        CLIARGS = cli_args(foo=value)
        # The inner function is not bound to a specific context so we can't use
        # the @pytest.fixture to set/restore the context.  Instead we use the
        # global here (which seems to work ok because we never call pytest
        # fixtures within these nested functions below)
        deferred_value = cliargs_deferred_get('foo', default=default, shallowcopy=shallowcopy)
        assert deferred_value() == result

# Generated at 2022-06-12 21:20:01.246895
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""

    # This is the "sanity test" where CLIARGS exists and we get the value that
    # is stored in it
    _init_global_context({'ANSIBLE_CONFIG': 'test'})
    func = cliargs_deferred_get('ANSIBLE_CONFIG')
    assert 'test' == func()
    _init_global_context({})

    # This is the case where we want to get a value from CLIARGS but it hasn't
    # been set up yet so we get the default
    func = cliargs_deferred_get('ANSIBLE_FOO', default={'foo'}, shallowcopy=True)
    assert {'foo'} == func()
    _init_global_context({})

    # This is the case where we want to get

# Generated at 2022-06-12 21:20:10.468522
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.context_objects import GlobalCLIArgs
    class FakeCliArgs(GlobalCLIArgs):
        def __init__(self):
            self._values = {}

    # Note: if you change this, ensure that you update the fields in testcases
    # to match

# Generated at 2022-06-12 21:20:19.946883
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    # Set up a context for testing
    global CLIARGS
    CLIARGS = CLIArgs({'test': [{'a': 1, 'b': 2}], 'test2': [{'c': 3, 'd': 4}]})

    default_function = cliargs_deferred_get('test')
    assert default_function() is CLIARGS.test
    assert default_function() is not CLIARGS.test
    assert default_function() == CLIARGS.test
    assert default_function()[0] is CLIARGS.test[0]
    assert default_function()[0] is not CLIARGS.test[0]
    assert default_function()[0] == CLIARGS.test[0]
    # Test that shallow copy works for sequences
   

# Generated at 2022-06-12 21:20:29.357378
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'test': {'key': [1, 2, 3]}})
    closure = cliargs_deferred_get('test', 'key')
    assert closure() == [1, 2, 3]

    closure = cliargs_deferred_get('<not>', '<exists>')
    assert closure() == '<exists>'

    closure = cliargs_deferred_get('test', 'key', shallowcopy=True)
    assert closure() == [1, 2, 3]
    assert closure() is not [1, 2, 3]

    closure = cliargs_deferred_get('test', 'key', shallowcopy=True)
    assert closure() == [1, 2, 3]
    assert closure() is not [1, 2, 3]

# Generated at 2022-06-12 21:20:31.771457
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_deferred_get('test', 'value')()
    cliargs_deferred_get('test')()

# Generated at 2022-06-12 21:20:40.964461
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({})
    cliargs.processed = True
    cliargs['magic'] = 42
    cliargs['mylist'] = [1, 2, 3]
    cliargs['mytuple'] = (1, 2, 3)
    cliargs['myset'] = set([1, 2, 3])
    cliargs['mydict'] = {1: 2, 3: 4}

    assert cliargs_deferred_get('magic', shallowcopy=False)() == 42
    assert cliargs_deferred_get('magic', shallowcopy=True)() == 42
    assert cliargs_deferred_get('mytuple', shallowcopy=False)() == (1, 2, 3)

# Generated at 2022-06-12 21:20:52.475034
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict

    global CLIARGS
    CLIARGS = CLIArgs({'a': [1, 2, 3]})

    assert cliargs_deferred_get('a')(), CLIARGS['a']
    assert cliargs_deferred_get('b')(), None
    assert cliargs_deferred_get('c', [4, 5, 6])(), [4, 5, 6]
    assert cliargs_deferred_get('c', shallowcopy=True)(), [4, 5, 6]
    assert cliargs_deferred_get('a', shallowcopy=True)(), [1, 2, 3]

    CLIARGS = CLIArgs({'a': ImmutableDict({'b': [1, 2, 3]})})

# Generated at 2022-06-12 21:21:00.803687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    expected = {'roles': []}
    class _GlobalCLIArgs(GlobalCLIArgs):
        def __init__(self, args):
            super(_GlobalCLIArgs, self).__init__(args)
        def get(self, key, default=None):
            if key == 'roles':
                return expected['roles']
            else:
                raise RuntimeError('Unexpected key passed to get')

    global CLIARGS
    CLIARGS = _GlobalCLIArgs({})
    roles = cliargs_deferred_get('roles')
    assert roles() == []

    roles = cliargs_deferred_get('roles', shallowcopy=True)
    assert roles() == []

    expected['roles'] = ['a']
    assert roles() == []

    roles = cliargs_deferred_get

# Generated at 2022-06-12 21:21:04.975886
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def run_test(cliargs, key, default, expected):
        global CLIARGS
        try:
            CLIARGS = CLIArgs(cliargs)
            assert cliargs_deferred_get(key, default=default)() == expected
        finally:
            CLIARGS = CLIArgs({})

    run_test({'a': 'a', 'b': 'b'}, 'b', 'c', 'b')
    run_test({'a': 'a', 'b': 'b'}, 'c', 'c', 'c')
    run_test({'a': 'a', 'b': 'b'}, 'b', 'c', 'b')
    run_test({'a': 'a', 'b': 'b'}, 'c', 'c', 'c')

# Generated at 2022-06-12 21:21:12.406039
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get()"""

    # pylint: disable=unused-variable,missing-docstring,invalid-name
    def test(caseno, key, value, shallowcopy, expected_result):
        CLIARGS = CLIArgs({key: value})
        assert cliargs_deferred_get(key, default=None, shallowcopy=shallowcopy)() == expected_result

    test(1, 'key', 1, False, 1)
    test(2, 'key', [1], False, [1])
    test(3, 'key', (1, 2), False, (1, 2))
    test(4, 'key', {'foo': 'bar'}, False, {'foo': 'bar'})

    test(5, 'key', 1, True, 1)

# Generated at 2022-06-12 21:21:22.711400
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': 1, 'b': 2, 'c': [1, 2]})
    value = cliargs_deferred_get('a')()
    assert value == 1

    value = cliargs_deferred_get('a', 2)()
    assert value == 1

    value = cliargs_deferred_get('z', 2)()
    assert value == 2

    value = cliargs_deferred_get('c', shallowcopy=True)()
    assert value == [1, 2]
    assert value is not CLIARGS['c']
    CLIARGS['c'].append(3)
    value = cliargs_deferred_get('c', shallowcopy=False)()
    assert value == [1, 2, 3]
    assert value is CLIAR

# Generated at 2022-06-12 21:21:33.313147
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    global CLIARGS

# Generated at 2022-06-12 21:21:39.960094
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that ``cliargs_deferred_get`` works as intended

    For the full test of this functionality, see ``tests/units/module_utils/common/common_context.py``
    """
    test_cliargs = {
        'debug': True,
        'verbosity': 5,
        'module_paths': ['path1', 'path2'],
        'check_mode': True,
        'diff': False,
        'tree': '/path/to/tree',
        'extra_vars': {
            'var1': 'val1',
            'var2': 'val2',
        }
    }
    class GlobalCLIArgsMock(object):
        """Mock out GlobalCLIArgs so that we can properly test the cliargs_deferred_get function"""

# Generated at 2022-06-12 21:21:42.577302
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['test1'] = 'test2'
    assert cliargs_deferred_get('test1')() == 'test2'
    assert cliargs_deferred_get('test3')() is None

# Generated at 2022-06-12 21:21:48.147989
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Functional test for cliargs_deferred_get

    Initializes the global context for testing.
    """
    global CLIARGS
    cli_args = {'test_list': [1, 2, 3]}
    CLIARGS = CLIArgs(cli_args)
    inner = cliargs_deferred_get('test_list', shallowcopy=True)
    value = inner()
    assert value != cli_args['test_list']
    assert value == cli_args['test_list']

    cli_args = {'test_list': [1, 2, 3]}
    CLIARGS = CLIArgs(cli_args)
    inner = cliargs_deferred_get('test_list', shallowcopy=False)
    value = inner()
    assert value == cli_args['test_list']

# Generated at 2022-06-12 21:21:58.861392
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class GlobalCLIArgsTest:
        def __init__(self, cli_args):
            self.values = cli_args

        def get(self, key, default=None):
            return self.values[key]

        def __contains__(self, key):
            return key in self.values

    def _get_val(key):
        return cliargs_deferred_get(key, shallowcopy=False)()

    global CLIARGS
    CLIARGS = GlobalCLIArgsTest({'key': 'value'})
    assert _get_val('key') == 'value'
    assert _get_val('missing_key') is None
    assert _get_val('missing_key', 'default_value') == 'default_value'


# Generated at 2022-06-12 21:22:10.040332
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    from unittest import mock
    from copy import copy, deepcopy
    from ansible.utils.context_objects import CLIArgs

    # CLIArgs.get returns a list by default
    class MockCLIArgs(CLIArgs):
        def get(self, key, default=None):
            return ['value']

    test_value = 'test_value'
    empty_list = []
    empty_dict = {}
    empty_set = set()

    # cliargs_deferred_get defaults to copy
    with mock.patch('ansible.utils.context_objects.CLIARGS', MockCLIArgs()):
        assert test_value != cliargs_deferred_get('key', test_value)
        assert test_value != cliargs_deferred_get

# Generated at 2022-06-12 21:22:20.120305
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from collections import namedtuple
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping, Set

    class FakeCLIArgs(object):
        def __init__(self, values):
            self._values = values

        def get(self, key, default=None):
            return self._values.get(key, default)


# Generated at 2022-06-12 21:22:27.411081
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Test no defined
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('foo')() == None
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    # Test different types
    assert cliargs_deferred_get('foo', shallowcopy=True, default='baz')() == 'bar'
    CLIARGS = CLIArgs({'foo': [1, 2], 'bar': {'one': 1}, 'baz': set([1, 2, 3])})
    assert cl

# Generated at 2022-06-12 21:22:30.861789
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    >>> CLIARGS['test_arg'] = 'test_val'
    >>> assert cliargs_deferred_get('test_arg')() == 'test_val'
    """

# Generated at 2022-06-12 21:22:44.421225
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    import pprint
    from ansible.module_utils.common.collections import is_sequence

    _init_global_context({'a': {'b': [1, 2, 3]}, 'c': [4, 5, 6], 'd': {1, 2, 3}, 'e': 'foo'})
    a_b = cliargs_deferred_get('a.b')
    assert a_b() == [1, 2, 3]
    assert [1, 2, 3] != a_b()
    assert a_b(1, [1, 2, 3]) == [1, 2, 3]

    a_b_copy = cliargs_deferred_get('a.b', shallowcopy=True)
    assert a_b_copy() == [1, 2, 3]

# Generated at 2022-06-12 21:22:46.970634
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    global CLIARGS
    assert cliargs_deferred_get('not_there')() is None



# Generated at 2022-06-12 21:22:58.546202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': ['bar'], 'bar': 1, 'baz': {'spam': 'eggs'}, 'quux': {1, 2}}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs_deferred_get('bar')() == 1
    assert cliargs_deferred_get('baz')() == {'spam': 'eggs'}
    assert cliargs_deferred_get('quux')() == {1, 2}

    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']
    assert cliargs_deferred_get('bar', shallowcopy=True)() == 1

# Generated at 2022-06-12 21:23:07.169682
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:23:16.497921
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs, ContextObject

    globals()['CLIARGS'] = GlobalCLIArgs.from_options({'ANSIBLE_CALLABLE_WHITELIST': ['ping']})
    ContextObject._instances = {}

    # Function is callable
    cliargs_deferred_get('ANSIBLE_CALLABLE_WHITELIST')()

    # Default works
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'

    # Shallow copy function works
    import types
    assert cliargs_deferred_get('ANSIBLE_CALLABLE_WHITELIST', shallowcopy=True)() is not CLIARGS.get('ANSIBLE_CALLABLE_WHITELIST')

# Generated at 2022-06-12 21:23:25.988445
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import contextlib
    global CLIARGS
    test_dict = {'test': 'dict'}
    test_list = ['test', 'list', 'of', 'objects']
    test_vals = [
        ('test_default', None, None),
        ('test_dict', test_dict, test_dict),
        ('test_list', test_list, test_list),
    ]
    for key, value, expected in test_vals:
        func = cliargs_deferred_get(key, value)
        assert not func() is value
        assert func() == expected
        with contextlib.suppress(AttributeError):
            test_list.pop()
        with contextlib.suppress(AttributeError):
            test_dict.pop('test')
        func = cliargs_deferred_get(key, value, True)

# Generated at 2022-06-12 21:23:35.314367
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from collections import namedtuple
    CliArgsTest = namedtuple('CliArgsTest', ['items'])
    cli_args = CliArgsTest(items=[1, 2, 3])
    _init_global_context(cli_args)
    assert cliargs_deferred_get('items')() == [1, 2, 3]
    # Make sure we are getting copies
    cliargs_deferred_get('items')()[1] = 4
    assert cli_args.items == [1, 2, 3]
    assert cliargs_deferred_get('items', shallowcopy=True)() == [1, 2, 3]
    # Make sure we are getting copies
    cliargs_deferred_get('items', shallowcopy=True)()[1] = 4

# Generated at 2022-06-12 21:23:45.114671
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test case where the shallow copy is required
    cli_args = dict(foo=['hello', 'world'])
    _init_global_context(cli_args)
    value = cliargs_deferred_get('foo', shallowcopy=True)()
    assert value == ['hello', 'world']
    assert id(value) != id(cli_args['foo'])

    # Test case where shallow copy is not required
    cli_args = dict(foo=10)
    _init_global_context(cli_args)
    value = cliargs_deferred_get('foo')()
    assert value == 10
    assert id(value) == id(cli_args['foo'])

    # Test default
    cli_args = dict(foo='bar')
    _init_global_context(cli_args)
   

# Generated at 2022-06-12 21:23:52.087858
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    from ansible.module_utils.common.collections import frozendict

    def test_get(key, default=None, shallowcopy=False):
        return cliargs_deferred_get(key, default, shallowcopy)()

    CONST_DEFAULT = 'CONST_DEFAULT'

    # Do not use with defaults
    test_args = {'inventory': 'test.inventory'}
    test_global_args = CLIArgs.from_options(test_args)
    CLIARGS = test_global_args

    assert 'inventory' in test_args
    assert test_get('inventory') == 'test.inventory'
    assert test_get('inventory', default=CONST_DEFAULT) == 'test.inventory'

    # If a default is passed in, we get

# Generated at 2022-06-12 21:24:03.010303
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'connection': 'network_cli', 'become_user': 'bob'})
    # Connection should be deferred
    assert cliargs_deferred_get('connection', default='local')() == 'network_cli'
    # Become user should be deferred
    assert cliargs_deferred_get('become_user')() == 'bob'
    # Nothing should be deferred
    assert cliargs_deferred_get('inventory', default='/dev/null')() == '/dev/null'

    # Work with objects that need to be shallow copied
    _init_global_context({'extra_vars': {'a': 'b', 'c': 'd'}})
    #

# Generated at 2022-06-12 21:24:14.410802
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from mock import patch
    from ansible.utils.context_objects import GlobalCLIArgs

    with patch('ansible.utils.context_objects.CLIARGS', GlobalCLIArgs({})) as cli_args:
        cliargs_deferred_get('key')()

    cli_args.get.assert_called_once_with('key', default=None)

# Generated at 2022-06-12 21:24:25.987454
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # when a shallowcopy is not requested
    assert cliargs_deferred_get('a')() is None
    assert cliargs_deferred_get('a', default=3)() == 3
    CLIARGS['a'] = 3
    assert cliargs_deferred_get('a')() == 3
    # nothing is shallow copied
    CLIARGS['a'] = [1, 2, 3]
    assert cliargs_deferred_get('a')() is CLIARGS['a']
    CLIARGS['a'] = (1, 2, 3)
    assert cliargs_deferred_get('a')() is CLIARGS['a']
    CLIARGS['a'] = {'a': 'b'}
    assert cliargs_deferred_get('a')() is CLIARGS['a']

    #

# Generated at 2022-06-12 21:24:36.869476
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    mock_cliargs = {'one': 1, 'two': 2, 'three': 3, 'four': [4, 4, 4], 'five': {'five': 5}, 'six': {'six', 6}, 'none': None, 'false': False}
    cliargs = CLIArgs(mock_cliargs)
    # Test that the cliargs object is unique to the returned reference
    assert mock_cliargs is not cliargs

    func = cliargs_deferred_get('one')
    assert func() == 1

    func = cliargs_deferred_get('four')
    assert func() == [4, 4, 4]

    func = cliargs_deferred_get('four', shallowcopy=True)
    # Make sure a shallow copy was actually made
    assert func() is not [4, 4, 4]


# Generated at 2022-06-12 21:24:47.052289
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_equal(actual, expected):
        assert actual == expected, '%s != %s' % (actual, expected)

    def _try_and_catch(fn, expected_exc):
        try:
            fn()
        except expected_exc:
            pass
        except BaseException:
            raise AssertionError('Function %s did not raise exception %s' % (fn.__name__, expected_exc))
        else:
            raise AssertionError('Function %s did not raise exception %s' % (fn.__name__, expected_exc))

    CLIARGS['test_field'] = 'test_value'
    inner = cliargs_deferred_get('test_field')
    assert_equal(inner(), 'test_value')

# Generated at 2022-06-12 21:24:57.951251
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.utils.collection_plugins import CollectionFinder
