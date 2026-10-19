

# Generated at 2022-06-12 21:15:03.623550
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'verbosity': 20, 'foo': {'bar': 'baz'}})

    assert cliargs_deferred_get('verbosity')() == 20
    assert not cliargs_deferred_get('verbosity', shallowcopy=True)() is cliargs_deferred_get('verbosity')()
    assert cliargs_deferred_get('foo')() == {'bar': 'baz'}
    assert not cliargs_deferred_get('foo', shallowcopy=True)() is cliargs_deferred_get('foo')()

# Generated at 2022-06-12 21:15:10.360744
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test good and bad values for cliargs_deferred_get"""
    import pytest
    from ansible.module_utils._text import to_bytes

    _init_global_context({'accelerate': 0, 'errors': None})

    mod_args = {'test': None, 'test2': 'a', 'test3': [1, 2, 3], 'test4': {'key': 'value'}, 'test5': set([to_bytes('key')])}
    mod_args2 = dict(mod_args)
    mod_args2['test3'] = mod_args['test3'][:]
    mod_args2['test4'] = mod_args['test4'].copy()
    mod_args2['test5'] = mod_args['test5'].copy()

    # Test with the global values
   

# Generated at 2022-06-12 21:15:18.494349
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._opts = {'test': 'foo'}
    assert cliargs_deferred_get('test')() == 'foo'
    assert cliargs_deferred_get('non-existent')() is None
    assert cliargs_deferred_get('non-existent', 'default')() == 'default'
    CLIARGS._opts = {'list': [1, 2, 3]}
    assert cliargs_deferred_get('list', shallowcopy=False)() == [1, 2, 3]
    assert cliargs_deferred_get('list', shallowcopy=True)() == [1, 2, 3]
    CLIARGS._opts = {'set': {1, 2, 3}}

# Generated at 2022-06-12 21:15:29.524916
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=missing-docstring
    def test_deferred_get(key):  # pylint: disable=missing-docstring
        global CLIARGS  # pylint: disable=global-statement
        CLIARGS = CLIArgs({key: 'value'})
        assert cliargs_deferred_get(key)() == 'value'
        assert cliargs_deferred_get(key, default='default')() == 'value'
        assert cliargs_deferred_get(key, default='default', shallowcopy=True)() == 'value'
        assert cliargs_deferred_get(key, default='default', shallowcopy=False)() == 'value'
        CLIARGS = CLIArgs({})
        assert cliargs_deferred_get(key)() is None
        assert cliargs_

# Generated at 2022-06-12 21:15:38.217053
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get

    ``CLIARGS`` is a global variable.  Unit tests create a new python process so
    a global variable's value can't persist between unit tests.  We need to reset
    the value every test to make sure we get the desired behavior
    """
    assert cliargs_deferred_get('doesnotexist')() is None

    # Set CLIARGS to a known value
    global CLIARGS
    global_cliargs = CLIARGS
    CLIARGS = GlobalCLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'

    # Make sure we don't pass up a closure
    a = cliargs_deferred_get('foo')
    b = cliargs_deferred_get('foo')
    assert a()

# Generated at 2022-06-12 21:15:49.328920
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    options = dict(
        run_hosts=['foo.bar.com'],
        run_tags=['foo', 'bar'],
        run_group_names=['foo', 'bar'],
        run_role_names=['foo', 'bar'],
        run_tasks=['foo', 'bar'],
        roles_path=['/tmp/libs', '/home/libs'],
    )

    _init_global_context(options)
    assert CLIARGS == options

    # Test known value
    assert cliargs_deferred_get('run_hosts') == options['run_hosts']

    # Test default value
    assert cliargs_deferred_get('host_inventory', default=dict()) == dict()

    # Test shallow copy of sequence
    old_cli_run_

# Generated at 2022-06-12 21:15:50.771089
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_deferred_get('verbosity', 0)()

# Generated at 2022-06-12 21:15:59.922706
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = GlobalCLIArgs({'k1': 'value1'})
    assert cliargs_deferred_get('k1')() == 'value1'
    assert cliargs_deferred_get('k2', default='value2')() == 'value2'
    assert cliargs_deferred_get('k1', default='value2')() == 'value1'
    CLIARGS = CLIArgs({'k1': 'value1'})
    assert cliargs_deferred_get('k1')() == 'value1'
    assert cliargs_deferred_get('k2', default='value2')() == 'value2'

