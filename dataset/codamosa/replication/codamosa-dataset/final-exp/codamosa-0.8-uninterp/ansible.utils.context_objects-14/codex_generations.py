

# Generated at 2022-06-13 15:59:37.927864
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    testArgs = CLIArgs({'key1': 'value1', 'key2': 'value2'})
    assert testArgs['key1'] == 'value1'
    assert testArgs['key2'] == 'value2'

# Generated at 2022-06-13 15:59:40.961895
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    a = A()
    b = A()
    assert a is b, '_ABCSingleton failed to meet the Singleton criteria'



# Generated at 2022-06-13 15:59:43.507193
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs.from_options(GlobalCLIArgs)
    GlobalCLIArgs.from_options(CLIArgs)



# Generated at 2022-06-13 15:59:46.285041
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert 'ANSIBLE_MODULE_ARGS' in GlobalCLIArgs({'ANSIBLE_MODULE_ARGS': 'test'})



# Generated at 2022-06-13 15:59:49.849295
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(Singleton):
        pass
    class TestABCMeta(ABCMeta):
        pass
    class TestBoth(_ABCSingleton):
        pass

    assert isinstance(TestBoth, Singleton)
    assert isinstance(TestBoth, ABCMeta)

# Generated at 2022-06-13 15:59:54.917942
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    o = GlobalCLIArgs({'a': 'b'})
    assert isinstance(o, CLIArgs)

    o = CLIArgs.from_options(GlobalCLIArgs({'a': 'b'}))
    assert isinstance(o, CLIArgs)

# Generated at 2022-06-13 15:59:59.989296
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    global_value = GlobalCLIArgs
    program_args = [
        '--startup-become-password',
        'some-password',
        '--module-path',
        '/path/to/modules',
        '--become-user',
        'some-user',
        'some-playbook.yml',
    ]
    # Normally this is done at the top of the file, but for unit testing that's a pain, so we do it here instead
    global_value._GlobalCLIArgs__instance = None
    global_value.from_options(global_value._set_options(program_args))
    actual = GlobalCLIArgs.get_instance()

# Generated at 2022-06-13 16:00:03.678530
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    immutable_dict = CLIArgs({'force': True, 'check': False})
    assert immutable_dict.get('force') and not immutable_dict.get('check')



