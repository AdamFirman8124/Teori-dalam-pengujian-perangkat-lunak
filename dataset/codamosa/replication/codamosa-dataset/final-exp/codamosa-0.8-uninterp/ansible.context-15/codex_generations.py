

# Generated at 2022-06-12 21:15:09.115607
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the returned function from cliargs_deferred_get"""
    from copy import deepcopy
    from types import FunctionType

    class CLIARGS(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    # Test with no default
    CLIARGS = CLIARGS(foo='bar', baz='FOO')
    retval = cliargs_deferred_get('foo')
    assert isinstance(retval, FunctionType)
    assert retval() == 'bar'
    CLIARGS = CLIARGS(foo='bar', baz='FOO')
    retval = cliargs_deferred_get('baz')
    assert retval() == 'FOO'

# Generated at 2022-06-12 21:15:15.710307
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Options:
        pass

    options = Options()
    options.key = "value"
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs(options)

    def check(expected, shallowcopy):
        closure = cliargs_deferred_get("key", "some_default", shallowcopy=shallowcopy)
        res = closure()
        assert res == expected

    check("value", False)
    check("value", True)
    check("some_other_default", False)
    check("some_other_default", True)

    CLIARGS = old_cliargs



# Generated at 2022-06-12 21:15:25.979013
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'string': 'value', 'list': [1, 2, 3], 'dict': {'key': 'value'}})

    assert cliargs_deferred_get('string')() == 'value'
    assert cliargs_deferred_get('list')() == [1, 2, 3]
    assert cliargs_deferred_get('dict')() == {'key': 'value'}

    assert cliargs_deferred_get('nosuchkey')() is None
    assert cliargs_deferred_get('nosuchkey', default='default')() == 'default'

    assert cliargs_deferred_get('string', shallowcopy=True)() == 'value'

# Generated at 2022-06-12 21:15:36.359541
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for cliargs_deferred_get"""
    global CLIARGS
    # Test getting a value that is not in the initial context
    test_args = {}
    CLIARGS = CLIArgs(test_args)
    assert cliargs_deferred_get('test', None)() is None

    # Test getting a value set in the initial context
    test_args = {'test': 'foo'}
    CLIARGS = CLIArgs(test_args)
    assert cliargs_deferred_get('test', None)() == 'foo'

    # Test getting a value that is not in the initial context and setting it.
    test_args = {}
    CLIARGS = CLIArgs(test_args)
    assert cliargs_deferred_get('test', None)() is None

# Generated at 2022-06-12 21:15:41.730502
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collection_compat import MutableSequence
    from ansible.module_utils.common._json_compat import JSONDecoder

    defm = object()
    def test_fun(key, default=defm, shallowcopy=False):
        func = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)
        return func()

    cli_args = {'ANSIBLE_JSON_DEFAULT_DECODER': JSONDecoder}
    _init_global_context(cli_args)

    assert CLIARGS.get('ANSIBLE_JSON_DEFAULT_DECODER') is JSONDecoder
    assert test_fun('ANSIBLE_JSON_DEFAULT_DECODER') is JSONDecoder

# Generated at 2022-06-12 21:15:52.536474
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import collections

    CLIARGS = CLIArgs({'a': []})  # empty list

    # Testing that we can get a value from a CliArgs
    assert cliargs_deferred_get('a')() == []

    # Testing that we get a default value if the key is not present
    assert cliargs_deferred_get('b', default=0)() == 0

    # Testing that we can get a shallow copy of a value
    a = []
    b = a
    assert a is b

    # We shall now test that we don't have a reference to a, but are copying the value
    c = cliargs_deferred_get('a', shallowcopy=True)()
    a.append(0)
    assert a == c

    # Test that we get a shallow copy for a sequence that is not a list or a tuple


