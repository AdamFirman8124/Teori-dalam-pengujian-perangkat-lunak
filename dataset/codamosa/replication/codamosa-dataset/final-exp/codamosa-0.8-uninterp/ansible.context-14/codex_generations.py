

# Generated at 2022-06-12 21:15:06.254744
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    import copy
    cliargs = {
        'raw_value': 'raw',
        'raw_seq': [1, 2, 3],
        'raw_mapping': {'a': 1, 'b': 2},
        'raw_set': {1, 2, 3},
        'copy_value': 'copy',
        'copy_seq': [1, 2, 3],
        'copy_mapping': {'a': 1, 'b': 2},
        'copy_set': {1, 2, 3},
    }
    CLIARGS = CLIArgs(cliargs)
    assert cliargs_deferred_get('raw_value')() is cliargs['raw_value']
    assert cliargs_deferred_get('raw_seq')() is cliargs['raw_seq']
   

# Generated at 2022-06-12 21:15:15.431350
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': ['bar', 'baz'], 'spam': {'eggs': 'sausage', 'beans': 'tomatoes'}})

    assert cliargs_deferred_get('foo')() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']
    assert cliargs_deferred_get('foo')() == ['bar', 'baz']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']

    assert cliargs_deferred_get('spam')() == {'eggs': 'sausage', 'beans': 'tomatoes'}

# Generated at 2022-06-12 21:15:25.451183
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_stack = []

    # Create some proxy objects that act like CLIARGS
    class CLIArgsProxy:
        def __init__(self, value):
            self.value = value

        def get(self, key, default=None):
            return self.value

    def set_CLIARGS(value):
        global CLIARGS
        CLIARGS = CLIArgsProxy(value)

    # Create a wrapper around cliargs_deferred_get that will allow us to record what calls
    # are being made to it
    def cliargs_deferred_get_wrapper(key, default=None, shallowcopy=False):
        cliargs_stack.append((key, default, shallowcopy))
        return cliargs_deferred_get(key, default, shallowcopy)

    # Test the case where we never call the cl

# Generated at 2022-06-12 21:15:33.949882
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._deferred_defaults = {'foo': {'default': 42, 'shallowcopy': False}}
    assert cliargs_deferred_get('foo')() == 42
    CLIARGS.foo = 42
    assert cliargs_deferred_get('foo')() == 42

    CLIARGS.foo = {'a': 42}
    assert cliargs_deferred_get('foo', shallowcopy=True)() == {'a': 42}
    CLIARGS.foo = ['a']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['a']

