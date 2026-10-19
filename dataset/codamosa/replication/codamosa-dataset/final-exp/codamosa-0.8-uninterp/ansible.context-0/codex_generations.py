

# Generated at 2022-06-12 21:15:07.601290
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict

    CLIARGS._ansible_options = ImmutableDict({'foo': 'bar'})
    get_foo = cliargs_deferred_get('foo')
    assert get_foo() == 'bar'

    get_non_existing = cliargs_deferred_get('non-existing')
    assert get_non_existing() is None

    get_non_existing_with_default = cliargs_deferred_get('non-existing', default='default')
    assert get_non_existing_with_default() == 'default'


# Generated at 2022-06-12 21:15:13.237991
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = CLIArgs({'fact_caching': 'jsonfile', 'fact_caching_connection': '/etc/ansible/facts',
                        'test': [1, 2, 3], 'test2': {'a': 10}})
    global CLIARGS
    CLIARGS = cli_args
    assert CLIARGS.get('fact_caching') == cliargs_deferred_get('fact_caching')()
    assert CLIARGS.get('fact_caching') == cliargs_deferred_get('fact_caching', shallowcopy=True)()
    assert CLIARGS.get('test') == cliargs_deferred_get('test')()
    assert CLIARGS.get('test') != cliargs_deferred_get('test', shallowcopy=True)()

# Generated at 2022-06-12 21:15:18.904884
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test function cliargs_deferred_get"""
    _init_global_context(dict(A='A', B='B', C=['C']))
    assert cliargs_deferred_get('A')() == 'A'
    assert cliargs_deferred_get('Z')() is None
    assert cliargs_deferred_get('Z', default='Z')() == 'Z'
    assert cliargs_deferred_get('C')() == ['C']
    assert cliargs_deferred_get('C', shallowcopy=True)() == ['C']

# Generated at 2022-06-12 21:15:29.861522
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test the cliargs_deferred_get closure"""
    # pylint: disable=missing-docstring
    CLIARGS.update(dict(
        somesequence=['test1', 'test2'],
        somedict=dict(test1=42),
        sometuple=('test1', 'test2'),
        somelist=['test1', 'test2'],
        someset=set(['test1', 'test2']),
    ))

# Generated at 2022-06-12 21:15:37.075404
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar', 'baz': ['qux']})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz', default=None)() == ['qux']
    copy_baz = cliargs_deferred_get('baz', shallowcopy=True)()
    assert copy_baz == ['qux']
    copy_baz[-1] = 'quux'
    assert CLIARGS['baz'] == ['qux']
    assert cliargs_deferred_get('quux')() is None

# Generated at 2022-06-12 21:15:48.427081
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_key(value):
        inner = cliargs_deferred_get(key=value)
        inner.__name__ = "<deferred_accessor>"
        return inner

    value = '123'
    cliargs_deferred_get.value = '123'
    assert test_key('value').__name__ == '<deferred_accessor>'
    assert test_key('ANSIBLE_CALLABLE_WHITELIST').__name__ == '<deferred_accessor>'
    assert test_key('ANSIBLE_PRIVILEGE_ESCALATION').__name__ == '<deferred_accessor>'
    assert test_key('ANSIBLE_PRIVILEGE_ESCALATION').__name__ == '<deferred_accessor>'

# Generated at 2022-06-12 21:15:59.270982
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    import pytest
    cli_args = dict(test_key=dict(test_key_key=1234))
    _init_global_context(cli_args)
    assert cliargs_deferred_get('test_key') == {'test_key_key' : 1234}
    assert cliargs_deferred_get('test_key', shallowcopy=True) != {'test_key_key' : 1234}
    assert cliargs_deferred_get('test_key', shallowcopy=True) == {'test_key_key' : 1234}
    assert cliargs_deferred_get('test_key_key') == 1234
    assert cliargs_deferred_get('test_key_key', shallowcopy=True) == 1234

