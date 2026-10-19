

# Generated at 2022-06-13 15:59:51.410924
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    var1 = ['1', '2', '3']
    var2 = ['a', 'b', 'c']
    var3 = {'k1': ['a', 'b', 'c'], 'k2': ['a', 'b', 'c']}

    cli_args = CLIArgs({'var1': var1, 'var2': var2, 'var3': var3})

    assert cli_args.get('var1') == var1
    assert cli_args.get('var2') == var2
    assert cli_args.get('var3') == var3

    # Test if constructor make nested dictionary immutable
    assert isinstance(cli_args.get('var3'), ImmutableDict)
    assert isinstance(cli_args.get('var3').get('k1'), tuple)

# Generated at 2022-06-13 16:00:01.908549
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest

    class TestCLIArgs(unittest.TestCase):
        def setUp(self):
            self.test_cli_args = CLIArgs.from_options(self.options)

        def test_constructor(self):
            self.assertIsInstance(self.test_cli_args, CLIArgs)
            self.assertIsInstance(self.test_cli_args, ImmutableDict)

        def test_vars(self):
            # options is a MagicMock object created by the argument parser
            self.assertIsInstance(self.test_cli_args['options'], self.options)

    class TestCLIArgsWithNestedVariables(TestCLIArgs):
        def setUp(self):
            self.options = un

# Generated at 2022-06-13 16:00:09.862784
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    dict_obj = {'key1': 1, 'key2': {'key3': 2, 'key4': [1, 2, [3, 4]]}, 'key5': {'set1': {1, 2, 3}, 'set2': {4, 5, 6}}}
    # Create a temporary object of CLIArgs
    obj = CLIArgs(dict_obj)
    # Check if obj is immutable
    assert dict_obj != obj
    # Check if items of dict_obj and obj are immutables
    assert isinstance(obj['key2'], ImmutableDict)
    assert isinstance(obj['key5'], ImmutableDict)
    assert isinstance(obj['key2']['key4'],tuple)

# Generated at 2022-06-13 16:00:19.395189
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'a': 'b', 'c': {'d': {'e': 'f'}, 'g': ['h', 'i', 'j']}, 'k': ['l', 'm', {'n': 'o'}]}
    test_result = _make_immutable(test_dict)
    assert isinstance(test_result, ImmutableDict)
    assert isinstance(test_result['c'], ImmutableDict)
    assert isinstance(test_result['c']['g'], tuple)
    assert isinstance(test_result['c']['d'], ImmutableDict)
    assert isinstance(test_result['k'], tuple)
    assert isinstance(test_result['k'][1], ImmutableDict)

# Generated at 2022-06-13 16:00:21.217830
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestClass(object):
        __metaclass__ = _ABCSingleton
    assert _TestClass() is _TestClass()