# Generated at 2022-06-12 21:16:02.234748
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function ``cliargs_deferred_get``"""
    def _check_value(value):
        """Checks that the given value is the same as the one returned
        by ``cliargs_deferred_get``

        :arg value: Value to use when setting cliargs
        :returns: True if the given value matches the value returned by
            ``cliargs_deferred_get``
        """
        # Init global context
        _init_global_context({'foo': value})
        # Get the value from cliargs
        value_got = cliargs_deferred_get('foo')()
        # Check that the value_got matches the value given
        return value == value_got

    # Test for undefined value
    assert cliargs_deferred_get('bob')() is None

    # Test for value being

# Generated at 2022-06-12 21:16:12.816682
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""

    _init_global_context(dict(color='true'))

    closure = cliargs_deferred_get('color')
    assert closure() == 'true'

    _init_global_context(dict(color='false'))

    closure = cliargs_deferred_get('color')
    assert closure() == 'false'

    _init_global_context(dict(color=None))

    closure = cliargs_deferred_get('color')
    assert closure() is None

    closure = cliargs_deferred_get('color', 'true')
    assert closure() == 'true'

# Generated at 2022-06-12 21:16:23.105977
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """ Unit test for testing the cliargs_deferred_get function """
    def test_as_dict_callable():
        """ Unit test as a dict callable """
        assert CLIARGS == {'test_dict': {}}
        return CLIARGS.get('test_dict')
    def test_as_list_callable():
        """ Unit test as a list callable """
        assert CLIARGS == {'test_list': []}
        return CLIARGS.get('test_list')
    def test_as_set_callable():
        """ Unit test as a set callable """
        assert CLIARGS == {'test_set': set()}
        return CLIARGS.get('test_set')
    def test_as_str_callable():
        """ Unit test as a str callable """
        assert CLIAR

# Generated at 2022-06-12 21:16:33.578593
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.context_objects import FieldAttribute, FrozenDict
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.connection import ConnectionBase

    class FakeConnection(ConnectionBase):
        transport = 'fake'
        has_pipelining = True
        def __init__(self, *args, **kwargs):
            super(FakeConnection, self).__init__(*args, **kwargs)

    old_module_utils = module_utils_loader.all()

# Generated at 2022-06-12 21:16:44.830514
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import AttributeDict
    from ansible.module_utils._text import to_text
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE

    TEST_ARGS = CLIArgs(AttributeDict(test_value='test_value'))
    cliargs_default = cliargs_deferred_get('test_value', 'default')
    assert cliargs_default() == 'test_value'

    # Test with a different CLIArgs
    CLIARGS = TEST_ARGS
    cliargs_default = cliargs_deferred_get('test_value', 'default')
    assert cliargs_default()

# Generated at 2022-06-12 21:16:55.042629
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {"list_value": [1, 2, 3], "set_value": set([1, 2, 3]), "mapping_value": {"a": 1, "b": 2}, "scalar_value": 10}
    _init_global_context(cli_args)

    deferred_get_scalar = cliargs_deferred_get("scalar_value", default=None)
    assert deferred_get_scalar() == cli_args["scalar_value"]

    deferred_get_list = cliargs_deferred_get("list_value", shallowcopy=True)
    assert deferred_get_list() == cli_args["list_value"]

    deferred_get_set = cliargs_deferred_get("set_value", shallowcopy=True)
    assert deferred_get_

# Generated at 2022-06-12 21:17:06.545412
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence, Set
    # setup
    cli = CLIArgs({})
    cli.set_option(key='foo', value='bar')
    non_shallow_copy = cliargs_deferred_get(key='foo')
    shallow_copy = cliargs_deferred_get(key='foo', shallowcopy=True)

    # test non-shallow copy for sequences
    cli.set_option(key='foo', value=['a', 'b'])
    assert non_shallow_copy() == ['a', 'b']
    assert shallow_copy() == ['a', 'b']
    cli.set_option(key='foo', value=('a', 'b'))

# Generated at 2022-06-12 21:17:12.395707
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_cli_args = {
        "one": 1,
        "not_default": "foo",
    }
    _init_global_context(test_cli_args)
    assert cliargs_deferred_get('one')() == 1
    assert cliargs_deferred_get('not_default')() == "foo"
    assert cliargs_deferred_get('not_default')(shallowcopy=True) == "foo"
    assert cliargs_deferred_get('not_default')(shallowcopy=False) == "foo"
    # Key not in result from cliargs_deferred_get()
    assert cliargs_deferred_get('two')() is None
    assert cliargs_deferred_get('two')(default="bar") == "bar"
    # Key not in result

# Generated at 2022-06-12 21:17:20.772833
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the deferred get function"""
    class Context(dict):
        """Base class to mock CLIARGS"""

    class CLIContext(Context):
        """Mock CLIARGS"""
        shallowcopy = False

    orig_cliargs = CLIARGS

