

# Generated at 2022-06-12 21:15:07.340664
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from unittest import TestCase

    class TestDeferred(TestCase):
        def setUp(self):
            self.cliargs = ImmutableDict({'foo': 'bar', 'baz': ['qux', 'quux'], 'quuz': {'corge': 'grault'}})

        def check_dict(self, getter, value):
            # Check to make sure the value is correct
            self.assertEqual(getter(), value)
            # Check to make sure it makes a copy
            self.assertNotEqual(getter(), value)
            # Check to make sure it makes a copy of the dict
            value_copy = getter()
            value_copy['corge'] = 'garply'
            self.assertNotEqual

# Generated at 2022-06-12 21:15:16.136734
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['t'] = 't'
    assert cliargs_deferred_get('t')() == 't'
    assert cliargs_deferred_get('t', default=dict())() is not CLIARGS['t']

    CLIARGS['t'] = 't'
    assert cliargs_deferred_get('t', shallowcopy=True)() == 't'
    assert cliargs_deferred_get('t', default=dict(), shallowcopy=True)() is not CLIARGS['t']

    l = list(range(10))
    CLIARGS['t'] = l
    assert cliargs_deferred_get('t', shallowcopy=True)() == l
    assert cliargs_deferred_get('t', shallowcopy=True)() is not l


# Generated at 2022-06-12 21:15:26.516752
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('test_key')() is None
    CLIARGS['test_key'] = 'test_val'
    assert cliargs_deferred_get('test_key')() == 'test_val'
    assert cliargs_deferred_get('test_key', default='default')() == 'test_val'
    assert cliargs_deferred_get('test_key', default='default', shallowcopy=True)() == 'test_val'
    test_list = [1, 2, 3]
    CLIARGS['test_key'] = test_list
    assert cliargs_deferred_get('test_key')() == test_list
    assert cliargs_deferred_get('test_key', default='default')() == test_list
    assert cliargs_deferred_