# Generated at 2022-06-13 16:00:24.853682
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    This unit test does not actually test any code, but it should pass
    """
    class TestClass(object):
        __metaclass__ = _ABCSingleton

    assert isinstance(TestClass(), TestClass)

# Generated at 2022-06-13 16:00:31.359055
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Make sure that we can create two objects of the same type, but with different values
    test_args = [
        dict(a=1, b=2, c=3),
        dict(a=6, b=5, c=4),
    ]
    for args in test_args:
        try:
            SingletonClass = _ABCSingleton('SingletonClass', (object,), dict(args=args))
            SingletonClass.__new__(SingletonClass)
        except TypeError:
            raise Exception("Failed to create Singleton with {0}".format(args))

# Generated at 2022-06-13 16:00:34.607455
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs({'a': 1, 'b': '2'})
    assert a == {'a': 1, 'b': '2'}

# Generated at 2022-06-13 16:00:42.725775
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = dict(a=1, b=2, c=1, d=[1,2,3])
    cliargs = GlobalCLIArgs(args)

    assert cliargs == args
    assert isinstance(cliargs['a'], int)
    assert cliargs['a'] == 1
    assert isinstance(cliargs['b'], int)
    assert cliargs['b'] == 2
    assert isinstance(cliargs['c'], int)
    assert cliargs['c'] == 1
    assert isinstance(cliargs['d'], tuple)
    assert cliargs['d'] == (1, 2, 3)
    assert isinstance(cliargs, ImmutableDict)

# Generated at 2022-06-13 16:00:43.337746
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs == GlobalCLIArgs

# Generated at 2022-06-13 16:00:51.540975
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    arg = {'delete': False, 'networks': [], 'force': False, 'project': 'desktop', 'user': 'student', 'image': 'fedora', 'flavor': '1', 'instance': 'HelloWorld', 'key': 'Mykey', 'config_file': '/path/to/config.yml'}
    cli_args = CLIArgs(arg)
    assert cli_args == arg

# Generated at 2022-06-13 16:00:52.583941
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    a = A()
    a2 = A()
    assert a is a2

# Generated at 2022-06-13 16:00:57.190867
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        # No params passed on to constructor, which is ok
        args1 = GlobalCLIArgs()
        args2 = GlobalCLIArgs()
        assert args1 is args2
    except Exception as e:
        raise AssertionError("Exception raised while creating GlobalCLIArgs singleton instance: {}".format(e))

# Generated at 2022-06-13 16:01:06.601796
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert isinstance(_ABCSingleton, type)
    assert isinstance(_ABCSingleton, ABCMeta)
    assert isinstance(_ABCSingleton, Singleton)

    class C1(object):
        pass

    assert isinstance(C1, type)
    assert not isinstance(C1, ABCMeta)
    assert not isinstance(C1, Singleton)

    class C2(object):
        __metaclass__ = ABCMeta

    assert isinstance(C2, type)
    assert isinstance(C2, ABCMeta)
    assert not isinstance(C2, Singleton)

    class C3(object):
        __metaclass__ = Singleton

    assert isinstance(C3, type)
    assert not isinstance(C3, ABCMeta)
    assert isinstance(C3, Singleton)


# Generated at 2022-06-13 16:01:16.453098
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from copy import deepcopy
    # We want to test that we create a copy of the command line args and then convert them
    # to immutable data types so that they cannot be modified.
    #
    # We will pass in a dict to the constructor and verify the data in it is unchanged in the
    # constructed object by using the == operator, which is overloaded by __eq__ to check the
    # values in the dict.
    #
    # We will deepcopy the original dict so that we can verify that the original dict did not
    # get changed by the constructor.
    #
    # We will also verify that the data types in the dict are changed by testing the type of
    # each object in the dict.

# Generated at 2022-06-13 16:01:26.262743
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test for constructor of class CLIArgs"""
    cli_args_map1 = ImmutableDict({'extra-vars': 'a=b', 'roles': ['role1', 'role2']})
    # Test if the initializer will transform the sequence to a immutable data type
    cli_args = CLIArgs(cli_args_map1)
    assert cli_args['roles'] == ('role1', 'role2')
    assert cli_args == cli_args_map1
    # Test if the initializer will transform the mapping to a immutable data type
    cli_args_map2 = {'extra-vars': 'a=b', 'roles': ['role1', 'role2'], 'extra-vars-dict': {'role3': 'c=d'}}
    cli_args = CLIArgs

# Generated at 2022-06-13 16:01:34.515312
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import sys
    # new_instance will return a singleton
    gca = GlobalCLIArgs.new_instance()
    # Due to the singleton property, modify instance in one place should be visible in other place
    gca['test'] = 'test'
    # Asserts two objects point to the same memory location
    assert GlobalCLIArgs.new_instance() is gca
    assert GlobalCLIArgs.new_instance() == {'test': 'test'}
    # Now test the __init__ method
    test_dict = {'test_dict': {'test_dict1': 'test'}}
    # new_instance will return a singleton
    gca = GlobalCLIArgs.new_instance()
    assert gca is not {}
    assert gca is not collections.defaultdict(dict)
    assert gca

# Generated at 2022-06-13 16:01:38.205230
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options_dict = {'foo': 'bar'}

    # test simple pass through
    assert GlobalCLIArgs.from_options(options_dict) == {'foo': 'bar'}

    # test conversion of mutable to immutable
    options_dict['bar'] = set(['foo', 'bar'])

