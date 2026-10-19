

# Generated at 2022-06-13 15:59:40.077047
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert isinstance(_make_immutable(""), text_type)
    assert isinstance(_make_immutable("abc"), text_type)
    assert isinstance(_make_immutable("abc" * 1000), text_type)
    assert isinstance(_make_immutable(b""), binary_type)
    assert isinstance(_make_immutable(b"abc"), binary_type)
    assert isinstance(_make_immutable(b"abc" * 1000), binary_type)

    x = _make_immutable(["a", "b", "c"])
    assert isinstance(x, tuple)
    assert len(x) == 3
    assert isinstance(x[0], text_type)
    assert isinstance(x[1], text_type)
    assert isinstance(x[2], text_type)

    x = _make_

# Generated at 2022-06-13 15:59:48.087048
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Expected constructor to take a dict, not a list
    assert CLIArgs({'hello': 'goodbye'}).get('hello') == 'goodbye'

    # Expected constructor to convert a dict to immutable
    test_mutable = {}
    test_immutable = CLIArgs(test_mutable)
    assert test_immutable.get('hello') is None
    test_mutable['hello'] = 'goodbye'
    assert test_immutable.get('hello') is None



# Generated at 2022-06-13 15:59:54.099525
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test construction and access of CLIArgs"""
    expected = {
        'listitems': [1, 2, 3],
        'dictitems': {'a': 1, 'b': 3, 'c': 3},
        'setitems': {'a', 'b', 'c'},
        'string': 'string',
        'int': 4,
        'float': 3.14,
        'bool_false': False,
        'bool_true': True,
    }
    cliargs = CLIArgs(expected)
    assert cliargs == expected

# Generated at 2022-06-13 16:00:02.973764
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Create a test class
    class _Test(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key and self.value == other.value

    # Create a dictionary with values we know are mutable
    test_dict = {text_type('foo'): [1, 2, 3],
                 text_type('bar'): {text_type('baz'): set(),
                                    text_type('bat'): frozenset()},
                 text_type('boo'): _Test(text_type('foo'), 7)}

    # Create a CLIArgs object based on the mutable test_dict
    test = CLIArgs(test_dict)

    # Verify that everything is immutable and unchanged except the

# Generated at 2022-06-13 16:00:06.095252
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # make sure we can't modify the CLIArgs class
    args = CLIArgs.from_options(GlobalCLIArgs())
    args['foo'] = 'bar'
    assert args['foo'] != 'bar'

# Generated at 2022-06-13 16:00:12.266971
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Just need to create multiple versions of this class and make sure they are the same
    class TestABCSingleton(_ABCSingleton('TestABCSingleton_Meta', (), {'test': 42})):
        pass

    class TestABCSingleton2(_ABCSingleton('TestABCSingleton_Meta', (), {'test': 42})):
        pass

    obj = TestABCSingleton()
    obj2 = TestABCSingleton2()

    assert obj is obj2
    assert TestABCSingleton is TestABCSingleton2

# Generated at 2022-06-13 16:00:21.844959
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:00:25.480142
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        def test(self):
            return 1

    class B(A):
        def test(self):
            return 2

    a = A()
    b = B()

    assert a.test() == 1
    assert b.test() == 2
    assert A() is a
    assert B() is b

# Generated at 2022-06-13 16:00:27.380419
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca1 = GlobalCLIArgs({'a': 1})
    gca2 = GlobalCLIArgs({'a': 2})
    assert gca1 == gca2
    assert gca1 is gca2
    assert gca1['a'] == 2

# Generated at 2022-06-13 16:00:34.647521
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class MockOptions:
        def __init__(self, dictionary):
            self.__dict__.update(dictionary)

    # test CLIArgs is a singleton
    options1 = MockOptions({"foo": "bar", "baz": "quux"})
    options2 = MockOptions({"foo": "bar", "baz": "quux"})
    args1 = CLIArgs.from_options(options1)
    args2 = CLIArgs.from_options(options2)
    assert args1 is args2, "CLIArgs should be a singleton"

    # test __contains__ works
    assert "foo" in args1, "__contains__() method should work"

    # test __getitem__ works
    assert args1["foo"] == "bar", "__getitem__() method should work"

    # test __

# Generated at 2022-06-13 16:00:43.307423
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from collections import OrderedDict
    from ansible.module_utils.common.collections import MutableMapping
    import ansible.module_utils.common._collections_compat as collections_compat

    d = OrderedDict([('a', 1), ('b', [1, 2, 3]), ('c', [{'x': 1, 'y': 2, 'z': 3}, {'l': 4, 'm': 5, 'n': 6}])])
    args = GlobalCLIArgs(d)
    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args, collections_compat.Mapping)
    assert not isinstance(args, MutableMapping)


test_GlobalCLIArgs()

# Generated at 2022-06-13 16:00:46.109585
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Alpha(_ABCSingleton):
        pass

    class Beta(_ABCSingleton):
        pass

    class Gamma(_ABCSingleton):
        pass

    #Check uninstantiated classes
    assert Alpha is Beta is Gamma

    #Check instantiated classes
    assert Alpha() is Beta() is Gamma()

# Generated at 2022-06-13 16:00:47.330066
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs([])

# Generated at 2022-06-13 16:00:50.040332
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({'arg1': 'value'}) == {'arg1': 'value'}



# Generated at 2022-06-13 16:00:53.372110
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        """
        This should fail because it is a metaclass only but does not inherit from the correct base classes
        """
        __metaclass__ = _ABCSingleton
    test = TestClass()

# Generated at 2022-06-13 16:00:58.554584
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Class1(metaclass=_ABCSingleton):
        pass

    class Class2(_ABCSingleton, ABCMeta):
        pass

    assert issubclass(Class1, Singleton)
    assert issubclass(Class2, Singleton)
    assert issubclass(Class1, ABCMeta)
    assert issubclass(Class2, ABCMeta)

# Generated at 2022-06-13 16:01:01.010720
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.compat import get_optionparser
    parser = get_optionparser()
    (options, _) = parser.parse_args()
    GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:01:08.336918
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:01:14.100371
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():  # pragma: nocover
    from ansible.utils.display import Display

    class TestClass(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, arg):
            self.arg = arg

        def get_arg(self):
            return self.arg

    assert TestClass.__bases__ == (Singleton, )
    assert TestClass.__mro__ == (TestClass, Singleton, object)

    obj = TestClass("test")
    assert isinstance(obj, TestClass)
    assert obj is TestClass("test")
    assert obj.get_arg() == "test"

    class TestClassDisplay(TestClass, Display):
        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            pass

    obj

# Generated at 2022-06-13 16:01:15.982619
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import doctest
    results = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert results.failed == 0

# Generated at 2022-06-13 16:01:27.983789
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    d = dict(a=1, b=dict(a=1, b=dict(a=1, b=1)))
    t = text_type('abc')
    b = binary_type('abc')
    l = [1, 2, 3]
    s = set([1, 2, 3])
    d1 = dict(a=1, b=dict(a=1, b=dict(a=1, b=1)), t=t, b=b, l=l, s=s)
    c = CLIArgs(d1)
    assert c['a'] == 1
    assert c['b']['a'] == 1
    assert c['b']['b']['a'] == 1
    assert c['b']['b']['b'] == 1
    assert c['t'] == t

# Generated at 2022-06-13 16:01:30.194260
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class Test():
        """
        Test GlobalCLIArgs
        """
        def __init__(self):
            self.args = GlobalCLIArgs({})

    Test()
    Test()

# Generated at 2022-06-13 16:01:32.474738
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo():
        pass
    class Bar():
        pass

    assert Foo() == Foo()
    assert Foo() is Foo()
    assert Bar() != Bar()
    assert Bar() is not Bar()

# Generated at 2022-06-13 16:01:35.316205
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Passes if Python accepts this syntax
    class _ABCSingletonTest(_ABCSingleton):
        """
        Test class used as a unit test for _ABCSingleton metaclass
        """
        pass

# Generated at 2022-06-13 16:01:46.490136
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.constants as C
    import ansible.module_utils.common.args as my_args
    from collections import namedtuple
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 16:01:51.077782
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'first_arg': 1, 'second_arg': 'two', 'third_arg': ['3a', '3b', '3c']}
    assert CLIArgs(mapping) == ImmutableDict({'first_arg': 1, 'second_arg': 'two', 'third_arg': ('3a', '3b', '3c')})

# Generated at 2022-06-13 16:02:00.917104
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import copy
    import ansible.constants as C
    from ansible.module_utils.common.collections import MutableMapping, MutableSequence, MutableSet
    from ansible.module_utils.common.collections import MutableDict

    test_dict = {u"a": u"b"}
    test_dict_mutable = MutableDict(test_dict.copy())

    test_sequence = [1, 2, 3]
    test_sequence_mutable = MutableSequence(test_sequence.copy())

    test_set = {123, 456}
    test_set_mutable = MutableSet(test_set.copy())

    test_args = CLIArgs(test_dict)
    # Test if the CLIArgs is immutable

# Generated at 2022-06-13 16:02:02.725761
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options = GlobalCLIArgs.from_options(None)
    options.update({'test': 1})
    assert options['test'] == 1

# Generated at 2022-06-13 16:02:09.938128
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import copy
    import collections
    import json
    import yaml

    def check_deep_equal(a, b):
        if a == b:
            assert a == b
            assert b == a
        elif isinstance(a, collections.Iterable) and isinstance(b, collections.Iterable):
            check_deep_equal(list(a), list(b))
        else:
            assert a == b

    # Check basic types
    for value in ['1', 1, True, 1.1]:
        test = CLIArgs({'test': value})
        check_deep_equal(test['test'], value)
        assert isinstance(test['test'], type(value))
        assert isinstance(test, ImmutableDict)

    # Check that lists are converted to tuples

# Generated at 2022-06-13 16:02:21.061042
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test that the constructor makes the proper changes to the "mapping" param
    """
    temp_dict = {}
    temp_list = []
    temp_set = set()
    temp_string = ""
    temp_integer = 1
    temp_float = 1.5
    temp_dict['dict'] = {}
    temp_dict['list'] = []
    temp_dict['set'] = set()
    temp_dict['string'] = ""
    temp_dict['integer'] = 1
    temp_dict['float'] = 1.5
    temp_list.append({})
    temp_list.append([])
    temp_list.append(set())
    temp_list.append("")
    temp_list.append(1)
    temp_list.append(1.5)
    temp_set.add({})


