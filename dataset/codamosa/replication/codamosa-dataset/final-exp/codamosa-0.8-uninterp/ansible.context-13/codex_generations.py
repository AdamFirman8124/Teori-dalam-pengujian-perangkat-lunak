

# Generated at 2022-06-12 21:15:06.167881
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    def test_func(key, default=None, shallowcopy=False):
        return cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3], 'blurfl': {'a': 1}})
    assert test_func('foo') == 'bar'
    assert test_func('foo', 'default') == 'bar'
    assert test_func('foo', default='default') == 'bar'
    assert test_func('baz', shallowcopy=True) == [1, 2, 3]
    assert test_func('baz') == [1, 2, 3]
    assert test_func('blurfl', shallowcopy=True) == {'a': 1}
   

# Generated at 2022-06-12 21:15:15.349841
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    CLIARGS.update({'test_key1': [1, 2, 3], 'test_key2': ('a', 'b', 'c')})

    def check_list(list1, list2):
        return all([l1 == l2 for l1, l2 in zip(list1, list2)])

    v1 = cliargs_deferred_get('test_key1')()
    assert check_list(v1, [1, 2, 3]), "Failed to get cli args"
    v2 = cliargs_deferred_get('test_key1')(shallowcopy=True)
    assert check_list(v2, [1, 2, 3]), "Failed to get cli args"

# Generated at 2022-06-12 21:15:21.255050
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that the closure for cliargs_deferred_get works as expected"""
    from ansible.module_utils.common._collections_compat import Mapping, Set

    global CLIARGS
    options = dict(a=1, b=[1, 2], c={'d': 4}, e=set('f'))
    CLIARGS = CLIArgs(options)

    for key, value in options.items():
        assert cliargs_deferred_get(key)() == value
        assert cliargs_deferred_get(key, shallowcopy=True)() == value

    assert cliargs_deferred_get('not_there')() is None
    assert cliargs_deferred_get('not_there', shallowcopy=True)() is None

# Generated at 2022-06-12 21:15:32.207585
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    CLIARGS['foo'] = ['bar', 'baz']
    assert cliargs_deferred_get('foo')() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']

# Generated at 2022-06-12 21:15:37.576884
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.text.converters import to_text
    assert to_text(cliargs_deferred_get('_ansible_version'))

    _init_global_context({})
    # using assert as it's easier to distinguish the success/failure
    assert to_text(CLIARGS.get('_ansible_version')) == to_text(cliargs_deferred_get('_ansible_version')())



# Generated at 2022-06-12 21:15:49.089204
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    CLIARGS = CLIArgs({'become': True, 'become_user': 'root', 'become_ask_pass': True})
    assert cliargs_deferred_get('become')()
    assert cliargs_deferred_get('become_user')() == 'root'
    assert cliargs_deferred_get('become_ask_pass')()
    assert cliargs_deferred_get('ansible_version')()

    CLIARGS = CLIArgs({'become': False, 'become_user': 'nobody', 'become_ask_pass': False})
    assert not cliargs_deferred_get('become')()
    assert cliargs_deferred_get('become_user')() == 'nobody'
    assert not cliargs_def

# Generated at 2022-06-12 21:15:59.882941
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    global CLIARGS
    try:
        # Test that if used before CLIARGS is initialized to a GlobalCLIArgs object
        # that it will gracefully fail
        CLIARGS = {}
        cliargs_deferred_get('foobar')
        assert 0, 'expected cliargs_deferred_get to raise an exception'
    except AttributeError:
        pass

    # Test that it returns the value if we pass it
    CLIARGS = CLIArgs({'foobar': True})
    assert cliargs_deferred_get('foobar')

    # Test that it returns the default if we don't pass it
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('foobar', default=False) == False

# Generated at 2022-06-12 21:16:11.184805
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for ``cliargs_deferred_get``."""
    # pylint: disable=protected-access
    CLIARGS._data.clear()
    inner = cliargs_deferred_get('key1', 'default1')
    assert inner() == 'default1'
    CLIARGS._data['key1'] = 'v1'
    assert inner() == 'v1'
    CLIARGS._data['key2'] = ['v2', 'v3']
    inner = cliargs_deferred_get('key2', 'default2', shallowcopy=True)
    assert inner() == ['v2', 'v3']
    CLIARGS._data['key2'].append('v4')
    assert inner() == ['v2', 'v3']
    # pylint: enable=protected-access

