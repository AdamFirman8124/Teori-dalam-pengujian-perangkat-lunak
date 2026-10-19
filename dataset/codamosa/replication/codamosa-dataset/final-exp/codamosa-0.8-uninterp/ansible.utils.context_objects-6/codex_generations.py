

# Generated at 2022-06-13 15:59:37.110145
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    # Make sure we can make a copy of itself
    my_GlobalCLIArgs = GlobalCLIArgs({})
    type(my_GlobalCLIArgs)
    
    # Make sure we can't change it
    with pytest.raises(TypeError):
        my_GlobalCLIArgs['foo'] = 'bar'

# Generated at 2022-06-13 15:59:39.500782
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class ABCSingleton(object):
        pass

    @add_metaclass(_ABCSingleton)
    class A(ABCSingleton):
        pass

    @add_metaclass(_ABCSingleton)
    class B(A):
        pass

# Generated at 2022-06-13 15:59:45.439768
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class TestClass(object):
        __metaclass__ = _ABCSingleton

    class TestClass2(object):
        __metaclass__ = _ABCSingleton

    assert TestClass() is TestClass()
    assert TestClass2() is TestClass2()
    assert TestClass() is not TestClass2()

# Generated at 2022-06-13 15:59:47.381203
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class C(with_metaclass(_ABCSingleton)):
        pass
    assert C() == C()

# Generated at 2022-06-13 15:59:54.946417
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    import unittest

    class TestClass(metaclass=_ABCSingleton):
        pass

    class DuplicateTestClass(TestClass):
        pass

    class TestCLIArgs(unittest.TestCase):
        def test1__ABCSingleton_singleton_type(self):
            test1 = TestClass()
            test2 = TestClass()
            self.assertEqual(test1, test2)

        def test2__ABCSingleton_singleton_type(self):
            test1 = DuplicateTestClass()
            test2 = DuplicateTestClass()
            self.assertEqual(test1, test2)

    import doctest
    doctest.testmod()

    unittest.main()

# Generated at 2022-06-13 15:59:55.908461
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs.instance() == GlobalCLIArgs.instance()

# Generated at 2022-06-13 16:00:01.317447
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        'k1': 'v1',
        'k2': [1, 2, 3],
        'k3': (1, 2, 3),
        'k4': {
            'k5': 'v2',
            'k6': [4, 5, 6],
            'k7': (4, 5, 6)
        }
    }
    test_cli_args = CLIArgs(test_dict)
    for key in test_dict:
        assert key in test_cli_args
    assert isinstance(test_cli_args['k1'], text_type)
    assert isinstance(test_cli_args['k2'], tuple)
    assert isinstance(test_cli_args['k3'], tuple)

# Generated at 2022-06-13 16:00:03.941316
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        def __init__(self):
            pass
    a = A()
    a = A()
    assert a is not False

# Generated at 2022-06-13 16:00:11.930692
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    opt = Options(connection='local', module_path=['/usr/share/ansible/'], forks=10, become_method='sudo', become_user='root', check=False, diff=False, extra_vars=[])
    gargs = GlobalCLIArgs.from_options(opt)

    # We do not modify the representation of the extra_vars.
    # extra_vars should not be a collection, but rather a direct mapping to the value
    # the user passed in.
    assert 'extra_vars' not in gargs
    assert gargs['become_method'] == 'sudo'

# Generated at 2022-06-13 16:00:13.465763
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.utils.parser import Parser

    display = Display()
    parser = Parser(display)
    options = parser.parse()
    GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:00:24.668682
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    d = {
        'foo': 'bar',
        'bar': AnsibleVaultEncryptedUnicode('test'),
        'baz': {
            'test': 1,
            'test2': AnsibleVaultEncryptedUnicode('test2'),
        },
        'rofl': [
            AnsibleVaultEncryptedUnicode('test3'),
            AnsibleVaultEncryptedUnicode('test4'),
        ],
        'zomg': set([
            'test5',
            AnsibleVaultEncryptedUnicode('test6'),
        ]),
    }

    a = CLIArgs(d)

    # Test foo
    assert a.foo == 'bar'

# Generated at 2022-06-13 16:00:26.351878
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # use "from_options" static method to populate it
    foo = GlobalCLIArgs.from_options
    foo({})
    # use "as_singleton" method to retrieve it
    foo = GlobalCLIArgs.as_singleton
    foo