# Generated at 2022-06-12 21:15:32.252454
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for a function that calls cliargs_deferred_get"""
    def my_test_function():
        return cliargs_deferred_get('test_param')()

    c = CLIArgs({'test_param': 'test_value'})
    global CLIARGS
    CLIARGS = c
    assert my_test_function() == 'test_value'

# Generated at 2022-06-12 21:15:36.124495
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    value = {'a': 1}
    _init_global_context({'foo': value})
    assert value is CLIARGS['foo']
    assert value is cliargs_deferred_get('foo')()
    assert value is not cliargs_deferred_get('foo', shallowcopy=True)()

# Generated at 2022-06-12 21:15:41.636718
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils import context_objects
    from ansible.module_utils.common._collections_compat import Mapping
    assert isinstance(cliargs_deferred_get, context_objects.CLIArgsWrapper)

    class DummyCLIArgs(Mapping):

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def __getitem__(self, key):
            return self.kwargs[key]

        def get(self, key, default):
            return self.kwargs.get(key, default)

        def __iter__(self):
            return iter(self.kwargs)

        def __len__(self):
            return len(self.kwargs)


# Generated at 2022-06-12 21:15:52.439716
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    key = 'my_key'
    default = 'my_default'
    other_default = 'another_default'

    from ansible.utils.context_objects import CLIArgs, GlobalCLIArgs

    # CLIARGS defaults to CLIArgs() which returns None for missing keys
    assert cliargs_deferred_get(key)() is None

    cli_arg = {'my_key': None, 'my_other_key': True}

    # CLIArgs returns None
    CLIARGS.update(cli_arg)
    assert cliargs_deferred_get(key)() is None

    # CLIArgs returns key
    CLIARGS.update({'connected': False})
    assert cliargs_deferred_get(key)() is None

    # CLIArgs returns default

# Generated at 2022-06-12 21:16:02.177081
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('baz', default='baz')() == 'baz'
    assert cliargs_deferred_get('baz', default='baz', shallowcopy=True)() == 'baz'
    CLIARGS['deeper'] = {'foo': 'bar'}
    assert cliargs_deferred_get('deeper')() == {'foo': 'bar'}

# Generated at 2022-06-12 21:16:14.297703
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=unused-variable
    def _deferred_get_closure():
        return cliargs_deferred_get('subset', default='all')
    global CLIARGS
    CLIARGS = CLIArgs({'subset': 'a'})
    assert _deferred_get_closure()() == 'a'
    CLIARGS = CLIArgs({})
    assert _deferred_get_closure()() == 'all'

    def _deferred_get_closure_shallowcopy():
        return cliargs_deferred_get('subset_copy', default=[], shallowcopy=True)
    global CLIARGS
    CLIARGS = CLIArgs({'subset_copy': ['a', 'b']})
    subset_copy = _deferred_get_closure_shallowcopy()()
    assert subset_

# Generated at 2022-06-12 21:16:24.268427
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeCliArgs(object):
        def __init__(self, data):
            self._data = data

        def get(self, key, default=None):
            return self._data.get(key, default)

        def __getitem__(self, key):
            return self._data[key]

    # Test basic usage
    global CLIARGS
    data = {'foo': 'bar'}
    CLIARGS = FakeCliArgs(data)
    assert 'bar' == cliargs_deferred_get('foo')()
    assert 'baz' == cliargs_deferred_get('nothere', 'baz')()

    # Test sequences
    CLIARGS = FakeCliArgs(data)

# Generated at 2022-06-12 21:16:34.616464
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs({'foo': 42})
    assert cliargs_deferred_get('foo')() == 42
    assert cliargs_deferred_get('bar')(None) is None
    CLIARGS = CLIArgs({'foo': [1, 2, 3]})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == [1, 2, 3]
    CLIARGS = old_cliargs

# Generated at 2022-06-12 21:16:44.587525
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get returns a callable that gets a key from CLIARGS"""

    # Setup
    test_args = {'a': 'valuea'}
    _init_global_context(test_args)

    # Test that value is returned
    assert cliargs_deferred_get('a')() == 'valuea'

    # Test that default is returned if key is missing
    assert cliargs_deferred_get('b')(default='valueb') == 'valueb'

    # Test that value is returned by default
    assert cliargs_deferred_get('b')(default='valueb', shallowcopy=False) == 'valueb'

    # Test that shallowcopy works

# Generated at 2022-06-12 21:16:54.279494
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    value = 'test'
    test_cli_args = {'test1': 'test1', 'test2': value, 'test3': ['test3']}
    _init_global_context(test_cli_args)

    result = cliargs_deferred_get('test1')
    assert result == test_cli_args['test1']
    result = cliargs_deferred_get('test2')
    assert result == value
    result = cliargs_deferred_get('test3', shallowcopy=True)
    assert result == test_cli_args['test3']
    result[0] = 'test4'
    assert result == ['test4']
    assert CLIARGS['test3'] == ['test3']



# Generated at 2022-06-12 21:17:05.878504
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert callable(cliargs_deferred_get)

    original_args = {'x':'y'}
    CLIARGS = CLIArgs(original_args)
    assert cliargs_deferred_get('x')() == 'y'
    assert cliargs_deferred_get('x', default='z')() == 'y'
    assert cliargs_deferred_get('z')() is None
    assert cliargs_deferred_get('z', default='a')() == 'a'

    CLIARGS = CLIArgs({'x': []})
    assert cliargs_deferred_get('x', shallowcopy=True)() == []
    CLIARGS = CLIArgs({'x': set()})
    assert cliargs_deferred_get('x', shallowcopy=True)()

# Generated at 2022-06-12 21:17:16.293577
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the deferred cliargs getter"""

    # Test the default case
    assert cliargs_deferred_get('foo') == None

    # Test the regular get case
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo') == 'bar'

    # Test the default case with a default
    assert cliargs_deferred_get('baz', 'baz') == 'baz'

    # Test the regular get case with a default
    CLIARGS['baz'] = 'baz'
    assert cliargs_deferred_get('baz', default='default_baz') == 'baz'

    # Test the regular get case with a default is set and we ask for a shallow copy
    CLIARGS['baz'] = 'baz'
    value = cliargs

# Generated at 2022-06-12 21:17:27.285202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get
    """
    from ansible.module_utils.common.validation import check_type_list
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.formatters import yaml_quote
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    old_cliargs = CLIARGS
    #  Replace globally available CLIARGS with our own test data

