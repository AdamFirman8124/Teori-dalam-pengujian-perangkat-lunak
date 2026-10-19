

# Generated at 2022-06-12 21:15:08.466041
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from copy import deepcopy
    def foo():
        pass

    CLIARGS.clear()
    CLIARGS.update({'foo': 'bar',
                    'baz': 'wibble',
                    'spam': 'eggs',
                    'a_tuple': ('larry', 'curly'),
                    'a_dict': {'none': None, 'empty_list': [], 'empty_dict': {}},
                    'a_set': set(['a', 'b']),
                    'a_frozenset': frozenset(['c', 'd']),
                    'a_function': foo})
    CLIARGS.update(ImmutableDict(IMMUTABLEDICT={'immutabledict': 'should be returned as is'}))

# Generated at 2022-06-12 21:15:16.924635
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=too-many-locals
    """Ensure cliargs_deferred_get behaves correctly"""
    global CLIARGS
    args = ['--force-handlers', '--module-path=/path/to/module', '--extra-vars=a=1 b=2']
    parser = GlobalCLIArgs.create_parser(args)
    cli_args = parser.parse_args()
    _init_global_context(cli_args)
    a = cliargs_deferred_get('force_handlers')
    assert a() is True

    b = cliargs_deferred_get('module_path')
    assert b() == '/path/to/module'

    c = cliargs_deferred_get('extra_vars')

# Generated at 2022-06-12 21:15:27.210304
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    from ansible.module_utils.common._collections_compat import MutableSequence, MutableMapping
    from collections import OrderedDict, defaultdict
    from ansible.module_utils._text import to_text
    import ansible.utils.context_objects

    gargs_init = OrderedDict((
        (u'vault-password-file', u'/test/path'),
        (u'someoption', u'value'),
    ))
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options(gargs_init)

    # Test get a value that's in the context
    assert CLIARGS.get(u'someoption', default=u'value') == u'value'
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:15:37.435978
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    args = dict(a='a', b=1, c=['c'], d=dict(e='e'))
    from ansible.utils.context_objects import GlobalCLIArgs
    global CLIARGS
    CLIARGS = GlobalCLIArgs.from_options(args)
    # Don't use shallow copy
    a = cliargs_deferred_get('a')()
    b = cliargs_deferred_get('b')()
    c = cliargs_deferred_get('c')()
    d = cliargs_deferred_get('d')()
    assert a is args['a']
    assert b is args['b']
    assert c is args['c']
    assert d is args['d']

    # Use shallow copy

# Generated at 2022-06-12 21:15:48.903516
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    import pytest

    try:
        # pylint: disable=unused-import
        from unittest.mock import MagicMock, patch
    except ImportError:
        from mock import MagicMock, patch

    from ansible.context import cliargs_deferred_get

    mock_cli_args = MagicMock(spec=['get'])

    # Test default and copy
    mock_cli_args.get.return_value = 'default'
    assert cliargs_deferred_get('a')(shallowcopy=False) == 'default'
    assert cliargs_deferred_get('a')(shallowcopy=True) == 'default'

    assert cliargs_deferred_get('a', 'other')(shallowcopy=False) == 'other'
    assert cliargs_