# Generated at 2022-06-13 16:01:47.255926
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({1: 1}) == {1: 1}
    assert CLIArgs({1: [1, 2, 3]}) == {1: (1, 2, 3)}
    assert CLIArgs({1: {1: 1, 2: 2}}) == {1: {1: 1, 2: 2}}
    assert CLIArgs({1: (1, 2, 3)}) == {1: (1, 2, 3)}
    assert CLIArgs({1: {1: 1, 2: {1: 1}}}) == {1: {1: 1, 2: {1: 1}}}
    assert CLIArgs({1: {1: 1, 2: (1, 2, 3)}}) == {1: {1: 1, 2: (1, 2, 3)}}

# Generated at 2022-06-13 16:01:49.312309
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    # sys.argv[1] = "--version"
    # assert(CLIArgs.from_options(options)



# Generated at 2022-06-13 16:01:55.415062
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs({'foo': 'bar', 'bam': 'baz'})
    assert global_cli_args['foo'] == 'bar'
    assert global_cli_args['bam'] == 'baz'

# Generated at 2022-06-13 16:01:59.139861
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class ABCSingletonTest(object):
        pass
    assert isinstance(ABCSingletonTest, ABCMeta)
    assert isinstance(ABCSingletonTest, Singleton)
    assert isinstance(ABCSingletonTest, _ABCSingleton)

# Generated at 2022-06-13 16:02:05.928656
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:15.160471
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common._collections_compat import Mapping

    d = {'a': 1, 'b': {'c': 2, 'd': 3}}
    try:
        d['b']['c'] = 2.1
    except TypeError:
        pass
    else:
        raise AssertionError('Failed to make dictionary immutable')

    try:
        d['b']['newkey'] = 4
    except TypeError:
        pass
    else:
        raise AssertionError('Failed to make dictionary immutable')

    cli_args = CLIArgs(d)
    assert isinstance(cli_args, ImmutableDict), "CLIArgs didn't use ImmutableDict"
    assert isinstance(cli_args, Mapping), "CLIArgs didn't use ImmutableDict"



# Generated at 2022-06-13 16:02:26.032620
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLIArgs(dict(a=1, b=2))
    # Test that we support immutable objects
    CLIArgs(dict(a=1, b=ImmutableDict(dict(c=3, d=4)), c=2))
    # Test that we convert sequences to immutable sequences
    CLIArgs(dict(a=[1, 2], b=ImmutableDict(dict(c=[3, 4], d=4)), c=2))
    # Test that we convert sets to immutable sets
    CLIArgs(dict(a={1, 2}, b=ImmutableDict(dict(c={3, 4}, d=4)), c=2))
    # Test that we convert dictionaries to immutable dictionaries