# Generated at 2022-06-12 21:17:38.844446
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cli_args = {'foo': 'bar'}
    _init_global_context(cli_args)
    assert 'foo' in vars(CLIARGS)
    assert cliargs_deferred_get('foo') == 'bar'
    # the bound function should be the same as calling directly
    assert cliargs_deferred_get('foo') == CLIARGS.get('foo')
    # foo2 isn't in the args object so should default to None
    assert cliargs_deferred_get('foo2') is None
    # and we should be able to set a different default
    assert cliargs_deferred_get('foo2', default='bar') == 'bar'
    # and the bound function should be the same

# Generated at 2022-06-12 21:17:45.659233
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    # Set up with the key and value
    key = 'k'
    value = object()

    # Make sure the inner function returns the value if key is in CLIARGS
    CLIARGS.update({key: value})
    assert cliargs_deferred_get(key)() == value
    # And that the default gets returned if key is not in CLIARGS
    default = object()
    assert cliargs_deferred_get(object(), default=default)() == default

    # Test that a shallow copy is returned if asked for
    assert cliargs_deferred_get(key, shallowcopy=True)() == value
    CLIARGS[key] = [1, 2, 3]
    assert cliargs_deferred_get(key, shallowcopy=True)() == [1, 2, 3]
    CLI