# Generated at 2022-06-12 21:16:05.168175
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'a': 1, 'b': [1, 2, 3], 'c': {'d': 1}})
    dg = cliargs_deferred_get

    assert dg('a')() == 1
    assert dg('a', default=True)() == 1
    assert dg('z')() is None
    assert dg('z', default=True)() is True

    assert dg('b')() == [1, 2, 3]
    assert dg('b', default=True)() == [1, 2, 3]
    assert dg('b', shallowcopy=True)() == [1, 2, 3]

    assert dg('c')() == {'d': 1}

# Generated at 2022-06-12 21:16:16.172628
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from nose.plugins.attrib import attr
    from ansible.module_utils.six import PY2

    @attr('unit')
    def test_get_by_default():
        # Verify that the get function with no arguments works
        global CLIARGS
        CLIARGS = CLIArgs({'test_key': 'test_value'})
        assert 'test_value' == cliargs_deferred_get('test_key')()

    @attr('unit')
    def test_get_default_value():
        # Verify that the get function with just a default works
        global CLIARGS
        CLIARGS = CLIArgs({'test_key': 'test_value'})
        assert 'test_value' == cliargs_deferred_get('test_key', 'default_value')()


# Generated at 2022-06-12 21:16:25.179689
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    expected = {'some': 'value'}
    CLIARGS.some = expected
    assert cliargs_deferred_get('some')() is expected
    assert cliargs_deferred_get('some', shallowcopy=True)() is expected
    assert cliargs_deferred_get('some', shallowcopy=True)() == expected
    CLIARGS.some = list(expected.keys())
    assert cliargs_deferred_get('some')() == [key for key in expected.keys()]
    assert cliargs_deferred_get('some', shallowcopy=True)() == [key for key in expected.keys()]
    assert cliargs_deferred_get('some', shallowcopy=True)() == [key for key in expected.keys()]

# Generated at 2022-06-12 21:16:40.580852
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    cli_args = {'vault_password_file': 'foo', 'tags': ['bar'], 'something': {'dict': 'value'}}
    _init_global_context(cli_args)
    result = cliargs_deferred_get('no_key', 'default')
    assert result() == 'default'
    result = cliargs_deferred_get('vault_password_file', 'default')
    assert result() == 'foo'
    result = cliargs_deferred_get('tags', 'default')
    assert result() == ['bar']
    result = cliargs_deferred_get('something')
    assert result() == {'dict': 'value'}

# Generated at 2022-06-12 21:16:47.168384
# Unit test for function cliargs_deferred_get

# Generated at 2022-06-12 21:16:54.052005
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() == None
    assert cliargs_deferred_get('bar', 'baz')() == 'baz'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)().startswith('bar')

# Generated at 2022-06-12 21:17:05.669175
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class TestCLIArgs(dict):
        def __init__(self, *args, **kwargs):
            super(TestCLIArgs, self).__init__(*args, **kwargs)
            self._validated = True

    # Test non-defaults
    for cli_args in (dict(foo='bar'), TestCLIArgs(foo='bar')):
        get = cliargs_deferred_get('foo', default='default')
        assert get() == 'bar'

        get = cliargs_deferred_get('bar', default='default', shallowcopy=False)
        try:
            assert get() == 'default'
        except:
            pytest.fail("non-default test failed for cli_args: {}".format(str(cli_args)))


# Generated at 2022-06-12 21:17:16.063330
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global_args = {
        'key2': 3,
        'key4': ['a', 'b', 'c'],
        'key5': {'a': 1, 'b': 2, 'c': 3},
    }
    CLIARGS.options = global_args