# Generated at 2022-06-13 16:00:31.462113
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestClass(object):
        # pylint: disable=no-self-use,unused-argument
        def __init__(self, arg):
            arg.test()

    class _TestSingle(_TestClass, metaclass=_ABCSingleton):
        pass

    _TestSingle('item')
    _TestSingle('item2')
    assert _TestSingle('item') is _TestSingle('item2')



# Generated at 2022-06-13 16:00:34.219832
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(_ABCSingleton, ABCMeta)
    assert issubclass(_ABCSingleton, Singleton)

# Generated at 2022-06-13 16:00:42.333173
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Make sure _ABCSingleton metaclass works as intended"""
    class TestABCMeta(object):
        """This class is an ABCMeta so we know _ABCSingleton works as intended"""
        __metaclass__ = _ABCSingleton
    class TestNoABCMeta(object):
        """This class is not an ABCMeta so we know _ABCSingleton works as intended"""
        pass

    assert issubclass(TestABCMeta, ABCMeta)
    assert issubclass(TestABCMeta, _ABCSingleton)
    assert isinstance(TestABCMeta, ABCMeta)
    assert isinstance(TestABCMeta, _ABCSingleton)
    assert isinstance(TestABCMeta(), ABCMeta)
    assert isinstance(TestABCMeta(), _ABCSingleton)

    assert not issubclass(TestNoABCMeta, ABCMeta)

# Generated at 2022-06-13 16:00:47.906865
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import inspect
    try:
        import configparser
    except ImportError:
        import ConfigParser as configparser

    test_dict = {
        "foo": 1,
        "bar": 2,
        "baz": [3, 4, 5],
        "qux": {
            "quux": {"corge": True},
            "grault": ["garply", "waldo"],
        },
    }
    immutable_dict = CLIArgs(test_dict)

    assert isinstance(immutable_dict, ImmutableDict)
    assert inspect.isclass(CLIArgs)



# Generated at 2022-06-13 16:01:00.002066
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
    output = CLIArgs({'data': data,'data1': {'data2': {'data3': data}}})

# Generated at 2022-06-13 16:01:05.959612
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonTest(object):
        __metaclass__ = _ABCSingleton
        pass
    class ABCSingletonTestSubclass(ABCSingletonTest):
        pass

    # Create the first instance of ABCSingletonTest
    a = ABCSingletonTest()
    # Create a second instance of ABCSingletonTest
    b = ABCSingletonTest()

    # Make sure they are the same instance
    assert a is b

    # Create a subclass instance
    c = ABCSingletonTestSubclass()

    assert a is c
    assert b is c

# Generated at 2022-06-13 16:01:11.278170
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({"hello": "world", "alpha": {"beta": "gamma"}})
    assert isinstance(args, Mapping)
    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args["alpha"], Mapping)
    assert args["alpha"]["beta"] == "gamma"



# Generated at 2022-06-13 16:01:14.285728
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca = GlobalCLIArgs.from_options(ImmutableDict({'a': 'a', 'b': 'b', 'c': 'c'}))
    assert gca['a'] == 'a'
    assert gca['b'] == 'b'
    assert gca['c'] == 'c'

# Generated at 2022-06-13 16:01:28.721592
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.module_utils.common.args import AnsibleModuleArgumentParser
    import ansible_evtx

    parser = AnsibleModuleArgumentParser(supports_check_mode=True)
    parser.add_argument('-i', '--input', required=True,
                        help='EVTX file to be processed')
    parser.add_argument('-m', '--max_events', type=int,
                        help='Max events to return at a time. Defaults to 1000')
    parser.add_argument('-t', '--time_format', default='long', choices=['long', 'iso'],
                        help='Format of timestamp to return')
    parser.add_argument('-r', '--force-removal', default='False',  type='bool',
                        help='Remove input files once processed')
   

# Generated at 2022-06-13 16:01:31.059785
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        pass
    class B(_ABCSingleton):
        pass
    assert A() is A()
    assert A() is not B()
    assert B() is B()



# Generated at 2022-06-13 16:01:32.563603
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:01:40.088692
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import argparse

    # Create a test argparse object
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store', type=int, dest='foo')
    parser.add_argument('--bar', action='store_true', dest='bar')

    # Create a test dictionary
    my_dict = {'foo': 42, 'bar': True, 'spam': 'eggs'}

    # Create a test list
    my_list = [1, 1, 2, 3, 5, 8]

    # Turn the dictionary into a mapping object
    my_mapping = parser.parse_args('--foo 42 --bar'.split())

    # Turn the list into a sequence object
    my_sequence = my_list[:]

    # Turn the dictionary into a set object

# Generated at 2022-06-13 16:01:45.546242
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    parser.add_argument('--foo')
    opts = parser.parse_args(sys.argv[1:])
    opts.verbosity = 10
    opts.foo = [1, 2, 3, 4]

    GlobalCLIArgs.from_options(opts)



# Generated at 2022-06-13 16:01:48.335432
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object, metaclass=_ABCSingleton):
        pass

    try:
        class B(A):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError("`class B` should not be allowed since it does not override A")

# Generated at 2022-06-13 16:01:52.152656
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton
    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2, 'Singleton classes do not have only one instance'

# Generated at 2022-06-13 16:01:57.308889
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    @add_metaclass(_ABCSingleton)
    class A(object):
        pass
    assert A() is A()

    @add_metaclass(_ABCSingleton)
    class A(object):
        def __init__(self, foo):
            self.foo = foo
    assert A(1) is A(1)
    assert A(1).foo == 1

# Generated at 2022-06-13 16:02:02.766632
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test that class GlobalCLIArgs is actually a singleton as it is intended to be.
    """
    args = {'one': 1, 'two': 2}

    # Call the constructor with our args
    GlobalCLIArgs(args)

    # Call the constructor again with different args,
    # but the object returned should be the same as the original
    different_args = {'foo': 'bar', 'baz': 'quux'}
    different_instance = GlobalCLIArgs(different_args)
    assert id(different_instance) == id(GlobalCLIArgs())



