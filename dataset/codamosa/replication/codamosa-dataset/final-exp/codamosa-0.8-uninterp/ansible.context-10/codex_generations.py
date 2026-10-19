

# Generated at 2022-06-12 21:15:08.579688
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the function cliargs_deferred_get"""
    global CLIARGS
    sample_cliargs = {'a': 1, 'b': 'foo', 'c': [1,2,3], 'd': {'foo': 'bar'}, 'e': {'foo', 'bar'}}
    CLIARGS = CLIArgs(sample_cliargs)

    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() == 'foo'
    assert cliargs_deferred_get('c')() == [1,2,3]
    assert cliargs_deferred_get('d')() == {'foo': 'bar'}
    assert cliargs_deferred_get('e')() == {'bar', 'foo'}

    assert cliargs_

# Generated at 2022-06-12 21:15:17.037701
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    import os
    from ansible.utils.context_objects import GlobalCLIArgs


# Generated at 2022-06-12 21:15:24.872287
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('no-such-key', default=False)()
    cli_args = {'foo': {'bar': 'frobnicate'}}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')().get('bar') == 'frobnicate'
    assert cliargs_deferred_get('no-such-key', default=False)() == False
    assert cliargs_deferred_get('foo', shallowcopy=True)() != cliargs_deferred_get('foo')()

# Generated at 2022-06-12 21:15:35.405941
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get

    This function is not directly bound to ``CliArgs`` so that it works with
    ``CLIARGS`` being replaced
    """
    from contextvars import Token
    class GlobalCLIArgsMock:
        def __init__(self, value):
            self.value = value

        def get(self, x=None, default=None):
            if x is None:
                return self.value
            return self.value.get(x, default)

    global CLIARGS
    gca_token = Token.new_token()
    gca_value = '__gca_value'
    CLIARGS.set(gca_token, gca_value)
    assert cliargs_deferred_get(None)() == gca_value
    assert cliargs_

# Generated at 2022-06-12 21:15:47.197021
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils._text import to_bytes
    from itertools import permutations
    # We don't use a MappingProxyType here because we want to be able to mutate
    # the dictionary and we want to be able to have a default value we can test
    # that the function uses
    mutable_dict = {'a': 2, 'b': 'hello'}
    default_dict = {'default': 'value'}
    args = {'key': 'a', 'default': 'default', 'shallowcopy': False}
    pytest_generate_tests = [[False, False], [True, False], [False, True], [True, True]]

# Generated at 2022-06-12 21:15:51.422771
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'test': {'key': 'value'}})
    assert cliargs_deferred_get('test') == {'key': 'value'}
    assert cliargs_deferred_get('test', shallowcopy=True) == {'key': 'value'}

# Generated at 2022-06-12 21:16:01.482248
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Ensure that the deferred get works correctly"""
    global CLIARGS
    CLIARGS = CLIArgs({'test': True})
    assert cliargs_deferred_get('test')(), "Deferred get did not work with true"
    CLIARGS = CLIArgs({'test': False})
    assert not cliargs_deferred_get('test')(), "Deferred get did not work with false"
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('test', default=True)(), "Deferred get did not return default"
    inner_dict = {'a': 1, 'b': 2}
    CLIARGS = CLIArgs({'test': [1, inner_dict]})
    result = cliargs_deferred_get('test', shallowcopy=True)()

# Generated at 2022-06-12 21:16:13.438392
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get

    Ensure that the closure returns the right type and that the value passed as default is
    used if not in ``CLIARGS``.
    """
    assert type(cliargs_deferred_get('Nonexistent', 'value')) == type(cliargs_deferred_get('Nonexistent', 'value'))

    assert cliargs_deferred_get('Nonexistent', 'value')() == 'value'
    assert cliargs_deferred_get('Nonexistent', False)() is False
    assert cliargs_deferred_get('Nonexistent', None)() is None
    assert cliargs_deferred_get('Nonexistent', 42)() == 42
    assert cliargs_deferred_get('Nonexistent', [])() == []
    assert cl

