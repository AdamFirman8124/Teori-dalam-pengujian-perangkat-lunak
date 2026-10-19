

# Generated at 2022-06-12 21:15:07.433806
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    # No args
    assert cliargs_deferred_get('mykey')([]) is None
    # Defaults to non-None
    assert cliargs_deferred_get('mykey', 'myval')([]) == 'myval'
    assert cliargs_deferred_get('mykey', 42)([]) == 42
    # Key present
    assert cliargs_deferred_get('mykey')(['--mykey=val1']) == 'val1'
    assert cliargs_deferred_get('mykey')(['--mykey', 'val1']) == 'val1'

# Generated at 2022-06-12 21:15:13.120531
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSet
    global CLIARGS

    test_args = {}
    CLIARGS = CLIArgs(test_args)

    def set_args(*args, **kwargs):
        test_args.clear()
        test_args.update(*args, **kwargs)

    # Test basic get
    set_args(foo='foo')
    assert cliargs_deferred_get('foo')() == 'foo'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'foo'
    set_args(foo=42)
    assert cliargs_deferred_get('foo')() == 42
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 42

    # Test getting

# Generated at 2022-06-12 21:15:20.323123
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # If no cli_args are present, keys are missing, and no default is provided, raise KeyError
    fail_key = cliargs_deferred_get('test_missing_key')
    try:
        fail_key()
    except KeyError:
        pass
    else:
        raise AssertionError('Should have failed for missing key')

    # If no cli_args are present, non-missing keys use the default
    no_args = cliargs_deferred_get('test_present_key', default='test')
    assert no_args() == 'test'

    # After args have been passed in, non-missing keys use the present value
    present_key = cliargs_deferred_get('test_present_key', default='test')

# Generated at 2022-06-12 21:15:31.339360
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest
    from ansible.module_utils.common._collections_compat import Sequence, Mapping, Set
    from copy import copy, deepcopy
    def uniq_dict(d):
        return dict((k, id(v)) for k, v in d.items())
    def uniq_set(s):
        return set(id(x) for x in s)
    def uniq(s):
        if is_sequence(s):
            s = list(s)
            for idx, v in enumerate(s):
                s[idx] = id(v)
            return tuple(s)
        return id(s)


# Generated at 2022-06-12 21:15:39.459508
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Unit test
    key = 'ansible_foo'
    default = 'ansible_bar'
    expected = 'ansible_baz'

    def _test_shallowcopy(shallowcopy):
        expected_copy = expected
        if shallowcopy:
            expected_copy = expected[:]
            expected_copy.append('should not mutate original')
            expected.append('should not mutate copy')

        # Assert that the returned function does not take any parameters
        assert not cliargs_deferred_get(key, default, shallowcopy).__code__.co_argcount
        # Assert that the function returns the correct value
        assert cliargs_deferred_get(key, default, shallowcopy)() == expected_copy

        # Assert that the function returns the correct value when the key is not in the dict
        assert cl

# Generated at 2022-06-12 21:15:50.398644
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'test_key': [1, 2, 3], 'mapping_key': {'a': 1, 'b': 2}, 'set_key': {'a', 'b'}})
    assert cliargs_deferred_get('test_key')() == [1, 2, 3]
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('test_key')() == [1, 2, 3]
    assert cliargs_deferred_get('mapping_key')() == {'a': 1, 'b': 2}
    assert cliargs_deferred_get('mapping_key', shallowcopy=True)() == {'a': 1, 'b': 2}