# Generated at 2022-06-12 21:17:32.051545
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""

    # Test case: no special treatment for shallow copy
    TEST_KEY = 'test_key'
    TEST_VALUE = 'test_value'
    def test_inner_no_shallow_copy():
        """Test case for ``cliargs_deferred_get`` with no shallow copy"""
        global CLIARGS
        TEST_CLI_ARGS = {TEST_KEY: TEST_VALUE}
        CLIARGS = CLIArgs(TEST_CLI_ARGS)
        inner_function = cliargs_deferred_get(TEST_KEY)
        assert inner_function() == TEST_VALUE
        assert inner_function() == inner_function()
        CLIARGS = CLIArgs({})
    test_inner_no_shallow_copy()

    # Test case:

# Generated at 2022-06-12 21:17:42.548461
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Using a class instead of a function since pylint doesn't like just defining cliargs
    # as a global.  There's probably a better way to do this...
    class CliArgs(object):
        def __init__(self, args_dict):
            self.args_dict = args_dict

        def __getitem__(self, key):
            return self.args_dict[key]

        def get(self, key, default=None):
            return self.args_dict.get(key, default)

    global CLIARGS

    # just a default
    CLIARGS = CliArgs({})
    cli_args_get = cliargs_deferred_get('random', default='ok')
    assert cli_args_get() == 'ok'

    # copy

# Generated at 2022-06-12 21:17:53.010034
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    class CliArgs():
        def __init__(self, args):
            self.args = args

        def get(self, key, default=None):
            return self.args.get(key, default=default)

    global CLIARGS


    args = {'key1': 1, 'key2': [1,2,3], 'key3': {'a': 1,'b': 2}, 'key4': (1,2,3), 'key5': {'a','b','c'}}
    original = copy.deepcopy(args)
    CLIARGS = CliArgs(args)

    check = cliargs_deferred_get('key1')
    assert check() == 1

    check = cliargs_deferred_get('key1', shallowcopy=True)
    assert check() == 1

   

# Generated at 2022-06-12 21:18:02.301247
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert CLIARGS.get('foo') is None
    assert cliargs_deferred_get('foo')() is None

    old_cliargs = CLIARGS
    try:
        CLIARGS = CLIArgs({'foo': 'bar'})
        assert CLIARGS.get('foo') == 'bar'
        assert cliargs_deferred_get('foo')() == 'bar'
    finally:
        CLIARGS = old_cliargs

    old_cliargs = CLIARGS
    try:
        CLIARGS = CLIArgs({'foo': 'bar'})
        assert CLIARGS.get('foo') == 'bar'
        assert cliargs_deferred_get('foo', default='fie')() == 'bar'
    finally:
        CLIARGS = old_cliargs

    old_cliargs = CLIAR

# Generated at 2022-06-12 21:18:06.204405
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    assert cliargs_deferred_get('foo', default=5)() == 5
    CLIARGS['foo'] = 5
    assert cliargs_deferred_get('foo', default=5)() == 5

# Generated at 2022-06-12 21:18:20.999326
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    # pylint: disable=unused-variable
    test_default_value = 5
    test_key = 'test_key'
    test_value = [1, 2, 3]
    cli_args = {test_key: test_value}
    _init_global_context(cli_args)

    # Verify that we can get a value from the cliargs
    assert cliargs_deferred_get(test_key)() == test_value

    # Verify that we get back the default
    assert cliargs_deferred_get(test_key, default=test_default_value)() == test_default_value

    # Verify that we get back a copy of the value when we want a shallowcopy

# Generated at 2022-06-12 21:18:26.010615
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert isinstance(cliargs_deferred_get('test1')(), type(None))
    CLIARGS = CLIArgs({'test1': 'foo'})
    assert cliargs_deferred_get('test1')() == 'foo'
    assert cliargs_deferred_get('test1', default='bar')() == 'foo'
    assert cliargs_deferred_get('test1', default='bar', shallowcopy=True)() == 'foo'

# Generated at 2022-06-12 21:18:34.378921
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['a'] = 1
    check = cliargs_deferred_get('a', 42)
    assert check() == 1
    check = cliargs_deferred_get('b', 42)
    assert check() == 42
    check = cliargs_deferred_get('a', shallowcopy=True)
    assert check() == 1
    CLIARGS['a'] = [1, 2, 3]
    check = cliargs_deferred_get('a', shallowcopy=True)
    assert check() == [1, 2, 3]

