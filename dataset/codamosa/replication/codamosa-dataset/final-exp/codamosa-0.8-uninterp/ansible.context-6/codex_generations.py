

# Generated at 2022-06-12 21:15:07.387948
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCliArgs(dict):
        """Fake cli_args that can be called to assert certain keys are being accessed"""
        def __init__(self, *args, **kwargs):
            super(TestCliArgs, self).__init__(*args, **kwargs)
            self.keys_accessed = set()
        def __getitem__(self, key):
            self.keys_accessed.add(key)
            return super(TestCliArgs, self).__getitem__(key)
        def __missing__(self, key):
            self.keys_accessed.add(key)
            raise KeyError
        def __bool__(self):
            # Return true if any keys have been accessed
            return bool(self.keys_accessed)


# Generated at 2022-06-12 21:15:13.054954
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': 1})
    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() is None
    assert cliargs_deferred_get('b', default=2)() == 2
    assert cliargs_deferred_get('b', default={'c': 3})() == {'c': 3}
    assert cliargs_deferred_get('a', shallowcopy=True)() == 1
    assert cliargs_deferred_get('b', default=[1], shallowcopy=True)() == [1]
    CLIARGS = CLIArgs({'a': [1]})
    assert cliargs_deferred_get('a', shallowcopy=True)() == [1]

# Generated at 2022-06-12 21:15:20.277068
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=too-many-locals
    """Test creating a closure with cliargs_deferred_get"""
    key = 'test_key'
    default = 'test_default'

    # Initialize CLIARGS to the CLIArgs version, so the GlobalCLIArgs version will replace it
    from ansible.module_utils.common.collections import CLIARGS
    # pylint: disable=no-member
    old_cliargs = CLIARGS
    cliargs = CLIARGS = CLIArgs({})  # pylint: disable=redefined-variable-type

    cliargs_vals = {
        key: 'test_value',
        'not_my_key': 'not_my_val',
    }
    # pylint: disable=no-member

# Generated at 2022-06-12 21:15:31.297911
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'test': ['testing']})

    assert cliargs_deferred_get('test')() == ['testing']
    assert cliargs_deferred_get('test', default=[])() == ['testing']
    assert cliargs_deferred_get('test', default=['test'])() == ['testing']
    assert cliargs_deferred_get('test', shallowcopy=True)() == ['testing']
    assert cliargs_deferred_get('test', shallowcopy=True, default=[])() == ['testing']
    assert cliargs_deferred_get('test', shallowcopy=True, default=['test'])() == ['testing']

    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('test')() is None
    assert cl

# Generated at 2022-06-12 21:15:39.435094
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    a_dict = {'foo': 'bar', 'fooname': {'bar': 'foo'}, 'fooset': set(['bar', 'foo'])}
    b_dict = {'foo': 'baz'}

    f = cliargs_deferred_get('foo')
    assert f() == 'bar'

    g = cliargs_deferred_get('fooname')
    assert g() == {'bar': 'foo'}

    h = cliargs_deferred_get('fooset')
    assert isinstance(h(), set)
    assert h() == set(['bar', 'foo'])

    global CLIARGS
    CLIARGS = CLIArgs(b_dict)
    assert f() == 'baz'
    assert g() == {'bar': 'foo'}
    assert h

# Generated at 2022-06-12 21:15:50.395895
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({"foo": "bar", 'baz': []})
    assert cliargs_deferred_get("foo")() == "bar"
    assert cliargs_deferred_get("foo")() == "bar"
    assert cliargs_deferred_get("foo", shallowcopy=True)() == "bar"
    assert cliargs_deferred_get("baz", shallowcopy=True)() == []
    assert cliargs_deferred_get("foo", default="apple")() == "bar"
    assert cliargs_deferred_get("baz", default="apple")() == []
    assert cliargs_deferred_get("baz")() == []
    assert cliargs_deferred_get("baz", shallowcopy=True)() == []
    assert cliargs_deferred