# Generated at 2022-06-12 21:16:00.824092
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    Test for method cliargs_deferred_get

    This is a regression test for bug #23102 that the module_utils_importer
    import logic erroneously converts CLIARGS to a string causing the
    Mapping of the arguments to fail.  Therefore make sure we can pickle the
    cliargs_deferred_get method and that the reference to CLIARGS is not
    implicitly replaced by `str(CLIARGS)`
    """
    import pickle

    # The pickled form of cliargs_deferred_get should look like this
    # Note that this is the bytecode for python2 and python3.  Also note that
    # it has to match the code in cliargs_deferred_get exactly.  So if that
    # changes we need to update this pickled form

# Generated at 2022-06-12 21:16:07.832923
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'roles_path': 'foo', 'inventory': 'bar'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('roles_path', default='does_not_exist')() == 'foo'
    assert cliargs_deferred_get('does_not_exist', default='does_exist')() == 'does_exist'

# Generated at 2022-06-12 21:16:18.521261
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get returns the right values"""
    import copy
    import types
    cli_args = {'foo': 'bar', 'baz': [1, 2, 3], 'bam': {1: [1, 2, 3]}}
    # Make a copy so that our copy code doesn't modify the original
    expected_cli_args = copy.deepcopy(cli_args)
    _init_global_context(cli_args)

    # test retrieval of keys that exist
    for key in expected_cli_args:
        func = cliargs_deferred_get(key)
        assert isinstance(func, types.FunctionType)
        assert func() == expected_cli_args[key]


# Generated at 2022-06-12 21:16:22.854808
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # This is just a basic test that the function works the way we expect it to.  The functionality
    # will be tested thorougly in test_global_context
    CLIARGS.set('test_cliargs_deferred_get', 1)
    assert cliargs_deferred_get('test_cliargs_deferred_get')() == 1

# Generated at 2022-06-12 21:16:36.834224
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = GlobalCLIArgs({'v': 1,
                             'verbosity': 'vvvvvvvvv',
                             'private_key_file': '/path/to/ssh/key',
                             'foo': 'bar'})
    def_get = cliargs_deferred_get

    assert def_get('v')() == 1
    assert def_get('v', default=2)() == 1
    assert def_get('v', default=2, shallowcopy=True)() == 1

    assert def_get('verbosity')() == 'vvvvvvvvv'
    assert def_get('verbosity', default='vvvv')() == 'vvvvvvvvv'
    assert def_get('verbosity', default='vvvv', shallowcopy=True)() == 'vvvvvvvvv'

# Generated at 2022-06-12 21:16:45.253621
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = {'foo': 'bar', 'abc': 'def'}
    _init_global_context(cliargs)

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('abc')() == 'def'
    assert cliargs_deferred_get('def')('42') == '42'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('abc', shallowcopy=True)() == 'def'
    assert cliargs_deferred_get('def', '42', shallowcopy=True)() == '42'
    assert cliargs_deferred_get('foo', shallowcopy=True)() is not cliargs_deferred_get('foo')

# Generated at 2022-06-12 21:16:55.356708
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'one': 1, 'two': 'two', 'three': [1, 2, 3]})

    def test_get(key, expected, copy=False):
        assert cliargs_deferred_get(key, shallowcopy=copy)() == expected

    # test with a known value in CLIargs
    test_get('one', 1)
    # test with a known value that is not a mutable type
    test_get('two', 'two')
    # test with a known value that is a mutable type
    test_get('three', [1, 2, 3])
    # test with a known value that is a mutable type with shallowcopy
    test_get('three', [1, 2, 3], copy=True)
    # test with a known value that is a mutable type with shallowcopy
    test

# Generated at 2022-06-12 21:17:06.788275
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Args:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
        def __getattr__(self, name):
            return self.kwargs[name]

    def tdict(**kwargs):
        return kwargs

    cliargs = Args(a=1, b=[1,2,3], c={'foo': 'bar'}, d=tdict(foo='bar'))
    # Normal get
    assert cliargs_deferred_get('a')(cliargs) == 1
    assert cliargs_deferred_get('b')(cliargs) == [1,2,3]
    assert cliargs_deferred_get('c')(cliargs) == {'foo': 'bar'}