# Generated at 2022-06-12 21:18:44.953428
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    cli_args = dict(foo='bar', bardict=dict(baz='boo'), barlist=[1, 2, 3])

    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('barlist')() == [1, 2, 3]
    assert cliargs_deferred_get('barlist', shallowcopy=True)() == [1, 2, 3]  # shallowcopy is ignored on non-dictionaries
    assert cliargs_deferred_get('barlist', shallowcopy=True)() == [1, 2, 3]  # shallowcopy is ignored on non-dictionaries
    assert cliargs_deferred_get('baz')() is None
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:18:55.616850
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    expected = {'foo': 'bar'}
    cli_args = dict(foo='bar', baz='bam')
    _init_global_context(cli_args)
    output = cliargs_deferred_get('foo')().copy()
    assert output == expected, 'Wrong value returned: expected: {!s} actual: {!s}'.format(expected, output)
    output = cliargs_deferred_get('bar', default='bam')().copy()
    expected = 'bam'
    assert output == expected, 'Wrong value returned: expected: {!s} actual: {!s}'.format(expected, output)
    assert output is not 'bam', 'Should have returned a copy of the value not the value itself'

# Generated at 2022-06-12 21:19:02.515859
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    class CliArgs(Mapping):
        def __getitem__(self, key):
            return key

        def __contains__(self, key):
            return True

        def __iter__(self):
            return iter(('not', 'a', 'dict'))

        def __len__(self):
            return 0

    CLIARGS = CliArgs()

    assert cliargs_deferred_get('not_a_dict', shallowcopy=False) == 'not_a_dict'

    assert cliargs_deferred_get('not_a_dict', shallowcopy=True) == 'not_a_dict'



# Generated at 2022-06-12 21:19:13.934358
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': 'quux'})

    # test value found
    assert 'bar' == cliargs_deferred_get('foo')()
    # test default
    assert None is cliargs_deferred_get('nonexistent')()
    # test default value
    assert 'bar' == cliargs_deferred_get('nonexistent', 'bar')()
    # test value found
    assert 'quux' == cliargs_deferred_get('baz')()

    # test sequence shallowcopy
    CLIARGS['foo'] = ['a']
    assert ['a'] == cliargs_deferred_get('foo', shallowcopy=True)()
    assert ['a'] != cliargs_deferred_get('foo')()
   