# Generated at 2022-06-13 16:02:28.850523
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = {
        'inventory': ['inventory.ini'],
        'args': ['--wait', '1', '--limit=foo,bar', '--limit', 'bar'],
        'vars': ['myvar=myvalue'],
        'other': {
            'check': True,
            'connection': 'ssh'
        },
        'check': False
    }

    args = CLIArgs(data)
    assert isinstance(args['inventory'], tuple)
    assert args['inventory'][0] == "inventory.ini"
    assert isinstance(args['inventory'], tuple)
    assert isinstance(args['args'], tuple)
    assert isinstance(args['args'][0], text_type)
    assert isinstance(args['args'][1], text_type)

# Generated at 2022-06-13 16:02:40.355637
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test parser cli args when pass empty dict as argument
    cli_args_empty = CLIArgs({})
    assert isinstance(cli_args_empty, CLIArgs)
    assert len(cli_args_empty.keys()) == 0

    # test parser cli args when pass dict with data as argument
    cli_args_with_data = CLIArgs({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(cli_args_with_data, CLIArgs)
    assert len(cli_args_with_data.keys()) == 2
    assert cli_args_with_data['key1'] == 'value1'
    assert cli_args_with_data['key2'] == 'value2'

    # test parser cli args when pass dict that contains container as argument
    cli_args_

# Generated at 2022-06-13 16:02:45.010292
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test CLIArgs constructor"""

    # Empty mapping
    empty_mapping = {}
    cli_args = CLIArgs(empty_mapping)
    assert isinstance(cli_args, ImmutableDict)
    assert {} == cli_args

    # Empty mapping with explicit key set
    cli_args = CLIArgs({'i': '', 'j': None})
    assert isinstance(cli_args, ImmutableDict)
    assert {'i': '', 'j': None} == cli_args

    # Validate that a sequence is converted to an immutable tuple
    cli_args = CLIArgs({'i': [1, 2, 3]})
    assert isinstance(cli_args, ImmutableDict)
    assert {'i': (1, 2, 3, )} == cli_args

    # Validate that

# Generated at 2022-06-13 16:02:48.456049
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Parent(object):
        pass

    class Child(_ABCSingleton, Parent):
        pass

    assert Child() is Child()

# Generated at 2022-06-13 16:02:56.723351
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'color': 'blue', 'list': (1, 2), 'set': set((3, 4)), 'dict': {5: 6, 7: 8}})

    assert isinstance(args, Mapping) and isinstance(args, ImmutableDict)
    assert isinstance(args['color'], ImmutableDict) or args['color'] == 'blue'
    assert isinstance(args['list'], ImmutableDict) or isinstance(args['list'], tuple)
    assert isinstance(args['set'], ImmutableDict) or isinstance(args['set'], frozenset)
    assert isinstance(args['dict'], ImmutableDict) or isinstance(args['dict'], ImmutableDict)

    assert args['list'] == (1, 2)
    assert args['set'] == frozenset

# Generated at 2022-06-13 16:03:05.967334
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test GlobalCLIArgs constructor

    :return: True if the test is successful
    :rtype: bool
    """
    # The following code would be the equivalent of:
    #   class A(GlobalCLIArgs):
    #       def __init__(self, mapping):
    #           super(A, self).__init__(mapping)
    #       @property
    #       def foo(self):
    #           return self['foo']
    #       @property
    #       def bar(self):
    #           return self['bar']
    #       @property
    #       def baz(self):
    #           return self['baz']
    #       @property
    #       def password(self):
    #           return self['password']
    #       @property
    #       def foobar(self):

# Generated at 2022-06-13 16:03:12.467588
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Test that an exception gets thrown when we try to add a second class with the same metaclass
    class TestABCSingletonClass(object):
        __metaclass__ = _ABCSingleton
    try:
        class TestABCSingletonClass2(object):
            __metaclass__ = _ABCSingleton
        assert False, "Should not be able to create two classes with the same metaclass"
    except TypeError:
        pass



# Generated at 2022-06-13 16:03:17.687517
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'a': 1})
    assert args['a'] == 1
    with pytest.raises(TypeError):
        args['a'] = 2
        args.update({'b': 2})
        args.__setitem__('b', 2)
    assert args['a'] == 1
    assert 'b' not in args