# Generated at 2022-06-12 21:16:23.581185
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    global CLIARGS

    cli_args = {
        "verbosity": 5,
        "b": [3, 4],
        "a": {1: 2, 3: 4},
        "c": set([1, 2])
    }
    CLIARGS = GlobalCLIArgs.from_options(cli_args)

    cliargs_deferred_get('verbosity')()
    cliargs_deferred_get('b')()
    cliargs_deferred_get('a')()
    cliargs_deferred_get('c')()
    cliargs_deferred_get('d')()

    cliargs_deferred_get('verbosity', shallowcopy=True)()

# Generated at 2022-06-12 21:16:33.711805
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check(value):
        """Test against value"""
        assert value == "value"

    try:
        del CLIARGS['foo']
    except KeyError:
        pass

    # Check getting the default value
    assert cliargs_deferred_get('foo', "value")() == "value"
    assert cliargs_deferred_get('foo', "value", True)() == "value"

    # Check getting the real value
    CLIARGS['foo'] = "value"
    assert cliargs_deferred_get('foo', "value")() == "value"
    assert cliargs_deferred_get('foo', "value", True)() == "value"

    # Check that shallowcopy works
    CLIARGS['foo'] = ["value"]
    assert cliargs_deferred_get('foo', None)

# Generated at 2022-06-12 21:16:44.891741
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

# Generated at 2022-06-12 21:16:55.078418
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = dict(
        foo='bar',
        toys=['teddy', 'train', 'truck'],
    )

    _init_global_context(cli_args)

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('toys')() == ['teddy', 'train', 'truck']

    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('toys', shallowcopy=True)()[:] == ['teddy', 'train', 'truck']
    assert cliargs_deferred_get('toys', shallowcopy=True)() is not cliargs_deferred_get('toys')()



# Generated at 2022-06-12 21:17:06.585748
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:17:17.022015
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'foo': {'bar': 'baz'}, 'spam': [1, 2, 3]})
    assert cliargs_deferred_get('foo')().get('bar') == 'baz'
    assert cliargs_deferred_get('missing', default='default')().get('missing') == 'default'

    # Test sequence cloning
    assert cliargs_deferred_get('spam')().pop(0) == 1
    assert cliargs.get('spam').pop(0) == 1  # Original argument should be unchanged
    assert cliargs_deferred_get('spam', shallowcopy=True)().pop(0) == 2

    # Test dictionary cloning
    assert cliargs_deferred_get('foo')().pop('bar') == 'baz'
   

# Generated at 2022-06-12 21:17:28.560198
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['test_key'] = 'test_value'
    func = cliargs_deferred_get('test_key')
    assert func() == 'test_value'
    assert cliargs_deferred_get('test_key', default='test_default')() == 'test_value'
    assert cliargs_deferred_get('bad_key', 'test_default')() == 'test_default'
    predefined_list = [1, 2, 3]
    CLIARGS['test_list'] = predefined_list
    assert id(predefined_list) == id(cliargs_deferred_get('test_list')())
    assert id(predefined_list) != id(cliargs_deferred_get('test_list', shallowcopy=True)())

# Generated at 2022-06-12 21:17:33.168763
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_dict = {'foo': 'bar', '1': 1, 'baz': {'hello': 'world'}}
    global CLIARGS
    CLIARGS = CLIArgs(test_dict)
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('1')() == 1
    assert cliargs_deferred_get('baz')() == {'hello': 'world'}
    func_kwargs = {'default': 10, 'shallowcopy': True}
    assert cliargs_deferred_get('bar', **func_kwargs)() == 10
    assert cliargs_deferred_get('1', **func_kwargs)() == 1