# Generated at 2022-06-13 16:02:07.385707
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Make sure that we cannot use GlobalCLIArgs as a normal dictionary, but we can use it as a
    # ContextManager
    args = GlobalCLIArgs({'foo': 'bar'})
    assert 'foo' in args
    try:
        args['foo'] = 'bar'
        assert False
    except TypeError:
        assert True

    with GlobalCLIArgs({'foo': 'bar'}) as args:
        assert 'foo' in args

# Generated at 2022-06-13 16:02:12.768031
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs.from_options(object())


# Generated at 2022-06-13 16:02:20.015189
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        def __init__(self, a):
            self.a = a

        def __repr__(self):
            return 'Foo({})'.format(self.a)

    class Bar(_ABCSingleton):
        def __init__(self, a):
            self.a = a

        def __repr__(self):
            return 'Bar({})'.format(self.a)

    assert Foo(1) is Foo(2)
    assert Foo(1) is not Bar(1)
    assert Foo(1) is not Foo(1)
    assert Bar(1) is Bar(1)
    assert Bar(1) is not Foo(1)
    assert Bar(1) is not Bar(2)

# Generated at 2022-06-13 16:02:26.025148
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    global_vars = CLIArgs.from_options(GlobalCLIArgs.instance())
    assert isinstance(global_vars, ImmutableDict)
    assert isinstance(global_vars, Mapping)
    assert len(global_vars) > 1

    temp_args = CLIArgs({'test': 'immutable', 'list': [1, 2 ,3, 'four'],
                         'dict': {'a': 'b', 'b': 'c'}})
    assert isinstance(temp_args, Mapping)
    assert isinstance(temp_args, ImmutableDict)
    assert isinstance(temp_args.get('dict'), ImmutableDict)
    assert isinstance(temp_args.get('dict'), Mapping)
    assert isinstance(temp_args.get('list'), tuple)

# Generated at 2022-06-13 16:02:28.294924
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
        pass

    class B(A):
        pass

    class C(A):
        pass

    assert B() is C()
    assert B() is B()

# Generated at 2022-06-13 16:02:33.203313
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, x):
            self.x = x

    assert X(x=1) is X(x=2)

if __name__ == '__main__':
    test__ABCSingleton()

# Generated at 2022-06-13 16:02:41.662828
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'
    assert args.get('bar') is None
    with pytest.raises(KeyError):
        args['bar']
    with pytest.raises(TypeError):
        # Can't add a new key
        args['bar'] = 'foo'
    assert len(args) == 1
    assert list(args) == ['foo']
    assert list(args.keys()) == ['foo']
    assert list(args.values()) == ['bar']
    assert list(args.items()) == [('foo', 'bar')]