# Generated at 2022-06-12 21:17:17.227333
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    from ansible.utils.context_objects import CliArgs
    import copy
    import pytest
    my_options = {
        'foo': 'bar',
        'baz': ['1', '2'],
        'bop': {'a': 1, 'b': 2},
    }
    c = CliArgs(my_options)
    d = cliargs_deferred_get('foo')
    assert c['foo'] is d()

    # Both return shallow copies of the same object
    c_baz = c['baz']
    d_baz = d()
    assert c_baz is d_baz
    assert isinstance(c_baz, list)
    assert isinstance(d_baz, list)

# Generated at 2022-06-12 21:17:29.183292
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    from ansible.module_utils.common.collections import ImmutableDict
    from copy import copy

    # Test default is used
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('not-there')(), 'default value should be used'
    assert cliargs_deferred_get('not-there', default=42)(), 'default value should be used'

    # Test types are copied when shallowcopy is true
    CLIARGS = CLIArgs({'test-tuple': (1,2,3), 'test-dict': {'a': 1}})
    assert cliargs_deferred_get('test-tuple', shallowcopy=False)(), (1,2,3)

# Generated at 2022-06-12 21:17:40.634399
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'key_1': 'value', 'key_2': 'value_2'})

    # key exist
    closure = cliargs_deferred_get('key_1')
    assert closure() == 'value'

    # key is not exist
    closure = cliargs_deferred_get('key_3', default='default_value')
    assert closure() == 'default_value'

    # shallowcopy is True
    closure = cliargs_deferred_get('key_1', shallowcopy=True)
    value = closure()
    assert value == 'value'
    value = 'value_3'
    assert closure() == 'value'

    # shallowcopy is False
    closure = cliargs_deferred_get('key_1', shallowcopy=False)
    value = closure()

# Generated at 2022-06-12 21:17:51.801018
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # Test the default case
    CLIARGS = CLIArgs({})

    get_default = cliargs_deferred_get('test')
    assert get_default() is None

    get_with_default = cliargs_deferred_get('test', 42)
    assert get_with_default() == 42

    CLIARGS = CLIArgs({'test': 'one'})
    assert get_default() == 'one'
    assert get_with_default() == 'one'

    # Test shallowcopy
    get_shallowcopy = cliargs_deferred_get('test', shallowcopy=True)

    assert get_shallowcopy() == ['one']
    assert get_shallowcopy().pop() == 'one'

    assert get_shallowcopy() == []
    assert get_shallowcopy().pop

# Generated at 2022-06-12 21:18:01.386699
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS  # pylint: disable=locally-disabled, global-statement
    cli_args = {'foo': ['bar', 'baz']}
    cliargs = CLIArgs(cli_args)
    CLIARGS = cliargs
    test_val = cliargs_deferred_get('foo')
    new_value = test_val()
    assert new_value == ['bar', 'baz']
    assert new_value is not cli_args['foo']

    # Change the value in the cliargs and test the new value
    cliargs['foo'] = ['a', 'b', 'c']
    new_value = test_val()
    assert new_value == ['a', 'b', 'c']
    assert new_value is not cli_args['foo']

    # test shallow copy

# Generated at 2022-06-12 21:18:12.901171
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_values = {
        1: 1,
        'a': 'a',
        (1, 2, 3): (1, 2, 3),
        (1, [1, 2, 3], 3): (1, [1, 2, 3], 3),
        [1, 2, 3]: [1, 2, 3],
        [1, [1, 2, 3], 3]: [1, [1, 2, 3], 3],
        {1: 2}: {1: 2},
        {1: {2: 3}}: {1: {2: 3}},
        {1: [2, 3, 4]}: {1: [2, 3, 4]},
    }
    CLIARGS.update(test_values)

    for key, value in test_values.items():
        assert cliargs_deferred_get