# Generated at 2022-06-12 21:17:43.115340
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert CLIARGS.get('test_key', cliargs_deferred_get('test_key')) == None
    CLIARGS['test_key'] = 1
    assert cliargs_deferred_get('test_key')() == 1
    CLIARGS['test_key'] = 'abc'
    assert cliargs_deferred_get('test_key')('def') == 'abc'

    CLIARGS['test_key'] = set((1, 2, 3))
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == {1, 2, 3}
    CLIARGS['test_key'] = (1, 2, 3)
    assert cliargs_deferred_get('test_key', shallowcopy=True)() == (1, 2, 3)
    CLIARGS

# Generated at 2022-06-12 21:17:53.622776
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function"""
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    global CLIARGS
    cli_args = CLIARGS.copy()
    cli_args['test_key'] = 1, 2, 3

    with mock.patch.object(GlobalCLIArgs, 'from_options') as mock_from_options:
        mock_from_options.return_value = cli_args

        cli_args_deferred_get = cliargs_deferred_get('test_key')

# Generated at 2022-06-12 21:18:02.674637
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    Primarily necessary since the function in question is a closure over
    ``CLIARGS`` which is replaced with a singleton.
    """
    # Ensure we can call the function without a singleton created yet
    cliargs_deferred_get('foo')
    # Create a singleton (the real one creates a singleton using the parsed
    # cli arguments, but for this simple test, we'll just create a simple
    # singleton
    _init_global_context({'foo': 1, 'bar': {'baz': 2}, 'quux': [3, 4, 5]})
    # Test defaults
    assert cliargs_deferred_get('foo', default=10) == 1
    assert cliargs_deferred_get('herp', default=10) == 10

# Generated at 2022-06-12 21:18:14.513171
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert CLIARGS is None
    _init_global_context({})
    assert cliargs_deferred_get('foo')(), None
    assert cliargs_deferred_get('foo', 42)(), 42
    CLIARGS['foo'] = 42
    assert cliargs_deferred_get('foo')(), 42
    CLIARGS['foo'] = ['foo', 'bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)(), ['foo', 'bar']
    assert cliargs_deferred_get('foo')(), ['foo', 'bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)(), ['foo', 'bar']
    CLIARGS['foo'].append('baz')

# Generated at 2022-06-12 21:18:25.973429
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Sequence
    value = 1
    assert cliargs_deferred_get('key')(value) == value
    # Now use a sequence
    value = Sequence([1, 3, 3])
    assert cliargs_deferred_get('key')(value) == value
    assert cliargs_deferred_get('key', shallowcopy=True)(value) != value
    assert cliargs_deferred_get('key', shallowcopy=True)(value) == value[:]
    # Now use a set
    value = set(value)
    assert cliargs_deferred_get('key')(value) == value
    assert cliargs_deferred_get('key', shallowcopy=True)(value) != value

# Generated at 2022-06-12 21:18:37.546352
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Note: we are not testing a call in a 'context'.  This is since we'd need to
    # python2/3 compatible code to create a context and we don't need it for this
    # test.

    data = {'a': 1}
    CLIARGS.update(data)

    f = cliargs_deferred_get('a', shallowcopy=False)
    assert f() == data['a']
    f = cliargs_deferred_get('b', default=2, shallowcopy=False)
    assert f() == 2
    f = cliargs_deferred_get('a', shallowcopy=True)
    assert f() == data['a']
    data['a'] = 2
    assert f() == 1
    f = cliargs_deferred_get('b', default=2, shallowcopy=True)

# Generated at 2022-06-12 21:18:47.483866
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update(dict(a=1, b=[1,2,3], c=dict(d=4, e=5), f={1,2,3}))
    assert cliargs_deferred_get('a') == 1
    assert cliargs_deferred_get('b') == [1,2,3]
    assert cliargs_deferred_get('c') == dict(d=4, e=5)
    assert cliargs_deferred_get('f') == {1,2,3}
    assert cliargs_deferred_get('a', shallowcopy=True) == 1
    assert cliargs_deferred_get('b', shallowcopy=True) == [1,2,3]

# Generated at 2022-06-12 21:18:58.795103
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': {'quux': 'quuz'}, 'lst': [1, 2, 3], 'set': {'a', 'b'}})

    # Testing default behaviour
    assert cliargs_deferred_get('foo')() is 'bar'
    assert cliargs_deferred_get('baz')() == {'quux': 'quuz'}
    assert cliargs_deferred_get('lst')() == [1, 2, 3]
    assert cliargs_deferred_get('set')() == {'a', 'b'}

    # Testing default value
    assert cliargs_deferred_get('not_found', default='asdf')() == 'asdf'

    # Testing shallow copies

# Generated at 2022-06-12 21:19:09.440375
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Empty dict
    global CLIARGS
    _init_global_context({})
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default=42)() == 42
    assert cliargs_deferred_get('foo', shallowcopy=True)() is None
    assert cliargs_deferred_get('foo', default=42, shallowcopy=True)() == 42

    # basic values
    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default=42)() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs

# Generated at 2022-06-12 21:19:18.179656
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # Test with global CLIARGS dictionary
    CLIARGS = CLIArgs({'foo': 1, 'bar': 'baz'})
    assert cliargs_deferred_get('foo', default=None, shallowcopy=False)() == 1
    assert cliargs_deferred_get('foo', default=None, shallowcopy=True)() == 1
    assert cliargs_deferred_get('bar', default=None, shallowcopy=False)() == 'baz'
    assert cliargs_deferred_get('bar', default=None, shallowcopy=True)() == 'baz'
    assert cliargs_deferred_get('foobar', default=None, shallowcopy=False)() is None
    assert cliargs_deferred_get('foobar', default=None, shallowcopy=True)()

# Generated at 2022-06-12 21:19:26.737692
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    @pytest.fixture
    def orig_cliargs():
        global CLIARGS
        orig = CLIARGS
        CLIARGS = CLIArgs({})
        yield CLIARGS
        CLIARGS = orig

    def test_empty(orig_cliargs):
        assert cliargs_deferred_get('foo') == None

    def test_with_default(orig_cliargs):
        assert cliargs_deferred_get('foo', default='bar') == 'bar'

    def test_with_default_dict(orig_cliargs):
        assert cliargs_deferred_get('foo', default={'a': 'b'}) == {'a': 'b'}


# Generated at 2022-06-12 21:19:38.325579
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS_ORIG = CLIARGS