# Generated at 2022-06-12 21:15:59.683689
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function ``cliargs_deferred_get``"""
    def test_function(key, default=None, shallowcopy=False, cliargs=CLIARGS):
        """Test the closure over the cliargs function"""
        return cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()
    CLIBYTES = b'bytesstring'
    CLISTR = 'string'
    CLIINT = 1
    CLIBOOL = False
    CLIBOOLTRUE = True
    CLILIST = [1, 2]
    CLITUPLE = (1, 2)
    CLIDICT = dict(a=1, b=2)
    CLISET = set(CLILIST)

# Generated at 2022-06-12 21:16:04.731099
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    cli_args = GlobalCLIArgs.from_options({})
    assert cliargs_deferred_get('foo')() is None
    cli_args['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'

# Generated at 2022-06-12 21:16:15.585207
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common.text.converters import to_bytes
    # Original object
    original_cliargs = OrderedDict((
        ("first", u'string'),
        ("second", {u'asdf': True, u'composite': (1, 2, 3, u'four')}),
        ("third", [u'one', {"two": 2}]),
    ))

    # Test first get
    CLIARGS = CLIArgs(original_cliargs)
    get_first = cliargs_deferred_get("first")
    assert get_first() == u"string"

# Generated at 2022-06-12 21:16:20.208076
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Note: The only way to test this is to mock out CLIARGS but I didn't want to
    # mock out the whole framework to do that so only test that it returns the function
    # that it's supposed to.
    inner = cliargs_deferred_get('foo')
    assert callable(inner)

# Generated at 2022-06-12 21:16:30.993369
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    def check_get(key, default=None, shallowcopy=False):
        CLIARGS = CLIArgs({key: 'foo'})

        result = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()
        assert result == 'foo'

        CLIARGS = CLIArgs({})

        result = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()
        assert result == default

    def check_get_copy(key):
        from copy import deepcopy
        from ansible.module_utils.common._collections_compat import Mapping, Set

        CLIARGS = CLIArgs({key: 'foo'})  # string
        assert cliargs_deferred_get(key, shallowcopy=True)() == 'foo'



# Generated at 2022-06-12 21:16:43.915812
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable, protected-access
    """Test function cliargs_deferred_get"""

    # Create a fake object for CLIARGS
    class FakeCLIARGS(object):
        """Fake CLIARGS object"""
        def get(self, key, default=None):
            """Fake CLIARGS.get"""
            if key == 'foo':
                return 'bar'

    # Create the global variable to hold the fake object so it will be seen when
    # we invoke the cliargs_deferred_get function
    CLIARGS = FakeCLIARGS()

    # Get the closure around the function
    inner_func = cliargs_deferred_get('foo', default=None, shallowcopy=False)

    # Call the closure and check the value to make sure it works
    assert inner_func

# Generated at 2022-06-12 21:16:54.355060
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for the cliargs_deferred_get function"""
    # Have to set a default value because the CLIARGS is not created when this
    # test runs
    cliargs_deferred_get.key = 'test'
    default = True
    key = cliargs_deferred_get.key

    # Test normal case
    cliargs_value = 'test'
    CLIARGS = CLIArgs({key: cliargs_value})
    value = cliargs_deferred_get(key, default=default, shallowcopy=False)()
    assert value == cliargs_value

    # Test shallow copy case
    cliargs_value = ['test']
    CLIARGS = CLIArgs({key: cliargs_value})

# Generated at 2022-06-12 21:17:05.956892
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import CLIArgs
    cli_args = CLIArgs({'foo': 'bar'})
    _init_global_context(cli_args)
    assert cliargs_deferred_get('foo')() == 'bar'
    cli_args = CLIArgs({'foo': 'bar'})
    cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'baz'
    cli_args = CLIArgs({'foo': ['bar', 'baz']})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar', 'baz']
    cli_args = CLIArgs({'foo': {'bar': 'baz'}})
    assert cli

# Generated at 2022-06-12 21:17:16.442384
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=missing-function-docstring
    CLIARGS.update({
        'foo': 'bar',
        'baz': [1, 2, 3],
        'qux': {'foo': 'bar'},
    })
    foo_value = cliargs_deferred_get('foo')
    baz_value = cliargs_deferred_get('baz', shallowcopy=True)
    qux_value = cliargs_deferred_get('qux', shallowcopy=True)
    assert foo_value() == 'bar'
    del CLIARGS['foo']
    # Because we use a closure, the old value is still cached
    assert foo_value() == 'bar'
    # But using new values work correctly