# Generated at 2022-06-12 21:16:21.789120
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    get = cliargs_deferred_get('test')
    assert get() == None
    CLIARGS['test'] = 123
    assert get() == 123

    get = cliargs_deferred_get('test', default=456)
    assert get() == 123

    get = cliargs_deferred_get('test', shallowcopy=True)
    CLIARGS['test'] = [1, 2, 3]
    assert get() == [1, 2, 3]
    assert get() is not CLIARGS['test']

if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
   

# Generated at 2022-06-12 21:16:23.021921
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_deferred_get('bad_key', default='default value')()

# Generated at 2022-06-12 21:16:39.128246
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'foo': 'bar', 'baz': [1, 2, 3], 'qux': {'a': 'b'}})
    assert cliargs_deferred_get('foo') == 'bar'
    assert cliargs_deferred_get('baz') == [1, 2, 3]
    assert cliargs_deferred_get('qux') == {'a': 'b'}
    assert cliargs_deferred_get('foobar') is None
    assert cliargs_deferred_get('foobar', 'default') == 'default'
    assert cliargs_deferred_get('foo', shallowcopy=True) == 'bar'
    assert cliargs_deferred_get('baz', shallowcopy=True) == [1, 2, 3]
    assert cliargs_

# Generated at 2022-06-12 21:16:46.481062
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    def _test_inner(key, default=None, shallowcopy=False):
        value = CLIARGS.get(key, default=default)
        if not shallowcopy:
            return value
        elif is_sequence(value):
            return value[:]
        elif isinstance(value, (Mapping, Set)):
            return value.copy()
        return value

    # Test setting and getting a value
    def test_inner_set():
        cliargs = CLIARGS
        cliargs['foo'] = 'bar'
        assert _test_inner('foo') == 'bar'
        assert cliargs_deferred_get('foo')() == 'bar'
        cliargs['foo'] = 'bar2'
        assert _test_inner('foo') == 'bar2'
        assert cliargs

# Generated at 2022-06-12 21:16:55.792975
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # these two are not directly bound to CLIARGS because that would cause
    # a circular reference on the test runner
    cliargs = CLIArgs({'key1': 1, 'key2': 'junk'})
    getter = cliargs_deferred_get

    # must be callable
    getter()

    assert getter() == 1
    assert getter(key='key2') == 'junk'
    assert getter(key='key1', default=2) == 1
    assert getter(key='key3', default=2) == 2

    # Shallow copy or not
    assert getter(key='key1', shallowcopy=True) == getter(key='key1', shallowcopy=False)