# Generated at 2022-06-13 16:03:27.107860
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    import argparse
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play import Play

    class TestGlobalCLIArgs(unittest.TestCase):
        def test_init_args(self):
            parser = argparse.ArgumentParser()
            parser.add_argument('-v')
            options = parser.parse_args([])
            args = GlobalCLIArgs.from_options(options)
            self.assertIsInstance(args, GlobalCLIArgs)

    def test_immutable_string(self):
        args = GlobalCLIArgs({'foo': 'foo'})

# Generated at 2022-06-13 16:03:38.849401
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict

    # Make a dict with a dict in it
    d = dict(a=dict(b='c'))
    # Create a CLIArgs object using the dict as input
    c = CLIArgs(d)
    # Test that the dict was replaced with an ImmutableDict
    assert isinstance(c['a'], ImmutableDict)

    # Test with a dict with a list in it
    d = dict(a=dict(b=['c']))
    # Create a CLIArgs object using the dict as input
    c = CLIArgs(d)
    # Test that the list was replaced with a tuple
    assert isinstance(c['a']['b'], tuple)

    # Test with a dict with a set in it

# Generated at 2022-06-13 16:03:51.186872
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:03:53.949892
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(metaclass=_ABCSingleton):
        pass
    X.__init__ = lambda self, *args: None
    assert X() is X()