# Generated at 2022-06-12 21:15:42.718961
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function ``cliargs_deferred_get``"""
    from mock import MagicMock

    # This is a deeper copy of CLIARGS
    CLIARGS_backup = CLIARGS
    CLIARGS = CLIARGS_backup.copy()

    # Test default return value
    default = 'default value'
    assert cliargs_deferred_get('non-existant-key', default=default)() is default

    # Test that the original value is returned if the original is mutable
    value = ['change me']
    assert cliargs_deferred_get('non-existant-key', default=value)() is value
    value.append('changed')
    assert cliargs_deferred_get('non-existant-key', default=value)() is value
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:15:51.568238
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.context_objects import GlobalCLIArgs

    assert cliargs_deferred_get('foo', 'bar')() == 'bar'

    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options({'foo': 'bar'})

    assert cliargs_deferred_get('foo', 'baz')() == 'bar'

    d = {'foo': 'bar'}
    assert cliargs_deferred_get('foo', default=d, shallowcopy=True)() is not d
    assert cliargs_deferred_get('foo', default=d)() is d

# Generated at 2022-06-12 21:16:01.583462
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('foo')(key='bar1') is None
    assert cliargs_deferred_get('foo')(key='bar2', default=2) == 2
    assert cliargs_deferred_get('foo', default=2)(key='bar3') == 2
    assert cliargs_deferred_get('foo')(key='bar4', shallowcopy=True) is None
    assert cliargs_deferred_get('foo')(key='bar5', default=2, shallowcopy=True) == 2
    assert cliargs_deferred_get('foo', default=2)(key='bar6', shallowcopy=True) == 2
    assert cliargs_deferred_get('foo', shallowcopy=True)(key='bar7') is None

# Generated at 2022-06-12 21:16:13.584587
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # For use in unit tests only
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'apple': ['banana', 'pear']})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('apple')() == ['banana', 'pear']
    assert cliargs_deferred_get('apple', shallowcopy=True)() == ['banana', 'pear']
    assert cliargs_deferred_get('orange', ['kiwi', 'mango'])() == ['kiwi', 'mango']
    assert cliargs_deferred_get('orange', ['kiwi', 'mango'], shallowcopy=True)() == ['kiwi', 'mango']

# Generated at 2022-06-12 21:16:23.738756
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set

    CLIARGS.clear()
    assert cliargs_deferred_get('foo')() is None

    CLIARGS['foo'] = 'foo_value'
    assert cliargs_deferred_get('foo')() == 'foo_value'
    assert cliargs_deferred_get('foo', default='default_value')() == 'foo_value'

    CLIARGS['bar'] = 'bar_value'
    assert cliargs_deferred_get('bar')() == 'bar_value'
    assert cliargs_deferred_get('bar', default='default_value')() == 'bar_value'

    CLIARGS['bar'] = ['bar_value']

# Generated at 2022-06-12 21:16:32.981965
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # cliargs_deferred_get should return the value of the key if we set the default
    # value to None
    global CLIARGS
    CLIARGS = GlobalCLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get(key='foo')(), 'bar'
    # It should return the default we pass in if the key is not there
    assert cliargs_deferred_get(key='BAD', default='baz')(), 'baz'

    # The default value should be lazily evaluated
    CLIARGS = GlobalCLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get(key='BAD', default=lambda: 'baz')() == 'baz'

# Generated at 2022-06-12 21:16:44.772137
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import math
    import copy

    # This is a minimal modificatin of the fieldoptions class where
    # the default is a simple number (42), the cli_args are an empty dict,
    # and the cli_args are replaced after the class is created to a
    # dictionary with that number as a value for key 'answer_to_life'
    class AnswerToLife(object):
        answer_to_life = 42

        def __init__(self):
            self._answer_to_life = cliargs_deferred_get('answer_to_life')

        @property
        def answer_to_life(self):
            return self._answer_to_life()

        @answer_to_life.setter
        def answer_to_life(self, value):
            self._answer_to_life = lambda: value

   

# Generated at 2022-06-12 21:16:55.007044
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _try_values(args, expected):
        for arg, expected in zip(args, expected):
            cloner = cliargs_deferred_get('key', default=arg, shallowcopy=True)
            assert cloner() is expected
            cloner = cliargs_deferred_get('key', default=arg, shallowcopy=False)
            assert cloner() is expected

    # Try with a singleton
    x = object()
    _init_global_context({'key': x})
    cloner = cliargs_deferred_get('key', shallowcopy=True)
    assert cloner() is x
    cloner = cliargs_deferred_get('key', shallowcopy=False)
    assert cloner() is x

    # Try with a list
    y = [object(), object(), object()]
    _init

# Generated at 2022-06-12 21:17:06.546219
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=undefined-variable
    global CLIARGS


# Generated at 2022-06-12 21:17:16.979410
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    # pylint: disable=too-few-public-methods, protected-access
    class MutableClass:
        def __init__(self, val):
            self.val = val

    class ImmutableClass:
        def __init__(self, val):
            self._val = val

        @property
        def val(self):
            return self._val

    class MutableSerializableClass(MutableClass):
        def __eq__(self, other):
            return self.val == other.val

        def __repr__(self):
            return 'MutableSerializableClass(%r)' % self.val

        def copy(self):
            return self


# Generated at 2022-06-12 21:17:28.818153
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-argument,unused-variable,expression-not-assigned,unused-wildcard-import
    from .context_tests import test_cliargs_deferred_get as test_func
    from .context_tests import test_context_init as test_context_init
    from .context_tests import MockCliArgs

    # We can't just bind this to the object as the object gets replaced out
    # with a Singleton version in the global context
    def _get(key, default=None, shallowcopy=False):
        value = CLIARGS.get(key, default=default)
        if not shallowcopy:
            return value
        elif is_sequence(value):
            return value[:]
        elif isinstance(value, (Mapping, Set)):
            return value.copy()
       

# Generated at 2022-06-12 21:17:40.320577
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    Test function cliargs_deferred_get.
    """
    global CLIARGS

    class TestArgs(object):
        """
        Used by the tests below
        """
        def __init__(self, args):
            self.args = args
        def get(self, key, default=None):
            return self.args.get(key, default)

    test_args = {
        'list_arg': [1, 2, 3],
        'set_arg': set([1, 2, 3]),
        'dict_arg': {'o': 'xomg'},
        'string_arg': 'afabsf',
        'seq_arg': (1, 2, 3),
    }

    # test of case where key does not exist
    CLIARGS = TestArgs({})
    assert cliargs_

