

# Generated at 2022-06-12 21:15:07.433418
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_args = {
        'test_key1': 'test_value1',
        'test_key2': 'test_value2',
        'test_key3': ['test_value3', 'test_value4'],
        'test_key4': {'test_key5': 'test_value5'},
    }
    global CLIARGS
    CLIARGS = CLIArgs(test_args)

    assert cliargs_deferred_get('test_key1')() == 'test_value1'
    assert cliargs_deferred_get('test_key2')() == 'test_value2'
    assert cliargs_deferred_get('test_key3')() == ['test_value3', 'test_value4']
    assert cliarg

# Generated at 2022-06-12 21:15:13.120237
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert not hasattr(CLIARGS, '_mykey')
    my_value = cliargs_deferred_get('_mykey')
    assert my_value() is None
    assert not hasattr(CLIARGS, '_mykey')

    CLIARGS = GlobalCLIArgs.from_options({'_mykey': 'test'})
    assert my_value() == 'test'

    CLIARGS._mykey = 'test2'
    assert my_value() == 'test2'

    my_value_copy = cliargs_deferred_get('_mykey', shallowcopy=True)
    CLIARGS._mykey = 'test3'
    assert my_value_copy() == 'test2'
    assert my_value() == 'test3'

# Generated at 2022-06-12 21:15:20.323664
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from types import FunctionType
    from ansible.module_utils.six import string_types

    assert isinstance(cliargs_deferred_get('something'), FunctionType)
    assert cliargs_deferred_get('something')() is None
    assert cliargs_deferred_get('something', default='foo')() == 'foo'
    assert cliargs_deferred_get('stack', default=[])() == []
    assert cliargs_deferred_get('stack', default=['foo'])() == ['foo']
    assert cliargs_deferred_get('stack', default={})() == {}
    assert cliargs_deferred_get('stack', default={'foo': 'bar'})() == {'foo': 'bar'}
    class MyStr(string_types):
        pass
    assert cliargs_def

# Generated at 2022-06-12 21:15:31.339096
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from copy import copy

    # no default set and key not in CLIARGS
    res = cliargs_deferred_get('test')()
    assert res is None

    # no default set and key in CLIARGS
    CLIARGS['test'] = 'testing'
    res = cliargs_deferred_get('test')()
    assert res == 'testing'

    # default set but key not in CLIARGS
    res = cliargs_deferred_get('test', default='default')()
    assert res == 'default'

    # default set and key in CLIARGS
    res = cliargs_deferred_get('test', default='default')()
    assert res == 'testing'

    # default set and key in CLIARGS with shallow copy

# Generated at 2022-06-12 21:15:39.463617
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """
    The purpose of this test is to ensure that cliargs_deferred_get is robust,
    and guards against potential refactorings
    """
    # Testing with empty-string default value
    my_deferred_get = cliargs_deferred_get(key='some_key', default='', shallowcopy=False)
    my_default = my_deferred_get()
    assert my_default == '', 'Unexpected value: {0}'.format(my_default)

    # Testing with list default value
    my_deferred_get = cliargs_deferred_get(key='some_other_key', default=[], shallowcopy=False)
    my_default = my_deferred_get()
    assert my_default == [], 'Unexpected value: {0}'.format(my_default)