# Generated at 2022-06-12 21:17:56.680801
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get function"""

    global CLIARGS

    CLIARGS = CLIArgs(dict(foo='bar', baz=dict(bob='jim')))

    assert 'bar' == cliargs_deferred_get('foo')()
    assert dict(bob='jim') == cliargs_deferred_get('baz')()

    CLIARGS = CLIArgs(dict(foo='bob', baz=dict(bob='jim')))

    assert 'bob' == cliargs_deferred_get('foo')()
    assert dict(bob='jim') == cliargs_deferred_get('baz')()

    CLIARGS = CLIArgs(dict(foo='bob', baz=dict(bob='jim')))


# Generated at 2022-06-12 21:18:02.106465
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _set_cliargs_then_get(key, default=None, shallowcopy=False):
        cliargs = {'foo': 'bar'}
        _init_global_context(cliargs)
        return cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)()

    value = 'bar'
    assert _set_cliargs_then_get('foo') == value
    assert _set_cliargs_then_get('foo', shallowcopy=True) != value

# Generated at 2022-06-12 21:18:14.948744
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'foo': [1,2], 'bar': {'baz': 3}})
    assert cliargs_deferred_get('foo')().pop() == 2
    assert cliargs_deferred_get('bar')().popitem() == ('baz', 3)
    CLIARGS['foo'].append(3)
    assert cliargs_deferred_get('foo')() == [1,2,3]
    assert cliargs_deferred_get('foo', shallowcopy=True)() == [1,2]



# Generated at 2022-06-12 21:18:20.962616
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['default_value'] = 'DEFAULT'
    assert cliargs_deferred_get('default_value')() == 'DEFAULT'
    assert cliargs_deferred_get('default_value', default='override_default')() == 'DEFAULT'
    CLIARGS['default_value'] = []
    assert cliargs_deferred_get('default_value')() == []
    assert cliargs_deferred_get('default_value', shallowcopy=True)() == []
    CLIARGS['default_value'] = set()
    assert cliargs_deferred_get('default_value')() == set()
    assert cliargs_deferred_get('default_value', shallowcopy=True)() == set()
    CLIARGS['default_value'] = {}
    assert cliargs_deferred

# Generated at 2022-06-12 21:18:30.758709
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(one=1, two=2, three=3, a_list=[1, 2, 3], a_set={1, 2, 3}, a_dict={'a': 1, 'b': 2}))
    get_one = cliargs_deferred_get('one')
    get_two = cliargs_deferred_get('two')
    list_a_list = cliargs_deferred_get('a_list', shallowcopy=True)
    copy_a_set = cliargs_deferred_get('a_set', shallowcopy=True)
    get_a_dict = cliargs_deferred_get('a_dict', shallowcopy=True)
    assert get_one() == 1
    assert get_two() == 2

# Generated at 2022-06-12 21:18:41.137288
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs(dict(testkey=2, testkey2=[1, 2, 3]))

    # Test shallow copy of value
    inner_value_copy = cliargs_deferred_get('testkey', default=5, shallowcopy=True)()
    assert inner_value_copy == 2
    # Modify value
    inner_value_copy += 1
    # Ensure value was modified
    assert inner_value_copy == 3
    # Ensure original was not modified
    assert CLIARGS['testkey'] == 2

    # Test deep copy of value
    inner_value_copy = cliargs_deferred_get('testkey2', default=[4, 5, 6], shallowcopy=True)()
    assert inner_value_copy == [1, 2, 3]
    # Modify value
   

# Generated at 2022-06-12 21:18:49.633550
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # Test setting the default
    CLIARGS = CLIArgs(dict(option1=dict(value=1)))
    cli_arg_value = cliargs_deferred_get('option1.value')
    assert cli_arg_value() == 1

    # Test getting the default when unavailable
    assert cliargs_deferred_get('option2.value', default=2)() == 2

    # Test getting the actual value
    CLIARGS = CLIArgs(dict(option1=dict(value=3)))
    cli_arg_value = cliargs_deferred_get('option1.value', default=2)
    assert cli_arg_value() == 3

    # Test with a list
    CLIARGS = CLIArgs(dict(option1=dict(value=[1, 2, 3])))

# Generated at 2022-06-12 21:19:00.539686
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class ClassWithFields:
        test_field = FieldAttribute(default=cliargs_deferred_get('test_default'),
                                    choices=cliargs_deferred_get('test_choices'))

        def __init__(self, **kwargs):
            self.test_field = kwargs.pop('test_field', self.test_field)

    global CLIARGS
    CLIARGS = CLIArgs({'test_default': 1, 'test_choices': [1, 2, 3]})
    instance = ClassWithFields()
    assert instance.test_field == 1
    assert instance.test_field.choices == [1, 2, 3]
    CLIARGS = CLIArgs({'test_default': 2, 'test_choices': [2, 3, 4]})
    instance = ClassWithFields()

# Generated at 2022-06-12 21:19:12.296186
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'list': ['foo', 'bar', 'baz'], 'dict': {'key': 'value'}, 'set': {'value'}})
    assert cliargs_deferred_get('missing')() is None
    assert cliargs_deferred_get('list')() == ['foo', 'bar', 'baz']
    assert cliargs_deferred_get('dict')() == {'key': 'value'}
    assert cliargs_deferred_get('set')() == {'value'}

    assert cliargs_deferred_get('list', shallowcopy=True)() == ['foo', 'bar', 'baz']
    assert cliargs_deferred_get('dict', shallowcopy=True)() == {'key': 'value'}
    assert cliargs_deferred_

# Generated at 2022-06-12 21:19:24.268494
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test with CLIArgs that has no default value
    class NoDefaultCLIArgs(CLIArgs):
        def _default_values(self):
            return None

    # Test with missing default value
    try:
        CLIARGS = NoDefaultCLIArgs({})
        assert cliargs_deferred_get('foo')() is None
        CLIARGS = NoDefaultCLIArgs({'foo': 'tuna'})
        assert cliargs_deferred_get('foo')() == 'tuna'
    except KeyError:
        pytest.fail("KeyError raised when it should not have been raised")

    # Test with value present
    assert cliargs_deferred_get('foo', default='chicken')('foo') == 'tuna'
    assert cliargs_deferred_get('foo', default='chicken')()

# Generated at 2022-06-12 21:19:29.210233
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    # pylint: disable=missing-kwoa
    bar = cliargs_deferred_get('foo')
    assert bar() == 'bar'
    CLIARGS = CLIArgs({'foo': ['bar', 'baz']})
    bar = cliargs_deferred_get('foo', shallowcopy=True)
    assert bar() == ['bar', 'baz']
    # pylint: enable=missing-kwoa

# Generated at 2022-06-12 21:19:40.503985
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set

    init_dict = {'a': 1, 'b': [1, 2, 3], 'c': {'A': 1}, 'd': {1, 2, 3}}
    global CLIARGS
    CLIARGS = CLIArgs(init_dict)

    # When we defer the get, we should get back the value
    wrapped = cliargs_deferred_get('a')
    assert wrapped == init_dict['a']

    # Now we should get the default (and not an error)
    wrapped = cliargs_deferred_get('e', default='error')
    assert wrapped == 'error'

    # Now we should get the default (and not an error) even if the value is a reference

# Generated at 2022-06-12 21:19:56.991379
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    class FakeCliArgs(dict):
        def __init__(self, *args, **kwargs):
            self.updated = False
            super(FakeCliArgs, self).__init__(*args, **kwargs)
        def __setitem__(self, *args, **kwargs):
            self.updated = True
            super(FakeCliArgs, self).__setitem__(*args, **kwargs)

    # check default
    fca = FakeCliArgs({"key": "value"})
    _init_global_context(fca)
    assert cliargs_deferred_get("key", default="new_value")("key") == "value"
    assert cliargs_deferred_get("new_key", default="new_value")("new_key") == "new_value"

# Generated at 2022-06-12 21:20:03.298405
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_inner():
        ret = cliargs_deferred_get('not-there')
        assert ret is None
        ret = cliargs_deferred_get('not-there', default='A')
        assert ret == 'A'
        ret = cliargs_deferred_get('not-there', default='A', shallowcopy=True)
        assert ret == 'A'

        ret = cliargs_deferred_get('dict', default={'a': 1})
        assert ret == {'a': 1}
        ret = cliargs_deferred_get('dict', shallowcopy=True)
        assert ret == {'a': 1}

        ret = cliargs_deferred_get('list', default=[1, 2])
        assert ret == [1, 2]
        ret = cliargs_deferred_get

# Generated at 2022-06-12 21:20:07.743053
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'parameter': 'value'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('parameter') == 'value'


# These are private helpers, they should not be called by other code.  They are meant only to
# be used by the global attributes bindings

# Generated at 2022-06-12 21:20:17.589611
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    Unit test for function :func:`ansible.context.cliargs_deferred_get`

    :returns: ``True`` if the test succeeded. ``False`` otherwise.
    :rtype: bool

    """
    import mock

    cliargs_value_to_return = {'i': 'like', 'spam': ['one', 'two', 'three']}
    cliargs_default = 'spam'
    mock_cliargs = mock.MagicMock(spec=dict)
    mock_cliargs.get.return_value = cliargs_value_to_return
    test_get_fn = cliargs_deferred_get('spam', cliargs_default)
    # Initial code path