# Generated at 2022-06-13 16:00:11.780893
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test for constructor of class CLIArgs"""
    test_containers = [
        {
            'a': 'b',
            'c': (1, 2, {'subkey': 'subvalue'})
        },
        ['one', 'two', 'three', {'subkey': 'subvalue'}],
        'abcd',
        b'abcd',
        u'abcd',
        (1, 2, {'subkey': 'subvalue'}),
        set(['one', 'two', 'three', {'subkey': 'subvalue'}]),
        frozenset(['one', 'two', 'three', {'subkey': 'subvalue'}])
    ]

    for container in test_containers:
        obj = CLIArgs(container)
        assert obj == container

# Generated at 2022-06-13 16:00:14.992079
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        GlobalCLIArgs({"aa": "aa"})
        assert False, "GlobalCLIArgs should not be instantiated."
    except TypeError:
        pass

# Generated at 2022-06-13 16:00:25.582005
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """CLIArgs should accept a dict and turn it into an immutable dict and children (recursively)"""
    # Create a dict to test
    test_dict = {
        'test_string': 'a string',
        'test_list': ['a', 'list', 'of', {'a': 'string', 'and': 'another'}],
        'test_set': {'set', 'is', 'a', {'hashable': 'object', 'with': 'a string'}},
        'test_tuple': (1, 'a', {'mapping': 'dict', 'in': 'a tuple'}),
        'test_dict': {'a dict': 'mapping', 'items': {'to': 'other', 'items': 'or strings'}}
    }
    # Convert it using CLIArgs
    args = GlobalCLIArgs

# Generated at 2022-06-13 16:00:26.802078
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object, metaclass=_ABCSingleton):
        pass
    class B(A):
        pass



# Generated at 2022-06-13 16:00:34.405443
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import copy
    import sys

    class MockOptions(object):
        pass

    mock_options = MockOptions()
    mock_options.always_collect_facts = False
    mock_options.ask_vault_pass = False
    mock_options.ask_sudo_pass = False
    mock_options.ask_su_pass = False
    mock_options.ask_pass = False
    mock_options.become = False
    mock_options.become_ask_pass = False
    mock_options.become_method = 'sudo'
    mock_options.become_user = None
    mock_options.check = False
    mock_options.colors = 256
    mock_options.connection = 'smart'
    mock_options.diff = False
    mock_options.extra_vars = collections.Ordered

# Generated at 2022-06-13 16:00:35.522388
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({1: 1, 2: 2})

# Generated at 2022-06-13 16:00:43.060491
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.config.manager import ConfigManager
    from ansible.utils import CLIARGS
    from ansible.utils.plugin_docs import get_docstring

    # Ensure default ansible.cfg is found
    ConfigManager(['/etc/ansible/ansible.cfg', '~/.ansible.cfg', '/ansible/ansible.cfg'])

    # Ensure all default plugins are found
    get_docstring('')

    # Build an empty Options object since we have to have something to give the GlobalCLIArgs constructor
    empty_options = CLIARGS._build_options_object()
    GlobalCLIArgs(empty_options)

# Generated at 2022-06-13 16:00:46.243023
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--keep-inventory-file', dest='keep_inventory_file',
                        action='store_true')
    args = parser.parse_args()

    arg1 = GlobalCLIArgs.from_options(args)
    assert arg1['keep_inventory_file']
    assert arg1._mutable is False

# Generated at 2022-06-13 16:00:58.443729
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        'b_key': [b'binary', b'string'],
        'u_key': [u'unicode', u'string'],
        's_key': ['str', 'ing'],
        'i_key': [1, 2, 3],
        'f_key': [1.1, 2.2, 3.3],
        't_key': (1, 2, 3),
        'l_key': [1, 2, 3],
        'd_key': {
            u'unicode': u'string',
            'str': 'ing',
            8: 8,
            9.1: 9.1
        },
        'n_key': None,
        'set_key': {1, 2, 3},
    }

# Generated at 2022-06-13 16:01:07.145020
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    try:
        t1 = CLIArgs(None)
    except TypeError as e:
        if str(e) == "'NoneType' object is not iterable":
            print('NoneType object is type checked')
        else:
            raise
    try:
        t2 = CLIArgs(3)
    except TypeError as e:
        if str(e) == "'int' object is not iterable":
            print('Int object is type checked')
        else:
            raise
    try:
        t2 = CLIArgs('')
    except TypeError as e:
        if str(e) == "'str' object is not iterable":
            print('Str object is type checked')
        else:
            raise
    t3 = CLIArgs({'test':3})
    assert t3 == {'test':3}

# Generated at 2022-06-13 16:01:14.991412
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    c = CLIArgs({'a': {'b': {'c': {'d': 1}}}, 'e': 'f'})
    assert isinstance(c, CLIArgs)
    assert isinstance(c, ImmutableDict)
    assert isinstance(c, Mapping)
    assert c == {'a': {'b': {'c': {'d': 1}}}, 'e': 'f'}
    assert c.a.b.c.d == 1

    try:
        c.b
    except AttributeError:
        pass
    else:
        raise RuntimeError('c should not have attribute b')

# Generated at 2022-06-13 16:01:20.377583
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('--some-list', action='append', default=[])

    options, args = parser.parse_known_args(sys.argv[1:])
    args = CLIArgs.from_options(options)

    assert args['debug'] is False
    assert args['some_list'] == []
    assert not isinstance(args['debug'], Mapping)
    assert not isinstance(args['some_list'], Mapping)

# Generated at 2022-06-13 16:01:26.161555
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    parsed_args = {'listtags': True}
    global_args = GlobalCLIArgs(parsed_args)
    assert isinstance(global_args, dict) is True
    assert global_args == parsed_args

# Generated at 2022-06-13 16:01:33.300096
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            self.x = 1

    a = A()
    b = A()
    assert a is b
    assert a.x == b.x == 1

    a.x = 2
    assert a.x == b.x == 2

    class B(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            self.y = 3

    b = B()
    assert a is not b

    class C(A):
       pass

    c = C()
    assert a is c
    assert c.x == 2



# Generated at 2022-06-13 16:01:34.786659
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs({'a': 1, 'b': 2})
    assert obj['b'] == 2

# Generated at 2022-06-13 16:01:45.817241
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Make args both Mutable and Immutable to cause errors if the Singleton pattern doesn't work
    class Args(MutableMapping):
        def __init__(self, *args, **kwargs):
            self._dict = dict(*args, **kwargs)
        def __getitem__(self, key):
            return self._dict[key]
        def __setitem__(self, key, value):
            self._dict[key] = value
        def __delitem__(self, key):
            del self._dict[key]
        def __iter__(self):
            return iter(self._dict)
        def __len__(self):
            return len(self._dict)
    class ArgsI(ImmutableDict):
        def __init__(self, *args, **kwargs):
            self._dict = dict

# Generated at 2022-06-13 16:01:49.530252
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_args = {
        'f': 'test_f_val',
        'k': 'test_k_val',
        'n': None,
        'test_option': 'test_option_val',
        'test_list_option': ['test_option1_val', 'test_option2_val'],
    }
    immutable_args = CLIArgs(test_args)
    assert test_args == immutable_args


_CLI_ARGS = None



# Generated at 2022-06-13 16:02:00.168200
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Create a dummy module object
    class options():
        def __init__(self):
            self.foo = 'foo'
            self.bar = ['bar1', 'bar2']
            self.baz = {'baz1': 'bazone', 'baz2': ['baztwo1', 'baztwo2']}

    # Create an instance of GlobalCLIArgs
    args = GlobalCLIArgs.from_options(options())

    # Make sure args is an instance of CLIArgs and is immutable
    assert isinstance(args, CLIArgs)
    assert isinstance(args, ImmutableDict)

    # See which attributes are in the args
    assert args.keys() == set(['foo', 'bar', 'baz'])

    # Make sure the 'foo' attribute is a string and immutable

# Generated at 2022-06-13 16:02:08.150931
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:02:11.811007
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass
    class Bar(_ABCSingleton):
        pass

    f1 = Foo()
    f2 = Foo()
    b1 = Bar()
    assert f1 is f2
    assert b1 is not f1

# Generated at 2022-06-13 16:02:13.123741
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    assert TestClass() is TestClass()
    assert TestClass().__class__ is TestClass

# Generated at 2022-06-13 16:02:21.202466
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # type: () -> None
    """
    Simple unit test for ensuring the _ABCSingleton constructor doesn't blow up.

    This test is completely unnecessary since the ABCMeta and Singleton metaclasses are still there,
    but we want to catch errors if the _ABCSingleton constructor ever gets modified in a way that
    removes the benefits.
    """

    class MyMetaclass(_ABCSingleton):
        pass

    class MyClass(object):
        __metaclass__ = MyMetaclass

    assert MyClass() is MyClass()

# Generated at 2022-06-13 16:02:30.465869
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    assert isinstance(A(), A)
    assert isinstance(A(), B)
    assert isinstance(B(), A)
    assert isinstance(B(), B)

    a = A()
    b = B()
    aa = A()
    assert a is aa
    # Since a is an A and B, it's id should be the same as b's id
    assert a is b

# Generated at 2022-06-13 16:02:41.681501
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    options = Options(a_int=2, a_dict=dict(a=1, b=2))

    args = CLIArgs.from_options(options)
    assert args.a_int == 2
    assert isinstance(args.a_dict, ImmutableDict)
    assert args.a_dict.a == 1
    assert args.a_dict.b == 2

    # Should complain because dictionary is mutable
    try:
        CLIArgs({'a_dict': options.a_dict})
    except TypeError:
        pass
    else:
        assert False

    # Singleton version
    from ansible.utils.plugin_docs import GlobalCLIArgs
    args = GlobalCLIArgs

# Generated at 2022-06-13 16:02:45.983858
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonObject(object):
        __metaclass__ = _ABCSingleton
        pass

    class SingletonObject2(object):
        __metaclass__ = _ABCSingleton
        pass

    assert SingletonObject() is SingletonObject()
    assert SingletonObject2() is SingletonObject2()
    assert SingletonObject() is not SingletonObject2()

# Generated at 2022-06-13 16:02:55.537432
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    GlobalCLIArgs holds cli arguments as a container. This test creates the
    container and verifies that the constructed object is immutable.

    NOTE: This test is run by the library unittest framework.
    """

    args = GlobalCLIArgs({'a': '1', 'b': {'c': '3', 'd': '4'}})
    assert args == {'a': '1', 'b': {'c': '3', 'd': '4'}}
    try:
        args['e'] = '5'
        # If the assignment above is successful, this message will be printed.
        print("ERROR: GlobalCLIArgs should be immutable but assignment succeeded.")
    except TypeError as e:
        assert "ImmutableDict object does not support item assignment" in str(e)