# Generated at 2022-06-12 21:15:50.395818
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_obj = object()

    class FakeOpts(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.kwargs = kwargs

        def __getitem__(self, key):
            return self.kwargs[key]

    global CLIARGS
    CLIARGS = FakeOpts(
        ansible_opts=FakeOpts(
            testitem=test_obj,
            testlist=['test'],
            testdict={'test': 'test'},
            testsets={'test'}
        )
    )

    # testitem is an object
    assert test_obj is cliargs_deferred_get('ansible_opts.testitem')()

    # testlist is a list
    assert ['test'] == cliargs

# Generated at 2022-06-12 21:16:00.824326
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    from ansible.module_utils.common._collections_compat import Sequence, Mapping, Set

    # Set up some example data
    testdata = dict(
        list_data=[9, 8, 7],
        dict_data={'one': 1, 'two': 2, 'three': 3},
        set_data=set(['a', 'b', 'c']),
    )

    # Call cliargs_deferred_get and verify it returns the correct data
    for key, value in testdata.items():
        inner_func = cliargs_deferred_get(key)
        assert inner_func() == value

    # Call cliargs_deferred_get with default values and verify it returns the default when
    # key is not set

# Generated at 2022-06-12 21:16:12.715325
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'ANSIBLE_DEBUG': True})
    assert cliargs_deferred_get('ANSIBLE_DEBUG')() is True

    _init_global_context({'ANSIBLE_DEBUG': False})
    assert cliargs_deferred_get('ANSIBLE_DEBUG')() is False

    # Test that we pass through the default
    assert cliargs_deferred_get('DOES_NOT_EXIST', default=True)() is True

    _init_global_context({'ANSIBLE_DEBUG': [True]})
    assert cliargs_deferred_get('ANSIBLE_DEBUG', shallowcopy=True)() == [True]

    _init_global_context({'ANSIBLE_DEBUG': set([True])})
    assert cliargs_deferred_get('ANSIBLE_DEBUG', shallowcopy=True)()

# Generated at 2022-06-12 21:16:22.980381
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    # start with empty context
    CLIARGS = CLIArgs({})
    # get a field which doesn't exist
    field1 = cliargs_deferred_get('field1')
    # should be default of None
    assert field1() is None
    # field should not exist in CLIARGS
    assert 'field1' not in CLIARGS

    # add field with a default of None
    CLIARGS['field1'] = None
    # get field
    field1 = cliargs_deferred_get('field1')
    # should be None
    assert field1() is None
    # field should exist in CLIARGS
    assert 'field1' in CLIARGS

    # add field with a value of 'foobar'
    CLIARGS['field1'] = 'foobar'
    # get field with

# Generated at 2022-06-12 21:16:24.516600
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # TODO: Make a test for this
    pass

# Generated at 2022-06-12 21:16:38.838602
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    from copy import copy
    # Test defaulting
    _init_global_context(ImmutableDict())
    assert CLIARGS.get('foo', 'bar') == 'bar'
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'
    _init_global_context(ImmutableDict(foo=2))
    assert CLIARGS.get('foo', 'bar') == 2
    assert cliargs_deferred_get('foo', 'bar')() == 2

    # Test non-defaulting
    assert CLIARGS.get('foo') == 2
    assert cliargs_deferred_get('foo')() == 2

    # Test shallow copy returns a copy

# Generated at 2022-06-12 21:16:46.320813
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Make sure get works
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo') == 'bar'

    # Make sure that we get the default
    assert cliargs_deferred_get('foo2', default='baz') == 'baz'

    # Make sure copying works for various types
    CLIARGS['copyme'] = [2, 3]
    assert cliargs_deferred_get('copyme') == [2, 3]
    assert cliargs_deferred_get('copyme', shallowcopy=True) == [2, 3]

    CLIARGS['copyme'] = {'a': 1}
    assert cliargs_deferred_get('copyme') == {'a': 1}

# Generated at 2022-06-12 21:16:55.679760
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(a=1, b=dict(c=2), d=dict(e=3, f=4)))
    assert 1 == cliargs_deferred_get('a')()
    # Shallow copy of a mutable is the same object
    assert 1 == cliargs_deferred_get('a', shallowcopy=True)()
    assert 2 == cliargs_deferred_get('b.c')()
    assert 2 == cliargs_deferred_get('b.c', shallowcopy=True)()
    assert dict(e=3, f=4) == cliargs_deferred_get('d')()
    assert dict(e=3, f=4) != cliargs_deferred_get('d', shallowcopy=True)()
    assert 3 == cliargs_deferred_

# Generated at 2022-06-12 21:17:07.139677
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils import context_objects
    def test_func(method, copy_ansible_context):
        # Use an empty dict as the cliargs_deferred_get is a closure over CLIARGS
        context = context_objects.CLIArgs({})
        original_ansible_context = context_objects.ANSIBLE_CONTEXT_CLOSURE
        if copy_ansible_context:
            context_objects.ANSIBLE_CONTEXT_CLOSURE = cliargs_deferred_get(method)
        else:
            context_objects.ANSIBLE_CONTEXT_CLOSURE = context
        test_value = context_objects.cliargs_deferred_get('foo', default='bar')
        context.CLIARGS = dict(foo='bar')

