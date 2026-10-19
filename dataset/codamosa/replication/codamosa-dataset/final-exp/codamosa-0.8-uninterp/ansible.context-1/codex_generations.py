

# Generated at 2022-06-12 21:15:07.525125
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_init({'x': 'valx', 'y': 'valy', 'z': 'valz'})
    default = 'def'
    assert cliargs_deferred_get('x', default)() == 'valx'
    assert cliargs_deferred_get('n', default)() == default

    default = ['def']
    assert cliargs_deferred_get('x', default, shallowcopy=True)() == 'valx'
    assert cliargs_deferred_get('n', default, shallowcopy=True)() == default[:]

    default = {'def': 'def'}
    assert cliargs_deferred_get('x', default, shallowcopy=True)() == 'valx'

# Generated at 2022-06-12 21:15:13.192696
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Start off with CLIARGS not being able to get anything
    assert CLIARGS.get('anything', default='not_here') == 'not_here'

    # Now set a dictionary in the CLIARGS
    global CLIARGS
    CLIARGS = CLIArgs({'test': {'test1': 'test_value'}})
    assert cliargs_deferred_get('test') == {'test1': 'test_value'}
    assert cliargs_deferred_get('test', shallowcopy=True) == {'test1': 'test_value'}

    # Now replace the CLIARGS
    CLIARGS = CLIArgs({'test_there': True})
    assert cliargs_deferred_get('test_there') is True

# Generated at 2022-06-12 21:15:16.680602
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS, _init_global_context

    test_args = {"foo": "bar"}

    _init_global_context(test_args)

    assert cliargs_deferred_get("foo") == "bar"

    # Test new global args object
    _init_global_context({"bar": "baz"})

    # Get the current value
    assert cliargs_deferred_get("bar") == "baz"

    # Make sure the the key was not present in the first object
    assert cliargs_deferred_get("foo") is None

# Generated at 2022-06-12 21:15:27.014802
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    cli_args = {'foo': [1, 2, 3], 'bar': {'x': 1}}
    _init_global_context(cli_args)

    cliargs_foo = cliargs_deferred_get('foo')
    assert cliargs_foo() is CLIARGS['foo']

    cliargs_bar = cliargs_deferred_get('bar')
    assert cliargs_bar() is CLIARGS['bar']

    orig_set = CLIARGS['foo']
    orig_set.append(1)
    assert cliargs_foo() is orig_set

    orig_dict = CLIARGS['bar']
    orig_dict['y'] = 2
    assert cliargs_bar() is orig_dict

    cliargs_foo_copy = cliargs_deferred

# Generated at 2022-06-12 21:15:37.258001
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    pairs = (
        ('test', True),
        ('ansible_check_mode', True),
        ('diff', True),
        ('ansible_verbosity', None),
        ('ansible_verbose', None),
        ('ansible_quiet', None),
        ('ansible_metadata', None),
        ('ansible_force_color', None),
        ('ansible_ansible_module_muted', None),
    )
    global CLIARGS
    CLIARGS = CLIArgs({key: value for key, value in pairs})
    for key, value in pairs:
        assert cliargs_deferred_get(key)() == value
        if value is not None:
            assert cliargs_deferred_get(key, shallowcopy=True)() is not value

# Generated at 2022-06-12 21:15:48.669116
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=redefined-outer-name
    cliargs_deferred_get = cliargs_deferred_get  # pylint: disable=redefined-builtin
    # Test return of value for a non-sequence object
    def _test():  # pylint: disable=missing-docstring, invalid-name
        return cliargs_deferred_get('foo', default='bar', shallowcopy=False)

    assert 'bar' == _test()
    assert 'bar' != cliargs_deferred_get('foo', default='baz', shallowcopy=False)

    # Test that we get a shallow copy of a sequence

# Generated at 2022-06-12 21:15:59.482133
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common.yaml import AnsibleUnsafeLoader

    CLIARGS_TEST = CLIArgs({'a': ['a', 'b', 'c'], 'b': {'1': '11', '2': '22'}, 'c': (1, 2, 3)})

    def get_test(key, default, shallowcopy, expected_type, expected_value):
        result = cliargs_deferred_get(key, default, shallowcopy)()
        assert isinstance(result, expected_type), \
            "Expected type %r but got %r" % (expected_type, type(result))