# Generated at 2022-06-12 21:16:11.292113
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest
    cli_args = {
        'foo': 'bar',
        'baz': [1, 2, 3],
        'sing': 'le',
        'dup': [2, 3, 4],
    }
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')(), "bar"
    assert cliargs_deferred_get('baz')(), [1, 2, 3]
    assert cliargs_deferred_get('sing')(), "le"
    assert cliargs_deferred_get('dup')(), [2, 3, 4]


# Generated at 2022-06-12 21:16:21.923608
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_args = {'testkey': 'testvalue', 'testkey2': ['testvalue2']}
    global CLIARGS
    CLIARGS = CLIArgs(test_args)
    # Test our noop
    assert cliargs_deferred_get('testkey')() == test_args['testkey']
    assert cliargs_deferred_get('testkey', shallowcopy=True)() == test_args['testkey']
    # Test with a value
    assert cliargs_deferred_get('testkey2')() == test_args['testkey2']
    assert cliargs_deferred_get('testkey2', shallowcopy=True)() == test_args['testkey2']
    # Test with a default value

# Generated at 2022-06-12 21:16:37.768364
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': 'b'})
    defg1 = cliargs_deferred_get('a')
    defg2 = cliargs_deferred_get('a', shallowcopy=True)
    defg3 = cliargs_deferred_get('a', 'b', True)
    assert defg1() == 'b'
    assert defg2() == 'b'
    assert defg3() == 'b'
    CLIARGS = CLIArgs({'a': 'c'})
    assert defg1() == 'c'
    assert defg2() == 'c'
    assert defg3() == 'c'

# Generated at 2022-06-12 21:16:45.763911
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # The global CLIArgs object is replaced during the tests
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})

    f = cliargs_deferred_get('foo', 'baz')
    assert f() == 'bar'

    f = cliargs_deferred_get('foo', 'baz', True)
    assert f() == 'bar'

    f = cliargs_deferred_get('baz', 'baz')
    assert f() == 'baz'

    f = cliargs_deferred_get('baz', 'baz', True)
    assert f() == 'baz'

    CLIARGS = CLIArgs({'foo': [1, 2]})
    f = cliargs_deferred_get('foo',None, True)

# Generated at 2022-06-12 21:16:55.620658
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from . import cliargs_deferred_get

    # Test 1
    class FakeCliArgs(dict):
        def get(self, key, default=None):
            return {
                'testkey': 'testvalue'
            }[key]

    global CLIARGS
    CLIARGS = FakeCliArgs()
    assert cliargs_deferred_get('testkey')() == 'testvalue'
    assert cliargs_deferred_get('testkey', default='notfound')() == 'testvalue'
    assert cliargs_deferred_get('notkey', default='notfound')() == 'notfound'
    assert cliargs_deferred_get('notkey')() is None
    CLIARGS = CLIArgs({})

    # Test 2

# Generated at 2022-06-12 21:17:03.029824
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    cliargs = CLIArgs({'foo': 0})
    my_deferred_get = cliargs_deferred_get('foo', -1)
    assert my_deferred_get() == 0
    assert cliargs_deferred_get('not_foo', 0)() == 0
    assert cliargs_deferred_get('not_foo', -1, True)() == -1


# Generated at 2022-06-12 21:17:13.711836
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Validate that cliargs_deferred_get does not return the actual CLIARGS value

    This validates that the closure is being returned, not the value of the closure
    """
    global CLIARGS
    original = dict(CLIARGS)

# Generated at 2022-06-12 21:17:21.493221
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test deferred getting values from CLIARGS"""
    _init_global_context(dict(foo=['bar'], bar=dict(one=1), baz=dict(two=2)))
    # No copy
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs_deferred_get('bar')() == dict(one=1)
    assert cliargs_deferred_get('baz')() == dict(two=2)
    # shallow copy
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']
    assert cliargs_deferred_get('bar', shallowcopy=True)() == dict(one=1)
    assert cliargs_deferred_get('baz', shallowcopy=True)() == dict(two=2)


# Generated at 2022-06-12 21:17:32.645008
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def dict_shallow_copy():
        options = dict(key=dict(child=dict(key='value')))
        _init_global_context(options)
        try:
            getter = cliargs_deferred_get('key')
            retrieved = getter()
            assert id(retrieved) != id(options['key']), "Expected a shallow copy. Got a reference"
            retrieved['child']['key'] = 'changed'
            assert (CLIARGS['key']['child']['key'] == 'changed')
        finally:
            CLIARGS.clear()

    def list_shallow_copy():
        options = dict(key=['value'])
        _init_global_context(options)