# Generated at 2022-06-12 21:17:26.780828
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.six import PY3

    CLIARGS['a'] = '1'
    a = cliargs_deferred_get('a')
    assert a == '1'
    assert a() == '1'

    CLIARGS['a'] = 2
    a = cliargs_deferred_get('a')
    assert a == 2
    assert a() == 2

    CLIARGS['a'] = {'a': 1}
    a = cliargs_deferred_get('a')
    assert a == CLIARGS['a']
    if PY3:
        # Note: References on Py2 and copies on Py3
        assert a() is not CLIARGS['a']
        assert a() == CLIARGS['a']

# Generated at 2022-06-12 21:17:38.265822
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS._opts = {'foo': 'bar'}
    assert cliargs_deferred_get('foo')() == 'bar'
    CLIARGS._opts = {'foo': [1, 2, 3]}
    assert cliargs_deferred_get('foo', shallowcopy=True)() == [1, 2, 3]
    assert cliargs_deferred_get('foo', shallowcopy=False)() == [1, 2, 3]
    result = cliargs_deferred_get('foo', shallowcopy=True)()
    assert result == [1, 2, 3]
    result.pop()
    assert CLIARGS._opts['foo'] == [1, 2, 3]
    result = cliargs_deferred_get('foo', shallowcopy=False)()

# Generated at 2022-06-12 21:17:45.413026
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('bar')() is None
    assert cliargs_deferred_get('bar', default='some default')() == 'some default'
    assert cliargs_deferred_get('bar', default=['some default'])() == ['some default']
    assert cliargs_deferred_get('bar', default='some default', shallowcopy=True)() == 'some default'
    assert cliargs_deferred_get('bar', default=['some default'], shallowcopy=True)() == ['some default']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert cliargs_deferred_

# Generated at 2022-06-12 21:17:56.390098
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Given we have not parsed the command line arguments yet
    global CLIARGS
    CLIARGS = CLIArgs({})

    # When we retrieve the test_arg
    get_test_arg = cliargs_deferred_get('test_arg', 'test')
    # And we retrieve the test_arg_2
    get_test_arg_2 = cliargs_deferred_get(
        'test_arg_2', 'test_2', shallowcopy=True)

    # Then get_test_arg returns the provided default
    assert get_test_arg() == 'test'
    # And get_test_arg_2 returns the provided default
    assert get_test_arg_2() == 'test_2'

    # When we initialize the global context

# Generated at 2022-06-12 21:18:02.544888
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIARGS.from_options({})
    # Should return default when CLIARGS has no value
    default = ['foo']
    val = cliargs_deferred_get('nothing', default)()
    assert val is default
    # Should return the nested value based on a passed in string key
    CLIARGS = CLIARGS.from_options({'pipelining': {'enabled': True}})
    assert cliargs_deferred_get('pipelining.enabled')() is True
    # Should return the nested value based on a passed in list of keys
    CLIARGS = CLIARGS.from_options({'pipelining': {'enabled': True}})
    assert cliargs_deferred_get(['pipelining', 'enabled'])() is True
    # Should return the default

# Generated at 2022-06-12 21:18:22.282813
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeCliArgs(dict):
        def __getattr__(self, *args):
            return self.get(*args)

    global CLIARGS
    CLIARGS = FakeCliArgs({'key': 'value'})
    assert 'value' == cliargs_deferred_get('key')()

    global CLIARGS
    CLIARGS = FakeCliArgs({'key': [1,2,3]})
    assert [1,2,3] == cliargs_deferred_get('key')()
    assert [1,2,3] == cliargs_deferred_get('key', shallowcopy=True)()

# Generated at 2022-06-12 21:18:28.255973
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    assert not CLIARGS
    assert cliargs_deferred_get('foo')() is None
    CLIARGS = GlobalCLIArgs({'foo': 'bar', 'baz': 'quux'})
    assert CLIARGS
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('baz')() == 'quux'
    assert cliargs_deferred_get('blam')() is None

