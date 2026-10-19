

# Generated at 2022-06-13 15:59:35.258494
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton
        pass

    t1 = Test()
    t2 = Test()
    assert t1 == t2
    assert t1 is t2

# Generated at 2022-06-13 15:59:37.059958
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        pass

    assert isinstance(A(), A)
    assert A() is A()

# Generated at 2022-06-13 15:59:37.698026
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 15:59:40.536978
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SomeABC(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(SomeABC, Singleton)
    assert '__abstractmethods__' in SomeABC.__dict__
    # Make sure we can create an instance of the class.
    assert isinstance(SomeABC(), SomeABC)
    # Make sure we can create only one instance of the class.
    assert SomeABC() is SomeABC()

# Generated at 2022-06-13 15:59:44.947498
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli import CLI
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import fragment_loader
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.vars import combine_hash
    from ansible.vars import load_extra_vars as load_extra_vars1
    from ansible.vars import load_options_vars
    from ansible.vars import load_post_validate_vars
    from ansible.vars import load_yaml_config_file

# Generated at 2022-06-13 15:59:54.277658
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 15:59:56.115814
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    assert A() is A()

# Generated at 2022-06-13 16:00:01.831451
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(_ABCSingleton):
        def __init__(self, an_arg):
            self.an_arg = an_arg

    class TestSomeOtherName(_ABCSingleton):
        pass

    instance1 = TestABCSingleton('hello')
    instance2 = TestABCSingleton('goodbye')

    assert instance1.an_arg == 'hello'
    assert instance2.an_arg == 'hello'

    instance3 = TestSomeOtherName()
    assert instance3 is instance1

# Generated at 2022-06-13 16:00:10.642687
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from types import ModuleType
    from collections import OrderedDict

    class SingletonABC(GlobalCLIArgs):
        pass

    # Verify that modules references in the `mro()` are of type Module
    for base in SingletonABC.mro():
        if base is not SingletonABC:
            assert isinstance(base, (type, ModuleType))

    assert SingletonABC.__bases__ == (GlobalCLIArgs,)
    assert SingletonABC.__class__ == type
    assert SingletonABC.__doc__ is None
    assert SingletonABC.__dict__ == OrderedDict()
    assert SingletonABC.__mro__ == (SingletonABC, GlobalCLIArgs, ImmutableDict, object)
    assert SingletonABC.__name__ == 'SingletonABC'
    assert SingletonABC.__subclasses__()

# Generated at 2022-06-13 16:00:15.897872
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test making a GlobalCLIArgs object
    """
    x = GlobalCLIArgs({'a': 1, 'b': 2, 'c': 3})
    assert x['a'] == 1
    assert x['b'] == 2
    assert x['c'] == 3



# Generated at 2022-06-13 16:00:24.910157
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(metaclass=_ABCSingleton):
        my_val = None
        def __init__(self):
            if self.my_val is None:
                self.my_val = 'foo'

    class Bar(Foo):
        my_val = 'bar'

    assert Foo().my_val == 'foo'
    assert Bar().my_val == 'bar'

# Generated at 2022-06-13 16:00:26.495099
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        """A class to use for testing in test_docs."""

    a1 = A()
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:00:34.233822
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Unit test for constructor of class _ABCSingleton

    The purpose of this test is to highlight the behavior of the _ABCSingleton class and the
    differences between it and a regular Python Singleton class.  This class cannot be unit tested
    via a traditional way because it uses the metaclass _ABCSingleton, which requires that the class
    be declared as the type of a metaclass
    """
    class BaseClass(object):
        pass

    class ChildClassA(BaseClass):
        pass

    class ChildClassB(BaseClass):
        pass

    class GrandChildClass(ChildClassA, ChildClassB):
        pass

    class TestClassA(BaseClass):
        pass

    class TestClassB(BaseClass):
        pass

    class TestClassC(BaseClass):
        pass


# Generated at 2022-06-13 16:00:43.634909
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import unittest
    class GlobalCLIArgsTest(unittest.TestCase):
        def test_constructor(self):
            class FakeOptions(object):
                def __init__(self, mapping):
                    self.__dict__ = mapping
            flags = {
                'verbosity': 1,
                'private_key_file': '~/this_is_a_path.pem',
                'foo': 'bar'
            }
            options = FakeOptions(flags)
            args = GlobalCLIArgs.from_options(options)
            self.assertIsInstance(args, CLIArgs)
            self.assertEqual(args['verbosity'], 1)
            self.assertEqual(args['private_key_file'], '~/this_is_a_path.pem')

# Generated at 2022-06-13 16:00:44.805949
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class test_class(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(test_class, Singleton)

# Generated at 2022-06-13 16:00:56.522421
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict
    import types
    import sys
    import re

    if sys.version_info[0] >= 3:
        reload_module = types.ModuleType.reload
    else:
        reload_module = reload

    reload_module(GlobalCLIArgs)
    singleton_methods = ['__call__', '__deepcopy__', '__init__', '__reduce_ex__', '__repr__', '__reduce__', '__new__',
                         '__str__']
    if sys.version_info[0] >= 3:
        singleton_methods.append('__getnewargs_ex__')
    else:
        singleton_methods.append('__getnewargs__')

    # Validate that there are only the expected methods

# Generated at 2022-06-13 16:01:02.594869
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(A):
        pass
    def foo():
        class C(A):
            pass
    try:
        foo()
    except AssertionError as e:
        pass
    else:
        raise AssertionError('AssertionError not raised')
    a = A()
    b = B()

# Generated at 2022-06-13 16:01:05.389291
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class TestClass(_ABCSingleton):
        pass

    class TestClass2(TestClass):
        pass

    assert TestClass() is TestClass()
    assert TestClass2() is TestClass2()
    assert TestClass() is not TestClass2()

# Generated at 2022-06-13 16:01:10.401665
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    # Create two instances, should be the same instance
    t1 = Test()
    t2 = Test()
    assert t1 is t2
    assert isinstance(t1, object)

# Generated at 2022-06-13 16:01:18.148443
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Mapping to put into CLIArgs
    test_dict = {"testa": "testa", "testb": "testb"}

    test_dict["c"] = {"c1": "c1", "c2": "c2"}
    test_dict["c"]["c3"] = {"c4": "c4"}
    test_dict["d"] = {"d1": "d1", "d2": "d2"}
    test_dict["d"]["d3"] = {"d4": "d4"}

    test_dict["e"] = ["e1", "e2", "e3"]
    test_dict["e"][2] = ["e4", "e5", "e6"]
    test_dict["e"][2][2] = ["e7", "e8", "e9"]
    test

# Generated at 2022-06-13 16:01:32.415082
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from collections import OrderedDict
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    # OrderedDict so we can test __eq__ in order
    test_dict = OrderedDict((('key1', 'value1'),
                             ('key2', to_bytes('value2')),
                             ('key3', to_text('value3')),
                             ('key4', {'dict_key': [1, 2, 3]}),
                             ('key5', (1, 2, 3)),
                             ('key6', frozenset((1, 2, 3))),
                             ('key7', ImmutableDict({'item1': 1, 'item2': 2, 'item3': 3}))))
    cli_args = CLIArgs(test_dict)


# Generated at 2022-06-13 16:01:38.037954
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options():
        pass

    options = Options()
    options.debug = "yes"
    options.verbose = True
    options.test = [1,2,3]
    options.foo = {"bar": "baz"}
    options.dict = {"foo": "bar", "foobar": {"bar": "foo", "foo": "bar"}}
    options.list = [1,2,3, [1,2,3]]

    args = CLIArgs.from_options(options)

    # no longer a dict
    assert type(args) is not dict

    # dict-like
    assert args.get('debug') == "yes"
    assert args['verbose']

    assert args.get('not_a_real_option') == None

# Generated at 2022-06-13 16:01:40.687142
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    a1 = A()
    a2 = A()

    assert a1 is a2

# Generated at 2022-06-13 16:01:41.712276
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs()



# Generated at 2022-06-13 16:01:48.819366
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display

    # A basic test which is an exact copy of the Display class's test
    d = Display()
    assert isinstance(d, Display)

    d = Display(verbosity=5, log_only=True, log_path='/tmp/log.txt')
    assert isinstance(d, Display)

    # This should fail as we are trying to set a variable that isn't allowed
    try:
        d = Display(this_should_fail='always')
    except Exception:
        pass
    else:
        assert False, 'ImmutableDict should have failed'

# Generated at 2022-06-13 16:01:53.523385
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test if CLIArgs class successfully uses implicit defined constructor
    """
    a = {"a": "a", "b": "b"}
    cliArgs = CLIArgs(a)
    assert cliArgs["a"] == "a"
    assert cliArgs["b"] == "b"



# Generated at 2022-06-13 16:01:56.722511
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.cli
    globalcliargs = GlobalCLIArgs.from_options(ansible.cli.CLI.base_parser(None, None, ['-M', '/foo', '-vvvv']))
    pass

# Generated at 2022-06-13 16:02:04.492407
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=redefined-outer-name
    import sys
    from ansible.module_utils.common.arguments import _ensure_keys
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import Mock, patch

    # This fake options object has the same fields that the Ansible Options object has.  If
    # we add any more fields to Ansible Options, we need to add them here.
    class FakeOptions(object):
        """Fake options object"""
        # pylint: disable=too-few-public-methods
        def __init__(self):
            self.extra_vars = None
            self.forks = None
            self.become_user = None
            self.module_path = None
            self.become = None
           

# Generated at 2022-06-13 16:02:14.421112
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:19.218693
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'hello': 'world', 'nested': [{'mykey': 'myvalue'}, {'mykey': 'othervalue', 'boolean': False}]}
    assert args == CLIArgs(args)


# Unit tests for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:26.070355
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    assert A() is A()
    assert B() is A()
    assert C() is A()
    assert D() is A()

# Generated at 2022-06-13 16:02:28.595862
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options():
        test2 = 2
    options = Options()
    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args == {"test2": 2}
    return cli_args

if __name__ == '__main__':
    print("This file is supposed to be included in other files, not run directly")

# Generated at 2022-06-13 16:02:40.092459
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'hosts': {'host1': {'hostname': 'host1', 'vars': {'var1': 'value1', 'var2': {'value2': 2}}}}})
    assert args['hosts']['host1']['hostname'] == 'host1'
    assert args['hosts']['host1']['vars']['var1'] == 'value1'
    assert args['hosts']['host1']['vars']['var2']['value2'] == 2
    try:
        args.append('foo')
        assert False
    except AttributeError:
        pass

# Generated at 2022-06-13 16:02:48.603589
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Create a 'mock' object for command line arguments
    from argparse import Namespace
    from collections import OrderedDict
    from ansible.module_utils.common._collections_compat import MutableMapping
    mapping = OrderedDict()
    mapping['inventory'] = Namespace()
    mapping['inventory'].host_list = ['test1', 'test2']
    mapping['inventory'].graph_filename = 'test'
    mapping['inventory'].source_plugins = ['test3']
    mapping['playbook'] = Namespace()
    mapping['playbook'].syntax = None
    mapping['playbook'].listhosts = None
    mapping['playbook'].listtags = None
    mapping['playbook'].listtasks = None
    mapping['playbook'].step = None

# Generated at 2022-06-13 16:02:56.809878
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Precondition, these would be initialized by the time we get here.
    assert GlobalCLIArgs() is not None
    assert GlobalCLIArgs() is GlobalCLIArgs()


# Generated at 2022-06-13 16:03:06.027369
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import pytest

    assert GlobalCLIArgs is GlobalCLIArgs()

    class MutableSet(collections.UserSet):
        def add(self, value):
            super(MutableSet, self).add(value)

    # Check that subclassing actually works
    class MyGlobalCLIArgs(GlobalCLIArgs):
        pass

    # Check that subclassing actually works
    class MyCLIArgs(CLIArgs):
        pass

    class MyMutableCLIArgs(CLIArgs):
        def __init__(self, mapping):
            super(MyMutableCLIArgs, self).__init__(mapping)

        def __setitem__(self, key, value):
            if not hasattr(self, "_mutable_dict"):
                self._mutable_dict = dict(self)
            self._

# Generated at 2022-06-13 16:03:07.548828
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli import CLI
    cli = CLI()
    options = cli.parse()
    cli_args = GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:03:12.776627
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert(len(A.__instance) == 0)
    A()
    A()
    assert(len(A.__instance) == 1)
    a = A()
    a.a = 1
    assert(A().a == a.a)



# Generated at 2022-06-13 16:03:19.906326
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class FooBar(metaclass=_ABCSingleton):
        def __init__(self, val):
            self.val = val

    class Baz(metaclass=_ABCSingleton):
        def __init__(self, val):
            self.val = val

    assert FooBar.__name__ == 'FooBar'
    assert Baz.__name__ == 'Baz'
    assert FooBar(1).val == 1
    assert Baz(2).val == 2

# Generated at 2022-06-13 16:03:28.209703
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class MockOptions(object):
        def __init__(self):
            self.become_ask_pass = None
            self.become_method = 'become_method'
            self.become_password = 'become_password'
            self.become_username = 'become_username'
            self.check = True
            self.connection = 'connection'
            self.diff = True
            self.extra_vars = [
                'a:b',
                'c:d'
            ]
            self.follow = True
            self.force_handlers = True
            self.force_paging = True
            self.forks = 5
            self.inventory = 'inventory'
            self.listhosts = True
            self.listtasks = True
            self.module_path = 'module_path'


# Generated at 2022-06-13 16:03:36.687520
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({'foo': 'bar'})

# Generated at 2022-06-13 16:03:42.895024
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object):
        def __init__(self):
            self.foo = 42
            self.bar = dict(a=1, b=2)
            self.baz = (1, 2, 3)
            self.qux = set()
            self.quux = None

    options = Options()
    args = GlobalCLIArgs(vars(options))
    assert args['foo'] == 42, "foo is 42"
    assert args['bar']['a'] == 1 and args['bar']['b'] == 2, "bar is {'a': 1, 'b': 2}"
    assert args['baz'] == (1, 2, 3), "baz is (1, 2, 3)"
    assert args['qux'] == frozenset(), "qux is set()"

# Generated at 2022-06-13 16:03:48.538760
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    import json
    import ansible.utils.json_encoder as json_encoder
    import ansible.utils.json_loader as json_loader
    import ansible.module_utils.common.text as text

    # Use the json_* routines here to make sure we are checking the same thing.
    # We want to make sure that they can serialize/deserialize things that we
    # have marked as immutable.  This means ansible/ansible has not made any
    # assumptions about internals that we didn't know about.  In python3, json
    # can handle all of these, so we don't have to do anything different.

# Generated at 2022-06-13 16:03:49.838451
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyClass(object, metaclass=_ABCSingleton):
        pass

    assert type(MyClass) == _ABCSingleton



# Generated at 2022-06-13 16:03:54.920027
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        pass

    class S(A, _ABCSingleton):
        pass
    assert A in S.__mro__
    assert ABCMeta in S.__mro__
    assert Singleton in S.__mro__
    assert _ABCSingleton in S.__mro__



# Generated at 2022-06-13 16:04:02.437823
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object, metaclass=_ABCSingleton):
        pass

    class Bar(object, metaclass=_ABCSingleton):
        pass

    # Ensure that the metaclass is registered with ABCMeta
    assert(Bar.__abstractmethods__ is not Foo.__abstractmethods__)

    # Ensure that the metaclass allows the Singleton behavior
    assert(Bar() is Bar())
    assert(Foo() is Foo())
    assert(Foo() is not Bar())

# Generated at 2022-06-13 16:04:04.196920
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class _GlobalCLIArgs(GlobalCLIArgs):
        pass
    _GlobalCLIArgs({})

# Generated at 2022-06-13 16:04:07.876922
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        class _ABCSingletonTest(object):
            __metaclass__ = _ABCSingleton
    except AssertionError:
        # Purposely fail the test if we cannot make an instance of this class
        assert False, "Could not create an instance of _ABCSingleton"

# Generated at 2022-06-13 16:04:16.976883
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import mock
    from ansible.cli import CLICliOptions

    options = CLICliOptions()
    options = options.parse([])[1]
    myargs = GlobalCLIArgs.from_options(options)

    # Try to mutate and ensure that we throw an error
    with mock.patch('ansible.utils.immutable_types.ImmutableDict.__setitem__') as m:
        m.side_effect = TypeError()
        try:
            myargs['foo'] = 'bar'
            assert False
        except Exception:
            assert True
        else:
            assert False

# Generated at 2022-06-13 16:04:23.076960
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:04:38.932838
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    x = CLIArgs(dict(foo='bar'))
    assert isinstance(x, CLIArgs)
    assert x == dict(foo='bar')


# Generated at 2022-06-13 16:04:41.983814
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyClass(object):
        __metaclass__ = _ABCSingleton
    a = MyClass()
    b = MyClass()
    assert a is b
    assert a == b
    assert hash(a) == hash(b)

# Generated at 2022-06-13 16:04:51.793022
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test the CLIArgs class constructor."""
    # command line arguments; these are intentionally a mix of data types
    command_line_arguments = dict(
        foo="bar",
        baz=[1, 2, 3],
        bool=True,
        int=1,
        float=1.0,
        qux={"xyzzy": "foo"}
    )

    cli_args = CLIArgs(command_line_arguments)

    # make sure that no exception is raised when trying to modify
    # the CLIArgs object
    try:
        cli_args["foo"] = "quux"
    except TypeError:
        pass

# Generated at 2022-06-13 16:05:00.225071
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    x = {'y': {'z': {'a': 'b'}, 'c': 'd'}}
    x = CLIArgs(x)
    assert x == {'y': {'z': {'a': 'b'}, 'c': 'd'}}

    x = {'y': {'z': {'a': 'b'}, 'c': 'd'}}
    x = CLIArgs(x)
    assert x == {'y': {'z': {'a': 'b'}, 'c': 'd'}}

    x = {'y': {'z': {'a': 'b'}, 'c': 'd'}}
    x = CLIArgs(x)
    assert x == {'y': {'z': {'a': 'b'}, 'c': 'd'}}


# Generated at 2022-06-13 16:05:06.578874
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from ansible.module_utils.common.collections import MutableMapping
    class Foo(MutableMapping):
        __metaclass__ = _ABCSingleton
    class Bar(MutableMapping):
        __metaclass__ = _ABCSingleton

    Foo()
    Foo()
    try:
        Bar()
        assert(False)
    except TypeError:
        assert(True)


# Unit tests for methods of class CLIArgs

# Generated at 2022-06-13 16:05:15.736744
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():  # pylint: disable=unused-variable
    class SingletonMetaClass(_ABCSingleton):
        pass

    class SingletonClass(six.with_metaclass(SingletonMetaClass)):
        pass

    class SubclassedSingletonClass(SingletonClass):
        pass

    # Make sure new class can be created from metaclass
    #
    # If we weren't using Singleton, this would break
    assert issubclass(SingletonMetaClass, Singleton)
    #
    # If we weren't using ABCMeta, this would break
    assert issubclass(SingletonMetaClass, ABCMeta)
    #
    # If we weren't using type, the metaclass wouldn't be created properly
    # and this would break
    assert issubclass(SingletonClass, object)
    #
    # If we weren't using type

# Generated at 2022-06-13 16:05:26.928252
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:05:32.943448
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    # Supplying different arguments and ensure that we get an instance of the GlobalCLIArgs class
    args = (_ for _ in ()).throw(NotImplementedError())
    options = _make_immutable(args)
    cliargs = GlobalCLIArgs.from_options(options)

    assert isinstance(cliargs, GlobalCLIArgs)

# Generated at 2022-06-13 16:05:43.218131
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    # Create an instance of CollectionLoader and update its C paths, so we can import plugins
    # Since this is the first time we're instantiating the collection loader, it will also create a
    # session singleton.
    collection_loader = AnsibleCollectionLoader(ConfigYaml(), None, None, None)
    import ansible.plugins.loader

    # Import the module so it'll add itself to cli.CLIArgs but don't store the reference to it.
    # (This is a little hacky, but we only do it here so we can easily check if the module was
    # built into the CLIArgs object)
    import ansible.plugins.callback.log_plays
    del ansible.plugins.callback.log_plays

    # Instantiate a new instance of GlobalCL

# Generated at 2022-06-13 16:05:44.811143
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyTest(object):
        __metaclass__ = _ABCSingleton

    m1 = MyTest()
    m2 = MyTest()
    assert m1 is m2

# Generated at 2022-06-13 16:06:15.934855
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args_dict = {
        'connection': 'smart',
        'module_path': 'test_module',
        'forks': 100
    }
    cli_obj = CLIArgs(args_dict)
    assert cli_obj['connection'] == 'smart'
    assert cli_obj['module_path']  == 'test_module'
    assert cli_obj['forks']  == 100

# Generated at 2022-06-13 16:06:20.417054
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs.from_options({'test': 'test'})
    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args, dict)
    assert 'test' in args
    assert isinstance(args['test'], text_type)

# Generated at 2022-06-13 16:06:30.033975
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonType1(object):
        __metaclass__ = _ABCSingleton

    class SingletonType2(object):
        __metaclass__ = _ABCSingleton

    class NotSingletonType1(object):
        __metaclass__ = ABCMeta

    class NotSingletonType2(object):
        __metaclass__ = Singleton

    assert id(SingletonType1()) == id(SingletonType1())
    assert SingletonType1() is not SingletonType2()
    raise AssertionError("Not Singleton Type 1 should never be a singleton")

    raise AssertionError("Not Singleton Type 2 should never be a singleton")

# Generated at 2022-06-13 16:06:34.579271
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingleton_test(object):
        __metaclass__ = _ABCSingleton
    a = _ABCSingleton_test()
    b = _ABCSingleton_test()
    assert a is b
    if 'abc' in globals():
        def _test_abc(): del globals()['abc']
        _test_abc()

# Generated at 2022-06-13 16:06:39.068658
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Dummy(_ABCSingleton):
        pass

    def _functest(dupe):
        return dupe

    d1 = Dummy()
    d2 = Dummy()
    assert d1 == d2
    assert _functest(d1) == _functest(d2)

# Generated at 2022-06-13 16:06:43.230806
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    GlobalCLIArgs is a singleton class.
    The code below shows that even though we create two instances
    of type GlobalCLIArgs, these two instances refer to the same
    singleton object.
    """
    x = GlobalCLIArgs.from_options(dict())
    y = GlobalCLIArgs.from_options(dict(new=1))

    assert x == y

# Generated at 2022-06-13 16:06:51.111175
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({}) == ImmutableDict()
    assert CLIArgs({'foo': 'bar'}) == ImmutableDict({'foo': 'bar'})
    assert CLIArgs({'list': [1, 2]}) == ImmutableDict({'list': (1, 2)})
    assert CLIArgs({'dict': {'foo': 'bar'}}) == ImmutableDict({'dict': ImmutableDict({'foo': 'bar'})})
    assert CLIArgs({'set': {1, 2}}) == ImmutableDict({'set': frozenset({1, 2})})

# Generated at 2022-06-13 16:06:59.043494
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Check that we really are using the class _ABCSingleton correctly

    Check that our metaclass works the way we expect with Singleton and ABCMeta.
    """

    def abc_func():
        pass

    class TestABC(object):
        """Test class for checking the metaclass"""
        __metaclass__ = _ABCSingleton
        __abstractmethods__ = frozenset(['abc_func'])

        def abc_func(self):
            pass

    # Test that TestABC should not be an abstract class
    assert not TestABC.__subclasshook__(TestABC)
    assert not TestABC().abc_func()



# Generated at 2022-06-13 16:07:10.508382
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test for the conversion of a dict to ImmutableDict
    dict_test = {'test1': 1, 'test2': 2, 'test3_list': [1, 2, 3]}
    test_mutable = CLIArgs(dict_test)
    assert isinstance(test_mutable, ImmutableDict)
    # Test for conversion of a list to a tuple
    list_test = ['test1', 'test2', 'test3']
    test_mutable = CLIArgs({'list_test': list_test})
    assert 'list_test' in test_mutable
    assert isinstance(test_mutable['list_test'], tuple)
    # Test for conversion of a set to a frozenset
    set_test = {'test1', 'test2', 'test3'}
    test_mutable = CLIArgs

# Generated at 2022-06-13 16:07:12.961454
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Test(object):
        __metaclass__ = GlobalCLIArgs
    test_instance = GlobalCLIArgs()
    test_instance2 = GlobalCLIArgs()
    assert test_instance is test_instance2

# Generated at 2022-06-13 16:08:21.772121
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_args = CLIArgs({'foo': 'bar'})
    assert isinstance(cli_args, CLIArgs)
    assert cli_args == {'foo': 'bar'}
    assert cli_args['foo'] == 'bar'
    with pytest.raises(KeyError):
        cli_args['bar']
    cli_args = CLIArgs(foo='bar')
    assert isinstance(cli_args, CLIArgs)
    assert cli_args == {'foo': 'bar'}
    assert cli_args['foo'] == 'bar'
    with pytest.raises(KeyError):
        cli_args['bar']
    cli_args = CLIArgs({'foo': ['bar', 'baz']})
    assert isinstance(cli_args, CLIArgs)
    assert cli_args

# Generated at 2022-06-13 16:08:28.741227
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        def __init__(self,**kw):
            self._dict = kw
        def __getattr__(self,name):
            return self._dict[name]
    opt = Options(
        diff='diff_value',
        check=True,
        test_name=[1,2,3],
        test_devices = { 1: {'disk': 'sda1'},
                         2: {'disk': 'sdb1'},
                         3: {'disk': 'sdc1'} })
    cliargs = CLIArgs.from_options(opt)
    assert isinstance(cliargs._store, ImmutableDict)
    assert cliargs['diff'] == 'diff_value'
    assert isinstance(cliargs['test_name'],tuple)

# Generated at 2022-06-13 16:08:30.841313
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    cli = GlobalCLIArgs({})
    assert cli is not None

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 16:08:36.674428
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # This is a class that we can instantiate from GlobalCLIArgs and be sure that we are now not
    # a singleton

    class NotASingleton(GlobalCLIArgs):
        pass

    singleton = GlobalCLIArgs()
    not_singleton = NotASingleton()

    if not isinstance(singleton, GlobalCLIArgs):
        raise RuntimeError("_ABCSingleton should have enforced singleton")

    if isinstance(not_singleton, GlobalCLIArgs):
        raise RuntimeError("_ABCSingleton should have enforced singleton")



# Generated at 2022-06-13 16:08:39.540493
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Require modifier for python2.7
    obj = CLIArgs({'a': 1, 'b': [2]})
    assert obj['a'] == 1
    assert obj['b'][0] == 2
    # This test is only valid via python3's concept of container and non-container types
    assert obj['b'] == (2,)

# Generated at 2022-06-13 16:08:47.773933
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.utils.listify import listify_lookup_plugin_terms

    def mock_module_utils_common_collections_ImmutableDict(mapping):
        return dict(mapping)


# Generated at 2022-06-13 16:08:50.295196
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    opt = GlobalCLIArgs({'a': 'b'})
    assert opt['a'] == 'b'


# Generated at 2022-06-13 16:09:00.770421
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    cli_args = CLIArgs.from_options(sys.modules['__main__'].options)
    assert isinstance(cli_args.module_name, str)
    assert isinstance(cli_args.module_path, str)
    assert isinstance(cli_args.module_args, (str, bytes, tuple))
    assert isinstance(cli_args.forks, int)
    assert isinstance(cli_args.become, bool)
    assert isinstance(cli_args.become_method, (str, bytes))
    assert isinstance(cli_args.become_user, (str, bytes))
    assert isinstance(cli_args.check, bool)
    assert isinstance(cli_args.diff, bool)
    assert isinstance(cli_args.verbosity, int)
    assert isinstance

# Generated at 2022-06-13 16:09:07.532241
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_args = GlobalCLIArgs({'foo': {'bar': 'baz', 'bat': 'boo'},
                                 'wiz': [{'blah': 'blah'}, {'meh': 'meh'}],
                                 'bam': 'egg',
                                 'zap': None})

    # Test that constructor correctly converted to immutable
    assert isinstance(global_args, ImmutableDict)
    assert isinstance(global_args['foo'], ImmutableDict)
    assert isinstance(global_args['wiz'], tuple)
    assert isinstance(global_args['wiz'][0], ImmutableDict)
    assert isinstance(global_args['wiz'][1], ImmutableDict)

    # Test that original data was left intact, raise exception to trigger failure

# Generated at 2022-06-13 16:09:17.243133
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar', 'bam': {'baz': [1, {'bam': [2, 3]}]}})
    assert args['foo'] == 'bar'
    assert args['bam']['baz'][0] == 1
    assert args['bam']['baz'][1]['bam'][0] == 2
    assert args['bam']['baz'][1]['bam'][1] == 3

    assert isinstance(args, ImmutableDict)
    assert isinstance(args['bam'], ImmutableDict)
    assert isinstance(args['bam']['baz'], tuple)
    assert isinstance(args['bam']['baz'][1], ImmutableDict)