# Generated at 2022-06-13 16:04:02.018062
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class cls0(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            self.a = 1
    class cls1(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            self.a = 2

    x = cls0()
    y = cls0()
    z = cls1()
    assert x is y
    assert x.a == y.a
    assert x.a != z.a

# Generated at 2022-06-13 16:04:10.728446
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", action='store_true')
    parser.add_argument("--bar", action='store_true')
    args = parser.parse_args([])
    global_cli_args1 = GlobalCLIArgs.from_options(args)
    global_cli_args2 = GlobalCLIArgs.from_options(args)
    assert id(global_cli_args1) == id(global_cli_args2)

    # Make sure that we can't accidentally change the global args in a way that will affect other tests
    args.foo = True
    global_cli_args3 = GlobalCLIArgs.from_options(args)
    assert id(global_cli_args1) == id(global_cli_args3)

# Generated at 2022-06-13 16:04:14.259320
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'test': 'value'}
    cliargs = CLIArgs(args)
    assert cliargs['test'] == args['test']


# Generated at 2022-06-13 16:04:21.846695
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Check that we use ImmutableDict for non-container types.
    assert isinstance(CLIArgs({'a': 'b'}), ImmutableDict)
    # Check that we convert nested containers to immutable types
    cli_args = {'a': 'b',
                'c': {'d': 'e'},
                'f': ['g', {'h': 'i'}],
                'j': ['k', 'l']
                }
    cli_args_copy = cli_args.copy()
    new_cli_args = CLIArgs(cli_args)
    assert cli_args == cli_args_copy
    assert cli_args != new_cli_args
    assert isinstance(new_cli_args, ImmutableDict)

# Generated at 2022-06-13 16:04:27.292723
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'a': 1, 'b': 2, 'c': {'d': 4}}
    cli_args = CLIArgs(args)

    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args['c'], ImmutableDict)
    assert cli_args['c']['d'] == 4

