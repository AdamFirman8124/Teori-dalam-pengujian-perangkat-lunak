

# Generated at 2022-06-13 15:59:39.061613
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    options = parser.parse_args([])
    args = GlobalCLIArgs.from_options(options)
    assert args['__opts__']


# Deprecation warning for module variable
__global_args = GlobalCLIArgs.from_options({})
__global_args['__ex_local__'] = False
__global_args['__ex_remote__'] = False
__global_args['__ex_local_only__'] = False
__global_args['__ex_remote_only__'] = False

# Generated at 2022-06-13 15:59:45.617698
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import copy
    import types


# Generated at 2022-06-13 15:59:48.849960
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        class SingletonChecker(object):
            __metaclass__ = _ABCSingleton

    except TypeError:
        assert False, 'Error in class _ABCSingleton'
    else:
        assert True

# Generated at 2022-06-13 15:59:50.702917
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(_ABCSingleton, Singleton)
    assert issubclass(_ABCSingleton, ABCMeta)

# Generated at 2022-06-13 15:59:59.000543
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Unit test for constructor of class GlobalCLIArgs
    """
    from DummyCLIArgs import DummyCLIArgs
    dummyCLIArgs = DummyCLIArgs()
    dummyCLIArgs_dict = vars(dummyCLIArgs)
    globalCLIArgs_dict = vars(GlobalCLIArgs(dummyCLIArgs_dict))
    assert dummyCLIArgs_dict == globalCLIArgs_dict
    globalCLIArgs_dict['connection'] = 'test'
    dummyCLIArgs_dict['connection'] = 'test'

# Generated at 2022-06-13 16:00:06.681195
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import GlobalCLIArgs
    from collections import OrderedDict

    args = GlobalCLIArgs()

    # test __init__ of class GlobalCLIArgs
    assert isinstance(args, dict)
    assert isinstance(args, ImmutableDict)

    # test __init__ of super class ImmutableDict
    args = GlobalCLIArgs({'a':1, 'b':2, 'c':3})
    assert isinstance(args, dict)
    assert isinstance(args, ImmutableDict)
    assert isinstance(args, Mapping)
    assert isinstance(args, Sequence)
    assert not isinstance(args, Set)
    assert args['a'] == 1
    assert args['b'] == 2
    assert args['c'] == 3

    # test __setitem

# Generated at 2022-06-13 16:00:07.480938
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({})

# Generated at 2022-06-13 16:00:14.019102
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test the _ABCSingleton class

    Test to see if class _ABCSingleton is a metaclass as All classes that inherit from this class
    should be metaclasses.
    """
    class FOO(_ABCSingleton):
        pass

    class BAR(FOO):
        pass

    assert FOO.__class__.__name__ == '_ABCSingleton'
    assert isinstance(FOO(), _ABCSingleton)
    assert BAR.__class__.__name__ == '_ABCSingleton'

# Generated at 2022-06-13 16:00:20.632176
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class A(GlobalCLIArgs):
        def __init__(self, args, *args1, **kwargs1):
            super(A,self).__init__(args, *args1, **kwargs1)
    class B(GlobalCLIArgs):
        def __init__(self, args, *args1, **kwargs1):
            super(B,self).__init__(args, *args1, **kwargs1)

    A({"a": "b"})
    B({"a": "b"})
    A({"a": "c"}) # raises AssertionError
    A({"a": "c"}) # also raises AssertionError

# Generated at 2022-06-13 16:00:22.390838
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestObject(object):
        __metaclass__ = _ABCSingleton

    assert TestObject is TestObject.__class__()

# Generated at 2022-06-13 16:00:34.515019
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'foo': {'bar': 'baz', 'qux': 5}, 'connection': 'local', 'new': 'old'}
    cli_args = CLIArgs(args)
    assert cli_args['foo']['bar'] == 'baz'
    assert cli_args['foo']['qux'] == 5
    assert cli_args['connection'] == 'local'
    assert cli_args['new'] == 'old'
    assert cli_args == args
    assert cli_args != {'foo': {'bar': 'baz', 'qux': 5}, 'connection': 'local'}
    assert cli_args != {'foo': {'bar': 'baz', 'qux': 5}, 'connection': 'local', 'new': 'new'}