# Generated at 2022-06-12 21:19:24.588302
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the ``cliargs_deferred_get`` function"""
    global CLIARGS

    CLIARGS = CLIArgs({'foo': {'bar': {'baz': 'shallow_copy'}}})
    cliargs_deferred_get_closure = cliargs_deferred_get('foo', shallowcopy=True)
    assert cliargs_deferred_get_closure() == {'bar': {'baz': 'shallow_copy'}}
    assert cliargs_deferred_get_closure()['bar'] == {'baz': 'shallow_copy'}

    CLIARGS = CLIArgs({'foo': ['sequence']})
    cliargs_deferred_get_closure = cliargs_deferred_get('foo', shallowcopy=True)
    assert cliargs_deferred_get_closure()

# Generated at 2022-06-12 21:19:31.250984
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check(value):
        # The function we test should be the same between calls
        assert cliargs_deferred_get('a') is cliargs_deferred_get('a')
        # The function should not be directly bound to CLIARGS
        assert cliargs_deferred_get('a') is not cliargs_deferred_get('a', default=default)
        return value
    for default in (None, 1, False, 'b', [], {}, set()):
        for shallowcopy in (False, True):
            for value in (None, 1, False, 'b', [], {}, set()):
                # Make a different CLIARGS for this test
                cli_args = CLIArgs({})
                cli_args['a'] = value
                _init_global_context(cli_args)

                #

# Generated at 2022-06-12 21:19:38.642945
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    data = ['foo', 'bar']
    CLIARGS.update({'foo': data})
    assert cliargs_deferred_get('foo') is data
    assert cliargs_deferred_get('foo', shallowcopy=True) is not data
    assert cliargs_deferred_get('foo', shallowcopy=True) == data
    assert cliargs_deferred_get('bar') is None
    assert cliargs_deferred_get('bar', default='cheeky') == 'cheeky'

# Generated at 2022-06-12 21:19:55.631168
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    _init_global_context({'v': {'a': 5, 'b': ['c', 'd']}, 'w': set()})
    f = cliargs_deferred_get('v', 'default', True)
    assert f() == {'a': 5, 'b': ['c', 'd']}
    f = cliargs_deferred_get('v:a', 'default')
    assert f() == 5
    f = cliargs_deferred_get('v:b', 'default')
    assert f() == ['c', 'd']
    f = cliargs_deferred_get('w', 'default')
    assert f() == set()
    assert f() is f()

    CLIARGS['v']['a'] = 6
    assert f() == set()
    assert f()

# Generated at 2022-06-12 21:20:02.445229
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """This is a test of the function cliargs_deferred_get"""
    class AnsibleContext:
        """ Simple fake class to allow us to switch out the global var """
        def __init__(self, cliargs):
            self.cliargs = cliargs
        def __getitem__(self, key):
            return self.cliargs[key]
    # Allocating the global variable and keeping track of it in the local variable
    cliargs = AnsibleContext({'v': ['This is a test'], 'vv': ['This is a test'], 'vvv': 'This is a test'})
    class FakeCLIARGS:
        """ Simple fake class to allow us to switch out the global var """
        def __init__(self, cliargs):
            self.cliargs = cliargs

# Generated at 2022-06-12 21:20:10.782318
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})

    default = 'default_value'
    cli_key = cliargs_deferred_get('some_key', default=default)
    assert cli_key() == default
    cli_key = cliargs_deferred_get('some_key')
    assert cli_key() is None

    set_value = 123
    CLIARGS = CLIArgs({'some_key': set_value})
    assert cli_key() == set_value

    # Test shallowcopy=True
    seq = ['a', 'b', 'c']
    CLIARGS = CLIArgs({'some_key': seq})
    cli_key = cliargs_deferred_get('some_key', shallowcopy=True)
    assert cli_key() is not seq


# Generated at 2022-06-12 21:20:20.174441
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test unset key
    assert cliargs_deferred_get('test')(), None
    assert cliargs_deferred_get('test', default='foo')(), 'foo'

    # Test set key
    CLIARGS['test'] = 'bar'
    assert cliargs_deferred_get('test')(), 'bar'
    assert cliargs_deferred_get('test', default='foo')(), 'bar'

    # Test shallow copy
    CLIARGS['test'] = [1, 2, 3]
    assert cliargs_deferred_get('test')(), [1, 2, 3]
    value = cliargs_deferred_get('test', shallowcopy=True)()
    assert value, [1, 2, 3]
    assert value is not CLIARGS['test']

    CLI

# Generated at 2022-06-12 21:20:29.791755
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # If we are testing, this will already be setup with a mock
    global CLIARGS
    assert CLIARGS.__class__.__name__ == 'GlobalCLIArgs', "%s != %s" % (CLIARGS.__class__.__name__, 'GlobalCLIArgs')
    # Hardcode a dictionary to test with
    for k, v in (('list', ['one', 'two']), ('tuple', ('one', 'two')), ('dict', {'one': 'two'}), ('set', {'one'})):
        CLIARGS[k] = v
        assert cliargs_deferred_get(k, shallowcopy=True) == v
        assert cliargs_deferred_get(k) == v
        if isinstance(v, (Mapping, Set)):
            assert cliargs_def

# Generated at 2022-06-12 21:20:39.575684
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Ensure that the function works"""
    args = {'1': [1, 2], '2': {'foo': 'bar'}}
    global CLIARGS
    CLIARGS = CLIArgs(args)
    assert cliargs_deferred_get('1')() == args['1']
    assert cliargs_deferred_get('2')() == args['2']
    assert cliargs_deferred_get('1', shallowcopy=True)() == args['1'][:]  # list shallow copy
    assert cliargs_deferred_get('2', shallowcopy=True)() == args['2'].copy()  # dict shallow copy

    # 3 is not in args
    assert cliargs_deferred_get('3')() is None

# Generated at 2022-06-12 21:20:44.743134
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class DummyClass:
        pass

    c = DummyClass()
    c.a = 1
    c.b = 'foo'
    c.c = [1, 2, 3]
    c.d = (1, 2, 3)
    c.e = {'foo': 1, 'bar': 2, 'baz': 3}
    c.f = set((1, 2, 3, 4))

    def _test_get_value(func, value):
        assert func() == value

    def _test_set_value(func, value):
        func()
        assert CLIARGS[key] == value

    def _test_shallow_copy_value(func, value):
        func()
        assert CLIARGS[key] == value
        value[0] = 'foo'
        assert CLIARGS[key]

# Generated at 2022-06-12 21:20:55.124329
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CliArgs
    global CLIARGS
    CLIARGS = CliArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo2')() is None
    assert cliargs_deferred_get('foo2', 'baz')() == 'baz'

    CLIARGS = CliArgs({'foo': ['bar', 'baz']})
    assert cliargs_deferred_get('foo', default=['baz'])() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']