# Generated at 2022-06-13 16:02:48.036492
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Create two subclasses of _ABCSingleton and make sure that we get the same instances back
    """
    class _TestClass1(object, metaclass=_ABCSingleton):
        pass

    class _TestClass2(object, metaclass=_ABCSingleton):
        pass

    class1 = _TestClass1()
    class2 = _TestClass2()

    assert class1 is class2

    class3 = _TestClass1()
    class4 = _TestClass2()

    assert class3 is class4
    assert class1 is class2
    assert class3 is class4



# Generated at 2022-06-13 16:02:51.951533
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Opts(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)

    options = Opts(foo=dict(wibble=3))
    GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:02:59.852791
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({'a': '1'}) == {'a': '1'}

# Generated at 2022-06-13 16:03:07.848124
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # pylint: disable=unused-variable,unused-argument
    def test_constructor(self, cls, options, expected):

        actual = cls.from_options(options)
        assert actual
        assert isinstance(actual, ImmutableDict)
        assert actual == expected

        for key, value in actual.items():
            if isinstance(value, Container):
                assert isinstance(value, ImmutableDict)
                for subkey, subvalue in value.items():
                    assert isinstance(subvalue, (text_type, binary_type))
            else:
                assert isinstance(value, (text_type, binary_type))

    # pylint: enable=unused-variable,unused-argument

    import argparse
    parser = argparse.ArgumentParser()

# Generated at 2022-06-13 16:03:24.416559
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = ImmutableDict({'ignore-errors': True, 'verbosity': 1})
    assert CLIArgs(options) == options
    options = ImmutableDict({'ignore-errors': True, 'verbosity': 1, 'run-validate': True})
    assert CLIArgs(options) == options

    options = ImmutableDict({'ignore-errors': True, 'verbosity': 1, 'tags': ['foo', 'bar']})
    expected_options = ImmutableDict({'ignore-errors': True, 'verbosity': 1, 'tags': ('foo', 'bar')})
    assert CLIArgs(options) == expected_options

    options = ImmutableDict({'ignore-errors': True, 'verbosity': 1, 'tags': set(['foo', 'bar'])})

# Generated at 2022-06-13 16:03:26.499438
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonMetaB(Container, _ABCSingleton):
        pass

    a = SingletonMetaB()
    b = SingletonMetaB()
    assert a is b

# Generated at 2022-06-13 16:03:38.260469
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from argparse import Namespace

# Generated at 2022-06-13 16:03:45.952626
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import copy
    import collections
    # make a mapping for a cli args object
    mapping = {
        'a': -1,
        'b': 8,
        'c': [3, 9],
        'd': {'e': 4},
        'f': set([0, 1]),
        'g': collections.OrderedDict([(0, 'a'), (1, 'b')]),
    }
    # create the object
    cli_args = CLIArgs(mapping)
    # make sure we only got immutable types
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args['d'], ImmutableDict)
    assert isinstance(cli_args['c'], tuple)
    assert isinstance(cli_args['f'], frozenset)

# Generated at 2022-06-13 16:03:51.839456
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Unittest for empty dictionary as inputs
    input_dict = {}
    expected_result = {}
    result = CLIArgs(input_dict)
    assert result == expected_result

    # Unittest for non-empty dictionary
    input_dict = {'a': 'abc', 'b': 'def'}
    expected_result = {'a': 'abc', 'b': 'def'}
    result = CLIArgs(input_dict)
    assert result == expected_result

if __name__ == '__main__':
    test_CLIArgs()

# Generated at 2022-06-13 16:03:54.713397
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar'})
    assert isinstance(args, ImmutableDict)
    assert args['foo'] == 'bar'


# Generated at 2022-06-13 16:03:56.787443
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonTest(metaclass=_ABCSingleton):
        pass

    SingletonTest()
    SingletonTest()

# Generated at 2022-06-13 16:04:07.548198
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Ensure the CLIArgs is immutable and the constructor actually runs recursively.
    nested_dict = {
        'a': {
            '1': 1,
            '2': 2,
            '3': 3,
        },
        'b': {
            '1': 1,
            '2': 2,
            '3': 3,
        },
        'c': {
            '1': 1,
            '2': 2,
            '3': 3,
        }
    }
    nested_dict_from_cli_args = CLIArgs(nested_dict)
    # We don't care about the ImmutableDict implementation that were using, just that it is immutable
    assert(nested_dict != nested_dict_from_cli_args)

# Generated at 2022-06-13 16:04:13.897493
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': 1,
               'b': [1, 2, 3],
               'c': {'one': 1, 'two': 2}}
    expected = ImmutableDict({'a': 1,
                              'b': (1, 2, 3),
                              'c': ImmutableDict({'one': 1, 'two': 2})})

    cli_args = CLIArgs(mapping)

    assert cli_args == expected

# Generated at 2022-06-13 16:04:25.267702
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Verify that the constructor does what we expect
    """
    from collections import OrderedDict
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import OrderedDict

    arguments = OrderedDict()
    arguments['bare_var_single'] = "bar"
    arguments['bare_var_list'] = ["a", "b", "c"]

    arguments['bare_var_dict'] = {"a": "b"}

    if PY3:
        arguments['bare_var_set'] = {'a', 'b', 'c'}

    arguments['bare_var_tuple'] = (1, 2, 3)

    cliargv = CLIArgs(arguments)