# Generated at 2022-06-12 21:16:04.731108
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Make sure the function works on default data
    assert cliargs_deferred_get('foo')() == None, 'default value not working'
    # Make sure the function works on set data
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar', 'set value not working'



# Generated at 2022-06-12 21:16:15.636093
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    c = CLIArgs({'a': 1, 'b': {'c': 'd', 'e':'f'}, 'g': ['h','i','j']})
    f = cliargs_deferred_get('a')
    assert f() == 1
    f = cliargs_deferred_get('b')
    assert f() == {'c':'d', 'e':'f'}
    f = cliargs_deferred_get('g')
    assert f() == ['h','i','j']
    f = cliargs_deferred_get('g', shallowcopy=True)
    assert isinstance(f(), list)
    assert f() == ['h','i','j']
    assert f() is not c['g']
    f = cliargs_deferred_get('b', shallowcopy=True)


# Generated at 2022-06-12 21:16:25.146485
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_dict = {'a': {'b': 'c', 'd': ['e', 'f']}, 'g': set()}
    cli_args = CLIArgs(test_dict)
    global CLIARGS
    CLIARGS = cli_args
    assert cliargs_deferred_get('a')() == test_dict['a']
    assert cliargs_deferred_get('a', default={})() == test_dict['a']
    assert cliargs_deferred_get('a', shallowcopy=True)() == test_dict['a']
    assert cliargs_deferred_get('a', shallowcopy=True)() is not cliargs_deferred_get('a')()
    assert cliargs_deferred_get('a')() is cliargs_deferred_get('a')()


# Generated at 2022-06-12 21:16:40.898613
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': [1, 2]}
    _init_global_context(cli_args)
    inner = cliargs_deferred_get('foo')
    assert inner() == cli_args['foo']
    cli_args['foo'].append(3)
    assert inner() == cli_args['foo']
    assert inner() != [1, 2, 3]

    inner = cliargs_deferred_get('foo', shallowcopy=True)
    assert inner() == [1, 2, 3]
    cli_args['foo'].append(4)
    assert inner() == [1, 2, 3]

    inner = cliargs_deferred_get('bar', default='default')
    assert inner() == 'default'


# Generated at 2022-06-12 21:16:52.674372
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    local_dict = {}
    cli_args = {
        'test_value_0': 0,
        'test_value_1': [1, 2, 3],
        'test_value_2': {'a': 1, 'b': 2},
        'test_value_3': set([1, 2, 3]),
    }
    _init_global_context(cli_args)

# Generated at 2022-06-12 21:17:04.135548
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    global CLIARGS  # pylint: disable=global-statement,invalid-name
    CLIARGS = GlobalCLIArgs.from_options({})
    assert cliargs_deferred_get('shallowcopy')(default=False) is False
    assert cliargs_deferred_get('shallowcopy')(default=True) is True

    CLIARGS.update(dict(shallowcopy=True))
    assert cliargs_deferred_get('shallowcopy')(default=False) is True
    assert cliargs_deferred_get('shallowcopy')(default=True) is True

    CLIARGS.update(dict(shallowcopy=False))
    assert cliargs_deferred_get('shallowcopy')(default=False) is False
   

# Generated at 2022-06-12 21:17:14.664143
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    _init_global_context(dict(
        deprecation_warnings=False,
        ignore_deprecations=False,
        log_deprecations=0,
        declared_vars=dict(),
        extra_vars=dict(),
    ))
    # Basic function test
    cliargs_deferred_get('deprecation_warnings')()
    cliargs_deferred_get('ignore_deprecations')()
    cliargs_deferred_get('log_deprecations')()
    cliargs_deferred_get('declared_vars')()
    cliargs_deferred_get('undefined_vars')()

    # Shallow copy test

# Generated at 2022-06-12 21:17:21.938652
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': '1', 'b': [2, 3], 'c': {'d': 4}})
    assert(cliargs_deferred_get('a')() == '1')
    assert(cliargs_deferred_get('b')() == [2, 3])
    assert(cliargs_deferred_get('c')() == {'d': 4})
    assert(cliargs_deferred_get('d')() is None)
    assert(cliargs_deferred_get('d', '5')() == '5')

    assert(cliargs_deferred_get('a', shallowcopy=True)() == '1')
    assert(cliargs_deferred_get('b', shallowcopy=True)() == [2, 3])