# Generated at 2022-06-12 21:16:00.824284
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit Test
    """
    d = {}
    d["key"] = cliargs_deferred_get("foo", "bar")
    d["key2"] = cliargs_deferred_get("baz", "buzz")
    d["key3"] = cliargs_deferred_get("key", [])
    d["key4"] = cliargs_deferred_get("key2", set())
    cliargs = {}
    cliargs["foo"] = "baz"
    cliargs["baz"] = ["one", "two", "three"]
    cliargs["key"] = 42
    cliargs["key2"] = {"one": 1, "two": 2}
    _init_global_context(cliargs)
    assert d["key"]() == "baz"

# Generated at 2022-06-12 21:16:12.715387
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeCLIArgs(dict):
        def get(self, key, default=None):
            return super(FakeCLIArgs, self).get(key, default)

    cliargs_deferred_get(None, None)
    assert cliargs_deferred_get(None, 'abc')() == 'abc'
    assert cliargs_deferred_get(None)() is None

    fake_cli_args = FakeCLIArgs(CLIARGS=FakeCLIArgs(
            {'debug': True, 'listtags': ['a', 'b']}))
    fake_get_dict = cliargs_deferred_get('CLIARGS')
    fake_cli_args['CLIARGS'] = fake_cli_args

# Generated at 2022-06-12 21:16:23.022952
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for function cliargs_deferred_get"""
    # Test dictionary
    dictionary = dict(k1=dict(k2='v2'))
    assert cliargs_deferred_get('k1')(dictionary)['k2'] == 'v2'
    assert cliargs_deferred_get('k1', default='no_key')(dictionary)['k2'] == 'v2'
    assert cliargs_deferred_get('no_key', default='no_key')(dictionary) == 'no_key'
    assert cliargs_deferred_get('k1', shallowcopy=True)(dictionary)['k2'] == 'v2'

# Generated at 2022-06-12 21:16:33.578867
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a':1, 'b':[2,3], 'c':{'a':'b'}})
    assert 1 == cliargs_deferred_get('a')
    assert 1 == cliargs_deferred_get('a', default=2)
    assert [2,3] == cliargs_deferred_get('b')
    assert [2,3] == cliargs_deferred_get('b', default=[])
    assert {'a': 'b'} == cliargs_deferred_get('c', default={})
    assert {'a': 'b'} == cliargs_deferred_get('c')
    assert None == cliargs_deferred_get('d', default=None)
    assert None == cliargs_deferred_

# Generated at 2022-06-12 21:16:39.582558
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import cliargs_deferred_get as deferred_get, CLIArgs
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import MutableMapping

    inner_dict = ImmutableDict({'a': 1, 'b': 2})
    outer_dict = {'c': 3, 'd': inner_dict}
    cliargs_object = CLIArgs(outer_dict)

    defn1 = deferred_get('c', default=None, shallowcopy=False)
    assert defn1() == 3
    defn2 = deferred_get('c', default=None, shallowcopy=True)
    assert defn2() == 3
    assert isinstance(defn2(), MutableMapping)

   

# Generated at 2022-06-12 21:16:42.654986
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for the ``cliargs_deferred_get`` function"""
    # Put something in a cliargs
    _init_global_context(dict(foo='bar'))
    assert cliargs_deferred_get('foo')

# Generated at 2022-06-12 21:16:53.461498
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'foo':'bar', 'baz': [1,2,3], 'qux': {1:2, 3:4}})

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz')() == [1, 2, 3]
    assert cliargs_deferred_get('qux')() == {1:2, 3:4}
    assert cliargs_deferred_get('missing')() == None
    assert cliargs_deferred_get('missing', default='default')() == 'default'

    baz = cliargs_deferred_get('baz', shallowcopy=True)
    baz()[0] = 5
    assert CLIARGS.get('baz')[0] == 5

   

# Generated at 2022-06-12 21:17:05.046781
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get
    """
    # Create a dummy context
    _init_global_context({'test': 'dummy'})

    # Create the closure with various values
    dummy_closure = cliargs_deferred_get('test', 'default')
    list_closure = cliargs_deferred_get('test', ['default'], shallowcopy=True)
    dict_closure = cliargs_deferred_get('test', {'default': 'value'}, shallowcopy=True)

    # Get the value and compare to the default
    assert dummy_closure() == 'dummy'
    assert list_closure() == ['dummy']
    assert dict_closure() == {'test': 'dummy'}

    # Get the value, change it, and then compare to the default again
    # These should be different