# Generated at 2022-06-12 21:17:17.540159
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence

    assert cliargs_deferred_get('nope')() is None
    assert cliargs_deferred_get('nope', 'blah')() == 'blah'

    # If the cliargs are (or will be) a list make sure that if it's a shallow copy
    # then we don't get the same object back
    _init_global_context({'blah': [1, 2, 3]})
    assert cliargs_deferred_get('blah', shallowcopy=False)() == [1, 2, 3]
    assert cliargs_deferred_get('blah', shallowcopy=True)() == [1, 2, 3]


# Generated at 2022-06-12 21:17:29.224202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCliArgs(object):
        """Object that has getattr work like a dict"""
        def __init__(self, **kwargs):
            self._attrs = kwargs

        def __getattr__(self, name):
            return self._attrs[name]

    # Test with a traditional list
    cli_args = TestCliArgs(verbosity=1, listattr=[0, 1, 2])
    assert cliargs_deferred_get('listattr', default=None)() == [0, 1, 2]

    # Test with a traditional mapping
    cli_args = TestCliArgs(verbosity=1, mapattr=dict(a=1, b=2, c=3))

# Generated at 2022-06-12 21:17:40.633825
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    class FakeCliArgs(object):
        def __init__(self, values):
            self._values = values

        def get(self, key, default=None):
            return self._values.get(key, default)

        def __getitem__(self, key):
            return self._values[key]

        def __iter__(self):
            return iter(self._values)

        def __contains__(self, key):
            return key in self._values

    fake_cliargs = FakeCliArgs({"a": 1, "b": [2, 3, 4], "c": {"d": 5, "e": 6}})

    fca = cliargs_deferred_get(
        'a', default=None, shallowcopy=False)
    assert fca() == 1

    fcb = cliargs_def

# Generated at 2022-06-12 21:17:43.755460
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')(), 'bar'

# Generated at 2022-06-12 21:17:51.558963
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3]})
    global CLIARGS
    CLIARGS = cliargs
    fdg = cliargs_deferred_get

    assert fdg('foo') == 'bar'
    assert fdg('foo', default='baz') == 'bar'
    assert fdg('baz', default='baz') == [1, 2, 3]
    assert fdg('baz', default='baz', shallowcopy=True) == [1, 2, 3]

# Generated at 2022-06-12 21:17:57.226557
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('debug')(), False
    assert cliargs_deferred_get('verbosity')(), 0
    assert cliargs_deferred_get('verbosity', default=7)(), 7
    assert cliargs_deferred_get('roles_path')(), []
    assert cliargs_deferred_get('roles_path', shallowcopy=True)(), []

# Generated at 2022-06-12 21:18:13.422974
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import AttributeDict
    cliargs = AttributeDict(a=1, b=2, c=[3, 4, 5], d={'x': 1, 'y': 2}, e=AttributeDict(x=1, y=2))
    _init_global_context(cliargs)
    assert(cliargs_deferred_get('a')() == 1)
    assert(cliargs_deferred_get('b')() == 2)
    assert(cliargs_deferred_get('c')() == [3, 4, 5])
    assert(cliargs_deferred_get('d')() == {'x': 1, 'y': 2})
    assert(cliargs_deferred_get('e')() == AttributeDict(x=1, y=2))



# Generated at 2022-06-12 21:18:20.953454
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = 'bar'
    closure = cliargs_deferred_get('foo')
    assert 'bar' == closure()
    assert 'bar' == cliargs_deferred_get('foo')()

    CLIARGS['foo'] = ['bar']
    assert ['bar'] == closure()
    assert ['bar'] == cliargs_deferred_get('foo')()

    key = 'bar'
    default = 'baz'
    assert default == cliargs_deferred_get(key, default)()
    assert default == cliargs_deferred_get(key, default)()