# Generated at 2022-06-13 16:04:29.532433
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs()
    assert global_cli_args is GlobalCLIArgs()
    assert global_cli_args

# Generated at 2022-06-13 16:04:33.134063
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonTest(GlobalCLIArgs):
        def __init__(self):
            pass

    assert(ABCSingletonTest() is ABCSingletonTest())
    assert(ABCSingletonTest() is not GlobalCLIArgs())

# Generated at 2022-06-13 16:04:37.559909
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class First(_ABCSingleton):
        """
        Test the first call to create a _ABCSingleton
        """
        def __init__(self):
            pass

    class Second(_ABCSingleton):
        """
        Test the second call to create a _ABCSingleton
        """
        def __init__(self):
            pass

    first = First()
    second = Second()
    assert first is second

# Generated at 2022-06-13 16:04:46.376620
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(object):
        __metaclass__ = _ABCSingleton

    a = _ABCSingletonTest()
    b = _ABCSingletonTest()
    del a
    del b

# Generated at 2022-06-13 16:04:50.733538
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A_ABCMeta(object):
        __metaclass__ = ABCMeta

    class A_ABCSingleton(object):
        __metaclass__ = _ABCSingleton

    A_ABCMeta()
    A_ABCSingleton()

# Generated at 2022-06-13 16:04:55.995976
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class TestOptions:
        def __init__(self):
            self.host_key_checking = True
            self.tree = [{'first': "value"}]

    test_options = TestOptions()
    cli_args = GlobalCLIArgs.from_options(test_options)

    assert cli_args.get('host_key_checking') is True
    assert isinstance(cli_args['tree'][0], ImmutableDict)