# Generated at 2022-06-12 21:17:11.089357
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._dict = {'a': 'bar', 'b': [1,2,3]}
    assert 'bar' == cliargs_deferred_get('a')()
    assert 'bar' == cliargs_deferred_get('a', shallowcopy=True)()
    assert ['bar'] == cliargs_deferred_get('a', shallowcopy=True)()
    assert [1,2,3] == cliargs_deferred_get('b')()
    assert [1,2,3] == cliargs_deferred_get('b', shallowcopy=True)()
    assert [1,2,3] == cliargs_deferred_get('b')()

# Generated at 2022-06-12 21:17:19.983580
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that ``cliargs_deferred_get`` does the right thing"""

    from ansible.utils.context_objects import GlobalCLIArgs
    # Make a new GlobalCLIArgs object because ``from_options`` will already have been run for
    # this test
    cliargs = GlobalCLIArgs.from_dict({'foo': 'bar', 'baz': [1,2,3], 'qaz': {'q': 'q'}})

    # Test that the value is returned correctly
    assert cliargs_deferred_get('foo', default='not_there')() == 'bar'
    assert cliargs_deferred_get('baz', default='not_there')() == [1,2,3]

# Generated at 2022-06-12 21:17:31.196006
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # set up a global context
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})

    # test a key that is present in the CliArgs
    result = cliargs_deferred_get('foo')()
    assert result == 'bar'

    # test a key that is missing in the CliArgs, with a default
    new_result = cliargs_deferred_get('you_arent_there', default="I'll be here")()
    assert new_result == "I'll be here"

    # test a key that is missing in the CliArgs, with no default
    new_result = cliargs_deferred_get('you_arent_there')()
    assert new_result is None

    # test a key that is present in the CliArgs, with shallowcopy=True

# Generated at 2022-06-12 21:17:38.567741
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert CLIARGS.get('foo') is None
    default = 12345
    assert cliargs_deferred_get('foo')(default=default) == default
    CLIARGS['foo'] = 12345
    assert cliargs_deferred_get('foo')(default=default) != default
    CLIARGS['foo'] = 12345
    assert cliargs_deferred_get('foo')(default=default) == 12345

# Generated at 2022-06-12 21:17:45.489934
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    global CLIARGS
    input_cliargs = {
        'a': {'a': 'a'},
        'b': [1, 2, 3],
        'c': 'c',
    }
    CLIARGS = CLIArgs(input_cliargs)
    assert cliargs_deferred_get('a')(), input_cliargs['a']
    assert cliargs_deferred_get('b')(), input_cliargs['b']
    assert cliargs_deferred_get('b', default=None)(), input_cliargs['b']
    assert cliargs_deferred_get('c')(), input_cliargs['c']
    assert cliargs_deferred_get('d', default=None)(), None

# Generated at 2022-06-12 21:17:56.545868
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=missing-docstring,too-many-locals
    import copy
    import io
    import os
    import shutil
    import tempfile

    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Set

    from units.mock.cliargs import MockCLIArgs

    def reset_global_context():
        global CLIARGS
        # Reinitialize the default global value.
        CLIARGS = CLIArgs({})

    def create_mutable_object():
        return {'foo': 'bar'}

    def create_immutable_object():
        return (1, 2, 3, 4)

    # py2.7

# Generated at 2022-06-12 21:18:07.320791
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = ['a', 'b', 'c']

    def inner():
        return cliargs_deferred_get('foo', shallowcopy=True)()

    assert inner() is not CLIARGS['foo']

    # individual item also not the same
    assert inner()[0] is CLIARGS['foo'][0]

    # make sure we can call the function more than once
    assert inner() is inner()

# Generated at 2022-06-12 21:18:18.403497
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    def assert_equal(actual, expected, msg=None):
        # Perform an assertion
        if actual != expected:
            raise AssertionError(msg or 'Got {} but expected {}'.format(actual, expected))

    class MockCliArgs(object):
        """A mock wrapper around dict"""
        def __init__(self, options):
            self.options = options

        def __getitem__(self, key):
            return self.options[key]

        def get(self, key, default=None):
            return self.options.get(key, default)

    # Set up the context
    GLOBAL_CLIARGS = CLIARGS

# Generated at 2022-06-12 21:18:27.197276
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function ``cliargs_deferred_get``"""
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible_collections.ansible.community.tests.unit.compat import unittest

    class TestCliArgs(object):
        """Test for ``CliArgs`` objects that are passed to ``GlobalCLIArgs``

        Need to test the ``shallowcopy`` functionality of the ``cliargs_deferred_get``
        """
        def __init__(self, value):
            self.value = value

        def get(self, key, default=None):
            return self.value if key == 'test' else default

    class TestGlobalCLIArgs(GlobalCLIArgs):
        """Test case for ``GlobalCLIArgs``"""