# Generated at 2022-06-12 21:21:04.687820
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get

    This function is not tested directly but is run as part of the ``CliArgs`` unit tests
    """
    global CLIARGS

    # Do not use the singleton version.  The Singleton is only created once the program has
    # actually parsed the args
    CLIARGS = CLIArgs({'foo': ['bar', 'baz']})
    result = cliargs_deferred_get('foo')()
    assert result == ['bar', 'baz']

    result = cliargs_deferred_get('foo', shallowcopy=True)()
    assert result == ['bar', 'baz']
    result.append('fee')
    assert CLIARGS['foo'] == ['bar', 'baz', 'fee']

# Generated at 2022-06-12 21:21:12.201072
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': ['a', 'b', 'c'], 'qux': {'one': 1, 'two': 2}})

    assert cliargs_deferred_get('foo')(), 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)(), 'bar'

    assert cliargs_deferred_get('baz')(), ['a', 'b', 'c']
    assert cliargs_deferred_get('baz', shallowcopy=True)(), ['a', 'b', 'c']

    assert cliargs_deferred_get('qux')(), {'one': 1, 'two': 2}

# Generated at 2022-06-12 21:21:30.868354
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar', 'baz')() == 'baz'
    CLIARGS.update({'bar': 'baz'})
    assert cliargs_deferred_get('bar', 'baz')() == 'baz'
    assert cliargs_deferred_get('bar')() == 'baz'
    assert cliargs_deferred_get('bar', 'baz', shallowcopy=True)() == 'baz'
    assert cliargs_deferred_get('bar', shallowcopy=True)() == 'baz'

# Generated at 2022-06-12 21:21:38.590654
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from copy import copy, deepcopy
    global CLIARGS

    # create default object, check default value
    CLIARGS = GlobalCLIArgs({'defaults': {'key1': 'value1', 'key2': 'value2'}, 'DEFAULT_MODULE_PATH': '/some/path'})
    assert cliargs_deferred_get('key1')() == 'value1'
    assert cliargs_deferred_get('key2')() == 'value2'

    # check default value if key not found in context object
    assert cliargs_deferred_get('key3', 'value3')() == 'value3'

    # check that value is not shallowcloned if shallowcopy is False

# Generated at 2022-06-12 21:21:46.370638
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args_orig = CLIARGS
    CLIARGS = CLIArgs({'value': 'blah'})
    assert cliargs_deferred_get('value') == 'blah'
    assert cliargs_deferred_get('value', default='foo') == 'blah'
    assert cliargs_deferred_get('novalue', default='foo') == 'foo'
    assert cliargs_deferred_get('novalue', default=['foo']) == ['foo']
    assert cliargs_deferred_get('novalue', default=['foo'], shallowcopy=False) == ['foo']
    assert cliargs_deferred_get('novalue', default=['foo'], shallowcopy=True) == []

# Generated at 2022-06-12 21:21:57.495530
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    class _GlobalCliArgs(dict):
        def __init__(self):
            super(_GlobalCliArgs, self).__init__()
            self.set_called = False

        def __setitem__(self, key, value):
            self.set_called = True

    class_arg = _GlobalCliArgs()

    CLIARGS = class_arg

    # Test simple retrieval
    func = cliargs_deferred_get('foo', 'bar')
    assert (class_arg.set_called == False)
    assert (func() == 'bar')

    # Test setting
    class_arg['foo'] = 'zod'
    assert (func() == 'zod')

    # Test cli_args_deferred_get() can be used before cli_args is set to a value
   

# Generated at 2022-06-12 21:22:08.205867
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get works as expected"""
    from ansible import context
    from unittest import TestCase

    class TestCliargsDeferredGet(TestCase):
        """Test the functionality of cliargs_deferred_get"""
        def setUp(self):
            context.CLIARGS = context.CLIArgs({'verbosity': 0, 'foo': True, 'bar': True, 'baz': False,
                                               'str': 'something', 'lst': [1, 2, 3], 'dict': {'a': 1, 'b': True}})

        def tearDown(self):
            context.CLIARGS.clear()

        def test_get_raw(self):
            """A normal get"""