# Generated at 2022-06-12 21:20:28.920687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    global CLIARGS
    CLIARGS = CLIArgs({'a': 1, 'b': {'c': 2}, 'd': [3], 'e': '4', 'f': set([5])})
    assert 1 == cliargs_deferred_get('a')()
    assert cliargs_deferred_get('a')(default=2) == 1
    assert cliargs_deferred_get('z')(default=2) == 2
    assert cliargs_deferred_get('b')(default=2) == {'c': 2}
    assert cliargs_deferred_get('d')(default=2) == [3]

# Generated at 2022-06-12 21:20:36.907608
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""

    def tfunc(x):
        """Test function for cliargs_deferred_get()"""
        # pylint: disable=unused-argument
        return x * 2
    _init_global_context({'foo': 10})

    assert cliargs_deferred_get('foo', default=1)() == 10
    assert cliargs_deferred_get('does-not-exist', default=1)() == 1
    assert cliargs_deferred_get('foo', default=tfunc)(2) == 20

# Generated at 2022-06-12 21:20:47.447302
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common.text.converters import to_text

    # Return default value
    assert CLIARGS is CLIARGS
    getter = cliargs_deferred_get('non_existent_value', shallowcopy=False, default='default_value')
    assert getter() == 'default_value'

    # Return the value but don't copy it
    CLIARGS._opts['some_mapping'] = {'a': 1}
    getter = cliargs_deferred_get('some_mapping', shallowcopy=False)
    value = getter()
    assert value == {'a': 1}
    CLIAR