# Generated at 2022-06-13 16:00:38.073447
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs.from_options(ImmutableDict())
    assert obj == {}
    obj = GlobalCLIArgs.from_options(ImmutableDict(test='test'))
    assert obj == {'test': 'test'}

# Generated at 2022-06-13 16:00:46.060282
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'one': 1, 'two': 'deux', 'three': ['trois', 'tres', 'tres']})
    assert args == {'one': 1,
                    'two': 'deux',
                    'three': ('trois', 'tres', 'tres')
                    }
    assert set(args.keys()) == {'one', 'two', 'three'}
    assert set(args.items()) == {('one', 1),
                                 ('two', 'deux'),
                                 ('three', ('trois', 'tres', 'tres'))}
    assert set(args.values()) == {1, 'deux', ('trois', 'tres', 'tres')}
    assert args.get('one') == 1
    assert args.get('two') == 'deux'

# Generated at 2022-06-13 16:00:49.008440
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestMeta(object):
        __metaclass__ = _ABCSingleton

    TestMeta()

# Generated at 2022-06-13 16:01:00.603275
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from collections import OrderedDict
    from ansible.module_utils.common.collections import is_immutable
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.action import ActionBase
    from ansible.plugins.connection import ConnectionBase

    # Test with a complex dictionary

# Generated at 2022-06-13 16:01:04.159753
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.cli.arguments import options
    from ansible.utils.collection_plugins import cut_data

    args = CLIArgs.from_options(options)
    cut_data_value = cut_data(args, 'debug')
    assert(cut_data_value)

# Generated at 2022-06-13 16:01:13.725986
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Singleton:
        __metaclass__ = _ABCSingleton
        pass

    class Singleton2(Singleton):
        pass

    class Singleton3(Singleton2):
        pass

    class Singleton4(Singleton3, Singleton2):
        pass

    assert Singleton is Singleton
    assert Singleton is Singleton()
    assert Singleton2 is Singleton2()
    assert Singleton3 is Singleton3()
    assert Singleton4 is Singleton4()

    class NewSingleton(Singleton4):
        __metaclass__ = _ABCSingleton
        pass

    assert NewSingleton is NewSingleton()

# Generated at 2022-06-13 16:01:16.140563
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # successful setup
    args = GlobalCLIArgs({'foo': 'bar', 'hello': 'world'})
    assert args['foo'] == 'bar'
    assert args['hello'] == 'world'

# Generated at 2022-06-13 16:01:18.861625
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = CLIArgs(dict(foo='bar'))
    global_args = GlobalCLIArgs(dict(foo='bar'))

    assert (args == global_args)


if __name__ == "__main__":
    # Unit test code
    test_GlobalCLIArgs()

# Generated at 2022-06-13 16:01:29.498921
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest

    class TestGlobalCLIArgs(unittest.TestCase):
        def test_can_set_global_cli_args_immutable(self):
            orig = {
                'k1': 'v1',
                'k2': 'v2',
                'k3': {
                    'k3_1': 'v3_1',
                    'k3_2': 'v3_2',
                    'k3_3': {
                        'k3_3_1': 'v3_3_1',
                        'k3_3_2': 'v3_3_2',
                        'k3_3_3': 'v3_3_3'
                    },
                },
            }
            orig_copy = GlobalCLIArgs(orig)