# Generated at 2022-06-12 21:22:18.621815
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _test_get(test_case, arg_default, arg_value, expected_value, expected_type, shallowcopy):
        class TestArgs(CLIArgs):
            default_value = arg_default

        global CLIARGS
        CLIARGS = TestArgs({'value': arg_value})
        deferred_get = cliargs_deferred_get('value', default=TestArgs.default_value,
                                            shallowcopy=shallowcopy)
        value = deferred_get()

        if is_sequence(arg_default):
            test_case.assertEqual(expected_value, value)
            test_case.assertTrue(type(value) is expected_type)
            if expected_type is list:
                # make sure subsequent modification of the returned list does not alter
                # the value in the cli args
                value.append

# Generated at 2022-06-12 21:22:26.720407
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})

    # Test when the key exists in CLIARGS
    cliargs_deferred_get_closure = cliargs_deferred_get('foo', default='bar')
    CLIARGS['foo'] = 'foo'
    assert cliargs_deferred_get_closure() == 'foo'
    CLIARGS['foo'] = [1,2,3]
    assert cliargs_deferred_get_closure(shallowcopy=True) == [1,2,3]
    assert cliargs_deferred_get_closure() == [1,2,3]
    CLIARGS['foo'] = {'a': 1}
    assert cliargs_deferred_get_closure(shallowcopy=True) == {'a': 1}
    assert cliargs