# Generated at 2022-06-13 16:02:29.257348
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test the constructor for class GlobalCLIArgs.
    """
    opts = GlobalCLIArgs({'foo': 'bar'})
    assert opts['foo'] == 'bar'
    assert isinstance(opts, ImmutableDict)
    assert isinstance(opts, GlobalCLIArgs)
    assert not isinstance(opts, CLIArgs)


# Generated at 2022-06-13 16:02:33.828126
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # ImmutableDict is a class from a 3rd-party library.  However, the verison we use does not support
    # the `is` operator for comparing two references to the same object.  Instead, it requires `==`.
    # This means we can't test that the dict was actually made immutable, but we can at least test
    # that the ImmutableDict constructor was called.

    # Define a simple dictionary
    plain = {
        'a': 1,
        'b': ['c', 'd', 'e'],
        'f': 'g',
    }

    # Instantiate a CLIArgs object with it
    test_obj = CLIArgs(plain)

    # Verify that `is` fails, but `==` passes
    assert plain is not test_obj
    assert plain == test_obj

# Generated at 2022-06-13 16:02:36.655901
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonTest(object):
        __metaclass__ = _ABCSingleton

    test1 = SingletonTest()
    test2 = SingletonTest()
    assert test1 is test2

# Generated at 2022-06-13 16:02:42.689753
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyMetaClass(metaclass=_ABCSingleton):
        pass

    class MyABC(metaclass=ABCMeta):
        pass

    # The intent of this is to check that we do not get an error when we instantiate a class with
    # _ABCMetaclass as its metaclass.  The following references are not used, just checking that
    # they can be instantiated without error.
    MyMetaClass()
    MyABC()

# Generated at 2022-06-13 16:02:50.436479
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    import itertools

    class TestSingleton(unittest.TestCase):
        def __test_singleton_equality(self, val1, val2):
            g = GlobalCLIArgs
            g1 = GlobalCLIArgs()
            self.assertEqual(g1, g)
            self.assertEqual(g, g1)
            self.assertEqual(hash(g1), hash(g))
            self.assertEqual(g.instance, g)
            self.assertEqual(g1.instance, g1)
            g2 = GlobalCLIArgs()
            self.assertEqual(g1, g2)
            self.assertEqual(g2, g1)
            self.assertEqual(hash(g2), hash(g1))

# Generated at 2022-06-13 16:03:05.346641
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--testlist', nargs='+', default=['one', 'two', 'three'])
    parser.add_argument('--testdict', type=dict, default={'one': 1, 'two': 2, 'three': 3})
    parser.add_argument('--teststr', type=str, default='test')
    parser.add_argument('--testint', type=int, default=1)

    # call to parse_args is how we would normally get CLIArgs
    args = CLIArgs.from_options(parser.parse_args())

    assert isinstance(args, ImmutableDict)
    assert args.get('testlist') == ('one', 'two', 'three')

# Generated at 2022-06-13 16:03:08.903067
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class S1(object):
        __metaclass__ = _ABCSingleton
    class S2(object):
        __metaclass__ = _ABCSingleton
    assert S1() == S2()

# Generated at 2022-06-13 16:03:16.937657
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Check that the CLIArgs object is immutable by verifying exception thrown when we try to modify.

    Check that the CLIArgs object is immutable by verifying exception thrown when we try to modify.
    """
    test_dict = {"key1": "value1", "key2": "value2"}
    cli_args = CLIArgs(test_dict)

    try:
        cli_args["key1"] = "new value1"
    except RuntimeError:
        pass
    else:
        assert "Error testing immutability, expected exception"
    assert cli_args["key1"] == "value1"
    assert cli_args["key2"] == "value2"


# Generated at 2022-06-13 16:03:26.574376
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import mock
    import datetime

    now = datetime.datetime.now()

    # Make sure we can handle all the basic types
    mapping = {
        'a': 1,
        'b': 1.0,
        'c': True,
        'd': now,
        'e': text_type('text'),
        'f': binary_type('binary'),
        'g': bytearray('bytearray'),
        'h': 'text2',
    }
    # Make sure the constructor returns a tuple if given one
    mapping['i'] = (1, 2, 3)
    # Make sure the constructor returns a ImmutableDict if given one
    mapping['j'] = ImmutableDict({'key': 'value'})
    # Make sure we recurse into nested containers

# Generated at 2022-06-13 16:03:28.979440
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():  # pragma: no cover
    class Test(_ABCSingleton):
        pass

    assert isinstance(Test(), Test)
    assert Test() is Test()

# Generated at 2022-06-13 16:03:40.410778
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs.from_options([])
    assert isinstance(global_cli_args, ImmutableDict)
    assert global_cli_args == ImmutableDict()

    # Assuming we have a CLI args parser that is similar to Ansible's normal parser, the type of
    # object returned from parser.parse_args() is a list of Namespace objects.
    from argparse import Namespace
    classnamespace = Namespace(a=1, b=2)
    global_cli_args = GlobalCLIArgs.from_options([classnamespace])
    assert isinstance(global_cli_args, ImmutableDict)
    assert global_cli_args == ImmutableDict({'a': 1, 'b': 2})


# Generated at 2022-06-13 16:03:42.604799
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # noinspection PyTypeChecker
    class MetaSubclass(_ABCSingleton):
        pass

    class Subclass(object):
        __metaclass__ = MetaSubclass

    a = Subclass()
    b = Subclass()
    assert a is b