# Generated at 2022-06-12 21:17:46.372968
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest
    from ansible.module_utils.six.moves import builtins

    # Make sure cliargs_deferred_get doesn't call CLIARGS directly
    with pytest.raises(AttributeError):
        cliargs_deferred_get('foo')

    # Make sure the cliargs_deferred_get doesn't error if the cliargs is not set
    with pytest.raises(TypeError):
        cliargs_deferred_get('foo')('bar')

    # Set up some test data
    global_cli_args = dict(baz='foz', spam=list('spam'), eggs=dict(a=1, b=2, c=3))
    global CLIARGS
    CLIARGS = CLIArgs(global_cli_args)

    # Test getting key
    assert cli

# Generated at 2022-06-12 21:17:57.325369
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    class TestContext(GlobalCLIArgs):
        foo = cliargs_deferred_get('foo')

    def test_default():
        TestContext.CLIARGS = TestContext({})
        assert TestContext.foo is None

    def test_shallowcopy_basics():
        TestContext.CLIARGS = TestContext({'foo': 'bar'})
        assert TestContext.foo == 'bar'
        TestContext.CLIARGS = TestContext({'foo': 'baz'})
        assert TestContext.foo == 'baz'

    def test_shallowcopy_sequence():
        TestContext.CLIARGS = TestContext({'foo': ['bar', 'baz']})
        assert TestContext.foo == ['bar', 'baz']
       

# Generated at 2022-06-12 21:18:05.131936
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    _init_global_context({'thekey': 'thevalue',})

    # test some simple key lookups
    assert cliargs_deferred_get('thekey')() == 'thevalue'
    assert cliargs_deferred_get('thekey', shallowcopy=True)() == 'thevalue'
    assert cliargs_deferred_get('notakey')() is None
    assert cliargs_deferred_get('notakey', 'default')() == 'default'

    # test shallow copies
    assert cliargs_deferred_get('notakey', [1, 2, 3])() == [1, 2, 3]
    assert cliargs_deferred_get('notakey', [1, 2, 3], shallowcopy=True)() is not [1, 2, 3]

   

# Generated at 2022-06-12 21:18:16.990018
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('baz', default='baz')() == 'baz'
    assert cliargs_deferred_get('baz') is None
    assert cliargs_deferred_get('baz', default=None)() is None
    assert cliargs_deferred_get('baz', default=[1, 2, 3])() == [1, 2, 3]

    CLIARGS = CLIArgs({'foo': ['bar', 'baz']})

# Generated at 2022-06-12 21:18:27.694159
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.context_objects import CliArgs  # Avoid circular import
    cli_args = CliArgs({
        'inventory_file': 'my.inventory',
        'module_path': 'test_path',
        'extra_vars': ['foo', 'bar'],
    })
    cliargs_global = CliArgs(cli_args)

    global CLIARGS
    CLIARGS = cliargs_global

    # The value for `extra_vars` is a list so this should return a different object when shallow copying
    assert cliargs_deferred_get('extra_vars', shallowcopy=False) is cli_args['extra_vars']