# Generated at 2022-06-12 21:20:57.736458
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSet

# Generated at 2022-06-12 21:21:01.433576
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function 'cliargs_deferred_get'"""
    pass

# Generated at 2022-06-12 21:21:10.033400
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test ``cliargs_deferred_get`` with different types of values"""
    CLIARGS.set_options({'abc': [1, 2, 3]})

    # list
    orig_value = cliargs_deferred_get('abc')()
    assert isinstance(orig_value, list)
    copied_value = cliargs_deferred_get('abc', shallowcopy=True)()
    assert isinstance(copied_value, list)
    assert orig_value == copied_value
    assert orig_value is not copied_value
    # copy is shallow
    orig_value[0] = 42
    assert orig_value == copied_value
    orig_value.append(43)
    assert orig_value != copied_value

    # dict

# Generated at 2022-06-12 21:21:31.234785
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Add a fake cli arg for the purpose of unit testing
    _init_global_context({'MINIMUM_PROTOCOL_VERSION': '2.0'})

    # Verify it works without shallowcopy
    v = cliargs_deferred_get('MINIMUM_PROTOCOL_VERSION')
    assert v == '2.0'

    # Verify it works with shallowcopy
    v = cliargs_deferred_get('MINIMUM_PROTOCOL_VERSION', shallowcopy=True)
    assert v == '2.0'
    assert type(v) == str

    # Verify it works with shallowcopy and default
    v = cliargs_deferred_get('MINIMUM_PROTOCOL_VERSION_MISSING', '1.1', shallowcopy=True)

# Generated at 2022-06-12 21:21:38.782056
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the closure over CLIARGS
    CLIARGS['foo'] = 'bar'
    get_foo = cliargs_deferred_get('foo')
    assert get_foo() == 'bar'
    del CLIARGS['foo']
    assert get_foo() == None

    # Test shallow copy
    CLIARGS['foo'] = [1, 2, 3]
    get_foo = cliargs_deferred_get('foo', shallowcopy=True)
    assert get_foo() == [1, 2, 3]
    assert id(get_foo()) != id(CLIARGS['foo'])

    CLIARGS['foo'] = {'bar': 'baz'}
    get_foo = cliargs_deferred_get('foo', shallowcopy=True)

# Generated at 2022-06-12 21:21:46.463476
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence, MutableSet
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common.text.utils import is_text

    class MyMutableMapping(dict, MutableMapping):
        pass
    class MyMutableSequence(list, MutableSequence):
        pass
    class MyMutableSet(set, MutableSet):
        pass

    def get_key(value):
        k = value.__class__.__name__.lower()
        if is_text(value):
            k += '_str'
        elif isinstance(value, bytes):
            k += '_bytes'