# Generated at 2022-06-12 21:22:38.499388
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the function cliargs_deferred_get"""
    global CLIARGS
    CLIARGS.update(dict(
        str1='foo',
        str2='bar',
        list1=['foo', 'bar'],
        list2=['baz'],
    ))
    assert cliargs_deferred_get('str1')() == 'foo'
    assert cliargs_deferred_get('str2')() == 'bar'
    assert cliargs_deferred_get('list1')().sort() == ['foo', 'bar'].sort()
    assert cliargs_deferred_get('list2')().sort() == ['baz'].sort()
    CLIARGS.clear()


# Generated at 2022-06-12 21:22:47.049014
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-argument
    def cli_args(**kwargs):
        return kwargs
    _init_global_context(cli_args())
    assert cliargs_deferred_get('foo') == None
    _init_global_context(cli_args(foo=True))
    assert cliargs_deferred_get('foo') == True
    _init_global_context(cli_args(foo='bar'))
    assert cliargs_deferred_get('foo') == 'bar'
    _init_global_context(cli_args(foo=[1, 2, 3]))
    assert cliargs_deferred_get('foo') == [1, 2, 3]
    assert cliargs_deferred_get('foo', shallowcopy=True) == [1, 2, 3]

# Generated at 2022-06-12 21:22:57.880824
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.data = {'foo': ['bar','baz','qux']}
    assert cliargs_deferred_get('foo')() == ['bar','baz','qux']
    assert cliargs_deferred_get('bar')(default='qux') == 'qux'
    # Test the shallowcopy functionality
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar','baz','qux']
    CLIARGS.foo[1] = 'testing'
    assert CLIARGS.foo == ['bar', 'testing', 'qux']
    # Because of the shallow copy, the original value is still the same
    assert cliargs_deferred_get('foo')() == ['bar','baz','qux']

# Generated at 2022-06-12 21:23:16.147476
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    def make_context(**context):
        global CLIARGS
        CLIARGS = CLIArgs(context)

    def has_context():
        assert CLIARGS.keys()

    def check_value(key, expected_value, shallowcopy=False):
        cliargs_value = cliargs_deferred_get(key, shallowcopy=shallowcopy)()
        assert cliargs_value == expected_value

    # Ensure that we start with a context populated with data
    make_context(a='b', c='d')
    has_context()

    # First key will be in CLIARGS
    check_value('a', 'b')

    # First key will not be in CLIARGS, returns the default
    check_value('z', 'default')

    # Request the default which is the value in CLIARGS
    check_

# Generated at 2022-06-12 21:23:25.662235
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import ansible.utils.context_objects as co

    def run_test(should_get_default=False, key=None, default=None, shallowcopy=False,
                 should_raise=False, should_call=False, should_be_default=False,
                 should_shallow_copy=False):
        if should_get_default:
            if shallowcopy:
                input_default = default[:]
            else:
                input_default = default
            cliargs = co.CLIARGS
            co.CLIARGS = co.CLIArgs({})
            func = co.cliargs_deferred_get(key, default=input_default, shallowcopy=shallowcopy)
            if should_raise:
                with pytest.raises(KeyError):
                    func()
            else:
                assert func() == default

# Generated at 2022-06-12 21:23:34.578600
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'foo': 'bar', 'baz': [1, 2, 3]})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz', [])() == [1, 2, 3]
    assert cliargs_deferred_get('baz', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('foo', [])() == 'bar'
    assert cliargs_deferred_get('missingkey', [])() == []
    assert cliargs_deferred_get('missingkey', ['value'])() == ['value']
    assert cliargs_deferred_get('missingkey', None)() is None

# Generated at 2022-06-12 21:23:44.591347
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.defaults['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', None)() == 'bar'
    assert cliargs_deferred_get('foo', 'baz')() == 'bar'
    assert cliargs_deferred_get('bar')() is None
    assert cliargs_deferred_get('bar', None)() is None
    assert cliargs_deferred_get('bar', 'baz')() == 'baz'

    CLIARGS.defaults['foo'] = ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']

# Generated at 2022-06-12 21:23:51.762905
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Simple test for the closure
    cliargs_dict = {'foo': {'bar': 'baz'}, 'bob': 42, 'sally': [1, 2, 3]}
    _init_global_context(cliargs_dict)
    assert 42 == cliargs_deferred_get('bob', default=1)
    assert 3 == cliargs_deferred_get('sally')[-1]
    assert 'baz' == cliargs_deferred_get('foo')['bar']
    assert 42 == cliargs_deferred_get('bob')
    assert cliargs_deferred_get('foo')['bar'] == cliargs_dict['foo']['bar']
    assert 42 == cliargs_deferred_get('bob', shallowcopy=True)
    assert 3 == cli

# Generated at 2022-06-12 21:24:02.965754
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({"a": [1], "b": {"foo": "bar"}})
    assert cliargs_deferred_get("a")() == [1]
    assert cliargs_deferred_get("b")() == {"foo": "bar"}
    assert cliargs_deferred_get("a", shallowcopy=True)() == [1]
    assert cliargs_deferred_get("b", shallowcopy=True)() == {"foo": "bar"}
    assert cliargs_deferred_get("a", default=['default'])() == ['default']
    assert cliargs_deferred_get("b", default=['default'])() == ['default']
    assert cliargs_deferred_get("a", shallowcopy=True, default=[])() == []


# Generated at 2022-06-12 21:24:14.459594
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Indirectly test that the inner function closure works correctly
    _init_global_context({'v': 1, 'other': [1, 2, 3], 'mapping': {'foo': 'bar'}})
    assert cliargs_deferred_get('v', shallowcopy=True)() == 1
    assert cliargs_deferred_get('v', shallowcopy=False)() == 1
    # Indirectly test that the default works correctly
    assert cliargs_deferred_get('missing', default=2, shallowcopy=True)() == 2
    # Test shallow copy works with a list
    assert cliargs_deferred_get('other', shallowcopy=True)() == [1, 2, 3]
    # Test shallow copy works with a set
    assert cliargs_deferred_get('other', shallowcopy=True)

# Generated at 2022-06-12 21:24:24.655594
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': 'b'})
    value = cliargs_deferred_get('a')()
    assert value == 'b'
    CLIARGS = CLIArgs({'a': ['b']})
    value = cliargs_deferred_get('a', shallowcopy=True)()
    assert value == ['b']
    assert value is not CLIARGS.get('a')
    CLIARGS = CLIArgs({'a': ['b']})
    value = cliargs_deferred_get('a', shallowcopy=True)()
    assert value == ['b']
    assert value is not CLIARGS.get('a')

# Generated at 2022-06-12 21:24:35.295059
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=protected-access,unused-argument
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')().endswith('bar')
    assert cliargs_deferred_get('bar')().endswith(None)
    assert cliargs_deferred_get('foo', default='newbar')().endswith('bar')
    assert cliargs_deferred_get('bar', default='newbar')().endswith('newbar')

    factory = cliargs_deferred_get('foo', default='newbar')
    assert factory().endswith('bar')
    CLIARGS = CLIArgs({})
    assert factory().endswith('newbar')


# Generated at 2022-06-12 21:24:46.230366
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from unittest import mock

    def test_dict_attrs(key, default, shallowcopy):
        cli_args = {
            key: 'value',
            default: 'default',
        }
        with mock.patch('ansible.context.CLIARGS', CLIArgs(cli_args)):
            cli_default = cliargs_deferred_get(default, default)
            assert cli_default == cli_args[default]
            cli_value = cliargs_deferred_get(key, default, shallowcopy)
            assert cli_value == cli_args[key]

    test_dict_attrs('key', 'default', False)
    test_dict_attrs('key', 'default', True)

    def test_list_attrs(key, default, shallowcopy):
        cl