# Generated at 2022-06-13 16:04:42.874617
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Instantiate the class
    GlobalCLIArgs.instance({'connection': 'local'})

# Generated at 2022-06-13 16:04:50.683481
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.parsing.mod_args import ModuleArgsParser

    display = Display()
    options = ModuleArgsParser(None, display).parse()
    global_cli_args = GlobalCLIArgs(vars(options))
    assert isinstance(global_cli_args, ImmutableDict)
    assert global_cli_args == vars(options)
    assert global_cli_args == GlobalCLIArgs(vars(options))

# Generated at 2022-06-13 16:04:55.368852
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys
    import tempfile
    import unittest

    test_file = tempfile.NamedTemporaryFile()
    test_file.write("""[defaults]\n""")
    test_file.seek(0)

    test_args = [
        # test_dir = tempdir
        test_file.name,
        '-e', 'foo=bar',
        '-e', 'baz=qux',
        '-c',
        '-i', 'localhost,'
    ]


# Generated at 2022-06-13 16:05:02.577647
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Test that constructor works properly
    args = GlobalCLIArgs({'a':1, 'b':2, 'c':3})
    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args['a'], int)
    assert args['a'] == 1
    assert isinstance(args['b'], int)
    assert args['b'] == 2
    assert isinstance(args['c'], int)
    assert args['c'] == 3

    # Test that we cannot modify the data
    try:
        args['a'] = 10
        raise Exception("Dict should be immutable")
    except TypeError:
        pass

    try:
        args['d'] = 4
        raise Exception("Dict should be immutable")
    except TypeError:
        pass

# Generated at 2022-06-13 16:05:06.159687
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class E(object):
        __metaclass__ = _ABCSingleton

    class F(object):
        __metaclass__ = _ABCSingleton

    assert E() == F()

# Generated at 2022-06-13 16:05:12.248268
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Unit test for CLIArgs constructor
    for config_file in ('/etc/ansible/ansible.cfg', './ansible.cfg'):
        for verbosity in (0, 1, 2, 3, 4, 5):
            cli_args = CLIArgs.from_options(CLIOptions(config_file=config_file, verbosity=verbosity))
            assert cli_args.get('config_file') == config_file
            assert cli_args.get('verbosity') == verbosity



# Generated at 2022-06-13 16:05:16.556627
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    assert issubclass(A, B)
    assert issubclass(B, A)

    class C(A, B):
        pass

    assert issubclass(C, A)
    assert issubclass(C, B)