# Generated at 2022-06-12 21:21:57.571673
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get"""
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.collections import is_sequence
    ctx = CLIArgs({'a': ['b', 'c'], 'b': 123, 'c': {1: 2}, 'd': set([1, 2, 3])})
    assert ctx.a == cliargs_deferred_get('a')()
    assert ctx.b == cliargs_deferred_get('b')()
    assert ctx.c == cliargs_deferred_get('c')()
    assert ctx.d == cliargs_deferred_get('d')()
    assert '@test-test' == cliargs_deferred_get('test')()

# Generated at 2022-06-12 21:22:06.325432
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # set CLIARGS global
    global CLIARGS
    CLIARGS = CLIArgs({})
    # test default behavior
    get_cliargs_key = cliargs_deferred_get("key", "default")
    assert get_cliargs_key() == "default"
    CLIARGS[("key")] = "new"
    assert get_cliargs_key() == "new"
    # test shallow copy
    CLIARGS[("key")] = [{"a": 1}]
    assert get_cliargs_key(shallowcopy=True)[0] == {"a": 1}
    # clean up CLIARGS global
    del CLIARGS

# Generated at 2022-06-12 21:22:16.916238
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    global CLIARGS
    cli_args = {'foo': 'bar', 'baz': [1, 2, 3], 'qux': {'a': 1, 'b': 2}}
    CLIARGS = CLIArgs(cli_args)
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('qux', shallowcopy=True)() == {'a': 1, 'b': 2}

    # Change the contents of the dictionary
    cli_args['foo'] = 'baz'
    cli_args['baz'].append(4)

# Generated at 2022-06-12 21:22:25.644599
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({})
    global CLIARGS
    assert CLIARGS == {}
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', 1)() == 1
    CLIARGS = CLIArgs({'foo':'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', 1)() == 'bar'
    CLIARGS = CLIArgs({'foo':{'bar':'baz'}})
    assert cliargs_deferred_get('foo')() == {'bar':'baz'}
    assert cliargs_deferred_get('foo', 1)() == {'bar':'baz'}
    assert cliargs_deferred_

# Generated at 2022-06-12 21:22:36.684808
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('key', default='value')() == 'value'
    assert cliargs_deferred_get('key', shallowcopy=True)() is None
    CLIARGS[1] = 'value'
    assert cliargs_deferred_get(1, shallowcopy=True)() == 'value'
    CLIARGS[1] = ['value', 'shallowcopy']
    assert cliargs_deferred_get(1, shallowcopy=True)() == ['value', 'shallowcopy']
    CLIARGS[1] = {'value': 'shallowcopy'}
    assert cliargs_deferred_get(1, shallowcopy=True)() == {'value': 'shallowcopy'}

# Generated at 2022-06-12 21:22:45.884687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test no value set
    orig_CLIARGS = CLIARGS
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('does_not_exist')() is None

    # Test explicit None
    CLIARGS = CLIArgs({'does_not_exist': None})
    assert cliargs_deferred_get('does_not_exist')() is None

    # Test other values
    CLIARGS = CLIArgs({'some_key': 'some_value'})
    assert cliargs_deferred_get('some_key')() == 'some_value'
    CLIARGS = CLIArgs({'some_key': 42})
    assert cliargs_deferred_get('some_key')() == 42

# Generated at 2022-06-12 21:22:56.627058
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    no_copy_default = CLIARGS['no_log']
    copy_default = CLIARGS['roles_path']
    no_copy_key = cliargs_deferred_get('no_log')
    copy_key = cliargs_deferred_get('roles_path', shallowcopy=True)
    try:
        CLIARGS = CLIArgs(dict(no_log=False, roles_path=['/tmp/foo', '/tmp/bar']))
        assert no_copy_key() == CLIARGS['no_log']
        assert copy_key() == CLIARGS['roles_path']
    finally:
        CLIARGS = CLIArgs(dict(no_log=no_copy_default, roles_path=copy_default))

# Generated at 2022-06-12 21:23:42.036440
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    import copy
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')(), CLIARGS['foo']
    assert cliargs_deferred_get('bar')('default'), 'default'
    assert cliargs_deferred_get('bar')(), None
    CLIARGS['baz'] = {'a': 1, 'b': 2}
    assert cliargs_deferred_get('baz')(), CLIARGS['baz']
    assert cliargs_deferred_get('baz', shallowcopy=True)() != CLIARGS['baz']
    assert cliargs_deferred_get('baz', shallowcopy=True)() == CLIARGS['baz']
    assert cliargs_deferred_get

# Generated at 2022-06-12 21:23:49.843355
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that deferred dictionary gets the value from the context"""
    from ansible.module_utils.common.text.converters import to_text
    class FakeContext:
        def __init__(self):
            self._values = {'foo': 'bar'}

        def get(self, key, default=None):
            return self._values.get(key, default)

    ctx = FakeContext()

    dget = cliargs_deferred_get('foo')
    assert dget() == 'bar'

    def update_values(new_values):
        ctx._values.update(new_values)

    update_values({'foo': 'baz'})
    assert dget() == 'baz'

    update_values({'foo': to_text('FÄÖÜ')})
    assert dget