# Generated at 2022-06-13 16:01:40.088565
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():  # pylint: disable=too-few-public-methods
    """
    Ensure that _ABCSingleton is a valid metaclass using Singleton as a base
    """

    class Foo(object):
        """
        Fake class to satisfy __init__ test
        """
        def __init__(self, arg):
            self.arg = arg

    class Bar(Foo):
        """
        Fake class to satisfy __init__ test
        """
        __metaclass__ = _ABCSingleton

    class Test(object):
        """
        Fake class to satisfy __init__ test
        """
        def __init__(self):
            pass

    instance_of_foo = Foo(arg=4)
    assert instance_of_foo.arg == 4
    instance_of_bar = Bar(arg=5)
    assert instance_of

# Generated at 2022-06-13 16:01:49.330803
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Create a variable to hold the CLI options
    cli_opts = {}
    # Create the types we will test
    container_types = [
        ['test_str', 'This is a string'],
        ['test_int', 7],
        ['test_tuple', ('tuple_item1', 'tuple_item2')],
        ['test_list', ['list_item1', 'list_item2']],
        ['test_dict', {'dict_key1': 'dict_value1', 'dict_key2': 'dict_value2'}],
        ['test_set', {'set_item1', 'set_item2'}],
        ['test_list_dict', [
            {'test_dict': {'test_int': i}} for i in range(4)]],
    ]

