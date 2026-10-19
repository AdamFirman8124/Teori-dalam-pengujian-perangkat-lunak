

# Generated at 2022-06-13 15:59:39.122658
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class DummyClass(object):
        """Just a class for _ABCSingleton testing"""
        pass

    assert DummyClass().__class__.__metaclass__.__name__ == 'ABCMeta'
    assert DummyClass().__class__.__name__ == 'DummyClass'

# Generated at 2022-06-13 15:59:45.666303
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_args = CLIArgs({})
    assert isinstance(cli_args, ImmutableDict)

    cli_args = CLIArgs({'a': 1, 'b': 2})
    assert isinstance(cli_args['a'], int)
    assert isinstance(cli_args['b'], int)
    assert cli_args['a'] == 1
    assert cli_args['b'] == 2

    #check that we did not turn the list into a tuple
    cli_args = CLIArgs({'a': {'b': [1, 2, 3]}})
    assert isinstance(cli_args['a'], ImmutableDict)
    assert cli_args['a']['b'] == [1, 2, 3]


# Generated at 2022-06-13 15:59:50.179170
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test GlobalCLIArgs constructor

    :return: None
    """
    args = ['-ansible-debug', '-vvvv']
    options = parser.parse_args(args)[0]
    mapped = vars(options)
    gca = GlobalCLIArgs(mapped)
    print(gca)
    assert gca['verbosity'] == 4
    assert gca['debug'] is True

if __name__ == '__main__':
    # GlobalCLIArgs is a singleton and we have not modified the singleton, so we should not be able
    # to create a new instance of it
    from ansible.module_utils.common.parameters import parser
    from ansible.utils.display import Display
    display = Display()
    display.display('testing display')
    test_GlobalCLIArgs()

# Generated at 2022-06-13 15:59:53.556249
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = vars(GlobalCLIArgs.from_options(None))
    assert isinstance(args, ImmutableDict)

# Generated at 2022-06-13 16:00:00.787183
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.utils.args import tup

    with pytest.raises(TypeError):
        i = GlobalCLIArgs(None)

    g1 = GlobalCLIArgs(dict(a=1))
    g2 = GlobalCLIArgs(dict(a=1))
    g3 = GlobalCLIArgs(dict(b=2))

    assert g1 == g2
    assert g1 == g1
    assert g1 != g3
    assert g1 != None

    assert GlobalCLIArgs.from_options(tup(['-a', '1'])) == g1

# Generated at 2022-06-13 16:00:10.188594
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.dict_transformations import _to_dict
    import collections as py_collections
    from ansible.module_utils.common.collections import _ImmutableDict

    import collections
    import json

    # We use an OrderedDict to ensure reproducibility in the test
    test_dict = collections.OrderedDict()
    test_dict["one"] = "string"
    test_dict["two"] = collections.OrderedDict()
    test_dict["two"]["six"] = "final string"
    test_dict["two"]["seven"] = py_collections.OrderedDict()
    test_dict["two"]["seven"]["eight"] = ['one', 'two', 'three']
    test_dict["two"]["seven"]["ninth"]

# Generated at 2022-06-13 16:00:11.879432
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(metaclass=_ABCSingleton):
        pass
    assert TestClass() is TestClass()

# Generated at 2022-06-13 16:00:13.730049
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = ImmutableDict(dict(a='A', b=2, c=[1, 2, 3]))
    args = CLIArgs(options)

    assert isinstance(args['a'], str)
    assert isinstance(args['b'], int)
    assert isinstance(args['c'], tuple)

# Generated at 2022-06-13 16:00:21.259887
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict
    a = CLIArgs({'foo': 123, 'bar': {'a': 1, 'b': 2, 'c': 3}, 'baz': [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]})
    assert isinstance(a['foo'], int)
    assert isinstance(a['bar'], ImmutableDict)
    assert isinstance(a['baz'], tuple)
    assert isinstance(a['baz'][0], ImmutableDict)
    assert isinstance(a['baz'][1], ImmutableDict)
    assert a['foo'] == 123
    assert a['bar']['a'] == 1
    assert a['bar']['b'] == 2

# Generated at 2022-06-13 16:00:27.246940
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonABCMeta(object):
        __metaclass__ = _ABCSingleton

    class ABCSingletonTest(SingletonABCMeta):
        pass

    class ABCSingletonTest2(SingletonABCMeta):
        pass

    assert ABCSingletonTest() == ABCSingletonTest()
    assert ABCSingletonTest() is ABCSingletonTest()
    assert ABCSingletonTest() is not ABCSingletonTest2()

# Generated at 2022-06-13 16:00:40.970337
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import tempfile
    import os


# Generated at 2022-06-13 16:00:43.134980
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingleton(object):
        __metaclass__ = _ABCSingleton
    # See Ansible PR #48886 for more details
    ABCSingleton()

# Generated at 2022-06-13 16:00:47.754054
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    import six

    class TestGlobalCLIArgs(unittest.TestCase):
        def setUp(self):
            self.testargs = ['testone=valueone', 'testtwo=valuetwo', 'testthree=valuethree', 'file=foobar.txt']

            self.testopts = {
                'testone': 'valueone',
                'testtwo': 'valuetwo',
                'testthree': 'valuethree',
                'file': ['foobar.txt'],
            }

        def test_construction(self):
            options = self._setup_options()
            args = GlobalCLIArgs(self.testopts)
            self.assertIsInstance(args, CLIArgs)
            self.assertEqual(args, self.testopts)


# Generated at 2022-06-13 16:00:59.955325
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:01:02.124710
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object, metaclass=_ABCSingleton):
        pass
    assert A() is A()



# Generated at 2022-06-13 16:01:03.176372
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    global_cli_args = GlobalCLIArgs({})

    # Should be a singleton
    assert global_cli_args is GlobalCLIArgs()

# Generated at 2022-06-13 16:01:04.873331
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    g = GlobalCLIArgs()
    assert g.args == {}

# Generated at 2022-06-13 16:01:10.659739
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass

    class Bar(_ABCSingleton):
        pass

    class Baz(Foo, Bar):
        pass

    assert isinstance(Baz(), Baz)

    class Quux(_ABCSingleton, Foo):
        pass

    assert isinstance(Quux(), Quux)

# Generated at 2022-06-13 16:01:17.693697
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    def test_setattr_on_GlobalCLIArgs_object(mapping):
        assert(isinstance(mapping, Mapping))
        global_cliargs = GlobalCLIArgs(mapping)
        try:
            global_cliargs.testattr = True
        except AttributeError:
            assert(True)
        else:
            assert(False)
        assert(not hasattr(global_cliargs, "testattr"))

    mapping1 = {'k1': 'v1', 'k2': 'v2', 'k3': {'k4': 'v4', 'k5': 'v5'}, 'k6': ('a', 'b', 'c')}
    test_setattr_on_GlobalCLIArgs_object(mapping1)

# Generated at 2022-06-13 16:01:28.201105
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _Test1(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, x):
            self.x = x

    class _Test2(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            super(_Test2, self).__init__(x=42)

    class _Test3(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            super(_Test3, self).__init__(x=42)
            self.x = 43

    class _Test4(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, x):
            self.x = x

    first = _Test1(42)
    second = _Test2()
    third

# Generated at 2022-06-13 16:01:33.240478
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton
    t1 = Test()
    t2 = Test()
    assert t1 is t2

# Generated at 2022-06-13 16:01:40.275744
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from copy import deepcopy
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import zip

    cli_args = {'test_boolean': True,
                'test_string': "I am a string",
                'test_list': ['a', 'list', 'of', 'strings']}
    mutable_dict = deepcopy(cli_args)
    immutable_dict = CLIArgs.from_options(ImmutableDict(mutable_dict))
    assert isinstance(immutable_dict, ImmutableDict)
    assert not isinstance(immutable_dict, dict)
    assert isinstance(immutable_dict['test_boolean'], bool)

# Generated at 2022-06-13 16:01:48.298054
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    dict = {'b': 'bar', 'a': 'foo', 'c': ['a', 'b', 'c'], 'd': [{'e': 'f'}], 'e': {'f': {'g': {'h': 'i'}}}}
    expected_dict = ImmutableDict({'b': 'bar', 'a': 'foo', 'c': ('a', 'b', 'c'), 'd': (ImmutableDict({'e': 'f'}),), 'e': ImmutableDict({'f': ImmutableDict({'g': ImmutableDict({'h': 'i'})})})})
    assert CLIArgs(dict).copy() == expected_dict

# Generated at 2022-06-13 16:01:52.832515
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {
        "foo": 0xfeedface,
        "bar": ["1", "2", 3, {"four": 4}],
        "baz": {"a": "A", "b": "B", "c": {"d": "D", "e": "E"}},
        "boo": {"x": "X", "y": "Y", "z": {"w": "W"}},
        "cow": {"x": "X", "y": "Y", "z": {"w": "W", "u": {"t": "T"}}}
    }
    global_args = GlobalCLIArgs(args)
    assert global_args["foo"] == args["foo"]
    assert global_args["bar"] == tuple(args["bar"])

# Generated at 2022-06-13 16:01:57.263080
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class x(object):
        __metaclass__ = _ABCSingleton
    class x2(object):
        __metaclass__ = _ABCSingleton

    x()
    try:
        x2()
    except TypeError as e:
        assert "can't instantiate abstract class" in str(e).lower()

# Generated at 2022-06-13 16:02:04.815755
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    x = {'foo': 'bar', 'baz': 1, 'list': [1, 2, 3], 'list2': ['a', 'b', 'c']}
    y = CLIArgs(x)
    assert y['foo'] == 'bar'
    assert y['baz'] == 1
    assert y['list'] == (1, 2, 3)
    assert y['list2'] == ('a', 'b', 'c')
    assert y.get('v') is None
    # this should fail
    try:
        y['test'] = 'test'
    except TypeError as e:
        assert "AttributeError: 'CLIArgs' object has no attribute 'test'" not in str(e)
        assert 'immutable' in str(e)
    # this should fail

# Generated at 2022-06-13 16:02:06.974054
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    raise NotImplementedError  # TODO: implement your test here

# Generated at 2022-06-13 16:02:16.242733
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.vars import combine_vars

    # test dict
    d = dict(a=1, b=2, c=3)
    # test list
    l = [dict(a=1), dict(b=2), dict(c=3)]
    # test string
    s = "foo"
    # test unicode
    u = u'\u00C5'
    # test combine_vars
    c = combine_vars(d, l)

    a = CLIArgs(mapping=d)
    assert isinstance(a, dict)
    assert a['a'] == 1

    b = CLIArgs(mapping=l)
    assert isinstance(b, dict)
    assert b['a'] == 1

    c = CLIArgs(mapping=s)

# Generated at 2022-06-13 16:02:27.023082
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test constructor of class CLIArgs
    test_args = {'debug': True, 'connection': 'winrm', 'module_path': '/opt/ansible/modules', 'forks': 8}
    test_args_dict = CLIArgs(test_args)
    assert test_args_dict['debug'] == True
    assert test_args_dict['connection'] == 'winrm'
    assert test_args_dict['module_path'] == '/opt/ansible/modules'
    assert test_args_dict['forks'] == 8

    test_args_list = [1, 2, 3]
    test_args_dict['test_list'] = test_args_list
    assert test_args_dict['test_list'] == (1, 2, 3)

    test_args_tuple = (4, 5, 6)
    test

# Generated at 2022-06-13 16:02:32.537701
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Can we instantiate _ABCSingleton class?
    """
    # This is a metaclass, so how do we test it?  Well, actually it is an abstract class so we don't
    # expect to be able to instantiate it.  If it doesn't throw an exception when we try to
    # instantiate it then it is a failure of this test.
    class Foo(_ABCSingleton):
        """
        Class to instantiate to test _ABCSingleton
        """
        pass
    instantiated = False
    try:
        Foo()
        instantiated = True
    except NotImplementedError:
        assert not instantiated

