

# Generated at 2022-06-12 21:15:06.700786
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def _test(value):
        def _inner():
            return value
        return _inner

    cliargs = {}
    assert cliargs_deferred_get('')() is None
    assert cliargs_deferred_get('', default=10)() == 10
    cliargs['key'] = 10
    assert cliargs_deferred_get('key')() == 10
    cliargs['key'] = _test(20)
    assert cliargs_deferred_get('key')() == 20
    cliargs['key'] = {'a': 20}
    assert cliargs_deferred_get('key')() == {'a': 20}
    assert cliargs_deferred_get('key', shallowcopy=True)() == {'a': 20}

# Generated at 2022-06-12 21:15:15.790784
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    context = CLIArgs({'a': 1,
                       'b': [1,2,3],
                       'c': {'key': 'value'},
                       'd': set(['A', 'B', 'C'])})
    assert context.get('a', 5) == 1
    assert context.get('b', [1,2,3]) == [1,2,3]
    assert context.get('c', {'key': 'value'}) == {'key': 'value'}
    assert context.get('d', {'A', 'B'}) == set(['A', 'B', 'C'])

    assert context.get('a', shallowcopy=True) == 1
    assert context.get('b', shallowcopy=True) == [1,2,3]
    assert context.get('c', shallowcopy=True)