# Generated at 2022-06-13 16:02:00.052396
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:08.058863
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class FakeOptions(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    foo = FakeOptions(foo=1)
    bar = FakeOptions(bar=2, something=foo)
    mapping = {'bar': bar}
    args = GlobalCLIArgs(mapping)

    assert args.bar.bar == 2
    assert args.bar.something.foo == 1

    try:
        args['bar'] = 3
        print(args)
    except Exception:
        pass
    else:
        assert False, 'Excepted TypeError on setting a value in the dictionary'

    try:
        args.bar.a_new_thing = 3
        print(args)
    except Exception:
        pass

# Generated at 2022-06-13 16:02:10.696487
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
    assert isinstance(TestClass(), TestClass)

# Generated at 2022-06-13 16:02:15.197593
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    _ABCSingleton has a constructor that doesn't do anything
    """
    class Test(object):
        pass
    class Testable(_ABCSingleton, Test):
        def __init__(self):
            Singleton.__init__(self)
            Test.__init__(self)
    test = Testable()
    assert isinstance(test, Testable)
    assert test is Testable()



# Generated at 2022-06-13 16:02:22.708523
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test that _ABCSingleton can be used for metaclass.

    This will fail if there is a problem combining the two metaclasses and will even fail on Python 2.7 if we
    are not careful.  Just a basic sanity check in case someone starts subclassing the Singleton directly instead
    of going through the _ABCSingleton.
    """

    class TestABCSingleton(metaclass=_ABCSingleton):
        pass

    test_singleton = TestABCSingleton()
    assert isinstance(test_singleton, TestABCSingleton)

# Generated at 2022-06-13 16:02:28.851950
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        pass

    class B(_ABCSingleton):
        def __init__(self, x=None):
            if x is not None:
                raise NotImplementedError("B has no __init__")

    class C(B, A):
        pass

    assert isinstance(A(), B)
    assert isinstance(C(), A)
    assert isinstance(C(), B)

    A.__init__ = lambda self: None

    assert isinstance(A(), C)

    class D(B):
        __doc__ = 'This is a bug in python 2.7, would be fixed in 2.7.16 if it was released.'
        def __init__(self):
            super(D, self).__init__()

    assert isinstance(D(), B)

# Generated at 2022-06-13 16:02:29.331004
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:02:32.791078
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = type('', (object,), {'hosts': 'localhost'})
    args = CLIArgs(vars(options))
    assert args['hosts'] == 'localhost'

# Generated at 2022-06-13 16:02:39.390549
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    x = A()
    y = A()

    assert x is y

# Generated at 2022-06-13 16:02:42.819111
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    assert A() is A()
    assert B() is B()
    assert A() is not B()

# Generated at 2022-06-13 16:02:48.824258
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    command_line = {"verbosity": 3, "verbosity": 3, "connection": "ssh"}
    cmd = CLIArgs(command_line)
    assert cmd == command_line
    assert isinstance(cmd, ImmutableDict)
    assert isinstance(cmd, Mapping)


# Generated at 2022-06-13 16:02:53.475197
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    def _get_attrs(cls):
        return sorted(set(dir(cls)) - set(dir(GlobalCLIArgs)))

    g1 = GlobalCLIArgs({'a': 1})
    g2 = GlobalCLIArgs({'a': 2})
    assert _get_attrs(g1) == _get_attrs(g2)

# Generated at 2022-06-13 16:02:56.380063
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyABCSingleton(_ABCSingleton):
        pass

    obj = MyABCSingleton()
    assert isinstance(obj, MyABCSingleton)



# Generated at 2022-06-13 16:03:05.681669
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.collections import is_immutable
    c = CLIArgs(dict(a=1, b=dict(c=1), d=dict(e=[dict(f=1), "foobar"])))
    assert c.a == 1
    assert c.b.c == 1
    assert c.d.e[0].f == 1
    assert c.d.e[1] == "foobar"
    assert isinstance(c.b, ImmutableDict)
    assert isinstance(c.d, ImmutableDict)
    assert isinstance(c.d.e[0], ImmutableDict)
    assert isinstance(c.d.e, tuple)
    assert is_immutable(c)

    # test a string conversion

# Generated at 2022-06-13 16:03:08.429650
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton
    class Bar(object):
        __metaclass__ = _ABCSingleton
    # These should be the exact same objects
    assert Bar() is Foo()



# Generated at 2022-06-13 16:03:11.036003
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    my_GlobalCLIArgs = GlobalCLIArgs.instance()
    assert isinstance(my_GlobalCLIArgs, GlobalCLIArgs)

# Generated at 2022-06-13 16:03:15.829852
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Check that we can't create more than one of them
    a = GlobalCLIArgs({'a': 1})
    try:
        b = GlobalCLIArgs({'b': 2})
        # If we got here, something broke
        assert False
    except TypeError as e:
        assert "Can't instantiate abstract class GlobalCLIArgs with abstract methods __new__" in str(e)
    assert a == b

# Generated at 2022-06-13 16:03:18.964194
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class BaseABCClass(object):
        __metaclass__ = ABCMeta

    class Foo(BaseABCClass, object):
        pass

    class Bar(BaseABCClass, object):
        pass

    class ABCSingletonTest(BaseABCClass):
        __metaclass__ = _ABCSingleton



# Generated at 2022-06-13 16:03:26.240658
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Meta(object):
        __metaclass__ = _ABCSingleton
    x = Meta()

# Generated at 2022-06-13 16:03:30.133404
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test for str
    assert CLIArgs({"a":"b"})["a"] == "b"

    # Test for dict
    assert CLIArgs({"a":{"b":"c"}})["a"]["b"] == "c"

    # Test for set
    assert CLIArgs({"a":set(["b"])})["a"] == frozenset({"b"})

    # Test for list
    assert CLIArgs({"a":["b"]})["a"] == ("b",)

# Generated at 2022-06-13 16:03:41.225885
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=invalid-name
    import ansible.constants as C
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.color import stringc

# Generated at 2022-06-13 16:03:43.710114
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo:
        __metaclass__ = _ABCSingleton
    assert isinstance(Foo(), Foo)

# Generated at 2022-06-13 16:03:47.076156
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(_ABCSingleton):
        pass

    class _ABCSingletonTest1(_ABCSingletonTest):
        pass

    class _ABCSingletonTest2(_ABCSingletonTest):
        pass

    assert _ABCSingletonTest1() is _ABCSingletonTest2()

# Generated at 2022-06-13 16:03:49.771348
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Ensure that an instance of _ABCSingleton can be created"""
    class _ABCSingletonTest(object):
        __metaclass__ = _ABCSingleton
    _ABCSingletonTest()

# Generated at 2022-06-13 16:03:51.487241
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    _ABCSingleton("ABC", (), {})

# Generated at 2022-06-13 16:03:54.345015
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestClass(object):
        pass
    assert not hasattr(_TestClass, 'instance')
    assert not hasattr(_TestClass, '__new__')

# Generated at 2022-06-13 16:03:58.999880
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        def __init__(self):
            self.fizz = "buzz"

    bar = Foo()
    baz = Foo()
    assert bar.fizz == "buzz"
    assert baz.fizz == "buzz"
    assert baz is bar

# Generated at 2022-06-13 16:04:09.164375
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(_ABCSingleton):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class _ABCTest(_ABCSingletonTest):
        pass

    class _SingletonTest(_ABCSingletonTest):
        pass

    class _SingletonTest2(_SingletonTest):
        pass

    _abc_singleton_test = _ABCSingletonTest(foo='bar')
    assert _abc_singleton_test.foo == 'bar'

    _abc_test = _ABCTest(foo='baz')
    assert _abc_test.foo == 'baz'

    _singleton_test = _SingletonTest(foo='biz')
    assert _singleton_test.foo == 'biz'


# Generated at 2022-06-13 16:04:30.950747
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object, metaclass=_ABCSingleton):
        pass

        # Add a member to the class to test that classes are not replaced
        # Should only exist on one class
        def __init__(self):
            self.new_attribute = True

    # Create singleton of Foo
    foo_singleton = Foo()
    assert hasattr(foo_singleton, 'new_attribute')

    # Create second class of Foo and test that it is a different instance
    foo2 = Foo()
    assert foo_singleton != foo2
    assert hasattr(foo2, 'new_attribute')

    # Create second singleton of Foo and test that it is the same singleton
    foo_singleton2 = Foo()
    assert foo_singleton is foo_singleton2
    assert hasattr(foo_singleton2, 'new_attribute')

# Generated at 2022-06-13 16:04:33.214340
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test = CLIArgs(dict(a=1, b=2))
    assert isinstance(test, ImmutableDict)
    assert test['a'] == 1



# Generated at 2022-06-13 16:04:42.323489
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        'ansible_become_user': 'root',
        'ansible_become': True,
        'ansible_become_method': 'sudo',
        'ansible_become_exe': '/usr/bin/sudo',
        'ansible_become_ask_pass': False,
    }
    args = CLIArgs(mapping)
    assert args.ansible_become_user == 'root'
    assert args.ansible_become == True
    assert args.ansible_become_method == 'sudo'
    assert args.ansible_become_exe == '/usr/bin/sudo'
    assert args.ansible_become_ask_pass == False

    # Make sure all keys are still present
    assert set(args.keys()) == set(mapping.keys())

    #

# Generated at 2022-06-13 16:04:53.992563
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:04:55.593406
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert _ABCSingleton('a', (), {'a': 0}) is _ABCSingleton('a', (), {'a': 0})

# Generated at 2022-06-13 16:04:58.296304
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ConcreteMeta(_ABCSingleton):
        pass

    class ConcreteClass(object, metaclass=ConcreteMeta):
        pass

    a = ConcreteClass()
    b = ConcreteClass()

    assert a is b

# Generated at 2022-06-13 16:05:02.865358
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    mapping = {
        "foo": "bar",
        "bar": [
            "foo",
        ]
    }
    cliargs = GlobalCLIArgs(mapping)
    assert cliargs["foo"] == "bar"

    # should not be able to change this
    try:
        cliargs["foo"] = "baz"
    except TypeError as e:
        assert e.args[0] == "object does not support item assignment"

    assert mapping["foo"] == "bar"

# Generated at 2022-06-13 16:05:07.003944
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():  # pylint: disable=missing-docstring
    args = GlobalCLIArgs({'debug': False, 'connection': 'local', 'diff': True})
    assert isinstance(args, GlobalCLIArgs)

# Generated at 2022-06-13 16:05:13.260667
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class FakeOptions:
        def __init__(self):
            self.a = "b"
            self.c = None

    obj = GlobalCLIArgs.from_options(FakeOptions())
    import pytest
    assert isinstance(obj, GlobalCLIArgs) is True
    assert isinstance(obj, CLIArgs) is True
    assert isinstance(obj, ImmutableDict) is True
    assert isinstance(obj, dict) is True
    with pytest.raises(AttributeError):
        obj.d = "e"

# Generated at 2022-06-13 16:05:22.280511
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.utils.unsafe_proxy

    opt = ansible.utils.unsafe_proxy.FakeOptions()
    opt.option_a = 'foo'
    opt.option_b = 'bar'
    opt.option_c = {'c1': 'c1v', 'c2': 'c2v', 'c3': {'c3a': 'c3av', 'c3b': 'c3bv'}}
    opt.option_d = (1, 2, 3)
    opt.option_e = None

# Generated at 2022-06-13 16:05:54.011446
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs.from_options({"a": "A", "b": "B", "c": "C"})

    # Make sure we're immutable
    try:
        a["d"] = "D"
    except KeyError as e:
        pass
    else:
        assert False, "Should have thrown a KeyError exception"
    try:
        del a["a"]
    except KeyError as e:
        pass
    else:
        assert False, "Should have thrown a KeyError exception"

    # Make sure we're a singleton
    b = GlobalCLIArgs.from_options({"a": "A", "b": "B", "c": "C"})
    assert a == b, "a and b should be equal but differ"

# Generated at 2022-06-13 16:05:56.686886
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton
    assert A() is A()

# Generated at 2022-06-13 16:05:59.807841
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    class Bar(object):
        __metaclass__ = _ABCSingleton

    assert Bar is not Foo

# Generated at 2022-06-13 16:06:01.754448
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass
    t = Test()
    assert t is Test()

# Generated at 2022-06-13 16:06:14.477760
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        my_key = 1
        my_key2 = 'a'

    my_options = Options()

    result = CLIArgs.from_options(my_options)
    assert isinstance(result, CLIArgs)
    assert isinstance(result, ImmutableDict)
    assert result['my_key'] == 1
    assert result['my_key2'] == 'a'

    mapping = {'my_key': 2, 'my_key3': (1, 2, 3)}
    result = CLIArgs(mapping)
    assert isinstance(result, CLIArgs)
    assert isinstance(result, ImmutableDict)
    assert result['my_key'] == 2
    assert result['my_key3'] == (1, 2, 3)
    result['my_key3'] += (4, 5) 

# Generated at 2022-06-13 16:06:25.537297
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        "one": 1,
        "two": ["a", "b"],
        "three": {"four": 4},
        "five": {},
        "six": [],
        "seven": {"eight":{"nine": {"ten": set()}}},
    }
    test_dict_immutable = _make_immutable(test_dict)

    cli_args = CLIArgs(test_dict)

    assert cli_args == test_dict_immutable
    assert cli_args["three"] == ImmutableDict({"four": 4})
    assert cli_args["seven"] == ImmutableDict({"eight": ImmutableDict({"nine": ImmutableDict({"ten": frozenset()})})})

# Generated at 2022-06-13 16:06:36.309011
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import datetime
    import pytz
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Create a singleton object manually and assert that it can not be instantiated again
    cli_args = GlobalCLIArgs({u"foo": u"bar"})
    assert cli_args == {u"foo": u"bar"}           # Can access items
    assert cli_args.get(u"foo") == u"bar"         # Can get items with get
    assert cli_args.get(u"baz") is None          # Can get non-existent items with get
    assert cli_args.get(u"baz", u"default") == u"default"  # Can get non-existent items with get and a default value

    # Copies are the same object
    cli_args2 = cli

# Generated at 2022-06-13 16:06:40.853311
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class AbcSingletonTest(_ABCSingleton):
        def __new__(mcs, name, bases, dct):
            return super(AbcSingletonTest, mcs).__new__(mcs)
    assert issubclass(AbcSingletonTest, Singleton)
    assert issubclass(AbcSingletonTest, ABCMeta)

# Generated at 2022-06-13 16:06:45.806756
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    my_args = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
    my_args_immutable = _make_immutable(my_args)
    my_cli_args = CLIArgs(my_args)
    assert my_cli_args == my_args
    assert id(my_cli_args) != id(my_args)
    assert isinstance(my_cli_args, ImmutableDict)
    assert id(my_cli_args) == id(my_args_immutable)

# Generated at 2022-06-13 16:06:49.571882
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Constructor of class CLIArgs

    Check sanity of input
    """

    options = ImmutableDict({'a': 1, 'b': 2})
    args = CLIArgs(options)
    assert args['a'] == 1
    assert args['b'] == 2

# Generated at 2022-06-13 16:07:43.448813
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:07:46.846730
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.constants as C

    global_args = GlobalCLIArgs({})
    assert C.DEFAULT_LOG_PATH in global_args.get('log_path', '')

# Generated at 2022-06-13 16:07:55.791722
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cls = CLIArgs({"a": 1, "b": {"c": {"d": 3}}, "e": [1, 2, 3]})
    assert isinstance(cls, ImmutableDict)
    assert isinstance(cls["a"], int)
    assert isinstance(cls["b"], ImmutableDict)
    assert isinstance(cls["b"]["c"], ImmutableDict)
    assert isinstance(cls["b"]["c"]["d"], int)
    assert isinstance(cls["e"], tuple)
    assert isinstance(cls["e"][0], int)
    assert isinstance(cls["e"][1], int)
    assert isinstance(cls["e"][2], int)

# Generated at 2022-06-13 16:07:59.497689
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton

    assert TestClass() is TestClass()
    assert isinstance(TestClass(), TestClass)


# Generated at 2022-06-13 16:08:02.242698
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class A(metaclass=_ABCSingleton):
        pass

    a = A()
    b = A()
    assert a is b, 'Both objects should be the same'

# Generated at 2022-06-13 16:08:04.865446
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonTestClass(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            pass
    ABCSingletonTestClass()

# Generated at 2022-06-13 16:08:14.944606
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test _ABCSingleton metaclass

    This is a metaclass that combines ABCMeta and Singleton.  So it should still allow you to define
    abstract, concrete, and abstract concrete methods.  You should also only be able to create one
    of these per program.
    """
    import abc
    from ansible.utils.singleton import SingletonException

    class TestMetaclassBase:
        """
        Example base class to use with _ABCSingleton
        """
        __metaclass__ = _ABCSingleton

        @abc.abstractmethod
        def test_abstract(self):
            pass

        def test_concrete(self):
            pass

        @abc.abstractmethod
        def test_abstract_concrete(self):
            pass


# Generated at 2022-06-13 16:08:22.151842
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_cli_args = {'foo': ['bar'], 'zar': {'zar1': 'zar2'}, 'zar3': [{'zar3-1': 'zar3-2'}, {'zar3-1': 'zar3-3'}]}

    result = CLIArgs(test_cli_args)

    assert result.get('zar')['zar1'] == 'zar2'
    assert result.get('zar3')[0]['zar3-1'] == 'zar3-2'
    assert result.get('zar3')[1]['zar3-1'] == 'zar3-3'

# Generated at 2022-06-13 16:08:25.912344
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'a': 1,
                          'b': (1, 'abc', ['cd', 12, {'e': 'fg'}])})
    assert args['a'] == 1
    assert args['b'][1] == 'abc'
    assert args['b'][2][2]['e'] == 'fg'



# Generated at 2022-06-13 16:08:29.639496
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton
    a = A()
    b = B()
    assert a is b