# Generated at 2022-06-12 21:18:28.667810
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    input = {'key1': 'value1', 'key2': 'value2'}
    CLIARGS = GlobalCLIArgs.from_options(input)
    assert cliargs_deferred_get('key1', default='value')() == 'value1'
    assert cliargs_deferred_get('nokey', default='value')() == 'value'
    assert cliargs_deferred_get('key1', shallowcopy=True)() == 'value1'
    assert cliargs_deferred_get('key2', shallowcopy=True)() == 'value2'
    assert cliargs_deferred_get('nokey', shallowcopy=True) == None
    CLIARGS.clear_cached()
    CLIARGS = CLIArgs(input)
    assert cliargs_def

# Generated at 2022-06-12 21:18:35.429130
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=protected-access
    """Test the cliargs_deferred_get function
    """
    # Call the inner function before the CLIARGS singleton has been initialized
    inner = cliargs_deferred_get('foo', default=42)
    assert inner() == 42
    # Call the inner function after CLIARGS singleton has been initialized
    CLIARGS._initialize({'foo': 1})
    assert inner() == 1

# Generated at 2022-06-12 21:18:44.789200
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})
    cliargs_deferred_get('__builtin__')().__name__ == 'builtins'  # check that it defaults to the builtin module
    CLIARGS._dict = {'__builtin__': __name__}
    assert cliargs_deferred_get('__builtin__')() == __name__  # check that it returns the value from CLIARGS
    assert cliargs_deferred_get('test', default='test') == 'test'  # check that it returns the default value
    assert cliargs_deferred_get('test')('test')() == 'test'  # check that it returns the default value

# Generated at 2022-06-12 21:18:46.566298
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(dict(foo='bar'))
    assert cliargs_deferred_get('foo')() == 'bar'

# Generated at 2022-06-12 21:18:58.125574
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_cliargs = {'arg1': {'item1': 1}, 'arg2': [1, 2]}
    _init_global_context(test_cliargs)
    assert cliargs_deferred_get('arg1') == test_cliargs['arg1']
    assert cliargs_deferred_get('arg2') == test_cliargs['arg2']
    assert cliargs_deferred_get('arg2', shallowcopy=True) == test_cliargs['arg2']
    assert cliargs_deferred_get('arg2', shallowcopy=True) is not test_cliargs['arg2']
    assert cliargs_deferred_get('arg3', default='default') == 'default'
    assert cliargs_deferred_get('arg3') is None

# Generated at 2022-06-12 21:19:08.425339
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'foo': [1, 2, 3], 'bar': {'a': 1, 'b': 2}, 'baz': 'hello', 'qux': set([1, 2, 3])}
    _init_global_context(cli_args)
    assert CLIARGS['foo'] == [1, 2, 3]
    # Check that default value is returned when key is missing
    assert cliargs_deferred_get('missing', default='testing') == 'testing'
    assert cliargs_deferred_get('missing', default='testing', shallowcopy=True) == 'testing'
    # Check that shallow copy is made
    assert cliargs_deferred_get('foo', shallowcopy=True) == [1, 2, 3]

# Generated at 2022-06-12 21:19:17.734664
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_dict = {'foo': 'bar'}
    test_seq = ('a', 'b', 'c')
    test_set = {'a', 'b', 'c'}
    key = 'test_dict'

    def inner():
        # Test defaults
        assert cliargs_deferred_get(key)() is None
        assert cliargs_deferred_get(key, default='bar')() == 'bar'
        assert cliargs_deferred_get(key, default=test_dict)().get('foo') == 'bar'
        assert cliargs_deferred_get(key, default=test_seq)() == ('a', 'b', 'c')
        assert cliargs_deferred_get(key, default=test_set)() == {'a', 'b', 'c'}
       

# Generated at 2022-06-12 21:19:26.532496
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test for ``key`` being None
    assert cliargs_deferred_get(None)() == {}

    # Test for ``key`` not being None
    key = 'foo'
    default = 'bar'
    assert cliargs_deferred_get(key, default=default)() == default

    # Test for ``key`` existing in the ``CLIARGS``
    value = 'value'
    CLIARGS[key] = value
    assert cliargs_deferred_get(key, default=default)() == value

    # Test for ``key`` existing in ``CLIARGS`` and shallowcopy being set
    sequence = ['foo', 'bar']
    CLIARGS[key] = sequence
    assert cliargs_deferred_get(key, default=default, shallowcopy=True)() == sequence

    # Test for