# Generated at 2022-06-13 16:05:27.307300
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class FakeOptions(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # Test an option with a dictionary
    fake_options = FakeOptions(a_dict=dict(a=1, b=2))
    assert isinstance(GlobalCLIArgs.from_options(fake_options), CLIArgs)
    assert isinstance(GlobalCLIArgs.from_options(fake_options)["a_dict"], ImmutableDict)

    # Test an option with a list
    fake_options = FakeOptions(a_list=[1, 2, 3])
    assert isinstance(GlobalCLIArgs.from_options(fake_options), CLIArgs)
    assert isinstance(GlobalCLIArgs.from_options(fake_options)["a_list"], tuple)

    # Test an option with

# Generated at 2022-06-13 16:05:38.447762
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {}
    options = GlobalCLIArgs.from_options(options=args)
    assert options == {}
    args = {'a': 1, 'b': 2}
    options = GlobalCLIArgs.from_options(options=args)
    assert options == {}
    args = {'a': 'hi', 'b': [1, 2, 3], 'c': {'x': 1, 'y': 2, 'z': 3}, 'd': list()}
    options = GlobalCLIArgs.from_options(options=args)
    assert options == {
        'a': 'hi',
        'b': (1, 2, 3),
        'c': ImmutableDict({'x': 1, 'y': 2, 'z': 3}),
        'd': tuple()
    }

# Generated at 2022-06-13 16:05:39.746855
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs.from_options(None)


# Generated at 2022-06-13 16:06:20.102345
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli.arguments import optparse_helpers as opt_help
    from ansible.parsing.splitter import parse_kv
    import tempfile


# Generated at 2022-06-13 16:06:28.669424
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    The constructor for _ABCSingleton should be equivalent to the constructor for Object
    """
    class DummyClass(object):
        def __init__(self):
            self.attr = 0
    assert issubclass(DummyClass, object)
    assert DummyClass().attr == 0

    class DerivedClass(_ABCSingleton):
        def __init__(self):
            self.attr = 0
    assert issubclass(DerivedClass, object)
    assert DerivedClass().attr == 0
    assert DerivedClass() is DerivedClass()

# Generated at 2022-06-13 16:06:33.576720
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mydict = {"test": "value"}
    mydict = _make_immutable(mydict)
    args = CLIArgs(mydict)
    assert args['test'] == 'value'
    assert isinstance(args, Mapping)
    assert not isinstance(args, MutableMapping)
    assert not isinstance(args, GlobalCLIArgs)

# Generated at 2022-06-13 16:06:42.964185
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Arrange
    nested_dict = {'key1': 'value1', 'key2': 'value2'}
    nested_list = ['value1', 'value2']
    test_dict = {'key1': 'value1', 'key2': nested_dict, 'key3': nested_list}
    expected_dict = {"key1": "value1", "key2": ImmutableDict({"key1": "value1", "key2": "value2"}),
                     "key3": ("value1", "value2")}
    expected_set = frozenset(("value1", "value2"))
    leftover_int = 123
    test_set = set()
    test_set.add(leftover_int)
    test_set.add(nested_list)

# Generated at 2022-06-13 16:06:54.500473
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options_source = {'foo': ['bar', 'baz'], 'foobar': 123, 'blarg': [1, 2, 3, 4], 'bleep': ['a', 'b', 'c', 'd', 'e']}
    options = CLIArgs.from_options(options_source)

    assert options['foo'] == ('bar', 'baz')
    assert options['foobar'] == 123
    assert options['blarg'] == (1, 2, 3, 4)
    assert options['bleep'] == ('a', 'b', 'c', 'd', 'e')
    try:
        options['foo'] = ('foo', 'bar')
        assert False
    except Exception as e:
        assert isinstance(e, TypeError)


# Generated at 2022-06-13 16:07:03.022347
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_dict = {'one': 1, 'two': 2}
    cli_args = CLIArgs(cli_dict)
    assert cli_args.one == 1
    assert cli_args.two == 2

    # Make sure that we can't modify this object
    try:
        cli_args.one = 3
        assert False
    except AttributeError:
        pass

    cli_dict = {'one': 1, 'two': 2, 'three': {'four': 4}}
    cli_args = CLIArgs(cli_dict)
    assert cli_args.one == 1
    assert cli_args.two == 2
    assert cli_args.three.four == 4

    # Make sure that we can't modify this object

# Generated at 2022-06-13 16:07:13.147475
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.module_utils.six import PY2
    from ansible.module_utils.common._collections_compat import Mapping

    mut_foo = {'foo': 'bar'}
    immut_foo = {'foo': 'bar'}

    def check_immutable(obj):
        obj['foo'] = 'baz'
        assert obj['foo'] == 'bar'
        with pytest.raises(AttributeError):
            obj.update({'foo': 'baz'})
        with pytest.raises(AttributeError):
            obj.clear()
        with pytest.raises(AttributeError):
            obj.pop('foo')
        with pytest.raises(AttributeError):
            obj.popitem()

# Generated at 2022-06-13 16:07:21.128257
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    my_args = CLIArgs({'test1': 'test1', 'test2': ['test2', 'test3'], 'test4': {'test5': 'test5'}})
    assert my_args['test1'] == 'test1'
    assert isinstance(my_args['test2'], tuple)
    assert my_args['test2'][1] == 'test3'
    assert isinstance(my_args['test4'], ImmutableDict)
    assert isinstance(my_args['test4']['test5'], ImmutableDict)

# Generated at 2022-06-13 16:07:23.267201
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options, _ = GlobalCLIArgs.parse(args=None, values=None)
    assert GlobalCLIArgs.from_options(options) is GlobalCLIArgs.from_options(options)

# Generated at 2022-06-13 16:07:24.084209
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs.from_options({}) == {}

# Generated at 2022-06-13 16:08:41.047708
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Unit test, which tests is the construction method of class GlobalCLIArgs,
    and its immutability property.

    Note:
    1) Unit test can be performed by command "python cli_args.py".
    2) If the unit test fails, it is due to the change of construct method of
    class GlobalCLIArgs.
    3) Please check the construction method of class GlobalCLIArgs, and its
    immutability property.
    """
    args = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4}}}
    args = _make_immutable(args)
    cli_args = GlobalCLIArgs(args)
    assert isinstance(cli_args, GlobalCLIArgs) is True