# Generated at 2022-06-12 21:19:49.243753
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get works as expected"""
    from collections import defaultdict
    from itertools import chain
    from unittest import TestCase

    #
    # Test with a dictionary
    #
    class TestDictCliargsDeferredGet(TestCase):
        """Test the return value when the value of the cliarg is a dict"""
        def setUp(self):
            """Create the context and set the cliarg"""
            global CLIARGS
            CLIARGS = CLIArgs({'key': {'foo': 'bar'}})

        def test_deferred_get(self):
            deferred_get = cliargs_deferred_get('key')
            self.assertEqual(deferred_get(), {'foo': 'bar'})


# Generated at 2022-06-12 21:19:55.932757
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.display import Display
    from ansible.module_utils.common.text.converters import to_text, to_bytes

    class DummyCliArgs(object):
        def __init__(self, data):
            self._data = data

        def get(self, key, default=None):
            return self._data.get(key, default)

    from ansible.module_utils.common.collections import is_sequence


# Generated at 2022-06-12 21:20:11.294461
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:20:16.536602
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # We're just testing that a call to this function actually works in the current context
    # but we're not actually testing all the functionality.  That's covered by the unit tests
    # in ansible.utils.context_objects.CLIArgs
    assert cliargs_deferred_get('foobar')() is None
    CLIARGS.args = {'foobar': 'fooval', 'barbar': 'barval'}
    assert cliargs_deferred_get('foobar')() == 'fooval'
    assert cliargs_deferred_get('barbar')() == 'barval'
    assert cliargs_deferred_get('bazbaz')() is None
    assert cliargs_deferred_get('bazbaz', default='bazval')() == 'bazval'

# Generated at 2022-06-12 21:20:28.850571
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def bind(val):
        return lambda: val

    # Validate basic functionality
    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('baz', default='bar')() == 'bar'
    assert cliargs_deferred_get('baz')() == None

    # Validate shallowcopy
    test_structure = {'foo': 'bar', 'baz': 'quux'}
    _init_global_context({'test': test_structure})
    assert cliargs_deferred_get('test')() == test_structure

# Generated at 2022-06-12 21:20:39.496961
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test case 1
    global CLIARGS
    CLIARGS = CLIArgs({'verbosity': None})
    cliargs_deferred_get_ans = cliargs_deferred_get('verbosity', default=0)
    assert cliargs_deferred_get_ans() == 0

    # Test case 2
    global CLIARGS
    CLIARGS = CLIArgs({'verbosity': 5})
    cliargs_deferred_get_ans = cliargs_deferred_get('verbosity', default=0)
    assert cliargs_deferred_get_ans() == 5

    # Test case 3
    global CLIARGS
    CLIARGS = CLIArgs({'verbosity': 5, 'inventory_plugins': [1, 2, '3']})
    cliargs_deferred_get_ans = cli

# Generated at 2022-06-12 21:20:50.552677
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # First test with a singleton object
    from ansible.utils.context_objects import CLIArgs
    pre_init_cliargs = CLIArgs({'foo': 'bar'})
    pre_init_cliargs.is_singleton = True
    global CLIARGS
    CLIARGS = pre_init_cliargs

    # Now test that it returns the unset value when the CLIArgs have not been initialized
    assert(cliargs_deferred_get('foo')() is None)

    # Initialize the global CLIARGS
    _init_global_context({'foo': 'bar'})

    # Now test that it returns the foo value
    assert(cliargs_deferred_get('foo')() == 'bar')

    # Now test with sequence

# Generated at 2022-06-12 21:20:59.795716
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import types

    # Test the function
    assert cliargs_deferred_get('not_there')() is None
    assert cliargs_deferred_get('not_there', default='boo')() == 'boo'

    temp_cliargs = CLIARGS
    cliargs_dict = {'foo': 1, 'bar': '2'}
    CLIARGS.update(cliargs_dict)
    # Test that it works with the dictionary
    assert cliargs_deferred_get('foo')() == 1
    assert cliargs_deferred_get('bar')() == '2'

    # Replace the CLIARGS with a CLIArgs instance
    CLIARGS = CLIArgs(cliargs_dict)

    # Test that it works for the new object

# Generated at 2022-06-12 21:21:09.565307
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeArgs:
        def __init__(self):
            self.data = {}
        def __getitem__(self, key):
            return self.data[key]
        def get(self, key, default=None):
            return self.data.get(key, default)

    global CLIARGS
    args = FakeArgs()
    CLIARGS = args

    args.data['foo'] = 'bar'
    args.data['bar'] = 'foo'
    args.data['baz'] = [1,2,3,4]
    args.data['cat'] = {'foo':1, 'bar':2}

    get_foo = cliargs_deferred_get('foo')
    assert 'bar' == get_foo()

# Generated at 2022-06-12 21:21:19.643887
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS = CLIArgs({'a': 'b', 'c': [1,2]})
    assert cliargs_deferred_get('a')() == 'b'
    assert cliargs_deferred_get('c')() == [1,2]
    CLIARGS['c'].extend([3,4])
    assert cliargs_deferred_get('c')() == [1,2,3,4]
    assert cliargs_deferred_get('d')() is None
    assert cliargs_deferred_get('d', default='e')() == 'e'
    assert cliargs_deferred_get('c', shallowcopy=True)() == [1,2,3,4]

# Generated at 2022-06-12 21:21:31.124693
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_inner_closure(cliargs_dict):
        global CLIARGS
        CLIARGS = CLIArgs(cliargs_dict)
        get_clioption = cliargs_deferred_get('clioption', default='default_clioption')
        get_listoption = cliargs_deferred_get('listoption', default='default_listoption')
        get_shallowcopy = cliargs_deferred_get('shallowcopy', default='default_shallowcopy', shallowcopy=True)
        get_dflt_keyerror = cliargs_deferred_get('dflt_keyerror')
        get_dflt_nonexistent = cliargs_deferred_get('dflt_nonexistent', default='dflt_nonexistent_default')

        assert get_clioption() == cliargs_

# Generated at 2022-06-12 21:21:38.755438
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    _init_global_context({'foo': 'bar'})
    assert 'bar' == cliargs_deferred_get('foo')()

    _init_global_context({'foo': 'bar'})
    assert 'baz' == cliargs_deferred_get('quux', default='baz')()

    # Test we don't modify the original object
    _init_global_context({'foo': [1, 2, 3]})
    shallow_copy_original = cliargs_deferred_get('foo', shallowcopy=True)()
    assert shallow_copy_original == [1, 2, 3]
    shallow_copy = cliargs_def

# Generated at 2022-06-12 21:21:58.482914
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    test_values = {'key1': 'value1',
                   'key2': ['value2', 'value3'],
                   'key3': {'key31': 'value31', 'key32': 'value32'},
                   'key4': 'value4'}
    # Test default case
    CLIARGS = CLIArgs(test_values)
    assert cliargs_deferred_get('key5')() is None

    # Test normal case
    for key, value in test_values.iteritems():
        assert cliargs_deferred_get(key)() == value

    # Test shallow copy case
    for key, value in test_values.iteritems():
        if isinstance(value, (list, set, frozenset, dict)) and len(value) > 0:
            assert cliargs_

# Generated at 2022-06-12 21:22:09.742114
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # Values that we expect to be shallowcopied
    cliargs_list = ['foo', 'bar', 'baz']
    cliargs_dict = {'foo': 'bar'}
    cliargs_set = set('foo')

    CLIARGS['list'] = cliargs_list
    CLIARGS['dict'] = cliargs_dict
    CLIARGS['set'] = cliargs_set

    # First test, no shallow copy
    cliargs_no_copy = cliargs_deferred_get('list')()
    assert cliargs_no_copy is cliargs_list

    cliargs_no_copy = cliargs_deferred_get('dict')()
    assert cliargs_no_copy is cliargs_dict

    cliargs_no_copy = cliargs_def

# Generated at 2022-06-12 21:22:17.921375
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    inner = cliargs_deferred_get('foo')
    assert inner() == 'bar'
    inner = cliargs_deferred_get('does_not_exist', 'baz')
    assert inner() == 'baz'
    inner = cliargs_deferred_get('baz', shallowcopy=True)
    assert inner() == {}
    inner = cliargs_deferred_get('baz', ['hi', 'my', 'name', 'is'], shallowcopy=True)
    assert inner() == ['hi', 'my', 'name', 'is']

# Generated at 2022-06-12 21:22:26.280529
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    # TODO: Update tests to use GlobalCLIArgs

    def reset_global_context():
        # Reset global context
        global CLIARGS
        CLIARGS = CLIArgs({})

    # Verify that getting key, value pair that has not been set returns default
    reset_global_context()
    assert cliargs_deferred_get('test1')() is None

    # Verify that getting key, value pair that has not been set returns default provided
    reset_global_context()
    assert cliargs_deferred_get('test1', default='default1')() == 'default1'

    # Verify that default value returned is a reference, not a copy of value
    reset_global_context()
    mylist = []
    result = cliargs_deferred_get('test1', default=mylist, shallowcopy=False)

# Generated at 2022-06-12 21:22:38.075667
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _test_scenarios(cli_args):
        expected_value = 'bar'
        cli_args['foo'] = 'bar'
        assert cliargs_deferred_get('foo')() == expected_value
        cli_args['foo'] = 'notbar'
        expected_value = 'baz'
        assert cliargs_deferred_get('foo', default=expected_value)() == expected_value
        assert cliargs_deferred_get('doesnotexist', default=expected_value)() == expected_value
        cli_args['foo'] = ['bar', 'baz']
        expected_value = ['bar', 'baz']
        assert cliargs_deferred_get('foo')() == expected_value
        expected_value = ['bar', 'baz']
        assert cliargs_

# Generated at 2022-06-12 21:22:46.784904
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    test_args = {'a':1, 'b':[1,2], 'c':{'a':1}, 'd':{1,2}}
    CLIARGS = CLIArgs(test_args)

    # without shallowcopy
    for key, value in test_args.items():
        value_deffered = cliargs_deferred_get(key)()
        assert value == value_deffered
        CLIARGS[key] = value_deffered
        value_after_set = CLIARGS[key]
        assert value == value_after_set
        assert value is value_after_set

    # with shallowcopy
    for key, value in test_args.items():
        value_deffered = cliargs_deferred_get(key, default=None, shallowcopy=True)

# Generated at 2022-06-12 21:22:57.918393
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    try:
        CLIARGS.keys
    except AttributeError:
        CLIARGS.keys = lambda: ['a', 'b', 'c', 'd']
        CLIARGS.get = lambda key, default: {
            'a': 'foo',
            'b': [1, 2, 3],
            'c': {'a': 'A', 'b': 'B'},
            'd': set(['A', 'B', 'C']),
            }.get(key, default)

    assert 'foo' == cliargs_deferred_get('a')()
    assert ['1', '2', '3'] == cliargs_deferred_get('b', default=['1', '2', '3'])()
    assert {'a': 'A', 'b': 'B'} == cliargs_deferred

# Generated at 2022-06-12 21:23:04.350780
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'key': 'value'})
    assert cliargs_deferred_get('key')() == 'value'
    assert cliargs_deferred_get('default')('default') == 'default'
    CLIARGS['some_list'] = [1, 2, 3]
    assert cliargs_deferred_get('some_list', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('some_list', shallowcopy=True)()[:] == [1, 2, 3]
    assert cliargs_deferred_get('some_list', shallowcopy=False)()[:] == [1, 2, 3]
    CLIARGS.setdefault('some_dict', {})

# Generated at 2022-06-12 21:23:13.918887
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'foo': 'bar', 'baz': [1, 2, 3], 'perms': {'a': 1, 'b': 2}, 'other': 42})

    # get a value
    assert cliargs_deferred_get('foo')() == 'bar'
    # get a value with a default
    assert cliargs_deferred_get('not_found', default='default')() == 'default'
    # get a value with a shallowcopy
    assert cliargs_deferred_get('baz', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('perms', shallowcopy=True)() == {'a': 1, 'b': 2}
    assert cliargs_deferred_get('other', shallowcopy=True)() == 42

# Generated at 2022-06-12 21:23:23.463080
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_factory(cli_args, key, default, shallowcopy, result):
        _init_global_context(cli_args)
        assert cliargs_deferred_get(key, default, shallowcopy) == result
    cli_args = {'a': 1, 'b': [2, 3], 'c': {'f': 4}, 'd': {5, 6}}
    test_factory(cli_args, 'a', default='d', shallowcopy=False, result=1)
    test_factory(cli_args, 'b', default='d', shallowcopy=False, result=[2, 3])
    test_factory(cli_args, 'c', default='d', shallowcopy=False, result={'f': 4})

# Generated at 2022-06-12 21:23:48.753254
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update(dict(foo=1, bar='baz', baz=['qux', 'foo', 'bar', 'qux'], paz=None))

    inner = cliargs_deferred_get('foo')
    assert inner() == 1

    inner = cliargs_deferred_get('bar')
    assert inner() == 'baz'

    inner = cliargs_deferred_get('baz')
    assert inner() == ['qux', 'foo', 'bar', 'qux']

    inner = cliargs_deferred_get('bar', 'qux')
    assert inner() == 'baz'

    inner = cliargs_deferred_get('paz', 'qux')
    assert inner() == 'qux'


# Generated at 2022-06-12 21:23:53.887996
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() is None
    assert cliargs_deferred_get('bar', default='bat')() == 'bat'
    CLIARGS = CLIArgs({'foo': ['a', 'b']})
    assert cliargs_deferred_get('foo')() == ['a', 'b']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['a', 'b']
    assert cliargs_deferred_get('foo', shallowcopy=True)()[0] == 'a'
    assert cliargs_deferred_get('foo')() == ['a', 'b']
   

# Generated at 2022-06-12 21:24:03.968233
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that the function cliargs_deferred_get acts as expected"""
    # Test case for cliargs_deferred_get with default value
    assert cliargs_deferred_get('default_value_key', default=42)() == 42

    # Test case for cliargs_deferred_get with no default value
    assert cliargs_deferred_get('default_value_key')() is None

    # Test case for cliargs_deferred_get with no shallow copy when getting a list
    assert cliargs_deferred_get('list_value_key', default=[1, 2, 3], shallowcopy=False)() == [1, 2, 3]

    # Test case for cliargs_deferred_get with shallow copy when getting a list