# Generated at 2022-06-12 21:18:26.263226
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    Covers the case where CLIArgs is a ``GlobalCLIArgs`` object and
    where it is a ``CLIArgs`` object.
    """
    from copy import copy
    from ansible.module_utils.common.hashing import hash_params
    key = 'key'
    args = {'key': 'value'}
    gcliargs = GlobalCLIArgs.from_options(args)
    cliargs = CLIArgs(args)
    default = 'default'
    # Test getting a value from CLIArgs
    func = cliargs_deferred_get(key, default, shallowcopy=False)
    assert func() == args[key]
    func = cliargs_deferred_get(key, default, shallowcopy=True)
    # Test that we return a

# Generated at 2022-06-12 21:18:37.585180
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert callable(cliargs_deferred_get('test'))
    CLIARGS.test = 'tacocat'
    assert cliargs_deferred_get('test')() == 'tacocat'

    CLIARGS.list_test = ['cat', 'hat']
    assert cliargs_deferred_get('list_test', shallowcopy=True)() == ['cat', 'hat']

    CLIARGS.map_test = {'one': 1}
    assert cliargs_deferred_get('map_test', shallowcopy=True)() == {'one': 1}

    CLIARGS.set_test = set(('a', 'b'))
    assert cliargs_deferred_get('set_test', shallowcopy=True)() == set(('a', 'b'))

# Generated at 2022-06-12 21:18:47.517220
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Deferred:
        def __init__(self, inner):
            self.inner = inner

    def get(key):
        if key == 'key_shallow_copy_true':
            return Deferred(['a', 'b'])
        elif key == 'key_shallow_copy_false':
            return Deferred('abc')
        elif key == 'key_default':
            return Deferred(None)
        elif key == 'key_default_value':
            return Deferred(None)
        else:
            return None


# Generated at 2022-06-12 21:18:58.782023
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    def test_equal(expected, value):
        """Test if two values are equal"""
        assert expected == value, 'expected [%s] got [%s]' % (expected, value)

    # Test a non-sequence (string) without shallow copy
    cliargs = CLIArgs({'not_a_sequence': 'foo'})
    get_not_a_sequence = cliargs_deferred_get('not_a_sequence')
    test_equal('foo', get_not_a_sequence())

    # Test a non-sequence (string) with shallow copy
    get_not_a_sequence = cliargs_deferred_get('not_a_sequence', shallowcopy=True)
    test_equal('foo', get_not_a_sequence())
    get_

# Generated at 2022-06-12 21:19:09.440842
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get()"""

    def _test_value(expected, shallowcopy):
        assert expected == cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()

    cli_args = {'key': 'value',
                'key_shallow': [1, 2, 3],
                'key_deep': {'k': 'v'},
                }
    _init_global_context(cli_args)
    for key in cli_args:
        for shallowcopy in (True, False):
            _test_value(cli_args[key], shallowcopy)

    # Test defaults
    for key in ('missing_key', 'missing_shallow_key', 'missing_deep_key'):
        default = 'default'

# Generated at 2022-06-12 21:19:18.180920
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test with a stub version of ``CLIARGS``
    global CLIARGS

    class StubCliArgs(Mapping):
        def __init__(self, expected_key, expected_default, expected_shallowcopy,
                     return_value):
            self._expected_key = expected_key
            self._expected_default = expected_default
            self._expected_shallowcopy = expected_shallowcopy
            self._return_value = return_value

        def __getitem__(self, key):
            if key != self._expected_key:
                raise AssertionError(
                    'Expected key {0}, got {1}'.format(
                        self._expected_key, key
                    )
                )
            return self._return_value


# Generated at 2022-06-12 21:19:26.737761
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import sys
    import unittest
    from ansible.utils.context_objects import GlobalCLIArgs

    class GlobalCLIArgsTestCase(unittest.TestCase):
        def test_field_attributes(self):
            # Verify that the inner function returned behaves as expected
            # We test CLIARGS directly since the context object has already been created.
            # The function will have a closure around the context object which is expected
            self.assertIs(CLIARGS, cliargs_deferred_get('connection'))
            self.assertEqual(1, cliargs_deferred_get('start_at_task'))

            # Shallow copy affects the class of the returned value.  This is because we
            # want to avoid mutating the global context