# Generated at 2022-06-13 16:05:01.313955
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Set up the objects needed for creating a valid CLIArgs object
    class MockOptions(object):
        pass

    mock_options = MockOptions()
    mock_options.test_arg = 'baz'

    # Create the CLIArgs object
    cli_args = CLIArgs.from_options(mock_options)

    # Ensure it is immutable and has the correct value
    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args['test_arg'] == 'baz'

# Generated at 2022-06-13 16:05:05.653099
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    assert GlobalCLIArgs.__bases__[0] == CLIArgs
    assert issubclass(GlobalCLIArgs, Singleton)
    gca = GlobalCLIArgs.from_options(optparse.Values({}))
    assert gca == {}

# Generated at 2022-06-13 16:05:08.959575
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _Class1(object):
        __metaclass__ = _ABCSingleton
    class _Class2(object):
        __metaclass__ = _ABCSingleton
    assert id(_Class1) == id(_Class2)

# Generated at 2022-06-13 16:05:10.580182
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(_ABCSingleton):
        pass

    assert TestABCSingleton() is TestABCSingleton()

# Generated at 2022-06-13 16:05:15.343274
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.z = {}

    options = Options(1, 2)
    g = GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:05:25.081405
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    import ansible.module_utils.common.collections

    # Initialize GlobalCLIArgs()
    gca = GlobalCLIArgs({})

    # Make a copy of GlobalCLIArgs()
    gca2 = GlobalCLIArgs(gca)

    # Make sure the copy is the same as the one we started with
    assert gca is gca2

    # It should be immutable
    with pytest.raises(ansible.module_utils.common.collections.ReadOnlyError) as execinfo:
        gca['foo'] = 1
    assert "cannot be modified" in str(execinfo.value)

# Generated at 2022-06-13 16:05:34.827371
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.six import PY2

    args = GlobalCLIArgs(vars(dict(verbosity=4)))
    if PY2:
        assert isinstance(args, ImmutableDict)
    else:
        assert isinstance(args, Mapping)
    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args, CLIArgs)
    assert args['verbosity'] == 4
    # Creating a second GlobalCLIArgs should raise a TypeError
    try:
        another = GlobalCLIArgs(vars(dict(verbosity=4)))
    except TypeError:
        assert True
    else:
        assert False, 'Should not be able to create another instance of GlobalCLIArgs'

# Generated at 2022-06-13 16:05:52.170547
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(_ABCSingleton):
        pass
    TAS = TestABCSingleton()
    assert isinstance(TAS, TestABCSingleton)
    assert isinstance(TAS, _ABCSingleton)
    TAS.foo = 'bar'
    assert TAS.foo == 'bar'
    TAS.bar = 'foo'
    TABAS = TestABCSingleton()
    assert TABAS.foo == 'bar'
    assert TABAS.bar == 'foo'

    class TestABCMetaclass(ABCMeta):
        pass

    class TestABCSingleton2(_ABCSingleton, metaclass=TestABCMetaclass):
        pass

    TAS2 = TestABCSingleton2()
    assert isinstance(TAS2, TestABCSingleton2)

# Generated at 2022-06-13 16:06:03.221104
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.args import AnsibleOptions
    from ansible.utils.args import check_mutually_exclusive
    from ansible.utils.args import check_required_args
    from ansible.utils.args import check_required_if
    from ansible.utils.args import validate_file
    from ansible.utils.args import validate_conflicts
    from ansible.parsing.plugin_docs import read_docstring

    options = AnsibleOptions(
        connection='ssh',
        forks=10,
        module_path='/path/to/modules',
        become=False,
        become_method='sudo',
        become_user='root',
        check=False,
        diff=True,
        verbosity=3,
    )

    # Set mutually exclusive options and make sure they are set
    options.become

# Generated at 2022-06-13 16:06:14.904478
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import GlobalCLIArgs
    from ansible.module_utils.common.parameters import AnsibleSpecification
    from ansible.module_utils.common.text.converters import to_unicode