# Generated at 2022-06-13 16:08:45.893209
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    a = A()
    assert(type(a) == A)
    assert(a.__class__ == A)
    b = B()
    assert(type(b) == B)
    assert(b.__class__ == B)

# Generated at 2022-06-13 16:08:57.403909
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class OldABCMeta(ABCMeta):
        """This is the class used before the fix"""
        pass

    class NewABCMeta(ABCMeta):
        """This is the new class"""
        pass


    class SingletonA(Singleton):
        """For checking if the old code works"""
        pass


    class SingletonB(Singleton):
        """For checking if the new code works"""
        pass


    class SingletonC(Singleton):
        """For checking if the old code fails"""
        pass


    class SingletonD(Singleton):
        """For checking if the new code fails"""
        pass


    class A(OldABCMeta, SingletonA):
        pass


    class B(NewABCMeta, SingletonB):
        pass


    class C(OldABCMeta, SingletonC):
        pass




# Generated at 2022-06-13 16:08:59.819450
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class SingletonABC(object):
        __metaclass__ = _ABCSingleton

    # This will fail without test__ABCSingleton decorator
    SingletonABC()
    SingletonABC()

# Generated at 2022-06-13 16:09:11.010543
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    options_mock = {
        'check': True,
        'connection': 'smart',
        'diff': True,
        'extra_vars': ['key=value'],
        'module_path': '/path/to/modules',
        'start_at_task': '',
        'version': False,
        'vault_password_file': '~/.vault_pass.txt'}

    GlobalCLIArgs.from_options(options_mock)

    # Test that the passed in options object was converted to an immutable object
    assert isinstance(GlobalCLIArgs().connection, text_type)
    assert isinstance(GlobalCLIArgs().vault_password_file, text_type)
    assert isinstance(GlobalCLIArgs().extra_vars, tuple)

# Generated at 2022-06-13 16:09:18.964802
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyABCSingletonClassA(object):
        __metaclass__ = _ABCSingleton

    class MyABCSingletonClassB(object):
        __metaclass__ = _ABCSingleton

    assert MyABCSingletonClassA is MyABCSingletonClassB

    class MyABCSingletonClassC(MyABCSingletonClassB):
        pass

    assert MyABCSingletonClassC is MyABCSingletonClassB

    if not hasattr(MyABCSingletonClassC, '__abstractmethods__'):
        # This only runs in Python 2.7, not in Python 3.x, since Abstract Base Classes are only
        # a thing there, not in Python 2.7.
        class MyABCSingletonClassD(MyABCSingletonClassB):
            def abc(self):
                return "abc"

        assert MyABCSingleton

# Generated at 2022-06-13 16:09:21.822108
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        default_values = {"check_mode": False, "diff": False}
        GlobalCLIArgs.from_options(default_values)
    except Exception as e:
        assert False, 'GlobalCLIArgs constructor failed. {0}'.format(e)
    else:
        assert True

# Generated at 2022-06-13 16:09:25.818087
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args1 = {'foo': 'bar'}
    args2 = {'foo': 'bar'}

    g1 = GlobalCLIArgs(args1)
    g2 = GlobalCLIArgs(args2)

    assert id(g1) == id(g2)
    assert g1 == g2

# Generated at 2022-06-13 16:09:28.979008
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import copy
    from ansible.module_utils import basic
    from ansible.module_utils.common.vars_plugins import b_vars_plugins

    # Prevent argv from being parsed so we use defaults
    basic.AN