# Generated at 2022-06-12 21:19:43.678827
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    ret = cliargs_deferred_get('foo', {})
    assert ret == {}
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert ret == 'bar'
    CLIARGS = CLIArgs({'foo': {'one': 1}})
    assert ret == {'one': 1}
    assert ret() == {'one': 1}
    assert ret(shallowcopy=True) == {'one': 1}
    CLIARGS = CLIArgs({'foo': ['one', 1]})
    assert ret == ['one', 1]
    assert ret() == ['one', 1]
    assert ret(shallowcopy=True) == ['one', 1]
    CLIARGS = CLIArgs({'foo': set(['one', 1])})

# Generated at 2022-06-12 21:19:52.957993
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'foo': 'foo_value', 'bar': 'bar_value', 'baz': ['baz_value', 'baz_value2']})

    get_foo = cliargs_deferred_get('foo')
    get_bar = cliargs_deferred_get('bar')
    get_baz = cliargs_deferred_get('baz')
    get_blah = cliargs_deferred_get('blah', default='blah_value')

    get_foo_shallowcopy = cliargs_deferred_get('foo', shallowcopy=True)
    get_baz_shallowcopy = cliargs_deferred_get('baz', shallowcopy=True)

# Generated at 2022-06-12 21:20:00.311342
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for function :py:func:`test_cliargs_deferred_get`"""
    original_dict = {'foo': [1, 2, 3]}
    CLIARGS['foo'] = original_dict['foo']
    # Test when we are not shallow copying
    cliargs_deferred = cliargs_deferred_get('foo')
    returned_dict = cliargs_deferred()
    assert id(original_dict['foo']) == id(returned_dict)
    # Test when we are shallow copying
    cliargs_deferred = cliargs_deferred_get('foo', shallowcopy=True)
    returned_dict = cliargs_deferred()
    assert id(original_dict['foo']) != id(returned_dict)
    assert original_dict['foo'] == returned_dict


# Generated at 2022-06-12 21:20:09.397240
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the functionality of cliargs_deferred_get"""
    def inner():
        return cliargs_deferred_get('foo')()

    old_cliargs = CLIARGS
    try:
        CLIARGS = CLIArgs({'foo': 1})
        assert inner() == 1

        CLIARGS = CLIArgs({})
        assert inner() is None

        CLIARGS = CLIArgs({'foo': {1: 2}})
        assert inner() == {1: 2}

        CLIARGS = CLIArgs({'foo': [1, 2, 3]})
        assert inner() == [1, 2, 3]

        CLIARGS = CLIArgs({})
        assert inner() is None
    finally:
        CLIARGS = old_cliargs