# Generated at 2022-06-12 21:15:26.127143
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test a key that exists in the dictionary
    cli_args = {'ask_val': 'http://foo'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('ask_val') == 'http://foo'
    assert cliargs_deferred_get('ask_val', shallowcopy=True) == 'http://foo'
    assert cliargs_deferred_get('become_method') == 'sudo'
    assert cliargs_deferred_get('become_method', shallowcopy=True) == 'sudo'

    # Test a key that does not exist in the dictionary
    assert cliargs_deferred_get('ask_val2') is None
    assert cliargs_deferred_get('ask_val2', shallowcopy=True) is None

    # Test a

# Generated at 2022-06-12 21:15:36.513141
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from collections import OrderedDict
    from ansible.module_utils.six import string_types

    def do_test(key, default, shallowcopy):
        result = cliargs_deferred_get(key, default, shallowcopy)()
        assert result is not default
        for k, v in result.items():
            if isinstance(v, string_types):
                assert isinstance(k, string_types)
            elif isinstance(v, int):
                assert isinstance(k, int)
            else:
                assert False, "Unknown value type: {}".format(v)
        return result

    def copy_dict(dictionary):
        return OrderedDict((k, dictionary[k]) for k in dictionary)


# Generated at 2022-06-12 21:15:47.850500
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class CLIArgs:
        def __init__(self, value):
            self.value = value

        def get(self, key, default=None):
            return self.value

    cli_args = CLIArgs('foo')
    cb = cliargs_deferred_get(None)
    global CLIARGS
    CLIARGS = cli_args

    assert cb() == 'foo'

    cli_args = CLIArgs([1, 2, 3])
    cb = cliargs_deferred_get(None, shallowcopy=True)
    CLIARGS = cli_args

    assert cb() == [1, 2, 3]

    cli_args = CLIArgs({'foo': 1, 'bar': 2})
    cb = cliargs_deferred_get(None, shallowcopy=True)


# Generated at 2022-06-12 21:15:58.543453
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import Context
    from ansible.utils.context_objects import CLIArgs
    from ansible.utils.context_objects import GlobalCLIArgs
    import copy

    class MyContext(Context):
        # at this point the CLIARGS have not been initialized
        # So we can't just set the default as cliargs['foo']
        # Instead, we use a closure to return the value of cliargs['foo']
        # when the default is actually needed
        foo = 'bar'
        foo_deferred_default = cliargs_deferred_get('foo')

        # test nested shallowcopy
        # normally this would need to be a class variable, but since
        # we can't return a class variable from the closure, we
        # convert it to an instance variable in __init__
        foo_deferred_

# Generated at 2022-06-12 21:16:08.615534
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = GlobalCLIArgs.from_options({})

    # Note: this will fail if you import this module directly.  It will only
    # pass when it is imported by Ansible, where the _init_global_context has
    # been called
    assert CLIARGS is old_cliargs

    val = cliargs_deferred_get('foo')
    assert val() is None

    CLIARGS = GlobalCLIArgs.from_options({'foo': 'bar'})
    assert val() == 'bar'

    def f():
        pass
    CLIARGS = GlobalCLIArgs.from_options({'foo': f})

# Generated at 2022-06-12 21:16:19.230479
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS  # pylint: disable=global-statement

    CLIARGS = CLIArgs({'a': 'foo', 'b': 'bar', 'c': [1, 2], 'd': {1: 2}, 'e': {'x': 'y'}, 'f': (1,)})

    assert cliargs_deferred_get('a', default='baz')() == 'foo'
    # Default won't be used until after CLIARGS has been initialized
    assert cliargs_deferred_get('z', default='baz')() == 'baz'
    assert cliargs_deferred_get('c', shallowcopy=True)() == [1,2]
    assert cliargs_deferred_get('c')() == [1,2]

# Generated at 2022-06-12 21:16:26.950992
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('test', shallowcopy=True)() is None
    CLIAGS = CLIArgs({'test': True})
    assert cliargs_deferred_get('test', shallowcopy=True)() is True
    assert cliargs_deferred_get('test', default=False, shallowcopy=True)() is True
    assert cliargs_deferred_get('not-a-key', shallowcopy=True)() is None
    assert cliargs_deferred_get('not-a-key', default=False, shallowcopy=True)() is False
    assert cliargs_deferred_get('not-a-key', default=True, shallowcopy=True)() is True

    assert cliargs_deferred_get('test-list', default=[], shallowcopy=True)() == []

# Generated at 2022-06-12 21:16:38.922867
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get

    This tests the closure functionality and that it refers to the global CLIARGS
    """
    global CLIARGS
    CLIARGS = CLIArgs({})
    my_get = cliargs_deferred_get('a', default=None)
    assert my_get() is None

    CLIARGS = CLIArgs({'a': 1})
    assert my_get() == 1

    CLIARGS = CLIArgs({'a': [1]})
    assert my_get(shallowcopy=True) == [1]
    assert my_get(shallowcopy=False) == [1]

    CLIARGS = CLIArgs({'a': {'b': 1}})
    assert my_get(shallowcopy=True) == {'b': 1}

# Generated at 2022-06-12 21:16:52.765862
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.clear()
    CLIARGS.update({
        'a': 2,
        'b': {'c': 3},
        'd': [4],
        'e': {'f': {'g': 5}},
        'h': [{'i': 6}, {'i': 7}],
    })
    assert cliargs_deferred_get('a')() == 2
    assert cliargs_deferred_get('b')() == {'c': 3}
    assert cliargs_deferred_get('d')() == [4]
    assert cliargs_deferred_get('e')() == {'f': {'g': 5}}
    assert cliargs_deferred_get('h')() == [{'i': 6}, {'i': 7}]


# Generated at 2022-06-12 21:17:04.317062
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    try:
        CLIARGS = CLIArgs(dict(a=1, b=2, c=3))

        default = cliargs_deferred_get('a')
        assert callable(default)
        assert default() == 1

        default = cliargs_deferred_get('d', default=4)
        assert callable(default)
        assert default() == 4

        default_list = cliargs_deferred_get('b', shallowcopy=True)
        assert callable(default_list)
        assert default_list() == 2
    finally:
        CLIARGS = CLIArgs(dict())


# Generated at 2022-06-12 21:17:06.499565
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.update({'a': 'b'})
    assert cliargs_deferred_get('a')() == 'b'

# Generated at 2022-06-12 21:17:16.937030
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def make_object(name):
        class X(object):
            def __init__(self, name):
                self.name = name
        return X(name)

    CLIARGS[u'foo'] = u'bar'
    CLIARGS[u'baz'] = [u'qux']
    CLIARGS[u'quux'] = {u'corge': u'grault'}
    CLIARGS[u'garply'] = make_object(u'waldo')

    assert cliargs_deferred_get(u'foo')() == u'bar'
    assert cliargs_deferred_get(u'baz', shallowcopy=True)() != [u'qux']

# Generated at 2022-06-12 21:17:20.616869
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('not_exist')(None) is None
    CLIARGS['test'] = 'test_value'
    assert cliargs_deferred_get('test')(None) == 'test_value'
    assert cliargs_deferred_get('not_exist', 'default')(None) == 'default'


# Generated at 2022-06-12 21:17:31.371230
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = {'foo': 'bar',
               'baz': ['seven', 'eleven'],
               'qux': {'forty': 'two', 'answer': 42}}
    _init_global_context(cliargs)
    assert cliargs_deferred_get('foo', default='baz') == 'bar'
    assert cliargs_deferred_get('baz', shallowcopy=True) == ['seven', 'eleven']
    assert cliargs_deferred_get('baz') is not cliargs['baz']
    assert cliargs_deferred_get('baz') == ['seven', 'eleven']
    assert cliargs_deferred_get('qux', shallowcopy=True) == {'forty': 'two', 'answer': 42}

# Generated at 2022-06-12 21:17:42.176354
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.utils.context_objects import GlobalCLIArgs

    test_cliargs = dict(
        ids=[],
        listtags=False,
        listtasks=False,
        listhosts=False,
    )
    # Map of values to test for each type of `shallowcopy`

# Generated at 2022-06-12 21:17:52.588641
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.utils.context_objects import GlobalCLIArgs

    class TestCliArgs(Mapping):
        def __init__(self, val):
            self._val = val

        def get(self, key, default=None):
            return self._val.get(key, default=default)

        def keys(self):
            return self._val.keys()

        def __getitem__(self, key):
            return self._val[key]

        def __len__(self):
            return len(self._val)

    # Test dict

# Generated at 2022-06-12 21:18:01.969764
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    __tracebackhide__ = True

    global CLIARGS
    old_cliargs_obj = CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': [1, 2, 3]})

    # Test simple get
    func = cliargs_deferred_get('foo')
    assert func() == 'bar'

    # Test simple get with a default
    func = cliargs_deferred_get('cog', default='nope')
    assert func() == 'nope'

    # Test list get with shallow copy
    func = cliargs_deferred_get('baz', shallowcopy=True)
    list_val = func()
    assert is_sequence(list_val)
    assert list_val == [1, 2, 3]
    list_val[0] = 'z'


# Generated at 2022-06-12 21:18:13.616395
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test with a default value
    default_value = 'foo'
    assert cliargs_deferred_get('does_not_exist')(default=default_value) == default_value
    assert cliargs_deferred_get('does_not_exist', default=default_value) == default_value

    # Test when a value is set
    cliargs = CLIArgs({'key': 'value'})
    assert cliargs_deferred_get('key')(cliargs=cliargs) == 'value'
    assert cliargs_deferred_get('key', cliargs=cliargs) == 'value'
    assert cliargs_deferred_get('key', default='baz', cliargs=cliargs) == 'value'

    # Test when a shallow copy is needed

# Generated at 2022-06-12 21:18:25.936709
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    value = {'key1': 'value'}

    def testfunc(shallowcopy=False):
        return cliargs_deferred_get('key1', value, shallowcopy=shallowcopy)

    mvalue = testfunc()
    assert mvalue is value, 'should return the default value'
    CLIARGS['key1'] = 'value1'
    mvalue = testfunc()
    assert mvalue == 'value1', 'should return value1'
    CLIARGS['key1'] = value
    mvalue = testfunc()
    assert mvalue is value, 'should return the same value'
    mvalue = testfunc(True)
    assert mvalue is not value, 'should not return the same value if shallowcopy True'

# Generated at 2022-06-12 21:18:37.546270
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    foo = 1
    inner = cliargs_deferred_get('foo', default=foo)

    # We should get the default if the key is not in CLIARGS
    CLIARGS.clear()
    assert(inner() is foo)

    # We should get the stored value if it exists in CLIARGS
    bar = 2
    CLIARGS.update({'foo': bar})
    assert(inner() is bar)

    # We should get a shallow copy of a sequence if the value is a sequence and shallowcopy=True
    baz = [1, 2, 3]
    CLIARGS.update({'foo': baz})
    assert(inner(shallowcopy=True) == baz and inner(shallowcopy=True) is not baz)

    # We should get a shallow copy of a Set if the value is a Set and shallowcopy

# Generated at 2022-06-12 21:18:47.484279
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'test_cliargs': True})
    assert cliargs_deferred_get('test_cliargs')()
    assert cliargs_deferred_get('non_existent_key')() is None
    assert cliargs_deferred_get('non_existent_key', default='foo')() == 'foo'
    assert cliargs_deferred_get('non_existent_key', default='foo', shallowcopy=True)() == 'foo'
    assert cliargs_deferred_get('non_existent_key', default=['foo', 'bar', 1])() == ['foo', 'bar', 1]

# Generated at 2022-06-12 21:18:58.782953
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit tests for cliargs_deferred_get"""
    from ansible.utils.context_objects import CLIArgs
    from ansible.module_utils.common.collections import is_sequence

    # Test object creation
    cli_args = {'a': 'A', 'b': 'B', 'c': ['C', 'D'], 'd': {'E': 'F'}, 'e': set()}
    CLIARGS.data = cli_args
    test_list = []
    for key, default in [('a', 'foo'), ('b', 'bar'), ('c', ['foo']), ('d', {}), ('e', [])]:
        test_list.append(cliargs_deferred_get(key, default=default))
    del CLIARGS.data

# Generated at 2022-06-12 21:19:09.445415
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get with various defaults"""
    # No default:
    _init_global_context(dict(foo=1))
    assert cliargs_deferred_get('foo')() == 1
    assert cliargs_deferred_get('foo')(default=None) == 1
    assert cliargs_deferred_get('missing')() is None
    assert cliargs_deferred_get('missing')(default=None) is None
    assert cliargs_deferred_get('missing')(default='foo') == 'foo'
    assert cliargs_deferred_get('missing')(default=1) == 1
    assert cliargs_deferred_get('missing')(default=dict()) == {}
    assert cliargs_deferred_get('missing')(default=list()) == []


# Generated at 2022-06-12 21:19:18.204885
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class C(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
        def __eq__(self, other):
            return self.__dict__ == other.__dict__
    def assert_shallow_copy_success(key, value):
        old_cliargs = CLIARGS
        try:
            CLIARGS = C(**{key: value})
            copy_func = cliargs_deferred_get(key, shallowcopy=True)
            assert value is not copy_func()
            assert value == copy_func()
        finally:
            CLIARGS = old_cliargs
    def assert_shallow_copy_failure(key, value):
        old_cliargs = CLIARGS

# Generated at 2022-06-12 21:19:26.773275
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCliArgs(object):
        def get(self, key, default=None):
            pass

    old_cli_args = CLIARGS
    cli_args = TestCliArgs()

# Generated at 2022-06-12 21:19:38.369707
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['vars'] = dict(a=1, b=2)
    assert cliargs_deferred_get('vars')() == dict(a=1, b=2)
    assert isinstance(cliargs_deferred_get('vars', default=dict())() is not CLIARGS['vars'], True)
    assert cliargs_deferred_get('vars', default=dict())() == dict()
    assert cliargs_deferred_get('vars', shallowcopy=True)() == dict(a=1, b=2)
    assert isinstance(cliargs_deferred_get('vars', shallowcopy=True)() is not CLIARGS['vars'], True)
    CLIARGS['vars'] = [1, 2]

# Generated at 2022-06-12 21:19:49.243828
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cliargs = CLIArgs({'a': 'b', 'c': [1, 2, 3], 'd': {'e': 'f'}})
    global CLIARGS
    CLIARGS = cliargs
    # should work normally
    assert cliargs_deferred_get('a') == 'b'
    assert cliargs_deferred_get('c') == [1, 2, 3]
    assert cliargs_deferred_get('d') == {'e': 'f'}
    assert not cliargs_deferred_get('z')
    # should work with shallow copy
    # -- normal mode
    cliargs['c'].append('foo')
    assert cliargs_deferred_get('c', shallowcopy=True) == [1, 2, 3, 'foo']

# Generated at 2022-06-12 21:19:57.308068
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_equal(x, y):
        if x != y:
            raise Exception("{} != {}".format(x, y))

    CLIARGS.data['a'] = 'b'
    test_equal(cliargs_deferred_get('a')(), 'b')
    test_equal(cliargs_deferred_get('a', default='c')(), 'b')
    test_equal(cliargs_deferred_get('a', default='c', shallowcopy=True)(), 'b')
    test_equal(cliargs_deferred_get('a', shallowcopy=True)(), 'b')
    test_equal(cliargs_deferred_get('b', default='c')(), 'c')

# Generated at 2022-06-12 21:20:17.144590
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the inline function CliArgs.deferred_get

    This test is built into the function so that it is documented what it is supposed to be
    testing.
    """
    global CLIARGS

    a_list = list('abc')
    a_dict = dict(a=1, b=2)
    a_set = {1, 2, 3}

    def test_get(default, cliargs, key, shallowcopy, expected_value, expected_type):
        """Test get for the given values"""
        # sanity check to make sure that cliargs actually has the value in it
        assert cliargs.get(key, default) == expected_value
        # actual test
        cliargs_instance = GlobalCLIArgs(cliargs)

# Generated at 2022-06-12 21:20:28.920975
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class CliArgs(CLIArgs):
        def get(self, key, default=None):
            return default

    global CLIARGS

    # Test default
    saved_cliargs = CLIARGS
    try:
        CLIARGS = CliArgs({})
        assert cliargs_deferred_get('foo', 'bar')() == 'bar'
        assert cliargs_deferred_get('foo', 'bar', shallowcopy=True)() == 'bar'
    finally:
        CLIARGS = saved_cliargs

    # Test cliargs returns something
    saved_cliargs = CLIARGS

# Generated at 2022-06-12 21:20:39.497055
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def call_closure(key):
        retval = closure()
        assert CLIARGS.get(key) == retval

    global CLIARGS
    # Check that a closure properly gets a value
    CLIARGS = GlobalCLIArgs.from_options({'foo': 2})
    closure = cliargs_deferred_get('foo')
    call_closure('foo')

    # Check that the closure still works after cliargs gets updated
    CLIARGS = GlobalCLIArgs.from_options({'foo': 5, 'bar': 'baz'})
    call_closure('foo')
    assert CLIARGS.get('bar') is not None
    call_closure('bar')

    # Check that the closure doesn't swallow errors in cliargs

# Generated at 2022-06-12 21:20:44.684367
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context(None)
    assert callable(cliargs_deferred_get('become'))
    assert callable(cliargs_deferred_get('become', None, True))
    assert cliargs_deferred_get('become', None, True)() is False
    assert callable(cliargs_deferred_get('check_mode'))
    assert callable(cliargs_deferred_get('check_mode', None, True))
    assert cliargs_deferred_get('check_mode', None, True)() is False
    assert callable(cliargs_deferred_get('tags'))
    assert callable(cliargs_deferred_get('tags', None, True))
    assert cliargs_deferred_get('tags', None, True)() == []

# Generated at 2022-06-12 21:20:48.945330
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    cli_args = {'foo': 'bar', 'flower': 'rose'}
    CLIARGS = CLIArgs(cli_args)
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('flower')() == 'rose'
    assert cliargs_deferred_get('car')() is None
    assert cliargs_deferred_get('car', default='truck')() == 'truck'
    assert cliargs_deferred_get('car', default='truck')() is not 'truck'

    mylist = ['a', 'b', 'c']
    assert cliargs_deferred_get('car', default=mylist)() is mylist

# Generated at 2022-06-12 21:20:58.616655
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():  # pragma: no cover
    from collections import Mapping, Set

    _init_global_context({})
    assert cliargs_deferred_get('foo', 'bar')() == 'bar'
    _init_global_context({'foo': 'baz'})
    assert cliargs_deferred_get('foo', 'bar')() == 'baz'

    _init_global_context({'foo': [1, 2, 3]})
    copy_val = cliargs_deferred_get('foo', [], shallowcopy=True)()
    assert copy_val == [1, 2, 3]
    assert copy_val is not CLIARGS['foo']
    dict_val = cliargs_deferred_get('foo')()
    assert dict_val == [1, 2, 3]

# Generated at 2022-06-12 21:21:09.257913
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Make sure it can handle a failure case
    global CLIARGS
    old_cliargs = CLIARGS

# Generated at 2022-06-12 21:21:15.686991
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # setup
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': ['one', 'two', 'three']})

    # test
    assert cliargs_deferred_get('foo')(), CLIARGS['foo']
    assert cliargs_deferred_get('baz')() == CLIARGS['baz'], cliargs_deferred_get('baz')()
    assert cliargs_deferred_get('baz', shallowcopy=True)() == CLIARGS['baz'], cliargs_deferred_get('baz')(shallowcopy=True)

# Generated at 2022-06-12 21:21:22.771846
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'one': 'one', 'two': ['one', 'two', 'three'], 'three': {'four': 'five'}, 'four': set([1, 2, 3])}
    _init_global_context(cli_args)
    # Get a single value
    first = cliargs_deferred_get('one')
    assert first == 'one'

    # Get a nested value
    second = cliargs_deferred_get('three')['four']
    assert second == 'five'

    # Get a immediate value with the default
    third = cliargs_deferred_get('five', default='six')
    assert third == 'six'

    # Get a nested value with the default
    fourth = cliargs_deferred_get('six', default={'seven': 'eight'})['seven']