# Generated at 2022-06-12 21:18:38.576533
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping

    _init_global_context({'foo': 'bar', 'answer': 42})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('answer')() == 42
    assert cliargs_deferred_get('does_not_exist', default='baz')() == 'baz'
    assert cliargs_deferred_get('does_not_exist')() is None

    my_dict = {'a': 1, 'b': 2}
    my_set = {'a', 'b'}
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

# Generated at 2022-06-12 21:18:48.243535
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for the cliargs_deferred_get function"""

    import pytest

    # pylint: disable=global-statement
    global CLIARGS

    test_cli_args = {
        'my_key': 'my_value',
        'my_sequence': [1, 2, 3],
        'my_mapping': {'name': 'value'}
    }

    def test_deferred_get(key, default=None, shallowcopy=False):
        value = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()
        return value

    CLIARGS = CLIArgs(test_cli_args)

    assert test_deferred_get('my_key') == 'my_value'

# Generated at 2022-06-12 21:18:59.459737
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:19:01.523111
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Nothing to test here other than it imports.
    # TODO: Come up with some way to write a unit test for this.
    pass

# Generated at 2022-06-12 21:19:13.096256
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import to_sequence, is_sequence

    def do_test(key):
        assert key == 1
        _init_global_context(dict(key=key))
        assert key == 1
        dget = cliargs_deferred_get('key')
        key = dget()
        return key

    key = 1
    assert key == do_test(key)
    assert key == do_test(key)

    key = 'a'
    assert key == do_test(key)
    assert key == do_test(key)

    key = {'a': 1}
    assert key == do_test(key)
    assert key == do_test(key)
    assert do_test(key) is not key

    key = set((1, 2, 3))

# Generated at 2022-06-12 21:19:22.397551
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'username': 'testing_username'})
    assert cliargs_deferred_get('username')(), 'testing_username'
    assert cliargs_deferred_get('password', 'testing_password')(), 'testing_password'

# Test of _init_global_context function
# Note: This function is only ever called from the top level of a python program.
#       It is not referenced from another function so pytest can not call it.
#       It must be called from the top level of an interactive python shell.

# Generated at 2022-06-12 21:19:30.102333
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.removed import removed
    import copy

    # Test for no args or kwargs
    try:
        cliargs_deferred_get()
        assert False
    except TypeError:
        pass

    # Test for no kwargs
    try:
        cliargs_deferred_get('foo')
        assert False
    except TypeError:
        pass

    # Test function creation
    get_func = cliargs_deferred_get('foo', 'bar')
    assert callable(get_func)

    # Test context with nothing in it
    CLIARGS.clear()
    assert get_func() == 'bar'

    # Test context with key and default
    CLIARGS.update({'foo': 'baz'})
    assert get_func() == 'baz'



# Generated at 2022-06-12 21:19:41.023575
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the ``cliargs_deferred_get`` function"""
    global CLIARGS

    class Options(object):
        def __init__(self, options):
            for key, value in options.items():
                setattr(self, key, value)

    # normal get
    cli_args = Options({'foo': 'bar'})
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')(), 'Did not get the value of foo'
    assert cliargs_deferred_get('bar', default='baz')(), 'Did not get the default'

    # get with shallow copy
    cli_args = Options({'foo': [1, 2, 3]})
    _init_global_context(cli_args)
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:19:51.502601
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    # pylint: disable=unused-variable,too-few-public-methods
    class CliArgsMock():
        """Mock class to allow unit testing of deferred cliargs"""
        # pylint: disable=attribute-defined-outside-init
        def __init__(self, cli_args):
            self._cli_args = cli_args

        def get(self, key, default=None):
            return self._cli_args.get(key, default=default)

    field_type = type('field_type', (object,), {})

    args = {'k1': 1, 'k2': [1, 2, 3], 'k3': {'kk1': 1}, 'k4': {1, 2}}
    cli_args = Cl