# Generated at 2022-06-12 21:19:38.323444
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({
        'foo': ['bar', 'baz'],
        'bar': {'baz': 1},
        'baz': 'qux',
    })
    assert cliargs_deferred_get('foo')() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']
    assert cliargs_deferred_get('bar')() == {'baz': 1,}
    assert cliargs_deferred_get('bar', shallowcopy=True)() == {'baz': 1}
    assert cliargs_deferred_get('baz')() == 'qux'
    assert cliargs_deferred_get('baz', shallowcopy=True)() == 'qux'

# Generated at 2022-06-12 21:19:49.250029
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that a closure is created
    assert isinstance(cliargs_deferred_get('fake'), type(lambda: None))
    # Test the return value
    CLIARGS.update(name='value')
    assert cliargs_deferred_get('name')() == 'value'
    assert cliargs_deferred_get('name')(True) == 'value'

    # Test the return value of a default
    assert cliargs_deferred_get('no_key')() is None
    assert cliargs_deferred_get('no_key')(True) is None
    assert cliargs_deferred_get('no_key', 'default')() == 'default'
    assert cliargs_deferred_get('no_key', 'default')(True) == 'default'

    # Test that the shallowcopy works


# Generated at 2022-06-12 21:19:55.936153
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=too-many-locals, too-many-branches
    import pytest
    from ansible.plugins.loader import cli_args

    cli_args(dict(list_tasks=dict(type='bool', default=False)))

    _init_global_context(dict(list_tasks=False, list_hosts=True))

    # Check default
    default_val = 42
    deferred_get = cliargs_deferred_get('no_such_key', default=default_val)
    assert deferred_get() == default_val

    for key, cli_value in dict(list_tasks=True, list_hosts=False).items():
        deferred_get = cliargs_deferred_get(key)

        assert deferred_get() == cli_value

        new

# Generated at 2022-06-12 21:20:11.653935
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_equal(key, expected, shallowcopy=False):
        inner = cliargs_deferred_get(key, default=999, shallowcopy=shallowcopy)
        assert inner() == expected

    global CLIARGS
    CLIARGS = CLIArgs({'a': 'b', 'c': [1, 2, 3]})
    assert_equal('a', 'b')
    assert_equal('c', [1, 2, 3])
    assert_equal('d', 999)
    assert_equal('d', 999, shallowcopy=True)
    assert_equal('a', 'b', shallowcopy=True)
    assert_equal('c', [1, 2, 3], shallowcopy=True)
    CLIARGS = CLIArgs({})

# Generated at 2022-06-12 21:20:20.338679
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    def _test_deferred_get(options, key, expected, shallowcopy):
        """Test the deferred get with the given options, key and expected result"""
        global CLIARGS
        CLIARGS = CLIArgs(options)

        assert cliargs_deferred_get(key, shallowcopy=shallowcopy)() == expected

    test_options = {
        'diff': True,
        'listhosts': True,
    }

    _test_deferred_get(test_options, 'diff', True, False)

    test_options = {
        'listhosts': [],
        'inventory': './test/test_inventory',
    }

    _test_deferred_get(test_options, 'inventory', './test/test_inventory', False)
   

# Generated at 2022-06-12 21:20:29.914752
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    value = [1, 2, 3, 4]
    CLIARGS['foo'] = value
    assert cliargs_deferred_get('foo')() == value

    assert cliargs_deferred_get('foo', shallowcopy=True)() is not value
    assert cliargs_deferred_get('foo', shallowcopy=True)() == value

    value = [1, 2, 3, 4]
    CLIARGS['foo'] = copy.copy(value)
    assert cliargs_deferred_get('foo')() is value
    assert cliargs_deferred_get('foo', shallowcopy=True)() is not value
    assert cliargs_deferred_get('foo', shallowcopy=True)() == value

    value = {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-12 21:20:36.496346
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    dict_parm = dict(key="value")
    list_parm = ["value"]
    frozenset_parm = frozenset([1, 2, 3])
    non_shallow_copy_parm = CLIARGS

    # Note inner() is the closure around cliargs_deferred_get(key, default=None, shallowcopy=False)
    inner = cliargs_deferred_get("key", default=dict_parm)
    assert inner() is dict_parm
    global CLIARGS
    CLIARGS = CLIArgs(dict(key="value"))
    inner = cliargs_deferred_get("key", default=dict_parm)
    assert inner() is CLIARGS

    inner = cliargs_deferred_get("key", shallowcopy=True)
    assert inner() is CLIARGS

# Generated at 2022-06-12 21:20:47.030888
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(changed=True, original_only=set(['a', 'b']),
                              original_copy=dict(a=1, b=2)))
    assert cliargs_deferred_get('changed')() == True
    assert cliargs_deferred_get('original_only')() == set(['a', 'b'])
    assert cliargs_deferred_get('original_copy')() == dict(a=1, b=2)

    # Lookup of keys that don't exist returns the default
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default=None)() is None
    assert cliargs_deferred_get('foo', default=[1, 2, 3])() == [1, 2, 3]