# Generated at 2022-06-13 16:03:47.867459
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': {'b': 1, 'c': 2}, 'd': [1, 2, 3]}
    cli_args = CLIArgs(mapping)
    assert cli_args['a']['b'] == 1
    with pytest.raises(TypeError):
        cli_args['a']['b'] = 2



# Generated at 2022-06-13 16:03:51.042370
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass
    # The first time we call Test() it creates an instance
    assert Test()
    # The second time we call Test() it should return the same instance instead of creating a new one
    assert Test() == Test()



# Generated at 2022-06-13 16:03:52.500684
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs is type(GlobalCLIArgs())



# Generated at 2022-06-13 16:04:11.684992
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert_equal = __import__('unit.compat').assert_equal
    import collections
    import sys
    import ansible.constants as C
    cliargs = CLIArgs.from_options(C.initialize_global_options(sys.argv))
    assert cliargs.get('diff') is False
    assert isinstance(cliargs, collections.Mapping)
    assert isinstance(cliargs, collections.MutableMapping)
    assert type(cliargs) is not collections.Mapping
    assert type(cliargs) is not collections.MutableMapping
    assert not isinstance(cliargs, collections.Sequence)
    assert not isinstance(cliargs, collections.MutableSequence)
    assert_equal(cliargs.get('vault_password_file'), '.vault_pass')

# Generated at 2022-06-13 16:04:23.401939
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test CLIArgs constructor"""
    list1 = ['one', 'two', 'three']
    list2 = ['four', 'five', 'six']
    dict1 = {'one': 1, 'two': 2, 'three': 3}
    dict2 = {'four': 4, 'five': 5, 'six': 6}
    dict3 = {'seven': 7, 'eight':  8, 'nine': 9}
    dict4 = {'ten': 10, 'eleven': 11, 'twelve': 12}
    dict_in_dict = {'nested_dict': dict4, 'list_in_dict': list2}
    dict_in_dict_in_dict = {'nested_dict': dict_in_dict, 'list_in_dict': list2}

# Generated at 2022-06-13 16:04:27.158447
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ClassA(metaclass=_ABCSingleton):
        pass

    class ClassB(ClassA):
        pass

    class ClassC(ClassB):
        pass

    class ClassD(ClassB):
        pass

    assert ClassA is ClassB is ClassC is ClassD

# Generated at 2022-06-13 16:04:31.075870
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class NewType(object, metaclass=_ABCSingleton):
        pass

    new_type_1 = NewType()
    new_type_2 = NewType()

    assert new_type_1 is new_type_2

# Generated at 2022-06-13 16:04:34.297351
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Base(object):
        pass

    class Foo(Base):
        __metaclass__ = _ABCSingleton

    class Bar(Base):
        __metaclass__ = _ABCSingleton

    class Baz(Foo, Bar):
        pass

    assert Baz() is Baz()

# Generated at 2022-06-13 16:04:38.146857
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_args = {'listtags': False, 'listtasks': False}
    test_parser = CLIArgs(test_args)
    assert test_parser['listtags'] == False
    assert test_parser['listtasks'] == False


# Generated at 2022-06-13 16:04:41.220344
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class test(object):
        pass
    assert issubclass(test, test)  # Ensure _ABCSingleton is a subclass of _ABCSingleton
    assert issubclass(test, Singleton)  # Ensure _ABCSingleton is a subclass of Singleton as well

# Generated at 2022-06-13 16:04:45.319195
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Meta(object):
        foo = 'bar'

    class Test(metaclass=_ABCSingleton):
        __metaclass__ = Meta

    assert issubclass(Test, Singleton)
    assert Test.foo == 'bar'



# Generated at 2022-06-13 16:04:48.185591
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestABCSingleton(object, metaclass=_ABCSingleton):
        def __init__(self, foo):
            pass

    assert _TestABCSingleton


# Generated at 2022-06-13 16:04:56.201271
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    # Args 1 and 3 are unicode, 2 is bytes
    cargs = CLIArgs({b'1': u'a', b'2': 1, b'3': [u'a', 1]})
    if sys.version_info[0] > 2:
        # unicode is str in Python 3 so we can iterate on it
        for key, value in cargs.items():
            assert(isinstance(key, text_type))
            assert(isinstance(value, text_type))
    else:
        # unicode is not iterable in Python 2 so we can not iterate on it
        pass

# Generated at 2022-06-13 16:05:28.736736
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class _A(object):
        def __init__(self, *args, **kwargs):
            pass
    # Make sure we cannot make more than one of this
    a = _A()
    b = _A()
    assert(id(a) == id(b))
    # And it should continue being a Subclass of object
    assert(isinstance(a, object))
    # And if we try to override __new__, it should still be a Singleton
    class _B(object):
        def __new__(cls, *args, **kwargs):
            pass
    @add_metaclass(_ABCSingleton)
    class _C(_B):
        def __init__(self, *args, **kwargs):
            super(_C, self).__init__

# Generated at 2022-06-13 16:05:34.132798
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Test that _ABCSingleton is indeed a Singleton class that is also ABCMeta based"""

    class MyABCSingleton(_ABCSingleton):
        """An example of a class that uses _ABCSingleton metaclass"""

    my_object = MyABCSingleton()
    my_object2 = MyABCSingleton()
    assert my_object is my_object2