# Generated at 2022-06-13 16:03:05.194032
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    class TestCLIArgs(unittest.TestCase):
        def setUp(self):
            import argparse

            arg_parser = argparse.ArgumentParser(description="For testing GlobalCLIArgs")
            arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
            arg_parser.add_argument('-v', '--verbose', action='count', dest='verbosity',
                                    help='Set verbosity level')
            # add action to discard 1st param
            class DiscardAction(argparse.Action):
                def __call__(self, parser, namespace, values, option_string=None):
                    # not really needed, but just to show how this has to be set
                    setattr(namespace, self.dest, option_string)
           

# Generated at 2022-06-13 16:03:06.208476
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    A()

# Generated at 2022-06-13 16:03:16.845457
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test the CLIArgs constructor where we can"""
    test_data = {'a': 1, 'b': 2, 'c': 3}
    cliargs = CLIArgs(test_data)

    # Confirm that we have the data we expect
    assert cliargs.data == test_data

    # Confirm that the data is immutable
    try:
        cliargs['a'] = 2
        assert False, 'Changing cliargs should have raised a TypeError'
    except TypeError:
        pass

    # Confirm that we have the expected data where we can
    cliargs = CLIArgs(test_data)

# Generated at 2022-06-13 16:03:20.760244
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    Test()
    Test()

# Test the way the cli args are frozen if the number of arguments to ImmutableDict.__init__ is larger than 5

# Generated at 2022-06-13 16:03:25.459558
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', required=True)
    parser.add_argument('--bar', default='hello')
    parser.add_argument('--baz', default=['a', 'b'])

    args = parser.parse_args(['--foo', 'bar'])
    GlobalCLIArgs.from_options(args)

# Generated at 2022-06-13 16:03:27.456884
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert type(A()) is A()

# Generated at 2022-06-13 16:03:42.831930
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    temp_dict = {
        'a': {'key': 'value'},
        'b': 'Test',
        'c': ['A', 'B'],
        'd': ['C'],
        'e': {
            'a': 1,
            'b': 2,
            'c': [3],
        },
    }

    obj = CLIArgs(temp_dict)

    assert obj['a'] == _make_immutable(temp_dict['a'])
    assert obj['b'] == _make_immutable(temp_dict['b'])
    assert obj['c'] == _make_immutable(temp_dict['c'])
    assert obj['d'] == _make_immutable(temp_dict['d'])
    assert obj['e'] == _make_immutable(temp_dict['e'])



# Generated at 2022-06-13 16:03:45.846258
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Y(metaclass=_ABCSingleton):
        pass
        # Note: It is important that Y have no body.
        # _ABCSingleton calls the metaclass of the class being created.
        # For `class Y(_ABCSingleton)`, this would be _ABCSingleton.
        # That causes an infinite loop.


# Generated at 2022-06-13 16:03:47.956481
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca = GlobalCLIArgs({'foo': True, 'bar': False})
    assert gca['foo']
    assert not gca['bar']

# Generated at 2022-06-13 16:03:59.596475
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonClass1(metaclass=_ABCSingleton):
        pass

    class ABCSingletonClass2(metaclass=_ABCSingleton):
        pass

    assert isinstance(ABCSingletonClass1(), ABCSingletonClass1)
    assert isinstance(ABCSingletonClass2(), ABCSingletonClass2)
    assert not isinstance(ABCSingletonClass1(), ABCSingletonClass2)
    assert not isinstance(ABCSingletonClass2(), ABCSingletonClass1)
    assert type(ABCSingletonClass1()) is type(ABCSingletonClass2())
    assert isinstance(type(ABCSingletonClass1()), ABCSingleton)
    assert isinstance(type(ABCSingletonClass2()), ABCSingleton)

    assert isinstance(ABCSingletonClass1(), ABCSingleton)

# Generated at 2022-06-13 16:04:02.649079
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class TestClass():
        pass

    assert isinstance(TestClass, Singleton)

# Generated at 2022-06-13 16:04:08.117993
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from ansible.utils.sentinal import Sentinel
    from ansible.utils.hashing import secure_hash
    from ansible.module_utils._text import to_bytes

    class HashableTest(object):
        def __init__(self):
            self.value = Sentinel('value')

        def __hash__(self):
            return int(secure_hash(to_bytes(repr(self.value))))

        def __eq__(self, other):
            return self.value == other.value

        def __ne__(self, other):
            return not(self == other)

    class HashableTestABCMeta(HashableTest, metaclass=_ABCSingleton):
        pass

    # these two should be the same canonical object
    one = HashableTestABCMeta()
    two = HashableTestABCMeta()


# Generated at 2022-06-13 16:04:11.929014
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    expected_answer = {'foo': 'bar', 'baz': ('qux', )}
    cli_args = CLIArgs({'foo': 'bar', 'baz': ('qux', )})
    assert cli_args == expected_answer

# Generated at 2022-06-13 16:04:23.633255
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class BaseClass(object):
        pass
    class SubClass(BaseClass):
        pass
    assert issubclass(BaseClass, SubClass)
    assert issubclass(SubClass, BaseClass)
    assert not issubclass(BaseClass, BaseClass)
    assert not issubclass(SubClass, SubClass)

    class MetaBaseClass(object, metaclass=_ABCSingleton):
        pass
    with pytest.raises(TypeError):
        class SubClass(MetaBaseClass):
            pass
    with pytest.raises(TypeError):
        class MetaSubClass(MetaBaseClass, metaclass=_ABCSingleton):
            pass
    assert issubclass(MetaBaseClass, BaseClass)
    assert not issubclass(BaseClass, MetaBaseClass)

# Generated at 2022-06-13 16:04:27.826532
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass
    assert Test() is Test()
    assert Test.__metaclass__.__mro__[0:2] == (Singleton, ABCMeta)



# Generated at 2022-06-13 16:04:37.389717
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        'key1': 'value1',
        'key2': {
            'key3': 'value3',
            'key4': 'value4',
            'key5': {
                'key6': 'value6',
            },
        },
    }
    cli_args = CLIArgs(mapping)
    # Try to modify original mapping. If we did not make it immutable we would be modifying it below.
    mapping['key2']['key3'] = 'value3modified'
    # Check that all types of the mapping were converted to immutable types
    assert isinstance(cli_args['key2']['key5']['key6'], (text_type, binary_type))
    assert isinstance(cli_args['key2']['key5'], ImmutableDict)

# Generated at 2022-06-13 16:05:04.836571
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    if __name__ == '__main__':
        foo = CLIArgs({'verbose': 2})
        assert foo.get('verbose') == 2
        try:
            foo['verbose'] = 4
        except TypeError:
            pass
        assert foo.get('verbose') == 2
        try:
            foo['verbose'] = 4
        except TypeError:
            pass
        assert foo.get('verbose') == 2

# Generated at 2022-06-13 16:05:09.230892
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        class ClassOne(object):
            __metaclass__ = _ABCSingleton
        class ClassTwo(ClassOne):
            pass
        ClassOne()
        ClassTwo()
        assert False, "Class with _ABCSingleton as a metaclass should throw TypeError when instantiated"
    except TypeError:
        pass

# Generated at 2022-06-13 16:05:10.854836
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SomeContainer(object):
        pass

    # make sure this compiles
    SomeContainer()



# Generated at 2022-06-13 16:05:17.964716
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Ensure that the constructor for CLIArgs does not remove any of the command line args
    """
    args = CLIArgs({'a': [1, 2, 3], 'b': 'hello', 'c': {'d': 'goodbye'}, 'e': {1, 2, 3}, 'f': 'test'})
    assert args.get('a') == (1, 2, 3)
    assert args.get('b') == 'hello'
    assert args.get('c') == ImmutableDict({'d': 'goodbye'})
    assert args.get('e') == frozenset({1, 2, 3})
    assert args.get('f') == 'test'