# Generated at 2022-06-12 21:17:41.510729
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {
        'foo': 'bar',
    }
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo') == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True) == 'bar'
    new_foo = cliargs_deferred_get('foo', shallowcopy=True)
    new_foo = 'baz'
    assert cliargs_deferred_get('foo') == 'bar'
    cli_args['foo'] = 'bar2'
    assert cliargs_deferred_get('foo') == 'bar2'

# Generated at 2022-06-12 21:17:52.181459
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def f(key, value, sc=False):
        return cliargs_deferred_get(key, sc)(), sc

    assert f("key", "value") == ("value", False)
    assert f("key", "value", sc=True) == ("value", True)

    assert f("key", ["value1", "value2"]) == (["value1", "value2"], False)
    assert f("key", ["value1", "value2"], sc=True) == (["value1", "value2"], True)

    assert f("key", {"value1": "1", "value2": "2"}) == ({"value1": "1", "value2": "2"}, False)

# Generated at 2022-06-12 21:18:01.684422
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'ANSIBLE_LOG_PATH': 'foo',
                          'ANSIBLE_POTENTIALLY_PRIVILEGED_ENV_VAR': ['bar', 'baz']})
    result = cliargs_deferred_get('ANSIBLE_LOG_PATH')()
    assert result == 'foo'

    result = cliargs_deferred_get('ANSIBLE_POTENTIALLY_PRIVILEGED_ENV_VAR')()
    assert result == ['bar', 'baz']

    result = cliargs_deferred_get('ANSIBLE_POTENTIALLY_PRIVILEGED_ENV_VAR', shallowcopy=True)()
    assert result == ['bar', 'baz']
    result[0] = 'foo'

    result2 = cliargs_

# Generated at 2022-06-12 21:18:19.003967
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    global CLIARGS
    import copy
    import sys

    old_stdout = sys.stdout
    sys.stdout = open('/dev/null', 'w')  # Python 2 requires the file to be openable

# Generated at 2022-06-12 21:18:27.662826
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    cli_args = {'hello': 'world'}
    _init_global_context(cli_args)
    # Normal get with no default and shallowcopy
    assert cliargs_deferred_get('hello', shallowcopy=False)() == 'world'
    assert cliargs_deferred_get('hello', shallowcopy=True)() == 'world'
    assert cliargs_deferred_get('hello', shallowcopy=False)() is cli_args['hello']
    assert cliargs_deferred_get('hello', shallowcopy=True)() is not cli_args['hello']
    # Normal get with default and shallowcopy
    default = 'foo'
    assert cliargs_deferred_get('missing', default=default, shallowcopy=False)() is default

# Generated at 2022-06-12 21:18:38.576329
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test setup
    original_cliargs = CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': 'abc'})

    # Deferred Get with default
    deferred_get = cliargs_deferred_get('spam', default='not_spam')
    assert deferred_get() == 'not_spam'
    CLIARGS['spam'] = 'yum'
    assert deferred_get() == 'yum'
    del CLIARGS['spam']
    assert deferred_get() == 'not_spam'

    # Deferred Get without default
    deferred_get = cliargs_deferred_get('foon')
    assert deferred_get() is None
    assert deferred_get() is None

    # Deferred Get with shallow copy
    deferred_get = cliargs_deferred

# Generated at 2022-06-12 21:18:48.244133
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import collections
    import copy
    CLIARGS.update({'list': [1, 2, 3], 'dict': {'a': 'b'}})
    assert cliargs_deferred_get('list') == [1, 2, 3]
    assert cliargs_deferred_get('dict') == {'a': 'b'}

    assert copy.copy(cliargs_deferred_get('list', shallowcopy=True)) == [1, 2, 3]
    assert copy.copy(cliargs_deferred_get('dict', shallowcopy=True)) == {'a': 'b'}

    for value in cliargs_deferred_get('list', shallowcopy=True):
        assert isinstance(value, int)