# Generated at 2022-06-13 16:02:37.341488
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(_ABCSingleton, ABCMeta)
    assert issubclass(_ABCSingleton, Singleton)

# Generated at 2022-06-13 16:02:40.195173
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli.arguments import options
    cli_args = CLIArgs.from_options(options)
    assert (GlobalCLIArgs(cli_args) == cli_args)

# Generated at 2022-06-13 16:02:44.853353
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options:
        def __init__(self):
            self.module_path = '/foo/bar'
            self.extra_vars = {'foo': 'bar', 'nested_dict': {'a': 'b', 'c': 'd'}}
            self.args = ['localhost', 'arg2', 'arg3']

    opt = Options()
    global_args = GlobalCLIArgs.from_options(opt)
    # GlobalCLIArgs is a singleton and so this is a noop
    # global_args = GlobalCLIArgs.from_options(opt)
    assert list(global_args.keys()) == ['module_path', 'extra_vars', 'args']
    assert isinstance(global_args['module_path'], text_type)

# Generated at 2022-06-13 16:02:55.571432
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test for CLIArgs"""

    # Create a CLIArgs object
    original = {'foo': [1, 2, 3], 'bar': 'baz', 'zoo': {'1': 1, '2': 2}}
    args = CLIArgs(original)

    # Make a deep copy
    expected = original.copy()

    # Assert the copy is immuable
    assert args == expected
    with pytest.raises(TypeError):
        args['something'] = 'other'
    with pytest.raises(TypeError):
        del args['zoo']
    with pytest.raises(TypeError):
        args['foo'].append(4)
    with pytest.raises(TypeError):
        del args['foo'][0]

# Generated at 2022-06-13 16:03:03.114417
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonMetaclass(_ABCSingleton):
        pass
    class A(metaclass=SingletonMetaclass):
        pass
    assert A() == A()
    assert isinstance(A.__mro__, tuple)
    assert A.__mro__[0] is A
    assert A.__mro__[1] is SingletonMetaclass
    assert A.__mro__[2] is object
    class B(metaclass=SingletonMetaclass, base=A):
        pass
    assert B() == B()
    assert isinstance(B.__mro__, tuple)
    assert B.__mro__[0] is B
    assert B.__mro__[1] is SingletonMetaclass
    assert B.__mro__[2] is object
    assert B.__

# Generated at 2022-06-13 16:03:07.500032
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=unused-variable
    global_cli_args = GlobalCLIArgs({'some': {'nested': {'data': 'one', 'more': 'two'}, 'data': 'one'}, 'data': 'one'})
    # pylint: enable=unused-variable

# Generated at 2022-06-13 16:03:17.527787
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'a': 1, 'b': 'one', 'c': {'d': 2, 'e': 'two'}}
    cli_args = CLIArgs(test_dict)
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args == test_dict
    assert cli_args['c'] == test_dict['c']
    assert cli_args['c']['e'] == test_dict['c']['e']

    test_list = [1, 2, 3.14, [4, 5, 6.18]]
    cli_args = CLIArgs(test_list)
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args == test_list
    assert cli_args[2] == test_list[2]

# Generated at 2022-06-13 16:03:22.891031
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # test should not raise an exception
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton
    class C(A):
        pass
    class D(B):
        pass
    class E(C, D):
        pass
    class F(E):
        pass

# Generated at 2022-06-13 16:03:25.417942
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(_ABCSingleton):
        pass

    first_instance = _ABCSingletonTest()
    second_instance = _ABCSingletonTest()

    assert first_instance is second_instance

# Generated at 2022-06-13 16:03:27.456806
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object, metaclass=_ABCSingleton):
        pass
    assert Foo() is Foo()

# Generated at 2022-06-13 16:03:42.799174
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert(CLIArgs({'a': 'foo'}) == {'a': 'foo'})

    args = CLIArgs.from_options(
        type('Options', (object,), {'a': 'foo', 'b': [1, 2, 3], 'c': {'d': [{'e': 'f'}]}})
    )

    assert(args == {'a': 'foo', 'b': (1, 2, 3), 'c': ImmutableDict({'d': ((ImmutableDict({'e': 'f'}),),)})})

    args = CLIArgs({'a': 'foo', 'b': [1, 2, 3], 'c': {'d': [{'e': 'f'}]}})

# Generated at 2022-06-13 16:03:45.991000
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Check the interface of class GlobalCLIArgs
    """

    global_cliargs = GlobalCLIArgs.instance(None)
    assert isinstance(global_cliargs, GlobalCLIArgs)