# Generated at 2022-06-12 21:17:07.219068
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get works as expected
    """
    import collections
    # test with args not set
    expected_default = 'foo'
    assert cliargs_deferred_get('doesnotexist', default=expected_default)() == expected_default

    # test with args set and shallowcopy=False
    expected_value = 'bar'
    cli_args = {'foo': expected_value}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo', default=expected_default)() == expected_value

    # test with args set and shallowcopy=True with tuple
    expected_value = ('bar', 'baz')
    cli_args = {'foo': expected_value}
    _init_global_context(cli_args)

# Generated at 2022-06-12 21:17:17.616197
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    def assert_func_equivalent(func1, func2):
        assert func1() == func2()

    # test a valid value from the initial value - i.e. it should be the same as
    # just looking up the value directly
    assert_func_equivalent(cliargs_deferred_get('verbosity'), CLIARGS.get('verbosity'))

    # test a new value that is set onto the CLIARGS
    global CLIARGS
    CLIARGS = GlobalCLIArgs({'verbosity': 5})
    assert_func_equivalent(cliargs_deferred_get('verbosity'), CLIARGS.get('verbosity'))

    # test a value that is not there and the default

# Generated at 2022-06-12 21:17:29.223907
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class CliArgs(dict):
        def get(self, key, default=None):
            if key in self:
                return self[key]
            return default
    cliargs = CliArgs()
    cliargs['foo'] = [1, 2, 3]
    assert cliargs_deferred_get('foo', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('foo', shallowcopy=False)() == [1, 2, 3]
    cliargs['bar'] = {1: 2, 2: 3}
    assert cliargs_deferred_get('bar', shallowcopy=True)() == {1: 2, 2: 3}
    assert cliargs_deferred_get('bar', shallowcopy=False)() == {1: 2, 2: 3}

# Generated at 2022-06-12 21:17:40.632868
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class DummyCLIARGS(object):
        def __init__(self, values):
            self._values = values

        def __getitem__(self, key):
            return self._values[key]

    # Make sure that we can call without the CLIARGS being set to an actual object
    assert cliargs_deferred_get('foo')(None) is None

    # Make sure that we get the default when CLIARGS doesn't have the key
    old_CLIARGS = CLIARGS
    CLIARGS = DummyCLIARGS({})
    assert cliargs_deferred_get('foo')(None) is None
    assert cliargs_deferred_get('foo', 'bar')(None) == 'bar'
    CLIARGS = old_CLIARGS

    # Make sure that we get the value

# Generated at 2022-06-12 21:17:51.748043
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class GlobalCLIArgs_2(GlobalCLIArgs):
        # Need to redefine this so it doesn't just grab things from the CLI
        def get(self, key, default):
            return self._inner.get(key, default)

        def __setitem__(self, key, value):
            self._inner[key] = value

    global CLIARGS
    orig_cliargs = CLIARGS
    CLIARGS = GlobalCLIArgs_2({})

    # Test shallow copy
    CLIARGS['a'] = [1, 2, [3, 4]]
    a_copy = cliargs_deferred_get('a', shallowcopy=True)()
    CLIARGS['a'].append(5)
    assert a_copy == [1, 2, [3, 4]]

    # Test no shallow copy
    a_

# Generated at 2022-06-12 21:18:01.311595
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    global CLIARGS
    from ansible.parsing.vault import VaultLib

    CLIARGS = CLIArgs({'vault_password_file': 'password_file', 'default_vault_identity_list': ['identity1', 'identity2']})
    getter = cliargs_deferred_get('vault_password_file')
    assert getter() == CLIARGS.vault_password_file

    # Test default
    getter = cliargs_deferred_get('vault_password_file', default='default')
    assert getter() == 'password_file'

    CLIARGS = CLIArgs({'vault_password_file': 'password_file'})

# Generated at 2022-06-12 21:18:12.900523
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the case where there is no value and a default is returned
    CLIARGS.noop_flags = {}
    assert cliargs_deferred_get('noop_flags')() == {}
    # Test the case where there is a value and it is returned
    CLIARGS.noop_flags['foo'] = 'bar'
    assert cliargs_deferred_get('noop_flags')() == {'foo': 'bar'}
    # Test the case where we ask for a shallow copy and the copy is returned
    CLIARGS.noop_flags = {'foo': 'bar'}
    assert cliargs_deferred_get('noop_flags', shallowcopy=True)() == {'foo': 'bar'}
    # Test the case where we ask for a shallow copy of a mutable value and that a copy is returned

# Generated at 2022-06-12 21:18:26.263226
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    global CLIARGS
    dummy_cliargs = {'a': 'b', 'c': [1, 2, 3]}
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs(dummy_cliargs)
    result_no_copy = cliargs_deferred_get('a')()
    result_shallow = cliargs_deferred_get('c', shallowcopy=True)()
    # restore state
    CLIARGS = old_cliargs
    assert result_no_copy == dummy_cliargs['a']
    assert result_shallow == dummy_cliargs['c']

# Generated at 2022-06-12 21:18:37.584312
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    import copy
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils._text import to_text

    # test default
    CLIARGS = CLIArgs({'test': 'value'})
    value = cliargs_deferred_get('not-there')
    assert value is None, to_text(value)

    # test normal value
    value = cliargs_deferred_get('test')
    assert value is CLIARGS['test'], to_text(value)

    # test default value
    CLIARGS = CLIArgs({})
    value = cliargs_deferred_get('not-there', default='not-here')
    assert value == 'not-here', to_text(value)

    # test shallow copy

# Generated at 2022-06-12 21:18:47.518260
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    '''Verify that cliargs_deferred_get picks up the values when variables are set'''

    class TestCliArgs(GlobalCLIArgs):
        def __init__(self, vars_):
            self._vars = vars_
            self._keys = frozenset(vars_.keys())

        def __contains__(self, key):
            return key in self._keys

        def __getitem__(self, key):
            return self._vars[key]

        def get(self, key, default=None):
            return self._vars.get(key, default=default)

    vars_ = {'foo': 3, 'bar': [1, 2]}
    cliargs = TestCliArgs(vars_)

    # Verify that the right value is returned
    assert cliargs_def

# Generated at 2022-06-12 21:18:58.783352
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    context = CLIArgs({'a': 1,
                       'b': [1, 2, 3],
                       'c': {1, 2, 3},
                       'd': {'a': 1, 'b': 2, 'c': 3}})
    assert CLIARGS.get('a') is None
    assert CLIARGS.get('b') is None
    assert CLIARGS.get('c') is None
    assert CLIARGS.get('d') is None
    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() == [1, 2, 3]
    assert cliargs_deferred_get('c')() == {1, 2, 3}

# Generated at 2022-06-12 21:19:01.564690
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    get = cliargs_deferred_get('foo')
    assert get() == 'bar'



# Generated at 2022-06-12 21:19:11.500333
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # default
    assert cliargs_deferred_get('some_key', 'default')() == 'default'
    # value
    CLIARGS._values = {'some_key': 'value'}
    assert cliargs_deferred_get('some_key', 'default')() == 'value'
    # shallow copy
    CLIARGS._values = {'some_key': ['a', 'b']}
    assert cliargs_deferred_get('some_key', 'default', shallowcopy=True)() == ['a', 'b']
    assert cliargs_deferred_get('some_key', 'default')() is CLIARGS._values['some_key']

# Generated at 2022-06-12 21:19:18.998510
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.dict_transformations import dict_merge

    class DummyField:
        def __init__(self, name, default=None, shallow_copy=False):
            self.name = name
            self.default = default
            self.shallow_copy = shallow_copy

        def __repr__(self):
            return "Dummy {0}: name={1!r}, default={2!r}, shallow_copy={3!r}".format(
                type(self).__name__, self.name, self.default, self.shallow_copy)

        def default_or_cli(self):
            return cliargs_deferred_get(self.name, self.default, self.shallow_copy)


# Generated at 2022-06-12 21:19:27.281608
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('foo')(), None
    assert cliargs_deferred_get('foo', default=True)(), True
    CLIARGS['foo'] = False
    assert cliargs_deferred_get('foo')(), False
    assert cliargs_deferred_get('foo', default=True)(), False
    assert cliargs_deferred_get('foo', default=True, shallowcopy=True)(), False
    CLIARGS['foo'] = {'a': 'b'}
    assert cliargs_deferred_get('foo')(), {'a': 'b'}
    assert cliargs_deferred_get('foo', default={})(), {'a': 'b'}

# Generated at 2022-06-12 21:19:39.030511
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test shallow copy of a list
    CLIARGS['test_key'] = ['test_value']
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == ['test_value']
    cliargs_val = cliargs_deferred_get('test_key', shallowcopy=True)()
    cliargs_val[0] = 'new_value'
    assert cliargs_deferred_get('test_key')() == cliargs_val

    # Test shallow copy of a dictionary
    CLIARGS['test_key'] = {'test_key': 'test_value'}
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == {'test_key': 'test_value'}
    cliargs_val = cliargs_deferred

# Generated at 2022-06-12 21:19:48.117150
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    cliargs = CLIArgs({'foo': 1, 'bar': 'value'})

    @cliargs_deferred_get('foo')
    def foo_from_cliargs():
        pass

    @cliargs_deferred_get('bar')
    def bar_from_cliargs():
        pass


    assert foo_from_cliargs() == 1
    assert bar_from_cliargs() == 'value'

    cliargs['foo'] = 2
    cliargs['bar'] = 'other_value'

    assert foo_from_cliargs() == 1
    assert bar_from_cliargs() == 'value'

# Generated at 2022-06-12 21:20:04.352150
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    CLIARGS = CLIArgs({'foo': ['bar', 'baz']})
    assert cliargs_deferred_get('foo')() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']
    CLIARGS = CLIArgs({'foo': {'bar': 'baz'}})
    assert cliargs_deferred_get('foo')() == {'bar': 'baz'}
    assert cliargs_deferred_get('foo', shallowcopy=True)() == {'bar': 'baz'}
    CLIARGS = CLIArgs({})


# Generated at 2022-06-12 21:20:11.690075
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update(_bin_ansible_galaxy=True, _bin_ansible_playbook=False, mystuff=666)
    f = cliargs_deferred_get('mystuff')
    assert f() == 666
    CLIARGS.update(mystuff=777)
    assert f() == 777
    assert cliargs_deferred_get('nosuchkey', 'default')() == 'default'
    assert cliargs_deferred_get('nosuchkey', default='default')() == 'default'
    CLIARGS.update(mylist=['one', 'two'])
    assert cliargs_deferred_get('mylist')() == ['one', 'two']
    assert cliargs_deferred_get('mylist', shallowcopy=True)() == ['one', 'two']
    assert cli

# Generated at 2022-06-12 21:20:16.812894
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # can read from original
    assert cliargs_deferred_get('--version')() == None
    # can set the value
    CLIARGS['--version'] = 1
    # can read the value back
    assert cliargs_deferred_get('--version')() == 1
    # can read the shallow copy and confirm it's a copy
    new_dict = cliargs_deferred_get('--connection-user', shallowcopy=True)()
    assert new_dict == {}
    new_dict['foo'] = 'bar'
    assert new_dict != cliargs_deferred_get('--connection-user', shallowcopy=True)()
    # can read a deep copy and get a deep copy
    CLIARGS['--forks'] = [1,2]

# Generated at 2022-06-12 21:20:27.767055
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    temp_cli_args = {}
    _init_global_context(temp_cli_args)
    assert cliargs_deferred_get('test_key')() is None
    temp_cli_args['test_key'] = 'test_value'
    _init_global_context(temp_cli_args)
    assert cliargs_deferred_get('test_key')() == 'test_value'
    temp_cli_args['test_key'] = ['1', '2', '3']
    _init_global_context(temp_cli_args)
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == ['1', '2', '3']

# Generated at 2022-06-12 21:20:38.998231
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.context import cliargs_deferred_get, CLIARGS
    _init_global_context({'key1': 1, 'key2': 2, 'key3': None, 'key4': 'value4',
                          'key5': False, 'key6': '1'})

    assert cliargs_deferred_get('key1')() == 1
    assert cliargs_deferred_get('key2')() == 2
    assert cliargs_deferred_get('key3')() is None
    assert cliargs_deferred_get('key4')() == 'value4'
    assert not cliargs_deferred_get('key5')()
    assert cliargs_deferred_get('key6')() == '1'

    assert cliargs_deferred_

# Generated at 2022-06-12 21:20:49.208097
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('foo')() == None
    assert cliargs_deferred_get('foo', 'baz')() == 'baz'
    assert cliargs_deferred_get(None)() == None
    assert cliargs_deferred_get('foo', 'baz', True)() == 'baz'
    assert cliargs_deferred_get('foo', ['baz'], True)() == ['baz']
    assert cliargs_deferred_get('foo', {'baz': 'qux'}, True)() == {'baz': 'qux'}
    assert cliargs_deferred_get('foo', {'baz'}, True)() == {'baz'}

# Generated at 2022-06-12 21:20:58.835740
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = {'foo': 'bar', 'town': ('a', 'b'), 'foods': {'chocolate', 'cake', 'candy'}}
    _init_global_context(cliargs)
    assert 'bar' == cliargs_deferred_get('foo')()
    assert ('a', 'b') == cliargs_deferred_get('town')()
    assert {'chocolate', 'cake', 'candy'} == cliargs_deferred_get('foods')()

    assert 'baz' == cliargs_deferred_get('argh', default='baz')()
    assert 'baz' == cliargs_deferred_get('argh')('baz')

    assert ['a', 'b'] == cliargs_deferred_get('town', shallowcopy=True)()


# Generated at 2022-06-12 21:21:03.966201
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test a deferred get"""
    value = object()
    args = {'key': value}
    global CLIARGS
    CLIARGS = CLIArgs(args)
    assert cliargs_deferred_get('key')(), value