# Generated at 2022-06-12 21:24:01.370887
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Exercise the function cliargs_deferred_get"""

    # Exercise that it returns the default correctly
    cli = CLIArgs({})
    value = cliargs_deferred_get('TEST', default='default')()
    assert value == 'default'

    # Exercise getting a key with no shallowcopy
    cli = CLIArgs({'TEST': 'value'})
    assert cli.get('TEST') == 'value'
    value = cliargs_deferred_get('TEST')(cli)
    assert value == 'value'

    # Exercise that shallow copy returns a copy of a sequence
    cli = CLIArgs({'TEST': ['a', 'b', 1, 2]})
    value = cliargs_deferred_get('TEST', shallowcopy=True)(cli)

# Generated at 2022-06-12 21:24:12.572612
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    list_default = [1, 2, 3]
    set_default = {1, 2, 3}
    dict_default = {'one': 1, 'two': 2, 'three': 3}
    int_default = 1

    list_local = [4, 5, 6]
    set_local = {4, 5, 6}
    dict_local = {'four': 4, 'five': 5, 'six': 6}
    int_local = 2

    global CLIARGS
    cli_args = {'list': list_local, 'set': set_local, 'dict': dict_local, 'int': int_local}
    CLIARGS = CLIArgs(cli_args)

    list_value = cliargs_deferred_get('list', list_default, True)()
    set_value = cliargs_def

# Generated at 2022-06-12 21:24:18.859716
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    fake_cliargs = {'a': 'b'}
    global CLIARGS
    try:
        CLIARGS = CLIArgs(fake_cliargs)
        assert cliargs_deferred_get('a') == 'b'
        assert not cliargs_deferred_get('b')
        assert cliargs_deferred_get('b', default=1) == 1
    finally:
        CLIARGS = CLIArgs({})

# Generated at 2022-06-12 21:24:30.638617
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

    CLIARGS['foo'] = ['a', 'b']
    pre_get = cliargs_deferred_get('foo')

    CLIARGS['foo'].append('c')
    pre_get_copy = cliargs_deferred_get('foo', shallowcopy=True)
    assert pre_get()[-1] == 'c'
    assert pre_get_copy

# Generated at 2022-06-12 21:24:35.164733
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    global CLIARGS
    CLIARGS = CLIArgs()
    inner = cliargs_deferred_get('foo', default='bar')
    assert inner() == 'bar'
    CLIARGS = CLIArgs(dict(foo='baz'))
    assert inner() == 'baz'

# Generated at 2022-06-12 21:24:46.136859
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Verify that it works when CLIARGS hasn't yet been bound
    import sys
    context = CLIArgs({'a': 1, 'b': 2})
    cliargs_deferred = cliargs_deferred_get('a', default=3)

    sys.modules['ansible.utils.context_objects'].CLIARGS = context

# Generated at 2022-06-12 21:24:57.573421
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    Ensure cliargs_deferred_get can be called before and after CLIARGS is initialized
    and get the same results"""

    # pylint: disable=protected-access
    _init_global_context(dict(foo=dict(bar='baz'),
                              no_shallow_copy=[0],
                              shallow_copy=['val']))
    foo_bar_baz = cliargs_deferred_get('foo')['bar']
    foo_bar_baz2 = cliargs_deferred_get('foo')['bar']

    assert foo_bar_baz == 'baz'
    assert foo_bar_baz is foo_bar_baz2
    assert cliargs_deferred_get('no_shallow_copy') is CLIARGS['no_shallow_copy']