# Generated at 2022-06-12 21:20:17.699961
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for ``cliargs_deferred_get``"""
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'
    CLIARGS['foo'] = 'baz'
    assert cliargs_deferred_get('foo', 'bar')() == 'baz'
    CLIARGS['foo'] = ['one', 'two', 'three']
    assert cliargs_deferred_get('foo', 'bar', shallowcopy=True)() == ['one', 'two', 'three']
    assert cliargs_deferred_get('foo', 'bar', shallowcopy=False)() is CLIARGS['foo']


# Generated at 2022-06-12 21:20:21.408596
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    try:
        val = cliargs_deferred_get('key')()

    finally:
        CLIARGS = GlobalCLIArgs.from_options({})

# Generated at 2022-06-12 21:20:30.773727
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _test_with_value(key, default=None, shallowcopy=False):
        cli_args = dict()
        cli_args[key] = 'abc'
        _init_global_context(cli_args)
        deferred_get = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)
        if shallowcopy:
            assert cli_args[key] == deferred_get()
        else:
            assert cli_args[key] is deferred_get()

    def _test_default(key, default=None, shallowcopy=False):
        cli_args = dict()
        _init_global_context(cli_args)
        deferred_get = cliargs_deferred_get(key, default=default, shallowcopy=shallowcopy)

# Generated at 2022-06-12 21:20:40.186127
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy

    # Test with empty dict, missing key
    result = cliargs_deferred_get(key='key', default=2)()
    assert result == 2

    # Test with dict with no key, but with a default
    test_dict = {'a': 1}
    result = cliargs_deferred_get(key='b', default=test_dict)(test_dict)
    assert result is test_dict

    # Test with dict with no key, no default
    result = cliargs_deferred_get(key='b')(test_dict)
    assert result is None

    # Test with dict with no key, and a default
    test_dict = {'a': 1}
    result = cliargs_deferred_get(key='b', default=2)(test_dict)
    assert result == 2



# Generated at 2022-06-12 21:20:51.417892
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the ``cliargs_deferred_get`` function"""
    def _test(cliargs=None, key=None, default=None):
        global CLIARGS
        CLIARGS = CLIArgs(cliargs)
        my_dict = {'a': 1, 'b': 2}
        my_set = {1, 2, 3}

        f1 = cliargs_deferred_get(key, default)
        f2 = cliargs_deferred_get(key, default, shallowcopy=True)
        assert f1() == f2()

        if not cliargs:
            assert f1() == default
            assert f2() == default
        else:
            assert f1() == cliargs[key]
            assert f2() == cliargs[key]
            cliargs[key] = my_dict

# Generated at 2022-06-12 21:21:00.242024
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Any import of ``CLIARGS`` will have to have ``CLIARGS`` instantiated
    # for unit tests.  If not then we will be using the CLIARGS closure
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3], 'qux': {'a': 1, 'b': 2}, 'spam': {'a', 'b'}})

    # simple key, no copy
    assert cliargs_deferred_get('foo')() == 'bar'
    # simple key, shallow copy
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

    # list key, no copy
    value = cliargs_deferred_get('baz')()
    assert value is cliargs_deferred_

# Generated at 2022-06-12 21:21:28.692191
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 21:21:37.234674
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest

    class DummyClass1(object):
        # Defaults to None
        cli_arg = cliargs_deferred_get('--unknown-arg')

    class DummyClass2(object):
        # Defaults to 'world'
        cli_arg2 = cliargs_deferred_get('--unknown-arg2', default='world')

    class DummyClass3(object):
        # Defaults to 'world'
        cli_arg3 = cliargs_deferred_get('--unknown-arg3', default='world', shallowcopy=True)

    class DummyClass4(object):
        # Defaults to 'world'
        cli_arg4 = cliargs_deferred_get('--unknown-arg4', default='world', shallowcopy=False)