# Generated at 2022-06-12 21:21:11.679391
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test ``cliargs_deferred_get``"""
    assert not hasattr(CLIARGS, 'test_cliargs_deferred_get')
    assert 'test_cliargs_deferred_get' not in CLIARGS

    # Test that it gets a key not set in the CLIARGS
    test_value = {'key': 'value'}
    result1 = cliargs_deferred_get('test_cliargs_deferred_get', default=test_value)()
    result2 = cliargs_deferred_get('test_cliargs_deferred_get', default=test_value, shallowcopy=True)()
    assert result1 is result2
    assert result1 == result2 == test_value

    # Test it gets a key set in CLIARGS

# Generated at 2022-06-12 21:21:20.817117
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get returns the value of CLIARGS.get"""
    global CLIARGS
    original_cliargs = CLIARGS
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'
    CLIARGS = CLIArgs({'foo': 'baz'})
    assert cliargs_deferred_get('foo')() == 'baz'
    assert cliargs_deferred_get('foo', default='bar')() == 'baz'
    CLIARGS = CLIArgs({'foo': [1, 2, 3]})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == [1, 2, 3]
   

# Generated at 2022-06-12 21:21:43.694138
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Make sure it is a function
    assert cliargs_deferred_get('test')
    # Make sure that it returns the value of the global config object
    CLIARGS['test'] = 'foo'
    assert cliargs_deferred_get('test')() == 'foo'
    # Make sure that it can accept an optional default
    assert cliargs_deferred_get('test2', default='bar')() == 'bar'
    # Make sure that it returns a copy of the object when shallowcopy
    CLIARGS['test3'] = 'baz'
    assert cliargs_deferred_get('test3', shallowcopy=True)() == 'baz'
    # Make sure it returns a copy of the sequence when shallowcopy and value is a sequence
    CLIARGS['test4'] = [1, 2]
    assert cl