# Generated at 2022-06-12 21:21:33.351599
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_dict = {'foo': 'bar', 'baz': 123}
    test_cliargs = CLIArgs(test_dict)
    assert cliargs_deferred_get('foo')() is test_cliargs.get('foo')

    test_list = [1, 2, 3]
    test_cliargs = CLIArgs(test_list)
    assert cliargs_deferred_get('foo')() is test_cliargs.get('foo')

    assert cliargs_deferred_get('foo', shallowcopy=True)() is not test_cliargs.get('foo')

    test_set = {'foo', 'bar'}
    test_cliargs = CLIArgs(test_set)
    assert cliargs_deferred_get('foo')() is test_cliargs.get('foo')

    assert cliargs

# Generated at 2022-06-12 21:22:00.291221
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert cliargs_deferred_get('test', default=1)() == 1
    CLIARGS = CLIArgs({'test': 1})
    assert cliargs_deferred_get('test', default=3)() == 1
    assert cliargs_deferred_get('test2', default=3)() == 3
    CLIARGS = CLIArgs({'test': [1], 'test2': [1, 2, 3]})
    assert cliargs_deferred_get('test', default=[1])() == [1]
    assert cliargs_deferred_get('test2', default=[])() == [1, 2, 3]
    assert cliargs_deferred_get('test3', default={})() == {}