# Generated at 2022-06-12 21:18:38.082213
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.utils.context_objects import cli_options_defaults
    from ansible.utils import context_objects

    cli_args = cli_options_defaults.copy()
    context_objects._init_global_context(cli_args)
    # Should make a copy of the defaults when specifying None
    # as the default
    get_value = cliargs_deferred_get('--verbosity')

    # Check that the bound function returns a copy
    assert get_value() == 0
    # Make sure the copy is deep
    assert get_value() is not False

    # Make sure that the default is returned when CLIARGS doesn't contain
    # the value

# Generated at 2022-06-12 21:18:47.920021
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(test=1, testlist=[1, 2, 3], testset=set([1, 2, 3]), testdict=dict(a=1, b=2)))
    simplevalue = cliargs_deferred_get('test')
    assert simplevalue == 1
    simplevalue = cliargs_deferred_get('test2', default=999)
    assert simplevalue == 999
    listvalue = cliargs_deferred_get('testlist', default=[])
    assert listvalue == [1, 2, 3]
    setvalue = cliargs_deferred_get('testset', default=set())
    assert setvalue == set([1, 2, 3])
    dictvalue = cliargs_deferred_get('testdict', default={})

# Generated at 2022-06-12 21:18:54.859870
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_args = {'foo': 'bar'}
    _init_global_context(test_args)
    value = cliargs_deferred_get('foo')()
    assert value == 'bar'
    assert value is not cliargs_deferred_get('foo')()
    value = cliargs_deferred_get('foo', shallowcopy=True)()
    assert value == 'bar'
    assert value is not cliargs_deferred_get('foo')()