# Generated at 2022-06-13 16:05:24.361118
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display

    display = Display()
    constructor = display.__init__

    # The display object is a singleton, so create one to test the constructor.
    display = constructor()

    # We want to test the constructor, the __init__ and __new__ methods of display.
    # We also want to test the constructor of the superclass, Display.
    # But Display inherits from Singleton, then Display re-implements __new__.
    #
    # The method __new__ of Singleton is invoked first, which then invokes the method
    # __new__ of the Display.  The method __new__ of Display then invokes the constructor
    # of the superclass, Display.  So the constructor of the superclass, Display, is invoked
    # first, then the constructor Display is invoked.
    #
    #

# Generated at 2022-06-13 16:05:26.529336
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs({'foo': 'bar'})
    assert global_cli_args == {'foo': 'bar'}

# Generated at 2022-06-13 16:05:34.780764
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # test that a singleton instance is only created once
    args_1 = GlobalCLIArgs({"a": 1, "b": 2, "c": None})
    args_1["a"] = 3
    args_2 = GlobalCLIArgs({"a": 1, "b": 2, "c": None})
    args_2["a"] = 5
    assert (args_1 == args_2)
    assert (args_1 is args_2)
    assert (args_1["a"] is 3)
    assert (args_2["a"] is 3)

# Generated at 2022-06-13 16:05:42.165119
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str)
    parsed_args = parser.parse_args(["--action", "test"])
    args = GlobalCLIArgs.from_options(parsed_args)
    # Expected output
    # {'action': 'test', 'args': [], 'help': None, 'version': None}
    print(args)
    assert args.action == 'test'
    assert args.version == None