# Generated at 2022-06-12 21:20:57.406491
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # GlobalCLIArgs.from_options exists to make it easier to test
    # cliargs_deferred_get.  It creates a unique object that is not
    # ``CLIARGS``, which is a singleton.
    cli_args = GlobalCLIArgs.from_options({'foo': 'bar'})
    assert cli_args.get('foo') == 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('foo', default=['baz'])() == 'bar'
    assert cliargs_deferred_get('nope', default=['baz'])() == ['baz']
    assert cliargs_deferred

# Generated at 2022-06-12 21:21:09.167463
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    global CLIARGS

    CLIARGS = CLIArgs({'foo': 'bar'})
    get = cliargs_deferred_get('foo')
    assert get() == 'bar'

    CLIARGS = CLIArgs({'foo': [1, 2, 3]})
    get = cliargs_deferred_get('foo', shallowcopy=True)
    assert get() == [1, 2, 3]
    assert get() is not CLIARGS['foo']

    CLIARGS = CLIArgs({'foo': [1, 2, 3]})
    get = cliargs_deferred_get('foo', shallowcopy=False)
    assert get() == [1, 2, 3]
    assert get() is CLIARGS['foo']


# Generated at 2022-06-12 21:21:19.620484
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3]})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('baz')() == [1, 2, 3]
    assert cliargs_deferred_get('baz', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('not-there')() is None
    assert cliargs_deferred_get('not-there', default='default')() == 'default'

# Generated at 2022-06-12 21:21:28.223418
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._store = {'foo': 'bar'}
    assert cliargs_deferred_get('foo')() == cliargs_deferred_get('foo')(), \
        "A closure should return the same value each time it's called"
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo')() is not cliargs_deferred_get('foo')(), \
        "The closure should return a new reference each time it's called"

# Generated at 2022-06-12 21:21:32.488478
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Foo(object):
        def __init__(self):
            self.cliargs = {'bar': 1}
    foo = Foo()
    inner = cliargs_deferred_get('bar')
    assert inner.__closure__[0].cell_contents is foo.cliargs
    assert inner() == 1



# Generated at 2022-06-12 21:21:59.404969
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TempCLIArgs(CLIArgs):
        def __init__(self):
            self.val = True

    # This instance is not the global
    temp_cli_args = TempCLIArgs()

    cli_arg_lookup_result = cliargs_deferred_get('val', default=False)
    assert cli_arg_lookup_result() is False

    # We expect the reference to CLIARGS to be frozen
    global CLIARGS
    CLIARGS = temp_cli_args

    cli_arg_lookup_result = cliargs_deferred_get('val', default=False)
    assert cli_arg_lookup_result() is True

    cli_arg_lookup_result = cliargs_deferred_get('val', default=False, shallowcopy=True)

# Generated at 2022-06-12 21:22:10.642096
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.context.cliargs import CLIARGS
    from ansible.module_utils.common.collections import list_of_strings

    old = CLIARGS

# Generated at 2022-06-12 21:22:20.696187
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check_return(val):
        return_value = inner()
        assert return_value == val

    global CLIARGS
    CLIARGS = CLIArgs({})
    check_return(None)

    # Set the value as if setting a default
    CLIARGS._cli_args['foo'] = None
    check_return(None)

    # Set a non-default value
    CLIARGS._cli_args['foo'] = 2
    check_return(2)
    check_return(2)

    # Set a non-default value which is a list
    CLIARGS._cli_args['foo'] = [1, 2, 3]
    check_return([1, 2, 3])
    check_return([1, 2, 3])

    # Set a non-default value which is a list with shallow copy
    CLIARGS._

# Generated at 2022-06-12 21:22:24.536539
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Foo:
        myvar = cliargs_deferred_get('myvar', 42)

    foo = Foo()
    assert foo.myvar == 42

    class Bar:
        myvar = cliargs_deferred_get('myvar', 42, shallowcopy=True)

    bar = Bar()
    assert bar.myvar == 42

# Generated at 2022-06-12 21:22:36.537853
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import is_sequence
    from ansible.utils.context_objects import GlobalCLIArgs
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options({'foo': {'bar': 'alpha', 'baz': 'beta'},
                                          'flip': ['flop'],
                                          'flips': ['flops'],
                                          'set': set(['one', 'two', 'three']),
                                          'frozset': frozenset(['one', 'two', 'three'])})

    ref = {'bar': 'alpha', 'baz': 'beta'}
    assert ref == cliargs_deferred_get('foo')()

# Generated at 2022-06-12 21:22:45.780991
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test with a value set and defaults set
    global CLIARGS
    CLIARGS = CLIArgs({'one': 1})
    assert cliargs_deferred_get('one')(), 1
    assert cliargs_deferred_get('one', default=2)(), 1
    assert cliargs_deferred_get('one', shallowcopy=True)(), 1
    assert cliargs_deferred_get('one', default=2, shallowcopy=True)(), 1

    # Test with a value set and defaults not set
    assert cliargs_deferred_get('one')(), 1
    assert cliargs_deferred_get('one', shallowcopy=True)(), 1

    # Test with no value set and defaults not set
    assert cliargs_deferred_get('two')(), None
    assert cliargs_

# Generated at 2022-06-12 21:22:56.925108
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assign(key, value):
        CLIARGS[key] = value
    assign("mykey", [1, 2, 3])
    assert cliargs_deferred_get("mykey", [])() == [1, 2, 3]
    assert cliargs_deferred_get("mykey", [], True)() == [1, 2, 3]

    assign("mykey", {1: 2, 3: 4})
    assert cliargs_deferred_get("mykey", {})() == {1: 2, 3: 4}
    assert cliargs_deferred_get("mykey", {}, True)() == {1: 2, 3: 4}

    assign("mykey", {1, 2, 3})

# Generated at 2022-06-12 21:23:06.269118
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Set up a context
    _init_global_context({'diff': False})

    # Create the deferred getters
    deferred_keys = ['diff', 'some_other_key']
    deferred_defaults = [False, 'foo']
    deferred_shallowcopy = [True, False]
    deferred_getters = []
    for key, default, shallowcopy in zip(deferred_keys, deferred_defaults, deferred_shallowcopy):
        deferred_getters.append(cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy))
    # Run the deferred getters
    deferred_values = []
    for i, getter in enumerate(deferred_getters):
        value = getter()
        assert value == deferred_defaults[i]