# Generated at 2022-06-12 21:18:39.108565
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for cliargs_deferred_get"""
    def check_default(key, default, expected):
        """Helper function to check that cliargs_deferred_get returns the correct default"""
        actual = cliargs_deferred_get('not_' + key, default)()
        assert actual == expected, '{} should be {}, got {}'.format(key, expected, actual)

    check_default('none', None, None)
    check_default('int', 2, 2)
    check_default('list', [], [])
    check_default('list_pop', [1, 2, 3], [1, 2, 3])
    assert cliargs_deferred_get('list_pop', [1, 2, 3], shallowcopy=True)() == [1, 2, 3]
    assert cliargs_

# Generated at 2022-06-12 21:18:48.612024
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs({'foo': 'foo', 'bar': 'bar'})
    assert cliargs_deferred_get('foo')() == 'foo'
    assert cliargs_deferred_get('bar')() == 'bar'
    assert cliargs_deferred_get('baz', default='baz')() == 'baz'
    CLIARGS = CLIArgs({'foo': 'override foo', 'bar': ['bar'], 'baz': {'baz': 'baz'}})
    assert cliargs_deferred_get('foo')() == 'override foo'
    assert cliargs_deferred_get('bar')() == ['bar']

# Generated at 2022-06-12 21:18:59.733141
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from collections import namedtuple
    from unittest import TestCase

    class TestCliargsDeferredGet(TestCase):
        def test_cliargs_deferred_get(self):
            class Args:
                one = 1
                two = 2
                three = 3
            class CLIARGS:
                def get(self, key, default):
                    return getattr(Args(), key)

            self.assertEqual(cliargs_deferred_get('one')(), 1)
            self.assertEqual(cliargs_deferred_get('two')(), 2)
            self.assertEqual(cliargs_deferred_get('three')(), 3)

            global CLIARGS
            original_CLIARGS = CLIARGS

            CLIARGS = namedtuple('CLIARGS', [])()._asdict

# Generated at 2022-06-12 21:19:11.074061
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test with normal int
    my_int = cliargs_deferred_get('intval', default=1)
    assert callable(my_int)
    CLIARGS = CLIArgs({'intval': 2})
    assert my_int() == 2

    # Test with int copy
    my_int = cliargs_deferred_get('intval', default=1, shallowcopy=True)
    CLIARGS = CLIArgs({'intval': 2})
    assert my_int() == 2

    # Test with normal list
    my_list = cliargs_deferred_get('listval', default=[1])
    assert callable(my_list)
    CLIARGS = CLIArgs({'listval': [2]})
    assert my_list() == [2]

    # Test with list copy
    my_list

# Generated at 2022-06-12 21:19:17.677286
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test = [{'default':cliargs_deferred_get('default')}]
    _init_global_context({'default':5})
    assert test[0]['default']() == 5

    _init_global_context({'not_default':100})
    assert test[0]['default']() == 100

    _init_global_context({'not_default':100})
    assert test[0]['default']() == 100

    test = [{'default':cliargs_deferred_get('not_default', 5)}]
    _init_global_context({'not_default':100})
    assert test[0]['default']() == 100

# Generated at 2022-06-12 21:19:26.497441
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Test the case where CLIARGS is replaced globally by a mock object
    original = CLIARGS.copy()
    key = 'test_key'
    value = 'test_value'
    mock = {key: value}
    global CLIARGS
    CLIARGS = CLIArgs(mock)
    assert cliargs_deferred_get(key)() == value
    assert cliargs_deferred_get('no_key')() is None
    assert cliargs_deferred_get('no_key', default='no_value')() == 'no_value'
    CLIARGS = original

    # Test the case where CLIARGS is not replaced and we get a closure over the original object
    original = CLIARGS.copy()
    mock = {key: value}
    cliargs_deferred_get_mock = cl

# Generated at 2022-06-12 21:19:37.992421
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    This is not a particularly good unit test since we are relying on GlobalCLIArgs to be
    bound to CLIARGS and for it to return the correct value for get.  But I need something
    that shows that I am not returning the dictionary itself.

    Also, it relies on the ``MutableSequence`` type being a type.  But I'm not going to pull
    all the code in to make it a callable just for the unit test.
    """
    CLIARGS = GlobalCLIArgs.from_options(dict(a=3, b=dict(c=[1, 2, 3]), d=True))
    assert cliargs_deferred_get('a')() == 3