# Generated at 2022-06-13 16:06:18.382760
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Unit test for CLIArgs
    x = CLIArgs({'key1': 'value1'})
    assert len(x) == 1
    assert 'key1' in x

# Generated at 2022-06-13 16:06:22.355334
# Unit test for constructor of class CLIArgs
def test_CLIArgs():  # pylint: disable=function-redefined
    """
    Unit test for the CLIArgs class

    This function is used as a unit test of the CLIArgs constructor
    """
    test_dict = {'a': 'a'}
    assert isinstance(CLIArgs(test_dict), CLIArgs)

# Generated at 2022-06-13 16:06:32.994430
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from unittest.case import TestCase
    from types import MethodType
    from types import FunctionType
    from inspect import isfunction, ismethod, isclass

    class A(metaclass=_ABCSingleton):
        @classmethod
        def a(cls):
            return 0

    class B(A):
        @classmethod
        def b(cls):
            return 1

    # isclass(Something) can return True for instances of metaclasses
    assert isclass(A), "isclass(A) returned False"
    assert isclass(B), "isclass(B) returned False"

    # ismethod is true for instances of methods
    assert ismethod(B.b), "ismethod(B.b) returned False"
    assert ismethod(B.a), "ismethod(B.a) returned False"



# Generated at 2022-06-13 16:06:42.385033
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    aa = {'a': 1, 'b': [1, 2, 3, '4', {'c': 3}]}
    bb = {'b': frozenset([1, 2]),
          'c': 'c',
          'd': {'a': 'a', 'b': 'b', 'c': ['a', 'b', 'c']}}
    new_map = ImmutableDict(aa)
    new_map.update(bb)
    cli_args = CLIArgs(new_map)
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args['b'], frozenset)
    assert isinstance(cli_args['d'], ImmutableDict)
    assert isinstance(cli_args['d']['c'], tuple)
    assert cli_args

# Generated at 2022-06-13 16:06:53.741159
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import doctest
    from ansible.module_utils.six import PY2
    from ansible.module_utils.common import CLIARGS_REPLACED_BY_VARS

    # Skip doctests for python 2.6 as it does not support PEP 343 (with statement)
    if PY2 and doctest.register_optionflag('PY2_66'):
        doctest.skip_on(lambda: True, msg='python 2.6 does not support `with`')

    globs = globals()
    globs['CLIARGS_REPLACED_BY_VARS'] = CLIARGS_REPLACED_BY_VARS
    doctest.testmod(m=GlobalCLIArgs, globs=globs)

# Generated at 2022-06-13 16:06:56.688231
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    # We don't test the Singleton part, since it would require a trickier test
    assert A is B

# Generated at 2022-06-13 16:07:01.799330
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    some_dict = {'a': 1, 'b': (1, 2, 3)}
    some_args = CLIArgs(some_dict)
    assert(some_dict['b'][1] == 2)
    some_dict['b'] = 'four'
    assert(some_dict['b'] == 'four')
    assert(some_args['b'][1] == 2)
    assert(GlobalCLIArgs(some_dict) is GlobalCLIArgs(some_dict))

# Generated at 2022-06-13 16:07:24.794070
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = dict(B=4, A=3)
    assert GlobalCLIArgs(args) == GlobalCLIArgs(args)

# Generated at 2022-06-13 16:07:29.789347
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {}
    string = 'abc'
    sequence = ['a', 'b', 'c']
    mapping[string] = sequence
    result = CLIArgs(mapping)
    assert isinstance(result, CLIArgs)
    assert isinstance(result[string], tuple)
    assert isinstance(result, ImmutableDict)
    return result