# Generated at 2022-06-12 21:17:23.393938
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """ Unit tests for the cliargs_deferred_get helper function"""
    # This is checking that the function accepts a key that is invalid and
    # returns the default passed in
    assert cliargs_deferred_get('BadKey', default=17)() == 17

    # This is checking that global state has been set up
    CLIARGS._set_cache({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'

# Generated at 2022-06-12 21:17:34.054134
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get
    """
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    # initialize global context
    _init_global_context({})

    # test getting non-existing key
    getter = cliargs_deferred_get('non-existing')
    value = getter()
    assert value is None

    # test getting existing key
    getter = cliargs_deferred_get('existing')
    value = getter()
    assert value is None

    # initialize global context again with a key
    _init_global_context({'existing': 'value'})

    # test getting existing key with default

# Generated at 2022-06-12 21:17:43.649761
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

# Generated at 2022-06-12 21:17:47.389833
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({"tags": 'tag'})
    assert CLIARGS.tags == [u'tag']

    f = cliargs_deferred_get('tags')
    assert f() == [u'tag']

    f = cliargs_deferred_get('vault_password_file')
    assert f() is None

    f = cliargs_deferred_get('tags', shallowcopy=True)
    assert f() == [u'tag']
    assert f() is not CLIARGS.tags

    f = cliargs_deferred_get('vault_password_file', shallowcopy=True)
    assert f() is None

# Generated at 2022-06-12 21:17:57.668865
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:18:04.623149
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = GlobalCLIArgs({'foo': 'bar'})
    func = cliargs_deferred_get('foo')
    assert func() == 'bar'

    cliargs = GlobalCLIArgs({'foo': ['bar']})
    func = cliargs_deferred_get('foo')
    assert func() == ['bar']

    cliargs = GlobalCLIArgs({'foo': ['bar']})
    func = cliargs_deferred_get('foo', shallowcopy=True)
    assert func() == ['bar']
    assert func() is not ['bar']

    cliargs = GlobalCLIArgs({'foo': {'bar': 'baz'}})
    func = cliargs_deferred_get('foo')
    assert func() == {'bar': 'baz'}

    cliargs

# Generated at 2022-06-12 21:18:19.811922
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import Mapping

    assert cliargs_deferred_get('non-existent') is None

    d = {}
    CLIARGS['keys'] = []
    CLIARGS['dict'] = d
    CLIARGS['list'] = []
    CLIARGS['set'] = set([])
    CLIARGS['int'] = 1

    # check we get a non-shallowcopy value
    assert CLIARGS['keys'] is cliargs_deferred_get('keys')

    # check we get a value
    assert cliargs_deferred_get('keys') is not None
    assert cliargs_deferred_get('dict') is not None
    assert cliargs_deferred_get('list') is not None

# Generated at 2022-06-12 21:18:28.059434
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test ``ansible.utils.context_objects.cliargs_deferred_get``"""
    # Set up Mocks
    def change_cliargs():
        global CLIARGS
        CLIARGS.clear()
        CLIARGS["foo"] = "foo value"
        CLIARGS["bar"] = "bar value"
        CLIARGS["baz"] = "baz value"

    change_cliargs()
    foo_deferred = cliargs_deferred_get("foo")
    bar_deferred_default = cliargs_deferred_get("bar", default="default value")
    baz_deferred_default_shallow = cliargs_deferred_get("baz", default=["default value"], shallowcopy=True)
    assert foo_deferred() == "foo value"
    assert bar_deferred_

# Generated at 2022-06-12 21:18:38.906031
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # A singleton is created by assigning a different object.  This is ok because the
    # code is only run during unit tests
    global CLIARGS
    CLIARGS = CLIArgs({'key1': 'value1'})

    # Test getting a value
    assert cliargs_deferred_get('key1') == 'value1'

    # Test getting a value with a default
    assert cliargs_deferred_get('key2', default='value2') == 'value2'

    # Test getting a value with a default that is a list
    assert cliargs_deferred_get('key2', default=['value2']) == ['value2']

    # Test shallow copy when the default is a list
    mylist = ['value2']

# Generated at 2022-06-12 21:18:46.902202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    >>> CLIARGS.__dict__['_CLIArgs__data']['something'] = 1
    >>> default = 'some default'
    >>> func = cliargs_deferred_get('something', default)
    >>> CLIARGS.__dict__['_CLIArgs__data']
    {'something': 1}
    >>> func()
    1
    >>> func = cliargs_deferred_get('somethingelse', default)
    >>> CLIARGS.__dict__['_CLIArgs__data']
    {'something': 1}
    >>> func()
    'some default'
    """

# Generated at 2022-06-12 21:18:58.740275
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.data = {'foo': [1, 2, 3]}

    # Test default
    assert cliargs_deferred_get('nonexistent', default='default') == 'default'

    # Test  value is returned
    assert cliargs_deferred_get('foo') == [1, 2, 3]

    # Test with shallow copy
    import copy
    c = cliargs_deferred_get('foo', shallowcopy=True)
    assert c == [1, 2, 3]
    assert copy.copy(c) == [1, 2, 3]
    assert copy.deepcopy(c) == [1, 2, 3]

    # Test that value is a copy
    c[-1] = 4
    assert cliargs_deferred_get('foo') == [1, 2, 3]
    assert c

# Generated at 2022-06-12 21:19:09.387638
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import types
    assert isinstance(cliargs_deferred_get('somekey'), types.FunctionType)

    class FakeArgs(dict):
        def get(self, key, default=None):
            return self[key]

    class GlobalFakeArgs(FakeArgs):
        @classmethod
        def from_options(cls, cli_args):
            return cls()

    def fake_init_global_context(cli_args):
        global CLIARGS
        CLIARGS = GlobalFakeArgs.from_options(cli_args)


# Generated at 2022-06-12 21:19:18.155389
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that the ``cliargs_deferred_get`` returns an appropriate value"""

    # Note: the Mocking context manager is not used to avoid an additional dependency
    CLIARGS = {'a': 1}
    closure = cliargs_deferred_get('a')
    assert closure() == 1

    # If a key is not found in the dict, the default is used
    closure = cliargs_deferred_get('b', default=3)
    assert closure() == 3

    # Test that if the key is not found in the dict, and there is no default, we get the default
    # for the ``get`` method which is ``None``
    closure = cliargs_deferred_get('c')
    assert closure() is None

    # Test that a shallow copy is made if requested.

# Generated at 2022-06-12 21:19:26.772214
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # No CLiArgs have been parsed yet
    assert CLIARGS.get('random') is None
    assert CLIARGS.get('random', default='random-default') == 'random-default'

    # Set up some dummy cli args
    test_args = {'list': [1, 2, 3],
                 'set': set([1, 2, 3]),
                 'dict': {'foo': 'bar'}}
    _init_global_context(test_args)

    # Test that deferred get functions return the right value
    # -- No shallow copy
    deferred_list = cliargs_deferred_get('list')
    deferred_set = cliargs_deferred_get('set')
    deferred_dict = cliargs_deferred_get('dict')

    assert deferred_list() == test_args['list']

# Generated at 2022-06-12 21:19:38.369325
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def assert_shallow_copy(value):
        '''Assert that the returned value from ``cliargs_deferred_get`` is a shallow copy'''
        pre_value = value[:]
        val = cliargs_deferred_get(key, default=value, shallowcopy=True)()
        if is_sequence(val):
            val[0] = 'not original value'
        elif isinstance(val, (Mapping, Set)):
            val['not original key'] = 'not original value'
        assert pre_value == value
        assert val != value

    def assert_default(value):
        '''Assert that the returned value from ``cliargs_deferred_get`` is the default value'''
        val = cliargs_deferred_get(key, default=value, shallowcopy=True)()

# Generated at 2022-06-12 21:19:49.243089
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test some of the simple cases where we just return the value
    CLIARGS['a'] = 'b'
    assert cliargs_deferred_get('a')() == 'b'
    assert cliargs_deferred_get('a', default='c')() == 'b'
    assert cliargs_deferred_get('b', default='c')() == 'c'

    # Test some of the complex cases where we make copies of the contents
    CLIARGS['c'] = {'d': 'e'}
    assert cliargs_deferred_get('c')() == {'d': 'e'}
    assert cliargs_deferred_get('c', shallowcopy=True)() == {'d': 'e'}


# Generated at 2022-06-12 21:20:08.404112
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.common.collections import Mapping, Set
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.six import string_types, integer_types
    import sys

    _v = {}

# Generated at 2022-06-12 21:20:18.242278
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS['my_key'] = 'my_value'
    assert cliargs_deferred_get('my_key')() == 'my_value'

    cli_args = {'my_key': 'my_other_value'}
    CLIARGS = CLIArgs(cli_args)
    assert cliargs_deferred_get('my_key')() == 'my_other_value', "Should not have defaulted to global value"
    assert cliargs_deferred_get('my_missing_key')() is None, "Should have returned None"
    assert cliargs_deferred_get('my_missing_key', default='default_value')() == 'default_value', "Should have returned the default value"

    cli_args = {'mylist': [1, 2, 3]}

# Generated at 2022-06-12 21:20:28.988803
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Import here so that we don't import unittest2 on Python 2.6.9
    import unittest
    from ansible.utils.context_objects import CliArgs

    class TestCliArgsDeferredGet(unittest.TestCase):
        def setUp(self):
            self.cli_args = CliArgs({'C': 'C_value', 'D': 'D_value', 'E': 'E_value'})

        def test_simple(self):
            global CLIARGS
            old_cliargs = CLIARGS
            try:
                CLIARGS = self.cli_args

                self.assertEqual(cliargs_deferred_get('C')(), 'C_value')
            finally:
                CLIARGS = old_cliargs

        def test_default(self):
            global CLIARGS

# Generated at 2022-06-12 21:20:39.497231
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from unittest import TestCase

    class TestCliArgsGet(TestCase):
        def test_no_default(self):
            getter = cliargs_deferred_get('foo')
            self.assertRaises(KeyError, getter)

        def test_with_default(self):
            getter = cliargs_deferred_get('foo', default=None)
            self.assertEqual(getter(), None)

        def test_shallowcopy(self):
            getter = cliargs_deferred_get('foo', default=[1, 2, 3], shallowcopy=True)
            self.assertEqual(getter(), [1, 2, 3])

            getter = cliargs_deferred_get('foo', default={'a': 1, 'b': 2}, shallowcopy=True)
            self

# Generated at 2022-06-12 21:20:44.682738
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for ``CLIARGS`` wrapper function ``cliargs_deferred_get``

    This function is not exposed outside of the context module
    """
    # pylint: disable = protected-access
    from ansible.utils.context_objects import _CLIArgs
    from ansible.compat.tests.mock import patch
    from ansible.module_utils.common.collections import is_sequence

    # Test wrapped value
    cli_args = {'foo': 'bar'}
    cli_args_obj = _CLIArgs(cli_args)
    with patch('ansible.utils.context.CLIARGS', cli_args_obj):
        key = 'foo'
        default = None
        shallowcopy = False

        func = cliargs_deferred_get(key, default, shallowcopy)

# Generated at 2022-06-12 21:20:55.075340
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCLIArgs(CLIArgs):
        def __init__(self, vars, **kwargs):
            super(TestCLIArgs, self).__init__(vars, **kwargs)

    cli_args = TestCLIArgs({'verbosity': [1]})

    # Test case 1
    assert cli_args_deferred_get('verbosity')() == 1
    cli_args['verbosity'] = 0
    assert cli_args_deferred_get('verbosity')() == 0

    # Test case 2
    cli_args['verbosity'] = ['1']
    assert cli_args_deferred_get('verbosity')() == ['1']
    cli_args['verbosity'] = ['0']

# Generated at 2022-06-12 21:21:05.260309
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping, AnsibleSet
    import copy

    test_dict = {'foo': 'bar', 'baz': 'qux'}
    test_list = ['foo', 'bar', 'baz', 'qux', 6, 7, 8]
    test_set = {'foo', 'bar', 'baz', 'qux'}

    def test_unicode():
        # Test handling of str types (not including subclassed types)
        cliargs_deferred_get('foo', default=None)()
        cliargs_deferred_get('foo', default='bar')()
        cliargs_deferred_get('foo', default='qux')()

# Generated at 2022-06-12 21:21:12.547966
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'a':'b', 'c':[1, 2]}
    _init_global_context(cli_args)
    assert CLIARGS is CLIARGS
    assert cliargs_deferred_get('a')() == 'b'
    assert cliargs_deferred_get('c')() == [1, 2]
    assert cliargs_deferred_get('c', shallowcopy=True)() == [1, 2]
    assert cliargs_deferred_get('b')() is None
    assert cliargs_deferred_get('b', 'd')() == 'd'
    assert cliargs_deferred_get('b', ['d'])() == ['d']

# Generated at 2022-06-12 21:21:21.258151
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for ``CLIARGS``.get_closure

    Use this as an example of how to use deferred access to CLIARGS from code that
    can be parsed/executed at import time.
    """
    global CLIARGS

    assert cliargs_deferred_get('foo') == None
    assert cliargs_deferred_get('foo', default=1) == 1
    assert cliargs_deferred_get('foo', default=1)() == 1

    CLIARGS = CLIArgs({'foo': 2})
    assert cliargs_deferred_get('foo') == 2
    assert cliargs_deferred_get('foo', default=1) == 2
    # note that this is not a singleton, so cliargs_deferred_get() is not the same
    # as cliargs_deferred

# Generated at 2022-06-12 21:21:32.363673
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    a = {}
    b = [1]
    c = (1,)
    d = [2, 3, 4]
    e = {'a': 1}
    f = {1, 2, 3, 5}

    global CLIARGS
    CLIARGS = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}

    assert cliargs_deferred_get('a')() is a
    assert cliargs_deferred_get('a', shallowcopy=True)() is a
    assert cliargs_deferred_get('b')() is b
    b_copy = cliargs_deferred_get('b', shallowcopy=True)()
    assert b_copy is not b
    assert b_copy == b
    assert cliargs_def

# Generated at 2022-06-12 21:21:59.128111
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # noqa
    from ansible.module_utils.common import remove_values


# Generated at 2022-06-12 21:22:06.379337
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # Test with a key that is not present in the dict
    assert cliargs_deferred_get('key that is not present')().get('key that is not present') is None
    # Test with a key that is present in the dict with that value
    CLIARGS = CLIArgs({'key that is present': 'value that is present'})
    assert cliargs_deferred_get('key that is present')().get('key that is present') == 'value that is present'

# Generated at 2022-06-12 21:22:16.962890
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    # given
    args = {'key': 'val'}
    _init_global_context(args)

    # when
    _get = cliargs_deferred_get('key')
    value = _get()

    # then
    assert value == 'val'
    assert value is not args['key']

    # given
    args = {'key': ['val_list']}
    _init_global_context(args)

    # when
    _get = cliargs_deferred_get('key', shallowcopy=True)
    value = _get()

    # then
    assert value == ['val_list']
    assert value is not args['key']

    # given
    args = {'key': set(['val_set'])}
    _init_global_context(args)

    #

# Generated at 2022-06-12 21:22:25.678139
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the internal function to make sure it does shallow copies and
    # None's properly.
    assert [] == _test_cliargs_deferred_get([], shallowcopy=True)
    assert [1, 2, 3] == _test_cliargs_deferred_get([1, 2, 3], shallowcopy=True)
    assert ['foo', 'bar'] == _test_cliargs_deferred_get(['foo', 'bar'], shallowcopy=True)
    assert (1, 2, 3) == _test_cliargs_deferred_get((1, 2, 3), shallowcopy=True)
    assert {'a': 'b', 'c': None} == _test_cliargs_deferred_get({'a': 'b', 'c': None}, shallowcopy=True)
    assert set('foo') == _test_cliargs_

# Generated at 2022-06-12 21:22:37.499257
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from copy import copy

    # default value with no key
    _init_global_context({})
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'

    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo', 'default')() == 'bar'

    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'

    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

    _init_global_context({'foo': ['bar']})
    assert cliargs_deferred_get('foo')() == ['bar']
    assert cliargs

# Generated at 2022-06-12 21:22:46.435471
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert cliargs_deferred_get("foo")() == None
    CLIARGS = CLIArgs({"foo": "bar"})
    assert cliargs_deferred_get("foo")() == "bar"
    CLIARGS = CLIArgs({"foo": [5, 10]})
    assert cliargs_deferred_get("foo")() == [5, 10]
    assert cliargs_deferred_get("foo", shallowcopy=True)() == [5, 10]
    assert cliargs_deferred_get("foo", shallowcopy=False)() == [5, 10]
    CLIARGS = CLIArgs({"foo": {"bar": 15, "baz": 20}})
    assert cliargs_deferred_get("foo")() == {"bar": 15, "baz": 20}

# Generated at 2022-06-12 21:22:57.726996
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Similar tests to ``test/test_collection_loader.test_cliargs_deferred_get`` but with a different
    # call site and therefore a slightly different code path

    # Test that we actually copy Mapping, Sequence, and Set types
    import copy
    import types

    class Test(Mapping):
        def __getitem__(self, key):
            return None

        def __iter__(self):
            return iter(())
    test_map = Test()
    assert test_map is not cliargs_deferred_get('key', default=test_map)()
    assert test_map.copy() == cliargs_deferred_get('key', default=test_map, shallowcopy=True)()

    test_set = set()

# Generated at 2022-06-12 21:23:06.900817
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get"""
    global CLIARGS

# Generated at 2022-06-12 21:23:16.272130
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'a': 1, 'b': [2, 3], 'c': {'d': 4}, 'e': 'abc', 'f': {'g': 5}}

    _init_global_context(cli_args)
    original_CLIARGS = CLIARGS

    assert cliargs_deferred_get('a')() == 1
    assert cliargs_deferred_get('b')() == [2, 3]
    assert cliargs_deferred_get('c')() == {'d': 4}
    assert cliargs_deferred_get('e')() == 'abc'
    assert cliargs_deferred_get('f')() == {'g': 5}

    assert cliargs_deferred_get('b', default=[])() == [2, 3]
    assert cli

# Generated at 2022-06-12 21:23:25.770871
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get() works as expected

    We are testing an internal function so we won't throw the "method is private" warning
    """
    # pylint: disable=W0212
    orig_cliargs = CLIARGS
    cliargs = CLIArgs({'foo': 'bar'})
    CLIARGS = cliargs

    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() == None
    assert cliargs_deferred_get('bar', 'baz')() == 'baz'

    cliargs['bar'] = 'baz'
    assert cliargs_deferred_get('bar')() == 'baz'

    # test shallow copy

# Generated at 2022-06-12 21:24:13.264426
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'one': [1, 2]})
    assert cliargs_deferred_get('one')() == [1, 2]
    assert cliargs_deferred_get('two')() is None
    assert cliargs_deferred_get('two', [])() == []
    assert cliargs_deferred_get('one', shallowcopy=True)() == [1, 2]
    assert cliargs_deferred_get('one', shallowcopy=True)() is not CLIARGS['one']
    CLIARGS = CLIArgs({'one': {'two': 2}})
    assert cliargs_deferred_get('one')() == {'two': 2}