# Generated at 2022-06-12 21:22:11.883902
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class MyCLIArgs(CLIArgs):
        def __init__(self, args):
            super(MyCLIArgs, self).__init__(args)
            self.called_get = False

        def get(self, key, default=None):
            '''Track when we're called'''
            self.called_get = True
            return super(MyCLIArgs, self).get(key)

        def __setitem__(self, key, value):
            self.called_get = False
            super(MyCLIArgs, self).__setitem__(key, value)

    # Test that calling with a global value set
    CLIARGS = MyCLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')(), 'bar'

    # Test that calling with a global value un

# Generated at 2022-06-12 21:22:21.705812
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get function.

    The cliargs_deferred_get function is a closure that wraps usage of a dict.  These tests
    validate that when it's called it behaves like a dict.
    """
    import copy

    # we have to create a dummy CLIArgs class to mock out the _cli_args functionality
    class _TestCLIArgs(CLIArgs):
        """Dummy CLIArgs class"""
        def __init__(self, parser, args):
            # self._cli_args is the dict we're testing against
            self._cli_args = copy.deepcopy(args)
            super(_TestCLIArgs, self).__init__(parser)

    # create a getter that uses the dummy CLIArgs class

# Generated at 2022-06-12 21:22:31.155756
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    assert cliargs_deferred_get('missing')() == None
    # If a key is missing, then it will return the default value as specified
    CLIARGS['foo'] = 'bar'
    assert cliargs_deferred_get('foo', default='missing')() == 'bar'
    assert cliargs_deferred_get('missing', default='bar')() == 'bar'
    # Make sure it's a shallow copy, so if the underlying value changes
    # the value we get is not
    original = {'one': 1, 'two': 2}
    CLIARGS['original'] = original
    shallow_copied = cliargs_deferred_get('original', shallowcopy=True)()
    assert shallow_copied == original
    original['three'] = 3
    assert shallow_copied != original
    assert shallow_cop

# Generated at 2022-06-12 21:22:40.216464
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # No copy
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    # Shallow copy
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    CLIARGS = CLIArgs({'foo': {'fie': 'baz'}})
    assert cliargs_deferred_get('foo', shallowcopy=True)() == {'fie': 'baz'}

# Generated at 2022-06-12 21:22:48.845302
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test cliargs_deferred_get function

    This function is not bound to ``CLIARGS`` directly to support ``CLIARGS``
    being replaced with a singleton
    """
    from ansible.module_utils.common._collections_compat import Mapping
    import copy
    import inspect
    import types
    import warnings

    # Helper function to validate the function signature