# Generated at 2022-06-12 21:19:02.919234
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get.

    covers the following cases
    - make sure shallowcopy works for list (from default)
    - make sure shallowcopy works for dict (from default)
    - make sure shallowcopy works for set (from default)
    - make sure shallowcopy does not copy for a non-mutable type (from default)
    - make sure shallowcopy works for list (from key)
    - make sure shallowcopy works for dict (from key)
    - make sure shallowcopy works for set (from key)
    - make sure shallowcopy does not copy for a non-mutable type (from key)
    - make sure default value returned if key not in dict
    """
    def dict_match(d1, d2):
        """Quick and dirty dict compare"""

# Generated at 2022-06-12 21:19:14.299893
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.context_objects import MockCLIArgs
    global CLIARGS
    CLIARGS = MockCLIArgs({})

    # Check shallow copy
    CLIARGS['lst'] = [1, 2]
    value = cliargs_deferred_get('lst', shallowcopy=True)()
    assert value is not CLIARGS['lst']
    assert value == CLIARGS['lst']

    # Check shallow copy of dict
    CLIARGS['dict'] = {'a': 'b'}
    value = cliargs_deferred_get('dict', shallowcopy=True)()
    assert value is not CLIARGS['dict']
    assert value == CLIARGS['dict']

    # Check shallow copy of set
    CLIARGS['set'] = {1, 2}
    value

# Generated at 2022-06-12 21:19:24.745179
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the deferred copy
    assert cliargs_deferred_get('random_key', default=1)() == 1
    assert cliargs_deferred_get('random_key', default="1")() == "1"
    assert cliargs_deferred_get('random_key', default=None)() is None
    assert cliargs_deferred_get('random_key', default=[1,2,3], shallowcopy=True)() == [1,2,3]
    assert cliargs_deferred_get('random_key', default=(1,2,3), shallowcopy=True)() == (1,2,3)
    assert cliargs_deferred_get('random_key', default={'a': 1}, shallowcopy=True)() == {'a': 1}
    assert cliargs_deferred_

# Generated at 2022-06-12 21:19:35.839481
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCLIArgs(GlobalCLIArgs):
        def __init__(self):
            super(TestCLIArgs, self).__init__({'test_key': 'test_value'})

    global CLIARGS
    CLIARGS = TestCLIArgs()

    assert cliargs_deferred_get('test_key', None)() == 'test_value'
    assert cliargs_deferred_get('test_key_not_exists', None)() is None
    assert cliargs_deferred_get('test_key', [])() == 'test_value'

    assert cliargs_deferred_get('test_key', None, True)() == 'test_value'
    assert cliargs_deferred_get('test_key_not_exists', None, True)() is None
    assert cl

# Generated at 2022-06-12 21:19:53.468469
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCLIArgs(dict):
        def get(self, key, default=None):
            return self[key]

    class TestDefault(list):
        def __init__(self):
            self.append("I'm a list!")

    # test getting item
    cli_args = TestCLIArgs({'key1': "foo"})
    get_fn = cliargs_deferred_get('key1')
    assert get_fn() == "foo"

    # test getting default
    cli_args = TestCLIArgs({'key1': "foo"})
    get_fn = cliargs_deferred_get('key2', default=TestDefault())
    assert get_fn() == ["I'm a list!"]
    assert get_fn() == ["I'm a list!"]  # assert we are not doing

# Generated at 2022-06-12 21:20:03.086096
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    global CLIARGS
    CLIARGS = CLIArgs({'context': 2, 'noop': True, 'diff': True})
    get_context = cliargs_deferred_get('context')
    assert get_context() == 2
    CLIARGS = CLIArgs({'context': 3, 'noop': True, 'diff': True})
    assert get_context() == 3
    get_context_deepcopy = cliargs_deferred_get('context', shallowcopy=True)
    assert get_context_deepcopy() == 3
    CLIARGS = CLIArgs({'context': 4, 'noop': True, 'diff': True})
    assert get_context_deepcopy() == 3
    get_default = cliargs_deferred_get('default', default=5)


# Generated at 2022-06-12 21:20:11.162181
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    # pylint: disable=redefined-outer-name

    # Test the closure itself
    cli_args = {}
    _init_global_context(cli_args)
    assert CLIARGS.get('foo', default='bar') == 'bar'
    f = cliargs_deferred_get('foo', default='bar')
    assert f() == 'bar'

    # f() should not be affected by changes in CLIARGS
    CLIARGS = CLIArgs({'foo': 'baz'})
    assert f() == 'bar'

    # f() should not be affected by changes in cli_args
    cli_args['foo'] = 'qux'
    assert f() == 'bar'

    # But if CLIARGS is replaced, f() should reflect that


# Generated at 2022-06-12 21:20:16.380600
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert cliargs_deferred_get('junk')() == None

    CLIARGS = GlobalCLIArgs.from_options({'junk': 1})
    assert cliargs_deferred_get('junk')() == 1
    assert cliargs_deferred_get('junk', default=2)() == 1
    assert cliargs_deferred_get('junk2', default=2)() == 2
    assert cliargs_deferred_get('junk', default=[1, 2, 3])() == 1

    assert cliargs_deferred_get('junk', shallowcopy=False)() == 1
    new_value = cliargs_deferred_get('junk', shallowcopy=True)()
    assert new_value == 1
    new_value = 2
    assert cl

# Generated at 2022-06-12 21:20:24.822531
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'ANSIBLE_FOO': 'bar'}
    _init_global_context(cli_args)

    val_foo = cliargs_deferred_get('ANSIBLE_FOO')
    assert val_foo == 'bar'

    val_bar = cliargs_deferred_get('ANSIBLE_BAR', default='baz')
    assert val_bar == 'baz'

# Generated at 2022-06-12 21:20:32.809471
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update(dict(one=1, list=['a', 'b', 'c'], set=set(['a', 'b', 'c']), dict=dict(a='a', b='b', c='c')))

    # Not calling inner function yet
    get_one = cliargs_deferred_get('one')
    get_one_default = cliargs_deferred_get('one_default', default=1)
    get_list = cliargs_deferred_get('list')
    get_set = cliargs_deferred_get('set')
    get_dict = cliargs_deferred_get('dict')

    # Default of None if key is not found
    get_unknown = cliargs_deferred_get('unknown')

    # Default value when key is not found is same type as

# Generated at 2022-06-12 21:20:41.889327
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.text.converters import to_text


# Generated at 2022-06-12 21:20:52.334518
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs

    # Test with shallow copy
    cliargs = GlobalCLIArgs({'test': [1,2,3]})
    getter = cliargs_deferred_get('test', shallowcopy=True)
    assert getter() == [1,2,3]
    assert getter() is not [1,2,3]

    # Test with deep copy
    cliargs = GlobalCLIArgs({'test': [1,2,3]})
    getter = cliargs_deferred_get('test')
    assert getter() == [1,2,3]
    assert getter() is [1,2,3]

# Generated at 2022-06-12 21:20:56.465238
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    _init_global_context({'test': 42})
    assert cliargs_deferred_get('test', default=99)() == 42
    assert cliargs_deferred_get('not_present', default=99)() == 99

# Generated at 2022-06-12 21:21:08.074358
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'key1': ['one', 'two'], 'key2': {'key2.1': 1}, 'key3': Set([1, 2, 3])})

    get = cliargs_deferred_get('key1', [])
    assert get() == ['one', 'two']
    assert get() != ['one', 'two']
    value = get()
    assert value is not ['one', 'two']

    get = cliargs_deferred_get('key2', {})
    assert get() == {'key2.1': 1}
    assert get() != {'key2.1': 1}
    value = get()
    assert value is not {'key2.1': 1}

    get = cliargs_deferred_get('key3', set())
    assert get() == Set

# Generated at 2022-06-12 21:21:34.784968
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    foo_default = 'bar'
    foo_closure = cliargs_deferred_get('foo', default=foo_default, shallowcopy=True)
    assert foo_default == foo_closure()

    new_value = 'baz'
    CLIARGS['foo'] = new_value
    assert new_value == foo_closure()

    nested_value = [[1], (1,), {1}]
    CLIARGS['foo'] = nested_value
    assert nested_value == foo_closure()

    new_nested = nested_value + [[2], (2,), {2}]
    assert new_nested != foo_closure()
    assert new_nested != CLIARGS['foo']
    assert new_nested[0] == foo_closure()[0]

# Generated at 2022-06-12 21:21:41.336185
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    cliargs_get = cliargs_deferred_get('foo')
    assert cliargs_get() == CLIARGS['foo']
    CLIARGS = CLIArgs({'foo': None})
    assert cliargs_get() == CLIARGS['foo']
    CLIARGS['foo'] = 'baz'
    assert cliargs_get() == CLIARGS['foo']

# Generated at 2022-06-12 21:21:49.845069
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    original_CLIARGS = CLIARGS
    global CLIARGS

    CLIARGS = CLIArgs({'a': 1, 'b': 'foo'})

    # Test get of non-default
    assert 1 == cliargs_deferred_get('a')()

    # Test get with default
    assert 'default' == cliargs_deferred_get('c', default='default')()

    # Test shallow copy
    CLIARGS = CLIArgs({'a': [1, 2, 3], 'b': {'1': 'a', '2': 'b'}})

    assert [1, 2, 3] == cliargs_deferred_get('a', shallowcopy=True)()
    assert {'1': 'a', '2': 'b'} == cliargs_deferred_get('b', shallowcopy=True)

# Generated at 2022-06-12 21:22:00.063326
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils.common.collections import ImmutableDict
    # Because this is usually called from FieldAttribute we have to have it
    # in a function so that the ``get`` call takes place in the function.
    # This is to allow us to set a breakpoint on the function and then do
    # repeated get calls on a similar object
    #
    # So to test this, we need to wrap it in a function.  Use closures to get
    # the desired result

    # Create an object that acts like CLIARGS
    class TempCLIARGS(GlobalCLIArgs):
        def __init__(self, data):
            self.data = data

        def get(self, key, default=None):
            return self.data.get

# Generated at 2022-06-12 21:22:07.563450
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Set up
    CLIARGS['foo'] = 'bar'

    got = cliargs_deferred_get('foo')()
    assert got == 'bar'

    got = cliargs_deferred_get('foo', default='default_value')()
    assert got == 'bar'

    got = cliargs_deferred_get('does_not_exist', default='default_value')()
    assert got == 'default_value'

    # Clean up
    del CLIARGS['foo']

# Generated at 2022-06-12 21:22:18.120498
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    '''Test from module'''
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.utils.context_objects import CLIArgs, GlobalCLIArgs
    import copy

    class TestGlobalCLIArgs(GlobalCLIArgs):
        '''Derived class to override get'''
        def __init__(self, value):
            self._value = value

        def get(self, key=None, default=None):
            '''Override get to trigger exception'''
            retval = copy.copy(self._value)
            if key is None:
                return retval

# Generated at 2022-06-12 21:22:26.422616
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pragma: no cover
    import copy
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.module_utils.facts import wrap_var

    def assertDeepcopy(actual, expected):
        assert expected is not actual
        assert expected == actual

    def assertShallowCopy(actual, expected):
        assert expected is not actual
        assert expected == actual
        assert type(expected) is type(actual)
        if is_sequence(expected):
            assert expected[:] is actual[:]
        elif isinstance(expected, (Mapping, Set)):
            assert expected.copy() is actual.copy()

    # Test falling back to the default
    CLIARGS.clear()
    expected = 'fake ansible_playbook_python'

# Generated at 2022-06-12 21:22:38.213219
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for function cliargs_deferred_get"""
    global CLIARGS

    # this is the typical use case of the function
    # value is a str
    CLIARGS = CLIArgs({'list_tasks': 'list_tasks_val'})
    assert cliargs_deferred_get('list_tasks') == 'list_tasks_val'
    assert cliargs_deferred_get('list_tasks', default='default_val') == 'list_tasks_val'
    assert cliargs_deferred_get('list_tasks', shallowcopy=True) == 'list_tasks_val'
    assert cliargs_deferred_get('list_tasks', default='default_val', shallowcopy=True) == 'list_tasks_val'

    # value is a list
   