# Generated at 2022-06-12 21:24:24.961929
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set, Sequence

    # Import this here so we can get the expected exception
    from ansible.errors import AnsibleAssertionError

    # Test for non-copy behavior
    CLIARGS.data = {'key1': [1, 2], 'key2': {'a': 'b'}, 'key3': 'somestring', 'key4': None}
    assert cliargs_deferred_get('key1')() == [1, 2]
    assert cliargs_deferred_get('key1', shallowcopy=True)() == [1, 2]
    assert cliargs_deferred_get('key2')() == {'a': 'b'}
    assert cliargs_deferred_get('key2', shallowcopy=True)

# Generated at 2022-06-12 21:24:35.246595
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    options = {'a': 1, 'b': 2, 'c': [3, 4], 'd': {'foo': 'bar'}}
    global CLIARGS
    CLIARGS = CLIArgs(options)
    assert cliargs_deferred_get('a')() == options['a']
    assert cliargs_deferred_get('c') is not options['c']
    assert cliargs_deferred_get('c', shallowcopy=True) is not options['c']
    assert cliargs_deferred_get('c', shallowcopy=True)() == options['c']
    assert cliargs_deferred_get('d', shallowcopy=True) is not options['d']
    assert cliargs_deferred_get('d', shallowcopy=True)() == options['d']