# Generated at 2022-06-12 21:17:26.571613
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    test_dict = {
        'a': ['a', 'b', 'c'],
        'b': {'a': 1, 'b': 2, 'c': 3},
        'c': {'a', 'b', 'c'},
        'd': 'a',
        'e': '',
        }
    # Test with no default and shallow copy behavior
    for key, value in test_dict.items():
        cliargs_inner = cliargs_deferred_get(key, default=None, shallowcopy=True)
        assert cliargs_inner() == value

    # Test with no default and no shallow copy behavior

# Generated at 2022-06-12 21:17:30.251369
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    _cliargs = CLIArgs({'foo': 'bar'})
    _globals = {'CLIARGS': _cliargs}
    _locals = {}


# Generated at 2022-06-12 21:17:41.325014
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """test_cliargs_deferred_get - Unit test for function cliargs_deferred_get

    This tests that the closure returned from ``cliargs_deferred_get()`` is
    actually returning the value from CLIARGS and not a static value.
    """
    from collections import OrderedDict, Counter, Set

    # Use an ordered dict for the test so we can predict what order the
    # elements will be returned in
    expected_value = OrderedDict((('foo', 'bar'), ('baz', 'quux')))
    CLIARGS['test_key'] = expected_value

    # We'll expect a copy of the value when cliargs_deferred_get is called
    expected_return = expected_value.copy()

    # Create the closure and test it

# Generated at 2022-06-12 21:17:48.304291
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': set()})

    # Make sure we copy explicitly
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('baz', shallowcopy=True)() == set()
    assert cliargs_deferred_get('baz', shallowcopy=True)() is not CLIARGS['baz']

# Generated at 2022-06-12 21:17:58.381153
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._data = {'abc': [1, 2, 3],
                     'bcd': {'e': 44},
                     'def': {'e': 44}.copy()}
    get_abc = cliargs_deferred_get('abc')
    get_def = cliargs_deferred_get('def')
    get_bcd = cliargs_deferred_get('bcd')
    get_zzz = cliargs_deferred_get('zzz')
    get_zzz_shallow = cliargs_deferred_get('zzz', shallowcopy=True)
    get_def_shallow = cliargs_deferred_get('def', shallowcopy=True)

    assert get_abc() == [1, 2, 3]
    assert get_def() == {'e': 44}
   