# Generated at 2022-06-12 21:21:55.353716
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Dummy(object):
        def __init__(self, content):
            self.content = content

    # Default is returned if key is not set
    CLIARGS.setdefault('foo', 'bar')
    assert cliargs_deferred_get('bar', default='baz')() == 'baz'
    # Existing value is returned if key is set
    assert cliargs_deferred_get('foo')() == 'bar'
    # Shallow copy is correct for strings
    assert cliargs_deferred_get('foo', shallowcopy=True)() != 'bar'
    # Shallow copy is correct for sequences
    assert cliargs_deferred_get('compile_callable_whitelist', shallowcopy=True)() != ['copy', 'file']
    # Shallow copy is correct for mappings

# Generated at 2022-06-12 21:22:04.930975
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils._text import to_native

    class CLIArgsClass(object):
        def __init__(self, items):
            self._items = items

        def get(self, key, default=None):
            return self._items[key]

    # Create 2 nested lists so we can make sure that shallow copying works
    cli_args = CLIArgsClass({'foo': [[1, 2], 'bar']})
    cliargs_get = cliargs_deferred_get('foo')
    old_cliarags = CLIARGS


# Generated at 2022-06-12 21:22:15.767087
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # no scope
    _init_global_context(dict(foo='bar', baz=dict(a=1, b=2)))
    assert cliargs_deferred_get('foo') == 'bar'
    assert cliargs_deferred_get('baz') == dict(a=1, b=2)
    assert cliargs_deferred_get('baz', shallowcopy=True) != dict(a=1, b=2)
    assert cliargs_deferred_get('baz', shallowcopy=True) == dict(a=1, b=2)
    assert cliargs_deferred_get('baz', shallowcopy=True) == dict(a=1, b=2)
    # empty scope