# Generated at 2022-06-12 21:19:45.375202
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Make sure we get the default value
    global CLIARGS
    CLIARGS = CLIArgs({})
    assert cliargs_deferred_get('somekey', 'someval')() == 'someval'

    # Make sure we get a value from the CLIARGS object
    CLIARGS = CLIArgs({'somekey': 'someval'})
    assert cliargs_deferred_get('somekey', 'ignored')() == 'someval'

    # Make sure that lists and dicts are shallow copied (not shared)
    CLIARGS = CLIArgs({'somekey': ['someval']})
    deferred = cliargs_deferred_get('somekey', shallowcopy=True)()
    assert type(deferred) is list
    deferred.append('someotherval')
    assert CLIARGS.get('somekey') != deferred

# Generated at 2022-06-12 21:20:19.135505
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'testkey': 'testvalue'})
    value = cliargs_deferred_get('testkey')()
    assert value == 'testvalue'

    CLIARGS = CLIArgs({'testkey': 'testvalue'})
    value = cliargs_deferred_get('testkey', default=None)()
    assert value == 'testvalue'

    CLIARGS = CLIArgs({'testkey': 'testvalue'})
    value = cliargs_deferred_get('missingkey', default=None)()
    assert value is None

    CLIARGS = CLIArgs({'testkey': 'testvalue'})
    value = cliargs_deferred_get('testkey', default='defaultvalue')()
    assert value == 'testvalue'

    CLIARGS = CLIArgs

# Generated at 2022-06-12 21:20:23.597662
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Set up a mock global context
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = CLIArgs({'prefixed': 'value', 'unprefixed': 'value'})

    # Now execute the tests
    # Do nothing with the value, just return it
    dg = cliargs_deferred_get('unprefixed')
    assert dg() == 'value'

    # Slice a list
    CLIARGS['unprefixed'] = ['a', 'b', 'c']
    dg = cliargs_deferred_get('unprefixed', shallowcopy=True)
    value = dg()
    assert value == ['a', 'b', 'c']
    assert value is not CLIARGS['unprefixed']  # The copy should produce a new object

    # Copy a dict
    CLI

# Generated at 2022-06-12 21:20:31.752514
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    # set up default value
    default = {'x': 'y'}
    # set up non-shallowcopy test
    global_value = {'a': 'b'}
    CLIARGS[default.keys()[0]] = global_value
    assert cliargs_deferred_get(default.keys()[0], default)() == global_value
    # set up shallowcopy test
    global_value = {'a': 'b'}
    CLIARGS[default.keys()[0]] = global_value
    assert cliargs_deferred_get(default.keys()[0], default, shallowcopy=True)() != global_value
    # set up unset test
    CLIARGS.pop(default.keys()[0], None)

# Generated at 2022-06-12 21:20:40.963844
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({'testlist': ['testlist0'],
                       'testdict': {'testkey': 'testvalue'},
                       'testset': ['testset0']})
    # Test getting a list value
    test_var = cliargs_deferred_get('testlist')
    test_var()[0] = 'testlist1'
    assert CLIARGS.get('testlist') == ['testlist0']
    test_var = cliargs_deferred_get('testlist', shallowcopy=True)
    test_var()[0] = 'testlist1'
    assert CLIARGS.get('testlist') == ['testlist1']
    test_var = cliargs_deferred_get('testlist', default=['testlist2'])
    assert test_var