if __name__ == '__main__':
    test_GlobalCLIArgs()

# Generated at 2022-06-13 16:05:46.139770
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=attribute-defined-outside-init
    class TestGlobal(GlobalCLIArgs):
        def __init__(self, name):
            self.name = name
    t = TestGlobal('Foo')
    assert t.name == 'Foo'

# Generated at 2022-06-13 16:05:50.658946
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    for opt in ['-i', '-k', '-K']:
        parser = optparse.OptionParser()
        parser.add_option(opt)
        (options, _) = parser.parse_args([opt])
        GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:06:22.395876
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys
    import unittest
    from ansible.cli import CLI

    class TestGlobalCLIArgs(unittest.TestCase):

        def setUp(self):
            self.cli = CLI(args=[])
            self.parser = self.cli.parser

        def test_basic(self):
            self.parser.parse_args(['--version'])
            self.assertIsInstance(GlobalCLIArgs.instance, GlobalCLIArgs)

if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 16:06:24.840099
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs({'test_key': 'test_value'})
    assert obj['test_key'] == 'test_value'



# Generated at 2022-06-13 16:06:34.580617
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    args = GlobalCLIArgs({'hello': 'pretty', 'goodbye': 'ugly'})
    assert args.get('hello') == 'pretty'
    assert args.get('goodbye') == 'ugly'

    # Test immutability of constructor
    try:
        args['hello'] = 'ugly'
    except TypeError:
        pass
    else:
        raise RuntimeError("Failed to test immutability of constructor")

    # Test immutability of constructor
    try:
        args['insert'] = 'ugly'
    except TypeError:
        pass
    else:
        raise RuntimeError("Failed to test immutability of constructor")