# Generated at 2022-06-12 21:20:02.634277
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Initial state
    assert not hasattr(CLIARGS, '_is_initialized')
    # Normal value
    CLIARGS = CLIArgs(dict(one=1))
    assert cliargs_deferred_get('one')() == 1
    # Shallow copy of list
    CLIARGS = CLIArgs(dict(one=[1]))
    assert cliargs_deferred_get('one', shallowcopy=True)() == [1]
    # Shallow copy of set
    CLIARGS = CLIArgs(dict(one=set([1])))
    assert cliargs_deferred_get('one', shallowcopy=True)() == set([1])
    # Shallow copy of dict
    CLIARGS = CLIArgs(dict(one=dict(one=1)))
    assert cliargs_def

# Generated at 2022-06-12 21:20:10.888406
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # This is a little involved to set up the test but it ensures we get the right behaviour
    # with a real CLIARGS object and that we get the right behaviour early in initialization
    # when CLIARGS is still an empty dict
    testdata = {'shallow': [1, 2],
                'deep': {1: 2},
                'deepset': {1, 2},
                'trivial': '123',
                'noncopyable': object()}
    for key in testdata:
        CLIARGS[key] = testdata[key]

    for key, shallowcopy in (('shallow', True), ('shallow', False), ('deep', True), ('deep', False), ('deepset', True),
                             ('deepset', False), ('trivial', True), ('trivial', False)):
        value = cliargs_

# Generated at 2022-06-12 21:20:20.257600
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    class MyDict(dict):
        """A custom dict type to test that a shallow copy creates a new object of the same type"""
        pass

    # Test without shallowcopy
    class_type = None
    mydict = MyDict(a=1)
    _init_global_context(dict(a=1))
    assert CLIARGS.get('a') is mydict
    assert cliargs_deferred_get('a') is mydict

    # Test with shallowcopy
    class_type = None
    mydict = MyDict(a=1)
    _init_global_context(dict(a=1))
    assert CLIARGS.get('a') is mydict
    assert cliargs_deferred_get('a', shallowcopy=True) is not mydict

# Generated at 2022-06-12 21:20:29.858836
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs(dict(
        a=1,
        b=2,
        c=3,
        d=[1, 2, 3],
        e={'f': 4},
        l=['a', 'b', 'c'],
        m={'n': 'o', 'p': 'q'},
        n=('a', 'b', 'c'),
        o=('p', 'q', 'r'),
        p='p',
        q='q',
    ))
    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() == 2
    assert cliargs_deferred_get('c')() == 3
    assert cliargs_deferred_get('d')() == [1, 2, 3]

# Generated at 2022-06-12 21:20:39.576085
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    CLIARGS.update(dict(a='a_value', b='b_value', c=[1,2,3], d={'one': 1, 'two': 2}))
    a_key = cliargs_deferred_get('a')
    assert a_key() == 'a_value'
    b_key = cliargs_deferred_get('b')
    assert b_key() == 'b_value'
    c_key = cliargs_deferred_get('c')
    assert c_key() == [1,2,3]
    d_key = cliargs_deferred_get('d')
    assert d_key() == {'one': 1, 'two': 2}
    def_key = cliargs_deferred_get

# Generated at 2022-06-12 21:20:43.355815
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(A=1, B=2, C=[1, 2, 3], D=[None], E={1: 2}))
    assert cliargs_deferred_get('Z')() is None
    assert cliargs_deferred_get('Z', default=1)() == 1
    assert cliargs_deferred_get('A')(1) == 1
    assert cliargs_deferred_get('A', default=1)() == 1
    assert cliargs_deferred_get('C')([1, 2, 3])
    assert cliargs_deferred_get('C', shallowcopy=True)([1, 2, 3])
    assert cliargs_deferred_get('D')([None])

# Generated at 2022-06-12 21:20:53.757732
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def get_value():
        return CLIARGS.get('foo')

    cli_args = CLIArgs({'foo': 'foo'})
    assert get_value() is None
    assert cliargs_deferred_get('foo')() is None

    # Set the global CLIARGS, triggering that function to return the value
    global CLIARGS
    CLIARGS = cli_args
    assert get_value() == 'foo'
    assert cliargs_deferred_get('foo')() == 'foo'

    # Unset the global CLIARGS and make sure the function still returns the value
    CLIARGS = CLIArgs({})
    assert get_value() == 'foo'
    assert cliargs_deferred_get('foo')() == 'foo'