# Generated at 2022-06-12 21:22:46.866217
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # invalidate any state
    global CLIARGS

    # test setting CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    CLIARGS = CLIArgs({'foo': 'baz'})
    assert cliargs_deferred_get('foo')() == 'baz'

    # test default behaviour is same as `CLIARGS.get`
    assert cliargs_deferred_get('foo', default='foobar')() == 'baz'
    assert cliargs_deferred_get('foobar', default='foobar')() == 'foobar'

    # test shallowcopy
    mylist = ['a', 'b', 'c']
    CLIARGS = CLIArgs({'foo': mylist})
    assert cl

# Generated at 2022-06-12 21:22:54.770644
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    '''Test function cliargs_deferred_get'''

    cliargs = CLIArgs({'foo': 'bar'})
    cliargs_deferred_get_foo = cliargs_deferred_get('foo')
    assert cliargs_deferred_get_foo() == 'bar'
    cliargs_deferred_get_foo_default_baz = cliargs_deferred_get('foo', default='baz')
    assert cliargs_deferred_get_foo_default_baz() == 'baz'

# Generated at 2022-06-12 21:23:41.920950
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('fugazi')('default_value') == 'default_value'

    # Set some value in the actual CLIARGS value
    CLIARGS['fugazi'] = 'something'
    assert cliargs_deferred_get('fugazi')('default_value') == 'something'

    CLIARGS['fugazi'] = {'not': 'shared'}
    assert cliargs_deferred_get('fugazi', shallowcopy=True)('default_value') == {'not': 'shared'}
    assert cliargs_deferred_get('fugazi')('default_value') is CLIARGS['fugazi']

    CLIARGS['fugazi'] = [1, 2, 3]