# Generated at 2022-06-12 21:18:59.457256
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Simple default
    cliargs = CLIArgs({})
    deferred = cliargs_deferred_get('value', default='foo')
    assert deferred() == 'foo'

    # Default from existing cliargs
    cliargs['value'] = 'bar'
    deferred = cliargs_deferred_get('value', default='foo')
    assert deferred() == 'bar'

    # Override existing cliargs
    deferred = cliargs_deferred_get('value', default='foo2')
    assert deferred() == 'foo2'

    # Return value from existing cliargs
    cliargs['value'] = 'foo'
    deferred = cliargs_deferred_get('value', default='bar')
    assert deferred() == 'foo'

    # Return value from existing item with shallow copy
    cliargs['value']

# Generated at 2022-06-12 21:19:07.586920
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cliargs = {'this': 'default'}
    CLIARGS = CLIArgs(cliargs)
    assert cliargs_deferred_get('this', default='default')() == 'default'
    assert cliargs_deferred_get('this', default='not_default')() == 'default'
    assert cliargs_deferred_get('that', default='default')() == 'default'
    assert cliargs_deferred_get('that', default='not_default')() == 'not_default'
    assert cliargs_deferred_get('that')() is None

# Generated at 2022-06-12 21:19:17.055437
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # This needs to be reset outside of the function
    tmp_cliargs = CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    # Test normal copy
    value = cliargs_deferred_get('foo')()
    assert value == 'bar'
    assert value is not CLIARGS['foo']
    assert value is not tmp_cliargs['foo']
    # Test shallow copy
    value = cliargs_deferred_get('foo', shallowcopy=True)()
    assert value == 'bar'
    assert value is not CLIARGS['foo']
    assert value is not tmp_cliargs['foo']
    # Test default
    value = cliargs_deferred_get('fizz', 'default value')()
    assert value == 'default value'

# Generated at 2022-06-12 21:19:26.017544
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # Test get
    CLIARGS = GlobalCLIArgs.from_options({})
    assert cliargs_deferred_get('foo', default=1)() == 1
    assert cliargs_deferred_get('foo', default=None)() is None
    CLIARGS = GlobalCLIArgs.from_options({'foo': 2})
    assert cliargs_deferred_get('foo', default=1)() == 2

    # Test shallow copy
    CLIARGS = GlobalCLIArgs.from_options({})
    assert cliargs_deferred_get('foo', default=1, shallowcopy=True)() == 1
    assert cliargs_deferred_get('foo', default=None, shallowcopy=True)() is None

# Generated at 2022-06-12 21:19:37.311070
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'first': 'test'})
    assert cliargs_deferred_get('first')() == 'test'
    assert cliargs_deferred_get('non-existent')() is None
    assert cliargs_deferred_get('non-existent', 'default')() == 'default'
    CLIARGS = CLIArgs({'first': ['test', 'another']})
    assert cliargs_deferred_get('first')() == ['test', 'another']
    assert cliargs_deferred_get('first', shallowcopy=True)() == ['test', 'another']
    assert cliargs_deferred_get('non-existent')() is None
    assert cliargs_deferred_get('non-existent', ['default'])() == ['default']
    assert cl

# Generated at 2022-06-12 21:19:44.116466
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Setup
    import ansible
    cli_args = ansible.utils.context_objects.CLIArgs({'list_key': ['item 1', 'item 2']})
    global CLIARGS
    CLIARGS = cli_args

    # Run
    list_key_value = cliargs_deferred_get('list_key', default=[])()

    # Assert
    assert list_key_value == ['item 1', 'item 2']
    assert CLIARGS.get('list_key') is list_key_value
    assert cliargs_deferred_get('list_key', default=[])() is list_key_value



# Generated at 2022-06-12 21:20:07.583748
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import Mapping, Set, MutableSet

    def value_should_be_default(key, default, shallowcopy):
        assert value() == default

    def value_should_be_unchanged(key, default, shallowcopy):
        assert value() == key


# Generated at 2022-06-12 21:20:12.993007
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'s': 'test'})
    global CLIARGS
    CLIARGS = cliargs
    f = cliargs_deferred_get('s')
    assert f() == 'test'
    CLIARGS = CLIArgs()
    assert f() is None
    f = cliargs_deferred_get('s', default='boo')
    assert f() == 'boo'