# Generated at 2022-06-12 21:21:01.432034
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': 'bar'}
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Set

    _init_global_context(cli_args)

    test_dict = {'a': 1}
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('a', default=test_dict)() == test_dict
    assert cliargs_deferred_get('a', default=test_dict, shallowcopy=True)() == test_dict

    # Make sure we return a shallow copy

# Generated at 2022-06-12 21:21:02.398983
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the deferred get closure"""
    CLIARGS['test'] = 4
    assert cliargs_deferred_get('test')() == 4

# Generated at 2022-06-12 21:21:09.676952
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common import AnsibleMixin
    class TestClass(AnsibleMixin):
        def __init__(self, foo):
            self.foo = foo
    _init_global_context(dict(foo="bar"))
    obj1 = TestClass(foo=cliargs_deferred_get("foo"))
    assert obj1.foo == 'bar'

    obj2 = TestClass(foo=cliargs_deferred_get("foo", default=[]))
    assert obj2.foo == []

    obj3 = TestClass(foo=cliargs_deferred_get("foo", default=[], shallowcopy=True))
    assert obj3.foo == []
    assert obj3.foo is not []

# Generated at 2022-06-12 21:21:29.368476
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from copy import copy
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common.collections import is_sequence_of_strings

    if PY3:
        import builtins
        BUILTIN_MODULE = builtins
    else:
        import __builtin__ as BUILTIN_MODULE

    # Initialize and setup CLIARGS
    global CLIARGS

# Generated at 2022-06-12 21:21:39.058953
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_equal(value, expected, shallowcopy=False):
        fn = cliargs_deferred_get(value, default=None, shallowcopy=shallowcopy)
        assert fn() == expected

    cli_args = {'foo': 1, 'bar': 2, 'baz': '3',
                'aset': set([1,2,3]),
                'alist': ['a', 'b'],
                'adict': {'a': 1, 'b': 2, 'c': 'foo',
                          'aset': set([1,2,3]),
                          'alist': ['a', 'b'],
                          },
    }
    _init_global_context(cli_args)

    assert_equal('foo', 1)
    assert_equal('bar', 2)

# Generated at 2022-06-12 21:21:46.439443
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'a': [1, 2, 3]})

    assert(CLIARGS.get('foo') == cliargs_deferred_get('foo')())
    assert(CLIARGS.get('a') == cliargs_deferred_get('a')())
    assert(CLIARGS.get('a') is not cliargs_deferred_get('a', shallowcopy=True)())

    with pytest.raises(KeyError):
        assert(CLIARGS['bogus'] == cliargs_deferred_get('bogus')())

    assert('default' == cliargs_deferred_get('bogus', 'default')())

# Generated at 2022-06-12 21:21:57.576492
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    global CLIARGS
    testargs = dict(a=1, b=2, c=[1,2,3], d=dict(x=1, y=2), e=set('abc'))
    CLIARGS = CLIArgs(testargs)

    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() == 2
    assert cliargs_deferred_get('c')() == [1,2,3]
    assert cliargs_deferred_get('d')() == dict(x=1,y=2)
    assert cliargs_deferred_get('e')() == set('abc')

    # Make sure we have shallow copies

# Generated at 2022-06-12 21:21:59.947474
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'a': {'b': 'c'}}
    _init_global_context(cli_args)
    assert cliargs_de

# Generated at 2022-06-12 21:22:11.480202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    class MockCliArgs:
        def __init__(self, data):
            self.data = data

        def get(self, key, default=None):
            return self.data.get(key, default)

    def test_check_basic_type(data, default='foo'):
        cliargs = MockCliArgs(data)
        func = cliargs_deferred_get(key='foo', default=default, shallowcopy=False)
        # Force the function to be bound to the CLIARGS
        func.__defaults__ = (cliargs, )
        assert func() == data.get('foo', default)

    def test_check_mutable_type(data, default):
        cliargs = MockCliArgs(data)

# Generated at 2022-06-12 21:22:20.967615
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_deep_equal(v1, v2):
        if isinstance(v1, (Mapping, Set)):
            return v1 == v2
        assert v1 == v2

    cli_args = {'foo': {'bar': 'baz', 'bak': 'buz'},
                'baz': [1, 2, 3],
                'buz': set([1, 2, 3]),
                }
    _init_global_context(cli_args)

    for key in cli_args:
        assert_deep_equal(cliargs_deferred_get(key, shallowcopy=False)(), cli_args[key])
        assert_deep_equal(cliargs_deferred_get(key, shallowcopy=True)(), cli_args[key])

# Generated at 2022-06-12 21:22:22.850800
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({})
    cliargs_deferred_get('nope', 'b')() == 'b'



# Generated at 2022-06-12 21:22:33.590157
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs(dict(
        test=123,
        test2=[1, 2, 3],
        test3={'a': 1, 'b': 2}
    ))
    assert cliargs_deferred_get('test')() == 123
    assert cliargs_deferred_get('test2')() == [1, 2, 3]
    assert cliargs_deferred_get('test3')() == {'a': 1, 'b': 2}

    assert cliargs_deferred_get('test', shallowcopy=True)() == 123
    assert cliargs_deferred_get('test2', shallowcopy=True)() == [1, 2, 3]

# Generated at 2022-06-12 21:22:44.273679
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable,redefined-outer-name
    import collections
    import copy
    from .context import Context

    def inner():
        return Context({'a': ['b', 'c']})

    def inner2():
        return Context({'a': ['b', 'c']})

    CLIARGS2 = CLIArgs({})
    CLIARGS2.update(inner)

    closure = cliargs_deferred_get('a')
    assert closure() == ['b', 'c']

    assert closure() is closure()

    # Validate we get a different copy if we use the shallow copy functionality
    closure_shallow_copy = cliargs_deferred_get('a', shallowcopy=True)
    # Bunch of ways to prove this is a different copy
    assert closure() is not closure_shallow

# Generated at 2022-06-12 21:23:08.146952
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    backup_cliargs = CLIARGS

    # Make sure the function works with both singletons and a normal object
    for cliargs in [CLIARGS, CLIArgs({'small': 1})]:
        CLIARGS = cliargs

        # When value is not present in the args the default is returned
        assert cliargs_deferred_get('big', default=3)() == 3
        assert CLIARGS.get('big') is None

        # When value is present in the args the value is returned
        assert cliargs_deferred_get('small', default=3)() == 1
        assert CLIARGS.get('small') == 1

        # When value is not present in the args but there is a default and shallowcopy is True
        # the returned value is a shallow copy of the default
        assert cliargs_deferred_get

# Generated at 2022-06-12 21:23:17.876053
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    '''Unit test for function cliargs_deferred_get '''
    # Test case 1
    CLIARGS['verbosity'] = 9
    assert cliargs_deferred_get('verbosity')() == 9
    assert cliargs_deferred_get('verbosity', default=0)() == 9

    # Test case 2
    CLIARGS['verbosity'] = None
    assert cliargs_deferred_get('verbosity', default=0)() == 0

    # Test case 3
    CLIARGS['verbosity'] = 9
    assert cliargs_deferred_get('verbosity',
                                shallowcopy=True)() == CLIARGS['verbosity']
    CLIARGS['verbosity'] = None
    assert cliargs_deferred_get('verbosity',
                                shallowcopy=True)() == CLI

# Generated at 2022-06-12 21:23:26.579691
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'test_key': 'test_value', 'test_empty': [], 'test_list': ['a', 'b', 'c'], 'test_set': set(['d', 'e', 'f'])})
    assert cliargs_deferred_get('test_key')() == 'test_value'
    assert cliargs_deferred_get('test_empty')() == []
    assert cliargs_deferred_get('test_list')() == ['a', 'b', 'c']
    assert cliargs_deferred_get('test_set')() == set(['d', 'e', 'f'])
    assert cliargs_deferred_get('test_key', default=1)() == 'test_value'
    assert cliargs_deferred

# Generated at 2022-06-12 21:23:36.666594
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    global CLIARGS
    test_cli_args = {'foo': 'bar'}
    CLIARGS = CLIArgs(test_cli_args)
    def_get = cliargs_deferred_get('foo')
    assert def_get() is test_cli_args['foo']
    assert def_get() is CLIARGS['foo']

    CLIARGS = CLIArgs({'foo': None})
    def_get = cliargs_deferred_get('foo', 'abc')
    assert def_get() is None
    assert def_get() is CLIARGS['foo']

    CLIARGS = CLIArgs({'foo': None})
    def_get = cliargs_deferred_get('foo', 'abc', True)
    assert def_get() == 'abc'


# Generated at 2022-06-12 21:23:45.967564
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.errors import AnsibleError
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    old_CLIARGS = CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3], 'bam': {'a': 1, 'b': 2}})

    # Test default
    default = cliargs_deferred_get('x', default=None)
    assert default() is None

    # Test shallow copy the default
    default = cliargs_deferred_get('x', default=[1, 2, 3], shallowcopy=True)
    assert default() is not [1, 2, 3]
    assert default() == [1, 2, 3]



# Generated at 2022-06-12 21:23:48.247013
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    try:
        _init_global_context(dict(k=123))
        get_k = cliargs_deferred_get('k')
        assert get_k() == 123
    finally:
        del CLIARGS

# Generated at 2022-06-12 21:23:53.642647
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # does it work on it's own without calling it from within a closure?
    assert cliargs_deferred_get('non-existent key') is None
    assert cliargs_deferred_get('non-existent key', default='default') == 'default'

    CLIARGS['foo'] = 'bar'

    # does it get the correct key, no copy for strings
    assert cliargs_deferred_get('foo') == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True) == 'bar'

    # does it get the correct key, yes copy for list
    seq = ['a', 'b', 'c']
    CLIARGS['seq'] = seq
    assert cliargs_deferred_get('seq') == seq

# Generated at 2022-06-12 21:23:59.173524
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    class my_dict(dict):
        pass

    class my_set(set):
        pass

    class my_tuple(tuple):
        pass

    class my_list(list):
        pass

    class my_str(str):
        pass

    global CLIARGS
    CLIARGS = {}
    assert cliargs_deferred_get('A')(), None

    CLIARGS = {'A': 'B'}
    assert cliargs_deferred_get('A')(), 'B'
    assert cliargs_deferred_get('A', shallowcopy=True)(), 'B'
    assert cliargs_deferred_get('C')(), None
    assert cliargs_deferred_get('C', 'C')(), 'C'

# Generated at 2022-06-12 21:24:04.942170
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(option1='value1', option2='value2'))
    get_val1 = cliargs_deferred_get('option1')
    get_val2 = cliargs_deferred_get('option2')
    copied_val1 = cliargs_deferred_get('option1', shallowcopy=True)
    copied_val2 = cliargs_deferred_get('option2', shallowcopy=True)

    assert CLIARGS['option1'] is get_val1()
    assert CLIARGS['option2'] is get_val2()
    assert CLIARGS['option1'] is not copied_val1()
    assert CLIARGS['option2'] is not copied_val2()

# Generated at 2022-06-12 21:24:16.732300
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test getting a value from CLIARGS with shallow copy functionality

    This unit test verifies that ``cliargs_deferred_get()`` does the following:
    - Retrieves the current value of a key from ``CLIARGS``
    - Returns a copy of the value if ``shallowcopy`` is set to ``True``
    - Returns the original value if ``shallowcopy`` is set to ``False``
    """
    # Create a dict with some values to test

# Generated at 2022-06-12 21:24:58.155002
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = GlobalCLIArgs.from_options({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'

    cliargs = GlobalCLIArgs.from_options({'foo': 'bar', 'bar': 'foo'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() == 'foo'

    cliargs = GlobalCLIArgs.from_options({'foo': 'bar', 'bar': 'foo'})
    assert cliargs_deferred_get('foobar')() is None
    assert cliargs_deferred_get('foobar', default='baz')() == 'baz'