# Generated at 2022-06-12 21:24:15.591228
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    args = {'foo': ['bar'], 'bar': {'baz': 'bat'}, 'baz': 'bat'}
    _init_global_context(args)

    assert cliargs_deferred_get('foo', shallowcopy=True)() == args['foo']
    assert cliargs_deferred_get('bar', shallowcopy=True)() == args['bar']
    assert cliargs_deferred_get('baz', shallowcopy=True)() == args['baz']

    args = {'foo': ['bar'], 'bar': {'baz': 'bat'}, 'baz': 'bat'}
    _init_global_context(args)

    assert cliargs_deferred_get('foo', shallowcopy=False)() == args['foo']

# Generated at 2022-06-12 21:24:23.950467
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test that it returns the default when the context object doesn't have the value
    assert cliargs_deferred_get('foo')() is None

    # Test that it returns the original object when not doing a shallowcopy
    val = (1, 2, 3)
    CLIARGS.update(foo=val)
    assert cliargs_deferred_get('foo')() is val

    # Test that it returns a shallow copy when asked
    assert cliargs_deferred_get('foo', shallowcopy=True)() is not val

# Generated at 2022-06-12 21:24:34.467203
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._options = {
        'test': 'test',
        'test2': ['test2', 'test3']
    }

    # Test with no shallow copy
    assert cliargs_deferred_get('test')() == 'test'
    assert cliargs_deferred_get('test', default='default')() == 'test'
    assert cliargs_deferred_get('test2')() == ['test2', 'test3']
    assert cliargs_deferred_get('test2', default='default')() == ['test2', 'test3']
    assert cliargs_deferred_get('test3')() is None

    # Test with shallow copy
    assert cliargs_deferred_get('test', shallowcopy=True)() == 'test'

# Generated at 2022-06-12 21:24:45.721033
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test ``cliargs_deferred_get``"""
    cli_args = dict(always_show_module_path=False, warning_list=[])
    _init_global_context(cli_args)
    assert cliargs_deferred_get(key='always_show_module_path')()
    assert cliargs_deferred_get(key='warning_list')() == []
    cli_args = dict(always_show_module_path=True, warning_list=['never'])
    _init_global_context(cli_args)
    assert cliargs_deferred_get(key='always_show_module_path')()
    assert cliargs_deferred_get(key='warning_list')() == ['never']

# Generated at 2022-06-12 21:24:57.223636
# Unit test for function cliargs_deferred_get