# Generated at 2022-06-12 21:23:49.740650
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _set_cli_args(args):
        global CLIARGS

# Generated at 2022-06-12 21:24:01.288965
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check_default(key, default, expected, shallow_expected):
        old_cliargs = CLIARGS
        # Test that the default is returned when the CLIARGS is empty
        CLIARGS = CLIArgs({})
        assert cliargs_deferred_get(key, default) == expected
        assert cliargs_deferred_get(key, default, shallowcopy=True) == shallow_expected
        # Test that the default is returned when the CLIARGS has a different default set
        CLIARGS = CLIArgs({'default_foo': 'bar'})
        assert cliargs_deferred_get(key, default) == expected
        assert cliargs_deferred_get(key, default, shallowcopy=True) == shallow_expected
        assert cliargs_deferred_get('default_foo', 'foo') == 'bar'


# Generated at 2022-06-12 21:24:12.485605
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping, Set
    import copy

    # Shallow copy where not shallow copy
    mutable_value = [1,2,3]
    verify_fn = lambda value: mutable_value is value
    fn = cliargs_deferred_get('mutable', mutable_value)
    assert fn() is mutable_value
    mutable_value.pop()
    assert fn() is mutable_value
    assert fn() == [1,2]

    # Sequence shallow copy
    mutable_value = [1,2,3]
    verify_fn = lambda value: (is_sequence(value) and value == [1,2,3] and value is not mutable_value)