# Generated at 2022-06-12 21:18:16.470186
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    default_value = 'default value'
    key = 'key'
    cli_args = {key: 'value'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get(key, default_value)() == cli_args[key]
    _init_global_context({})
    assert cliargs_deferred_get(key, default_value)() == default_value

# Generated at 2022-06-12 21:18:22.578947
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get function

    This currently only tests that the ``_deferred_get`` function returns
    the same value as ``CLIArgs.get``

    It does not test that it is correctly returning a shallow copy
    """
    dummy_data = {'a': [1, 2, 3]}
    _init_global_context(dummy_data)
    assert cliargs_deferred_get('a')() == CLIARGS.get('a')

# Generated at 2022-06-12 21:18:27.841980
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})

    dg = cliargs_deferred_get('newkey', default=123)
    assert 123 == dg()
    dg = cliargs_deferred_get('newkey2', default=[])
    assert [] == dg()
    dg = cliargs_deferred_get('newkey3', default={})
    assert {} == dg()



# Generated at 2022-06-12 21:18:38.740855
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check(inp, copy, out):
        """Check basic functionality"""
        assert out == cliargs_deferred_get(inp, default=out, shallowcopy=copy)()
    def mock_cli(inp):
        """Create a mock CLIARGS object with the specified key and return the closure for that key"""
        global CLIARGS
        CLIARGS = GlobalCLIArgs.from_options(inp)
        return cliargs_deferred_get('foo')
    # Check default
    check('bar', False, 'bar')
    check('bar', True, 'bar')
    # Check basic cases
    check(None, False, None)
    check(True, False, True)
    check(0, False, 0)
    check(0.0, False, 0.0)

# Generated at 2022-06-12 21:18:48.364886
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def closure(*args, **kwargs):
        def inner():
            return args, kwargs
        return inner
    assert cliargs_deferred_get()() == ()
    assert cliargs_deferred_get('foo')() == ('foo',)
    assert cliargs_deferred_get('foo', 'bar')() == ('foo', 'bar')
    assert cliargs_deferred_get('foo', 'bar', 'baz')() == ('foo', 'bar', 'baz')
    assert cliargs_deferred_get('foo', 'bar', 'baz', wibble='wobble')() == (('foo', 'bar', 'baz'), dict(wibble='wobble'))

# Generated at 2022-06-12 21:18:59.563525
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCliArgs(GlobalCLIArgs):
        def __init__(self, value):
            self.value = value

        def get(self, key, default=None):
            return self.value

        def __contains__(self, key):
            return True

    orig = CLIARGS

    # Test the default value
    CLIARGS = TestCliArgs(None)
    result = cliargs_deferred_get(key='nosuchkey', default='default')()
    assert result == 'default', "%s != 'default'" % result

    # Test the value
    CLIARGS = TestCliArgs('foo')
    result = cliargs_deferred_get(key='foo')()
    assert result == 'foo', "%s != 'foo'" % result

    # Test shallow copy of list

# Generated at 2022-06-12 21:19:10.872988
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class DummyCliArgs:
        def __init__(self, args):
            for k,v in args.iteritems():
                setattr(self, k, v)
            self._orig_options = {}
        def get(self, key, default=None):
            return getattr(self, key, default)
    def test_get(key, def_opt, opts, shallowcopy, expected):
        global CLIARGS
        CLIARGS = DummyCliArgs(opts)
        getter = cliargs_deferred_get(key, def_opt, shallowcopy=shallowcopy)
        assert getter() == expected
        # make sure it hasn't changed the value in the cliargs
        assert CLIARGS.get(key) == opts[key]

    # test getting a key that doesn't exist
   

# Generated at 2022-06-12 21:19:18.694961
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'test1': [1, 2, 3], 'test2': 'abc', 'test3': 123})
    assert cliargs_deferred_get('test0', 'default')(), 'default'
    assert cliargs_deferred_get('test0', 'default', True)(), 'default'
    assert cliargs_deferred_get('test1', ['a', 'b'], True)(), [1, 2, 3]
    assert cliargs_deferred_get('test2', ['a', 'b'], True)(), 'abc'
    assert cliargs_deferred_get('test3', ['a', 'b'], True)(), 123

# Generated at 2022-06-12 21:19:27.074881
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('foo')() == None
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('foo', default=['baz'])() == 'bar'
    assert cliargs_deferred_get('foo', default='baz', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('foo', default=('baz',), shallowcopy=True)() == 'bar'
    CLIARGS['foo'] = ['bar']
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:19:34.027670
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_key = 'foo'
    test_value = ['bar', 'baz']
    CLIARGS = CLIArgs({test_key: test_value})
    value_getter = cliargs_deferred_get(test_key, shallowcopy=True)
    value = value_getter()
    assert value == test_value
    value[1] = 'boo'
    assert value != test_value

# Generated at 2022-06-12 21:19:59.373563
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get(key='_ansible_check_mode')() is False


# Generated at 2022-06-12 21:20:04.933314
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    test_cli_value = {'list': [1, 2, 3], 'set': set([1, 2, 3]), 'dict': {'a': 1, 'b': 2, 'c': 3}}
    _init_global_context(test_cli_value)
    assert cliargs_deferred_get('list')() == test_cli_value['list']
    assert cliargs_deferred_get('set')() == test_cli_value['set']
    assert cliargs_deferred_get('dict')() == test_cli_value['dict']
    assert cliargs_deferred_get('list', shallowcopy=True)() is not test_cli_value['list']
    assert cliargs_deferred_get('set', shallowcopy=True)() is not test_cli_value['set']

# Generated at 2022-06-12 21:20:16.907035
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'my_key': ['my', 'value']}
    CLIARGS = CLIArgs(cli_args)

    value = cliargs_deferred_get('my_key', shallowcopy=False)()
    assert value == ['my', 'value']
    assert value is cli_args['my_key']

    value = cliargs_deferred_get('my_key', shallowcopy=True)()
    assert value == ['my', 'value']
    assert value is not cli_args['my_key']

    cli_args['my_key'] = ['my', 'different', 'value']

    value = cliargs_deferred_get('my_key', shallowcopy=False)()
    assert value == ['my', 'different', 'value']

    value = cliargs_deferred_get

# Generated at 2022-06-12 21:20:26.921208
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # test case 1
    global CLIARGS
    CLIARGS = CLIArgs({'forks': 5})
    get_1 = cliargs_deferred_get('forks')
    assert 5 == get_1()
    # test case 2
    global CLIARGS
    CLIARGS = CLIArgs({'forks': 5, 'question': 'What is the Answer to the Ultimate Question of Life, the Universe, and Everything?'})
    get_2 = cliargs_deferred_get('question')
    assert 'What is the Answer to the Ultimate Question of Life, the Universe, and Everything?' == get_2()

# Generated at 2022-06-12 21:20:37.864645
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'a': 1, 'b': [2]})
    # Test for item retrieval
    assert cliargs_deferred_get('a')(CLIARGS) == 1
    assert cliargs_deferred_get('a')(cliargs) == 1
    # Test for tuple
    assert cliargs_deferred_get('b')(CLIARGS) == [2]
    assert cliargs_deferred_get('b')(cliargs) == [2]
    # Test for non-existent key with and without default
    assert cliargs_deferred_get('c')(CLIARGS) is None
    assert cliargs_deferred_get('c', default='foo')(CLIARGS) == 'foo'

# Generated at 2022-06-12 21:20:47.639565
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # Test standard operation of CLIARGS
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'

    # Test shallowcopy=True of CLIARGS
    CLIARGS['foo'] = ['bar', 'baz']
    CLIARGS['foo'].append('qux')
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz', 'qux']

    # Test shallowcopy=True of CLIARGS
    CLIARGS['foo'] = ['bar']
    CLIARGS['foo'].append('baz')
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']

# Generated at 2022-06-12 21:20:57.894149
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'a': 'b'})
    cliargs_value_deferred = cliargs_deferred_get('a')
    cliargs_default_deferred = cliargs_deferred_get('b', 'c')

    assert cliargs_value_deferred() == 'b'
    assert cliargs_default_deferred() == 'c'
    assert cliargs_value_deferred() is cliargs_value_deferred()
    assert cliargs_default_deferred() is cliargs_default_deferred()
    assert cliargs_value_deferred() is not cliargs_default_deferred()

    _init_global_context({'a': 'b', 'b': 'c'})
    assert cliargs_value_deferred() == 'b'

# Generated at 2022-06-12 21:21:09.199050
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from tests.unit.ansible_module_utils.common.context.test_context_objects import \
        TestCaseCliArgs, TestCaseGlobalCliArgs
    # Test with a regular CLIArgs
    cli_args = TestCaseCliArgs({})
    getter = cliargs_deferred_get('test_key')
    assert getter() is None

    cli_args.update({'test_key': 'test_value'})
    assert getter() is None

    # Test with a GlobalCLIArgs
    cli_args = TestCaseGlobalCliArgs({})
    getter = cliargs_deferred_get('test_key')
    assert getter() is None

    cli_args.update({'test_key': 'test_value'})
    assert getter() == 'test_value'



# Generated at 2022-06-12 21:21:20.435280
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Basic tests of cliargs_deferred_get"""
    cliargs = CLIArgs({})
    # Test that it can get a standard item
    assert cliargs.get('skip_tags', 'foo') == 'foo'
    assert cliargs_deferred_get('skip_tags', 'foo')() == 'foo'
    # Test that it can get from a default list
    cliargs['skip_tags'] = ['tag']
    cliargs.defaults['skip_tags'] = ['default_tag']
    assert cliargs['skip_tags'] == ['tag']
    assert cliargs.defaults['skip_tags'] == ['default_tag']
    assert cliargs_deferred_get('skip_tags')() == ['tag']
    assert cliargs_deferred_get('skip_tags', 'foo')

# Generated at 2022-06-12 21:21:31.893290
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from collections import namedtuple
    from ansible.module_utils._text import to_text
    cli_args = namedtuple('MockCLIArgs', 'test')([1, 2, 3])
    _init_global_context(cli_args)
    assert cliargs_deferred_get('test') == [1, 2, 3]
    assert cliargs_deferred_get('test', shallowcopy=True) == [1, 2, 3]
    assert cliargs_deferred_get('test', shallowcopy=False) == [1, 2, 3]
    assert cliargs_deferred_get('test', shallowcopy=False) is not cliargs_deferred_get('test', shallowcopy=False)


# Generated at 2022-06-12 21:22:02.638013
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=too-few-public-methods,too-many-instance-attributes,too-many-arguments
    class CliArgs(dict):
        """An object that acts like a dictionary for testing cliargs_deferred_get"""
        def __init__(self, args):
            super(CliArgs, self).__init__(args)
            self.initial_args = args
            self.args = args

        def get(self, key, default=None, shallowcopy=False):
            return self.args.get(key, default)

        def update(self, args):
            self.args.update(args)

    cliargs = CliArgs({'foo': 'bar', 'spam': 'eggs'})
    cliargs_get = cliargs_deferred_get('foo')

# Generated at 2022-06-12 21:22:14.284320
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    class MyFakeCliArgs(Mapping):
        def get(self, key, default=None):
            return {'a_mapping': {}, 'a_sequence': [], 'a_set': set()}.get(key, default)
        def __getitem__(self, key, default=None):
            return self.get(key, default)
        def __iter__(self):
            return iter({'a_mapping', 'a_sequence', 'a_set'})
        def __contains__(self, key):
            return key in self.__iter__
        def __len__(self):
            return 3

    CLIARGS = MyFakeCliArgs()

# Generated at 2022-06-12 21:22:23.752562
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeArgs:
        def get(self, key, default=None):
            return {
                'roles_path': 'path1:path2',
                'module_path': 'path3:path4',
                'extra_vars': {'bar': 'baz'},
                'vault_password_files': 'path1/foo path2/foo',
            }.get(key, default)

    fake_args = FakeArgs()

# Generated at 2022-06-12 21:22:35.952376
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test normal get behavior
    _init_global_context({'x': 4})
    assert cliargs_deferred_get('x')() == 4
    assert cliargs_deferred_get('x', shallowcopy=True)() == 4
    assert cliargs_deferred_get('y', default=None)() is None
    assert cliargs_deferred_get('y', default=None, shallowcopy=True)() is None
    # Test shallow copy
    _init_global_context({'x': [1, 2, 3]})
    assert cliargs_deferred_get('x')() == [1, 2, 3]
    assert cliargs_deferred_get('x', shallowcopy=True)() == [1, 2, 3]

# Generated at 2022-06-12 21:22:45.354385
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    result = cliargs_deferred_get('foo', 'bar')
    assert result == 'bar'
    arg = {'foo': 'baz'}
    _init_global_context(arg)
    assert cliargs_deferred_get('foo', 'bar')() == 'baz'
    assert cliargs_deferred_get('foo', 'bar', shallowcopy=True)() == 'baz'
    assert cliargs_deferred_get('baz', [])() == []
    assert cliargs_deferred_get('baz', [], shallowcopy=True)() == []
    assert cliargs_deferred_get('baz', {})() == {}
    assert cliargs_deferred_get('baz', {}, shallowcopy=True)() == {}
    assert cliargs_deferred

# Generated at 2022-06-12 21:22:56.396080
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function to fetch arguments from CLIARGS"""
    class TestArgs:
        """TestArgs class to mimic ansible.config.options.Options() class"""
        def __init__(self, test_arg):
            self.test_arg = test_arg

    test_arg = [1, 2, 3]

    cli_args = TestArgs(test_arg)
    cli_args.test_arg = test_arg
    _init_global_context(cli_args)

    # test for list values
    test_arg_func = cliargs_deferred_get('test_arg')
    value = test_arg_func()
    assert value == test_arg

    # test for dict value
    test_arg = {'testkey': 'testvalue'}
    cli_args.test_arg = test_arg


# Generated at 2022-06-12 21:23:05.857813
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_get():
        assert cliargs_deferred_get('foo') == 'bar'
        assert cliargs_deferred_get('foo', default='baz') == 'bar'
        assert cliargs_deferred_get('foo', shallowcopy=True) == 'bar'
        assert cliargs_deferred_get('foo', shallowcopy=False) == 'bar'

        assert cliargs_deferred_get('baz') == None
        assert cliargs_deferred_get('baz', default='baz') == 'baz'
        assert cliargs_deferred_get('baz', shallowcopy=True) == None
        assert cliargs_deferred_get('baz', shallowcopy=False) == None


# Generated at 2022-06-12 21:23:11.289405
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cli_args = {}
    _init_global_context(cli_args)
    assert CLIARGS.get('foo') is None
    assert CLIARGS.get('foo', 'bar') == 'bar'
    assert cliargs_deferred_get('foo') is None
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'

# Generated at 2022-06-12 21:23:20.616510
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'one': 1, 'two': 2, 'three': isinstance, 'four': [1, 2, 3], 'five': {'six': 6, 'seven': 7}, 'eight': set([8, 9, 10])}

    assert cliargs_deferred_get('one', 2)() == 1
    assert cliargs_deferred_get('ten', 10)() == 10
    assert cliargs_deferred_get('two', default=3)() == 2
    assert cliargs_deferred_get('eleven', default=11)() == 11

    assert cliargs_deferred_get('four')([]) == [1, 2, 3]
    assert cliargs_deferred_get('four', [])([]) == [1, 2, 3]

    assert cliargs_def

# Generated at 2022-06-12 21:23:24.866449
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options({'A': 'B'})
    assert cliargs_deferred_get('A')() == 'B'
    assert cliargs_deferred_get('C')() is None
    assert cliargs_deferred_get('C', default='D')() == 'D'

# Generated at 2022-06-12 21:24:03.402184
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    # Unit tests should clear the global context so that various unit tests can be
    # run in isolation.  This test acts as a simple sanity check that the context
    # is already cleared.
    assert CLIARGS == CLIArgs({})
    # Try getting 2 different types of values.  Get them deferredly and directly
    # to verify that we get the same thing both ways
    for test_value in (u'unicode', b'byte'):
        cliargs_deferred_value = cliargs_deferred_get('test', test_value, shallowcopy=False)()
        CLIARGS['test'] = test_value
        cliargs_value = CLIARGS.get('test')
        assert cliargs_deferred_value == test_value

# Generated at 2022-06-12 21:24:14.947928
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'hello': 'world'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('hello')() == 'world'
    assert cliargs_deferred_get('goodbye')(default='universe') == 'universe'
    assert cliargs_deferred_get('list')() is None
    cli_args['list'] = [1, 2, 3]
    assert cliargs_deferred_get('list')() == [1, 2, 3]
    assert cliargs_deferred_get('list', shallowcopy=True)() == [1, 2, 3]
    cli_args['set'] = {1, 2, 3}
    assert cliargs_deferred_get('set')() == {1, 2, 3}
   

# Generated at 2022-06-12 21:24:26.531240
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import list_of_strings_or_none
    from ansible.parsing.vault import VaultLib

    from ansible.module_utils.common.context_objects import GlobalCLIArgs
    from ansible.module_utils.ansible_release import __version__


# Generated at 2022-06-12 21:24:38.237215
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class DummyCliArgs(dict):
        def __init__(self):
            super(DummyCliArgs, self).__init__()
            self['foo'] = 'bar'
            self['baz'] = [1, 2, 3]

    def callback():
        return cliargs_deferred_get('foo')

    assert callback() == 'bar'

    def callback_default():
        return cliargs_deferred_get('spam', default='eggs')

    assert callback_default() == 'eggs'

    def callback_copy():
        return cliargs_deferred_get('baz', shallowcopy=True)

    first_copy = callback_copy()
    assert first_copy == [1, 2, 3]
    assert first_copy is not CLIARGS['baz']

    # Make sure we

# Generated at 2022-06-12 21:24:47.324286
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    global CLIARGS
    CLIARGS = CLIArgs({})
    # None
    assert cliargs_deferred_get('inventories', default=None)() is None
    # sequence
    assert cliargs_deferred_get('inventories', default=[])() == []
    CLIARGS.inventories = ['here.yml', 'there.yml']
    assert cliargs_deferred_get('inventories', default=None)() == ['here.yml', 'there.yml']
    # sequence, shallow copy
    assert cliargs_deferred_get('inventories', default=None, shallowcopy=True)() == ['here.yml', 'there.yml']

# Generated at 2022-06-12 21:24:57.979383
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    from ansible.module_utils.six.moves import cStringIO

    a_string = "abc"
    a_list = [1, 2, 3]
    a_set = {'a', 'b', 'c'}
    a_dict = {'a': 1, 'b': 2, 'c': 3}

    cli_args = {
        'a_string': a_string,
        'a_list': a_list,
        'a_set': a_set,
        'a_dict': a_dict,
    }

    _init_global_context(cli_args)

    assert a_string is cliargs_deferred_get('a_string')()