# Generated at 2022-06-12 21:22:24.868668
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import Iterable
    from ansible.module_utils.common.collections import is_sequence
    cli_args = {'test1': 'value1', 'test2': 'value2', 'test3': {'key': 'value'}, 'test4': ['item1', 'item2'], 'test5': b'bytes'}
    _init_global_context(cli_args)

    # Makes sure that the function gets the right value and respects the shallowcopy option
    assert cliargs_deferred_get('test1')() == cli_args['test1']
    assert cliargs_deferred_get('test2')() == cli_args['test2']
    assert cliargs_def

# Generated at 2022-06-12 21:22:36.629635
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test regular usage
    CLIARGS = CLIArgs({"foo": "bar"})
    dget = cliargs_deferred_get("foo")
    assert dget() == "bar"
    # Test that the default value is used when key doesn't exist
    dget = cliargs_deferred_get("doesnotexist", "bar")
    assert dget() == "bar"
    dget = cliargs_deferred_get("doesnotexist", [])
    assert dget() == []
    # Test that lists are shallow copied
    CLIARGS = CLIArgs({"foo": ["bar1", "bar2"]})
    dget = cliargs_deferred_get("foo", shallowcopy=True)
    assert dget() == ["bar1", "bar2"]

# Generated at 2022-06-12 21:22:45.850795
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.cli.argparser import CLIArgParser

    # Create a context, set a few keys to it and set it to global context
    args = CLIArgParser(['--connection=local', '-i', 'localhost,']).parse_args()
    cliargs = GlobalCLIArgs.from_options(args)
    keys = ['connection', 'inventory', 'module_path']
    values = ['foo', ['bar', 'baz'], '/fake/path']
    for key, value in zip(keys, values):
        cliargs[key] = value

    # Normal case, no copy
    for key, value in zip(keys, values):
        assert cliargs_deferred_get(key) == value
    
    # Shallow copy case
    new_