# Generated at 2022-06-13 16:07:33.192568
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Ensure that we can import the _ABCSingleton class without errors
    """
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton

    assert A() is A()
    assert B() is B()

# Generated at 2022-06-13 16:07:36.546040
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        GlobalCLIArgs.__init__(GlobalCLIArgs({'key': 'value'}))
        assert False
    except TypeError:
        pass
    except:
        assert False

# Generated at 2022-06-13 16:07:43.401119
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        'host_key_checking': True,
        'style_test': 'style',
        'test_set': set(['foo', 'bar']),
        'test_list': [1, 2, 3],
        'test_dict': {
            'foo': 'bar',
            'frobbable': set([1, 2, 3, 'foo', 'bar']),
            'baz': [1, 2, 3]
        }
    }

# Generated at 2022-06-13 16:07:52.971323
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton
    # isinstance(A, B) will be True
    assert isinstance(A, B) == True
    # issubclass(A, B) will be True
    assert issubclass(A, B) == True
    b = B()
    # isinstance(a, B) will be True
    assert isinstance(A(), B) == True
    # issubclass(A, B) will be True
    assert issubclass(A, B) == True


# Generated at 2022-06-13 16:08:04.674490
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Create two classes that share a metaclass and should be able to override each other
    class A(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            self.var = 1

    class B(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            self.var = 2

    x = A()
    y = B()

    if x.var != 1:
        raise AssertionError("Failed to init x.var with class A")

    if y.var != 2:
        raise AssertionError("Failed to init y.var with class B")

    if x.var != 2:
        raise AssertionError("Failed to override x.var with class B")

    if y.var != 2:
        raise Assert

# Generated at 2022-06-13 16:08:14.740458
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Verify ImmutableDict functionality of GlobalCLIArgs

    This is a test of the constructor of GlobalCLIArgs and not the Singleton functionality of it.
    """
    import os

    # We can't just use vars(GlobalCLIArgs) because it will return a tmpdir.
    # We use vars(os) to test that ImmutableDict is working.
    test_args = vars(os)
    args = GlobalCLIArgs(test_args)

    for key in test_args:
        assert args[key] == test_args[key]
        assert isinstance(args[key], text_type)
        assert test_args[key] is not args[key]

    with pytest.raises(AttributeError):
        args.copy_class_docstrings = 'foo'

# Generated at 2022-06-13 16:08:23.811584
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', action='store', type=str, help='name of the person')
    parser.add_argument('--address', action='store', type=str, help='address of the person')

    args, sys.argv = sys.argv[:1], sys.argv[1:]
    options = parser.parse_args(args)
    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args is GlobalCLIArgs()
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args, Mapping)
    assert isinstance(cli_args, Sequence)
    assert not isinstance(cli_args, Set)



# Generated at 2022-06-13 16:08:32.901489
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options = {'a': 1, 'b': '2'}
    global_cli_args = GlobalCLIArgs.from_options(options)
    assert not isinstance(global_cli_args['a'], Mapping)
    assert not isinstance(global_cli_args['a'], Set)
    assert not isinstance(global_cli_args['a'], Sequence)
    assert not isinstance(global_cli_args['b'], Mapping)
    assert not isinstance(global_cli_args['b'], Set)
    assert not isinstance(global_cli_args['b'], Sequence)

    a = 1
    b = '2'
    options = {'a': a, 'b': b}
    global_cli_args = GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:09:19.711578
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    c = CLIArgs({"a": 1, "b": "2"})
    assert c.a == 1
    assert c.b == "2"
    assert not hasattr(c, "c")


# Generated at 2022-06-13 16:09:29.483931
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'lambda_function': 'foo', 'dry_run': False})
    assert args['lambda_function'] is 'foo'
    assert args['dry_run'] is False

    args = GlobalCLIArgs({'lambda_function': {'foo': 'bar', 'baz': 'buz'}, 'dry_run': False})
    assert args['lambda_function']['foo'] is 'bar'
    assert args['lambda_function']['baz'] is 'buz'
    assert args['dry_run'] is False

    args = GlobalCLIArgs({'lambda_function': set(['foo', 'bar']), 'dry_run': False})
    assert ('foo' in args['lambda_function']) is True
    assert ('bar' in args['lambda_function']) is True