# Generated at 2022-06-12 21:20:20.956031
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_bytes
    CLIARGS.update(ImmutableDict({'ANSIBLE_ANSIBLE_MODULE_UTILS': to_bytes(__name__)}))
    # a function expecting one argument
    assert cliargs_deferred_get('ANSIBLE_ANSIBLE_MODULE_UTILS')() == __name__
    assert cliargs_deferred_get('ANSIBLE_ANSIBLE_MODULE_UTILS')(shallowcopy=True) == __name__
    assert cliargs_deferred_get('ANSIBLE_ANSIBLE_MODULE_UTILS')(default='foo') == __name__
    # a function that does not expect an argument
    assert cliargs_deferred

# Generated at 2022-06-12 21:20:30.416305
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pragma: no cover
    CLIARGS['foo'] = 'bar'
    assert 'bar' == cliargs_deferred_get('foo')()
    CLIARGS['foo'] = ['bar']
    assert 'bar' == cliargs_deferred_get('foo')()
    CLIARGS['foo'] = ['bar']
    assert ['bar'] == cliargs_deferred_get('foo', shallowcopy=False)()
    assert ['bar'] == cliargs_deferred_get('foo', shallowcopy=True)()
    CLIARGS['foo'] = ['bar']
    assert [] == cliargs_deferred_get('foo', default=None, shallowcopy=True)()
    assert ['bar'] == cliargs_deferred_get('foo', default=None, shallowcopy=False)()

# Generated at 2022-06-12 21:20:39.925653
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = {'_ansible_version': '2.8.0',
               'tags': ['all'],
               'ssh_args': '-o ForwardAgent=yes',
               'playbook_command': 'playbook'}

    CLIARGS._options = cliargs
    # test a value that is not present in the cliargs
    assert cliargs_deferred_get('test_key')() == None
    # test a value with default
    assert cliargs_deferred_get('test_key', default="default_value")() == 'default_value'
    # test shallow copy
    assert cliargs_deferred_get('test_key', default="default_value", shallowcopy=True)() == 'default_value'
    # test a value without shallow copy
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:20:46.022491
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    C = CLIArgs({'a': 'a'})
    CLIARGS = C
    get_a = cliargs_deferred_get('a')
    assert get_a() == 'a'
    CLIARGS = CLIArgs({'b': 'b'})
    get_a = cliargs_deferred_get('a')
    assert get_a() == 'a'

# Generated at 2022-06-12 21:20:56.417702
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = {'foo': 'bar'}
    _init_global_context(cliargs)
    assert cliargs_deferred_get('foo')() == 'bar'
    cliargs['foo'] = 'baz'
    assert cliargs_deferred_get('foo')() == 'baz'
    assert cliargs_deferred_get('missing')() is None
    assert cliargs_deferred_get('missing', default='default')() == 'default'

    from copy import copy
    cliargs['foo'] = copy(cliargs)
    assert cliargs_deferred_get('foo')() is not cliargs
    assert cliargs_deferred_get('foo')() == cliargs
    assert cliargs_deferred_get('foo', shallowcopy=True)() is not cl

# Generated at 2022-06-12 21:21:02.515714
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test it works with a mapping type
    class options(Mapping):
        def __init__(self):
            self._store = {'a': 1}
        def __getitem__(self, key):
            return self._store[key]
        def __iter__(self):
            return iter(self._store)
        def __len__(self):
            return len(self._store)

    CLIARGS_TEST = options()

    g = cliargs_deferred_get('a')
    assert g() == 1
    # Test shallow copy
    CLIARGS_TEST['a'] = []
    assert g() == []
    CLIARGS_TEST['a'].append(2)
    assert g() == [2]

    # Test simple values
    CLIARGS_TEST['a'] = 1


# Generated at 2022-06-12 21:21:07.931045
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    cli_args = CLIArgs({'hi': 'bye'})
    assert cliargs_deferred_get('hi', default='top')(cli_args) == 'bye'
    assert cliargs_deferred_get('top', default='top')(cli_args) == 'top'
    assert cliargs_deferred_get('top', default='top', shallowcopy=True)(cli_args) == 'top'

# Generated at 2022-06-12 21:21:19.808501
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {
        'foo': 'bar',
        'baz': [1, 2, 3],
        'quux': {'a': 'b'},
    }
    _init_global_context(cli_args)
    no_default_shallow_copy = cliargs_deferred_get('foo', shallowcopy=True)
    no_default_copy = cliargs_deferred_get('foo', shallowcopy=False)
    default_shallow_copy = cliargs_deferred_get('nonexistant', shallowcopy=True)
    default_copy = cliargs_deferred_get('nonexistant', shallowcopy=False)

    # lambda c: c, c[:], c.copy()
    #            str, list, dict