# Generated at 2022-06-12 21:21:45.984430
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get"""
    def test_get(key, value, shallowcopy):
        """Closure over test values for function cliargs_deferred_get"""
        def inner():
            """Test closure"""
            cliargs_dict = {key: value}
            _init_global_context(cliargs_dict)
            result = cliargs_deferred_get(key, shallowcopy=shallowcopy)()
            assert result == value
        return inner

    test_get('a', 'b', True)()
    test_get('a', 1, True)()
    test_get('a', [1, 2, 3], True)()
    test_get('a', [1, 2, 3], False)()
    test_get('a', {1, 2, 3}, True)()

# Generated at 2022-06-12 21:21:57.147590
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import list_of_strings
    CLIARGS.update({'foo': 'bar'})
    assert cliargs_deferred_get('foo')(), 'bar'
    assert cliargs_deferred_get('boo')(), None

    def test_deferred_with_default():
        assert cliargs_deferred_get('boo', 'baa')(), 'baa'

    CLIARGS.update({'foo': list_of_strings(['bar'])})
    assert cliargs_deferred_get('foo')(), ['bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)(), ['bar']

    CLIARGS.update({'foo': Set([1, 2, 3])})
    assert cliargs_

# Generated at 2022-06-12 21:22:07.761188
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import unittest

    class TestCLIArgsDeferredGet(unittest.TestCase):
        def test_ta(self):
            # No key
            cadi = CLIArgs({})
            CLIARGS = GlobalCLIArgs.from_options(cadi)
            # Default provided, shallowcopy true
            self.assertEqual(cliargs_deferred_get('key', default='val1')(), 'val1')
            # Default provided, shallowcopy false
            self.assertEqual(cliargs_deferred_get('key', default='val1', shallowcopy=False)(), 'val1')
            # No default, key doesn't exist
            self.assertIsNone(cliargs_deferred_get('key')(), None)

# Generated at 2022-06-12 21:22:17.870833
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', default='baz')() == 'bar'
    assert cliargs_deferred_get('bar', default='baz')() == 'baz'
    CLIARGS['bar'] = ['foo', 'bar', 'baz']
    assert cliargs_deferred_get('bar', shallowcopy=True)() == ['foo', 'bar', 'baz']
    CLIARGS['bar'] = set(['foo', 'bar', 'baz'])
    assert cliargs_deferred_get('bar', shallowcopy=True)() == set(['foo', 'bar', 'baz'])

# Generated at 2022-06-12 21:22:26.251468
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function CLIARGS_DEFERRED_GET

    Used to test that ``CLIARGS_DEFERRED_GET`` returns the value from ``CLIARGS``
    and also that it returns a shallow copy (if requested) of the value.
    """
    global CLIARGS
    # Tests that the arg is retrieved from CLIARGS
    CLIARGS = CLIArgs({'arg': 'value'})
    assert 'value' == cliargs_deferred_get('arg')()
    assert 'value' == cliargs_deferred_get('arg', 'default')()
    assert 'default' == cliargs_deferred_get('default_value', 'default')()

    # Tests that the results are shallow copied
    value = ['value']
    CLIARGS = CLIArgs({'arg': value})
    assert value

# Generated at 2022-06-12 21:22:38.028410
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pylint: disable=no-self-use
    class FakeCliArgs:
        def __init__(self, input_dict):
            self.input_dict = input_dict

        def __getitem__(self, key):
            return self.input_dict[key]

        def get(self, key, default=None):
            return self.input_dict.get(key, default)

    cli_arg_values = {'var': 'foo', 'list': [1, 2, 3], 'set': set(range(3)), 'dict': {'a': 1, 'b': 2}}

    def inner():
        cliargs_deferred = cliargs_deferred_get('var', 'default')()
        assert cliargs_deferred == 'foo'

        cliargs_deferred = cliargs_

# Generated at 2022-06-12 21:22:46.784557
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs_init_dict = {'DEFAULT_CALLBACK_WHITELIST': ['get_url', 'get_urls']}
    _init_global_context(cliargs_init_dict)
    value_function = cliargs_deferred_get('DEFAULT_CALLBACK_WHITELIST')
    assert value_function() == ['get_url', 'get_urls']
    value_function = cliargs_deferred_get('DEFAULT_CALLBACK_WHITELIST', shallowcopy=True)
    assert value_function() == ['get_url', 'get_urls']
    value_function = cliargs_deferred_get('DEFAULT_CALLBACK_WHITELIST', default=['wait_for'])

# Generated at 2022-06-12 21:22:57.919541
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    cli_args = {'some_key': 'any old value'}
    CLIARGS = CLIArgs(cli_args)
    assert cliargs_deferred_get('some_key')() == 'any old value'

    # Can also test with GlobalCLIArgs
    # Calling it GlobalCLIArgs_test to avoid collisions when running pytests on the whole tree
    # Note: If a GlobalCLIArgs singleton exists before this test is run it will still be used.  If we really need to
    # test this with a GlobalCLIArgs, we may have to find some way to force the singleton to be created here
    class GlobalCLIArgs_test(GlobalCLIArgs):
        @staticmethod
        def from_options(cli_args):
            return GlobalCLIArgs_test(cli_args)
   

# Generated at 2022-06-12 21:23:43.150796
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    default_value = (1, 2, 3)
    a = cliargs_deferred_get('a', default_value, shallowcopy=False)
    assert a() is CLIARGS.get('a')
    b = cliargs_deferred_get('b', default_value, shallowcopy=True)
    assert b() == CLIARGS.get('b')
    assert b() is not CLIARGS.get('b')
    c = cliargs_deferred_get('c', default_value, shallowcopy=False)
    assert c() is default_value