# Generated at 2022-06-12 21:20:50.856047
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    test_value = [b'foo']
    cli_args = {'test_key': test_value}
    _init_global_context(cli_args)
    from ansible.module_utils.common.parameters import FieldAttribute
    test_attr = FieldAttribute(None, None, defer_get=cliargs_deferred_get('test_key'))
    assert test_value is test_attr()
    assert test_attr() is test_attr()
    test_attr2 = FieldAttribute(None, None, defer_get=cliargs_deferred_get('test_key', shallowcopy=True))
    assert test_attr2() is not test_attr2()

# Generated at 2022-06-12 21:20:59.944535
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class opt:
        foo = cliargs_deferred_get('foo')
        bar = cliargs_deferred_get('bar')
        baz = cliargs_deferred_get('baz', default=dict())
        boo = cliargs_deferred_get('boo', default=list())
        bam = cliargs_deferred_get('bam', shallowcopy=True)
        bop = cliargs_deferred_get('bop', shallowcopy=True)
        bap = cliargs_deferred_get('bap', shallowcopy=True)

    class a:
        foo = 1
        bar = None
        baz = {}
        boo = []
        bam = [1, 2]
        bop = {'foo': 1}
        bap = 'foo'


# Generated at 2022-06-12 21:21:09.622955
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Defer getting a value from special option
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.six import string_types
    from ansible.module_utils import basic
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.remote_tmp import RemoteTmp
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.splitter import parse_kv
    from ansible.utils.context_objects import RemoteTmpManager

# Generated at 2022-06-12 21:21:20.435213
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    CLIARGS = CLIArgs({})
    key, value = 'key', 'value'
    assert cliargs_deferred_get(key)() == None
    CLIARGS = CLIArgs({key: value})
    assert cliargs_deferred_get(key)() == value
    CLIARGS = CLIArgs({key: value})
    assert cliargs_deferred_get(key, shallowcopy=True)() == value
    CLIARGS = CLIArgs({key: [value]})
    assert cliargs_deferred_get(key, shallowcopy=True)() == [value]
    assert cliargs_deferred_get(key, shallowcopy=True)() is not [value]
    CLIARGS = CLIArgs({key: {value: 'value2'}})
    assert cliargs

# Generated at 2022-06-12 21:21:31.947895
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Simple operation
    def test_simple():
        global CLIARGS
        CLIARGS.data = {
            'a': 'b',
        }
        assert cliargs_deferred_get('a')(), 'b'
        assert cliargs_deferred_get('b', 'c')(), 'c'

    # Simple operation with shallow copy
    def test_shallow_copy():
        global CLIARGS
        CLIARGS.data = {
            'a': 'b',
            'c': ['d', 'e', 'f'],
            'g': {'k': 'l'},
        }
        assert cliargs_deferred_get('a', shallowcopy=True)(), 'b'
        assert cliargs_deferred_get('b', 'c', shallowcopy=True)(), 'c'

# Generated at 2022-06-12 21:21:39.169747
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    get = cliargs_deferred_get
    gcda = _init_global_context
    # pylint: disable=C0103
    # TODO:  Change this to be pytest based unit tests
    assert get
    # Ensure defaults work
    gcda({})
    assert get('vault_password_file') == get('vault_password_file')() == ''

    # Ensure we can see values in the global cliargs object
    gcda({'vault_password_file': '/path/to/password'})
    assert get('vault_password_file')() == '/path/to/password'

    # Ensure we can override global cliargs defaults
    assert get('vault_password_file', default='default')() == '/path/to/password'

    # Ensure shallowcopy works
    # ..