# Generated at 2022-06-12 21:22:56.968036
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS_COPY = CLIARGS
    global CLIARGS
    CLIARGS = CLIArgs({'a': 1, 'b': 2, 'c': 3, 'd': [4, 5, 6], 'e': {7: 8, 9: 10}, 'f': set((11, 12, 13)), 'g': None, 'h': False})

# Generated at 2022-06-12 21:23:06.303873
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_me(cur_v, new_v):
        global CLIARGS
        local_v = CLIARGS
        CLIARGS = new_v
        try:
            return cur_v()
        finally:
            CLIARGS = local_v

    local_v = cliargs_deferred_get('new_key', default='val')
    assert test_me(local_v, CLIArgs({})) == 'val'
    assert test_me(local_v, CLIArgs({'new_key': 'testing'})) == 'testing'
    assert test_me(local_v, CLIArgs({'new_key': ['testing', 'more', 'stuff']})) == ['testing', 'more', 'stuff']

# Generated at 2022-06-12 21:23:15.684761
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pragma: no cover
    cli_args = {'a':'xyz', 'b':[1,2,3], 'c':{'d':5, 'e':6}, 'f':{7,8,9}}
    _init_global_context(cli_args)
    assert list(cli_args.keys()) == list(CLIARGS.keys())
    for k, v in cli_args.items():
        assert cliargs_deferred_get(k)() == v
        if is_sequence(v):
            assert cliargs_deferred_get(k, shallowcopy=True)() is not v
        elif isinstance(v, (Mapping, Set)):
            assert cliargs_deferred_get(k, shallowcopy=True)() is not v
        else:
            assert cl