# Generated at 2022-06-13 16:03:53.723890
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test the CLIArgs constructor"""
    fake_args = {
        'a_text_argument': 'foo',
        'a_number_argument': 42,
        'a_bool_argument': True,
        'an_argument_with_default': 'bar',
        'a_list_argument': [1, 2, 3],
        'a_collection_argument': set((1, 2, 3)),
        'a_dict_argument': {'foo': 'bar', 'baz': 42},
        'a_nested_collection_argument': {1: ['foo'], '2': ['bar', 'baz'], 3: ['qux']}
    }
    cli_args = CLIArgs(fake_args)

    assert cli_args == fake_args
    # Is it truly immutable?

# Generated at 2022-06-13 16:04:02.596618
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'foo': 1,
                 'bar': [1, 2, 3],
                 'baz': {'baz1': 1, 'baz2': 2}}

    test_immutable_dict = CLIArgs(test_dict)
    assert isinstance(test_immutable_dict, ImmutableDict)
    assert test_immutable_dict['foo'] == 1
    assert test_immutable_dict['bar'] == (1, 2, 3)
    assert test_immutable_dict['baz'] == {'baz1': 1, 'baz2': 2}

# Generated at 2022-06-13 16:04:11.077154
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class Globals:
        def __init__(self):
            self.ROOT_PATH = 'ROOT_PATH'
            self.MODULE_PATH = 'MODULE_PATH'
            self.COLLECTION_PATHS = 'COLLECTION_PATHS'
            self.ANSIBLE_CONFIG = 'ANSIBLE_CONFIG'
            self.DEVEL_CONFIG_FILE = 'DEVEL_CONFIG_FILE'
            self.KEEP_REMOTE_FILES = False
            self.REMOTE_MULTIPLEX = 'REMOTE_MULTIPLEX'
            self.PASSWORD = 'PASSWORD'
            self.PRIVATE_DATA_DIR = 'PRIVATE_DATA_DIR'

# Generated at 2022-06-13 16:04:22.859681
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    from ansible import context, constants as C
    from ansible.cli.arguments import option_helpers as opt_help

    display = Display()

    # we have to parse args to create the display object
    # since the CLI code reads it and sets up the plugin
    # paths
    parser = opt_help.create_parser(module_name='test', desc='test parser')
    options = parser.parse_args([])[0]
    context.CLIARGS = CLIArgs.from_options(options)

    # To test this we need to create a class and see if it has access
    # to the data created by context.CLIARGS
    # To do that we need to modify how context.CLIARGS is set.

    # So that context.CLIARGS is not set twice

# Generated at 2022-06-13 16:04:24.775357
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(_ABCSingleton):
        pass

    assert TestSingleton() is TestSingleton()

# Generated at 2022-06-13 16:04:29.784188
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import GlobalCLIArgs
    try:
        GlobalCLIArgs.__new__(GlobalCLIArgs)
        assert False, "Second instantiation of GlobalCLIArgs should raise an exception"
    except TypeError:
        pass

# Generated at 2022-06-13 16:04:31.249813
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs == GlobalCLIArgs()

# Generated at 2022-06-13 16:04:32.096594
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    a = _ABCSingleton()

# Generated at 2022-06-13 16:04:45.079842
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from collections import Mapping, Sequence
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes

    # Check that the constructor works as expected
    class D1(dict):
        pass

    class D2(dict):
        def __init__(self, value):
            self.value = value

    d1 = CLIArgs(D1(a=1))
    assert isinstance(d1, Mapping)
    assert isinstance(d1, ImmutableDict)

    # A dict subclass with a custom __init__ is not immutable
    d2 = CLIArgs(D2(1))
    assert isinstance(d2, Mapping)
    assert not isinstance(d2, ImmutableDict)
    assert d2.value == 1
    assert isinstance

# Generated at 2022-06-13 16:04:50.366063
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = type('options', (object,), {'a': 'b', 'c': 'd'})

    ca = CLIArgs(vars(options))
    assert(ca['a'] == 'b')
    assert(ca['c'] == 'd')
    assert(len(ca) == 2)

# Generated at 2022-06-13 16:04:51.476595
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    pass


# Generated at 2022-06-13 16:04:53.163794
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(metaclass=_ABCSingleton):
        def __init__(self):
            pass
    class Y(X):
        def __init__(self):
            pass
    assert Y() is Y()

# Generated at 2022-06-13 16:04:55.696575
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options():
        def __init__(self):
            self.check = False
    opt = Options()
    args = GlobalCLIArgs.from_options(opt)
    assert args['check'] == False

# Generated at 2022-06-13 16:05:01.598622
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Bar(object):
        __metaclass__ = _ABCSingleton

    assert issubclass(Bar, object)
    assert issubclass(Bar, Singleton)
    assert issubclass(Bar, ABCMeta)
    assert Bar('spam') is Bar('spam')
    assert Bar('spam') is not Bar('eggs')
    assert Bar('spam') is Bar.__call__('spam')
    assert Bar('spam') is not Bar.__call__('eggs')
    assert not Bar.__new__(Bar)
    assert not Bar('spam').__new__(Bar)

# Generated at 2022-06-13 16:05:05.521350
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object, metaclass=_ABCSingleton):
        pass
    class B(object, metaclass=_ABCSingleton):
        pass
    assert A is B
    assert A() is A()
    assert A() == A()



# Generated at 2022-06-13 16:05:09.901314
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    global ABCSingleton
    ABCSingleton = _ABCSingleton('ABCSingleton', (object, ), {})

    class TestSingleton(_ABCSingleton):
        pass

    class TestSingletonSubclass(TestSingleton):
        pass

    assert TestSingleton() is TestSingleton()
    assert TestSingletonSubclass() is TestSingletonSubclass()

# Generated at 2022-06-13 16:05:19.869055
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test the default case
    mapping = {'a': 1, 'b': 2}
    cli_args = CLIArgs(mapping)
    assert cli_args.a == cli_args.b == None
    assert cli_args['a'] == cli_args['b'] == None
    cli_args['b'] = 2
    cli_args['a'] = 1
    assert cli_args.a == cli_args.b == None
    assert cli_args['a'] == cli_args['b'] == None

    # test the case that the key's value is a dict
    mapping = {'c': 3, 'd': {'e': 4}}
    cli_args = CLIArgs(mapping)
    assert cli_args.c == cli_args['c'] == None
   

# Generated at 2022-06-13 16:05:29.447429
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'a': 1, 'b': 'foo', 'c': [1, 2, 3], 'd': {'1': 1, '2': 2}}
    cli_args = CLIArgs(args)
    assert cli_args == args
    assert cli_args is not args
    assert cli_args['a'] == 1
    assert cli_args['b'] == 'foo'
    assert cli_args['c'] == [1, 2, 3]
    assert cli_args['d'] == {'1': 1, '2': 2}

    global_cli_args = GlobalCLIArgs(args)
    assert cli_args == global_cli_args
    assert cli_args is not global_cli_args


# Generated at 2022-06-13 16:05:43.151138
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonABCMeta(object):
        __metaclass__ = _ABCSingleton

    assert SingletonABCMeta.__isabstractmethod__(SingletonABCMeta.__init__)

# Generated at 2022-06-13 16:05:50.161916
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import copy

    x = ImmutableDict({'a': 'hello', 'b': ['world', 2, 3], 'c': {'d': 4}, 'e': {'f', 'g', 'h'}})
    a = CLIArgs(x)
    assert a == x
    b = copy.deepcopy(a)
    assert a == b
    assert a is not b

    assert isinstance(a, ImmutableDict)
    assert isinstance(a, Mapping)
    assert isinstance(a['b'], tuple)
    assert isinstance(a['c'], ImmutableDict)
    assert isinstance(a['e'], frozenset)



# Generated at 2022-06-13 16:06:01.365763
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SubclassWithABCMetaclass(object):
        __metaclass__ = _ABCSingleton
    class SubclassWithABCABCMeta(object):
        __metaclass__ = ABCMeta
    class SubclassWithABCABCMetaAndSingleton(object):
        __metaclass__ = _ABCSingleton

    assert len(SubclassWithABCMetaclass.__mro__) == 3
    assert _ABCSingleton in SubclassWithABCMetaclass.__mro__
    assert ABCMeta in SubclassWithABCMetaclass.__mro__

    assert len(SubclassWithABCABCMeta.__mro__) == 3
    assert _ABCSingleton in SubclassWithABCABCMeta.__mro__
    assert ABCMeta in SubclassWithABCABCMeta.__mro__


# Generated at 2022-06-13 16:06:04.948003
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    globalcliargs = GlobalCLIArgs()
    assert isinstance(globalcliargs, GlobalCLIArgs)

# Generated at 2022-06-13 16:06:10.491899
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Unit test for constructor of class _ABCSingleton
    """
    class One(with_metaclass(_ABCSingleton, object)):
        pass

    class Two(with_metaclass(_ABCSingleton, object)):
        pass

    assert isinstance(One(), One)
    assert not isinstance(One(), Two)