# Generated at 2022-06-13 16:05:39.895795
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {u'foo': u'bar'}
    obj = GlobalCLIArgs(args)
    assert obj == args
    try:
        obj[u'foo'] = u'baz'
    except TypeError:
        pass
    else:
        raise AssertionError("GlobalCLIArgs should be immutable")
# end of test_GlobalCLIArgs()

# Generated at 2022-06-13 16:05:47.176868
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    def check_container(container):
        for key, value in container.items():
            if isinstance(value, collections.MutableMapping):
                assert isinstance(value, ImmutableDict)
                check_container(value)
            elif isinstance(value, collections.Sequence) and not isinstance(value, str):
                assert isinstance(value, tuple)
                for item in value:
                    check_container(item)
            elif isinstance(value, collections.Set):
                assert isinstance(value, frozenset)
                for item in value:
                    check_container(item)
            else:
                assert not isinstance(value, collections.Container)


# Generated at 2022-06-13 16:05:52.494347
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # do not use super() because it will cause a ClassNotFound error
    class A(_ABCSingleton):
        pass

    class B(_ABCSingleton):
        def __init__(self):
            pass

    class C(_ABCSingleton):
        def __init__(self):
            pass

    assert A() is A()
    assert B() is B()
    assert C() is C()
    assert A() is not B()

# Generated at 2022-06-13 16:06:03.482721
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(metaclass=_ABCSingleton):
        def __init__(self, **kwargs):
            self.name = kwargs.get('name', None)

    assert id(TestSingleton()) == id(TestSingleton())
    assert id(TestSingleton()) == id(TestSingleton(name='foo'))
    one = TestSingleton(name='one')
    assert id(one) == id(TestSingleton(name='one'))
    two = TestSingleton(name='two')
    assert id(two) != id(TestSingleton(name='one'))
    assert one != two
    assert one.name != two.name


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-vvv'])

# Generated at 2022-06-13 16:06:06.911858
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
        pass

    class B(A):
        pass

    assert A() == B()



# Generated at 2022-06-13 16:06:10.882431
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs() == ImmutableDict()
    assert CLIArgs({}) == ImmutableDict()
    assert CLIArgs({'a': 'b'}) == ImmutableDict({'a': 'b'})



# Generated at 2022-06-13 16:06:12.888458
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """exercise the GlobalCLIArgs constructor in the utils dir"""
    GlobalCLIArgs({})

# Generated at 2022-06-13 16:06:17.177269
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _FakeABCMeta(object):
        @staticmethod
        def __subclasshook__(cls, subclass):
            return True

    assert issubclass(type(_ABCSingleton('__ABCSingleton_test', (type,), {'__abstractmethods__': set()})), _FakeABCMeta)


# Unit tests for the test_make_immutable function