# Generated at 2022-06-12 21:23:52.020957
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIARGS._replace(dict(a='foo', b=123, c=('x', 'y', 'z'), d='bar'))
    fn = cliargs_deferred_get('a')
    assert fn() == 'foo'
    CLIARGS = CLIARGS._replace(dict(a='baz'))
    assert fn() == 'baz'
    fn = cliargs_deferred_get('b')
    assert fn() == 123
    CLIARGS = CLIARGS._replace(dict(b=456))
    assert fn() == 456
    fn = cliargs_deferred_get('c', shallowcopy=True)
    assert fn() == ('x', 'y', 'z')

# Generated at 2022-06-12 21:24:03.011500
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # test that it gets the value from CLIARGS
    CLIARGS.update({"test_key_for_default": "test_value_for_default"})
    deferred_get_value = cliargs_deferred_get("test_key_for_default")
    assert deferred_get_value() == "test_value_for_default"
    # test that we get the system-default based on the type
    deferred_get_value = cliargs_deferred_get("test_key_for_type", default=None)
    assert deferred_get_value() == []
    # test that we can override the type-based system-default
    deferred_get_value = cliargs_deferred_get("test_key_for_type", default=42)
    assert deferred_get_value() == 42
    # test that we

# Generated at 2022-06-12 21:24:09.675379
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({})
    assert cliargs_deferred_get('a', default=1)() == 1
    _init_global_context({'a': 1})
    assert cliargs_deferred_get('a', default=2)() == 1
    _init_global_context({'a': 1})
    assert cliargs_deferred_get('a', default=2, shallowcopy=True)() == 1

# Generated at 2022-06-12 21:24:20.767142
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Set up a dummy CLIARGS
    from ansible.utils.context_objects import CLIArgs
    global CLIARGS
    CLIARGS = CLIArgs({'x': 1, 'y': 'string', 'z': [1, 2]})

    # Test that we can get values from it
    assert cliargs_deferred_get('x')() == 1
    assert cliargs_deferred_get('y')() == 'string'
    assert cliargs_deferred_get('z')() == [1, 2]
    assert cliargs_deferred_get('x', default='default')() == 1
    assert cliargs_deferred_get('notthere', default='default')() == 'default'

    # Test that shallow=True makes copies

# Generated at 2022-06-12 21:24:32.339066
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    class CliArgs(dict):
        def get(self, key, default=None):
            return self.get(key, default=default)

    global CLIARGS
    CLIARGS = CliArgs({'foo':'bar'})

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('not_here', 'default')() == 'default'
    assert cliargs_deferred_get('not_here')('default') == 'default'

    CLIARGS['foo'] = ['one', 'two', 'three']
    assert cliargs_deferred_get('foo')(shallowcopy=True) == ['one', 'two', 'three']

# Generated at 2022-06-12 21:24:38.742493
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    assert cliargs_deferred_get('determined_default')() is None

    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('determined_default')() is None

    CLIARGS = CLIArgs({'determined_default': 'Not None'})
    assert cliargs_deferred_get('determined_default')() == 'Not None'

# Generated at 2022-06-12 21:24:47.558575
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping, Set
    values = (1, 'a', [1, 2], {'b': 2}, {'b'})
    for value in values:
        res = cliargs_deferred_get('nonexistent_value', value)()
        assert value == res, 'Value returned should be the same'

        if is_sequence(value):
            res = cliargs_deferred_get('nonexistent_value', value, True)()
            assert value[:] == res, 'Value returned should be a shallow copy of the original'

# Generated at 2022-06-12 21:24:58.070274
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class CLIArgsStub(CLIArgs):
        # We need a global mutable here....
        updated = False

        def __getitem__(self, key):
            if self.updated:
                return self.data[key]
            raise KeyError(key)

        def get(self, key, default=None):
            if self.updated:
                return self.data.get(key, default=default)
            return default

        def __setitem__(self, key, value):
            self.updated = True
            self.data[key] = value

    CLIARGS = CLIArgsStub({})
    inner = cliargs_deferred_get('foo')

    assert inner() is None

    CLIARGS['foo'] = 'bar'
    assert inner() == 'bar'