# Generated at 2022-06-12 21:24:44.863207
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    The function needs to be rewritten in pytest-3.3 in order to cover use of closure
    """
    global CLIARGS
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('unknownkey')() == None
    CLIARGS = CLIArgs({'knownkey': 'val'})
    assert cliargs_deferred_get('knownkey')() == 'val'
    assert cliargs_deferred_get('unknownkey')() == None
    assert cliargs_deferred_get('unknownkey', default='default')() == 'default'

# Generated at 2022-06-12 21:24:50.959993
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    testargs = {'cliargs_deferred_get_test': 'success'}
    CLIARGS = CLIArgs(testargs)
    assert cliargs_deferred_get('cliargs_deferred_get_test')() == 'success'
    assert cliargs_deferred_get('fakekey')('default') == 'default'

# Generated at 2022-06-12 21:24:59.586491
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class Test1():
        test_member = cliargs_deferred_get('test_key')

    class Test2():
        test_member = cliargs_deferred_get('test_key', [])

    class Test3():
        test_member = cliargs_deferred_get('test_key', shallowcopy=True)

    class Test4():
        test_member = cliargs_deferred_get('test_key', {}, shallowcopy=True)

    test1 = Test1()
    assert test1.test_member() is None
    test1.test_member = 1
    assert test1.test_member == 1

    CLIARGS.setdefault('test_key', 1)

    test1 = Test1()
    assert test1.test_member() == 1
    test1.test_member = 2