# Generated at 2022-06-12 21:23:50.760666
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function ``cliargs_deferred_get``"""
    # pylint: disable=too-many-statements
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.six import text_type, binary_type
    from ansible.module_utils._text import to_bytes
    import copy
    import pickle
    import sys
    import types

    # first use with a normal dictionary:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    f = cliargs_deferred_get('a')
    assert f is not None
    assert f() == 1

# Generated at 2022-06-12 21:24:02.073411
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # empty cli arguments
    cliargs = {}
    _init_global_context(cliargs)
    default_value = []
    assert cliargs_deferred_get('nonexistant_key', default=default_value) is default_value
    # shallowcopy is True by default
    assert cliargs_deferred_get('nonexistant_key', default=default_value) is not default_value
    # sequence returned as expected
    assert cliargs_deferred_get('nonexistant_key', default=default_value, shallowcopy=True) is not default_value
    # mapping returned as expected
    default_value = {'foo': 'bar'}
    assert cliargs_deferred_get('nonexistant_key', default=default_value, shallowcopy=True) is not default_value
    assert cli

# Generated at 2022-06-12 21:24:10.124240
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'foo': 'bar', 'baz': dict(qux='quux')})
    assert 'bar' == cliargs_deferred_get('foo', default='notbar')()
    assert 'notbar' == cliargs_deferred_get('blah', default='notbar')()
    assert {'qux': 'quux'} == cliargs_deferred_get('baz', shallowcopy=True)()
    assert {'qux': 'quux'} == cliargs_deferred_get('baz', shallowcopy=True)()

# Generated at 2022-06-12 21:24:21.378297
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _get_return(key):
        return CLIARGS._get_return(key)

    # When not set
    assert cliargs_deferred_get('foo')() is None

    # When set, but not shallow copy
    CLIARGS.set('foo', 'Value of foo')
    assert cliargs_deferred_get('foo')() == 'Value of foo'

    # When set and shallow copy
    CLIARGS.set('bar', 'Value of bar')
    assert cliargs_deferred_get('bar', shallowcopy=True)() == 'Value of bar'

    CLIARGS.set('foo', ['a', 'b'])
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['a', 'b']

# Generated at 2022-06-12 21:24:32.759900
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs(dict(a=1, b='foo'))
    assert cliargs_deferred_get('a')(None) == 1
    assert cliargs_deferred_get('b')(None) == 'foo'
    assert cliargs_deferred_get('b', 'bar')(None) == 'foo'
    assert cliargs_deferred_get('c', 'bar')(None) == 'bar'
    assert cliargs_deferred_get('a', shallowcopy=True)(None) == 1
    assert cliargs_deferred_get('b', shallowcopy=True)(None) == 'foo'
    assert cliargs_deferred_get('b', 'bar', shallowcopy=True)(None) == 'foo'
    assert cliargs_deferred_

# Generated at 2022-06-12 21:24:44.586695
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test that cliargs_deferred_get() gets the value of CLIARGS."""
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSet
    from ansible.module_utils.common.dicts import type_defs

    def get(key, default=None):
        if key not in self:
            return default
        return self[key]
    def inc_loop():
        self['loop_count'] += 1

    class TestCliArgs(MutableMapping):
        """Mock object for tests.

        For testing we don't care about the internal state of ``CLIARGS`` so
        this just wraps the provided dict for internal state.
        """



# Generated at 2022-06-12 21:24:56.403840
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():

    value_map = {'any_value': 'any_value',
                 'set_value': set([1, 2, 3, 4]),
                 'list_value': [1, 2, 3, 4],
                 'dict_value': {'a': 1, 'b': 2},
                 'default': 'default'}

    def check(key, expected_shallow, expected_deep):
        inner = cliargs_deferred_get(key)
        assert inner() is expected_shallow
        assert inner() is expected_deep
        inner = cliargs_deferred_get(key, shallowcopy=True)
        assert inner() is expected_shallow
        assert inner() is not expected_deep

    for name, value in value_map.items():
        check(name, value, value)

    # This test is only needed for set