# Generated at 2022-06-13 16:06:43.002769
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.collection_plugins.test_utils.test_data.test_data_cli_args import test_data_cli_args
    from ansible.utils.collection_plugins.test_utils.test_data.test_data_global_cli_args import test_data_global_cli_args

    cli_args = CLIArgs(test_data_cli_args)
    assert cli_args == test_data_cli_args

    global_cli_args = GlobalCLIArgs(test_data_global_cli_args)
    assert global_cli_args == test_data_global_cli_args

    # Make sure that the Singleton patterns work
    assert global_cli_args is GlobalCLIArgs()

# Generated at 2022-06-13 16:06:46.950982
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """Unit test for constructor of class GlobalCLIArgs"""
    import argparse
    args = GlobalCLIArgs.from_options(GlobalCLIArgs.parse_args())
    assert isinstance(args, GlobalCLIArgs)



# Generated at 2022-06-13 16:06:51.280692
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, abc):
            self.abc = abc

    foo = Foo('abc')
    foo_second = Foo('xyz')
    assert foo.abc == 'abc'
    assert foo is foo_second

# Generated at 2022-06-13 16:06:55.150717
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class Test(_ABCSingleton):
        pass

    class Test2(_ABCSingleton):
        pass

    test1 = Test()
    test2 = Test()
    test3 = Test2()
    assert test1 is test2
    assert test1 is not test3
    assert test2 is not test3