# Generated at 2022-06-12 21:21:55.586540
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    class ExtraCLIArgs(CLIArgs):
        test_list = []
        test_dict = {}
    def assert_deep_equal(value, expected):
        assert value == expected

    # Make sure that the closure returns values from CLIARGS and not from the outer closure
    CLIARGS = ExtraCLIArgs({'test_list': [1, 2, 3], 'test_dict': {'foo': 'bar'}})
    test_list_closure = cliargs_deferred_get('test_list', default=[])
    test_dict_closure = cliargs_deferred_get('test_dict', default={})
    assert_deep_equal(test_list_closure(), [1, 2, 3])
    assert_deep_equal(test_dict_closure(), {'foo': 'bar'})



# Generated at 2022-06-12 21:22:02.183796
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    key = 'foo'
    value = 'bar'
    default = 'baz'
    cliargs_dict = {key: value}

    def verify_value(expected, shallowcopy=False):
        assert cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)() == expected
        assert cliargs_deferred_get(key, default=default, shallowcopy=False)() == expected

    # No CLI args, defer to default
    verify_value(default)

    # CLI args set, use them
    cliargs_dict[key] = value
    CLIARGS.update(cliargs_dict)
    verify_value(value)

    # Check shallow copy
    CLIARGS[key] = [1, 2, 3, 4]

# Generated at 2022-06-12 21:22:13.732521
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:22:22.355348
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the function cliargs_deferred_get"""
    options = dict(a=1, b=59, c=dict(d=50, e=51))
    CLIARGS.update(options)
    assert cliargs_deferred_get('a', default=62)() == 1
    assert cliargs_deferred_get('b', default=62)() == 59
    assert cliargs_deferred_get('c', default=62)() == dict(d=50, e=51)
    assert cliargs_deferred_get('d', default=62)() == 62
    assert cliargs_deferred_get('d', default=62, shallowcopy=True)() == 62

# Generated at 2022-06-12 21:22:32.487252
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that it can be called before CLIARGS is initialized
    assert cliargs_deferred_get('verbosity')(), 0

    test_args = dict(verbosity=3, debug=False)
    _init_global_context(test_args)
    # Test that is returns the expected values
    assert cliargs_deferred_get('verbosity')(), 3
    assert cliargs_deferred_get('debug')(), False
    assert cliargs_deferred_get('missingkey')(), None
    assert cliargs_deferred_get('missingkey', 'hello')(), 'hello'
    assert cliargs_deferred_get('missingkey', default=10)(), 10
    assert cliargs_deferred_get('verbosity', shallowcopy=True)(), 3

# Generated at 2022-06-12 21:22:43.397534
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args_old = {'best_key': 'best_value'}
    _init_global_context(cli_args_old)
    assert cliargs_deferred_get('best_key')() == 'best_value'
    # see if defaults work
    assert cliargs_deferred_get('no_key', 'best_value')() == 'best_value'
    # Test shallow copies
    cli_args_old['new_best_seq'] = ["a", "b", "c"]
    assert cliargs_deferred_get('new_best_seq', shallowcopy=True)() == ["a", "b", "c"]
    cli_args_old['new_best_map'] = {"a": 1, "b": 2}

# Generated at 2022-06-12 21:22:49.101215
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': [1, 2, 3], 'b': {'a': 1, 'b': 2}, 'c': 'foo', 'd': (4, 5, 6)})
    tests = [
        ('a', [1, 2, 3]),
        ('b', {'a': 1, 'b': 2}),
        ('c', 'foo'),
        ('d', (4, 5, 6)),
        ('e', None),
    ]
    for arg_name, arg_val in tests:
        assert cliargs_deferred_get(arg_name) == arg_val
        assert cliargs_deferred_get(arg_name, shallowcopy=True) == arg_val

    # Change the values after they were read

# Generated at 2022-06-12 21:23:01.092595
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    class TestArgs(object):
        TEST_FIELD = FieldAttribute(default=cliargs_deferred_get('test_deferred'))

    assert TestArgs().TEST_FIELD is None

    CLIARGS = CLIArgs({'test_deferred': 'value'})
    assert TestArgs().TEST_FIELD == 'value'

    CLIARGS = CLIArgs({'test_deferred': ['a', 'b', 'c']})
    assert TestArgs().TEST_FIELD == ['a', 'b', 'c']

    CLIARGS = CLIArgs({'test_deferred': {'a': 'b'}})
    assert TestArgs().TEST_FIELD == {'a': 'b'}

    assert TestArgs(test_deferred='value').TEST_FIELD == 'value'

# Generated at 2022-06-12 21:23:08.453756
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import unittest
    import inspect
    class TestCliArgsDeferredGet(unittest.TestCase):
        def test_func_returns_callable(self):
            func = cliargs_deferred_get('foo')
            self.assertTrue(inspect.isroutine(func))

        def test_func_returns_default(self):
            func = cliargs_deferred_get('foo', 'bar')
            self.assertEqual(func(), 'bar')

        def test_func_returns_cliarg(self):
            global CLIARGS
            CLIARGS = CLIArgs({'foo': 'bar'})
            func = cliargs_deferred_get('foo')
            self.assertEqual(func(), 'bar')
            del CLIARGS # So cleanup doesn't leave objects behind

   

# Generated at 2022-06-12 21:23:16.460689
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Ensure that cliargs_deferred_get() behaves correctly"""
    global CLIARGS
    CLIARGS = CLIArgs({})
    assert not CLIARGS
    assert cliargs_deferred_get('nonexistent')() == None
    assert cliargs_deferred_get('nonexistent', default='foo')() == 'foo'
    CLIARGS = CLIArgs({'foo': 'the foo value'})
    assert cliargs_deferred_get('nonexistent')() == None
    assert cliargs_deferred_get('nonexistent', default='foo')() == 'foo'
    assert cliargs_deferred_get('foo')() == 'the foo value'