# Generated at 2022-06-12 21:23:13.710100
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test functionality of ``cliargs_deferred_get``"""
    global CLIARGS
    CLIARGS = CLIArgs({})
    for key, value in {
            'asdf': 3,
            'list': [],
            'dict': {},
            'tuple': (),
            'set': set(),
            }.items():
        func = cliargs_deferred_get(key, shallowcopy=False)
        CLIARGS[key] = value
        assert func() == value
        func = cliargs_deferred_get(key, shallowcopy=True)
        assert func() == value



# Generated at 2022-06-12 21:23:23.236558
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    context = CLIARGS
    context.foo = 'bar'
    assert cliargs_deferred_get('foo')(), 'bar'
    context.list = ['foo']
    assert cliargs_deferred_get('list', shallowcopy=True)(), ['foo']
    context.list[0] = 'changed'
    assert cliargs_deferred_get('list', shallowcopy=True)(), ['foo']
    context.set = set(['foo'])
    assert cliargs_deferred_get('set', shallowcopy=True)(), set(['foo'])
    context.set = set(['foo'])
    context.set.add('changed')
    assert set(cliargs_deferred_get('set', shallowcopy=True)()), set(['foo'])

# Generated at 2022-06-12 21:24:09.674291
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCliargs(object):
        def __init__(self, **kwargs):
            self._options = kwargs

        def get(self, key, default=None):
            return self._options.get(key, default)

        def __getitem__(self, key):
            return self._options[key]

    _init_global_context(TestCliargs(testlist=[1, 2, 3]))
    assert cliargs_deferred_get('testlist')() == [1, 2, 3]
    assert cliargs_deferred_get('testlist', shallowcopy=True)() == [1, 2, 3]

    _init_global_context(
        TestCliargs(testmapping={'a': 1, 'b': 2}, testset={3, 4, 5}))
    assert cl

# Generated at 2022-06-12 21:24:20.765024
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    from collections import namedtuple
    from ansible.module_utils.common.collections import recursive_diff
    from ansible.utils.context_objects import GlobalCLIArgs

    test_args = {'something': 'one', 'otherthing': ['foo', 'bar'], 'one_more': {'abc': 123, 'def': 456}}
    CLIARGS = GlobalCLIArgs(test_args)

    # Test basic operation
    test = cliargs_deferred_get('something')
    assert test() == 'one'

    # Test with a missing key and default set
    test = cliargs_deferred_get('unknown', 'a new value')
    assert test() == 'a new value'

    # Test with a missing key and default missing

# Generated at 2022-06-12 21:24:32.337495
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Correctly returns the value of an existing key
    CLIARGS.setdefault('foo', 'bar')
    assert cliargs_deferred_get('foo') == 'bar'

    # Correctly returns the default value of a non existent key
    CLIARGS.setdefault('foo', 'bar')
    assert cliargs_deferred_get('baz', default='qux') == 'qux'

    # Returns a shallow copy of an existing list key
    CLIARGS.setdefault('foo', [1, 2, 3])
    assert cliargs_deferred_get('foo', shallowcopy=True) == [1, 2, 3]
    assert cliargs_deferred_get('foo', shallowcopy=True) is not CLIARGS['foo']

    # Returns a shallow copy of an existing dict key

# Generated at 2022-06-12 21:24:44.203812
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # GlobalCLIArgs has been replaced by the time the test starts so we mostly test the
    # functionality of `cliargs_deferred_get`
    expected = dict(key3='value3',
                    key4=dict(k1=1, k2='2'),
                    key5=dict(k1=1, k2='2'),
                    )

    def assert_expected(d):
        for k, v in expected.items():
            assert d[k] == v

        # Test that sets and dicts are shallow copies
        d['key5']['k1'] = 1000
        assert expected['key5']['k1'] != d['key5']['k1']

        # Test that sequences are not shallow copies
        d['key4']['k1'] = 1000
        assert expected['key4']['k1']

# Generated at 2022-06-12 21:24:55.953388
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs(dict(foo='foo', bar=['bar1', 'bar2', 'bar3'], zoo={'zoo1': 'zoo1value', 'zoo2': 'zoo2value'}))
    assert cliargs_deferred_get('foo', default=None)() == 'foo'
    assert cliargs_deferred_get('bad', default=None)() == None
    assert cliargs_deferred_get('bar', default=None, shallowcopy=True)() == ['bar1', 'bar2', 'bar3']
    assert cliargs_deferred_get('bar', default=None, shallowcopy=False)() == ['bar1', 'bar2', 'bar3']