# Generated at 2022-06-13 16:07:12.347943
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test the constructor of class CLIArgs
    """
    # pylint: disable=unused-variable
    # Test initialization with set of arguments
    args = CLIArgs({"foo": "bar"})

    # Test initialization with another CLIArgs objects
    args = CLIArgs(CLIArgs({"foo": "bar"}))

    # Test initialization with another ImmutableDict object.
    args = CLIArgs(ImmutableDict({"foo": "bar"}))

    # Test initialization with a regular dict
    args = CLIArgs({"foo": ["bar", "baz"]})

    args = CLIArgs({"foo": {"bar": "baz"}})

    # Test initialization with a regular list
    args = CLIArgs({"foo": ["bar", ["baz", ["foofoo"]]]})

    # Test initialization with a regular set


# Generated at 2022-06-13 16:07:19.132012
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # pylint: disable=too-few-public-methods
    class TestABCSingleton(object):
        __metaclass__ = _ABCSingleton
    assert isinstance(TestABCSingleton(), TestABCSingleton)
    assert isinstance(TestABCSingleton(), Singleton)
    assert isinstance(TestABCSingleton(), object)
    assert TestABCSingleton() is TestABCSingleton()

# Generated at 2022-06-13 16:07:26.159821
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {
        'foo': 'bar',
        'bar': {'baz': 'biz'},
        'baz': [1, 2, 3],
        'biz': set([1, 2, 3]),
    }
    x = CLIArgs(args)
    assert x['foo'] == 'bar'
    assert x['bar']['baz'] == 'biz'
    assert x['baz'] == (1, 2, 3)
    assert x['biz'] == frozenset([1, 2, 3])

    assert isinstance(x['foo'], text_type)
    assert isinstance(x['baz'], tuple)
    assert isinstance(x['biz'], frozenset)

# Generated at 2022-06-13 16:07:32.940459
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = None
    cli_args = CLIArgs(vars(options))

    assert len(cli_args) == 0

    options = {'list': [1, 2, 3]}
    cli_args = CLIArgs(vars(options))
    assert len(cli_args) == 1

    options = {'dict': {'a': 1, 'b': 'x'}}
    cli_args = CLIArgs(vars(options))


# Generated at 2022-06-13 16:07:35.349863
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    global_args = GlobalCLIArgs.from_options(argparse.Namespace(test='arg'))
    assert global_args.test == 'arg'

# Generated at 2022-06-13 16:07:39.317049
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    one_GlobalCLIArgs = GlobalCLIArgs({'a': 'b', 'c': 'd'})
    another_GlobalCLIArgs = GlobalCLIArgs({'x': 'y'})

    assert one_GlobalCLIArgs == another_GlobalCLIArgs
    assert one_GlobalCLIArgs is another_GlobalCLIArgs

# Generated at 2022-06-13 16:07:41.482432
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'connection': 'ssh', 'become': 'sudo'}
    cliargs = CLIArgs(mapping)
    assert cliargs['connection'] == 'ssh'
    assert cliargs['become'] == 'sudo'

# Generated at 2022-06-13 16:07:50.480867
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Unit test for constructor of class CLIArgs
    """
    # Test with dictionary
    test_dict = {'foo': 'bar'}
    cli_args = CLIArgs(test_dict)
    assert cli_args == test_dict
    assert isinstance(cli_args, ImmutableDict)

    # Test with empty dictionary
    test_dict = {}
    cli_args = CLIArgs(test_dict)
    assert cli_args == test_dict
    assert isinstance(cli_args, ImmutableDict)


# Generated at 2022-06-13 16:07:52.353950
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Make sure you can create objects of a class using _ABCSingleton as it's metaclass.
    """
    class ThisIsATest(object):
        __metaclass__ = _ABCSingleton

    first = ThisIsATest()
    second = ThisIsATest()

    assert first is second

# Generated at 2022-06-13 16:07:59.544354
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys

    class MockCLIArgs(object):
        def __init__(self):
            self.argument = 'hi'

    mock_args = MockCLIArgs()
    sys.argv = ['ansible-console', '--argument', 'hi']
    global_args = GlobalCLIArgs.from_options(mock_args)
    assert global_args == {'argument': 'hi'}