# Generated at 2022-06-12 21:23:00.853002
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'var1': 1, 'var2': 2, 'var3': [1, 2]})

    assert cliargs_deferred_get('var1')() == 1
    assert cliargs_deferred_get('var2')() == 2
    assert cliargs_deferred_get('var3')() == [1, 2]

    assert cliargs_deferred_get('var3', shallowcopy=True)() == [1, 2]
    assert cliargs_deferred_get('var3', default=['var3'], shallowcopy=True)() == ['var3']
    assert cliargs_deferred_get('var3', shallowcopy=True)() == [1, 2]


# Generated at 2022-06-12 21:23:08.337553
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_value = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    class TestClass(object):
        cli_args = cliargs_deferred_get('key1')
        cli_args_copy = cliargs_deferred_get('key1', shallowcopy=True)
        cli_args_default = cliargs_deferred_get('key4', default='default value')
        cli_args_default_copy = cliargs_deferred_get('key4', default='default value', shallowcopy=True)

    # Test value before global context is initialized
    test_obj = TestClass()
    assert test_obj.cli_args == 'value1'
    assert test_obj.cli_args_copy == 'value1'
    assert test_

# Generated at 2022-06-12 21:23:18.042033
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test for function cliargs_deferred_get"""
    args = {'foo_bar': 'bazz', 'bleep': 'bloop', 'bleep2': ['a', 'b', 'c'], 'bleep3': {'a': 'b'}, 'bleep4': {'a', 'b', 'c'}}
    # Test normal access
    _init_global_context(args)
    assert CLIARGS['foo_bar'] == 'bazz'
    assert cliargs_deferred_get('foo_bar') == 'bazz'
    assert cliargs_deferred_get('bleep2')[1] == 'b'
    assert cliargs_deferred_get('bleep3')['a'] == 'b'

# Generated at 2022-06-12 21:23:26.722006
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the functionality of ``cliargs_deferred_get``"""
    global CLIARGS
    assert callable(cliargs_deferred_get('test-key'))
    assert callable(cliargs_deferred_get('test-key', shallowcopy=True))
    cli_args = {'test-key': 'test-value'}
    _init_global_context(cli_args)
    assert cliargs_deferred_get('test-key')() == 'test-value'
    assert cliargs_deferred_get('test-key', shallowcopy=True)() == 'test-value'
    assert cliargs_deferred_get('unknown-key')() is None
    assert cliargs_deferred_get('unknown-key', 'default-value')() == 'default-value'
    cli_