# Generated at 2022-06-12 21:24:20.511082
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.clear()
    CLIARGS['foo'] = 'bar'
    get_foo = cliargs_deferred_get('foo')
    assert get_foo() == 'bar'

    CLIARGS.clear()
    CLIARGS['foo'] = ['bar']
    get_foo = cliargs_deferred_get('foo', shallowcopy=True)
    assert get_foo() == ['bar']
    CLIARGS['foo'].append('baz')
    assert get_foo() == ['bar']

    CLIARGS.clear()
    CLIARGS['foo'] = {'bar': 'baz'}
    get_foo = cliargs_deferred_get('foo', shallowcopy=True)
    assert get_foo() == {'bar': 'baz'}

# Generated at 2022-06-12 21:24:31.788636
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # queue up a mock cliargs
    cli_args = {}
    _init_global_context(cli_args)
    assert CLIARGS.get('foo').__defaults__ == (None,)
    cli_args['foo'] = 'bar'
    _init_global_context(cli_args)
    assert CLIARGS.get('foo').__defaults__ == (None,)
    x = cliargs_deferred_get('foo', default='foo')
    assert x().__defaults__ == ('bar',)
    cli_args['foo'] = 'baz'
    _init_global_context(cli_args)
    assert x().__defaults__ == ('baz',)
    assert x.__defaults__ == ('foo',)

# Generated at 2022-06-12 21:24:43.679730
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Test pure function
    assert 10 == cliargs_deferred_get('nonexistent', 10)()
    assert 10 == CLIARGS.get('nonexistent', 10)
    # Test shallow copy
    CLIARGS = CLIArgs({'test': {'test': 'test'}})
    assert {'test': 'test'} == cliargs_deferred_get('test', {}, shallowcopy=True)()
    assert {'test': 'test'} != cliargs_deferred_get('test', {}, shallowcopy=True)()
    # Test set shallow copy
    CLIARGS = CLIArgs({'test': {'test': 'test'}})
    assert {'test', 'test'} == cliargs_deferred_get('test', {}, shallowcopy=True)()
   

# Generated at 2022-06-12 21:24:55.667318
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that we copy when we are asked to
    _init_global_context({'foo': [1, 2, 3]})
    cliargs_deferred_get_foo = cliargs_deferred_get('foo', shallowcopy=True)
    assert id(cliargs_deferred_get_foo()) != id(CLIARGS['foo'])
    assert cliargs_deferred_get_foo() == CLIARGS['foo']

    # Test that we make copies at different depths
    _init_global_context({'bar': {'a': 1, 'b': 2}})
    cliargs_deferred_get_bar = cliargs_deferred_get('bar', shallowcopy=True)
    assert cliargs_deferred_get_bar() != CLIARGS['bar']