# Generated at 2022-06-12 21:22:10.884919
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Unit test for function cliargs_deferred_get

    Since this function is almost entirely about closures, it'd be difficult to
    write a proper unit test for it
    """
    deferred = cliargs_deferred_get('test_key', 'test_value')
    assert deferred() == 'test_value'
    CLIARGS.update({'test_key': 'new_value'})
    assert deferred() == 'new_value'
    assert deferred() is not 'new_value'

# Generated at 2022-06-12 21:22:19.779281
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    """Test to make sure that ``cliargs_deferred_get`` behaves correctly"""
    # First make sure it works without the CLIARGS being replaced
    _init_global_context({'foo': 'bar'})
    assert cliargs_deferred_get('foo')() == 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'

    # Make sure it works when CLIARGS is replaced
    global CLIARGS
    CLIARGS = CLIArgs({'foo': 'baz'})
    assert cliargs_deferred_get('foo')() == 'baz'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'baz'

# Generated at 2022-06-12 21:22:27.259635
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import ImmutableDict
    GlobalCLIArgs.CLIARGS = GlobalCLIArgs(ImmutableDict({'connection_plugins': ['/path/one', '/path/two']}))
    assert cliargs_deferred_get('connection_plugins', shallowcopy=True)() == ['/path/one', '/path/two']
    assert cliargs_deferred_get('connection_plugins', shallowcopy=True)() != GlobalCLIArgs.CLIARGS.connection_plugins
    GlobalCLIArgs.CLIARGS = GlobalCLIArgs(ImmutableDict({'connection_plugins': ['path/one', 'path/two']}))

# Generated at 2022-06-12 21:22:39.007597
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def check_deferred_value(key, default, shallowcopy):
        # This function calls ``cliargs_deferred_get`` so that the reference to ``CLIARGS`` will
        # be correct when the lambda is called.  Since the lambda is called later, the ``CLIARGS``
        # will be whatever it is at the time the lambda is called.
        deferred = cliargs_deferred_get(key, default, shallowcopy)

        # Call the first time with the ``CLIARGS`` as it is now.  It should return the default value
        # since there is no key defined
        first_value = deferred()
        assert CLIARGS == GlobalCLIArgs({})
        assert first_value == default

        # Add the key with a value to the ``CLIARGS`` and then call again
        CLIARGS[key]

# Generated at 2022-06-12 21:22:45.919556
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS

    CLIARGS = CLIArgs({})

    cliargs_deferred_get('test_key')()
    assert CLIARGS.get('test_key') == None

    cliargs_deferred_get('test_key', default='test_value')()
    assert CLIARGS.get('test_key') == 'test_value'

    CLIARGS = CLIArgs({'test_key': 'test_value'})
    cliargs_deferred_get('test_key')()
    assert CLIARGS.get('test_key') == 'test_value'



# Generated at 2022-06-12 21:22:57.049766
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    def test_func(value):
        inner = cliargs_deferred_get('test', value)
        return inner()

    CLIARGS['test'] = [1, 2, 3]
    assert [1, 2, 3] == test_func([4, 5, 6])
    assert [1, 2, 3] != test_func([4, 5, 6])

    CLIARGS['test'] = [1, 2, 3]
    assert [1, 2, 3] == test_func([4, 5, 6])
    assert [1, 2, 3] == test_func([4, 5, 6])

    CLIARGS['test'] = 'abc'
    assert 'abc' == test_func('def')
    assert 'abc' == test_func('def')


# Generated at 2022-06-12 21:23:06.420655
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    key = 'key'
    default = 'default'
    expected = 'expected'
    returned = 'returned'
    shallowcopy = 'shallowcopy'

    def check_value(actual, expected, shallowcopy, msg):
        if shallowcopy is not None:
            assert actual is not expected
        else:
            assert actual is expected
        assert actual == expected

    # Test that it returns the defaults if the cliargs are not yet available
    cliargs_deferred_get(key, default, shallowcopy)().should.equal(default)
    cliargs_deferred_get(key, returned, shallowcopy)().should.equal(returned)

    # Test that it returns actual values from the CLIARGS
    # Shallow copy is only shallow
    test_dict = {'key': 'value'}

# Generated at 2022-06-12 21:23:15.799611
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    from ansible.module_utils.common.collections import Mapping, Set
    from ansible.module_utils.common._collections_compat import Sequence

    def assert_shallowcopy(n, expected):
        assert cliargs_deferred_get(n, shallowcopy=True)() == expected

    def assert_no_shallowcopy(n, expected):
        assert cliargs_deferred_get(n, shallowcopy=False)() == expected

    cli_args = {
        "test1": "foo",
        "test2": ["bar"],
        "test3": dict(a=1, b=2),
        "test4": set([1, 2, 3]),
        "test5": None
    }
    global CLIARGS

# Generated at 2022-06-12 21:23:25.327825
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # Instantiate cliargs_deferred_get
    def_value = cliargs_deferred_get('foo')
    def_copy = cliargs_deferred_get('foo', shallowcopy=True)

    # Create CLIARGS instance and populate with a foo
    test_cliargs = CLIArgs({'foo': 'bar'})

    # Simply call def_value and make sure we get the expected result
    assert def_value() == 'bar'
    assert def_copy() == 'bar'

    # Replace CLIARGS instance
    global CLIARGS
    cliargs_bak = CLIARGS
    CLIARGS = test_cliargs

    # Make sure that def_value still returns the expected result
    assert def_value() == 'bar'
    assert def_copy() == 'bar'

    # Replace foo with a list

# Generated at 2022-06-12 21:23:34.538769
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    global CLIARGS
    args = {}
    _init_global_context(args)
    # Make sure it returns None
    assert cliargs_deferred_get('foo')() is None
    assert cliargs_deferred_get('foo', default='bar')() == 'bar'
    # Make sure it can be shallow copied
    args['foo'] = 'bar'
    assert cliargs_deferred_get('foo', shallowcopy=True)() == 'bar'
    assert id(args['foo']) != id(cliargs_deferred_get('foo', shallowcopy=True)())
    args['foo'] = ['bar']
    assert cliargs_deferred_get('foo', shallowcopy=True)() == ['bar']

# Generated at 2022-06-12 21:24:35.695098
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    # pylint: disable=redefined-outer-name
    def cliargs_deferred_get_handler(key, default=None, shallowcopy=False):
        """Pretend this is the cliargs_deferred_get function and return the values the function called with"""
        return key, default, shallowcopy

    class TestCLIArgs(dict):
        """Pretend this is the cliargs object that allows us to use the above function"""
        def __init__(self, *args, **kwargs):
            super(TestCLIArgs, self).__init__(*args, **kwargs)
            self._handler = cliargs_deferred_get_handler

        def get(self, key, default=None):
            return self._handler(key, default=default, shallowcopy=False)


# Generated at 2022-06-12 21:24:46.452811
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    CLIARGS.BAR = 'BAR'
    assert cliargs_deferred_get('FOO')(), None
    assert cliargs_deferred_get('BAR')(), 'BAR'
    CLIARGS.FOO = 'FOO'
    assert cliargs_deferred_get('FOO')(), 'FOO'

    CLIARGS.BAZ = [1, 2, 3, 4]
    assert cliargs_deferred_get('BAZ', shallowcopy=True)(), [1, 2, 3, 4]
    assert cliargs_deferred_get('BAZ', shallowcopy=True)() is not CLIARGS.BAZ
    assert cliargs_deferred_get('BAZ', shallowcopy=False)(), [1, 2, 3, 4]
    assert cliargs_

# Generated at 2022-06-12 21:24:57.747409
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():
    class FakeCLIArgs(dict):
        def __getattr__(self, name):
            value = super(FakeCLIArgs, self).get(name, None)
            if value is None:
                raise AttributeError()
            return value

    expected = ['discover']
    cliargs = FakeCLIArgs()
    cliargs['module_name'] = expected
    assert CLIARGS.get('module_name') is None
    getter = cliargs_deferred_get('module_name')
    assert getter() is None
    global CLIARGS
    old_cliargs = CLIARGS
    CLIARGS = cliargs
    assert CLIARGS.get('module_name') == expected
    assert getter() == expected
    CLIARGS = old_cliargs
    assert getter() is None