# Generated at 2022-06-12 21:24:16.455735
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test logic of cliargs_deferred_get function

    This also tests that ``CLIARGS`` and ``cliargs_deferred_get`` play nice together
    """
    # Test that it works with empty CLIARGS
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'
    assert cliargs_deferred_get('foo', default=[1,2,3])() == [1,2,3]
    assert cliargs_deferred_get('foo', default='bar', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('foo', default=[1,2,3], shallowcopy=True)() == [1,2,3]

    # Test that it works with CLIARGS set

# Generated at 2022-06-12 21:24:22.225290
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS['a'] = 'b'
    assert cliargs_deferred_get('a')(), 'b'
    CLIARGS.set_default(('a',), 'c')
    assert cliargs_deferred_get('a', default='c')(), 'b'
    assert cliargs_deferred_get('b', default='c')(), 'c'

# Generated at 2022-06-12 21:24:33.781133
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'v': 'v'})
    assert cliargs_deferred_get('v')() == 'v'

    CLIARGS = GlobalCLIArgs.from_options({'v': 'v'})
    assert cliargs_deferred_get('v')() == 'v'
    assert cliargs_deferred_get('v', shallowcopy=True)() == 'v'
    assert cliargs_deferred_get('v', default='x')() == 'v'
    assert cliargs_deferred_get('v', default='x', shallowcopy=True)() == 'v'
    assert cliargs_deferred_get('x')() is None
    assert cliargs_deferred_get('x', shallowcopy=True)() is None
    assert cl

# Generated at 2022-06-12 21:24:36.900633
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Minimal test just to check the function's basic functionality
    CLIARGS.update({'key': 'val'})
    assert cliargs_deferred_get('key')() == 'val'

# Generated at 2022-06-12 21:24:47.077143
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import copy
    import pytest

    global CLIARGS
    CLIARGS = CLIArgs({'a': [1, 2, 3], 'b': {'b1': 'b1val'}, 'c': {'c1': 'a', 'c2': 'b'}})

    def check_mutable_copy(copy_fn):
        for key in ('a', 'b', 'c'):
            orig_val = CLIARGS[key]
            # pytest.approx requires numpy 1.15+.  On older:
            #          def check_mutable_copy(copy_fn):
            #              for key in ('a', 'b', 'c'):
            #                  orig_val = CLIARGS[key]
            #                  copy_val = copy_fn()
            #                  assert id(orig_val) == id

# Generated at 2022-06-12 21:24:57.949256
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # set up test object and some defaults
    CLIARGS._opts = {'b': [1, 2, 3], 'd': {'e': 4, 'f': 5}}
    CLIARGS._opts_not_bool = {'a': [4, 5, 6], 'c': {'g': 6, 'h': 7}}
    CLIARGS._aliases = {'a': ['b']}