# Generated at 2022-06-13 16:06:15.485178
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass
    class Bar(_ABCSingleton):
        pass
    f1 = Foo()
    f2 = Foo()
    b1 = Bar()
    b2 = Bar()
    assert f1 is f2
    assert b1 is b2
    assert f1 is not b1

# Unit test that checks GlobalCLIArgs is a singleton

# Generated at 2022-06-13 16:06:21.982787
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Make sure that _ABCSingleton works as expected by calling the constructor
    """
    class Foo(object):
        __metaclass__ = _ABCSingleton

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    assert Foo() is Foo()
    assert Bar() is Bar()
    assert Baz() is Baz()
    assert Foo() is not Bar() and Bar() is not Baz() and Baz() is not Foo()

# Generated at 2022-06-13 16:06:29.769484
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import GlobalCLIArgs
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six import PY3

    args = GlobalCLIArgs()
    args.add_args = {'foo1': {'bar1': 'baz1'}}

    assert args.add_args == {'foo1': {'bar1': 'baz1'}}

    if PY2:
        assert isinstance(args.add_args, dict)
    if PY3:
        assert isinstance(args.add_args, ImmutableDict)

    # Test the singleton aspect
    args2 = GlobalCLIArgs()
    assert args2.add_args == {'foo1': {'bar1': 'baz1'}}

# Generated at 2022-06-13 16:06:35.456558
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(metaclass=_ABCSingleton):
        def __init__(self, arg):
            self.arg = arg
        def __str__(self):
            return str(self.arg)

    class Y(X):
        def __init__(self):
            super(Y, self).__init__("foo")

    assert str(X("bar")) == "bar"
    assert str(Y()) == "foo"

# Generated at 2022-06-13 16:06:37.722974
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    display = Display()
    args = GlobalCLIArgs.from_options(display.options)

# Generated at 2022-06-13 16:07:00.302738
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:07:06.152448
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLIArgs(_make_immutable({'a':1, 'b':{'c':2, 'd':[4,5,6]}, 'd':set([1,2,3]), 'e':(6,7,8)}))
    CLIArgs(_make_immutable({'a':1}))
    CLIArgs(_make_immutable(dict(a=1)))

# Generated at 2022-06-13 16:07:11.426243
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_args = {'foo': {'bar': 'baz'}, 'qux': ['quux']}
    test_args = CLIArgs(cli_args)
    assert isinstance(test_args, ImmutableDict)
    assert isinstance(test_args['foo'], ImmutableDict)
    assert isinstance(test_args['qux'], tuple)



# Generated at 2022-06-13 16:07:15.746974
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'test_dict': {'test_int': 1, 'test_str': 'test_str', 'test_list': [1, 'test_str', b'test_bytes']}}
    cli_args = CLIArgs(test_dict)

    assert isinstance(cli_args['test_dict'], ImmutableDict)
    assert isinstance(cli_args['test_dict']['test_list'], tuple)
    assert isinstance(cli_args['test_dict']['test_list'][2], binary_type)

# Generated at 2022-06-13 16:07:20.492182
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = dict(a=1, b=dict(c=[1, 2, 3], d=[dict(e=1, f=[1, 2, 3])]))
    g = GlobalCLIArgs(args)

    assert g.a == 1
    assert isinstance(g.b, ImmutableDict)
    assert g.b.c == (1, 2, 3)
    assert isinstance(g.b.d, tuple)
    assert isinstance(g.b.d[0], ImmutableDict)
    assert g.b.d[0].e == 1
    assert g.b.d[0].f == (1, 2, 3)

# Generated at 2022-06-13 16:07:23.303476
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs({'a1': 'b1'})
    assert a['a1'] == 'b1'

    a['a1'] = 'b2'
    assert a['a1'] == 'b1'

# Generated at 2022-06-13 16:07:26.871409
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        'foo': 'bar',
        'baz': ['a', 'b'],
        'biz': 'bout',
    }
    args = CLIArgs(mapping)
    assert args['foo'] == 'bar'
    assert args['baz'] == ('a', 'b')
    assert 'biz' in args
    assert len(args) == 3


# Generated at 2022-06-13 16:07:31.659941
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class options(object):
        foo = 'bar'

    global_cli_args = GlobalCLIArgs.from_options(options)
    assert global_cli_args['foo'] == 'bar'
    assert isinstance(global_cli_args, CLIArgs)
    assert isinstance(global_cli_args, ImmutableDict)

# Generated at 2022-06-13 16:07:39.244082
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar', 'baz': {'quux': {'wibble': 'wubble'}}, 'numbers': [1, 2, 3, 4]})
    assert args['foo'] == 'bar'
    assert args['baz']['quux']['wibble'] == 'wubble'
    assert args['numbers'][3] == 4

    # Testing for immutability
    try:
        args['baz']['quux']['wibble'] = 'frodo'
    except TypeError:
        pass
    else:
        assert False, "Expected a TypeError, got none"

# Generated at 2022-06-13 16:07:42.001612
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    new_dict = {'some': 'dict'}
    cli_args = CLIArgs(new_dict)
    assert cli_args['some'] == 'dict'
    cli_args['some'] = 'newdict'
    assert cli_args['some'] == 'dict'


# Generated at 2022-06-13 16:08:34.403387
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo1(GlobalCLIArgs):
        def __init__(self, foo):
            super(Foo1, self).__init__(foo)
    class Foo2(GlobalCLIArgs):
        def __init__(self, foo):
            super(Foo2, self).__init__(foo)

    foo1 = Foo1('1')
    foo2 = Foo2('2')

    assert foo1 == foo2
    assert foo1 is foo2

# Generated at 2022-06-13 16:08:45.482025
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'one':1,
                    'two':2,
                    'three':[1, 2, {5:5}],
                    'four':{'five':5, 'six':6},
                    'seven':(7, 8),
                    'nine':{'ten':[1, 2]}})
    try:
        assert args['one'] == 1
        assert args['two'] == 2
    except KeyError:
        assert 0, "KeyError thrown on valid keys"

    try:
        bad = args['bad']
        assert 0, "KeyError not thrown on invalid keys"
    except KeyError:
        pass

    try:
        args['one'] = 1
        assert 0, "TypeError not thrown on assignment"
    except TypeError:
        pass


# Generated at 2022-06-13 16:08:47.930522
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass

    Test()
    Test()
    Test()

# Generated at 2022-06-13 16:08:58.905110
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    for mapping in [
        {'test0': 'test0'},
        {'test1': 'test1', 'test2': 'test2'},
        {'test1': 'test1', 'test2': {'test3': 'test3'}},
        {'test1': 'test1', 'test2': {'test3': {'test4': 'test4'}}},
        {'test1': 'test1', 'test2': {'test3': [{'test4': 'test4'}]}},
        {'test1': 'test1', 'test2': [{'test3': [{'test4': 'test4'}]}]},
    ]:
        # Ensure that we get the same immutable types back
        cli_args = CLIArgs(mapping)

# Generated at 2022-06-13 16:09:00.346840
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    mapping = {'x': [1,2,3]}
    GlobalCLIArgs(mapping)

# Generated at 2022-06-13 16:09:02.521200
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({})
    GlobalCLIArgs(ImmutableDict({
        'a': 'b',
        'c': 'd'
    }))

# Generated at 2022-06-13 16:09:09.275015
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.constants as C
    from ansible.cli import CLI
    from ansible.utils.display import Display
    display = Display()
    # Remove all the variables in an environment before loading it
    display.display(dict(C.config.settings), color='blue')
    cli = CLI(args=[])
    cli.parse()
    display.display(vars(cli.args), color='blue')
    GlobalCLIArgs.from_options(cli.args)

# Generated at 2022-06-13 16:09:18.133608
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:09:26.347164
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Unit test for CLIArgs constructor
    test_input = {
        'a': 'hello',
        'b': {
            'c': 'bye',
            'd': [1, 2, 3, 4]
        }
    }
    ca = CLIArgs(test_input)
    assert ca['a'] == 'hello'
    assert ca['b'] == {'c': 'bye', 'd': (1, 2, 3, 4)}
    assert ca['b']['d'] == (1, 2, 3, 4)
    assert ca['b']['d'][3] == 4