# Generated at 2022-06-12 21:24:24.219106
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = CLIArgs({'a':1, 'b':[1,2,3], 'c':{'d':2}})
    g = cliargs_deferred_get('a')
    assert g() == 1

    cli_args = CLIArgs({'a':1, 'b':[1,2,3], 'c':{'d':2}})
    g = cliargs_deferred_get('b')
    assert g() == [1,2,3]

    cli_args = CLIArgs({'a':1, 'b':[1,2,3], 'c':{'d':2}})
    g = cliargs_deferred_get('b', shallowcopy=True)
    assert g() == [1,2,3]


# Generated at 2022-06-12 21:24:30.201851
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'no_log': True, 'verbosity': 10, 'diff': True})
    assert cliargs_deferred_get('no_log')() == True
    assert cliargs_deferred_get('verbosity')() == 10
    assert cliargs_deferred_get('diff')() == True
    assert cliargs_deferred_get('foobar')() is None

# Generated at 2022-06-12 21:24:41.073719
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # this kind of sucks.  At least make sure the inner function does what
    # we expect
    cli_args = {'foo':'bar'}
    assert cliargs_deferred_get('foo')(cli_args, default=None) == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)(cli_args, default=None) == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)(cli_args, default=None) == 'bar'  # no shallow copy on immutable values
    assert cliargs_deferred_get('foo', default='baz')(cli_args, default=None) == 'bar'

# Generated at 2022-06-12 21:24:47.829213
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Just ensure that the function returns something

    # Pure function, no side effects
    def test_inner():
        assert cliargs_deferred_get('key')(), "Got a value for a default key"

    test_inner()

    # Make sure we can override the value of the key
    def test_inner():
        assert cliargs_deferred_get('key', default='hi')(), "Got a value for a default key"

    test_inner()

    # Make sure we can override the value of the key
    def test_inner():
        assert cliargs_deferred_get('key', default='hi')(), "Got a value for a default key"

    test_inner()

# Generated at 2022-06-12 21:24:58.099066
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class LocalArgs(CLIArgs):
        def __init__(self, args):
            self.args = args
        def get(self, key, default=None):
            return self.args.get(key, default)
    saved_args = CLIARGS