# Generated at 2022-06-13 16:06:57.857706
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(CLIArgs, object)
    assert hasattr(CLIArgs, '__init__')
    assert isinstance(CLIArgs, _ABCSingleton)

# Generated at 2022-06-13 16:07:02.461836
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    lst = [1, 2]
    outer = [lst, lst]
    mapping = {'a': outer, 'b': outer}
    cliargs = CLIArgs(mapping)
    assert cliargs['a'] == outer
    assert cliargs['a'][0] is lst
    assert cliargs['a'][1] is lst
    assert cliargs['a'] is cliargs['b']

# Generated at 2022-06-13 16:07:12.712095
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            self.foo = 'foo'

        @classmethod
        def a_class_method(cls):
            return cls()

        @staticmethod
        def a_static_method():
            pass

        def an_instance_method(self):
            return self

        def another_instance_method(self):
            pass

    foo = Foo()
    assert(foo.foo == 'foo')
    assert(foo is Foo())

    assert(foo is Foo.a_class_method())
    assert(foo is foo.a_class_method())
    assert(foo is Foo().a_class_method())

    # Static methods are not really interesting, just verify that they exist
    Foo.a_static_method()
   

# Generated at 2022-06-13 16:08:04.370756
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
        pass

    o1 = TestClass()
    o2 = TestClass()
    assert o1 is o2

# Generated at 2022-06-13 16:08:06.670502
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    d = {"a": "b"}
    g = GlobalCLIArgs(d)
    d["a"] = "c"
    assert g["a"] == "b"

# Generated at 2022-06-13 16:08:08.892382
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
    assert TestClass

# Generated at 2022-06-13 16:08:11.327268
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    x = GlobalCLIArgs({"a": {"b": {"c": "d"}}})
    assert x["a"]["b"]["c"] == "d"

# Generated at 2022-06-13 16:08:21.272309
# Unit test for constructor of class CLIArgs
def test_CLIArgs():

    import collections
    from ansible.module_utils.six import text_type

    class MyMapping(collections.Mapping):
        def __init__(self, *args, **kwargs):
            self.store = dict(*args, **kwargs)

        def __getitem__(self, key):
            return self.store[key]

        def __iter__(self):
            return iter(self.store)

        def __len__(self):
            return len(self.store)



# Generated at 2022-06-13 16:08:30.877889
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest

    args = CLIArgs({'foo': {'bar': {'baz': 'y', 'quux': False}}, 'qux': 'z', 'zap': True})

    assert args.qux == 'z'
    assert args.foo.bar.baz == 'y'
    assert args.foo.bar.quux is False
    assert args.zap

    with pytest.raises(AttributeError):
        args.foo.bar.quux = True

    with pytest.raises(AttributeError):
        args.baz = 'y'

    with pytest.raises(AttributeError):
        args['baz'] = 'y'

    with pytest.raises(AttributeError):
        del args.foo

    with pytest.raises(AttributeError):
        *_, args.foo

# Generated at 2022-06-13 16:08:33.644244
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = {'one': 'value for one', 'two': 'value for two'}
    obj = CLIArgs(options)
    assert obj['one'] == 'value for one'
    assert obj['two'] == 'value for two'

# Generated at 2022-06-13 16:08:44.078089
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class CLIArgsTest(CLIArgs):
        pass
    dict_test = {1: [1, 2, 'abc', {'abc': 123}], 2: set([1, 'abc', 12])}
    cli_args_test = CLIArgsTest(dict_test)
    assert dict_test[1][3] == {'abc': 123}
    assert dict_test[2] == set([1, 'abc', 12])
    assert isinstance(cli_args_test[1], tuple)
    assert isinstance(cli_args_test[1][3], ImmutableDict)
    assert isinstance(dict_test[2], set)
    assert isinstance(cli_args_test[2], frozenset)

# Generated at 2022-06-13 16:08:47.108790
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    a = A()
    b = A()
    assert a is b

# Generated at 2022-06-13 16:08:51.282179
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    sys.argv.append('--a=1')
    sys.argv.append('--b=2')
    ga = GlobalCLIArgs.instance()
    assert ga.get('a') == '1'
    assert ga.get('b') == '2'